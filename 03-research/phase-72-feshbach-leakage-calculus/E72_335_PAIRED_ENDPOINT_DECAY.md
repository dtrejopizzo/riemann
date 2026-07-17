# E72.335 -- Paired endpoint decay for the finite packet remainder

**Purpose.** Identify the first decay mechanism behind `UREM-POLY`. The finite packet has one nonzero
endpoint, but the `w ~ -w` pairing cancels the leading `1/w` endpoint term. The outside contour
therefore starts at order `1/w^2`.

## 1. Endpoint values of the finite packet

For the actual finite transformed packet

```text
B_z^M(y)=sum_n xi_n KQ_z^M(y;n),
```

the cell endpoints satisfy

```text
Q_0(m,n)=2delta_mn,
Q_L(m,n)=0.
```

Therefore

```text
B_z^M(0)=2G_x(z),
B_z^M(L)=0.                                           (1)
```

This is true before the complete/tail split.

## 2. Large-w expansion

Let

```text
M_z^M(w)=int_0^L e^(wy)B_z^M(y)dy.
```

For `w` on a vertical zero-avoiding contour, integration by parts gives

```text
M_z^M(w)
= [e^(wL)B_z^M(L)-B_z^M(0)]/w
   - (1/w)int_0^L e^(wy)(B_z^M)'(y)dy.
```

Using (1),

```text
M_z^M(w)
= -2G_x(z)/w
   - (1/w)int_0^L e^(wy)(B_z^M)'(y)dy.                (2)
```

Similarly,

```text
M_z^M(-w)
= 2G_x(z)/w
   + (1/w)int_0^L e^(-wy)(B_z^M)'(y)dy.               (3)
```

Adding (2)--(3), the endpoint term cancels:

```text
Pair_z^M(w)
= M_z^M(w)+M_z^M(-w)
= (1/w)int_0^L [e^(-wy)-e^(wy)](B_z^M)'(y)dy.         (4)
```

Thus the paired kernel has no `1/w` endpoint term.

## 3. Second integration by parts

If `(B_z^M)'` has controlled endpoint values, integrate by parts again:

```text
Pair_z^M(w)
= O( ( |(B_z^M)'(0)|+|(B_z^M)'(L)| )/|w|^2 )
   + O( |w|^(-2) int_0^L |(B_z^M)''(y)|dy )
```

on vertical contours, with the usual exponential factors tracked by pairing the two sides of the
rectangle.

Therefore `UREM-POLY` follows from the proof-facing packet smoothness estimate:

```text
PACK-SMOOTH:
|(B_z^M)'(0)|+|(B_z^M)'(L)| + int_0^L |(B_z^M)''(y)|dy <= C_K L^B.
```

Then

```text
|Pair_z^M(w)| <= C_K L^B/|w|^2.
```

Since `Z'(w)/Z(w)=O(log |w|)` on zero-avoiding contours, the outside contour integral is polynomial.

## 4. Meaning

The earlier E72.332 obstruction came from treating the paired kernel as if it had a raw `G(w)/w`
tail. E72.335 shows that the actual finite packet pairing cancels the leading endpoint term. The
remaining gate is no longer zero-divisor strength; it is a finite packet smoothness estimate.

## 5. Status

```text
proved: paired finite packet cancels the 1/w endpoint tail;
reduced: UREM-POLY to PACK-SMOOTH, a finite y-regularity estimate for B_z^M;
refined: E72.336 collapses the endpoint derivative part of PACK-SMOOTH to a rank-one scalar identity.
```

The next step is to prove `PACK-SMOOTH` from the explicit finite Fourier formula for `Q_y`.
