# 104_116 — Triangular-exchange Mecke identity and the source–circulation gate

## Result

The Mecke identity requested for the `104_115` pivot exists and is proved
in closed form. Let (s=1+\varepsilon>1), let

\[
 \mathbb P_s(N=n)={n^{-s}\over\zeta(s)},
 \qquad N=\prod_pp^{A_p},                                  \tag{1}
\]

and let (\omega=(\omega_{pq})) be an antisymmetric matrix of finite
support. Define

\[
 (J_\omega G)(N)
 =\sum_{p\ne q}\omega_{pq}
   \left({q\over p}\right)^{s/2}
   \mathbf1_{A_q\ge1}\,G(Np/q).                          \tag{2}
\]

Then

\[
 \boxed{
 \langle F,J_\omega G\rangle_s
 =\sum_{p\ne q}{\omega_{pq}\over(pq)^{s/2}}
   \mathbb E_s\{\overline{F(qN)}G(pN)\}.}                \tag{3}
\]

The operator is anti-self-adjoint. Moreover (J_\omega\mathbf1=0) if and
only if, with (u_p=p^{-s/2}),

\[
 \omega u=0.                                               \tag{4}
\]

On a triple (a<b<c), (4) fixes, up to a scalar (\kappa), the local
current

\[
 \omega_{ab}=\kappa c^{-s/2},\qquad
 \omega_{bc}=\kappa a^{-s/2},\qquad
 \omega_{ca}=\kappa b^{-s/2}.                             \tag{5}
\]

Its bilinear form is the cyclic determinant

\[
\boxed{
\begin{aligned}
 \langle F,J_{a,b,c}G\rangle_s
 ={\kappa\over(abc)^{s/2}}\mathbb E_s\{&
  \overline{F(bN)}G(aN)-\overline{F(aN)}G(bN)\\
 &+\overline{F(cN)}G(bN)-\overline{F(bN)}G(cN)\\
 &+\overline{F(aN)}G(cN)-\overline{F(cN)}G(aN)\}.
                                                               \tag{6}
\end{aligned}}
\]

Identity (3)–(6) preserves the other primes inside (N), is signed, and
uses no absolute values. However, it does not produce the bridge claimed
in `104_115`: it is a **bilinear circulation**, whereas
(B_{n,s}) is a **linear prime–pole source**. The difference is not an
automatically positive Hardy remainder. The boundary term that would turn
a circulation into a source exactly reconstitutes the prime–pole
functional (B_{n,s}), whose sign is A1.

Hence the Mecke identity is proved, but it is refuted that it, by itself,
completes the resolvent certificate. This document proves neither A1 nor
RH.

---

## 1. Mecke's formula for removing one unit from a tower

The exponents in (1) are independent and

\[
 \mathbb P_s(A_p=k)=(1-p^{-s})p^{-ks},\qquad k\ge0.        \tag{7}
\]

For every integrable function (H), shifting (A_q=k+1) to (k) gives

\[
 \boxed{
 \mathbb E_s\{\mathbf1_{A_q\ge1}H(N)\}
 =q^{-s}\mathbb E_s\{H(qN)\}.}                           \tag{8}
\]

Applying (8) to

\[
 H(N)=\overline{F(N)}G(Np/q)
\]

gives

\[
\begin{aligned}
 &\mathbb E_s\{\mathbf1_{A_q\ge1}
       \overline{F(N)}G(Np/q)\}\\
 &\qquad=q^{-s}\mathbb E_s\{\overline{F(qN)}G(pN)\}.
                                                               \tag{9}
\end{aligned}
\]

Multiplying by
(\omega_{pq}(q/p)^{s/2}) and summing proves (3).

## 2. Anti-self-adjointness and conservation

Grouping in (3) the pairs ((p,q)) and ((q,p)),

\[
\begin{aligned}
 \langle F,J_\omega G\rangle_s
 =\sum_{p<q}{\omega_{pq}\over(pq)^{s/2}}
 \mathbb E_s\{&\overline{F(qN)}G(pN)\\
               &-\overline{F(pN)}G(qN)\}.
                                                               \tag{10}
\end{aligned}
\]

Swapping (F,G) and conjugating proves

