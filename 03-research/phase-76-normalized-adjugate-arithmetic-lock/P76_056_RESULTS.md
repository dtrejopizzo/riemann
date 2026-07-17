# P76.056 - Shell moment falsifiers

At outer cutoff `9`:

```text
case       |1^T w|/||w||    ||B w||/||w||    |theta(2i)|
zeta          2.65e-12          7.43e-19        1.48e-2
planted       9.18e-10          9.39e-12        8.73e-3
random        1.25              3.01e-1         2.38
```

The shell mechanism rejects an unstructured random matrix but is shared by
the planted Loewner model.  Therefore it is a finite-section stability
mechanism, not the arithmetic identification theorem.  This cleanly
separates the program:

```text
shell Cauchy/moments: establish convergence as N -> infinity at fixed L;
safe-log limit in L: distinguish zeta from planted arithmetic.
```
