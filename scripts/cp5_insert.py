#!/usr/bin/env python3
"""CP5: Combinatieplanten voor Panicum virgatum t/m Polemonium caeruleum (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Panicum virgatum": ["Echinacea purpurea", "Rudbeckia fulgida", "Helenium autumnale", "Persicaria amplexicaulis", "Sanguisorba officinalis"],
    "Pennisetum alopecuroides": ["Echinacea purpurea", "Rudbeckia fulgida", "Persicaria amplexicaulis", "Miscanthus sinensis", "Solidago"],
    "Stipa": ["Verbena bonariensis", "Coreopsis verticillata", "Salvia nemorosa", "Echinacea purpurea", "Knautia macedonica"],
    "Anemone nemorosa": ["Brunnera macrophylla", "Pulmonaria", "Primula", "Galium odoratum", "Convallaria majalis"],
    "Carex": ["Hosta", "Brunnera macrophylla", "Astilbe", "Dryopteris filix-mas", "Hakonechloa macra"],
    "Aster novae-angliae": ["Solidago", "Helenium autumnale", "Rudbeckia fulgida", "Persicaria amplexicaulis", "Pennisetum alopecuroides"],
    "Bergenia": ["Helleborus", "Epimedium", "Pulmonaria", "Pachysandra terminalis", "Galium odoratum"],
    "Crocosmia": ["Kniphofia", "Hemerocallis", "Achillea filipendulina", "Helenium autumnale", "Rudbeckia fulgida"],
    "Geum": ["Salvia nemorosa", "Nepeta faassenii", "Aquilegia vulgaris", "Alchemilla mollis", "Achillea millefolium"],
    "Leucanthemum": ["Salvia nemorosa", "Achillea millefolium", "Centranthus ruber", "Monarda", "Phlox paniculata"],
    "Delphinium": ["Phlox paniculata", "Achillea millefolium", "Veronicastrum virginicum", "Lupinus", "Geranium pratense"],
    "Heuchera": ["Tiarella cordifolia", "Astilbe", "Hosta", "Brunnera macrophylla", "Pulmonaria"],
    "Iris sibirica": ["Baptisia australis", "Trollius europaeus", "Campanula 'Sarastro'", "Lupinus", "Aquilegia vulgaris"],
    "Iris germanica": ["Salvia nemorosa", "Allium", "Nepeta faassenii", "Paeonia lactiflora", "Stachys byzantina"],
    "Iris pumila": ["Thymus serpyllum", "Dianthus", "Stachys byzantina", "Salvia nemorosa", "Festuca glauca"],
    "Iris ensata": ["Iris pseudacorus", "Lythrum salicaria", "Ligularia dentata", "Astilbe", "Filipendula"],
    "Iris foetidissima": ["Helleborus", "Epimedium", "Pachysandra terminalis", "Polystichum", "Dryopteris filix-mas"],
    "Iris pallida": ["Salvia nemorosa", "Allium", "Stachys byzantina", "Nepeta faassenii", "Achillea millefolium"],
    "Iris pseudacorus": ["Lythrum salicaria", "Caltha palustris", "Lysimachia clethroides", "Ligularia dentata", "Eupatorium maculatum"],
    "Iris reticulata": ["Primula", "Pulmonaria", "Brunnera macrophylla", "Hepatica", "Anemone nemorosa"],
    "Liatris spicata": ["Echinacea purpurea", "Rudbeckia fulgida", "Pennisetum alopecuroides", "Salvia nemorosa", "Achillea millefolium"],
    "Lupinus": ["Delphinium", "Iris sibirica", "Baptisia australis", "Geranium 'Johnson's Blue'", "Aquilegia vulgaris"],
    "Agapanthus": ["Salvia nemorosa", "Stachys byzantina", "Achillea millefolium", "Echinops ritro", "Perovskia atriplicifolia"],
    "Centaurea montana": ["Salvia nemorosa", "Aquilegia vulgaris", "Geranium 'Johnson's Blue'", "Nepeta faassenii", "Stachys byzantina"],
    "Dianthus": ["Salvia nemorosa", "Thymus serpyllum", "Festuca glauca", "Stachys byzantina", "Achillea millefolium"],
    "Papaver orientale": ["Salvia nemorosa", "Nepeta faassenii", "Stachys byzantina", "Achillea millefolium", "Geranium psilostemon"],
    "Pulsatilla vulgaris": ["Arabis", "Aubrieta", "Thymus serpyllum", "Dianthus", "Primula"],
    "Euphorbia": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Allium", "Stachys byzantina", "Tulbaghia violacea"],
    "Helianthus": ["Rudbeckia fulgida", "Helenium autumnale", "Persicaria amplexicaulis", "Echinacea purpurea", "Solidago"],
    "Heliopsis helianthoides": ["Rudbeckia fulgida", "Echinacea purpurea", "Helenium autumnale", "Monarda", "Veronicastrum virginicum"],
    "Primula": ["Pulmonaria", "Brunnera macrophylla", "Anemone nemorosa", "Iris reticulata", "Hepatica"],
    "Veronica": ["Salvia nemorosa", "Stachys byzantina", "Achillea millefolium", "Nepeta faassenii", "Centranthus ruber"],
    "Platycodon grandiflorus": ["Salvia nemorosa", "Nepeta faassenii", "Centranthus ruber", "Stachys byzantina", "Penstemon"],
    "Polemonium caeruleum": ["Aquilegia vulgaris", "Geranium 'Johnson's Blue'", "Salvia nemorosa", "Brunnera macrophylla", "Pulmonaria"],
}

def build_cp_str(cp_list):
    items = ",".join(f'"{n}"' for n in cp_list)
    return f"[{items}]"

def insert_combinaties(content, latin_name, cp_list):
    search = f'l:"{latin_name}"'
    idx = content.find(search)
    if idx == -1:
        print(f"  NIET GEVONDEN: {latin_name}")
        return content, False
    cv_marker = ', cv:['
    cv_idx = content.find(cv_marker, idx, idx + 20000)
    if cv_idx == -1:
        print(f"  cv:[ niet gevonden na: {latin_name}")
        return content, False
    if 'combinatieplanten' in content[idx:cv_idx]:
        print(f"  AL AANWEZIG (overgeslagen): {latin_name}")
        return content, False
    cp_str = f', combinatieplanten:{build_cp_str(cp_list)}'
    new_content = content[:cv_idx] + cp_str + content[cv_idx:]
    print(f"  OK: {latin_name}")
    return new_content, True

def validate(content, combinaties):
    all_names = set(re.findall(r'\{ n:"[^"]*", l:"([^"]+)"', content))
    missing = []
    for plant, partners in combinaties.items():
        for p in partners:
            if p not in all_names:
                missing.append(f"  '{p}' (partner van {plant})")
    if missing:
        print(f"\n⚠ Niet gevonden in catalogus ({len(missing)}):")
        for m in missing:
            print(m)
    else:
        print("\n✓ Alle namen gevalideerd.")

def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    validate(content, COMBINATIES)
    updated = 0
    for latin_name, cp in COMBINATIES.items():
        content, changed = insert_combinaties(content, latin_name, cp)
        if changed:
            updated += 1
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nKlaar. {updated}/{len(COMBINATIES)} entries bijgewerkt.")

if __name__ == '__main__':
    main()
