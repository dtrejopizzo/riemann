# PROOF_L_SHARP_K_001 — Strategy K: J.3's exact evaluation inside the Paley–Wiener regime, at the prolate vector

Phase 199, prover memo (pen and paper; NUMÉRICO only to check). Target: Lemma L′♯ / (★★) (AUDIT_L_SHARP_2 §7).
No previous partial K memo existed.

**Outcome in one line.** The requested law "W_T(Eψ₀) = κ₀μ^a(1−λ₀(2πμ))(1+o(1))" is **mis-posed**, and we give the exact
obstruction. (K.1) ψ₀ cannot be made admissible by a small modification. The constraint f̂(0) = 0 forces a correction
of relative size O(1) along ψ₂, so the admissible prolate vector has defect scale 1−λ₂ ≍ c²(1−λ₀), not 1−λ₀ (PROVED
modulo the CITED Hermite limit). (K.2) The out-of-band tail has an explicit Langer/Bessel form (CITED + derived).
(K.3) Inside the PW regime, J.3's step (Poisson in the dilate index) has no small remainder. The dual terms k ≤ μ
resonate, and the Poisson dual of Zr is the window vector itself, so the method returns W_T(g) (PROVED identity;
circular, NO-GO for this technique). (K.4) The data are consistent only with a defect at index 4: Mori's
certified margin is 1.89·(1−λ₄) at μ = 15. In units of 1−λ₀ this is a = 4, κ₀ ≈ 5.0·10⁵ (NUMÉRICO). No sign. (★★) OPEN.

## 0. Corpus check and why this is not a retry
Read: AUDIT_L_SHARP_2 (constraints 1–11; constraint 9 says J.3 lies outside PW), J_001 (Thm J.3, §4.1), A_001 (Thm 1.1, Thm 3.1,
§3.2), PATTERN_001 §2–§3 (κ-band with λ₄, Fuchs), index README l.449–458. New relative to the index: J.3 had never been
attempted on PW data. The attempt here uses an *extremal* vector instead of a deep bump. It ends in an obstruction,
so nothing in the index is retried as a sign source.

## 1. (i) Admissible repair of ψ₀ (K.1)
Notation of A §1: λ = √μ, c = 2πμ (time·band of [−λ,λ] × [−λ,λ]), ψ_n the prolates of [−λ,λ], ∫_{−λ}^{λ}ψ_n² = 1,
λ_n = λ_n(c).

**Lemma K.1a (free constraints; PROVED).** g = Ef|_I depends only on f|_{|x|>1/λ}. For u ∈ (1/λ,λ) and n ≥ 1 we have
nu > 1/λ. Hence f(0) = 0 can be imposed by adding a zero-mass C_c^∞ bump supported in (−1/λ,1/λ), and this changes neither g nor f̂(0).
The condition f(λ) = 0 costs |ψ₀(λ)| = O(c^{3/4}e^{−c}). It is imposed by a C² edge cutoff on a layer of width 1/c. The change in g and in the
tail is O(e^{−c}·poly(c)) in amplitude, which is relatively negligible against the scale of 1−λ₀ only in the L²-amplitude sense. This is ARGUED for the form, because Z is not L²-bounded (C Prop 4.2).

**Proposition K.1b (f̂(0) = 0 is not small; PROVED given the CITED Hermite limit).** ψ̂_n = i^{n}·(scaled)√λ_n·ψ_n
(Slepian–Pollak 1961, CITED), and as c → ∞, ψ_n(x) = (c^{1/2}/λ)^{1/2}h_n(√c·x/λ)(1+O(1/c)) near 0 (Slepian 1965,
CITED), with h_0(0) = π^{−1/4} and h_2(0) = −π^{−1/4}/√2. Hence ψ̂₀(0) ≠ 0 at relative size O(1). Within span{ψ_{2k}}, the
minimal-leak admissible vector with leading coefficient 1 on ψ₀ is f = ψ₀ + αψ₂ + O(c^{−1}), with α = −ψ̂₀(0)/ψ̂₂(0) =
−√2(1+O(1/c)). Its leak is
  leak(f)/‖f‖² ≈ [(1−λ₀) + 2(1−λ₂)]/3 ≈ (2/3)(1−λ₂) ≈ (64/3)c²(1−λ₀)
by Fuchs (1964, CITED): 1−λ_n(c) ≈ 4√π·8ⁿ/n!·c^{n+½}e^{−2c}. Minimisation: the weights 1−λ_{2k} increase by a factor ≍ c² per step, so the
optimum loads ψ₂ first. **Consequence:** "Eψ₀ corrected by a small admissible modification" does not exist. Every
admissible prolate-built vector has defect at least ≍ 1−λ₂. A law with 1−λ₀ is mis-posed.

