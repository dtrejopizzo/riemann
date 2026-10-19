# R163_101 — The Beurling frontier (BF_θ), θ < ½

Pure math, no numerics. Target: (BF_θ) of R163_003 §3. No sign claimed. Gate 1 and Row D stay OPEN.

**Verdict.**
- **(BF_θ) in the extended class** (dΠ ≥ 0, the project's "genuine" class of R162_2901 §0): **YES for every θ ∈ (0,1). PROVED** (§2). It is a two-line check on a system Broucke writes down.
- **(BF_θ) for discrete systems** (integer prime multiplicities): **OPEN.** The literature has no construction and no obstruction for θ < ½ (SURVEY, §1). A random-rounding construction gives counterexamples for θ ∈ (1/3, ½) *heuristically*. This is PARTIAL (§4): the linear and quadratic orders are computed, and the full exp_* chaos is not controlled.
- **R162_2901 Thm B family:** this is not a counterexample and not θ-regular for any θ < 1. More generally, no positive "ζ × rational" system can have an R-created off-line zero with θ < ½. PROVED (§3).
- **Obstructions using only the analytic data** (analyticity for Re s > θ, growth, dΠ ≥ 0/Landau, Phragmén–Lindelöf, Jensen, mean values, Euler product in the extended sense): **NO-GO (PROVED).** Any theorem "θ < ½ ⇒ zeros on the line" must use the **integrality of the prime multiplicities** (§5).

Labels: CITED = read in `00-references/beurling-dmv` (file:line given). CITED-2 = a secondary quotation of a primary source that was not read.

## 1. SURVEY: what the references say at θ ≤ ½

1. **DMV** (Math. Ann. 334 (2006); primary paper not read). For each θ ∈ (½,1) there is a discrete system with N(x) = Ax + O(x^θ) and zeros on σ = 1 − a/log(|t|+2). CITED-2: 2409.10051.txt:2687–2692, 2004.11501.txt:17, 2207.00665.txt:199–210 (the last says "at least if θ > 1/2"). **No statement at θ ≤ ½.**
2. **Zhang** (Math. Ann. 337 (2007), zbMATH record). Two discrete systems with N(x) = kx + O(x^{½}exp(c(log x)^{2/3})): one satisfies RH, the other has infinitely many zeros on σ = 1 − 1/log t. This is the DMV phenomenon *at* the √x level, up to a factor x^{o(1)}. It is the closest known example to θ = ½; nothing is known below it.
3. **Broucke 2409.10051, §6.1, Thm 6.3** (lines 2380–2665). For θ ∈ [½,1) there is a discrete system with N = Ax + O(x^θ(1+𝟙_{θ=½} log x)) and N(ζ_P; (1+θ)/2, T) ~ ((1−θ)T/2π) log T. It has off-line zeros for every θ ≥ ½ (including θ = ½ up to a log). The proof explicitly assumes θ ≥ ½ (line 2380). The author states that the range α > (1+θ)/2 "should be optimal for any value of θ" and is proved only for θ > ½ (lines 245–246). Open question (lines 222–226): can a_j ≡ 1, the Euler product or multiplicativity improve the density estimates?
4. **BDV 2004.11501.** A discrete system satisfying RH, with N oscillating at x·exp(−c√(log x log log x)). The discretisation is DMV random Bernoulli primes (§6, lines 2618–2700), and log ζ₀ − log ζ_C continues only to σ > ½ (Lemma 6.2, line 2888). The Bateman–Diamond problem is open except at the endpoints (lines 224–267).
5. **Révész 2207.00665:186** (CITED-2 of Hilberdink, JNT 112 (2005); Neamah–Hilberdink 2020). For discrete systems, among the exponents of the errors in N, ψ and M_G, "the two largest have to be at least 1/2 and must match". This is the **only integrality-based constraint** found. With θ < ½ it forces exp(ψ) = exp(M_G) ≥ ½. That is consistent with off-line zeros and is not a zero-free region.
6. **2211.08716** (Broucke–Debruyne). The short-interval and density results are all stated for θ ∈ (½,1) (lines 108, 1191). **2012.06220:** Lemma 2.1 (DMV/Zhang discretisation) gives π error O(√x) (lines 164–180).

**Where the method breaks at θ = ½.** There are two separate steps.
- **(B1) Random discretisation (DMV/Zhang/BDV).** Bernoulli primes with probability q_j give π(x) = Π_C(x) + O(√x) (Lemma 2.1 of 2012.06220; bound (A) in BDV §6). The random factor e^{Z} with Z = log ζ₀ − log ζ_C is controlled only in σ > ½, because the variance Σ v_j^{−2σ} converges only for σ > ½ when there is one atom per unit of logarithmic density. So the integer error is at best x^{½+o(1)}. This is a central-limit barrier and is intrinsic to rounding a continuous prime density 1/log u.
- **(B2) Deterministic floor-rounding (Broucke Thm 6.3, lines 2595–2625).** The extended system ζ_θ is rounded to ⌊a_{p,m}⌋. The removed measure satisfies N_R(x) ≪ x^{1−θ} (Lemma 6.2). The error is x^{1−θ} + x^θ∫_1^x u^{−2θ}du. This is ≪ x^θ **iff θ ≥ ½**; for θ < ½ it is x^{1−θ} > x^θ. The step fails because the error is bounded by the **total variation** of the rounding measure dM_R ≤ dN_R, with no cancellation.

## 2. PROVED: (BF_θ) is YES in the extended (positive-measure) class

**Proposition 1.** Fix θ ∈ (0,1) and put a = θ/(1−θ). Following Broucke (2409.10051 §6.1), define
  dN_θ = Σ_n n^{a} δ_{n^{1/(1−θ)}},  dΠ_θ = Σ_p Σ_{m≥1} (1/m) p^{ma} δ_{p^{m/(1−θ)}}.

Then:
- (i) dΠ_θ ≥ 0, dN_θ = exp_*(dΠ_θ), and ζ_θ(s) = ζ((s−θ)/(1−θ));
- (ii) N_θ(x) = (1−θ)x + O(x^θ);
- (iii) ζ_θ has infinitely many zeros on Re s = (1+θ)/2 > ½, and every nontrivial zero has real part in (θ,1).

*Proof.* (i) Put w = (s−θ)/(1−θ). Then Σ_n n^{a} n^{−s/(1−θ)} = Σ n^{−w}, and log ζ(w) = Σ_{p,m} p^{−mw}/m = Σ p^{ma}(p^{m/(1−θ)})^{−s}/m. Since exp_* of a measure corresponds to exp of its transform, and the measures are positive, (i) holds.
(ii) Put X = x^{1−θ}. Euler–Maclaurin with 0 < a gives Σ_{n≤X} n^a = X^{a+1}/(a+1) + O(X^a). Here X^{a+1} = x and 1/(a+1) = 1−θ, and X^a = x^θ.
(iii) A zero ρ of ζ(w) maps to s = θ + (1−θ)ρ. Hardy's zeros on Re w = ½ give Re s = (1+θ)/2. ∎

**Consequence.** Take (BF_θ) as literally posed in R163_003 with "sistema de Beurling" read as dΠ ≥ 0. This is the meaning used in R162_2901 §0 and the one fed into the dichotomy there. Then (BF_θ) has a positive answer for **every** θ ∈ (0,½), with the zeros at a fixed distance θ/2 to the right of the critical line. This also holds for small θ, where the system tends to ζ itself as θ → 0.

So the first branch of R163_003's dichotomy ("integer error < √x ⇒ Beurling RH, a class statement") is **false in the positive-measure class**. It can survive only in the discrete class.

## 3. PROVED: R162_2901 Thm B, and the ζ × rational class

**(a) θ of N₀ for ζ₀^K = ζ·S₁^K·P₀/P.** ζ₀^K has a pole of order K+1 at s = 1 (R162_2901 Thm B(iv)), so N₀^K(x) ~ c x (log x)^K. For K ≥ 1 this is not of the form ρx + O(x^θ) for any θ < 1. For K = 0 (the strict class), dΠ₀ ≥ 0 fails (Thm A). Moreover, by Thm B(iv) every strip zero of ζ₀^K is on the line. **Thm B gives no conditional counterexample.** It is the opposite type of object: it is positive and on the line, but not θ-regular.

The mirror system ζ·S₁^K·P/P₀, with an *artificial* off-line quartet A, is unconditional and positive by the same K₀ argument (λ ↦ −λ). It has off-line zeros but the same pole of order K+1, so it is also not θ-regular.

**(b) Lemma R.** Let R be rational with R(∞) = 1. Suppose ζ_B = ζR is a positive Beurling system (dΠ_B ≥ 0) with a simple pole at 1 and N_B(x) = ρx + O(x^θ). If R has a zero at ½+β+iγ with β > 0, then θ ≥ ½+β.

*Proof.* Frullani gives dΠ_B = (Λ-atoms) + λ(u)du/u, where λ(u) = Σ_{poles of R} e^{au} − Σ_{zeros of R} e^{au} (with multiplicity). The atoms are singular, so λ ≥ 0 a.e. Let σ* be the largest real part of an exponent with nonzero net coefficient; then σ* ≥ ½+β. Write λ = e^{σ* u}(f(u) + o(1)) with f a trigonometric polynomial. Since λ ≥ 0, we get liminf f ≥ 0, and so f ≥ 0 because f is almost periodic. Its Bohr mean is the coefficient of the real exponent σ*. That coefficient is > 0, because otherwise f ≡ 0, which contradicts the choice of σ*. So R has a pole at the real point σ*.

Now place σ*. It cannot be > 1, because a pole at a real point > 1 is impossible for a series with dN ≥ 0 and N ~ ρx. It cannot equal 1, because the pole at 1 is simple and R(1) ≠ 0,∞. So ½+β ≤ σ* < 1. Since ζ(σ*) ≠ 0, ζ_B has a pole at σ*, and N_B(x) − ρx ~ c x^{σ*} with c ≠ 0. ∎

So **rational modifications of ζ cannot produce (BF_θ) counterexamples for θ < ½**. This is Landau's real-singularity principle: positivity pays for the off-line zero with a real singularity at least as far right. Broucke's ζ_θ avoids this because its positive part is **atomic and rescaled**, not a finite sum of exponentials.

## 4. PARTIAL: a discrete construction for θ ∈ (1/3, ½) (heuristic at full order)

**Construction.** Round Broucke's multiplicities *randomly* instead of taking the floor. At each point y = p^{m/(1−θ)}, put ⌊a⌋ or ⌈a⌉ primes, with the probabilities chosen so that the mean equals a = a_{p,m}. The error is ε_y ∈ (−1,1), independent and of mean 0. Let π_P be the resulting counting function and Π_P = Σ_k π_P(x^{1/k})/k. Then
  ζ_P = ζ_θ · e^{Z},  Z(s) = Σ_y ε_y y^{−s} + (a series in y^{−ks}, k ≥ 2, that converges absolutely for σ > (1−θ)/2).

**PROVED ingredients.**
- The atoms satisfy #{y ≤ x} ≍ x^{1−θ}/log x. So Var Z(σ) = Σ Var(ε_y) y^{−2σ} < ∞ iff **σ > (1−θ)/2**.
- This threshold replaces DMV's ½ in (B1), because only fractional parts are rounded and the atoms are sparse.
- Kolmogorov's three-series theorem gives a.s. convergence of Z for σ > (1−θ)/2.
- The DMV/Zhang sup-bound argument (2012.06220 Lemma 2.1; BDV bound (B)) adapts to give, a.s., Z(s) ≪ √(log|t|) for σ ≥ (1−θ)/2 + ε. This is standard; the adaptation is sketched, not written out.
- Consequently: ζ_P has exactly ζ_θ's zeros in σ > (1−θ)/2, and in particular zeros on Re s = (1+θ)/2. The kernel K = exp_*(dΠ_P − dΠ_θ) satisfies K(y) ≪ y^{(1−θ)/2+ε}. The proof is Perron's formula applied to e^{Z}/s, which has subpolynomial growth. For the truncation, the local mass is bounded by exp_*(|dΠ_R|), which is ≪ y^{1−θ+ε}.

**Integer error.** Write N_P = N_θ * K. Using §2(ii), the main term is (1−θ)e^{Z(1)}x + O(x^{(1−θ)/2+ε}).

The remaining term is ∫E_θ(x/u) dK(u), where E_θ(y) = −y^θ ψ(y^{1−θ}) + O(1) and ψ is the sawtooth.
- At **linear order** in ε, this is Σ_y ε_y E_θ(x/y). Its variance is ≪ x^{2θ} Σ_{y≤x} y^{−2θ} ≍ x^{2θ} + x^{1−θ}.
- At **quadratic order**, the off-diagonal part has the same size up to log x. The diagonal ε_y² (nonzero mean) is a deterministic measure at the y², which contributes O(x^{(1−θ)/2}).

The heuristic integer error exponent is therefore
  Θ(θ) = max(θ, (1−θ)/2),  equal to θ iff θ ≥ 1/3.

**Conjecture C₁/₃.** For every θ ∈ (1/3, ½) there is a discrete Beurling system with N(x) = ρx + O(x^{θ+ε}) and zeros on Re s = (1+θ)/2.

**The open step** is to control the full exp_* chaos: terms of order k ≤ C log x in the ε's, with tails uniform over a grid of x of spacing x^θ (N_P is monotone, so a grid suffices). The alternative is a divisor-problem-type estimate for ∫y^θ e(h y^{1−θ}) dK(x/y) that goes below total variation.

Total variation is exactly what breaks Broucke's (B2): it gives x^{1−θ}. The random version replaces it by its square root, x^{(1−θ)/2}. This is the precise place where θ = ½ becomes θ = 1/3.

## 5. NO-GO (PROVED): analytic obstructions

The system ζ_θ of Proposition 1 satisfies all of the following for θ < ½:
- ζ − ρ/(s−1) is analytic in Re s > θ;
- polynomial growth (and the Phragmén–Lindelöf/convexity bounds inherited from ζ(w));
- dΠ ≥ 0, so every Landau-type positivity argument applies to it;
- an Euler product (extended sense) and a Jensen zero count of order T log T;
- the Broucke density estimates.

It still has zeros at Re s = (1+θ)/2. Hence **no argument that uses only these properties can prove a zero-free region to the right of (1+θ)/2**. In particular none can prove RH for θ-regular systems, nor any region beyond what holds for ζ((s−θ)/(1−θ)).

The only property ζ_θ lacks is **integer prime multiplicities**. Lemma R and (B2) show that integrality is where every mechanism acts. The only integrality-based theorem found (Hilberdink 2005, item 5 of §1) forces an exponent ≥ ½ onto ψ and M_G, not onto the zeros.

## 6. Consequence for the program (R163_003 dichotomy)

- The "class-statement" branch (θ < ½ ⇒ RH, uniform over the Beurling class) is **refuted in the positive-measure class** (Prop. 1). It remains possible only for discrete systems.
- If Conjecture C₁/₃ holds, the discrete branch is refuted too, for θ ∈ (1/3, ½). The frontier would then move to θ ≤ 1/3.
  - Data point: Dedekind zetas of quadratic fields have θ = 1/3 (Landau's exponent 1 − 2/(d+1)) and are conjectured to satisfy RH (GRH).
  - The heuristic bound Θ ≥ 1/3 of random rounding is the same number, but no link is claimed.
- In both cases the discriminator is again **integrality/atomicity**: here of the *prime* multiplicities (discrete class), and for ζ of the exact lattice N(x) = ⌊x⌋. This is the same place R162_2901 and R163_002 end: O2601.1.
- New residuals:
  - **O163.101a:** prove C₁/₃ (chaos control).
  - **O163.101b:** find a discrete construction with Θ < 1/3 and off-line zeros, or an integrality obstruction at θ < 1/3.
  - **O163.101c:** decide whether Hilberdink's matching theorem can be sharpened to a statement about zeros.
