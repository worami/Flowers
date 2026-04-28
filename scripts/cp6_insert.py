#!/usr/bin/env python3
"""CP6: Combinatieplanten voor Saxifraga t/m Cosmos atrosanguineus (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Saxifraga": ["Thymus serpyllum", "Arabis", "Aubrieta", "Sempervivum", "Dianthus"],
    "Tricyrtis": ["Anemone hupehensis", "Actaea simplex", "Hosta", "Brunnera macrophylla", "Dryopteris filix-mas"],
    "Verbascum": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Eryngium planum", "Centranthus ruber"],
    "Sedum": ["Thymus serpyllum", "Sempervivum", "Festuca glauca", "Stachys byzantina", "Delosperma"],
    "Sempervivum": ["Sedum", "Thymus serpyllum", "Saxifraga", "Dianthus", "Festuca glauca"],
    "Gypsophila": ["Salvia nemorosa", "Achillea millefolium", "Lychnis", "Stachys byzantina", "Centranthus ruber"],
    "Lychnis": ["Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Aquilegia vulgaris", "Achillea millefolium"],
    "Liriope muscari": ["Hosta", "Hakonechloa macra", "Ophiopogon planiscapus", "Brunnera macrophylla", "Helleborus"],
    "Amsonia": ["Iris sibirica", "Baptisia australis", "Salvia nemorosa", "Geranium 'Johnson's Blue'", "Achillea millefolium"],
    "Astilboides tabularis": ["Rodgersia aesculifolia", "Hosta", "Ligularia dentata", "Dryopteris filix-mas", "Aruncus dioicus"],
    "Caltha palustris": ["Iris pseudacorus", "Trollius europaeus", "Lysimachia nummularia", "Myosotis palustris", "Filipendula"],
    "Crambe cordifolia": ["Echinops ritro", "Eryngium planum", "Salvia nemorosa", "Stachys byzantina", "Achillea filipendulina"],
    "Darmera peltata": ["Rodgersia aesculifolia", "Ligularia dentata", "Caltha palustris", "Lythrum salicaria", "Iris pseudacorus"],
    "Anthemis": ["Salvia nemorosa", "Stachys byzantina", "Achillea millefolium", "Centranthus ruber", "Eryngium planum"],
    "Armeria": ["Dianthus", "Thymus serpyllum", "Festuca glauca", "Sempervivum", "Stachys byzantina"],
    "Acanthus": ["Salvia nemorosa", "Echinops ritro", "Stachys byzantina", "Eryngium planum", "Verbascum"],
    "Catananche": ["Salvia nemorosa", "Knautia macedonica", "Centranthus ruber", "Stachys byzantina", "Scabiosa columbaria"],
    "Cephalaria": ["Thalictrum aquilegiifolium", "Salvia nemorosa", "Verbena bonariensis", "Stachys byzantina", "Achillea millefolium"],
    "Gentiana": ["Primula", "Thymus serpyllum", "Pulsatilla vulgaris", "Aubrieta", "Helianthemum"],
    "Gillenia trifoliata": ["Astrantia major", "Geranium phaeum", "Alchemilla mollis", "Digitalis purpurea", "Thalictrum aquilegiifolium"],
    "Hepatica": ["Primula", "Pulmonaria", "Anemone nemorosa", "Brunnera macrophylla", "Epimedium"],
    "Inula": ["Rudbeckia fulgida", "Helenium autumnale", "Echinacea purpurea", "Ligularia dentata", "Sanguisorba officinalis"],
    "Kirengeshoma palmata": ["Hosta", "Astilbe", "Actaea simplex", "Rodgersia pinnata", "Dryopteris filix-mas"],
    "Sidalcea": ["Salvia nemorosa", "Monarda", "Achillea millefolium", "Centranthus ruber", "Stachys byzantina"],
    "Silphium": ["Echinacea purpurea", "Rudbeckia fulgida", "Helenium autumnale", "Sanguisorba officinalis", "Persicaria amplexicaulis"],
    "Stokesia laevis": ["Echinacea purpurea", "Salvia nemorosa", "Achillea millefolium", "Helenium autumnale", "Penstemon"],
    "Symphytum": ["Brunnera macrophylla", "Pulmonaria", "Hosta", "Aruncus dioicus", "Alchemilla mollis"],
    "Tellima grandiflora": ["Brunnera macrophylla", "Pulmonaria", "Helleborus", "Epimedium", "Tiarella cordifolia"],
    "Anemonella thalictroides": ["Hepatica", "Primula", "Epimedium", "Pulmonaria", "Anemone nemorosa"],
    "Arisaema": ["Hosta", "Polygonatum multiflorum", "Dryopteris filix-mas", "Trillium", "Actaea pachypoda"],
    "Trillium": ["Polygonatum multiflorum", "Hosta", "Arisaema", "Actaea pachypoda", "Dryopteris filix-mas"],
    "Uvularia grandiflora": ["Polygonatum multiflorum", "Trillium", "Brunnera macrophylla", "Actaea pachypoda", "Hosta"],
    "Jeffersonia": ["Hepatica", "Primula", "Anemone nemorosa", "Pulmonaria", "Epimedium"],
    "Cosmos atrosanguineus": ["Salvia nemorosa", "Stachys byzantina", "Penstemon", "Centranthus ruber", "Knautia macedonica"],
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
