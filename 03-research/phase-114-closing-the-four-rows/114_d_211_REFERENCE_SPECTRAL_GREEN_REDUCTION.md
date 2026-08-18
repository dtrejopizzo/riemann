# D.211 — Source spectral cutoff and exact finite Green reduction

## Verdict

The positive reference in the centred screw factorization gives a
source-defined finite/infinite split for which the infinite block is
coercive without assuming row D.  This removes one genuine analytic
ambiguity from the multilevel Green route.

On the two-Tate primitive Hilbert space let

\[
 R_T=X_T^*X_T>0,
 \qquad L_T=Y_T^*Y_T\geq0,
 \qquad Q_T=R_T-L_T=-B_{\rm nuc,T}^{\rm prim}.       \tag{0.1}
\]

D.134 proves that \(R_T\) has compact resolvent and that

\[
 0\leq L_T\leq M_T I,
 \qquad
 M_T=\beta+4+2\sum_{p^k\leq e^{2T}}
              {\log p\over p^{k/2}}.                 \tag{0.2}
\]

For \(\Lambda>M_T\), let

\[
 P_\Lambda={\bf1}_{[0,\Lambda)}(R_T),
 \qquad Z_\Lambda=I-P_\Lambda.                       \tag{0.3}
\]

Then \(P_\Lambda\) has finite rank and

\[
 \boxed{
 Z_\Lambda Q_TZ_\Lambda
 \geq(\Lambda-M_T)Z_\Lambda.
 }                                                     \tag{0.4}
\]

Consequently row D on the fixed window \(T\) is equivalent to positivity
of one finite-dimensional Schur complement with the *exact* operator Green
of the high block.  Moreover every further Schur complement taken wholly
inside the high block retains the same gap \(\Lambda-M_T\).  Combining
this fact with D.210 gives a directed finite upper enclosure of the exact
Green correction.

These statements are **PROVED OPERATOR THEOREMS**.  They do not prove the
finite Schur complement positive, and therefore do not prove row D.  Their
content is that the remaining obstruction is finite-dimensional at each
fixed window in a canonical, source-defined filtration; no unproved
coercivity of \(Q_T\) at high modes remains.

## 1. Reference spectral tail

Because \(R_T\) is self-adjoint with compact resolvent, its spectral
projection \(P_\Lambda\) has finite rank.  For every
\(z\in Z_\Lambda\operatorname {Dom}(R_T^{1/2})\), the spectral theorem and
(0.2) give

\[
 \langle z,R_Tz\rangle\geq\Lambda\|z\|^2,
 \qquad
 \langle z,L_Tz\rangle\leq M_T\|z\|^2.
\]

Subtraction proves (0.4).  Notice what has not been used: no sign of
\(Q_T\) on the whole primitive space, no zero of \(\xi\), and no
numerical approximation.  The cutoff is defined by the Gamma/contact
reference itself.

The half-open convention in (0.3) is immaterial.  If \(\Lambda\) is an
eigenvalue, one may include its eigenspace in \(P_\Lambda\), after which
the right side of (0.4) remains valid with \(\Lambda\) replaced by the
first excluded eigenvalue.  Below we use only a strict positive number

\[
 \delta_{T,\Lambda}:=\Lambda-M_T>0.                  \tag{1.1}
\]

## 2. Exact fixed-window equivalence

Put \(P=P_\Lambda\), \(Z=Z_\Lambda\), and write the form operator in
blocks

\[
 Q_T=
 \begin{pmatrix}
  Q_{PP}&Q_{PZ}\\
  Q_{ZP}&Q_{ZZ}
 \end{pmatrix}.                                      \tag{2.1}
\]

Equation (0.4) makes \(Q_{ZZ}\) boundedly invertible as a map between its
form domain and anti-dual.  The closed-form Schur theorem therefore gives

\[
 \boxed{
 Q_T\geq0
 \quad\Longleftrightarrow\quad
 S_{T,\Lambda}:=
 Q_{PP}-Q_{PZ}Q_{ZZ}^{-1}Q_{ZP}\geq0.
 }                                                     \tag{2.2}
\]

The operator \(S_{T,\Lambda}\) acts on the finite-dimensional space
\(P_\Lambda\mathcal P_T\).  Formula (2.2) is an exact equivalence, not a
Galerkin implication.  The second term is the operator-valued Green
correction demanded by D.209.

If equality is considered, the same block factorization gives

\[
 \ker Q_T=
 \left\{
 p-Q_{ZZ}^{-1}Q_{ZP}p:
 p\in\ker S_{T,\Lambda}
 \right\}.                                           \tag{2.3}
\]

Thus the equality space is finite-dimensional and is determined exactly
by the finite Schur kernel.  No independent infinite-tail equality mode
can occur because \(Q_{ZZ}\geq\delta_{T,\Lambda}I\).

## 3. Gap preservation under internal elimination

The following elementary lemma is essential for using D.210.

**Lemma 3.1 (shorting preserves a lower bound).**  Let \(A=A^*\geq
\delta I>0\) on \(W\oplus Z\), and assume \(A_{WW}\) is invertible.  Its
Schur complement

\[
 S_W=A_{ZZ}-A_{ZW}A_{WW}^{-1}A_{WZ}
\]

satisfies \(S_W\geq\delta I_Z\).

**Proof.**  The block inverse formula identifies

\[
 S_W^{-1}=P_ZA^{-1}|_Z.
\]

