# Phase 92 - Cluster adjugate projectivization

## 1. Objective

Remove the one-line dominance and matched-width hypotheses from the endpoint
route by projectivizing the complete Feshbach cluster before taking any
singular limit.

## 2. Main identity

For the exact Feshbach data of E88.001, define

```text
N_t(z)
 =G_(t,z)^reg det F_t
  -h_(t,z)^eff adj(F_t)b_t^eff.                       (2.1)
```

Whenever `F_t` is invertible,

```text
G_t(z)=N_t(z)/det F_t.                                (2.2)
```

The determinant is independent of the safe variable and cancels exactly in
every normalized safe ratio.  The numerator extends through singular cluster
values without choosing an eigenline.

## 3. Work order

```text
E92.001  exact denominator-free cluster numerator;
E92.002  projective continuation through cluster singularities;
E92.003  parity polynomial and elimination of matched scales;
E92.004  inverse-free tangent current;
E92.005  corrected endpoint ledger and RDI crosswalk.
E92.006  global bordered fallback without a regular complement.
E92.007  cofinal projective diagonal without a uniform rate.
```

## Outcome

Closed; see [`PHASE_92_CLOSURE.md`](PHASE_92_CLOSURE.md) (“Exact projectivization before the endpoint limit”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: CA-1 fixed-L projective convergence; `CLUSTER-RDI-ANCHOR`; RDI-ANCHOR and Omega7.

## Contents

- `E92_001_DENOMINATOR_FREE_CLUSTER.md` — E92.001 - Denominator-free cluster numerator
- `E92_002_PROJECTIVE_CONTINUATION.md` — E92.002 - Projective continuation through the endpoint
- `E92_003_PARITY_POLYNOMIAL.md` — E92.003 - Exact parity polynomial
- `E92_004_INVERSE_FREE_TANGENT.md` — E92.004 - Inverse-free cluster tangent
- `E92_005_CORRECTED_ENDPOINT_LEDGER.md` — E92.005 - Corrected endpoint ledger
- `E92_006_GLOBAL_BORDERED_FALLBACK.md` — E92.006 - Global bordered fallback
- `E92_007_COFINAL_DIAGONAL.md` — E92.007 - Cofinal projective diagonal
- `PHASE_92_CLOSURE.md` — Phase 92 closure - Exact projectivization before the endpoint limit

## Relation to other phases

Continues [`phase-91-kato-coboundary-equivalence`](../phase-91-kato-coboundary-equivalence/); its open target passes to [`phase-93-direct-bordered-anchor`](../phase-93-direct-bordered-anchor/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
