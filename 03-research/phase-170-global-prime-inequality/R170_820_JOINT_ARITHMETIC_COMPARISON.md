# R170_820 — Joint comparison of PC at two scales

Continuation of R170_819 and priority 2 of R170_818.
The complete Poisson–Chebyshev identity is conjugated, including the
Poisson defect and both collars, before comparing scales. The result
corrects a possible false lead: dilation does not break the
cancellation \(\Lambda*1=\log\) inside the hyperbola. The comparison
leaves an explicit joint remainder, but not a new one-sided inequality.
Neither RH nor the sign of \(\Phi+E_\rho\) is proved.

## 1. Complete conjugation

Let

\[
 (D_\rho f)(t)=\rho^{-1/2}f(t/\rho),\qquad 0<\rho<1,
 \quad O^{(\rho)}=D_\rho^*OD_\rho .
\]

On the Schwartz kernel,

\[
 X^{(\rho)}=\rho X,\qquad
 \tau_a^{(\rho)}=\tau_{a/\rho},\qquad
 \mathscr F_\rho=D_\rho^*\mathscr FD_\rho,
 \qquad J^{(\rho)}=J.                                  \tag{1}
\]

We define, conjugating each PC operator,

\[
\begin{aligned}
 S_N^{(\rho)}&=\sum_{n\le N}n^{-1/2}\tau_{\log n/\rho},&
 K_N^{(\rho)}&=\sum_{n\le N}(\log n)n^{-1/2}
                    \tau_{\log n/\rho},\\
 L_M^{(\rho)}&=\sum_{d\le M}\Lambda(d)d^{-1/2}
                    \tau_{\log d/\rho},&
 A_M^{(\rho)}&=m(D/\rho)-
                   (L_M^{(\rho)}+L_M^{(\rho)*}),\\
 E_N^{(\rho)}&=S_N^{(\rho)}\mathscr F_\rho-JS_N^{(\rho)},&
 H_{M,N}^{(\rho)}&=L_M^{(\rho)}S_N^{(\rho)}-K_N^{(\rho)}.
\end{aligned}                                           \tag{2}
\]

Here it is essential to also conjugate \(X\) and \(\mathscr F\). We have

\[
 [\rho X,S_N^{(\rho)}]=-K_N^{(\rho)},                  \tag{3}
\]

and the unitary conjugation of PC gives the exact identity

\[
\boxed{
 S_N^{(\rho)}A_M^{(\rho)}\mathscr F_\rho
 =\{\rho X,E_N^{(\rho)}\}
  -L_M^{(\rho)*}E_N^{(\rho)}
  -JH_{M,N}^{(\rho)}
  -H_{M,N}^{(\rho)}\mathscr F_\rho .}
                                                               \tag{PC\(_\rho\)}
\]

This formula is a new identity only in a bookkeeping sense: it is PC
unitarily conjugated, not a new estimate.

## 2. The divisor cancellation survives intact

In the product appearing in (2),

\[
 \tau_{\log d/\rho}\tau_{\log m/\rho}
   =\tau_{\log(dm)/\rho}.                               \tag{4}
\]

Consequently the coefficient of
\(k^{-1/2}\tau_{\log k/\rho}\) in
\(L_M^{(\rho)}S_N^{(\rho)}\) is

\[
 \sum_{\substack{dm=k\\d\le M,\ m\le N}}\Lambda(d).
\]

If \(M\ge N\), for \(k\le N\) every divisor appears and

\[
 \sum_{d\mid k}\Lambda(d)=\log k.                     \tag{5}
\]

Thus,

\[
\boxed{
 H_{M,N}^{(\rho)}
 =\sum_{N<k\le MN}h_{M,N}(k)k^{-1/2}
       \tau_{\log k/\rho},}
\quad
 h_{M,N}(k)=
 \sum_{\substack{dm=k\\d\le M,\ m\le N}}\Lambda(d)\ge0. \tag{6}
\]

The coefficients are exactly the same as at scale one. There is no
interior remainder with coefficient \(\log d/\rho\): that term would
only appear if one translation were scaled and the other left unscaled,
an operation that is not the PC conjugation. This corrects the
statement in R170_819 according to which the scaled shifts would no
longer form the full hyperbola.

## 3. Exact subtraction of the two identities

Set

\[
 \Delta E=E_N^{(\rho)}-E_N,\quad
 \Delta L=L_M^{(\rho)}-L_M,\quad
 \Delta H=H_{M,N}^{(\rho)}-H_{M,N},\quad
 \Delta\mathscr F=\mathscr F_\rho-\mathscr F.
\]

Subtracting \(\mathrm{PC}\) from \(\mathrm{PC}_\rho\), without
estimating its terms, gives

\[
\begin{aligned}
 &S_N^{(\rho)}A_M^{(\rho)}\mathscr F_\rho
       -S_NA_M\mathscr F                                      \\
 ={}&(\rho-1)\{X,E_N\}+\rho\{X,\Delta E\}                    \\
 &-\Delta L^*E_N-L_M^{(\rho)*}\Delta E                       \\
 &-J\Delta H-\Delta H\mathscr F-H_{M,N}^{(\rho)}\Delta\mathscr F.
                                                               \tag{7}
\end{aligned}
\]

