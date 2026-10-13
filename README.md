# Mali (ML) — législation en Markdown

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as plain Markdown in git.

**Minimal repository: the Constitution of the Republic of Mali only** (in French), as published in the Journal
officiel by the Secrétariat général du Gouvernement (SGG).

Retrieved 2026-10-13.

<!-- COUNTS -->
| Directory | Files |
|---|---|
| `constitution/` | 1 |
| **Total** | **1** |
<!-- /COUNTS -->

## Contents

```
constitution/constitution-2023.md   Constitution promulgated on 22 July 2023 (with the promulgation decree)
```

Constitutional context (stated factually): following the military takeovers of August 2020 and May 2021, Mali has
been governed by transitional authorities under a *Charte de la Transition* (2020, revised by loi n° 2022-001 of
25 February 2022 and again in 2025). A new Constitution was adopted by referendum on 18 June 2023 and promulgated by
décret n° 2023-0401/PT-RM of 22 July 2023 (Journal officiel, numéro spécial n° 13 of 22 July 2023); it replaced the
Constitution of 25 February 1992. The transitional institutions provided for by the Charter continue to operate
until the end of the transition. The Transition Charter itself is **not** included here.

The PDF is a born-digital two-column Journal officiel issue; columns are extracted separately (poppler) and
articles become `####` headings under TITRE (`##`) and CHAPITRE (`###`).

## Source

| Source | URL |
|---|---|
| SGG Mali — Journaux spéciaux, JO n° 2023-13 spécial du 22/07/2023 | https://sgg-mali.ml/JO/2023/mali-jo-2023-13-sp-3.pdf (listed at https://sgg-mali.ml/fr/journal-officiel/journaux-speciaux.html) |

## Not covered — why

The SGG website (https://sgg-mali.ml) is the official source of Malian law: it offers the Journal officiel since
the 1960s, the consolidated codes ("Codes en vigueur": code pénal, procédure pénale, personnes et famille, travail,
domanial et foncier, minier, douanes...) and other consolidated texts, and would allow a substantial corpus.
However, its legal notice (https://sgg-mali.ml/fr/mentions-legales.html) states that **any total or partial
reproduction of the site or of its content (including texts), by any means, without the prior express
authorisation of the Secrétariat général du Gouvernement du Mali, is forbidden**. In line with LawCodex's policy of
respecting site terms, only the Constitution is published here and nothing else was downloaded.

To complete this repository, written authorisation would be needed from the Secrétariat général du Gouvernement du
Mali (Cité administrative, Bamako; contact form at https://sgg-mali.ml/fr/contacts/nous-contacter.html). The older
SGG site (sgg.gov.ml) and the Assemblée nationale / Conseil national de Transition sites were unreachable.

## Copyright

The Constitution is an official text of the Republic of Mali. The Markdown conversion is provided as is; the
authoritative text is the one published in the Journal officiel de la République du Mali.

## Regenerating

```sh
python3 scripts/ml_fetch.py     # downloads the JO issue to ../_raw/ml/ and writes the Markdown
python3 scripts/ml_readme.py    # updates the counts table
```
