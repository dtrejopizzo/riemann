# 104_19 — Branch-free cocycle: three-channel expansion and stop-gate

**Role.** Audit the successor of `104_18` that incorporates exactly the
Gamma budget of the strong margin. A finite expansion is obtained with
non-negative arithmetic coefficients and a positive Beta measure. The polar
factor, however, is a signed combination of three channels, and the limit is
exactly \(-\Delta D_n\), the gate of `103_59`.

**Verdict.** No new unconditional inequality is obtained. This document
proves neither A1 nor RH.

## 1. Internal duplication gate

The object is not new. `103_49`, `103_53`, and `103_59` already define

\[
 Y(s)={\xi(s)^2\over s\pi^{-s/2}\Gamma(s/2)}
 ={1\over4}s(s-1)^2\pi^{-s/2}\Gamma(s/2)\zeta(s)^2. \tag{1}
\]

`103_59` proves

\[
 \log{Y((1-z)^{-1})\over Y(1)}
 =\sum_{n\ge1}{D_n\over n}z^n,
 \qquad D_n=2\lambda_n-A_n,                         \tag{2}
\]

and

\[
 s{Y'(s)\over Y(s)}-D_1
 =\sum_{n\ge1}\Delta D_nz^n,\qquad s=(1-z)^{-1}.   \tag{3}
\]

Here \(\Delta D_n=D_{n+1}-D_n\).

The cocycle being tested is

\[
 \mathcal S_u(s):={Y(s-u)\over Y(s)}.               \tag{4}
\]

If \(H_u=F(s-u)/F(s)\), \(F=(s-1)\zeta(s)\), and

\[
 K_u(s):=\pi^{u/2}{\Gamma(1+(s-u)/2)\over\Gamma(1+s/2)}, \tag{5}
\]

then

\[
 \boxed{\mathcal S_u(s)=H_u(s)^2K_u(s).}            \tag{6}
\]

It is also the square of the half-cocycle
\(H_uK_u^{1/2}\) of `104_16` §7.2. The only new question is whether keeping
\(u=c\varepsilon\) finite preserves a three-channel cancellation that the
first jet hides.

## 2. The quadratic Euler channel is positive

For \(\Re s>1+u\),

\[
 A_u(s)={\zeta(s-u)\over\zeta(s)}
 =\sum_{m\ge1}{J_u(m)\over m^s},\qquad J_u(m)\ge0.  \tag{7}
\]

Set

\[
 b_u=J_u*J_u.
\]

Then

\[
 \boxed{A_u(s)^2=\sum_{m\ge1}{b_u(m)\over m^s},\qquad b_u(m)\ge0.} \tag{8}
\]

The function \(b_u\) is multiplicative. If \(q=p^u\) and \(k\ge1\),

\[
 \boxed{
 b_u(p^k)=2(q-1)q^{k-1}
 +(k-1)(q-1)^2q^{k-2}.}                            \tag{9}
\]

Indeed, \(J_u(p^0)=1\) and
\(J_u(p^j)=(q-1)q^{j-1}\) for \(j\ge1\). The two extremes of the
convolution give the first term of (9), and the \(k-1\) interior terms are
all \((q-1)^2q^{k-2}\).

## 3. The Gamma channel has a positive Beta measure

Form (5) and the Beta integral give

\[
 K_u(s)={\pi^{u/2}\over\Gamma(u/2)}
 \int_0^1v^{(s-u)/2}(1-v)^{u/2-1}\,dv.             \tag{10}
\]

Fix

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z},
 \qquad u=c\varepsilon,\qquad0<c<1,                 \tag{11}
\]

and define the positive measure

\[
 d\nu_{\varepsilon,u}(v)
 ={\pi^{u/2}\over\Gamma(u/2)}
 v^{(1+\varepsilon-u)/2}(1-v)^{u/2-1}\,dv.         \tag{12}
\]

The factor \(v^{z/[2(1-z)]}\) shifts the Laguerre argument by
\(-\frac12\log v\). No sign is lost in this channel.

## 4. Exact three-channel theorem

The polar part of \(H_u^2\) is

\[
 \left(1-{u\over s-1}\right)^2
 =1-{2u\over s-1}+{u^2\over(s-1)^2}.               \tag{13}
\]

Let

\[
 d\omega_0(y)=\delta_0(dy),\qquad
 d\omega_1(y)=e^{-\varepsilon y}\,dy,
 \qquad
 d\omega_2(y)=y e^{-\varepsilon y}\,dy,            \tag{14}
\]

and

