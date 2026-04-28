#!/usr/bin/env python3
"""ZK3: Zorgkalender invoegen voor Aster frikartii t/m Baptisia (24 genera)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Aster frikartii": {
        "mrt": "Terugsnoeien tot op de grond of tot het eerste groene blad",
        "jun": "Chelsea chop (halverwege terugsnoeien) voor compactere plant en latere bloei",
        "okt": "Bloeistelen laten staan voor vogels",
    },
    "Aster hybride": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor meer vertakking en latere bloei",
        "okt": "Zaadpluizen laten staan als wintervoedsel voor vogels",
    },
    "Aster laevis": {
        "mrt": "Terugsnoeien tot op de grond",
        "okt": "Decoratieve blauwig-grijze stelen mogen de winter in blijven",
    },
    "Aster lateriflorus": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor compact blijven",
        "okt": "Bloeistelen laten staan",
    },
    "Aster linosyris": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in goed doorlatende, kalkrijke grond",
    },
    "Aster macrophyllus": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Mulchen in vochtige schaduwgrond",
    },
    "Aster novae-angliae": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor extra vertakking en meer bloemen",
        "okt": "Decoratieve zaadpluizen laten staan als wintervoedsel voor vogels",
    },
    "Aster novae-belgii": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten en eventueel delen bij dichte pollen",
        "jun": "Chelsea chop voor compact en rijk bloeiend",
        "okt": "Bloeistelen met zaadpluizen laten staan voor vogels",
    },
    "Aster peduncularis": {
        "mrt": "Terugsnoeien tot op de grond",
        "okt": "Bloeistelen laten staan",
    },
    "Aster pilosus pringlei": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor extra vertakking en massale late bloei",
        "okt": "Decoratieve stelen met rijpe pluizen laten staan de hele winter",
    },
    "Aster ptarmicoides": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in goed doorlatende, droge grond",
    },
    "Aster pyrenaeus": {
        "mrt": "Terugsnoeien tot op de grond",
    },
    "Aster radula": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
    },
    "Aster sedifolius": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in goed doorlatende, kalkrijke grond",
    },
    "Aster tataricus": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond — verdraagt lichte natte omstandigheid",
        "okt": "Hoge bloeistelen laten staan als architectonisch winterelement",
    },
    "Aster thomsonii": {
        "mrt": "Terugsnoeien tot op de grond",
    },
    "Aster tongolensis": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in goed doorlatende grond",
    },
    "Astilbe": {
        "mrt": "Dode stengels verwijderen; wortelkuil indien nodig verhogen met compost",
        "apr": "Bijmesten met langzaamwerkende meststof; grond vochtig houden",
        "jun": "Nooit laten uitdrogen — bij droogte rijkelijk water geven",
        "sep": "Pluimen laten staan als winterdecoratie",
    },
    "Astilboides tabularis": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Mulchen in vochthoudende, humeuze grond",
        "jun": "Nooit laten uitdrogen — grote bladeren verdampen veel vocht",
    },
    "Astrantia major": {
        "jun": "Verwelkte bloemschermen terugknippen voor tweede bloei in augustus",
        "aug": "Tweede bloeiflush na terugsnoeien",
        "okt": "Stelen laten staan voor winterdecoratie",
    },
    "Athyrium": {
        "mrt": "Alle oude frondes volledig terugsnoeien voor nieuw blad verschijnt",
        "apr": "Mulchen met bladcompost in vochtige schaduwgrond",
    },
    "Aubrieta": {
        "jun": "Na de bloei volledig terugsnoeien voor compact en dicht tapijt",
    },
    "Aurinia saxatile": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact blijven",
    },
    "Baptisia australis": {
        "mrt": "Dode stengels van vorig jaar verwijderen — plant komt laat op",
        "apr": "Niet verplanten — diepe penwortel; niet storen",
        "sep": "Opgezwollen zwarte peulen laten staan als winterdecoratie",
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
