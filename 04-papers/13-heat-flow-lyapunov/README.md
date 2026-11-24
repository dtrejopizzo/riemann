# Monotonicity of the Off-Line Mass under the de Bruijn–Newman Zero Flow

The paper studies the zero dynamics of the backward heat flow $\partial_t p=-\partial_{zz}p$, which defines the
de Bruijn–Newman deformation $H_t$ of the Riemann $\xi$-function. It records an identity for the off-line mass
$\mathcal L=\sum_j(\mathrm{Im}\, z_j)^2$ and computes backward-collision times for a few windows of zeta zeros.

## Contents

- Theorem 2.1: for a real polynomial with simple zeros,
  $\dot{\mathcal L}=-2\sum_{j\ne k}(y_j-y_k)^2/|z_j-z_k|^2\le0$ (elementary finite-configuration identity).
- Corollary 2.2: de Bruijn's strip bound, $\Lambda\le t_0+\Delta^2/2$ (known; cited to de Bruijn 1950), with an
  exact polynomial example showing it is only an upper bound.
- Remarks 3.1, 4.1, 4.2: the identity holds for every conjugate-symmetric configuration and so does not
  distinguish $\xi$; two-body collision time $-g_0^2/8$; the computation yields no RH criterion in terms of gap statistics.
- Numerical: backward-collision times $t_c$ and ratios $t_c/s^2$ for three windows of 20 zeta zeros.

The flow, de Bruijn's bound and $\Lambda\ge0$ (Rodgers–Tao) are known; the paper's contribution is the
monotonicity identity stated for the off-line mass and the small numerical table.

## Files

- [main.tex](main.tex) — LaTeX source.
- [heat-flow-lyapunov.pdf](heat-flow-lyapunov.pdf) — compiled paper (4 pages).
- [collision_times.py](collision_times.py) — computes the table and the polynomial example.
- [output.txt](output.txt) — output of the script.

## Relation to other papers

Companion to Paper 12.
