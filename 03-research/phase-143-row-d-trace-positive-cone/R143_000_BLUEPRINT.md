# R143.000 — Blueprint, phase 143: `s_*`, the trace-positive cone B4, and a repaired transfer theorem

unsatisfiable for `ξ`; diagnosis; horns A/B; order (0) O-19, (1) Horn B/B4, (2) Horn A), `R142_001`
§§D.31–D.32 (Lemma D.31.4, `s(γ,θ)`, D.31.10 witness family `E_{t,d}`, Thm D.32.4, candidates B1–B5),
`R142_004` (J1–J10, especially J3: the witness family lies in B4; J2: B4 ⊇ 𝓝_∞, `𝓔 ⊂ B4` unproved),
`R141_001` §D.26 (traces `t_n(E) = I_∞(E, τ_{log n}g)`, moment cone), Paper 47 §§11–12 (Thm 11.13, 11.14,
12.3 and its proof), Paper 44 (Frobenius Gram form (A), Thm 8bis.4a).*

Standing rules as before (labels; zero-free definitions — `ξ` as data, traces defined by the arithmetic
side; three falsifiers `Ξ_a`, `Ξ_Q`, `ζ_K`; corpus check per idea; FATAL rule: a proof of a transfer
theorem plus a proof of its hypothesis would prove RH — flag, do not fix; any argument valid verbatim for
`Ξ_a` is wrong when it purports to prove positivity for `ξ`).

## D.33 — O-19: the constant `s_*` (do first; gates both horns)
`s(γ,θ) := sup_u |cos(γu+θ)|/cosh(u/2)`, `s_* := inf` over zeros `ρ = ½+iγ` of `ξ` and `θ ∈ R` (or the
relevant `θ` for each zero). Determine `s_*`: is it `0`, positive, attained? Note `s(γ,θ) → ?` as
`γ → ∞` (the sup is near `u ≈ 0` where `cosh ≈ 1`, so `s(γ,θ) → 1` for `θ = 0`; for `θ = π/2` the first
maximum of `|sin(γu)|` is at `u = π/(2γ) → 0`, `s → 1`; so `s_*` is probably attained at small `γ` — compute
`s(γ_j, θ)` for the first zeros, prove monotonicity in `γ` if true, and give `s_*` with a certified
margin). Consequences: the strongest admissible Horn-A defect; the size of `𝔐 ∩ S_0`. Label.

## D.34 — Horn B: the trace-positive cone B4
1. **Definition, zero-free.** Fix `g` as in §D.26 (real even `C_c^∞`, `g ≥ 0`; the Baire choice ensuring
   `Φ_g(ρ) ≠ 0` for all zeros — record whether the definition of B4 depends on `g`, and if so define
   `B4 := ∩_g` or fix one `g` and say so). `B4 := {E ∈ D^W : t_n(E) ≥ 0 for all n ≥ 1}` (with or without
   `t_0`: decide; note `t_n(E) = PRIME − ARCH` of `E ⋆ (τ_{log n}g)^∨`, arithmetic). `B4 ⊇ 𝓝_∞` (traces
   vanish there): so B4 is a cone **containing the radical**, and all statements are mod `𝓝_∞`.
2. **The decidable first question (T1 mod 𝓝_∞).** *Is there a primitive `F ∉ 𝓝_∞` with `t_n(F) ≥ 0` for all
   `n`?* Equivalently: is `B4 ∩ P^W ⊋ 𝓝_∞`? Under the explicit formula `t_n(F) = −Σ_ρ Φ_F(ρ)Φ_g(1−ρ) n^{½−ρ}`
   for primitive `F` (no polar term); so the question is whether the almost-periodic-type function
   `n ↦ Σ_ρ c_ρ n^{½−ρ}` can be `≤ 0` on all integers `n ≥ 1` with `c ≠ 0`. Attack: (i) if RH, `n^{½−ρ} = n^{−iγ}`
   and `Σ_ρ c_ρ n^{−iγ}` is a Bohr almost-periodic function of `log n` sampled at `log n`; a nonzero
   almost-periodic function with mean value `0` (does it have mean `0`? the coefficients pair `ρ, ρ̄`) must
   change sign — but only on `R`, and the samples `{log n}` are a discrete set: use the density of `{log n
   mod T}` (Weyl equidistribution of `log n`? — `log n` is NOT equidistributed mod 1; use instead that
   `n^{−iγ}` for `n` ranging over integers realizes all values of the character on a dense set by
   Kronecker/Dirichlet for finitely many `γ`'s, then truncation of the tail with the `ℓ¹` control of
   Paper 47 (11.2)) — build the argument or find the obstruction; (ii) unconditionally, the frequencies
   `½−ρ` may have real parts; then `n^{½−ρ}` has growth and the sign question changes — record what is
   provable without RH and what is not (FATAL rule: if the answer "no such `F`" is proved unconditionally
   *and* it makes a transfer theorem run, stop and flag). Outcome: YES (Horn B dies at (T1); give `F`) /
   NO (theorem; label; state exactly what was used) / OPEN (the exact missing estimate).
