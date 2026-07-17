# Lemma 2.3.F — what it is, everything we tried, and where the wall is

*A briefing to request a new route. Honest throughout: no proof reached; every claimed positive
result is marginal/detector-grade and is flagged as such.*

---

## 1. The statement of 2.3.F

Let `λ > 1`, `L = 2 log λ`, and let `QW_λ` be the (Connes–Moscovici / prolate-type) quadratic form
of the explicit formula compressed to the window `[0,L]` in the Fourier basis `e_n = e^{2πi n y/L}`,
`n = −N..N`. Concretely the Weil matrix is

```
    A_λ = L_arch − L_prime ,     A_λ[m,n] = ⟨e_m, (archimedean − Σ_p Λ(·)/√· ) e_n⟩ ,
```

with the prime sum truncated at `n ≤ λ²` (the support set by the ground state `u₀`).

**Lemma 2.3.F (the shorted-Dirichlet quotient lemma).** After Doob conjugation by the positive
ground state `u₀` (which exists unconditionally at finite λ by Perron–Frobenius, our Theorem 2.2),
the quotient form `G_λ` has, on its near-radical, the spectrum of the Dirichlet Laplacian `−∂_θ²` on
an interval, i.e. the eigenvalue ratios converge to `(k+1)²`. Equivalently: the intrinsic
tridiagonal (Jacobi) form of `G_λ` has a **bounded** band edge giving the `(k+1)²` ladder.

This is **the single remaining non-RH item** in our proof chain (Steps 1–12); everything else is
proven unconditionally. 2.3.F and "the wall" (Step 12, `ε₀(λ) ≥ 0 ∀λ ⟺ RH`) share one core.

---

## 2. The reduction we *did* prove (so the target is sharp)

**R1 (proven, RH-neutral).**
`2.3.F  ⟸  2.3.F-Loc  ⟸  three lemmas on the intrinsic Jacobi of G_λ`, of which the only open one is

> **(L1) Boundedness.** `sup_λ max_{i,j} |A_λ-intrinsic-Jacobi coefficient| < ∞`, uniformly in λ.

The Doob conjugation by `u₀` separates **FORM** (the `(k+1)²` ratios — these we get) from **SIGN /
SCALE** (the boundedness — this is the wall). Numerically the Doob step is validated (E70: the local
2nd-order form is flat; the `(k+1)²` ladder is reproduced; the Davenport–Heilbronn falsador breaks
it). So **2.3.F is now equivalent to L1**, a single uniform-boundedness statement.

**The precise analytic decomposition of L1.** By the explicit formula, each coefficient splits as
```
    A_λ[m,n]  =  A^smooth_λ[m,n]   +   A^osc_λ[m,n]
    A^smooth  =  archimedean  −  ∫ (PNT main term)        ← bounded, smooth in λ  (OK, via PNT)
    A^osc     =  − Σ_ρ  ĝ_{m,n}(ρ, λ)                     ← sum over the zeros ρ of ζ
```
So **L1 ⟺ the zero-sum term `A^osc_λ` is bounded uniformly in λ.** That term is exactly where every
attack has died. (A pointwise-in-λ bound on `A^osc` grows like `log³λ` until the oscillation of the
zeros cancels it — and that cancellation is RH-grade.)

---

## 3. Everything we tried, and the exact failure mode of each

We group by idea. Every test carries the DH (Davenport–Heilbronn) falsador as a control: DH has
off-line zeros and **must** fail any genuine mechanism — it always does, which is what tells us our
quantities are faithful detectors of RH (and hence why proving them is RH-hard).

### A. Direct / pointwise bounds on `A^osc` (Phases 60–61, attempts R3–R10)
- **Tried:** bound the coefficient, the eigenvalue, the heat trace, perturbations — all *pointwise
  in λ*.
