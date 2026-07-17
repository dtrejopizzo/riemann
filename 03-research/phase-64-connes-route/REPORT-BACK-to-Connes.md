# Report back: results from your route for 2.3.F / L1

*Following your four-task program. Honest throughout: no proof reached; every positive result is a
faithful but RH-equivalent detector, flagged as such. All experiments reproducible (mpmath dps≥30–40;
Davenport–Heilbronn falsador mandatory in every test).*

---

## Executive summary

Your reclassification is **confirmed end-to-end**: L1 is not a lemma below RH, it is an RH criterion,
and finite-window positivity is **edge-contractivity / a Herglotz–inner condition**, not a spectral
gap. Of the four tasks: **A confirmed, B confirmed, D proven, C's crossing object validated on the
genuine ζ.** What remains is exactly the one thing numerics cannot supply: the construction of the
**Euler-product/adelic unitary colligation** realizing the Schur function. Our question to you is
about how to build (or characterize) that colligation.

---

## Task A — the Laplace-pole theorem: L1 ⟹ RH (confirmed)

We accept the reclassification. The detector-nonvanishing hypothesis — every off-line zero is seen by
some intrinsic-Jacobi coefficient — is numerically confirmed on the **stable bulk functionals**
(individual Lanczos coefficients are too noisy):

| growth exponent of `log|·|` vs `t=log λ` | ζ | DH (off-line zeros) |
|---|---|---|
| `beta_bulk_mean` | **−0.26** (bounded) | **+0.40** (grows) |
| `alpha_bulk_mean` | **−0.04** (bounded) | **+0.45** (grows) |

ζ's coefficients are bounded (L1 holds, RH-consistent); DH's grow at ≈ `2β−1` for its off-line zero.
This is exactly your Laplace-pole obstruction made visible: the off-line zero is a pole at `2ρ−1`
(`Re>0`), and no averaging/soft method removes it. **We now treat L1 as RH-strength**, and we no
longer attempt to bound `A^osc` coefficientwise.

*Open (for you):* the clean analytic statement of detector-nonvanishing
(`∀ρ, Re ρ>½, ∃a∈𝒥: C_a(ρ)≠0`) — is this provable from the completeness of the Jacobi family, or
does it need an input we are missing?

---

## Task B — relative determinant / edge contractivity (confirmed)

You predicted: replace the (impossible) gap by a relative determinant; ζ bounded, DH drift `λ^{2β−1}`.
We found the **bulk** relative determinant is dominated by the gapless `e^{−cL}` cascade
(uninformative — both drift). The **edge** of the generalized spectrum `L_prime x = μ L_arch x` is the
right object (your finite part at `z=1`). Model-free result (λ=9..21):

| | ζ | DH |
|---|---|---|
| `μ_max` | **1.000 – 1.031** | **7.6 → 10.7 (drifts)** |
| mass past the contractive edge `μ=1` | **≈ 0** | **26 → 53 (grows)** |
| complex `μ` (off-line modes) | **0** | **present** |
| edge drift | contractive, bounded | **`(μ_max−1) ~ λ^{0.43}`** |

So ζ's spectrum is **edge-contractive** (`μ_max=1`, no mass past the edge — your `‖K‖=1` boundary
identity, here as "no off-line poles"); DH spills past the edge with complex modes and the predicted
**`λ^{2β−1}`** drift (β≈0.72). This realizes your "positivity = boundary contractivity" picture exactly.

*Caveat:* the `L_arch^{−½}` factorization is obstructed on the window — **`L_arch` is not PD** there
(ζ: 9 negative eigenvalues of 37; DH: 36 of 37). The generalized-eigenvalue form sidesteps it, but it
suggests the correct positive reference is the true archimedean Plancherel form, not the finite-window
`L_arch`. *Is that the reference you intend for `K_λ`?*

---

## Task D — parity no-go (proven)

For a window Fourier multiplier `M_a e_n = a_n e_n` with `J e_n = sgn(n) e_{−n}` (`J²=−1`):
`[M_a,J]=0 ⟺ a_n` even; `{M_a,J}=0 ⟺ a_n` odd. The scaling generator `D_log` has symbol `2πn/L`
(odd) ⟹ `D_log J = −J D_log` (exact: `‖[D_log,J]‖/‖D_log‖ = 2.000`). So it is complex-**antilinear**;
any **J-linear** operator has even symbol and sees only `D_log²`, `γ²`, `|γ|`. **No first-order
J-linear (Frobenius-type) zero operator exists on the Fourier window.** We have stopped trying to make
`D_log` itself a Frobenius; per your guidance the true object must be the J-unitary canonical-system /
transfer object, not the scaling generator.

