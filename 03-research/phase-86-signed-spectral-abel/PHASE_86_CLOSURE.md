# Phase 86 closure - variation localization

## 1. Exact Abel reduction

Each parity response has the exact representation

```text
response
 =-coefficient d_1 sum_j pi_j B_j,                    (1.1)
```

where `pi` is the probability measure formed from the monotone variation of
the cluster Weyl defect.

The crude global ceiling is a valid but badly mis-scaled upper bound.  Exact
finite diagnostics show that the variation measure avoids the late cumulative
maximum.

## 2. First-mode theorem

The variation is localized at the first complementary pole.  The exact
decomposition is

```text
response
 =-coefficient d_1b_1+tail,

|tail|
 <=|coefficient|d_2 max_{j>=2}|B_j-B_1|.              (2.1)
```

Thus the full signed spectral sum is reduced to two first-mode products and
two strictly lower-variation tails.

## 3. Closure decision

Phase 86 is closed at localization grade.

```text
closed:
  finite Abel identity;
  crude ceiling route;
  variation-weighted scalar formulation;
  first-complementary-mode extraction;

open and transferred:
  FM-E and FM-O;
  the two d_2 tail estimates;
  a cofinal rank schedule preserving the projective limit;
  the outer arithmetic anchor and Omega7.
```

