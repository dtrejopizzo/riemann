# 114.a.60 — G-3 closed as a boundary: the effectivity branch is RH-equivalent

```
+--------------------------------------------------------------------------+
| SOURCE      No class of D^o is strictly effective (113_10 Cor 2.4).     |
| TARGET      On a4-weak, q(L)>0 implies L or -L is strictly effective.   |
| MAP         q(J(c))>=s(c,c) and exact sign-sensitive effectivity.       |
| FORWARD     If s(c,c)>0, one target sign becomes effective: impossible. |
| CONVERSE    Under RH, map every c to sqrt(-s(c,c)/2)*(1,-1).            |
| THEOREM     G3-EFF exists iff RH.                                       |
| STATUS      Every meaningful G-3 branch is now RH-equivalent.           |
+--------------------------------------------------------------------------+
```

## 1. Strict effectivity on source and target

Use the repaired basepoint convention of `a_08`: the zero class is on the
boundary and is not **strictly** effective.

On the source, 113_10 Corollary 2.4 gives

\[
 D^\circ\cap\operatorname{Eff}=\{0\}.                                   \tag{1.1}
\]

Therefore no class of `D^o`, including zero under the strict convention, is
strictly effective; the same holds for its negative.

On the rank-two divisor plane of the a4-weak surface, write

\[
 V=\mathbb R f_v\oplus\mathbb R f_h,
 \qquad q(kf_v+af_h)=2ka,                                                \tag{1.2}
\]

and use the strict cone

\[
 \operatorname{Eff}_{\rm str}(V)
 =\{(k,a):k\ge0,\ a\ge0,\ (k,a)\ne(0,0)\}.                            \tag{1.3}
\]

Theorem 4.1(4) of `a_02` gives the relevant property:

\[
 q(v)>0\quad\Longrightarrow\quad
 v\in\operatorname{Eff}_{\rm str}
 \text{ or }-v\in\operatorname{Eff}_{\rm str}.                         \tag{E}
\]

Indeed `q(v)>0` means that its two coordinates have the same nonzero sign.

## 2. The exact G3-EFF conditions

A G3-EFF map for this target is a set map

\[
 J:D^\circ_{\mathbb R}\longrightarrow V                                \tag{2.1}
\]

such that:

1. `J(tc)=tJ(c)` for `t>=0`;
2. `q(J(c))>=s(c,c)` for every `c`;
3. for both signs, strict source effectivity is equivalent to strict target
   effectivity.

By (1.1), condition 3 is simply

\[
 J(c),-J(c)\notin\operatorname{Eff}_{\rm str}(V)
 \qquad(c\in D^\circ).                                                    \tag{2.2}
\]

No additivity, continuity, polarization or Kunneth law is assumed.

## 3. Equivalence theorem

### Theorem 3.1

A G3-EFF map (2.1) exists if and only if the Riemann hypothesis holds.

### Proof: G3-EFF implies RH

If RH fails, the phase-113 index theorem gives a real `c in D^o` with

\[
 s(c,c)>0.                                                               \tag{3.1}
\]

Domination gives `q(J(c))>0`. Property (E) then makes `J(c)` or `-J(c)`
strictly effective, contradicting (2.2). Hence `s(c,c)<=0` for all real
`c in D^o`, which is equivalent to RH by 113_14 Theorem 5.2.

### Proof: RH implies G3-EFF

Assume RH, so `s(c,c)<=0` on `D^o`. Put

\[
 K=f_v-f_h=(1,-1),\qquad q(K)=-2,                                      \tag{3.2}
\]

and define

\[
 J(c)=\sqrt{\frac{-s(c,c)}2}\,K.                                       \tag{3.3}
\]

Then positive quadratic homogeneity gives `J(tc)=tJ(c)` for `t>=0`, and

\[
 q(J(c))=s(c,c).                                                         \tag{3.4}
\]

Every nonzero image lies on the mixed-sign ray `(u,-u)`, so neither it nor
its negative belongs to (1.3). If `s(c,c)=0`, the image is zero, which is not
strictly effective. Thus (2.2) holds and `J` is G3-EFF. QED.

Formula (3.3) is deliberately tautological and is not evidence for RH. Its
role is to prove the converse and identify the logical strength of the gate.

## 4. Final G-3 classification

Combining `a_13`, `a_59` and Theorem 3.1:

| G-3 formulation | exact status |
|---|---|
| pointwise domination + homogeneity | always exists, vacuous |
| additive Lorentzian domination | RH-equivalent |
| non-additive two-point polarization/Kunneth domination | RH-equivalent |
| pointwise domination + exact strict-effectivity dictionary | RH-equivalent |

Thus G-3 is no longer an unspecified open construction. Every formulation
strong enough to connect the phase-113 space to the a4-weak Hodge/effectivity
engine is equivalent to RH; weakening below these formulations gives the
vacuous collapse of `a_13`.

This does not prove RH. It proves that constructing G-3 cannot be advertised
as a prior unconditional lemma: in its remaining effectivity form it **is the
RH step**.

The full effectivity dictionary outside `D^o` remains a separate row-A/R8
compatibility problem.

## 5. Verification scope

`114_a_60_g3_effectivity_equivalence_verify.py` checks the Lorentzian form and
strict cone, property (E), the spatial-ray construction for many exact
negative-semidefinite samples, positive homogeneity, domination, and the
contradiction produced by a positive source square. The equivalence between
`s<=0` on `D^o` and RH is the phase-113 theorem cited above.
