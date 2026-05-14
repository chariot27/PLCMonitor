import sys
import time
from pymodbus.client import ModbusTcpClient

def test_communication(ip, port, slave):
    client = ModbusTcpClient(ip, port=port, timeout=2)
    print(f"[*] Testando: IP={ip}, Porta={port}, Slave={slave}...", end=" ", flush=True)
    
    if not client.connect():
        print("FALHA (TCP)")
        return False
    
    # 1. Teste M1000
    res_m = client.read_coils(3048, count=1, device_id=slave)
    if res_m.isError():
        print(f"FALHA (Modbus Erro)")
        client.close()
        return False
    
    print(f"CONECTADO! (M1000={res_m.bits[0]})")
    
    # 2. Teste Bits X0 e X1 (Tentativa 1: Discrete Inputs 1024)
    res_x = client.read_discrete_inputs(1024, count=8, device_id=slave)
    x0 = res_x.bits[0] if not res_x.isError() else "Erro"
    x1 = res_x.bits[1] if not res_x.isError() else "Erro"
    print(f"    [INFO] Bits X (DI 1024): X0={x0}, X1={x1}")

    # 3. Teste Bits X0 e X1 (Tentativa 2: Coils 1024)
    res_x_c = client.read_coils(1024, count=8, device_id=slave)
    x0_c = res_x_c.bits[0] if not res_x_c.isError() else "Erro"
    print(f"    [INFO] Bits X (Coil 1024): X0={x0_c}")

    # 4. Teste RTC Completo
    res_rtc = client.read_holding_registers(5409, count=7, device_id=slave)
    if not res_rtc.isError():
        s, m, h = res_rtc.registers[0], res_rtc.registers[1], res_rtc.registers[2]
        dia, mes, ano = res_rtc.registers[3], res_rtc.registers[4], res_rtc.registers[6]
        print(f"    [INFO] RTC COMPLETO: {dia:02}/{mes:02}/{ano:02} {h:02}:{m:02}:{s:02}")

    # 5. Teste Encoder C251
    res_c = client.read_holding_registers(3835, count=2, device_id=slave)
    if not res_c.isError():
        val = (res_c.registers[1] << 16) | res_c.registers[0]
        if val > 0x7FFFFFFF: val -= 0x100000000
        print(f"    [INFO] ENCODER C251: {val}")
    
    client.close()
    return True

if __name__ == "__main__":
    PLC_IP = "192.168.0.10"
    test_communication(PLC_IP, 502, 1)
