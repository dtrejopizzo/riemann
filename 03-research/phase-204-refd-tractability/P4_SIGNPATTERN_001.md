# P4_SIGNPATTERN_001: the sign pattern of c_{g*} at the contacts (gap P4, phase 204k)

The numerics are done only on data that already exists in the corpus (Mori eigenvector
μ = 15 in `MORI15_EXTREMAL_001_data/p{0,1}_eig.json`) and carries the NUMERICAL label. Row D / L′♯ is treated as an
independent goal.

## Summary (≤250 words)

The fact from CALIB_R3 is that in Mori's even extremal (μ = 15, T = ½log15), c_{g*}(log n) > 0 holds for n = 2..14. **It is a
property of the test, not of the contacts.** I evaluated g* at 90 digits over 802 points of [0, T] (it is even) and g* **does not change
sign**: in the file's normalization it is −1.598 at 0, −9.7·10⁻¹⁶ at 1.2, and −1.42·10⁻³⁴ at T (NUMERICAL). Therefore
c_{g*}(u) > 0 throughout [0, 2T): the contacts avoid no zero, because there are no zeros to avoid. (The function that
changes sign, f* = 1.106ψ₀ − 1.822ψ₄, is the **Möbius inverse** of g* in the variable u, not g*.) It is the Perron–Frobenius
ground state, already indexed (P60-1, PARTIAL, «mechanism Λ(n) ≥ 0, gives simplicity, not sign»). It holds for
every comb with v_n ≥ 0 in which the pole does not dominate, so it is comb-generic. It includes (1+ε)Λ, whose floor at ½log15 is
negative (AUDIT_203).

The contrast with DH is a parity artifact. The DH witness is **odd**, and for odd F, ∫c_F = |F̂(0)|² = 0 forces c_F
to change sign. The odd sector of ζ also has c(log 2) = −0.333 < 0.

P4.1 holds trivially and does not discriminate (branch 1). The statement «min Σv_n c(log n) + arch + pole over c positive
definite with support in [−2T, 2T]» is, by Boas–Kac (CITED), exactly the LP (P) of def:PD (branch 2). **Verdict: P4
(contact sign pattern) NO-GO (ARGUED; lemmas PROVED/NUMERICAL). Gap 3 of BARRIER_SOUND_001 is closed in its
only data-bearing instance.**

## 0. Corpus check and new reason

I grepped `05-meta-and-planning/ROUTES-TRIED-INDEX/` for: «sign pattern» (1: V2_RECURRENCE_001, Theorem V2-0),
«contacts» (2: G2C-R161_027-029, G2B-R162_103), «nodal» (4: includes P74, W-jet, G8D), «Sturm» (3: G3F-105, G8D-155),
«Courant» (1: SPEC_011), «SPEC_011», «CS0», «Thm 3′» (AUDIT_200_DCONS), «non-analytic», «Lipschitz» (3), «staircase» (2:
G2D-R162_504, SYNTHESIS), «AUDIT_203», «CALIB_R3», «P4.1» (homonym P4-1 of Kreĭn, unrelated), «Turán» (5), «Delsarte»
(5, row 98, L55-A Johns), «Cohn» (row 76 Cohn–Elkies, row 78 Cohn–Gonçalves), «Bochner» (6, R5-04), «Fejér» (6, ES-13),
«Perron–Frobenius» (P60-1, G8D-R160_S2, G2D-R162_504), «Beurling–Deny» (G2D-R160_S3: «the pole kernel violates
Beurling–Deny»; INV_D_001) and «c_{g*}(log n)» (INVENT_001 Danskin; CALIB_R3).

**New reason, in writing, against what is recorded:**
- SPEC_011 counts **oscillations of the function** (of r, of f̂) and closes with Lemma N2 (a gap requires a cut unrelated to
  the comb). Here the object is different: the **sign of the autocorrelation evaluated at the contacts**, which is a finite pattern of
  signs, not a zero count.
- CS0 closes the Courant route going through a differential commutant. No differential operator is used here.
- AUDIT_203 reads the staircase (the values |c_{g*}(log n)|) as an edge profile. It does not examine whether c_{g*} has zeros **between**
  contacts, which is question (1). That question could have given an arithmetic fact if the contacts avoided zeros.
