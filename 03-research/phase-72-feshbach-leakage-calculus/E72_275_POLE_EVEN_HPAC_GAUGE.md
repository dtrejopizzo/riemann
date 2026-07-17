# E72.275 -- Pole-even HPAC gauge

**Purpose.** Remove the constant HPAC term in the corrected pole-even geometry without returning to the
invalid old projection.

E72.274 tested the repaired source

```text
b_tau = B_even^T A_x(tau)xi_x.
```

The probe is well-defined, but it exposes a structural issue: at finite Weyl roots the source is
dominated by the constant `2I` term of the HPAC matrix, not by the resonant two-resolvent part.

## Exact finite-root simplification

From E72.71,

```text
A_x(tau)
 = 2I
   + i alpha(tau)[(tau I+D)^(-1)+(tau I-D)^(-1)]
   - alpha(tau)(E_tau-1)/L
       [r_+(tau)r_+(tau)^T+r_-(tau)r_-(tau)^T],
```

where `alpha(tau)=1/2+i tau` and

```text
S_tau=(tau I+D)^(-1)+(tau I-D)^(-1)=2tau(tau^2I-D^2)^(-1).
```

At a finite Weyl root,

```text
<r_-(tau_j),xi_x>=0.
```

Since `xi_x` is even,

```text
<r_+(tau_j),xi_x>=<r_-(tau_j),xi_x>=0.
```

Therefore the rank-one boundary term vanishes and

```text
A_x(tau_j)xi_x = 2xi_x+i alpha(tau_j)S_tau_j xi_x.              (HPAC-root)
```

This is an exact identity.  It is the corrected replacement for the old claim that the `2I` term drops
because of `Q=I-kk^*`.

## Correct gauge

Let

```text
a_s = B_even^T s(s^2-D^2)^(-1)1.
```

The constant source contributes

```text
2<a_s,C_E^(-1)xi_x>.
```

It is not part of the resonant HPAC channel.  The pole-even way to remove it is the left gauge

```text
a_s^perp = a_s - xi_x <xi_x,a_s>/<xi_x,xi_x>,
```

computed in the full even basis.  Then

```text
<a_s^perp,C_E^(-1)2xi_x>=0,
```

because `xi_x` is an eigenvector of the actual even compression and hence `C_E^(-1)xi_x` is a scalar
multiple of `xi_x`.

Thus the corrected resonant source is

```text
b_tau^res = i alpha(tau) B_even^T S_tau xi_x,
```

paired against the left-gauged Cauchy vector.

## Probe

Run:

```text
python3 E72_275_pole_even_hpac_gauge_probe.py
```

Output:

```text
E72.275 pole-even HPAC gauge probe
At finite roots: A(tau)xi = 2xi + i(1/2+i tau)S_tau xi.
The left gauge a_perp=a-xi<xi,a> kills the constant 2xi without using old Q=I-kk*.
lam L roots |<xi,a>| maxSimpl maxFull maxLeftPerp maxResOnly
 16 5.545177     4 9.431750e-02 4.851e-12 1.883342e-02 3.195818e-03 3.535162e-03
 20 5.991465     4 1.216693e-01 8.190e-12 1.779402e-02 2.137288e-03 2.556129e-03
 24 6.356108     4 4.775298e-02 3.102e-12 8.248877e-03 3.244693e-03 3.389981e-03
```

## Reading

This is the corrected HPAC gate:

```text
finite-root HPAC source
  = harmless constant actual-ground source
    + resonant source i alpha S_tau xi_x.
```

The harmless constant must be removed by the **left actual-ground gauge**, not by the old removed-line
projection.  After this gauge, the measured residual is on the scale of the true resonant source.

The remaining theorem is now sharper:

```text
max_{P_x(tau_j)=0}
|<a_s^perp,C_E^(-1)i alpha(tau_j)S_tau_j xi_x>| -> 0
```

uniformly in the required Cauchy windows, with the corresponding bordered-minor/divisibility form.
