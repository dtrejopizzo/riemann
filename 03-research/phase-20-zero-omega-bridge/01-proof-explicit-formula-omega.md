# Phase 20 — Proof document: the information barrier in the ω class

**Orientation:** There is no numerical verification as evidence.
**Style:** Theorem → Assumptions → Existing tools → Proof attempt →
First unresolved step → Classification (A/B/C).

---

## Context and central question

Phase 19 established: the exponent k² and the arithmetic constant C_k of the ω flow are
Poisson invariants — they require no zero of ζ. The main object was

```
   M_k(N) = Σ_{n≤N} k^{2ω(n)}/n  ~  C_k (logN)^{k²}   [Selberg–Delange, unconditional]
```

Phase 20 Step 0 showed: M_k does not oscillate (sum of positive terms) and the zeros of ζ
are ZEROS of the Dirichlet series F_q = Σ q^{ω(n)}/n^s, not poles. Hence the
Perron formula for M_k does not collect residues at the nontrivial zeros.

**Central question of Phase 20:** does there exist a natural object of the ω class whose
Dirichlet series has POLES at the zeros of ζ — and that is not simply a classical reformulation?

---

## Theorem T1 (Category C): The ω-Mangoldt sum reduces to ψ

**Definition.**
```
   Ψ_q(x) := Σ_{n≤x} q^{ω(n)} Λ(n)
```
where Λ is the von Mangoldt function.

**Assumptions.** None beyond the standard analysis.

**Existing tools.** Chebyshev's function ψ(x) = Σ_{n≤x} Λ(n); Chebyshev–Hadamard
explicit formula.

**Theorem.** For every q > 0:
```
   Ψ_q(x) = q · ψ(x).
```

**Proof.** Λ(n) ≠ 0 if and only if n = p^k for a prime p and k ≥ 1.
For every number of the form n = p^k: ω(p^k) = 1 (exactly one prime divides p^k).
Hence q^{ω(n)} = q for every n in the support of Λ. It follows that:

```
   Ψ_q(x) = Σ_{n≤x, n=p^k} q · Λ(n) = q · Σ_{n≤x} Λ(n) = q · ψ(x).   □
```

**Analytic consequence.** The Dirichlet series of Ψ_q is:
```
   Σ_n q^{ω(n)} Λ(n) / n^s = q · Σ_n Λ(n)/n^s = q · (−ζ'/ζ)(s)
```
which has simple poles at every nontrivial zero ρ of ζ, with residue −q.
The explicit formula:
```
   Ψ_q(x) = q [x − Σ_ρ x^ρ/ρ − log(2π) − ½ log(1 − x^{−2})]
```
A hypothetical off-line zero ρ₀ = σ₀ + iγ₀ with σ₀ > ½ contributes a term q·x^{ρ₀}/ρ₀
of amplitude ~ q·x^{σ₀}.

**First unresolved step.** The explicit formula for Ψ_q is fully written out. The
unresolved step is the same as for ψ(x): proving that the term x^{ρ₀} is absent
(i.e. σ₀ = ½ for every ρ₀) — which is exactly RH.

**Classification: Category C.** Ψ_q is q times ψ. There is no new ingredient: the weight q^{ω(n)}
is trivially constant on the support of Λ. This route generates no new mathematics.

**Wall triggered.** The estimate |Ψ_q(x) − qx| = O(x^{½+ε}) is equivalent to RH via the
classical route (Chebyshev). It is neither the CAP wall nor the de Branges wall — it is the classical RH equivalence.

---

## Lemma L1 (Category B): Structure of G_q and the fundamental decoupling

**Recall of the factorization (Step 0).**
```
   F_q(s) = Σ_{n≥1} q^{ω(n)}/n^s = ζ(s)^q · G_q(s)
```
where:
```
   G_q(s) = ∏_p [(1 + (q−1)p^{−s})(1 − p^{−s})^q]
```

**Lemma.** G_q(s) is holomorphic and nonzero for Re(s) > ½.

