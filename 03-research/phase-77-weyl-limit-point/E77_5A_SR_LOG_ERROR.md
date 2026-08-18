# E77.5a - SR-LOG-ERR core probe

**Run:** 2026-07-18.

## 1. Statement

E77.3c reduced the IDENT target to the coupled two-generator safe
logarithmic derivative error:

```text
SR-LOG-ERR:
E_{L,N}(sigma)
= L coth(sigma L/2)
  + 2 Re(i F_b'(i sigma)/F_b(i sigma) - i/(i sigma-d_b))
  - B_ext(sigma)
  - 2 Xi'(1/2+sigma)/Xi(1/2+sigma).
```

E77.5a asks whether the finite data show actual decay of this coupled
error, and whether the planted falsifier breaks at this IDENT link.

## 2. Probe

Probe:

```text
E77_5a_sr_log_error_probe.py
```

Command:

```bash
python3 E77_5a_sr_log_error_probe.py \
  --lambda 6 \
  --max-modes 20 \
  --dps 60
```

Output:

```text
E77_5a_sr_log_error_results.json
```

The sigma set is

```text
0.55, 0.60, 0.75, 1.0, 1.5, 2.0, 3.0.
```

The expression stays coupled through `F_b'/F_b`; no hard prime trace or
ambient inverse norm is used.

## 3. Numerical Results

### Max Error By N

| build | N=8 | N=10 | N=12 | N=14 | N=16 | N=18 | N=20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| zeta | 0.555 | 0.494 | 0.454 | 0.422 | 0.398 | 0.376 | 0.357 |
| planted | 65.86 | 50.66 | 50.27 | 50.36 | 50.40 | 50.47 | 50.52 |

At N=20, zeta errors by sigma are:

| sigma | rel. error |
|---:|---:|
| 0.55 | 0.3510 |
| 0.60 | 0.3510 |
| 0.75 | 0.3512 |
| 1.00 | 0.3515 |
| 1.50 | 0.3524 |
| 2.00 | 0.3537 |
| 3.00 | 0.3573 |

At N=20, planted errors by sigma are:

| sigma | rel. error |
|---:|---:|
| 0.55 | 50.52 |
| 0.60 | 48.47 |
| 0.75 | 42.60 |
| 1.00 | 34.37 |
| 1.50 | 23.51 |
| 2.00 | 17.36 |
| 3.00 | 11.06 |

Log-linear slopes in N:

```text
zeta max error:    c = -0.0358
zeta sigma 0.55:  c = -0.0327
zeta sigma 3.00:  c = -0.0358
plant max error:  c = -0.0143
```

## 4. Verdict

The planted falsifier breaks decisively at IDENT/SR-LOG-ERR.  It satisfies
the exact two-generator algebra but misses the zeta safe target by one to
two orders of magnitude across the safe sigma window.

The zeta build shows slow, coherent decay of SR-LOG-ERR from `0.555` to
`0.357` over N=8..20.  The decay is nearly uniform over the tested sigma
range.  This supports the IDENT route, but it is far from a theorem and far
from numerical closure.

## 5. Reduced Target

E77.5a reduces IDENT to the following finite analytic estimate:

```text
SR-LOG-RATE:
For sigma in compact subsets of (1/2,infinity),

    sup_sigma |E_{L,N}(sigma)| <= eps(L,N),
    eps(L,N) -> 0

with E_{L,N} built from the coupled two-generator formula before any
archimedean/prime separation.
```

The data suggest `eps` may be slow in N at fixed lambda.  Therefore the
next proof attempt must explain the rate from the coupled Gamma-prime/cell
formula, not from raw prime-tail convergence alone.

## 6. Autopsy of the Naive Absolute-Convergence Closure

Absolute convergence of prime powers in `Re(s)>1` controls the infinite
Euler tail after the correct finite expression has been identified.  It
does not by itself control the finite-section two-generator error:

```text
F_b'/F_b still carries the finite Schur solve;
the observed zeta error is O(0.35) at N=20;
the hard prime tail estimate alone would ignore this finite-section term.
```

Thus the naive statement

```text
absolute convergence in Re(s)>1 => SR-LOG-ERR -> 0
```

is incomplete.  The missing object is the finite-section error bound for
the coupled two-generator Schur expression.

## 7. Next Step

Proceed to E77.5b:

```text
derive a finite-section error equation for F_b'/F_b itself;
measure which named term accounts for the remaining zeta error ~0.35;
test the same term on the planted build.
```

If this term is exactly `MOM-RATIO`, the E77.3 route and IDENT merge.  If
not, name the new finite error slot and continue.

## 8. Status

```text
proved:    no IDENT theorem;
observed:  zeta SR-LOG-ERR decays coherently to 0.357 at N=20;
observed:  planted SR-LOG-ERR remains 50.5 at N=20;
refuted:   exact two-generator algebra alone as IDENT closure;
refuted:   bare absolute prime-tail convergence as sufficient without a
           finite-section F_b'/F_b error estimate;
open:      SR-LOG-RATE;
next:      E77.5b finite-section error equation for F_b'/F_b.
```
