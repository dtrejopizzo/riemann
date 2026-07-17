# E73.029 results - high precision multiplicity growth

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_029_confluent_high_precision_probe.py
```

Output:

```text
E73.029 high precision confluent multiplicity probe
 sigma      t   delta    m        normH        log10(normH)
  0.20   50.0    3.00    4 12.5293259482         1.097928
  0.20   50.0    3.00    8 19.8590601116         1.297959
  0.20   50.0    3.00   12 20.2158446371         1.305692
  0.20   50.0    3.00   16 20.2197229689         1.305775
  0.20   50.0    3.00   20 20.2197383677         1.305776
  0.20   50.0    3.00   24 20.219738397          1.305776
  0.20   50.0    3.00   28 20.219738397          1.305776
  0.20   50.0    0.50    4 1.7090131866          0.232745
  0.20   50.0    0.50    8 1.71346271124         0.233875
  0.20   50.0    0.50   12 1.71346302029         0.233875
  0.20   50.0    0.50   16 1.71346302029         0.233875
  0.20   50.0    0.50   20 1.71346302029         0.233875
  0.20   50.0    0.50   24 1.71346302029         0.233875
  0.20   50.0    0.50   28 1.71346302029         0.233875
  0.05   50.0    0.50    4 1.64945404996         0.217340
  0.05   50.0    0.50    8 1.65283776507         0.218230
  0.05   50.0    0.50   12 1.65283795149         0.218230
  0.05   50.0    0.50   16 1.65283795149         0.218230
  0.05   50.0    0.50   20 1.65283795149         0.218230
  0.05   50.0    0.50   24 1.65283795149         0.218230
  0.05   50.0    0.50   28 1.65283795149         0.218230
```

Conclusion:

```text
Hermite-normalized confluent projection norms stabilize with multiplicity in the tested cases.
```

The explosive values from E73.028 were numerical artifacts of ill-conditioned double-precision
solves.
