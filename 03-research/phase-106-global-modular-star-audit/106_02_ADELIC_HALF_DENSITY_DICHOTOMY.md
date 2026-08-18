# 106.02 — The adelic half-density dichotomy

## Result

The natural infinite adelic star can be constructed exactly on the ambient
scaling space. What fails is its descent through the arithmetic summation
quotient.

For \(\delta\ge0\), let

\[
\mathcal H_\delta
=L^2\!\left(\mathbb R,w_\delta(t)dt\right),
\qquad
w_\delta(t)=(1+t^2)^{\delta/2}.
\]

The corrected half-density generator

\[
\Theta_{\mathrm{mod}}
=\frac12-\frac d{dt}-\frac{\delta t}{2(1+t^2)}
\tag{1}
\]

satisfies exactly

\[
\Theta_{\mathrm{mod}}^*=1-\Theta_{\mathrm{mod}}.
\tag{2}
\]

However:

* for \(\delta>0\), if both raw Euler scaling and the corrected modular flow
  preserve the adelic summation image, that image is the whole ambient space
  and the arithmetic quotient is zero;
* for \(\delta=0\), where no correction is needed, the adelic summation image
  is already dense by an explicit Wiener-cyclic vector, so the quotient is
  again zero;
* on the potentially nontrivial raw weighted quotient, the exact adjoint
  defect is

  \[
  B_\delta^*-(1-B_\delta)
  =P_\delta M_{\delta t/(1+t^2)}P_\delta.
  \tag{3}
  \]

Thus the desired global star does not descend for free. Equation (3) is the
precise remaining condition and supplies a direct falsifier.

## 1. Adelic summation and involution

Let \(\mathbb A=\mathbb A_\mathbb Q\),
\(C=\mathbb A^*/\mathbb Q^*\), \(C^1=\ker|\cdot|\), and
\(t=\log|x|\). Put

\[
\mathcal S_0(\mathbb A)
=\{\phi\in\mathcal S(\mathbb A):\phi(0)=\widehat\phi(0)=0\}.
\]

With self-dual additive Haar measure, define

\[
E\phi(x)=|x|^{1/2}\sum_{q\in\mathbb Q^*}\phi(qx),
\tag{4}
\]

and let \(E_0\phi\) be its average over the compact group \(C^1\). Define

\[
j_{\mathbb A}\phi=\overline{\widehat\phi},
\qquad
(Jf)(t)=\overline{f(-t)}.
\tag{5}
\]

Then

\[
j_{\mathbb A}^2=J^2=1,
\qquad
E_0j_{\mathbb A}=JE_0.
\tag{6}
\]

Indeed, complex conjugation \(\mathcal C\) and the adelic Fourier transform
\(\mathcal F\) satisfy
\(\mathcal C\mathcal F\mathcal C=\mathcal F^{-1}\), hence
\((\mathcal C\mathcal F)^2=1\). Adelic Poisson summation gives

\[
E(\widehat\phi)(x)
=E\phi(x^{-1})+|x|^{-1/2}\phi(0)-|x|^{1/2}\widehat\phi(0),
\tag{7}
\]

and the boundary terms vanish on \(\mathcal S_0\).

For an idele \(a_u\) with \(|a_u|=e^u\), put

\[
(\sigma_u\phi)(x)=e^{-u/2}\phi(a_u^{-1}x),
\qquad
(T_uf)(t)=f(t-u).
\tag{8}
\]

Unfolding (4) gives

\[
E_0\sigma_u=T_uE_0.
\tag{9}
\]

Consequently

\[
\mathcal M_\delta
=\overline{E_0\mathcal S_0(\mathbb A)}^{\,\mathcal H_\delta}
\tag{10}
\]

is invariant under every raw translation \(T_u\) and under \(J\).

## 2. Exact ambient adjoint

On \(C_c^\infty(\mathbb R)\), let

