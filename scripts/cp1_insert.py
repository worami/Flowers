#!/usr/bin/env python3
"""CP1: Combinatieplanten voor Baptisia australis t/m Geranium sanguineum (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Baptisia australis": ["Iris sibirica", "Salvia nemorosa", "Geranium 'Johnson's Blue'", "Aquilegia vulgaris", "Allium"],
    "Echinacea purpurea": ["Rudbeckia fulgida", "Sanguisorba officinalis", "Agastache", "Helenium autumnale", "Pennisetum alopecuroides"],
    "Rudbeckia fulgida": ["Echinacea purpurea", "Helenium autumnale", "Persicaria amplexicaulis", "Pennisetum alopecuroides", "Calamagrostis acutiflora"],
    "Hemerocallis": ["Salvia nemorosa", "Nepeta faassenii", "Achillea millefolium", "Penstemon", "Kniphofia"],
    "Echinops ritro": ["Eryngium planum", "Stachys byzantina", "Salvia nemorosa", "Centranthus ruber", "Achillea filipendulina"],
    "Lythrum salicaria": ["Iris pseudacorus", "Ligularia dentata", "Eupatorium maculatum", "Filipendula", "Lysimachia clethroides"],
    "Helenium autumnale": ["Rudbeckia fulgida", "Echinacea purpurea", "Persicaria amplexicaulis", "Solidago", "Sanguisorba officinalis"],
    "Phlox paniculata": ["Monarda", "Leucanthemum", "Veronicastrum virginicum", "Achillea millefolium", "Centranthus ruber"],
    "Monarda": ["Echinacea purpurea", "Phlox paniculata", "Helenium autumnale", "Veronicastrum virginicum", "Persicaria amplexicaulis"],
    "Agastache": ["Salvia nemorosa", "Stachys byzantina", "Nepeta faassenii", "Echinacea purpurea", "Knautia macedonica"],
    "Kniphofia": ["Crocosmia", "Hemerocallis", "Achillea filipendulina", "Stipa", "Helenium autumnale"],
    "Solidago": ["Aster novae-angliae", "Helenium autumnale", "Echinacea purpurea", "Sanguisorba officinalis", "Pennisetum alopecuroides"],
    "Salvia nemorosa": ["Stachys byzantina", "Nepeta faassenii", "Allium", "Achillea millefolium", "Agastache"],
    "Achillea millefolium": ["Salvia nemorosa", "Nepeta faassenii", "Centranthus ruber", "Knautia macedonica", "Eryngium planum"],
    "Nepeta faassenii": ["Salvia nemorosa", "Stachys byzantina", "Allium", "Agastache", "Achillea millefolium"],
    "Paeonia lactiflora": ["Allium", "Iris germanica", "Geranium 'Johnson's Blue'", "Aquilegia vulgaris", "Baptisia australis"],
    "Paeonia officinalis": ["Allium", "Iris germanica", "Geranium 'Johnson's Blue'", "Baptisia australis", "Aquilegia vulgaris"],
    "Paeonia suffruticosa": ["Allium", "Iris germanica", "Geranium phaeum", "Baptisia australis", "Aquilegia vulgaris"],
    "Persicaria amplexicaulis": ["Pennisetum alopecuroides", "Helenium autumnale", "Veronicastrum virginicum", "Rudbeckia fulgida", "Sanguisorba officinalis"],
    "Perovskia atriplicifolia": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Eryngium planum", "Achillea filipendulina"],
    "Campanula persicifolia": ["Aquilegia vulgaris", "Geranium 'Johnson's Blue'", "Salvia nemorosa", "Lychnis", "Iris germanica"],
    "Campanula carpatica": ["Thymus serpyllum", "Geranium cantabrigiense", "Potentilla", "Prunella grandiflora", "Stachys byzantina"],
    "Campanula garganica": ["Thymus serpyllum", "Saxifraga", "Cerastium tomentosum", "Aubrieta", "Acaena"],
    "Campanula glomerata": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Aquilegia vulgaris", "Knautia macedonica", "Achillea millefolium"],
    "Campanula lactiflora": ["Geranium pratense", "Achillea millefolium", "Thalictrum aquilegiifolium", "Aquilegia vulgaris", "Veronicastrum virginicum"],
    "Campanula latifolia": ["Geranium phaeum", "Thalictrum aquilegiifolium", "Actaea simplex", "Digitalis purpurea", "Aruncus dioicus"],
    "Campanula latiloba": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Iris sibirica", "Aquilegia vulgaris", "Thalictrum aquilegiifolium"],
    "Campanula portenschlagiana": ["Thymus serpyllum", "Aubrieta", "Arabis", "Saxifraga", "Geranium cantabrigiense"],
    "Campanula poscharskyana": ["Geranium cantabrigiense", "Thymus serpyllum", "Stachys byzantina", "Potentilla", "Aubrieta"],
    "Campanula rapunculoides": ["Geranium pratense", "Salvia nemorosa", "Achillea millefolium", "Knautia macedonica", "Digitalis purpurea"],
    "Campanula 'Pink Octopus'": ["Geranium 'Rozanne'", "Nepeta faassenii", "Potentilla", "Gaillardia × grandiflora", "Knautia macedonica"],
    "Campanula 'Sarastro'": ["Iris sibirica", "Thalictrum aquilegiifolium", "Geranium 'Johnson's Blue'", "Salvia nemorosa", "Achillea millefolium"],
    "Knautia macedonica": ["Salvia nemorosa", "Agastache", "Stachys byzantina", "Centranthus ruber", "Eryngium planum"],
    "Geranium sanguineum": ["Salvia nemorosa", "Nepeta faassenii", "Stachys byzantina", "Achillea millefolium", "Thymus serpyllum"],
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
