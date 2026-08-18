# D.171 — Hadamard phase-defect counter-scaling

## Verdict

D.164--D.167 do not imply the output-capacity inequality of D.170.  The
failure already occurs in one exact spectral fibre of the Hadamard
(J_\pm) rotation, even after the old comparison is contractive and all
unweighted boundary Grams are fixed.

For a unitary translation with spectral value (e^{i\theta}),

\[
 |J_+(\theta)|^2=1+\cos\theta,\qquad
 |J_-(\theta)|^2=1-\cos\theta.                        \tag{0.1}
\]

After normalizing by the positive (J_-) reference, the old comparison
has scalar modulus

\[
 |A(\theta)|^2={1+\cos\theta\over1-\cos\theta}.       \tag{0.2}
\]

On the contractive half-circle (cos\theta\le0), its output defect is

\[
 d(\theta)=1-|A(\theta)|^2
 ={ -2\cos\theta\over1-\cos\theta}.                  \tag{0.3}
\]

As (\(\theta\downarrow\pi/2\)) from the contractive side,
(d(\theta)\downarrow0), although both quantities in (0.1) stay bounded
above and below.  Hence a boundary-load column (y) of fixed unweighted
size has

\[
 y^*(I-AA^*)^{-1}y={|y|^2\over d(\theta)}\longrightarrow\infty.      \tag{0.4}
\]

The exact additional theorem is therefore not another norm estimate.  It
is a **phase-defect Carleson estimate** forcing the centered boundary load
to lose mass at least linearly at every almost-balanced Hadamard phase.

## 1. Exact one-fibre construction

Fix (\(0<\epsilon<1\)) and choose
(\(\theta_\epsilon\in(\pi/2,\pi)\)) by

\[
 \cos\theta_\epsilon=-{\epsilon\over2-\epsilon}.      \tag{1.1}
\]

Then (0.2)--(0.3) give exactly

\[
 |A(\theta_\epsilon)|^2=1-\epsilon,\qquad
 d(\theta_\epsilon)=\epsilon.                        \tag{1.2}
\]

Let the new normalized boundary load be the scalar

\[
 y_\epsilon=\epsilon^{1/4}.                           \tag{1.3}
\]

Its ordinary Gram tends to zero,

\[
 |y_\epsilon|^2=\epsilon^{1/2}\to0,                  \tag{1.4}
\]

so it satisfies every fixed unweighted bound, including a bound much
stronger than the leading ((1/2)\log N) estimate of D.167.  Nevertheless

\[
 \boxed{
 y_\epsilon^*d(\theta_\epsilon)^{-1}y_\epsilon
 =\epsilon^{-1/2}\to\infty.}                         \tag{1.5}
\]

The input cross is still exactly of D.170 form,

\[
 z_\epsilon=A(\theta_\epsilon)^*y_\epsilon,           \tag{1.6}
\]

and its ordinary norm also tends to zero.  Thus the counter-scaling
respects the exact output-channel factorization (z=A^*y); it is not the
abstract counterexample of D.168 pasted onto an unrelated model.

Two Tate directions may be adjoined as an orthogonal two-plane and then
shorted.  The fibre (1.1) lies in the remaining primitive summand, so this
does not change any equation above.  Direct sums with the other
prime-power fibres and with a positive Gamma channel likewise preserve
(1.5).  Therefore neither codimension two nor the presence of all the
other correctly signed channels repairs an estimate which has no control
at the balanced phase.

## 2. Why (V_N\pm H_N) do not see the failure

For a spectral measure (d\mu(\theta)), the two raw Hadamard Grams are

\[
 \int(1+\cos\theta)d\mu,\qquad
 \int(1-\cos\theta)d\mu.                             \tag{2.1}
\]

D.164 computes their finite arithmetic analogues exactly as
(V_N+H_N) and (V_N-H_N).  At
(\(\theta=\theta_\epsilon\)), both integrands in (2.1) tend to one.  Hence
the two Grams remain uniformly comparable while (0.3) tends to zero.

D.167 adds the pure-Gamma inverse weight and proves the correct leading
unweighted size of the boundary synthesis.  But its weight is
(h_{5/4}^{-1}), not (d(\theta)^{-1}).  A direct sum may keep the Gamma
frequency and (h_{5/4}) fixed while moving only the Hadamard phase to
(\(\theta_\epsilon\)).  Thus the pure-Gamma estimate cannot control (1.5).

This proves, by a model using the actual (J_\pm) functions, that the
output defect contains information absent from D.164--D.167.

## 3. Exact missing weighted inequality

Let (D_{\rm out}=I-A_NA_N^*), let (E_N^{\rm out}) be its spectral
measure, and define the boundary-load operator measure

\[
 \mu_N^y(B)=y_N^*E_N^{\rm out}(B)y_N.                 \tag{3.1}
\]

The desired capacity is exactly

\[
 y_N^*D_{\rm out}^\dagger y_N
 =\int_{(0,1]}{1\over d}\,d\mu_N^y(d).               \tag{3.2}
\]

Consequently the additional estimate required beyond D.164--D.167 is

\[
 \boxed{
 \int_{(0,1]}{1\over d}\,d\mu_N^y(d)\le I,}          \tag{3.3}
\]

after the boundary reference is normalized.  A sufficient layer estimate
with explicit summability is, for example,

\[
 \mu_N^y((0,2^{-j}])
 \le C_N\,2^{-j}(1+j)^{-2},\qquad j\ge0,             \tag{3.4}
\]

with the constants summing inside the available capacity budget.  Merely
having
(\(\mu_N^y((0,2^{-j}])=O(2^{-j})\)) is borderline and loses a logarithm when
inserted in (3.2).

In the simultaneous Hadamard spectral model, (3.3) becomes

\[
 \int_{\{\cos\theta<0\}}
 {1-\cos\theta\over-2\cos\theta}
 |y_N(\theta)|^2d\mu_N(\theta)\le I,                 \tag{3.5}
\]

with the full Gamma and Tate terms changing the exact defect denominator
but not the principle: the denominator is the complete old-cell defect,
not the raw (J_-) energy.  The singular set is the zero set of that
complete defect.

## 4. Where the atomic discrepancy enters

The continuous polynomial (M_N) removed by the two Tate moments supplies
the smooth Hadamard balance.  The centered polynomial

\[
 E_N=W_N-M_N                                             \tag{4.1}
\]

determines how much of the actual boundary column lies near the balanced
phases of the old comparison.  D.167 bounds its Gamma-weighted mean.  To
close D, one must prove the stronger defect-weighted estimate

\[
 \boxed{
 \int { |E_N(\theta)|^2\over d_N(\theta)}
       \,d\nu_N(\theta)\le\text{available boundary capacity},}      \tag{4.2}
\]

where (d_N) is the complete output defect and the formula is interpreted
operatorially when the channels do not commute.

Equation (4.2) is not a reformulation of a pure-Gamma norm: the example
(1.1)--(1.5) proves the strict logical gap.  It is the concrete new
inequality that an endpoint-flat or de Branges--Rovnyak construction must
establish.

The ancillary `114_d_171_hadamard_phase_counterexample.py` verifies
(0.1)--(1.6), keeps both raw Grams uniformly bounded, and demonstrates the
divergent output capacity over twelve orders of defect size.
