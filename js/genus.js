// genus.js — detailpagina per genus

const MAANDEN = ['jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec'];
const MAAND_LABEL = {
  jan:'Januari', feb:'Februari', mrt:'Maart', apr:'April', mei:'Mei', jun:'Juni',
  jul:'Juli', aug:'Augustus', sep:'September', okt:'Oktober', nov:'November', dec:'December'
};

let _favVP = new Set(JSON.parse(localStorage.getItem('mj_fav') || '[]'));
let _favBH = new Set(JSON.parse(localStorage.getItem('mj_fav_bh') || '[]'));

function saveFav(bron) {
  if (bron === 'bh') localStorage.setItem('mj_fav_bh', JSON.stringify([..._favBH]));
  else localStorage.setItem('mj_fav', JSON.stringify([..._favVP]));
}

// laadAfbeelding() in shared.js roept imgObserver.unobserve() aan — hier dummy zodat er geen fout ontstaat.
const imgObserver = new IntersectionObserver(() => {});

function genusFlower(c) {
  const pts = [0,60,120,180,240,300].map(a => {
    const x = 60 + 13*Math.cos(a*Math.PI/180), y = 22 + 13*Math.sin(a*Math.PI/180);
    return `<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="7" ry="5" fill="${c}" opacity="0.8" transform="rotate(${a},${x.toFixed(1)},${y.toFixed(1)})"/>`;
  }).join('');
  return `<svg viewBox="0 0 120 90" style="background:${c}15;width:100%;height:100%">
    <ellipse cx="60" cy="80" rx="52" ry="8" fill="${c}20"/>
    <line x1="60" y1="80" x2="60" y2="22" stroke="${c}77" stroke-width="2.5"/>
    <ellipse cx="44" cy="55" rx="10" ry="4" fill="#4a7c5955" transform="rotate(-25,44,55)"/>
    <ellipse cx="76" cy="57" rx="10" ry="4" fill="#4a7c5955" transform="rotate(25,76,57)"/>
    ${pts}
    <circle cx="60" cy="22" r="6" fill="${c}"/>
    <circle cx="60" cy="22" r="2.5" fill="white" opacity="0.4"/>
  </svg>`;
}

