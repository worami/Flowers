#!/usr/bin/env python3
"""ZK8: Zorgkalender voor Geranium macrorrhizum t/m Helleborus (28 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Geranium macrorrhizum": {
        "jun": "Na de vroege bloei halverwege terugsnoeien voor compact, geurig tapijt",
        "sep": "Decoratief rood en oranje herfstblad — laten zitten",
    },
    "Geranium nodosum": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
    },
    "Geranium oxonianum": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei in augustus",
        "aug": "Rijke tweede bloei na terugknippen",
    },
    "Geranium phaeum": {
        "jun": "Na de vroege bloei halverwege terugsnoeien voor fris zomerblad",
    },
    "Geranium pratense": {
        "jun": "Na de eerste bloei helemaal terugsnoeien voor tweede bloei én fris nieuw blad",
        "aug": "Tweede bloei na terugknippen",
    },
    "Geranium psilostemon": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "jun": "Na de bloei halverwege terugsnoeien",
    },
    "Geranium renardii": {
        "jun": "Na de vroege bloei licht terugsnoeien voor compact kussen",
    },
    "Geranium sanguineum": {
        "jun": "Na de vroege bloei halverwege terugsnoeien voor tweede bloei",
        "aug": "Tweede bloei na terugknippen",
    },
    "Geranium sylvaticum": {
        "jun": "Na de vroege bloei halverwege terugsnoeien voor fris zomerblad",
    },
    "Geranium versicolor": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
    },
    "Geranium wlassovianum": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "sep": "Decoratief herfstblad — laten zitten",
    },
    "Geranium × magnificum": {
        "jun": "Na de vroege bloei halverwege terugsnoeien voor compact blijven",
    },
    "Geranium × riversleaianum": {
        "jun": "Na de bloei licht terugsnoeien voor lange najaarsgroei",
        "okt": "Plant bloeit door tot late herfst — niet te vroeg terugsnoeien",
    },
    "Geum": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor langere bloei",
        "aug": "Halverwege terugsnoeien na de piek voor hergroei",
    },
    "Gillenia trifoliata": {
        "mrt": "Dode stengels verwijderen",
        "sep": "Decoratief rood herfstblad — laten zitten",
    },
    "Gypsophila": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
    },
    "Hakonechloa macra": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Gouden herfstkleur is decoratief — niet snoeien",
    },
    "Hedera": {
        "mrt": "Lange, uitbundige ranken terugsnoeien",
        "mei": "Nieuwe ranken leiden langs muur of drager",
    },
    "Helenium autumnale": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "jun": "Chelsea chop voor lagere, stevigere planten met meer bloemen",
        "okt": "Bloeistelen laten staan voor vogels",
    },
    "Helianthemum": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact tapijt",
    },
    "Helianthus": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in voedselrijke grond",
        "jun": "Chelsea chop voor meer vertakking en meer bloemen",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Helictotrichon sempervirens": {
        "mrt": "Dode bladpunten uitkammen; verouderde halmen verwijderen",
        "apr": "Verouderde pollen na 4–5 jaar verjongen door te splitsen",
    },
    "Heliopsis helianthoides": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor compacte, rijkbloeiende planten",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Helleborus": {
        "feb": "Beschadigde of zieke bladeren verwijderen vlak voor de bloei",
        "apr": "Mulchen met bladcompost in halfschaduw",
        "jun": "Zaaddozen verwijderen bij gevarieerde kleuren om ongewenste kruising te beperken",
    },
    "Hosta": {
        "apr": "Opkomende scheuten beschermen tegen slakken",
        "jun": "Droog houden — slakken vermijden vochtig blad minder snel",
        "okt": "Na afsterven blad volledig verwijderen om slakkeneitjes te verwijderen",
    },
    "Houstonia caerulea": {
        "apr": "Mulchen met zand voor goed doorlatende groeiplaats",
    },
    "Houttuynia cordata": {
        "mrt": "Terugsnoeien tot op de grond",
        "mei": "Uitlopers terugknippen — kan sterk uitzaaien",
    },
    "Humulus lupulus": {
        "feb": "Alle stengels terugsnoeien tot op de grond — plant groeit elk jaar opnieuw",
        "mei": "Nieuwe ranken inbinden voor de groeispurt begint",
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