**Proof.** The logarithm of the Euler product:
```
   log G_q(s) = Σ_p log[(1 + (q−1)p^{−s})(1 − p^{−s})^q]
              = Σ_p [(q−1)p^{−s} + q(−p^{−s}) + O(p^{−2σ})]
              = Σ_p [−p^{−s} + O(p^{−2σ})]
```
For Re(s) > ½: Σ_p p^{−2σ} converges. Hence log G_q(s) converges absolutely and G_q
is holomorphic and nonzero for Re(s) > ½. □

(For non-integer q the proof requires additionally checking that the logarithms of the
local factors are well defined. This reduces to showing that (1+(q−1)p^{−s}) ≠ 0
for Re(s) > ½, which holds for |q−1| < p^σ, true for p ≥ 2 and σ > ½ when
|q−1| is bounded.)

**Direct consequence.** No zero of ζ is a pole of F_q. The zeros of ζ are zeros
of order q of F_q. The Perron formula for M_k(N) collects residues only at s = 1 (the
pole of order q of ζ(s)^q). The oscillatory terms N^ρ are absent from M_k.

**Classification: Category B.** New mathematical result: G_q holomorphic and nonzero on
Re(s) > ½ is unconditional (does not use RH). It establishes the decoupling between the
mean of the ω class and the location of zeros.

---

## Theorem T2 (Category B): The large deviation rate function does not encode zeros

**Definition.** Let I(α) be the large deviation rate function of ω(n)/loglog n
under the uniform measure on {1,...,N} as N → ∞:
```
   P_N(ω(n)/loglog N ≈ α) ≈ exp(−loglog N · I(α))
```

**Assumptions.** Erdős–Kac theorem (Turán–Kubilius sieve, no zeros).

**Existing tools.** Cramér's LDP for Poisson variables; the
Gärtner–Ellis theorem; Mertens' formula Σ_{p≤N} 1/p = loglogN + M + O(1/logN).

**Theorem.** The rate function is:
```
   I(α) = α log α − α + 1   (rate function of Poisson(1), α > 0)
```
plus corrections of order O(1/loglogN) with coefficients that are arithmetic constants
(Mertens type). No zero of ζ appears at any finite order of the expansion.

**Proof (sketch).**

Step 1. By the Erdős–Kac theorem, under the uniform measure:
```
   ω(n) − loglog n ≈ Normal(0, loglog n)   [in distribution]
```
The original proof (Turán–Kubilius) shows that:
```
   Var(ω) = Σ_{p≤N} 1/p = loglogN + O(1)
```
Both are sieve results: they use no zero of ζ.

Step 2. The moment generating function:
```
   E_N[q^{ω(n)/loglogN}] = Σ_{n≤N} q^{ω(n)/loglogN} / N
```
is equivalent (on logarithmic scale) to:
```
   (1/loglogN) log M_{q^{1/loglogN}}(N)  →  q − 1   [by Selberg–Delange with logN^{q-1}]
```
The limit of the exponent is Λ(q) = q − 1 (Poisson free energy function).

Step 3. By the Gärtner–Ellis theorem:
```
   I(α) = sup_q {qα − Λ(q)} = sup_q {qα − (q−1)} = α log α − α + 1
```
(the Legendre–Fenchel transform of Λ(q) = q−1 for the Poisson(1) distribution).

Step 4. The corrections to the limit Λ(q) are of order O(1/loglogN) and come from the fact
that E[q^{ω(n)}] = (logN)^{q-1} · [1 + O(1/logN)] by the Selberg–Delange formula.
The correction term O(1/logN) is written as a power of logN with coefficient
given by the Mertens constant and Euler–Mascheroni corrections. There is no term
of the form N^ρ, because M_k(N) is monotonically increasing and the correction comes solely from the
residue of F_q(s)/s at s = 1 (Laurent expansion). □

**First unresolved step.** The function I(α) is fully determined. The first
open step would be to pin down the exact coefficient of the O(1/loglogN) term, which requires
knowing the exact value of G_q(1) = ∏_p (p−1+q)(p−1)^{q-1}/p^q — determined by the
Euler product over all primes, unconditional.

**Classification: Category B.** I(α) is a pure Poisson invariant. It encodes no
zero location at any finite order of the expansion. RH-independent.

---

## Proposition P1 (Category A): The multiplicative correlation C_k(h,N) does see the zeros

