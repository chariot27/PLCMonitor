# 02 - Modbus RTU e RS-485

O Modbus RTU sobre RS-485 é o protocolo mais difundido na indústria devido à sua simplicidade e baixo custo.

## 1. A Camada Física RS-485
O RS-485 utiliza **sinais diferenciais** (fios A e B). A diferença de tensão entre os dois fios determina o bit, o que o torna extremamente imune a ruídos.

### Regras de Ouro do RS-485:
- **Topologia em Varal (Daisy Chain)**: Os dispositivos devem ser conectados um após o outro. Evite derivações em estrela.
- **Resistores de Terminação**: Um resistor de 120 ohms deve ser colocado em cada extremidade da rede para evitar a reflexão do sinal.
- **Aterramento do Shield**: A malha do cabo deve ser aterrada em apenas UM ponto para evitar loops de terra.

## 2. O Protocolo Modbus RTU
- **Mestre/Escravo**: Apenas o mestre inicia a comunicação. O escravo apenas responde.
- **Endereçamento**: Cada escravo deve ter um ID único (1 a 247).
- **Parâmetros de Porta**: Todos os dispositivos na rede devem ter o mesmo Baud Rate (ex: 9600, 19200, 38400) e Paridade.

## 3. Esquema Mestre-Escravo (Topology)

Diferente de redes Ethernet onde vários dispositivos podem falar ao mesmo tempo, no Modbus RTU existe uma hierarquia rígida.

```mermaid
graph TD
    M[MESTRE <br> PC / CLP / IHM] -- "Pergunta (Request)" --> S1[ESCRAVO 1 <br> ID: 1]
    M -- "Pergunta (Request)" --> S2[ESCRAVO 2 <br> ID: 2]
    M -- "Pergunta (Request)" --> S3[ESCRAVO n <br> ID: n]
    
    S1 -- "Resposta (Response)" --> M
    S2 -- "Resposta (Response)" --> M
    S3 -- "Resposta (Response)" --> M

    style M fill:#1a3a5f,stroke:#3498db,stroke-width:2px,color:#fff
    style S1 fill:#2c3e50,stroke:#95a5a6,color:#fff
    style S2 fill:#2c3e50,stroke:#95a5a6,color:#fff
    style S3 fill:#2c3e50,stroke:#95a5a6,color:#fff
```

### Funcionamento do Ciclo:
1. **O Mestre** envia um pacote contendo o ID do escravo alvo.
2. **Todos os Escravos** recebem o pacote, mas apenas aquele com o ID correspondente o processa.
3. **O Escravo** processa a solicitação e envia uma resposta de volta ao mestre.
4. **O Mestre** aguarda a resposta (Timeout) antes de enviar a próxima pergunta para o mesmo ou outro escravo.

---
*Módulo 09 - Redes e Protocolos Industriais*
