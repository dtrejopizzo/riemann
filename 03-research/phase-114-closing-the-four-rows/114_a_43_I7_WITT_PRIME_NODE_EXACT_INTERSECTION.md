# 114.a.43 — I7 positive: the prime Witt node has exact `log p` intersection

```
+--------------------------------------------------------------------------+
| RING        W_p=Z phi_1 + Z phi_p is Z x_{F_p} Z.                       |
| BRANCHES    The characters F_0 and tr are its two projections to Z.      |
| INTERSECT   The corresponding Spec Z branches meet in exactly Spec F_p.  |
| DEGREE      log #F_p=log p=Lambda(p)=log|Phi_p(1)|.                     |
| CORRECTION  The cyclotomic mass is a branch-intersection invariant, not  |
|             the fixed-locus length of Graph(F_p) cap Delta.              |
| OPEN        Glue this local node into Haran's square and extend           |
|             composition to p^k and general n.                            |
+--------------------------------------------------------------------------+
```

## 1. The rank-two prime Witt algebra

Fix a prime `p` and write

\[
 \mathcal W_p=\mathbb Z e_0\oplus\mathbb Z e_1,
 \qquad e_0=\phi_1=1,quad e_1=\phi_p.                 \tag{1.1}
\]

Specializing Haran 2022, (12.16), to the equal prime-power exponents
`n=m=1` gives

\[
 e_1^2=(p-2)e_1+(p-1)e_0.                              \tag{1.2}
\]

The two ring characters of (12.22)--(12.30) are

\[
 F_0(e_1)=p-1,qquad \operatorname{tr}(e_1)=-1.         \tag{1.3}
\]

## 2. Exact nodal presentation

### Theorem 2.1

The character pair induces a ring isomorphism

\[
 \boxed{\quad
 (F_0,\operatorname{tr}):\mathcal W_p
 \xrightarrow{\sim}
 \mathbb Z\times_{\mathbb F_p}\mathbb Z
 =\{(r,s)\in\mathbb Z^2:r\equiv s\pmod p\}.
 \quad}                                                \tag{2.1}
\]

### Proof

For `a,b in Z`,

\[
 a e_0+b e_1\longmapsto
 (a+b(p-1),a-b).                                       \tag{2.2}
\]

The coordinate difference is `bp`, so the image lies in the fiber product.
Conversely, if `r congruent s mod p`, put

\[
 b=(r-s)/p,qquad a=s+b.                                \tag{2.3}
\]

Then (2.2) is `(r,s)`, proving bijectivity. Both components are ring maps,
so the bijection is a ring isomorphism. Equivalently, (1.2) factors as

\[
 (e_1-(p-1))(e_1+1)=0,                                 \tag{2.4}
\]

with the two roots congruent precisely modulo `p`. QED.

## 3. Literal branch intersection

Put `Z_p^W=Spec W_p`. The two projections in (2.1) give closed immersions

\[
 s_0,s_1:\operatorname{Spec}\mathbb Z
 \hookrightarrow Z_p^W.                               \tag{3.1}
\]

### Theorem 3.1

Their scheme-theoretic intersection is

\[
 \boxed{\quad
 s_0(\operatorname{Spec}\mathbb Z)
 \cap s_1(\operatorname{Spec}\mathbb Z)
 \simeq\operatorname{Spec}\mathbb F_p.
 \quad}                                                \tag{3.2}
\]

### Proof

The intersection coordinate ring is

\[
 \mathbb Z\otimes_{\mathcal W_p}\mathbb Z,            \tag{3.3}
\]

where `e_1` acts by `p-1` on the first factor and by `-1` on the second.
The balanced tensor relation therefore imposes

\[
 (p-1)-(-1)=p=0.                                       \tag{3.4}
\]

There are no further relations, so (3.3) is `Z/pZ`. QED.

Consequently the finite Arakelov mass is

\[
 \deg(s_0\cdot s_1)=\log\#\mathbb F_p
 =\log p=\Lambda(p)=\log|\Phi_p(1)|.                  \tag{3.5}
\]

This is a literal finite intersection, not an assigned weight.

## 4. Reconciliation with the two previous no-go theorems

There is no contradiction with `a_41`: graph/diagonal fixed intersection
imposes `F_p=id` and leaves the horizontal `F_0` branch `Spec Z`. Nor is
there a contradiction with `a_42`: the reduced cone of `1-F_p` has
determinant one.

The correct cyclotomic determinant appears instead as the difference of the
two branch values in (1.3):

\[
 F_0(e_1)-\operatorname{tr}(e_1)=p
 =N_{\mathbb Q(\zeta_p)/\mathbb Q}(1-\zeta_p).         \tag{4.1}
\]

Thus H7-WLEF-cyc has a concrete local geometric model: intersect the
`F_0` branch with the cyclotomic trace branch.

## 5. Interface with Haran's square

`a_17` independently proves on the literal square

\[
 \Delta\cap V_p\simeq\operatorname{Spec}\mathbb F_p.  \tag{5.1}
\]

Equations (3.2) and (5.1) have the same integral branches, residue field and
degree. This supplies the exact local target for H7-WBASE:

> **H7-WNODE.** Construct a compatible local kernel/functor taking the two
> Witt branches `(F_0,tr)` to `(Delta,V_p)` and the node (3.2) to the
> incidence (5.1), then prove compatibility with the operator graph
> composition of `a_36`--`a_37`.

The local intersection/mass clause is now closed for `n=p`. What remains is
the global gluing, prime-power correspondence labels and multiplicative
composition. The equality of residue diagrams alone is not yet such a
functor.

## 6. Verification scope

`114_a_43_i7_witt_prime_node_verify.py` checks the Witt multiplication,
fiber-product isomorphism, character values, balanced tensor intersection
and exact `Lambda(p)` mass over many primes. It does not assert H7-WNODE.
