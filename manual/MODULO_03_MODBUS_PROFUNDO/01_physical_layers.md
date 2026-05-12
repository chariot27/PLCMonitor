# 01 - Camadas Físicas e Topologia Modbus

O Modbus pode ser transportado por diferentes meios físicos. Escolher o correto é vital para a estabilidade da rede.

## Modbus RTU (Serial)
Baseado em RS-232 ou RS-485.
-   **RS-232**: Ponto-a-ponto (apenas 2 dispositivos), distâncias curtas (até 15m).
-   **RS-485**: Multi-ponto (até 32 dispositivos sem repetidores), distâncias longas (até 1200m).
    -   *Resistores de Terminação*: Essenciais em RS-485 (120 ohms) nas extremidades para evitar reflexão de sinal.

## Modbus TCP (Ethernet)
O Modbus encapsulado em pacotes TCP/IP.
-   **Vantagem**: Pode usar a infraestrutura de rede existente (switches, roteadores).
-   **Velocidade**: Muito superior ao RTU.
-   **Confiabilidade**: O protocolo TCP gerencia a retransmissão de pacotes perdidos.

## Topologias Recomendadas
1.  **Daisy Chain (Varal)**: Recomendada para RS-485. Evite topologias em estrela para serial.
2.  **Estrela**: Padrão para Modbus TCP usando switches.

---
*Módulo 03 - Modbus Profundo*
