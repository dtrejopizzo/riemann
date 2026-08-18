# 106.114 — The theta martingale and the total-variance gate

## 1. Purpose and verdict

The theta--divisor decomposition of 106.104 has an exact probabilistic
interpretation.  Conditional on the farther theta index \(b\), choose a
prime-power divisor \(n\mid b\) with probability

\[
 \frac{\Lambda(n)}{\log b}.
\]

Then the divisor current is the conditional mean of the spatial increment
and the divisor dispersion is its conditional variance.  There is also a
natural latent-theta probability space for the folded polar law
\(\mu_K\).  Thus both sides of the sharp physical inequality possess exact
law-of-total-variance decompositions.

This note constructs both laws and tests whether they can be joined into one
positive martingale coupling while retaining the same-side, central and
Gamma channels before any square is discarded.  The answer is no.

The obstruction is exact.  Every complete positive martingale tower
collapses, by the tower property, to a positive first-chaos coupling between
the complete theta edge law and the polar pair law.  Equality on the Riemann
radicals forces every martingale difference and every unused source square
to vanish.  The radical signatures then force endpoint preservation.  This
is incompatible with the literal positive source mass on the ordinary
prime-power lines, which have zero polar-pair measure.

Consequently a law-of-total-variance proof cannot establish

\[
 \mathscr E_K(r)\geq\frac12\operatorname {Var}_{\mu_K}(r)
\]

with equality on all \(K^{(2j)}/K\), even when every divisor dispersion and
the full continuous Gamma channel are retained.  A surviving proof must be
globally signed after the exact radical anti-short; it cannot be a positive
probability coupling in disguise.

No zero location is used below.

## 2. The folded polar theta law

For \(t>0\), retain the theta atoms

\[
 k_b(t)=e^{t/2}\phi(be^t),
 \qquad
 \phi(s)=\pi s^2(2\pi s^2-3)e^{-\pi s^2},
 \qquad
 K(t)=\sum_{b\geq1}k_b(t).
 \tag{1}
\]

The normalization is the one for which
\(c_K=\int_{\mathbb R}\cosh(x/2)K(x)\,dx=1/2\).  For an even multiplier,
folding the polar probability measure to the positive half-line gives

\[
 d\bar\mu_K(t)=4\cosh(t/2)K(t)\,dt.
 \tag{2}
\]

Introduce a latent integer \(B\) by

\[
 \mathbb P(B=b,T\in dt)
 =4\cosh(t/2)k_b(t)\,dt.
 \tag{3}
\]

Summing over \(b\) gives (2), so (3) is a probability law.  Its dilation
coordinate

\[
 S=Be^T
 \tag{4}
\]

is particularly simple.  The change of variables
\(t=\log(s/b)\), \(dt=ds/s\), gives

\[
 \boxed{
 \mathbb P(S\in ds,B=b)
 =2\phi(s)\left(\frac1b+\frac1s\right)
   {\bf1}_{\{b<s\}}\,ds.}
 \tag{5}
\]

Put

\[
 q_s(b)=\frac1b+\frac1s,
 \qquad
 Q(s)=\sum_{b<s}q_s(b),
 \qquad
 R_s(b)=r\!\left(\log\frac{s}{b}\right).
 \tag{6}
\]

The \(S\)-marginal is

\[
 d\nu(s)=2\phi(s)Q(s)\,ds,
 \tag{7}
\]

and the conditional law of \(B\) given \(S=s\) is \(q_s(b)/Q(s)\).
Therefore the ordinary law of total variance gives the exact identity

\[
\boxed{
\begin{aligned}
 \operatorname {Var}_{\mu_K}(r)
={}&2\int_1^\infty\phi(s)
 \left\{
  \sum_{b<s}q_s(b)|R_s(b)|^2
  -\frac{\left|\sum_{b<s}q_s(b)R_s(b)\right|^2}{Q(s)}
 \right\}ds\\
 &+\operatorname {Var}_{\nu}
 \left(
   \frac1{Q(S)}\sum_{b<S}q_S(b)R_S(b)
 \right).
\end{aligned}}
\tag{8}
\]

Thus the target variance already has a canonical two-level theta
martingale: a conditional theta-index variance at fixed \(S\), followed by
the variance of the conditional mean in the continuous dilation variable.

## 3. The divisor currents are source martingales

For \(b\geq2\), let

\[
 \mathbb P_b(N=n)
 =\frac{\Lambda(n)}{\log b},
 \qquad n\mid b,\quad n\geq2.
 \tag{9}
\]

