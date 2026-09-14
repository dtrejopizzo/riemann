# P124.007 -- virial collar attack and the Tate projection defect

Status: `COMMUTATOR CANDIDATE REFUTED BY EXACT PROJECTION RESIDUAL`.

This note tests whether the collar residual of P124.005--P124.006 can be
killed by a virial/Mourre identity.  The most direct multiplier is

\[
        x_\rho(t):=e^{-t/2}\rho_{+,T}(t),
        \qquad \rho_{+,T}=P_T(e^{t/2}\Phi_{+,T}),
        \tag{0.1}
\]

because

\[
        M_+(x_\rho F)=\int e^{t/2}x_\rho(t)F(t)\,dt
        =\langle\rho_{+,T},F\rangle=J_+(F)          \tag{0.2}
\]

for every primitive `F`.  The result is negative and exact: the projected
virial identity does contain `J_+(F)`, but only in the finite-dimensional
Tate projection defect.  That defect cancels the raw commutator term
identically on a first-contact vector.  Positivity `L_T>=0` supplies no
sign for this commutator.

## 1. Bounded multiplier domain and formal collar limit

Let

\[
        L_T=P_T\mathscr A_TP_T,\qquad
        \mathscr A_T=G_{\Gamma,T}-m_0I-B_{T,+}-B_{T,-}.
\]

All rigorous commutator identities in this note are asserted only for real
bounded regular multipliers `x`, say Lipschitz on `I_T` with finite
one-sided seam values.  Multiplication by such an `x` preserves the
subcritical `H^s` spaces used by first contact, and the finite shift
commutators are bounded on `L^2`.  The Gamma commutator is read first on a
smooth core and then closed in the logarithmic form topology by the usual
Calderon commutator bound for a Lipschitz multiplier.

The discontinuous collar multiplier

\[
        x_\rho=e^{-t/2}\rho_{+,T}
\]

is therefore only a formal target unless one proves a separate convergence
theorem for a chosen family `x_{\rho,\delta}`.  The no-go conclusion below
does not use that limiting step.  It is an identity in the bounded
projected algebra and hence applies to every bounded regularized collar
multiplier individually.  If some regularization converges to `x_\rho` in
a form anti-dual topology strong enough to preserve the displayed Tate
pairings, the same cancellation merely passes to the limit; it does not
become a new equation.

We use the Hilbert convention of D.240: pairings are linear in the first
variable.  With the opposite convention all displayed commutator pairings
are complex conjugated, and the cancellation statements are unchanged.

## 2. Complete commutator formula

For `a>0`,

\[
        [S_a,M_x]F(t)=(x(t-a)-x(t))F(t-a),
        \tag{2.1}
\]

and similarly

\[
        [S_{-a},M_x]F(t)=(x(t+a)-x(t))F(t+a).
        \tag{2.2}
\]

Therefore, on the regular core,

\[
\boxed{
\begin{aligned}
[\mathscr A_T,M_x]
={}&-\int_0^\infty c_\Gamma(u)
       \bigl([S_u,M_x]+[S_{-u},M_x]\bigr)\,du\\
&-\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       \bigl([S_{\log n},M_x]+[S_{-\log n},M_x]\bigr).
\end{aligned}}                                      \tag{2.3}
\]

The jump part of (2.3) is explicit: if `x` has a jump `Delta_s x` at an
interior point `s`, then `[S_a,M_x]F` has the shifted jump

\[
        \Delta_{s+a}\bigl([S_a,M_x]F\bigr)
        =(\Delta_sx)F(s),                            \tag{2.4}
\]

and `[S_{-a},M_x]F` has the shifted jump

\[
        \Delta_{s-a}\bigl([S_{-a},M_x]F\bigr)
        =(\Delta_sx)F(s).                            \tag{2.5}
\]

Thus the collar jumps are not annihilated by the commutator; they are
transported to neighboring activation cells and weighted by the unknown
values of the minimizer.

For real `x`, the expectation of the raw commutator vanishes on the real
subspace:

\[
        \langle[\mathscr A_T,M_x]F,F\rangle=0
        \tag{2.6}
\]

whenever `F` is real and both pairings are defined.  This follows from the
real antisymmetry of the commutator; in (2.3) it is also seen by changing
variables in the two shifted integrals.  On the complex Hilbert space
`i[\mathscr A_T,M_x]` has no fixed sign: complex conjugation changes its
expectation sign.  Since the first-contact equation has real coefficients,
one may take a nonzero real component of any complex first-contact vector.

## 3. Projected virial identity

Let `F_*` be a first-contact minimizer:

\[
        P_TF_*=F_*,\qquad L_TF_*=0,\qquad L_T\ge0.
        \tag{3.1}
\]

For a regularized multiplier `x`, the projected virial identity is

\[
        0=\langle[L_T,iM_x]F_*,F_*\rangle .          \tag{3.2}
\]

Expanding only the left occurrence of `P_T` gives the exact identity

\[
\boxed{
\langle[\mathscr A_T,iM_x]F_*,F_*\rangle
=\langle Q_T iM_xF_*,\mathscr A_TF_*\rangle
 -\langle iM_x\mathscr A_TF_*,F_*\rangle,}
\tag{3.3}
\]

where `Q_T=I-P_T` is the projection onto the two Tate characters.  This is
the full projection defect.  It is finite-dimensional but not zero.

Write

\[
        \mathscr A_TF_*=\alpha\phi_-+\beta\phi_+,
        \qquad \phi_\pm(t)=e^{\pm t/2}.             \tag{3.4}
\]

Since the right side of (3.4) lies in the Tate span,

\[
        \langle Q_T iM_xF_*,\mathscr A_TF_*\rangle
        =\langle iM_xF_*,\mathscr A_TF_*\rangle.    \tag{3.5}
\]

