# D.140 — The positive theta quotient and its exact Cauchy defect

## Verdict

Although D.139 rules out a nondegenerate positive metric making the theta
operator pair symmetric on the full source, there is a canonical positive
quotient metric.  Let

\[
 k=e^{-\phi},\qquad L=-i(\partial+\phi'),\qquad
 Q=I-{|k\rangle\langle k|\over\|k\|^2}.               \tag{0.1}
\]

Since \(\ker L=\mathbb Ck\), the formula

\[
 \langle Lu,Lv\rangle_{\rm q}:=\langle Qu,Qv\rangle_{L^2} \tag{0.2}
\]

is well defined and positive on \(\mathrm{Ran}\,L\).  Its failure to
make \((LD,L)\) symmetric is the rank-two boundary form

\[
 \Omega(u,v)=
 {-\langle Du,k\rangle\langle k,v\rangle
 +\langle u,k\rangle\langle k,Dv\rangle\over\|k\|^2}. \tag{0.3}
\]

For the theta eigenfunction \(u_\alpha\) attached to
\(\Xi(\alpha)=0\), put \(b=\mathrm{Im}\,\alpha\),
\(N=\|k\|^2\), \(z_\alpha=\langle u_\alpha,k\rangle\), and
\(J_\alpha=\|u_\alpha\|^2\).  Direct Fourier calculation gives

\[
 \boxed{\Omega(u_\alpha,u_\alpha)
 ={2ib\over N}\bigl(|z_\alpha|^2-NJ_\alpha\bigr).}    \tag{0.4}
\]

The Cauchy--Schwarz inequality is strict:

\[
 |z_\alpha|^2<NJ_\alpha.                              \tag{0.5}
\]

Hence (0.4) is nonzero for every non-real zero and has sign opposite to
\(\mathrm{Im}\,\alpha\) after division by \(2i\).  For a real zero it
vanishes.  The quotient metric is therefore an exact off-line detector,
not a proof that the defect vanishes.

The two boundary coordinates in (0.3) are
\(\langle u,k\rangle\) and \(\langle Du,k\rangle\).  They are not the two
A--B--C Tate moments of \(F=Lu\):

\[
 M_\pm(F)=\int e^{\pm x/2}F(x)\,dx
 =-i\int e^{\pm x/2}\bigl(\phi'(x)\mp\tfrac12\bigr)u(x)\,dx. \tag{0.6}
\]

Thus the rank-two anomaly cannot be declared removed by the already proved
Tate shorting.  A comparison between these two different boundary planes
would be additional mathematics; no such comparison is assumed here.

No zero location is used to construct the metric.  The paper is not
modified.

## 1. The quotient metric

Work in \(H=L^2(\mathbb R,dx)\), with inner products linear in the first
variable.  The theta vector \(k\) is real, positive, even and belongs to
the Schwartz class.  Since

\[
 L=-iC,\qquad C=\partial+\phi',\qquad Ck=0,            \tag{1.1}
\]

the kernel of the maximal first-order realization is \(\mathbb Ck\).
If \(Lu=Lv\), then \(u-v\in\mathbb Ck\), so \(Qu=Qv\).  This proves that
(0.2) is well defined.  It is nondegenerate on \(\mathrm{Ran}\,L\):
\(Qu=0\) implies \(u\in\ker L\), hence \(Lu=0\).

This is the minimal \(L^2\) quotient norm.  It is source-defined from the
positive theta kernel and contains no choice of zero polarization.

## 2. The exact pair-symmetry defect

For vectors in a common rapidly decaying core, \(D=-i\partial\) is
symmetric.  Expanding \(Q=I-P_k\), where

\[
 P_ku={\langle u,k\rangle\over N}k,\qquad N=\|k\|^2,  \tag{2.1}
\]

gives

\[
\begin{aligned}
 &\langle LDu,Lv\rangle_{\rm q}
 -\langle Lu,LDv\rangle_{\rm q}\\
 &=\langle QDu,Qv\rangle-\langle Qu,QDv\rangle\\
 &={-\langle Du,k\rangle\langle k,v\rangle
 +\langle u,k\rangle\langle k,Dv\rangle\over N}.
                                                               \tag{2.2}
\end{aligned}
\]

All bulk terms cancel by symmetry of \(D\).  Thus the quotient has exactly
two boundary coordinates and no hidden infinite-rank defect.

## 3. Fourier form of the theta eigenfunction

The theta eigenfunction equation can be written

\[
 Du_\alpha+\alpha u_\alpha=-ik.                       \tag{3.1}
\]

With \(\widehat f(\tau)=\int f(x)e^{-i\tau x}dx\),
\(D\) is multiplication by \(\tau\), and therefore

\[
 \widehat u_\alpha(\tau)
 ={-i\,\widehat k(\tau)\over\tau+\alpha}.             \tag{3.2}
\]

When \(\alpha\) is real and \(\Xi(\alpha)=0\), the apparent pole at
\(\tau=-\alpha\) is removable because
\(\widehat k(-\alpha)=\tfrac12\Xi(\alpha)=0\).
For non-real \(\alpha\) the denominator has no real pole.  Thus (3.2)
belongs to \(L^2\) for every nontrivial zero in the critical strip.

Put

\[
 d\mu(\tau)={|\widehat k(\tau)|^2\over2\pi}\,d\tau.   \tag{3.3}
\]

Plancherel gives

\[
\begin{aligned}
 N&=\int_{\mathbb R}d\mu(\tau),\\
 z_\alpha&=-i\int_{\mathbb R}{d\mu(\tau)\over\tau+\alpha},\\
 J_\alpha&=\int_{\mathbb R}{d\mu(\tau)\over|\tau+\alpha|^2}.
                                                               \tag{3.4}
\end{aligned}
\]

For \(\alpha=a+ib\),

\[
 \mathrm{Re}\,z_\alpha=-bJ_\alpha.                \tag{3.5}
\]

## 4. The Cauchy variance

Taking the inner product of (3.1) with \(k\) gives

\[
 \langle Du_\alpha,k\rangle
 =-\alpha z_\alpha-iN.                                \tag{4.1}
\]

Substitution of (4.1) and its conjugate into (2.2), with \(u=v=u_\alpha\),
yields

\[
\begin{aligned}
 N\Omega(u_\alpha,u_\alpha)
 &=2ib|z_\alpha|^2+2iN\mathrm{Re}\,z_\alpha\\
 &=2ib\bigl(|z_\alpha|^2-NJ_\alpha\bigr),             \tag{4.2}
\end{aligned}
\]

 and therefore, with the convention (0.3), the final formula is

\[
 \boxed{\Omega(u_\alpha,u_\alpha)
 ={2ib\over N}\bigl(|z_\alpha|^2-NJ_\alpha\bigr).}    \tag{4.3}
\]

Formula (4.3) is the same as (0.4).

By Cauchy--Schwarz in \(L^2(d\mu)\),

\[
 |z_\alpha|^2
 \le N J_\alpha.                                      \tag{4.4}
\]

Equality would require \((\tau+\alpha)^{-1}\) to be constant
\(\mu\)-almost everywhere.  But \(\widehat k=\Xi/2\) is nonzero on a set
of full measure, so \(\mu\) is not supported at one point.  Hence (4.4) is
strict.

If \(b\ne0\), (4.3) is nonzero.  If \(b=0\), the removable real integrand
in the second line of (3.4) is real before multiplication by \(-i\), so
\(\mathrm{Re}\,z_\alpha=0\), and (4.3) vanishes.

This proves the announced exact detector.

## 5. Comparison with the two Tate moments

Let \(F=Lu=-i(u'+\phi'u)\).  For \(s=\pm\tfrac12\), integration by parts
on a rapidly decaying core gives

\[
\begin{aligned}
 M_s(F)
 &=\int_{\mathbb R}e^{sx}F(x)\,dx\\
 &=-i\int_{\mathbb R}e^{sx}(\phi'(x)-s)u(x)\,dx.      \tag{5.1}
\end{aligned}
\]

The theta quotient plane is generated by the functionals

\[
 u\longmapsto\langle u,k\rangle,\qquad
 u\longmapsto\langle Du,k\rangle
               =\langle u,Dk\rangle.                 \tag{5.2}
\]

The Tate plane is generated by the two functions

\[
 e^{x/2}(\phi'-\tfrac12),\qquad
 e^{-x/2}(\phi'+\tfrac12).                            \tag{5.3}
\]

These planes are not equal.  Indeed \(k,Dk\) are Schwartz functions,
whereas both functions in (5.3) grow super-exponentially at one end because
\(\phi'(x)\sim\pm2\pi e^{2|x|}\).  Equality as distributions on
\(C_c^\infty\) is therefore impossible.

Consequently imposing \(M_+(F)=M_-(F)=0\) does not annihilate (2.2).
The positive theta quotient cannot be substituted for the contraction of
D.137.

## 6. Consequence for the active route

The theta quotient supplies all three pieces one would hope for:

1. a canonical positive metric;
2. a rank-two rather than infinite-rank failure of self-adjointness; and
3. an exact scalar detector of off-line zeros.

The remaining mismatch is now explicit:

\[
 \text{theta boundary plane }
 \mathrm{span}\,\{k,Dk\}
 \ne
 \text{A--B--C Tate plane in (5.3)}.                  \tag{6.1}
\]

A valid continuation would need a source-defined symplectic transport
between these planes which also intertwines every \(p^k\) channel and the
Gamma screw.  Merely choosing an isomorphism between two abstract
two-dimensional spaces would change the pair defect and would not prove
contractivity.

Thus D.140 advances the Hilbert descent to a finite, explicitly computed
boundary mismatch.  It does not identify the two planes and does not claim
row D.
