#!/usr/bin/env python3
"""CP12: Combinatieplanten voor Aristolochia t/m Stauntonia hexaphylla (33 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Aristolochia": ["Hosta", "Brunnera macrophylla", "Polygonatum multiflorum", "Dryopteris filix-mas", "Helleborus"],
    "Celastrus orbiculatus": ["Hosta", "Carex", "Helleborus", "Aster novae-angliae", "Persicaria amplexicaulis"],
    "Fallopia": ["Eupatorium maculatum", "Persicaria amplexicaulis", "Rudbeckia fulgida", "Sanguisorba officinalis", "Vernonia"],
    "Humulus lupulus": ["Aruncus dioicus", "Rodgersia aesculifolia", "Hosta", "Dryopteris filix-mas", "Eupatorium maculatum"],
    "Aster ageratifolius": ["Thymus serpyllum", "Dianthus", "Festuca glauca", "Pulsatilla vulgaris", "Saxifraga"],
    "Aster alpinus": ["Dianthus", "Thymus serpyllum", "Festuca glauca", "Aubrieta", "Arabis"],
    "Aster amellus": ["Salvia nemorosa", "Echinops ritro", "Stachys byzantina", "Festuca glauca", "Centranthus ruber"],
    "Aster cordifolius": ["Actaea simplex", "Persicaria amplexicaulis", "Anemone hupehensis", "Sanguisorba officinalis", "Deschampsia"],
    "Aster divaricatus": ["Hosta", "Brunnera macrophylla", "Actaea simplex", "Polygonatum multiflorum", "Dryopteris filix-mas"],
    "Aster ericoides": ["Sanguisorba officinalis", "Persicaria amplexicaulis", "Salvia nemorosa", "Sporobolus heterolepis", "Molinia"],
    "Aster frikartii": ["Salvia nemorosa", "Helenium autumnale", "Rudbeckia fulgida", "Echinacea purpurea", "Stachys byzantina"],
    "Aster laevis": ["Sanguisorba officinalis", "Echinacea purpurea", "Rudbeckia fulgida", "Sporobolus heterolepis", "Schizachyrium scoparium"],
    "Aster lateriflorus": ["Actaea simplex", "Persicaria amplexicaulis", "Sanguisorba officinalis", "Sporobolus heterolepis", "Molinia"],
    "Aster linosyris": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Festuca glauca", "Centranthus ruber"],
    "Aster macrophyllus": ["Hosta", "Brunnera macrophylla", "Dryopteris filix-mas", "Actaea simplex", "Polygonatum multiflorum"],
    "Aster novae-belgii": ["Helenium autumnale", "Rudbeckia fulgida", "Echinacea purpurea", "Sanguisorba officinalis", "Persicaria amplexicaulis"],
    "Aster peduncularis": ["Sanguisorba officinalis", "Actaea simplex", "Molinia", "Persicaria amplexicaulis", "Deschampsia"],
    "Aster pyrenaeus": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Centranthus ruber", "Achillea millefolium", "Stachys byzantina"],
    "Aster ptarmicoides": ["Echinacea purpurea", "Salvia nemorosa", "Sporobolus heterolepis", "Schizachyrium scoparium", "Sanguisorba officinalis"],
    "Aster radula": ["Sanguisorba officinalis", "Eupatorium maculatum", "Lythrum salicaria", "Molinia", "Persicaria amplexicaulis"],
    "Aster sedifolius": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Centranthus ruber", "Festuca glauca"],
    "Aster tataricus": ["Eupatorium maculatum", "Vernonia", "Persicaria amplexicaulis", "Rudbeckia fulgida", "Sanguisorba officinalis"],
    "Aster thomsonii": ["Salvia nemorosa", "Actaea simplex", "Persicaria amplexicaulis", "Anemone hupehensis", "Sanguisorba officinalis"],
    "Aster tongolensis": ["Geranium 'Johnson's Blue'", "Salvia nemorosa", "Iris sibirica", "Aquilegia vulgaris", "Centranthus ruber"],
    "Aster hybride": ["Helenium autumnale", "Rudbeckia fulgida", "Echinacea purpurea", "Sanguisorba officinalis", "Persicaria amplexicaulis"],
    "Aster pilosus pringlei": ["Actaea simplex", "Sanguisorba officinalis", "Sporobolus heterolepis", "Persicaria amplexicaulis", "Molinia"],
    "Jasminum officinale": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Nepeta faassenii", "Alchemilla mollis", "Clematis"],
    "Kadsura japonica": ["Hosta", "Helleborus", "Brunnera macrophylla", "Epimedium", "Galium odoratum"],
    "Lathyrus latifolius": ["Salvia nemorosa", "Centranthus ruber", "Achillea millefolium", "Verbena bonariensis", "Geranium 'Johnson's Blue'"],
    "Lathyrus vernus": ["Pulmonaria", "Brunnera macrophylla", "Primula", "Hepatica", "Anemone nemorosa"],
    "Periploca graeca": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Centranthus ruber", "Achillea millefolium"],
    "Pileostegia viburnoides": ["Hosta", "Helleborus", "Brunnera macrophylla", "Epimedium", "Galium odoratum"],
    "Stauntonia hexaphylla": ["Hosta", "Brunnera macrophylla", "Helleborus", "Epimedium", "Galium odoratum"],
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
