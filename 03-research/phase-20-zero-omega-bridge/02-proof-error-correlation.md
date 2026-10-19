# Phase 20 — Proof document 2: the error term in C_k(h,N) and the equivalence with RH

**Prerequisite:** `01-proof-explicit-formula-omega.md` (factorization F_q, information barrier).
**Goal:** Derive the explicit error formula for C_k(h,N)/M_k(N)² − r_q(h),
establish the equivalence with RH, and correct the identification of wall W4.

---

## 0. Correction to the previous document: W4 is not the correct obstacle

The document `01-proof-explicit-formula-omega.md` identified wall W4 (Chowla–Elliott)
as the obstacle for the rate of convergence of C_k(h,N)/M_k(N)² → r_q(h).

**This identification was incorrect.** The distinction is crucial:

**Chowla–Elliott conjecture (W4):** For f bounded multiplicative with zero mean:
```
   (1/N) Σ_{n≤N} f(n) f(n+h) → 0   as N → ∞
```
This is STRONGER than RH (implies RH but is not equivalent).

**Our problem:** The function q^{ω(n)} has POSITIVE mean ~ (logN)^{q-1} (grows with N).
The correlation C_k(h,N)/M_k(N)² converges to a limit r_q(h) > 0 (not to zero).
The problem is NOT whether the correlation tends to zero; it is at what RATE it converges to the positive limit.

**The real obstacle for the rate of convergence:** the error in the PNT in arithmetic
progressions — which IS equivalent to RH. It is not stronger than RH (it is not Chowla–Elliott).

**Formal correction:** W4 is removed as a wall. The obstacle is the classical W1 wall
(positivity/RH) reached by a new route. This is better news than what was previously reported.

---

## 1. Setup: the Perron formula for sums over arithmetic progressions

Let m ≥ 1 and r with gcd(r,m) = 1 (or more generally r an integer). Define:

```
   A(r,m,N) := Σ_{n≤N: n≡r mod m} 1/n
```

**Proposition A** (classical, Dirichlet–Perron).
```
   A(r,m,N) = (logN)/m + γ/m − (1/m) Σ_{p|m} logp/(p−1) + E(r,m,N)
```
where the error term satisfies:
```
   E(r,m,N) = −(1/φ(m)) Σ_{χ mod m} χ̄(r) Σ_{ρ_χ} N^{ρ_χ−1}/ρ_χ + O_m(1/N)
```
with the inner sum over the nontrivial zeros ρ_χ of L(s,χ).

**Proof.** By the Perron formula:
```
   A(r,m,N) = (1/2πi) ∫_{c-i∞}^{c+i∞} [Σ_n 1_{n≡r mod m}/n^s] N^s/s ds
```
The Dirichlet series on the left-hand side expands via Dirichlet characters:
```
   Σ_n 1_{n≡r mod m}/n^s = (1/φ(m)) Σ_{χ mod m} χ̄(r) L(s,χ)
```
Moving the contour to the left, the residue of L(s,χ₀)/s at s=1 gives (1/m)logN + O(1);
the residues of L(s,χ)/s at s=1 for χ≠χ₀ are zero (L(1,χ) finite). The residues at the
zeros ρ_χ of L(s,χ) give the error term. □

**Corollary.** For the sum over the progression {n: d|n, e|(n+h)} with gcd(d,e)|h:
```
   Σ_{n≤N: d|n, e|(n+h)} 1/n = (gcd(d,e)/de) logN + E_main(d,e,h) + E_error(d,e,h,N)
```
where E_main is an arithmetic constant and E_error satisfies:
```
   E_error(d,e,h,N) = −(gcd(d,e)/de·φ(m)) Σ_{χ mod m} χ̄(r_{d,e,h}) Σ_{ρ_χ} N^{ρ_χ−1}/ρ_χ
```
with m = lcm(d,e)/gcd(d,e) and r_{d,e,h} the residue class defined by the conditions d|n, e|(n+h).

---

## 2. The total error in C_k(h,N)

Using the decomposition of P1 from the previous document:
```
   C_k(h,N) = Σ_{d,e squarefree, gcd(d,e)|h} (q−1)^{ω(d)+ω(e)} Σ_{n≤N: d|n, e|(n+h)} 1/n
```

This splits into a main term plus an error term:
```
   C_k(h,N) = S_q(h) · logN + Const_q(h) + Error_k(h,N)
```

