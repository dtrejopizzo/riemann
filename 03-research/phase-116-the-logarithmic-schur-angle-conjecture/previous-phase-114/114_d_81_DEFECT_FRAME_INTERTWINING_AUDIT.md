# D.81 — Defect-frame intertwining and the primitive landing cocycle

## Status

D.80 writes the positive Schur channel as an infinite observability tower
and shows that its terminal trace boundary vanishes.  This note tests the
most direct candidate for the missing contraction: resolve the negative
source by the quadratic defect of the primitive average

\[
 D_R=(I-A_R^2)^{1/2}
\]

and map its orthogonal defect channels to the Schur channels one by one.

The source defect resolution is exact and unconditional.  The proposed
intertwining is not.  Even in the best commuting scalar model, every
diagonal stage-by-stage map becomes unbounded when a Poisson angle
`lambda` exceeds `||A_R||^2`; the prolate eigenvalues approach `1`, whereas
`||A_R||<1` for every fixed `R>0`.  In the actual semilocal representation
there is an additional exact failure: the negative landing operator does
not commute with scaling.  Its commutator is a sum of cutoff-annulus
operators, the same boundary covariance carried by D.77.

The coarse sufficient estimate `||q||<=2||L_-||` is also false on every
generic Halmos fiber and cannot follow from primitivity alone, because the
primitive ideal has a strong approximate identity.  The surviving
candidate is necessarily a non-diagonal Hankel/observability lifting which
absorbs the explicit boundary cocycle.  Contractivity of an arbitrary such
lifting is equivalent to row D; a noncircular construction must derive it
from cancellation of that cocycle.

All constructions remain before a sign and retain the row-C local
character.  No RH or spectral-sign selection is used.  The paper is not
modified.

## 1. The quadratic primitive defect frame

Fix `R>0` and put

\[
 A=A_R={S_R+S_{-R}\over2\cosh(R/2)},
 \qquad \eta_R=\|A\|={1\over\cosh(R/2)}<1.                 \tag{1.1}
\]

On the central logarithmic Hilbert representation, `A` is a self-adjoint
strict contraction.  Therefore

\[
 D=D_R=(I-A^2)^{1/2}                                      \tag{1.2}
\]

is bounded, positive and boundedly invertible.  Since `A` and `D` commute,

\[
 I=\sum_{j=0}^{N-1}A^jD^2A^j+A^{2N}.                      \tag{1.3}
\]

As `N` tends to infinity, (1.3) converges in operator norm and gives

\[
 \boxed{
 \|x\|^2=\sum_{j\ge0}\|DA^jx\|^2.}                      \tag{1.4}
\]

Thus

\[
 J_A:x\longmapsto(DA^jx)_{j\ge0}                         \tag{1.5}
\]

is an isometry.  It is the canonical defect-frame resolution associated
with the primitive averaging pair.

The square `D^2=I-A^2` is a compactly generated convolution operator and
commutes with every shift `S_(k log p)` and with `partial_infinity`.
Consequently insertion of (1.3) into the polarized row-C trace preserves
every `p^k` and Gamma term.  The square root `D` itself is generally a
noncompact convolution multiplier; (1.4) is a Hilbert defect resolution,
not a new compactly supported section functor.

## 2. The Schur observability frame

Use the notation of D.80.  On the generic Halmos part let

\[
 0<C=P\widehat PP<I,
 \qquad \beta=[C(I-C)]^{1/2}V.                             \tag{2.1}
\]

For `z=Vq` put

\[
 K_jz={1\over2}(I-C)^{1/2}C^{j/2}z,
 \qquad j\ge1.                                            \tag{2.2}
\]

The observability operator

\[
 \mathcal O_Cz=(K_jz)_{j\ge1}                             \tag{2.3}
\]

satisfies

\[
 \|\mathcal O_Cz\|^2={1\over4}\langle z,Cz\rangle
 \le {1\over4}\|z\|^2.                                  \tag{2.4}
\]

If `S_left` denotes the left shift on the sequence space, then

\[
 S_{\rm left}\mathcal O_C=\mathcal O_CC^{1/2}.             \tag{2.5}
\]

Likewise

\[
 S_{\rm left}J_A=J_AA.                                    \tag{2.6}
\]

Equations (2.5)--(2.6) make precise the proposed comparison: an indexed
intertwiner should relate the state contraction `C^(1/2)` to the primitive
average `A`.

## 3. Failure of diagonal stage matching

Consider first the most favorable scalar model in which both contractions
are simultaneously diagonal.  Let `C=lambda`, `A=a`, with

\[
 0<\lambda<1,
 \qquad |a|\le\eta_R<1.                                   \tag{3.1}
\]

The `j`th Schur channel has amplitude

