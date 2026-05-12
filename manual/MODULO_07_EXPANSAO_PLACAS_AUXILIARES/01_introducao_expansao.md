# 01 - Introdução aos Módulos de Expansão

Os módulos de expansão (ou placas auxiliares) permitem aumentar a capacidade do CLP para além das entradas e saídas integradas na CPU.

## 1. Conexão Física
Módulos de expansão do lado direito (como os da linha Delta DVP-S) são conectados através de um barramento paralelo. A CPU identifica cada módulo pela sua posição física.

## 2. Endereçamento de Módulos
O CLP numera os módulos automaticamente de acordo com a proximidade da CPU:
- **Módulo 0**: O primeiro módulo acoplado à direita da CPU.
- **Módulo 1**: O segundo módulo, e assim por diante (até o limite de 8 módulos em muitas CPUs).

## 3. Comunicação via Barramento
Diferente das I/Os digitais simples (X/Y), os módulos especiais (analógicos, temperatura, posicionamento) trocam dados complexos com a CPU através de **Registradores de Controle (CR - Control Registers)**.

Para acessar esses registradores, utilizamos as instruções **FROM** (para ler) e **TO** (para escrever).

---
*Módulo 07 - Expansão e Placas Auxiliares*
