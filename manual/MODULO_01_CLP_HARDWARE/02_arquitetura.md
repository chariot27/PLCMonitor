# 02 - Arquitetura Interna da CPU

A CPU de um CLP não apenas executa o programa, mas gerencia a integridade do sistema.

## Organização de Memória
-   **Memória de Programa**: Armazena a lógica Ladder compilada (Flash/EEPROM).
-   **Memória de Dados (Registradores)**:
    -   **V (Variable Memory)**: Valores de processo.
    -   **D (Data Registers)**: Registradores de 16-bits (comuns em Delta/Mitsubishi).
-   **Imagem das Entradas/Saídas**: Buffer que sincroniza o estado físico com a lógica.

## Barramento de I/O (Bus)
O barramento permite que a CPU se comunique com módulos de expansão. A velocidade deste barramento determina quão rápido o CLP pode ler centenas de pontos.

## Watchdog Timer (WDT)
Um mecanismo de segurança. Se o ciclo de varredura demorar mais do que o previsto (ex: loop infinito), o WDT "derruba" a CPU para um estado seguro (Stop), desligando todas as saídas.

---
*Módulo 01 - Hardware*
