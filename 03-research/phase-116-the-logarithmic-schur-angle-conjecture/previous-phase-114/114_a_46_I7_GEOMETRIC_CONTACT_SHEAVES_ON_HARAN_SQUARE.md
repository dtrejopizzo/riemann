# 114.a.46 — I7 positive: geometric contact sheaves on Haran's literal square

> **Dynamic refinement (`a_70`).** H7-CYCLE-LIFT is now closed in the
> Picard-decorated span category: diagonal carriers decorated by `T_n`
> compose faithfully and have `P_n` as monoidal contact. The stronger demand
> for distinct undecorated Chow-type cycles remains open.

```
+--------------------------------------------------------------------------+
| SUPPORT     Z_p=Delta cap V_p=Spec F_p is the literal incidence of a_17. |
| SHEAF       M_p=(i_p)_* F_p on the underlying site of the Haran square.  |
| GLOBAL      M_n=tensor_{p|n} M_p is M_p for n=p^k and zero otherwise.    |
| MASS        log #Gamma(Y,M_n)=Lambda(n).                                |
| COMPOSE     M_m tensor M_n is canonically M_mn.                          |
| GAIN        The complete primitive contact system of a_45 is now         |
|             geometrically supported on the literal square.               |
| OPEN        Lift M_n to actual correspondence cycles Gamma_n and an      |
|             intersection/RR theory.                                      |
+--------------------------------------------------------------------------+
```

## 1. Literal supports

Let

\[
 Y=X\times_{\operatorname{Spec}\mathbb F\{\pm1\}}X.   \tag{1.1}
\]

For every rational prime `p`, Theorem 2.1 of `a_17` gives the closed
incidence

\[
 i_p:Z_p:=\Delta\times_YV_p\hookrightarrow Y,
 \qquad Z_p\simeq\operatorname{Spec}\mathbb F_p.       \tag{1.2}
\]

For distinct primes, these supports are disjoint:

\[
 Z_p\times_YZ_q=\varnothing\qquad(p\ne q),              \tag{1.3}
\]

because their projections to `X` are the distinct ordinary closed points
`x_p` and `x_q`.

## 2. Contact sheaves

Work in the ordinary symmetric monoidal category of sheaves of abelian
groups on the underlying pro-site/topological site of `Y`. This category
exists independently of a missing divisor or coherent-sheaf theory for
generalized schemes.

Define

\[
 \mathcal M_p:=(i_p)_*\underline{\mathbb F_p}.          \tag{2.1}
\]

For `n>1`, put

\[
 \mathcal M_n:=\bigotimes_{p\mid n}^{\mathbb Z}\mathcal M_p,              \tag{2.2}
\]

with one factor per distinct prime, and put `M_1=underline Z`, the tensor
unit.

### Theorem 2.1 (geometric realization of the contact modules)

\[
 \boxed{
 \mathcal M_n\simeq
 \begin{cases}
  (i_p)_*\underline{\mathbb F_p},&n=p^k,\\
  0,&n\text{ has at least two distinct prime divisors}.
 \end{cases}}                                           \tag{2.3}
\]

### Proof

Tensor products of abelian sheaves are computed stalkwise. On `Z_p`,

\[
 \mathbb F_p\otimes_{\mathbb Z}\mathbb F_p\simeq\mathbb F_p.            \tag{2.4}
\]

For `p!=q`, no point belongs to both supports by (1.3), so at every stalk at
least one of `M_p,M_q` is zero; their tensor product is the zero sheaf. The
statement follows. QED.

## 3. Composition and mass

### Theorem 3.1

There are canonical symmetric monoidal isomorphisms

\[
 \boxed{\quad
 \mathcal M_m\otimes_{\mathbb Z}\mathcal M_n
 \xrightarrow{\sim}\mathcal M_{mn}.
 \quad}                                                \tag{3.1}
\]

### Proof

This is the sheaf version of Theorem 4.1 in `a_45`. Equal prime supports use
(2.4), distinct supports give zero, and `M_1` is the tensor unit. Stalkwise
canonical identifications supply associativity and symmetry. QED.

For `n>1`, global sections give

\[
 \Gamma(Y,\mathcal M_n)\simeq
 \begin{cases}
  \mathbb F_p,&n=p^k,\\
  0,&n\text{ has at least two prime divisors}.
 \end{cases}                                           \tag{3.2}
\]

Therefore, counting the single element of the zero group as cardinality
one,

\[
 \boxed{\quad
 \log\#\Gamma(Y,\mathcal M_n)=\Lambda(n).
 \quad}                                                \tag{3.3}
\]

The isomorphism

\[
 P_n\xrightarrow{\sim}\Gamma(Y,\mathcal M_n)          \tag{3.4}
\]

identifies the algebraic contact system of `a_45` with literal geometric
supports on Haran's square.

## 4. Exact remaining cycle lift

The sheaves `M_n` are geometric incidence modules, but they are not cycles
`Gamma_n`. In particular, (3.1) is tensor composition of diagonal-contact
shadows, not composition of correspondences in `Y times_X Y`.

The remaining I7 gate is:

> **H7-CYCLE-LIFT.** Construct correspondence objects `Gamma_n` on Haran's
> square with `Gamma_m compose Gamma_n=Gamma_mn`, together with a derived
> diagonal pullback/intersection functor satisfying
> \[
> L\Delta^*(\Gamma_n)\simeq\mathcal M_n                \tag{4.1}
> \]
> and carrying composition to (3.1).

If H7-CYCLE-LIFT holds, I7's finite local intersection, arithmetic labels,
multi-prime cancellation and composition all agree with the faithful Witt
operator algebra. A global divisor class, archimedean metric and RR theorem
would still be needed for the full row-A package.

`a_61`/`a_66` later give a faithful abstract unit-torsor lift `T_n`
unconditionally. H7-PRIME-REG would promote it to a completed lattice. The
type audit `a_66` retracts the claim that this alone recovers (4.1): a typed
Cartier/module and derived-intersection formalism is still required.
Decorated-span convolution is supplied by `a_70`; undecorated cycle
convolution remains open.

## 5. Verification scope

`114_a_46_i7_geometric_contact_sheaf_verify.py` checks disjoint supports,
stalkwise tensor products, global sections, monoidal composition and
`Lambda(n)` over broad finite ranges. It does not assert H7-CYCLE-LIFT.
