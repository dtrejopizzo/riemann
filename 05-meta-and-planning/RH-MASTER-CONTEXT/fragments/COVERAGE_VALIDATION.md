# Mechanical coverage validation

## Verdict

Documentary coverage is complete for the three declared scopes. No broken links, nonexistent catalog references, LaTeX imbalances, or contradictions between the central formulas and the restart plan were detected.

## Cross-checked inventory

- Paper 36: `04-papers/36-obstruction-ledger/main.tex` has 8,806 lines and 54,962 words. The main audit and its logical fragment exist.
- RH1–RH9: there are 626 `task` directories, distributed as 89, 94, 83, 83, 60, 68, 43, 27, and 79. Each series is continuous from `task1` to its maximum and belongs to a block audit.
- Phases: there are 101 `phase-*` directories. Labels 001 and 002 do not exist and 044 has two paths; both anomalies are on record. The five audits cover every interval from 000 to 101.
- Block 076–089 accounts for the 512 Markdown files present. The nominal sweep for closures found no candidates outside the audited directories.

## Navigation and size

The 42 local Markdown links resolve. The eight reading-order documents, the textual scope references, and the index map exist.

Excluding this report to avoid circularity, the other nineteen Markdown files contain 45,101 words, 320,961 Unicode characters, and 326,879 bytes. The mechanical bound of one token per byte comes to 326,879 tokens. Including this report, the dossier keeps twenty Markdown files, fewer than 50,000 words, and fewer than 350,000 bytes, within the declared limit.

## LaTeX balance

In all the Markdown files the block and inline math delimiters match, as do the `begin`/`end` pairs and the `left`/`right` pairs. No aligned rows are left ending with a single backslash, nor are there malformed RDI spacing sequences.

## Verified formulas

The one-sided formula is an exact algebraic consequence of the declared split:

\[
\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime},
\qquad
\lambda_n\ge0
\Longleftrightarrow
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]

Su tratamiento por signo es correcto. La fórmula exacta de la parte arquimediana, junto con la convexidad discreta, da

\[
I_-:=\{n\ge1:\lambda_n^{\rm arch}<0\}=\{1,2,\ldots,7\}.
\]

The independent numerical check reproduces \(d_3\approx0{,}00626036\), \(\lambda_7^{\rm arch}\approx-0{,}355731\), and \(\lambda_8^{\rm arch}\approx0{,}020900\). Hence, outside \(I_-\) the control of the negative part can be formulated; inside \(I_-\) the full lower bound must be kept.

The Laguerre limit is correctly paired. For \(\varepsilon>0\), the first summand is the integral of \(f_{n,\varepsilon}\) against Lebesgue measure and the second is the integral against \(d\psi\); both use the same regulator. At \(n=1\), the difference tends to \(\gamma\), as required by \(\lambda_1^{\rm prime}\).

With

\[
f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\qquad f_{n,\varepsilon}(1)=n,
\]

integration by parts preserves the sign and the lower boundary:

\[
\lambda_n^{\rm prime}
=\lim_{\varepsilon\downarrow0}
\left[-n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right]
=\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

The two forms agree because \(\int_1^\infty f'_{n,\varepsilon}=-n\). The asymptotic normalization is also consistent:

\[
\lambda_n^{\rm arch}
=\frac n2\log\frac n{2\pi}
+\frac{\gamma-1}{2}n
+\frac34+O(n^{-1}).
\]

The linear term is not absorbed into \(O(\sqrt n\log n)\), and every bound with that factor starts at \(n\ge2\).

## Consistency of the RDI plan

The RDI route remains open and subordinate to the outcome of the LP/GAP-Z triage. The plan does not present it as a requirement of the one-sided attack nor as an already-obtained closure. If the attribution survives, it freezes a single coordinate, `C_core`, requires an explicit order of limits and Gamma–Euler source, and rejects new reformulations without an additional estimate. This hierarchy agrees with `MASTER_CONTEXT.md`, `PHASES_AUDIT.md`, and the record of withdrawals.

## Form checks

The full sweep finds neither the two restricted voices nor temporal metadata fields. The auxiliary format counts certify presence, not mathematical content.
