# Phase 27 — Adelic rigidity

**Prerequisite:** Conjecture 26-C.2 (Bridge Theorem) accepted as a working hypothesis.
**Sole objective:** prove $\mathrm{neg.ind}(H_C) = 0$ via the structure of $C_\mathbb{Q}$.

If Phase 26 is completed (the bridge is established), the program changes nature:
zeros of $\zeta$ are no longer studied. An operator on an adelic space is studied.

---

## 0. The starting point

**What Phase 26 would have established:**

$$\kappa(Q) = \mathrm{neg.ind}(H_C),$$

where $Q$ is the Weil form, $H_C$ is the Connes scaling operator, and the
identity holds on the Pontryagin space $\mathcal{K} = (L^2(C_\mathbb{Q}), Q)$.

**The consequence:**

$$\text{RH} \iff \kappa(Q) = 0 \iff \mathrm{neg.ind}(H_C) = 0.$$

**The one remaining open problem:**

$$\boxed{\mathrm{neg.ind}(H_C) = 0.}$$

---

## 1. The structure of the problem

The negative index of $H_C$ on $\mathcal{K}$ is the number of pairs of complex
(non-real) eigenvalues of $H_C$. By the Bridge Theorem:

$$\mathrm{neg.ind}(H_C) = 2m = \text{number of off-line orbits.}$$

So $\mathrm{neg.ind}(H_C) = 0$ is equivalent to: **there are no non-unitary
characters in the scaling spectrum of $H_C$.**

Each negative direction of $Q$ corresponds to a non-unitary character
$|x|^{b_j + i\gamma_j}$ (with $b_j > 0$) in the scaling spectrum.

The question of Phase 27: can such a character exist given the arithmetic structure of $C_\mathbb{Q}$?

---

## 2. The four sub-phases

### 27-A: Classification of negative directions

**Objective:** Prove that each negative direction of $Q$ on $\mathcal{K}$ produces
an isolated complex eigenvalue of $H_C$.

**Tool:** Kreĭn–Langer theorem (available for free from the bridge).

**Expected status:** Almost immediate from the bridge; the bound "at most $\kappa$" inverts
to "exactly $\kappa$" if each negative direction has a complex eigenvalue.

**Expected result:** A complete classification of the negative subspaces of
$\mathcal{K}$ in terms of non-unitary characters.

---

### 27-B: Adelic interpretation of the complex eigenvalues

**Objective:** Prove that every complex eigenvalue $\lambda_j = \gamma_j - ib_j$ of
$H_C$ (with $b_j > 0$) corresponds to a non-unitary Grössencharacter of $C_\mathbb{Q}$.

**Definition:** A Grössencharacter of $C_\mathbb{Q}$ of the form
$\chi_j(x) = |x|^{b_j + i\gamma_j}$ (with $b_j > 0$) is **non-unitary**: it has modular
growth $|x|^{b_j}$ and is not in the unitary dual $\widehat{C_\mathbb{Q}}$ measured by
the Haar measure.

**Tool:** Representation theory of $C_\mathbb{Q}$ (class field theory,
Tate 1950).

**Expected status:** Relatively direct from Tate's theory on adèles; the Grössencharacter
corresponding to an off-line zero $\rho_j$ should be the evaluation of the function $\zeta$
on the line $\Re(s) = 1/2 + b_j$, which is not the unitary line.

---

### 27-C: The adelic local-global principle

**Objective:** Prove that the existence of a non-unitary Grössencharacter in the spectrum
of $H_C$ contradicts some global property of $C_\mathbb{Q}$.

**The hypothesis of Phase 27:**

Let $Q = Q_\infty \times \prod_p Q_p$ be the local factorization of the Weil form
(if it exists). Then:

$$Q_p \ge 0 \text{ for every prime } p
\implies Q \ge 0 \text{ globally}
\implies \kappa(Q) = 0
\implies \mathrm{neg.ind}(H_C) = 0.$$

**The analogy:** The Hasse–Minkowski theorem says that a quadratic form $Q$ over
$\mathbb{Q}$ is globally positive-definite iff it is positive-definite locally (in
$\mathbb{R}$ and in $\mathbb{Q}_p$ for every prime $p$). If the Weil form $Q$ admits
an analogous principle, and if $Q_p \ge 0$ for every $p$ (which would follow from the
LOCAL Riemann hypothesis for curves over $\mathbb{F}_p$, which is PROVED by Weil–Deligne), then
$Q \ge 0$ globally, giving RH.

