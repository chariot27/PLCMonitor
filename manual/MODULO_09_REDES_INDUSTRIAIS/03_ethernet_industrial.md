# 03 - Ethernet Industrial: Ethernet/IP e Profinet

Diferente da Ethernet comum, a Ethernet Industrial utiliza protocolos que priorizam o tráfego de controle sobre o tráfego de dados comum.

## 1. EtherNet/IP (Industrial Protocol)
Muito usado por Rockwell (Allen-Bradley) e dispositivos Delta modernos.
- Baseado no **CIP (Common Industrial Protocol)**.
- Utiliza switches padrão, mas se beneficia de switches gerenciáveis com suporte a **IGMP Snooping** para controlar o tráfego multicast.

## 2. Profinet
O padrão da Siemens e muito forte na Europa.
- **Profinet RT (Real Time)**: Para aplicações comuns de automação.
- **Profinet IRT (Isochronous Real Time)**: Para controle de movimento de alta precisão (Motion Control). Requer hardware específico (switches Profinet).

## 3. Modbus TCP
É o protocolo Modbus RTU "encapsulado" em pacotes Ethernet.
- **Vantagem**: Facilidade de implementação. Quase qualquer dispositivo Ethernet industrial fala Modbus TCP.
- **Desvantagem**: Não é tão performático para sincronismo de eixos quanto o EtherCAT.

---
*Módulo 09 - Redes e Protocolos Industriais*
