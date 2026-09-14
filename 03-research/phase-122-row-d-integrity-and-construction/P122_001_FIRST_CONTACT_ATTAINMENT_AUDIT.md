# P122.001 — first-contact attainment is not yet a closed dependency

## Status

`RESOLVED-BY-P122.002`, conditional on the separate audit of the strict base
certificate.  This note records the gap that had to be repaired; it did not
prove that the first-contact reduction was false.

## The conflicting repository statements

Phase 121 repeatedly treats the implication

```text
failure of global positivity
  -> a first T_* and a nonzero primitive F_* with Delta_(T_*) F_*=0
```

as proved.

However, `phase-114/114_d_54_SMALL_WINDOW_BASE_AND_NO_CREATION_AUDIT.md`,
Section 6, explicitly records the infinite-dimensional caveat: zero is an
accumulation point in the compact-kernel representation, and negative modes
may in principle be born from that accumulation while the finite-Galerkin
first-exit parameters drift, without a nonzero kernel vector at a limiting
`T_*`.  It says that a uniform Galerkin/compactness estimate is required.

The phase-121 files inspected so far cite “exact nesting” and the initial
positive interval but do not identify a later theorem discharging that
uniform attainment requirement.

## Why exact nesting alone is insufficient

Nesting preserves the value of the form on a fixed compactly supported
test.  It does not by itself give compactness of a normalized sequence whose
supports, frequencies or Galerkin dimensions vary.  Nor does an indefinite
form containing both positive and negative directions have to possess a
kernel at a fixed parameter.

At prime-power births there is an additional issue: a truncated translation
whose overlap shrinks to zero converges strongly to zero but need not
converge in operator norm.  Therefore ordinary norm-continuous eigenvalue
perturbation cannot simply be invoked across a threshold.

## Exact theorem now required

One must prove a compactness/attainment theorem with a fixed transported form
domain, including threshold behavior and the moving Tate projection.  A
valid proof may instead use a coercive reference operator with compact
resolvent and establish Mosco/norm-resolvent convergence strong enough to
prevent spectral pollution at zero.

The required theorem is now written in
`P122_002_FIRST_CONTACT_COMPACTNESS_THEOREM.md`.  It uses compactness of the
Gamma form-domain inclusion to upgrade the strong convergence of newborn
channels to norm convergence after whitening.  Thus the assertion is no
longer `AUDIT-OPEN`; its remaining dependency is the strict base certificate.

## Alternative that does not require first contact

If the fixed-window primitive operator is lower semibounded with compact
resolvent, a negative form value yields an attained eigenpair with
`lambda<0`.  The correct Euler--Lagrange equation is then

\[
 \mathscr A_TF=\lambda F+\alpha e^{-t/2}+\beta e^{t/2}.
\]

Track II of the phase plan investigates whether phase 121's nonlinear
residue mechanisms can be rebuilt for this equation.  This alternative must
not drop the `lambda F` term.
