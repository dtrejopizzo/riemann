# E73.110 - HERM-BOX derivative certificate

## 1. Purpose

E73.109 shows that a modest Hermite box enclosure is enough for the weighted FAR-SLOPE budget.
This note states the rigorous derivative certificate that upgrades E73.109 from numerical evidence
to interval proof.

## 2. Elementary variables

For:

```text
a=alpha+i tau,
k=i gamma,
beta=k-a,
u=1/a,
v=1/beta,
w0=u/2,
wstar=-v,
d=|wstar-w0|,
r=theta d,
```

the Hermite bound is:

```text
G(a,k)
=
1/(|beta|(1-theta)d)
*
sum_{p=0}^{m-1}
  1/p!
  sum_{q=p}^{m-1}
    binom(q,p)|w0|^(q-p)(theta d)^(-q).
```

It is a finite expression in:

```text
|a|, |beta|, |v+u/2|.
```

## 3. Box separation data

On a cluster box `B`, compute lower bounds:

```text
A_B      <= |a|,
B_B      <= |beta|=|i gamma-a|,
D_B      <= |v+u/2|.
```

More explicitly:

```text
A_B := inf_{a in B}|a|,
B_B := inf_{a in B}|i gamma-a|,
D_B := inf_{a in B}|1/(i gamma-a)+1/(2a)|.
```

The natural boxes used in E73.107 have these quantities bounded away from zero for the FAR rows.

## 4. Derivative envelope

Because:

```text
partial_alpha (1/a) = -1/a^2,
partial_tau   (1/a) = -i/a^2,
partial_alpha (1/beta) =  1/beta^2,
partial_tau   (1/beta) = -i/beta^2,
```

one obtains:

```text
|partial_* u| <= A_B^-2,
|partial_* v| <= B_B^-2,
|partial_* w0| <= (1/2)A_B^-2,
|partial_* wstar| <= B_B^-2,
|partial_* d| <= B_B^-2 + (1/2)A_B^-2.
```

For a monomial:

```text
M_{q,r}=|w0|^r d^(-q),
```

the logarithmic derivative bound is:

```text
|partial_* M_{q,r}|
<=
M_{q,r}
(
 r |w0|^-1 (1/2)A_B^-2
 + q D_B^-1 (B_B^-2+(1/2)A_B^-2)
).
```

The prefactor:

```text
P=1/(|beta|(1-theta)d)
```

satisfies:

```text
|partial_* P|
<=
P
(
 B_B^-1 B_B^-2
 + D_B^-1(B_B^-2+(1/2)A_B^-2)
).
```

Combining these finitely over `p,q` gives an explicit derivative envelope:

```text
Lip_B(G;k,m,theta)
>= sup_{a in B} max(|partial_alpha G|, |partial_tau G|).
```

## 5. Rigorous HERM-BOX enclosure

Given a subdivision of `B` into cells `B_j`, choose one point `a_j` in each cell and compute:

```text
G_j=G(a_j,k),
Lip_j=Lip_{B_j}(G;k,m,theta),
rad_j=diam(B_j)/2.
```

Then:

```text
sup_{a in B}G(a,k)
<=
max_j (G_j + Lip_j rad_j).
```

This is the rigorous version of the E73.109 grid enclosure.

## 6. Theorem

**Theorem 110.1.**  If the separation data `A_B,B_B,D_B` are positive on every subdivision cell,
then the above procedure gives a rigorous finite upper enclosure for `G_theta,m(a,i gamma)` on `B`.

*Proof.*  On each cell, the derivative envelope bounds the norm of the gradient of `G`.  The mean
value theorem gives:

```text
G(a,k) <= G(a_j,k)+Lip_j|a-a_j|
```

for every `a` in the cell.  Taking the maximum over cells proves the enclosure. `□`

## 7. Consequence

Combining Theorem 110.1 with E73.106 gives:

```text
HERM-BOX => rigorous box certificate for FAR3-MAIN-RAT.
```

The remaining implementation task is mechanical: compute `A_B,B_B,D_B` and the finite derivative
sum on each cell with outward rounding or rational interval arithmetic.
