# Rebuild of Paper 46

The old Paper 46 ("Row D: the sign", ~130k words of markdown, `archive/main.md`) is superseded as the row D
paper by Paper 47. It has been rebuilt as a standalone paper, *An Intersection Frame for the Explicit Formula:
Hodge-Index Transfer, a Frame Defect Theorem and a Function-Field Model* (`main.tex`, 15 pages). The old
folder `46-row-d-the-sign` was renamed to `46-intersection-frame-defect`; all repository references to the old
name (outside `03-research/phase-209*`) were updated, links to `main.md` now point to `archive/main.md`.

## Classification of the old paper's results

(a) = duplicated in Paper 47 or Papers 43–45 → dropped (cite 47); (b) = superseded / withdrawn / refuted in
the old text, or restatements → dropped; (c) = valid and not in 47. Items in (c) not on the chosen theme are
dropped from the new paper but remain in the archive.

| old § | content | class | in new paper |
|---|---|---|---|
| 0–2 | row D target, standing negatives, acceptance test, self-assessment | b (row D framing) | no |
| 3.1 Lemma 3.1 | Π bijection onto the primitive class | c | yes, Lemma 2.9 |
| 3.2–3.4 | state reformulation D.1 (Bochner–Schwartz/SNAG), zero-side expression | b (graded RESTATEMENT; 3.6a(iii) withdrawn) | no |
| 4 | Schur complement Σ(T), swap law, monotonicity failure | a (window/Tate-block analysis superseded by 47's duality and finite reduction) | no |
| 5 | finite inertia of smeared Frobenius family; Thm 14.1 transport refuted | c (narrow, numerics-heavy; P47 §inertia covers inertia) / a | no |
| 6 | five candidate invariants refuted; requirement list (R1)–(R5) | b (superseded by Thm 12.3 per old Prop 12.5) | no |
| 7 | Ξ_a not a partial isometry; Davenport–Heilbronn | a (falsifiers in 47 §shape) | Ξ_a only via §9 |
| 9, 10, 14.4–14.5 | open lists, refutation ledgers, label | b (process record) | no |
| 11.0–11.2 | Weil class, explicit formula on D^W, extended form, Pólya class K, pairing | c | yes, §§2–3 |
| 11.3–11.4 | separation lemma, perp, radical, Prop 11.11a, compact radical = 0 | c | yes, §4 |
| 11.5 | degree, bounded density, ample cone | c | yes, §5 |
| 12.1–12.2 | σ_K, Hodge-index transfer theorem | c | yes, §6 |
| 12.3–12.5 | Ξ_a frame, Π_P, analogue of P45 Thm F, no h⁰ for Ξ_a | c | yes, §9 (condensed) |
| 12.4a–b | model-uniformity schema, heuristic | b (schema/heuristic) | no |
| 13 | candidate h⁰ (naive, integral, Connes–Consani dimension); growth | b (large parts withdrawn; closed by §19) | no |
| 14.1–14.3 | K in Paper 43's ruling plane, Frob_n vs K | c (Papers 43/44 dictionary) | no |
| 17.1–17.3 | ruling/zero data, splitting D^W = Λ ⊥ P^W, polar slack | c | yes, Thm 3.5, Prop 3.6 |
| 17.4–17.9 | Lorentzian criterion, detecting cones, Landau triangle family, PNT remainder, equimodularity | b (RH restatements) / c (17.8, 17.21–22 elementary) | no |
| 18.1–18.2 | T1 field uniformity, T2 Epstein constraint, axioms A1–A9 | a (P47 §shape: Epstein O10, field-uniform properties) | no |
| 18.3–18.6 | frame over number fields, base change, fork, growth of h⁰_Z | c / b | no |
| 19.1–19.7 | RR functional, Serre symmetry, gated candidate, χ>0 refuted, (b′)⁺, cosh lemma, witness, frame defect thm, truncation, small domain | c | yes, §§7–8 |
| 19.7 Rem 19.25c(i), Prop 19.7, Cor 19.9(ii) | statements whose content is an RH equivalence or assumes RH | b (program rule) | no |
| 19.8–19.9 | geometric diagnosis, horns A/B, enlargement test | c (19.30) / b (horn A blocked) | 19.30 as Thm 8.13; diagnosis in §11 |
| 19bis | Frobenius family over number fields, Pólya realization, bidegree route | a (Frobenius family is Paper 44) / c | no |
| 20 | trace-positive cone B4, transfer 12.3-B4, fixed-index ⟺ RH | c (transfer) / b (RH equivalences) | mentioned only |
| 21.1–21.5, 21.7 | function-field model: dictionary, radical, defect on the curve, cones, K = ½(F₁+F₂), no "+" | c | yes, §10 |
| 21.6 | bigness clause ⟺ RH | b (restatement; program rule) | no |
| 22 | degree form on Z⟨Frob_n⟩, computed Frobenius diagonal | c (zero-blind; Paper 44 material) | no |
| 23 | state of the sign | b | no |
| 24–25 | Galois ring inert at ζ, mixed effectivity | c (negative, row D method) | no |
| 26–27 | additive pencil, Deligne extraction, T3/T4/T5, coefficient classes | c (T5) / a (T3 Beurling in 47) / b (withdrawn items) | no |
| 28 | closure of row D in the map, Berkovich line, adèle class space | b (row D map decisions; now Paper 48) | no |

Counts (by numbered statements, approximate): ~330 numbered items in the old text; ~85 kept (condensed into
~60 statements of the new paper); ~245 dropped (~60 class a, ~95 class b, ~90 class c off-theme, retained in
the archive).

## Theme

The intersection-theoretic frame on D^W and its defect: structure (Pólya class, radical, polar plane,
bounded density) → conditional Hodge-index transfer → frame defect theorem → Ξ_a model → curve model. It is
stated as structural mathematics, not as an attack on row D. The relation to Paper 47 is one paragraph in §1.3.

## Mathematical changes and corrections

1. **Conclusion of the transfer theorem.** Old Thm 12.3 ended "hence RH (Paper 45 Thm 10.4)". The new
   Theorem 6.2 concludes `I(F,F) ≤ 0` on primitive compactly supported tests and stops (program rule: no
   statement linking this positivity with RH). Same for old Thm 19.11 (now Thm 7.4). Not a change of mathematics.
2. **Name of K.** Called the Pólya class, following the old paper's own correction of record (§21.5).
3. **Lemma 19.20(iv), flagged citation gap closed.** The old proof counted ≤ log T ordinates per unit interval
   from T = 21, which explicit bounds do not give there. Now: Trudgian's explicit S(T) bound (constant 2.510)
   gives ≤ 10 log T for T ≥ 21, hence L ≤ 5.5·10⁻⁹⁰ (was 5.46·10⁻⁹¹).
4. **Lemma 19.20(v), arithmetic.** The old bound |W − 2G²| ≤ 6·10⁻⁹¹ does not follow from its own proof
   (11.59·L = 6.3·10⁻⁹⁰ with the old L). Now ≤ 7·10⁻⁸⁹ with the new L. Downstream: C_{F0} < G s₁ + 10⁻⁸⁹,
   s_{F0} ≤ s₁ + 10⁻⁸⁹ (old: s₁(1+10⁻⁸⁹)^{1/2}). Threshold 324.9598266… and the certified instance (d = 400)
   are unchanged in every displayed digit; truncation constants change only in the 10⁻⁸⁹ term.
5. **Curve witness in a general direction θ (old Thm 21.14).** The old proof took F₀ with coordinates
   (0,0,0,1) for every θ; then Re(e^{iθ}Φ_{F0}(ρ₁)) = −sin θ, not 1, so the witness is only correct at
   θ = π/2. Corrected: F_θ has coordinates (0,0,cos θ, −sin θ) (Thm 10.8). The certified instance at θ* (d = 3)
   now holds as stated.
6. **Degree normalization for Ξ_a.** The old §12.5 (S2) set deg_Z = I(·,K_Z) while §19 used I(·,2K_Z). The new
   paper uses deg_a = I^{(a)}(·,2K_a) throughout (Prop 9.1). Notational; no statement changes.
7. Old Thm 11.12 is not claimed for Ξ_a (as in the old text); old Prop 12.6's hypothesis list is condensed into
   the three non-verbatim proof steps of Prop 9.1.

## Build

`pdflatex main.tex` twice: 0 errors, no undefined references or citations, 15 pages. (The old paper was
markdown; there is no previous page count.)

## Note for Paper 47

Paper 47 cites `\cite{Paper46}` ("Row D: the sign") for the axioms A1–A6 and the field-uniform properties.
Those live in the archived text (old §18), not in the rebuilt paper; the bibitem should point to the archived
record or be re-targeted.

## Follow-up: Paper 47's citations of the old Paper 46 (done)

Backup: `47-row-d-dual-certificates/main_pre_cite46.tex`. All four `\cite{Paper46}` (deduction classes, Lemma O10
Epstein, Lemma O12 field change, the open-problem list) cite old §18 (axioms A1–A6/A9, T1 = Thm 18.1,
Thms 18.10, 18.16), none of which is in the rebuilt Paper 46 and none short enough to restate as proved in 47.
The bibitem (key and all labels unchanged) now describes the source as the unpublished, superseded manuscript
kept as research notes in `46-intersection-frame-defect/archive/main.md` §18, explicitly not part of the paper
published as number 46; each citation says "research notes" and gives the § or theorem number. No
mathematics changed. Recompiled: 0 errors, no undefined references, 194 pages.
