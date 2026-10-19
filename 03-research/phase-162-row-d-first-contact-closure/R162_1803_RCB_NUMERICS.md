# R162_1803 — numerics for R-C.b: (N2), (C2), sign of ⟨u₂,φ⟩ on {μ₂^ev = 0}

Status: **UNCERTIFIED float** (double precision, Legendre–Galerkin, base `scripts/c3/t1601_nodal_rerun.py` with the fixed
tail sign of R162_1590/R162_1601). This file has no proof status.
Scripts: `scripts/c3/t1803_rcb_numerics.py` (scan and μ₂-crossing), `scripts/c3/t1803_conv.py` (K-convergence of the
(C2) defect), `scripts/c3/t1803_contact.py` (addendum from R162_1801: μ₂^ev at T_*(s), and the (R2′) test).

Conventions:
- A = A_T is the matrix of the Weil form on L²(−T,T), with comb weights s·2Λ(n)/√n.
- ψ_T is the ground state of A^ev, and u₂ is the second even eigenvector. Both are normalised to be > 0 at t = 0⁺.
- φ = cosh(t/2), and φ̂ = φ/‖φ‖.
- Odd sector: ψ₁^odd and u₂^odd are the first two odd eigenvectors; the odd analogue of (C2) is ψ₁^odd/sinh(t/2).
- The deletion model a = Λ·1_{n≥5} equals the archimedean operator Γ_T for T < ½log 5. So on [0.3,0.6] it is a test of
  Γ_T.

## 1. (C2): is ψ_T/cosh(t/2) monotone?

Robust measure: CV = counter-trend total variation of r = ψ/cosh on (0,T], divided by ptp(r). CV = 0 means r is monotone.
CV_in is the same quantity on (0, 0.9T). Δ_K is sup|r_K − r_{K_prev}|/ptp(r). The grid has N = 8001 points.

| model | s | T | K=26 | K=34 | K=46 | K=60 | K=76 (CV_in) | Δ_K range |
|---|---|---|---|---|---|---|---|---|
| Γ_T | 0 | 0.45 | 0 | 0 | 0 | 0 | 2.8e-4 (0) | 2–5e-2 |
| Γ_T | 0 | 0.8047 | 0 | 0 | 0 | 0 | 0 (0) | 2e-2 |
| ζ | 1 | 0.30 | 0 | 0 | 0 | 0 | 5.6e-2 (4e-4) | 2–9e-2 |
| ζ | 1 | 0.34 | 0 | 0 | 0 | 0 | 2.7e-2 (9e-5) | 2–7e-2 |
| ζ | 1 | 0.36 | 0 | 1.6e-2 | 2.4e-2 | 3.1e-2 | 5.5e-2 (3e-4) | 2–9e-2 |
| ζ | 1 | 0.38 | 3.9e-2 | 5.6e-2 | 6.8e-2 | 7.3e-2 | 9.4e-2 (7.4e-2) | 2–10e-2 |
| ζ | 1 | 0.45 | 0.166 | 0.163 | 0.159 | 0.154 | 0.146 (0.145) | 2–8e-2 |
| ζ | 1 | 0.5523 | 0.252 | 0.245 | 0.232 | 0.238 | 0.233 (0.211) | 2–7e-2 |
| ζ | 1 | ½log5 | 0.325 | 0.337 | 0.373 | 0.343 | 0.347 (0.347) | 2–7e-2 |

Reading of the table:
- Sanity check: for Γ_T, r is monotone at every K, which agrees with Prop. 4 of R162_1701 (Almgren–Lieb). The small
  values at K = 76 are endpoint Gibbs effects, and they vanish on (0, 0.9T).
- For ζ, the defect is 0 up to T ≈ 0.36, i.e. up to about ½log 2 = 0.347, where the prime 2 enters the comb.
- From T ≈ 0.38 on, CV is 15–35 % of the range. It is stable in K from 26 to 76, it sits in the interior, and it is
  larger than the K-discretisation error Δ_K.
- At T = 0.45, r has a bump with turning points at t ≈ 0.21 and 0.28 at both K = 34 and K = 46. The finer turning
  points are not K-stable, but the bump itself is.
- The step-fraction diagnostic in the scan tables (§4) agrees: 0.12–0.43 of grid steps go against the trend for
  T ≥ 0.39, and the per-step maximal violation scales like 1/N. So r is a smooth non-monotone function, not noise.

**Verdict (C2): looks FALSE for ζ (and for s = 0.5, 1.5, 2) once T > ½log 2.** It is true for Γ_T, which covers deletion on
[0.3, 0.6].

## 2. (N2): sign changes of u₂ on (0,T) (K = 46, N = 4001; K = 34 agrees in every row)

S2 is the number of sign changes of u₂ on (0,T).

| T | ζ (s=1) | s=0.5 | s=1.5 | s=2 | deletion (T∈[0.3,0.6]) |
|---|---|---|---|---|---|
| 0.30–0.52 | 1 | 1 | 1 | 1 | 1 at all 7 points |
| 0.52–0.60 | 1 | 1 | 1 (0.516), 2 (0.588) | 2 | 1 |
| 0.66 | 1 | 1 | 2 | 3 | — |
| 0.73 | 1 | 1 | 4 | 4 | — |
| ½log5 | 1 | 1 | 5 | 5 | — |

- In the rows where S2 > 1, μ₂^ev is already negative (−0.16 to −0.97). There u₂ is no longer the eigenvector in
  question, because the contact has passed.
- **At every μ₂^ev = 0 crossing, S2 = 1** (see §3).
- For ζ, μ₂^ev stays > 0 but becomes tiny (8e-4 at 0.55, 4e-12 at ½log5). This is the Connes-type near-kernel, and in
  that range u₂ is ill-conditioned. Even so, S2 = 1 is stable there.

