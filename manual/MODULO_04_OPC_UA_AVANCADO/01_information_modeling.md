# 01 - Modelagem de Informação (Nós e Objetos)

Diferente do Modbus, onde tudo é um número em uma lista, o OPC UA permite criar uma representação digital da sua planta.

## O Conceito de Nó (Node)
Tudo no OPC UA é um nó. Existem diferentes tipos:
-   **Variable Node**: Contém um valor (ex: Temperatura).
-   **Object Node**: Representa um componente físico (ex: Motor 01).
-   **Method Node**: Uma função que pode ser chamada (ex: Resetar Contador).

## Referências
As referências conectam os nós para criar uma hierarquia:
-   `Motor_01` -- *HasComponent* --> `Sensor_Temperatura`
-   `Sensor_Temperatura` -- *HasTypeDefinition* --> `AnalogItemType`

## Namespaces
O Servidor OPC UA organiza os nós em namespaces (índices numéricos).
-   **NS 0**: Padrão da OPC Foundation.
-   **NS 1**: Reservado para o servidor.
-   **NS 2+**: Onde os dados do seu projeto (CLP) geralmente residem.

## NodeID
Para ler um dado, você precisa do seu NodeID. Ele é composto por:
`NamespaceIndex ; IdentifierType ; Identifier`
Ex: `ns=2;s=GlobalVars.MotorSpeed` (Identificador do tipo String).

---
*Módulo 04 - OPC UA*
