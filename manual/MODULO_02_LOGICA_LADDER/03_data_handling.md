# 03 - Manipulação de Dados e Matemática

Para trabalhar com sinais analógicos e cálculos complexos, o Ladder utiliza instruções de movimentação e aritmética.

## Movimentação de Dados (MOV)
A instrução `MOV` copia o valor de uma origem para um destino.
-   `MOV K100 D0`: Move a constante 100 para o registrador D0.
-   `MOV D0 D10`: Copia o valor de D0 para D10.

## Comparações (CMP)
Essenciais para lógica de decisão baseada em valores analógicos.
-   `LD> D0 K50`: Liga a linha se D0 for maior que 50.
-   `LD= D0 K100`: Liga a linha se D0 for exatamente 100.

## Operações Aritméticas
-   **ADD / SUB**: Adição e Subtração.
-   **MUL / DIV**: Multiplicação e Divisão (Cuidado: Divisões podem gerar resto e ocupar dois registradores).

## Processamento de Sinais Analógicos (Escalonamento)
Um sinal analógico chega como um número bruto (ex: 0 a 4000). Precisamos converter isso para uma unidade de engenharia (ex: 0 a 100°C).

**Fórmula de Escalonamento Linear:**
`Y = ((X - In_Min) * (Out_Max - Out_Min) / (In_Max - In_Min)) + Out_Min`

Muitos CLPs possuem a instrução **SCL** ou **SCLP** para fazer isso automaticamente. No Delta DVP, costuma-se usar a instrução `SCLP`.

---
*Módulo 02 - Lógica Ladder*
