# R163_102 — The θ = 0 branch: bounded integer error vs the exact lattice

**Status:** (1) PROVED, in a stronger eventual form. (2) PARTIAL: non-lattice systems with bounded error exist (PROVED, with
explicit families). The zero-transfer theorem is PROVED. Whether zeros can lie off the line in general is OPEN. (3) NO-GO
for every perturbative counterexample, meaning any system comparable to ℕ, whether through finitely many or sparse prime
deletions and arbitrary additions. No RH claim. Literature statements: `CITED (secondary source)` per `00-references/beurling-dmv/README.md`.

Notation. B = (P_B, N_B). Π_B = Σ_j Σ_k δ_{p_j^k}/k is the Riemann prime measure and dN_B = exp^*(Π_B) is the integer measure.
ζ_B(s) = ∫ x^{-s} dN_B. R(x) := N_B(x) − ρx. Π_ζ, ζ are the data for ℕ.

---

## 1. Rigidity of the exact lattice (PROVED)

**Theorem R.** Suppose there are X₀ and c ∈ ℤ such that N_B(x) = ⌊x⌋ + c for all x ≥ X₀. Then c = 0, the integer
multiset is ℕ with multiplicity one, and P_B is the set of ordinary primes. In particular N_B(x) − ⌊x⌋ → 0 already
forces B = ℕ, because N_B − ⌊x⌋ is integer-valued, so it tends to 0 only if it is eventually 0.

*Proof.* Take x ≥ X₀. Then N_B jumps only at integers and by exactly 1, so the B-integers in [X₀,∞) are exactly the
ordinary integers there, each with multiplicity 1.

(a) *Every B-integer is an ordinary integer.* Let a be a B-integer. Choose an integer n with n·a ≥ X₀ and n ≥ X₀. Then
n and n+1 are B-integers, so an and a(n+1) are B-integers ≥ X₀, hence ordinary integers. So a = a(n+1) − an ∈ ℤ.
It follows that every B-prime is an integer ≥ 2.

(b) *Large ordinary primes are B-primes of multiplicity 1.* Let r ≥ X₀ be an ordinary prime. It is a B-integer with
multiplicity 1. Every B-factorisation of r uses integers ≥ 2, so the only one is r itself.

(c) *Multiplicities are ≤ 1.* Let n be a B-integer with multiplicity c_n and let r > X₀ be prime. Multiplying each
factorisation of n by r gives c_n distinct factorisations of nr. So c_n ≤ c_{nr} = 1.

(d) *No integer is missing.* Suppose an ordinary integer n is not a B-integer. Take a prime r > X₀·n. In every
factorisation of nr, r divides exactly one B-prime factor, say r·d with d | n. If d = 1 then n would be a B-integer,
so d > 1. Now take an integer m ≥ X₀ with dm ≥ X₀. The B-integer rd·m has two distinct factorisations: {rd} ∪ fact(m) and
{r} ∪ fact(dm). Both dm and m are B-integers because they are ≥ X₀. This contradicts c_{rdm} = 1.

So the B-integers are exactly ℕ with multiplicity 1, which gives c = 0 and ζ_B = ζ as generalized Dirichlet series.
Uniqueness of Laplace–Stieltjes coefficients in σ > 1 gives Π_B = Π_ζ. The primes are then read off one at a time, from the
smallest atom upward: the weight at x minus the known contributions of p^k = x with k ≥ 2 is the multiplicity of x as
a prime. So P_B is the set of ordinary primes. ∎

## 2. Bounded error without the lattice: existence (PROVED)

**Lemma S.** Suppose ζ_B = ζ·A, where A(s) = Σ a_m m^{-s} is a generalized Dirichlet series whose frequencies are real
numbers m ≥ 1 and whose coefficients satisfy Σ|a_m| < ∞. Then N_B(x) = A(1)x + O(1).

*Proof.* N_B(x) = Σ_{m≤x} a_m ⌊x/m⌋ = A(1)x − xΣ_{m>x} a_m/m − Σ_{m≤x} a_m{x/m}. The last two terms are each bounded by
Σ|a_m|. ∎

**Examples.** All of the following have R bounded, and none of them is the lattice.

