# CLAUDE.md — Flowers / Kwekerij Muijderman Plant Catalogue

## Project Overview

A multi-file static web application for **Kwekerij Muijderman** (Muijderman Nursery) in Veldhoven, Netherlands.

### Doel / Purpose

Het doel van deze app is het **doorzoekbaar en overzichtelijk maken van de plantenassortiment van Kwekerij Muijderman**. De kwekerij verkoopt een groot en gevarieerd assortiment vaste planten, bodembedekkers, siergrassen en klimplanten. De officiële assortimentslijst is te vinden op:

> https://www.kwekerijmuijderman.nl/assortiment/overzicht

**Scope:** de categorie *vaste planten* (inclusief bodembedekkers, siergrassen en klimplanten) uit het Muijderman-assortiment valt binnen de scope van `index.html`. Andere categorieën die de kwekerij voert — zoals bomen, heesters of seizoensplanten — worden **buiten beschouwing gelaten** en mogen niet worden toegevoegd aan de `PLANTS`-array van dit bestand.

De app lost drie problemen op die de ruwe assortimentslijst niet oplost:

1. **Groepering per genus** — planten worden gegroepeerd onder hun Latijnse geslachtsnaam (bijv. alle *Echinacea*-soorten bij elkaar), met per soort de beschikbare cultivars.
2. **Filters** — bezoekers kunnen snel filteren op hoogte, bloeiperiode, categorie, lichtbehoefte en vrije tekst, zodat ze direct de planten zien die bij hun situatie passen.
3. **Favorieten** — bezoekers kunnen individuele cultivars markeren als favoriet (opgeslagen in `localStorage`) zodat ze een persoonlijke verlanglijst kunnen samenstellen voor hun bezoek aan de kwekerij.

The app is a filterable catalogue of *vaste planten* (perennial plants) with cultivar listings, SVG flower previews, favourite tracking, and Google Images photo links.

- **Language:** Dutch throughout (UI text, variable names, commit messages)
- **Stack:** Pure vanilla HTML + CSS + JavaScript — no framework, no build tool, no dependencies
- **Entry point:** `index.html` (vaste planten) · `bomen-heesters.html` (bomen, heesters, conifeers)

### Tweede pagina: `bomen-heesters.html`

Naast `index.html` bestaat er een tweede zelfstandige pagina voor **bomen, heesters en conifeers**. Deze pagina heeft dezelfde visuele stijl maar een aangepast dataschema en andere filters.

**Aanvullende / gewijzigde schema-velden:**

| Veld | Waarden |
|------|---------|
| `h` | `"klein"` (<3m) \| `"middel"` (3–8m) \| `"groot"` (>8m) |
| `cat` | `"boom"` \| `"heester"` \| `"conifeer"` |
| `blad` | `"bladverliezend"` \| `"groenblijvend"` *(nieuw veld)* |
| `s` | `"voorjaar"` \| `"zomer"` \| `"herfst"` \| `"winter"` *(winter toegevoegd)* |
| `b` | Sierperiode (niet alleen bloei — ook herfstkleur, bessen, schors) |

**Extra filter:** `#filters-blad` (bladverliezend / groenblijvend), state variabele `filterBlad`.

**LocalStorage sleutel:** `'mj_fav_bh'` (apart van `'mj_fav'` in index.html).

**SVG illustraties:** `plantSVG(cat, c)` — dispatcher naar `boomSVG`, `heesterSVG`, `conifeerSVG` in plaats van `flower(c)`.

**Scope van `bomen-heesters.html`:** uitsluitend `"boom"`, `"heester"` en `"conifeer"`. Voeg geen vaste planten, bodembedekkers of siergrassen toe aan de `PLANTS`-array van dit bestand.

---

## Architecture

The project uses a multi-file structure. Both HTML pages are lean skeletons that load shared and page-specific assets.

