# 106.154 — Cauchy dilation and global polarized descent of the prime modules

## 1. Purpose

Document 106.153 constructed, for every prime \(p\), a polarized degree-one
coefficient module

\[
 \mathcal V_p^1=L^2(\mathbb T,\mu_{p^{-1/2}};\mathbb R^2)
\]

whose normalized monodromy has moments \(p^{-|k|/2}\).  The modules were
locally positive but were not yet realized inside one global coefficient
object.  This document constructs such an object.  The construction uses
only the convolution identity of the Poisson measures and the standard
stationary dilation of the resulting Markov semigroup.  No zeta zero and no
Weil positivity assertion enters.

The outcome is a single real Hilbert space carrying:

* a nondegenerate alternating form \(\Omega\);
* a compatible complex structure \(J\);
* a positive metric \(g=\Omega(\cdot,J\cdot)\);
* a deterministic one-parameter flow \(F_t\) with
  \(\Omega(F_tu,F_tv)=e^t\Omega(u,v)\);
* isometric polarized embeddings of every \(\mathcal V_p^1\);
* one finite von Neumann algebra containing every local prime algebra and
  reproducing all literal coefficients \(p^{-|k|/2}\).

This completes the global descent of the **coefficient modules**.  It does
not identify the resulting Hilbert object with the cyclic-homology
\(H^1\) of Connes--Consani--Marcolli.  That comparison is treated in
Section 8.

## 2. The Poisson convolution semigroup

For \(t\geq0\), let \(\nu_t\) be the probability measure on
\(\mathbb T=\mathbb R/2\pi\mathbb Z\) with Fourier coefficients

\[
 \widehat\nu_t(k)=e^{-|k|t/2},\qquad k\in\mathbb Z.              \tag{1}
\]

Thus \(\nu_t=\mu_{e^{-t/2}}\), in the notation of 106.153.  Fourier
coefficients give

\[
 \nu_t*\nu_u=\nu_{t+u}.                                        \tag{2}
\]

The convolution operators \(P_tf=f*\nu_t\) form the symmetric Markov
semigroup \(P_t=e^{-t|D|/2}\) on \(L^2(\mathbb T)\).

## 3. The stationary two-sided dilation

Let

\[
 (\Omega_{\rm path},\mathscr F,\mathbf P,(X_t)_{t\in\mathbb R})
\]

be the stationary two-sided circular Cauchy process: \(X_t\) is Haar
distributed on \(\mathbb T\), the increments are stationary and independent,
and

\[
 \mathrm{Law}(X_{t+u}-X_t)=\nu_u,\qquad u\geq0.            \tag{3}
\]

Existence follows directly from Kolmogorov consistency: for ordered times
\(t_0<\cdots<t_n\), take \(X_{t_0}\) Haar and the successive increments
independent with laws \(\nu_{t_j-t_{j-1}}\).  Equation (2) proves consistency
under deletion of an intermediate time.  Translation of all times preserves
these finite-dimensional distributions, so the path shift

\[
 (\sigma_t\omega)(s)=\omega(s+t)                               \tag{4}
\]

preserves \(\mathbf P\).

Write

\[
 c_t(\omega)=X_t(\omega)-X_0(\omega)\in\mathbb T.               \tag{5}
\]

The increments obey the cocycle identity

\[
 c_{t+u}(\omega)=c_t(\omega)+c_u(\sigma_t\omega).               \tag{6}
\]

## 4. The global polarized Hilbert module

Let

\[
 \mathscr K=L^2(\Omega_{\rm path},\mathbf P;\mathbb R^2).
\]

On the standard real plane use

