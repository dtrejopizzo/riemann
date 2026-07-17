# E72.55 -- Loewner cancellation probe

**Date:** 2026-07-08.
**Role:** test whether the half-power scalar endpoint channel comes from separate smallness of the two
pieces in E72.54 or from cancellation between them.

## 0. Split

E72.54 proved:

```text
Q_x(y)=2cos(yD)-(2/L)Lo_y.
```

Thus:

```text
<v,S_x(z)k>
 = Cos_x(s;z)+Lo_x(s;z).
```

## 1. Numerical signal

Representative values:

```text
z=10, x=64:
  |total|=8.36e-4, |cos|=1.33e-2, |lo|=1.26e-2, ratio=3.24e-2

z=10, x=144:
  |total|=1.91e-4, |cos|=2.88e-3, |lo|=2.72e-3, ratio=3.42e-2

z=14, x=64:
  |total|=4.99e-4, |cos|=1.08e-2, |lo|=1.05e-2, ratio=2.34e-2

z=14, x=144:
  |total|=8.39e-5, |cos|=2.22e-3, |lo|=2.16e-3, ratio=1.91e-2
```

The total is often one to two orders of magnitude smaller than the sum of the two absolute pieces.

## 2. Interpretation

The half-power weighted channel bound is not produced by estimating:

```text
2cos(yD)
```

and:

```text
-(2/L)Lo_y
```

separately.

It is produced by their finite Loewner cancellation. Therefore the proof must use the identity:

```text
Q_x(y)=2cos(yD)-(2/L)D(sin(yD))[J]
```

as a whole.

## 3. New target

### Loewner Endpoint Cancellation

For the endpoint-weighted transform:

```text
sum_{n<=x}(n/x)^z n^(-1/2)
<v,[2cos(log n D)-(2/L)Lo_{log n}]k>,
```

prove half-power smallness by the Loewner identity, not by separate bounds.

This is now the finite identity behind the observed scalar WRL cancellation.

## 4. Status

```text
observed: strong cancellation between diagonal cosine and Loewner terms;
open: prove Loewner Endpoint Cancellation from the commutator relation [D,Lo_y]=[sin(yD),J].
```

The next step is to turn the endpoint sum of the full Loewner expression into a boundary term in `y`.
