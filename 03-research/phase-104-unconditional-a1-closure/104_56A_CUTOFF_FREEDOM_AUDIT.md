# 104_56A — Audit of cutoff freedom and strict fourth margin

**Object.** Audit the proposal to replace the uniform gate

\[
 {2002\over501}\lambda_n-A_n\ge0
\]

by the strict pointwise gate

\[
 \boxed{\;4\lambda_n>A_n.\;}                         \tag{1}
\]

The verdict has two parts. The improvement of A0 holds for **every**
subsequent cutoff, and (1) allows existentially choosing a cutoff that
satisfies A1. But that cutoff depends on the slack
\(\delta_n=\lambda_n-A_n/4\). Therefore the reduction is correct as a
conditional implication, but does not supply an a priori cutoff with which
to prove the slack itself.

## 1. Notation without the \(B_n\) collision

Set

\[
 A_n=\lambda_n^{\rm arch}>0,\qquad
 \delta_n:=\lambda_n-{A_n\over4},\qquad
 R_n(T):=-\int_T^\infty E(u)K_n(u)\,du,
\]

\[
 C_n(T)=\lambda_n-{A_n\over4}-R_n(T)
       =\delta_n-R_n(T).                              \tag{2}
\]

In `102_A0_UNIFORM_TAIL_THEOREM.md` the letter \(B_n\) denotes a positive
lower bound for \(A_n\); in later documents it sometimes denotes
\(A_n-\lambda_n\). To avoid that collision we will write here
\(b_n^{\rm A0}\), with

\[
 0<b_n^{\rm A0}\le A_n.                              \tag{3}
\]

Let \(T_n^0\) be any cutoff for which condition (B) of A0 holds:

\[
 \eta(u)\ge(n+1)\log(1+u)+
 \log {12An^2\over b_n^{\rm A0}}
 \qquad(u\ge T_n^0).                                \tag{4}
\]

## 2. Cofinal lemma of A0

**Lemma 2.1.** For every \(T\ge T_n^0\),

\[
 \boxed{
 |R_n(T)|\le {b_n^{\rm A0}\over4(1+T)}
             \le {A_n\over4(1+T)}.}                 \tag{5}
\]

**Proof.** If (4) holds for every \(u\ge T_n^0\), it holds a fortiori
for every \(u\ge T\) when \(T\ge T_n^0\). We repeat the last line of
the proof of A0 starting at \(T\):

\[
\begin{aligned}
 |R_n(T)|
 &\le3An^2\int_T^\infty(1+u)^{n-1}e^{-\eta(u)}\,du\\
 &\le {b_n^{\rm A0}\over4}
       \int_T^\infty(1+u)^{-2}\,du
  ={b_n^{\rm A0}\over4(1+T)}.
\end{aligned}
\]

The second inequality in (5) is (3). \(\square\)

Thus the correct statement is: **enlarging the cutoff improves the
absolute envelope of A0**. It does not imply that \(C_n(T)\) is
monotone; indeed

\[
 C_n'(T)=-E(T)K_n(T)
\]

has no known sign (`153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md`).

The same conclusion can be read directly in `104_01`: its condition
(B\(_\theta\)) is required for every \(u\ge T\), so every larger cutoff
remains admissible. For \(\theta=1/4\), that normalization corresponds
to taking \(b_n^{\rm A0}=A_n\).

## 3. Adapted cutoff theorem

**Theorem 3.1.** Suppose \(\delta_n>0\). Every choice satisfying

\[
 T\ge T_n^0,\qquad 1+T>{A_n\over4\delta_n}           \tag{6}
\]

satisfies \(C_n(T)>0\), and therefore A1 at that cutoff.

In particular the following explicit choice, as a real number, works

\[
 \boxed{
 \widetilde T_n:=\max\left\{T_n^0,{A_n\over4\delta_n}\right\}.} \tag{7}
\]

**Proof.** By (2), (5) and (6),

\[
 C_n(T)\ge\delta_n-|R_n(T)|
 \ge\delta_n-{A_n\over4(1+T)}>0.                    \tag{8}
\]

The collapse of A1 is proved for every admissible A0 cutoff, so (8) is
exactly A1\(_n(T)\). \(\square\)

There is no hidden restriction forcing use of the minimum
\(T_n(1/4)\). Theorem A0 says "if \(T_n\) is chosen so that", and the
collapse of A1 holds for every A0 cutoff. There is also no moving-endpoint
problem: the moving endpoint charge is zero because \(\omega_n(T_n)=0\).
If one wishes to preserve a strictly increasing sequence, define
recursively

\[
 \widetilde T_n=max\left\{T_n^0,\widetilde T_{n-1}+1,
                      {A_n\over4\delta_n}\right\};             \tag{9}
\]

Lemma 2.1 still applies.

**Corollary 3.2 (exact quantifiers).**

