# E74.6 - Branch no-go and return to the cell target

Date: 2026-07-16.

## Purpose

E74.5 reduced the harmonic-symbol scalar to

```text
QH_L(I-P_w)xi_L=(mu_LI-QH_LQ^*(QQ^*)^{-1})Qxi_L.       (1)
```

This note audits (1) against the previous program and records the allowed next
target.

## Audit against Phase 73

The identity (1) is not new.  It is exactly the transverse eigen-branch of
E73.188 and the rank-two transport branch rejected by E73.240, E73.266, and
E73.296 as a proof mechanism.

The issue is not algebraic correctness.  The identity is exact.  The issue is
load-bearing direction:

```text
T_w := QH_L(I-P_w)xi_L
     = B_w h_w,

B_w = mu_LI-QH_LQ^*(QQ^*)^{-1},
h_w = Qxi_L.
```

Using smallness of `h_w` to prove smallness of `T_w` is circular, because
smallness of the off-line Cauchy data is precisely what NAT-PROJ/PW-Cauchy is
meant to prove.

E73.296 also tested the only possible escape:

```text
maybe B_w itself is small or structurally singular.
```

It is not.  In the natural windows `||B_w||` and `s_min(B_w)` are often
positive powers of `L`.  Therefore the branch is a detector, not a forcer.

## What E74 contributed anyway

E74.2-E74.4 are still useful because they give exact coordinates for the same
row:

```text
qH_L
= qM_U + qM_W(A+M_{H_beta}),

H_beta(n)= -i/(2 pi) sum_{m != n}[1/(m-n)-1/(m-beta)].
```

So the Hilbert/harmonic language did not close the theorem, but it did expose
the final row in a finite mesh form that is equivalent to the CCM cell row.

## Allowed next target

By E73.294, the harmonic-symbol row is exactly the Gamma-prime functional of
the CCM cell:

```text
qH_Leta = F_L[ y -> qQ_y eta ],

Q_y(j,j)=2(1-y/L)cos(d_jy),
Q_y(j,b)=(sin(d_jy)-sin(d_by))/(pi(n_b-n_j)), j != b.
```

Therefore the non-circular theorem is:

```text
Directional Cell Eigenline Cancellation.
For eta=(I-P_w)xi_L, Q_w eta=0,

F_L[ y -> q_a Q_y eta ] = O_M(L^(-M))
```

uniformly in the admissible window.

This must be proved from the explicit cell algebra plus `Q_w eta=0`, not from
`Q_wxi_L` being small and not from a norm estimate on `Q_y`.

## Immediate analytic reformulation

For a row `q=q_a`, define

```text
B_q,eta(y)=qQ_yeta.
```

Using the cell formula, `B_q,eta(y)` is an exponential polynomial in `e^{id_n y}`
whose coefficients are explicit bilinear expressions in `q` and `eta`.

The constraint

```text
Q_w eta=0
```

means that the Cauchy transforms

```text
sum_n eta_n/(w+id_n),        sum_n eta_n/(-w+id_n)
```

vanish.  The next proof attempt must turn those two rational cancellations
into a structural divisibility of the exponential polynomial `B_q,eta(y)`,
then apply the Gamma-prime functional `F_L`.

## Status

```text
closed: E74.5 branch formula is exact;
rejected as forcer: proving through h_w=Qxi_L or small B_w;
kept: harmonic-symbol coordinates for qH_L;
next: prove Directional Cell Eigenline Cancellation from Q_w eta=0.
```
