# 104_38 — Canonical Selberg square cancellation and the Schur-square gate

**Status.** An attempt was made to close the adjacent determinant

\[
 \mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2
 \tag{1}
\]

using the exact Selberg identity for the canonical weights
\(\log p\), keeping the linear term, the quadratic term, the archimedean
block, and the higher prime powers together. The result is an algebraic
stop-gate narrower than the Hankel minor of `104_37`:

1. the single square \(\mu*\mu\) produced by Selberg cancels
   **identically** against the square introduced by the inversion;
2. if, instead of canceling it, one tries to use that square to pay for
   the Schur term of (1), the residual kernel has a negative diagonal in
   the tail for every \(n\ge2\);
3. the diagonal witness can be placed at \(R=\log p\), with the
   canonical weight \(\log p\), for an arbitrarily large real prime.

This rules out a completing-the-square approach based on the first
Selberg identity, even after exactly incorporating the optimal taper. It
does not refute \(\mathcal T_n\ge0\) for the complete arithmetic measure: a
proof could still use a special signed cancellation between the linear and
quadratic terms **at the total canonical value**, but it can no longer
obtain it by declaring the quadratic remainder positive. Neither A1 nor RH
is proved.

## 1. Regulated form with all blocks kept

Fix \(a>1\). We use the notation of `104_35`:

\[
 d\alpha=\sum_p\log p\,\delta_{\log p},\qquad
 d\beta=e^u\,du,\qquad d\mu=d\alpha-d\beta,
 \tag{2}
\]

\[
 w_{n,a}(u)=ae^{-au}L_{n-1}^{(1)}(au),\qquad
 P_{n,a}=\langle w_{n,a},\beta-\alpha\rangle
        =-\langle w_{n,a},\mu\rangle .
 \tag{3}
\]

Let the convergent contribution of the higher powers, with the same
regularization, be

\[
 C_{n,a}:=a\sum_p\sum_{k\ge2}{\log p\over p^{ka}}
              L_{n-1}^{(1)}(ka\log p).
\]

Then

\[
 B_{n,a}=C_{n,a}-P_{n,a},\qquad
 H_{n,a}=\kappa A_n-C_{n,a}+P_{n,a},
 \quad \kappa={1501\over2002}.
 \tag{4}
\]

Set

\[
 d_{n,a}=\kappa\Delta A_n-B_{1,a},\qquad
 x_{n,a}=\Delta B_{n,a}-B_{1,a}.
 \tag{5}
\]

As \(a\downarrow1\),

\[
 d_{n,a}\longrightarrow d_n=\kappa\Delta A_n+\gamma>0,
 \qquad
 x_{n,a}\longrightarrow H_n+d_n-H_{n+1}.
 \tag{6}
\]

The exact polarization of `104_34` holds before the limit:

\[
 \mathsf M_a[g_n+t\phi_n]
 =H_{n,a}-t x_{n,a}+t^2d_{n,a}.
 \tag{7}
\]

In particular, for \(a>1\) sufficiently close to one,
\(d_{n,a}>0\) and

\[
 \min_t\mathsf M_a[g_n+t\phi_n]
 =H_{n,a}-{x_{n,a}^2\over4d_{n,a}}.
 \tag{8}
\]

No higher power has been omitted: everything is in \(C_{n,a}\). Nor was
the pole separated: it is coupled to \(P_{n,a}\) via
\(\beta-\alpha\).

## 2. The cross-entry functional

The Laguerre identity

\[
 L_n^{(1)}-L_{n-1}^{(1)}=L_n
 \tag{9}
\]

gives

\[
 \ell_{n,a}(u)
 :=w_{n+1,a}(u)-w_{n,a}(u)-w_{1,a}(u)
 =ae^{-au}\{L_n(au)-1\}.
 \tag{10}
\]

If

\[
 c_{n,a}:=\Delta C_{n,a}-C_{1,a},
 \tag{11}
\]

then (3)–(5) produce, with no estimate,

\[
 \boxed{x_{n,a}=c_{n,a}+\langle\ell_{n,a},\mu\rangle.}
 \tag{12}
\]

So the square that (8) must pay for is a square of a linear functional of
the real centered measure, together with the ordinarily convergent
boundary term of the higher powers.

## 3. Exact cancellation of the Selberg square

Define

\[
 d\mathcal B_p=u\,d\mu+2\beta*\mu+\mu*\mu,
 \tag{13}
\]

and let \(G_{n,a}\) be the decreasing solution of

\[
 (\mathcal TG)(v)
 :=vG(v)+2\int_0^\infty G(v+u)\,d\beta(u)
 =w_{n,a}(v).
 \tag{14}
\]

Identity (23) of `104_35` is

\[
 P_{n,a}=-\langle G_{n,a},\mathcal B_p\rangle
          +\mathcal Q_{G_{n,a}}(\mu),
 \qquad
 \mathcal Q_G(\mu)=\iint G(u+v)\,d\mu(u)d\mu(v).
 \tag{15}
\]

No hidden positive square remains here. Indeed, inserting
(13), Fubini gives the form identity

\[
\begin{aligned}
 -\langle G,\mathcal B_p\rangle+\mathcal Q_G(\mu)
 &=-\langle uG,\mu\rangle
   -2\langle G,\beta*\mu\rangle\\
 &=-\langle\mathcal TG,\mu\rangle.
\end{aligned}
 \tag{16}
\]