- V2-0 covers functionals of the sign pattern **of F** at {log n} via Thm 3′. Here the pattern is that of c_{g*}, a
  quadratic in g. V2-0 covers it in the form «sign function of a test functional» and Theorem X covers it at the
  minimizer, but neither had decided the **origin** of the pattern.

The new reason is question (1). If it is negative (no zeros between contacts), the route dies, and that is what happens.

## 1. Is the pattern a fact about g* or about the structure? (NUMERICAL + PROVED)

**Data.** I used the lower even eigenvector of the Mori form (832 Legendre modes by parity, 120 digits,
`p0_eig.json`) and the reconstruction g*(x) = Σ_j v_j √((2j+1)/2L) P_j(x/L), L = T = ½log15, via Clenshaw in mpmath with
dps = 90. The scripts are in the session's scratchpad (`g_mp.py`, `c_np.py`) and are not copied into the repository.

**Result 1.1 (NUMERICAL).** Over 401 equispaced points on [0, 0.76L] and another 401 on [0.75L, L], all values of
g*(x) have the same sign (negative in the file's normalization; the global sign is arbitrary). Sample values:
g*(0) = −1.5984649, g*(1.2) = −9.67·10⁻¹⁶, g*(L − 0.01) = −5.64·10⁻³⁰ and g*(L) = −1.4208·10⁻³⁴, all well above the
rounding error at 90 digits. This agrees with MORI15 §3, where |g*(T)|/√λ = 7.2·10⁻³⁵ and λ = √15 gives
|g*(T)| ≈ 2.8·10⁻³⁴ (same order; the factor of 2 comes from jump conventions). In double precision, over 20,001 points,
the only «sign changes» appear where |g*| < 10⁻¹⁶, i.e. they are noise. The high-precision grid discards them.

**Lemma 1.2 (PROVED, elementary).** If g is continuous on [−T, T], with g ≠ 0 on (−T, T) and of constant sign, then
c_g(u) = ∫ g(x) g(x+u) dx > 0 for all u ∈ [0, 2T). *Proof:* the integrand is ≥ 0 and > 0 on the open set
(−T, T−u) ≠ ∅. ∎

**Corollary 1.3 (NUMERICAL by 1.1 + PROVED by 1.2).** c_{g*} > 0 throughout [0, 2T). In particular it is positive at the 13
contacts and also at every ratio log(m/n), as MORI15 §3 already said («smooth function of the lag, no arithmetic
structure»). Direct evaluation of c_{g*} in double precision over a grid of 2,709 points confirms this where
c > 10⁻¹⁴: c(0.3) = 0.613, c(log 2) = 0.0639, c(log 3) = 4.87·10⁻⁴, c(log 4) = 1.58·10⁻⁶, c(log 5) = 2.71·10⁻⁹,
c(1.8) = 1.83·10⁻¹², no zeros in [0, 2.2]. For u > 2.2 double precision does not resolve, but 1.2 covers that stretch.

**Answer to (1).** The dichotomy of the goal was: if c_{g*} has zeros between contacts, the pattern is arithmetic; if
c_{g*} ≥ 0 throughout [0, 2T], it is a property of the test. The second branch holds, and in the strongest possible way: the test is
**single-signed**, so there are no zeros of c_{g*} anywhere.

**Premise correction.** The goal says that «f* = 1.106ψ₀ − 1.822ψ₄ changes sign» and that therefore c ≥ 0 would not be
automatic. But f* is not g*. In MORI15 §4, f* is the **Möbius inverse** f₁(u) = Σ_m μ(m)(mu)^{−½} g*(log mu) on
[1/λ, λ], and its sign changes (f₁ > 0 up to u ≈ 2/λ, f₁ < 0 from 3/λ on) come from μ(m), not from g*. The autocorrelation that
enters the form is that of g*, in the additive variable x. The sign changes of f* are not transmitted to c_{g*}.

**Why the ground state is single-signed (ARGUED, mechanism already indexed).** The even form is
W_T(g) = c₀‖g‖² + ℰ_Lévy(g) − Σ_n v_n c_g(log n) + 2(∫g cosh(x/2))², with v_n = 2Λ(n)n^{−½} ≥ 0. Each of the first three
terms satisfies Q(|g|) ≤ Q(g):
- for ℰ_Lévy = ∫[c(0) − c(v)]2ν(v) dv, because c_{|g|}(v) ≥ c_g(v), ν ≥ 0 and c_{|g|}(0) = c_g(0);
- for the comb, because c_{|g|} ≥ c_g and v_n ≥ 0.

This is Beurling–Deny / Perron–Frobenius. The pole goes the other way: (∫|g| cosh)² ≥ (∫g cosh)². This matches
row G2D-R160_S3 («the pole kernel violates Beurling–Deny»). That the minimizer is single-signed anyway says
that, at μ = 15, the Markov term dominates the rank-one pole in the direction of |g|. This is the simple ground state of
P60-1 («Perron–Frobenius of Weil's ground state, mechanism Λ(n) ≥ 0: gives simplicity, not sign»). The pattern
c_{g*}(log n) > 0 is exactly the imprint of that mechanism at the contacts.

## 2. The class «c_g ≥ 0 on [0, 2T]» and positivity of the form

**2.1 Precise class.** There are three distinct classes at play:
- (B) **positive type**, ĉ_g = |ĝ|² ≥ 0. This is automatic for every autocorrelation and restricts nothing.
- (C⁺) **non-negative autocorrelation**, c_g ≥ 0 on [0, 2T]. This is a genuine restriction, because it does not hold for odd g
  (∫c_g = |ĝ(0)|² = 0 and c_g(0) > 0 force it to take negative values).
- (P⁺) **single-signed tests**, g ≥ 0 or g ≤ 0. This is the class into which the minimizer falls.

One has (P⁺) ⊊ (C⁺) ⊊ (B). The inclusion (P⁺) ⊂ (C⁺) is Lemma 1.2. The inclusion is strict: there exist g with a small
sign change and c_g > 0, because the condition is open in c.

**2.2 What the class does NOT give (PROVED with one NUMERICAL datum).** The goal proposes seeking a statement of the type «if c_g ≥ 0 on
[0, 2T], then 𝔞_T(g) ≥ (explicit function)» with a bound useful for the sign. It gives nothing new. Since the even
minimizer g* lies in (P⁺) ⊂ (C⁺) (NUMERICAL 1.1), one has

  inf_{(C⁺), ‖g‖=1} W_T = inf_{(P⁺), ‖g‖=1} W_T = λ_A^{even}(T)   (μ = 15).

Any lower bound on the class is therefore a lower bound on the entire even sector, just as hard as the
full problem. Restricting to the class simplifies nothing.

**2.3 Structure of «all contacts subtract».** In (C⁺) the form is written 𝔞(g) = arch(g) + pole(g) − Σ v_n c_g(log n),
with every comb term ≤ 0. Positivity then reads as «arch + pole beats a sum of same-signed contacts».
This is precisely the **TV estimate**: Σ v_n c_g(log n) ≤ Σ v_n ‖c_g‖_∞ (BARRIER_EST). For mixed-sign tests,
by contrast, there is cancellation between contacts. Class (C⁺) is the **cancellation-free** region, where positivity depends
only on size bounds. There the cΛ class falsifier, c > 1, applies: AUDIT_203 gives a negative floor for (1+ε)Λ at ½log15 with
ε > 8·10⁻⁶⁹ (NUMERICAL-certifiable). By continuity of the simple ground state, its minimizer is also single-signed
(ARGUED), and yet the form is negative. **No statement that uses only «c ≥ 0 at the contacts» and v_n ≥ 0 can
give the sign.** This is proved by the pair Λ / (1+ε)Λ: same sign pattern, opposite signs of the form (ARGUED for the pattern of
(1+ε)Λ, by continuity; PROVED in the sense that the pattern does not contain the magnitude of the v_n, which is what decides).

**2.4 The contrast with DH is a parity matter (PROVED).** CALIB_R3's DH witness is **odd** (witness 9/5, «odd, 35
contacts»). For every odd F, ∫_ℝ c_F = |F̂(0)|² = 0 and c_F(0) = ‖F‖² > 0, so c_F takes negative values on (0, 2T).
Hence the mixed signs of c_F at the contacts are partly forced by parity. The odd sector of **ζ** has the
same thing: in MORI15 §3 (odd), c(log 2) = −0.3325, and the nine terms of the odd comb all have the same sign, negative,
i.e. c < 0 at every contact. In the odd sector of ζ, c_{g*} changes sign near u ≈ 0.31 (NUMERICAL, double
precision) and then stays negative at every contact. The comparison «ζ positive at contacts / DH mixed» compares the
even sector of ζ with an odd DH witness. It does not discriminate arithmetic.

## 3. Lemma P4.1 (DECIDED)

**BARRIER_SOUND_001's statement:** is the condition «c_{g*}(log n) > 0 ∀ n < N» stable under the comb (a_P, Beurling)?

**Decision (PROVED in the «same g*» form, ARGUED in the «minimizer of the perturbed comb» form).**

(a) **With the same g\*.** c_{g*} depends only on g*. Erasing prime P (a_P) or moving a contact δ(log 2) (Beurling),
c_{g*} does not change; only which contacts are summed changes. By Corollary 1.3, c_{g*} > 0 throughout [0, 2T), so **any**
set of contacts in [0, 2T) gives a positive pattern, including Beurling's shifted contacts. P4.1 holds
trivially and does not discriminate.

(b) **With the minimizer of the perturbed comb** (which is the relevant discriminant, according to Theorem X). For a_P and for
Beurling with weights ≥ 0, the Markov term remains Beurling–Deny (v_n ≥ 0), and the even ground state remains
simple and single-signed throughout the range where the pole does not dominate (P60-1, mechanism Λ(n) ≥ 0). That gives the same
positive pattern, with the condition open on the comb. By INVENT_001's Danskin, ∂λ_A/∂a(n) = −2n^{−½}c_{g*}(log n) < 0 for
every n: the pattern is exactly the gradient direction, a first-order discriminant and hence a functional of
h*, not of σ (Theorem X). This is the case BARRIER_SOUND_001 called «branch 1»: comb-generic and cancelable. The only way
to break the pattern is with mixed-sign weights (DH), which break Beurling–Deny. That is line F3 «DH, line v_n ≥ 0», already
DEAD (G2D-R162_504).

## 4. Is there a nontrivial statement of its own left? The extremal contact problem

**4.1 The goal's intuition is correct and has a name.** A minimizer would «want» c < 0 at the contacts (so they subtract
less), but the restriction ĉ = |ĝ|² ≥ 0 with support in [−2T, 2T] prevents it from making c very negative at many points at
once. It is the Turán/Delsarte type of restriction. The data show more besides: the minimizer does not even try. It takes c > 0
everywhere and pays the full comb, because in the direction of |g| the Markov term (Lévy + c₀) gets cheaper by more than
the comb gets more expensive. In the even sector, Perron–Frobenius and the energy win, not Turán.

