# 106.138 — Common PNT Stieltjes reconstruction and the centered-path gate

## 1. Purpose and result

The boundary realization uses the normalized PNT discrepancy

\[
 D_1(T)=\frac{\psi(T)-T+1}{T},
\]

whereas the displacement form uses the weighted discrepancy

\[
 \mathcal D(u)
 =\sum_{\log n\le u}\frac{\Lambda(n)}{\sqrt n}
  -2(e^{u/2}-1).
\]

This note proves that these are two primitives of the same distribution
and reconstructs the outgoing diagonal PNT quadrature and incoming Abel
flux as one Stieltjes form.  No endpoint, theta-tail, or factor \(1/2\) is
left outside that form.

For an even multiplier \(q\), let

\[
 J_u(q)=\int_{\mathbb R}K(x)K(x-u)
 |q(x)-q(x-u)|^2\,dx.
 \tag{1}
\]

The exact conclusion is

\[
 \boxed{
 \mathfrak P_{\rm PNT}(q)
 =\mathfrak P_{\rm out}(q)+\mathfrak P_{\rm in}(q)
 =\int_{[0,\infty)}J_u(q)\,d\mathcal D(u).}
 \tag{2}
\]

Equivalently,

\[
 \boxed{
 \mathfrak P_{\rm PNT}(q)
 =-\int_0^\infty k_D(u)
 \{J_u'(q)-\tfrac12J_u(q)\}\,du,}
 \tag{3}
\]

where

\[
 k_D(u)=e^{u/2}D_1(e^u)
       =e^{-u/2}\{\psi(e^u)-e^u+1\}.
 \tag{4}
\]

The original physical form is

\[
 \boxed{
 \mathfrak Q_{\rm phys}(q)
 =\mathfrak P_{\rm PNT}(q)+\mathfrak b_{\Gamma,*}(q).}
 \tag{5a}
\]

The connection-corrected KYP supply of 106.133 is

\[
 \mathfrak Q_{\rm KYP}(q)
 =\mathfrak Q_{\rm phys}(q)
 +2\mathrm{Re}\,\langle F,\mathcal CF\rangle_{\omega_K},
 \qquad F=hq.
 \tag{5b}
\]

Combining (2) with 106.135 gives the exact KYP form

\[
 \boxed{
 \mathfrak Q_{\rm KYP}(q)
 =\mathfrak P_{\rm PNT}(q)
 +\mathfrak b_{r_\Gamma-2K}(q)
 +2\int_{\mathbb R}(K*K)(x)K(x)|q(x)|^2\,dx.}
 \tag{5c}
\]

A common sufficient gate for both
\(\mathfrak Q_{\rm phys}\ge0\) and
\(\mathfrak Q_{\rm KYP}\ge0\) is

\[
 \boxed{
 \mathfrak P_{\rm PNT}(q)
 +\frac{499}{2000}\mathfrak b_{\Gamma,*}(q)\ge0.}
 \tag{6}
\]

Indeed, (6) implies (5a) after adding
\((1501/2000)\mathfrak b_{\Gamma,*}\ge0\), while 106.135 implies

\[
 \mathfrak Q_{\rm KYP}
 \ge\mathfrak P_{\rm PNT}
 +\frac{499}{2000}\mathfrak b_{\Gamma,*}.
\]

Thus (6) is stronger than the original physical surplus; it is not an
exact rewriting of it.

The reconstruction is exact, but it also gives a sharp factorization
gate.  The measure in (6) is strictly negative on a whole interval below
the first prime.  Moreover the canonical centered-path completion has an
unavoidable negative derivative square.  Consequently neither a
displacement-local square nor a triangle estimate can prove (6).  A
successful continuation must be nonlocal in displacement and use the
complete mean-periodic compression.

## 2. Common core and cutoff convention

The calculations are first made on the real-even smooth multiplier core
for which

\[
 f=Kq,\qquad p=K|q|^2
 \tag{7}
\]

and their required first derivatives decrease rapidly.  Compact smooth
multipliers are sufficient.  At a finite displacement cutoff \(U\), all
prime atoms, the PNT continuum, and the Abel transform use the same
right-continuous convention.  The limit is then taken jointly.

It is enough below that

\[
 \mathcal D(U)J_U(q)\longrightarrow0,
 \qquad k_D(U)J_U(q)\longrightarrow0,
 \tag{8}
\]

and that the analogous boundary products for the correlation in (18)
vanish.  These conditions hold on the stated core because \(K\) decreases
double exponentially.  Heat rows and translation-smooth hybrid rows are
obtained by the common-cutoff closed-form approximation already used in
106.102, 106.118, and 106.131.  Thus no separate conditional integral is
introduced in passing to the closed heat core.

## 3. The two PNT discrepancies are exact primitives

Put

\[
 E_1(T)=\psi(T)-T+1,
 \qquad E_1(1)=0.
 \tag{9}
\]

The weighted discrepancy is the locally finite Stieltjes primitive

\[
 \boxed{
 \mathcal D(u)
 =\int_{[1,e^u]}T^{-1/2}\,dE_1(T).}
 \tag{10}
\]

Indeed, its atoms are \(\Lambda(n)n^{-1/2}\), while its continuous
part is \(-T^{-1/2}dT\), whose integral is
\(-2(e^{u/2}-1)\).  Stieltjes integration by parts in (10) gives

\[
\begin{aligned}
 \mathcal D(u)
 &=e^{-u/2}E_1(e^u)
   +\frac12\int_1^{e^u}E_1(T)T^{-3/2}\,dT\\
 &=k_D(u)+\frac12\int_0^u k_D(v)\,dv.
\end{aligned}
 \tag{11}
\]

Thus, as distributions on the positive half-line,

\[
 \boxed{d\mathcal D=dk_D+\frac12k_D(u)\,du.}
 \tag{12}
\]

This identity is the exact source of the centered derivative
\(\partial_u-1/2\) in the Abel realization.

## 4. One Stieltjes form

Pairing (12) with (1), using \(k_D(0)=0\) and the common boundary
condition, gives

\[
\begin{aligned}
 \int J_u\,d\mathcal D(u)
 &=\int J_u\,dk_D(u)+\frac12\int k_D(u)J_u\,du\\
 &=-\int_0^\infty k_D(u)
    \{J_u'-\tfrac12J_u\}\,du.
\end{aligned}
 \tag{13}
\]

This proves (3).  A second equivalent version is

\[
 \boxed{
 \mathfrak P_{\rm PNT}(q)
 =-\int_0^\infty E_1(e^u)
 \frac d{du}\{e^{-u/2}J_u(q)\}\,du.}
 \tag{14}
\]

Replacing \(E_1\) by \(E=\psi(e^u)-e^u\) changes (14) by the integral
of a full derivative with zero endpoints.  Hence (14) is exactly the
quadrature formula of 106.116, with its endpoint convention now explicit.

## 5. Exact outgoing and incoming pieces

Expanding the difference square in (1) and using evenness gives

\[
 J_u(q)=B_-(u)+B_+(u)-2\mathrm{Re}\,C(u),
 \tag{15}
\]

where

\[
\begin{aligned}
 B_-(u)&=\int_{\mathbb R}K(x)|q(x)|^2K(x-u)\,dx,\\
 B_+(u)&=\int_{\mathbb R}K(x)|q(x)|^2K(x+u)\,dx,\\
 C(u)&=\int_{\mathbb R}\overline{f(y+u)}f(y)\,dy.
\end{aligned}
 \tag{16}
\]

The diagonal term is therefore

\[
 \boxed{
 \mathfrak P_{\rm out}(q)
 =\int_{\mathbb R}K(x)|q(x)|^2
 \int_{[0,\infty)}\{K(x-u)+K(x+u)\}\,d\mathcal D(u)\,dx.}
 \tag{17}
\]

Multiplication of the inner integral by \(c_K/h(x)\), followed by pairing
against \(d\mu_K=hK\,dx/c_K\), is precisely the outgoing multiplier
\(\Delta_\psi\) of 106.127.  Thus (17) fixes its coefficient without a
boundary normalization choice.

For the correlation term, (12) gives

\[
 -2\mathrm{Re}\,\int C\,d\mathcal D
 =2\mathrm{Re}\,\int_0^\infty
 k_D(u)\{C'(u)-\tfrac12C(u)\}\,du.
 \tag{18}
\]

Integration by parts in the base point \(y\) yields

\[
 C'(u)-\frac12C(u)
 =-\int_{\mathbb R}\overline{f(y+u)}
 \{f'(y)+\tfrac12f(y)\}\,dy.
 \tag{19}
\]

Consequently

\[
 \boxed{
\begin{aligned}
 \mathfrak P_{\rm in}(q)
 =-2\mathrm{Re}\,\int_{x>y}
 D_1(e^{x-y})e^{(x-y)/2}\,
 \overline{K(x)q(x)}
 \{(Kq)'(y)+\tfrac12K(y)q(y)\}\,dy\,dx.
\end{aligned}}
 \tag{20}
\]

This is exactly the Abel flux of 106.127 and 106.131.  Equations
(15)--(20) prove (2).  In particular, the theta endpoint which appears
when the raw prime sum is Abel-summed separately is already canceled by
the continuum line inside \(d\mathcal D\).  Adding it once more would
double count a boundary term.

## 6. Centered-path factorization

Let

\[
 (C_uq)(x)=\{K(x)K(x-u)\}^{1/2}
 \{q(x)-q(x-u)\}
 \tag{21}
\]

and define the Hilbert-valued centered path

\[
 Z_q(u)=e^{-u/4}C_uq.
 \tag{22}
\]

Then

\[
 \|Z_q(u)\|_2^2=e^{-u/2}J_u(q).
 \tag{23}
\]

For \(0<\theta\le1\), set

\[
 a_\theta(u)
 =\theta e^{u/2}r_\Gamma(u)
 =\theta\frac{e^{-2u}}{1-e^{-2u}}>0.
 \tag{24}
\]

Equations (14), (23), and (24) give the exact path form

\[
\boxed{
\begin{aligned}
 \mathfrak P_{\rm PNT}(q)
 +\theta\mathfrak b_{\Gamma,*}(q)
 =\int_0^\infty
 \{a_\theta\|Z_q\|^2
 -2E_1(e^u)\mathrm{Re}\,\langle Z_q,Z_q'\rangle\}\,du.
\end{aligned}}
 \tag{25}
\]

Completing the only pointwise square available in (25) produces

\[
\boxed{
\begin{aligned}
 \mathfrak P_{\rm PNT}
 +\theta\mathfrak b_{\Gamma,*}
 ={}&\int_0^\infty a_\theta
 \left\|Z_q-\frac{E_1(e^u)}{a_\theta}Z_q'\right\|^2du\\
 &-\int_0^\infty
 \frac{E_1(e^u)^2}{a_\theta(u)}\|Z_q'(u)\|^2du.
\end{aligned}}
 \tag{26}
\]

The second line has the wrong sign.  It is not an omitted Gamma term: all
of the Gamma budget used in this completion is already in \(a_\theta\).
Thus the centered Abel derivative does not yield a local positive square.

## 7. Exact local-sign obstruction at the available margin

Take

\[
 \theta_*=\frac{499}{2000}.
 \tag{27}
\]

Below the first prime, \(d\mathcal D(u)=-e^{u/2}du\).  Hence the scalar
density in the sufficient form (6) is

\[
 w_*(u)=-e^{u/2}+\theta_*r_\Gamma(u).
 \tag{28}
\]

Writing \(z=e^u\), one has

\[
 \frac{\theta_*r_\Gamma(u)}{e^{u/2}}
 =\frac{\theta_*}{z^3-z}.
 \tag{29}
\]

For \(z\ge9/8\),

\[
 z^3-z\ge\frac{153}{512}>\frac{499}{2000},
 \tag{30}
\]

because \(306000>255488\).  Therefore

\[
 \boxed{
 w_*(u)<0
 \quad\left(\log\frac98\le u<\log2\right).}
 \tag{31}
\]

So (6) cannot be obtained by replacing its scalar coefficient of the
same local difference square (C_uq) by a nonnegative density.  In
the exact KYP residual (5c), the displacement density

\[
 -e^{u/2}+r_\Gamma(u)-2K(u)
 \tag{32}
\]

is likewise strictly negative for
\(\log(3/2)\le u<\log2\), since
\(z^3-z\ge15/8>1\) and \(K>0\).  The final positive multiplication term
in (5) is therefore genuinely nonlocal relative to the displacement
measure; it cannot be absorbed into a pointwise density.

## 8. The derivative-square loss is quantitatively real

Let

\[
 q_N(x)=\chi(x)\cos(Nx),
 \qquad0\ne\chi\in C_c^\infty(\mathbb R)
 \tag{33}
\]

be the oscillatory hybrid family of 106.118, with the support chosen so
that it overlaps its translates on a fixed closed interval
\(I\Subset(0,\log2)\).  Differentiating (21)--(22) shows, uniformly for
\(u\in I\),

\[
 Z_{q_N}'(u,x)
 =-N e^{-u/4}\{K(x)K(x-u)\}^{1/2}
 \chi(x-u)\sin(N(x-u))+O_I(1)
 \tag{34}
\]

in \(L^2(dx)\).  Averaging the leading sine square and using positivity of
\(K\) on the compact overlap gives

\[
 \boxed{
 \int_I\|Z_{q_N}'(u)\|_2^2\,du\ge c_I N^2}
 \tag{35}
\]

for all sufficiently large \(N\).  On the same interval,
\(|E_1(e^u)|\) and \(a_{\theta_*}^{-1}\) are bounded below by positive
constants after shrinking \(I\) away from zero.  Thus the negative term
in (26) has size at least \(cN^2\).  By contrast, 106.118 proves

\[
 \mathfrak b_{\Gamma,*}(q_N)=O(\log N),
 \qquad
 \mathfrak P_{\rm PNT}(q_N)=O(1).
 \tag{36}
\]

The two \(N^2\) terms in (26) cancel each other.  Estimating either one
separately destroys that cancellation by a factor larger than any fixed
Gamma margin.  Projection off any fixed finite radical block changes
(34)--(36) by \(O(N^{-A})\) for every \(A\), as proved in 106.118.

This is a test of the local completion, not a counterexample to the
physical Riemann form.  The family is not the complete cofinal radical
anti-short.

## 9. Consequence for the physical-surplus proof

The outgoing and incoming PNT channels are no longer separate unknowns.
They are exactly the one common Stieltjes form (2), and the available
Gamma--connection margin reduces the sufficient closure to (6).

Equations (26), (31), and (35) prove that the next step cannot be any of:

1. positivity of the scalar coefficient of the existing displacement
   square;
2. the canonical pointwise completion of the centered Abel derivative;
3. a bound of \(J'\) or \(Z'\) by the Gamma form;
4. a finite-radical version of one of those estimates.

These statements do not exclude an enlarged matrix-valued local amplitude
which mixes additional channels before taking a square; such a construction
would require a separate locality-uniqueness analysis.  The presently
surviving theorem is a nonlocal contraction for
the map

\[
 q\longmapsto\{C_uq\}_{u>0}
 \tag{37}
\]

after the complete mean-periodic anti-short, using the actual prime-power
locations before taking a norm.  For the original physical theorem it
must prove (5a); for the connection-corrected route it must prove (5c).
The common stronger sufficient version is (6).  The present reconstruction
fixes the coefficients and domain of that theorem and rules out a local
Stieltjes or centered-path substitute.
