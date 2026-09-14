# P124.006 -- retard range attack on the collar residual

Status: `PARTIAL RANGE REDUCTION / INTERIOR CORRECTOR OBSTRUCTION`.

This note attacks the residual

\[
        \rho_{+,T}=P_T(e^{t/2}\Phi_{+,T})
\]

from P124.005 by trying to write it as `L_TG+r`, where

\[
        L_T=P_T\mathscr A_TP_T,\qquad
        \mathscr A_T=G_{\Gamma,T}-m_0I-B_{T,+}-B_{T,-}.
\]

The jump calculation gives a useful partial theorem: all arithmetic jumps
of `rho_(+,T)` are matched by `L_TG` if and only if the candidate has the
two endpoint traces

\[
        G(-T+)=e^{-T/2},\qquad G(T-)=e^{T/2}.        \tag{0.1}
\]

This is the trace of `e^(t/2)`.  It is exactly the right retard boundary
datum, but `e^(t/2)` itself is a Tate vector and its primitive projection is
zero.  Therefore any admissible primitive jump matcher must be

\[
        G=e^{t/2}+h,\qquad h(\pm T)=0,
        \qquad M_\pm(e^{t/2}+h)=0.                  \tag{0.2}
\]

For every such `h`, the exact residual is

\[
        \boxed{\rho_{+,T}-L_TG=-P_T\mathscr A_T h.} \tag{0.3}
\]

Thus the arithmetic jumps are triangularized away, but the problem does
not close: it becomes a Dirichlet-moment correction problem for `h`.  The
remaining residual has no arithmetic jumps, yet it is not forced to vanish
by the first-contact equation or by the retard identities alone.

## 1. Jump formula for `L_TG`

Let `G` lie in the logarithmic Gamma form domain, have no interior jumps,
and have finite one-sided endpoint traces

\[
        g_L=G(-T+),\qquad g_R=G(T-).                \tag{1.1}
\]

The finite shift part of `\mathscr A_TG` has the only interior jumps.  The
Gamma term contributes endpoint logarithmic singularities but no finite
interior step when `G` is interior continuous.  Since the Tate projection
subtracts continuous functions, it does not change jumps.  Hence, for
`a_n=\log n` and `w_n=\Lambda(n)n^{-1/2}`,

\[
\boxed{
\begin{aligned}
\Delta_{t=T-a_n}L_TG &= w_n g_R,\\
\Delta_{t=-T+a_n}L_TG &= -w_n g_L.
\end{aligned}}                                      \tag{1.2}
\]

The target residual from P124.005 has jumps

\[
\boxed{
\begin{aligned}
\Delta_{t=T-a_n}\rho_{+,T}
 &=e^{(T-a_n)/2}\Lambda(n),\\
\Delta_{t=-T+a_n}\rho_{+,T}
 &=-e^{(-T+a_n)/2}{\Lambda(n)\over n}.
\end{aligned}}                                      \tag{1.3}
\]

Because `w_n=\Lambda(n)e^{-a_n/2}`, equations (1.2)--(1.3) agree for every
active `n` exactly when

\[
        g_R=e^{T/2},\qquad g_L=e^{-T/2}.            \tag{1.4}
\]

So the jump recursion does not produce a prime-by-prime small divisor.  It
collapses to two endpoint traces.

## 2. Endpoint logarithms are matched by the same trace

The same trace condition also matches the endpoint logarithmic part of the
Gamma collar.  Indeed P124.005 proved

\[
        \mathscr A_T^*e^{t/2}
        =e^{t/2}\Phi_{+,T}+\kappa_{+,T}e^{t/2}.     \tag{2.1}
\]

After primitive projection, this says

\[
        P_T\mathscr A_Te^{t/2}=\rho_{+,T}.          \tag{2.2}
\]

Thus the nonprimitive vector `e^(t/2)` reproduces at once:

1. the right and left arithmetic jumps in (1.3);
2. the endpoint logarithms coming from `A_T(T-t)` and `B_T(T+t)`;
3. the continuous Gamma--Euler collar potential, modulo Tate characters.

The obstruction is not local matching.  The obstruction is that
`e^(t/2)` is itself one of the two forbidden Tate directions.

## 3. Primitive jump matchers and the exact residual

Let `G` be an admissible primitive candidate satisfying the jump traces
(1.4).  Write

\[
        G=e^{t/2}+h.                                \tag{3.1}
\]

Then

\[
        h(-T+)=h(T-)=0,                              \tag{3.2}
\]

and primitivity of `G` gives the two moment equations

\[
        M_+(h)=-M_+(e^{t/2}),\qquad
        M_-(h)=-M_-(e^{t/2}).                       \tag{3.3}
\]

