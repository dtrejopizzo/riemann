# E78.155 - Escaped-eigenvalue trajectories: corrects E78.154

**Run:** 2026-07-21.
**Scope:** IDENT / point 6. Corrects the E78.154 "single stable avatar" reading.
**Class:** AUTOPSIA (retraction + corrected structure).

## 1. Trajectory data (probe E78_155, lambda=6, dps=50)

```text
build  N   c            (ratio)   kappa_esc(farthest)  gap    mesh_r  kappa_hat=(qTx/c+mean d)
zeta   8   3.928e-7               1673.07              1661   12.27   1650.68
zeta  10  -4.561e-9    0.0116     1852.67              1837   15.78   1815.51
zeta  12   1.293e-7    28.35      2557.56              2538   19.29   2512.64
zeta  14   2.240e-9    0.0173     2807.59              2785   22.79   2739.56
zeta  16  -2.042e-10   0.0911     3310.03              3284   26.30   3222.55
zeta  18   3.593e-10   1.76       3748.87              3719   29.81   3640.78
plant  8  -18.31                  14.24                1.97   12.27   9.48
plant 10  -2.316       0.127      28.01                12.23  15.78   26.05
plant 12  -11.78       5.08       30.01                10.73  19.29   24.62
plant 14  -34.69       2.95       31.41                8.62   22.79   24.86
plant 16  -7.219       0.208      42.57                16.27  26.30   34.68
plant 18  -7.002       0.970      49.87                20.07  29.81   42.50
```

Direct spectrum (zeta N=12, mesh radius 19.3): 21 of 23 eigenvalues of `K_N`
lie OUTSIDE the mesh, in a near-symmetric cloud
`{+-21, +-25, +-30, +-38, +-42, +-50, +-66, +-99, +-216}` plus the single
asymmetric outlier `+2558`.

## 2. What this corrects

E78.154 claimed a single escaped eigenvalue at a stable `~ -50` acting as the
"avatar of the true zero", and reduced point-6 summability to a "1-outlier
problem". BOTH are wrong:

```text
- The farthest eigenvalue is at +1673 -> +3748 (GROWING), predicted well by
  kappa_hat = qTx/c + mean(d) (rank-one escape). It contributes
  ~2 sigma/(sigma^2 + kappa_esc^2) ~ 1e-7 to the transfer: NEGLIGIBLE.
- Because c is tiny, the rank-one term (1/c) x q^T reshapes the WHOLE spectrum
  into a near-symmetric cloud outside the mesh. There is no single isolated
  avatar; the M_N peak near -50 is one atom of that cloud.
- c_N is small (~1e-7..1e-10) but sign-oscillating and NOT geometric.
```

## 3. What survives (independently solid)

```text
- BOUND=TRUE=5.4/N^2 summable for zeta (E78.153): the fixed-L convergence half
  is still numerically reduced to a summable counting object;
- M_N * x single-signed (zeta) vs sign-mixed (plant): still the cleanest
  structural discriminant (E78.154 Sec 2 data unaffected);
- |c| small (zeta) vs O(1) (plant): still a build fingerprint.
```

## 4. Corrected open problem

Point-6 summability is a **difference-of-clouds** problem: `nu_N` and `nu_{N+2}`
are each near-symmetric spectral clouds (pushed out by `c` small), and
`BOUND_N = int |M_N| w ~ 5.4/N^2` measures their cumulative difference against
the kernel. This is genuinely harder than the retracted "1-outlier" claim. The
route is: (a) the near-symmetry of each cloud makes `M_N * x` single-signed
(explaining the tightness), and (b) the cloud converges in a scaled sense so the
difference decays like `1/N^2`. Neither is proved.

The build discriminant is NOT the (non-existent) stable avatar but the
**single-signedness of `M_N * x`** = coherence of the spectral-shift cloud,
present for zeta and absent for the plant.

## 5. Status

```text
retracted (E78.154):
  "single stable escaped eigenvalue ~ -50 = avatar of the zero"; "1-outlier
  summability"; "c -> 0 geometric";
observed (corrected):
  farthest kappa_esc at +1673..+3748 growing (negligible to transfer); K_N
  spectrum is a near-symmetric cloud outside the mesh (c small); c sign-oscillating;
surviving solid results:
  BOUND=TRUE=5.4/N^2 summable (zeta); M_N*x single-signed (zeta) vs sign-mixed
  (plant); |c| small vs O(1);
open (corrected, harder):
  point-6 summability = difference-of-clouds decay ~1/N^2 (not 1-outlier);
  discriminant = single-signedness/coherence of the spectral-shift cloud;
next:
  characterize the cloud's scaling limit (does nu_N, rescaled, converge?), which
  would control the difference; this is the honest remaining analytic object.
```
