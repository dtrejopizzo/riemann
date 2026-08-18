# 106.30 — Quantitative cyclicity conditioning stop gate

## Result

The translates and derivatives of Riemann's full kernel are cyclic in
ordinary \(L^2(\mathbb R)\): their Fourier transforms have the common factor
\(\Xi(t)\), which is nonzero almost everywhere on the real axis.  This does
not yield the complementary lower floor left open by 106.27.

The obstruction is quantitative and exact.  If an off-line zero
\(\rho=\beta+i\gamma\), \(\beta>1/2\), exists, complex evaluation on the
Paley--Wiener window forces every truncated radical approximant of a test
which detects \(\rho\) to have squared \(L^2\)-error at least

\[
 \asymp \lambda^{-2(\beta-1/2)}.
\]

The available semilocal lower bound costs \(\asymp\lambda\) times this
error.  Its product therefore grows as

\[
 \lambda^{2(1-\beta)},
\]

and cannot tend to zero.  Thus qualitative Wiener cyclicity has exactly the
wrong conditioning for the semilocal inertia problem.  This rules out the
proposed growing-radical-density argument; it does not rule out a genuinely
new arithmetic complement estimate.

## 1. Setup

Put

\[
 I_L=[-a,a],\qquad a=L/2,\qquad \lambda=e^a.
\]

For a nontrivial zero \(\rho=\beta+i\gamma\), write

\[
 z_\rho=\gamma-i\eta,\qquad \eta=\beta-\frac12.
\]

Then \(1/2+iz_\rho=\rho\).  Assume \(\eta>0\); by the functional equation
this loses no generality if RH is false.

The exact positive-square decomposition of 106.17 gives

\[
 A_L^+=\mathcal L_{e^L}^+-\kappa_{e^L}I,
 \qquad \mathcal L_{e^L}^+\ge0,
 \qquad \kappa_{e^L}=4\lambda+o(\lambda).
\]

Consequently

\[
 \langle A_L^+r,r\rangle\ge-\kappa_{e^L}\|r\|_2^2.
 \tag{1}
\]

## 2. The complex-evaluation barrier

### Theorem 1

Let \(h\in L^2(\mathbb R)\) have fixed compact support and suppose

\[
 H_\rho:=\widehat h(z_\rho)\ne0.
\]

Let \(v_L\in L^2(I_L)\) satisfy

\[
 \widehat v_L(z_\rho)=o(1).
 \tag{2}
\]

Then

\[
 \boxed{
 \|h-v_L\|_2^2
 \ge (1+o(1))|H_\rho|^2
 \frac{\eta}{\sinh(2\eta a)}
 \gg_{h,\rho}\lambda^{-2\eta}.}
 \tag{3}
\]

In particular,

\[
 \boxed{
 \kappa_{e^L}\|h-v_L\|_2^2
 \gg_{h,\rho}\lambda^{1-2\eta}
 =\lambda^{2(1-\beta)}\longrightarrow\infty.}
 \tag{4}
\]

#### Proof

For all sufficiently large \(L\), both \(h\) and \(v_L\) are supported in
\(I_L\).  Put \(r_L=h-v_L\).  Cauchy--Schwarz gives

\[
 \begin{aligned}
 |\widehat r_L(z_\rho)|^2
 &\le \|r_L\|_2^2
 \int_{-a}^{a}|e^{-iz_\rho x}|^2\,dx\\
 &=\|r_L\|_2^2
 \int_{-a}^{a}e^{-2\eta x}\,dx\\
 &=\|r_L\|_2^2\frac{\sinh(2\eta a)}{\eta}.
 \end{aligned}
\]

By (2), \(\widehat r_L(z_\rho)=H_\rho+o(1)\).  This proves (3).  Since
\(0<\eta<1/2\) and \(\kappa_{e^L}=4\lambda+o(\lambda)\), multiplication by
\(\kappa_{e^L}\) proves (4). \(\square\)

## 3. Why this stops the growing radical frame

Every finite linear combination of translates and derivatives of \(K\) has
Fourier transform

\[
 \widehat u(z)=P(z)\Xi(z)
\]

with an exponential polynomial \(P\).  Hence

\[
 \widehat u(z_\rho)=0
 \tag{5}
\]

at every nontrivial zero, independently of the number of modes.  Smooth
truncation gives \(v_L=\chi_a u\).  Whenever the exterior-tail estimate is
strong enough to retain the operator-quasimode conclusion of 106.27, it in
particular gives (2) for each fixed zero.

Ordinary \(L^2\)-cyclicity only asserts that one can make
\(\|h-u\|_2\) small with no relation between the error and the spatial
radius or coefficient conditioning.  To transfer the quasimode inequality
to a fixed test using (1), one would need

\[
 \kappa_{e^L}\|h-v_L\|_2^2=o(1),
 \tag{6}
\]

equivalently an error \(o(\lambda^{-1/2})\).  Theorem 1 says that (6) is
impossible for every test which detects an off-line zero.  The exponent is
strictly adverse for every \(1/2<\beta<1\).

This is the quantitative version of the common-\(\Xi\)-factor obstruction
found for fixed frames in 106.13--106.14.  Allowing the number of translates
or derivatives to grow does not remove it: either their truncated complex
evaluations remain small, in which case (3)--(4) apply, or coefficient and
boundary growth destroys the operator residual before cyclicity can be used.

## 4. Audit boundary

This stop gate does not duplicate the earlier statements.

- 106.09 proves small finite scalar Weil matrices.
- 106.13 proves asymptotic orthogonality of a fixed derivative family to an
  off-line evaluation mode.
- 106.14 proves that every fixed finite radical frame misses a negative
  direction and records an aggregate-residual obstruction.
- 106.27 proves one full operator quasimode from a smooth cutoff.

The new statement is the radius-dependent lower bound (3), and its exact
comparison with the semilocal floor scale in (4).  It closes only the
proposal that ordinary cyclicity plus double-exponential tails could supply
the missing complement floor.

The floor itself is not a new logical weakening of the old semilocal
spectral-bottom criterion.  Phase 35, Doc. 99, already records
\(\liminf_L\inf\sigma(A_L)\ge0\) as an RH-equivalent spectral statement,
and Phase 37, Doc. 110, restates it as absence of negative spectral flow.
Once 106.27 supplies a zero quasimode, the codimension-one floor below is
asymptotically equivalent to that old obstruction by 106.25.  Likewise, the
ground-state/Hardy route was already tested in Phase 60; 106.19 gives its
exact modern form and proves that its Poincare constant is the missing
inequality itself.

The live theorem remains

\[
 \inf_{\substack{g\perp q_L^K\\g\ \mathrm{even}\\\|g\|_2=1}}
 \langle A_L^+g,g\rangle\ge-o(1),
\]

or an equivalent arithmetic signed estimate which cannot be obtained from
unconditioned \(L^2\) density of the Weil radical.
