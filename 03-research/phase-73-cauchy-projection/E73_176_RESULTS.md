# E73.176 results - quotient packet linearity

Date: 2026-07-14.

Script:

```text
E73_176_quotient_packet_linearity_probe.py
```

## Output

```text
E73.176 quotient packet linearity
Checks B_r(y)=sum_j conj(q_rj) B_{z_j}(y), z_j=i gamma_j.
 lam     L imageRel form rowRel pktRel b0B
   8   4.159  4.0e-06    0 1.4e-16 3.2e-16 -13.75
   8   4.159  4.0e-06    1 9.8e-17 2.9e-16 -13.59
   8   4.159  4.0e-06    2 1.2e-16 3.8e-16 -13.45
  10   4.605  1.9e-07    0 9.4e-17 3.4e-16 -14.93
  10   4.605  1.9e-07    1 2.8e-16 3.3e-16 -13.99
  10   4.605  1.9e-07    2 9.3e-17 2.6e-16 -13.41
  12   4.970  1.8e-06    0 1.7e-16 3.1e-16 -14.34
  12   4.970  1.8e-06    1 9.7e-17 3.9e-16 -12.38
  12   4.970  1.8e-06    2 1.4e-16 3.5e-16 -12.67
  14   5.278  9.5e-06    0 1.1e-16 4.0e-16 -11.86
  14   5.278  9.5e-06    1 7.2e-17 5.2e-16 -10.87
  14   5.278  9.5e-06    2 1.8e-16 5.8e-16 -10.62
  16   5.545  1.8e-04    0 1.2e-16 5.0e-16 -12.53
  16   5.545  1.8e-04    1 1.4e-16 5.1e-16 -11.51
  16   5.545  1.8e-04    2 5.2e-17 6.2e-16 -10.35
```

## Reading

Both levels match at roundoff:

```text
rowRel ~= 1e-16,
pktRel ~= 1e-16.
```

Thus the quotient packets are exactly the linear combinations of Phase 72
transformed packets at the five critical nodes.

## Endpoint

The current theorem is:

```text
QTPW:
the quotient linear combination of the five critical-node transformed packet
equations forces B_{r,L}(0)=O(L^B e^(-alpha L)).
```

This is stronger than Phase 72 `PW-Cauchy`, because it asks for quotient
annihilation rather than polynomial growth of each critical value separately.
