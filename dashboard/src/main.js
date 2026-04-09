const translations = {
    es: {
        nav_models: "MODELOS",
        nav_context: "CONTEXTO",
        nav_visualizations: "VISUALIZACIONES",
        nav_unicorn_cards: "Fichas Unicornio",
        nav_interactive_pitch: "Cancha Interactiva",
        nav_graphs: "Gráficas",
        title_xg_model: "Modelo xG (Nivel de Tiro)",
        title_match_predictor: "Match Predictor (Resultado)",
        title_clustering: "Clustering (K-Means & DBSCAN)",
        title_rf_cluster: "Random Forest + Cluster",
        title_obj: "Objetivo del Proyecto",
        title_hypothesis: "Hipótesis de Machine Learning",
        title_datasets: "Análisis de Datos y Estadísticas",
        title_vars: "Diccionario de Variables",
        title_eng: "Ingeniería de Características",
        title_metrics: "Salud y Calidad de los Datos",
        hero_subtitle: "MODELO DE ANALÍTICA AVANZADA",
        hero_title: "¿QUIERES PREDECIR EL<br>PRÓXIMO PARTIDO?",
        hero_desc: "Selecciona tus equipos y deja que el Machine Learning decida quién se llevará la victoria.",
        btn_results: "REALIZAR PREDICCIÓN",
        btn_model: "EXPLORAR EL MODELO",
        btn_close: "CERRAR",
        sec_models_title: "TECNOLOGÍAS DEL PROYECTO",
        unicorn_title: "Fichas",
        unicorn_subtitle: "Los jugadores que desafían la probabilidad estadística.",
        graphs_main_title: "Análisis de",
        graphs_accent_title: "Gráficas",
        graphs_subtitle: "Visualización avanzada de patrones ofensivos: Comparativa de disparos local vs visitante.",
        graph_local_title: "Shot Map - Local",
        graph_away_title: "Shot Map - Visitante",
        interpretation_label: "Interpretación",
        graph_local_interpretation: "Los datos locales muestran un volumen de disparos 22% superior. La confianza de jugar en casa permite remates desde zonas de media distancia con mayor frecuencia.",
        graph_away_interpretation: "Fuera de casa, los equipos son más selectivos. El 60% de los tiros se concentran dentro del corazón del área, buscando maximizar el xG ante menos oportunidades.",
        pitch_help_text: "Haz <strong>clic</strong> en cualquier zona de la cancha para calcular la probabilidad estadística de gol basada en el modelo xG entrenado con datos reales de la Premier League 2025-26.",
        ml_def: "<strong>Machine Learning:</strong> El motor principal del proyecto. Permite que el sistema 'aprenda' de miles de partidos históricos para encontrar patrones que un humano no vería a simple vista.",
        ml_vid: "xrQ1YH0PnrM",
        rf_def: "<strong>Random Forest:</strong> Nuestro modelo ganador. Funciona creando cientos de 'árboles de decisión' que votan por quién ganará, asegurando una predicción más robusta.",
        rf_vid: "v6VJ2RO66Ag",
        xg_def: "<strong>Models xG (Expected Goals):</strong> Mide la probabilidad de que cada tiro sea un gol basándose en la distancia y el ángulo. Es la métrica reina del fútbol moderno.",
        xg_vid: "", 
        cluster_def: "<strong>Clustering:</strong> Agrupamos a los jugadores no por su posición, sino por cómo juegan realmente, detectando estilos de juego únicos.",
        cluster_vid: "rWKM5sSSzLM",
        knn_def: "<strong>Modelos KNN:</strong> Algoritmo que clasifica resultados basándose en los 'vecinos más cercanos'. Ideal para encontrar similitudes históricas.",
        knn_vid: "gs9E7E0qOIc"
    },
    en: {
        nav_models: "MODELS",
        nav_context: "CONTEXT",
        nav_visualizations: "VISUALIZATIONS",
        nav_unicorn_cards: "Unicorn Cards",
        nav_interactive_pitch: "Interactive Pitch",
        nav_graphs: "Graphs",
        title_xg_model: "xG Model (Shot Level)",
        title_match_predictor: "Match Predictor (Outcome)",
        title_clustering: "Clustering (K-Means & DBSCAN)",
        title_rf_cluster: "Random Forest + Cluster",
        title_obj: "Project Objective",
        title_hypothesis: "Machine Learning Hypothesis",
        title_datasets: "Data & Statistics Analysis",
        title_vars: "Variable Dictionary",
        title_eng: "Feature Engineering",
        title_metrics: "Data Health & Quality",
        hero_subtitle: "ADVANCED ANALYTICS MODEL",
        hero_title: "WANT TO PREDICT THE<br>NEXT MATCH?",
        hero_desc: "Select your teams and let Machine Learning decide the winner.",
        btn_results: "PERFORM PREDICTION",
        btn_model: "EXPLORE THE MODEL",
        btn_close: "CLOSE",
        sec_models_title: "PROJECT TECHNOLOGIES",
        unicorn_title: "Unicorn",
        unicorn_subtitle: "Players who defy statistical probability.",
        graphs_main_title: "Analysis of",
        graphs_accent_title: "Graphs",
        graphs_subtitle: "Advanced visualization of offensive patterns: Home vs Away shot comparison.",
        graph_local_title: "Shot Map - Home",
        graph_away_title: "Shot Map - Away",
        interpretation_label: "Interpretation",
        graph_local_interpretation: "Home data shows a 22% higher shot volume. Playing at home increases confidence to shoot from medium distance zones more frequently.",
        graph_away_interpretation: "Away from home, teams are more selective. 60% of shots are concentrated within the heart of the box, seeking to maximize xG given fewer opportunities.",
        pitch_help_text: "<strong>Click</strong> anywhere on the pitch to calculate the statistical goal probability based on the xG model trained with real Premier League 2025-26 data.",
        ml_def: "<strong>Machine Learning:</strong> The core engine of the project. It allows the system to 'learn' from thousands of historical matches to find patterns.",
        ml_vid: "xrQ1YH0PnrM",
        rf_def: "<strong>Random Forest:</strong> Our winning model. It works by creating hundreds of 'decision trees' that vote for the winner, ensuring robust prediction.",
        rf_vid: "v6VJ2RO66Ag",
        xg_def: "<strong>Models xG (Expected Goals):</strong> Measures the probability of each shot being a goal based on distance and angle. Modern football's key metric.",
        xg_vid: "",
        cluster_def: "<strong>Clustering:</strong> We group players not by their position, but by how they actually play, detecting unique playing styles.",
        cluster_vid: "rWKM5sSSzLM",
        knn_def: "<strong>KNN Models:</strong> Algorithm that classifies outcomes based on 'nearest neighbors'. Ideal for finding historical similarities.",
        knn_vid: "gs9E7E0qOIc"
    }
};

