<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de Torneo Aristoi III - v12 (Descarga Forzada)</title>
    <!-- Librería Excel -->
    <script src="https://cdn.sheetjs.com/xlsx-0.20.0/package/dist/xlsx.full.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1e293b; --secondary: #64748b; --accent: #10b981; --bg: #f1f5f9; --card-bg: #ffffff; --text: #0f172a; --border-radius: 12px; --success: #10b981;
        }
        * { box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.5; }
        header { background-color: var(--primary); color: white; padding: 1.5rem 2rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        h1 { margin: 0; font-size: 1.5rem; font-weight: 700; }
        small { color: #94a3b8; font-size: 0.85rem; }
        nav button { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.6rem 1.2rem; cursor: pointer; border-radius: 8px; margin-left: 0.5rem; font-weight: 500; }
        nav button:hover, nav button.active { background: white; color: var(--primary); }
        main { padding: 2rem; max-width: 1400px; margin: 0 auto; padding-bottom: 4rem; }
        section { display: none; animation: slideUp 0.4s ease-out; }
        section.active { display: block; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .card { background: var(--card-bg); padding: 2rem; border-radius: var(--border-radius); box-shadow: 0 1px 3px 0 rgba(0,0,0,0.1); margin-bottom: 2rem; border: 1px solid #e2e8f0; }
        
        /* Forms */
        input[type="text"], input[type="number"], select, textarea { width: 100%; padding: 0.75rem 1rem; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; font-family: inherit; }
        input:focus, select:focus, textarea:focus { outline: none; border-color: var(--accent); ring: 2px solid rgba(16, 185, 129, 0.2); }
        .form-group { margin-bottom: 1rem; }
        label { display: block; font-weight: 600; margin-bottom: 0.5rem; font-size: 0.9rem; color: var(--secondary); }
        
        /* Buttons */
        .btn { background-color: var(--primary); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; cursor: pointer; font-size: 0.9rem; font-weight: 600; margin-right: 0.5rem; transition: all 0.2s; display: inline-flex; align-items: center; justify-content: center; }
        .btn:hover { transform: translateY(-1px); }
        .btn-success { background-color: var(--accent); color: white; }
        .btn-success:hover { background-color: #059669; }
        .btn-danger { background-color: #ef4444; }
        .btn-danger:hover { background-color: #dc2626; }
        .btn-outline { background: transparent; border: 1px solid var(--primary); color: var(--primary); }
        .btn-outline:hover { background: #f8fafc; }
        .btn-remove { background: #ef4444; color: white; border: none; padding: 4px 8px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; margin-left: 8px; }
        
        /* Tables */
        .table-container { overflow-x: auto; border-radius: 8px; border: 1px solid #e2e8f0; }
        table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
        th, td { padding: 1rem; text-align: left; border-bottom: 1px solid #e2e8f0; }
        th { background-color: #f8fafc; font-weight: 600; color: var(--secondary); text-transform: uppercase; font-size: 0.75rem; }
        tr:hover td { background-color: #f8fafc; }

        /* Rubric */
        .rubric-container { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; background: #fff; padding: 1rem; border: 1px solid #e2e8f0; border-radius: var(--border-radius); }
        .team-column { border: 1px solid #e2e8f0; border-radius: 10px; padding: 1.5rem; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        .team-column.team-a { border-top: 5px solid #10b981; }
        .team-column.team-b { border-top: 5px solid #ef4444; }
        .rubric-section { margin-bottom: 1.5rem; border-bottom: 1px dashed #e2e8f0; padding-bottom: 1rem; }
        .rubric-section:last-child { border-bottom: none; }
        .rubric-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; }
        .rubric-label { font-size: 0.85rem; color: #475569; flex: 1; padding-right: 10px; }
        .rubric-input-wrapper { display: flex; align-items: center; gap: 5px; }
        .rubric-input-wrapper input { width: 60px; text-align: center; padding: 4px 8px; }
        .rubric-max { font-size: 0.75rem; color: #94a3b8; width: 25px; text-align: right; }
        .subtotal-row { background: #f1f5f9; padding: 0.5rem 0.75rem; border-radius: 6px; font-weight: 600; display: flex; justify-content: space-between; margin-top: 0.5rem; font-size: 0.9rem; color: var(--primary); }
        .grand-total { font-size: 1.75rem; font-weight: 700; text-align: right; margin-top: 1.5rem; color: var(--primary); padding: 1rem; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0; }
        .nom-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem; }
        .nom-select { font-size: 0.9rem; }
        .hidden { display: none !important; }
        .badge { display: inline-block; padding: 0.25rem 0.6rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600; }
        .badge-success { background: #dcfce7; color: #166534; }
        .badge-neutral { background: #f1f5f9; color: #475569; }
        #judge-finished-msg { text-align: center; padding: 4rem 2rem; color: var(--secondary); }
        #judge-finished-msg svg { width: 64px; height: 64px; color: var(--success); margin-bottom: 1rem; }
        .io-box { border: 1px dashed #cbd5e1; padding: 1rem; border-radius: 8px; background: #fff; margin-bottom: 1rem; }
        @media (max-width: 900px) { .rubric-container { grid-template-columns: 1fr; } }
    </style>
</head>
<body>

<header>
    <div>
        <h1>Torneo Debate Aristoi III</h1>
        <small>Gestión Oficial v12</small>
    </div>
    <nav>
        <button onclick="showSection('admin-panel')" id="nav-admin" class="active">Organización</button>
        <button onclick="showSection('judge-view')" id="nav-judge">Vista Juez</button>
    </nav>
</header>

<main>
    <!-- ================= ADMIN PANEL ================= -->
    <section id="admin-panel" class="active">
        
        <!-- Excel Import/Export -->
        <div class="io-box">
            <div style="display:flex; gap: 1rem; flex-wrap: wrap; align-items: center;">
                <div>
                    <strong>💾 Copia de Seguridad / Excel</strong>
                    <div style="font-size:0.85rem; color: #64748b; margin-bottom: 0.5rem;">
                        Exporta a Excel para guardar. Importa un Excel para cargar resultados o cambiar de PC.
                    </div>
                </div>
                <div style="display:flex; gap:0.5rem;">
                    <button class="btn btn-success" onclick="exportToExcel()">📤 Exportar a Excel</button>
                    <label class="btn btn-outline" style="cursor: pointer;">
                        📥 Importar Excel <input type="file" id="excel-input" accept=".xlsx, .xls" style="display: none;" onchange="importFromExcel(this)">
                    </label>
                </div>
            </div>
        </div>

        <div style="margin-bottom: 2rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <button class="btn btn-outline" onclick="toggleSetup('teams')">Gestionar Equipos</button>
            <button class="btn btn-outline" onclick="toggleSetup('judges')">Gestionar Jueces</button>
            <button class="btn btn-outline" onclick="toggleSetup('pairings')">Generar Rondas</button>
            <button class="btn btn-outline" onclick="toggleSetup('awards')">Clasificaciones</button>
        </div>

        <!-- 1. Teams -->
        <div id="setup-teams" class="card">
            <h2>Gestión de Equipos</h2>
            <div class="form-group"><label>Nombre</label><input type="text" id="new-team-name"><input type="hidden" id="edit-team-id"></div>
            <div class="form-group">
                <label>Miembros</label>
                <div id="members-container"></div>
                <button class="btn btn-outline" onclick="addMemberInput()">+ Miembro</button>
            </div>
            <div style="margin-top: 1rem;">
                <button class="btn" onclick="saveTeam()">Guardar</button>
                <button class="btn btn-danger hidden" id="cancel-edit-btn" onclick="resetTeamForm()">Cancelar</button>
            </div>
            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 2rem 0;">
            <div class="table-container"><table id="teams-table"><thead><tr><th>Equipo</th><th>Miembros</th><th>Acciones</th></tr></thead><tbody></tbody></table></div>
        </div>

        <!-- 2. Judges -->
        <div id="setup-judges" class="card hidden">
            <h2>Gestión de Jueces</h2>
            <div class="form-group">
                <input type="hidden" id="edit-judge-id">
                <label>Nombre</label><input type="text" id="new-judge-name">
                <label style="font-weight: normal;">Incompatible con:</label>
                <select id="new-judge-conflicts" multiple style="height: 100px;"></select>
            </div>
            <div style="margin-top: 1rem;">
                <button class="btn" onclick="saveJudge()">Guardar</button>
                <button class="btn btn-danger hidden" id="cancel-judge-edit-btn" onclick="resetJudgeForm()">Cancelar</button>
            </div>
            <div class="table-container"><table id="judges-table"><thead><tr><th>Juez</th><th>Incompatibilidades</th><th>Acciones</th></tr></thead><tbody></tbody></table></div>
        </div>

        <!-- 3. Pairings -->
        <div id="setup-pairings" class="card hidden">
            <h2>Emparejamientos</h2>
            <p id="pairing-mode-text" style="color: var(--secondary);"></p>
            <div style="margin: 1.5rem 0;">
                <button class="btn" onclick="generatePairings()">Generar Ronda</button>
                <span id="current-round-display" style="font-weight: 700; margin-left: 1rem; font-size: 1.1rem;">Ronda: 0</span>
            </div>
            <div class="table-container"><table id="pairings-table"><thead><tr><th>Mesa</th><th>Enfrentamiento</th><th>Jueces</th><th>Estado</th></tr></thead><tbody></tbody></table></div>
        </div>

        <!-- 4. Rankings -->
        <div id="setup-awards" class="card hidden">
            <h2 style="margin-bottom: 1.5rem;">Clasificación General</h2>
            <h3 style="font-size: 1.1rem; color: var(--secondary); border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Ranking de Equipos</h3>
            <div class="table-container" style="margin-bottom: 2rem;"><table id="standings-table-final"><thead><tr><th>Pos</th><th>Equipo</th><th>Victorias</th><th>Puntos</th></tr></thead><tbody></tbody></table></div>
            <h3 style="font-size: 1.1rem; color: var(--secondary); border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">Premios Individuales</h3>
            <div class="table-container"><table id="awards-table-final"><thead><tr><th>Categoría</th><th>Ganador</th><th>Nominaciones</th></tr></thead><tbody></tbody></table></div>
        </div>
    </section>

    <!-- ================= JUDGE VIEW ================= -->
    <section id="judge-view">
        <div class="card" style="max-width: 1200px; margin: 0 auto;">
            <h2>Panel de Juez</h2>
            
            <div id="judge-login">
                <div class="form-group" style="max-width: 400px; margin: 0 auto;">
                    <label>Identifíquese:</label>
                    <select id="judge-selector" onchange="loadJudgeMatchups()"></select>
                </div>
            </div>

            <div id="judge-finished-msg" class="hidden">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <h3>Finalizado</h3>
                <button class="btn" onclick="exportJudgeResults()">📥 Descargar Mis Resultados (Excel)</button>
                <button class="btn btn-outline" onclick="initJudgeView()" style="margin-top: 1rem;">Reiniciar</button>
            </div>

            <div id="judge-scoring" class="hidden">
                <button class="btn btn-outline hidden" id="exit-judge-btn" onclick="initJudgeView()">← Salir</button>
                
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 1.5rem; border-bottom: 1px solid #e2e8f0;">
                    <button class="btn" id="prev-match-btn" onclick="navigateMatch(-1)">← Anterior</button>
                    <div style="text-align:center;">
                        <h3 id="scoring-title" style="font-size: 1.25rem;">Hoja de Puntuación</h3>
                        <span id="match-counter" class="badge badge-neutral"></span>
                    </div>
                    <button class="btn" id="next-match-btn" onclick="navigateMatch(1)">Siguiente →</button>
                </div>
                
                <p style="color: var(--secondary); font-size: 0.9rem; text-align:center; margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto;">
                    Complete los campos. El sistema calculará los totales automáticamente. 
                    <br><strong>Nota:</strong> Una vez pulsado "Guardar", no podrá modificar.
                </p>

                <form id="rubric-form" onsubmit="submitScores(event)">
                    <div class="rubric-container">
                        <!-- EQUIPO A -->
                        <div class="team-column team-a">
                            <h4 style="color: #047857; margin-bottom: 1rem;">EQUIPO A FAVOR</h4>
                            <input type="hidden" id="score-team-id-a">
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>GENERAL (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Calidad/Línea</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="A" data-sec="gen"> <span class="rubric-max">10</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Exordio</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="A" data-sec="gen"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Victoria Arg.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="A" data-sec="gen"> <span class="rubric-max">10</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-A-gen">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>INTRO (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Arg.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="A" data-sec="intro"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="A" data-sec="intro"> <span class="rubric-max">10</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">POIs</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="A" data-sec="intro"> <span class="rubric-max">10</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-A-intro">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>REFUT 1 (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Arg. (ARE)</span><div class="rubric-input-wrapper"><input type="number" min="0" max="15" class="score-input" data-team="A" data-sec="r1"> <span class="rubric-max">15</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Refut.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="A" data-sec="r1"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="A" data-sec="r1"> <span class="rubric-max">5</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-A-r1">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>REFUT 2 (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Refut.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="15" class="score-input" data-team="A" data-sec="r2"> <span class="rubric-max">15</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Arg.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="A" data-sec="r2"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="A" data-sec="r2"> <span class="rubric-max">5</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-A-r2">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>CONCLU (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="15" class="score-input" data-team="A" data-sec="conclu"> <span class="rubric-max">15</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Síntesis</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="A" data-sec="conclu"> <span class="rubric-max">10</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-A-conclu">0</span></div>
                            </div>
                            <div class="grand-total">Total A: <span id="total-a">0</span></div>
                        </div>

                        <!-- EQUIPO B -->
                        <div class="team-column team-b">
                            <h4 style="color: #b91c1c; margin-bottom: 1rem;">EQUIPO EN CONTRA</h4>
                            <input type="hidden" id="score-team-id-b">
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>GENERAL (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Calidad/Línea</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="B" data-sec="gen"> <span class="rubric-max">10</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Exordio</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="B" data-sec="gen"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Victoria Arg.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="B" data-sec="gen"> <span class="rubric-max">10</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-B-gen">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>INTRO (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Arg.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="B" data-sec="intro"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="B" data-sec="intro"> <span class="rubric-max">10</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">POIs</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="B" data-sec="intro"> <span class="rubric-max">10</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-B-intro">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>REFUT 1 (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Arg. (ARE)</span><div class="rubric-input-wrapper"><input type="number" min="0" max="15" class="score-input" data-team="B" data-sec="r1"> <span class="rubric-max">15</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Refut.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="B" data-sec="r1"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="B" data-sec="r1"> <span class="rubric-max">5</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-B-r1">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>REFUT 2 (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Refut.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="15" class="score-input" data-team="B" data-sec="r2"> <span class="rubric-max">15</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Arg.</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="B" data-sec="r2"> <span class="rubric-max">5</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="5" class="score-input" data-team="B" data-sec="r2"> <span class="rubric-max">5</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-B-r2">0</span></div>
                            </div>
                            <div class="rubric-section">
                                <div style="display:flex; justify-content:space-between; font-weight:700; font-size:0.8rem; color:#64748b; margin-bottom:0.5rem;"><span>CONCLU (25)</span></div>
                                <div class="rubric-row"><span class="rubric-label">Estilo</span><div class="rubric-input-wrapper"><input type="number" min="0" max="15" class="score-input" data-team="B" data-sec="conclu"> <span class="rubric-max">15</span></div></div>
                                <div class="rubric-row"><span class="rubric-label">Síntesis</span><div class="rubric-input-wrapper"><input type="number" min="0" max="10" class="score-input" data-team="B" data-sec="conclu"> <span class="rubric-max">10</span></div></div>
                                <div class="subtotal-row"><span>Subtotal:</span> <span id="sub-B-conclu">0</span></div>
                            </div>
                            <div class="grand-total">Total B: <span id="total-b">0</span></div>
                        </div>
                    </div>

                    <!-- Nominations -->
                    <div style="background: #f8fafc; padding: 2rem; margin-top: 2rem; border-radius: var(--border-radius); border: 1px solid #e2e8f0;">
                        <h4 style="margin-top:0; color: var(--primary); margin-bottom: 1rem;">Nominaciones Individuales</h4>
                        <div class="nom-grid">
                            <div><label>🏆 MEJOR ORADOR (MVP)</label><select id="nom-mvp" class="nom-select" required><option value="">--</option></select></div>
                            <div><label>🎤 Mejor Introducción</label><select id="nom-intro" class="nom-select" required><option value="">--</option></select></div>
                            <div><label>⚔️ Mejor Refutación 1</label><select id="nom-r1" class="nom-select" required><option value="">--</option></select></div>
                            <div><label>🛡️ Mejor Refutación 2</label><select id="nom-r2" class="nom-select" required><option value="">--</option></select></div>
                            <div><label>⚖️ Mejor Conclusión</label><select id="nom-conclu" class="nom-select" required><option value="">--</option></select></div>
                        </div>
                    </div>

                    <div style="text-align: center; margin-top: 2rem;">
                        <button type="submit" class="btn" style="padding: 1rem 2.5rem; font-size: 1rem;">GUARDAR PUNTUACIÓN</button>
                    </div>
                </form>
            </div>
        </div>
    </section>
</main>

<script>
    const state = { teams: [], judges: [], rounds: [], currentRound: 0 };
    let isRestrictedMode = false;
    let myAssignedMatches = [], myCurrentMatchIndex = 0;

    function loadExampleData() {
        const t1 = { id: 't1', name: 'Escuela Atenea', members: [{id:'m1', name:'Sócrates'}, {id:'m2', name:'Platón'}], wins:0, points:0, speakerPoints:0, opponents:[] };
        const t2 = { id: 't2', name: ' academy SPQR', members: [{id:'m3', name:'Cicerón'}, {id:'m4', name:'Séneca'}], wins:0, points:0, speakerPoints:0, opponents:[] };
        const t3 = { id: 't3', name: 'Instituto Zenón', members: [{id:'m5', name:'Marco Aurelio'}, {id:'m6', name:'Epicteto'}], wins:0, points:0, speakerPoints:0, opponents:[] };
        const t4 = { id: 't4', name: 'Liceo Moderno', members: [{id:'m7', name:'Aristóteles'}, {id:'m8', name:'Alejandro'}], wins:0, points:0, speakerPoints:0, opponents:[] };
        const j1 = { id: 'j1', name: 'Juez Pericles', conflicts: [] };
        const j2 = { id: 'j2', name: 'Juez Aspasia', conflicts: [] };
        state.teams = [t1, t2, t3, t4];
        state.judges = [j1, j2];
        state.rounds = [];
        saveState();
    }

    function loadState() {
        const saved = localStorage.getItem('aristoi_tournament_v12');
        if (saved) {
            const parsed = JSON.parse(saved);
            state.teams = parsed.teams || [];
            state.judges = parsed.judges || [];
            state.rounds = parsed.rounds || [];
            state.currentRound = parsed.currentRound || 0;
        } else {
            loadExampleData();
        }
        renderAll();
    }

    function saveState() {
        localStorage.setItem('aristoi_tournament_v12', JSON.stringify(state));
        renderAll();
    }

    function renderAll() {
        renderTeamsTable(); renderJudgesTable(); renderConflictOptions(); renderPairingsTable(); renderStandingsAndAwards();
        document.getElementById('current-round-display').innerText = `Ronda Actual: ${state.currentRound}`;
        document.getElementById('pairing-mode-text').innerText = state.currentRound === 0 ? "MODO: SORTEO ALEATORIO" : "MODO: SISTEMA SUIZO";
    }

    // ================= EXCEL LOGIC (ROBUST DOWNLOAD) =================
    // Helper function to force download
    function downloadFile(blob, filename) {
        if (window.navigator.msSaveOrOpenBlob) {
            // IE10+
            navigator.msSaveOrOpenBlob(blob, filename);
        } else {
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            document.body.appendChild(a);
            a.style = "display: none";
            a.href = url;
            a.download = filename;
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }
    }

    function exportToExcel() {
        // 1. Teams Sheet
        const teamsData = state.teams.map(t => ({
            ID: t.id,
            Nombre: t.name,
            Miembros: t.members.map(m => m.name).join(", ")
        }));
        const wsTeams = XLSX.utils.json_to_sheet(teamsData);

        // 2. Judges Sheet
        const judgesData = state.judges.map(j => ({
            ID: j.id,
            Nombre: j.name,
            Incompatibilidades: j.conflicts.map(cid => state.teams.find(t=>t.id===cid)?.name).filter(Boolean).join(", ")
        }));
        const wsJudges = XLSX.utils.json_to_sheet(judgesData);

        // 3. Rounds Sheet
        const roundsData = [];
        state.rounds.forEach((round, rIdx) => {
            round.forEach(m => {
                const tA = state.teams.find(t=>t.id===m.teamA);
                const tB = state.teams.find(t=>t.id===m.teamB);
                let row = {
                    Ronda: rIdx + 1,
                    Mesa: `Mesa ${state.rounds[rIdx].indexOf(m) + 1}`,
                    "Equipo A": tA ? tA.name : "???",
                    "Equipo B": tB ? tB.name : "???",
                    Juez: m.judgeNames.join(", "),
                    Estado: m.finalScores ? "Finalizado" : "Pendiente"
                };
                if(m.finalScores) {
                    row["Puntos A"] = m.finalScores.totalA.toFixed(1);
                    row["Puntos B"] = m.finalScores.totalB.toFixed(1);
                    row["Ganador"] = m.winner === m.teamA ? tA.name : (m.winner === tB.id ? tB.name : "Empate");
                }
                roundsData.push(row);
            });
        });
        const wsRounds = XLSX.utils.json_to_sheet(roundsData);

        const wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, wsTeams, "Equipos");
        XLSX.utils.book_append_sheet(wb, wsJudges, "Jueces");
        XLSX.utils.book_append_sheet(wb, wsRounds, "Rondas");

        // Write and Force Download
        const wbout = XLSX.write(wb, {bookType:'xlsx', type:'array'});
        const blob = new Blob([wbout], {type: "application/octet-stream"});
        downloadFile(blob, "Torneo_Datos_Sesion.xlsx");
        
        alert("Intentando descargar el archivo Excel... Si no se descarga, busca el icono de descarga bloqueado en tu navegador (arriba a la derecha).");
    }

    function importFromExcel(input) {
        const file = input.files[0];
        if(!file) return;
        const reader = new FileReader();
        reader.onload = function(e) {
            const data = new Uint8Array(e.target.result);
            const workbook = XLSX.read(data, {type: 'array'});
            
            // Import Teams
            if(workbook.Sheets["Equipos"]) {
                const jsonData = XLSX.utils.sheet_to_json(workbook.Sheets["Equipos"]);
                jsonData.forEach(row => {
                    let t = state.teams.find(x => x.id == row.ID);
                    const membersArr = row.Miembros ? row.Miembros.split(/,\s*/) : [];
                    const members = membersArr.map((n, i) => ({id: (row.ID || Date.now())+'_'+i, name: n.trim()}));
                    if(t) { t.name = row.Nombre; t.members = members; }
                    else {
                        state.teams.push({ id: row.ID || Date.now().toString(), name: row.Nombre, members: members, wins: 0, points: 0, speakerPoints: 0, opponents: [] });
                    }
                });
            }

            // Import Judges
            if(workbook.Sheets["jueces"]) { // Note: sheet name matches data export, check logic below
                 // If user created sheet manually, name might differ. Let's iterate all sheets if specific name fails.
                 // Assuming user uses the file created by this app.
                 const sheetName = workbook.SheetNames.find(n => n.includes("Juez") || n.includes("Judge"));
                 if(sheetName) {
                    const jsonData = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName]);
                    jsonData.forEach(row => {
                        let j = state.judges.find(x => x.id == row.ID);
                        const conflictNames = row.Incompatibilidades ? row.Incompatibilidades.split(/,\s*/) : [];
                        const conflictIds = conflictNames.map(name => {
                            const t = state.teams.find(x => x.name === name);
                            return t ? t.id : null;
                        }).filter(Boolean);
                        if(j) { j.name = row.Nombre; j.conflicts = conflictIds; }
                        else { state.judges.push({ id: row.ID || Date.now().toString(), name: row.Nombre, conflicts: conflictIds }); }
                    });
                 }
            }

            // Import Rounds
            const roundSheetName = workbook.SheetNames.find(n => n.includes("Ronda"));
            if(roundSheetName) {
                const rows = XLSX.utils.sheet_to_json(workbook.Sheets[roundSheetName]);
                let newRounds = [], maxRound = 0;
                rows.forEach(row => {
                    const rNum = parseInt(row.Ronda) - 1;
                    if(!newRounds[rNum]) newRounds[rNum] = [];
                    if(rNum > maxRound) maxRound = rNum;
                    const tA = state.teams.find(t => t.name === row["Equipo A"]);
                    const tB = state.teams.find(t => t.name === row["Equipo B"]);
                    if(tA && tB) {
                        const jNames = row.Juez ? row.Juez.split(/,\s*/) : [];
                        const jIds = jNames.map(n => {
                            const j = state.judges.find(j => j.name === n);
                            return j ? j.id : null;
                        }).filter(Boolean);
                        let match = newRounds[rNum].find(m => m.teamA === tA.id && m.teamB === tB.id);
                        if(!match) {
                            match = { id: Date.now() + Math.random(), teamA: tA.id, teamB: tB.id, judges: [], judgeNames: [], judgeSubmissions: {}, finalScores: null, winner: null };
                            newRounds[rNum].push(match);
                        }
                        match.judges = [...new Set([...match.judges, ...jIds])];
                        match.judgeNames = match.judges.map(jid => state.judges.find(x=>x.id===jid)?.name).filter(Boolean);
                        if(row.Estado === "Finalizado" && row["Puntos A"] !== undefined) {
                            match.finalScores = { totalA: parseFloat(row["Puntos A"]), totalB: parseFloat(row["Puntos B"]), bestA: 0, bestB: 0 };
                            // Note: Importing "Finalizado" locks the round from further scoring in this simplified version.
                        }
                    }
                });
                newRounds.forEach((r, idx) => { state.rounds[idx] = r; });
                state.currentRound = newRounds.length - 1;
            }

            saveState();
            alert("Datos importados correctamente desde Excel.");
            input.value = "";
        };
    }

    // ================= NAVIGATION =================
    function showSection(id) {
        if (isRestrictedMode && id !== 'judge-view') return;
        document.querySelectorAll('main > section').forEach(s => s.classList.remove('active'));
        document.getElementById(id).classList.add('active');
        if(id === 'admin-panel') document.getElementById('nav-admin').classList.add('active');
        if(id === 'judge-view') {
            document.getElementById('nav-judge').classList.add('active');
            initJudgeView();
        }
    }

    function toggleSetup(type) {
        ['setup-teams', 'setup-judges', 'setup-pairings', 'setup-awards'].forEach(id => document.getElementById(id).classList.add('hidden'));
        document.getElementById('setup-' + type).classList.remove('hidden');
    }

    // ================= TEAMS CRUD =================
    function addMemberInput(name = '') {
        const container = document.getElementById('members-container');
        const div = document.createElement('div');
        div.className = 'form-group';
        div.style.marginBottom = '0.5rem';
        div.innerHTML = `<input type="text" class="member-input" placeholder="Nombre" value="${name}"> <button type="button" class="btn-remove" onclick="this.parentElement.remove()">X</button>`;
        container.appendChild(div);
    }
    function resetTeamForm() {
        document.getElementById('edit-team-id').value = '';
        document.getElementById('new-team-name').value = '';
        document.getElementById('members-container').innerHTML = '';
        addMemberInput(); addMemberInput();
        document.querySelector('#setup-teams .btn').innerText = 'Guardar Equipo';
        document.getElementById('cancel-edit-btn').classList.add('hidden');
    }
    function editTeam(id) {
        const t = state.teams.find(x => x.id === id);
        if(!t) return;
        document.getElementById('edit-team-id').value = t.id;
        document.getElementById('new-team-name').value = t.name;
        document.getElementById('members-container').innerHTML = '';
        t.members.forEach(m => addMemberInput(m.name));
        document.querySelector('#setup-teams .btn').innerText = 'Actualizar Equipo';
        document.getElementById('cancel-edit-btn').classList.remove('hidden');
        toggleSetup('teams'); window.scrollTo(0,0);
    }
    function saveTeam() {
        const idInput = document.getElementById('edit-team-id').value;
        const name = document.getElementById('new-team-name').value.trim();
        if(!name) return alert("Nombre requerido");
        const memberInputs = document.querySelectorAll('.member-input');
        const members = [];
        memberInputs.forEach((inp, idx) => {
            if(inp.value.trim()) members.push({ id: (idInput ? idInput : Date.now()) + '_' + idx, name: inp.value.trim() });
        });
        if(members.length === 0) return alert("Añade al menos 1 miembro");
        if(idInput) { const t = state.teams.find(x => x.id === idInput); t.name = name; t.members = members; }
        else { state.teams.push({ id: Date.now().toString(), name: name, members: members, wins: 0, points: 0, speakerPoints: 0, opponents: [] }); }
        resetTeamForm(); saveState();
    }
    function deleteTeam(id) { if(confirm("¿Borrar?")) { state.teams = state.teams.filter(t => t.id !== id); saveState(); } }
    function renderTeamsTable() {
        const tbody = document.getElementById('teams-table').querySelector('tbody');
        tbody.innerHTML = '';
        state.teams.forEach(t => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${t.name}</td><td><small>${t.members.map(m=>m.name).join(', ')}</small></td><td><button class="btn btn-outline" style="font-size:0.8rem;" onclick="editTeam('${t.id}')">Editar</button> <button class="btn btn-remove" onclick="deleteTeam('${t.id}')">Borrar</button></td>`;
            tbody.appendChild(tr);
        });
    }

    // ================= JUDGES CRUD =================
    function resetJudgeForm() {
        document.getElementById('edit-judge-id').value = '';
        document.getElementById('new-judge-name').value = '';
        document.getElementById('new-judge-conflicts').selectedIndex = -1;
        document.querySelector('#setup-judges .btn').innerText = 'Guardar Juez';
        document.getElementById('cancel-judge-edit-btn').classList.add('hidden');
    }
    function editJudge(id) {
        const j = state.judges.find(x => x.id === id);
        if(!j) return;
        document.getElementById('edit-judge-id').value = j.id;
        document.getElementById('new-judge-name').value = j.name;
        const sel = document.getElementById('new-judge-conflicts');
        Array.from(sel.options).forEach(opt => { opt.selected = j.conflicts.includes(opt.value); });
        document.querySelector('#setup-judges .btn').innerText = 'Actualizar Juez';
        document.getElementById('cancel-judge-edit-btn').classList.remove('hidden');
        toggleSetup('judges'); window.scrollTo(0,0);
    }
    function saveJudge() {
        const idInput = document.getElementById('edit-judge-id').value;
        const name = document.getElementById('new-judge-name').value.trim();
        const conflicts = Array.from(document.getElementById('new-judge-conflicts').selectedOptions).map(o => o.value);
        if(!name) return alert("Nombre requerido");
        if(idInput) { const j = state.judges.find(x => x.id === idInput); j.name = name; j.conflicts = conflicts; }
        else { state.judges.push({ id: Date.now().toString(), name: name, conflicts: conflicts }); }
        resetJudgeForm(); saveState();
    }
    function deleteJudge(id) { if(confirm("¿Borrar?")) { state.judges = state.judges.filter(j => j.id !== id); saveState(); } }
    function renderJudgesTable() {
        const tbody = document.getElementById('judges-table').querySelector('tbody');
        tbody.innerHTML = '';
        state.judges.forEach(j => {
            const cNames = j.conflicts.map(cid => state.teams.find(t=>t.id===cid)?.name).filter(Boolean).join(', ');
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${j.name}</td><td><small>${cNames||'Ninguna'}</small></td><td><button class="btn btn-outline" style="font-size:0.8rem;" onclick="editJudge('${j.id}')">Editar</button> <button class="btn btn-remove" onclick="deleteJudge('${j.id}')">Borrar</button></td>`;
            tbody.appendChild(tr);
        });
    }
    function renderConflictOptions() {
        const sel = document.getElementById('new-judge-conflicts');
        sel.innerHTML = '';
        state.teams.forEach(t => { const opt = document.createElement('option'); opt.value = t.id; opt.innerText = t.name; sel.appendChild(opt); });
    }

    // ================= PAIRING LOGIC =================
    function shuffle(array) { return array.sort(() => Math.random() - 0.5); }
    function generatePairings() {
        if (state.teams.length < 2) return alert("Mínimo 2 equipos.");
        if (state.teams.length % 2 !== 0) return alert("Número par de equipos.");
        if (state.rounds[state.currentRound] && state.rounds[state.currentRound].length > 0) {
            if(!confirm("Regenerar ronda?")) return;
        }
        const roomsNeeded = state.teams.length / 2;
        let matchups = [];
        let teamPairs = [];
        if (state.currentRound === 0) {
            const shuffled = shuffle([...state.teams]);
            for(let i=0; i<shuffled.length; i+=2) teamPairs.push([shuffled[i], shuffled[i+1]]);
        } else {
            const sorted = [...state.teams].sort((a,b) => (b.wins - a.wins) || (b.points - a.points));
            const paired = new Set();
            for(let tA of sorted) {
                if(paired.has(tA.id)) continue;
                for(let tB of sorted) {
                    if(tA.id===tB.id || paired.has(tB.id)) continue;
                    if(tA.opponents.includes(tB.id)) continue;
                    teamPairs.push([tA, tB]);
                    paired.add(tA.id); paired.add(tB.id); break;
                }
            }
        }
        if(teamPairs.length < roomsNeeded) return alert("Error restricciones.");

        let assignedJudges = new Set();
        let availableJudges = shuffle([...state.judges]);
        const findCompatible = (pair, judgeList) => {
            return judgeList.find(j => !assignedJudges.has(j.id) && !j.conflicts.includes(pair[0].id) && !j.conflicts.includes(pair[1].id));
        };

        for(let pair of teamPairs) {
            const judge = findCompatible(pair, availableJudges);
            if(!judge) return alert(`No hay jueces para ${pair[0].name} vs ${pair[1].name}`);
            matchups.push({
                id: Date.now() + Math.random(), teamA: pair[0].id, teamB: pair[1].id,
                judges: [judge.id], judgeNames: [judge.name], judgeSubmissions: {}, finalScores: null, winner: null
            });
            assignedJudges.add(judge.id);
        }

        let shuffledMatchups = shuffle([...matchups]);
        let remainingJudges = state.judges.filter(j => !assignedJudges.has(j.id));
        for(let j of remainingJudges) {
            const room = shuffledMatchups.find(m => !j.conflicts.includes(m.teamA) && !j.conflicts.includes(m.teamB));
            if(room) { room.judges.push(j.id); room.judgeNames.push(j.name); assignedJudges.add(j.id); }
        }

        state.rounds[state.currentRound] = matchups;
        saveState(); alert("Ronda generada.");
    }

    function renderPairingsTable() {
        const tbody = document.getElementById('pairings-table').querySelector('tbody');
        tbody.innerHTML = '';
        const currentRound = state.rounds[state.currentRound] || [];
        if (currentRound.length === 0) { tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding: 2rem; color: #94a3b8;">Sin datos.</td></tr>'; return; }
        currentRound.forEach((m, idx) => {
            const tA = state.teams.find(t => t.id === m.teamA);
            const tB = state.teams.find(t => t.id === m.teamB);
            let status = `<span class="badge badge-neutral">Pendiente</span>`;
            if(m.finalScores) {
                const w = m.winner === tA.id ? tA.name : (m.winner === tB.id ? tB.name : "Empate");
                status = `<span class="badge badge-success">Finalizado</span><br><small style="margin-top:4px; display:block; color: #64748b;">Ganador: ${w}</small>`;
            }
            const tr = document.createElement('tr');
            tr.innerHTML = `<td><strong>Mesa ${idx + 1}</strong></td><td>${tA.name} vs ${tB.name}</td><td>${m.judgeNames.map(n=>`<span class="badge badge-neutral" style="font-size:0.7rem;">${n}</span>`).join(' ')}</td><td>${status}</td>`;
            tbody.appendChild(tr);
        });
    }

    // ================= JUDGE INTERFACE =================
    function initJudgeView() {
        const sel = document.getElementById('judge-selector');
        sel.innerHTML = '<option value="">-- Seleccione su nombre --</option>';
        state.judges.forEach(j => { const opt = document.createElement('option'); opt.value = j.id; opt.innerText = j.name; sel.appendChild(opt); });
        sel.value = "";
        document.getElementById('judge-login').classList.remove('hidden');
        document.getElementById('judge-scoring').classList.add('hidden');
        document.getElementById('judge-finished-msg').classList.add('hidden');
        if (isRestrictedMode) document.getElementById('exit-judge-btn').classList.add('hidden');
        else document.getElementById('exit-judge-btn').classList.remove('hidden');
    }

    function loadJudgeMatchups() {
        const judgeId = document.getElementById('judge-selector').value;
        if(!judgeId) return;

        const round = state.rounds[state.currentRound] || [];
        myAssignedMatches = round.filter(m => m.judges.includes(judgeId));
        const pendingMatches = myAssignedMatches.filter(m => !m.judgeSubmissions[judgeId]);

        if (myAssignedMatches.length === 0) {
            document.getElementById('judge-login').classList.add('hidden');
            document.getElementById('judge-scoring').classList.add('hidden');
            document.getElementById('judge-finished-msg').classList.remove('hidden');
            document.getElementById('judge-finished-msg').querySelector('p').innerText = "No tiene debates asignados en esta ronda.";
            return;
        }

        if (pendingMatches.length === 0) {
            document.getElementById('judge-login').classList.add('hidden');
            document.getElementById('judge-scoring').classList.add('hidden');
            document.getElementById('judge-finished-msg').classList.remove('hidden');
        } else {
            document.getElementById('judge-login').classList.add('hidden');
            document.getElementById('judge-finished-msg').classList.add('hidden');
            document.getElementById('judge-scoring').classList.remove('hidden');
            const firstPendingId = pendingMatches[0].id;
            myCurrentMatchIndex = myAssignedMatches.findIndex(m => m.id === firstPendingId);
            openRubric(myAssignedMatches[myCurrentMatchIndex].id);
        }
    }

    function navigateMatch(direction) {
        const newIndex = myCurrentMatchIndex + direction;
        const judgeId = document.getElementById('judge-selector'). value;
        if (newIndex >= 0 && newIndex < myAssignedMatches.length) {
            const nextMatch = myAssignedMatches[newIndex];
            if(nextMatch.judgeSubmissions[judgeId]) { alert("Bloqueado."); return; }
            myCurrentMatchIndex = newIndex;
            openRubric(nextMatch.id);
        }
    }

    let currentMatchupId = null;

    function openRubric(mid) {
        const m = myAssignedMatches[myCurrentMatchIndex];
        if(m.id !== mid) return;

        currentMatchupId = mid;
        const tA = state.teams.find(t => t.id === m.teamA);
        const tB = state.teams.find(t => t.id === m.teamB);
        
        document.getElementById('scoring-title').innerText = `Sala: ${tA.name} vs ${tB.name}`;
        document.getElementById('match-counter').innerText = `Debate ${myCurrentMatchIndex + 1} de ${myAssignedMatches.length}`;
        
        document.getElementById('prev-match-btn').style.visibility = myCurrentMatchIndex === 0 ? 'hidden' : 'visible';
        document.getElementById('next-match-btn').style.visibility = myCurrentMatchIndex === myAssignedMatches.length - 1 ? 'hidden' : 'visible';

        document.getElementById('score-team-id-a').value = m.teamA;
        document.getElementById('score-team-id-b').value = m.teamB;
        
        document.querySelectorAll('.score-input').forEach(i => i.value = 0);
        document.querySelectorAll('.subtotal-row span:not(:first-child)').forEach(s => s.innerText = "0");
        document.getElementById('total-a').innerText = "0"; document.getElementById('total-b').innerText = "0";
        
        calculateRubricTotals(); 

        const noms = ['nom-mvp','nom-intro','nom-r1','nom-r2','nom-conclu'];
        noms.forEach(id => {
            const sel = document.getElementById(id);
            sel.innerHTML = '<option value="">-- Seleccionar --</option>';
            [tA, tB].forEach(team => {
                const grp = document.createElement('optgroup');
                grp.label = team.name;
                team.members.forEach(mem => {
                    const opt = document.createElement('option');
                    opt.value = mem.id; opt.innerText = mem.name;
                    grp.appendChild(opt);
                });
                sel.appendChild(grp);
            });
        });

        window.scrollTo(0,0);
    }

    document.querySelectorAll('.score-input').forEach(i => i.addEventListener('input', calculateRubricTotals));

    function calculateRubricTotals() {
        const teams = ['A', 'B'];
        const sections = ['gen', 'intro', 'r1', 'r2', 'conclu'];
        let totalA = 0, totalB = 0, bestScoreA = 0, bestScoreB = 0;
        teams.forEach(team => {
            let teamTotal = 0;
            sections.forEach(sec => {
                let secSum = 0;
                document.querySelectorAll(`.score-input[data-team="${team}"][data-sec="${sec}"]`).forEach(inp => { secSum += parseInt(inp.value || 0); });
                const subDisplay = document.getElementById(`sub-${team}-${sec}`);
                if(subDisplay) subDisplay.innerText = secSum;
                teamTotal += secSum;
                if(sec !== 'gen') { if(team === 'A') bestScoreA = Math.max(bestScoreA, secSum); else bestScoreB = Math.max(bestScoreB, secSum); }
            });
            if(team === 'A') totalA = teamTotal; else totalB = teamTotal;
        });
        document.getElementById('total-a').innerText = totalA;
        document.getElementById('total-b').innerText = totalB;
        return { totalA, totalB, bestScoreA, bestScoreB };
    }

    function submitScores(e) {
        e.preventDefault();
        const scores = calculateRubricTotals();
        const teamA_id = document.getElementById('score-team-id-a').value;
        const teamB_id = document.getElementById('score-team-id-b').value;
        
        let localWinner = null;
        if(scores.totalA > scores.totalB) localWinner = teamA_id;
        else if(scores.totalB > scores.totalA) localWinner = teamB_id;
        else {
            if(scores.bestScoreA > scores.bestScoreB) localWinner = teamA_id;
            else if(scores.bestScoreB > scores.bestScoreA) localWinner = teamB_id;
            else {
                const c = confirm(`EMPATE TOTAL (${scores.totalA}). ¿Ganó AF (Aceptar) o EC (Cancelar)?`);
                localWinner = c ? teamA_id : teamB_id;
            }
        }

        const judgeId = document.getElementById('judge-selector').value;
        const roundIdx = state.currentRound;
        const mIdx = state.rounds[roundIdx].findIndex(m => m.id === currentMatchupId);

        if(mIdx !== -1) {
            state.rounds[roundIdx][mIdx].judgeSubmissions[judgeId] = {
                scores: scores,
                winner: localWinner,
                nominations: {
                    mvp: document.getElementById('nom-mvp').value,
                    intro: document.getElementById('nom-intro').value,
                    r1: document.getElementById('nom-r1').value,
                    r2: document.getElementById('nom-r2').value,
                    conclu: document.getElementById('nom-conclu').value
                }
            };
            recalculateMatch(roundIdx, mIdx);
            saveState();
            alert("Guardado.");
            loadJudgeMatchups();
        }
    }

    function recalculateMatch(rIdx, mIdx) {
        const m = state.rounds[rIdx][mIdx];
        const submissions = Object.values(m.judgeSubmissions);
        if(submissions.length === 0) return;

        let avgA=0, avgB=0, avgBestA=0, avgBestB=0, votesA=0, votesB=0;
        submissions.forEach(sub => {
            avgA += sub.scores.totalA; avgB += sub.scores.totalB;
            avgBestA += sub.scores.bestScoreA; avgBestB += sub.scores.bestScoreB;
            if(sub.winner === m.teamA) votesA++; else votesB++;
        });
        avgA /= submissions.length; avgB /= submissions.length;
        avgBestA /= submissions.length; avgBestB /= submissions.length;

        m.finalScores = { totalA: avgA, totalB: avgB, bestA: avgBestA, bestB: avgBestB };
        
        if(avgA > avgB) m.winner = m.teamA;
        else if(avgB > avgA) m.winner = m.teamB;
        else {
            if(avgBestA > avgBestB) m.winner = m.teamA;
            else if(avgBestB > avgBestA) m.winner = m.teamB;
            else m.winner = (votesA >= votesB) ? m.teamA : m.teamB;
        }
        recalculateStandings();
    }

    function recalculateStandings() {
        state.teams.forEach(t => { t.wins=0; t.points=0; t.speakerPoints=0; t.opponents=[]; });
        state.rounds.forEach(round => {
            round.forEach(m => {
                const tA = state.teams.find(t=>t.id===m.teamA);
                const tB = state.teams.find(t=>t.id===m.teamB);
                if(!m.finalScores) return;
                tA.points += m.finalScores.totalA; tB.points += m.finalScores.totalB;
                tA.speakerPoints += m.finalScores.bestA; tB.speakerPoints += m.finalScores.bestB;
                if(!tA.opponents.includes(tB.id)) { tA.opponents.push(tB.id); tB.opponents.push(tA.id); }
                if(m.winner === tA.id) tA.wins++; else tB.wins++;
            });
        });
    }

    function renderStandingsAndAwards() {
        // 1. Standings
        const tbodySt = document.getElementById('standings-table-final').querySelector('tbody');
        tbodySt.innerHTML = '';
        const sortedTeams = [...state.teams].sort((a,b) => (b.wins - a.wins) || (b.points - a.points) || (b.speakerPoints - a.speakerPoints));
        sortedTeams.forEach((t, idx) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td><strong>${idx+1}</strong></td><td>${t.name}</td><td>${t.wins}</td><td>${t.points}</td>`;
            tbodySt.appendChild(tr);
        });

        // 2. Awards
        const tbodyAw = document.getElementById('awards-table-final').querySelector('tbody');
        tbodyAw.innerHTML = '';
        const cats = ['mvp','intro','r1','r2','conclu'];
        const counts = {};
        state.teams.forEach(t => t.members.forEach(m => counts[m.id]={name:m.name, team:t.name, mvp:0, intro:0, r1:0, r2:0, conclu:0, total:0}));
        state.rounds.flat().forEach(m => {
            if(m.judgeSubmissions) {
                Object.values(m.judgeSubmissions).forEach(sub => {
                    cats.forEach(c => {
                        const wid = sub.nominations[c];
                        if(wid && counts[wid]) { counts[wid][c]++; counts[wid].total++; }
                    });
                });
            }
        });
        cats.forEach(c => {
            const sorted = Object.values(counts).sort((a,b)=>b[c]-a[c]);
            const top = sorted[0];
            if(top && top[c]>0) {
                const tr = document.createElement('tr');
                const cn = {mvp:'🏆 MVP', intro:'🎤 Intro', r1:'⚔️ R1', r2:'🛡️ R2', conclu:'⚖️ Conclu'}[c];
                tr.innerHTML = `<td>${cn}</td><td>${top.name} <small class="text-gray-500">(${top.team})</small></td><td>${top[c]}</td>`;
                tbodyAw.appendChild(tr);
            }
        });
    }

    // Judge Export
    function exportJudgeResults() {
        if(!myAssignedMatches || myAssignedMatches.length === 0) return alert("Sin resultados.");
        const judgeId = document.getElementById('judge-selector').value;
        
        const data = [];
        myAssignedMatches.forEach(m => {
            const tA = state.teams.find(t=>t.id===m.teamA);
            const tB = state.teams.find(t=>t.id===m.teamB);
            const sub = m.judgeSubmissions[judgeId];
            
            if(sub) {
                const getNom = (k) => {
                    const mid = sub.nominations[k];
                    const mem = [...tA.members, ...tB.members].find(x => x.id === mid);
                    return mem ? mem.name : "";
                };

                data.push({
                    Ronda: state.currentRound + 1,
                    Debate: `${tA.name} vs ${tB.name}`,
                    Puntos_A: sub.scores.totalA,
                    Puntos_B: sub.scores.totalB,
                    Ganador: sub.winner === tA.id ? tA.name : tB.name,
                    MVP: getNom('mvp'),
                    Intro: getNom('intro'),
                    R1: getNom('r1'),
                    R2: getNom('r2'),
                    Conclu: getNom('conclu')
                });
            }
        });

        if(data.length === 0) return alert("No ha guardado nada.");

        const ws = XLSX.utils.json_to_sheet(data);
        const wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, ws, "Mis_Resultados");
        
        // FORCE DOWNLOAD FIX
        const wbout = XLSX.write(wb, {bookType:'xlsx', type:'array'});
        const blob = new Blob([wbout], {type: "application/octet-stream"});
        downloadFile(blob, "Resultados_Juez.xlsx");
    }

    window.onload = loadState;
</script>
</body>
</html>
