# D.258 — Prime-index coherence does not make the boundary port finite rank

## Verdict

The coherent degree/dual-central port isolated in D.256--D.257 has rank one
only in the finite **prime-index** coordinate.  After the multiplicative
Fourier realization it is an \(L^2\)-valued port.  On every nontrivial
support window its restriction to the two-Tate primitive space has
infinite rank.

Therefore the two Tate equations do not close the coherent port.  They
remove two scalar polar modes from an infinite-dimensional boundary
channel.  The global feedback still has to transport that whole channel
through the old output defect of D.170.

## 1. The coherent dual-central map

For a finite prime set \(S\), put

\[
 \eta_S(\tau)=prod_{p\in S}
  (1-p^{-1/2+i\tau})^{-1}.                          \tag{1.1}
\]

Every factor is bounded and bounded away from zero on the real \(\tau\)
axis.  Hence multiplication by \(\eta_S\), denoted \(M_{\eta_S}\), is a
bounded invertible operator on \(L^2(\mathbb R_\tau)\).

Let \(J_T:L^2(I_T)\to L^2(\mathbb R_t)\) be zero extension, \(\mathcal F\)
the unitary Fourier transform, and \(\Pi_T\) the orthogonal projection onto
the two-Tate primitive space.  The realized coherent port is

\[
 \mathcal C_{S,T}
 :=M_{\eta_S}\mathcal FJ_T\Pi_T:
 L^2(I_T)\longrightarrow L^2(\mathbb R_\tau).      \tag{1.2}
\]

The phrase “one coherent port” means that (1.2) has no remaining direct
sum over \(p\).  It does not mean that its Hilbert target is
one-dimensional.

## 2. Infinite-rank theorem

For every \(T>0\),

\[
 \boxed{\mathrm{rank}\,\mathcal C_{S,T}=\infty.} \tag{2.1}
\]

Indeed \(\mathcal P_T=\mathrm{Ran}\,\Pi_T\) has codimension two in
the infinite-dimensional space \(L^2(I_T)\), hence is infinite-dimensional.
The zero-extension \(J_T\), Fourier transform \(\mathcal F\), and
multiplication operator \(M_{\eta_S}\) are all injective.  Therefore their
composition is injective on \(\mathcal P_T\), which proves (2.1).

More generally, replacing \(\eta_S\) by any nonzero multiplier which is
nonvanishing almost everywhere gives the same conclusion.

## 3. Tate shorting is only finite rank

Since \(I-\Pi_T\) has rank two,

\[
 M_{\eta_S}\mathcal FJ_T
 -\mathcal C_{S,T}
 =M_{\eta_S}\mathcal FJ_T(I-\Pi_T)                 \tag{3.1}
\]

has rank at most two.  Thus Tate shorting changes the coherent port by a
finite-rank map but leaves its infinite-dimensional range.

This is the port-level version of the rank-four correction to the
old/born quadratic block in D.190.

## 4. Consequence for the D.256 exchange

The coherent/primitive split in prime-index space is still exact and
necessary.  After tensoring with the spectral Hilbert space it has the
form

\[
 (\mathbb Ce_S\otimes L^2)
 \oplus
 (e_S^\perp\otimes L^2).                            \tag{4.1}
\]

The first summand is one prime-index channel but has infinite Hilbert
rank; the second is the local contact-defect bundle.  Exchanging the first
summand with the degree channel is therefore an operator-valued feedback,
not a scalar Schur complement.

The two Tate equations act on the \(L^2\) source and cannot replace this
feedback.  The required factor remains

\[
 y_N=D_{{\rm out},N}^{1/2}v_N,\qquad\|v_N\|\le1,   \tag{4.2}
\]

with \(v_N\) transporting an infinite-dimensional coherent boundary
range.

## 5. Correct next object

The next state-space calculation must use an operator-valued coherent
pivot on a compact smooth form core.  Its internal operator is the
support commutator of the dual Euler multiplier, with the Gamma multiplier
adjoined.  It must not replace that pivot by the scalar degree functional
of the finite coefficient model.

## 6. Classification

* Prime-index rank-one coherence: **PROVED IN D.256--D.257**.
* Bounded invertibility of the finite Euler multiplier (1.1): **PROVED**.
* Infinite Hilbert rank after support/Tate compression (2.1): **PROVED**.
* Tate correction rank at most two at the feature level: **PROVED**.
* Reduction of the global feedback to a scalar pivot: **IMPOSSIBLE**.
* Operator-valued coherent feedback and D.190 comparison: **OPEN**.
* Row D: **OPEN**.