```
/
├── index.html               (~54 regels — HTML-skelet vaste planten)
├── bomen-heesters.html      (~61 regels — HTML-skelet bomen/heesters)
├── css/
│   ├── shared.css           (gedeelde stijlen, ~85% identiek in beide pagina's)
│   ├── vaste-planten.css    (badge-klassen: hoog/middel/laag, vaste/bodem/gras)
│   └── bomen-heesters.css   (badge/pill-klassen: klein/middel/groot, boom/heester/conifeer, bladverliezend/groenblijvend)
├── js/
│   ├── shared.js            (_KLEUR_MAP, kleurBg(), glink(), laadAfbeelding())
│   ├── vaste-planten.js     (flower(), cardHTML(), applyFilter(), renderMore(), events, init)
│   └── bomen-heesters.js   (plantSVG + SVG-helpers, cardHTML(), applyFilter() + filterBlad, events, init)
└── data/
    ├── vaste-planten.js     (const PLANTS = [...] — ~271 entries)
    └── bomen-heesters.js   (const PLANTS = [...] — ~179 entries)
```

**Laadvolgorde per pagina** (via `<script src="">` tags, géén ES modules):
1. `js/shared.js` — gedeelde utilities
2. `data/vaste-planten.js` of `data/bomen-heesters.js` — plantdata
3. `js/vaste-planten.js` of `js/bomen-heesters.js` — paginalogica

---

## Plant Data Schema

Each entry in the `PLANTS` array (lines 116–212) follows this shape:

```js
{
  n: string,      // Dutch common name, e.g. "Rode zonnehoed"
  l: string,      // Latin / scientific name, e.g. "Echinacea purpurea"
  h: string,      // Height category: "hoog" (>60 cm) | "middel" (30–60 cm) | "laag" (<30 cm)
  s: string,      // Bloom season: "voorjaar" | "zomer" | "herfst"
  b: string,      // Bloom months text, e.g. "jul–sep"
  c: string,      // Representative hex colour, e.g. "#c0607a"
  licht: string,  // Light need: "zon" | "halfschaduw" | "schaduw"
  cat: string,    // Category: "vaste plant" | "bodembedekker" | "siergras"
  d: string,      // Dutch prose description (care tips, characteristics)
  cv: [           // Array of cultivars / varieties
    {
      name: string,   // Cultivar name (or species epithet)
      kleur: string,  // Flower colour in Dutch
      hoogte: string, // Height as string, e.g. "80cm"
      tip: string     // Short Dutch cultivation/selection tip
    },
    …
  ]
}
```

**Adding a new plant:** copy any existing entry, adjust all fields, and insert it into the `PLANTS` array in `data/vaste-planten.js` (vaste planten) or `data/bomen-heesters.js` (bomen/heesters).

---

## Key Functions

| Function | Bestand | Purpose |
|----------|---------|---------|
| `flower(c)` | `js/vaste-planten.js` | Generates an inline SVG flower illustration using the plant's hex colour `c` |
| `plantSVG(cat, c)` | `js/bomen-heesters.js` | Dispatcher naar `boomSVG`, `heesterSVG` of `conifeerSVG` |
| `glink(l, cv)` | `js/shared.js` | Returns a Google Images URL for Latin name + cultivar |
| `kleurBg(kleur, fallback)` | `js/shared.js` | Vertaalt een kleurnaam naar een hex-kleur of gradient via `_KLEUR_MAP` |
| `laadAfbeelding(el)` | `js/shared.js` | Laadt een Wikipedia-thumbnail lazy via `imgObserver` |
| `cardHTML(p)` | `js/vaste-planten.js` of `js/bomen-heesters.js` | Returns the full HTML string for a plant card, including cultivar list |
| `applyFilter()` | `js/vaste-planten.js` of `js/bomen-heesters.js` | Filters `PLANTS` into `filtered[]` based on current filter state; resets pagination and re-renders |
| `renderMore()` | `js/vaste-planten.js` of `js/bomen-heesters.js` | Appends the next page slice (`PAGE = 8`) of `filtered[]` to `#grid` using `insertAdjacentHTML` |
| `saveFav()` | `js/vaste-planten.js` of `js/bomen-heesters.js` | Persists the `favorieten` Set to `localStorage` as JSON |

---

## State Variables

