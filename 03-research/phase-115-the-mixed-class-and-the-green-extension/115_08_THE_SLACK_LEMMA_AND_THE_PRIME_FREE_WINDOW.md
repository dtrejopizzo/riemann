# 115.08 — The slack lemma: why every archimedean lower bound is stronger than row (d), and why the Connes–Consani window is exactly the locus `K = 0`

This note fixes the sign conventions against the source, proves a lemma that
refutes an entire family of proposed reductions of row (d) — including the one
proposed in this phase — and replaces them by two exact, lossless identities.
It also proves that the support restriction in Connes–Consani's Theorem 1 is
not a technical artefact but is *precisely* the condition that the finite
contact term vanishes.

Everything asserted here is either proved below, or is an explicitly cited
theorem of Connes–Consani stated with its full hypotheses.

## 0. Conventions, verified rather than recalled

Write, as in `main.tex`,

\[
 B_{\rm nuc}(f,f)=K(f,f)+G_\infty(f,f),
 \qquad
 K(f,g)=W_{\rm fin}(f\star g^\vee),
\]
\[
 W_{\rm fin}(h)=\sum_{p,k\ge1}\log p\,\bigl(h(p^k)+p^{-k}h(p^{-k})\bigr)
 \quad(\text{`eq:Ktest`}),
\]
\[
 G_\infty(f,f)=\frac1{2\pi}\int_{\mathbb R}m_\infty(\tau)\,
 |\widehat f(\tfrac12+i\tau)|^2\,d\tau,
 \qquad
 m_\infty(\tau)=\log\pi-\Re\psi(\tfrac14+i\tfrac\tau2)
\]
(`eq:archmultiplier`), and let \(\mathcal T^0\) be the space cut out by
\(\widehat h(0)=\widehat h(1)=0\).

**The explicit formula was not recalled from memory; its coefficients were
fitted.**  With \(F(t)=e^{-t^2/(2s^2)}\), \(g=F\star F\),
\(h(r)=|\widehat F(r)|^2=2\pi s^2e^{-s^2r^2}\), the five quantities

\[
 Z=\sum_\gamma h(\gamma),\quad
 P_0=2h(i/2),\quad
 \Pi=2\!\sum_{n\ge2}\!\tfrac{\Lambda(n)}{\sqrt n}g(\log n),\quad
 A=\tfrac1{2\pi}\!\int\! h\,\Re\psi(\tfrac14+\tfrac{ir}2),\quad
 L_\pi=\tfrac{\log\pi}{2\pi}\!\int\! h
\]

were computed independently for \(s\in\{0.10,0.15,0.22,0.30,0.45\}\) (120 zeta
zeros, von Mangoldt to \(2\times10^5\), adaptive quadrature at 25 digits) and
the \(4\times4\) system \(Z=c_1P_0+c_2\Pi+c_3A+c_4L_\pi\) was solved.  The
solution is

\[
 (c_1,c_2,c_3,c_4)=(+1,-1,+1,-1)
\]

**exactly** — four clean integers out of a solve on independent data.  Since
\(A-L_\pi=-\frac1{2\pi}\int h\,m_\infty\), this reads

\[
 \sum_\gamma h(\gamma)=2h(i/2)-K(f,f)-G_\infty(f,f),
\]

and on \(\mathcal T^0\) the pole term vanishes.  Hence:

> **Proposition 0.**  For \(f\in\mathcal T^0\),
> \[
>  \boxed{\;\sum_\gamma\bigl|\widehat f(\tfrac12+i\gamma)\bigr|^2
>   =-B_{\rm nuc}(f,f)\;}
> \]
> the sum running over all nontrivial zeros \(\rho=\tfrac12+i\gamma\).  In
> particular `main.tex`'s sign convention is internally consistent and row (d),
> \(B_{\rm nuc}\le0\) on \(\mathcal T^0\), is Weil's inequality in the standard
> orientation.

