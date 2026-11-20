# Round 23, memo D — an exact identity for the per-atom cancellation for general vectors?

Selection gate. No new derivations or computations. Object: 𝔸_M = Arch_M − Div_M − Near_M (P47 prop:AM).

## 0. What is proved and what is numerical (reading of the sources)
- **Identity (PROVED, elementary, class W7).** For exact s = m^{−½}:
  sᵀ(Div+Near)s = 2Σ_N N^{−½} log N · E_M(N), E_M(N) = Σ_{m≤M} m^{−½} c₀(log(N/m))
  (phase 190 EXP_003 §4; checked to 12 digits, M = 800). It uses Λ∗1 = log once, linearly.
- **Family s_w = m^{−½}w(m/M)** (P47 prop:shape-family, l.≈9008–9045, (i)–(iii) PROVED): collapse
  sᵀ𝔸s = sᵀArch s − Σ_{N<Me^{2T₀}} N^{−½} D_w(N) E_w(N); (iv) Ψ_w, continuous analogue of the atom n, with ∫Ψ_w = 0.
  EI_002 Thm 3(iii) (phase 192): «Div ≈ −Near» as an identity, with remainders: boundary at scale M (not estimated),
  small-divisor defects and dual Poisson terms (Thm 3(ii)).
- **Per-atom mechanism (PROVED-elementary, not specific to the weight).** For smooth s_m = S(m),
  Σ_m s_m c₀(log(kn/m)) is a Riemann sum of (kn)^{½}∫S(kn e^{−u})e^{−u}c₀(u)du, zero for S = y^{−½} by the
  Tate condition ∫c₀(u)e^{u/2}du = 0 (lem:transl(iii)). Discretization error large only if kn ≲ 1/(2T₀).
- **NUMERICAL.** That at the *minimizer* (overlap 0.993 with m^{−½}) each n ≥ 5 cancels to 3 decimals:
  δ_n = Near_n + Div_n = +0.169, +0.120, +0.027 (n = 2,3,4), +0.003 (n = 5), ≤ 0.001 afterwards; Σδ_n = 0.322 = Arch − λ
  (EXP_003 §4, M = 800, T₀ = 0.3). E_M(2,3,4) = 0.778, 0.636, 0.287; |E_M(N)| ≤ 2·10⁻⁶ on 50 ≤ N ≤ 400 (NUMERICAL;
  decay ARGUED by Euler–Maclaurin). The sign is decided by the 0.7 % correction of the minimizer relative to m^{−½}
  (EXP_003 §2–4), which is NOT in the identity.
- **L2_BUILD_030 (phase 188) §§1–3**: Near = finite-resolution remainder (Toeplitz sample of Ξ_{F₀} minus exact
  coincidences) of |P_s|²V; identities PROVED, without a sign of their own (§2).

## 1. Closest antecedent
(a) **211 ROUND_001_A §1** (Poisson on ℤ / Mellin–Euler–Maclaurin along Dirichlet polynomials): for general
s, each atom is written as continuous part + nonzero dual frequencies; NO-GO for the sign (survives cΛ,
a_P, finite modification and Beurling at first order; §3, «Result»). (b) **192 EI_002 Thm 3(ii)–(iii)**: the same
per-atom decomposition, with «Div ≈ −Near» as an identity and dual/boundary/small-divisor remainders. (c) **191 SPEC_B
T*₃/C*₃**: divisor collapse D_w(N) = 2c log N − defects; C*₃ OPEN, REF-D for η ≤ η₀ (NUMERICAL); T*₃ NUMERICAL-false
under finite modifications. (d) **193 CA_K_002 Thm 3.2(iii)** and **CA_M_001**: at prime sites Arch ≥ Near is the
statement itself (equivalent under the premise), not a mechanism. (e) **188 N_BUILD_022 §3**: NO-GO PROVED, no
identity derived from 1∗Λ = log reaches the non-divisor part (𝒟_M = Near).

## 2. Requested object, with formula
The only thing that can be written for general s is, per atom n,
  δ_n(s) := Div_n(s) + Near_n(s) = (v_n/2) Σ_{m,k≤M} s_m s_k c₀(log(kn/m))  (full sum, kn = m included),