The summand \(-\langle G,\mu*\mu\rangle\) of the first line cancels
coefficient by coefficient against
\(+\mathcal Q_G(\mu)\). For \(\mathcal TG=w_{n,a}\), (16) returns exactly
to (3). The cancellation uses the real weights of (2), not an envelope or
a competing measure.

Hence there are only two accountable options:

* expand (13), in which case the Selberg square disappears and (8)
  returns to the original linear functional minus the Schur square;
* keep \(\mathcal Q_G\), in which case one must study the residual
  quadratic kernel of the next section.

## 4. The residual kernel has a negative diagonal

Inserting (12) and (15) into (8), with no block separated, we obtain

\[
\begin{aligned}
 \min_t\mathsf M_a[g_n+t\phi_n]
={}&\kappa A_n-C_{n,a}
 -\langle G_{n,a},\mathcal B_p\rangle
 +\mathcal Q_{G_{n,a}}(\mu)\\
 &-{\{c_{n,a}+\langle\ell_{n,a},\mu\rangle\}^2
       \over4d_{n,a}}.
\end{aligned}
 \tag{17}
\]

The two quadratic terms a completion-of-squares argument would try to
compare, \(\mathcal Q_{G_{n,a}}(\mu)\) and the square of the cross entry,
have as their difference the kernel

\[
 \boxed{
 K_{n,a}(u,v)=G_{n,a}(u+v)
 -{\ell_{n,a}(u)\ell_{n,a}(v)\over4d_{n,a}}.}
 \tag{18}
\]

This is not the total quadratic part of (17): expanding
\(-\langle G,\mathcal B_p\rangle\), its term
\(-\langle G,\mu*\mu\rangle\) cancels \(\mathcal Q_G\), as (16) proves.
Precisely because of that, keeping \(\mathcal Q_G\) as a supposed reserve
requires difference (18) to have a sign, while the remaining term is
controlled without using the same square again. That difference is not
positive semidefinite. For \(n\ge2\), (10) gives

\[
 \ell_{n,a}(R)
 ={(-1)^na^{n+1}\over n!}e^{-aR}R^n
   \{1+O_{n,a}(R^{-1})\}.                                  \tag{19}
\]

By Lemma 5.1 of `104_37`, applied to the untapered test,

\[
 G_{n,a}(2R)
 ={(-1)^{n-1}a^n\over(n-1)!}
 e^{-2aR}(2R)^{n-2}\{1+O_{n,a}(R^{-1})\}.                  \tag{20}
\]

Since \(2n>n-2\), (18)–(20) imply

\[
 \boxed{
 K_{n,a}(R,R)
 =-{a^{2n+2}\over4d_{n,a}(n!)^2}
   e^{-2aR}R^{2n}\{1+O_{n,a}(R^{-1})\}<0}                 \tag{21}
\]

for every sufficiently large \(R\). This is a **single-point** witness,
not the two-point Hankel minor of `104_37`.

There are arbitrarily large primes. Consequently, a real prime \(p\)
with \(R=\log p\) can be chosen within the range of (21), and then

\[
 \mathcal Q_{K_{n,a}}
   ((\log p)\delta_{\log p})
 = (\log p)^2K_{n,a}(\log p,\log p)<0.                      \tag{22}
\]

The atom of (22) lies on the real prime support and carries exactly the
canonical weight \(\log p\). So not even the residual square required by
the adjacent Schur step is an energy over the canonical atomic directions.

## 5. Collision defect: why the Schur square is not Hankel

There is a local obstruction independent of the tail. Every kernel
produced by a Selberg convolution depends on \(u+v\). By contrast, the
rank-one kernel appearing in (18) is not Hankel. From (10),

\[
 \ell_{n,a}(0)=0,\qquad \ell_{n,a}'(0)=-na^2.               \tag{23}
\]

Taking two decompositions of the same number \(5x\), one obtains

\[
 \boxed{
 \lim_{x\downarrow0}{
 \ell_{n,a}(x)\ell_{n,a}(4x)
 -\ell_{n,a}(2x)\ell_{n,a}(3x)\over x^2}
 =-2n^2a^4<0.}                                             \tag{24}
\]

If there existed a function \(J\) with
\(J(u+v)=\ell_{n,a}(u)\ell_{n,a}(v)\) in a neighborhood, the two products
of (24) would be identical. Hence the scalar square of the cross entry
cannot be identified with the Selberg quadratic convolution. The
difference is not a small constant: it already appears at order \(x^2\)
with explicit coefficient \(-2n^2a^4\).

## 6. Decision

```text
proved unconditionally:
  the complete regulated form (7)--(8), with pole and higher powers;
  the exact cross-entry response (10)--(12);
  the identity cancellation of the mu*mu Selberg term (16);
  the exact residual kernel (18);
  negative diagonal (21) for every n>=2;
  a single-atom witness with canonical prime support and weight (22);
  the quantitative collision defect (24).

ruled out:
  using the Selberg square as a positive reserve to pay for the Schur
  term;
  representing exactly the square of the cross entry by a
  convolution/Hankel kernel;
  closing T_n>=0 by declaring the quadratic remainder of (17) PSD.

remains open:
  a value inequality for the complete canonical measure that preserves
  the cancellation between the linear part of (17), its indefinite
  quadratic part, the archimedean block, and C_{n,a};
  T_n>=0 for every n>=149, A1, and RH.
```

`tools/canonical_selberg_square_gate_check.py` checks with `Fraction` the
cancellation (16) on formal atomic measures, identity (10), the leading
coefficients of (19)–(21), and the collision coefficient (24).
</content>
