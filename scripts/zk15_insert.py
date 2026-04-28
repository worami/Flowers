#!/usr/bin/env python3
"""ZK15: Zorgkalender voor Thymus t/m Zantedeschia + resterende klimplanten (21 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Thymus serpyllum": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact, aromatisch tapijt",
        "aug": "Eventuele tweede bloei na terugknippen",
    },
    "Tiarella cordifolia": {
        "apr": "Mulchen met bladcompost in vochtige, halfschaduwrijke grond",
        "jun": "Na de bloei blad laten staan — wintergroen decoratief blad",
    },
    "Trachelospermum jasminoides": {
        "feb": "Licht terugsnoeien om de groei te beheersen",
        "mei": "Nieuwe ranken inbinden langs drager of pergola",
        "nov": "Mulchen bij strenge winters; groenblijvend — beschermt blad",
    },
    "Tradescantia × andersoniana": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Verwelkte bloemen dagelijks verwijderen — elke bloem leeft kort",
    },
    "Trachystemon orientalis": {
        "apr": "Mulchen in vochtige grond — groot blad verdampt veel vocht",
        "jul": "Uitlopers terugdringen indien te breed uitlopend — kan invasief worden",
    },
    "Trifolium": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
    },
    "Trillium": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Blad laten uitsterven na de bloei — niet te vroeg terugknippen",
    },
    "Trollius europaeus": {
        "apr": "Mulchen in vochthoudende tot natte grond",
        "jun": "Na de vroege bloei halverwege terugsnoeien voor fris zomerblad",
    },
    "Tulbaghia violacea": {
        "apr": "Bijmesten in goed doorlatende, zonnige grond",
        "nov": "Dik mulchen bij strenge winters; bollen zijn matig winterhard",
    },
    "Uvularia grandiflora": {
        "apr": "Mulchen met bladcompost in vochtige, humeuze schaduwgrond",
        "jun": "Blad laten uitsterven na de bloei",
    },
    "Valeriana officinalis": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Verwelkte bloemen tijdig verwijderen om overmatige zelfsaai te beperken",
    },
    "Verbascum": {
        "mrt": "Basaalblad laten staan — plant is tweejaar of kortlevend",
        "jun": "Na de grote bloei zaaddozen gedeeltelijk verwijderen; zaad deels laten rijpen voor zelfsaai",
    },
    "Verbena bonariensis": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Verwelkte bloemstelen verwijderen voor langere bloei",
        "okt": "Zaadhoofden laten staan als vogelvoer en wintersilhouet",
    },
    "Verbesina alternifolia": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
    },
    "Vernonia": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "okt": "Bloeistelen laten staan als winterdecoratie",
    },
    "Veronica": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor tweede bloei",
    },
    "Veronicastrum virginicum": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "jun": "Chelsea chop voor compactere, stevigere planten",
        "okt": "Stelen laten staan als winterdecoratie",
    },
    "Waldsteinia ternata": {
        "apr": "Mulchen in halfschaduw; goed doorlatende grond",
        "jun": "Na de bloei blad laten staan — halfwintergroen tapijt",
    },
    "Wisteria": {
        "feb": "Zijscheuten terugsnoeien tot 2–3 knoppen van de hoofdstelen",
        "aug": "Tweede snoei: lange nieuwe scheuten terugsnoeien tot 5–6 bladeren",
    },
    "Zantedeschia aethiopica": {
        "apr": "Bijmesten in vochthoudende tot natte grond",
        "jun": "Witte spathelken bloeien — verwelkte bloemen verwijderen",
        "nov": "Dik mulchen bij strenge winters; rhizomen zijn matig winterhard",
    },
    "Periploca graeca": {
        "mei": "Nieuwe ranken inbinden langs drager of pergola",
        "nov": "Mulchen bij strenge winters; matig winterhard",
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
