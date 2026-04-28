#!/usr/bin/env python3
"""ZK11: Zorgkalender voor Mitella t/m Parthenium (25 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Mitella": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Na de bloei laten staan — blad blijft decoratief door de zomer",
    },
    "Molinia": {
        "mrt": "Terugsnoeien tot op de grond — halmen breken makkelijk af in winter",
        "sep": "Goudbruin herfstblad is decoratief — niet snoeien",
    },
    "Monarda": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in voedselrijke, vochthoudende grond",
        "jun": "Chelsea chop voor compactere, rijker bloeiende planten",
        "sep": "Zaadhoofden laten staan als winterdecoratie en vogelvoer",
    },
    "Morina longifolia": {
        "apr": "Bijmesten in goed doorlatende, kalkrijke grond",
        "jun": "Bloeit — rozige bloemen langs de stelen, niet storen",
        "okt": "Stelen laten staan voor wintersilhouet",
    },
    "Muehlenbergia capillaris": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Roze-paarse harige pluimen zijn decoratief in de late herfst",
    },
    "Mukdenia rossii": {
        "apr": "Mulchen met bladcompost in vochthoudende halfschaduw",
        "sep": "Decoratief rood herfstblad — laten zitten",
    },
    "Myosotis palustris": {
        "mrt": "Uitlopers terugknippen indien te breed uitlopend op oeverplaatsen",
        "apr": "Plant bloeit vroeg en zaait zichzelf royaal — laten staan voor verjonging",
    },
    "Nepeta faassenii": {
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei in augustus",
        "aug": "Tweede bloei na terugknippen",
    },
    "Nerine bowdenii": {
        "sep": "Late bloeier — niet verstoren; bloeit voor het blad verschijnt",
        "nov": "Licht mulchen bij strenge winters; bollen zijn matig winterhard",
    },
    "Oenothera fruticosa": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor langere bloeitijd",
    },
    "Oenothera lindheimeri": {
        "mrt": "Terugsnoeien tot op de grond — pas bij zeker groene knoppen snoeien",
        "apr": "In droge, goed doorlatende grond — nooit nat staande wortels",
    },
    "Oenothera missouriensis": {
        "apr": "In goed doorlatende, zonnige grond — nooit wateroverlast",
        "jun": "Grote gele bloemen openen 's avonds — prachtig effect bij ondergaande zon",
    },
    "Oenothera speciosa": {
        "mrt": "Uitlopers terugdringen — kan sterk uitzaaien op droge, zonnige plekken",
        "jun": "Roze bloemen langs uitlopers — decoratief bodembedekker in zon",
    },
    "Onoclea sensibilis": {
        "mrt": "Alle oude frondes volledig terugknippen voor het nieuwe blad uitloopt",
        "apr": "Mulchen in vochtige tot natte grond; uitlopers kunnen breed uitzaaien",
    },
    "Ophiopogon planiscapus": {
        "mrt": "Verouderde bladeren bijknippen",
        "apr": "Bijmesten in halfschaduw; goed wintergroen blad",
    },
    "Origanum": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
        "aug": "Halverwege terugsnoeien voor hergroei en tweede bloei",
    },
    "Osmunda regalis": {
        "mrt": "Alle oude frondes volledig terugknippen voor nieuw blad",
        "apr": "Mulchen met bladcompost in vochtige tot natte, zure grond",
    },
    "Pachysandra terminalis": {
        "apr": "Mulchen in schaduwrijke, vochthoudende grond",
        "jun": "Eventuele lange uitlopers inperken voor nette bodembedekker",
    },
    "Paeonia lactiflora": {
        "mrt": "Terugknoeien tot op de grond na eerste groene knoppen — vroeg snoeien schaadt bloemknoppen",
        "mei": "Hoge cultivars staken vóór de bloem opengaat",
        "nov": "Blad volledig terugsnoeien om schimmelziekten te voorkomen",
    },
    "Paeonia officinalis": {
        "mrt": "Dode stengels verwijderen na eerste tekens van nieuw groen",
        "mei": "Staken bij zware bloemknoppen",
        "nov": "Blad terugsnoeien na afsterven",
    },
    "Paeonia suffruticosa": {
        "feb": "Dode en zwakke stengels verwijderen — struikpioen snoeien vlak voor groei begint",
        "mei": "Bloei — niet verstoren; na bloei verwelkte bloemen verwijderen",
    },
    "Panicum virgatum": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Roodachtig herfstblad en zaadpluimen zijn decoratief — laten staan",
    },
    "Papaver orientale": {
        "jun": "Na de bloei blad laten uitsterven; gat in border opvullen met zomerbloeiende plant",
        "aug": "Goed moment om te verplaatsen of te delen",
    },
    "Parthenocissus": {
        "feb": "Lange ranken terugsnoeien vóór de groei begint",
        "mei": "Nieuwe ranken inbinden of richting geven langs drager",
        "okt": "Vuurroze herfstkleur — laten staan tot het blad gevallen is",
    },
    "Parthenium integrifolium": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Verwelkte bloemen verwijderen voor langere bloeitijd",
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
