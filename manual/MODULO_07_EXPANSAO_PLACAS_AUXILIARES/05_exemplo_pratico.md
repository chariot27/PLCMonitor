# 05 - Exemplo Prático: Leitura de Temperatura

Vamos configurar um módulo **DVP-04PT** (4 canais PT100) posicionado como o primeiro módulo à direita da CPU (Módulo 0).

## Passo 1: Configuração (Opcional se padrão)
Normalmente o módulo PT100 já vem configurado para Celsius. Se quiséssemos garantir isso ou mudar a média:
```text
(M1002)--------- [ TO K0 K2 K10 K4 ]
```
*Ao ligar (M1002), define que a média dos 4 canais (K4) será de 10 amostras (K10).*

## Passo 2: Leitura dos Valores
A temperatura no módulo PT100 é entregue com uma casa decimal (ex: 25.5°C aparece como 255).
```text
(M1000)--------- [ FROM K0 K6 D200 K4 ]
```
*Lê constantemente (M1000) os 4 canais de temperatura e guarda em D200 até D203.*

## Passo 3: Conversão para Ponto Flutuante
Para exibir no IHM com vírgula ou usar em cálculos complexos:
```text
(M1000)--------- [ FLT D200 D210 ]
        |
        +------- [ DIVR D210 F10.0 D220 ]
```
1. `FLT`: Converte o inteiro 255 para ponto flutuante 255.0.
2. `DIVR`: Divide 255.0 por 10.0, resultando em **25.5** no registrador D220 (que agora é um par de registradores REAL).

---
*Módulo 07 - Expansão e Placas Auxiliares*
