#!/usr/bin/env python3
"""KM1: Kenmerken invoegen voor entries 1–51 (Baptisia australis t/m Coreopsis verticillata)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

KENMERKEN = {
    "Baptisia australis":         {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Echinacea purpurea":         {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Rudbeckia fulgida":          {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Hemerocallis":               {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Echinops ritro":             {"plantafstand":"60–90 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Lythrum salicaria":          {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"hoog","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Helenium autumnale":         {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Phlox paniculata":           {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"vlinders"},
    "Monarda":                    {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Agastache":                  {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Kniphofia":                  {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Solidago":                   {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Salvia nemorosa":            {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Achillea millefolium":       {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Nepeta faassenii":           {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Paeonia lactiflora":         {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Paeonia officinalis":        {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":True,"insectvriendelijk":"bijen"},
    "Paeonia suffruticosa":       {"plantafstand":"90–150 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"solitair","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Persicaria amplexicaulis":   {"plantafstand":"90–120 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Perovskia atriplicifolia":   {"plantafstand":"60–90 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Campanula persicifolia":     {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula carpatica":        {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula garganica":        {"plantafstand":"15–25 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula glomerata":        {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula lactiflora":       {"plantafstand":"60–90 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula latifolia":        {"plantafstand":"45–60 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula latiloba":         {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula portenschlagiana": {"plantafstand":"15–25 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula poscharskyana":    {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula rapunculoides":    {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula 'Pink Octopus'":   {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Campanula 'Sarastro'":       {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Knautia macedonica":         {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Geranium sanguineum":        {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Ceratostigma plumbaginoides":{"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Scabiosa columbaria":        {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"kalkminnend","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Festuca glauca":             {"plantafstand":"20–30 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"nee"},
    "Stachys byzantina":          {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium macrorrhizum":      {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Geranium cantabrigiense":    {"plantafstand":"25–35 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Ajuga reptans":              {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Prunella grandiflora":       {"plantafstand":"20–30 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Thymus serpyllum":           {"plantafstand":"15–25 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Potentilla":                 {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Achillea filipendulina":     {"plantafstand":"45–60 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Allium":                     {"plantafstand":"15–20 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Veronicastrum virginicum":   {"plantafstand":"60–90 cm","grondtype":"vochtig","zuurgraad":"normaal","waterbehoefte":"normaal","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Verbena bonariensis":        {"plantafstand":"30–45 cm","grondtype":"normaal","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Penstemon":                  {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"bijen"},
    "Gaillardia × grandiflora":   {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"groepje","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
    "Coreopsis verticillata":     {"plantafstand":"30–45 cm","grondtype":"droog","zuurgraad":"normaal","waterbehoefte":"laag","groepering":"massa","winterhard":True,"giftig":False,"insectvriendelijk":"beide"},
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
