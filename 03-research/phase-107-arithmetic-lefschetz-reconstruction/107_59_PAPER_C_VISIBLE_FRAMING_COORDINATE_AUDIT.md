# 107.59 -- Paper C visible framing-coordinate audit

## 1. Purpose

`107_18` replaces the abstract framing coordinate \(\xi\) by a finite
visible rooted/cyclotomic coordinate \((n,\chi)\), but until now that
replacement had no exact audit artifact of its own.

The present note exact-audits the finite combinatorial shadow of that
claim.  It does not solve the full compactified framed-divisor moduli
problem.  It proves something narrower and exact:
inside the visible window, the rooted coordinate really factors through
a finite order set, its characters have the declared order-divisibility
behavior, the action \(\mu_m\) is a genuinely finite combinatorial map,
and the graph-closure equations reduce to finitely many packet data.

## 2. Shadow being tested

The audit uses the visible order set \(\mathcal N_T\), the visible
rooted dual \(X_T^\vee\), and the finite action \(\mu_m\) of `107_18`.

The exact finite question is:

\[
 \xi_T=(n,\chi)
 \tag{2.1}
\]

does this visible replacement actually behave like a finite combinatorial
coordinate system rather than only a suggestive notation?

## 3. What the verifier checks

The script `107_59_paper_c_visible_framing_coordinate_audit.py`
exact-audits four statements in the visible window \(n\le 12\).

1. Every visible order in the window satisfies the declared prime-power
   visibility rule.
2. For each visible order \(n\), every visible character has order
   dividing \(n\), and the exact-order spectrum can be read off
   combinatorially.
3. The finite action \(\mu_m\) is defined exactly when the multiplied
   order remains in the visible window, and then lands back in finite
   rooted packet data.
4. The graph-closure equations of `107_18` reduce to finitely many
   combinatorial packet outputs together with the one-dimensional chart
   coordinates.

Everything is exact: the verifier checks discrete packet data and
order-divisibility identities, not floating approximations.

## 4. Result

The verifier passes exactly.

This means `107_18` now has a real exact shadow:
the finite visible framing coordinate is no longer only a theorem-level
reduction claim, but a combinatorial witness that the rooted data do
factor through a finite window and support finite-type graph equations.

## 5. Scope boundary

This audit still does **not** prove:

1. that the visible charts glue to the full compactified factor
   \(\overline{\mathfrak P}_{\rm fr}\);
2. that the resulting global compactification is proper or regular;
3. that the Gamma--polar metric descends on the realized model;
4. the full theorem of `107_18`.

Its force is finite and exact:
the visible rooted framing coordinate now has an independent audit
artifact rather than remaining purely formal.
