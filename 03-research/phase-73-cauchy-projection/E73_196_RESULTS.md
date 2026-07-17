# E73.196 results - WR tail certification for finite-frequency endpoint

Command:

```text
python3 E73_196_wr_tail_certified_ff_probe.py
```

Output:

```text
E73.196 WR tail certified finite-frequency
Compares accelerated order-2 WR tail with grouped derivative bound.
 lam     L gamma row    R tailB boundB ratioB M3B
  12   4.970   14.13   0   400  -18.70   -6.91   11.79    6.71
  12   4.970   14.13   0  1000  -17.50   -8.62    8.87    6.71
  12   4.970   14.13   0  2500  -17.45  -10.34    7.12    6.71
  16   5.545   14.13   0   400  -17.83   -5.32   12.50    7.43
  16   5.545   14.13   0  1000  -16.42   -6.93    9.50    7.43
  16   5.545   14.13   0  2500  -16.38   -8.53    7.85    7.43
```

Reading:

```text
The grouped derivative bound is rigorous and dominates the accelerated WR
tail, but it is far too conservative at the final residual scale.
```

The gap is about:

```text
7 to 12 powers of L.
```

Conclusion:

```text
The finite-frequency certificate cannot be closed by the existing absolute
local WR tail bound alone.
```

The next necessary refinement is a signed closed tail:

```text
WR-tail per frequency =
sum_{r>=R} [
  c_omega int_0^L e^{(-2r-1/2+iomega)y}dy
 +l_omega int_0^L y e^{(-2r-1/2+iomega)y}dy
 -B(0) int_0^L e^{-(2r+1)y}dy
]
```

evaluated by special functions or interval arithmetic without taking absolute
values frequency-by-frequency.
