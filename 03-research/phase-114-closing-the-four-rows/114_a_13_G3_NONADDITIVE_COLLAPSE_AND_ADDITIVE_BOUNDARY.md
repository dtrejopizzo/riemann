# 114.a.13 — G-3 delimited exactly: additive domination is RH-equivalent; non-additive domination is vacuous

```
+--------------------------------------------------------------------------+
| ADDITIVE     An additive Q-homogeneous domination into a Lorentzian      |
|              target exists iff RH (114_d3_03 Thm 6.5, proof repaired).   |
| NONADDITIVE  Positive homogeneity plus q(iota c)>=s(c,c) is automatic:   |
|              every class can be collapsed onto one positive ray.        |
| CONSEQUENCE  A meaningful G-3 must transport two-point/polarization or   |
|              effectivity data. Pointwise self-intersection is too weak. |
+--------------------------------------------------------------------------+
```

## 1. The additive boundary

Let `(D^o_R,s)` be the phase-113 quadratic space.  Theorem 6.5 of
`114_d3_03`, with its rational-density proof now made explicit, states:

> For any real quadratic space `(V,q)` with `n_+(q)<=1`, the existence of an
> additive, `Q`-homogeneous map `iota:D^o_R->V` satisfying
> `q(iota(c))>=s(c,c)` for every `c` is equivalent to RH.

The subtle point is that a `Q`-linear image need not itself be a real
subspace.  The correct proof chooses a positive real 2-plane with basis `u,v`,
uses the inequality first for rational combinations, proves `iota(u)` and
`iota(v)` real-linearly independent by rational approximation, and then
extends the inequality to all real combinations by continuity.  This produces
a genuine positive real 2-plane in `V`, contradicting `n_+(q)<=1`.

Thus the additive/Lorentzian version of G-3 is not merely open: it is exactly
RH-equivalent and cannot be used as an unconditional intermediate lemma.

## 2. Universal non-additive collapse

### Proposition 2.1

Let `(E,s)` be any real quadratic space and `(V,q)` any real quadratic space
containing `h` with `q(h)>0`. Define

\[
 J_h(c)=
 \sqrt{\frac{\max\{s(c,c),0\}}{q(h)}}\,h.                \tag{2.1}
\]

Then, for every `t>=0`,

\[
 J_h(tc)=tJ_h(c),\qquad
 q(J_h(c))=\max\{s(c,c),0\}\ge s(c,c).                  \tag{2.2}
\]

Unless `s<=0`, this map is generally non-additive and satisfies
`J_h(-c)=J_h(c)`.

### Proof

Quadratic homogeneity gives `s(tc,tc)=t^2s(c,c)`. Taking the nonnegative square
root proves the first identity. Substitution into `q` proves the second.
For example, if `s(e_1,e_1)=s(e_2,e_2)=1` and the vectors are orthogonal, then

\[
 J_h(e_1)+J_h(e_2)=\frac{2h}{\sqrt{q(h)}},\qquad
 J_h(e_1+e_2)=\frac{\sqrt2h}{\sqrt{q(h)}},
\]

so additivity fails. QED.

### Corollary 2.2 (an arithmetic target already exists)

Take the toric arithmetic surface of `114_a_07` and its positive class
`H=(1,1)`, for which `H^2=2`. Formula (2.1) with `h=H` gives a positively
homogeneous pointwise-dominating map into its Lorentzian real divisor space,
unconditionally.

This map is deliberately tautological: it is defined from `s(c,c)` itself,
collapses all positive directions onto one ray, transports no mixed pairing,
and identifies `c` with `-c`. Therefore it supplies neither a divisor-group
homomorphism nor the effectivity dictionary required by row (a).

## 3. Exact meaning of G-3 after this result

The following hierarchy is now rigorous:

| requested structure | status |
|---|---|
| pointwise domination, positive homogeneity | ALWAYS EXISTS; no RH content |
| additive `Q`-homogeneous domination into Lorentzian target | RH-EQUIVALENT |
| isometric additive realization | RH-EQUIVALENT, stronger formulation |
| source-defined non-additive realization with exact effectivity | RH-EQUIVALENT by `a_60` |

Consequently a future non-additive G-3 proposal must include at least one
condition that rules out (2.1), for example:

1. a two-point polarization identity or inequality;
2. compatibility with addition on an explicitly generated positive plane;
3. a section/effectivity functor distinguishing `c` from `-c`;
4. a Kunneth law coupling independent divisor directions.

Without such a condition, “escaping additivity” merely hides every positive
direction on the same ray and cannot contribute to a proof of RH.

**Later sharpening (`a_59`).** The polarization/Kunneth alternatives in
items 1, 2 and 4 are already RH-equivalent if they imply
`q(aJ(c)+bJ(d))>=s(ac+bd)` for every pair and every real `a,b`; no additivity
of `J` is needed. Therefore the only structured branch not eliminated here
is item 3: the exact effectivity/section dictionary G3-EFF, without two-point
linearized domination.

**Final sharpening (`a_60`).** On `D^o`, no class is strictly effective,
whereas the a4-weak target has property (E): every positive-square class has
an effective sign. Hence G3-EFF plus pointwise domination implies
`s<=0` on `D^o`, i.e. RH. Conversely RH gives the explicit spatial collapse
`J(c)=sqrt(-s(c,c)/2)(1,-1)`, whose two signs are never strictly effective.
Thus G3-EFF is RH-equivalent too. G-3 is fully delimited: meaningful versions
are RH-equivalent, weaker ones are vacuous.

## 4. Circularity

No RH assumption is used in Proposition 2.1.  Conversely, its formula depends
explicitly on `s(c,c)`, so it is not a source-defined geometric realization
and must not be advertised as evidence for RH.  Its purpose is negative and
precise: it identifies the minimum extra structure G-3 must demand.

`114_a_13_g3_boundary_verify.py` checks (2.2), its homogeneity, and a concrete
failure of additivity.
