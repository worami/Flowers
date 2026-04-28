#!/usr/bin/env python3
"""ZK2: Zorgkalender invoegen voor Anemonella t/m Aster ericoides (25 genera)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Anemonella thalictroides": {
        "mrt": "Vroeg in het voorjaar verschijnen de eerste blaadjes — niet verstoren",
        "mei": "Blad laten uitsterven na de bloei; plant gaat in zomerruste",
    },
    "Anemonopsis macrophylla": {
        "apr": "Mulchen met bladcompost om de vochtige, humeuze grond te bewaren",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Angelica": {
        "mrt": "Dode stengels van de vorige bloeicyclus verwijderen",
        "aug": "Zaad oogsten voor uitzaai zodra het rijp is (plant sterft na zaadzetting)",
    },
    "Anthemis": {
        "mrt": "Terugsnoeien tot het groene bladrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor langere bloei",
        "aug": "Halverwege terugsnoeien voor krachtige hergroei en tweede bloei",
    },
    "Anthericum": {
        "mrt": "Dode bladeren verwijderen",
        "apr": "Bijmesten met langzaamwerkende meststof",
    },
    "Aquilegia vulgaris": {
        "mrt": "Dode stengels en oud blad verwijderen",
        "jun": "Bloeistelen na de bloei terugsnoeien om zaadverspreiding te beperken — of laten staan voor zelfsaai",
        "aug": "Zaad verzamelen voor uitzaai of nieuwe planten",
    },
    "Arabis": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact en dicht tapijt",
    },
    "Arctostaphylos uva-ursi": {
        "apr": "Eventueel uitlopers terugknippen bij te brede uitgroei",
    },
    "Arenaria montana": {
        "jun": "Na de bloei licht terugsnoeien voor compact blijven",
    },
    "Arisaema": {
        "mei": "Voorzichtig mulchen — knollen komen laat op",
        "okt": "Rode bessen zijn decoratief; knollen bij strenge vorst dik mulchen",
    },
    "Aristolochia": {
        "feb": "Langste ranken terugsnoeien voor compact houden",
        "mei": "Nieuwe ranken inbinden en leiden langs drager of gaas",
        "nov": "Wortels mulchen bij strenge winters",
    },
    "Armeria": {
        "jun": "Verwelkte bloemhoofden verwijderen voor hergroei en tweede bloei",
        "aug": "Eventuele tweede bloei na terugknippen",
    },
    "Artemisia": {
        "mrt": "Terugsnoeien tot op de grond of tot levende knoppen",
        "jun": "Halverwege terugsnoeien voor compacte, dichte groei",
    },
    "Arum italicum": {
        "apr": "Blad verschijnt in winter/voorjaar — niet verstoren",
        "sep": "Rode beskolven zijn decoratief in de herfst — laten staan",
        "okt": "Knollen mulchen bij strenge winters",
    },
    "Aruncus dioicus": {
        "mrt": "Alle dode stengels terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "sep": "Pluimen laten staan als winterdecoratie en voor vogels",
    },
    "Asarum": {
        "mrt": "Eventueel beschadigde bladeren verwijderen",
        "apr": "Mulchen met bladcompost om de vochtige schaduwgrond te bewaren",
    },
    "Asclepias": {
        "mrt": "Terugsnoeien tot op de grond na de winter",
        "apr": "Laat in de grond uitkomen — mulch laten liggen tot scheuten zichtbaar zijn",
        "sep": "Zaaddozen laten staan voor vogels en winterdecoratie",
    },
    "Asphodeline lutea": {
        "mrt": "Dode bladeren en bloeistelen verwijderen",
        "apr": "Bijmesten in goed doorlatende grond",
    },
    "Asplenium trichomanes": {
        "mrt": "Beschadigde frondes verwijderen",
        "apr": "Mulchen met grof zand en kalk voor mineraalrijke groeiplaats",
    },
    "Aster ageratifolius": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "sep": "Bloeiende plant weinig storen — zaad laten rijpen voor vogels",
    },
    "Aster alpinus": {
        "jun": "Verwelkte bloemen verwijderen voor eventuele tweede bloei",
        "aug": "Overjarige planten na 3–4 jaar verjongen door te delen",
    },
    "Aster amellus": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "okt": "Verwelkte bloemen laten staan voor vogels",
    },
    "Aster cordifolius": {
        "mrt": "Terugsnoeien tot op de grond",
        "okt": "Bloeistelen laten staan als winterdecoratie en zaadmaaltijd voor vogels",
    },
    "Aster divaricatus": {
        "mrt": "Terugsnoeien tot op de grond",
        "sep": "Bloeit in schaduw en halfschaduw; zaden laten rijpen voor zelfsaai",
    },
    "Aster ericoides": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Hoge cultivars eventueel tijdig snoeien (chelsea chop) voor meer vertakking",
        "okt": "Bloeistelen met zaadpluizen laten staan voor vogels",
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
