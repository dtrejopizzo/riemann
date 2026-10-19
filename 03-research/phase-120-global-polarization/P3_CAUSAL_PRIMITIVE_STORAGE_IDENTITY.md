# Causal primitive storage identity

Status: exact finite-horizon state identity on the compact-potential core.
It does not yet prove positivity.  It replaces the abstract storage request
by a literal bulk-plus-terminal formula and exposes a quarter-shift
cancellation in the first Gamma state.

## 1. Causal Gamma states

Put

\[
 \alpha_n=n+\tfrac14,\qquad \lambda_n=2\alpha_n=2n+\tfrac12,
 \qquad D={d\over dt}.
\]

For a profile \(F\) supported in \((-T,T)\), let \(z_n\) be the causal
solution

\[
 (D+\lambda_n)z_n=F,\qquad z_n(-T)=0,                 \tag{1.1}
\]

and put \(y_n=\alpha_n^{-1}Dz_n\).  Its transfer function is

\[
 {y_n(s)\over F(s)}={1\over\alpha_n}{s\over s+2\alpha_n},
\]

so the parallel sum of these cells is exactly the positive-real Gamma
impedance \(H_\Gamma\) of the effective Herglotz--Gamma gate.

Since \(F=Dz_n+2\alpha_nz_n\), direct integration gives

\[
 \boxed{
 \operatorname{Re}\int_{-T}^{T}F\overline{y_n}\,dt
 ={1\over\alpha_n}\int_{-T}^{T}|Dz_n|^2dt
   +|z_n(T)|^2-|z_n(-T)|^2 .}                       \tag{1.2}
\]

Thus the canonical Gamma storage is \(|z_n|^2\), with no Riccati equation
and no coefficient chosen from the Weil form.  Summing (1.2), and using the
causal initial condition, yields

\[
 \operatorname{Re}\langle F,H_\Gamma(D)F\rangle_{[-T,T]}
 =\mathcal D_\Gamma(F)+\mathcal S_\Gamma^+(F),       \tag{1.3}
\]

where

\[
 \mathcal D_\Gamma(F)
 =\sum_{n\ge0}{1\over\alpha_n}\|Dz_n\|_{L^2(-T,T)}^2,
 \qquad
 \mathcal S_\Gamma^+(F)=\sum_{n\ge0}|z_n(T)|^2.    \tag{1.4}
\]

## 2. Causal prime-delay states

For an active prime put

\[
 a_p=\log p,\qquad r_p=p^{-1/2},
\]

and let \(x_p\) be the causal solution

\[
 x_p(t)-r_px_p(t-a_p)=F(t),\qquad x_p(t)=0\quad(t<-T). \tag{2.1}
\]

Define

\[
 y_p(t)=x_p(t)+r_px_p(t-a_p).                         \tag{2.2}
\]

Then \(y_p/F=(1+c_p)/(1-c_p)\), with
\(c_p(s)=r_pe^{-a_ps}\).  Pointwise cancellation of the cross terms gives

\[
 \operatorname{Re}\{F\overline{y_p}\}
 =|x_p(t)|^2-r_p^2|x_p(t-a_p)|^2.                    \tag{2.3}
\]

For \(0<a_p<2T\), integration and a change of variables give the exact
finite-horizon balance

\[
 \boxed{
 \operatorname{Re}\int_{-T}^{T}F\overline{y_p}\,dt
 =(1-r_p^2)\int_{-T}^{T-a_p}|x_p(t)|^2dt
   +\int_{T-a_p}^{T}|x_p(t)|^2dt .}                 \tag{2.4}
\]

Write the two nonnegative terms as

\[
 \mathcal D_p(F)=(1-p^{-1})\|x_p\|_{L^2(-T,T-a_p)}^2,
 \qquad
 \mathcal S_p^+(F)=\|x_p\|_{L^2(T-a_p,T)}^2.       \tag{2.5}
\]

The second term is the literal outgoing delay-line storage.  It is not a
free boundary complement.

## 3. Exact global causal balance

The signed impedance is

\[
 Z_T=H_\Gamma+\theta_T-m_0-\sum_{p\in S_T}a_pH_p.
\]

Combining (1.3) and (2.4) gives, for every compactly supported \(F\),

\[
\boxed{
\begin{aligned}
 \operatorname{Re}\langle F,Z_T(D)F\rangle_{[-T,T]}
 ={}&\mathcal D_\Gamma(F)+(\theta_T-m_0)\|F\|^2\\
 &-\sum_{p\in S_T}a_p\mathcal D_p(F)\\
 &+\mathcal S_\Gamma^+(F)
   -\sum_{p\in S_T}a_p\mathcal S_p^+(F).
\end{aligned}}                                             \tag{3.1}
\]

This is the requested storage calculation before any positivity comparison.
It shows exactly why separate passivity is insufficient: the arithmetic
bulk and terminal storages occur with the opposite orientation.  A global
square must jointly complete the two signed lines in (3.1); there is no
unspecified Maslov remainder left.

## 4. Quarter-shift primitive cancellation

Now impose the primitive potential condition

