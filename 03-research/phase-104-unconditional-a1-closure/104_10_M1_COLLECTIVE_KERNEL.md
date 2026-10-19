# 104_10 — M1: collective kernel max(i,j)

**Status:** preregistration executed; the local-PSD version of M1 is ruled out with exact
witnesses. The global version is also closed as a mechanism: `104_11` proves that the
compensator is the energy of the same `max` kernel and that the two Hessians cancel
identically, boundary term included. Neither A1 nor RH is proved.

## 1. Goal and implication

\(\theta=1/4\) is fixed. M1 does not attack A1 directly: it attempts to prove the stronger
sufficient condition

\[
 \Delta D_n\ge0,\qquad D_n=2\lambda_n-A_n,\qquad n\ge149.
\tag{1}
\]

Since \(D_{149}>0\) is certified in 103_51, (1) would imply \(D_n>0\) for every
\(n\ge149\), hence the strong margin \(\lambda_n\ge A_n/2\), A1 together with A0, and finally
RH. The implication is correct, but 103_59 already proves that (1) is structurally stronger
than RH for general symmetric entire functions.

## 2. Axioms and inputs

Every use of M1 must declare which of these levels it employs.

**Finite algebraic level.**

1. \(q_1<\cdots<q_M\) are real numbers \(>1\).
2. \(\ell_j>0\), \(\Psi_j=\sum_{i\le j}\ell_i\), and
   \(d_j=q_j-1-\Psi_{j-1}-\ell_j/2\).
3. \(w_1,\ldots,w_M\) are arbitrary real numbers.

**Regulated arithmetic level.**

4. \(q_j\) ranges over the prime powers and \(\ell_j=\Lambda(q_j)\).
5. For \(n\ge0,\varepsilon>0\),
   \[
   \tau(x)=x^{-1-\varepsilon}L_n(\log x),\qquad w(x)=\tau'(x),
   \qquad E(x)=\psi(x)-x+1.
   \tag{2}
   \]
6. PNT is used only to make the boundary term vanish as \(X\to\infty\) with
   \(\varepsilon>0\). The effective PNT triple declared in 104_01 is not used.

The special datum of level 4 cannot be replaced by "positive atomic measure": that would be a
strict relaxation, and 103_59 already shows that the resulting transport has both signs.

## 3. Finite regulated identity, with the missing boundary term

Let \(X>1\) not be a prime power, and define

\[
 C_{n,\varepsilon}(X):=-\int_1^X E(x)\tau'(x)\,dx,\qquad
 G(X)=\int_1^X E(t)\,dt.
\tag{3}
\]

Set

\[
 \mathcal H(X)=\sum_{q_j\le X}\ell_j(q_j-1)-{\psi(X)^2\over2}.
\tag{4}
\]

As proved in 103_67,

\[
 \mathcal H(X)=-G(X)-{E(X)^2\over2},\qquad
 d\mathcal H=\sum_j\ell_jd_j\delta_{q_j}.
\tag{5}
\]

Two integrations by parts **on the finite interval** give

\[
 \boxed{
 C_{n,\varepsilon}(X)
 =\sum_{q_j<X}\ell_jd_jw(q_j)
  -{1\over2}\int_1^X E(x)^2\tau''(x)\,dx
  +{1\over2}E(X)^2w(X).}
\tag{6}
\]

