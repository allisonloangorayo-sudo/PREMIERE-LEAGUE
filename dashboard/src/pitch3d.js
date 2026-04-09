// ============================================================
//  3D CANVAS PITCH ENGINE
//  Produces an isometric-perspective football pitch like the
//  reference image (slab + stripes + markings + goals).
// ============================================================

let pCanvas, pCtx, pW, pH;
let pCorners = {}; // canvas pixel coords for the 4 field corners
let pitchZoom = 1.0;

// Map field coords (x: 0-100 left→right, y: 0-60 far→near) to canvas px
function f2c(fx, fy) {
    const { fl, fr, nl, nr } = pCorners;
    const tx = fl.x + (fx / 100) * (fr.x - fl.x);
    const ty = fl.y + (fx / 100) * (fr.y - fl.y);
    const bx = nl.x + (fx / 100) * (nr.x - nl.x);
    const by = nl.y + (fx / 100) * (nr.y - nl.y);
    const t = fy / 60;
    return { x: tx + t * (bx - tx), y: ty + t * (by - ty) };
}

function setupPitchCanvas() {
    pCanvas = document.getElementById('pitch-canvas');
    if (!pCanvas) return;

    const resize = () => {
        const dpr = window.devicePixelRatio || 1;
        const container = pCanvas.parentElement;
        pW = container.clientWidth;
        pH = Math.round(pW * 0.58);

        // Set CSS size explicitly so container knows its height
        pCanvas.style.width  = pW + 'px';
        pCanvas.style.height = pH + 'px';

        // Set actual pixel buffer for DPR
        pCanvas.width  = Math.round(pW * dpr);
        pCanvas.height = Math.round(pH * dpr);

        pCtx = pCanvas.getContext('2d');
        pCtx.scale(dpr, dpr);

        // Sync the SVG overlay to same pixel dimensions
        const svg = document.getElementById('soccer-field');
        if (svg) {
            svg.style.width  = pW + 'px';
            svg.style.height = pH + 'px';
            svg.setAttribute('width',  pW);
            svg.setAttribute('height', pH);
            svg.setAttribute('viewBox', `0 0 ${pW} ${pH}`);
            // Ensure layers exist
            ['layer-heatmap','layer-goals','layer-shots','layer-positions'].forEach(id => {
                if (!svg.querySelector('#' + id)) {
                    const g = document.createElementNS("http://www.w3.org/2000/svg","g");
                    g.id = id; svg.appendChild(g);
                }
            });
        }

        // Define perspective corners
        pCorners = {
            fl: { x: pW * 0.21, y: pH * 0.05 },
            fr: { x: pW * 0.79, y: pH * 0.05 },
            nl: { x: pW * 0.01, y: pH * 0.80 },
            nr: { x: pW * 0.99, y: pH * 0.80 },
        };

        drawPitch3D();
        renderActiveLayer();
    };

    resize();
    window.addEventListener('resize', resize);

    // Click handler for xG simulator
    pCanvas.addEventListener('click', (e) => {
        if (activeLayer !== 'sim') return;
        const rect = pCanvas.getBoundingClientRect();
        const mx = (e.clientX - rect.left) * (pW / rect.width);
        const my = (e.clientY - rect.top) * (pH / rect.height);
        const fc = canvasToField(mx, my);
        if (fc) {
            placeShotMarker(fc.x, fc.y);
            calculateXG(fc.x, fc.y);
        }
    });

    // Zoom buttons
    const zi = document.getElementById('zoom-in');
    const zo = document.getElementById('zoom-out');
    const zr = document.getElementById('zoom-reset');
    if (zi) zi.addEventListener('click', () => { pitchZoom = Math.min(2.0, pitchZoom + 0.15); resize(); });
    if (zo) zo.addEventListener('click', () => { pitchZoom = Math.max(0.7, pitchZoom - 0.15); resize(); });
    if (zr) zr.addEventListener('click', () => { pitchZoom = 1.0; resize(); });
}

