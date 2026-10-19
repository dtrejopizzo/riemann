# 104_37 — Adjacent taper, Selberg inversion, and the two-point Hankel gate

**Status.** The collective Selberg inversion of `104_35` was applied to
the exact tapered vector of `104_34`, including the optimal value
\(t_n^*\). The regulated Laguerre test closes into a single-polynomial
formula:

\[
 w_{n,t,a}(u)=ae^{-au}
 \{L_{n-1}^{(1)}(au)+tL_n(au)+t(t-1)\}.
 \tag{1}
\]

The inversion is done before taking signs. However, the taper does not
turn the resulting Hankel form into a coercive energy. For **every**
\(t\in\mathbb R\), including \(t=t_n^*\), a two-point compression has
strictly negative leading determinant in the tail. The leading coefficient
is \(8^d-9^d<0\), with \(d\ge147\) in the phase's range. The same witness
can be placed on logarithms of real primes.

This rules out exactly the closing of the adjacent compression via Hankel
positivity after the Selberg inversion. It does not refute
\(\mathcal T_n\ge0\) for the canonical weights \(\log p\): a proof of that
statement would still have to use a special signed cancellation among
Selberg's linear term, its quadratic term, the archimedean block, and the
higher-power correction. Hence this document proves neither A1 nor RH.

## 1. Pre-registration and scope

Let

\[
 c={501\over2002},\qquad \kappa=1-c={1501\over2002},
 \qquad H_n=\lambda_n-cA_n,
 \tag{2}
\]

and

\[
 d_n=\kappa\Delta A_n+\gamma,
 \qquad
 \mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2.
 \tag{3}
\]

The front of `104_34` is proving \(\mathcal T_n\ge0\) for every
\(n\ge149\). The only idea tested here is:

1. writing the form exactly over
   \(h_{n,t}=g_n+t\phi_n\);
2. removing the powers \(p^k,\ k\ge2\), ordinarily, as in `104_32`;
3. collectively inverting the simple-prime Selberg identity;
4. attempting to obtain the sign at \(t=t_n^*\) from a Hankel energy.

No absolute-value bound, zero localization, or conditional result is
used. The off-line falsifier of `104_34` remains binding: a mechanism
proving \(\mathcal T_n\ge0\) using only functional symmetry would have to
fail against that quartet. The witness of Section 5 is more specific: it
kills Hankel positivity even on the support of real primes, without
claiming to alter the canonical weights.

## 2. Exact tapered form

Recall

\[
 g_n=e^{-x/2}L_{n-1}^{(1)}(x),\qquad
 \phi_n=e^{-x/2}L_n(x),\qquad g_{n+1}=g_n+\phi_n.
 \tag{4}
\]

For any sequence \(X_0=0,X_1,X_2,\ldots\), its Toeplitz polarization over
the plane \(\mathrm{span}\,\{g_n,\phi_n\}\) gives

\[
 \boxed{
 X_{n,t}:=X_n+t(X_{n+1}-X_n-X_1)+t^2X_1.}
 \tag{5}
\]

Indeed, the cross entry is
\((X_{n+1}-X_n-X_1)/2\). Set

\[
 P_n:=B_n^{(p+\mathrm{pole})},\qquad
 C_n:=P_{n-1}^{(\ge2)}(1)\quad(n\ge1),\qquad P_0=C_0=0.
 \tag{6}
\]

Identity (24) of `104_32` implies

\[
 B_n=A_n-\lambda_n=C_n-P_n.                                 \tag{7}
\]

Hence, with no informal limit or omitted term,

\[
 \mathsf Q_0[h_{n,t}]=C_{n,t}-P_{n,t}.                       \tag{8}
\]

The flag orthogonality of `104_34` in turn gives

\[
 \mathsf A_{\rm flag}[h_{n,t}]=A_n+t^2\Delta A_n,             \tag{9}
\]

and the margin form is

\[
 \boxed{
 \mathsf M[h_{n,t}]
 =\kappa(A_n+t^2\Delta A_n)-C_{n,t}+P_{n,t}.}
 \tag{10}
\]

Recomposing (7), (10) is exactly

