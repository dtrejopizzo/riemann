# Phase 60 — The Discriminant: the CCM reduction program, its three-part audit, and the multiplicativity pivot

This phase contains two connected efforts. The first (the bulk of the phase, documents such as
`RH-PROOF-FULL.md`, `PRUEBA-COMPLETA-E0-E4.md`, `RH-demostracion.md`, the `E1`–`E5`/`III`–`IV` chain,
and the Connes–Consani–Moscovici "CCM" spectral-triple numerics) builds and audits a proposed reduction
of RH to the positivity of a localized Weil quadratic form realized as a Connes–Consani–Moscovici
spectral triple, following arXiv:2511.22755/23257. A three-part independent audit (files `tribunal-*`) checks every piece of the
chain line by line. The second effort (`00-PLAN.md`, `RESULTS.md`, and supporting `E1`/`E2`/`E2b`
experiments) replaces an earlier withdrawn sub-phase and tests a new, falsifiable thesis: that the sign
of the Weil residual is controlled by multiplicativity (the Euler product), isolated by contrasting ζ
with the explicit non-Euler RH-violator L_DH (Davenport–Heilbronn).

## Results
- CCM spectral-triple construction (E0) and ground-state structure (H1, Perron–Frobenius):
  verified SOLID on audit — the Weil form is exactly realized with no conflation with the true Weil
  form, and the ground state is simple, isolated, and even.
- Real-rootedness of the ground state (E1): the document's own proof attempt was REFUTED by an explicit
  counterexample; real-rootedness survives only as a mandatory CITED result (CCM Theorem 1.1(iii)), not
  as something closable at the level of entire-function lemmas in this phase.
- Approximation scaffolding (N0, N1, N2, N3, the Reduction Theorem, N5b, N5c, E3, E4): verified on audit
  SOLID (RH-neutral, i.e. unconditional), with one correction — N2's convergence horizon is SUB-CRITICAL,
  not critical (density $1 - 1/(2\log\lambda) < 1$), overturning the document's original claim.
- Reduction Theorem: RH ⟺ a single band-deficit estimate $\varepsilon_{\mathrm{loc}}(\lambda) = o(\lambda^{-1/2})$:
  verified SOLID on audit modulo E1 (a genuine localization of RH to one approximation-theory quantity,
  not circular).
- Relative-stability / limit-operator pieces (III, IV.1, IV.2): CONDITIONAL — proving a uniform spectral
  gap (H-gap) is shown to be equivalent to local RH, i.e. this part of the chain is RH-hard, not RH-neutral;
  IV.2 is correctly labeled RH-equivalent; the claim that exponent "γ=3" follows from IV.1 is downgraded
  from derived to phenomenological/numerical (the compactness of the limit operator obstructs the
  claimed derivation).
- New lemmas recorded by the audit as genuinely solid additions: a sub-case of E1 via Herglotz
  (positive-residue case), a corrected sub-critical horizon-density lemma, finiteness of the spectral gap
  at each finite λ, and confirmation of the Weil variational identity with no conflation of objects.
- First validated numerical CCM spectral triple (`CCM_VALIDATED.md`): machine-precision reproduction of
  the first ~6 nontrivial zeros of ζ from a self-adjoint realization with primes ≤ 13: NUMERICAL,
  confirming the construction's central numerical claim; the N,λ→∞ convergence needed for RH remains
  open and is identified as a pure approximation-theory problem, not a positivity problem.
- Multiplicativity discriminant thesis (δ-direction pivot): tested via three experiments (E1 zero-side
  blindness, E2 multiplicativity discriminant, E2b confound-kill). Result: NO-GO — the apparent
  Euler-vs-non-Euler separation in E2 is shown by E2b to be spurious, caused by smoothness/coherence of
  the coefficients in log n rather than by multiplicativity itself; smooth non-multiplicative controls
  match or exceed ζ's separation score. Both sides of the localized Weil form (zero side and arithmetic
  side) are shown to be blind to multiplicativity. Recorded as [NG-F1] in the program's NO-GO list;
  phase closed on this direction.

