# Q2_DEGREE2_001 — Eisenstein–Epstein family E(τ,·): the window form as a function on the upper half-plane (phase 200, round 10)

Only positivity of window forms is discussed. Facts about zeros of
Epstein functions are CITED as facts about those functions. or invoked.
No new computation was done.

## Summary (≤300 words)

There is a continuous family, with FE and fixed Γ factor Γ(s) = Γ_ℝ(s)Γ_ℝ(s+1)·(const)^s, that passes through
ζ·L(·,χ₋₄) (τ = i) and through the falsifier x²+5y² (τ = i√5): Z_τ(s) = Σ'_{(m,n)}|mτ+n|^{−2s}, with conductor 4y²
(y = Im τ). Its window form 𝔞_T^{(τ)} is written with the template of Lemma E, and with it:
(L1, PROVED) For F in the core, τ ↦ 𝔞_T^{(τ)}(F) is continuous in τ, so S_T := {τ : 𝔞_T^{(τ)} ≥ 0} is closed.
  Passing to a generic τ is a Beurling deformation of the comb with FE: the frequencies are logs of values
  |mτ+n|².
(L2, PROVED except for an explicit constant) **Cusp lemma.** If T < log y, the form is exactly that of ζ(2s) on
  the squares plus the constant log(4y²)‖F‖². Hence S_T contains {y ≥ e^{2T+c}}.
(C, CITED) For y > 7.0556 (= 4πe^{−γ}; BIBLIO_CHECK_001 corrects 7.0236) the function Z_τ has a real zero in
  (½,1) (Bateman–Grosswald). Davenport–Heilbronn gives zeros in σ > 1 on a dense set of τ. So S_∞ = ∩_T S_T is
  bounded and is contained, save for one unverified case, in the 13 Heegner points h = 1, which all have
  y ≤ √163/2 ≈ 6.38. Whether the form is positive at those points remains OPEN.
(R, PROVED given C) **Restriction C-τ.** No lower bound that is continuous in τ and uniform in T on a
  neighborhood of an h = 1 point works as a proof. If positivity holds at those points, T*(τ) is a "needle."
**The Maass–Selberg identity integrated over 𝓕 is a RETRY.** The index (Front A) already records
"Maass–Selberg = window form of ζ(2s) on the squares" as NO-GO PROVED. Moreover the form is not linear in E
(it goes through the log-derivative), so ∫𝔞^{(τ)}dμ is not the form of ∫E. The Maass families are discrete. The
continuous family ζ(s+ir)ζ(s−ir) through ζ² is a modulation orbit and deforms nothing. Verdict Q2: the direction
exists and gives new geometry (Heegner needles), but gives no sign. What is new is the restriction C-τ.

---

