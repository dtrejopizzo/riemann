# 114.a.36 — I7: faithful Witt operator correspondences and exact Lambda mass

```
+--------------------------------------------------------------------------+
| SOURCE      Haran 2022, (12.14), (12.35), (12.37), (13.37).             |
| ALGEBRA     V_m V_n=V_mn on the cyclotomic Witt Hilbert space.           |
| FAITHFUL    V_n phi_1=phi_n and the phi_n are an orthogonal basis.        |
| MASS        log|tr(lambda_1(V_n phi_1))|=log|Phi_n(1)|=Lambda(n).         |
| GAIN        Composition and arithmetic local mass coexist without the    |
|             rank-two quotient blindness.                                |
| OPEN        V_n are operators, not divisors/cycles on Haran's square;    |
|             geometric realization and intersection remain required.     |
+--------------------------------------------------------------------------+
```

## 1. Exact source type

For the compactified arithmetic curve, Haran constructs

\[
 \mathcal W=\bigoplus_{n\ge1}\mathbb Z\phi_n,          \tag{1.1}
\]

where `phi_n` is the primitive cyclotomic orbit. After complexification and
completion with respect to the state `int`, equation (12.35) gives

\[
 \mathcal H=\widehat{\mathcal W}_{\mathbb C},\qquad
 \langle\phi_m,\phi_n\rangle
 =\delta_{mn}\varphi(n).                               \tag{1.2}
\]

The Frobenius endomorphisms `F_n` have adjoints (Verschiebung operators)

\[
 V_n:=F_n^*,\qquad V_n\phi_m=\phi_{nm},                \tag{1.3}
\]

and (12.37) states

\[
 V_mV_n=V_{mn}.                                        \tag{1.4}
\]

These are endomorphisms of a Witt/Hilbert object associated with the
**curve**. They are not asserted in the source to be pro-scheme maps of the
curve, graphs in its square, or divisor classes.

## 2. Faithful correspondence algebra

Let

\[
 \mathscr C_{\rm op}=\mathbb Z[\mathbb N_{>0}^{\times}]\n+ =\bigoplus_{n\ge1}\mathbb Z\Gamma_n^{\rm op},
 \qquad \Gamma_m^{\rm op}\Gamma_n^{\rm op}
       =\Gamma_{mn}^{\rm op}.                           \tag{2.1}
\]

Define

\[
 \rho_{\rm op}:\mathscr C_{\rm op}\longrightarrow
 \operatorname{End}_{\mathbb C}(\mathcal H),
 \qquad \Gamma_n^{\rm op}\longmapsto V_n.             \tag{2.2}
\]

### Theorem 2.1

The representation (2.2) is an injective algebra homomorphism.

### Proof

Multiplicativity is (1.4). If a finite sum satisfies

\[
 \sum_na_nV_n=0,                                       \tag{2.3}
\]

apply it to the cyclic vector `phi_1`. Equation (1.3) gives

\[
 \sum_na_n\phi_n=0.                                    \tag{2.4}
\]

The vectors `phi_n` are orthogonal and nonzero by (1.2), so every `a_n=0`.
QED.

Thus the full multiplicative label `n`, including its prime-power data, is
retained. This algebra does not factor through the blind rank-two invariants
`(r,m)` of `a_05`.

## 3. The exact von Mangoldt functional

Haran's equation (13.37), with `Phi_n(t)` denoting the usual cyclotomic
polynomial, is

\[
 \operatorname{tr}(\lambda_t(\phi_n))=\Phi_n(t).       \tag{3.1}
\]

For `n>=2`, define the operator-diagonal mass

\[
 I_{\rm op}(\Gamma_n^{\rm op},\Delta_{\rm op})
 :=\log\left|
 \operatorname{tr}\bigl(\lambda_1(V_n\phi_1)\bigr)
 \right|.                                              \tag{3.2}
\]

### Theorem 3.1

For every `n>=2`,

\[
 \boxed{\quad
 I_{\rm op}(\Gamma_n^{\rm op},\Delta_{\rm op})
 =\log|\Phi_n(1)|=\Lambda(n).
 \quad}                                                \tag{3.3}
\]

### Proof

By (1.3), `V_n phi_1=phi_n`; by (3.1), the expression inside the logarithm
is `Phi_n(1)`. The elementary cyclotomic identity is

\[
 \Phi_n(1)=
 \begin{cases}
 p,&n=p^k,\\
 1,&n>1\text{ is not a prime power}.
 \end{cases}                                           \tag{3.4}
\]

Taking logarithms gives the von Mangoldt function. QED.

This is not an arbitrary assignment of `Lambda(n)`: the mass is recovered
from the cyclic vector, Verschiebung action, lambda-ring operation and trace
already present in the Witt object.

## 4. Comparison with the literal Haran square

The constructions `a_17`--`a_19` provide on

\[
 Y=X\times_{\operatorname{Spec}\mathbb F\{\pm1\}}X
\]

the diagonal, prime-incidence carriers, nontrivial prime ruling classes and
an injective two-prime divisor lattice. They do not provide cycles
`Gamma_n` with composition.

Conversely, Theorems 2.1 and 3.1 provide composition and the exact local
mass but no map

\[
 \rho_{\rm geom}:\mathscr C_{\rm op}
 \longrightarrow\operatorname{CorrDiv}(Y).             \tag{4.1}
\]

The source's final Remark 12.42 explicitly distinguishes the adelic/Witt
action from the intersection theory on a surface and says that the latter
is still needed even in the function-field analogy.

The remaining I7 realization gate is therefore:

> **H7-I7-REAL.** Construct a correspondence/divisor object on `Y` and an
> injective multiplicative map (4.1) such that `rho_geom(Gamma_1^op)` is the
> diagonal, composition maps to correspondence composition, and
> \[
> \langle\rho_{\rm geom}(\Gamma_n^{\rm op}),\Delta\rangle_Y
> =I_{\rm op}(\Gamma_n^{\rm op},\Delta_{\rm op})
> =\Lambda(n).                                          \tag{4.2}
> \]

This gate is strictly sharper than the former request for unspecified
Frobenius maps: the source algebra, its faithful representation and its
required diagonal functional are now fixed.

## 5. Consequence for I7

I7 is closed **operatorially**:

1. the correspondence labels form a faithful multiplicative algebra;
2. its cyclic diagonal mass is exactly `Lambda(n)`;
3. neither datum descends to the blind toric rank-two quotient.

I7 remains open **geometrically** because no divisor/cycle realization on
the literal square and no geometric intersection pairing have been
constructed. Operator composition must not be called cycle composition
until H7-I7-REAL is proved.

## 6. Verification scope

`114_a_36_i7_witt_operator_verify.py` checks finite matrix models of the
Verschiebung composition, linear independence on the cyclic vector and the
cyclotomic/von-Mangoldt identity. It also checks the cited source anchors;
it does not assert H7-I7-REAL.
