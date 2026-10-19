# 104_17 — Incomplete block: Abel–Fejér stop-gate after the erratum

**Role.** First attack on the lower bound that remains after correcting
Lagarias's sign. It does not prove A1. It rules out a precise family:
obtaining the coefficient-by-coefficient sign from radial Abel positivity or
from Cesàro/Fejér averages of the incomplete block.

The correct coordinate from `104_02` is

\[
 \mathrm {A1}_{\theta}
 \iff
 -\lambda_n(\sqrt n)+\widetilde\varepsilon_n
 +R_n(T_n(\theta))\le(1-\theta)A_n.                 \tag{1}
\]

Hence a **lower** bound for
\(\lambda_n(\sqrt n)\) is needed. Averaging cannot replace it without a signed
Tauberian theorem.

## 1. Internal non-duplication audit

`103_27` and `103_28` already prove that pointwise Fejér positivity on the
circle does not survive a reciprocal off-line quartet. This document does not
repeat that result. It adds:

1. the exact cumulative and triangular sums of the quartet;
2. a radial Abel positivity theorem for **every** quartet, even off the
   line;
3. a rational witness where the Abel germ is positive but the coefficient
   and the triangular average are negative.

The extension identifies why a radial Tauberian argument cannot be the
missing mechanism.

## 2. Exact contribution of a quartet

Let \(\rho=\beta+i\gamma\), with \(0<\beta<1\), \(\gamma\ne0\), and
\(\beta\ne\tfrac12\), and let

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\}.
\]

Set

\[
 w_\eta=1-{1\over\eta},\qquad
 w=w_\rho=re^{i\vartheta}=e^{a+i\vartheta}.
\]

The symmetries give

\[
 w_{\bar\rho}=\bar w,\qquad
 w_{1-\rho}=w^{-1},\qquad
 w_{1-\bar\rho}=\bar w^{-1}.                       \tag{2}
\]

The quartet's contribution to the Li coefficient is, therefore,

\[
\begin{aligned}
 Q_n
 &:=\sum_{\eta\in\mathcal O(\rho)}(1-w_\eta^n)\\
 &=4-(w^n+\bar w^n+w^{-n}+\bar w^{-n})\\
 &=\boxed{\,4-2(r^n+r^{-n})\cos(n\vartheta)\,}\\
 &=4-4\cosh(an)\cos(n\vartheta).                  \tag{3}
\end{aligned}
\]

The factor is \(4\), not \(8\). The Weil form
\(2\mathrm{Re}\,\lambda_n\) doubles (3); that is the source of the factor
\(8\) in `103_69` and `104_14`.

## 3. The two finite averages preserve the exponential obstruction

Define

\[
 G_N(z)=\sum_{n=1}^Nz^n={z(1-z^N)\over1-z},
\]

and

\[
 V_N(z)=\sum_{n=1}^N(N+1-n)z^n
 ={z\{N-(N+1)z+z^{N+1}\}\over(1-z)^2}.             \tag{4}
\]

Summing (3) gives exactly

\[
 \sum_{n=1}^NQ_n
 =4N-2\mathrm{Re}\,\{G_N(w)+G_N(w^{-1})\},     \tag{5}
\]

and, for the triangular average,

\[
 \sum_{n=1}^N(N+1-n)Q_n
 =2N(N+1)-2\mathrm{Re}\,\{V_N(w)+V_N(w^{-1})\}.\tag{6}
\]

If \(r>1\), the dominant parts of (5)–(6) are, respectively,

\[
 2\mathrm{Re}{w^{N+1}\over1-w},
 \qquad
 -2\mathrm{Re}{w^{N+2}\over(1-w)^2}.        \tag{7}
\]

So both summations retain a load of size \(r^N\); they do not turn it into a
polynomial error. The same computation, after a fixed number of summations,
only adds a fixed power of \((1-w)^{-1}\) and keeps \(r^N\).

## 4. Theorem: radial Abel positivity for every functional orbit

Define

\[
 \mathcal A_\rho(q)=\sum_{n\ge1}Q_nq^n.
\]

The series converges ordinarily for
\(0<q<e^{-|a|}=\min(r,r^{-1})\).

**Theorem.** For every \(q\) in that interval,

\[
 \boxed{
 \mathcal A_\rho(q)
 ={2q(1+q)\over(1-q)^3}{X\over X^2+Y^2}>0,}         \tag{8}
\]

where

\[
 x={q\over1-q},\qquad
 X=(x+\beta)(x+1-\beta)+\gamma^2>0,\qquad
 Y=\gamma(1-2\beta).                                \tag{9}
\]

The rational side of (8) continues as a strictly positive function over
the whole interval \(0<q<1\). Equality with the **series** is asserted only
within its radius of convergence.

*Proof.* For each \(\eta\in\mathcal O(\rho)\),

