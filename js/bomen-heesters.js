const PAGE = 8;
let filter = "all", filterLicht = "all", filterBlad = "all", query = "", page = 1, filtered = [];
let favorieten = new Set(JSON.parse(localStorage.getItem('mj_fav_bh') || '[]'));
function saveFav() { localStorage.setItem('mj_fav_bh', JSON.stringify([...favorieten])); }

function plantSVG(cat, c) {
  if (cat === 'conifeer') return conifeerSVG(c);
  if (cat === 'heester')  return heesterSVG(c);
  return boomSVG(c);
}
function boomSVG(c) {
  return `<svg viewBox="0 0 120 90" style="background:${c}15">
    <rect x="54" y="62" width="12" height="22" rx="2" fill="${c}88"/>
    <ellipse cx="60" cy="40" rx="34" ry="28" fill="${c}99"/>
    <ellipse cx="60" cy="36" rx="26" ry="20" fill="${c}cc"/>
    <ellipse cx="48" cy="32" rx="14" ry="10" fill="${c}aa" opacity="0.6"/>
    <ellipse cx="72" cy="38" rx="12" ry="9"  fill="${c}aa" opacity="0.5"/>
  </svg>`;
}
function heesterSVG(c) {
  return `<svg viewBox="0 0 120 90" style="background:${c}15">
    <ellipse cx="60" cy="72" rx="52" ry="8"  fill="${c}20"/>
    <ellipse cx="38" cy="58" rx="22" ry="16" fill="${c}88"/>
    <ellipse cx="80" cy="60" rx="20" ry="14" fill="${c}88"/>
    <ellipse cx="60" cy="50" rx="26" ry="20" fill="${c}bb"/>
    <ellipse cx="46" cy="44" rx="16" ry="12" fill="${c}99" opacity="0.7"/>
    <ellipse cx="74" cy="46" rx="15" ry="11" fill="${c}99" opacity="0.7"/>
  </svg>`;
}
function conifeerSVG(c) {
  return `<svg viewBox="0 0 120 90" style="background:${c}15">
    <rect x="55" y="72" width="10" height="14" rx="1" fill="${c}77"/>
    <polygon points="60,8 82,48 38,48"  fill="${c}99"/>
    <polygon points="60,22 86,62 34,62" fill="${c}bb"/>
    <polygon points="60,36 88,76 32,76" fill="${c}dd"/>
  </svg>`;
}

