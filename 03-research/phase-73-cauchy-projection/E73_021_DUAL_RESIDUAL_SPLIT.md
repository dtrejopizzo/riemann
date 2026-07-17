# E73.021 - Dual residual split

## 1. Problem

After E73.020 the source gate is:

```text
S_b = M_LY_b + R_b,
e^(Re b L)|<xi,R_b>| <= L^B,
```

where

```text
M_L=C_E-mu I.
```

The residual may be non-small in norm.  Therefore the proof must identify the part of the residual
seen by `xi`.

## 2. Orthogonal split

Let

```text
I_L=Image(M_LP_{O,K}),
P_I=orthogonal projection onto I_L.
```

For the best image approximation:

```text
R_b=P_I^perp S_b.
```

Split

```text
R_b = <xi,R_b>xi + R_b^perp,
```

with

```text
<xi,R_b^perp>=0.
```

Only the scalar coefficient `<xi,R_b>` is load-bearing.

## 3. What E73.021 shows

The residual norm can be visible:

```text
||R_b||/||S_b|| = 1e-6..3.2e-4.
```

But its share in the `xi` direction is tiny:

```text
||<xi,R_b>xi||/||R_b|| = 1e-7..1e-5.
```

Hence the finite data support:

```text
P_I^perp S_b = high-cokernel component + xi-small scalar.
```

This is exactly the geometry scalar WRL needs.

## 4. New theorem form

The sharpened theorem is:

```text
DUAL-XI:
For all natural-height off-line nodes b,

P_I^perp S_b = Z_b + E_b,

where <xi,Z_b>=0 and

e^(Re b L)|<xi,E_b>| <= L^B.
```

Equivalently:

```text
e^(Re b L)|<xi,P_I^perp S_b>| <= L^B.
```

Since `xi` is orthogonal to `I_L`, this is also:

```text
e^(Re b L)|<xi,S_b>| <= L^B.
```

The advantage of the split is structural: `Z_b` may be large, but it is harmless.

## 5. Analytic interpretation

The large cokernel directions arise because `P_{O,K}` is a deliberately small rational primitive
space.  They are not obstructions unless they overlap the ground eigenline.

Therefore the proof should not try to enlarge `P_{O,K}` until the residual norm disappears.  That
would recreate a full-space operator estimate.  The correct proof must show that the finite rational
residual is orthogonal, or nearly orthogonal after Phase 72 tails, to the ground eigenline.

## 6. Next finite identity

By E73.018, `S_b` and `P_{O,K}` are rational Cauchy modules on the pole mesh.  The next identity is:

```text
Rational dual identity:
<xi,S_b> = Phase72Residual_b.
```

where the right side is built from the parity-cancelled finite Fourier tail, zero-node absorbed
tail, and outside-natural-height second-variation tail.

This is now a scalar identity, not a vector-norm estimate.