let currentLang = 'es';

const langToggle = document.getElementById('lang-toggle');
const langText = document.getElementById('lang-text');

function updateLanguage(lang) {
    const translation = translations[lang];
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translation[key]) {
            element.innerHTML = translation[key];
        }
    });
    langText.textContent = lang.toUpperCase();
    
    const activeItem = document.querySelector('.model-item.active');
    if (activeItem) {
        showDefinition(activeItem.getAttribute('data-definition'));
    }
}

langToggle.addEventListener('click', () => {
    currentLang = currentLang === 'es' ? 'en' : 'es';
    updateLanguage(currentLang);
});

// Interacción de Iconos de Modelos (Solo si el elemento existe en el DOM)
const modelItems = document.querySelectorAll('.model-item');
const definitionBox = document.getElementById('definition-box');
const definitionText = document.getElementById('definition-text');
const closeDef = document.getElementById('close-def');

function showDefinition(defKey) {
    if (!definitionBox || !definitionText) return;
    
    const translation = translations[currentLang];
    const videoKey = defKey.replace('_def', '_vid');
    const videoId = translation[videoKey];
    
    let contentHtml = `<p>${translation[defKey]}</p>`;
    
    if (videoId) {
        contentHtml += `
            <div class="video-wrapper" style="margin-top: 20px;">
                <iframe 
                    width="100%" 
                    height="315" 
                    src="https://www.youtube-nocookie.com/embed/${videoId}?rel=0" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen>
                </iframe>
                <div style="margin-top: 15px; text-align: center;">
                    <a href="https://www.youtube.com/watch?v=${videoId}" target="_blank" class="secondary-button" style="display: inline-block; padding: 10px 20px; font-size: 11px;">
                        VER EN YOUTUBE <i class="fa-solid fa-up-right-from-square"></i>
                    </a>
                </div>
            </div>
        `;
    }
    
    definitionText.innerHTML = contentHtml;
    definitionBox.classList.remove('hidden');
    
    definitionBox.style.opacity = '0';
    setTimeout(() => {
        definitionBox.style.opacity = '1';
    }, 10);

    definitionBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

if (modelItems.length > 0) {
    modelItems.forEach(item => {
        item.addEventListener('click', () => {
            modelItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            
            const defKey = item.getAttribute('data-definition');
            showDefinition(defKey);
        });
    });
}

if (closeDef) {
    closeDef.addEventListener('click', () => {
        definitionBox.classList.add('hidden');
        modelItems.forEach(i => i.classList.remove('active'));
    });
}

// Smooth Scroll para la flecha
const scrollArrow = document.querySelector('.scroll-arrow');
if (scrollArrow) {
    scrollArrow.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({
            behavior: 'smooth'
        });
    });
}

