# 106.27 — Smooth radical truncations are operator quasimodes

## Purpose

The direct branch theorem of 106.25 does not require the quantitative
prolate scale \(d_8\). It only requires a normalized even vector \(q_L\)
such that

\[
 \|A_L^+q_L\|\longrightarrow0
 \tag{1}
\]

and a qualitative lower floor on \(q_L^\perp\). The sharply truncated
co-Poisson vector of 106.23 leaves (1) behind the open co-Poisson
graph-transfer problem: its exterior Fourier carrier has a nonzero endpoint
trace, and the additive \(H^1\) estimate of 106.24 does not control the
form-dual norm.

For the direct branch theorem that sharp truncation is unnecessary. This
note proves (1) unconditionally for a smooth truncation of Riemann's full
kernel. The scalar near-radical construction is already in 106.09. The new
point is the **operator** estimate, uniform against the whole \(L^2\) unit
ball.

## 1. Setup

Put

\[
 a=\frac L2,\qquad \lambda=e^a,\qquad I_L=[-a,a].
 \tag{2}
\]

Let \(K\) be Riemann's full additive kernel, normalized by

\[
 \widehat K(z)=\Xi(z),\qquad K(-x)=K(x).
 \tag{3}
\]

Choose smooth even cutoffs \(\chi_a\) such that

\[
 0\leq\chi_a\leq1,\qquad
 \chi_a=1\ \hbox{on }[-a+1,a-1],\qquad
 \mathrm{supp}\,\chi_a\subset(-a,a),
 \tag{4}
\]

and, for each fixed \(r\),

\[
 \sup_{a\ge2}\|\chi_a^{(r)}\|_\infty<\infty.
 \tag{5}
\]

Define

\[
 v_L=\chi_aK,\qquad
 e_L=v_L-K=(\chi_a-1)K,\qquad
 q_L^K=\frac{v_L}{\|v_L\|_2}.
 \tag{6}
\]

The vector \(v_L\) is even and belongs to the smooth core of the semilocal
Weil operator \(A_L^+\).

For a nontrivial zero \(\rho=\beta+i\gamma\), use

\[
 z_\rho=\gamma-i\left(\beta-\frac12\right),\qquad
 \frac12+iz_\rho=\rho.
 \tag{7}
\]

Unconditionally,

\[
 |\mathrm{Im}\,z_\rho|<\frac12.
 \tag{8}
\]

## 2. Uniform decay of the exterior transform

The theta-series formula and modular symmetry give, for each fixed
\(r\ge0\), constants \(C_r,M_r,c_r>0\) such that

\[
 |K^{(r)}(x)|
 \leq C_re^{M_r|x|}e^{-c_re^{2|x|}}.
 \tag{9}
\]

This is 106.09(15).

### Lemma 1 — Strip-uniform transform decay

For every integer \(r\ge0\), there are constants \(C_r,M_r,c_r>0\) such
that

\[
 \boxed{
 \sup_{|\eta|\le1/2}
 |\widehat e_L(t+i\eta)|
 \leq
 C_r\lambda^{M_r}e^{-c_r\lambda^2}(1+|t|)^{-r}.}
 \tag{10}
\]

#### Proof

The support of \(e_L\) is contained in \(\{|x|\ge a-1\}\). Equations
(4)--(5), Leibniz's rule, and (9) give

\[
 \int_{\mathbb R}e^{|x|/2}|e_L^{(r)}(x)|\,dx
 \leq C_r\lambda^{M_r}e^{-c_r\lambda^2}.
 \tag{11}
\]

For \(|t|\ge1\), integrate the Fourier transform \(r\) times by parts.
There are no boundary terms, and for \(|\eta|\le1/2\),

\[
 |\widehat e_L(t+i\eta)|
 \leq |t+i\eta|^{-r}
 \int_{\mathbb R}e^{\eta x}|e_L^{(r)}(x)|\,dx.
 \tag{12}
\]

Equation (11) bounds the last integral. The range \(|t|<1\) follows from
the same estimate with \(r=0\), after changing the constants.
\(\square\)

## 3. From divisor decay to an operator residual

The polarized zero-side form is

\[
 QW(f,g)
 =\sum_\rho
   \overline{\widehat f(\overline{z_\rho})}
   \widehat g(z_\rho),
 \tag{13}
\]

with multiplicities and the symmetry-complete divisor convention.

For \(g\in L^2(I_L)\), Cauchy--Schwarz and (8) give

\[
\begin{aligned}
 |\widehat g(z_\rho)|
 &\leq \|g\|_2
 \left(\int_{-a}^{a}
 e^{2\mathrm{Im}(z_\rho)x}\,dx\right)^{1/2}\\
 &\leq (L\lambda)^{1/2}\|g\|_2.
\end{aligned}
 \tag{14}
\]

The unconditional local Riemann--von Mangoldt estimate, including
multiplicities, is

\[
 N(T+1)-N(T)=O(\log(3+T)).
 \tag{15}
\]

Hence, for every fixed \(r>1\),

\[
 \sum_\rho(1+|\gamma|)^{-r}<\infty.
 \tag{16}
\]

### Theorem 2 — Operator quasimode estimate

There are constants \(C,M,c>0\) such that

