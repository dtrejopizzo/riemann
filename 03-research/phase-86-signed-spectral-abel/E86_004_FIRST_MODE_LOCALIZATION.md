# E86.004 - First complementary mode localization

## 1. Exact localization lemma

Use the notation of E86.001 and E86.003.  Since

```text
B_1=b_1,                                              (1.1)
```

the variation-weighted return can be split at its first atom.

### Theorem 1.1

One has

```text
sum_{j=1}^m b_jd_j=d_1b_1+R_1,                       (1.2)
```

with

```text
|R_1|
 <=d_2 max_{2<=j<=m}|B_j-B_1|.                        (1.3)
```

### Proof

From E86.003,

```text
sum_j b_jd_j=d_1 sum_j pi_j B_j.                      (1.4)
```

Subtract `d_1B_1` and use

```text
sum_{j=2}^m pi_j=d_2/d_1.                             (1.5)
```

The triangle inequality then gives (1.3). `QED`

The theorem takes absolute values only after the exact first-mode extraction.
It does not sum individual complementary contributions.

## 2. Two-clause sufficient criterion

For either parity channel, the response tends to zero if

```text
coefficient_N d_{1,N} b_{1,N}(z)->0,                  (2.1)

|coefficient_N| d_{2,N}
 max_{j>=2}|B_{j,N}(z)-B_{1,N}(z)|->0,                (2.2)
```

locally uniformly on safe compact sets, with the analogous derivative
conditions.

Clause (2.1) is the first complementary resonance.  Clause (2.2) is a
strictly smaller tail once `d_2/d_1` collapses.

## 3. Finite anatomy

For the same exact sections used in E86.002, the ratios are

```text
outer  r   d_2^E/d_1^E   d_2^O/d_1^O
6      1   1.84e-9       4.76e-10
6      2   9.19e-8       7.92e-9
6      3   1.01e-5       4.27e-6
6      4   terminal       9.79e-7

8      1   7.43e-8       6.57e-9
8      2   3.95e-8       7.38e-8
8      3   5.11e-8       2.64e-8
8      4   4.40e-7       1.24e-7.                    (3.1)
```

The weighted cumulative profiles have constant sign on these rows.  Their
small return-to-ceiling ratios are therefore support-localization effects,
not sign cancellation.  In particular, the first mode accounts for the
observed response to the displayed precision scale.

## 4. Explicit first-mode factors

Let `q_1^O` be the first odd complementary eigenvector and `q_1^E` the first
even one.  The leading clauses are

```text
FM-E:
alpha d_1^E ell_z(q_1^O)(s^Tq_1^O)->0,                (4.1)

FM-O:
beta d_1^O ell_z(q_1^E)(1^Tq_1^E)->0.                 (4.2)
```

The associated tail clauses are exactly (2.2).  All factors in (4.1)--(4.2)
are finite CCM data; no zero location or complement inverse occurs.

## 5. Status

```text
proved:
  exact first-mode plus tail decomposition;
  tail bound weighted by d_2 rather than d_1;

localized:
  signed parity WRL to FM-E, FM-O and their two d_2 tails;

open:
  cofinal rate estimates for those four scalar clauses.
```

