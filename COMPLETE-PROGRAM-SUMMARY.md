# The Riemann Program — Summary

This document describes the whole program in a few pages: its arcs, the papers they produced, what
is proved, and what remains open. Details and proofs are in the papers (`04-papers/`) and in the
research record (`03-research/`). No paper claims a proof of the Riemann hypothesis.

## 1. Structure

The work has two layers.

- **Research programs RH1–RH9** (`01-context/`). Nine computational investigations: resonance and
  ω-class statistics of Dirichlet polynomials, extreme values, covariance structure, inverse spectral
  problems, the localized Weil form and its detector, stability and monotonicity, and a literature
  study of Lefschetz/Arakelov approaches. They are descriptive and numerical; they fixed the
  vocabulary and the objects of the later work.
- **The phase sequence** (`03-research/`, phases 0–209). The theoretical program, organised in
  numbered phases, each with its memos, audits and verdicts.

## 2. The arcs

**Arc A — ω-classes (phases 0–9).** Decomposition of $S_N(t)=\sum_{n\le N}n^{-1/2-it}$ by
$\omega(n)\bmod 2$. The target bound $B(N)\le N^{\varepsilon}$ turned out to be stronger than
Lindelöf and to be blocked by the parity problem of sieve theory. RH-independent output: the
ω-class / multiplicative-chaos dictionary (Paper 05) and an exact information barrier (Paper 21).

**Arc B — inverse operators and Hilbert–Pólya (phases 10–28).** Attempts to build a self-adjoint
operator with spectrum the zero ordinates. Every construction met the same propagation wall.

**The Connes–Consani–Moscovici frame (phases 29–33).** Spectral-triple and prolate reformulations;
trace and measure criteria (Papers 22–25). Reformulations, no sign.

**Phases 34–106 — the Weil form and the Pick architecture.** The localized Weil form, its Kreĭn and
Pontryagin realizations, a large catalogue of no-go theorems and falsifiers (Papers 06–41), and a
fifteen-step arithmetic Pick/Nevanlinna architecture terminating at the Li–Keiper criterion
(Paper 36).

**Arc C — the arithmetic Lefschetz programme (phases 107–133).** A direct imitation of Weil's proof
for curves over finite fields, built on the idele class group of $\mathbb Q$ and organised in four
rows (Paper 42, then Papers 43–45). After an adversarial audit (phase 128) row A was rebuilt
(phase 129) and rows A, B and C were closed on the declared carrier (phases 130–133).

**Row D (phases 134–209).** The sign. Row D is the statement
$$\lambda_A(T)=\inf\{A(F,F): F\in P_T,\ \|F\|=1\}\ \ge 0,$$
the positivity of the window form $A$ (Paper 47, eq. `eq:Aform`) on the space $P_T$ of admissible
test functions supported in $[-T,T]$, with prime weights $v_n=2\Lambda(n)/\sqrt n$. It is treated
as a target in its own right.

## 3. What is proved about row D (Paper 47)

- **Dual theory.** The archimedean multiplier is a Lévy exponent (complete Bernstein in $\tau^2$);
  strong duality with finitely atomic dual sequences; non-attainment; the Wiener–Hopf
  Euler–Lagrange equation; every sum-of-squares certificate is the explicit formula on flat-top
  tests.
- **Certificates.** Explicit certificates prove $\lambda_A(T)>0$ for $T\le\tfrac12\log 3$, then
  $\tfrac12\log5$ (certified interval arithmetic, independent reruns); the current frontier
  $T\le\tfrac12\log15$ is due to Mori and is cited.
- **Finite reduction.** $\lambda_A(T)>0$ is equivalent to positive definiteness of an explicit
  finite matrix $S_{T,k}$ (Theorems A/B and their corollary).
- **Barrier theorems.** Classes of methods that provably cannot produce the sign: linear and
  determinantal criteria, moment and family arguments, first-order discriminants (which are
  functionals of the extremal $h^*$ and not of the prime distribution), lattice certificates
  (rate $O(1/\log M)$), and others. Each barrier is a theorem about a declared class.
- **The node.** In the even sector, positivity reduces to one inequality on the polar orthogonal
  of an explicit finite-dimensional space: the prime fluctuation term $\Phi_T$ must dominate the
  gamma deficit $-(\mathfrak m_T+\mathfrak e_T)$ in every direction orthogonal to the polar one.
  The node is PROVED for $T\le\tfrac12\log5$ and OPEN in general (phases 205–208).

## 4. Routes attempted

About 1,400 routes towards the sign, from RH1–RH9, phases 0–209, the papers and the literature, are
indexed in `05-meta-and-planning/ROUTES-TRIED-INDEX/`, with the reason each one failed. Paper 48
classifies them on an 8×8 grid (how the arithmetic of ζ enters × which object carries it) and
states the specification any closing argument must meet.

## 5. What is proved unconditionally (selection)

- Rows A, B, C on the declared carrier (Papers 43–45).
- Row D for $T\le\tfrac12\log15$ (Paper 47; endpoint cited from Mori).
- The dual theory, finite reduction and barrier theorems of Paper 47.
- RH-independent results: the ω-class hierarchy (05), stable arithmetic fingerprints (09), the
  localized-Weil anatomy as a complete local invariant (10), the ω-information barrier (21), the
  failure of Stepanov almost periodicity of ζ in every sub-strip (32), an unconditional finite
  bottom for the localized Weil form (16).

## 6. What is open

Row D for $T>\tfrac12\log15$, and in particular the node of §3 for $T>\tfrac12\log5$. The live gate
after phase 207 is narrow: a sign step must use premises that are theorems only for logarithmic
derivatives of $L$-functions with an Euler product over all primes (so that they are not inherited
by the falsifier models), with margin compatible with the measured $e^{-15.449T}$. No candidate is
known.
