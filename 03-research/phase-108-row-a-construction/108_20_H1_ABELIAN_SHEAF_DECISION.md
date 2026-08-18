# 108.20 -- The abelian-sheaf H^1 route is not available for DC objects: a decision, negative, and why

## 1. The question

Connes-Consani declare \(H^1\) open for the idempotent-monoid formulation
(1805.10501). A candidate rescue exists in principle: Mikhalkin-Zharkov and
Cartwright construct \(H^1(\Delta,\mathcal A_{\mathbb Z})\cong
\mathrm{Pic}_{\mathrm{ridge}}\) for the sheaf of \(\mathbb Z\)-affine
(piecewise-linear, integer-slope) functions on a **finite** \(\Delta\)-complex.
108_00 SS7 asks whether that machinery is available for the DC objects this
phase works with (both 107_237's \(D_f\), \(f\in C_c\), and 108.03's graded
family \(\mathcal G\)), and states plainly that a negative answer is a full
deliverable. It is negative, for two independent reasons.

## 2. Obstruction 1: DC objects are outside the theorem's hypothesis, by an already-proved theorem

Mikhalkin-Zharkov/Cartwright's \(H^1\cong\mathrm{Pic}_{\mathrm{ridge}}\)
is stated for the sheaf \(\mathcal A_{\mathbb Z}\) of piecewise-**linear**
functions with integer slopes on a **finite** polyhedral complex \(\Delta\):
functions that are, locally, the maximum (or a fixed combination) of
finitely many affine pieces.

### Theorem 2.1 (restatement of 107_237 Theorem 2.1, cited not re-derived)

If \(f\in C((0,\infty))\) is nonzero on an interval, \(U_f\) is not the
divisor of any finite-PL rational section: the angular second derivative of
a finite-PL function is a finite atomic measure, while \(u_f''=f/r\) is a
nonzero continuous density on that interval. These distributions cannot
agree.

### Proposition 2.2 (the graded family is finite-PL for no \(s\))

Every \(U_s\in\mathcal G\) (108.03 (2.1)-(2.2)) is real-analytic away from
\(0\) and nonlinear for every \(s\) (its second derivative
\(u_s''(r)=r^{s-1}\) is nowhere zero on \((0,\infty)\)), hence is not
piecewise-linear on any subdivision with finitely many pieces (a PL
function has vanishing second derivative off a finite set; \(r^{s-1}\) does
not vanish anywhere).

**Proof.** Direct: \(r^{s-1}=0\) has no solution in \((0,\infty)\) for any
real \(s\). \(\square\)

### Consequence

Both DC categories this phase constructs -- 107_237's \(C_c\)-currents and
108.03's graded monomials -- fail the finite-PL hypothesis that
Mikhalkin-Zharkov/Cartwright's theorem is stated for, by an exact
already-proved theorem (Theorem 2.1) plus a one-line extension (Proposition
2.2) covering the new family this phase adds. This is not a matter of the
theorem being hard to apply; its domain of applicability *excludes* the
objects by construction.

## 3. Obstruction 2: even granting an extension, the two \(H^1\)'s are not shown to agree

108_00 SS7 flags this explicitly, and it survives independently of
Obstruction 1.

\(\mathrm{Pic}_{\mathrm{ridge}}=H^1(\Delta,\mathcal A_{\mathbb
Z}^\times)\) is the cohomology of the **sheaf of units** of
\(\mathcal A_{\mathbb Z}\) (its multiplicative/invertible-elements sheaf,
in whatever sense "invertible" is meant for a sheaf of monoid-valued PL
functions) -- it classifies line bundles, i.e. it is a Picard group. What
Connes-Consani's Riemann-Roch program needs is \(H^1\) of the **structure
sheaf** itself, additively: the object whose dimension appears as the
"\(h^1(D)\)" term in a Riemann-Roch formula
\(h^0(D)-h^1(D)=\deg D+\chi\).

### Proposition 3.1 (no comparison map is constructed anywhere in this program)

