# E73.262 - UNIF-ETA frontier and prior audit

Date: 2026-07-14.

## 1. Purpose

E73.259--E73.261 finished the finite certificate side of the current route.
This note freezes the mathematical frontier and audits it against the earlier
program so the next work does not loop through a known dead branch.

The endpoint is not a generic matrix estimate.  It is the uniform decay of one
certified scalar center:

```text
UNIF-ETA:
|q_a H_L (I-P_w) xi_L| <= A_M L^-M
```

for every `M`, uniformly over the admissible Cauchy rows and windows.

## 2. Equivalent forms now proved

Let

```text
E_L=H_L-mu_LI,
E_L xi_L=0,
rho_{a,w}=q_aH_L(I-P_w).
```

For a simple ground eigenvalue the reduced adjugate satisfies

```text
Adj_red(E_L)=scale * xi_L xi_L^*.
```

Therefore:

```text
rho_{a,w}Adj_red(E_L)
=scale*(rho_{a,w}xi_L)xi_L^*.
```

This proves the exact equivalence

```text
UNIF-ETA
<=> ETA-DIV
<=> normalized ETA-ADJ
<=> ETA-DET.
```

Here:

```text
ETA-DIV:
finite Gamma-prime coefficient identity for rho_{a,w}xi_L.

ETA-ADJ:
rho_{a,w}Adj_red(E_L)=O_M(L^-M)||Adj_red(E_L)||.

ETA-DET:
all row-replacement determinants
det ReplaceRow(E_L;i,rho_{a,w})
are O_M(L^-M) relative to the reduced cofactor scale.
```

These are equivalent certificates, not independent forcing mechanisms.

## 3. Finite certification status

The proof-facing finite pipeline is:

```text
BALL-ENTRY-CERT
=> bordered Krawczyk [xi_L]
=> Cauchy projection [eta_w]=(I-P_w)[xi_L]
=> scalar interval for q_aH_Leta_w
=> normalized ETA-ADJ interval.
```

E73.261 shows that in the tested windows the certified radius is far below the
center.  Thus finite verification is no longer failing because of:

```text
1. matrix entry uncertainty;
2. eigenline instability;
3. Cauchy projection amplification;
4. adjugate/cofactor normalization;
5. row-replacement determinant conditioning.
```

The remaining theorem is analytic decay of the center itself.

## 4. Non-repeating audit

The following routes are now explicitly excluded as closing mechanisms.

```text
Phase 72 / E72.348--E72.354:
adjugate, cofactor, determinant, and rowspace tests detect null leakage but
become tautological if used as the proof source.

E73.256:
DD-local quotient projections change coordinates but leave the scalar pairing
with xi_L unchanged.

E73.257:
Q_w eta=0 and endpoint/Dirichlet constraints alone give no useful bound on
q_aH_Leta_w; the operator norm on ker Q_w is enormous.

E73.258:
autonomous transverse eigen-residual smallness routes through P_w xi_L and
therefore returns to the circular branch.

E73.239:
endpoint moments and the balanced ramp are normal forms only; their moment
annihilator does not explain the center decay.

E73.255:
no fixed pair/parity mode of the b-vector explains the cancellation.
```

Consequently the next proof cannot be another generic rowspace, determinant,
endpoint, parity, or quotient argument.

## 5. Analytic form that remains

E73.237 gives the most useful zero-free analytic form.  For the eta packet

```text
B(y)=sum_omega c_omega e^(iomega y)
    +y sum_omega l_omega e^(iomega y),
```

after subtracting the neutral balanced ramp,

```text
B^bal(y)=B(y)-B'(0)r_*(y),
F_L[r_*]=0,
```

one has:

```text
B^bal(0)=0,
(B^bal)'(0)=0,
B^bal(L)=0,
F_L[B]=F_L[B^bal].
```

The scalar center is exactly

```text
F_L[B]
= int_0^L K_L(t)(B^bal)''(t)dt,                 (1)
```

where

```text
K_L(t)=int_t^L (y-t)W_L(y)dy
 -sum_{p^k: klog p>=t}(log p)p^(-k/2)(klog p-t).
```

Thus `UNIF-ETA` is equivalent to the signed curvature orthogonality:

```text
|int_0^L K_L(t)(B^bal)''(t)dt| <= A_M L^-M.      (2)
```

The constraints

```text
sum c_omega=0,
sum l_omega=0,
B'(0)=sum iomega c_omega+sum l_omega
```

are necessary but not sufficient.  The missing input must be the actual
finite eigen-equation:

```text
(H_L-mu_LI)xi_L=0.
```

## 6. Minimal theorem to prove next

The next load-bearing theorem should be stated in the strongest non-circular
form:

```text
Eigenline Curvature Orthogonality Theorem.
Let xi_L be the normalized ground eigenline of the explicit finite
Gamma-prime Hermitian matrix H_L, and let B_{a,w,L}^{eta} be the transverse
Cauchy eta-packet built from eta_w=(I-P_w)xi_L.  Then for every M there are
constants A_M,L_M such that, for all L>=L_M and all admissible rows/windows,

|int_0^L K_L(t)((B_{a,w,L}^{eta})^bal)''(t)dt|
<= A_M L^-M.
```

This theorem would prove `UNIF-ETA`, hence the scalar WRL annihilation gate in
the current route.  It does not use zeros as input and does not ask for a
positive Weil form.  It is exactly the missing analytic identity.

## 7. What a proof must exploit

The only remaining non-rejected source of cancellation is that the same
eigenline `xi_L` appears in both:

```text
1. the eta packet B_{a,w,L}^{eta};
2. the Gamma-prime eigen-equation E_L xi_L=0.
```

Therefore the proof should derive additional coefficient relations from
`E_L xi_L=0` and then show that the curvature weight in (1) lies in the
annihilator of those relations up to `O_M(L^-M)`.

Equivalently:

```text
EIG-COEFF:
the coefficient vector of eta_w satisfies finite eigenline relations whose
annihilator contains the second-Abel curvature weight modulo O_M(L^-M).
```

This is the first point after the finite certification chain where genuinely
new analysis is required.

## 8. Status

```text
proved: finite certificate pipeline for the scalar center;
proved: UNIF-ETA <=> ETA-DIV <=> ETA-ADJ <=> ETA-DET;
proved: second-Abel balanced curvature form;
audited: determinant/rowspace/endpoint/parity/quotient mechanisms do not close;
open: Eigenline Curvature Orthogonality / EIG-COEFF.
```

