# Exemplo: Configurando o DVP-04TC no ISPSoft

Embora possamos configurar módulos de expansão via código Ladder (usando a instrução `TO`), o ISPSoft oferece uma interface visual muito mais simples através do **HWCONFIG**.

## 🚀 Passo a Passo no HWCONFIG

### 1. Abrir a Ferramenta
No ISPSoft, clique duas vezes em **HWCONFIG** na árvore de projeto à esquerda.

### 2. Adicionar o Módulo
1. Com a janela do HWCONFIG aberta, você verá a CPU no centro.
2. Na lista de dispositivos à direita (**Device List**), procure por **Special Module** > **Analog Module** > **Temperature Module**.
3. Encontre o **DVP-04TC** e arraste-o para o slot imediatamente à direita da CPU (Módulo 0).

### 3. Configuração Visual (Sem Código)
1. Clique duas vezes sobre a imagem do módulo DVP-04TC que você acabou de adicionar.
2. Uma janela de propriedades será aberta.
3. Vá na aba **Configuration Parameters**.
4. Aqui você pode definir:
   - **Mode (CR#1)**: Selecione "Type K", "Type J", etc., para cada um dos 4 canais individualmente.
   - **Average Number**: Defina quantas leituras o módulo deve fazer para calcular a média (ex: 10).
5. Clique em **OK**.

### 4. Salvar e Baixar
1. Clique no ícone de **Download** (seta para baixo) no topo do HWCONFIG para enviar essas configurações para o CLP físico.
2. **Importante:** Essas configurações são salvas na memória Flash do módulo e aplicadas automaticamente no boot.

---

## 🧙 Usando o Assistente de Instrução (Wizard)

Se você preferir ler os dados via software sem decorar os endereços de CR, o ISPSoft tem um assistente:

1. No editor de Ladder, clique com o botão direito e selecione **Wizard** > **Auxiliary Setup for Special Modules**.
2. Escolha o slot do módulo (ex: Slot 0) e selecione o módulo **DVP04TC-S**.
3. **Para Ler Dados (FROM):**
   - Marque a caixa **Read Register**.
   - Em **Condition**, defina o gatilho (ex: `LD M1000` para leitura constante).
   - Em **Register for Storing Data**, escolha onde salvar (ex: `D100`).
   - Selecione o dado desejado na lista à esquerda (ex: `#10 Average Celsius Temperature`).
4. **Para Configurar (TO):**
   - Marque a caixa **Write Register**.
   - Note que na parte inferior (**Set Value**), você pode selecionar o tipo de sensor (J, K, R, S, T) diretamente em menus suspensos para cada canal.
5. Clique em **Add to List** e depois em **OK**. O código será inserido automaticamente no seu Ladder.

---

## ✅ Resumo das Vantagens
- **HWCONFIG:** Ótimo para configurações estáticas (tipo de sensor que nunca muda).
- **Instrução TO:** Necessária se você precisar mudar o tipo de sensor dinamicamente via IHM durante o processo.
- **Instrução FROM:** Sempre necessária no Ladder para trazer o valor da temperatura para as variáveis do programa.
