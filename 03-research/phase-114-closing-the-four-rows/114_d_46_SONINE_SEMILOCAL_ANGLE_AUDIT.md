# D.46 — Sonine/de Branges and semilocal projection-angle audit

## 1. Setup

Let `H` be the semilocal self-dual Hilbert space, let `P` be the orthogonal
projection onto the chosen two-sided support window, put `Q=I-P`, and let
`U` be the unitary Fourier--Poisson transform.  The basic phase operator is

\[
 A_U=U^*PU-P.                                                  \tag{1.1}
\]

If `F_P=2P-I`, then

\[
 \boxed{
 A_U={1\over2}U^*[F_P,U].}                                    \tag{1.2}
\]

Thus (1.1) is exactly the `U^*[P,U]`-type operator requested in the
semilocal route.  It is source-defined and contains no zeta zeros.

Let `ell_+` and `ell_-` be the two continuous Tate jets in the analytic
test/RKHS realization and let

\[
 \mathcal P_0=\ker\ell_+\cap\ker\ell_- .                       \tag{1.3}
\]

When the two functionals have Riesz vectors, write `R` for the orthogonal
projection onto `P_0`.  Otherwise every assertion below is read on the
closed codimension-at-most-two subspace (1.3), without using `R`.

## 2. Exact block form and the support square

Relative to `H=PH direct-sum QH`, write

\[
 U=\begin{pmatrix}a&b\\c&d\end{pmatrix},
 \qquad
 a=PUP,\ b=PUQ,\ c=QUP,\ d=QUQ.                                \tag{2.1}
\]

Unitarity gives `a*a+c*c=I_(PH)`.  Direct multiplication yields

\[
 \boxed{
 A_U=
 \begin{pmatrix}
   -c^*c&a^*b\\
   b^*a&b^*b
 \end{pmatrix}.}                                               \tag{2.2}
\]

Consequently

\[
 \begin{aligned}
 \langle x,A_Ux\rangle&=-\|QUx\|^2,
 &&x\in PH,\\
 \langle y,A_Uy\rangle&= \|PUy\|^2,
 &&y\in QH.                                                    \tag{2.3}
 \end{aligned}
\]

The negative-square identity in D.35 is exactly the first line of (2.3).
It requires **range support**.  It is not a statement on all of `H`.

## 3. Sonine space and what it actually proves

The (semi)local Sonine space is

\[
 \mathcal S_{P,U}
 =QH\cap U^*QH
 =\ker P\cap\ker(PU).                                         \tag{3.1}
\]

Equivalently, its orthogonal projection is the meet

\[
 E_S=Q\wedge U^*QU
     =I-(P\vee U^*PU).                                         \tag{3.2}
\]

For every `s in S_(P,U)`, both terms in (1.1) vanish:

\[
 Ps=0,\qquad PUs=0,
 \qquad\Longrightarrow\qquad
 \boxed{A_Us=0.}                                               \tag{3.3}
\]

Thus Sonine's simultaneous support gap does not make (1.1) strictly
negative.  It places vectors in its kernel.

The Mellin transforms of Sonine vectors may form de Branges spaces, and
their reproducing kernels have the usual positive Hilbert norm.  That
positivity is compatible with (3.3); it is not the primitive Weil sign.
To identify it with `-B_nuc` one still needs a different compressed scaling
operator and the exact trace comparison of D.35.

## 4. Two jets do not imply Sonine triangularity

Sonine implies the two point conditions in the standard self-dual setting:
a physical support gap contains the origin, and a Fourier support gap also
contains the origin.  The converse is false for a structural reason.

The space `P_0` in (1.3) has codimension at most two.  The support condition
`Px=x`, or the exterior condition `Px=0`, has infinite codimension in the
opposite half of a genuine interval decomposition.  Two scalar evaluations
cannot imply either support condition.

The following statement gives the exact obstruction.

> **Proposition 4.1 (primitive compression is not triangular).** Assume the
> cross-window operator
> \[
> b=PUQ:QH\longrightarrow PH                                  \tag{4.1}
> \]
> has rank greater than two.  Then there exists
> \[
> 0\ne y\in\mathcal P_0\cap QH
> \quad\text{with}\quad PUy\ne0,                              \tag{4.2}
> \]
> and hence
> \[
> \langle y,A_Uy\rangle=\|PUy\|^2>0.                         \tag{4.3}
> \]
> In particular `RA_UR` is not nonpositive.

