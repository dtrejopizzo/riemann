# 114.a.87 — H7: one characteristic-zero residual embedding would settle every prime

```
+-------------------------------------------------------------------------+
| SCALAR RING Haran's first addition makes the scalar plane an ordinary   |
|             commutative ring A_1.                                      |
| REAL BIOS   For every u>0, a49 gives a ring map rho_u:A_1 -> R.         |
| PRODUCT     rho=(rho_u)_u lands in the torsion-free ring R^(R_{>0}).    |
| CONSEQUENCE Faithfulness of rho implies scalar p-regularity for every p.|
| ALL ARITIES Tameness then promotes scalar regularity to every operation. |
| EXACT GATE  H7-REAL-RES plus H7-TAME-PLANE.                             |
+-------------------------------------------------------------------------+
```

## 1. The scalar plane is an ordinary ring

Let

\[
 A=\left(\mathbb Z\mathbin{\mathop\otimes_{\mathbb F}}\mathbb Z
    \right)_{[1],[1]}.
\]

Haran's formula (10.21) defines, for either ruling `i`, an addition
`+_(i)` on this same scalar set.  The sentence immediately following that
formula states that `(A,+_(i),multiplication)` is an ordinary commutative
ring with involution.  Fix `i=1` and write the resulting ring as `A_1`.
The first-ruling element denoted by an integer prime `p` is therefore
`p*1` in this ordinary ring.  Consequently scalar H7-PRIME-REG is exactly

\[
 px=py\quad\Longrightarrow\quad x=y\qquad(x,y\in A_1).              \tag{1.1}
\]

Equivalently, the additive group of `A_1` has no `p`-torsion.

## 2. The characteristic-zero residual map

For every real parameter `u>0`, `a49` maps the two structural ring bios to
the homogeneous endomorphism bio.  On unary operations every homogeneous
endomorphism of `R` is multiplication by its value at `1`.  Taking that
coefficient in the representation and in its involutive-opposite factor gives

\[
 \rho_u:A_1\longrightarrow\mathbb R\times\mathbb R.                 \tag{2.1}
\]

Because the first structural addition is ordinary addition in the target
and composition of scalar multiplications multiplies their coefficients,
`rho_u` is a unital ring homomorphism.  Assemble them into

\[
 \rho:A_1\longrightarrow\prod_{u>0}(\mathbb R\times\mathbb R),
 \qquad x\longmapsto(\rho_u(x))_{u>0}.                               \tag{2.2}
\]

The target is torsion-free as an abelian group.

> **H7-REAL-RES.** The map (2.2) is injective.

### Theorem 2.1 (simultaneous scalar prime regularity)

H7-REAL-RES implies multiplication by every nonzero integer, hence by every
prime, is injective on `A_1`.

### Proof

If `n x=n y`, apply (2.2).  Coordinatewise cancellation of the nonzero real
number `n` gives `rho(x)=rho(y)`.  H7-REAL-RES gives `x=y`.  QED.

This is stronger and cleaner than proving one colon identity separately for
each prime: one characteristic-zero embedding settles all of them at once.

## 3. Promotion to all arities

The tame scalar criterion of `a84` now gives an exact two-hypothesis route.

### Corollary 3.1

If H7-REAL-RES and H7-TAME-PLANE hold, then first-ruling multiplication by
every prime is injective in every arity of the base arithmetic plane.
Thus base H7-PRIME-REG holds; the central-localization argument of `a71`
then transports it to the required affine localizations.

### Proof

Theorem 2.1 supplies scalar injectivity.  Apply Theorem 2.1 of `a84` prime
by prime.  QED.

There is also a stronger sufficient replacement for tameness: injectivity
of every matrix-coefficient map.  Haran proves that a matrix generalized
ring is tame, but does not state that the arithmetic plane is matrix or
tame.

## 4. What is already separated and what is not

The residual family is known to be faithful on the common integral scalar
copy: under every `rho_u`, an integer `m` acts as multiplication by `m`, so
evaluation at `1` recovers it (`a49`).  The multivariable version separates
all signed read-once alternating trees (`a74`--`a75`).  It also distinguishes
the two addition generators when `u!=1`.

These facts do **not** prove H7-REAL-RES on all scalar classes.  Moreover,
`a88` proves that this particular unary family forgets the detailed leaf
matching `sigma` inside fixed sign fibers: its two coordinates retain only
the signed left and right marginals.  Thus H7-REAL-RES entails the additional
H7-MARGINAL-COMPLETE theorem that the full Haran quotient already identifies
every residual ambiguity invisible to those marginals.  Corrected `a89`
shows that on one arbitrary fixed two-level grid both ruling cancellations
collapse the table to total signed mass; naive row/column margins are not
invariants.  Nested cut-changing overlaps remain.  A possible
kernel element must use repeated/contraction data or genuinely bilateral
cut identifications, precisely the residual sector already isolated in
`a75`--`a86`.  Nor do scalar evaluations prove H7-TAME-PLANE, which is a
separation assertion in every arity.

The live sufficient route is therefore

\[
 \boxed{\text{H7-REAL-RES}+\text{H7-TAME-PLANE}
        \Longrightarrow\text{H7-PRIME-REG}.}                          \tag{4.1}
\]

Alternatively one may still prove H7-PRIME-REG directly through component
injectivity (`a85`).  H7-p-ONE-BOUNDARY and H7-p-DIVPATH are a structured
sufficient factorization of that direct route; they are not silently
assumed here.  H7-REAL-RES and H7-TAME-PLANE remain open, so row A remains open.

**Later sharpening (`a102`).**  The fold splits the scalar ring as
`R=Z direct-sum K`.  H7-REAL-RES is a sufficient way to prove that `K` is
torsion-free, while H7-AUG-FLAT names that exact necessary-and-sufficient
scalar property without requiring this particular real residual family.

**Later resolution (`a104`).**  H7-TAME-PLANE is false, so implication
(4.1) cannot be applied to the signed plane.  H7-REAL-RES may still study
the scalar kernel, but it no longer promotes scalar injectivity to all
arities through tameness.

## 5. Verification scope

`114_a_87_h7_characteristic_zero_residual_verify.py` checks the primary
source statement that each scalar ruling is an ordinary commutative ring,
the coefficient extraction used in `a49`, and the simultaneous
torsion-cancellation theorem in exhaustive finite injective models.  It
also enforces the two open-hypothesis markers.  The mathematical implication
is Theorem 2.1 and Corollary 3.1; the finite controls do not assert residual
faithfulness or marginal completeness of the Haran plane.

Primary sources: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.19)--(10.21); Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Definition 1.4.3.