```js
const PAGE = 8;                        // items per infinite-scroll page
let filter = "all";                    // active primary filter value
let filterLicht = "all";              // active light filter value
let query = "";                        // lowercased search string
let page = 1;                          // current pagination page
let filtered = [];                     // result of applyFilter()
let favorieten = new Set(…);           // Set of favourite IDs from localStorage
```

Favourite IDs use the format `"Latin Name||Cultivar Name"`, e.g. `"Echinacea purpurea||'Magnus'"`.

---

## Filtering Logic

Filters are **independent and ANDed** (`applyFilter` in `js/vaste-planten.js` / `js/bomen-heesters.js`):

1. **Primary filter** (`#filters` buttons, `data-filter` attribute):
   - `"all"` — no restriction
   - `"hoog"` / `"middel"` / `"laag"` — matches `p.h`
   - `"voorjaar"` / `"zomer"` / `"herfst"` — matches `p.s`
   - `"bodembedekker"` / `"siergras"` — matches `p.cat`
   - `"favorieten"` — plant must have at least one starred cultivar

2. **Light filter** (`#filters-licht` buttons, `data-licht`): matches `p.licht`

3. **Text search** (`#search`): substring match on `p.n` or `p.l` (case-insensitive, 200 ms debounce)

---

## Infinite Scroll

- `#loader` div at the bottom is observed by an `IntersectionObserver`.
- When it enters the viewport, `renderMore()` appends the next 8 cards.
- `applyFilter()` always resets `page = 1` and clears `#grid` before the first batch.

---

## Persistence

- `localStorage` key: `'mj_fav'` (vaste planten) / `'mj_fav_bh'` (bomen & heesters)
- Value: JSON array of favourite ID strings, e.g. `["Echinacea purpurea||'Magnus'", …]`
- Read on page load, written by `saveFav()` after every toggle.

---

## CSS Conventions

- Gedeelde stijlen staan in `css/shared.css`. Pagina-specifieke badge/pill-klassen staan in `css/vaste-planten.css` resp. `css/bomen-heesters.css`.
- **Colours** are hardcoded hex values — no CSS custom properties:
  - Background: `#f5f0e8`
  - Primary dark green: `#2d4a2d`
  - Accent gold: `#c8a84b`
  - Card background: `white`
- **Height badge colours** are set inline via JS maps (`hBg`, `hTx` in `cardHTML`).
- **Naming:** kebab-case classes (`.card-body`, `.cv-name`, `.badge-hoog`).
- **Layout:** CSS Grid for the card grid (`auto-fill, minmax(240px, 1fr)`); flexbox for toolbar rows.
- **Toolbar:** `position: sticky; top: 0; z-index: 10`.

---

## JavaScript Conventions

- **Language:** Dutch variable names, Dutch-language strings, Dutch commit messages.
- **Style:** ES6+ — `const`/`let`, arrow functions, template literals, `Set`, `IntersectionObserver`.
- **No transpilation:** code runs directly in the browser; do not introduce syntax that requires a build step.
- **DOM updates:** use `insertAdjacentHTML('beforeend', …)` for appending; assign `.innerHTML` only on full re-renders.
- **Event handling:** event delegation on `#filters`, `#filters-licht`, and `#grid` — do not add per-card listeners.
- **No external libraries:** keep the file free of CDN script tags or import statements.

---

## Development Workflow

There is no build system, no test runner, and no package manager.