| system | ζ_B / ζ = A | ρ | zeros of ζ_B in σ > 0 |
|---|---|---|---|
| finite deletion T (drop the primes in T) | Π_T (1 − p^{-s}) | Π_T (1 − 1/p) | exactly those of ζ; the new zeros are on σ = 0 |
| **root substitution**: replace p by p^{1/m} | (1 − p^{-s})/(1 − p^{-s/m}) = Σ_{j<m} p^{-js/m} | Σ_{j<m} p^{-j/m} > 1 | exactly those of ζ; the new zeros are on σ = 0 |
| combinations of the two rows above | products of these factors | products | exactly those of ζ |
| deletion model Λ·1_{n≥5} (a continuous Beurling measure, not discrete) | exp(−2^{-s} − 3^{-s} − 4^{-s}/2), which is entire and zero-free | e^{−23/24} | exactly those of ζ |

Example: P_B = (primes ∖ {2}) ∪ {√2}. Its integers are odd·(√2)^k, ζ_B = ζ(s)(1 + 2^{-s/2}), and N_B(x) = (1 + 2^{-1/2})x + O(1).
A check up to 10⁶ gives sup |R| ≈ 1.95. For finite deletion the error is exactly
Σ_{d|∏T} μ(d)(⌊x/d⌋ − x/d), so |R| ≤ 2^{|T|−1}.

So "N = ρx + O(1)" is **not rigid**. The point where rigidity breaks is precisely the step from "eventually ⌊x⌋ + c" to
"ρx + O(1)".

The case ρ = 1 with a non-lattice system is not realised by these families: none of the products we tried equals 1.
Whether some system achieves it is OPEN, but it is irrelevant for the zeros (see §3).

## 3. Zeros of bounded-error systems

**Lemma B (PROVED).** If |R| ≤ M, then ζ_B(s) = ρs/(s−1) + F(s), where F(s) = s∫₁^∞ R(x)x^{-s-1}dx. F is analytic in σ > 0
and satisfies |F(s)| ≤ M|s|/σ. In particular |ζ_B(σ)| stays bounded as σ → 0⁺ along the reals.

This is the only analytic content of bounded error. It gives analyticity plus a growth bound. It does not give a
functional equation, and it does not locate any zero.

**Theorem T (zero transfer, PROVED).** Let B be any Beurling system, discrete or continuous, with N_B = ρx + O(x^θ), where
θ < 1. Split
Π_B = Π_ζ − τ + q, with τ := (Π_ζ − Π_B)⁺ ≤ Π_ζ and q := (Π_B − Π_ζ)⁺.
Let σ_τ be the abscissa of convergence of ∫x^{-s}dτ, and put σ* := max(σ_τ, θ, 0). Then in σ > σ*, the zeros of ζ_B
coincide with the zeros of ζ, multiplicities included.

*Proof.* In σ > 1 we have ζ_B = ζ·E_q/E_τ, where E_μ := ∫x^{-s} d exp^*(μ). Both of these are Laplace–Stieltjes transforms
of nonnegative measures.

- E_τ converges absolutely for σ > σ_τ and is nonzero there.
- On the real half-line (σ*, ∞), the function ζ_B·E_τ/ζ is analytic. This uses three facts: ζ(σ) < 0 on (0,1); ζ_B is
  analytic for σ > θ; and at s = 1 the simple poles cancel, with residue ρ/1.
- The function ζ_B·E_τ/ζ equals E_q, which has nonnegative coefficients. By Landau's theorem, the abscissa of E_q is ≤ σ*.
- exp^*(q) ≥ q, so ∫x^{-σ}dq ≤ E_q(σ) < ∞. Hence log E_q = ∫x^{-s}dq converges absolutely for σ > σ*, and E_q is zero-free there.

Therefore ζ_B = ζ·(zero-free analytic) in σ > σ*. ∎

**Corollary F (PROVED).** Take T finite, meaning B agrees with ℕ up to deleting finitely many primes and adding an arbitrary
multiset Q, and assume R is bounded. Then:

(i) Q is finite and |Q| ≤ |T|. The reason: as σ → 0⁺, ζ_B(σ) = O(1) by Lemma B, ζ(σ) → −1/2, and
Π_T(1 − p^{-σ}) ≍ σ^{|T|}. Any finite Q′ ⊂ Q contributes a factor ≥ Π_{Q′}(σ log q)^{-1}.

(ii) The zeros of ζ_B in σ > 0 are exactly the zeros of ζ. Hence RH_B ⟺ RH, and every such system has infinitely many zeros
on σ = ½.

Not every Q with |Q| ≤ |T| gives bounded error. Example: T = {2}, Q = {4} gives A = 1/(1 + 2^{-s}), with poles on σ = 0.
At x = 4^K·4/3 one finds R = K/3 + O(1), confirmed numerically up to K = 25. So the error grows like log x.

