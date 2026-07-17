# E73.042 - WCS minimal endpoint

## 1. Purpose

E73.040 and E73.041 audited the mesh-root covering route.  The finite Cauchy divisor is exact, but
root-distance certificates do not improve the final weighted budget.

The remaining endpoint is therefore the direct weighted Cauchy smallness estimate.

## 2. Definitions

Let an off-line Hermite cluster be centered at

```text
a=alpha+i tau,        alpha>0,
```

with natural-height multiplicity `m`.  Let `K_L={i gamma_k}` be the critical natural-height window.

From E73.037 define the explicit geometric bound

```text
G_theta,m(a,i gamma_k)
```

for the confluent Hermite kernel:

```text
||h_A(i gamma_k)||_Herm <= G_theta,m(a,i gamma_k).
```

Let

```text
C_x(i gamma_k)=sum_n xi_n/(-gamma_k-d_n)
```

be the finite CCM Cauchy spectral defect, and let

```text
M_L(gamma_k)=|1-exp(i gamma_k L)|.
```

## 3. WCS

The minimal sufficient endpoint is:

```text
WCS:
e^(alpha L) sum_{gamma_k in K_L}
G_theta,m(a,i gamma_k)
M_L(gamma_k)
|C_x(i gamma_k)|
<= L^B.
```

This is a finite scalar inequality.  It contains no Cauchy matrix inverse and no hidden projection.

## 4. Proof that WCS closes the Phase 73 gate

By E73.037,

```text
||h_A(i gamma_k)||_Herm <= G_theta,m(a,i gamma_k).
```

Therefore

```text
e^(alpha L) sum_k
||h_A(i gamma_k)||_Herm
M_L(gamma_k)
|C_x(i gamma_k)|
<=
e^(alpha L) sum_k
G_theta,m(a,i gamma_k)
M_L(gamma_k)
|C_x(i gamma_k)|.
```

The right-hand side is at most `L^B` by `WCS`.  Hence `PFD` holds.

E73.036 proves

```text
PFD => DATA-HERM.
```

E73.032 and E73.023 give

```text
DATA-HERM => CC-PROJ => NAT-PROJ.
```

E72.396 gives

```text
NAT-PROJ => scalar WRL branch.
```

Thus

```text
WCS => scalar WRL.
```

Within the Phase 72 route, scalar WRL feeds the compact branch toward `Omega_7`.

## 5. Why WCS is minimal after the audits

Earlier candidates attempted to prove `WCS` through stronger intermediate mechanisms:

```text
PI-LEB:      false for close off-line clusters;
GEOM:        cannot overcome e^(alpha L);
MOMENT:      universal Hermite cancellation is absent;
MRC-abs:     derivative envelope with sum |xi_n| is too weak;
VAR-MRC:     signed derivative variation does not improve the weighted budget.
```

After these audits, the non-tautological finite content is exactly the smallness of the weighted
critical Cauchy data in `WCS`.

## 6. Finite certificate format

For fixed `L`, `theta`, natural-height critical window `K_L`, and an off-line cluster box

```text
Box = {alpha in [alpha_0,alpha_1], tau in [tau_0,tau_1], m fixed},
```

a finite certificate for `WCS` consists of:

```text
1. upper bounds for G_theta,m(alpha+i tau,i gamma_k) on the box;
2. exact values or interval enclosures for M_L(gamma_k);
3. interval enclosures for |C_x(i gamma_k)|;
4. a final interval sum bounded by L^B.
```

All four components are finite:

```text
G_theta,m: explicit elementary formula;
M_L: elementary scalar phase;
C_x: finite rational Cauchy sum;
sum: finite positive sum.
```

This is the promised finite verifiable identity form.

## 7. Remaining uniform theorem

The unresolved analytic theorem is the uniform version:

```text
Uniform WCS:
There exist B and L0 such that for every L>=L0 and every natural-height off-line Hermite cluster A,
WCS(A,L) holds.
```

This is now the exact place where new mathematics is required.
