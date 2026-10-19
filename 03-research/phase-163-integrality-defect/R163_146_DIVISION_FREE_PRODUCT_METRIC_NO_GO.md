# R163_146 — The division-free Poisson product does not select contact

**Status:** direct proof of strict positivity of the product metric on physical vectors; limited NO-GO against using its vanishing as a first-contact condition. It does not rule out a finite oriented defect with collars; Row D remains open.

## Proposition

Let `F∈L²(I_T)`, `F≠0`, extended by zero to `ℝ`, and suppose the regularity `F∈H^s(ℝ)` for some `s>1/4`, which the contact eigenvectors used in `R163_127` have. With the unitary transform `F̂`, define

```
 M(F)=∫_ℝ |ζ(1/2+iτ)|² |F̂(τ)|² dτ.       (1)
```

Then `0<M(F)<∞`. Consequently, the equation `H_TF=0` **cannot** imply `M(F)=0` unless `F=0` has already been proved.

*Proof.* The classical convexity bound for ζ on the critical line is `|ζ(1/2+iτ)|≪_ε(1+|τ|)^(1/4+ε)`; choose `ε>0` with `1/2+2ε<2s`. Weighted Plancherel gives finiteness of (1). ζ's zeros on the line form a discrete, measure-zero set. So `ζ(1/2+iτ)F̂(τ)=0` almost everywhere only if `F̂=0` almost everywhere, i.e. `F=0`. This proves strict positivity. □

The same argument works with the completed function `ξ(1/2+iτ)`; there the Gamma decay makes finiteness even more direct, and the zeros remain discrete.

## Relation to R163_145's rectangle

Multiplying the two edges of the quotient `ζ(s+u)/ζ(s)` before reflecting produces, at `u=0` and `s=1/2+iτ`, the non-negative product `ζ(s)ζ(1−s)=|ζ(s)|²`. Its integral against `|F̂|²` is exactly (1). Poisson reflection gives an **equality of representations** of this metric, but at a hypothetical first-contact vector both representations have the same **positive** value. There is no zero-norm equality state eliminating the exterior.

Creating new information requires an oriented difference **before** that product, or a subtraction with the Tate/exterior terms whose value does vanish selectively when `H_TF=0` is imposed. That is the `(PC-ren)` requirement already localized in `R161_040` and `R163_139`–`145`. This memo does not claim every quadratic identity is useless: it only excludes the concrete argument "positive completed product + first contact ⇒ zero product."

## Falsifiers

(1)'s positivity also holds at a contact of a `κ` model if ζ is replaced by `Z_{a_κ}`: its exponential factor has no zeros, and the set of zeros inherited from ζ remains discrete. Epstein/DH with non-identically-zero meromorphic functions have the same local property wherever the integral is defined. So the isolated positive product does not use `R163_143`'s arithmetic distinction nor `R163_145 (3)`'s defective orientation.
