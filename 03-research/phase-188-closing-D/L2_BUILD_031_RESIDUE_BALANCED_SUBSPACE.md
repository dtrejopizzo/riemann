# L2_BUILD_031 — Residue-balanced test vectors: the constrained target is equivalent to D, not weaker

> **Aviso de corrección posterior (phase211, auditado):** la omisión de componentes p^b<=Q en§3 y su repetición en§4 no son válidas sólo por B_Q. CORRECTION_RESIDUE_BALANCE_031.md y su auditoría exhiben M=Q=2,s=(1,1), un perfil e interpolante suave declarados y pairingq2=v2/2>0. El TeoremaE de§2 permanece intacto. Se conserva abajo el texto histórico; no usar la supresión corregida.

## Corpus check
030 (Q = m^♯-form − Chebyshev fluctuation (q=1) − Σ_{p^b} additive-character components), 028 §1 (A_M ⟺ D by approximation of configurations), 029
(Near-free sets trivial); N_BUILD_021 (Prop 1: Near = s^T[Ξ_{F₀}(log(m/k)) − exact]s; Theorem 2: all progression/shifted-sum classes 𝒞_prog KILLED by finmod;
Prop 3: twisted vectors give a hybrid, conductor > 1 does not enter exactly). New: §1–§4.

## 1. Two precise constraint families (definitions)
(R_Q) Rough support: s_m = 0 unless (m, p) = 1 for every prime p ≤ Q.
(B_Q) Residue balance: s is a sum of blocks, each block a set of consecutive integers I = [x, x + L) with L a multiple of q_Q := lcm{p^b ≤ Q}, carrying a
    constant weight; then Σ_{m∈I, m≡r (p^b)} s_m is independent of r for every p^b ≤ Q. For such s the components of 030 §3 with modulus p^b ≤ Q vanish
    exactly in the block sums (complete residue systems: Σ_{r mod p^b} c_{p^b}(r) = 0, and every Ramanujan sum c_{p^b} is constant on residue classes).
    (That this kills the q = p^b components in the full quadratic form, not only at first order in the block sums, is ARGUED: the components are
    Ramanujan sums evaluated at j = kn with k in a balanced block; balance in k transfers to j only for p ∤ n.)
(B_Q) is the constraint asked for; (R_Q) is its multiplicative analogue (it kills the Div part of the small primes exactly).

## 2. Theorem E (both constrained families are equivalent to D; PROVED)
For any fixed Q: D ⟺ s^TA_Ms ≥ 0 for all M and all s in (R_Q) ⟺ the same for all s in (B_Q).
*Proof.* (⟹) restriction. (⟸) As in 028 §1 it suffices that the admissible vectors approximate F = Σ_j s_jτ_{a_j}F₀ for any finite configuration.
(R_Q): Q-rough integers have bounded gaps (≤ q_Q), so for c → ∞ there are rough m_j with |log m_j − c − a_j| ≤ q_Q e^{−c−a_j} → 0; continuity of B_{F₀}
gives the limit. (B_Q): put weight s_j/L on the block [⌊e^{c+a_j}⌋, ⌊e^{c+a_j}⌋ + L) with L = q_Q; all positions lie within log(1 + L e^{−c−a_j}) → 0 of
c + a_j, so Σ_{block pairs}(s_j/L)(s_l/L)Σ_{m∈I_j,k∈I_l}B(log m − log k) → s_js_lB(a_j − a_l). Hence B_{F₀} is positive definite and Theorem S gives D. ∎
**Consequence: the target "q = 1 Chebyshev fluctuation ≤ m^♯-form on the residue-balanced subspace (all M)" is EQUIVALENT to D — not a strictly weaker
partial result.** At a fixed M it is a finite section (weaker, trivially), with no M-uniform gain.

## 3. The finite target at fixed M (PROVED as an identity)
On (B_Q) ∩ {s supported in [1, M]}, with W_g as in 030:
  s^TA_Ms = s^TW_{m^♯}s − s^T𝔉_M s − (components with modulus p^b > Q),   𝔉_M := q = 1 Chebyshev-fluctuation matrix,
and the m^♯-form is bounded below by (C₀ + 4)·s^TW_1s (m^♯ ≥ m^♯(0) = C₀ + 4 ≈ −1.37, W_1 ⪰ 0). Dimension of (B_Q) ∩ [1, M]: ⌊M/q_Q⌋ blocks
(one weight each) — codimension ≈ M(1 − 1/q_Q). The target at M: s^TW_{m^♯}s ≥ s^T𝔉_M s + (large-modulus components) on that subspace. Note the
m^♯-form itself is NOT positive (lower bound negative), so even the "q = 1 only" target requires the fluctuation to be negative on the m^♯-negative
directions — the anti-alignment of 017, now in integer coordinates.

## 4. Escape analysis (PROVED)
- finmod: Theorem E's proof uses no property of Λ (only continuity of B and Theorem S, which hold for any comb with the same structure). Hence for the
  amplified comb Λ + c1_{n=2} (which fails D at T > ½log 2 for large c), the (R_Q)/(B_Q)-restricted family also fails. Amplification at a single n₀ still
  breaks it — no escape from cor:void. W-tail likewise (equivalence transfers every falsifier).
- The constraints kill the LOCAL Euler structure for p^b ≤ Q (Div of small primes exactly in (R_Q); small-modulus components in (B_Q)), but by Theorem E
  they lose no information about D: the local structure was never where the sign lives (029), and the global content passes intact into the
  remaining terms (Near / large-modulus components / q = 1 fluctuation), consistent with N_BUILD_021 §4.

## 5. Review
- Theorem E is the same approximation argument as 028 §1; the block version uses only continuity of B. PROVED.
- §1(B_Q) "kills exactly" is ARGUED beyond first order (noted); Theorem E does not depend on it.
- §3 identity is 030 §3 restricted; the lower bound C₀ + 4 for m^♯ is N_BUILD_001 (B).
- Verdict: residue balancing is not a reduction. Honest negative: no strictly weaker finite target arises this way. No sign certified; no negative value of 𝔞_T for ζ.
