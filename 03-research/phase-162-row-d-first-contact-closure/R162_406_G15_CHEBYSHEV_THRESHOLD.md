# R162_406 — G1.5: the collar residual through compressed Chebyshev across the threshold e^{2T_*}

Round 4, mechanism G1.5.

Status: **NO-GO (PROVED) for Gate 1 through the minimality line, with four PROVED STEPS.** The
minimality line G1.x is exhausted. Gate 1 is OPEN. The closing input is stated as Conjecture 7.1.

- PROVED STEP 1 (§2, collar formula, three regimes). For δ < δ_1 (δ_1 fixed by the first integer
  above e^{2T_*}), the right collar residual is
  ξ_+ = −γ_F − Σ_{d<e^{2T_*}} ℓ_d V_{log d}F − θ ε ℓ_{n_0} ϱF − r on (T_*, T').
  Here ϱ is the reflection t ↦ 2T_* − t, θ = 1 iff n_0 = e^{2T_*} is a prime power, and every old
  translate reads F at a point strictly inside I_{T_*}. The left collar residual is ε times the
  reflection of ξ_+.
- PROVED STEP 2 (§3, Chebyshev across the threshold). Prop. 2.3 of R162_404 at the window T' gives
  B_{T'} = (Z_{T'}^*)^{−1} X Z_{T'}^* − X exactly. On the collar it yields
  ξ_+ = −γ_F − (Z_{T'}^*)^{−1}XZ_{T'}^*EF − r. At degree n_0 = e^{2T_*} ∈ ℤ the coefficient of the
  reflected edge germ is n_0^{−1/2}(log n_0 − Σ_{d|n_0, d<n_0} a(d)). This is the unique Λ*1 = log step
  at the threshold. It vanishes at a composite non-prime-power n_0 exactly because Λ*1 = log.
  It equals n_0^{−1/2}a(n_0) for any weight a.
- PROVED STEP 3 (§4, the R_L-part of the residual). ξ_F = −γ_F^{[1,L]} + ξ_F^{>L}, where
  γ_F^{[1,L]}(t) = Σ_{1≤j≤L} e^{−a_jt}μ_F(a_j) is an exact linear image of R_LF. Its coefficients are
  e^{−a_jt} and do not involve Λ. Λ enters ξ only through the comb, which carries values of F and not
  Gamma residues. The only Λ-dependent Gamma coefficients, d_m = −ζ'/ζ(s_m) (by Chebyshev
  = −ζ'(s_m)/ζ(s_m)), appear only after pairing over the **whole** exterior (T_*, ∞). That pairing is
  eq:collar, and it is not a collar datum.
- PROVED STEP 4 (§5, signed Gamma energy is linear in the variation). The only positive-definite
  Gamma quantity reachable from ξ is the exterior Cauchy–Hankel energy
  ‖γ_F‖²_{L²(T_*,∞)} = Σ_{j,m} μ_F(a_j)μ_F(a_m)e^{−(a_j+a_m)T_*}/(a_j+a_m). By Lemma 2.1 of R162_405,
  it enters the variational problem at T' only in the **linear** term 2s⟨ξ, η⟩. That term is
  sign-blind in s.
- NO-GO (§6). Combining Steps 1–4 with the collar identity (λ_δ < 0, λ_δ → 0) and H_{T_*}F = 0 yields
  only the list (a)–(c) of R162_405 Thm 5.1. The Chebyshev rewriting is an automorphism of the
  compressed Dirichlet algebra 𝒟_{T'} (Möbius inversion), so it adds no relation. F1 and F3 are
  verified.

Notation follows R162_404/405: 𝔞_T = 𝔪_T − ⟨(B_T + B_T^*)·,·⟩, κ(x) = −Σ_{j≥0}e^{−a_j|x|},
a_j = 2j + ½, s_j = 2j + 1, ℓ_d = Λ(d)d^{−1/2}, μ_F(a) = ∫e^{at}F, K_F(a) = ∫e^{−at}F, and
μ_F = εK_F for JF = εF. N = ker H_{T_*}, T' = T_* + δ, C_± are the right and left collars, and E is
zero extension. V_c is the right shift, τ_c the left shift, and X is multiplication by t.
(R_LF)_m = b_m e^{−a_m(T+δ_0)}K_F(a_m) (Paper 46, eq:Gammaenergy normalisation, b_m ≠ 0), 1 ≤ m ≤ L.

## 0. Corpus check

- **R162_404 Prop. 2.3** (B^*Z_T = K_T, exact) is used here at the window T' for the first time. That
  note never used it (§2 there, final paragraph). R162_404 §7-F3 records that the Prop fails for Λ+η_0
  by D(η_0*1). §6.2 below shows this failure is an artefact of fixing Z = D(1), and that the adapted
  comb Z_f restores it for every weight.
- **R162_401 / R162_403** ([X, Z] = −K; H^{(P)} = 0). The identity of Step 2 is the compressed
  version of the same log-derivative identity. The lesson recorded in the README ("X, J,
  Dirichlet-multiplier identities are symbol identities and fail F1") is confirmed here in collar form
  (§6.1).
- **R162_405** (collar identity Thm 2.2, non-extendability Thm 3.1, Lemma 1.1). Used as stated. Step 1
  gives the explicit formula for its ξ, which R162_405 §1 had only in unexpanded form.
- **P124_004 §5** (birth terms carry no divided rate). Consistent with §4.3 below: the threshold atom
  of regime II reads an edge germ of F, and has no δ-rate independent of the collar profile of F_δ.
- **Paper 46 eq:collar** (RB_N = D_NR − ℰ_N). This is the full-exterior form of the pairing in
  Step 3.
- R160 survey (NG-F1: smoothness, not multiplicativity, controls the localized sign) is consistent
  with Step 2: the Chebyshev content at the threshold is a single coefficient identity.

## 1. Preliminaries

**Lemma 1.1 (threshold gap).** Let n_1 be the least integer > e^{2T_*}, and let
δ_1 = ½ log(n_1 e^{−2T_*}) ∧ ½ log 2. For 0 < δ < δ_1:
(i) the only integer in [e^{2T_*}, e^{2T'}) is n_0 = e^{2T_*}, and only if e^{2T_*} ∈ ℤ;
(ii) for d < e^{2T_*} and t ∈ (T_*, T'), t − log d ∈ (−T_* + (2T_* − log d), T_* − log 2 + δ), a
compact subinterval of I_{T_*} (interior translates);
(iii) for integers n ≥ n_1 and t ∈ (T_*, T'), t − log n < −T_*, so V_{log n}F vanishes on C_+.

*Proof.* (i) holds by the definition of n_1, since e^{2T'} < n_1. (ii) t − log d > T_* − log d > −T_*
because d < e^{2T_*}, and t − log d < T' − log 2 < T_* − log 2 + δ < T_*. (iii) We need
log n > T' + T_* = 2T_* + δ. This holds because log n ≥ log n_1 = 2T_* + 2δ_1 > 2T_* + δ. ∎

This gives three regimes:
- (I) e^{2T_*} ∉ ℤ;
- (I′) e^{2T_*} = n_0 ∈ ℤ, not a prime power;
- (II) e^{2T_*} = p^k, a prime power.

## 2. The collar formula (PROVED STEP 1)

**Theorem 2.1.** Let F ∈ L²(I_{T_*}) with JF = εF, let r ∈ span{e^{±t/2}} with Jr = εr, and put
γ_F(t) := Σ_{j≥0} e^{−a_jt}μ_F(a_j) for t > T_*. For 0 < δ < δ_1 the residual (R162_405 (1.1)) is,
as an element of (𝒬 ∩ L²(C_+))′,

    ξ_+(t) = −γ_F(t) − Σ_{2≤d<e^{2T_*}} ℓ_d F(t − log d) − θ ε ℓ_{n_0} F(2T_* − t) − r(t),        (2.1)

where θ = 1 in regime II and θ = 0 otherwise. On C_−, ξ_−(t) = ε ξ_+(−t).

*Proof.* On C_+, MF = ∫κ(t − u)F(u)du = −γ_F (R162_404 §4, termwise by Tonelli), and B^*_{T'}EF = 0.
Also B_{T'}EF(t) = Σ_{d<e^{2T'}} ℓ_d F(t − log d). By Lemma 1.1(iii) only d ≤ n_0 contribute. The d
with d < e^{2T_*} give the old translates. The term d = n_0 is present iff Λ(n_0) ≠ 0, which is
regime II. In that case F(t − 2T_*) = F(−(2T_* − t)) = εF(2T_* − t). For C_−, JMJ = M,
JB_{T'}J = B_{T'}^*, Jr = εr and JF = εF give (JΞ)(t) = εΞ(t) for the full residual Ξ. ∎

**Remarks.** (i) In regimes I and I′ the collar sees only the analytic Gamma tail, translates of F
restricted to compact subintervals of I_{T_*}, and r. In regime II it additionally sees the edge germ
F|_{(T_*−δ, T_*)}, reflected across T_*, with weight εℓ_{p^k}.
(ii) Edge singularity. κ(x) = −1/(2x) + O(1) as x ↓ 0. If F has a one-sided value F(T_*−) = c, then
γ_F(T_* + s) = (c/2) log(1/s) + O(1) as s ↓ 0. This holds conditionally on the existence of that
value; F ∈ 𝒬 does not guarantee it. In regime II the threshold term, −εℓ_{p^k}c + o(1), is bounded.
So in regime II both the leading singular term and the threshold term are governed by the same edge
germ of F.
(iii) Theorem 2.1 does not use H_{T_*}F = 0. It holds for every F ∈ L²(I_{T_*}) and every r.

## 3. Compressed Chebyshev across the threshold (PROVED STEP 2)

**Lemma 3.1.** On L²(I_{T'}), [X, PV_cP] = cPV_cP and [X, Pτ_cP] = −cPτ_cP. Hence
[X, Z_{T'}^*] = K_{T'}^* and [X, Z_{T'}] = −K_{T'}.

*Proof.* P commutes with X. Also (XV_c − V_cX)g(t) = tg(t − c) − (t − c)g(t − c) = cg(t − c), and
similarly for τ_c. Sum with the weights n^{−1/2} and (log n)n^{−1/2}. ∎

**Theorem 3.2 (Chebyshev collar formula).** For F ∈ L²(I_{T_*}) and 0 < δ < δ_1,

    B_{T'} = (Z_{T'}^*)^{−1} X Z_{T'}^* − X,     B_{T'}^* = X − Z_{T'}^{−1} X Z_{T'},              (3.1)
    ξ_+ = −γ_F − ((Z_{T'}^*)^{−1} X Z_{T'}^* EF)|_{C_+} − r|_{C_+}.                                (3.2)

*Proof.* R162_404 Prop. 2.3 at T' gives B_{T'}^*Z_{T'} = K_{T'}; its adjoint is Z_{T'}^*B_{T'} = K_{T'}^*.
Z_{T'}^* is invertible (R162_404 Cor. 2.2), and Lemma 3.1 gives (3.1). XEF vanishes on C_+. ∎

**Proposition 3.3 (the threshold coefficient).** Write (Z_{T'}^*)^{−1}XZ_{T'}^* − X = Σ_{n<e^{2T'}} c(n)
n^{−1/2}PV_{log n}P in 𝒟_{T'}^*. Then c = μ*(1·log) = Λ. At degree n_0 = e^{2T_*} ∈ ℤ,

    c(n_0) = log n_0 − Σ_{d|n_0, 1<d<n_0} Λ(d),                                                    (3.3)

and n_0^{−1/2}PV_{log n_0}P EF = F(· − 2T_*) on C_+ is the reflected edge germ. More generally, for a
weight a: ℕ → ℝ with a(1) = 0 and B_a := D^*(a), the identity B_a = (Z^*)^{−1}XZ^* − X +
(Z^*)^{−1}D^*(a*1 − log) holds, and the coefficient of the reflected edge germ in ξ^a_+ is
n_0^{−1/2}[(a*1)(n_0) − Σ_{d|n_0, d<n_0} a(d)] = n_0^{−1/2}a(n_0).

*Proof.* In 𝒟^*_{T'} the element (Z^*)^{−1}[X, Z^*] corresponds to μ*(log) = Λ (Möbius inversion of
Λ*1 = log, truncated at e^{2T'}; R162_404 Prop. 2.1). Its value at n_0 is (3.3) by
log n_0 = Σ_{d|n_0}Λ(d). At a composite non-prime-power n_0 (regime I′), the new operator
n_0^{−1/2}PV_{log n_0}P ≠ 0 appears in Z_{T'}^* and K_{T'}^*. It also appears through the compositions
PV_{log d}PV_{log(n_0/d)}P = PV_{log n_0}P (Lemma 1.1(a) of R162_404; at the window T_* these
compositions vanish because log n_0 = 2T_*). The total coefficient is log n_0 − Σ_{d|n_0,d<n_0}Λ(d) = 0.
The same computation with a in place of Λ gives the general statement, and the bracket equals a(n_0)
by definition of Dirichlet convolution. ∎

**Reading.** Regime I′ is the one place where compressed Chebyshev does non-trivial work across the
threshold. The log n_0 carried by the new integer in K_{T'} is exactly cancelled by the composed old
atoms, which switch on at T' because the semigroup relation PV_aPV_bP = PV_{a+b}P now has a + b < 2T'.
So Λ*1 = log is **exactly** the statement that a composite threshold creates no edge reflection in ξ.
For a = Λ + η_0 with η_0(n_0) ≠ 0 the reflection appears, with coefficient n_0^{−1/2}η_0(n_0). This is
the Λ-specific link the task asked for. Its coefficient multiplies the edge germ of F, not any Gamma
residue.

## 4. The R_L-part of the residual (PROVED STEP 3)

**Proposition 4.1.** For every L ≥ 1 there is a linear map ℓ_L: ℂ^L → C^∞([T_*, ∞)),
ℓ_L(v)(t) = Σ_{m=1}^L ε b_m^{−1}e^{a_m(T_*+δ_0)} v_m e^{−a_mt}, which is injective and has Λ-free
coefficients, such that

    ξ_F = −ℓ_L(R_LF) + ξ_F^{>L},   ξ_F^{>L} := −Σ_{j>L} e^{−a_jt}μ_F(a_j) − (comb) − r   on C_+.   (4.1)

The j = 0 term is absent because μ_F(½) = A(F) = 0. Moreover
‖ℓ_L(R_LF)‖_{L²(T_*,T_*+δ)} ≤ C_L δ^{1/2}‖R_LF‖.

*Proof.* μ_F(a_m) = εK_F(a_m) = εb_m^{−1}e^{a_m(T_*+δ_0)}(R_LF)_m. Injectivity follows because the
exponentials e^{−a_mt} are independent on any interval. The bound holds because the functions are
bounded on [T_*, T_*+1]. ∎

**Corollary 4.2 (where Λ can meet R_LF).** In (4.1), R_LF enters only through Λ-free exponentials,
and Λ enters only through the comb. The comb is a combination of values of F on compact subintervals
of I_{T_*} (Thm 2.1) and carries no μ_F(a_j). A Λ-dependent coefficient in front of μ_F(a_m) arises
only by pairing the comb with e^{−a_mt} over the whole exterior:

    ∫_{T_*}^∞ e^{−a_mt}(LF)(t)dt = Σ_d Λ(d)d^{−s_m}K_F(a_m) − Σ_d Λ(d)d^{−s_m}K_F^{[−T_*, T_*−log d]}(a_m),  (4.2)

with Σ_dΛ(d)d^{−s_m} = −ζ'/ζ(s_m). By Chebyshev (ζ·(−ζ'/ζ) = −ζ'), this is −ζ'(s_m)/ζ(s_m). (4.2) is
Paper 46 eq:collar (d_m = d_{m,∞}, second term = ℰ). The test e^{−a_m t}1_{(T_*,∞)} is not supported
in any collar C_δ, and it is not in 𝒫_{T'} for any finite T'.

*Proof.* Substitute u = t − log d (Fubini; absolute convergence for a_m ≥ 5/2). ∎

**4.3 (leading order as δ → 0).** If F(T_*−) = c ≠ 0 (conditional), then by Remark 2(ii)
‖γ_F‖_{L²(T_*,T_*+δ)} ≍ |c|δ^{1/2}log(1/δ). This is dominated by the tail j > L. The R_L-part is
O(δ^{1/2}) by Prop. 4.1. So on shrinking collars, **R_LF is subleading** in ξ: the collar
sees the boundary behaviour of g(z) = Σμ_F(a_j)z^j on its circle of convergence |z| = e^{−2T_*}
(R162_405 Lemma 1.1), whereas R_LF is the Taylor germ of g at z = 0. The only exact bridge between
the two is analytic continuation of g across the whole disc, that is, the whole exterior. This is
(4.2) again.

## 5. The signed Gamma energy enters linearly (PROVED STEP 4)

**Proposition 5.1.** (a) ‖γ_F‖²_{L²(T_*,∞)} = Σ_{j,m≥1}μ_F(a_j)μ_F(a_m)e^{−(a_j+a_m)T_*}/(a_j+a_m).
This vanishes iff F = 0.
(b) For η_c := χ_δγ_F on C_+ (χ_δ a cutoff to (T_*, T')), extended by parity and made primitive by an
interior correction φ ∈ C_c^∞(I_{T_*}) as in R162_001 Step 3, put η := η_c + φ ∈ 𝒫_{T'} ∩ 𝒬.
Then 𝔞_{T'}(EF + sη) = 2s⟨ξ_F, η_c⟩ + s²𝔞_{T'}(η) for F ∈ N, and
⟨ξ_F, η_c⟩ = −2‖χ_δ^{1/2}γ_F‖² − 2⟨comb + r, χ_δγ_F⟩_{C_+}.

*Proof.* (a) Expand the square. The Cauchy matrix (1/(a_j+a_m)) = (∫_0^∞e^{−(a_j+a_m)x}dx) is
positive definite, and faithfulness is R162_405 Lemma 1.1. (b) Use R162_405 Lemma 2.1 and 𝔞_{T'}(EF) =
0. The factor 2 is the two collars, by parity. ∎

So the one positive-definite Gamma quantity appears with a definite sign inside ⟨ξ, η⟩. But ⟨ξ, η⟩ is
the coefficient of s, and s ranges over both signs. Hence the minimisation produces
λ_A(T') ≤ −⟨ξ_F,η_c⟩²/(𝔞_{T'}(η)^+ ...), an upper bound (R162_101 §3) in which the sign of the Gamma
energy is squared away. This is F2 (orientation loss) in its sharpest form.

## 6. Decision (NO-GO, PROVED)

**Theorem 6.1.** Let T_* be a first-contact window (regime I, I′ or II). Every consequence of
(i) H_{T_*}F = 0 and H_{T_*} ≥ 0, (ii) the collar identity λ_δ⟨F_δ, EF⟩ = ⟨ξ_F^δ, F_δ|_{C_δ}⟩ with
λ_δ < 0 and λ_δ → 0, and (iii) Theorems 2.1, 3.2, Prop. 3.3, 4.1, 5.1, is a consequence of (i)–(ii)
alone. Hence (R162_405 Thm 5.1) it is one of (a) the eigen-equations, (b) non-extendability N ≠ V_0,
(c) sign⟨ξ_G^δ, F_δ|_{C_δ}⟩ < 0. None of these forces R_LF = 0.

*Proof.* Theorem 2.1 is the definition (1.1) of R162_405 evaluated using supports only (Remark 2(iii)).
Theorem 3.2 and Prop. 3.3 follow from Theorem 2.1 by the identity B_{T'} = D^*(Λ) =
D^*(μ*log) = (Z^*)^{−1}[X, Z^*], an identity in the commutative algebra 𝒟^*_{T'}. Here Z^* is
invertible (unipotent), so the rewriting is an equivalence: every relation expressible through
(3.1)–(3.3) is one expressible through B_{T'} directly, and conversely. Prop. 4.1 is a relabelling of
μ_F(a_m), m ≤ L. Prop. 5.1 is (2.1) of R162_405 at a particular test. So (iii) adds no relation
among F, r, F_δ, λ_δ beyond those in (i)–(ii). The remaining assertion is R162_405 Thm 5.1. For
completeness, (c) with (4.1) reads

    −⟨ℓ_L(R_LG), F_δ⟩_{C} + ⟨ξ_G^{>L}, F_δ⟩_C = λ_δ⟨F_δ, EG⟩ < 0.

This is one real inequality, in which R_LG is paired against the unknown collar profile of F_δ (sign
not determined by G) and is subleading to the tail term (§4.3, when F(T_*−) ≠ 0). A single inequality
cannot force the vector R_LG ∈ ℂ^L to vanish. For instance, it is compatible with R_LG ≠ 0 as soon as
the tail term is negative. ∎

**Exact obstruction.** Compressed Chebyshev at the threshold is a *coefficient identity in 𝒟_{T'}*. It
decides which atoms of the comb meet the collar: no reflection at a composite threshold, weight
ℓ_{p^k} at a prime-power threshold. It does not convert comb data into Gamma data. The conversion (4.2)
carries the Λ*1-dependent coefficient −ζ'(s_m)/ζ(s_m), but it requires the whole exterior (T_*, ∞),
which no window T' = T_* + δ contains. On the collars the Gamma residues appear with Λ-free
coefficients e^{−a_jt}, and the R_L-part is subleading.

### 6.1 F1 (first contact vs strictly decreasing positive ground state)

Theorems 2.1, 3.2 and Props. 3.3, 4.1, 5.1 hold for every F ∈ L²(I_{T_*}) (Remark 2(iii)). At a window
T with λ_A(T) = λ > 0 and λ_A strictly decreasing, the ground state F satisfies (2.2λ) of R162_405,
(λ_δ − λ)⟨F_δ, EF⟩ = ⟨ξ_F, F_δ⟩ < 0, with ξ_F given by (2.1)/(3.2) verbatim, in the same three regimes.
By eq:Qspectral such F have R_LF ≠ 0. So the collar–Chebyshev package cannot distinguish first
contact from a positive strictly decreasing ground state. The only distinguishing datum, λ(T_*) = 0,
enters through λ_δ − λ, which is covariant under λ ↦ λ − c. Plateau windows are distinguished only by
the open condition N ≠ V_0 (R162_405 Thm 3.1(e)). **F1 is PASSED as a falsifier: the NO-GO is
correct and the package proves no falsehood.**

### 6.2 F3 (finite modifications and Davenport–Heilbronn)

(a) For a = Λ + η_0 the collar formula changes exactly by −Σ_{d<e^{2T_*}}η_0(d)d^{−1/2}F(t − log d)
− n_0^{−1/2}η_0(n_0)F(t − 2T_*). By Prop. 3.3 this is the Chebyshev defect D^*(a*1 − log) seen through
(Z^*)^{−1}. So Λ*1 = log is visible, but only as the absence of these atoms.
(b) The defect is an artefact of fixing Z = D(1). For any a with a(1) = 0, put
f := exp_*(a/log), the Dirichlet-series exponential Σ_k (a/log)^{*k}/k! (where (a/log)(n) =
a(n)/log n). Then f(1) = 1 and a*f = f·log (formal logarithmic derivative). Z_f := D(f) is unipotent
in 𝒟_{T'}, and B_a^*Z_f = K_f := D(f log) holds exactly. Theorem 3.2 holds with Z_f, and ξ^a has the
same shape (2.1). For Davenport–Heilbronn data, f is the DH coefficient sequence (f(1) = 1, no Euler
product), and the same holds. **So every statement of §§2–5 has an exact analogue for every weight a,
including DH.** The only Λ-specific feature, f ≡ 1 (completely multiplicative, non-negative), enters ξ
nowhere, because ξ involves only a (Theorem 2.1) and M. F3 is satisfied by the NO-GO: no step of the
package is Λ-specific in the sense of Problem prob:annihilate (iii).
(c) Modifications with supp η_0 ⊂ [e^{2T'}, ∞) leave 𝔞_T unchanged for T ≤ T'. Any argument local to
[T_*, T'] is therefore identical for Λ and such a. A closing argument must use Λ on (1, e^{2T'}), and
by (a)–(b) the collar sees Λ there only through the atom set.

## 7. What would close Gate 1 (clean conjecture)

By Theorem 6.1 and R162_101 §6.2 (item 2), the minimality line needs one independent, two-sided input
to the right of T_*. By (2.2) of R162_405 and ⟨F_δ, EG⟩ → 1, it suffices to supply the following.

**Conjecture 7.1 (two-sided collar law at first contact).** Let T_* be a first-contact window, and let
G ∈ N_{T_*} (parity ε) be the Lemma-5 limit of parity ground states F_δ at T_* + δ. Let L be injective
on N_{T_*}. There are functions κ, κ' > 0 on (0, δ_1) with κ(δ)/κ'(δ) → 0 as δ ↓ 0 such that

    (LB)  λ_A(T_* + δ) ≥ −κ(δ),
    (NE)  |⟨ξ_G^δ, F_δ|_{C_δ}⟩| ≥ κ'(δ)‖R_LG‖².

*Consequence (PROVED given 7.1).* By (2.2), |λ_δ|(1 + o(1)) = |⟨ξ_G^δ, F_δ⟩| ≥ κ'‖R_LG‖². With (LB),
‖R_LG‖² ≤ (1 + o(1))κ/κ' → 0. So R_LG = 0, hence G = 0 (L is injective), which contradicts ‖G‖ = 1.
Therefore no first contact exists, and by R162_001 (Consequence) and Paper 45 Thm 11.3, RH follows.

Requirements, from the falsifiers:
- (NE) is a quantitative form of non-extendability (R162_405 Thm 3.1, Lemma 1.1). Theorem 2.1 and
  §4.3 suggest that the natural rate is κ'(δ) ≍ δ·(collar profile). By F1, (NE) with some κ' also
  holds at positive strictly decreasing windows. So (NE) alone is not the arithmetic input.
- (LB) is the arithmetic input. It must fail at positive windows in the sense that there
  κ/κ' ↛ 0 (F1). It must fail for a = Λ + η_0 whenever η_0 meets (1, e^{2T'}), in particular at a
  composite threshold n_0 with η_0(n_0) ≠ 0 (§6.2(a), regime I′). It must also fail for DH. By
  §6.2(b), (LB) cannot come from any Dirichlet-algebra identity. It must use f ≡ 1 (the Euler product)
  quantitatively, for example as a local dual certificate (Paper 46 Theorem C / D1 type) on windows
  [T_*, T_* + δ] with deficit o(κ'(δ)).
- The sharpest threshold version is in regime II (e^{2T_*} = p^k). There the edge germ enters ξ both
  through the Hilbert singularity of γ_G and through the new atom εℓ_{p^k}ϱG (Remark 2(ii)). The
  sub-question is whether the sign of ε·G(T_*−)·(½log(1/s) − ℓ_{p^k}) is forced at first contact.
  That is the only place where a new Λ-weight and a Gamma singularity meet on the collar.

## 8. Status and next step

- G1.5: **NO-GO (PROVED)**, with PROVED STEPS 1–4 (§§2–5). The minimality line G1.1–G1.5 is
  **exhausted**. Left minimality equals H ≥ 0, right minimality equals non-extendability, and the
  Chebyshev threshold identity is an automorphism of 𝒟_{T'} that gives no new relation.
- Next step: attack (LB) of Conjecture 7.1 as a **local certificate problem to the right of T_*.** The
  question is whether the flat-top / dual-certificate machinery of Paper 46 (Theorems C, D1, Z) can
  give λ_A(T) ≥ −κ(T − T_*) with κ = o(δ) or o(δ/log(1/δ)), which matches the §4.4 heuristic of
  R162_405. Separately, quantify (NE) in regime II.

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