3. **(T2) for B4**: the bounded-density constant `C'_X := sup_{E' ∈ B4, deg E' > 0} |I_∞(E',X)|/deg E'` —
   finite for every `X`? With constants `≍ γ_j²` as the auditor guesses? Prove or bound.
4. **The transfer theorem 12.3-B4.** Re-run Paper 47 Thm 12.3's proof with "effective" replaced by "in B4
   with `deg > 0`" (and (b′)_{B4}: `h⁰(E) > 0 ⟹ E ∈ B4 + 𝓝_∞`, `deg E > 0`): which steps survive (the
   degree argument uses Thm 11.13: `deg E' > 0` for nonzero `E' ≥ 0` — for B4 this must be replaced by
   the definition or by (T1)); which need (T2); state the theorem with its exact hypotheses and label. Then
   check the FATAL rule: is (b′)_{B4} for `h⁰_RR⁺` (i.e. `R(E) > 0, deg E > 0 ⟹ E ∈ B4`) refuted by a
   witness, provable, or RH? By J3 the D.31.10 family lies in B4 — so the old refutation does not apply.
   Compute: for `E ∈ S_0`, are all traces nonnegative? `t_n(E) = [polar ≥ 0 part] − Σ_ρ Φ_E(ρ)Φ_g(1−ρ)n^{½−ρ}`;
   the polar part is `Φ_E(0)Φ_{τg}(1) + Φ_E(1)Φ_{τg}(0) = a·n^{½}Φ_g(1) + b·n^{−½}Φ_g(0)` (check) and the
   zero part is bounded by Cauchy–Schwarz in terms of `W(E)` and `Σ|Φ_g(ρ)|²n^{…}`; `R(E) > 0` bounds `W(E)`
   by `d²/2 − d/2`; determine whether this yields `t_n(E) ≥ 0` (under RH? unconditionally?). Be exact.
5. **Falsifiers.** `Ξ_a`: define B4_a verbatim; the transfer theorem 12.3-B4 must NOT prove positivity for
   `Ξ_a` (which is false): locate the step that fails (expected: (T1)/(T2) or the polar part with rank 4).
   `Ξ_Q`: frame broken (A7) — record what makes sense. `ζ_K`: all statements verbatim.
6. **Reading A8.** Where exactly do the weights `Λ(n)n^{−½}` (A8/A4) enter B4's properties? (The traces are
   `PRIME − ARCH`; the PRIME part is `Σ_m Λ(m)m^{−½}(E ⋆ (τg)^∨)(log m)`.) State it as a labelled remark.

## D.35 — Horn A (secondary; only what is cheap)
State (c′) with `Δ(d) = max(0, (d²/4)(1 − s_*²) − d/4)` using `s_*` from D.33; confirm Thm 12.3 runs
with (c′) (degrees 0 and 1 only); state the gated candidate with the **primitive** (★)-gate (J1) and record
its blocker O-18′ precisely. No new attack on O-18′ in this phase.

## D.36 — Synthesis input
One page: `s_*`; the answer to (T1); whether 12.3-B4 exists and what its hypothesis (b′)_{B4} looks like for
`h⁰_RR⁺`; the exact place where A3 and A8 enter; recommendation for phase 144.

## Deliverables and rounds
`R143_001_ROUND1.md` (D.33; D.34 items 1–4 with the decision on (T1) or the exact gap; D.34.5–6;
D.35; D.36; corpus check per idea — grep in particular for "trace positive", "positive traces",
"nonnegative Frobenius", "almost periodic sign change", "Kronecker" in 03-research; paper-facing; open
list; label), README; audit `R143_002`, repairs, confirmation, closing decision `R143_005`. Scripts only to certify
`s_*` and constants (`--fast`, margin).

## Warnings
* B4 depends on `g` unless proved otherwise; say which.
* (T1) is the whole game for Horn B: do not build 12.3-B4 on an unproved (T1); label conditionally.
* Anything that proves `R > 0, deg > 0 ⟹ E ∈ B4` unconditionally together with 12.3-B4 is FATAL-flag
  territory: stop, run `Ξ_a`, report.
