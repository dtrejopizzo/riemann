# L2_BUILD_012 — A non-linear use of Euler product × functional equation in the window

Requirements (coordinator): non-linear in Λ; must NOT apply to a_P = Λ1_{p≥P} (Euler, no FE) nor to
Epstein/DH (FE, no Euler); not linear in window data (M_m), not a finite-zero statement (cor:void); tested on the
clamped ground mode h_T (008/009).

## Corpus check
- N_BUILD_004 §1 (reflection u ↦ 2T−u is a window property, not of Λ), §3 (Selberg symmetry formula, NO-GO ARGUED).
- N_BUILD_005 (truncated causal algebra 𝔄_T; comb = −∂_s log Z_s; Euler-structure stability NO-GO; the surviving
  object (Ω_EM): Z = M + B Euler–Maclaurin split), N_BUILD_006 (additive half bounded; sign sits in Z^{−1};
  contraction test NO-GO).
- Riemann–Siegel / AFE: R164_000, R164_190, R184_009, R168_203 (mentions as untried inputs, no window identity).
- Mertens/dlVP 3+4cosθ+cos2θ: R160_M12_R1 Prop 5.3 (output class C_zeros, void by cor:void) — not repeated.
- Rankin: R158_001, R184_004 (inertia), R186_005 (degree-2 Selberg, TB3-neg).
- Crossword §3.2 (δ) "couple the primes with the archimedean place without being D already"; I4 Thm O.
New here: (a) the reduction of candidates (i)–(iii) to one object with explicit discrimination proofs against a_P
and Epstein; (b) the explicit Volterra computation −∂_s log M_{½} = (e^{u/2} − e^{−3u/2})du; (c) NO-GO for (ii).

## 1. Candidate (ii): positive kernels |ζ|², ζ(s)ζ(1−s) — NO-GO (PROVED)
Any statement of the form "∫ |f(½+iτ)|² w(τ)dτ ≥ 0" or "f(s)f(1−s) = |f(s)|² on the line" holds for every function f
real on the real axis satisfying its own FE (Epstein E_Q), and |·|² ≥ 0 holds for every f whatsoever (in particular
ζ_{a_P}). So the positivity is satisfied by both test objects; by transfer it cannot by itself imply WP_T for ζ at
any window where those objects fail (a_P: 0.60 ≤ T ≤ ½log P, PROVED in 011; Epstein: rem:twohalves, CITED). ∎
A discriminating version must relate |ζ|² to the comb (−ζ′/ζ) — through log, i.e. Jensen/Littlewood-type
identities, which hold for every meromorphic function of finite order (no FE, no Euler): NO-GO by the same
transfer (PROVED; the identities are general complex analysis).

## 2. Candidate (iii): AFE / Riemann–Siegel as a window identity
(a) Class version (PROVED NO-GO): the AFE ζ(s) = Σ_{n≤x} n^{−s} + χ(s)Σ_{n≤y} n^{s−1} + R, 2πxy = |t|, is a consequence of
    FE + Dirichlet series and has the exact analogue for every Epstein E_Q (coefficients r_Q(n)) [CITED: standard AFE
    for Epstein/Hecke-type series]. A conclusion drawn only from "an AFE with signed remainder exists" transfers to
    E_Q, which fails (rem:twohalves). ∎
(b) Specialized version: AFE with coefficients exactly 1. Its proof is Poisson summation for ℤ (theta transform),
    which at the level of the window algebra is the Euler–Maclaurin/Poisson split of the integer comb:
      Z_s = M_s + B_s in 𝔄_T,  M_s = ½δ₀ + e^{(1−s)u}du,  B_s = Σ_{k≠0} (Poisson-dual modes) = sawtooth (N_BUILD_005 §4).
    So (iii)-specialized = candidate (i) below. (The remainder of RS is a height-t object; the window algebra sees
    the same Poisson structure at all heights at once through B.)

