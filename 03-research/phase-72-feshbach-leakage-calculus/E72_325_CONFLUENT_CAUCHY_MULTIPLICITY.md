# E72.325 -- Confluent Cauchy block for multiple zeros

**Purpose.** Close the multiplicity bookkeeping left open in E72.324. Multiple zeros replace the simple
Cauchy matrix `1/(a_j+a_k)` by its confluent Hermite limit. That matrix is still invertible when the
cluster lies in the positive shifted half-plane.

## 1. Confluent block

Let the maximal-real-part cluster be

```text
A={a_1,...,a_J},        Re a_j=alpha>0,
```

where `a_j` has multiplicity `m_j`. The leading simple-cluster kernel is

```text
C(x,y)=1/(x+y).
```

For multiplicities, the block indexed by `(j,p)` and `(k,q)`, with

```text
0<=p<m_j,        0<=q<m_k,
```

is the Hermite/confluent Cauchy matrix

```text
C_conf[(j,p),(k,q)]
:= (1/(p!q!)) partial_x^p partial_y^q [1/(x+y)]|_{x=a_j,y=a_k}.     (1)
```

Equivalently,

```text
C_conf[(j,p),(k,q)]
= (-1)^(p+q) binom(p+q,p)/(a_j+a_k)^(p+q+1).                       (2)
```

This is the leading block for nodal values and derivative jets of `G_x` at a multiple shifted zero.

## 2. Invertibility theorem

### Lemma 72.325

If `Re a_j>0` and the `a_j` are distinct modulo the `+-` representative choice, then `C_conf` is
invertible.

### Proof

Assume a vector of coefficients `c_{j,p}` lies in the nullspace. Define the rational function

```text
R(y):=sum_{j,p} c_{j,p} (1/p!) partial_x^p [1/(x+y)]|_{x=a_j}.
```

The nullspace condition says that, for every `k` and `0<=q<m_k`,

```text
(1/q!) partial_y^q R(y)|_{y=a_k}=0.                              (3)
```

Thus `R(y)` has zeros of multiplicity at least `m_k` at each `a_k`.

But `R` has poles only at

```text
y=-a_j,
```

with pole order at most `m_j`. Since

```text
Re(a_k+a_j)=2alpha>0,
```

none of the zeros `a_k` coincides with any pole `-a_j`.

Put everything over the common denominator

```text
D(y):=prod_j (y+a_j)^(m_j).
```

Then

```text
R(y)=N(y)/D(y),
```

where

```text
deg N < M,        M:=sum_j m_j.
```

Condition (3) gives `M` zeros of `N`, counted with multiplicity, at the points `a_k`. Hence `N` is the
zero polynomial. Therefore `R` is identically zero.

The partial fractions of `R` at the distinct poles `-a_j` are unique, so all coefficients `c_{j,p}`
vanish. Thus the nullspace is trivial and `C_conf` is invertible. `QED`

## 3. Consequence for zero-node forcing

For a maximal-real-part cluster with multiplicities, the leading zero-node block is

```text
-diag(e^(a_jL)) C_conf
```

with the appropriate Hermite derivative-row expansion. By Lemma 72.325 it is invertible. Therefore
polynomial errors force all nodal Hermite jets:

```text
G_x^(p)(a_j)=O(e^(-alpha L)L^B),        0<=p<m_j.
```

The exact power `B` may increase with the multiplicity and window, but remains polynomial for fixed
window.

## 4. Updated cluster status

Combining E72.324 and E72.325:

```text
cluster invertibility is closed for finite maximal-real-part clusters, including multiplicity.
```

The remaining nodal theorem is now only:

```text
1. finite Fourier tail bound;
2. outside-window zero contribution;
3. propagation from nodal Hermite suppression to strip PW-Cauchy.
```

## 5. Status

```text
proved: confluent Cauchy maximal cluster is invertible;
closed: multiplicity bookkeeping for the leading zero-node block;
open:   tail, outside-window, and nodal-to-strip propagation.
```
