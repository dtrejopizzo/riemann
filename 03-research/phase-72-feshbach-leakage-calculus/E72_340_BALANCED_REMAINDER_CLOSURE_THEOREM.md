# E72.340 -- Balanced remainder closure theorem

**Purpose.** Fuse E72.334 and E72.339 into the exact analytic endpoint.  The remaining contour
estimate is neither a matrix estimate nor a standalone prime estimate.  It is the polynomial boundedness
of one balanced explicit-formula remainder attached to the transformed Feshbach packet.

## 1. The finite packet functional

For the actual finite packet `B_z^M`, set

```text
F_z^M(w):=int_{-L}^L e^(wt)B_z^M(|t|)dt
        = M_z^M(w)+M_z^M(-w).
```

E72.339 proves that this is exactly the paired `POSC` kernel:

```text
F_z^M(w)
=(1/w)int_0^L (e^(-wy)-e^(wy))(B_z^M)'(y)dy.          (1)
```

Let `W_T` be a fixed finite zero-pair window.  Define the balanced explicit-formula remainder

```text
BER_T^M(z)
:= Arch_L(B_z^M)
 - sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n)
 - sum_{w in W_T/+-} F_z^M(w).                        (2)
```

The archimedean term uses the same finite-part convention as E72.319--E72.330.

## 2. Exact equivalence with UREM-POLY

By the completed explicit formula for the compactly supported even packet,

```text
Arch_L(B_z^M)
 - sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n)
= sum_{w in Div(Z)/+-} F_z^M(w).                      (3)
```

Subtracting the finite window gives

```text
BER_T^M(z)
= sum_{w notin W_T/+-} F_z^M(w)
= Rem_T^M(z).                                        (4)
```

Thus

```text
BER-POLY:
sup_{z in K}|BER_T^M(z)| <= C_{K,T}L^B
```

is exactly `UREM-POLY`.

This matters because (2) is a finite arithmetico-archimedean expression, while (4) is a zero-tail
expression.  The equality lets the proof choose the side where cancellation is visible.

## 3. The Feshbach equation cancels the full balanced functional

The transformed finite eigenvector equation gives, with the endpoint-normalized coefficient
`Lambda_L` of E72.330,

```text
Lambda_L G_x(z)
= sum_{w in Div(Z)/+-} F_z^M(w).                      (5)
```

Combining (3) and (5),

```text
Arch_L(B_z^M)
 - sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n)
= Lambda_L G_x(z).                                   (6)
```

Therefore the finite window remainder has the completely finite form

```text
Rem_T^M(z)
= Lambda_L G_x(z) - sum_{w in W_T/+-} F_z^M(w).       (7)
```

Equation (7) is the analytic closure identity for the transformed route.  It is not an estimate.  It
is the exact cancellation law that replaces all earlier incoherent tails.

## 4. Consequence: the only missing estimate is nodal finite-window control

From (7), `UREM-POLY` follows if and only if

```text
Lambda_L G_x(z) - sum_{w in W_T/+-} F_z^M(w)
```

is polynomially bounded on the compact shifted strip `K`.

E72.324--E72.327 prove that, once this expression is polynomial for a window containing the relevant
off-line cluster, the maximal-real-part Cauchy block forces the off-line nodal values of `G_x` to be
exponentially suppressed.  Hence the transformed route can now be stated without any derivative or
absolute prime bound:

```text
BFW:
the finite-window balanced Feshbach-Weil expression (7) is polynomially bounded.

BFW => UREM-POLY => PW-Cauchy => compact-root HPAC decay.
```

## 5. Non-circular proof target

The identity (7) by itself does not prove `BFW`, because it contains `G_x`.  The non-circular target is
to prove (7) polynomially by applying the finite Feshbach equation before evaluation at the zero nodes:

```text
(mu+e_pole)G_x(z)
= T_W02(z)[xi]-T_WR(z)[xi]-T_Prime(z)[xi],
```

with the three terms kept coupled.  In the balanced language this becomes:

```text
BFW-coupled:
the difference between the full transformed Feshbach functional and its W_T interpolation projection
is polynomial in fixed shifted strips.
```

No estimate of

```text
sum Lambda(n)n^(-1/2)B_z^M(log n)
```

alone is admissible; that would return to the incoherent ceiling.

## 6. Status

```text
proved: BER-POLY is exactly UREM-POLY;
proved: the full balanced explicit-formula functional equals Lambda_L G_x(z);
proved: the finite remainder has the closed form (7);
reduced: the remaining analytic theorem to BFW-coupled, a finite-window interpolation remainder for
         the coupled transformed Feshbach operator.
```
