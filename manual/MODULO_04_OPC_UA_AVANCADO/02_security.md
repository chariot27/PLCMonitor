# 02 - Segurança e Certificados Digitais

O OPC UA foi projetado com segurança em mente, permitindo comunicações seguras mesmo em redes abertas.

## Pilares da Segurança
1.  **Autenticação**: Quem está tentando se conectar? (Anônimo, Usuário/Senha ou Certificado).
2.  **Integridade**: A mensagem foi alterada no caminho? (Assinatura Digital).
3.  **Confidencialidade**: Alguém pode ler o conteúdo da mensagem? (Criptografia).

## Certificados X.509
Cada cliente e servidor OPC UA possui um certificado digital. No primeiro aperto de mão (Handshake):
-   O Servidor envia seu certificado para o Cliente.
-   O Cliente deve "confiar" explicitamente no certificado do Servidor (geralmente movendo o arquivo para uma pasta `trusted`).
-   O Servidor faz o mesmo com o certificado do Cliente.

## Políticas de Segurança (Security Policies)
-   **None**: Sem segurança (apenas para testes).
-   **Basic256Sha256**: Alto nível de segurança.
-   **Aes128_Sha256_RsaOaep**: Padrão moderno.

## Modos de Mensagem
-   **None**: Texto puro.
-   **Sign**: As mensagens são assinadas para garantir a origem.
-   **SignAndEncrypt**: Mensagens assinadas e criptografadas.

---
*Módulo 04 - OPC UA*
