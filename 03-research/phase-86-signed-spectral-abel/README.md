# Phase 86 - Signed spectral Abel reduction

## 1. Objective

Prove or sharply reduce the two signed parity sums left by Phase 85 while
preserving cancellation across the complementary spectrum.

## 2. Binding target

For each parity channel, order the complementary eigenvalues and prove that

```text
coefficient times
sum_q safe_weight_q Delta_P(lambda_q) -> 0             (2.1)
```

locally uniformly on safe sets, with one derivative.

## 3. Restrictions

```text
- no termwise bound on Delta_P(lambda_q);
- no maximum-partial-sum estimate is accepted without scale verification;
- endpoints in Abel summation are retained;
- the parity channels remain separate on the imaginary axis;
- any identification with historical scalar WRL is made explicitly.
```

## 4. Work order

```text
E86.001  exact finite Abel identity.
E86.002  crude ceiling autopsy.
E86.003  variation-weighted return criterion.
E86.004  first complementary mode and lower-variation tail.
```

## Outcome

Closed at localization grade; see [`PHASE_86_CLOSURE.md`](PHASE_86_CLOSURE.md) (“variation localization”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: FM-E and FM-O; the two d_2 tail estimates; a cofinal rank schedule preserving the projective limit; the outer arithmetic anchor and Omega7.

## Contents

- `E86_001_FINITE_ABEL_IDENTITY.md` — E86.001 - Exact finite spectral Abel identity
- `E86_002_CEILING_AUTOPSY.md` — E86.002 - Autopsy of the crude cumulative ceiling
- `E86_003_VARIATION_WEIGHTED_RETURN.md` — E86.003 - Variation-weighted return criterion
- `E86_004_FIRST_MODE_LOCALIZATION.md` — E86.004 - First complementary mode localization
- `PHASE_86_CLOSURE.md` — Phase 86 closure - variation localization

## Relation to other phases

Continues [`phase-85-parity-weyl-defect`](../phase-85-parity-weyl-defect/); its open target passes to [`phase-87-euler-deformation-discriminant`](../phase-87-euler-deformation-discriminant/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
