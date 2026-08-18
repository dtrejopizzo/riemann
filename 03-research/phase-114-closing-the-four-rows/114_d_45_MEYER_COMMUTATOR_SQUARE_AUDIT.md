# D.45 — Meyer commutators: square audit and exact operator defect

## 1. Question and answer

For a primitive test `f`, put

\[
 g=f*f^\sharp,                                                \tag{1.1}
\]

where `sharp` is the centrally normalized group involution.  The question is
whether Meyer's source trace formula rewrites the primitive nuclear form as

\[
 B_{\rm nuc}(f,f)=-\|K_f\|_{\rm HS}^2                         \tag{1.2}
\]

or as the negative trace of a positive square, without first constructing
the row-D Hilbert polarization.

The answer is no.  Meyer's actual commutator identity gives a **difference
of two Hankel squares**, and his positive-chart map has an additional
almost-section defect.  After the exact D.32 comparison the total defect is,
at every finite cutoff and hence as a stabilized quadratic form,

\[
 \boxed{
 B_{\rm nuc}(f,f)
   =\|\mathbf Sf\|^2-\|\mathbf Bf\|^2
   =-\langle f,\Delta_Hf\rangle,
 \qquad
 \Delta_H=\mathbf B^*\mathbf B-\mathbf S^*\mathbf S.}          \tag{1.3}
\]

Turning (1.3) into (1.2) is possible exactly when `Delta_H>=0`; then one may
take `K_f=Delta_H^(1/2)f`.  That positivity is Weil's criterion, not a
consequence of Meyer's trace computation.

## 2. The four Meyer maps

Let

\[
 \mathscr A=\mathcal S_>\oplus\mathcal S_<
\]

and choose a smooth cutoff `phi` with

\[
 \phi(x)+\phi(x^{-1})=1.
\]

Write `M=M_phi`, `J` for inversion, `F` for additive Fourier transform and
`Z` for the zeta/Poisson operator.  Meyer defines

\[
 \begin{aligned}
 \iota_+h&=(Zh,JZFh),
 &\pi_+(h_1,h_2)&=(MZ^{-1}h_1,FMZ^{-1}Jh_2),\\
 \iota_-h&=(h,h),
 &\pi_-(h_1,h_2)&=(Mh_1,JMJh_2).
 \end{aligned}                                                  \tag{2.1}
\]

The minus maps satisfy

\[
 \pi_-\iota_-=I,                                               \tag{2.2}
\]

so `P_-:=iota_- pi_-` is an idempotent.  The plus maps satisfy only

\[
 \pi_+\iota_+=M+FMF
 =I+M-FJMJF.                                                    \tag{2.3}
\]

Thus the exact almost-section defect is

\[
 \boxed{D_+=I-\pi_+\iota_+=FJMJF-M.}                           \tag{2.4}
\]

In particular `iota_+ pi_+` is not proved to be a projection, and `D_+` is
a difference of two self-adjoint cutoff conjugates, not a positive
operator.

Meyer's character formula is

\[
 \begin{aligned}
 \chi(\rho)(h)
 ={}&-\operatorname{Tr}\Lambda(h)
      (\iota_-\pi_- -\iota_+\pi_+)\\
 &+\operatorname{Tr}\Lambda(h)D_+.                            \tag{2.5}
 \end{aligned}
\]

Equivalently, after expanding the matrices,

\[
 \begin{aligned}
 \chi(\rho)(h)={}&
 -\operatorname{Tr}_{\mathcal S_>}\Lambda(h)(M-ZMZ^{-1})\\
 &-\operatorname{Tr}_{\mathcal S_<}\Lambda(h)
       J(M-ZMZ^{-1})J\\
 &-\operatorname{Tr}_{\mathcal H_+}\Lambda(h)
       (M-FJMJF).                                               \tag{2.6}
 \end{aligned}
\]

All three products in (2.6) are nuclear.  Neither their individual
factors nor their sum is asserted by Meyer to be positive.

## 3. The exact projection-commutator lemma

The elementary Hilbert-space identity behind Meyer's Toeplitz trace
calculation determines the sign question completely.

> **Lemma 3.1.** Let `P=P*=P^2`, `Q=I-P`, and let `A` be such that the two
> off-diagonal blocks `QAP` and `PAQ` are Hilbert--Schmidt.  Then
> \[
> \boxed{
> \operatorname{Tr}\bigl(A[P,A^*]\bigr)
> =\|QAP\|_{\rm HS}^2-\|PAQ\|_{\rm HS}^2.}                    \tag{3.1}
> \]

**Proof.** Relative to `H=PH direct-sum QH`, write

\[
 A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
 \qquad b=PAQ,\quad c=QAP.
\]

Then

