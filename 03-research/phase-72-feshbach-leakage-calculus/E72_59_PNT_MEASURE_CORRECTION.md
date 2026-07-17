# E72.59 -- PNT measure correction for endpoint operators

**Date:** 2026-07-08.
**Role:** correct the continuous endpoint operator normalization in E72.46/E72.47.

## 0. The mistake

For the prime-weighted operator:

```text
sum_{n<=x} Lambda(n)(n/x)^z n^(-1/2)Q(log n),
```

the PNT main term is:

```text
int_1^x (u/x)^z u^(-1/2)Q(log u) du,
```

because:

```text
dPsi(u) ~ du.
```

With `u=e^y`, `du=e^y dy`, so the continuous main is:

```text
int_0^L exp(z(y-L)) exp(y/2) Q(y) dy.            (MAIN)
```

E72.46/E72.47 used `exp(-y/2)dy`, which corresponds to `du/u` and is not the PNT main measure.

## 1. Correct endpoint scale

Near the endpoint `y=L-r`:

```text
exp(z(y-L))exp(y/2) = x^(1/2) exp(-(z+1/2)r).
```

Using the overlap taper:

```text
||Q(L-r)|| <= 2r/L,
```

the continuous endpoint main has size:

```text
||S_x^{cont}(z)||
 <= 2x^(1/2) int_0^L exp(-(sigma+1/2)r) r/L dr
 <= 2x^(1/2)/(L(sigma+1/2)^2).                  (MAIN-scale)
```

Thus the continuous endpoint operator is **not** small. It is a large PNT main term and must be
subtracted.

## 2. Correct decomposition

The true endpoint object is:

```text
S_x^Lambda(z)
 = S_x^{cont}(z) + S_x^{err}(z),
```

where:

```text
S_x^{err}(z)
 = int_1^x (u/x)^z u^(-1/2)Q(log u)dE(u).
```

Only the error operator `S_x^{err}` is expected to be small after scalar compression.

## 3. Impact on previous documents

The following claims must be read as applying to the endpoint **shape/taper**, not to smallness of the
PNT main operator:

```text
E72.46 continuous endpoint operator smallness,
E72.47 continuous endpoint operator norm O(x^-1/2/L).
```

The corrected norm is:

```text
O(x^(1/2)/L).
```

This does not damage the scalar WRL route because E72.31 already requires model-main subtraction. It
does mean the continuous main cannot be used as a small term.

## 4. Correct remaining target

After model-main subtraction, prove:

```text
<v_{x,s},S_x^{err}(z)k_x> -> 0,
```

where:

```text
S_x^{err}(z)=int_1^x (u/x)^z u^(-1/2)Q(log u)dE(u).
```

This is exactly the scalar endpoint discrepancy `SEDC` of E72.48.

## 5. Status

```text
corrected: PNT main measure is du, giving exp(y/2)dy;
corrected: continuous endpoint main is O(sqrt(x)/L), not small;
survives: scalar WRL after model-main subtraction;
open:     prove scalar compressed Chebyshev-discrepancy smallness.
```
