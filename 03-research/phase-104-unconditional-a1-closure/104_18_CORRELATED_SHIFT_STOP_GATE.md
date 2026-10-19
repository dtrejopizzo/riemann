# 104_18 — Finite correlated shift: identity and stop-gate

**Role.** Keep the regulator
\(\varepsilon\downarrow0\) and the Jordan shift \(u\downarrow0\) finite and
correlated, before taking the first jet. The goal was to check whether the
exact positivity of \(J_u\) survives the pole–Euler collision and produces
the A1 bound. The result is negative but precise: a new finite identity is
obtained, an exact renewal equation, and three falsifiers. The limit returns
to the signed cost \(C_n\) of `104_16`.

This document **does not prove A1 or RH**.

## 1. Pre-registration and internal non-duplication

Let

\[
 F(s)=(s-1)\zeta(s),\qquad
 A_u(s)={\zeta(s-u)\over\zeta(s)},\qquad
 H_u(s)={F(s-u)\over F(s)}.
 \tag{1}
\]

`104_16` already proved the infinitesimal jet

\[
 \left.\partial_uH_u(s)\right|_{u=0}=-{F'(s)\over F(s)}
 \tag{2}
\]

and its Cayley–Laguerre pullback. What is tested here is not another jet:
one fixes

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z},
 \qquad u=c\varepsilon,\qquad 0<c<1,                 \tag{3}
\]

and keeps \(H_{c\varepsilon}\) exact right up until after the coefficient is
extracted.

**Allowed inputs.** Only the absolutely convergent series of
\(A_u\) in \(\Re s>1+u\), the Laguerre generating identity, Abel
summation, and the real order of \(F\) on \((1,\infty)\) are used.

**Mandatory falsifier.** Any sign inference must survive the symmetric
product \(X_a(s)=\xi(s+a)\xi(s-a)\), which has zeros off the line
\(1/2\) for every \(a>0\).

## 2. Finite coefficient theorem

For \(\Re s>1+u\),

\[
 A_u(s)=\sum_{m\ge1}{J_u(m)\over m^s},
 \qquad
 J_u(m)=m^u\prod_{p\mid m}(1-p^{-u})\ge0.            \tag{4}
\]

Define

\[
 a_n(u,\varepsilon)
 :=\sum_{m\ge1}{J_u(m)\over m^{1+\varepsilon}}
                    L_n(\log m).                    \tag{5}
\]

The generating identity

\[
 {e^{-xz/(1-z)}\over1-z}=\sum_{n\ge0}L_n(x)z^n
\]

gives, for \(z\) in a neighborhood of the origin,

\[
 \boxed{
 {A_u(s_\varepsilon(z))\over1-z}
 =\sum_{n\ge0}a_n(u,\varepsilon)z^n.}               \tag{6}
\]

Since

\[
 H_u(s)=\left(1-{u\over s-1}\right)A_u(s),          \tag{7}
\]

for \(u=c\varepsilon\) the polar factor is exactly

\[
 P_{c,\varepsilon}(z)
 ={(1-c)\varepsilon+[1-(1-c)\varepsilon]z
   \over \varepsilon+(1-\varepsilon)z}.             \tag{8}
\]

If

\[
 {H_u(s_\varepsilon(z))\over1-z}
 =\sum_{n\ge0}b_n(u,\varepsilon)z^n,                \tag{9}
\]

then (6)–(8) prove the finite recurrence

\[
 \boxed{
 \begin{aligned}
  \varepsilon b_0&=(\varepsilon-u)a_0,\\
  \varepsilon b_n+(1-\varepsilon)b_{n-1}
   &=(\varepsilon-u)a_n+(1-\varepsilon+u)a_{n-1},
       \qquad n\ge1.
 \end{aligned}}                                      \tag{10}
\]

No divergent quantity has been separated: (10) keeps the pole and the
positive Jordan coefficients coupled.

## 3. Exact renewal form

Set

\[
 G_{n,c,\varepsilon}
 :=[z^n]{H_{c\varepsilon}(s_\varepsilon(z))-1
             \over c\varepsilon(1-z)}.              \tag{11}
\]

And let

\[
 S_u(x):=\sum_{m\le x}{J_u(m)\over m}.              \tag{12}
\]

Then

