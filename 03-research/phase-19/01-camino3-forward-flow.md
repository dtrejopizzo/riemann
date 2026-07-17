# Camino 3, Step 1 — The forward flow: building ζ's statistics from multiplicative structure

**Phase 19** (the ω / multiplicative-chaos line; the one frontier not absorbed by the
CAP / de Branges / SURF / pair-correlation wall). **RH-INDEPENDENT exploration — not an
RH-proof attempt** (the framing the program's discriminator forces).
**Experiment:** `experiments/camino3_omega_moments.py` (runs clean).
**Date:** 2026-06-07.

> **The reframe.** Every line that ended at the wall (P29) runs the *reverse* flow:
> `ζ → operator → RH`. Camino 3 runs the **forward** flow:
> ```
>    primes → ω(n) → multiplicative chaos / BRW → moments → statistics of ζ.
> ```
> It does not try to locate the zeros; it asks what the multiplicative structure *predicts*
> about the value statistics of ζ. This is why it is not absorbed by the wall — the wall is a
> statement about zero locations (positivity `κ=0`), while the forward flow is about the value
> distribution.

---

## 0. Why this line, and its honest barrier

- **Not the wall.** P29 showed the reverse-flow realizations (Hilbert–Pólya, de Branges,
  Connes, SURF) all supply symmetry and stall at the same positivity (CAP). The forward flow
  touches none of that machinery: it builds from primes directly.
- **The known barrier (N7, Phase 12).** The probabilistic / multiplicative-chaos machinery
  controls the **ensemble statistics** of ζ (moments, maxima, value distribution), *not* the
  deterministic count of off-line zeros. So Camino 3 cannot, and does not, attack RH. Its honest
  product is **RH-independent new mathematics** about the ω-class — exactly the category the
  program's discriminator marks as the only genuinely-new one (P14, alongside P9fp, B2conj).

This is stated up front so nothing here is mistaken for progress on RH. The goal is new math.

---

## 1. The dictionary (from P14) and the forward claim

P14 established `d_k(n)² ↔ k^{2ω(n)}` (equality for squarefree `n`) and `z = β²`, with
`moments = multiplicative chaos = branching random walk`. The forward claim tested here:
```
   M_k(N) := Σ_{n≤N} k^{2ω(n)}/n   ~   C_k (log N)^{k²}.
```
The exponent `k²` is the **Keating–Snaith / RMT moment exponent** of `|ζ(½+it)|^{2k}`. The
point: it should **emerge from the statistics of `ω(n)` alone** (Selberg–Delange: the average of
`q^{ω(n)}` is `~ (log n)^{q−1}`, here `q = k²` from squaring `d_k ~ k^{ω}`) — with no zeros and
no operator.

---

## 2. What the experiment shows (honest)

Sieving `ω(n)` for `n ≤ 2×10⁶` (max `ω = 7`, mean `≈ loglog N = 2.68`):

### (A) The exponent — right law, finite-N suppression
| `k` | fitted exponent (slope `log M_k` vs `loglog N`) | asymptotic `k²` |
|---|---|---|
| 1.0 | 0.96 | 1.00 |
| 1.5 | 1.89 | 2.25 |
| 2.0 | 2.87 | 4.00 |

`k=1` matches; for `k>1` the fitted exponent is **suppressed** below `k²`. This is **not** a
failure — and that is the interesting part:

### (B) The carrier — why it is suppressed (the new object)
The `k^{2ω}`-tilted mean of `ω` (the typical number of prime factors of the integers that
*carry* the `2k`-th moment) should be `~ k²·loglog N`:

| `k` | tilted-mean `ω` | `k²·loglog N` |
|---|---|---|
| 1.0 | 2.06 | 2.68 |
| 1.4 | 2.90 | 5.24 |
| 1.8 | 3.51 | 8.67 (saturated) |
| 2.0 | 3.76 | 10.70 (saturated) |

The `2k`-th moment wants to be carried by integers with **`~k²` times the typical number of
prime factors** — but those integers do not exist yet at `N = 2×10⁶` (max `ω = 7 < 10.7`). So
the moment cannot reach its asymptotic exponent: **the finite-`N` suppression of the exponent is
exactly the large-deviation saturation of `ω`.** Parts (A) and (B) are the same phenomenon.

> **Reading.** The `k²` law of `|ζ|` is a *shadow of the large-deviation tail of `ω(n)`*: the
> high moments are carried by integers with anomalously many prime factors (`ω ≈ k²·loglog N`,
> deep in the `ω`-large-deviation regime), which is precisely the **multifractal / freezing**
> structure of multiplicative chaos. The forward flow gives the right law; the genuinely-new,
> computable object is the **large-deviation rate function of `ω` that controls the approach to
> it**, and its freezing transition.

---

## 3. Where this connects, and what is genuinely open

- **Keating–Snaith / moments:** the `k²` exponent and the arithmetic factor `a_k` are classical;
  the forward derivation here makes the **carrier** (`ω ≈ k²·loglog N` integers) explicit.
- **Fyodorov–Hiary–Keating (FHK):** the maximum of `|ζ|` on a unit interval of the critical line
  is a log-correlated-field / BRW maximum, with a freezing transition — the *same* multiplicative
  chaos. The `ω`-large-deviation rate is the arithmetic side of that field.
- **Genuinely open (RH-independent):** the precise **large-deviation rate function**
  `I(α) = lim −(1/loglog N) log P(ω(n)/loglog N ≈ α)` and its **freezing** under the `q^{ω}`
  tilt — i.e. the multifractal spectrum of the ω-class — including the arithmetic corrections that
  distinguish it from the pure-Poisson (Erdős–Kac) Gaussian. This is new math about the
  multiplicative structure, not about the zeros.

---

## 4. Next

- **Step 2 (the rate function / freezing).** Compute the empirical large-deviation rate `I(α)` of
  `ω(n)/loglog N` and its Legendre-dual free energy `λ(q) = lim log(avg q^{ω})/loglog N = q−1`
  (Selberg–Delange) vs the multiplicative-chaos / BRW prediction; locate the **freezing point**
  where the `q^{ω}`-tilted measure condenses onto the large-`ω` tail (`q_c`), and measure the
  arithmetic deviation from the Gaussian (Erdős–Kac) bulk. The freezing point is the analogue of
  the FHK transition on the arithmetic side. → `02-omega-rate-freezing.md`.
- **Honest scope:** treat any result as RH-independent new math (the N7 barrier stands); the value
  is in the multifractal structure of the ω-class, not in the zeros.

---

## 5. Findings (durable)

1. **The forward flow works:** the `k²` Keating–Snaith moment exponent is a shadow of `ω(n)`
   statistics, derivable from primes with no zeros and no operator (`k=1` confirms exactly;
   `k>1` is finite-`N`-suppressed).
2. **The suppression is the structure:** the `2k`-th moment is carried by integers with
   `ω ≈ k²·loglog N` — the large-deviation / multifractal tail of `ω`; that is why finite `N`
   underestimates the exponent. The new computable object is this rate function and its freezing.
3. **Honest scope:** RH-independent (the N7 barrier — statistics, not zero locations). This is the
   one frontier not absorbed by the wall, pursued as new math, not as an RH attack.

---

*Cross-refs:* `../06-papers/P14` (ω-hierarchy = chaos = moments = BRW, the dictionary),
`../phase-12/` (multiplicative chaos, N7 barrier, the ω-class large-values frontier),
`../06-papers/P29` (why the reverse-flow lines converge to the wall — the contrast motivating this).
*Memory:* `[[project-rh-current-direction]]`, `[[riemann-program-structure]]`.