- **Failed because:** `A^osc_λ` oscillates arithmetically with λ (the prime echo in the band
  `L = 2 log λ`). A pointwise bound requires cancellation among the zeros = the wall. R10's honest
  correction: the fluctuation term is literally `Σ_ρ(...)`, growing until zero-oscillation tames it.

### B. Cesàro / log averaging in λ (Phase 62, C1 — NG-62)
- **Idea:** don't bound `A^osc_λ` pointwise; average over λ. The hope (our O11): the average of the
  zero-sum → 0 by **unconditional** zero-density `N(T) ~ (T/2π) log T`, no zero locations needed.
- **Failed because:** a zero `ρ = β + iγ` contributes `λ^{2β−1} · λ^{2iγ}`. On the line (`β = ½`)
  this is a pure oscillation that Cesàro-averages to 0. **Off the line it is secular growth
  `λ^{2β−1}` that no average removes**, and density estimates bound the *count* and the *imaginary
  parts* of zeros, never the *real parts*. So Cesàro convergence of the coefficients is
  **RH-equivalent**, not RH-neutral. Confirmed numerically: ζ's band width is flat/bounded; DH's
  grows as a positive power of λ (the off-line signature).
- **Side finding:** the `(k+1)²` (or shifted `k(k+2)`) ladder is **not** a discriminator — DH
  reproduces it *better* than ζ. The ladder is generic period-2 Dirichlet geometry, not arithmetic.
  So "the averaged Jacobi gives the ladder" cannot be the content of 2.3.F.

### C. Quaternionic Hodge–Riemann polarization (Phase 62, E92–E96 — NG-62b)
- **Idea:** realize positivity intrinsically. With the Deninger complex structure `J` (`J² = −1`,
  `J e_n = sgn(n) e_{−n}`), test whether `A_λ` is a polarization, i.e. positive on the +i-eigenspace
  `V₊` of `J`.
- **Found (genuinely):** `A_λ` **is positive semidefinite on V₊ for ζ at every λ**, while the DH
  falsador *and* a symmetry-matched random control are both **indefinite**. This is the clearest
  intrinsic appearance of Weil/Hodge–Riemann positivity we have produced, and it is not trivially
  algebraic.
- **Failed because:** it is **gapless**. The V₊ spectrum is an exponential cascade `e^{−cL}` down to
  zero (rate ≈ 1.40 log₁₀/step, λ-independent; the positivity is intrinsic, not a cancellation
  artifact). Reformulating `A|V₊ ⪰ 0` as `max μ(L_prime, L_arch) ≤ 1`, ζ sits **exactly at
  μ_max = 1** (marginal, with many μ piling at 1 from below) while DH is at 6–13. So it is a
  faithful but **gapless marginal detector** = the wall again.

### D. The realization frontier: is there a Frobenius? (Phase 63 — NG-63)
The function-field proof of RH needs a **Frobenius**: a `J`-**linear** endomorphism (a morphism of
the Hodge structure) that is an **isometry of a positive-definite, gapped polarization**; positivity
then forces its eigenvalues onto `|z| = √q`. We tested whether the Spec-ℤ analog exists on the window.

- **R1.** The Connes scaling operator `H_x` (whose spectrum reproduces the zeros — validated:
  eigenvalue 14.105 vs γ₁ = 14.135 at λ = 11) is built from the scaling generator
  `D_log = diag(2πn/L)`. We found **`D_log` anti-commutes with `J`** (exactly:
  `‖[D_log,J]‖/‖D_log‖ = 2.000`; its symbol `2πn/L` is *odd* in n). So it is complex-**antilinear**
  — the **wrong type** to be a Frobenius (which must be `J`-linear). The zeros live in the antilinear
  sector; the polarization's positivity lives in the linear sector.
- **R3 (F_q positive control).** For real elliptic curves over `F_q`, Frobenius `F = √q·R(θ)` in the
  Hodge basis **commutes with `J`** (`[F,J] = 0` exactly), is a similitude of a **positive-definite,
  gapped** polarization, and its eigenvalues are **exactly on `|z| = √q`**. Both ingredients the
  curve proof needs are present there and *both* absent on the ζ window.
