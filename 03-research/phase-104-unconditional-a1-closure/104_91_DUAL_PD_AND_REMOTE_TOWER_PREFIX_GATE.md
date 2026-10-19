# 104_91 — Exact PD duality and the remote tower gate

**Result.** The dual formulation of the one-sided bound of 104_89
contains no hidden relaxation. If

\[
 d\nu(t)={dt\over2\pi(t^2+1/4)},\qquad
 k(y)=\int_{\mathbb R}e^{ity}\,d\nu(t)=e^{-|y|/2},       \tag{1}
\]

then the kernels that appear when \(0\leq\varphi\leq1\) varies are
exactly

\[
 \mathcal K=\{K\in C(\mathbb R;\mathbb R):K\text{ is even, and }
              K,\ k-K\text{ are positive definite}\}.         \tag{2}
\]

No coercivity is gained by replacing the supremum over selectors with
a supremum over (2): they are the same problem, and the extreme points
are again the indicator selectors.

The arithmetic part of the functional has the closed global form

\[
 \int\varphi u_X\,d\nu
 =\int_{1^-}^{X}
 \left\{x^{-1/2}K(\log x)-{K(0)\over x}\right\}
 d\{J(x)-\mathrm{Li}(x)\},                       \tag{3}
\]

where

\[
 dJ=\sum_{p^a}{1\over a}\,\delta_{p^a},\qquad
 d\mathrm{Li}(x)={dx\over\log x}.               \tag{4}
\]

Since \(d\mathrm{Li}\,\) has infinite mass at \(1^+\), (3) does not
assert that their difference is a Radon measure in a neighborhood of
one. The notation means the regularized improper functional

\[
 \int_{1^-}^Xq\,d(J-\mathrm{Li})
 :=\sum_{p^a\leq X}{q(p^a)\over a}
   -\lim_{\delta\downarrow0}\int_{1+\delta}^X
                  q(x){dx\over\log x},                 \tag{4a}
\]

for the test functions \(q(x)=O(\log x)\) that appear here.

Thus (3) jointly preserves all towers and the comparator. Renewal/Möbius
inversion adds no sign term: it reconstructs the same regularized
discrepancy, as 104_80 and E101_087, §11, already anticipate.

A stronger quantitative gate than the fixed model of 104_90 is also
proved. For every prefix \(M\) there is an ordinary prime \(P>M\) and
an Euler system that:

1. agrees literally with \(\Lambda(n)\) for all \(n\leq M\);
2. agrees with zeta on every tower except \(P^a\);
3. has nonnegative weights on ordinary prime powers;
4. preserves a continuous PNT with Vinogradov--Korobov-type error;
5. admits an entire completion with symmetry \(s\leftrightarrow1-s\);
6. has a real zero
   \(\beta_P=\tfrac12+\log(3/2)/(2\log P)>1/2\).

Its Jensen defect contains at least

\[
 \boxed{
 D_P=\log {\log P+\log(3/2)\over
                 \log P-\log(3/2)}>0.}                 \tag{5}
\]

Therefore no argument based on exact prefixes, PD restrictions,
positivity, prime support, PNT, and a broad functional equation can
prove the one-sided bound. A proof for the real zeta function must
simultaneously use the literal equality of all towers and the exact
data of its completion. The countermodel alters one tower and has
additional Euler poles; it is not a counterexample to RH.

This document does not prove the Deep-\(\Lambda\) limit, A1, or RH.

---

## 1. The PD class is exactly the selector interval

Since \(u(t)\) and \(u_X(t)\) are even, in

\[
 I_X=\sup_{0\leq\varphi\leq1}
       \int\varphi(t)\{u(t)-u_X(t)\}\,d\nu(t)           \tag{6}
\]

\(\varphi\) can be replaced by
\((\varphi(t)+\varphi(-t))/2\). Assume from now on that \(\varphi\) is
even and define

\[
 K_\varphi(y)=\int\varphi(t)e^{ity}\,d\nu(t)
              =\int\varphi(t)\cos(ty)\,d\nu(t).        \tag{7}
\]

The positive measures \(\varphi\nu\) and \((1-\varphi)\nu\) have
transforms \(K_\varphi\) and \(k-K_\varphi\). Bochner's theorem
immediately gives that both are positive definite.

The converse is just as important. If \(K\) and \(k-K\) are continuous
and positive definite, Bochner produces symmetric positive measures
\(\mu,\eta\) such that

\[
 \widehat\mu=K,\qquad \widehat\eta=k-K.                 \tag{8}
\]

By uniqueness of the Fourier transform of finite measures,

