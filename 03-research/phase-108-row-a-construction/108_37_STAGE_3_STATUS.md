# 108.37 — Stage 3 status

## 1. Verdict

> **Stage 3 closes**, in the reformulated sense prescribed by the design
> condition, with an explicit convergence boundary.

| item | status |
|---|---|
| $\Gamma_{p,k}$ constructed as a functional | **closed** (108_34) |
| pairing formula with the graded family | **closed** (108_34) |
| normalization producing $\log p$ | **closed** (108_35) |
| Weil coefficient $\Lambda(p^k)/\sqrt{p^k}$ at $s=\tfrac12$ | **closed, exact** (108_35 Thm 2.1) |
| assembly $=-\zeta'/\zeta(s)$ | **closed on $\Re s>1$** (108_36 Thm 1.1) |
| assembly on the critical strip | **only as continuation** (108_36 Prop 2.1) |
| design condition satisfied | **yes** (§2) |
| dependence on Stage 2 | **none** (§3) |

## 2. The design condition is satisfied

108_90 §5 flagged Stage 3 as posed, because it asked for classes that are
simultaneously scaling-equivariant and supported at finitely many places —
the combination that has failed eight times.

The construction avoids it.  $\Gamma_{p,k}$ is a **functional**: by 108_34
Lemma 1.3 it is $p^{\min(k,0)}$ times the Dirac evaluation $\delta_{p^k}$, so
its support is a single point — finite.  It is **not required to be
equivariant**: the scaling covariance is carried entirely by the graded
sections it is paired against, which by 108_02 are the character-covariant
family $f_s$.

> Finiteness sits on the functional; equivariance sits on the sections.  The
> two demands are on opposite sides of the pairing, exactly as the design
> condition prescribes.

## 3. Independence from Stage 2

Stage 2 asks whether the pairing descends to a quotient.  Nothing in 108_34,
108_35 or 108_36 refers to a quotient, to principality, or to any
equivalence relation on divisors: $\Gamma_{p,k}$ is defined from the shell
decomposition of $\mathbb Q_p^\times$ and a choice of Haar measure, and the
assembly is an identity of Dirichlet series.  **Stage 3 is therefore
independent of Stage 2**, and its results stand whatever Stage 2 returns.

## 4. What Stage 3 does not give

Stated plainly, because the identity of 108_36 invites over-reading.

* **The assembly is not an intersection number.**  108_36 Theorem 1.1 is an
  identity between a sum of functionals and a Dirichlet series.  Making
  either side an intersection pairing is Stage 5, and is untouched here.
* **No convergence on the strip.**  108_36 Proposition 2.1 states the
  opposite; on $0<\Re s<1$ the assembly exists only as the meromorphic
  continuation.  This is the same phenomenon as 108_06 Theorem 4.1, now at
  the level of the functionals.
* **The archimedean term is absent.**  That is Stage 4.
* **Normalization (N2) is conventional, not forced.**  It is the standard
  adelic choice and the one in which the explicit formula is stated, but no
  uniqueness theorem is proved (108_35 §3).
* **Nothing bears on RH.**

## 5. Programme position

```
Stage 0  corner pairing                      closed
Stage 1  descent, graded pairing             closed
Stage 2  Picard: does the pairing descend?   PLANNED, NOT EXECUTED
Stage 3  correspondences                     closed (this note)
Stage 4  archimedean fibre                   open
Stage 5  Lefschetz as intersection           open
Stage 6  primitive inequality (row d)        open
Stage 7  scaling compatibility               open
```

Stage 3 having proved independent of Stage 2, the two may be pursued in
either order.  Stage 5 is the natural successor, since it is precisely the
step that would turn 108_36's identity into an intersection statement, and it
requires Stage 4 for the archimedean term.

`ROW_A_STATUS` is not promoted here; that is a ledger decision.

## 6. Verifier

`108_37_stage_3_status.py` re-runs the three Stage-3 verifiers as
subprocesses and confirms each exits 0.
