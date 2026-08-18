# Euler--Gamma Carathéodory margin audit

## Purpose

This note audits the variational, Toeplitz--Schur, second-difference, and
Fejer routes in `142`, `164`, `198`, and `202`.  It isolates one exact
completed Euler--Gamma candidate which is stronger than the generic theta
moment statements:

* its unshifted Carathéodory positivity is **exactly equivalent to RH**;
* its formal half-archimedean Loewner strengthening would imply the strong
  margin and hence A1 after A0, but is false even under RH;
* all generating-function and Schur identities below are unconditional.

The required positivity is not proved.  The point of the audit is to state
it without hiding the RH-strength step in a formal factorisation.

The four earlier formulations are the same requirement at different levels:
`142` asks for a non-tautological positive Friedrichs energy; `164` asks for
its Toeplitz Schur margin; `198` evaluates that margin on the Dirichlet
vector; and `202` asks for enough Fejer mass near the boundary point (1).
Equations
(12)--(18) below identify their common completed Euler--Gamma symbol.

## 1. Exact disk generator from the completed logarithmic derivative

For (a>1), set
\[
 s_a(z)={a\over1-z},\qquad
 \mathcal L_a(z)=\sum_{n\ge1}\lambda_n(a)z^n
 =z{d\over dz}\log\xi(s_a(z)),
\tag{1}
\]
where the coefficients are understood in the regulated disk from `103_14`.
Let
\[
 g_0(a)=2\lambda_1(a),\qquad
 g_m(a)=\lambda_{m+1}(a)-2\lambda_m(a)+\lambda_{m-1}(a)\quad(m\ge1).
\tag{2}
\]
The symmetric Carathéodory generator of these second differences is
\[
 \mathfrak C_a(z):=g_0(a)+2\sum_{m\ge1}g_m(a)z^m.
\tag{3}
\]

