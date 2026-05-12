# 06 - Matemática de Inteiros e Ponto Flutuante

O processamento numérico avançado exige o entendimento de como o CLP lida com diferentes formatos de números.

## Números Inteiros (INT / DINT)
-   **INT (16-bit)**: -32.768 a 32.767.
-   **DINT (32-bit)**: -2.147.483.648 a 2.147.483.647.
*Ao multiplicar dois INTs, o resultado pode estourar a capacidade de 16 bits, exigindo um destino DINT.*

## Números de Ponto Flutuante (REAL)
Usados para cálculos de alta precisão (ex: temperatura com casas decimais).
-   Seguem o padrão **IEEE 754**.
-   Instruções: `ADD_R`, `SUB_R`, `MUL_R`, `DIV_R`.

## Status Word (Palavra de Status)
Em CLPs Siemens, cada operação matemática afeta bits de status globais:
-   **OV (Overflow)**: O resultado excedeu o limite do formato.
-   **OS (Stored Overflow)**: Indica que houve um estouro em algum momento anterior.
-   **Z (Zero)**: O resultado é exatamente zero.

## Funções Trigonométricas e Logarítmicas
Disponíveis para cálculos complexos de engenharia:
-   `SIN`, `COS`, `TAN`.
-   `LN` (Logaritmo Natural), `EXP` (Exponencial).
-   `SQR` (Raiz Quadrada).

---
*Módulo 02 - Lógica Ladder*