\[
 [P,A^*]=\begin{pmatrix}0&c^*\\-b^*&0\end{pmatrix}
\]

and the diagonal blocks of `A[P,A*]` are `-bb*` and `cc*`.  Taking traces
gives (3.1).  This proof also works by approximation when only the displayed
products are trace class.  QED.

Thus a commutator trace is a signed index/anomaly.  It is a negative square
only under the additional triangularity condition

\[
 QAP=0,                                                        \tag{3.2}
\]

and a positive square only if `PAQ=0`.  Neither condition holds for general
bilateral convolution operators.

## 4. Direct computation in logarithmic coordinates

Replace the smooth cutoff by the sharp projection

\[
 P=1_{[0,\infty)}quad\text{on }L^2(\mathbb R,du).              \tag{4.1}
\]

This replacement is legitimate for Meyer's trace anomaly because only the
asymptotic values of `phi` enter it.  Let `A_f` be convolution by a compactly
supported smooth function `f`.  Its kernel is `f(u-v)`.  A change of
variables gives

\[
 \begin{aligned}
 \|QA_fP\|_{\rm HS}^2
   &=\int_{r<0}|r|\,|f(r)|^2\,dr,\\
 \|PA_fQ\|_{\rm HS}^2
   &=\int_{r>0}r\,|f(r)|^2\,dr.                                \tag{4.2}
 \end{aligned}
\]

Therefore

\[
 \operatorname{Tr}\bigl(A_f[P,A_f^*]\bigr)
 =-\int_{\mathbb R}r|f(r)|^2\,dr.                              \tag{4.3}
\]

Equation (4.3) is the logarithmic-coordinate version of Meyer's lemma

\[
 \operatorname{Tr}\Lambda(f_0)[M,\Lambda(f_1)]
   =\tau(f_0*\partial f_1).                                   \tag{4.4}
\]

For `f_1=f_0^sharp`, the right side of (4.4) is (4.3), up to the fixed
involution convention.

The sign in (4.3) is genuinely free.  A nonzero `f` supported in `(0,infty)`
gives a negative value; one supported in `(-infty,0)` gives a positive
value.

This remains true after imposing the two primitive moments.  On either
open half-line choose three nonzero test bumps with disjoint supports.  The
two linear conditions

\[
 \int e^{u/2}f(u)\,du=0,
 \qquad
 \int e^{-u/2}f(u)\,du=0                              \tag{4.5}
\]

have a nonzero solution in their three-dimensional span.  Its support stays
in the chosen half-line.  Hence both signs in (4.3) occur even on the
primitive source.  This statement concerns the **individual Toeplitz
anomaly**, not the full global form; the remaining Meyer terms may cancel
it.

## 5. Why the zeta conjugation does not turn the anomaly into a square

For `h=f_0*f_1`, Meyer rewrites the first term of (2.6) as

\[
 \begin{aligned}
 -\operatorname{Tr}\Lambda(h)(M-ZMZ^{-1})
 ={}&\operatorname{Tr}\Lambda(f_0)[M,\Lambda(f_1)]\\
 &-\operatorname{Tr}\Lambda(Z^{-1}f_0)
       [M,\Lambda(Zf_1)].                                     \tag{5.1}
 \end{aligned}
\]

If `f_1=f_0^sharp`, the first trace is the signed Hankel difference (3.1).
The second trace is not its Hilbert adjoint square: its two convolution
symbols are `Z^{-1}f` and `Zf^sharp`.  They would be adjoints precisely if

\[
 Zf^\sharp=(Z^{-1}f)^\sharp
 \quad\text{for every }f,
 \quad\text{i.e.}\quad
 \boxed{Z=(Z^{-1})^\sharp.}                                   \tag{5.2}
\]

Condition (5.2) says that `Z` is unitary for the chosen Hilbert involution.
The zeta operator is not unitary; its functional equation relates it to the
opposite Gamma/Fourier chart instead.  The exact non-unitarity obstruction
in this attempted factorization is

\[
 \boxed{\mathfrak d_Z=Z-(Z^{-1})^\sharp.}                       \tag{5.3}
\]

The other boundary chart and the Fourier--Gamma term in (2.6) repair the
**character identity**, but they do not make each summand a positive
square.  Formula (2.4) contributes the independent almost-section defect
`D_+`.

## 6. Full source defect and comparison with D.32--D.44

Let

\[
 \mathfrak D_M(h)=
 -\Lambda(h)(\iota_-\pi_- -\iota_+\pi_+)
 +\Lambda(h)D_+.                                               \tag{6.1}
\]

Meyer's theorem states

\[
 \chi(\rho)(h)=\operatorname{Tr}_{\rm nuc}\mathfrak D_M(h).   \tag{6.2}
\]