\[
\Theta_0=\frac12-\frac d{dt},
\qquad
b_\delta(t)=\frac{w_\delta'(t)}{w_\delta(t)}
=\frac{\delta t}{1+t^2}.
\tag{11}
\]

Weighted integration by parts gives, on the usual weighted \(H^1\) domains,

\[
\Theta_0^*=1-\Theta_0+M_{b_\delta},
\qquad
J\Theta_0J=1-\Theta_0.
\tag{12}
\]

Thus raw scaling has the explicit bounded defect \(M_{b_\delta}\). Subtracting
one half of the defect gives (1), and (12) immediately yields

\[
\Theta_{\mathrm{mod}}^*=1-\Theta_{\mathrm{mod}}
=J\Theta_{\mathrm{mod}}J.
\tag{13}
\]

The centered generator \(\Theta_{\mathrm{mod}}-1/2\) generates the unitary
group

\[
(U_uf)(t)=c_u(t)f(t-u),
\qquad
c_u(t)=\sqrt{\frac{w_\delta(t-u)}{w_\delta(t)}}.
\tag{14}
\]

## 3. Simultaneous invariance collapses the quotient

### Theorem 1

Assume \(\delta>0\). No nonzero proper closed subspace of
\(\mathcal H_\delta\) is invariant under every \(T_u\) and every \(U_u\).

### Proof

If \(\mathcal M\) is invariant under both groups, then it is invariant under

\[
U_uT_{-u}=M_{c_u}.
\tag{15}
\]

The multipliers are real and self-adjoint, so \(\mathcal M\) reduces them.
They separate points. To see this, suppose
\(c_u(t_1)=c_u(t_2)\) for every \(u\). With
\(F=\log w_\delta\) and \(d=t_2-t_1\), this implies

\[
F(s+d)-F(s)=F(t_2)-F(t_1)
\qquad(s\in\mathbb R).
\tag{16}
\]

Therefore \(F'(s+d)=F'(s)\). But

\[
F'(s)=\frac{\delta s}{1+s^2}\longrightarrow0
\qquad(s\to\pm\infty).
\]

A periodic function with this limit is identically zero, impossible for
\(\delta>0\) unless \(d=0\). By continuity the countable family
\(\{c_q:q\in\mathbb Q\}\) already separates points and generates the Borel
sigma algebra. Its von Neumann algebra is therefore the full multiplication
MASA \(L^\infty(\mathbb R)\).

A reducing subspace for this MASA has the form

\[
\mathcal M=L^2(S,w_\delta dt)
\]

for a measurable set \(S\). Invariance under every translation makes \(S\)
translation-invariant modulo null sets, hence null or conull. Therefore
\(\mathcal M=0\) or \(\mathcal H_\delta\). \(\square\)

Since \(\mathcal M_\delta\ne0\), invariance under the corrected modular group
would force \(\mathcal M_\delta=\mathcal H_\delta\), leaving a zero quotient.

## 4. The zero-weight case also collapses

For \(\delta=0\), take

\[
h(x)=x^2\left(x^2-\frac3{2\pi}\right)e^{-\pi x^2},
\qquad
\phi=h\otimes\bigotimes_p\mathbf 1_{\mathbb Z_p}.
\tag{17}
\]

Then \(\phi(0)=0\), and the Gaussian moments give

\[
\widehat\phi(0)=\int_\mathbb R h(x)dx=0,
\]

so \(\phi\in\mathcal S_0\). Its Tate transform is

\[
Z(\phi,s)
=\frac{s-1}{2}\pi^{-(s+4)/2}\Gamma\!\left(\frac{s+2}{2}\right)\zeta(s).
\tag{18}
\]

The \(\mathcal S_0\) Tate--Poisson theorem continues (18) entire. It is not
identically zero; no zero-free claim is needed. Hence its zeros on the central
vertical line are discrete and its boundary value is nonzero almost
everywhere. Unfolding gives

\[
\mathcal F_t(E_0\phi)(\tau)=Z(\phi,1/2-i\tau).
\tag{19}
\]

Wiener's \(L^2\) translation theorem says that the translates of
\(E_0\phi\) span \(L^2(\mathbb R)\). By (9), all these translates belong to
\(E_0\mathcal S_0\). Thus

\[
\mathcal M_0=\mathcal H_0.
\tag{20}
\]

At \(\delta=0\) the ambient adjoint is perfect, but the arithmetic quotient is
zero.

## 5. Exact defect on the raw quotient

Let \(P_\delta\) be the orthogonal projection onto

\[
\mathcal K_\delta=\mathcal M_\delta^\perp
\]

and let \(B_\delta\) be the compressed raw generator on a common smooth core.
Compressing (12) gives

\[
\boxed{
B_\delta^*-(1-B_\delta)
=P_\delta M_{b_\delta}P_\delta.
}
\tag{21}
\]

Therefore the desired quotient adjoint relation is exactly

\[
P_\delta M_{b_\delta}P_\delta=0,
\tag{22}
\]

equivalently \(b_\delta\mathcal K_\delta\subset\mathcal M_\delta\). A direct
falsifier is any pair \(u,v\) in the quotient core such that

\[
\delta\int_\mathbb R
\frac{t}{1+t^2}u(t)\overline{v(t)}
(1+t^2)^{\delta/2}dt\ne0.
\tag{23}
\]

## 6. Consequence

The ambient adelic construction evades the finite discriminant obstruction:
the star and corrected generator are exact. But it does not transport through
the Euler--Gamma cokernel:

\[
\begin{array}{c|c|c}
\text{choice}&\Theta^*=1-\Theta&\text{arithmetic quotient}\\ \hline
\delta=0&\text{yes}&0\\
\delta>0,\ \Theta_{\mathrm{mod}}&\text{yes}&0\text{ if it descends}\\
\delta>0,\ \Theta_0&\text{defect (21)}&\text{potentially nontrivial}
\end{array}
\]

The missing operation is not another ambient modular correction. It would
have to prove the arithmetic annihilation (22) without imposing corrected
invariance, or construct a different global quotient which retains Euler
covariance and avoids the MASA-collapse theorem.

## Status

Proved: the ambient star, the corrected adjoint, the simultaneous-invariance
collapse, the \(\delta=0\) Wiener collapse, and the exact quotient defect.

Refuted: descent of the natural corrected half-density flow to a nonzero
adelic summation quotient.

Open: a different global source quotient or a proof of (22) from literal
arithmetic data. No RH conclusion is claimed.
