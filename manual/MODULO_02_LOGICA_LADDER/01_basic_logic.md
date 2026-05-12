# 01 - Lógica Básica e Circuitos de Selo

A programação Ladder deve ser lida como um fluxo de energia.

## Operações Lógicas
-   **AND**: Contatos em série.
-   **OR**: Contatos em paralelo.
-   **NOT**: Contato NF (Normalmente Fechado).

## O Circuito de Selo (Latch)
Fundamental para manter um motor ligado após um pulso momentâneo em um botão.

```text
   START      STOP       MOTOR
---| |----+---|/|--------( )---
          |
   MOTOR  |
---| |----+
```
1. Ao pressionar `START`, a linha fica verdadeira e ativa `MOTOR`.
2. O contato auxiliar de `MOTOR` fecha, mantendo a energia mesmo após soltar `START`.
3. Pressionar `STOP` quebra o circuito.

## Instruções de Diferencial (Pulsos)
-   **LDP (Leading Edge)**: Dispara um pulso de apenas UM ciclo de varredura quando o contato fecha.
-   **LDF (Falling Edge)**: Dispara um pulso quando o contato abre.

---
*Módulo 02 - Lógica Ladder*