**Proof.** If `PU` vanished on `P_0 intersect QH`, then the map `b=PUQ`
would factor through the quotient

\[
 QH/(\mathcal P_0\cap QH),
\]

whose dimension is at most two.  This would force `rank(b)<=2`, contrary to
the hypothesis.  Choose `y` as in (4.2) and use the second identity in
(2.3).  QED.

For Fourier transformation between a nonempty interval and its exterior,
`b` has infinite rank.  Indeed, its integral kernel is

\[
 e^{-2\pi ixy},\qquad x\text{ in the window},\quad
 y\text{ outside it}.                                         \tag{4.4}
\]

If (4.4) had finite rank, the functions
`x -> exp(-2 pi i x y_j)` for arbitrarily many distinct exterior points
`y_j` would span a finite-dimensional space on an interval.  They are
linearly independent by the uniqueness theorem for exponential
polynomials.  Hence the rank is infinite.  The same argument applies to
the semilocal Fourier--Poisson cross kernel on any nontrivial continuous
archimedean component.

The opposite cross block `c=QUP` also has infinite rank.  The same quotient
argument gives `x in P_0 intersect PH` with `QUx != 0`, and then

\[
 \langle x,A_Ux\rangle=-\|QUx\|^2<0.                           \tag{4.5}
\]

Therefore

\[
 \boxed{RA_UR\text{ is indefinite}.}                           \tag{4.6}
\]

This does not decide the sign of the **globally corrected** `B_nuc`; it
proves that the raw support/Fourier phase operator cannot be that negative
form after merely imposing the two jets.

## 5. Poisson formula does not add the missing triangularity

Poisson summation identifies the two chart boundary values and supplies the
relations used in Meyer's quotient.  It does not assert

\[
 \mathcal P_0\subseteq PH                                     \tag{5.1}
\]

or

\[
 PU(\mathcal P_0\cap QH)=0.                                   \tag{5.2}
\]

Equation (5.2) is precisely contradicted by Proposition 4.1 for the raw
test realization.  Passing to the Poisson quotient may identify some
vectors, but D.41 shows that taking the ordinary boundary Hilbert closure
kills the whole quotient.  Hence triangularity cannot be obtained by
ordinary closure without losing faithfulness.

The semilocal stability theorem for Sonine spaces says that the kernels
(3.1) form a compatible system when places are added.  Compatibility of
kernels is not an inclusion of the two model spaces whose projection
difference realizes `B_nuc`, and (3.3) shows that the raw phase operator
detects no strict form on those kernels.

## 6. Exact angle criterion on a compressed source

Let `M:K -> H` be a proposed source lift.  Put

\[
 C_0=PM,\qquad C_1=PUM.                                       \tag{6.1}
\]

Then

\[
 \boxed{
 M^*A_UM=C_1^*C_1-C_0^*C_0.}                                  \tag{6.2}
\]

Therefore the conditioned negativity is equivalent to

\[
 \|C_1k\|\le\|C_0k\|\quad(k\in K).                           \tag{6.3}
\]

By the Douglas factorization lemma, (6.3) is equivalent to the existence
of a contraction `T` such that

\[
 C_1=TC_0.                                                     \tag{6.4}
\]

In particular it requires

\[
 \ker(PM)\subseteq\ker(PUM).                                  \tag{6.5}
\]

For `M=R`, Proposition 4.1 violates (6.5).  For a lift satisfying

\[
 PM=M,                                                        \tag{6.6}
\]

equation (6.2) becomes the negative square

\[
 M^*A_UM=-M^*U^*QUM,                                          \tag{6.7}
\]

which is D.35.

Thus the semilocal problem is an angle/contractivity problem, not a formal
subspace inclusion supplied by Sonine theory.  In graph coordinates the
optimal constant is

\[
 \alpha(M)=sup_{C_0k\ne0}{\|C_1k\|\over\|C_0k\|}.            \tag{6.8}
\]

The required sign is `alpha(M)<=1`; strict equality requires that no
nonzero primitive vector be an isometric vector of the contraction.  This
is the same angular-operator gate found in the Krein audit.