// Invert f2c for click detection (approximate)
function canvasToField(cx, cy) {
    const { fl, fr, nl, nr } = pCorners;
    // Simple iterative search: find (fx,fy) whose f2c is closest to (cx,cy)
    let bestDist = Infinity, best = null;
    const steps = 50;
    for (let xi = 0; xi <= steps; xi++) {
        for (let yi = 0; yi <= steps; yi++) {
            const fx = xi / steps * 100;
            const fy = yi / steps * 60;
            const p = f2c(fx, fy);
            const d = (p.x - cx) ** 2 + (p.y - cy) ** 2;
            if (d < bestDist) { bestDist = d; best = { x: fx, y: fy }; }
        }
    }
    return best;
}

// Place a canvas-layer shot marker dot
let markerPos = null;
function placeShotMarker(fx, fy) {
    markerPos = { x: fx, y: fy };
    drawPitch3D();
}

// Main 3D render
function drawPitch3D() {
    if (!pCtx) return;
    const ctx = pCtx;
    const { fl, fr, nl, nr } = pCorners;
    const W = pW, H = pH;
    const SLAB = H * 0.09;

    ctx.clearRect(0, 0, W, H);

    // ── SHADOW under slab ──
    const shadow = ctx.createLinearGradient(0, nl.y + SLAB, 0, nl.y + SLAB + 30);
    shadow.addColorStop(0, 'rgba(0,0,0,0.35)');
    shadow.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.beginPath();
    ctx.moveTo(nl.x - 20, nl.y + SLAB);
    ctx.lineTo(nr.x + 20, nr.y + SLAB);
    ctx.lineTo(nr.x + 30, nl.y + SLAB + 30);
    ctx.lineTo(nl.x - 30, nl.y + SLAB + 30);
    ctx.closePath();
    ctx.fillStyle = shadow;
    ctx.fill();

    // ── SLAB: Left face ──
    ctx.beginPath();
    ctx.moveTo(fl.x, fl.y);
    ctx.lineTo(nl.x, nl.y);
    ctx.lineTo(nl.x, nl.y + SLAB);
    ctx.lineTo(fl.x, fl.y + SLAB * 0.25);
    ctx.closePath();
    ctx.fillStyle = '#033d2a';
    ctx.fill();

    // ── SLAB: Right face ──
    ctx.beginPath();
    ctx.moveTo(fr.x, fr.y);
    ctx.lineTo(nr.x, nr.y);
    ctx.lineTo(nr.x, nr.y + SLAB);
    ctx.lineTo(fr.x, fr.y + SLAB * 0.25);
    ctx.closePath();
    ctx.fillStyle = '#055c40';
    ctx.fill();

    // ── SLAB: Front face ──
    ctx.beginPath();
    ctx.moveTo(nl.x, nl.y);
    ctx.lineTo(nr.x, nr.y);
    ctx.lineTo(nr.x, nr.y + SLAB);
    ctx.lineTo(nl.x, nl.y + SLAB);
    ctx.closePath();
    const fg = ctx.createLinearGradient(0, nl.y, 0, nl.y + SLAB);
    fg.addColorStop(0, '#067358');
    fg.addColorStop(1, '#022c22');
    ctx.fillStyle = fg;
    ctx.fill();

    // ── FIELD SURFACE: alternating stripe clipped to trapezoid ──
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(fl.x, fl.y); ctx.lineTo(fr.x, fr.y);
    ctx.lineTo(nr.x, nr.y); ctx.lineTo(nl.x, nl.y);
    ctx.closePath();
    ctx.clip();

    const stripes = 14;
    for (let i = 0; i < stripes; i++) {
        const x1 = i / stripes * 100, x2 = (i + 1) / stripes * 100;
        const p1 = f2c(x1, 0), p2 = f2c(x2, 0);
        const p3 = f2c(x2, 60), p4 = f2c(x1, 60);
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.lineTo(p3.x, p3.y);
        ctx.lineTo(p4.x, p4.y);
        ctx.closePath();

        const mid = f2c((x1 + x2) / 2, 0);
        const mid2 = f2c((x1 + x2) / 2, 60);
        const sg = ctx.createLinearGradient(mid.x, mid.y, mid2.x, mid2.y);
        if (i % 2 === 0) {
            sg.addColorStop(0,   '#14532d');
            sg.addColorStop(0.45,'#1d9b50');
            sg.addColorStop(1,   '#15803d');
        } else {
            sg.addColorStop(0,   '#166534');
            sg.addColorStop(0.45,'#22c55e');
            sg.addColorStop(1,   '#1a8a45');
        }
        ctx.fillStyle = sg;
        ctx.fill();
    }

    // Surface highlight (center glow)
    const glow = ctx.createRadialGradient(W / 2, H * 0.42, 0, W / 2, H * 0.42, W * 0.38);
    glow.addColorStop(0, 'rgba(255,255,255,0.07)');
    glow.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H);

    ctx.restore();

    // ── FIELD MARKINGS ──
    ctx.strokeStyle = 'rgba(255,255,255,0.88)';
    ctx.lineWidth = 1.6;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';

    const dL = (x1, y1, x2, y2) => {
        const a = f2c(x1, y1), b = f2c(x2, y2);
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
    };
    const dR = (x1, y1, x2, y2) => {
        const ps = [f2c(x1,y1), f2c(x2,y1), f2c(x2,y2), f2c(x1,y2)];
        ctx.beginPath();
        ctx.moveTo(ps[0].x, ps[0].y);
        ps.forEach(p => ctx.lineTo(p.x, p.y));
        ctx.closePath(); ctx.stroke();
    };
    const dE = (cx_, cy_, rx, ry) => {
        ctx.beginPath();
        for (let i = 0; i <= 64; i++) {
            const a = (i / 64) * Math.PI * 2;
            const p = f2c(cx_ + rx * Math.cos(a), cy_ + ry * Math.sin(a));
            i === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y);
        }
        ctx.closePath(); ctx.stroke();
    };
    const dSpot = (x, y) => {
        const p = f2c(x, y);
        ctx.beginPath(); ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255,255,255,0.88)'; ctx.fill();
    };

    // Boundary
    dR(0, 0, 100, 60);
    // Halfway
    dL(50, 0, 50, 60);
    // Center circle (rx=9.15, ry adjusted for perspective ratio)
    dE(50, 30, 9.15, 9.15 * 0.6);
    dSpot(50, 30);

    // Left penalty & goal areas
    dR(0, 13.85, 16.5, 46.15);
    dR(0, 24.85, 5.5, 35.15);
    dSpot(11, 30);

    // Right penalty & goal areas
    dR(83.5, 13.85, 100, 46.15);
    dR(94.5, 24.85, 100, 35.15);
    dSpot(89, 30);

    // Corner arcs (approximate quarter circles)
    [[0,0,1,1],[100,0,-1,1],[0,60,1,-1],[100,60,-1,-1]].forEach(([cx,cy,sx,sy]) => {
        ctx.beginPath();
        for (let i = 0; i <= 12; i++) {
            const a = (i / 12) * Math.PI / 2;
            const p = f2c(cx + sx * Math.sin(a), cy + sy * Math.cos(a));
            i === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y);
        }
        ctx.stroke();
    });

    // ── GOALS (3D-looking boxes) ──
    const goalTop = 26.34, goalBot = 33.66, goalD = 3.5;
    // Left goal
    ctx.strokeStyle = 'rgba(255,255,255,0.9)';
    ctx.lineWidth = 1.8;
    const lg = [f2c(0,goalTop), f2c(0,goalBot), f2c(-goalD,goalBot), f2c(-goalD,goalTop)];
    ctx.beginPath();
    ctx.moveTo(lg[0].x, lg[0].y); lg.forEach(p => ctx.lineTo(p.x, p.y));
    ctx.closePath(); ctx.stroke();
    ctx.fillStyle = 'rgba(255,255,255,0.06)'; ctx.fill();

    // Right goal
    const rg = [f2c(100,goalTop), f2c(100,goalBot), f2c(100+goalD,goalBot), f2c(100+goalD,goalTop)];
    ctx.beginPath();
    ctx.moveTo(rg[0].x, rg[0].y); rg.forEach(p => ctx.lineTo(p.x, p.y));
    ctx.closePath(); ctx.stroke();
    ctx.fillStyle = 'rgba(255,255,255,0.06)'; ctx.fill();

    // Corner flags (red triangles matching reference)
    [[0,0],[100,0],[0,60],[100,60]].forEach(([fx,fy]) => {
        const p = f2c(fx, fy);
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3.5, 0, Math.PI * 2);
        ctx.fillStyle = '#ef4444'; ctx.fill();
    });

    // ── SHOT MARKER (sim layer) ──
    if (activeLayer === 'sim' && markerPos) {
        const mp = f2c(markerPos.x, markerPos.y);
        ctx.beginPath();
        ctx.arc(mp.x, mp.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255,255,255,0.25)'; ctx.fill();
        ctx.beginPath();
        ctx.arc(mp.x, mp.y, 3.5, 0, Math.PI * 2);
        ctx.fillStyle = '#22c55e'; ctx.fill();
        ctx.strokeStyle = '#fff'; ctx.lineWidth = 1.5;
        ctx.stroke();
    }
}

