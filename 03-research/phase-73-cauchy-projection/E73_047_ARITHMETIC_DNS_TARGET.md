# E73.047 - Arithmetic DNS target

## 1. Motivation

E73.046 proves that the dominant WCS nodes cannot be selected by geometry and mesh alone.

The dangerous nodes are selected by arithmetic data.  To avoid tautology, the arithmetic selector
must be structural: it may use the finite Cauchy divisor/eigenvector equations, but it must not use
the final WCS products as the definition of dominance.

## 2. Data allowed for an arithmetic selector

The selector may use:

```text
1. poles d_n of the finite CCM model;
2. weights xi_n through the numerator polynomial P_x of C_x=P_x/D_x;
3. finite Cauchy roots rho_j=Div(P_x);
4. mesh factors |1-exp(i gamma L)|;
5. Hermite geometry G_theta,m(a,i gamma).
```

It may not choose nodes by sorting

```text
G_theta,m(a,i gamma)|1-exp(i gamma L)||C_x(i gamma)|.
```

## 3. Candidate selector

For each critical height `gamma_k`, define a structural arithmetic score

```text
S_k(A,L)
:=
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|
* R_x(gamma_k),
```

where `R_x(gamma_k)` is a divisor proxy built before evaluating `C_x(gamma_k)`, for example

```text
R_x(gamma_k) =
min_j dist(gamma_k,rho_j) / sep_x(gamma_k,rho_j),
```

with `sep_x` computed from the finite pole and divisor configuration.

Then define

```text
D_r(A,L) = top r nodes by S_k(A,L).
```

## 4. Required theorem

The arithmetic dominant-node theorem is:

```text
ADNS:
There exist B, epsilon, r, and L0 such that for every L>=L0 and every natural-height off-line
cluster A,

sum_{k in D_r(A,L)} T_k(A,L) <= (1-epsilon)L^B,
sum_{k notin D_r(A,L)} T_k(A,L) <= epsilon L^B.
```

Here `T_k` is the true WCS term, but `D_r` is selected by `S_k`, not by `T_k`.

## 5. Why this is the right next identity

The finite divisor identity E73.038 showed that `C_x` is controlled by the numerator divisor
`P_x`.  E73.046 showed that geometry alone does not find the dangerous nodes.

Therefore the missing information is precisely:

```text
how the finite Cauchy divisor of the CCM pole-even vector aligns with the critical mesh.
```

`ADNS` is the finite explicit form of that alignment.
