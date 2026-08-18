# D.65 — Pilot-leaf width audit for the adaptive Arb manifest

The proposed first test leaf `[0.395,0.405]` was evaluated with
`h_target=0.001`, the factored off-diagonal kernel formula, `rho=10`, and
the complete D.63 residual subtraction.

The fixed mesh has

\[
 m_b=117,\qquad m_m=598,\qquad n=832=416+416.
\]

After subtracting the worst residual, the midpoint parity minima are

\[
 \lambda_e(0.4)=0.1128900\ldots,qquad
 \lambda_o(0.4)=0.1059453\ldots.
\]

Both endpoint diagnostics remain positive.  Nevertheless the leaf cannot
be certified by midpoint plus Frobenius variation:

\[
 \|R(.395)-R(.4)\|_F=0.54036\ldots,qquad
 \|R(.405)-R(.4)\|_F=0.52490\ldots.
\]

These exceed the midpoint gap by a factor about five.  The corresponding
operator-norm diagnostics, `0.4385` and `0.4271`, show that this is genuine
geometric variation, not exponential-cancellation inflation.

Therefore the recursive manifest must bisect this range to radii of order
`5*10^-4` (with further adaptive reduction where the certified margin
shrinks).  No certificate for the width-`0.01` pilot leaf is claimed.

## 2. A complete rescaled-boundary bridge at the first threshold

The failure of the deliberately wide pilot leaf is unrelated to the
singularity of the newborn overlap.  That endpoint is handled analytically.
Put

\[
 T_2={\log2\over2},\qquad \delta=2T-\log2.
\]

The directed endpoint certificate
`114_d_65_endpoint_penalty_verify.py` proves on the **full**, not merely
primitive, endpoint space

\[
 q_{19,T_2}+10H>0.0783I.                                  \tag{2.1}
\]

For `T>T_2`, decompose `[-T,T]` into the middle interval

\[
 M=[T-\log2,\log2-T]
\]

and the two boundary intervals paired by `S_(log2)`.  Their union `B` has
measure `2 delta`.  After zero-extending `L^2(M)` into the endpoint window,
the middle--middle block is exactly a compression of the operator in
(2.1), hence remains greater than `0.0783 I`.

On the boundary pair, `J=S_(log2)+S_(-log2)` has norm one.  Since
`K_19(x,y)<=20`, Schur's test gives

\[
 A_{BB}\geq(C_{19}-c-40\delta)I
          >(1.3483-40\delta)I.                            \tag{2.2}
\]

The kernel cross block obeys

\[
 \|K_{MB}\|\leq20\sqrt{|M||B|}
 <24\sqrt\delta.                                         \tag{2.3}
\]

For `delta<=37*10^(-6)` one has `T<0.35`, hence

\[
 \|h_\pm\|_{M}<0.846,
 \qquad \|h_\pm\|_B<1.686\sqrt\delta.
\]

The cross block of `10H` is therefore smaller than
`10*2*0.846*1.686 sqrt(delta)<28.54 sqrt(delta)`.  Combining it with
(2.3) gives the directed round bound

\[
 \|A_{MB}\|<53\sqrt\delta.                               \tag{2.4}
\]

The scalar Schur comparison matrix is

\[
 \begin{pmatrix}
 0.0783&-53\sqrt\delta\\
 -53\sqrt\delta&1.3483-40\delta
 \end{pmatrix}.                                         \tag{2.5}
\]

For `0<=delta<=37*10^(-6)`, both diagonal entries are positive and

\[
 53^2\delta
 \leq0.103933
 <0.0783(1.3483-40\cdot37\,10^{-6}).                    \tag{2.6}
\]

Thus (2.5), and hence `q_(19,T)+10H`, is strictly positive throughout this
whole interval.  On primitive vectors the `10H` term vanishes; the omitted
Gamma channels are nonnegative.  Consequently

\[
 \boxed{QW_T>0\quad
 \left(T_2\leq T\leq T_2+{37\over2\,10^6}\right).}     \tag{2.7}
\]

This bridge is macroscopic relative to D.61 and contains no unspecified
`O(delta)` term.  The rational verifier checks the enlarged determinant
inequality exactly.  The remaining manifest starts at its right endpoint.
