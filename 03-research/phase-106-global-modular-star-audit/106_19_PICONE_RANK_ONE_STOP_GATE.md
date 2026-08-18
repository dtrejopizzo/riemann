# 106.19 — The Picone rank-one gate and a positive-jump countermodel

## Purpose

Document 106.17 reduces the even completed Weil form to

\[
 Q_L^+=\mathcal D_N-\kappa_N I+2|h_L\rangle\langle h_L|,
 \qquad h_L(x)=\mathbf 1_{I_L}(x)\cosh(x/2),
 \tag{1}
\]

where \(\mathcal D_N\) is a positive zero-extended jump form containing
the ordinary von Mangoldt atoms and the Gamma Levy measure.  This note
tests whether a nonlocal ground-state, Picone or Hardy representation can
prove the two remaining rank-one inequalities.

There are three exact conclusions.

1. The Picone identity exists, with all zero-extension boundary terms
   retained.
2. With the true ground state it is exactly the missing spectral-gap
   inequality, not a proof of that inequality.
3. Positivity of the jump measure, even with the same Gamma and polar
   channels, cannot imply the desired inertia: a one-atom positive jump
   model has arbitrarily many levels below the shifted threshold.

The ordinary-prime problem is therefore isolated in one signed
PNT-discrepancy form.  No statement below proves its required sign or RH.

## 1. The exact quadratic compensation identity

Put

\[
 \nu_\Gamma(du)=\frac{e^{-u/2}}{1-e^{-2u}}\,du,
 \qquad
 \nu_*(du)=\frac{e^{-5u/2}}{1-e^{-2u}}\,du,
 \tag{2}
\]

and, for a zero-extended \(f\in C_c^\infty(I_L)\), write

\[
 H_f(u)=\langle f,\tau_u f\rangle,
 \qquad F_f(u)=H_f(u)+H_f(-u).
 \tag{3}
\]

Define

\[
 \begin{aligned}
 \mathcal E_*(f)
 &:=\int_0^\infty\|f-\tau_u f\|_2^2\,\nu_*(du),\\
 \mathcal A_\Delta(f)
 &:=\int_{(0,L]}F_f(u)e^{-u/2}\,
 d\bigl(\psi(e^u)-e^u\bigr).
 \end{aligned}
 \tag{4}
\]

The first integral is finite on the logarithmic Gamma-form domain: near
zero its density is \(1/(2u)+O(1)\), while the translation difference
vanishes quadratically on the smooth core.

### Theorem 1 — Full quadratic prime--Gamma--pole compensation

Let

\[
 c_*:=\gamma+\frac\pi2+3\log2+\log\pi-4>0.
 \tag{5}
\]

Then the complete semilocal Weil quadratic form satisfies

\[
 \boxed{
 QW_L(f,f)=\mathcal E_*(f)-c_*\|f\|_2^2-\mathcal A_\Delta(f).}
 \tag{6}
\]

#### Proof

Let

\[
 \nu_p(du)=e^{-u/2}\,d\psi(e^u),
 \qquad
 \nu_0(du)=e^{u/2}\,du,
 \qquad
 \nu_\Delta=\nu_p-\nu_0.
 \tag{7}
\]

Expanding the prime jump form in 106.17 and subtracting its scalar part
gives \(-\int F_f\,d\nu_p\).  The two polar branches give

\[
 \int_0^L F_f(u)(e^{u/2}+e^{-u/2})\,du.
 \tag{8}
\]

The \(e^{u/2}\) branch cancels \(\nu_0\), leaving

\[
 \int_0^L F_f(u)e^{-u/2}\,du-\mathcal A_\Delta(f).
 \tag{9}
\]

If \(\nu_e(du)=e^{-u/2}du\), then

\[
 \int_0^L F_f(u)e^{-u/2}\,du
 =4\|f\|_2^2-\mathcal D_{\nu_e}(f),
 \tag{10}
\]

because \(\nu_e(0,\infty)=2\).  Moreover

