# 02 - Temporizadores e Contadores em Detalhe

Temporizadores e contadores são os blocos construtivos do controle sequencial.

## Temporizadores (T)
No Delta DVP, cada temporizador tem uma resolução (base de tempo).
-   **100ms**: T0-T199
-   **10ms**: T200-T239
-   **1ms**: T240-T255

### Modos de Funcionamento
1.  **TON (On-Delay)**: Começa a contar quando a entrada é ativada. Liga a saída após o tempo `K`.
2.  **TOF (Off-Delay)**: Liga a saída imediatamente. Começa a contar quando a entrada é DESLIGADA. Desliga a saída após o tempo.
3.  **TMR**: Instrução Delta típica: `TMR T0 K100` (Timer 0 por 10 segundos).

## Contadores (C)
-   **CTU (Up)**: Conta de 0 até o limite PV.
-   **CTD (Down)**: Conta do limite até 0.

### Retentividade
Contadores e Temporizadores podem ser **retentivos**. Isso significa que se o CLP for desligado e ligado novamente, o valor atual não é zerado.

---
*Módulo 02 - Lógica Ladder*
