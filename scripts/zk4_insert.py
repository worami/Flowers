#!/usr/bin/env python3
"""ZK4: Zorgkalender invoegen voor Beesia t/m Campanula poscharskyana (26 genera)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Beesia calthifolia": {
        "apr": "Mulchen met bladcompost in vochtige, schaduwrijke grond",
    },
    "Belamcanda chinensis": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in goed doorlatende grond",
        "nov": "Licht mulchen bij strenge winters",
    },
    "Bergenia": {
        "mrt": "Oude, uitgelopen bladeren en dode stelen verwijderen",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "sep": "Blad kleurt rood-bruin in de herfst — decoratief laten zitten",
    },
    "Berkheya purpurea": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in goed doorlatende, zonnige grond",
        "nov": "Licht mulchen; niet geheel winterhard in strenge winters",
    },
    "Betonica officinalis": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "jun": "Verwelkte aren afknippen voor eventuele tweede bloei",
    },
    "Blechnum spicant": {
        "mrt": "Beschadigde of uitgevroren frondes verwijderen",
        "apr": "Mulchen met bladcompost in vochtige, zure grond",
    },
    "Boltonia asteroides": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor compactere plant en extra vertakking",
        "okt": "Bloeistelen laten staan voor vogels",
    },
    "Briza": {
        "mrt": "Dode bladpunten en verouderde halmen verwijderen",
        "jul": "Siertrossen oogsten voor droogboeketten voor ze volledig rijp zijn",
    },
    "Brunnera macrophylla": {
        "mrt": "Oude bladeren verwijderen",
        "apr": "Mulchen in vochthoudende, humeuze grond; verdraagt geen droogte",
    },
    "Buglossoides purpurocaerulea": {
        "apr": "Uitlopers terugknippen indien te breed uitlopend",
        "jun": "Na de bloei halverwege terugsnoeien",
    },
    "Buphthalmum salicifolium": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor lange bloeiperiode",
    },
    "Calamagrostis acutiflora": {
        "mrt": "Helemaal terugsnoeien tot op de grond voor nieuw blad",
        "sep": "Pluimen laten staan als winterdecoratie — lang stabiel",
    },
    "Calamintha nepeta": {
        "mrt": "Terugsnoeien tot op de grond",
        "sep": "Bloeistelen laten staan als wintervoedsel voor bijen en vogels",
    },
    "Caltha palustris": {
        "jun": "Na de vroege bloei blad terugknippen voor frisse hergroei",
        "aug": "Plant is in rust — niks doen",
    },
    "Campanula 'Pink Octopus'": {
        "jun": "Na de bloei halverwege terugsnoeien voor tweede bloei",
    },
    "Campanula 'Sarastro'": {
        "jun": "Verwelkte bloemen verwijderen; halverwege terugsnoeien voor tweede bloei",
    },
    "Campanula carpatica": {
        "mrt": "Eventueel dode bladeren verwijderen",
        "jun": "Verwelkte bloemen consequent verwijderen voor lange bloeitijd",
        "aug": "Halverwege terugsnoeien na piek voor hergroei",
    },
    "Campanula garganica": {
        "jun": "Verwelkte bloemen verwijderen",
        "aug": "Na de bloei licht terugsnoeien voor compact tapijt",
    },
    "Campanula glomerata": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Bloeistelen na de eerste bloei afknippen voor tweede bloei",
    },
    "Campanula lactiflora": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor compacter en rijker bloeiend",
        "aug": "Hoge stelen na bloei afknippen voor hergroei",
    },
    "Campanula latifolia": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Uitgebloeide stelen afknippen",
    },
    "Campanula latiloba": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Bloeistelen na de bloei afknippen voor hergroei",
    },
    "Campanula persicifolia": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Verwelkte klokjes regelmatig aftrekken voor langere bloeitijd",
        "aug": "Halverwege terugsnoeien na de bloei",
    },
    "Campanula portenschlagiana": {
        "jun": "Na de bloei terugknippen voor compact tapijt over muren en stenen",
    },
    "Campanula poscharskyana": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei",
        "sep": "Tweede bloeiflush in september bij goed terugknippen",
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
