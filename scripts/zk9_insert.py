#!/usr/bin/env python3
"""ZK9: Zorgkalender voor Hydrangea petiolaris t/m Lysimachia (25 genera)."""

import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'vaste-planten.js')

ZORGKALENDER = {
    "Hydrangea anomala petiolaris": {
        "feb": "Alleen zijscheuten die te ver uitsteken terugsnoeien — nooit de hoofdranken",
        "mei": "Nieuwe ranken voorzichtig inbinden — hechtzuigers werken zelf",
    },
    "Hylomecon japonica": {
        "apr": "Mulchen met bladcompost in vochtige schaduwgrond",
        "jun": "Blad laten uitsterven na de bloei",
    },
    "Hylotelephium spectabile": {
        "mrt": "Terugsnoeien tot op de grond — pas bij groene scheuten",
        "sep": "Vlinders en bijen bezoeken de bloemen intensief — niet storen",
        "nov": "Stelen met verdroogde schermen laten staan als winterdecoratie",
    },
    "Iberis sempervirens": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact, evergreen tapijt",
    },
    "Imperata cylindrica": {
        "mrt": "Dode bladpunten bijknippen; voorzichtig — rode kleur ontwikkelt langzaam",
    },
    "Incarvillea delavayi": {
        "mrt": "Plant komt laat op — mulch laten liggen tot scheuten verschijnen",
        "nov": "Dik mulchen voor vorstbescherming van de vlezig penwortel",
    },
    "Inula": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Verwelkte bloemen verwijderen voor langere bloei",
    },
    "Iris ensata": {
        "apr": "Bijmesten in zure, vochtige grond",
        "jun": "Bloeit vroeg — verwelkte bloemen verwijderen",
        "okt": "Blad terugsnoeien tot 15 cm",
    },
    "Iris foetidissima": {
        "okt": "Oranje-rode bessen zijn decoratief in winter — stelen laten staan",
    },
    "Iris germanica": {
        "jun": "Bloeit! Na de bloei verwelkte bloemstelen afknippen",
        "aug": "Rhizomen liggen half boven de grond — niet bedekken",
        "sep": "Verouderde pollen na 4–5 jaar verjongen door te splitsen",
    },
    "Iris pallida": {
        "jun": "Na de bloei bloemstelen afknippen",
        "aug": "Rhizomen in de zon laten liggen voor rijping en bloemknopvorming",
    },
    "Iris pseudacorus": {
        "apr": "Bijmesten in oever- of watertuinomgeving",
        "jun": "Na de bloei zaaddozen verwijderen om overmatige zaadverspreiding te beperken",
    },
    "Iris pumila": {
        "jun": "Na de vroege bloei bloemstelen afknippen",
        "aug": "Rhizomen in zon laten rijpen",
    },
    "Iris reticulata": {
        "sep": "Bolletjes planten op 8–10 cm diepte in goed doorlatende grond",
        "jun": "Blad laten uitsterven na de vroege bloei",
    },
    "Iris sibirica": {
        "mrt": "Dode bladeren terugknippen",
        "apr": "Bijmesten in vochthoudende grond",
        "okt": "Blad terugsnoeien tot 15 cm; oude pollen na 5–6 jaar verjongen",
    },
    "Isotoma axillaris": {
        "apr": "Na laatste nachtvorst buiten planten of pot buiten zetten",
        "nov": "Vorstgevoelig — binnenhalen of als eenjarige behandelen",
    },
    "Jasminum officinale": {
        "feb": "Na de bloei (in de zomer of direct na winter) terugsnoeien",
        "mei": "Nieuwe ranken inbinden langs drager of pergola",
    },
    "Jeffersonia": {
        "apr": "Mulchen met bladcompost in vochtige schaduwgrond",
        "jun": "Blad laten uitsterven na de bloei",
    },
    "Kadsura japonica": {
        "mei": "Ranken inbinden langs drager",
        "nov": "Licht mulchen bij strenge winters",
    },
    "Kalimeris incisa": {
        "mrt": "Terugsnoeien tot op de grond",
        "jun": "Verwelkte bloemen verwijderen voor langere bloei",
    },
    "Kirengeshoma palmata": {
        "mrt": "Dode stengels verwijderen",
        "apr": "Mulchen in vochtige, zure, humeuze grond",
        "sep": "Late bloeier — pas terugsnoeien na de bloei",
    },
    "Knautia macedonica": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen regelmatig verwijderen voor de langste bloeitijd",
    },
    "Kniphofia": {
        "mrt": "Dode bladeren voorzichtig verwijderen; stam mulchen bij strenge winters",
        "apr": "Goed doorlatende grond — nooit nat in de winter",
        "okt": "Bladeren samenbinden ter bescherming van het hart bij strenge vorst",
    },
    "Koeleria glauca": {
        "mrt": "Dode bladpunten bijknippen of uitkammen",
    },
    "Lamium maculatum": {
        "jun": "Na de bloei halverwege terugsnoeien voor compact, sierbladig tapijt",
    },
    "Lamprocapnos spectabilis": {
        "apr": "Plant komt vroeg op — beschermen bij late vorst",
        "jun": "Na de bloei blad laten uitsterven; gat in de border opvullen met zomerbloeiende planten",
    },
    "Lathyrus latifolius": {
        "feb": "Ranken van vorig jaar verwijderen — plant groeit elk jaar opnieuw vanuit de wortel",
        "mei": "Ranken inbinden langs drager of gaas",
    },
    "Lathyrus vernus": {
        "jun": "Na de vroege bloei blad laten uitsterven — plant gaat in zomerruste",
    },
    "Leontopodium alpinum": {
        "apr": "Bijmesten in kalkrijke, goed doorlatende grond",
        "jun": "Verwelkte bloemen verwijderen",
    },
    "Leptinella squalida": {
        "mei": "Uitlopers terugknippen indien te breed uitlopend",
    },
    "Leucanthemum": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Verwelkte bloemen verwijderen voor tweede bloei",
        "aug": "Halverwege terugsnoeien na de piek voor hergroei",
    },
    "Lewisia cotyledon": {
        "apr": "Goed doorlatende, kalkarme grond in zon; nooit water op het hart",
        "jun": "Verwelkte bloemen verwijderen",
    },
    "Leymus arenarius": {
        "mrt": "Terugknippen; uitlopers terugdringen — kan sterk uitzaaien",
    },
    "Liatris spicata": {
        "mrt": "Terugsnoeien tot op de grond",
        "jul": "Aren van boven naar beneden bloeiend — verwelkte toppen verwijderen",
        "okt": "Bloeistelen laten staan als wintervoedsel voor vogels",
    },
    "Ligularia dentata": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
        "aug": "Nooit laten uitdrogen — grote bladeren verdampen veel vocht",
    },
    "Limonium latifolium": {
        "mrt": "Dode stengels verwijderen",
        "aug": "Bloemen oogsten voor droogboeketten",
    },
    "Linaria purpurea": {
        "mrt": "Terugsnoeien tot het grondrozet",
        "jun": "Verwelkte stelen halverwege terugsnoeien voor tweede bloei",
    },
    "Linum perenne": {
        "mrt": "Terugsnoeien tot het grondrozet",
    },
    "Liriope muscari": {
        "mrt": "Verouderde bladeren bijknippen",
        "apr": "Bijmesten in halfschaduw",
    },
    "Lobelia cardinalis": {
        "mrt": "Terugsnoeien tot het groene rozet",
        "apr": "Bijmesten in vochthoudende grond",
        "nov": "Licht mulchen bij strenge winters",
    },
    "Lobelia gerardii": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
    },
    "Lobelia siphilitica": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochtige tot natte grond",
    },
    "Lobelia tania": {
        "mrt": "Terugsnoeien tot het groene rozet",
        "nov": "Licht mulchen bij strenge winters",
    },
    "Lobelia × speciosa": {
        "mrt": "Terugsnoeien tot het groene rozet",
        "nov": "Licht mulchen bij strenge winters",
    },
    "Lonicera": {
        "feb": "Na de bloei (zomer) of in februari langste ranken terugsnoeien",
        "mei": "Nieuwe ranken inbinden langs drager of pergola",
    },
    "Lunaria rediviva": {
        "jun": "Zaadschijfjes laten rijpen — zilverachtig decoratief effect",
        "aug": "Stelen met zaadschijfjes oogsten voor droogboeketten",
    },
    "Lupinus": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Eerste bloeistelen afknippen voor tweede bloei",
        "aug": "Na de bloei terugsnoeien; plant is kortlevend — zaden verzamelen",
    },
    "Luzula": {
        "mrt": "Dode bladeren uitkammen",
        "apr": "Mulchen in vochtige, schaduwrijke grond",
    },
    "Lychnis": {
        "mrt": "Terugsnoeien tot het groene grondrozet",
        "jun": "Na de eerste bloei terugsnoeien voor tweede bloei",
    },
    "Lysimachia atropurpurea": {
        "mrt": "Terugsnoeien tot op de grond",
        "apr": "Bijmesten in vochthoudende grond",
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
