# Manual Mestre de Automação Industrial

Este é um compêndio técnico detalhado cobrindo desde o hardware básico até integrações de sistemas de alto nível (gRPC/OPC UA).

## 📚 Estrutura do Manual

### [Módulo 01: CLP & Hardware](./MODULO_01_CLP_HARDWARE/)
*Foco na parte física e sinais elétricos.*
- [01 Fundamentos e Evolução](./MODULO_01_CLP_HARDWARE/01_fundamentos.md)
- [02 Arquitetura Interna da CPU](./MODULO_01_CLP_HARDWARE/02_arquitetura.md)
- [03 Sinais de I/O e Condicionamento](./MODULO_01_CLP_HARDWARE/03_io_signals.md)
- [05 Digital vs Analógico: Guia Definitivo](./MODULO_01_CLP_HARDWARE/05_digital_vs_analogico.md)
- [06 Sistemas Numéricos (Hex, Octa, Dec)](./MODULO_01_CLP_HARDWARE/06_sistemas_numericos.md)
- [07 Esquemas Elétricos e Ligações](./MODULO_01_CLP_HARDWARE/07_esquemas_eletricos.md)

### [Módulo 02: Lógica Ladder Mastery](./MODULO_02_LOGICA_LADDER/)
*A arte da programação industrial.*
- [01 Lógica Básica e Selos](./MODULO_02_LOGICA_LADDER/01_basic_logic.md)
- [02 Temporizadores e Contadores](./MODULO_02_LOGICA_LADDER/02_timers_counters.md)
- [03 Manipulação de Dados e Analógicos](./MODULO_02_LOGICA_LADDER/03_data_handling.md)
- [04 Instruções de Bit e Bordas (Edges)](./MODULO_02_LOGICA_LADDER/04_instrucoes_avancadas.md)
- [05 Controle de Fluxo e Saltos](./MODULO_02_LOGICA_LADDER/05_controle_fluxo.md)
- [06 Matemática e Ponto Flutuante](./MODULO_02_LOGICA_LADDER/06_matematica_avancada.md)
- [07 Exemplos Práticos (Digital e Analógico)](./MODULO_02_LOGICA_LADDER/07_exemplos_praticos.md)
- [08 Relés Internos (M) e Memória](./MODULO_02_LOGICA_LADDER/08_reles_internos_m.md)

### [Módulo 03: Protocolo Modbus Profundo](./MODULO_03_MODBUS_PROFUNDO/)
*Dominando a comunicação industrial padrão.*
- [01 Camadas Físicas e Topologia](./MODULO_03_MODBUS_PROFUNDO/01_physical_layers.md)
- [02 Estrutura de Tramas e CRC](./MODULO_03_MODBUS_PROFUNDO/02_data_frames.md)
- [03 Instrução MODRW (Leitura/Escrita)](./MODULO_03_MODBUS_PROFUNDO/03_instrucao_modrw.md)
- [04 Mapeamento de Memória Delta DVP](./MODULO_03_MODBUS_PROFUNDO/04_delta_mapping.md)
- [05 Configuração do CLP como Escravo](./MODULO_03_MODBUS_PROFUNDO/05_configuracao_slave.md)

### [Módulo 04: Arquitetura OPC UA Avançada](./MODULO_04_OPC_UA_AVANCADO/)
*Comunicação moderna, segura e orientada a objetos.*
- [01 Modelagem de Informação (Nós)](./MODULO_04_OPC_UA_AVANCADO/01_information_modeling.md)
- [02 Segurança e Certificados](./MODULO_04_OPC_UA_AVANCADO/02_security.md)

### [Módulo 05: Integração de Sistemas](./MODULO_05_INTEGRACAO_SISTEMAS/)
*Ponte entre a fábrica e a TI moderna.*
- [01 gRPC na Indústria](./MODULO_05_INTEGRACAO_SISTEMAS/01_grpc_industrial.md)
- [02 Sincronização de Relógio (RTC)](./MODULO_05_INTEGRACAO_SISTEMAS/02_rtc_sync.md)
- [03 Performance e Polling](./MODULO_05_INTEGRACAO_SISTEMAS/03_performance_tuning.md)

### [Módulo 06: Arquitetura Avançada (Blocks)](./MODULO_06_ARQUITETURA_AVANCADA_BLOCKS/)
*Padrão Siemens S7 e IEC 61131-3.*
- [01 Blocos de Software (OB, FC, FB)](./MODULO_06_ARQUITETURA_AVANCADA_BLOCKS/01_blocos_software_ob_fc_fb.md)
- [02 Blocos de Dados (DB)](./MODULO_06_ARQUITETURA_AVANCADA_BLOCKS/02_blocos_dados_db.md)

### [Módulo 07: Expansão e Placas Auxiliares](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/)
*Uso de FROM/TO e comunicação com módulos especiais.*
- [01 Introdução aos Módulos](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/01_introducao_expansao.md)
- [02 Instrução FROM (Leitura)](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/02_instrucao_from.md)
- [03 Instrução TO (Escrita)](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/03_instrucao_to.md)
- [04 Registradores de Controle (CR)](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/04_mapeamento_cr.md)
- [05 Exemplo Prático (PT100)](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/05_exemplo_pratico.md)
- [06 Datasheet DVP-04TC (Termopares)](./MODULO_07_EXPANSAO_PLACAS_AUXILIARES/06_datasheet_dvp04tc.md)

### [Módulo 08: Programação ISPSoft](./MODULO_08_ISPSOFT_PROGRAMACAO/)
*Dominando o ambiente de desenvolvimento moderno da Delta.*
- [01 Introdução ao ISPSoft](./MODULO_08_ISPSOFT_PROGRAMACAO/01_introduction_ispsoft.md)
- [02 COMMGR e HWCONFIG](./MODULO_08_ISPSOFT_PROGRAMACAO/02_commgr_hwconfig.md)
- [03 Programação e POUs](./MODULO_08_ISPSOFT_PROGRAMACAO/03_programacao_pou.md)
- [04 Variáveis e Símbolos](./MODULO_08_ISPSOFT_PROGRAMACAO/04_variaveis_simbolos.md)
- [05 Monitoramento e Debug](./MODULO_08_ISPSOFT_PROGRAMACAO/05_monitoramento_debug.md)

### [Módulo 09: Redes Industriais e Protocolos](./MODULO_09_REDES_INDUSTRIAIS/)
*Comunicação e conectividade no chão de fábrica.*
- [01 Introdução às Redes](./MODULO_09_REDES_INDUSTRIAIS/01_introducao_redes.md)
- [02 Modbus RTU e RS-485](./MODULO_09_REDES_INDUSTRIAIS/02_modbus_rtu_rs485.md)
- [03 Ethernet Industrial](./MODULO_09_REDES_INDUSTRIAIS/03_ethernet_industrial.md)
- [04 EtherCAT Alta Performance](./MODULO_09_REDES_INDUSTRIAIS/04_ethercat_alta_performance.md)
- [05 Comparativo e Boas Práticas](./MODULO_09_REDES_INDUSTRIAIS/05_comparativo_boas_praticas.md)

---
*Organizado para o projeto Teste - 2026*
