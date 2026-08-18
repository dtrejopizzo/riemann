# 106.121 — Gamma coercivity after complete radical anti-shorting

## Purpose and verdict

The Gamma small-jump channel controls one logarithmic Fourier moment.  A
natural successor is to ask whether that coercivity survives projection
off the complete Riemann radical strongly enough to force the physical
floor \(1/2\) on heat and hybrid rows.

There is a precise answer.

1.  The logarithmic **upper** control survives the complete projection
    without loss: the projected row has local high-frequency mass bounded
    by the complete prime--Gamma form of the input.
2.  No positive lower-frame transfer from an input row to its projected
    row is possible.  Every nonzero exact radical vector is a threshold
    heat eigenvector, retains nonzero Fourier mass above every finite
    frequency after localization, and is annihilated by the projection.
3.  Restricting the claim to rows already in the complement removes that
    counterexample, but then the desired estimate is exactly the
    Gamma-only maximal anti-short of 106.68.  Its Picone potential is not
    Fourier diagonal, and a high-frequency support statement for the
    mean-periodic carrier does not control it.

Thus Gamma coercivity survives anti-shorting only in the compactness
direction.  It cannot supply the missing lower floor.  The obstruction is
exact and remains present on heat-regularized radical/hybrid families; it
is not a numerical failure of a chosen frame.

## 1. Semantic audit

The following prior routes were checked.

* Phase 15 and `106_18` prove positivity/logarithmic growth of the
  translation-invariant archimedean multiplier outside a compact band.
* `106_20` finds that the extremal compensated rows are low-frequency,
  boundary-concentrated and near-radical; increasing the Fourier cutoff
  does not move the bottleneck to the ultraviolet edge.
* `106_24` computes the prolate endpoint and \(H^1\)-leakage scales.  It
  does not transfer them to the complete signed source.
* `106_30` proves that ordinary cyclic approximation by a growing radical
  frame has the wrong radius-dependent conditioning at an off-line
  evaluation.
* `106_62` derives the exact zero-mode Gamma Gram and gives the four-mode
  Gamma-only diagnostic.
* `106_68` derives the maximal anti-short and the nonconstant Gamma Picone
  potential.
* `106_70` separates compact-open zero-mode synthesis from weighted form
  synthesis; translations are unbounded in the physical weighted space.
* `106_71` shows that a cofinal prime filter bank controls the omitted tail
  but does not produce the lower frame bound.
* `106_116` and `106_118` quantify the logarithmic Gamma scale and the
  \(N/\log N\) loss of absolute Abel quadrature.
* `106_120` proves fixed-gap finite reduction but also proves that the
  logarithmic moment gives no uniform form-tail compactness as the gap
  tends to zero.

The result below is not another Paley--Wiener or prolate estimate.  It
identifies exactly what the complete radical projection preserves and
constructs an exact heat-invariant obstruction to every lower-frame
version.

## 2. Setup

Let

\[
 \mathscr H=L^2_{\rm even}(\mu_K),\qquad
 \mathscr C=(\mathbf1\oplus\mathcal R)^\perp,
 \qquad P_{\mathscr C}:\mathscr H\to\mathscr C,     \tag{1}
\]

where \(\mathcal R\) is the closed span of the centered exact radical
vectors

\[
 r_j^\circ={K^{(2j)}\over K}-\mu_K\!\left({K^{(2j)}\over K}\right),
 \qquad j\ge1.                                      \tag{2}
\]

Let \(L\ge0\) be the complete ordinary-prime--Gamma generator.  The strong
radical identity is

\[
 Lr_j^\circ={1\over2}r_j^\circ.                    \tag{3}
\]

Consequently \(\mathbf1\oplus\mathcal R\) and \(\mathscr C\) reduce
\(L\), and

\[
 P_{\mathscr C}e^{-tL}=e^{-tL}P_{\mathscr C}.      \tag{4}
\]

Write \(\mathscr E_K\) and \(\mathscr E_\Gamma\) for the complete and
Gamma forms.  Since every ordinary-prime channel is positive,

\[
 0\le\mathscr E_\Gamma(q)\le\mathscr E_K(q).       \tag{5}
\]

For \(\chi\in C_c^\infty(\mathbb R)\) define the local logarithmic
seminorm

