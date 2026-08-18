# 106.20 — Compensated-spectrum diagnostic

## Purpose and status

Document 106.19 reduces the completed semilocal Weil inequality to

\[
 \mathcal A_\Delta(f)
 \le \mathcal E_*(f)-c_*\|f\|_2^2,
 \qquad
 c_*=\gamma+\frac\pi2+3\log2+\log\pi-4.
 \tag{1}
\]

This note implements (1) in the Fourier Galerkin bases already used by
106.04.  It has two goals:

1. verify numerically that the independently assembled compensated matrix
   is the original coupled Weil matrix; and
2. locate the nearly extremal modes of (1) without asserting that finite
   precision proves their sign.

The computation is a diagnostic only.  In particular, eigenvalues at or
below the float64/quadrature scale are recorded as unresolved, not as
positive or negative certificates.

## 1. Independent matrix assembly

Let

\[
 U_k(x)=L^{-1/2}e^{2\pi ikx/L}\mathbf1_{[-L/2,L/2]}(x),
 \qquad |k|\le K,
 \tag{2}
\]

and let \(\Omega_K(u)\) be the correlation matrix

\[
 \bigl(\Omega_K(u)\bigr)_{jk}
 =\langle U_j,\tau_uU_k\rangle
  +\langle U_j,\tau_{-u}U_k\rangle.
 \tag{3}
\]

Thus \(\Omega_K(0)=2I\).  The three matrices in (1) are assembled as

\[
\begin{aligned}
 E_{*,K}
 &=\int_0^\infty
   \bigl(2I-\Omega_K(u)\bigr)
   \frac{e^{-5u/2}}{1-e^{-2u}}\,du,\\
 P_K
 &=\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}
   \Omega_K(\log n),\\
 M_K
 &=\int_0^L e^{u/2}\Omega_K(u)\,du,\\
 A_{\Delta,K}&=P_K-M_K.
\end{aligned}
\tag{4}
\]

For \(u\ge L\), zero extension makes \(\Omega_K(u)=0\).  The tail in the
first line of (4) is therefore the explicit scalar

\[
 2I\sum_{j\ge0}\frac{e^{-(5/2+2j)L}}{5/2+2j}.
 \tag{5}
\]

The independently compensated matrix is

\[
 W_K^{\mathrm{comp}}=E_{*,K}-c_*I-A_{\Delta,K}.
 \tag{6}
\]

It is compared with the matrix \(W_K\) assembled directly from the polar,
Gamma and prime-power entries of 106.04.  On the complete sweep

\[
 \lambda\in\{1.5,2.2,3,5,10\},\qquad
 K\in\{2,4,6,8,10\},
 \tag{7}
\]

with 512-point Gauss quadrature, the worst relative Frobenius residual was

\[
 \max_{\lambda,K}
 \frac{\|W_K-W_K^{\mathrm{comp}}\|_{\mathrm{HS}}}
      {\max(1,\|W_K\|_{\mathrm{HS}})}
 =1.60\times10^{-13}.
 \tag{8}
\]

Repeating the numerically resolved part with quadrature orders
256, 384, 512 and 768 leaves the displayed Rayleigh margins unchanged to
the printed digits.  Equation (8) checks the bookkeeping and normalization;
it does not certify (1).

## 2. Generalized extremal problem

Since \(E_{*,K}>0\) in every tested finite basis, define

\[
 \rho_K
 =\lambda_{\max}\left(
 E_{*,K}^{-1/2}(A_{\Delta,K}+c_*I)E_{*,K}^{-1/2}
 \right).
 \tag{9}
\]

The finite-dimensional compensated inequality is \(\rho_K\le1\), and its
generalized margin is \(1-\rho_K\).  Representative rows are:

| \(\lambda\) | \(L\) | \(K\) | \(\min W_K\) | \(1-\rho_K\) | physical boundary mass | RMS Fourier index |
|---:|---:|---:|---:|---:|---:|---:|
| 1.5 | 0.811 | 2 | \(3.22\cdot10^{-4}\) | \(4.36\cdot10^{-4}\) | 0.461 | 0.54 |
| 1.5 | 0.811 | 10 | \(1.57\cdot10^{-4}\) | \(2.14\cdot10^{-4}\) | 0.462 | 0.53 |
| 2.2 | 1.577 | 2 | \(2.51\cdot10^{-7}\) | \(5.13\cdot10^{-7}\) | 0.604 | 0.69 |
| 2.2 | 1.577 | 4 | \(9.70\cdot10^{-11}\) | \(1.68\cdot10^{-10}\) | 0.683 | 0.81 |
| 3.0 | 2.197 | 2 | \(4.92\cdot10^{-9}\) | \(1.36\cdot10^{-8}\) | 0.633 | 0.73 |
| 5.0 | 3.219 | 2 | \(2.39\cdot10^{-10}\) | \(1.08\cdot10^{-9}\) | 0.636 | 0.74 |
| 10.0 | 4.605 | 2 | \(1.46\cdot10^{-11}\) | \(1.11\cdot10^{-10}\) | 0.641 | 0.75 |

