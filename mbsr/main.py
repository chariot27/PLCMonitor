import sys
import os
import grpc
import subprocess
import time

def restart_grpc_server():
    print("[*] Reiniciando servidor gRPC...")
    
    # Tenta matar processos que estão rodando grpc_server.py usando PowerShell (mais preciso no Windows)
    kill_cmd = 'powershell "Get-Process python | Where-Object { $_.CommandLine -like \'*grpc_server.py*\' } | Stop-Process -Force"'
    subprocess.run(kill_cmd, shell=True, capture_output=True)
    
    # Aguarda um momento para liberar a porta
    time.sleep(1)
    
    # Sobe um novo servidor gRPC em uma nova janela de console
    # O script do servidor está na pasta pai (raiz do projeto)
    server_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "grpc_server.py")
    
    try:
        subprocess.Popen([sys.executable, server_script], creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("[OK] Servidor gRPC iniciado em nova janela.")
        time.sleep(2) # Aguarda inicialização
    except Exception as e:
        print(f"[!] Erro ao subir servidor gRPC: {e}")

# Adiciona o diretório atual e infradata ao path para facilitar imports internos e do gRPC
root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_path)
sys.path.append(os.path.join(root_path, "infradata"))

from infradata.grpc_plc_gateway import GrpcPLCGateway
from application.monitor_use_case import MonitorPLCUseCase
from utils.dynamic_table import DynamicConsoleTable

def main():
    # Reinicia o servidor antes de começar
    restart_grpc_server()
    
    # Configurações
    PLC_IP = "192.168.0.10"
    
    # Inicializa Infra
    gateway = GrpcPLCGateway(host="localhost", port=50051)
    
    # Inicializa Caso de Uso
    monitor_use_case = MonitorPLCUseCase(gateway)
    
    # Inicializa View (Malleable Table)
    table = DynamicConsoleTable("Log de Operação em Tempo Real - Clean Architecture")
    
    print(f"[*] Conectando ao PLC {PLC_IP} via gRPC...")
    
    try:
        # Executa o stream (Sincroniza RTC no início)
        for state in monitor_use_case.execute(PLC_IP, sync_rtc=True):
            table.update(state)
            
    except KeyboardInterrupt:
        print("\n[!] Monitoramento encerrado pelo usuário.")
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("\n[!] ERRO: Não foi possível conectar ao servidor gRPC.")
            print("    Certifique-se de que 'grpc_server.py' está rodando em localhost:50051.")
        else:
            print(f"\n[!] Erro gRPC: {e.details()}")
    except Exception as e:
        print(f"\n[!] Erro fatal: {e}")

if __name__ == "__main__":
    main()