\[
 \mathcal H_\chi(q)
 :=\int_{\mathbb R}\log(2+|\xi|)
       |\widehat{\chi q}(\xi)|^2\,d\xi.            \tag{6}
\]

The local Gamma theorem of 106.47 says

\[
 \mathcal H_\chi(q)
 \le C_\chi\{\mathscr E_\Gamma(q)+\|q\|^2\}.      \tag{7}
\]

## 3. The maximal projection-stable theorem

### Theorem 1 — Complete projection preserves logarithmic compactness

For every \(f\in D(\mathscr E_K)\),

\[
\boxed{
 \mathcal H_\chi(P_{\mathscr C}f)
 \le C_\chi\{\mathscr E_K(f)+\|f\|^2\}.}           \tag{8}
\]

More generally, for every \(t\ge0\),

\[
\boxed{
 \mathcal H_\chi(P_{\mathscr C}e^{-tL}f)
 \le C_\chi\{\mathscr E_K(e^{-tL}f)
                    +\|e^{-tL}f\|^2\}.}           \tag{9}
\]

#### Proof

Because \(P_{\mathscr C}\) is a reducing spectral projection of \(L\),

\[
 \mathscr E_K(P_{\mathscr C}f)\le\mathscr E_K(f),
 \qquad \|P_{\mathscr C}f\|\le\|f\|.              \tag{10}
\]

Apply (7) to \(P_{\mathscr C}f\), use (5) and then (10).  Equation (9)
follows in the same way, using (4).  \(\square\)

This is a genuine stability statement.  It is also the strongest statement
of this type which follows from logarithmic Gamma coercivity: it bounds the
high-frequency mass of the **output** from above.  It supplies local
compactness, not a lower spectral floor.

## 4. Exact failure of every lower-frame transfer

For \(\Omega>0\), put

\[
 \mathcal H_{\chi,\Omega}(q)
 :=\int_{|\xi|>\Omega}\log(2+|\xi|)
       |\widehat{\chi q}(\xi)|^2\,d\xi.            \tag{11}
\]

### Theorem 2 — Heat-invariant radical annihilation

Choose a nonzero \(r\in\mathcal R\cap D(L)\), for example one of the
vectors (2), and choose \(\chi\) so that \(\chi r\not\equiv0\).  Then, for
every finite \(\Omega\) and every \(t\ge0\),

\[
\boxed{
 \mathcal H_{\chi,\Omega}(e^{-tL}r)>0,
 \qquad
 \mathcal H_{\chi,\Omega}
   (P_{\mathscr C}e^{-tL}r)=0.}                    \tag{12}
\]

Consequently there is no \(c>0\) for which

\[
 \mathcal H_{\chi,\Omega}(P_{\mathscr C}e^{-tL}f)
 \ge c\,\mathcal H_{\chi,\Omega}(e^{-tL}f)        \tag{13}
\]

holds on any heat/hybrid class containing the exact radical rows.

#### Proof

Equations (3)--(4) give

\[
 e^{-tL}r=e^{-t/2}r,
 \qquad P_{\mathscr C}e^{-tL}r=0.                 \tag{14}
\]

The compactly supported smooth function \(\chi r\) is nonzero.  Its
Fourier transform is entire.  If the first quantity in (12) vanished,
that entire function would vanish almost everywhere on the open rays
\((\Omega,\infty)\) and \(( -\infty,-\Omega)\), hence identically by the
identity theorem.  Fourier injectivity would give \(\chi r=0\), a
contradiction.  Multiplication by \(e^{-t/2}\) does not change this
conclusion.  \(\square\)

The obstruction is stronger than poor frame conditioning.  The lower
frame constant is exactly zero before any limit is taken.  Heat
regularization does not repair it because the complete radical is an exact
threshold eigenspace.

## 5. Why restricting to the post-short complement does not close the gap

One may exclude the inputs used in Theorem 2 and ask only about
\(q\in\mathscr C\).  Then \(P_{\mathscr C}q=q\), so (8) reduces to the
already known local Gamma estimate.  A lower estimate sufficient for the
physical threshold would have to prove, directly or after a uniform
uncertainty step,

\[
 \mathscr E_\Gamma(q)\ge{1\over2}\|q\|^2,
 \qquad q\in\mathscr C.                            \tag{15}
\]