This is a probability law because

\[
 \sum_{n\mid b}\Lambda(n)=\log b.
 \tag{10}
\]

At a same-side fibre \((b,y)\), set

\[
 X_{b,y}=r(y+\log N)-r(y).
 \tag{11}
\]

Equations 106.104(12)--(14) are exactly

\[
\boxed{
\begin{aligned}
 D_b^+r(y)&=\mathbb E_bX_{b,y},\\
 V_b^+(r;y)&=(\log b)\operatorname {Var}_b(X_{b,y}),\\
 \sum_{n\mid b}\Lambda(n)|\Delta_n^+r(y)|^2
 &=(\log b)|\mathbb E_bX_{b,y}|^2
   +(\log b)\operatorname {Var}_b(X_{b,y}).
\end{aligned}}
\tag{12}
\]

At a central fibre \((b,x)\), use instead

\[
 \mathbb P_{b,x}(N=n)
 =\frac{\Lambda(n)}{\ell_b(x)},
 \qquad n\mid b,\quad \log n\geq x.
 \tag{13}
\]

With \(X_{b,x}=r(\log N-x)-r(x)\), one obtains

\[
\boxed{
 D_{b,x}^-r=\mathbb E_{b,x}X_{b,x},
 \qquad
 V_{b,x}^-(r)=\ell_b(x)\operatorname {Var}_{b,x}(X_{b,x}).}
\tag{14}
\]

Hence the current and dispersion terms are not two estimates.  They are
the constant and mean-zero coordinates of one conditional \(L^2\) space.
Fibrewise, the map

\[
 z_N\longmapsto
 \left(\sqrt{\ell}\,\mathbb Ez_N,
       \sqrt{\ell}\{z_N-\mathbb Ez_N\}\right)
 \tag{15}
\]

is unitary from the weighted divisor fibre to
\(\mathbb C\oplus L_0^2(N)\).  Taking the direct integral of (15) over all
same-side and central fibres, and using the identity on the Gamma channel,
produces a unitary source gauge \(U_{\rm anova}\) satisfying

\[
 \boxed{
 \|U_{\rm anova}\nabla_\Theta r\|^2
 =\|\nabla_\Theta r\|^2
 =\mathscr E_K(r).}
 \tag{16}
\]

Thus retaining *all* currents, dispersions and Gamma fibres restores the
complete source norm, but creates no additional norm.

## 4. The canonical separated assignment already fails

The most direct use of (8) and (12) would charge the conditional
theta-index variance in (8) to the same-side divisor edges and reserve the
continuous Gamma channel for the outer \(S\)-variance.  This assignment
fails pointwise before any asymptotic issue arises.

Put

\[
 \Phi(v)=\sum_{a\geq1}\phi(av).
 \tag{17}
\]

In the same-side prime form, set \(s=be^y\).  Since

\[
 K(y)=e^{y/2}\Phi(e^y),
 \qquad
 k_b(y)=e^{y/2}\phi(be^y),
\]

the exact change of variables in 106.104(7) gives

\[
\boxed{
 \mathscr E_p^{\rm ss}(r)
 =2\int_1^\infty\phi(s)
 \sum_{b<s}\frac{\Phi(s/b)}{b}
 \sum_{n\mid b}\Lambda(n)
 |R_s(b/n)-R_s(b)|^2\,ds.}
\tag{18}
\]

For \(2<s<3\), the target conditional law has only \(b=1,2\).  The
coefficient of

\[
 |R_s(1)-R_s(2)|^2
\]

in one half of the first line of (8), after the common factor \(\phi(s)\)
is removed, is

\[
 c_{\rm pol}(s)
 =\frac{(1+s^{-1})(1/2+s^{-1})}
        {3/2+2s^{-1}},
 \qquad
 \lim_{s\downarrow2}c_{\rm pol}(s)=\frac35.
 \tag{19}
\]

The only same-side prime edge connecting these two states is
\(b=2,n=2\).  Its coefficient in (18), after the same common factor is
removed, is

\[
 c_p(s)=(\log2)\Phi(s/2).
 \tag{20}
\]

There is a completely elementary strict gap at the endpoint.  Indeed,

\[
 \Phi(1)=\sum_{a\geq1}
 \pi a^2(2\pi a^2-3)e^{-\pi a^2}.
\]

Using \(\pi<22/7\), \(e^3>20\), \(\log2<0.7\), and, for \(a\geq2\),

\[
 0<\phi(a)<20a^4e^{-3a^2},
\]

