# P76.064 - Fourier-tail cancellation results

Reinserting all Fourier columns through `|j|<=18` changes the prolate
rectangular residual norms as follows:

```text
row window N    one-sided finite residual    extended residual
8                    8.10e-6                    2.70e-11
10                   2.91e-6                    3.15e-11
12                   1.18e-7                    3.67e-11
15                   4.03e-8                    4.80e-11
```

For fixed rows `N=8`, cumulative symmetric Fourier cutoffs give an
oscillatory but rapidly decreasing envelope:

```text
J=8:  4.89e-6
J=11: 8.51e-8
J=14: 5.37e-10
J=17: 1.69e-11.
```

Thus the finite residual is overwhelmingly an omitted-Fourier-column tail,
not an interior defect of the prolate model.  The oscillation forbids a
monotone tail argument; signed Fourier summation or repeated Abel summation
is required.
