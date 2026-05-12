# 02 - Estrutura de Tramas e Verificação de Erros

A "trama" é a sequência de bytes enviada pelo barramento.

## Estrutura da Trama Modbus RTU
1.  **Endereço do Escravo (1 byte)**: 1 a 247.
2.  **Código da Função (1 byte)**: O que fazer (ler, escrever).
3.  **Dados (N bytes)**: Endereço do registrador, quantidade, valores.
4.  **CRC (2 bytes)**: Cyclic Redundancy Check para detecção de erros.

## O que é o CRC?
É um cálculo matemático baseado em polinômios aplicado a todos os bytes anteriores. O receptor refaz o cálculo; se o resultado for diferente, a mensagem é descartada. Isso protege contra ruídos eletromagnéticos que podem "virar bits".

## Diferença para Modbus TCP
No Modbus TCP, o CRC é removido porque a camada Ethernet/IP já faz essa verificação. Em seu lugar, é adicionado o **MBAP Header** (7 bytes):
-   **Transaction ID**: Identifica a resposta para uma pergunta específica.
-   **Protocol ID**: Sempre 0 para Modbus.
-   **Length**: Tamanho do restante da mensagem.
-   **Unit ID**: Equivalente ao endereço do escravo no RTU.

---
*Módulo 03 - Modbus Profundo*
