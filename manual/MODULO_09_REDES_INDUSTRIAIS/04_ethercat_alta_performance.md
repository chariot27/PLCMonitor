# 04 - EtherCAT: A Rede de Alta Performance

O EtherCAT (Ethernet for Control Automation Technology) é atualmente a rede mais rápida para controle de máquinas.

## 1. O Diferencial: "Processing on the fly"
Em outras redes, o mestre envia um pacote para cada escravo. No EtherCAT, o mestre envia **um único pacote** que percorre todos os escravos da rede.
- Cada escravo lê seus dados e insere suas respostas no pacote enquanto ele passa, sem parar o fluxo.
- Isso permite tempos de ciclo extremamente baixos (sub-milissegundos).

## 2. Topologia Flexível
O EtherCAT não exige switches. Os dispositivos possuem duas portas (In/Out) e são conectados em linha. Internamente, o último dispositivo fecha o anel lógico e envia o pacote de volta ao mestre.

## 3. Sincronismo (Distributed Clocks)
O EtherCAT consegue sincronizar os relógios de todos os escravos com precisão de nanosegundos. Isso é vital para máquinas de embalagem ou robótica onde vários eixos devem se mover em perfeita harmonia.

---
*Módulo 09 - Redes e Protocolos Industriais*
