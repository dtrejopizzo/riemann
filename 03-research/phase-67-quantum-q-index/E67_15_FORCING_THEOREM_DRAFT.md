# E67.15 — The forcing theorem: what is proved, what is Omega_7 in disguise, and the real gap

**Date:** 2026-07-06.
**Role:** formulate the remaining Phase-67 statement honestly, separating the trivial part from the
content, and grounding it in the E67.15 numerical probe.

## Setup (from E67.9–E67.14)

```text
D_N = A_N^{-1/2}(A_N - P_lambda) A_N^{-1/2}     (exact whitened terminal defect)
Omega_7 at level N  <=>  ind_-(D_N) = 0.
G_q e_n = q^{2(n+y)} e_n                          (canonical pivotal K^2)
qTr_N(X;q) = Tr(G_q X) = sum_n q^{2(n+y)} X_nn
Pi_{N,-} = negative spectral projection of D_N
Q_N(q) = qTr_N(Pi_{N,-};q) = q^{2y} sum_{n=0}^{N-1} a_n (q^2)^n,   a_n = <e_n,Pi_{N,-}e_n>.
```

Architecture fixed in E67.14: keep the **exact** form `D_N`; use `q` only as a pivotal/negligible
overlay. Do NOT q-deform the form (that contaminated and fabricated: E67.12/E67.13).

## Part 1 — a theorem that is correct but essentially tautological

**Theorem FQT (finite q-trace forcing).** If `q^{-2y} Q_N(q)` is the zero polynomial in `q^2`, then
`Pi_{N,-} = 0`, hence `D_N >= 0` and `delta_N >= 0`.

**Proof.** `Pi_{N,-}` is an orthogonal projection, so `a_n = <e_n,Pi_{N,-}e_n> = ||Pi_{N,-}e_n||^2 >= 0`.
If `sum_n a_n (q^2)^n = 0` identically, every `a_n = 0`, so `Pi_{N,-} e_n = 0` for all `n`, so
`Pi_{N,-} = 0`. ∎

**Honest labelling.** FQT is valid but carries no content: it is the statement "a positive-semidefinite
projection with zero trace is zero." The pivotal `G_q` adds nothing — at `q=1` it is already
`Tr(Pi_{N,-}) = 0  <=>  Pi_{N,-} = 0  <=>  D_N >= 0`. The polynomial dressing is decoration. FQT is not
where any difficulty lives, and should not be credited as an advance.

## Part 2 — the statement that is Omega_7 in disguise, not a reduction of it

The "forcing" content is the claim that `Q_N(q) = 0`. But

```text
Q_N(q) = 0 (as polynomial)  <=>  Pi_{N,-} = 0  <=>  D_N >= 0  <=>  delta_N >= 0,
```

which is exactly `Omega_7` at level `N`. **Re-expressing `Omega_7` as a q-trace identity does not make
it a different or weaker problem.** As written, "the pivotal q-resolvent character has zero negative
residue" is `Omega_7` wearing a q-trace hat, not a reduction of it.

It becomes a genuine reduction in exactly one case: when an **independent evaluation** of

```text
R_N(z;q) = Tr(G_q (z - D_N)^{-1})
```

is supplied — a closed form from the algebra / Gamma_q / fusion that does **not** go through
diagonalizing `D_N`. That independent evaluation is the entire missing content. It does not yet exist.
Until it does, there is no reduction, only a restatement.

## Part 3 — the single-root vs multi-root gap

FQT needs the **polynomial** to vanish: the identity at `N` distinct pivotal values (multi-root).
Fusion/Verlinde structure naturally lives at **one** root of unity, giving only `Q_N(q_0) = 0`. But
`Q_N(q_0) = 0` at a single root does **not** force `Pi_{N,-} = 0`: q-trace cancellation can imitate
negligibility — this is precisely the fabrication seen in E67.13. The single-root case needs the
negligible-faithfulness bridge (E67.14), which is **unproven**. So what the quantum structure supplies
(one root) is strictly weaker than what the clean theorem needs (many roots), and closing that gap is
itself nontrivial.

## Part 4 — numerical probe (E67.15), honestly read

`z0=100-i`, `y=1`, `N=12` (script `E67_15_resolvent_probe.py`):

- zeta: `a_n = 0` for all n, `Tr(Pi_-)=0`, `Q_N=0` at every root (min-eig of `D_N` = 2e-18). Consistent.
- off-line `beta=0.8`: `a_n in [0.19, 0.89]`, `Tr(Pi_-)=6`, `Q_N != 0` at every root (0.88–3.71,
  growing with `ell`). Consistent.
- **Structure of the masses `a_n`:** ratios `a_{n+1}/a_n` are irregular (0.41, 2.11, 0.65, 1.29, 0.82,
  1.52, ...) — **no q-geometric / q-hypergeometric decay is visible.**

Reading: the framing is self-consistent (`Q_N` separates zeta from off-line), but this is the E67.9
detector, since `D_N` is diagonalized (uses zeta). It is NOT the forcing theorem. And the irregular
`a_n` are mild **evidence against** a simple closed form for `Q_N` being near: the negative-residue data
does not look like a recognizable q-character. A closed-form/fusion evaluation, if it exists, is not
sitting on the surface.

## The real open problem

```text
Find an INDEPENDENT closed form for  R_N(z;q) = Tr(G_q (z-D_N)^{-1})
from the Gamma_q/Plancherel structure of D_N -- not by diagonalizing D_N, not from
-zeta'/zeta as a partition function, not by fitting P_lambda -- and show its negative
spectral residue vanishes as a q-polynomial for every N.
```

Only that turns Part 2 from a restatement of `Omega_7` into a reduction. The E67.15 probe suggests the
form is not elementary; the honest next step is to test whether `D_N` (equivalently its resolvent
trace) has ANY q-hypergeometric / contiguous-relation structure inherited from the `Gamma_q` carrier,
before assuming a fusion identity exists.

## Status

```text
proved, tautological : FQT  (Tr of a PSD projection = 0  <=>  it is 0)
NOT a reduction       : "Q_N(q)=0" is Omega_7 restated, pending an independent eval of R_N
open gap              : single-root (fusion) is weaker than multi-root (FQT)
probe                 : framing consistent; masses a_n irregular => no obvious closed form near
real target           : closed form for R_N(z;q) from Gamma_q, independent of the zeros
```

Phase 67's honest endpoint: the right object (signed index), the right architecture (exact form +
pivotal overlay), a satisfied precondition (E67.14), and a precisely located hard problem — with no
claim that `Omega_7` has been reduced to anything easier.
