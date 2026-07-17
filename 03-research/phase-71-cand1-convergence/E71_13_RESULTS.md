# E71.13 -- persistent-divisor product results

**Date:** 2026-07-07.
**Script:** `E71_13_persistent_product_probe.py`.

## Output

The product over persistent clusters was compared to `Xi(t)/Xi(0)` on `[0,12]`.

```text
zeta true:
#persistent=11  relL2=2.025853e-01  relSup=1.749564e-01
centers=[14.134725 21.022040 25.010858 30.424876 32.935062
         37.586178 40.918719 43.327073 48.005151 49.773832
         52.970321]

planted off-line:
#persistent=1  relL2=9.146182e-01  relSup=7.677714e-01
centers=[25.001074]
```

## Reading

The persistent divisor substantially improves over the all-root product and separates the planted
control:

```text
all-root product at N=40:       relL2 ~ 1.32
persistent product, zeta:       relL2 ~ 0.20
persistent product, planted:    relL2 ~ 0.91
```

This means persistence is not merely locating isolated roots; it is recovering a meaningful low-energy
piece of the determinant shape.

## Limitation

The persistent product is finite and only includes clusters visible under the chosen `lambda,N,hmax`.
It therefore cannot exactly reproduce `Xi/Xi(0)`.

More importantly, numerical clustering is not a proof object. The proof object must be an intrinsic
stable projection or Fredholm decomposition that produces the same divisor.

## Consequence

The next theorem target is:

```text
construct stable Riesz/Fredholm projections for the CCM m-function,
whose determinant converges locally uniformly to Xi.
```

If that theorem is proved, E71.5 closes `Omega_7`.
