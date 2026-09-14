# P122.010 — second-order reciprocity curvature no-go

## Verdict

Differentiating the tame-symbol product formula to second order does not
produce the positive critical square.  The logarithmic norm of a
holomorphic unit is pluriharmonic, so its mixed Hermitian curvature
vanishes.  A nonzero `|c|^2` term requires an additional curved metric,
which is new D data rather than a consequence of reciprocity.

## 1. The tempting argument

At a divisor point the oriented infinitesimal unit is

\[
 u_c(z)=1+zc,
\]

with `c=K_F(lambda)`.  Since

\[
 |u_c(z)|^2=1+zc+\bar z\bar c+|z|^2|c|^2,
\]

the raw mixed derivative at zero contains `|c|^2`.  One might hope that a
second variation of a global product formula sums these positive terms and
forces them to vanish.

## 2. Exact cancellation in the multiplicative invariant

Product formulas linearize after taking logarithms.  Locally,

\[
 \log|u_c(z)|^2
 =\log(1+zc)+\log(1+\bar z\bar c).                   \tag{2.1}
\]

Therefore

\[
 \partial_z\partial_{\bar z}
 \log|u_c(z)|^2\big|_{z=0}=0.                       \tag{2.2}
\]

The apparent positive term in the raw norm is cancelled exactly by the
quadratic term in the logarithm.  This is simply the pluriharmonicity of
the log modulus of a nonvanishing holomorphic function.

Consequently differentiating

\[
 \sum_x\log|\partial_x\kappa(z)|=0                  \tag{2.3}
\]

cannot yield `sum_x |c_x|^2=0`.  Its mixed second variation is again
`0=0` away from a change of divisor.

## 3. Relation to the phase-121 critical square

The negative-half defect

\[
 8\pi\sum_\rho |K_F(i\gamma)|^2                     \tag{3.1}
\]

is a genuine positive Hermitian square.  It is not the curvature of the
flat multiplicative tame-symbol norm.  To derive (3.1) from a determinant
line one would have to equip that line with a non-flat Hermitian/Quillen
metric whose curvature has exactly the critical residue term and prove a
global sign/equality theorem for it.

That metric cannot be selected by requiring its curvature to equal (3.1):
this would define the desired square from the target.  It must arise from a
source complex before comparison and must fail on Davenport--Heilbronn or
the shifted rank-two pair for an independently checkable reason.

## 4. Consequence

Neither first-order nor second-order bare reciprocity closes F2:

```text
first variation  -> sum c_x = 0, permits (c,-c)
mixed second variation of log norm -> 0, no |c_x|^2
positive curvature -> possible only with a new metric/Hodge theorem.
```

This leaves the D-geometry route precise: construct the curved metric and
prove its index/effectivity theorem independently.  Formal `K_2`
reciprocity by itself is exhausted.
