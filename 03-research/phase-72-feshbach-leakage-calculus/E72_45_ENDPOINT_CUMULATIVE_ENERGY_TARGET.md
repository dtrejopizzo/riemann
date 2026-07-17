# E72.45 -- Endpoint cumulative-energy target

**Date:** 2026-07-08.
**Role:** isolate the exact estimate needed after the Green pairing identity E72.44.

## 0. Endpoint source

The endpoint-weighted source is:

```text
F_z = Q_xS_x(z)k_x/k_x,
S_x(z)=sum_{n<=x}(n/x)^zT_{x,n}.
```

Its cumulative force is:

```text
G_z(theta)=int_a^theta F_z(t)m_x(t)dt.
```

The estimate needed for Endpoint Doob-Weyl Smallness is:

```text
||G_z||_{rho^{-1}} -> 0.                         (ECE)
```

uniformly for `z` in compact subsets of `Re z>1/2`.

## 1. Cell cumulative kernels

For each cell define:

```text
K_{x,n}(theta)
 := int_a^theta k_x(t)T_{x,n}k_x(t)dt
    - beta_{x,n} int_a^theta k_x(t)^2dt,
beta_{x,n}=<k_x,T_{x,n}k_x>.
```

Then:

```text
G_z(theta)=sum_{n<=x}(n/x)^z K_{x,n}(theta).     (KZ)
```

This is the endpoint-weighted analogue of E72.13.

## 2. Endpoint cumulative energy

Define the endpoint Gram:

```text
M_x^end(z,w)
 := int_a^b
    [sum_n (n/x)^zK_{x,n}(theta)]
    conj([sum_m (m/x)^wK_{x,m}(theta)])
    /rho_x(theta)dtheta.
```

Then:

```text
||G_z||_{rho^{-1}}^2 = M_x^end(z,z).             (EG)
```

The target `(ECE)` is:

```text
M_x^end(z,z)->0.                                 (ECE-Gram)
```

## 3. Endpoint taper advantage

E72.38 gives:

```text
|T_{x,u}| <= u^(-1/2)(1-log u/L) * channel.
```

After cumulative integration in `theta`, the expected endpoint cell estimate is:

```text
||K_{x,u}||_{rho^{-1}}
 <= C_x u^(-1/2)(1-log u/L)^2.                  (K-taper)
```

The second taper factor is the new gain from cumulative centering.

If `(K-taper)` holds with `C_x` bounded in the endpoint-weighted Gram sense, then for `sigma=Re z>1/2`:

```text
||G_z||_{rho^{-1}}
 <= C_x sum_{n<=x}(n/x)^sigma n^(-1/2)(1-log n/L)^2.
```

The continuous analogue is:

```text
x^(-1/2) int_0^L exp(-(sigma-1/2)r)(r/L)^2 dr
 <= 2 x^(-1/2)/((sigma-1/2)^3 L^2).             (E2)
```

This tends to zero if `C_x=o(x^(1/2)L^2)`.

## 4. The exact new estimate

### Quadratic Endpoint Taper

For the centered cumulative cells,

```text
||K_{x,u}||_{rho^{-1}}
 <= C_x u^(-1/2)(1-log u/L)^2
```

with `C_x=o(x^(1/2)L^2)` in the coherent endpoint-weighted sum.

This is the estimate that would prove `(ECE)`.

## 5. Why this is plausible

The first factor `(1-log u/L)` is exact in the cell kernel `q_{mn}`. The second is expected because
`K_{x,u}` is a centered cumulative primitive with endpoint values zero:

```text
K_{x,u}(a)=K_{x,u}(b)=0.
```

Endpoint vanishing plus centering usually upgrades a boundary taper by one primitive order.

## 6. Status

```text
proved: Endpoint Doob-Weyl smallness follows from endpoint cumulative energy decay;
identified: quadratic endpoint taper is sufficient;
open: prove quadratic endpoint taper for centered cumulative CCM cells.
```

The next step is to test and then prove the quadratic taper for `K_{x,u}`.