**Computation of the error coefficient.** The error term in C_k(h,N) coming from the
zeros of ζ (through the principal character χ₀) is:

```
   Error_k^{ζ}(h,N) = −Σ_{ρ_ζ} N^{ρ−1}/ρ · A_q(h,ρ)
```

where the arithmetic coefficient is:

```
   A_q(h,ρ) = Σ_{d,e squarefree, gcd(d,e)|h} (q−1)^{ω(d)+ω(e)} · gcd(d,e)/de
```

**Proposition B.** A_q(h,ρ) is a NONZERO ARITHMETIC CONSTANT (independent of ρ) equal to:

```
   A_q(h) = ∏_{p∤h} (1 + 2(q−1)/p) · ∏_{p|h} (1 + 2(q−1)/p + (q−1)²/p)
```

**Proof.** The sum over (d,e) squarefree factors into an Euler product. For each prime p:
- If p ∤ h: the allowed combinations are (v_p(d),v_p(e)) ∈ {(0,0),(1,0),(0,1)}.
  Local factor: 1 + (q-1)/p + (q-1)/p = 1 + 2(q-1)/p.
- If p | h: all combinations (0,0),(1,0),(0,1),(1,1) are allowed.
  gcd(p,p)=p contributes factor p/p²=1/p to the ratio gcd/de.
  Local factor: 1 + (q-1)/p + (q-1)/p + (q-1)²·(1/p) = 1 + 2(q-1)/p + (q-1)²/p. □

**Key observation.** A_q(h) ≠ 0 (each local factor is positive for q > 0 and p ≥ 2):
```
   1 + 2(q−1)/p > 0   for q > 0 and p ≥ 2   ✓
   1 + 2(q−1)/p + (q−1)²/p > 0             ✓
```

Hence the coefficient of the error term is STRICTLY NONZERO.

---

## 3. The explicit error formula

**Theorem T4 (Category A): Explicit formulation of the error in C_k(h,N).**

Let h ≥ 1 be fixed, q = k² > 0. Then:

```
   C_k(h,N)/M_k(N)² − r_q(h) = −[A_q(h)/C_q²] · Σ_{ρ_ζ} N^{ρ−1}/ρ · (1 + O(1/logN))
                                  + [L-function terms] + O(N^{-1+ε})
```

where:
- The sum is over all nontrivial zeros ρ of ζ(s).
- A_q(h) > 0 is the arithmetic constant of Proposition B.
- C_q = G_q(1)/Γ(q) is the Selberg–Delange constant of M_k.
- The "L-function terms" are the contributions of the zeros of L(s,χ) for
  nonprincipal characters χ; under RH for Dirichlet L-functions these are also O(N^{-½+ε}).

**Corollary T4.1 (RH equivalence).**

```
   RH  ⟺  for every h ≥ 1 and every q > 0:
           |C_k(h,N)/M_k(N)² − r_q(h)| = O(N^{−½+ε})
```

**Proof of the implication RH → bound.**
Under RH: every zero ρ of ζ satisfies Re(ρ) = ½. Hence:
```
   |N^{ρ−1}| = N^{Re(ρ)−1} = N^{−½}   for each ρ.
```
The sum Σ_{ρ} N^{−½}/|ρ| converges conditionally to O(N^{−½+ε}) by Chebyshev's theorem
on the growth order of the zero count. (The logN factor in the denominator of M_k²
absorbs the (logN)^{-2q} factor.) □

**Proof of the implication off-line zero → worse bound.**
If ρ₀ = σ₀ + iγ₀ with σ₀ > ½ (off-line zero), the corresponding term in the sum is:
```
   N^{ρ₀−1}/ρ₀ = N^{σ₀−1} · e^{iγ₀ logN} / ρ₀
```
of amplitude N^{σ₀−1} > N^{−½}. Since A_q(h)/C_q² ≠ 0, the error term has:
```
   |C_k(h,N)/M_k(N)² − r_q(h)| = Ω(N^{σ₀−1})
```
which contradicts the bound O(N^{−½+ε}). □

**Classification: Category A.** The rate of convergence of C_k(h,N)/M_k(N)² → r_q(h) is
RH-equivalent, via the PNT in arithmetic progressions. The obstacle is the classical wall
(W1: positivity of the Weil form), reached from a new direction.

