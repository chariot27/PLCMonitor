# Configuração do CLP como Escravo (Slave)

Neste modo, o CLP Delta não inicia a comunicação, mas sim **responde** às solicitações de um Mestre (como um IHM, Sistema SCADA ou outro CLP). Para que isso funcione, o CLP precisa de uma identidade (ID) e parâmetros de rede bem definidos.

## 📡 Portas de Comunicação

| Porta | Interface Física | Uso Comum |
| :--- | :--- | :--- |
| **COM1** | RS-232 (MD8) | Programação e IHM local |
| **COM2** | RS-485 (Bornes) | Redes de longa distância e múltiplos escravos |
| **COM3** | RS-485 (Bornes) | Redes adicionais (depende do modelo) |

---

## ⚙️ Registradores de Configuração

Para definir o CLP como escravo, utilizamos os seguintes registradores especiais:

### 1. Endereço da Estação (Station ID)
O registrador **D1121** define o endereço do CLP na rede Modbus.
- **Faixa:** 1 a 254 (O endereço 0 é broadcast).
- **Exemplo:** `MOV K1 D1121` define o CLP como **Escravo 1**.

### 2. Formato de Comunicação (Protocolo)
O registrador **D1120** (para COM2) define Baud Rate, Parity, Stop Bits e Data Bits.

| Bit | Descrição | Valores |
| :---: | :--- | :--- |
| **b0** | Data Length | 0: 7 bits, 1: 8 bits |
| **b2-b1**| Parity | 00: None, 01: Odd, 11: Even |
| **b3** | Stop Bit | 0: 1 bit, 1: 2 bits |
| **b7-b4**| Baud Rate | 1000 (9600), 1001 (19200), etc. |

**Valores Hex comuns para D1120:**
- `H81`: 9600, 8, N, 1
- `H87`: 9600, 8, E, 1
- `H97`: 19200, 8, E, 1

---

## 🚩 Flags de Controle (M-Relays)

Além dos registradores, precisamos ativar flags para "confirmar" a configuração:

- **M1120:** Retenção de configuração para COM2. Deve ser ligada para aplicar o valor de D1120.
- **M1143:** Seleção de Modo para COM2 (OFF: ASCII, **ON: RTU**).
- **M1138:** Retenção de configuração para COM1.
- **M1139:** Seleção de Modo para COM1 (OFF: ASCII, **ON: RTU**).

---

## 💡 Exemplo: Configurando COM2 como Escravo RTU

Este código deve ser colocado no início do programa (usando `M1002` - Primeiro Scan):

```ladder
|  M1002 (Primeiro Scan)
|--[MOV K1 D1121]-------|  // Define Station ID = 1
|
|--[MOV H87 D1120]------|  // 9600, 8, E, 1
|
|--[SET M1143]----------|  // Modo RTU (Importante!)
|
|--[SET M1120]----------|  // Ativa/Retém Configuração
```

---

## 🔍 Como Testar?

1. Use um software simulador de Mestre Modbus (como o **Modbus Poll** ou **QModMaster**).
2. Conecte um conversor USB/RS-485 ao PC e aos bornes (+ e -) da COM2 do CLP.
3. Tente ler o registrador `D0`. No Modbus, o endereço de `D0` geralmente é `4097` (ou `H1000` dependendo do mapeamento).

> [!IMPORTANT]
> Se você alterar o `D1121` ou `D1120` enquanto o CLP está rodando, a mudança só terá efeito após desligar e ligar o CLP ou dar um pulso no relé de retenção correspondente. No ISPSoft, o **HWCONFIG** pode fazer isso de forma visual sem necessidade de código Ladder.
