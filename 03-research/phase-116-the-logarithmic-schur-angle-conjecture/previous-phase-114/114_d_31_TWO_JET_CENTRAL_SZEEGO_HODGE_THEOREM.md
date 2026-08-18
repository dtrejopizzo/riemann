# D.31 — Two-jet central Szegő Hodge theorem

## Status

This note repairs the weight mismatch isolated in D.27.  At the central
weight `p^(-1/2)` the one-jet argument diverges, but the divergence is
confined to the first Hardy tail coefficient.  Removing the two canonical
jets `1,z` leaves a uniformly contractive tail and gives a strict
codimension-two Hodge theorem with the exact central weight.

This is an independent finite/cofinal Hodge theorem.  It is not row D.
D.32 proves that the full prime-power contact has infinite rank already at
one prime and therefore cannot factor through this one-column-per-prime
space.  The theorem remains a correct finite Hodge model, but the comparison
target for A--C must be a Gamma-coupled vector-valued enlargement.

## 1. Central Szegő vectors and their two jets

For a prime `p`, put

```text
r_p=p^(-1/2),
h_p(z)=sqrt(1-r_p^2)/(1-r_p z) in H^2(D).            (1.1)
```

Then `||h_p||=1`, and its coefficient of `z^k` is a fixed scalar
multiple of `p^(-k/2)`, the central coefficient of the full tower `p^k`.
Write

```text
h_p=a_p 1+b_p z+R_p,
a_p=sqrt(1-p^(-1)),
b_p=p^(-1/2)sqrt(1-p^(-1)),
R_p perpendicular to span{1,z}.                     (1.2)
```

The exact tail norm is

```text
||R_p||^2
 =(1-r_p^2) sum_(k>=2) r_p^(2k)
 =r_p^4=p^(-2).                                     (1.3)
```

Thus the critical divergence `sum_p p^(-1)` found in D.27 is precisely the
first-winding `z`-jet.  After retaining that jet as a second boundary
coordinate, all higher prime powers remain in the square-summable tail.

## 2. The finite form

For a finite set `S` of primes let `E_S=R[S]` with orthonormal basis `e_p`,
and define

```text
J_S e_p=h_p,
q_S(v,w)=<J_Sv,J_Sw>-<v,w>,                          (2.1)
d_0(v)=sum_(p in S) a_p v_p,
d_1(v)=sum_(p in S) b_p v_p.                         (2.2)
```

Let `R_S:E_S -> H^2 ominus span{1,z}` be given by `R_Se_p=R_p`.
Orthogonality of the three Hardy pieces gives the exact identity

```text
q_S(v,v)=|d_0(v)|^2+|d_1(v)|^2+||R_Sv||^2-||v||^2. (2.3)
```

## 3. Uniform two-ruling Hodge theorem

### Theorem 3.1

For every finite `S` and every

```text
v in ker(d_0) intersect ker(d_1),                    (3.1)
```

one has

```text
q_S(v,v)
 <= -(1-1627/2640)||v||^2
 =  -(1013/2640)||v||^2.                             (3.2)
```

In particular the primitive restriction is strictly negative and equality
occurs only for `v=0`.  The estimate is uniform under all finite-support
inclusions.

### Proof

By (1.3),

```text
||R_S||^2 <= ||R_S||_HS^2
 =sum_(p in S)p^(-2)
 <sum_p sum_(k>=1)p^(-2k)
 =sum_p 1/(p^2-1).                                   (3.3)
```

Separating `p=2,3,5,7` and bounding the remaining primes by all integers
`n>=11` gives

```text
sum_p 1/(p^2-1)
 < 1/3+1/8+1/24+1/48
   +1/2(1/10+1/11)
 =1627/2640<1.                                       (3.4)
```

On (3.1), identity (2.3) becomes

```text
q_S(v,v)=||R_Sv||^2-||v||^2,
```

and (3.2) follows from (3.3)--(3.4).  Strictness and compatibility with
finite-support inclusions are immediate.

## 4. Meaning of the repair

D.20 proved a one-boundary theorem with the subcritical parameter `n^(-1)`.
D.27 correctly showed that its proof fails at `p^(-1/2)` because the whole
one-boundary tail has squared mass `sum_p p^(-1)`.  The present theorem does
not contradict that audit: it changes the boundary type.  At the central
weight one must retain two jets,

```text
coefficient of 1,     coefficient of z,              (4.1)
```

and impose two primitive equations.  The remaining tail again has the
subcritical mass `sum_p p^(-2)`.

This is structurally aligned with row A, which has two ruling degrees, and
with the primitive test space, which has the two moments at `+1/2` and
`-1/2`.  No zero of zeta or sign of the nuclear form enters Theorem 3.1.

## 5. Comparison audit

The initially proposed comparison would require, from the periodic Yoneda
sections, Witt correspondences, torsor filtration and Gamma boundary, a map

```text
J_2jet : T_mix -> colim_S E_S (or a vector-valued enlargement)             (5.1)
```

such that

```text
(d_0,d_1) J_2jet(F)
   =(integral e^(t/2)F(t)dt, integral e^(-t/2)F(t)dt),                     (5.2)
q(J_2jet(F),J_2jet(G))=B_nuc(F,G).                         (5.3)
```

Equations (5.2)--(5.3) are comparison theorems, not definitions.  The
important improvement is that their target now has the correct central
weight and already satisfies the required strict Hodge sign independently.

D.32 proves that no local, one-scalar-per-prime map can satisfy (5.3) while
retaining all powers `p^k`: the local translation kernel has infinite rank,
and the natural Hardy orbit enlargement even has positive vectors with its
first two coefficient jets zero.  Hence (5.1)--(5.3) are not the live gate
for this scalar space.  The live gate is the global vector-valued contraction
in D.32(7.1), after finite and Gamma boundaries have been coupled.
