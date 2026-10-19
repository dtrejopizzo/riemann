# Scope and method of the review

## Corpus included

The review covers three layers.

| Layer | Size inspected | Protocol |
|---|---:|---|
| Paper 36 | `main.tex`: 8,806 lines, 54,962 words | Full reading and second independent logical audit. |
| RH1–RH9 | 5,867 files; 743 Markdown; 629 `README`/`OVERVIEW` | Reading of all trajectory responses and cross-check against data, code or tables when they support a material claim. |
| Phases | 101 directories; 4,052 files; 2,228 Markdown; 12 TeX; 1,067 Python probes | Block reading of all mathematical documents and closures; inspection of probes when they certify signs, identities or falsifiers. |

The phase directories represent labels 0 and 3–101; 1–2 do not exist and there are two directories labeled 44. This irregularity is preserved as part of the record and is not artificially filled in.

PDFs, images, binaries, caches and bulk outputs were not interpreted as evidence. They were used only to verify that a text was not attributing to a figure or run a conclusion stronger than its data.

## Audit unit

Each claim was split into six fields:

\[
(\text{object},\ \text{hypothesis},\ \text{quantifiers},\ \text{conclusion},\ \text{evidence},\ \text{dependencies}).
\]

The label is assigned to that sextuple, not to the file title or the name `theorem`, `closure`, `QED`, `wall` or `no-go`. The procedure prevents a correct finite-dimensional identity from absorbing, by association, an unproved limit.

For every finite-to-infinite bridge, the logical order was audited separately

\[
\forall N\ \exists X_N
\qquad\text{versus}\qquad
\exists X\ \forall N,
\]

the dependence of constants, and the preservation of support, conjugation, linear multiplicity and sign. Most false closures in the corpus occur by swapping those quantifiers or by losing one of those four pieces of information.

## Adversarial test H0

Any route that claims to close \(\Omega_7\) must exhibit its difficulty-carrying step. The following control is applied:

1. replace the real divisor with a model having an off-line quartet;
2. keep, as far as possible, conductor, symmetries, coefficients and normalization;
3. locate the first claim that stops being true;
4. require an arithmetic proof of that claim that does not use the sought divisor;
5. classify it as **RH-STRENGTH** if, via the existing transfers, it already forbids the quartet.

If a construction also works on the off-line control, it is infrastructure or a build-neutral identity. If it only fails after Weil positivity, real-rootedness, a real divisor, or a metric adapted to the roots has been inserted, it is circular. The only legitimate candidate is an arithmetic property that fails on the control and whose proof does not presuppose that failure.

## Document precedence

The following order applies

\[
\text{correction with proof}
\;>\;
\text{final ledger}
\;>\;
\text{explicit closure}
\;>\;
\text{draft or summary}
\;>\;
\text{isolated numerical output}.
\]

An earlier closure label is withdrawn if a later document identifies an open hypothesis or a counterexample. If two versions disagree and neither resolves the discrepancy, the conservative status is **CONDITIONAL** or **OPEN**.

## Limits of this review

The review determines internal consistency, proof scope and duplications within the repository. It does not by itself certify bibliographic priority. Before declaring an idea novel, restarting requires a separate search in primary sources and a comparison by statement, hypothesis and mechanism, not by vocabulary.

The dossier is kept deliberately well below one million tokens. The exact measurement and the final inventory are kept in `COVERAGE_INDEX.md`.
