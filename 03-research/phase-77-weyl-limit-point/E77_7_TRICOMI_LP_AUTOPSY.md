# E77.7 - Fixed-L TRICOMI-LP Setup and Autopsy

**Run:** 2026-07-18.

## 1. Real Spectral Target

Fix `L` and let `H_L` be the bilateral CCM matrix on the Fourier mesh

```text
d_n=2 pi n/L,  n in Z.
```

The initial operator is the symmetric matrix on finitely supported sequences.
Its self-adjoint realization and domain must be obtained from the fixed-L
matrix estimates; they are not inferred from finite self-adjoint sections.

The target is at a real spectral point:

```text
TRICOMI-LP(mu): ker_l2(H_L-mu I)={0},  mu in R,
```

where `mu` is the limiting real point selected by the bordered system.  A
non-real kernel statement would be automatic for a self-adjoint realization
and would not prove LP.  The required conclusion is absence of an embedded
`l2` eigenvector at the real point `mu`.

## 2. Exact Fixed-L Coefficients

The Loewner identity is

```text
H_L=2 diag(C_L(d_n))-(2/L)Loew(S_L).
```

For the diagonal cell

```text
q_nn(y)=2(1-y/L)cos(2 pi n y/L),
```

the prime-power contribution is exactly

```text
V_n^arith
=-2 sum_{p^k<=lambda^2}
    log(p) p^(-k/2) (1-k log(p)/L)
    cos(2 pi n k log(p)/L).                    (AT-1)
```

Thus, at fixed arithmetic cutoff, `V_n^arith` is a finite almost-periodic
trigonometric polynomial in `n`.  It is not a decaying Fourier tail.

## 3. Noncompactness Lemma

After grouping equal frequencies modulo `2 pi`, write

```text
V_n^arith=sum_j c_j exp(i n theta_j).
```

For distinct grouped frequencies,

```text
lim_{M->infinity} (1/M) sum_{n=0}^{M-1}|V_n^arith|^2
=sum_j |c_j|^2.                                (AT-2)
```

This follows by expanding the square and applying the finite geometric-sum
identity to every cross term.  Since `(AT-1)` has a nonzero coefficient,
the right side is positive.  Consequently

```text
V_n^arith does not tend to zero.
```

If the arithmetic matrix defined a compact operator `K`, then for the
standard orthonormal basis `e_n`, weak convergence `e_n->0` would imply

```text
<K e_n,e_n> -> 0.
```

Equation `(AT-1)` contradicts this.  Therefore the fixed-L arithmetic part
is not a compact or decaying perturbation of the pure Cauchy/Gamma operator.

The planted addition does not repair this.  It is added to the same zeta
prime-power base.  Its diagonal integral is an ordinary Fourier coefficient
of a smooth finite-interval function and decays away from finite resonances;
it cannot cancel the nondecaying frequency package `(AT-1)`.

## 4. Probe

Companion:

```text
E77_7_tricomi_lp_probe.py
```

Command:

```bash
python3 E77_7_tricomi_lp_probe.py \
  --lambda 6 --max-index 4000 --dps 60
```

The exact formula agrees with independently integrated CCM entries to

```text
max relative defect = 8.07e-61.
```

Tail statistics for `V_n^arith`:

| index block | mean | RMS | max absolute value |
|---|---:|---:|---:|
| 0--99 | -3.288e-2 | 1.38664 | 5.93742 |
| 100--499 | -2.132e-3 | 1.34717 | 4.00192 |
| 500--999 | 1.856e-3 | 1.34330 | 3.93001 |
| 1000--1999 | 1.439e-3 | 1.33652 | 4.55954 |
| 2000--4000 | -3.796e-4 | 1.34635 | 4.48491 |

The mean approaches zero while the RMS remains near `1.34`, exactly the
almost-periodic rather than decaying signature.  The standard planted build
was also evaluated.  It retains the same base package; its extra diagonal is
small at late sampled indices (`-8.51e-3` at `n=16`, `-2.33e-3` at `n=24`)
apart from finite resonances.

## 5. Autopsy of the Proposed R2 Mechanism

The proposed reduction was

```text
H_L = H_L^Tricomi + compact/decaying arithmetic perturbation,
```

followed by pure-Tricomi fundamental asymptotics.  Sections 2--4 refute its
second premise.  The exact blocking coefficient is `(AT-1)`:

```text
V_n^arith, a nondecaying almost-periodic diagonal coefficient.
```

The displacement equation still exists, but its fundamental solutions solve
a variable almost-periodic problem, not the constant-coefficient discrete
Tricomi equation.  Treating `(AT-1)` as an asymptotically negligible constant
would change the operator and would not identify the intrinsic fixed-L Weyl
function required by E77.6.

This autopsy does not refute LP.  It refutes only the advertised R2 proof by
compact perturbation of the pure Cauchy model.  A new almost-periodic
subordinacy theorem could in principle attack LP, but no such theorem follows
from RDP-1/MR-1, and introducing it here would not be a smaller target.

## 6. Mandatory Pivot to R3

The next admissible object is direct fixed-point growth:

```text
FIXED-MU-BLOCK-GROWTH:
for the real limiting mu and each fixed L, canonical solutions normalized
at the border satisfy

  min_{0<=j<q} S_{N+j}(mu) -> infinity

for a fixed finite block width q, separately across the mesh parities.
```

This implies Weyl-disk contraction because the disk radius is the reciprocal
canonical energy.  Block minima absorb the finite resonances seen in E77.1b.
The quantitative extension required by the radical interface is

```text
SHELL-CAUCHY-GROWTH:
|r_z w_N|/|r_z g_N| -> 0
```

for shell-supported sources, locally uniformly on safe compacta.

Before estimating growth, R3 must freeze the moving finite-section points:

```text
MU-LIMIT:
mu_{L,N}->mu_L in R, and replacing mu_{L,N} by mu_L preserves the
block-growth and selected Cauchy ratios.
```

`MU-LIMIT + FIXED-MU-BLOCK-GROWTH` implies the LP obligation in E77.6;
adding `SHELL-CAUCHY-GROWTH` supplies the promised RDP-SHELL interface.

## 7. Status

```text
proved:    exact nondecaying arithmetic coefficient (AT-1);
proved:    the fixed-L arithmetic matrix is not a compact perturbation;
observed:  tail RMS remains 1.34 through n=4000 for lambda=6;
refuted:   pure Tricomi plus decaying arithmetic perturbation as R2;
open:      LP at the real point mu;
open:      MU-LIMIT, FIXED-MU-BLOCK-GROWTH, SHELL-CAUCHY-GROWTH;
next:      E77.7b R3 moving-mu versus fixed-mu audit.
```

