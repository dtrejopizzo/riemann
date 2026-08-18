# 114.a.75 — H7: signed read-once trees are prime-regular at every depth

```
+-------------------------------------------------------------------------+
| SIGNS       A leaf carries epsilon_i in {+1,-1}.                       |
| DETECT      With only input i active, the output is epsilon_i.          |
| ORTHANT     Put x_i=epsilon_i y_i with every y_i>0.                     |
| REDUCE      The signed evaluation becomes the positive function of a74. |
| HESSIAN     A diagonal sign change preserves the nonzero mixed-Hessian  |
|             graph, so the complete tree is reconstructed recursively.   |
| RESULT      Every signed read-once fiber is prime-regular, uniformly in  |
|             depth and arity.                                            |
| OPEN        Repeated leaves/contractions and genuinely two-sided cuts.   |
+-------------------------------------------------------------------------+
```

## 1. Signed read-once evaluation

Let `T` be a reduced alternating read-once tree as in `a_74`, and attach a
sign

\[
 \varepsilon_i\in\{+1,-1\}                                             \tag{1.1}
\]

to every labelled leaf `i`.  In the real full-bio representation, evaluate
the leaf as `epsilon_i x_i` and use the two transported additions of `a_39`.
Denote the resulting homogeneous function by `F_{T,epsilon}`.

The signed power map fixes `+1,-1`, and zero is the identity for both
additions.  Therefore, for the standard unit vector `e_i`,

\[
 F_{T,\varepsilon}(e_i)=\varepsilon_i.                                 \tag{1.2}
\]

Every other leaf is zero, so all off-path vertices disappear by their unit
relations and the path from leaf `i` to the root is unary.

### Lemma 1.1 (sign recovery)

The represented function determines the complete leaf-sign map
`epsilon:X->{+1,-1}`.

## 2. Orthant reduction to the positive theorem

After recovering `epsilon`, work on the open orthant

\[
 \mathcal O_\varepsilon
 =\{x:\varepsilon_i x_i>0\text{ for every }i\}.                         \tag{2.1}
\]

Write `x_i=epsilon_i y_i`, `y_i>0`.  Every signed leaf then equals

\[
 \varepsilon_i x_i=y_i,                                                 \tag{2.2}
\]

so

\[
 F_{T,\varepsilon}(\varepsilon_1y_1,\ldots,
                    \varepsilon_ny_n)=F_T(y_1,\ldots,y_n),              \tag{2.3}
\]

where `F_T` is exactly the positive unsigned function of `a_74`.

The chain rule gives

\[
 \frac{\partial^2}{\partial y_i\partial y_j}
 F_{T,\varepsilon}(\varepsilon y)
 =\varepsilon_i\varepsilon_j
  \frac{\partial^2F_{T,\varepsilon}}
       {\partial x_i\partial x_j}(\varepsilon y).                      \tag{2.4}
\]

Multiplication by a nonzero sign cannot create or remove an identically
nonzero mixed derivative.  Hence the Hessian graphs used in `a_74` are
preserved by the orthant change.

### Theorem 2.1 (signed Hessian reconstruction)

The real full-bio map is injective on all reduced signed read-once trees,
with no bound on depth or arity.

### Proof

Equality of represented functions gives equality at each `e_i`; Lemma 1.1
therefore gives the same sign map.  Apply the common orthant substitution
(2.3).  The positive functions agree, so Theorem 3.1 of `a_74` recovers the
same unsigned colored tree.  Together with the recovered signs this gives
the same signed tree.  QED.

## 3. Prime cancellation

### Corollary 3.1

For every prime `ell` and signed read-once trees `F,G`,

\[
 \ell F=\ell G\quad\Longrightarrow\quad F=G.                           \tag{3.1}
\]

### Proof

In the real target, first-ruling multiplication by `ell` is multiplication
of the represented function by the nonzero real scalar `ell`.  Cancel it and
apply Theorem 2.1.  QED.

Thus signs alone cannot produce the torsion sought by a counterexample to
H7-PRIME-REG.

## 4. Remaining exact gate

The signed read-once theorem is still one-sided: every input label occurs
once in one rooted operation tree.  Haran's full prop representation
contains an input tree and an output tree, a signed leaf bijection,
contractions/repeated uses, and equivalences produced by changing cuts.

The residual statement is now

> **H7-RF-BICUT.** Prove prime cancellation for repeated/contracted,
> genuinely two-sided signed tree data modulo cut-commutativity, on a
> cofinal affine pro-cover.

Any failure of H7-PRIME-REG must use one of those bilateral or contraction
features; it cannot occur in a signed one-sided read-once tree of any size.

## 5. Verification scope

`114_a_75_h7_signed_read_once_verify.py` checks exact sign recovery,
orthant substitution, Hessian-support invariance under every sign pattern
through ten leaves, and the scope boundary.  The verifier does not assert
H7-RF-BICUT.