## Documents
- `00-PLAN.md`, `RESULTS.md` — the multiplicativity-discriminant program and its NO-GO closure.
- `RH-PROOF-FULL.md`, `RH-PROOF-PAPER.md`/`.tex`/`.pdf`, `RH-demostracion.md`/`.tex`/`.pdf`, `PRUEBA-COMPLETA-E0-E4.md` — the CCM reduction chain (E0–E4, III–IV).
- `tribunal-VEREDICTO.md`, `tribunal-Connes.md`, `tribunal-Consani.md`, `tribunal-Moscovici.md`, `E1-VEREDICTO-tribunal.md`, `E1proof-Connes.md`/`-Consani.md`/`-Moscovici.md`, `III-IV1-VEREDICTO-tribunal.md`, `III-IV1-Connes.md`/`-Consani.md`/`-Moscovici.md`, `Testrella-VEREDICTO-tribunal.md`, `Testrella-Connes.md`/`-Consani.md`/`-Moscovici.md` — the three-referee audits of each piece of the chain.
- `CCM_VALIDATED.md`, `N5-analytic-loewner.md`, `N5-subpieces-proved.md`, `H1_PROOF.md`, `E2-nucleo-proof.md`, `proof-E2-soft.md`, `eslabon2-soft-theorem.md`, `IV1-limit-operator.md`, `IV1-operator-identification.md`, `IV1star-relative-gap.md`, `E5_RESULTS.md`, `N5c-rh-false` and related `ESLABON2`/`MAP_2b`/`MAP_ESLABON2`/`AUDIT-repairs` files — supporting construction, proof, and audit documents for individual pieces.
- `attack-deltaV-analysis.md`, `attack-gap-a-groundstate.tex`/`.pdf`, `attack-gap-i-improved-hardy.tex`/`.pdf`, `attack-pole-deficit.tex`/`.pdf`, `audit-deltaV.md`, `objective-B-verdict.tex`/`.pdf`, `weil-remainder-attack.tex`/`.pdf`, `spectral-gap-analysis.tex`/`.pdf`, `cierre-1-CONF-landau-widom.md`, `CONSOLIDACION_L_y_eslabones.md`, `tres-problemas.md`, `III-ruta-correcta.md` — further analytic attacks on specific sub-estimates of the chain.
- `engine/`, `experiments/`, `results/` — the numerical CCM/Weil-form engine and its experiment scripts (E1–E96-range scripts referenced by the documents above).

## Relation to other phases
Builds on the Kreĭn-space/no-go results of `phase-4-handoff`/`phase-5-structural` and the per-place
positivity refutation of `phase-6-osterwalder-schrader-reflection`; the NO-GO multiplicativity finding
is recorded in the program's shared routes-tried index and should not be retried without a new,
explicitly different hypothesis.

## Other files in this folder

Files not described above:

- `0-triangulation-of-the-wall-from-three.md` — ε₀>0: triangulation of the wall from three frames + window-design route
- `2b_O4b_analytic.md` — O-4b: analytic derivation of the effective operator 𝓛 (in progress, with markers)
- `2b_ObjB_lower_bound_attempt.md` — Goal B — attempt to prove the lower bound of ε₀ (transparent, with [GAP])
- `2b_PROOF_DRAFT.md` — #2 — PROOF DRAFT (for verification)
- `2b_PROOF_FRAMEWORK.md` — #2: rigorous proof framework (edge spectrum (k+1)²) — scaffolding + open step
- `2b_SCALING_LIMIT.md` — 2b: reduction to the SCALING LIMIT of the bottom of A_λ (the three fronts)
- `2b_part_i_EXACT.md` — 2b part (i): the localized form is an EXACT restriction — CLOSED
- `2b_scale_correction_propagation.md` — Propagation of the scale correction −log ε₀ ~ c·n(T*) through Link 2
- `AUDIT-repairs-E1-III.md` — Repair of the two points of maximum severity: E1 and III
- `AUDIT-repairs-norm-N5c-IV2.md` — Repair of the three 🟠 points: Normalization, N5c-DH, IV.2≡§V (conflation)
- `A_intento_demostracion.md` — Goal A — proof attempt (pure mathematics, proved steps + frank [GAP])
- `ESLABON2_ESTADO_COMPLETO.md` — Link 2 — Complete consolidated status (what is proved, what is missing, how to close it)
- `MAP_2b.md` — Link 2b (λ→∞): reformulation as a Szegő limit and concrete target
- `MAP_ESLABON2.md` — Link 2 (convergence ξ̂_{λ,N} → Ξ): structure, attack and status
- `REDUCCION-RH-CCM-final.md` — A reduction of the Riemann Hypothesis via zeta spectral triples (CCM program)
- `rh-proof.pdf` — PDF
- `rh-proof.tex` — LaTeX source