\[
\begin{aligned}
 \sum_{n\ge1}q^n(1-w_\eta^n)
 &= {q\over1-q}-{qw_\eta\over1-qw_\eta}\\
 &= {q(1-w_\eta)\over(1-q)(1-qw_\eta)}
  ={q\over(1-q)^2}{1\over x+\eta}.                 \tag{10}
\end{aligned}
\]

The last equality uses
\(1-w_\eta=1/\eta\) and
\(1-qw_\eta=((1-q)\eta+q)/\eta\). Summing over the quartet,

\[
 \mathcal A_\rho(q)
 ={2q\over(1-q)^2}\mathrm{Re}
 \left({1\over x+\rho}+{1\over x+1-\rho}\right).  \tag{11}
\]

The parenthesis is

\[
 {1+2x\over(x+\rho)(x+1-\rho)},                   \tag{12}
\]

and

\[
 (x+\rho)(x+1-\rho)=X+iY.                         \tag{13}
\]

Since \(\mathrm{Re}(X+iY)^{-1}=X/(X^2+Y^2)\) and
\(1+2x=(1+q)/(1-q)\), (8) follows from (11)–(13). All
the factors are strictly positive. \(\square\)

If \(\beta=\tfrac12\), the four labels duplicate the conjugate pair; (8) is
divided by two and positivity remains.

## 5. Exact rational witness

Take

\[
 \rho={1+2i\over5},\qquad w=2i.
\]

The exact arithmetic of (3) gives

\[
\begin{array}{c|rrrrrrrr}
n&1&2&3&4&5&6&7&8\\ \hline
Q_n&4&25/2&4&-225/8&4&4225/32&4&-65025/128.
\end{array}                                                     \tag{14}
\]

With

\[
 C_N=\sum_{n=1}^NQ_n,\qquad
 F_N=\sum_{n=1}^N(N+1-n)Q_n,
\]

one obtains

\[
 \boxed{
 Q_4=-{225\over8},\quad C_4=-{61\over8},\quad
 F_4={267\over8}>0,\quad F_8=-{10885\over128}<0.} \tag{15}
\]

So \(F_4\) masks the negative coefficient, but \(F_8\) proves that the
average does not preserve positivity either. By contrast, for \(0<q<1/2\),

\[
 \boxed{
 \mathcal A_\rho(q)
 ={4q\over1-q}+{8q^2\over1+4q^2}+{2q^2\over4+q^2}>0,}          \tag{16}
\]

even though

\[
 Q_{4k}=4-2(2^{4k}+2^{-4k})\longrightarrow-\infty.             \tag{17}
\]

## 6. Why there is no transfer to the moving cutoff

For a fixed height \(T\), if

\[
 \lambda_n(T)=\sum_{|\Im\rho|<T}(1-w_\rho^n),
\]

then

\[
 \Delta^k\lambda_n(T)
 =(-1)^{k-1}\sum_{|\Im\rho|<T}{w_\rho^n\over\rho^k},
 \qquad k\ge1.                                      \tag{18}
\]

This has no fixed sign. For \(T=\sqrt n\), the difference also contains the
zeros of the shell
\([\sqrt n,\sqrt{n+1})\), likewise with no sign. The recovery identities

\[
 Q_N=C_N-C_{N-1},\qquad
 Q_N=F_N-2F_{N-1}+F_{N-2}                           \tag{19}
\]

show the exact loss: a size bound on \(C_N\) or \(F_N\) does not control the
required signed difference. A strong-variation hypothesis sufficient for
(19) would already exclude (15)–(17) and would contain the same RH-strength
datum.

## 7. Decision

```text
proved:
  exact formulas for the quartet and its two summations;
  strict radial Abel positivity even for off-line quartets;
  rational witness with a negative coefficient and a negative Fejér average;
  absence of a fixed sign in the differences, with either fixed or moving
  cutoff.

ruled out as an autonomous source of A1:
  radial Abel positivity;
  a fixed number of Cesàro/Fejér averages;
  Tauberian transfer without a new angular or variation hypothesis.

not ruled out:
  a specific identity for the real weights of zeta that simultaneously
  controls the angle and the coefficient-by-coefficient recovery.

not proved:
  the lower bound for lambda_n(sqrt n), A1, or RH.
```

The natural successor is not another radial average. Uniform angular control
is the Toeplitz–Herglotz/Weil gate already audited in phases 102–103. The
front attempted next instead keeps the Euler–pole cocycle at finite
correlated shift \(u=c\varepsilon\), which `104_16` did not eliminate.

## 8. Exact reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 incomplete_abel_stop_gate_check.py
```

The program uses only `Fraction`: it certifies (14)–(15) and compares the two
rational forms of (8)/(16) at three rational values of \(q\). Positivity over
the whole interval is the algebraic argument of (8)–(13), not a numerical
sampling.
</content>
