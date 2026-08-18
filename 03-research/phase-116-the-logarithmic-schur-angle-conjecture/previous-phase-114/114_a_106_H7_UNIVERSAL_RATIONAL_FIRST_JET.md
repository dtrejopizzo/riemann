# 114.a.106 — H7: the universal rational first jet is prime-regular

```
+------------------------------------------------------------------------+
| CORRECTION  C Omega -> N is not injective; an entropy cocycle survives. |
| UNIVERSAL   M_Q=C Omega(F(Z)/F{+-1}) tensor Q.                          |
| TARGET      H_Q=F(Z) Pi M_Q is prime-regular in every arity.            |
| REDUCTION   Every source p-collision is invisible to both ordered       |
|             universal rational first jets.                              |
| REMAINS     Integral torsion in C Omega and genuinely higher jets.       |
+------------------------------------------------------------------------+
```

## 1. The omitted injectivity claim in the source is false

Let

\[
 \Omega_C=C\Omega\bigl(F(\mathbb Z)/F\{\pm1\}\bigr).          \tag{1.1}
\]

Haran gives a surjection

\[
 \bar\partial:\Omega_C\twoheadrightarrow\ker(N\to F(\mathbb Z))
                                                                    \tag{1.2}
\]

and comments out, without proof, the assertion that it is injective.  We
now give an exact counterexample already in arity `(1,1)`.

Let `V(n)` be the vector of prime valuations of `|n|` in the free abelian
group

\[
 L=\bigoplus_{\ell\ {m prime}}\mathbb Z e_\ell,qquad V(0)=0,
                                                                    \tag{1.3}
\]

and put

\[
 q(n)=nV(n),\qquad
 f(a,b)=q(a)+q(b)-q(a+b).                                    \tag{1.4}
\]

The map `q` is odd and obeys

\[
 q(\lambda n)=\lambda q(n)+\lambda nV(\lambda).               \tag{1.5}
\]

Therefore `f` is a normalized symmetric two-cocycle and

\[
 f(\lambda a,\lambda b)=\lambda f(a,b).                       \tag{1.6}
\]

On the generators in Haran's Theorem 7.8.1 define

\[
 \mathscr E\!\left([a|b,b']\right)=a f(b,b'),\qquad
 \mathscr E\!\left([a,a'|b]\right)=b f(a,a').                 \tag{1.7}
\]

### Proposition 1.1

Formula (1.7) descends to a homomorphism

\[
 \mathscr E:(\Omega_C)_{1,1}\longrightarrow L.                \tag{1.8}
\]

### Proof

Normalization and symmetry of `f` give the zero and commutativity
relations.  The identity `delta^2 q=0` is exactly each associativity
relation.  For the almost-linear relation, both sides evaluate to

\[
 (b_1+b_2)f(a_1,a_2)+(a_1+a_2)f(b_1,b_2).                    \tag{1.9}
\]

Oddness gives `f(a,-a)=0`, proving cancellation.  Equations (1.5)--(1.6)
give the sign and scalar-transfer relations.  These are all relations in
the cited presentation.  QED.

Now

\[
 \mathscr E([1,1|1])=f(1,1)=-2e_2\ne0.                       \tag{1.10}
\]

But

\[
 \bar\partial[1,1|1]=[1|1]+[1|1]-[2|1]=0\quad\text{in }N,    \tag{1.11}
\]

by scalar transfer.  Thus `[1,1|1]` has infinite order and lies in the
kernel of (1.2).

### Corollary 1.2

The commented injectivity assertion `C Omega -> N` is false.  Consequently
the explicit `N`-jets of `a105` do not exhaust universal first-order data.

Composing `e_l -> log l` turns (1.8) into the familiar real cocycle from
`q(n)=n log|n|`; no analytic approximation is used in the proof above.

## 2. A prime-regular universal rational target

Rationalize the universal commutative module aritywise:

\[
 M_{\mathbb Q}=\Omega_C\otimes_{\mathbb Z}\mathbb Q.           \tag{2.1}
\]

The `F(Z)`-module actions and involution are group homomorphisms, hence
extend uniquely to (2.1); commutativity is preserved.  Let

\[
 H_{\mathbb Q}=F(\mathbb Z)\Pi M_{\mathbb Q}.                  \tag{2.2}
\]

### Proposition 2.1

Every prime acts injectively on every operation set of `H_Q`.

### Proof

For every finite `Y,X`,

\[
 (H_{\mathbb Q})_{Y,X}
 =\mathbb Z^{Y\times X}\times(M_{\mathbb Q})_{Y,X}.            \tag{2.3}
\]

The first factor is free abelian and the second is a rational vector space.
The relative universal derivation vanishes on `F{+-1}`, and its scalar prime
has derivative zero, so `p` acts as `(a,m)->(pa,pm)`.  Both coordinates
cancel `p`.  QED.

## 3. The stronger collision localization

Let `d_Q:F(Z)->M_Q` be the rationalized universal derivation.  The two ruling
pairs

\[
 x_1\mapsto(x,0),\ x_2\mapsto(x,d_Qx),
 \qquad
 x_1\mapsto(x,d_Qx),\ x_2\mapsto(x,0)                         \tag{3.1}
\]

induce maps `J^Q_12,J^Q_21:P->H_Q` from the full signed plane.

### Theorem 3.1 (universal rational first-jet collision theorem)

For every prime, arity and pair of operations,

\[
 pF=pG\quad\Longrightarrow\quad
 J^{\mathbb Q}_{12}(F)=J^{\mathbb Q}_{12}(G),\qquad
 J^{\mathbb Q}_{21}(F)=J^{\mathbb Q}_{21}(G).                  \tag{3.2}
\]

### Proof

Apply the two maps and cancel `p` by Proposition 2.1.  QED.

This strictly sharpens `a105`: the entropy class (1.10) is invisible in `N`
but nonzero after rationalization, so it is retained by the universal
rational jet.

## 4. Exact remaining gate

Any failure of H7-PRIME-REG is now confined to the common equality kernel of
the two maps in (3.1).  At first order, this kernel can contain only integral
torsion in `Omega_C`; rational non-torsion first-order classes are separated.
It can also contain genuinely nonlinear/higher-order differences.

The next exact alternatives are therefore:

1. prove `Omega_C` torsion-free and use the integral universal first jet;
2. construct universal rational jets/principal parts of all orders and prove
   their joint faithfulness; or
3. prove p-CONVEX/p-DIVPATH directly inside the common rational-jet kernel.

None is asserted here.  H7-PRIME-REG, the completed lattice and row A remain
open.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Theorem 7.8.1 and the exact sequence immediately following it.

## 5. Verification scope

`114_a_106_h7_universal_rational_jet_verify.py` verifies all defining
relations of (1.7) exactly on exhaustive bounded integer boxes, proves the
nonzero kernel value in the free prime-valuation group, and checks prime
cancellation in rationalized jet coordinates.  Exhaustion supports the
displayed symbolic proof; it does not prove faithfulness of the jet pair.

**Later resolution (`a107`--`a108`).**  The scalar integral universal
differential is two free prime copies plus one `Z/2`; its torsion generator
integrates to the nonzero plane scalar `kappa` killed by `2`.  Thus the
rational target is regular precisely because it discards the obstruction,
and full H7-PRIME-REG is false.
