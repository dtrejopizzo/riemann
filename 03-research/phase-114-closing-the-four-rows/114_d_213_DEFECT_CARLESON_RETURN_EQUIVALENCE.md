# D.213 — Defect layers and exact return decay

## Verdict

The defect-layer estimate isolated in D.212 has an equivalent return-orbit
form which is directly compatible with D.176--D.189.  Let \(0\leq K\leq I\),
put \(D=I-K\), and let \(b:E\to H\).  Define

\[
 m_k=b^*K^kb\geq0,
 \qquad k\geq0.                                      \tag{0.1}
\]

Then, as an increasing identity of quadratic forms,

\[
 \boxed{
 b^*D^\dagger b=\sum_{k\geq0}m_k,
 }                                                     \tag{0.2}
\]

provided \(bE\perp\ker D\); otherwise both sides are infinite in the
corresponding direction.  Moreover a small-defect Carleson bound

\[
 \|E_D((0,\delta])be\|^2
 \leq A,{\delta\over(1+|\log\delta|)^\alpha}\|e\|^2
 \quad(0<\delta\leq1)                                \tag{0.3}
\]

with \(\alpha>1\) implies

\[
 \boxed{
 m_k\leq {C_\alpha A\over
 (k+1)(1+\log(k+1))^\alpha}I
 \quad(k\geq1),
 }                                                     \tag{0.4}
\]

and hence

\[
 \sum_{k\geq1}m_k\leq C_\alpha'A I.                \tag{0.5}
\]

Conversely, a bound of the form (0.4) implies (0.3), up to a constant
depending only on \(\alpha\).  Thus the layer and return formulations are
quantitatively equivalent at the logarithmic scale needed for row D.

Equations (0.2)--(0.5) are **PROVED OPERATOR THEOREMS**.  In the A--B--C
application, a bound of type (0.4) for the exact centered born column is a
source-defined sufficient asymptotic theorem.  The sharp necessary and
sufficient statement remains the total capacity (4.2).

## 1. Neumann identity with the range condition

The spectral theorem gives

\[
 \sum_{k=0}^{r}K^k={I-K^{r+1}\over I-K}.             \tag{1.1}
\]

For every \(e\in E\), monotone convergence against the spectral measure
of \(K\) yields

\[
 \sum_{k\geq0}\langle be,K^kbe\rangle
 =\int_{[0,1)}{1\over1-\lambda}\,
   d\|E_K(\lambda)be\|^2.                           \tag{1.2}
\]

This is \(\langle be,D^\dagger be\rangle\).  An atom at \(\lambda=1\)
is exactly the component in \(\ker D\) and makes the series divergent.
This proves (0.2) without assuming norm convergence of the Neumann series.

## 2. From defect layers to returns

Fix a unit vector \(e\) and write

\[
 F(d)=\|E_D((0,d])be\|^2.
\]

For \(k\geq1\), integration by parts gives

\[
 \langle e,m_ke\rangle
 =k\int_0^1(1-d)^{k-1}F(d)\,dd.                    \tag{2.1}
\]

Insert (0.3), split the integral at \(d=(k+1)^{-1/2}\), and use
\((1-d)^{k-1}\leq e^{-(k-1)d}\).  On the first part set \(u=kd\); on the
second use the exponential factor.  This gives