and the exact «cancellation» requires choosing an interpolant S of s and writing δ_n(s) = (v_n/2)[𝓘_n(S) + 𝓔_n(s,S)], with
𝓘_n the integral (zero only if S ∝ y^{−½} on the support of the window) and 𝓔_n the discretization/Poisson remainder.
Then 𝔸_M(s) = Arch(s) − Σ_n δ_n(s) is tautological (sum over atoms of the definition), and the comparison «Σδ_n with
Arch in one step» is literally (S). There is no new operation: for s outside the family s_w, 𝓘_n ≠ 0 and is of full
size; the choice of S is exactly the lattice→continuum transfer of ROUND_001_A / EI_002 Thm 3.
No different object giving δ_n(s) the meaning of «defect» for general s without that step could be written.

## 3. Does it avoid the reason for failure?
No. (i) δ_n(s) is (v_n) × (quadratic form of the monoid independent of the weight): affine in the weight and signed atom by
atom → F3 and B″ (NEAR_DOSSIER §«Linearity in Λ», items C3, CA_C_002, CA_H_002, CA_K_002). (ii) The cancellation of the
n ≥ 5 is Tate + Riemann sum: it holds for every density-1 comb on smooth vectors (EXP_005 R5, class (a));
it does not distinguish Λ from any control. (iii) The part that does depend on the weight (Σ_{d|N}a(d) = log N) enters linearly once
(W7, EXP_005 R7) and only on vectors of type m^{−½}. (iv) The residue n = 2,3,4 is the contact set of the
certified windows (thm:log5A): restricting to it is (S) under another name (also L2_BUILD_031 Thm E: restricted
subspaces are equivalent to the full goal).

## 4. Connection with 𝔸_M ⪰ 0 and controls
The necessary inequality would be Σ_n δ_n(s) ≤ Arch(s) ∀s, ∀M, with precision M^{−3} (F4). There is no named step that
fails under the controls, because the controls do NOT break the per-atom identity where it lives:
- **Where the controls fail (EXP_002 §§3–4, NUMERICAL).** The negative eigenvector is a smooth packet of consecutive
  integers at the upper scale (peak ≈ 0.15–0.25 M), not m^{−½}. There Div ≈ 0 (few exact relations kn = m
  between large consecutive integers) and Near ≈ Arch + |λ|. Example pert₂(+10⁻⁵), M = 1500: Arch 120.12, Div 0.60,
  Near 119.52, λ = −7.9·10⁻⁴. By atoms (M = 800): Near_n = +41.9 (n = 2), +27.9 (3), +10.5 (4), −14.1 (5): small
  atoms, size O(M), no per-atom cancellation **not even for Λ** on that vector (the cancellation is a property of
  S ≈ y^{−½}, not of the weight). The control changes the form by ε·(Near₂ ≈ O(M)) against a margin ≍ M^{−3}: threshold
  c*(M) ≍ M^{−3} (EXP_002 §2). Deletions a₃/a₅: λ −1.5/−2.4 already at M = 50; Beurling ±0.02: −1.5 at M = 50.
- **Under each control**: (substituted weight) identity C3 breaks exactly in Σ_{n|N}a(n) − log N, but on
  m^{−½}, where the form has margin 2.58/7.26 and does not decide the sign; (deleted power) likewise, a linear term;
  (Beurling) the lattice ℤ stops being the monoid and the Riemann sum changes, again linearly. None of those
  steps is where the controls fail (upper-scale packets), so the object does not see the failure: F1 is not met.

## Verdict
**DOES NOT PASS (repetition + no mechanism).** The exact version for general s is the Poisson/Riemann decomposition
of ROUND_001_A and EI_002 Thm 3 (NO-GO), its pieces δ_n are affine in the weight and signed per atom (F3), and comparing Σδ_n
with Arch is (S) or the relabelled candidate of CA_K_002. Proved: identity C3 at s = m^{−½}, collapse on s_w, Tate+Riemann
mechanism. Numerical: cancellation to 3 decimals at the minimizer, residues at n = 2,3,4, sizes of E_M and the packet
data of the controls.
