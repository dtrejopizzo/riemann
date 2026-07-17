# E73.001 - NAT-PROJ finite identity

## 1. Purpose

This note starts Phase 73 by isolating the exact finite identity left by Phase 72.

The problem is no longer a tail estimate.  It is the finite Cauchy projection

```text
Pi_{O<-K}G_K=C_OO^(-1)C_OKG_K
```

from critical-line nodal data into the off-line Cauchy block.

## 2. Objects

Let

```text
W_L={w=rho-1/2 mod +- : |Im w|<=T_L},       T_L=e^L L^A.
```

Split

```text
O_L={a in W_L : Re a>0},
K_L={k in W_L : Re k=0}.
```

Define finite Cauchy matrices

```text
C_OO(a,b)=1/(a+b),        a,b in O_L,
C_OK(a,k)=1/(a+k),        a in O_L, k in K_L.
```

The critical vector is

```text
G_K(k)=G_x(k)
     =(1-e^(kL)) sum_m xi_m/(ik-d_m).
```

Here `xi` is the finite pole-even CCM vector, and `d_m=2pi m/L`.

## 3. Exact remaining condition

Phase 72 proves that off-line nodal suppression follows from:

```text
NAT-PROJ:
max_{a in O_L} e^(Re a L)
 |(C_OO^(-1)C_OKG_K)_a| <= L^B.                       (1)
```

This is finite for every `L`.  It contains no infinite zero tail and no finite Fourier tail.

## 4. Equivalent row form

Equation (1) is equivalent to the existence of a vector `H_O` with

```text
H_O(a)=O(e^(-Re a L)L^B)
```

such that

```text
C_OO H_O = -C_OKG_K.                                  (2)
```

Equivalently, the meromorphic function

```text
R_L(s):=sum_{a in O_L} H_O(a)/(s+a)
       +sum_{k in K_L} G_K(k)/(s+k)
```

has zeros at every off-line node:

```text
R_L(a)=0,        a in O_L,                            (3)
```

up to the exponentially small tolerance in (1).

Thus `NAT-PROJ` can be attacked as a finite interpolation statement:

```text
critical-line residues generate an off-line cancelling rational function with exponentially small
off-line coefficients.
```

## 5. The target for the next step

The first possible closure mechanism is:

```text
CRIT-DD:
G_K(k) is not an arbitrary polynomially bounded vector; it is a divided-difference trace of the
finite pole-even Cauchy numerator.  This structure forces the rational interpolant R_L to have
exponentially small off-line residues.
```

The next theorem should express `G_K(k)` in the basis dual to the Cauchy evaluation functionals
`s -> 1/(s+a)`, and test whether the off-line coefficients vanish by the finite Weyl numerator
relations.

## 6. Status

```text
entry identity: NAT-PROJ;
equivalent finite form: rational interpolation equations (2)--(3);
open: prove CRIT-DD or find the exact finite obstruction.
```