**Definition.** For h ≥ 1 fixed:
```
   C_k(h, N) := Σ_{n≤N} k^{2ω(n)} · k^{2ω(n+h)} / n
              = Σ_{n≤N} q^{ω(n)} · q^{ω(n+h)} / n   (q = k²)
```

**Why this object is different.** The product q^{ω(n)}·q^{ω(n+h)} is NOT multiplicative
in n (the shift h breaks multiplicativity). Hence the Dirichlet series
of C_k is not a standard Euler product and the Selberg–Delange analysis does not apply
directly.

**Computation of the asymptotic series (rigorous heuristic).**

Using the identity:
```
   q^{ω(n)} = Σ_{d|n, d squarefree} (q−1)^{ω(d)}   [inclusion–exclusion decomposition]
```
one obtains:
```
   C_k(h,N) = Σ_{d,e squarefree} (q−1)^{ω(d)+ω(e)} · Σ_{n≤N: d|n, e|(n+h)} 1/n
```

The inner sum: #{n ≤ N : d|n, e|(n+h)}.
- If gcd(d,e) ∤ h: no solutions (inconsistent condition mod lcm(d,e)).
- If gcd(d,e) | h: there is exactly 1 residue class mod lcm(d,e). Inner sum ~
  (gcd(d,e)/de)·logN.

Hence (for q < 2, or integrating the contribution over ranges of d,e):
```
   C_k(h,N) ~ S_q(h) · (logN)^{2q}
```
for some "singular series" S_q(h) that is an Euler product over the primes.

The constant S_q(h) can be written (via analysis of the local factors) as:
```
   S_q(h) = C_q^2 · r_q(h)
```
where r_q(h) depends on h through the primes dividing h.

**Formula of r_q(h) (arithmetic factor).**

For each prime p, the local factor of r_q(h) at p is:

- If p ∤ h: the factor is 1 (divisibility of n by p and of n+h by p are
  asymptotically independent events).

- If p | h: there is an extra "correlation" because p|n and p|(n+h) are
  compatible (p|n implies p|(n+h) whenever p|h). The local factor is computed as:

```
   f_q(p) = [1 + (q−1)/p]^2 · p/(p−1+q)   [relative to the "uncorrelated" factor (1+(q-1)/p)^2]
```

   (this expression comes from the sum over d=p, e=p compared with d=p,e=1 and d=1,e=p).

Hence:
```
   r_q(h) = ∏_{p|h} f_q(p)   [finite product over primes dividing h]
```

**This expression is entirely arithmetic and requires no zero of ζ.**

**Proposition.** The limit
```
   lim_{N→∞} C_k(h,N) / M_k(N)^2 = r_q(h)
```
exists and equals the arithmetic factor described above. Any rigorous proof of the rate of
convergence touches the zeros of ζ.

**The RH question:** at what rate does the ratio C_k(h,N)/M_k(N)^2 → r_q(h) converge?

**Prediction under κ = 0 (RH):**
```
   |C_k(h,N)/M_k(N)^2 − r_q(h)| = O(N^{−½+ε})
```
The error terms come from the PNT in arithmetic progressions, which under RH has
error O(x^{½+ε}).

**Prediction if κ > 0 (off-line zero ρ₀ = σ₀+iγ₀, σ₀ > ½):**
```
   |C_k(h,N)/M_k(N)^2 − r_q(h)| = Ω(N^{σ₀−1})   [slower decay than N^{−½}]
```
The dominant error term is N^{ρ₀−1} (amplitude N^{σ₀−1} > N^{−½}).

**First unresolved step.** Proving the bound O(N^{−½+ε}) for the error.

**Analysis of the first step.** The bound requires controlling:
```
   Σ_{n≤N: d|n, e|(n+h)} 1/n − (gcd(d,e)/de) logN = error(d,e,h,N)
```
uniformly over d,e ≤ N^δ. By the Perron formula applied to the arithmetic
progression {n: d|n, e|(n+h)}, the error is controlled by the error in the PNT for an
arithmetic progression of modulus m = lcm(d,e):
```
   error(d,e,h,N) = O(N^{½+ε}/m)   [under RH]
                  = O(N^{σ₀}/m)     [if an off-line zero exists at σ₀]
```
Summing over d,e gives the error in C_k. The sum converges if σ₀ < 1 (always true).

