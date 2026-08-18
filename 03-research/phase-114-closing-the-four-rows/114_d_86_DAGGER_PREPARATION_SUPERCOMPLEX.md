# D.86 — The dagger-preparation supercomplex and the minimal global block

## Status

D.85 constructs a round-trip colligation whose output is exactly the Schur
tower and isolates the initial residual `r_0=2L_-`.  This note attempts to
make that residual the differential of a source-defined dagger complex and
to obtain the boundary domination from exactness or contractibility.

There is a canonical complex, but its exact metric is Krein rather than
Hilbert.  With the grading required by the row-C character, its pullback is
`-4 B_nuc`.  On every generic Halmos angle the resulting matrix has zero
auxiliary diagonal, nonzero cross term and negative determinant.  Replacing
the grading by an ordinary positive metric gives a sum of the residual and
boundary norms and no longer computes `B_nuc`.

Koszul or Clifford stabilization preserves this distinction: a supertrace
recovers the signed prime--Gamma character, while an ordinary trace is
positive but computes a different form.  Exactness supplies no inequality
between the even and odd pieces unless the boundary map factors
contractively through the differential; that factorization is row D.

No finite set of prime blocks joined to Gamma can give a pointwise positive
dagger either.  Its defect multiplier is negative at central frequency.
The first block where cancellation could occur is the complete
support-compressed, two-jet, all-active-prime--Gamma block; its positivity is
precisely the unresolved global inequality, not a local determinant fact.

No RH, spectral norm defined from `B_nuc`, or sign-selected subspace is used.
The paper is not modified.

## 1. The round-trip boundary operator

Let

\[
 C=T^*T,
 \qquad D_T=(I-C)^{1/2},
 \qquad z=Vq.                                              \tag{1.1}
\]

D.85 constructs the round-trip observability map

\[
 \mathcal O_Cz=(K_jz)_{j\ge1},                             \tag{1.2}
\]

with

\[
 \|\mathcal O_Cz\|^2
 ={1\over4}\langle z,Cz\rangle.                           \tag{1.3}
\]

The preparation residual is

\[
 r_0(p,z)=2D_Tp-C^{1/2}z=2L_-(p,q).                        \tag{1.4}
\]

Consequently the exact primitive form is

\[
 \boxed{
 -4B_{\rm nuc}(F,F)
 =\|r_0(p(F),z(F))\|^2
  -\|C^{1/2}z(F)\|^2.}                                    \tag{1.5}
\]

The second norm in (1.5) is four times the complete output norm (1.3), so
it contains every even and odd round-trip Schur channel.

## 2. Canonical preparation supercomplex

Put

\[
 \mathcal P^0=PH\oplus PH,
 \qquad
 \mathcal P^1=PH\oplus PH,                                \tag{2.1}
\]

and define

\[
 \mathcal Q:\mathcal P^0\longrightarrow\mathcal P^1,
 \qquad
 \mathcal Q(p,z)=
 \bigl(2D_Tp-C^{1/2}z,\ C^{1/2}z\bigr).                   \tag{2.2}
\]

The first target component is the differential/preparation residual and
the second is the compressed round-trip boundary.  Give the target the
fundamental symmetry

\[
 J=\begin{pmatrix}I&0\\0&-I\end{pmatrix}.                 \tag{2.3}
\]

Then

\[
 \langle\mathcal Q(p,z),J\mathcal Q(p,z)\rangle
 =\|r_0(p,z)\|^2-\|C^{1/2}z\|^2.                          \tag{2.4}
\]

By (1.5), the pullback of (2.4) along the primitive A--B--C realization is
exactly `-4 B_nuc`, including all prime powers and Gamma.

In block form,

\[
 \boxed{
 \mathcal Q^*J\mathcal Q
 =\begin{pmatrix}
 4(I-C)&-2D_TC^{1/2}\\
 -2C^{1/2}D_T&0
 \end{pmatrix}.}                                          \tag{2.5}
\]