// ── OVERLAY: render data on top of 3D canvas ──
// We use the SVG overlay for data points, mapping field coords → canvas px

function getSVGOverlay() { return document.getElementById('soccer-field'); }

function clearOverlayLayers() {
    const svg = getSVGOverlay();
    if (!svg) return;
    ['layer-heatmap','layer-goals','layer-shots','layer-positions'].forEach(id => {
        let el = svg.querySelector('#' + id);
        if (!el) { el = document.createElementNS("http://www.w3.org/2000/svg","g"); el.id = id; svg.appendChild(el); }
        else el.innerHTML = '';
    });
}

function ensureOverlayViewBox() {
    const svg = getSVGOverlay();
    if (!svg || !pW) return;
    svg.setAttribute('viewBox', `0 0 ${pW} ${pH}`);
    svg.setAttribute('width', pW);
    svg.setAttribute('height', pH);
}

// Called by main.js renderGoals / renderShots / etc.
function overlayGoals(goals) {
    ensureOverlayViewBox();
    const svg = getSVGOverlay();
    const layer = svg.querySelector('#layer-goals');
    if (!layer) return;
    const tooltip = document.getElementById('pitch-tooltip');
    goals.forEach(g => {
        const p = f2c(g[0], g[1] * 0.6);
        const circle = document.createElementNS("http://www.w3.org/2000/svg","circle");
        circle.setAttribute('cx', p.x); circle.setAttribute('cy', p.y);
        circle.setAttribute('r', '6'); circle.setAttribute('fill','#f43f5e');
        circle.setAttribute('stroke','#fff'); circle.setAttribute('stroke-width','1');
        circle.setAttribute('opacity','0.85');
        circle.style.cursor = 'pointer';
        circle.addEventListener('mouseenter', () => {
            if(tooltip){ tooltip.style.display='block'; tooltip.innerHTML=`<b>⚽ GOL</b><br>Pos: ${g[0].toFixed(1)}, ${g[1].toFixed(1)}`; }
        });
        circle.addEventListener('mousemove', (e) => {
            if(tooltip){
                const r = document.getElementById('interactive-pitch').getBoundingClientRect();
                tooltip.style.left=(e.clientX-r.left+15)+'px';
                tooltip.style.top=(e.clientY-r.top+15)+'px';
            }
        });
        circle.addEventListener('mouseleave', () => { if(tooltip) tooltip.style.display='none'; });
        layer.appendChild(circle);
    });
}