## 4. Consequence for (BF_0): where a counterexample would have to live

(a) **No perturbative counterexample.** By Theorem T, a bounded-error system with a zero at σ > ½ must satisfy one of
two conditions. Either σ_τ > ½, meaning B deletes a set of ordinary primes whose Dirichlet series diverges beyond ½; this
forces the integers far from ℕ and makes the system essentially non-comparable to ℕ. Or RH is false. Every system obtained
by perturbing the primes of ℕ with sparse deletions (σ_τ ≤ ½) and arbitrary additions has, if its error is O(x^{½}), the
same zeros as ζ in σ > ½.

(b) **The class statement is at least as hard as RH.** "R = O(1) ⇒ RH_B for every B" contains ℕ, so it implies RH. By
Corollary F, its ℕ-comparable part is *equivalent* to RH. Bounded error alone does **not** supply an RH-type conclusion
through any argument available here. The only analytic content is Lemma B: analyticity in σ > 0 and |F| ≤ M|s|/σ.
Broucke's density bound N(α,T) ≪ T^{4(1−α)/(3−2α)}(log T)⁹ for α ≥ ½ (2409.10051, eq. 1.4 with θ = 0) is the strongest
known class-uniform statement, and it is a density bound, not a zero-free region.

(c) **Why the known constructions stop at θ > ½.** DMV (θ > ½), Zhang (θ = ½·exp(c(log)^{2/3})) and Broucke–Debruyne–Vindas
all use random discretisation of a continuous system. The discretisation noise has size ≍ √x. Bounded error requires
exact discretisation, which is an arithmetic constraint and not a probabilistic one. No construction in the literature or
in this corpus reaches θ < ½ (2409.10051 §6.2 only states the range as "should be optimal" for θ ≤ ½). A θ = 0
counterexample with an off-line zero is therefore OPEN. By (a), it would require a system whose prime measure differs from
Π_ζ on a set of abscissa > ½, with the integers still kept within O(1) of ρx.

(d) **Precise discontinuity.**

  - N_B = ⌊x⌋ + c eventually ⇒ B = ℕ, which is rigid (Theorem R).
  - N_B = ρx + O(1) ⇒ B ranges over a non-trivial class (§2). Its ℕ-comparable members (σ_τ < ½) have zero set
    Z(ζ) ∩ {σ > 0}, so they are RH-equivalent (Theorem T).
  - The members that are not ℕ-comparable are unconstrained beyond Lemma B.

  So the passage from O(1) to exact ⌊x⌋ changes **the structure** (the class collapses to a point) but **not the zero
  question**. The zero question is already RH-hard on the comparable part of the class, and it is open off that part.

## 5. Falsifiers

- **Epstein zeta** (class number > 1). It has no Euler product, so it is not Beurling. Its lattice count is
  N(x) = (2π/√D)x + O(x^{1/3}) with Ω(x^{1/4}), so the error is not bounded. It has off-line zeros (Davenport–Heilbronn).
  It fails both hypotheses, so it is not a counterexample. It does show that lattice-point regularity without an Euler product
  does not control zeros.
- **Deletion Λ1_{n≥5}.** R = O(1) (Lemma S, since A is entire with Σ|a| ≤ e^{5/2}), and its zeros are those of ζ. This is
  consistent with Theorem T (τ finite, σ_τ = −∞). It is a continuous system: the weight 1/3 at 8 with no atom at 2 means it
  has no discrete prime set.
- **Witt obstruction check.** A = 1 − 2^{-s} − 3^{-s} has a real zero at σ ≈ 0.788 and summable coefficients. But its
  factorisation exponent at 6 is e₆ = −1, which is a forbidden deletion at a composite. So ζ·A is not Beurling. This is
  consistent with Theorem T.
- **T = {2}, Q = {4}.** The error is unbounded (log x). This shows that Lemma B's bound |F| ≤ M|s|/σ does not by itself
  exclude boundary poles; boundedness needs more.

## 6. Open items handed on

- (O102.1) Is there any non-lattice B with N = x + O(1), that is, with ρ = 1?
- (O102.2) (BF_0) restricted to σ_τ > ½: does bounded error plus Π_B ⊥-far from Π_ζ allow a zero with σ > ½? Any
  construction must be exact (non-random).
- (O102.3) Can Theorem T be sharpened to σ* = max(σ_τ, θ) with τ measured only up to multiplicative cancellation? Root
  substitution already shows that τ ≠ 0 and q ≠ 0 can cancel exactly.
