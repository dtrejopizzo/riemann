# 107.47 -- Paper C correction-sum audit

## 1. Purpose

`107_27` closes the qualitative part of the corner-preserving audit:
the currently visible local centers do not collapse the corner
structurally.  What remains open there is quantitative:

\[
 \varepsilon_{\rm vv}(T)+\varepsilon_{\rm hh}(T)+2\varepsilon_{\rm vh}(T)
 \stackrel{?}{=}
 -2c_T.
 \tag{1.1}
\]

The present note exact-audits the finite bookkeeping shadow of that
transition from local center list to signed correction sum.

## 2. What is audited

The verifier `107_47_paper_c_correction_sum_audit.py` checks four exact
statements.

1. The currently visible center types contribute only through the
   correction channels already isolated in `107_25`--`107_27`.
2. The total correction package is an additive sum over a finite center
   list.
3. Cancellation of \(-2c_T\) is a genuine signed numerical equality,
   not a combinatorial consequence of the center types alone.
4. Boundary-only centers cannot directly alter the corner term.

## 3. Finite shadow being tested

The audit encodes each visible center by:

1. its type `A`--`E`;
2. the correction channels it can feed
   \((\varepsilon_{\rm vv},\varepsilon_{\rm hh},\varepsilon_{\rm vh})\);
3. whether it is corner-touching or boundary-only.

The denominator is then reconstructed exactly as

\[
 h_T=2c_T+\varepsilon_{\rm vv}(T)+\varepsilon_{\rm hh}(T)+2\varepsilon_{\rm vh}(T).
 \tag{3.1}
\]

## 4. Result

The verifier passes exactly.

It confirms that:

1. no currently visible center type carries a direct `corner-killing`
   channel;
2. the correction package aggregates additively over the finite center
   list;
3. exact cancellation requires a special signed equality of the
   coefficients and is not forced by the qualitative local audit;
4. boundary-only centers only affect self-correction bookkeeping.

So the open issue left by `107_27` is now sharply identified as a
numerical signed-sum problem, not a hidden new structural failure mode.

## 5. Scope boundary

This audit still does **not** compute the actual correction signs or
sizes on the real model.  It does not prove:

1. the true values of
   \(\varepsilon_{\rm vv}(T),\varepsilon_{\rm hh}(T),\varepsilon_{\rm vh}(T)\);
2. the nonvanishing of \(h_T\) on the actual constructed surface;
3. the transport of this denominator control into the Picard/Jacobian
   realization or the terminal identity.

Its role is exact but finite: it validates the bookkeeping architecture
of the remaining denominator problem.
