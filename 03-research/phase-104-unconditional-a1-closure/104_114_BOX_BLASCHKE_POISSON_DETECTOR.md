# 104_114 — Blaschke–Poisson detector of the deep box

**Question.** After `104_112`–`104_113`, the front is excluding the box

\[
 0<\gamma\lesssim T,\qquad
 \beta-\frac12\gtrsim{\gamma^2\over T^2}.                \tag{1}
\]

Is there a local form, in the Cayley disc, that detects exactly those
zeros and can be turned into a new inequality for the ordinary primes?

**Result.** There is an exact detector, but it is not a new source of
sign. In the coordinate

\[
 s={1\over1-z},\qquad E(z)=(s-1)\zeta(s),
\]

the zeros with \(\Re\rho>1/2\) are the interior zeros

\[
 a_\rho={\rho-1\over\rho}=e^{-a_\rho^{\rm rad}+i\theta_\rho}.
\]

Box (1) is equivalent to a family of Carleson boxes

\[
 1-|a_\rho|\gtrsim T^{-2},\qquad |\theta_\rho|\gtrsim T^{-1}
 \quad(\hbox{with } |\theta_\rho|\asymp \gamma^{-1}).      \tag{2}
\]

For \(z\in\mathbb D\), the factorization from `104_111`
\[
 E(z)=B(z)O(z)
\]
gives the exact deficit

\[
 \boxed{
 \mathcal J(z):=
 P_z(\log|E^*|)-\log|E(z)|
 =
 \sum_{\Re\rho>1/2} m_\rho
 \log\left|
 {1-\overline{a_\rho}z\over z-a_\rho}
 \right|.
 }                                                       \tag{3}
\]

Here \(P_z\) is the Poisson integral at the boundary. Hence
\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 \mathcal J(z)\equiv0\quad(z\in\mathbb D).              \tag{4}
\]

Moreover, a zero in box (1) produces a positive spike of size
\(\gg1\) in \(\mathcal J(z)\) for a \(z\) in the same hyperbolic box. So,
excluding \(R_T\) is equivalent to proving
\[
 \sup_{z\in\mathcal C_T}\mathcal J(z)\longrightarrow0
\]
over a cofinal family of boxes \(\mathcal C_T\).

This detector is useful as an exact coordinate for the obstacle, but it
does not prove RH. Any proof of \(\mathcal J=0\) is exactly the removal
of the interior Blaschke factor of `104_111`. The boundary term
\(P_z(\log|E^*|)\) lives on the critical line; turning it into an
ordinary prime inequality returns to Weil's explicit formula. Hence the
Poisson–Jensen/outer-function route is not an independent source of
sign.

---

## 1. Geometry of the box in the disc

For \(\rho=\beta+i\gamma\), \(\beta>1/2\), set

\[
 a_\rho^{\rm rad}
 ={1\over2}\log{|\rho|^2\over|\rho-1|^2}.
\]

Then

\[
 |a_\rho|=e^{-a_\rho^{\rm rad}},\qquad
 a_\rho^{\rm rad}\asymp{\beta-\frac12\over\gamma^2}.
\]

The phase satisfies

\[
 \theta_\rho=\arg{\,\rho-1\over\rho}
 =\arg\left(1-{1\over\rho}\right),
 \qquad |\theta_\rho|\asymp{1\over\gamma}
\]

for \(\gamma\ge2\). Hence (1) translates into

\[
 1-|a_\rho|\asymp a_\rho^{\rm rad}\gtrsim T^{-2},
 \qquad |\theta_\rho|\gtrsim T^{-1}.                    \tag{5}
\]

The radial boundary \(T^{-2}\) coincides with the scale of the Deep
detector: a mode with \(1-|a|\asymp T^{-2}\) has growth
\(\exp(n/T^2)\), and at degrees \(n\asymp T^4\) it reaches
\(\exp(T^2)=e^{\sqrt X}\).

## 2. Exact local Jensen

The factorization from `104_111` gives \(E=BO\), with no singular
interior factor. For the normalized Blaschke product

\[
 b_a(z)={|a|\over a}{a-z\over1-\bar a z},
 \qquad b_a(0)=|a|,
\]

one has
\[
 \log|B(z)|
 =\sum_{\Re\rho>1/2}m_\rho
 \log\left|{a_\rho-z\over1-\overline{a_\rho}z}\right|.
\]

Since \(O\) is exterior,

\[
 \log|O(z)|=P_z(\log|E^*|).
\]

Subtracting \(\log|E(z)|=\log|B(z)|+\log|O(z)|\) gives (3). The quantity
\(\mathcal J(z)\) is non-negative and vanishes at a point if and only if
no interior zero contributes to the potential seen from that point. It
vanishes identically if and only if \(B\equiv1\).

## 3. A zero of the box produces a spike

Let \(a\in\mathbb D\) be an interior zero. Take \(z\) on the same radius,
with
\[
 1-|z|=\kappa(1-|a|),\qquad 0<\kappa<1,\qquad \arg z=\arg a.
\]

Then
\[
 \left|{1-\bar a z\over z-a}\right|
 ={1-|a||z|\over ||z|-|a||}
 ={(1-|a|)+|a|(1-|z|)\over |(1-|a|)-(1-|z|)|}.
\]

If \(1-|z|=\kappa(1-|a|)\), the ratio tends to
\[
 {1+\kappa\over1-\kappa}
\]
as \(|a|\to1\). So a single zero of the box contributes at least
\[
 \log{1+\kappa\over1-\kappa}+o(1)                       \tag{6}
\]
to \(\mathcal J(z)\), with multiplicity. The detection is local and of
constant size; it is not lost in averages.

## 4. Why this is not a new closing mechanism

Identity (3) proves that the correct detector exists and is positive. The
problem is that its positivity is that of the Blaschke factor, not an
arithmetic inequality that makes it vanish. To conclude RH one would have
to prove

\[
 P_z(\log|E^*|)\le \log|E(z)|
 \qquad(z\in\mathbb D),                                  \tag{7}
\]

because the opposite inequality is the automatic subharmonicity of
\(\log|E|\). But (7) is exactly saying that there is no interior factor.

In terms of primes, \(\log E(z)\) in \(\Re s>1\) has an Euler series, but
\(P_z(\log|E^*|)\) lives on the boundary \(\Re s=1/2\). Transporting that
boundary to the primes requires Weil's explicit formula with a test
adapted to the Poisson kernel. The contribution of an interior zero is
precisely the positive term of (3). Hence the inequality that would make
\(\mathcal J\) vanish is Weil-positivity/RH for this family of tests, not
a consequence of PNT, density, or the exterior factorization.

## 5. Consequence

The deep box can be attacked in two equivalent coordinates:

1. the Li/Deep coordinate of `104_75`–`104_113`, where a zero in the box
   produces deep negative excursions;
2. the Blaschke–Poisson coordinate (3), where the same zero produces a
   local positive Green spike.

Both isolate the same interior factor. Neither reduces the final task. A
genuine successor would have to prove an ordinary prime inequality
forcing \(\mathcal J(z)=0\) on cofinal boxes and failing for the exterior
Euler models. In the absence of that inequality, the detector is a clean
coordinate for the obstacle, not a proof of RH.
</content>
