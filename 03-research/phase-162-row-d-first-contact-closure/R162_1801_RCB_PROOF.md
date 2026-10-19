# R162_1801 — R-C.b (no Type I first contact): weight-blind attempt

Note. Pure mathematics, no numerics.
Inputs: R162_1701 (Thm 1, Lemma C, Thm 3, Props 4–6), R162_1602 (Prop C, Prop R, Lemma R′), R162_504 (Thms 1–3,
Prop 4.1), R162_1601 (float, UNCERTIFIED). Corpus grep: "polariz", "two-point", "Baernstein", "homotop", "cyclic",
"residue at mu_2". Nothing beyond 1602 §4(i) and 1701 §2 was found.

**Status: PARTIAL.**
- §1 Theorem A: an exact spectral restatement of R-C.b. **PROVED**.
- §2 Theorem B: Perron structure plus homotopy in s cannot exclude Type I. This is idea (i). **NO-GO, PROVED**.
- §3 Proposition P: two-point polarization is broken by any positive comb. This is idea (ii). **NO-GO, PROVED**.
- §4 Theorem D: (C2) fails for a = sΛ at windows where the comb dominates, and first contact is exactly what bounds the
  comb. **PROVED**. Consequence: a proof of (C2) must use λ_A ≥ 0 on (0, T]; it cannot be a property of the operator
  alone.
- §5 The precise residual, reduced to one statement. **OPEN**.

No sign is claimed. No label moves. Gate 1 stays OPEN.

## 1. Theorem A (spectral form of R-C.b) — PROVED

Setting: T_W = T_*, as in R162_1701 Thm 1. Let f_ev(z) = ⟨(A^ev − z)^{−1}φ_ev, φ_ev⟩, as in 504 §4.

**Theorem A.**
1. An even first contact at T_* is Type I ⟺ μ₂^ev(T_*) = 0.
   Equivalently, R-C.b in the even sector ⟺ **μ₂^ev(T_*) > 0**, i.e. A^ev_{T_*} has exactly one nonpositive
   eigenvalue.
2. If μ₂^ev(T) is simple with eigenvector u₂, then
   ⟨u₂, φ_ev⟩ = 0 ⟺ f_ev has no pole at μ₂^ev ⟺ the compressed bottom z₀(T) and μ₂^ev(T) coincide or cross
   (interlacing is no longer strict).
   An even Type I contact is therefore a codimension-2 event, {μ₂^ev = 0} ∩ {Res_{μ₂} f_ev = ⟨u₂,φ⟩² = 0}. Near it,
   the zero z₀ of f_ev merges with the pole μ₂ as the residue tends to 0.
3. Odd sector: an odd contact is Type I ⟺ 0 ∈ spec A^odd_{T_*} with an eigenvector ⊥ φ_odd.

*Proof.*
- (1, ⟸) If μ₂^ev(T_*) = 0, then 0 is an eigenvalue. The even contact satisfies λ_ev(T_*) = 0 ≤ μ₂^ev, and
  interlacing (504 Thm 2(b)) gives μ₁ < λ_ev ≤ μ₂^ev. So λ_ev = μ₂^ev.
  - If ⟨u₂, φ⟩ ≠ 0 for every u₂ ∈ E₂, then f_ev has a pole at μ₂. Its zero in (μ₁, μ₂) lies strictly below μ₂ = 0,
    which contradicts λ_ev(T_*) = 0. Hence some u₂ ∈ E₂ ∩ ker ℓ_ev.
  - That u₂ satisfies AF = 0 with r = 0, so it is Type I.
- (1, ⟹) Type I means AF = 0 with F ≠ 0, F ⊥ ψ, so 0 = μ_k^ev with k ≥ 2 (504 Thm 3). Hence μ₂^ev ≤ 0. Interlacing
  gives μ₂^ev ≥ λ_ev = 0.
- (2) The residue of f_ev at a simple eigenvalue μ is ⟨u,φ⟩². The rest is Weinstein–Aronszajn (504 §4).
- (3) This is 504 Thm 3. ∎

**Reading.** R-C.b is a second-eigenvalue statement localised at the contact: "at T_*, the Tate-constrained bottom
sits strictly below μ₂^ev". It is weaker than 504 Cor 2.1 (μ₂ ≥ 0 for all T, which is E1), because it is imposed only
at T_* and only in the even sector. This should be recorded next to R162_504.

