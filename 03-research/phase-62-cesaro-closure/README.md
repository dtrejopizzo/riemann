# Phase 62 — Cesàro Closure of 2.3.F

**Status:** open · no proof reached · started 2026-06-26

## Goal

Advance the last non-RH item in the proof chain, **Lemma 2.3.F** (the shorted-Dirichlet
quotient lemma: the intrinsic Jacobi of the Doob-conjugated operator `G_λ` has a bounded
band edge giving the `(k+1)²` ratios). All pointwise-in-λ attacks (Program 10, R3–R10) died
on the same obstacle: the residual `e^{−cL}` oscillates arithmetically with λ and bounding it
pointwise touches the wall. Phase 62 tests the escape flagged as **O11** in
[phase-61 OPEN-PROBLEMS](../phase-61-open-problems/OPEN-PROBLEMS.md): **average over λ** (Cesàro),
where the zero-sum fluctuation washes out by *unconditional* zero-density (no RH needed).

## Steps

| step | what | status |
|------|------|--------|
| **C0** | numerical gate: does the Cesàro-averaged intrinsic Jacobi of `G_λ` converge for ζ and reject the DH falsador? | **DONE** — [E90_RESULTS.md](E90_RESULTS.md) |
| **C1** | analytic: decompose `b_bulk(λ) = smooth + oscillatory`; can the Cesàro average of the oscillatory part → 0 *unconditionally*? | **DONE — NO-GO** — [C1-ANALYSIS.md](C1-ANALYSIS.md) (frame confirmed [E91_RESULTS.md](E91_RESULTS.md)) |
| ~~C2~~ | ~~identify Cesàro limit with period-2 symbol~~ | **withdrawn** (assumed C1 closed) |
| ~~C3~~ | ~~lift to CvS Thm 5.10~~ | **withdrawn** |
| **C4** | verdict + writeup; update NO-GO-LIST / OPEN-PROBLEMS | **DONE** |

## Phase verdict (2026-06-26): NO-GO for the Cesàro route, with insight

**Cesàro-in-λ does not make 2.3.F / the boundedness L1 RH-neutral.** The zero-sum's Cesàro
average converges **iff** zeros lie on the line: off-line zeros contribute `λ^{2β−1}` *secular
growth*, which zero-density estimates (which bound counts and imaginary parts, not real parts)
cannot remove. So the boundedness of ζ's `b_bulk` is RH-equivalent at this step — averaging
relocates the wall but does not cross it. The DH falsador's observed growth is the direct
signature of off-line zeros. What survives is a **detector** (`b_bulk` bounded ⟺ zeros on line),
not a proof step. The live lever remains the geometric-positivity / Hodge route (MW-5, Phase 61),
not λ-averaging. See [C1-ANALYSIS.md](C1-ANALYSIS.md).

## Second thread — the quaternionic Hodge–Riemann lever (E92–E94)

After C1 sent us to the MW-5 positivity lever, this thread tested whether the Weil matrix `A`
carries an intrinsic **quaternionic Hodge–Riemann polarization** (Deninger object, `J²=−1`).

| script | finding |
|--------|---------|
| [E92](E92_hodge_riemann.py) (phase-61, superseded) | wrong structure (involution `Σ²=+1`); form indefinite |
| [E93](E93_quaternionic_HR.py) | with correct `J²=−1`, `AJ` is ≈antisymmetric for ζ → its symmetric part is `[A,J]/2`, tiny for ζ |
| [E94](E94_Jcompat.py) + [E94_RESULTS.md](E94_RESULTS.md) | **ζ is positive-semidefinite on V₊ (J's +i-eigenspace) at every λ; DH and random-symmetric are indefinite** |

**Result (strong, honest):** ζ's finite-window Weil matrix genuinely behaves like a *polarized
quaternionic Hodge structure* — PSD on V₊, while the off-line DH falsador and a symmetry-matched
random control both fail. The clearest intrinsic appearance of Weil/Hodge–Riemann positivity in
the program, and not trivially algebraic (random fails).

**But it lands on the master wall.** The V₊ positivity is **gapless**: the spectrum is an
exponential cascade `e^{−cL}` down to machine zero, no spectral margin (the "rank 8" was a
threshold artifact). So it is a *detector* (PSD ⟺ RH, DH fails), now known to be gapless — the
same `ε₀(λ)≥0` wall in Hodge–Riemann clothing. The lever is the **right object**; the obstacle is
located precisely as "give V₊-positivity a uniform `e^{−cL}` gap without zero locations" = the
master wall, still requiring the Spec-ℤ geometric realization (MW-5) to become a theorem.

### MW-5 crossing attempt (E95, E96) — NO-GO, see [CROSSING-ATTEMPT.md](CROSSING-ATTEMPT.md)

Tried to give the V₊ margin a prime-side gap. Findings: the cascade rate is a λ-independent
structural constant (~1.40 log10/step) and the positivity is intrinsic (no cancellation), but
`A|V₊⪰0` reformulates as `max μ(Lprime,Larch) ≤ 1`, with ζ sitting **exactly at μ_max=1**
(marginal, many μ piling at 1 from below = gapless) and DH at μ_max∈[6.4,13.5]. All three Phase-62
reformulations (Cesàro, Hodge–Riemann, Euler/μ) are **faithful but gapless marginal detectors** =
the master wall from three sides. The crossing needs the Spec-ℤ cohomological realization (MW-5);
numerics cannot manufacture it.

## Phase 62 — CLOSED. Both levers (Cesàro, Hodge–Riemann) exhausted as proof routes.

Next: a genuinely different road (new phase). The finite-window object keeps returning the same
gapless wall, so the productive frontier is the geometric realization (MW-5) or a different object,
not more brute force on the window.

## C0 result (honest, 2026-06-26)

- The **`k(k+2)` ladder is NOT a discriminator** — the DH falsador reproduces it *better* than ζ.
  It is generic period-2 Dirichlet geometry, not arithmetic. This refutes the optimistic reading
  of E85-T3 and **relocates** the content of 2.3.F.
- The **real discriminator is boundedness**: ζ's bulk band-width `b_bulk(λ)` stays bounded (~0.12,
  no growth) → L1 `sup_λ max|A_ij|<∞` holds in the average sense; DH's grows monotonically
  (1.38→2.18, `max b` linear in λ) → L1 fails, correctly rejected.
- **C1 target accordingly:** prove `b_bulk(λ) = O(1)` in Cesàro average via PNT + zero-density.

## Files

- [E90_cesaro_jacobi.py](E90_cesaro_jacobi.py) — the C0 gate. Reuses the phase-61 engine
  (`engine_cache.py`, `E70_doob_parter.py`, `.cache_23F/`) via a path shim; falsador DH mandatory; dps≥40.
- [E90_RESULTS.md](E90_RESULTS.md) — full C0 writeup and reproduce instructions.

## Honesty guardrails

dps ≥ 40; DH falsador mandatory in every test; no "RH proved" claim until C0–C3 all close;
a false victory is worse than failure. The engine and disk cache live in
[../phase-61-open-problems/](../phase-61-open-problems/) and are imported, not duplicated.
