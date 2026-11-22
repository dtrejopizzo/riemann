# AUDIT_204_CSTAR_001 — Audit of (C★) "Hamburger inequality with defect" (COMPOSE_EF_001 §5)

Row D / L′♯ is treated as an independent
objective.

## Summary (≤250 words)

(C★) is written as an explicit inequality (COMPOSE §5.2), so it is auditable. The audit reduces it as follows:

1. **δ_E(Λ; f) is not an Euler defect.** With a = Λ, b(Λ) ≡ 1 and r_f^Λ = r_f, and by prop:ext-gauge (PROVED given
   Guo L4.4) one has **2δ_E(Λ; f)² = ℓ(Ef)**, the gauge-minimized leak. Euler enters as an **identity** (Λ∗1 = log), not
   as an inequality. Q-P2.2 contributes no quantity defined at ζ that differs from ℓ.
2. **The term F is a fixed seminorm of f.** 𝔑_F(f) := sup_{a∈𝒱(Λ)} |𝔇_F(a;f)|²/‖a−Λ‖² is evaluated only around Λ.
   To first order it is ‖L f‖², with L linear and universal (the derivative of the Dirichlet exponential at Λ). The FE
   is used only as the identity 𝔇_F(Λ; ·) = 0, which makes the quotient finite.
3. With K(T) free, the content of (C★) is: **W_T ≥ ℓ on the subspace ker 𝔑_F**, plus a penalty term. It is a case of
   prob:ext-L (κ = 1, A₀ = 0) restricted to a subspace fixed by an identity F. By Def. O1.2, **it chains**: F acts as a
   prior identity and the sign step is the coercivity of the leak, a single channel (gauge/radical, branch 1 by
   GUO_QUANT Prop 1.3 and R-Q6). Abstract falsifier at the intermediate object: W′ = ℓ − ε‖·‖² on the quotient.
4. The "cancellation to 10⁻⁷" prediction is not a prediction. The inequality only gives a one-sided bound, K is free,
   and 9·10⁻⁸ is a Galerkin 𝔤 normalized by ℓ, not W_T(h_ev).

