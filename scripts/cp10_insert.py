#!/usr/bin/env python3
"""CP10: Combinatieplanten voor Galega t/m Vernonia (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Galega": ["Thalictrum aquilegiifolium", "Eupatorium maculatum", "Veronicastrum virginicum", "Achillea millefolium", "Astrantia major"],
    "Dendranthema": ["Aster novae-angliae", "Helenium autumnale", "Rudbeckia fulgida", "Persicaria amplexicaulis", "Solidago"],
    "Dystaenia takesimana": ["Rodgersia aesculifolia", "Ligularia dentata", "Dryopteris filix-mas", "Hosta", "Darmera peltata"],
    "Erodium": ["Dianthus", "Thymus serpyllum", "Stachys byzantina", "Salvia nemorosa", "Festuca glauca"],
    "Gaura lindheimeri": ["Salvia nemorosa", "Stachys byzantina", "Perovskia atriplicifolia", "Penstemon", "Nepeta faassenii"],
    "Houstonia caerulea": ["Primula", "Arabis", "Thymus serpyllum", "Mazus reptans", "Saxifraga"],
    "Peucedanum verticillare": ["Salvia nemorosa", "Verbena bonariensis", "Selinum", "Stachys byzantina", "Eryngium planum"],
    "Betonica officinalis": ["Salvia nemorosa", "Stachys byzantina", "Knautia macedonica", "Centranthus ruber", "Scabiosa columbaria"],
    "Boltonia asteroides": ["Aster novae-angliae", "Helenium autumnale", "Echinacea purpurea", "Rudbeckia fulgida", "Pennisetum alopecuroides"],
    "Buglossoides purpurocaerulea": ["Pulmonaria", "Brunnera macrophylla", "Geranium endressii", "Alchemilla mollis", "Epimedium"],
    "Chelonopsis moschata": ["Hosta", "Astilbe", "Actaea simplex", "Dryopteris filix-mas", "Rodgersia pinnata"],
    "Chrysogonum virginianum": ["Epimedium", "Pulmonaria", "Pachysandra terminalis", "Brunnera macrophylla", "Helleborus"],
    "Chrysosplenium macrophyllum": ["Hosta", "Brunnera macrophylla", "Carex", "Galium odoratum", "Pulmonaria"],
    "Alstroemeria": ["Salvia nemorosa", "Achillea millefolium", "Penstemon", "Geum", "Centranthus ruber"],
    "Althaea": ["Delphinium", "Phlox paniculata", "Achillea millefolium", "Verbascum", "Centranthus ruber"],
    "Anemonopsis macrophylla": ["Hosta", "Astilbe", "Brunnera macrophylla", "Actaea simplex", "Dryopteris filix-mas"],
    "Asphodeline lutea": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Eryngium planum", "Allium"],
    "Beesia calthifolia": ["Hosta", "Epimedium", "Pulmonaria", "Helleborus", "Pachysandra terminalis"],
    "Belamcanda chinensis": ["Iris germanica", "Iris sibirica", "Salvia nemorosa", "Stachys byzantina", "Allium"],
    "Origanum": ["Salvia nemorosa", "Centranthus ruber", "Stachys byzantina", "Thymus serpyllum", "Achillea millefolium"],
    "Dicentra": ["Brunnera macrophylla", "Pulmonaria", "Hosta", "Primula", "Epimedium"],
    "Corydalis": ["Brunnera macrophylla", "Pulmonaria", "Hosta", "Primula", "Hepatica"],
    "Physostegia virginiana": ["Eupatorium maculatum", "Lythrum salicaria", "Lobelia cardinalis", "Persicaria amplexicaulis", "Filipendula"],
    "Doronicum": ["Primula", "Pulmonaria", "Brunnera macrophylla", "Aquilegia vulgaris", "Anemone nemorosa"],
    "Epimedium": ["Helleborus", "Pulmonaria", "Tiarella cordifolia", "Pachysandra terminalis", "Galium odoratum"],
    "Filipendula": ["Lythrum salicaria", "Eupatorium maculatum", "Iris pseudacorus", "Lysimachia clethroides", "Sanguisorba officinalis"],
    "Alcea": ["Delphinium", "Phlox paniculata", "Verbascum", "Centranthus ruber", "Achillea millefolium"],
    "Helianthemum": ["Thymus serpyllum", "Dianthus", "Stachys byzantina", "Festuca glauca", "Saxifraga"],
    "Eremurus": ["Allium", "Salvia nemorosa", "Stachys byzantina", "Iris germanica", "Achillea filipendulina"],
    "Epilobium angustifolium": ["Eupatorium maculatum", "Lythrum salicaria", "Filipendula", "Verbena bonariensis", "Sanguisorba officinalis"],
    "Hesperis matronalis": ["Aquilegia vulgaris", "Digitalis purpurea", "Geranium phaeum", "Alchemilla mollis", "Astrantia major"],
    "Angelica": ["Eupatorium maculatum", "Filipendula", "Rodgersia aesculifolia", "Aruncus dioicus", "Persicaria amplexicaulis"],
    "Strobilanthes": ["Salvia nemorosa", "Penstemon", "Agastache", "Nepeta faassenii", "Aster novae-angliae"],
    "Vernonia": ["Eupatorium maculatum", "Veronicastrum virginicum", "Persicaria amplexicaulis", "Sanguisorba officinalis", "Echinacea purpurea"],
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
