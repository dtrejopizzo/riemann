# 114.a.58 — H7-DEN-TRANS: ordinary spans, derived base change and Witt lifts fail

```
+--------------------------------------------------------------------------+
| FRESH       Global coverage requires changing p as denominators grow.   |
| SPAN        No nonzero unital ring receives F_p and F_q for p!=q.      |
| DERIVED     F_p tensor^L_Z F_q = 0 for p!=q.                           |
| SELF        For p=q, Tor_1=F_p records self-excess but p is not a unit. |
| WITT        Z_p reduces to F_p; after inverting p it becomes Q_p and    |
|             can no longer reduce to the finite block.                   |
| RESULT      Ordinary/derived unital transitions cannot repair a_57.     |
+--------------------------------------------------------------------------+
```

## 1. No common unital apex in distinct characteristics

### Lemma 1.1

Let `p!=q` be primes. If a unital ring `A` admits unital maps

\[
 \mathbb F_p\longrightarrow A,
 \qquad
 \mathbb F_q\longrightarrow A,                                         \tag{1.1}
\]

then `A` is the zero ring.

### Proof

The first map gives `p*1_A=0`, and the second gives `q*1_A=0`. Choose
integers `u,v` with `up+vq=1`. Then

\[
 1_A=(up+vq)1_A=0.                                                       \tag{1.2}
\]

QED.

Thus there is no nonempty affine-scheme correspondence

\[
 \operatorname{Spec}\mathbb F_p
 \longleftarrow Z\longrightarrow
 \operatorname{Spec}\mathbb F_q                                       \tag{1.3}
\]

over `Spec Z`: its coordinate ring would satisfy (1.1). The opposite diagram
of ring reductions `Z->F_p`, `Z->F_q` exists, but it is only a common source;
it supplies no transition carrying finite moment values from one field to
the other.

## 2. The derived intersection is also empty

Use the free resolution

\[
 0\longrightarrow\mathbb Z\xrightarrow{p}\mathbb Z
 \longrightarrow\mathbb F_p\longrightarrow0.                            \tag{2.1}
\]

Tensoring with `F_q` gives the two-term complex

\[
 [\mathbb F_q\xrightarrow{p}\mathbb F_q].                               \tag{2.2}
\]

If `p!=q`, multiplication by `p` is an isomorphism in `F_q`. Hence every
homology group vanishes:

\[
 \boxed{
 \mathbb F_p\otimes_{\mathbb Z}^{\mathbf L}\mathbb F_q\simeq0
 \qquad(p\ne q).
 }                                                                       \tag{2.3}
\]

Equivalently,

\[
 \operatorname{Tor}^{\mathbb Z}_0(\mathbb F_p,\mathbb F_q)=0,
 \qquad
 \operatorname{Tor}^{\mathbb Z}_1(\mathbb F_p,\mathbb F_q)=0.           \tag{2.4}
\]

For `p=q`, (2.2) has zero differential and

\[
 H_0\simeq H_1\simeq\mathbb F_p.                                       \tag{2.5}
\]

This same-characteristic `Tor_1` is a legitimate self-intersection/excess
class, analogous to the prime-local excess appearing in I7. It cannot move
to a fresh characteristic, and `p` remains noninvertible, so it does not
repair the denominator collision of `a_57`.

## 3. Witt and p-adic lifts give an exact dichotomy

The strict `p`-typical Witt ring satisfies

\[
 W(\mathbb F_p)=\mathbb Z_p,
 \qquad \mathbb Z_p\twoheadrightarrow\mathbb F_p.                       \tag{3.1}
\]

There is no unital section `F_p->Z_p`: it would send the equality `p=0` in
`F_p` to the false equality `p=0` in `Z_p`.

The lift can evaluate every denominator prime to `p`, but not `1/p`. After
inverting `p`,

\[
 \mathbb Z_p[1/p]=\mathbb Q_p,                                          \tag{3.2}
\]

and `1/p` exists. However, no unital reduction `Q_p->F_p` can extend (3.1),
again because `p(1/p)=1` would reduce to `0=1`.

Thus one must choose between:

1. the finite residue block, which cannot cross denominator `p`; or
2. the characteristic-zero local field, which has no reduction retaining
   that finite block.

Finite Witt truncations `Z/p^nZ` have the same obstruction: `p` is nilpotent
or a zero divisor, never a unit.

## 4. Exact consequence for H7-DEN-TRANS

### Theorem 4.1

H7-DEN-TRANS cannot be realized by any of the following while preserving
unital first-addition/multiplication and the finite moment values:

1. a nonzero common ring or affine-scheme span between fresh residue fields;
2. their derived fiber product over `Spec Z`;
3. a Witt or finite `p`-adic lift followed by inversion of the colliding
   denominator and reduction back to the old block.

The proof is Lemma 1.1, (2.3), and the dichotomy (3.1)--(3.2).

The remaining transition possibilities must abandon at least one of these
requirements. Examples of correctly typed but still unconstructed options
are:

- nonunital or additive correspondences rather than ring/bio maps;
- a characteristic-zero adelic/locally compact target with a new dimension,
  not a retained finite quotient;
- determinant or trace data that compare cardinalities without transporting
  individual moment values;
- a genuinely derived global object whose local `Tor_1` classes are used at
  the same prime, rather than a nonexistent cross-prime derived intersection.

This sharpens H7-DEN-TRANS; it does not construct one of these alternatives.

## 5. Verification scope

`114_a_58_h7_den_trans_span_derived_witt_verify.py` checks Bezout collapse
for many distinct prime pairs, the exact `Tor_0/Tor_1` gcd formulas, the
same-prime excess, failure of `p` inversion in all finite Witt truncations,
and the incompatibility between inversion in `Q_p` and residue reduction.
