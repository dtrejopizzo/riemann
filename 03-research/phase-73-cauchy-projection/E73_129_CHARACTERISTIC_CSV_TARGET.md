# E73.129 - Characteristic CSV Target

Date: 2026-07-12.

E73.124--E73.128 narrow the CSV problem:

```text
CSV is arithmetic, not arch/free geometry.
CSV is not proved by displacement-image projection.
CSV is not uniformly explained by root proximity.
```

The correct target is direct characteristic interpolation.

## 1. Finite characteristic function

Let

```text
C_x(s)=sum_n xi_n/(s-d_n),
Phi_N(s)=(2/sqrt(L)) sin(sL/2) C_x(s).
```

`Phi_N` is entire because the sine factor cancels the pole mesh.

The CSV requirement is equivalent to:

```text
|Phi_N(-gamma)| <= C L^-17 * |(2/sqrt(L))sin(gamma L/2)|
```

for all critical rows `gamma` appearing in the natural-height Phase 73
gate.

## 2. The theorem to prove

```text
Characteristic CSV Theorem.
There exist C and L0 such that for every L>=L0 and every natural-height
critical row gamma in the Phase 73 standard boxes,

|Phi_N(-gamma)| <= C L^-17.
```

If the sine factor is retained, the equivalent Cauchy version is:

```text
|C_x(-gamma)| <= C L^-17.
```

away from the harmless sine zeros; near sine zeros the characteristic
statement is even stronger than needed.

## 3. What this theorem must not use

It must not use:

```text
known zeta zero locations as input;
root proximity of Phi_N as an assumption;
global scalar normalization fitted to Xi;
positivity / RH / de Branges.
```

Allowed data:

```text
the explicit finite CCM matrix C_E,
the zeta-coupled ground vector xi from C_E xi=mu xi,
the prime/Gamma cell formula,
the pole mesh d_n=2pi n/L,
the critical row heights gamma only as evaluation points.
```

## 4. Relation to E71

E71.6 showed that raw global convergence

```text
c_N Phi_N -> Xi
```

with a naive scalar fit is not available.

E73.129 asks for much less:

```text
finite interpolation smallness at a fixed list of critical rows.
```

This is compatible with E71.12 persistence:
physical critical rows may be detected by stable finite interpolation even
when global normalization remains unresolved.

## 5. Route to proof

The proof should attack the evaluation functional

```text
Ev_gamma(xi)=Phi_N(-gamma)
```

directly from the finite eigen-equation.

A promising finite identity has the form:

```text
Ev_gamma
= arithmetic cell cancellation + endpoint residual,
```

where the arithmetic cell cancellation is the coupled zeta-prime part that
is absent in the arch/free vector, as shown in E73.124.

The finite statement to seek is therefore:

```text
EV-CELL:
Phi_N(-gamma)
 =
 R_arch/gamma(L) + R_prime/gamma(L)
```

with exact cancellation of the leading arch/free term and residual

```text
|R_arch/gamma + R_prime/gamma| <= C L^-17.
```

This is the next mathematical construction.  It is not another gate; it is
the arithmetic interpolation identity behind CSV.

## 6. Why this matters for Omega7

E73.123 proves:

```text
CSV_17 + elementary envelopes
=> Asymptotic Standard-Box Theorem.
```

E73.120 supplies the finite base/transition manifest.

Therefore:

```text
Characteristic CSV Theorem
+ E73.123
+ E73.120
=> Uniform GATE-73
=> scalar WRL
=> Omega7.
```

