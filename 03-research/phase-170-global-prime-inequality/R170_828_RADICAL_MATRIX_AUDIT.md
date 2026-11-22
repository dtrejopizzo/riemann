# R170_828 — Audit of the radical multiscale matrix

R170_827 was built on a first attempt; an independent review and a final audit followed. The vanishing of the radical is not proved.

## Verdict

The corrected version of R170_827 is consistent. It provides an exact
finite matrix interface over \(Z=\ker H_T\), a faithful positive metric,
and a quantitative finite-rank approximation for the averaged collar.
It does not provide the two matrix inequalities that would close the
sign.

The first version contained a double count: it called the sum of the
four lines on the right-hand side of R170_823 a residual and then added
the interior energy to it again. This was corrected to

\[
 Q=K=P+E,
\]

where \(K\) polarizes the full multiscale form, \(P\) the exterior flux,
\(E\succeq0\) the interior energy, and \(Q\) the PC expansion of the four
lines. There is no implicit fifth term left over.

## Validated points

1. The Gram matrix \(B_{ij}=\langle R_LF_j,R_LF_i\rangle\) is positive
   definite because a single \(R_L\) is injective on the complete finite
   radical.
2. The Hermitization \((K^{raw}+K^{raw*})/2\) is the right one.
3. \(U_\rho\) is not assumed to preserve parity. A form can be restricted
   to \(Z_+\) or \(Z_-\), but the full matrix is not thereby block
   diagonal.
4. For a real weight, the averaged collar satisfies
   \(q(-\xi)=\overline{q(\xi)}\), from which \(q(D)J\) is self-adjoint.
   Its compression is Hilbert--Schmidt, not necessarily trace class nor
   positive.
5. The singular values satisfy
   \(s_{r+1}\le\|C\|_{HS}/\sqrt{r+1}\). This produces a rank-\(r\)
   approximation of the isolated collar. The term with
   \(\delta_\rho F\) needs its own bound.
6. The normalization \(\widehat K=B^{-1/2}KB^{-1/2}\) gives exactly the
   generalized ratio.

## Matrix map of the closure

The two pieces that would produce a contradiction are

\[
 P-(1-q_0)B\succeq0,
 \qquad P+E\preceq0.
\]

Together with \(E\succeq0\) and \(B\succ0\), they would imply

\[
 (1-q_0)B\preceq P\preceq-E\preceq0,
\]

which is impossible if \(Z\ne0\). The already-known Gamma--Euler
contraction proves that its own matrix is at least \((1-q_0)B\); it does
not prove that \(P\) dominates that matrix in the multiscale functional.
Inserting that comparison without a joint identity would be circular.

## Scope

The reduction is certifiable for a fixed contact if a rigorous basis of
\(Z\) and bounds for all the entries are available. That does not deliver
uniformity in \(T\), and it also does not yet use the dynamical property
that distinguishes the first contact from any semidefinite kernel.

The piece improves the architecture: any future joint cancellation can be
audited as an inequality between Hermitian matrices in the metric \(B\),
preserving correlations. Constructing at least one of the two inequalities
above by means of the arithmetic of the integers, and connecting the
other to minimality, remains to be done. The range of Paper 46 is not
extended, nor is D proved.
