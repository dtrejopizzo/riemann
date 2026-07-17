# E72.209 - Resonant pair energy

## Purpose

E72.208 split the fixed certificate into resonant even energy, non-resonant displacement Poincare, and
high-block odd sign. This note isolates the first exact resonant even identity at degree `2`.

For signed cells

```text
A_n^+ delta_n + A_n^- delta_{n^{-1}},
qquad A_n^-=(A_n^+)^*,
```

the resonant words of length `2` are exactly

```text
(+n,-n),       (-n,+n).
```

Therefore

```text
Res_2
= sum_n Tr(A_n^+A_n^-)+Tr(A_n^-A_n^+)
= 2 sum_n ||A_n^+||_HS^2.                       (RPE2)
```

This is positive and completely local over prime-power cells.

## Diagnostic

Script:

```text
E72_209_resonant_pair_energy_probe.py
```

Output:

```text
E72.209 resonant pair energy probe
r=2 resonant identity: Res2 = 2 sum_n ||A_n^+||_HS^2
lam block cells totalTrK2 Res2 NonRes2 ResFrac
 12     0    12 +1.282124e+00 +7.506459e-01 +5.314786e-01 0.585
 12     1    35 +4.679419e-01 +3.723544e-01 +9.558749e-02 0.796
 16     0    15 +1.041547e+00 +5.903247e-01 +4.512219e-01 0.567
 16     1    55 +4.699814e-01 +3.676131e-01 +1.023683e-01 0.782
 20     0    18 +9.216830e-01 +5.066864e-01 +4.149966e-01 0.550
 20     1    79 +4.401854e-01 +3.181675e-01 +1.220179e-01 0.723
 24     0    21 +8.496992e-01 +4.667205e-01 +3.829787e-01 0.549
 24     1   105 +4.667118e-01 +2.615648e-01 +2.051470e-01 0.560
 28     0    24 +7.338575e-01 +4.259593e-01 +3.078982e-01 0.580
 28     1   136 +4.356553e-01 +2.487475e-01 +1.869078e-01 0.571
```

## Reading

The resonant pair energy accounts for a large positive fraction of the quadratic block moment:

```text
ResFrac ~= 0.55--0.80.
```

The non-resonant quadratic part is also positive in these tests. Thus degree `2` even energy is not a
cancellation phenomenon. It is a local positive cell-energy plus positive non-resonant leakage.

## Consequence

For the even part of the certificate, the first sublemma should be a direct local bound:

```text
2 sum_{n in S_j(x)} ||A_n^+||_HS^2 <= explicit block budget.
```

Higher even resonances are more complicated because `prod n_i^eps_i=1` has non-pairing solutions, but
`(RPE2)` is the base case and the correct sign model.

This distinguishes the roles:

```text
even energy: positive local cell energy to bound,
odd high-block sign: non-resonant signed cancellation to prove.
```
