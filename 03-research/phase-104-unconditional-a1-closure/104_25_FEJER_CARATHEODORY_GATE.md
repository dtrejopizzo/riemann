# 104_25 — Fejér–Carathéodory gate and the exact holomorphy barrier

**Role.** Test the shortest analytic mechanism that would turn the cubic
cocycle into the margin \(3\lambda_n-A_n\), and audit whether it supplies
unconditional information. The mechanism is correct: a Carathéodory bound
on the disc produces every sign through the Fejér kernel. However, for the
completed cocycle, mere holomorphy on those discs as
\(\varepsilon\downarrow0\) is already equivalent to RH. On smaller safe
discs one only obtains damped averages, insufficient
coefficient-by-coefficient.

This document proves neither A1 nor RH.

## 1. Exact Fejér identity

Fix \(u>0\), and write

\[
 \Phi(z)=\mathcal S_u^{[3]}(s_\varepsilon(z))
          =\sum_{k\ge0}a_kz^k,
 \qquad s_\varepsilon(z)=1+\varepsilon+{z\over1-z}.       \tag{1}
\]

Define the margin-signed normalization:

\[
 Q(z):={1-\Phi(z)\over u(1-z)^2}=\sum_{m\ge0}q_mz^m.      \tag{2}
\]

Multiplying series gives, with no additional analytic hypothesis,

\[
 \boxed{
 q_m={1\over u}\left[(m+1)-
       \sum_{k=0}^m(m-k+1)a_k\right]
 ={m+1\over u}\bigl(1-\sigma_m(\Phi;1)\bigr),}           \tag{3}
\]

where

\[
 \sigma_m(\Phi;1)=
 \sum_{k=0}^m\left(1-{k\over m+1}\right)a_k.             \tag{4}
\]

By `104_22`, along \(u=c\varepsilon\),

\[
 \boxed{q_{n-1}\longrightarrow 3\lambda_n-A_n.}          \tag{5}
\]

**Theorem 1.1 (Fejér–Carathéodory).** Suppose
\(\Phi\in\mathrm{Hol}(\mathbb D)\), that its coefficients are real, and
that

\[
 \Re\Phi(z)\le1\qquad(z\in\mathbb D).                    \tag{6}
\]

Then \(q_m\ge0\) for every \(m\ge0\).

**Proof.** The function \(g=1-\Phi\) has non-negative real part. Since
\(g(0)=1-a_0\) and all its coefficients are real, its Herglotz
representation can be taken with no imaginary constant, with a positive
measure \(\mu\) normalized by \(\mu(\mathbb T)=g(0)\). The combination in
(3) is

\[
 \boxed{
 q_m={m+1\over u}\int_{-\pi}^{\pi}F_m(t)\,d\mu(t),}       \tag{7}
\]

with

\[
 F_m(t)=1+2\sum_{k=1}^m
 \left(1-{k\over m+1}\right)\cos(kt)
 ={1\over m+1}\left|\sum_{j=0}^me^{ijt}\right|^2\ge0.   \tag{8}
\]

Hence (7) is non-negative. In particular, the stronger condition
\(|\Phi(z)|\le1\) also suffices. \(\square\)

## 2. The required holomorphy already equals RH

For \(u_j=c\varepsilon_j\), \(0<c<1\),
\(\varepsilon_j\downarrow0\), let

\[
 \Phi_j(z)={Y_3(s_{\varepsilon_j}(z)-u_j)
                 \over Y_3(s_{\varepsilon_j}(z))}.        \tag{9}
\]

The Cayley map (1) is a bijection

\[
 s_\varepsilon(\mathbb D)
 =\{s:\Re s>\tfrac12+\varepsilon\},
 \qquad
 z={s-1-\varepsilon\over s-\varepsilon}.                 \tag{10}
\]

**Theorem 2.1.** The following statement is equivalent to RH:

> there exists a sequence \(\varepsilon_j\downarrow0\) for which each
> \(\Phi_j\) is holomorphic on \(\mathbb D\).

