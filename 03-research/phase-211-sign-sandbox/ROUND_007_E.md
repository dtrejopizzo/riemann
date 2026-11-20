# Round 007 E — The comb-response family E_T at T = 1.0, 1.2, 1.4 in multiprecision: dimension, capture, sharp necessary condition, sign budget

Object: E_T = N′ ⊕ P_𝒞Π(𝒩_η + 𝒯) of ROUND_005_C Definition 1 (with the corrections of REVIEW_004 §1: −σ_T
in place of |σ_T|; the two Tate responses kept, which is what makes Theorem 2(iii) exact). Target (★): λ_A(T) ≥ 0
for every T (STATEMENT_001). This memo is a NUMERICAL structure test; it proves nothing about (★). No
equivalence of (★) with any other statement is used; nothing is reduced to zeros.

Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.


Setup. Galerkin space: N = 120 Dirichlet modes per T at 40 digits (T = 1.0, 1.2) via tools/galerkin_mp.py,
P_T = complement of the two Tate directions (59 modes per parity sector, 118 total). N = 120 instead of the
requested 90 was used because each family run stayed near 5 minutes; a control run at N = 90, T = 1.0 is
reported. The gauged negative Nyquist block (ROUND_001_C gauge, constant c optimised on the mesh) has more
frequencies q than the Galerkin space resolves, so the block is TRUNCATED to q ≤ q_cap (q_cap = 120 unless
stated). Every number below is NUMERICAL.

## 1. Dimensions (NUMERICAL)

