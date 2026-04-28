#!/usr/bin/env python3
"""CP9: Combinatieplanten voor Limonium latifolium t/m Macleaya microcarpa (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Limonium latifolium": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Centranthus ruber", "Achillea millefolium"],
    "Patrinia": ["Aster novae-angliae", "Helenium autumnale", "Actaea simplex", "Persicaria amplexicaulis", "Sanguisorba officinalis"],
    "Scutellaria incana": ["Echinacea purpurea", "Rudbeckia fulgida", "Salvia nemorosa", "Penstemon", "Sanguisorba officinalis"],
    "Seseli montanum": ["Salvia nemorosa", "Stachys byzantina", "Peucedanum verticillare", "Eryngium planum", "Verbena bonariensis"],
    "Succisa": ["Knautia macedonica", "Salvia nemorosa", "Scabiosa columbaria", "Molinia", "Deschampsia"],
    "Buphthalmum salicifolium": ["Rudbeckia fulgida", "Helenium autumnale", "Achillea millefolium", "Salvia nemorosa", "Echinacea purpurea"],
    "Cenolophium denudatum": ["Salvia nemorosa", "Verbena bonariensis", "Stachys byzantina", "Selinum", "Eryngium planum"],
    "Hylomecon japonica": ["Pulmonaria", "Brunnera macrophylla", "Epimedium", "Hepatica", "Actaea pachypoda"],
    "Ophiopogon planiscapus": ["Hosta", "Carex", "Liriope muscari", "Brunnera macrophylla", "Helleborus"],
    "Selinum": ["Salvia nemorosa", "Verbena bonariensis", "Cenolophium denudatum", "Deschampsia", "Sanguisorba officinalis"],
    "Incarvillea delavayi": ["Salvia nemorosa", "Aquilegia vulgaris", "Allium", "Geranium 'Johnson's Blue'", "Penstemon"],
    "Morina longifolia": ["Stachys byzantina", "Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Verbascum"],
    "Podophyllum": ["Hosta", "Rodgersia aesculifolia", "Dryopteris filix-mas", "Polygonatum multiflorum", "Actaea pachypoda"],
    "Trachystemon orientalis": ["Hosta", "Brunnera macrophylla", "Symphytum", "Rodgersia aesculifolia", "Aruncus dioicus"],
    "Trifolium": ["Salvia nemorosa", "Achillea millefolium", "Sanguisorba officinalis", "Knautia macedonica", "Molinia"],
    "Cardamine": ["Brunnera macrophylla", "Pulmonaria", "Anemone nemorosa", "Primula", "Galium odoratum"],
    "Lunaria rediviva": ["Digitalis purpurea", "Geranium phaeum", "Alchemilla mollis", "Brunnera macrophylla", "Astrantia major"],
    "Mertensia": ["Pulmonaria", "Brunnera macrophylla", "Anemone nemorosa", "Primula", "Hepatica"],
    "Tanacetum": ["Achillea millefolium", "Salvia nemorosa", "Leucanthemum", "Centranthus ruber", "Stachys byzantina"],
    "Thermopsis": ["Baptisia australis", "Lupinus", "Iris sibirica", "Salvia nemorosa", "Aquilegia vulgaris"],
    "Delosperma": ["Thymus serpyllum", "Sedum", "Sempervivum", "Stachys byzantina", "Festuca glauca"],
    "Erysimum": ["Salvia nemorosa", "Allium", "Aquilegia vulgaris", "Centranthus ruber", "Stachys byzantina"],
    "Linum perenne": ["Salvia nemorosa", "Stachys byzantina", "Festuca glauca", "Achillea millefolium", "Centranthus ruber"],
    "Malva": ["Salvia nemorosa", "Centranthus ruber", "Achillea millefolium", "Verbena bonariensis", "Stachys byzantina"],
    "Physalis alkekengi": ["Aster novae-angliae", "Rudbeckia fulgida", "Solidago", "Helenium autumnale", "Persicaria amplexicaulis"],
    "Anaphalis": ["Stachys byzantina", "Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Centranthus ruber"],
    "Anthericum": ["Salvia nemorosa", "Stachys byzantina", "Aquilegia vulgaris", "Geranium 'Johnson's Blue'", "Centranthus ruber"],
    "Kalimeris incisa": ["Aster novae-angliae", "Echinacea purpurea", "Salvia nemorosa", "Rudbeckia fulgida", "Penstemon"],
    "Sisyrinchium": ["Salvia nemorosa", "Stipa", "Festuca glauca", "Dianthus", "Thymus serpyllum"],
    "Telekia speciosa": ["Rudbeckia fulgida", "Helenium autumnale", "Sanguisorba officinalis", "Ligularia dentata", "Echinacea purpurea"],
    "Artemisia": ["Stachys byzantina", "Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Perovskia atriplicifolia"],
    "Asclepias": ["Echinacea purpurea", "Rudbeckia fulgida", "Monarda", "Sanguisorba officinalis", "Penstemon"],
    "Dictamnus albus": ["Salvia nemorosa", "Baptisia australis", "Paeonia lactiflora", "Iris germanica", "Allium"],
    "Macleaya microcarpa": ["Eupatorium maculatum", "Persicaria amplexicaulis", "Sanguisorba officinalis", "Aruncus dioicus", "Filipendula"],
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