\[
 \mathsf M[h_{n,t}]
 =H_n-t(H_n+d_n-H_{n+1})+t^2d_n.                            \tag{11}
\]

In particular,

\[
 t_n^*={H_n+d_n-H_{n+1}\over2d_n},\qquad
 \boxed{\mathsf M[h_{n,t_n^*}]={\mathcal T_n\over4d_n}.}     \tag{12}
\]

So the taper does not approximate the Schur determinant: it evaluates it
exactly.

## 3. Simple-prime Laguerre test

With the measures of `104_35`,

\[
 d\alpha=\sum_p\log p\,\delta_{\log p},\qquad
 d\beta=e^u\,du,\qquad d\mu=d\alpha-d\beta,                 \tag{13}
\]

let, for \(a>1\),

\[
 w_{n,a}(u)=ae^{-au}L_{n-1}^{(1)}(au),\qquad
 P_{n,a}=\langle w_{n,a},\beta-\alpha\rangle.                \tag{14}
\]

Applying (5) before removing the regulator,

\[
 w_{n,t,a}
 =w_{n,a}+t(w_{n+1,a}-w_{n,a}-w_{1,a})+t^2w_{1,a}.           \tag{15}
\]

The identity
\(L_n^{(1)}-L_{n-1}^{(1)}=L_n\) turns (15) into formula
(1), and hence

\[
 \boxed{
 P_{n,t,a}=\langle w_{n,t,a},\beta-\alpha\rangle,
 \qquad P_{n,t}=\lim_{a\downarrow1}P_{n,t,a}.}               \tag{16}
\]

Note the term \(t(t-1)\). Omitting it would amount to forgetting the
diagonal entry of \(\phi_n\) or the \(-X_1\) term of the cross
polarization.

## 4. Collective inversion before the sign

Define, as in `104_35`,

\[
 (\mathcal Tg)(v)=vg(v)+2e^{-v}\int_v^\infty e^ug(u)\,du,
 \qquad
 \mathcal Q_g(\nu)=\iint g(u+v)\,d\nu(u)d\nu(v),             \tag{17}
\]

and

\[
 d\mathcal B_p=u\,d\mu+2\beta*\mu+\mu*\mu.                 \tag{18}
\]

The decreasing solution of
\(\mathcal TG_{n,t,a}=w_{n,t,a}\) is

\[
 \boxed{
 G_{n,t,a}(v)={1\over v}\left[w_{n,t,a}(v)
 -2v^2e^{-v}\int_v^\infty{e^uw_{n,t,a}(u)\over u^3}\,du
 \right].}                                                  \tag{19}
\]

(18) is used first, and only afterward is the sign examined. This gives
the fully coupled identity

\[
 \boxed{
 P_{n,t,a}
 =-\langle G_{n,t,a},\mathcal B_p\rangle
   +\mathcal Q_{G_{n,t,a}}(\mu).}                            \tag{20}
\]

Inserting (20) into (10), neither any prime nor the pole has been
separated:

\[
 \mathsf M[h_{n,t}]
 =\kappa(A_n+t^2\Delta A_n)-C_{n,t}
  +\lim_{a\downarrow1}
   \{-\langle G_{n,t,a},\mathcal B_p\rangle
       +\mathcal Q_{G_{n,t,a}}(\mu)\}.                      \tag{21}
\]

The precise question is whether the value \(t=t_n^*\) turns the last term
into an energy with a proportional lower bound. The answer for Hankel
positivity is no, uniformly in \(t\).

## 5. Quantitative two-point Hankel witness

We use an elementary fact that avoids deciding the pointwise sign of
\(G_{n,t,a}\).

**Lemma 5.1.** Let
\(w(v)=ae^{-av}P(av)\), \(a>1\), where \(P\) is a real polynomial of
degree \(D\ge2\) with leading coefficient \(p_D\ne0\). If \(G\) is (19),
then, with \(d=D-1\) and \(C=p_Da^{D+1}\),

\[
 G(v)=Ce^{-av}v^d\{1+O_{P,a}(v^{-1})\}.                     \tag{22}
\]

Consequently,

