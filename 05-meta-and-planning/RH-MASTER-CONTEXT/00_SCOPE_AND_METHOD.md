# Scope and method of the review

## Corpus covered

The review covers three layers.

| Layer | Size inspected | Protocol |
|---|---:|---|
| Paper 36 | `main.tex`: 8,806 lines, 54,962 words | Complete reading and a second, independent logical audit. |
| RH2017–RH2025 | 5,867 files; 743 Markdown; 629 `README`/`OVERVIEW` | Reading of all trajectory answers and comparison with data, code or tables where they support a material claim. |
| Phases | 101 directories; 4,052 files; 2,228 Markdown; 12 TeX; 1,067 Python probes | Block reading of all mathematical documents and closures; inspection of probes where they certify signs, identities or falsifiers. |

The phase directories carry labels 0 and 3–101; 1–2 do not exist and two directories carry label 44. This irregularity is kept as part of the record and not filled in artificially.

PDFs, images, binaries, caches and bulk outputs were not interpreted as proofs. They were used only to check that a text did not attribute to a figure or run a conclusion stronger than its data.

## Unit of audit

Each claim was split into six fields:

\[
(\text{object},\ \text{hypotheses},\ \text{quantifiers},\ \text{conclusion},\ \text{evidence},\ \text{dependencies}).
\]

The label is assigned to that sextuple, not to the file title or to the names `theorem`, `closure`, `QED`, `wall` or `no-go`. This prevents a correct finite-dimensional identity from absorbing, by association, an unproved limit.

For every finite–infinite bridge, the logical order

\[
\forall N\ \exists X_N
\qquad\text{versus}\qquad
\exists X\ \forall N,
\]

the dependence of constants, and the preservation of support, conjugation, linear multiplicity and sign were audited separately. Most false closures in the corpus occur when these quantifiers are swapped or one of these four pieces of information is lost.

## Adversarial test H0

Every route that claims to close \(\Omega_7\) must exhibit the step that carries the difficulty. The following check applies:

1. replace the actual divisor by a model with an off-line quartet;
2. keep, as far as possible, conductor, symmetries, coefficients and normalisation;
3. locate the first statement that ceases to be true;
4. require an arithmetic proof of that statement that does not use the divisor sought;
5. classify it as **RH-STRENGTH** if, through existing transfers, it already forbids the quartet.

If a construction also works on the off-line control, it is infrastructure or a build-neutral identity. If it fails only after Weil positivity, real-rootedness, a real divisor or a metric adapted to the roots has been inserted, it is circular. The only legitimate candidate is an arithmetic property that fails on the control and whose proof does not presuppose that failure.

## Documentary precedence

The order applied is

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

An earlier closure label is withdrawn if a later document identifies an open hypothesis or a counterexample. If two versions disagree and neither resolves the disagreement, the conservative status is **CONDITIONAL** or **OPEN**.

## Limits of this review

The review determines internal consistency, scope of proofs and duplications within the repository. It does not by itself certify bibliographic priority. Before declaring an idea new, the restart requires a separate search of primary sources and a comparison by statement, hypotheses and mechanism, not by vocabulary.

The dossier is deliberately kept compact (well below one megabyte). The exact measurement and the final inventory are in `COVERAGE_INDEX.md`.