\[
 \left[\forall n\ge150:\ 4\lambda_n>A_n\right]
 \Longrightarrow
 \left[\exists(\widetilde T_n)_{n\ge150}\quad
       \forall n\ge150:\ {\rm A1}_n(\widetilde T_n)\right]. \tag{10}
\]

Together with the certificates \(1\le n\le149\), either side of the
implication leads to \(\lambda_n>0\) for all \(n\), and by Li to RH.
In fact the detour through A1 is not logically necessary once the
left-hand side is proved: \(A_n>0\) and \(4\lambda_n>A_n\) already give
\(\lambda_n>0\).

## 4. What happens with a cutoff fixed in advance

If a **prescribed** cutoff \(T_n^0\) is kept, A0\(^+\) only supplies
the sufficient condition

\[
 \lambda_n\ge
 \left({1\over4}+{1\over4(1+T_n^0)}\right)A_n
 ={T_n^0+2\over4(T_n^0+1)}A_n.                    \tag{11}
\]

Equivalently,

\[
 r\lambda_n-A_n\ge0,\qquad
 r\le r_{\max}(T_n^0):={4(1+T_n^0)\over T_n^0+2}. \tag{12}
\]

Therefore `104_23` is correct, but \(2002/501\) is only the best
**uniform constant deduced from the raw floor** \(T_n^0\ge1000\). It is
not the best constant of index-by-index computed cutoffs. With the
current version of `theta_family_check.py` one obtains, diagnostically,

\[
 T_{1000}(1/4)\simeq6.9160\times10^8,\qquad
 {1\over r_{\max}}\simeq0.2500000003615,
\]

and the corresponding A0 overcost is approximately
\(8.40\times10^{-7}\). These figures are floating point and do not
enter the theorem.

Three objects must be distinguished:

1. the exact condition at a fixed cutoff is
   \(C_n(T)\ge0\iff\delta_n\ge R_n(T)\);
2. condition (11) is a signless sufficient condition obtained by
   substituting \(R_n(T)\) with \(|R_n(T)|\);
3. with an adapted cutoff and \(\delta_n>0\), Lemma 2.1 lets that
   sufficient condition be made true by moving \(T\) toward infinity.

For this reason it is not accurate to call
\(A_n-\lambda_n<3A_n/4\) "the exact A1": it is the **cofinal sufficient
threshold without sign information**. A1 may hold at a specific cutoff
even if that threshold fails, for example if \(R_n(T)<0\) compensates
the deficit.

## 5. Circularity audit

Choice (7) is not circular within implication (10): under the
hypothesis \(\delta_n>0\), the number \(\widetilde T_n\) is well
defined and the proof is valid. A choice may depend on \(n\); A0 never
requires a cutoff uniform in \(n\).

It **would** be circular to use (7) as a **mechanism to prove**
\(\delta_n>0\):

- (7) presupposes the sign and size of the very slack that remains to
  be proved;
- without an independent lower bound for \(\delta_n\), it does not
  produce a numerical a priori cutoff derived solely from PNT;
- proving A1 at that cutoff does not back-prove
  \(4\lambda_n>A_n\): A1+A0 only yields \(\lambda_n\ge0\).

In summary, cutoff freedom correctly eliminates the fixed proportional
slack of `104_23`, but does not eliminate the RH-strength theorem. It
replaces it with the strict gate

\[
 \boxed{
 4\lambda_n>A_n\quad(n\ge150)
 \quad\Longleftrightarrow\quad
 A_n-\lambda_n<{3\over4}A_n\quad(n\ge150),}       \tag{13}
\]

as a cofinal sufficient condition. The novelty is quantitative: a
uniform proportional slack is no longer needed. The central logical
difficulty remains.

## 6. Verdict

| Proposed statement | Verdict |
|---|---|
| A0\(^+\) holds for every \(T\ge T_n^0\) | **Correct** |
| The cutoff may depend on \(n\) | **Correct; already allowed** |
| \(4\lambda_n>A_n\) allows choosing a cutoff that closes A1 | **Correct, existentially** |
| That cutoff can be fixed from PNT without knowing the slack | **Not proved** |
| \(4\lambda_n>A_n\) proves RH together with the finite certificates | **Correct, even without going through A1** |
| \(B_n<3A_n/4\) is equivalent to A1 at a fixed canonical cutoff | **False in general** |
| \(2002/501\) is the intrinsic front | **False; it is the uniform front of the floor \(T\ge1000\)** |

## Status

- **Proved:** Lemma 2.1, Theorem 3.1 and Corollary 3.2.
- **Correction accepted:** the proportional margin \(A_n/1001\) is not
  intrinsic if an adapted cutoff is allowed.
- **Binding caveat:** the adaptation uses the RH-strength slack and
  does not constitute a proof of it.
- **A1/RH:** remain open.
