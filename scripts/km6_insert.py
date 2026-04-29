#!/usr/bin/env python3
"""KM6: Kenmerken invoegen voor entries 254–304 (Deinanthe t/m Dictamnus albus)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

KENMERKEN = {
    "Deinanthe":                  {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Melittis melissophyllum":    {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Parthenium integrifolium":   {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Peltoboykinia watanabei":    {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Saruma henryi":              {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Serratula seoanei":          {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Smilacina racemosa":         {"plantafstand":"45–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Stylophorum diphyllum":      {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Tulbaghia violacea":         {"plantafstand":"25–35 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":False,"giftig":False,"insectvriendelijk":"bijen"},
    "Mitella":                    {"plantafstand":"15–20 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Mukdenia rossii":            {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Phuopsis stylosa":           {"plantafstand":"20–30 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Phyteuma scheuchzeri":       {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Ranunculus":                 {"plantafstand":"20–40 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Chrysanthemum":              {"plantafstand":"30–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Leontopodium alpinum":       {"plantafstand":"15–20 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lewisia cotyledon":          {"plantafstand":"15–20 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":False,"giftig":False,"insectvriendelijk":"bijen"},
    "Linaria purpurea":           {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Meconopsis cambrica":        {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Limonium latifolium":        {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Patrinia":                   {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Scutellaria incana":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Seseli montanum":            {"plantafstand":"30–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Succisa":                    {"plantafstand":"30–60 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Buphthalmum salicifolium":   {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Cenolophium denudatum":      {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Hylomecon japonica":         {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Ophiopogon planiscapus":     {"plantafstand":"15–25 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Selinum":                    {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Incarvillea delavayi":       {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Morina longifolia":          {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Podophyllum":                {"plantafstand":"30–45 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"nee"},
    "Trachystemon orientalis":    {"plantafstand":"30–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Trifolium":                  {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Cardamine":                  {"plantafstand":"20–30 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lunaria rediviva":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Mertensia":                  {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Tanacetum":                  {"plantafstand":"30–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Thermopsis":                 {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Delosperma":                 {"plantafstand":"10–15 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":False,"giftig":False,"insectvriendelijk":"bijen"},
    "Erysimum":                   {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Linum perenne":              {"plantafstand":"20–30 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Malva":                      {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Physalis alkekengi":         {"plantafstand":"30–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":True,"insectvriendelijk":"nee"},
    "Anaphalis":                  {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Anthericum":                 {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Kalimeris incisa":           {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Sisyrinchium":               {"plantafstand":"15–25 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Telekia speciosa":           {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Artemisia":                  {"plantafstand":"30–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Asclepias":                  {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":True,"insectvriendelijk":"beide"},
    "Dictamnus albus":            {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"solitair","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
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
