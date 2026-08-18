# E77.7h - Krylov window-resolution audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the bracket problem to:

```text
KRYLOV-WINDOW-RESOLUTION:
prove a deterministic relation between the window scale eta_R and the
Lanczos depth m_R, producing a certified Stieltjes upper bracket for
Sigma_R(eta).
```

This note tests the obvious route: generic interval resolution by Chebyshev
or CG-type estimates on

```text
A_eta=K_R-mu_R+eta.
```

The route fails for zeta.  The live object becomes cyclic pole capture, not
ambient interval approximation.

## 2. Generic interval bound

If

```text
spec(A_eta) subset [a_R(eta),b_R(eta)], 0<a_R<=b_R,
```

then a standard Krylov/CG-style interval estimate pays roughly

```text
q_R=(sqrt(kappa_R)-1)/(sqrt(kappa_R)+1),
kappa_R=b_R/a_R.
```

To reach tolerance `tau`, the depth scale is

```text
m >= log(tau/2)/log(q_R).                     (K-1)
```

This estimate is valid as a generic interval majorant, but it ignores the
cyclic measure `alpha_R`.  It is therefore admissible only if its depth still
keeps `eta_R` compatible with `BRACKETED-LOW-MODE-BTG`.

## 3. Probe

Companion:

```text
E77_7h_krylov_resolution_probe.py
E77_7h_krylov_resolution_results.json
```

Command:

```bash
python3 E77_7h_krylov_resolution_probe.py \
  --lambda 6 --max-modes 18 --refs 14,16 \
  --lanczos-steps 32 --dps 70
```

The probe measures:

```text
a=min(kappa+delta), b=max(kappa+delta), b/a;
Chebyshev step counts from (K-1);
how many exact cyclic poles carry 90 percent of Sigma(delta);
whether 32-step Lanczos Ritz values capture the dominant exact poles.
```

### Zeta

| R | log10(b/a) | Cheb 1e-2 | Cheb 1e-8 | poles for 90% |
|---:|---:|---:|---:|---:|
| 14 | 46.0473 | 2.797e23 | 1.009e24 | 3 |
| 16 | 46.0473 | 2.797e23 | 1.009e24 | 2 |

The generic interval estimate is unusable: it asks for about `10^24` Krylov
steps.  Yet the self-energy is cyclically low-rank in the measured window.
For `R=16`, two exact poles give 90 percent:

```text
kappa ~= 4.9847e-38, fraction .8817;
kappa ~= 3.2190e-43, fraction .0644.
```

The 32-step Lanczos tridiagonal captures those poles at relative kappa
errors about `2.8e-28` and `9.3e-17`, respectively.  This matches the deep
run of E77.7h, where 32 steps recovered `Sigma(delta)` to `~6e-18`.

### Planted build

| R | log10(b/a) | Cheb 1e-2 | Cheb 1e-8 | poles for 90% |
|---:|---:|---:|---:|---:|
| 14 | 2.3968 | 42 | 151 | 3 |
| 16 | 2.3968 | 42 | 151 | 2 |

The planted build has a moderate ambient condition number and is resolved
by very shallow Lanczos in the previous probe.  It stays compatible with the
front-A audit: the algebra does not filter the planted build by sign or by
zeros.

## 4. Autopsy

`KRYLOV-WINDOW-RESOLUTION` is not closed by generic interval estimates.

The failed denominator is:

```text
a_R(delta)=min_l(kappa_l+delta),
```

which is governed by a near-edge complement pole with little cyclic
self-energy relevance.  Chebyshev sees the whole interval `[a,b]`; the proof
needs only the `h_R`-cyclic poles that carry the Stieltjes mass.

Thus the next smaller object is:

```text
CYCLIC-POLE-CAPTURE:
For a cofinal depth m_R, prove that the Lanczos/Ritz poles associated to
the h_R-cyclic Krylov subspace capture the Stieltjes-dominant windows of
alpha_R, with a certified residual tail small enough that
U_R^(m_R)(eta_R) <= eta_R.
```

Then

```text
CYCLIC-POLE-CAPTURE
=> KRYLOV-WINDOW-RESOLUTION
=> LANCZOS-RESOLUTION-ENVELOPE
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.                              (K-2)
```

This is still a cyclic Stieltjes convergence target.  It is not a Weil-sign
claim, not a zero filter, and not a bound on the ambient bordered inverse.

## 5. Status

```text
proved:    generic Chebyshev/CG interval depth formula (K-1);
proved:    CYCLIC-POLE-CAPTURE would imply the chain to BTG-DIV-L (K-2);
refuted:   ambient interval Chebyshev as a usable zeta proof mechanism;
observed:  zeta ambient condition ~10^46 at R=14,16;
observed:  zeta Stieltjes mass is carried by 2--3 cyclic poles;
observed:  32-step Lanczos captures the dominant zeta poles in the finite run;
observed:  planted ambient condition is moderate and shallow Lanczos works;
open:      certified cyclic pole capture with residual tail;
open:      KRYLOV-WINDOW-RESOLUTION, CYCLIC-WINDOW-MASS,
           WFE-CYCLIC-TAIL, RITZ-BRACKET, BRACKETED-LOW-MODE-BTG,
           BTG-DIV-L, corrected LP;
live:      CYCLIC-POLE-CAPTURE.
```