---

## Task C — the colligation/Herglotz crossing object (validated on the genuine ζ)

The finite window is "too positive" to discriminate (any self-adjoint Jacobi gives Herglotz `m`,
Schur `S`, `H⪰0` for **both** ζ and DH; ζ's canonical Hamiltonian is merely *marginally degenerate*,
min block eig `~1e-20`, sitting exactly at the de Branges boundary). So we tested your criterion on the
**actual** function. With `Ξ(z)=ξ(½+iz)`, `φ(z)=Ξ'/Ξ = Σ_ρ 1/(z−t_ρ)`:

> **RH ⟺ φ is Herglotz** (`Im φ ≤ 0` for `Im z>0`) ⟺ `S=(φ−i)/(φ+i)` Schur/inner.

| test (mpmath, ~15 zeros, UHP grid) | max `Im φ` | reading |
|---|---|---|
| **(0) archimedean + pole part only** | **+0.98 — FAILS** | the base is **not** Herglotz alone |
| **(1) full ζ** (arch + ζ′/ζ) | **−0.009 — Herglotz** | RH-consistent; **the on-line zeros restore it** |
| **(2) ζ + one planted off-line zero** | **+9.55 — FAILS** | the criterion **detects** off-line zeros |

The criterion is therefore **faithful and falsifiable**, and — crucially — **not** a trivial
archimedean positivity: the archimedean/pole part alone is *not* Herglotz; it is precisely the zeros
lying on the critical line that make the total `φ` Herglotz. This is the correct
infinite-dimensional inner/colligation object — the one the finite window could not exhibit. It
remains RH-equivalent: proving `φ` Herglotz for all heights *is* RH.

---

## Where this leaves us (and our questions)

Everything testable confirms your route. The single remaining step is the one you named: realize the
Schur function `S_λ` (equivalently, prove `φ=Ξ'/Ξ` Herglotz) from an **Euler-product / adelic unitary
colligation**, where contractivity is forced by Hilbert-space geometry and the falsifier DH fails for
lack of that colligation. We cannot construct it numerically. Concretely we would like your guidance on:

1. **The colligation.** Is there a canonical construction of a unitary colligation (Lax–Phillips
   scattering system on the adele class space) whose characteristic/transfer function is `S_λ`, with
   the **local Euler factors** as the passive building blocks? What is the state space, and what plays
   the role of the incoming/outgoing subspaces?

2. **The positive reference for `K_λ`.** Since the finite-window `L_arch` is indefinite, should `K_λ`
   be built against the **archimedean Plancherel form** (the positive operator `Re ψ(¼+it/2)−log π`
   in frequency)? If so, the relative determinant `det₂((I−zK)(I−zK⁰)^{−1})` would be against a
   genuinely positive reference — is that the intended object, and what is the right model `K⁰`?

3. **From contractivity to no-pole.** Our marginal certificate is `μ_max=1` (boundary norm-one). You
   noted this is an index/norm-one statement, not coercivity. **What is the regularized mechanism (a
   Riemann–Roch / index identity, or scattering unitarity) that upgrades boundary contractivity to the
   absence of poles in `Re w>0`?** This is the precise gap: we have `‖K_λ‖→1`, and we need that the
   approach to the boundary contains no off-line spectrum.

4. **Detector-nonvanishing (Task A).** Is `∀ρ (Re ρ>½) ∃a∈𝒥: C_a(ρ)≠0` provable from completeness of
   the intrinsic-Jacobi family, closing `L1 ⟹ RH` rigorously?

We are ready to test any concrete construction you propose against the same machinery (DH falsifier,
edge-contractivity, Herglotz `φ`) at dps≥40.

*Files:* `phase-64-connes-route/` (E100 Task A, E101 Task B, E102/E103 Task C, RESULTS.md);
reduction in `phase-61-open-problems/`; the prior briefing in
`phase-63-lefschetz-realization/BRIEFING-2.3.F-for-Connes.md`.
