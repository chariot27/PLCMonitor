# 04 - Mapeamento de Memória Delta DVP

A Delta utiliza um mapeamento específico para converter seus registradores internos em endereços Modbus. Este capítulo é o seu "dicionário" de endereços.

## Tabela de Conversão

| Recurso Delta | Endereço Modbus (Hex) | Endereço Modbus (Dec) | Tipo de Dado |
| :--- | :--- | :--- | :--- |
| **S** (Step) | 0000H - 03FFH | 0 - 1023 | Coil |
| **Y** (Saídas) | 0500H - 05FFH | 1280 - 1535 | Coil |
| **M** (Memória) | 0800H - 0FFFH | 2048 - 4095 | Coil |
| **X** (Entradas) | 0400H - 04FFH | 1024 - 1279 | Discrete Input |
| **T** (Timer) | 0600H - 06FFH | 1536 - 1791 | Discrete Input / Register |
| **C** (Counter) | 0E00H - 0EFFH | 3584 - 3839 | Discrete Input / Register |
| **D** (Dados) | 1000H - 1FFFH | **4096 - 8191** | Holding Register |

## Dicas Importantes de Endereçamento
-   **Offset 0 vs 1**: Muitos softwares (como o Python `pymodbus`) usam endereçamento baseado em 0. O registrador **D0** no Delta é o endereço decimal **4096**.
-   **Leitura de Bits Individuais**: Se você quiser ler um bit específico dentro de um registrador D, você deve ler o registrador inteiro (16 bits) e aplicar uma máscara de bits no seu código.

## Registradores Especiais (D1000+)
A Delta possui centenas de registradores especiais que dão informações sobre o estado do CLP:
-   **D1000**: Modelo do CLP.
-   **D1010 - D1019**: Tempos de varredura (Scan time).
-   **D1313 - D1319**: Relógio de Tempo Real (RTC).

---
*Módulo 03 - Modbus Profundo*