There is, in the sources read for this phase (Mikhalkin-Zharkov, Cartwright,
Connes-Consani 1805.10501, and every phase-106/107/108 document), no
constructed comparison map \(H^1(\mathcal O)\to\mathrm{Pic}\,\) or
\(\mathrm{Pic}\,\to H^1(\mathcal O)\) for this category, additive versus
multiplicative sheaf cohomology in general disagree (e.g. already in
classical algebraic geometry, \(H^1(X,\mathcal O_X)\) and
\(H^1(X,\mathcal O_X^\times)=\mathrm{Pic}(X)\) are related by the
exponential/Kummer exact sequence, not equal, and that sequence is not
available here since there is no exponential map between the idempotent
monoid structure sheaf and its units in the relevant category), and nothing
in this phase constructs or rules out such a comparison for the DC/graded
category. This is an candid gap, not a claim that the two invariants
*must* differ; only that no argument identifying them exists.

## 4. Decision

\[
 \boxed{\texttt{ABELIAN\_SHEAF\_H1\_ROUTE\_FOR\_DC\_OBJECTS: NOT\_AVAILABLE}}
\]

for two independent reasons: (1) neither DC category constructed in this
program (107_237's \(C_c\)-currents, 108.03's graded family) is finite-PL,
which is the stated hypothesis of the only cited construction of
\(H^1\cong\mathrm{Pic}\,\) (Theorem 2.1, Proposition 2.2); (2) even
granting an extension of that theorem past its finite-PL hypothesis, its
target \(\mathrm{Pic}_{\mathrm{ridge}}\) is not shown, here or
anywhere cited, to compute the same invariant Connes-Consani's program
needs (\(H^1\) of the structure sheaf), and no comparison map is
constructed (Proposition 3.1).

## 5. What would be needed instead (not pursued here)

Three avenues, named and left open, matching the style of 107_237 SS5 and
107_239 SS5's "next gate" sections:

1. **A new \(H^1\) theory built directly for the DC/graded category**,
   rather than imported from the finite-PL theory -- the candid route, and
   a substantial undertaking on its own, not attempted in this phase.
2. **A comparison map** \(H^1(\mathcal O_{\mathrm{DC}})\to
   \mathrm{Pic}_{\mathrm{ridge}}\)-analogue, constructed and proved
   an isomorphism (or at least injective/surjective with controlled
   kernel/cokernel) for this category -- would resolve Obstruction 2 alone,
   leaving Obstruction 1 (finite-PL exclusion) untouched, so it would need
   pairing with (1) or a genuine finite-PL approximation scheme (not the
   graded family, which is exactly non-PL by Proposition 2.2).
3. **Abandon the abelian-sheaf strategy** for row (a)'s existence theorem
   entirely, and pursue \(H^1\)/RR through the adelic corner-trace methods
   of 107_239, which do not invoke a finite \(\Delta\)-complex at all. This
   is consistent with, and does not require retracting, anything already
   proved: 107_239-107_241's construction never used finite-PL machinery.

None of the three is constructed or ruled out here; this note only removes
the abelian-sheaf/Pic_ridge shortcut from consideration for DC objects.

## 6. Scope

Proved here:

* Proposition 2.2: the graded family \(\mathcal G\) is non-finite-PL for
  every \(s\), extending 107_237 Theorem 2.1's exclusion to the new family
  constructed in this phase;
* Proposition 3.1 (a scope statement, not a theorem about an external
  object): no comparison map between the two candidate \(H^1\)'s is
  constructed anywhere in the read literature or this program.

Not established:

* that \(H^1(\mathcal O)\) and \(\mathrm{Pic}_{\mathrm{ridge}}\)
  actually differ in this category (only that nothing shows they agree);
* any of the three avenues of SS5;
* any change to `ROW_A_STATUS`.

## 7. Verifier

`108_20_h1_abelian_sheaf_decision.py`:

1. re-derives (does not merely assert) Proposition 2.2: samples
   \(u_s''(r)=r^{s-1}\) on a grid for a bank of \(s\) and confirms it is
   bounded away from zero everywhere on the sampled domain, i.e. no
   finite-PL (piecewise-affine, second-derivative-supported-on-finitely-
   many-points) representative can match it -- the discrete analogue of
   Theorem 2.1's argument, applied to every member of \(\mathcal G\);
2. cross-checks that 107_237's own compactly supported category is
   excluded too, by re-sampling a bump function's second derivative and
   confirming it is not concentrated on a finite set (contrasted with an
   explicitly finite-PL function, e.g. \(\max(y-x,0)\), whose second
   derivative sampled this way is exactly supported at one point up to grid
   resolution);
3. prints the two obstructions and `VERDICT: NOT_AVAILABLE`.
