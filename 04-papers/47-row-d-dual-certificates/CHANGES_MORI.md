# Paper 47: Mori frontier update

Backup: main_pre_mori.tex. Author approved.

## Frontier statement (made consistent everywhere)
- Own certificate: T <= 1/2 log 5 (PROVED here, thm:log5A/thm:log5W).
- Liu, T <= 17/16, constant 2^-49162 (CITED).
- Mori, T <= 1/2 log 15, lambda^W_T >= 2^-2904 (CITED; computational part independently reproduced: author checker at 1280 bits, margins even 2.3979e-70, odd 3.9458e-66, independent mpmath spot checks; analytic reduction lemmas of the log 10 / log 12 papers not re-checked; unrefereed). Convention: width log mu means e^{2T} = mu; Mori's form = W_T with pole term 2Re(A B-bar).

## Edits
- Abstract: first-failure window now T_* > 1/2 log 15 (Mori, cited).
- Intro (certified range paragraph), "What remains open", related work, contributions: Mori added as current frontier; open range now T > 1/2 log 15.
- rem (contact-set list before shape section), rem:log5scope, rem:liu, rem:shape-scope: Mori added alongside Liu.
- New rem:moriceiling after cor:margin1: Mori's upper bound ~exp(-4 pi e^{2T}) (PLAUSIBLE-UNVERIFIED, cited); notes cor:margin1 uninformative for T <~ 1.5; consistent with prop:env.
- New rem:FDH at end of subsec:bar-arith: Davenport-Heilbronn falsifier F-DH (Ziad, a = 9/5), not W_T; methods not using multiplicativity must fail at some a < 9/5; PLAUSIBLE-UNVERIFIED.
- Bibliography: Mori15 (zenodo 23281236, code 23092422, data 23281176), MoriUpper (23363767 / concept 23175060), ZiadDH (23145454). Log 10 / log 12 papers cited only in text as earlier papers of the series (no DOIs in the record).

## Build
pdflatex x3: 0 errors, no undefined references; 172 pages.