\[
 \boxed{
 \begin{aligned}
 G_{n,c,\varepsilon}
 &=\sum_{m\ge2}{J_u(m)\over u\,m^{1+\varepsilon}}
                    L_n(\log m)\\
 &\quad-\int_1^\infty x^{-1-\varepsilon}L_n(\log x)
                    S_u(x)\,dx,
 \qquad u=c\varepsilon.
 \end{aligned}}                                      \tag{13}
\]

*Proof.* From (7),

\[
 {H_u(s)-1\over u}={A_u(s)-1\over u}-{A_u(s)\over s-1}. \tag{14}
\]

The first term produces the sum in (13) via (6). For the second, Abel
summation gives, absolutely in the half-plane used,

\[
 {A_u(s)\over s-1}
 =\int_1^\infty x^{-s}S_u(x)\,dx.                   \tag{15}
\]

Applying the same Laguerre generating function within (15) proves (13).
\(\square\)

Formula (13) displays the problem with no estimates: it is the difference
of two positive measures, but both are tested against the signed polynomial
\(L_n\). The positivity of \(J_u\) does not decide the sign.

## 4. The correlated limit is independent of \(c\)

For each fixed \(n\ge1\), analyticity of \(F\) at \(s=1\) and (2) give

\[
 \lim_{\varepsilon\downarrow0}G_{n,c,\varepsilon}
 =[z^n]{-F'(1+z/(1-z))/F(1+z/(1-z))\over1-z}.       \tag{16}
\]

The exact identity of `103_59`/`104_16` identifies this coefficient as

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}G_{n,c,\varepsilon}
 =C_n:=\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime},} \tag{17}
\]

independently of \(c\in(0,1)\). In particular, keeping the finite shift
creates no new margin: removing the regulator returns exactly the earlier
gate.

## 5. The real order does not control the Cayley coefficients

Alzer–Kwong, Corollary 4.1, proves that

\[
 {(s-1)\zeta(s)\over s^\alpha}
 \quad\hbox{is strictly increasing on }(1,\infty)
 \quad\Longleftrightarrow\quad \alpha\le\gamma.
\]

The choice \(\alpha=0\) implies that \(F\) is strictly increasing.
Hence, for \(0\le r<1\),

\[
 0<H_{c\varepsilon}(s_\varepsilon(r))<1.            \tag{18}
\]

However, `104_16` certifies exactly

\[
 C_6\in
 [0.008107486973374973910460,
  0.008107486973374973910461].                       \tag{19}
\]

By (17), for each fixed \(c\in(0,1)\), \(G_{6,c,\varepsilon}>0\) holds for
every sufficiently small \(\varepsilon>0\), even though the function in (11)
is negative on the real ray. So radial order (18) does not imply
coefficient-by-coefficient order after the Cayley pullback.

Reference: H. Alzer and M. K. Kwong, *Some inequalities for the Riemann
zeta function*, Rend. Istit. Mat. Univ. Trieste 53 (2021),
[official PDF](https://rendiconti.dmi.units.it/volumi/53/005.pdf).

## 6. The variable \(c\) is not completely monotone either

At the center \(z=0\), define

\[
 h_\varepsilon(c)
 :=H_{c\varepsilon}(1+\varepsilon)
 ={F(1+(1-c)\varepsilon)\over F(1+\varepsilon)}.    \tag{20}
\]

Then

\[
 h_\varepsilon'''(c)
 =-\varepsilon^3{F'''(1+(1-c)\varepsilon)
                    \over F(1+\varepsilon)}.        \tag{21}
\]

With the convention

\[
 \zeta(1+t)={1\over t}+
     \sum_{k\ge0}{(-1)^k\gamma_k\over k!}t^k,
\]

one has \(F'''(1)=3\gamma_2<0\). The sign is not taken from an
approximation: `tools/jordan_cocycle_sign_gate.py` rationally certifies

\[
 -3\gamma_2\in
 [0.029071089578616955453591,
  0.029071089578616955453592].
\]

By continuity, there exists
\(\varepsilon_0>0\) such that \(h_\varepsilon'''(c)>0\) for
\(0<\varepsilon<\varepsilon_0\) and \(0\le c\le3/4\). Integrating three times,