whose successive ratio is less than \(2\cdot10^{-6}\), gives

\[
 \Phi(1)<0.519,
 \qquad
 (\log2)\Phi(1)<0.364<\frac35.
 \tag{21}
\]

By continuity, \(c_p(s)<c_{\rm pol}(s)\) on a nonempty interval to the
right of \(2\).  Thus the prime divisor martingale cannot pay the inner
variance while Gamma pays only the outer variance.  Any probabilistic
successor would have to mix Gamma and prime fibres already inside the same
conditional layer.

The central channel is not a fixed-\(S\) edge in the folded law (5), so
using it to repair (21) likewise requires a cross-\(S\) coupling.  Thus
(21) rules out only the canonical separated filtration; the theorem below
allows arbitrary cross-\(S\) mixing of the central and Gamma channels.

## 5. Complete martingale towers reduce to first chaos

We now allow precisely that mixing and show that it still cannot be sharp.
Let \(\mathsf E_\Theta\) be the complete marked edge space of 106.65,
including Gamma, divisible, fractional and central edges, with measure
\(\Omega_\Theta\).  Let \(\mathsf S=\{(t,s):t>s>0\}\) carry the polar pair
measure

\[
 d\rho(t,s)=8h(t)h(s)K(t)K(s)\,dt\,ds.
 \tag{22}
\]

For an even multiplier, write

\[
 V_r(E)=\nabla_\Theta r(E),
 \qquad
 v_r(Z)=\nabla_0r(Z).
 \tag{23}
\]

Then

\[
 \int|V_r|^2d\Omega_\Theta=\mathscr E_K(r),
 \qquad
 \int|v_r|^2d\rho=\frac12\operatorname {Var}_{\mu_K}(r).
 \tag{24}
\]

### Definition — Complete positive martingale routing

Such a routing consists of a positive measure \(Q\) on
\(\mathsf S\times\mathsf E_\Theta\), with

\[
 Q_{\mathsf S}=\rho,
 \qquad
 Q_{\mathsf E_\Theta}\leq\Omega_\Theta,
 \tag{25}
\]
and a finite or countable filtration

\[
 \sigma(Z)=\mathcal F_0\subset\mathcal F_1\subset\cdots
 \subset\mathcal F_\infty=\sigma(Z,E),
 \tag{26}
\]

such that, for every multiplier in the form core,

\[
 M_k^r=\mathbb E_Q[V_r(E)\mid\mathcal F_k],
 \qquad
 M_0^r=v_r(Z),
 \qquad
 M_\infty^r=V_r(E).
 \tag{27}
\]

This is a finite measure: \(\rho(\mathsf S)=1/4\).  All conditional
expectations below are therefore the ordinary finite-measure ones.  The
domination in (25) also makes
\(\Omega_\Theta-Q_{\mathsf E_\Theta}\) a positive measure.

The divisor conditioning (9)--(14), arbitrary further theta conditionings,
and an arbitrary mixing of the Gamma and prime channel labels are all
allowed in (26).  No conditional square is discarded.

### Theorem 1 — Exact martingale defect identity

Every complete positive martingale routing would satisfy

\[
\boxed{
\begin{aligned}
 \mathscr E_K(r)-\frac12\operatorname {Var}_{\mu_K}(r)
={}&\sum_{k\geq1}\|M_k^r-M_{k-1}^r\|_{L^2(Q)}^2\\
 &+\int_{\mathsf E_\Theta}|V_r(e)|^2
 \,d(\Omega_\Theta-Q_{\mathsf E_\Theta})(e).
\end{aligned}}
\tag{28}
\]

For a countable filtration, \(\mathcal F_k\uparrow\sigma(Z,E)\) is
understood modulo completion.  The sum is the monotone \(L^2\)-martingale
limit.

#### Proof

Martingale differences are mutually orthogonal.  Therefore

\[
 \int|V_r|^2dQ_{\mathsf E_\Theta}
 -\int|v_r|^2d\rho
 =\sum_{k\geq1}\|M_k^r-M_{k-1}^r\|_2^2.
 \tag{29}
\]

Add the nonnegative unused-source integral in (28), and apply (24)--(25).
\(\square\)

Equation (28) is the most flexible law-of-total-variance proof available
on the latent theta probability space.  In particular, (15) may be placed
at any level of its filtration without changing the identity.

## 6. Radical saturation gives a literal prime-line contradiction

Let

\[
 r_j=K^{(2j)}/K,
 \qquad j\geq0.
 \tag{30}
\]

The exact radical identity gives