**Verdict: NO-GO as an E∧F composition (chains; PROVED from COMPOSE's definitions).** The residual inequality is OPEN,
but it is not new: it is prob:ext-L/eq:ext-starstar. Do not request calibration of (C★).

---

## 0. Corpus check

Read: COMPOSE_EF_001 (complete, §§1–8), O1_COMPOSITION_001 (Def. O1.2, Prop. O1.C, Lemma O1.E and the table §3),
BARRIER_D1_001 (Prop 1, Thm 2, Cor 3, Thm 4, §5, §7), GUO_QUANT_001 (Prop 1.3 and §1.3), and in Paper 46 thm:ext-half,
rem:ext-killing, prop:ext-gauge, lem:ext-ellbound, prob:ext-L and prop:ext-consol. Index: AUDIT_200_SPEC_003 (R-Q6: the
descent of 𝒲 to the gauge quotient already uses exact Λ; (𝒬_μ, 𝒲, ℓ) = prob:ext-L) and AUDIT_204_CLOSURES_001 (PC-2:
𝔤_ev ≲ 9·10⁻⁸ is a Galerkin quotient). This audit builds nothing new. It classifies.

## 1. "The FE depends on the data in the half-line model"

**What is true.** The map a ↦ b(a) (Dirichlet exponential of a/log) is not linear. For a_P, b = 1_{(n,∏p)=1}, and the
c_N of the exterior datum (FF.1, GG: Σ c_N N^{−s} = ζM_μ − 1) change nonlinearly with the comb. ✓ Also
𝔇_F(a; f) ≠ 0 for a ≠ Λ in the Euler family (BARRIER_D1 Thm 2 gives the exact Bohr defect, which is positive). ✓

**What (C★) actually uses.** In (C★)

  W_T(g) ≥ 2 δ_E(Λ; f)² − K(T) · sup_{a∈𝒱(Λ)} |𝔇_F(a; f)|² / ‖a − Λ‖²

**everything is evaluated at Λ**. The variation in a only appears in the sup, which is a number attached to f, and no
other L is compared. Two things must be separated:

- (i) *"F depends on a"*: true as a function a ↦ 𝔇_F(a; ·).
- (ii) *"F distinguishes ζ inside (C★)"*: false as a mechanism. The only thing (C★) uses of F at ζ is
  𝔇_F(Λ; ·) ≡ 0, because without that identity the quotient diverges as a → Λ and the right-hand side equals −∞, which
  gives a trivially true inequality and not a signless inequality, as COMPOSE §5.2 claims. Beyond that identity, the
  term is a universal seminorm.

To first order: Db_n[u] = Σ_{m|n} u(m)/log m (derivative of exp(Σ a(m)m^{−s}/log m) at Λ, where b ≡ 1), so that

  D𝔇_F(Λ; f)[u] = Σ_m (u(m)/log m) Σ_{k≥1} (f(km) − f̂(km)) − (pole variation) =: ⟨u, L f⟩,

and 𝔑_F(f) = ‖L f‖² (1 + O(diam 𝒱)) in the dual norm of ‖·‖ (PROVED to first order, direct computation; the pole term
is one more linear functional, which does not change the structure). L is **linear in f and does not depend on which
L-function is audited**. That is why "the FE as the derivative of the conductor-1 Poisson in the direction of the
data" is a fixed quadratic form on the tests. It is not a quantity that distinguishes ζ.

**Branch 1.** Exterior Poisson and radicality (Guo L4.4) hold for every L with an explicit formula (GUO_QUANT
Prop 1.3). That does not make 𝔇_F identical for all of them, because Hamburger does distinguish b ≡ 1. But (C★) does
not exploit that distinction. It would be exploited by a statement of the form "for every a ∈ 𝒱,
W_T^{a} ≥ … − K|𝔇_F(a)|²", and COMPOSE does not write that.

Side remark (ARGUED): at T = ½log3 one has λ = e^T = √3 < 2. The core's tests are supported on [−λ, λ], so f(n) = 0
for n ≥ 2 and 𝔇_F reduces to values of f̂ at the integers n ≥ 2 > λ, i.e. to samples of r_f = 𝓕f|_{(λ,∞)} (up to
normalization). The two terms on the right-hand side are then functionals of **the same** r_f: ℓ is its L² distance
to the gauge and 𝔑_F is its sampling on ℕ weighted by Möbius/log. This reinforces that (C★) is an inequality about r_f
at ζ.

**Verdict (1).** The statement exists. "The FE depends on the data" is true as a fact, but it does not act within
(C★): there F is an identity (finiteness) plus a fixed seminorm.

## 2. Euler as a δ_E inequality

- GUO_QUANT §1 (Prop 1.3): the radical is an **identity** for every L with an explicit formula and carries no
  quantity. The defects that distinguish (cΛ) are **linear**: (1−c)·arch.
- P2_SCHUR §5 / table O1 §3: Q-P2.2 is "nearly radical block, 𝒲_AA ~ ε, 𝒲_AB ~ ε^{½}", subject to thm:shape(B′), with
  constant 4·10⁹T e^{−15.449T}. It is a **rate**, not a quantity δ_E(a; f) defined for a general comb. COMPOSE §5.3(2)
  admits that at ½log3 that rate equals ≈ 4.5·10⁵ and is useless.
- Definition given by COMPOSE: δ_E(a; f) = dist_{L²(λ,∞)}(r_f^a, 𝒢̄_T^a). At a = Λ, the only point (C★) uses,
  prop:ext-gauge gives **2δ_E(Λ; f)² = ℓ(Ef)** (PROVED given Guo L4.4). It is the gauge-minimized leak from
  prob:ext-L. It measures no distance from Λ to another comb.
- If instead δ_E is taken as the gauge–radical distance of 𝒲_a at another comb (P2_GAUGE_RADICAL:
  Σ 2(Λ−a)(n)n^{−½}c_Φ(log n)), the quantity is **linear** in a − Λ, equals 0 at ζ and O(1) at the falsifiers. By
  Lemma O1.E it is a linear identity in the weights: it chains. Moreover (C★) does not use it, because it evaluates
  δ_E only at Λ.

**Verdict (2).** There is no δ_E "of Euler" defined as an inequality. In (C★), δ_E(Λ)² = ℓ/2, and E enters only
through Λ∗1 = log (rem:ext-killing(ii)), i.e. as an identity. The label "E as an inequality (Q-P2.2)" is incorrect.

## 3. Chaining or composing (Def. O1.2 applied to (C★) as written)

Exact rewriting using §§1–2:

  (C★) ⟺ W_T(Ef) ≥ ℓ(Ef) − K(T)·𝔑_F(f)  for all f in the core (and, since W and ℓ depend only on g = Ef, with the
  infimum of 𝔑_F over the gauge).

Steps, in the order of O1.2:

- A₁ (identity, channel E): Λ∗1 = log ⇒ b ≡ 1 ⇒ thm:ext-half, prop:ext-gauge. Object: (W_T, ℓ) on the core modulo the
  gauge. R-Q6: this descent already uses exact Λ.
- A₂ (identity, channel F): 𝔇_F(Λ; ·) ≡ 0 (conductor-1 Poisson) ⇒ 𝔑_F < ∞. Object: the seminorm 𝔑_F, whose kernel is
  𝒩 := ker L.
- A₃ (inequality, **sign step**): W_T ≥ ℓ − K𝔑_F.

**K free.** COMPOSE says "K(T) explicit constant", but does not give it. With K free, the signed content of A₃ is
exactly: **W_T ≥ ℓ on 𝒩** (outside 𝒩 one can take K large, and for each fixed K the statement is weaker outside 𝒩).
On 𝒩 the F term disappears. The sign step uses F only to select the subspace, which is a prior identity, and the sign
comes from **a single channel**: the coercivity of the leak with respect to the gauge/radical. It is prob:ext-L with
κ = 1, A₀ = 0, restricted to 𝒩.

So s(A) = {leak coercivity}, |s(A)| = 1: **it chains** (Def. O1.2). No reordering is needed to bring it down to 1,
because it is already at 1. COMPOSE §5.2's argument "(ii) the sup is a joint quantity in (E, F)" fails: the sup is
joint in the *definition*, but in the sign step it enters only as a fixed seminorm (§1), and at most it can
**weaken** the bound. The F term carries a − sign, so it never contributes positivity. All the sign comes from ℓ ≥ 0.

**Abstract falsifier (Prop. O1.C).** The intermediate object is the triple (quadratic form 𝒲′ on the gauge quotient,
ℓ, 𝔑_F). It suffices to take 𝒲′ := ℓ − ε‖·‖² (or any form with 𝒲′ < ℓ at a vector of 𝒩), which satisfies all prior
identities as data of the object and violates A₃. It need not come from a comb. This has the same shape as "Lemma R ∧
gap" (P2_SCHUR, V1): an identity reduces the object and a single inequality on the quotient carries the sign.

Comparison with Lemma O1.E: identity F is linear (L linear in f and in u), and the sign step is quadratic in f but
not in a. The nonlinearity of a ↦ b, which is what COMPOSE invokes as (i), lies outside the sign step, because only
its derivative at Λ is used. The condition of O1.E's corollary (nonlinear sign step **in a**, or a channel as an
inequality) is not met.

