# R130.000 — Lead blueprint for closing row A (A.8, A.5, A.7, A.1) — phase 130

Author: session lead (Fable 5.1). Date: 2026-09-12. Status of this note:
`BLUEPRINT` — the mathematics below was derived and checked by the lead
(hand computation, and numerical checks in `scripts/`), and is handed to the
builder to be written into Paper 43 with complete proofs, and to the auditor
to be attacked. Nothing here is a citation of a theorem; every claim must be
re-proved in the paper or refuted in the audit.

Decisions by the repository owner that this phase acts on (2026-09-12):
(1) the A.6 amendment of Paper 43 §14.2 is **accepted** and is now the text
of clause A.6 in `P123_A_ACCEPTANCE_SPECIFICATION.md`; (2) A.8 is to be
attempted with new mathematics; (3) nothing of A.1–A.10 is to be left open.

Standing conventions: those of Paper 43 after phase 129 (`C_S ≅ R^× × ∏_{p∈S_f}Z_p^×`,
`D_A = C_c^∞(C_S)`, `T = Σ_v W_v + c·F(1)`, symbol `T̂` of Theorem 9.7, the
Tate functionals `λ_∓(F) = F̂(∓i/2)`, `M = (λ_−,λ_+)`, `B_T = C²` with
`β_T = [[0,1],[1,0]]`, `I_A(F,G) = T(F⋆G^†)`, `I_Tate = β_T(M·,M·)`,
`I_vec = (I_A, I_Tate)`, the completion `N_A^dist` of Theorem 9.14).
On the even unramified component write `f(t)` for the profile of `F` in
`t = log|w|_∞` and `F̂(τ) = ∫ f(t)e^{−iτt}dt`, so that `λ_+(F) = F̂(i/2) = ∫f e^{t/2}`
and `λ_−(F) = F̂(−i/2) = ∫f e^{−t/2}`.

---

## 0. The three insights, in one paragraph each

