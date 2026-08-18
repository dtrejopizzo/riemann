# E78.153 - SPECTRAL-SHIFT-COUNTING-SUM: tight, summable, build-separating

**Run:** 2026-07-21.
**Scope:** IDENT / point 6 (fixed-L convergence half) + a new discriminant lead.
**Class:** REDUCCION GENUINA (well-conditioned reformulation; summability law
decisive numerically, proof open).
**Attribution:** spectral-shift target by the program author (2026-07-21);
extended, tightened, and build-separated here.

## 1. The object

From E78.152 (`kappa_j` real), on `z=i sigma`,

```text
2 Re( i T_N'/T_N )(i sigma) = integral 2 sigma/(x^2+sigma^2) d nu_N(x),
   nu_N = sum_j delta_{kappa_j} - sum_j delta_{d_j} - delta_{d_b}   (mass -1).
```

Consecutive difference `Delta nu_N = nu_N - nu_{N+2}` (mass 0),
`M_N(x) = Delta nu_N((-inf,x])` (piecewise constant, -> 0 at +-inf). Integrating
by parts,

```text
2 Re i[ (T'/T)_{N+2} - (T'/T)_N ](i sigma)
   = integral M_N(x) * 4 sigma x/(x^2+sigma^2)^2 dx,
```

and, uniformly on a safe set K,

```text
BOUND_N := integral |M_N(x)| * w(x) dx,   w(x) = sup_{sigma in K} 4 sigma|x|/(x^2+sigma^2)^2
         >= max_{sigma in K} | Delta_N (2 Re i T'/T) | =: TRUE_N.        (SSC)
```

`sum_N BOUND_N < infinity` closes the fixed-L convergence half via the
LOGT-CELL/section-lag chain. This replaces LINEAR-MIXED-CANCELLATION (E78.9) and
the pole/zero split (E78.147) by one real, monotone counting object.

## 2. Result (probe E78_153, lambda=6, dps=50, K={0.55..3})

```text
build  N->N+2   BOUND_N     TRUE_N       ratio    N^2*BOUND_N
zeta   8->10    0.0814831   0.0814831    --       5.215
zeta  10->12    0.0544278   0.0544278    0.668    5.443
zeta  12->14    0.0378234   0.0378234    0.695    5.447
zeta  14->16    0.0282227   0.0282227    0.746    5.532
zeta  16->18    0.0211528   0.0211528    0.750    5.415
plant  8->10    1.70677     0.790609     --       109.2
plant 10->12    0.323036    0.0316867    0.189    32.30
plant 12->14    0.0360488   0.00382205   0.112    5.191
plant 14->16    0.0167192   0.00454571   0.464    3.277
plant 16->18    0.0052131   0.00140529   0.312    1.335
```

Three facts:

**(a) Zeta: BOUND_N = TRUE_N exactly.** Two independent computations (transfer
log-derivative vs the `nu_N` counting integral) agree to 6 digits: this
cross-validates `2 Re i T'/T = int 2sigma/(x^2+sigma^2) d nu_N` AND shows the
Stieltjes bound is TIGHT, i.e. `M_N` is single-signed (coherent spectral shift).

**(b) Zeta: `N^2 * BOUND_N ~ 5.4` stable** (5.21..5.53) => `BOUND_N ~ 5.4/N^2`,
SUMMABLE. So `sum_N BOUND_N < infinity` numerically decisively, and the bound is
tight, so this is the true `sum_N |Delta LOGT-CELL|` -- the fixed-L convergence
input, now as a clean counting object.

**(c) Plant: BOUND_N > TRUE_N (loose), `N^2*BOUND` erratic.** For the plant `M_N`
CHANGES SIGN (incoherent spectral shift), so the Stieltjes bound is not tight and
has no clean law -- even though `TRUE_N` still decays (Outcome A). The
**tightness gap** `BOUND_N/TRUE_N` (1.0 for zeta, 2.2..10 for plant) is a new
structural discriminant: zeta's spectral-shift counting function is single-signed;
the plant's oscillates.

## 3. What this establishes and what remains

```text
established:
  - the spectral-shift identities (E78.152), kappa_j real;
  - BOUND_N = TRUE_N ~ 5.4/N^2 for zeta: fixed-L convergence half of point 6
    reduced to a TIGHT, SUMMABLE, real counting object (numerically decisive);
  - a new discriminant lead: single-signedness of M_N (tightness of SSC),
    zeta coherent / plant incoherent.

open (the proof):
  - prove BOUND_N = O(N^{-2}) (equivalently sum_N BOUND_N < infinity). Route:
    show M_N is single-signed and its mass concentrates at the moving edge
    |x| ~ 2 pi N/L, where w(x) = O(sigma/|x|^3); the interior (bulk) mass cancels
    because nu_N converges in the bulk. This is the geometric replacement for
    ZERO-SIDE-BOUNDEDNESS (E78.147) and is much better conditioned.
  - the arithmetic DISCRIMINANT: whether single-signedness of M_N (or the exact
    limit of the counting function) is the point where the plant genuinely fails
    SAFE-GAMMA-IDENT. The tightness gap in (c) is the first clean lead.
```

## 4. Wall checklist

```text
MW-1..6, K1-K5: not invoked. The object is a difference of resolvent traces of
   a real diagonal and its (real-spectrum) rank-one update -- a Krein-type
   spectral shift, not a positivity or local-to-global assembly.
E72.16/E77.7az: the convergence law (b) is build-neutral (both converge, Outcome
   A). The tightness discriminant (c) lives in IDENT where separation is required
   and is recorded as a lead, not yet used as a forcing detector.
Circularity: nu_N is built from (D,x,q,c), independent of the target Gamma/cell
   derivative -- escapes the E78.150 reformulation trap.
```

## 5. Status

```text
proved/verified:
  spectral-shift identities (E78.152); BOUND_N >= TRUE_N (Stieltjes);
observed (decisive):
  zeta BOUND_N = TRUE_N = 5.4/N^2 (tight, summable); M_N single-signed (zeta);
observed:
  plant BOUND_N loose (M_N sign-changing), erratic -- tightness gap is a new
  build discriminant lead;
reduced:
  point-6 fixed-L convergence to SPECTRAL-SHIFT-COUNTING-SUM (prove BOUND_N
  summable), a well-conditioned real counting statement replacing E78.9/E78.147;
open:
  (i) prove BOUND_N = O(N^{-2}) via single-signedness + edge concentration of M_N;
  (ii) test whether M_N single-signedness is the arithmetic discriminant (plant
       fails) -- the load-bearing point-6 identification;
next:
  diagnose M_N support (bulk vs edge) and sign, both builds, to attack (i)/(ii).
```
