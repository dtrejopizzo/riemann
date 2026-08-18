# Row D sharp Douglas gate

## The theorem to be proved

Fix a prime-power threshold cell and assume positivity has already been
proved on the transported old core.  With the notation of
`ROW_D_OPERATOR_MAP.md`, define

\[
A_N=Y_0R_0^{\dagger/2},\qquad
y_N=(Y_E-Y_0R_0^\dagger X_0^*X_E)S_E^{\dagger/2},
\]

\[
D_{\rm out}=I-A_NA_N^*.
\]

The sharp gate is

\[
\boxed{
y_N=D_{\rm out}^{1/2}v_N,
\qquad \|v_N\|\le1,
}
\tag{SD}
\]

where (v_N) must be constructed from the prime--Gamma--Poisson source
before knowing the sign of the enlarged row-D block.

Equivalently,

\[
y_Ny_N^*\le D_{\rm out},
\tag{SD1}
\]

or

\[
\operatorname{Ran}y_N\subseteq\operatorname{Ran}D_{\rm out}^{1/2},
\qquad y_N^*D_{\rm out}^\dagger y_N\le I.
\tag{SD2}
\]

These equivalences are **PROVED** by Douglas' lemma and generalized Schur
shorting.  Assertion (SD) itself is **OPEN** uniformly over all cells.

## Relation with D.190 equation (0.3)

D.190 writes the same gate in raw old/shell coordinates as

\[
\boxed{
X_{OE}^{\rm prim}=A_O^{1/2}C_{OE},\qquad
C_{OE}^*C_{OE}\le B_E.
}
\tag{0.3-corrected}
\]

The source note prints (C_{OE}C_{OE}^*\le B_E), but with the stated type
(C_{OE}:H_E\to\overline{\operatorname{Ran}A_O}), the well-typed
inequality on (H_E) is (C_{OE}^*C_{OE}\le B_E).  This is a typographical
orientation correction; the Schur complement in D.190 uses the correctly
typed version.

The Cholesky change of D.170 transforms this raw statement into (SD).
Thus the two formulations have the same unit constant and the same range
obligation.

## Exact logical equivalence

For one old-plus-born block, the following are equivalent:

1. the enlarged primitive form is nonnegative;
2. its Schur complement is nonnegative, with the required range inclusion;
3. the raw factorization (0.3-corrected) holds;
4. the output-defect factorization (SD) holds.

For an exhaustive family of cells, initial positivity plus (SD) at every
birth implies (Q_T=-B_{{\rm nuc},T}^{\rm prim}\ge0) for every window.
Conversely, global positivity gives every compressed Schur inequality and
hence (SD).  This is a **PROVED EQUIVALENCE**, not a proof of (SD).

## Role of the Tate jets

The two moments define the orthogonal projection (\Pi_T) and remove the
two polar characters exactly.  They also cancel the continuous low-rank
part of the Dirichlet polynomial against its Chebyshev main term.  These
are **PROVED** facts.

They cannot supply (SD) alone:

* (I-\Pi_T) has rank two;
* the change of the old/shell block has rank at most four after
  regularization;
* the Gamma boundary operator between any two nonempty intervals has
  infinite rank.

Therefore the required (v_N) must transport an infinite-rank Poisson
boundary block.  Any construction using only the two jets is ruled out.

## Regularized version

For (\varepsilon>0), set

\[
D_{{\rm out},\varepsilon}=D_{\rm out}+\varepsilon I,
\qquad
\mathcal C_{N,\varepsilon}
=I-y_N^*D_{{\rm out},\varepsilon}^{-1}y_N.
\]

If one proves

\[
\mathcal C_{N,\varepsilon}\ge0
\quad\text{for every }\varepsilon>0
\]

uniformly enough to pass to (\varepsilon\downarrow0), then the range
condition and (SD2) follow automatically by monotone convergence.  This is
a valid noncircular target provided the positivity is derived from a
source identity rather than assumed from the enlarged block.

## Acceptance test for a proposed proof

A proposed (v_N) closes the gate only if all of the following are proved:

1. it is defined without zeros, the sign of (B_{\rm nuc}), or a positive
   spectral projection of that form;
2. it contains every (p^k), the full Gamma term and the centered Poisson
   correction;
3. (D_{\rm out}^{1/2}v_N=y_N) holds as an operator/form identity;
4. (\|v_N\|\le1) holds with the exact constant one;
5. the construction is uniform for all sufficiently large births;
6. the remaining finite births are interval-certified;
7. the equality kernel is identified and disappears modulo the known
   polar/radical channels.