*Proof.* From \(G'=E\),
\[
 C(X)=-G(X)w(X)+\int_1^XG(x)\tau''(x)\,dx.
\]
Inserting \(G=-\mathcal H-E^2/2\) and integrating
\(-\int\mathcal H\tau''\) in the Stieltjes sense yields
\(-\mathcal H(X)w(X)+\int w\,d\mathcal H\). By (5), the two boundary terms add to
\(-[G(X)+\mathcal H(X)]w(X)=E(X)^2w(X)/2\), giving (6). \(\square\)

The last term of (6) is mandatory in every truncation. For
\(\varepsilon>0\) it tends to zero as \(X\to\infty\), recovering the identity of
103_67:

\[
 C_{n,\varepsilon}
 =\sum_j\ell_jd_jw_j-{1\over2}\int_1^\infty E(x)^2\tau''(x)\,dx.
\tag{7}
\]

Separating the two terms of (7) and taking absolute values is forbidden: their reverse
integration by parts exactly reconstructs \(C_{n,\varepsilon}\).

## 4. The max(i,j) identity and all the discrete boundary terms

At the finite algebraic level,

\[
 \boxed{
 \sum_{j=1}^M\ell_jd_jw_j
 =\sum_{j=1}^M\ell_j(q_j-1)w_j
  -{1\over2}\sum_{i,j\le M}\ell_i\ell_jw_{\max(i,j)}.}
\tag{8}
\]

Let
\[
 H_j=\sum_{i\le j}\ell_i(q_i-1)-{\Psi_j^2\over2},\qquad H_0=0.
\tag{9}
\]
Then, with no implicit limit,
\[
 \boxed{
 \sum_{j=1}^M\ell_jd_jw_j
 =\sum_{j=1}^{M-1}H_j(w_j-w_{j+1})+H_Mw_M.}
\tag{10}
\]

The term \(H_Mw_M\) is the discrete boundary term. Writing only
\(\sum H_j(w_j-w_{j+1})\) on a finite prefix is incorrect.

### Exact block decomposition

Let \(0=m_0<m_1<\cdots<m_B=M\), \(I_b=(m_{b-1},m_b]\),
\[
 P_{b-1}=\sum_{i\le m_{b-1}}\ell_i,\qquad
 L_{b,k}=\sum_{m_{b-1}<i\le k}\ell_i,\qquad L_b=L_{b,m_b}.
\tag{11}
\]
The quadratic form of (8) decomposes exactly as
\[
 \begin{split}
 {1\over2}\sum_{i,j\le M}\ell_i\ell_jw_{\max(i,j)}
 =\sum_{b=1}^B\Bigg\{&
 P_{b-1}\sum_{j\in I_b}\ell_jw_j
 +{w_{m_b}\over2}L_b^2\\
 &+{1\over2}\sum_{k=m_{b-1}+1}^{m_b-1}
 (w_k-w_{k+1})L_{b,k}^2\Bigg\}.
 \end{split}
\tag{12}
\]

*Proof.* Within a block,
\[
 w_{\max(i,j)}
 =w_{m_b}+\sum_{k=\max(i,j)}^{m_b-1}(w_k-w_{k+1}).
\]
Summing over \(i,j\in I_b\) gives the last two terms of (12). If \(i\) is in an
earlier block and \(j\in I_b\), then \(w_{\max(i,j)}=w_j\); the two orientations of the pair
cancel the factor \(1/2\) and give the first term. \(\square\)

For a globally non-increasing infinite sequence with limit \(w_\infty\),
\[
 w_{\max(i,j)}
 =w_\infty+\sum_{k\ge\max(i,j)}(w_k-w_{k+1}).
\tag{13}
\]
Thus the form is PSD if \(w_\infty\ge0\) and all the differences are non-negative. In the
real kernel \(w=\tau'\), \(w_\infty=0\), but \(w\) alternates in monotonicity: (13) does not
give global PSD.

## 5. Exact no-go for the local-PSD strategy

The phrase "each decreasing block gives a PSD form" omits three terms that decide the sign:

1. the rank-one term \(w_{m_b}L_b^2/2\), which is negative if \(w_{m_b}<0\);
2. the cross terms
   \(P_{b-1}\sum_{j\in I_b}\ell_jw_j\), with no fixed sign;
3. the increasing blocks, where \(w_k-w_{k+1}<0\).

By (10), keeping the first moment and the max form together does not remove the problem: it
collapses them into the signed correlator \(H_j(w_j-w_{j+1})\). And \(H_j\) also has no fixed
sign for the **real** von Mangoldt weights.

The tool tools/m1_cumulative_sign_certificate.py uses only outward rational arithmetic for
the logarithms of the primes and certifies
\[
 \boxed{H(2969)<-21,\qquad H(3167)>110.}
\tag{14}
\]
Here \(H(x)=\sum_{q\le x}\Lambda(q)(q-1)-\psi(x)^2/2\). Therefore neither a global
orientation of \(H\), nor a global orientation of \(w_j-w_{j+1}\), nor blockwise PSD can
prove (7).

**M1-local verdict:** ruled out by witness (12)–(14). A global sum across blocks might still
cancel, but that requires a new correlated inequality; it is not a consequence of PSD.

## 6. Falsifiers and correct scope

### 6.1 Falsifier of arithmetic relaxations

If a step uses only axioms 1–3 (ordered positive atoms), the mass-move falsifier of 103_59
applies: moving a mass \(W\) from \(b\) to \(a<b\) gives
\[
 \delta C=W\{\tau(a)-\tau(b)\}.
\tag{15}
\]
For \(n=1\) the kernel has an explicit zero and (15) takes both signs. It satisfies exactly
the relaxed algebraic axioms and kills any conclusion based solely on positivity, monotonicity
of the counting function, or atomic support.

### 6.2 Spectral falsifier

If a step stops using level 4 and uses only functional symmetry/critical localization, apply
\[
 X(s)=\left(s-\tfrac12\right)^2+\tfrac14.
\tag{16}
\]
All its zeros lie on the line, but \(\Delta\lambda_2[X]=-2\). This kills any derivation of
(1) from RH or from squares of an individual zero.

The off-line quartet
\[
 8-8\cosh(n\alpha)\cos(n\vartheta)
\tag{17}
\]
is used in the same way against steps that retain only conjugation and the functional
equation.

### 6.3 Logical limit of the "same axioms" requirement

Level 4 literally fixes \(q=p^k\) and \(\ell=\log p\): it fixes the arithmetic of \(\zeta\).
An "off-line divisor" also satisfying that same axiom would be \(\zeta\) itself with an
off-line zero, whose existence is exactly the question at hand. That is why (17) **cannot
honestly be required** as a model satisfying level 4 without presupposing the negation of
RH.

The valid rule is: whenever an estimate relaxes level 4, it must pass the falsifier
corresponding to the axioms it actually retains. An argument using a special quantitative
property of the real weights is not refuted by (15)–(17), but must declare and prove that
property.

## 7. Global correlator: later stop-gate

After the local no-go, what remained was to directly and uniformly prove
\[
 \limsup_{\varepsilon\downarrow0}
 \left[
 \sum_j H_j(w_j-w_{j+1})
 -{1\over2}\int_1^\infty E(x)^2\tau''(x)\,dx
 \right]
 \le {1\over2}\Delta A_n,\qquad n\ge149,
\tag{18}
\]
with the boundary term of (6) controlled before each limit.

`104_11`, Theorems 1–2, identifies the second term and its boundary term with the `max`
energy of \(d\psi-dx\). Adding it to the first term, the quadratic component cancels
exactly and (18) reduces back to

\[
 -\int_1^\infty E(x)\tau'(x)\,dx\le {1\over2}\Delta A_n.
\]

Therefore (18) is not a living global version of M1: it is the linear first-difference
target with no residual coercivity. Proving it would still be sufficient for A1, but it
would no longer be a consequence of the `max` mechanism. M1 is ruled out; its successor is
recorded in `104_11` and developed separately.

## Status

| item | result |
|---|---|
| finite regulated identity with boundary term | proved, (6) |
| max identity and boundary term \(H_Mw_M\) | proved, (8)–(10) |
| blocks, cross terms, and rank one | proved, (12) |
| global PSD | false for the oscillatory \(w\) |
| sign of real \(H\) | false, certified (14) |
| M1 local-PSD | ruled out |
| global Hessian of (18) | exactly zero, boundary term included (`104_11`) |
| M1 global | ruled out: collapses to the original linear functional |
| A1/RH | not proved |
</content>
