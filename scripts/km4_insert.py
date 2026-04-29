#!/usr/bin/env python3
"""KM4: Kenmerken invoegen voor entries 153–203 (Iris foetidissima t/m Cosmos atrosanguineus)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

KENMERKEN = {
    "Iris foetidissima":         {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Iris pallida":              {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Iris pseudacorus":          {"plantafstand":"30–45 cm","grondtype":"nat","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Iris reticulata":           {"plantafstand":"10–15 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Liatris spicata":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Lupinus":                   {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"zuurminnend","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Agapanthus":                {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":False,"giftig":False,"insectvriendelijk":"bijen"},
    "Centaurea montana":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Dianthus":                  {"plantafstand":"15–30 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Papaver orientale":         {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Pulsatilla vulgaris":       {"plantafstand":"15–25 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Euphorbia":                 {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Helianthus":                {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Heliopsis helianthoides":   {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Primula":                   {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Veronica":                  {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Platycodon grandiflorus":   {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Polemonium caeruleum":      {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Saxifraga":                 {"plantafstand":"15–25 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Tricyrtis":                 {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Verbascum":                 {"plantafstand":"30–60 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Sedum":                     {"plantafstand":"20–40 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Sempervivum":               {"plantafstand":"10–20 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Gypsophila":                {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Lychnis":                   {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Liriope muscari":           {"plantafstand":"25–35 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Amsonia":                   {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Astilboides tabularis":     {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Caltha palustris":          {"plantafstand":"30–45 cm","grondtype":"nat","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Crambe cordifolia":         {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Darmera peltata":           {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Anthemis":                  {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Armeria":                   {"plantafstand":"15–25 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Acanthus":                  {"plantafstand":"90–120 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Catananche":                {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Cephalaria":                {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Gentiana":                  {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"zuurminnend","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Gillenia trifoliata":       {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Hepatica":                  {"plantafstand":"10–15 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Inula":                     {"plantafstand":"60–120 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Kirengeshoma palmata":      {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"zuurminnend","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Sidalcea":                  {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Silphium":                  {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Stokesia laevis":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Symphytum":                 {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Tellima grandiflora":       {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Anemonella thalictroides":  {"plantafstand":"10–15 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Arisaema":                  {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"nee"},
    "Trillium":                  {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"zuurminnend","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Uvularia grandiflora":      {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Jeffersonia":               {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Cosmos atrosanguineus":     {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":False,"giftig":False,"insectvriendelijk":"beide"},
}


def build_km_str(km):
    parts = []
    for k, v in km.items():
        if isinstance(v, bool):
            parts.append(f'{k}:{str(v).lower()}')
        else:
            parts.append(f'{k}:"{v}"')
    return "{" + ",".join(parts) + "}"


def insert_kenmerken(content, latin_name, km):
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

    if 'kenmerken' in content[idx:cv_idx]:
        print(f"  AL AANWEZIG (overgeslagen): {latin_name}")
        return content, False

    km_str = f', kenmerken:{build_km_str(km)}'
    new_content = content[:cv_idx] + km_str + content[cv_idx:]
    print(f"  OK: {latin_name}")
    return new_content, True


def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = 0
    for latin_name, km in KENMERKEN.items():
        content, changed = insert_kenmerken(content, latin_name, km)
        if changed:
            updated += 1

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nKlaar. {updated}/{len(KENMERKEN)} entries bijgewerkt.")


if __name__ == '__main__':
    main()
