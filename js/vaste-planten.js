const PAGE = 8;
let filterHoogte = 'alles', filterType = null, filterSeizoen = null, filterLicht = 'alle licht', filterFav = false;
let query = "", sorteer = "az", page = 1, filtered = [];
let favorieten = new Set(JSON.parse(localStorage.getItem('mj_fav') || '[]'));
function saveFav() { localStorage.setItem('mj_fav', JSON.stringify([...favorieten])); }

function flower(c) {
  const pts = [0,60,120,180,240,300].map(a => {
    const x = 60 + 13*Math.cos(a*Math.PI/180), y = 22 + 13*Math.sin(a*Math.PI/180);
    return `<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="7" ry="5" fill="${c}" opacity="0.8" transform="rotate(${a},${x.toFixed(1)},${y.toFixed(1)})"/>`;
  }).join('');
  return `<svg viewBox="0 0 120 90" style="background:${c}15">
    <ellipse cx="60" cy="80" rx="52" ry="8" fill="${c}20"/>
    <line x1="60" y1="80" x2="60" y2="22" stroke="${c}77" stroke-width="2.5"/>
    <ellipse cx="44" cy="55" rx="10" ry="4" fill="#4a7c5955" transform="rotate(-25,44,55)"/>
    <ellipse cx="76" cy="57" rx="10" ry="4" fill="#4a7c5955" transform="rotate(25,76,57)"/>
    ${pts}
    <circle cx="60" cy="22" r="6" fill="${c}"/>
    <circle cx="60" cy="22" r="2.5" fill="white" opacity="0.4"/>
  </svg>`;
}

function cardHTML(p) {
  const hBg = {hoog:'#e8f0e8',middel:'#fdf3e3',laag:'#fdecea'};
  const hTx = {hoog:'#2d4a2d',middel:'#7a5a20',laag:'#8b3a2a'};
  const hLb = {hoog:'Hoog >60cm',middel:'Middel 30–60cm',laag:'Laag <30cm'};
  const cvList = filterFav ? p.cv.filter(cv => favorieten.has(`${p.l}||${cv.name}`)) : p.cv;
  const cvHTML = cvList.map(cv => {
    const id = `${p.l}||${cv.name}`;
    const starred = favorieten.has(id);
    return `
    <div class="cultivar">
      <div class="cv-header">
        <div><span class="cv-name">${cv.name}</span><span class="cv-height">· ${cv.hoogte}</span></div>
        <div style="display:flex;gap:0.3rem;align-items:center">
          <button class="cv-fav${starred?' active':''}" data-fav="${id}" title="Favoriet">${starred?'★':'☆'}</button>
          <a class="cv-photo" href="${glink(p.l,cv.name)}" target="_blank" rel="noopener">📷 foto</a>
        </div>
      </div>
      <div class="cv-color"><span class="cv-dot" style="background:${kleurBg(cv.kleur, p.c)}"></span><span class="cv-kleur">${cv.kleur}</span></div>
      <div class="cv-tip">${cv.tip}</div>
    </div>`;
  }).join('');
  return `<div class="card">
    <div class="card-img" data-lat="${p.l}" data-kleur="${p.c}" style="background:${p.c}20">
      ${flower(p.c)}
      <img alt="${p.l}">
      <a class="photo-link" href="${glink(p.l,'')}" target="_blank" rel="noopener">📷</a>
    </div>
    <div class="card-body">
      <div class="badges">
        <span class="badge badge-${p.h}" style="background:${hBg[p.h]};color:${hTx[p.h]}">${hLb[p.h]}</span>
        <span class="badge ${p.cat==='bodembedekker'?'badge-bodem':p.cat==='siergras'?'badge-gras':p.cat==='klimplant'?'badge-klimplant':'badge-vaste'}">${p.cat}</span>
      </div>
      <div class="card-name">${p.n}</div>
      <div class="card-latin">${p.l}</div>
      <div class="pills">
        <span class="pill ${p.licht==='schaduw'?'pill-schaduw':p.licht==='halfschaduw'?'pill-halfschaduw':'pill-sun'}">${p.licht==='schaduw'?'🌑 schaduw':p.licht==='halfschaduw'?'🌤 halfschaduw':'☀️ zon'}</span>
        <span class="pill pill-bloom">🌸 ${p.b}</span>
      </div>
      <div class="card-desc">${p.d}</div>
    </div>
    <button class="cultivar-toggle" onclick="this.nextElementSibling.classList.toggle('open');this.querySelector('.arr').textContent=this.nextElementSibling.classList.contains('open')?'▲':'▼'">
      <span>🌿 ${cvList.length} varianten</span><span class="arr">${filterFav?'▲':'▼'}</span>
    </button>
    <div class="cultivars${filterFav?' open':''}">${cvHTML}</div>
  </div>`;
}

