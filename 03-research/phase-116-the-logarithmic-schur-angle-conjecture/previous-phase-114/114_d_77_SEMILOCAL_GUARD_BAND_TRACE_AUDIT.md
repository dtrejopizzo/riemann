# D.77 — Semilocal guard-band trace: corner versus supported leakage

## Status

D.76 constructs a supported guard-band lift and asks whether its
Fourier--Poisson leakage is exactly the A--B--C form.  This note defines the
semilocal transform and performs the comparison before taking a sign.

The result is an exact obstruction for the present lift.  The established
semilocal trace theorem evaluates a **corner operator**
`P_hat P`; supported leakage contains instead the self-adjoint compression
`P P_hat P`.  Their difference is the cross-window block

\[
 Q\widehat P P.
\]

It has infinite rank.  The two primitive moments remove the two polar
characters but do not annihilate this block.  The guard-band version moves
the same obstruction into a boundary covariance defect depending on the two
scaling variables separately; it does not factor through
`h=f star f^vee`, and primitivity does not cancel its logarithmic boundary
weight.

Thus Fourier--Poisson and the semilocal trace do reproduce every local
`p^k` and Gamma term, but not as the leakage norm of the D.76 guard-band
operator.  A further global correction of the lift is necessary.  No RH,
zero divisor, or Julia operator defined from `B_nuc` is used.  The paper is
not modified.

## 1. The source-defined semilocal Fourier--Poisson operator

Let `S` be a finite set of places containing infinity and put

\[
 X_S=\mathbb Z_S^\times\backslash\mathbb A_S,
 \qquad \mathcal H_S=L^2(X_S).                              \tag{1.1}
\]

The product of the self-dual additive local Fourier transforms descends to
a unitary

\[
 U_S=\mathcal F_S:\mathcal H_S\longrightarrow\mathcal H_S. \tag{1.2}
\]

Let `P_Lambda` be the position cutoff and set

\[
 \widehat P_\Lambda=U_S^*P_\Lambda U_S,
 \qquad Q_\Lambda=I-P_\Lambda.                              \tag{1.3}
\]

The multiplicative scaling representation is denoted `theta`, and for a
compactly supported multiplicative test `f` put

\[
 A_f=\theta(f),\qquad
 h=f\star f^\vee,qquad A_fA_f^*=\theta(h).                  \tag{1.4}
\]

All formulas below are first made with finite-rank/smoothing cutoffs; the
semilocal trace theorem supplies their nuclear limits.

The renormalized corner character is

\[
 \mathfrak T_S(h)
 =\lim_{\Lambda\to\infty}
 \left(\mathrm{Tr}(\theta(h)\widehat P_\Lambda P_\Lambda)
       -2h(1)\log\Lambda\right).                            \tag{1.5}
\]

Its local evaluation is

\[
 \mathfrak T_S(h)
 =\sum_{v\in S}\int_{\mathbb Q_v^\times}'
 {h(u^{-1})\over|1-u|_v}\,d^\times u.                       \tag{1.6}
\]

After stabilization in `S`, (1.6) is the row-C distribution.  For
`h=f star f^vee`, the logarithmic realization of (1.6) is exactly

\[
 \begin{aligned}
 B_{\rm nuc}(F,F)={}&
 2\sum_{p,k\ge1}{\Lambda(p^k)\over\sqrt{p^k}}
    \mathrm{Re}\,\langle F,S_{k\log p}F\rangle\\
 &+m_0\|F\|^2-\|\partial_\infty F\|^2.                     \tag{1.7}
\end{aligned}
\]

Thus `U_S` and the corner trace already contain every `p^k` and Gamma.  The
question is whether the same trace is a supported leakage.

## 2. Projected lift and the exact cross-window anomaly

The most direct supported lift is

\[
 M_\Lambda^P(f)=P_\Lambda A_f.                              \tag{2.1}
\]

It satisfies `P_Lambda M=M`, so

\[
 \mathrm{Tr}igl((M_\Lambda^P)^*
   (\widehat P_\Lambda-P_\Lambda)M_\Lambda^P\bigr)
 =-\|Q_\Lambda U_SM_\Lambda^P\|_{\rm HS}^2\le0.            \tag{2.2}
\]

By cyclicity at finite cutoff, the unrenormalized corner difference is

\[
 C_\Lambda(f)
 =\mathrm{Tr}igl(A_f^*
   (\widehat P_\Lambda P_\Lambda-P_\Lambda)A_f\bigr).        \tag{2.3}
\]

The supported leakage is

\[
 D_\Lambda^P(f)
 =\mathrm{Tr}igl(A_f^*
  (P_\Lambda\widehat P_\Lambda P_\Lambda-P_\Lambda)A_f\bigr).
                                                                  \tag{2.4}
\]

Subtracting gives the exact identity