\[
 \boxed{
 h_\varepsilon(3/4)-3h_\varepsilon(1/2)
 +3h_\varepsilon(1/4)-h_\varepsilon(0)>0.}          \tag{22}
\]

A Hausdorff/completely-monotone representation would require this third
difference to be \(\le0\). The failure occurs even before extracting
coefficients in \(z\).

## 7. No-go for identically canceling the explicit channel with finite shifts

Let \(c_1,\ldots,c_M>0\) be distinct and \(w_1,\ldots,w_M\) constants.
In a linear combination of (7) with **constant weights**, identically
canceling the explicit channel proportional to \((s-1)^{-1}\) would require

\[
 \sum_{j=1}^M w_jc_jA_{c_j\varepsilon}(s)=0.        \tag{23}
\]

Multiplying by \(\zeta(s)\),

\[
 \sum_{j=1}^M w_jc_j\zeta(s-c_j\varepsilon)=0.     \tag{24}
\]

Uniqueness of Dirichlet series turns (24) into
\(\sum_jw_jc_jm^{c_j\varepsilon}=0\) for every \(m\). Letting
\(m\to\infty\) successively eliminates the largest exponent and proves

\[
 w_1=\cdots=w_M=0.                                  \tag{25}
\]

This does not assert that \(H_u\) has a real pole at \(s=1\): the zero of
\(A_u\) cancels the apparent factor. It only asserts that no finite system
of constant weights erases that channel separately in identity (7).

For the normalized shifts \((H_{c_j\varepsilon}-1)/(c_j\varepsilon)\),
the same proof applies without the factor \(c_j\). In that normalized
family, canceling only the first order via \(\sum_jw_j=0\) does not help
either: by (17), it simultaneously cancels the target \(C_n\).

Within the class of finite products of the explicit factors
\((1-c_jx)\) with constant exponents, a multiplicative combination cannot
erase that channel either. If

\[
 \prod_{j=1}^M(1-c_jx)^{\alpha_j}\equiv1,           \tag{26}
\]

taking the logarithm of (26) gives
\(\sum_j\alpha_jc_j^k=0\) for every \(k\ge1\). The first \(M\)
equations form a Vandermonde system and force
\(\alpha_1=\cdots=\alpha_M=0\).

## 8. Off-line falsifier

Let

\[
 X_a(s)=\xi(s+a)\xi(s-a),\qquad 0<a<\tfrac12.       \tag{27}
\]

This function satisfies \(X_a(1-s)=X_a(s)\) and has zeros
\(1/2\pm a+i\gamma\), off the line of symmetry. Its pole–Euler component
is

\[
 F_a(s)=F(s+a)F(s-a),
\]

and the cocycle factors as

\[
 {F_a(s-u)\over F_a(s)}=H_u(s+a)H_u(s-a).           \tag{28}
\]

In the safe real half-plane, both factors satisfy order (18). The series of
the Euler quotients are products of series with non-negative Jordan
coefficients in \(\Re s>1+a+u\). Hence these local inputs are compatible
with zeros off the line. This example, by itself, does not transport
positivity up to the critical Cayley germ; the precise obstruction for such
a continuation rule is proved in `104_19` §7.

## 9. Verdict and successor

The correlated shift leaves four exact results:

1. the finite recurrence (10);
2. the coupled renewal (13);
3. the inevitable collapse to the signed cost (17);
4. the stop-gates (19), (22), (25)–(28).

The following inference is ruled out:

\[
 J_{c\varepsilon}\ge0
 +H_{c\varepsilon}<1\text{ on the real ray}
 \quad\Longrightarrow\quad
 C_n\text{ has the required sign.}              \tag{29}
\]

The minimal successor that additionally preserves the Gamma half of the
strong margin is the branch-free cocycle

\[
 \mathcal S_u(s)={Y(s-u)\over Y(s)}=H_u(s)^2K_u(s), \tag{30}
\]

with \(Y\) from `103_49`/`103_59`. This is not a new object: it is the
square of the half-cocycle of `104_16`. What remains to be audited is
whether its three finite channels

\[
 A_u(s)^2\left(1-{2u\over s-1}+{u^2\over(s-1)^2}\right)K_u(s) \tag{31}
\]

preserve a cancellation that is lost when taking the jet. That is the next
attack; (17) prevents counting it in advance as progress toward A1.
</content>