Since \(A\geq\delta I\), inverse order gives
\(A^{-1}\leq\delta^{-1}I\).  Compression preserves order, hence
\(S_W^{-1}\leq\delta^{-1}I_Z\), and inverse order once more gives the
claim. \(\square\)

Apply the lemma to \(A=Q_{ZZ}\), which satisfies (0.4).  Any finite
reference-spectral band \(W\subset Z_\Lambda\) can therefore be eliminated
exactly, while the unrepresented final tail keeps the same certified gap
\(\delta_{T,\Lambda}\).  This fact is stronger than a lower bound on a raw
compression: it controls the post-Galerkin Schur complement required in
D.210.

## 4. Directed Green enclosure

Let \(E=P_\Lambda\mathcal P_T\), let \(A=Q_{ZZ}\), and let
\(C=Q_{ZP}:E\to Z_\Lambda\).  Choose an increasing sequence of finite
reference-spectral bands \(W_j\subset Z_\Lambda\) whose union is a form
core for \(A\).  With the notation of D.210,

\[
 G_j=C_{W_j}^*A_{W_jW_j}^{-1}C_{W_j},
\]

\[
 R_j=C_{Z_j}-A_{Z_jW_j}A_{W_jW_j}^{-1}C_{W_j}.
\]

The exact and directed statements are

\[
 G_j\uparrow C^*A^{-1}C,                              \tag{4.1}
\]

\[
 \boxed{
 G_j\leq C^*A^{-1}C
 \leq G_j+\delta_{T,\Lambda}^{-1}R_j^*R_j.
 }                                                     \tag{4.2}
\]

The lower inequality and monotonicity are D.210.  For the upper inequality,
Lemma 3.1 supplies the required lower bound for the final Schur complement.
Thus the enclosure width is

\[
 0\leq C^*A^{-1}C-G_j
 \leq\delta_{T,\Lambda}^{-1}R_j^*R_j.                \tag{4.3}
\]

It follows that the sufficient finite certificate

\[
 Q_{PP}-G_j-\delta_{T,\Lambda}^{-1}R_j^*R_j\geq0       \tag{4.4}
\]

proves row D on the fixed window.  Conversely, if a directed lower
enclosure proves a negative vector for
\(Q_{PP}-C^*A^{-1}C\), then row D fails on that window.  This makes the
certificate two-sided and falsifiable.

## 5. Relation to the sharp Douglas birth problem

At a prime-power birth there are now two exact reductions of the same
full-cell inequality:

1. D.170 first eliminates the transported old core and obtains the
   output-defect capacity

\[
 y_N^*D_{\rm out}^{\dagger}y_N\leq I.                \tag{5.1}
\]

2. D.211 applies the reference-spectral cutoff to the full primitive cell
   and obtains the finite Schur inequality (2.2).

Under the old-cell positivity hypothesis, D.170 proves that (5.1) is
equivalent to positivity of the full enlarged cell.  D.211 proves that
(2.2) is equivalent to the same positivity statement.  Therefore the two
final inequalities are equivalent.  This is a transitive equivalence of
two Schur reductions; it does **not** assert that their displayed matrices
are literally equal or that the reference spectral projection commutes
with the old/born Cholesky transform.

The D.211 construction is source-defined: it uses only \(X_T\), \(Y_T\),
the explicit load bound \(M_T\), and spectral calculus of
\(R_T=X_T^*X_T\).  It does not define the Douglas contraction by the
desired inequality.

What remains is not an infinite-tail coercivity theorem.  It is the
following uniform finite-Schur theorem:

\[
 \boxed{
 \text{For every sufficiently large prime-power birth, one can choose }
 \Lambda_N>M_N\text{ and a finite band }W_{N,j(N)}
 \text{ for which (4.4) holds on the full primitive cell.}
 }                                                     \tag{5.2}
\]

The finitely many births below the effective threshold must then be
certified with directed arithmetic.  Statement (5.2) remains **OPEN**.

## 6. What Suzuki supplies, and what it does not

Suzuki's localized operator theorem supplies an independent realization
of the same analytic pattern: a Friedrichs self-adjoint localization,
discrete spectrum, continuity in the window, and positivity for
sufficiently small windows.  Those results support the domain and compact
resolvent framework used above.

They do not supply a non-circular global lower bound for \(Q_T\): the sign
of its lowest eigenvalue for every window is equivalent to the target
criterion.  D.211 therefore uses Suzuki only for compatible operator
infrastructure, never as an input for (0.4).  The latter comes from the
already proved positivity of the reference \(R_T\) and the elementary
bounded-load estimate (0.2).

## 7. Epistemic classification

* Compactness of the reference resolvent and boundedness (0.2):
  **PROVED** in D.134.
* Reference-tail coercivity (0.4): **PROVED**.
* Fixed-window Schur equivalence (2.2):
  **PROVED OPERATOR THEOREM**.
* Kernel formula (2.3): **PROVED**.
* Preservation of the high gap under shorting: **PROVED**.
* Directed Green enclosure (4.2): **PROVED**, using D.210.
* Positivity of a particular finite Schur certificate: not asserted here.
* Uniform large-birth theorem (5.2): **OPEN**.
* Global row D and RH consequence: **OPEN**.

## 8. Exact reduction achieved

For every fixed window, all uncontrolled infinite-dimensional directions
have now been moved into a source-defined block with an explicit positive
gap.  The only remaining sign question is a finite-dimensional Schur
complement, together with a directed enclosure of its Green correction.
This is a strict reduction of the missing theorem, but it is not its proof.
