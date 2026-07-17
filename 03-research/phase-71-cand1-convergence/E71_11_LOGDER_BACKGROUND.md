# E71.11 -- log-derivative background probe for the CCM m-function

**Date:** 2026-07-07.
**Script:** `E71_11_logder_background_probe.py`.
**Role:** test the first canonical background candidates for the Weyl m-function target in E71.10.

## Setup

E71.10 identifies the finite spectral carrier as

```text
m_N(s) = sum_k xi_k/(s-d_k),
d_k = 2*pi*k/L.
```

Writing

```text
m_N(s) = P_N(s)/Q_N(s),
```

the CCM finite roots are the zeros of `P_N`. The desired Hurwitz theorem needs a normalized/deformed
object built from `P_N`, but E71.8-E71.9 showed that raw products are contaminated by finite-section
background roots.

## Diagnostic

On the zero-free interval `[0.4,12]`, compare `Xi'/Xi` against:

1. the log derivative of the all-root product over CCM roots;
2. the pole-relative log derivative

```text
m_N'/m_N = P_N'/P_N - Q_N'/Q_N;
```

3. the sine-depoled log derivative

```text
d/ds log(sin(sL/2)m_N(s)).
```

These are all computed from finite CCM data. No zeta zero locations are used.

## Why this matters

If either pole-relative or sine-depoled log derivatives approximate `Xi'/Xi`, then the missing
background in E71.10 has a concrete canonical form.

If they fail, the background is not merely:

- the pole mesh `d_k`;
- the sine comb cancelling poles;
- the all-root product background.

Then the desired determinant must be a subtler de Branges/Fredholm normalization.

## Result

All three simple log-derivative backgrounds fail. Results are recorded in `E71_11_RESULTS.md`.

The next zero-independent candidate is not a static pole/sine background but a dynamic finite-section
filter: roots stable under refinement in `N` are physical; drifting roots are background.

## Audit constraints

The test is allowed because it does not use:

- Weil positivity;
- `epsilon_0>0`;
- fitted zero locations;
- KMS or zeta partition normalization;
- global Stone/unitarity.

It is still only diagnostic. A successful approximation would not be a proof until promoted to local
uniform convergence on complex compact sets.
