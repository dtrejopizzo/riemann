# E78.157 - Three-way decomposition of the shared consecutive-section difference

**Run:** 2026-07-21.
**Scope:** SHARED-N2-LEMMA (convergence half of points 2, 5, 6). Decomposes the
consecutive-section log-transfer difference into three exact additive pieces and
isolates, with numbers, the single build-dependent piece that carries the whole
remaining analytic gap.
**Class:** REDUCCION GENUINA (exact identity + two rigorous build-neutral bounds)
+ honest refinement of the "clean N^{-2}" narrative (E78.153/156).

## 0. One line

The observable consecutive-section difference `g_{N+2}-g_N` splits EXACTLY into
`ZERO + MESH + BND`. `MESH` and `BND` are RIGOROUSLY `O(sigma/N^2)` and
`O(sigma/N^3)`, build-INDEPENDENT (verified identical for both builds). The whole
remaining gap is the `ZERO` piece = a Poisson sum over the real spectrum of `K_N`;
and -- honest correction -- `ZERO` does NOT decay like a clean `N^{-2}` for either
build (its `N^2`-scaled value keeps rising), so the clean `N^{-2}` of the
observable is carried by the rigorous MESH term, not by the hard piece.

## 1. The exact decomposition

From E78.152 (TR), with `kappa_j` REAL (verified), on `z=i sigma`,

```text
g_N(sigma) := 2 Re( i (log T_N)'(i sigma) )
            = sum_j P(kappa_j,sigma) - sum_j P(d_j,sigma) - P(d_{b,N},sigma),
            P(a,sigma) = 2 sigma/(a^2+sigma^2)   (Poisson kernel, each real atom).
```

Taking the consecutive-section difference `Delta = (section N+2) - (section N)`
gives THREE additive groups, exactly:

```text
ZERO = sum_{kappa in N+2} P(kappa) - sum_{kappa in N} P(kappa)     [spectrum of K_N]
MESH = -( sum_{d in N+2} P(d) - sum_{d in N} P(d) )                [added outer mesh poles]
BND  = -( P(d_{b,N+2}) - P(d_{b,N}) )                              [moving boundary pole]
g_{N+2}-g_N = ZERO + MESH + BND.
```

Probe `E78_157_three_way_decomposition_probe.py` (lambda=6, dps=60) verifies this
against the independent partial-fraction `transfer/transfer_prime`:
`|ZERO+MESH+BND - (g_{N+2}-g_N)_direct| ~ 1e-37..1e-46` at every N, both builds.
Exact.

## 2. MESH and BND are rigorous, build-independent, summable

`MESH` and `BND` involve ONLY the mesh geometry `d_n = 2 pi n/L` and the boundary
index `d_{b,N} = 2 pi N/L`, which depend on `L` alone -- NOT on the build's
residues/matrix. The probe confirms `N^2*MESH` and `N^2*BND` are numerically
IDENTICAL for zeta and plant (e.g. `N^2*MESH(sigma=1)`: -2.3185, -2.3693, -2.4047,
... for BOTH builds).

**MESH (proved).** Going `N -> N+2` only ADDS the outer mesh poles at
`d = +-2 pi N/L, +-2 pi(N+1)/L`; the fixed inner poles are unchanged. The `+-`
symmetry gives, at `z=i sigma`,

```text
P(d,sigma)+P(-d,sigma) = 4 sigma/(d^2+sigma^2),  d = 2 pi k/L, k~N
   => MESH = -4 sigma[ 1/(d_N^2+sigma^2) + 1/(d_{N+1}^2+sigma^2) ]
           <= -4 sigma L^2/(4 pi^2) [1/N^2 + 1/(N+1)^2] = O(sigma/N^2).
```

Exact `O(sigma/N^2)`, build-independent. Numerically `N^2*MESH` CONVERGES to a
constant (`~ -2.50` at sigma=1; increments shrink monotonically
.05,.04,.03,.02,.02,.01,.01,.01 over N=8..24) -- a clean, convergent `N^{-2}`.
This is the dominant term.

**BND (proved).** `d_{b,N}=2 pi N/L`, so

```text
BND = 2 sigma[ 1/(d_{b,N+2}^2+sigma^2) - 1/(d_{b,N}^2+sigma^2) ]  (note sign)
    = -2 sigma (d_{b,N+2}^2 - d_{b,N}^2) / [ (d_{b,N}^2+sigma^2)(d_{b,N+2}^2+sigma^2) ],
      d_{b,N+2}^2-d_{b,N}^2 = O(N), denominator = O(N^4)  =>  BND = O(sigma/N^3).
```

An `O(N^{-3})` term. Numerically `N^3*BND ~ 1.9..2.2` (sigma=1), confirming
`o(N^{-2})`. Build-independent. Summable.

So two of the three components satisfy SHARED-N2-LEMMA rigorously and
build-neutrally. **The entire remaining content is `ZERO`.**

## 3. ZERO is the sole build-dependent piece -- and it is NOT clean N^{-2}

`ZERO = Delta[ sum_j P(kappa_j,sigma) ]` is a Poisson sum over the real spectrum
`{kappa_j}` of `K_N = D + (1/c) x q^T`. It is the ONLY build-dependent term.
Probe `E78_157b_zeroside_exponent_probe.py` (dps=60, N=8..24, sigma=1):

