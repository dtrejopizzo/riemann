# E78.56 - On the inward branch, the denominator margin factors as scale times gap

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.54 gave the cone lock

```text
r_N + 2 c_N < 0,                                          (DMF-1)
```

and E78.55 rewrote it on the inward branch `c_N<0` as

```text
r_N < 2 sqrt(1-s_N^2),                                    (DMF-2)
```

where

```text
r_N := |Delta d_N|/|d_N|,
s_N := DIRINC_N.                                          (DMF-3)
```

This note records the final exact factorization of the Euclidean lock margin
through that scalar gap.

## 2. Exact factorization

From E78.54,

```text
EUCLIDEAN-MARGIN_N
 := -2<Delta d_N,d_N> - |Delta d_N|^2
 = |Delta d_N| |d_N| ( -r_N - 2 c_N ).                   (DMF-4)
```

On the inward branch `c_N<0`, E78.55 gives

```text
-c_N = sqrt(1-s_N^2),                                     (DMF-5)
```

so

```text
EUCLIDEAN-MARGIN_N
 = |Delta d_N| |d_N| ( 2 sqrt(1-s_N^2) - r_N ).          (DMF-6)
```

This is exact.

Therefore, on the inward branch,

```text
sign(EUCLIDEAN-MARGIN_N)
 = sign( 2 sqrt(1-s_N^2) - r_N ),                         (DMF-7)
```

because the prefactor `|Delta d_N| |d_N|` is positive.

So the denominator front has now collapsed to a single scalar gap:

```text
GAP_N := 2 sqrt(1-s_N^2) - r_N.                           (DMF-8)
```

## 3. Meaning

This is stronger than the earlier reductions:

- E78.54 identified the cone condition.
- E78.55 merged size and sine into one exact criterion.
- Here we see that the full Euclidean lock margin itself is nothing but:

```text
positive scale  *  scalar gap.                           (DMF-9)
```

So there is no further hidden denominator content inside the modulus front once
the inward branch is fixed.

## 4. Audit

Certified data already available:

```text
E78_54_den_cone_lock_results.json
E78_43_den_directional_increment_results.json
```

On the audited inward rows, the exact factorization `(DMF-6)` holds to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  |Delta d_N| |d_N| = 0.02859940029
  GAP_N             = 1.49421823805
  margin            = 0.04273374584

sigma=3.0, N=12->14:
  |Delta d_N| |d_N| = 0.00460559441
  GAP_N             = 1.61790133149
  margin            = 0.00745139741.                     (DMF-10)
```

So the audited zeta denominator margin is positive for two independent reasons:
the scale is positive and the scalar gap is decisively positive.

### Planted build

The planted build fails first by leaving the inward branch:

```text
sigma=1.0, N=10->12:
  c_N = 0.9420192582 > 0.                                 (DMF-11)
```

On later planted rows that re-enter the branch, the same exact factorization
holds, but the gap alone no longer separates them from zeta.

## 5. Consequence

This yields the tightest denominator endpoint named so far:

```text
DEN-GAP-LOCK:
  prove cofinally that the increment stays on the inward branch and
  GAP_N = 2 sqrt(1-s_N^2) - r_N > 0.                      (DMF-12)
```

Then the whole denominator chain follows:

```text
GAP_N > 0 on inward branch
=> Euclidean lock margin > 0
=> radial contraction
=> modulus subunit law
=> denominator rigidity chain.                            (DMF-13)
```

## 6. Honest reading

This note does not prove the inward branch or the positivity of `GAP_N`
cofinally. What it does prove is that the denominator front is now literally a
single scalar gap once the branch is fixed.

That is the cleanest endpoint of the entire E78 denominator descent.

## 7. Status

```text
proved:
  on the inward branch, the Euclidean lock margin factors exactly as
  |Delta d_N||d_N| times GAP_N = 2 sqrt(1-s_N^2) - r_N;

proved:
  the sign of the full denominator lock is exactly the sign of GAP_N on that
  branch;

observed:
  audited zeta rows have large positive GAP_N;

observed:
  the planted build fails first by leaving the inward branch;

reduced:
  the entire denominator front to DEN-GAP-LOCK on the inward branch;

next:
  isolate a finite shell law forcing the inward branch, or prove a cofinal
  lower bound for GAP_N directly from the shell dynamics.
```
