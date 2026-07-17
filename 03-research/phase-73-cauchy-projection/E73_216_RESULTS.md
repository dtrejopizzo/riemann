# E73.216 results - sector constant budget

Command:

```text
python3 E73_216_sector_constant_budget.py
```

Output:

```text
E73.216 sector constant budget
Maximum Bernoulli sector constant C_sec allowed by BALL-ENTRY-CERT.
 lam     L    N  dim    K      Cmax       log10C worst
   8   4.159    6   13   12   10781942.0       7.03 (0, 0)
   8   4.159    6   13   16 1.4241932e+17      17.15 (0, 0)
   8   4.159    6   13   20 2.4115311e+26      26.38 (0, 0)
   8   4.159    6   13   24 7.9870598e+34      34.90 (0, 0)
  10   4.605    8   17   12   25986606.0       7.41 (0, 0)
  10   4.605    8   17   16 3.4346664e+17      17.54 (0, 0)
  10   4.605    8   17   20 5.8193476e+26      26.76 (0, 0)
  10   4.605    8   17   24 1.9285757e+35      35.29 (0, 0)
  12   4.970   10   21   12   60081781.0       7.78 (0, 0)
  12   4.970   10   21   16 7.9443487e+17      17.90 (0, 0)
  12   4.970   10   21   20 1.3465751e+27      27.13 (0, 0)
  12   4.970   10   21   24 4.4645478e+35      35.65 (0, 0)
```


Reading:

```text
K=12 already tolerates C_sec around 10^7, but K=16 tolerates C_sec around
10^17 in all tested windows.  Therefore the proof-facing BALL-ENTRY-CERT
should use K=16, not because K=12 fails, but because K=16 makes the sectorial
constant in the Bernoulli remainder lemma irrelevant for any reasonable formal
normalization.
```
