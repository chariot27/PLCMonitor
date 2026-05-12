# 05 - Digital vs Analógico: O Guia Definitivo

Entender a diferença entre sinais digitais e analógicos é o primeiro passo para qualquer projeto de automação.

## 1. Sinais Digitais (Discretos)

Sinais digitais possuem apenas dois estados possíveis: **LIGADO (1)** ou **DESLIGADO (0)**.

### No Hardware:
-   **Níveis de Tensão**: Geralmente 24VDC ou 110/220VAC.
-   **Entradas**: Sensores fim-de-curso, botões de pressão, pressostatos.
-   **Saídas**: Relés auxiliares, bobinas de contatores, lâmpadas piloto.

### No Ladder:
São representados por contatos (`| |`, `|/|`) e bobinas (`( )`).
-   **Endereçamento Delta**: Entradas físicas são `X0, X1...` e saídas físicas são `Y0, Y1...`.

---

## 2. Sinais Analógicos (Contínuos)

Sinais analógicos variam continuamente em uma faixa. Eles representam grandezas físicas reais como temperatura, pressão, vazão ou velocidade.

### No Hardware:
-   **Faixas Padrão**: 4-20mA, 0-20mA, 0-10V, -10 a +10V.
-   **Conversão A/D (Analógico para Digital)**: O CLP possui um conversor que transforma a tensão/corrente em um número inteiro (registrador).
-   **Resolução**: Um CLP de 12 bits terá uma faixa de 0 a 4095. Um de 14 bits, de 0 a 16383.

### No Ladder:
São manipulados através de **Registradores de Dados (D)**.
-   Não usamos contatos simples, mas sim blocos de comparação (`CMP`, `LD>`) e instruções matemáticas.

### Comparativo Rápido

| Característica | Digital | Analógico |
| :--- | :--- | :--- |
| **Estados** | 2 (On/Off) | Infinitos (dentro de uma faixa) |
| **Precisão** | Absoluta (Sim/Não) | Depende da resolução do CLP |
| **Custo** | Baixo | Mais elevado (módulos especiais) |
| **Ruído** | Imune (até certo ponto) | Muito sensível (requer cabos blindados) |

---
*Módulo 01 - Hardware*
