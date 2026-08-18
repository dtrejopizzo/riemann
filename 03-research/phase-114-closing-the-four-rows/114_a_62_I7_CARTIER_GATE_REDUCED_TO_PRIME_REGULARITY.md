# 114.a.62 — I7: prime regularity is the denominator gate, not yet Cartier

> **Type correction (`a_66`).** The earlier short exact sequence in
> `O_Y`-modules and its `Tor_1` reformulation are retracted.  Haran's
> structure sheaf is generalized-ring-valued, whereas his abelian modules
> are separately linearized objects.  The source does not identify the two.
>
> **Partial repair (`a_67`).** Using equivalence ideals instead, the ruling
> is the principal quotient `D_Y(p)`. Under H7-PRIME-REG its ideal is an
> invertible principal right act and its restriction to the ordinary diagonal
> has layers `p^k Z_(p)/p^(k+1) Z_(p)=F_p`. No global conormal Ab-module or
> `Tor` is asserted.

```
+-------------------------------------------------------------------------+
| CURVE       p is regular and L_p is the inverse-uniformizer bundle.     |
| SQUARE      V_p=x_p x_S X is a literal closed prime ruling.             |
| EXACT GATE  p must satisfy Haran's all-arity regularity condition.      |
| PAYOFF      Then 1/p is an admissible square-side K denominator.        |
| OPEN        Cartier ideals, normal modules and Tor need extra theory.   |
+-------------------------------------------------------------------------+
```

## 1. Curve-side facts

For `X=overline{Spec Z}`, the finite-prime neighbourhood is ordinary and
`p` is a non-zero-divisor there.  Haran (11.17)--(11.19) gives the completed
inverse-uniformizer bundle

\[
 L_p,\qquad \widehat\deg L_p=\log p.                                  \tag{1.1}
\]

The closed point is `x_p=Spec F_p`.  These statements require no square-side
Cartier formalism.

## 2. The literal ruling and the exact denominator condition

Let

\[
 Y=X\times_SX,\qquad V_p=x_p\times_SX.                                \tag{2.1}
\]

The fiber-product identity and diagonal incidence are unconditional:

\[
 \Delta\times_YV_p\simeq x_p.                                        \tag{2.2}
\]

To pull the local rational generator `1/p` of `L_p` into the Section-11
fraction sheaf on `Y`, equation (11.1) requires

\[
 pa=pa'\Longrightarrow a=a'                                         \tag{2.3}
\]

for every relevant open, later pro-level and operation arity.  This is
H7-PRIME-REG.  In the tree presentation it is the saturation condition of
`a_64`.

Under H7-PRIME-REG, `p` belongs to Haran's denominator system and `1/p`
defines the expected **completed lattice** on the square. `a_67` additionally
constructs the regular principal quotient/right-act datum and its ordinary
diagonal-normal shadow. This is a typed Cartier analogue, but not a global
abelian conormal theory.

## 3. Why the previous `Tor` reduction was ill-typed

Haran Section 6 modules are abelian-group-valued.  By contrast,
`O_Y(U)_{d,d'}` consists of generalized-ring operations.  The source does
not make `O_Y` itself an object of that abelian module category.  Therefore
the displayed sequence

\[
 p_1^*\mathcal O_X(-x_p)\xrightarrow p\mathcal O_Y
 \longrightarrow\mathcal O_{V_p}\longrightarrow0                    \tag{3.1}
\]

from the previous version was not a typed short exact sequence there, and
its claimed equivalence with a `Tor_1` vanishing is withdrawn.

Section 6 makes `A-mod` an abelian category and supplies extension of scalars
and cotangent modules, so a module-valued linearization can be sought.  It
does **not**, in the cited passage, specify a canonical free rank-one object
`A^[1]` with automorphism group `GL_1(A)`.  Thus even the first linearization
step needs a construction.  After it, at least two further comparison
theorems would be needed:

1. identify the linearized quotient by `p` with the module of the closed
   fiber `V_p`;
2. compare that module-theoretic construction with the Section-11 lattice
   and a divisor theory.

Neither theorem is in the cited source or proved in phase 114.

`a_134` records the full torsor-to-module gate and retracts the unsupported
`A^[1]` shorthand without retracting any of the typed right-act results.

## 4. Correct status

- curve prime bundle and degree: **closed**;
- literal ruling and diagonal incidence: **closed**;
- square completed generator `1/p`: conditional on H7-PRIME-REG;
- principal generalized Cartier right act and ordinary diagonal filtration:
  **closed conditional on H7-PRIME-REG** by `a_67`;
- global abelian conormal filtration and derived incidence: **open**;
- the underlying-site contact sheaf of `a_46`: unaffected, but not obtained
  from a Cartier normal layer.

## 5. Verification scope

`114_a_62_i7_cartier_prime_regularity_verify.py` is updated to check the
ordinary curve model, the all-arity source definition and the distinction
between operation sets and abelian modules.  It no longer reports a
`Tor_1` equivalence.
