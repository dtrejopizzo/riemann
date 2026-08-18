# 106.142 — Cofinal allocation-rank obstruction after the exact anti-short

## 1. Purpose and result

The fixed and scalar-adaptive Gamma splits of 106.139--106.140 leave one
apparently wider possibility.  On each post-short heat or hybrid row, one
could spend the positive Gamma remainder only in the directions in which
the signed prime--connection block is negative.  This would be an
operator-valued, row-adaptive allocation rather than a scalar split.

There is an exact finite-dimensional obstruction.  Write, on a row \(E\),

\[
 B_E=\left(\mathfrak P_{\rm PNT}+2\mathfrak b_K\right)|_E,
 \qquad
 W_E=\mathfrak b_{w_\Gamma}|_E>0,
 \qquad
 Q_E=B_E+W_E.                                             \tag{1}
\]

Suppose a positive allocation \(R_E\) is extracted from the available
Gamma reserve,

\[
 0\preceq R_E\preceq W_E,                                \tag{2}
\]

and is required to repair the signed block,

\[
 B_E+R_E\succeq0.                                        \tag{3}
\]

Then necessarily

\[
 \boxed{\mathrm{rank}\,R_E\ge n_-(B_E)}              \tag{4}
\]

and

\[
 \boxed{\mathrm{Tr}\,R_E\ge\mathrm{Tr}(B_E)_-.} \tag{5}
\]

Thus no bounded-rank memory, finite number of signed ports, or fixed
finite block correction can close a cofinal exhaustion on which
\(n_-(B_E)\) is unbounded.  The only possible positive-allocation closure
must spend Gamma energy in every negative direction of the literal signed
block.  At full rank, existence of such an allocation is equivalent to
the original physical sign \(Q_E\succeq0\); it is not an intermediate
theorem.

This result is an algebraic falsifier for finite-rank cofinal storage.  It
does not prove that \(n_-(B_E)\) is unbounded on the exact form-core
exhaustion, and it does not decide the physical surplus.

## 2. The rank and trace theorem

### Theorem 1 — Every repaired negative direction consumes one allocation direction

Let \(E\) be a finite-dimensional Hilbert space, let \(B=B^*\), and let
\(R\succeq0\).  If

\[
 B+R\succeq0,                                             \tag{6}
\]

then

\[
 \mathrm{rank}\,R\ge n_-(B),                         \tag{7}
\]

and

\[
 \mathrm{Tr}\,R\ge\mathrm{Tr}\,B_-.             \tag{8}
\]

Here \(B_-=(-B)_+\) and \(n_-(B)=\mathrm{rank}\,B_-\).

#### Proof

Let \(N=\mathrm{ran}\,\mathbf1_{(-\infty,0)}(B)\), so that
\(\dim N=n_-(B)\).  If \(\mathrm{rank}\,R<\dim N\), then the map

\[
 R^{1/2}|_N:N\longrightarrow E
\]

has a nonzero kernel vector \(v\in N\).  For this vector,

\[
 \langle v,Rv\rangle=\|R^{1/2}v\|^2=0,
 \qquad
 \langle v,Bv\rangle<0,
\]

contradicting (6).  This proves (7).

Choose an orthonormal eigenbasis \(e_1,\ldots,e_r\) of \(N\), with
\(Be_j=-\beta_je_j\), \(\beta_j>0\).  Equation (6) gives

\[
 \langle e_j,Re_j\rangle\ge\beta_j.
\]

Since \(R\succeq0\), completing this basis to an orthonormal basis of
\(E\) yields

\[
 \mathrm{Tr}\,R
 \ge\sum_{j=1}^r\langle e_j,Re_j\rangle
 \ge\sum_{j=1}^r\beta_j
 =\mathrm{Tr}\,B_-.
\]

This proves (8). \(\square\)

### Corollary 2 — Exact operator-valued Gamma allocation gate

Let \(B=B^*\) and \(W>0\).  There exists an operator \(R\) satisfying

\[
 0\preceq R\preceq W,
 \qquad B+R\succeq0                                    \tag{9}
\]

if and only if

\[
 \boxed{B+W\succeq0.}                                  \tag{10}
\]

#### Proof

If (9) holds, then

\[
 B+W=(B+R)+(W-R)\succeq0.
\]

Conversely, (10) permits the choice \(R=W\). \(\square\)

Applied to (1), Corollary 2 says

\[
 \exists R_E\text{ satisfying (2)--(3)}
 \quad\Longleftrightarrow\quad
 \mathfrak Q_{\rm phys}|_E\succeq0.                    \tag{11}
\]

This extends the scalar identity of 106.140 to arbitrary noncommuting
operator-valued allocations.  Noncommutativity can reduce the amount of
reserve spent in selected directions, but it cannot create a criterion
strictly weaker than the physical surplus.

## 3. Sharp finite-rank falsifier

The rank obstruction is present even when the completed physical form is
strictly positive.  Take

