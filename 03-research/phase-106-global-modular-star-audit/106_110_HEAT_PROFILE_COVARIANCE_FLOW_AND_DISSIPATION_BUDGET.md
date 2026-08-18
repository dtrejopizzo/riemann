# 106.110 — Heat-profile covariance flow and the dissipation budget

## 1. Purpose and conclusion

The heat-localized criterion of 106.102 is expressed through the scalar
displacement profile

\[
 J_t(u)=\mathcal J_u[\Gamma_t].
 \tag{1}
\]

This profile is much more constrained than an arbitrary positive bump.  It
is the difference between a ground-state convolution and a positive-definite
autocorrelation.  Under the physical heat flow it is the diagonal marginal
of a positive source covariance satisfying a closed noncommutative Lyapunov
equation.

After one canonical cutoff-safe subtraction, the ground-state convolution
annihilates against the complete compensated source by the exact Riemann
radical identity.  Hence the scalar defect is governed entirely by the
positive-definite autocorrelation component.  This is the strongest scalar
simplification supplied by the heat profile.

Those facts are exact.  They also locate the remaining obstruction.  The
scalar profile does not satisfy a closed evolution: its derivative contains
off-diagonal two-displacement amplitudes.  The theta-character identities of
106.104--106.108 give exact coordinates for those amplitudes, but act by a
unitary change of source gauge and therefore leave the required norm and the
heat dissipation invariant.

The resulting exact target is a first-versus-second source budget:

\[
 \boxed{
 \int_t^\infty \mathrm{Var}_s(A)\,ds
 \leq
 \frac{\displaystyle\int_0^\infty J_t(u)\,d\sigma(u)}
      {\mathrm{Tr}\,\Gamma_t}.}
 \tag{2}
\]

For one, equivalently every, heat time, (2) is equivalent to the physical
surplus.  Thus the all-order theta currents can contribute only if they prove
this quantitative dissipation budget with the fractional, central, Gamma and
polar channels still assembled.  Positivity of the raw second current is not
enough.

No zero location is used below.

## 2. The exact autocorrelation representation

First let

\[
 \Gamma=\sum_{j=1}^N\gamma_j|r_j\rangle\langle r_j|,
 \qquad \gamma_j>0,
 \tag{3}
\]

be a finite-rank positive state whose rows are even and translation-smooth.
Put

\[
 f_j=Kr_j,
 \qquad
 p_\Gamma(x)=K(x)\sum_{j=1}^N\gamma_j|r_j(x)|^2,
 \tag{4}
\]

and define

\[
 C_\Gamma(u)
 =\sum_{j=1}^N\gamma_j
   \int_{\mathbb R}f_j(x)\overline{f_j(x-u)}\,dx,
 \qquad
 W_\Gamma(u)=(p_\Gamma*K)(u).
 \tag{5}
\]

Both functions are even and real after taking the real part of
\(C_\Gamma\).  Moreover,

\[
 W_\Gamma(0)=C_\Gamma(0)
 =\sum_j\gamma_j\int_{\mathbb R}K(x)^2|r_j(x)|^2\,dx.
 \tag{6}
\]

### Theorem 1 — Ground-state convolution minus autocorrelation

For every real \(u\),

\[
 \boxed{
 \mathcal J_u[\Gamma]
 =2\{W_\Gamma(u)-\mathrm{Re}\,C_\Gamma(u)\}.}
 \tag{7}
\]

The function \(C_\Gamma\) is positive definite.  If

\[
 G_\Gamma(u)
 :=\sum_j\gamma_j\|f_j-\tau_uf_j\|_2^2
 =2\{C_\Gamma(0)-\mathrm{Re}\,C_\Gamma(u)\},
 \tag{8}
\]

then \(G_\Gamma\) is conditionally negative definite and

\[
 \boxed{
 \mathcal J_u[\Gamma]
 =G_\Gamma(u)+2\{W_\Gamma(u)-W_\Gamma(0)\}.}
 \tag{9}
\]

#### Proof

Expand the jump square.  The first diagonal term is

\[
 \sum_j\gamma_j\int K(x)K(x-u)|r_j(x)|^2\,dx
 =W_\Gamma(u).
\]

After the change of variable \(x\mapsto x+u\), the second diagonal term is
\(W_\Gamma(-u)=W_\Gamma(u)\).  The cross term is
\(2\mathrm{Re}\,C_\Gamma(u)\), proving (7).