\[
 \boxed{
 C_\Lambda(f)-D_\Lambda^P(f)
 =E_\Lambda^P(f)
 :=\mathrm{Tr}igl(
 A_f^*Q_\Lambda\widehat P_\Lambda P_\Lambda A_f\bigr).}    \tag{2.5}
\]

No local factor or limit is involved in (2.5).  The established trace uses
the non-self-adjoint corner `P_hat P`; the negative square uses the
self-adjoint compression `P P_hat P`.

Relative to `H=P H direct-sum Q H`, write

\[
 \widehat P=\begin{pmatrix}\alpha&\beta\\\beta^*&\delta\end{pmatrix}.
                                                                  \tag{2.6}
\]

Then

\[
 Q\widehat PP=\begin{pmatrix}0&0\\\beta^*&0\end{pmatrix}.   \tag{2.7}
\]

For the archimedean Fourier transform between a nonempty interval and its
exterior, `beta` has infinite rank: its kernel contains the linearly
independent family `x mapsto exp(-2 pi ixy)` indexed by exterior `y`.  The
semilocal product retains this continuous block, hence (2.7) has infinite
rank on every nontrivial window.

> **Theorem 2.1 (corner--leakage decomposition).**  The semilocal character
> equals a supported negative leakage plus the cross anomaly (2.5).  The
> anomaly is not a two-dimensional boundary term and cannot be absorbed by
> changing the matrix of the two ruling jets.

## 3. Why primitivity does not annihilate the cross block

Primitivity is

\[
 \widehat f(0)=\widehat f(1)=0.                              \tag{3.1}
\]

It kills the two one-dimensional characters in the even Poisson quotient.
It does not impose either of the infinite-codimensional triangularity
conditions

\[
 Q_\Lambda\widehat P_\Lambda P_\Lambda A_f=0,
 \qquad
 P_\Lambda\widehat P_\Lambda Q_\Lambda A_f=0.               \tag{3.2}
\]

There is also a direct approximation argument.  D.75 constructs primitive
compact measures

\[
 \epsilon_R=\delta_1-
 {\delta_{e^R}+\delta_{e^{-R}}\over2\cosh(R/2)}              \tag{3.3}
\]

whose integrated scaling operators converge strongly to the identity on
every unitary scaling representation.  If the first operator in (3.2)
vanished for every primitive test, smoothing (3.3) and passing strongly to
the limit would force

\[
 Q_\Lambda\widehat P_\Lambda P_\Lambda=0,                    \tag{3.4}
\]

contrary to its infinite-rank archimedean block.

This proves an operator statement.  It does not by itself say that every
scalar trace in (2.5) is nonzero; it proves that no identity based only on
the two moment equations can delete the anomaly before the trace.

## 4. The genuine guard-band lift

Assume

\[
 \mathrm{supp}\,f\subset[e^{-T},e^T].                  \tag{4.1}
\]

Scaling covariance of the position cutoff gives a smaller projection

\[
 J_{\Lambda,T}=P_{\Lambda e^{-T}}                            \tag{4.2}
\]

such that

\[
 P_\Lambda A_fJ_{\Lambda,T}=A_fJ_{\Lambda,T}.                \tag{4.3}
\]

Thus

\[
 M_{\Lambda,T}^G(f)=A_fJ_{\Lambda,T}                        \tag{4.4}
\]

is supported without projecting its output.  Its leakage is

\[
 D_{\Lambda,T}^G(f)
 =\mathrm{Tr}igl(
 J_{\Lambda,T}A_f^*(\widehat P_\Lambda-P_\Lambda)
 A_fJ_{\Lambda,T}\bigr)\le0.                               \tag{4.5}
\]

Put

\[
 \mathscr E_{\Lambda,T}(f)
 =P_\Lambda A_fA_f^*-A_fJ_{\Lambda,T}A_f^*.                  \tag{4.6}
\]

Cyclicity gives the exact comparison

\[
 \boxed{
 C_\Lambda(f)-D_{\Lambda,T}^G(f)
 =\mathrm{Tr}igl(
   (\widehat P_\Lambda-P_\Lambda)
   \mathscr E_{\Lambda,T}(f)\bigr),}                        \tag{4.7}
\]

up to the same diagonal replacement of
`Tr(theta(h)P_Lambda)` by `2h(1)log Lambda` used in (1.5).  That replacement
has the established vanishing remainder in the semilocal trace theorem.

The new term is a boundary covariance defect, not the cross block (2.5),
but it carries the same missing information.

## 5. Expansion of the boundary covariance defect

Write the integrated representation as

\[
 A_f=\int f(u)\theta(u)\,d^\times u.                         \tag{5.1}
\]

For `w=uv^{-1}`, covariance gives

\[
 P_\Lambda\theta(w)=\theta(w)P_{\Lambda/|w|},
 \qquad
 \theta(u)J_{\Lambda,T}\theta(v)^*
 =\theta(w)P_{|v|\Lambda e^{-T}},                            \tag{5.2}
\]

