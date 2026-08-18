# 106.34 — Dyadic Bessel closure of the cross residual

## Purpose

Document 106.33 proves, for the endpoint-corrected moving source,

\[
 |A_\lambda(w)|
 \ll \frac{\lambda^{7/2}\sqrt{d_4}}
 {1+|\mathrm{Im}\,w|},
 \qquad |\mathrm{Re}\,w|<\frac12.
 \tag{1}
\]

That estimate was used there only quadratically, to prove

\[
 |\mathscr R_L^+|\ll\lambda^7d_4.
 \tag{2}
\]

The present note uses the same carrier linearly.  A dyadic Bessel bound for
the complex exponentials attached to the zeta divisor gives

\[
 \boxed{
 \|b_L^+\|
 \ll \lambda^4\sqrt{(1+L)d_4}.}
 \tag{3}
\]

In particular,

\[
 \boxed{\|b_L^+\|\longrightarrow0.}
 \tag{4}
\]

This closes the cross residual needed by the direct asymptotic-inertia
criterion of 106.25.  It does not prove the stronger weighted-curvature
budget

\[
 \|b_L^+\|=O(\lambda^{p_b}d_4),\qquad p_b\le\frac{15}{2}.
 \tag{5}
\]

The distinction is decisive: (5) is exponentially stronger than (3), but
it is unnecessary for the direct RH implication once the complementary
floor is nonnegative.

## 1. The exact cross functional

Use the endpoint-corrected source and notation of 106.33.  Thus

\[
 q_L^+=\frac{V_\lambda^+}{\|V_\lambda^+\|},
 \qquad
 e_L^+=\frac{R_\lambda^+}{\|V_\lambda^+\|},
 \qquad
 \|V_\lambda^+\|\ge c_V>0.
 \tag{6}
\]

The moving-radical identity gives, for every even semilocal core vector
\(g\perp q_L^+\),

\[
 \langle b_L^+,g\rangle
 =QW_\lambda(q_L^+,g)
 =-QW(e_L^+,g).
 \tag{7}
\]

Write every nontrivial zero as

\[
 \rho=\beta+i\gamma,
 \qquad
 x_\rho=\rho-\frac12.
 \tag{8}
\]

The exact positive-parity coordinate of 106.26 is

\[
 \widehat {R_\lambda^+}(z_\rho)
 =b_\lambda(x_\rho),
 \qquad
 b_\lambda(w)=\frac{A_\lambda(w)+A_\lambda(-w)}{\sqrt2}.
 \tag{9}
\]

Consequently (1), the critical-strip inclusion \(0<\beta<1\), and (6)
give coefficients \(c_{\rho,\lambda}\) in (7) satisfying

\[
 \boxed{
 |c_{\rho,\lambda}|
 \ll
 \frac{B_\lambda}{1+|\gamma|},
 \qquad
 B_\lambda:=\lambda^{7/2}\sqrt{d_4}.}
 \tag{10}
\]

The functional therefore has the divisor representation

\[
 QW(e_L^+,g)
 =\sum_\rho c_{\rho,\lambda}\widehat g(z_\rho),
 \tag{11}
\]

with the complete symmetry and multiplicity convention.  The task is to
bound (11) uniformly over the \(L^2\) unit ball.  Pointwise evaluation
followed by an \(\ell^1\) sum would fail logarithmically.  The missing
gain is the Bessel cancellation among distinct ordinates.

## 2. A divisor Bessel lemma

Let

\[
 I_L=[-L/2,L/2],\qquad \lambda=e^{L/2}.
 \tag{12}
\]

We use only the unconditional facts

\[
 |\beta-\tfrac12|<\frac12
 \tag{13}
\]

and

\[
 N(T+1)-N(T)\ll\log(3+T),
 \tag{14}
\]

including multiplicities.

### Lemma 1 — Dyadic complex-frequency Bessel bound

Suppose coefficients indexed by the nontrivial divisor satisfy

\[
 |a_\rho|\le\frac{B}{1+|\gamma|}.
 \tag{15}
\]

Then the symmetric partial sums of

\[
 h(x)=\sum_\rho a_\rho
 e^{-i\gamma x}e^{(\beta-1/2)x}
 \tag{16}
\]

converge in \(L^2(I_L)\), and

\[
 \boxed{
 \|h\|_{L^2(I_L)}
 \ll B\sqrt{\lambda(1+L)}.}
 \tag{17}
\]

The implied constant is absolute for the Riemann divisor.

#### Proof

Partition the positive ordinates into the bounded initial block and the
dyadic blocks

\[
 \mathcal Z_k=\{\rho:2^k\le\gamma<2^{k+1}\},
 \qquad k\ge0.
 \tag{18}
\]

The negative ordinates are treated by conjugation.  For two zeros in the
same block, direct integration gives the Gram entry

