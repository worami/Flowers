const FAV_KEY_VP    = 'mj_fav';
const FAV_KEY_BH    = 'mj_fav_bh';
const NOTITIES_KEY  = 'mj_notities';

const hBg = { hoog:'#e8f0e8', middel:'#fdf3e3', laag:'#fdecea', klein:'#fdecea', groot:'#e8f0e8' };
const hTx = { hoog:'#2d4a2d', middel:'#7a5a20', laag:'#8b3a2a', klein:'#8b3a2a', groot:'#2d4a2d' };

function catBadgeKlasse(cat) {
  const map = {
    'bodembedekker': 'badge-bodem',
    'siergras':      'badge-gras',
    'klimplant':     'badge-klimplant',
    'boom':          'badge-boom',
    'heester':       'badge-heester',
    'conifeer':      'badge-conifeer',
    'rosa':          'badge-rosa',
  };
  return map[cat] || 'badge-vaste';
}

function lichtPillHTML(licht) {
  if (licht === 'schaduw')     return '<span class="pill pill-schaduw">🌑 schaduw</span>';
  if (licht === 'halfschaduw') return '<span class="pill pill-halfschaduw">🌤 halfschaduw</span>';
  return '<span class="pill pill-sun">☀️ zon</span>';
}

let notities = JSON.parse(localStorage.getItem(NOTITIES_KEY) || '{}');
let notitieTimer;

function slaNotitiesOp() {
  localStorage.setItem(NOTITIES_KEY, JSON.stringify(notities));
}

function zoekPlant(id, bron) {
  const sep = id.indexOf('||');
  if (sep === -1) return null;
  const latijn   = id.slice(0, sep);
  const cvNaam   = id.slice(sep + 2);
  const dataset  = bron === 'vp' ? PLANTS_VP : PLANTS_BH;
  const plant    = dataset.find(p => p.l === latijn);
  if (!plant) return null;
  const cv = plant.cv.find(c => c.name === cvNaam) || null;
  return { plant, cv };
}

function kaartHTML(id, bron) {
  const gevonden = zoekPlant(id, bron);
  if (!gevonden) return '';
  const { plant: p, cv } = gevonden;
  const noot     = (notities[id] || {}).notitie || '';
  const aantal   = (notities[id] || {}).aantal   || '';
  const bronLabel = bron === 'vp' ? 'Vaste plant' : 'Boom/Heester';
  const bronKlasse = bron === 'vp' ? 'fav-bron-vp' : 'fav-bron-bh';
  const cvBlok = cv ? `
  <div class="cv-color fav-cv-kleur">
    <span class="cv-dot" style="background:${kleurBg(cv.kleur, p.c)}"></span>
    <span class="cv-kleur">${cv.kleur}</span>
  </div>
  <div class="cv-tip">${cv.tip}</div>` : '';

  return `<div class="fav-card card" data-id="${id}" data-bron="${bron}">
  <div class="fav-card-top">
    <div>
      <div class="card-name">${p.n}</div>
      <div class="card-latin">${p.l}</div>
      ${cv ? `<div class="cv-name fav-cv-naam">${cv.name}</div>` : ''}
    </div>
    <div class="fav-top-acties">
      <a class="cv-photo" href="${glink(p.l, cv ? cv.name : '')}" target="_blank" rel="noopener">📷 foto</a>
      <button class="fav-verwijder" data-id="${id}" data-bron="${bron}" title="Verwijder uit favorieten">☆</button>
    </div>
  </div>
  <div class="badges fav-badges">
    <span class="badge" style="background:${hBg[p.h]||'#eee'};color:${hTx[p.h]||'#333'}">${p.h}</span>
    <span class="badge ${catBadgeKlasse(p.cat)}">${p.cat}</span>
    <span class="pill fav-bron-pill ${bronKlasse}">${bronLabel}</span>
  </div>
  <div class="pills fav-pills">
    ${lichtPillHTML(p.licht)}
    <span class="pill pill-bloom">🌸 ${p.b}</span>
  </div>
  ${cvBlok}
  <div class="fav-acties">
    <label class="fav-label">
      <span class="fav-label-tekst">Notitie</span>
      <textarea class="fav-notitie" data-id="${id}" placeholder="Notitie voor je bezoek…" rows="2">${noot}</textarea>
    </label>
    <label class="fav-label fav-label-aantal">
      <span class="fav-label-tekst">Aantal</span>
      <input type="number" class="fav-aantal" data-id="${id}" min="1" placeholder="1" value="${aantal}">
    </label>
  </div>
</div>`;
}

function render() {
  const favVP = JSON.parse(localStorage.getItem(FAV_KEY_VP) || '[]');
  const favBH = JSON.parse(localStorage.getItem(FAV_KEY_BH) || '[]');
  const alle  = [
    ...favVP.map(id => ({ id, bron: 'vp' })),
    ...favBH.map(id => ({ id, bron: 'bh' })),
  ];

  const teller = document.getElementById('fav-teller');
  if (teller) teller.textContent = alle.length + ' favoriet' + (alle.length !== 1 ? 'en' : '');

  const grid = document.getElementById('fav-grid');
  const leeg = document.getElementById('fav-leeg');

  if (alle.length === 0) {
    grid.innerHTML = '';
    leeg.hidden = false;
    return;
  }
  leeg.hidden = true;
  grid.innerHTML = alle.map(({ id, bron }) => kaartHTML(id, bron)).join('');
}

document.getElementById('fav-grid').addEventListener('input', e => {
  const el = e.target;
  const id = el.dataset.id;
  if (!id) return;
  if (!notities[id]) notities[id] = {};
  if (el.classList.contains('fav-notitie')) notities[id].notitie = el.value;
  if (el.classList.contains('fav-aantal'))  notities[id].aantal  = el.value ? Number(el.value) : '';
  clearTimeout(notitieTimer);
  notitieTimer = setTimeout(slaNotitiesOp, 400);
});

document.getElementById('fav-grid').addEventListener('click', e => {
  const btn = e.target.closest('.fav-verwijder');
  if (!btn) return;
  const id   = btn.dataset.id;
  const bron = btn.dataset.bron;
  const key  = bron === 'vp' ? FAV_KEY_VP : FAV_KEY_BH;
  const favs = JSON.parse(localStorage.getItem(key) || '[]');
  localStorage.setItem(key, JSON.stringify(favs.filter(f => f !== id)));
  render();
});

document.getElementById('btn-print').addEventListener('click', () => window.print());

render();
