# E72.321 -- Symmetric zero-pair reduction of the packet equation

**Purpose.** Use the even symmetry of the completed zeta divisor and the pole-even symmetry of the
finite Cauchy transform to simplify the scalar packet equation of E72.320.

The important cancellation: the zero-sum term proportional to `G_x(z)` cancels exactly in symmetric
zero pairs.

## 1. Symmetries

Let

```text
Z(w):=xi(1/2+w).
```

The functional equation gives

```text
Z(w)=Z(-w),
```

so the shifted nontrivial-zero divisor is symmetric:

```text
w in Div(Z)  <=>  -w in Div(Z).
```

The pole-even Cauchy transform is odd:

```text
C_x(-u)=-C_x(u).
```

Since

```text
G_x(w)=(1-e^(wL))C_x(iw),
```

we have

```text
G_x(-w)
=(1-e^(-wL))C_x(-iw)
=-(1-e^(-wL))C_x(iw)
=e^(-wL)G_x(w).                                      (1)
```

## 2. Cancellation of the `G_x(z)` zero sum

E72.320 gives

```text
M_z(w)
= [ ((w+z)+e^(zL)(w-z))G_x(w) - 2wG_x(z) ]
   /(w^2-z^2).
```

The part proportional to `G_x(z)` is

```text
-2wG_x(z)/(w^2-z^2).
```

Under `w -> -w`, this becomes

```text
+2wG_x(z)/(w^2-z^2).
```

Hence for every symmetric pair `{w,-w}`,

```text
-2wG_x(z)/(w^2-z^2)
+2wG_x(z)/(w^2-z^2)
=0.                                                     (2)
```

So the zero-sum does not renormalize the left coefficient after symmetric pairing.

## 3. Paired coefficient for the off-point values

Let

```text
E_z:=e^(zL),       E_w:=e^(wL).
```

The pair contribution of the `G_x(w)` terms is

```text
Pair_z(w)
:= [((w+z)+E_z(w-z))G_x(w)
    +((-w+z)+E_z(-w-z))G_x(-w)]/(w^2-z^2).
```

Using (1),

```text
Pair_z(w)
= G_x(w)/(w^2-z^2)
   [ w(1+E_z)(1-E_w^(-1))
     + z(1-E_z)(1+E_w^(-1)) ].                         (3)
```

Thus the complete-mesh packet equation becomes

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_{w in Div(Z)/+-} Pair_z(w)
   - Lcal(B_z^tail),                                   (4)
```

with the usual symmetric limiting convention.

## 4. Why this matters

E72.320 left a possible coefficient

```text
sum_w 2w/(w^2-z^2)
```

on the left side. E72.321 proves that this term is identically zero after using the natural symmetric
divisor convention. This is not an estimate and does not use RH.

The remaining pressure is only the interpolation of `G_x(w)` at one representative of each pair.

## 5. The new target

The packet-zero bound is now:

```text
PAIR-Z:
|sum_{w in Div(Z)/+-} Pair_z(w)| <= C L^B(1+|z|)^B
```

in fixed shifted strips, together with the finite tail bound

```text
|Lcal(B_z^tail)| <= C L^B(1+|z|)^B.
```

Then `PW-Cauchy` follows from (4) and the pole-even gap.

## 6. Status

```text
proved: G_x(-w)=e^(-wL)G_x(w);
proved: the G_x(z)-coefficient zero sum cancels exactly by pairs;
reduced: packet-zero control to PAIR-Z plus finite tail.
```

The next step is to rewrite `Pair_z(w)` in terms of the un-cancelled Cauchy value `C_x(iw)` and look
for exponential cancellation inside the bracket.
