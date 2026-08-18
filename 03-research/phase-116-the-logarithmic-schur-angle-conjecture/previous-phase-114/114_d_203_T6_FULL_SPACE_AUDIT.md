# Full-space audit at \(T=\tfrac12\log 6\)

## Verdict

The endpoint is **not yet certified on the full Hilbert space**.  Two parts
are rigorous and positive:

1. the primitive complement of the constrained Legendre space \(V_{200}\)
   has directed lower gap
   \[
   \delta_Q>0.2199999999999998;
   \]
2. the complete primitive compression to \(V_{200}\), with the Gamma place,
   \(m_0\), both Tate equations and contacts \(2,3,4,5\), is positive.  In
   the stable native-Arb whitening its final two-by-two determinant has lower
   endpoint
   \[
   2.01637550\times10^{-30}.
   \]

These statements do not by themselves prove positivity of the coupled
operator.  A proof which combines them while omitting the coupling between
the finite safe block and \(V_{200}^{\perp}\) is invalid.

## 1. The exact three-block obligation

Write the operator relative to a delicate finite block \(D\), a safe finite
block \(S\), and the infinite complement \(Q\):

\[
 A=\begin{pmatrix}
 A_{DD}&A_{DS}&C_D\\
 A_{SD}&A_{SS}&C_S\\
 C_D^*&C_S^*&A_{QQ}
 \end{pmatrix},
 \qquad A_{QQ}\ge\delta_Q Q.
\]

Assume \(A_{SS}>0\), and put

\[
 \kappa=\|C_S^*A_{SS}^{-1/2}\|^2,
 \qquad
 C_{\rm eff}=C_D-A_{DS}A_{SS}^{-1}C_S.
\]

Elimination of \(S\), not a formal replacement of \(A_{QQ}\) by
\(\delta_Q I\), gives

\[
 A_{QQ}^{\rm eff}
 =A_{QQ}-C_S^*A_{SS}^{-1}C_S
 \ge(\delta_Q-\kappa)Q.
\]

Consequently a sufficient directed certificate consists of

\[
 \kappa<\delta_Q
\]

and

\[
 A_{DD}-A_{DS}A_{SS}^{-1}A_{SD}
 -(\delta_Q-\kappa)^{-1}C_{\rm eff}C_{\rm eff}^*>0.
\]

This is the criterion that remains to be certified.

## 2. Direct audit of the apparent negative Ritz directions

An inherited five-column Schur graph initially produced negative midpoint
eigenvalues.  That calculation was not directed: its interval radii reached
\(255\)--\(272\), and its Tate residuals had radii \(1.55\).  It therefore
certified no sign.

Freezing only each candidate's Legendre tail, resolving the two Tate
coefficients in Arb, and evaluating the complete operator without a Schur
inverse gives instead

\[
 q_1=[4.404883\times10^{-9}\pm4.01\times10^{-16}],
\]

\[
 q_2=[1.476\times10^{-12}\pm4.00\times10^{-16}].
\]

Both candidates are strictly positive.  Their Tate residuals are bounded by
\(2.6\times10^{-1100}\).  Thus there is no certified negative vector at this
endpoint.

## 3. Coupling diagnostics and their scope

The rectangular rows \(200{:}260\) were rebuilt at 1600 decimal digits and
cached before changing finite splittings.  These data remain diagnostics
because the contacts in the rectangular block use binary64 centres.

For the raw split after two slow Ritz directions, the generalized band
coupling has

\[
 \kappa_{200:260}^{\rm diag}=0.31854644.
\]

Thus the uniform complement gap cannot absorb the raw safe block.

Imposing twenty vanishing jets at each endpoint leaves an endpoint-flat
safe space of dimension \(156\).  On that space the same band has

\[
 \kappa_{200:260}^{\rm flat}=0.27044883.
\]

After promoting the thirty largest generalized singular directions, the
sum of all remaining band singular squares is

\[
 0.04396309.
\]

This leaves numerical room below \(\delta_Q\), but it is not a theorem: the
rows beyond 260 and the corrected cross \(C_{\rm eff}\) still require
directed bounds.

The appropriate bridge is a Legendre tail, not the crude Fourier tail at
frequency 150.  If \(g\in H^m(-1,1)\) and \(p_n\) are the normalized
Legendre polynomials, Jacobi integration by parts and Bessel's inequality
give the sharp associated-Legendre estimate

\[
 \sum_{n\ge N}|\langle g,p_n\rangle|^2
 \le c_{N,m}\int_{-1}^1(1-u^2)^m|g^{(m)}(u)|^2\,du,
 \qquad
 c_{N,m}^{\sharp}={ (N-m)!\over(N+m)!}.
\]

For \(m=20\),

\[
 c_{230,20}^{\sharp}<3.274\times10^{-95},\qquad
 c_{260,20}^{\sharp}<2.426\times10^{-97}.
\]

Here \(g=A F\).  The endpoint-log decomposition shows that, for
\(F=(1-u^2)^{20}P\), the singular pieces are of the form
\((1-u^2)^{20}P\log(1\pm u)\); translated contacts are piecewise
\(C^{19}\).  Hence the weighted twentieth-derivative integral is finite and
can be evaluated from beta/logarithmic moments.  To spend at most \(0.05\)
 at cutoff 260 it is enough to certify, in the normalized \(u\)-coordinate,
 the corresponding trace bound

\[
 J_{20}<2.0615\times10^{95}.

Equivalently, when derivatives and integration are kept in the physical
\(t\)-coordinate, the coefficient is
\(c_{260,20}^{\sharp}T^{40}<2.984\times10^{-99}\) and the budget is
\(1.6757\times10^{97}\).  Mixing these two coordinate conventions would
invalidate the bound.
\]

That interval evaluation of \(J_{20}\) has not yet been completed.  It must
also include the primitive graph correction; the independent complement
audit bounds its norm by \(6.58\times10^{-505}\), so it is negligible but
not silently set to zero.  Thus endpoint flatness supplies a rigorous route
to the missing tail, not yet the numerical enclosure required to close it.

## 4. Reproducible artifacts

- `/tmp/t6_whitened_native_schur.npz`: rigorous finite \(V_{200}\) Schur
  output.
- `/tmp/t6_safe2_band260_diagnostic.npz`: rectangular band, generalized
  Gram and singular spectrum for the raw slow-two split.
- `/tmp/t6_flatM20_safe2_band260.npz`: endpoint-flat diagnostic split.
- `114_d_185_log6_complement_arb.py`: directed infinite-complement gap.
- `114_d_189_t6_direct_witness_arb.py`: Schur-free directed evaluation of
  the two apparent negative candidates.
- `114_d_199_t6_whitened_native_schur.py`: stable native-Arb finite-block
  certificate.
- `114_d_200_t6_safe_coupling_diagnostic.py`: cached rectangular coupling
  and generalized singular-value audit.
- `114_d_204_legendre_tail_bridge_verify.py`: exact factorial coefficient
  and remaining derivative-budget audit for the Legendre tail.

The `/tmp` files are working artifacts, not public archival certificates.
The certified statements above are reproducible from the named scripts;
the coupling values are explicitly labelled diagnostic.