Here “physical boundary mass” is the fraction of \(|f(x)|^2\) in the two
outer strips, each of width \(0.1L\).  A spatially uniform mode would have
boundary mass 0.2.

For the rows whose margin falls to the matrix-identity scale, the sign is
unresolved.  More importantly, the largest generalized eigenvalue ceases to
be isolated: at \((\lambda,K)=(2.2,10)\) three generalized modes lie within
\(10^{-10}\) of the top, at \((5,10)\) there are ten, and at \((10,10)\)
there are twelve.  Individual eigenvectors inside that cluster are not
stable objects.  The growing near-extremal subspace, rather than a stable
negative eigenmode, is the numerical event.

## 3. Localization of the bottleneck

### 3.1 It is not a Fourier-edge instability

In every resolved row the extremal vector is even to numerical precision.
Its RMS Fourier index lies between 0.53 and 0.81, and more than 91% of its
Fourier mass lies in the central quarter of the available indices.  The
mass in the outer 20% of Fourier indices is below 2.7% and normally below
0.1%.

Thus the saturation is low-frequency.  Increasing \(K\) does not move the
worst vector to the ultraviolet edge; it creates more near-radical modes.

### 3.2 It is physically boundary-concentrated

Although it is low-frequency in coefficient space, the resolved extremal
vector places 46%--74% of its physical mass in boundary strips occupying
only 20% of the interval.  At \((\lambda,K)=(2.2,6)\), just before the top
eigenspace becomes numerically multiple, that fraction is 0.706.

The observed bottleneck is therefore consistent with the moving
co-Poisson/prolate radical and zero-extension leakage already identified in
106.09--106.14.  A coercive estimate that treats the boundary killing as a
fixed positive gap will miss the observed scale.

### 3.3 The arithmetic saturation is atom-driven but jointly compensated

On the extremal vector the two constituents of \(A_\Delta=P-M\) are much
larger than the final Weil margin.  Examples are

\[
\begin{array}{c|c|c|c}
 (\lambda,K)&\langle P\rangle&\langle M\rangle&
 \langle A_\Delta\rangle\\ \hline
 (2.2,2)&0.1497&1.0320&-0.8822\\
 (3,2)&0.4018&1.4130&-1.0112\\
 (5,2)&1.1013&2.2518&-1.1506\\
 (10,2)&2.3921&3.6327&-1.2406.
\end{array}
\tag{10}
\]

The role of the atoms is not a termwise positive correction.  If they are
removed and the generalized problem is recomputed, the maximum ratios at
\(K=2\) are respectively

\[
 1.028,\ 1.996,\ 3.364,\ 8.031,\ 25.712
 \tag{11}
\]

for the five \(\lambda\)-values in (7).  Thus the smoothed PNT replacement
violates the target severely, while the complete atom matrix reorganizes
the spectrum and returns its top to \(1\) within the observed margin.  This
is collective signed cancellation, not monotone domination.

A leave-one-atom-out test makes the distinction sharper.  At
\((\lambda,K)=(10,2)\), removing only the atom \(n=11\) raises the
reoptimized ratio from \(1+O(10^{-10})\) to 4.315; omitting \(n=13\) gives
4.221 and omitting \(n=7\) gives 3.962.  At \(K=10\), omission of \(n=11\)
gives 4.413.  These are reoptimized quotients: the damaging vector rotates
after the atom is removed.  Consequently no ranking of atoms on one fixed
extremal captures the mechanism.

On the actual
extremal at \((\lambda,K)=(10,2)\), the five largest atom expectations
carry 92% of the sum of the absolute atom expectations; the leading atoms
are \(2,3,5\).  At \(K=10\) the top-five fraction remains 73.5%.

This does **not** justify a finite-prime truncation: the extremal vector and
the ranking of atoms change with \(L\) and \(K\), and (1) is a uniform
global assertion.  It does show that replacing the actual Stieltjes measure
by a smooth PNT envelope erases the mechanism that makes the inequality
sharp.

## 4. Reproduction

Run

```bash
cd 03-research/phase-106-global-modular-star-audit
python3 106_20_compensated_spectrum_probe.py
```

Optional arguments include comma-separated `--lambdas`, comma-separated
`--modes`, and `--quadrature`.

## 5. Verdict

The diagnostic gives no stable counterexample to the compensated
inequality.  It verifies that the exact compensation of 106.19 is the same
matrix problem as the source Weil form and identifies the numerical
bottleneck:

\[
 \boxed{
 \text{low Fourier frequency}
 +\text{ physical boundary concentration}
 +\text{ literal low-prime atoms}
 +\text{ a growing near-radical cluster}.}
 \tag{12}
\]

Accordingly, a viable proof cannot rely on high-frequency Gamma coercivity,
a fixed boundary Poincare constant, or a smooth PNT majorant.  It must prove
a **relative** estimate on the moving near-radical space while retaining the
signed atom-by-atom prime/PNT compensation.  Establishing that estimate is
still the force-bearing theorem; this computation does not prove it or RH.
