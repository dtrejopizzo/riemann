# BARRIER_D2_001 — door (D2): defect-stability inequalities split into the target plus a sign-free rigidity; continuation in the comb is endpoint-equivalent

Phase 197. Memo (pure mathematics, no numerics), not yet reviewed.
positivity of 𝔞_T on P_T is assumed true; this memo closes a *method class* (door D2 of BARRIER_001 §6), not the target.

## 0. Corpus / index check and new reason
- Read: BARRIER_001 (Thm 3, Thm 5, §6 D2), BARRIER_EST_001 (Thm 4), INV_P_001 (P1 Mellin defect, P2 band), INV_L_001 (L1–L3),
  Paper 47 def:W/eq:nuw, lem:degen, lem:contA, prop:shape-eulerdel, thm:log5A, cor:Tarch, cor:margin1.
- Index hits: **06_ R4 (Ω_Φ) "functional inequality controlling the window negativity by the Poisson–Euler residual"**, dead
  sub-route "perturbative or Lipschitz 𝒦_T linearized at Λ is tautological (N_010 §3)"; 02_ MONO (stability/monotonicity of LWF);
  AUDIT_193 #28/#101 (amplitude homotopy W(α); spectral-flow/no-crossing = positivity); INV_P (P2 band defect not entering sign).
- **New reason (written):** N_010 §3 kills the *linearization* at Λ. Door D2 asks for an arbitrary, non-linear, non-local defect
  Δ_T (global FE of the completed Euler product) and for a *continuation/homotopy* from a provably positive comb. Neither the
  non-linear case nor the homotopy is covered by N_010 or AUDIT_193 #101 (which concerns spectral flow of a fixed form, not a path
  in comb space). The result below covers every Δ_T and every path, so it is a strict generalisation, not a retry.

## 1. The family 𝓔𝓟 and the defect Δ_T (definitions)
Window: N=⌈e^{2T}⌉, v_n(a)=a(n)/√n, 𝔞_T^{(a)}, λ_A(T;a) as in BARRIER_001 §1 (Paper 47 def:W, eq:nuw); window collapse:
λ_A(T;a) depends only on π_N a.
- **𝓔𝓟 (Euler-product combs).** For θ=(θ_p)_p real with Σ_p |θ_p−1| p^{−1/4} < ∞, let a_θ(p^k)=θ_p log p, a_θ=0 off prime
  powers; ζ_{a_θ}(s)=∏_p(1−p^{−s})^{−θ_p} (Beurling-type real-exponent Euler product over ℕ). Contains Λ (θ≡1), a_P (θ_p=0 for
  p<P, 1 else; prop:shape-eulerdel), weight-perturbed Λ (finitely many θ_p≠1). 𝓔𝓟_Q := {θ : θ_p=1 for p∉Q}, Q finite.
- **Defect.** ξ_a(s):=s(s−1)π^{−s/2}Γ(s/2)ζ_a(s). Since ξ_Λ=ξ satisfies ξ(s)=ξ(1−s), on ½<σ<1 (where every factor (1−p^{s−1})
  is zero-free and the series converge)
    ℓ_θ(s) := log ξ_{a_θ}(s)/ξ_{a_θ}(1−s) = Σ_p (1−θ_p)[log(1−p^{−s}) − log(1−p^{s−1})]   (exact; the ζ-part cancels).
  Put Δ_T(a_θ) := sup{|ℓ_θ(s)| : σ=¾, |t|≤τ_T} with any fixed τ_T>0 (or an L² norm; nothing below depends on the choice).
  Δ_T ≥ 0, Δ_T(Λ)=0, Δ_T(a_P)>0 (the finite product ∏_{p<P}(1−p^{−s}) is not FE-invariant). This is the log-form of the INV_P
  defect D_S and the L1 defect, globalised.
- **(I_T; C)** : λ_A(T;a) ≥ −C·Δ_T(a) for all a ∈ 𝓔 (𝓔 ⊆ 𝓔𝓟 with Λ∈𝓔). This is BARRIER_001 (D2).