// Force Play Video Fondo
document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('hero-video');
    if (video) {
        video.play().catch(error => console.log("Autoplay background blocked", error));
    }
});

// Scroll Reveal Effect Header
window.addEventListener('scroll', () => {
    const header = document.querySelector('.main-header');
    if (header) {
        if (window.scrollY > 50) {
            header.style.background = 'rgba(2, 6, 23, 0.9)'; // UEFA deep dark blur
            header.style.height = '80px';
        } else {
            header.style.background = 'rgba(2, 6, 23, 0.7)';
            header.style.height = '100px';
        }
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const teamSelector = document.getElementById('team-selector');
    const dynamicPlayerList = document.getElementById('dynamic-player-list');

    // Poblar el selector de equipos con TODOS LOS EQUIPOS si están disponibles
    if (teamSelector && typeof allTeams !== 'undefined') {
        teamSelector.innerHTML = '';
        allTeams.forEach(team => {
            const option = document.createElement('option');
            option.value = team;
            option.textContent = team;
            teamSelector.appendChild(option);
        });
        // Si no hay valor seleccionado por defecto, seleccionamos el primero
        if (allTeams.includes("Man City")) {
            teamSelector.value = "Man City";
        }
    }

    function renderPlayers(team) {
        if (!dynamicPlayerList) return;
        // Usamos la variable global de players_data.js y tomamos SOLO LOS MEJORES 3
        let players = [];
        if (typeof teamPlayersData !== 'undefined' && teamPlayersData[team]) {
            players = teamPlayersData[team].slice(0, 3);
        }
        
        dynamicPlayerList.innerHTML = '';
        
        if (players.length === 0) {
            dynamicPlayerList.innerHTML = '<p style="color: white; text-align: center; padding: 10px;">No hay datos para este equipo.</p>';
            return;
        }

        players.forEach(p => {
            dynamicPlayerList.innerHTML += `
                <div class="player-item" style="animation: fadeIn 0.3s ease-in-out;">
                    <div class="player-avatar ${p.isSuper ? 'halaand' : ''}">${p.init}</div>
                    <div class="player-info">
                        <span class="player-name">${p.name}</span>
                        <span class="player-club">${team}</span>
                    </div>
                    <div class="player-stats">
                        <span class="stat-badge ${p.style}">xG ${p.xg}/90</span>
                        <span class="market-value">£${p.price}</span>
                    </div>
                </div>
            `;
        });
    }

    // Initial render
    renderPlayers(teamSelector.value);
});

// Función para renderizar mini-canchas 3D en la sección de Gráficas
function initAnalysisGraphs() {
    const localCanvas = document.getElementById('canvas-local-shots');
    const awayCanvas = document.getElementById('canvas-away-shots');
    
    if (!localCanvas || !awayCanvas) return;

    const renderMiniPitch = (canvas, type) => {
        const ctx = canvas.getContext('2d');
        const dpr = window.devicePixelRatio || 1;
        const w = canvas.offsetWidth;
        const h = canvas.offsetHeight;
        
        canvas.width = w * dpr;
        canvas.height = h * dpr;
        ctx.scale(dpr, dpr);

        // Perspective corners for mini pitch
        const corners = {
            fl: { x: w * 0.15, y: h * 0.1 },
            fr: { x: w * 0.85, y: h * 0.1 },
            nl: { x: w * 0.05, y: h * 0.85 },
            nr: { x: w * 0.95, y: h * 0.85 }
        };

        const miniF2C = (fx, fy) => {
            const { fl, fr, nl, nr } = corners;
            const tx = fl.x + (fx / 100) * (fr.x - fl.x);
            const ty = fl.y + (fx / 100) * (fr.y - fl.y);
            const bx = nl.x + (fx / 100) * (nr.x - nl.x);
            const by = nl.y + (fx / 100) * (nr.y - nl.y);
            const t = fy / 60;
            return { x: tx + t * (bx - tx), y: ty + t * (by - ty) };
        };

        // Draw Pitch Slab and Surface
        ctx.fillStyle = '#111827';
        ctx.fillRect(0,0,w,h);
        
        ctx.beginPath();
        ctx.moveTo(corners.fl.x, corners.fl.y);
        ctx.lineTo(corners.fr.x, corners.fr.y);
        ctx.lineTo(corners.nr.x, corners.nr.y);
        ctx.lineTo(corners.nl.x, corners.nl.y);
        ctx.closePath();
        ctx.fillStyle = '#064e3b';
        ctx.fill();
        ctx.strokeStyle = 'rgba(255,255,255,0.3)';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Draw Markings
        ctx.strokeStyle = 'rgba(255,255,255,0.2)';
        const drawLine = (x1, y1, x2, y2) => {
            const p1 = miniF2C(x1, y1), p2 = miniF2C(x2, y2);
            ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
        };
        drawLine(50, 0, 50, 60); // Center line
        drawLine(0, 15, 16.5, 15); drawLine(16.5, 15, 16.5, 45); drawLine(16.5, 45, 0, 45); // Left area
        drawLine(100, 15, 83.5, 15); drawLine(83.5, 15, 83.5, 45); drawLine(83.5, 45, 100, 45); // Right area

        // Render Data Points (Simulated based on aggregate data for visual density)
        const teamData = PITCH_DATA["Man City"] || Object.values(PITCH_DATA)[0];
        const shots = type === 'local' ? teamData.shots.slice(0, 40) : teamData.shots.slice(20, 50);
        const color = type === 'local' ? '#22c55e' : '#38bdf8';

        shots.forEach(s => {
            const p = miniF2C(s[0], s[1] * 0.6);
            ctx.beginPath();
            ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
            ctx.fillStyle = s[2] === 'Goal' ? '#ef4444' : color;
            ctx.fill();
        });
    };

    renderMiniPitch(localCanvas, 'local');
    renderMiniPitch(awayCanvas, 'away');
}

// Extender openModal para que llame a initAnalysisGraphs
const originalOpenModal = window.openModal;
window.openModal = function(id) {
    if (typeof originalOpenModal === 'function') {
        originalOpenModal(id);
    } else {
        // Fallback si no estaba definida antes
        const modal = document.getElementById(id);
        if(modal) {
            modal.classList.remove('hidden');
            document.body.classList.add('modal-open');
            window.dispatchEvent(new Event('resize'));
        }
    }
    
    if (id === 'section-graphs') {
        setTimeout(initAnalysisGraphs, 150);
    }
};

// =============================================================================
// PITCH SIMULATOR - now delegates to pitch3d.js
// =============================================================================

const simDistText  = document.getElementById('sim-dist');
const simAngleText = document.getElementById('sim-angle');
const simXgText    = document.getElementById('sim-xg');
const haalandSwitch= document.getElementById('haaland-effect');
const teamFilter   = document.getElementById('pitch-team-filter');
const layerBtns    = document.querySelectorAll('.layer-btn');

const layerDescriptions = {
    sim:       "Simulador Interactivo: Calcula el xG (Goles Esperados) haciendo clic en la cancha. Considera distancia y ángulo al arco.",
    goals:     "Mapa de Goles: Ubicación exacta de los goles anotados durante la temporada.",
    shots:     "Mapa de Tiros: Distribución de todos los remates. Verde=Gol, Azul=Parada, Amarillo=Bloqueado.",
    heatmap:   "Estructura xG: Zonificación de peligrosidad. Zonas más brillantes = mayor probabilidad histórica de gol.",
    positions: "Posiciones Promedio: Ubicación táctica media de cada jugador. Útil para analizar el esquema del equipo."
};

let activeLayer = 'sim';
let currentTeam = 'all';

function initPitch() {
    layerBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            layerBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            activeLayer = btn.getAttribute('data-layer');
            const descText = document.getElementById('pitch-desc-text');
            if (descText) descText.textContent = layerDescriptions[activeLayer];
            // Sync new pitch-tab buttons
            document.querySelectorAll('.pitch-tab').forEach(t => {
                t.classList.toggle('active', t.getAttribute('data-layer') === activeLayer);
            });
            drawPitch3D();
            renderActiveLayer();
        });
    });

    // Wire up new premium .pitch-tab buttons
    document.querySelectorAll('.pitch-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.pitch-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            activeLayer = tab.getAttribute('data-layer');
            // Sync old layer-btn buttons
            layerBtns.forEach(b => {
                b.classList.toggle('active', b.getAttribute('data-layer') === activeLayer);
            });
            const descText = document.getElementById('pitch-desc-text');
            if (descText) descText.textContent = layerDescriptions[activeLayer];
            drawPitch3D();
            renderActiveLayer();
        });
    });

    if (teamFilter) {
        teamFilter.addEventListener('change', e => {
            currentTeam = e.target.value;
            renderActiveLayer();
        });
    }

    // Init the Canvas 3D engine (defined in pitch3d.js)
    setupPitchCanvas();
}

