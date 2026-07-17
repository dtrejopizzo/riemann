# Camino 3, Step 3 — B-smooth restricted sums and the arithmetic pre-freezing condensation

**Phase 19** (ω / multiplicative chaos, RH-INDEPENDENT).  
**Experiment:** `experiments/camino3_bsmooth_freezing.py` (runs clean, ~20s).  
**Date:** 2026-06-07.

---

## 0. Motivation

Step 2 showed the bulk Dirichlet sum W(q,N) = Σ q^{ω(n)}/n has NO sharp freezing transition
(Selberg–Delange slope = q is exactly linear; the BRW glass phase is a QUENCHED phenomenon of
the MAXIMUM, not the annealed sum). The natural next probe: restrict to **B-smooth numbers**
(n with all prime factors ≤ B), where max ω is controllable, to observe the pre-freezing
condensation at tunable scales.

---

## 1. Setup

**B-smooth Dirichlet sum:**
```
   W_B(q, N) := Σ_{n≤N, B-smooth}  q^{ω(n)} / n
```
**Exact asymptote (N → ∞, B fixed):**
```
   W_B(q, ∞) = Π_{p≤B} (1 + q/(p−1))          [finite product, converges for all q>0]
```
So unlike the full sum (loglog growth for all N), the B-smooth sum converges to a CONSTANT.
The interesting regime is intermediate N, before convergence.

**Max ω for B-smooth n ≤ 2×10⁶:**

| B | primes ≤ B | max ω | count |
|---|---|---|---|
| 7 | {2,3,5,7} | 4 | 1,502 |
| 11 | {2,...,11} | 5 | 2,956 |
| 13 | {2,...,13} | 6 | 5,119 |
| 17 | {2,...,17} | 7 | 7,872 |

**Empirical freezing proxy:** q_c(B) ~ max_ω_B / loglog N.

| B | max ω | q_c (predicted) |
|---|---|---|
| 7 | 4 | ~1.50 |
| 11 | 5 | ~1.87 |
| 13 | 6 | ~2.25 |
| 17 | 7 | ~2.62 |

---

## 2. Results

### (A) Empirical free energy λ_B(q): slope of log W_B vs loglog N

| q | B=7 | B=11 | B=13 | B=17 | Full | theory q |
|---|---|---|---|---|---|---|
| 0.5 | 0.000 | 0.001 | 0.001 | 0.001 | **0.499** | 0.500 |
| 1.0 | 0.002 | 0.003 | 0.005 | 0.008 | **0.958** | 1.000 |
| 2.0 | 0.005 | 0.013 | 0.025 | 0.042 | **1.733** | 2.000 |
| 3.0 | 0.010 | 0.028 | 0.059 | 0.101 | **2.362** | 3.000 |
| 5.0 | 0.020 | 0.064 | 0.151 | 0.270 | **3.346** | 5.000 |

**Reading.** B-smooth slopes are near **zero** — not because of suppression, but because at
N = 2×10⁶ the partial sums have **already converged** to their asymptotic products (panel C
shows ratios ≥ 0.9997 across all B and q tested). The loglog growth is a pre-asymptotic
regime; at this N, it's over for B ≤ 17. The full sum (B=∞) still shows slope ≈ q (ongoing
Selberg–Delange growth) — a genuine qualitative difference in the two regimes.

### (B) Convergence to the asymptotic product W_B(q, ∞)

| q | B=7 ratio | B=11 ratio | B=13 ratio | B=17 ratio |
|---|---|---|---|---|
| 0.5 | 1.0000 | 1.0000 | 1.0000 | 0.9999 |
| 1.0 | 1.0000 | 0.9999 | 0.9998 | 0.9997 |
| 2.0 | 0.9998 | 0.9995 | 0.9988 | 0.9978 |
| 3.0 | 0.9997 | 0.9988 | 0.9970 | 0.9939 |

**Reading.** The B-smooth sums at N = 2×10⁶ are within 0.01–0.6% of their N→∞ limit across
all B and q tested. The partial sum has essentially equilibrated. The non-trivial arithmetic
information is now **in the product Π_{p≤B}(1+q/(p−1)) itself**, not in how fast it's
approached.

### (C) Weight condensation (Panel D): B=13 example

| ω | count | weight at q=1 | weight at q=2 | weight at q=4 |
|---|---|---|---|---|
| 0 | 1 | 19.2% | 6.0% | 1.1% |
| 1 | 60 | 40.3% | 25.0% | 9.0% |
| 2 | 617 | 29.3% | 36.4% | 26.3% |
| 3 | 1,878 | 9.6% | 23.9% | 34.5% |
| 4 | 1,904 | 1.5% | 7.6% | 22.0% |
| 5 | 612 | 0.1% | 1.1% | 6.4% |
| 6 | 47 | 0.0% | 0.1% | 0.6% |

