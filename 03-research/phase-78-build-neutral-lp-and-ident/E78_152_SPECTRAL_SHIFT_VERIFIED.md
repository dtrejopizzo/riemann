# E78.152 - Bordered-determinant / rank-one spectral-shift identities VERIFIED

**Run:** 2026-07-21.
**Scope:** IDENT / point 6. Verifies the author's spectral-shift reformulation.
**Class:** PRUEBA COFINAL (exact identities, verified to roundoff).
**Attribution:** reformulation by the program author (2026-07-21); verified here.

## 1. The identities (proved by hand + checked numerically)

Actual transfer (P76.018): `T_N(z) = 1/(z-d_b) - sum_j x_j/(z-d_j)`,
`x = A^{-1} b` (right_transfer_data), `d_j = 2 pi n_j/L`, `d_b = 2 pi N/L`.
Set `F_N = (z-d_b) T_N`, `D = diag(d_j)`, `q_j = d_j - d_b`, `c = 1 - sum_j x_j`.

```text
(BD)  F_N(z) = det([ zI-D , x ; q^T , c ]) / det(zI-D).
(R1)  c != 0 => K_N := D + (1/c) x q^T,  F_N(z) = c det(zI-K_N)/det(zI-D).
(TR)  T_N'/T_N = Tr(zI-K_N)^{-1} - Tr(zI-D)^{-1} - 1/(z-d_b).
```

Hand proof of (BD): Schur complement gives `det(...)/det(zI-D) = c -
q^T(zI-D)^{-1}x = 1 - sum x_j - sum_j (d_j-d_b)x_j/(z-d_j)`, and
`(d_j-d_b)/(z-d_j) = -1 + (z-d_b)/(z-d_j)` collapses this to
`1 - (z-d_b) sum_j x_j/(z-d_j) = F_N`. (R1) is the matrix determinant lemma;
(TR) is `d/dz log det`. All exact.

**Independence from circularity:** `F_N` here is built from the transfer's own
data `(D, x, q, c)` -- NOT by integrating the target Gamma/cell derivative. So
(BD)/(R1)/(TR) escape the reformulation-circularity that reclassified E78.150.
This is the INDEPENDENT cell object point 6 needed.

## 2. Numerical verification (probe E78_152, lambda=6, dps=50, z=i)

```text
build  N   |c|        err_TR      max|Im kappa|   #complex
zeta   8   3.928e-7   1.22e-38    1.58e-37        0/15
zeta  10   4.561e-9   1.08e-36    4.502e-36       0/19
zeta  12   1.293e-7   4.59e-33    8.749e-33       0/23
plant  8   18.31      1.35e-51    0.0             0/15
plant 10   2.316      3.40e-52    5.22e-50        0/19
plant 12   11.78      2.01e-51    3.481e-49       0/23
```

- `(TR)` holds to `1e-33 .. 1e-51` (roundoff): the trace formula is exact.
- **`kappa_j` are REAL** (`max|Im| ~ 1e-33..1e-49`, `#complex=0`) for BOTH builds.
  So `nu_N = sum delta_{kappa_j} - sum delta_{d_j} - delta_{d_b}` is a real signed
  measure and the counting reformulation (E78.153) is well posed. Note: F_N is
  real-rooted even though NOT Herglotz (E78.148 sign-mixed residues) -- real
  roots without simple mesh interlacing.
- `|c| = F_N(infinity) = 1 - sum x_j` is TINY for zeta (1e-9..1e-7) and O(10)
  for the plant -- a further build fingerprint; the search must avoid dividing by
  `c` (use the generalized pencil for `kappa_j`).

## 3. Status

```text
proved (exact, verified to roundoff): (BD), (R1), (TR);
verified: kappa_j real both builds; measure nu_N well posed;
enables: SPECTRAL-SHIFT-COUNTING reformulation (E78.153), an INDEPENDENT cell
         object free of the E78.150 circularity;
next: E78.153 counting-sum summability.
```
