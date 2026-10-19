# R154.018 — Blueprint, round 7 of phase 154: PURE MATHEMATICS — the approximation theory of the dual certificate.

*pure mathematics; computation only when strictly necessary (identity checks at most; no LP, no B&B).*

## 0. What the data force us to understand
At `T = ½log3` (one contact) lattice certificates with `M = 24` capture `c = 8.86·10⁻⁵` of `λ_min = 9.8·10⁻⁴` (9%). At `T = 0.58` (two
contacts) `M = 24` gives `−3.18·10⁻³` against `λ_min = 2.16·10⁻⁴`; larger `M` did not converge (compute wall). Shape transfer 0.58 → 0.62
fails (−0.40). Theorem D1 says atomic certificates approach `λ_min`; it says nothing about the RATE in the number of atoms, the spacing
`h = 2T/M`, or the range `U`. Without the rate we cannot know whether the staircase to `log 2` (target `1.09·10⁻⁷`) is feasible at all.

## 1. The reformulation to be written (PROVED, exact)
Weil positivity at support `T` on `P_T` is a **one-sided approximation problem with a spectral gap**: with `Ψ_T(τ) := σ_T(τ) + β₀ĝ₀(τ) + β₁ĝ₁(τ)`
(β free), `λ_min(A_T) = sup_{β} sup{ c : ∃ ν finite signed measure on |u| ≥ 2T with Ψ_T + ν̂ ≥ c on R }` (Theorems A/O/D1 restated).
Equivalently: `λ_min = sup_β inf over spectral-gap functions G (Ĝ supported in |u| ≥ 2T) of sup_τ [G(τ) − Ψ_T(τ)]`… write the exact
minimax statement with signs right, and its finite-lattice version (spacing `h`, range `U`): `c(h,U;T)`. Corpus check: R153_016 §2.3,
R154_007 §D1, R154_015 §F1. Literature to place it: Beurling–Selberg extremal functions (Vaaler 1985 BAMS; Holt–Vaaler 1996;
Carneiro–Vaaler 2010 "Some extremal functions in Fourier analysis II/III"; Littmann; Carneiro–Littmann–Vaaler "Gaussian subordination"),
**and specifically the spectral-gap / "functions vanishing on an interval of the spectrum" side** (Beurling–Malliavin; Logvinenko–Sereda;
Kolountzakis; one-sided approximation by exponential sums with frequency gaps). State precisely which classical problem ours is the dual of
(band-limited minorants of a given function ↔ our spectral-gap minorants), and what is known about RATES there.

## 2. The rate theorem (the round's target; PROVE what can be proved, state the rest as a precise conjecture-free OPEN)
(R1) **Lower bound on the certificate deficit for lattice measures.** For ν on the lattice `{j·h}`, `ν̂` is `P = 2π/h`-periodic. The ideal
(unattainable) dual would satisfy `Ψ_T + ν̂ ≡ λ_min` on `supp|F̂_T|² = R`. Prove a lower bound `λ_min − c(h,U) ≥ D(h,U;T) > 0` in terms of
the part of the Weil kernel `k_T(u)` (Fourier transform of `Ψ_T − λ_min` restricted to `(−2T,2T)`, i.e. the Gamma kernel on the window
plus the atoms at `±log n` with `n < e^{2T}`) that a `P`-periodic function cannot represent: periodic `ν̂` has Fourier support on the
lattice `hZ`, so it can match `k_T` only on lattice points; the mismatch on `(−2T,2T)` is what forces the deficit. Get an explicit `D` (a
Jackson-type bound in `h`, with the singularity of `k_T` at `u = 0` (`~1/(2u)`) and the atoms as the obstructions). This is the theorem
that says how `M` must scale with the target: if `D ~ h^α`, then `M ~ (λ_min)^{−1/α}`; evaluate the prediction at `½log3` (data: `M=24`,
deficit `8.9·10⁻⁴`), at `0.58` (deficit `3.4·10⁻³` at `M=24`) and at `log 2` (target `10⁻⁷`). Compare with data qualitatively; no new
computation beyond arithmetic.
(R2) **The effect of the second contact.** Why does adding `n = 3` at `0.58` cost a factor ~15 in the deficit at fixed `M`? Analyse the
kernel `k_T`: a new atom at `u = ±log 3` inside `(−2T, 2T)` is a new δ that a lattice with `log 3 ∉ hZ` cannot place — quantify the
one-sided approximation cost of an off-lattice δ by lattice atoms *outside* the window (it must be paid through the periodic structure).
This may be the exact reason the two-contact steps are hard and may suggest the remedy (atoms at `2T + (log 3 − log 2)·k`? two lattices?
non-lattice atoms with a non-periodic but controlled tail?). Prove what you can; propose the remedy as a theorem-candidate with the exact
statement that would need to be proved, and what it would cost to verify (no runs).
(R3) **Upper bound on the deficit (constructive, analytic).** From the minimiser's E-L (Theorem W): `(σ_T − λ)F̂_T = Ĥ + αĥ₀ + βĥ₁` with
`H` supported in `|t| ≥ T`. Try to build an analytic near-certificate: e.g. `ν := ` a smoothed version of `H ⋆ H̃`-type outside-window
measures, or `ν̂ := (Ĥ·conj F̂_T + c.c.)/|F̂_T|²`-type expressions corrected to have spectral gap — determine whether any such construction
yields a spectral-gap function minorising `λ − Ψ_T` with an explicit deficit; if not, prove the obstruction (Theorem O's mechanism).
(R4) **The polar term.** Prove analytically that the optimal `β₀ → 2` as the certificate class exhausts (D1 limit): i.e. that in the limit
the dual multiplier of the constraint `∫Φcosh(u/2) = 0` equals the polar coefficient of the explicit formula. (Idea: the optimal dual
is the limit of the E-L multipliers `α, β` of Theorem W normalised by `λ`; compute them in terms of `F̂_T(±i/2)` derivatives.) PROVED or OPEN.

## 3. Rules
No computation except arithmetic on recorded numbers and at most identity checks with mpmath at a few points. Corpus-check lines
(grep "Beurling–Selberg", "Vaaler", "spectral gap", "hueco espectral", "Logvinenko", "Jackson", "one-sided approximation", "minorant").
Labels PROVED / RESTATEMENT / DIAGNOSTIC / OPEN; FATAL rule; no sign for ζ beyond `log 2`. Deliverable `R154_019_ROUND7.md`
(≤ 5000 words) with complete proofs; an audit follows.
