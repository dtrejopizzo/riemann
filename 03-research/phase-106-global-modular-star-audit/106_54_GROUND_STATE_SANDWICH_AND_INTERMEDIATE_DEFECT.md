# 106.54 — Ground-state sandwich and the intermediate-position defect

## Purpose

Documents 106.52--106.53 put the Euler Riccati identity in \(L^2(dx)\),
but the physical generator is the Doob operator in \(L^2(\mu_K)\). This
note computes the unitary bridge exactly. It exhibits the correction which
must be subtracted from the primitive \(j_2\) lift: the two-step physical
walk carries the ground-state weight at its intermediate position.

The correction is a nonnegative square. Thus the primitive Riccati identity
does overcount the physical three-point product, and the amount of the
overcount is now explicit.

## 1. Unitary form of the full generator

Put

\[
 w(x)=\frac{h(x)K(x)}{c_K},\qquad
 \eta(x)=\left(\frac{c_KK(x)}{h(x)}\right)^{1/2},
 \qquad \mathcal Uf=w^{1/2}f.                       \tag{1}
\]

Fix a Gamma cutoff \(\varepsilon>0\) and a prime cutoff \(N\). On
\(L^2(dx)\), define the symmetric finite convolution

\[
\begin{aligned}
 H_{\varepsilon,N}
={}&\int_\varepsilon^{\varepsilon^{-1}}
 g(u)(S_u+S_{-u})\,du\\
 &+\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
 (S_{\log n}+S_{-\log n}).                          \tag{2}
\end{aligned}
\]

Let \(T_{\varepsilon,N}\) be the off-diagonal part of
\(\widetilde L_{\varepsilon,N}
=\mathcal UL_{\varepsilon,N}\mathcal U^{-1}\).

### Theorem 1 — Exact ground-state sandwich

\[
\boxed{
 T_{\varepsilon,N}
 =M_\eta H_{\varepsilon,N}M_\eta,}                  \tag{3}
\]

and

\[
\boxed{
 \widetilde L_{\varepsilon,N}
 =V_{\varepsilon,N}-T_{\varepsilon,N},}             \tag{4}
\]

where \(V_{\varepsilon,N}\) is multiplication by

\[
 V_{\varepsilon,N}(x)
 =\int c_s(x)\,d\nu_{\varepsilon,N}^{\rm sym}(s),
 \qquad c_s(x)=\frac{c_KK(x+s)}{h(x)}.               \tag{5}
\]

#### Proof

For one oriented displacement \(s\), conjugating the off-diagonal term
gives the coefficient

\[
\begin{aligned}
 w(x)^{1/2}c_s(x)w(x+s)^{-1/2}
 &=\frac{c_K\sqrt{K(x)K(x+s)}}
         {\sqrt{h(x)h(x+s)}}\\
 &=\eta(x)\eta(x+s).                                \tag{6}
\end{aligned}
\]

This is exactly the coefficient of \(M_\eta S_sM_\eta\). Summing both
orientations, the Gamma continuum and all prime powers proves (3). The
diagonal term is unchanged by a multiplication conjugation, giving
(4)--(5). \(\square\)

The factors \(1/2\) do not occur in (2): its two displayed orientations
are exactly the two terms of 106.41(7).

## 2. The sandwich is strictly contractive

### Lemma 2 — Pointwise bound

\[
\boxed{0<\eta(x)^2<\frac12\qquad(x\in\mathbb R).}    \tag{7}
\]

#### Proof

The strict log-concavity and evenness calculation of 103.34 gives
\(K(x)\le K(0)\). In the normalization \(\widehat K=\Xi\),

\[
 K(0)=\sum_{m\ge1}\pi m^2(2\pi m^2-3)e^{-\pi m^2}.  \tag{8}
\]

Using \(\pi^2<10\) and \(e^\pi>23\),

\[
 K(0)
 <20\sum_{m\ge1}\frac{m^4}{23^{m^2}}<1.             \tag{9}
\]

For completeness, the first term is \(20/23<0.87\). For \(m\ge2\), the
ratio of consecutive terms is at most
\((3/2)^4/23^5<10^{-5}\), while the first tail term is
\(16/23^4<6\times10^{-5}\); hence the whole right side of (9) is below
\(0.872\). Since \(c_K=1/2\) and \(h\ge1\),

\[
 \eta^2=\frac{K}{2h}\le\frac{K(0)}2<\frac12.
\]

Positivity follows from \(K,h>0\). \(\square\)

The weaker bound \(\eta^2<1\) is what is needed below.

