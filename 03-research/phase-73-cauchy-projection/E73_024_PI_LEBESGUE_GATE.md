# E73.024 - Pi Lebesgue gate

## 1. Starting point

E73.023 identifies the scalar dual endpoint with the cancelled Cauchy projection:

```text
CC-PROJ:
max_{b in O_L} e^(Re b L)
|sum_{k in K_L} Pi(b,k)g_cancelled(k)| <= L^B.
```

E72.327 proves the critical-line polynomial bound:

```text
CRIT-POLY:
max_{k in K_L}|g_cancelled(k)| <= L^{B_1},
```

provided the active pole-even dimension is polynomial in `L`.

Therefore `CC-PROJ` follows from the purely Cauchy-geometric estimate:

```text
PI-LEB:
max_{b in O_L} e^(Re b L) sum_{k in K_L}|Pi(b,k)| <= L^{B_2}.      (1)
```

Indeed,

```text
e^(Re b L)|sum_k Pi(b,k)g_cancelled(k)|
<= e^(Re b L)sum_k|Pi(b,k)| max_k|g_cancelled(k)|
<= L^{B_1+B_2}.
```

## 2. Meaning

This is a significant simplification.  The previous formulation made `NAT-SRC` look like a delicate
orthogonality between the arithmetic eigenpacket and the off-line source.  After E73.023, the
critical data are already the cancelled divided-difference values controlled by E72.327.  The only
remaining possible exponential loss is the Cauchy interpolation operator.

Thus this sufficient route would move the remaining analytic theorem into finite Cauchy geometry:

```text
prove weighted Lebesgue control for the off-line Cauchy-Schur projection kernel.
```

E73.025 audits this point: such a bound is false for arbitrary positive-half-plane clusters.  Hence
`PI-LEB-NH` must be proved using the actual natural-height node geometry, confluent/Hermite
normalization, or cancellation of the critical data in the bad Cauchy directions.

## 3. Explicit kernel

From E73.002,

```text
Pi(b,k)=
  1/D_O'(-b)
  sum_{a in O_L}
     D_O(a) ell_a(-b)/(a+k),
```

where

```text
D_O(s)=prod_{c in O_L}(s+c),
ell_a(s)=prod_{c in O_L,c!=a}(s-c)/(a-c).
```

So `PI-LEB` is a finite rational inequality involving only the off-line node set `O_L` and critical
node set `K_L`.

## 4. Tested behavior

E73.024 measures

```text
e^(Re b L)sum_k|Pi(b,k)|
```

for the fixed diagnostic windows.  It remains between:

```text
1.7e-3 and 1.7e1.
```

The signed output is already below the absolute ceiling, but this extra signed cancellation is not
load-bearing if `PI-LEB` holds through natural height.

## 5. Remaining theorem

The natural-height version must handle growing node sets.  The precise remaining gate is:

```text
PI-LEB-NH:
For natural-height off-line and critical windows from E72.395--E72.396,
the residue kernel Pi satisfies

max_{b in O_L} e^(Re b L)sum_{k in K_L}|Pi(b,k)| <= L^B.
```

If `PI-LEB-NH` holds, then:

```text
PI-LEB-NH + E72.327 CRIT-POLY
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL
=> Omega_7.
```

## 6. Status

```text
proved: CRIT-POLY + PI-LEB-NH implies CC-PROJ;
validated: fixed-window Pi amplification is polynomial-sized;
open: prove PI-LEB-NH for natural-height Cauchy node sets.
```

This is a sufficient route.  E73.025 shows that the finite Cauchy Lebesgue inequality is itself a
serious natural-height theorem, not an automatic estimate.
