#!/usr/bin/env python3
"""CP3: Combinatieplanten voor Geranium magnificum t/m Geranium Rozanne (34 entries)."""

import os
import re
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

COMBINATIES = {
    "Geranium × magnificum": ["Alchemilla mollis", "Salvia nemorosa", "Aquilegia vulgaris", "Iris germanica", "Stachys byzantina"],
    "Tradescantia × andersoniana": ["Geranium 'Johnson's Blue'", "Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Achillea millefolium"],
    "Trollius europaeus": ["Iris sibirica", "Caltha palustris", "Filipendula", "Lysimachia nummularia", "Primula"],
    "Thalictrum aquilegiifolium": ["Astrantia major", "Geranium phaeum", "Digitalis purpurea", "Actaea simplex", "Alchemilla mollis"],
    "Lysimachia punctata": ["Ligularia dentata", "Lythrum salicaria", "Filipendula", "Iris pseudacorus", "Eupatorium maculatum"],
    "Lysimachia atropurpurea": ["Salvia nemorosa", "Stachys byzantina", "Nepeta faassenii", "Knautia macedonica", "Centranthus ruber"],
    "Lysimachia barystachys": ["Lythrum salicaria", "Filipendula", "Lysimachia clethroides", "Persicaria amplexicaulis", "Eupatorium maculatum"],
    "Lysimachia ciliata": ["Ligularia dentata", "Lythrum salicaria", "Eupatorium maculatum", "Filipendula", "Lobelia cardinalis"],
    "Lysimachia clethroides": ["Lythrum salicaria", "Persicaria amplexicaulis", "Ligularia dentata", "Filipendula", "Eupatorium maculatum"],
    "Lysimachia ephemerum": ["Salvia nemorosa", "Perovskia atriplicifolia", "Stachys byzantina", "Euphorbia", "Centranthus ruber"],
    "Lysimachia nummularia": ["Primula", "Myosotis palustris", "Caltha palustris", "Trollius europaeus", "Cardamine"],
    "Cirsium rivulare": ["Sanguisorba officinalis", "Filipendula", "Persicaria amplexicaulis", "Lythrum salicaria", "Eupatorium maculatum"],
    "Ligularia dentata": ["Rodgersia pinnata", "Filipendula", "Lythrum salicaria", "Iris pseudacorus", "Eupatorium maculatum"],
    "Digitalis purpurea": ["Geranium phaeum", "Astrantia major", "Alchemilla mollis", "Aquilegia vulgaris", "Thalictrum aquilegiifolium"],
    "Digitalis ferruginea": ["Salvia nemorosa", "Centranthus ruber", "Achillea millefolium", "Stachys byzantina", "Eryngium planum"],
    "Digitalis lutea": ["Geranium phaeum", "Astrantia major", "Thalictrum aquilegiifolium", "Alchemilla mollis", "Digitalis purpurea"],
    "Digitalis mertonensis": ["Geranium × magnificum", "Astrantia major", "Alchemilla mollis", "Aquilegia vulgaris", "Salvia nemorosa"],
    "Digitalis parviflora": ["Salvia nemorosa", "Centranthus ruber", "Stachys byzantina", "Eryngium planum", "Achillea millefolium"],
    "Lobelia cardinalis": ["Ligularia dentata", "Lythrum salicaria", "Eupatorium maculatum", "Iris pseudacorus", "Persicaria amplexicaulis"],
    "Lobelia gerardii": ["Eupatorium maculatum", "Persicaria amplexicaulis", "Lythrum salicaria", "Veronicastrum virginicum", "Filipendula"],
    "Lobelia siphilitica": ["Eupatorium maculatum", "Lythrum salicaria", "Lobelia cardinalis", "Iris pseudacorus", "Persicaria amplexicaulis"],
    "Lobelia × speciosa": ["Eupatorium maculatum", "Persicaria amplexicaulis", "Lythrum salicaria", "Filipendula", "Ligularia dentata"],
    "Lobelia tania": ["Eupatorium maculatum", "Lythrum salicaria", "Persicaria amplexicaulis", "Ligularia dentata", "Filipendula"],
    "Geranium phaeum": ["Digitalis purpurea", "Alchemilla mollis", "Astrantia major", "Thalictrum aquilegiifolium", "Actaea simplex"],
    "Geranium endressii": ["Alchemilla mollis", "Astrantia major", "Geranium 'Rozanne'", "Salvia nemorosa", "Aquilegia vulgaris"],
    "Geranium himalayense": ["Salvia nemorosa", "Aquilegia vulgaris", "Geranium 'Johnson's Blue'", "Alchemilla mollis", "Stachys byzantina"],
    "Geranium 'Johnson's Blue'": ["Salvia nemorosa", "Aquilegia vulgaris", "Alchemilla mollis", "Baptisia australis", "Stachys byzantina"],
    "Geranium nodosum": ["Digitalis purpurea", "Alchemilla mollis", "Geranium phaeum", "Astrantia major", "Pulmonaria"],
    "Geranium oxonianum": ["Alchemilla mollis", "Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Aquilegia vulgaris"],
    "Geranium pratense": ["Thalictrum aquilegiifolium", "Aquilegia vulgaris", "Alchemilla mollis", "Campanula lactiflora", "Astrantia major"],
    "Geranium psilostemon": ["Alchemilla mollis", "Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Aquilegia vulgaris"],
    "Geranium renardii": ["Salvia nemorosa", "Stachys byzantina", "Festuca glauca", "Nepeta faassenii", "Thymus serpyllum"],
    "Geranium × riversleaianum": ["Geranium 'Rozanne'", "Centranthus ruber", "Knautia macedonica", "Stachys byzantina", "Sedum"],
    "Geranium 'Rozanne'": ["Salvia nemorosa", "Stachys byzantina", "Centranthus ruber", "Knautia macedonica", "Nepeta faassenii"],
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