**(I) The rulings exist — in the completion, as limits of test classes.**
Theorem 9.13(a) proves that no `D_A`-module splitting of `0 → D_A^prim → N_A → B_T → 0`
exists inside `D_A`. It does **not** say the rulings are absent from the
theory. Take `ψ ∈ C_c^∞((0,∞))`, `∫ψ = 1`, and the "spread Tate character"
`f_n(t) := n^{−1} e^{−t/2} ψ(t/n)` (times `1_{∏Z_p^×}`). Then `λ_+(f_n) = 1`
exactly, `λ_−(f_n) = O(1/n)`, and `sup_τ|f̂_n(τ)| ≤ 2‖ψ‖_∞/n → 0`. Hence
`I_A(f_n, G) → 0` uniformly on bounded sets of `D_A` while `M(f_n) → e_+`.
So `J(f_n) → (0, e_+)` in `D_A' ⊕ B_T`, i.e. **`e_+ := (0,e_+) ∈ N_A^dist`**,
and likewise `e_− = lim J(g_m)`, `g_m(t) = m^{−1}e^{t/2}ψ(−t/m)`. These are
the two rulings: `D_A` acts on `(0,e_±)` by the characters `λ_±` (eigenvectors
in the completion — which does not contradict 9.13(a), whose eigenvector had to
be a function on the unitary dual; here the distribution component is **zero**).
Consequences: `N_A^dist = N_A^{dist,prim} ⊕ B_T` **canonically and as
`D_A`-modules** (`(ℓ,m) = (ℓ,0)+(0,m)`, both summands in the closure), so the
exact sequence splits in the completion and does not split on the dense sector.
The Weil decomposition `NS = rulings ⊕ Prim` is recovered exactly there.
Moreover the rulings are **`I_A`-null**: `I_A(f_n, g_m) → 0` (the integrand is
`O((nm)^{−1}(1+τ²)^{−1})` against `log|τ|`), while `I_Tate(f_n, g_m) → β_T(e_+,e_−) = 1`.
So the plane `span(e_+,e_−)` is exactly the **boundary radical of the scalar
completion** (P123.007 §4's `R_∂`), separated by the Tate component — this is
*why* P123.017 had to make the pairing vector-valued, and it is a theorem, not a
device.

**(II) The symbol is a Mittag-Leffler sum over the periodic Tate lattice with
universal residue.** For unramified `p` with `ζ = p^{−1/2−iτ}`:

    Ŵ_p(τ) = −i Σ_{k∈Z} [ 1/(τ − (i/2 + 2πk/log p)) − 1/(τ − (−i/2 + 2πk/log p)) ] − log p,

(symmetric summation; from `1/(1−e^{−w}) = ½ + Σ_k^{sym} 1/(w−2πik)` with
`w = (½+iτ)log p`). For the even archimedean factor, with `ω_n := i(2n+½)`:

    Ŵ_∞(0,τ) = log π + γ + Σ_{n≥0} [ −i/(τ−ω_n) + i/(τ+ω_n) − 1/(n+1) ].

So **every place has simple poles at the Tate points `±i/2` with the same
residue `∓i`**, the finite place `p` repeats them `2π/log p`-periodically
(the "periodic" of the periodic ruling determinant, P123.008), and the
archimedean place adds the Gamma tower `±ω_n`, `n ≥ 1`, and nothing else.
Checked numerically (`scripts/ml_check.py`): the Mittag-Leffler sum reproduces
`Ŵ_p` to `10^{−6}` for `p = 2,3,7`, and the residues at `±i/2` are `∓i` for
`Ŵ_2` and `Ŵ_∞`. Contour consequence (also checked): for `h > ½`,

    W_p(F) = Σ_{k∈Z} F̂(i/2 + 2πk/log p) + (1/2π)∫_{Im τ = h} F̂(τ)Ŵ_p(τ)dτ ,
    Σ_k F̂(i/2 + 2πk/log p) = (log p) Σ_{m∈Z} f(m log p) p^{m/2}   (Poisson),

the `p`-periodization of the Tate-twisted profile. **Consequence for A.8:** at
finite `S` the pole of `T̂_S` at `±i/2` has residue `∓i(|S_f|+1)`, so the
hyperbolic Tate form `I_Tate` is **not** a canonical analytic piece of the
scalar `I_A^S` (each place carries its own copy); the Tate structure at finite
`S` is carried by `M` and by the completion, not by the symbol. This is the
structural reason behind (I): the scalar line is trivial on the rulings.

**(III) The determinant lives on a Banach algebra, not on an operator cutoff.**
`T(F) = ∫F̂(T̂+c)dχ` (Thm 9.7(d)) and `(F^{⋆r})^∧ = F̂^r`, so for every `F ∈ D_A`
and `|z| < 1/‖F‖_{L¹}`:

    log Δ_F(z) := Σ_{r≥1} (−1)^{r+1} z^r T(F^{⋆r})/r = ∫_{Ĉ_S} log(1 + zF̂(χ)) (T̂(χ)+c) dχ ,
    |T(F^{⋆r})| ≤ ‖F‖_{L¹}^{r−1} · ∫|F̂|(|T̂|+|c|)dχ .

Define `‖F‖_tr := ‖F‖_{L¹(C_S)} + ∫_{Ĉ_S}|F̂|(|T̂|+|c|)dχ` and `𝓐_tr := ` the
completion of `D_A`. Then `‖F⋆G‖_tr ≤ 2‖F‖_tr‖G‖_tr` (use `|Ĝ| ≤ ‖G‖_1`), so
`𝓐_tr` is a Banach `†`-algebra, `T` extends continuously, `Det_S^rel = e^T`
is a continuous character `𝓐_tr → C^×`, the germ `Δ_F(z) = Det_S^rel(log(1+zF))`
is holomorphic on `|z| < 1/‖F‖_1`, continuous in `F`, and exactly multiplicative:
`Δ_F(z)Δ_G(z) = Δ_{F+G+zF⋆G}(z)`. This closes both halves of (O-A5-1): (a) the
inequality with `ρ = ‖F‖_1`, (b) the construction for **all** shells and the
archimedean place at once, because the symbol of Theorem 9.7 already contains
the cutoff limit. P123.105 §4's obstacle ("nonunit dilations … mix valuation
shells") is an obstacle for the *operator-cutoff* germ `det(1+zR_Λ(F))`, which
may carry a Szegő-type anomaly (P123.107 §5); the determinant of the theory is
P123.012's exp-type relative determinant `det_F exp(θ(F)R_Λ)e^{−2F(1)logΛ} → e^{T(F)}`,
which has no anomaly, and its Banach extension is the one above. On the unit
block the two agree (the cutoff commutes there), which recovers P123.105 (3)–(6).

---

## 1. A.8 — the theorem to prove, and the negative theorem beside it

### 1.1 Correct the formulation first

Paper 43 §10 (round 4) displays (A.8-I) as a monoidal functor `Φ_det` carrying
`Tr_A = Det_S^rel` to `λ_per`. **That requirement is unsatisfiable and must be
withdrawn as a formulation**: any functor through the Tate fibre depends on
`M(s(K))` only, while `Tr_A` separates classes with equal `M` (Thm 9.5, Thm 9.8).
The trace is not the ruling determinant in Weil's case either: `Tr(D) = D·Δ`
is not a function of the bidegree `(d_1,d_2)`. What A.8 asks (spec, as amended
in spirit by the A.6 decision) is that the Riemann–Roch determinant on the
**mixed sector** *extend* the intrinsic ruling determinant on the **ruling
plane**. With the ruling plane a canonical quotient (A.6) and a canonical
**subobject of the completion** (insight I), this has an exact meaning.

### 1.2 Target and definitions

* `T_A := Pic_b(B_T)`, based invertible `B_T = C_−⊕C_+`-modules ≅ pairs of based
  Hermitian lines. This is a determinant target in the sense of A.5, and it is
  the target of P123.008 §6 (two Knudsen–Mumford lines, `♯` exchanging them).
* Intrinsic periodic ruling determinant (Paper 42 `eq:intrinsicRRform`,
  P123.008 §6, A_MIXED_METRIC_WORK "fixed ruling line", norm `exp(−d_1d_2)`):
  `λ_per(b,b') := (C, ‖1‖² = exp(−β_T(b,b')))` on `B_T` — the hyperbolic Deligne
  pairing. **Fix the norm-vs-square convention once** (A_MIXED: `‖1‖ = exp(−I/2)`).
* Analytic determinant biextension: `L_S(F,G) := (C, ‖1‖² = exp(−I_A(F,G)))`
  (= `Det_S^rel(F⋆G^†)` with the metric convention fixed so that
  `L_S = L_tan` of A_MIXED (6)–(7) when `S = {q}`, `c = 0`).
* `λ_RR(F,G) := ( L_S(F,G) , λ_per(MF,MG) ) ∈ Pic_b(C)² = T_A` — the
  **vector-valued Riemann–Roch biextension**, the exponential of P123.017's
  numerical pairing `I_vec`.

### 1.3 Theorem A.8 (to be written as Theorem 10.7 with full proof)

(a) `λ_RR` is a based Hermitian biextension on `N_A = D_A`: additive in each
variable, Hermitian, with the interchange/associativity identities (P123.012 §4,
A_MIXED (7)), `†`-compatible (`λ_RR(F^†,G^†) = conj`, and `♯` on the second slot).
(b) *Convergence / continuity*: `λ_RR` extends continuously to `𝓐_tr × 𝓐_tr` in
the first slot (insight III) and to `N_A^dist` against tests (Thm 9.14), and
by the explicit limits of insight (I) to the ruling plane.
(c) *Principal invariance*: P123.012 §5 with the commutator hypothesis checked
(vacuous, `D_A` commutative) — keep Paper 43's honest note.
(d) *Restriction*: along the chart maps `J_{ST}`, `λ_RR` transforms by the
exact comparison (8A.12) in the first slot and **invariantly** in the second
(`M∘J_{ST} = M`); and on the colimit `D_A^∞` (§3 below) the first slot is
chart-invariant too.
(e) **Extension of the ruling determinant.** In `N_A^dist = N_A^{dist,prim} ⊕ B_T`
(insight I), the restriction of `λ_RR` to the ruling subobject `B_T` is
`(trivial, λ_per)`: the intrinsic periodic ruling determinant; its restriction
to the primitive completed sector is `(L_S, trivial)`; and for `F ∈ D_A` with
`J(F) = (I_A(F,·), 0) + (0, MF)` the **equality formula in `T_A`** is

    λ_RR(F,G) = λ_RR( (I_A(F,·),0), (I_A(G,·),0) ) ⊗ λ_per(MF, MG) ,

i.e. "intersection line = primitive line ⊗ ruling Deligne pairing", Weil's
`D·D' = P·P' + d_1d_2' + d_2d_1'` with the rulings entering only through their
Deligne pairing.
(f) *Metric comparison (A.8-II)*: `L_S = L_tan` for `S = {q}`, `c = 0`, exactly,
including the factor between norm and squared norm; for general `S`, `L_S` is
the exp-type operator determinant limit of P123.012 Thm 2.1 (no anomaly) and
the all-amplitude limit `Nμ(F/√N) → I_A(F,F)` holds at the symbol level by
insight III (`|T(H^{⋆r})| ≤ ‖H‖_1^{r−1}‖H‖_tr`, `H = F^†⋆F/N`).
(g) *No sign*: state that (e) contains no Hodge-index assertion, as the clause
requires, and cross-reference Theorem 14.1.

### 1.4 The negative theorem that must stand beside it (Theorem 10.8)

**The scalar line `L_S` alone does not extend `λ_per`**: on the rulings in the
completion `I_A(e_+, e_−) = 0`, so `L_S|_{B_T}` is trivial. Proof: the limit
computation of insight (I). Interpretation: at finite `S` the Tate degrees are
analytic functionals off the unitary axis (Thm 9.13(a)), so no continuous
scalar form built from the symbol can see them; and by insight (II) the poles
of `T̂_S` at `±i/2` overcount by `|S_f|+1`. This is the exact reason the
Riemann–Roch determinant of row A is vector-valued (`T_A = Pic_b(B_T)`), and
it must be stated as a theorem, not hidden.

### 1.5 The source functor, correctly typed (Theorem 10.9)

`M: D_A^+ → B_T` (unitization, `1 ↦ (1,1)`) is a surjective unital `†`-algebra
homomorphism (Thm 9.1). Base change `Φ_det := − ⊗_{D_A^+} B_T` from bounded
complexes of **based free** `D_A^+`-modules (the presented complexes of
Def 8A.1, with their differentials in `D_A^+`) to based free `B_T`-complexes is
exact, **strictly monoidal on free complexes**, carries `†` to `♯`, `Δ` to the
unit, and its Euler class is `M∘s`. Record P123.008 §7's derived gate honestly:
`Tor_1^{D_A^+}(B_T,B_T) = I/I²`, `I = ker M`; `I² ⊆ {F̂ has a double zero at
±i/2}` so `I/I²` surjects onto `C²` (the derivatives `∂_τF̂(±i/2)`), hence `M`
is **not** a homological epimorphism — P123.008 §7's predicted relative Tor is
nonzero and at least two-dimensional — but on the trace-class domain (free
complexes) the base change is strictly monoidal, and the Riemann–Roch content is
carried by (e), not by the cone `C_{T,S}`. Prop 10.6 stays: the contact
determinant is blind; `Φ_det` is base change along the Tate boundary, a
different construction.

---

## 2. A.5 — close every obstacle

* **(O-A5-1a, 1b)**: insight III. Write `𝓐_tr`, prove the Banach algebra
  inequality, continuity of `T`, holomorphy and multiplicativity of `Δ_F(z)`,
  and the agreement with P123.105 (3)–(6) on the unit block. State clearly the
  distinction between the exp-type determinant (anomaly-free) and the
  operator-cutoff germ (P123.107 §5's caveat), and that the theory's
  determinant is the former.
* **(O-A5-2)** *restriction*: the colimit trace. For `F ∈ D_A(S)` with
  `R^×`-support radius `R`, `W_ℓ(J_{S,S∪ℓ}F) = (log ℓ)Σ_{k≠0}ℓ^{−|k|/2}F(δ_S(ℓ^{−k}))`
  vanishes for `log ℓ > R`. So `T_∞(F) := T_S(F) + Σ_{ℓ∉S} W_ℓ(J F)` is a **finite**
  sum, and by (8A.12) `T_∞∘J_{ST} = T_∞` on the nose once `c` is chart-independent
  (next item). Define `D_A^∞ := colim_S D_A(S)` along `J_{ST}` (a `†`-algebra
  colimit); `T_∞`, `I_∞`, `M` (chart-invariant: `M∘J = M`) live on it. This is
  the "enlarged target" that (O-A5-2) asked for, and it closes O-A1-1/O-A1-2 too
  (§4). Do **not** claim `𝓝_∞ = 0` (see §5).
* **(O-A5-3)** the constant: **declare `c := 0`**. Justification to write out:
  (i) `T` is a definition since round 4, so `c` is a normalization; (ii) `c = 0`
  is the unique choice for which the chart constants agree (`c_T = c_S`) and the
  colimit trace is exactly chart-invariant; (iii) it is the unique choice for
  which the identity coefficient of the symbol equals the sum of the *intrinsic*
  Mittag-Leffler constants of the local factors (`−log p` at `p`, `log π + γ` at
  `∞`, insight II) with no extra global constant; (iv) it agrees with Paper 45's
  `χ_A = Σ_p W_p + W_∞`. Then Thm 14.1 is stated at `c = 0`. The imported cutoff
  theorem's own constant `c_cut` (Thm 8.10) is a *comparison* datum: attempt to
  compute it from P123.046's declared cutoff and P123.035 §3's folding; if it
  comes out, Thm 8.10 becomes exact; if not, Thm 8.10 keeps `c_cut` as a
  comparison constant and nothing in the theory depends on it. Either way the
  obstacle is closed for the theory.
* **(O-A5-4)** invariance of objects: **the obstacle was mis-posed**.
  `E_{2F} ≅ E_F` as (bi)modules (multiply by 2), yet `T(2F) = 2T(F)`; so no
  trace of correspondences can factor through unbased isomorphism classes — nor
  does Weil's: `Tr(2Γ) = 2Tr(Γ)`. The trace-class domain is the category of
  **based/presented** objects (Def 8A.1), exactly as cycles carry coefficients.
  Record the counterexample, delete the requirement (a), and note that (b)
  (idempotent splitting) is then not needed.
* **(O-A5-5)** shadow vs trace: the categorical shadow `Sh` (relative Hochschild,
  §7) on `E_F` is the divergent operator trace `Tr R(F)` (Thm 7.2 "constant or
  divergent"); `Tr_A = T` is its declared regularization, and Theorem 8.10 **is**
  the identification `Tr_A = Sh^{ren} − c_cut F(1)`. Write it as the closure of
  O-A5-5, with the identity-coefficient ambiguity named and absorbed by `c := 0`.
* **(O-A5-6)** faithfulness of `F ↦ E_F`: the regular representation of `L¹(C_S)`
  is faithful (Fourier transform `L¹ → C_0(Ĉ_S)` injective). Check that this is
  what "into the Fell sections" means in the paper and prove it.

---

## 3. A.7 — close (O-A7-1) and (O-A7-2)

* **(O-A7-1)** properness in the completion. Let `(ℓ,m) ∈ cl J(Eff) ∩ −cl J(Eff)`,
  `(ℓ,m) = lim J(F_n) = −lim J(G_n)`, `F_n, G_n ≥ 0`. Then `M(F_n), M(G_n) ∈ R_{≥0}²`
  and `m = lim M(F_n) = −lim M(G_n)` forces `m = 0`, i.e. `λ_±(F_n) → 0`. Since
  `|w|^{1/2}+|w|^{−1/2} ≥ 2`, `‖F_n‖_{L¹(d^*w)} ≤ ½(λ_+(F_n)+λ_−(F_n)) → 0`, so
  `sup|F̂_n| → 0` and `ℓ(G) = lim I_A(F_n,G) = 0` for every `G`. Hence `(ℓ,m) = 0`:
  **the cone is proper in `N_A^dist`**. This is exactly what P123.017 §7 said no
  `C*`-argument could give; the Tate component is a positive functional on the
  cone controlling the `L¹` norm.
* **(O-A7-2)** RR compatibility: `M(Eff) ⊆ R_{≥0}²` (effective classes have
  nonnegative bidegree, as in Weil), `Eff` is stable under `⋆`, `†`, the cone
  maps to the positive quadrant of the ruling plane, and `λ_per(MF,MF) = e^{−2λ_−λ_+}
  ≤ 1` on `Eff`. Read P123.010 §§2,5 and close each of its open items with a
  proof or an exact statement of what is (not) true; no sign on `L_S` is to be
  asserted.

---

## 4. A.1, A.2 — descent and the carrier

* **(O-A1-1)** geometric descent: the carrier is the directed system of charts
  `(C_S, D_A(S), T_S, M)` with transition maps `J_{ST} = π_{TS}^*` (Lemma 3.3),
  and the colimit `D_A^∞` of §2. `X` = the arithmetic curve realized as this
  system (all places), `Y` its square realized by the graph sectors `G(S)`.
  Construct and state the comparison maps; this is what A.1 asks.
* **(O-A1-2)** functor on objects along `S ⊆ T`: inflation `E_F ↦ E_{J_{ST}F}`,
  a monoidal `†`-functor `Corr_A^tr(S) → Corr_A^tr(T)` (since `J` is a
  `†`-algebra homomorphism), with the trace comparison (8A.12) and
  `M`-invariance; and the restriction `R_{TS} := (π_{TS})_*` (integration over the
  compact kernel), also a `†`-algebra homomorphism with `R∘J = id`, which does
  **not** preserve traces (say so, with the reason: `j_{T,p}` places `p^{−k}` at
  the new coordinates, not the average).
* **A.2**: re-read the ledger line; state exactly what is proved for the
  stable category on the colimit (closure under the declared completion,
  "more than the two rulings" — the primitive sector is nonzero, Thm 9.12).

---

## 5. What must NOT be claimed

* `𝓝_∞ = 0` for the colimit. Per chart `𝓝_S = 0` (Thm 9.8). For the colimit,
  `F ∈ 𝓝_∞` iff `f_𝔠 ⋆ 𝒯_{∞,𝔠} = 0` for every component, `𝒯_∞ := cδ + K_∞ +
  Σ_{all p}(log p)Σ_{m≠0}p^{−|m|/2}(phase)δ_{m log p}` — a uniqueness statement for
  a convolution equation with an exponentially growing arithmetic kernel. It is
  true, but the lead's proof uses the analytic continuation of `−ζ'/ζ` and the
  Riemann–von Mangoldt zero count against the Cartwright zero bound for `f̂`:
  **classical input about zeta zeros, forbidden in A by A.10**. Record it as a
  Remark labelled `CLASSICAL / belongs to row C`, and note that no clause of A
  needs it (A.6 is per chart).
* Any Hodge-index sign. Add to §14.1 the support-window remark: `W_p(k) = 0` when
  `log p > radius(k)`, so on tests of radius `< log ℓ_next(S)` the chart form
  `I_A^S` equals the colimit form `I_∞` exactly, and beyond that window the
  finite-`S` positive index of Thm 14.1(b) is a chart artifact. The sign is a
  purely global statement (rows B/D).
* That `Φ_det` carries `Tr_A` to `λ_per` (§1.1).

---

## 6. §11bis and the label

Re-assess §11bis item 4 after the above: the bidegree **is** supplied
(`M(E_a) = (|a|^{−1/2}, |a|^{1/2})`, the half-density-normalized Frobenius
bidegree `(1,q)` of P123.008 (2.3)); `E_q⋆E_q^† = Δ` is the normalized
`Γ_F⋆Γ_F^t = q·Δ` of P123.021 §2 with the `q^{−1/2}` built in, so the invertible
sector is the rational span of normalized Frobenius powers — exactly the part of
`Corr(C)` Weil's proof uses (`aΔ + bΓ_F + rulings`). Effectivity of `E_q` holds
(Def 10.1). The index theorem is a sign and is excluded from A by the spec. Then
apply the closure rule §4 clause by clause and the "not a renaming" test, and
state the label the mathematics earns. If a clause remains genuinely open after
this campaign, say which and why; the lead will not accept a relabeling.

## 7. Deliverables

1. Paper 43 `main.md`: new §10.7–10.9 (A.8, the negative theorem, the source
   functor), §8A rewritten obstacles (each O-A5-* closed with proof or
   corrected), §10 (O-A7-1/2), §3.3/§8A.5 (colimit and functors), §9.3.6
   (rulings in the completion, splitting theorem, boundary radical), §9.3.2
   (Mittag-Leffler Theorem 9.7b with the contour identity), §14 verdict, §14.0
   ledger, §14.1 remark, §14.2 status, References. Every new passage marked
   `[REBUILT, phase 130]`. Complete proofs; no step by citation of this blueprint.
2. `R130_001_BUILDER_REPORT.md` in this directory: what was proved, what was
   corrected, what (if anything) stays open with the exact missing statement.
3. `scripts/`: any check scripts used (the lead's `ml_check.py` and
   `contour_check.py` are already here).
