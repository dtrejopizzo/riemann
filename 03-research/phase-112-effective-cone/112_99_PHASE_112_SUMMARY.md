# 112.99 — Phase 112 summary

**Verdict: d5 is satisfied only formally — outcome (b).**

* $D_f\cdot H=\widehat f(0)+\widehat f(1)>0$ for $f\ge0$: holds, but is a
  restatement of the positivity of an integral, with no geometric content.
* $f\ge0\iff u_f$ convex (from $u_f''(r)=f(r)/r$): a real characterization —
  "no subtraction needed in the DC decomposition" — but **not** a sections
  statement.
* Disjoint-support test (the falsifiable one): 142 pairs, **0 negative, 0
  sign flips**, truncation convergence verified by refinement. Evidence, not
  proof.
* $D_f^2<0$ for narrow bumps: **expected**, not a refutation — effective
  divisors may have negative self-intersection ($E^2=-1$ on a blowup of
  $\mathbb P^2$). The classical statement requires no common component.

**The gap.** Classically $D$ is effective iff $h^0(D)>0$. No $h^0$ exists in
this category, so the classical proof's step *"$h^0(nD)\to\infty$, hence
$nD$ is effective"* has nothing to land in. Building $h^0$ is d3/d4, blocked
upstream by d1.

Verifiers `112_01`, `112_02`, `112_03` all exit 0. Nothing here bears on RH.
