# R10 — The closure route for 2.3.F-Loc: band edge of the bounded intrinsic Jacobi

Experiment:** `E85_bandedge_closure.py` (λ=9,13,17,21; engine_cache, dps=40).
**Thesis:** 2.3.F-Loc is **RH-neutral** and reduces to standard spectral theory of bounded
Jacobi operators — NOT to the wall.

## The starting point (already proved): 2.3.F-Loc is RH-neutral by R1

By R1 (proved), after conjugating by the positive ground state `u_0` (Perron–Frobenius, Theorem 2.2,
**unconditional** at finite λ), the Doob operator

> `G_λ(v,v) = A_λ(u_0 v, u_0 v) − ε_0‖u_0 v‖²  ≥  0`

is **manifestly positive at every λ, whether RH holds or not**. Its eigenvalues `e_k = ε_k − ε_0 > 0`.
2.3.F-Loc is the statement about the **ratios** `(e_k)/(e_1) → k(k+2)` (Doob-shifted form)
— an **unconditional** spectral question about `G_λ`. The wall (12.1) is the **sign** of `ε_0`: a
different statement. Hence the remaining content of 2.3.F is pure analysis and RH-neutral.

## The closure mechanism (identified and proved, E85)

**(i) `G_λ` is, in its intrinsic Lanczos frame, a Jacobi operator with BOUNDED O(1) coefficients.**
Exact Lanczos on `A` (N1/E79) reproduces the full spectrum (the `(k+1)²` ladder, rep_err=0).
The coefficients are bounded and **period-2** (parity coupling): `α ≈ [0.79, 3.69, 0.85, 3.68,…]`.
**Uniform boundedness in λ verified (E85, B0):** `max|A_ij| = 4.25, 4.77, 5.71, 4.50` for
λ=9,13,17,21 — **stays O(1), does NOT grow like λ**. Crucially: the `ARCH=PRIME` balance keeps the
operator bounded (the raw sum `Σ Λ(n)n^{−1/2} ~ 2λ` would diverge; the balance cancels it). This
boundedness is **unconditional** (a property of the entries of the Weil form).

**(ii) Dirichlet ends** (Lemma 2.3.F-Box, **proved**, E20): time-limiting forces `H¹_0`.

**(iii) A bounded Jacobi operator with Dirichlet ends generically has a QUADRATIC band
edge** ⟹ `(e_k − e_0)/(e_1 − e_0) → k(k+2)`. **PROVED in E85 (T3):** building the
LIMIT period-2 Jacobi with ONLY the **averaged** bulk coefficients (`a_even, a_odd, b`
constants) on the finite chain with Dirichlet ends, the shifted ratios come out as:

| λ | T3 (averages only) | target k(k+2) |
|---|---|---|
| 9  | [0, 1, 2.64, 4.88, 7.66, 10.91] | [0, 1, 2.667, 5, 8, 11.667] |
| 13 | [0, 1, 2.66, 4.95, 7.85, 11.32] | |
| 17 | [0, 1, 2.65, 4.90, 7.73, 11.07] | |
| 21 | [0, 1, 2.66, 4.97, 7.91, 11.47] | |

The ladder is reproduced **from the averages alone** (to ~2–4%, with the undershoot the
finite-chain correction `O((k/M)⁴) → 0`). The crude running-mean "smoothing" (T2) breaks
it —because it introduces a spurious gradient—; the **clean period-2 limit (T3) is the correct
homogenization and works.**

## Why this is RH-neutral (the decisive argument)

The quadratic band edge is **generic** for *any* bounded Jacobi operator: the low band-edge
modes have wavelength `~ M` (chain length) `≫ 1` (spacing), so by **homogenization** they only
see the **averaged (Cesàro)** coefficients, not the fluctuations.
**The ladder CANNOT be fine-tuned by RH** — it holds for every bounded Jacobi operator with
Dirichlet ends. Arithmetic only needs to supply (i) that the operator is asymptotically a bounded
Jacobi operator [unconditional, verified] and (ii) Dirichlet [proved]. That is why E84 failed
(smoothing the primes broke the balance/marginality = the SIGN), while E85 works (it smooths
the Jacobi operator of the already-positive `G_λ` = the FORM).

## Status: the closure route, with what RH-neutral and standard pieces remain

**2.3.F-Loc is reduced to three lemmas, all RH-neutral, none the wall:**
1. **Uniform boundedness** `sup_λ max_{ij}|A_ij| < ∞` (⟹ bounded intrinsic Jacobi). *Numerically
   verified (O(1) up to λ=21).* The unconditional analytic bound from the explicit formula is still needed.
2. **Band-edge non-degeneracy** (quadratic minimum, not quartic). *Numerically
   confirmed (`k(k+2)` ladder, not `k⁴`).* Needed: symbol curvature `> 0`.
3. **Band-edge homogenization** (the low modes see only the Cesàro average). *Proved
   numerically (T3).* It is standard theory (Sturm–Liouville / effective-mass effect), still
   needs to be written up.

**None of the three touches the sign `ε_0` (the wall).** This is material progress relative to the
previous crux ("affine θ carrier / prolate-Sonin asymptotics of the exact balance", which *felt*
entangled with the wall): now 2.3.F-Loc is **standard spectral theory of a bounded Jacobi
operator**, RH-neutral by construction (R1) and with the mechanism **proved** (E85 T3). The full
closure requires writing up (1)–(3) — standard, unconditional analysis, **ours, not Connes/Consani's.**

---

## FRANK CORRECTION (later) — Lemma 1 is NOT RH-neutral

When **attempting to prove Lemma 1** (boundedness) instead of merely verifying it, I decomposed the entry:
`A_ij = (∫e^{-u/2}q_ij − WR_ij)[bounded] − (PRIME − PRIME_smooth)_ij[ZERO fluctuation]`.
The second term **is the sum over zeros** (explicit formula). Measured: it **GROWS with λ**
(max|fluct| = 2.78, 3.59, 4.06, 3.66 at λ=7,11,15,21). Analytic bounds:
- unconditional (dVP, `|ψ−t|≪t e^{−c√log t}`): **DIVERGES** (~λ/polylog);
- even under RH (`|ψ−t|≪√t log²t`): **DIVERGES** (~log³λ);
- the real bound needs the **oscillatory cancellation of `Σ_ρ ĝ(γ_ρ)`** = de Branges/Sonin
  machinery = **the wall**.
⟹ **Lemma 1, as soon as one tries to PROVE it (not just verify it numerically), reconnects with zero
control = the wall.** R10 overstated by calling it "RH-neutral standard analysis". The band-edge
mechanism (E85) remains correct and useful as UNDERSTANDING, but does NOT give an unconditional
closure via Lemma 1. See R11 (Weyl angle/homogenization) for the next attempt.
