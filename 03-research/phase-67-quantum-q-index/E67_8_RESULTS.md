# E67.8 Results — semigroup-isometry off-diagonal test

**Date:** 2026-07-06.
**Script:** [E67_8_semigroup_offdiag.py](E67_8_semigroup_offdiag.py).
**Exact source:** `../../04-papers/P52-riemann-proof-audit/h8lab.py` (per-integer prime jet + `inv_sqrt`).

## What was tested

After retracting the E67.7 "fine line empty" no-go (the dichotomy omitted the isometric
multiplicative-semigroup structure), this test measures whether the Cuntz N^x coherent state
reproduces the *off-diagonal coherence* of the exact P52 whitened prime operator.

- Semigroup prediction (canonical Mellin coherent vector `w_m = m^{-alpha} e^{-i t0 log m}`):
  ```
  rho_mod[a,b] = (gcd(a,b)^2/(a b))^alpha * (b/a)^{i t0}   (zeta-free after normalization).
  ```
  Magnitude depends ONLY on divisibility (coprime cofactors a/gcd, b/gcd).
- Exact prediction: whitened per-integer contribution `t_a = A_N^{-1/2} pick_jet(h_{P,a}) A_N^{-1/2}`,
  `rho_exact[a,b] = <t_a,t_b>_F / (||t_a|| ||t_b||)`.

## Numbers (t0=100, y=1, N=6, prime powers <=33)

```
complex   offdiag_error = 0.75   (alpha*=0.22, sign=-1)
magnitude offdiag_error = 0.60
phase tracking          = 0.66   (1 perfect, 0 random)
```

Phase partly tracks `t0*(log b - log a)` (both channels carry `(b/a)^{it0}`), confirming the setup is
sane. Magnitude does not match.

## Decisive diagnostic

`|rho_exact|` is governed by **log-distance** `Delta = log b - log a`, not by gcd:

| pair  | gcd | Delta | \|rho_exact\| | \|rho_mod\| |
|-------|-----|-------|-------------|-----------|
| (4,5) | 1   | 0.22  | 0.93        | 0.51      |
| (2,3) | 1   | 0.41  | 0.90        | 0.67      |
| (4,9) | 1   | 0.81  | 0.68        | 0.45      |
| (5,25)| 5   | 1.61  | 0.38        | 0.70      |
| (3,27)| 3   | 2.20  | 0.24        | 0.61      |
| (2,32)| 2   | 2.77  | 0.076       | 0.54      |

Two inverters falsify the divisibility-coherence hypothesis:
- **(4,5)** coprime but close in log: exact strongly coherent (0.93), semigroup predicts weak (0.51).
- **(2,32)** share factor 2 but far in log: exact incoherent (0.076), semigroup predicts strong (0.54).

At fixed `Delta=0.69`, gcd gives only a weak secondary modulation
(`(2,4),(4,8),(8,16),(16,32)`: 0.785, 0.827, 0.870, 0.890).

## Verdict

**Semigroup cross-terms are real but carry the WRONG coherence.**

- The isometric cross-terms `s_p^* s_q` are nonzero and do encode a genuine, zeta-free divisibility
  coherence. The E67.7 no-go retraction was correct: the mechanism exists.
- But `P_lambda`'s off-diagonal coherence is **archimedean log-distance**, not divisibility. This is
  structural, not an `alpha`-tuning issue: `omega(s_a^* s_b)` depends only on the coprime cofactors, so
  a canonical Mellin weight cannot produce a smooth `log b - log a` dependence. Forcing it requires
  engineering `w_m`, i.e. fitting = the circularity Phase 67 forbids.

Consequence: the RH-carrying interference lives in the archimedean/Mellin channel (= Omega_7). The
multiplicative-semigroup channel supplies a real but lateral coherence that is not the one `P_lambda`
uses. The semigroup coherent-state mechanism is empirically falsified as THE source of QSC-contract.

## Residual open question (honest)

This falsifies the *canonical Mellin coherent state* on the semigroup algebra. It does not prove that
*no* state on the multiplicative-semigroup C*-algebra carries log-distance coherence — but any such
state must produce `log b - log a` (archimedean) rather than the intrinsic divisibility invariant, and
no canonical semigroup state does this without an engineered weight. Absent such a state, Phase 67-iso
folds back to the archimedean/Omega_7 channel.
