# E77.5b - Two-scale SR-LOG-ERR autopsy

**Run:** 2026-07-18.

## 1. Statement

E77.5a showed that zeta `SR-LOG-ERR` decreases with N at fixed
`lambda=6`.  E77.5b asks whether this is already the IDENT limit, or
whether the missing theorem is genuinely two-scale in `L` and `N(L)`.

## 2. Probe

Probe:

```text
E77_5b_two_scale_error_probe.py
```

Command:

```bash
python3 E77_5b_two_scale_error_probe.py
```

Output:

```text
E77_5b_two_scale_error_results.json
```

The probe reads the certified E77.3c/E77.5a JSON artifacts and separates:

```text
fixed lambda=6, N=8..20;
fixed N=18, lambda=6,7,8.
```

## 3. Results

At fixed `lambda=6`, the maximum zeta error decreases:

| N | max SR-LOG-ERR |
|---:|---:|
| 8 | 0.5553 |
| 10 | 0.4942 |
| 12 | 0.4543 |
| 14 | 0.4221 |
| 16 | 0.3976 |
| 18 | 0.3757 |
| 20 | 0.3573 |

The log-error slope versus N is:

```text
c_N = -0.03580.
```

At fixed `N=18`, increasing lambda does not improve the error:

| lambda | max SR-LOG-ERR |
|---:|---:|
| 6 | 0.3716 |
| 7 | 0.3739 |
| 8 | 0.3777 |

The log-error slope versus `log(lambda)` is:

```text
c_L = +0.05655.
```

## 4. Autopsy

The one-scale statement

```text
N -> infinity at fixed L controls IDENT
```

is not the Phase-77 endpoint.  IDENT needs the cofinal regime:

```text
L -> infinity,    N=N(L),    N(L)/L -> infinity.
```

E77.5a measured useful fixed-L section convergence, but E77.5b shows that
holding `N=18` while increasing lambda does not move toward the target.
Thus the live error is not merely the finite section tail at fixed L.  It
is the two-scale finite-section/cell error.

This also explains why bare absolute convergence in `Re(s)>1` is
insufficient: it controls the prime-power tail after the correct cofinal
finite expression is in place, but it does not choose the admissible
`N(L)` rate or control the coupled Schur error uniformly in L.

## 5. Reduced Target

The new smallest endpoint is:

```text
SR-LOG-2SCALE:
For compact K subset (1/2,infinity), prove

    sup_{sigma in K} |E_{L,N(L)}(sigma)| -> 0

with N(L)/L -> infinity and E built from the coupled two-generator
F_b'/F_b expression.
```

The proof must produce an explicit cofinal admissibility condition on
`N(L)`, or identify the finite obstruction term preventing it.

## 6. Next Step

E77.5c:

```text
run a cofinal grid in (lambda,N), not a rectangular one:
lambda in {6,7,8}, N chosen as the largest feasible nested section for
each lambda, plus any feasible N=20/N=22 cores;
fit SR-LOG-ERR against N/L and L;
name the dominant residual term.
```

If the dominant term is the same `MOM-RATIO` package, then E77.3 and E77.5
merge.  If not, the new term becomes the next finite object.

## 7. Status

```text
proved:    no IDENT theorem;
observed:  fixed-lambda N convergence exists in the measured range;
observed:  fixed-N lambda growth does not improve SR-LOG-ERR;
refuted:   one-scale fixed-L section convergence as sufficient for IDENT;
open:      SR-LOG-2SCALE with explicit cofinal N(L);
next:      E77.5c cofinal grid and residual-term naming.
```
