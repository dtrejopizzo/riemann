# E72.57 -- Lambda weighting correction for endpoint probes

**Date:** 2026-07-08.
**Role:** correct a normalization ambiguity in the endpoint-channel probes.

## 0. The issue

The true scalar WRL prime contribution is:

```text
sum_{n<=x} Lambda(n) (n/x)^z <v_{x,s},T_{x,n}k_x>.
```

Some endpoint probes measured the support-restricted unweighted sum:

```text
sum_{n<=x, Lambda(n)!=0} (n/x)^z <v_{x,s},T_{x,n}k_x>,
```

while earlier diagnostics also reported the `Lambda`-weighted values.

The mathematically relevant object is the `Lambda`-weighted one.

## 1. Effect on the signal

E72.37 already recorded both unweighted and `Lambda`-weighted normalized values. The `Lambda`-weighted
values were larger but still small in the tested finite windows, for example:

```text
lambda=8, x=64:
  r=2.7080   |norm|=5.69e-3, |normLambda|=1.82e-2
  r=5.9877   |norm|=1.92e-3, |normLambda|=6.58e-3
  r=9.5183   |norm|=8.49e-4, |normLambda|=3.09e-3

lambda=12, x=144:
  r=3.375    |norm|=1.58e-3, |normLambda| comparable-scale expected
  r=8.025    |norm|=2.97e-4
```

So the positive signal survives qualitatively, but every theorem must carry `Lambda`.

## 2. Correct endpoint operator

From now on, the endpoint operator for scalar WRL is:

```text
S_x^Lambda(z)
 := sum_{n<=x} Lambda(n)(n/x)^z T_{x,n}.
```

The model/discrepancy split is:

```text
S_x^Lambda(z)
 = S_x^{cont}(z) + S_x^{disc-err}(z),
```

where `S_x^{cont}` is the PNT main term and `S_x^{disc-err}` is the Chebyshev-discrepancy term.

## 3. Documents affected

The following statements should be read with `S_x(z)=S_x^Lambda(z)` when they refer to scalar WRL:

```text
E72.41  Weighted channel refinement,
E72.42  Endpoint operator probe,
E72.43  Endpoint coborder lemma,
E72.44  Adjoint Green pairing,
E72.50  Half-power WCB probe,
E72.55  Loewner cancellation probe,
E72.56  Endpoint rank-one expansion.
```

Unweighted probes remain useful only as structural diagnostics of the cell support.

## 4. Correct target

The current target is:

```text
sqrt(x)
|<v_{x,s}, S_x^Lambda(z) k_x>| -> 0
```

or a version with the PNT exponential factor, after subtracting the continuous model main term.

## 5. Status

```text
corrected: scalar WRL endpoint channel must be Lambda-weighted;
open: rerun/prove the half-power and rank-one suppression estimates in the Lambda-weighted channel.
```