## 2. (K.2) The tail r = ψ̂₀|_{(λ,∞)}
ψ₀ extends to an entire function, and ∫_{−1}^{1}e^{icxω}ψ₀(x)dx = μ₀ψ₀(ω) holds for all ω (CITED, Slepian–Pollak). So the tail *is*
ψ₀ continued beyond the band edge (normalised variable ω = ξ/λ > 1). For ω > 1 the prolate ODE has a regular singular point at
ω = 1. The local solution is J₀(c√(2(ω−1))), and the Langer/WKB form (Dunster 1986, CITED, uniform in ω ≥ 1 + c^{−2}) is
  ψ₀(ω) = C_c (ω²(ω²−1))^{−1/4} cos(c√(ω²−1) − π/4)(1 + O(1/c)),  C_c² = 2(1−λ₀)/π,
where C_c is fixed by ∫_{|ω|>1}ψ₀² = (1−λ₀)/λ₀ (ARGUED: normalisation derived, phase/amplitude CITED). In ξ the tail
oscillates with local frequency 2πλ·ξ/√(ξ²−λ²). This is the aliasing scale 1/λ of J §4.1, and it has no smooth deep component.

## 3. (K.3) J.3's technique in the PW regime: the obstruction
J.3 applies Poisson summation in m to F_x(m) = m^{−1/2}r̃(x+log m). For smooth data the dual terms ĝ(kL), k ≠ 0, are
superpolynomially small, and the quasi-mode B e^{−x/2} carries everything. **Proposition K.3 (PROVED).** For r = tail of an f ∈ PW
with supp f ⊂ [−λ,λ], Poisson summation in n of Σ_n r(nu) gives exactly u^{−1}Σ_k f(k/u) restricted to the
out-of-band part (Guo (4.6), CITED). For u > λ the dual frequencies k/u with 1 ≤ k < λu lie inside supp f. So the
dual terms are O(1), not small. They are the window samples, and the identity is A Thm 1.1 read backwards
(Ψ_f = Zr_f). In particular:
- the J.3 quasi-mode B = ∫_λ^∞r has |B| ≲ C_c/c (it is the integral of the oscillating tail, by K.2 and one integration by parts);
- the "remainder" Ψ_1 is the whole object.
J.3's four-piece anatomy (Γ_ℝ, Lévy energy of e^{−x/2}, residue-1 cancellation, Mertens 2γ) therefore enters at relative order
O(c^{−2}), multiplied by 0.046. It is **not** the leading term at the extremal vector. The leading term is the window
form itself, so the method is circular. NO-GO for "J.3 technique as the evaluator in PW" (PROVED for this
technique, not as a class).

**ARGUED heuristic (not used).** A local-symbol reading with Θ_∞(τ) = log(τ/2π) + O(τ^{−2}) (exact, from the functional equation),
dilate n at Mellin frequency τ = 2πλnu, and prime weight log n gives a local symbol log(λu/n). It is negative for dilates n > μ.
Near-coincidences m ≈ kn decide the rest. This is constraint 5/8 again, and no evaluation is obtained.

## 4. (K.4) Comparison with certified data (NUMÉRICO / CITED)
μ = 15, c = 30π: 1−λ₀ ≈ 9.44e−81, Fuchs 1−λ₄ ≈ 1.272e−70 (reproduces PATTERN_001), ratio 1.35e10 = (8⁴/4!)c⁴.
- Mori VIII's certified margin 2.40e−70 (CITED) is 1.89·(1−λ₄). In units of 1−λ₀ it is 5.0e5·μ⁴(1−λ₀), so the empirical law
has a = 4, κ₀ ≈ 5·10⁵ (NUMÉRICO). The defect index 4 is consistent with K.1b: the constraints absorb the lowest even prolates
(ARGUED).
- Guo Thm 1.6 (upper side, CITED) bounds W_T on prolate images from above only. It gives no κ₀ > 0.

For ψ₂ and ψ₄: each needs the same f̂(0) repair. ψ₂ repairs along ψ₀/ψ₄ with defect ≍ 1−λ₄ when ψ₀ is excluded. ψ₄ is
the first even index whose repair stays at its own defect scale. This is the natural extremal candidate (ARGUED). Its
exact evaluation meets the same circularity as §3.

## 5. Labels and residual
- PROVED: K.1a; K.1b (given CITED Hermite/Fuchs); K.3 (identity and technique NO-GO).
- CITED: Slepian–Pollak, Slepian 1965, Fuchs 1964, Dunster 1986, Guo (4.6)/Thm 1.6, Mori VIII margin.
- ARGUED: C_c normalisation; edge-cutoff negligibility; index-4 reading; local symbol.
- NUMÉRICO: §4.
- OPEN: the reposed target, "W_T(Eψ₄^adm) ≥ κμ^{−A}(1−λ₄)", i.e. the κ-band lower half. Row D OPEN. No sign claimed.

Do not retry: J.3-type Poisson-in-m evaluation on PW tails (dual terms k < λu are the window); "Eψ₀ + small correction"
as extremal (f̂(0) = 0 costs O(1) along ψ₂).
