# scripts/r156 — phase 156, item 156c (per-window converse), R156_001

All scripts are small (< 60 s each, run one at a time). Galerkin outputs are DIAGNOSTIC (variational upper
bounds on infima; float64). The two witness scripts give elementary closed-form upper bounds (PROVED-grade,
see R156_001 Thm 3.1, Thm 3.3) [amended per R156_004: "Thm 3.2" -> "Thm 3.3"; these 30-digit float evaluations are superseded as certificates of record by the two interval audit scripts below]: they bound the Levy density by K(u) <= 1/u + 1/2 against g = c_F(0)-c_F(u) >= 0,
all other terms are exact closed forms evaluated at 30 digits.

| script | what | label |
|---|---|---|
| `r156_green_matrix.py T N [--noprimes]` | Legendre-Galerkin a_T, W_T; parity bottoms; channel constants g_+ = kappa_+ + 2, g_- = kappa_- - 2 | DIAGNOSTIC |
| `r156_scan_noprimes.py N` | prime-free model (v = 0): scan in T of the two channels | DIAGNOSTIC |
| `r156_inertia_check.py` | checks n_-(W) = n_-(a|P_T) + n_-(G_T) on Galerkin matrices; cross-check of the t-witness | DIAGNOSTIC |
| `r156_lamP_model.py T N [--noprimes]` | bottoms of a on P_T, ker{A,A'}, ker{A} (relaxed class K^prim) | DIAGNOSTIC |
| `r156_theta_family.py N [theta...]` | one-contact family theta*v_2 at T = (1/2)log 3 | DIAGNOSTIC |
| `r156_odd_witness.py` | F = t at T = (1/2)log 3, prime-free: A_inf(F) <= -0.02005 (elementary bound), exact value -0.026877 | PROVED-grade bound |
| `r156_witness_threshold.py` | the same bound U(T) as a function of T; root 0.46075 | PROVED-grade bound |
| `r156_theta_witness.py` | odd quintic witness: W_theta < 0 at (1/2)log 3 for every theta < 0.8148 | PROVED-grade bound |

Validation: `r156_green_matrix.py 0.5493061443 20 --noprimes` reproduces the P47 Galerkin value
lambda^{inf,P}(1/2 log 3) ~ +0.083 (P47 after cor:Tarch), and with primes lambda_min(A_T|P_T) ~ 9.5e-4 (P47: 9.89e-4 upper bound at 120 modes).

## Audit re-verification (R156_004, hostile audit of R156_001)

Outward-rounded mpmath interval arithmetic (`iv`, 40-50 digits) with exact sympy closed forms. These are the
**certificates of record** for the two load-bearing witnesses. Each script runs in about 1 s, one at a time.

| script | what | label |
|---|---|---|
| `audit_r156_witness_t.py` | Thm 3.1: `U(0.461) in [-3.59383e-5, -3.59382e-5]`, `U(0.4608) = -7.016e-6 < 0`, `U(1/2 log 3) = -0.02005264...`; exact re-derivation of `c_F`, `g`, body integral, `s(F)`; independent Fourier-side value of `A_inf(t)` at `1/2 log 3`, `-0.026876865` (DIAGNOSTIC, float64) | PROVED (interval) |
| `audit_r156_theta_quintic.py` | Thm 3.3(ii): quintic `U0 in -0.0061377844356900...`, `Pi(F) in +0.0075328378143278...`, `-U0/Pi in 0.81480374156...`, `U0 + 0.8148 Pi = -2.82e-8 < 0`; `F = t`: `-U0/Pi = 0.47411384...` | PROVED (interval) |

Note: the bound in `r156_theta_witness.py` output, `A_inf(F) <= -0.0061378`, is rounded in the unsafe direction. The
correct statement is `<= -0.00613778`.
