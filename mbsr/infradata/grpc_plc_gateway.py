import grpc
import time
from typing import Iterator
from domains.interfaces import IPLCGateway
from domains.models import PLCState, RTCData
from . import modbus_wiki_pb2 as pb2
from . import modbus_wiki_pb2_grpc as pb2_grpc

class GrpcPLCGateway(IPLCGateway):
    def __init__(self, host: str = "localhost", port: int = 50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.ModbusWikiServiceStub(self.channel)

    def sync_rtc(self, rtc: RTCData, device_ip: str) -> bool:
        enderecos = [5409, 5410, 5411, 5412, 5413, 5415]
        valores = [rtc.second, rtc.minute, rtc.hour, rtc.day, rtc.month, rtc.year]
        
        try:
            for addr, val in zip(enderecos, valores):
                req = pb2.WriteRequest(device_ip=device_ip, address=addr, type=pb2.HOLDING_REGISTER, value=val)
                self.stub.WriteRegister(req)
            
            # Trigger sync coil
            self.stub.WriteRegister(pb2.WriteRequest(device_ip=device_ip, address=3063, type=pb2.COIL, value=1))
            return True
        except Exception as e:
            print(f"Error syncing RTC: {e}")
            return False

    def stream_data(self, device_ip: str, interval_ms: int) -> Iterator[PLCState]:
        req = pb2.StreamRequest(config=pb2.SnapshotRequest(), poll_interval_ms=interval_ms)
        
        clicks_x0 = 0
        clicks_x1 = 0
        last_x0 = False
        last_x1 = False

        for response in self.stub.StreamRegisters(req):
            x0, x1, y0, m1000 = False, False, False, False
            c_s, c_m, c_h, c_dia, c_mes, c_ano = 0, 0, 0, 1, 1, 0
            
            for val in response.values:
                # Digital states
                if val.address in [1024, 1536] and val.raw_value == 1: x0 = True
                if val.address in [1025, 1537] and val.raw_value == 1: x1 = True
                if val.address in [1280, 1600] and val.raw_value == 1: y0 = True
                if val.address == 3048 and val.raw_value == 1: m1000 = True
                
                # RTC Registers
                if val.type == pb2.HOLDING_REGISTER:
                    if val.address == 5409: c_s = int(val.raw_value)
                    if val.address == 5410: c_m = int(val.raw_value)
                    if val.address == 5411: c_h = int(val.raw_value)
                    if val.address == 5412: c_dia = int(val.raw_value)
                    if val.address == 5413: c_mes = int(val.raw_value)
                    if val.address == 5415: c_ano = int(val.raw_value)

            # Click counting logic (Rising edge)
            if x0 and not last_x0: clicks_x0 += 1
            if x1 and not last_x1: clicks_x1 += 1
            
            last_x0 = x0
            last_x1 = x1

            rtc_data = RTCData(c_s, c_m, c_h, c_dia, c_mes, c_ano)
            
            yield PLCState(
                x0=x0, x1=x1, y0=y0, m1000=m1000,
                rtc=rtc_data,
                clicks_x0=clicks_x0,
                clicks_x1=clicks_x1,
                is_real=response.all_ok
            )
