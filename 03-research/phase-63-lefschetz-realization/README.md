# Phase 63 — The MW-5 Realization Frontier: the missing Lefschetz operator

**Status:** open · no proof reached · started 2026-06-26 · road chosen by David after Phase 62 closed.

## Where we are

Phase 62 confirmed, from three independent sides (Cesàro, quaternionic Hodge–Riemann, Euler/μ),
that the finite-window Weil matrix of ζ carries the **right positive structure** — `A` is positive
semidefinite on V₊ (the +i eigenspace of the quaternionic `J`, `J²=−1`) — but only **gaplessly /
marginally** (`max μ(Lprime,Larch)=1` exactly; cascade `e^{−cL}` to zero). That gapless margin is
the master wall (`ε₀(λ)≥0`, Step 12). See [phase-62 CROSSING-ATTEMPT.md](../phase-62-cesaro-closure/CROSSING-ATTEMPT.md).

The diagnosis (MW-5): we **have** the polarization data `(A, J)`; what we **lack** is what turns a
polarization into a *Hodge index theorem with a gap*. In every case where RH-type positivity is a
theorem — curves over `F_q` (Weil), Kähler manifolds (Hodge) — the gap is forced by a **Lefschetz
operator `L`** generating an `sl₂` action with **Hard Lefschetz**. Over `F_q` that operator is the
Frobenius/hyperplane class; over Spec ℤ there is no such operator (no Weil cohomology). **That
absence is MW-5, and it is concretely testable on our matrices.**

## Thesis of Phase 63

> The gap missing from the V₊ positivity is exactly the gap that a Hard-Lefschetz `sl₂`-triple
> `(L, Λ, H)` would force. Find whether such an operator exists for ζ's `A` (→ would cross the
> wall), or prove it cannot exist over Spec ℤ as it does over `F_q` (→ pins MW-5 precisely).

## Steps (testable, falsador-disciplined, no false victory)

| step | question | method |
|------|----------|--------|
| **R1** | Is the scaling/Frobenius operator (spectrum=zeros) a polarized isometry / Hodge morphism? | **DONE** — [R1-VERDICT.md](R1-VERDICT.md): the scaling generator **anti-commutes** with `J` (exact, ratio 2.000) → it is complex-**antilinear**, the *wrong type* to be Frobenius. Operator-level MW-5. ([E97](E97_polarized_isometry.py) crude attempt inconclusive, [E97_RESULTS.md](E97_RESULTS.md)) |
| ~~R2~~ | ~~Hard Lefschetz gap~~ | reframed: for weight-1 (curve) there is no within-H¹ Lefschetz; the operator is Frobenius (R1), not L |
| **R3** | F_q positive control: does the curve case pass the same test (J-linear Frobenius + gapped polarization)? | **DONE** — [R3-VERDICT.md](R3-VERDICT.md): yes, exactly. 3 real curves: `[F,J]=0`, PD gapped polarization, `|eig|=√q` exact. Contrast with ζ confirmed. |
| **R5** | verdict + conclusion | **DONE** — Phase 63 closed; sharpened MW-5 (see below) |

## Phase 63 — CLOSED. MW-5 made precise; no crossing within reach of numerics.

**Result (R1 + R3):** the function-field proof needs two ingredients — a **J-linear Frobenius**
(Hodge morphism) that is an **isometry of a positive-definite (gapped) polarization**. R3 confirms
real curves over F_q have both exactly (`[F,J]=0`, polarization PD with gap, `|eig|=√q`). R1 shows
the ζ window has **neither**: the scaling operator (spectrum=zeros) **anti-commutes** with J
(antilinear, ratio 2.000 exact) and the polarization is **gapless** `e^{−cL}` (Phase 62). These are
two faces of one absence — **no J-linear Frobenius isometry of a gapped polarization on the ζ
window**. That object would be the Frobenius of the Connes–Consani arithmetic site / Deninger
cohomology, which is not a realized object: this is **MW-5, now stated and demonstrated by direct
contrast**. No proof of RH; the obstruction is exact and located.

### R6 (E99) — the squaring lever, and the deepest statement of the wall

Pushed further: since `D` is antilinear, `D²` is J-linear (spectrum `γ²`, `RH⟺D²⪰0`), so squaring
moves the zeros into the J-linear sector. **Tested whether that sector is gapped — it is not**
([E99_RESULTS.md](E99_RESULTS.md)): ζ's polarization is PSD but **gapless in both** the J-linear
(even) and antilinear (odd) sectors (relgap ~1e-12). The gaplessness is sector-independent. Working
out why gives the program's sharpest statement of the wall:

> **A spectral gap needs finitely many eigenvalues.** A curve over F_q has finite genus `g` (Frobenius
> = a `2g×2g` matrix, polarization PD with a gap). ζ has **infinitely many, accumulating** zeros
> (`N(T)~(T/2π)logT`), so its polarization margin → 0 as λ grows — **gaplessness is the analytic
> shadow of Spec ℤ having "infinite genus".** The crossing needs an honestly infinite-dimensional
> *regularized* positivity (Deninger regularized determinants), not a finite gap — a theory problem
> beyond numerics.

Per David's plan, the program stops here on this frontier — now with the obstruction pinned not just
as "MW-5" but as the structural impossibility of a finite gap for an object with infinitely many zeros.
| **R3** | `F_q` positive control: build the analog for a curve `ζ_C/F_q`; confirm `L`=Frobenius gives the gap (HL = the proven `F_q` RH). | construct `A` for a known curve; verify gap present where it must be |
| **R4** | Contrast: show precisely *which* property of `L` exists over `F_q` and is obstructed over Spec ℤ. | the sharp MW-5 statement |
| **R5** | Verdict + writeup. If R1–R2 cross → RH route; if R3–R4 only pin the obstruction → sharpened MW-5, hand to experts. | honest |

## Guardrails (unchanged)

dps ≥ 40; **DH falsador mandatory** in every test (must NOT admit a gap-forcing `L`); `F_q` control
is the *positive* control (must admit one); no "RH proved" claim until R1+R2 close with a real gap
and a non-circular `L`; a false victory is worse than failure (`[[riemann-anti-self-deception]]`).
Reuse the phase-61 engine (`engine_cache.py`, `.cache_23F/`) via path shim, as in phase-62.

## Why this is the right frontier (not more brute force)

Phase 62 showed the window keeps returning the same gapless wall under *form-level* reformulations.
The Lefschetz operator is an *operator-level* structure that does not appear in any form-level
test — it is the one ingredient the program has not yet searched for directly, and it is exactly the
ingredient that makes positivity a theorem elsewhere. It is also the concrete shadow of the
Connes–Consani arithmetic-site / Deninger-cohomology object (`[[riemann-phase61-deninger-quaternionic]]`,
Phase 10 "cohomological turn").

## First action

**R1 — `E97_lefschetz_search.py`:** on ζ's `A` (and J from phase-62 E94), search for a Lefschetz
operator `L` and test the `sl₂` relations + Hard Lefschetz, with DH as falsador and (R3) an `F_q`
curve as positive control.