## 2. Idea (i), homotopy in the comb coupling: NO-GO — PROVED

**Theorem B.** There are symmetric 3×3 matrices M_s, s ∈ [0,1], and a fixed vector φ > 0 such that:
- every M_s has strictly positive entries (so e^{tM_s} is positivity improving and the Perron eigenvalue is simple);
- the spectrum of M_s is {3, 1, 0} for every s, so it is simple and no eigenvalue ever crosses another;
- the second eigenvector v₂(s) satisfies ⟨v₂(0), φ⟩ ≠ 0 and ⟨v₂(1), φ⟩ = 0.

With A_s := −M_s, the event at s = 1 is exactly a Type I configuration: the second eigenvector is orthogonal to a
positive "Tate" vector.

*Proof.*
- Take v₁ = (1,1,1)/√3. Let v₂(s) be a unit vector in v₁^⊥ that rotates from (1,0,−1)/√2 at s = 0 to (1,−2,1)/√6 at
  s = 1. Let v₃(s) be the completing unit vector in v₁^⊥.
- Put M_s = 3v₁v₁ᵀ + v₂(s)v₂(s)ᵀ.
- Entries of M_s: 3v₁v₁ᵀ has all entries equal to 1. A unit vector x ⊥ (1,1,1) has max_i x_i² ≤ 2/3, so
  |x_i x_j| ≤ 2/3. Hence (M_s)_{ij} ≥ 1 − 2/3 > 0.
- Take φ = (1+ε, 1, 1−ε) with 0 < ε < 1. Then ⟨v₂(0), φ⟩ = √2 ε ≠ 0 and ⟨v₂(1), φ⟩ = (1+ε − 2 + 1−ε)/√6 = 0. ∎

**Consequences.**
- Perron–Frobenius constrains only the ground state. Along a positivity-preserving homotopy, ⟨u₂, φ⟩ can pass through 0
  without any eigenvalue crossing and without losing irreducibility.
- So the argument "a Type I event needs a crossing that Perron forbids" is false in general.
- A homotopy proof would have to carry an **oriented** invariant, i.e. a continuous sign of ⟨u₂, φ⟩ fixed by some
  normalisation of u₂. On a simply connected parameter set where μ₂ is simple, u₂ can always be oriented continuously.
  The pairing then keeps its sign ⟺ it never vanishes, and that is R-C.b itself.
- The only known source of such an orientation is nodal: u₂ has one sign change on (0,T) and is positive near 0, and
  ψ/cosh is monotone. That is (N2) + (C2) (1701 Prop 6). Idea (i) therefore **reduces back to (C2) + (N2)**.
- The example is consistent with Lemma C:
  - at s = 1, φ/ψ = (1+ε, 1, 1−ε) is strictly monotone;
  - v₂(1) = (1,−2,1)/√6 has two sign changes, so it violates (N2).
  - The obstruction is exactly the nodal count.

## 3. Idea (ii), two-point rearrangement: NO-GO — PROVED

Take the reflection σ_p(t) = 2p − t with p ∈ (0,T). Let H be the half-line {t < p}, which contains the centre. The
polarization is F^p(t) = max(F(t), F(σ_p t)) on H and min(F(t), F(σ_p t)) off H.
- It preserves L^p norms.
- It keeps supp ⊂ I_T: for t < 2p − T we have σ_p t > T, so F^p(t) = F(t).
- For a kernel g(t − s), the two-point inequality ∬F^pF^p g ≥ ∬FF g holds for all F ≥ 0 ⟺ g(|t−s|) ≥ g(|t+s−2p|)
  whenever t, s ∈ H. This is Baernstein–Taylor (CITED): the four-point check on the pair {t, σt} × {s, σs}.

**Proposition P.**
- Let g_h = δ(|u| − h), a single comb tooth, and p ∈ (0,T) with h < 2T.
- Then there are F ≥ 0 supported in I_T with c_{F^p}(h) < c_F(h). So −v c_F(h) increases under polarization for every
  v > 0.
- Hence no polarization about any point of the window (the only window-preserving isometric reflections are σ_p with the
  rule above) lowers a_T when some v_n > 0.

