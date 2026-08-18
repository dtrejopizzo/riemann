# 114.a.102 — H7: scalar prime regularity is flatness of the off-diagonal augmentation ideal

```
+-------------------------------------------------------------------------+
| SCALAR      R=(Z tensor_F{+-1} Z)_[1,1] with first-ruling addition.      |
| SPLIT       First ruling i:Z->R and fold nabla:R->Z satisfy nabla i=id.  |
| KERNEL      R=Z direct-sum K as additive groups, K=ker(nabla).           |
| PRIME       p is regular on R iff K[p]=0 iff Tor_1^Z(K,Z/p)=0.           |
| ALL PRIMES  Every prime is regular iff K is torsion-free iff K is        |
|             flat as an ordinary Z-module.                               |
| WARNING     A split fold does not imply flatness.                        |
| OPEN        H7-AUG-FLAT; all arities additionally need H7-TAME-PLANE.    |
+-------------------------------------------------------------------------+
```

## 1. The ordinary scalar ring and its fold

Let

\[
 A=\mathbb Z\mathbin{\mathop\otimes_{\mathbb F\{\pm1\}}}\mathbb Z
\]

be Haran's affine arithmetic plane in the bilateral formalism.  Use the
first ruling to define the ordinary commutative scalar ring

\[
 R=A_{[1],[1]}^{\{1\}}.                                      \tag{1.1}
\]

This is the ordinary ring supplied by Haran's formula (10.21).  The first
ruling gives a unital ring homomorphism

\[
 i_1:\mathbb Z\longrightarrow R.                              \tag{1.2}
\]

The coproduct universal property gives the fold homomorphism

\[
 \nabla:A\longrightarrow\mathbb Z                             \tag{1.3}
\]

whose restrictions to both rulings are the identity.  Since generalized-ring
homomorphisms preserve the addition induced by the chosen ruling, its scalar
map is a ring homomorphism `R->Z` and

\[
 \nabla\circ i_1=id_{\mathbb Z}.                               \tag{1.4}
\]

Put

\[
 K=\ker(\nabla:R\longrightarrow\mathbb Z).                     \tag{1.5}
\]

Thus `K` is an ordinary ring ideal and (1.4) gives the canonical additive
decomposition

\[
 R=i_1(\mathbb Z)\oplus K.                                    \tag{1.6}
\]

The word *canonical* here refers to the chosen first ruling and the fold; it
does not assert a product decomposition of rings.

## 2. Exact scalar PRIME-REG criterion

### Theorem 2.1 (augmentation-kernel criterion)

For a rational prime `p`, the following are equivalent:

1. multiplication by `p=i_1(p)` is injective on `R`;
2. multiplication by `p` is injective on the additive group `K`;
3. `K[p]={k in K:pk=0}=0`;
4. `Tor_1^Z(K,Z/p)=0`.

### Proof

Under (1.6), multiplication by the central scalar `i_1(p)` is the direct
sum of multiplication by `p` on `Z` and on `K`.  The first summand is
injective, proving the equivalence of (1)--(3).  Tensor the exact sequence

\[
 0\longrightarrow\mathbb Z\xrightarrow{p}\mathbb Z
 \longrightarrow\mathbb Z/p\longrightarrow0
\]

with `K`.  Its long exact Tor sequence identifies

\[
 \mathrm{Tor}_1^{\mathbb Z}(K,\mathbb Z/p)
 \cong\ker(p:K\to K)=K[p],                                    \tag{2.1}
\]

which proves (4).  QED.

### Theorem 2.2 (simultaneous criterion)

The following are equivalent:

1. every nonzero integer, equivalently every prime, acts injectively on `R`;
2. the additive group `K` is torsion-free;
3. `K` is flat as an ordinary `Z`-module;
4. `R` is flat as an ordinary `Z`-module.

### Proof