function renderActiveLayer() {
    clearOverlayLayers();
    const data = (currentTeam === 'all') ? aggregateAllData() : PITCH_DATA[currentTeam];
    if (!data) return;
    switch (activeLayer) {
        case 'goals':     overlayGoals(data.goals); break;
        case 'shots':     overlayShots(data.shots); break;
        case 'heatmap':   overlayHeatmap(data); break;
        case 'positions': overlayPositions(data.player_positions); break;
    }
}

function aggregateAllData() {
    const all = { goals: [], shots: [], player_positions: [] };
    Object.values(PITCH_DATA).forEach(team => {
        all.goals.push(...team.goals.slice(0, 8));
        all.shots.push(...team.shots.slice(0, 8));
    });
    return all;
}

// FIFA Carousel
const carousel = document.querySelector('.fifa-carousel');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
if (carousel && prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => carousel.scrollBy({ left: -330, behavior: 'smooth' }));
    nextBtn.addEventListener('click', () => carousel.scrollBy({ left: 330, behavior: 'smooth' }));
}

function calculateXG(fieldX, fieldY) {
    const goalX = 100, goalY = 30;
    const dx = (goalX - fieldX) * 1.05;
    const dy = (fieldY - goalY) * 1.13;
    const distance = Math.sqrt(dx*dx + dy*dy);
    const y1 = fieldY - 26.34, y2 = fieldY - 33.66;
    const a = Math.sqrt(dx*dx + y1*y1), b = Math.sqrt(dx*dx + y2*y2);
    let cosTheta = (a*a + b*b - 7.32*7.32) / (2 * a * b);
    cosTheta = Math.max(-1, Math.min(1, cosTheta));
    const angleRad = Math.acos(cosTheta);
    let xG = (angleRad / Math.PI) * Math.exp(-0.08 * distance);
    if (haalandSwitch && haalandSwitch.checked) xG *= 1.55;
    xG = Math.min(0.99, Math.max(0.01, xG));

    const color = xG > 0.4 ? '#22c55e' : (xG > 0.15 ? '#eab308' : '#f43f5e');

    if (simDistText)  simDistText.textContent  = `${distance.toFixed(1)} m`;
    if (simAngleText) simAngleText.textContent  = `${((angleRad * 180) / Math.PI).toFixed(1)}°`;
    if (simXgText) {
        simXgText.textContent = xG.toFixed(2);
        simXgText.style.color = color;
    }

    // Animate SVG ring gauge
    const ringEl = document.getElementById('xg-ring-progress');
    if (ringEl) {
        const circumference = 326.73;
        ringEl.setAttribute('stroke-dashoffset', circumference * (1 - xG));
        ringEl.setAttribute('stroke', color);
    }

    // Animate bar fill
    const barFill = document.getElementById('xg-bar-fill');
    if (barFill) {
        barFill.style.width = (xG * 100) + '%';
    }
}

document.addEventListener('DOMContentLoaded', initPitch);