The following identity is exact:
\[
 \boxed{\quad
 \mathfrak C_a(z)
 ={2(1-z)^2\over z}\mathcal L_a(z)
 =2a\,{\xi'\over\xi}\!\left({a\over1-z}\right).
 \quad}                                                          \tag{4}
\]
Indeed, the one-sided calculation gives
\[
 g_0(a)+\sum_{m\ge1}g_m(a)z^m
 =\lambda_1(a)+{(1-z)^2\over z}\mathcal L_a(z).
\]
Subtracting its constant term \(g_0(a)=2\lambda_1(a)\) after reflection
gives (4).  This proves the coefficient identity before any positivity is
asserted.

In the Euler-product region, (4) is the explicit completed expression
\[
 {\mathfrak C_a(z)\over2a}
 ={1\over s}+{1\over s-1}-{1\over2}\log\pi
 +{1\over2}\psi\!\left({s\over2}\right)+{\zeta'\over\zeta}(s),
 \qquad s={a\over1-z}.
\tag{5}
\]
Thus the prime, pole, and Gamma terms are paired *before* a boundary
positivity claim is made.  This is the concrete Euler--Gamma content absent
from an arbitrary positive theta measure.

## 2. The exact RH gate

Consider the completed Carathéodory inequality
\[
 \boxed{\qquad \Re\mathfrak C_1(z)\ge0\qquad(|z|<1).\qquad}       \tag{CP}
\]
Here \(\mathfrak C_1\) is defined at the base point by the analytic
completed logarithm in (1), not by separating the divergent terms in (5).
The map \(s=1/(1-z)\) sends the unit disk conformally onto
\(\Re s>1/2\).  Hence (4) turns (CP) into
\[
 \Re {\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).                    \tag{6}
\]

This is not a new soft positivity theorem.  It is exactly RH:
\[
 \boxed{\quad (CP)\ \Longleftrightarrow\ RH.\quad}              \tag{7}
\]
For completeness, if (6) held and \(\xi(\rho)=0\) with
\(\Re\rho>1/2\), then the real part of \(\xi'/\xi\) has both signs in
every punctured neighbourhood of the pole at \(\rho\), a contradiction.
The functional equation then excludes zeros left of the line.  Conversely,
under RH the paired zero divisor gives
\[
 \Re{\xi'\over\xi}(s)
 =\sum_\rho {\Re s-1/2\over |s-\rho|^2}>0
 \qquad(\Re s>1/2),                                                \tag{8}
\]
with symmetric limiting interpretation.  This proves (7).

Equivalently, the kernel
\[
 \mathcal K_a(z,w)
 ={\mathfrak C_a(z)+\overline{\mathfrak C_a(w)}\over1-z\bar w}
\tag{9}
\]
is positive semidefinite for every finite set of disk points precisely when
\(\Re\mathfrak C_a\ge0\).  At \(a=1\) this is an RH-equivalent kernel
positivity statement, not a consequence of the Euler product in
\(\Re s>1\).

There is a useful structural consequence under RH.  On \(|z|=1\), apart
from the image of the zeros and the point \(z=1\), the map
\(s=1/(1-z)\) has \(\Re s=1/2\).  Functional equation plus reality gives
\(\Re(\xi'/\xi)=0\) there.  The Herglotz measure of \(\mathfrak C_1\)
is therefore singular.  Its pole at
\[
 w_\rho=1-{1\over\rho}\in\partial\mathbb D
\]
has positive atomic mass \(1/|\rho|^2\) when
\(\rho=1/2+i\gamma\).  Indeed, the residue of
\(2\xi'/\xi(1/(1-z))\) at \(w_\rho\) is \(2/\rho^2\), whereas an atom
of mass \(\mu\) at \(w\) contributes residue \(-2\mu w\); on the line,
\(-1/(w_\rho\rho^2)=1/|\rho|^2\).  There is no atom at \(1\), since
the completed logarithmic derivative has only logarithmic growth there.
Thus the exact RH measure is atomic; there is no independent bounded
``archimedean density'' that can furnish the Fejer margin for free.  This
explains the density obstruction in `202`.

## 3. Formal Loewner margin identity and its obstruction

Let
\[
 \mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n
\tag{10}
\]
be the already paired archimedean generator used in the A1 decomposition,
and define its second-difference generator by
\[
 \mathfrak C_{\rm arch}(z)
 ={2(1-z)^2\over z}\mathcal A(z).
\tag{11}
\]
Both (10) and (11) are analytic at zero.  In particular, (11) does not
illegitimately split the pole from the Gamma factor at the base point.

Define the strong-margin symbol
\[
 \boxed{\quad
 \mathfrak C_{\rm SM}(z)
 :=\mathfrak C_1(z)-\tfrac12\mathfrak C_{\rm arch}(z)
 ={2(1-z)^2\over z}
 \left(\mathcal L(z)-\tfrac12\mathcal A(z)\right).
 \quad}                                                          \tag{12}
\]
It has coefficient sequence
\[
 g_m^{\rm SM}=g_m-\tfrac12g_m^{\rm arch}\qquad(m\ge0).           \tag{13}
\]
Using the prime--pole generator of `141`, the same identity has the exact
Euler--Gamma form
\[
 \mathfrak C_{\rm SM}(z)
 ={\mathfrak C_{\rm arch}(z)\over2}
 +2\left[{1\over s-1}+{\zeta'\over\zeta}(s)\right],
 \qquad s={1\over1-z},                                            \tag{14}
\]
initially for \(\Re s>1\), with the right side continued only as the paired
completed expression (12).  Formula (14) suggests the following formal
Euler--Gamma Loewner condition:
\[
 \boxed{\qquad
 \mathcal K_{\rm SM}(z,w):=
 {\mathfrak C_{\rm SM}(z)+\overline{\mathfrak C_{\rm SM}(w)}
  \over1-z\bar w}\succeq0.
 \qquad}                                                          \tag{EGSM}
\]

It is a Loewner/Schur factorisation requirement on the *completed,
prime-pole-paired* symbol, not coefficientwise positivity of Euler factors.
The local-factor calculation in `103_14` shows why such a conclusion cannot
be proved one Euler factor at a time.

It is crucial that (EGSM) is **not** a viable conjectural theorem.  The
archimedean boundary calculation in `103_25` proves that, even under RH,
\[
 \Re\mathfrak C_{\rm SM}(z)<0
\]
at interior points arbitrarily close to the critical-line boundary at large
height.  Hence its one-point kernel already fails positivity.  Equations
(12)--(16) remain exact algebra, but (EGSM) is only a no-go diagnostic.

## 4. What (EGSM) proves

Expanding the positive kernel (EGSM) at the origin is equivalent to the
Toeplitz inequalities
\[
 [g_{j-k}^{\rm SM}]_{1\le j,k\le N}\succeq0\qquad(N\ge1).         \tag{15}
\]
Test (15) against \(\mathbf1_n=(1,\ldots,1)^t\).  The exact
second-difference summation identity gives
\[
 \mathbf1_n^*[g_{j-k}^{\rm SM}]\mathbf1_n
 =2\lambda_n-\lambda_n^{\rm arch}.                               \tag{16}
\]
Therefore (EGSM) implies the strong margin
\[
 \lambda_n\ge\tfrac12\lambda_n^{\rm arch}\qquad(n\ge1).         \tag{17}
\]
The A0 tail inequality then gives the compact A1 inequality exactly as in
`164` and `198`.  Thus (EGSM) is a single explicit Euler--Gamma condition
which implies A1; it also implies Li positivity and hence RH.

This proves the algebraic implication chain conditional on (EGSM), while
`103_25` proves its premise false.  The unshifted weaker version (CP) is
already equivalent to RH by (7).  Full Loewner positivity therefore cannot
be the sought quantitative strengthening.

## 5. A Dirichlet-vector weakening still does not avoid RH

One might try to avoid the full Herglotz condition by asking only for the
Dirichlet-vector inequalities from `198`.  For the unshifted symbol, their
exact identity is
\[
 \mathbf1_n^*[g_{j-k}]_{1\le j,k\le n}\mathbf1_n=2\lambda_n.
\tag{19}
\]
Hence requiring these inequalities just for the special vectors
\(\mathbf1_n\), for every \(n\), is already
\[
 \lambda_n\ge0\qquad(n\ge1),                                    \tag{20}
\]
which is equivalent to RH by the Li criterion.  Requiring instead the
margin version gives (16), hence (17), and is stronger still.  A finite
collection of Dirichlet-vector inequalities can be a certificate for a
finite range, but it cannot prove the global statement.

Thus the weakening from all Toeplitz vectors to the \(D_n\) vectors removes
the *formal* equivalence with a Herglotz kernel, but it does not remove the
RH-strength of an all-\(n\) proof.  The exact remaining issue is whether the
Euler--Gamma expression (14) has a direct, non-circular lower bound on these
particular vectors; no such bound is established here.

## 6. Why a pre-log Schur factorisation does not add force by itself

There is a tempting factorisation before taking a logarithm:
\[
 H(z)={\xi(1/(1-z))\over\xi(1)},\qquad
 {H(z)\overline{H(w)}\over1-z\bar w}.                             \tag{21}
\]
The kernel in (21) is always positive semidefinite, for every holomorphic
\(H\): it is just the Szegő kernel multiplied by a scalar function.  It
therefore contains no zero-location information and cannot imply A1.

Replacing it by the Schur defect
\[
 {1-H(z)\overline{H(w)}\over1-z\bar w}                            \tag{22}
\]
would be nontrivial, but it is false: along real \(z\uparrow1\),
\(s=1/(1-z)\to+\infty\) and \(\xi(s)\to+\infty\), so \(H\) is not a
Schur function.  Thus a literal pre-log Schur factorisation cannot supply
the missing sign.  Passing to the completed logarithmic derivative exposes
the exact RH gate (CP), but its full Loewner-margin strengthening is ruled
out by `103_25`.

## Status

The full Euler--Gamma Loewner margin (EGSM) is eliminated by `103_25`.
Its identities and the conditional implication
\[
 (EGSM)\ \Longrightarrow\ A1\ \Longrightarrow\ \text{Li positivity}
\]
remain exact, but it is not a live target.  The surviving Toeplitz statement
is only the Dirichlet/Fejer scalar energy (16); it avoids the false boundary
sign while still requiring an RH-strength proof for all indices.
