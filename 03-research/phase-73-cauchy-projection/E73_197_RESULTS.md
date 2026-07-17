# E73.197 results - signed WR tail form

Command:

```text
python3 E73_197_signed_wr_tail_probe.py
```

Output:

```text
E73.197 signed WR tail grouped form
Checks grouped frequency tail against direct integrate_modes tail.
 lam     L gamma row    R directB groupB errB
  12   4.970   14.13   0   400  -15.06  -15.06  -21.49
  12   4.970   14.13   0  1000  -15.65  -15.65  -21.99
  12   4.970   14.13   0  2500  -16.31  -16.31  -21.73
  16   5.545   14.13   0   400  -14.73  -14.73  -19.66
  16   5.545   14.13   0  1000  -14.86  -14.86  -19.67
  16   5.545   14.13   0  2500  -15.37  -15.37  -19.94
```

Reading:

```text
The signed grouped-frequency formula matches the direct WR tail to about
L^-20--L^-22 in the tested rows.
```

Conclusion:

```text
The algebra of the signed tail is correct.
```

The remaining implementation step is:

```text
replace the long signed sums by interval evaluations of
S_1(R,omega)-S_0(R) and S_2(R,omega).
```

That is the correct path toward a rigorous finite-frequency certificate.
