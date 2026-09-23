# R155_021 — Note (DIAGNOSTIC + one PROVED reading): what the row D of Z_1000 and of Z_100000 have in common (2026-09-22)

Owner's question: build D for Z_100000 as for Z_1000 and compare; then "generalise D to all Z".

D for Z_N is μ_N = Σ_{j≤N} δ_{±γ_j} (Paper 47 prop:finuniv). Comparing lists says nothing; comparing their Fourier
transforms g_N(u) = Σ_{j≤N} cos(γ_j u) w(γ_j/Γ_N) (Gaussian cutoff) does. Script `scripts/reverse/dinf/spikes.py` (5 s).

**Observation.** g_N has spikes exactly at u = log n for prime powers n, of area −v_n/4 = −Λ(n)/(2√n):
- Z_1000 (Γ = 1419): n = 2,3,4,5,7,9,11,13,19,31,41 resolved to 1–4 %; n = 8,16,17,23,25,27,29,37 unresolved
  (resolution 1/Γ vs neighbouring spikes and cutoff ringing);
- Z_100000 (Γ = 74921): every n ≤ 41 to 0.1 %; controls at non-prime-power u give 0 to 1e−5.
So what the two D share is the prime comb with the von Mangoldt weights, at precision growing with N.

**Why (PROVED, it is the explicit formula, row C).** With h = φ_Γ(·−u) + φ_Γ(·+u), ĥ(t) = 2cos(tu)w(t/Γ), the
explicit formula Σ_ρ ĥ(γ_ρ) = 2∫h cosh(u/2) − Σ_n v_n h(log n) + (1/2π)∫mĥ gives, near u = log n, a spike of area
−v_n in Σ_{±γ} 2cos(γu)w, i.e. −v_n/4 in Σ_{γ>0} cos(γu)w. Independent of Γ. This is the theorem Riemann had in
1859 and is the reason a few zeros already "know" the primes.

**Generalisation to all Z (the owner's question), stated precisely.**
1. The limit of μ_N as N → ∞ exists as a tempered distribution (density N(T) ~ (T/2π)log T); its Fourier transform
   is, by the explicit formula, the prime comb −Σ_n v_n δ_{±log n} plus the smooth Γ/cosh part. So "D for all Z"
   IS the prime side: it is determined by the primes alone, with no reference to zeros. This is row C.
2. RH ⟺ that tempered distribution is the Fourier transform of a POSITIVE measure (Bochner/Weil). For finite Z the
   positivity is automatic (prop:finuniv); for ζ it is the whole content. That is row D = Problem B of Paper 47.
3. The spike pattern does not discriminate RH: a zero ½+δ+iγ contributes cos(γu)cosh(δu) instead of cos(γu); at
   u ≤ 4 the change is < e^{4δ} − 1, invisible at this precision. What would discriminate is a negative part of
   the spectral measure, which no finite real list can exhibit (thm:finZ, prop:finuniv).

Label: the observation is DIAGNOSTIC (zero table); the explanation is PROVED (explicit formula); no label of record
changes; no sign for ζ claimed. The reverse-engineering track remains CLOSED (R155_018).
