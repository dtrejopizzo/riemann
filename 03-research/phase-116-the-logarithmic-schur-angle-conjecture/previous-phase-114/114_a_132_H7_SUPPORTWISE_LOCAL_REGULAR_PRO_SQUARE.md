# 114.a.132 — H7: supportwise local reflection constructs the repaired pro-square

```
+------------------------------------------------------------------------+
| INDEX       Fix finite prime support T and a level N divisible by prod T.|
| LOCAL       Require p_i-regularity only where the scalar p_i is an       |
|             actual integral section of the chart.                        |
| OVERLAP     When a finite chart meets a real chart, every p in T is a    |
|             unit on the chosen overlap, so reflection is trivial there.  |
| GLUE        Relative reflections therefore glue at every (T,N).          |
| PRO         Increasing T and N gives one directed repaired pro-square.    |
| LATTICE     Every finite-support prime lattice exists on a cofinal tail.  |
+------------------------------------------------------------------------+
```

## 1. The supportwise index category

Let `T` be a finite set of rational primes and put `n_T=product_(p in T)p`.
Work only at compactification levels `N` divisible by `n_T`.  Order pairs

\[
 (T,N)\preceq(T',N')quad\Longleftrightarrow\quad
 T\subseteq T',\quad N\mid N'.                                      \tag{1.1}
\]

This category is directed.  Every finite divisor support occurs in a
cofinal tail, while no single real chart is required to contain all integer
scalars.

At level `N`, use Haran's standard product cover.  A factor is either the
finite chart `Spec Z` or the real chart
`Spec A_N`, `A_N=Z[1/N] intersect Z_R`.  For a product chart `A_alpha`, let
`I_alpha subset {1,2}` record the factors of finite type.  For `i in I_alpha`
and `p in T`, the central scalar `p_i` is an actual section of `A_alpha`.
No such scalar is imposed for a real factor.

## 2. Relative regular reflection

Call a target of `A_alpha` **(T,alpha)-regular** if multiplication by every
actual scalar

\[
 \{p_i:p\in T,\ i\in I_\alpha\}                                    \tag{2.1}
\]

is injective on every operation set.  Define `Reg_(T,alpha)(A_alpha)` as
the quotient by the intersection of equality kernels of maps to all such
targets, exactly as in `a109`.

The family of targets is nonempty.  Central localization obtained by
inverting all scalars in (2.1) is a regular target, and is nonzero because
it maps to the common generic overlap.  The product argument of `a109`
therefore proves:

### Proposition 2.1

`Reg_(T,alpha)` is the universal quotient of `A_alpha` in which the actual
scalars (2.1) act injectively.  It is functorial for maps preserving the
displayed local scalar systems, and is idempotent.

On the finite-finite chart this is the finite-support version of `a109`.  On
the real-real chart `I_alpha` is empty and the identity map occurs among the
targets, so the reflection is the identity.  Thus the real unit-ball chart
is preserved rather than being fed to an undefined `Reg_Z`.

## 3. Compatibility on overlaps

There are two cases.

### 3.1 The active scalar systems agree

For a central localization `S^(-1)A_alpha` on which the same scalars (2.1)
remain active, the universal-property proof of `a110` applies verbatim:

\[
 S^{-1}Reg_{T,\alpha}(A_\alpha)
 \simeq Reg_{T,\alpha}(S^{-1}A_\alpha).                               \tag{3.1}
\]

### 3.2 A finite factor meets a real factor

The common overlap is the generic chart `Z[1/N]`.  Since `n_T|N`, every
`p in T` is a unit there.  Injectivity of multiplication by a unit is
automatic on every operation set.  Hence imposing or forgetting the
corresponding member of (2.1) gives the same universal category on the
overlap.  Both sides of the gluing map reduce canonically to the unreflected
localized overlap.

### Theorem 3.1 (H7-LOCAL-REG-GLUE)

For every pair `(T,N)` with `n_T|N`, the reflected standard charts glue to a
commutative involutive generalized-ring scheme

\[
 Y^{\rm locreg}_{T,N}.                                                \tag{3.2}
\]

The construction is independent of refinement of the standard product
cover, preserves the real-real chart, and has a canonical morphism to the
literal stage `Y_N`.

### Proof

Equation (3.1) handles overlaps with unchanged active systems.  Section 3.2
handles every overlap where a factor changes type.  The resulting overlap
isomorphisms are the unique ones representing the same localization
universal property, so their triple-overlap cocycles commute automatically.
Refining the cover repeats the same two cases.  Quotient maps on charts give
the contravariant morphism to `Y_N`.  QED.

## 4. Pro-transitions and prime lattices

If `T subset T'`, every `(T',alpha)`-regular target is `(T,alpha)`-regular.
The intersection-of-kernels construction gives a canonical quotient

\[
 Reg_{T,\alpha}(A_\alpha)\longrightarrow
 Reg_{T',\alpha}(A_\alpha).                                          \tag{4.1}
\]

If `N|N'`, Haran's restriction maps preserve the actual local scalar
systems, and the overlap argument above makes their reflected maps glue.
Contravariantly, (4.1) and the level maps form a pro-system

\[
 Y^{\rm locreg}=\{Y^{\rm locreg}_{T,N}\}_{(T,N)}.                    \tag{4.2}
\]

Fix a prime-generated divisor whose support is `T_0`.  On every tail
`T superset T_0`, its finite-chart denominators are regular by Proposition
2.1.  On real charts its local multiplier is the already integral value `1`,
not a nonexistent scalar `p`.  Therefore its Section-11 local lattices glue
and define a completed pro-lattice on (4.2).  Tensor products add valuations,
so every finite-support prime presentation is defined on a cofinal tail.

The finite diagonal/contact calculation of `a109` is unchanged: on a chart
where `p` cuts the divisor, `p` is active and regular; quotient base change
still gives `Spec F_p`.

## 5. Exact scope restored

This proves H7-LOCAL-REG-GLUE and replaces the ill-typed global claim of
`a110`.  It constructs a supportwise directed repaired pro-square and
restores the **existence** of every finite-support prime completed lattice
and its literal diagonal contact.

It does not by itself prove:

1. independence of the prime anti-diagonal in completed Picard;
2. H7-MIXED-BDRY-PIC on the repaired mixed boundaries;
3. geometric RR/Green/Deligne comparison;
4. undecorated dynamic cycles.

Thus `a111`--`a130` may now be read on `Y^locreg` after replacing the old
global symbol `Y^reg`; their implication chains are restored, but their
explicit remaining gates stay open.  Row A and RH remain open.

## 6. Verification scope

`114_a_132_h7_supportwise_local_reg_verify.py` checks directed support
indices, active chart systems, localization-unit compatibility, relative
torsion reflection on exhaustive finite abelian shadows, transition maps and
source anchors.  The scheme gluing theorem is the displayed pair of
localization universal properties.
