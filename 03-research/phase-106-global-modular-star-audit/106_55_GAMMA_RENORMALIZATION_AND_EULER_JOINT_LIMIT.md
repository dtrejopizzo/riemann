# 106.55 — Gamma renormalization and the joint Euler limit

## Purpose

The small-jump Gamma diagonal and off-diagonal terms diverge separately and
must be centered. It is tempting to center the prime connection in the same
way. That is incorrect: the artificial scalar
\(\sum\Lambda(n)/\sqrt n\) then diverges although the ground-state
sandwiched prime operator is finite.

This note gives the correct mixed renormalization. Gamma is centered as a
translation Dirichlet form; the ordinary-prime part is kept as one
ground-state-sandwiched difference. The calculation also proves that the
primitive \(j_2\) term and the intermediate-position defect of 106.54 need
not possess separate infinite-cutoff limits.

## 1. The Gamma translation form

Define the nonnegative closed translation form

\[
\boxed{
 J_\Gamma
 =\int_0^\infty g(u)(2I-S_u-S_{-u})\,du.}            \tag{1}
\]

On \(H^1(\mathbb R)\),

\[
 \langle f,J_\Gamma f\rangle
 =\int_0^\infty g(u)\|f-S_uf\|_2^2\,du.             \tag{2}
\]

Near zero the integrand is \(O(u)\), because
\(g(u)=1/(2u)+O(1)\). The large-\(u\) tail is integrable. Thus (2) is
finite on a dense core and closes by monotone convergence.

Put

\[
 \eta^2=\frac{c_KK}{h},\qquad
 W_\Gamma=-\frac{c_K}{h}J_\Gamma K.                 \tag{3}
\]

### Theorem 1 — Exact Gamma renormalization

The conjugated Gamma generator is

\[
\boxed{
 \widetilde L_\Gamma
 =M_\eta J_\Gamma M_\eta+M_{W_\Gamma}.}             \tag{4}
\]

#### Proof

At cutoff \(\varepsilon\), write

\[
 H_{\Gamma,\varepsilon}
 =\int_\varepsilon^{\varepsilon^{-1}}
 g(u)(S_u+S_{-u})\,du,
\quad
 \kappa_{\Gamma,\varepsilon}
 =\int_\varepsilon^{\varepsilon^{-1}}g(u)\,du.
\]

Then
\(H_{\Gamma,\varepsilon}
=2\kappa_{\Gamma,\varepsilon}I-J_{\Gamma,\varepsilon}\).
The off-diagonal sandwich is

\[
 T_{\Gamma,\varepsilon}
 =2\kappa_{\Gamma,\varepsilon}M_{\eta^2}
  -M_\eta J_{\Gamma,\varepsilon}M_\eta.             \tag{5}
\]

Its diagonal partner is

\[
 V_{\Gamma,\varepsilon}
 =2\kappa_{\Gamma,\varepsilon}\eta^2
  -\frac{c_K}{h}J_{\Gamma,\varepsilon}K.             \tag{6}
\]

Subtracting (5) from (6) cancels the divergent scalar before the limit.
Form convergence gives (4). \(\square\)

## 2. The prime part must remain uncentered

Let

\[
\begin{aligned}
 H_{p,N}
 &=\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
   (S_{\log n}+S_{-\log n}),\\
 T_{p,N}&=M_\eta H_{p,N}M_\eta,\\
 V_{p,N}(x)
 &=\frac{c_K}{h(x)}
 \sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
 \{K(x-\log n)+K(x+\log n)\}.                       \tag{7}
\end{aligned}
\]

The prime generator is

\[
 \widetilde L_{p,N}=V_{p,N}-T_{p,N}.                \tag{8}
\]

### Proposition 2 — Joint prime cutoff removal

The forms \(\widetilde L_{p,N}\) increase to the closed positive prime
form. On the smooth compact core, both expressions in (7) converge in the
joint difference (8), and

\[
\boxed{\widetilde L_p=V_p-T_p}                      \tag{9}
\]

in the form sense.

#### Proof

Undoing the unitary conjugation, the quadratic form of (8) is exactly

\[
 \sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
 \int K(x)K(x-\log n)|f(x)-f(x-\log n)|^2\,dx.      \tag{10}
\]

Every summand is nonnegative. Monotone convergence therefore defines the
closed limit, and double-exponential decay of one of the two \(K\)-factors
gives convergence on the compact core. Conjugating back proves (9).

In fact, the off-diagonal operators converge in norm. Since \(K\) is
log-concave, \(h\) is log-convex, and
\(\log\eta=\tfrac12(\log(c_KK)-\log h)\), the function \(\eta\) is even
and log-concave. Therefore the product below is maximized at the midpoint:

\[
 \|M_\eta S_aM_\eta\|
 \le\sup_x\eta(x)\eta(x+a)=\eta(a/2)^2.              \tag{10a}
\]

For \(a=\log n\), the theta formula gives
\(\eta(a/2)^2\ll\exp(-c n)\). Hence

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \|M_\eta S_{\log n}M_\eta\|<\infty,                \tag{10b}
\]

