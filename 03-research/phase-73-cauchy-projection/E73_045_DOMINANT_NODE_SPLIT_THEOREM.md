# E73.045 - Dominant-node split theorem

## 1. Purpose

E73.043 shows that global product decoupling is too lossy.
E73.044 shows that the `WCS` mass is concentrated on very few critical nodes.

This document states the resulting finite sufficient theorem.

## 2. WCS terms

For a fixed off-line Hermite cluster `A=(a,m)`, define

```text
T_k(A,L)
:=
e^(alpha L)
G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|C_x(i gamma_k)|.
```

Then

```text
WCS(A,L) is exactly sum_k T_k(A,L) <= L^B.
```

## 3. Dominant-node split

Let `D(A,L)` be a finite set of dominant critical indices and `R(A,L)` its complement.

Assume:

```text
DNS-main:
sum_{k in D(A,L)} T_k(A,L) <= (1-epsilon)L^B,
```

and

```text
DNS-tail:
sum_{k in R(A,L)} T_k(A,L) <= epsilon L^B.
```

Then `WCS(A,L)` holds.

## 4. Proof

The proof is just the disjoint decomposition:

```text
sum_k T_k
= sum_{k in D} T_k + sum_{k in R} T_k
<= (1-epsilon)L^B + epsilon L^B
= L^B.
```

By E73.042,

```text
WCS => scalar WRL.
```

Therefore

```text
DNS-main + DNS-tail => scalar WRL.
```

## 5. Non-tautological certificate format

For a finite box of off-line centers and fixed multiplicity, choose `D` by an upper envelope for
the geometric part:

```text
D = indices where
G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|
is among the largest few on the box.
```

Then:

```text
DNS-main
```

is a finite list of direct Cauchy value certificates at the dominant critical nodes, and

```text
DNS-tail
```

may use a coarser separated estimate because the largest dangerous terms have been removed.

This avoids the failure of global decoupling in E73.043.

The key rule is:

```text
D must be chosen without using |C_x(i gamma_k)|.
```

Otherwise the split would only rename the already known WCS terms.  The admissible data for choosing
`D` are:

```text
1. the off-line box;
2. the explicit Hermite bound G_theta,m;
3. the mesh factor |1-exp(i gamma L)|;
4. the critical window geometry.
```

After `D` is fixed by these data, the arithmetic Cauchy values enter only in the estimates for
`DNS-main` and `DNS-tail`.

## 6. Remaining theorem

The current sharp target is the uniform dominant-node split:

```text
Uniform DNS:
There exist B, epsilon, r, and L0 such that for every L>=L0 and every natural-height off-line
cluster A, the r dominant WCS nodes satisfy DNS-main and the complement satisfies DNS-tail.
```

The experiments suggest `r<=3` in the tested windows, but the proof must derive `r` from the
explicit Hermite kernel envelope and the natural-height window geometry.
