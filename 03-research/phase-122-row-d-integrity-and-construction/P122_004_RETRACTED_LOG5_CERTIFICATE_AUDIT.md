# P122.004 — retracted `log 5` certificate audit

## Verdict

The file
`114_d_181_SELF_CONTAINED_FIRST_ENDPOINT_CERTIFICATE.md` must not be used
as a theorem.  Its boxed claim of full infinite-dimensional positivity at

\[
 T={1\over2}\log 5
\]

was later retracted by D.200.  The strongest surviving certified initial
interval is

\[
 0<T\le\log 2.
\]

## Exact defect

D.181 decomposes the primitive space using a finite `V_200` block and its
infinite complement.  It then eliminates a large finite safe block and
keeps five slow Schur directions.  The proof silently reuses the
`V_200`-complement gap as if it held on the complement of those five slow
directions.  Those complements differ by the 193 eliminated finite safe
directions.

For the actual three-block decomposition

\[
 \mathcal P_T=D\oplus S\oplus Q,
\]

shorting `S` changes both the slow-to-tail coupling and the tail block:

\[
 \begin{aligned}
 C_D&=A_{DQ}-A_{DS}A_{SS}^{-1}A_{SQ},\\
 Q_S&=A_{QQ}-A_{QS}A_{SS}^{-1}A_{SQ}.
 \end{aligned}
\]

D.181 computed neither the safe-tail relative norm

\[
 \kappa=\|A_{QS}A_{SS}^{-1/2}\|^2
\]

nor the corrected residual `C_D`.  D.200 supplies a scalar counterexample
showing that omitting these terms can certify an indefinite matrix as
positive.  Hence the omission is logical, not merely a loose estimate.

## Repository chronology

The controlling later records agree:

1. `114_d_200_THREE_BLOCK_FESHBACH_AND_D172_CORRECTION.md` explicitly
   demotes D.181.
2. `PHASE_114_CLOSURE.md` records row (d) as reduced, not closed, and says
   the `T=(1/2)log5` paper claim was demoted.
3. Paper 42's audited-next-endpoint discussion says the two required
   inequalities were never computed.
4. Phase 118's `W4_CERTIFIED_RANGE.md` confirms that the certified endpoint
   remains `T=log2`.
5. Phase 120's full-residual diagnostic still treats `(1/2)log5` as the
   first open endpoint.

The stale D.181 file remains useful only as provenance for the finite and
five-column calculations.  Its heading and boxed theorem are superseded.

## Consequence for phase 122

The first-contact theorem P122.002 uses only the strict full-space
certificate at `T_0=log2`; it does not use D.181.  Therefore this retraction
does not damage first-contact attainment.  It does show that phase 122 must
resolve claims by chronological dependency, not by finding an isolated
file labelled `PASS` or `theorem`.
