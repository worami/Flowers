#!/usr/bin/env python3
"""KM3: Kenmerken invoegen voor entries 102–152 (Geranium 'Rozanne' t/m Iris ensata)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

KENMERKEN = {
    "Geranium 'Rozanne'":        {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium sylvaticum":       {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium versicolor":       {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium wlassovianum":     {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium hybride":          {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Alchemilla mollis":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Actaea simplex":            {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Actaea pachypoda":          {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Actaea 'Queen of Sheba'":   {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Cimicifuga japonica":       {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Cimicifuga racemosa":       {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Cimicifuga ramosa":         {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Aruncus dioicus":           {"plantafstand":"90–150 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Astilbe":                   {"plantafstand":"30–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Brunnera macrophylla":      {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Hosta":                     {"plantafstand":"30–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Lamium maculatum":          {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Pulmonaria":                {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Polygonatum multiflorum":   {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"nee"},
    "Tiarella cordifolia":       {"plantafstand":"25–35 cm","grondtype":"vochtig","zuurgraad":"zuurminnend","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Rodgersia pinnata":         {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Rodgersia aesculifolia":    {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Rodgersia henrici":         {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Rodgersia podophylla":      {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Rodgersia sambucifolia":    {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Dryopteris filix-mas":      {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Pachysandra terminalis":    {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Convallaria majalis":       {"plantafstand":"15–20 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":True,"insectvriendelijk":"nee"},
    "Lamprocapnos spectabilis":  {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Helleborus":                {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Waldsteinia ternata":       {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Calamagrostis acutiflora":  {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Hakonechloa macra":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Miscanthus sinensis":       {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Molinia":                   {"plantafstand":"45–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Panicum virgatum":          {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Pennisetum alopecuroides":  {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Stipa":                     {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Anemone nemorosa":          {"plantafstand":"10–15 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Carex":                     {"plantafstand":"30–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Aster novae-angliae":       {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Bergenia":                  {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Crocosmia":                 {"plantafstand":"10–15 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geum":                      {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Leucanthemum":              {"plantafstand":"30–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Delphinium":                {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Heuchera":                  {"plantafstand":"25–35 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Iris sibirica":             {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Iris germanica":            {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Iris pumila":               {"plantafstand":"15–20 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Iris ensata":               {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
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
