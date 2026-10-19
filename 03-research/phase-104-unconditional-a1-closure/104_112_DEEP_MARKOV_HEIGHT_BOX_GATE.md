# 104_112 — Deep height box and the no-slack Markov gate

**Question.** Does the deep form of `104_75`–`104_76` leave real slack
that could be exploited by Markov's inequality, averages in \(n\), or a
small positive-density bound?

**Result.** No. The deep relaxation is indeed weaker than A1, but its
logarithmic average contains no intermediate margin. For an exterior
zero \(\rho=\beta+i\gamma\), \(\beta>1/2\), set

\[
 w_\rho={\rho-1\over\rho}=e^{-a_\rho+i\theta_\rho},\qquad
 a_\rho={1\over2}\log {|\rho|^2\over|\rho-1|^2}>0 .
\]

The functional quartet contributes to \(\lambda_n\)

\[
 q_n(\rho)=4-4\cosh(na_\rho)\cos(n\theta_\rho).          \tag{1}
\]

With the deep threshold \(S_X=e^{\sqrt X}\), a return
\(\cos(n\theta_\rho)\ge1/2\) with \(n\in[X/2,X]\) forces
\[
 q_n(\rho)\le 4-e^{na_\rho}.
\]
Hence the deep detector trips as soon as
\[
 a_\rho>2X^{-1/2}+O(X^{-1}\log X).                       \tag{2}
\]

Since
\[
 a_\rho={2\beta-1\over 2\gamma^2+O(1)}
 \qquad(\gamma\to\infty,\ \beta\hbox{ fixed}),             \tag{3}
\]
the equivalent obstacle box is, up to absolute constants,

\[
 \boxed{
 R_X=\left\{\rho:\ 0<\gamma\lesssim X^{1/4},\quad
 \beta-{1\over2}\gtrsim \gamma^2X^{-1/2}\right\}.}        \tag{4}
\]

Thus `104_75`–`104_76` do not turn RH into a smooth average estimate:
they turn RH into a family of zero-free regions whose boundary touches
\(\Re s=1/2\) as \(X\to\infty\). A single zero in (4) produces a deep
excursion on a syndetic set of positive logarithmic density.

This document closes three routes:

1. a Markov bound on the positive part of the sum of low zeros;
2. any attempt to improve only a constant
   \(\limsup\Omega_X\le c\), with \(c>0\);
3. using finite zero verification as an asymptotic substitute.

It does not prove the deep limit, A1, or RH. It proves that this
coordinate no longer has hidden quantitative slack: either zeros in box
\(R_X\) are excluded, or the detector fails.

---

## 1. The box \(R_X\)

Equation (1) is the same as in `104_76`. If
\(\cos(n\theta_\rho)\ge1/2\), then

\[
 q_n(\rho)\le4-2\cosh(na_\rho)\le4-e^{na_\rho}.          \tag{5}
\]

In the deep observable, the subexponential error from the non-interior
factors (`104_111`) and from the high tail (`104_76`) is allowed. Both
are \(\exp(o(\sqrt X))\) or smaller compared with \(S_X=e^{\sqrt X}\).
Hence, in the range \(n\in[X/2,X]\), the condition that is both
sufficient and necessary at exponential scale for a fixed quartet to
trip the detector is

\[
 {X\over2}a_\rho\ge\sqrt X+o(\sqrt X),                  \tag{6}
\]

which is (2).

On the other hand,

\[
 e^{2a_\rho}
={\beta^2+\gamma^2\over(1-\beta)^2+\gamma^2}
=1+{2\beta-1\over(1-\beta)^2+\gamma^2}.                 \tag{7}
\]

When \(0<\beta-1/2\le1/2\),
\[
 {2\beta-1\over 2(\gamma^2+1)}
 \le a_\rho
 \le {2\beta-1\over 2\gamma^2}.                         \tag{8}
\]

The constants in (8) do not matter for the gate: combined with (2) they
say exactly that the required boundary has the form
\[
 \beta-{1\over2}\asymp\gamma^2X^{-1/2}.                  \tag{9}
\]

Moreover, the universal bound of `104_76`,
\[
 a_\rho\le {1\over2\gamma^2},                            \tag{10}
\]
implies that no zero with
\(\gamma\gg X^{1/4}\) can by itself produce an excursion of size
\(e^{\sqrt X}\) at degrees \(n\le X\). This recovers the scale
\(\gamma\le X^{1/4}\) of `104_76` from the opposite side: the scale is
not an artifact of the tail proof, but the exact scale of the detector.

## 2. Exact Markov, no gain

Let \(Y=X^{1/4}\), and write \(D_n(Y)\) for the low-zero part, with the
sign oriented so that an exterior quartet with
\(\cos(n\theta_\rho)\ge1/2\) contributes positively to \(D_n(Y)\).
On the critical line, each orbit contributes a non-negative amount to
\(\lambda_n\); hence \(D_n(Y)\le0\) for every \(n\) if all the low zeros
are on the line.

If there is an exterior quartet in box (4), the returns
\(\cos(n\theta_\rho)\ge1/2\) form a syndetic set. In any interval
\([X/2,X]\), its harmonic mass has a positive lower bound, and at those
returns

\[
 D_n(Y)_+\ge e^{na_\rho}-O(N(Y)).                       \tag{11}
\]

Since
\[
 N(X^{1/4})\asymp X^{1/4}\log X,                         \tag{12}
\]
one obtains

\[
 \sum_{n\le X}{D_n(Y)_+\over n}
 \gg e^{Xa_\rho/2}-O(X^{1/4}\log X).                    \tag{13}
\]

The Markov bound that would want to prove the deep limit would have scale
\[
 e^{\sqrt X}H_X.                                        \tag{14}
\]

Equations (13)–(14) show that there is no intermediate regime: under RH
the positive sum is zero; with an exterior zero sufficiently deep inside
the box it grows faster than the threshold. Markov loses nothing, and
therefore gains nothing. Any average in \(n\) that preserves the deep
excursions again requires the pointwise exclusion of (4).

## 3. Positive density constants do not work

`104_56` already records that, in the abstract Fejér phase model, the bad
density forced by an exterior zero can be made arbitrarily small. Hence
no statement of the form

\[
 \limsup_{X\to\infty}\Omega_X\le c
 \qquad(c>0)                                            \tag{15}
\]

can be a partial step toward RH. Excluding all exterior zeros requires
the limit \(c=0\). Improving \(1/2\) to \(1/8\), or to any positive
constant, does not rule out the already-built dominant-phase
counterexamples.

The correct form of the deep target is therefore:

\[
 \boxed{\Omega_X\to0}
 \quad\Longleftrightarrow\quad
 \boxed{\hbox{no zeros in }R_X\hbox{ as }X\to\infty}
 \quad\Longleftrightarrow\quad
 \mathrm{RH}.                                           \tag{16}
\]

The first equivalence is operational: (4) gives the only window in which
the detector can fail after `104_76` and `104_111`. The second is the
fact that, for any fixed zero with \(\beta>1/2\), there is a sufficiently
large \(X\) such that it falls inside \(R_X\).

## 4. Strategic consequence

The deep route remains valid as a criterion, but it does not reduce the
final step to a first-moment estimate, a second-moment estimate, Markov,
Chernoff, or a positive density constant. The next mechanism, if it
exists, must be a zero-exclusion inequality in box \(R_X\) using the
literal ordinary primes and the Riemann completion. It must fail for the
exterior Euler models of `104_78`, `104_81`, `104_90`, and `104_91`;
otherwise it does not distinguish the real zeta.
</content>