\[
 F=L_0G,\qquad L_0=-D^2+\tfrac14,\qquad
 G\in C_c^\infty(-T,T).                              \tag{4.1}
\]

Let \(R_\lambda^+=(D+\lambda)^{-1}\) denote the causal resolvent.  Polynomial
division gives the operator identity

\[
 L_0=(-D+\lambda)(D+\lambda)
       -(\lambda^2-\tfrac14).                        \tag{4.2}
\]

Consequently the Gamma state has the exact primitive formula

\[
 \boxed{
 z_n=(-D+\lambda_n)G
      -(\lambda_n^2-\tfrac14)R_{\lambda_n}^+G.}      \tag{4.3}
\]

For \(n=0\), \(\lambda_0=1/2\), so the resolvent term disappears:

\[
 \boxed{z_0=(-D+\tfrac12)G,\qquad z_0(T)=0.}         \tag{4.4}
\]

This is an exact cancellation specific to the quarter twist.  For \(n\ge1\),
compact support gives the explicit terminal coordinate

\[
 z_n(T)=-(\lambda_n^2-\tfrac14)
   \int_{-T}^{T}e^{-\lambda_n(T-s)}G(s)\,ds.         \tag{4.5}
\]

Thus the Gamma terminal storage on the primitive core is the positive
Laplace-sampling form

\[
 \boxed{
 \mathcal S_{\Gamma,\mathrm{prim}}^+(G)
 =\sum_{n\ge1}(\lambda_n^2-\tfrac14)^2
   \left|\int_{-T}^{T}e^{-\lambda_n(T-s)}G(s)ds\right|^2 .} \tag{4.6}
\]

The polar Gamma mode \(n=0\) has vanished before comparison with the prime
side; it is not removed by declaring a quotient.

### Theorem 4.1 — closed Hankel kernel of the terminal Gamma storage

Put \(g_T(u)=G(T-u)\) for \(0<u<2T\).  The infinite sum in (4.6) can be
performed exactly.  If \(w=u+v\) and \(q=e^{-2w}\), define

\[
 \mathcal K_{1/4}^+(u,v)
 =4e^{-w/2}{q(q^3+31q^2+55q+9)\over(1-q)^5}.         \tag{4.7}
\]

Then

\[
 \boxed{
 \mathcal S_{\Gamma,\mathrm{prim}}^+(G)
 =\int_0^{2T}\!\int_0^{2T}
   \mathcal K_{1/4}^+(u,v)g_T(u)\overline{g_T(v)}\,du\,dv .} \tag{4.8}
\]

Indeed, with \(\lambda_n=2n+1/2\),

\[
 (\lambda_n^2-\tfrac14)^2=[2n(2n+1)]^2
 =16n^4+16n^3+4n^2,                                  \tag{4.9}
\]

and the elementary power-series identities give

\[
 \sum_{n\ge1}[2n(2n+1)]^2q^n
 ={4q(q^3+31q^2+55q+9)\over(1-q)^5}.                \tag{4.10}
\]

Formula (4.7) is a positive Hankel Gram kernel because, before summation,

\[
 \mathcal K_{1/4}^+(u,v)
 =\sum_{n\ge1}(\lambda_n^2-\tfrac14)^2
       e^{-\lambda_n u}e^{-\lambda_n v}.            \tag{4.11}
\]

Thus the terminal Gamma side is no longer an unspecified infinite bank: it
is one explicit rational Hankel form on distance from the right endpoint.

There is a second, lower-order form of the same identity.  Put

\[
 \mathcal K_0^+(u,v)
 ={e^{-\frac52(u+v)}\over1-e^{-2(u+v)}}
 =\sum_{n\ge1}e^{-\lambda_n u}e^{-\lambda_n v}.     \tag{4.12}
\]

Since

\[
 L_{0,u}e^{-\lambda_n u}
 =-(\lambda_n^2-\tfrac14)e^{-\lambda_n u},
\]

one has the exact differential factorization

\[
 \boxed{
 \mathcal K_{1/4}^+=L_{0,u}L_{0,v}\mathcal K_0^+.}  \tag{4.13}
\]

Because \(G\) is flat at the endpoints of its compact support, integration
by parts creates no boundary distribution.  Hence (4.8) is equivalently the
Gram of \(L_0G\) against the lower-order kernel (4.12).  On the prime side,
\(x_p(L_0G)=L_0x_p(G)\).  Therefore the primitive differential is now common
to both terminal banks; the remaining mismatch is between the positive
Hankel geometry (4.12) and the discrete delay-tail geometry, not between
differently typed derivatives.

### Theorem 4.2 — radial depth unification and the missing boundary sample

Fix a prime \(p\), put \(a=\log p\), \(r=p^{-1/2}\), and extend \(G\) by
zero.  For \(0<u<a\), define the finite depth series

\[
 \mathscr X_{p,T}(z,u)
 =\sum_{j\ge0}r^jG(T-u-ja)z^j.                       \tag{4.14}
\]

It is a polynomial for every \(u\), because \(G\) has compact support.  The
outgoing prime tail is its boundary value:

\[
 x_p(G)(T-u)=\mathscr X_{p,T}(1,u).                  \tag{4.15}
\]

