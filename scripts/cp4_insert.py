#!/usr/bin/env python3
"""CP4: Combinatieplanten voor Geranium sylvaticum t/m Molinia (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Geranium sylvaticum": ["Alchemilla mollis", "Aquilegia vulgaris", "Astrantia major", "Digitalis purpurea", "Thalictrum aquilegiifolium"],
    "Geranium versicolor": ["Alchemilla mollis", "Geranium endressii", "Astrantia major", "Aquilegia vulgaris", "Pulmonaria"],
    "Geranium wlassovianum": ["Aster novae-angliae", "Persicaria amplexicaulis", "Helenium autumnale", "Stachys byzantina", "Salvia nemorosa"],
    "Geranium hybride": ["Alchemilla mollis", "Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Aquilegia vulgaris"],
    "Alchemilla mollis": ["Astrantia major", "Geranium phaeum", "Digitalis purpurea", "Aquilegia vulgaris", "Hosta"],
    "Actaea simplex": ["Aconitum carmichaelii", "Anemone hupehensis", "Hosta", "Astilbe", "Cimicifuga racemosa"],
    "Actaea pachypoda": ["Trillium", "Polygonatum multiflorum", "Hosta", "Dryopteris filix-mas", "Brunnera macrophylla"],
    "Actaea 'Queen of Sheba'": ["Hosta", "Astilbe", "Alchemilla mollis", "Brunnera macrophylla", "Dryopteris filix-mas"],
    "Cimicifuga japonica": ["Aconitum carmichaelii", "Actaea simplex", "Anemone hupehensis", "Hosta", "Dryopteris filix-mas"],
    "Cimicifuga racemosa": ["Astilbe", "Hosta", "Actaea simplex", "Aconitum carmichaelii", "Thalictrum aquilegiifolium"],
    "Cimicifuga ramosa": ["Anemone hupehensis", "Hosta", "Astilbe", "Actaea simplex", "Alchemilla mollis"],
    "Aruncus dioicus": ["Astilbe", "Rodgersia pinnata", "Hosta", "Thalictrum aquilegiifolium", "Dryopteris filix-mas"],
    "Astilbe": ["Hosta", "Rodgersia pinnata", "Aruncus dioicus", "Dryopteris filix-mas", "Tiarella cordifolia"],
    "Brunnera macrophylla": ["Hosta", "Pulmonaria", "Lamium maculatum", "Astilbe", "Geranium macrorrhizum"],
    "Hosta": ["Astilbe", "Brunnera macrophylla", "Aruncus dioicus", "Rodgersia pinnata", "Dryopteris filix-mas"],
    "Lamium maculatum": ["Brunnera macrophylla", "Pulmonaria", "Geranium macrorrhizum", "Ajuga reptans", "Helleborus"],
    "Pulmonaria": ["Brunnera macrophylla", "Helleborus", "Lamium maculatum", "Primula", "Epimedium"],
    "Polygonatum multiflorum": ["Hosta", "Astilbe", "Actaea pachypoda", "Brunnera macrophylla", "Dryopteris filix-mas"],
    "Tiarella cordifolia": ["Astilbe", "Hosta", "Brunnera macrophylla", "Pulmonaria", "Epimedium"],
    "Rodgersia pinnata": ["Hosta", "Astilbe", "Ligularia dentata", "Dryopteris filix-mas", "Aruncus dioicus"],
    "Rodgersia aesculifolia": ["Hosta", "Ligularia dentata", "Rodgersia pinnata", "Dryopteris filix-mas", "Astilbe"],
    "Rodgersia henrici": ["Hosta", "Astilbe", "Rodgersia pinnata", "Dryopteris filix-mas", "Aruncus dioicus"],
    "Rodgersia podophylla": ["Hosta", "Ligularia dentata", "Astilbe", "Dryopteris filix-mas", "Rodgersia pinnata"],
    "Rodgersia sambucifolia": ["Hosta", "Astilbe", "Rodgersia pinnata", "Ligularia dentata", "Dryopteris filix-mas"],
    "Dryopteris filix-mas": ["Hosta", "Polygonatum multiflorum", "Astilbe", "Brunnera macrophylla", "Actaea pachypoda"],
    "Pachysandra terminalis": ["Helleborus", "Pulmonaria", "Epimedium", "Lamium maculatum", "Galium odoratum"],
    "Convallaria majalis": ["Hosta", "Polygonatum multiflorum", "Brunnera macrophylla", "Lamium maculatum", "Pulmonaria"],
    "Lamprocapnos spectabilis": ["Brunnera macrophylla", "Pulmonaria", "Epimedium", "Hosta", "Aquilegia vulgaris"],
    "Helleborus": ["Epimedium", "Pulmonaria", "Pachysandra terminalis", "Brunnera macrophylla", "Galium odoratum"],
    "Waldsteinia ternata": ["Pachysandra terminalis", "Epimedium", "Galium odoratum", "Lamium maculatum", "Helleborus"],
    "Calamagrostis acutiflora": ["Persicaria amplexicaulis", "Echinacea purpurea", "Rudbeckia fulgida", "Salvia nemorosa", "Sanguisorba officinalis"],
    "Hakonechloa macra": ["Hosta", "Astilbe", "Brunnera macrophylla", "Dryopteris filix-mas", "Polygonatum multiflorum"],
    "Miscanthus sinensis": ["Pennisetum alopecuroides", "Echinacea purpurea", "Rudbeckia fulgida", "Helenium autumnale", "Persicaria amplexicaulis"],
    "Molinia": ["Sanguisorba officinalis", "Persicaria amplexicaulis", "Eupatorium maculatum", "Pennisetum alopecuroides", "Lythrum salicaria"],
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
