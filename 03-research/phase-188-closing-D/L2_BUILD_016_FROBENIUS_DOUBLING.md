# L2_BUILD_016 — Transport in T by Frobenius dilation n ↦ n^k: exact decomposition and why the induction fails

## Corpus check
Paper 46 lem:contA (dilations U_r with r → 1, continuity only), lem:monoT / prop:arch(i) (monotonicity in T by inclusion),
thm:wit-Tc and first-contact (witness/absorption theory), Lemma flowdet (W-det), thm:famblind (W-fam). grep "n ↦ n^k /
doubling / renormaliz / dilat kT / U_k" across the corpus: only unrelated uses (R184_010 random U_k, R154 Chebyshev U_k,
R160 survey). Paper 44 (row B) Frobenius family is about the arithmetic family, not a window map. Not a repeat: no memo
writes the window form at kT through a dilation by k with integer k.

## 1. Exact decomposition (PROVED)
U_k: L²(I_T) → L²(I_{kT}), (U_kF)(t) := k^{−1/2}F(t/k), unitary. Then (U_kF)^(τ) = k^{1/2}F̂(kτ) and c_{U_kF}(u) = c_F(u/k).
For F in the form domain:
  𝔞_{kT}(U_kF) = (1/2π)∫ m(σ/k)|F̂(σ)|²dσ − Σ_{n<e^{2kT}} v_n Re c_F((log n)/k).
Split the comb by whether n is a k-th power, n = m^k (then Λ(n) = Λ(m), log n/k = log m, m < e^{2T}):
  𝔞_{kT}(U_kF) = 𝔉_T^{(k)}(F) − 𝔖_{kT}(F),
  𝔉_T^{(k)}(F) := (1/2π)∫ m(σ/k)|F̂|² − Σ_{m<e^{2T}} 2Λ(m) m^{−k/2} Re c_F(log m)          ("Frobenius copy"),
  𝔖_{kT}(F) := Σ_{n<e^{2kT}, n not a k-th power} v_n Re c_F((log n)/k)                         ("shell + fractional lags").
Corrections to the coordinator's sketch (PROVED by the formulas): (a) the copy is NOT an exact rescaled copy of the window-T
prime form: the weights are Λ(m)m^{−k/2}, not Λ(m)m^{−1/2} (the factor n^{−1/2} = e^{−u/2} is not dilation invariant);
the copy is the comb of ζ on the line Re s = k/2 (absolutely convergent for k ≥ 3, boundary for k = 2).
(b) The archimedean part becomes m(σ/k) ≤ m(σ) (m increasing in |σ|): dilation LOWERS the archimedean symbol, by ≈ log k at
high frequency, and m(σ/k) → C₀ on the band |σ| ≲ k.
(c) "New" is not only the shell (e^{2T}, e^{2kT}): every prime p < e^{2T} reappears in 𝔖 at the fractional lag (log p)/k.
(d) Tate conditions are not transported: U_k(P_T) ⊄ P_{kT} (∫(U_kF)e^{±t/2}dt = k^{1/2}∫F(s)e^{±ks/2}ds, the Tate
moments at ±k/2, not ±½).

## 2. Mass count: the copy carries a vanishing fraction (PROVED)
Total weight of the copy: Σ_{m<e^{2T}} 2Λ(m)m^{−k/2} ≤ 2Σ_m Λ(m)m^{−1} ≤ 2(2T + O(1)) for k ≥ 2 (Mertens, CITED).
Total weight of the full comb at kT: A_{kT} = Σ_{n<e^{2kT}} 2Λ(n)n^{−½} ≍ 4e^{kT} (PNT, CITED). So the "copy" carries O(T) of
the O(e^{kT}) prime mass; 𝔖_{kT} carries all but O(T e^{−kT}) of it. A statement about 𝔖 alone ("shell statement") must
therefore control essentially the whole comb at window kT, including all old primes at fractional lags — it is (L2) at kT up
to a term of relative size O(Te^{−kT}). NO-GO for "positivity at T + shell statement ⟹ positivity at kT" as a reduction:
the shell statement is not smaller than the target. (PROVED as a mass statement; that mass dominance implies the shell
statement is as hard as the target is ARGUED — the comparison is in total variation, not in the form.)

## 3. Escape analysis (W-tail / finmod)
The shell statement uses the shell primes exactly (individual values Λ(n), n in the shell, and all old primes at lag log p/k),
so it is not killed by W-tail per se; but finmod(ii) (amplification of one old prime, e.g. n = 2, which sits in 𝔖 at lag
log 2/k) and the deletion falsifier act inside 𝔖. The induction does not separate old from new data.

## 4. Variant that survives the mass count: dilation by a real factor r close to 1 (corpus-known)
For r = 1 + ε the copy/new split is lem:contA's argument (continuity, non-explicit modulus) and L2_BUILD_001 (explicit modulus at
contact entry). These give only continuity in T, which with λ_A > 0 at T gives positivity on [T, T + δ(T)] with δ(T) of size
controlled by λ_A(T) ≲ e^{−15T} — the W-fam/thm:margin regime. No transport beyond continuity.

## 5. Review
- §1 formulas: c_{U_kF}(u) = ∫k^{−1}F(t/k)F̄((t−u)/k)dt = ∫F(s)F̄(s−u/k)ds ✓; Fourier scaling ✓; Λ(m^k) = Λ(m) ✓.
- (a)–(d) are the decisive corrections: the Frobenius map relates window T at s = ½ to window kT at s = k/2 (the "Frobenius
  family" of row B shifts the line), so an induction in T along s = ½ is not what the map provides.
- §2 is solid as mass accounting; the NO-GO is a "not a reduction" statement, not an impossibility theorem; labelled honestly.
- Could the copy at Re s = k/2 be useful in its own right? On Re s = k/2 ≥ 1 the comb is absolutely summable and the
  corresponding forms are trivially controlled (|copy| ≤ 4T + O(1)); that is exactly why it is negligible.
- No sign certified; no negative value of 𝔞_T.
Verdict: the Frobenius doubling is an exact identity but transports the wrong line (Re s = k/2), lowers the archimedean symbol,
breaks the Tate conditions, and leaves ≥ 1 − O(Te^{−kT}) of the prime mass in the "new" part. Closed as a transport mechanism.
