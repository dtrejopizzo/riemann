# E72.290 -- APCB band split

**Purpose.** Turn the band-exclusion diagnostic of E72.289 into a proof-facing block inequality.

Let

```text
Delta = Delta_arith
```

on the corrected even sector, and split the mesh-frequency space by a cutoff `D0`:

```text
E_low  = span{|d_n|<D0},
E_high = E_low^perp.
```

In block form,

```text
Delta = [[A,B],[B^*,D]].
```

Then

```text
lambda_max(Delta)_+
<= lambda_max(A)_+ + lambda_max(D)_+ + ||B||.              (BAND)
```

Thus APCB follows from:

```text
low positive ceiling:    lambda_max(A)_+ = O(L^2),
high positive ceiling:   lambda_max(D)_+ = O(L^2),
cross ceiling:           ||B|| = O(L^2).
```

This is tautological as an inequality, but useful because E72.289 shows the top positive mode belongs
almost entirely to the high band, while the full-line DSF obstruction is low-frequency.

## Probe

Run:

```text
python3 E72_290_apcb_band_split_probe.py
```

Output:

```text
E72.290 APCB band-split probe
Delta_arith split by mesh-frequency cut |d|<cut in the corrected even sector.
lam cut L rankLow rankHigh total+/L2 low+/L2 high+/L2 cross/L2
 16   2 5.545177       2       39 1.617975e-01 6.418911e-02 1.615172e-01 6.032589e-02
 24   2 6.356108       3       54 1.428683e-01 5.598715e-02 1.428407e-01 4.128077e-02
 32   2 6.931472       3       70 1.327397e-01 5.136055e-02 1.327393e-01 4.972894e-02
 16   4 5.545177       4       37 1.617975e-01 6.420636e-02 1.608840e-01 2.581636e-02
 24   4 6.356108       5       52 1.428683e-01 5.599483e-02 1.428188e-01 2.212685e-02
 32   4 6.931472       5       68 1.327397e-01 5.136160e-02 1.327391e-01 2.442811e-02
```

## Reading

The cutoff `D0=4` gives a cleaner split than `D0=2`: the cross block is roughly halved while the low
positive ceiling stays around `0.05--0.06 L^2`.

The high block still carries the actual top eigenvalue.  Therefore the next useful target is not
``low is everything'', but:

```text
APCB-high:
prove lambda_max(P_high Delta P_high)_+ = O(L^2)
```

with a separate, smaller low/cross budget.

This is still a compressed autocorrelation theorem, but now localized away from the low-frequency
Dirichlet-symbol obstruction.