Conversely, any `h` in the form domain satisfying (3.2)--(3.3) gives a
primitive `G` whose `L_TG` matches every finite arithmetic jump of
`\rho_(+,T)`.

Using (2.2) and `P_TG=G`,

\[
\begin{aligned}
        L_TG
        &=P_T\mathscr A_TG\\
        &=P_T\mathscr A_Te^{t/2}+P_T\mathscr A_Th\\
        &=\rho_{+,T}+P_T\mathscr A_Th.
\end{aligned}                                      \tag{3.4}
\]

Therefore

\[
\boxed{
        \rho_{+,T}-L_TG=-P_T\mathscr A_Th.}
        \tag{3.5}
\]

This is the exact residual after the retard jump matching.  It is smaller
only in the sense that it has no forced arithmetic jumps: `h` has zero
endpoint trace, so the active shifts create no activation jumps, and the
zero extension of `h` creates no endpoint Gamma jump.  The residual still
contains the full signed Gamma--Euler action of the interior correction.

## 4. Concrete correctors exist, but they do not solve the range problem

Choose two smooth bump functions `\eta_+,\eta_-` supported strictly inside
`I_T` such that the matrix

\[
        \left(M_\sigma(\eta_\tau)\right)_{\sigma,\tau\in\{+,-\}}
\]

is invertible.  Solving the two-by-two system gives constants
`c_+,c_-` for

\[
        h_0=c_+\eta_+ + c_-\eta_-                  \tag{4.1}
\]

so that (3.3) holds.  Then

\[
        G_0=e^{t/2}+h_0                             \tag{4.2}
\]

belongs to the logarithmic Gamma form domain, is primitive, has the correct
endpoint traces, and matches all jumps of `rho_(+,T)`.

However, the residual is explicitly

\[
        r_0=\rho_{+,T}-L_TG_0=-P_T\mathscr A_T h_0. \tag{4.3}
\]

There is no cancellation in (4.3) coming from the retard identities.
Because `h_0` is compactly supported in the interior, the shift part of
`\mathscr A_Th_0` is an ordinary finite sum of interior translates and the
Gamma part is the closed logarithmic operator applied to an interior
smooth function.  This residual is a regular primitive bulk term, not a
boundary collar term.

Thus jump matching alone converts the collar obstruction into the problem
of finding a nonzero interior corrector `h` satisfying

\[
        P_T\mathscr A_T h=0                         \tag{4.4}
\]

together with the moment equations (3.3) and zero endpoint trace.  That is
not a triangular retard recursion; it is an interior null equation for the
same signed operator.

## 5. Why the naive iteration is not a contraction

One might try to iterate

\[
        r_k=-P_T\mathscr A_T h_k,\qquad
        \rho_{+,T}=L_T(e^{t/2}+h_k)+r_k,
\]

and choose a new zero-trace correction `h_(k+1)` to cancel `r_k`.  This
requires solving

\[
        P_T\mathscr A_T h_{k+1}=r_k                 \tag{5.1}
\]

on the zero-trace, two-moment affine class.  No Volterra ordering is
available in (5.1):

* the finite Euler part contains both `S_{\log n}` and `S_{-\log n}`;
* the Gamma part is the two-sided logarithmic multiplier;
* the Tate projection is global and re-inserts both exponential moments.

In Fourier language, even before projection, (5.1) asks one to divide by
the full signed symbol

\[
        g_\Gamma(\tau)-m_0
        -\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
          \left(e^{i\tau\log n}+e^{-i\tau\log n}\right),
        \tag{5.2}
\]

with compact-window and moment constraints.  At a first-contact parameter
the compressed operator has a kernel by hypothesis.  Therefore a bounded
inverse or contraction estimate for (5.1) would have to exclude the kernel
projection of the right-hand side.  That exclusion is exactly the desired
collar cancellation, not a consequence of the jump recursion.

## 6. Dual-Euler support anomaly test

D.240 gives the strongest available non-scalar identity near this problem.
Before support cutoff, the dual Euler maps satisfy

\[
        \theta_\sigma^*\eta_\sigma=I,
        \tag{6.1}
\]

and differentiating gives the exact conservation of the completed
Euler--Gamma logarithmic metric derivative.  Let `\chi_T` be the support
projection onto `I_T` and `N_T=I-\chi_T`.  After cutoff,

\[
\chi_T\theta_\sigma^*\chi_T\eta_\sigma\chi_T
=\chi_T-\chi_T\theta_\sigma^*N_T\eta_\sigma\chi_T.
\tag{6.2}
\]

Thus the localized derivative is paid by the support anomaly

\[
        \mathfrak D_{T,\sigma}
        :=\chi_T\theta_\sigma^*N_T\eta_\sigma\chi_T.
        \tag{6.3}
\]

