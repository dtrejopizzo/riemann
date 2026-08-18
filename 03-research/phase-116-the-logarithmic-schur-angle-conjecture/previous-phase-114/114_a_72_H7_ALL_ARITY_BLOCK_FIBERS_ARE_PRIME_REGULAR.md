# 114.a.72 — H7: every generic block fiber is prime-regular

> **Extension (`a_73`).** Boolean one/two-point probes extend the cubic
> argument from independent blocks to every alternating read-once tree of
> depth at most two and arbitrary arity.  The remaining target is H7-RF-DEEP.

```
+-------------------------------------------------------------------------+
| FAMILY      V_epsilon:[2N]->[N] and T_epsilon:[2N]->[1] from a21/a22.  |
| SAME FOLD   All binary words epsilon have the same diagonal fold.       |
| TARGET      One auxiliary finite twisted-field bio with cubic twist.    |
| SEPARATE    delta_1(1,1)=2 while delta_2(1,1)=8.                        |
| CANCEL      Choose auxiliary characteristic q different from the prime  |
|             ell; multiplication by ell is injective in the target.      |
| RESULT      ell V_epsilon=ell V_eta, or ell T_epsilon=ell T_eta, forces  |
|             epsilon=eta for every N.                                   |
| OPEN CORE   Nested/cut-related tree pairs not admitting block recovery. |
+-------------------------------------------------------------------------+
```

## 1. Keep the full bio evaluation, not only its scalar moment

Let

\[
 A=\mathbb Z\boxtimes_{\mathbb F\{\pm1\}}\mathbb Z
\]

and denote its two binary additions by `delta_1,delta_2`.  The constructions
`a_49` and `a_51` provide, for a finite field `F_q` and an exponent `s`
coprime to `q-1`, a map of full bios

\[
 E_{q,s}:A\longrightarrow\mathcal D_{q,s}.                            \tag{1.1}
\]

Its unary scalar shadow is what enters the odd-moment count, but (1.1) also
retains operations in every arity.  In the first factor `delta_1` becomes
ordinary addition.  In the second it becomes

\[
 x+_{(s)}y=
 \left(x^{s^{-1}}+y^{s^{-1}}\right)^s,                                \tag{1.2}
\]

where `s^{-1}` is computed modulo `q-1` and zero is fixed.

Fix a prime `ell` whose regularity on the Haran plane is being tested.
Choose an auxiliary prime

\[
 q>\max(8,\ell),\qquad q\equiv2\pmod3.                                \tag{1.3}
\]

Such primes exist by Dirichlet's theorem.  Then `3` is invertible modulo
`q-1`, so the cubic target `E_{q,3}` exists.  At the input `(1,1)`,

\[
 E_{q,3}(\delta_1)(1,1)=2,
 \qquad E_{q,3}(\delta_2)(1,1)=8.                                     \tag{1.4}
\]

They are distinct because `q>8`.

## 2. Separation in arbitrary block arity

Recall from `a_21`

\[
 V_\epsilon=\bigoplus_{k=1}^N\delta_{\epsilon_k}:
 [2N]\longrightarrow[N],\qquad \epsilon\in\{1,2\}^N,                \tag{2.1}
\]

and from `a_22`

\[
 T_\epsilon=a_N^{(1)}\circ V_\epsilon:[2N]\longrightarrow[1].       \tag{2.2}
\]

### Theorem 2.1 (full-bio block separation)

For every `N`, the single map `E_{q,3}` is injective on both families
`{V_epsilon}` and `{T_epsilon}`.

### Proof

For `V_epsilon`, project onto output block `k`, set all other inputs to zero,
and put `(1,1)` in block `k`.  The resulting value is `2` if
`epsilon_k=1` and `8` if `epsilon_k=2`, by (1.4).  Hence the image recovers
every bit.

For `T_epsilon`, use the zero-insertion `j_k` of `a_22`.  Its exact recovery
identity

\[
 T_\epsilon j_k=\delta_{\epsilon_k}                                  \tag{2.3}
\]

is preserved by the bio map.  Evaluation at `(1,1)` again recovers the
`k`-th bit.  QED.

This proof uses higher-arity target operations.  Unary odd moments alone do
not establish Theorem 2.1.

## 3. Prime cancellation on the whole block fiber

In the homogeneous endomorphism bio over `F_q`, first-ruling multiplication
by `ell` is pointwise multiplication of functions by the nonzero scalar
`ell mod q`.  It is therefore injective in every arity.

### Theorem 3.1 (block PRIME-REG)

For every prime `ell`, every `N`, and all binary words `epsilon,eta`,

\[
 \ell V_\epsilon=\ell V_\eta\Longrightarrow\epsilon=\eta,
 \qquad
 \ell T_\epsilon=\ell T_\eta\Longrightarrow\epsilon=\eta.            \tag{3.1}
\]

### Proof

Apply `E_{q,3}`.  Cancel the nonzero scalar `ell` in the finite target, then
apply Theorem 2.1.  QED.

All the operations in either family have a common diagonal fold.  Thus
Theorem 3.1 proves H7-RF-FOLD on the exponential same-fold fibers constructed
in `a_21` and on their one-output scalarizations from `a_22`, uniformly in
their growing arity.

The same argument applies to any family possessing functorial block
extractions whose recovered primitive operations are `delta_1` or
`delta_2`.

## 4. What remains of H7-RF-FOLD

This removes three possible sources of prime torsion:

1. direct sums of independent off-diagonal bits;
2. passage to a single output by the first addition;
3. unbounded input/output arity by itself.

It does not give a faithful evaluation on every tree class.  A general
representative can contain alternating nested vertices, contractions and
the cut-commutativity relation (10.17), with no block projection recovering
its internal choices.  The remaining exact target is:

> **H7-RF-NEST.** Finite full-bio evaluations of auxiliary characteristic
> separate same-fold pairs of nested reduced tree operations, compatibly
> with cut-commutativity, on an affine cover at every pro-level.

H7-RF-NEST implies H7-RF-FOLD of `a_71`, hence H7-PRIME-REG.  Neither the
odd-Vandermonde scalar theorem nor Theorem 3.1 proves H7-RF-NEST.

## 5. Verification scope

`114_a_72_h7_all_arity_block_regular_verify.py` checks exact transported
field laws, the `2/8` witness, exhaustive word recovery through arity 24,
common folds and cancellation for many tested principal and auxiliary
primes.  The proof of Theorems 2.1--3.1 is uniform in `N`; the verifier does
not assert H7-RF-NEST.

Primary construction sources are `a_21`, `a_22`, `a_49` and `a_51`.