## 3. Exact intermediate-position defect

### Theorem 3 — Sandwich defect

For every finite cutoff,

\[
\boxed{
\begin{aligned}
 M_\eta H_{\varepsilon,N}^2M_\eta
 -T_{\varepsilon,N}^2
 &=
 M_\eta H_{\varepsilon,N}
 (I-M_{\eta^2})
 H_{\varepsilon,N}M_\eta\\
 &=
 \bigl[
 M_{\sqrt{1-\eta^2}}H_{\varepsilon,N}M_\eta
 \bigr]^*
 \bigl[
 M_{\sqrt{1-\eta^2}}H_{\varepsilon,N}M_\eta
 \bigr]\\
 &\ge0.
\end{aligned}}                                       \tag{10}
\]

#### Proof

By (3),

\[
 T_{\varepsilon,N}^2
 =M_\eta H_{\varepsilon,N}M_{\eta^2}
  H_{\varepsilon,N}M_\eta.                          \tag{11}
\]

Subtract (11) from \(M_\eta H_{\varepsilon,N}^2M_\eta\).
Since \(H_{\varepsilon,N}=H_{\varepsilon,N}^*\) and
\(1-\eta^2>0\), the result factors as the square in (10).
\(\square\)

This is the exact form of the intermediate theta position in the physical
three-point formula. A primitive convolution first composes two shifts and
only then evaluates the ground state. The true walk evaluates the
ground-state weight between the two shifts; the difference is (10).

## 4. Where \(j_2\) occurs and what it misses

Write the prime part of (2) as

\[
 H_{p,N}=A_N+A_N^*,\qquad
 A_N=\sum_{2\le n\le N}
 \frac{\Lambda(n)}{\sqrt n}S_{\log n}.               \tag{12}
\]

The same-orientation part of \(H_{p,N}^2\), after applying the scale
derivation, is the primitive Riccati coefficient

\[
 \delta\Lambda+\Lambda*\Lambda=j_2.                 \tag{13}
\]

However, (10) proves that the physical product is not
\(M_\eta H_{p,N}^2M_\eta\). It is

\[
\boxed{
 T_{p,N}^2
 =M_\eta H_{p,N}^2M_\eta-\mathcal D_{p,N},\qquad
 \mathcal D_{p,N}
 =M_\eta H_{p,N}(1-\eta^2)H_{p,N}M_\eta\ge0,}       \tag{14}
\]

before the mixed prime--Gamma products are inserted. Thus positivity of
\(j_2\) controls an overcount. Any proof which replaces \(T_{p,N}^2\) by
the primitive \(j_2\) term and drops \(\mathcal D_{p,N}\) has the wrong
lower-bound direction.

For the complete \(H_{\varepsilon,N}=H_{p,N}+H_{\Gamma,\varepsilon}\),
the single square in (10) retains the prime--prime, prime--Gamma and
Gamma--Gamma defects jointly. No mixed term should be split from it.

## 5. The sharpened cluster target

Let \(\widetilde P=\mathcal UP_\mu\mathcal U^{-1}\) be a finite reducing
cluster. The physical curvature is

\[
 \operatorname {Tr}
 \{\widetilde P(\widetilde L^2-\tfrac12\widetilde L)\}. \tag{15}
\]

Equations (4) and (10) show that every attempted Riccati lift must include
the following three objects with their displayed signs:

\[
\begin{aligned}
 &\text{primitive completed Riccati curvature},\\
 &-\operatorname {Tr}(\widetilde P\mathcal D_{\varepsilon,N}),\\
 &\operatorname {Tr}\widetilde P
 \{V^2-VT-TV-\tfrac12V+\tfrac12T\}.                 \tag{16}
\end{aligned}
\]

Here \(\mathcal D_{\varepsilon,N}\) is the full square (10). The remaining
claim is no longer an unspecified lift of \(j_2\): it is the assertion that
the diagonal/threshold expression in the last line of (16), together with
the position-shell completion of 106.52, compensates the explicit defect
\(\mathcal D_{\varepsilon,N}\) and the centered \(j_2\) energy of 106.53.

This compensation has not been proved. Equation (10) identifies the exact
term that any successful physical three-point proof must pay.

## 6. Novelty audit

Ground-state conjugation itself is standard, and the finite compression
shell already appears in E101.063. The new result recorded here is their
exact combination in the Phase-106 full-kernel normalization: the ordinary
prime--Gamma two-step product differs from the primitive
\(j_2\) convolution by the positive intermediate-position square (10).
This is a calculation, not a claim of RH closure.