const _hOrd = {laag:0, middel:1, hoog:2};
const _sOrd = {voorjaar:0, zomer:1, herfst:2};

function updateTeller() {
  const isActief = filterHoogte !== 'alles' || filterType !== null || filterSeizoen !== null || filterLicht !== 'alle licht' || filterFav;
  const telGetal = document.getElementById('count');
  const telTotaal = document.getElementById('teller-totaal');
  const wisBtn = document.getElementById('filter-wis');
  telGetal.textContent = filtered.length;
  if (telTotaal) telTotaal.textContent = '/' + PLANTS.length;
  telGetal.classList.toggle('actief', isActief || query !== '');
  wisBtn.classList.toggle('zichtbaar', isActief);
}

function applyFilter() {
  filtered = PLANTS.filter(p => {
    if (filterFav && !p.cv.some(cv => favorieten.has(`${p.l}||${cv.name}`))) return false;
    if (filterHoogte !== 'alles' && p.h !== filterHoogte) return false;
    if (filterType !== null && p.cat !== filterType) return false;
    if (filterSeizoen !== null && p.s !== filterSeizoen) return false;
    if (filterLicht !== 'alle licht' && p.licht !== filterLicht) return false;
    if (query !== '' && !p.n.toLowerCase().includes(query) && !p.l.toLowerCase().includes(query)) return false;
    return true;
  });
  if (sorteer === 'az') filtered.sort((a,b) => a.n.localeCompare(b.n, 'nl'));
  else if (sorteer === 'za') filtered.sort((a,b) => b.n.localeCompare(a.n, 'nl'));
  else if (sorteer === 'bloei') filtered.sort((a,b) => (_sOrd[a.s]??2) - (_sOrd[b.s]??2));
  page = 1;
  const grid = document.getElementById('grid');
  grid.innerHTML = '';
  updateTeller();
  const loader = document.getElementById('loader');
  do { renderMore(); }
  while ((page - 1) * PAGE < filtered.length && loader.getBoundingClientRect().top < window.innerHeight);
  if (filtered.length === 0) {
    grid.innerHTML = filterFav
      ? '<p class="empty-msg">Nog geen favorieten. Open een plant, klik op ☆ bij een cultivar om hem op te slaan.</p>'
      : '<p class="empty-msg">Geen resultaten gevonden.</p>';
    loader.textContent = '';
  }
}

function renderMore() {
  if ((page - 1) * PAGE >= filtered.length) return;
  const grid = document.getElementById('grid');
  const loader = document.getElementById('loader');
  const slice = filtered.slice((page-1)*PAGE, page*PAGE);
  grid.insertAdjacentHTML('beforeend', slice.map(cardHTML).join(''));
  const allCards = grid.querySelectorAll('.card-img[data-lat]');
  Array.from(allCards).slice(-slice.length).forEach(el => imgObserver.observe(el));
  const shown = Math.min(page*PAGE, filtered.length);
  document.getElementById('hdr-count').textContent = PLANTS.length + ' planten met cultivarvarianten · 📷 = Google foto\'s';
  loader.textContent = shown < filtered.length ? 'Meer laden…' : '— alle ' + filtered.length + ' planten getoond —';
  page++;
}

const imgObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting && !e.target.dataset.gevraagd) laadAfbeelding(e.target);
  });
}, { rootMargin: '300px' });

const _loaderEl = document.getElementById('loader');
new IntersectionObserver(entries => {
  if (entries[0].isIntersecting) renderMore();
}, { rootMargin: '200px' }).observe(_loaderEl);
window.addEventListener('scroll', () => {
  if (_loaderEl.getBoundingClientRect().top < window.innerHeight + 300) renderMore();
}, { passive: true });

