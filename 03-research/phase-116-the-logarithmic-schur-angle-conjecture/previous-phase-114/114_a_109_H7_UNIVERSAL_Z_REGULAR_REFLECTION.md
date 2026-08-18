# 114.a.109 — H7: the universal Z-regular reflection repairs the base square

```
+------------------------------------------------------------------------+
| INPUT       P=F(Z)_1 tensor_(F{+-1}) F(Z)_2, with scalar 2-torsion.     |
| REFLECTION  P^reg=P/E_reg, intersection of kernels of all targets in    |
|             which both integer rulings act injectively in every arity.  |
| KILLS       The class kappa of a108.                                    |
| RETAINS     Both Z rulings, the fold, and the non-total cross defect.    |
| CONTACT     Delta^* V_p^reg = Spec F_p, of degree log p.                 |
| SCOPE       Base algebra repaired; pro-sheaf, full divisors/RR/gauge     |
|             still require transport.                                    |
+------------------------------------------------------------------------+
```

## 1. The regular subcategory and its universal quotient

Work in the category of commutative involutive `F`-rings equipped with two
compatible maps from `F(Z)` over `F{+-1}`.  Call such an object
**Z-regular** when, for every nonzero integer `n`, each of its two scalar
images acts injectively on every operation set.

Let

\[
 P=F(\mathbb Z)_1\otimes_{F\{\pm1\}}F(\mathbb Z)_2.             \tag{1.1}
\]

Consider the set of equivalence ideals `E` on `P` for which `P/E` is
Z-regular, and define

\[
 E_{\rm reg}=\bigcap_E E,\qquad P^{\rm reg}=P/E_{\rm reg}.      \tag{1.2}
\]

The family is nonempty: the fold kernel gives the quotient `F(Z)`, which is
Z-regular.  It is a set, since every equivalence ideal is a subset of the
set of operation pairs of `P`.

### Theorem 1.1 (regular reflection)

`P^reg` is Z-regular, and every map from `P` to a Z-regular target factors
uniquely through it.

### Proof

The diagonal map

\[
 P/E_{\rm reg}\longrightarrow\prod_E P/E                       \tag{1.3}
\]

is injective on every operation set by the definition of the intersection.
Every integer acts injectively on the product, coordinatewise, and hence on
its subobject `P^reg`.  If `f:P->A` has Z-regular target, its equality kernel
is one of the ideals occurring in (1.2); therefore `E_reg subset ker(f)` and
`f` factors uniquely.  QED.

This is the reflection of this specific coproduct into the full regular
subcategory.  Equivalently, `P^reg` is the coproduct of the two integers in
that subcategory.  It is canonical and symmetric under exchange of the two
rulings.

## 2. What the quotient kills and what it provably retains

### Proposition 2.1 (the obstruction is removed)

The scalar `kappa` of `a108` maps to zero in `P^reg`.

### Proof

Its image is killed by `2`; Z-regularity cancels `2`.  QED.

This is not an ad hoc relation: every map to every regular target kills
`kappa`, so (1.2) is the minimal universal quotient that must kill it.

### Proposition 2.2 (both arithmetic axes survive)

Both ruling maps

\[
 i_1,i_2:F(\mathbb Z)\longrightarrow P^{\rm reg}                \tag{2.1}
\]

are injective, and the fold

\[
 \nabla:P^{\rm reg}\longrightarrow F(\mathbb Z)                 \tag{2.2}
\]

satisfies `nabla i_1=nabla i_2=id`.

### Proof

The original fold has Z-regular target and therefore factors through
`P^reg`.  Its composites with the two rulings remain the identity, giving
left inverses and hence injectivity.  QED.

### Proposition 2.3 (the plane does not collapse to the diagonal)

The mixed centre/grid defect of `a104` remains nonzero in `P^reg`.

### Proof

The target `H=F(Z) Pi N` of `a104` is Z-regular in every arity by `a105`, so
its map from `P` factors through `P^reg`.  It sends the defect to the
nonzero nine-coordinate element of the free group `N_(2,2)`.  Therefore the
class cannot vanish in `P^reg`.  QED.

Thus the repair removes the forced torsion without imposing total
commutativity or identifying the two additions.

## 3. Prime rulings and diagonal contact survive

For a prime `p` and a ruling `i`, let

\[
 V^{\rm reg}_{p,i}
 =\mathrm{Spec}\,\bigl(P^{\rm reg}/E((i_i(p)))\bigr).       \tag{3.1}
\]

Since `i_i(p)` is regular, this is now a regular principal generalized
Cartier datum in the sense of `a67`.

Let `Delta:Spec F(Z)->Spec P^reg` be the section corresponding
contravariantly to the fold.  Quotient base change gives

\[
 \Delta^*V^{\rm reg}_{p,i}
 \simeq\mathrm{Spec}\,\bigl(F(\mathbb Z)/E((p))\bigr)
 \simeq\mathrm{Spec}\,\mathbb F_p.                         \tag{3.2}
\]

### Corollary 3.1

The repaired prime ruling has canonical diagonal contact mass

\[
 \deg_\Delta(V^{\rm reg}_{p,i})
 =\log\#\mathbb F_p=\log p.                                   \tag{3.3}
\]

In particular the repair does not erase the `Lambda(2)` contact that
motivated it.

## 4. Consequences and remaining construction work

At the base affine level, `P^reg` supplies exactly the algebraic properties
that the failed H7-PRIME-REG route was trying to prove:

1. every nonzero integer is a regular scalar in both rulings and all
   arities;
2. both arithmetic axes and the diagonal retraction survive;
3. the plane remains genuinely non-total;
4. every prime ruling remains a regular principal quotient with diagonal
   degree `log p`.

But `P^reg` is a **modified** arithmetic square, not Haran's literal
coproduct in the unrestricted category.  To use it for row A one must still
prove:

1. functorial reflection on every finite-stage open and compatibility with
   restrictions, central localization and the pro-transition maps;
2. descent of `Pic_tor`, completed lattices and section sheaves;
3. preservation of the prime-power/dynamic contact system, not only (3.2);
4. a canonical degree, intersection form and gauge satisfying the row-A
   acceptance tests.

These are the next gates H7-REG-SHEAF, H7-REG-DIV and H7-REG-RR.  This file
does not assert them, does not close G-7 or row A, and does not assert RH.

## 5. Verification scope

`114_a_109_h7_z_regular_reflection_verify.py` exhausts finite generated
abelian shadow presentations, verifies that intersection-of-regular-kernels
is torsion-free and universal, and checks the exact fold, obstruction,
noncollapse and `F_p` contact logic.  The categorical proof above, rather
than the finite shadows, establishes Theorem 1.1 for the `F`-ring plane.