function overlayShots(shots) {
    ensureOverlayViewBox();
    const svg = getSVGOverlay();
    const layer = svg.querySelector('#layer-shots');
    if (!layer) return;
    const tooltip = document.getElementById('pitch-tooltip');
    shots.forEach(s => {
        const p = f2c(s[0], s[1] * 0.6);
        const outcome = s[2] || 'Unknown';
        let fill = '#64748b';
        let label = 'Fallido';
        if (outcome === 'Goal' || outcome === 'Successful') { fill = '#f43f5e'; label = 'Gol'; }
        else if (outcome === 'Saved') { fill = '#38bdf8'; label = 'Parada'; }
        else if (outcome === 'Blocked') { fill = '#f59e0b'; label = 'Bloqueado'; }
        const rect = document.createElementNS("http://www.w3.org/2000/svg","rect");
        rect.setAttribute('x', p.x-4); rect.setAttribute('y', p.y-4);
        rect.setAttribute('width','8'); rect.setAttribute('height','8');
        rect.setAttribute('fill', fill); rect.setAttribute('opacity','0.8');
        rect.setAttribute('rx','1'); rect.style.cursor='pointer';
        rect.addEventListener('mouseenter', () => {
            if(tooltip){ tooltip.style.display='block'; tooltip.innerHTML=`<b>${label}</b><br>${outcome}`; }
        });
        rect.addEventListener('mousemove', (e) => {
            if(tooltip){
                const r = document.getElementById('interactive-pitch').getBoundingClientRect();
                tooltip.style.left=(e.clientX-r.left+15)+'px';
                tooltip.style.top=(e.clientY-r.top+15)+'px';
            }
        });
        rect.addEventListener('mouseleave', () => { if(tooltip) tooltip.style.display='none'; });
        layer.appendChild(rect);
    });
}

