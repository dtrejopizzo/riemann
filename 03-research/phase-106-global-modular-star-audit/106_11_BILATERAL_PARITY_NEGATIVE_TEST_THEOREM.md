# 106.11 — Bilateral parity detection for the semilocal Weil form

## Purpose

The anti-orthogonality criterion of 106.08 was left with a parity caveat:
failure of RH was shown to produce a compactly supported negative Weil test
in at least one parity sector, whereas the CCM model vector belongs to the
even sector.  This note removes that caveat.

The result is stronger and completely bilateral:

\[
 \boxed{
 \neg\mathrm{RH}
 \quad\Longrightarrow\quad
 \text{there are fixed compactly supported negative tests in both the
 even and the odd sectors.}
 }
 \tag{1}
\]

Consequently, either semilocal parity bottom detects failure of RH once its
support window is sufficiently large.  In particular, the even CCM branch
does not require an additional even--odd comparison theorem.

This theorem resolves only **parity detection**.  It does not prove the
model/ground overlap estimate, the model residual estimate, or RH.

## 1. Zero coordinate and the parity signs

Use the normalized zero coordinate

\[
 \rho=\frac12+is,
 \qquad
 \mathcal Z:=\{s\in\mathbb C:\zeta(\tfrac12+is)=0\},
 \tag{2}
\]

with multiplicity.  Every \(s=x+iy\in\mathcal Z\) lies in

\[
 |y|<\frac12.
 \tag{3}
\]

The functional equation and complex conjugation make the divisor invariant
under

\[
 s\longmapsto -s,
 \qquad
 s\longmapsto \overline s.
 \tag{4}
\]

For a real compactly supported smooth function \(f\) in the additive
coordinate, put

\[
 F(z)=\widehat f(z)=\int_{\mathbb R}f(u)e^{-izu}\,du.
 \tag{5}
\]

The polarized explicit formula gives the absolutely convergent identity

\[
 QW(f,f)
 =\sum_{s\in\mathcal Z}
   \overline{F(\overline s)}F(s).
 \tag{6}
\]

Reality gives

\[
 \overline{F(\overline z)}=F(-z).
 \tag{7}
\]

It follows that

\[
 \begin{array}{lll}
 f\text{ real even}:&F(-z)=F(z),
   &\overline{F(\overline s)}F(s)=F(s)^2,\\[2mm]
 f\text{ real odd}:&F(-z)=-F(z),
   &\overline{F(\overline s)}F(s)=-F(s)^2.
 \end{array}
 \tag{8}
\]

Assume RH is false and fix an off-line zero

\[
 s_0=x_0+iy_0,
 \qquad x_0y_0\ne0.
 \tag{9}
\]

Here \(y_0\ne0\) is exactly the failure of the critical-line condition,
and \(x_0\ne0\) follows from the classical absence of real nontrivial
zeros \(\rho\in(0,1)\).  The associated quartet is

\[
 \mathcal O_0
 =\{s_0,-s_0,\overline{s_0},-\overline{s_0}\}.
 \tag{10}
\]

If its common multiplicity is \(m_0\), then (8) gives

\[
 \begin{aligned}
 \sum_{s\in\mathcal O_0}
 \overline{F(\overline s)}F(s)
 &=4m_0\Re F(s_0)^2
 &&(f\text{ even}),\\
 &=-4m_0\Re F(s_0)^2
 &&(f\text{ odd}).
 \end{aligned}
 \tag{11}
\]

Thus the target values

\[
 F_+(s_0)=i,
 \qquad
 F_-(s_0)=1
 \tag{12}
\]

make the quartet contribution equal to \(-4m_0\) in both sectors.  The
remaining task is to realize (12) by Paley--Wiener functions while making
the rest of the zero sum arbitrarily small.

## 2. A fixed Paley--Wiener damping factor

Choose a nonzero real even function

\[
 \varphi\in C_c^\infty(\mathbb R)
 \tag{13}
\]

such that

\[
 \Phi(s_0)\ne0,
 \qquad
 \Phi:=\widehat{\varphi}.
 \tag{14}
\]

Such a choice is possible because evaluation at \(s_0\) is a nonzero
continuous linear functional on \(C_c^\infty(\mathbb R)\); one may, for example, use
an even approximate identity sufficiently concentrated at the origin.
The function \(\Phi\) is real even and entire of finite exponential type.
Integration by parts gives, for every \(M\ge0\),

\[
 \sup_{|\Im z|\le1/2}
 (1+|\Re z|)^M|\Phi(z)|<\infty.
 \tag{15}
\]

Choose \(R>|x_0|+1\), with no zero on \(|\Re z|=R\), so large that

