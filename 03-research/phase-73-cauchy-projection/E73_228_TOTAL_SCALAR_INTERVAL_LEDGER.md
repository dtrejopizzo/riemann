# E73.228 - Total scalar interval ledger

Date: 2026-07-14.

## 1. Purpose

E73.226 listed the finite local scalar certificate pieces separately.  E73.228
combines them row-by-row around the closed center:

```text
C_a=A_L^digamma[B_a]-P_L[B_a].
```

The total radius is:

```text
R_total = R_etaH + R_coeff + R_weight,
```

where:

```text
R_etaH   = scalar q_aHeta propagation radius from E73.219,
R_coeff  = coefficient-radius contribution through weight centers,
R_weight = weight-radius contribution through coefficient centers.
```

## 2. Result

The total interval remains tiny relative to the closed center in all tested
windows.

Worst inflated-sector ratio:

```text
R_total/|C_a| = 1.7e-14.
```

The dominant piece is `R_coeff`, not `R_etaH`:

```text
R_coeff > R_etaH >> R_weight.
```

This corrects the preliminary reading in E73.226/E73.225, where `R_etaH` was
identified as the likely dominant finite uncertainty before the complete sum
was assembled.

## 3. Interpretation

This is not a new obstruction.  `R_coeff` is also inherited from the certified
vector radius:

```text
rad(c_omega)<=||u_omega||rho_eta,
rad(l_omega)<=||v_omega||rho_eta.
```

The full center interval is therefore still controlled by the Krawczyk/Cauchy
vector certificate.  The weight radii are far smaller.

## 4. Finite local status

For the tested windows, the executable ledger gives:

```text
closed center scale:     L^-14 ... L^-22,
total radius scale:      L^-40 ... L^-56,
worst ratio:             1.7e-14.
```

Thus the finite local TRANS-CELL interval is numerically stable with large
margin.  The formal proof-facing replacements still required are:

```text
1. make the coefficient balls actual interval objects rather than Euclidean
   radius entries;
2. prove/cite the Bernoulli sector lemma for psi/psi_1;
3. wrap the final scalar sum with outward complex-ball summation.
```

## 5. Status

```text
implemented: executable total finite scalar interval ledger;
corrected: dominant finite uncertainty is R_coeff, not R_etaH;
role: ultraconservative cross-check, not the minimal closed scalar wrapper;
open: formal outward interval implementation and uniform theorem.
```

E73.230 removes the matrix-route double count and gives the proof-facing closed
scalar interval wrapper.
