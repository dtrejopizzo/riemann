# 114.a.23 — H7: variable-arity entropy is not quadratic `h^0`

```
+--------------------------------------------------------------------------+
| AUDIT       The 2^N families of a_21--a_22 are genuine operations.       |
| NO-GO       Choosing input arity N=mn manufactures quadratic entropy.    |
| WITNESS     A one-dimensional ordinary contraction module already has   |
|             2^d bounded binary rows whenever d<=R^2.                    |
| CONSEQUENCE Raw cardinality in a varying arity cannot certify a4.        |
| NEW GATE    Fix an intrinsic rank/arity budget or compute minimal         |
|             generator dimension before applying H7-K.                   |
+--------------------------------------------------------------------------+
```

## 1. Exact arity-inflation theorem

Let `R>=1`.  In the ordinary Euclidean contraction prop, consider for each
`d>=1` the row operators

\[
 t_\epsilon=R^{-1}(\epsilon_1,\ldots,\epsilon_d):
 \mathbb R^d\longrightarrow\mathbb R,
 \qquad \epsilon\in\{0,1\}^d.                            \tag{1.1}
\]

### Theorem 1.1

If `d<=R^2`, all `2^d` operators (1.1) are contractions.  Hence choosing
`d=floor(R^2)` gives

\[
 \log\#\{t_\epsilon\}=\lfloor R^2\rfloor\log2.           \tag{1.2}
\]

### Proof

The Euclidean operator norm of a row is its Euclidean length, so

\[
 \|t_\epsilon\|_{\rm op}
 =R^{-1}\sqrt{\epsilon_1+\cdots+\epsilon_d}
 \le R^{-1}\sqrt d\le1.                                  \tag{1.3}
\]

Different binary words give different rows. QED.

For `R=p^m q^n`, the right side of (1.2) is exponential in `m+n`, far larger
than the desired quadratic law.  Selecting instead `d=2mn` merely truncates
this generic arity effect at a convenient place.

## 2. Application to `a_21`--`a_22`

The operations `T_epsilon:[2N]->[1]` in `a_22` are genuinely distinct and
their construction is useful: it proves that non-total commutativity survives
one-output scalarization.  But the implication written conditionally there,

\[
 \#\mathcal O_Y(\mathcal B_{m,n})_{2mn}\ge2^{mn},          \tag{2.1}
\]

would be a statement about a component whose input arity was chosen to be
`2mn`.  It is not by itself a statement about:

- the scalar component `d_1=1`;
- the minimal number of generators of the section module;
- a theta count in a fixed intrinsic lattice;
- or an arity-normalized absolute dimension.

There is a second obstruction.  Every `T_epsilon` is obtained from the same
two operations `v_1,v_2`, zero, direct sum and one outer addition.  Thus raw
cardinality of their closure does not imply that `Omega(N)` independent module
generators are necessary.  A small generating set can have a very large
operadic closure.

### Corollary 2.1 (status correction)

`114_a_22` closes only the **one-output typing** of the generic defect.  It
does not close the load-bearing H7-S realization of quadratic `h^0`.

## 3. Corrected H7 section acceptance test

Before a mixed family can pass H7-K, it must specify one of the following and
prove its compatibility with degree:

1. **fixed scalar route:** work in `O(B_{m,n})_1` and obtain
   `exp(Theta(mn))` elements there;
2. **intrinsic-rank route:** construct canonically determined ranks
   `r_{m,n}=Theta(m+n)` and apply a proper radius
   `log R_{m,n}=Theta(m+n)`, then compute a minimal-generator invariant such
   as the one in `114_a_11`;
3. **normalized-arity route:** define and prove an arity-normalized dimension
   theorem that prevents the inflation in Theorem 1.1.

In every route, the rank/arity is part of the geometry and may not be selected
after seeing the desired asymptotic.

The most compatible route with the already closed G-1 theorem is (2).  Its
new exact gate is:

> **H7-R.** Extract from the bidegree `(m,n)` an intrinsic section lattice
> `I_{r_{m,n}}(R_{m,n})` with `r_{m,n}=Theta(m+n)` and
> `log R_{m,n}=Theta(m+n)`, and prove that Haran equivalence preserves its
> minimal-generator dimension.

## 4. Verification scope

`114_a_23_h7_arity_inflation_verify.py` checks Theorem 1.1 and contrasts the
quadratic truncation with the full admissible arity.  This verifier does not
construct H7-R.
