# 08 - Relés Internos (M) e Memória de Estado

Os relés internos (conhecidos como **M** ou **Markers**) são "saídas virtuais" que residem apenas na memória do CLP. Eles são essenciais para armazenar estados intermediários.

## 1. Por que usar Relés M?
-   **Economia de Saídas Físicas**: Você não precisa gastar um borne Y para lembrar que uma etapa do processo foi concluída.
-   **Organização Lógica**: Dividir lógicas complexas em partes menores.
-   **Intertravamento**: Garantir que uma condição ocorra apenas se um "bit de memória" estiver ativo.

## 2. Tipos de Bits M (Padrão Delta DVP)
1.  **M Gerais (M0 - M511)**: Perdidos ao desligar o CLP (voláteis).
2.  **M Retentivos (M512 - M767)**: Mantêm o estado mesmo sem energia (bateria ou supercapacitor).
3.  **M Especiais (M1000 - M1999)**: Bits com funções pré-definidas pelo fabricante.

## 3. Bits M Especiais Importantes
| Bit | Função | Uso Comum |
| :--- | :--- | :--- |
| **M1000** | Always ON | Manter uma lógica sempre ativa. |
| **M1001** | Always OFF | Desabilitar temporariamente uma linha. |
| **M1002** | First Scan ON | Pulso único ao ligar o CLP (Setar valores iniciais). |
| **M1013** | 1s Clock | Piscar lâmpadas ou criar temporizações simples. |
| **M1012** | 100ms Clock | Piscar rápido para alarmes críticos. |

## 4. Bits de Passo (S - Step Bits)
Embora parecidos com os M, os bits **S** são usados especificamente em **SFC (Sequential Function Chart)** para representar etapas de um processo.

## Exemplo de Uso de M
```text
  Sensor_1      Sensor_2          M10 (Memória: Tanque Cheio)
---| |-----------| |--------------( )---

    M10         Start_Bomba       BOMBA (Saída Física Y0)
---| |-----------| |--------------( )---
```
Neste exemplo, a `BOMBA` só liga se os dois sensores estiverem ativos (armazenado em `M10`) E o operador apertar `Start`.

---
*Módulo 02 - Lógica Ladder*