function laadHereFoto(el, latinNaam, wikiSlug) {
  const slug = (wikiSlug || latinNaam).replace(/ /g, '_');
  fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(slug)}`)
    .then(r => r.ok ? r.json() : Promise.reject())
    .then(data => {
      const url = data.originalimage?.source || data.thumbnail?.source;
      if (!url) { el.classList.add('geladen'); return; }
      const img = el.querySelector('img');
      img.onload = () => { img.classList.add('geladen'); el.classList.add('geladen'); };
      img.src = url;
    })
    .catch(() => el.classList.add('geladen'));
}

function hBadge(p) {
  const bg = {hoog:'#e8f0e8',middel:'#fdf3e3',laag:'#fdecea',klein:'#fdecea',groot:'#e8f0e8'}[p.h] || '#ebebea';
  const tx = {hoog:'#2d4a2d',middel:'#7a5a20',laag:'#8b3a2a',klein:'#8b3a2a',groot:'#2d4a2d'}[p.h] || '#444';
  const lb = {hoog:'Hoog >60cm',middel:'Middel 30–60cm',laag:'Laag <30cm',klein:'Klein <3m',groot:'Groot >8m'}[p.h] || p.h;
  return `<span class="badge badge-${p.h}" style="background:${bg};color:${tx}">${lb}</span>`;
}

function catBadge(p) {
  const cls = {
    bodembedekker:'badge-bodem', siergras:'badge-gras', klimplant:'badge-klimplant',
    boom:'badge-boom', heester:'badge-heester', conifeer:'badge-conifeer'
  }[p.cat] || 'badge-vaste';
  return `<span class="badge ${cls}">${p.cat}</span>`;
}

function lichtPill(p) {
  if (p.licht === 'schaduw') return `<span class="pill pill-schaduw">🌑 schaduw</span>`;
  if (p.licht === 'halfschaduw') return `<span class="pill pill-halfschaduw">🌤 halfschaduw</span>`;
  return `<span class="pill pill-sun">☀️ zon</span>`;
}

function renderCultivars(p, bron) {
  const fav = bron === 'bh' ? _favBH : _favVP;
  const cvHTML = p.cv.map(cv => {
    const id = `${p.l}||${cv.name}`;
    const starred = fav.has(id);
    return `<div class="cv-detail cultivar">
      <div class="cv-header">
        <div><span class="cv-name">${cv.name}</span><span class="cv-height">· ${cv.hoogte}</span></div>
        <div style="display:flex;gap:0.3rem;align-items:center">
          <button class="cv-fav${starred?' active':''}" data-fav="${id}" data-bron="${bron}" title="Favoriet">${starred?'★':'☆'}</button>
          <a class="cv-photo" href="${glink(p.l,cv.name)}" target="_blank" rel="noopener">📷 foto</a>
        </div>
      </div>
      <div class="cv-color"><span class="cv-dot" style="background:${kleurBg(cv.kleur,p.c)}"></span><span class="cv-kleur">${cv.kleur}</span></div>
      <div class="cv-tip">${cv.tip}</div>
    </div>`;
  }).join('');
  return `<div class="detail-sectie">
    <div class="detail-sectie-titel">🌿 Alle varianten (${p.cv.length})</div>
    <div class="cv-detail-list">${cvHTML}</div>
  </div>`;
}

function renderZorgkalender(p) {
  if (!p.zorgkalender) return '';
  const taken = MAANDEN.filter(m => p.zorgkalender[m]);
  if (taken.length === 0) return '';
  const maandHTML = taken.map(m => `
    <div class="zk-maand">
      <div class="zk-maand-naam">${MAAND_LABEL[m]}</div>
      <div class="zk-taak">${p.zorgkalender[m]}</div>
    </div>`).join('');
  return `<div class="detail-sectie">
    <div class="detail-sectie-titel">📅 Zorgkalender</div>
    <div class="zorgkalender-grid">${maandHTML}</div>
  </div>`;
}

function renderCombinaties(p) {
  if (!p.combinatieplanten || p.combinatieplanten.length === 0) return '';
  const allePlants = [...PLANTS_VP, ...PLANTS_BH];
  const combHTML = p.combinatieplanten.map(lat => {
    const gevonden = allePlants.find(x => x.l === lat);
    if (!gevonden) return '';
    const destBron = PLANTS_BH.find(x => x.l === lat) ? 'bh' : 'vp';
    return `<a class="combinatie-link" href="genus.html?l=${encodeURIComponent(lat)}&bron=${destBron}">
      <span class="comb-naam">${gevonden.n}</span>
      <span class="comb-latijn">${lat}</span>
    </a>`;
  }).filter(Boolean).join('');
  if (!combHTML) return '';
  return `<div class="detail-sectie">
    <div class="detail-sectie-titel">🌱 Combinatieplanten</div>
    <div class="combinaties-grid">${combHTML}</div>
  </div>`;
}

function renderFout(latinNaam) {
  document.getElementById('detail-container').innerHTML = `
    <div class="detail-wrap">
      <a class="terug-link" href="index.html">← Terug naar catalogus</a>
      <p class="detail-fout">Plant niet gevonden: <em>${latinNaam || '(onbekend)'}</em></p>
    </div>`;
}

function init() {
  const params = new URLSearchParams(location.search);
  const latinNaam = params.get('l');
  const bron = params.get('bron') || 'vp';

  if (!latinNaam) { renderFout(''); return; }

  const dataset = bron === 'bh' ? PLANTS_BH : PLANTS_VP;
  const p = dataset.find(x => x.l === latinNaam);
  if (!p) { renderFout(latinNaam); return; }

  document.title = `${p.n} – Kwekerij Muijderman`;

  const terugHref = bron === 'bh' ? 'bomen-heesters.html' : 'index.html';
  const terugLabel = bron === 'bh' ? '← Bomen & heesters' : '← Vaste planten';

  document.getElementById('detail-container').innerHTML = `
    <div class="card-img detail-hero" id="genus-hero" data-lat="${p.wiki||p.l}" data-kleur="${p.c}" style="background:${p.c}20">
      ${genusFlower(p.c)}
      <img alt="${p.l}">
    </div>
    <div class="detail-wrap">
      <a class="terug-link" href="${terugHref}">${terugLabel}</a>
      <div class="detail-badges">
        ${hBadge(p)}
        ${catBadge(p)}
        ${lichtPill(p)}
        <span class="pill pill-bloom">🌸 ${p.b}</span>
      </div>
      <h1 class="detail-naam">${p.n}</h1>
      <div class="detail-latijn">${p.l}</div>
      <p class="detail-beschrijving">${p.d}</p>
      ${renderCultivars(p, bron)}
      ${renderZorgkalender(p)}
      ${renderCombinaties(p)}
    </div>`;

  laadHereFoto(document.getElementById('genus-hero'), p.l, p.wiki);

  document.getElementById('detail-container').addEventListener('click', e => {
    const btn = e.target.closest('.cv-fav');
    if (!btn) return;
    const id = btn.dataset.fav;
    const b = btn.dataset.bron;
    const favSet = b === 'bh' ? _favBH : _favVP;
    if (favSet.has(id)) {
      favSet.delete(id);
      btn.classList.remove('active');
      btn.textContent = '☆';
    } else {
      favSet.add(id);
      btn.classList.add('active');
      btn.textContent = '★';
    }
    saveFav(b);
  });
}

init();
