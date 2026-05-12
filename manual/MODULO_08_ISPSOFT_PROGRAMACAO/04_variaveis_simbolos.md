# 04 - Variáveis e Símbolos

Gerenciar endereços de memória manualmente (`D0`, `M10`, `Y0`) é propenso a erros. O ISPSoft foca no uso de **Símbolos**.

## 1. Global Symbols
São variáveis acessíveis por todos os programas do projeto.
- Geralmente mapeadas para endereços físicos (ex: `Botao_Emergencia` -> `X0.0`).
- Usadas para sinais de I/O e registradores de interface com IHM.

## 2. Local Symbols
Variáveis que existem apenas dentro de uma POU específica.
- O ISPSoft gerencia o endereço automaticamente ou você pode deixar como "Auto".
- Essenciais para criar blocos de função reutilizáveis.

## 3. Tipos de Dados Comuns
- **BOOL**: Bit (True/False).
- **INT / UINT**: Inteiro de 16 bits.
- **DINT**: Inteiro de 32 bits.
- **REAL**: Ponto flutuante (decimal).
- **STRING**: Cadeia de caracteres.

---
*Módulo 08 - ISPSoft e Programação*
