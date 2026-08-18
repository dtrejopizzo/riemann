# Adversarial status correction

> **Later effectivity update.**  Items below describing the Laguerre
> constants as unavailable are superseded by `103_22`, which proves both
> interior integral budgets with explicit (very large) constants for every
> \(N\ge1\).  The warnings about the threshold 150, numerical certification,
> `103_05`, and the unconditional RH gate remain in force.

## Purpose

This note is the controlling status statement for `103_04`--`103_07`.
It removes claims that became untenable after the audits in `103_08`--
`103_12`.  It adds no hypothesis and proves no version of RH.

## 1. What remains proved

The algebraic reduction is exact:
\[
 C_n(T_n)\ge0
 \quad\Longleftrightarrow\quad
 \int_{\log2}^{T_n}(\psi(e^u)-e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
 \le {3\over4}A_n+1-L_n^{(1)}(\log2).                 \tag{1}
\]
The endpoint at \(T_n\) is convention-free, and the fixed interval
\([\log2,T_8]\) has the exact finite collapse proved in `103_12`.
The reserve has leading scale \(\frac38n\log n\), subject to the effectivity
qualification recorded in `103_08` and `103_11`.

The outer Laguerre tail is controlled rigorously by `103_09`, and the
interior powers
\[
 I_2(\log2;4N)\ll N^{3/4},\qquad
 I_3(\log2;4N)\ll N^{5/4}
\]
follow qualitatively from the uniform estimate used in `103_10`.  The
hidden comparison constants have not been evaluated.

Finally, if (1) is proved for every \(n\ge8\), the inherited A0 estimate and
the finite base imply all Li coefficients are nonnegative, hence RH.  This
is an implication, not a proof of its premise.

## 2. Claims withdrawn

1. **The threshold 150.**  The tables in `103_04` and `103_06` are
   diagnostics.  The source of the interior Laguerre estimate supplies no
   numerical constants for \(\alpha=2,3\), so no rigorous crossing at 150
   has been established.
2. **A certified range through 1200.**  The values were computed
   numerically.  The Cauchy extractor additionally requires a finite
   zero-free certificate for its transformed disk; `103_06` now states this
   precondition.  No interval certificate through 1200 is present.
3. **Theorem 1 of `103_05`.**  A transition occupying a fixed fraction of
   a lobe's width need not carry the same fraction of the mass
   \(W|K_n|\).  The missing local mass estimate is not supplied, the final
   exponential budget is empirical/asymptotic in the cited document, and
   the nearest logarithm of an integer is not necessarily a prime power.
   Thus the advertised supported competitor and the universal no-go are not
   theorems as written.
4. **The converse RH \(\Rightarrow\) A1 with a finite check.**  A qualitative
   eventual implication under RH is available after `103_09`--`103_10`, but
   the effective threshold and its complementary certified range are both
   missing.  The converse claimed in `103_07` is therefore not closed.

## 3. Exact unconditional gate

Let
\[
 F(u)=\sum_\rho {e^{\rho u}\over\rho^2}.
\]
`103_11` proves, without assuming RH,
\[
 RH\quad\Longleftrightarrow\quad
 F(u)=O\!\left(e^{u/2}(1+u)^A\right)
 \quad\text{for some fixed }A.                         \tag{2}
\]
Therefore (2) cannot serve as an intermediate unconditional estimate: it is
already a complete RH criterion.  A successful Phase-103 proof must instead
derive (1) for the particular Laguerre family by a new arithmetic
cancellation or positivity mechanism, and must verify that the mechanism
does not assume (2), Li positivity, zero-line localization, or an equivalent
zero-free analytic continuation.

## Status

The exact reduction, fixed-window cancellation, qualitative Laguerre
budgets, outer tail, and the equivalence (2) are rigorous.  The weighted A1
inequality remains unproved unconditionally.  No document in Phase 103 may
currently be cited as a proof of RH.
