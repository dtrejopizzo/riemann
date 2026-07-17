# E72.292 -- Low/cross band budget

**Purpose.** Complete the proof-facing APCB band package with low and cross estimates.

Use the cutoff `|d|<4` from E72.290.  In block form:

```text
Delta = [[A,B],[B^*,D]].
```

E72.291 reduces the high block `D` to the row-sum estimate `H-GERSH`.

For the remaining blocks:

```text
lambda_max(Delta)_+
<= lambda_max(A)_+ + lambda_max(D)_+ + ||B||.
```

The low block has fixed tiny rank in the tested windows (`4--5`), so it can be certified by direct
finite block estimates.  The cross block is small and can be bounded by either Frobenius or Schur:

```text
||B|| <= ||B||_F,
||B|| <= sqrt( max_i sum_j |B_ij| * max_j sum_i |B_ij| ).
```

## Probe

Run:

```text
python3 E72_292_low_cross_band_budget_probe.py
```

Output:

```text
E72.292 low/cross band budget probe
Cutoff |d|<4. Low is finite rank; cross can be bounded by Frobenius or Schur.
lam L rankLow low+/L2 lowRow/L2 cross/L2 crossF/L2 crossSchur/L2 highRow/L2
 16 5.545177       4 6.420636e-02 7.694847e-01 2.581636e-02 2.875139e-02 3.938756e-02 3.664654e-01
 24 6.356108       5 5.599483e-02 9.037586e-01 2.212685e-02 2.524127e-02 3.909721e-02 3.620481e-01
 32 6.931472       5 5.136160e-02 1.013867e+00 2.442811e-02 2.737756e-02 4.274821e-02 3.374529e-01
```

## Reading

The low row-sum bound is loose, but the low block is finite rank and its positive eigenvalue is
small (`~0.05--0.06 L^2`).  The cross block is stable around `0.02--0.03 L^2`.

Thus APCB is now reduced to three non-spectral estimates:

```text
LOW-FIN:   lambda_max(A)_+ <= C_low L^2       (finite-rank low block),
H-GERSH:   max_i sum_j |D_ij| <= C_high L^2   (high row sums),
CROSS-HS:  ||B||_F <= C_cross L^2             (cross block).
```

This is the current clean compressed route for APCB.