Splitting the Laplace integral into cells \(v=u+ja\) gives, for every
\(n\ge0\),

\[
 \boxed{
 \int_0^{2T}e^{-\lambda_n v}G(T-v)\,dv
 =\int_0^a e^{-\lambda_n u}
      \mathscr X_{p,T}(p^{-2n},u)\,du .}            \tag{4.16}
\]

Indeed,

\[
 e^{-\lambda_n j a}=p^{-(2n+1/2)j}=r^jp^{-2nj},    \tag{4.17}
\]

which is exactly the coefficient in (4.14) evaluated at \(z=p^{-2n}\).
Thus the prime and Gamma terminal variables are boundary and radial samples
of one canonical depth polynomial.

The quarter cancellation now has a sharper meaning.  The missing Gamma
index \(n=0\) would evaluate

\[
 \mathscr X_{p,T}(p^0,u)=\mathscr X_{p,T}(1,u),     \tag{4.18}
\]

which is precisely the prime boundary trace, but its primitive coefficient
\(\lambda_0^2-1/4\) is zero.  Every surviving Gamma terminal coordinate has
strictly interior radius \(p^{-2n}<1\).  Therefore terminal Gamma storage
alone cannot supply a cutoff-independent boundary estimate by a radial
maximum-principle argument: the only boundary sample is exactly the mode
removed by primitivity.  A valid square must also use the interior Gamma
dissipation in (3.1).

Finally, commutation with \(L_0\) gives the physical terminal load

\[
 \mathcal S_p^+(L_0G)
 =\int_0^a\left|L_{0,u}\mathscr X_{p,T}(1,u)\right|^2du. \tag{4.19}
\]

Equations (4.16) and (4.19) put the final terminal comparison on one literal
two-variable object \(\mathscr X_{p,T}\), with no identification map left to
choose.

The same unification holds before taking the terminal trace.  For any time
\(t\), define

\[
 \mathscr X_{p,t}^{F}(z,u)
 =\sum_{j\ge0}r^jF(t-u-ja)z^j,\qquad 0<u<a.          \tag{4.20}
\]

Then the two state systems are the boundary value and radial Laplace
functionals of this one object:

\[
 \boxed{
 x_p(t)=\mathscr X_{p,t}^{F}(1,0),
 \qquad
 z_n(t)=\int_0^a e^{-\lambda_n u}
   \mathscr X_{p,t}^{F}(p^{-2n},u)du.}              \tag{4.21}
\]

Moreover

\[
 Dz_n(t)=F(t)-\lambda_nz_n(t).                      \tag{4.22}
\]

Thus both the interior dissipations and the terminal storages in (3.1) now
live on the same radial-depth field.  The missing global square is a
structured radial trace theorem for fields of the special translation form
(4.20), not an arbitrary comparison of two passive systems.

### Corollary 4.3 — the Gamma ladder is a safe-Euler-line lift

In Fourier variables the depth return has boundary character
\(r_pe^{i\tau a_p}=p^{-1/2+i\tau}\), up to the fixed Fourier-sign convention.
At the Gamma radial node it becomes

\[
 r_pp^{-2n}e^{i\tau a_p}
 =p^{-(2n+1/2)+i\tau}.                              \tag{4.23}
\]

Thus every surviving Gamma index \(n\ge1\) evaluates the same local Euler
return on the absolutely convergent vertical line
\(\operatorname{Re}s=2n+1/2\).  The absent \(n=0\) node is exactly the
critical boundary \(\operatorname{Re}s=1/2\).  The radial-depth theorem is
therefore a source-level lift from the critical boundary to safe Euler
lines, not merely a formal similarity between two sequences.

For a profile of exponential type \(T\), a vertical displacement by \(2n\)
can grow like \(e^{2nT}\), while (4.23) damps by \(p^{-2n}\).  This observation
does **not** reproduce the geometric activity condition
\(\log p<2T\): the two thresholds have different origins and must not be
identified.  It does show why shifting to the safe lines is not by itself a
bounded argument on the Paley--Wiener class.  The finitely many geometric
return factors still have to be treated in the radial trace theorem before
any safe-line limit is taken.

### Proposition 4.4 — terminal-only radial trace is impossible

Let \(0<q<1\) and let \(w_n\ge0\) satisfy
\(\sum_{n\ge1}w_nq^{2n}<\infty\).  There is no finite constant \(C\) such
that every polynomial \(P\) obeys

\[
 |P(1)|^2\le C\left(|P(0)|^2+
          \sum_{n\ge1}w_n|P(q^n)|^2\right).         \tag{4.24}
\]

Indeed, take \(P_J(z)=z^J\).  The left side is one and \(P_J(0)=0\), while

\[
 \sum_{n\ge1}w_n|P_J(q^n)|^2
 =\sum_{n\ge1}w_nq^{2nJ}\longrightarrow0           \tag{4.25}
\]

by dominated convergence.  The Gamma terminal weights in (4.6) grow only
polynomially in \(n\), so they satisfy the hypothesis for \(q=p^{-2}\).
The half-density coefficient \(r^J\) does not repair the failure: it
multiplies both the boundary value and every radial sample.

