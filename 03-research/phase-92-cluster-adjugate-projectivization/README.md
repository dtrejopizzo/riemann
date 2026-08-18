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
