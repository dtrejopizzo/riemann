# D.67 — The arithmetic defect is not Green-form bounded

## Status

This note gives a precise negative result for the continuum route of D.62.
Immediately after the first prime threshold, the arithmetic discrepancy
cannot be dominated separately by the continuum Green energy, even on the
two-Tate primitive space and even on one fixed compact window.  Its positive
relative bound is infinite.

The complete Gamma term reverses the high-frequency growth.  Thus the result
does **not** disprove the row-D inequality.  It proves that any successful
global argument must keep the prime and Gamma terms coupled before making a
Green-energy estimate.  No zeta zero, Weil positivity, screw positivity or
Riemann-hypothesis assumption is used.

## 1. The three forms

Put

\[
 L={d^2\over dx^2}-{1\over4},\qquad
 \mathcal P=\ker M_-\cap\ker M_+ .                         \tag{1.1}
\]

By the exact Green calculation of D.62, `L` maps
`C_c^infinity(R)` bijectively to `P`.  If `F=Lu`, then

\[
 E_G(u):=-V_0(F,F)
 =\int_{\mathbb R}\left(|u'|^2+{1\over4}|u|^2\right)dx.    \tag{1.2}
\]

The arithmetic form and its continuum discrepancy are

\[
 \begin{aligned}
 V_{\rm ar}(F,F)
 &=2\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
             \operatorname {Re}\langle F,S_{\log n}F\rangle,\\
 V_\varepsilon(F,F)&=V_{\rm ar}(F,F)-V_0(F,F).
 \end{aligned}                                             \tag{1.3}
\]

For compactly supported `F`, the sum in (1.3) is finite.  The full primitive
form is

\[
 B_{\rm nuc}(F,F)=V_0(F,F)+V_\varepsilon(F,F)
                         +\Gamma(F,F)
                  =V_{\rm ar}(F,F)+\Gamma(F,F).             \tag{1.4}
\]

All prime powers are present in (1.3), and `Gamma` is the complete
archimedean multiplier of D.32.

## 2. A primitive high-frequency family isolating the first contact

Fix

\[
 T>{\log2\over2}.                                           \tag{2.1}
\]

Choose a length

\[
 \log2<\ell<\min(2T,\log3)                                 \tag{2.2}
\]

and a real nonnegative, nonzero function
`chi in C_c^infinity((-T,T))` whose support is contained in an interval of
length `ell` and for which

\[
 I_2:=\int_{\mathbb R}\chi(x)\chi(x-\log2)dx>0.             \tag{2.3}
\]

Such a function is obtained by taking a positive bump on an interval of
length strictly between `log 2` and `ell` and smoothing near the endpoints.
For

\[
 N_j={2\pi j\over\log2},\qquad
 u_j(x)=\chi(x)e^{iN_jx},\qquad F_j=Lu_j,                   \tag{2.4}
\]

every `F_j` lies in `P`, because `u_j` is compactly supported and the two
integrations by parts

\[
 \int e^{\pm x/2}Lu_j(x)dx=0                               \tag{2.5}
\]

are exact.

The support choice has two further exact consequences.  The translates of
`F_j` by `log n` have disjoint support for every `n>=3`, while the translate
by `log 2` has nonempty overlap.  Hence the complete prime-power sum reduces
on this family to the single `n=2` contact:

\[
 V_{\rm ar}(F_j,F_j)
 ={2\log2\over\sqrt2}
       \operatorname {Re}\langle F_j,S_{\log2}F_j\rangle.  \tag{2.6}
\]

This is not a truncation: all omitted terms vanish by disjoint support.

## 3. Infinite relative bound of the arithmetic discrepancy

Write `a=log 2`.  Direct differentiation gives

\[
 F_j(x)=e^{iN_jx}
 \left(-(N_j^2+1/4)\chi(x)+2iN_j\chi'(x)+\chi''(x)\right).
                                                                    \tag{3.1}
\]

Since `exp(-i N_j a)=1`, expansion of (3.1), followed by
Cauchy--Schwarz for the lower-order terms, gives

\[
 \operatorname {Re}\langle F_j,S_aF_j\rangle
 =N_j^4 I_2+O_\chi(N_j^3).                                \tag{3.2}
\]

On the other hand, because `chi` is real,

\[
 E_G(u_j)=N_j^2\|\chi\|_2^2+
           \|\chi'\|_2^2+{1\over4}\|\chi\|_2^2.          \tag{3.3}
\]

Equations (2.6), (3.2) and (3.3) prove

\[
 {V_{\rm ar}(F_j,F_j)\over E_G(u_j)}
 ={\sqrt2\log2\,I_2\over\|\chi\|_2^2}N_j^2+O_\chi(N_j)
 \longrightarrow+\infty.                                  \tag{3.4}
\]

Since `V_0(F_j,F_j)=-E_G(u_j)`, it follows equally that

\[
 \boxed{
 {V_\varepsilon(F_j,F_j)\over E_G(u_j)}\longrightarrow+\infty.}
                                                                    \tag{3.5}
\]

We have proved:

> **Theorem 3.1 (separate-defect no-go).**  For every fixed
> `T>(log 2)/2`,
> \[
> \sup_{0\ne F=Lu\in\mathcal P,\ \operatorname {supp}u\subset(-T,T)}
> {V_\varepsilon(F,F)\over E_G(u)}=+\infty.               \tag{3.6}
> \]
> In particular there is no finite constant `C_T` for which
> \[
> V_\varepsilon(F,F)\le C_TE_G(u)                          \tag{3.7}
> \]
> on the primitive compact core, and a fortiori no relative bound smaller
> than one that could prove D.62(7.1) after estimating Gamma separately by
> its positive or absolute magnitude.

The theorem uses just the first derived contact `n=2`.  Therefore adding
the remaining prime powers cannot repair the asserted *separate* bound:
the test support makes all of them vanish.

## 4. Gamma exactly repairs the ultraviolet order

The no-go is not a counterexample to row D.  Let

\[
 m_\infty(\tau)=\log\pi-
 \operatorname {Re}\psi\left({1\over4}+{i\tau\over2}\right).       \tag{4.1}
\]

Stirling's formula in a fixed vertical sector gives

\[
 m_\infty(\tau)=-\log{|\tau|\over2\pi}+O(\tau^{-2})
 \quad(|\tau|\longrightarrow\infty).                      \tag{4.2}
\]

Moreover

\[
 \widehat {F_j}(\tau)=-(\tau^2+1/4)\widehat\chi(\tau-N_j).
                                                                    \tag{4.3}
\]

Plancherel, the rapid decay of `widehat chi`, and (4.2) imply by dominated
convergence

\[
 \boxed{
 {\Gamma(F_j,F_j)\over N_j^4\log N_j}
 \longrightarrow-\|\chi\|_2^2.}                          \tag{4.4}
\]

In comparison, (3.2) shows

\[
 V_{\rm ar}(F_j,F_j)=O_\chi(N_j^4).                       \tag{4.5}
\]

Consequently

\[
 {B_{\rm nuc}(F_j,F_j)\over N_j^4\log N_j}
 \longrightarrow-\|\chi\|_2^2,                           \tag{4.6}
\]

and hence `B_nuc(F_j,F_j)<0` for all sufficiently large `j`.

This gives a sharp order audit:

\[
 \begin{array}{c|c}
 \text{term}&\text{size on the primitive family}\ \\ \hline
 -V_0=E_G&N_j^2\\
 V_\varepsilon&+c_\chi N_j^4+O(N_j^3)\\
 \Gamma&-N_j^4\log N_j+O(N_j^4).
 \end{array}                                               \tag{4.7}
\]

Thus the continuum Green energy is two derivative orders too weak to
control the atomic discrepancy separately; the logarithmic Gamma energy is
the indispensable ultraviolet completion.

## 5. Exact Stieltjes form of the defect

The failure above can also be seen at the level of the prime-counting
remainder.  Put

\[
 E(x)=\psi(x)-x,qquad
 C_F(a)=2\operatorname {Re}\langle F,S_aF\rangle.          \tag{5.1}
\]

Since

\[
 d\nu_{\rm ar}(a)=e^{-a/2}d\psi(e^a),\qquad
 d\nu_0(a)=e^{-a/2}d(e^a),                                \tag{5.2}
\]

Stieltjes integration by parts, using `E(1)=-1` and the compact support of
`C_F`, yields the exact identity

\[
 \boxed{
 V_\varepsilon(F,F)
 =2\|F\|_2^2-
 \int_0^\infty E(e^a){d\over da}
       \left(e^{-a/2}C_F(a)\right)da.}                    \tag{5.3}
\]

For smooth `F` the ordinary integral in (5.3) is finite.  Formula (5.3)
explains why a pointwise prime-number-theorem envelope is not adapted to
the Green norm: after `F=Lu`, the derivative of the autocorrelation contains
up to five derivatives of the compact potential, whereas (1.2) controls
only one.  The Gamma multiplier supplies precisely the missing logarithmic
high-frequency control, but only after it is combined with the atomic
form.

## 6. Circularity audit and surviving global gate

The proof used only:

1. the source identity `(d^2-1/4)e^(|x|/2)=delta_0`;
2. compact supports and the positive coefficient `Lambda(2)/sqrt 2`;
3. the unconditional digamma asymptotic;
4. elementary Fourier analysis.

It did not use the explicit zeta zero divisor, a location of zeros, Weil
positivity, or positivity of the screw kernel.

What is falsified is the proposed route

\[
 V_\varepsilon\ \hbox{bounded in the continuum Green norm}
 \quad+\quad \Gamma\ \hbox{estimated separately}.         \tag{6.1}
\]

What survives is a coupled prime--Gamma estimate.  On each fixed window,
D.55 already proves that the coupled multiplier is negative beyond an
explicit frequency.  Therefore the genuinely unresolved part is the
finite-band parity--Feshbach core of D.56, uniformly through every
prime-power threshold and under support exhaustion.  Theorem 3.1 proves
that this coupling is logically necessary; it does not prove the remaining
finite-band inequality and hence does not close row D.

