# 104_89 — One-sided BSY gate for real Euler truncations

**Result.** The zero-free global truncations of `104_85`,
normalized at \(s=1\), have exactly zero Poisson logarithmic mean. The
limit function

\[
 H(s)=(s-1)\zeta(s),\qquad H(1)=1,                       \tag{1}
\]

has mean

\[
 D_B=-\log|B(0)|
 =\sum_{\Re\rho>1/2}m_\rho
      \log { |\rho|\over|1-\rho|}\ge0.                  \tag{2}
\]

Therefore, for **every** truncation \(X\),

\[
 \boxed{
 D_B\le
 \int_{\mathbb R}
 \left(
  \log|H(\tfrac12+it)|
  -\log|\widehat F_X(\tfrac12+it)|
 \right)_+
 {dt\over2\pi(t^2+1/4)}.}                               \tag{3}
\]

Consequently, it suffices to construct a sequence \(X_j\to\infty\) for
which the right-hand side of (3) tends to zero. This is a direct,
one-sided target, written only with the real zeta function and
truncations of its weights \(\Lambda(m)\); it would imply \(D_B=0\) and,
therefore, RH.

Pointwise convergence, almost-everywhere convergence, or convergence in
measure of the logarithms is not enough. There is an explicit family of
zero-free, normalized functions whose means are zero and whose
log-moduli converge almost everywhere to the modulus of a function with
an interior zero. The whole difference (2) escapes into a Poisson well
of decreasing measure and increasing depth at the point at infinity of
the critical line.

Moreover, a pole, a functional equation, and an Euler channel supported
on ordinary prime powers with strictly positive Mangoldt weights also do
not force (3). The family

\[
 Z_a(s)=C_a{(s-1)^2-a^2\over s-1}\zeta(s-a)\zeta(s+a),
 \qquad0<a<{1\over2},                                   \tag{4}
\]

has these properties, with weights

\[
 \Lambda(n)(n^a+n^{-a})>0,                              \tag{5}
\]

and has zeros off the line. It does not preserve the exact weights
\(\Lambda(n)\); by the uniqueness theorem of `104_88`, preserving them
literally would pin down \(\zeta\) itself.

This document does not prove (3), Deep-\(\Lambda\), or RH. It
identifies the minimal one-sided bound for this attack and shows, by an
exact falsifier, why it does not follow from Fatou's lemma,
subharmonicity, Euler positivity, or interior convergence.

---

## 1. Global normalization with zero mean

Let \(F_X\) be the zero-free function of `104_85`. Dividing by its value
at one gives

\[
 \widehat F_X(s)={F_X(s)\over F_X(1)}=\exp L_X(s),       \tag{6}
\]

\[
 L_X(s)=
 \sum_{m\le X}{\Lambda(m)\over\log m}(m^{-s}-m^{-1})
 +\int_1^X{x^{-1}-x^{-s}\over\log x}\,dx.              \tag{7}
\]

The apparent singularity of the integrand at \(x=1\) is removable.
Hence \(L_X\) is entire, \(\widehat F_X\) is entire and zero-free, and
\(\widehat F_X(1)=1\).

Set

\[
 d\nu(t)={dt\over2\pi(t^2+1/4)}.                        \tag{8}
\]

This is a probability measure and its characteristic function is

\[
 \int_{\mathbb R}e^{ity}\,d\nu(t)=e^{-|y|/2}.          \tag{9}
\]

On the critical line, \(u_X(t)=\log|\widehat F_X(1/2+it)|\)
equals

\[
\begin{aligned}
 u_X(t)={}&
 \sum_{m\le X}{\Lambda(m)\over\log m}
 \{m^{-1/2}\cos(t\log m)-m^{-1}\}\\
 &+\int_0^{\log X}
 {1-e^{y/2}\cos(ty)\over y}\,dy.                       \tag{10}
\end{aligned}
\]

Equation (9) separately annihilates the mean of each bracket and each
integrand:

\[
 \int m^{-1/2}\cos(t\log m)d\nu(t)=m^{-1},
 \qquad
 \int e^{y/2}\cos(ty)d\nu(t)=1.                        \tag{11}
\]