**4.2 The extremal problem is def:PD (PROVED, with one citation).** The entire form is linear in c_g:
- arch(g) = (1/π)∫a|ĝ|² = (1/π)∫a ĉ_g;
- pole = 2(∫g e^{x/2})(∫g e^{−x/2}) = 2∫c_g(u)e^{u/2} du (a linear functional of c_g);
- the comb is linear in c_g.

Therefore W_T(g) = ℓ_T(c_g) with ℓ_T linear. Moreover:
- (Boas–Kac 1945, CITED; it holds in dimension 1 and fails in dimension ≥ 2, Rudin) every continuous positive-definite function with
  support in [−2T, 2T] is of the form g∗g̃ with supp g ⊂ [−T, T]. More generally, the closed convex cone generated by the
  autocorrelations {c_g : supp g ⊂ [−T, T]} is the cone of measures μ ≥ 0 on the spectral side whose transform vanishes
  for |u| ≥ 2T.
- Therefore inf{W_T(g) : ‖g‖ = 1} = inf{ℓ_T(c) : c positive definite, supp c ⊂ [−2T, 2T], c(0) = 1}. This is
  **literally (P) of def:PD** from Paper 46, with μ the spectral measure of c, «μ̌(u) = 0 for |u| ≥ 2T», and the
  primitive restrictions ĝ₀, ĝ₁ if working in the primitive class. Its dual (D) is the certificate (ν, β).

