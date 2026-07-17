# E72.230 - Negative edge mode

## Purpose

E72.229 suggested that HOC3 is driven by a leading negative eigenvalue of the high plus-current

```text
A_1=sum_{0.60L<log n<=L} A_n^+.
```

This probe tests simple explicit phase candidates

```text
c_u = Q_even cos(2*pi*m*u)
```

against the minimum eigenvector.

## Diagnostic

Script:

```text
E72_230_negative_edge_mode_probe.py
```

Output:

```text
E72.230 negative edge-mode probe
High block A_1. Candidate c_u=Q_even cos(2*pi*m*u) in bq coordinates.
lam minEig k50 k90 maxCoord bestU bestRayleigh eigAlign candAlign
 12 -2.226316e-01   3  13 0.347 1.00 -5.507559e-02 0.542 0.542
 16 -2.186781e-01   2   8 0.326 0.90 -1.822965e-02 0.262 0.262
 20 -2.243125e-01   2  10 0.500 0.80 -1.245514e-02 0.130 0.130
 24 -2.542393e-01   2  16 0.491 1.00 -1.179745e-02 0.179 0.179
 28 -2.409324e-01   4  25 0.391 1.00 -5.319352e-03 0.168 0.168
 32 -1.368453e-01   2   6 0.419 1.00 -4.912686e-03 0.075 0.075
```

## Reading

A single phase candidate does not capture the minimum mode uniformly. The coordinate spread is small
(`k50` is usually 2 or 3), but the correct vector is not a raw endpoint phase.

This forced the next probe: inspect the lifted Fourier profile.
