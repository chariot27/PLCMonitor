# 02 - Sincronização de Relógio (RTC)

Em sistemas de logging, a precisão do timestamp é crítica. Se o relógio do CLP estiver errado, seus logs de falhas serão inúteis.

## O Desafio do Drift
Relógios de CLPs costumam sofrer "drift" (desvio) de alguns segundos por semana devido a variações de temperatura e precisão do cristal interno.

## Estratégias de Sincronização
1.  **Mestre de Tempo (PC)**: O script Python lê a hora do Windows/Linux e escreve periodicamente nos registradores RTC do CLP.
2.  **NTP (Network Time Protocol)**: Alguns CLPs modernos suportam NTP nativamente, mas os compactos como o Delta DVP-SE geralmente exigem sincronização via software.

## Implementação no Delta DVP
Os registradores `D1313` a `D1319` controlam o RTC.
-   Para sincronizar, você deve converter o tempo atual do Python para o formato esperado (geralmente BCD ou decimal simples, dependendo do modelo).
-   **Importante**: A maioria dos CLPs Delta requer que você escreva os valores e então dê um pulso em um bit especial (ex: `M1076`) para que o hardware assuma a nova data/hora.

---
*Módulo 05 - Integração*
