# E86.002 - Autopsy of the crude cumulative ceiling

## 1. Test

For the exact `L=2 log 6` multiprecision sections, compare each parity response
with the right side of E86.001, equation (3.1).  The cluster contains the
nearest `r` eigenlines of each parity and the safe point is `z=i`.

```text
outer  r   E actual    E ceiling   O actual    O ceiling
6      1   2.68e-8     4.63e-3     1.31e-1     3.64e6
6      2   9.74e-10    1.08e-6     1.10e-3     1.20e2
6      3   1.60e-10    4.55e-9     2.40e-5     2.24e-2
6      4   4.98e-10    4.98e-10    5.74e-6     3.38e-4

8      1   4.33e-6     2.58e2      6.07e1      2.76e11
8      2   7.64e-6     6.56         2.34         1.32e8
8      3   3.40e-7     3.19e-3     5.27e-2     3.61e4
8      4   3.98e-9     5.96e-7     6.93e-4     4.85.                 (1.1)
```

## 2. Decision

The even-complement channel can be smaller than its crude ceiling by many
orders of magnitude.  The cumulative maximum occurs where the monotone
variation weight is not carrying the final scalar, so replacing every
`B_j` by `max|B_j|` destroys the effective return.

```text
CRUDE-CEILING:
valid inequality, rejected as the load-bearing asymptotic mechanism.   (2.1)
```

The finite table does not prove asymptotic decay.  It proves that the global
ceiling is badly mis-scaled relative to the exact scalar on the audited
sections.

## 3. Surviving information

The exact Abel identity itself remains useful because it pairs each cumulative
sum with the local variation

```text
d_j-d_{j+1}.                                          (3.1)
```

The next criterion must retain that pairing rather than dominate it by the
largest cumulative excursion.

## 4. Status

```text
refuted as proof mechanism:
  the crude global cumulative ceiling;

retained:
  the variation-weighted Abel identity.
```

