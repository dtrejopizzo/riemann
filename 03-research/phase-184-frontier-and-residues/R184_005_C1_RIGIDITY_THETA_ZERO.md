# R184_005 — C1: rigidity of discrete Beurling systems with N = ρx + O(1)

Phase 184. Inputs: R166_701 (T1–T6, C1, C2, O166.701.1),
R163_102 (Lemma S, Theorem R, Cor F), R184_001 (Prop 2.1–2.2), `00-references/beurling-dmv/`.

## State

| # | Statement | Label |
|---|---|---|
| L1 | N = ρx + R, \|R\| ≤ C ⟹ ζ_𝒫 holomorphic in Re s > 0 except s = 1, \|ζ_𝒫(s) − ρs/(s−1)\| ≤ C\|s\|/σ; in particular ζ_𝒫(σ) bounded as σ → 0⁺ | PROVED |
| L2 | In the finite Euler class ζ·∏_{q∈Q}(1−q^{−s})^{−1}∏_{p∈T}(1−p^{−s}): O(1) ⟹ #Q ≤ #T (pole order at s = 0) | PROVED (generalizes R166_701 T4) |
| L3 | If ζ_𝒫 = ζ·D with D = Σ_{d∈𝒟} a_d d^{−s}, 𝒟 finite, a_d ∈ ℤ, then N = D(1)x + O(1) | PROVED |
| N1 | The set-theoretic version of the lead ("{n_k} ⊂ finite modification of (1/c)ℕ") | REFUTED (counterexample ℕ ∪ √2·ℕ) |
| N2 | The Diophantine route of the lead (O(1) window around (1/c)ℕ + multiplicative closure) gives no restriction | NO-GO (PROVED) |
| C1(O(1)) | Every system θ = 0 is ζ·E, E a finite Euler modification | **OPEN** (no counterexample; L1–L3 + T2–T4 in favor) |
| C1(O(log x)) | same with error O(log x) | **FALSE** (Prop 4.1, PROVED); but the counterexample is RH-equivalent |
| C1(O(x^ε)) | same with O(x^ε) | **FALSE** (Prop 4.1); for ε > ½ there are systems with zeros off the line (DMV, CITED) |
| O166.701.1 | Hilberdink's 2012 classification (Acta Arith. 152) of N − cx periodic | OPEN: the article is not in the corpus (only cited as [21] in `beurling-dmv/2207.00665.txt:175,3464`); not verifiable without web access |

**Verdict.** C1 in the O(1) reading **is not decided**: I neither prove nor refute it. A
necessary analytic condition (L1) is proved, forcing cancellation of the pole at s = 0 (L2), and
the suggested Diophantine route is closed negatively (N1, N2). In the O(log x) and O(x^ε) readings, literal C1 is
**false**, but the constructed counterexample has E holomorphic and zero-free in Re s > 0, so the
equivalence with RH (form T6) survives in that family. There is no claim about RH or about row D.

## 1. Readings of "θ = 0"

R166_701 fixes θ = 0 as N(x) = ρx + O(1) (discrete system: generalized primes p_j > 1 with
multiplicities in ℤ_{≥0}; integers = free commutative monoid, integer multiplicities). I also consider
(b) N = ρx + O(log^A x) and (c) N = ρx + O(x^ε) for every ε > 0.

## 2. Results in the O(1) reading

**L1 (PROVED).** ζ_𝒫(s) = s∫_1^∞ N(x)x^{−s−1}dx = ρs/(s−1) + s∫_1^∞ R(x)x^{−s−1}dx (Re s > 1),
and |∫R x^{−s−1}| ≤ C/σ, holomorphic in σ > 0. Hence ζ_𝒫 continues to Re s > 0 with a single pole (s = 1),
|ζ_𝒫(s) − ρs/(s−1)| ≤ C|s|/σ. At s = σ → 0⁺: |ζ_𝒫(σ)| ≤ C + O(σ), **bounded**. At s = σ + it₀,
t₀ ≠ 0: at most O(1/σ), i.e. the continuation to Re s = 0 admits at most simple-pole-type
singularities at it₀ ≠ 0 and **none** at 0. ∎

This imposes nothing on the zeros in 0 < σ < 1 (as already noted in the task).

