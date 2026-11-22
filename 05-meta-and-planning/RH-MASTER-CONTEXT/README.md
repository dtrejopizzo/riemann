# Master context of the RH program

This directory freezes the comprehensive review of the program carried out before continuing with \(\Omega_7\). It is not a new phase and contains no claim of a proof of RH. Its purpose is to prevent three research errors: counting an equivalence as progress, reusing a withdrawn claim, and walking again through a class already closed by a no-go.

The central finding is:

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}
\Longleftrightarrow
\bigl[J_N(z_0)\succeq0\ \forall N\bigr]
\Longleftrightarrow
\bigl[\lambda_n\ge0\ \forall n\bigr].
\]

This chain correctly locates the difficulty; it does not reduce its strength. \(\Omega_7\) remains open. The audit also forces the correction of an earlier, stronger claim: not all auxiliary pieces announced as closed in paper 36 are proved with the stated scope. In particular, \(\Omega_4\) mixes two whitenings with different domains, and \(\Omega_5\) proves continuity at fixed order but not unconditional positivity.

There is also a correction that changes the restart. From the exact split \(\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}\), Ω₇ is equivalent to

\[
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\qquad(n\ge1),
\]

not to \(|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}\). Absolute domination is a stronger sufficient condition and cannot even be the stated equivalence at \(n=1\). Hence the recommended front becomes a one-sided inequality that preserves the signed cancellation.

The audit also corrects the formula that should start that front: the printed integration by parts changes the sign and omits the boundary term \(-n\). With \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), the valid identity is

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

No continuation should therefore reuse the earlier version without repair.

## Reading order

1. [`00_SCOPE_AND_METHOD.md`](00_SCOPE_AND_METHOD.md): corpus, protocol and meaning of the labels.
2. `MASTER_CONTEXT.md`: self-contained synthesis of the whole path and current mathematical state.
3. `PAPER36_AUDIT.md`: logical spine, confirmed results and necessary repairs.
4. `RH1_RH9_AUDIT.md`: assessment of the nine exploratory programs.
5. `PHASES_AUDIT.md`: walk through all phases, without counting reparametrisations as new closures.
6. `NO_GO_AND_RETRACTIONS.md`: record of discarded routes, exact scope and precedence of corrections.
7. `LIVE_FRONTIER_AND_RESTART_PLAN.md`: admission criterion and restart plan centred on the RH-strength step.
8. `COVERAGE_INDEX.md`: coverage check and size of the dossier.

The files in [`fragments/`](fragments/) keep the block audits that support the synthesis. They are traceability evidence; in case of discrepancy, a later mathematical correction exhibiting the exact step prevails.

## Binding labels

| Label | Meaning |
|---|---|
| **PROVED** | The conclusion follows from the written hypotheses. The scope may be finite or restricted. |
| **CONDITIONAL** | At least one hypothesis used by the conclusion remains to be proved. |
| **NUMERICAL** | Evidence for fixed cut-offs, data and precision; not a limit. |
| **REFUTED** | The specific mechanism fails or contains an identified error. |
| **RH-STRENGTH** | Proving the statement would resolve RH through transfers already established. It cannot be used as an auxiliary lemma. |
| **OPEN** | The statement is well typed and has neither proof nor refutation. |

A proved finite identity does not automatically inherit a cofinal conclusion. An RH-strength condition is not a small gap. A no-go closes only the class of arguments its hypotheses actually cover.
