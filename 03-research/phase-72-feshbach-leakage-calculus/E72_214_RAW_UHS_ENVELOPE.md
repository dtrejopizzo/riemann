# E72.214 - Raw truncated-translation HS envelope

## Purpose

E72.212 reduces the geometric envelope to:

```text
lambda_min(C_x) >= c_C L^2,
||B_x^*U_yB_x||_HS^2 <= C_U L^2 Phi(y/L).
```

E72.213 supports the first estimate. This note audits the second.

## Diagnostic

Script:

```text
E72_214_raw_uhs_probe.py
```

Output:

```text
E72.214 raw U_y Hilbert-Schmidt probe
UHS candidate: ||B* U_y B||_HS^2 <= C L^2 Phi(y/L)
lam L qdim u0.1/L2 u0.25/L2 u0.5/L2 u0.75/L2 u0.9/L2 maxRaw/L2
 12  4.97   32 0.577 0.480 0.314 0.147 0.056 0.681
 16  5.55   40 0.583 0.487 0.319 0.155 0.060 0.649
 20  5.99   48 0.593 0.500 0.328 0.160 0.061 0.624
 24  6.36   56 0.625 0.516 0.340 0.162 0.058 0.711
 28  6.66   64 0.636 0.538 0.355 0.175 0.068 0.685
```

## Reading

The raw one-sided translation overlap satisfies a stable scale:

```text
||B_x^*U_yB_x||_HS^2 = O(L^2).
```

On the tested grid,

```text
||B_x^*U_yB_x||_HS^2 / L^2 <= 0.72.
```

The profile decreases in `u=y/L`, except for mild finite-section variation near the lower endpoint.

## Coercive consequence

Combining this with E72.213 gives a fully explicit but conservative envelope:

```text
Geom_x(y)
<= (0.72/c_C^2) L^(-2).
```

Using only the tested lower bound `c_C=0.20` gives `18 L^-2`, which is too crude for sharp budgets but
already has the correct scale. Using the stable-window values `c_C~=0.30--0.48` gives a much sharper
constant.

The proof route is now clear:

```text
prove MCOER2 with a stable-window constant,
prove UHS with a monotone profile Phi,
then sum Lambda(n)^2/n against Phi(log n/L).
```

## Status

Positive. The raw Fourier/translation half of the resonant geometric envelope has the expected
`L^2` scale.
