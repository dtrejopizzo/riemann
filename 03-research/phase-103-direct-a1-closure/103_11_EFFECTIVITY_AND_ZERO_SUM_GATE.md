# Effectivity audit and the exact zero-sum gate

> **Later update.**  The source audit in §1 remains correct, but `103_22`
> subsequently supplies different, self-contained explicit constants for
> the two required Laguerre integrals.  This removes that analytic
> effectivity gap; it does not prove the diagnostic threshold 150 and does
> not alter the RH-equivalent zero-sum gate in §2.

This note records two facts needed to prevent the conditional argument in
`103_04` from being advertised as an effective or unconditional theorem.

> **Update.** `103_22` subsequently obtains explicit (very large) constants
> for the two integral budgets by a direct Bessel--Volterra and energy
> argument.  The audit in this section remains valid: those constants do not
> come from the cited pointwise theorem (1), and they do not validate the
> separate finite threshold \(150\).  Section 2, the RH-equivalent zero-sum
> gate, is unchanged.

## 1. The constants in `103_10` are not supplied by the cited lemma

Let
\[
 I_\alpha(a;N)=\int_a^{4N}e^{-u/2}|L_N^{(\alpha)}(u)|\,du,
 \qquad a=\log 2.
\]
The calculation in `103_10` is valid if one is given a numerical constant
\(A_\alpha\) in
\[
 e^{-u/2}|L_N^{(\alpha)}(u)|\le A_\alpha N^{\alpha/2}
 (N^{-1}+u)^{-\alpha/2-1/4}
 (N^{1/3}+|u-4N|)^{-1/4}\Phi_N(u).                 \tag{1}
\]
It then gives, with \(p_\alpha=\alpha/2+1/4\) and
\(B=(4/3)3^{3/4}\),
\[
 I_\alpha(a;N)\le A_\alpha\left{
 {a^{1-p_\alpha}\over2^{1/4}(p_\alpha-1)}
 +B2^{-p_\alpha}\right}N^{\alpha/2-1/4}.        \tag{2}
\]

We checked the actual statement of Shi--Li, Lemma 2.2.  After cancelling
their factors \(u^{-\alpha/2}\) and \(u^{\alpha/2}\), its powers agree with
(1).  However, the comparison is written with \(\lesssim\); the paper's
convention explicitly says that the hidden constant may depend on fixed
parameters.  No value for it is stated or traced through the cited papers.
Thus (2) is an explicit formula **conditional on** \(A_\alpha\), not a
numerical estimate for \(C_2,C_3\).

Two proposed replacements do not presently repair this:

* Borwein--Borwein--Crandall, *Effective Laguerre Asymptotics*, treats the
  fixed-parameter subexponential regime described by
  \(L_n^{(-a)}(-z)\) with fixed \((a,z)\).  It is not a uniform estimate in
  the oscillatory/turning-point range \(u\asymp N\) used in (1).
* Krasikov's *Inequalities for orthonormal Laguerre polynomials* contains
  genuinely explicit oscillatory estimates, but its advertised global
  theorem assumes \(\alpha\ge24\).  That hypothesis does not include the
  required \(\alpha=2,3\).  No constant from that theorem may therefore be
  substituted into (2).

Consequently no numerical threshold (in particular, not \(150\)) follows
from the cited material.  Even a valid numerical pair \(A_2,A_3\) would not
alone prove such a threshold: one must also make effective the low-zero
sum, the tail \(\sum_{|\gamma|>Y}|\rho|^{-2}\), the elementary term, the
outer Laguerre tail, and a lower bound for the exact reserve \(q(n)\), and
then certify the remaining finite indices.

There is a useful fully explicit but weaker fallback.  Laguerre
orthogonality and Cauchy--Schwarz give, for every \(\alpha>1\),
\[
 I_\alpha(a;N)
 \le \left({\Gamma(N+\alpha+1)\over N!}
 {a^{1-\alpha}\over\alpha-1}\right)^{1/2}.        \tag{3}
\]
This is \(O(N^{\alpha/2})\), not the needed
\(O(N^{\alpha/2-1/4})\).  Formula (3) proves that the missing quarter-power
is exactly the oscillatory input; it cannot be manufactured merely by
making the orthogonality argument effective.

