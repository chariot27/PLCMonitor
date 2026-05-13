# Instrução MODRW (Modbus Read/Write)

A instrução `MODRW` é a ferramenta fundamental nos CLPs Delta (família DVP) para realizar a comunicação Modbus como **Mestre**. Ela permite ler e escrever dados em dispositivos escravos (Inversores de Frequência, Controladores de Temperatura, outros CLPs, etc.) via portas seriais (COM2/RS-485 ou COM3).

## 🛠️ Sintaxe da Instrução

```ladder
|--[MODRW  S1  S2  S3  S4  n]--|
```

| Operando | Descrição | Faixa/Exemplo |
| :--- | :--- | :--- |
| **S1** | Endereço do Escravo (Slave ID) | 0 ~ 254 |
| **S2** | Código de Função Modbus | 0x01, 0x03, 0x06, 0x10, etc. |
| **S3** | Endereço Modbus de Destino | Endereço no escravo (ex: H2000) |
| **S4** | Registrador Local do CLP | Onde os dados serão lidos/escritos (ex: D100) |
| **n** | Comprimento dos Dados | Quantidade de registros/bits |

---

## 📋 Códigos de Função Suportados (S2)

| Hex | Descrição | Uso Comum |
| :--- | :---: | :--- |
| **0x01** | Read Coil Status | Ler saídas digitais do escravo |
| **0x02** | Read Input Status | Ler entradas digitais do escravo |
| **0x03** | Read Holding Registers | Ler múltiplos parâmetros (D-registers) |
| **0x04** | Read Input Registers | Ler registros de entrada analógica |
| **0x05** | Write Single Coil | Ligar/Desligar uma saída específica |
| **0x06** | Write Single Register | Escrever um único valor |
| **0x0F** | Write Multiple Coils | Escrever vários bits de uma vez |
| **0x10** | Write Multiple Registers | Escrever vários valores de uma vez |

---

## 🚦 Relés Especiais de Controle (Importante!)

Para garantir que a comunicação não sofra colisões, é essencial usar os relés de estado:

- **M1127:** Indica que o comando foi finalizado com sucesso.
- **M1129:** Indica erro de **Timeout** (o escravo não respondeu).
- **M1140:** Indica erro de dados ou CRC inválido.
- **M1141:** Indica erro de endereço ou função inexistente.
- **M1122:** Solicitação de envio (Trigger). Geralmente ativado pelo programa para iniciar o MODRW.

---

## 💡 Exemplo Prático: Lendo a Frequência de um Inversor

Suponha que queremos ler a frequência de saída de um inversor (Escravo 1) que está no endereço Modbus `H2103`, e guardar no registrador `D200` do CLP.

1. **Configuração de Hardware:** Porta COM2 configurada para 9600, 8, N, 1.
2. **Lógica Ladder:**

```ladder
|  M1000 (Sempre ON)
|--[MOV H87 D1120]--|  // Configura COM2: 9600, 8, N, 1

|  M1002 (Primeiro Scan)
|--[SET M1120]-------|  // Retém configuração de comunicação

|  X0 (Botão de Leitura)
|--[MODRW K1 H3 H2103 D200 K1]--| // S1=1, S2=3, S3=H2103, S4=D200, n=1

|  M1127 (Finalizado)
|--[RST M1127]-------|  // Reseta flag para próxima leitura
```

> [!TIP]
> Use sempre um intertravamento para não disparar várias instruções `MODRW` ao mesmo tempo na mesma porta serial. O Modbus RTU é sequencial (Half-Duplex).

---

## ⚠️ Erros Comuns

1. **Sobreposição de Comandos:** Tentar ler de dois escravos diferentes no mesmo ciclo sem esperar o `M1127`.
2. **Endereçamento Hex vs Dec:** Muitos manuais de fabricantes trazem endereços em Hexadecimal (ex: `2000H`). No ISPSoft, use o prefixo `H` (ex: `H2000`).
3. **Offset de Endereço:** Alguns dispositivos usam base 1 (40001). Na instrução `MODRW`, você deve usar o endereço real (0-based ou conforme o mapa do fabricante).
