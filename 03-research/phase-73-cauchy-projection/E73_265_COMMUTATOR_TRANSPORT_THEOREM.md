# E73.265 - Commutator transport form of the paired theorem

Date: 2026-07-14.

## 1. Purpose

E73.264 shows that the remaining `UNIF-ETA` cancellation is not row-level:

```text
rho^A ~= rho^P
```

fails in norm.  The cancellation appears only after pairing with the actual
Gamma-prime eigenline `xi_L`.

This note derives the exact transport identity explaining where that pairing
lives.

## 2. Setup

Let

```text
H_L=H_L^A-H_L^P,
H_Lxi_L=mu_Lxi_L,
Q=Q_w,
P=Q^*(QQ^*)^(-1)Q,
R=I-P,
q=q_a.
```

Since `q` is a row of `Q`,

```text
qR=0.                                             (1)
```

The center is

```text
C_{a,w}=qH_LRxi_L.                               (2)
```

## 3. Left-projected eigenline matching

Apply the eigenline equation to the left row `qR`:

```text
qRH_L^Axi_L-qRH_L^Pxi_L
=qRH_Lxi_L
=mu_LqRxi_L
=0.                                             (3)
```

Thus the left-projected archimedean and prime pairings match exactly:

```text
qRH_L^Axi_L=qRH_L^Pxi_L.                         (4)
```

This is not the desired center, because the center has `R` on the right:

```text
qH_L^ARxi_L-qH_L^PRxi_L.
```

The gap between left and right placement is a commutator.

## 4. Commutator transport

For `X=A,P`, define

```text
T_X(a,w;L)
=qH_L^X Rxi_L-qR H_L^X xi_L
=q[H_L^X,R]xi_L.                                (5)
```

Subtract (3) from (2).  Then

```text
C_{a,w}
=T_A(a,w;L)-T_P(a,w;L).                         (6)
```

Therefore `UNIF-ETA` is equivalent to the commutator transport matching:

```text
T_A(a,w;L)-T_P(a,w;L)=O_M(L^-M).                 (CTM)
```

This is the precise eigenline-paired theorem left by E73.264.

## 5. Why this avoids the circular branch

The circular E73.240 branch uses

```text
QH_Leta_w=(mu I-A(w))Qxi_L
```

and then needs `Qxi_L` to be small.

The commutator transport identity does not use `Qxi_L` as a small input.  It
uses only:

```text
1. qR=0;
2. H_Lxi_L=mu_Lxi_L;
3. the fixed projector R=I-P_w;
4. the split H_L=H_L^A-H_L^P.
```

The required estimate is not smallness of `Qxi_L`, nor a row norm estimate.
It is the rapid matching of two explicit commutator transport defects.

## 6. Numerical audit

The companion script reports:

```text
rightAB = log_L |qH_L^ARxi_L|;
rightPB = log_L |qH_L^PRxi_L|;
leftAB  = log_L |qR H_L^Axi_L|;
leftPB  = log_L |qR H_L^Pxi_L|;
leftMatchB = log_L |qR(H_L^A-H_L^P)xi_L|;
commAB  = log_L |T_A|;
commPB  = log_L |T_P|.
```

The observed pattern is:

```text
leftMatchB is at numerical zero, as forced by the eigenline equation;
leftAB and leftPB are already tiny and match;
commAB and commPB have the ordinary size of the right-projected terms;
the final center is the tiny difference commAB-commPB.
```

Thus the analytic frontier is not left-projected matching, which is exact, but
right-left transport matching:

```text
q[H_L^A,R]xi_L ~= q[H_L^P,R]xi_L.
```

## 7. The theorem to prove

```text
Commutator Transport Matching Theorem.
For every M there exist A_M,L_M such that, for all L>=L_M and all admissible
Cauchy rows/windows,

|q_a[H_L^A,R_w]xi_L - q_a[H_L^P,R_w]xi_L|
<= A_M L^-M.
```

Together with E73.262--E73.264 this proves `UNIF-ETA`, hence the scalar WRL
gate of the current route.

## 8. Status

```text
proved: left-projected arch/prime matching is exact by the eigenline equation;
proved: UNIF-ETA center equals arch-prime commutator transport defect;
rejected: row-level Schur convergence and generic transport norms;
open: prove Commutator Transport Matching from the explicit Gamma-prime cell formula.
```

