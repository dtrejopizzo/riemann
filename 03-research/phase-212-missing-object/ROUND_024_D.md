# ROUND_024_D — Gate: object of degree ≥ 2 with the Möbius of the system μ_a and the boundary leak

Question. Is there an explicit formula of degree ≥ 2 in the weight a, built with μ_a (Dirichlet inverse
of b_a, where −ζ_a′/ζ_a = Σ a(n)n^{−s} and ζ_a = Σ b_a(n)n^{−s}) and with the compressed jump of ROUND_023_B
  D_p := E_{p,T} − E_{p−1,T} = p^{−1/2} P_T τ_{log p}(1−P_T)𝓕Π_T,
that is not a divisor variance (K2), a Selberg/Riccati identity, a congruence or a square?

Verdict: **DOES NOT PASS (repetition on the algebraic side; no mechanism on the rest).** The formulas can be
written, but each one falls into one of the four excluded classes, and none fails under the controls.

## (1) Closest antecedents (opened)

- phase-163 R163_144 §1, eq. (2): family r_{a,u} = μ_a∗(b_a·(·)^{−u}) for GENERAL weight a; derivatives
  r′ = −a, r″ = W_a := a·log + a∗a = μ_a∗(b_a·log²). It is exactly "degree 2 in the weight built with
  μ_a"; §2 gives positivity (6) only scalar at Gamma points; §3: does not reach the physical kernel. Master
  index l.14210–14214 (recorded as absent, fails by "scalar positivity, κ models equal").
- ROUND_004_A, ARGUED observation after (iv) and "NOT excluded" 3: with μ_a, M^{(a)}S^{(a)} = I + exterior holds
  for the whole family (pattern B1); E_N^{(a)} loses Poisson for a ≠ Λ. REVIEW_004 l.59 (R4-b).
- R166_502 §5 (Riccati δV + V² = Z⁻¹δ²Z = Selberg; §5.2: V∗V = Σ_p V_p∗V_p + Σ_{p≠q}V_p∗V_q, the comb
  of quotients is the Hermitian cross part that the convolution algebra does not touch); phase 70 E70_10–12;
  ROUND_002_C l.31, l.111–154 (linear and homogeneous channel: γ_{cΛ} = c·γ_Λ).
- ROUND_023_B §§2–3: the compressed jump is a(p)·(fixed operator); orienting it requires degree ≥ 2 (F3).
- RULES_AVOID K1 (squares of leaks), K2 (variance ½ΣΣΛ(d)Λ(e)‖m_d − m_e‖², generic).

## (2) What can be written

Let J_a := Σ_n a(n) n^{−1/2} P_T τ_{log n}(1−P_T)𝓕Π_T (weighted sum of jumps; linear in a).
The degree-2 objects that can be formed with J_a, μ_a, b_a and log are, exhausting the product types:

(A) Hermitian product: ⟨J_aF, J_aF⟩ = Σ_{m,n} a(m)a(n)(mn)^{−1/2}⟨τ_{log m}C_TF, P_Tτ_{log n}C_TF⟩,
    with C_T = (1−P_T)𝓕Π_T. It is a square of leaks (R161_002 Thm. 1.1; K1); its off-diagonal part
    m ≠ n is the variance/cross Gram of K2 (030–034) and the cross part of R166_502 §5.2.
(B) Composition: J_a∘J_a = Σ_{m,n} a(m)a(n)(mn)^{−1/2} P_Tτ_{log m}C_T P_Tτ_{log n}C_T. Without the intermediate
    compression (C_T P_T → 𝓕) the translations compose τ_{log m}τ_{log n} = τ_{log mn} and the coefficient is
    a∗a = μ_a∗(b_a·log²) − a·log: Riccati (R163_144 (2); R166_502 §5). With the compression, the coefficient
    of (m,n) depends on m and n separately (it is not a function of mn): there is no convolution identity; it is
    a bilinear form in a with no written sign, and its only known control is (A) via Cauchy–Schwarz
    (square).
(C) Conjugation by μ_a: X ↦ M^{μ_a} X S^{(a)} (S^{(a)} with coefficients b_a). It is a congruence/
    similarity (R162_903, N_BUILD_022, ROUND_022_A); its interior exactness M^{μ_a}S^{(a)} = I + exterior
    holds for every a (ROUND_004_A Lemma 3 generalized), hence it does not distinguish the weight.
(D) Higher-order expansions of μ_a (Faà di Bruno: μ_a∗(b_a·log^k) = polynomial in a, a·log, a∗a,…)
    are consequences of μ_a∗b_a = δ_1 and μ_a∗(b_a·log) = a; the only new degree-2 term at each
    order is another instance of the same Riccati equation.

I cannot write a fifth type: μ_a enters only by convolution (C,D) and J_a by product or composition (A,B).

## (3) Why it does not avoid the reason for failure

- Reason of R163_144: W_a ≥ 0 is scalar positivity on the Euler side, valid for every weight with positive Euler
  measure (κ models included). (B) without compression is W_a itself; with compression it loses the
  convolution structure that gave W_a and gains no sign.
- Reason of ROUND_004_A/B1: every identity built from μ_a holds identically in a (μ_a∗b_a = δ_1
  for every a); using μ_a instead of μ turns the identity of Λ into an identity of the family.
- Reason of K2/R166_502 §5.2: the cross part m ≠ n (comb of quotients m ≈ kn) is not seen by the
  convolution algebra; (A) sees it only as a Gram (square, without orientation, F3).
No type changes the hypothesis that caused the failure; only the notation (μ → μ_a) or the carrier
(translation → compressed jump) change, which the filter does not accept.

## (4) Connection with 𝔸_M ⪰ 0 and controls

Identity that would be needed (not available): a_T(F) = Φ_T(F) − ‖C-leaks‖² with Φ_T ≥ 0 by a term of
degree 2 in a that vanishes exactly at a = 2Λ (or Λ) and not on the controls; via Paper 47 prop:AM it would give
𝔸_M ⪰ 0 for M ≥ e^{2T}.
Named steps under the controls:
- weight cΛ / substituted weight: (C),(D) Riccati and μ_a∗b_a = δ_1 hold for every a: they do not fail. (A) ≥ 0
  for every a: does not fail. (B) compressed: no sign for any a: there is no step that fails.
- deletion of a prime power: same identities for the deleted weight (μ_a is recomputed): they do not fail.
- Beurling: the convolution identities use only the free generated semigroup; they hold in Beurling
  (R167_103 Thm. S for the sieve class): they do not fail.
(F1) unmet; (F2) also not: Arch enters only through P_T/𝓕 in J_a, not through μ_a.

## Status

- Inventory (A)–(D): ARGUED (exhaustion of product types, not a class theorem).
- Residue "Möbius of the system" of ROUND_004_A "NOT excluded" 3: reduced to R163_144 + (C); no
  new mechanism appears. Still without a general impossibility proof (OPEN as a class), but there is no
  written candidate that passes the gate.
- Pending record in Part V of the index (done at coordination); I did not edit the index.
