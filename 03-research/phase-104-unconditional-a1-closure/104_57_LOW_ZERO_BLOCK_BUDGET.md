# 104_57 — Exact budget for the low zero block

**Role.** Turn Lagarias's corrected translation into a bound, not a mere
coordinate. This document proves neither A1 nor RH. It isolates the single
block of zeros that retains RH strength, fixes its cardinality with all
factor-of-two conventions, and gives an algebraic criterion for discarding
estimates whose error is incompatible with the margin they claim.

**Binding dependencies.** The sign erratum of `104_02`, the A1 normalization
of `104_01`, and the fully numerical counting bound of `103_58` §2 are used.
The printed sign of (1.15), (1.17) or (6.7) of Lagarias is not imported.

---

## 1. Conventions and exact decomposition

Let

\[
 \lambda_n(T):=
 \sum_{\substack{\rho\text{ nontrivial zero}\ |\Im\rho|<T}}
 m_\rho\left[1-\left(1-{1\over\rho}\right)^n\right]             \tag{1}
\]

be Lagarias's incomplete coefficient. The inequality on the height is
**strict**. Thus the definition does not need to decide what to do if an
ordinate were exactly equal to the cutoff.

We define

\[
 L_n^{<}:=\lambda_n(\sqrt n),\qquad
 L_n^{>}:=\lambda_n-L_n^{<}.                                  \tag{2}
\]

The second quantity means the difference between the complete coefficient,
with its canonical symmetric-sum convention, and the finite sum (1). It is
not claimed to be an absolutely convergent sum obtained by subtracting terms
one by one.

Erratum `104_02`, equations (2.3)--(2.4), defines

\[
 \widetilde\varepsilon_n:=A_n-\lambda_n+L_n^{<}
\]

and proves unconditionally that there is an absolute constant \(C_*>0\) such
that

\[
 |\widetilde\varepsilon_n|\le C_*\sqrt n\log n.                 \tag{3}
\]

The constant exists but was not made explicit by that argument.

### Theorem 1 (the high tail reproduces the archimedean block) `[INC]`

For every \(n\ge2\),

\[
 \boxed{
 L_n^{>}=A_n-\widetilde\varepsilon_n,\qquad
 |L_n^{>}-A_n|\le C_*\sqrt n\log n.}                            \tag{4}
\]

In particular,

\[
 \boxed{\lambda_n=A_n+L_n^{<}-\widetilde\varepsilon_n.}         \tag{5}
\]

**Proof.** From the definition of

\(
\widetilde\varepsilon_n=A_n-\lambda_n+L_n^{<}
\)

one gets

\(
\lambda_n-L_n^{<}=A_n-\widetilde\varepsilon_n
\).
The bound is (3). RH plays no role. \(\square\)

This is the precise form of the phrase "the zeros with
\(|\gamma|\ge\sqrt n\) reproduce \(A_n\)": it is an identity for the
**canonically regularized** tail and an unconditional error
\(O(\sqrt n\log n)\). It is not a term-by-term positivity of those zeros.

---

## 2. Exact translation of A1 and of the quartic margin

For \(\theta=1/4\), `104_02` proves

\[
 \mathrm {A1}_{1/4}
 \iff
 -L_n^{<}+\widetilde\varepsilon_n+R_n(T_n)
 \le {3\over4}A_n.                                             \tag{6}
\]

Hence the lower-bound form is

\[
 \boxed{
 \mathrm {A1}_{1/4}
 \iff
 L_n^{<}\ge-{3\over4}A_n+\widetilde\varepsilon_n+R_n(T_n).}    \tag{7}
\]

Separately, for any \(c\in\mathbb R\), (5) gives the purely algebraic
equivalence

\[
 \boxed{
 \lambda_n\ge cA_n
 \iff
 L_n^{<}\ge-(1-c)A_n+\widetilde\varepsilon_n.}                 \tag{8}
\]

In particular,

\[
 \boxed{
 4\lambda_n\ge A_n
 \iff
 L_n^{<}\ge-{3\over4}A_n+\widetilde\varepsilon_n.}             \tag{9}
\]

Using only (3), one gets the one-sided sandwich

\[
 L_n^{<}\ge-{3\over4}A_n+C_*\sqrt n\log n
 \quad\Longrightarrow\quad
 4\lambda_n\ge A_n,                                           \tag{10}
\]

and

\[
 4\lambda_n\ge A_n
 \quad\Longrightarrow\quad
 L_n^{<}\ge-{3\over4}A_n-C_*\sqrt n\log n.                    \tag{11}
\]