## 3. Candidate (i): FE on the truncated Euler side in 𝔄_T
(a) What s ↔ 1−s does in 𝔄_T (PROVED): nothing directly. 𝔄_T is a quotient of measures on [0,2T); Z_s and Z_{1−s}
    are both elements and the global FE ζ(s) = χ(s)ζ(1−s) is not an identity in 𝔄_T (it involves the tail n ≥ N
    through analytic continuation). The FE enters 𝔄_T only through Poisson summation: B_s is the Poisson-dual
    sum Σ_{k≥1} 2∫cos(2πkx)·(…)dx, whose global resummation is the FE (Riemann's second proof).
(b) The joint object (PROVED, exact in 𝔄_T; from N_BUILD_005 §1, §4):
      comb_{½} := Σ_{n<N} Λ(n)n^{−½}δ_{log n} = −∂_s log Z_s|_{½} = −∂_s log M_s|_{½} + R_B,
      R_B := −∂_s log(δ₀ + M_{½}^{−1}*B_{½}) − ∂_s-terms of B,   precisely R_B = (M+B)^{−1}*(−∂_s(M+B)) − M^{−1}*(−∂_sM).
(c) Explicit main term (PROVED, Laplace transform on [0,∞), legitimate in 𝔄_T since all objects are causal):
    𝓛M_{½}(z) = ½ + 1/(z−½) = (z+3/2)/(2(z−½)); 𝓛(−∂_sM)(z) = 𝓛(u e^{u/2})(z) = 1/(z−½)².
    So 𝓛(−∂_s log M_{½}) = 2/((z−½)(z+3/2)) = 1/(z−½) − 1/(z+3/2), i.e.
      −∂_s log M_{½} = (e^{u/2} − e^{−3u/2}) du.
    (M_{½}^{−1} = 2δ₀ − 4e^{−3u/2}du: Volterra resolvent of ½δ₀ + e^{u/2}du.)
(d) Window form in this split (PROVED on P_T, with N_BUILD_001 (A): 2∫_0^{2T}c_F e^{u/2} = −𝔭(F), and
    2∫_0^{2T}c_F e^{−3u/2}du = (1/2π)∫|F̂|²·3/(9/4+τ²)dτ since the even extension e^{−3|u|/2} has transform 3/(9/4+τ²)):
      𝔞_T(F) = (1/2π)∫ m^♭|F̂|² − 2⟨R_B, c_F⟩,  m^♭(τ) := m(τ) + 1/(¼+τ²) + 3/(9/4+τ²),
    with m^♭(0) = C₀ + 4 + 4/3 = C₀ + 16/3 = −0.0389… (C₀ = −5.37218…, lem:K).
(e) Discrimination (PROVED):
    - a_P: its comb is −∂_s log(Z_s·Π_{p<P}(δ₀ − p^{−s}δ_{log p})). The factor Z_s·Π(…) has coefficient 1 at
      P-rough n (no prime factor < P) and 0 otherwise (e.g. 0 at n = 2 for P > 2): it is not of the form
      M + (sawtooth) — its additive part differs from M by a non-oscillating measure (density of P-rough integers
      Π_{p<P}(1−1/p)·e^{u/2}), so the split (b)–(d) does not apply with the same M; with the correct density c_P e^{u/2}
      the polar step (A) gives c_P·𝔭 and m^♭ changes. The construction uses "coefficients exactly 1" (FE side). ✓
    - Epstein E_Q: comb_Q = −∂_s log Z_Q with Z_Q = Σ r_Q(n)n^{−s}δ_{log n} = M_Q + B_Q (lattice Poisson); but
      −∂_s log Z_Q has coefficients of both signs and is not supported on prime powers (no Euler product): the
      statement "R_B is the log-derivative remainder of an Euler product whose coefficients are ≥ 0 on prime powers"
      fails. The construction uses the Euler side. ✓
    - Not linear in window data: R_B is −∂_s log of a perturbation of M — a non-linear (Volterra-logarithmic)
      functional of the coefficients 1 of Z. Not a zero statement: no zeros enter. ✓
(f) Test on h_T (PROVED reduction): 𝒯₀(T) ⟺ 2⟨R_B, c_{φ₀}⟩ ≤ (1/2π)∫m^♭|φ̂₀|², and with φ₀ low-frequency
    (008 §2b) the right side is ≈ m^♭(0)‖φ₀‖² = −0.0389‖φ₀‖² + O(T^{−2}).

## 4. Review
- §1, §2(a): transfer NO-GOs, correct and elementary; the Epstein AFE is CITED (standard).
- §3(c): Laplace computation checked twice: (z+3/2)/(2(z−½)) inverted gives 2(z−½)/(z+3/2) = 2 − 4/(z+3/2) ✓;
  times 1/(z−½)² gives 2/((z−½)(z+3/2)) ✓; partial fractions with (z+3/2) − (z−½) = 2 ✓.
- §3(d) the small value m^♭(0) ≈ −0.039 is NOT intrinsic: it comes from the zero z = −3/2 of 𝓛M, i.e. from the
  ½δ₀ in the first-order Euler–Maclaurin main term. Higher-order E–M main terms move the spurious zero and change
  m^♭; correspondingly R_B changes. The split moves at most 4/3·‖F‖² from the prime side to the archimedean side;
  the total is unchanged. So (d) is an exact, choice-dependent repackaging, not slack. Downgrade: PROVED identity,
  no gain. It does show that the sawtooth remainder needs to be controlled only to the level 0.039·‖φ₀‖² in this
  normalization — but R_B is correspondingly larger by the same 4/3-term; no free lunch.
- §3(e): the a_P discrimination is that the main density differs (c_P = Π_{p<P}(1−1/p)); stated precisely enough;
  PROVED. Epstein discrimination: correct but the construction does not yet USE Euler positivity anywhere to obtain
  an inequality — it only records that the object is defined from an Euler product. The non-linear INEQUALITY that
  would use both halves is still missing.
- Overlap with the track (N): §3 is their (Ω_EM) object (N_BUILD_005/006). I add (c)–(d), (e), (f); I do not attempt
  the contraction/positivity of M^{−1}*B (N_BUILD_006 addendum: contraction NO-GO).
- No sign certified; no negative value of 𝔞_T.

## 5. Conclusion
All three candidates collapse to one object: the Volterra logarithm in 𝔄_T of the Poisson-split integer comb,
Z = M + B, whose log-derivative must equal a nonnegative prime-power comb. This is the unique place where
"coefficients exactly 1" (FE via Poisson) and "Euler product" (log with prime-power support, Λ ≥ 0) meet
non-linearly, and it passes both discrimination tests. What is missing (OPEN): an inequality, not an identity, that
uses Λ ≥ 0 on prime powers for log(M+B) and the sawtooth structure of B simultaneously. Candidate for 013: the
positivity of exp-type: Z = exp(log Z) with log Z having nonnegative coefficients ⇒ Z^{−1} = exp(−log Z) and
positivity of the "Euler cone" {exp(ν): ν ≥ 0 on prime powers} under pairing with autocorrelations c_F of P_T.
