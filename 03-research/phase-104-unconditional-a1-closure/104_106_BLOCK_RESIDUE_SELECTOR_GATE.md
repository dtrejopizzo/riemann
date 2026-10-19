# 104_106 — Block averages, residues, and the exact selector gate

**Question.** Can the block relaxation of `104_67` be combined with the
residue formula of `104_33`–`104_41`, by averaging the transport defect
over consecutive degrees?

**Result.** The combination has a closed form, but a signed linear
average does not produce a good block. For any finite filter of degrees,
each right zero is transformed by the same filter polynomial evaluated at
\(w_\rho\) and \(w_\rho^{-1}\). In particular, box, triangular Cesàro, and
Fejér averaging all preserve the exterior mode; they only change its
phase and amplitude.

The correct operation for the upper barrier of `104_67` is nonlinear:
the positive part of \((-\mathscr R_n)\), or equivalently a supremum over
**all** block selectors. The exact criterion is proved:

\[
 \mathrm {RH}\quad\Longleftrightarrow\quad
 {e^{-\sqrt{M_L}}\over L}
 \sum_{n=L^2}^{L^2+L-1}(-\mathscr R_n)_+\longrightarrow0,
 \qquad M_L=L^2+L-1.                                    \tag{1}
\]

Here \(\mathscr R_n\) is the signed sum of interior residues from
`104_41`, not an estimated remainder. Equivalence (1) precisely localizes
the target that an arithmetic estimate would have to bound, but it does
not bound it for the real weights \(\Lambda(m)\). The rational quartet
\(w=i/2\) demonstrates exactly that replacing the positive part by a
signed average is invalid even in arbitrarily distant blocks.

This document does not prove (1) arithmetically, nor A1, nor RH.

---

## 1. The exact block filter

For a nontrivial zero \(\rho\) with \(\Re\rho>1/2\), set

\[
 w_\rho=1-{1\over\rho},\qquad |w_\rho|<1.
\]

The transport defect of `104_33`, summed over both signs of the
ordinate, is

\[
 \mathscr R_n:=
 \sum_{\Re\rho>1/2}
 {m_\rho\,\mathcal F_n(w_\rho)\over\rho(\rho-1)}.
                                                               \tag{2}
\]

The sum includes conjugates and is real. The elementary identity already
used in `104_33` is

\[
 \boxed{
 {\mathcal F_n(w_\rho)\over\rho(\rho-1)}
 =w_\rho^n+w_\rho^{-n}-2.}                              \tag{3}
\]

Now let \(I=\{N,N+1,\ldots,N+L-1\}\), let
\(a_0,\ldots,a_{L-1}\in\mathbb R\), and define

\[
 A(z)=\sum_{j=0}^{L-1}a_jz^j,\qquad A(1)=\sum_ja_j.       \tag{4}
\]

Since the filter is finite and the residue series converges absolutely
at each fixed degree, (3) can be summed term by term.

**Lemma 1.1 (filter–residue identity).** One has

\[
 \boxed{
 \sum_{j=0}^{L-1}a_j\mathscr R_{N+j}
 =\sum_{\Re\rho>1/2}m_\rho
 \left\{
 w_\rho^N A(w_\rho)
 +w_\rho^{-N}A(w_\rho^{-1})-2A(1)
 \right\}.}                                             \tag{5}
\]

No new sign appears upon averaging: the growing mode
\(w_\rho^{-N}\) is still present and is multiplied by
\(A(w_\rho^{-1})\).

### 1.1 Box, Cesàro, and Fejér

Write

\[
 G_L(z)={1-z^L\over L(1-z)}={1\over L}\sum_{j=0}^{L-1}z^j. \tag{6}
\]

The box average of the contribution (3) of a zero is

\[
 \boxed{
 w^NG_L(w)+w^{-N}G_L(w^{-1})-2.}                         \tag{7}
\]

For the one-sided triangular average, with weights
\(2(L-j)/[L(L+1)]\), the polynomial is

\[
 T_L(z)={2\over L(L+1)}
 {L-(L+1)z+z^{L+1}\over(1-z)^2},                         \tag{8}
\]

and the answer is \(w^NT_L(w)+w^{-N}T_L(w^{-1})-2\).

Finally, if \(N\ge L\), the symmetric Fejér average uses

\[
 K_L(z)={1\over L^2}\sum_{|j|<L}(L-|j|)z^j
 ={\mathcal F_L(z)\over L^2}=K_L(z^{-1}).                \tag{9}
\]

Hence

\[
 \boxed{
 \sum_{|j|<L}{L-|j|\over L^2}
 \{w^{N+j}+w^{-N-j}-2\}
 =K_L(w)(w^N+w^{-N})-2.}                                 \tag{10}
\]

