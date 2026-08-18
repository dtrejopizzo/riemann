# D.170 — Exact output-defect channel reduction

## Verdict

After the born annulus is orthogonalized in the **complete positive
reference metric**, its cross with the old defect factors exactly through
the old comparison operator.  There is no extra Gamma, Tate or
prime-power remainder in that factorization.

Let (X=(X_0,X_E)) be the reference feature map and
(Y=(Y_0,Y_E)) the load feature map of D.137, split into old-core and
born-boundary source variables.  The entries of (X) contain the complete
Gamma screw and every (J_{p^k,-}); the entries of (Y) contain the
(\beta)-line, the resolvent and every (J_{p^k,+}).  Both are already
restricted by the exact two-Tate projection.

After the reference Cholesky transform, the full comparison has the column
form

\[
 \boxed{\mathcal A_N=(A_N,y_N).}                      \tag{0.1}
\]

Consequently its defect is

\[
 I-\mathcal A_N^*\mathcal A_N=
 \begin{pmatrix}
 I-A_N^*A_N&-A_N^*y_N\\
 -y_N^*A_N&I-y_N^*y_N
 \end{pmatrix}.                                      \tag{0.2}
\]

Thus the D.168 cross vector is exactly

\[
 \boxed{z_N=A_N^*y_N.}                               \tag{0.3}
\]

If the old comparison is a contraction, positivity of the enlarged cell
is equivalent to the **output-defect capacity**

\[
 \boxed{
 y_N^*(I-A_NA_N^*)^\dagger y_N\le I.}                \tag{0.4}
\]

Equivalently, there must exist a contraction (v_N) such that

\[
 \boxed{y_N=(I-A_NA_N^*)^{1/2}v_N.}                  \tag{0.5}
\]

The atomic centered discrepancy has therefore been located precisely: it
is not a residual in (0.3); it is the component of the explicitly
orthogonalized boundary load (y_N) in the small spectral layers of the
**output** defect (I-A_NA_N^*).

## 1. Reference Cholesky transform

Put

\[
 R_0=X_0^*X_0,\qquad r=X_0^*X_E.                    \tag{1.1}
\]

On the supported range, define the reference harmonic lift and residual

\[
 H=R_0^\dagger r,\qquad
 \widetilde X_E=X_E-X_0H,\qquad
 S_E=\widetilde X_E^*\widetilde X_E.                 \tag{1.2}
\]

Then (X_0^*\widetilde X_E=0).  The normalized reference columns

\[
 \widehat X_0=X_0R_0^{\dagger/2},\qquad
 \widehat X_E=\widetilde X_ES_E^{\dagger/2}          \tag{1.3}
\]

are orthonormal on their supported ranges and mutually orthogonal.  Apply
the same triangular source change to the load features:

\[
 \boxed{
 A_N=Y_0R_0^{\dagger/2},\qquad
 y_N=(Y_E-Y_0H)S_E^{\dagger/2}.}                     \tag{1.4}
\]

Equations (1.3)--(1.4) prove (0.1).  They are identities between the
complete feature maps.  In particular:

* every (p^k\le e^{2T}) is present in the (J_{p^k,\pm}) components;
* the full Gamma integral is present in (X_0,X_E);
* the (\beta) and (Q_{1/2}) channels are present in (Y_0,Y_E); and
* the same Tate projection is applied before the split.

No term can appear outside (1.4) after the common source transform.

## 2. Output Schur identity

Let

\[
 D_{\rm in}=I-A_N^*A_N,\qquad
 D_{\rm out}=I-A_NA_N^*.                            \tag{2.1}
\]

Assume (D_{\rm in}\ge0), which is the old-cell induction hypothesis.
Shorting the upper-left corner of (0.2) gives

\[
 I-y_N^*y_N-y_N^*A_ND_{\rm in}^\dagger A_N^*y_N.     \tag{2.2}
\]

The push-through identity

\[
 I+A_ND_{\rm in}^\dagger A_N^*=D_{\rm out}^\dagger \tag{2.3}

\]

holds on the supported range, with the usual kernel condition.  Hence
(2.2) equals

\[
 I-y_N^*D_{\rm out}^\dagger y_N,                     \tag{2.4}
\]

which proves (0.4).

Douglas factorization applied to (y_N) and
(D_{\rm out}^{1/2}) proves the equivalence with (0.5).  The intertwining
identity

\[
 D_{\rm in}^{1/2}A_N^*=A_N^*D_{\rm out}^{1/2}        \tag{2.5}

\]

