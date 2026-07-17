# Phase 20 — Design document: the zero–ω bridge question

**Date:** 2026-06-07.  
**Status:** OPENED (Phase 19 closed; Rutas A–D identified by advisor post-Phase-19).  
**RH orientation:** DIRECT — the question is whether ω-class statistics can distinguish κ=0 from κ>0.

---

## 0. Strategic context

Phase 19 established that the k² Keating–Snaith exponent — and the arithmetic constant C_k —
are completely determined by the Euler product / Poisson structure of ω, independently of
the zeros. The MEAN of M_k is insensitive to κ.

The advisor's question (post-Phase-19):

> **"¿Qué información sobre los ceros está contenida en la función de tasa de ω(n)?"**

If the answer is "ninguna" → Camino 3 is a complete independent theory (valuable but separate).  
If the answer is "alguna" → a genuinely new bridge exists.

Phase 20 probes this question by looking at objects BEYOND the mean: fluctuations, correlations,
and short-interval statistics of ω.

---

## 1. The four routes (advisor's ranking)

| Route | Name | Core question | Advisor rank |
|---|---|---|---|
| C | Large-deviation rigidity | Does I(α) have arithmetic rigidity that κ>0 violates? | 1 |
| A | ω–zeros incompatibility | Does κ>0 alter the moment exponent in a way ω forbids? | 2 |
| B | k² uniqueness | Is k² the unique moment exponent compatible with multiplicativity? | 3 |
| D | First negative direction | What global law forbids even one off-line zero? | 4 |

