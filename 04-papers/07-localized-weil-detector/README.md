# Paper 07 — A Rigorous Localized Weil Detector for Off-Critical Zeros: Forced Negativity, Unconditional Truncation Control, and the Logical Status of the Truncation Lemma

The paper studies a finite, localized realization $Q(T_0,\sigma,J)$ of Weil's quadratic form. It is
the Gram matrix of the Weil functional on $J$ Hermite–Gauss test functions centred at height $T_0$
with width $\sigma$, assembled as $Q=M_{\mathrm{zeros}}-M_{\mathrm{arith}}$. An off-critical zero
forces a negative eigenvalue with an explicit constant. Truncating the prime sum at $X$ costs an
error controlled by the prime number theorem alone. Together these give an unconditional detector
for a fixed off-critical zero. The uniform passage $\lambda_{\min}(Q_X)\to\lambda_{\min}(Q_\infty)$
is shown to be the whole remaining difficulty.

## Main results

- `lem:rank2`, `thm:forced`: an off-line zero at displacement $\delta$ lowers $\lambda_{\min}(Q)$ by
  $c\sim\delta^2A(\gamma)$, with explicit constants — PROVED.
- `prop:numconf`: the constant matches high-precision computation to relative error $<10^{-5}$ — NUMERICAL.
- `thm:trunc`: $\eta(X)\le A\exp(-\alpha(\log X)^2)$, $\alpha\approx\sigma^2/8$, using only the prime
  number theorem — PROVED.
- `prop:eta-emp`: empirical match of the truncation floor across $L$-functions — NUMERICAL.
- `thm:detector`: for a fixed off-critical zero there is an explicit $X_{\min}$ beyond which
  $\lambda_{\min}(Q_X)<0$ unconditionally — PROVED.
- `prop:dichotomy`, `cor:LB`: the uniform spectral-gap inequality between $\lambda_{\min}(Q_X)$ and
  $\lambda_{\min}(Q_\infty)$ is the single missing inequality — OPEN (its logical status is PROVED).

## Files

- `main.tex`, `main.pdf` — source and compiled paper.
- `figures/` — figures.

## Relation to other papers

Papers 09–11 build on the localized form $Q$ (stability, anatomy, negative index).
