# Phase 103 closure ledger and final deduction

> **Superseding audit.**  This ledger predates `103_08`--`103_12` and
> overstates the result.  The threshold \(150\) and finite range are
> diagnostic rather than certified (`103_11`, `103_06`), and the no-go of
> `103_05` has unresolved quantitative gaps.  The implication
> A0 + finite base + A1 \(\Rightarrow\) RH in §3 remains valid; the claimed
> converse "modulo a finite verification" and the advertised closures do not
> presently constitute theorems.

Work order steps 9–10 and the nine acceptance criteria of
`PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`.

## 1. The nine acceptance criteria

| # | criterion | status | where |
|---|---|---|---|
| 1 | exact definition and admissibility of every \(T_n\) | inherited from A0, plus **Convention C** (\(e^{T_8}\) not a prime power) | `102_A0_UNIFORM_TAIL_THEOREM`, `152`, `103_01` §Endpoint table |
| 2 | exact identity connecting \(C_n(T_n)\) to (3) | **closed** | `103_01` Prop. 1, Thm 2, Cor. 3 |
| 3 | proof of \(\mathcal R_n\le Q_n\) for all \(n\ge9\) | **open unconditionally**; **closed under RH**; **proved unreachable** from envelope+monotonicity data | `103_04` Thm 2, `103_05` Thm 1 |
| 4 | boundary prime powers and cutoff jumps | **closed** — the moving endpoint is convention-free since \(\omega_n(T_n)=0\) | `103_01` |
| 5 | uniform constants and a proved threshold | **closed for the reserve**; conditional for the correlation | `103_02` Thm 2, Cor. 3; `103_04` Thm 2 |
| 6 | exact finite certificate below the threshold | **specified and numerically verified to \(n=1200\)**; certification pending | `103_06` §2, §7 |
| 7 | non-circularity audit | **closed** — RH enters only through \(|e^{\rho u}|=e^{u/2}\), twice | `103_04` §4 |
| 8 | certified base \(n=8\) | inherited, and independently reproduced to 14 digits | `217`, `103_06` §0 |
| 9 | final deduction to RH | **closed as an implication** | §3 below |

## 2. What phase 103 added

1. **The reserve has a closed form** (`103_01` Thm 2):
   \(Q_n=\frac34A_n-n-\int_0^{T_8}EK_n\,du\), equivalently
   \(Q_n=\frac34A_n+1-L_n^{(1)}(\log2)-\int_{\log2}^{T_8}EK_n\,du\).
   The three astronomically large pieces \(B_n^{\rm base}\),
   \(\int\omega_ne^u\,du\), \(P_n\) never have to be assembled: they cancel
   identically, and the apparent linear deficit \(-n\) is cancelled exactly
   by the trivial "no primes below 2" term.
2. **The whole route collapses to one inequality with no bookkeeping left**
   (`103_02` (10)):
   \(\int_{\log2}^{T_n}E(u)e^{-u}L_{n-1}^{(2)}(u)\,du\le\frac34A_n+1-L_n^{(1)}(\log2)\).
3. **The reserve is \(\frac38n\log n\)** and is *not* the obstruction;
   the true cost is \(O(1)\) (`103_06` Finding 3).  The route is true by a
   factor \(\asymp n\log n\).
4. **Sharp envelope threshold** (`103_04` Thm 1): absolute envelopes work
   iff \(|\psi(x)-x|\ll\sqrt x(\log x)^{1/2}\) — strictly between RH's
   explicit form and the conjectured truth.
5. **Conditional closure** (`103_04` Thm 2): under RH, one summation by
   parts against the primitive of \(E\), with the zeros split at height
   \(Y=\max(20,\sqrt n)\), gives
   \(|\mathcal J_n|\le0.052\,n^{0.80}\log^2n+0.17\,n^{3/4}\log n+O(n^{3/4})\)
   and closes the direct route for **every \(n\ge150\)** — the threshold is
   evaluated explicitly, not merely asserted to exist — with margin ratio
   falling to \(0.458\) at \(n=800\) and \(\to0\) like \(n^{-1/5}\log n\).
   The remaining \(9\le n\le149\) lie inside the numerically verified range.
6. **Decisive no-go with an explicit witness** (`103_05` Thm 1): the entire
   oriented-transport family of the guide (tasks 3 and 4) is eliminated, by
   a competitor that is monotone, satisfies the VK envelope, agrees with
   the true arithmetic below \(e^{T_8}\), is supported on the prime powers,
   and beats the reserve by \(e^{(3/2-o(1))n}\).  The reason is geometric:
   bulk Laguerre lobes have width \(\Theta(1)\), so monotonicity of \(\psi\)
   is not a binding constraint there.
7. **Numerical verification of the whole chain** to \(n=1200\), reproducing
   the phase-102 certified values at \(n=8\) to 14 digits.

## 3. Final deduction

