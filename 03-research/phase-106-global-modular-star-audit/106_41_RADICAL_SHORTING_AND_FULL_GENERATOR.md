# 106.41 — Radical shorting and the full ordinary-prime generator

## Purpose

The complementary contraction in 106.39 contains an abstract projection in
the source edge space. This note removes that abstraction. Radical shorting
is exactly orthogonal projection in the multiplier space, and the surviving
inequality is the spectral floor of one explicit reversible jump generator.
The formula keeps every ordinary von Mangoldt atom and the complete Gamma
measure. No zero-location statement is used.

## 1. Multiplier realization of radical shorting

Let

\[
r_j=K^{(2j)}/K\qquad(j\geq0)
\]

and let \(\mathcal R\) be the closed span in \(L^2(\mu_K)\) of the centered
functions \(r_j-\mu_K(r_j)\), \(j\geq1\). Denote its orthogonal projection
by \(P_{\mathcal R}\). Constants are factored out.

### Theorem 1 — Exact shorting formula

For every multiplier in the common form core,

\[
\boxed{
UP_{\mathscr M}\mathcal Gr=D_\mu P_{\mathcal R}r,
\qquad
P_{\mathscr M^\perp}\mathcal Gr
=\mathcal G(I-P_{\mathcal R})r.}
\tag{1}
\]

Consequently, with \(q=(I-P_{\mathcal R})r\), the complementary contraction
is exactly

\[
\boxed{\|D_\mu q\|\leq\|\mathcal Gq\|,
\qquad q\perp(1\oplus\mathcal R).}
\tag{2}
\]

#### Proof

Polarization of the full-kernel identity gives

\[
\langle\mathcal Gr,\mathcal Gr_j\rangle
=\langle D_\mu r,D_\mu r_j\rangle                    \tag{3}
\]

because \(Kr_j=K^{(2j)}\) belongs to the Weil radical. The difference
gradient is a scaled isometry on centered multipliers:

\[
\langle D_\mu r,D_\mu s\rangle
=\frac12\langle r-\mu_K(r),s-\mu_K(s)\rangle_{L^2(\mu_K)}. \tag{4}
\]

Equations (3)--(4) show that the orthogonal projection of \(\mathcal Gr\)
onto \(\mathscr M\) is \(\mathcal GP_{\mathcal R}r\). Applying the radical
isometry \(U\) gives the first identity in (1), and subtracting gives the
second. Substitution in 106.39(20) proves (2). \(\square\)

The orthogonality condition in (2) is the infinite family

\[
\boxed{
\int_{\mathbb R}q(x)h(x)K^{(2j)}(x)\,dx=0
\qquad(j\geq0).}                                      \tag{5}
\]

Thus the complementary problem is a Poincare estimate after all exact
Riemann-radical directions have been removed.

## 2. The full reversible generator

Write

\[
a_n=\frac{\Lambda(n)}{\sqrt n},\qquad
g(u)=\frac{e^{-u/2}}{1-e^{-2u}},\qquad c_K=\frac12.    \tag{6}
\]

The closed form \(\mathscr E_K\) defines a nonnegative self-adjoint
generator \(L\) in \(L^2(\mu_K)\). On a smooth core it is

\[
\begin{aligned}
(Lr)(x)=\frac{c_K}{h(x)}\Bigg[&
\int_0^\infty g(u)\big\{K(x-u)(r(x)-r(x-u))\\
&\hspace{31mm}+K(x+u)(r(x)-r(x+u))\big\}\,du\\
&+\sum_{n\ge2}a_n\big\{K(x-\log n)(r(x)-r(x-\log n))\\
&\hspace{31mm}+K(x+\log n)(r(x)-r(x+\log n))\big\}
\Bigg].                                                \tag{7}
\end{aligned}
\]

The Gamma integral is understood in difference form. Direct symmetrization
against \(d\mu_K=hK\,dx/c_K\) gives

\[
\boxed{\langle r,Ls\rangle_{\mu_K}
=\langle\mathcal Gr,\mathcal Gs\rangle_{\mathscr H_{\rm src}}.} \tag{8}
\]

In particular, \(L1=0\) and \(\langle r,Lr\rangle=\mathscr E_K(r)\).

## 3. Exact quotient spectral target

For centered \(q\), \(\|D_\mu q\|^2=\frac12\|q\|^2_{\mu_K}\). Therefore
(2) becomes

\[
\boxed{
\langle q,Lq\rangle_{\mu_K}\geq\frac12\|q\|^2_{\mu_K}
\qquad(q\perp1\oplus\mathcal R).}                    \tag{9}
\]

Moreover, (3) for arbitrary tests implies the weak operator identity

\[
Lr_j=\frac12\bigl(r_j-\mu_K(r_j)\bigr).               \tag{10}
\]

Thus \(\mathcal R\) is an exact threshold eigenspace. The contraction
problem is the exclusion of spectrum below \(1/2\) after the constant state
and the threshold radical have been shorted out.

## 4. Integrated curvature identity

Since \(L\geq0\), the quotient floor (9) is equivalent to

\[
\boxed{
\|Lq\|^2_{\mu_K}-\frac12\langle q,Lq\rangle_{\mu_K}
\geq0\qquad(q\perp1\oplus\mathcal R).}                \tag{11}
\]

Indeed, the spectral multiplier is \(\lambda(\lambda-1/2)\); after the zero
mode is removed, (11) excludes exactly \((0,1/2)\). Formula (11) is the
integrated \(\Gamma_2\) form of the desired estimate. Its prime--prime
coefficient algebra contains the two nonnegative ordinary arithmetic jets

\[
\delta\Lambda(n)=\Lambda(n)\log n,
\qquad (\Lambda*\Lambda)(n),                           \tag{12}
\]

whose sum is

\[
j_2(n)=\delta\Lambda(n)+(\Lambda*\Lambda)(n)
=(\mu*\log^2)(n)\geq0.                                \tag{13}
\]

Equation (13) is the coefficient Riccati curvature realized spatially in
106.40. A closing factorization of (11), however, must be performed after
the intermediate theta position and the Gamma--polar cross terms are
retained. The unrestricted divisor-index lift is false by
106.40(15)--(16).

## 5. Search gate

The Phase-77 commutator no-go does not apply to (7): that document used a
rank-two finite displacement commutator, whereas (7) has a continuous Gamma
channel and every literal prime-power displacement. Conversely, Phase 101
rules out declaring a finite commutator itself positive. A successful virial
calculation must therefore produce (11) as squared full spatial currents
plus a vanishing boundary term; it cannot identify the commutator alone with
a positive matrix.

The remaining calculation is the joint spatial lift of (13) on the
constrained subspace (5). No term may be estimated before Gamma, polar,
divisible-theta, fractional-theta and central channels have been combined.