*Proof.*
- Pick t₀ ∈ H and s₀ = t₀ + h, with s₀ ∉ H and σ_p s₀ ∈ I_T.
- Take F = 1_{B(t₀,η)} + 1_{B(s₀,η)} with small η. Then c_F(h) ≈ 2η.
- Polarization moves the bump at s₀ to σ_p s₀ ∈ H. After that, the two bumps sit at distance |t₀ − σ_p s₀| =
  |2t₀ + h − 2p|, which is ≠ h for generic p. So c_{F^p}(h) = 0 for η small.
- This is Lemma R′ of 1602 made two-point. ∎

**Weighted variant.** (C2) is monotonicity of w = ψ/cosh, not of ψ. In the variable w the archimedean form becomes
∬(w(t)cosh(t/2) − w(s)cosh(s/2))²k(t−s). This is not translation invariant, so the polarization inequality already
fails for the comb-free part: the four-point check needs k(t−s)cosh(t/2)cosh(s/2) to satisfy the Baernstein–Taylor
condition, and the product with cosh(t/2)cosh(s/2) does not.
- The weighted route is therefore closed at the archimedean level too. The only rearrangement input is Almgren–Lieb for
  ψ itself, and it works only when v ≡ 0 (1602 Prop R).

## 4. (C2) is not an operator property: Theorem D — PROVED

Take a single active shift h = log n with h/2 < T < h. For a = sΛ this is n = 2 and T ∈ (½log2, ½log3). Let
J = [h−T, T], M₊ = (0, h−T), and v = s·v_n.

**Lemma D1 (reflection form of the comb).** For even F on I_T,
  c_F(h) = 2∫_J F(t)F(h−t) dt.
So on even functions the comb couples J to itself by the reflection about h/2.
*Proof.* F(t)F(t−h) ≠ 0 requires t ∈ J. Then use F(t−h) = F(h−t) and add the symmetric half. ∎

**Theorem D.**
(a) There is V₀(T, h) < ∞ such that for v ≥ V₀ the ground state ψ_T of A_T is **not** such that ψ/cosh is
    nonincreasing on (0,T). So (C2) fails.
(b) If λ_A(τ) ≥ 0 for all τ ≤ T (i.e. T ≤ T_*), then v ≤ 2γ(T), where
    γ(T) := inf{Γ_T(F)/‖F‖² : F even, F(t) = F(t−h) on J, supp F ⊂ J ∪ (J−h), ℓ_ev(F) = 0} < ∞.
    So at and before first contact the comb is bounded by an archimedean constant, and (a) cannot occur with an
    arbitrarily large v.

*Proof.*
- (b) The admissible class is infinite-dimensional, so ker ℓ_ev meets it. For F in the class,
  c_F(h) = ∫_J F² = ½‖F‖². Hence a_T(F) = Γ_T(F) − (v/2)‖F‖², where Γ_T is the archimedean part of a_T. If
  λ_A(T) ≥ 0 then a_T ≥ 0 on P_T^ev, which gives v ≤ 2γ. γ < ∞ because smooth bumps have finite Γ-energy (the symbol
  grows like log).
- (a) Write c₀ := inf spec Γ_T > −∞, and let C₁ be the Rayleigh quotient of a fixed smooth even F₀ in the class of (b),
  without the ℓ-constraint.
  - Cauchy–Schwarz gives |c_F(h)| ≤ ½(‖F‖² − ‖F|_M‖²), where M = (T−h, h−T) is the middle.
  - Hence μ₁ ≥ c₀ − (v/2)(1 − ‖ψ_M‖²) for the normalised ψ, while μ₁ ≤ C₁ − v/2.
  - So ‖ψ_M‖² ≤ 2(C₁ − c₀)/v.
  - Now suppose ψ/cosh is nonincreasing on (0,T). For s ∈ M₊ and t ∈ J this gives
    ψ(s) ≥ ψ(t)cosh(s/2)/cosh(t/2) ≥ ψ(t)/cosh(T/2).
  - Squaring and integrating over s ∈ M₊ and t ∈ J gives |J|·‖ψ_{M₊}‖² ≥ |M₊|·‖ψ_J‖²/cosh²(T/2).
  - By evenness ‖ψ_J‖² = ½(1 − ‖ψ_M‖²) → ½, while ‖ψ_{M₊}‖² → 0. This is a contradiction for v large.