\[
 \boxed{
 \|A_L^+v_L\|_2
 \leq C\sqrt{L\lambda}\,\lambda^Me^{-c\lambda^2}.}
 \tag{17}
\]

Consequently,

\[
 \boxed{\|A_L^+q_L^K\|_2\longrightarrow0.}
 \tag{18}
\]

#### Proof

Since \(\widehat K=\Xi\), the full kernel lies in the polarized Weil
radical:

\[
 QW(K,g)=0
 \tag{19}
\]

for every smooth admissible \(g\). Since \(v_L=K+e_L\),

\[
 QW(v_L,g)=QW(e_L,g).
 \tag{20}
\]

Take \(r>1\) in Lemma 1. Equations (10), (13)--(16) give, for every
smooth \(g\) supported in \(I_L\),

\[
\begin{aligned}
 |QW(v_L,g)|
 &\leq
 C_r\lambda^{M_r}e^{-c_r\lambda^2}
 \sqrt{L\lambda}\,\|g\|_2
 \sum_\rho(1+|\gamma|)^{-r}\\
 &\leq
 C\sqrt{L\lambda}\,\lambda^Me^{-c\lambda^2}\|g\|_2.
\end{aligned}
 \tag{21}
\]

The divisor series in (21) is absolutely convergent. Thus (20) extends to
a bounded \(L^2(I_L)\) functional. On the smooth core the global form
equals the semilocal form because both arguments are supported in \(I_L\).
Its Riesz representative is \(A_L^+v_L\), proving (17).

Finally, \(v_L\to K\) in \(L^2(\mathbb R)\), so

\[
 \|v_L\|_2\longrightarrow\|K\|_2>0.
 \tag{22}
\]

Divide (17) by \(\|v_L\|_2\).
\(\square\)

### Corollary 3 — Both residual components vanish

Writing

\[
 A_L^+q_L^K
 =\mathscr R_L^Kq_L^K+b_L^K,\qquad b_L^K\perp q_L^K,
 \tag{23}
\]

one has

\[
 \boxed{
 |\mathscr R_L^K|+\|b_L^K\|\longrightarrow0.}
 \tag{24}
\]

## 4. The direct RH gate after the residual theorem

Define

\[
 \beta_{L,K}^+
 :=\inf_{\substack{g\perp q_L^K\\g\ {\rm even}\\\|g\|_2=1}}
 \langle A_L^+g,g\rangle.
 \tag{25}
\]

The abstract proof of 106.25, Theorem 1, does not use a special property
of the moving prolate vector.

### Corollary 4 — Residual-complete branch reduction

If

\[
 \boxed{\beta_{L,K}^+\ge-o(1),}
 \tag{26}
\]

then RH holds.

Indeed, if RH fails, 106.11 supplies a fixed \(c_+>0\) with

\[
 \inf\sigma(A_L^+)\le-c_+
\]

for every sufficiently large \(L\). Equations (18) and (26) contradict
106.25, Theorem 1.

Thus the operator-residual half of the relaxed branch gate is proved
unconditionally. The only remaining statement in this coordinate is the
literal-prime complementary inertia estimate (26).

## 5. Relation to the moving PSWF vector

Theorem 2 deliberately does not claim

\[
 \|A_L^+q_L^+\|\to0
 \tag{27}
\]

for the sharply truncated moving PSWF vector of 106.23. That vector has a
nonzero endpoint trace. Its exterior Fourier continuation therefore has
the \(t^{-1}\) carrier proved in 106.24(39)--(41), and the integration by
parts used in Lemma 1 does not acquire arbitrarily many powers of
\((1+|t|)^{-1}\). The additive \(H^1\) result cannot repair this: 106.26
gives an explicit bounded-\(H^1\) counterexample to the required
co-Poisson Mellin continuity.

The smooth kernel vector avoids that graph-transfer problem without
weakening the direct negative-branch contradiction. It is not a substitute
for the stronger weighted-curvature comparison, where the precise prolate
levels \(d_4,d_8\) are essential.

## 6. Semantic audit and status

The closest predecessors are:

- 106.09, which proves only the finite scalar Weil matrix bound for the
  vectors \(\chi_aK_j\);
- 106.10, which records that the \(C^0\) Meixner estimate does not imply an
  operator residual for the hard CCM model;
- 106.12--106.15, which identify the moving-vector form-dual residual;
- E101.053 and 106.24, which give additive endpoint and \(H^1\) data but no
  co-Poisson graph transfer;
- 106.25, which proves that a vanishing full residual plus a qualitative
  complementary floor is sufficient for the direct RH contradiction.

No audited predecessor upgrades the smooth near-radical matrix of 106.09
to the operator estimate (17). The upgrade works because the smooth cutoff
makes the exterior transform rapidly decreasing, so the zero-side
functional is absolutely summable uniformly against the full \(L^2\) unit
ball.

\[
\begin{array}{c|c}
\text{statement}&\text{status}\\ \hline
\|A_L^+q_L^K\|\to0&\text{proved unconditionally}\\
\beta_{L,K}^+\ge-o(1)&\text{open literal-prime inertia theorem}\\
\text{RH}&\text{follows from the second line by 106.11 and 106.25.}
\end{array}
\tag{28}
\]

No statement in this note proves (26) or RH.
