# 107.70 -- Paper A audit coverage matrix

## 1. Purpose

Paper A now has several exact audit artifacts, but they land on
different layers of `107_03`--`107_05`.  This note records, in one
place, which parts of Milestone I are now exact-audited shadows and
which parts remain only theorem-level synthesis.

Its role is governance:

\[
 \text{several exact shadows}
 \neq
 \text{full Milestone I independently closed}.
 \]

## 2. Coverage matrix

| Part I component | Current evidence | Status |
| --- | --- | --- |
| Connected extractor on Euler unions | `107_35` exact Hopf-algebra audit and fixed-control specialization | exact-audited shadow |
| Raw/divisor separation before connected extraction | `107_35` exact audit of the visible Euler-vs-connected extractor logic | exact-audited shadow |
| Prime-power local support law | `107_34` exact resultant-support audit | exact-audited shadow |
| Diagonal warning at the finite level | `107_34` exact audit of diagonal resultant vanishing | exact-audited shadow |
| Common Green functional for diagonal and cross terms | `107_64` exact diagonal-coherence audit | exact-audited shadow |
| Matched-cutoff stabilization shadow | `107_64` exact audit of cutoff independence in one finite symbolic model | exact-audited shadow |
| Full analytic Gamma--polar metric theorem | theorem statement in `107_05`; factor-level support from `107_41` | partial shadow |
| Unified finite-support intersection theorem of `107_06` | `107_75` exact unified-synthesis audit, together with the component shadows `107_34`, `107_35`, `107_64` | partial shadow |

## 3. What is genuinely secured

1. The Eulerian connected extractor is no longer only formal prose:
   `107_35` exact-audits the primitive/decomposable separation and its
   fixed-control specialization.
2. The local cyclotomic support law is no longer only theorem-level:
   `107_34` exact-audits the prime-power support rule and the diagonal
   finite warning.
3. The diagonal coherence claim of `107_05` is no longer only verbal:
   `107_64` exact-audits one common Green functional, matched-cutoff
   stabilization, exact polarization, and the failure of diagonal-only
   shifts.
4. `107_41` gives a narrow exact consistency audit for the explicit
   coupled Gamma--pole factor used by `107_05`, but not yet for the full
   analytic metric theorem.
5. `107_75` exact-audits one finite unified shadow of `107_06`: in one
   shared symbolic model, connected extraction kills decomposable Euler
   mass before pairing, only visible prime-power support survives in the
   finite sector, and the same Green functional still governs both
   cross and diagonal pairings with exact polarization.

## 4. What remains unaudited

1. the full analytic archimedean metric descent of `107_05`;
2. the full analytic theorem-level synthesis of `107_06` beyond the
   current finite unified shadow;
3. the target-side realization of the Paper A determinant/metric data on
   a proved arithmetic surface or adelic category.

## 5. Status consequence

The correct reading after `107_34`, `107_35`, `107_64`, `107_41`, and
`107_75` is:

\[
 \text{Paper A no longer merely formalized},
 \qquad
 \text{but still only partially exact-audited}.
 \]

So later forward construction may not promote the whole of Milestone I
to fully proved-from-audits status without a new artifact that directly
tests the remaining unified metric/synthesis gap.
