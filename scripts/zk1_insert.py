#!/usr/bin/env python3
"""ZK1: Zorgkalender invoegen voor Acaena t/m Anemone nemorosa (26 genera)."""

import re, sys, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Acaena": {
        "apr": "Dode en uitgevroren stengels verwijderen",
        "mei": "Uitlopers terugknippen als de mat te breed uitloopt",
    },
    "Acanthus": {
        "mrt": "Oude bladeren en afgestorven stengels tot op de grond snoeien",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "jun": "Bloeiwijzen na de bloei afknippen",
        "nov": "Wortelstok mulchen met droge bladcompost bij strenge winters",
    },
    "Achillea filipendulina": {
        "mrt": "Terugsnoeien tot op de grond of tot het eerste groene blad",
        "jun": "Verwelkte bloemschermen afknippen voor tweede bloei",
        "nov": "Droge schermen optioneel laten staan als winterdecoratie voor vogels",
    },
    "Achillea millefolium": {
        "mrt": "Terugsnoeien tot het groene bladrozet",
        "jun": "Na eerste bloei halverwege terugsnoeien voor hergroei en tweede bloei",
        "aug": "Tweede keer terugsnoeien voor eventuele derde bloei in september",
    },
    "Aconitum carmichaelii": {
        "mrt": "Oude stengels verwijderen; mulch aanbrengen",
        "mei": "Hoge cultivars tijdig staken voor de wind",
        "okt": "Na afsterven terugsnoeien; plant is giftig — handschoenen gebruiken",
    },
    "Actaea 'Queen of Sheba'": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in vochthoudende, humeuze grond",
        "okt": "Bloeistelen laten staan voor winterdecoratie",
    },
    "Actaea pachypoda": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Mulchen om vochtige grond te bewaren",
        "sep": "Witte bessen zijn decoratief — stelen laten staan",
    },
    "Actaea simplex": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in voedselrijke grond",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Actinidia": {
        "feb": "Zijscheuten en langste ranken terugsnoeien tot 2–3 knoppen",
        "jun": "Nieuwe ranken inbinden en leiden langs drager",
        "sep": "Vruchten oogsten bij eetbare soorten zodra ze zacht aanvoelen",
    },
    "Adiantum pedatum": {
        "mrt": "Alle frondes volledig terugsnoeien voor het nieuwe blad verschijnt",
        "apr": "Mulchen met bladcompost om vochtige grond te bewaren",
    },
    "Agapanthus": {
        "apr": "Pot naar buiten brengen na laatste nachtvorst; buiten geplante exemplaren mulch wegnemen",
        "jun": "Regelmatig water geven en maandelijks bijmesten",
        "sep": "Zaaddozen laten staan voor winterdecoratie of zaden oogsten",
        "nov": "Ingepotte exemplaren vorstvrij bewaren; buiten geplante wortelstokken dik mulchen",
    },
    "Agastache": {
        "mrt": "Terugsnoeien tot op de grond zodra de vorstperiode voorbij is",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "sep": "Bloeistelen voor de helft laten staan als wintervoedsel voor pimpelmezen",
    },
    "Ajuga reptans": {
        "apr": "Uitlopers inkorten als de mat te breed uitloopt",
        "mei": "Bloeiaren na de bloei afknippen om zaadverspreiding te beperken",
    },
    "Akebia quinata": {
        "feb": "Langste ranken terugsnoeien om plant compact te houden",
        "mei": "Nieuwe ranken inbinden en leiden langs drager of pergola",
        "nov": "Bij strenge winters kwetsbare wortels mulchen",
    },
    "Alcea": {
        "mrt": "Dode stengels van het vorige jaar helemaal verwijderen",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "jul": "Na eerste bloei stengel halverwege terugsnoeien voor zijscheuten",
    },
    "Alchemilla mollis": {
        "jun": "Na eerste bloei volledig terugsnoeien voor fris, nieuw blad",
        "aug": "Eventueel tweede keer terugsnoeien voor nette najaarsvorm",
    },
    "Allium": {
        "jul": "Verwelkte bloemhoofdjes verwijderen; blad laten uitsterven — niet afknippen",
        "sep": "Bollen planten op 10–15 cm diepte in goed doorlatende grond",
        "okt": "Mulchen bij nieuwe aanplant in koud klimaat",
    },
    "Alstroemeria": {
        "apr": "Opkomende scheuten door de grond breken voor meer bloei",
        "jun": "Bloeiende stelen aan de basis uit de grond trekken (niet knippen) voor doorgroei",
        "nov": "Wortelstok dik mulchen bij strenge winters",
    },
    "Althaea": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Hoge cultivars staken voor wind",
        "sep": "Zaden verzamelen voor uitzaai",
    },
    "Ampelopsis": {
        "feb": "Langste ranken terugsnoeien, plant compact houden",
        "mei": "Nieuwe ranken inbinden en leiden langs drager",
    },
    "Amsonia": {
        "mrt": "Terugsnoeien tot op de grond of tot levende knoppen",
        "sep": "Niet snoeien — de gele herfstkleur van het blad is decoratief",
    },
    "Anaphalis": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "aug": "Bloemen oogsten voor droogboeketten vlak voor ze volledig opengaan",
    },
    "Anchusa azurea": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Na de bloei halverwege terugsnoeien voor eventuele hergroei",
    },
    "Anemanthele lessoniana": {
        "mrt": "Alleen vorstbeschadigde bladpunten bijknippen — niet tot op de grond snoeien",
        "sep": "Niet snoeien; dit halfwintergroene gras blijft jaarrond decoratief",
    },
    "Anemone hupehensis": {
        "apr": "Mulch aanbrengen om de grond vochtig en onkruidvrij te houden",
        "aug": "Verwelkte bloemen verwijderen om de bloeitijd te verlengen",
        "nov": "Na afsterven licht mulchen voor vorstbescherming",
    },
    "Anemone nemorosa": {
        "mrt": "Vroege bloeier — niks doen; plant bloeit vanzelf",
        "mei": "Blad na de bloei laten uitsterven — niet afknippen",
        "aug": "Geschikte periode om te verplaatsen of te splitsen terwijl de plant in rust is",
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

    # Sla over als zorgkalender al aanwezig
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