function overlayHeatmap(data) {
    ensureOverlayViewBox();
    const svg = getSVGOverlay();
    const layer = svg.querySelector('#layer-heatmap');
    if (!layer) return;
    for (let xi = 0; xi < 10; xi++) {
        for (let yi = 0; yi < 6; yi++) {
            const x1 = xi*10, y1 = yi*10, x2 = x1+10, y2 = y1+10;
            const count = data.goals.filter(g => g[0]>=x1&&g[0]<x2&&(g[1]*0.6)>=y1&&(g[1]*0.6)<y2).length;
            if (count === 0) continue;
            const opacity = Math.min(0.65, count * 0.15);
            const corners = [f2c(x1,y1), f2c(x2,y1), f2c(x2,y2), f2c(x1,y2)];
            const poly = document.createElementNS("http://www.w3.org/2000/svg","polygon");
            poly.setAttribute('points', corners.map(p=>`${p.x},${p.y}`).join(' '));
            poly.setAttribute('fill','#f43f5e'); poly.setAttribute('opacity', opacity);
            layer.appendChild(poly);
        }
    }
}

function overlayPositions(positions) {
    ensureOverlayViewBox();
    const svg = getSVGOverlay();
    const layer = svg.querySelector('#layer-positions');
    if (!layer) return;
    const tooltip = document.getElementById('pitch-tooltip');
    positions.forEach(p => {
        const cp = f2c(p.x, p.y * 0.6);
        const g = document.createElementNS("http://www.w3.org/2000/svg","g");
        g.style.cursor = 'pointer';

        const circle = document.createElementNS("http://www.w3.org/2000/svg","circle");
        circle.setAttribute('cx', cp.x); circle.setAttribute('cy', cp.y);
        circle.setAttribute('r','9'); circle.setAttribute('fill','#1e40af');
        circle.setAttribute('stroke','#fff'); circle.setAttribute('stroke-width','1.5');

        const text = document.createElementNS("http://www.w3.org/2000/svg","text");
        text.setAttribute('x', cp.x); text.setAttribute('y', cp.y + 18);
        text.setAttribute('fill','#fff'); text.setAttribute('font-size','9');
        text.setAttribute('text-anchor','middle'); text.setAttribute('font-weight','600');
        text.textContent = p.name.split(' ').pop();

        g.addEventListener('mouseenter', () => {
            if(tooltip){ tooltip.style.display='block'; tooltip.innerHTML=`<b>${p.name}</b><br>Pos. Promedio`; }
        });
        g.addEventListener('mousemove', (e) => {
            if(tooltip){
                const r = document.getElementById('interactive-pitch').getBoundingClientRect();
                tooltip.style.left=(e.clientX-r.left+15)+'px';
                tooltip.style.top=(e.clientY-r.top+15)+'px';
            }
        });
        g.addEventListener('mouseleave', () => { if(tooltip) tooltip.style.display='none'; });

        g.appendChild(circle); g.appendChild(text);
        layer.appendChild(g);
    });
}
