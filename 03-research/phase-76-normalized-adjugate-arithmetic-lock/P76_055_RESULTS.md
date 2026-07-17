# P76.055 - Shell generator moment results

For the canonical shell response `w` at `lambda=6`,

```text
N    |1^T w|/||w||     |s^T w|/(||s||||w||)    ||B w||/||w||
5      4.61e-9               8.13e-8              1.11e-15
6      7.88e-10              5.81e-9              7.12e-17
7      4.28e-11              3.26e-10             2.65e-18
8      2.65e-12              1.45e-11             7.43e-19
```

The `N^-2` shell Cauchy gain is therefore not geometric localization.  The
selected response is an approximate null vector with simultaneous
annihilation of the two displacement-generator moments `1` and `s`.

This is precisely the structure needed by the rectangular rank-two
commutator: after commuting one mesh multiplier through the CCM block, the
only global source terms are proportional to these two moments.
