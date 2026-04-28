#!/usr/bin/env python3
"""CP7: Combinatieplanten voor Dierama t/m Arenaria montana (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Dierama": ["Stipa", "Hemerocallis", "Crocosmia", "Kniphofia", "Pennisetum alopecuroides"],
    "Disporum": ["Polygonatum multiflorum", "Hosta", "Brunnera macrophylla", "Dryopteris filix-mas", "Actaea pachypoda"],
    "Dodecatheon": ["Primula", "Hepatica", "Pulmonaria", "Anemone nemorosa", "Brunnera macrophylla"],
    "Isotoma axillaris": ["Verbena bonariensis", "Salvia nemorosa", "Lobelia cardinalis", "Penstemon", "Centranthus ruber"],
    "Briza": ["Stipa", "Festuca glauca", "Salvia nemorosa", "Centranthus ruber", "Stachys byzantina"],
    "Deschampsia": ["Sanguisorba officinalis", "Astrantia major", "Geranium phaeum", "Molinia", "Hosta"],
    "Helictotrichon sempervirens": ["Stachys byzantina", "Salvia nemorosa", "Festuca glauca", "Echinops ritro", "Perovskia atriplicifolia"],
    "Luzula": ["Hosta", "Dryopteris filix-mas", "Brunnera macrophylla", "Carex", "Helleborus"],
    "Milium effusum": ["Hosta", "Brunnera macrophylla", "Galium odoratum", "Polygonatum multiflorum", "Carex"],
    "Anemanthele lessoniana": ["Stipa", "Hemerocallis", "Echinacea purpurea", "Rudbeckia fulgida", "Salvia nemorosa"],
    "Chasmanthium latifolium": ["Hosta", "Carex", "Dryopteris filix-mas", "Hakonechloa macra", "Astilbe"],
    "Imperata cylindrica": ["Stachys byzantina", "Festuca glauca", "Salvia nemorosa", "Pennisetum alopecuroides", "Carex"],
    "Schizachyrium scoparium": ["Echinacea purpurea", "Salvia nemorosa", "Pennisetum alopecuroides", "Sorghastrum nutans", "Sporobolus heterolepis"],
    "Sorghastrum nutans": ["Echinacea purpurea", "Rudbeckia fulgida", "Schizachyrium scoparium", "Sporobolus heterolepis", "Sanguisorba officinalis"],
    "Sporobolus heterolepis": ["Echinacea purpurea", "Salvia nemorosa", "Schizachyrium scoparium", "Sorghastrum nutans", "Rudbeckia fulgida"],
    "Acaena": ["Thymus serpyllum", "Festuca glauca", "Sempervivum", "Sedum", "Stachys byzantina"],
    "Arabis": ["Aubrieta", "Thymus serpyllum", "Pulsatilla vulgaris", "Primula", "Saxifraga"],
    "Asarum": ["Hosta", "Polygonatum multiflorum", "Brunnera macrophylla", "Helleborus", "Galium odoratum"],
    "Aubrieta": ["Arabis", "Thymus serpyllum", "Pulsatilla vulgaris", "Aurinia saxatile", "Primula"],
    "Chiastophyllum oppositifolium": ["Saxifraga", "Sempervivum", "Sedum", "Thymus serpyllum", "Armeria"],
    "Galium odoratum": ["Hosta", "Brunnera macrophylla", "Helleborus", "Convallaria majalis", "Polygonatum multiflorum"],
    "Houttuynia cordata": ["Lysimachia nummularia", "Carex", "Myosotis palustris", "Iris pseudacorus", "Caltha palustris"],
    "Adiantum pedatum": ["Hosta", "Polygonatum multiflorum", "Astilbe", "Brunnera macrophylla", "Actaea pachypoda"],
    "Athyrium": ["Hosta", "Brunnera macrophylla", "Astilbe", "Dryopteris filix-mas", "Polygonatum multiflorum"],
    "Blechnum spicant": ["Dryopteris filix-mas", "Polystichum", "Hosta", "Brunnera macrophylla", "Helleborus"],
    "Matteuccia struthiopteris": ["Hosta", "Astilbe", "Rodgersia pinnata", "Ligularia dentata", "Dryopteris filix-mas"],
    "Osmunda regalis": ["Matteuccia struthiopteris", "Ligularia dentata", "Rodgersia aesculifolia", "Iris pseudacorus", "Caltha palustris"],
    "Polystichum": ["Helleborus", "Epimedium", "Brunnera macrophylla", "Hosta", "Galium odoratum"],
    "Asplenium trichomanes": ["Saxifraga", "Sempervivum", "Thymus serpyllum", "Festuca glauca", "Arabis"],
    "Cyrtomium": ["Helleborus", "Polystichum", "Epimedium", "Brunnera macrophylla", "Hosta"],
    "Onoclea sensibilis": ["Matteuccia struthiopteris", "Osmunda regalis", "Hosta", "Carex", "Iris pseudacorus"],
    "Phyllitis scolopendrium": ["Polystichum", "Dryopteris filix-mas", "Helleborus", "Epimedium", "Hosta"],
    "Arctostaphylos uva-ursi": ["Epimedium", "Helleborus", "Waldsteinia ternata", "Galium odoratum", "Pachysandra terminalis"],
    "Arenaria montana": ["Thymus serpyllum", "Arabis", "Sempervivum", "Festuca glauca", "Dianthus"],
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
