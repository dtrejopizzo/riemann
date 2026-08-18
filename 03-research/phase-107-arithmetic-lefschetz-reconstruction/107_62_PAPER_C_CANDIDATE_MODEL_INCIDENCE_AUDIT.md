# 107.62 -- Paper C candidate-model incidence audit

## 1. Purpose

`107_15` is the first note that actually proposes a candidate finite
model \(\mathcal X_T^{(1)}\), but until now it still had no exact audit
artifact of its own.

The present note exact-audits the finite structural shadow of that
candidate-model protocol.  It does not prove the regular proper surface
theorem.  It proves something narrower and exact:
in the visible model, the incidence locus really contains the two
rulings, the diagonal, and the visible graph generators, those
generators do not collapse into one another, the graphs meet the common
boundary receiver compatibly with the two-ruling structure, and the
regularization centers form a finite visible list.

## 2. Shadow being tested

The audit uses the structural pieces explicitly named in `107_15`:

1. the diagonal \(\Delta_{\rm fr}\);
2. the two boundary ruling families \(B_{\infty,\mathrm v}\),
   \(B_{\infty,\mathrm h}\);
3. the visible prime-power graph generators \(\Gamma_n^{\rm fr}\);
4. the regularization-center classes listed in the candidate envelope
   protocol.

The exact finite question is:

\[
 \mathfrak U_T
 \Longrightarrow
 \mathcal X_T^{(1)} \text{ keeps the required visible incidence data}
 \tag{2.1}
\]

already at the symbolic finite level.

## 3. What the verifier checks

The script `107_62_paper_c_candidate_model_incidence_audit.py`
exact-audits five statements.

1. The visible incidence locus contains the diagonal, both rulings, and
   every visible graph generator.
2. No visible graph generator collapses to the diagonal or to a ruling
   component.
3. Every visible graph meets the shared boundary receiver while
   preserving the phase channel and the two-ruling structure.
4. The regularization-center types used by the candidate-model protocol
   form a finite visible list.
5. The visible carrier data are incompatible with a single-chart
   genus-zero envelope shadow.

Everything is exact: the verifier checks discrete incidence and
component data, not floating approximations.

## 4. Result

The verifier passes exactly.

This means `107_15` now has a real exact shadow:
the candidate model is no longer only a prose construction protocol, but
also a finite witness that the visible incidence data it is supposed to
carry are structurally present and noncollapsed.

## 5. Scope boundary

This audit still does **not** prove:

1. existence of the true regular proper model;
2. correctness of the global normalization and blow-up sequence;
3. the actual Picard/Jacobian degree-one theorem;
4. the full theorem of `107_15`.

Its force is finite and exact:
the visible incidence structure of the candidate model now has an
independent audit artifact rather than remaining purely formal.
