# E72.334 -- Unified finite remainder contour

**Purpose.** Merge the two remaining transformed tails, `TAIL-SPEC` and `OUT-CONTOUR`, into one finite
remainder statement. The split into a complete-mesh outside-zero tail and a finite-mesh Fourier tail is
bookkeeping; the actual finite CCM equation only has one remainder after a zero window is chosen.

## 1. Complete and finite packet kernels

Let

```text
B_z^M(y)=B_z^infty(y)-B_z^tail(y)
```

be the actual finite transformed packet. For a shifted spectral variable `w`, define

```text
M_z^M(w):=int_0^L e^(wy)B_z^M(y)dy,
M_z^infty(w):=int_0^L e^(wy)B_z^infty(y)dy,
M_z^tail(w):=int_0^L e^(wy)B_z^tail(y)dy.
```

Thus

```text
M_z^M(w)=M_z^infty(w)-M_z^tail(w).                    (1)
```

E72.320 gives `M_z^infty` explicitly. E72.333 gives `M_z^tail` explicitly as a finite Fourier
coefficient sum.

## 2. Exact finite transformed equation

E72.319 gives, with endpoint normalization absorbed into the left coefficient,

```text
Lambda_L G_x(z)
= sum_{w in Div(Z)} M_z^M(w),                         (2)
```

where the zero sum is taken symmetrically and

```text
Lambda_L=mu+e_pole-2kappa_*.
```

After pairing `w ~ -w`, write

```text
Pair_z^M(w):=M_z^M(w)+M_z^M(-w).
```

Then

```text
Lambda_L G_x(z)
= sum_{w in Div(Z)/+-} Pair_z^M(w).                   (3)
```

This is the actual finite equation. No separate `TAIL` or `OUT` term appears until a zero window is
chosen.

## 3. Window remainder

Let `W_T` be a finite set of zero-pair representatives in a fixed height window. Split (3):

```text
Lambda_L G_x(z)
= sum_{w in W_T} Pair_z^M(w)
   + Rem_T^M(z),                                      (4)
```

where

```text
Rem_T^M(z):=sum_{w notin W_T} Pair_z^M(w).             (5)
```

This is the only remainder needed for the zero-node system.

The earlier split is recovered by inserting (1):

```text
Rem_T^M
= sum_{w notin W_T} Pair_z^infty(w)
 - sum_{w in Div(Z)/+-} Pair_z^tail(w)
 + sum_{w in W_T} Pair_z^tail(w).
```

Thus `OUT-CONTOUR` and `TAIL-SPEC` are two pieces of the same finite remainder.

## 4. Unified gate

The transformed theorem can now use one gate:

```text
UREM-POLY:
sup_{z in K}|Rem_T^M(z)| <= C_{K,T}L^B.                (6)
```

Once `UREM-POLY` holds, the Cauchy-block induction of E72.324--E72.326 proceeds with the finite kernel
`Pair^M`, not with the artificial complete-plus-tail split.

## 5. Contour form

Let

```text
P_z^M(w):=M_z^M(w)+M_z^M(-w)
```

as a meromorphic function of `w` with removable values at finite nodes. Then

```text
Rem_T^M(z)
= (1/2pi i) int_{Gamma_T} P_z^M(w) Z'(w)/Z(w)dw,       (7)
```

where `Gamma_T` is a zero-avoiding contour enclosing the outside of the finite window in the standard
symmetric limiting sense.

Therefore `UREM-POLY` is the single contour estimate:

```text
|int_{Gamma_T} P_z^M(w) Z'(w)/Z(w)dw| <= C_{K,T}L^B.   (8)
```

## 6. Advantage

This avoids proving a pointwise Fourier-tail estimate and an outside-zero estimate separately. The
finite packet may have cancellations between:

```text
complete outside-zero contribution,
finite mesh tail,
inside-window tail correction.
```

Those cancellations are invisible in the split formulation but present in the actual finite equation.

## 7. Status

```text
proved: TAIL-SPEC and OUT-CONTOUR combine into the exact finite remainder Rem_T^M;
reduced: the two transformed tail gates to one contour estimate UREM-POLY;
reduced further: E72.335 shows UREM-POLY follows from PACK-SMOOTH for the finite packet;
corrected: E72.338 shows absolute PACK-SMOOTH is too strong in right shifted strips;
open:   prove the paired oscillatory smoothness gate POSC.
```

This is the cleanest current endpoint for the transformed route.
