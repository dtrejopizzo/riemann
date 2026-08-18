# 114.a.133 — I7 no-go: diagonal Chow multiples cannot carry Lambda

```
+------------------------------------------------------------------------+
| ASSUME      Gamma_n is an undecorated Chow-type cycle supported on the  |
|             irreducible diagonal, hence Gamma_n=k(n) Delta.             |
| COMPOSE     Gamma_m o Gamma_n=Gamma_mn forces k(mn)=k(m)k(n).           |
| INTERSECT   Bilinearity gives <Gamma_n,Delta>=k(n)<Delta,Delta>.         |
| CONFLICT    Lambda(p)=Lambda(p^2)=log p contradicts multiplicativity,   |
|             and different primes rule out the remaining constant case.  |
| RESULT      A viable undecorated lift must move or thicken its support;  |
|             diagonal multiplicity cannot replace the torsor decoration. |
+------------------------------------------------------------------------+
```

## 1. The diagonal-supported Chow hypothesis

Let `C` be any correspondence theory in which:

1. cycles supported on the irreducible diagonal are the free group
   `Z Delta`;
2. the diagonal is the identity correspondence and composition is bilinear;
3. intersection with the diagonal is additive in the first variable.

These are the minimal properties of an ordinary undecorated Chow-type
correspondence theory.  Suppose

\[
 \Gamma_n=k(n)\Delta,\qquad k(n)\in\mathbb Z,                          \tag{1.1}
\]

satisfies

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{mn},\qquad\Gamma_1=\Delta.             \tag{1.2}
\]

Since `Delta o Delta=Delta`, bilinearity gives

\[
 k(mn)=k(m)k(n),\qquad k(1)=1.                                       \tag{1.3}
\]

Thus the multiplicity is a completely multiplicative integer function.

## 2. Incompatibility with von Mangoldt contact

Put

\[
 c=\langle\Delta,\Delta\rangle.                                      \tag{2.1}
\]

Additivity of intersection forces

\[
 \langle\Gamma_n,\Delta\rangle=k(n)c.                               \tag{2.2}
\]

### Theorem 2.1 (diagonal-multiple no-go)

There are no `k:N^x->Z` and `c in R` satisfying (1.3) and

\[
 k(n)c=\Lambda(n)\qquad(n>1).                                        \tag{2.3}
\]

### Proof

For any prime `p`, equations (2.3) at `p` and `p^2` give

\[
 k(p)c=\log p,\qquad k(p)^2c=\log p.                                 \tag{2.4}
\]

The right side is nonzero, so `c!=0` and `k(p)!=0`.  Subtracting gives
`k(p)(k(p)-1)c=0`, hence `k(p)=1`.  Then (2.4) says `c=log p` for every
prime `p`, impossible for two distinct primes.  QED.

The contradiction does not use faithfulness; even a nonfaithful
diagonal-multiple family cannot have the required contact values.

## 3. Consequence for the live dynamic route

The decorated diagonal kernels of `a70` evade the theorem because their
arithmetic information lies in `T_n`, not in the cycle multiplicity, and
their contact is the nonlinear monoidal shadow `P_n` rather than a fixed
self-intersection multiple.

If the final acceptance test insists on an undecorated cycle with an
ordinary bilinear intersection, its carrier must therefore do at least one
of the following:

1. move away from the diagonal for some `n`;
2. carry a nontrivial scheme-theoretic thickening or derived structure not
   classified by `Z Delta`;
3. live in a larger correspondence theory whose contact is not ordinary
   intersection with a fixed diagonal class.

The prime ruling option is already excluded by `a48`.  Hence the exact
remaining gate is:

> **H7-DYNAMIC-THICKENING.** Construct a faithful commutative family of
> nontrivial diagonal thickenings or moving supports whose convolution is
> multiplicative and whose derived reduced contact is `P_n`.

This closes the undecorated **diagonal Chow-multiple** route negatively.  It
does not rule out H7-DYNAMIC-THICKENING, close row A, or prove RH.

## 4. Verification scope

`114_a_133_i7_diagonal_chow_nogo_verify.py` exhausts multiplicative integer
labels on bounded prime powers and checks the symbolic two-prime
contradiction and scope markers.  The theorem is the exact algebraic proof
above, not a numerical extrapolation.