\[
 \begin{aligned}
 G_{\rho,\rho'}
 &=\int_{-L/2}^{L/2}
 e^{(\beta+\beta'-1)x}
 e^{-i(\gamma-\gamma')x}\,dx,\\
 |G_{\rho,\rho'}|
 &\ll \lambda\min\left(L,
 \frac1{|\gamma-\gamma'|}\right),
 \end{aligned}
 \tag{19}
\]

with the second expression read as \(L\) when the ordinates coincide.
Partitioning the block into unit ordinate intervals and using (14), the
Schur row sum of this Gram matrix is

\[
 \sup_{\rho\in\mathcal Z_k}
 \sum_{\rho'\in\mathcal Z_k}|G_{\rho,\rho'}|
 \ll
 \lambda\,(1+L+k)(1+k).
 \tag{20}
\]

Indeed the interval containing \(\gamma\) contributes
\(O(\lambda L(1+k))\), while the intervals at integer distance \(m\)
contribute
\(O(\lambda(1+k)/m)\); summing up to \(O(2^k)\) gives (20).
Schur's test therefore yields

\[
 \left\|
 \sum_{\rho\in\mathcal Z_k}a_\rho
 e^{-i\gamma x}e^{(\beta-1/2)x}
 \right\|_2^2
 \ll
 \lambda(1+L+k)(1+k)
 \sum_{\rho\in\mathcal Z_k}|a_\rho|^2.
 \tag{21}
\]

Riemann--von Mangoldt and (15) give

\[
 \sum_{\rho\in\mathcal Z_k}|a_\rho|^2
 \ll B^2\frac{1+k}{2^k}.
 \tag{22}
\]

Taking square roots in (21), using (22), and summing the dyadic blocks by
the triangle inequality gives

\[
 \begin{aligned}
 \|h\|_2
 &\ll B\sqrt\lambda
 \sum_{k\ge0}
 \frac{(1+k)\sqrt{1+L+k}}{2^{k/2}}\\
 &\ll B\sqrt{\lambda(1+L)}.
 \end{aligned}
 \tag{23}
\]

The same majorant proves that the symmetric partial sums are Cauchy in
\(L^2(I_L)\).  The finite initial block and the negative ordinates only
change the constant.  This proves (17). \(\square\)

## 3. Cross-residual theorem

### Theorem 2 — Unconditional vanishing of the cross residual

For the endpoint-corrected moving vector of 106.33,

\[
 \boxed{
 \|b_L^+\|
 \ll \lambda^4\sqrt{(1+L)d_4}.}
 \tag{24}
\]

Consequently \(\|b_L^+\|\to0\).

#### Proof

For \(g\in L^2(I_L)\), insert its Fourier integral in (11).  Lemma 1
shows that the resulting divisor series has an \(L^2(I_L)\) Riesz
representative \(h_{\lambda}\) and, by (10),

\[
 \|h_\lambda\|_2
 \ll B_\lambda\sqrt{\lambda(1+L)}
 =\lambda^4\sqrt{(1+L)d_4}.
 \tag{25}
\]

Therefore

\[
 \begin{aligned}
 \|b_L^+\|
 &=\sup_{\substack{g\perp q_L^+\\g\ \mathrm{even}\\\|g\|=1}}
 |QW(e_L^+,g)|\\
 &\le\sup_{\|g\|=1}|\langle h_\lambda,g\rangle|
 \le\|h_\lambda\|_2,
 \end{aligned}
 \tag{26}
\]

which proves (24).  Finally,

\[
 d_4\asymp\lambda^9e^{-4\pi\lambda^2}
 \tag{27}
\]

gives

\[
 \lambda^4\sqrt{(1+L)d_4}
 \asymp
 \lambda^{17/2}\sqrt{1+L}\,e^{-2\pi\lambda^2}
 \longrightarrow0.
 \tag{28}
\]

This proves the asserted vanishing. \(\square\)

## 4. Consequence for the RH closure

Combining Theorem 2 with 106.33 gives

\[
 |\mathscr R_L^+|+\|b_L^+\|\longrightarrow0.
 \tag{29}
\]

Lemmas A and B of Paper 40 imply

\[
 \beta_L^+\ge c_0d_8\ge0.
 \tag{30}
\]

Thus their conclusion is stronger than the qualitative complement
condition \(\beta_L^+\ge-o(1)\) in 106.25.  The asymptotic-inertia theorem
therefore gives the implication

\[
 \boxed{
 \text{Lemma A}+\text{Lemma B}
 \Longrightarrow \mathrm{RH},}
 \tag{31}
\]

without the weighted cross budget (5).

The force-bearing obligations for the direct RH route are consequently
reduced to Lemmas A and B.  Estimate (5) remains open only if one insists
on the stronger weighted-curvature comparison rather than the direct
negative-branch contradiction.

## 5. Scope

The proof uses no localization of zeros and no positivity of the Weil
form.  Its inputs are:

1. the endpoint-corrected Fuchs--Mellin carrier estimate of 106.33;
2. the exact moving-radical cross identity;
3. the critical-strip inclusion and the unconditional local zero count;
4. a dyadic Bessel estimate for the resulting complex exponentials.

The use of the complete divisor in Lemma 1 is summability bookkeeping, not
an RH assumption: the real parts are allowed throughout the full critical
strip.
