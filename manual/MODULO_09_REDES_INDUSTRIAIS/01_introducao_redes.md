# 01 - Introdução às Redes Industriais

As redes industriais são a espinha dorsal da pirâmide da automação, conectando sensores, CLPs, IHMs e sistemas de supervisão.

## 1. Redes de Campo vs. Redes de Informação
- **Redes de Campo (Fieldbus)**: Focadas em determinismo e tempo real. Precisam garantir que um sinal de emergência chegue em milissegundos. Ex: EtherCAT, Profibus.
- **Redes de Informação**: Focadas em volume de dados e conectividade. Ex: Ethernet corporativa, Wi-Fi.

## 2. O Conceito de Determinismo
Em automação, **determinismo** é a garantia de que uma mensagem será entregue dentro de um tempo máximo conhecido. Em redes Ethernet padrão (Office), se houver colisão, o pacote é reenviado mais tarde (não determinístico). Em redes industriais como EtherCAT, o tempo é fixo.

## 3. Meios Físicos Comuns
- **Par Trançado Blindado (STP)**: Padrão para RS485 e Ethernet Industrial.
- **Fibra Óptica**: Usada para longas distâncias ou ambientes com altíssimo ruído eletromagnético.
- **Wireless Industrial**: Usado onde cabos são impossíveis (ex: AGVs - Veículos Guiados Automatizados).

---
*Módulo 09 - Redes e Protocolos Industriais*
