#!/usr/bin/env python3
"""ZK14: Zorgkalender voor Serratula t/m Thermopsis (25 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Serratula seoanei": {
        "mrt": "Terugsnoeien tot op de grond",
        "okt": "Zaadhoofden laten staan als winterdecoratie",
    },
    "Sesleria": {
        "mrt": "Dode bladpunten uitkammen; compacte pollen hoeven weinig onderhoud",
    },
    "Seseli montanum": {
        "mrt": "Dode stengels verwijderen",
        "jun": "Schermbloemige bloemen zijn rijke nectarbron voor insecten",
        "okt": "Stelen laten staan voor winterdecoratie",
    },
    "Sidalcea": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Halverwege terugsnoeien na de eerste bloei voor tweede bloei",
    },
    "Silphium": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Verwelkte bloemen verwijderen voor langere bloei",
        "okt": "Zaadhoofden laten staan als vogelvoer",
    },
    "Sisyrinchium": {
        "mrt": "Verouderd en dood blad verwijderen",
        "jun": "Kleine blauwe of gele bloemen — verwelkte bloemen dagelijks verwijderen",
    },
    "Smilacina racemosa": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Pluimige witte bloemen decoratief — laten staan",
        "okt": "Rode bessen zijn decoratief in de herfst",
    },
    "Solidago": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Chelsea chop voor compactere, minder omvallende planten",
        "okt": "Zaadpluimen laten staan als winterdecoratie en vogelvoer",
    },
    "Sorghastrum nutans": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Goudachtige aren zijn decoratief in de herfst",
    },
    "Sphaeralcea": {
        "apr": "In goed doorlatende, zonnige grond — verdraagt droogte",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
        "nov": "Licht mulchen bij strenge winters; matig winterhard",
    },
    "Spodiopogon sibiricus": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Zilveren aren zijn decoratief in de herfst",
    },
    "Sporobolus heterolepis": {
        "mrt": "Terugsnoeien tot op de grond voor vers nieuw blad",
        "sep": "Fijne waaiervormige aren zijn decoratief in de herfst",
    },
    "Stachys byzantina": {
        "mrt": "Verouderd en beschadigd zilvergrijs blad verwijderen",
        "jun": "Bloemstelen verwijderen voor een puur zilver bladeffect; of laten staan voor bijen",
    },
    "Stauntonia hexaphylla": {
        "mei": "Nieuwe ranken inbinden langs drager of pergola",
        "nov": "Mulchen bij strenge winters; groenblijvend — beschermt bladeren",
    },
    "Stipa": {
        "mrt": "Dode halmen uitkammen; niet te sterk snoeien — veroudert langzaam",
        "aug": "Golvende aren zijn decoratief als wintersilhouet",
    },
    "Stokesia laevis": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor langere bloei",
    },
    "Strobilanthes": {
        "apr": "Bijmesten in licht beschutte, goed doorlatende grond",
        "jun": "Blauwe bloemen decoratief — laten staan",
        "nov": "Mulchen bij strenge winters; matig winterhard",
    },
    "Stylophorum diphyllum": {
        "apr": "Mulchen met bladcompost in vochtige, halfschaduwrijke grond",
        "jun": "Na de bloei zaad laten rijpen voor zelfsaai",
    },
    "Succisa": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "aug": "Blauwe knopjesachtige bloemen zijn rijke nectarbron voor bijen en vlinders",
    },
    "Symphytum": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Mulchen in vochtige grond",
        "mei": "Uitlopers terugdringen — kan sterk uitstoelen",
    },
    "Tanacetum": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
    },
    "Telekia speciosa": {
        "mrt": "Dode stengels verwijderen",
        "aug": "Grote gele schijfbloemen zijn decoratief — laten staan",
        "okt": "Stelen laten staan als winterdecoratie",
    },
    "Tellima grandiflora": {
        "apr": "Mulchen in vochtige, halfschaduwrijke grond",
        "jun": "Na de bloei blad laten staan — halfwintergroen decoratief blad",
    },
    "Thalictrum aquilegiifolium": {
        "mrt": "Dode stengels verwijderen",
        "mei": "Hoge cultivars staken vóór de groei te ver gevorderd is",
        "jun": "Decoratieve paarsroze pluimen laten staan — zaadhoofden ook mooi",
    },
    "Thermopsis": {
        "mrt": "Terugsnoeien tot op de grond",
        "mei": "Gele lupine-achtige bloemaren — niet te storen",
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
