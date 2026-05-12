# 07 - Exemplos Práticos de Programação

Aqui consolidamos o conhecimento com exemplos que você encontrará no dia a dia industrial.

## Exemplo 1: Controle Digital (Partida Estrela-Triângulo)
Um clássico da automação para reduzir o pico de corrente na partida de motores grandes.

```text
   START      STOP      KM_TRIA     KM_LINE
---| |----| |----|/|-------( )---  (KM_LINE: Contator Geral)
     |      |
  KM_LINE   |
---| |------+

  KM_LINE     T0       KM_TRIA     KM_ESTR
---| |----|/|----|/|-------( )---  (KM_ESTR: Contator Estrela)

  KM_LINE                          [ TMR T0 K50 ] (5 segundos)

    T0      KM_ESTR                KM_TRIA
---| |----|/|--------------( )---  (KM_TRIA: Contator Triângulo)
```

## Exemplo 2: Controle Analógico (Nível de Reservatório)
Lógica para ligar uma bomba quando o nível está baixo e desligar quando está alto, usando um sensor de 4-20mA.

1.  **Leitura e Escalonamento**:
    -   Suponha que o sensor 4-20mA entregue 0-4000 no registrador `D100`.
    -   Queremos converter para 0-100% no registrador `D110`.
    -   `SCLP D100 K0 K4000 K0 K100 D110` (Instrução Delta de exemplo).

2.  **Lógica de Controle**:
```text
  Nível (D110) < 20%              BOMBA
-------[ LD< D110 K20 ]-----------( S )--- (Ligar Bomba - Set)

  Nível (D110) > 90%              BOMBA
-------[ LD> D110 K90 ]-----------( R )--- (Desligar Bomba - Reset)
```

## Exemplo 3: Alarmes de Temperatura
-   Se `Temp > 85°C`, pisca uma lâmpada de alarme.
-   Se `Temp > 95°C`, desliga o sistema e trava em erro.

```text
  Temp > 85      Clock_1s       Lâmpada
---| |-------| |----------( )---

  Temp > 95                     DESLIGA_SISTEMA
---| |--------------------( S )---
```

---
*Módulo 02 - Lógica Ladder*
