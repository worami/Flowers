#!/usr/bin/env python3
"""CP2: Combinatieplanten voor Ceratostigma t/m Eupatorium maculatum (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Ceratostigma plumbaginoides": ["Hylotelephium spectabile", "Stachys byzantina", "Hemerocallis", "Geranium cantabrigiense", "Sesleria"],
    "Scabiosa columbaria": ["Knautia macedonica", "Salvia nemorosa", "Centranthus ruber", "Stachys byzantina", "Geranium sanguineum"],
    "Festuca glauca": ["Stachys byzantina", "Salvia nemorosa", "Erigeron speciosus", "Dianthus", "Thymus serpyllum"],
    "Stachys byzantina": ["Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Perovskia atriplicifolia", "Achillea millefolium"],
    "Geranium macrorrhizum": ["Helleborus", "Lamium maculatum", "Pulmonaria", "Brunnera macrophylla", "Epimedium"],
    "Geranium cantabrigiense": ["Helleborus", "Stachys byzantina", "Ceratostigma plumbaginoides", "Pulmonaria", "Alchemilla mollis"],
    "Ajuga reptans": ["Lamium maculatum", "Pulmonaria", "Geranium macrorrhizum", "Brunnera macrophylla", "Primula"],
    "Prunella grandiflora": ["Thymus serpyllum", "Potentilla", "Geranium sanguineum", "Knautia macedonica", "Stachys byzantina"],
    "Thymus serpyllum": ["Cerastium tomentosum", "Stachys byzantina", "Dianthus", "Festuca glauca", "Arabis"],
    "Potentilla": ["Salvia nemorosa", "Knautia macedonica", "Prunella grandiflora", "Geranium sanguineum", "Thymus serpyllum"],
    "Achillea filipendulina": ["Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Perovskia atriplicifolia", "Verbena bonariensis"],
    "Allium": ["Salvia nemorosa", "Stachys byzantina", "Nepeta faassenii", "Iris germanica", "Paeonia lactiflora"],
    "Veronicastrum virginicum": ["Phlox paniculata", "Monarda", "Helenium autumnale", "Persicaria amplexicaulis", "Echinacea purpurea"],
    "Verbena bonariensis": ["Pennisetum alopecuroides", "Stipa", "Panicum virgatum", "Echinacea purpurea", "Knautia macedonica"],
    "Penstemon": ["Salvia nemorosa", "Agastache", "Knautia macedonica", "Hemerocallis", "Gaillardia × grandiflora"],
    "Gaillardia × grandiflora": ["Rudbeckia fulgida", "Hemerocallis", "Achillea filipendulina", "Echinacea purpurea", "Coreopsis verticillata"],
    "Coreopsis verticillata": ["Salvia nemorosa", "Knautia macedonica", "Gaillardia × grandiflora", "Stachys byzantina", "Stipa"],
    "Hylotelephium spectabile": ["Helenium autumnale", "Rudbeckia fulgida", "Echinacea purpurea", "Ceratostigma plumbaginoides", "Aster novae-angliae"],
    "Eryngium planum": ["Echinops ritro", "Stachys byzantina", "Salvia nemorosa", "Achillea filipendulina", "Centranthus ruber"],
    "Centranthus ruber": ["Salvia nemorosa", "Achillea millefolium", "Knautia macedonica", "Echinops ritro", "Eryngium planum"],
    "Sanguisorba officinalis": ["Echinacea purpurea", "Helenium autumnale", "Pennisetum alopecuroides", "Persicaria amplexicaulis", "Molinia"],
    "Oenothera lindheimeri": ["Salvia nemorosa", "Stachys byzantina", "Perovskia atriplicifolia", "Penstemon", "Nepeta faassenii"],
    "Oenothera fruticosa": ["Salvia nemorosa", "Achillea millefolium", "Centranthus ruber", "Knautia macedonica", "Stachys byzantina"],
    "Oenothera missouriensis": ["Dianthus", "Thymus serpyllum", "Festuca glauca", "Stachys byzantina", "Salvia nemorosa"],
    "Oenothera speciosa": ["Salvia nemorosa", "Thymus serpyllum", "Centranthus ruber", "Stachys byzantina", "Knautia macedonica"],
    "Erigeron speciosus": ["Salvia nemorosa", "Knautia macedonica", "Stachys byzantina", "Achillea millefolium", "Centranthus ruber"],
    "Calamintha nepeta": ["Salvia nemorosa", "Stachys byzantina", "Nepeta faassenii", "Agastache", "Penstemon"],
    "Phlomis russeliana": ["Stachys byzantina", "Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Festuca glauca"],
    "Aconitum carmichaelii": ["Actaea simplex", "Anemone hupehensis", "Persicaria amplexicaulis", "Helenium autumnale", "Cimicifuga racemosa"],
    "Anemone hupehensis": ["Aconitum carmichaelii", "Actaea simplex", "Persicaria amplexicaulis", "Helenium autumnale", "Aster novae-angliae"],
    "Aquilegia vulgaris": ["Geranium 'Johnson's Blue'", "Salvia nemorosa", "Campanula persicifolia", "Baptisia australis", "Allium"],
    "Astrantia major": ["Geranium 'Johnson's Blue'", "Alchemilla mollis", "Digitalis purpurea", "Thalictrum aquilegiifolium", "Salvia nemorosa"],
    "Chelone obliqua": ["Eupatorium maculatum", "Lythrum salicaria", "Lobelia cardinalis", "Ligularia dentata", "Persicaria amplexicaulis"],
    "Eupatorium maculatum": ["Veronicastrum virginicum", "Sanguisorba officinalis", "Persicaria amplexicaulis", "Rudbeckia fulgida", "Helenium autumnale"],
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