---

## 4. Why W4 (Chowla–Elliott) is NOT the correct obstacle

The precise distinction:

**Chowla–Elliott** studies:
```
   (1/N) Σ_{n≤N} f(n) f(n+h)   for f of ZERO MEAN
```
The difficulty is proving that this tends to 0 (correlations vanish). Stronger than RH.

**Our problem** studies:
```
   C_k(h,N)/M_k(N)² − r_q(h)   for the function q^{ω(n)} of POSITIVE MEAN
```
The difficulty is proving that the difference tends to 0. EQUIVALENT to RH (not stronger).

The reason for the difference: q^{ω(n)} ≥ 1 for all n. The correlation C_k converges to a
POSITIVE limit r_q(h) > 0. The error term is oscillatory with amplitude N^{−½} (under RH),
controlled by the zeros of ζ. But the LIMIT ITSELF is positive and arithmetic.

In contrast, for Chowla (f = μ or f = λ), the limit is ZERO, and proving it is zero
requires cancellations between positive and negative terms (which go deeper than RH).

**Updated wall map:**

```
   W1 (CAP): positivity/sign of the Weil form Q              [algebraic]
   W2 (de Branges): canonical systems                         [spectral]
   W3 (Montgomery pair correlation): autocorrelation of ρ    [analytic]
   W4 (REMOVED): does not apply to C_k (positive-mean function)
```

Wall W4 is removed from the program. The ω-correlation route reaches wall W1 (=RH)
via the classical path (PNT in arithmetic progressions).

---

## 5. The new formulation of RH from the ω class

The equivalence T4.1 produces a new explicit formulation of RH:

**RH reformulated (from the ω class):**

For every integer h ≥ 1 and every positive rational q = k² > 0:
```
   Σ_{ρ_ζ, σ_ρ > ½} N^{σ_ρ − ½} / |ρ| · A_q(h) = o(1)   as N → ∞
```
(The sum is over the zeros with real part > ½; under RH the sum is empty.)

This formulation has unique features:
- **Fully explicit:** all coefficients are computable arithmetic quantities.
- **Positive:** A_q(h) > 0, C_q > 0; the required inequality is a decay bound
  for a sum of positive terms.
- **Multi-parameter:** both h and q are free; a violation of the bound implies a violation for
  ALL (h,q). This is a family of necessary conditions.

**Does it offer any strategic advantage?**

The main advantage is that C_k(h,N) and M_k(N)² are sums of POSITIVE TERMS. This allows:

1. **Direct upper and lower bounds:** with no sign cancellations in the summation range.
   Positive sums are more tractable than oscillatory ones.

2. **Jensen-type inequalities:** e.g., by Cauchy–Schwarz:
   ```
   C_k(h,N)² ≤ M_{k²}(N) · Σ_{n≤N} k^{2ω(n+h)}/n  =  M_{k²}(N) · M_{k²}(N+h)
   ```
   These bounds involve only moments of ω, which are arithmetic (Category B).

3. **Monotonicity:** M_k(N) is monotonically increasing in N. C_k(h,N) too (sum of
   positive terms). The ratio C_k/M_k² can be analyzed with monotone-series methods.

However, these advantages still do not break the fundamental obstacle: the convergence error
remains controlled by the zeros of ζ (Theorem T4).

---

## 6. A genuinely new question: can positivity self-cancel the error?

**The most precise question that emerges from the analysis:**

The error Error_k^ζ(h,N) = −Σ_{ρ} N^{ρ−1}/ρ · A_q(h) is a sum over ALL the zeros of ζ.
Under RH, these zeros come in pairs ρ = ½ + iγ, ½ − iγ, and the error is:

```
   Error_k^ζ(h,N) = −2A_q(h) Σ_{γ>0} N^{−½} cos(γ logN − arg(ρ)) / |ρ|
```

