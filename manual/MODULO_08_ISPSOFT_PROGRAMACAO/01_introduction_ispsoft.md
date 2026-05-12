# 01 - Introdução ao ISPSoft

O **ISPSoft** é o ambiente de desenvolvimento moderno da Delta para sua linha de CLPs (DVP, AS, AH). Ele sucede o antigo WPLSoft, trazendo suporte a linguagens da norma IEC 61131-3 e uma organização baseada em projetos.

## 1. Vantagens sobre o WPLSoft
- **Programação Estruturada**: Uso de POUs (Program Organization Units).
- **Blocos de Função (FB)**: Permite criar blocos reutilizáveis com variáveis locais.
- **Gerenciamento de Símbolos**: Definição de nomes para endereços (ex: `Bomba_Partida` em vez de apenas `Y0`).
- **HWCONFIG**: Interface gráfica para configuração de hardware e expansões.

## 2. Estrutura de um Projeto
Um projeto no ISPSoft é organizado em uma árvore hierárquica:
- **Device Configuration**: Configurações de hardware.
- **Symbols**: Tabelas de variáveis globais.
- **Programs**: Onde reside a lógica Ladder ou ST.
- **Function Blocks**: Blocos customizados com memória própria.
- **Tasks**: Define como e quando cada programa será executado (Cíclico, por Interrupção, etc).

---
*Módulo 08 - ISPSoft e Programação*
