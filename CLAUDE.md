# CLAUDE.md — Flowers / Kwekerij Muijderman Plant Catalogue

## Project Overview

A self-contained, single-file static web application for **Kwekerij Muijderman** (Muijderman Nursery) in Veldhoven, Netherlands.

### Doel / Purpose

Het doel van deze app is het **doorzoekbaar en overzichtelijk maken van de plantenassortiment van Kwekerij Muijderman**. De kwekerij verkoopt een groot en gevarieerd assortiment vaste planten, bodembedekkers en siergrassen. De officiële assortimentslijst is te vinden op:

> https://www.kwekerijmuijderman.nl/assortiment/overzicht

**Scope:** alleen de categorie *vaste planten* (inclusief bodembedekkers en siergrassen) uit het Muijderman-assortiment valt binnen de scope van deze app. Andere categorieën die de kwekerij voert — zoals bomen, heesters, klimplanten of seizoensplanten — worden **buiten beschouwing gelaten** en mogen niet worden toegevoegd aan de `PLANTS`-array.

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

Everything lives in one file: `index.html`.

| Lines | Content |
|-------|---------|
| 1–5 | HTML boilerplate, `lang="nl"`, viewport meta |
| 6–74 | Embedded `<style>` block — all CSS |
| 67–73 | CSS comment with field reference for adding new plants |
| 76–112 | HTML structure: `<header>`, `.toolbar`, `.grid`, `<footer>` |
| 111–215 | `<script>`: `PLANTS` array (the data) |
| 217–376 | `<script>`: state variables, functions, event listeners, init call |

**Do not split this into multiple files** unless explicitly asked. The single-file approach is intentional — it keeps deployment trivial (any static host, GitHub Pages, direct file open).

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

**Adding a new plant:** copy any existing entry, adjust all fields, and insert it into the `PLANTS` array. The CSS comment at lines 67–73 gives the same field reference.

---

## Key Functions

| Function | Location | Purpose |
|----------|----------|---------|
| `flower(c)` | line 222 | Generates an inline SVG flower illustration using the plant's hex colour `c` |
| `glink(l, cv)` | line 238 | Returns a Google Images URL for Latin name + cultivar |
| `cardHTML(p)` | line 242 | Returns the full HTML string for a plant card, including cultivar list |
| `applyFilter()` | line 289 | Filters `PLANTS` into `filtered[]` based on current `filter`, `filterLicht`, and `query`; resets pagination and re-renders |
| `renderMore()` | line 303 | Appends the next page slice (`PAGE = 8`) of `filtered[]` to `#grid` using `insertAdjacentHTML` |
| `saveFav()` | line 220 | Persists the `favorieten` Set to `localStorage` as JSON |

---

## State Variables (lines 218–220)

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

Filters are **independent and ANDed** (`applyFilter`, line 289):

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

- `localStorage` key: `'mj_fav'`
- Value: JSON array of favourite ID strings, e.g. `["Echinacea purpurea||'Magnus'", …]`
- Read on page load (line 219), written by `saveFav()` after every toggle.

---

## CSS Conventions

- All styles are in the single embedded `<style>` block (lines 7–74).
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
1. Open `index.html` in a browser (file:// or any local server).
2. Edit and reload.

**To test:**
- Manual testing in the browser is the only test method.
- Verify all filter combinations, search, favourites toggle, and infinite scroll.
- Check mobile layout (resize browser or use DevTools).

**To deploy:**
- Copy `index.html` to any static host (GitHub Pages, Netlify, a plain web server). No build step needed.

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
- **Do not split the file** into separate HTML/CSS/JS files without a clear request.
- **Do not add external dependencies** (React, Vue, jQuery, Tailwind, etc.).
- **Do not add TypeScript** — the project is intentionally plain JavaScript.
- **Do not add a `<link>` to an external stylesheet** — all styles stay embedded.
- **Do not change the Dutch language** of the UI or data without being asked.
- **Do not add automated tests** speculatively — there is no test infrastructure.
- **Do not introduce CSS custom properties** unless refactoring all hardcoded colours at once.

---

## Extending the Catalogue

To add a new plant category beyond `"vaste plant"`, `"bodembedekker"`, `"siergras"`:

1. Add the `cat` value to the new plant entry.
2. Add a filter button in `#filters` with the matching `data-filter` attribute (line 86–96).
3. Add a CSS badge class `.badge-<suffix>` in the `<style>` block.
4. Update the badge selector ternary in `cardHTML` (line 272).

To add a new light requirement beyond `"zon"`, `"halfschaduw"`, `"schaduw"`:

1. Add a button in `#filters-licht` with `data-licht="<value>"`.
2. Add a CSS pill class and update the pill ternary in `cardHTML` (line 277).

---

## Catalogus uitbreiden — voortgang

De PLANTS-array is nog niet compleet. Het volledige Muijderman-assortiment bevat ~90 extra genera voor vaste planten plus ~13 siergrassen en ~8 bodembedekkers die nog niet in de app staan.

**Werkwijze:** voeg per sessie 1 batch toe (5–7 genera), commit daarna, en markeer de batch hieronder als ✅.

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

---

## Catalogus uitbreiden — bomen-heesters.html

De PLANTS-array in `bomen-heesters.html` is nog niet compleet. Op basis van het volledige Muijderman-assortiment ontbreken ~60 genera bomen, heesters en conifeers.

**Werkwijze:** voeg per sessie 1 batch toe (5–7 genera), commit daarna, en markeer de batch hieronder als ✅.

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