Testing the derivative of (6.2) at `sigma=1/2` against the positive Tate
character gives exactly the full collar functional:

\[
        \left\langle
        \left.\partial_\sigma\right|_{1/2}
        \mathfrak D_{T,\sigma}F,\phi_+
        \right\rangle
        =-\langle b^{full}_{+,T},F\rangle .         \tag{6.4}
\]

After imposing `M_+(F)=0` and then projecting away both Tate characters,
(6.4) becomes

\[
        \left\langle
        \left.\partial_\sigma\right|_{1/2}
        \mathfrak D_{T,\sigma}F,\phi_+
        \right\rangle
        =-\langle\rho_{+,T},F\rangle
        \qquad(F\in\mathcal P_T).                  \tag{6.5}
\]

So the D.240 support defect does not mismatch the collar residual: it is
the same object with one exterior leg fixed to `\phi_+`.

This identification still does not prove orthogonality at first contact.
The anomaly in (6.3) is an exterior support block.  Its quadratic
Frobenius-seam descendant is the ANOVA/seam defect of phase 120, but that
defect is known only as a positive detector; first contact does not make it
zero.  Therefore D.240 converts `rho_(+,T)` into the exact support anomaly,
not into a range vector for `L_T`.

## 7. First-contact consequence

Let `F_*` be a first-contact minimizer:

\[
        F_*\in\mathcal P_T,\qquad L_TF_*=0,\qquad L_T\ge0.
\]

For every primitive jump matcher `G=e^(t/2)+h` satisfying (3.2)--(3.3),
equation (3.5) gives

\[
\boxed{
        J_+(F_*)=\langle\rho_{+,T},F_*\rangle
        =-\langle P_T\mathscr A_T h,F_*\rangle.}
        \tag{7.1}
\]

If `h` belongs to the operator domain, symmetry gives the exact value of
the right side rather than a vanishing:

\[
\begin{aligned}
-\langle P_T\mathscr A_T h,F_*\rangle
&=-\langle h,\mathscr A_TF_*\rangle\\
&=-\alpha M_-(h)-\beta M_+(h).
\end{aligned}                                      \tag{7.2}
\]

Using the moment equations (3.3),

\[
        -\alpha M_-(h)-\beta M_+(h)
        =\alpha M_-(e^{t/2})+\beta M_+(e^{t/2}).
        \tag{7.3}
\]

This is exactly the crossed Tate multiplier contribution already measured
by `J_+(F_*)`.  It does not vanish unless the desired Tate coefficient
vanishes.  Projecting `h` before applying `L_T` would make it primitive,
but then `e^(t/2)+P_Th` no longer has the endpoint traces (1.4) and the
jump matching is lost.

Equivalently, the formal proof would need a corrector satisfying all four
conditions

\[
\begin{cases}
h(\pm T)=0,\\
M_\pm(h)=-M_\pm(e^{t/2}),\\
P_T\mathscr A_Th=0,\\
h\ \text{is in the operator domain needed for symmetry against }F_*.
\end{cases}                                          \tag{7.4}
\]

This is the exact obstruction isolated by the range attack.  The first two
lines are elementary and solvable; the third is a homogeneous signed
Gamma--Euler equation with prescribed nonzero Tate moments; the fourth is
the domain requirement that prevents treating a formal anti-dual identity
as a proof.

The D.240 anomaly calculation explains why this happens.  The support
defect with one Tate leg is exactly `rho_(+,T)`, and the nonprimitive
corrector `h` couples to the Tate normal component of `\mathscr A_TF_*`.
The first-contact equation kills primitive range vectors only; it does not
kill this exterior/Tate support anomaly.

## 8. Verdict

The retard attack proves a partial positive result and a concrete
obstruction.

Positive result: all jumps and endpoint Gamma logarithms of the collar
kernel are matched by the nonprimitive vector `e^(t/2)`, and by every
primitive vector `e^(t/2)+h` with zero endpoint trace and the two moment
corrections (3.3).

Obstruction: after this exact matching, the residual is not another
smaller collar.  It is

\[
        -P_T\mathscr A_Th,
\]

where `h` is the mandatory interior corrector used to make the boundary
trace lift primitive.  Eliminating that residual requires solving the
interior equation (7.4), or proving a signed range estimate for it.  The
retard identities alone provide no convergent triangular iteration and no
kernel-projection cancellation at first contact.

D.240 identifies the same residual as the differentiated support anomaly
`\partial_\sigma(\chi_T\theta_\sigma^*N_T\eta_\sigma\chi_T)` with one Tate
leg.  This is a real identification, not a mismatch, but it leaves a free
support-defect term.  The phase-120 seam ANOVA can measure its quadratic
descendant; using that measurement to set it to zero would assume the
missing seam law.
