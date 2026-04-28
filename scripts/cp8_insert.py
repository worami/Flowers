#!/usr/bin/env python3
"""CP8: Combinatieplanten voor Aurinia saxatile t/m Meconopsis cambrica (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Aurinia saxatile": ["Aubrieta", "Arabis", "Pulsatilla vulgaris", "Thymus serpyllum", "Dianthus"],
    "Cerastium tomentosum": ["Thymus serpyllum", "Stachys byzantina", "Sempervivum", "Aubrieta", "Festuca glauca"],
    "Leptinella squalida": ["Thymus serpyllum", "Sagina subulata", "Mazus reptans", "Acaena", "Arenaria montana"],
    "Mazus reptans": ["Thymus serpyllum", "Sagina subulata", "Leptinella squalida", "Arabis", "Aubrieta"],
    "Sagina subulata": ["Thymus serpyllum", "Mazus reptans", "Leptinella squalida", "Arenaria montana", "Sempervivum"],
    "Elymus magellanicus": ["Festuca glauca", "Helictotrichon sempervirens", "Stachys byzantina", "Salvia nemorosa", "Echinops ritro"],
    "Eragrostis spectabilis": ["Salvia nemorosa", "Stipa", "Verbena bonariensis", "Pennisetum alopecuroides", "Knautia macedonica"],
    "Koeleria glauca": ["Festuca glauca", "Stachys byzantina", "Dianthus", "Thymus serpyllum", "Salvia nemorosa"],
    "Leymus arenarius": ["Helictotrichon sempervirens", "Festuca glauca", "Echinops ritro", "Eryngium planum", "Stachys byzantina"],
    "Melica": ["Deschampsia", "Astrantia major", "Geranium phaeum", "Carex", "Hosta"],
    "Muehlenbergia capillaris": ["Pennisetum alopecuroides", "Stipa", "Verbena bonariensis", "Sesleria", "Echinacea purpurea"],
    "Sesleria": ["Deschampsia", "Carex", "Molinia", "Astrantia major", "Pulmonaria"],
    "Spodiopogon sibiricus": ["Miscanthus sinensis", "Molinia", "Persicaria amplexicaulis", "Sanguisorba officinalis", "Helenium autumnale"],
    "Cortaderia selloana": ["Miscanthus sinensis", "Pennisetum alopecuroides", "Echinacea purpurea", "Rudbeckia fulgida", "Verbena bonariensis"],
    "Berkheya purpurea": ["Echinops ritro", "Eryngium planum", "Stachys byzantina", "Salvia nemorosa", "Verbascum"],
    "Deinanthe": ["Hosta", "Astilbe", "Rodgersia pinnata", "Actaea simplex", "Dryopteris filix-mas"],
    "Melittis melissophyllum": ["Geranium phaeum", "Digitalis purpurea", "Alchemilla mollis", "Astrantia major", "Pulmonaria"],
    "Parthenium integrifolium": ["Echinacea purpurea", "Rudbeckia fulgida", "Sanguisorba officinalis", "Penstemon", "Salvia nemorosa"],
    "Peltoboykinia watanabei": ["Rodgersia aesculifolia", "Hosta", "Astilbe", "Ligularia dentata", "Dryopteris filix-mas"],
    "Saruma henryi": ["Asarum", "Hosta", "Brunnera macrophylla", "Pulmonaria", "Actaea pachypoda"],
    "Serratula seoanei": ["Sanguisorba officinalis", "Salvia nemorosa", "Knautia macedonica", "Stachys byzantina", "Penstemon"],
    "Smilacina racemosa": ["Polygonatum multiflorum", "Hosta", "Brunnera macrophylla", "Actaea pachypoda", "Dryopteris filix-mas"],
    "Stylophorum diphyllum": ["Hosta", "Brunnera macrophylla", "Pulmonaria", "Digitalis purpurea", "Actaea pachypoda"],
    "Tulbaghia violacea": ["Salvia nemorosa", "Stachys byzantina", "Agapanthus", "Euphorbia", "Achillea millefolium"],
    "Mitella": ["Hosta", "Tiarella cordifolia", "Brunnera macrophylla", "Pulmonaria", "Asarum"],
    "Mukdenia rossii": ["Hosta", "Bergenia", "Brunnera macrophylla", "Heuchera", "Pulmonaria"],
    "Phuopsis stylosa": ["Thymus serpyllum", "Stachys byzantina", "Geranium sanguineum", "Centranthus ruber", "Salvia nemorosa"],
    "Phyteuma scheuchzeri": ["Thymus serpyllum", "Dianthus", "Primula", "Saxifraga", "Campanula carpatica"],
    "Ranunculus": ["Caltha palustris", "Trollius europaeus", "Primula", "Lysimachia nummularia", "Myosotis palustris"],
    "Chrysanthemum": ["Aster novae-angliae", "Helenium autumnale", "Rudbeckia fulgida", "Solidago", "Persicaria amplexicaulis"],
    "Leontopodium alpinum": ["Thymus serpyllum", "Dianthus", "Sempervivum", "Saxifraga", "Pulsatilla vulgaris"],
    "Lewisia cotyledon": ["Sempervivum", "Sedum", "Dianthus", "Saxifraga", "Thymus serpyllum"],
    "Linaria purpurea": ["Salvia nemorosa", "Centranthus ruber", "Knautia macedonica", "Verbena bonariensis", "Stachys byzantina"],
    "Meconopsis cambrica": ["Brunnera macrophylla", "Pulmonaria", "Digitalis purpurea", "Aquilegia vulgaris", "Geranium phaeum"],
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