// ── Chip-filters ──
document.getElementById('chips-scroll').addEventListener('click', e => {
  const btn = e.target.closest('.chip[data-groep]');
  if (!btn) return;
  const groep = btn.dataset.groep;
  const val = btn.dataset.val;

  if (groep === 'hoogte') {
    filterHoogte = filterHoogte === val ? 'alles' : val;
    document.querySelectorAll('#chips-scroll [data-groep="hoogte"]').forEach(b =>
      b.classList.toggle('chip-actief', b.dataset.val === filterHoogte));
  } else if (groep === 'type') {
    filterType = filterType === val ? null : val;
    document.querySelectorAll('#chips-scroll [data-groep="type"]').forEach(b =>
      b.classList.toggle('chip-actief', b.dataset.val === filterType));
  } else if (groep === 'seizoen') {
    filterSeizoen = filterSeizoen === val ? null : val;
    document.querySelectorAll('#chips-scroll [data-groep="seizoen"]').forEach(b =>
      b.classList.toggle('chip-actief', b.dataset.val === filterSeizoen));
  } else if (groep === 'licht') {
    filterLicht = filterLicht === val ? 'alle licht' : val;
    document.querySelectorAll('#chips-scroll [data-groep="licht"]').forEach(b =>
      b.classList.toggle('chip-actief', b.dataset.val === filterLicht));
  } else if (groep === 'fav') {
    filterFav = !filterFav;
    btn.classList.toggle('chip-actief', filterFav);
  }

  applyFilter();
});

// ── Wis-knop (teller) ──
document.getElementById('filter-wis').addEventListener('click', () => {
  filterHoogte = 'alles'; filterType = null; filterSeizoen = null; filterLicht = 'alle licht'; filterFav = false;
  document.querySelectorAll('#chips-scroll [data-groep="hoogte"]').forEach(b =>
    b.classList.toggle('chip-actief', b.dataset.val === 'alles'));
  document.querySelectorAll('#chips-scroll [data-groep="type"]').forEach(b => b.classList.remove('chip-actief'));
  document.querySelectorAll('#chips-scroll [data-groep="seizoen"]').forEach(b => b.classList.remove('chip-actief'));
  document.querySelectorAll('#chips-scroll [data-groep="licht"]').forEach(b =>
    b.classList.toggle('chip-actief', b.dataset.val === 'alle licht'));
  document.querySelectorAll('#chips-scroll [data-groep="fav"]').forEach(b => b.classList.remove('chip-actief'));
  applyFilter();
});

// ── Favorieten toggle in grid ──
document.getElementById('grid').addEventListener('click', e => {
  const btn = e.target.closest('.cv-fav');
  if (!btn) return;
  e.stopPropagation();
  const id = btn.dataset.fav;
  if (favorieten.has(id)) {
    favorieten.delete(id);
    btn.classList.remove('active');
    btn.textContent = '☆';
    if (filterFav) { applyFilter(); }
  } else {
    favorieten.add(id);
    btn.classList.add('active');
    btn.textContent = '★';
  }
  saveFav();
});

// ── Sortering ──
document.getElementById('sorteer').addEventListener('change', e => {
  sorteer = e.target.value;
  applyFilter();
});

// ── Zoekbalk ──
const _zoekbalk = document.getElementById('zoekbalk');
const _zoekWis = document.getElementById('search-clear');
const _zoekInput = document.getElementById('search');

_zoekInput.addEventListener('focus', () => _zoekbalk.classList.add('focus'));
_zoekInput.addEventListener('blur', () => _zoekbalk.classList.remove('focus'));

let debounce;
_zoekInput.addEventListener('input', e => {
  clearTimeout(debounce);
  const val = e.target.value;
  _zoekWis.classList.toggle('zichtbaar', val !== '');
  debounce = setTimeout(() => { query = val.toLowerCase(); applyFilter(); }, 200);
});

_zoekWis.addEventListener('click', () => {
  _zoekInput.value = '';
  _zoekWis.classList.remove('zichtbaar');
  query = '';
  applyFilter();
});

applyFilter();