For arbitrary \(c_a\in\mathbb C\) and \(u_a\in\mathbb R\),

\[
 \sum_{a,b}c_a\overline{c_b}C_\Gamma(u_a-u_b)
 =\sum_j\gamma_j
   \left\|\sum_a c_a\tau_{u_a}f_j\right\|_2^2\geq0.
 \tag{10}
\]

Thus \(C_\Gamma\) is positive definite.  Formula (8) is the squared
translation distance of a Hilbert-space orbit and is therefore
conditionally negative definite.  Equations (6)--(8) give (9).  \(\square\)

Theorem 1 separates precisely the stationary information from the Doob
ground-state correction.  Negative type controls \(G_\Gamma\), but the
second term of (9) is not translation invariant and has no fixed sign.
This is why the translation-metric obstruction of 106.22 does not by itself
settle the physical profile.

The formulas extend to positive trace-class translation-smooth states by
positive finite-rank approximation.  On the heat core all pairings below
are obtained by the same approximation in the closed source form.

## 3. Cutoff-safe cancellation of the diagonal convolution

The two terms on the right of (7) cannot be paired separately with
\(d\sigma\) as written.  At the Gamma endpoint they have the same nonzero
constant, while at infinity a constant subtraction would meet the growing
polar density.  There is, however, a canonical simultaneous
renormalization which makes both terms admissible and exposes an exact
cancellation.

Put

\[
 C_K(u)=\int_{\mathbb R}K(x)K(x-u)\,dx,
 \qquad
 \chi_K(u)=\frac{C_K(u)}{C_K(0)}.
 \tag{10a}
\]