The sums and integrals are finite, so Fubini poses no issue. Thus

\[
 \boxed{\int_{\mathbb R}u_X(t)d\nu(t)=0\quad(X<\infty).} \tag{12}
\]

This is also the Poisson formula for \(\log|\widehat F_X|\), seen from
\(s=1\), but (10)--(11) check directly that no mass was skipped at
infinity in each truncation.

## 2. The exact defect of the limit function

Use the map from the disk to the half-plane

\[
 s={1\over1-z}.                                         \tag{13}
\]

The center \(z=0\) corresponds to \(s=1\), the circle to
\(s=1/2+it\), and the angular measure transforms exactly into (8).
The zeros of \(H\) with \(\Re\rho>1/2\) transform into

\[
 w_\rho={\rho-1\over\rho},\qquad |w_\rho|<1.            \tag{14}
\]

Poisson--Jensen gives

\[
 \boxed{
 \int_{\mathbb R}\log|H(\tfrac12+it)|d\nu(t)
 =\sum_{\Re\rho>1/2}m_\rho\log{1\over|w_\rho|}
 =D_B.}                                                  \tag{15}
\]

The factor \(s-1\) has zero logarithmic mean, so (15) is the normalized
form of the Balazard--Saias--Yor criterion. The polynomial growth of
zeta removes an additional singular factor.

Subtracting (12) from (15),

\[
 \int(u-u_X)d\nu=D_B,
 \qquad u(t)=\log|H(1/2+it)|.                            \tag{16}
\]

Since \(f\le f_+\), (16) implies (3). It also gives

\[
 \|u-u_X\|_{L^1(\nu)}\ge D_B.                           \tag{17}
\]

There is an even more precise bookkeeping. If

\[
 I_X=\int (u-u_X)_+d\nu,
 \qquad J_X=\int (u_X-u)_+d\nu,                          \tag{17a}
\]

then (16) is exactly equivalent to

\[
 \boxed{I_X=D_B+J_X.}                                    \tag{17b}
\]

In particular, the target \(I_{X_j}\to0\) simultaneously requires
\(D_B=0\) and \(J_{X_j}\to0\). It is a sufficient condition for RH, but
it is not claimed here that RH alone forces that convergence for this
concrete family of truncations. That direction also needs a boundary
tightness proof.

Hence either of the two conditions

\[
 \|u-u_{X_j}\|_1\longrightarrow0,
 \qquad\hbox{or only}\qquad
 \|(u-u_{X_j})_+\|_1\longrightarrow0                   \tag{18}
\]

implies RH. The second is strictly the natural one-sided requirement;
controlling \((u_X-u)_+\) goes in the wrong direction.

### 2.1 The target is no stronger than RH if a subsequence is allowed

For real cutoffs \(X\ge2\), define

\[
 J(x)=\sum_{2\le m\le x}{\Lambda(m)\over\log m},
 \qquad
 L_2(x)=\int_2^x{dt\over\log t},
 \qquad A(x)=J(x)-L_2(x).                               \tag{18a}
\]

Then

\[
 \boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
 \exists X_j\to\infty:\ 
 \|u-u_{X_j}\|_{L^1(\nu)}\to0.}                         \tag{18b}
\]

The right-to-left implication is already (17). For the converse, under
RH the quadratic Cramér bound gives

\[
 \int_2^\infty {A(x)^2\over x^2}\,dx<\infty.            \tag{18c}
\]

Indeed, exact partial summation

\[
 A(x)={\psi(x)-x\over\log x}
 +\int_2^x{\psi(t)-t\over t\log^2t}\,dt+{2\over\log2}   \tag{18d}
\]

and \(\int_Y^{2Y}|\psi(t)-t|^2dt\ll Y^2\) under RH make the first term
summable in dyadic blocks; Cauchy--Schwarz gives
\[
 \int_2^x{\psi(t)-t\over t\log^2t}\,dt
 =O(\sqrt x/\log^2x),
\]
which handles the second.

The finite energy (18c) allows choosing a non-atomic sequence with
\[
 {A(X_j)^2\over X_j}\longrightarrow0.                  \tag{18e}
\]