Non-negativity of \(K_L(e^{i\theta})\) only holds on the circle. For
\(|w|\ne1\), \(K_L(w)\) is generally complex and does not orient (10).

---

## 2. The boundary part is subexponential

Let \(\lambda_n^{\rm crit}\) be the contribution of the zeros located on
the critical line, grouped by conjugation:

\[
 \lambda_n^{\rm crit}
 =2\sum_{\substack{\rho=1/2+i\gamma\\\gamma>0}}
 m_\rho\{1-\cos(n\theta_\rho)\},
 \qquad
 1-{1\over\rho}=e^{i\theta_\rho}.                       \tag{11}
\]

Splitting Li's formula into critical orbits and exterior quartets,
(3) gives the exact identity

\[
 \boxed{\lambda_n=\lambda_n^{\rm crit}-\mathscr R_n.}  \tag{12}
\]

Moreover,

\[
 \boxed{0\le\lambda_n^{\rm crit}\ll n\log(n+2).}       \tag{13}
\]

Indeed, the critical zeros with \(\gamma\le n\) contribute at most
four each and \(N(n)\ll n\log(n+2)\). For \(\gamma>n\),

\[
 |\theta_\rho|=2\arctan{1\over2\gamma}\le{1\over\gamma},
 \qquad
 2\{1-\cos(n\theta_\rho)\}\le {n^2\over\gamma^2}.
\]

Riemann–von Mangoldt partial summation gives

\[
 \sum_{\gamma>n}{m_\rho\over\gamma^2}
 \ll {\log(n+2)\over n},
\]

which proves (13). Thus every positive exponential growth of
\(\lambda_n\) sits in the negative part of \(\mathscr R_n\); the critical
boundary can neither produce nor cancel it.

---

## 3. What average would actually suffice

The positive part has the exact finite duality

\[
 \boxed{
 \sum_{j=0}^{L-1}(-\mathscr R_{N+j})_+
 =\sup_{0\le a_j\le1}
 \left\{-\sum_{j=0}^{L-1}a_j\mathscr R_{N+j}\right\}.}   \tag{14}
\]

Inserting (5), the right-hand side is a supremum over all selector
polynomials \(A(z)=\sum a_jz^j\), not the evaluation of a single box or
Fejér polynomial. Similarly,

\[
 \max_{0\le j<L}(-\mathscr R_{N+j})
 =\sup_{\substack{a_j\ge0\\\sum a_j=1}}
 \left\{-\sum_ja_j\mathscr R_{N+j}\right\}.             \tag{15}
\]

By (12)–(13), a local certificate that produces a complete block of the
upper barrier of `104_67` is

\[
 \boxed{
 \sum_{n=N}^{N+L-1}(-\mathscr R_n)_+
 \le {1\over2}e^{\sqrt N}.}                              \tag{16}
\]

Indeed, let \(M=N+L-1\) and suppose
\(M\log(M+2)=o(e^{\sqrt N})\). For \(N\) sufficiently large,
\(\lambda_n^{\rm crit}\le e^{\sqrt N}/2\) throughout the block. The bound
on the sum of positive parts in (16) implies, in particular, that each
summand is at most \(e^{\sqrt N}/2\). Then (12) gives
\(\lambda_n\le e^{\sqrt n}\) degree by degree. The hypothesis on \(M\)
holds, in particular, for \(N=L^2\) and length \(L\).

The weakest formulation that still detects every exterior zero is (1).

**Theorem 3.1 (positive-block criterion).** With

\[
 I_L=\{L^2,\ldots,L^2+L-1\},\qquad M_L=L^2+L-1,
\]

equivalence (1) holds. More precisely, if RH is false, the left-hand
side of (1) tends to \(+\infty\).

*Proof.* Under RH there are no zeros with \(\Re\rho>1/2\), so
\(\mathscr R_n=0\) for every \(n\).

If RH is false, Theorem 1.1 of `104_67` provides \(c>0\), \(R>1\),
and a syndetic set \(D_+\) such that

\[
 \lambda_n\ge cR^n\qquad(n\in D_+)
\]

from some fixed index on. By (12)–(13), shrinking \(c\) if needed,

\[
 (-\mathscr R_n)_+\ge {c\over2}R^n\qquad(n\in D_+).      \tag{17}
\]

Let \(G\) be a syndeticity gap. For \(L\ge G\), the last \(G\)
places of \(I_L\) contain a \(d_L\in D_+\), so that

\[
 {e^{-\sqrt{M_L}}\over L}
 \sum_{n\in I_L}(-\mathscr R_n)_+
 \ge {c\over2L}R^{M_L-G}e^{-\sqrt{M_L}}\longrightarrow\infty.
                                                               \tag{18}
\]

This proves the dichotomy. \(\square\)

For a zero-logarithmic-density exception, it suffices, by the same
reasoning, to prove

