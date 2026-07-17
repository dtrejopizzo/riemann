# E73.286 - Weight derivative bridge audit

Date: 2026-07-14.

## 1. Purpose

E73.285 showed that `BLOCK-FREQ-DIV` is a cancellation between:

```text
sum c_omega W'_omega
```

and

```text
sum l_omega V'_omega.
```

The natural analytic idea is:

```text
y e^(i omega y)=(1/i) partial_omega e^(i omega y),
```

so perhaps

```text
V_omega=(1/i)partial_omega W_omega
```

turns the `l`-block into a frequency integration-by-parts correction to the
`c`-block.

E73.286 tests the discrete version of that idea on the actual mesh frequencies
`omega=d_n`.

## 2. Test

Build `W,V` as in E73.285.  Approximate:

```text
partial_omega W
```

by central finite differences on the uniform frequency mesh.  Then compare:

```text
V_omega  versus  (1/i)D_omega W_omega.
```

Also form the discrete adjoint correction:

```text
c_eff = c+(1/i)D_omega^*l,
```

so that, if the discrete bridge were valid,

```text
sum cW + sum lV approx sum c_eff W.
```

## 3. Result

The discrete bridge fails.

The finite-difference derivative error is order one:

```text
dErrB about 0.02--0.06
```

meaning `||V-(1/i)D W||/||V||` is not small.  The integration-by-parts
replacement gives pairings of ordinary size:

```text
ibpB around L^(-3) to L^(0),
```

while the actual block cancellation is around:

```text
pairB around L^(-18) to L^(-21).
```

Thus the sharp cancellation cannot be recovered by discrete frequency
summation by parts on the mesh.

## 4. Meaning

The formal continuous identity

```text
V_omega=(1/i)partial_omega W_omega
```

may still be true for a continuous closed formula `W(omega)`, but it is not
usable through coarse finite differences at the mesh frequencies.  The
Gamma-prime weights vary too sharply, and endpoint/prime sampling effects are
not captured by the naive discrete derivative.

Therefore `BLOCK-FREQ-DIV` needs exact closed formulas for `W_omega,V_omega`,
not a finite-difference bridge.

## 5. Corrected next target

The next theorem must derive closed formulas:

```text
W_omega = W^A_omega-W^P_omega,
V_omega = V^A_omega-V^P_omega,
```

where:

```text
W^P_omega = sum_{p^k<=e^L}(log p)p^(-k/2)e^(i omega klog p),
V^P_omega = sum_{p^k<=e^L}(log p)p^(-k/2)(klog p)e^(i omega klog p),
```

and the archimedean parts are written by explicit elementary/digamma-series
integrals.

Then prove `BLOCK-FREQ-DIV` from the exact formulas, not from numerical
derivatives.

## 6. Status

```text
tested: discrete derivative bridge V approx (1/i)D W;
rejected: mesh integration-by-parts explanation of c/l cancellation;
open: derive exact closed W,V formulas and prove BLOCK-FREQ-DIV directly.
```
