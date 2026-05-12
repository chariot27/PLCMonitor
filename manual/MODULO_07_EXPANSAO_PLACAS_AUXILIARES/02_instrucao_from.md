# 02 - A Instrução FROM (Leitura de Módulo)

A instrução **FROM** é utilizada para buscar informações que estão dentro de um módulo de expansão e trazê-las para os registradores internos do CLP (D).

## Sintaxe da Instrução
```text
FROM [m1] [m2] [D] [n]
```

### Parâmetros:
1. **m1**: Número do módulo de expansão (0 a 7).
2. **m2**: Endereço do Registrador de Controle (CR) dentro do módulo que você deseja ler.
3. **D**: Registrador de destino no CLP (ex: D100) onde o valor lido será armazenado.
4. **n**: Quantidade de palavras (words) a serem lidas consecutivamente.

## Exemplo de Uso
```text
[ FROM K0 K10 D200 K1 ]
```
*Tradução: "Vá ao módulo 0, leia o CR#10 e salve o valor no registrador D200 do CLP. Leia apenas 1 palavra."*

## Quando usar?
- Ler valores de temperatura (PT100/Termopares).
- Ler o valor atual de uma entrada analógica (0-10V ou 4-20mA).
- Verificar o status de erro de um módulo.
- Identificar o modelo do módulo (geralmente no CR#0).

---
*Módulo 07 - Expansão e Placas Auxiliares*
