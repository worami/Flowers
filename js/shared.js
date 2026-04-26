const _KLEUR_MAP = {
  'wit':'#ffffff','crème':'#f5e4c0','creme':'#f5e4c0','crèmewit':'#f5e8d0','crèmegeel':'#f0d890',
  'geel':'#f0c020','citroengeel':'#f5e020','goudgeel':'#e0b030','goud':'#d4a820','diepgeel':'#e0a000',
  'wasgeel':'#f0e080','lichtgeel':'#f5ee80','geelgroen':'#99bb22','groen-geel':'#99bb22','geel-groen':'#99bb22',
  'oranje':'#f07820','oranjerood':'#e05020','oranjegeel':'#f0a020','zalmoranje':'#f08060','karamel':'#cc7733',
  'abrikoos':'#f5a055',
  'rood':'#cc3333','donkerrood':'#991111','felrood':'#ff2222','vuurrood':'#ff2200',
  'scharlakenrood':'#cc2200','scharlaken':'#cc2200','tomaatrood':'#cc3322','bloedrood':'#990000',
  'bordeauxrood':'#880022','wijnrood':'#881133','robijnrood':'#aa0033','baksteenrood':'#cc5533',
  'roodbruin':'#993322','roodpurper':'#882244',
  'roze':'#e87898','dieproze':'#e05070','dieprose':'#e05070','lichtroze':'#f5c0c0',
  'donkerroze':'#dd3366','zachtroze':'#f0b0c0','zalmroze':'#f5a080','koraalroze':'#e07060',
  'bloedroze':'#dd4466','scharlakenroze':'#dd3355','rozerood':'#dd4466','paarsroze':'#cc5588',
  'lavendelroze':'#c888a0','magenta':'#cc2288','helderoze':'#ff5599',
  'paars':'#8844aa','dieppaars':'#661188','donkerpaars':'#551188','lila':'#b07ed0',
  'violet':'#7744aa','diepviolet':'#5522aa','violetpaars':'#7722aa','pruimpaars':'#662288',
  'lavendel':'#b070cc','blauwpaars':'#6644cc','paarsrood':'#993366',
  'blauw':'#4466cc','hemelblauw':'#6699dd','hemelsblauw':'#6699dd','kobaltblauw':'#2244cc',
  'koningsblauw':'#2244cc','diepblauw':'#2233bb','donkerblauw':'#2233aa','lichtblauw':'#88aadd',
  'middenblauw':'#4477cc','staalblauw':'#5577aa','staalBlauw':'#5577aa','staalsblauw':'#5577aa',
  'ijsblauw':'#aaccee','grijsblauw':'#8899bb','blauwgrijs':'#8899bb','zilverblauw':'#9999cc',
  'lavendelblauw':'#8888cc','lila-blauw':'#8888cc','intens blauw':'#2244cc',
  'intens kobaltblauw':'#1133bb','intens staalBlauw':'#4466aa',
  'groen':'#44aa44','lichtgroen':'#88cc44','donkergroen':'#226622','heldergroen':'#44cc44',
  'blauwgroen':'#338888','zilvergroen':'#88aa88',
  'zilver':'#c0c0c0','zilvergrijs':'#a0a0b0','zilverpaars':'#9988bb',
  'bruin':'#8b5a2b','brons':'#cd7f32','koperbruin':'#aa6633','chocoladebruin':'#774433',
  'donkerbrons':'#8b5a2b','hertsbruin':'#8b4513',
  'beige':'#e8d8a0','goud-beige':'#d4b870',
  'zwart':'#333333','bijna zwart':'#444444','glanzend zwart':'#222222',
  'grijs':'#888888',
};

function kleurBg(kleur, fallback) {
  const k = kleur.toLowerCase().replace(/\u00ad/g, '').trim();
  if (_KLEUR_MAP[k]) return _KLEUR_MAP[k];
  const delen = k.split(/[-\s]+/);
  const gevonden = delen.map(d => _KLEUR_MAP[d]).filter(Boolean);
  if (gevonden.length >= 2) return `linear-gradient(to right, ${gevonden[0]} 50%, ${gevonden[1]} 50%)`;
  if (gevonden.length === 1) return gevonden[0];
  return fallback;
}

function laadAfbeelding(el) {
  el.dataset.gevraagd = '1';
  imgObserver.unobserve(el);
  const lat = el.dataset.lat.replace(/ /g, '_');
  fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(lat)}`)
    .then(r => r.ok ? r.json() : Promise.reject())
    .then(data => {
      const url = data.thumbnail?.source;
      if (!url) { el.classList.add('geladen'); return; }
      const img = el.querySelector('img');
      img.onload = () => { img.classList.add('geladen'); el.classList.add('geladen'); };
      img.src = url;
    })
    .catch(() => el.classList.add('geladen'));
}

function glink(l, cv) {
  return `https://www.google.com/search?q=${encodeURIComponent(l+' '+cv)}&tbm=isch`;
}