**L2 (PROVED).** Let ζ_𝒫 = ζ·∏_{q∈Q}(1−q^{−s})^{−1}∏_{p∈T}(1−p^{−s}) with Q, T finite multisets
(Q: added primes, reals > 1; T: primes of ℕ removed). As σ → 0⁺: ζ(σ) → −½ ≠ 0,
(1−q^{−σ})^{−1} ~ 1/(σ log q), (1−p^{−σ}) ~ σ log p. So ζ_𝒫(σ) ≍ σ^{#T−#Q}; by L1, #Q ≤ #T. ∎
This recovers T4 of R166_701 (Q = {q}, T = ∅) analytically, and shows that "adding" must be
compensated by "removing." It is not sufficient: ℕ ∖ {p} ∪ {q} with log q/log p ∉ ℚ satisfies L1–L2 (pole at 0
cancelled, simple poles at 2πik/log q) and, by the coboundary criterion T3 of R166_701, its R is
Σ_{j ≤ log x/log q} R_{ℕ∖p}(x/q^j), a sum of a mean-zero bounded function over a
log-equidistributed orbit: it is not generically bounded (ARGUED; not disproved here).

**L3 (PROVED).** If ζ_𝒫 = ζ·D, D = Σ_{d∈𝒟} a_d d^{−s} finite, then N_𝒫 = Σ_d a_d ⌊x/d⌋ (Dirichlet
convolution of measures), so N_𝒫 = D(1)x − Σ_d a_d{x/d} = D(1)x + O(Σ|a_d|). ∎
Examples (Lemma S of R163_102): substitution 2 ↦ √2: ζ_𝒫 = ζ(s)(1−2^{−s})/(1−2^{−s/2}) = ζ(s)(1+2^{−s/2}),
N = ⌊x⌋ + ⌊x/√2⌋. In general p ↦ p^{1/m}: D = 1 + p^{−s/m} + … + p^{−(m−1)s/m}, zeros on Re s = 0.
Finite suppression: D = ∏_T(1−p^{−s}), zeros on Re s = 0. In this whole class the zeros of ζ_𝒫 in
Re s > 0 are those of ζ, and C2 restricted to it ⟺ ¬RH (T6, in the already proved direction).

**Refined form of C1 (OPEN).** C1′: "N = ρx + O(1) ⟹ ζ_𝒫/ζ is a finite generalized Dirichlet
polynomial with integer coefficients." C1′ ⟹ C1 and is what L1–L3 suggest. C1 also contains a
nontrivial statement nobody has addressed: that a θ = 0 system be **commensurable with ℕ** (that
ζ_𝒫/ζ even be a reasonable Dirichlet series). There is no argument for or against it.

## 3. The Diophantine route of the lead: NO-GO

**N1 (set-theoretic statement REFUTED).** 𝒜 = ℕ ∪ √2·ℕ (multiplicity 1 except for coincidences,
of which there are none since √2 ∉ ℚ) is a free monoid (L3) with N = (1+1/√2)x + O(1), and is not a
finite modification of (1/c)ℕ, c = 1 + 1/√2: it contains infinitely many points √2·m at nonzero distance
from (1/c)ℤ, with distances that do not vanish. The correct form lives at the level of Dirichlet series (ζ·E), not of sets.

**N2 (NO-GO, PROVED).** (i) "n_k ∈ [(k−C)/c, (k+C)/c]" is automatic for *any* increasing sequence
with N = cx + O(1), without using multiplicativity. (ii) For a ∈ 𝒜, ab ∈ 𝒜 gives
ab ∈ (1/c)ℕ + [−C/c, C/c]; but if C ≥ 1/2 (forced: R jumps by 1 at each generalized integer, so
sup R − inf R ≥ 1 as soon as there are isolated unit jumps, hence C ≥ ½) the window of width 2C/c ≥ 1/c
covers all of ℝ, and the condition is vacuous. The useful multiplicative information is 𝒜 ⊇ a𝒜 with
N(x) − N(x/a) = c(1−1/a)x + O(1), which is exactly the T2/T3 calculation of R166_701; it gives no more than L1–L2.
Any proof of C1 must be global analytic/arithmetic (L1-type + integrality), not about
windows. ∎

## 4. Weaker readings

**Prop 4.1 (PROVED).** Let p_1 < p_2 < … be primes with p_k ≥ 2^{2^k}, S = {p_k}. System 𝒫: primes
of ℕ outside S, plus √p for p ∈ S. Then every generalized integer is written uniquely as
n·d_J, n ∈ ℕ, d_J = ∏_{p∈J}√p, J ⊂ S finite; hence
N(x) = Σ_J ⌊x/d_J⌋, ζ_𝒫 = ζ(s)∏_{p∈S}(1+p^{−s/2}), ρ = ∏(1+p^{−1/2}) < ∞.
Error: N − ρx = −Σ_{d_J ≤ x}{x/d_J} − x Σ_{d_J > x} 1/d_J. The number of J with d_J ≤ x is ≤ 2^{K(x)},
K(x) = #{k : p_k ≤ x²} ≤ log₂log₂ x² , hence ≤ 2 log₂ x + O(1); the tail x Σ_{d_J>x} d_J^{−1} is O(log x)
by the same dispersion (each J with d_J > x has a largest index k, and the sum over the other
factors is bounded by ρ). Thus N = ρx + O(log x). E = ∏_S(1+p^{−s/2})(…) is **infinite**: literal C1
fails in O(log x) and a fortiori in O(x^ε). But ∏(1+p^{−s/2}) converges absolutely in σ > 0
(Σp_k^{−σ/2} < ∞) and its zeros lie on σ = 0; zeros of ζ_𝒫 in the strip = zeros of ζ. ∎
With a less dispersed S (p_k ≥ 2^{k^{1/A}}·…), errors O(log^A x) of the same type are obtained (ARGUED).

**O(x^ε).** DMV (cited in `beurling-dmv/2004.11501.txt:15–19`) construct, for each θ ∈ (½,1), discrete
systems with N = ρx + O(x^θ) and primes with a de la Vallée Poussin-type error (CITED); with θ < ½,
Hilberdink 2005 + Révész Thm 8 give Θ_𝒫 ≥ ½ (R166_701 T1, CITED). Zeros off the line with
N = ρx + O(x^ε), small ε < ½: OPEN (Révész 2207.00665 l.1930–1938 considers it plausible, without proof).

## 5. Consequence

- If C1′ (O(1)) were true, E would be a finite quotient of factors (1−p^{−s})^{±1} with poles
  cancelled (L2), zeros only on Re s = 0, and C2(O(1)) ⟺ ¬RH exactly; the θ = 0 frontier would fall
  into the E1 box (equivalent to RH, with no gain). This is CONDITIONAL on C1′.
- In O(log x): the class is strictly larger (Prop 4.1) but the constructed family remains
  RH-equivalent; existence of an O(log x) system with a zero in Re s > ½: OPEN.
- In O(x^ε), ε ≥ ½+: the DMV systems give zeros off the line (CITED); ε < ½: OPEN.

## For the audit

1. L1 uses only |R| ≤ C and the Mellin formula; verify that N(1⁻) = 0 adds no boundary term.
2. L2: the pole/zero at 0 of each factor is simple; if Q contains repetitions or q = p^{a} coincides with
   factors of T, the count #T − #Q remains the exact order (the factors as s → 0 are independent
   of the arithmetic of q). Check that ζ(0) = −½ is the only input.
3. N2(ii): the argument "C ≥ ½" is coarse; even with small C the lead only gives the closure a𝒜 ⊆ 𝒜,
   already exploited. It is not claimed that *no* Diophantine proof exists, only that the lead does not supply one.
4. Prop 4.1: review the bound on the number of J with d_J ≤ x and on the tail; the double exponential guarantees
   K(x) = O(log log x).
5. Nothing here claims RH, C2, or the closure of D. O166.701.1 (Hilberdink 2012) remains unverified: if that
   article classifies periodic N − cx, C1 might already be resolved in the periodic subclass (e.g.
   ℕ ∪ √2ℕ is **not** periodic: R = −{x} − {x/√2} is almost periodic), which does not cover general O(1).

## Note (R184_092)

* N1 correct: generators {√2,3,5,…}, ζ(1+2^{−s/2}), N=⌊x⌋+⌊x/√2⌋ (name them). L1: the sentence about Re s=0 is not proved; L2 does not use it. L2: T must be a set. Prop 4.1: O(log x) is correct.
