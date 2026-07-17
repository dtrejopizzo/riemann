# P76.061 - Bordered ambient-norm autopsy

For the prolate residual direction, the full bordered evaluation bound is
catastrophic:

```text
N    ambient bound      actual safe error      overestimate
6      1.54e16              0.163               9.46e16
8      8.14e19              0.104               7.81e20
10     1.36e24              0.081               1.68e25
12     1.92e27              0.066               2.92e28
```

Even the amplification measured only on the actual residual direction grows
from about `30` to `8.5e3`.  Therefore `SAFE-PROLATE-BRIDGE` cannot follow
from an operator norm for the bordered inverse.  The decay and signed
structure of the exact source `M k_lambda` must be used before inversion.

This is the safe-axis analogue of the inverse-gap wall, now stated without
an irrelevant eigenvector norm.
