# E73.266 - Rank-two transport collapse audit

Date: 2026-07-14.

## 1. Purpose

E73.265 identifies the remaining center as a commutator transport matching:

```text
C_{a,w}=q_a[H_L^A,R_w]xi_L-q_a[H_L^P,R_w]xi_L.
```

The next tempting move is to expand `R_w=I-Q_w^*(Q_wQ_w^*)^(-1)Q_w`.
This note records what happens: the expansion is exact, but it collapses back
to the circular two-dimensional Cauchy-plane branch of E73.240.

## 2. Exact rank-two identity

Let

```text
G=(QQ^*)^(-1),
P=Q^*GQ,
R=I-P,
h=Qxi_L,
B=QH_LQ^*G.
```

Since `H_Lxi_L=mu_Lxi_L`,

```text
QH_Lxi_L=mu_LQxi_L=mu_Lh.
```

Therefore

```text
QH_LRxi_L
=QH_Lxi_L-QH_LQ^*GQxi_L
=(mu_LI-B)h.                                     (1)
```

For a row `q_a`, this is:

```text
q_aH_LRxi_L = [(mu_LI-B)h]_a.                    (2)
```

This is exactly the E73.240 branch.

## 3. Archimedean-prime split

Writing `H_L=H_L^A-H_L^P` gives:

```text
q_aH_L^XRxi_L
=q_aH_L^Xxi_L-q_aH_L^XQ^*G h,     X=A,P.        (3)
```

Subtracting the two identities recovers (1).  No new cancellation is created;
all smallness is now hidden in `h=Qxi_L`.

## 4. Why this is rejected as a proof route

Equation (1) is useful as a consistency check, but it cannot prove
`UNIF-ETA` non-circularly.  The scalar WRL route uses `UNIF-ETA` precisely to
control the Cauchy divisor data.  Bounding `(mu I-B)h` through prior smallness
of `h=Qxi_L` repeats the already rejected E73.240 mechanism.

Thus:

```text
commutator transport matching      admissible target;
rank-two Cauchy-plane expansion    detector only, not forcer.
```

## 5. Status

```text
proved: qH_LRxi_L=(mu_LI-QH_LQ^*G)Qxi_L;
proved: arch/prime rank-two expansions match direct Schur terms;
rejected: rank-two transport as non-circular proof source.
```

