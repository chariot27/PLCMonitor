# 05 - Controle de Fluxo: Saltos e Master Control Relay

Programas complexos exigem o controle de quais partes do código devem ser executadas em cada momento.

## Saltos (JMP / JMPN)
-   **JMP (Jump)**: Salta para uma etiqueta (`LABEL`) se a condição da linha for verdadeira.
-   **JMPN (Jump if Not)**: Salta se a condição for falsa.
*Cuidado: Saltos para trás podem causar erros de Watchdog se não forem bem controlados.*

## Master Control Relay (MCR)
Uma funcionalidade poderosa do padrão Siemens que permite "desligar" zonas inteiras do programa.
-   Quando o MCR está ativo, as bobinas dentro da zona MCR se comportam normalmente.
-   Quando o MCR é desativado, todas as bobinas normais na zona são forçadas a zero, independentemente da lógica.

## Chamadas de Bloco (CALL)
Permite invocar um FC ou FB no meio da lógica Ladder.
-   Ao usar o CALL, você deve preencher os parâmetros de entrada e saída definidos na interface do bloco.

---
*Módulo 02 - Lógica Ladder*
