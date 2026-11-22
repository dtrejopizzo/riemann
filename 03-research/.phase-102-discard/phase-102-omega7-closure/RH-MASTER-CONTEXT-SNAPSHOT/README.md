# Master context of the RH program

*This folder is an earlier frozen copy of [`../RH-MASTER-CONTEXT/`](../RH-MASTER-CONTEXT/); the two differ only in the verification script under `tools/`.*

This directory freezes the comprehensive review of the program before continuing with \(\Omega_7\). It
is not a new phase and contains no claim of a proof of RH. Its function is to prevent three research
errors: counting an equivalence as progress, reusing a withdrawn claim, and re-traveling a class
already closed by a no-go.

The central verdict is:

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}
\Longleftrightarrow
\bigl[J_N(z_0)\succeq0\ \forall N\bigr]
\Longleftrightarrow
\bigl[\lambda_n\ge0\ \forall n\bigr].
\]

This chain is a correct localization of the difficulty, not a reduction of its strength. \(\Omega_7\)
remains open. The audit also forces the correction of a previous, stronger claim: not every auxiliary
piece announced as closed in paper 36 is proved with the declared scope. In particular, \(\Omega_4\)
mixes two whitenings with different domains and \(\Omega_5\) proves continuity for fixed order, but not
unconditional positivity.

There is also a correction that changes the restart. From the exact split
\(\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}\), \(\Omega_7\) is equivalent to

\[
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\qquad(n\ge1),
\]

not to \(|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}\). The absolute domination is a stronger
sufficient condition and cannot even be the declared equivalence at \(n=1\). For this reason the
recommended frontier becomes a one-sided inequality that preserves the signed cancellation.

The audit also corrects the formula that should start that frontier: the printed integration by parts
flips the sign and omits the boundary term \(-n\). With
\(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), the valid identity is

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

Therefore no continuation should reuse the previous version without repair.

## Reading order

1. [`00_SCOPE_AND_METHOD.md`](00_SCOPE_AND_METHOD.md): corpus, protocol and meaning of the labels.
2. `MASTER_CONTEXT.md`: self-contained synthesis of the full path and current mathematical status.
3. `PAPER36_AUDIT.md`: logical column, confirmed results and necessary repairs.
4. `RH1_RH9_AUDIT.md`: balance of the nine exploratory programs.
5. `PHASES_AUDIT.md`: tour of all phases, without counting reparametrizations as new closures.
6. `NO_GO_AND_RETRACTIONS.md`: register of discarded routes, exact scope and precedence of
   corrections.
7. `LIVE_FRONTIER_AND_RESTART_PLAN.md`: admission criterion and restart plan centered on the
   RH-strength-carrying step.
8. `COVERAGE_INDEX.md`: coverage check and context size.

The files in [`fragments/`](fragments/) preserve the block audits that support the synthesis. They are
traceability evidence; in case of any discrepancy, a later mathematical correction that exhibits the
exact step prevails.
The folder [`tools/`](tools/) holds the interval-arithmetic verification script for the finite
certificate of point 4 of \(\Omega_7\).

## Binding labels

| Label | Meaning |
|---|---|
| **PROVED** | The conclusion follows from the written hypotheses. The scope may be finite or restricted. |
| **CONDITIONAL** | At least one hypothesis used by the conclusion remains to be proved. |
| **NUMERICAL** | Evidence for fixed cuts, data and precision; not a limit. |
| **REFUTED** | The concrete mechanism fails or contains an identified error. |
| **RH-STRENGTH** | Proving the statement would solve RH under already-established transfers. It cannot be used as an auxiliary lemma. |
| **OPEN** | The statement is well typed and still has neither a proof nor a refutation. |

A proved finite identity does not automatically inherit a cofinal conclusion. An RH-strength condition
is not a small gap. A no-go only closes the class of arguments that its hypotheses actually cover.