Then \(\chi_K(0)=1\), \(\chi_K'(0)=0\), and \(\chi_K\) decreases
double exponentially at infinity.  Define

\[
 W_\Gamma^\circ(u)=W_\Gamma(u)-W_\Gamma(0)\chi_K(u),
 \qquad
 C_\Gamma^\circ(u)=\mathrm{Re}\,C_\Gamma(u)
                    -C_\Gamma(0)\chi_K(u).
 \tag{10b}
\]

Both functions vanish to second order at zero and decay at infinity.
Consequently their pairing with the complete compensated distribution is
cutoff independent.  Denote that pairing by

\[
 \ell_\sigma(F)=\int_0^\infty F(u)\,d\sigma(u).
 \tag{10c}
\]

### Theorem 2 — Exact radical cancellation of the diagonal term

For every state in Theorem 1,

\[
 \boxed{\ell_\sigma(W_\Gamma^\circ)=0.}
 \tag{10d}
\]

Therefore

\[
 \boxed{
 \int_0^\infty\mathcal J_u[\Gamma]\,d\sigma(u)
 =-2\ell_\sigma(C_\Gamma^\circ).}
 \tag{10e}
\]

#### Proof

It is enough to prove the assertion for one row and then sum.  Let

\[
 p=K|r|^2,
 \qquad
 g=p-\frac{\langle p,K\rangle_2}{\|K\|_2^2}K.
 \tag{10f}
\]

Then

\[
 W_r^\circ(u)
 =\mathrm{Re}\,\int_{\mathbb R}g(x)K(x-u)\,dx
 \tag{10g}
\]

is the normalized cross-correlation of \(g\) with \(K\).  Apply the
polarized completed Weil autocorrelation formula with the same spatial and
prime cutoffs on its two entries.  Its physical side is
\(-2\ell_\sigma(W_r^\circ)\).  Its zero side contains the factor
\(\widehat K\) at every nontrivial zero.  Since

\[
 \widehat K(z)=\Xi(z),
 \tag{10h}
\]

that zero side vanishes identically.  Removing the common cutoffs is
legitimate because (10g) has two vanishing jets at zero and both factors
have double-exponential spatial decay.  Hence
\(\ell_\sigma(W_r^\circ)=0\).

Equivalently, this is the physical-side content of the full radical
identity \(QW(K,g)=0\), applied only after the common autocorrelation
subtraction has made each term admissible.  Summing over the rows proves
(10d).  Finally, (6), (7), and (10b) give

\[
 \mathcal J_u[\Gamma]
 =2\{W_\Gamma^\circ(u)-C_\Gamma^\circ(u)\},
\]

and (10e) follows.  \(\square\)

This answers a possible cutoff ambiguity: the diagonal term does pair to
zero, but only after the radical autocorrelation is subtracted jointly from
both terms.  Pairing \(W_\Gamma\) or \(C_\Gamma\) separately without this
common subtraction is not defined.

### Corollary 3 — Bochner form of every heat-row defect

Assume \(C_\Gamma(0)>0\) and put

\[
 \Phi_\Gamma(u)=\frac{\mathrm{Re}\,C_\Gamma(u)}{C_\Gamma(0)}.
 \tag{10i}
\]

Then \(\Phi_\Gamma\) and \(\chi_K\) are normalized even
positive-definite functions, and

\[
 \boxed{
 \int_0^\infty\mathcal J_u[\Gamma]\,d\sigma(u)
 =-2C_\Gamma(0)\,
   \ell_\sigma(\Phi_\Gamma-\chi_K).}
 \tag{10j}
\]

With the Fourier convention
\(\widehat f(\xi)=\int f(x)e^{-i\xi x}\,dx\), their Bochner probability
measures are

\[
 \boxed{
 \begin{aligned}
 d\beta_\Gamma(\xi)
 &=\frac{\sum_j\gamma_j|\widehat{Kr_j}(\xi)|^2}
         {2\pi C_\Gamma(0)}\,d\xi,\\
 d\beta_K(\xi)
 &=\frac{|\widehat K(\xi)|^2}
         {2\pi C_K(0)}\,d\xi.
 \end{aligned}}
 \tag{10k}
\]

#### Proof

Positive definiteness follows from (10), and normalization follows from
the value at zero.  Formula (10j) is (10e) divided by the common value
in (6).  Plancherel gives (10k).  \(\square\)

Thus the strongest consequence of scalar heat-profile geometry is an exact
ordering problem on a highly constrained family of Bochner measures:

\[
 \int\mathcal J_u[\Gamma]\,d\sigma(u)\geq0
 \quad\Longleftrightarrow\quad
 \ell_\sigma(\Phi_\Gamma-\chi_K)\leq0.
 \tag{10l}
\]

This is a genuine simplification: the nonstationary diagonal convolution
has disappeared completely.  It is not yet a sign theorem.  Completed Weil
positivity on autocorrelations is false under an off-line quartet, and a
hypothetical subthreshold mean-periodic heat mode produces precisely an
admissible \(\Phi_\Gamma\) for which the direction in (10l) is reversed.

## 4. Exact heat evolution of the profile

On the shorted complement put

\[
 A=L|_{\mathscr C},
 \qquad S=A+\frac12I,
 \qquad
 \Gamma_t=e^{-tS/2}Ve^{-tS/2},
 \tag{11}
\]

where \(V\) is the faithful positive trace-class boost of 106.103.  Let
\(B_u=D_u^*D_u\) denote the positive displacement-form operator, so that

\[
 \mathcal J_u[\Gamma_t]=\mathrm{Tr}(B_u\Gamma_t).
 \tag{12}
\]

All identities in this section are first read on a finite translation-smooth
hybrid row.  Heat-core approximation then gives the corresponding closed
form identities.

Let

\[
 d\nu_+(v)=\frac{e^{-v/2}}{1-e^{-2v}}\,dv
 +\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
       \delta_{\log n}(dv).
 \tag{13}
\]

In the weak-form sense,

\[
 A=\int_0^\infty B_v\,d\nu_+(v).
 \tag{14}
\]

### Theorem 4 — The scalar heat profile is not a closed state variable

For every displacement for which the hybrid row is in the common product
domain,

\[
 \boxed{
 \partial_tJ_t(u)
 =-\frac12J_t(u)
 -\int_0^\infty
   \mathrm{Re}\,\mathrm{Tr}
      (\Gamma_tB_vB_u)\,d\nu_+(v).}
 \tag{15}
\]

#### Proof

The heat state satisfies

\[
 \Gamma_t'=-\frac12(S\Gamma_t+\Gamma_tS).
 \tag{16}
\]

Differentiate (12), use trace cyclicity on the hybrid row, and substitute
\(S=A+I/2\):

\[
 \partial_tJ_t(u)
 =-\frac12J_t(u)
  -\frac12\mathrm{Tr}
       \{\Gamma_t(AB_u+B_uA)\}.
 \tag{17}
\]

The last trace is twice its real part.  Formula (14) gives (15).  \(\square\)

The mixed quantity in (15) is a two-displacement, three-point amplitude.
It is not determined by the diagonal values \(J_t(u)\).  This loss is
already visible in dimension two.  The positive matrices

\[
 M_\pm=\frac12
 \begin{pmatrix}1&\pm r\\ \pm r&1\end{pmatrix},
 \qquad
 H=\begin{pmatrix}1&c\\c&1\end{pmatrix},
 \qquad 0<r,c<1,
 \tag{18}
\]

have the same diagonal, while

\[
 \mathrm{Tr}(HM_\pm)=1\pm cr.
 \tag{19}
\]

Thus positivity and the complete diagonal profile cannot reconstruct the
mixed phase seen by the generator.  The example is only a scalar-profile
falsifier, not a counterexample to the Riemann source.

## 5. The closed variable is the source covariance

Let

\[
 \mathcal G=U_AA^{1/2}:\mathscr C\longrightarrow\mathscr H_{\rm src}
 \tag{20}
\]

be the complete ordinary-prime--Gamma gradient after exact radical
shorting, and put

\[
 H=\mathcal G\mathcal G^*,
 \qquad
 M_t=\mathcal G\Gamma_t\mathcal G^*.
 \tag{21}
\]

The covariance \(M_t\) retains the off-diagonal phases between distinct
prime powers, fractional theta residues, central crossings and Gamma
displacements.

### Theorem 5 — Closed noncommutative heat equation

On the source-gradient closure,

\[
 \boxed{
 M_t'=-\frac12M_t-\frac12(HM_t+M_tH).}
 \tag{22}
\]

Moreover,

\[
 \boxed{
 \mathrm{Tr}\,M_t=\mathrm{Tr}(A\Gamma_t),
 \qquad
 \mathrm{Tr}(HM_t)=\mathrm{Tr}(A^2\Gamma_t).}
 \tag{23}
\]

#### Proof

Functional calculus in the polar decomposition gives the intertwining
relations

\[
 \mathcal GA=H\mathcal G,
 \qquad
 A\mathcal G^*=\mathcal G^*H
 \tag{24}
\]

on the natural domains.  Apply \(\mathcal G\) and \(\mathcal G^*\) to
(16) and use (24).  This gives (22).  Trace cyclicity gives (23).  \(\square\)

Hence heat localization does produce a closed evolution, but only before
the phase covariance is collapsed to its displacement diagonal.

## 6. The exact first-versus-second source budget

Put

\[
 Z(t)=\mathrm{Tr}\,\Gamma_t,
 \qquad
 R(t)=\frac{\mathrm{Tr}(A\Gamma_t)}{Z(t)},
 \qquad
 \alpha=\inf\sigma(A).
 \tag{25}
\]

Let \(\mathbb P_t\) be the heat-tilted spectral probability measure of
106.103 and write

\[
 \mathrm{Var}_t(A)
 =\frac{\mathrm{Tr}(A^2\Gamma_t)}{Z(t)}-R(t)^2.
 \tag{26}
\]

The exact Rayleigh flow is

\[
 R'(t)=-\mathrm{Var}_t(A),
 \qquad R(t)\downarrow\alpha.
 \tag{27}
\]

Integrating (27) gives the following sharpened form of the heat criterion.

### Theorem 6 — Dissipation-budget equivalence

For every \(t>0\),

\[
 \boxed{
 \alpha-\frac12
 =\frac{\displaystyle\int_0^\infty J_t(u)\,d\sigma(u)}{Z(t)}
  -\int_t^\infty\mathrm{Var}_s(A)\,ds.}
 \tag{28}
\]

Consequently the following are equivalent.

1. \(A\geq\frac12I\).
2. For one heat time \(t>0\), inequality (2) holds.
3. For every heat time \(t>0\), inequality (2) holds.

#### Proof

The signed source identity of 106.102 gives

\[
 \frac{\int J_t\,d\sigma}{Z(t)}=R(t)-\frac12.
 \tag{29}
\]

Equation (27) gives

\[
 R(t)-\alpha
 =\int_t^\infty\mathrm{Var}_s(A)\,ds.
 \tag{30}
\]

Subtract (30) from (29) to obtain (28).  The equivalences follow because
the left side of (28) is independent of \(t\).  \(\square\)

The first term in (28) is the literal signed prime--Gamma--polar source.
The variance is a second-order source quantity.  By (23),

\[
 \mathrm{Var}_t(A)
 =\frac{\mathrm{Tr}(HM_t)}{Z(t)}
  -\left(\frac{\mathrm{Tr}\,M_t}{Z(t)}\right)^2.
 \tag{31}
\]

Thus the generalized von Mangoldt coefficient
\(j_2=\delta\Lambda+\Lambda*\Lambda\geq0\) enters the first term of
(31) only as part of the complete operator product \(H M_t\).  Its scalar
coefficient positivity does not compare the integrated variance with the
signed first source in (28).

## 7. Effect of theta residue Poisson duality

The grouped theta-character construction of 106.108 replaces the complete
gradient by

\[
 \widetilde{\mathcal G}=W\mathcal G,
 \tag{32}
\]

where \(W\) is an isometry retaining the divisible, fractional, central
and Gamma fibers.  Therefore

\[
 \widetilde H=WHW^*,
 \qquad
 \widetilde M_t=WM_tW^*.
 \tag{33}
\]

It follows exactly that

\[
 \mathrm{Tr}\,\widetilde M_t=\mathrm{Tr}\,M_t,
 \qquad
 \mathrm{Tr}(\widetilde H\widetilde M_t)
 =\mathrm{Tr}(HM_t).
 \tag{34}
\]

Hence the nonzero modular residues do impose phase relations on the full
covariance, but their exact Fourier--Poisson implementation is a source
gauge change.  It preserves both sides of the dissipation budget.  A proof
must use a new inequality between the character blocks; the modular
identity alone cannot provide it.

## 8. Exact subthreshold stress test

If \(\alpha<1/2\), then (28) reads

\[
 \boxed{
 \frac{\int J_t\,d\sigma}{Z(t)}
 -\int_t^\infty\mathrm{Var}_s(A)\,ds
 =-\left(\frac12-\alpha\right)<0}
 \tag{35}
\]

for every \(t>0\).  If the bottom is an isolated eigenvalue, heat
concentration additionally gives

\[
 \frac{\int J_t\,d\sigma}{Z(t)}\longrightarrow\alpha-\frac12,
 \qquad
 \int_t^\infty\mathrm{Var}_s(A)\,ds\longrightarrow0.
 \tag{36}
\]

Thus heat smoothing does not average away a subthreshold mode.  It removes
the higher spectral variance and exposes its fixed negative signed-source
margin.  Equations (35)--(36) hold in the finite subthreshold model of
106.99 as well, so no argument based only on covariance positivity or on
the Lyapunov flow (22) can prove the desired direction.

There is an equally sharp Bochner stress test.  If \(Aq=\alpha q\),
\(\|q\|_{\mu_K}=1\), and \(0<\alpha<1/2\), then Corollary 3 applied to
\(\Gamma=|q\rangle\langle q|\) gives

\[
 \boxed{
 \ell_\sigma(\Phi_q-\chi_K)
 =\frac{\frac12-\alpha}{2\|Kq\|_2^2}>0.}
 \tag{37}
\]

For every radical row \(Aq=q/2\), the same expression is exactly zero.
Thus normalized positive definiteness and exact radical saturation still
permit the forbidden sign in a subthreshold mean-periodic mode.  A closing
Bochner argument must use a placement property of the actual heat-evolved
measures \(\beta_{\Gamma_t}\), not merely their positivity or total mass.

## 9. Result and next theorem

Proved here:

* the exact convolution--autocorrelation structure (7)--(9) of every heat
  displacement profile;
* positive definiteness of its autocorrelation component;
* the cutoff-safe annihilation (10d) of the complete diagonal convolution;
* the exact Bochner reduction (10j)--(10k);
* the exact nonclosed scalar evolution (15);
* the closed source-covariance equation (22);
* the exact dissipation budget (28);
* invariance of that budget under the full grouped theta-character
  amplitude;
* the fixed-margin subthreshold falsifier (35).

The physical surplus is not proved here.  In the heat/hybrid coordinate,
the remaining arithmetic theorem can now be stated without auxiliary
losses:

> **Joint source dissipation lemma.**  For the literal ordinary-prime,
> fractional-theta, central, Gamma and polar source covariance, prove at
> one heat time that
> \[
>  \int_t^\infty
>  \left\{
>   \frac{\mathrm{Tr}(HM_s)}{Z(s)}
>   -\left(\frac{\mathrm{Tr}\,M_s}{Z(s)}\right)^2
>  \right\}ds
>  \leq
>  \frac{\displaystyle\int_0^\infty J_t(u)\,d\sigma(u)}{Z(t)}.
> \]

This formulation shows exactly what extra information the all-order theta
hierarchy would have to supply: a quantitative comparison of the complete
off-diagonal second source covariance with the signed first source.  Raw
moment positivity, a scalar profile estimate, or a unitary residue
reparameterization does not imply it.
