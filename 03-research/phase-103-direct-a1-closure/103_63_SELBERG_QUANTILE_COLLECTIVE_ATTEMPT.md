# Selberg--quantile collective attempt: exact Hankel form and coercivity obstruction

## Verdict

There is an exact way to insert the canonical quantile kernel of `103_59`
and `103_61` **before** taking a sign in Selberg's identity.  In logarithmic
coordinates it gives

\[
 \boxed{\qquad
 C_{n,\varepsilon}
   =\langle g_{n,\varepsilon},{\cal B}\rangle
    -\iint g_{n,\varepsilon}(u+v)\,d\mu(u)d\mu(v),
 \qquad}                                                   \tag{1}
\]

where \(\mu\) is the exact prime--pole discrepancy, \({\cal B}\) is the
centered Selberg measure, and \(g_{n,\varepsilon}\) is given explicitly in
(21) below.  Thus Selberg convolution does create a genuinely collective
bilinear term; it is not the local positive-coefficient pullback rejected in
`103_17`.

The new term is not coercive.  For every odd \(n\), the diagonal
\(g_{n,\varepsilon}(2u)\) is negative for all sufficiently large \(u\).
Consequently its Hankel form is not positive semidefinite.  The other term
in (1) is also signed: positivity belongs to the uncentered measure
\(u\,d\alpha+\alpha*\alpha\), not to \({\cal B}\) after the continuous
reference is subtracted.

This is not only a pointwise-kernel objection.  Positive measures with
counting discrepancy \(O(1)\) and centered Selberg discrepancy \(O(x)\)
can have either sign, and arbitrarily large positive size, for the same
quantile functional.  Hence the exact Selberg identity and the usual
Selberg-symmetry scale do not imply the A1 comparison.  This does **not**
rule out a further theorem special to the discrete weights
\(\Lambda(p^k)=\log p\); it proves that such a theorem is additional to the
standard Selberg convolution identity.

No RH statement is assumed or proved here.

## 1. Selberg's measure identity from first principles

For \(\Re s>1\), absolute convergence of the Euler product gives