\[
 \sup_{\substack{|\Re z|\ge R\\|\Im z|\le1/2}}
 \frac{|\Phi(z)|}{|\Phi(s_0)|}
 \le\frac12.
 \tag{16}
\]

This ordering is important: the damping factor \(\Phi\) is fixed first,
and only then is the finite height \(R\) selected from its uniform strip
decay.

## 3. Exact annihilation of the finite non-target divisor

There are finitely many zeros in

\[
 \mathcal Z_R:=\{s\in\mathcal Z:|\Re s|<R\}.
 \tag{17}
\]

Delete every occurrence of the full target orbit \(\mathcal O_0\), with
its multiplicity \(m_0\), from the zero multiset in this box, and take the
product over the remaining divisor:

\[
 Z_R(z)
 :=\prod_{s\in\mathcal Z_R\setminus\mathcal O_0}(z-s).
 \tag{18}
\]

Thus (18) is multiset subtraction, not ordinary set difference. Because
the remaining divisor is invariant under conjugation and negation,
\(Z_R\) is a real even polynomial. Moreover,

\[
 Z_R(s_0)\ne0.
 \tag{19}
\]

Put \(w_0=s_0^2\).  By (9),

\[
 \Im w_0=2x_0y_0\ne0.
 \tag{20}
\]

Therefore the real-linear map

\[
 \mathbb R^2\longrightarrow\mathbb C,
 \qquad (a,b)\longmapsto a+bw_0
 \tag{21}
\]

is an isomorphism.  For every positive integer \(N\), there consequently
exist real coefficients \(a_N,b_N,c_N,d_N\) such that

\[
 \begin{aligned}
 F_{N,+}(z)
 &:=Z_R(z)(a_N+b_Nz^2)\Phi(z)^N,
 &F_{N,+}(s_0)&=i,\\
 F_{N,-}(z)
 &:=izZ_R(z)(c_N+d_Nz^2)\Phi(z)^N,
 &F_{N,-}(s_0)&=1.
 \end{aligned}
 \tag{22}
\]

The inverse of (21) is fixed.  Hence there is a constant \(C_R\),
independent of \(N\), such that

\[
 |a_N|+|b_N|+|c_N|+|d_N|
 \le C_R|\Phi(s_0)|^{-N}.
 \tag{23}
\]

The functions in (22) have the required Paley--Wiener symmetries:

\[
 F_{N,+}\text{ is real even on }\mathbb R,
 \qquad
 F_{N,-}\text{ is purely imaginary and odd on }\mathbb R.
 \tag{24}
\]

Since multiplication by a polynomial corresponds to differentiation and
\(\Phi^N\) is the Fourier transform of the \(N\)-fold convolution of
\(\varphi\), the Paley--Wiener theorem gives real functions

\[
 f_{N,+},f_{N,-}\in C_c^\infty(\mathbb R),
 \tag{25}
\]

respectively even and odd, whose Fourier transforms are (22).  By (18),

\[
 F_{N,\pm}(s)=0
 \qquad
 (s\in\mathcal Z_R\setminus\mathcal O_0).
 \tag{26}
\]

Multiplicity causes no difficulty: every repeated occurrence in the zero
sum has value zero, while the target quartet is repeated exactly \(m_0\)
times in (11).

## 4. Uniform domination of the infinite tail

Let \(D\) be a fixed degree larger than the degrees of the polynomial
factors in (22).  From (23), for \(|\Im z|\le1/2\),

\[
 |F_{N,\pm}(z)|
 \le C_R(1+|z|)^D
 \left(\frac{|\Phi(z)|}{|\Phi(s_0)|}\right)^N.
 \tag{27}
\]

Choose a fixed \(N_0\) sufficiently large.  The rapid strip decay (15),
together with the zero-count estimate

\[
 \#\{s\in\mathcal Z:|\Re s|\le T\}=O(T\log T),
 \tag{28}
\]

implies

\[
 \sum_{\substack{s\in\mathcal Z\\|\Re s|\ge R}}
 (1+|s|)^{2D}
 \left(\frac{|\Phi(s)|}{|\Phi(s_0)|}\right)^{2N_0}
 <\infty.
 \tag{29}
\]

For \(N\ge N_0\), (16) and (27) now give

\[
 \begin{aligned}
 &\sum_{\substack{s\in\mathcal Z\\|\Re s|\ge R}}
 \left|
 \overline{F_{N,\pm}(\overline s)}F_{N,\pm}(s)
 \right|\\
 &\qquad\le
 C_R\,4^{-(N-N_0)}
 \sum_{\substack{s\in\mathcal Z\\|\Re s|\ge R}}
 (1+|s|)^{2D}
 \left(\frac{|\Phi(s)|}{|\Phi(s_0)|}\right)^{2N_0}
 \longrightarrow0.
 \end{aligned}
\tag{30}
\]

