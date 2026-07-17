# E72.89 -- Finite-band root remainder

**Date:** 2026-07-09.
**Role:** state the current minimal finite identity after the CCGD and finite-band reductions.

## 0. Input

E72.87 gives the Cauchy-channel Green decay certificate `(CCGD-QR)`.

E72.88 shows that, once `(CCGD)` is known, the full dual cofactor transport residual is reduced to its
finite physical-height band:

```text
R_{x,H}(s;tau)
 = i C_{P_Hg,k}(tau)
   -(exp(i tau L)-1)L^(-1)C_{P_Hg,1}(tau)M_k(tau).
```

Here:

```text
g=g_{x,s}=B_xC_E^(-1)B_x^*r_s^even,
P_H=1_{|d_n|<=H}.
```

For fixed `x` and `H`, this is a finite rational-exponential function of `tau`.

## 1. Root remainder

Let the active positive finite Weyl roots be:

```text
Tau_x={tau_1,...,tau_J},
P_{x,+}(z)=prod_j(z-tau_j).
```

Define:

```text
Rem_{Tau_x}R_{x,H}(s;z)
 := sum_j R_{x,H}(s;tau_j)
    P_{x,+}(z)/(P_{x,+}'(tau_j)(z-tau_j)).
```

Then:

```text
R_{x,H}(s;tau_j)=0 for every active tau_j
    <=> Rem_{Tau_x}R_{x,H}(s;z) identically 0.                (FBRR)
```

Thus finite-band root transport is exactly the vanishing of this finite interpolation remainder.

## 2. Current minimal theorem

The remaining proof can now be written as:

```text
Finite-band root-remainder theorem:
For every compact s-window K and every fixed physical cutoff H,

lim_{x->infty} sup_{s in K}
  ||Rem_{Tau_x}R_{x,H}(s;.)|| = 0.                            (FBRT)
```

Then:

```text
CCGD-QR + FBRT for all fixed H + H->infty
    => dual cofactor root transport
    => HPAC divisibility
    => scalar WRL resonance annihilation.
```

This is the most explicit endpoint reached so far:

```text
1. a finite quadratic inequality in s for CCGD;
2. a finite interpolation remainder identity in tau for root transport.
```

## 3. Non-circularity check

The finite roots `tau_j` are roots of the finite CCM Weyl divisor:

```text
M_xi(tau_j)=0.
```

The model vector `k_x`, the shorted cofactor vector `g_{x,s}`, and the physical cutoff `P_H` are built
without using global zeta zeros. The statement does not insert the target `Xi` divisor. It is still a
hard arithmetic identity, but it is finite and explicit.

## 4. Status

```text
proved: finite-band transport is equivalent to finite root-remainder vanishing;
open:   prove (CCGD-QR) and (FBRT).
```
