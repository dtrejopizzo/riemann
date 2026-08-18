# D.212 — Restricted resolvent transfer is a defect-layer theorem

## Verdict

The pure-Gamma estimate of D.167 cannot be transferred to the complete old
core from a norm bound, compactness, or positivity alone.  The exact extra
cost is a Stieltjes integral over the small spectral layers of the old
defect.  This identifies the minimal uniform theorem still missing after
D.210--D.211.

Let

\[
 \Gamma>0,
 \qquad
 A=\Gamma^{1/2}D\Gamma^{1/2},
 \qquad
 D=I-K>0,quad 0\leq K<I,                            \tag{0.1}
\]

where \(\Gamma\) is the pure reference and \(A\) is the already assembled
old primitive core.  For a boundary synthesis \(\mathcal B:E\to H\), put

\[
 b=\Gamma^{-1/2}\mathcal B.                          \tag{0.2}
\]

Then

\[
 \boxed{
 \mathcal B^*A^{-1}\mathcal B
 -\mathcal B^*\Gamma^{-1}\mathcal B
 =b^*K(I-K)^{-1}b.
 }                                                     \tag{0.3}
\]

For \(e\in E\), let

\[
 \mu_e(S)=\|E_D(S)be\|^2.                            \tag{0.4}
\]

The same identity is

\[
 \boxed{
 \langle e,\Delta e\rangle
 =\int_{(0,1]}{1-d\over d}\,d\mu_e(d),
 \qquad
 \Delta:=b^*K(I-K)^{-1}b.
 }                                                     \tag{0.5}
\]

Thus D.167's desired transfer \(\Delta=o(\log N)I\) is precisely a
uniform integrability statement for the normalized boundary vector at
\(d=0\).  The already proved estimate

\[
 b^*b\leq(\tfrac12+o(1))\log N\,I                   \tag{0.6}
\]

controls only the total mass of \(\mu_e\), not its distribution near
zero.  It cannot imply (0.5) with the required scale.

Equations (0.3)--(0.5) are **PROVED OPERATOR IDENTITIES**.  The required
defect-layer estimate is **OPEN**.

## 1. Exact resolvent identity

From (0.1), on the supported range,

\[
 A^{-1}=\Gamma^{-1/2}D^{-1}\Gamma^{-1/2}.
\]

Therefore

\[
\begin{aligned}
 \mathcal B^*A^{-1}\mathcal B
 -\mathcal B^*\Gamma^{-1}\mathcal B
 &=b^*(D^{-1}-I)b\\
 &=b^*K(I-K)^{-1}b,
\end{aligned}
\]

because \(D=I-K\) and \(K\) commutes with every Borel function of \(D\).
This proves (0.3).  Applying the spectral theorem to \(D\) proves (0.5).

If kernels occur, replace the inverses by Moore--Penrose inverses.  The
identity remains valid exactly when

\[
 be\perp\ker D.                                      \tag{1.1}
\]

Failure of (1.1) makes the transfer infinite.  This is the range part of
the sharp Douglas condition, not a technicality.

## 2. Dyadic defect layers

Let

\[
 I_j=(2^{-(j+1)},2^{-j}],\qquad j\geq0,
\]

and set

\[
 \nu_e(\delta)=\mu_e((0,\delta]).                   \tag{2.1}
\]

On \(I_j\),

\[
 2^j-1\leq{1-d\over d}\leq2^{j+1}.                 \tag{2.2}
\]

Consequently

\[
 \sum_{j\geq0}(2^j-1)\mu_e(I_j)
 \leq\langle e,\Delta e\rangle
 \leq\sum_{j\geq0}2^{j+1}\mu_e(I_j).              \tag{2.3}
\]

A sufficient source-defined estimate is therefore

\[
 \boxed{
 \nu_e(\delta)
 \leq \varepsilon_N\log N\,
 {\delta\over(1+|\log\delta|)^{2}}
 \|e\|^2,
 \quad0<\delta\leq1,
 \quad\varepsilon_N\to0.
 }                                                     \tag{2.4}
\]

Indeed summation by parts in (2.3) gives

\[
 \Delta=O(\varepsilon_N\log N)I=o(\log N)I.         \tag{2.5}
\]

The exponent two is not cosmetic: the dyadic series after multiplication
by \(d^{-1}\) is comparable to \(\sum_j(1+j)^{-2}\).  This is the same
defect-layer exponent found independently in D.174.

Conversely, (0.5) immediately implies the necessary weak estimate

\[
 \nu_e(\delta)
 \leq {\delta\over1-\delta}
       \langle e,\Delta e\rangle
 \qquad(0<\delta<1).                                 \tag{2.6}
\]

