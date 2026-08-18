# 107.64 -- Paper A diagonal coherence audit

## 1. Purpose

`107_05` claims that the diagonal is closed by the same Gamma--polar
metric that governs off-diagonal pairings.  This is stronger than
checking a standalone archimedean factor: it means there is one common
Green functional, stabilized by one matched cutoff protocol, and that no
extra diagonal-only scalar may be slipped in later.

This note adds an exact finite audit artifact for that narrow logical
pattern.

## 2. Exact shadow audited here

The verifier `107_64_paper_a_diagonal_coherence_audit.py` exact-audits a
finite symbolic shadow of `107_05` §§5--7.

It checks:

1. matched-cutoff stabilization is cutoff-independent once the cutoff
   exceeds the finite support of the correlation;
2. the same stabilized Green functional is used for cross-pairings and
   self-pairings;
3. the resulting quadratic and bilinear packages satisfy the exact
   polarization identity when built from one common metric;
4. inserting any diagonal-only additive correction breaks that
   polarization identity immediately.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper A diagonal-coherence checks passed.
```

So the workspace now contains a reproducible finite audit that the
diagonal/coherent-metric claim of `107_05` is not merely verbal.

## 4. What this proves and what it does not

This audit proves a useful but narrow point:

1. the common-cutoff stabilization can be represented exactly in one
   finite symbolic model;
2. one and the same Green functional closes both cross and diagonal
   pairings in that model;
3. diagonal-only renormalization shifts are detectable because they
   violate polarization.

It does **not** prove:

1. the full analytic archimedean Green theory of `107_05`;
2. the published arithmetic-surface or adelic metric theorem;
3. the final geometric realization over \(\operatorname{Spec}\mathbf Z\).

So the correct reading is:

\[
 \text{finite diagonal-coherence shadow exact-audited},
 \qquad
 \text{full Green metric theorem still not proved on the target side}.
 \]
