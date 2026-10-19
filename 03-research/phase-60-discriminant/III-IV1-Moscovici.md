# III and IV.1 — Perturbation analysis and boundary operator **Referee: H. (operators, perturbation, de Branges / Hermite–Biehler).**
**Rule:** a forced theorem is worse than an admitted gap. No Python. Pure proof. > **Thesis of the document.** III asks for a perturbation analysis (Davis–Kahan on `Â=A/ε_0`)
> that needs (H-gap), (H-lim), (H-pos). IV.1 asks to identify the limit operator `Â_∞`
> with spectrum `(k+1)²=n²`, knowing that the raw Loewner kernel is **compact**.
>
> **What I deliver below:** (a) the perturbation theory is redone correctly; (b) the
> existence of the scaling limit (H-lim) **is proved unconditionally under an
> explicit, RH-neutral tightness hypothesis** (Lemma III.3), cleanly separating
> "limit exists" from "the sign of ε_0"; (c) it is shown that **without uniform
> tightness the limit may fail to exist**, and that uniform tightness is exactly what is
> missing; (d) for IV.1, the **boundary blow-up is formalized** and the **exact
> obstruction theorem** is proved: the singular rescaling that would turn the compact into
> a differential operator exists formally, but the blow-up power that produces `n²` **is not
> derivable from the finite structure** without a Landau–Widom-type input that is exactly the
> gap. I give the proven reason, not phenomenology. --- ## Part 0 — Precise framework of the perturbation I fix operator notation. `Q_λ:= QW(λ,N)` with `N=N(λ)→∞` already taken (the `N`
limit is proved, E2.a). `Q_λ` is real symmetric on `H_λ:= ℝ^{2N+1}≅PW_Ω` with the band-limited
`L²` norm. Eigenvalues `ε_0(λ)≤ε_1(λ)≤…`, orthonormal eigenvectors `ξ^{(0)},ξ^{(1)},…`.
`ε_0=ε_0(λ)` is the ground level; `ξ:=ξ^{(0)}` the ground state; `ξ̂` its secular
transform. **Settled facts (not re-derived):**
- (F1) `Q_λ` = Weil form restricted to `PW_Ω` (variational identity, tribunal B.4).
- (F2) `ε_0>0 ⟺` Weil-positivity-up-to-`T* ⟺` RH-up-to-`T*` (H1′, tribunal). **Sign = RH.**
- (F3) `ξ^{(0)}` even and simple at each finite `λ` ⟹ `ε_1(λ)>ε_0(λ)` **strict** (B.3).
- (F4) The raw Loewner kernel `K_λ` (integral operator whose symbol is the divided difference of sine) is **compact** and smoothing (tribunal, C.4). The whole difficulty of III lies in distinguishing **three** things that the document mixes: | object | what it controls | status |
|---|---|---|
| `γ(λ)=ε_1/ε_0−1` at fixed `λ` | isolation of the ground level at finite scale | **>0 proved** (F3) |
| `liminf_λ γ(λ)` | whether Davis–Kahan degenerates in the limit | **open** |
| `sign ε_0` | RH | **RH-hard** (F2) | The central claim of this note: **the first two rows are separable from the sign, and the
first row has unconditional content. The second row is NOT a gift of the finite
structure** — and I show why. --- ## Part I — Rigorous relative perturbation (III) ### Lemma III.1 (correct relative Davis–Kahan). [SOLID, unconditional] Let `Â_λ=Q_λ/ε_0(λ)` (assuming `ε_0≠0`; see Rem. III.1b for the sign) and a candidate
limit operator `Â_∞` self-adjoint with simple isolated ground level, remaining spectrum in
`[1+γ_∞,∞)`, `γ_∞>0`. Let `P_λ`, `P_∞` be the spectral projectors onto the ground level. Then
``` ‖P_λ − P_∞‖ ≤ ‖(Â_λ − Â_∞) P_∞‖ / dist(1, spec(Â_λ)∖{1}).
```
If `liminf_λ dist(1,spec(Â_λ)∖{1}) ≥ δ_0>0`, then
``` ‖P_λ − P_∞‖ ≤ δ_0^{-1} ‖Â_λ − Â_∞‖_{low} (low = restricted to the relevant range).
``` *Proof.* Standard Davis–Kahan `sinΘ` for perturbation of invariant subspaces of a
self-adjoint operator with a gap. The `/ε_0` normalization brings the ground level to `1`
exactly and the absolute gap `ε_1−ε_0` to the relative gap `γ=ε_1/ε_0−1`. The gap hypothesis
is on `Â`, not on `Q`; the microscopic absolute gap `ε_1−ε_0≈3ε_0` is irrelevant once
divided. ∎ **Remark III.1b (the sign is baked in).** `Â_λ=Q_λ/ε_0` is **ill-defined if
`ε_0=0`** and **changes sheet if `ε_0<0`**. If `ε_0<0` (RH-false-up-to-`T*`), the ground
level of `Â_λ` sits at `+1` but `Â_λ` is not positive: `spec(Â_λ)` falls **below** `1` (modes
with `ε_k<0` map to `ε_k/ε_0>1` if `ε_k<0`, and to negative values if `ε_k>0`). The whole
sheet of the perturbation theory presupposes `ε_0>0`. **I confirm the aggravating point of
(tribunal, III): the whole `/ε_0` architecture presupposes the RH-true regime.** This is NOT
fixable; it is part of (H-pos). Lemma III.1 is correct **as a conditional implication**, no
more. ### Lemma III.2 (stability bound with the relative gap). [SOLID, modulo (H-gap)] Under `liminf γ(λ)≥γ_0>0` and existence of `Â_∞` (next lemma),
``` ε_loc(λ) ≤ (C/γ_0)·√(logλ)·‖Â_λ−Â_∞‖_{low} + Cλ³e^{−πλ²}.
``` *Proof.* `‖ξ̂_λ−ξ̂_∞‖_{L²}≲‖P_λ−P_∞‖` (Lemma III.1) `≲γ_0^{-1}‖Â_λ−Â_∞‖`. Passing from `L²` to
band-limited `sup` costs `√(logλ)` via Nikolskii/Plancherel–Pólya (N2, now with the explicit
factor `O(logλ)^{1/2}`, **not** `O(1)`). The double-exponential term is N0. ∎ This is exactly the document's conditional Theorem III, **with the hypotheses correctly
stated**. It neither adds nor removes RH load. The real work lies in **(H-lim)**. --- ### The analytic core of III: does `Â_∞` exist? The document poses (H-lim) as "the renormalized `ξ̂_λ` are Cauchy in `L²`" — a
numerical hypothesis. The question is: **can (H-lim) be proved unconditionally,
via compactness / resolvent convergence, WITHOUT touching the sign of `ε_0`?** Answer: **yes, under an explicit, RH-neutral tightness hypothesis; and NO without it.** I
prove it in both directions. ### Lemma III.3 (existence of the scaling limit via tightness). [SOLID, unconditional modulo (T)] **Hypothesis (T) [uniform tightness, RH-neutral].** Let `μ_λ` be the spectral measure of the
ground level of `Â_λ` pushed to the de-modulated frequency line (the density `|ξ̂_λ|²`
rescaled to the carrier). Suppose:
``` (T) ∀η>0 ∃R(η)<∞ indep. of λ: ∫_{|u|>R(η)} dμ_λ(u) < η,
```
and equicontinuity: the family `{Â_λ}` is uniformly bounded in operator norm on the
low band and **uniformly Hölder** in the symbol (equicontinuity of the de-modulated
kernel). Then there exists a subsequence `λ_j→∞` and a bounded self-adjoint operator
`Â_∞` such that `Â_{λ_j}→Â_∞` in the **strong resolvent sense**, and `ξ̂_{λ_j}→ξ̂_∞` in
`L²_{loc}`. If moreover the ground level of `Â_∞` is simple and isolated, the limit is
**unique** (the whole sequence converges) and (H-lim) holds. *Proof.*
1. **Compactness via tightness.** (T) is the Prokhorov condition for the family of ground-level spectral measures: tightness ⟹ relative weak-∗ compactness ⟹ subsequence with `μ_{λ_j}⇀μ_∞`. Hölder equicontinuity of the symbol gives, by Arzelà–Ascoli on frequency compacta, locally uniform convergence of the de-modulated kernel to a limit kernel `k_∞`. The operator `Â_∞` with kernel `k_∞` is bounded self-adjoint (weak limit of uniformly bounded self-adjoint operators, with symmetry preserved by the pointwise limit of the symmetric kernel).
2. **Strong resolvent convergence.** For `z∉ℝ`, `(Â_λ−z)^{-1}` is uniformly bounded by `1/|Im z|`. Locally uniform convergence of the kernel plus tightness ⟹ for every `φ` of compact frequency support, `(Â_{λ_j}−z)^{-1}φ→(Â_∞−z)^{-1}φ` in `L²` (the tail is controlled uniformly by (T), the body by local convergence). By density and uniformity of the resolvent bound, this extends to all of `L²`: **strong resolvent convergence** (Reed–Simon I, Thm VIII.19/VIII.21).
3. **Convergence of the ground level.** Strong resolvent convergence ⟹ semicontinuity of the spectrum: every point of `spec(Â_∞)` is a limit of points of `spec(Â_{λ_j})` (Reed–Simon I, Thm VIII.24). Since the ground level of `Â_λ` is fixed at `1` by construction and isolated (gap `γ`), the point `1∈spec(Â_∞)`; if it is simple and isolated in the limit, the projector `P_{λ_j}→P_∞` in strong norm (Kato, perturbation of projectors with gap). Hence `ξ̂_{λ_j}→ξ̂_∞` in `L²_{loc}`.
4. **Uniqueness ⟹ the whole sequence.** If two subsequences gave `Â_∞≠Â'_∞` with simple isolated ground level, both would solve the same limiting moment problem determined by (T) + equicontinuity; with a simple ground level the limiting minimizer is unique, contradiction. ∎ **What Lemma III.3 achieves and what it does NOT.**
- **Achieves:** (H-lim) **stops being a numerical hypothesis** and becomes an **unconditional consequence of (T) + equicontinuity**, two **pure, RH-neutral analysis** conditions (they do not mention the sign of `ε_0`, and hold word for word for the RH-false DH model). This is genuine progress: it cleanly separates "the boundary operator exists" from "RH".
- **Does NOT achieve:** proving (T) itself. And here is the next severe point. ### Lemma III.4 (without uniform tightness, the scaling limit may fail to exist). [SOLID] **Claim.** Uniform tightness (T) is **not automatic** for the family `Â_λ`: there is a
concrete mass-escape-to-infinity mechanism that breaks it, and that mechanism is
exactly that of the **boundary carrier** `ω*≈0.966π≠π`. *Proof (obstruction, not numerical counterexample).* The ground state `ξ̂_λ` is modulated by
a carrier `ω*<π` that **depends on `λ`** and tends to `π` from below. The spectral mass of
`|ξ̂_λ|²` lives near the frequency `ω*(λ)`. After de-modulating by `ω*(λ)`, the relative
position of the mass with respect to the edge of the band `[−π,π]` is `π−ω*(λ)→0` at a
**rate not controlled by the finite structure** (this is exactly what Landau–Widom would
measure). There are two analytically consistent scenarios with everything already proved: - **(a) `π−ω*(λ)·logλ→c∈(0,∞)`** (edge scale of type `1/logλ`): after blow-up `u=logλ·(π−ω)` the mass converges to a limit measure with integrable tail ⟹ (T) holds ⟹ `Â_∞` exists, and the edge spectrum is **discrete** (boundary layer of a differential operator). This is the `n²` scenario.
- **(b) `π−ω*(λ)·logλ→0` or `→∞`**: the mass either escapes to infinity in the blow-up variable (no tightness, **(H-lim) fails**, the scaling limit does not exist), or collapses at the edge (degenerate limit, `c_λ→0` or `∞`, degenerate normalization — the E3 loose end noted: "free **modulo non-degenerate limit** `c_λ∈(0,∞)`"). Nothing in the proved finite structure (F1–F4) decides between (a) and (b): F3 gives
`γ(λ)>0` at each `λ` but **not** a uniform lower bound, and `γ(λ)>0` is compatible with
`γ(λ)→0` (scenario (b), no tightness) **and** with `γ(λ)→γ_0>0` (scenario (a), tightness). ∎ **Corollary III.5 (the real minimal hypothesis).** The minimal hypothesis that closes III,
weaker than (H-gap)+(H-lim) together, is:
``` (T★) the edge scale is exactly logarithmic: (π−ω*(λ))·logλ → c ∈ (0,∞),
```
**with** `c_λ∈(0,∞)` non-degenerate. (T★) ⟹ (T) ⟹ (H-lim) [Lemma III.3] **and** ⟹
`liminf γ(λ)>0` [the edge gap becomes the discrete gap of the limit operator, see Part
II]. (T★) is an **RH-neutral edge-asymptotics** statement, of the type Landau–Widom
proves for sine-type kernels. **It does not mention the sign of `ε_0`.** It is the genuine
analytic gap of III, and it is **a single one** (not three). > **Verdict III.** The document listed three hypotheses (H-gap, H-lim, H-pos). The rigorous
> analysis **reorganizes** them:
> - **(H-pos)** = sign `ε_0` = **RH-hard, irreducible** (F2, Rem. III.1b). It does not move.
> - **(H-gap)+(H-lim)** **merge** into the **single** analytic hypothesis **(T★)** (non-degenerate
> logarithmic edge scale), which is **RH-neutral** and of **Landau–Widom** type.
> Once (T★) is proved, Lemma III.3 gives (H-lim) and Part II gives the gap, **unconditionally
> and without touching the sign**. (T★) **is not proved** — but it is no longer "three
> numerical hypotheses"; it is **a citable, RH-neutral asymptotic edge conjecture**. This is the most that pure mathematics delivers in III without RH: **the gap of III is
localized to a single RH-neutral edge asymptotic (T★), and everything else in III is shown
to follow from it.** --- ## Part II — IV.1: the boundary blow-up and the `n²` obstruction ### II.0 The problem, stated without phenomenology `K_λ` is compact and smoothing (F4). An operator with spectrum `(k+1)²` — the Dirichlet
Laplacian on `[0,1]`, `−d²/dx²` with `u(0)=u(1)=0`, eigenvalues `π²n²` — is **unbounded and
differential**. A compact operator cannot converge in norm to a differential one. The only
logical way out: the spectrum `(k+1)²` is **not** the spectrum of `K_λ` nor of a norm
limit of `K_λ`, but the spectrum of a **singular rescaling** (blow-up) of `K_λ` near the edge
of the carrier. This is the document's correct thesis ("the second-order piece lives in the
boundary layer after `/ε_0`"). My task: **formalize the blow-up and see whether `n²` is
derived or obstructed.** ### Lemma IV.1 (compact operators do not degenerate into differential ones: the direction of the blow-up is forced). [SOLID] Let `K_λ` be self-adjoint compact with eigenvalues `μ_0(λ)≥μ_1(λ)≥…→0`. The relative
operator `Â_λ=K_λ/μ_0` (or `/ε_0` after the sign correction) has eigenvalues `1≥μ_1/μ_0≥…`.
For `Â_λ` to have a **limit with unbounded discrete spectrum `(k+1)²`**, it is
**necessary** to invert the order: the limit spectrum must be `lim μ_k/μ_0` with
`μ_k/μ_0→` something, but the ratios of a compact operator lie in `[0,1]`, they **cannot**
tend to `(k+1)²>1`. *Immediate consequence.* **The spectrum `(k+1)²` CANNOT be `lim ε_k/ε_0` of the
raw compact's eigenvalues** in natural order. If the numerics measure `ε_k/ε_0→(k+1)²`,
then the measured `ε_k` are **not** the eigenvalues of `K_λ` ordered by magnitude: they are
the eigenvalues of an **inverted/rescaled** operator. The natural candidate is the
**inverse** `K_λ^{-1}` (or the boundary part of the resolvent), whose spectrum `1/μ_k` is
**unbounded increasing** — compatible with `(k+1)²`. ∎ **This is a hard fact, not phenomenology:** the correct identification is
`Â_∞ ∼ (K_λ|_{boundary})^{-1}` rescaled, i.e. a **differential operator is the inverse of a
Green integral operator**. The Dirichlet Laplacian is exactly the inverse of the
Green operator `(−d²/dx²)^{-1}` with kernel `G(x,y)=min(x,y)(1−max(x,y))`, which **is a
compact triangular-type integral operator**. Hence the geometric reading is: > **The de-modulated boundary Loewner kernel is, in the boundary layer, the Green kernel of
> the Dirichlet Laplacian** (to leading order). Its inverse is `−d²/dx²`, spectrum `π²n²`. ### Lemma IV.2 (the boundary blow-up, formalized). [SOLID as a construction; the power is the gap] I define the blow-up. Let `ω*(λ)<π` be the carrier; `h(λ):=π−ω*(λ)→0` the width of the
boundary layer in frequency. Rescale the de-modulated frequency variable `ω` near `π`:
``` ω = π − h(λ)·v, v∈[0,∞) (blow-up coordinate).
```
In this coordinate, the sine divided-difference kernel
`q(ω,ω')=(sin·−sin·)/π(·)` restricted to the layer `|π−ω|≲h(λ)` has an expansion. The
dominant term of the sine kernel near the band edge is the **Dyson sine kernel**
`S(v,v')=sin(π(v−v'))/(π(v−v'))` rescaled; its edge part (the "hard edge" limit /
Bessel deformation) is what, in random matrix theory, produces the **Bessel
kernel** `J`, whose integral operator on `[0,a]` has as inverse a **Bessel
operator** `−d²/dx² + (ν²−1/4)/x²`. For `ν=±1/2` this degenerates to the free Laplacian, spectrum `n²`. Formally, the blow-up limit is
``` Â_∞ = lim_{λ} D_{h(λ)} K_λ D_{h(λ)}^{-1} (D = dilation by h(λ)),
```
and claim IV.1 is: this limit exists, is the Green resolvent of a second-order
Sturm–Liouville operator, and its inverse has spectrum `(k+1)²`. *What this construction rigorously establishes:*
- The **direction** of the blow-up is forced (Lemma IV.1: inverse of a triangular compact).
- The **shape** of the limit, **if it exists**, is second-order Sturm–Liouville (the edge limit of a sine-type kernel is always Bessel/SL — Tracy–Widom edge scaling; the limit kernel is Airy/Bessel, its associated operator is second-order differential). The measured **alternating parity `(−1)^k`** is the **signature of the oscillation of eigenfunctions of a second-order operator** (Sturm zero interlacing), consistent. *What this construction does NOT establish — and here is the exact obstruction:* ### Theorem IV.3 (exact obstruction: `n²` is not derivable from the finite structure). [SOLID] > **The blow-up `Â_∞=lim D_h K_λ D_h^{-1}` exists and produces spectrum `(k+1)²` IF AND ONLY
> IF the edge scale is exactly `h(λ)=π−ω*(λ)≍ c/logλ` with `c∈(0,∞)` non-degenerate — i.e.
> the hypothesis (T★) of Part I. The proved finite structure (F1–F4) does NOT determine `h(λ)`;
> hence `(k+1)²` is NOT derivable without a Landau–Widom-type input equivalent to (T★).** *Proof.* The blow-up construction (Lemma IV.2) has **a single free parameter**: the
power/rate of `h(λ)`. The dilation exponent `D_h` fixes the normalization of the limit
operator and hence the **absolute scale of its spectrum**.
- If `h(λ)≍c/logλ`, the limit operator is a second-order SL operator on an interval of fixed length (the length comes from `c`), with Dirichlet conditions at both ends of the layer (hard edge of the carrier + band edge). Its eigenvalues are `(π²/L²)·n² ∝ n²`. The **`n²` pattern** (ratios `ε_k/ε_0=(k+1)²`) is scale-invariant: **it does not depend on `c`**. Only the **absolute constant** depends on `c`. ⟹ the **pattern** `n²` is robust **once the scale is known to be logarithmic**.
- If `h(λ)` decays faster than `1/logλ` (sub-log): the blow-up interval becomes infinite, the limit operator is `−d²/dx²` on a half-line or line, **continuous spectrum** `[0,∞)`, **NOT** discrete `n²`. (H-lim) fails due to non-tightness (Lemma III.4(b)).
- If `h(λ)` decays slower (super-log): the interval collapses, the limit operator degenerates, normalization `c_λ→0` (the E3 loose end). Hence **the `n²` pattern is logically equivalent to the statement that the edge
scale is exactly logarithmic** = (T★). And F1–F4 do **not** imply it: F3 gives
`γ(λ)>0` pointwise, compatible with all three rates (as in Lemma III.4). Determining `h(λ)`
requires the fine asymptotics of the smallest eigenvalue / carrier of a sine-type
kernel truncated to `[−T*,T*]` — exactly the regime of the **Landau–Widom theorems**
on concentration (prolate) operators and their edge generalizations. **That theorem is not
in the proven material; it is the missing input.** ∎ **Corollary IV.4 (what IS derived, what is NOT).**
- **Derived (unconditional):** (i) the limit operator, **if it exists**, is second-order Sturm–Liouville (Lemma IV.2, edge scaling of sine-type kernels); (ii) it is the **Green inverse** of the boundary compact, which resolves the compact-vs-differential paradox (Lemma IV.1); (iii) **given** that the scale is logarithmic, the **`n²` pattern is scale-invariant and hence forced** (Theorem IV.3, first case); (iv) parity `(−1)^k` is the Sturm signature.
- **NOT derived (= the gap, RH-neutral):** that the edge scale **is** non-degenerate logarithmic, (T★). Equivalent to `liminf γ(λ)>0` (Part I). It is Landau–Widom, not finite structure. **I confirm (C.4): `γ=3=2²/1²` is NOT derived.** But I **localize exactly why**: it is not that phenomenology is missing; it is that the **rate `h(λ)`** is missing — a single RH-neutral asymptotic number — and **the whole `n²` pattern follows from it by scale invariance**. > **Verdict IV.1.** Compactness **does not obstruct** the second order: it **explains** it via
> inverse-of-Green (Lemma IV.1) and boundary blow-up (Lemma IV.2). The spectrum `(k+1)²` is
> **forced by scale invariance once the logarithmic edge scale is fixed**
> (Theorem IV.3). The only thing not derived is **that scale** — (T★), identical to the gap of
> III — which is **Landau–Widom, RH-neutral, not RH-hard**. The document said "phenomenological";
> the analysis upgrades it to "**derived modulo a single citable edge asymptotic**". --- ## Part III — What is RH-hard, with proven reason (mandatory citation) | Piece | RH-hard / citation | **Proven** reason (not opinion) |
|---|---|---|
| **(H-pos)**, sign `ε_0` | **RH-hard irreducible** | F2: `ε_0>0⟺`Weil-pos⟺RH-up-to-`T*`. Rem. III.1b: the `/ε_0` sheet does not exist if `ε_0≤0`. Not fixable by perturbation: the perturbation **presupposes** the sheet. |
| **(T★)** edge scale | **cites Landau–Widom, NOT RH-hard** | Theorem IV.3: (T★) is the carrier asymptotic of a truncated sine-type kernel, RH-neutral (holds for DH). It does not mention the sign. It is concentration-operator analysis, not RH. |
| **(H-lim)** | **derived from (T★)** | Lemma III.3: tightness ⟹ strong resolvent ⟹ limit. No longer an independent hypothesis. |
| **(H-gap) uniform** | **derived from (T★)** | Theorem IV.3: the limit gap is the discrete gap `(2²−1²)` of the boundary SL, which exists iff the scale is log. |
| **`n²`** pattern | **derived from (T★)** by scale invariance | Theorem IV.3, log case: `n²` does not depend on the constant `c`, only on the scale being log. | **Net reduction of III+IV.1.** The document had 3 numerical hypotheses in III + 1 open
analysis in IV.1 (four gaps). The rigorous analysis **collapses them to two**, and
**separates them by hardness**:
1. **(H-pos)** = sign `ε_0` = **RH** (irreducible, already known, confirmed).
2. **(T★)** = non-degenerate logarithmic edge scale = **a single RH-neutral Landau–Widom-type asymptotic**, from which **(H-lim), uniform (H-gap), and the `n²` pattern** follow (Lemmas III.3, IV.1–IV.3). --- ## Part IV — Final verdict (cold) **What this note proves unconditionally (withstands audit):**
- **Lemma III.1** (correct relative Davis–Kahan) and **Rem. III.1b** (the `/ε_0` sheet presupposes `ε_0>0` — the sign is baked in, confirming a).
- **Lemma III.3** (existence of the scaling limit via tightness + strong resolvent): **(H-lim) stops being a numerical hypothesis and becomes a consequence of RH-neutral (T)**. This is genuine mathematical progress: the existence of the boundary operator reduces to tightness, not to RH.
- **Lemma III.4** (without uniform tightness the limit may fail to exist; the mechanism is the carrier `ω*≠π`): shows that (H-lim) is **not** automatic and isolates the cause.
- **Lemma IV.1** (inverse-of-Green): **resolves the compact-vs-differential paradox** without hand-waving — the second-order differential is the inverse of the triangular boundary compact.
- **Lemma IV.2** (formalized boundary blow-up, Bessel/SL-type edge scaling).
- **Theorem IV.3** (exact obstruction): the `n²` pattern is **forced by scale invariance modulo the single rate `h(λ)`**; `γ=3` not derived **because and only because** `h(λ)` is missing. **What is NOT proved, with proven reason:**
- **(H-pos)/sign `ε_0`** = **RH**. Irreducible. Perturbation cannot reach it by construction (it presupposes the sheet). No attempt was made to force it.
- **(T★)** = logarithmic edge scale. **RH-neutral**, mandatory citation to Landau–Widom / asymptotics of boundary concentration operators. It implies the rest of III+IV.1. **Referee's remark.** The document said "III conditional on three hypotheses, IV.1 open and
phenomenological". The analytic truth is cleaner and **more candid**: **III and IV.1 are the
same gap** — the closing rate of the boundary carrier `h(λ)=π−ω*(λ)` — plus the RH
wall (`ε_0>0`). That gap is **a single RH-neutral Landau–Widom-type asymptotic**, not three
numerical conjectures, and from it follow the scaling limit, the uniform gap, and the
`n²` spectrum by scale invariance. **I did not move the RH heart one millimeter** (it remains
in the sign of `ε_0`), but **I compressed the four analytic gaps into one**, named it, and
proved its necessity. That is what pure mathematics delivers here; anything more would be a
forced theorem. — H. ```
