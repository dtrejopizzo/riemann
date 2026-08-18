# D.257 — Tensor duality selects one coherent prime port

## Verdict

For a finite prime set, the first variation of the tensor Euler state pairs
with a **single** dual central tensor state.  All spectator factors cancel
by the exact relation \(\theta_p^*\eta_p=I\), leaving the sum of the local
prime scores and no cross-prime remainder.

Thus the dual-central channel is intrinsically rank one in prime-index
space.  After the torsion normalization of D.244 it is the coherent degree
port isolated in D.256.  The orthogonal contact directions cannot couple
to this central state and remain positive defect outputs.

This completes the finite tensor-port identification before semilocal
quotient, Gamma, position support and Tate shorting.

## 1. Local dual pairs

For every \(p\in S\), let

\[
 \theta_p=h_p=I-p^{-1/2}U_p,
 \qquad
 \eta_p=(h_p^*)^{-1}.                               \tag{1.1}
\]

Then

\[
 \boxed{\theta_p^*\eta_p=I.}                       \tag{1.2}
\]

Let \(d_{p,+}\) be the even local tangent of D.245 and use the
adjoint-oriented cotangent insertion

\[
 \delta_{p,+}:=d_{p,+}^*.
\]

Its score identity is

\[
 \delta_{p,+}^*\eta_p+\eta_p^*\delta_{p,+}
 =L_p(P_{r_p}-I),
 \qquad L_p=\log p,\quad r_p=p^{-1/2}.             \tag{1.3}
\]

Indeed \(\delta_{p,+}^*\eta_p=d_{p,+}(h_p^*)^{-1}\)
is one half of the self-adjoint score in D.245(2.2).  The adjoint
orientation is essential: using \(d_{p,+}\) itself in this Hilbert cross
would give the wrong pair of denominators.

## 2. Adjoint-oriented tensor tangent

Put

\[
 \theta_S=\bigotimes_{p\in S}\theta_p,
 \qquad
 \eta_S=\bigotimes_{p\in S}\eta_p.                \tag{2.1}
\]

For real coefficients \(a=(a_p)\), define the directional even tangent

\[
 \dot\theta_{S,+}(a)
 =\sum_{p\in S}a_p\,
   \delta_{p,+}\otimes
   \bigotimes_{q\ne p}\theta_q.                   \tag{2.2}
\]

Using (1.2) in every spectator factor gives

\[
 \dot\theta_{S,+}(a)^*\eta_S
 =\sum_{p\in S}a_p\,
   \delta_{p,+}^*\eta_p\otimes I_{S\setminus\{p\}}. \tag{2.3}
\]

Adding the adjoint and using (1.3) proves

\[
 \boxed{
 \dot\theta_{S,+}(a)^*\eta_S
 +\eta_S^*\dot\theta_{S,+}(a)
 =\sum_{p\in S}a_pL_p(P_{r_p}-I).
 }                                                   \tag{2.4}
\]

There are no cross-prime terms.  Their absence is not orthogonality of the
tangents; it is exact cancellation of every spectator against the dual
central tensor.

## 3. Rank-one coherence in prime-index space

The central object \(\eta_S\) in (2.4) is one tensor state.  Consequently
the map from the prime-index tangent coefficients to the central channel
is a single linear functional.  The local contact directions orthogonal to
that functional do not enter (2.4).

D.244 proves that the unique diagonal coordinate change compatible with
the torsion contact sends this functional to

\[
 z\longmapsto
 \sum_{p\in S}\sqrt{\log p}\,z_p.                 \tag{3.1}
\]

Equation (3.1) is exactly the degree/coherent port of D.247 and D.256.
Thus the following three rank-one objects agree after the established
normalizations:

\[
 \boxed{
 \text{tensor dual-central pairing}
 =\text{coherent contact component}
 =\text{arithmetic degree port}.
 }                                                   \tag{3.2}
\]

This is an identification of source functionals.  It does not identify
the whole tensor Hilbert space with the D.190 support space.

## 4. Finite prime port diagram

Before Gamma and support compression the prime construction now has the
typed diagram

\[
 \begin{array}{ccc}
 (\text{odd tangent},\text{degree})
 &\xrightarrow{\text{D.247 conservative}}&
 (\text{even tangent},\text{contact})\\[1mm]
 &&\downarrow\ \text{D.256 split}\\[-1mm]
 &&(\text{even tangent},\text{coherent contact},
                 \text{primitive contact})\\[1mm]
 &&\downarrow\ \text{D.254 dual-central rotation}\\[-1mm]
 &&(W_+^{\rm cr},W_-^{\rm cr},
                 \text{primitive contact}).
 \end{array}                                       \tag{4.1}
\]

The coherent contact is the only component paired with \(\eta_S\).  The
primitive contact is retained as the exact defect from D.256(4.2).

## 5. Remaining comparison

At the scalar-form level, D.240 already proves that semilocal assembly,
the full Gamma factor and Tate compression give exactly
\(Q_T=-B_{{\rm nuc},T}^{\rm prim}\).  What has not been transported is the
**conservative port factorization** above.  In particular it does not
commute automatically with:

1. the semilocal quotient;
2. the archimedean tensor state;
3. position support compression;
4. the two Tate equations;
5. old-core reference shorting.

The next theorem must construct the image of diagram (4.1) at the
feature/defect level under these operations and compare its final defect with
\(I-y_N^*D_{{\rm out},N}^\dagger y_N\).  Equality before those operations
is now proved and cannot be the remaining gap.

## 6. Classification

* Spectator cancellation (2.3): **PROVED TENSOR IDENTITY**.
* Complete weighted score (2.4): **PROVED**, including every prime tower
  through the Poisson expansion.
* Single coherent central functional: **PROVED**.
* Identification with the torsion-normalized degree covector (3.1):
  **PROVED USING D.244**.
* Finite prime port diagram (4.1): **CONSTRUCTED AT THE SOURCE/TENSOR
  LEVEL**.
* Semilocal/Gamma/Tate scalar-form comparison: **PROVED IN D.240**.
* Conservative-port transport through support/Tate/old short: **OPEN**.
* Row D: **OPEN**.
