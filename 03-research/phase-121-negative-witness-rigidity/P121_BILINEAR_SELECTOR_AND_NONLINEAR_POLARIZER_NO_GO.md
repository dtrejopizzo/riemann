# Phase 121 -- bilinear radical, finite selectors, and nonlinear polarizer no-go

## Status

This note audits the most direct attempt to extract more information from a
first-contact radical: polarize against all primitive tests and use spectral
interpolation to isolate one divisor fibre.  The finite construction is
valid, but its global use was already developed in phase 116.  The new point
recorded here is that the Cartwright obstruction does not require a linear or
bounded operator: it also excludes witness-dependent same-window
polarizers.

No positivity claim is made.

## 1. What radicality really gives

At a first-loss parameter `T`, let `F` be a nonzero primitive radical and
write `q_T` for the polarized Weil form.  Since the compressed operator is
nonnegative at first contact,

\[
 q_T(F,G)=0\qquad(G\in\mathcal P_T).                 \tag{1.1}
\]

In residue coordinates this says

\[
 \langle J_{\rm res}\mathcal E_TF,\mathcal E_TG\rangle=0
 \qquad(G\in\mathcal P_T),                          \tag{1.2}
\]

or, with `R_T=E_T(P_T)`,

\[
 \mathcal E_TF\in \mathscr R_T\cap
                  (J_{\rm res}\mathscr R_T)^\perp. \tag{1.3}
\]

Thus polarization does give the whole annihilator equation, not merely the
single scalar equality `q_T(F,F)=0`.

## 2. Finite interpolation is exact and insufficient

For every finite union of divisor orbits, phase 116 v94 (606)--(608)
constructs explicit primitive Paley--Wiener cardinal sources.  Hence the
truncated evaluation map has an explicit right inverse, with no inverse of
the Weil operator.  Equations (609)--(610) even solve the finite residue
conservation equation exactly.

The obstruction is the limit.  The exact tail is v94 (611), and uniform
source control plus tail extinction is condition (612).  Theorem (613)
proves that the isolated fibrewise lift cannot have such a global limit if
an off-line orbit exists.  The reason is not a bad choice of cardinal
functions: a fixed-type Paley--Wiener function cannot vanish at the
`gg R log R` unconditional family of distinct critical zeros unless it is
zero.

Consequently (1.1) cannot be converted into an individual residue equation
by first isolating finitely many fibres and then passing to the limit.

## 3. Nonlinear critical-preservation rigidity

Let `C` be any unconditional family of distinct critical-line zeros with

\[
 N_C(R)\gg R\log R.                                 \tag{3.1}
\]

For a source `U` supported in `[-T,T]`, denote its Paley--Wiener transform
by `K_U`.

### Theorem 3.1

Fix `F,U in P_T` and a complex scalar `a`.  If

\[
 K_U(\rho-\tfrac12)=aK_F(\rho-\tfrac12)             \tag{3.2}
\]

for all `rho in C` outside a set whose counting function is `O_T(R)`, then

\[
 U=aF.                                               \tag{3.3}
\]

This remains true when `U` and `a` are chosen nonlinearly and
witness-dependently from `F`.

#### Proof

`K_U-aK_F` is a Cartwright entire function of exponential type at most
`T`.  Unless it is identically zero, its zero-counting function is
`O_T(R)`.  By (3.1)--(3.2) it has `gg R log R` zeros after removal of only
`O_T(R)` exceptions.  Therefore it is identically zero.  Injectivity of the
Paley--Wiener transform gives (3.3).  No linearity, continuity or uniformity
of the rule `F -> U` was used.  QED.

### Corollary 3.2 -- no exact same-window selector

There is no nonzero `U in P_T` whose transform vanishes at every point of
`C` except finitely many prescribed points.  In particular, an exact
global coordinate selector cannot live in the physical same-window source
space.

### Corollary 3.3 -- no witness-dependent off-line polarizer

Suppose a proposed construction assigns to a particular witness `F` a
same-window source `U_F` and is required to leave the critical residues
fixed while changing the coordinates on an off-line orbit.  Then
`U_F=F`, so none of its off-line coordinates can change.  The requested
polarization is therefore impossible whenever it is nontrivial.

This strengthens the linear full-involution no-go in v94: allowing the
source transformation to depend nonlinearly on the hypothetical radical
does not evade critical overdetermination.

## 4. Consequence for F2

The bilinear family (1.1) is not the missing noncircular input.  It is the
compressed residue equation itself.  It can be used in either of two ways:

1. finite interpolation, which leaves the uncontrolled tail (611); or
2. a global same-window polarizer, which is excluded by Theorem 3.1.

Therefore a surviving F2 mechanism may not attempt to preserve the
critical coordinates and modify the off-line coordinates through another
physical source.  It must instead prove a scalar consequence directly on
the original witness, before introducing a second same-window source.

The weakest sufficient scalar consequence remains the density form already
isolated in phase 121:

\[
 \#\{\rho\in C:|\Im\rho|\le R,
              K_F(\rho-\tfrac12)\ne0\}=o(R\log R). \tag{4.1}
\]

Cartwright then forces `F=0`.  Unlike an exact selector, (4.1) does not ask
for coordinatewise interpolation.  A noncircular proof must obtain this
sparsity from an Euler-specific nonlinear law of the equality state, not
from a lift, projection, inverse residue map or positive comparison.

## 5. Corpus verdict

The finite-selector route is not new: its complete finite construction and
its global obstruction are v94 (606)--(613).  Reverse residue sampling
v94 (642)--(643) closes the range analytically but does not change the
Cartwright obstruction.  Theorem 3.1 is the additional phase-121 closure:
the same obstruction applies to nonlinear, witness-dependent same-window
polarizers.

The result removes a false escape route; it does not close F2 or row (d).
