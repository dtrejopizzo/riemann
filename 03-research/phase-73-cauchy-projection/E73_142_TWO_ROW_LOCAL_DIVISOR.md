# E73.142 - Two-Row Local Divisor Forcing

Date: 2026-07-12.

## 1. Purpose

E73.141 stated `LOCAL-DIVISOR-FORCING` qualitatively.  This note gives the
finite algebraic theorem that makes it usable.

The exact pair divisibility is

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).       (1)
```

For a fixed critical divisor node `w`, evaluate (1) at two rows

```text
z_1=sigma+i eta_1,
z_2=sigma+i eta_2,
```

with the same `sigma>0` and `eta_1 != eta_2`.  Set

```text
M_L(w;z_1,z_2)
 =
 [ A_L(z_1,w)  B_L(z_1,w) ]
 [ A_L(z_2,w)  B_L(z_2,w) ].
```

Then

```text
M_L(w;z_1,z_2)
 [ H_0(w)  ]
 [ H_0(-w) ]
 =
 [ Pair_{z_1}^infty(w) ]
 [ Pair_{z_2}^infty(w) ].                             (2)
```

## 2. Two-row forcing theorem

**Theorem 142.1.**  Suppose that for every standard-box critical node `w`
one can choose two rows `z_1,z_2` such that

```text
||M_L(w;z_1,z_2)^(-1)|| <= C_M L^a,                  (INV_a)
```

and

```text
|Pair_{z_j}^infty(w)| <= C_P L^{-17-a},  j=1,2.       (PAIR_{17+a})
```

Then

```text
|H_0(w)|+|H_0(-w)| <= C L^-17.                        (LDIV_17)
```

*Proof.*  Taking the Euclidean norm in (2),

```text
||(H_0(w),H_0(-w))||
 <= ||M_L^(-1)|| ||(Pair_{z_1}^infty(w),Pair_{z_2}^infty(w))||.
```

The hypotheses give the right hand side

```text
<= C_M L^a * sqrt(2) C_P L^{-17-a}
 = C L^-17.
```

The `l^1` bound follows from `|x|+|y|<=sqrt(2)||(x,y)||`.  `□`

## 3. Actual finite packet

The actual packet is finite:

```text
Pair_z^M(w)=Pair_z^infty(w)-TailPair_z^M(w).
```

Thus it is enough to prove the two estimates

```text
|Pair_{z_j}^M(w)| <= C L^{-17-a},
|TailPair_{z_j}^M(w)| <= C L^{-17-a}.
```

This is the precise local form of `LOCAL-DIVISOR-FORCING`.

## 4. Non-circularity

The theorem does not assume `H_0(w)` is small.  It uses:

```text
the exact pair divisor identity,
two explicit rows,
polynomial invertibility of the 2x2 coefficient matrix,
smallness of actual paired packet values plus finite-tail correction.
```

The only way circularity can re-enter is if `PAIR_{17+a}` is proved by
substituting the already-small `H_0(w)`.  The intended proof of
`PAIR_{17+a}` must instead use the packet equation / explicit formula and
the finite signed tail calculus of E72.339--E72.341.

## 5. Numerical status

The companion probe

```text
E73_142_local_divisor_condition_probe.py
```

uses two nearby FAR rows and finds

```text
||M_L^(-1)|| = L^0.7 ... L^2.8,
cond(M_L)    = L^2.5 ... L^3.0,
```

on the tested `lambda=16..32` rows.  Thus the inverse loss is polynomial
and compatible with a target `PAIR_{20}` or stronger.

The known finite/base exception is still visible:

```text
lambda=16, gamma=25.01
```

where `LDIV_17` itself fails in the raw asymptotic row table and is handled
by the finite manifest rather than the asymptotic theorem.

## 6. Updated endpoint

The Phase 73 analytic endpoint is now:

```text
INV_3
+ PAIR_20 for two rows
+ finite tail PAIR_20
=> LDIV_17
=> CSV_17
=> Uniform GATE-73.
```

`INV_3` is an elementary coefficient-matrix estimate.  The load-bearing
new theorem is `PAIR_20` for the actual finite Feshbach packet, proved
without substituting `H_0(w)` through (1).