By Theorem 2.1, all primes act injectively precisely when `K` has no
prime-order torsion.  Every nonzero finite-order element has an element of
prime order in its cyclic subgroup, so this is equivalent to torsion-freeness.
Over the principal ideal domain `Z`, a module is flat if and only if it is
torsion-free.  Finally (1.6) and flatness of `Z` show that `K` is flat if and
only if `R` is flat.  QED.

Define the exact scalar gate

> **H7-AUG-FLAT.** The off-diagonal augmentation ideal `K=ker(nabla)` is a
> torsion-free (equivalently flat) ordinary `Z`-module.

This is exactly H7-SCALAR-SAT from `a84`, simultaneously for all primes; it
is not a stronger hidden assumption.

## 3. Why the retraction alone is insufficient

A ring retraction does not imply flatness.  Fix a prime `p` and take

\[
 S=\mathbb Z\times\mathbb F_p,\qquad
 i(n)=(n,\bar n),\qquad \rho(n,a)=n.                               \tag{3.1}
\]

Then `rho o i=id_Z`, but

\[
 i(p)(0,1)=(p,0)(0,1)=(0,0),\qquad (0,1)\ne0.                      \tag{3.2}
\]

Its augmentation kernel is `0 x F_p`.  Thus neither the existence of the
fold nor injectivity of a ruling proves H7-AUG-FLAT.  A freeness, purity or
faithful characteristic-zero residual theorem for `K` is still required.

The tensor product defining the arithmetic plane is a categorical coproduct
of generalized rings.  Haran's construction gives generators, relations and
the fold, but the audited sources do not state that the induced ordinary
`Z`-module `R` or `K` is flat.  Categorical coproduct must not be conflated
with the tensor product in an abelian module category.

## 4. Relation to the completed sectors

The previous saturation results now locate their content inside `K`:

- the fixed two-level quotients of `a89` are free abelian (indeed their
  residual invariant is total mass);
- the laminar gluing lattices of `a90` have only unit Smith factors;
- the read-once sectors `a72`--`a75` embed into characteristic-zero targets.

Hence these sectors contribute no torsion to the corresponding restrictions
of `K`.  Any failure of H7-AUG-FLAT must be represented by the remaining
nonlaminar bilateral/cut-changing macro sector.  The coefficient-annihilator
branch H7-COEFF-ANN of `a101` is one possible mechanism, not an exhaustive
classification of every macro obstruction.

If H7-AUG-FLAT and H7-TAME-PLANE both hold, Theorem 2.1 of `a84` promotes
scalar cancellation to every arity; `a71` then transports it through the
central affine localizations.  Thus

\[
 \boxed{\text{H7-AUG-FLAT}+\text{H7-TAME-PLANE}
 \Longrightarrow\text{H7-PRIME-REG}.}                              \tag{4.1}
\]

Neither hypothesis is proved here.  The alternative direct route remains
the component-injectivity/p-CONVEX/p-DIVPATH theorem of `a85`--`a86`.
Completed lattices, the geometric gauge and row A remain open.

## 5. Verification scope

`114_a_102_h7_augmentation_flatness_verify.py` checks the split-kernel
decomposition in finite presentations, the prime-kernel/Tor formula on
finitely generated abelian groups, the retracted nonflat ring (3.1), the
source markers for the ordinary scalar ring, and all open-scope guards.  The
flatness equivalence itself is the standard PID theorem used explicitly in
Theorem 2.2; finite computation does not prove H7-AUG-FLAT for Haran's plane.

Primary sources: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.19)--(10.22); Haran,
[*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Sections 13.1--13.2 (coproduct presentation and fold).

**Later resolution (`a104`).**  H7-TAME-PLANE is false.  H7-AUG-FLAT
remains the exact scalar criterion, but the conditional promotion (4.1)
cannot establish all-arity H7-PRIME-REG for the signed plane.

**Final resolution of this gate (`a108`).**  H7-AUG-FLAT is false.  The
nonzero scalar `kappa=(1,-1)_1 o (1,1)_2^t` lies in `ker(nabla)` and satisfies
`2kappa=0`.  Thus the augmentation ideal has explicit 2-torsion; this is the
Haran plane itself, not the split warning model of Section 3.