## 2. Lipschitz lemma (PROVED)
For all combs a,b: |λ_A(T;a) − λ_A(T;b)| ≤ d_v(a,b) := Σ_{n<N} |a(n)−b(n)|/√n.
*Proof.* For unit F, 𝔞^{(a)}(F)−𝔞^{(b)}(F) = −Σ_{n<N}(v_n(a)−v_n(b)) Re c_F(log n) and |c_F|≤‖F‖²=1; take inf over F (lem:degen
setting). ∎ Together with lem:degen: λ_A(T;·) is concave, d_v-1-Lipschitz, with supergradient w_T at Λ.

## 3. Theorem 1 (splitting; PROVED)
Let 𝓔∋Λ be any comb class, Δ:𝓔→[0,∞] any functional with Δ(Λ)=0, μ:=λ_A(T;Λ), C>0.
(a) (I_T;C) on 𝓔 ⟹ μ ≥ 0.
(b) [sufficiency] If μ ≥ 0 and **(Rig_C)** Δ(a) ≥ C^{−1}(d_v(a,Λ) − μ)_+ on 𝓔, then (I_T;C) holds.
(c) [necessity] (I_T;C) ⟹ μ ≥ 0 and **(Rig^w_C)** Δ(a) ≥ C^{−1}(⟨π_N(a−Λ), w_T⟩ − μ) on 𝓔.
*Proof.* (a) evaluate at a=Λ. (b) λ_A(a) ≥ μ − d_v(a,Λ) ≥ −CΔ(a) by §2. (c) lem:degen gives λ_A(a) ≤ μ − ⟨a−Λ,w_T⟩; combine with (I). ∎
**Reading.** (I_T) = WP_T(Λ) ∧ (a rigidity property of Δ). (Rig_C) involves only Δ and the comb (no form, no sign); (Rig^w_C) involves
only the direction w_T and the number μ. **The defect contributes no sign**: every bit of sign in (I_T) is the statement at Λ.
So D2 with a defect vanishing at Λ is REF-D ∧ (sign-free rigidity). This holds for *every* Δ, linear or not, local or global — it
extends N_010 §3 from the linearization to all defects.

## 4. Theorem 2 (continuation / homotopy is endpoint-equivalent; PROVED)
Let a_s (s∈[0,1]) be any path in 𝓔 with s↦π_N a_s d_v-continuous, a_1=Λ, Δ(a_s)>0 for s<1.
(i) (No early barrier.) For s<1, (I) at a_s forbids only λ_A(a_s) < −CΔ(a_s) < 0; it never forbids a zero crossing at s<1. The
crossing set {λ_A(a_s)=0} can be excluded by (I) only where Δ=0, i.e. at s=1.
(ii) (Reference positivity is inert.) Any information of the form λ_A(T;a_s) ≥ φ(s) on s∈[0,s₀] yields at the endpoint exactly
  μ ≥ sup_{s≤s₀} [φ(s) − d_v(a_s,Λ)],
