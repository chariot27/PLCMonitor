import sys
import os
import grpc
import time
from concurrent import futures
from pymodbus.client import ModbusTcpClient

# Setup de caminhos
root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_path)
sys.path.append(os.path.join(root_path, "infradata"))

from infradata import modbus_wiki_pb2 as pb2
from infradata import modbus_wiki_pb2_grpc as pb2_grpc

class ModbusWikiServer(pb2_grpc.ModbusWikiServiceServicer):
    def __init__(self):
        self.default_ip = "192.168.0.10"
        self.active_slave = 1

    def StreamRegisters(self, request, context):
        print(f"[*] Monitoramento gRPC INDUSTRIAL iniciado para {self.default_ip}")
        client = ModbusTcpClient(self.default_ip, port=502, timeout=3)
        
        while context.is_active():
            if not client.connected:
                client.connect()
            
            if not client.connected:
                yield pb2.SnapshotResponse(all_ok=False, error_msg="CLP Offline")
                time.sleep(1)
                continue

            values = []
            try:
                # 1. Leitura M1000 (Status do CLP)
                res_m = client.read_coils(3048, count=1, device_id=self.active_slave)
                if not res_m.isError():
                    values.append(pb2.RegisterValue(address=3048, type=pb2.COIL, raw_value=1 if res_m.bits[0] else 0))

                # 2. Leitura X0 e X1 (Entradas Digitais)
                res_x = client.read_discrete_inputs(1024, count=8, device_id=self.active_slave)
                if not res_x.isError():
                    values.append(pb2.RegisterValue(address=1024, type=pb2.DISCRETE_INPUT, raw_value=1 if res_x.bits[0] else 0))
                    values.append(pb2.RegisterValue(address=1025, type=pb2.DISCRETE_INPUT, raw_value=1 if res_x.bits[1] else 0))

                # 3. Leitura Encoder C251 (32 bits)
                res_c = client.read_holding_registers(3835, count=2, device_id=self.active_slave)
                encoder_val = 0
                if not res_c.isError():
                    encoder_val = (res_c.registers[1] << 16) | res_c.registers[0]
                    if encoder_val > 0x7FFFFFFF: encoder_val -= 0x100000000
                    values.append(pb2.RegisterValue(address=3835, type=pb2.HOLDING_REGISTER, raw_value=encoder_val))

                # 4. Leitura RTC (D1313-D1319)
                res_rtc = client.read_holding_registers(5409, count=7, device_id=self.active_slave)
                if not res_rtc.isError():
                    for i, addr in enumerate([5409, 5410, 5411, 5412, 5413, 5414, 5415]):
                        values.append(pb2.RegisterValue(address=addr, type=pb2.HOLDING_REGISTER, raw_value=res_rtc.registers[i]))
                
                # Feedback no console do servidor
                print(f"[LIVE] RTC: {res_rtc.registers[2] if not res_rtc.isError() else '?'}:{res_rtc.registers[1] if not res_rtc.isError() else '?'}:{res_rtc.registers[0] if not res_rtc.isError() else '?'} | Encoder: {encoder_val}")

                yield pb2.SnapshotResponse(values=values, device_ip=self.default_ip, all_ok=True)
                    
            except Exception as e:
                print(f"[!] Erro no loop: {e}")
                yield pb2.SnapshotResponse(all_ok=False, error_msg=str(e))
            
            time.sleep(request.poll_interval_ms / 1000.0)
        
        client.close()

    def WriteRegister(self, request, context):
        client = ModbusTcpClient(self.default_ip, port=502, timeout=2)
        client.connect()
        try:
            if request.type == pb2.COIL:
                res = client.write_coil(request.address, bool(request.value), device_id=self.active_slave)
            else:
                res = client.write_register(request.address, int(request.value), device_id=self.active_slave)
            client.close()
            return pb2.WriteResponse(success=not res.isError())
        except Exception:
            if client: client.close()
            return pb2.WriteResponse(success=False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pb2_grpc.add_ModbusWikiServiceServicer_to_server(ModbusWikiServer(), server)
    server.add_insecure_port('[::]:50051')
    print("----------------------------------------------------------")
    print("🚀 SERVIDOR gRPC FINALIZADO COM BASE NO DIAGNÓSTICO")
    print("----------------------------------------------------------")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