The zero bottom corner is not a normalization accident: the positive
`z*Cz` term in `r_0*r_0` is exactly the boundary energy which the
supergrading subtracts.

## 3. Ambient dagger positivity is impossible

On a scalar angle `0<lambda<1`, (2.5) is

\[
 \begin{pmatrix}
 4(1-\lambda)&-2\sqrt{\lambda(1-\lambda)}\\
 -2\sqrt{\lambda(1-\lambda)}&0
 \end{pmatrix}.                                           \tag{3.1}
\]

Its determinant is

\[
 -4\lambda(1-\lambda)<0.                                 \tag{3.2}
\]

Thus it has one positive and one negative direction.  Equivalently, on

\[
 p={1\over2}D_T^{-1}C^{1/2}z                              \tag{3.3}
\]

the differential component is zero and the boundary component is nonzero.

> **Proposition 3.1 (dagger ambient no-go).**  No positive dagger metric on
> the ambient preparation object can have pullback (2.5).  Positivity can
> hold only after proving that the actual primitive image avoids the graph
> (3.3), or after changing the character.

If the ordinary positive metric is used on the target instead of `J`, then

\[
 \mathcal Q^*\mathcal Q
 \quad\text{pulls back to}\quad
 \|r_0\|^2+\|C^{1/2}z\|^2\ge0.                            \tag{3.4}
\]

This is a valid dagger Laplacian, but it differs from `-4 B_nuc` by

\[
 2\|C^{1/2}z\|^2.                                        \tag{3.5}
\]

It cannot be used as the row-D form.

## 4. Exactness and contractibility do not order a supercomplex

One may enlarge (2.2) to a Koszul or Clifford complex with a contracting
homotopy.  Its ordinary Laplacian is a sum of positive squares, while its
supertrace is the alternating difference (2.4).  Contractibility gives an
algebraic cancellation of Euler classes; it does not imply

\[
 \|C^{1/2}z\|\le\|r_0(p,z)\|.                              \tag{4.1}
\]

Indeed, the vector (3.3) is already a contractible two-term pair with zero
differential image and nonzero odd boundary.

More generally, a Hilbert complex could imply (4.1) only if the boundary
operator factored through the differential:

\[
 C^{1/2}z=\mathcal A r_0(p,z),
 \qquad \|\mathcal A\|\le1.                               \tag{4.2}
\]

By Douglas factorization, existence of (4.2) on the primitive image is
equivalent to (4.1), hence to row D.  Adding infinitely many Clifford
generators cancels cross-place monomials in the **supertrace**, but does not
construct (4.2).

At finite cutoff, solving algebraically for `p` uses `D_T^(-1)`.  The
prolate eigenvalues of `C` approach one, so this homotopy is unbounded in
the directed limit.  Thus finite contractibility does not yield a
continuous contracting homotopy in the required Frechet/pro category.

## 5. Local prime--Gamma dagger block

For a finite set of primes `P`, the exact feature maps of D.76 give

\[
 \begin{aligned}
 \mathbf S_PF&=((\sqrt{\log p}\,A_pF)_{p\in P},
                   \sqrt{m_0}F),\\
 \mathbf B_PF&=((\sqrt{\log p}\,F)_{p\in P},
                   \partial_\infty F).                    \tag{5.1}
 \end{aligned}
\]

The candidate positive dagger defect is

\[
 \Delta_P=\mathbf B_P^*\mathbf B_P-\mathbf S_P^*\mathbf S_P.
                                                                  \tag{5.2}
\]

On the central Fourier variable its scalar multiplier is

\[
 \delta_P(\tau)
 =-m_\infty(\tau)
 +\sum_{p\in P}\log p
  \left(1-P_{p^{-1/2}}(e^{i\tau\log p})\right).            \tag{5.3}
\]

At `tau=0`,

\[
 m_\infty(0)=m_0>0,
 \qquad
 1-P_r(1)=-{2r\over1-r}<0.                                \tag{5.4}
\]

