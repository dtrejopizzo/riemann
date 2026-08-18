# 114.a.56 — H7-SEL: exact coordinate-hitting criterion for multiplicative quotients

```
+--------------------------------------------------------------------------+
| SOURCE      One moment block is the ring F_p^m under first addition.    |
| QUOTIENT    Every unital ring quotient retains a coordinate subset S.   |
| SEPARATE    S works iff it hits the support of every code difference.   |
| MINIMUM     kappa(r,Q;p) is the minimum such hitting-set size.           |
| BOUNDED     a_55 makes every retained quotient exactly F_p^S.            |
| SHARP RR    Equivalent to kappa log p-log #I_r(Q)=o(t^2).               |
| RESULT      H7-SEL is reduced to one finite asymptotic invariant.        |
+--------------------------------------------------------------------------+
```

## 1. Multiplicativity leaves only coordinate projections

Let

\[
 R_m=\mathbb F_p^m                                                       \tag{1.1}
\]

be one odd-moment block, with its first selected addition and common
multiplication. This is the ordinary product ring.

### Lemma 1.1 (quotients of a product of fields)

Every ideal of `R_m` has the form

\[
 I_J=\{x=(x_i):x_i=0\text{ for }i\notin J\}                             \tag{1.2}
\]

for a unique subset `J` of `{0,...,m-1}`. Consequently every nonzero unital
ring quotient of `R_m` is, up to coordinatewise field automorphisms,

\[
 R_m/I_J\simeq\mathbb F_p^S,
 \qquad S=\{0,\ldots,m-1\}\setminus J.                                  \tag{1.3}
\]

### Proof

If `x in I` and `x_i!=0`, multiply `x` by the tuple which is `x_i^(-1)` in
coordinate `i` and zero elsewhere. The primitive idempotent `e_i` belongs
to `I`. Thus `I` is spanned by exactly the primitive idempotents it contains,
which proves (1.2)--(1.3). QED.

A bio quotient restricts on unary scalars with the first addition to a ring
quotient. Therefore any **quotient-based** H7-SEL construction preserving
that addition and multiplication can only discard moment coordinates. This
does not rule out a genuinely different, non-quotient cohomology theory.

## 2. The exact hitting invariant

Let `C=I_r(Q)` be the balanced code and let

\[
 E:C\longrightarrow\mathbb F_p^m,
 \qquad m=2r,                                                           \tag{2.1}
\]

be the odd-moment embedding of `a_51`. For distinct `c,c' in C`, define

\[
 \operatorname{Diff}(c,c')
 =\{j:E_j(c)\ne E_j(c')\}.                                               \tag{2.2}
\]

Every such set is nonempty because `E` is injective. Define

\[
 \boxed{
 \kappa(r,Q;p)=min\bigl\{|S|:
 S\cap\operatorname{Diff}(c,c')\ne\varnothing
 \text{ for all }c\ne c'\bigr\}.
 }                                                                       \tag{2.3}
\]

### Theorem 2.1 (selective quotient criterion)

For a coordinate set `S`, the following are equivalent:

1. the quotient `pi_S:R_m->F_p^S` is injective on the balanced code;
2. `S` hits every set (2.2).

The minimum number of coordinates in a multiplicative moment quotient
separating the code is exactly `kappa(r,Q;p)`.

### Proof

The projected images of `c,c'` agree precisely when every coordinate in
`S` lies outside `Diff(c,c')`. This proves the equivalence and then (2.3).
QED.

The information bound gives

\[
 \kappa(r,Q;p)\ge
 \left\lceil{\log\#I_r(Q)\over\log p}\right\rceil.                     \tag{2.4}
\]

It need not be an equality at finite scale: the moment coordinates are a
restricted family of hashes.

## 3. Exact acceptance test after the bounded no-go

The bounded interpolation theorem `a_55` surjects the complete bounded
section set onto `F_p^m`. Composing with `pi_S` proves

\[
 \#\pi_S E(H^0_{\rm bd})=p^{|S|}.                                       \tag{3.1}
\]

Thus discarding coordinates does not leave an unknown upper count: its
bounded image is the whole selected quotient.

For the block parameters `(r_t,Q_t,p_t)`, a multiplicative selective moment
quotient has the sharp code coefficient if and only if it admits separating
coordinate sets `S_t` such that

\[
 \boxed{
 |S_t|\log p_t-\log\#I_{r_t}(Q_t)=o(t^2).
 }                                                                       \tag{H7-SEL-MOM}

Equivalently, the minimum choice works exactly when

\[
 \kappa(r_t,Q_t;p_t)\log p_t
 -\log\#I_{r_t}(Q_t)=o(t^2).                                            \tag{3.2}
\]

This is necessary and sufficient for the **finite multiplicative quotient
and cardinality** part of H7-SEL-RR. It does not yet prove:

1. (3.2) uniformly on all positive Picard rays;
2. compatibility of minimizing sets under the cofinal projections;
3. restriction/exact-sequence functoriality;
4. realization of the polarized coefficient as an intersection product.

Those four clauses are the remaining H7-SEL-RR/EXACT gate. The first is now
a precise finite asymptotic problem rather than an unspecified filtration.

`a_57` later adds a denominator obstruction to clause 2: an old
characteristic-`p` coordinate cannot be retained once `p` itself becomes an
allowed divisor denominator. Hence this criterion is unconditional per
block and on fixed-support rays, but global use also requires H7-DEN-TRANS.

## 4. Finite evidence and its limit

Small exact computations show both behaviours:

- sometimes `kappa` attains the information bound;
- sometimes it is strictly larger, even when the target field has more
  elements than the code.

Therefore finite injectivity of a convenient moment subset cannot be
extrapolated to (3.2). A proof must control the hitting number asymptotically;
the full `2r`-moment Vandermonde theorem supplies only the coarse upper bound
`kappa<=2r`.

## 5. Verification scope

`114_a_56_h7_selective_moment_quotient_verify.py` enumerates all ideals of
small product rings, computes `kappa` exactly for finite balanced codes,
checks the information bound and examples of strictness, and confirms that
the bounded interpolation family remains surjective after every coordinate
projection. It does not infer the unresolved asymptotic (3.2) from those
finite examples.