**Verdict (3): CHAINS (PROVED from the definitions of COMPOSE §5.2 and of prop:ext-gauge).**

## 4. Risks

- **BARRIER_D1.** It does not cover (C★) literally, because D1 deals with premises {Δ ≤ ε} on combs and (C★) is an
  inequality about tests at a fixed ζ. But risk test 1 proposed by COMPOSE ("compute the tangent of {𝔇_F = 0} at Λ;
  if it is {0}, the term is coercive, good") **is already resolved**: BARRIER_D1 Prop 1 (Hamburger CITED) gives
  tangent {0}, and Thm 2 gives a defect that is positive definite and symmetric in ±t to second order. By COMPOSE's
  own criterion the result would be "good", but the criterion is poorly posed: that 𝔇_F is coercive **in a** says
  nothing about the sign of W_T **in f**, and the collapse happens anyway by §3. D1 Thm 4's lesson (analytic defects
  are symmetric and blind to w) repeats here: |𝔇_F|² is even in the direction of the data.
- **Kronecker parity** (d(p^j) ↦ (−1)^j d(p^j)). Does not apply, because (C★) does not compare different L's.
  Kronecker's twist (α_p = −1) is not in a small neighborhood 𝒱(Λ), and BARRIER_D1 Thm 2 already separates it via the
  defect (factor 4/(p−1) > 0). COMPOSE's risk 3 is vacuous for the statement as it stands.
