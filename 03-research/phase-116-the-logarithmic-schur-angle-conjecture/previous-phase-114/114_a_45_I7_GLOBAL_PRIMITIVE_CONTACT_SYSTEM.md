# 114.a.45 — I7 positive: the global primitive contact system realizes all `Lambda(n)`

```
+--------------------------------------------------------------------------+
| LOCAL       P_{p,k}=p^(k-1)Z/p^k Z is canonically F_p.                  |
| GLOBAL      P_n=tensor_{p^k||n} P_{p,k}.                                |
| CANCELLATION F_p tensor_Z F_q=0 for p!=q.                               |
| MASS        log #P_n is log p for n=p^k and 0 otherwise: Lambda(n).     |
| COMPOSE     P_m tensor_Z P_n is canonically P_mn for all m,n.           |
| STATUS      Arithmetic labels, local mass and composition are closed in  |
|             finite contact modules; geometric transport to Haran remains.|
+--------------------------------------------------------------------------+
```

## 1. Definition

For every prime power `p^k`, `k>=1`, take the primitive contact layer of
`a_44`:

\[
 P_{p,k}=p^{k-1}\mathbb Z/p^k\mathbb Z\simeq\mathbb F_p.                 \tag{1.1}
\]

Set `P_1=Z`. For `n>1`, define

\[
 P_n:=\bigotimes_{p^k\parallel n}^{\mathbb Z} P_{p,k}.  \tag{1.2}
\]

This uses the prime tensor decomposition of the Witt algebra in Haran
2022, (12.18), but only the elementary finite modules (1.1) enter the
definition.

## 2. Exact multi-prime cancellation

For positive integers `a,b`,

\[
 \mathbb Z/a\mathbb Z\otimes_{\mathbb Z}\mathbb Z/b\mathbb Z
 \simeq\mathbb Z/(a,b)\mathbb Z.                       \tag{2.1}
\]

Thus

\[
 \mathbb F_p\otimes_{\mathbb Z}\mathbb F_q=0
 \quad(p\ne q),qquad
 \mathbb F_p\otimes_{\mathbb Z}\mathbb F_p\simeq\mathbb F_p.           \tag{2.2}
\]

### Theorem 2.1

For every `n>1`,

\[
 \boxed{
 P_n\simeq
 \begin{cases}
  \mathbb F_p,&n=p^k,\\
  0,&n\text{ has at least two distinct prime divisors}.
 \end{cases}}                                           \tag{2.3}
\]

### Proof

If `n=p^k`, (1.2) has the single factor (1.1). If two distinct primes occur,
their factors tensor to zero by (2.2), and the full tensor product is zero.
QED.

## 3. Exact von Mangoldt mass for every label

For a finite module, let `#0=1`, since the zero module contains its single
zero element. Define

\[
 I_{\rm cont}(n):=\log\#P_n\qquad(n>1).                 \tag{3.1}
\]

### Theorem 3.1

\[
 \boxed{\quad I_{\rm cont}(n)=\Lambda(n)\quad(n>1).\quad}                \tag{3.2}
\]

### Proof

Theorem 2.1 gives `#P_n=p` for `n=p^k` and `#P_n=1` otherwise. Taking
logarithms is exactly the definition of the von Mangoldt function. QED.

This realizes the vanishing for multi-prime labels by an actual tensor
annihilation, not by assigning zero after the fact.

## 4. Compatibility with correspondence composition

### Theorem 4.1

There are canonical isomorphisms

\[
 \boxed{\quad
 P_m\otimes_{\mathbb Z}P_n\xrightarrow{\sim}P_{mn}
 \quad(m,n\ge1),                                       \tag{4.1}
\]

associative, symmetric and unital with `P_1=Z`.

### Proof

If either label has at least two prime divisors, both sides are zero. If
`m=p^a,n=p^b` have the same prime, both sides are canonically `F_p` by
`F_p tensor F_p=F_p`. If their primes differ, both sides are zero by (2.2).
The cases involving `1` are the tensor unit identities. These canonical
tensor identifications inherit associativity and symmetry from finite
`Z`-modules. QED.

Therefore the assignment

\[
 n\longmapsto P_n                                      \tag{4.2}
\]

is a symmetric monoidal contact realization of the semigroup law
`Gamma_m^op Gamma_n^op=Gamma_mn^op` from `a_36`.

Notice that logarithmic cardinality is not additive under (4.1) when the
same prime is repeated; this is correct because `Lambda(p^{a+b})=log p`, not
`2log p`.

## 5. What remains geometric

The modules `P_n` arise canonically from character-branch contacts in the
Witt orders, and their composition/mass now match every operator label. The
remaining I7 gate is no longer arithmetic cancellation:

> **H7-WCONTACT.** Construct on Haran's literal square a symmetric monoidal
> kernel/correspondence functor sending `P_n` to the derived incidence module
> of `(Gamma_n,Delta)`, sending `P_{p,k}=F_p` to the literal carrier
> `Delta cap V_p=Spec F_p` of `a_17`, and preserving (4.1).

Such a functor would close H7-WNODE-COMP and H7-WLEF-cyc simultaneously.
The equality of the finite modules and masses does not itself construct the
global cycles `Gamma_n` or their intersection product.

## 6. Verification scope

`114_a_45_i7_global_contact_verify.py` checks the tensor-gcd formula, all
prime-support cases, `Lambda(n)` through a large range and associativity of
the module labels. It does not assert H7-WCONTACT.
