# 114.a.49 — H7-UEMB closed by the homogeneous endomorphism bio

> **Further use (`a_74`).** On the positive orthant this full bio realizes
> the two additions as an ordinary sum and a power-conjugated sum.  Their
> mixed-Hessian connectivity faithfully reconstructs all unsigned read-once
> alternating trees, proving prime cancellation on that all-depth sector.

```
+--------------------------------------------------------------------------+
| TARGET      B^-(n)=multiplicatively homogeneous maps R^n -> R;          |
|             B^+(n)=columns x -> (a_1x,...,a_nx).                        |
| TWO FIELDS  Ordinary and u-twisted linear forms both map into B.         |
| COMMUTE     Haran's bio commutativity is exactly scalar homogeneity.     |
| INVOLUTION  D=B x B^op with factor-swap involution.                      |
| SEPARATE    A scalar a acts by x -> ax, hence evaluation at 1 recovers a.|
| RESULT      H7-UEMB(u) holds for every u>0.                              |
+--------------------------------------------------------------------------+
```

## 1. The homogeneous endomorphism bio

Let `M=(R,multiplication)` act on the set `R` by scalar multiplication, and
let `E=M-Set` with cartesian product carrying the diagonal action. Put

\[
 \mathcal B:=\operatorname{End}_{\mathcal E}(\mathbb R).                 \tag{1.1}
\]

Thus

\[
 \mathcal B^-(n)=
 \{f:\mathbb R^n\to\mathbb R:
 f(tx_1,\ldots,tx_n)=t f(x_1,\ldots,x_n)\},                              \tag{1.2}
\]

and every equivariant map `R -> R^n` is uniquely

\[
 c_a(x)=(a_1x,\ldots,a_nx),\qquad a=(a_1,\ldots,a_n)\in\mathbb R^n.       \tag{1.3}
\]

The assertion in (1.3) follows by evaluating at `1`; equivariance then gives
the value at every `x`, including `x=0`.

### Proposition 1.1

`B` is a commutative bio in Haran's sense.

### Proof

It is a bio by Haran 2022, Example 1.14. Composition of homogeneous maps is
homogeneous. Its plus operations are exactly the scalar columns (1.3), so
the mutual actions also stay in (1.2)--(1.3).

It remains to check Haran's commutativity identities (4.1)--(4.2). Moving a
column `c_a` through an `n`-ary minus operation `f` replaces

\[
 f(a_i x_1,\ldots,a_i x_n)
 \quad\text{by}\quad
 a_i f(x_1,\ldots,x_n),                              \tag{1.4}
\]

which is precisely (1.2). After the block permutation `sigma_{m,n}`, both
sides of (4.1) reduce to the identity

\[
 f\bigl(a_i g(x_1,\ldots,x_n)\bigr)_{i=1}^m
 =f\bigl(g(a_i x_1,\ldots,a_i x_n)\bigr)_{i=1}^m,       \tag{1.5}
\]

for homogeneous `g`; corresponding untouched inputs may be inserted on both
sides. Equation (1.5) holds coordinate by coordinate by (1.2). The dual
identity (4.2) has the same calculation, because every plus operation is a
column. Hence both defining commutativity equations hold.
QED.

## 2. Simultaneous regular representations

Let `R_1` and `R_u` be the two fields of `a_39`. For either field law
`+_(v)`, the regular representation sends a row `a=(a_i)` to

\[
 L_a^{(v)}(x_1,\ldots,x_n)
   =\mathop{+_{(v)}}_i a_i x_i,                         \tag{2.1}
\]

and sends a column to (1.3). Distributivity over the common multiplication
gives

\[
 L_a^{(v)}(t x_1,\ldots,t x_n)=tL_a^{(v)}(x_1,\ldots,x_n).                \tag{2.2}
\]

Consequently the full and faithful ring-bio embedding, followed by the
regular action, gives bio maps

\[
 \varphi_1:\mathcal P_1\longrightarrow\mathcal B,
 \qquad
 \varphi_u:\mathcal P_u\longrightarrow\mathcal B.                      \tag{2.3}
\]

They agree on `F`. More strongly, they agree on every unary real scalar:

\[
 \varphi_1(a)(x)=ax=\varphi_u(a)(x),                                    \tag{2.4}
\]

because unary linear forms use multiplication but not addition.

## 3. Restoring the involution

The bio `B` need not be self-dual. Form instead

\[
 \mathcal D:=\mathcal B\times\mathcal B^{op},                            \tag{3.1}
\]

with involution exchanging the two factors. Products and opposites preserve
the equational commutativity identities, so `D` is a commutative involutive
bio.

For a self-dual ring bio `P_v`, the map

\[
 \Phi_v=(\varphi_v,\varphi_v^{op}\circ t):
 \mathcal P_v\longrightarrow\mathcal D                                 \tag{3.2}
\]

is involution preserving. Equations (2.3)--(2.4) show that `Phi_1` and
`Phi_u` agree on `F` and on all common unary scalars. Therefore the universal
property of `Q_u` from `a_40` gives

\[
 \overline\Phi_u:\mathcal Q_u\longrightarrow\mathcal D.                 \tag{3.3}
\]

## 4. Unary embedding theorem

### Theorem 4.1

For every `u>0`, the canonical map

\[
 \eta_u:(\mathbb R,\cdot)\longrightarrow\mathcal Q_u(1)                 \tag{4.1}
\]

is injective. Hence H7-UEMB(u) holds for every `u>0`.

### Proof

Under (3.3), `eta_u(a)` maps in both factors to scalar multiplication
`m_a:x -> ax`. If `eta_u(a)=eta_u(b)`, then `m_a=m_b`. Evaluating at `1`
gives `a=b`. QED.

### Corollary 4.2

The universal `Q_u` is noncollapsed. For `u!=1`, its two addition generators
are distinct, since equality would give `eta_u(2)=eta_u(2^u)`, contradicting
Theorem 4.1. Thus H7-TBIO is closed, and the power-evaluation descent required
for the Laurent sector in `a_26` and the finite-moment separation in `a_33`
is unconditional.

This does not construct H7-DYNAMIC-LIFT or H7-RR0. It closes the scalar/bio
gate, not the geometric correspondence or Riemann--Roch gates.

## 5. Verification scope

`114_a_49_h7_homogeneous_endobio_verify.py` builds a finite exact analogue
using two transported field additions with the same multiplication. It checks
field laws, homogeneity, the commutativity move, common unary action and
scalar separation. The proof above establishes the real/categorical result.
