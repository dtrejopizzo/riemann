# E72.198 - Signed Green-word cancellation diagnostic

## Purpose

E72.197 proves the exact signed-word expansion. This diagnostic measures how much information is lost
by taking absolute values over signed Green-words.

For a block kernel

```text
K_j = sum_alpha A_alpha^signed,
```

compare

```text
|Tr(K_j^r)|
```

with the incoherent ceiling

```text
sum_{alpha_1,...,alpha_r}
|Tr(A_{alpha_1}^signed ... A_{alpha_r}^signed)|.
```

## Result

Script:

```text
E72_198_signed_word_cancellation_probe.py
```

Output:

```text
E72.198 signed Green-word cancellation diagnostic
reports |Tr(K^r)| versus sum of absolute signed-word traces
lam block r cells signedTrace absCeil ratio
  6     0 2    12 +1.894812e+00 2.320108e+00 1.224e+00
  6     0 3    12 +7.412135e-01 9.731124e-01 1.313e+00
  6     1 2    24 +7.233123e-01 1.584702e+00 2.191e+00
  6     1 3    24 -1.902974e-01 6.120327e-01 3.216e+00
  8     0 2    16 +1.461278e+00 2.275711e+00 1.557e+00
  8     0 3    16 +2.083292e-01 5.257407e-01 2.524e+00
  8     1 2    38 +5.957448e-01 2.005691e+00 3.367e+00
  8     1 3    38 -3.593871e-02 7.348706e-01 2.045e+01
 10     0 2    18 +1.381335e+00 1.883132e+00 1.363e+00
 10     0 3    18 +3.086448e-01 5.080193e-01 1.646e+00
 10     1 2    52 +6.282831e-01 2.061908e+00 3.282e+00
 10     1 3    52 -1.300025e-01 6.953147e-01 5.348e+00
```

## Reading

The low block has modest cancellation at these low degrees. The high block already shows stronger
signed cancellation, especially in odd moments.

This confirms the proof constraint:

```text
Do not prove the fixed certificate by summing absolute signed Green-words.
```

The remaining theorem has to preserve the signed Green-word structure through the trace. A viable
estimate should group words by their total signed translation, their endpoint overlap, or another
phase-sensitive invariant before applying inequalities.

## Next target

The natural next invariant is the signed displacement

```text
Delta(eps,n)=sum_i eps_i log n_i.
```

Words with `Delta=0` are multiplicative resonances. Words with `Delta != 0` carry oscillatory
translation phase. The next proof attempt should decompose the Green-word sums by `Delta` and prove:

```text
resonant words give the main positive energy,
non-resonant signed words cancel after the Green insertions,
the mixed block XNEG sign comes from the imbalance of these two classes.
```

This is still arithmetic, but it is sharper than the old prime-cell ceiling.
