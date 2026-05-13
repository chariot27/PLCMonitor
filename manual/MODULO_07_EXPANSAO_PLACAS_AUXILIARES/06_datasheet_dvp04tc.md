# Datasheet e Guia: Módulo DVP-04TC

O **DVP-04TC** é um módulo de expansão de temperatura para a linha Delta DVP, projetado para ler até **4 canais** de termopares (J, K, R, S, T) com alta precisão.

## 📋 Especificações Técnicas

- **Canais:** 4 canais de entrada.
- **Sensores Suportados:** Termopares Tipo J, K, R, S, T.
- **Resolução:** 0.1°C / 0.1°F.
- **Tempo de Conversão:** 200ms por canal.
- **Precisão:** ±0.5% da escala completa em 25°C.
- **Isolação:** Isolamento galvânico entre os canais e o barramento do CLP.

---

## 🛠️ Mapeamento de Registradores de Controle (CR)

A comunicação entre a CPU e o módulo é feita através das instruções `FROM` e `TO` acessando os CRs abaixo:

| CR# | Nome do Registro | Descrição | Permissão |
| :---: | :--- | :--- | :---: |
| **0** | Model Name | Código do modelo (DVP-04TC = H8804) | R |
| **1** | Configuração | Define o tipo de sensor para cada canal | R/W |
| **2-5** | Média (CH1-CH4) | Número de amostras para média (1-4096) | R/W |
| **6-9** | Temp. Atual | Temperatura lida em tempo real (0.1°C) | R |
| **10-13**| Temp. Média | Temperatura processada com filtro | R |
| **18-21**| Ajuste de Offset | Calibração de erro de leitura | R/W |
| **30** | Erro Status | Indica erro de hardware ou sensor aberto | R |

---

## ⚙️ Configuração de Tipo de Sensor (CR#1)

No CR#1, cada 3 bits definem o tipo de sensor para um canal.

| Valor (Binário) | Tipo de Termopar | Faixa de Temperatura |
| :---: | :--- | :--- |
| **000** | Tipo J | -200°C ~ 1200°C |
| **001** | Tipo K | -200°C ~ 1300°C |
| **010** | Tipo R | 0°C ~ 1700°C |
| **011** | Tipo S | 0°C ~ 1700°C |
| **100** | Tipo T | -200°C ~ 400°C |

---

## 💡 Exemplo de Programação (Ladder)

Para ler a temperatura do **Canal 1** (Termopar Tipo K) no **Módulo 0**:

1. **Configurar o Canal 1 como Tipo K (001):**
```ladder
|  M1002 (Primeiro Scan)
|--[TO K0 K1 H1 K1]--|  // Módulo 0, CR#1, Valor H1 (Tipo K), 1 registro
```

2. **Ler a Temperatura Média do CH1:**
```ladder
|  M1000 (Sempre ON)
|--[FROM K0 K10 D100 K1]--| // Módulo 0, CR#10, Destino D100, 1 registro
```

> [!NOTE]
> O valor lido em `D100` virá multiplicado por 10. Se o valor for `255`, a temperatura real é **25.5°C**.

---

## 🚦 Diagnóstico por LEDs

- **POWER:** Ligado quando a alimentação 24VDC está presente.
- **RUN:** Pisca durante a operação normal.
- **ERROR:** 
    - Aceso: Erro de Hardware ou alimentação baixa.
    - Piscando: Sensor desconectado ou fora da faixa.