\[
 {1\over2}\sqrt{1-\lambda}\,\lambda^{j/2},                \tag{3.2}
\]

whereas the `j`th negative defect channel has amplitude

\[
 \sqrt{1-a^2}\,a^j.                                      \tag{3.3}
\]

The unique scalar diagonal coefficient which maps (3.3) to (3.2) has

\[
 |t_j|^2
 ={1-\lambda\over4(1-a^2)}
   \left({\lambda\over |a|^2}\right)^j.                   \tag{3.4}
\]

Hence

\[
 \lambda>|a|^2\quad\Longrightarrow\quad
 \sup_j|t_j|=\infty.                                      \tag{3.5}
\]

At every expanding Fourier--Poisson window, the prolate spectrum of `C`
has eigenvalues arbitrarily close to `1`.  For fixed `R`,
`eta_R^2<1`, so eventually there are angle fibers with

\[
 \lambda>\eta_R^2\ge |a|^2.                               \tag{3.6}
\]

> **Proposition 3.1 (diagonal defect no-go).**  No uniformly bounded
> directed intertwiner can map the stages `D_R A_R^j` separately to the
> stages `K_j`.  The failure occurs even if covariance and domain issues are
> suppressed and the two contractions are assumed to commute.

Allowing `R` to tend to zero with the window makes `eta_R` tend to `1`, but
then

\[
 \inf\operatorname {spec}D_R
 =\sqrt{1-\eta_R^2}\longrightarrow0,                       \tag{3.7}
\]

so the inverse defect coordinate becomes unbounded.  This only moves the
same angle singularity between the two sides.

## 4. Exact covariance defect

Let `theta` be the multiplicative scaling representation on the semilocal
ambient space and define

\[
 \Theta_R={\theta(e^R)+\theta(e^{-R})\over2\cosh(R/2)}.     \tag{4.1}
\]

For the integrated source realization `R_src`, convolution gives

\[
 R_{\rm src}(A_RF)=\Theta_RR_{\rm src}(F).                 \tag{4.2}
\]

Scaling covariance of the position cutoff is

\[
 P_\Lambda\theta(u)=\theta(u)P_{\Lambda/|u|}.              \tag{4.3}
\]

It follows that

\[
 \boxed{
 [P_\Lambda,\Theta_R]
 ={1\over2\cosh(R/2)}
 \sum_{\epsilon=\pm1}\theta(e^{\epsilon R})
 \bigl(P_{\Lambda e^{-\epsilon R}}-P_\Lambda\bigr).}     \tag{4.4}
\]

The two summands in (4.4) are the inner and outer cutoff annuli.  They are
nonzero on every nontrivial window.

The negative landing operator obtained by completing the Halmos corner is

\[
 L_-(p,q)
 =(I-C)^{1/2}p-{1\over2}C^{1/2}Vq.                         \tag{4.5}
\]

It is built functorially from `P` and `P_hat`, so (4.4) propagates to a
nonzero commutator `[L_-,Theta_R]`.  Let

\[
 \mathscr D_R=(I-\Theta_R^2)^{1/2}.                        \tag{4.6}
\]

The exact failure of the desired stage intertwining is

\[
 \boxed{
 \mathfrak b_{j,R}(F)
 =[L_-,\mathscr D_R\Theta_R^j]R_{\rm src}(F).}             \tag{4.7}
\]

It splits as

\[
 [L_-,\mathscr D_R\Theta_R^j]
 =[L_-,\mathscr D_R]\Theta_R^j
 +\mathscr D_R\sum_{m=0}^{j-1}
   \Theta_R^m[L_-,\Theta_R]\Theta_R^{j-1-m}.              \tag{4.8}
\]

Because `||Theta_R||<1` on the central representation, functional calculus
gives the convergent formula

\[
 \begin{aligned}
 [L_-,\mathscr D_R]
 =\sum_{n\ge1}c_n\sum_{m=0}^{2n-1}
 \Theta_R^m[L_-,\Theta_R]\Theta_R^{2n-1-m},               \tag{4.9}
 \end{aligned}
\]

where

\[
 (1-z^2)^{1/2}=\sum_{n\ge0}c_nz^{2n}.                     \tag{4.10}
\]

Equations (4.4), (4.8) and (4.9) identify the failed term completely: it is
an infinite weighted propagation of the two cutoff annuli.  It is the
linear landing version of the quadratic boundary covariance defect (5.3)
of D.77.

## 5. Primitivity does not cancel the landing cocycle

D.75 constructs primitive measures `epsilon_T` whose integrated operators
converge strongly to the identity on every unitary scaling representation.
If (4.7) vanished on every primitive source vector for a fixed `j,R`, then
applying the primitive approximate identity to an arbitrary cyclic vector
and taking the strong limit would force

