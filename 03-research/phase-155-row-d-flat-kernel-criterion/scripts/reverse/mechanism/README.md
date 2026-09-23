# scripts/reverse/mechanism — owner's questions 2026-09-22 (DIAGNOSTIC)
- `lzeros.py q k` — first k zeros of L(s,(·/q)) for a prime q ≡ 1 mod 4 via the smoothed approximate functional
  equation with complex incomplete gamma (validated against mpmath.dirichlet at q=101 to 12 digits).
  q=101: 5 s. q=100000000057 (12 digits): 944 070 terms per evaluation, ~1–2 s each, ~30–40 min for 10 zeros.
- `weil.py` — prime-side Weil functional W(F)=pole+gamma+prime for real F∈C_c^∞(−U,U), phase-118 normalisation;
  cross-checked against 2Σ_{γ≤1419}|F̂(γ)|² to 6 digits (100000-zero column in the __main__ output is aliased: ignore).
- `why.py` / `why.out` — 12 random F per support U: min W, mean pole/gamma, prime range, cancellation ratio.
- GUE spacing check and the off-line quadruple counterexample are inline in R155_022.