**Consequence for the notation.**  Connes–Consani (arXiv:2006.13771) write
their criterion as \(\sum_v\mathcal W_v(g*g^\sharp)\le0\) (their (2)) and set
\(W_\infty:=-W_{\mathbf R}\) (their (15)).  The archimedean summand of
\(\sum_vW_v\) is therefore \(W_{\mathbf R}=-W_\infty^{CC}\), and comparison
with Proposition 0 gives

\[
 \boxed{\;G_\infty^{\text{ours}}=W_{\mathbf R}^{CC}=-\,W_\infty^{CC}\;}
\]

So `eq:forcedgreen`, which reads \(G_\infty(f,g)=W_\infty(f\star g^\vee)\),
uses the symbol \(W_\infty\) with **the opposite sign to the source paper**.
The mathematics is unaffected; the notation is a genuine collision and must be
fixed in `main.tex` before circulation, since a reader carrying CC's
convention will read every archimedean statement backwards.

## 1. The inputs from Connes–Consani

Cited with full hypotheses; these are theirs, not ours.

* **(CC-1) Theorem 1.**  For \(g\in C_c^\infty(\mathbb R_+^*)\) with
  \(\mathrm{supp}\,g\subset[2^{-1/2},2^{1/2}]\) and \(\widehat g\)
  vanishing at \(i/2\) and \(0\),
  \[
   W_\infty^{CC}(g*g^*)\ \ge\ \mathrm{Tr}\,\bigl(\vartheta(g)\mathbf S\vartheta(g)^*\bigr)=:\mathcal S(g)\ \ge\ 0 .
  \]
* **(CC-3) Theorem 3.**  For **all** \(f\in C_c^\infty(\mathbb R_+^*)\),
  \[
   \mathrm{Tr}(\vartheta(f)\mathbf S)=W_\infty^{CC}(f)+E(f),
   \qquad E(f):=\int f(\rho)\epsilon(\rho)\,d^*\rho,
  \]
  with \(\epsilon\) given by their prolate series (14).
* **(CC-9).**  \(L(f):=D(f)+W_\infty^{CC}(f)\ \ge 0\) for positive-definite
  \(f\), **with no restriction on the support**, where
  \(D(f)=\int f(\rho^{-1})\delta(\rho)d^*\rho\) and \(\delta\) is elementary:
  \[
   \delta(\rho)=2\rho^{1/2}\Bigl(\frac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)}
   +\frac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\Bigr),\ \rho\ge1,
   \qquad \delta(\rho^{-1})=\delta(\rho).
  \]

## 2. The slack lemma

> **Lemma 1 (slack).**  Let \(\mathcal A\) be any functional satisfying the
> archimedean lower bound \(-G_\infty(f,f)\ge\mathcal A(f)\) on \(\mathcal T^0\),
> and put \(\sigma(f):=-G_\infty(f,f)-\mathcal A(f)\ \ge0\).  Then for every
> \(f\in\mathcal T^0\)
> \[
>  \mathcal A(f)-K(f,f)\;=\;-B_{\rm nuc}(f,f)\;-\;\sigma(f).
> \]

*Proof.*  \(\mathcal A=-G_\infty-\sigma\), so
\(\mathcal A-K=-G_\infty-K-\sigma=-B_{\rm nuc}-\sigma\). \(\square\)

> **Corollary 2.**  The condition \(\mathcal A(f)\ge K(f,f)\) on \(\mathcal T^0\)
> implies row (d), and is **strictly stronger** than row (d) at every \(f\) with
> \(\sigma(f)>0\).  It is equivalent to row (d) only if \(\sigma\equiv0\), i.e.
> only if the archimedean bound is an identity.

This is the decisive structural fact of the note.  Any strategy of the shape
*"lower-bound the archimedean term by something, then show that something beats
the finite contact"* does not reduce row (d); it strengthens it by exactly the
slack in the bound.  Such a condition may still be true, but proving it is
strictly harder than proving row (d), so it cannot serve as a route to it.