```text
       N=8    10     12     14     16     18     20     22     24
zeta   N^2*ZERO: 0.282 0.312 0.384 0.410 0.490 0.525 0.515 0.662 0.657
plant  N^2*ZERO: -12.0 0.873 1.739 1.443 1.983 1.880 2.140 2.251 2.072
```

- **zeta:** `N^2*ZERO` does NOT converge -- it RISES monotonically-in-trend from
  0.28 to 0.66 over N=8..24 (factor ~2.3 across an N-factor 3). Fit `ZERO ~ N^{-p}`
  gives `p ~ 1.2` (borderline). It is summable (p>1 observed) but decays STRICTLY
  SLOWER than `N^{-2}`.
- **plant:** after an N=8 transient, `N^2*ZERO` wanders around ~2 (0.87..2.25),
  also not converging, same borderline character.

**Honest correction to E78.153/156.** The clean `N^{-2}` law of the observable
(`BOUND_N=TRUE_N~5.4/N^2`, `dprof~1.2/N^2`, `C(sigma)/N^2`) is carried by the
rigorous, build-independent MESH term (`N^2*MESH` converges). The build-dependent
`ZERO` piece is a SLOWER (~`N^{-1.2}`), non-convergent correction. Its fingerprint
is already visible in E78.153's zeta `N^2*BOUND` drifting UP 5.21 -> 5.53 (not
flat) and in E78.147's `C(sigma)` mild upward wander -- both are the zero-side's
sub-`N^{-2}` tail riding on the clean mesh term. So "consecutive differences decay
like a clean `O(N^{-2})`" is TRUE for the observable/total but FALSE for the
build-dependent component in isolation; the observable is `N^{-2}` because MESH
dominates ZERO at these N, not because ZERO is `N^{-2}`.

## 4. Consequence: the sharpened gap

```text
SHARED-N2-LEMMA (as an upper bound |g_{N+2}-g_N| <= C(K)/N^2, summable, both builds)
  <=  |ZERO(sigma)| summable, locally uniform on safe K, both builds,     (GAP-Z)
      where ZERO(sigma) = sum_{kappa in spec K_{N+2}} 2 sigma/(kappa^2+sigma^2)
                        - sum_{kappa in spec K_N}     2 sigma/(kappa^2+sigma^2),
      spec K_N real (E78.152).
```

Everything else (MESH `O(N^{-2})`, BND `O(N^{-3})`) is proved and build-neutral.
GAP-Z is the whole remaining analytic problem, now in its sharpest form: a
Poisson-transform difference of two real spectra (the "difference-of-clouds" of
E78.155, made exact). Two warnings this decomposition establishes:

```text
(W1) One canNOT close GAP-Z by a crude |ZERO| = O(N^{-2}) bound: numerically ZERO
     is slower (~N^{-1.2}) and N^2*ZERO diverges. A proof must extract the true
     borderline rate (or exploit the near-cancellation ZERO against MESH-growth
     that keeps the observable's N^2-constant bounded).
(W2) The Herglotz/interlacing route is already dead (E78.148); and now the
     "clean N^{-2} per piece" hope is also dead for ZERO. What survives is:
     spec K_N is real, and the two clouds spec K_{N+2}, spec K_N converge in a
     scaled sense -- the honest object is the RATE of that convergence.
```

## 5. Wall checklist

```text
MW-1..6, K1-K5: not invoked (resolvent-trace difference, no positivity/assembly).
E72.16/E77.7az: MESH and BND are build-neutral (identical both builds, proved).
   ZERO's build-dependence (zeta rising-but-slower vs plant wandering) is recorded
   as a regularity difference, NOT used as a forcing detector. Convergence claim is
   Outcome A (both builds' observable decays).
Circularity: ZERO/MESH/BND built from (D,x,q,c) via K_N, independent of the target
   Gamma/cell derivative (escapes E78.150).
```

## 6. Status

```text
proved (exact, verified 1e-37): the three-way decomposition g_{N+2}-g_N = ZERO+MESH+BND;
proved (rigorous, build-independent):
   MESH = O(sigma/N^2) (dominant, N^2*MESH -> const ~ -2.50);
   BND  = O(sigma/N^3) (N^3*BND ~ 2);
   => two of the three components satisfy SHARED-N2-LEMMA build-neutrally;
observed (decisive, corrects prior narrative):
   ZERO (Poisson sum over real spec K_N) is the SOLE build-dependent piece and does
   NOT decay like a clean N^{-2}: N^2*ZERO rises (zeta 0.28->0.66; plant wanders ~2),
   borderline p~1.2; the clean N^{-2} observable is carried by MESH, not ZERO;
   this explains the upward drift of N^2*BOUND (5.21->5.53) in E78.153;
reduced:
   SHARED-N2-LEMMA -> GAP-Z: summability of ZERO(sigma), both builds -- a
   Poisson-transform difference of two real K_N-spectra (exact difference-of-clouds);
open:
   GAP-Z, with two established no-go warnings (W1: no crude N^{-2}; W2: no Herglotz,
   no clean-per-piece) -- the honest remaining object is the scaled convergence RATE
   of spec K_N;
next:
   characterize the rate of spec K_{N+2} -> spec K_N (cloud convergence) via the
   rank-one secular equation sum_j q_j x_j/(z-d_j) = -c and the arithmetic decay of
   the residues q_j x_j (route D/B), the only remaining handle on GAP-Z.
```