Thus the transfer theorem and the small-defect distribution are two
coordinate descriptions of the same analytic obstruction.

## 3. Norm information is insufficient

The insufficiency can be proved in dimension one.  Take

\[
 \Gamma_N=1,
 \qquad K_N=1-\epsilon_N,
 \qquad D_N=\epsilon_N,
 \qquad b_N=\sqrt{\tfrac12\log N},                  \tag{3.1}
\]

with \(0<\epsilon_N<1\).  Then the old core is strictly positive and

\[
 b_N^*b_N=\tfrac12\log N,                            \tag{3.2}
\]

exactly matching the pure-reference scale.  But

\[
 \Delta_N
 ={1-\epsilon_N\over\epsilon_N}\,
   {\log N\over2}.                                   \tag{3.3}
\]

Choosing \(\epsilon_N\downarrow0\) makes (3.3) arbitrarily larger than
\(\log N\).  Hence the following inputs, even together, do not prove the
transfer:

* positivity of the old core;
* compactness or finite dimensionality;
* the pure-Gamma norm (0.6);
* a lower bound for the unrelated high-frequency reference tail.

The example does not refute a source-specific theorem for A--B--C.  It
proves that such a theorem must use the alignment of the centered boundary
vector with the old defect layers.

## 4. Interaction with D.211

D.211 cuts the full primitive source with the spectral projections of the
positive reference \(R_T\).  Above \(\Lambda>M_T\), the complete signed
operator has the explicit gap \(\Lambda-M_T\).  Therefore the contribution
of every dangerous spectral layer to (0.5) is encoded by the finite
reference-low Schur complement and its high harmonic lift.  The associated
eigenvectors need not literally lie in the reference-low block.

This is a genuine reduction, but not a uniform estimate: the dimension of
that block may grow with \(N\), and a finite matrix can still have an
arbitrarily small eigenvalue.  Combining D.211 with (0.5) shows exactly
what a directed or analytic proof must enclose:

\[
 \boxed{
 \int_{(0,1]}d^{-1}\,d
 \bigl(b_N^*E_{D_N}(d)b_N\bigr),
 }                                                     \tag{4.1}
\]

after the reference-high block has been shorted by the operator-valued
Green identity of D.210.

## 5. Translation to the D.170 output defect

D.170 uses the output defect

\[
 D_{{\rm out},N}=I-A_NA_N^*
\]

and the normalized born column \(y_N\).  Its exact capacity is

\[
 y_N^*D_{{\rm out},N}^{\dagger}y_N.                  \tag{5.1}
\]

Define the output spectral measure

\[
 \sigma_{N,e}(S)
 =\|E_{D_{{\rm out},N}}(S)y_Ne\|^2.                 \tag{5.2}
\]

Then

\[
 \langle e,y_N^*D_{{\rm out},N}^{\dagger}y_Ne\rangle
 =\int_{(0,1]}d^{-1}\,d\sigma_{N,e}(d),             \tag{5.3}
\]

with the independent range condition
\(y_Ne\perp\ker D_{{\rm out},N}\).  The row-D birth theorem is exactly
the assertion that (5.3) is bounded by the born budget.  A source-defined
bound of the form (2.4), with the correct normalization of that budget,
would prove it.

This is the authoritative target.  The two Tate moments remove the polar
channels in the definition of \(y_N\); they do not imply (2.4).

## 6. Consequences for the active route

The following attempted implications are now ruled out:

\[
 \text{pure-Gamma norm}\Longrightarrow\text{complete-core inverse},
\]

\[
 \text{finite dangerous block}\Longrightarrow\text{uniform capacity},
\]

\[
 \text{high-reference gap}\Longrightarrow
 \text{small old-defect spectral mass}.
\]

The next lemma must instead act on the exact centered discrepancy
\(E_N\) inside the output-defect spectral projections.  The noncircular
target is (2.4)/(5.3), preferably derived from the source semigroup and
the integer-cell separation, and tested against the Beurling surrogate.

## 7. Classification

* Resolvent transfer identity (0.3): **PROVED OPERATOR IDENTITY**.
* Spectral integral (0.5): **PROVED OPERATOR IDENTITY**.
* Dyadic bounds (2.3), sufficient estimate (2.4): **PROVED**.
* Scalar counterexample: **PROVED**.
* Encoding of the dangerous layers by the finite reference-low Schur
  complement and its harmonic lift: **PROVED**, using D.211.
* A--B--C defect-layer estimate (2.4)/(5.3): **OPEN**.
* Uniform large-birth capacity and row D: **OPEN**.
