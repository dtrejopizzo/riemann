# R155_029 — Lead closing decision, round 3 (3a/3b/3c) (2026-09-22)

Inputs: R155_023/025 (archimedean thresholds), R155_024/027 (two-prime enclosures, Theorem 3.3ᴾ), R155_026/028 (Schur
reduction at log 2, hardened enclosure r3c_04). Notes R155_020–022 (owner's questions; DIAGNOSTIC). Rules applied as in
R155_010/018.

## 1. Labels of record
| statement | label |
|---|---|
| Two archimedean thresholds: λ^∞_min, λ^{∞,P}_min non-increasing; λ^∞ ≤ λ^{∞,P} ≤ C₀ + φ((3π/2T)²) (thm:SC, A = 0); negative for T ≥ 0.74921; → C₀; ≥ 0 for 2T < log 2 (cited); thresholds exist in [½log2, 0.749] | PROVED (structure) |
| T*_∞ ≤ 0.3716 (L²), T*_{∞,P} ≤ 0.5958 (P_T) — Galerkin upper bounds on infima | DIAGNOSTIC |
| ½log3 < T*_{∞,P}: archimedean form on P_T positive alone (≈ 0.083), primes a cost; log 2 > T*_{∞,P}: deficit η_P ≈ 0.154, prime form on the ground state ≈ 0.188 — primes necessary | DIAGNOSTIC (reading), ‖Π_T‖ ≤ A_T PROVED |
| Theorem N′: no lattice certificate of order M ≤ 24 has non-negative value at T = 0.68 or log 2, β-uniform, any range/atoms/tail lemma (32 enclosures, all reproduced by the audit; every M ≤ 24 covered via 20/24) | PROVED (machine-verified) |
| Theorem 3.3ᴾ / P1 / P2 / Cor Aᴾ / Cor Cᴾ (concentration radius R = 2πexp(1 + C₀ + (λ^P+ε+B)/η); verified-on-[−R,R] bound; no uniform rate; O(K(log M)^{−δ}) on a sub-family) with the (E_R + C₀)⁺ hypothesis | PROVED |
| Remark P3 in corrected form (exponential in 1/η forced by V′(ii); constant open) | PROVED |
| Prop 3c.1 / Cor 3c.2 (Schur reduction; congruence; ⟹ unconditional, coercive converse needs β bounded); parity splitting S = S_even ⊕ W|V_odd | PROVED (re-application of the corpus's Feshbach/parity technique with a new prime-independent pivot) |
| Theorem 3c.3 (hardened): W_{log2}[F*] ∈ [0.0342113430, 0.0342182500] for the archived direction F*, interval arithmetic, no float budget | PROVED (machine-verified). One direction at log 2, NOT a sign for the form. |
| w₁₁ at four windows; crude condition fails by 1.07–1.49; S ground state 99.46 % on the third archimedean eigenvector; even-sector ideal condition fails by 0.064–0.310 | DIAGNOSTIC |
| w₁₁ is far above every Galerkin upper bound on λ_min(W_T\|P_T); no value of inf W_{log2}\|P_T is supported [amended 2026-09-22 per R155_036] | DIAGNOSTIC |
| (H1) n₋(A_∞|P_T) = 1 on (T*_{∞,P}, 0.80] | HYPOTHESIS (computed, not proved); Landau–Widom growth HEURISTIC |

Row-D label unchanged. Endpoint of record unchanged: λ_min(A_{½log3}) ≥ 8.8577e−5. No sign for ζ beyond log 2.

## 2. What round 3 changed in the map
1. The two-prime windows are now provably out of reach of every lattice class up to order 24 (N′), the class that
   carries the endpoint at ½log3. The wall is a theorem, not an optimiser failure.
2. The role of the primes flips at T*_{∞,P} ≈ 0.596 (upper bound): below it (Theorem C) the certificate pays for the
   primes; above it (log 2) the primes must create positivity in the archimedean ground-state direction. Any
   construction of D at log 2 must USE the prime atoms, which is why comb-vanishing (R155_016) failed structurally.
3. Positivity at log 2 splits into one cheap direction, now PROVED (w₁₁ > 0), and the Schur complement on V, where
   the obstruction is an even-sector cancellation with no margin. Every class impossibility proved so far obstructs
   only the second part.
4. Problem A (a class-dependent LOWER bound) remains untouched: rounds 1–3 are entirely upper-bound-side.

## 3. Round 4 orders (pure math)
(a) Even-sector Schur complement at log 2: characterise S_even's ground state analytically (third archimedean
    eigenvector + prime correction); attempt a rigorous enclosure of λ_min(S_even) on a finite-dimensional
    Galerkin subspace — a lower bound on the form's minimum over that subspace is NOT what we need; what is needed
    is a certificate on V, i.e. Problem A on the even sector.
(b) Prove or refute (H1) n₋(A_∞|P_T) = 1 on (T*_{∞,P}, T₂) with explicit T₂ (min–max with the m < 0 band |τ| < τ₀ = 6.2898).
(c) Problem A lower bound: first attempt on the archimedean form alone (A_∞|P_T restricted to a lattice class) where
    the operator is explicit and no primes intervene — if even there no class-dependent lower bound is provable,
    record it as a structural negative.
(d) Rigorous enclosure of T*_{∞,P} to 3 digits (interval Galerkin with a certified lower bound on the infimum —
    the direction the Galerkin cannot give; needs a Temple/Kato-type bound).