For a primitive square `h=f*f^sharp`, the two polar characters vanish and
the A--B--C comparison identifies (6.2), with the established global sign
convention, with `B_nuc(f,f)`.  D.32 then gives

\[
 \operatorname{Tr}_{\rm nuc}\mathfrak D_M(f*f^\sharp)
 =\|\mathbf Sf\|^2-\|\mathbf Bf\|^2.                           \tag{6.3}
\]

Thus the exact **total** operator defect is not merely `d_Z` or `D_+`; after
all cancellations it is, at finite cutoff, the operator below and globally
the associated stabilized quadratic-form operator

\[
 \boxed{
 \mathscr R_M=\mathbf S^*\mathbf S-\mathbf B^*\mathbf B
             =-\Delta_H.}                                     \tag{6.4}
\]

The intermediate defects have the following roles:

* the two Hankel blocks in (3.1) are the incoming/outgoing cutoff defect;
* `d_Z` is the failure of zeta conjugation to identify them as adjoints;
* `D_+` is the failure of the positive-chart map to be an candid section;
* their complete prime--Gamma recombination is (6.4).

No term may be discarded: doing so changes Meyer's character and breaks the
exact D.32 comparison.

## 7. Necessary and sufficient condition for a negative square

Suppose there is a Hilbert space `K` and a closed operator

\[
 K:\mathcal P\longrightarrow\mathscr K
\]

such that

\[
 B_{\rm nuc}(f,f)=-\|Kf\|^2.                                  \tag{7.1}
\]

Polarization of (7.1) and (6.4) forces

\[
 K^*K=\Delta_H.                                                \tag{7.2}
\]

Consequently

\[
 \boxed{
 \text{a negative-square realization exists}
 \Longleftrightarrow
 \Delta_H\ge0\text{ on }\mathcal P.}                          \tag{7.3}
\]

If positivity holds, the canonical choice is

\[
 K=\Delta_H^{1/2}.                                             \tag{7.4}
\]

Conversely (7.1) immediately proves the sign.  By D.37 and Weil's
criterion, (7.3) is equivalent to RH.  Hence no algebraic rearrangement of
Meyer's unconditional commutator formula can prove (7.1) unless it also
proves the missing global Hodge inequality.

The same conclusion applies to a trace-square formula

\[
 B_{\rm nuc}(f,f)=-\operatorname{Tr}(T_fT_f^*).                 \tag{7.5}
\]

Indeed, (7.5) is available in D.37 only after a positive, centrally unitary,
trace-compatible completion is constructed.  Meyer's original Frechet
nuclear trace has cyclicity and heredity, but no `C*` positivity axiom:
`Tr_nuc(AA*)>=0` is not meaningful until an appropriate Hilbert adjoint and
positive trace have been supplied.

## 8. Equality case

If the missing sign is established, then

\[
 B_{\rm nuc}(f,f)=0
 \Longleftrightarrow
 f\in\ker\Delta_H
 \Longleftrightarrow
 Kf=0.                                                         \tag{8.1}
\]

Thus strictness requires

\[
 \ker\Delta_H\cap\mathcal P=\{0\}.                            \tag{8.2}
\]

Neither the Toeplitz commutator lemma nor the almost-section formula proves
(8.2).  D.24 proves it downstream after the sign.  No zero-side argument is
used in the present audit.

## 9. Finite-dimensional certificate

The script `114_d_45_meyer_commutator_verify.py` checks, with exact rational
matrices:

1. identity (3.1);
2. a pure upper off-diagonal example giving a negative trace;
3. a pure lower off-diagonal example giving a positive trace;
4. a matrix with both blocks, verifying that the value is their difference,
   not minus the norm of the full commutator.

This certificate tests the algebraic step on which any proposed
Hilbert--Schmidt-square rewriting must rely.

## 10. Verdict

Meyer's maps provide an exact nuclear **index formula**, not reflection
positivity.  For convolution squares, the basic trace is

\[
 \|QAP\|_{\rm HS}^2-\|PAQ\|_{\rm HS}^2,
\]

and the full formula contains the additional source defects `d_Z` and
`D_+`.  D.32 combines them exactly into

\[
 -\Delta_H=\mathbf S^*\mathbf S-\mathbf B^*\mathbf B.
\]

Therefore the desired formula `B_nuc=-||K_f||^2_HS` is not an unconditional
rearrangement of Meyer's trace.  It exists exactly when `Delta_H` is
positive, which is row D itself.

### Primary source audited

R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta
function*, especially the definitions of `iota_+`, `iota_-`, `pi_+`,
`pi_-`, the almost-section identities, the nuclearity corollary, and the
Toeplitz trace lemma (arXiv:math/0412277).