- Strict monotonicity is not needed for the contradiction. ∎

**Consequences.**
- (C2) fails in the amplification family a = sΛ (s large, T ∈ (½log2, ½log3)). This is inside a ≥ 0 and is the
  operator the task names.
- These windows lie beyond T_*(s) (by (b)), so R-C.b is not falsified. What is falsified is **(C2) as an a ≥ 0 operator
  property**.
- Any proof of (C2) at T_* must use λ_A ≥ 0 on (0, T_*], i.e. a quantitative bound on the comb relative to the
  archimedean energy of the kind in (b).
- The same regime also defeats (N2). In the limit v → ∞ the low even spectrum is Γ compressed to the class of (b). In
  G-coordinates (G = F|_J, even about h/2) the second even mode G₂ has two sign changes inside J ⊂ (0,T). This is
  stated as a heuristic, not proved: it needs the compressed ground state G₁ to be symmetric decreasing about h/2.
- Structural reading: by Lemma D1, the comb is a reflection coupling about h/2. It is maximised by functions symmetric
  about h/2 on J, and so it competes directly with monotone decrease from 0. (C2) at contact is a balance between the
  archimedean energy and this reflection term, not a positivity statement.

## 5. What remains: the single residual statement

By Theorem A, and with Theorems B and D and Proposition P closing ideas (i) and (ii), R-C.b (even) is equivalent to:

  **(R2) μ₂^ev(T_*) > 0**: at the first contact, A^ev has one nonpositive eigenvalue.

The best available sufficient condition is still 1701 Thm 3, (C2) + (N2) at the single window T_*. It can be refined
into one statement about the two lowest even modes:

  **(R2′)** Let t₀ be a sign change of u₂ on (0,T_*) and c = ψ(t₀)/cosh(t₀/2). Then u₂·(ψ − c·cosh(t/2)) ≥ 0
  on (0,T_*), and it is not ≡ 0.

- (R2′) implies ⟨u₂, cosh⟩ ≠ 0 (1701 Prop 6) and so implies R-C.b.
- It is implied by (C2) + (N2), but it is weaker: it asks only that ψ − c·cosh and u₂ change sign at the same place,
  not that each is globally monotone or single-crossing.
- Proving (R2′) requires, by Theorem D(b), the a priori comb bound v ≤ 2γ(T_*) (and its multi-shift analogue) as input.
  This is where any proof has to use the first-contact hypothesis.
- Odd sector: (P-odd) already fails once the reflected tooth is active (1701 §2.3). The odd residual is: 0 ∉ spec
  A^odd_{T_*} restricted to φ_odd^⊥. No reduction beyond Thm 3's odd version is available.

**Falsifier lines.**
- Theorems A, B, D and Proposition P use only v_n ≥ 0. They therefore hold for deletion, κ and sΛ, as intended.
- Deletion is a test of (R2), not a counterexample: at T_c = 0.5958 (float) it is Type II with μ₂^ev > 0 there,
  consistent with (R2).
- Test for R162_1803: compute μ₂^ev(T_*(s)) along a = sΛ, s ∈ [0, s_max]. (R2) predicts μ₂^ev(T_*(s)) > 0 throughout.
  A zero is a weight-blind counterexample, and R-C.b would then have to be arithmetic.

## 6. For README / R162_590

- R-C.b ⟺ μ₂^ev(T_*) > 0 (Thm A). This is a localised second-eigenvalue statement.
- Homotopy/Perron route NO-GO (Thm B, a 3×3 positive example with no crossing). Polarization NO-GO for any comb, and
  weighted polarization NO-GO even with no comb (Prop P).
- (C2) fails for sΛ at comb-dominated windows (Thm D). First contact bounds the comb (v ≤ 2γ). Any (C2)/(R2′) proof must
  use λ_A ≥ 0 up to T_*.
- Open: (O1801.1) prove (R2′) using the a priori comb bound; (O1801.2) the multi-shift version of D(b);
  (O1801.3) the float test of μ₂^ev(T_*(s)) along sΛ.
