# E73.229 - Bernoulli sector proof for psi/psi_1

Date: 2026-07-14.

## 1. Purpose

E73.214 isolated the only special-function lemma still needed by the finite
certificate:

```text
|R_K^psi(z)|  <= C_sec |B_{2K}|/(2K |z|^(2K)),
|R_K^psi1(z)| <= C_sec |B_{2K}|/|z|^(2K+1),
```

for

```text
z=R+1/4-iomega/2,       R=80.
```

This note gives the proof-facing derivation and fixes the role of `C_sec`.

## 2. Euler-Maclaurin remainder

For `Re z>0`, Euler-Maclaurin applied to the logarithmic derivative of the
Weierstrass product for `Gamma` gives

```text
psi(z)
= log z - 1/(2z) - sum_{j=1}^{K-1} B_{2j}/(2j z^(2j))
  + R_K^psi(z),
```

with periodic-Bernoulli remainder

```text
R_K^psi(z)
= - int_0^infty B_{2K}({t})/(2K (t+z)^(2K+1)) dt.      (1)
```

Differentiating gives

```text
psi_1(z)
= 1/z + 1/(2z^2) + sum_{j=1}^{K-1} B_{2j}/z^(2j+1)
  + R_K^psi1(z),
```

where

```text
R_K^psi1(z)
= int_0^infty B_{2K}({t}) (2K+1)/(2K (t+z)^(2K+2)) dt. (2)
```

These formulas use the same Bernoulli normalization as E73.210.

## 3. Bernoulli-polynomial bound

For even Bernoulli polynomials,

```text
sup_{0<=u<=1} |B_{2K}(u)| <= |B_{2K}|.
```

Therefore, writing `x=Re z>0`,

```text
int_0^infty |t+z|^(-2K-1) dt
<= int_0^infty (t+x)^(-2K-1) dt
= x^(-2K)/(2K),
```

and

```text
int_0^infty |t+z|^(-2K-2) dt
<= x^(-2K-1)/(2K+1).
```

Substituting in (1)--(2) gives the `Re z` bounds:

```text
|R_K^psi(z)|
<= |B_{2K}|/(2K) * x^(-2K)/(2K)
<= |B_{2K}|/(2K x^(2K)),

|R_K^psi1(z)|
<= |B_{2K}|/(2K) * x^(-2K-1)
<= |B_{2K}|/x^(2K+1).
```

The displayed bounds are deliberately looser than the integral gives, matching
the conservative numerical convention of E73.210.

## 4. Conversion to the `|z|` form

Let

```text
sigma(z)=|z|/Re z >= 1.
```

Then

```text
x^(-2K)     = sigma(z)^(2K) |z|^(-2K),
x^(-2K-1)   = sigma(z)^(2K+1) |z|^(-2K-1).
```

Thus the E73.210/E73.216 bounds hold with

```text
C_sec >= max_{z in window} sigma(z)^(2K+1).          (3)
```

For the Phase 73 finite windows,

```text
z=80+1/4-iomega/2
```

has very small angle, so `sigma(z)` is close to `1`.  Even if one uses the very
coarse proof-facing choice

```text
C_sec=10^6,
```

E73.217--E73.228 show that all tested finite certificates retain large margin.
E73.216 shows that the entry certificate at `K=16` tolerates constants around
`10^17`.

## 5. Result

**Lemma 229.1 (sector Bernoulli bound).**  Fix a finite Phase 73 window and
let

```text
S=max_z |z|/Re z
```

over all `psi/psi_1` arguments in that window.  For every `K>=1`, the
remainders in the E73.210 expansions satisfy

```text
|R_K^psi(z)|  <= S^(2K)   |B_{2K}|/(2K |z|^(2K)),
|R_K^psi1(z)| <= S^(2K+1) |B_{2K}|/|z|^(2K+1).
```

Consequently the E73.210 numerical bound is rigorous with any

```text
C_sec >= S^(2K+1).
```

For the proof-facing audits in this phase we may take `C_sec=10^6`, far below
the certified slack at `K=16`.

## 6. Status

```text
proved: sectorial Bernoulli remainder bound in the E73.210 normalization;
removed: special-function remainder as an informal heuristic;
remaining: final outward scalar assembly wrapper and uniform theorem.
```
