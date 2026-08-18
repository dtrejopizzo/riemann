# 114.a.39 — Twisted-field scalar models and the exact bio-lift gate

```
+--------------------------------------------------------------------------+
| MODEL       T_u(x)=sgn(x)|x|^(1/u) transports ordinary addition to a    |
|             second field addition sharing the usual multiplication.      |
| MOMENT      The second integer n becomes sgn(n)|n|^u, exactly the power  |
|             character required by a_25-a_26.                             |
| NON-TOTAL   For u!=1 the two additions differ; Boardman-Vogt             |
|             interchange would force them equal.                          |
| LIMIT       Two scalar field laws do not by themselves define Haran's    |
|             higher-arity operations, co-operations, actions or           |
|             involution.                                                   |
| RESOLVED    a_40 constructs the universal bio and a_49 proves its unary  |
|             embedding; H7-TBIO and power-evaluation descent are closed.  |
+--------------------------------------------------------------------------+
```

## 1. Transported field addition

Fix `u>0` and define the multiplicative bijection

\[
 T_u:\mathbb R\longrightarrow\mathbb R,
 \qquad T_u(x)=\mathrm{sgn}(x)|x|^{1/u}.          \tag{1.1}
\]

It fixes `0,1,-1` and satisfies `T_u(xy)=T_u(x)T_u(y)`. Define

\[
 x+_{(2,u)}y
 :=T_u^{-1}\bigl(T_u(x)+T_u(y)\bigr).                  \tag{1.2}
\]

### Proposition 1.1

The structure

\[
 \mathbb R_u=(\mathbb R,+_{(2,u)},\cdot,0,1)           \tag{1.3}
\]

is a field, and `T_u:R_u -> R` is a field isomorphism. Its multiplication
is the usual real multiplication, shared with the ordinary field structure.

### Proof

All additive field axioms transport through the bijection `T_u`.
Multiplicativity of `T_u` gives

\[
 T_u\bigl(z(x+_{(2,u)}y)\bigr)
 =T_u(z)(T_u(x)+T_u(y)),                                \tag{1.4}
\]

which is the image of `zx+_(2,u)zy`; hence multiplication distributes.
The multiplicative unit and inverses are unchanged. QED.

## 2. The exact power-character integer map

Let `i_{2,u}:Z -> R_u` be the unique unital ring map. Since the `n`-fold
second sum of `1` is transported from the ordinary integer `n`,

\[
 i_{2,u}(n)=T_u^{-1}(n)
 =\mathrm{sgn}(n)|n|^u.                          \tag{2.1}
\]

Keep the ordinary embedding

\[
 i_1(n)=n.                                              \tag{2.2}
\]

Therefore any common scalar object containing both field laws would send

\[
 i_1(a)i_2(b)longmapsto
 a\mathrm{sgn}(b)|b|^u,                          \tag{2.3}
\]

exactly the character `E_u` required in `a_25` and `a_26`.

This explains the power evaluations structurally: they are not arbitrary
analytic probes but the scalar shadows of multiplicatively conjugate field
additions.

## 3. Why the model is genuinely non-total

For `u!=1`, the additions differ. For example,

\[
 1+_{(2,u)}1=2^u\ne2=1+_{(1)}1.                        \tag{3.1}
\]

The Boardman--Vogt interchange for two binary additions would include the
medial identity

\[
 (a+_{(2)}b)+_{(1)}(c+_{(2)}d)
 =(a+_{(1)}c)+_{(2)}(b+_{(1)}d).                       \tag{3.2}
\]

Putting `b=c=0` makes (3.2) say

\[
 a+_{(1)}d=a+_{(2)}d                                   \tag{3.3}
\]

for all `a,d`. Thus total interchange would force equality of the two
additions, contradicting (3.1). The scalar model has exactly the kind of
non-totality needed to avoid the collapse of `a_38`.

## 4. The missing higher-arity structure

A Haran commutative bio is not specified by its scalar monoid and two binary
operations. It also contains:

1. symmetric operations in every arity on both the minus and plus sides;
2. operadic compositions and mutual actions;
3. naturality and co-naturality relations (Haran 2022, (1.9)--(1.12));
4. commutativity relations (4.1)--(4.2);
5. for the arithmetic square used here, an involution exchanging operations
   and co-operations.

Naively representing both sums as functions on the same set does not supply
the plus-side co-operations or an injective transpose. Hence Proposition 1.1
does **not** yet define a target of

\[
 \mathbb Z\boxtimes_{\mathbb F}\mathbb Z.              \tag{4.1}
\]

The exact construction gate is:

> **H7-TBIO.** For every `u>0`, construct a commutative involutive bio
> `Q_u` with scalar monoid containing `R`, two maps
> `P_Z -> Q_u` inducing (2.2) and (2.1), with `delta_1 != delta_2` whenever
> `u!=1`; prove all bio relations without imposing total interchange.

This gate is resolved by `a_40` and `a_49`: the universal quotient supplies
the bio relations, and the homogeneous-endobio representation proves that
its common real unary monoid embeds.

### Theorem 4.1 (conditional descent consequence)

If H7-TBIO holds for every `u>0`, then every power character `chi_u` of
`a_26` factors through `A_12`. Consequently H7-LNF holds, the bounded codes
of `a_30`--`a_35` are injective, and H7-FMD follows.

### Proof

The two maps from `P_Z` induce, by the coproduct universal property, a bio
map from (4.1) to `Q_u`. On the chosen first-additive scalar subring its
restriction is (2.3), so `chi_u` kills `J_Har`. This holds for every `u>0`.
Theorem 3.1 of `a_26` then gives `J_Har=0`; the remaining implications were
proved in `a_30`, `a_33` and `a_35`. QED.

Full H7-LNF would make raw scalar cardinality too large by `a_31`; Theorem
4.1 is therefore useful only with the normalized finite-moment dimension,
not with raw H7-U.

## 5. Relation to H7-WBASE

An H7-TBIO family would provide explicit non-total targets separating the
two rulings and would bypass the ordinary-target collapse of `a_38`.
However, scalar separation alone does not transport Witt graphs or define
their intersection. A solution of H7-WBASE would still need a compatible
kernel/sheaf construction, and H7-WLEF would still need the trace formula.

Thus H7-TBIO is a common algebraic prerequisite for H7-FMD and a non-total
WBASE, not a solution of either geometric gate by itself.

By `a_49`, this prerequisite is now satisfied. H7-DYNAMIC-LIFT and the
global dimension/RR promotion remain independent open gates.

## 6. Verification scope

`114_a_39_h7_twisted_field_verify.py` checks multiplicativity, the transported
field laws, distributivity, the integer power character and failure of total
interchange on exact rational exponents/sample grids. It does not construct
the higher-arity bio required by H7-TBIO; that later construction and its
unary faithfulness are verified in `a_40` and `a_49`.