Consequently no Parseval--Green formula involving only the free coefficient
and terminal Gamma samples can close the prime boundary trace.  The required
positive differential must be genuinely mixed: it must use evolution in
\(t\), through \(Dz_n=F-\lambda_nz_n\), together with radial depth.  This
rules out a purely radial measure before any attempt to fit its moments.

### Theorem 4.5 — a single mixed transport carrier

The mixed differential is already forced by (4.20).  Direct differentiation
gives

\[
 (\partial_t+\partial_u)\mathscr X_{p,t}^{F}(z,u)=0. \tag{4.26}
\]

At the two ends of one depth cell, reindexing the series gives

\[
 \boxed{
 \mathscr X_{p,t}^{F}(z,0)
 -r_pz\,\mathscr X_{p,t}^{F}(z,a_p)=F(t).}          \tag{4.27}
\]

Introduce the half-density field

\[
 \mathscr Y_{p}^{F}(z,u,t)=e^{-u/2}
       \mathscr X_{p,t}^{F}(z,u).                   \tag{4.28}
\]

Since \(r_pe^{a_p/2}=1\), equations (4.26)--(4.27) become

\[
 \boxed{
 (\partial_t+\partial_u+\tfrac12)\mathscr Y_p^F=0,
 \qquad
 \mathscr Y_p^F(z,0,t)-z\mathscr Y_p^F(z,a_p,t)=F(t).} \tag{4.29}
\]

Thus every Frobenius cylinder and every radial Gamma sample are sections of
one explicitly defined first-order transport problem.  No boundary unitary
or defect-complement identification is left to choose.

To recover the Gamma state, set \(z=p^{-2n}\) and

\[
 Z_{p,n}(t)=\int_0^{a_p}e^{-2nu}
       \mathscr Y_p^F(p^{-2n},u,t)du.               \tag{4.30}
\]

Because \(e^{-2na_p}=p^{-2n}=z\), integration by parts in (4.29), followed
by the seam law, gives

\[
\begin{aligned}
 DZ_{p,n}
 &=\mathscr Y_p^F(z,0,\cdot)
   -z\mathscr Y_p^F(z,a_p,\cdot)
   -(2n+\tfrac12)Z_{p,n}\\
 &=F-\lambda_nZ_{p,n}.                              \tag{4.31}
\end{aligned}
\]

Comparison with the causal initial condition proves

\[
 \boxed{Z_{p,n}=z_n,}                               \tag{4.32}
\]

independently of \(p\).  This independence is the global compatibility
condition: different cell decompositions give the same Gamma state because
they are subdivisions of the same causal half-line.

Equations (4.29)--(4.32) construct the previously missing common
Gamma--Frobenius carrier.  The remaining Green calculation is no longer a
search for a coupling map; it is the computation of the positive transverse
energy of this fixed transport system after the two compact-potential
conditions are imposed.

### Theorem 4.6 — canonical return-length operator

Let \(N_z=z\partial_z\) and define on the polynomial core

\[
 \mathcal L_p=u+a_pN_z.                              \tag{4.33}
\]

Every monomial of depth \(j\) is an eigenvector with the literal traveled
length \(u+ja_p\):

\[
 \mathcal L_p\bigl(r_p^jF(t-u-ja_p)z^j\bigr)
 =(u+ja_p)r_p^jF(t-u-ja_p)z^j.                     \tag{4.34}
\]

If \(Q\) is multiplication by the source time, \((QF)(s)=sF(s)\), then

\[
 \boxed{
 \mathscr X_p^{QF}
 =(t-\mathcal L_p)\mathscr X_p^F,\qquad
 t\mathscr X_p^F-\mathscr X_p^{QF}
 =\mathcal L_p\mathscr X_p^F.}                     \tag{4.35}
\]

Thus \(\mathcal L_p\ge0\) is the exact lifted Wigner--Smith delay before
boundary compression.  Its two summands have the required provenance:
\(u\) is the continuous Gamma/half-line length and \(a_pN_z\) is the
Frobenius return length, with the grading derivative producing \(j\log p\).
This proves positivity of the un-oriented length observable.  The global
Green commutator is its **oriented** outer-minus-inner boundary combination,
so its sign does not follow yet.  What remains nontrivial is precisely the
primitive short: after coherent degree and the two Tate modes are removed,
the oriented compression must split into a positive centered variance with
no leakage.  Equation (4.35), rather than a fitted contraction, fixes the
operator on which that calculation must be performed.

### Theorem 4.7 — universal causal half-line and exact location of leakage

The apparent dependence of the length observable on \(p\) is only a choice
of cell coordinates.  Define the universal causal half-line field

\[
 \mathfrak h_F(t,\ell)=e^{-\ell/2}F(t-\ell),\qquad \ell\geq0. \tag{4.36}
\]

It obeys

\[
 (\partial_t+\partial_\ell+\tfrac12)\mathfrak h_F=0,
 \qquad \mathfrak h_F(t,0)=F(t).                   \tag{4.37}
\]

For every prime, define its \(a_p\)-cell transform by

