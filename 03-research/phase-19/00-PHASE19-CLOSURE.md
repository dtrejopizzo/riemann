# Phase 19 — Closure document

**Date:** 2026-06-07.  
**Status:** CLOSED (5 steps complete, unification written, honest scope established).

---

## What Phase 19 accomplished

Phase 19 ran the **forward flow** (primes→ω(n)→moments→ζ statistics) — the only line in
the program not absorbed by the CAP/de Branges/SURF/pair-correlation wall.

### Durable results (5 steps)

| Step | File | Result |
|---|---|---|
| 1 | `01-camino3-forward-flow.md` | k² Keating–Snaith exponent emerges from ω statistics (Selberg–Delange forward) |
| 2 | `02-omega-rate-freezing.md` | Rate function I_emp(α): narrower than Gaussian; NO bulk freezing (annealed = linear) |
| 3 | `03-bsmooth-freezing.md` | B-smooth sums → exact products; weight condensation quantified |
| 4 | `04-random-mult-maximum.md` | Quenched max: monotone in Σ1/p; pre-asymptotic BRW onset |
| 5 | `05-k2-from-erdjoskac.md` | **k² proven from Erdős–Kac + Poisson MGF, NO ζ zeros. The Poisson proxy S_k has slope k² exactly.** |

### The unification (Steps 1–5 form a single argument)

```
   primes → ω(n) ~ Poisson(loglogn)    [Erdős-Kac / Turán-Kubilius, no zeros]
         ↓
   E[q^ω] ~ (logn)^{q-1}               [Poisson MGF, q=k²]
         ↓
   M_k(N) ~ C_k (logN)^{k²}            [elementary integral; k² FORCED]
         ↓ [FINITE-N GAP = same phenomenon throughout]
   large-deviation saturation of ω: integers with ω≈k²·loglogN absent at finite N
         ↓ [B-smooth: condensation]
   weight shifts to large-ω integers as q↑ [arithmetic pre-freezing]
         ↓ [quenched: field strength]
   random max grows with Σ1/p [log-correlated field onset]
```

The constant C_k = G_q(1)/Γ(q+1) is also prime-theoretic (Euler product G_q(1)=Π_p(p-1+q)(p-1)^{q-1}/p^q). **Neither the exponent k² nor the constant C_k requires any zero of ζ.**

---

## What Phase 19 did NOT accomplish

- **No bridge to the zeros:** I(α), M_k, and C_k are unconditional (Selberg–Delange). They are
  insensitive to the location of individual zeros. The ω forward flow and RH are, so far,
  **separate theories** — the N7 barrier holds throughout.
- **No true BRW freezing:** The quenched glass transition requires N→∞ in restricted sums;
  Steps 3–4 document the pre-asymptotic regime only.
- **No proof of Keating–Snaith:** The k² in M_k is for the Dirichlet sum (arithmetic object),
  not the moments of |ζ(½+it)| on the critical line (analytic object). The connection
  between the two is the open Keating–Snaith conjecture.

---

## The honest assessment (advisor's framing)

**Two separate branches of the program now exist:**

**Branch A (RH):** κ=0. Status: wall identified (CAP/de Branges/SURF/pair correlation);
no new handle. All operator realizations (Hilbert–Pólya, Connes, Burnol, de Branges,
SURF) supply symmetry not positivity. Frozen as "the wall is known."

**Branch B (ω-class multifractal theory):** Forward flow, RH-independent new math.
Phase 19 = 5 complete steps. NOT absorbed by any known wall. The k² exponent is a Poisson
invariant; the rate function and condensation dynamics are new computable objects.

---

## The open frontier identified by Phase 19

> **Does the large-deviation rate function I(α) encode ANY information about the zeros?**

- If NO: Camino 3 = a complete independent theory (genuinely new but separate from RH).
- If YES: a new bridge exists that no known approach uses.

The boundary of what is known:
- The MEAN (slope = k², constant C_k): unconditional, does NOT encode zero locations.
- The FLUCTUATIONS of M_k around its mean: unknown whether sensitive to κ.
- The SHORT-INTERVAL ω statistics: unknown whether sensitive to prime distribution anomalies
  caused by off-line zeros.
- The MULTIPLICATIVE CORRELATIONS between ω(n) and ω(n+h): connect to Goldbach-type sieve;
  potentially sensitive to zero pair-correlation.

**Phase 20 opens this bridge question as an explicit research program.**

---

*Files: experiments/camino3_{omega_moments,rate_freezing,bsmooth_freezing,random_mult_maximum,k2_from_erdjoskac}.py*  
*Documents: 01–05-*.md + this closure.*  
*Memory updated: [[project-rh-current-direction]].*
