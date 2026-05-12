# 06 - Sistemas Numéricos na Automação

O CLP processa tudo em binário, mas para nós humanos e para certos protocolos (como Modbus), usamos diferentes bases.

## 1. Decimal (Base 10)
O que usamos no dia a dia.
-   Símbolos: 0-9.
-   Ex: No Ladder Delta, `K100` representa o número decimal 100.

## 2. Binário (Base 2)
Como o CLP pensa internamente. Cada bit é uma chave (On/Off).
-   Símbolos: 0, 1.
-   Ex: `1101` em binário é `13` em decimal.

## 3. Hexadecimal (Base 16)
Muito usado para endereços Modbus e representação de bytes.
-   Símbolos: 0-9 e A-F (A=10, B=11, ..., F=15).
-   Vantagem: Um byte (8 bits) é representado perfeitamente por 2 dígitos hexa (00 a FF).
-   Ex: No Delta, prefixo `H`. `HFF` = 255 em decimal.

## 4. Octal (Base 8)
Usado historicamente por alguns fabricantes para endereçar I/Os (como a linha Mitsubishi ou Delta em alguns modelos).
-   Símbolos: 0-7.
-   Ex: Após a entrada `X7`, a próxima é `X10` (não existe X8 ou X9).

## Tabela de Conversão Rápida

| Decimal | Binário | Hexa | Octal |
| :--- | :--- | :--- | :--- |
| 0 | 0000 | 0 | 0 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 8 | 10 |
| 10 | 1010 | A | 12 |
| 15 | 1111 | F | 17 |
| 16 | 0001 0000 | 10 | 20 |

---
*Módulo 01 - Hardware*