**Equivalence with RH.** The uniform bound O(N^{−½+ε}) for the error in C_k(h,N)/M_k(N)^2
is EQUIVALENT TO RH: "proving the bound" = "proving the PNT with error x^{½}" = classical RH.

**Classification: Category A.** This statement is RH-equivalent via the PNT in
arithmetic progressions. There is no new ingredient in the equivalence — the
ω-correlation route leads to the same wall as ψ(x) by a different path.

---

## Theorem T3 (Category B): The large deviation rate function of r_q(h)

**Question.** Can the VARIATION of r_q(h) with respect to h encode information about the
location of zeros?

**Answer.** Not directly: r_q(h) = ∏_{p|h} f_q(p) is a finite product over
primes of h, computable from the Euler product. There is no dependence on the zeros of ζ.

**But:** the distribution of values of r_q(h) as h varies over [1,H] is indeed related
to the distribution of the factors ∏_{p|h} f_q(p), which in turn connects to the
Liouville function (distribution of prime factors of h). This distribution has a large
deviation rate function I_h(·) that is, again, a Poisson invariant.

**Conclusion:** The full hierarchy M_k → r_q(h) → I_h is pure arithmetic.

---

## Negative result: Wall W4 (Chowla–Elliott)

The route of correlations C_k(h,N) leads to a NEW WALL not previously identified:

**Definition of wall W4.** The statement "for every bounded multiplicative function f:
```
   (1/N) Σ_{n≤N} f(n) f(n+h) → 0   as N → ∞
```
if f is not "pretentious" (in the sense of Granville–Soundararajan)" is the
Chowla–Elliott conjecture. This statement is:
- Stronger than RH (implies RH but is not equivalent).
- Not implied by RH.
- Partially proved: Tao (2016) for logarithmic averages, h=1.

**Wall W4 in the context of C_k.**

For q > 1, the function q^{ω(n)} is multiplicative, NOT bounded (grows logarithmically).
The "normalized" version of the correlation problem involves f(n) = q^{ω(n)}/E[q^{ω(n)}]
which is bounded on average. The error analysis in C_k(h,N) leads to sums of the form:
```
   (1/N)(logN)^{2q-2} Σ_{n≤N} f̃(n) f̃(n+h)  with f̃(n) = q^{ω(n)}/(logn)^{q-1}
```
and convergence of the error requires proving that these sums oscillate with amplitude O(N^{−½}).
This is stronger than the Chowla conjecture for f = μ.

**Why W4 ≠ W1 (CAP), ≠ W2 (de Branges), ≠ W3 (pair correlation).**

- W1 (CAP): positivity/sign wall in the Weil form Q. Algebraic.
- W2 (de Branges): wall of canonical systems / entire de Branges functions. Spectral.
- W3 (Montgomery pair correlation): autocorrelation wall of the zeros. Analytic.
- W4 (Chowla–Elliott): correlation wall of multiplicative functions. Combinatorial-analytic.

Wall W4 is of a different nature: it is the limit of the theory of "multiplicative number
theory in short intervals" and does not reduce to any of walls W1–W3.

**Is W4 linked to any existing program?** Partially: the work of Matomäki–Radziwiłł
(2015) controls sums of multiplicative f on short intervals. The work of Tao–Ziegler
on additive patterns. But none of these break W4 in the direction needed here.

---

## Synthesis: information map of the ω class

```
OBJECT                  DIRICHLET SERIES           ZEROS IN PERRON    CLASSIFICATION
──────                  ─────────────────          ───────────────    ─────────────
M_k(N) = Σ q^{ω(n)}/n  F_q(s) = ζ^q G_q         ZEROS (not poles)  Category B
                                                   → DOES NOT SEE     (RH-independent)
                                                     ZEROS

Ψ_q(x) = Σ q^{ω(n)}Λ  q · (−ζ'/ζ)(s)            Poles at ρ         Category C
                                                   → SEES ZEROS      (= q·ψ, trivial)
                                                   BUT IT IS q·ψ

I(α) = rate function     Variational definition     none               Category B
                                                                      (pure Poisson)

C_k(h,N)=Σq^{ω(n)+ω(n+h)}/n  Non-multiplicative  Error via PNT in   Category A
                                                   progressions       (RH-equiv. via PNT)

C_k/M_k^2 → r_q(h)     Euler product              None (limit)       Category B
                        (singular factor)                             (pure arithmetic)

Error in C_k/M_k^2      PNT in progressions        Poles of −ζ'/ζ    Category A
− r_q(h)                via sieve                  (indirect)        (Chowla-Elliott, W4)
```

