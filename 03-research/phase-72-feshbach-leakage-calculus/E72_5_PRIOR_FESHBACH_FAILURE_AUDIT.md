# E72.5 -- Prior Feshbach/Schur failures audit

**Date:** 2026-07-08.
**Role:** audit the earlier uses of Feshbach/Schur shorting before using it again in Phase 72.

## Files audited

Main sources:

- `phase-65-signature-continuity/STAGE1-finite-dimensional-model.md`
- `phase-65-signature-continuity/D4-POSITIVE-POLE-FESHBACH-SHORTING.md`
- `phase-65-signature-continuity/CORRECTIONS-CONNES-R1.md`
- `phase-65-signature-continuity/D8.5a-MARKED-TATE-BINET.md`
- `phase-65-signature-continuity/D8.5b-i-SELF-ADJOINT-COMPLETION.md`
- `phase-63-lefschetz-realization/BRIEFING-2.3.F-for-Connes.md`
- `phase-60-discriminant/III-ruta-correcta.md`
- `phase-60-discriminant/attack-gap-i-improved-hardy.tex`
- `00-MAP.md`
- `phase-4-handoff/proofs/00-PROOF-LOG.md`

Also searched the repo for `Feshbach`, `Schur`, `shorting`, `Haynsworth`, `Feshbach inverse`,
`graph norm`, and `coboundary`.

## 1. What Feshbach already gave us

The earlier program established several solid facts.

### Fact A -- shorting, not subtraction

Phase 65 Stage 1 and D4 prove the decisive linear algebra:

```text
Short_a [[a,b*],[b,C]] = C - b a^{-1} b*
```

is the correct removal of a positive pole line. Naive subtraction creates spurious negative squares
(`G_R` counterexample); Schur/Feshbach shorting does not.

### Fact B -- positive-pole shorting preserves negative index

Haynsworth inertia gives, for `a>0`,

```text
nu_-([[a,b*],[b,C]]) = nu_-(C - b a^{-1}b*).
```

So positive-pole shorting is index-safe. This is real and should be reused.

### Fact C -- Feshbach is the right way to remove high-mode contamination

Phase 60 found that full Rayleigh/operator norms are contaminated by fast modes. The correct low-sector
object was the shorted form

```text
F_tilde = P A P - P A Q (Q A Q)^{-1} Q A P.
```

This is the same lesson now reappearing as E72.3:

```text
the eigenvector sees C^{-1}b, not b.
```

## 2. Where Feshbach failed before

### Failure A -- Feshbach did not provide convergence by itself

D4 supplies the correct shorted object, but D4 explicitly does not prove that the shorted kernels
converge to the fixed endpoint. The open piece remained:

```text
K_P^circ -> K_Xi^{G5}
```

or, in operator language, strong-resolvent convergence across the strip.

Thus Phase 72 must not say: "because we shorted, convergence follows." Shorting defines the right
quantity; it is not a convergence theorem.

### Failure B -- sourced determinants do not Euler-factor

Connes R1 corrected the sourced product claim. For finite-rank sources,

```text
D_P^{src}(Phi C Phi*) / D_P
   = exp(anomaly) det(I + C G_P^circ),
```

where

```text
G_P^circ = Phi* F_P^{-1} Phi.
```

The determinant is taken after the Feshbach inverse. It does not factor over places. Therefore any Phase
72 proof that expands `C_x^{-1}` additively over prime cells is invalid.

### Failure C -- Green/resolvent additivity was false

D8.5a block 7 originally wrote an additive assembly of Green matrices. D8.5b-i refuted it:

```text
(A+B-z)^{-1} != (A-z)^{-1} + (B-z)^{-1}.
```

Only first-order local masses add. The actual object is the non-additive Feshbach inverse. This is the
most important warning for Phase 72.

### Failure D -- endpoint identification carries RH-strength

The corrected Phase 65 split is:

```text
D8.5a: convergence to some marked Green limit       plausibly local
D8.5b: identify that limit with G_Xi^{G5}           RH-strength
```

Phase 72 must not hide endpoint identification inside notation. If a proof of the variational lemma
requires knowing that the limiting reduced resolvent is the `Xi` resolvent, it has reintroduced the
Phase 65 wall.

### Failure E -- Schur tests and l1 routes hit oversampling

The Phase 4 proof log records that pointwise Schur/Gram/Jaffard/interpolation routes all run into the
oversampling parameter `P = rho ell -> infinity`. This is a different use of Schur, but the lesson is
relevant: an `l1` coefficient bound is usually too strong and loses the coherent cancellation.

Phase 72 must work in the reduced `C_x`-graph norm, not in row/column `l1` bounds.

## 3. What Phase 72 is allowed to use

Allowed:

- Schur complement as the definition of pole removal.
- Haynsworth/inertia for positive finite blocks.
- The actual compressed complement `C_x`, including all cross terms.
- The reduced vector `C_x^{-1}Q_xR_xk_x`.
- Variational estimates in the graph norm `||C_x v||`.
- Low/high spectral splits of the actual `C_x`.

Forbidden:

- pole subtraction;
- additive Green/resolvent assembly over primes;
- sourced Euler products for arbitrary sources;
- endpoint identification from the scalar determinant alone;
- `l1` Schur/Gram row-column bounds as a substitute for coherent cancellation;
- proving convergence merely from the fact that a Feshbach transform exists.

## 4. Consequence for E72.3/E72.4

The reduced leakage target

```text
||C_x^{-1}Q_x(H_x-H_x^0)k_x|| -> 0
```

is compatible with the prior audit only if `C_x` is the **actual** Feshbach-compressed complement. It
must not be replaced by:

```text
sum_p C_{x,p},
sum_p C_{x,p}^{-1},
```

or any local inverse assembled term-by-term.

The variational form

```text
sup_v |<v,(H_x-H_x^0)k_x>| / ||C_xv|| -> 0
```

is safer because it keeps the non-additive inverse implicit in the denominator.

## 5. Verdict

Feshbach is not the proof. It is the correct coordinate system.

The one remaining valid attack is:

```text
prove the first-variation functional is small in the actual Feshbach graph norm.
```

Not:

```text
factor the resolvent,
sum local inverses,
or infer endpoint convergence from scalar determinants.
```

If Phase 72 can prove the reduced variational estimate without those three mistakes, it is genuinely
new relative to Phase 65. If it cannot, it collapses back to D8.5b / endpoint identification.