The two boundaries are separated by \(2C_*\sqrt n\log n\). Since \(C_*\)
is not effective, (10) does not by itself produce a numerical threshold.

**Logical status.** (4)--(11) are unconditional. Proving the lower bound of
(7) or (9) uniformly remains the RH-strength step; none of these
identities proves it.

---

## 3. How many terms actually remain

Let

\[
 N_{<}(T):=\sum_{\substack{\rho=\beta+i\gamma\text{ zero}\\0<\gamma<T}}m_\rho
                                                                    \tag{12}
\]

be the count of **positive** ordinates, with multiplicity and a strict
cutoff. Conjugation symmetry implies that (1) contains exactly
\(2N_{<}(T)\) zero labels.

The Riemann–von Mangoldt formula unconditionally gives `[INC]`

\[
 N_{<}(T)={T\over2\pi}\log{T\over2\pi e}+O(\log T).             \tag{13}
\]

Changing \(<T\) to \(\le T\) does not change this asymptotic. At \(T=\sqrt n\),

\[
 \boxed{
 N_{<}(\sqrt n)
 ={\sqrt n\over4\pi}\log n
 -{\sqrt n\over2\pi}\log(2\pi e)+O(\log n).}                 \tag{14}
\]

So the low block contains

\[
 \boxed{
 2N_{<}(\sqrt n)
 ={\sqrt n\over2\pi}\log n+O(\sqrt n)}                       \tag{15}
\]

labeled summands. The factor \(1/(4\pi)\) corresponds to the count of
**positive ordinates**; the factor \(1/(2\pi)\), to the number of labels in
the symmetric sum. Mixing them up wrongly doubles or halves the budget.

There is also a fully numerical bound already proved in `103_58` §2. If
\({\cal N}(T)\) counts both signs, then

\[
 {\cal N}(T)\le25T\log T\qquad(T\ge10).                         \tag{16}
\]

Hence, for \(n\ge100\),

\[
 \boxed{
 2N_{<}(\sqrt n)\le {25\over2}\sqrt n\log n,
 \qquad
 N_{<}(\sqrt n)\le {25\over4}\sqrt n\log n.}                 \tag{17}
\]

These constants are deliberately coarse; their purpose is that no future
argument can hide a Riemann–von Mangoldt constant.

### Local calibration `[COND: RH for \(|\gamma|<\sqrt n\)]`

If the zeros of the block are on the critical line, each conjugate pair
contributes

\[
 2-2\cos(n\vartheta_\rho)\in[0,4].
\]

Then

\[
 \boxed{
 0\le L_n^{<}\le4N_{<}(\sqrt n)
 ={\sqrt n\over\pi}\log n+O(\sqrt n).}                         \tag{18}
\]

The natural scale of the low block under RH is therefore
\(\sqrt n\log n\), the same as the transport error (3). Inequality
(18) is not an unconditional input.

---

## 4. Exact scale of a zero off the line `[INC]`

Let \(\rho=\beta+i\gamma\), \(\beta>1/2\), and

\[
 w_\rho:=1-{1\over\rho}={\rho-1\over\rho}.
\]

Then

\[
 |w_\rho|^2
 ={\gamma^2+(1-\beta)^2\over\gamma^2+\beta^2}
 =1-{2\beta-1\over\gamma^2+\beta^2}<1.                        \tag{19}
\]

Write \(w_\rho=e^{-a_\rho+i\vartheta_\rho}\), \(a_\rho>0\). With

\[
 d:=2\beta-1,\qquad x:={d\over\gamma^2+\beta^2}\in(0,1),
\]

one has exactly

\[
 a_\rho=-{1\over2}\log(1-x).                                  \tag{20}
\]

The inequalities \(x\le-\log(1-x)\le x/(1-x)\) give the effective bound

\[
 \boxed{
 {2\beta-1\over2(\gamma^2+\beta^2)}
 \le a_\rho\le
 {2\beta-1\over2(\gamma^2+(1-\beta)^2)}.}                     \tag{21}
\]

Uniformly in \(0<\beta<1\), as \(\gamma\to\infty\),

\[
 \boxed{
 a_\rho={2\beta-1\over2\gamma^2}+O(\gamma^{-4}).}             \tag{22}
\]

The full functional quadruple contributes to \(L_n^{<}\), once
\(|\gamma|<\sqrt n\),

\[
 Q_n(\rho)=4-4\cosh(na_\rho)\cos(n\vartheta_\rho).             \tag{23}
\]

