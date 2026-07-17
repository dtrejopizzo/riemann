# E72.332 -- Outside-window zero tail reduction

**Purpose.** Reformulate `OUT-POLY`, the second remaining transformed gate, as a contour tail estimate
for a paired logarithmic-derivative kernel. This separates standard zero-counting from the remaining
decay requirement.

## 1. Outside tail

For fixed compact shifted `z` and zero representatives modulo `w ~ -w`, E72.321 gives the paired
coefficient

```text
Pair_z(w)
= G_x(w)/(w^2-z^2)
   [ w(1+e^(zL))(1-e^(-wL))
     + z(1-e^(zL))(1+e^(-wL)) ].
```

The outside-window contribution is

```text
OUT_T(z):=sum_{|Im w|>T} Pair_z(w),
```

with the symmetric limiting convention.

## 2. Why absolute zero-counting is not enough

For large `|w|`,

```text
Pair_z(w)
~ G_x(w)(1+e^(zL))(1-e^(-wL))/w.
```

A raw zero-counting estimate gives

```text
sum_{|Im w|>T} 1/|w|
```

which is not absolutely convergent over zeta zeros. Therefore `OUT-POLY` cannot be proved by absolute
values of the paired kernel alone.

The tail must be interpreted as a symmetric contour sum:

```text
sum_w Pair_z(w)
= (1/2pi i) int Pair_z(w) Z'(w)/Z(w) dw,
Z(w)=xi(1/2+w),
```

with the same pairing that already cancelled the `G_x(z)` coefficient.

## 3. Correct contour target

Define the meromorphic kernel

```text
P_z(w)
:= G_x(w)/(w^2-z^2)
   [ w(1+e^(zL))(1-e^(-wL))
     + z(1-e^(zL))(1+e^(-wL)) ].
```

Then

```text
OUT-POLY
```

is the statement that, for rectangles `R_T` exhausting the shifted plane outside the finite zero
window,

```text
| (1/2pi i) int_{partial R_T,outside} P_z(w) Z'(w)/Z(w) dw |
<= C_K L^B.                                             (1)
```

The kernel poles at `w=+-z` are avoided or interpreted by the removable values already used in
E72.322.

## 4. Sufficient decay condition

The standard bound

```text
Z'(w)/Z(w)=O(log |w|)
```

on zero-avoiding contours is enough if the cancelled Cauchy transform satisfies, on the outside
contours,

```text
G_x(w)(1-e^(-wL)) = O_K(L^B |w|^(-1-epsilon)).
```

More generally, one needs the symmetric contour integral of `P_z(w)` to be polynomial; this may follow
from one integration by parts in the Cauchy numerator or from a high-frequency version of
`PW-Cauchy`.

## 5. Reduced gate

Thus `OUT-POLY` is equivalent to the following proof-facing statement:

```text
OUT-CONTOUR:
the paired kernel P_z(w) has polynomial logarithmic-derivative contour tail against Z'/Z.
```

This is not a new positivity statement. It is a standard contour-tail estimate once high-|w| decay of
the finite cancelled Cauchy transform is known.

## 6. Status

```text
proved: absolute zero-counting is insufficient for OUT-POLY;
reduced: OUT-POLY to the explicit contour estimate OUT-CONTOUR;
open:   prove high-|w| decay of the paired cancelled Cauchy kernel on zero-avoiding contours.
```

Together with E72.331, the two remaining transformed gates are now both exact signed/contour
statements, not informal tail bounds.