**Proof.** Under RH, the denominator of (9) has no zeros in half-plane
(10), so (9) is holomorphic.

Conversely, suppose \(\xi(\rho)=0\) with
\(\Re\rho>1/2\). For every sufficiently large \(j\), \(\rho\) belongs to
half-plane (10). Since \(G\) is regular and nonzero in the critical strip,
removability in (9) forces

\[
 \xi(\rho-c\varepsilon_j)=0.                              \tag{11}
\]

A subsequence gives infinitely many distinct zeros converging to
\(\rho\), contradicting the isolation of zeros of a nonzero entire
function. There are, therefore, no zeros to the right of the line. The
functional equation and conjugation also exclude those to the left.
\(\square\)

Thus, directly applying Theorem 1.1 to a sequence that removes the
regulator would introduce the desired conclusion already in the
holomorphy hypothesis, before using inequality (6).

## 3. Even an eventual sign at fixed regulator forces the disc

There is a coefficient-by-coefficient version of the same barrier. With
\(\varepsilon>0\) fixed, suppose the coefficients of (2) satisfy
\(q_m\ge0\) for every sufficiently large \(m\). The cocycle is regular for
\(0<z<1\), because there \(s_\varepsilon(z)>1\). If the tail were a
polynomial, the radius of \(Q\) would be infinite. Otherwise, if the
radius were \(R<1\), Pringsheim's theorem, applied after removing the
finite prefix, would force a singularity at the positive real point
\(z=R\). But the meromorphic formula for \(\Phi\) is holomorphic in a
neighborhood of every point of \((0,1)\); by overlap the germ continues
up to that neighborhood, a contradiction. Hence \(R\ge1\), and (2)
holomorphically extends \(\Phi\) to \(\mathbb D\).

Consequently, proving that eventual sign for each member of a sequence
\(\varepsilon_j\downarrow0\) again implies RH by Theorem 2.1. This does
not make limit (5) circular; it shows that a proof attempting to
strengthen it to all coefficients at fixed regulator already contains RH.

## 4. The safe disc does not transfer the sign

The Euler Dirichlet series is only guaranteed on
\(\Re s>1+u\). Setting \(\delta=\varepsilon-u\), for
\(0<\delta<1/2\) the largest disc centered at zero that map (1) places
entirely within that half-plane has radius

\[
 R_\varepsilon={\varepsilon-u\over1-\varepsilon+u}
 \sim(1-c)\varepsilon\longrightarrow0.                    \tag{12}
\]

In general the radius is \(\min\{1,\delta/(1-\delta)\}\); the formula
shown is the one governing the regime used here,
\(u=c\varepsilon\), \(\varepsilon\downarrow0\).

Even granting a Schur bound on \(|z|\le R_\varepsilon\), Fejér would only
control averages with damping factors \(R_\varepsilon^k\). There is no
formal transfer to the undamped coefficient. The following witness proves
this exactly.

Let \(0<R<1\), choose \(N\) so that \(R^{-N}>N+1\), and take

\[
 \Phi(z)=a+Mz^N,\qquad
 (N+1)(1-a)<M\le(1-a)R^{-N},\quad0\le a<1.       \tag{13}
\]

Then \(|\Phi(z)|\le1\) for \(|z|\le R\), but

\[
 q_N={(N+1)(1-a)-M\over u}<0.                    \tag{14}
\]

Hence the information on any strictly smaller disc is not enough, without
a new special inequality for the arithmetic cocycle.

## Status

- **Proved:** identity (3), the Fejér–Carathéodory mechanism, and the
  exact equivalence between holomorphy on the regulated discs and RH.
- **Ruled out:** obtaining the cubic margin by applying
  Carathéodory/Schur on the full disc as an independent input; and
  formally transferring the sign from the small Euler convergence disc.
- **Open:** a signed inequality acting directly on limit (5), with no
  requirement of global holomorphy nor of an eventual sign at fixed
  regulator.
</content>
