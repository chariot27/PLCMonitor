# 01 - Organização por Blocos (OB, FC, FB)

Sistemas avançados como o Siemens S7 não utilizam um programa único linear. Eles dividem a inteligência em diferentes tipos de blocos.

## 1. OB (Organization Blocks)
São a interface entre o sistema operacional do CLP e o seu programa.
-   **OB1**: O ciclo principal (Main). É executado ciclicamente.
-   **OB100**: Executado apenas uma vez no "Warm Start" (partida). Ideal para inicializar variáveis.
-   **OB35**: Executado em intervalos de tempo fixos (ex: a cada 100ms), independente do ciclo principal. Essencial para controles PID.

## 2. FC (Functions)
Blocos de código que executam uma tarefa específica e **não possuem memória própria**.
-   Ex: Uma função para calcular a média de 4 sensores.
-   Você passa os dados (Inputs), ela processa e devolve o resultado (Output).

## 3. FB (Function Blocks)
Diferente da FC, o FB possui uma **Memória de Instância** (geralmente um Data Block).
-   Isso permite que o FB "lembre" o que aconteceu no ciclo anterior.
-   Ideal para controle de motores, válvulas ou qualquer dispositivo que tenha estados e alarmes.

---
*Módulo 06 - Arquitetura Avançada*