\[
 (U_p\mathfrak h)(z,u,t)
   =\sum_{j\geq0}\mathfrak h(t,u+ja_p)z^j,
 \qquad 0\leq u<a_p.                              \tag{4.38}
\]

On the compact-source algebraic core the sum is finite, and (4.28) says
exactly

\[
 U_p\mathfrak h_F=\mathscr Y_p^F.                 \tag{4.39}
\]

Each cell chart is equipped with the inner product transported from the
universal half-line by \(U_p\).  This makes \(U_p\) unitary onto its range by
construction; it introduces no Weil-form sign and is needed only to compare
the differently sized cells without a type error.

If \(M_\ell\) denotes multiplication by return length, then

\[
 \boxed{U_pM_\ell=\mathcal L_pU_p.}               \tag{4.40}
\]

In particular, the different \(\mathcal L_p\)'s must not be added as if
they acted on one previously identified fibre: they are coordinate forms of
the single operator \(M_\ell\).  The universal formulas for the two state
banks are

\[
 \boxed{
 z_n(t)=\int_0^\infty e^{-2n\ell}\mathfrak h_F(t,\ell)d\ell,
 \qquad
 x_p(t)=\sum_{j\geq0}\mathfrak h_F(t,ja_p).}       \tag{4.41}
\]

Thus Gamma is a continuous Laplace trace of the universal half-line and a
prime is a lattice trace of that same half-line.

Put \(\theta_T=\sum_pa_p\), \(w_p=\sqrt{a_p/\theta_T}\), and define the
coherent lift into the cell charts by

\[
 j\mathfrak h=(w_pU_p\mathfrak h)_p,
 \qquad \mathcal A_T=\bigoplus_p\mathcal L_p.      \tag{4.42}
\]

Equation (4.40) gives the exact intertwining

\[
 \boxed{\mathcal A_Tj=jM_\ell.}                   \tag{4.43}
\]

Consequently the coherent universal subspace reduces the length operator:
with the transported cell inner products, \(j\) is an isometry and, if
\(P_{\rm coh}=jj^*\), then

\[
 \boxed{(I-P_{\rm coh})\mathcal A_Tj=0.}          \tag{4.44}
\]

There is therefore **no coherent-degree leakage in the interior length
operator**.  The former formal operator variance of the
\(\mathcal L_p\)'s was ill-typed before the cell charts were identified; after
the canonical identification (4.40), that variance is identically zero.

The support and Tate assertions are equally transparent on the universal
field.  Source time is \(S=t-M_\ell\), hence

\[
 [S,M_\ell]=0,\qquad [D_t,M_\ell]=0.               \tag{4.45}
\]

It follows that the source-support projection
\(\mathbf1_{[-T,T]}(S)\) and the primitive operator
\(L_{0,S}=-D_t^2+1/4\) reduce \(M_\ell\).  Thus support, the two Tate
conditions, and coherent degree all have zero interior leakage.

The first nonzero column can occur only after the \(p\)-dependent lattice
trace in (4.41).  Make it explicit by defining, with all functions extended
by zero to common copies of \(L^2(-T,T)\),

\[
 \begin{aligned}
 B_p\mathfrak h(t)&=\sum_{j\geq0}\mathfrak h(t,ja_p),\\
 E_{p,T}\mathfrak h&=\bigl(
  \sqrt{1-p^{-1}}\,\mathbf1_{[-T,T-a_p]}B_p\mathfrak h,
  \mathbf1_{[T-a_p,T]}B_p\mathfrak h\bigr).
 \end{aligned}                                    \tag{4.46}
\]

For \(\mathfrak h=\mathfrak h_F\), equations (2.5) and (4.41) give

\[
 \|E_{p,T}\mathfrak h_F\|^2
   =\mathcal D_p(F)+\mathcal S_p^+(F).             \tag{4.47}
\]

Let

\[
 \overline E_T=\sum_pw_p^2E_{p,T},\qquad
 \mathcal K_T^{\rm seam}\mathfrak h
   =\bigl(w_p(E_{p,T}-\overline E_T)\mathfrak h\bigr)_p. \tag{4.48}
\]

Weighted ANOVA, now on the common output space and with no commutativity
assumption, gives the exact boundary decomposition

\[
 \boxed{
 \sum_pa_p\|E_{p,T}\mathfrak h\|^2
 =\theta_T\|\overline E_T\mathfrak h\|^2
  +\theta_T\|\mathcal K_T^{\rm seam}\mathfrak h\|^2,} \tag{4.49}
\]

and hence

\[
 \boxed{
 (\mathcal K_T^{\rm seam})^*\mathcal K_T^{\rm seam}
 =\sum_pw_p^2E_{p,T}^*E_{p,T}-\overline E_T^*\overline E_T\succeq0.} \tag{4.50}
\]

The same column has a parameter-free pairwise square:

\[
 \boxed{
 \theta_T\|\mathcal K_T^{\rm seam}\mathfrak h\|^2
 ={1\over2\theta_T}\sum_{p,q}a_pa_q
   \|(E_{p,T}-E_{q,T})\mathfrak h\|^2.}            \tag{4.51}
\]

