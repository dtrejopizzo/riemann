# D.199 — Stable directed primitive certificate at `T=log(6)/2`

## Verdict

The complete row-D operator is strictly positive on the `198`-dimensional
two-Tate-primitive Legendre space `V_200` at

\[
 T={1\over2}\log6.                                      \tag{0.1}
\]

This is a directed Arb theorem, not the sign of a floating Galerkin matrix.
The construction uses the exact two Tate jets, the complete Gamma block,
the scalar finite-part constant and every active prime-power contact
`n=2,3,4,5`.  The apparent negative midpoint values of D.198 disappear once
the frame is whitened before the Schur reduction.

The result is a finite-block theorem.  Coupling `V_200` to its
infinite-dimensional orthogonal complement remains a separate Feshbach
obligation.

No paper file is modified.

## 1. Exact pullback and primitive frame

For `f` on the multiplicative line use the central logarithmic pullback

\[
 F(t)=e^{t/2}f(e^t).                                    \tag{1.1}
\]

Then the two A--B--C polar characters become

\[
 \widehat f(0)=\int F(t)e^{-t/2}dt=:M_-F,
 \qquad
 \widehat f(1)=\int F(t)e^{t/2}dt=:M_+F.               \tag{1.2}
\]

Thus the primitive test space is exactly `ker M_- intersect ker M_+`.
For each numerical tail column the script solves its first two Legendre
coefficients in Arb from (1.2).  Matrix multiplication by the two jet rows
then contains the exact zero matrix.  At 1100 decimal digits the largest
radius in the resulting primitive frame is below `7e-1101`.

The numerical eigensystem is used only to choose coordinates.  It proves no
sign.  All quadratic entries are recomputed after imposing (1.2).

## 2. Complete operator and active powers

On zero-extended functions on `(-T,T)`, the form representing
`-B_nuc` is

\[
 A_T=G_{\Gamma,T}-m_0I-
 \sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       (S_{\log n}+S_{-\log n}),                       \tag{2.1}
\]

where

\[
 m_0=\log\pi-\psi(1/4).                                \tag{2.2}
\]

At (0.1), `e^(2T)=6`; hence (2.1) contains exactly

\[
 n=2,3,4,5,                                             \tag{2.3}
\]

with `Lambda(4)=log 2`.  Thus the `p^2` contact is present and no
prime-only truncation is made.  The threshold `n=6` has `Lambda(6)=0` and
does not change the operator.

The Gamma matrix is assembled from the exact Hurwitz--Lerch formula at 1100
decimal digits.  This precision is essential: at 500 digits its endpoint
formula still suffers a cancellation of about five hundred digits.  At
1100 digits the largest projected Gamma-base radius is below `6.2e-95`.

The two rows of every contact needed by the delicate block are integrated
natively with the certified Arb Gauss rule
`arb.legendre_p_root(204,k,weight=True)`.  Since the integrands have degree
at most `398`, the 204-node rule is exact.  Its weight sum has error ball
of radius below `5.2e-1099`.

## 3. Safe Loewner budget

Let the approximate primitive eigencoordinates split as

\[
 V_{200}=D_2\oplus S_{196}.                             \tag{3.1}
\]

The safe midpoint eigenvalues begin with

\[
 1.8018\,10^{-11},\quad3.0778\,10^{-9},\quad
 5.5820\,10^{-7}.                                      \tag{3.2}
\]

The serialized full contact enclosure is not multiplied as one large
interval matrix.  If `C=C_0+E`, `|E|<=R` entrywise, then

\[
 |S^*ES|\le |S|^TR|S|                                  \tag{3.3}
\]

entrywise.  Its maximum row sum gives the operator bound

\[
 \delta=5.6260660600332873\,10^{-14}.                  \tag{3.4}
\]

Consequently

\[
 B_{SS}\ge
 L_{SS}:=B_{\Gamma,SS}+S^*C_0S-\delta I.               \tag{3.5}
\]

After one midpoint Cholesky whitening, the directed Gershgorin lower margin
of `L_SS` is

\[
 0.9999999999999995901\ldots>0.                         \tag{3.6}
\]

so the entire safe block is positive.

## 4. Directed `2 by 2` Feshbach block

Because inversion reverses Loewner order on positive operators,

\[
 B_{SS}^{-1}\le L_{SS}^{-1}.                            \tag{4.1}
\]

The native delicate rows therefore give the rigorous lower Schur block

\[
 K_2=B_{DD}-B_{DS}L_{SS}^{-1}B_{SD}
 =\begin{pmatrix}
 8.1526804798787876\,10^{-17}&6.8500639240917485\,10^{-17}\\
 6.8500639240917485\,10^{-17}&2.4790225091734754\,10^{-14}
 \end{pmatrix},                                        \tag{4.2}
\]

with entry radii at most `4.9e-112`.  Its directed leading minor and
determinant satisfy

\[
 K_{2,11}>8.1526804798787\,10^{-17},\qquad
 \det K_2>2.0163755043954\,10^{-30}.                   \tag{4.3}
\]

Sylvester's criterion proves `K_2>0`.  Combining (3.6), (4.1) and (4.3)
proves

\[
 \boxed{A_T|_{V_{200}\cap\ker(M_-,M_+)}>0.}            \tag{4.4}
\]

## 5. Reproducibility and exact remaining step

Run

```text
PYTHONPATH=/tmp/d61-flint D199_DPS=1100 \
python3 114_d_199_t6_whitened_native_schur.py
```

The final line is

```text
PASS T6 V200: exact jets, native delicate contacts, stable Schur
```

and the compact directed summary is written to
`/tmp/t6_whitened_native_schur.npz`.

The next theorem must bound the coupling

\[
 Q_{200}A_TP_{200}                                      \tag{5.1}
\]

in the positive `Q_200 A_T Q_200` metric and prove that its capacity is
smaller than the two tiny margins in (4.2).  A raw operator-norm estimate is
unlikely to retain a `10^-17` budget; the coupling must be contracted in the
Gamma/reference Green metric or its first two near-null columns must be
enlarged into the directed low block.  Equation (4.4) itself is complete and
does not assume that continuum estimate.
