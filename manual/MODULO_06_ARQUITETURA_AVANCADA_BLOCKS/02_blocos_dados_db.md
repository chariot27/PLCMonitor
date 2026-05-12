# 02 - Blocos de Dados (DB)

Os Data Blocks são áreas de memória global ou local usadas para armazenar valores de forma organizada e estruturada.

## Tipos de DB
1.  **Global DB**: Acessível por qualquer parte do programa (OB, FC ou FB). Funciona como uma grande base de dados global da máquina.
2.  **Instance DB**: Atrelado exclusivamente a um **FB (Function Block)**. Armazena os parâmetros e variáveis estáticas daquela chamada específica do bloco.

## Vantagens da Estruturação
Ao invés de endereços soltos como `D4096`, você trabalha com nomes simbólicos:
-   `DB_Motores.Motor1.Corrente`
-   `DB_Receitas.Cerveja_Pilsen.Temperatura_Fervura`

## Retentividade
No Siemens S7, você pode configurar quais variáveis de um DB devem ser retentivas (manter o valor após queda de energia) e quais devem ser resetadas para o valor inicial.

---
*Módulo 06 - Arquitetura Avançada*