\[
 J_\omega^*=-J_\omega.                                   \tag{11}
\]

On the other hand, directly from (2),

\[
 (J_\omega\mathbf1)(N)
 =\sum_{q:A_q\ge1}q^{s/2}\sum_p\omega_{pq}p^{-s/2}.       \tag{12}
\]

This vanishes for every (N) exactly when (\omega u=0), since
antisymmetry makes the right and left kernels equivalent.

In dimension three, every nonzero antisymmetric matrix has a
one-dimensional kernel. Substituting (5) directly shows that its kernel
vector is

\[
 (a^{-s/2},b^{-s/2},c^{-s/2}),                            \tag{13}
\]

which proves the uniqueness of (5). Inserting it into (10) proves (6).

## 3. Laguerre specialization

Take

\[
 F_n(N)=L_{n-1}^{(1)}(\log N),\qquad
 G_n(N)=L_{n-2}^{(2)}(\log N)=-{d\over dx}
 L_{n-1}^{(1)}(x)\bigg|_{x=\log N}.                       \tag{14}
\]

Then (6) is an exact average of signed areas of the curve

\[
 x\longmapsto
 \bigl(L_{n-1}^{(1)}(x),L_{n-2}^{(2)}(x)\bigr)            \tag{15}
\]

evaluated at the three shifts

\[
 x+\log a,\qquad x+\log b,\qquad x+\log c.                \tag{16}
\]

This explains the nonzero cross term observed in `104_115`. It also
explains why no free global sign appears: curve (15) turns every time the
Laguerre function crosses one of its zeros.

## 4. Why (B_{n,s}) does not appear

The regularized prime–pole form is linear in the test function:

\[
 M_s(f)
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
  -\int_0^\infty e^{-(s-1)x}f(x)\,dx,
 \qquad B_{n,s}=sM_s(f_{n,s}).                            \tag{17}
\]

In contrast, (3) is alternating and bilinear:

\[
 \langle F,J_\omega F\rangle_s=0,
 \qquad
 \langle F,J_\omega(G+cF)\rangle_s
 =\langle F,J_\omega G\rangle_s.                         \tag{18}
\]

It also annihilates constants by construction. Functional (17) does not:

\[
 M_s(1)=-{\zeta'(s)\over\zeta(s)}-{1\over s-1},          \tag{19}
\]

which is not identically zero. Hence there is no natural identification
of (3) with (M_s) on a linear test class containing the constants. An
open current toward the continuous comparator would need to be added.

Let (J^{\rm open}) be that hypothetical extension. The
discrete–continuous divergence identity would necessarily have the form

\[
 \langle\mathbf1,J^{\rm open}f\rangle=M_s(f).             \tag{20}
\]

But (20), with the Laguerre test function, is precisely the functional
one wants to bound. Closing the current to recover positivity eliminates
(20); opening it to recover (17) reintroduces (B_{n,s}) with its unknown
sign. This is the source–circulation gate.

The general second-order Palm identity of `104_50` expresses the same
obstruction in covariance coordinates:

\[
 \mathbb E_s[Z_fZ_g]
 =\mathrm{Cov}_s(D_f,D_g)+M_s(f)M_s(g).             \tag{21}
\]

The new formula (3) does not contradict (21): it extracts the alternating
part of the exchanges, while (21) extracts the symmetric part. Neither of
the two by itself orients the linear term (M_s(f)).

## 5. Consequence for the `104_115` certificate

The matrix block

\[
 \begin{pmatrix}-S&\eta J_\omega\\-\eta J_\omega&-S\end{pmatrix}
                                                               \tag{22}
\]

can be positive by Schur's criterion, and its cross term is computed
exactly by (6). But the claimed identity

\[
 {3\over4}A_n-\delta_n-B_{n,s}
 =\langle G_n,(22)G_n\rangle+\mathcal R_{n,s}             \tag{23}
\]

with (\mathcal R_{n,s}\ge0) does not exist as a consequence of Mecke's
formula. Defining \(\mathcal R_{n,s}\) by (23) merely renames A1. To
support (23) one would need an additional theorem comparing the open
source (20) with the circulation energy (22); that is again a signed
prime–pole inequality, not an identity.

## Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 triangle_exchange_mecke_check.py
```
</content>
