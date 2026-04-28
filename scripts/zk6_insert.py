#!/usr/bin/env python3
"""ZK6: Zorgkalender invoegen voor Crambe t/m Dystaenia (25 genera)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Crambe cordifolia": {
        "mrt": "Dode stengels van vorig jaar verwijderen",
        "apr": "Bijmesten in diepe, voedselrijke grond",
        "jul": "Na de grote bloei bloeistelen afknippen",
    },
    "Crocosmia": {
        "mrt": "Dode bladeren verwijderen; bij strenge winters mulchen wegnemen",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "sep": "Rode bessen op de stelen zijn decoratief — laten staan",
        "nov": "Dik mulchen bij strenge winters; kormen zijn matig winterhard",
    },
    "Cyrtomium": {
        "mrt": "Beschadigde of vorstbeschadigde frondes verwijderen",
        "apr": "Mulchen met bladcompost in schaduwrijke, vochtige grond",
    },
    "Darmera peltata": {
        "mrt": "Bloeit voor het blad verschijnt — roze bloemen op kale stelen, niet verstoren",
        "apr": "Mulchen in vochthoudende tot natte grond",
    },
    "Deinanthe": {
        "apr": "Mulchen met bladcompost in humeuze schaduwgrond",
        "okt": "Licht mulchen bij strenge winters",
    },
    "Delosperma": {
        "mrt": "Dode of uitgevroren stengels verwijderen",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor ononderbroken bloei",
    },
    "Delphinium": {
        "apr": "Scheuten uitdunnen tot 3–5 per plant voor grotere bloemen",
        "mei": "Staken vóór de planten te groot zijn",
        "jul": "Na de eerste bloei terugsnoeien tot 30 cm voor tweede bloei",
        "sep": "Tweede bloei in september na eerder terugsnoeien",
        "nov": "Terugsnoeien na afsterven; mulchen bij strenge vorst",
    },
    "Dendranthema": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "jun": "Chelsea chop voor meer vertakking en meer herfstbloemen",
        "okt": "Decoratieve bloemen laten staan tot de eerste vorst",
    },
    "Deschampsia": {
        "mrt": "Terugsnoeien tot op de grond of uitkammen",
        "aug": "Siertrossen laten staan als winterdecoratie",
    },
    "Dianthus": {
        "jun": "Na de bloei terugsnoeien tot het bladkussen voor compact blijven",
        "aug": "Eventuele tweede bloei na terugknippen",
    },
    "Dicentra": {
        "apr": "Plant komt vroeg op — beschermen bij late vorst",
        "jun": "Na de bloei blad laten uitsterven of afknippen als het geel wordt",
        "aug": "Goed moment om wortelstokken te splitsen",
    },
    "Dictamnus albus": {
        "mrt": "Dode stengels verwijderen — plant komt laat op",
        "apr": "Niet verplanten — plant heeft diepe penwortel",
        "jun": "Zaaddozen kunnen in droog, warm weer spontaan ontbranden — decoratief",
    },
    "Dierama": {
        "mrt": "Beschadigd blad verwijderen",
        "nov": "Kormen mulchen bij strenge winters; liever niet verplanten",
    },
    "Digitalis ferruginea": {
        "mrt": "Dode bloeistelen van vorig jaar verwijderen",
        "jul": "Bloeistelen gedeeltelijk laten staan voor zelfsaai",
    },
    "Digitalis lutea": {
        "mrt": "Dode stengels verwijderen",
        "jul": "Laten zaaien voor verjonging van de populatie",
    },
    "Digitalis mertonensis": {
        "mrt": "Dode stengels verwijderen",
        "jul": "Na de bloei terugsnoeien voor eventuele tweede bloei",
    },
    "Digitalis parviflora": {
        "mrt": "Dode stengels verwijderen",
        "jul": "Bloeistelen deels laten staan voor zelfsaai",
    },
    "Digitalis purpurea": {
        "mrt": "Dode stengels verwijderen; plant is tweejaar — na zaadsetting sterft hij",
        "jul": "Stelen gedeeltelijk laten staan voor zelfsaai",
    },
    "Disporum": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Mulchen in vochtige, humeuze schaduwgrond",
    },
    "Dodecatheon": {
        "apr": "Plant bloeit vroeg en gaat dan in zomerruste — niet verstoren",
        "jun": "Blad laten uitsterven",
    },
    "Doronicum": {
        "jun": "Na de vroege bloei halverwege terugsnoeien voor fris zomerblad",
    },
    "Draba bruniifolia": {
        "jun": "Na de vroege bloei licht terugsnoeien voor compact kussen",
    },
    "Dryas": {
        "jun": "Na de bloei zijranken licht terugsnoeien voor neat tapijt",
    },
    "Dryopteris filix-mas": {
        "mrt": "Alle oude frondes helemaal terugknippen voor nieuw blad",
        "apr": "Mulchen met bladcompost in schaduwrijke grond",
    },
    "Dystaenia takesimana": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Mulchen in vochtige grond",
    },
}

def build_zk_str(zk_dict):
    parts = [f'{m}:"{t}"' for m, t in zk_dict.items()]
    return "{" + ",".join(parts) + "}"

def insert_zorgkalender(content, latin_name, zk_dict):
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
    if 'zorgkalender' in content[idx:cv_idx]:
        print(f"  AL AANWEZIG (overgeslagen): {latin_name}")
        return content, False
    zk_str = f', zorgkalender:{build_zk_str(zk_dict)}'
    new_content = content[:cv_idx] + zk_str + content[cv_idx:]
    print(f"  OK: {latin_name}")
    return new_content, True

def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = 0
    for latin_name, zk in ZORGKALENDER.items():
        content, changed = insert_zorgkalender(content, latin_name, zk)
        if changed:
            updated += 1
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nKlaar. {updated}/{len(ZORGKALENDER)} entries bijgewerkt.")

if __name__ == '__main__':
    main()
