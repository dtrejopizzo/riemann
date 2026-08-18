# 107.53 -- Paper D A1 boundary audit: regular properness remains a genuine geometric jump

## 1. Purpose

`107_50` records A1 as `partial`, and after the new finite audits it
is worth isolating exactly why A1 has not moved with A2, A3, A5, or A6.
The issue is not that nothing has been built.  The issue is that the
existing Part III artifacts only establish candidate-model architecture,
chartwise control, and exclusion of obvious bad envelopes; they do not
yet produce a proved regular proper arithmetic surface or an exact
adelic comparison theorem.

The methodological distinction is:

\[
 \text{``candidate model with structural constraints''}
 \neq
 \text{``proved regular proper model for Route A''}.
 \tag{1.1}
\]

This note turns that distinction into an explicit audit boundary.

## 2. The A1 target

By `107_12`, A1 requires one of the following.

1. a regular proper arithmetic surface
   \(\mathcal X_T\to\operatorname{Spec}\mathbf Z\), or
2. an exact adelic substitute together with a proved comparison to such
   a regular proper model.

Nothing weaker closes Route A.

## 3. What the current Part III package does secure

The current Phase 107 papers do provide real structural progress.

### 3.1. The target is fixed globally

`107_10` fixes the correct realization problem:
finite support of \(D_f\) may restrict which prime-power packets are
visible, but it may not truncate the arithmetic base.

### 3.2. Obvious wrong envelopes are excluded

`107_10` proves three negative structural facts.

1. genus-zero envelopes are excluded;
2. the realization must preserve both polar rulings;
3. absolutely continuous completions that erase the divisor/point
   sector are excluded.

These exclusions matter because they eliminate the precise failures
already isolated by the earlier stop tests.

### 3.3. A concrete candidate-model protocol exists

`107_15` replaces pure blueprint language by an explicit protocol:
take the finite-support incidence locus inside the framed-divisor
square, compactify, normalize, and blow up the diagonal/boundary and
graph-intersection strata.  This is stronger than merely postulating
\(\mathcal X_T\).

### 3.4. Boundary and local charts are organized

`107_16` specifies a compactified framed-divisor square
\(\overline{\mathfrak S}\), the two ruling boundaries, and the common
corner \(C_\infty\) where the Gamma--polar page should descend.
`107_17` adds a local chart atlas and a finite-type criterion for the
closed graph loci \(\overline{\Gamma}_n^{\rm fr}\).

Together these notes show that the candidate realization is not a vague
black box.

## 4. Why this still does not prove A1

The load-bearing gap is geometric, not editorial.

### 4.1. The ambient square is still only a candidate ambient object

`107_15` states explicitly that
\(\mathfrak S=\widetilde{\mathrm{Pic}}_{\rm fr}\times
\widetilde{\mathrm{Pic}}_{\rm fr}\) is not yet a regular proper
arithmetic surface.  It is only the ambient moduli square from which a
classical envelope should later be cut out.

### 4.2. The compactification is protocol-level, not theorem-level

`107_16` gives the first boundary protocol for
\(\overline{\mathfrak S}\), but it does not prove that the desired
compactification exists as a finished arithmetic scheme or stack with
all comparison properties required by Route A.

### 4.3. The regularization step is still aspirational

`107_15` defines \(\mathcal X_T^{(1)}\) by closure, normalization, and
blowups, but states explicitly that this is a candidate rather than a
theorem.  No artifact in the present tree proves that the output is a
regular proper arithmetic surface carrying the required realized cycles
with the exact target-side comparison maps.

### 4.4. Chartwise finite-type control is not regular properness

`107_17` reduces parts of the problem to finitely many local conditions,
but finite-type chart control does not by itself establish:

1. global properness over all of \(\operatorname{Spec}\mathbf Z\);
2. regularity after all required blowups;
3. compatibility of the resulting global object with the adelic
   categories used in Route A.

## 5. Audit conclusion

### Proposition 5.1: A1 remains `partial`

The current Phase 107 artifacts justify keeping A1 at `partial`.

Proof.  `107_10`, `107_15`, `107_16`, and `107_17` jointly fix the
global target, exclude several structurally wrong envelopes, and provide
an explicit candidate-model and chartwise compactification protocol.
However, none of them proves the existence of a regular proper
arithmetic surface \(\mathcal X_T\to\operatorname{Spec}\mathbf Z\), nor
an exact adelic substitute with a proved comparison theorem to such a
surface.  By the definition of A1 in `107_12`, that means A1 is not yet
proved.  The current exact shadows are still only candidate-level
support and exclusion/coherence witnesses, not a target-side
regular-properness theorem.  Therefore the correct status remains
`partial`, not `proved`.  \(\square\)

## 6. What would actually promote A1

No additional forward construction alone can promote A1.  A promotion
artifact would need at least one of the following.

1. a proved regular proper model theorem for \(\mathcal X_T\) on the
   full arithmetic base;
2. a proved exact adelic substitute together with a comparison theorem
   into a published Hodge-applicable category;
3. an audit artifact that directly checks the target-side regular
   properness/comparison hypotheses rather than only the source-side or
   candidate-level architecture.

## 7. Operational rule

Any later document using `107_15`--`107_17` may cite them as structural
support for the candidate realization program, but may not cite them as
closing A1.  Until a new artifact of the type listed in §6 exists,
regular properness remains a genuine geometric jump in Phase 107.
