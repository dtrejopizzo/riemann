# P76.060 - Prolate rectangular residual

At `lambda=6`, after matching boundary and prolate vectors at `z_0=i`:

```text
N    ||M k||/||k||    ||M e||/||e||    max safe error
6       1.00e-3          2.50e-3           0.1630
10      3.90e-5          1.40e-4           0.0806
12      1.58e-6          6.68e-6           0.0657
15      5.39e-7          2.83e-6           0.0500
```

The prolate candidate is an increasingly accurate null vector of the exact
rectangular CCM block, and its boundary-normalized Cauchy error decreases
without division by the ground gap.

The theorem target becomes a bordered directional stability estimate for
the source `M k`, rather than an ambient eigenvector perturbation bound.
