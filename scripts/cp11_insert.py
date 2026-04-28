#!/usr/bin/env python3
"""CP11: Combinatieplanten voor Hesperantha coccinea t/m Ampelopsis (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Hesperantha coccinea": ["Lythrum salicaria", "Eupatorium maculatum", "Lobelia cardinalis", "Persicaria amplexicaulis", "Sanguisorba officinalis"],
    "Hibiscus moscheutos": ["Rudbeckia fulgida", "Echinacea purpurea", "Lythrum salicaria", "Eupatorium maculatum", "Persicaria amplexicaulis"],
    "Nerine bowdenii": ["Salvia nemorosa", "Stachys byzantina", "Sedum", "Aster novae-angliae", "Persicaria amplexicaulis"],
    "Cornus canadensis": ["Hosta", "Galium odoratum", "Pulmonaria", "Brunnera macrophylla", "Helleborus"],
    "Petasites hybridus": ["Rodgersia aesculifolia", "Darmera peltata", "Iris pseudacorus", "Lysimachia nummularia", "Caltha palustris"],
    "Zantedeschia aethiopica": ["Iris pseudacorus", "Caltha palustris", "Lythrum salicaria", "Rodgersia aesculifolia", "Darmera peltata"],
    "Romneya coulteri": ["Salvia nemorosa", "Stachys byzantina", "Echinops ritro", "Eryngium planum", "Perovskia atriplicifolia"],
    "Myosotis palustris": ["Caltha palustris", "Iris pseudacorus", "Lysimachia nummularia", "Carex", "Trollius europaeus"],
    "Valeriana officinalis": ["Achillea millefolium", "Salvia nemorosa", "Iris sibirica", "Eupatorium maculatum", "Sanguisorba officinalis"],
    "Anchusa azurea": ["Salvia nemorosa", "Iris germanica", "Allium", "Aquilegia vulgaris", "Geranium 'Johnson's Blue'"],
    "Draba bruniifolia": ["Sempervivum", "Saxifraga", "Thymus serpyllum", "Dianthus", "Aubrieta"],
    "Dryas": ["Thymus serpyllum", "Saxifraga", "Sempervivum", "Dianthus", "Arabis"],
    "Arum italicum": ["Hosta", "Helleborus", "Brunnera macrophylla", "Galium odoratum", "Pulmonaria"],
    "Iberis sempervirens": ["Aubrieta", "Arabis", "Thymus serpyllum", "Dianthus", "Pulsatilla vulgaris"],
    "Hieracium aurantiacum": ["Thymus serpyllum", "Festuca glauca", "Salvia nemorosa", "Dianthus", "Stachys byzantina"],
    "Senecio": ["Stachys byzantina", "Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Verbascum"],
    "Sphaeralcea": ["Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Achillea millefolium", "Echinacea purpurea"],
    "Meehania urticifolia": ["Hosta", "Pulmonaria", "Brunnera macrophylla", "Epimedium", "Galium odoratum"],
    "Ruellia humilis": ["Salvia nemorosa", "Echinacea purpurea", "Penstemon", "Sporobolus heterolepis", "Schizachyrium scoparium"],
    "Verbesina alternifolia": ["Eupatorium maculatum", "Vernonia", "Persicaria amplexicaulis", "Rudbeckia fulgida", "Sanguisorba officinalis"],
    "Pimpinella major": ["Salvia nemorosa", "Geranium phaeum", "Alchemilla mollis", "Astrantia major", "Brunnera macrophylla"],
    "Clematis": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Alchemilla mollis", "Stachys byzantina", "Nepeta faassenii"],
    "Hedera": ["Pulmonaria", "Helleborus", "Epimedium", "Galium odoratum", "Brunnera macrophylla"],
    "Lonicera": ["Geranium 'Johnson's Blue'", "Alchemilla mollis", "Astrantia major", "Salvia nemorosa", "Nepeta faassenii"],
    "Parthenocissus": ["Hosta", "Carex", "Brunnera macrophylla", "Helleborus", "Epimedium"],
    "Wisteria": ["Allium", "Salvia nemorosa", "Geranium 'Johnson's Blue'", "Iris germanica", "Alchemilla mollis"],
    "Actinidia": ["Hosta", "Aruncus dioicus", "Rodgersia aesculifolia", "Dryopteris filix-mas", "Astilbe"],
    "Campsis": ["Salvia nemorosa", "Echinops ritro", "Eryngium planum", "Stachys byzantina", "Perovskia atriplicifolia"],
    "Hydrangea anomala petiolaris": ["Hosta", "Brunnera macrophylla", "Helleborus", "Galium odoratum", "Epimedium"],
    "Passiflora": ["Salvia nemorosa", "Centranthus ruber", "Stachys byzantina", "Verbena bonariensis", "Verbascum"],
    "Schizophragma hydrangeoides": ["Hosta", "Brunnera macrophylla", "Astilbe", "Helleborus", "Dryopteris filix-mas"],
    "Trachelospermum jasminoides": ["Salvia nemorosa", "Geranium 'Johnson's Blue'", "Nepeta faassenii", "Stachys byzantina", "Centranthus ruber"],
    "Akebia quinata": ["Hosta", "Brunnera macrophylla", "Epimedium", "Helleborus", "Galium odoratum"],
    "Ampelopsis": ["Hosta", "Carex", "Helleborus", "Brunnera macrophylla", "Epimedium"],
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