Its activation parameter is, by (21),

\[
 {n(2\beta-1)\over2(\gamma^2+\beta^2)}
 \le na_\rho\le
 {n(2\beta-1)\over2(\gamma^2+(1-\beta)^2)}.                  \tag{24}
\]

Hence the hyperbolic modulus only starts to be large when

\[
 \gamma^2\lesssim {n(2\beta-1)\over2};                         \tag{25}
\]

in the large-height approximation. In particular, if
\(|\gamma|\ge\sqrt n\), then \(na_\rho\le1/2\) by (21). This
is a statement **per individual quadruple**: its hyperbolic factor cannot
activate exponentially outside the low block. It is not a collective
bound for the sum of the high zeros.

**Warning.** (23)--(25) describe one quadruple. They do not give a lower
bound for the growing sum of all quadruples: the phases
\(n\vartheta_\rho\) can interfere. Bombieri–Lagarias is the correct input
for asserting that, if RH fails, the incomplete block has exponential
excursions over a subsequence. That theorem is not replaced by an
unproved "dominant zero" argument.

---

## 5. Exact budget criterion for future mechanisms `[INC]`

Suppose an unconditional mechanism produces, with
\(\alpha_n\ge0\), \(E_n\ge0\),

\[
 L_n^{<}\ge-\alpha_n A_n-E_n.                                  \tag{26}
\]

From (5) and (3),

\[
 \lambda_n\ge(1-\alpha_n)A_n-E_n-C_*\sqrt n\log n.             \tag{27}
\]

Hence, to prove \(\lambda_n\ge cA_n\) via (26), it is necessary and
sufficient for this worst-case transfer that

\[
 \boxed{
 E_n+C_*\sqrt n\log n
 \le(1-c-\alpha_n)A_n.}                                       \tag{28}
\]

For the quartic margin \(c=1/4\),

\[
 \boxed{
 E_n+C_*\sqrt n\log n
 \le\left({3\over4}-\alpha_n\right)A_n.}                      \tag{29}
\]

For exact A1, if moreover only a one-sided bound
\(R_n(T_n)\le r_n^+\) is known, (7) shows that the corresponding test is

\[
 \boxed{
 E_n+C_*\sqrt n\log n+r_n^+
 \le\left({3\over4}-\alpha_n\right)A_n.}                      \tag{30}
\]

This corrects two possible false diagnoses.

1. **An error \(\gg\sqrt n\log n\) does not automatically kill a route.** If
   \(\alpha_n\le3/4-\delta\) for some \(\delta>0\), any
   \(E_n=o(A_n)=o(n\log n)\) eventually satisfies (29), even if it is much
   larger than \(\sqrt n\log n\).
2. **The scale \(\sqrt n\log n\) is indeed blocking when that is the whole
   signed gain.** If a mechanism aims to resolve the block at its
   natural scale --e.g. \(L_n^{<}\ge-O(\sqrt n\log n)\)--, an
   uncontrolled error of larger order erases exactly the information it
   claims to produce. And if \(\alpha_n=3/4\), no nonnegative error closes
   (29) without using additional sign from \(\widetilde\varepsilon_n\).

Thus the correct stop-gate is not "error larger than \(\sqrt n\log n\)" in
the abstract. It is the budget inequality (28), with the mechanism's
proportional margin written out explicitly.

---

## 6. What changes and what does not

**Unconditionally closed.** The high tail is \(A_n\) with error
\(O(\sqrt n\log n)\); the remaining block is a finite sum of
\(\asymp\sqrt n\log n\) labels; the activation scale of a quadruple is
\(na_\rho\asymp n(2\beta-1)/(2\gamma^2)\); and (28)--(30) decide whether the
precision a mechanism claims reaches the goal.

**Not closed.** No new lower bound was obtained for
\(L_n^{<}\), no collective control of the off-line phases, neither A1 nor
RH.

**Operational consequence.** Future mechanisms must state, before
starting, their pair \((\alpha_n,E_n)\) in (26). If they cannot satisfy (29),
or (30) with the tail bound they actually use, they are discarded without
developing the remaining machinery.

---

## 7. Diagnostic reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 low_zero_block_budget_check.py
```

The program checks the rational identity (19), the two bounds of (21), the
normalization of the quadruple (23), and the algebraic equivalences of
(8)/(28) on rational data. The counting and Lagarias theorems are not
"certified" by sampling: their proofs are the inputs cited above.