Thus the transverse output is exactly relative prime-cell phase: it
vanishes for one cell structure and measures only disagreements between the
\(\log p\) and \(\log q\) lattice traces.  Formula (4.51) is already the
square of the leakage; no square root or fitted completion is required.

This proves and locates the leakage: it is not a bulk, support, Tate, or
degree defect.  It is precisely the positive variance of the inequivalent
prime lattice traces of one universal causal half-line.  Keeping
\(\mathcal K_T^{\rm seam}\) as an output channel removes it as an untracked
remainder; the global-square problem is now the oriented Green comparison
for the coherent trace \(\overline E_T\) together with this fixed transverse
channel.

### Theorem 4.8 — exact Euler transgression of every prime seam

The lattice trace itself has a canonical continuous-plus-transverse
decomposition.  Put

\[
 \beta_a(\ell)=\{\ell/a\}-\tfrac12,\qquad
 I\mathfrak h=\int_0^\infty\mathfrak h(\ell)d\ell,\qquad
 R_a\mathfrak h=\int_0^\infty\beta_a(\ell)
                   \partial_\ell\mathfrak h(\ell)d\ell. \tag{4.52}
\]

For every compactly supported \(C^1\) half-line profile, integration by
parts against the counting staircase gives

\[
 \boxed{
 B_a\mathfrak h={1\over a}I\mathfrak h
       +\tfrac12\mathfrak h(0)+R_a\mathfrak h.}    \tag{4.53}
\]

This is the exact first Euler summation formula, not an asymptotic
Euler--Maclaurin expansion.  Indeed the counting function of
\(a\mathbb N_0\) is

\[
 N_a(\ell)=\lfloor\ell/a\rfloor+1
 ={\ell\over a}+\tfrac12-\beta_a(\ell),           \tag{4.54}
\]

and \(B_a\mathfrak h=-\int_0^\infty N_a\,d\mathfrak h\) gives (4.53).

For the causal field (4.36), \(I\mathfrak h_F=z_0\),
\(\mathfrak h_F(t,0)=F(t)\), and the transport equation gives

\[
 \boxed{
 x_p(t)={1\over a_p}z_0(t)+\tfrac12F(t)
  -\int_0^\infty\beta_{a_p}(\ell)
       (D_t+\tfrac12)\mathfrak h_F(t,\ell)d\ell.}  \tag{4.55}
\]

On the primitive core \(F=L_0G\), equation (4.4) identifies the continuous
term without inversion:

\[
 z_0=(-D_t+\tfrac12)G.                             \tag{4.56}
\]

Most importantly, the common source trace cancels between two primes:

\[
 \boxed{
 (B_p-B_q)\mathfrak h
 =\left({1\over a_p}-{1\over a_q}\right)I\mathfrak h
   +(R_{a_p}-R_{a_q})\mathfrak h.}                 \tag{4.57}
\]

Thus the pairwise square (4.51) contains no unidentified cross-prime
coupling.  Before the finite-window weights in \(E_{p,T}\) are applied, it
is built only from the already explicit quarter-Gamma state \(z_0\) and the
bounded sawtooth transgressions \(R_{a_p}-R_{a_q}\).  The latter are the
precise differential variables that the interior Gamma dissipation must
match in (5.3).

### Theorem 4.9 — one holomorphic quadrant carrier for both axes

Take the Laplace transform of the universal return-depth variable:

\[
 \mathcal H_F(t,s)=\int_0^\infty e^{-s\ell}
        \mathfrak h_F(t,\ell)d\ell,\qquad \Re s\geq0. \tag{4.58}
\]

The transport equation and the causal boundary condition imply

\[
 \boxed{
 (D_t+s+\tfrac12)\mathcal H_F(t,s)=F(t).}          \tag{4.59}
\]

Consequently the complete Gamma bank is the positive-real-axis sampling
of one holomorphic resolvent:

\[
 \boxed{z_n(t)=\mathcal H_F(t,2n),\qquad n\geq0.}  \tag{4.60}
\]

The centered sawtooth has the symmetric Fourier expansion

\[
 \beta_a(\ell)=-\mathop{\rm pv}\sum_{k\ne0}
 {e^{2\pi i k\ell/a}\over2\pi i k}.               \tag{4.61}
\]

Insert (4.61) in (4.52) and integrate by parts.  The endpoint term cancels
between \(k\) and \(-k\), and one obtains the exact imaginary-axis sampling
formula

\[
 \boxed{
 R_a\mathfrak h_F(t)
 ={1\over a}\mathop{\rm pv}\sum_{k\ne0}
 \mathcal H_F\!\left(t,-{2\pi i k\over a}\right).} \tag{4.62}
\]

For the compact smooth sources used here the symmetric series converges
because the \(1/k\) endpoint terms cancel and the paired remainder is
\(O(k^{-2})\).
Combining (4.53) and (4.62) gives the resolvent form of the prime trace:

\[
 \boxed{
 B_p\mathfrak h_F
 ={1\over a_p}\left[
   \mathcal H_F(\cdot,0)
   +\mathop{\rm pv}\sum_{k\ne0}
      \mathcal H_F\!\left(\cdot,-{2\pi i k\over a_p}\right)
   \right]+\tfrac12F.}                            \tag{4.63}
\]