Therefore

\[
 \boxed{\delta_P(0)<0}                                    \tag{5.5}
\]

for every finite `P`, including the empty set.  No finite prime--Gamma
feature block is pointwise dagger-positive.

This does not refute row D: compact support and the two Tate conditions do
not permit arbitrary pointwise spectral localization uniformly through the
support exhaustion.  It proves that positivity cannot be supplied by a
fiberwise star-functor before compression.

The smallest block in which global cancellation can even be formulated is

\[
 \boxed{
 \Delta_T^{\rm comp}
 =P_{\rm prim,T}\left(
 \partial_\infty^*\partial_\infty-m_0I
 +\sum_{p\le e^{2T}}\log p\,(I-A_p^*A_p)
 \right)P_{\rm prim,T},}                                  \tag{5.6}
\]

with every prime active on the support window, all powers already contained
in `A_p* A_p`, the complete Gamma oscillator, and the two-jet projection.
No proper finite-place subblock has the required local sign.  Positivity of
(5.6) for all `T` is the compressed form of row D itself.

## 6. Determinant obstruction to a local positive trace

The periodic/Yoneda contact functional satisfies

\[
 \ell(1)=0,
 \qquad \ell(\delta_p)=\ell(\delta_{p^2})=\log p.          \tag{6.1}
\]

On `{1,delta_p}` its star-Gram matrix is

\[
 \begin{pmatrix}0&\log p\\\log p&\log p\end{pmatrix},   \tag{6.2}
\]

with determinant `-(log p)^2`.  Hence no local positive dagger trace can
retain the contact determinant.

Adding a scalar positive diagonal `gI` would replace (6.2) by

\[
 \begin{pmatrix}g&\log p\\\log p&g+\log p\end{pmatrix}.   \tag{6.3}
\]

Even in this oversimplified model, positivity requires

\[
 g(g+\log p)\ge(\log p)^2,
 \qquad
 g\ge {\sqrt5-1\over2}\log p.                            \tag{6.4}
\]

The true Gamma channel is not such a scalar diagonal and, by (5.5), does
not repair the local block.  Formula (6.4) is only a quantitative lower
bound showing that an arbitrarily small archimedean perturbation cannot
make the prime contact positive.

## 7. What periodic Yoneda does and does not impose

The enriched Yoneda construction gives actual effective section objects,
Day multiplication, representable internal Hom and a positive ordered
extremal frame after real realization.  It does not impose a relation
between the two Halmos coordinates `p,z` in (2.2).  In particular, the
reduced prime contact has zero periodic component in the IDN pullback; its
von Mangoldt mass lives in the common nuclear coefficient component.

Therefore no existing Yoneda morphism excludes the positive graph (3.3).
Declaring the preparation object to be the orthogonal complement of that
graph would select the sign of (2.5) and be circular.

A genuine dagger preparation must instead be a new natural transformation

\[
 \mathfrak p_\dagger:
 \mathbf R\Gamma_{\rm per}(\mathcal F_{\rm per})
 \longrightarrow\mathcal P^0                              \tag{7.1}
\]

whose image satisfies (4.2) by a categorical support or duality theorem.
The norm on its source must come from periodic section geometry, not from
`B_nuc`; the ordered-frame Euclidean norm alone has no map with the required
round-trip boundary.

## 8. Conclusion

The canonical dagger-preparation complex has been constructed.  Its
supermetric pulls back exactly to `-4 B_nuc`, but it is a Krein form with an
indefinite generic angle block.  An ordinary positive dagger metric computes
a different form.  Exact/Koszul/Clifford stabilization does not change this
fact.

No finite prime--Gamma feature block is pointwise positive; the first
possible cancellation object is the complete compressed operator (5.6),
whose positivity is row D.  Periodic Yoneda currently supplies no landing
relation excluding the positive graph.  The remaining constructive target
is the natural transformation (7.1) together with a source-derived
factorization (4.2).
