# Independent audit of the first theta Jensen minor

## Verdict

The theorem in `103_34` is correct as stated.  This audit independently
checks the modular matching at the origin, the log-sum curvature constants, the
factorial-normalized moment lemma, and the passage to the even subsequence.
No RH assumption or zero-location input enters any of them.

## 1. Smooth even matching at the origin

Put
\[
 \psi(u)=\sum_{m\ge1}e^{-\pi m^2e^{2u}},\qquad
 h(u)=e^{u/2}\psi(u).
\tag{1}
\]
For one summand, with \(x=\pi m^2e^{2u}\), direct differentiation gives
\[
 {1\over2}\left({d^2\over du^2}-{1\over4}\right)
 \left(e^{u/2}e^{-x}\right)=e^{u/2}x(2x-3)e^{-x}.                \tag{2}
\]
Hence the `103_34` kernel is
\[
 \Phi(u)={1\over2}\left({d^2\over du^2}-{1\over4}\right)h(u).\tag{3}
\]
For \(\vartheta(u)=1+2\psi(u)\), the theta transformation is
\[
 \vartheta(u)=e^{-u}\vartheta(-u).                               \tag{4}
\]
It follows that
\[
 h(u)-h(-u)=-\sinh(u/2).                                         \tag{5}
\]
The operator in (3) annihilates \(\sinh(u/2)\).  Thus \(\Phi\) has a
smooth even extension and
\[
 \Phi'(0+)=0.                                                     \tag{6}
\]
The differentiated series converge at zero by domination with a polynomial
in \(m\) times \(e^{-\pi m^2}\).  This verifies the nontrivial boundary
fact used to deduce monotonicity in `103_34`.

## 2. Audit of the curvature constants

For the summands \(f_m\) and \(x=\pi e^{2u}\), the exact formulas are
\[
 \ell_m'={5\over2}+{4m^2x\over2m^2x-3}-2m^2x,
\qquad
 \ell_m''=-4m^2x-{24m^2x\over(2m^2x-3)^2}.                       \tag{7}
\]
Thus \(\ell_m''<-4m^2x\le-4x\).  The log-sum identity has the correct
sign
\[
 (\log\Phi)''=\sum_mw_m\ell_m''+
 \operatorname{Var}_w(\ell_m').                                  \tag{8}
\]
With \(a=m^2-1\ge3\), the bounds in `103_34` give
\[
 \operatorname{Var}_w(\ell_m')
 \le18x^2\sum_{m\ge2}m^4(m^2-1)^2e^{-(m^2-1)x}.                  \tag{9}
\]
Every numerical constant checks:
\[
 m^4=(a+1)^2\le{16\over9}a^2,qquad18\cdot{16\over9}=32,       \tag{10}
\]
and (x^2e^{-ax}) decreases for \(x\ge\pi,a\ge3\).  Therefore
\[
 \operatorname{Var}_w(\ell_m')
 \le32\pi^2\sum_{a=3}^\infty a^4e^{-a\pi}.
\tag{11}
\]
The elementary inputs \(\pi^2<10\) and \(e^\pi>23\) are sufficient.
For the latter, the terms of orders (0) through (8) in the exponential
series at (6283/2000<\pi) already sum to more than (23).  The term
ratio in the resulting series is at most
\[
 {1\over23}\left({4\over3}\right)^4={256\over1863}<{1\over7}.
\tag{12}
\]
Hence the variance is at most
\[
 320\,{81\over23^3}\,{7\over6}
 ={30240\over12167}<{249\over100}.                              \tag{13}
\]
It follows that
\[
 (\log\Phi)''<-4x+2.49<0.                                       \tag{14}
\]
Together with (6), this makes \(\Phi\) strictly decreasing on
\((0,\infty)\).

## 3. The normalized-moment lemma

For \(m_p=\int_0^\infty u^pf(u)du\), \(p\ge1\), and
\(h=-f'/f\), integration by parts gives
\[
 \mathbb E_{\nu_p}h={p\,m_{p-1}\over m_p},
 \qquad \mathbb E_{\nu_p}(uh)=p+1,
 \qquad \mathbb E_{\nu_p}u={m_{p+1}\over m_p}.                  \tag{15}
\]
There is no lost endpoint: \(u^pf(u)\) vanishes at zero and rapid decrease
handles infinity.  Strict log-concavity makes \(h\) strictly increasing, so
\[
 2\operatorname{Cov}_{\nu_p}(u,h)
 =\iint(u-v)(h(u)-h(v))d\nu_p(u)d\nu_p(v)>0.                      \tag{16}
\]
Substitution of (15) proves
\[
 m_p^2>{p\over p+1}m_{p-1}m_{p+1}.                               \tag{17}
\]
This is exactly strict log-concavity of \(m_p/p!\).  With \(f=2\Phi\),
the moments are precisely the \(M_p\) of `103_34`, so its factor 2 is
correct.

## 4. Even subsequence and Jensen roots

Strict log-concavity makes the ratios \(a_p/a_{p-1}\),
\(a_p=M_p/p!\), strictly decreasing.  Hence
\[
 {a_{2N+2}\over a_{2N}}
 ={a_{2N+1}\over a_{2N}}{a_{2N+2}\over a_{2N+1}}
 >{a_{2N+3}\over a_{2N+2}}{a_{2N+4}\over a_{2N+3}}
 ={a_{2N+4}\over a_{2N+2}},                                      \tag{18}
\]
so \(a_{2N+2}^2>a_{2N}a_{2N+4}\).  Since \(c_N=a_{2N}\), this is the
claimed first Jensen minor.  Its quadratic has positive product of roots,
negative sum, and positive discriminant, hence two distinct negative roots.

## Status

`103_34` is a valid all-shift PF\(_2\)-level theorem for the specific theta
moments.  This audit finds no boundary, normalization, or constant error.
It does not by itself control higher Jensen minors or the strong-margin
quantities \(D_n\).
