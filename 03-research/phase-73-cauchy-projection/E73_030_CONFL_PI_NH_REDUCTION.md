# E73.030 - CONFL-PI-NH reduction

## 1. Starting point

E73.026 showed that separated-node blow-up is removed by Hermite/confluent coordinates.  E73.027
identified the local confluent inverse with a Taylor problem:

```text
f_beta(w)=w/(1+beta w),
w0=1/(2a),
beta=k-a.
```

The Hermite projection coefficients are the coefficients of the degree `<m` polynomial in `w`
matching `f_beta` at `w0` through order `m-1`.

## 2. Local analytic control

The only pole of `f_beta` is

```text
w_*=-1/beta=-1/(k-a).
```

Thus the local Hermite norm is controlled by the Taylor radius

```text
R(a,k)=|w0-w_*|
= | 1/(2a) + 1/(k-a) |.
```

Equivalently,

```text
R(a,k)= |(k+a)/((2a)(k-a))|.
```

For a shifted off-line node

```text
a=sigma+it,       sigma>0,
```

and a critical node

```text
k=i gamma,
```

the dangerous case is not `gamma≈t`.  Then `k-a≈-sigma+i(gamma-t)` and
`k+a≈sigma+i(gamma+t)`, so `R(a,k)` is large, not small, when `|gamma-t|` is small.

The dangerous case is instead the reflected near-pole condition:

```text
k≈-a,
```

because then `k+a≈0`.  But the representative convention in the shifted divisor identifies `w` and
`-w`, and the off-line block uses one representative from each pair.  This is exactly the same
condition that keeps the Cauchy denominator `a+k` away from zero.

## 3. Finite local bound

For fixed multiplicity `m`, if

```text
R(a,k) >= r0 > 0,
```

then Cauchy's estimate for the Taylor expansion of `f_beta` in the `w`-plane gives

```text
||C_conf(a,m)^(-1)v_k||_Herm <= C(m,a,k,r0).
```

In the tested natural geometry this bound is stable and often saturates as `m` grows, because the
Hermite polynomial converges to the local Taylor expansion before numerical instability appears.

## 4. Natural-height reduction

The global Hermite projection gate becomes:

```text
CONFL-PI-NH:
For every natural-height off-line Hermite cluster A and critical window K_L,

e^(alpha L) sum_{k in K_L}
  ||C_conf(A)^(-1)v_k||_Herm
<= L^B.
```

By E73.027, this is now equivalent to a finite rational Taylor-radius bound:

```text
e^(alpha L) sum_{k in K_L} T_m(a,k) <= L^B,
```

where `T_m(a,k)` is the Hermite norm of the Taylor polynomial of `w/(1+(k-a)w)` at `w0=1/(2a)`.

## 5. What remains

This reduction isolates the true remaining geometric content:

```text
REFLECTED-SEPARATION:
natural-height critical nodes do not approach reflected off-line cluster poles k=-a at an
exponential scale that defeats the factor e^(alpha L).
```

E73.031 corrects this point.  Reflected separation controls only the Hermite projection geometry.
It does not remove the factor `e^(alpha L)` in the weighted norm.  Since E72.327 `CRIT-POLY` gives
only a polynomial bound for the critical data, reflected separation plus `CRIT-POLY` is not enough
to prove `CC-PROJ` for a fixed off-line `alpha>0`.

The remaining route must be `DATA`: the cancelled Cauchy values must be exponentially small after
projection onto the Hermite confluent directions.

## 6. Status

```text
proved: local confluent inverse equals Taylor matching;
validated: local cluster blow-up disappears in Hermite coordinates;
reduced: local CONFL-PI to Taylor-radius control;
corrected by E73.031: absolute geometry cannot close NAT-PROJ;
open: prove DATA-HERM cancellation.
```

This is now the sharpest finite geometric formulation of the remaining projection gate.
