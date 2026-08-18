# E77.5c - Cofinal SR-LOG grid

**Run:** 2026-07-18.

## 1. Statement

E77.5b showed that fixed-L section convergence is not enough for IDENT.
E77.5c runs an explicit cofinal grid for the coupled two-generator
`SR-LOG-ERR`:

```text
lambda,N = (6,20), (7,20), (8,20),
plus core (6,22).
```

The question is whether increasing `N/L` moves zeta toward the safe target,
and where the planted falsifier breaks.

## 2. Probe

Probe:

```text
E77_5c_cofinal_sr_log_probe.py
```

Commands:

```bash
python3 E77_5c_cofinal_sr_log_probe.py \
  --pairs 6:20,7:20,8:20 \
  --dps 60

python3 E77_5c_cofinal_sr_log_probe.py \
  --pairs 6:22 \
  --dps 60 \
  --output E77_5c_n22_core_results.json
```

Outputs:

```text
E77_5c_cofinal_sr_log_results.json
E77_5c_n22_core_results.json
```

The sigma window is:

```text
0.55, 0.60, 0.75, 1.0, 1.5, 2.0, 3.0.
```

## 3. Endpoint Table

| build | lambda | N | N/L | max SR-LOG-ERR |
|---|---:|---:|---:|---:|
| zeta | 6 | 20 | 5.581 | 0.3573 |
| plant | 6 | 20 | 5.581 | 50.52 |
| zeta | 7 | 20 | 5.139 | 0.3617 |
| plant | 7 | 20 | 5.139 | 61.93 |
| zeta | 8 | 20 | 4.809 | 0.3621 |
| plant | 8 | 20 | 4.809 | 99.06 |
| zeta | 6 | 22 | 6.139 | 0.3427 |
| plant | 6 | 22 | 6.139 | 50.57 |

At `N=20`, zeta is almost flat across lambda.  At fixed lambda 6,
increasing `N/L` from `5.581` to `6.139` lowers the error from `0.3573` to
`0.3427`.  The plant remains far from the zeta target.

## 4. Reading

The falsifier break is stable:

```text
plant/zeta error separation:
lambda 6, N20:  about 141x
lambda 7, N20:  about 171x
lambda 8, N20:  about 274x
lambda 6, N22:  about 148x
```

Thus the planted build does not pass IDENT.  It passes the exact finite
two-generator algebra but fails the zeta safe target.

For zeta, the dominant residual is not the prime tail alone and not the
two-generator identity.  The identity error is tiny compared with the
target error.  The dominant residual is the finite-section lag:

```text
SECTION-LAG:
the coupled Schur/two-generator expression has not reached its
cofinal limit at the measured N/L.
```

This is consistent with E77.5a: fixed L improves with N.  E77.5c adds that
keeping N fixed while L grows loses that improvement.  The theorem must
therefore prescribe an admissible cofinal growth law for `N(L)`.

## 5. Reduced Target

`SR-LOG-2SCALE` is now reduced to:

```text
SECTION-LAG:
For compact K subset (1/2,infinity), prove an explicit bound

    sup_{sigma in K} |E_{L,N}(sigma)|
      <= A_K(L,N) + B_K(L)

where A_K(L,N)->0 under an explicit condition N/L -> infinity, and
B_K(L)->0 by the coupled Gamma-prime/Euler-safe tail.
```

The measured data suggest that `A_K` is slow and depends primarily on the
cofinal ratio `N/L`.  No evidence supports a closure at fixed `N`.

## 6. Autopsy

The attempted shortcut

```text
N/L around 5 is already enough for IDENT
```

is false on the measured range.  Zeta remains at error about `0.35`.

The attempted shortcut

```text
increase lambda at fixed N=20
```

also fails: the zeta error is essentially flat from lambda 6 to 8.

The finite object has therefore been reduced again: the missing theorem is
not the exact algebra, not the planted falsifier, and not the Euler-safe
tail alone.  It is the cofinal finite-section lag of `F_b'/F_b`.

## 7. Next Step

E77.5d:

```text
estimate SECTION-LAG directly by comparing consecutive N at fixed L
inside the two-generator formula:

    Delta_N(sigma)=E_{L,N+2}(sigma)-E_{L,N}(sigma).

If Delta_N is summable with an explicit envelope, SR-LOG-2SCALE reduces to
the remaining L-tail B_K(L).  If not, name the nonsummable term.
```

This keeps the proof inside the selected Cauchy response and avoids
ambient inverse norms.

## 8. Status

```text
proved:    no IDENT theorem;
observed:  zeta improves when N/L increases from 5.58 to 6.14 at lambda 6;
observed:  zeta does not improve by increasing lambda at fixed N=20;
observed:  planted fails SR-LOG-ERR by 50--99 at N=20;
refuted:   N/L around 5 as sufficient for closure;
open:      SECTION-LAG summability/cofinal bound;
next:      E77.5d consecutive-N lag equation and summability test.
```
