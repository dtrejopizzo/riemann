# R155_060 — Lead closing decision, round 8, and closing summary of phase 155 (2026-09-22)

Inputs: `R155_053`+`R155_058` (P6), `R155_054`+`R155_057` (P7), `R155_055`+`R155_059` (P9), `R155_056` (opening).
Round 8a (exact negative index via the multi-band relaxation) is **computed but not written up**: the scripts and
certified outputs are in `scripts/r8a/`, the memo `R155_052` is pending (the builder was cut off by a model quota
limit). Nothing of 8a enters any record until its memo is written and audited.

## 1. Labels of record added by round 8
| statement | label |
|---|---|
| Prop 1.1/1.3 (8b): `D_T ⟺ v_T ∈ 𝒟_T` closed convex, `Γ`-data only; RH `⟺ ∀T`; **the arithmetic content of row D is uniformity in `T` alone** | PROVED |
| Band structure (8b): `{σ_T<0}` finite union of intervals, `τ_* ≤ 60.5432` (`{2,3}`) and `120.0865` (`{2,3,4}`); alignment arcs at the convergents of `log2/log3` | PROVED (witnesses modulo double precision) |
| Thm 3.1 (8b): `𝖠_T(w) ⟹ D_T`; per window `[∃w: 𝖠_T(w)] ⟺ λ^W_T > 0`; `∀T ⟺ RH` | PROVED |
| Per-window converse `λ^A ≥ 0 ⟹ λ^W ≥ 0` | OPEN |
| Thm 4.2 + Cor 4.4 (8b): modifications of `Λ` preserving nonnegativity, `ψ` up to a constant, all zeros and the pole, yet failing `D_T`; **no classical prime-side theorem decides any window** | PROVED (in the sense of P46 Thm 18.1) |
| P7: **D-HS KILLED** by three independent routes (Thm 19.25 on `D^W`; radial collapse `h⁰ = O(m)`; Lemma 3 (b′)-failure). Residuals R1 (truncation of the Gaussian witness) and R2 (Horn B) belong to the frame | PROVED |
| Thm 1 + Cor 1 (8d): `λ^A(T) ≤ 4·10⁹·T·e^{−15.449T}` for `T ≥ 1`, unconditional given `(X19)`, `(X19′)`, `(X-N)` | PROVED |
| Cor 2 (8d): no `T`-uniform margin exists; `lim λ^A` exists in `[−∞,0]`; **RH `⟺ lim λ^A(T) ≥ 0`** | PROVED |
| Lemma 5 (8d): on primitive tests the prime comb **is** the Chebyshev remainder | PROVED |
Row-D label unchanged. Endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, primitive form). No sign for `ζ` beyond `T ≤ log 2`. No statement about the zeros of `ζ` except through the labelled imports.

## 2. What round 8 changes in the map
`PATH-TO-D` ranked P1–P7. After round 8: P1 negative (round 4), P2 partial, P3 bounded (rounds 5–7), P4 and P5 closed,
P8 closed (round 6), **P6 closed as an equivalence**, **P7 closed as a kill**. The ranked path is therefore exhausted;
what replaced it is sharper and entirely negative in the same direction: the sign at a fixed window is a statement about
finitely many `Λ(n)` and the `Γ`-factor, no classical prime-side theorem decides it, the margin to be certified decays at
least exponentially in `T`, and the only content left is uniformity in `T` — which, by `thm:Z` and Paper 46 W4, **is** RH.

## 3. Closing summary of phase 155
The phase was opened to attack Problem A of Paper 47 (class-dependent value bounds) and closed having converted the
obstruction from a qualitative wall into a quantified one. Proved in the phase: the Toeplitz ceilings and the class
impossibilities (`TK`, `N`, `N′`); collective positivity (`SC`) and non-termwise positivity in the zeros (Lemma R);
the intrinsic infiniteness of row D (`finZ`, `cor:infinite`); the two archimedean thresholds and the proved change of
role of the primes at `T*_{∞,P} ≈ 0.596`; RH as Kreĭn indeterminacy, unconditional below `0.8`; a proved positive value
in one direction at `log 2` and positive definiteness on seven even modes; the arena theorem (no finite truncation
decides the even Schur complement); Theorem P and the negative-index ceilings `5/7/8`; the retraction of `thm:AL` and
its correct replacement `AL′`; and, in round 8, the three results tabulated above. The phase also produced the reverse
track (row D of a finite zero universe is the zero measure) and the corpus synthesis `PATH-TO-D`.

## 4. Orders (owner decisions)
(a) Write and audit the 8a memo from `scripts/r8a/` (one short round; the certified outputs exist).
(b) Integrate into Paper 47 §9 what the audits cleared: 8b's Props 1.1–1.3, 2.1–2.3, Thm 3.1 with the new
    non-attainment lemma, Thm 4.2 / Cor 4.4 as a method constraint; 8d's Lemma 1, Lemma 2, Theorem 1, Cor 1, Cor 2
    and Lemma 5, with `(X-N)` and `(X19′)` added to the import table. Then a whole-paper review R4 (the three-round rule).
(c) Commit: phases 147–155, Papers 46–47, `PATH-TO-D`, repo-root `scripts/` — still untracked, still the owner's call.

## 5. Addendum (2026-09-22, evening): order (a) executed, order (b) executed
* **8a written and audited.** `R155_052` (builder, from `scripts/r8a/`) + `R155_061` (hostile audit: all headline
  claims PASS, six amendments A1–A6 applied in place, eight upper-bound runs regenerated with the corrected
  border sign — identical counts and margins, each < 15 s; lower bounds of record = `r8a_03_recheck.json`).
  Labels of record added:

| statement | label |
|---|---|
| Lemma 4.1 parity split (counts add) ; Lemma 4.2 monotonicity of the counts in `T` | PROVED |
| Lemma 4.3: `λ_ev`, `λ_odd`, `λ^P_∞` strictly decreasing in `T` | PROVED |
| Thm 5.1: `n₋(A_∞\|P_T) = 0` for `T < T*_ev`, `1` on `(T*_ev, T*_odd)`, `2` on `(T*_odd, 0.90]`; `0.58 ≤ T*_ev ≤ 0.60`, `log2 ≤ T*_odd ≤ 0.81` | PROVED (machine-verified) |
| Cor 5.2: `0.58 ≤ T*_{∞,P} ≤ 0.60` (first certified LOWER bound; round-4 order (d)); `A_∞ > 0` on `P_{½log3}` | PROVED (machine-verified) |
| Cor 5.3: **(H1) holds at `log 2`** (`n₋(A_∞\|P_{log2}) = 1`), for every `T₂ < T*_odd ∈ [log2, 0.81]` | PROVED (machine-verified) |
| (H1) at `0.80`, `n_odd(0.80) = 0` | OPEN (needs `τ_N ≈ 60`, off-machine) |

* **8b/8d integrated into Paper 47** (§§10.3–10.7, 34 labels, 67 pp.; backup `main_pre_R4.tex.bak`). The editor
  found an error in 8b Prop 2.3(v) missed by `R155_058` (erratum appended to `R155_053`) and an endpoint slip at
  `T₀(0)` (for R4). 8a integration into §9.1–9.2 in progress; then whole-paper review R4; then commit (owner
  authorised 2026-09-22).
Row-D label and endpoint of record unchanged. No sign for `ζ` beyond `log 2`.