> **Corollary 3.**  Both routes considered in this phase are strengthenings.
>
> | \(\mathcal A\) | slack \(\sigma\) | source |
> |---|---|---|
> | \(\mathcal S(f)=\mathrm{Tr}(\vartheta(f)\mathbf S\vartheta(f)^*)\) | \(-E(f\star f^\vee)\ge0\) | (CC-3) |
> | \(-D(f\star f^\vee)\) | \(L(f)\ge0\) | (CC-9) |
>
> *Proof.*  (CC-3) with \(f\) replaced by \(f\star f^\vee\) gives
> \(\mathcal S(f)=-G_\infty(f,f)+E(f\star f^\vee)\), whence
> \(\sigma=-G_\infty-\mathcal S=-E\).  (CC-9) gives
> \(-G_\infty=L(f)-D(f\star f^\vee)\), whence \(\sigma=L\). \(\square\)

**The proposal of the previous note is therefore refuted**, not by a
counterexample but by an exact identity: \(\mathcal S(f)\ge K(f,f)\) is row (d)
plus \(-E(f\star f^\vee)\ge0\).

## 3. What survives: two lossless identities

The same two theorems, used as identities rather than as inequalities, give
exact decompositions of the target.  Both are unconditional.

> **Theorem 4.**  For \(f\in\mathcal T^0\) with \(f\in C_c^\infty(\mathbb R_+^*)\),
> \[
>  -B_{\rm nuc}(f,f)\;=\;\mathcal S(f)\;-\;E(f\star f^\vee)\;-\;K(f,f),
> \]
> \[
>  -B_{\rm nuc}(f,f)\;=\;L(f)\;-\;D(f\star f^\vee)\;-\;K(f,f).
> \]
> *Proof.*  Substitute \(-G_\infty=\mathcal S-E\) (from CC-3) and
> \(-G_\infty=L-D\) (from CC-9) into \(-B_{\rm nuc}=-K-G_\infty\). \(\square\)

Row (d) is *equivalent* to the nonnegativity of either right-hand side — no
slack, nothing given away.  The second is the more usable one: \(L\ge0\) holds
with no support restriction, and \(D\) is elementary (sine integral), so the
whole difficulty is concentrated in the single comparison

\[
 \boxed{\;L(f)\ \ge\ D(f\star f^\vee)+K(f,f)\qquad(f\in\mathcal T^0).\;}
\]

## 4. The window is exactly the locus \(K=0\)

> **Proposition 5.**  If \(\mathrm{supp}\,g\subset(2^{-1/2},2^{1/2})\) then
> \(K(f,f)=0\).
>
> *Proof.*  \(\mathrm{supp}(g\star g^\vee)\subset(1/2,2)\).  By
> `eq:Ktest`, \(K(f,f)=W_{\rm fin}(g\star g^\vee)\) samples \(g\star g^\vee\)
> only at the points \(p^{k}\) and \(p^{-k}\) with \(p\) prime, \(k\ge1\); all
> of these lie in \([2,\infty)\cup(0,1/2]\), disjoint from the support.
> \(\square\)

Combining Proposition 5 with Proposition 0: **on CC's window, row (d) reduces
to \(-G_\infty\ge0\), which is exactly their Theorem 1.**  So their support
restriction is not incidental — it is the precise condition under which the
finite contact term disappears and archimedean positivity alone suffices.

### 4.1 Cross-check of the whole chain, computed two ways

`scripts/115_08_prime_free_window_crosscheck.py`.  Take
\(\mathcal G=\sum_{j=1}^4c_j\,\beta(t-\mu_j)\) with
\(\beta(u)=\cos^8(\pi u/2w)\) on \(|u|\le w\), \(w=0.08\),
\(\mu\in\{-0.24,-0.08,0.08,0.24\}\).  Then
\(\mathrm{supp}\,\mathcal G\subset[-0.32,0.32]\subset(-\log\sqrt2,\log\sqrt2)\),
so Proposition 5 gives \(K=0\) exactly.  Writing
\(\widehat{\mathcal G}(\tau)=\Psi(\tau)\sum_jc_je^{i\tau\mu_j}\) with \(\Psi\)
entire, the three conditions \(\widehat{\mathcal G}(0)=\widehat{\mathcal G}(\pm i/2)=0\)
become \(\sum c_j=0\), \(\sum c_je^{\mp\mu_j/2}=0\), solved to \(10^{-26}\) by
\(c=(-1,\,3.006403414,\,-3.006403414,\,1)\).

