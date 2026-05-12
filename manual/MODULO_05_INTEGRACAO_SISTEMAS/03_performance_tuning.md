# 03 - Performance e Otimização de Polling

Quando monitoramos dezenas de CLPs ou centenas de variáveis, a rede pode se tornar um gargalo.

## Leitura em Bloco (Block Reading)
Esta é a regra #1 da performance industrial.
-   **Ruim**: Fazer 10 requisições Modbus para ler 10 registradores individuais.
-   **Bom**: Fazer 1 requisição solicitando um bloco de 10 registradores contíguos.
*Redução de overhead: Cada pacote TCP tem um cabeçalho fixo. Ler em bloco reduz drasticamente o tráfego de cabeçalhos.*

## Otimização de Ciclo (Polling Rate)
Nem todo dado precisa ser lido na mesma velocidade.
-   **Críticos (Alarmes, Emergências)**: 100ms.
-   **Processo (Temperatura, Pressão)**: 500ms - 1s.
-   **Configuração (Setpoints)**: 5s ou apenas sob demanda.

## Gerenciamento de Conexões
-   Mantenha a conexão TCP aberta enquanto o serviço estiver rodando.
-   Abrir e fechar o socket a cada leitura (como um browser faz) é extremamente ineficiente e pode esgotar os recursos de rede do CLP.

---
*Módulo 05 - Integração*