\[
 [L_-,\mathscr D_R\Theta_R^j]=0                            \tag{5.1}
\]

on the whole cyclic representation.  This contradicts the cutoff-annulus
formula (4.4) on the generic Poisson block.

Thus the two Tate moments do not supply the desired intertwining.  A
successful map must carry, rather than delete, the cocycle
`mathfrak b_(j,R)`.

## 6. Audit of the coarse Halmos bound

From (2.4), a sufficient condition for the row-D contraction would be

\[
 \|q(F)\|\le2\|L_-F\|.                                    \tag{6.1}
\]

This estimate is false on every generic scalar Halmos fiber.  For
`0<lambda<1`, formula (4.5) becomes

\[
 L_-(p,q)=\sqrt{1-\lambda}\,p
          -{\sqrt\lambda\over2}q.                          \tag{6.2}
\]

Taking

\[
 p={\sqrt\lambda\over2\sqrt{1-\lambda}}q,
 \qquad q\ne0,                                            \tag{6.3}
\]

gives

\[
 L_-(p,q)=0,
 \qquad {1\over4}\langle q,V^*CVq\rangle
       ={\lambda\over4}\|q\|^2>0.                        \tag{6.4}
\]

Hence (6.1) is not an ambient two-projection inequality.

Nor can (6.1) be deduced from the word “primitive” alone.  In any cyclic
scaling representation containing a vector of the form (6.3), its orbit
under the primitive approximate identity converges strongly to that
vector.  A uniform estimate on all primitive orbit vectors would pass to
the limit and contradict (6.4).  Therefore a proof of (6.1) would require a
new **landing theorem** saying that the actual A--B--C source avoids the
positive graph (6.3).  Such a theorem is stronger than primitivity and
support.

This does not prove that the A--B--C source contains an exact vector (6.3);
it proves that the proposed coarse estimate is not a formal consequence of
the structures presently used.

## 7. General non-diagonal comparison

Apply the defect isometry (1.5) to the negative coordinate and the
observability map (2.3) to the positive coordinate:

\[
 \begin{aligned}
 \mathcal J_-(F)&=(D_RA_R^jL_-F)_{j\ge0},\\
 \mathcal K_+(F)&=(K_jVq(F))_{j\ge1}.                     \tag{7.1}
 \end{aligned}
\]

Then

\[
 \|\mathcal J_-(F)\|^2=\|L_-F\|^2,
 \qquad
 \|\mathcal K_+(F)\|^2
 ={1\over4}\langle q(F),V^*CVq(F)\rangle.                \tag{7.2}
\]

A contraction `T` satisfying

\[
 \mathcal K_+(F)=T\mathcal J_-(F)                         \tag{7.3}
\]

would prove row D.  Conversely, the Douglas lemma shows that such a
contraction on the closures of the two ranges exists if and only if

\[
 B_{\rm nuc}(F,F)\le0                                     \tag{7.4}
\]

on the primitive source.  Thus choosing an arbitrary non-diagonal `T` is
not a construction; it is equivalent to the theorem sought.

There is, however, a more restrictive and noncircular candidate.  Because
of (2.5)--(2.6), ask for a **shift-intertwining** lifting.  Define the two
landing defects

\[
 \begin{aligned}
 e_-(F)&=L_-(A_RF)-A_RL_-(F),\\
 e_+(F)&=Vq(A_RF)-C^{1/2}Vq(F).                            \tag{7.5}
 \end{aligned}
\]

They are explicit cutoff-annulus cocycles by Section 4.  A source-defined
Hankel lifting must solve

\[
 S_{\rm left}\,T-TS_{\rm left}
 =\mathcal H(e_-,e_+),                                    \tag{7.6}
\]

where the right side is fixed by (7.5), not by the sign of `B_nuc`.
Equation (7.6), together with a norm-one estimate obtained from the Poisson
unitary, would yield (7.3).  This is the first candidate surviving both the
finite-chart Schur theorem and the diagonal growth test.

## 8. Conclusion

The quadratic defect resolution of the primitive average is exact,
Parseval and compatible with every prime-power and Gamma operator.  It does
not by itself construct the row-D contraction.

The diagonal comparison fails for the exact rate reason (3.4), and the
actual geometric comparison has the nonzero boundary cocycle (4.7).  The
coarse estimate `||q||<=2||L_-||` fails on the generic Halmos space and
cannot follow from primitivity alone.

The next concrete problem is no longer to guess a contraction.  It is to
solve the cocycle lifting equation (7.6) from the semilocal Poisson unitary
and prove its norm is at most one.  That construction would be independent
of the row-D sign; a generic Douglas factorization would not.