For \(s=1/2+it\), integration by parts in the tail gives

\[
\begin{aligned}
 \log H(s)-L_X(s)
 ={}&-(X^{-s}-X^{-1})A(X)\\
 &+s\int_X^\infty A(x)x^{-s-1}dx
 -\int_X^\infty A(x)x^{-2}dx.                          \tag{18f}
\end{aligned}
\]

Mellin--Plancherel and the choice of \(\nu\) produce the identities

\[
\begin{aligned}
 \int\left|s\int_X^\infty A(x)x^{-s-1}dx\right|^2d\nu
 &=\int_X^\infty{A(x)^2\over x^2}dx,\\
 \int|X^{-s}-X^{-1}|^2d\nu&=X^{-1}-X^{-2}.             \tag{18g}
\end{aligned}
\]

The last term of (18f) tends to zero by Cauchy--Schwarz. Equations
(18c), (18e), and (18g) give \(L^2(\nu)\) convergence, and hence
\(L^1(\nu)\) convergence, of the real parts. This proves (18b).

The equivalence uses, in the RH \(\Rightarrow\) direction, the
conditional Cramér estimate; it is not progress toward an unconditional
proof. Its role here is to show that the one-sided gate with a
subsequence has exactly the right strength. Phases 49 and 101 already
contain equivalent Cramér energy criteria; no new equivalence is
claimed here, only its translation into the concrete hard truncations
of (7).

## 3. Mass escape at the point at infinity

Let \(b_a\) be an elementary Blaschke factor with \(0<|a|<1\),
normalized by \(b_a(0)=|a|\), and set

\[
 H_a(z)={b_a(z)\over|a|},
 \qquad D=-\log|a|>0.                                   \tag{19}
\]

Then \(H_a(0)=1\), it has an interior zero, and

\[
 \log|H_a(e^{i\theta})|=D                              \tag{20}
\]

almost everywhere. For \(0<r<1\), define

\[
 F_r(z)=\exp\left\{
 D\left[1-{1+rz\over1-rz}\right]\right\}.             \tag{21}
\]

Each \(F_r\) is zero-free and \(F_r(0)=1\). On the boundary,

\[
 \log|F_r(e^{i\theta})|
 =D\{1-P_r(\theta)\},
 \qquad
 P_r(\theta)={1-r^2\over|1-re^{i\theta}|^2}.           \tag{22}
\]

Since \(\int P_r\,d\theta/(2\pi)=1\), each mean in (22) is zero.
But \(P_r(\theta)\to0\) for every \(\theta\ne0\), so the log-moduli
converge almost everywhere and in measure to (20), whose mean is
\(D\). Moreover,

\[
 \int|D-\log|F_r||{d\theta\over2\pi}
 =D\int P_r{d\theta\over2\pi}=D.                       \tag{23}
\]

All the lost mass lives in the negative well \(-DP_r\), concentrated at
\(z=1\), which under (13) is \(|t|=\infty\). This falsifies any step
based solely on almost-everywhere convergence, convergence in measure,
Fatou's lemma, or subharmonicity.

Seen from the quotient \(Q_r=H_a/F_r\), one has exactly

\[
 \log|Q_r(e^{i\theta})|=DP_r(\theta)\ge0,
 \qquad I_r=D,\quad J_r=0.                              \tag{23a}
\]

Thus the falsifier saturates (17b): the full interior defect
reappears in the positive part even though the quotient tends to one
almost everywhere.

The falsifier can be made locally invisible inside the disk:

\[
 S_{r,n}(z)=\exp\left\{
 D\left[1-{1+rz^n\over1-rz^n}\right]\right\}.          \tag{24}
\]

If \(n\to\infty\), then \(S_{r,n}\to1\) uniformly on every compact
subset of the disk. Choosing simultaneously \(r=r_n\uparrow1\) with
\(\sum_n\sqrt{1-r_n}<\infty\), Borel--Cantelli gives

\[
 \log|S_{r_n,n}(e^{i\theta})|\longrightarrow D          \tag{25}
\]