Here \(\Phi(\bar s)=\overline{\Phi(s)}\), and the same real-divisor
symmetry holds for \(Z_R\) and the polynomial factors in (22). Hence the
single strip ratio in (16) controls both factors in the polarized product;
the harmless square of \(C_R\) has been absorbed into the notation.

This also justifies absolute convergence of the zero sums used here.  More
generally, for every \(f\in C_c^\infty(\mathbb R)\), repeated integration by parts
gives rapid decay of \(\widehat f\) uniformly in (3), and (28) makes (6)
absolutely convergent.

## 5. Bilateral negative-test theorem

### Theorem 1 — Failure of RH is detected in each parity sector

If RH is false, there exist fixed nonzero real functions

\[
 f_+\in C_c^\infty(\mathbb R)^{\mathrm{even}},
 \qquad
 f_-\in C_c^\infty(\mathbb R)^{\mathrm{odd}}
 \tag{31}
\]

such that

\[
 \boxed{
 QW(f_+,f_+)<0,
 \qquad
 QW(f_-,f_-)<0.
 }
 \tag{32}
\]

#### Proof

For the even function in (22), equations (11)--(12) give target-quartet
contribution \(-4m_0\).  Equation (26) removes every other zero in the
finite box, while (30) makes the remaining contribution tend to zero.
Thus \(QW(f_{N,+},f_{N,+})<0\) for all sufficiently large \(N\).

The same argument applies to the odd function: its target-quartet
contribution is again \(-4m_0\), all other finite zeros are annihilated,
and its tail tends to zero.  Fix one sufficiently large \(N\) in each
sector and call the resulting functions \(f_+\) and \(f_-\).  This proves
(32). \(\square\)

### Corollary 2 — Both semilocal parity bottoms detect failure of RH

Let \(A_L^+\) and \(A_L^-\) be the even and odd restrictions of the
ordinary-prime semilocal Weil operator on the centered additive interval
\([-L/2,L/2]\), and let their spectral bottoms be
\(\epsilon_L^+\) and \(\epsilon_L^-\).  If RH is false, there are constants
\(c_+,c_->0\) and \(L_0\) such that

\[
 \boxed{
 \epsilon_L^+\le-c_+,
 \qquad
 \epsilon_L^-\le-c_-
 \qquad(L\ge L_0).
 }
 \tag{33}
\]

#### Proof

Choose \(L_0\) so that the fixed supports in (31) lie in
\([-L/2,L/2]\) for \(L\ge L_0\). Their additive convolutions are then
supported in \([-L,L]\), which is precisely the support range entering
the semilocal explicit formula in this normalization. Put

\[
 c_\pm=-\frac{QW(f_\pm,f_\pm)}{\|f_\pm\|_2^2}>0.
 \tag{34}
\]

The semilocal form equals the full form on these fixed tests.  The Rayleigh
principle gives (33). \(\square\)

### Corollary 3 — The even anti-orthogonality gate is parity-complete

Let \(q_L\) be normalized even model vectors for \(A_L^+\), let
\(\phi_L^+\) be normalized even ground states, and let
\(\mu_L\to0\).  If

\[
 \frac{\|(A_L^+-\mu_L)q_L\|}
 {|\langle\phi_L^+,q_L\rangle|}
 \longrightarrow0,
 \tag{35}
\]

then RH holds.

#### Proof

The sharp residual/overlap identity of 106.08 gives
\(\epsilon_L^+\to0\).  Under failure of RH this contradicts the even
estimate in (33). \(\square\)

## 6. What this does and does not close

The former parity alternative is now gone:

- no comparison \(\epsilon_L^+\le\epsilon_L^-\) is needed;
- no assumption that a generic negative Weil test happens to be even is
  needed;
- the even CCM ground branch by itself detects every hypothetical off-line
  quartet.

The remaining branch-selection problem is unchanged.  One still has to
prove the quantitative ordinary-prime estimate (35), or the stronger
weighted angle/gap estimate required for curvature convergence.  The
Paley--Wiener construction above proves that a negative even branch exists
under failure of RH; it does not exclude that branch.  Thus Theorem 1 is a
parity theorem, not a proof of Weil positivity.

## Status

Proved unconditionally:

1. an off-line zero produces a fixed compactly supported negative test in
   the even sector;
2. the same off-line zero produces a fixed compactly supported negative
   test in the odd sector;
3. both parity bottoms are bounded above by negative constants under
   failure of RH;
4. the even residual/overlap gate of 106.08 is sufficient for RH without
   any additional parity-dominance hypothesis.

Still open:

\[
 \frac{\|A_L^+q_L\|}
 {|\langle\phi_L^+,q_L\rangle|}\longrightarrow0
 \tag{36}
\]

for the actual ordinary-prime CCM model and ground state.
