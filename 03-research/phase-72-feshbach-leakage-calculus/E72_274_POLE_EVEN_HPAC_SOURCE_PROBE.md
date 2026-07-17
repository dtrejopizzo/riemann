# E72.274 -- Pole-even HPAC source probe

**Purpose.** Rebuild the HPAC source after the pole-even repair of E72.261--E72.273.

The old E72.79 source used the invalid even-line removal

```text
Q = I-kk^*,             h = k-xi.
```

That source cannot be recycled after the corrected geometry.  The corrected complement is instead

```text
e_pole  = lambda_0(H_model)                         # odd pole energy
B_even  = full even Fourier basis
C_E     = B_even^T(H_actual-e_pole I)B_even.
```

This probe tests the first pole-even HPAC source that is intrinsic to the finite divisor vector:

```text
b_tau = B_even^T A_x(tau) xi_x,
```

where `A_x(tau)` is the same HPAC matrix used in the earlier finite-root probes.  This uses neither
the accidental old projection nor the displacement vector `k-xi`.

## Endpoint identity

For a Cauchy test vector

```text
a_s = B_even^T (s/(s^2-d^2)),
```

the corrected endpoint scalar is

```text
F_x(s,tau) = <a_s,C_E^{-1}b_tau>.
```

By E72.273 it is exactly the bordered minor

```text
F_x(s,tau)
= - det [[C_E,b_tau],[a_s^*,0]] / det(C_E).
```

The script verifies this identity numerically for the corrected source.

## Probe

Run:

```text
python3 E72_274_pole_even_hpac_source_probe.py
```

Output:

```text
E72.274 pole-even HPAC source probe
Uses source b_tau=B_even^T A_x(tau) xi_x; no Q=I-kk* and no old h=k-xi.
lam L roots max|F| values minorRel
 16 5.545177     4 1.883342e-02 [1.535e-02 1.594e-02 1.703e-02 1.883e-02] 6.822e-15
 20 5.991465     4 1.779402e-02 [1.530e-02 1.567e-02 1.639e-02 1.779e-02] 1.084e-14
 24 6.356108     4 8.248877e-03 [5.585e-03 6.295e-03 6.655e-03 8.249e-03] 1.259e-14
```

## Reading

This is a positive repair, not a closure.

Positive:

```text
1. The corrected pole-even HPAC source is well-defined without the old invalid line removal.
2. The bordered-minor endpoint identity survives at roundoff for this source.
3. The tested scalar size is small and does not grow from lambda=16 to lambda=24.
```

Still open:

```text
1. Prove that b_tau=B_even^T A_x(tau)xi_x is the exact load-bearing HPAC source for scalar WRL.
2. Prove the finite-root decay uniformly, rather than measuring the first four roots.
3. Convert the bordered minor into the Mellin spectral divisibility statement needed for WRL.
```

Thus E72.274 repairs the endpoint source and restores a non-tautological object for the scalar WRL
channel.  The remaining theorem is a pole-even HPAC source theorem plus its divisibility/decay
consequence.