\[
 \mathscr E_K(r_j)
 =\frac12\operatorname {Var}_{\mu_K}(r_j).
 \tag{31}
\]

Although the \(r_j\) need not be compactly supported, they belong to the
extended closed form domain by the compact near-radical approximation of
106.32.  More explicitly, if \(\chi_R\) is an even smooth cutoff equal to
one on \([-R,R]\), that approximation proves

\[
 \nabla_\Theta(\chi_Rr_j)\longrightarrow\nabla_\Theta r_j
 \quad\text{in }L^2(\Omega_\Theta),
 \qquad
 \nabla_0(\chi_Rr_j)\longrightarrow\nabla_0r_j
 \quad\text{in }L^2(\rho).
 \tag{31a}
\]

The first convergence uses the theta double-exponential tail and the
Gamma small-jump estimate; the second uses the same tail in the polar
probability.  Since \(Q_{\mathsf E_\Theta}\leq\Omega_\Theta\), conditional
expectation is an \(L^2\)-contraction on these approximants.  Hence
(27)--(29) pass to every \(r_j\).

### Theorem 2 — No complete positive theta martingale exists

There is no routing satisfying (25)--(27) and the radical equalities
(31).

#### Proof

Insert \(r_j\) in (28).  Every term on the right is nonnegative and the
left side is zero.  Intersecting the resulting countable family of
full-measure sets, one obtains simultaneously for all \(j\),

\[
 V_{r_j}(E)=v_{r_j}(Z)\quad Q\text{-almost surely},
 \tag{32}
\]

and

\[
 \int|V_{r_j}|^2
 \,d(\Omega_\Theta-Q_{\mathsf E_\Theta})=0.
 \tag{33}
\]

The radical edge-separation lemma of 106.65 applies to the countable family
in (32).  It forces equality of the oriented spatial endpoints:

\[
 \partial E=Z\quad Q\text{-almost surely}.
 \tag{34}
\]

Let \(\mathcal L_p\) be the countable union of the ordinary prime-power
lines

\[
 t-s=\log n,
 \qquad
 t+s=\log n,
 \qquad \Lambda(n)>0.
 \tag{35}
\]

The prime part of \(\Omega_\Theta\) has strictly positive mass on every
such line.  For the nonconstant radical \(r_1=K''/K\), its edge increment
is nonzero almost everywhere on every line: otherwise analyticity would
make \(r_1\) periodic or reflection-periodic.  Thus (33) says that the
prime-line energy cannot be omitted by \(Q_{\mathsf E_\Theta}\).

On the other hand, (34) and the first marginal in (25) give

\[
 Q\{\partial E\in\mathcal L_p\}
 =\rho(\mathcal L_p)=0,
 \tag{36}
\]

because \(\rho\) is absolutely continuous.  This contradicts the positive
prime-line energy forced by (33).  \(\square\)

The contradiction uses the literal ordinary von Mangoldt atoms and every
conditional dispersion.  It is not the current-only Jensen failure of
106.104: (28) permits all currents, all dispersions, the fractional and
central channels, and the entire Gamma continuum at arbitrary martingale
levels.

## 7. Heat and hybrid rows

For a positive finite-rank heat or hybrid state, apply (28) row by row and
sum with its positive spectral weights.  Tonelli applies to every term on
the right.  A universal martingale routing would therefore give the same
identity with Hilbert--Schmidt norms.  Taking a rank-one radical row again
gives Theorem 2.  Positive mixing of heat rows cannot remove the
obstruction.

This does not rule out a state-dependent globally signed transfer after
the radical has been projected out.  It proves that such a transfer cannot
be obtained by enlarging the theta probability space and applying the law
of total variance, even with infinitely many conditioning levels.

## 8. Status

Proved here:

* the exact folded polar theta probability law (5);
* the target law-of-total-variance decomposition (8);
* the exact divisor-selector martingales (12)--(14);
* the unitary current-plus-dispersion gauge (16);
* a strict two-state obstruction to separating inner prime variance from
  outer Gamma variance;
* the exact defect identity for every finite or countable complete
  martingale tower (28);
* impossibility of a radical-sharp positive martingale coupling by the
  literal prime-line capacity contradiction.

Not proved here:

\[
 \mathscr E_K(r)\geq\frac12\operatorname {Var}_{\mu_K}(r).
\]

The remaining heat/hybrid physical surplus must use a globally signed,
non-Markov transfer after exact radical anti-shorting.  The latent theta
mixture supplies exact coordinates, but no positive probabilistic shortcut.