\[
 \mu+\eta=\nu.                                         \tag{9}
\]

Hence \(0\leq\mu\leq\nu\), there exists
\(\varphi=d\mu/d\nu\) with \(0\leq\varphi\leq1\), and
\(K=K_\varphi\). This proves

\[
 \boxed{
 \{K_\varphi:0\leq\varphi\leq1,\ \varphi\text{ even}\}
 =\mathcal K.}                                         \tag{10}
\]

The order interval \(0\leq\varphi\leq1\) has the characteristic
functions as extreme points. By (10), these are also the extreme
points of \(\mathcal K\). In particular the optimal selector

\[
 \varphi_X=\mathbf1_{\{u>u_X\}}                        \tag{11}
\]

does not disappear under the PD translation. A minimax that merely
replaces (6) by (2) returns exactly to (6).

## 2. Stieltjes form preserving all towers

Set

\[
 h_x(t)=x^{-1/2}\cos(t\log x)-x^{-1}.                  \tag{12}
\]

Equation (10) of 104_89 is written, without separating towers, as

\[
 \boxed{u_X(t)=\int_{1^-}^{X}h_x(t)\,
              d\{J(x)-\mathrm{Li}(x)\}.}        \tag{13}
\]

Indeed, the atom at \(p^a\) has mass
\(1/a=\Lambda(p^a)/\log(p^a)\). The continuous part of (13), with
\(x=e^y\), is

\[
 -\int_1^Xh_x(t){dx\over\log x}
 =\int_0^{\log X}{1-e^{y/2}\cos(ty)\over y}\,dy.      \tag{14}
\]

The singularity at \(x=1\) is removable because
\(h_x(t)=O(\log x)\). Since (13) is finite, Fubini is legitimate. If
\(c=K_\varphi(0)=\int\varphi\,d\nu\), then

\[
 \int\varphi h_x\,d\nu
 =x^{-1/2}K_\varphi(\log x)-{c\over x}.                \tag{15}
\]

Equations (13)--(15) prove (3).

To record the full dual, let

\[
 \mathcal U(K)=\int\varphi_K(t)u(t)\,d\nu(t),          \tag{16}
\]

where \(\varphi_K\) is the unique density of (10). Then

\[
 \boxed{
 I_X=\sup_{K\in\mathcal K}
 \left[
  \mathcal U(K)-
  \int_{1^-}^{X}
  \{x^{-1/2}K(\log x)-K(0)/x\}\,
  d(J-\mathrm{Li})(x)
 \right].}                                             \tag{17}
\]

Positive definiteness jointly restricts all the values
\(K(\log p^a)\), but (10) shows that it imposes nothing that was not
already in the original selector. Proving that (17) tends to zero
remains the one-sided arithmetic inequality of 104_89.

Exact renewal likewise produces no reserve. In the logarithmic
coordinate, \(L*N=yN\), or equivalently \(\Lambda*1=\log\). Solving
for \(L\) again gives \(L=\mu*\log\); exponentiating \(dJ\)
reconstructs the same Euler product. 104_80, equations (10)--(13),
proves that this inversion returns to the same meromorphic germ and
preserves every pole coming from a zero. For this reason it is not
reopened here as a distinct mechanism.

## 3. Countermodel on an arbitrarily remote prime tower

Let \(P>6\) be an ordinary prime and define

\[
 Z_-(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},\qquad
 T_P(s)=\sqrt{P/6}\,P^{-s},                             \tag{18}
\]

\[
 W_P(s)=Z_-(T_P(s)),\qquad Z_P(s)=\zeta(s)W_P(s).       \tag{19}
\]

For

\[
 A_a=6^a+1-3^a-2^a=(3^a-1)(2^a-1)>0                  \tag{20}
\]

one has, where it converges absolutely,

\[
 \log W_P(s)=\sum_{a\geq1}{A_a\over a}
                    (P/6)^{a/2}P^{-as}.                \tag{21}
\]

Hence

