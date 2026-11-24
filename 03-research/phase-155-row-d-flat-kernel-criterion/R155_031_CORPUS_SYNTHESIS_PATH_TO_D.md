# R155_031 — Corpus synthesis: the funnel of 155 phases and a ranked path to row D

Status: **synthesis and plan. No new theorem, no label change,
no sign for ζ beyond `T ≤ log 2`.** Every statement below is either cited to a file of record or marked
`DIAGNOSTIC` / `HEURISTIC` / `PROPOSED`.

Copy of record: `05-meta-and-planning/ABCD-CLOSURE-PLAN/PATH-TO-D.md`.

---

## §1 The funnel in one page

### 1.1 What rows A, B, C established

Weil's 1948 method for curves over finite fields has four rows. The programme built them over
`Spec Z` (Paper 42 = Arc C, phases 107–119; rebuilt on the true carrier in phases 129–132).

* **Row A — the correspondence algebra.** `04-papers/43-row-a-correspondence-algebra/main.md` (phase 130).
 A determinant Banach algebra `𝓐_tr` with a canonical trace on the idele class group, `𝓝 = 0`,
 rulings existing in the completion and splitting canonically, a Mittag-Leffler symbol with a
 universal Tate residue, and Mertens giving the global hyperbolic ruling pairing.
 Label: **`WEIL-STRENGTH-COMPLETE` on the declared carrier** (record `R130.005`; `A.8` amended,
 accepted phase 133).
* **Row B — the Frobenius family.** `04-papers/44-row-b-arithmetic-family/main.md` (phase 131).
 `Frob_n` as Haar measures of fixed-point strata, an inverse semigroup graded by prime sets, an
 integral shadow `Sh_Z`, two Gram forms — the Weil kernel *is* the Gram form of `Frob ⋆ Δ^rad` —
 and `vol(Z_p^×) = log p` forced by the universal Tate residue.
 Label: **`WEIL-STRENGTH-COMPLETE` on the declared carrier** (`R131.019`). No sign, no zeros.
* **Row C — the explicit formula.** `04-papers/45-row-c-explicit-formula/main.md` (phase 132).
 The Weil explicit formula **proved inside the repository** (Thm 9.4), the comparison theorem
 `T_∞(Γ_{F⋆F†}) = 2Φ_F(0)Φ_F(1) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`, `c = 0` derived, Tate poles by residues of
 the continued Euler-product symbol, and **sufficiency of primitive tests** (Thm 10.4).
 Label: **`WEIL-STRENGTH-COMPLETE` on the declared carrier** (`R132.007`). No sign.

The carrier is declared, the trace exists, the family exists, and the trace formula is proved *in
the repository*, not imported. Rows A–C are exactly Weil's rows (a)–(c) and they carry **no
inequality**.

### 1.2 What row D is, exactly

Row D is the **sign**. On the declared carrier it is the positivity of the Hermitian/Weil form:

> `RH ⟺ ∀T: W_T ≥ 0 on L²(−T,T) ⟺ ∀T: 𝔞_T ≥ 0 on P_T`,

where (Paper 46 §1, eqs. (1.1)–(1.3))
`𝔞_T(F) = (1/2π)∫ σ_T(τ)|F̂(τ)|² dτ`, `σ_T(τ) = m(τ) − Σ_{n∈N_T} v_n cos(τ log n)`,
`m(τ) = Re ψ(¼ + iτ/2) − log π`, `v_n = 2Λ(n)/√n`, `N_T = {n ≥ 2 : log n < 2T}`, and
`P_T = {F : ∫F e^{t/2} = ∫F e^{−t/2} = 0}` is the primitive subspace (Paper 45 Thm 10.4;
Bombieri 2000 Thm 1). Equivalently, on the intersection-theoretic side: `RH ⟺ 𝔏 = −Π²(W_fin + ω_∞)`
positive definite (Paper 47 §5, `RESTATEMENT`), a Hodge-index inequality on the adelic square.
Unconditional positivity is known for `T ≤ log 2` (Paper 42; Yoshida 1992; Bombieri 2000) and,
by certified matrix computation, at support `1.6` (Zhu, arXiv:2608.24827). **Nothing beyond.[amended per R156_004 A14: this is proved for the PRIMITIVE form on `P_T` only (Paper 42 is primitive-only; Yoshida/Bombieri give the complete form only for `T ≤ ½log2`). Complete form `λ^W ≥ 0`: `T ≤ ½log2` classical, `(½log2, 0.8]` Zhu 2026 Thm 1.2, cited not re-verified.]**

### 1.3 The successive reductions, phases 134–155