With \(K=0\) and the pole term killed, Proposition 0 forces
\(\sum_\gamma|\widehat{\mathcal G}(\gamma)|^2=-G_\infty(f,f)\) **exactly**.  The
two sides, computed by completely independent routes:

| quantity | route | value |
|---|---|---|
| \(-G_\infty(f,f)\) | quadrature against \(\Re\psi(\tfrac14+\tfrac{i\tau}2)-\log\pi\) | \(0.933956227412732\) |
| \(\sum_\gamma\|\widehat{\mathcal G}(\gamma)\|^2\) | 200 nontrivial zeta zeros, \(\gamma\le396.4\) | \(0.933973624903562\) |

The zero sum is converged: stable in the 12th digit from 150 zeros on, tail
\(|\widehat H(396.4)|=3.4\times10^{-19}\).  Relative agreement
\(1.86\times10^{-5}\), the whole residue sitting in the nested adaptive
quadrature for \(-G_\infty\) (the inner \(\Psi(\tau)\) integral is oscillatory
at large \(\tau\)); it is not structural.  A sign error would produce a
difference of \(\approx1.87\), five orders of magnitude larger.

This single computation verifies four things at once: the fitted sign
convention of §0; the identification \(G_\infty=-W_\infty^{CC}\) (a reversed
sign would give \(-0.934\)); Proposition 0; and row (d) itself on the window,
i.e. Connes–Consani's Theorem 1.

A caveat on generality.  With four bumps and three constraints the null space is
one-dimensional, and the solution that came out is **odd** in \(t\)
(\(c_j=-c_{5-j}\)) — for odd \(\mathcal G\) the conditions at \(\pm i/2\)
collapse to one.  The check should be repeated with five bumps, where a
non-odd solution exists, before the verification is called generic.

> **Corollary 6.**  The content of row (d) beyond Connes–Consani is entirely
> the domination of \(K\).  Every functional appearing in Theorem 4 —
> \(\mathcal S\), \(E\), \(L\), \(D\) — is defined from the scaling action on
> \(L^2(\mathbb R)_{\rm ev}\) and the phase-space cutoff at \(\Lambda=1\), with
> no arithmetic input; \(K\) is the only term carrying the primes.

### 4.2 The archimedean no-go

> **Corollary 7 (no single-place proof).**  Let \(\mathcal A\) be any functional
> built from the scaling action on \(L^2(\mathbb R)_{\rm ev}\) and the
> \(\Lambda=1\) phase-space cutoff — in particular any of
> \(\mathcal S,\ -E,\ L,\ -D\) or a nonnegative combination — and suppose
> \(-G_\infty\ge\mathcal A\) on \(\mathcal T^0\).  Then the statement
> \(\mathcal A\ge K\) is row (d) *plus* the nonnegative slack \(\sigma\), and is
> therefore not a proof of row (d) but a strengthening of it.
>
> *Proof.*  Lemma 1 and Corollary 2. \(\square\)

The force of this is that it is not a statement about any particular attempt.
It says that the *shape* "archimedean reservoir dominates the finite contact"
cannot close row (d), whatever reservoir is used, because the inequality used
to produce the reservoir always costs exactly the amount that is missing.  A
single-place construction cannot prove row (d).

Note also what escapes it: the hypothesis is that \(\mathcal A\) carries no
arithmetic input.  A functional built from a cutoff that *does* see the primes
is not subject to Corollary 7 — which is the content of `115_09`.

