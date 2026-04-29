#!/usr/bin/env python3
"""KM2: Kenmerken invoegen voor entries 52–101 (Hylotelephium t/m Geranium oxonianum)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

KENMERKEN = {
    "Hylotelephium spectabile":     {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Eryngium planum":              {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Centranthus ruber":            {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Sanguisorba officinalis":      {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Oenothera lindheimeri":        {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Oenothera fruticosa":          {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Oenothera missouriensis":      {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Oenothera speciosa":           {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Erigeron speciosus":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Calamintha nepeta":            {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Phlomis russeliana":           {"plantafstand":"60–90 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Aconitum carmichaelii":        {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Anemone hupehensis":           {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Aquilegia vulgaris":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Astrantia major":              {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Chelone obliqua":              {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Eupatorium maculatum":         {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Geranium × magnificum":        {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Tradescantia × andersoniana":  {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Trollius europaeus":           {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Thalictrum aquilegiifolium":   {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia punctata":          {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia atropurpurea":      {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia barystachys":       {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia ciliata":           {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia clethroides":       {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia ephemerum":         {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lysimachia nummularia":        {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Cirsium rivulare":             {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Ligularia dentata":            {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Digitalis purpurea":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Digitalis ferruginea":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Digitalis lutea":              {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Digitalis mertonensis":        {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Digitalis parviflora":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Lobelia cardinalis":           {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lobelia gerardii":             {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lobelia siphilitica":          {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lobelia × speciosa":           {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lobelia tania":                {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium phaeum":              {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium endressii":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium himalayense":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium 'Johnson's Blue'":    {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium nodosum":             {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium oxonianum":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium pratense":            {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium psilostemon":         {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium renardii":            {"plantafstand":"20–30 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium × riversleaianum":    {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
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
