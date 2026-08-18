# 114.a.107 — H7: the scalar universal differential has exactly one Z/2 anomaly

```
+------------------------------------------------------------------------+
| OBJECT      (C Omega(F(Z)/F{+-1}))_(1,1).                              |
| CLASSIFY    Homogeneous symmetric 2-cocycles on Z are arithmetic        |
|             derivatives, freely determined at the positive primes.      |
| RESULT      C Omega_(1,1) = D_left direct-sum D_right direct-sum Z/2,   |
|             D = direct-sum_p Z d_p.                                     |
| CLOSED      Odd-prime regular; the unique integral anomaly is 2-torsion. |
| LIMIT       This does not prove scalar-ring H7-AUG-FLAT or all arities.  |
+------------------------------------------------------------------------+
```

## 1. Arithmetic derivations

Let

\[
 D=\bigoplus_{p\ {m prime}}\mathbb Z\,d_p.                  \tag{1.1}
\]

Define `partial:Z->D` by `partial(0)=partial(+-1)=0`, oddness, and for
`n>1`,

\[
 \partial n=\sum_{p\mid n}v_p(n)\frac{n}{p}\,d_p.             \tag{1.2}
\]

Then

\[
 \partial(mn)=m\partial n+n\partial m.                        \tag{1.3}
\]

Put

\[
 c(a,b)=\partial a+\partial b-\partial(a+b).                   \tag{1.4}
\]

It is a normalized symmetric additive two-cocycle.  From (1.3),

\[
 c(\lambda a,\lambda b)=\lambda c(a,b)                        \tag{1.5}
\]

for every integer `lambda`.

## 2. Classification lemma, including the sign anomaly

### Lemma 2.1

For any abelian group `M`, homogeneous normalized symmetric two-cocycles

\[
 f:\mathbb Z\times\mathbb Z\longrightarrow M,qquad
 f(\lambda a,\lambda b)=\lambda f(a,b),                       \tag{2.1}
\]

are naturally in bijection with arbitrary families `(m_p)_{p prime}` in
`M` together with an element `t in M[2]`.  For positive `n` the family gives

\[
 q(n)=\sum_{p\mid n}v_p(n)\frac{n}{p}m_p,qquad
 f(a,b)=q(a)+q(b)-q(a+b),                                    \tag{2.2}
\]

and for `n>0` the extension to negative integers is

\[
 q(-n)=-q(n)+nt.                                               \tag{2.3}
\]

### Proof

Because `Z` is free abelian, every normalized symmetric two-cocycle is a
coboundary.  Explicitly, set `q(0)=q(1)=0` and recursively choose

\[
 q(n+1)=q(n)-f(n,1)                                           \tag{2.4}
\]

for positive `n`, extending to negative integers through the cocycle and
symmetry identities.  Then `f=delta q`; the normalization `q(1)=0` removes
the ambiguity by an additive homomorphism.

Homogeneity says that

\[
 r_\lambda(n)=q(\lambda n)-\lambda q(n)                       \tag{2.5}
\]

has zero coboundary, hence is additive in `n`.  Evaluating at `1` gives
`r_lambda(n)=n q(lambda)`, so

\[
 q(\lambda n)=\lambda q(n)+nq(\lambda).                       \tag{2.6}
\]

Taking `lambda=n=-1` in (2.6) gives `2q(-1)=0`; put `t=q(-1)`.
Equation (2.6) then gives (2.3).  Thus `q` is an arithmetic derivation of
the multiplicative monoid of integers.  Unique factorization and repeated
use of (2.6) give (2.2), with `m_p=q(p)`.  Conversely (2.2)--(2.3), for an
arbitrary `t in M[2]`, obey (2.6), and their coboundary satisfies all
conditions in (2.1).  QED.

No divisibility in `M` was used; the coefficient `n/p` in (2.2) is integral.
The parameter `t=f(1,-1)` is the only possible torsion anomaly.

## 3. Exact scalar differential group

Let `Omega_C=C Omega(F(Z)/F{+-1})`.  Haran's scalar presentation has two
generator types.  Define

