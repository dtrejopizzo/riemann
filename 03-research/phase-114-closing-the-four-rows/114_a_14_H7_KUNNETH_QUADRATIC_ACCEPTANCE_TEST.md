# 114.a.14 — H7 Künneth acceptance test: pure external sections cannot give quadratic growth

```
+--------------------------------------------------------------------------+
| NO-GO        If each factor has log #B_m = O(m), then the set of pure    |
|              external products has log cardinality O(m), not O(m^2).    |
| REQUIRED     Quadratic growth needs Theta(m^2) independently usable      |
|              mixed generators, with collision and mass control.         |
| MODEL        The cross-polytope theorem a_11 supplies the exact binary   |
|              constant once such a rank/radius section model is realised.|
| LIMIT        No such identification with Haran sections is yet proved.   |
+--------------------------------------------------------------------------+
```

## 1. Pure-section no-go

Let `B_m` and `C_m` be finite bounded section sets on the two copies of the
compactified arithmetic curve, and let

\[
 \boxtimes:B_m\times C_m\longrightarrow H^0(Y,L_m\boxtimes M_m) \tag{1.1}
\]

be the external multiplication constructed in `114_a_12`.

### Theorem 1.1

If

\[
 \log|B_m|=O(m),\qquad \log|C_m|=O(m),                   \tag{1.2}
\]

then the set `P_m` of pure external sections in the image of (1.1) satisfies

\[
 \log|P_m|\le\log|B_m|+\log|C_m|=O(m).                  \tag{1.3}
\]

In particular, pure products cannot establish a surface law
`log #H^0=Theta(m^2)`.

### Proof

The image of any map has cardinality at most that of its domain, so
`|P_m|<=|B_m||C_m|`. Take logarithms and use (1.2). QED.

This remains true even if (1.1) is injective. Therefore injectivity of the
external section map, while desirable, is not the missing Künneth theorem.

## 2. What a quadratic Künneth theorem must prove

Suppose the two curve directions provide generating families `F_m` and `G_m`
with cardinalities `Theta(m)`. Their formal mixed family has

\[
 |F_m\times G_m|=\Theta(m^2).                            \tag{2.1}
\]

If a coefficient alphabet with at least two choices can be used independently
on a positive proportion of these pairs, then it can produce
`exp(Omega(m^2))` sections. But this conclusion requires all of:

1. **mixed generation:** the Haran section object contains the required sums
   of pure external products;
2. **noncollision:** distinct admissible coefficient arrays give distinct
   sections;
3. **mass/properness:** those arrays stay in the intrinsic real boundedness
   condition;
4. **upper control:** all bounded sections have at most `exp(O(m^2))`
   descriptions modulo the defining relations.

These are logical requirements, not four independent conjectures: omitting
any one invalidates the quadratic count.

`114_a_23` adds a logically prior requirement:

0. **intrinsic rank/arity:** the component being counted must be fixed by the
   geometry (or normalized by a proved dimension invariant). Choosing input
   arity `Theta(m^2)` by hand manufactures quadratic entropy even in an
   ordinary one-dimensional contraction module.

### Definition 2.1 (H7-K acceptance test)

A proposed Haran Künneth construction passes H7-K only if it first specifies
a fixed scalar component, an intrinsic rank `r_m`, or a proved
arity-normalized dimension, and then supplies explicit families `A_m` of
sections and constants `c,C>0` such that

\[
 e^{c m^2}\le |A_m|
 \le \#H^0_{\mathrm{bounded}}(Y,mD)
 \le e^{C m^2}                                             \tag{2.2}
\]

for all sufficiently large `m`. Counting only pure tensors fails H7-K by
Theorem 1.1.

## 3. Relation with the closed G-1 problem

`114_a_11` proves for the Connes--Consani cross-polytope module that, when

\[
 r_m=mk+1,\qquad R_m=\lfloor e^{ma}\rfloor,
\]

its minimal signed-generator dimension obeys

\[
 \dim_{r_m}(R_m)\sim\frac{ka}{\log2}m^2.                 \tag{3.1}
\]

Thus the combinatorial rank/radius model needed after a successful Künneth
identification is already solved, including its constant. What is absent is a
functor or an explicit normal form identifying Haran's bounded sections with
that model.

Equation (3.1) may be applied only after proving:

- which Haran operation supplies the `r_m` independent coordinates;
- which real boundedness condition supplies `R_m`;
- that Haran equivalence relations preserve the cross-polytope normal form.

Without those statements, importing (3.1) would merely rename the toric model.

## 4. Updated G-7 status

| component | status |
|---|---|
| abstract external unit-torsor Picard and pure multiplication | HAVE (`a_66`) |
| completed bounded external sector | CONDITIONAL on H7-PB-REG (`a_63`) |
| pure products sufficient for quadratic growth | CLOSED NEGATIVELY (Thm 1.1) |
| exact mixed-generator acceptance test | HAVE (Def 2.1) |
| Haran mixed normal form satisfying H7-K | OPEN |
| intersection/Riemann--Roch compatible with H7-K | OPEN |

`114_a_20` now computes the prime-axis section sets exactly, constructs a
noncolliding `(m+1)(n+1)` pure grid, and proves a sharper no-go: every family
separated by diagonal restriction has logarithmic cardinality `O(m+n)`.
Therefore the H7-K lower bound must be separated by an intrinsically
off-diagonal normal form.

`114_a_14_h7_kunneth_verify.py` checks the cardinality inequalities and the
linear-versus-quadratic separation on exact integer models.
