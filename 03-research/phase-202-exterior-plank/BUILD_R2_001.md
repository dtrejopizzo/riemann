# BUILD_R2_001 — Phase 202, round 2: audit corrections and the "𝔅_n nearly multiplicative" lead. Verdict: DIES


Read: AUDIT_202_R1_001.md, REVIEW_STATE.md. Calibrator: CALIB_001_data/ has scripts and JSON, but there is no
CALIB_R1 memo; I do not use it (no need: the verdict is structural).
Index (grep "multiplicativ", "Euler", "D_μ", "mollif", "SQ.0", "MOMENTS", "R-K1"): the lead coincides with the
D_μ/C6 channel (SQ.0, AUDIT_200_SPEC_002, MOMENTS_001/R-MOM, K1_OSG_001/R-K1). Below, the theorem explaining why
it is that channel and no other.

## 1. Corrections applied to R1 (the six)
1. **0.644** = ‖QGp‖/√ℓ(p) (DD_001, AUDIT_L_SHARP_15), the norm of the window→exterior coupling of the Schur
   plank; it is NOT the cross block. BUILD_R1 §4.2.2 is FALSE and is withdrawn. The cross block
   pro04@1×Δr_out@2 = −0.481 does carry the sign. The −0.48 is X₁₂/X₁₁ (MM_001).
2. **"X1 uses (H-a)–(H-d)"** is withdrawn: X1 contains none of those hypotheses; only the ζ objects (c_q, d_q,
   s_q). What is PROVED in §3.1 is nothing more than that the FORM of the identity changes, and each falsifier
   falls by a different hypothesis (Epstein/DH by (H-b), Beurling by (H-d), a_P by (H-a)). There is no effective
   conjunction.
3. **X1 withdrawn.** (X1.a)+(X1.b)+(X1.c) is a partition of (★★) (REF-D, like rem:ext-latno (b)); X1 ⇒ (★★) is
   trivial.
4. **A single coordinate:** from here on, the ungrouped one (pairs of dilations, X_{mn} entries from MM_001).
   The grouped one (c_q, d_q) remains only as a registered identity; R1's §2.4 and §4.3 are not combined.
5. **R_n convention** = entries of the full 𝒲 form (MM_001 l.42: 𝒲_ext = Σ(mn)^{−½}X_{mn}); the μ(m)/m are
   already inside r; the sign μ(n) appears only once. The comb part of the resonance (−log n·μ(n)·(+)) helps
   for prime n; **the damaging sign comes from the archimedean part Σ_n μ(n)n^{−½}𝔅_n.**
6. **Killing term per layer:** on the half line, 𝔅_q(Y) uses κ_Y(y) = ∫_{y−Y}^∞ ½K with cutoff Y = T + log(ak),
   not T.
Diagonal q = 1 "locally positive": ARGUED and not usable (archimedean block not PSD, m(0) = C₀ < 0; J.4).
Withdrawn as an input.

## 2. The lead: is 𝔅_n(T+log n) nearly multiplicative in n, with the Möbius sum = a signed Euler product?

### 2.1 Exact writing of the term (PROVED, apart from cutoffs)
Without the layer cutoffs, 𝔅_n = 𝒜(r̃, τ_{log n} r̃) = (1/2π)∫ m(τ)|r̂̃(τ)|² n^{iτ} dτ (m(D) is a multiplier;
τ_{log n} is the modulation n^{iτ}). Then, exactly,

  Σ_{n<N} μ(n) n^{−½} 𝔅_n = (1/2π)∫ m(τ) |r̂̃(τ)|² · D_N(½ − iτ) dτ,   D_N(s) := Σ_{n<N} μ(n) n^{−s}.          (2.1)

The cutoffs y = T + log n add boundary terms (κ_Y) and do not change the kernel n^{iτ}.