## 0. Index and corpus check

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` for "Epstein", "Hecke", "Eisenstein", "Maass", "family",
"degree 2", "ζ_K", "Selberg class", "Lagarias", "Bateman", "Chowla". This is what exists:

- **README l.203–208 (phase 193, Front A, modular group/Hecke).** Records several things:
  - "Petersson/Maass–Selberg/Rankin–Selberg positivity (blind to the comb and to h*)";
  - "multiplicativity of Hecke on σ_T (comb-generic, PROVED)";
  - "transport of abscissa 1→½ by integration over Y or Hecke average (NO-GO PROVED;
    **Maass–Selberg = window form of ζ(2s) on the squares**)."

  **Consequence:** the "candidate theorem" proposed by the question (Maass–Selberg identity integrated over 𝓕
  for the window form) **appears in the index**. It is not retried. §5 explains why the variant "integrate
  𝔞^{(τ)} instead of E" does not dodge the reason for the failure: the object that comes out at the cusp is
  exactly the one on record (Lemma L2).
- **README l.227–228 (O10)**: the complete form separates ζ and ζ_{ℚ(i)} from the Epstein x²+5y² (NUMERICAL).
  This is consistent with τ = i versus τ = i√5.
- **README l.529, l.533, l.535 (GUO_QUANT_001, LEMMA_E_EPSTEIN_001, AUDIT_200_EPSTEIN_001).** They contain:
  - restriction C-Guo;
  - Lemma E PROVED;
  - C-E: every comb class closed under Λ ↦ ½(Λ₁+Λ₂)+Λ_cosh fails;
  - C₀^Q = log 20 + ψ(¼) + ψ(¾) − 2log π.
- **README l.536 (SPEC_SIGN_OBJECT_004)**: Prop 2.1, with Q2 open as "direction in degree 2 toward ζ²/ζ_K."
- **Q2_LADDER_001** (round 2): is a different "Q2," the ladder μ → μ/p, NO-GO. It is unrelated to the family of
  this memo.
- **05b l.50 (L98, Weng/Lagarias–Suzuki type)**: "comb-generic (only shifts of ξ)." The constant term of E(iy,s)
  is precisely a combination of shifts of ξ (§3). What was recorded is the positivity of those combinations, not
  the family in τ.
- "Bateman", "Grosswald", "Chowla", "Kronecker", "Epstein family in τ", "needle", "T*(τ)": **no entries**.

**What is new and why it is not a variant.** What is on record treats the modular family in three ways: as an
average (Maass–Selberg/RS), as a Hecke operator on σ_T, or as a constant term. The window form was never taken
as a **function of τ** nor was its positivity set studied. Nor was the family taken as "Beurling with FE." The
concrete difference: the object is the map τ ↦ 𝔞_T^{(τ)}, which is non-linear in E. What comes out of that is a
new restriction on methods (C-τ). No sign comes out.

## 1. The object: the family E(τ,·) and its window forms

### 1.1 Definition and FE (CITED: Epstein 1903; Chowla–Selberg 1949/1967)
Let τ = x + iy in the upper half-plane ℍ. Define

  Q_τ(m,n) = |mτ+n|² = n² + 2x mn + |τ|² m²,  disc(Q_τ) = −4y²,
  Z_τ(s) = Σ'_{(m,n)∈ℤ²} Q_τ(m,n)^{−s},  E(τ,s) = ½ y^s Z_τ(s).

Z_τ depends only on the orbit SL₂(ℤ)·τ. It converges for σ > 1, has a simple pole at s = 1 with residue π/y, and
Z_τ(0) = −1.

**FE (CITED).** With Λ_τ(s) := (2y/2π)^s Γ(s) Z_τ(s) one has Λ_τ(s) = Λ_τ(1−s). Λ_τ has simple poles only at 0
and 1. By duplication, (2y/2π)^sΓ(s) = ½(4y²)^{s/2}Γ_ℝ(s)Γ_ℝ(s+1).
- **The Γ factor is fixed:** Γ_ℝ(s)Γ_ℝ(s+1).
- **The conductor 4y² varies in a controlled way.**
- Control cases:
  - τ = i√5: 4y² = 20 (Lemma E ✓).
  - τ = i: 4y² = 4, Z_i = 4ζ(s)L(s,χ₋₄) (CITED, Jacobi).

In the classical normalization, ξ(2s)E(τ,s) = ξ(2−2s)E(τ,1−s) (ξ(s) = π^{−s/2}Γ(s/2)ζ(s)), which is the same FE.

### 1.2 Generalized comb (PROVED, formal)
Let 𝒱_τ = {Q_τ(m,n)} ⊂ (0,∞) be the set of values, with multiplicities r_τ(λ). Normalize
Z_τ/r_τ(λ₀) = 1 + Σ_{λ>λ₀} … with λ₀ = 1 the minimum, attained if τ is reduced. The log-derivative does not see
constants:

  −Z_τ′/Z_τ(s) = Σ_{μ∈𝔐_τ} Λ_τ(μ) μ^{−s},  σ > σ₀(τ).

𝔐_τ is the multiplicative semigroup generated by 𝒱_τ. The Λ_τ(μ) are defined by the recursion of the formal
exponential of a general Dirichlet series (Λ_τ(μ) = coefficients of −log, derived). The series converges
absolutely for σ sufficiently large. This is PROVED, in standard fashion, because
Z_τ/r_τ(1) − 1 = O(λ₁^{−σ}) with λ₁ > 1.

There are three cases:
- **τ with Q_τ proportional to an integral form:** 𝔐_τ ⊂ ℕ (after rescaling). It is a comb on log ℕ, integral.
- **Generic τ** (1, 2x, |τ|² linearly independent over ℚ): 𝒱_τ is not discrete on an arithmetic scale. 𝔐_τ is an
  infinite-rank Beurling semigroup with frequencies log μ. **This is a Beurling deformation of the comb that
  preserves the FE, the pole and the Γ factor.** The corpus's Beurling falsifier (ARGUED in P47) had never been
  built with an FE. E(τ,·) is one.
- **τ = iy with y² ∈ ℚ, y² = a/q:** values in (1/q)ℕ, and the comb moves with y.

### 1.3 The window form (PROVED from the FE, same derivation as LEMMA_E §1.3)
The Weil explicit formula for a function with FE, finitely many poles and a Dirichlet-series log-derivative
(general) does not use an Euler product (CITED: Weil 1952; for general frequencies, the same proof by contour
shift). Just as in Lemma E:

  **𝔞_T^{(τ)}(F) = C₀(τ)‖F‖² + ∫₀^{2T}(c(0)−c(u)) du/sinh(u/2) + Pol_T(F) − Σ_{μ∈𝔐_τ, log μ<2T} (2Λ_τ(μ)/√μ) c(log μ),**

where:
- c = c_F is the autocorrelation of F ∈ L²(I_T) (support in [−2T,2T], c(±2T) = 0);
- Pol_T is the polar term of ζ (same poles 0 and 1);
- C₀(τ) = log(4y²) + ψ(¼) + ψ(¾) − 2log π = **log(4y²) − 7.60276…**

Control: for 4y² = 20 this gives C₀ = −4.6070, which is the C₀^Q of Lemma E ✓.

**Tests (PROVED by identity of definitions):**
- τ = i√5: 𝔞_T^{(τ)} = 𝔞_T^Q of Lemma E. The value 𝔞/‖F‖² ∈ [−0.0619395254, −0.0619395173] at T = 8/5 is
  inherited as is (AUDIT_200_EPSTEIN_001). It is not recomputed: it is the same object with the same constant.
- τ = i: Λ_i = Λ_ζ + Λ_{χ₋₄} (log-derivative of 4ζL(χ₋₄)) and C₀(i) = log 4 − 7.60276 = the C₀ of ζ·L(·,χ₋₄) with
  conductor 4. Hence 𝔞_T^{(i)} = 𝔞_T^{ζ·L(χ₋₄)}.
- τ = ρ = e^{2πi/3}: Z_ρ = 6ζ(s)L(s,χ₋₃), conductor 4·¾ = 3 ✓ (CITED).

## 2. Continuity in τ and positivity sets

**Lemma L1 (PROVED for F ∈ C_c^∞(I_T), extension to the background ARGUED).** The map τ ↦ 𝔞_T^{(τ)}(F) is
continuous on ℍ.

*Proof.* C₀(τ) is continuous and the archimedean and polar terms do not depend on τ. For the comb, let
G(s) = ∫c(u)e^{(s−½)u}du. G is entire and, since c ∈ C_c^∞, decays faster than any power on vertical lines. One
has

  Σ_{log μ<2T} (Λ_τ(μ)/√μ) c(log μ) = (1/2πi)∫_{Re s=σ₁} (−Z_τ′/Z_τ)(s) G(s) ds

with σ₁ = σ₁(K) uniform for τ in a compact set K. Two facts are used:
- inf_{τ∈K} |Z_τ/r_τ(1)| ≥ ½ for σ ≥ σ₁, because the values Q_τ ≥ λ₁(K) > 1 away from the minima;
- the case where r_τ(1) jumps must be handled, at the elliptic points i and ρ, where more vectors of norm 1
  appear. At those points the extra minimal vectors have Q_τ → 1 continuously and the log-derivative is
  continuous all the same: −Z′/Z is continuous in τ as an analytic function, even though the normalization
  jumps.

With that, −Z_τ′/Z_τ is continuous in τ uniformly on Re s = σ₁ and bounded, and dominated convergence closes the
proof. Frequency collisions μ₁(τ) → μ₂(τ) sum up by themselves. ∎

**Corollary.** S_T := {τ ∈ ℍ : 𝔞_T^{(τ)}(F) ≥ 0 ∀F ∈ core} is an intersection of closed sets, hence **closed**
(PROVED). S_T decreases in T (P47 lem:monoT) and S_∞ := ∩_T S_T is closed. The function
T*(τ) := sup{T : τ ∈ S_T} ∈ (0,∞] is **upper semicontinuous** (PROVED: {T* ≥ T} = S_T is closed).

## 3. The cusp

### 3.1 Chowla–Selberg expansion (CITED)
For τ = x+iy:

  Z_τ(s) = 2ζ(2s) + 2√π Γ(s−½)ζ(2s−1)Γ(s)^{−1} y^{1−2s} + (8π^s y^{½−s}/Γ(s)) Σ_{n≥1} n^{s−½}σ_{1−2s}(n)K_{s−½}(2πny)cos(2πnx).

The third term is O(e^{−2πy}) uniformly on compact vertical strips. Written as E(τ,s) = y^s·(…): the constant
term is ζ*(2s)y^s + ζ*(2s−1)y^{1−s} (normalized with ξ). This is the Lagarias–Suzuki combination.

### 3.2 Lemma L2 (cusp; PROVED, with a constant to fix)
Let τ be in the fundamental domain 𝓕 (|x| ≤ ½, |τ| ≥ 1) and suppose **T < log y**. Then every value Q_τ(m,n)
with m ≠ 0 is ≥ y² > e^{2T}. Every μ ∈ 𝔐_τ with log μ < 2T is then a product of values with m = 0, i.e. squares
n², and in that range the log-derivative coefficients coincide with those of ζ(2s): Λ_τ(n²) = 2Λ(n). The reason
is that terms with m ≠ 0 contribute to the log-derivative only at frequencies ≥ y², by the semigroup structure.
Hence, exactly:

  **𝔞_T^{(τ)}(F) = (log(4y²) − 7.60276)‖F‖² + A(F) + Pol_T(F) − Σ_{2log n<2T} (4Λ(n)/n) c(2 log n).**

This is the window form of "ζ(2s) on the squares," the object of Front A, with conductor log(4y²). Positivity:
- A(F) ≥ 0, because |c(u)| ≤ c(0);
- |c| ≤ ‖F‖²;
- Σ_{n≤e^T} Λ(n)/n ≤ T + O(1) (Mertens; explicit Rosser–Schoenfeld constant CITED, to be fixed);
- the polar term is bounded by O(1)‖F‖² on P_T (P47).

With that:

  𝔞_T^{(τ)}(F) ≥ (2log(2y) − 4T − c₁)‖F‖².

Hence **S_T ⊇ {τ ∈ 𝓕 : y ≥ max(e^T, e^{2T+c₁/2}/2)}**. This is PROVED with the explicit c₁ pending.

**Reading.** At fixed T the cusp is trivially positive: the conductor 4y² wins. The ζ form (degree 1) does
**not** appear in the limit. What appears is ζ(2s) in the variable 2s, with frequencies log n² and an exploding
conductor. There is no reduction "E(τ,·) at i∞ = ζ plus a controllable term" that transports a sign: the term
y^{1−s}ζ*(2s−1) has no Dirichlet series in the window, and on the critical line it weighs the same as the first.
The question asks whether the form as τ → i∞ reduces to that of ζ plus a controllable term. **The answer is
NO-GO (PROVED by L2).** It reduces to ζ(2s)-on-squares, which is exactly what the index already records.

### 3.3 Real zeros near the cusp (CITED)
- **Bateman–Grosswald** (Acta Arith. 9, 1964): Z_τ has a real zero in (½,1) if y > 7.0556
  (= 4πe^{−γ}; BIBLIO_CHECK_001 corrects 7.0236)… The data are cited from memory. **The exact statement and the
  constant must be verified** before integrating into P47.
- **Lagarias–Suzuki** (J. Number Theory 118, 2006): the constant term a_y(s) = ζ*(2s)y^s + ζ*(2s−1)y^{1−s} has
  all its zeros on the line for 1 ≤ y ≤ y* = 4πe^{−γ} ≈ 7.0556, and exactly two real zeros off it for y > y*.
- **Ki** (2006): analogous results on zeros of Epstein approximations.

The two constants (7.02 and 7.06) are close because the Bessel tails are O(e^{−2π·7}).

## 4. The positivity set for ∀T

### 4.1 Zeros off the line (CITED)
- **Davenport–Heilbronn** (J. London Math. Soc. 11, 1936, I and II): if Q is a positive integral binary form
  with class number h > 1, Z_Q has infinitely many zeros in σ > 1. The same work gives zeros in σ > 1 for forms
  with a transcendental coefficient ratio, in the diagonal case x² + ty² with t transcendental. Cassels (1961)
  extended Hurwitz's argument to the algebraic irrational case. For a general binary Epstein with algebraic
  irrational ratio it is **not verified** that this is known: it remains a citation gap.
- **Stark** (1967) / **Heegner** / **Baker**: there are exactly 9 fundamental discriminants with h = 1, and 13
  counting orders: −3, −4, −7, −8, −11, −12, −16, −19, −27, −28, −43, −67, −163. At those points τ_D,
  Z_{τ_D} = w·ζ(s)L(s,χ_D) is an Euler product (CITED).
- **Bombieri–Hejhal** (Duke 1995): for linear combinations of Euler products, such as Z_Q with h > 1, almost
  all zeros are on the line, under hypotheses on the component L's (CONDITIONAL). This does not change the fact
  that there are zeros off the line.

### 4.2 From the zero to negativity (ARGUED, same step as O10 / Lemma E)
If Λ_τ has a zero ρ with Re ρ ≠ ½, there exists T with 𝔞_T^{(τ)} not ≥ 0. This is the direction of Weil's
criterion for Λ_τ, applied in the window class: the exhausting class P_T and lem:monoT give monotonicity. The
corpus uses it for Epstein (O10) with label ARGUED in the primitive background and PROVED by certificate at
τ = i√5. Here it remains ARGUED in general.

### 4.3 Proposition 4.1 (CONDITIONAL on 4.2 + the algebraic citation)
One has

  S_∞ ∩ 𝓕 ⊆ {τ_D : D one of the 13 discriminants h = 1} ∪ 𝒜,

where 𝒜 are the τ for which there is no citation of zeros off the line: τ with irrational algebraic data not
covered. Moreover S_∞ ∩ {y > 7.0556 (= 4πe^{−γ}; BIBLIO_CHECK_001 corrects 7.0236)} = ∅ (by 3.3 + 4.2).

**Consistency check (PROVED, arithmetic).** The largest y of a Heegner point is √163/2 = 6.3836 < 7.0556
(= 4πe^{−γ}; BIBLIO_CHECK_001 corrects 7.0236) ✓. No h = 1 point falls in the real-zero zone. This is consistent
and not a coincidence: ζ_K has no real zeros in (½,1) for those K (known numerical verification, CITED
generically). The margin is narrow: 6.38 versus 7.02.

**Answer to (d).** Yes, the "∀T" positivity set is (CONDITIONAL) a finite subset of Heegner points, except for
the gap 𝒜. **The cusp does not belong to S_∞:** positivity at the cusp is for fixed T (L2), and is lost for
y > 7.02. The dichotomy suggested by the question, "cusp vs. CM points," is **not** a sign dichotomy. It is this:
- for fixed T, S_T = (neighborhood of the cusp of height ~e^{2T}) ∪ (compact part);
- as T grows, the cusp neighborhood escapes and the compact part shrinks, toward the τ_D if positivity holds
  there.

Whether the form is positive at the τ_D (including τ = i, ζ·L(χ₋₄)) is **OPEN**. It is the same row-D question
for those L's.

## 5. Why the integrated Maass–Selberg identity does not work (NO-GO, declared retry)

The task suggests ∫_𝓕 𝔞_T^{(τ)} dμ(τ) = "something of ζ(2s)." There are three obstructions.

1. **Non-linearity (PROVED).** 𝔞_T^{(τ)} is linear in the comb Λ_τ, which are the coefficients of −Z_τ′/Z_τ, not
   in E(τ,·). Rankin–Selberg / Maass–Selberg / Zagier compute ∫_𝓕^{reg} E(τ,s) dμ = 0 (Zagier 1981, CITED) and
   products of E. They do not compute ∫ log E. ∫_𝓕 Λ_τ(μ)dμ(τ) has no unfolding expression, because Λ_τ(μ) is a
   polynomial in the multiplicities r_τ(λ), λ | μ, with no Poincaré structure.
2. **Divergence at the cusp (PROVED by L2).** By L2, 𝔞_T^{(τ)} ~ 2log y‖F‖² as y → ∞, and dμ = dx dy/y² makes
   the integral convergent: ∫^∞ log y dy/y² < ∞. But the cusp part is exactly the window form of ζ(2s) on the
   squares. Upon truncating to Maass–Selberg, the main term is that of the index (Front A, "Maass–Selberg =
   window form of ζ(2s) on the squares"). **Retry:** no hypothesis, object or class of methods changes compared
   with the record.
3. **Sign of an average (ARGUED).** By 4.1, almost every τ (Lebesgue measure; in fact every τ with h > 1 and a
   dense set) gives a negative form for large T. An average over 𝓕 of mostly negative forms cannot certify
   positivity at a measure-zero point. Even if ∫𝔞^{(τ)}dμ were a form of ζ(2s), its sign does not transport
   pointwise information to τ_D. It is the geometric version of C-E: the averages see Epstein.

**Verdict §5: NO-GO** (1 PROVED, 2 PROVED + index, 3 ARGUED). It is not recorded as a new route, but as
confirmation of Front A with the additional reason (1).

## 6. The new restriction C-τ

**Proposition 6.1 (PROVED given 4.1-DH and 4.2).** Let τ_D be a Heegner point with h = 1 and U a neighborhood of
τ_D in 𝓕. Suppose a method gives, for every τ ∈ U and every T, a bound 𝔞_T^{(τ)}(F) ≥ B(τ,T)‖F‖² with B
continuous in τ and inf_{τ∈U, T} B(τ,T) ≥ 0. Then the method is false.

*Proof.* The integral forms with h > 1 are dense in ℍ: the imaginary quadratic τ of discriminant with h > 1 are
dense, because almost all discriminants have h > 1 (Heilbronn, CITED). So U contains a τ₁ with h(τ₁) > 1. By DH,
Λ_{τ₁} has zeros in σ > 1. By 4.2 there is a T with 𝔞_T^{(τ₁)} not ≥ 0, which contradicts the bound. ∎
(For τ₁ = i√5 the contradiction is certified, Lemma E.)

**Corollary 6.2 (needles; ARGUED).** Suppose the form is ≥ 0 at τ_D for every T. By Hurwitz, the zeros off the
line of Z_τ, as τ → τ_D, must escape to infinite height, because Z_{τ_D} has none in a compact region. Detecting
them requires ever longer windows, so T*(τ) → ∞ as τ → τ_D. At the same time T*(τ) < ∞ on a dense set. T* is
u.s.c. with isolated infinite spikes: it is a "needle function."

**Reading of C-τ.**
- Every positivity proof for ζ·L(χ_D) that lives inside the family E(τ,·) must use the **integrality of the
  comb** (𝔐_τ ⊂ ℕ with an Euler product) in a way that is **discontinuous in τ**.
- Neither the FE, the pole, the Γ factor, nor any quantity continuous in τ suffices.
- C-τ refines C-Guo and C-E. C-E forbids surviving the average of two Euler products at a point. C-τ forbids
  surviving on a neighborhood, with bounds uniform in T, because the neighborhood contains Beurling
  deformations with FE (generic τ) and Epsteins with h > 1.

**Question within the question: comb-generic, or does positivity select the integral combs h = 1?**
- **Both, at different levels.**
- The form 𝔞_T^{(τ)} is affine in the comb, and the family shows non-integral combs with FE. Any inequality
  affine in the comb that does not use integrality is comb-generic and fails (C-τ).
- If positivity is true at τ_D, then S_∞ **selects** the integral combs with Euler product. This is CONDITIONAL
  on 4.2 + positivity at τ_D (OPEN).
- That a Beurling falsifier exists **with** FE is new in the corpus:
  - generic τ (ARGUED: zeros off the line by DH/transcendence on a dense set);
  - τ = i√5 (PROVED, certified).

  This closes the gap "the Beurling falsifier (ARGUED in P47) has no FE" in the record.

## 7. Alternatives in degree 2 (point 2 of the question)

- **Hecke Maass forms** (ARGUED, discarded). The spectral parameter r_j is discrete. The factor
  Γ_ℝ(s+ir_j)Γ_ℝ(s−ir_j) depends on r_j, so it is not fixed. There is no continuous family through ζ².
- **Eisenstein series in the spectral parameter.** The L-function of E(z,½+ir) is ζ(s+ir)ζ(s−ir): degree 2,
  Euler, conductor 1, passes through ζ² at r = 0. But its comb 2Λ(n)cos(r log n) is the modulation
  c(u) ↦ c(u)cos(ru), i.e. F ↦ F e^{±irt}. Its form is (PROVED, by the formula) the ζ form evaluated at
  modulated tests, plus the archimedean change ψ(s/2 ± ir/2). It is an **orbit of a symmetry**, not a
  deformation: there is no parameter where the Euler product breaks. No contact with C-θ (ARGUED, NO-GO as a
  deformation family). Moreover the Γ factor varies with r.
- **ζ² with Γ_ℝ(s)².** ζ(s)² is the zeta of the degenerate form xy (square discriminant). Zetas of indefinite
  forms have an FE with Γ_ℝ(s)² only for coefficients in a real quadratic field (Hecke; units). For generic
  ratios no FE is known (Siegel; ARGUED, citation to verify). So a continuous family with Γ_ℝ(s)² through ζ²
  appears not to exist beyond the modulations (ARGUED).

  **ζ² is not in the family E(τ,·)**, which has Γ_ℝ(s)Γ_ℝ(s+1). The h = 1 points of E(τ,·) are ζ·L(χ_D) with χ_D
  odd. Within degree 2, the natural family with fixed Γ passes through ζ·L(χ_D), not through ζ².
- Prop 2.1 of SPEC_004 (isolation of ζ in degree 1) has an analogue here. **ζ·L(χ_D) is not isolated as a
  function with FE of degree 2 with factor Γ_ℝ(s)Γ_ℝ(s+1)**: it lies in the continuous family E(τ,·). **It is
  isolated as an Euler product:** the family leaves the Euler products at every τ ≠ τ_D (Prop 4.1 via DH). This
  is CITED/ARGUED, consistent with Kaczorowski–Perelli.

## 8. Candidate theorem, first exact lemma and next step

**Candidate theorem (replaces the Maass–Selberg one, which is a retry).** "Needle geometry":
- (i) S_T is closed, contains a cusp neighborhood of height e^{2T+O(1)} (PROVED: L1, L2).
- (ii) S_∞ ⊆ {τ_D} ∪ 𝒜 and S_∞ ∩ {y > 7.0556 (= 4πe^{−γ}; BIBLIO_CHECK_001 corrects 7.0236)} = ∅
  (CONDITIONAL: 4.2, Bateman–Grosswald citation, gap 𝒜).
- (iii) C-τ (PROVED given DH + 4.2).
- (iv) if τ_D ∈ S_∞, then T*(τ) → ∞ as τ → τ_D (ARGUED).

**First exact lemma: L2**, with the explicit constant c₁. This requires Rosser–Schoenfeld for Σ Λ(n)/n and the
bound on Pol_T on P_T from P47.

**Proposed test (NUMERICAL, only if deemed strictly necessary).** Take T*(τ) on the line τ = it, t ∈ [1, √5]. It
passes through τ = i (ζ·L(χ₋₄)), τ = i√2 (h = 1, ζ·L(χ₋₈)), τ = i√3 (order −12, h = 1) and τ = i√5
(T* ≤ 1.59, Lemma E).
- Prediction of 6.2: spikes at t = 1, √2, √3, and finite, moderate T* between them.
- If T* were large over the whole segment, the needle scale would be wide and C-τ would only act at enormous T.
  That would be useful information for designing classes of methods.

**Actions for the index** (the reader does not write into it; the coordinator records them):
- (a) "Integrated Maass–Selberg of 𝔞^{(τ)}": retry of Front A, with an additional reason (non-linearity).
- (b) "E(τ,·) at the cusp → ζ": NO-GO by L2 (gives ζ(2s)-squares).
- (c) Restriction C-τ (new).
- (d) Discrete Maass / ζ(s±ir) orbit: NO-GO as a deformation.
- (e) Citation of Bateman–Grosswald and the algebraic irrational case of DH/Cassels: to verify.

## References (CITED; those marked † are cited from memory and must be verified before entering P47)
- P. Epstein, Math. Ann. 56 (1903).
- S. Chowla, A. Selberg, PNAS 35 (1949); J. reine angew. Math. 227 (1967).
- H. Davenport, H. Heilbronn, J. London Math. Soc. 11 (1936) 181–185, 307–312.
- J.W.S. Cassels, J. London Math. Soc. 36 (1961)†.
- P.T. Bateman, E. Grosswald, Acta Arith. 9 (1964) 365–373†, constant 7.0556 (= 4πe^{−γ}; BIBLIO_CHECK_001
  corrects 7.0236).
- J. Lagarias, M. Suzuki, J. Number Theory 118 (2006) 98–122†, y* = 4πe^{−γ}.
- H. Ki, Duke/Adv. Math. (2005–2006)†.
- E. Bombieri, D. Hejhal, Duke Math. J. 80 (1995).
- H. Stark, Michigan Math. J. 14 (1967); K. Heegner (1952); A. Baker (1966).
- D. Zagier, "The Rankin–Selberg method for automorphic functions which are not of rapid decay," J. Fac. Sci.
  Tokyo 28 (1981).
- J. Kaczorowski, A. Perelli (classification of degree ≤ 1 / degree 2, via SPEC_SIGN_OBJECT_004).
- Corpus: LEMMA_E_EPSTEIN_001, AUDIT_200_EPSTEIN_001, SPEC_SIGN_OBJECT_004, ROUTES-TRIED-INDEX README
  l.203–208, 227, 529–536.
