# E73.133 - From Critical Evaluation Kernel to CSV

Date: 2026-07-12.

E73.132 suggested a kernel theorem for normalized critical evaluation rows.
E73.134 sharpens it: because row norms can vary near pole-mesh resonances,
the correct statement is rowwise, not an aggregate `||K_L xi_L||` bound.

## 1. Normalized evaluation matrix

For each critical row `gamma`, define

```text
k_gamma(d_n)=1/(-gamma-d_n),
e_gamma = k_gamma / ||k_gamma||_2.
```

Let `K_L` be the matrix whose rows are the `e_gamma` in the natural-height
critical window.

The Cauchy value is

```text
C_x(-gamma)=<xi_L,k_gamma>
           =||k_gamma||_2 <xi_L,e_gamma>.
```

## 2. Elementary row norm bound

For the pole mesh

```text
d_n=2pi n/L,
```

and a fixed critical height `gamma`, the generic row norm obeys

```text
||k_gamma||_2^2
 =
 sum_n 1/(gamma+d_n)^2
 <= C L,
```

provided `gamma` stays uniformly separated from the pole mesh.

Thus

```text
||k_gamma||_2 <= C L^(1/2).
```

This part is purely elementary: compare the mesh sum with

```text
(L/2pi) int dx/(gamma+x)^2
```

plus the nearest-pole term.

But Phase 73 rows are not always uniformly separated from the pole mesh.
Direct checks show occasional near-pole amplification:

```text
rowNorm exponent can reach about L^2.6 in the tested boxes.
```

Therefore the safe elementary statement is

```text
||k_gamma||_2 <= C L^p,
```

where `p` is the mesh-separation exponent for the box.  For the tested
rows, `p=3` is safe.

## 3. Kernel theorem implies CSV

Assume the rowwise Critical Evaluation Kernel Theorem:

```text
ROW-KER_17:
for every critical row gamma,

|<xi_L,e_gamma>| <= C_K L^{-17-p_gamma},

where ||k_gamma|| <= C_p L^{p_gamma}.
```

Therefore

```text
|C_x(-gamma)|
 = ||k_gamma||_2 |<xi_L,e_gamma>|
 <= C L^{p_gamma} L^{-17-p_gamma}
 <= C L^-17.
```

This is exactly `CSV_17`.

E73.134 measures the rowwise margin

```text
q_gamma-p_gamma >= 17
```

for all tested asymptotic rows (`lambda>=20`), including near-pole rows.

## 4. Variational formulation

Since `xi_L` is the ground vector of the zeta-coupled CCM matrix `H_L`,
`KER_q` is equivalent to saying the ground vector is almost feasible for
the constrained minimization

```text
min <v,H_L v>,  ||v||=1,  K_L v=0.
```

A sufficient spectral form is:

```text
inf_{||v||=1, K_L v=0} <v,H_L v>
 -
 lambda_0(H_L)
 <= C L^{-2q}.
```

Indeed, adding the penalty `rho K_L^T K_L` gives

```text
lambda_0(H_L + rho K_L^T K_L) - lambda_0(H_L)
 <= rho ||K_L xi_L||^2.
```

Conversely, if the penalized energy shift is uniformly small and the
ground gap is controlled, one obtains a bound on `||K_L xi_L||`.

## 5. Current target

The remaining theorem is therefore:

```text
Rowwise Critical Evaluation Kernel Theorem.
For all sufficiently large L, the zeta-coupled CCM ground vector satisfies

|<xi_L,e_gamma>| <= C L^{-17-p_gamma}
```

where

```text
||k_gamma|| <= C L^{p_gamma}.
```

Together with row-norm accounting, this implies:

```text
CSV_17.
```

Then E73.123 gives the asymptotic standard-box theorem, and E73.120
supplies the finite base/transition manifest.
