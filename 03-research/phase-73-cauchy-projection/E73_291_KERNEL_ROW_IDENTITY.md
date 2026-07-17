# E73.291 - Kernel-row identity and commutator unification

Date: 2026-07-14.

## 1. Purpose

E73.290 introduced the explicit frequency kernel

```text
K_b
= r_b U^even_b
  + sum_{j != b} r_j (W^odd_j-W^odd_b)/(2 i pi (n_b-n_j)),
```

and reduced the endpoint to

```text
sum_b (R_w xi_L)_b K_b=O_M(L^(-M)).              (KERNEL-FREQ-DIV)
```

E73.291 identifies this kernel with the older commutator-Schur row of E73.263.
This is not a new proof of the scalar theorem, but it prevents a fork in the
program: the closed-weight frequency endpoint and the Cauchy-Schur commutator
endpoint are the same object.

## 2. Exact statement

Let

```text
H_L=H_L^A-H_L^P
```

be the explicit Gamma-prime CCM matrix and let `q=r` be one Cauchy row.  The
kernel `K` of E73.290 satisfies

```text
K = qH_L + alpha q_w + beta q_-w.                (KR)
```

The two Cauchy-gauge coefficients come only from the allowed constant gauges
in the closed weights `W'` and `U'`.

Consequently, for

```text
eta=R_w xi_L,       Q_w eta=0,
```

one has the exact scalar identity

```text
sum_b eta_b K_b = qH_L eta.                      (KR-pair)
```

Combining this with E73.263 gives

```text
sum_b eta_b K_b
= qH_LR_wxi_L
= -q[H_L,P_w]xi_L.                               (KR-comm)
```

Thus `KERNEL-FREQ-DIV` is exactly the Schur-commutator cancellation theorem.

## 3. Proof

The matrix entry `H_L(m,n)` is obtained by applying the same Gamma-prime
functional to the CCM cell `q_{mn}(y)`.

The row packet is

```text
B(y)=qQ_y eta=sum_b eta_b sum_j q_j q_{jb}(y).
```

Expanding every cell into the exact exponential-linear basis gives the
diagonal/off-diagonal coefficients used in E73.288.  Pairing those coefficients
with the closed Gamma-prime weights is therefore the same operation as applying
`H_L` to the row:

```text
<c^off,W'>+<c^diag,U'> = qH_L eta,
```

modulo the constant gauges.  The constant gauges add only a linear combination
of the two rows of `Q_w`, because:

```text
1. W^odd is invariant under constant shifts of W;
2. a constant shift of U^even contributes a multiple of r_b;
3. r is one row of Q_w.
```

Since `Q_w eta=0`, these gauges disappear in the paired scalar.  This proves
`KR-pair`.  Equation `KR-comm` is then E73.263:

```text
qH_LR_wxi_L=-q[H_L,P_w]xi_L.
```

## 4. Numerical certification

`E73_291_kernel_row_identity_probe.py` checks `K-qH_L` before and after
removing the Cauchy rowspace.

Representative output:

```text
 lam     L gamma row rawRel modRel pairKB rowHB pairErrB gaugePairB resPairB
  12   4.970   14.13   0 8.1e-02 2.2e-10  -20.89 -20.90   -23.44     -23.97   -22.75
  16   5.545   21.02   0 1.0e-01 1.6e-10  -18.13 -18.18   -19.61     -23.31   -19.64
  20   5.991   21.02   1 1.2e-01 3.9e-10  -17.90 -17.77   -17.45     -21.90   -17.45
```

Interpretation:

```text
rawRel  ~ 0.08--0.25  because the constant closed-weight gauge is visible;
modRel  ~ 1e-10       after quotienting by the Cauchy rowspace.
```

The paired scalar is much smaller than the row scale, so the numerical row
identity alone is not a certificate.  The proof must use the exact algebraic
identity above, not the floating residual.

## 5. Consequence for the route

E73.290 looked like a new frequency-kernel theorem.  E73.291 shows it is a
coordinate sharpening of the already surviving commutator theorem:

```text
KERNEL-FREQ-DIV
<=> qH_LR_wxi_L=O_M(L^(-M))
<=> q[H_L,P_w]xi_L=O_M(L^(-M)).
```

So the route is now unified:

```text
closed weights / diag-off kernel
     =
Cauchy-Schur commutator residual
     =
master scalar S_{a,w,L}.
```

No separate proof branch remains.  The single theorem still open is:

```text
Schur-Commutator Eigenline Cancellation:
q[H_L,P_w]xi_L=O_M(L^(-M)).
```

The frequency form tells us exactly what the commutator row is: a diagonal
`U^even` part plus a finite Hilbert-transform difference of `W^odd`.  This is
the proof-facing formula to use in the next analytic attack.

## 6. Program audit

Searches for `commutator-Schur`, `Cauchy-Schur`, `Loewner commutator`,
`K-DIAGOFF`, and `KERNEL-FREQ-DIV` show:

```text
old: E72.54/E72.62 exposed Loewner commutators for CCM cells;
old: E73.263 proved the Schur-commutator residual identity;
new: E73.290--291 identify the closed-weight diagonal/off-diagonal frequency
     kernel with that Schur row modulo Cauchy gauge.
```

Thus this step does not re-run an old failed commutator estimate.  It merges
the new exact frequency coordinates into the already audited commutator target.

## 7. Status

```text
proved: K-DIAGOFF equals qH_L modulo Cauchy gauge;
proved: KERNEL-FREQ-DIV is the same theorem as Schur-Commutator cancellation;
verified: row identity modulo Cauchy gauge numerically;
open: prove q[H_L,P_w]xi_L=O_M(L^(-M)) analytically.
```
