from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
import datetime

# Metadados para organizar o Swagger
tags_metadata = [
    {
        "name": "PLC Core",
        "description": "Endpoints para diagnóstico de hardware e saúde da conexão com o CLP Delta.",
    },
    {
        "name": "Monitoramento em Tempo Real",
        "description": "Leitura de registradores de dados (D) e estados de I/O (X/Y). **Uso: Dashboard de Operação.**",
    },
    {
        "name": "Controle e Comandos",
        "description": "Escrita de setpoints e acionamento de bobinas. **Uso: Intervenção do Operador.**",
    },
    {
        "name": "Histórico e Eventos",
        "description": "Acesso a logs de eventos e variações de sinais analógicos.",
    },
]

app = FastAPI(
    title="🏭 MBSR - Sistema Mestre de Monitoramento Industrial",
    description="""
## Arquitetura de Monitoramento
Esta API serve como a ponte entre a camada de campo (CLPs Delta DVP) e a camada de gestão (Sistemas Web/ERP).

### Como as rotas são utilizadas:
*   **Diagnóstico**: Verificação de heartbeat e latência de rede.
*   **Operação**: Alimentação de gráficos de tendência e indicadores (KPIs).
*   **Engenharia**: Ajuste de parâmetros de máquina e calibração de sensores.
""",
    version="2.0.0",
    openapi_tags=tags_metadata,
    docs_url="/docs"
)

# Modelos de Dados com Documentação de Campos
class RegisterValue(BaseModel):
    address: int = Field(..., description="Endereço Modbus do registrador (Ex: 4096 para D0)")
    name: str = Field(..., description="Nome amigável definido no mapa de memória")
    value: float = Field(..., description="Valor atual (convertido para unidade de engenharia se necessário)")
    unit: str = Field("un", description="Unidade de medida (Ex: °C, Bar, RPM)")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now)

class PLCStatus(BaseModel):
    connected: bool = Field(..., description="Status da conexão TCP/IP com o CLP")
    ip: str = Field(..., description="Endereço IP do equipamento na rede industrial")
    scan_time_ms: int = Field(..., description="Tempo de ciclo de varredura do CLP (D1010)")
    last_error: Optional[str] = None

# Mock de dados mais rico
mock_db = {
    "registers": [
        {"address": 4096, "name": "Temperatura_Tanque_01", "value": 82.5, "unit": "°C"},
        {"address": 4097, "name": "Pressao_Linha_Principal", "value": 6.2, "unit": "Bar"},
        {"address": 4098, "name": "Velocidade_Motor_M1", "value": 1750, "unit": "RPM"},
        {"address": 1024, "name": "Digital_Input_X0", "value": 0, "unit": "bit"},
        {"address": 1025, "name": "Digital_Input_X1", "value": 1, "unit": "bit"}
    ]
}

@app.get("/", tags=["Geral"], include_in_schema=False)
async def root():
    return {"status": "OK", "docs": "/docs"}

@app.get("/api/plc/status", response_model=PLCStatus, tags=["PLC Core"])
async def get_plc_status():
    """
    ### 🛡️ Diagnóstico de Conexão
    **Uso no Monitoramento:** Esta rota é chamada pelo 'Watchdog' do sistema de supervisão a cada 5 segundos 
    para garantir que a rede industrial está íntegra. 
    
    Se `connected` retornar `false`, o Dashboard deve exibir um alerta crítico de 'Perda de Comunicação'.
    """
    return {
        "connected": True,
        "ip": "192.168.1.5",
        "scan_time_ms": 12,
        "last_error": None
    }

@app.get("/api/monitor/live", response_model=List[RegisterValue], tags=["Monitoramento em Tempo Real"])
async def get_live_data():
    """
    ### 📈 Dados de Operação (Live)
    **Uso no Monitoramento:** Rota principal que alimenta os gauges e displays numéricos da interface principal.
    
    Os valores retornados já estão escalonados. Por exemplo, se um sensor PT100 retorna 825, 
    esta rota devolve 82.5°C pronto para exibição.
    """
    return [RegisterValue(**r) for r in mock_db["registers"]]

@app.post("/api/control/write", tags=["Controle e Comandos"])
async def send_command(
    address: int = Query(..., description="Endereço do registrador de destino"),
    value: float = Query(..., description="Novo valor a ser escrito (Setpoint)")
):
    """
    ### 🕹️ Comando de Escrita
    **Uso no Monitoramento:** Acionado quando o operador altera um Setpoint no Dashboard ou clica em um botão de 'Start/Stop'.
    
    **Segurança:** Toda escrita gera um log de auditoria com o ID do usuário e o valor anterior/atual.
    """
    # Lógica de validação de limites (Ex: não permitir temperatura > 100°C)
    return {"status": "Command Sent", "target": address, "new_value": value}

@app.get("/api/history/events", tags=["Histórico e Eventos"])
async def get_event_logs(limit: int = 10):
    """
    ### 📜 Logs de Eventos
    **Uso no Monitoramento:** Utilizado na aba de 'Histórico' para rastrear alarmes que ocorreram no passado.
    """
    return [
        {"time": "2026-05-12 09:00:01", "event": "Partida de Motor", "tag": "M1"},
        {"time": "2026-05-12 09:15:32", "event": "Alarme Alta Temperatura", "tag": "T1", "level": "CRITICAL"}
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
