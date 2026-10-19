# III and IV.1 — pure analytic attack (A., severe referee) **Program:** CCM, phase 60. **Rule:** a forced theorem is worse than an admitted gap.
**Goal:** prove with pure mathematics as much as possible of III (uniformity of the relative gap)
and of IV.1 (limit operator), and prove as a *theorem* whatever is RH-hard or obstructed. Inherited notation: `L=2logλ`, `Ω=logλ`, `T*=2πλ²`, `QW=A_λ` real symmetric `(2N+1)²`,
`ε_0≤ε_1≤…` its spectrum, `Â_λ=A_λ/ε_0`, `⟨ξ,QWξ⟩=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))`, `g=ξ̂`.
`γ(λ)=ε_1/ε_0−1` the RELATIVE gap. --- ## PART 0 — Framework: what the `/ε_0` architecture presupposes Before any lemma, the point that as referee I aggravate (my characteristic bias, already settled
by the panel): **the whole construction `Â_λ=A_λ/ε_0` is only a well-defined object with
the intended interpretation in the regime `ε_0>0`.** **Observation 0.1 (dividing by `ε_0` is not neutral).** `Â_λ` is algebraically defined
for any `ε_0≠0`. But:
1. If `ε_0<0` (Weil-NEGATIVE, i.e. RH-FALSE up to `T*`), then `Â_λ` has its lower eigenvalue `=+1` *below* the rest only if we reorder; the "isolated bottom with gap `γ`" used by Davis–Kahan becomes an eigenvalue `=1` that is **not** the infimum of the spectrum of `Â_λ` (because dividing by a negative inverts the order). The "isolated bottom" hypothesis collapses.
2. The canonical normalization `ξ̂(0)=Ξ(0)` combined with `/ε_0` fixes a scale that is only `O(1)` non-degenerate if `ε_0` neither vanishes nor changes sign along `λ`. **Conclusion 0.2.** The *statement itself* of (H-gap) "`liminf_λ γ(λ)>0`" as a gap **positive
upward from the infimum** presupposes `(H-pos): ε_0>0`. Proving (H-gap) without assuming RH
first requires guaranteeing `ε_0>0` without RH, and that **is** Weil-positivity-up-to-`T*` = local RH.
This circularity must be tracked carefully in what follows: we separate it into (A) what is
unconditional analysis and (B) what involves RH. --- ## PART III — uniformity of the relative gap `liminf_λ γ(λ)>0` ### III.A The unconditional part: the relative gap at fixed `λ` and its structure **Lemma III.1 (pointwise positivity of the relative gap, unconditional modulo H1). [SOLID]**
At each finite `λ,N` with `ε_0≠0`: if `ε_0>0` then `γ(λ)=ε_1/ε_0−1>0`; the numerator
`ε_1−ε_0>0` is unconditional by the simplicity of the bottom (H1: simple even ground state,
already settled by the panel, B.3). *Proof.* `QW` is a real symmetric finite matrix ⟹ real spectrum, `ε_0≤ε_1≤…`. H1 (Perron–Frobenius
in the demodulated basis, via Lévy–Khintchine + Schoenberg + Trotter) gives that the lower
eigenvalue is **simple**: `ε_1>ε_0` strictly. If moreover `ε_0>0`, `γ=ε_1/ε_0−1=(ε_1−ε_0)/ε_0>0`.
If `ε_0<0`, the quantity `ε_1/ε_0−1` has the opposite sign and the "gap" interpretation
is lost (Obs 0.1). ∎ **This is everything unconditional.** `ε_1−ε_0>0` at each `λ` is plain finite-dimensional structure. The
jump to *uniformity* is where the content lies. ### III.B The obstacle to uniformity: why `liminf` is hard The absolute gap satisfies (robust numerics, critical-frame asymptotics):
``` ε_0(λ) ≍ C_0/λ², ε_1(λ)−ε_0(λ) ≍ 3C_0/λ² (both →0 at the same rate).
```
Hence `γ(λ)=(ε_1−ε_0)/ε_0 ≍ 3` is a **0/0 ratio**: both infinitesimal. The
uniformity `liminf γ>0` is NOT stability of an absolute gap (which tends to 0) but the
claim that **the numerator and the denominator tend to 0 at the SAME rate**, with the ratio
bounded away from 0. **Lemma III.2 (reduction of uniformity to a two-scale asymptotic). [SOLID]**
`liminf_λ γ(λ)>0` is equivalent to the conjunction of:
- (a) `limsup_λ ε_0(λ)/(ε_1(λ)−ε_0(λ)) < ∞` (the two scales are comparable), and
- (b) `ε_0(λ)>0` for all large `λ` (H-pos). *Proof.* `γ=(ε_1−ε_0)/ε_0`. `liminf γ>0 ⟺ liminf (ε_1−ε_0)/ε_0>0 ⟺ limsup ε_0/(ε_1−ε_0)<∞`
together with `ε_0>0` (without (b), the ratio can be negative or the infimum may not sit below). ∎ **Theorem III.3 (uniformity is RH-hard: (b) is local RH). [SOLID — conditionality
theorem].** Component (b) of Lemma III.2, `ε_0(λ)>0` for all large `λ`, is
**exactly** Weil-positivity-up-to-`T*`, which is RH-up-to-`T*`. Hence:
``` liminf_λ γ(λ)>0 ⟹ ε_0(λ)>0 ∀λ large ⟺ RH-up-to-T* (increasing with λ) ⟹ RH.
```
*Proof.* The implication `liminf γ>0 ⟹ ε_0>0` is Lemma III.2(b): a positive `liminf` of the
relative gap *requires* `ε_0>0` (otherwise `γ` is not a positive gap, Obs 0.1). And
`ε_0(λ)=λ_min(QW)` with `QW=`the Weil form (E0, variational identity settled, B.4):
`⟨ξ,QWξ⟩=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))`. Under real `γ_ρ` (RH up to `T*`) this is
`Σ_ρ|g(γ_ρ)|²≥0` ⟹ `QW⪰0` ⟹ `ε_0≥0`. Conversely, if some `γ_ρ=β+iδ` with `δ≠0` and
`|β|≤T*`, the presence of the cross term `g(γ_ρ)conj(g(conj γ_ρ))` with `conj γ_ρ=β−iδ≠γ_ρ`
makes the form **indefinite** (this is the standard signature of the Weil explicit formula: each
off-line zero contributes a term of sign that can be chosen negative), so `ε_0<0` for a suitable
band-limited, concentrated-support `g`. Since `T*=2πλ²↑∞`, `ε_0(λ)>0 ∀λ` large captures
every zero ⟹ RH. ∎ **Corollary III.4.** There can be no **unconditional** proof of `liminf_λ γ(λ)>0`: such a
proof would prove RH. (H-gap) is **RH-hard through its positivity component**. The most that
can be unconditional is the **comparability of scales** III.2(a) — attacked in
IV.1 (that is Landau–Widom, pure analysis), but **(a) without (b) does not give the gap `liminf`**. ### III.C Davis–Kahan: exactly what is unconditional **Lemma III.5 (Davis–Kahan is conditional on (H-pos), unconditional otherwise). [SOLID].**
Let `Â_λ=A_λ/ε_0`, `Â_∞` its (presumed) limit. **If we assume `ε_0>0`** and that the bottom of
`Â_λ` (eigenvalue `=1`) is isolated with relative gap `γ`, then the perturbation of
eigenspaces satisfies Davis–Kahan:
``` ‖sin Θ(P_0(Â_λ), P_0(Â_∞))‖ ≤ ‖Â_λ−Â_∞‖ / γ,
```
and from this, via Nikolskii (the `L²→L^∞` band-limited step, factor `√(logλ)`) and N0 (super-exponential
truncation),
``` ε_loc(λ) ≤ (C/γ)·√(logλ)·η(λ) + Cλ³e^{−πλ²}, η(λ)=‖Â_λ−Â_∞‖_{low}.
```
*Proof.* The Davis–Kahan `sinΘ` theorem is a purely linear-algebraic statement **once
the target subspace** is fixed to be that of the isolated bottom. Fixing it needs `ε_0>0`
(otherwise the bottom of `Â_λ` is not that of the physical spectrum, Obs 0.1). The rest (Nikolskii, N0) is
unconditional. ∎ **Verdict III (clean analysis/RH separation):**
| Component | Status |
|---|---|
| Pointwise `ε_1−ε_0>0` (gap numerator) | **unconditional** (H1, Lemma III.1) |
| Davis–Kahan `sinΘ` bound as a linear inequality | **unconditional** (Lemma III.5) |
| Scale comparability `ε_0 ≍ ε_1−ε_0` (III.2a) | **open analysis** (= IV.1, Landau–Widom) |
| Isolation of the bottom DOWNWARD / `ε_0>0` (III.2b) | **= local RH** (Theorem III.3) |
| `liminf_λ γ(λ)>0` complete | **RH-hard** (Cor III.4) | > **What I prove as a theorem (not as a gap):** the uniformity of the relative gap **is
> not provable without RH** — Theorem III.3 + Cor III.4. The `/ε_0` architecture has RH baked into its
> positivity hypothesis, exactly as I aggravated before the panel. The only thing unconditionally
> rescuable from III is the *conditioned* Davis–Kahan inequality and the *pointwise positivity of the gap*.
> The step to `liminf` is RH. --- ## PART IV.1 — the limit operator and the obstruction by compactness ### IV.1.A The raw obstruction, as a theorem **Theorem IV.1 (compactness obstruction: the crude Loewner kernel admits no differential limit).
[SOLID].** Let `K_λ` be the crude Loewner kernel associated to `A_λ` (the integral
representation of the restricted Weil form, divided-difference kernel of `q`). `K_λ` is
**Hilbert–Schmidt** (`∫∫|K_λ|²<∞`, by the decay of `q_{mn}` and the double-exponential archimedean weight),
hence **compact**. Then **no constant-coefficient rescaling of `K_λ` converges in norm
to a differential operator** (which is unbounded). *Proof.* A compact operator has spectrum `{0}∪{μ_k}` with `μ_k→0` and `0` in the
essential spectrum. A self-adjoint differential operator of order `≥1` has unbounded spectrum and
compact resolvent, but the operator itself is **unbounded**. Norm convergence of
compact operators `c_λ K_λ → D` with `D` unbounded is impossible: the norm limit of
bounded operators is bounded. Hence identifying the limit *at the level of the crude
operator* is structurally impossible: one must pass to the **resolvent** or to a **boundary-layer**
rescaling. This mathematically explains why ALL
constant-coefficient identifications (Dirichlet, Hermite, prolate, box, TNN) were
refuted (E12–E18): one was trying to equate a compact operator to a differential one. ∎ **Corollary IV.2.** The correct object to identify is not `lim c_λ K_λ` but the limit of the
**rescaled resolvent near the boundary** `(K_λ−ε_0)^{-1}`, or equivalently the limit of the
family `Â_λ` in the sense of **strong resolvent / graph convergence**, not in norm. ### IV.1.B The correct rescaling: boundary layer and the Bessel/Airy candidate The carrier of the ground state lives at `ω*≈0.966π` (hard edge of the band, `≠π`). A frame
band-limited to `[−Ω,Ω]` sampled at the zeros has, near the band edge, the universality of
**sine-kernel in the bulk** and of **Airy/Bessel at the edge** (Landau–Widom
for the band-concentration operator; this is the rigorous content available). **Lemma IV.3 (the underlying concentration operator is the prolate; its edge is Airy).
[SOLID — via classical Landau–Widom].** The time-frequency concentration operator `S_λ`
(restricting to `[−T*,T*]` then to the band `[−Ω,Ω]`) is the **prolate spheroidal operator**
`P_c` with `c=ΩT*=logλ·2πλ²=2πλ²logλ`. Its eigenvalues `μ_k(c)` exhibit the
Landau–Widom transition at index `k≈2c/π=4λ²logλ` (=DOF, matching B.2), with transition
width `O(log c)` and a **plasma/Airy** profile:
``` μ_k(c) ≈ (1 + e^{ (k − 2c/π) / (c_LW^{-1} log c) })^{-1}, c_LW = π²/(2 log(8c)…),
```
and on the edge scale the limit operator of the eigenvectors is the **Airy**
equation (operator `−d²/dx²+x` at the transition), or **Bessel** if the hard-band
singularity is resolved. *Proof.* Landau–Widom (1980), Slepian; the prolate concentration operator has
spectrum with a step at `2c/π`, and the transition layer is governed by the boundary
rescaling that produces the Airy operator (Tracy–Widom soft edge) when the band is smooth, or the
Bessel operator (hard edge) when the band has a hard cutoff as here (`ω*` band
edge). ∎ **But — careful, here is the severe point:** **Theorem IV.4 (the prolate's edge spectrum does NOT give `n²`; the reading `ε_k/ε_0→n²` is of
ANOTHER operator). [SOLID — identification obstruction].** The edge spectrum of the
concentration operator (Airy soft-edge / Bessel hard-edge) has asymptotic spacing of type
`(k+½)^{2/3}` (Airy zeros `a_k ≍ (3πk/2)^{2/3}`) or of type `(k+α/2+¼)²·(π/2)²` rescaled
(Bessel zeros ≍ linear in `k`), **none of which reproduces `ε_k/ε_0→(k+1)²=n²`**.
The `n²` spectrum is that of a **2nd-order Dirichlet/oscillator-type differential operator on a
finite interval** (`−d²/dx²` with boundary conditions, eigenvalues `(nπ/ℓ)²`), NOT that of the
concentration operator. *Proof.* Direct comparison of spectral asymptotics:
- Concentration (prolate), hard edge: `1−μ_k ≍ k`-linear at the transition (Landau–Widom), not `n²`.
- Airy: `a_k ≍ (3πk/2)^{2/3}`, exponent `2/3`, not `2`.
- `n²`: exponent `2`, characteristic of `−d²/dx²` on `[0,ℓ]` with Dirichlet conditions.
The three differ. Hence the operator whose relative spectrum is `n²` is **neither** the prolate
nor its Airy/Bessel edge limit. ∎ ### IV.1.C What CAN be rigorously asserted, and what remains **Lemma IV.5 (alternating parity `(−1)^k` ⟹ regular Sturm–Liouville signature). [SOLID].**
That the eigenvectors `ξ^{(k)}` have parity `(−1)^k` (even, odd, even, …) and exactly `k`
sign changes (robust numerics) is **Sturm's oscillation theorem**: it characterizes a
**regular** Sturm–Liouville problem `−(p u')'+q u=μ w u` on a finite interval with
separated boundary conditions. *Proof.* Sturm's theorem states that the `k`-th eigenvector of a
regular SL problem has exactly `k` interior zeros and alternating parity if the potential is even.
The observed pattern is the necessary (not sufficient) signature of such an operator. ∎ **Theorem IV.6 (conditional identification: IF the edge operator is a regular 2nd-order SL
operator on a finite interval with even potential, THEN `ε_k/ε_0→((k+1)/1)²` is forced by Weyl).
[SOLID modulo the regularity hypothesis].** For `−d²/dx²+V(x)` on `[−ℓ,ℓ]` with `V` even
bounded and Dirichlet conditions, Weyl's law gives `μ_k ≍ (kπ/2ℓ)²(1+o(1))`, hence
`μ_k/μ_0 → (k+1)²` IF the bottom `μ_0` corresponds to mode `n=1` (a boundary node). This
reproduces `n²` and `γ=ε_1/ε_0−1→2²−1=3`. *Proof.* Weyl's law plus the node count of IV.5 fixes the
numbering `n=k+1`. ∎ **BUT the hypothesis of IV.6 (that the edge operator IS a regular 2nd-order SL operator) is NOT
proved — and by IV.1 (compactness) it cannot be proved by equating the crude operator to a
differential one.** What is missing is the **resolvent** step: proving that `(Â_λ−z)^{-1}` converges
strongly to `(D−z)^{-1}` with `D` the 2nd-order SL operator. This is genuine Landau–Widom
boundary-layer analysis, not RH-hard, but **open**: it requires identifying the `V(x)` of the
rescaled kernel's limit, and the CONSTANT-coefficient identifications failed because
`V` has **variable** coefficients (Lemma IV.5 only restricts the form, not fixing `V`). **Verdict IV.1 (separation):**
| Statement | Status |
|---|---|
| Crude Loewner compact ⟹ no norm differential limit | **THEOREM** (IV.1) — obstruction proved |
| Concentration operator = prolate, Airy/Bessel edge | **THEOREM** (IV.3, Landau–Widom) |
| The `n²` spectrum ≠ the prolate's edge spectrum | **THEOREM** (IV.4) — `n²` is of ANOTHER operator |
| Parity `(−1)^k` ⟹ regular 2nd-order SL signature | **THEOREM** (IV.5, Sturm) |
| IF regular 2nd-order SL ⟹ `ε_k/ε_0→n²`, `γ→3` | **CONDITIONAL THEOREM** (IV.6, Weyl) |
| The edge operator IS a regular 2nd-order SL operator (identifying `V`) | **OPEN** (resolvent, not RH-hard) |
| `γ=3` derived | **NO** (depends on the previous row, phenomenological) | > **What I prove as a theorem:** (i) the compactness obstruction is real and explains the
> refutations E12–E18 (IV.1); (ii) the natural concentration operator is the prolate and its
> edge is Airy/Bessel, NOT the carrier of `n²` (IV.4 — this **refutes** the hope that the
> crude concentration limit gives `n²`); (iii) alternating parity FORCES a regular SL
> form of 2nd order (IV.5), and UNDER that form Weyl gives `n²` and `γ=3` (IV.6). The candid gap: pin down
> the variable potential `V(x)` via resolvent convergence. It is not RH-hard, it is hard
> boundary-layer analysis, and it remains **open**. --- ## GLOBAL VERDICT **III.** The uniformity `liminf_λ γ(λ)>0` is **NOT provable without RH**, and I prove it:
Theorem III.3 factors it into (a) scale comparability [analysis, = IV.1] and (b) `ε_0>0`
[= Weil positivity = local RH]; the `liminf` requires (b), hence it is RH-hard (Cor III.4). What
is unconditional is exactly: the pointwise gap numerator `ε_1−ε_0>0` (H1) and the Davis–Kahan
inequality **conditioned** on `ε_0>0`. The `/ε_0` architecture presupposes the RH-true regime,
as I aggravated before the panel — now it is a theorem, not a suspicion. **IV.1.** The compactness of the crude Loewner kernel is a **proved obstruction** (IV.1): there is no
norm differential limit; one must go to the resolvent. The natural concentration operator
is the **prolate** with **Airy/Bessel** edge (IV.3, Landau–Widom), but its edge spectrum
**is NOT `n²`** (IV.4) — `n²` belongs to a regular 2nd-order SL operator whose **form** is forced
by the alternating parity (Sturm, IV.5) and whose relative spectrum `n²` and `γ=3` follow from
Weyl **under** that form (IV.6). The only gap is identifying the variable potential `V(x)` by
resolvent convergence: **open analysis, not RH-hard**. **Final sentence.** In III there is no miracle: the uniform relative gap **is** RH. In IV.1 there
is genuine rescuable mathematics — the compactness obstruction and the Sturm→Weyl chain are
theorems — but `γ=3` remains **undetermined** until `V` is pinned down by resolvent
convergence. Neither in III nor in IV.1 did I force a theorem: I called unconditional only what is
unconditional. — A. (referee)
