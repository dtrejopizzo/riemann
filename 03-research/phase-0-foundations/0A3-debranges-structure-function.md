# Phase 0.A.3 — Q and the de Branges structure function

**Status:** honest first draft of the dictionary. ⚑ = requires verification by a specialist in
de Branges spaces before it is trusted, **and** must be checked against the Conrey–Li
obstruction (§4) before any effort is invested. Goal: write the open inequality (LB) as a
chain (ordering) condition on a structure function $E(z)$.

---

## 1. de Branges spaces, in one screen

Given an entire **Hermite–Biehler** function $E$ (i.e. $|E(\bar z)|<|E(z)|$ for $\operatorname{Im}z>0$),
the de Branges space $\mathcal{H}(E)$ \[deBranges68\] consists of entire functions $F$ with
$F/E$ and $F^*/E$ in the Hardy space $H^2$ of the upper half-plane, with norm
$\|F\|^2=\int_\mathbb{R}|F(x)/E(x)|^2\,dx$. It is a reproducing-kernel Hilbert space with kernel
$$
K(w,z)=\frac{\overline{E(w)}E(z)-E^*(z)\overline{E^*(w)}}{2\pi i\,(\bar w-z)} ,\qquad
E=A-iB,\ A,B\ \text{real entire}.
$$
The decisive structural fact:
$$
\boxed{\text{the spaces }\mathcal{H}(E_t)\text{ of a "chain" are \emph{totally ordered by isometric inclusion}}
\iff\text{a positivity/ordering condition on }E.}
$$
For the Riemann $\xi$-function, de Branges' program seeks a chain
$\{\mathcal{H}(E_t)\}$ whose structure function degenerates to $\xi$ and for which the ordering
condition holds; **the ordering condition is his reformulation of RH.** \[deBranges86; deBranges92\] ⚑

## 2. The dictionary entry for our localized $Q$

Our Hermite–Gauss test functions $\{\varphi_j\}$ at $(T_0,\sigma)$ are, up to normalization, a
finite section of a **reproducing-kernel family**: $\varphi_j(\cdot)\approx K(\gamma_j,\cdot)$
for sample ordinates $\gamma_j$ near $T_0$. The Weil pairing $Q_{jk}=B(\varphi_j,\varphi_k)$ is
then a finite Gram matrix \emph{in} the candidate space $\mathcal{H}(E)$. ⚑ The required
identification is:

> ⚑ Determine the structure function $E=E_{T_0,\sigma}(z)$ for which the localized Hermite–Gauss
> kernels are (approximately) the reproducing kernels, and express $Q$ as the Gram matrix of the
> $B$-form in $\mathcal{H}(E)$.

| our object | de Branges object |
|---|---|
| $\varphi_j$ localized at $(T_0,\sigma)$ | reproducing kernels $K(\gamma_j,\cdot)$ of $\mathcal{H}(E)$ |
| $Q(T_0,\sigma,J)$ | Gram matrix of the $B$-form in a finite section of $\mathcal{H}(E)$ |
| enlarging the window / $\sigma$ | moving along the chain $E_t$ |
| (LB): $\lambda_{\min}(Q_\infty)\ge0$ for all localizations | the chain ordering condition on $E$ = RH |

## 3. What this buys, and the precise sub-question

The chain is **totally ordered** iff $\lambda_{\min}$ of the $B$-form behaves monotonically as
the space grows. Concretely:

> ⚑ **(de Branges-chain, the named lemma).** $\lambda_{\min}(Q(T_0,\sigma,J))$ is monotone under
> the canonical enlargement of the localization — monotone in $\sigma$ at fixed $(T_0,J)$ and
> monotone under nested windows — for the genuine $L$-functions.

If true, the chain condition holds and (LB) follows in the de Branges framework. This is exactly
hypothesis **(H2)** that the v9 stability probe tests. A clean *failure* of monotonicity (in the
specific pattern of §4) settles the de Branges route in the negative.

## 4. ⚑⚑ The Conrey–Li obstruction (mandatory guard)

de Branges' attempted proofs have a **known gap**: **Conrey & Li (2000)** \[ConreyLi00\]
constructed explicit counterexamples showing that the specific positivity hypotheses de Branges
required of his spaces are **not satisfied** by the spaces naturally attached to $\zeta$ — a
certain density/positivity condition fails. Any de Branges-flank work is therefore obligated to:
1. ⚑ identify *which* positivity our localized chain would need;
2. ⚑ check whether it is the very condition Conrey–Li show to fail;
3. abandon or modify the flank if it is.

This is why Flank II (de Branges) is weighted **below** Flank I (Connes) in the Phase 3 plan:
the Connes trace route has no comparably sharp known obstruction, whereas the de Branges route
has a documented one that must be cleared first.

## 5. What an expert must do (the hand-off)
1. ⚑ Identify $E_{T_0,\sigma}(z)$ explicitly for the localized kernels.
2. ⚑ Compute the positivity condition the chain requires and test it against Conrey–Li.
3. Use the v9 monotonicity numerics as a fast filter: monotonicity that *breaks in the
   Conrey–Li pattern* kills the flank cheaply; clean monotonicity keeps it alive pending (2).

**References to pin.** L. de Branges, *Hilbert Spaces of Entire Functions* (1968); L. de
Branges, *The convergence of Euler products* (1992) and related RH manuscripts; J. B. Conrey &
X.-J. Li, *A note on some positivity conditions related to zeta and L-functions* (Int. Math.
Res. Not. 2000); J. Lagarias, *Hilbert spaces of entire functions and Dirichlet L-functions*.
