# 114.a.97 — H7: positive scalar rigidification kills the required even moves

```
+-------------------------------------------------------------------------+
| WEIGHTS     In part i, bit 0 has weight a_i and bit 1 weight b_i.        |
| RATIOS      r_i=b_i/a_i in a characteristic-zero field.                  |
| EVEN MOVES  000~011, 000~101, 000~110 force                             |
|             r_2 r_3=r_1 r_3=r_1 r_2=1.                                 |
| SOLUTION    r_1=r_2=r_3 and r_i^2=1.                                    |
| POSITIVE    Positive real weights force every r_i=1.                     |
| CONFLICT    Any scalar-visible positive rigidification forbids at least   |
|             one even move needed by a94.                                 |
| OPEN        A scalar-invisible but intrinsically rigid decoration.        |
+-------------------------------------------------------------------------+
```

## 1. Multiplicative evaluation of decorated triples

Let the two decorations in part `i` have nonzero values `a_i,b_i` under a
homomorphism to a characteristic-zero field.  A triple `epsilon` in the
product context has value

\[
 W(\varepsilon)=\prod_{i=1}^3
   a_i^{1-\varepsilon_i}b_i^{\varepsilon_i}.                         \tag{1.1}
\]

This is the scalar shadow of inserting the three decorations into independent
context factors; composition/direct product multiplies their unary values.
Put `r_i=b_i/a_i`.

### Theorem 1.1 (even-move rigidity equation)

If all three even replacements required in `a94` are equivalences,

\[
 000\sim011,\qquad000\sim101,\qquad000\sim110,                       \tag{1.2}
\]

then

\[
 r_2r_3=r_1r_3=r_1r_2=1.                                           \tag{1.3}
\]

Consequently `r_1=r_2=r_3=r` and `r^2=1`.

### Proof

Apply the homomorphism to (1.2) and divide by the nonzero base weight
`a_1a_2a_3`.  This gives (1.3).  Dividing the first two equations gives
`r_2=r_1`; the other pairs give equality of all ratios.  Substitution gives
`r^2=1`.  QED.

### Corollary 1.2 (positive no-go)

If the weights are positive real numbers, every ratio is `r=1`.  Thus each
part's two decorations have the same scalar value.  In particular no family
of positive scalar evaluations can both distinguish a bit decoration and
preserve all three even moves.

## 2. Application to the a96 decorations

At `u=2`, the decorations of `a96` have

\[
 a=D_0(1,1,1)=3,\qquad b=D_1(1,1,1)=5.                              \tag{2.1}
\]

Hence

\[
 W(000)=3^3=27,qquad W(011)=3\cdot5^2=75.                           \tag{2.2}
\]

The real bio is a quotient invariant, so `P_000` and `P_011` cannot be
connected by a Haran equivalence path.  The same applies cyclically.  The
specific rigidification of `a96` therefore cannot realize H7-RIGID-EVEN-MOVES.

This is not a defect in the decorations; it exposes the structural tension:
the parity Smith class needs three pairwise bit changes to be invisible,
while a positive scalar rigidification makes at least one visible.

## 3. What parity variant remains possible

Over a general characteristic-zero field, Theorem 1.1 also permits the
common ratio `r=-1`.  Such a sign decoration is unlikely to rigidify the
tree against Haran's built-in `+/-1` action and cancellation, and no claim is
made that it works.

The only other possibility is

> **H7-SCALAR-INVISIBLE-RIGID.** Construct two intrinsically nonisomorphic
> same-fold blocks which have identical values under every multiplicative
> scalar evaluation used in (1.1), yet remain distinguishable by a genuinely
> higher-arity/bilateral invariant; then recheck even and odd macro closure.

This is substantially stronger than H7-PARITY-RIGID-TYPE.  The positive
read-once decorations of `a96` do not satisfy it.  Until such blocks exist,
the rigidified parity route does not produce endpoints.

The positive rigidified parity candidate is closed negatively.
H7-SCALAR-INVISIBLE-RIGID, H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_97_h7_positive_rigid_no_go_verify.py` checks the ratio equations over
exact rationals, exhausts bounded nonzero integer weights, verifies the
`27` versus `75` witness, and enforces the remaining-gate scope.
