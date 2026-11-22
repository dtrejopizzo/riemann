# R150.000 — Blueprint: phase 150, the three method theorems (T3, T4, T5)

Rules: pure mathematics; numerics only for identity checks; corpus check before every construction; never
relabel to gain labels; no sign is claimed anywhere in this phase. Read first:
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-CLOSURE-PLAN.md` §§3, 8, 9;
`03-research/phase-149-row-d-additive-pencil/R149_001_ROUND1.md` §3 (D.60) and `R149_002_AUDIT.md`;
`04-papers/47-intersection-frame-defect/archive/main.md` §18 (T1, T2); `NO-GO-LIST.md` NG-B1, MW-2; `03-research/phase-119-*/README.md`
(the Davenport–Heilbronn gate).*

## 0. Purpose

Row D has two method theorems: T1 (any proof of the sign is uniform in the number field) and T2 (it must use the
Euler product essentially; falsifier: Epstein `Ξ_Q`). Phases 145–149 and the re-examination in plan §§3, 8, 9
identified three further constraints that the corpus states as repeated observations but has never proved as
theorems. Phase 150 proves them. Deliverable: three theorems with exact hypotheses, each with a **falsifier class**
(an explicit object satisfying every hypothesis a putative proof would use, for which the conclusion is false),
labels, and a corpus-check section per item. Nothing else.

## 1. T3 — the Beurling theorem (the `+` is necessary)

**Statement to prove (T3).** Let `𝒫` be a Beurling system of generalized primes `1 < p_1 ≤ p_2 ≤ …` with generalized
integers `𝒩`, counting function `N_𝒫(x)`, zeta `ζ_𝒫(s) = Π(1 − p^{-s})^{-1}`, von Mangoldt `Λ_𝒫 ≥ 0`. Suppose
`N_𝒫(x) = ax + O(x exp(−c(log x)^{θ}))` (Beurling's hypothesis in a strong form, so that `ζ_𝒫` has a simple pole at
`1`, continues meromorphically to a region left of `Re s = 1`, and the PNT holds for `𝒫`). **Theorem (Diamond–
Montgomery–Vorhauer 2006, to be IMPORTED with exact statement and hypotheses):** there exist such systems whose
`ζ_𝒫` has zeros `β + iγ` with `β ≥ 1 − c/log γ` for infinitely many `γ` — i.e. the de la Vallée Poussin region is
optimal in the Beurling class. **Consequence to prove as T3:** any argument establishing `β ≤ 1 − δ` (any fixed
`δ > 0`, a fortiori RH) for `ζ` that uses only (a) the Euler product with `Λ ≥ 0`, (b) the pole at `s = 1` with its
residue, (c) meromorphic continuation and growth bounds of the type available for Beurling zetas, (d) Landau-type
positivity arguments, is invalid: it would prove the same for a DMV system. Hence every proof must use a property
of `Z` outside the Beurling class — specify exactly which known properties of `ζ` fail for Beurling systems:
functional equation (Poisson summation on `Z`), integrality of the integers (Vinogradov's mean value / additive
energy of `[N,2N]`), the additive structure of the sequence `𝒩` (the sum set `𝒩 + 𝒩`), Voronoi/Poisson for divisor
sums, the multiplicative-additive interplay `n ↦ n+1`.

**Tasks.** (1) State DMV's theorem exactly (Diamond, Montgomery, Vorhauer, *Beurling primes with large oscillation*,
Math. Ann. 334 (2006)); state also Zhang's and Hilberdink–Lapidus's Beurling results if they sharpen the class.
Label IMPORTED; anything not read in the source is CERTIFIED. (2) Prove T3 as a **meta-theorem with a precise
axiom list** (as T2 was proved in Paper 47 §18.2: an axiom list A1–A9 and a falsifier satisfying all but the
Euler-product axioms). Here the falsifier class is `{ζ_𝒫}`. Name the axioms that `ζ_𝒫` satisfies (BE1–BEk) and
prove that every classical unconditional zero-free-region proof for `ζ` (de la Vallée Poussin; Landau; the
trigonometric-polynomial method in general) uses only BE1–BEk. (3) Show which unconditional theorems about `ζ`
**fail** for Beurling systems and why (functional equation; Vinogradov–Korobov — its additive input is the mean
value theorem, i.e. the additive energy of the moment curve on the integers; Voronoi). This list is the positive
content of T3: the `+` enters known proofs only through these. (4) Position T3 next to T2: `Ξ_Q` (Epstein) has the
`+` (functional equation, Poisson) and no Euler product; `ζ_𝒫` has the Euler product and no `+`; `Ξ_a` has both but
non-unimodular local roots. Prove that the three falsifiers are **mutually independent** (none of the three axiom
sets implies another) — a triangle of necessary conditions. (5) Corpus check: `Beurling` (124 hits: all
Beurling–Malliavin / Beurling–Nyman except one), `Vorhauer` (1: `E101_089`), `generalized prime`: confirm none
states T3.

**Warning W-T3.** Do not claim T3 shows RH needs "more than analytic number theory". It shows exactly which inputs
are outside the Beurling class. Say that and nothing more.

## 2. T4 — the smooth-regime theorem (where RH lives, and where cancellation methods do not)

**Observation to turn into a theorem.** Every unconditional power-saving cancellation for sums over primes or over
`μ` against a phase `φ(n)` operates in the **oscillatory regime**: the phase changes by `≫ 1` over the summation
range, quantitatively `frequency ≥ length^{θ}` for some `θ > 0` (Vinogradov's minor-arc bound for `Σ Λ(n)e(nα)`
needs `α` far from rationals of small height relative to `N`; van der Corput/exponent pairs for `Σ n^{it}` need
`t ≥ N^{1+δ}`-type conditions or give nothing beyond trivial when `t ≤ N^{ε}`; Vaughan's identity type I sums
against a smooth phase reduce to `Σ_{d ≤ U} μ(d) d^{-1-it}`, i.e. to `1/ζ(1+it)` truncated). RH is the statement
`Σ Λ(n) n^{-iγ} w(n/N) − (main) ≪ N^{1/2+ε}` for **fixed** `γ` and `N → ∞`: the phase `n^{-iγ}` is constant on
dyadic blocks up to `O(γ/N)`-relative variation — the **smooth regime**.

**Statement to prove (T4).** Formalize a class `𝒞` of "cancellation mechanisms": bilinear/trilinear bounds
(Vaughan, Heath-Brown identities) fed by (i) large sieve / mean value theorems for Dirichlet polynomials, (ii)
exponent pairs / van der Corput / Vinogradov MVT, (iii) Fourier restriction / additive energy bounds. Prove: for
`φ(n) = n^{-iγ}` with `γ` fixed (or `γ ≤ N^{o(1)}`), every bound obtainable from `𝒞` for
`Σ_{N<n≤2N} Λ(n) φ(n)` is `≥ N^{1-o(1)}` — no power saving — because in the smooth regime each mechanism's
hypothesis (spacing of frequencies, size of the second derivative of the phase, size of the frequency set) is
violated or reduces the sum to an untwisted prime sum. Make the theorem sharp: identify the boundary
`γ ≍ N^{θ_0}` below which `𝒞` returns nothing, mechanism by mechanism (this is Lindelöf territory for `θ_0`; do
not claim anything about `ζ(1/2+it)` bounds beyond citing Bourgain's `13/84`).

**Corollaries to state.** (a) Zero-free regions of the form `1 − c/(log t)^{a}` are exactly what the oscillatory
regime can deliver (VK is the sharp instance); (b) any zero-free STRIP `β ≤ 1 − δ` requires a mechanism outside
`𝒞` acting in the smooth regime; (c) the additive-pencil wall `c = 1/2` (D.60.3), the archimedean mean-value wall
(`T ≥ N^k`, plan §9.3) and NG-B1 are three instances of T4. **Falsifier**: a sequence `b_n` (e.g. `b_n =
Λ_a(n) = Λ(n)(n^{a} + n^{-a})`, the `Ξ_a` coefficients, or a Beurling `Λ_𝒫`) for which every mechanism in `𝒞`
gives the same bounds as for `Λ` while the smooth-regime sum genuinely has size `N^{1/2+a}`: this shows `𝒞`
cannot distinguish them, hence cannot prove RH.

**Corpus check.** NG-B1 (fifteen mechanisms; "arithmetic at `Re s > 1` does not propagate"), MW-2, D.60.3–D.60.6,
phase-106 `106_16` (translated Montgomery–Vaughan estimate: "the estimate loses the block center"), phase-119
gate. Cite; do not rebuild. T4 must be stated so that NG-B1 becomes a corollary, not a restatement.

## 3. T5 — the no-extraction theorem (Parseval-computable families never extract)

**Setting.** A "family moment method" (Deligne extraction, D.59) has: a family `ℱ` of size `|ℱ|`, fibre sums
`S_f(N)` of length `N`, a moment `M_{2k} = Σ_{f∈ℱ} |S_f(N)|^{2k}`, extraction `|S_{f_0}|^{2k} ≤ M_{2k}`. A moment
bound is **Parseval-type** if it is derived from an `L²`-orthogonality (large sieve on Farey points, Montgomery–
Vaughan mean value theorem on `[0,T]`, Heath-Brown's quadratic large sieve, Ramanujan-sum orthogonality) — all
of the shape `M_2 ≤ (|ℱ| + L)·‖b‖²` with `L` the length (or its `k`-th power for `M_{2k}` via `b^{*k}`).

**Statement to prove (T5).** For every Parseval-type bound the extracted fibre bound is `≥` the trivial bound:
precisely, `|S_{f_0}| ≤ ((|ℱ| + L^k) L^{k})^{1/2k} ‖b‖_{∞}-normalised ≥ L^{1/2}·max(|ℱ|^{1/2k}, L^{1/2})` — and the
second factor is `≥ L^{1/2}` exactly when `|ℱ| ≥ L^k`, which is the only regime where the Parseval bound is
non-trivial. Hence Parseval-type moments extract at best the trivial bound `|S_{f_0}| ≪ L`, uniformly over `k`,
over the family type (additive/Farey, archimedean/`t`, quadratic twists, characters mod `q`), and over the model
used for centering. Give the three instances (D.60.1–D.60.3; plan §9.3 archimedean; quadratic family with the
♭-restriction excluding squares) as corollaries. **Falsifier**: `b_n ≡ 1` (or the uncentered `Λ`), for which the
Parseval bound is attained and the fibre at the trivial point equals `L`.

**Corollary.** Any extraction of a non-trivial bound needs a moment bound `M_{2k} ≪ |ℱ| L^{k+o(1)}` in a regime
`|ℱ| < L^{k}` — i.e. cancellation *inside* the family that is not orthogonality — which is the content of (P149)
and of Montgomery's large values conjecture. State the equivalence exactly at `k = 1` and `k = 2`.

**Corpus check.** D.60.1–D.60.5, D.62.1, NG-B1 (large sieve entry), phase-36 Doc 106 Prop. 3.9 (sterility lemma:
"superadditivity and growth computed from the same data cannot contradict") — T5 is the analytic face of Prop. 3.9;
say so and prove the implication in one direction at least.

## 4. Falsifier gates (mandatory, per item)

Every theorem must be checked against: `Ξ_a` (must be indifferent: the method theorems hold verbatim), `Ξ_Q`
(Epstein: T3's falsifier triangle), `ζ_K` (T1 compatibility: all three theorems field-uniform), Beurling `ζ_𝒫`
(T3's falsifier; also a T4/T5 falsifier). Record explicitly if a theorem fails to be field-uniform.

## 5. Labels and FATAL rule

Labels: PROVED / IMPORTED / CERTIFIED / RESTATEMENT / OPEN. **FATAL**: if any argument in this phase produces a
zero-free region, a moment bound, or a cancellation not in the literature, stop and re-derive; presume error.
**No sign is claimed.** Row D keeps no label.

## 6. Deliverable

`R150_001_ROUND1.md`: §0 executive summary; §1 corpus check per theorem (grep-verified, commands listed);
§2 T3 with DMV import, axiom list, falsifier triangle, independence proof; §3 T4 with the class `𝒞`, sharp
boundary per mechanism, corollaries, falsifier; §4 T5 with proof, three instances, equivalence at `k = 1, 2`;
§5 gates; §6 labels table; §7 open list; §8 what this changes in Paper 47 §18 (proposed text for T3–T5, ≤ 1 page).
Length: whatever the proofs need, no padding. English.