for almost every \(\theta\), while each mean remains zero. Therefore
not even local interior convergence plus almost-everywhere boundary
convergence provides the integrable uniformity of (18).

The defect can survive even when the limit is also zero-free. Set

\[
 C_r(w)={1+rw\over1-rw},
 \qquad
 G_{r,n}(z)=\exp\{D[C_r(z^n)-C_{-r}(z^n)]\}.             \tag{25a}
\]

Then \(G_{r,n}(0)=1\), it has no zeros, and its boundary log-modulus is

\[
 \log|G_{r,n}(e^{i\theta})|
 =D\{P_r(n\theta)-P_{-r}(n\theta)\},                    \tag{25b}
\]

with zero mean. If \(n\to\infty\) and \(r=r_n\uparrow1\) with
\(\sum_n\sqrt{1-r_n}<\infty\), then \(G_{r_n,n}\to1\)
uniformly on compacts and (25b) tends to zero almost everywhere.
However, since the sign of \(P_r-P_{-r}\) is the sign of
\(\cos\theta\),

\[
 \int(P_r-P_{-r})_+{d\theta\over2\pi}
 ={4\over\pi}\arctan{1+r\over1-r}-1\longrightarrow1.  \tag{25c}
\]

Therefore

\[
 \int\log^+|G_{r_n,n}|{d\theta\over2\pi}\longrightarrow D. \tag{25d}
\]

This balanced falsifier proves that not even "zero interior defect +
zero-free limit + local and boundary convergence" alone forces
\(J_X\to0\) in (17b). For the real Euler truncations that convergence
might still hold, but it would be an additional arithmetic theorem and
not a general functional principle.

## 4. Falsifier with ordinary prime support

Fix \(0<a<1/2\) and choose \(C_a\) so that (4) has residue one at
\(s=1\). The poles of \(\zeta(s-a)\) and \(\zeta(s+a)\), located at
\(1+a\) and \(1-a\), are cancelled by \((s-1)^2-a^2\). Only the
explicit pole at \(s=1\) remains.

The completed function is

\[
 \Xi_a(s)={1\over4C_a}(s^2-a^2)(s-1)\pi^{-s}
 \Gamma\!\left({s-a\over2}\right)
 \Gamma\!\left({s+a\over2}\right) Z_a(s)
 =\xi(s-a)\xi(s+a),                                    \tag{26}
\]

and it satisfies \(\Xi_a(s)=\Xi_a(1-s)\). For \(\Re s>1+a\), its Euler
channel is

\[
 -{d\over ds}\log\{\zeta(s-a)\zeta(s+a)\}
 =\sum_{n\ge2}{\Lambda(n)(n^a+n^{-a})\over n^s}.       \tag{27}
\]

The coefficients of the Euler channel are strictly positive and live
on ordinary prime powers; the rational factor of (4) belongs to the
completion block, not to that channel. Since there are infinitely many
zeros \(\rho=1/2+i\gamma\) of \(\zeta\), (26) has zeros

\[
 \rho+a,\qquad\rho-a,                                   \tag{28}
\]

off the line. Therefore positivity, support, pole, and functional
equation do not control (3). What (27) alters is exactly the height of
each jump: \(n^a+n^{-a}\) replaces the unit weight of the zeta
channel.

## 5. The exact towers also carry no one-sided sign

The full contribution of an ordinary prime tower, before combining it
with the other towers and with the continuous comparator, is

\[
 \begin{aligned}
 \tau_p(t)
 &=\sum_{k\ge1}{p^{-k/2}\cos(kt\log p)-p^{-k}\over k}\\
 &=\log{1-p^{-1}\over|1-p^{-1/2-it}|}.                  \tag{29}
 \end{aligned}
\]

The image of \(t\log p\) modulo \(2\pi\) under \(\nu\) has
wrapped-Cauchy density \(P_r(\theta)d\theta/(2\pi)\),
\(r=p^{-1/2}\), because its moments are \(r^{|k|}\). From this,

\[
 \int\tau_p\,d\nu=0,
 \qquad
 \tau_p(0)=\log(1+p^{-1/2})>0,
 \qquad
 \tau_p(\pi/\log p)=\log(1-p^{-1/2})<0.                \tag{30}
\]