So «minimizing Σv_n c(log n) (+ arch + pole) subject to ĉ ≥ 0, supp c ⊂ [−2T, 2T]» is the Cohn–Elkies/Delsarte LP that
the corpus already solved as **def:PD / Theorem Z** (row 76: Cohn–Elkies gives the upper direction; Paper 46: flat-top
certificates). **It is branch 2:** it reads λ_A exactly. Adding the extra restriction «c ≥ 0 on [0, 2T]» (class C⁺) does not change
the infimum in the even sector (by 2.2), so the restricted LP has the same value as def:PD.

**4.3 The candidate for a statement of its own.** «ζ's even minimizer has positive autocorrelation on [0, 2T]», or
in its strong form, «it is single-signed». It is true (NUMERICAL at μ = 15) and is explained by a half-PROVED mechanism:
Perron–Frobenius for the Markov part (P60-1) plus control of the rank-one pole. But:
- it is a statement about the minimizer, so Theorem X covers it at first order: the pattern is the Danskin direction;
- it holds for every comb with v_n ≥ 0 and non-dominant pole, including (1+ε)Λ with a negative floor. It is comb-generic and implies
  no sign of the form (2.3);
- its only quantitative version, «inf over C⁺ = global inf», is a reduction, not a bound.

No nontrivial statement of its own carrying a sign remains.