\[
 B=-I_2,
 \qquad W=2I_2,
 \qquad Q=B+W=I_2>0.                                  \tag{12}
\]

Every \(R\succeq0\) of rank at most one has a nonzero kernel vector \(v\).
Then

\[
 \langle v,(B+R)v\rangle=-\|v\|^2<0.                  \tag{13}
\]

Thus a one-port storage fails although the full two-direction Gamma
reserve closes the form with a strict margin.  More generally, the same
example in dimension \(m\), with \(B=-I_m\) and \(W=2I_m\), requires
allocation rank \(m\).  The obstruction is rank, not the size of the
available positive reserve.

## 4. Cofinal consequence

Let \(E_1\subset E_2\subset\cdots\) be a nested post-short heat/hybrid
form-core exhaustion.  Suppose a proposed cofinal construction uses
positive allocations \(R_m\preceq W_{E_m}\) and repairs every row:

\[
 B_{E_m}+R_m\succeq0.                                  \tag{14}
\]

Theorem 1 gives the exact necessary conditions

\[
 \mathrm{rank}\,R_m\ge n_-(B_{E_m}),
 \qquad
 \mathrm{Tr}\,R_m\ge\mathrm{Tr}(B_{E_m})_-.
                                                               \tag{15}
\]

Consequently:

1. if \(n_-(B_{E_m})\to\infty\), every bounded-state realization fails;
2. if \(\mathrm{Tr}(B_{E_m})_-\) exhausts the available Gamma
   trace, no uniform positive reserve survives;
3. allowing full-rank \(R_m\) does not solve the sign, because existence
   of \(R_m\) is exactly (11).

This conclusion is independent of a transfer representation or a Schur
factorization.  It follows directly from inertia and from the requirement
that the unused Gamma reserve remain positive.

## 5. Literal zero-span diagnostic

The script

```text
tools/cofinal_allocation_rank_diagnostic.py
```

forms (1) on weighted-orthonormal spans of the first critical-line modes

\[
 q_{\gamma_j}(x)=\frac{\cos(\gamma_jx)}{\cosh(x/2)}.
\]

It uses the literal atoms \(\Lambda(p^k)/\sqrt{p^k}\), the full numerical
Gamma density, the theta kernel, and a common spatial cutoff.  The output
is diagnostic only.  At \(x_{\max}=3.8\), the stable rows are

\[
\begin{array}{c|c|c|c|c|c}
 \dim E& n_-(B_E)&\lambda_{\min}(B_E)&\kappa_E
        &\lambda_{\min}(W_E-(B_E)_-)&\lambda_{\min}(Q_E)\\ \hline
 4&1&-1.0666\cdot10^{-1}&0.6047&6.25\cdot10^{-2}&6.40\cdot10^{-2}\\
 8&4&-1.1692\cdot10^{-1}&0.924&5.03\cdot10^{-3}&6.1\cdot10^{-3}\\
 12&6&-1.2036\cdot10^{-1}&0.985&-4.0\cdot10^{-5}&8.4\cdot10^{-4}\\
 16&9&-1.2198\cdot10^{-1}&0.998&-3.8\cdot10^{-4}&7.1\cdot10^{-5}
\end{array}                                             \tag{16}
\]

for mesh \(10^{-3}\).  Mesh \(2\cdot10^{-3}\) gives the same negative
indices \(1,4,6,9\) and respectively
\(\kappa_E=0.605,0.924,0.987,1.002\).  The last scalar is already at the
cutoff/mesh accuracy wall; larger spans eventually give a small negative
computed \(Q_E\), which cannot be interpreted as a theorem.  The robust
diagnostic information is instead that the signed block develops many
negative directions while the exact Gamma allocation is almost fully
spent.  The negative-part shortcut \(W_E\succeq(B_E)_-\) also changes
sign already near dimension \(12\), while the computed physical row is
still positive.  Meshes \(2\cdot10^{-3},10^{-3},5\cdot10^{-4}\) give
respectively \(-1.38\cdot10^{-4},-4.02\cdot10^{-5},
-2.68\cdot10^{-5}\) for that diagnostic eigenvalue.  This is consistent
with the exact rational noncommutativity falsifier of 106.140, but remains
a floating-point observation rather than an interval certificate.

No claim that \(n_-(B_{E_m})\to\infty\) is made from (16).  Proving that
claim would itself be a separate exact asymptotic theorem.

## 6. Result

Operator-valued adaptive splitting does not create a new sign mechanism.
Every repaired negative direction consumes one independent positive
allocation direction, and the existence of an unrestricted allocation is
equivalent to the original physical surplus.  Therefore a successful
cofinal signed prime--Gamma--pole argument cannot be a bounded-rank
positive storage correction.  It must either establish the complete
physical form directly or use a genuinely signed, source-specific
mechanism whose positivity is not obtained by leaving a positive Gamma
remainder.
