# 03 - Sinais de I/O e Condicionamento

A interface entre o CLP e o mundo físico ocorre através dos módulos de I/O.

## Entradas Digitais
-   **Sinking (NPN)**: O CLP fornece o positivo, o sensor fecha o circuito no negativo.
-   **Sourcing (PNP)**: O sensor fornece o positivo, o CLP fecha no negativo.
*Dica: Verifique sempre o borne "COM" ou "S/S" do seu CLP Delta para configurar o tipo de lógica.*

## Saídas Digitais
-   **Relé**: Suporta maiores correntes (ex: 2A), mas tem vida útil limitada por ciclos mecânicos.
-   **Transistor**: Chaveamento rápido (PWM), vida útil quase infinita, mas baixa corrente.

## Sinais Analógicos
Transformam grandezas físicas em números no CLP.
-   **4-20mA**: Mais imune a ruídos. Se o cabo quebrar, o valor cai para 0mA (erro detectável).
-   **0-10V**: Sensível a quedas de tensão em cabos longos.

### Resolução Analógica
Um módulo de 12 bits divide o sinal em 4096 partes (0 a 4095).
Um módulo de 14 bits divide em 16384 partes.

---
*Módulo 01 - Hardware*