**Verdict (N2): looks TRUE wherever it is needed** (for ζ on the whole range, and at every crossing). It fails only past the
contact, for strong amplification.

## 3. μ₂^ev = 0 crossings, primitive contacts T_*, and ⟨u₂, φ̂⟩

Crossing of μ₂^ev (brentq in T; the two K values are shown as K=34 / K=46):

| model | T(μ₂=0) K=34 / K=46 | S2 | ⟨u₂, φ̂⟩ at the crossing |
|---|---|---|---|
| s=0.5 | 0.626697 / 0.626629 | 1 | **−0.0623** |
| s=1 (ζ) | none in [0.3, ½log5]; μ₂ decreases to 4e-12 | — | ≈ −1e-5 → 0 (tracks μ₂) |
| s=1.5 | 0.426042 / 0.425969 | 1 | **+0.0163** |
| s=2 | 0.396106 / 0.396023 | 1 | **+0.0221** |
| deletion | 0.619008 / 0.619004 | 1 | **−0.1371** |

Addendum (R162_1801). T_* is the first zero of λ_ev = bottom of A^ev on φ^⊥. The table gives μ₂^ev(T_*) and the
(R2′) zero sets on (0,T):

| model | T_* (K=46) | μ₁^ev | μ₂^ev(T_*) | zero of u₂ | zeros of ψ − cφ | ⟨u₂, φ̂⟩ |
|---|---|---|---|---|---|---|
| s=0.5 | 0.617680 | −2.230 | **+9.05e-3** | 0.2457 | 0.3823 | −0.0625 |
| s=1 | no contact in [0.3, ½log5]; min λ_ev = 3.7e-12 | | | | | |
| s=1.5 | 0.425807 | −1.754 | **+4.61e-4** | 0.2304 | 0.0816, 0.2639, 0.3789 | +0.0161 |
| s=2 | 0.395903 | −1.635 | **+7.85e-4** | 0.2315 | 0.1184, 0.2962, 0.3757 | +0.0218 |
| s=3 | 0.370782 | −1.512 | **+9.51e-4** | 0.2309 | 0.1456, 0.3215, 0.3666 | +0.0248 |
| deletion | 0.595817 (K=34: 0.595820; R162_1801: 0.595818) | −1.937 | **+3.84e-2** | 0.2492 | 0.3630 | −0.1366 |

- All values are K-stable to about 1e-4 or better.
- **μ₂^ev(T_*) > 0 in every model**, so none of them is a weight-blind counterexample to R-C.b. For s ≥ 1.5 the margin
  is small (5e-4 to 1e-3), because T_* lies just before the μ₂ crossing (for s=1.5, 0.42581 against 0.42597).
- **(R2′) fails**: the zeros do not coincide. u₂ changes sign at about 0.23–0.25. For s ≤ 0.5 and for deletion, ψ − cφ
  has a single zero, but at about 0.36–0.38. For s ≥ 1.5, ψ − cφ has 3 zeros.

**Verdict O1701.3: the sign of ⟨u₂, φ⟩ on {μ₂^ev = 0} is NOT constant across the family.**
- It is negative for s = 0.5 and for deletion (Γ_T), and positive for s = 1.5 and s = 2.
- By continuity in s, it vanishes at some s ∈ (0.5, 1.5), which is a codimension-two event {μ₂ = 0, ⟨u₂, φ⟩ = 0}.
- This agrees with §1: (C2) fails with the comb, while (N2) holds at the crossings. So Theorem 3's hypothesis set is
  broken through (C2), not (N2).
- Consequently R-C.b cannot be weight-blind in the form (C2)+(N2). For ζ (s = 1), ⟨u₂, φ⟩ and μ₂ go to 0 together.
  This is the Perron–Tate alignment of Prop. 5, not a crossing.

## 4. Odd sector (K = 46; K = 34 agrees)

| model | ψ₁^odd > 0 on (0,T)? | ψ₁^odd/sinh monotone? | S(u₂^odd) |
|---|---|---|---|
| Γ_T / deletion, T ≤ 0.6 | yes | 94–97 % of steps; violations O(1e-5) at the endpoint (Gibbs) | 1 |
| ζ, T ≤ 0.48 | yes | yes, with endpoint noise only | 1–3 |
| ζ, T ≥ 0.53 | **no (1 sign change)** | no (27–39 % of steps) | 0–3, unstable |
| s = 1.5, 2, T ≥ 0.44 | no (1–4 sign changes) | no | 1–3 |

- For ζ with T ≥ 0.53, the odd μ₁ and μ₂ are 1e-2 down to 1e-10. The odd spectrum is then nearly degenerate, so the odd
  eigenvectors are poorly determined. S1 = 1 is K-stable, but S(u₂^odd) is not.
- Verdict: (P-odd) and (C2-odd) look false with the comb for T ≳ 0.5, and true for Γ_T.

## 5. Verdict

- **(C2): looks false once the comb is present** (T > ½log 2), with a K-stable interior defect of 15–35 %. It is true for
  Γ_T.
- **(N2): looks true** for ζ and at every μ₂ = 0 crossing.
- **O1701.3: the sign flips between s = 0.5/deletion (−) and s = 1.5, 2 (+).**
- μ₂^ev(T_*) > 0 at every primitive contact tested: s = 0.5, 1.5, 2, 3 and deletion.
- Theorem 3 of R162_1701 therefore cannot be applied weight-blindly. The route has to replace (C2), for example by an
  arithmetic statement on (0,T) valid near T_*, or be dropped.