\[
 \nu_\Gamma-\nu_e=\nu_*.
 \tag{11}
\]

The Gamma diagonal constant is \(2\theta'(0)\), and

\[
 2\theta'(0)
 =-\gamma-\frac\pi2-3\log2-\log\pi.
 \tag{12}
\]

Consequently

\[
 \mathcal D_{\nu_\Gamma}-\mathcal D_{\nu_e}
 +(4+2\theta'(0))I
 =\mathcal D_{\nu_*}-c_*I,
 \tag{13}
\]

which proves (6). \(\square\)

For a cross term \(f\perp g\), polarization of (6) is exactly the
identity of 106.18: the jump diagonal and the scalar vanish, leaving the
kernel \(-e^{-5u/2}/(1-e^{-2u})\) and the signed discrepancy measure.

Thus qualitative positivity of the completed form is exactly

\[
 \boxed{
 \mathcal A_\Delta(f)
 \le \mathcal E_*(f)-c_*\|f\|_2^2
 \quad\text{for every test }f.}
 \tag{14}
\]

Equation (14) is not proved.  It is the ordinary-prime signed inequality
left after the continuous PNT main term, Gamma and both polar branches have
all been cancelled algebraically.

## 2. Exact nonlocal Picone identity

Write the complete positive jump measure of 106.17 as

\[
 \nu_N
 =\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}
  +\nu_\Gamma.
 \tag{15}
\]

Let \(v>0\) on \(I_L\), extend \(v\) by zero, and put \(r=f/v\) on
\(I_L\).  Assume first that \(f,v\) lie on a common smooth form core.

### Theorem 2 — Zero-extension Picone formula

One has

\[
 \boxed{
 \begin{aligned}
 \mathcal D_N(f,f)
 &=\int_{(0,\infty)}\!\int_{\mathbb R}
 v(x)v(x-u)|r(x)-r(x-u)|^2\,dx\,\nu_N(du)\\
 &\quad+\int_{I_L}\frac{(\mathcal D_Nv)(x)}{v(x)}|f(x)|^2\,dx.
 \end{aligned}}
 \tag{16}
\]

#### Proof

For each fixed shift, the pointwise algebraic identity is

\[
 |v_xr_x-v_yr_y|^2
 =v_xv_y|r_x-r_y|^2
 +(v_x-v_y)(v_x|r_x|^2-v_y|r_y|^2).
 \tag{17}
\]

Set \(y=x-u\), integrate in \(x\), and change variables in the second
half of the last term.  It becomes

\[
 \int_{I_L}
 \frac{2v(x)-v(x-u)-v(x+u)}{v(x)}|f(x)|^2\,dx.
 \tag{18}
\]

Integration against \(\nu_N\) proves (16).  Values outside \(I_L\) are
zero; hence (18) includes, rather than discards, the killing/boundary
terms. \(\square\)

If \(\varphi_1>0\) is the normalized ground state of \(\mathcal D_N\),
with eigenvalue \(\mu_1\), then (16) becomes

\[
 \mathcal D_N(f,f)-\mu_1\|f\|_2^2
 =\int\!\int
 \varphi_1(x)\varphi_1(x-u)
 \left|\frac{f(x)}{\varphi_1(x)}
 -\frac{f(x-u)}{\varphi_1(x-u)}\right|^2dx\,\nu_N(du).
 \tag{19}
\]

Therefore the first rank-one inertia requirement

\[
 \lambda_2(\mathcal D_N)\ge\kappa_N
 \tag{20}
\]

is exactly the transformed Poincare inequality

\[
 \boxed{
 \int\!\int\varphi_1(x)\varphi_1(x-u)|r(x)-r(x-u)|^2
 \,dx\,\nu_N(du)
 \ge(\kappa_N-\mu_1)\int\varphi_1^2|r|^2,}
 \tag{21}
\]

for \(\int\varphi_1^2r=0\).  Thus the Picone transform is exact, but its
required Poincare constant is precisely the unproved second-level bound.
Taking \(v=h_L\) instead leaves the sign-indefinite local potential

\[
 \frac{\mathcal D_Nh_L}{h_L}-\kappa_N
 \tag{22}
\]

in (16); the positive rank-one term in (1) does not cancel this
pointwise potential.

## 3. Constrained form of the resolvent sign

Put \(B_N=\mathcal D_N-\kappa_NI\).  Assume \(B_N\) is invertible, has
one negative eigenvalue, and is nonnegative on \(h_L^\perp\).  Set

\[
 r_N=\langle h_L,B_N^{-1}h_L\rangle<0.
 \tag{23}
\]

Completing the square in the \(B_N\)-metric gives

\[
 \boxed{
 \inf_{\langle h_L,f\rangle=1}B_N(f,f)=\frac1{r_N}.}
 \tag{24}
\]

Hence

\[
 1+2r_N\le0
 \quad\Longleftrightarrow\quad
 \inf_{\langle h_L,f\rangle=1}B_N(f,f)\ge-2.
 \tag{25}
\]

Together with \(B_N\ge0\) on \(h_L^\perp\), (25) is simply

\[
 B_N(f,f)+2|\langle h_L,f\rangle|^2\ge0
 \quad(f\in\mathcal D(B_N)),
 \tag{26}
\]

namely the original completed even Weil inequality.  The resolvent
coordinate is exact but contains no automatic Hardy slack.

## 4. A positive one-atom countermodel

The following falsifier shows that (20) cannot be obtained from positivity
of the Levy measure, zero extension and the polar rank-one term alone.

Fix \(a>0\) and an integer \(M\ge6\).  Choose a smooth bump \(\phi_1\)
with support of width less than \(a/3\), and let

\[
 \phi_j=\tau_{(j-1)a}\phi_1,
 \qquad 1\le j\le M,
 \tag{27}
\]

inside a sufficiently long interval.  Normalize the bumps; they are
orthonormal.  Add to the fixed Gamma jump measure a positive atom
\(w\delta_a\), and shift by the corresponding scalar \(2w\), exactly as
in (7) of 106.17.

On \(V_M=\mathrm{span}\,\{\phi_1,\ldots,\phi_M\}\), the atomic
part after the scalar shift is

\[
 -wA_M,
 \tag{28}
\]

where \(A_M\) is the adjacency matrix of the path on \(M\) vertices.  Its
eigenvalues are

\[
 -2w\cos\frac{k\pi}{M+1},
 \qquad 1\le k\le M.
 \tag{29}
\]

The compression of the fixed Gamma form, its fixed scalar, and
\(2|h_L\rangle\langle h_L|\) to \(V_M\) has a finite norm \(C_M\),
independent of \(w\).  Weyl's inequality and (29) imply that, for all
sufficiently large \(w\), the completed compressed form has at least
\(\lfloor M/2\rfloor\) negative eigenvalues.  In particular, for
\(M\ge6\) it has at least three.

All jump weights in this model are nonnegative.  Thus no proof using only
nonnegativity of the Levy measure, generic Picone algebra, or a generic
rank-one pole perturbation can establish (20) or (26).  Such a proof must
use the locations and exact magnitudes of the ordinary coefficients
\(\Lambda(n)/\sqrt n\); in the fully compensated coordinate, this means
proving the signed discrepancy inequality (14).

## 5. Verdict

The ground-state/Picone attack does not close the rank-one gate.  It gives
the exact transformed Poincare target (21), while the resolvent condition
is exactly the constrained Hardy target (25).  A positive one-atom Levy
model violates the desired inertia with arbitrarily large negative index,
so positivity and boundary killing are insufficient.

The narrow remaining theorem is (14), quantitatively strengthened to the
moving-vector residual and \(d_8\) complement scale of Gate SPG.  It is a
signed estimate for the literal ordinary-prime discrepancy; it is not
proved here.
