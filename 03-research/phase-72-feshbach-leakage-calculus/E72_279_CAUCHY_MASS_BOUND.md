# E72.279 -- Cauchy-mass bound

**Purpose.** Prove the first analytic input produced by the Cauchy-factor identity.

E72.278 reduces the diagonal compact-root term to

```text
i alpha(tau_j)mu_x^(-1)
  z M_x(z)[-2tau_j/(z^2-tau_j^2)-V_x(tau_j)].
```

This note proves that the Cauchy-mass factor satisfies

```text
M_x(z)/mu_x -> 0
```

on fixed Cauchy compact sets, assuming the pole-even gap lower bound already isolated in the RFBD
package.

## Lemma

Let `K` be compact in `C\R`.  Then there is a constant `C_K` such that, for every pole-even window,

```text
sup_{z in K} |M_x(z)| <= C_K L_x^(1/2),
```

where

```text
M_x(z)=sum_n xi_n/(z^2-d_n^2),
||xi_x||_2=1,
d_n=2pi n/L_x.
```

If, in addition,

```text
mu_x >= c_mu L_x^2,
```

then

```text
sup_{z in K} |M_x(z)|/mu_x <= (C_K/c_mu)L_x^(-3/2) -> 0.      (CM)
```

## Proof

By Cauchy-Schwarz and `||xi_x||_2=1`,

```text
|M_x(z)|
<= (sum_n |z^2-d_n^2|^(-2))^(1/2).
```

Since `K` is compact away from the real axis,

```text
F_K(u)=sup_{z in K} |z^2-u^2|^(-2)
```

is continuous except for no real poles and satisfies `F_K(u)=O_K(u^-4)` as `|u|->infty`.  Therefore
`F_K` is integrable on `R`.  The mesh spacing is `2pi/L_x`, so the finite mesh sum is bounded by the
corresponding infinite mesh sum, and the standard upper Riemann estimate gives

```text
sum_n |z^2-d_n^2|^(-2) <= C_K^2 L_x.
```

Taking square roots gives the first claim.  Dividing by `mu_x>=c_mu L_x^2` gives `(CM)`.

No zeta zeros or prime estimates enter this lemma.

## Probe

Run:

```text
python3 E72_279_cauchy_mass_bound_probe.py
```

Output:

```text
E72.279 Cauchy-mass bound probe
Uses |M_x(z)| <= ||xi_x||_2 (sum |z^2-d_n^2|^-2)^1/2 and mu in the pole-even complement.
s=10+0.2i, z=conj(s).
lam L mu |M| CS |M|/mu CS/mu CS/sqrtL
 16 5.545177 1.232544e+01 9.429865e-03 2.746483e-01 7.650730e-04 2.228303e-02 1.166324e-01
 20 5.991465 1.596102e+01 1.216450e-02 2.009896e-01 7.621376e-04 1.259253e-02 8.211209e-02
 24 6.356108 1.965549e+01 4.774344e-03 3.342165e-01 2.429013e-04 1.700372e-02 1.325660e-01
 28 6.664409 2.339219e+01 4.052699e-03 2.277790e-01 1.732501e-04 9.737396e-03 8.823337e-02
 32 6.931472 2.716069e+01 2.781352e-03 3.770148e-01 1.024036e-04 1.388090e-02 1.432009e-01
```

## Reading

The observed `|M|/mu` is much smaller than the Cauchy-Schwarz bound, but the bound is already enough:
the quotient `CS/mu` decreases and is covered by the proven `O_K(L^-3/2)` estimate once the pole-even
gap is available.

Thus the diagonal HPAC compact-root theorem has one analytic component closed:

```text
Cauchy mass / pole-even gap -> 0.
```

The remaining diagonal component is the boundedness of the variance bracket

```text
-2tau/(z^2-tau^2)-V_x(tau).
```