Equations (4.60) and (4.63) are the promised common carrier.  Gamma and
Frobenius are not two independently chosen state systems: Gamma samples the
positive real axis \(s=2n\), while the prime-\(p\) seam samples the imaginary
axis with spacing \(2\pi/a_p\).  The missing coefficient-one comparison in
(5.3) is therefore a quadrant Green theorem for the single holomorphic
field \(\mathcal H_{L_0G}(t,s)\).  A successful theorem must use both axes;
any factorization restricted to only one of them necessarily discards one
of the two exact sampling formulas above.

### Theorem 4.10 — slit-disk filling and exact Gamma area norm

Generate the real-axis samples in one complex variable:

\[
 \mathscr Z_F(t,\zeta)=\sum_{n\geq0}z_n(t)\zeta^n,
 \qquad |\zeta|<1.                                \tag{4.64}
\]

Using (4.41) and summing the geometric series gives

\[
 \boxed{
 \mathscr Z_F(t,\zeta)=\int_0^\infty
 {\mathfrak h_F(t,\ell)\over1-\zeta e^{-2\ell}}d\ell.} \tag{4.65}
\]

For a source supported in \([-T,T]\), this continues holomorphically to
the slit plane, with the relevant cut contained in
\([1,e^{4T}]\).  If \(r=e^{2\ell}>1\), the Plemelj jump of (4.65) is

\[
 \boxed{
 \operatorname{Disc}\mathscr Z_F(t,e^{2\ell})
 :=\mathscr Z_F(t,e^{2\ell}+i0)
   -\mathscr Z_F(t,e^{2\ell}-i0)
 =\pi i\,\mathfrak h_F(t,\ell).}                  \tag{4.66}
\]

Indeed the denominator in (4.65) has derivative two with respect to
\(\ell\) at its zero.  Consequently every prime state is a finite coherent
sum of jumps of this one slit-plane field:

\[
 \boxed{
 x_p(t)=F(t)+{1\over\pi i}\sum_{j\geq1}
   \operatorname{Disc}\mathscr Z_F(t,p^{2j}).}     \tag{4.67}
\]

The sum is automatically finite on the compact-source core.  Thus the
Frobenius tower is not added to the Gamma filling: it is the discrete jump
trace of its analytic continuation.

The Gamma bulk is also an exact area norm of this filling.  Put

\[
 \mathscr C_F(t,\zeta)=D_t\mathscr Z_F(t,\zeta)
 =\sum_{n\geq0}D_tz_n(t)\zeta^n.                  \tag{4.68}
\]

Since

\[
 {1\over n+1/4}=2\int_0^1r^{2n-1/2}dr,            \tag{4.69}
\]

angular Parseval gives the coefficient-one identity

\[
 \boxed{
 \mathcal D_\Gamma(F)=2\int_{-T}^{T}\int_0^1
  \int_0^{2\pi}|\mathscr C_F(t,re^{i\vartheta})|^2
  {d\vartheta\over2\pi}\,r^{-1/2}dr\,dt.}        \tag{4.70}
\]

On the primitive core \(F=L_0G\), one has \(z_0(T)=0\), so the terminal
Gamma storage is the literal Hardy boundary norm

\[
 \boxed{
 \mathcal S_{\Gamma,\mathrm{prim}}^+(G)
 =\int_0^{2\pi}|\mathscr Z_{L_0G}(T,e^{i\vartheta})|^2
        {d\vartheta\over2\pi}.}                   \tag{4.71}
\]

Equations (4.66)--(4.71) construct the common Calderon filling that was
previously missing: the positive Gamma bank is its weighted Bergman bulk
plus Hardy terminal boundary, and every Frobenius output is its prescribed
discrete discontinuity on the exterior cut.  The square in (5.3) is now a
single trace theorem on this fixed slit domain; neither its bulk metric nor
its jump map remains adjustable.

### Theorem 4.11 — coefficient-one radial Green current

For analytic \(U(\zeta)=\sum_{n\geq0}u_n\zeta^n\), define

\[
 \|U\|_{\mathbb B_{1/4}}^2
 :=\sum_{n\geq0}{|u_n|^2\over n+1/4}
 =2\int_0^1\int_0^{2\pi}|U(re^{i\vartheta})|^2
       {d\vartheta\over2\pi}r^{-1/2}dr.           \tag{4.72}
\]

Let

\[
 \mathcal A_\zeta=2\zeta\partial_\zeta+\tfrac12. \tag{4.73}
\]

Its eigenvalue on \(\zeta^n\) is \(2n+1/2=2(n+1/4)\).  Therefore

\[
 \boxed{
 \operatorname{Re}\langle\mathcal A_\zeta U,U\rangle_{\mathbb B_{1/4}}
 =2\|U\|_{H^2(\partial\mathbb D)}^2.}              \tag{4.74}
\]

This is also obtained directly by radial integration by parts; the quarter
in (4.73) cancels the derivative of the weight \(r^{-1/2}\), leaving only
the unit-circle flux.

Summing the state equations \((D_t+2n+1/2)z_n=F\) gives the slit-disk PDE