\[
 \boxed{
 \begin{aligned}
 &G(2R)G(4R)-G(3R)^2\\
 &\quad=C^2e^{-6aR}R^{2d}
       \{8^d-9^d+O_{P,a}(R^{-1})\}<0
 \end{aligned}}                                             \tag{23}
\]

for every sufficiently large \(R\).

**Proof.** The first summand of (19) is
\(Ce^{-av}v^{D-1}\{1+O(v^{-1})\}\). Since \(a-1>0\), integrating by parts
in the second summand shows that it is
\(O(e^{-av}v^{D-2})\). This proves (22). Substituting \(2R,3R,4R\) gives
(23), and \(8^d-9^d<0\) for \(d\ge1\). \(\square\)

For (1), the degree and coefficient are

\[
 \begin{array}{c|c|c|c}
 &D&d&C\\ \hline
 t\ne0&n&n-1&t(-1)^n a^{n+1}/n!\\
 t=0&n-1&n-2&(-1)^{n-1}a^n/(n-1)!.
 \end{array}                                                \tag{24}
\]

Hence (23) holds for every \(n\ge3\) and **every** \(t\in\mathbb R\). In
particular it holds for the arithmetic number \(t_n^*\), whether zero or
not. In the range \(n\ge149\), the exponent satisfies \(d\ge147\).

Determinant (23) is the leading principal minor of the Hankel matrix

\[
 \begin{pmatrix}G(2R)&G(3R)\\G(3R)&G(4R)\end{pmatrix}.       \tag{25}
\]

So form \(\mathcal Q_G\) is indefinite on measures supported on
\(\{R,2R\}\). This is not the earlier observation that \(G\) changes
sign: even if both diagonal entries of (25) are positive, the negative
determinant produces a strictly negative direction.

The witness can live on the real prime support. Let \(p\to\infty\) be
primes and, by Bertrand's postulate, choose a prime \(q\) with
\(p^2<q<2p^2\). If \(R=\log p\), \(S=\log q\), then
\(S/R\to2\), and (22) gives

\[
 \begin{aligned}
 &G(2R)G(2S)-G(R+S)^2\\
 &\quad=C^2e^{-2a(R+S)}R^{2d}
 \left\{\left(4{S\over R}\right)^d
 -\left(1+{S\over R}\right)^{2d}+O(R^{-1})\right\}<0.      \tag{26}
 \end{aligned}
\]

The main inequality is strict because
\((R+S)^2-4RS=(R-S)^2>0\). So the restriction of the kernel to
\(\{\log p:\ p\text{ prime}\}\) is not positive semidefinite either.

## 6. Decision and remaining front

Identity (21) shows exactly what happens. Positivity of Selberg's
non-centered measure does not by itself turn
\(\mathcal Q_{G_{n,t,a}}\) into an energy. The optimal taper generally
raises the tail degree from \(n-2\) to \(n-1\), but it does not change
the negative minor (23). The archimedean block and \(C_{n,t}\) are fixed
scalars and do not repair a semidefiniteness claim about the kernel.

It is not concluded that (21) is negative for the real arithmetic
measure. In that measure, the linear and quadratic terms of (20) may
cancel in a special way; indeed, that cancellation is the only thing that
could still prove \(\mathcal T_n\ge0\). What is ruled out is inferring it
from a Hankel coercivity produced by Selberg, even after optimizing the
taper.

```text
proved unconditionally:
  the exact flag tapered form (10)--(12);
  the exact simple-prime Laguerre test (1), including t(t-1);
  the collective inversion (19)--(21) before taking signs;
  a negative Hankel minor with leading term 8^d-9^d;
  the same gate restricted to logarithms of real primes;
  coverage of every t, including t_n^* and the case t_n^*=0.

ruled out:
  closing the adjacent Schur step via positivity/PSD of the tapered
  Selberg kernel;
  attributing to the taper a Hankel energy absent in the original vector.

remains open:
  a joint signed bound using the exact weights log p in both terms of
  (20), together with C_{n,t} and the archimedean block;
  T_n >= 0 for every n >= 149, A1, and RH.
```

`tools/tapered_selberg_hankel_gate_check.py` checks with `Fraction` the
polynomial identity (1), the leading coefficients of (24), and the model
minor \(8^d-9^d<0\), with no floating-point sign decisions.
</content>