**To develop:**
1. Open `index.html` in a browser (file:// werkt — de `<script src="">` tags zijn géén ES modules).
2. Edit en reload. Plantdata zit in `data/`, logica in `js/`, stijlen in `css/`.

**To test:**
- Manual testing in the browser is the only test method.
- Verify all filter combinations, search, favourites toggle, and infinite scroll.
- Check mobile layout (resize browser or use DevTools).

**To deploy:**
- Kopieer de volledige repo-inhoud naar een static host (GitHub Pages, Netlify, een gewone webserver). Alle mappen (`css/`, `js/`, `data/`) moeten mee. No build step needed.

---

## Git Conventions

- Commit messages are written in **Dutch**.
- Example messages from history:
  - `Voeg siergrassen-categorie en ontbrekende soorten toe`
  - `Voeg favoriete cultivars toe met localStorage-opslag`
  - `Uitbreiding catalogus: 82 planten, lichtfilter, nieuwe UI`
- Feature branches follow the pattern `claude/<description>-<id>`.

---

## What Not To Do

- **Do not add a build system** (webpack, Vite, Parcel, etc.) unless explicitly requested.
- **Do not add external dependencies** (React, Vue, jQuery, Tailwind, etc.).
- **Do not add TypeScript** — the project is intentionally plain JavaScript.
- **Do not use ES modules** (`type="module"`) — reguliere `<script src="">` tags zijn bewust gekozen zodat `file://` blijft werken.
- **Do not change the Dutch language** of the UI or data without being asked.
- **Do not add automated tests** speculatively — there is no test infrastructure.
- **Do not introduce CSS custom properties** unless refactoring all hardcoded colours at once.

---

## Extending the Catalogue

To add a new plant category beyond `"vaste plant"`, `"bodembedekker"`, `"siergras"`:

1. Add the `cat` value to the new plant entry in `data/vaste-planten.js`.
2. Add a filter button in `#filters` in `index.html` with the matching `data-filter` attribute.
3. Add a CSS badge class `.badge-<suffix>` in `css/vaste-planten.css`.
4. Update the badge selector ternary in `cardHTML` in `js/vaste-planten.js`.

To add a new light requirement beyond `"zon"`, `"halfschaduw"`, `"schaduw"`:

1. Add a button in `#filters-licht` in the HTML with `data-licht="<value>"`.
2. Add a CSS pill class in `css/shared.css` and update the pill ternary in `cardHTML`.

---

## Catalogus uitbreiden — voortgang

De PLANTS-array in `data/vaste-planten.js` streeft naar het **volledige Muijderman-assortiment** — alle cultivars die zij voeren, geen curatieve selectie. Voor klimplanten (`cat:"klimplant"`) geldt dit eveneens.

**Werkwijze:** voeg per sessie 1 batch toe (5–7 genera) aan `data/vaste-planten.js`, commit daarna, en markeer de batch hieronder als ✅.

> **Volgende sessie:** start bij de eerste batch die nog ⬜ heeft.

### Vaste planten — batchplan

| # | Genera | Status |
|---|---|---|
| 1 | Aster · Bergenia · Crocosmia · Geum · Leucanthemum | ✅ |
| 2 | Delphinium · Heuchera · Iris (sibirica) · Liatris · Lupinus | ✅ |
| 3 | Agapanthus · Centaurea · Dianthus · Papaver orientale · Pulsatilla | ✅ |
| 4 | Euphorbia · Helianthus · Heliopsis · Primula · Veronica | ✅ |
| 5 | Platycodon · Polemonium · Saxifraga · Tricyrtis · Verbascum | ✅ |
| 6 | Sedum (kleine soorten) · Sempervivum · Gypsophila · Lychnis · Liriope | ✅ |
| 7 | Amsonia · Astilboides · Caltha · Crambe · Darmera | ✅ |
| 8 | Anthemis · Armeria · Acanthus · Catananche · Cephalaria | ✅ |
| 9 | Gentiana · Gillenia · Hepatica · Inula · Kirengeshoma | ✅ |
| 10 | Sidalcea · Silphium · Stokesia · Symphytum · Tellima | ✅ |
| 11 | Anemonella · Arisaema · Trillium · Uvularia · Jeffersonia | ✅ |
| 12 | Overige (Cosmos · Dierama · Disporum · Dodecatheon · Isotoma) | ✅ |
| 13 | Origanum · Dicentra · Corydalis · Physostegia · Doronicum | ✅ |
| 14 | Artemisia · Asclepias · Dictamnus · Macleaya · Galega | ✅ |
| 15 | Anaphalis · Anthericum · Kalimeris · Sisyrinchium · Telekia | ✅ |
| 16 | Delosperma · Erysimum · Linum · Malva · Physalis | ✅ |
| 17 | Cardamine · Lunaria · Mertensia · Tanacetum · Thermopsis | ✅ |
| 18 | Incarvillea · Morina · Podophyllum · Trachystemon · Trifolium | ✅ |
| 19 | Buphthalmum · Cenolophium · Hylomecon · Ophiopogon · Selinum | ✅ |
| 20 | Limonium · Patrinia · Scutellaria · Seseli · Succisa | ✅ |
| 21 | Chrysanthemum · Leontopodium · Lewisia · Linaria · Meconopsis | ✅ |
| 22 | Mitella · Mukdenia · Phuopsis · Phyteuma · Ranunculus | ✅ |
| 23 | Saruma · Serratula · Smilacina · Stylophorum · Tulbaghia | ✅ |
| 24 | Berkheya · Deinanthe · Melittis · Parthenium · Peltoboykinia | ✅ |
| 25 | Alstroemeria · Althaea · Anemonopsis · Asphodeline · Beesia · Belamcanda | ✅ |
| 26 | Betonica · Boltonia · Buglossoides · Chelonopsis · Chrysogonum · Chrysosplenium | ✅ |
| 27 | Dendranthema · Dystaenia · Erodium · Gaura · Houstonia · Peucedanum | ✅ |
| 28 | Epimedium · Filipendula · Alcea | ✅ |
| 29 | Helianthemum · Eremurus · Epilobium · Hesperis · Angelica | ✅ |
| 30 | Strobilanthes · Vernonia · Schizostylis · Hibiscus moscheutos · Nerine · Cornus canadensis | ✅ |
| 31 | Petasites · Zantedeschia · Romneya · Myosotis · Valeriana · Anchusa · Draba · Dryas | ✅ |
| 32 | Arum · Iberis · Hieracium · Senecio · Sphaeralcea · Meehania · Ruellia · Verbesina · Pimpinella | ✅ |

### Siergrassen — batchplan

| # | Genera | Status |
|---|---|---|
| S1 | Briza · Deschampsia · Helictotrichon · Luzula · Milium | ✅ |
| S2 | Anemanthele · Chasmanthium · Imperata · Schizachyrium · Sorghastrum · Sporobolus | ✅ |
| S3 | Elymus · Eragrostis · Koeleria · Leymus · Melica · Muehlenbergia · Sesleria · Spodiopogon | ✅ |

### Bodembedekkers — batchplan

| # | Genera | Status |
|---|---|---|
| B1 | Acaena · Arabis · Asarum · Aubrieta · Chiastophyllum · Galium · Houttuynia | ✅ |
| B2 | Arctostaphylos · Arenaria · Aurinia · Cerastium · Leptinella · Mazus · Sagina | ✅ |

### Varens (als vaste plant) — batchplan

| # | Genera | Status |
|---|---|---|
| V1 | Adiantum · Athyrium · Blechnum · Matteuccia · Osmunda · Polystichum | ✅ |
| V2 | Asplenium · Cyrtomium · Onoclea · Phyllitis | ✅ |

### Klimplanten — batchplan

**Doel: volledig assortiment** — voeg *alle* cultivars toe die Muijderman voert, geen selectie.

| # | Genera | Status |
|---|---|---|
| K1 | Clematis | ✅ |
| K2 | Hedera · Lonicera · Parthenocissus · Wisteria | ✅ |
| K3 | Actinidia · Campsis · Hydrangea petiolaris · Passiflora · Schizophragma | ✅ |

---

## Catalogus uitbreiden — bomen-heesters.html

De PLANTS-array in `data/bomen-heesters.js` is nog niet compleet. Op basis van het volledige Muijderman-assortiment ontbreken ~60 genera bomen, heesters en conifeers.

**Werkwijze:** voeg per sessie 1 batch toe (5–7 genera) aan `data/bomen-heesters.js`, commit daarna, en markeer de batch hieronder als ✅.

> **Volgende sessie:** start bij de eerste batch die nog ⬜ heeft.

### Bomen — batchplan

| # | Genera | Status |
|---|---|---|
| BH1 | Halesia · Ginkgo · Cercidiphyllum · Davidia · Nyssa | ✅ |
| BH2 | Koelreuteria · Sophora · Morus · Juglans · Pterocarya | ✅ |
| BH3 | Oxydendrum · Stewartia · Franklinia · Sassafras · Nothofagus | ✅ |
| BH4 | Eucalyptus · Tetradium · Idesia · Ptelea · Pterostyrax | ✅ |

### Heesters — batchplan

| # | Genera | Status |
|---|---|---|
| BH5 | Abeliophyllum · Edgeworthia · Sarcococca · Stachyurus · Jasminum nudiflorum | ✅ |
| BH6 | Clethra · Lagerstroemia · Vitex · Lespedeza · Spartium · Clerodendrum | ✅ |
| BH7 | Aronia · Rhus · Leucothoe · Vaccinium · Fuchsia | ✅ |
| BH8 | Kalmia · Zenobia · Sinocalycanthus · Diervilla · Escallonia | ✅ |
| BH9 | Decaisnea · Tamarix · Caragana · Rhodotypos · Genista · Ulex | ✅ |
| BH10 | Rhaphiolepis · Neillia · Corokia · Xanthorhiza · Rostrinucula | ✅ |

### Conifeers — batchplan

| # | Genera | Status |
|---|---|---|
| BHC1 | Cryptomeria · Larix · Microbiota · Sciadopitys · Sequoiadendron | ✅ |

### Aanvulling na hercontrole

| # | Genera | Status |
|---|---|---|
| BH11 | Aralia · Chitalpa · Chionanthus · Heptacodium · Maclura · Xanthoceras · Ziziphus | ✅ |
| BH12 | Arbutus · Cistus · Colutea · Distylium · Elsholtzia · Frangula · Myrica · Poncirus · Staphylea · Sycoparrotia · Sycopsis · Tetrapanax | ✅ |
| BH13 | Erica · Calluna | ✅ |
| BH14 | Vitis · Rubus | ✅ |
| BH15 | Phyllostachys · Fargesia · Pleioblastus · Sasa (bamboe, cat:"heester") | ✅ |
| BH16 | Rosa struikrozen · Rosa klimrozen · Rosa bodembedekkers (cat:"rosa") | ✅ |

### Aanvulling na assortimentslijst-analyse (2026-04)

**data/vaste-planten.js aanvullingen:**

| # | Inhoud | Status |
|---|--------|--------|
| VP-K1 | Klimplanten: Akebia · Ampelopsis · Aristolochia · Celastrus · Fallopia · Humulus | ✅ |
| VP-K2 | Klimplanten: Jasminum off. · Kadsura · Lathyrus · Periploca · Pileostegia · Stauntonia | ✅ |
| VP-V1 | Aster deel 1: ageratifolius · alpinus · amellus · cordifolius · divaricatus · ericoides | ✅ |
| VP-V2 | Aster deel 2: frikartii · laevis · lateriflorus · linosyris · macrophyllus · novae-belgii | ✅ |
| VP-V3 | Aster deel 3: peduncularis · pyrenaeus · ptarmicoides · radula · sedifolius · tataricus · thomsonii · tongolensis · hybrides · pilosus pringlei | ✅ |
| VP-V4 | Campanula: carpatica · garganica · glomerata · lactiflora · latifolia · latiloba · portenschlagiana · poscharskyana · rapunculoides · Pink Octopus · Sarastro | ✅ |
| VP-V5 | Iris germanica (20 cv) · pumila (6 cv) | ✅ |
| VP-V6 | Iris ensata · foetidissima · pallida · pseudacorus · reticulata | ✅ |
| VP-V7 | Geranium deel 1: endressii · himalayense · Johnson's Blue · nodosum · oxonianum · pratense | ✅ |
| VP-V8 | Geranium deel 2: psilostemon · renardii · riversleaianum · Rozanne · sylvaticum · versicolor · wlassovianum + 21 hybride cv | ✅ |
| VP-V9 | Actaea pachypoda · Queen of Sheba · Cimicifuga japonica · racemosa · ramosa; simplex uitgebreid | ✅ |
| VP-V10 | Digitalis ferruginea/lutea/mertonensis/parviflora · Lobelia gerardii/siphilitica/speciosa/tania · Lysimachia atropurpurea/barystachys/ciliata/clethroides/ephemerum/nummularia | ✅ |
| VP-V11 | Paeonia officinalis + suffruticosa · Oenothera fruticosa/missouriensis/speciosa · Rodgersia aesculifolia/henrici/podophylla/sambucifolia | ✅ |
| VP-V12 | Cortaderia selloana (pampasgras) | ✅ |
| VP-V13 | Trachelospermum + Schizophragma extra cv (al aanwezig) | ✅ |

**data/bomen-heesters.js aanvullingen:**

| # | Inhoud | Status |
|---|--------|--------|
| BH-A1 | Ilex crenata (8 cv) · meserveae (6 cv) als aparte entries; koehneana bij aquifolium | ✅ |
| BH-A2 | Ribes sanguineum · nigrum · rubrum · uva-crispa | ✅ |
| BH-A3 | Photinia fraseri (4 cv); Ligustrum extra soorten al aanwezig als cv | ✅ |
| BH-A4 | Cordyline australis · Hebe · Helwingia chinensis | ✅ |
| BH-A5 | Corylus maxima 'Purpurea' · Picea abies/glauca/omorika/orientalis · Cephalotaxus harringtonia | ✅ |

---

## Genus-detailpagina's — voortgang

### Infrastructuur
| # | Omschrijving | Status |
|---|---|---|
| Batch 1 | genus.html · css/genus.css · js/genus.js · "Meer info →" in cardHTML | ✅ |

### Zorgkalender — `data/vaste-planten.js` (407 entries, ~25 per batch)

**Aanpak:** Python-invoegscript per batch. Voegt `zorgkalender:{...}` in vóór `cv:[` op basis van `l:"<naam>"`.

**Status: ✅ VOLLEDIG — alle 407 entries verrijkt (scripts/zk1_insert.py t/m zk15_insert.py)**

| # | Genera (eerste → laatste, gesorteerd) | Status |
|---|---|---|
| ZK1 | Acaena → Anemone nemorosa (26 entries) | ✅ |
| ZK2 | Anemonella → Asplenium (25 entries) | ✅ |
| ZK3 | Aster ageratifolius → Baptisia (21 entries) | ✅ |
| ZK4 | Beesia → Campanula poscharskyana (25 entries) | ✅ |
| ZK5 | Campanula rapunculoides → Cosmos (30 entries) | ✅ |
| ZK6 | Crambe → Dystaenia (25 entries) | ✅ |
| ZK7 | Echinacea → Geranium cantabrigiense (27 entries) | ✅ |
| ZK8 | Geranium macrorrhizum → Humulus (28 entries) | ✅ |
| ZK9 | Hydrangea petiolaris → Lysimachia atropurpurea (50 entries) | ✅ |
| ZK10 | Hemerocallis → Miscanthus sinensis (25 entries) | ✅ |
| ZK11 | Mitella → Parthenium (25 entries) | ✅ |
| ZK12 | Passiflora → Primula (25 entries) | ✅ |
| ZK13 | Prunella → Senecio (25 entries) | ✅ |
| ZK14 | Serratula → Thermopsis (25 entries) | ✅ |
| ZK15 | Thymus → Zantedeschia + resterende klimplanten (21 entries) | ✅ |

### Combinatieplanten — `data/vaste-planten.js`

**Status: ✅ VOLLEDIG — alle 407 entries verrijkt (scripts/cp1_insert.py t/m cp12_insert.py)**

| # | Genera | Status |
|---|---|---|
| CP1–CP12 | Alle 407 genera in 12 batches van ~34 entries | ✅ |

### Bomen/heesters detailpagina
| # | Omschrijving | Status |
|---|---|---|
| BH-Detail | genus-bh.html + "Meer info →" in bomen-heesters cards | ⬜ |
| BH-ZK1–4 | Zorgkalender data bomen/heesters (4 batches) | ⬜ |