\[
\begin{aligned}
 \langle e,m_ke\rangle
 &\leq {C_\alpha A\over k(1+\log k)^\alpha}
   \int_0^\infty ue^{-u}\,du
   +O_\alpha(Ae^{-\sqrt k/2})\\
 &\leq {C_\alpha'A\over k(1+\log k)^\alpha}.
\end{aligned}                                       \tag{2.2}
\]

After changing the constant for bounded \(k\), this is (0.4).  Summing
over \(k\) proves (0.5) exactly when \(\alpha>1\).

## 3. From returns to defect layers

Let \(0<\delta\leq1/2\) and choose

\[
 k=\lfloor\delta^{-1}\rfloor.
\]

On the spectral set \(0<d\leq\delta\),

\[
 (1-d)^k\geq(1-\delta)^{1/\delta}\geq{1\over4}.     \tag{3.1}
\]

Therefore

\[
 F(\delta)leq4\langle e,m_ke\rangle.               \tag{3.2}
\]

Substitution of (0.4), together with
\(k\asymp\delta^{-1}\) and
\(\log(k+1)\asymp1+|\log\delta|\), proves (0.3) with a changed universal
constant.  The range \(1/2<\delta\leq1\) is absorbed by enlarging it once
more.

## 4. The exact A--B--C porting theorem

In the D.170 output coordinate set

\[
 K_N=A_NA_N^*,
 \qquad D_N=I-K_N,
 \qquad m_{N,k}=y_N^*K_N^ky_N.                      \tag{4.1}
\]

The old-cell induction gives \(0\leq K_N\leq I\).  The sharp new-cell
capacity is

\[
 y_N^*D_N^\dagger y_N
 =m_{N,0}+\sum_{k\geq1}m_{N,k}.                    \tag{4.2}
\]

The term \(m_{N,0}=y_N^*y_N\) is the direct born load.  D.164--D.167 give
the coefficient-one-half estimate for its pure-reference arithmetic
part.  The genuinely missing transfer is the return tail.

Consequently a convenient sufficient uniform theorem is:

\[
 \boxed{
 m_{N,k}
 \leq {\varepsilon_N\log N\over
 (k+1)(1+\log(k+1))^2}I,
 \qquad k\geq1,
 \qquad\varepsilon_N\to0,
 }                                                     \tag{4.3}
\]

where \(m_{N,k}\) is the return of the **complete** Tate-centered born
column: it includes the atomic--continuous discrepancy \(E_N\), the
endpoint Volterra pieces, their cross terms, and all intervening complete
Green operators.  It is not obtained by summing separately positive
``Witt'', ``continuous'', and ``endpoint'' return contributions.

D.183 and D.187 prove uniform summability for the arithmetic Witt-word
majorant.  D.188 gives a strict geometric contraction for the long-time
reference residual.  These are inputs for estimating the complete return,
not an additive decomposition of it.  D.189 proves that neither result is
yet (4.3), because the exact Green-weighted centered column is not the raw
Witt Gram.

Once (4.3) is proved, (0.5) gives

\[
 \sum_{k\geq1}m_{N,k}=o(\log N)I,                   \tag{4.4}
\]

which is the sufficient transfer proposed in D.167.  Combining (4.4) with
the leading margin from D.166--D.167 proves the sharp Douglas capacity for
all sufficiently large cells.  Row D could in principle hold with a
nonzero \(O(\log N)\) transfer still below the remaining margin; therefore
(4.3) is not asserted to be logically necessary.

## 5. Falsification requirement

The estimate (4.3) must be derived from the source formula for \(E_N\),
the complete Green returns and the Gamma/contact dynamics.  It may not be
deduced from \(D_N\geq0\), because that is the induction hypothesis only
on the old cell, nor from a Hilbertization whose contractivity is
equivalent to the location of the zeta zeros.

Any proposed proof of (4.3) must also be applied to the established
Beurling surrogate.  If it survives unchanged in an off-line-zero model,
then it has discarded the sign-sensitive centered channel and cannot be
the porting theorem.

## 6. Classification

* Neumann/Stieltjes identity (0.2): **PROVED OPERATOR IDENTITY**.
* Carleson-to-return implication: **PROVED**.
* Return-to-Carleson implication: **PROVED up to universal constants**.
* Uniform summability of raw arithmetic Witt words: **PROVED** in
  D.183/D.187.
* Strict contraction of the long reference residual: **PROVED** in D.188.
* Strong centered-return estimate (4.3): **OPEN SUFFICIENT THEOREM**.
* Large-cell sharp Douglas capacity: **OPEN**; it follows from (4.3), but
  may admit a weaker sharp proof directly from (4.2).