\[
 E=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 J=-E=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Define, for \(f,h\in\mathscr K\),

\[
 \begin{aligned}
 \Omega_{\mathscr K}(f,h)
   &=\int f(\omega)^{\mathsf T}E h(\omega)\,d\mathbf P(\omega),\\
 (J_{\mathscr K}f)(\omega)&=Jf(\omega),\\
 g_{\mathscr K}(f,h)
   &=\Omega_{\mathscr K}(f,J_{\mathscr K}h)
     =\int f(\omega)^{\mathsf T}h(\omega)\,d\mathbf P(\omega).
                                                               \tag{7}
 \end{aligned}
\]

Thus \(\Omega_{\mathscr K}\) is alternating and nondegenerate,
\(J_{\mathscr K}^2=-I\), and \(g_{\mathscr K}\) is the positive Hilbert
metric.

For \(t\in\mathbb R\), define

\[
 (V_tf)(\omega)=R_{c_t(\omega)}f(\sigma_t\omega),               \tag{8}
\]

where \(R_\theta\) is rotation through \(\theta\).

### Theorem 4.1 — Deterministic unitary dilation and weight-one flow

The operators \(V_t\) form a strongly continuous orthogonal group on
\(\mathscr K\), commute with \(J_{\mathscr K}\), and preserve
\(\Omega_{\mathscr K}\).  Consequently

\[
 F_t:=e^{t/2}V_t                                                   \tag{9}
\]

is a group of weight-one symplectic similitudes:

\[
 \boxed{
 \begin{aligned}
 \Omega_{\mathscr K}(F_tf,F_th)&=e^t\Omega_{\mathscr K}(f,h),\\
 F_tJ_{\mathscr K}&=J_{\mathscr K}F_t,\\
 g_{\mathscr K}(F_tf,F_th)&=e^t g_{\mathscr K}(f,h).
 \end{aligned}}                                                  \tag{10}
\]

If \(\Theta\) is the generator of \(F_t\), then on its natural domain

\[
 \boxed{\Theta^\dagger+\Theta=I.}                               \tag{11}
\]

#### Proof

Using (6), angle addition, and the group law of the shifts,

\[
 \begin{aligned}
 V_tV_uf(\omega)
 &=R_{c_t(\omega)}R_{c_u(\sigma_t\omega)}
     f(\sigma_u\sigma_t\omega)\\
 &=R_{c_{t+u}(\omega)}f(\sigma_{t+u}\omega)
 =V_{t+u}f(\omega).
 \end{aligned}
\]

The shift preserves \(\mathbf P\) and rotations preserve the Euclidean
metric and \(E\), so \(V_t\) is orthogonal and symplectic.  Rotations commute
with \(J\), hence \(V_tJ_{\mathscr K}=J_{\mathscr K}V_t\).  Strong
continuity follows first on bounded cylinder functions from stochastic
continuity of the Cauchy process and then on all of \(\mathscr K\) by
density and unitarity.  Multiplication by (e^{t/2}) proves (10).  Writing
(F_t=e^{t/2}e^{tA}) with \(A^\dagger=-A\) gives
\(\Theta=\frac12I+A\), and therefore (11). \(\square\)

## 5. Isometric descent of every prime module

For (t>0), define

\[
 \iota_t:L^2(\mathbb T,\nu_t;\mathbb R^2)\longrightarrow\mathscr K,
 \qquad
 (\iota_ta)(\omega)=a(c_t(\omega)).                             \tag{12}
\]

### Theorem 5.1 — Simultaneous polarized embeddings

Each \(\iota_t\) is an isometry preserving \(\Omega,J,g\).  At
\(t=\log p\), its source is exactly the local module \(\mathcal V_p^1\)
of 106.153.  Hence

\[
 \boxed{
 \iota_{\log p}:\mathcal V_p^1\hookrightarrow\mathscr K
 }
                                                                    \tag{13}
\]

gives a simultaneous polarized descent of all ordinary prime modules into
one object.

#### Proof

By (3) with initial time (0), (c_t) has law \(\nu_t\).  Therefore

\[
 \|\iota_ta\|_{\mathscr K}^2
 =\mathbf E\,|a(c_t)|^2
 =\int_{\mathbb T}|a(\theta)|^2d\nu_t(\theta).
\]

The same change of variables proves preservation of \(\Omega\) and \(g\),
while \(J\) is pointwise constant and commutes with \(\iota_t\).  Finally
\(\nu_{\log p}=\mu_{p^{-1/2}}\). \(\square\)

The images for different primes need not be orthogonal and are not declared
to be independent summands.  They are subspaces generated by different
increments of the same stationary process.  This is the required
non-disjoint gluing at coefficient level.

### Theorem 5.2 — Joint observability of the prime increments

Let \(G=\mathrm{span}_{\mathbb Z}\{\log p:p\text{ prime}\}
=\log\mathbb Q_+^\times\).  Let \(\mathscr A_{\rm pr}\) be the completed
sigma-algebra generated by all time translates

\[
 c_{\log p}\circ\sigma_g,qquad p\text{ prime},\quad g\in G.  \tag{14}
\]

Then \(G\) is dense in \(\mathbb R\), and \(\mathscr A_{\rm pr}\) is the
full increment sigma-algebra

\[
 \mathscr A_{\rm inc}=\sigma(c_t:t\in\mathbb R).              \tag{15}
\]

Consequently, the closed algebra generated by the prime observation
spaces and their translates is all of
\(L^2(\Omega_{\rm path},\mathscr A_{\rm inc},\mathbf P;\mathbb R^2)\).

#### Proof

Unique factorization identifies \(G\) with \(\log\mathbb Q_+^\times\),
which is dense because \(\mathbb Q_+^\times\) is dense in
\(\mathbb R_+^\times\).  From the cocycle identity,

\[
 c_u\circ\sigma_g=c_{g+u}-c_g.                                \tag{16}
\]

Products and translates of the generators in (14), followed by finite
concatenation of increments, therefore recover \(c_g\) for every
\(g\in G\); negative increments use
\(c_{-u}=-c_u\circ\sigma_{-u}\).  For arbitrary \(t\in\mathbb R\), choose
\(g_j\in G\) with \(g_j\to t\).  Stochastic continuity gives
\(c_{g_j}\to c_t\) in probability.  Passing to an almost-surely
convergent subsequence shows that \(c_t\) is measurable with respect to
the completion of \(\mathscr A_{\rm pr}\).  Hence
\(\mathscr A_{\rm inc}\subseteq\mathscr A_{\rm pr}\); the reverse
inclusion is immediate from (16).  The final assertion follows from the
density of bounded cylinder functions in \(L^2\). \(\square\)

The only path coordinate not seen by increments is the independent Haar
origin \(X_0\).  It is the generic degree-zero coordinate, not an
unobserved prime mode.  Thus there is no coefficient-level loss of
information in passing from all real times to the prime orbit lengths.

## 6. One global finite algebra and all von Mangoldt moments

Complexify the matrix coefficients and set

\[
 \mathscr M=L^\infty(\Omega_{\rm path},\mathbf P)
             \bar\otimes M_2(\mathbb C),
 \qquad
 \tau(A)=\frac12\mathbf E\,\mathrm{Tr}_2A.                \tag{17}
\]

For \(t\geq0\), let

\[
 U_t(\omega)=R_{c_t(\omega)}\in\mathscr M.                      \tag{18}
\]

### Theorem 6.1 — Literal arithmetic moments in one polarized algebra

For every \(k\in\mathbb Z\),

\[
 \boxed{\tau(U_t^k)=e^{-|k|t/2}.}                               \tag{19}
\]

In particular,

\[
 \boxed{
 (\log p)\tau(U_{\log p}^k)=\frac{\log p}{p^{k/2}},
 \qquad p\ {\rm prime},\ k\geq1.}                              \tag{20}
\]

#### Proof

The normalized matrix trace of (R_{c_t}^k) is (\cos(kc_t)).  Since
(c_t) has law \(\nu_t\), (1) gives

\[
 \tau(U_t^k)=\mathbf E\cos(kc_t)=e^{-|k|t/2}.
\]

Specializing \(t=\log p\) proves (20). \(\square\)

Therefore the full prime channel is one odd graded normal trace:

\[
 -\sum_p\sum_{k\geq1}(\log p)\tau(U_{\log p}^k)
       \widehat h(k\log p)
 =-\sum_p\sum_{k\geq1}\frac{\log p}{p^{k/2}}
       \widehat h(k\log p).                                    \tag{21}
\]

## 7. What has now been constructed

Equations (7)--(13) construct the previously missing global compatibility
of the local polarizations:

\[
 \{(\mathcal V_p^1,\Omega_p,J_p,g_p)\}_p
 \longrightarrow
 (\mathscr K,\Omega_{\mathscr K},J_{\mathscr K},g_{\mathscr K},F_t).
                                                               \tag{22}
\]

This construction is prior to the explicit formula.  The only arithmetic
input is the sampling set \(t=\log p\); the weight (p^{-k/2}) follows from
the transition law of the single process.  Positivity is the pointwise
Euclidean identity (7), not an estimate involving zeta zeros.

## 8. Comparison with the CCM cyclic \(H^1\)

CCM define (H^1\(\mathbb A_\mathbb Q/\mathbb Q^*,C_\mathbb Q\)) as cyclic
homology of the cokernel of the adelic restriction morphism.  The scaling
action on that object has a distributional trace containing every
nontrivial zero, including a hypothetical off-line zero.  The object
\(\mathscr K\) above is a positive Hilbert module with a unitary normalized
flow \(V_t\), so its generator is automatically skew-adjoint.

There is therefore one precise comparison theorem still required:

\[
 \boxed{
 \mathrm{Comp}:H^1_{\rm CCM}
   \longrightarrow H^1(\mathscr K,d_{\rm ar})
 \quad\text{is an equivariant isomorphism},}                    \tag{23}
\]

where \(d_{\rm ar}\) must be a geometrically defined differential on the
global coefficient object.  Neither \(d_{\rm ar}\) nor (23) is supplied by
the Markov dilation alone.

This is not a cosmetic qualification.  Completing the elementary
restriction cokernel in a weighted \(L^2\) norm cannot define the desired
cohomology: on the Mellin side its range is multiplication by a completed
Euler function which is nonzero almost everywhere on the critical line,
so the Hilbert closure is the whole ambient \(L^2\) space and the quotient
is zero.  The nontrivial cohomology must therefore be derived before Hilbert
completion, exactly as in the cyclic-module construction, and only then
receive the polarization from (7).

Thus the next construction is sharply determined: define a derived
differential \(d_{\rm ar}\) on the Cauchy-dilated rooted-divisor complex,
prove that its reduced degree-one cohomology realizes the target in (23),
and prove that the forms (7) descend through \(d_{\rm ar}\).  No further local-prime
polarization is missing.

## 9. Status

Proved here:

* existence of one stationary path-space object containing every prime
  Poisson module;
* a deterministic unitary dilation of the Markov correspondence;
* a global alternating form, compatible complex structure, and positive
  metric;
* the exact weight-one scaling law and generator identity
  \(\Theta^\dagger+\Theta=I\);
* simultaneous polarized embeddings of all prime modules;
* one finite normal trace reproducing every literal von Mangoldt weight.

Not proved here:

* a differential \(d_{\rm ar}\) whose cohomology is the CCM cokernel;
* the comparison isomorphism (20);
* the global Lefschetz theorem on this polarized derived complex;
* RH.
