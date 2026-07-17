# E72.126 -- Top-mode flux gain

**Date:** 2026-07-09.
**Role:** isolate the missing factor in the bad-test upper bound.

## 0. From singular values to bad projections

Let:

```text
R_x = U_x Sigma_x V_x^*
```

be the shorted pushforward from E72.112, and let `v_1,...,v_q` be the right singular vectors included
in the bad subspace.  Write:

```text
c_l(tau_j)=<Y_x(tau_j),v_l>.
```

The direct singular energy is:

```text
sum_l sigma_l^2 |c_l(tau_j)|^2 = ||R_xY_x(tau_j)||^2.
```

E72.112 gives bounded flux, and E72.122 gives:

```text
sigma_1(R_x) = O(1/(sqrt(x)L)).
```

The trivial implication is:

```text
|c_l(tau_j)| <= O(sqrt(x)L),
```

which is one factor `L` too weak for `BUP`.

Therefore the exact missing theorem is not merely bounded flux.  It is the top-mode flux gain:

```text
sum_{l<=q} sigma_l^2 |c_l(tau_j)|^2 <= C/L^2.                (TFG)
```

Together with `sigma_l >= c_l'/(sqrt(x)L)` for the retained finite modes, `(TFG)` gives:

```text
sum_{l<=q}|c_l(tau_j)|^2 <= Cx.
```

This is precisely the singular-vector part of `BUP`.

## 1. Mass channel

The mass component has the same structure.  If:

```text
|m_xY_x(tau_j)| <= C/L,
||m_x|| >= c/(sqrt(x)L),
```

then the mass projection is `O(sqrt(x))`.  The current data show the projection is already on this
scale; the proof must again use the root/shorting identity rather than a raw Cauchy estimate.

## 2. Reformulated target

The bad-test square bound `(BTB)` from E72.125 follows from:

```text
top-mode flux gain:    ||Sigma_{<=q}V_{<=q}^*Y_x(tau_j)|| <= C/L,
mass flux gain:        |m_xY_x(tau_j)| <= C/L,
retained lower scales: sigma_l,||m_x|| >= c/(sqrt(x)L).
```

The first two statements are the genuinely new mathematical content.  They say that finite CCM roots
annihilate the leading shorted leakage modes by one logarithmic factor.

## 3. Diagnostic

The companion script:

```text
E72_126_top_mode_flux_probe.py
```

measures:

```text
||V_{<=q}^*Y||/sqrt(x),
||Sigma_{<=q}V_{<=q}^*Y||,
L||Sigma_{<=q}V_{<=q}^*Y||,
sigma_1 sqrt(x)L.
```

Representative output:

```text
E72.126 top-mode flux probe q=3
 lam   L roots  max|c_top|/sqrtx  max|s c|  max L|s c|  max s1sqrtxL  max tailFlux
   6  3.58     3        4.592e-01  5.486e-02   1.966e-01     5.543e-01    6.810e-03
   8  4.16     4        4.711e-01  6.224e-02   2.588e-01     6.246e-01    8.917e-03
  10  4.61     3        5.961e-01  3.918e-02   1.804e-01     4.559e-01    3.153e-03
  12  4.97     4        3.416e-01  2.285e-02   1.136e-01     5.039e-01    1.621e-03
  14  5.28     4        4.608e-01  2.310e-02   1.219e-01     3.405e-01    9.996e-04
```

The data support the strengthened scale:

```text
||Sigma_{<=q}V_{<=q}^*Y|| = O(1/L),
```

while the retained singular scale `sigma_1 sqrt(x)L` stays bounded away from explosion.

## 4. Status

```text
proved: bounded flux alone loses one logarithm and cannot prove BUP;
proved: BUP is implied by the top-mode and mass flux gains;
open:   prove these gains from the finite CCM root equation and shorted Feshbach structure.
```