\[
 \begin{aligned}
 T_{n,j}:={}&\sum_{m\ge1}{b_u(m)\over m^{1+\varepsilon}}
 \int_0^1\int_0^\infty
 L_n\!\left(\log m+y-\tfrac12\log v\right)\\
 &\hspace{42mm}d\omega_j(y)\,d\nu_{\varepsilon,u}(v).
 \end{aligned}                                      \tag{15}
\]

**Theorem.** For every \(n\ge0\),

\[
 \boxed{
 [z^n]{\mathcal S_u(s_\varepsilon(z))\over1-z}
 =T_{n,0}-2uT_{n,1}+u^2T_{n,2}.}                   \tag{16}
\]

*Proof.* The generating function

\[
 {e^{-xz/(1-z)}\over1-z}=\sum_{n\ge0}L_n(x)z^n    \tag{17}
\]

applied to (8) and (10) produces \(T_{n,0}\). Moreover,

\[
 {1\over\varepsilon+z/(1-z)}
 =\int_0^\infty e^{-\varepsilon y}
 e^{-yz/(1-z)}\,dy,                                 \tag{18}
\]

and the same identity with the square of the denominator inserts the factor
\(y\). Multiplying (17) by (18) shifts \(L_n(x)\) to \(L_n(x+y)\).
Combining the three terms of (13) proves (16). All the series and
integrals converge absolutely for \(u<\varepsilon\) and \(z\) in a
sufficiently small neighborhood of the origin. \(\square\)

Each \(T_{n,j}\) is built from positive measures, but \(L_n\) has a sign,
and so does the combination \(1,-2u,u^2\). The positivity of (8) and (12)
does not decide (16).

## 5. Exact limit: \(-\Delta D_n\) reappears

Define

\[
 {\mathcal S_{c\varepsilon}(s_\varepsilon(z))-1
   \over c\varepsilon(1-z)}
 =\sum_{n\ge0}g_{n,\varepsilon,c}z^n.              \tag{19}
\]

By (16),

\[
 \boxed{
 g_{n,\varepsilon,c}
 ={T_{n,0}-2uT_{n,1}+u^2T_{n,2}-1\over u}.}         \tag{20}
\]

Only the complete combination admits the limit. Since

