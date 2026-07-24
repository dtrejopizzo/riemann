# E78.71 - The radial old-old log drift is exactly the sigma-integral of the safe shell derivative

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.70 reduced the live shell target to the sufficient quadratic barrier

```text
Re Delta ell_N > |wrap Im Delta ell_N|^2.               (RDI-1)
```

The remaining question is where the radial part

```text
a_N(sigma) := Re Delta ell_N(i sigma)                   (RDI-2)
```

comes from in the already certified front.

This note records the exact answer: `a_N` is the sigma-integral of the shell
safe derivative from E77.5g.

## 2. Exact differential identity

Let

```text
ell_N(z) := log(1-theta_N(z)),                          (RDI-3)
Delta ell_N(z) := ell_N(z) - ell_{N+2}(z).             (RDI-4)
```

Along the safe axis `z=i sigma`,

```text
d/dsigma Delta ell_N(i sigma)
 = i Delta ell_N'(i sigma).                             (RDI-5)
```

Taking real parts gives

```text
d/dsigma Re Delta ell_N(i sigma)
 = Re(i Delta ell_N'(i sigma)).                         (RDI-6)
```

But E77.5g defines the shell safe derivative as

```text
SAFEDELTA_N(sigma)
 := 2 Re(i Delta ell_N'(i sigma)).                      (RDI-7)
```

Therefore the exact differential identity is

```text
d/dsigma Re Delta ell_N(i sigma)
 = SAFEDELTA_N(sigma) / 2.                              (RDI-8)
```

Equivalently, for any `sigma_1 < sigma_2`,

```text
Re Delta ell_N(i sigma_2) - Re Delta ell_N(i sigma_1)
 = (1/2) ∫_{sigma_1}^{sigma_2} SAFEDELTA_N(t) dt.       (RDI-9)
```

So the radial shell drift is not an ad hoc scalar. It is exactly the integral
of the certified E77.5g safe shell derivative.

## 3. Consequence

This yields a real reduction:

```text
to prove Re Delta ell_N positive with a quantitative margin,
it is enough to prove:

  (a) a basepoint lower bound for Re Delta ell_N,
  (b) a signed integral control on SAFEDELTA_N.         (RDI-10)
```

In particular, if one proves

```text
SAFEDELTA_N(sigma) <= 0                                  (RDI-11)
```

on the relevant sigma-compact, then `Re Delta ell_N` is monotone decreasing in
`sigma` but remains explicitly controlled by its value at a left endpoint and
the accumulated integral tail.

This is exactly the kind of statement that can plug into the quadratic barrier
from E78.70.

## 4. Probe audit

Using the certified E77.5g rows:

### Zeta

For every audited step `N=8,10,12,14,16,18` and every audited

```text
sigma in {0.55,0.6,0.75,1,1.5,2,3},                     (RDI-12)
```

the shell safe derivative increment is strictly negative:

```text
N= 8:  min = -2.814e-2, max = -5.652e-3
N=10:  min = -1.280e-2, max = -2.504e-3
N=12:  min = -8.670e-3, max = -1.654e-3
N=14:  min = -4.565e-3, max = -8.655e-4
N=16:  min = -3.638e-3, max = -6.823e-4
N=18:  min = -2.245e-3, max = -4.198e-4.               (RDI-13)
```

So on the audited zeta ladder, the radial old-old log drift is strictly
decreasing in `sigma`.

### Planted build

The planted build does not preserve that sign regime:

```text
N= 8:  all positive
N=10:  all positive
N=12:  all positive
N=14:  all negative
N=16:  mixed
N=18:  mixed.                                           (RDI-14)
```

Thus the falsifier loses the radial monotonicity regime already at the exact
safe-derivative level.

## 5. Honest reading

This note does not prove the basepoint lower bound for `Re Delta ell_N`, and it
does not yet close the quadratic barrier. What it does prove is that the radial
part of that barrier is entirely governed by an exact integral law for a
previously certified shell object.

So the next theorem-grade step is now very concrete:

```text
RADIAL-OLD-OLD-DRIFT:
  prove a cofinal lower bound for Re Delta ell_N by combining
  (i) a left-endpoint estimate and
  (ii) a signed integral control of SAFEDELTA_N.         (RDI-15)
```

Together with a wrapped-phase bound, that would imply the quadratic barrier of
E78.70 and hence the shell sign.

## 6. Status

```text
proved:
  d/dsigma Re Delta ell_N = SAFEDELTA_N / 2 exactly;

proved:
  therefore Re Delta ell_N is the sigma-integral of the certified safe shell
  derivative;

observed:
  on the audited zeta ladder SAFEDELTA_N is strictly negative throughout,
  while the planted build does not preserve that sign pattern;

reduced:
  LOGQ-QUADRATIC-BARRIER to a radial integral law plus wrapped-phase control.
```
