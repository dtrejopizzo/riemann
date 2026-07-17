# E73.217 - Bordered Krawczyk certificate from BALL-ENTRY-CERT

Date: 2026-07-14.

## 1. Purpose

E73.215 gives entry balls for the closed finite matrix.  E73.208 gives the
Krawczyk inequality for the bordered eigenline system.  This note connects the
two directly.

## 2. Certified matrix radius

Let

```text
r_entry=max_{m,n} radius(H_mn),
d=2N+1.
```

Then

```text
||[H]-H_0||_op <= ||[H]-H_0||_F <= d r_entry = epsH.
```

Here `r_entry` is computed from E73.215:

```text
r_entry = R_ball_elementary + C_sec R_psi(K=16) + R_exp.
```

The script tests both `C_sec=1` and `C_sec=10^6`.

## 3. Krawczyk inequality

With `Y=J_0^{-1}` and `step=||YF(x_0)||`, use:

```text
step + ||Y|| epsH + ||Y||(epsH+2rho)rho < rho.
```

If a radius `rho` satisfies this inequality, the bordered eigenpair
`(mu,xi)` is uniquely enclosed in that ball.

## 4. Status

```text
implemented: finite Krawczyk certificate using the actual BALL-ENTRY epsH;
tested: C_sec=1 and C_sec=10^6 in small windows;
next: propagate [xi] through the Cauchy projection and final TRANS-CELL scalar.
```
