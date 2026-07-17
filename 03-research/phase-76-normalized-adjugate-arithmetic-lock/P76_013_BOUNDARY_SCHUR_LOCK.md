# P76.013 - Boundary Schur lock

## Nested cutoff decomposition

Fix `L` and write the cutoff-`N` CCM matrix in the order
`(-N, inner, N)`:

```text
H_N=[ A_N  B_N ],
    [ B_N* C_N ],
```

where `A_N=H_{N-1}` and the boundary block has dimension two.  Let `mu_N`
be the simple ground eigenvalue and write its normalized eigenvector as

```text
xi_N=(u_N,v_N),
v_N in C^2.
```

Provided `mu_N` is not an eigenvalue of `H_{N-1}`, the inner equation gives

```text
u_N=-(H_{N-1}-mu_N I)^(-1)B_N v_N.          (BS-1)
```

## Phase-free Cauchy transfer

Split the Cauchy row into inner and boundary parts:

```text
r_z=(r_z^in,r_z^bd).
```

Define the two-dimensional boundary transfer

```text
T_{L,N}(z)
=r_z^bd-r_z^in(H_{N-1}-mu_N I)^(-1)B_N.     (BS-2)
```

Then `(BS-1)` gives the exact identity

```text
r_z xi_N=T_{L,N}(z)v_N.                      (BS-3)
```

Since `||v_N||<=1`,

```text
|r_z xi_N|/||r_z||
<=||T_{L,N}(z)||/||r_z||.                    (BS-4)
```

Thus the following theorem is strictly stronger than the normalized
arithmetic lock and contains no eigenvector phase.

```text
BOUNDARY-SCHUR-LOCK:
for every M and every resolved natural window,
||T_{L,N(L)}(gamma)||/||r_gamma||=O_M(L^-M).
```

It implies `NORMALIZED-ARITH-LOCK` immediately by `(BS-4)`, and therefore
implies the complete Phase-75 closure chain to Omega7 once the already named
polynomial transfer hypotheses are supplied.

## Determinant form

For each boundary column `b_j` and boundary Cauchy value `r_j(z)`, Cramer's
rule gives

```text
T_j(z)
=det [[H_{N-1}-mu_N I, b_j],
      [r_z^in,             r_j(z)]]
 /det(H_{N-1}-mu_N I).                         (BS-5)
```

This is a finite bordered determinant ratio depending only on:

```text
the Gamma-prime CCM entries,
the mesh,
the ground level mu_N,
the two new boundary modes.
```

It does not use `xi_N`, a zero list, a pseudoinverse, or a fitted quotient.

## Rational interpolation form

Let

```text
x_j=(H_{N-1}-mu_N I)^(-1)b_j.
```

Then

```text
T_j(z)=1/(z-d_j^bd)-sum_{|n|<N}x_j(n)/(z-d_n). (BS-6)
```

So `BOUNDARY-SCHUR-LOCK` is a two-column rational interpolation theorem:
the CCM resolvent weights approximate each new boundary pole in the critical
Cauchy channel.  This is different from the rejected Phase-74 Schur transfer,
which compressed a fixed Cauchy plane and retained `Qxi` as input.  Here the
cutoff boundary is compressed and the upper bound is independent of `xi_N`.

## Numerical certification and falsifiers

For `lambda=6`, `N=9` and the first critical ordinate:

```text
zeta:
||T(gamma)||/||r||       =5.83e-18,
|r xi|/||r||             =2.18e-24,
||T(gamma+0.125)||/||r|| =1.46.

planted off-line at gamma:
||T(gamma)||/||r||       =3.86e-3.

random symmetric matrix:
||T(gamma)||/||r||       =1.24.
```

The exact identity `(BS-3)` closes between `1e-57` and `1e-70` in these
tests.  Hence the transfer norm itself, not only its pairing with the boundary
eigenvector, carries arithmetic selectivity.

## Remaining analytic theorem

The open task is to prove `BOUNDARY-SCHUR-LOCK` from `(BS-5)` or `(BS-6)` in
an admissible regime such as

```text
d_max >= (1+delta) max|gamma|,
N(L) polynomial or subexponential,
```

without invoking:

```text
global Weil/Pick positivity,
normal convergence to Xi as an assumption,
an inverse-gap norm bound,
or the desired Cauchy lock itself.
```

The most concrete next calculation is to insert the exact diagonal-Loewner
form of P76.011 into the linear systems defining `x_j`, then derive a signed
scalar interpolation remainder for `(BS-6)`.
