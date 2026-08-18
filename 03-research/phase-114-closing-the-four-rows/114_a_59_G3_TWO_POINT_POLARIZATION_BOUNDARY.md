# 114.a.59 — G-3: two-point polarization is RH-equivalent without additivity

```
+--------------------------------------------------------------------------+
| MAP         J:E->V may be completely non-additive.                     |
| TWO-POINT   q(aJ(c)+bJ(d)) >= s(ac+bd) for every a,b.                  |
| TARGET      q is Lorentzian: n_+(q)<=1.                                |
| THEOREM     Such a J exists iff n_+(s)<=1, hence iff RH on D^o.         |
| CONSEQUENCE Exact polarization and quadratic Kunneth are already       |
|             circular; additivity was not the essential obstruction.     |
| SURVIVES    Only the effectivity/section-compatible non-additive branch.|
+--------------------------------------------------------------------------+
```

## 1. The exact two-point condition

Let `(E,s)` be a real quadratic space and `(V,q)` a real quadratic space
with `n_+(q)<=1`. No algebraic condition is imposed on a set map

\[
 J:E\longrightarrow V.                                                   \tag{1.1}
\]

Define the two-point linearized domination condition:

\[
 q(aJ(c)+bJ(d))
 \ge s(ac+bd,ac+bd)\qquad
 (c,d\in E,\ a,b\in\mathbb R).                         \tag{G3-POL}
\]

The coefficients act only after applying `J`; in particular G3-POL does
**not** assume

\[
 J(ac+bd)=aJ(c)+bJ(d).                                  \tag{1.2}
\]

### Theorem 1.1 (non-additive polarization boundary)

If a map into a target with `n_+(q)<=1` satisfies G3-POL, then
`n_+(s)<=1`. Conversely, when `n_+(s)<=1`, some such target and map exist.

### Proof

If `n_+(s)>=2`, choose `c,d` spanning an `s`-positive definite plane. For
every nonzero `(a,b)`, G3-POL gives

\[
 q(aJ(c)+bJ(d))>0.                                      \tag{1.3}
\]

First `J(c),J(d)` are linearly independent: a nontrivial relation would make
the left side zero while the right side is positive. Equation (1.3) then
makes `q` positive definite on their two-dimensional span, contradicting
`n_+(q)<=1`.

Conversely, if `n_+(s)<=1`, take `V=E`, `q=s` and `J` the identity. If a
fixed Lorentzian target containing an isometric copy is required, that copy
is an additional embedding condition; for the phase-113 equivalence under
RH one has the stronger fact `s|_(D^o)<=0`, so the zero map into any target
satisfies G3-POL. QED.

For the actual phase-113 space `D^o`, its positive index is even and equals
twice the number of off-line zero quadruples. Hence `n_+(s)<=1` is equivalent
to `n_+(s)=0`, i.e. RH. Therefore:

### Corollary 1.2

On `D^o`, the existence of a G3-POL map into any Lorentzian target is
equivalent to RH, even when `J` is not additive, homogeneous, measurable or
continuous.

This strictly strengthens the additive boundary of `a_13`.

## 2. Polarization and Kunneth formulations caught by the theorem

Write `B_q`, `B_s` for the polar bilinear forms. Any of the following implies
G3-POL and is therefore RH-equivalent on `D^o`:

1. exact two-point polarization
   \[
   B_q(J(c),J(d))=B_s(c,d),\quad q(J(c))=s(c,c);                         \tag{2.1}
   \]
2. positive-semidefinite Gram domination
   \[
   \bigl(B_q(J(c_i),J(c_j))-B_s(c_i,c_j)\bigr)_{i,j}\succeq0            \tag{2.2}
   \]
   for every pair `c_1,c_2`;
3. a quadratic Kunneth law strong enough to identify the mixed coefficient
   of `q(aJ(c)+bJ(d))` with, or dominate it over, the polarization of `s`.

The proof uses only the two images `J(c),J(d)`. Thus calling the construction
"non-additive" does not evade the inertia obstruction once linear
combinations of two images retain the source quadratic form.

## 3. The effectivity-only branch

The one-ray collapse of `a_13` avoids G3-POL, but it maps every class with
positive square to the same positive ray and identifies `c` with `-c`.
It therefore cannot satisfy an effectivity dictionary whenever the target
positive class is effective and the source distinguishes the two signs.

The remaining clean structured gate is:

> **G3-EFF.** Construct a source-defined, positively homogeneous map
> `J:D^o->Pic_hat(X)_R` with pointwise
> `q(J(c))>=s(c,c)`, together with a strict/basepoint section predicate such
> that source effectivity is equivalent to target effectivity for both `c`
> and `-c`, but without imposing G3-POL.

If the target satisfies the arithmetic-surface property

\[
 q(L)>0\quad\Longrightarrow\quad L\text{ or }-L\text{ is strictly effective},
                                                                            \tag{E}
\]

then G3-EFF plus the source assertion that neither sign of a nonzero class in
`D^o` is effective forces `s(c,c)<=0`: otherwise pointwise domination and
(E) make one target sign effective. This is exactly the desired Weil
positivity conclusion. It is a valid route, but the burden is now entirely
the effectivity dictionary; neither `a_13` nor the imported theta invariant
constructs it.

Unlike G3-POL, G3-EFF is not proved equivalent to RH here: its target/source
effectivity biconditional contains additional geometric content and remains
an open construction. It is the only structured non-additive G-3 branch not
already eliminated as vacuous or RH-equivalent by inertia.

**Later closure (`a_60`).** For the a4-weak target, property (E) makes G3-EFF
equivalent to RH as well. The forward direction uses the absence of effective
classes in `D^o`; the converse is the explicit spatial-ray map.

## 4. Updated G-3 trichotomy

| requested structure | status |
|---|---|
| pointwise domination + positive homogeneity | vacuous (`a_13`) |
| additive domination | RH-equivalent (`a_13`) |
| non-additive two-point polarization/Kunneth domination | RH-equivalent (`a_59`) |
| pointwise domination + exact effectivity/section dictionary | RH-EQUIVALENT by `a_60` |

## 5. Verification scope

`114_a_59_g3_two_point_polarization_verify.py` checks the two-by-two Gram
argument symbolically, tests random Lorentzian Gram matrices for the one-
positive-direction bound, verifies that PSD Gram domination creates a
positive plane, and exhibits the sign loss of the one-ray collapse. It does
not assert the open G3-EFF dictionary.
