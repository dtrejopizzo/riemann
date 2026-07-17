# E73.166 - Projector moment audit

Date: 2026-07-12.

## 1. Purpose

E73.165 found that the canonical cauchy0 transfer

```text
T_L: Pi_A -> delta_A
```

is numerically an orthogonal projector of rank three on the five-dimensional
critical atom space.

E73.166 asks whether the two-dimensional kernel of `T_L` is a simple moment
space.  If yes, the quotient could be written by explicit moment
constraints.  If no, the projector is still useful but must be treated as a
finite operator depending on the local CCM/Feshbach data.

## 2. Tested moment candidates

The kernel of `T_L` was compared against simple two-dimensional spans:

```text
span{1,gamma},
span{1,gamma^2},
span{1,gamma-mean(gamma)},
span{1,phase(gamma L)},
span{1,|1-exp(i gamma L)|},
span{gamma,gamma^2},
span{1,1/gamma},
span{1,alternating}.
```

The diagnostic residual is:

```text
dist(Ker(T_L), candidate space).
```

## 3. Result

No simple candidate matches well.  The best residuals are usually:

```text
0.35 to 0.70.
```

The closest candidate alternates between `span{1,1/gamma}` and
`span{1,phase(gamma L)}`, but neither is close enough to be structural.

The subspace itself also changes noticeably with `L`:

```text
dist(Ker(T_L), previous Ker(T_L))   about 0.45--0.70,
dist(Range(T_L), previous Range)    about 0.36--0.58.
```

Thus the rank-three projector is not a fixed moment projector in the tested
coordinates.

## 4. Meaning

The rank-three phenomenon from E73.165 survives:

```text
T_L is essentially a finite orthogonal projector.
```

But its range/kernel are not described by elementary critical-height
moments.  Therefore the next finite theorem should not claim:

```text
delta_A is obtained by imposing two simple moment cancellations.
```

The honest object is:

```text
P_{bad,L} = the rank-three projector obtained from the canonical
coefficient action of (H_L-mu_L I).
```

This projector is finite and explicit, but apparently operator-dependent.

## 5. Updated endpoint

The sharp current statement remains:

```text
CANON-PROJ-CRIT-DIV:
e^(alpha L)
| < P_{bad,L}Pi_A, G_K > |
<= L^B,
```

where

```text
G_K(gamma)
=(1-exp(i gamma L))sum_n xi_L(n)/(-gamma-d_n).
```

The new information is:

```text
P_{bad,L} is rank three, but not an elementary moment projector.
```

## 6. Status

```text
kept:      rank-three quotient reduction;
rejected:  simple moment description of the two eliminated directions;
open:      derive P_{bad,L} symbolically from the finite coefficient action,
           or prove the scalar bound directly on its range.
```