| T | gauge c | full block (#q ≥ 0) | q kept (≤ q_cap) | dim N′ (ev+odd) | dim V = P_𝒞Π responses | dim E_T | dim P_T |
|---|---|---|---|---|---|---|---|
| 1.0 (N=90) | 0.613 | 41 | 15 | 15+14 = 29 | 16+15 = 31 | 60 | 88 |
| 1.0 | 0.613 | 41 | 16 | 16+15 = 31 | 17+16 = 33 | 64 | 118 |
| 1.2 | −0.140 | 127 | 25 | 25+24 = 49 | 26+25 = 51 | 100 | 118 |
| 1.2 (q_cap=60) | −0.140 | 127 | 17 | 17+16 = 33 | 18+17 = 35 | 68 | 118 |
| 1.4 (q_cap=60, 80 digits) | −0.169 | 289 | 22 | 22+21 = 43 | 21+22 = 43 | 86 | 118 |

The full gauged block grows fast (41 → 127 → 289 frequencies), consistent with R1, but at N = 120 only a
truncation is representable; at T = 1.2 E_T already fills 100/118 of P_T. At T = 1.4 with q_cap = 120 the
family fills the whole sector (E_T = P_T, residuals 1e-100): that run is DEGENERATE and is not used.

## 2. Capture (NUMERICAL)

F* = bottom eigenvector of a_T on P_T in each parity; resid = ‖F* − Π_E F*‖; λ_E = min Rayleigh of a_T on E_T;
S_E = exact Schur complement onto E_T (reproduces λ_A to all digits by construction); C = a_T on E_T^⊥.

| T | sector | λ_1 (sector) | λ_E | resid(F*) | λ_min(C) | ‖B‖ |
|---|---|---|---|---|---|---|
| 1.0 | ev | 1.74e-23 (= λ_A) | 2.13e-17 | 1.3e-8 | 1.43 | 1.08 |
| 1.0 | odd | 9.95e-21 | 1.22e-14 | 2.3e-7 | 1.31 | 1.17 |
| 1.2 | ev | 1.26e-41 (= λ_A) | 1.83e-28 | 2.5e-10 | 2.39 | 0.98 |
| 1.2 | odd | 2.09e-38 | 5.38e-25 | 9.1e-9 | 2.47 | 1.27 |
| 1.2 (q≤60) | ev | 1.26e-41 | 8.44e-27 | 2.1e-9 | 1.19 | 1.38 |
| 1.4 (q≤60) | ev | 5.67e-65 (= λ_A) | 6.36e-34 | 3.0e-12 | 0.905 | 1.46 |

Sines of principal angles between E_T and the cluster {eigenvalues < 1e-6}:

| T | cluster (ev+odd) | sines, ev | sines, odd |
|---|---|---|---|
| 1.0 | 4+3 = 7 | 2.3e-9, 1.1e-8, 4.9e-7, 1.8e-5 | 6.1e-8, 1.9e-7, 5.6e-6 |
| 1.2 | 7+7 = 14 | 2.3e-15 … 9.1e-9, 1.8e-7, 3.6e-5 | 1.6e-13 … 1.5e-7, 2.7e-6, 1.5e-4 |
| 1.4 (q≤60) | 13+12 = 25 | 5.9e-18 … 2.9e-8, 1.7e-6, 1.8e-4, 3.1e-3, 3.7e-2 | 6.3e-18 … 3.0e-7, 4.0e-5, 9.2e-4, 2.0e-2 |

Reading. E_T contains the bottom of the cluster to 1e-8 … 1e-15 in angle, and the exact complement is
uniformly coercive (λ_min(C) ∈ [0.9, 2.5], ‖B‖ ≈ 1). But the Rayleigh bottom on E_T exceeds λ_A by 6 orders
at T = 1.0, 13 orders at 1.2, 31 orders at 1.4: capture precision (resid² ≈ 1e-16 … 1e-20) is nowhere near the
R3(i) requirement (λ_A itself). The sign is decided in the Schur coupling B C⁻¹ Bᵀ, not on E_T alone.

## 3. Necessary condition λ_min(a_T|E_T) for perturbed combs (NUMERICAL)

E(w) = family rebuilt from the perturbed comb w (its own gauged block); E(Λ) = family of Λ.

| T | comb | λ_min on E(Λ) | λ_min on E(w) | λ_A(T; w) (tool) | E(w) − λ_A(w) |
|---|---|---|---|---|---|
| 1.0 | 0.99Λ | −0.00489 | −0.00489 | −0.00489 | < 1e-3 rel |
| 1.0 | 1.01Λ | −0.0138 | −0.0138 | −0.0138 | < 1e-3 rel |
| 1.0 | 1.1Λ | −0.146 | −0.146 | −0.146 | < 1e-3 rel |
| 1.0 | a_3 | −0.535 | −0.535 | −0.535 | < 1e-3 rel |
| 1.0 | v_2+0.1 | −0.0684 | −0.0684 | −0.0684 | < 1e-3 rel |
| 1.2 | 0.99Λ | −0.0070533 | −0.0070531 | −0.0070533 | 2.6e-7 |
| 1.2 | 1.01Λ | −0.0186550 | −0.0186550 | −0.0186551 | 1.0e-7 |
| 1.2 | 1.1Λ | −0.195997 | −0.196002 | −0.196004 | 1.5e-6 |
| 1.2 | a_3 | −0.548211 | −0.548214 | −0.548214 | 2.6e-7 |
| 1.2 | v_2+0.1 | −0.0792854 | −0.0792855 | −0.0792856 | 1.7e-7 |

The condition fails (negative) for every falsifier and tracks λ_A(T; w) to 5–7 significant digits at T = 1.2
(1e-7 … 6e-6 absolute on E(Λ), 1e-7 … 1.5e-6 on E(w)). Caveat: E(w) has dimension 92–107 out of 118, so
part of this tracking is saturation of the Galerkin space, not structure; for falsifiers the negative
eigenvector is O(1)-negative and well inside any large subspace.

## 4. Dimension vs cluster vs Λ-free capture E_k (NUMERICAL)

E_k = span of the k lowest archimedean eigenvectors on P_T; "capture" = smallest k with all cosines ≥ 0.99.

| T | cluster < 1e-6 | E_k capture (cos ≥ 0.99) | ratio | cluster < 1e-3 | E_k capture | dim E_T | dim E_T / cluster |
|---|---|---|---|---|---|---|---|
| 1.0 | 7 | 17 | 2.4 | 9 | 21 | 64 | 9.1 |
| 1.2 | 14 | 34 | 2.4 | 16 | 40 | 100 | 7.1 |

The Λ-free ratio ≈ 2.4 × cluster confirms ROUND_005_E. E_T is ≈ 3× larger than the Λ-free capture space, and
in exchange captures to 1e-8 … 1e-15 instead of 0.99 in cosine.

Budget on F* (NUMERICAL, check of the splitting a = κ + σ − R): on F*, κ + σ = −R to 1e-16; κ(F*) + σ =
+0.064 (ev) / +0.232 (odd) at T = 1.0 and +0.047 / +0.215 at T = 1.2; the Tate pairing on F* is ≤ 1e-16.

## Result

PIVOT (numerical structure test, nothing proved). R1–R4 at T = 1.2:
- R1: dim E_T grows (64 → 100 → full block 41 → 127 → 289 frequencies), but at N = 120 the growth is
  truncated and E_T fills 85% of P_T; growth vs truncation is not separable at this N. OPEN.
- R2: the responses P_𝒞Π e_q are built from exact Λ; the necessary condition fails for 0.99Λ, 1.01Λ, 1.1Λ,
  a_3, v_2+0.1 and tracks λ_A(T; w) to 5–7 digits. NUMERICAL, consistent with R2 but confounded by saturation.
- R3: (i) NOT met: λ_min(a|E_T) = 1.8e-28 vs λ_A = 1.3e-41; residual 2.5e-10; the sign lives in the Schur
  coupling. Coercivity of the complement is uniform (λ_min(C) ≈ 2.4, ‖B‖ ≈ 1) — the favourable half.
- R4: comb-first family, dimension ≈ 7 × cluster ≈ 3 × the Λ-free capture dimension, far below any doubly
  exponential count. NUMERICAL.

What was proved: nothing. What failed and why: E_T is not a capture subspace at precision λ_A (13 orders
short at T = 1.2, 31 at 1.4), so R3(i) cannot be closed with E_T alone; the T = 1.4, q_cap = 120 run is
degenerate (E_T = P_T). Next concrete step: compute the Schur coupling B C⁻¹ Bᵀ on E_T at N ≥ 200 with the
block truncated at a fixed fraction of N, to separate R1 growth from saturation and to see whether the sign
of S_E is carried by a fixed number of Π-iterated responses.
