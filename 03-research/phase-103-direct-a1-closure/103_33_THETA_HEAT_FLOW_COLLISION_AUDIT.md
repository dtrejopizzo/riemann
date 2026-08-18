# Theta heat flow and the backward-collision audit

## Purpose

This note develops the de Bruijn heat deformation directly from the positive
theta kernel of `103_15`, with no appeal to a pre-existing zero-flow theorem.
It proves the heat equation, the local zero-motion law, and the natural
positive (L^2) energy identity.  It then gives an exact positive-even,
log-concave atomic model in which real zeros collide and leave the real axis
when the flow is run backwards.

The conclusion is precise: positivity, modular evenness, and the elementary
heat energy do not provide the coercivity needed to carry real zeros back to
time zero.  A successful theta-specific proof would need a new quantitative
lower bound preventing those collisions.

## 1. The exact theta heat deformation

Let \(\Phi\) be the positive kernel of `103_15`, so that, up to an irrelevant
positive constant,
\[
 \Xi_0(z)=\xi(1/2+iz)=\int_{\mathbb R}\Phi(|u|)\cos(zu)\,du.
\tag{1}
\]
The series defining \(\Phi\) has superexponential decay.  Thus for every
real \(t\), and every compact set of \(z\)-values, multiplication by
\(e^{tu^2}\) still gives an integrable majorant for all \(z\)- and
\(t)-derivatives.  Define
\[
 \Xi_t(z)=\int_{\mathbb R}e^{tu^2}\Phi(|u|)\cos(zu)\,du.
\tag{2}
\]
It is even, real on the real axis, and entire in \(z\).  Differentiation
under the integral gives the exact backward heat equation
\[
 \boxed{\qquad \partial_t\Xi_t(z)=-\partial_z^2\Xi_t(z).\qquad}\tag{3}
\]
The Riemann hypothesis is exactly the assertion that the zeros of
\(\Xi_0\) are real: a zero \(\rho=\beta+i\gamma\) of \(\xi\) corresponds
to \(z=\gamma-i(\beta-1/2)\).

## 2. Motion of a simple zero

Let \(z_k(t)\) be a simple zero over an interval of times.  Differentiating
\(\Xi_t(z_k(t))=0\) and using (3) gives
\[
 \boxed{\qquad z_k'(t)={\Xi_t''(z_k(t))\over\Xi_t'(z_k(t))}.\qquad}\tag{4}
\]
For a finite even polynomial with simple roots \(z_j(t)\), the quotient in
(4) is exactly
\[
 z_k'(t)=2\sum_{j\ne k}{1\over z_k-z_j}.                         \tag{5}
\]
This follows by differentiating the product at a root.  Formula (5)
explains the direction of the usual real-root repulsion: for two nearby
real roots the \(4/(z_2-z_1)\) term makes their gap increase as \(t\)
increases.  It also shows the obstruction relevant here: reversing time
drives gaps toward zero, and (4) ceases to control the roots at a collision.

## 3. The positive heat energy has the wrong coercive content

For the actual theta kernel, the real-axis functions and their derivatives
are rapidly decreasing.  Integration by parts in (3) therefore gives
\[
 {d\over dt}\int_{\mathbb R}|\Xi_t(x)|^2\,dx
 =2\int_{\mathbb R}|\partial_x\Xi_t(x)|^2\,dx\ge0.               \tag{6}
\]
Equivalently, Plancherel reads this as the positive moment identity
\[
 \int_{\mathbb R}|\Xi_t(x)|^2dx
 =2\pi\int_{\mathbb R}e^{2tu^2}\Phi(|u|)^2du.                   \tag{7}
\]
This is a genuine theta-specific coercive quantity.  But it increases in
the forward heat direction and contains no lower bound for the spacing of
real zeros.  In particular, (6) remains finite through a double real zero;
it cannot rule out the backward collision required to leave the real axis.

## 4. Exact adversarial collision model

Take the positive even three-point kernel
\[
 \phi_q=\delta_{-1}+q\delta_0+\delta_1,\qquad q\ge2.             \tag{8}
\]
Its lattice weights \((1,q,1)\) are log-concave, and its exponential tilts
have the same MLR/TP2 properties audited in `103_29`.  Its heat deformation
is elementary:
\[
 X_t(z)=q+2e^t\cos z.                                             \tag{9}
\]
It satisfies the same equation \(\partial_tX_t=-\partial_z^2X_t\),
is even and real, and has all zeros real when
\[
 e^t>{q\over2}.                                                    \tag{10}
\]
At \(t_*=\log(q/2)\), it has the double real zeros
\(z=(2k+1)\pi\).  For \(t<t_*\), the zeros are
\[
 z=(2k+1)\pi\ \pm i\,\mathrm{arcosh}\,\!\left({q\over2e^t}\right),
 \qquad k\in\mathbb Z,                                           \tag{11}
\]
and are nonreal.

Thus a positive even, log-concave kernel with the same elementary tilt
ordering can have a completely real zero configuration at one time and lose
it at an explicit finite backward collision.  No argument using only those
properties can prove that \(\Xi_0\) is real-rooted.

## 5. Exact remaining theta theorem

The identities above leave a narrow non-circular target.  To use the theta
heat flow for RH, one would need a property of the *actual* \(\Phi\) which
prevents a real-zero collision on an interval ending at \(t=0\), for
example a quantitative lower bound on a suitable discriminant or on adjacent
zero gaps that remains valid under backward flow.  Such a bound must be
proved from the modular theta series, not inferred from positivity, evenness,
MLR/TP2, log-concavity, or the energy (6).

No such collision-prevention estimate is derived here.  Naming its endpoint
or a critical time without proving the estimate would only rename the
missing RH-strength input.