with the harmless inverse convention changed if scaling is written on the
opposite side.  Therefore

\[
 \boxed{
 \mathscr E_{\Lambda,T}(f)
 =\iint f(u)\overline{f(v)}\,
 \theta(uv^{-1})
 \left(P_{\Lambda/|uv^{-1}|}
       -P_{|v|\Lambda e^{-T}}\right)
 d^\times u\,d^\times v.}                                  \tag{5.3}
\]

The row-C test is

\[
 h(w)=\int f(wv)\overline{f(v)}\,d^\times v.                \tag{5.4}
\]

Unlike (5.4), (5.3) depends on `v` separately through its boundary annulus.
It therefore does not factor through `h`.  On logarithmic volume the size of
that annulus is proportional to

\[
 T-\log|u|,                                                 \tag{5.5}
\]

not to either character `1` or `|v|` killed by (3.1).

The failure is visible on a primitive finite frame.  Put `q=2` and use
three logarithmic positions `0,R,2R`, where `e^(R/2)=q`.  Then

\[
 \mu=\delta_0-\frac52\delta_R+\delta_{2R}                    \tag{5.6}
\]

satisfies

\[
 \sum c_ne^{nR/2}=0,
 \qquad \sum c_ne^{-nR/2}=0,                                \tag{5.7}
\]

but its logarithmically weighted quadratic mass is

\[
 \sum_{n=0}^2n|c_n|^2={33\over4}\ne0.                       \tag{5.8}
\]

Replacing the deltas by sufficiently small disjoint bumps preserves the two
moment equations after an arbitrarily small coefficient correction and
keeps (5.8) nonzero.  Thus primitivity does not cancel the boundary weight
in (5.5).

> **Theorem 5.1 (guard-band defect).**  The D.76 guard-band lift is
> supported and its leakage is negative, but its exact trace differs from
> the semilocal corner character by (4.7).  The defect is a two-variable
> boundary covariance term and is not killed by the two primitive moments.

## 6. Place decomposition and mixed terms

The tensor Fourier transform `U_S` itself is placewise.  The local sum in
(1.6) appears only after descent to
`Z_S^times backslash A_S` and the transverse fixed-point trace.  At that
stage there are no unwanted `p^k q^ell` coefficients: the trace theorem
decomposes into the sum of the local distributions, giving precisely
(1.7).

Before the trace, however, the quotient and the common position cutoff
couple the factors.  Expanding a product lift place by place creates mixed
operator blocks.  They do not represent new arithmetic contacts; their
role is exactly to assemble the corner `P_hat P`.  Replacing that corner by
the self-adjoint supported compression discards the cross blocks and changes
the trace by (2.5) or (4.7).

Thus the answer to the mixed-term test is:

* arithmetic mixed coefficients cancel in the **established corner trace**;
* operator cross-window terms do not cancel on the primitive source;
* confusing these two statements is the false step that would turn the
  semilocal trace formula into a proof of the Hodge sign.

## 7. Consequence for the trace-exact lift

For the projected and guard-band candidates we now have exact formulas:

\[
 \begin{aligned}
 B_{{\rm nuc},T}
 &=\lim C_\Lambda,\\
 D_\Lambda^P&=C_\Lambda-E_\Lambda^P,\\
 D_{\Lambda,T}^G
 &=C_\Lambda-operatorname {Tr}igl(
 (\widehat P_\Lambda-P_\Lambda)\mathscr E_{\Lambda,T}\bigr).
 \end{aligned}                                               \tag{7.1}
\]

Both `D` terms are negative leakages.  Neither correction on the right is
zero by formal Poisson summation or by primitivity.

A successful lift must therefore incorporate a source-defined correction
`K_(Lambda,T)(f)` satisfying simultaneously

\[
 P_\Lambda(M_{\Lambda,T}^G+K)=M_{\Lambda,T}^G+K             \tag{7.2}
\]

and cancellation, after polarization, of the entire boundary covariance
defect (4.7).  Choosing `K` from the negative spectral part of `B_nuc` or
from the Julia contraction of D.76 would be circular.  The Poisson range
lift of D.74 retains the correct cross block but is not supported; the
compact potential lift is supported but does not retain it.  The missing
map is precisely a comparison between those two lifts.

## 8. Verdict

The semilocal Fourier--Poisson operator is explicit, and its renormalized
corner trace reproduces all `p^k` and Gamma.  The D.76 guard-band lift is
also explicit and supported.  They do not satisfy the desired trace
identity: the exact discrepancies are (2.5) and (4.7).

The two primitive moments do not remove these terms.  They remove a rank-two
polar quotient, whereas the Fourier--Poisson cross-window block has infinite
rank and the guard-band annulus carries an independent logarithmic weight.

Accordingly D.77 rules out the uncorrected guard-band theorem.  The surviving
construction problem is to build a supported correction that transports the
Poisson cross block rather than deleting it.  Row D is not declared closed.
