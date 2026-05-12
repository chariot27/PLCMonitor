const manualStructure = [
    {
        title: "Início",
        files: [
            { name: "🏠 README / Introdução", key: "README.md" }
        ]
    },
    {
        title: "Módulo 01: Hardware",
        files: [
            { name: "01 Fundamentos", key: "MODULO_01_CLP_HARDWARE/01_fundamentos.md" },
            { name: "02 Arquitetura CPU", key: "MODULO_01_CLP_HARDWARE/02_arquitetura.md" },
            { name: "03 Sinais I/O", key: "MODULO_01_CLP_HARDWARE/03_io_signals.md" },
            { name: "05 Digital vs Analógico", key: "MODULO_01_CLP_HARDWARE/05_digital_vs_analogico.md" },
            { name: "06 Sistemas Numéricos", key: "MODULO_01_CLP_HARDWARE/06_sistemas_numericos.md" },
            { name: "07 Esquemas Elétricos", key: "MODULO_01_CLP_HARDWARE/07_esquemas_eletricos.md" }
        ]
    },
    {
        title: "Módulo 02: Lógica Ladder",
        files: [
            { name: "01 Lógica Básica", key: "MODULO_02_LOGICA_LADDER/01_basic_logic.md" },
            { name: "02 Timers e Contadores", key: "MODULO_02_LOGICA_LADDER/02_timers_counters.md" },
            { name: "03 Manipulação Dados", key: "MODULO_02_LOGICA_LADDER/03_data_handling.md" },
            { name: "04 Instruções de Bit", key: "MODULO_02_LOGICA_LADDER/04_instrucoes_avancadas.md" },
            { name: "05 Controle de Fluxo", key: "MODULO_02_LOGICA_LADDER/05_controle_fluxo.md" },
            { name: "06 Matemática Avançada", key: "MODULO_02_LOGICA_LADDER/06_matematica_avancada.md" },
            { name: "07 Exemplos Práticos", key: "MODULO_02_LOGICA_LADDER/07_exemplos_praticos.md" },
            { name: "08 Relés Internos (M)", key: "MODULO_02_LOGICA_LADDER/08_reles_internos_m.md" }
        ]
    },
    {
        title: "Módulo 03: Modbus",
        files: [
            { name: "01 Camadas Físicas", key: "MODULO_03_MODBUS_PROFUNDO/01_physical_layers.md" },
            { name: "02 Tramas e CRC", key: "MODULO_03_MODBUS_PROFUNDO/02_data_frames.md" },
            { name: "04 Mapeamento Delta", key: "MODULO_03_MODBUS_PROFUNDO/04_delta_mapping.md" }
        ]
    },
    {
        title: "Módulo 04: OPC UA",
        files: [
            { name: "01 Modelagem", key: "MODULO_04_OPC_UA_AVANCADO/01_information_modeling.md" },
            { name: "02 Segurança", key: "MODULO_04_OPC_UA_AVANCADO/02_security.md" }
        ]
    },
    {
        title: "Módulo 05: Integração",
        files: [
            { name: "01 gRPC Industrial", key: "MODULO_05_INTEGRACAO_SISTEMAS/01_grpc_industrial.md" },
            { name: "02 Sincronização RTC", key: "MODULO_05_INTEGRACAO_SISTEMAS/02_rtc_sync.md" },
            { name: "03 Performance Tuning", key: "MODULO_05_INTEGRACAO_SISTEMAS/03_performance_tuning.md" }
        ]
    },
    {
        title: "Módulo 06: S7 & Blocks",
        files: [
            { name: "01 Blocos (OB/FC/FB)", key: "MODULO_06_ARQUITETURA_AVANCADA_BLOCKS/01_blocos_software_ob_fc_fb.md" },
            { name: "02 Data Blocks (DB)", key: "MODULO_06_ARQUITETURA_AVANCADA_BLOCKS/02_blocos_dados_db.md" }
        ]
    }
];

const contentEl = document.getElementById('markdown-content');
const navMenuEl = document.getElementById('nav-menu');
const breadcrumbEl = document.getElementById('breadcrumb');

function init() {
    renderMenu();
    loadPage(manualStructure[0].files[0].key, manualStructure[0].title, manualStructure[0].files[0].name);
    
    // Initialize mermaid
    mermaid.initialize({ startOnLoad: false, theme: 'dark' });
}

function renderMenu() {
    manualStructure.forEach(group => {
        const groupEl = document.createElement('div');
        groupEl.className = 'nav-group';
        groupEl.innerHTML = `<div class="nav-group-title">${group.title}</div>`;
        
        group.files.forEach(file => {
            const item = document.createElement('a');
            item.href = "#";
            item.className = 'nav-item';
            item.innerText = file.name;
            item.onclick = (e) => {
                e.preventDefault();
                document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
                item.classList.add('active');
                loadPage(file.key, group.title, file.name);
            };
            groupEl.appendChild(item);
        });
        
        navMenuEl.appendChild(groupEl);
    });
}

function loadPage(key, groupTitle, fileName) {
    contentEl.innerHTML = '<div class="loader">Carregando...</div>';
    breadcrumbEl.innerText = `${groupTitle} / ${fileName}`;
    
    try {
        const text = manualData[key];
        if (!text) {
            console.error('Key not found:', key);
            console.log('Available keys:', Object.keys(manualData));
            throw new Error(`Arquivo não encontrado no bundle: ${key}`);
        }
        
        contentEl.innerHTML = marked.parse(text);
        
        // Highlight code
        hljs.highlightAll();
        
        // Render mermaid
        mermaid.run();
        
        // Scroll to top
        contentEl.scrollTop = 0;
    } catch (err) {
        contentEl.innerHTML = `
            <div class="error-container">
                <div class="error-title">Erro de Carregamento</div>
                <div class="error-message">${err.message}</div>
                <button onclick="location.reload(true)" class="btn-retry">Recarregar Página</button>
            </div>
        `;
    }
}

init();
