# P76.026 - Exact boundary Fourier reduction

## Exact transform identity

Let `d_n=2*pi*n/L` and let `y=(y_n)` be the null vector of the canonical
right-boundary Schur completion, ordered on its finite mesh.  Since

```text
T_+(z)=-sum_n y_n/(z-d_n),
```

the elementary identity

```text
int_{-L/2}^{L/2} exp(i(z-d_n)x) dx
  =2(-1)^n sin(zL/2)/(z-d_n)
```

gives

```text
sin(zL/2)T_+(z)
  =int_{-L/2}^{L/2} exp(izx) f_{L,N}(x) dx,       (BF-1)

f_{L,N}(x)=-(1/2)sum_n (-1)^n y_n exp(-id_n x).  (BF-2)
```

Consequently, with `c_{L,N}=int f_{L,N}`,

```text
Phi_{L,N}(z)=int exp(izx) g_{L,N}(x) dx,
g_{L,N}=f_{L,N}/c_{L,N}.                         (BF-3)
```

This is an identity, not an asymptotic model.  It also explains why bounding
the sine and the Cauchy transfer separately destroys the relevant
cancellation.

## One sufficient theorem for both analytic locks

Let `k_Xi` be the inverse Fourier kernel normalized by

```text
int_R k_Xi(x) dx=1,
int_R exp(izx) k_Xi(x) dx=Xi(1/2+iz)/Xi(1/2).
```

For some `epsilon>0`, suppose an admissible path satisfies

```text
N(L)/L -> infinity,                              (BF-HORIZON)

int_R exp((1/2+epsilon)|x|)
  |1_{|x|<=L/2}g_{L,N(L)}(x)-k_Xi(x)| dx ->0.   (BF-WL1)
```

Then, uniformly on every compact subset of
`|Im z|<1/2+epsilon`, `(BF-3)` converges to normalized `Xi`.  The same
weighted norm gives a compact-uniform bound, so `BCF-NORMAL` and
`BCF-SAFE-ID` both follow.

Thus the two hypotheses in P76.024 follow from the single explicit
boundary-null convergence theorem `BF-WL1`.  This is a sufficient route,
not an equivalence: local uniform convergence of Fourier transforms need
not imply weighted-`L1` convergence of their inverse densities.

## Why the horizon condition is mandatory

The factor `sin(zL/2)` has uncancelled zeros at mesh points outside the
finite pole set.  To prevent those artificial real zeros from entering a
fixed compact, the pole horizon

```text
2*pi*N(L)/L
```

must tend to infinity.  Merely taking `L,N -> infinity` is insufficient.

## Current status

`BF-1`--`BF-3` are exact.  `BF-WL1` is not proved.  It is a concrete strong
sufficient condition for the previous abstract normal-family pair.  It is
also compatible with the Phase-71 Connes/prolate bridge:
one may close it by proving that the normalized canonical boundary-null
polynomial `g_{L,N}` converges to the established Xi kernel in this weighted
`L1` norm.

The overlap probes of P76.021 do not prove this statement; an unweighted
Hilbert-space angle cannot control the exponential Fourier strip.