\[
 {1\over\log X}\sum_{n\le X}
 {(-\mathscr R_n)_+\over n e^{\sqrt n}}\longrightarrow0. \tag{19}
\]

Markov's inequality applied to (19) shows that
\(\{n:(-\mathscr R_n)_+>e^{\sqrt n}/2\}\) has upper logarithmic density
zero; (12)–(13) and `104_67` then close RH. Under non-RH, (17)
proves that the term in (19) not only fails to tend to zero, but is
unbounded.

---

## 4. Why the signed average is not enough

Consider the rational quartet of `104_41`, parametrized by

\[
 w={i\over2},\qquad
 \rho={1\over1-w}={4+2i\over5}.
\]

Its contribution to the Li coefficient is

\[
 q_n=4-2\Re(w^n+w^{-n})=-2\Re\{w^n+w^{-n}-2\}.           \tag{20}
\]

For \(N\equiv2\pmod4\),

\[
 q_N=4+2(2^N+2^{-N})>2^{N+1},                            \tag{21}
\]

but the box over four degrees satisfies

\[
 \boxed{
 \sum_{j=0}^3q_{N+j}
 =16-6\,2^N+{3\over2}\,2^{-N}<0
 \qquad(N\ge2, N\equiv2\!\!\pmod4).}                 \tag{22}
\]

So there are arbitrarily distant blocks whose **signed average**
satisfies an upper bound that is even negative, although the first
degree of the same block has an exponential positive excursion. The
average has not produced a good block; the bad degree was paid for by an
excursion of the opposite sign.

This phenomenon is not special to the box filter. For any nonzero finite
filter with non-negative real weights, let \(j_*\) be the largest index
with \(a_{j_*}>0\). If \(w=re^{i\theta}\) and \(r\downarrow0\), the
dominant term of (5) is

\[
 a_{j_*}r^{-N-j_*}e^{-i(N+j_*)\theta}.                   \tag{23}
\]

Choosing two non-real angles with cosines of opposite sign, (23) takes
both signs and dominates all the other terms. Both points correspond to
zeros with \(\Re\rho>1/2\). Hence no fixed linear filter has a universal
one-sided orientation over exterior quartets. Box, Cesàro, and Fejér are
no exceptions.

This falsifier does not preserve the exact Euler product of \(\zeta\).
Its role is logical: it proves that the step "small signed average
\(\Rightarrow\) good block" is false before using arithmetic. A specific
proof for the real weights must control (14), not merely (5) for a fixed
selector.

---

## 5. Consequence for the `104_41` homotopy

In the Euler half-plane,

\[
 |\mathcal B_{n,a}|\le3n\qquad(a\ge4).
\]

By linearity, for any selector \(0\le a_j\le1\),

\[
 \left|\sum_ja_j\mathcal B_{N+j,a}\right|
 \le3\sum_ja_j(N+j).                                    \tag{24}
\]

Transporting \(a\downarrow1\), the defect is exactly the right-hand side
of (5). To deduce (14) one would have to transport (24)
**uniformly over the entire cube** \([0,1]^L\). The extremal selector
adapts to the signs of the residues; a single box/Fejér filter does not
control it.

This is the precise combination of `104_33`, `104_41`, and `104_67`:

* the boundary contributes only \(O(n\log n)\);
* the signed sum of residues has the filtered formula (5);
* the block relaxation allows replacing control of every degree with
  (1), (16), or (19);
* but any of those targets requires the positive part, equivalent to the
  selector supremum (14).

No inference remains from a linear average. The missing arithmetic
theorem is a uniform bound on (14) for the residues produced by the
ordinary weights \(\Lambda(m)\).

---

## 6. Verdict

**Proved:** the exact filter identity (5); the box, Cesàro, and Fejér
formulas (7)–(10); the decomposition
\(\lambda_n=\lambda_n^{\rm crit}-\mathscr R_n\) with
\(0\le\lambda_n^{\rm crit}\ll n\log n\); the selector duality
(14)–(15); the deterministic criterion (1); and the rational falsifier
(21)–(22).

**Gain:** the proposal of averaging the defect is now split into two
objects that must not be confused. The signed average is a single filter
and is not enough. The average of the positive part is equivalent to RH
and admits the exact variational formula (14)–(5).

**Ruled out:** concluding complete blocks or a zero-density exception
from a box, Cesàro, or Fejér signed average.

**Not proved:** an arithmetic bound for the supremum (14), (1), A1, or
RH.

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 block_residue_selector_gate_check.py
```

The checker uses `Fraction` and Gaussian rationals. It verifies (3), (5),
(7)–(10), the finite duality (14)–(15), and the falsifier (21)–(22) over
a family of arbitrarily distant blocks. It does not certify the
arithmetic limit (1).
</content>