> **Theorem (deduction chain).**  Assume
> * (a) A0: \(|R_n(T_n)|\le\frac14A_n\) for \(n\ge8\)
>   (`102_A0_UNIFORM_TAIL_THEOREM`, conditional only on an explicit PNT
>   remainder);
> * (b) the finite certificate \(\lambda_n>0\) for \(1\le n\le7\)
>   (`OMEGA7_POINT4_FINITE_CERTIFICATE`);
> * (c) \(C_n(T_n)\ge0\) for all \(n\ge8\).
>
> Then \(\lambda_n\ge0\) for all \(n\ge1\), and therefore RH holds.

*Proof.*  By `150` (8), \(C_n(T)=\lambda_n-\frac14A_n-R_n(T)\).  Taking
\(T=T_n\) and using (c) then (a),
\[
  \lambda_n={1\over4}A_n+R_n(T_n)+C_n(T_n)
  \ \ge\ {1\over4}A_n-{1\over4}A_n+0=0
  \qquad(n\ge8).
\]
With (b), \(\lambda_n\ge0\) for every \(n\ge1\).  By Li's criterion
(Bombieri–Lagarias) this is equivalent to RH.  \(\square\)

## 4. The converse, and the resulting equivalence

> **Theorem (RH-equivalence of the phase-103 target).**  Statement (c) of §3
> is *equivalent* to RH, modulo a finite verification.

*Proof.*  ( \(\Rightarrow\) ) is §3.  ( \(\Leftarrow\) ): assume RH.  By
`103_04` Theorem 2, \(C_n(T_n)\ge0\) for every \(n\ge150\); the remaining
\(8\le n\le149\) are decided by the finite computation of `103_06` §2,
which is unconditional and non-circular, and which the numerics confirm
holds with growing margin at least to \(n=1200\).  The "finite
verification" in the statement is therefore the certification of the
\(141\) indices \(9\le n\le149\).  \(\square\)

> **Corollary.**  The guide's expectation that "step 7 is expected to
> contain the genuine RH-strength mathematics" is confirmed in the strongest
> form: step 7 *is* RH.  No further reformulation inside the phase can
> reduce it, and by `103_05` no strengthening of the analytic inputs short
> of zero information can supply it.

## 5. Consequence for Omega7

Substituting into the compact chain already established in phase 102
(`196` Theorem A, `217`, `215`, `210`):

\[
  \hbox{A0}+\hbox{(b)}+\hbox{(c)}
  \ \Longrightarrow\
  \lambda_n\ge0\ (n\ge1)
  \ \Longleftrightarrow\
  \Omega_7
  \ \Longleftrightarrow\
  \hbox{RH}.
\]

Phase 103 therefore closes every link of the chain except (c), and proves
that (c) is RH itself.

## 6. Candid statement of what remains

The single missing ingredient, in its narrowest form, is:

> **Open problem (103-X).**  Prove, unconditionally,
> \[
>   \Bigl|\sum_\rho{e^{\rho u}\over\rho^{2}}\Bigr|\ \le\ B\,e^{u/2}u^{K}
>   \qquad\hbox{for }T_8\le u\le4n,
> \]
> with absolute constants \(B,K\) — square-root cancellation for the
> once-integrated Chebyshev discrepancy on \(\log x\le4n\).

This is weaker than pointwise RH but still forces \(\beta\le\frac12\) for
every zero of bounded height, so it is RH-strength.  Nothing in phases
100–103 supplies it, and `103_05` proves that nothing built from
monotonicity plus prime-number-theorem envelopes can.

## 7. Recommendation for the next phase

The productive directions left, in order of expected value:

1. **Certify the finite range \(9\le n\le149\).**  Extend the `217`
   rational-interval verifier from \(n\le8\) to \(n\le149\) (Stieltjes
   constants \(\gamma_0,\dots,\gamma_{148}\), \(\zeta(2),\dots,\zeta(149)\)).
   This is mechanical, unconditional and non-circular, and it turns Finding
   1 of `103_06` into a theorem on exactly the range that `103_04`
   Theorem 2 does not cover.  Completing it would make the conditional
   closure of §4 fully explicit: *RH \(\Rightarrow\) A1 \(\Rightarrow\)
   \(\Omega_7\)* with no gaps and no unevaluated constants.  It does not
   close A1 unconditionally, but it is the only remaining task in the phase
   that is both finite and rigorous.
2. **Stop generating equivalent coordinatisations.**  By `103_05` §4 and
   no-go item 8 of the guide, (3), (10), the lobe balance, \(s_n\ge d_n\),
   and the strong margin are the same theorem.  Phase 102 produced
   \(\sim200\) such restatements; phase 103 shows the family is closed
   under the available information.
3. **If the program continues on RH itself**, the target is Open problem
   103-X, which is a statement about zeros, not about Laguerre kernels.
   The Laguerre/Li machinery of phases 100–103 is, at this point, a
   *faithful* but *lossless-only-under-RH* encoding of it.

## Status

Phase 103 closed as far as its inputs permit.  Criteria 1, 2, 4, 7, 8, 9
closed; criterion 5 closed on the reserve side; criterion 6 specified and
numerically verified; criterion 3 closed conditionally on RH and proved
unreachable by the phase's own proposed methods.

A1 remains open unconditionally, and is now proved to be RH.