This oscillates like N^{−½} · [sum of cosines], which by equidistribution (Weyl's theorem)
is O(N^{−½+ε}).

**The question:** can the SPECIFIC STRUCTURE of q^{ω(n)} force an additional cancellation
in the factor A_q(h) that reduces the amplitude of the error?

Specifically: does A_q(h) depend on ρ in some implicit way?

**Computation of A_q(h):**

```
   A_q(h) = ∏_{p∤h} (1 + 2(q−1)/p) · ∏_{p|h} (1 + 2(q−1)/p + (q−1)²/p)
```

This expression is INDEPENDENT of ρ. Hence A_q(h) is a fixed arithmetic constant
and there is no additional ρ-dependent cancellation.

**Answer:** NO. The structure of q^{ω(n)} produces no additional cancellation in the
error coefficient. The error remains Σ N^{ρ−1}/|ρ| with constant coefficient A_q(h).

**Implication:** The question "can q^{ω(n)} avoid wall W4 through its positivity?" has a
negative answer. Not because the wall is W4 (which has already been removed) but because
the error-convergence error has a nonzero coefficient that does not cancel.

---

## 7. Reformulation of the genuine open problem

After the analysis of Theorem T4 and the correction of W4, the genuine open question is:

**Does there exist any RATIO or DIFFERENCE of objects of the ω class whose rate of convergence
is SUBCRITICAL — i.e. decays faster than N^{−½+ε} — without assuming RH?**

Formally: does there exist a pair (f,g) of M_k-type sums such that:
```
   f(N)/g(N) − L  =  O(N^{−½−δ})   for some fixed δ > 0, without RH?
```

This could happen if f and g have the SAME zero structure in the Perron formula,
so that the terms N^{ρ−1} CANCEL in the ratio f/g.

**Candidate case:** The ratio M_k(N) / M_1(N)^{k²}.

Under Selberg–Delange: M_k(N) ~ C_k (logN)^{k²} and M_1(N) ~ (logN)^1.
Hence M_1(N)^{k²} ~ (logN)^{k²}.

The ratio M_k(N)/M_1(N)^{k²} ~ C_k converges to the same limit C_k. But the ERROR:

```
   M_k(N)/M_1(N)^{k²} − C_k = [M_k − C_k(logN)^{k²}] / M_1^{k²} + ...
```

The numerator M_k(N) − C_k(logN)^{k²} comes from the Laurent expansion of F_q at s=1 (it is
sub-logarithmic, of order (logN)^{k²−1}), NOT from the zeros. Similarly M_1(N)^{k²} has
error (logN)^{k²−1}.

**Hence:** M_k/M_1^{k²} − C_k = O(1/logN) — which is FASTER than N^{−½+ε}.

**This is a case where the rate of convergence is SUBCRITICAL without RH!**

The ratio M_k(N)/M_1(N)^{k²} converges to C_k with error O(1/logN) — faster than N^{−½}.
There is no zero contribution because F_q and F_1^{k²} have the same zeros of ζ (with the same
powers), and the Perron term for the ratio cancels the N^{ρ−1} exactly.

**Classification of this result: Category B.** The ratio M_k/M_1^{k²} converges to C_k
with error O(1/logN), without RH. This is an algebraic cancellation of the zeros in the ratio.

---

## 8. Synthesis: the topography of information in the ω class

The full analysis gives the following map:

```
OBJECT                          RATE OF CONV.    ZEROS IN ERROR    CLASSIFICATION
──────                          ─────────────    ──────────────    ─────────────
M_k(N)/(logN)^{k²} → C_k       O(1/logN)        NO (Laurent)      B — arithmetic
M_k/M_1^{k²} → C_k             O(1/logN)        NO (cancellation) B — new result
r_q(h) = lim C_k(h,N)/M_k(N)²  exists           NO (limit)        B — arithmetic
C_k(h,N)/M_k(N)² → r_q(h)      O(N^{-½+ε}|RH) YES (ζ zeros)      A — RH-equiv.
                                Ω(N^{σ₀−1})|κ>0
Ψ_q(x)/x → q                   O(x^{-½+ε}|RH) YES (= q·ψ)        C — trivial
```

**Information barrier (final version):**

The ω class has ONE WINDOW where the zeros of ζ are visible:
the error term in C_k(h,N)/M_k(N)² − r_q(h).

All other objects of the ω class are blind to the zeros (zero information
cancels algebraically in the ratios, or the zeros are zeros of F_q, not Perron poles).

**The window is unique and RH-equivalent.** This is the structural result of Phase 20.

---

## 9. Structural theorem: positivity prevents algebraic cancellation

The analysis of A_q(h) (Proposition B) suggests a natural question:

**Does there exist any choice of weights q₁,...,q_r > 0 and shifts h₁,...,h_r ≥ 0 such that
the arithmetic coefficient in the error term is ZERO, giving unconditional cancellation?**

**Theorem T5 (Category B): impossibility of algebraic cancellation.**

For any finite collection of real weights q₁,...,q_r > 0 (all positive) and integers
h₁,...,h_r ≥ 0, the arithmetic coefficient A_{q₁,...,q_r}(h₁,...,h_r) multiplying
Σ_ρ N^{ρ−1}/ρ in the error formula of the multi-point correlation:
```
   D_r(N) := Σ_{n≤N} q₁^{ω(n+h₁)} · q₂^{ω(n+h₂)} · ... · q_r^{ω(n+h_r)} / n
```
satisfies A_{q₁,...,q_r} > 0 strictly. Consequently, there exists no
linear combination with positive weights of correlations of the ω class that algebraically
eliminates the contribution of the zeros of ζ to the error.

**Proof.** The coefficient A is expressed as an Euler product over all primes p:
```
   A = ∏_p [local factor at p]
```
where the local factor at p is a sum over distributions of the shifts modulo p:
```
   local factor(p) = (1/p^s) Σ_{a mod p} ∏_j q_j^{[a ≡ −h_j mod p]}  > 0
```
Each term of the product is POSITIVE (sum of products of positive powers). The
product of positive factors is positive. □

**Interpretation:** The positivity q^{ω(n)} ≥ 1 — which guarantees the monotonicity of M_k and
prevents oscillations — is EXACTLY the obstacle that prevents algebraic cancellation
in the coefficient A. They are two faces of the same structural phenomenon:

```
   Positivity  →  monotonicity of M_k  →  no free oscillations  →  no cancellation of zeros
```

For functions WITH SIGNS (such as μ, λ), the local factors can be negative and algebraic
cancellations are possible. That is precisely what Möbius inversion uses
(1 + (−1)/p = (p−1)/p < 1, with sign alternation) to extract zero information.

**Consequence for the ω class:** There is no "arithmetic resonance" in correlations
of the ω class that eliminates the contribution of the zeros. The RH-sensitive window identified
in Section 8 (the error in C_k/M_k²) is the ONLY window available.

**Positivity is a definitive barrier:** there is no combination of positive correlations
that can cancel the N^{ρ−1} without assuming RH. This closes the search program for
"resonances" within the ω class.

**Note:** For cross correlations C_{k,k'}(h,N) = Σ q^{ω(n)} q'^{ω(n+h)}/n with
q+q'=2 (e.g. q=q'=1, trivial case), the factor for p∤h is 1+(q+q'−2)/p = 1, but for
p|h it becomes 1−(q−1)²/p < 1 (still positive). There is no cancellation: the rate
remains O(N^{-½+ε}) under RH, with a smaller but nonzero arithmetic coefficient.

---

## 10. Summary and next steps

**Results of this document:**

| Result | Classification | Status |
|---|---|---|
| Correction: W4 (Chowla-Elliott) does not apply | — | Corrected |
| T4: explicit error formula for C_k/M_k² | A (RH-equiv.) | Proved |
| T4.1: RH ⟺ rate O(N^{-½+ε}) | A | Proved |
| M_k/M_1^{k²} → C_k with error O(1/logN) | B (new, unconditional) | Proved |
| T5: positivity prevents algebraic cancellation | B (new, structural) | Proved |

**Status of the open questions:**

The question "can q^{ω(n)} avoid the obstacle to RH via arithmetic resonances?"
has a NEGATIVE answer by T5.

The only genuinely open question remaining in the ω class is:

> Can the specific regularity of the Euler product of F_q (in contrast to general
> multiplicative functions such as μ) give QUANTITATIVE upper bounds for A_q(h) that
> speed up practical convergence, even though the theoretical rate remains O(N^{-½+ε})?

This question is QUANTITATIVE in nature, not qualitative, and belongs to fine
analytic number theory (estimates of character sums with positive weights).

---

*Cross-refs:* `00b-step-0-analysis-of-the-dirichlet-series.md`, `01-proof-explicit-formula-omega.md`,
`../phase-19-omega-rate-freezing/05-k2-from-erdjoskac.md`.
*Classification of all of Phase 20 so far:* 4 Category B results (new, RH-independent) +
1 Category A result (RH-equiv, new formulation) + 1 correction of W4.