## 2. The proposed uniform zero-sum bound is equivalent to RH

Zeros below are counted with multiplicity, and
\[
 F(u)=\sum_\rho {e^{\rho u}\over\rho^2},\qquad u\ge0.                \tag{4}
\]
The series is absolutely and locally uniformly convergent, since
\(0<\Re\rho<1\) and \(\sum_\rho|\rho|^{-2}<\infty\).

> **Theorem.** The following are equivalent.
>
> 1. RH holds.
> 2. \(F(u)=O(e^{u/2})\) as \(u\to\infty\).
> 3. For some fixed \(A\ge0\),
>    \(F(u)=O(e^{u/2}(1+u)^A)\) as \(u\to\infty\).

*Proof.*  Under RH, absolute convergence immediately gives
\[
|F(u)|\le e^{u/2}\sum_\rho|\rho|^{-2},
\]
so theorem item 1 implies item 2, and item 2 trivially implies item 3.

Assume (3).  Its Laplace transform
\[
 H(s)=\int_0^\infty e^{-su}F(u)\,du                       \tag{5}
\]
is analytic for \(\Re s>1/2\).  For \(\Re s>1\), absolute convergence
permits termwise integration and gives
\[
 H(s)=G(s):=\sum_\rho {1\over\rho^2(s-\rho)}.             \tag{6}
\]
Indeed, if \(\sigma=\Re s>1\), then
\[
 \sum_\rho\int_0^\infty
 \left|{e^{-(s-\rho)u}\over\rho^2}\right|du
 \le {1\over\sigma-1}\sum_\rho|\rho|^{-2}<\infty.
\]
The series defining \(G\) converges normally on compact sets avoiding the
zeros (its tail is \(O(\sum|\rho|^{-3})\)); hence it is meromorphic, with
residue \(m/\rho_0^2\ne0\) at a zero \(\rho_0\) of multiplicity \(m\).
By the identity theorem, (6) continues from \(\Re s>1\) throughout
\(\Re s>1/2\) away from those poles.  But (5) is analytic on the whole
half-plane.  A zero \(\rho_0\) with \(\Re\rho_0>1/2\) would therefore make
the right side have a nonremovable pole where the left side is analytic,
a contradiction.  Thus every zero has \(\Re\rho\le1/2\).  The functional
equation symmetry \(\rho\mapsto1-\overline\rho\) gives the reverse
inequality, and RH follows. \(\square\)

The same proof applies if the bound is only asserted for all sufficiently
large \(u\): the omitted compact interval contributes an entire function
to (5).  It also shows why cancellation among different zeros cannot hide
an off-line zero in such a uniform estimate: the Laplace transform
separates it as a pole with nonzero residue.

## 3. Precise consequence for Phase 103

The estimate
\[
 \left|\sum_\rho e^{\rho u}/\rho^2\right|
 \ll e^{u/2}\operatorname{poly}(u)                         \tag{7}
\]
uniformly on expanding intervals \(0\le u\le4n\), with a constant and a
fixed polynomial independent of \(n\), covers every \(u\ge0\).  By the
theorem it is exactly an RH criterion.  It cannot be obtained from the
known zero-free region or zero-density estimates without proving RH.

This does **not** prove that the narrower Laguerre-weighted inequalities
needed for A1 are logically equivalent to the pointwise statement (7).
The latter is a sufficient input used by the integration-by-parts proof;
the former could exploit cancellation against the particular kernels.
However, the project's claimed implication A1 \(\Rightarrow\) Li
positivity \(\Rightarrow\) RH means that a uniform unconditional proof of
those weighted inequalities would itself prove RH.  Thus the candid open
gate is not an untracked constant: it is the construction of a new
RH-proving cancellation or positivity mechanism for the actual weighted
zero/prime sum.
