# 04 - Registradores de Controle (CR)

Cada módulo especial possui um mapa de memória interna chamado **Control Registers (CR)**. Embora cada modelo tenha seu mapa, existem alguns padrões comuns na linha Delta.

## Mapa Típico de um Módulo Analógico (Ex: DVP-04AD)

| CR# | Nome | Descrição | Acesso |
| :--- | :--- | :--- | :--- |
| **0** | Model Name | Código do modelo (ex: H6001 para 04AD). | R |
| **1** | Config Mode | Define se o canal é V ou I, e a faixa. | R/W |
| **2-5** | Average Times | Número de amostras para média (filtro). | R/W |
| **6-9** | Present Value | O valor lido em tempo real (Canais 1 a 4). | R |
| **18** | Binned Value | Valor após ajuste de offset/ganho. | R |
| **30** | Error Status | Indica se há erro de hardware ou sinal fora de faixa. | R |

## Dica de Performance
Em vez de usar quatro instruções FROM para ler os canais 1 a 4, use apenas uma:
```text
[ FROM K0 K6 D100 K4 ]
```
Isso lê o CR#6, 7, 8 e 9 de uma vez só e os coloca em D100, D101, D102 e D103. É muito mais eficiente para o barramento do CLP.

---
*Módulo 07 - Expansão e Placas Auxiliares*
