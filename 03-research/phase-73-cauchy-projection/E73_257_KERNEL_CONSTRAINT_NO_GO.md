# E73.257 - Kernel-constraint no-go for ETA-DIV

## 1. Purpose

E73.235 identifies the remaining scalar theorem as `ETA-DIV`:

```text
eta_w=(I-P_w)xi_L,        Q_w eta_w=0,
C_{a,w}=q_aH_Leta_w=O_M(L^-M).
```

E73.189--E73.193 already extract the endpoint consequences of `Q_w eta=0`:

```text
B_a(0)=0,        B_a(L)=0,
B_a'(0)=-(2/L)(sum q_a)(sum eta),
```

and then remove the rank-one endpoint derivative by the balanced ramp.

This note checks the stronger possible hope:

```text
Can Q_w eta=0 alone force C_{a,w}=q_aH_Leta small?
```

## 2. Test

For each Cauchy plane `Q_w`, let `Z_w` be an orthonormal basis of `ker Q_w`.
Compare:

```text
actual     = |q_aH_L(I-P_w)xi_L|,
opKer      = ||q_aH_L Z_w||,
sampleMax  = max over deterministic unit vectors v in ker Q_w of |q_aH_Lv|.
```

If `Q_w eta=0` were the main mechanism, `opKer` would have to live near the
same scale as `actual`.

## 3. Result

It does not.  The functional is large on the Cauchy kernel; the actual
eigenline vector is exceptional.

Representative output:

```text
 lam      L gamma row kerDim actualB opKerB sampleMaxB sampleMeanB gapActualToOpB qetaB
   8    4.159  14.13   0     11   -21.68   -3.18      -3.51       -4.02          18.50  -26.80
  10    4.605  21.02   0     15   -14.98   -3.16      -3.43       -3.89          11.82  -25.20
  12    4.970  14.13   0     19   -20.64   -1.47      -1.66       -2.21          19.17  -23.58
  16    5.545  21.02   0     39   -18.18   -0.68      -1.21       -1.76          17.50  -22.04
  20    5.991  21.02   0     47   -17.65    1.18       0.88        0.27          18.84  -21.39
```

The gap `opKer/actual` is typically `L^11` to `L^19`.

## 4. Consequence

Rejected:

```text
KER-Q-DIV:
Q_w eta=0 alone implies q_aH_Leta=O_M(L^-M).
```

Kept:

```text
EIGEN-KER-DIV:
For the special vector eta_w=(I-P_w)xi_L, with H_Lxi_L=mu_Lxi_L,
q_aH_Leta_w=O_M(L^-M).
```

Thus the remaining proof cannot be a generic endpoint/Dirichlet theorem for
all packets with `B(0)=B(L)=0`.  It must use the finite CCM eigenvector origin
of `eta_w`.

Equivalently, the required theorem is not:

```text
F_{a,w}|ker Q_w is small in operator norm.
```

That norm is false.  The required theorem is an evaluated divisibility:

```text
F_{a,w}(eta_w) is small for the eigenline-produced eta_w.
```

## 5. Revised minimal target

Combining E73.256 and E73.257, the scalar side of the route is now:

```text
EIGEN-KER-DIV:
Given
  H_Lxi_L=mu_Lxi_L,
  eta_w=(I-P_w)xi_L,
  Q_weta_w=0,
prove
  q_aH_Leta_w=O_M(L^-M)
for the admissible Cauchy rows.
```

The finite coefficient form from E73.235 remains the correct proof-facing
language:

```text
q_aH_Leta_w
= sum_omega c_omega(eta_w)W_omega
 +sum_omega l_omega(eta_w)V_omega
 +E_exp.
```

But the cancellation must be derived from the eigenvector equation and the
explicit Gamma-prime weights, not from `Q_weta_w=0` alone.

