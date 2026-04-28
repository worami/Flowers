#!/usr/bin/env python3
"""ZK13: Zorgkalender voor Prunella t/m Senecio (25 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Prunella grandiflora": {
        "jun": "Verwelkte bloemen verwijderen voor tweede bloei",
        "aug": "Tweede bloei na terugknippen",
    },
    "Pulmonaria": {
        "mrt": "Verouderd blad terugknippen vóór of tijdens de bloei",
        "apr": "Mulchen met bladcompost in vochtige, halfschaduwrijke grond",
        "jun": "Fris nieuw blad laten groeien na het terugknippen",
    },
    "Pulsatilla vulgaris": {
        "mrt": "Vroegbloeiend — alleen dode bladeren verwijderen, bloemen niet storen",
        "jun": "Zijdeachtige zaadpluimen zijn decoratief — laten staan",
    },
    "Ranunculus": {
        "apr": "Mulchen in vochthoudende grond",
        "jun": "Bij dormante soorten: blad laten uitsterven na de bloei",
    },
    "Rodgersia aesculifolia": {
        "apr": "Mulchen in vochthoudende, halfschaduwrijke grond",
        "aug": "Groot blad verdampt veel vocht — nooit laten uitdrogen",
    },
    "Rodgersia henrici": {
        "apr": "Mulchen in vochthoudende grond; windluwe plek gewenst",
        "aug": "Niet laten uitdrogen — blad verkleurt bij droogte",
    },
    "Rodgersia pinnata": {
        "apr": "Mulchen in vochthoudende, halfschaduwrijke grond",
        "aug": "Bloempluimen laten staan voor winterdecoratie",
    },
    "Rodgersia podophylla": {
        "apr": "Mulchen in vochthoudende grond",
        "sep": "Decoratief roodbruin herfstblad — laten staan",
    },
    "Rodgersia sambucifolia": {
        "apr": "Mulchen in vochthoudende, humeuze grond",
        "jun": "Roomwitte bloemtrossen laten staan na de bloei — zaadhoofden decoratief",
    },
    "Romneya coulteri": {
        "mrt": "Terugsnoeien tot 20–30 cm boven de grond",
        "apr": "Droge, goed doorlatende grond in volle zon — verdraagt geen natte grond",
        "nov": "Wortels mulchen; boven de grond verdwijnt bij vorst — komt terug vanuit de wortel",
    },
    "Rudbeckia fulgida": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten met langzaamwerkende meststof",
        "okt": "Zaadhoofden laten staan als vogelvoer en winterdecoratie",
    },
    "Ruellia humilis": {
        "apr": "Bijmesten in goed doorlatende, zonnige grond",
        "jun": "Blauwe bloemen verschijnen — verwelkte dagbloemen verwijderen",
    },
    "Sagina subulata": {
        "apr": "Uitlopers inperken voor compact groen tapijt",
        "jun": "Kleine witte sterretjes zichtbaar — niet snoeien",
    },
    "Salvia nemorosa": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Na de eerste bloei halverwege terugsnoeien voor tweede bloei in augustus",
        "aug": "Tweede bloei na terugknippen",
    },
    "Sanguisorba officinalis": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Knopjesachtige bloemen zijn rijke nectarbron voor insecten",
        "okt": "Zaadhoofden laten staan als winterdecoratie en vogelvoer",
    },
    "Saruma henryi": {
        "apr": "Mulchen in vochtige, halfschaduwrijke, humeuze grond",
        "jun": "Gele bloemen in combinatie met hartvormig blad — decoratief",
    },
    "Saxifraga": {
        "jun": "Na de bloei licht terugsnoeien voor compact kussenvorming",
        "aug": "Uitlopers inperken bij soorten die brede tapijten vormen",
    },
    "Scabiosa columbaria": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor ononderbroken bloei",
    },
    "Schizachyrium scoparium": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Rood herfstblad is decoratief — niet snoeien",
    },
    "Schizophragma hydrangeoides": {
        "feb": "Zijscheuten die te ver uitsteken licht terugsnoeien",
        "mei": "Nieuwe ranken voorzichtig inbinden — hechtzuigers werken zelf",
    },
    "Scutellaria incana": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Blauwe bloemen zijn rijke nectarbron voor bijen",
    },
    "Sedum": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Goed doorlatende grond — nooit wateroverlast in de winter",
        "okt": "Zaadhoofden en stelen laten staan als winterdecoratie",
    },
    "Selinum": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Schermbloemige bloemen zijn rijke nectarbron voor insecten",
        "okt": "Stelen laten staan voor winterdecoratie",
    },
    "Sempervivum": {
        "apr": "Dode rozetten na de winter verwijderen",
        "jun": "Bloeiende rozetten sterven na de bloei — zijrozetjes nemen automatisch over",
    },
    "Senecio": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen",
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