\[
 L(s):=-{\zeta'(s)\over\zeta(s)}
      =\sum_{m\geq2}{\Lambda(m)\over m^s}.                    \tag{2}
\]

Termwise differentiation and multiplication are legitimate there, so

\[
 {\zeta''(s)\over\zeta(s)}=-L'(s)+L(s)^2
 =\sum_{m\geq1}{A(m)\over m^s},                               \tag{3}
\]

with

\[
 \boxed{\quad A(m)=\Lambda(m)\log m+(\Lambda*\Lambda)(m)\geq0.\quad}
                                                                    \tag{4}
\]

Equation (4), including the convolution and its sign, follows merely by
collecting the coefficient of \(m^{-s}\); no form of the PNT is involved.

Put \(u=\log x\), and introduce the locally finite measures on
\([0,\infty)\)

\[
 d\alpha(u)=\sum_{m\geq2}\Lambda(m)\,\delta_{\log m}(du),
 \qquad d\beta(u)=e^u\,du,
 \qquad d\mu=d\alpha-d\beta.                                  \tag{5}
\]

Convolution below is additive convolution.  The measure in (4) is exactly

\[
 d{\cal A}=u\,d\alpha+\alpha*\alpha.                            \tag{6}
\]

The continuous reference is equally exact, because

\[
 (\beta*\beta)(du)
 =\left(\int_0^u e^v e^{u-v}\,dv\right)du
 =u e^u\,du=u\,d\beta(u).                                      \tag{7}
\]

Therefore its two Selberg pieces sum to \(2u\,d\beta\).  Define the
centered Selberg measure

\[
 d{\cal B}:=d{\cal A}-2u\,d\beta.                              \tag{8}
\]

Substitution of \(\alpha=\beta+\mu\) in (6), followed only by bilinearity
of convolution and (7), proves the central identity

\[
 \boxed{\quad
 d{\cal B}=u\,d\mu+2\,\beta*\mu+\mu*\mu.
 \quad}                                                        \tag{9}
\]

This is Selberg's identity in discrepancy coordinates.  In Mellin form it
is the elementary Riccati identity

\[
 {\zeta''\over\zeta}(1+t)-{2\over t^2}
 =-R'(t)+{2R(t)\over t}+R(t)^2,
 \qquad
 R(t)=L(1+t)-{1\over t}.                                       \tag{10}
\]

Thus (9) has not imported a hidden zero estimate: it is exactly (2)--(4)
with the double pole centered.

## 2. Insert the quantile kernel before taking signs

Fix \(n\geq1\) and \(\varepsilon>0\), and write \(a=1+\varepsilon\).
Retain the completed kernel of `103_59`,

\[
 \begin{split}
 K_{n,\varepsilon}(u)
   &=aL_n^{(1)}(u)-\varepsilon L_{n-1}^{(1)}(u),\\
 h_{n,\varepsilon}(v)
   &=T_{n,\varepsilon}(v)
     =\int_v^\infty e^{-au}K_{n,\varepsilon}(u)\,du.
 \end{split}                                                    \tag{11}
\]

The normalization proved in `103_59` is

\[
 h_{n,\varepsilon}(0)=1.                                      \tag{12}
\]

Pushing \(d\psi-dx\) through \(u=\log x\), the exact canonical cost is

\[
 \boxed{\quad C_{n,\varepsilon}=\langle h_{n,\varepsilon},\mu\rangle.
 \quad}                                                        \tag{13}
\]

This is the same quantity as the quantile integral and cell sum in
`103_59`--`103_61`; (13) changes only its coordinates.

For a test function \(g\) for which the displayed integrals converge,
pairing (9) with \(g\) gives

\[
 \langle g,{\cal B}\rangle
 =\langle {\cal T}g,\mu\rangle+Q_g(\mu),                        \tag{14}
\]

where

\[
 ({\cal T}g)(v)
 =v g(v)+2e^{-v}\int_v^\infty e^w g(w)\,dw,                     \tag{15}
\]

and

\[
 Q_g(\mu)=\iint_{[0,\infty)^2}g(u+v)\,d\mu(u)d\mu(v).          \tag{16}
\]

The second term in (15) is exactly the pairing with
\(2\beta*\mu\); hence no signed term has been discarded.

## 3. Exact inversion of the linear Selberg operator

We now solve

\[
 {\cal T}g=h_{n,\varepsilon}                                   \tag{17}
\]

rather than estimate its two terms separately.  For \(v>0\), set

\[
 H(v)=v^2e^{-v}\int_v^\infty
          {e^t h_{n,\varepsilon}(t)\over t^3}\,dt,              \tag{18}
\]

and

\[
 g_{n,\varepsilon}(v)
 ={h_{n,\varepsilon}(v)-2H(v)\over v}.                          \tag{19}
\]

The integral in (18) converges at infinity because \(h\) is a polynomial
times \(e^{-av}\).  Differentiation gives

\[
 H'(v)=\left({2\over v}-1\right)H(v)-{h(v)\over v},
 \qquad g(v)=-H'(v)-H(v).                                      \tag{20}
\]

Although (18) has a singular-looking integrand at zero, the cancellation
can be checked coefficient by coefficient.  Write

\[
 e^t h(t)=1+bt+O(t^2).
\]

Then

\[
 \int_v^\infty {e^t h(t)\over t^3}\,dt
 ={1\over2v^2}+{b\over v}+O(|\log v|),
\]

where the part of the integral above any fixed small endpoint contributes
only \(O(1)\).  Hence

\[
 H(v)={1\over2}+\left(b-{1\over2}\right)v
       +O(v^2|\log v|),
 \qquad
 h(v)=1+(b-1)v+O(v^2).
\]

It follows directly from (19) that
\(g(v)=-b+O(v|\log v|)\).  Thus \(g\) has a finite limit at zero, and we
define \(g(0)=-b\).
Moreover, integrating the second identity in (20), with the exponentially
decaying boundary value at infinity, yields

\[
 H(v)=e^{-v}\int_v^\infty e^w g(w)\,dw.
\]

Substitution in (19) proves \({\cal T}g=h\), including at zero by
continuity.  We have therefore obtained the promised explicit inverse

\[
 \boxed{\quad
 g_{n,\varepsilon}(v)
 ={1\over v}\left[
 h_{n,\varepsilon}(v)
 -2v^2e^{-v}\int_v^\infty
 {e^t h_{n,\varepsilon}(t)\over t^3}\,dt\right].
 \quad}                                                        \tag{21}
\]

For fixed \(\varepsilon>0\), \(g(v)=O_{n,\varepsilon}
(e^{-av}(1+v^{n-1}))\).  Hence (14)--(16) are absolutely convergent if
each occurrence of \(\mu=\alpha-\beta\) is expanded before integration:
the four positive product measures are controlled by
\(\sum\Lambda(m)m^{-a}<\infty\) and
\(\int_0^\infty e^{-\varepsilon u}(1+u^{n-1})du<\infty\).
The same observation controls \({\cal A}\) by (3).  Inserting (17) into
(14) proves (1) rigorously at every fixed regulator.

## 4. Why the quadratic term is not a square

The leading coefficient of (11) gives, for fixed \(n,\varepsilon\),

\[
 h_{n,\varepsilon}(v)
 ={(-1)^n\over n!}e^{-av}v^n\{1+O_{n,\varepsilon}(v^{-1})\}.
                                                                    \tag{22}
\]

This follows by one integration by parts, since the leading term of
\(K_{n,\varepsilon}\) is
\(a(-1)^nv^n/n!\).  Applying the same elementary tail estimate in (18)
gives

\[
 H(v)={(-1)^n\over n!\,\varepsilon}
       e^{-av}v^{n-1}\{1+O_{n,\varepsilon}(v^{-1})\}.            \tag{23}
\]

Consequently

\[
 \boxed{\quad
 g_{n,\varepsilon}(v)
 ={(-1)^n\over n!}e^{-av}v^{n-1}
   \{1+O_{n,\varepsilon}(v^{-1})\}.
 \quad}                                                        \tag{24}
\]

For every odd \(n\), (24) implies \(g(2R)<0\) for all sufficiently large
\(R\).  Taking even the positive finite measure \(\sigma=\delta_R\) gives

\[
 Q_g(\sigma)=g(2R)<0.                                          \tag{25}
\]

Thus the Hankel kernel \((u,v)\mapsto g(u+v)\) is not positive
semidefinite.  In particular, (16) cannot be represented as a positive
mixture of Laplace squares
\(\int|\int e^{-tu}d\mu(u)|^2d\rho(t)\) with \(d\rho\geq0\).
This is a collective obstruction: it tests the actual two-variable
convolution term after the inverse Selberg operator has been applied, not
the sign of one Laguerre polynomial in `103_17`.

## 5. Exact positive-measure countermodels at the Selberg scale

The failure above is not repaired by imposing a strong counting envelope
and the usual order of the Selberg symmetry remainder.  Fix \(c>0\) and
\(R>0\), and replace the arithmetic measure only for this audit by

\[
 \alpha_{c,R}=\beta+c\delta_R,
 \qquad \mu_{c,R}=c\delta_R.                                   \tag{26}
\]

This is a positive locally finite measure.  Its counting discrepancy from
\(\beta\) is exactly \(0\) below \(R\) and \(c\) above \(R\), hence is
\(O(1)\), much smaller than any PNT envelope.  Its uncentered Selberg
measure \(u\alpha_{c,R}+\alpha_{c,R}*\alpha_{c,R}\) is positive and (9)
holds identically.  In fact, direct substitution gives

\[
 d{\cal B}_{c,R}
 =cR\delta_R
  +2c e^{w-R}{\bf1}_{w\geq R}\,dw
  +c^2\delta_{2R}.                                              \tag{27}
\]

Therefore

\[
 |{\cal B}_{c,R}([0,U])|
 \leq cR+2ce^{U-R}+c^2=O_{c,R}(e^U).                            \tag{28}
\]

In \(x=e^U\) coordinates this is precisely the \(O(x)\) scale of the
centered Selberg symmetry formula.  Every assertion in (26)--(28) is an
exact measure calculation.

On the other hand, its quantile linear functional is

\[
 C_{n,\varepsilon}[\alpha_{c,R}]
 =c\,h_{n,\varepsilon}(R).                                     \tag{29}
\]

By (12) and continuity this is positive for all sufficiently small
positive \(R\).  For odd \(n\), (22) makes it negative for all sufficiently
large \(R\).  At a fixed small \(R\), increasing \(c\) makes the positive
value in (29) exceed any prescribed finite archimedean budget, while the
counting error remains \(O(1)\) and (28) remains \(O(x)\).

This countermodel is deliberately not claimed to have prime-power support
or weights \(\log p\).  Its exact conclusion is narrower and important:

> positivity of the Selberg measure, the Selberg convolution identity, a
> PNT-sized counting discrepancy, and the \(O(x)\) Selberg-symmetry scale
> do not imply the required quantile inequality.

The discrete prime-power structure must enter through an additional
theorem; it is not encoded by the formal positivity in (4).

## Status

The attempted route has produced a new exact formula rather than merely
repeating the no-go in `103_17`:

1. equations (9) and (14) retain the full \(\Lambda\log\) and
   \(\Lambda*\Lambda\) coupling;
2. equation (21) inserts the canonical quantile/Laguerre response before
   any sign or absolute value;
3. equation (1) is the resulting exact linear-minus-quadratic collective
   identity;
4. equations (24)--(25) prove that its quadratic term is not coercive;
5. equations (26)--(29) prove that Selberg positivity and symmetry scale
   alone permit both quantile signs.

What remains logically possible is a new inequality for (1) using the
specific discrete interlacing and weights of every actual prime-power
tower.  No such inequality has been proved here, so A1 and RH remain open.