then gives

\[
 z_N=A_N^*y_N
 =D_{\rm in}^{1/2}A_N^*v_N,                          \tag{2.6}
\]

which is exactly the input-defect factorization sought in D.169.

## 3. Explicit channel formula for the boundary load

Substituting D.137 into (1.4) gives

\[
\begin{aligned}
 Y_E-Y_0H={}&
 \bigl(
 \sqrt\beta\,(P_TE-P_TH),\;
 Q_{1/2}(P_TE-P_TH),\\
 &\qquad
 (\sqrt{w_{p^k}}J_{p^k,+}(P_TE-P_TH))_{p^k\le e^{2T}}
 \bigr),                                             \tag{3.1}
\end{aligned}
\]

where (E) denotes boundary injection and (H) is the reference harmonic
lift (1.2).  The corresponding reference residual is

\[
\begin{aligned}
 \widetilde X_E={}&
 \bigl(
 D_\infty(P_TE-P_TH),\\
 &\qquad
 (\sqrt{w_{p^k}}J_{p^k,-}(P_TE-P_TH))_{p^k\le e^{2T}}
 \bigr).                                             \tag{3.2}
\end{aligned}
\]

Thus (S_E) is the exact positive capacity of the Gamma plus
antisymmetric contact channels, while (y_N) is the symmetric/Tate load
of the same reference-harmonic residual.

The Hadamard rotation pairs the (J_+) and (J_-) components of
(3.1)--(3.2).  The continuous part of their mismatch is the convolution
kernel (M_N) of D.167 and is killed by the two Tate moments.  The
remaining output component is exactly the centered polynomial

\[
 E_N(\tau)=\sum_{n\le N}{\Lambda(n)\over\sqrt n}
 e^{-i\tau\log n}-{N^{1/2-i\tau}-1\over1/2-i\tau}.    \tag{3.3}
\]

Equation (3.3) is not an omitted summand: it is part of (y_N) in
(3.1).  The final theorem is the output Carleson estimate

\[
 y_N^*D_{\rm out}^\dagger y_N\le I,                  \tag{3.4}

\]

or the explicit construction of (v_N) in (0.5) from (3.1)--(3.3).

The output defect itself has the exact capacity formula

\[
 \boxed{
 D_{\rm out}=I-Y_0R_0^\dagger Y_0^*.}                \tag{3.5}
\]

Thus it is the short of the old reference energy against a prescribed
load-channel output: for (g) in the load feature target,

\[
 \langle g,D_{\rm out}g\rangle
 =\|g\|^2-\|R_0^{\dagger/2}Y_0^*g\|^2.               \tag{3.6}
\]

This is the precise channel which D.164--D.167 must control.  It is not
equal to the pure-Gamma Gram: the second term in (3.6) contains the entire
old load and can have spectrum arbitrarily close to one.  The Julia
identity yields only

\[
 \|D_{\rm in}^{\dagger/2}A_N^*y_N\|
 =\|A_N^*D_{\rm out}^{\dagger/2}y_N\|
 \le\|D_{\rm out}^{\dagger/2}y_N\|.                 \tag{3.7}
\]

Therefore neither (3.5) nor Julia unitarity proves that
(y_N\in\operatorname {Ran}D_{\rm out}^{1/2}).  The missing substantive
claim remains

\[
 y_N\in\operatorname {Ran}D_{\rm out}^{1/2},\qquad
 \|D_{\rm out}^{\dagger/2}y_N\|\le1,                 \tag{3.8}
\]

with the scalar one replaced by the available normalized boundary
capacity if the boundary reference has not yet been scaled to identity.
Equations (3.5)--(3.8) are the exact identification, not an appeal to an
abstract unnamed defect.

## 4. Consequence for the two active routes

1. **Directed finite Feshbach.**  It is enough to factor the corrected
   boundary-load columns (3.1) through the directed output defect.  The
   matrix inequality to certify is (2.4); ambient moment powers are not
   used.

2. **Global integer-cell induction.**  D.166--D.167 bound the reference
   capacity and the Gamma-normalized size of (3.3).  D.170 shows that the
   remaining estimate must be made in the output defect metric, where a
   Julia channel is canonical.  A raw (L^2) or pure-Gamma estimate is
   insufficient, but no additional geometric identification is missing.

The ancillary `114_d_170_output_defect_verify.py` checks the reference
Cholesky transform, (0.2)--(0.4), the push-through identity and the Julia
intertwining (2.5) on noncommuting finite matrices.
