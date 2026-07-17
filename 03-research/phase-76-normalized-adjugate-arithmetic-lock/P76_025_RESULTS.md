# P76.025 - Cofinal normality and safe-region audit

The full, non-evenized boundary characteristic was evaluated with rebuilt
multiprecision CCM entries at `lambda=4,6,8,10`, using cutoffs whose pole
horizon covers `[-18,18]`.

```text
lambda  N   N/L     max|Phi|   max safe error   odd defect
4       12  4.328    1.0295      0.0494          0.0648
6       15  4.186    1.0362      0.0596          0.0714
8       16  3.847    1.0423      0.0727          0.0808
10      18  3.909    1.0454      0.0755          0.0783
```

The sampled compact remains bounded, but the Euler-safe error does not
decrease.  Therefore this particular near-constant `N/L` path is not a
certified identification path.  It also fails the necessary global horizon
condition `N(L)/L -> infinity` isolated in P76.026.

This is a path falsification, not a falsification of the canonical boundary
characteristic.  Future scaling probes must increase `N/L` and must test the
full characteristic; the earlier P76.022 data primarily tested its even
part at fixed `lambda`.
