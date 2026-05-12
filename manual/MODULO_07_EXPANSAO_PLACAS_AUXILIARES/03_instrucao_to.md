# 03 - A Instrução TO (Escrita no Módulo)

A instrução **TO** é o inverso da FROM. Ela envia valores dos registradores do CLP (ou constantes) para configurar ou comandar um módulo de expansão.

## Sintaxe da Instrução
```text
TO [m1] [m2] [S] [n]
```

### Parâmetros:
1. **m1**: Número do módulo de expansão (0 a 7).
2. **m2**: Endereço do Registrador de Controle (CR) de destino dentro do módulo.
3. **S**: Fonte (Source) do dado. Pode ser um registrador (D) ou uma constante (K).
4. **n**: Quantidade de palavras a serem escritas.

## Exemplo de Uso
```text
[ TO K0 K1 H0001 K1 ]
```
*Tradução: "Vá ao módulo 0, escreva o valor Hexadecimal H0001 no CR#1. Isso configurará o modo de operação do módulo."*

## Quando usar?
- Configurar o tipo de sinal (ex: mudar canal 1 de 0-10V para 4-20mA).
- Definir o valor de saída de um módulo analógico (DA).
- Resetar alarmes internos do módulo.
- Habilitar/Desabilitar canais específicos.

---
*Módulo 07 - Expansão e Placas Auxiliares*
