#!/usr/bin/env python3
"""ZK10: Zorgkalender voor Hemerocallis t/m Miscanthus sinensis (25 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Hemerocallis": {
        "mrt": "Dode bladeren terugknippen tot op de grond",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "jun": "Verwelkte bloemen dagelijks verwijderen — elke bloem leeft één dag",
        "okt": "Blad laten staan als winterbescherming voor de kroon",
    },
    "Hepatica": {
        "feb": "Vroegbloeiend — beschermen bij harde nachtvorst, anders niet storen",
        "apr": "Mulchen met bladcompost in vochtige, kalkrijke schaduwgrond",
        "jun": "Blad laten staan — fotosyntheseert door de zomer",
    },
    "Hesperantha coccinea": {
        "apr": "Bijmesten in vochthoudende, zonnige tot halfschaduwrijke grond",
        "sep": "Late bloeier — pas terugsnoeien na de bloei",
        "nov": "Licht mulchen bij strenge winters; rhizomen zijn matig winterhard",
    },
    "Hesperis matronalis": {
        "mrt": "Dode stengels verwijderen — plant is kortlevend/tweejaar",
        "mei": "Geurend in de avond — staan laten voor zelfsaai en verjonging",
        "jul": "Zaaddozen deels laten rijpen voor nieuwe generatie",
    },
    "Heuchera": {
        "mrt": "Verouderd blad verwijderen; ingezakte pollen omhoog duwen in de grond",
        "apr": "Bijmesten in halfschaduw; goed doorlatende grond — nooit wateroverlast",
        "okt": "Wintergroen blad laten staan — decoratief in alle seizoenen",
    },
    "Hibiscus moscheutos": {
        "apr": "Plant komt laat op — mulch laten liggen tot scheuten verschijnen",
        "jun": "Bijmesten in voedselrijke, vochthoudende grond",
        "sep": "Reusbloemen in late zomer/herfst — niet storen",
        "nov": "Stengels afknippen; wortels mulchen bij strenge winters",
    },
    "Hieracium aurantiacum": {
        "jun": "Verwelkte bloemen verwijderen om overmatige zelfsaai te beperken",
        "okt": "Uitlopers terugdringen — kan sterk uitzaaien en uitstoelen",
    },
    "Lythrum salicaria": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Verwelkte aren gedeeltelijk verwijderen om zaadverspreiding te beperken",
        "okt": "Stelen laten staan als winterdecoratie en vogelvoer",
    },
    "Lysimachia barystachys": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
    },
    "Lysimachia ciliata": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond; uitlopers inperken indien nodig",
    },
    "Lysimachia clethroides": {
        "mrt": "Terugsnoeien tot op de grond",
        "mei": "Uitlopers terugdringen — kan sterk uitzaaien op vochtige plaatsen",
    },
    "Lysimachia ephemerum": {
        "mrt": "Terugsnoeien tot op de grond",
    },
    "Lysimachia nummularia": {
        "mei": "Uitlopers terugknippen indien te breed uitlopend",
        "jun": "Bloeit — kleine gele bloemetjes tussen het kruipend tapijt",
    },
    "Lysimachia punctata": {
        "mrt": "Terugsnoeien tot op de grond",
        "mei": "Uitlopers terugdringen — kan sterk uitstoelen op vochtige grond",
    },
    "Macleaya microcarpa": {
        "mrt": "Dode stengels terugsnoeien tot op de grond",
        "mei": "Uitlopers dringend beperken — kan sterk uitzaaien",
        "aug": "Grote sierplanten oogsten voor droogboeketten bij de pluimbloei",
    },
    "Malva": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Verwelkte bloemen verwijderen voor langere bloeitijd",
        "aug": "Halverwege terugsnoeien voor hergroei en tweede bloei",
    },
    "Matteuccia struthiopteris": {
        "mrt": "Alle oude frondes volledig terugknippen voor het nieuwe blad uitloopt",
        "apr": "Mulchen met bladcompost in vochthoudende tot natte grond",
    },
    "Mazus reptans": {
        "apr": "Mulchen met zand voor goed doorlatende groeiplaats in zon",
        "jun": "Laten groeien als laag bodembedekker — niet storen",
    },
    "Meconopsis cambrica": {
        "mrt": "Plant zaait zichzelf — nieuwe rozetten laten staan voor bloei",
        "jun": "Zaaddozen deels laten rijpen voor zelfsaai en verjonging",
    },
    "Meehania urticifolia": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Na de bloei licht terugsnoeien voor compact tapijt",
    },
    "Melica": {
        "mrt": "Dode halmen uitkammen of terugknippen",
        "aug": "Decoratieve trosvormige aren laten staan als winterdecoratie",
    },
    "Melittis melissophyllum": {
        "apr": "Mulchen met bladcompost in vochtige, halfschaduwrijke grond",
        "jun": "Na de bloei laten staan — blad blijft decoratief",
    },
    "Mertensia": {
        "apr": "Plant komt vroeg op — beschermen bij late vorst",
        "jun": "Na de vroege bloei blad laten uitsterven — gaat in zomerruste",
    },
    "Milium effusum": {
        "mrt": "Dode halmen verwijderen; plant zaait zichzelf",
        "jun": "Zaaddozen laten rijpen voor zelfsaai in vochtige schaduwgrond",
    },
    "Miscanthus sinensis": {
        "mrt": "Terugsnoeien tot op de grond — niet te vroeg; wacht tot de vorst voorbij is",
        "aug": "Pluimen verschijnen — sierlijk goudbruin effect in de herfst",
        "nov": "Pluimen en stelen laten staan voor wintersilhouet",
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