### 2.2 Lemma M (PROVED): the only possible multiplicativity is a character
Let Φ: ℚ_{>0} → ℂ, Φ(q) := 𝔅(r̃, τ_{log q}r̃)/𝔅(r̃, r̃) (or any function of the form φ(log q) with φ continuous and
bounded on ℝ, which is the case for every translation-invariant form applied to r̃ ∈ L² with r̃^ of finite mass
against m). If Φ is completely multiplicative on ℚ_{>0} (equivalently φ(x+y) = φ(x)φ(y) on log ℚ_{>0}), then
φ(x) = e^{iτ₀x} for some real τ₀, or φ ≡ 0.
*Proof.* log ℚ_{>0} is dense in ℝ; by continuity φ(x+y) = φ(x)φ(y) ∀x,y ∈ ℝ; the continuous solutions are e^{cx};
bounded ⇒ c = iτ₀. ∎
If multiplicativity is only required on coprimes, the same argument on the generated group gives
Φ(p^k) = Φ(p)^k-compatible with continuity only if Φ(p) = p^{iτ₀} (the log p are Q-linearly independent, but
continuity on a dense set forces the character on the generated subgroup; ARGUED in the coprime version, PROVED
in the complete one).
But φ(x) = (1/2π)∫m|r̂̃|²e^{iτx}dτ is the Fourier transform of an absolutely continuous measure (r̃ ∈ L²): by
Riemann–Lebesgue φ(x) → 0, and φ = e^{iτ₀x} is impossible except φ ≡ 0. **Hence 𝔅_n is never multiplicative in
n.** (PROVED.)

### 2.3 "Multiplicative plus error": what remains is D_N, i.e. C6
Any writing 𝔅_n = Φ(n)𝔅₁ + E_n with Φ multiplicative has, by 2.2, Φ(n) = n^{iτ₀} (or a mixture, which ceases to
be multiplicative). Then Σμ(n)n^{−½}Φ(n) = D_N(½ − iτ₀): the Möbius series truncated on the line ½, whose
"Euler product" Π_p(1 − p^{−½+iτ₀}) does not converge (Σp^{−½} diverges) and whose continuation is
1/ζ(½ − iτ₀) — the mollifier D_μ. The error E_n, summed with μ(n)n^{−½}, is (2.1) minus that term: again
∫m|r̂̃|²D_N. **There is no Euler product with a well-defined sign: the Möbius sum at abscissa ½ is not
absolutely convergent and its only multiplicative object is 1/ζ.** This is exactly the closed channel:
SQ.0/AUDIT_200_SPEC_002 (mollified exterior = −g mod radical), MOMENTS_001 (∫|ĝ|²(|D_μ|² − 1)σ = 0 on the core,
R-MOM), K1_OSG_001 (R-K1, Möbius correlation). **The lead is C6 in disguise. NO-GO PROVED** (2.1 + Lemma M),
except for the boundary terms from the layer cutoffs, which are layer pairings with no multiplicativity at all
(n enters as the cutoff T + log n, not as a character).

### 2.4 Does exterior Poisson relate 𝔅 across different layers?
Poisson (thm:ext-half) relates Zr to f over the window, not layer T+log n to layer T: layer T+log n is the
dilation of layer T, but the dilation is the translation τ_{log n}, which in Mellin terms is the modulation
n^{iτ}, already included in (2.1). Poisson converts Σ_n r(nw) into Σ_k f(k/w)/w; applied to (2.1) it gives back
W_T(Ef) (thm:ext-half), not a relation between layers weighted by μ. ARGUED: Poisson adds no information to
(2.1). The conjunction (H-b)∧(H-d) enters no inequality: (H-b) only produces D_N (= C6), (H-d) only produces the
half-line identity.

## 3. Any inequality with (H-b)∧(H-d) inside? Direct search, negative
Candidates reviewed and why they die:
- Inequality on (2.1) via the size of D_N on the line ½: uses |D_N| — norms (criterion (b)) or moments of 1/ζ
  (MOMENTS_001).
- Sign of Σ_p over primes after Euler: requires absolute convergence at ½ — false.
- Layer cutoffs: boundary terms κ_{T+log n}; no multiplicative structure (they depend on log n additively); any
  bound would be a size bound, generic-comb (rem:ext-latno (c)).
- Restriction to the lattice span with v = μ: positivity of G = stronger than (★★) (rem:ext-latno (b)).
None produces an inequality with the conjunction used as a hypothesis.

## 4. Verdict
Death criterion (a) (triggered after R1): round 2 produces no inequality, no non-identity, using (H-b)∧(H-d) in
the proof without passing through D_N, norms, or the minimizer. The only concrete path (the audit's lead) is C6
via Lemma M. **Phase 202 DIES in round 2.** What remains PROVED: Lemma M (non-multiplicativity of 𝔅_n; the only
compatible multiplicativity is a character ⇒ 1/ζ) as a class NO-GO: "every Möbius sum of archimedean pairings
of tail dilates is ∫m|r̂̃|²D_N(½−iτ)".
No sign is claimed. L′♯ OPEN. (★★) OPEN. Row D OPEN.
</content>