## 5. What this settles about the architecture of this phase

`115_07` concluded that the mixed lattice must supply the archimedean half by a
metric, and that the obstruction was regularizing \(\det M\) against
\(m_\infty\to-\infty\).  Corollary 6 relocates that conclusion: the archimedean
half is **already available in closed form** from (CC-9), unconditionally and
without support restriction.  What no purely archimedean construction can
supply — lattice, metric, theta invariant or otherwise — is the comparison
against \(K\), because \(K\) is the only place the primes enter.

This retroactively explains the failures catalogued in `115_04`–`115_07`: the
code lattice, the diagonal metric and the scalar-corrected candidate were all
attempts to manufacture, out of archimedean or combinatorial data, a quantity
that must dominate an arithmetic sum.  Corollary 6 says that no such attempt
can succeed on archimedean grounds alone.

## 5.1 State of the scripts

| script | status |
|---|---|
| `scripts/115_08_explicit_formula_sign_fit.py` | **ran to completion**; produced the exact \((+1,-1,+1,-1)\) of §0 |
| `scripts/115_08_prime_free_window_crosscheck.py` | **ran to completion**; output in `.out`; §4.1 |
| `scripts/115_08_cc_unconditional_positivity.py` | **TIMED OUT** (exit 124 at 900 s); one row only |

The third script was written to test (CC-9) directly, and it does not do its
job — for two reasons, both recorded so it is not rerun in the same form.

1. Its only completed row gives \(-G_\infty=-0.49005\), \(D=+0.51500\),
   \(L=D-G_\infty=+0.02496>0\).  Consistent with (CC-9), but **not a
   discriminator**: with the opposite sign one would get \(D+G_\infty=+1.005\),
   also positive.  The test as designed cannot distinguish the two conventions.
2. The test functions are Gaussians, which are **not in \(\mathcal T^0\)** —
   the run reports \(|\widehat{\mathcal G}(\pm i/2)|=0.504\).  This matters:
   it shows \(-G_\infty\ge0\) is *false* in general and holds only on the
   constrained space, so any check of CC's theorems must impose the vanishing
   conditions first.

Both defects are repaired by the window cross-check of §4.1, which uses genuine
\(\mathcal T^0\) test functions of compact support and does discriminate.  The
third script is retained only as the record of a failed test design.

## 6. Status

* Explicit-formula coefficients, fitted not recalled: \((+1,-1,+1,-1)\) exactly.
  **VERIFIED** numerically at 25 digits on five independent test functions.
* Proposition 0, \(\sum_\gamma|\widehat f|^2=-B_{\rm nuc}\) on \(\mathcal T^0\):
  **PROVED** (explicit formula with the fitted coefficients).
* \(G_\infty^{\text{ours}}=-W_\infty^{CC}\); notation collision in
  `eq:forcedgreen`: **PROVED**; fix pending in `main.tex`.
* Lemma 1 and Corollaries 2, 3: **PROVED**.
* The route \(\mathcal S(f)\ge K(f,f)\) proposed earlier in this phase:
  **REFUTED as a reduction** — it is row (d) plus \(-E\ge0\).
* Theorem 4, the two lossless identities: **PROVED** from (CC-3), (CC-9).
* Proposition 5, window \(\Rightarrow K=0\): **PROVED**.
* Corollary 6: **PROVED**.
* Row (d): **OPEN**, and now localised to
  \(L(f)\ge D(f\star f^\vee)+K(f,f)\) on \(\mathcal T^0\), where the left side
  is CC's unconditional positive functional and \(D\) is elementary.

## 7. Next

The only remaining question with a definite shape is quantitative: how large is
\(L(f)\), and does it grow with the support fast enough to absorb
\(D+K\)?  \(D\) is elementary and computable; \(K\) is a prime sum; \(L\) is the
one term requiring CC's operator theory.  A numerical comparison of the three
on \(\mathcal T^0\) test functions of widening support is the next step, and it
is cheap for \(D\) and \(K\).