This is not a consequence of the zero-frequency gap.  If

\[
 \chi_z(x)={\cos(zx)\over\cosh(x/2)},
 \qquad \Xi(z)=0,                                  \tag{16}
\]

then \(\chi_z\in\mathscr C\), but the physical Gamma test is

\[
 K\chi_z={K\over h}\cos(zx).                       \tag{17}
\]

Its Fourier transform is the convolutional spread

\[
 \widehat{K\chi_z}(\xi)
 ={1\over2}\{\Phi(\xi-z)+\Phi(\xi+z)\},
 \qquad \Phi=\widehat{K/h},                        \tag{18}
\]

not a point mass at \(\pm z\).  The Gamma Doob form also has the exact
Picone representation

\[
 \mathscr E_\Gamma(q)-{1\over2}\|q\|^2
 =\mathcal D_\Gamma(Kq)
 -\int_{\mathbb R}V_\Gamma(x)|K(x)q(x)|^2\,dx,    \tag{19}
\]

with the nonconstant potential

\[
 V_\Gamma(x)={D_\Gamma K(x)+h(x)\over K(x)}.       \tag{20}
\]

Thus the logarithmic multiplier controls only the first term of (19).
The radical/Doob potential is of the same order and cannot be discarded.
Indeed, for the exact radical tests

\[
 f_j=K^{(2j)}-4^{-j}K,                              \tag{21}
\]

the translation-invariant archimedean multiplier is positive for all
sufficiently large \(j\), whereas the exact completed radical identity
gives

\[
 \mathscr E_\Gamma(r_j^\circ)-{1\over2}\|r_j^\circ\|^2
 =-\mathscr E_p(r_j^\circ)<0.                      \tag{22}
\]

Equation (22) is an exact sign reversal between high-frequency multiplier
positivity and the physical Gamma Doob form.

On the actual complement, 106.62 supplies the exact four-zero vector

\[
 q_4={\cos(\gamma_1x)-2\cos(\gamma_2x)
             +2\cos(\gamma_3x)-\cos(\gamma_4x)\over h(x)}
 \in\mathscr C,                                    \tag{23}
\]

for which the Gamma quotient is numerically stable at

\[
 {\mathscr E_\Gamma(q_4)\over\|q_4\|^2}
 =0.488953\ldots<\frac12.                          \tag{24}
\]

Membership in \(\mathscr C\) is exact; (24) remains a diagnostic until
its quadrature and theta tails are enclosed by outward intervals.  It is
included only as a check of the exact mechanism (18)--(22), not as a
proved counterexample.

## 6. The anti-short identity identifies the missing term

Let

\[
 A_\Gamma(q)=\mathscr E_\Gamma(q)-{1\over2}\|q\|^2
\]

and maximize over the complete radical:

\[
 B_\Gamma(q)=\sup_{r\in\mathcal R}A_\Gamma(q+r),
 \qquad q\in\mathscr C.                            \tag{25}
\]

The tail-distance theorem of 106.68 gives the exact formula

\[
\boxed{
 B_\Gamma(q)=A_Q(q)-(\mathscr E_p)_{/\mathcal R}(q),}          \tag{26}
\]

where \(A_Q\) is the complete physical defect on the quotient and the
second term is the short of the complete positive prime tail over the
radical.  Therefore

\[
 B_\Gamma\ge0\quad\Longrightarrow\quad A_Q\ge0.    \tag{27}
\]

The high-frequency Gamma estimate does not control the tail distance in
(26).  Proving that it does, uniformly on the heat core, would already be
a complete physical-floor theorem rather than an uncertainty corollary.

## 7. Final gate

What survives complete radical anti-shorting is exactly

\[
 \boxed{
 \mathcal H_\chi(P_{\mathscr C}f)
 \lesssim_\chi \mathscr E_K(f)+\|f\|^2,}           \tag{28}
\]

which is sufficient for compactness and the essential threshold.  What
does not survive is any positive lower-frame comparison with the input,
even after heat regularization, by Theorem 2.

On rows already in \(\mathscr C\), the missing estimate is not an
uncertainty theorem.  It is the signed prime-tail distance inequality in
(26), equivalently the complete physical surplus.  Gamma logarithmic
coercivity therefore removes ultraviolet escape but cannot exclude the
localized subthreshold bound state.
