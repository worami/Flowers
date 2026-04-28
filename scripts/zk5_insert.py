#!/usr/bin/env python3
"""ZK5: Zorgkalender invoegen voor Campanula rapunculoides t/m Cosmos (30 genera)."""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Campanula rapunculoides": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Uitgebloeide stelen verwijderen",
    },
    "Campsis": {
        "feb": "Zijscheuten terugsnoeien tot 2–3 knoppen van de hoofdstelen",
        "mei": "Nieuwe ranken inbinden en strak leiden",
        "nov": "Bij strenge winters de wortels mulchen",
    },
    "Cardamine": {
        "mrt": "Vroegbloeiende soorten laten staan — geen ingreep nodig",
        "mei": "Na de bloei eventueel laten zaadrijpen voor zelfsaai",
    },
    "Carex": {
        "mrt": "Dode en verouderde halmen uitkammen of terugknippen",
        "sep": "Decoratieve pollen laten staan als winterstructuur",
    },
    "Catananche": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor hergroei",
    },
    "Celastrus orbiculatus": {
        "feb": "Ranken terugsnoeien — plant groeit krachtig en behoeft regelmatige snoei",
        "sep": "Oranje-rode bessen zijn decoratief — stelen laten staan",
    },
    "Cenolophium denudatum": {
        "mrt": "Dode stengels verwijderen",
        "sep": "Zaaddozen laten staan als winterdecoratie",
    },
    "Centaurea montana": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Na eerste bloei helemaal terugknippen voor tweede bloei",
    },
    "Centranthus ruber": {
        "mrt": "Dode stengels verwijderen",
        "jul": "Verwelkte pluimen afknippen om overmatige zelfsaai te beperken",
    },
    "Cephalaria": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Hoge stelen eventueel staken bij wind",
    },
    "Cerastium tomentosum": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact, zilverachtig tapijt",
    },
    "Ceratostigma plumbaginoides": {
        "mrt": "Terugsnoeien tot op de grond — plant komt laat op in het voorjaar",
        "sep": "Blauwe bloemen én rood herfstblad gelijktijdig — laten staan",
    },
    "Chasmanthium latifolium": {
        "mrt": "Terugsnoeien tot op de grond voor nieuw blad",
        "sep": "Siertrossen laten staan als winterdecoratie",
    },
    "Chelone obliqua": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Mulchen in vochthoudende grond",
    },
    "Chelonopsis moschata": {
        "mrt": "Dode stengels verwijderen",
        "nov": "Licht mulchen bij strenge winters",
    },
    "Chiastophyllum oppositifolium": {
        "jun": "Na de bloei licht terugsnoeien voor compact tapijt",
    },
    "Chrysanthemum": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Chelsea chop voor meer vertakking en meer bloemen",
        "okt": "Stelen met laatste bloemen laten staan tot vorst intreedt",
    },
    "Chrysogonum virginianum": {
        "apr": "Bijmesten in vochthoudende grond",
        "jun": "Regelmatig verwelkte bloemen verwijderen voor lange bloei",
    },
    "Chrysosplenium macrophyllum": {
        "apr": "Mulchen met bladcompost in vochtige schaduwgrond",
    },
    "Cimicifuga japonica": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in vochthoudende, humeuze grond",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Cimicifuga racemosa": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Mulchen in vochtige, humeuze schaduwgrond",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Cimicifuga ramosa": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Bijmesten in vochthoudende, humeuze grond",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Cirsium rivulare": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Zaadvorming beperken door bloemen deels te verwijderen",
    },
    "Clematis": {
        "feb": "Snoeien afhankelijk van groep: vroegbloeiende soorten licht na bloei; laat bloeiende soorten tot 30 cm terugknippen",
        "mei": "Nieuwe scheuten voorzichtig inbinden — breekbaar",
        "okt": "Wortels mulchen; stelen met zaadpluizen decoratief laten staan",
    },
    "Convallaria majalis": {
        "mrt": "Niet snoeien — vroeg opkomende bloemen zijn kwetsbaar",
        "mei": "Blad laten uitsterven na de bloei",
        "sep": "Goed moment om te verplaatsen of delen",
    },
    "Coreopsis verticillata": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor ononderbroken bloei",
        "aug": "Halverwege terugsnoeien na piek voor hergroei",
    },
    "Cornus canadensis": {
        "apr": "Mulchen met bladcompost in zure, vochthoudende grond",
        "jun": "Kleine witte bloemen — niet storen",
    },
    "Cortaderia selloana": {
        "mrt": "Handschoenen dragen! Oud blad uitkammen en dode bladpunten verwijderen; nooit te vroeg terugsnoeien",
        "sep": "Pluimen oogsten voor droogboeketten voor ze volledig opengaan",
    },
    "Corydalis": {
        "jun": "Na de bloei blad laten uitsterven — soort gaat in zomerruste",
        "aug": "Goed moment om te verplaatsen",
    },
    "Cosmos atrosanguineus": {
        "apr": "Knollen pas buiten planten na laatste nachtvorst",
        "nov": "Knollen uitgraven en vorstvrij bewaren of dik mulchen",
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
