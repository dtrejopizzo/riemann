# 114.a.134 — I7: the exact torsor-to-derived-kernel linearization gate

```
+------------------------------------------------------------------------+
| INPUT       Faithful multiplicative unit torsors T_n already exist.     |
| SOURCE      Haran Section 6 gives an abelian module category, scalar     |
|             extension and a cotangent complex.                          |
| MISSING     It does not supply the rank-one/tensor/descent comparison    |
|             needed to turn T_n into convolution kernels.                |
| RESULT      Module kernels are a precise conditional route, not yet a   |
|             construction of the required undecorated Gamma_n.           |
+------------------------------------------------------------------------+
```

## 1. What is actually available

For a generalized ring `A`, Haran (6.1)--(6.2) defines `A`-modules as
abelian-group-valued functors with the relevant left/right operations.  The
paragraph following (6.2) states that `A-mod` is complete and cocomplete,
abelian, and has enough projectives and injectives.  Equation (6.3) gives
extension/restriction of scalars, while (6.6)--(6.7) gives cotangent modules
and their derived version.

These statements justify doing homological algebra after a module has been
constructed.  They do not identify the Section-11 completed unit torsors or
right acts with invertible objects of `A-mod`.

In particular, the cited Section-6 passage does not define an object denoted
`A^[1]`, prove that its automorphism group is `GL_1(A)`, or equip `A-mod`
with the symmetric tensor product needed below.  The former shorthand in
`a_62` is therefore retracted.

## 2. Exact sufficient package

Let `Pic_tor(A)` be the unit-torsor Picard groupoid used in `a_61`, `a_66`
and `a_70`.  A torsor linearization adequate for I7 would consist of:

1. a distinguished locally free rank-one module `P_A` and a proved
   identification `Aut_A(P_A)=GL_1(A)`;
2. effective descent for the associated-module construction
   `T mapsto E(T)=T times^{GL_1(A)} P_A`;
3. a symmetric monoidal structure with canonical isomorphisms
   `E(T) tensor E(U) ~= E(T tensor U)`, compatible with pullback;
4. full faithfulness on the prime-generated subgroup, so that distinct
   `T_n` remain distinct after linearization;
5. a comparison between the derived diagonal contact of
   `K_n=Delta_* E(T_n)` and the already constructed contact object `P_n`.

If these five assertions hold on the supportwise repaired pro-square
`Y^locreg`, then the projection formula would give the desired conditional
convolution law

\[
 K_m star K_n \simeq K_{mn},
 \qquad
 \log\#\Gamma\,\operatorname{Cont}(K_n)=\Lambda(n).                 \tag{2.1}
\]

The first equality also requires the relevant pushforward and convolution
formalism for these module sheaves; it is part of item 3 rather than a
consequence of the bare abelian-category statement.

## 3. Necessity for this proposed route

The gates above are not cosmetic:

- without item 1 there is no canonical associated module;
- without item 2 local unit cocycles need not glue as modules;
- without item 3 torsor multiplication does not imply kernel convolution;
- without item 4 the arithmetic label may collapse, exactly as it does
  after forgetting the decoration in `a_70`;
- without item 5 a derived intersection has no proved relation to
  `Lambda(n)`.

Thus the existence of an abelian module category alone cannot close
H7-DYNAMIC-THICKENING.  It only makes the five-part package meaningful.

## 4. Status and consequence

This audit removes a false shortcut but preserves the viable route:

> **H7-TOR-LIN.** Construct and prove items 1--5 above, including the
> supportwise sheaf/convolution formalism and contact comparison.

H7-TOR-LIN would promote the already closed decorated monoid I7-DYN-TOR to
a derived/module kernel monoid.  Whether such kernels count as
"undecorated cycles" still depends on the final correspondence theory; no
ordinary Chow cycle is produced here.  Therefore I7 and row A remain open.

## 5. Verification scope

`114_a_134_i7_torsor_linearization_gate_verify.py` checks the precise
Section-6 source statements, absence of the unsupported notation in that
section, the five non-collapsible gates, and the scope markers.  It does not
claim to verify existence of H7-TOR-LIN.
