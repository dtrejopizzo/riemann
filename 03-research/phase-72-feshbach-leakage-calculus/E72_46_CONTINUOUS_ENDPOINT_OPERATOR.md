# E72.46 -- Continuous endpoint operator estimate

**Date:** 2026-07-08.
**Role:** replace the unproved "quadratic taper" expectation by a continuous endpoint operator estimate
that follows directly from the exact cell taper.

## 0. Continuous endpoint operator

Let `L=log x`, `u=e^y`, and define the continuous endpoint operator

```text
S_x^{cont}(z)
 := int_0^L exp(z(y-L)) e^(-y/2) Q_x(y) dy,
```

where `Q_x(y)` is the matrix with entries `q_{mn}(y)`.

This is the model-main endpoint operator. The prime-discrete endpoint operator is:

```text
S_x^{prime}(z)=sum_{n<=x} (n/x)^z n^(-1/2) Q_x(log n)Lambda(n).
```

The difference is a Chebyshev-discrepancy operator.

## 1. Endpoint layer estimate

E72.38 proved:

```text
|q_{mn}(y)| <= 2(L-y)/L.
```

For `sigma=Re z>1/2`, set `r=L-y`. Then:

```text
|exp(z(y-L))e^(-y/2)q_{mn}(y)|
 <= 2 x^(-1/2) exp(-(sigma-1/2)r) r/L.
```

Thus entrywise:

```text
|S_x^{cont}(z)_{mn}|
 <= 2 x^(-1/2)/(L(sigma-1/2)^2).                (entry)
```

This is the precise endpoint-layer gain: the operator is supported, after weighting, in a boundary
layer of `O(1)` in `r`, and the cell vanishes like `r/L`.

## 2. What entrywise control can and cannot prove

Entrywise control alone gives a dimension loss:

```text
||S_x^{cont}(z)|| <= d_x * 2 x^(-1/2)/(L(sigma-1/2)^2),
```

which may be too weak if `d_x` grows like the matrix cutoff.

Therefore the proof must use the actual Fourier structure of `q_{mn}`, not just the absolute taper, to
avoid an incoherent dimension ceiling.

## 3. Fourier-structure target

The kernel `q_{mn}(y)` is a finite Fourier overlap. The desired operator estimate is:

```text
||Q_xS_x^{cont}(z)k_x|| = o(1),                 (CEO)
```

or, more sharply for scalar WRL:

```text
|<v_{x,s},S_x^{cont}(z)k_x>| = o(1).            (CES)
```

The endpoint layer estimate proves smallness per entry; the missing step is an orthogonality/Bessel
bound summing the Fourier overlaps without paying full dimension.

## 4. Discrete discrepancy split

The prime endpoint operator decomposes as:

```text
S_x^{prime}(z)
 = S_x^{cont}(z) + S_x^{disc-err}(z),
```

where

```text
S_x^{disc-err}(z)
 = int_1^x (u/x)^z u^(-1/2)Q_x(log u)dE(u).
```

Thus scalar endpoint orthogonality follows from:

```text
<v_s,S_x^{cont}(z)k_x> -> 0,                    (model endpoint)
<v_s,S_x^{disc-err}(z)k_x> -> 0.                (discrepancy endpoint)
```

The first is geometric/Fourier. The second is arithmetic but endpoint-tapered and scalar-compressed.

## 5. Status

```text
proved: endpoint layer entry bound for S_x^{cont};
identified: dimension-loss obstruction for absolute summation;
open: prove Fourier/Bessel summation for the continuous endpoint operator and scalar-compressed
      Chebyshev-discrepancy control for the discrete error.
```

This corrects E72.45: the second taper is not automatic. The rigorous route is continuous endpoint
operator smallness plus endpoint discrepancy control.
