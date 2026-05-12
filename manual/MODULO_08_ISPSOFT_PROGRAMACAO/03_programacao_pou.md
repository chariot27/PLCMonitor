# 03 - Programação e POUs

No ISPSoft, o código não é um "blocão" único. Ele é dividido em **POUs (Program Organization Units)**.

## 1. Tipos de POUs
- **Programs (PROG)**: Unidades principais de lógica. Devem ser associadas a uma Task para rodar.
- **Function Blocks (FB)**: Blocos que possuem memória interna (instância). Ideais para controle de dispositivos repetitivos (ex: um FB para cada Motor da fábrica).
- **Functions (FC)**: Blocos matemáticos ou lógicos sem memória. Recebem entradas e retornam uma saída imediata.

## 2. Linguagens Suportadas
O ISPSoft permite misturar linguagens no mesmo projeto:
- **Ladder Diagram (LD)**: A mais comum, visual.
- **Structured Text (ST)**: Linguagem textual similar a C/Pascal, excelente para cálculos matemáticos complexos.
- **Sequential Function Chart (SFC)**: Para máquinas de estado e processos sequenciais.

## 3. Tasks (Tarefas)
Após criar um programa, você deve atribuí-lo a uma Task:
- **Cyclic Task**: Executada continuamente (o padrão).
- **I/O Interrupt**: Executada quando uma entrada física (ex: X0) muda de estado.
- **Timer Interrupt**: Executada em intervalos fixos (ex: a cada 10ms).

---
*Módulo 08 - ISPSoft e Programação*