## 5. Verdict

- (1) **Property of the test** (NUMERICAL + Lemma 1.2 PROVED): g* is single-signed on [−T, T] and c_{g*} > 0 throughout
  [0, 2T). There are no zeros for the contacts to avoid and no arithmetic fact.
- (2) Precise class: (P⁺) ⊊ (C⁺) ⊊ (B). (B) is automatic. In (C⁺) there is no cancellation between contacts, so
  positivity is a size estimate, and the falsifier (1+ε)Λ kills it. The contrast with DH is a parity matter (PROVED:
  ∫c_F = 0 for odd F; the odd sector of ζ is also negative at the contacts).
- (3) **P4.1 decided:** it holds trivially for the same g* (PROVED); it is stable under a_P and Beurling with weights ≥ 0
  for the perturbed minimizer (ARGUED, Perron–Frobenius); it is comb-generic, branch 1 (Theorem X / Danskin).
- (4) The extremal contact problem with ĉ ≥ 0 and support in [−2T, 2T] is, by Boas–Kac (CITED), **(P) of def:PD**: branch
  2.
- **Gap 3 of BARRIER_SOUND_001 (P4), in its only data-bearing instance: NO-GO (ARGUED; Lemma 1.2 and parity PROVED;
  1.1 NUMERICAL).** The general non-analytic class (Fredholm indices, inertias with |·|) remains uncovered by a theorem.
  But the only datum that made it relevant is Perron–Frobenius.

**Entry for the index (for the editor):**
- **P4_SIGNPATTERN_001 (phase 204k, gap P4): NO-GO (ARGUED; lemmas PROVED, NUMERICAL).** Mori's even g* (μ = 15) is
  single-signed on [−T, T] (90 digits, 802 points; g*(T) ≈ −1.42e−34 in the file's normalization) ⇒ c_{g*} > 0 throughout
  [0, 2T). The contact pattern is Perron–Frobenius (P60-1), not arithmetic; f* (with a sign change) is the Möbius
  inverse, not g*.
- The contrast with DH is a parity matter: odd F ⇒ ∫c_F = 0; the odd sector of ζ has c(log n) < 0.
- P4.1 holds trivially (branch 1, Danskin/Theorem X); (1+ε)Λ has the same pattern and a negative floor.
- The LP «min ℓ_T(c), ĉ ≥ 0, supp c ⊂ [−2T, 2T]» is def:PD by Boas–Kac (branch 2). Do not retry «positivity in the class
  c_g ≥ 0» nor «sign counts of c_{g*} at contacts».
