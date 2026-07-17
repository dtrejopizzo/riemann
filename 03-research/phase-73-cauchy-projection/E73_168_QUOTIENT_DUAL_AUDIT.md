# E73.168 - Quotient dual audit

Date: 2026-07-14.

## 1. Purpose

E73.167 identifies the canonical cauchy0 obstruction as a quotient:

```text
Q_L = C_L / (C_L cap M_L),
dim Q_L = 3
```

in the trusted finite windows.  The remaining scalar is:

```text
<P_{Q,L}Pi_A, G_K>.
```

E73.168 tests whether the quotient projection also makes the dual cancelled
Cauchy vector `G_K` small.  If yes, the bound would become easier.  If no,
the quotient is a dimensional reduction only.

## 2. Objects

Let:

```text
C_L      = five-dimensional cauchy0 critical atom space,
M_L      = principal coefficient image of the rational local action,
P_{Q,L}  = orthogonal projector onto C_L/(C_L cap M_L),
G_K(gamma)
         = <xi_L, DD_L(-gamma,d)>.
```

The scalar endpoint can be written:

```text
<P_{Q,L}Pi_A, G_K>
= <Pi_A, P_{Q,L}G_K>
```

because `P_{Q,L}` is Hermitian in the coefficient metric used by E73.165.

## 3. Result

In trusted rows, `imageRel <= 1e-3`, the quotient does not make the dual
vector small:

```text
||P_{Q,L}G_K||/||G_K|| = 0.85--1.00.
```

The row scalar ratios

```text
|<P_Q Pi_A,G_K>| / |<Pi_A,G_K>|
```

are usually order one and can be larger due to cancellation in the
unprojected scalar.

Thus `P_Q` does not supply a dual smallness theorem.

## 4. Meaning

The rank-three quotient remains valuable:

```text
it removes two generated cauchy0 directions from the source side.
```

But the cancelled Cauchy vector is essentially supported on the quotient.
Therefore the remaining theorem is genuinely a three-dimensional scalar
divisibility statement, not a consequence of dual orthogonality.

## 5. Updated endpoint

The current exact finite target is:

```text
QUOT-PAIR:
For every natural-height off-line Hermite cluster A,

e^(alpha L)
| <P_{Q,L}Pi_A, P_{Q,L}G_K> |
<= L^B.
```

Since `P_{Q,L}G_K` is not small by itself, a proof must exploit the pair:

```text
(P_{Q,L}Pi_A, P_{Q,L}G_K),
```

not either factor separately.

## 6. Status

```text
kept:      quotient reduction to dimension 3;
rejected:  dual smallness of P_Q G_K;
remaining: prove the three-dimensional quotient pairing bound.
```