\[
 \Theta([a,a'|b])=(b\,c(a,a'),0),\qquad
 \Theta([a|b,b'])=(0,a\,c(b,b'))                             \tag{3.1}
\]

in `D_left direct-sum D_right`.

### Theorem 3.1

\[
 (\Omega_C)_{1,1}\xrightarrow{\ \sim\ }
 D_{\rm left}\oplus D_{\rm right}\oplus\mathbb Z/2\,\tau.    \tag{3.2}
\]

### Proof

The relations with a scalar in the third slot give

\[
 [a,a'|b]=b[a,a'|1],\qquad [a|b,b']=a[1|b,b'].                \tag{3.3}
\]

For each orientation, zero, symmetry and associativity say exactly that the
remaining two-variable symbol is a normalized symmetric two-cocycle;
scalar transfer is its homogeneity.  Lemma 2.1 initially gives one copy of
`D direct-sum Z/2` for each orientation.

The almost-linear relation imposes no further coupling: under (3.3), both
sides separately equal

\[
 (b_1+b_2)c_L(a_1,a_2)+(a_1+a_2)c_R(b_1,b_2).                \tag{3.4}
\]

Let `t_L,t_R` be the two order-two parameters.  The cancellation relation

\[
 [a|b,-b]+[a,-a|b]=0                                      \tag{3.5}
\]

evaluates to `ab(t_R+t_L)=0`, and at `a=b=1` gives exactly
`t_R+t_L=0`.  Since both have order two, they become one common class
`tau`; no free-prime coordinate is affected.  The sign relations are the
negative-scalar instance of homogeneity.  Thus the presentation is exactly
the direct sum in (3.2).  QED.

For example,

\[
 [1,1|1]\longmapsto(-d_2,0,0),\qquad
 [1|1,1]\longmapsto(0,-d_2,0),                              \tag{3.6}
\]

while

\[
 [1,-1|1]=-[1|1,-1]\longmapsto\tau.                         \tag{3.7}
\]

This strengthens `a106`: its entropy cocycle is obtained from (3.2) by
`d_p -> p e_p` and then optionally `e_p -> log p`.

### Corollary 3.2

The universal scalar differential group is regular for every odd prime.
Multiplication by `2` kills exactly the `Z/2` summand in (3.2), so the
integral universal scalar first-jet target is not 2-regular.  Its
rationalization in `a106` removes precisely this anomaly.

## 4. Scope for PRIME-REG

The result completely determines integral differential torsion in scalar
arity: it is exactly one `Z/2`.  It does not prove 2-torsion in the scalar
ring or failure of H7-AUG-FLAT; torsion in a cotangent module does not imply
torsion in its source algebra.  H7-AUG-FLAT concerns the scalar ring's fold
augmentation ideal itself.  The theorem also says nothing yet about torsion
in `Omega_C` for `(Y,X)!=(1,1)` or about nonlinear/higher-order equality
kernels.

Thus H7-PRIME-REG and row A remain open.  For odd primes the remaining scalar
collision, if one exists, is invisible even to the integral universal first
jet.  At `p=2`, the class `tau` is the exact first-order obstruction that
must be shown not to integrate to a source collision (or be realized as one).
The all-arity route still requires p-CONVEX/p-DIVPATH or higher jets.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Theorem 7.8.1.

## 5. Verification scope

`114_a_107_h7_scalar_differential_z2_verify.py` checks the universal
arithmetic derivative, the order-two sign cocycle, homogeneity and all
coupled scalar relations exactly on bounded integer boxes, as well as the
two independent free-prime images and their single shared torsion class.
Lemma 2.1 supplies the unbounded classification proof.

**Integration in the plane (`a108`).**  The class `tau` is not merely a
cotangent warning: `kappa=(1,-1)_1 o (1,1)_2^t` maps to it under the
universal jet, while a wire swap gives `2kappa=0`.  Hence `kappa` is actual
nonzero scalar 2-torsion and H7-PRIME-REG fails.