\[
 {\mathcal S_u(s)-1\over u}\longrightarrow-{Y'(s)\over Y(s)},
\]

equations (2)–(3) give

\[
 \boxed{
 \begin{aligned}
  g_{0,\varepsilon,c}&\longrightarrow-D_1,\\
  g_{n,\varepsilon,c}&\longrightarrow-\Delta D_n,\qquad n\ge1.
 \end{aligned}}                                      \tag{21}
\]

The parameter \(c\) disappears. Proving
\(g_{n,\varepsilon,c}\le0\) uniformly as the regulator is removed would
prove \(\Delta D_n\ge0\), the strong gate sufficient for A1 already
recorded in `103_59`; it is not a weaker intermediate inequality.

## 6. Stop-gate: the polar square is not a positive mixture

Although (13) is non-negative for \(s>1+u\), its inverse Laplace
transform in \(t=s-1-\varepsilon\) is

\[
 d\mu_{\varepsilon,u}(y)
 =\delta_0(dy)-2u e^{-\varepsilon y}\,dy
     +u^2y e^{-\varepsilon y}\,dy.                 \tag{22}
\]

After \(u=c\varepsilon\) and \(r=\varepsilon y\),

\[
 \boxed{
 d\mu_c(r)=\delta_0(dr)+c(cr-2)e^{-r}\,dr.}         \tag{23}
\]

The continuous density of (23) is strictly negative on
\(0<r<2/c\) for **every** \(c>0\). Hence the real square is not a positive
Laplace mixture, and no value of \(c\) eliminates the signed channel.

The divergence that the combination must cancel already appears in the
Euler term \(m=1\), even omitting Gamma:

\[
 \boxed{
 [z]{1\over1-z}
 \left(1-{u\over\varepsilon+z/(1-z)}\right)^2
 =(1-c)^2+{2c(1-c)\over\varepsilon}.}               \tag{24}
\]

For \(0<c<1\), (24) diverges like \(\varepsilon^{-1}\). This persists
when Gamma is restored. Indeed, if

\[
 K_0:=K_u(1+\varepsilon),\qquad
 K_1:=[z]K_u(s_\varepsilon(z)),
\]

then \(K_0=1+O(\varepsilon)\) and \(K_1=O(\varepsilon)\), because

\[
 \partial_s\log K_u(s)
 ={1\over2}\left\{\psi(1+(s-u)/2)-\psi(1+s/2)\right\}=O(u).
\]

Hence the full coefficient of the \(m=1\) subchannel is

\[
 K_0\left((1-c)^2+{2c(1-c)\over\varepsilon}\right)
 +K_1(1-c)^2
 ={2c(1-c)\over\varepsilon}+O(1).                  \tag{24a}
\]

So separating \(m=1\) from \(m>1\) destroys precisely the cancellation
that makes (21) finite.

## 7. Global falsifier and the limit of its reach

Consider

\[
 X_a(s)=\xi(s+a)\xi(s-a),\qquad0<a<\tfrac12.        \tag{25}
\]

It satisfies \(X_a(1-s)=X_a(s)\) and has zeros
\(1/2\pm a+i\gamma\), off the line of symmetry. The product of its Euler
cocycles keeps non-negative Jordan coefficients in the half-plane of
absolute convergence; its Gamma quotients keep positive Beta
representations there.

Let \(Y_a(s)=Y(s+a)Y(s-a)\) and

\[
 \mathcal S_u^{(a)}(s)={Y_a(s-u)\over Y_a(s)}.       \tag{26}
\]

If \(0<\varepsilon<a\), a zero of \(Y_a\) with real part
\(1/2+a\) transforms via

\[
 z={s-1-\varepsilon\over s-\varepsilon}             \tag{27}
\]

into a point with \(|z|<1\). For every \(u\) outside a discrete set, the
numerator of (26) does not cancel it; the corresponding Taylor series has
radius \(R<1\).

Suppose the coefficients of

\[
 -{\mathcal S_u^{(a)}(s_\varepsilon(z))-1
       \over u(1-z)}                                 \tag{28}
\]

were eventually non-negative, as a structural deduction of the sign
\(g_n\le0\) would require. After subtracting a polynomial and dividing by a
power of \(z\), the Pringsheim theorem would force a singularity at the
positive real point \(z=R\). None exists: for \(0<z<1\),
\(s_\varepsilon(z)>1\) and the shifted completed factors are real,
positive, and nonzero. The real singularity at \(z=1\) does not help,
because \(R<1\). Applying the same argument to the negative of (28) also
excludes eventual non-positivity. Since the coefficients are real, there are
infinitely many positive and infinitely many negative ones.

**Exact reach.** The positive series of the shifted factor converges only
in a right half-plane, not throughout the whole disc of (27). Hence this
argument refutes a sign continuation based solely on "Jordan positive +
Beta positive + functional equation." It does not refute a new arithmetic
theorem that uses special quantitative information about the real weights
of \(\zeta\) within the critical zone. For a fixed
\(\varepsilon\), requiring holomorphy throughout that disc only excludes
zeros with \(\Re\rho>1/2+\varepsilon\). Requiring it for **every**
\(\varepsilon\downarrow0\), with generic \(u\) to avoid cancellations,
and using the functional symmetry, forces RH; global contractivity is an
even stronger input.

## 8. Already-existing theta stop-gate

The quadratic character does not rescue term-by-term positivity in the
theta representation either. `103_49` starts from the same \(Y\) and from
the positive coefficients of \(\zeta(s)^2\), but transferring the factor
\(s(s-1)^2\) to the density produces

\[
 2x(4x^2-16x+9)e^{-x},                              \tag{29}
\]

which is negative for

\[
 2-\frac{\sqrt7}{2}<x<2+\frac{\sqrt7}{2}.           \tag{30}
\]

So the branch-free packaging opens no positivity route that the repo would
have missed: (23) is the finite version of the same sign loss.

## 9. Operational verdict

The attack produces two reusable theorems: expansion (16) and limit
(21). It also proves three obstructions:

1. the polar measure is signed for every \(c>0\), equation (23);
2. separating channels creates \(\varepsilon^{-1}\)-order divergences,
   equation (24);
3. Jordan/Beta/functional equation do not force the Cayley sign, by (25)–(28).

Hence the immediate inference
"Jordan positive + positive Beta + real polar square" is ruled out as a
proof of A1. **Not** ruled out is the global cocycle: a coupled theorem
exploiting a new, exclusive quantitative property of \(J_u\), \(b_u\), or
\(\Lambda\) before splitting the three channels remains open. `104_20`
develops exactly that continuation and locates its global gate.

The verifier `tools/three_channel_cocycle_check.py` checks, with
`Fraction` arithmetic, formula (9), the transform (23), and the coefficient
(24). It does not verify A1.
</content>
