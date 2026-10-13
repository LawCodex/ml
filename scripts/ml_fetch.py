#!/usr/bin/env python3
"""Mali: Constitution of 22 July 2023, from the Journal officiel (special issue n° 13 of 22 July 2023)
published by the Secrétariat général du Gouvernement (https://sgg-mali.ml).

Only the Constitution is converted: the site's legal notice forbids any total or partial reproduction
of its content without the prior express authorisation of the Secrétariat général du Gouvernement.
Usage: python3 ml_fetch.py [--no-download]"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ml_text as T  # noqa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(os.path.dirname(REPO), "_raw", "ml")
RETRIEVED = os.environ.get("LC_RETRIEVED", "2026-10-13")
URL = "https://sgg-mali.ml/JO/2023/mali-jo-2023-13-sp-3.pdf"


def main():
    dest = os.path.join(RAW, "jo-2023-13-sp.pdf")
    if "--no-download" not in sys.argv:
        T.fetch(URL, dest, delay=2, check_pdf=True)
    if not T.pdf_ok(dest):
        raise SystemExit("bad pdf")
    pages, ocr = T.pdf_text_columns(dest, "fra", tmpdir=RAW)
    lines = T.clean_pages(pages)
    # drop the masthead before the promulgation decree
    for i, x in enumerate(lines):
        if x.startswith("Vu la Charte de la Transition"):
            k = i
            while k > 0 and not lines[k - 1].startswith("DECRET N°2023-0401"):
                k -= 1
            lines = lines[max(0, k - 1):]
            break
    lines = [x for x in lines if not re.match(r"^(JOURNAL OFFICIEL DE( LA)?( REPUBLIQUE DU MALI)?|\d{1,2} Juillet 2023)$", x)]
    body = T.structure(lines, "fr")
    meta = {"title": "Constitution de la République du Mali", "identifier": "Décret n° 2023-0401/PT-RM du 22 juillet 2023 portant promulgation de la Constitution",
            "type": "constitution", "jurisdiction": "ml", "language": "fr", "date": "2023-07-22", "status": "in_force",
            "source": URL, "gazette": "Journal officiel de la République du Mali, numéro spécial n° 13 du 22 juillet 2023",
            "retrieved": RETRIEVED,
            "note": "Constitution adopted by the referendum of 18 June 2023 and promulgated on 22 July 2023, with the promulgation decree"}
    T.write_md(os.path.join(REPO, "constitution", "constitution-2023.md"), meta, meta["title"], body)
    print("OK", sum(len(x) for x in body))


if __name__ == "__main__":
    main()
