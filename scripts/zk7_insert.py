#!/usr/bin/env python3
"""ZK7: Zorgkalender invoegen voor Echinacea t/m Geranium cantabrigiense (27 genera)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Echinacea purpurea": {
        "mrt": "Dode stengels terugsnoeien — zaadhoofden hebben de winter als vogelvoer gediend",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "jul": "Verwelkte bloemen verwijderen voor langere bloei",
        "okt": "Zaadhoofden laten staan als winterdecoratie en voor mus en mees",
    },
    "Echinops ritro": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Bolbloemen oogsten voor droogboeketten vlak voor ze volledig opengaan",
        "sep": "Stelen laten staan als winterdecoratie",
    },
    "Elymus magellanicus": {
        "mrt": "Dode bladpunten bijknippen of uitkammen",
    },
    "Epilobium angustifolium": {
        "mrt": "Terugsnoeien tot op de grond",
        "aug": "Zaaddozen tijdig verwijderen om te brede uitzaai te voorkomen",
    },
    "Epimedium": {
        "feb": "Groenblijvend oud blad terugknippen vóór nieuw blad verschijnt",
        "apr": "Mulchen met bladcompost in halfschaduw",
    },
    "Eragrostis spectabilis": {
        "mrt": "Terugsnoeien tot op de grond voor nieuw blad",
        "sep": "Siertrossen laten staan als winterdecoratie",
    },
    "Eremurus": {
        "apr": "Vroeg opkomende scheuten beschermen bij late nachtvorst",
        "jul": "Na de bloei blad laten uitsterven — niet afknippen",
        "aug": "Wortelrozet mulchen; niet verplaatsen",
    },
    "Erigeron speciosus": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor langdurige bloei",
        "aug": "Na de piekbloei halverwege terugsnoeien voor hergroei",
    },
    "Erodium": {
        "mrt": "Dode bladeren en stengels verwijderen",
        "jun": "Licht terugsnoeien na de eerste bloei voor hergroei",
    },
    "Eryngium planum": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Stelen met bolbloemen oogsten voor droogboeketten",
        "sep": "Stalen-blauwe stelen laten staan als winterdecoratie",
    },
    "Erysimum": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact blijven",
        "nov": "Licht mulchen; niet volledig winterhard",
    },
    "Eupatorium maculatum": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "okt": "Pluimen laten staan als winterdecoratie en vogelvoer",
    },
    "Euphorbia": {
        "jun": "Na de bloei bloeistelen verwijderen — versap is huidirritant, handschoenen dragen",
        "sep": "Decoratief herfstblad bij sommige soorten — laten zitten",
        "nov": "Wintergroene soorten niet terugsnoeien",
    },
    "Fallopia": {
        "feb": "Ranken terugsnoeien voor compact houden",
        "mei": "Nieuwe ranken inbinden en leiden",
    },
    "Festuca glauca": {
        "mrt": "Dode bladeren uitkammen; voorzichtig terugknoeien",
        "apr": "Verouderde pollen na 4–5 jaar verjongen door te splitsen",
    },
    "Filipendula": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in vochthoudende tot natte grond",
        "sep": "Pluimen laten staan als winterdecoratie",
    },
    "Gaillardia × grandiflora": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor aanhoudende bloei",
    },
    "Galega": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Staken bij hoge cultivars voor windschade te voorkomen",
    },
    "Galium odoratum": {
        "apr": "Mulchen in vochtige schaduwgrond",
        "jun": "Na de bloei eventueel halverwege terugsnoeien",
    },
    "Gaura lindheimeri": {
        "mrt": "Terugsnoeien tot op de grond — pas bij zeker groene knoppen snoeien",
        "apr": "In droge, goed doorlatende grond — nooit nat staande wortels",
    },
    "Gentiana": {
        "apr": "Bijmesten met lichte, zure meststof voor zuurminnende soorten",
        "jun": "Bloeiende plant niet verstoren",
    },
    "Geranium 'Johnson's Blue'": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
        "aug": "Tweede bloeiflush na terugknippen",
    },
    "Geranium 'Rozanne'": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Tussentijds verwelkte bloemen verwijderen",
        "okt": "Plant bloeit door tot de eerste vorst — laten staan",
    },
    "Geranium cantabrigiense": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact, halfwintergroen tapijt",
        "sep": "Decoratief rood herfstblad — laten zitten",
    },
    "Geranium endressii": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
        "aug": "Rijke tweede bloei na terugknippen",
    },
    "Geranium himalayense": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact groeien",
        "sep": "Decoratief herfstblad — laten zitten",
    },
    "Geranium hybride": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
        "sep": "Decoratief herfstblad bij veel hybriden — laten zitten",
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