More quantitatively, for \(p\ge5\), on the central third of the circle
one has \(P_r\ge1/3\) and \(-\tau_p\ge r/4\). By the zero mean,

\[
 \boxed{
 \int(\tau_p)_+d\nu
 =\int(-\tau_p)_+d\nu
 \ge {1\over36\sqrt p}.}                                \tag{31}
\]

Consequently, summing the positive costs tower by tower up to \(P\)
loses at least \(\gg\sqrt P/\log P\). The exact relation
\(\Lambda(p^k)=\log p\) provides no local sign; any proof of (18) must
preserve the global cancellation between towers and the comparator.

The dual form exhibits the same requirement. For \(f=u-u_X\),

\[
 \int f_+d\nu
 =\sup_{0\le\varphi\le1}\int\varphi f\,d\nu.            \tag{32}
\]

If

\[
 c_\varphi=\int\varphi d\nu,
 \qquad
 K_\varphi(y)=\Re\int\varphi(t)e^{ity}d\nu(t),          \tag{33}
\]

then (10) gives exactly

\[
\begin{aligned}
 \int\varphi u_Xd\nu={}&
 \sum_{m\le X}{\Lambda(m)\over\log m}
 \{m^{-1/2}K_\varphi(\log m)-m^{-1}c_\varphi\}\\
 &+\int_0^{\log X}{c_\varphi-e^{y/2}K_\varphi(y)\over y}\,dy. \tag{34}
\end{aligned}
\]

For \(\varphi=1\), (9) makes each bracket zero: that is (12). For the
optimal selector \(\varphi=\mathbf1_{\{u>u_X\}}\), both \(K_\varphi\)
and \(e^{-|y|/2}-K_\varphi\) are positive definite, but have no scalar
sign. The gap is, therefore, a uniform inequality over these
submeasures correlated with zeta itself, not another mean identity.

## 6. Cauchy energy and the limit of PNT bounds

Measure (8) has the exact kernel

\[
 \int u^{-1/2-it}v^{-1/2+it}d\nu(t)
 ={1\over\max(u,v)}.                                    \tag{35}
\]

For a truncated signed measure \(d\sigma\), with
\(V(y)=\sigma([1,y])\), it follows that

\[
 \boxed{
 \int\left|\int u^{-1/2-it}d\sigma(u)\right|^2d\nu(t)
 =\int_1^\infty{|V(y)|^2\over y^2}\,dy.}               \tag{36}
\]

Taking \(d\sigma=\mathbf1_{[1,X]}(d\psi-dx)\), the right-hand side is

\[
 \int_1^X{(\psi(y)-y+1)^2\over y^2}\,dy
 +{(\psi(X)-X+1)^2\over X}.                            \tag{37}
\]

The unconditional lower bound on prime energy recorded in `103_71`
implies that (31) grows at least like \(c\log X\). In particular, this
family of logarithmic derivatives is not even bounded in \(L^2(\nu)\),
even in the RH scenario. Passing from them to logarithms smooths out a
power of \(\log x\), but Vinogradov--Korobov still does not give the
boundary bound (18). The one-sided inequality is not obtained by
lifting the interior convergence topology of `104_85` to a crude
quadratic bound.

## 7. Exact status

It has been proved that:

\[
 \text{one-sided bound (18)}\Longrightarrow D_B=0
 \Longleftrightarrow \mathrm{RH}.                       \tag{38}
\]

It has also been proved that none of the following properties imply
(18): zero-freeness of each approximant, normalization at \(s=1\),
interior convergence, almost-everywhere or in-measure boundary
convergence, positivity of the Euler channel, support of that channel
on prime powers, a single pole, and functional equation. The input
still not proved must specifically prevent the negative mass escape of
(22) for the exact heights \(\Lambda(m)\).

## 8. Reproduction

From the tools directory:

    python3 bsy_one_sided_euler_boundary_check.py

The checker confirms the closed positive mass of the balanced spike and
the zero mean with costs of both signs from the prime towers. These
are numerical checks of identities already proved above, not
certificates of (18).
