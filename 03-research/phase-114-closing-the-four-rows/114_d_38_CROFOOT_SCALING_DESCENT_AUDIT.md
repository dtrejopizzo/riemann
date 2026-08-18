# D.38 — Crofoot scaling and Poisson-descent audit

## 1. Purpose

D.34 identifies every finite prime-power contribution with a Crofoot
model-space defect, and D.37 equips the doubled finite model space with a
positive complex structure.  This note tests whether that finite complex
structure can itself be the scaling-equivariant Weil operator on Meyer's
Poisson cokernel.

The answer is negative for the literal blockwise construction.  This does
not affect the exact pullback of `B_nuc`; it shows that the global Weil
operator cannot be obtained by taking the orthogonal direct sum of the
local Crofoot operators and then passing formally to a quotient.

## 2. Exact local commutator

Fix `0<r<1`, `L>0`, and put

\[
 \theta(\tau)=e^{iL\tau},\qquad
 c(\tau)=\frac{\sqrt{1-r^2}}{1-r e^{iL\tau}} .       \tag{2.1}
\]

The local Crofoot unitary is multiplication by `c` from
`K_theta` to `K_(b_r circle theta)`.  Let horizontal translation be

\[
 (T_s f)(\tau)=f(\tau-s).                            \tag{2.2}
\]

The source model space is translation invariant because
`theta(tau-s)=e^(-iLs)theta(tau)`, so multiplication of the inner function
by this scalar does not change its model space.  On `K_theta`, direct
calculation gives

\[
 (T_s C_r-C_rT_s)f(\tau)
  =\bigl(c(\tau-s)-c(\tau)\bigr)f(\tau-s).           \tag{2.3}
\]

Moreover

\[
 c(\tau-s)-c(\tau)
 =\sqrt{1-r^2}\,
   \frac{r e^{iL\tau}(e^{-iLs}-1)}
   {(1-r e^{iL(\tau-s)})(1-r e^{iL\tau})}.          \tag{2.4}
\]

Hence the commutator vanishes for every `f` if and only if

\[
 e^{iLs}=1.                                          \tag{2.5}
\]

For a prime block, `L=log p`; consequently the Crofoot map intertwines
only the discrete subgroup `s in (2 pi/log p) Z`, not the full real scaling
group.

## 3. The target model space is not translation invariant

Write `beta=b_r circle theta`.  Horizontal translation carries `K_beta`
unitarily onto `K_(beta(.-s))`.  Equality with `K_beta` would force

\[
 \beta(\tau-s)=\eta\beta(\tau)                       \tag{3.1}
\]

for a unimodular constant `eta`, because two scalar inner functions have
the same model space exactly when they differ by a unimodular constant.
Set `z=e^{iL tau}` and `a=e^{-iLs}`.  Equation (3.1) would say

\[
 \frac{az-r}{1-raz}
   =\eta\frac{z-r}{1-rz}.                            \tag{3.2}
\]

Comparing the constant and quadratic coefficients gives `eta=1` and
`a=1`.  Thus (3.1) also holds only under (2.5).  In particular, the target
block in D.37 does not carry the required continuous scaling action.

## 4. Why a direct Gamma summand cannot cancel the defect

In the finite construction of D.37 the prime blocks and the Gamma
oscillator are orthogonal summands and scaling acts place by place.  Let
`pi_p` be the orthogonal projection onto the `p`-block.  For a vector
supported in that block,

\[
 \pi_p[T_s,J_P]v=[T_s,J_p]v.                         \tag{4.1}
\]

The right side is nonzero for generic `s` by (2.3)--(2.5).  A commutator
on the orthogonal Gamma summand has zero `p`-projection and therefore
cannot cancel (4.1).  Cancellation could occur only after a genuinely
global Poisson gluing that mixes the places.  It is not a property of the
blockwise direct sum.

## 5. Type correction for the descent problem

The expression

\[
 J_Q(Z\mathcal H_\cap\cap V_Q)\subseteq
 Z\mathcal H_\cap\cap V_Q                            \tag{5.1}
\]

is not yet well typed: `J_Q` acts on the finite Crofoot--Gamma boundary
module, whereas `Z H_cap` is a subspace of Meyer's source-defined
Frechet representation.  D.34 supplies equality of quadratic traces, not
an embedding of either space into the other.

A valid descent datum must first construct a continuous comparison map

\[
 q_Q:\mathbb H_Q^{\rm Crofoot\text{-}Gamma}
       \longrightarrow V_Q                           \tag{5.2}
\]

onto a finite Poisson quotient, compatible with the transition maps and
the real scaling action.  Only then does descent have the precise form

\[
 J_Q(\ker q_Q)\subseteq\ker q_Q,                     \tag{5.3}
\]

and the descended operator must be checked to commute with scaling.  The
local computation above proves that `q_Q` cannot be the block-diagonal
identification implicit in the trace formula.

## 6. Surviving route

The exact `p^k`, Gamma, and two-jet comparison remains valid.  What this
audit removes is only the attempted local construction of the global Weil
operator.  The next construction must start from the Poisson relation

\[
 Zf=\mathscr J Z\mathcal Ff\qquad(f\in\mathcal H_\cap)             \tag{6.1}
\]

and build a global operator on the range--cokernel triangle before
decomposing its trace into local places.  Its local trace must recover the
Crofoot and Gamma blocks, but its action cannot be their orthogonal direct
sum.  This is a sharper target than (5.1): it demands an actual
scaling-equivariant comparison map and prevents a false formal descent.

