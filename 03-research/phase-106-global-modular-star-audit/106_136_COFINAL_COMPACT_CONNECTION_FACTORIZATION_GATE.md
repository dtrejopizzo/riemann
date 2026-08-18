# 106.136 — Cofinal compact connection factorization gate

## 1. Purpose and result

Documents 106.131 and 106.133 isolate the mean-periodic connection

\[
 \mathcal C F=T_{K'+K/2}M_{K/h}F                                      \tag{1}
\]

and its undifferentiated commutator

\[
 \mathcal JF=T_KM_{K/h}F=[T_K,M_{K/h}]F,
 \qquad F*K=0.                                                        \tag{2}
\]

The question here is whether these operators can be factored through the
*complete* ordinary-prime--Gamma displacement bank, rather than through a
finite Euler head or through independent local prime cells.

There is an exact answer.

1. Both \(\mathcal J\) and \(\mathcal C\) are Hilbert--Schmidt in the
   physical mean-periodic Hilbert space.
2. The complete positive generator is boundedly invertible after removing
   the constant and the exact Riemann radical.  Therefore both connection
   operators possess canonical compact factorizations through the full
   ordinary von Mangoldt--Gamma gradient.
3. The optimal factorization gains are

   \[
    \gamma_J^2=\|\mathcal J\widetilde A^{-1}\mathcal J^\sharp\|,
    \qquad
    \gamma_C^2=\|\mathcal C\widetilde A^{-1}\mathcal C^\sharp\|.     \tag{3}
   \]

4. These gains are limits in **operator norm** of common-cutoff,
   regularized factorizations containing every prime power cofinally.
   Hence the connection factorization is not merely formal and is not
   controlled by an arbitrary finite head.
5. A contractive connection factorization is equivalent to the concrete
   relative form inequality

   \[
    \mathcal C^\sharp\mathcal C\preceq\widetilde A.                  \tag{4}
   \]

   Thus a change of realization cannot manufacture the strict gain.  This
   is the sharp relative-amplitude gate for the Douglas/KYP realization;
   it is distinct from the linear Hermitian power absorbed in 106.135 and
   is not an exact rewriting of the original physical form.

This is a genuine signed all-atom factorization and a quantitative
obstruction.  It does not prove that \(\gamma_C<1\), and therefore does
not by itself prove the physical surplus.

## 2. Semantic audit

The following previous results are binding.

* 106.56 shows that a cutoff commutator cannot simply be discarded.
* 106.64 gives the exact mean-periodic coordinate.
* 106.96 constructs finite exterior-amplitude transfers, but only over a
  finite prime-power row.
* 106.105 proves the canonical transfer theorem for the *whole* threshold
  observation.  It does not calculate the compactness or the cofinal
  approximation of the connection operator (1).
* 106.131 rules out a product of passive local Euler cells.
* 106.133 computes the physical adjoint and the Hermitian connection
  coboundary.

The result below is therefore not another local KYP cell and not another
finite matched filter.  It is the Douglas factorization of the specific
connection (1) through the complete displacement bank, together with a
norm-convergent cofinal approximation theorem made possible by the new
Hilbert--Schmidt observation.

## 3. The physical connection is Hilbert--Schmidt

Put

\[
 h(x)=\cosh(x/2),\qquad a(x)=\frac{K(x)}{h(x)},
 \qquad d\omega_K(x)=\frac{a(x)}{c_K}\,dx,
 \qquad c_K=\frac12.                                                \tag{5}
\]

Let

\[
 \mathscr H_\omega=L^2_{\rm even}(\omega_K),
 \qquad \mathcal N_K=W(\mathbf1\oplus\mathcal R)^\perp,             \tag{6}
\]

where \(Wq=hq\).  The second definition in (6), rather than an
unsupported closedness statement for convolution, is used throughout.
On the analytic core it is exactly \(F*K=0\).

For an integrable kernel \(b\), define

\[
 \mathcal T_b=T_bM_a.                                                \tag{7}
\]

Since \(a(y)dy=c_Kd\omega_K(y)\), this operator has the physical integral
kernel

\[
 \boxed{
  (\mathcal T_bF)(x)
  =c_K\int_{\mathbb R}b(x-y)F(y)\,d\omega_K(y).}                    \tag{8}
\]

### Theorem 1 — Compactness and exact Hilbert--Schmidt norm

If \(b\) is bounded, then \(\mathcal T_b\) is Hilbert--Schmidt on
\(\mathscr H_\omega\), and

\[
 \boxed{
 \|\mathcal T_b\|_{\rm HS}^2
 =c_K^2\iint_{\mathbb R^2}|b(x-y)|^2
       \,d\omega_K(x)d\omega_K(y).}                               \tag{9}
\]

In particular, (9) applies to

\[
 b_0=K,
 \qquad b_+=K'+\frac12K,                                            \tag{10}
\]

and hence to \(\mathcal J=\mathcal T_{b_0}\) and
\(\mathcal C=\mathcal T_{b_+}\).

#### Proof

The theta representation makes \(K\) and \(K'\) bounded and
double-exponentially decreasing.  Moreover,

\[
 \omega_K(\mathbb R)
 =\frac1{c_K}\int\frac K h\,dx
 \leq\frac1{c_K}\int hK\,dx=1.                                  \tag{11}
\]

Equation (8) identifies \(c_Kb(x-y)\) as the integral kernel relative to
\(d\omega_K\).  Its squared \(L^2(\omega_K\otimes\omega_K)\)-norm is
exactly (9), and it is finite by boundedness of \(b\) and (11).  This is
the Hilbert--Schmidt criterion.  The two kernels in (10) are bounded, so
the last assertion follows. \(\square\)

The adjoint is also immediate from (8):

\[
 \mathcal T_b^\sharp=\mathcal T_{b^\vee},
 \qquad b^\vee(x)=\overline{b(-x)}.                                \tag{12}
\]

For \(F\in\mathcal N_K\), \(T_KF=0\), and therefore

\[
 \mathcal JF=T_KM_aF=[T_K,M_a]F.                                  \tag{13}
\]

This proves compactness of the exact commutator, not merely of a cutoff.

## 4. The full ordinary-prime--Gamma gradient

Let

\[
 d\nu_\zeta(u)
 =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
      \delta_{\log n}(du)
  +\frac{e^{-u/2}}{1-e^{-2u}}\,du.                                 \tag{14}
\]

On the multiplier core define

\[
 (\mathcal Gq)(u,x)
 =\{K(x)K(x-u)\}^{1/2}\{q(x)-q(x-u)\}.                            \tag{15}
\]

Its output space is

\[
 \mathscr Y_\zeta
 =L^2\big((0,\infty)\times\mathbb R,
          d\nu_\zeta(u)dx\big).                                  \tag{16}
\]

Every ordinary prime power occurs in (14), with its literal von Mangoldt
weight, and the full Gamma channel is retained.  The closed form identity
is

\[
 \|\mathcal Gq\|_{\mathscr Y_\zeta}^2
 =\mathscr E_K(q)=\langle q,Lq\rangle_{\mu_K}.                     \tag{17}
\]

Transport (15) by \(W\) and restrict to \(\mathcal N_K\):

\[
 \widetilde{\mathcal G}=\mathcal GW^{-1}|_{\mathcal N_K},
 \qquad
 \widetilde A=WLW^{-1}|_{\mathcal N_K}.
 \tag{18}
\]

Then

\[
 \widetilde{\mathcal G}^{\,*}\widetilde{\mathcal G}
 =\widetilde A                                                   \tag{19}
\]

as closed forms.

### Lemma 2 — Unconditional invertibility after exact anti-shorting

There exists \(\alpha_0>0\) such that

\[
 \boxed{\widetilde A\succeq\alpha_0I.}                            \tag{20}
\]

#### Proof

Document 106.47 proves

\[
 \sigma_{\rm ess}(L|_{\mathbf1^\perp})\subset[1/2,\infty).         \tag{21}
\]

The complete positive Gamma displacement density forces every
zero-energy vector of \(L\) to be constant.  Constants have been removed
in (6), so \(\ker\widetilde A=\{0\}\).  If \(0\) belonged to
\(\sigma(\widetilde A)\), then, being below the essential spectrum, it
would be an isolated eigenvalue of finite multiplicity.  That contradicts
the trivial kernel.  Since the spectrum is closed and nonnegative,
\(\alpha_0=\mathrm{dist}(0,\sigma(\widetilde A))>0\).  \(\square\)

The polar decomposition is consequently

\[
 \widetilde{\mathcal G}=U_A\widetilde A^{1/2},                    \tag{22}
\]

where \(U_A\) is an isometry from \(\mathcal N_K\) onto
\(\overline{\mathrm{Ran}\,\widetilde{\mathcal G}}\).

## 5. Canonical signed factorization

For \(B\in\{\mathcal J,\mathcal C\}\), define

\[
 \boxed{
 H_B
 :=B\widetilde A^{-1/2}U_A^*
  =B\widetilde A^{-1}\widetilde{\mathcal G}^{\,*}}                \tag{23}
\]

on \(\mathscr Y_\zeta\), with value zero on the orthogonal complement
of the closed gradient range.

### Theorem 3 — Exact all-atom factorization and optimal gain

The operator \(H_B\) is compact and

\[
 \boxed{B=H_B\widetilde{\mathcal G}.}                             \tag{24}
\]

Among all bounded operators \(H:\mathscr Y_\zeta\to\mathscr H_\omega\)
satisfying \(B=H\widetilde{\mathcal G}\), the operator in (23) has
minimum norm, and

\[
 \boxed{
 \inf_{B=H\widetilde{\mathcal G}}\|H\|^2
 =\|H_B\|^2
 =\|B\widetilde A^{-1}B^\sharp\|
 =\sup_{0\ne F\in D(\widetilde A^{1/2})}
   \frac{\|BF\|_{\omega_K}^2}
        {\langle F,\widetilde AF\rangle_{\omega_K}}.}            \tag{25}
\]

#### Proof

Equations (20), (22), and (23) give

\[
 H_B\widetilde{\mathcal G}
 =B\widetilde A^{-1/2}U_A^*U_A\widetilde A^{1/2}=B,                \tag{26}
\]

first on the form core and then by closure.  The factor
\(B\widetilde A^{-1/2}\) is compact because \(B\) is Hilbert--Schmidt
and \(\widetilde A^{-1/2}\) is bounded.  Hence \(H_B\) is compact.

Any other factor \(H\) satisfying (24) agrees with \(H_B\) on
\(\mathrm{Ran}\,\widetilde{\mathcal G}\), since that equation
fixes its value there.  Its norm is therefore at least the norm of the
zero extension (23).  Finally,

\[
 H_BH_B^\sharp=B\widetilde A^{-1}B^\sharp,                         \tag{27}
\]

which gives the first three expressions in (25).  The last is the usual
Rayleigh quotient for
\(B\widetilde A^{-1/2}\). \(\square\)

The heat representation is explicit and norm convergent:

\[
 \boxed{
 H_B
 ={1\over\sqrt\pi}B
   \int_0^\infty t^{-1/2}e^{-t\widetilde A}\,dt\,U_A^*.}          \tag{28}
\]

The exponential factor in (28) contains the complete generator (14), so
all prime powers remain coupled before the signed connection kernel
\(c_Kb(x-y)\) is applied.

### Corollary 4 — Exact contractivity criterion

For \(B=\mathcal C\),

\[
 \boxed{
 \|H_C\|\le1
 \quad\Longleftrightarrow\quad
 \mathcal C^\sharp\mathcal C\preceq\widetilde A.}                \tag{29}
\]

Strict contractivity is equivalent to the corresponding strict relative
form bound.  In particular, no alternative signed kernel realizing the
same connection through the same physical bank can have a smaller norm
than (23).

The unconditional finite estimate

\[
 \boxed{
 \|H_C\|^2
 \le {c_K^2\omega_K(\mathbb R)^2
          \|K'+K/2\|_\infty^2\over\alpha_0}<\infty}               \tag{30}
\]

follows from (9), (20), and (25).  Formula (30) proves bounded
factorability but does not imply the sharp constant one.

## 6. Cofinal ordinary-prime approximation in operator norm

Let \(\widetilde A_X\) be the compression to \(\mathcal N_K\) of the
closed positive form containing the full Gamma density and the prime
powers \(n=p^k\le X\), all with the literal weights
\(\Lambda(n)/\sqrt n\).  Then

\[
 \widetilde A_X\nearrow\widetilde A                              \tag{31}
\]

in the monotone-form sense.  For \(\varepsilon>0\), put

\[
 \Theta_{B;X,\varepsilon}
 :=B(\widetilde A_X+\varepsilon I)^{-1}B^\sharp.                  \tag{32}
\]

### Theorem 5 — Norm-convergent cofinal gain

For every \(\varepsilon>0\),

\[
 \boxed{
 \Theta_{B;X,\varepsilon}
 \longrightarrow
 B(\widetilde A+\varepsilon I)^{-1}B^\sharp
 \quad\hbox{in operator norm as }X\to\infty.}                   \tag{33}
\]

Moreover,

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}\lim_{X\to\infty}
 \|\Theta_{B;X,\varepsilon}\|
 =\|B\widetilde A^{-1}B^\sharp\|=\|H_B\|^2.}                   \tag{34}
\]

#### Proof

Monotone convergence of closed forms gives

\[
 (\widetilde A_X+\varepsilon I)^{-1}
 \longrightarrow
 (\widetilde A+\varepsilon I)^{-1}                               \tag{35}
\]

strongly, with all resolvents bounded by \(\varepsilon^{-1}\).  If a
uniformly bounded sequence converges strongly, then multiplication on
both sides by a compact operator and its adjoint upgrades convergence to
operator norm.  Theorem 1 supplies precisely that compact operator \(B\),
which proves (33).

By (20),

\[
 \|(\widetilde A+\varepsilon I)^{-1}-\widetilde A^{-1}\|
 \le {\varepsilon\over\alpha_0(\alpha_0+\varepsilon)}.            \tag{36}
\]

Sandwiching (36) by \(B,B^\sharp\) proves (34). \(\square\)

If \(P_M\) are the heat-core Galerkin projections of 106.98, then
\(P_M\to I\) strongly.  Since every operator in (32)--(34) is compact,

\[
 \|P_M\Theta P_M-\Theta\|\longrightarrow0.                       \tag{37}
\]

Thus the all-atom connection gain is accessible by the joint limit

\[
 M\to\infty,\qquad X\to\infty,\qquad\varepsilon\downarrow0,      \tag{38}
\]

with norm control at each regularized stage.  Fixing \(X\) is not an
admissible replacement for (38): it changes the denominator in (25) and
does not determine the physical gain.

## 7. Exact status of the signed factorization route

The requested global factorization exists:

\[
 \boxed{
 [T_K,M_{K/h}]|_{\mathcal N_K}
 =H_J\widetilde{\mathcal G},
 \qquad
 T_{K'+K/2}M_{K/h}|_{\mathcal N_K}
 =H_C\widetilde{\mathcal G}.}                    \tag{39}
\]

It is compact, uses the complete ordinary von Mangoldt--Gamma bank, and
is the operator-norm limit of cofinal common-cutoff factorizations.  The
sharp connection gain is not a free design parameter:

\[
 \boxed{
 \gamma_C^2
 =\|\mathcal C\widetilde A^{-1}\mathcal C^\sharp\|.}             \tag{40}
\]

Consequently the remaining KYP step cannot be closed merely by choosing a
different realization of the same delay bank.  It requires a proof of the
specific arithmetic relative inequality (29), or a weaker jointly signed
Schur estimate in which the ordinary-prime outgoing power is retained
together with the Hermitian connection kernel of 106.133.  The present
theorem proves existence, compactness, optimality, and cofinal numerical
access of the signed factor; it does not assert the missing unit gain.
