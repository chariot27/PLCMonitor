# 02 - COMMGR e HWCONFIG

Antes de programar, é necessário estabelecer a comunicação e configurar o hardware físico.

## 1. COMMGR (Communication Manager)
O COMMGR é um software auxiliar que roda na bandeja do sistema e gerencia os drivers de comunicação.
- **Drivers RS232/485**: Configuração de COM Port, Baud Rate e Paridade.
- **Drivers Ethernet**: Busca automática de IPs na rede.
- **Simulador (DVP Simulator)**: Permite testar a lógica sem um CLP físico.

## 2. HWCONFIG (Hardware Configuration)
Dentro do ISPSoft, o HWCONFIG é a ferramenta para "montar" seu CLP virtualmente.
- **Configuração da CPU**: Definição de senhas, protocolos das portas integradas (COM1, COM2, Ethernet).
- **Módulos de Expansão**: Arrastar e soltar os módulos na ordem correta (Módulo 0, 1, 2...).
- **Parâmetros de Módulo**: Permite configurar módulos analógicos (ex: faixas de 4-20mA) via interface visual, sem a necessidade de usar instruções `TO` manuais no código para configurações básicas.

---
*Módulo 08 - ISPSoft e Programação*
