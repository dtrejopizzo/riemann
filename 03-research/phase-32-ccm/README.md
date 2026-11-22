# Phase 32 — Semilocal Prolate Operators and Sonin Spaces (CCM)

Starting from the Connes–Consani–Moscovici (2024) theory of semilocal cyclic pairs and prolate wave operators, this phase builds a bridge between the Jacobi-coefficient discrepancy $\Delta_n^S$ of the semilocal measure $dm_S$ (for finite sets of places $S$) and the arithmetic deficit $C_\infty(\gamma_n)$ of Phase 29. The goal is a Jacobi-operator invariant whose vanishing is equivalent to RH, built entirely from orthogonal-polynomial and Christoffel–Darboux machinery.

## Results
- The Jacobi discrepancy $\Delta_n^S>0$ for every finite $S\supsetneq\{\infty\}$, and $\Delta_n^{\{\infty,p\}}\sim A_n/p$ with $\sum_{p\le T}\Delta_n^{\{\infty,p\}}\sim A_n\log\log T$. (PROVED)
- Exact Christoffel–Darboux representation of the perturbation functional $L_n$; the naive "Kernel Concentration Problem" (KCP) is refuted by an elementary Fourier argument and replaced by the "Pseudo-Pole Problem" (PPP). (PROVED / NO-GO for the naive form, reformulated)
- Correction of an earlier locality-scale estimate: the correct scale is $O(1)$, not $O(1/\log\gamma_n)$; the perturbation kernel $\kappa_n$ oscillates in sign, so individual discrepancies have indefinite sign. (PROVED, correcting a prior document)
- **Positive Trace Conjecture (PTC), full equivalence:** $\mathrm{RH} \iff T_\lambda = 0$ for all $\lambda>0$, where $T_\lambda$ is the cumulative Jacobi-discrepancy trace; both directions proved (positivity under ¬RH via $W_\lambda\ge0$, and the converse via injectivity of the Hamburger moment problem). (PROVED)
- Quantitative lower bound $T_\lambda \ge c\cdot N(\lambda)\cdot w(\gamma_0)$ under ¬RH, and an exact integral formula for $T_\lambda$ in terms of $|\zeta(1/2+is)|^2 - |\zeta_{\mathrm{on}}(1/2+is)|^2$. (PROVED)
- PPP (exact Wronskian non-vanishing $W_n(\gamma_n)\neq0$): proved exactly and unconditionally via the three-term recurrence ($W_n \equiv -1/a_n^\infty$, constant), after intermediate heuristic Plancherel–Rotach/Bessel asymptotic arguments. (PROVED exact; earlier intermediate steps labeled HEURISTIC)
- Explicit note that the PTC equivalence is a correct reformulation of RH, not a proof of it: $T_\lambda=0$ is not established, only shown equivalent to RH. (explicitly flagged, not a closure)

## Documents
- `59`: import of the CCM framework, semilocal measures $dm_S$, Bridge Conjecture (B.C.).
- `60`: decay rate of $\Delta_n^{\{\infty,p\}}$, operational Bridge Conjecture (B.C.-O).
- `61`: Christoffel–Darboux representation of $L_n$, Kernel Concentration Problem (KCP).
- `62`: refutation of the exact KCP, formulation of the Pseudo-Pole Problem (PPP) via the Stieltjes transform.
- `63`: correction of the locality scale, oscillation of $\kappa_n$, Positive Trace Conjecture (PTC), proof $W_\lambda\ge0$.
- `64`: converse of the PTC; main equivalence RH $\iff T_\lambda=0$; quantitative lower bound under ¬RH.
- `65`–`67`: PPP via the prolate recurrence and Wronskian, Plancherel–Rotach and Bessel asymptotics for the CCM orthogonal polynomials (heuristic stages).
- `68`: rigorous, exact evaluation of the Wronskian directly from the recurrence, closing the PPP unconditionally.
- `69`: synthesis — closed algebraic formula for $F_n$ and the integral form of $T_\lambda$; closes Phase 32.

## Relation to other phases
Continues Phase 29 (deficit $C_\infty$, arithmetic formula Doc 54) and Phase 31 (moment/attainment question). The main equivalence RH $\iff T_\lambda=0$ feeds into Phase 33 (de Bruijn–Newman / CCM trace).

## Contents

- `59-bridge-between-the-ccm-program.md` — Document 59 — Bridge between the CCM program and the deficit $C_\infty$
- `60-decay-and-sum-of-the-semilocal-jacobi.md` — Document 60 — Decay and sum of the semilocal Jacobi discrepancy
- `61-locality-of-the-functional-and-the-de.md` — Document 61 — Locality of the functional $L_n$ and the de Branges kernel
- `62-kcp-via-the-stieltjes-transform.md` — Document 62 — The KCP via the Stieltjes transform and the Sonin space
- `63-christoffel-scale-oscillations-of-and-global-positivity.md` — Document 63 — Christoffel scale, oscillations of $\kappa_n$, and global positivity
- `64-ptc-is-equivalent-to-rh-closure.md` — Document 64 — The PTC is equivalent to RH: closure of the program
- `65-ppp-recurrencia-prolate.md` — Document 65 — PPP via prolate recurrence: concentration of coefficients $c_k = \langle \Xi, P_k \rangle$
- `66-plancherel-rotach-dm-infty.md` — Document 66 — Plancherel-Rotach asymptotics for $P_k$ with the CCM measure $dm_\infty$
- `67-bessel-asymptotics-in-the-left-edge-region.md` — Document 67 — Bessel asymptotics in the left-edge region and the unconditional PPP
- `68-rigorous-verification-of-the-wronskian-ppp.md` — Document 68 — Rigorous verification of the Wronskian: PPP from the difference equation
- `69-synthesis-of-phase-32-exact-structure.md` — Document 69 — Synthesis of Phase 32: exact structure of $F_n$ and closure of the program