## 7. Comparison with the exact Hodge defect

If a semilocal Poisson lift `M_Q` satisfies the exact trace comparison of
D.35, then

\[
 \begin{aligned}
 B_Q(F,F)
 &=\operatorname{Tr}
   \bigl(M_Q(F)^*A_{U_Q}M_Q(F)\bigr)\\
 &=-\|Q_Q U_QM_Q(F)\|_{\rm HS}^2                    \tag{7.1}
\end{aligned}

because `P_Q M_Q(F)=M_Q(F)`.  Comparing with D.32--D.44 gives, at the
quadratic-form level,

\[
 \Delta_{H,Q}
 =\bigl(Q_QU_QM_Q\bigr)^*\bigl(Q_QU_QM_Q\bigr).                \tag{7.2}
\]

Equation (7.2) would be the desired source factorization of `Delta_H`.
What Proposition 4.1 proves is that the obvious choice `M_Q=R` cannot
satisfy it.  The raw multiplier choice also fails the support condition, as
proved in D.35.

Without (6.6), the exact defect is instead

\[
 \boxed{
 \Delta(M)=C_0^*C_0-C_1^*C_1
 =M^*(P-U^*PU)M.}                                             \tag{7.3}
\]

Its positivity is equivalent to the angle condition (6.3), and it is
indefinite for the primitive identity lift.

## 8. de Branges interpretation

The Sonine/de Branges correspondence supplies:

1. a positive RKHS norm on Mellin transforms of `S_(P,U)`;
2. Hermite--Biehler functions and monotone phase for that RKHS;
3. stable Sonine kernels under semilocal enlargement.

It does not supply:

1. an identification of the Sonine RKHS norm with `-B_nuc`;
2. the supported lift (6.6) retaining the D.32 prime--Gamma trace;
3. the contraction (6.4) on the primitive Meyer quotient;
4. strictness of (7.2).

Using a de Branges space built from the completed zeta function would make
Hermite--Biehler positivity equivalent to RH and is therefore not a
source-defined proof.  The source-defined semilocal Sonine spaces avoid
that circularity, but their phase operator lies in the kernel (3.3), not in
the desired negative defect.

## 9. New viable subroute

One subroute survives the audit and is sharper than the earlier statement:

> Construct `M_Q` not as the identity, a boundary multiplier or the Sonine
> projection, but as the **minimal-norm Poisson extension of the two-chart
> relation into `P_QH`**, and prove the intertwining identity
> \[
> \operatorname{Tr}M_Q(F)^*A_{U_Q}M_Q(F)=B_Q(F,F).              \tag{9.1}
> \]

If the extension is constructed by an independently proved support theorem,
(6.6) is automatic and (7.1) closes the finite sign.  The remaining tests
are:

1. existence and uniqueness without using `B_Q` or its spectrum;
2. preservation of all prime-power and Gamma terms in (9.1);
3. compatibility under enlargement of the set of places;
4. faithfulness and separation in the cofinal limit.

This is a genuine possible mechanism because support, rather than a
postulated positive metric, creates the square.  No existing Sonine theorem
in the audited framework constructs this extension or proves (9.1).

## 10. Verdict

The semilocal phase operator has the exact source form

\[
 A_U={1\over2}U^*[2P-I,U].
\]

Support compression gives a negative square; exterior compression gives a
positive square; Sonine compression gives zero.  Imposing the two Tate jets
leaves both signs because it removes only two directions while both
cross-window Fourier--Poisson blocks have infinite rank.  Hence Sonine plus
Poisson does **not** produce triangularity on the primitive source.

The required negativity remains equivalent to the contraction/angle
condition (6.3), or to the factorization (7.2) of `Delta_H`.  The viable
remaining version of this route is the construction of a supported,
trace-exact Poisson lift; the raw Sonine and de Branges inclusions do not
provide it.

### Primary framework audited

* A. Connes and C. Consani, *Weil positivity and Trace formula, the
  archimedean place*, Selecta Math. (2021), arXiv:2006.13771.
* A. Connes, C. Consani and H. Moscovici, *Zeta zeros and prolate wave
  operators: Semilocal adelic operators*, Ann. Funct. Anal. 15 (2024),
  arXiv:2310.18423.
