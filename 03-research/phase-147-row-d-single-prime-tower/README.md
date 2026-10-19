# Phase 147 — Single-prime Frobenius towers and Frob ⋆ Δ^rad (corpus check only)

Before building anything on the single-prime tower {Frob_{p^k}}_k and the radially-averaged
Frobenius object Frob ⋆ Δ^rad, this phase ran the mandatory corpus check: locate every existing
result on the Frobenius diagonal, single-prime positivity, and attempts to give the diagonal a
finite renormalized value, and determine what (if anything) would be new. No construction beyond
this check was carried out in the folder.

## Results

- Frobenius diagonal `I_A(Frob_n,Frob_n)` computed exactly in both bare and ♭ normalizations (Paper 44 Thm 8bis.1b, Cor 8bis.1b′, Rem 8bis.1c): **PROVED** that no sign-free limit exists — Frobenius point classes sit outside the space on which the pairing is defined.
- Radial self-pairing `Frob ⋆ Δ^rad`: **PROVED** (Thm 8bis.2) diagonal diverges to −∞ as the regularization is removed, with exact rate; no finite canonical renormalization exists (**NO-GO** for a Tate-residue-style finite value, not found anywhere in the corpus).
- Single-Euler-factor positivity (Doc 131 Thm 6.7): **PROVED** sharp iff-classification — a pure local weight (|α|=√p) gives positivity, any impurity gives an explicit negative two-bump test; extended to two and n primes (Doc 135 Thms A/A′/B).
- Transfer of this single/two-prime purity mechanism to ζ's destructive regime: **NO-GO** (Doc 135 §7.2, imported into phase 137 §3.4) — ζ's Euler weight sits in the opposite (destructive) regime from the constructive objects the theorem covers.
- Semilocal `W_S` positivity beyond `S={∞}`: **OPEN/NO-GO** per phase 137 D.12 — adding prime blocks only subtracts; the pure finite block is proved to carry no positivity to donate at any finite chart (Thm 8bis.4a).
- Pure-magnitude single-prime Gram forms (no phase/unimodularity datum) as sign-deciders: **PROVED-IMPOSSIBLE** (phase-60 "phase not magnitude" theorem; P122.028 Gate S).
- Identified as genuinely new and not previously computed: diagonal differences `δ_m − δ_n`; a profile-independent finite part of the regularized diagonal; a single-prime-tower object carrying an explicit phase datum coupled to Δ^rad; and an explicit link between Paper 46's open item (21) and Paper 44 Thm 8bis.2.

## Documents

- `CORPUS_CHECK_R147.md` — the full pre-phase corpus check, numbered by charge item, with a summary table and a final list of what would be new.

## Relation to other phases

Builds directly on Paper 44 §8bis, Doc 131/135 (phase 44/45), and phase 137's D.12 semilocal analysis, which it cites as the sharpest prior negative results rather than re-deriving them.
