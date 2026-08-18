# D.226 — Scope of the endpoint-flat Green construction

## Exact statement under construction

At \(T=\frac12\log 6\), let

\[
 F=S_{\rm flat}^{78}
 \subset V_{200}^{\rm prim}
\]

be the order-\(60\) endpoint-flat primitive source.  Inside the complete
order-\(60\) endpoint-flat primitive space in \(V_{400}\), D.226 constructs
the exact \(L^2\)-orthogonal complement \(W_{\rm flat}^{200}\) of \(F\).
Both spaces satisfy the two Tate equations.  For

\[
 B=F^*A_TF,\qquad E=W^*A_TW,\qquad C=F^*A_TW,
\]

the directed target is

\[
 CE^{-1}C^*\leq0.2B.                              \tag{0.1}
\]

The corrected source

\[
 F_{400}=F-WE^{-1}C^*
\]

remains divisible by \((T^2-t^2)^{60}\).  Therefore D.208 applies to its
post-\(400\) Legendre action tail without losing the endpoint-flat
hypothesis.

## Integration caveat

The band \(W_{\rm flat}\) is orthogonal to \(F\), not to the complete
primitive \(V_{200}\).  In particular it need not lie in
\((V_{200}^{\rm prim})^\perp\).  The complement gap

\[
 A_{QQ}\geq0.2199Q
\]

from D.185 is proved on the latter space and cannot be applied directly to
the complement of \(F\) after shorting \(W_{\rm flat}\).

Consequently (0.1), even together with the D.208 post-\(400\) estimate,
does **not** by itself prove the D.221 capacity \(\rho_6\leq0.7\).  The
correct complete finite decomposition is

\[
 D_{\rm bdry}^{120}\dotplus F^{78}
 \dotplus W_{\rm flat}^{200}\dotplus V_{400}^{\perp}.       \tag{0.2}
\]

The boundary block in (0.2) must be retained in the Schur factorization.
Equivalently, one may replace \(W_{\rm flat}\) by the correctly typed band

\[
 W_{\perp}=(V_{400}^{\rm prim})\ominus(V_{200}^{\rm prim}), \tag{0.3}
\]

which lies in the D.185 high block but no longer preserves endpoint
flatness.  D.227 compares these two candid alternatives before a further
large interval computation is attempted.

## Classification

* construction of \(F\), \(W_{\rm flat}\), and \(F_{400}\):
  **ALGEBRAIC / INTERVAL-DIRECTED**;
* finite inequality (0.1): **AWAITING THE GAMMA/CONTACT CACHE**;
* applicability of D.208 to \(F_{400}\): **PROVED**, conditional only on
  the successful directed D.226 construction;
* implication from these two facts to \(\rho_6\leq0.7\): **FALSE WITHOUT
  THE BOUNDARY SCHUR GATE**;
* four-block endpoint gate and row D: **OPEN**.
