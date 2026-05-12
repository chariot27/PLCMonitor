# 05 - Comparativo e Boas Práticas

Escolher o protocolo correto depende da aplicação e da arquitetura do sistema.

## 1. Tabela Comparativa

| Protocolo | Meio Físico | Velocidade | Aplicação Principal |
| :--- | :--- | :--- | :--- |
| **Modbus RTU** | RS-485 | Baixa (até 115kbps) | Sensores, Inversores simples, Distâncias longas. |
| **Modbus TCP** | Ethernet | Média/Alta | Integração com Sistemas, IHMs, Gateways. |
| **Profinet** | Ethernet | Alta | Indústria de Processos, Linhas Siemens. |
| **EtherCAT** | Ethernet | Altíssima | Motion Control, Robótica, Máquinas Rápidas. |

## 2. Boas Práticas de Instalação de Redes
1. **Segregação de Cabos**: Nunca passe cabos de rede junto com cabos de potência ou motores (inversores). Mantenha uma distância mínima de 20cm.
2. **Conectores Industriais**: Use conectores RJ45 metálicos e blindados. Em ambientes agressivos, prefira conectores **M12**.
3. **Redundância**: Em redes críticas, use topologia em anel se o protocolo suportar (ex: MRP para Profinet ou EtherCAT Redundancy).
4. **Documentação**: Identifique cada cabo em ambas as extremidades. Uma rede sem identificação é um pesadelo de manutenção.

## 3. Limitações e Capacidades dos Protocolos

Conhecer os limites de cada tecnologia evita falhas de comunicação intermitentes e gargalos no processamento.

| Característica | Modbus RTU (485) | Modbus TCP | Profinet (RT) | EtherCAT |
| :--- | :--- | :--- | :--- | :--- |
| **Limite de Nós** | 32 (sem repetidor) | Teórico 65k | Depende da CPU (ex: 128) | 65.535 |
| **Distância Máx.** | 1200m (baixa vel.) | 100m (entre nós) | 100m (entre nós) | 100m (entre nós) |
| **Conexões Simultâneas** | 1 (Mestre único) | Limitado pela CPU | Alta (Industrial) | Alta (Hardware) |
| **Velocidade Típica** | 19.2 - 115 kbps | 100 Mbps / 1 Gbps | 100 Mbps (Full Duplex) | 100 Mbps (Otimizado) |

### Pontos de Atenção:
- **Modbus RTU**: Embora suporte até 247 IDs, a carga elétrica no barramento RS-485 geralmente limita a **32 dispositivos** físicos antes de precisar de um repetidor de sinal.
- **Modbus TCP**: O gargalo não é o protocolo, mas a CPU do CLP. Muitos CLPs compactos suportam apenas **8 ou 16 conexões simultâneas**. Se você tiver 20 IHMs tentando ler o mesmo CLP via Modbus TCP, algumas falharão.
- **EtherCAT**: O limite prático é o **tempo de ciclo**. Adicionar centenas de eixos de servomotor aumentará o tempo de processamento do mestre, podendo degradar a performance do Motion Control.
- **Ethernet (Geral)**: A distância de 100m é rígida para cabos de cobre. Acima disso, é obrigatório o uso de switches intermediários ou conversores de fibra óptica.

---
*Módulo 09 - Redes e Protocolos Industriais*
