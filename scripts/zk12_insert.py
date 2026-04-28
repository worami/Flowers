#!/usr/bin/env python3
"""ZK12: Zorgkalender voor Passiflora t/m Primula (25 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Passiflora": {
        "mei": "Nieuwe ranken inbinden langs drager of pergola",
        "nov": "Wortels dik mulchen bij strenge winters; boven de grond bevriest meestal",
    },
    "Patrinia": {
        "mrt": "Dode stengels verwijderen",
        "aug": "Gele bloemen laten staan — zaadhoofden zijn decoratief in winter",
    },
    "Peltoboykinia watanabei": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Grote palmerige bladeren laten staan — blad is de sierwaarde",
    },
    "Pennisetum alopecuroides": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "aug": "Pluizige aren verschijnen — goudbruin siereffect in de herfst",
        "nov": "Aren laten staan voor wintersilhouet",
    },
    "Penstemon": {
        "mrt": "Terugsnoeien tot op de grond — pas bij zeker groene knoppen snoeien",
        "apr": "In goed doorlatende grond — nooit natte wortels in winter",
        "nov": "Licht mulchen bij strenge winters; matig winterhard",
    },
    "Perovskia atriplicifolia": {
        "mrt": "Terugsnoeien tot 20–30 cm boven de grond — niet tot op de stam",
        "apr": "In droge, goed doorlatende grond — verdraagt droogte uitstekend",
    },
    "Persicaria amplexicaulis": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Petasites hybridus": {
        "apr": "Mulchen in vochtige tot natte grond",
        "mei": "Uitlopers STERK beperken — plant is invasief, bevat schadelijke stoffen",
    },
    "Peucedanum verticillare": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Schermbloemige bloemen zijn rijke nectarbron voor insecten — laten staan",
    },
    "Phlomis russeliana": {
        "mrt": "Dode stengels verwijderen; zaadschermen van vorig jaar laten staan zijn mooi als wintersilhouet",
        "apr": "Bijmesten in droge tot matig vochtige grond in zon",
    },
    "Phlox paniculata": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten; voor goede luchtstroom zorgen om meeldauw te voorkomen",
        "jun": "Scheuten uitdunnen tot 5–7 per plant voor grotere bloemtrossen",
    },
    "Phuopsis stylosa": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact, kruipend tapijt",
    },
    "Phyllitis scolopendrium": {
        "mrt": "Beschadigde of bruine frondes terugknippen",
        "apr": "Mulchen met bladcompost in vochtige, halfschaduwrijke grond",
    },
    "Physalis alkekengi": {
        "mrt": "Terugsnoeien tot op de grond",
        "sep": "Rode lampionvruchten oogsten voor droogboeketten",
        "mei": "Uitlopers terugdringen — kan sterk uitstoelen",
    },
    "Physostegia virginiana": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "mei": "Uitlopers inperken indien te breed uitlopend",
    },
    "Phyteuma scheuchzeri": {
        "apr": "Bijmesten in kalkrijke, goed doorlatende grond",
        "jun": "Bolronde bloemhoofdjes zijn decoratief — laten staan na de bloei",
    },
    "Pileostegia viburnoides": {
        "mei": "Nieuwe ranken inbinden langs muur of drager",
        "nov": "Licht mulchen bij strenge winters; groenblijvend — behoudt blad",
    },
    "Pimpinella major": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Schermbloemige bloemen zijn rijke nectarbron — laten staan",
    },
    "Platycodon grandiflorus": {
        "apr": "Plant komt laat op — mulch laten liggen tot scheuten zichtbaar zijn",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
        "nov": "Stelen laten staan als bescherming — pas in het voorjaar terugsnoeien",
    },
    "Podophyllum": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Decoratieve vruchten rijpen na de bloei — giftig, niet eten",
        "okt": "Blad laten uitsterven",
    },
    "Polemonium caeruleum": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
    },
    "Polygonatum multiflorum": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Witte klokjes zijn decoratief — laten staan; blauwe bessen in herfst",
        "okt": "Stelen laten uitsterven, dan terugsnoeien",
    },
    "Polystichum": {
        "mrt": "Beschadigde of verouderde frondes volledig terugknippen",
        "apr": "Mulchen met bladcompost in vochtige, halfschaduwrijke grond",
    },
    "Potentilla": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor langere bloei",
    },
    "Primula": {
        "mrt": "Verdroogde bladrozetten opruimen",
        "apr": "Bijmesten in vochthoudende, humeuze grond; niet laten uitdrogen",
        "jun": "Na de bloei licht terugsnoeien voor hergroei van het blad",
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