- **Zero side.** The "Poisson derivative" ⟨u, Lf⟩ is on the summation side (integers km), not Σ_ρ ✓. But
  W_T(Ef) = Σ_ρ Φ_Ψ(ρ)Φ_Ψ(1−ρ) (rem:ext-killing(iii)), and proving A₃ on 𝒩 is proving coercivity of the leak, which
  is REF-D. COMPOSE proposes no proof route, so this risk cannot be evaluated beyond this.
- **New risk (decisive):** δ_E(Λ)² = ℓ/2. With that, (C★) with K = 0 is W_T ≥ ℓ, which is **stronger** than
  prob:ext-L (κ = 1, no loss N^{−A₀}). With K > 0 the signed content reduces to 𝒩. In no case does anything appear
  that is not already in prob:ext-L.

## 5. Test at ½log3

COMPOSE §6: "W_T(h_ev) ≈ 𝔤_ev ≈ 9·10⁻⁸ ≥ 2δ_E² − K·(F term) ⇒ δ_E² and the F term cancel to 10⁻⁷."

1. **It is not a prediction.** The inequality only gives ℓ(h) − K𝔑_F(h) ≤ W_T(h), a one-sided bound. There is no
   "cancellation": 𝔑_F can be arbitrarily large. With K free, any pair of measurements is compatible, except when
   h ∈ 𝒩. As it stands, it is not falsifiable.
2. **Confusion of quantities.** 9·10⁻⁸ is a Galerkin 𝔤 (AUDIT_204_CLOSURES PC-2: 𝔤_par ≤ W/ℓ², a bound on a
   subspace), not W_T(h_ev). Nor is it q_ev + ½ = −2.16·10⁻⁸, which is a resolvent quotient
   (−λ^W⟨𝔄⁻¹χ, (𝔄−λ^W)⁻¹χ⟩). None of the three numbers is the left-hand side of (C★).
3. **Falsifiable version** (only if one wanted to rescue the residue, and that is prob:ext-L): fix K = 0 and measure
   ℓ(h)/W_T(h) at the minimizer. If ℓ(h_ev) ≫ W_T(h_ev), the K = 0 variant falls. That measurement belongs to
   prob:ext-L, not to (C★).

## 6. Verdict

- (C★): **OPEN-as-a-stated-inequality, NO-GO as an E∧F composition (chains, PROVED from the definitions).**
  After the audit, the statement is identified with prob:ext-L (κ = 1, A₀ = 0) restricted to ker L. As a residue it
  is not new.
- COMPOSE's claim "the only construction with a genuine composition shape" is **withdrawn**. The shape was apparent:
  E is an identity (δ_E(Λ)² = ℓ/2) and F is an identity plus a fixed seminorm with a − sign.
- **To the calibrator: nothing about (C★).** Requests 3 and 4 of COMPOSE §7 become moot: request 3 is already
  answered by BARRIER_D1 Prop 1, and request 4 is ℓ(h_par), which belongs to prob:ext-L. Requests 1, 2 and 5 are
  independent of (C★) and are kept if they serve C2.
- What a real composition would need (specification, OPEN): a sign step that uses 𝔇_F(a; ·) at **a ≠ Λ** (families
  of forms W_T^{a} coupled to the Poisson of b(a)), nonlinear in a. Today no such object exists.

### Entry for ROUTES-TRIED-INDEX

> - **AUDIT_204_CSTAR_001 (audit, phase 204q): (C★) "Hamburger with defect" NO-GO as E∧F composition (chains).**
>   At Λ, 2δ_E(Λ;f)² = ℓ(Ef) by prop:ext-gauge: E is an identity (Λ∗1 = log), not a Q-P2.2 inequality. The term F,
>   sup_{𝒱(Λ)}|𝔇_F|²/‖a−Λ‖², is a fixed seminorm ‖Lf‖² (derivative of the Dirichlet exponential at Λ). F only gives
>   the identity 𝔇_F(Λ) = 0 and enters with a − sign. Signed content: W_T ≥ ℓ on ker L = prob:ext-L (κ=1, A₀=0)
>   restricted; abstract falsifier 𝒲′ = ℓ − ε‖·‖². The "10⁻⁷ cancellation" prediction is one-sided, with K free, and
>   confuses 𝔤/q with W_T. Do not retry "F as the Poisson derivative at Λ." A real composition requires using 𝔇_F at
>   a ≠ Λ.