so \(T_{p,N}\to T_p\) in operator norm.
\(\square\)

By contrast, if

\[
 \kappa_{p,N}=\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n},
\qquad
 J_{p,N}=2\kappa_{p,N}I-H_{p,N},                    \tag{11}
\]

then \(\kappa_{p,N}\to\infty\) and neither
\(M_\eta J_{p,N}M_\eta\) nor
\(V_{p,N}-2\kappa_{p,N}\eta^2\) has a finite limit separately.
Their cancellation merely reconstructs (8). Thus there is no cutoff-free
prime analogue of (4) obtained by scalar centering.

## 3. Correct cutoff-free full generator

Combining (4) and (9) gives

\[
\boxed{
 \widetilde L
 =M_\eta J_\Gamma M_\eta+W_\Gamma+V_p-T_p.}         \tag{12}
\]

All four terms in (12) are interpreted through their closed forms, with
\(V_p-T_p\) retained jointly.

Let

\[
 \mathfrak g=\left(\frac{hK}{c_K}\right)^{1/2}.
\]

Since \(\eta\mathfrak g=K\), the Gamma and prime parts separately annihilate
the ground state:

\[
\begin{aligned}
 (M_\eta J_\Gamma M_\eta+W_\Gamma)\mathfrak g&=0,\\
 (V_p-T_p)\mathfrak g&=0.                           \tag{13}
\end{aligned}
\]

For the second identity,
\(T_p\mathfrak g=\eta H_pK\), while
\(V_p\mathfrak g=(c_K/h)\mathfrak g\,H_pK=\eta H_pK\).

## 4. Consequence for the \(j_2\) square

At every finite prime cutoff, 106.54 gives

\[
\boxed{
 T_{p,N}^2
 =M_\eta H_{p,N}^2M_\eta
 -M_\eta H_{p,N}(1-\eta^2)H_{p,N}M_\eta.}           \tag{14}
\]

The first term contains the primitive
\(\delta\Lambda+\Lambda*\Lambda\) after the position derivation is added.
The second is the positive intermediate-position defect.

### Theorem 3 — No separate \(j_2\) limit

The two terms on the right side of (14) are not individually controlled by
the closed prime form as \(N\to\infty\). Only their difference, the
physical two-step operator \(T_{p,N}^2\), has the cutoff meaning supplied
by the complete cluster trace.

#### Proof

Take a nonzero \(f\in C_c^\infty\) and put \(\phi=\eta f\). Its Fourier
transform is entire and not identically zero, so at the origin

\[
 |\widehat\phi(t)|\ge c|t|^r
\]

on a sufficiently small interval, for some finite \(r\ge0\). For
\(0\le t\le(\log N)^{-1}\) and \(n\le N\),
\(\cos(t\log n)\ge\cos1>0\). Hence

\[
\begin{aligned}
 \langle f,M_\eta H_{p,N}^2M_\eta f\rangle
 &=\|H_{p,N}\phi\|_2^2\\
 &\ge c_r\,
 \frac{\kappa_{p,N}^2}{(\log N)^{2r+1}}.             \tag{15a}
\end{aligned}
\]

Chebyshev's estimate gives
\(\kappa_{p,N}\gg\sqrt N\), so (15a) tends to infinity. On the other
hand \(T_{p,N}\) converges on the physical form core by Proposition 2.
Identity (14) then forces the quadratic form of the defect to diverge by
the same leading amount. Thus neither term on the right of (14) has the
separate cutoff limit, although their difference does. \(\square\)

Therefore \(j_2\ge0\) can be used only inside a common finite-cutoff
identity in which the defect in (14), the prime diagonal \(V_{p,N}\), the
Gamma form (4), and the polar threshold are still present.

## 5. Central Gamma well

The finite Gamma potential is genuinely signed:

\[
\boxed{W_\Gamma(0)<0.}                              \tag{15}
\]

Indeed, \(K\) is even and strictly decreasing on \((0,\infty)\), so
\(K(-u)+K(u)-2K(0)<0\) for every \(u>0\). Formula (3) gives (15).
Thus even the correctly renormalized Gamma potential cannot be discarded
as a positive correction.

## 6. Revised physical target

The cutoff-free generator is (12), but its curvature must be evaluated
from a *common finite cutoff* before using \(j_2\). The remaining estimate
is the joint lower bound for

\[
 \mathrm{Tr}\,\widetilde P
 \left\{\widetilde L_{\varepsilon,N}^2
 -\frac12\widetilde L_{\varepsilon,N}\right\},       \tag{16}
\]

where the following are kept in one expression:

1. the primitive \(j_2\) convolution;
2. the intermediate-position defect (14);
3. both prime diagonal cross terms;
4. the centered Gamma form and its negative potential;
5. the polar threshold and the projection-position shell.

This corrects the false fully centered prime--Gamma decomposition. It also
shows why the desired proof cannot be obtained by first passing
\(j_2\) to an independent positive limiting operator.
