# E73.159 - Endpoint symmetric image audit

Date: 2026-07-12.

## 1. Purpose

E73.011 suggested that the structured image is generated mainly by endpoint
critical divided differences.  E73.159 tests a more canonical basis:

```text
endpoint critical DD kernels
times a symmetric off-node denominator product.
```

The goal was to see whether a smaller symbolic image family could replace
the large redundant `RAT-DD` dictionary.

## 2. Result

The endpoint-symmetric bases do reduce the ambient residual norm compared
with a pure polynomial endpoint basis.  But the scalar residual

```text
<xi_L,S_b>
```

does not change with the image basis.

This is not a bug.  It is exact:

```text
Image(E_L P_L) subset xi_L^perp.
```

Therefore for every structured image projection,

```text
<xi_L,S_b-P_Image S_b>=<xi_L,S_b>.
```

Changing the basis can make the cokernel residual small in norm, but it
cannot change the scalar obstruction.

## 3. Consequence

Endpoint-symmetric image reduction is useful only as a symbolic discovery
tool:

```text
find a small finite family whose E_L-image contains the non-scalar part of S_b.
```

It is not a proof of `Strong-CC-PROJ`.  The proof still has to bound

```text
<xi_L,S_b>
```

directly, or identify an explicit residual formula for the scalar part.

## 4. Updated interpretation

The correct statement is:

```text
S_b = E_L Y_b + R_b,
<xi_L,S_b>=<xi_L,R_b>.
```

The image part explains why the source has a large harmless component.  The
load-bearing theorem is a formula for `R_b` whose scalar pairing is bounded.

Thus the next symbolic target is not:

```text
find a smaller image basis.
```

It is:

```text
derive the explicit scalar residual left after projecting S_b through the
endpoint-critical image family.
```

That scalar residual should be expressible in endpoint/high-frequency
terms already controlled by Phase 72, or else it is the final obstruction.
