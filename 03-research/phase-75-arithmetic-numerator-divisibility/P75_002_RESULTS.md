# P75.002 results

Command:

```text
python3 P75_002_finite_numerator_probe.py
```

Result:

```text
P75.002 finite numerator package
z                  |P-D*C|        |P-P_border|    normalized Q diff
0.7                   9.537e-07      9.537e-06          0.000e+00
3.1                   0.000e+00      2.384e-07          2.776e-17
7.0                   1.192e-06      4.053e-06          8.674e-18
(2.3+0.4j)            9.830e-07      4.233e-06          2.776e-17
(-4.2+0.2j)           7.251e-07      8.055e-06          3.103e-17
worst_error 9.537e-06
```

The absolute polynomial errors are amplified by large product factors in the
barycentric numerator.  The normalized detector identity, which is the
`Q_gamma xi` object used in Phase 72-74, is at `1e-17` roundoff.