function cardHTML(p) {
  const hBg = {klein:'#fdecea', middel:'#fdf3e3', groot:'#e8f0e8'};
  const hTx = {klein:'#8b3a2a', middel:'#7a5a20', groot:'#2d4a2d'};
  const hLb = {klein:'Klein <3m', middel:'Middel 3–8m', groot:'Groot >8m'};
  const catBadge = p.cat==='heester' ? 'badge-heester' : p.cat==='conifeer' ? 'badge-conifeer' : p.cat==='rosa' ? 'badge-rosa' : 'badge-boom';
  const lichtPill = p.licht==='schaduw' ? 'pill-schaduw' : p.licht==='halfschaduw' ? 'pill-halfschaduw' : 'pill-sun';
  const lichtLabel = p.licht==='schaduw' ? '🌑 schaduw' : p.licht==='halfschaduw' ? '🌤 halfschaduw' : '☀️ zon';
  const bladPill = p.blad==='groenblijvend' ? 'pill-groenblijvend' : 'pill-bladverliezend';
  const bladLabel = p.blad==='groenblijvend' ? '🟢 groenblijvend' : '🍂 bladverliezend';
  const seizoenIcon = p.s==='winter' ? '❄️' : p.s==='herfst' ? '🍂' : p.s==='voorjaar' ? '🌱' : '☀️';
  const isFav = filter === 'favorieten';
  const cvList = isFav ? p.cv.filter(cv => favorieten.has(`${p.l}||${cv.name}`)) : p.cv;
  const cvHTML = cvList.map(cv => {
    const id = `${p.l}||${cv.name}`;
    const starred = favorieten.has(id);
    return `<div class="cultivar">
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
      ${plantSVG(p.cat, p.c)}
      <img alt="${p.l}">
      <a class="photo-link" href="${glink(p.l,'')}" target="_blank" rel="noopener">📷</a>
    </div>
    <div class="card-body">
      <div class="badges">
        <span class="badge badge-${p.h}" style="background:${hBg[p.h]};color:${hTx[p.h]}">${hLb[p.h]}</span>
        <span class="badge ${catBadge}">${p.cat}</span>
      </div>
      <div class="card-name">${p.n}</div>
      <div class="card-latin">${p.l}</div>
      <div class="pills">
        <span class="pill ${lichtPill}">${lichtLabel}</span>
        <span class="pill ${bladPill}">${bladLabel}</span>
        <span class="pill pill-bloom">${seizoenIcon} ${p.b}</span>
      </div>
      <div class="card-desc">${p.d}</div>
    </div>
    <button class="cultivar-toggle" onclick="this.nextElementSibling.classList.toggle('open');this.querySelector('.arr').textContent=this.nextElementSibling.classList.contains('open')?'▲':'▼'">
      <span>🌳 ${cvList.length} varianten</span><span class="arr">${isFav?'▲':'▼'}</span>
    </button>
    <div class="cultivars${isFav?' open':''}">${cvHTML}</div>
  </div>`;
}

function applyFilter() {
  filtered = PLANTS.filter(p => {
    const mf = filter==='favorieten'
      ? p.cv.some(cv => favorieten.has(`${p.l}||${cv.name}`))
      : filter==='all' || p.h===filter || p.s===filter || p.cat===filter;
    const ml = filterLicht==='all' || p.licht===filterLicht;
    const mb = filterBlad==='all' || p.blad===filterBlad;
    const ms = query==='' || p.n.toLowerCase().includes(query) || p.l.toLowerCase().includes(query);
    return mf && ml && mb && ms;
  });
  page = 1;
  const grid = document.getElementById('grid');
  grid.innerHTML = '';
  const loader = document.getElementById('loader');
  do { renderMore(); }
  while ((page - 1) * PAGE < filtered.length && loader.getBoundingClientRect().top < window.innerHeight);
  if (filtered.length === 0) {
    grid.innerHTML = filter === 'favorieten'
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
  document.getElementById('count').textContent = shown + '/' + filtered.length;
  document.getElementById('hdr-count').textContent = PLANTS.length + ' soorten met cultivarvarianten · 📷 = Google foto\'s';
  loader.textContent = shown < filtered.length ? 'Meer laden…' : '— alle ' + filtered.length + ' soorten getoond —';
  page++;
}

const imgObserver = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting && !e.target.dataset.gevraagd) laadAfbeelding(e.target); });
}, { rootMargin: '300px' });

const _loaderEl = document.getElementById('loader');
new IntersectionObserver(entries => {
  if (entries[0].isIntersecting) renderMore();
}, { rootMargin: '200px' }).observe(_loaderEl);
window.addEventListener('scroll', () => {
  if (_loaderEl.getBoundingClientRect().top < window.innerHeight + 300) renderMore();
}, { passive: true });

document.getElementById('filters').addEventListener('click', e => {
  const btn = e.target.closest('button');
  if (!btn || !btn.dataset.filter) return;
  document.querySelectorAll('#filters button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filter = btn.dataset.filter;
  applyFilter();
});

document.getElementById('filters-licht').addEventListener('click', e => {
  const btn = e.target.closest('button');
  if (!btn || !btn.dataset.licht) return;
  document.querySelectorAll('#filters-licht button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterLicht = btn.dataset.licht;
  applyFilter();
});

document.getElementById('filters-blad').addEventListener('click', e => {
  const btn = e.target.closest('button');
  if (!btn || !btn.dataset.blad) return;
  document.querySelectorAll('#filters-blad button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterBlad = btn.dataset.blad;
  applyFilter();
});

document.getElementById('grid').addEventListener('click', e => {
  const btn = e.target.closest('.cv-fav');
  if (!btn) return;
  e.stopPropagation();
  const id = btn.dataset.fav;
  if (favorieten.has(id)) {
    favorieten.delete(id);
    btn.classList.remove('active');
    btn.textContent = '☆';
    if (filter === 'favorieten') applyFilter();
  } else {
    favorieten.add(id);
    btn.classList.add('active');
    btn.textContent = '★';
  }
  saveFav();
});

let debounce;
document.getElementById('search').addEventListener('input', e => {
  clearTimeout(debounce);
  debounce = setTimeout(() => { query = e.target.value.toLowerCase(); applyFilter(); }, 200);
});

applyFilter();