**Phase 20 starts with Ruta C** (the advisor's top choice), incorporating elements of A as they arise.

---

## 2. The precise question for Ruta C

**Known (Phase 19, unconditional):** The mean M_k(N) ~ C_k(logN)^{k²} does NOT encode zero locations.

**Unknown:** Do the FLUCTUATIONS of M_k, or the SHORT-INTERVAL statistics of ω, encode zero locations?

Formally:
```
   M_k(N) = C_k(logN)^{k²} + FLUCTUATION(N)
```
The fluctuation = oscillatory part controlled by the explicit formula (through the zeros).

**Hypothesis C (falsifiable):** If κ > 0, the fluctuation of M_k has a DIFFERENT spectrum
(different leading oscillation frequency) than if κ = 0. Specifically:
- κ = 0 → fluctuation driven by on-line zeros γ_ρ (oscillates as N^{iγ_ρ})
- κ > 0 → additional term from off-line zero ρ₀ = σ₀+iγ₀: N^{σ₀+iγ₀} (LARGER amplitude)

The off-line term grows as N^{σ₀} (> N^{½}) while on-line terms grow as N^{½}. So if κ > 0,
the AMPLITUDE of the oscillation of M_k(N)/(logN)^{k²} should grow faster than N^{½-1} = N^{-½}.
This is in principle DETECTABLE from the time series of M_k(N).

**Pre-registered falsifier:** If M_k(N)/(logN)^{k²} oscillates with AMPLITUDE O(N^{-½+ε})
for all ε>0 (consistent with on-line zeros only), then Hypothesis C is unsupported at this
resolution. If the amplitude decays SLOWER than N^{-½}, a signal would be present.

---

## 3. Three concrete experiments for Phase 20

### Experiment 1 (Phase 20, Step 1): Fluctuation analysis of M_k(N)/(logN)^{k²}

Compute the "residual" R_k(N) = M_k(N) / (logN)^{k²} - C_k over many values of N.
Plot R_k(N) vs N; estimate the amplitude of oscillations; check whether the amplitude
decays as N^{-½} (consistent with κ=0) or slower (potential κ>0 signal).

Since we don't KNOW C_k exactly at finite N, this requires careful handling of the
sub-leading terms. The experiment will use: R_k(N) = M_k(N)/M_k(N/e) - e^{k²}
(a ratio that cancels the main growth and isolates oscillations).

→ `experiments/phase20_fluctuation_analysis.py`

### Experiment 2 (Phase 20, Step 2): Short-interval ω statistics

For n in [N, N+H] (short intervals), compute the distribution of ω(n).
- Does it differ from the Poisson(loglog N) bulk?
- If κ > 0, the prime distribution in [N, N+H] is anomalous (error term Ω(H^{σ₀}))
- Does this prime anomaly propagate to ω(n) for n in [N, N+H]?

**The sieve argument:** ω(n) for n ∈ [N, N+H] depends on which primes divide integers
in [N, N+H]. For small primes p << H, the number of multiples of p in [N, N+H] is
~H/p (equidistributed, insensitive to zeros). For large primes p ~ H, the count of
multiples in [N, N+H] is 0 or 1 (a Bernoulli trial, insensitive to zeros). So ω(n)
for n in [N, N+H] is INSENSITIVE to the zero distribution.

Pre-registered verdict: Experiment 2 likely shows NO sensitivity to zeros (ω is a
divisibility statistic, not a prime count statistic). This would close the short-interval
door and focus attention on the global fluctuation (Experiment 1).

→ `experiments/phase20_short_interval_omega.py`

### Experiment 3 (Phase 20, Step 3): Multiplicative correlations

The autocorrelation of k^{2ω}:
```
   C_k(h, N) := Σ_{n≤N} k^{2ω(n)} · k^{2ω(n+h)} / n
```
For h=0 this is M_k(N). For h≠0, this is a Goldbach-type twisted sum.

**Connection to zeros:** Via the Goldbach-like explicit formula, C_k(h,N) has an off-diagonal
oscillation controlled by Σ_ρ N^ρ... (schematically). If κ>0, there are additional off-line
terms growing as N^{σ₀} > N^{½}.

**Prediction:** For fixed h≠0, C_k(h,N)/M_k(N) → r_k(h) as N→∞. The RATE OF CONVERGENCE
(how C_k(h,N)/M_k(N) approaches r_k(h)) is controlled by:
- κ=0: rate ~ N^{-½+ε} (on-line zero oscillations cancel at rate N^{½})  
- κ>0: rate ~ N^{σ₀-1} (> N^{-½}) — slower convergence due to off-line zero

If the convergence rate of C_k(h,N)/M_k(N) can be measured and is N^{-½+ε}, this supports
κ=0 (not proves, but consistent). A SLOWER rate would be a signal.

→ `experiments/phase20_multiplicative_correlations.py`

---

## 4. Pre-registered verdicts and what they mean

| Experiment | Expected result | κ=0 consistent? | κ>0 signal? |
|---|---|---|---|
| 1 (fluctuation amplitude) | Amplitude ~ N^{-½+ε}, decaying | Yes | No (expected negative) |
| 2 (short-interval ω) | Same as bulk Poisson | Yes | No (sieve argument predicts this) |
| 3 (multiplicative correlations) | C_k(h,N)/M_k(N) → r_k(h) at rate N^{-½} | Yes | No (expected negative) |

**If all three give expected negative results:** The ω-class is confirmed as genuinely
independent of zero locations. Phase 20 = a structural negative result (publishable as
"the ω forward flow does not encode zero information"). Camino 3 stands as independent new math.

**If Experiment 1 shows anomalous amplitude:** First new signal in the program connecting
ω-statistics to zeros. Requires immediate verification and careful analysis of the
Perron-formula fluctuation structure.

---

## 5. Ruta D (advisor rank 4, held in reserve)

If Phase 20 Experiments 1–3 all give negative results, the most promising remaining
direction is Ruta D:

> "¿Qué estructura global permite la existencia de la primera dirección negativa?"

This is NOT the Weil form Q. It's asking: is there a global arithmetic law (not yet
identified in the program) such that even ONE off-line zero quartet violates it?

Candidates for the "global law":
- Some rigidity of the Hadamard product ξ(s) = Π(1-s/ρ) under the constraint that the
  product is an entire function of order 1 with specific archimedean symmetry
- A constraint from the functional equation that off-line zeros violate at the level of
  the Taylor coefficients (Jensen/Li coefficients)
- An arithmetic constraint on the DENSITY of zeros near the critical line (zero-density
  theorems + a new Riesz criterion-type inequality)

Ruta D is the most speculative but also the one least similar to anything already tried.

---

## 6. Files

- `00-PHASE20-DESIGN.md` — this document
- `experiments/phase20_fluctuation_analysis.py` — Step 1
- `experiments/phase20_short_interval_omega.py` — Step 2
- `experiments/phase20_multiplicative_correlations.py` — Step 3
- `01-fluctuation-verdict.md` — analysis of Step 1
- `02-short-interval-verdict.md` — analysis of Step 2
- `03-correlations-verdict.md` — analysis of Step 3
- `04-zero-bridge-verdict.md` — synthesis: what Phase 20 found about the zero–ω bridge

---

*Cross-refs:* `../phase-19/00-PHASE19-CLOSURE.md`, `../06-papers/P29` (why the reverse flow
fails), `../06-papers/P14` (ω→chaos dictionary).  
*Memory:* `[[project-rh-current-direction]]`.
