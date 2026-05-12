# 07 - Esquemas Elétricos e Ligações de I/O

A correta ligação elétrica evita a queima de portas do CLP e garante a leitura correta dos sinais.

## 1. Ligação de Entradas Digitais (Sinking vs Sourcing)

### Lógica Sinking (NPN)
O CLP fornece o comum positivo (24V). O sensor fecha o circuito no Negativo (0V).
```mermaid
graph LR
    subgraph CLP
    A[S/S ou COM] --- B[+24VDC]
    C[Entrada X0]
    end
    D[Sensor NPN] --- C
    D --- E[0VDC]
```

### Lógica Sourcing (PNP)
O sensor fornece o positivo (24V) para a entrada do CLP.
```mermaid
graph LR
    subgraph CLP
    A[S/S ou COM] --- B[0VDC]
    C[Entrada X0]
    end
    D[Sensor PNP] --- C
    D --- E[+24VDC]
```

## 2. Ligação de Saídas (Relé vs Transistor)

### Saída a Relé
Funciona como um contato seco. Pode chavear AC ou DC.
```mermaid
graph LR
    A[Linha L1] --- B[C0 - Comum]
    C[Y0 - Saída] --- D[Carga / Bobina KM1]
    D --- E[Neutro N]
```

## 3. Ligação de Sinais Analógicos
Sinais analógicos são sensíveis. Sempre use cabos **blindados (shielded)**.
-   **V+ / I+**: Sinal positivo.
-   **V- / I- / COM**: Sinal negativo/comum.
-   **FG (Frame Ground)**: Onde a malha do cabo deve ser aterrada (apenas em uma das extremidades).

---
*Módulo 01 - Hardware*