In particular, the scale tail appears grouped as

\[
 \Delta H
 =\sum_{N<k\le MN}\frac{h_{M,N}(k)}{\sqrt k}
   \left(\tau_{\log k/\rho}-\tau_{\log k}\right).       \tag{8}
\]

Formula (7) is the requested joint comparison: it preserves the Poisson
defect, the prime–defect product, both collar orientations, and the
change of the local transform. Separating \(\Delta H\) from \(\Delta E\)
via absolute values again produces the size loss observed in R170_816;
(7) does not authorize that separation.

The Tate port is not part of PC as an operator identity. If \(g\) is
fixed and we take

\[
 v_\rho=S_N^{(\rho)}\mathscr F_\rho g,
 \qquad v=S_N\mathscr Fg,
\]

then the comparison is between
\(a_M^{(\rho)}(F,v_\rho)\) and \(a_M(F,v)\). For the affine functionals,
with the same vector \(r\), one must add the corrector

\[
 \Delta_{\rm Tate}(r;v_\rho,v)
   =-\Re\langle r,v_\rho-v\rangle.                       \tag{9}
\]

If instead of keeping \(r\) fixed one conjugates the whole functional,
then \(r_\rho=D_\rho^*r\), and (9) gets absorbed by unitary invariance.
Leaving the term out, or replacing \(S_N^*r\) by \(S_Nr\), would produce
a comparison different from that of the contact.

## 4. The two possible comparisons must not be mixed

There are two legitimate uses of (7).

**Conjugation of all the data.** If \(F,r,g\) are simultaneously
replaced by their conjugates and all operators are conjugated, the
resulting scalar is identical to the original one. For example,

\[
 \langle D_\rho^*u,D_\rho^*OD_\rho D_\rho^*v\rangle
   =\langle u,Ov\rangle.                                 \tag{10}
\]

In this case PC and \(\mathrm{PC}_\rho\) produce no difference that
could carry a sign: they are just two coordinates of the same number.

**Fixed contact data.** To create a nontrivial subtraction one keeps at
least \(F\), \(r\), or the exterior test fixed. Then exactly (7)
remains, together with (9). But the scaled tests are nonlocal. The weak
equation of the first contact makes \(e_F(v)=0\) for every test in
\(Q_{\log}\) supported on \(I_T\); the identity \(a_M(F,v)=0\) without
the port \(r\) corresponds only to primitive tests. None of these
claims annihilates
\(D_\rho^*S_N\mathscr FS_LF\),
\(S_N^{(\rho)}\mathscr F_\rho g\), nor their differences. The window's
minimality likewise assigns no sign to these directions.

Hence conjugating everything gives a scalar tautology, while keeping
the data fixed gives a real but uncontrolled remainder. Using unitary
invariance in the second case would mean mixing both comparisons.

## 5. What sign the subtraction yields

None of the new blocks has a sign from its coefficients. For example,
the symmetric part of a term in (8) has a real multiplier proportional
to

\[
 \cos((\log k)\xi/\rho)-\cos((\log k)\xi),               \tag{11}
\]

which changes orientation with the frequency. The positivity of
\(h_{M,N}(k)\) does not turn (8) into a positive form. The change in
\(E_N\), in \(\mathscr F\), and the Tate term are precisely the terms
that a deeper cancellation would have to correlate with (8).

Applied to the bridge (8) of R170_819, a sufficient bound would have
the form

\[
 \Re e_G(z)+h^{-1}\Re a_M(\delta,\mathcal RF)\le0.       \tag{12}
\]

Subtraction (7) allows jointly rewriting the first term at two scales,
but it does not turn the second term into one of its collars. In
particular, the proved energy

\[
 a_M(\delta,\delta)=hE_\rho(F)\ge0                       \tag{13}
\]

does not appear as the negative of (7). Achieving (12) would still
require a law that, restricted to the first-contact radical,
correlates

\[
 \Delta E,\quad \Delta H,\quad \Delta\mathscr F,\quad
 \Delta_{\rm Tate},\quad
 a_M(\delta,\mathcal RF).                                \tag{14}
\]

No such law has been derived. Declaring the right-hand side of (7)
nonpositive would amount to introducing the sought inequality, not to
deriving it from \(\Lambda*1=\log\).

## 6. Result and concrete remainder

The comparison does yield three exact conclusions:

1. PC is covariant under dilation only if
   \(X,\mathscr F,S_N,L_M,K_N\) and the two collars are scaled jointly.
2. The cancellation \(\Lambda*1=\log\) remains complete for \(k\le N\),
   and \(H_{M,N}^{(\rho)}\) keeps the same tail coefficients.
3. The uncancelled difference is the joint block (7), plus the Tate
   corrector (9) when the contact vector is kept fixed.

The missing edge of the puzzle is not an additional repair of the
hyperbola. It is a one-sided bound for (7), (9), and the alignment
error of R170_819 on first-contact vectors. The divisor identity
correctly reduces the arithmetic to the tail, but it does not fix that
tail's correlations with the Poisson defect nor with the interior
contraction.
