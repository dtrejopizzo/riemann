# 114.a.131 — H7 correction: global Z-reflection is ill-typed on the real charts

```
+------------------------------------------------------------------------+
| FINITE      The affine plane P=F(Z) tensor_F F(Z) has two Z-rulings;    |
|             its universal regular reflection a109 remains valid.        |
| REAL        A real chart has scalar object A_N=Z[1/N] intersect [-1,1]; |
|             it does not contain the scalar 2.                           |
| TYPE ERROR  Such a chart has no local map F(Z)->A_N, hence cannot be     |
|             fed to Reg_Z as defined in a110.                            |
| RETRACT     The global gluing theorem and Y^reg are not yet constructed. |
| REPLACE     Reflect relative to the denominator scalars actually present |
|             on each chart, and prove overlap/pro compatibility.         |
+------------------------------------------------------------------------+
```

## 1. The missing hypothesis on the archimedean charts

Haran constructs the compactified curve from the ordinary finite chart and
the real charts

\[
 A_N=\mathbb Z[1/N]\cap\mathbb Z_{\mathbb R},
 \qquad \mathbb Z_{\mathbb R,[1]}=[-1,1].                             \tag{1.1}
\]

Consequently `2` is not a scalar section of `A_N`.  More generally the
structure at infinity is a generalized ring precisely because its scalar
unit ball is not closed under ordinary addition.

A map `F(Z)->A_N` of unital generalized rings would have to carry the scalar
integer `2`, encoded by the binary addition of two units, to the corresponding
scalar operation in `A_N`.  That scalar is absent from (1.1).  Hence no such
map exists.  There is only the common signed base map `F{+-1}->A_N` and the
map from the appropriate bounded/localized generalized integer object.

The mixed and real-real product charts therefore do not carry the two maps

\[
 F(\mathbb Z)_1,F(\mathbb Z)_2\longrightarrow A_\alpha               \tag{1.2}
\]

assumed at the start of `a110` Definition/Theorem 1.1.

### Theorem 1.1 (typing obstruction)

The instruction in `a110` to replace **every** affine chart `A_alpha` by
`Reg_Z(A_alpha)` is not defined on the archimedean charts of Haran's
compactification.  Therefore Proposition 3.1 of `a110` does not, as written,
construct a global repaired pro-scheme `Y^reg`.

### Proof

The functor `Reg_Z` in `a110` is defined only in the comma category of
objects equipped with two signed-integer ruling maps.  Equation (1.1) shows
that a real factor supplies no such full integer map.  Hence a mixed chart
has at most the ruling map belonging to its finite factor, and a real-real
chart has neither.  Applying a functor outside its domain is ill-typed. QED.

This is not repaired by viewing `p` as a rational fraction: `Reg_Z` requires
an integral central scalar acting on every operation set, whereas a fraction
in `K` is not an element of the chart structure object `O`.

## 2. What survives

The following results do not use the invalid global step:

1. `a109` on the dense finite-finite affine plane, where both integer maps
   genuinely exist;
2. the literal Haran pro-square and its prime incidence/contact objects;
3. the arithmetic curve lattices and their unit-torsor pullbacks;
4. every presentation-level finite moment, RR, Green and gauge calculation.

Results `a110`--`a130` that require the globally reflected pro-square are now
conditional on a corrected gluing theorem.  Their internal algebraic
implications remain useful, but they do not currently prove existence on a
global `Y^reg`.

## 3. Correct local replacement

For a chart `A_alpha`, let `S_(alpha,i)` be the central scalar sections from
ruling `i` that actually lie in `O(A_alpha)` and occur as denominators in the
prime lattices under consideration.  Define

\[
 Reg_{S_\alpha}(A_\alpha)
 =A_\alpha/\bigcap_f\ker_{=}(f),                                      \tag{3.1}
\]

where `f` ranges over targets on which multiplication by every element of
the present systems `S_(alpha,i)` is injective.  On the finite-finite chart,
(3.1) is `Reg_Z`.  On a real chart, a scalar such as `1/p` may already be a
bounded section and no nonexistent integral scalar `p` is imposed.

The new exact gate is:

> **H7-LOCAL-REG-GLUE.** Prove that the relative reflections (3.1) commute
> with the actual central localizations on every overlap, glue independently
> of the chosen standard cover, respect pro-transitions, preserve the real
> unit-ball charts, and make every local multiplier occurring in each
> `L_(p,i)` admissible where it is used.

Only after H7-LOCAL-REG-GLUE may one reinstate a global repaired square,
prime completed lattices on it, H7-ARCH-BDRY and the downstream geometric
descent claims.

## 4. Consequence for row A

This correction moves the first live G-7 gate earlier than H7-ARCH-BDRY.
The finite affine repair is real progress, and the presentation-level RR
package remains valid, but the global space carrying it is not yet built.
Row A and RH remain open.

## 5. Verification scope

`114_a_131_h7_global_reflection_type_verify.py` checks the scalar membership
failure on exhaustive real-chart samples, the domain hypothesis in `a110`,
the primary-source real-chart anchors and the corrected dependency scope.
The categorical conclusion is the domain-of-definition argument above.

**Later repair (`a132`).**  H7-LOCAL-REG-GLUE is proved supportwise.  For a
finite prime set `T`, choose levels `N` divisible by its product and impose
`p_i`-regularity only on charts where `p_i` is an actual section.  On every
finite/real overlap those primes are units, so the relative reflections glue.
The directed pairs `(T,N)` define the corrected pro-square `Y^locreg`.