For real `x` and a real first-contact representative, the two terms on the
right side of (3.3) are equal.  Hence (3.3) reduces to (2.6), and (3.2) is
an identity `0=0`.

This is the point at which first-contact positivity fails to help.  A
Mourre argument would need a positive lower bound for
`\langle[L_T,iM_x]F,F\rangle`, but every eigenvector in `ker L_T` has
zero virial expectation.  The positivity of `L_T` gives no sign to its
commutator with a multiplier.

## 4. Regularized collar multipliers expose the exact cancellation

Let `x_\delta` be any real bounded regular multiplier.  Define its two
Tate coordinates on the first-contact vector by

\[
        J_\delta:=M_+(x_\delta F_*),\qquad
        K_\delta:=M_-(x_\delta F_*).              \tag{4.1}
\]

The second term in the projection defect is therefore

\[
\boxed{
\langle iM_{x_\delta}\mathscr A_TF_*,F_*\rangle
=i\alpha K_\delta+i\beta J_\delta.}
\tag{4.2}
\]

The first term is the same number, because `Q_T` keeps exactly the Tate
component tested by `\mathscr A_TF_*`:

\[
\boxed{
\langle Q_T iM_{x_\delta}F_*,\mathscr A_TF_*\rangle
=i\alpha K_\delta+i\beta J_\delta.}
\tag{4.3}
\]

Thus any Tate functional inserted through a bounded multiplier appears in
both finite-dimensional projection-defect terms and cancels.  If a chosen
regularization satisfies

\[
        M_+(x_\delta F_*)\to J_+(F_*),
        \qquad M_-(x_\delta F_*)\to K_-(F_*),      \tag{4.4}
\]

then the desired collar current is recovered in the limit, but only as the
limit of a quantity that has already cancelled at every regularized level.
The limiting passage is therefore unnecessary for the no-go and, by
itself, cannot create `J_+(F_*)=0`.

In a parity sector, `\alpha=\epsilon\beta` and

\[
        c={J_+(F_*)\over2(\sinh T+\epsilon T)}.
        \tag{4.5}
\]

Therefore a virial proof of `J_+(F_*)=0` would have to prove that the
finite-dimensional projection defect in (3.3) vanishes.  But (4.2)--(4.3)
show that this assertion is exactly the desired Tate cancellation, already
inserted twice with opposite signs.

## 5. Relation with the D.240 support anomaly

D.240 identifies the localized dual-Euler support anomaly

\[
        \mathfrak D_{T,\sigma}
        =\chi_T\theta_\sigma^*(I-\chi_T)\eta_\sigma\chi_T
        \tag{5.1}
\]

as the object left after ambient Euler conservation is cut by support.
Differentiating at `\sigma=1/2` and testing one leg against `\phi_+` gives
P124.006's identification

\[
        \left\langle
        \left.\partial_\sigma\right|_{1/2}\mathfrak D_{T,\sigma}F,
        \phi_+\right\rangle
        =-\langle\rho_{+,T},F\rangle
        \qquad(F\in\mathcal P_T).                  \tag{5.2}
\]

The virial calculation above is the same support anomaly in commutator
language.  The cutoff/projection defect in (3.3) is precisely the term that
the uncut conservation law does not see.  It is not a mismatch and not a
new sign: it is the same exterior-support block with one Tate leg.

The phase-120 seam ANOVA can measure the quadratic descendant of this
support block, schematically as a weighted sum of
`\|E_{p,T}\mathfrak h_F-E_{q,T}\mathfrak h_F\|^2`.  First contact does not
make that seam square vanish.  Using it as zero would assume Gate S rather
than prove Gate R.

## 6. Algebraic counterexample to the commutator route

The obstruction is not analytic subtlety at the endpoint.  It is already
visible in the finite-dimensional projection algebra.

Let `H=P H \oplus Q H`, let `L=PAP` be nonnegative on `PH`, and let
`F in PH` satisfy `LF=0` while `AF=r in QH` is nonzero.  For any bounded
self-adjoint `X`,

\[
        \langle[L,iX]F,F\rangle=0.                 \tag{6.1}
\]

Moreover the expansion is exactly

\[
        \langle[A,iX]F,F\rangle
        =
        \langle Q iXF,r\rangle-\langle iXr,F\rangle.
        \tag{6.2}
\]

Choosing `X` so that one Tate coordinate of `QXF` is any prescribed linear
functional of `F` merely inserts that functional into both terms of
(6.2), where it cancels.  This model has the same algebra as
(3.3)--(4.4) and shows that no multiplier virial identity, by itself, can
force the Tate component `r` to vanish.

Thus the failure is not caused by a bad choice of smoothing for
`x_\rho`.  Smoothing only regularizes the formula; it does not alter the
projection algebra.

## 7. Verdict

The virial collar attack does not prove `c=0`.  The rigorous obstruction
is the bounded projected-algebra identity (3.3): any Tate coordinate created
by a bounded regular multiplier enters the two projection-defect terms with
the same value and cancels.  A discontinuous collar multiplier
`x_\rho=e^{-t/2}\rho_{+,T}` may be approached by regularizations only if a
separate convergence theorem is supplied; even then the regularized
cancellation simply survives in the limit.

The raw commutator contributes transported seam terms (2.4)--(2.5), but
for self-adjoint multipliers their expectation has no sign and, on real
first-contact representatives, vanishes identically.  The D.240 support
anomaly is therefore correctly identified with the collar residual, while
the virial/Mourre mechanism leaves exactly the same free seam/Tate
residual.  A future proof must add an independent signed estimate for the
support anomaly or a pre-scalar seam law; it cannot get `J_+=0` from the
projected commutator identity alone.
