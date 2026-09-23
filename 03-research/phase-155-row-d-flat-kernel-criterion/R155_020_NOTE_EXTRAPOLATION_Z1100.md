# R155_020 — Note (DIAGNOSTIC): extrapolating the finite-universe row D from Z_1000 to Z_1100 (2026-09-22)

Owner's question: "we have a pattern (D_N = Σ δ_{±γ_j}, step N → N+1 adds one atom); extrapolate it and see what
happens at Z_1100."

Protocol: predict γ_1001..γ_1100 WITHOUT reading them, from the only known law (Riemann–von Mangoldt smooth
counting N(T) = (T/2π)log(T/2πe) + 7/8, solving N(γ̃_j) = j − ½), build μ̃_1100 = μ_1000 + Σ δ_{±γ̃_j}, compare
with the true μ_1100 (Odlyzko) on probes ĥ_c(t) = e^{−(t−c)²/2s²} + e^{−(t+c)²/2s²}.

Results (script inline, 1 s):
- positions: γ̃_1001 = 1420.677 vs 1420.417; γ̃_1100 = 1534.601 vs 1535.042; error mean −0.002, rms 0.315,
  max 0.760 (mean gap 1.152 ⇒ rms 0.27 gaps, max 0.66 gaps).
- functional: relative error of W(μ̃_1100) vs W(μ_1100): s = 3 → 0.2–2 %; s = 1 → 1–15 %; s = 0.3 → −47 % … +179 %.

Reading (of record):
1. Positivity is never tested by extrapolation: any list of reals gives a positive measure (prop:finuniv).
2. What is tested is representation of the true functional: the density law extrapolates at coarse scale and fails at
   the scale of one zero. Theorem Z's certificates live at that fine scale (lobes of ŵ at distance 2–3 ≈ one gap;
   three orders of cancellation, R155_011/012), so an extrapolated zero list cannot carry a certificate.
3. The extrapolable law is the density, known since Riemann–von Mangoldt, and compatible with RH and with its
   negation (it counts zeros without locating them on the line).
Label: DIAGNOSTIC. No change to any label of record. The reverse-engineering track stays CLOSED (R155_018).