| phase | reduction | label of record |
|---|---|---|
| 134 | Target boxed; `Π` a bijection onto the primitive class; swap law for `Σ(T)`; Thm 5.8 (finite inertia uninformative at small ε); five negatives, requirements (R1)–(R5) | `R134.007`, no label |
| 135 | **Canonical class `K`** (Pólya), Weil completion, affine duality `σ_K`, **Hodge-index transfer theorem** (conditional on an `h⁰`), `Ξ_a` falsifier theorem | no label |
| 136 | **The map**: five wall-maps over the whole corpus; `MAP_1_WALLS_AND_MASTER_DOCS.md`; sign = polar/Frobenius coupling; campaign S1–S4; `NOTE_OFF_THE_PAGE_CANDIDATES.md` (D-HS, D-θ, D-K) | map only |
| 137–138 | Canonical coupling; **detecting cones**: primitive sector = `I_∞`-orthocomplement of the hyperbolic plane `Λ = span(K, K_odd)` (Thm D.15.1); polar block satisfies Hodge identically (does not detect); `RH ⟺ W(h_T) ≥ 0 ∀T` one-parameter Landau criterion | no label |
| 139–146 | **Frame defect theorem** (no `h⁰` with (a),(b′),(c) for `ξ`, given simplicity of the first zero); cosh bound, `s₁ = 0.99846`; trace-positive cone + unconditional transfer theorem for it; fixed-index equivalences; function-field model with sharp constant `√(7/11)`; ideal-indexed Frobenius family + bidegree no-go; coupled degree form (zero-blind). **Conclusion of record: within the intersection-theoretic frame every construction is a restatement; the missing ingredient is an additive ring of correspondences.** | no label |
| 147–149 | Galois group ring inert at ζ; mixed effectivity is tropical, cone unchanged; **the additive pencil**: Deligne extraction = a Hölder inequality, `κ(d) = d/φ(d)`, exponents add on the additive square and subtract on the multiplicative; **(P149) = the k-tuple conjecture** | no label |
| 150 | **Method theorems**: **T5 PROVED** (no single-fibre extraction from any `L²`-orthogonality moment, uniformly in moment order/family size/type); **T4 downgraded → the classical polar-at-zeros / entire-at-zeros classification** (Thms 27.10–27.11); **T3 conditional** on (H-DMV), blocking O-150.1 | `R150_005` |
| — | **Decisions : row D CLOSED IN THE MAP.** Paper 47 Part IV §§24–28; the wall = T1 + T2 + T5 + the polar/entire classification (§28.2); six-clause reopening criterion (§28.4) | no label, no sign |
| 151 | T6: no nonnegative family supplies Deligne's a priori pole over `Z`; ascent `σ_{2k} ≥ 2kσ_2` | `R151` |
| 152 | Round 0 on two never-analysed mechanisms (FUP/resonances; Berkovich–Poineau): Prop A.4 (Gauss-map branch series has abscissa `Re s = ½`), Prop B.3 (tree potential theory is per-branch, blind to cross-place coupling). No route, no impossibility | `R152_005` |
| 153 | **First sign-carrying theorem.** **Theorem A** (`A_T^{(a)} = E_{−a}A_T E_a + E_a A_T E_{−a}`: the falsifier's form is a *cross term*, never a sum of squares) ⟹ **D.12-α PROVED at `(S,T) = ({∞,2,3}, log 2)`**: a finite window separating ζ from `Ξ_a` by a sign. `T*(a)` detection threshold. Closed negative: single-pair detection, the needle, Slepian/origin-gap, projection-only arguments (round 6: `W_T` is not the `cos(π/m)` box, deficit 1.28 vs truth 1e−7) | `R153_005/010/017/021` |
| 154 | **Dual-certificate theory → Paper 46.** Archimedean multiplier is a **Lévy exponent** (complete Bernstein in `τ²`, density `½/sinh + ½/cosh`) (Thm S, Thm A); **Theorem D1** strong duality with outside-window atomic certificates; **Theorem O** non-attainment; **Theorem E** exponential columns exhaust; **Theorem W** Wiener–Hopf E–L; **Prop P** `β = (2,0)` = the polar multiplier; tail lemmas F1/T/Hybrid; **Theorem C(½log3): λ_min ≥ 8.8577·10⁻⁵** by a 437-atom explicit certificate; **Theorem V′** (`Θ(log R)` mass–value exchange, kills mass-based rates); **Theorem Z: the dual certificate *is* the explicit formula on `w(u)cos(τu)`, its value `Σ_ρ ŵ(τ−γ_ρ)`; RH ⟺ a one-sided flat-top smoothing of the zero measure exists for every window** | `R154_012/030/031` |
| 155 r1–2 | **Theorem TK** (Toeplitz ceiling: `c ≤ λ_min(C_M(τ₀,β))`, class ceiling depends only on `M`); **Theorem N** (`Ceil(8, ½log3) ≤ −5.70e−3`: no lattice class `M ≤ 8` certifies at ½log3); **Theorem B** (a priori `|β|` box); **Theorem SC** (any non-negative sub-comb of mass `A < 5.372` is eventually negative — *positivity is collective, never prime by prime*); **Lemma R / Cor** (no non-trivial flat-top `w` has `ŵ ≥ 0` — positivity is never termwise in the zeros); **Theorem R** (ceilings → `λ^P`); `thm:finZ` (**no finite zero set carries a flat-top certificate**), `cor:infinite` (row D is intrinsically infinite); Bernstein grid lemma; smoothness/far-zero lemma | `R155_010/018` |
| 155 r3 | **Two archimedean thresholds** (Prop arch): `A_∞` alone becomes indefinite; `T*_∞ ≤ 0.3716` (L²), `T*_{∞,P} ≤ 0.5958` (on `P_T`) — **below `T*_{∞,P}` primes are a COST, above it primes are NECESSARY**; **Theorem N′** (no lattice class `M ≤ 24` certifies at `0.68` or `log 2`, 32 interval enclosures); **Theorem 3.3ᴾ** (concentration radius); **Schur reduction + parity splitting** (Prop 3c.1); **Theorem 3c.3**: `W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]` for one archived even degree-17 direction — *one direction, not a sign*. **The obstruction at log 2 lives in the even Schur complement near the 3rd archimedean eigenvector, and is pure cancellation.** | `R155_029` |

Files: `04-papers/47-intersection-frame-defect/archive/main.md` (Parts I–IV, §28 = the wall),
`04-papers/46-row-d-sign-radial-intersection-form/main.tex` (36 pp.),
`03-research/phase-13x…15x-row-d-*/R*_LEAD_CLOSING_DECISION*.md` (documents of record).

---

## §2 The walls, de-duplicated and classified

### 2.A Theorems — cannot be crossed by objects of their own class

| # | wall | statement | class it forbids | source |
|---|---|---|---|---|
| W1 | **T1, field uniformity** | No derivation of the Hodge-index inequality from properties shared by every `ξ_K` is sound short of GRH for all `K` | every argument not naming a property separating `ξ` from all `ξ_K` | P47 Thm 18.1 |
| W2 | **T2, the Epstein constraint** | A1–A6 + A2⁺ + `𝔇` do not yield the inequality (`Ξ_Q` satisfies them and fails); so **A3 and at least one of A7/A8/A9 must be invoked**; A9 carries the Siegel-zero price | axiom-only derivations | P47 Thm 18.16, Cor 18.17 |
| W3 | **T5** | No single-fibre extraction from any `L²`-orthogonality moment bound, uniformly in moment order, family size, family type | the whole Deligne-extraction route over `Z` | P47 Thm 27.3–27.4 |
| W4 | **polar-at-zeros / entire-at-zeros** | The sign *is* `ψ(x) − x ≪ x^{1/2+ε}`, a partial-sum bound for a polar-at-zeros sequence, hence **equivalent** to the zero bound; entire-at-zeros sequences carry no zero information | any "power saving ⟹ RH" argument | P47 Thm 27.10–27.11 |
| W5 | **frame defect** | No `h⁰` with (a),(b′),(c) exists for `ξ` given simplicity of the first zero; holds also on a curve over `F_q` where RH is a theorem | intersection-theoretic `h⁰` constructions | P47 Thm 19.25, 21.15 |
| W6 | **non-attainment (O)** | No finite `ν` and no finite family of continuous multipliers attains the dual supremum, even purely archimedean. Primal attained (Bombieri Thm 3) / dual never attained | "certificate as an identity"; any closed-form exact dual | P46 Thm O |
| W7 | **V′, log exchange** | Primal mass pushed past `R` exchanges against value at exactly `Θ(log R)` | every mass-based / radius-based rate lemma uniform over the feasible set | P46 Thm V′ |
| W8 | **TK / N / N′** | Ceiling `Ceil(M,T) = sup_β inf_{τ₀} λ_min(C_M)`; `Ceil(8, ½log3) < 0`; `Ceil(M ≤ 24, 0.68) < 0` and `< 0` at `log 2` | all lattice certificate classes of order `M ≤ 8` (½log3), `M ≤ 24` (0.68, log 2) | P46 Prop TK, Thm N, Thm N′ |
| W9 | **finZ** | No finite symmetric zero multiset carries a flat-top certificate; every truncation of `Σ_ρ ŵ(τ−γ_ρ)` at height `Γ` goes negative (at `|τ| ≳ Γ/2`) | *all* finite-zero-data arguments; row D is intrinsically infinite | P46 thm:finZ, cor:infinite |
| W10 | **non-termwise (Lemma R)** | No non-trivial flat-top `w` has `ŵ ≥ 0` | any termwise-in-the-zeros certificate | P46 lem:Rrig, cor:nontermwise |
| W11 | **SC, collective positivity** | Any non-negative sub-comb of mass `A < 5.372` is eventually negative, with explicit `T₀(A)` | "positivity prime by prime"; the "ten random primes" question answered negatively | P46 Thm SC |
| W12 | **envelope / pointwise** | `A_T` is the exact sup of the prime comb, `A_T ∼ 4e^T`; the pointwise threshold `2πe^{A_T}` cannot be lowered — doubly exponential in `T` | pointwise-envelope closing arguments (independently Zhu Thm 1.4) | P46 Prop env |
| W13 | **circularity / no-go on the zero side** | The zero side alone cannot decide the sign; zero-side LP learns a universal profile that is negative at all 103 windows because its effective order `M ≈ 4.4` sits inside Theorem N's impossible class | zero-side-only reverse engineering | Paper 08; `R155_010`, `R155_018` |
| W14 | **no ring of correspondences** | Five independent mechanisms close five enlargements of the frame (no ring on `Spec Z`; where a ring exists it is invisible on the radial carrier; where a carrier sees it, it acts away from the zeros; full-square positivity constraints are vacuous or infinite; the additive coinvariant block is computable but zero-blind) | all frame enlargements tried in phases 147–149 | P47 §28.4 record |
| W15 | **non-induction in `T`** | `λ^P` is non-increasing in `T`, new contacts enter at `T = ½log n`; a certificate at `T` says nothing about `T' > T` | bootstrap-upward arguments | P46 Cor mono, §8.3(4) |

### 2.B Conjectural

* **Zhu's Landau–Widom law** (`Conj. 12.1`, arXiv:2608.24827): `−log λ^P ≍ e^{2T}`, `T* = 2πe^{2L}`.
 If true, the effort in Problem A grows at least like `e^{2T}`: finite for each `T`, **never uniform**.
 Cited in P46 §8.4 as the reason the dual method cannot itself supply uniformity.
* **(H1)** `n₋(A_∞|P_T) = 1` on `(T*_{∞,P}, 0.80]` — computed, **not proved** (`R155_029` §1).
* **(H-DMV)** blocks T3; O-150.1 (read Diamond–Montgomery–Vorhauer 2006) still open (P47 §28.3 item 41).
* The even-sector obstruction data at `log 2` (`w₁₁/λ_min`, failure of the crude condition by
 1.07–1.49, 99.46 % of the `S` ground state on the 3rd archimedean eigenvector) — all `DIAGNOSTIC`.

### 2.C Computational (a solver/budget limit, not a theorem)

* Two-prime windows: best certified value at `T = 0.58` is `−3.18e−3` against a Galerkin upper bound
 `2.16e−4`; column-generation LPs unconverged for `M ≥ 32`; clustering **refuted**; the wall there is the
 atom budget `M`, and after Theorem N′ it is *also* a theorem for `M ≤ 24`.
* `T*_∞ ≤ 0.3716`, `T*_{∞,P} ≤ 0.5958` are Galerkin **upper** bounds; a certified lower bound needs a
 Temple/Kato instrument (round-4 order (d)).
* Local heavy compute is forbidden by rule; off-machine package in `scripts/offmachine/`.

### 2.D How phases 154–155 relate to the phase-136/§28 wall

**They are a different formulation of the same obstruction, in a language where the obstruction is
now *localised and quantified* rather than only classified.** Precisely:

* **Same wall.** Theorem Z says the dual certificate *is* the explicit formula; Corollary `cor:zeros`
 says every certificate is an unconditional statement about the zeros; so a certificate for all `T`
 is `ψ(x) − x ≪ x^{½+ε}`, which is W4 verbatim. Theorem Z therefore does **not** evade §28.2: it
 re-expresses it. Likewise W6 (non-attainment) is the analytic shadow of W5 (the frame defect):
 both say "no finite/closed object realises the required invariant exactly".
* **New information the dual theory adds that §28 did not have.**
 (i) The wall is *finite per window and decidable* (P46 Prop decide) — the difficulty is exactly
 **uniformity in `T`**, nothing else. §28 did not isolate that.
 (ii) The wall is *located*: the work lies in `[2πe^{2T}, 2πe^{A_T}]`, at the ordinates where the
 prime phases `τ log p` are nearly aligned mod `2π`. §28 gave no interval.
 (iii) The wall has a *proved sign flip*: below `T*_{∞,P}` the archimedean form alone is positive on
 `P_T` and primes are a cost; above it the primes are **necessary**. That is a structural statement
 about *which* ingredient must do the work, and it is new (round 3, `R155_029` §2.2).
 (iv) The impossibilities are now *class-indexed with explicit ceilings* (TK/N/N′) instead of being
 "the optimiser failed".
* **Conclusion of record.** Rows 136 and 154/155 are two coordinate systems on one wall. The dual
 theory does not lower the wall; it tells you where on the wall to stand, and it proves that the
 standing place is arithmetic (W11 + the `T*_{∞,P}` flip), not analytic.

---

## §3 Where the solution must live

### 3.1 Necessary features of any proof of D for ζ — derived from the proved record

1. **Never termwise in the zeros.** `Lemma R`: no flat-top weight has `ŵ ≥ 0`. A certificate is
 always a statement of *cancellation across zeros*.
2. **Never termwise in the primes, and never a sub-family.** `Theorem SC`: any non-negative sub-comb
 of mass `< 5.372` eventually goes negative. Positivity is **collective over the full initial
 segment** of the comb.
3. **Collective over an infinite zero set.** `thm:finZ` + `cor:infinite`: no finite zero set carries a
 certificate; truncating at height `Γ` produces negativity at `|τ| ≳ Γ/2`. Row D is intrinsically
 infinite; no amount of computed zeros is a proof or even a fair model.
4. **The primes must supply positivity past `T*_{∞,P} ≈ 0.596`.** Below it the archimedean form on
 `P_T` is already positive (≈ 0.083 at ½log3) and Theorem C pays for the primes; above it the
 archimedean deficit is `η_P ≈ 0.154` and the prime term on the archimedean ground state is `0.188`.
 **Any construction of D at `log 2` and beyond must USE the prime atoms** — which is why the
 comb-vanishing class (`R155_016`) failed structurally.
5. **The certificate must be a one-sided smoothing of the full zero measure** (Theorem Z,
 Cor RH): `∃ w_T` flat-top with `Σ_ρ ŵ_T(τ − γ_ρ) ≥ 0` on `ℝ`, for every `T`.
6. **The high-frequency regime is PROVED, for every window**: for `|τ| ≳ 2πe^{A_T}` the archimedean
 `m(τ) ≥ log(τ/2π) − 1/τ − 1/2τ²` beats the bounded comb (`|comb| ≤ A_T`) — P46 Lemma 4.1, Prop env.
 Nothing remains to be done there.
7. **The low-frequency regime is a finite, decidable problem per window** (Prop decide) with
 **exponentially small margins** (`λ ≈ 1e−3` at ½log3, `≈ 1e−7` at log 2; `−log λ^P ≍ e^{2T}` if Zhu's
 law holds).
8. **Class-dependent LOWER bounds are the missing half.** Rounds 1–3 of phase 155 are *entirely*
 upper-bound-side (TK, N, N′, ceilings). Problem A — an explicit `D(T,d,U) → 0` with
 `c(T,d,U) ≥ λ^P − D` — is untouched. That is the tractable half of the whole enterprise.
9. **It must name a property separating `ξ` from every `ξ_K`** (T1) and must invoke A3 and one of
 A7/A8/A9 (T2). In the analytic language: the proof must use `Λ(n) ≥ 0` and/or the zero-free line
 `Re s ≥ 1` at a load-bearing step, not merely the functional equation and the pole. **[amended per R157_004: T1 does not forbid a field-uniform proof — such a proof is admissible and proves GRH for all K (P47 Rem 18.1a); what T1 excludes is a derivation from properties shared by all ξ_K that stops short of GRH for all K. T2 (A3 + one of A7/A8/A9) stands.]**
10. **It cannot be an induction upward in `T`** (W15), a mass-based rate (W7), a pointwise envelope
 (W12), or an identity (W6).

### 3.2 Formulations in which D has NOT yet been attacked (grep-confirmed)

| # | formulation | corpus status (grep) | verdict |
|---|---|---|---|
| (i) | **Problem A lower bound on the archimedean form alone.** `A_∞|P_T` is explicit (Lévy energy `C₀ + ∫(‖F‖²−c_F)K`, `K` completely monotone), contains no primes, and its class-dependent lower bound is a pure one-sided-approximation question | ordered as round-4 (c) in `R155_029`, **never attempted**; all of rounds 1–3 are ceilings | **OPEN, tractable, highest value** |
| (ii) | **Operator-theoretic / Hilbert–Pólya: `A_T` as a compression of an explicit self-adjoint operator on the declared carrier, positivity via a spectral realisation (Connes–Consani semi-local)** | Connes–Consani appears in phases 130, 135–137, 140 as *comparison and import*; the semi-local trace formula is read (`cc_2006.13771_text.txt`) but no realisation of `A_T` as a compression of a carrier operator with independently proved positivity was ever built. Paper 08's no-go is about the **zero side**, not about this | **OPEN**, but note the frame-defect wall W5 applies to any `h⁰`-style invariant; the realisation must be analytic, not intersection-theoretic |
| (iii) | **The even-sector Schur complement as an operator whose positivity follows from a structural identity** (3rd archimedean eigenvector coupling to the atoms `v_2`, `v_3`) | Prop 3c.1 built the reduction **, one day old; the even sector's ground state is characterised only `DIAGNOSTIC`ally (99.46 % on the 3rd archimedean eigenvector); **no identity attempted** | **OPEN, one round old, exactly at the obstruction** |
| (iv) | **de Branges / Kreĭn: the flat-top certificate as a Kreĭn extension problem in the indeterminate case** | `R155_014` §2.1 states the equivalence explicitly and notes Kreĭn's theorem does *not* forbid the extension; Remark 2.5 says finite zero sets are the **determinate** Carathéodory–Fejér/Kreĭn case (that is `thm:finZ`), and that for ζ "the extension problem is indeterminate at every scale" — but that sentence is **labelled `HEURISTIC`** (amended per `R155_015`). P46 open item (5) is exactly "the distributional Kreĭn extension route to Theorem D1" | **OPEN**; the determinate/indeterminate dichotomy is the right frame and has never been proved for ζ. Caveat: indeterminacy is *necessary*, not sufficient — see §4 |
| (v) | **Li/Keiper coefficients or Báez-Duarte-type sequential criteria recast as dual certificates** | Li–Keiper is the endpoint of Paper 36 (the corpus's *other* culmination) and appears in the row-D phases only in the phase-136/138 maps as history. **Zero hits in phases 147–155.** Báez-Duarte: no hits anywhere in the row-D arc | **OPEN and structurally attractive**: it is the one move that would connect the corpus's two culminations (36 and 42/47) in one language |
| (vi) | **Arithmetic-geometry side (phase 149 additive pencil, Deligne route)** | Corpus concluded: the Deligne extraction is a Hölder inequality; `κ(d) = d/φ(d)`; exponents add on the additive square and subtract on the multiplicative; **(P149) = the k-tuple conjecture**; **T5 PROVED** kills single-fibre extraction from any `L²` moment; T6 (phase 151) kills every nonnegative family | **CLOSED as a route.** The dual-certificate language does **not** change it: Theorem Z shows a certificate is `ψ(x)−x ≪ x^{½+ε}`, i.e. W4, which is what T5/T6 were already saying. *One residue survives*: the never-run kill tests T1–T5 of candidate **D-HS** (fibrewise Connes–Consani `h⁰` on the `S`-square with Frobenius transport, `NOTE_OFF_THE_PAGE_CANDIDATES.md` §1) — but it must first clear the frame defect theorem W5, which post-dates that note |

---

## §4 The path: ranked theorems to attempt

Ranking key: **(a)** probability of a *proved statement* in one round; **(b)** distance moved toward D.
"PM" = pure math, no compute. "PM + ε" = pure math with a small certified enclosure.

---

### P1 — Problem A restricted to the archimedean form (`A_∞|P_T`) — **rank 1**
**Statement (to prove).** For the lattice class of step `d = 2T/M`, range `U`, with the F1 tail rows,
and for the *prime-free* symbol `m(τ) + β·ĝ`, exhibit an explicit `D_∞(T,d,U) → 0` as `d → 0, U → ∞`
with `c_∞(T,d,U) ≥ λ^{∞,P}(T) − D_∞(T,d,U)`. Equivalently: a quantitative one-sided `L¹(μ⋆)`
approximation theorem for `−m − β·ĝ + λ^{∞,P}` on `[0, 2πe^{0}]` by `P`-periodic trigonometric
polynomials with vanishing low modes `|j| < M`.
**Why now.** It is the **first lower-bound statement of the whole programme** (§3.1 item 8). `m` is
explicit, completely-Bernstein in `τ²`, with a completely monotone Lévy density — the best-behaved
symbol that will ever appear. Theorem R says the ceilings converge, so a matching lower bound is not
excluded by anything proved. Theorem V′ says `D` must depend on the *class*, not on a radius: the
statement above respects that.
**Success.** An explicit `D_∞`. Then (a) the fixed-`M` lossiness question of Theorem R is answered,
(b) Theorem C becomes a *construction* rather than a found object, (c) the same proof template
transfers to `σ_T` by adding a bounded comb perturbation of sup `A_T`.
**Failure.** A proof that no class-dependent lower bound exists even for `m` alone — a structural
negative of first importance (it would mean Problem A is false as stated and the dual route is
closed as a *method*, not just as a computation).
**Difficulty.** Moderate–hard. This is one-sided approximation with a gap condition on low modes; the
literature to mine is Beurling–Selberg / Vaaler one-sided approximation and Cohn–Elkies LP duality.
**Type.** PM.

---

### P2 — The even-sector Schur complement at `T = log 2` — **rank 2**
**Statement (to prove).** With the parity splitting `S = S_even ⊕ W|V_odd` of Prop 3c.1 and the pivot
`w₁₁ > 0` (Thm 3c.3), characterise the ground state of `S_even` analytically as
(3rd archimedean eigenvector) + (explicit correction of order `v_2, v_3`), and prove
`λ_min(S_even) > 0` at `T = log 2` by a structural identity coupling that eigenvector to the two
prime atoms.
**Why now.** `R155_029` §2.3: positivity at `log 2` **splits** into one cheap direction (now PROVED)
and the Schur complement on `V`, and *every class impossibility proved so far obstructs only the
second part*. This is the exact locus of the obstruction, freshly isolated and one day old. It is
also the only place where the `T*_{∞,P}` sign flip can be exploited: the primes are *necessary*
there, and the 3rd archimedean eigenvector is where they act.
**Success.** An independent, non-Galerkin proof of positivity at `log 2` — the endpoint of Paper 42
reproved by a decomposition that *generalises in `T`*. That would be the first structural (not
computational) positivity proof in the arc and the first plausible generator of uniformity.
**Failure.** An obstruction theorem: the even-sector cancellation has no margin and no identity
explains it (record it; it is `DIAGNOSTIC` today — the crude condition fails by 1.07–1.49 and the
ideal even-sector condition by 0.064–0.310).
**Difficulty.** Hard, but bounded: two prime atoms, one explicit archimedean operator, finite rank.
**Type.** PM, with at most a certified enclosure of two constants.

---

### P3 — (H1): the archimedean form has negative index exactly one above `T*_{∞,P}` — **rank 3**
**Statement (to prove).** `n₋(A_∞|P_T) = 1` for `T ∈ (T*_{∞,P}, T₂]`, with `T₂` explicit; by min–max
against the band `|τ| < τ₀ = 6.2898` where `m < 0`.
**Why now.** If proved, the Schur/Feshbach reduction of P2 becomes **rigorous and rank-one**: the
whole low-frequency problem at each window collapses to a *single scalar inequality* (one pivot, one
complement). It converts a numerical splitting into a theorem, and it is the natural Pontryagin/Kreĭn
index statement the corpus has circled since Papers 08/11/18/25 without ever proving it for `A_∞`.
**Success.** `n₋ = 1` with explicit `T₂` ⟹ P2 becomes a one-dimensional problem.
**Failure.** `n₋ ≥ 2` somewhere ⟹ the reduction is not rank one and P2 must be run on a subspace;
still informative.
**Difficulty.** Moderate. Min–max with an explicit multiplier and an explicit negative band; the hard
part is the upper bound on the count on `P_T`.
**Type.** PM + ε (one enclosure).

---

### P4 — A dictionary theorem: Li/Keiper and Báez-Duarte criteria as flat-top dual certificates — **rank 4**
**Statement (to prove).** Exhibit a map from the Li–Keiper coefficients `λ_n = Σ_ρ [1 − (1−1/ρ)^n]`
(and/or the Báez-Duarte sequence) to weights `w` in the flat-top class `𝒲_T`, such that
`λ_n ≥ 0 ∀n` ⟺ `Σ_ρ ŵ_n(τ − γ_ρ) ≥ 0` up to an explicit error, and identify what the `λ_n` are as
*dual variables*: which `ν`, which `β`, which window.
**Why now.** This is the **only unattempted move that connects the corpus's two culminations** —
Paper 36's fifteen-step Pick/Nevanlinna chain ending at `λ_n ≥ 0`, and Paper 42/47's row D. Grep
confirms zero Li–Keiper work in phases 147–155. Theorem Z makes the translation *possible* for the
first time: every certificate is now known to be an explicit-formula evaluation, so any classical
zero-sum criterion is a candidate certificate in disguise. A dictionary would import Paper 37's
sixteen recorded positivity-transfer witnesses and Paper 38's FIR criteria straight into the dual
language, at no cost.
**Success.** A proved dictionary. Best case: the `λ_n` supply a *class* of certificates with a known
lower bound, attacking Problem A from the classical side.
**Failure.** A proved mismatch — e.g. that `λ_n`'s implied weight is not flat-top, or has a
non-decaying tail and so falls outside `𝒲_T`. That is itself a clean no-go and closes a long-standing
ambiguity between the two arcs.
**Difficulty.** Moderate. Mostly bookkeeping on the explicit formula; the risk is that it is *only*
bookkeeping.
**Type.** PM.

---

### P5 — Kreĭn indeterminacy for the ζ zero set — **rank 5**
**Statement (to prove).** For `Z` = the full zero multiset of `ζ` and every `T > 0`, the
positive-definite datum `g_Z|[−2T,2T]` is in the **indeterminate** case of the Kreĭn extension problem
(equivalently: the associated Toeplitz forms have full rank at every scale and no finite linear
recursion propagates), so that the finZ obstruction *provably does not apply*.
**Why now.** `R155_014` Remark 2.5 identifies this dichotomy as the answer to the the question,
but the ζ half is explicitly labelled `HEURISTIC` and the citation is unverified. P46 open item (5)
is the same route. Proving indeterminacy would convert `thm:finZ` from a bare negative into a
**dichotomy theorem**, and would make precise why the finite-zero intuition is not merely
insufficient but structurally inapplicable.
**Success.** A dichotomy theorem plus, in the best case, a de Branges-space model of the flat-top
class making the certificate an extension rather than an optimisation.
**Failure / limit — state this plainly.** **Indeterminacy is necessary, not sufficient.** Proving it
does *not* produce a certificate; it removes one obstruction. This item can only yield structure and
a negative-removal, never the sign. Rank it accordingly.
**Difficulty.** Moderate (indeterminacy for a non-lacunary infinite exponential sum is likely to be
routine once set up properly).
**Type.** PM.

---

### P6 — The alignment-band lower bound: what the primes must be proved to do — **rank 6**
**Statement (to prove/formulate sharply).** On the band `[2πe^{2T}, 2πe^{A_T}]`, at the ordinates where
`Σ_{n∈N_T} v_n cos(τ log n) > m(τ) ≈ log(τ/2π)` (Kronecker-dense by construction), prove a lower bound
for the smoothed prime sum `−2Re Σ_n Λ(n) n^{−½−iτ} w(log n)` beyond what the trivial envelope gives.
Even a *conditional* sharp statement — "D at window `T` follows from bound X on the comb at alignment
ordinates, and X is not implied by PNT/zero-density" — is a result.
**Why now.** P46 §8.4 verdict: "the interval between the two scales is where a proof must say
something new about the primes", and §8.3(5) proves that any prime-side inequality there *is* a
zero-side inequality. This item names the arithmetic input the whole arc has been circling.
**Success.** A clean conditional reduction: D ⟸ X, with X an isolated arithmetic statement.
**Failure — likely and expected.** X turns out to be RH-equivalent (this is what W4 predicts). Then
the item has still produced the **exact** arithmetic content of the sign, which §28.2 states only
qualitatively. **Be explicit with : P6 is the item most likely to yield only a negative or
an equivalence, and it should not be run before P1–P3.**
**Difficulty.** Hard.
**Type.** PM.

---

### P7 — D-HS kill tests, run against the frame defect theorem — **rank 7, negatives only**
**Statement.** Run kill tests T1–T5 of `NOTE_OFF_THE_PAGE_CANDIDATES.md` §1 on the fibrewise
Connes–Consani `h⁰` with Frobenius transport (`h⁰(mK) ≳ m²/4`?), and check first whether the frame
defect theorem (P47 Thm 19.25, and Thm 21.15 on the curve) already excludes it.
**Why.** It is the one arithmetic-geometry candidate in the corpus never built; its tensor-square reading was already refuted in phase 140 (Prop D.24.10, P47 §19bis), and the fibrewise reading was killed in round 8 (`R155_054`, audited `R155_057`) [amended ]. But
it was proposed in phase 136, *before* the frame defect theorem, and W5 is likely fatal.
**Success.** Almost certainly none. **This item can only yield a negative**, and its value is closing
the last open square of the geometric arc so that §28.4's six clauses can never be reopened by it.
**Difficulty.** Low, once W5 is applied.
**Type.** PM. Run it as hygiene, not as a hope.

---

**Sequencing recommendation.** Round 4 = **P1 + P3 in parallel** (independent, both pure math, both
lower-bound-side); round 5 = **P2** using P3's output; round 6 = **P4**; P5 and P7 as low-cost
side-tracks; **P6 last**, with the negative expectation stated in advance.

---

## §5 Honest paragraph for 

The map now proves something sharp about where row D lives, and it is worth stating without
decoration. Rows A, B and C are finished on the declared carrier: the algebra, the Frobenius family
and the explicit formula are all in the repository, proved, and none of them contains an inequality.
Row D is the inequality, and after phases 134–155 we know its address to within a bounded interval:
everything above frequency `2πe^{A_T}` is a theorem for every window and needs no further work;
everything below `2πe^{2T}` is a finite computation about the first zeros; and the sign is decided in
the band between them, at the ordinates where the phases of the small primes nearly align. We also
know who must do the work there. Below `T ≈ 0.596` the archimedean term alone is already positive on
the primitive subspace and the primes are a cost the certificate pays for; above it — and `log 2` is
above it — the archimedean term runs a deficit and **the primes are the only thing that can create
the positivity**. That is the single most useful structural fact the last two phases produced, and
it says the remaining work is arithmetic, not analysis.

It also says, unfortunately clearly, that finding the pattern in the first `10⁸` zeros cannot
substitute for the prime-side proof. Three proved statements block that road, and they block it
independently. First, `thm:finZ`: **no finite set of zeros carries a certificate at all** — for any
flat-top weight and any finite symmetric zero multiset, the smoothing `Σ ŵ(τ−γ)` takes negative
values, so every truncation of the true zero sum at height `Γ` goes negative just outside the
evaluated range (around `|τ| ≳ Γ/2`). A computation over `10⁸` zeros is not a weak version of row D;
it is a statement whose sign is *provably wrong*, and the corpus measured exactly that in phase 155
when the zero-side LP learned a beautiful universal profile that extrapolated from regime to regime
and was negative at all 103 windows. Second, Theorem Z: the certificate **is** the explicit formula,
so a prime-side inequality and a zero-side inequality are the same statement, and a proof of it from
the zeros in that band is precisely the content the explicit formula assigns to the primes — there is
no free direction to exploit. Third, the GUE reading: the spacing statistics of the first `10⁵` zeros
agree with Wigner's surmise column by column, which is the fingerprint of a self-adjoint spectrum,
but a fingerprint is not a proof of self-adjointness, and "the pattern that yields positivity" turns
out, when computed, to be nothing more than `t_ρ = t̄_ρ` — RH itself. Add Theorem SC, which says
positivity is never prime-by-prime and never sub-comb-by-sub-comb, and Lemma R, which says it is
never zero-by-zero, and the shape of the thing is fixed: row D is collective, infinite, and
cancellative, with margins near `10⁻⁷` at `log 2`.

What the zeros can still do is real and should be used. They are an **oracle for evaluation**: Theorem
Z was checked numerically on both sides across eight regimes against Odlyzko's `10⁵` zeros, and that
check is how we know the identity is right. They **validate identities** — the Schur reduction, the
parity splitting, the `T*_{∞,P}` flip, the archimedean ground-state decomposition were all found
numerically and then proved or enclosed. And they **guide the choice of test directions**: the
archived direction `F*` at `log 2`, the third archimedean eigenvector, the contact comb visible in the
437-atom certificate — all of these came from looking at zeros and are now objects in proofs. So: use
the zeros to see, never to conclude. The conclusion has to come from the primes, in the band between
`2πe^{2T}` and `2πe^{A_T}`, and the next round should attack it from the one side the programme has
never once tried — a class-dependent **lower** bound, starting where the operator is explicit and the
primes are absent.

---

*No compute was run for this document. No label of record changes. Row D: no label, no sign beyond
`T ≤ log 2`.*