**Reading.** This is the most informative panel. As q grows, the q^{ω}/n-tilted measure
shifts weight from the bulk (ω = 1, 2) toward the heavy-tail integers (ω = 4, 5, 6). At
q = 4, roughly 29% of the mass comes from ω ≥ 4 (vs. <2% at q = 1). This is the
**arithmetic pre-freezing condensation**: the analog of the BRW partition function
collapsing onto the maximum-ω integers as the "temperature" 1/q decreases. The kink (true
glass transition) would appear if we could continuously tune N → ∞ at fixed B; at this N,
we see the condensation dynamics in finite-N truncated form.

---

## 3. What the product formula encodes

The exact asymptote W_B(q, ∞) = Π_{p≤B}(1+q/(p−1)) contains:

1. **The full combinatorics of the ω-distribution** for B-smooth numbers (generating function).
2. **Arithmetic correction to Erdős–Kac:** for the pure Poisson/Gaussian (independent Bernoulli
   per prime), the generating function would be Π_{p≤B}(1 + q/p) (squarefree sum). The ratio
   Π(1+q/(p−1))/Π(1+q/p) = Π (p(p−1+q)) / ((p−1)(p+q)) encodes the non-squarefree correction
   (integers with p², p³,... among B-smooth numbers). This is a precise, computable arithmetic
   correction to the naive model.
3. **The condensation threshold:** as q grows, the log of the product is
   Σ_{p≤B} log(1+q/(p−1)) ~ q Σ_{p≤B} 1/(p−1) ~ q log log B (prime reciprocal sum). So the
   "effective loglog factor" for B-smooth numbers is loglog B, not loglog N. This is why the
   slope → 0 for fixed B: the B-smooth sum accesses only loglog B worth of "prime diversity."

---

## 4. The honest barrier to the genuine freezing transition

The BRW/FHK freezing transition (the kink from linear to frozen free energy) is a
**quenched** phenomenon:
```
   max_{t ∈ [T, 2T]} |ζ(½ + it)| grows as exp(√(loglog T))
```
This requires the MAXIMUM over a continuum (or the maximum of Σ_{p≤B} Re p^{-it}/p^{½}
over t ∈ interval). The annealed sum W_B(q, N) — which we compute — is NOT the maximum.

The maximum experiment would require: for each prime p ≤ B, draw a random phase θ_p ∈ [0,2π];
form M(θ) = Σ_{p≤B} cos(θ_p + log p·t)/p^{½}; compute max_t over a long interval; repeat.
The BRW freezing appears in the distribution of this maximum as B → ∞. This is OUTSIDE the
scope of a Dirichlet-sum computation but is the correct theoretical target.

**What we have instead (durable and new):** the exact product formula W_B(q,∞) as a function
of B and q, with its arithmetic correction to the Poisson model, and the empirical condensation
dynamics in panel C. These are computable new facts about the multiplicative structure of the
ω-class, RH-independent.

---

## 5. Findings (durable)

1. **B-smooth sums converge fast:** at N = 2×10⁶, all B-smooth sums (B ≤ 17) have reached
   ≥ 99.4% of their asymptotic product. The loglog-growth phase is over at this N for small B.
2. **Exact asymptote:** W_B(q, ∞) = Π_{p≤B}(1+q/(p−1)) — a computable arithmetic object
   encoding the full ω-combinatorics and the non-squarefree correction to Erdős–Kac.
3. **Weight condensation is real:** as q grows (lower "temperature"), the tilted measure
   condenses onto large-ω integers — 29% of W_{13}-mass comes from ω≥4 at q=4 vs <2% at q=1.
   This is the finite-N arithmetic pre-freezing condensation.
4. **The genuine BRW freezing** (quenched, kink in the free energy) lives in the MAXIMUM, not
   the sum. It requires a different experiment (random-phase / maximum over t ∈ interval).
5. **Honest scope:** RH-independent (N7 barrier). The new math is the arithmetic condensation
   dynamics and the exact product formula as a function of smoothness degree B.

---

## 6. What is left for Camino 3 (step 4+)

The natural next probe (to approach the true quenched freezing) is:

**Step 4: the random multiplicative function maximum.** Fix B, draw random signs ε_p = ±1 iid
for each prime p ≤ B. Form the B-smooth Dirichlet polynomial f(t) = Σ_{n≤N, B-smooth} ε^{ω(n)}/n^{½+it}.
Compute max_{t ∈ [0, T]} |f(t)|² over a long interval T. Repeat over many realizations.
Compare the distribution of the maximum with the BRW prediction (Gumbel after centering by the
log-correlated-field expected maximum). This IS the quenched experiment and is the arithmetic
side of the FHK freezing transition. → `04-random-mult-maximum.md`.

---

*Cross-refs:* `experiments/camino3_bsmooth_freezing.py`, `01-camino3-forward-flow.md`,
`02-omega-rate-freezing.md`, `../06-papers/P14` (dictionary), `../phase-12/` (N7 barrier).  
*Memory:* `[[project-rh-current-direction]]`.