- **R6 (squaring).** Since `D_log` is antilinear, `D_log²` is `J`-linear (spectrum `γ²`,
  `RH ⟺ D_log² ⪰ 0`). So squaring moves the zeros into the `J`-linear sector. **But that sector is
  equally gapless** — ζ's polarization is PSD but gapless in *both* the `J`-linear (even) and
  antilinear (odd) sectors. Squaring does not escape the wall.

---

## 4. The sharpest statement of the obstruction (where we are now)

Combining C, D-R3 and D-R6 gives a structural reason the wall is unmovable by these means:

> **A spectral gap requires finitely many eigenvalues.** A curve over `F_q` has finite genus `g`:
> `H¹` is `2g`-dimensional, Frobenius is a finite matrix, and the polarization is positive-definite
> **with a gap**. ζ has **infinitely many, accumulating zeros** (`N(T) ~ (T/2π) log T`), so the
> polarization's positivity margin → 0 as the window grows. **The gaplessness is the analytic shadow
> of Spec ℤ having "infinite genus".**

Equivalently, in terms of L1: the bounded part `A^smooth` is controlled by PNT; the obstruction is
entirely the zero-sum `A^osc`, and *every* way we have found to make `A^osc` bounded/positive is
exactly as strong as RH, because the only thing that tames it is the zeros being on the line.

---

## 5. The questions we would like a route for

1. **Is there a Doob/Jacobi-intrinsic proof of L1 that is genuinely RH-neutral?** I.e. can
   `sup_λ ‖A^osc_λ‖ < ∞` be obtained from the prime/archimedean side (Euler product, functional
   equation) without any input on zero locations? Our decomposition isolates `A^osc` as the only
   open piece; we could not bound it without zero cancellation.

2. **Is the gaplessness avoidable, or must one pass to a regularized positivity?** Over `F_q` the gap
   is finite-genus. For ζ should one work with a **regularized determinant / regularized polarization**
   (Deninger) where "positivity with a gap" is replaced by a zeta-regularized statement — and if so,
   what is the correct finite-window analogue we should be testing?

3. **Is there a `J`-linear operator on the window whose spectrum is the zeros?** We showed the natural
   scaling generator is antilinear and its square lands in an equally-gapless sector. Is there a
   different, genuinely `J`-linear (Hodge-morphism) operator carrying the zeros — the true Frobenius
   analogue — or is its non-existence on the window provable (and is that non-existence exactly MW-5)?

4. **Does the marginal certificate `max μ(L_prime, L_arch) = 1` have a meaning** in the CCM / arithmetic-site
   framework that we are missing — e.g. is `μ_max = 1` the shadow of a Riemann–Roch / index identity
   that, properly set up, *forces* the bound rather than merely detecting it?

---

## 6. What is solid (so a route can build on it)

- Steps 1–12 except L1 are proven unconditionally; **2.3.F ⟺ L1 ⟺ boundedness of the zero-sum
  `A^osc_λ`** (R1 reduction, validated).
- The Doob conjugation works and **separates form from sign**; the `(k+1)²` form is reproduced.
- ζ carries an intrinsic **quaternionic Hodge–Riemann polarization** (`A ⪰ 0` on `V₊`); DH and random
  controls do not. The structure is right; only the **gap** is missing.
- The obstruction is now pinned to one precise place: a finite spectral gap cannot exist for an object
  with infinitely many accumulating zeros, so the positivity must be made **regularized /
  infinite-dimensional**, not finite. That is the route we cannot build with our finite-window tools.

*All experiments are reproducible (mpmath dps ≥ 40; DH falsador mandatory). Source: `phase-62-cesaro-closure/`
and `phase-63-lefschetz-realization/`; reductions in `phase-61-open-problems/`.*
