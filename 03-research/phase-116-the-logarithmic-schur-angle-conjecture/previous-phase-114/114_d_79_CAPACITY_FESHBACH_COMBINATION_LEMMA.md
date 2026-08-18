# D.79 supplement — directed capacity–Feshbach combination

## Purpose

At the endpoint `T=log(2)` the dangerous direction is one-dimensional.
A scalar Hilbert--Schmidt estimate of the complete lower/high coupling is
far too expensive, while the coupling of the actual dangerous vector is
tiny.  The following lemma combines that directed residual with the
positive tail capacity without replacing the latter by a scalar norm.

## Lemma

Let `H=Cv+QH`, with `||v||=1`, and let `A_0=A_0^*` have block form

\[
 A_0=\begin{pmatrix}-\ell&r^*\\ r&D\end{pmatrix},
 \qquad D\ge gI,
 \qquad \|r\|\le\varepsilon,                         \tag{1}
\]

where `ell>=0` and `g>0`.  Let `R>=0`.  For every `0<eta<g`, put

\[
 h=g-\eta,
 \qquad
 \ell_{\rm eff}=\ell+{\varepsilon^2\over\eta}.       \tag{2}
\]

If

\[
 \boxed{
 \mathrm{cap}_{h}(v;R)
 ={1\over\langle v,(R+hI)^{-1}v\rangle}-h
 >\ell_{\rm eff},}                                    \tag{3}
\]

then `A_0+R>0`.  It is enough to prove the directed integral inequality

\[
 \boxed{
 \delta_h(v;R)
 >{\ell_{\rm eff}\over h(h+\ell_{\rm eff})},
 \qquad
 \delta_h={1\over h}-\langle v,(R+hI)^{-1}v\rangle .} \tag{4}
\]

If `R` is a nonnegative Fourier multiplier with symbol `r_R(tau)`, the
left hand side has the positive representation

\[
 \delta_h(v;R)={1\over2\pi}\int_{\mathbb R}
 |\widehat v(\tau)|^2
 {r_R(\tau)\over h(h+r_R(\tau))}\,d\tau.              \tag{5}
\]

Thus a directed lower quadrature on a finite frequency interval proves
(4); its omitted tail is positive and may be discarded.

## Proof

For `x=av+y`, `y in QH`, Cauchy--Schwarz and Young's inequality give

\[
 2\mathrm{Re}(\bar a\langle r,y\rangle)
 \ge -{\varepsilon^2\over\eta}|a|^2-\eta\|y\|^2.
                                                                    \tag{6}
\]

Together with (1), this is the operator inequality

\[
 A_0\ge-\ell_{\rm eff}|v\rangle\langle v|+hQ.          \tag{7}
\]

Consequently

\[
 A_0+R\ge
 R+hQ-\ell_{\rm eff}|v\rangle\langle v|.              \tag{8}
\]

Shorting `R+hQ` to `Cv` gives the scalar (3).  Hence the right hand side
of (8) is strictly positive exactly when its shorted scalar exceeds
`ell_eff`.  Formula (4) is the capacity--deficit identity of the preceding
supplement with `g` replaced by `h`; (5) is Plancherel.  This proves the
claim.

## Directed use at `T=log(2)`

The four inputs must be certified in compatible directions:

1. an upper enclosure for `ell`;
2. an upper enclosure for the **specific** residual norm `epsilon`;
3. a lower enclosure for the complementary gap `g`;
4. a lower enclosure for the finite positive integral in (5).

No norm of the full `P--Q` coupling appears.  In particular, this lemma
does not license replacing the specific residual by the Hilbert--Schmidt
norm measured in the floating diagnostic.