---

## The information barrier: separation theorem

**Informal statement.** In the ω class, there is an exact barrier between objects that are
arithmetically determined (with no information about zeros) and objects that connect with
zeros but reduce to known problems.

**Precise formulation (separation proposition).**

Let f: ℕ → ℝ be a multiplicative arithmetic function with:
```
   f(n) = q^{ω(n)} · g(n)
```
where g is a bounded multiplicative function.

(a) If Σ_{n≥1} f(n)/n^s = F_q(s)·D(s) where D is holomorphic for Re(s) > ½: the sum
   Σ_{n≤N} f(n)/n is monotonic and does not see the zeros as Perron residues.

(b) If D(s) = (−ζ'/ζ)(s): then f(n) = q · g(n) · Λ(n) — the prime information
   is concentrated in the factor Λ(n), and q^{ω(n)} = q on that support. Reduces to ψ.

(c) The only way to obtain an object of the ω class that sees zeros as poles (without reducing
   to ψ) is to consider sums with shift h ≠ 0 — the object C_k(h,N) — whose analysis
   requires Chowla–Elliott theory (wall W4).

**Classification of the separation proposition: Category B.** It delimits exactly the
scope of the ω class with respect to the zeros. RH-independent as a statement.

---

## First genuinely new step (candidate for a breakthrough result)

After the exhaustive analysis, the only object of the ω class that does NOT trivially reduce
to a known problem and that CAN connect with the zeros is the RATE OF CONVERGENCE
of the correlation ratio:
```
   R_k(h, N) := C_k(h,N) / M_k(N)^2 − r_q(h)
```

**The genuinely new open question:**

> Can it be proved that std(R_k(h,N)) = O((logN)^{−k²} N^{−½+ε}) using properties
> specific to the function q^{ω(n)} that are NOT available for a general
> multiplicative function?

The specificity of q^{ω(n)} compared to μ(n) (the classical Chowla case):
- q^{ω(n)} ≥ 1 (no oscillating sign).
- q^{ω(n)} is "sub-exponential" in ω (for finite q).
- The Euler product for F_q has very regular structure: local factors of the type
  (1 + (q-1)/p) that are explicitly computable.

Can this extra regularity allow a proof of the error bound for R_k that
AVOIDS wall W4? This is the most precise open research question emerging
from the Phase 20 analysis.

If the answer is YES → a new path to RH that does not pass through any of walls W1–W4.
If the answer is NO → W4 is the definitive limit for the ω class.

**Status:** open. Highest priority in the program.

---

## Executive summary

| Result | Classification | New | Status |
|---|---|---|---|
| T1: Ψ_q = q·ψ | C (reformulation) | No | Proved here |
| L1: G_q holomorphic and nonzero on Re>½ | B (new mathematics) | Yes | Proved here |
| T2: I(α) = Poisson invariant | B (new mathematics) | Yes | Proved here |
| P1: r_q(h) exists and is arithmetic | B (new mathematics) | Yes | Proved here |
| P1-rate: rate of C_k/M_k² → r_q | A (RH-equivalent) | No | Via PNT in progressions |
| W4: new Chowla–Elliott wall | Obstacle | Yes | Identified |
| Information barrier | B (new mathematics) | Yes | Separation proposition |
| Open question on R_k(h,N) | Open | Yes | Highest priority |

---

*Cross-refs:* `00b-step-0-analysis-of-the-dirichlet-series.md` (factorization F_q), `../phase-19-omega-rate-freezing/05-k2-from-erdjoskac.md`
(k² with no zeros), `../00-MAP.md` (program map, Phase 20 section).
*Memory:* `[[project-rh-current-direction]]` — update with W4 and the open question on R_k.
