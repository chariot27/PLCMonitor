# 04 - Instruções Avançadas de Bit e Detecção de Borda

Inspirado no padrão Siemens S7, este capítulo detalha operações que vão além do simples liga/desliga.

## Set e Reset (S / R)
Diferente da bobina simples `( )`, as bobinas Set e Reset são retentivas dentro da lógica.
-   **Set (S)**: Quando a linha é verdadeira, a variável liga e **permanece ligada** mesmo que a linha se torne falsa.
-   **Reset (R)**: Desliga a variável.
-   **Dominância**: Se um Set e um Reset da mesma variável forem acionados no mesmo ciclo, o que estiver **mais abaixo** no programa prevalecerá (no caso de blocos RS ou SR, a dominância é fixa).

## Detecção de Borda (Edges)
Essenciais para capturar o exato momento de uma mudança de estado.
-   **Borda de Subida (P - Positive Edge)**: Gera um pulso de UM ciclo quando o sinal passa de 0 para 1.
-   **Borda de Descida (N - Negative Edge)**: Gera um pulso de UM ciclo quando o sinal passa de 1 para 0.

*Nota técnica: No padrão S7, essas instruções requerem um "Bit de Memória Auxiliar" para armazenar o estado do ciclo anterior e comparar.*

## Saída Intermediária (# - Midline Output)
Permite salvar o estado parcial de uma linha lógica (RLO - Result of Logic Operation) no meio de uma série de contatos, continuando a lógica em seguida.

---
*Módulo 02 - Lógica Ladder*