\[
 \boxed{
 (D_t+\mathcal A_\zeta)\mathscr Z_F(t,\zeta)
 ={F(t)\over1-\zeta}.}                             \tag{4.75}
\]

Pair (4.75) coefficientwise with \(D_t\mathscr Z_F\) in
\(\mathbb B_{1/4}\), take real parts, and integrate in time.  By (4.74),

\[
 \boxed{
 \operatorname{Re}\int_{-T}^{T}
 \left\langle{F\over1-\zeta},D_t\mathscr Z_F\right\rangle_{\mathbb B_{1/4}}dt
 =\mathcal D_\Gamma(F)
  +\|\mathscr Z_F(T)\|_{H^2}^2
  -\|\mathscr Z_F(-T)\|_{H^2}^2.}                 \tag{4.76}
\]

The pairing on the left is understood coefficientwise; it converges on
the smooth compact-source core although \((1-\zeta)^{-1}\) alone is not in
\(\mathbb B_{1/4}\).  Causality makes the last term zero, and primitivity
makes the \(n=0\) coefficient at \(T\) zero.  Hence (4.76) is exactly the
Gamma bulk-plus-terminal side of (3.1), now as the Green flux of the same
analytic filling whose exterior jumps are the prime states.  Both the
coefficient and the boundary orientation are fixed.

## 5. New sharp target

Substitution of (4.3)--(4.6) and the delayed states

\[
 x_p(L_0G)=L_0x_p(G)                                  \tag{5.1}
\]

turns (3.1) into a completely explicit quadratic functional of \(G\).  Put

\[
 \mathfrak h_G:=\mathfrak h_{L_0G}.                 \tag{5.2}
\]

After inserting the exact seam ANOVA (4.49), the remaining theorem is the
single oriented completion

\[
\begin{aligned}
 &\mathcal D_\Gamma(L_0G)+(\theta_T-m_0)\|L_0G\|^2
   +\mathcal S_{\Gamma,\mathrm{prim}}^+(G)
   -\theta_T\|\overline E_T\mathfrak h_G\|^2\\
 &\qquad{}=
   \theta_T\|\mathcal K_T^{\rm seam}\mathfrak h_G\|^2
   +\|\mathcal Q_TG\|^2.                            \tag{5.3}
\end{aligned}
\]

where \(\mathcal Q_T\) must be constructed from the joint Gamma--delay
states, not from the left side.  Equation (5.3) is equivalent to the exact
balance (3.1), but it is structurally sharper: the only trace
leakage is the already constructed vector
\(\sqrt{\theta_T}\mathcal K_T^{\rm seam}\mathfrak h_G\), and it occurs on
the required positive side of the completion.  Therefore the next proof is
not allowed to rename or absorb a remainder.  It must produce that exact
vector, with coefficient one, from the transverse Gamma Green energy; the
orthogonal remainder is then \(\mathcal Q_TG\).

Proposition 4.4 forbids factoring the terminal block first.  The immediate
construction problem is the primitive short of the universal half-line
between its continuous Laplace traces and its prime lattice traces, using
terminal storage and interior dissipation together.  Its acceptance
equation is exactly (5.3).

## 6. Ledger

- causal Gamma balance (1.2)--(1.4): **PROVED**;
- causal delay balance (2.3)--(2.5): **PROVED**;
- exact global bulk-plus-terminal identity (3.1): **PROVED**;
- primitive quarter factorization (4.3): **PROVED**;
- disappearance of the \(n=0\) terminal storage (4.4): **PROVED**;
- explicit primitive Gamma terminal form (4.6): **PROVED**;
- closed positive Hankel kernel (4.7)--(4.11): **PROVED**;
- common primitive differential factorization (4.12)--(4.13): **PROVED**;
- radial depth identity and missing-boundary mechanism
  (4.14)--(4.22): **PROVED**;
- safe-Euler-line interpretation (4.23): **PROVED**;
- terminal-only radial trace: **IMPOSSIBLE BY (4.24)--(4.25)**;
- mixed transport PDE and seam law (4.26)--(4.32): **PROVED**;
- canonical positive return-length lift (4.33)--(4.35): **PROVED**;
- universal half-line and cell intertwiners (4.36)--(4.43): **PROVED ON THE
  COMPACT-SOURCE ALGEBRAIC CORE**;
- zero interior support/Tate/degree leakage (4.44)--(4.45): **PROVED**;
- exact seam-trace leakage and pairwise positive square (4.46)--(4.51):
  **PROVED**;
- exact Euler transgression into the \(n=0\) Gamma state and sawtooth
  derivatives (4.52)--(4.57): **PROVED**;
- holomorphic quadrant resolvent and its real/Gamma and imaginary/prime
  sampling identities (4.58)--(4.63): **PROVED**;
- slit-disk continuation, Frobenius jump formula and Gamma
  Bergman--Hardy norm (4.64)--(4.71): **PROVED**;
- coefficient-one radial Green current (4.72)--(4.76): **PROVED**;
- oriented continuous-trace/lattice-trace completion (5.3): **OPEN**;
- global square: **OPEN**.