\[
 -{W_P'\over W_P}(s)
 =\sum_{a\geq1}{b_P(P^a)\over P^{as}},                \tag{22}
\]

\[
 \boxed{
 b_P(P^a)=\log P\,(P/6)^{a/2}A_a>0.}                  \tag{23}
\]

The Euler channel of \(Z_P\) has weights

\[
 \Lambda_P(n)=
 \begin{cases}
  \Lambda(n)+b_P(n),&n=P^a,\\
  \Lambda(n),&n\ne P^a.
 \end{cases}                                           \tag{24}
\]

If \(P>M\), then (24) coincides with the ordinary Mangoldt function
for all \(n\leq M\), and agrees on every tower but one.

### 3.1. Continuous PNT

Set

\[
 \sigma_P={\log\sqrt{6P}\over\log P}
 ={1\over2}+{\log6\over2\log P}<1.                    \tag{25}
\]

Since \(A_a\leq2\,6^a\), a geometric sum gives

\[
 \sum_{P^a\leq x}b_P(P^a)=O_P(x^{\sigma_P}).          \tag{26}
\]

Consequently

\[
 \psi_P(x)=x+O\{xe^{-\eta(\log x)}+x^{\sigma_P}\}
            =x+O_P\{xe^{-\eta(\log x)}\},             \tag{27}
\]

because \(\sigma_P<1\) and \(\eta(y)=o(y)\). The threshold and the
constant of (27) may depend on \(P\); the VK exponent does not
change.

### 3.2. Completion and exterior zero

Define

\[
 r_P(s)={1\over2}+{\log P\over\log6}
                   \left(s-{1\over2}\right),          \tag{28}
\]

so that \(T_P(s)=6^{-r_P(s)}\) and
\(r_P(1-s)=1-r_P(s)\). The function

\[
 \Xi_-(r)=6^r-5+6^{1-r}                               \tag{29}
\]

is entire and satisfies \(\Xi_-(1-r)=\Xi_-(r)\). Hence

\[
 \mathcal X_P(s)=\xi(s)\Xi_-(r_P(s))                  \tag{30}
\]

is entire and symmetric under \(s\mapsto1-s\). It is a genuine
completion of (19): if \(q=6^r\), then

\[
 \Xi_-(r)={(q-1)(q-6)\over q}\,Z_-(q^{-1}).            \tag{30a}
\]

The factor in front of \(Z_-\) cancels exactly its additional poles.
The added zeros of the completion are

\[
 {1\over2}\pm{\log(3/2)\over2\log P}
       +{2\pi ik\over\log P},\qquad k\in\mathbb Z.     \tag{31}
\]

In particular

\[
 \beta_P={1\over2}+{\log(3/2)\over2\log P}>{1\over2}. \tag{32}
\]

The Jensen term of that real zero is

\[
 \log{\beta_P\over1-\beta_P}
 =\log {\log P+\log(3/2)\over
              \log P-\log(3/2)}=D_P>0,                \tag{33}
\]

which proves (5). The remaining right-hand zeros only add nonnegative
terms.

Moreover, as \(P\to\infty\), one has

\[
 D_P\sim{2\log(3/2)\over\log P},\qquad
 \beta_P\downarrow{1\over2},                          \tag{34}
\]

and \(W_P\to1\) locally uniformly on every
\(\Re s\geq1/2+\delta\). Hence the countermodels can agree on
ever-longer prefixes and be locally invisible at fixed distance from
the boundary, even though each preserves a positive defect.

## 4. Exact scope of the falsifier

System (19) does not preserve all the data of zeta:

* it alters the tower \(P^a\) via (23);
* \(W_P\) has additional Euler poles, which are cancelled by the
  explicit factor relating \(W_P\) to (29);
* (30) contains an additional symmetric factor and is not the literal
  Riemann completion.

By the uniqueness theorem of 104_88, no different countermodel can
simultaneously preserve all the values \(\Lambda(n)\) and the same
normalization: that would pin down \(\zeta\). Thus the correct scope
is

\[
 \begin{gathered}
 \text{arbitrarily long exact prefixes + PD + positivity +}\\
 \text{ordinary support + PNT/VK + broad FE}
 \not\Longrightarrow \text{one-sided bound},          \tag{35}\\
 \text{but (35) does not rule out an inequality that literally uses all}\\
 \text{ordinary towers and the exact Riemann completion.}
 \end{gathered}
\]

The operative consequence is twofold:

1. the PD/minimax coordinate of (17) does not reduce the target;
2. no certificate by prefix compactness can close it with uniform
   constants obtained only from the qualitative data of (35).

The remaining front is still a global bound specific to the
regularized discrepancy \(dJ-d\mathrm{Li}\,\) of the ordinary
integers.

## 5. Reproduction

From the tools directory:

    python3 dual_pd_remote_tower_gate_check.py

The program verifies the finite dual identity, the numerical
positivity of the two PD matrices for a test selector, the algebraic
identities (20)--(23), the symmetry (28)--(31), the agreement on
prefixes, and the defect (33). The claims for all \(P\), all prefixes,
and all kernels are proved above; the computation is an implementation
check, not a substitute for it.