and this is sharp in the class of concave d_v-1-Lipschitz functions of a (the only structure §2 and lem:degen provide).
In particular WP_T(a_0) with margin λ_A(a_0) transfers to Λ only if λ_A(a_0) > d_v(a_0,Λ); by BARRIER_001 Thm 5 / BARRIER_EST_001
Thm 4 this needs a_0 within d_v-distance ≤ λ_A(T;a_0) of Λ, and λ_A(T;Λ) ≤ 4·10⁹ T e^{−15.449T} (cor:margin1) for T≥1.
(iii) (Straight segments give upper bounds only.) On a_s=(1−s)a_0+sΛ, concavity gives λ_A(a_s) ≥ (1−s)λ_A(a_0)+sμ, i.e. interior
data bound μ from **above**: μ ≤ [λ_A(a_s) − (1−s)λ_A(a_0)]/s. No lower bound on μ follows beyond (ii).
(iv) (Limit form.) (I) on {a_s: s<1} with Δ(a_s)→0 implies μ≥0 by continuity (lem:contA-type/§2), without using a_0. So any
"defect-controlled continuation" proof of WP_T(Λ) contains a proof of λ_A(a_s) ≥ −CΔ(a_s)→0, i.e. of near-positivity at combs
d_v-close to Λ to precision → 0: the target at the limit.
*Proof.* (i) is the shape of (I). (ii): §2 gives μ ≥ λ_A(a_s) − d_v(a_s,Λ) ≥ φ(s) − d_v; sharpness: g(a):=min(φ(s₀), μ' + ...)—
explicitly, for any value μ' < sup[φ − d_v] fails, the function g(x)=min_s[φ(s)+d_v(x,a_s)] (inf-convolution, concave on segments
of the path's convex hull is not needed: g is 1-Lipschitz, ≥φ on the path data, and g(Λ)=sup-bound is attained) shows no better
bound is implied. (iii) concavity (lem:degen). (iv) §2. ∎  [Sharpness clause: PROVED for the Lipschitz class; the concave-and-
Lipschitz refinement via inf-convolution of affine minorants: ARGUED.]
**Consequence (NO-GO, class 𝒦_cont).** Methods of the form "positive reference comb + path to Λ + defect barrier / no-crossing"
cannot supply the sign: the reference is inert unless within the margin (precision ≤ λ_A, BARRIER_EST), and the barrier bites only
at Λ. This is the comb-space analogue of AUDIT_193 #101 (no-crossing = positivity), now PROVED for every path and every Δ.

## 5. What is proved positively (Theorem 3)
(a) [Finite-prime rigidity; PROVED qualitatively] For finite Q, θ↦ℓ_θ is linear injective on ℝ^Q (the functions
h_p(s)=log(1−p^{−s})−log(1−p^{s−1}) on σ=¾, |t|≤τ are real-analytic in t and linearly independent: their analytic continuation in t
is i·2π/log p-periodic in the imaginary direction with rationally independent periods — ARGUED in this form; PROVED alternatively by
the Dirichlet-series uniqueness of Σ_p c_p log(1−p^{−s}) in σ>1 after analytic continuation, since the h_p-combination vanishing on a
segment vanishes on ½<σ<1 and its p^{−s}-part determines c_p). Finite dimension ⇒ (Rig_C) on 𝓔𝓟_Q with C=C(T,Q,τ)<∞ (not explicit).
(b) [Hence] On 𝓔𝓟_Q: (I_T;C(T,Q)) ⟺ WP_T(Λ). For 0<T≤½log5, (I_T) is **PROVED** on every 𝓔𝓟_Q (thm:log5A + (a) + Thm 1(b)).
For T∈[0.60,½log P] it is satisfied by a_P only because Δ(a_P)>0 (consistent with prop:shape-eulerdel).
(c) [Tails; OPEN] On all of 𝓔𝓟 (infinitely many θ_p≠1, including p≥N, which λ_A ignores but Δ sees), (Rig_C) can fail: high-p
terms can approximate on a bounded segment the window terms (density of {p^{−it}} on bounded t-intervals), so a uniform
C_T needs Δ evaluated on an unbounded or σ-varying region. Quantitative rigidity with tails = OPEN; it is sign-free by Thm 1.

## 6. Self-check
- **BARRIER_001 trichotomy.** Ψ(a)=−CΔ_T(a) is non-uniform and non-affine (|ℓ_θ| is a norm of a non-linear function of θ for a
  general class; on 𝓔𝓟_Q it is a norm of a linear image, i.e. convex, still not of certificate form inf_τ[s_T+ν̂+β·ĝ]). So D2 is
  genuinely outside (i),(ii). Thm 1 shows it is (iii) **plus** a sign-free rigidity: the sign enters only through WP_T(Λ). The door
  is therefore not a sign source; it is a *re-packaging* of REF-D whose added content (Rig) is provable (finite Q) but signless.
- **Six clauses (prop:spec).** (1) comb-generic? Δ separates a_P (passes). (2)/(3) not cone, not integrality (passes). (4) not
  sparse-stable (passes). (5) reads the global FE (passes literally). (6) O_6/O_4 falsifiers have Δ>0 (passes). It passes all six
  and still carries no sign: confirms that the six clauses are necessary, not sufficient (already ARGUED in prop:spec).
- **REF-D trap.** Avoided only formally: Thm 1(a) shows any proof of (I_T) on a class containing Λ proves WP_T(Λ) by evaluation;
  Thm 2 shows that removing Λ from the class and passing to the limit does not change this.
- **Semiring principle.** Δ_T is built from the multiplicative (Euler) side alone; the additive interplay at m≈kn does not enter.

## 7. Labels and exact obstruction
PROVED: §2 Lipschitz; Thm 1 (a)–(c); Thm 2 (i),(ii) bound, (iii),(iv); Thm 3(b) for T≤½log5 (given (a)); (a) qualitative
(one proof ARGUED, one PROVED). ARGUED: concave-class sharpness in Thm 2(ii). OPEN: tail rigidity Thm 3(c) (sign-free).
**Exact obstruction (one line):** for any defect Δ vanishing at Λ, the defect-stability inequality equals WP_T(Λ) conjoined with a
sign-free rigidity of Δ, and any continuation from a positive reference comb transfers only λ_A(a_0) − d_v(a_0,Λ), which is
negative unless a_0 lies inside the e^{−15.4T} margin. Door D2 as a sign source: **NO-GO (class 𝒦_D2 = defect barriers +
comb-space continuation)**. Row D: OPEN; no sign obtained. Surviving lead: none from D2; the sign must enter at Λ itself (door D1
or a non-continuation argument).

## 8. Response to AUDIT_197_HOSTILE (BARRIER_001 audit, received during writing)
- *"At a=Λ the bound is the target; ill-posed until Δ_T, 'near Λ', C_T fixed."* Agreed and made precise: Thm 1(a) is exactly
  this, and §1 fixes Δ_T, the class (𝓔𝓟, 𝓔𝓟_Q) and C_T (=C(T,Q,τ) from finite-dim rigidity). Thm 1 is stated for **every** Δ
  and every class, so no choice of Δ_T rescues the inequality form.
- *"Δ_T from D_{S_N} nearly retries INV_P_001/INV_Q_001."* Δ_T here is not D_{S_N}: it is the log-ratio of the completed **global**
  real-exponent Euler product ξ_{a_θ}(s)/ξ_{a_θ}(1−s) (exactly zero at Λ, no truncation to S_N, no Green/area identity, no band
  localisation). New reason: the memo uses no property of the defect except Δ≥0, Δ(Λ)=0 (Thm 1, Thm 2) and finite-dim injectivity
  (Thm 3); the conclusions hold for D_{S_N}-based Δ too, so INV_P/INV_Q are not re-run, they are subsumed as instances.
- *"Keep the homotopy/continuity formulation (non-circular)."* That formulation is Thm 2, and it is closed: by concavity and the
  Lipschitz lemma the reference comb transfers only λ_A(a_0) − d_v(a_0,Λ), and (I) cannot exclude a crossing where Δ>0.
  A continuation that escapes Thm 2 must use information other than "λ_A(a_s) ≥ φ(s)" plus concavity/Lipschitz — e.g. an
  *openness* statement at crossings (a structural reason why ker of 𝔞_T^{(a_s)} cannot appear at s<1), which is a kernel/rigidity
  statement on the form, not on Δ. Recorded as the only residual of D2 (OPEN, not attempted here).
- *K_T convexity.* Consistent: K_T={a: λ_A(T;a)≥0} is convex (superlevel of concave μ_T), Thm 5's half-space is a supporting
  half-space at Λ only when μ=0; Thm 2(iii) is the same convexity. Minimizer non-uniqueness does not affect §2–§4 (only the
  supergradient inequality of lem:degen, valid for any real unit minimizer, is used).
