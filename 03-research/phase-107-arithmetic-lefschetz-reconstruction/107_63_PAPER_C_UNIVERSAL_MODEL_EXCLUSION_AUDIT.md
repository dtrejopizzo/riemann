# 107.63 -- Paper C universal-model exclusion audit

## 1. Purpose

`107_10` states the universal finite-model target for Phase 107, but
the first thing that target must survive is exclusion: we need a finite
shadow showing that the wrong ambient model types really destroy one of
the load-bearing structures that later Part III papers use.

This note records an exact finite audit of that exclusion layer.  It
does not prove existence of a universal finite model.  It proves only
that several tempting simplifications fail for explicit structural
reasons in one finite symbolic window.

## 2. Exact shadow audited here

The verifier `107_63_paper_c_universal_model_exclusion_audit.py`
exact-audits the following finite exclusion shadow.

1. Finite support is not the same thing as truncating the arithmetic
   base: removing the full-base receiver loses required prime channels.
2. Replacing the candidate model by a genus-zero envelope erases the
   degree-one carrier needed by the Phase 107 incidence package.
3. Collapsing the two rulings into one boundary class destroys the
   visible diagonal/transpose architecture used later in Papers C and D.
4. Replacing the discrete candidate by an absolutely continuous
   completion erases the point/resonance classes needed for graph and
   Euler packaging.
5. In the finite symbolic window, only a model that keeps all four
   features at once remains admissible.

## 3. What this closes

This gives `107_10` a real exact shadow rather than a purely verbal
warning.  The universal finite-model target is now supported by a
falsifiable finite obstruction test: several natural but wrong model
choices can be shown to fail exactly, not just heuristically.

## 4. What this does not close

The audit does not prove:

1. existence of a regular proper arithmetic surface
   \(\mathcal X_T/\operatorname{Spec}\mathbf Z\);
2. algebraic construction of the true universal finite model;
3. compatibility with exact adelic realization or Route A
   applicability;
4. any global Picard/Jacobian theorem.

So the gate of `107_29` remains open in the intended sense: the source
route still needs a proved arithmetic model, not just exclusion of bad
finite shadows.