**The obstacle:** The Weil form $Q$ is not a classical quadratic form over $\mathbb{Q}$
— it is an infinite-dimensional functional form. The classical Hasse–Minkowski theorem does not
apply directly. The concrete question is:

> Does a Hasse–Minkowski principle exist for infinite-dimensional Hermitian forms
> over $\mathbb{Q}$, and does it apply to the Weil form $Q$?

**Relation to Wall W4-RSRP:** Phase 27 is the most precise formulation of Wall W4-RSRP
the program has produced. Instead of "arithmetic information cannot be propagated
from $\Re(s)>1$ into the critical strip", Phase 27 asks: "can the local-global
principle (which would propagate information from the local Euler factors $Q_p$ to the
global form $Q$) be established for infinite-dimensional Hermitian forms?"

---

### 27-D: Conclusion

**Objective:** From 27-C, deduce $\mathrm{neg.ind}(H_C) = 0$ and hence RH.

**Logic:** If the local-global principle is established and $Q_p \ge 0$ for all $p$,
then $Q \ge 0$, $\kappa = 0$, $\mathrm{neg.ind}(H_C) = 0$, RH.

---

## 3. Why Phase 27 is different from Phases 21–26

**Phases 21–24:** Spectral strategies within the Kreĭn arc.
Result: no lower bound for $b_j$.

**Phase 25:** Audit of 15 classical mechanisms.
Result: all fail as Wall W4-RSRP.

**Phase 26:** The Kreĭn–Connes bridge.
Result (conditional): κ = neg.ind($H_C$).

**Phase 27:** Uses the bridge to attack $\mathrm{neg.ind}(H_C) = 0$ with adelic tools.

The crucial difference: Phase 27 is the **first formulation of the program where the proposed
tool (adelic local-global principle) did not exist in previous phases**.

Phases 21–25 used available tools: functional analysis, zero theory, Selberg CLT,
Kreĭn–Langer. All exhausted.

Phase 27 uses tools that come from the arithmetic structure of the adelic space:
the local-global principle, Euler factorization, representation theory of $C_\mathbb{Q}$.
These tools are new to the program.

---

## 4. The more attainable intermediate objective

Before attacking $\mathrm{neg.ind}(H_C) = 0$ directly (equivalent to RH),
Phase 27 seeks intermediate results that would already be extraordinary:

| Intermediate objective | Direct implication |
|---|---|
| $\mathrm{neg.ind}(H_C) < \infty$ | Finitely many off-line zeros (Hypothesis D) |
| $\mathrm{neg.ind}(H_C) \le M$ for some constant $M$ | At most $M/2$ off-line orbits |
| $\mathrm{neg.ind}(H_C) \le 10$ | At most 5 off-line orbits |
| $\mathrm{neg.ind}(H_C) = 0$ | RH |

The goal $\mathrm{neg.ind}(H_C) \le M$ would correspond to a theorem of the type
"the function $\zeta$ has at most $M/2$ orbits of zeros off the critical line",
which has never been proved for any finite $M$ without assuming additional restrictions.
It would already be a historic result.

---

## 5. Documents of Phase 27

**27-A:** `phase-27-adelic-rigidity/01-classification-negative-directions.md`
**27-B:** `phase-27-adelic-rigidity/02-adelic-interpretation.md`
**27-C:** `phase-27-adelic-rigidity/03-local-global-principle.md`
**27-D:** `phase-27-adelic-rigidity/04-conclusion.md`

**Paper:** P36 (to be written once Phase 27 progresses).

---

## 6. Success criterion

Phase 27 succeeds if:
- The local-global principle is established for the Weil form (27-C), or
- It is proved that the principle cannot be established in this form, with precise diagnosis.

Phase 27 fails only if it produces no concrete mathematical result. Since the two
possible outcomes (valid principle → RH; or diagnosis of why it fails → next
reformulation) are both mathematically valuable, Phase 27 cannot "fail" in the
ordinary sense.

---

## 7. Status at the start of Phase 27

| Component | Status |
|---|---|
| Bridge Theorem (Conjecture 26-C.2) | Accepted working hypothesis; V.1–V.4 pending |
| neg.ind($H_C$) = κ | Conditional on the bridge |
| Factorization $Q = \prod_p Q_p$ | Not established; first objective of 27-C |
| Local-global principle for $Q$ | Open question; central objective of Phase 27 |
| $Q_p \ge 0$ for every prime $p$ | Plausible (local RH for $\mathbb{F}_p$ proved); connection to $Q_p$ not established |
