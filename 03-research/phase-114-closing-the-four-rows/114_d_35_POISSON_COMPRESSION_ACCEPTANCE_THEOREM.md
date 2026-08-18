# D.35 — Exact Poisson compression acceptance theorem

## 1. The universal compression identity

Let `H` be a Hilbert space, `P` an orthogonal projection, `U` a unitary,
and put

\[
 A_U=U^*PU-P.                                         \tag{1.1}
\]

For every `x in Ran(P)`,

\[
 \langle x,A_Ux\rangle
 =\|PUx\|^2-\|x\|^2
 =-\|(1-P)Ux\|^2\le0.                               \tag{1.2}
\]

More generally, if `M:K -> H` is Hilbert--Schmidt and `PM=M`, then

\[
 \mathrm{Tr}(M^*A_UM)
 =-\|(1-P)UM\|_{\rm HS}^2.                           \tag{1.3}
\]

### Proof

Since `Px=x` and `U` is unitary,

\[
 \langle x,U^*PUx\rangle=\|PUx\|^2,qquad
 \|Ux\|^2=\|x\|^2.
\]

Pythagoras gives (1.2).  Apply (1.2) to an orthonormal basis of `K`, sum
the nonnegative terms by Tonelli, and obtain (1.3).

If `F_P=2P-1` and the quantized differential is
`-dU=[F_P,U]`, then

\[
 \frac12U^*(-dU)=U^*PU-P=A_U.                        \tag{1.4}
\]

Thus (1.3) is exactly the non-circular sign mechanism sought in the
semilocal trace formula: it is a squared norm before any explicit-formula
or zero calculation.

## 2. Application to the Crofoot assembly

For the finite prime set `P_Q`, D.34 constructs a unitary

\[
 \mathcal C_Q:K_{Z_Q}\longrightarrow K_{B_Q}.         \tag{2.1}
\]

After identifying the two model spaces inside one semilocal boundary
space, let `P_Z` denote the projection onto `K_(Z_Q)` and extend
`mathcal C_Q` to a unitary `U_Q` of the ambient space.  Then

\[
 P_B=U_QP_ZU_Q^*,                                    \tag{2.2}
\]

and the finite part of D.34 can be written as

\[
 K_Q(F,F)=
 \mathrm{Tr}\,\left(M_{\widehat F}^*M_{\widehat F}
                 (P_B-P_Z)\right).                  \tag{2.3}
\]

Equation (2.3) is independent of the chosen unitary extension because it
only contains the two canonical model-space projections.

The Gamma oscillator supplies a second unitary Fourier block and a pair of
projections whose renormalized projection difference is
`m_0||F||^2-||partial_infinity F||^2`.  Hence the completed form is one
paired projection-difference trace.

## 3. The exact sufficient theorem

Let `H_Q^adel` be the semilocal Poisson Hilbert space with its self-dual
additive Fourier transform `U_Q^adel`, and let `P_Q^adel` be the support
projection selected by the two-sided window.  Suppose one constructs,
functorially from the periodic Yoneda section associated with `F`, a
Hilbert--Schmidt operator

\[
 \mathcal M_Q(F):K_Q\longrightarrow H_Q^{adel}        \tag{3.1}
\]

with the following three properties:

\[
 P_Q^{adel}\mathcal M_Q(F)=\mathcal M_Q(F),           \tag{3.2}
\]

\[
 \mathrm{Tr}\,\left(\mathcal M_Q(F)^*
   \bigl((U_Q^{adel})^*P_Q^{adel}U_Q^{adel}-P_Q^{adel}\bigr)
   \mathcal M_Q(F)\right)=B_Q(F,F),                  \tag{3.3}
\]

and

\[
 \mathcal M_Q(F)=0\Longrightarrow F=0
 \quad\text{on }\widehat F(i/2)=\widehat F(-i/2)=0.  \tag{3.4}
\]

Then (1.3) gives

\[
 B_Q(F,F)=-\|(1-P_Q^{adel})U_Q^{adel}
                  \mathcal M_Q(F)\|_{\rm HS}^2\le0. \tag{3.5}
\]

If the constructions commute with `Q<Q'` and (3.3) stabilizes on compact
supports, the cofinal limit proves row D.  If the map in (3.5) separates
primitive sections, equality is strict.

This theorem is a sufficient contract, not a restatement of the desired
sign: (3.2) is a support theorem and (3.3) is an operator comparison which
can in principle be checked before taking a sign.

## 4. Why the raw multiplier does not satisfy the contract

The first candidate is the boundary multiplication operator
`M_(widehat F)`.  It gives the correct trace (D.34), but the two equations

\[
 \widehat F(i/2)=\widehat F(-i/2)=0                  \tag{4.1}
\]

do not imply

\[
 P_Q^{adel}M_{\widehat F}=M_{\widehat F}.             \tag{4.2}
\]

Indeed, a nonzero multiplication operator on the full boundary `L^2` has
range supported wherever its argument is supported; two point evaluations
of its analytic symbol do not force a Hardy or physical-space support
condition on that range.  Replacing it by `P_Q M_(widehat F)` forces (3.2)
but changes the trace in (3.3).  D.14 proves that this discrepancy has
infinite rank and cannot be repaired by a freely chosen two-by-two boundary
matrix.

Therefore the missing object is not another projection.  It is the
**Poisson lift** `mathcal M_Q(F)` which must simultaneously:

1. land in the support subspace by the global Poisson formula;
2. retain the Crofoot prime-power contact and Gamma oscillator trace;
3. turn the two Tate evaluations into the two Poisson boundary conditions;
4. be compatible with semilocal exhaustion.

Constructing this lift and proving (3.2)--(3.4) is the precise live route
to the contraction.  Defining it as a square root of `-B_Q`, or selecting
its range from the negative spectral subspace, would be circular and is
excluded.

