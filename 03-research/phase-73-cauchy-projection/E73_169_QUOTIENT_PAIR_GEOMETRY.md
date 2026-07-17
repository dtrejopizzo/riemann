# E73.169 - Quotient pair geometry

Date: 2026-07-14.

## 1. Purpose

E73.168 shows that neither quotient factor is automatically annihilated:

```text
<P_Q Pi_A, P_Q G_K>
```

is the remaining three-dimensional pairing.  E73.169 tests whether this
pairing is small because the natural projected source vectors `P_Q Pi_A`
avoid the projected dual vector `P_Q G_K` by a uniform angular mechanism.

## 2. Test

Choose an orthonormal basis of the quotient

```text
Q_L = C_L/(C_L cap M_L).
```

Compute:

```text
Pi_Q(A) = coordinates of P_Q Pi_A in Q_L,
G_Q     = coordinates of P_Q G_K in Q_L.
```

Measure:

```text
cos(A,L) = |<Pi_Q(A),G_Q>|/(||Pi_Q(A)|| ||G_Q||).
```

## 3. Result

In trusted rows, `imageRel <= 1e-3`, the cosines vary substantially:

```text
0.16 to 0.80.
```

There is no uniform angular avoidance visible in the tested data.

The scalar remains small because `G_Q` itself is numerically small in these
finite windows:

```text
||G_Q|| about 1e-9 to 1e-8.
```

But E73.168 already showed that this is not small relative to `G_K`; it is
small because the finite cancelled Cauchy values are small at the tested
critical ordinates.

## 4. Meaning

The quotient reduction does not reveal a hidden orthogonality between
`Pi_Q` and `G_Q`.

Therefore the proof target should not be:

```text
Pi_Q is almost orthogonal to G_Q.
```

The honest target is a weighted quotient norm/pairing estimate:

```text
e^(alpha L)||Pi_Q(A)|| ||G_Q|| <= L^B
```

or a sharper direct estimate of the pairing

```text
e^(alpha L)|<Pi_Q(A),G_Q>| <= L^B.
```

## 5. Updated finite theorem

The current finite theorem is:

```text
QUOT-NORM:
For every natural-height off-line Hermite cluster A,

e^(alpha L) ||P_Q Pi_A|| ||P_Q G_K|| <= L^B.
```

This implies `QUOT-PAIR` by Cauchy-Schwarz in the three-dimensional quotient.

If `QUOT-NORM` is too strong, the exact endpoint remains:

```text
QUOT-PAIR:
e^(alpha L)|<P_Q Pi_A,P_Q G_K>| <= L^B.
```

## 6. Status

```text
kept:      three-dimensional quotient;
rejected:  uniform angular avoidance as the closing mechanism;
remaining: prove quotient norm/pairing bounds.
```

