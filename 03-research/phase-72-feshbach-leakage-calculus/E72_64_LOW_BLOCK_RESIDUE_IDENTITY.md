# E72.64 -- Low-block residue identity and the spectral divisibility target

**Date:** 2026-07-08.
**Role:** identify the low-frequency Feshbach cancellation with scalar spectral divisibility.

## 0. Low block from E72.63

The low block is:

```text
B_low(T)
 = sum_{|d_n|<=T} alpha_n sigma_n(z)
   + sum_{|d_n|<=T} beta_n partial_{d_n}sigma_n(z).                (LOW)
```

For fixed `T`, the endpoint transforms are not controlled by oscillation. They contain the low
Mellin residues of the Chebyshev discrepancy.

## 1. Mellin form of the endpoint transforms

Set:

```text
a=z-1/2.
```

Using `r=log(x/u)`:

```text
exp(-ar)exp(id_nr)
 = x^(-a+id_n)u^(a-id_n).
```

Thus:

```text
sigma_n(z)
 = Im[ x^(-a+id_n) int_1^x u^(a-id_n)dE(u) ].                    (SIG-M)
```

Similarly, `partial_{d_n}sigma_n` is the same Mellin transform after applying the logarithmic
differential produced by:

```text
partial_d exp(idr)=ir exp(idr).
```

Therefore `B_low(T)` is a finite linear combination of:

```text
x^(-a+id_n) int_1^x u^(a-id_n)(log(x/u))^j dE(u),       j=0,1.     (MLOW)
```

## 2. Residue coefficient

Insert the explicit-formula expansion formally into `(MLOW)`. The contribution of a zero `rho` has
the shape:

```text
x^rho R_{x,T}(s,z;rho),
```

where:

```text
R_{x,T}(s,z;rho)
 = sum_{|d_n|<=T}
   alpha_n A_n(z,rho)
   + beta_n B_n(z,rho).                                           (RES)
```

Here `A_n` and `B_n` are explicit rational functions of:

```text
z-1/2-id_n+rho,
```

with `B_n` equal to the corresponding logarithmic derivative in `d_n`.

Thus low-current cancellation for every possible off-critical residue is equivalent to:

```text
R_{x,T}(s,z;rho)=o(x^(1/2-Re rho)L)
```

for each off-critical `rho`.

## 3. Identification with scalar WRL resonance

Let:

```text
M_x(s;w)=w int_1^x u^(w-1)L_x(s;u)du
```

be the scalar Mellin transform of E72.33. The reflected Loewner representation shows that, after the
same endpoint/model normalization,

```text
R_{x,T}(s,z;rho)
```

is the low-frequency truncation of:

```text
M_x(s;rho).
```

Consequently:

```text
low Feshbach current cancellation for all off-critical residues
```

is not an independent analytic-number-theory estimate. It is the low-frequency face of:

```text
Mellin spectral divisibility:
M_x(s;w)=P_x(w)A_x(s;w)+E_x(s;w).                                  (MSD)
```

## 4. Consequence

High-frequency endpoint cancellation may be accessible through oscillatory prime-sum estimates and
coefficient mass bounds. The low block cannot be closed this way. For fixed or slowly growing
frequencies, any proof that simply estimates each `sigma_n` would have to beat the possible
`x^rho` residues, which is RH-strength.

Therefore the low block must be proved by a finite algebraic identity:

```text
R_{x,T}(s,z;w)=P_x(w)A_{x,T}(s,z;w)+E_{x,T}(s,z;w).                (LMSD)
```

This is the precise, non-circular version of "the Feshbach coefficients kill the residues":

```text
the killing must occur before inserting any zero rho.
```

## 5. Status

```text
proved: low endpoint currents are finite Mellin residue functionals;
proved: low cancellation is the low-frequency form of Mellin spectral divisibility;
open:   construct the finite algebraic divisor P_x in the low reflected Loewner coefficients.
```
