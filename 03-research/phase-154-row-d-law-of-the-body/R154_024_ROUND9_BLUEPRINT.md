# R154.024 — Blueprint, round 9: smooth exponential certificates (the tail problem solved by construction) and mass-vs-value.

*Aggressive pace, do not stop; new insights required. Compute: pure mathematics first; ONE short LP (≤ 10 min, one process) only after the
tail lemma is PROVED on paper.*

## 0. The two problems and the idea
(P154.7) The lattice tail lemma worst-cases `ν̂` by `−ρ` on every period; its slack is 10²–10⁴× the targets and grows with the period.
(P154.8) No rate theorem: the relaxed-primal mass outside `[−τ₁,τ₁]` trades against the value only logarithmically.
**Idea A (tail by construction).** Theorem D1 allows any finite signed measure on `|u| ≥ 2T`. Take smooth **exponential columns**:
`ν_k(u) = e^{−s_k(u−2T)}·1_{u ≥ 2T}` (and its mirror), `s_k > 0`. Then `ν̂_k(τ) = 2 Re[ e^{2iTτ}/(s_k − iτ) ]`-type (compute exactly with the
paper's Fourier normalisation) — elementary, **decaying like 1/τ**, with explicit `|ν̂_k(τ)| ≤ 2/√(s_k² + τ²)`. A certificate
`ν = Σ_k b_k ν_k + (a few atoms at/near u = 2T)` has a tail bound with NO period and NO worst-case constant: for `τ ≥ τ₁`,
`f(τ) ≥ m(τ) − 2(w₂+w₃) − Σ|b_k|·2/√(s_k²+τ²) − |β·ĝ(τ)|`, and `m(τ) ≥ log(τ/2) − const` (use the audited constant, R154_016). Everything
is monotone in `τ` beyond an explicit point, so the tail is a two-line lemma and the incommensurability of `log 2, log 3` is irrelevant.
Also allowed and possibly better: `ν_k(u) = (u−2T)^{k} e^{−s(u−2T)}` (Laguerre-type; transforms `k!/(s−iτ)^{k+1}`), or Gaussian columns.
**Idea B (mass-vs-value on the atomic minimiser).** By Corollary K0 (R154_020) the relaxed primal minimiser is atomic with `≤ N+3` atoms;
the value `∫σ_T dμ` is a finite sum. Prove the exchange lemma directly on this finite sum: mass `ε` at `|τ| ≥ R` costs at least
`ε·(m(R) − 2Σw_n − C₀-part)` while it can buy at most … — derive the exact inequality and see whether the logarithmic exchange of
R154_020 is sharp or improvable for atomic `μ`.

## 1. Tasks
(A1) **Lemma T (tail by construction), PROVED:** exact transforms of the exponential (and Laguerre) columns in Paper 42's normalisation
(state `Φ̂`, `c_F`, and the pairing used in Theorem A so that `∫ν̂|F̂|² = 0` holds for `F ∈ P_T` — check the support condition: `ν` supported in
`|u| ≥ 2T` and continuous at `2T`: is `c_F(2T) = 0` enough, or does a density touching `2T` need care? it does not, since `c_F` vanishes
outside `(−2T,2T)`); the explicit tail inequality with all constants; the point `τ₁(b, β, s)` beyond which `f ≥ c` holds automatically.
Corpus check: grep "exponential column", "Laguerre", "smooth certificate", "densidad exponencial".
(A2) **The finite-dimensional certificate problem** with `K` exponential columns + `J` edge atoms + `β₀, β₁`: write it as an LP with rows on
`[0, τ₁]` only (the tail is free). Prove the dimension count: how many columns are needed in principle (Theorem D1 says smooth measures also
exhaust the sup? — check: D1 was proved for atomic `ν`; extend to the exponential class, or show atomic ⊂ closure of exponential class in the
relevant topology: exponentials with varying `s` are dense in `L¹(2T,∞)`, so `ν̂` approximable uniformly on compacts — PROVE the needed
statement, label).
(A3) **ONE LP** (≤ 10 min, one process, after A1): at `T = 0.58`, `K = 40` exponential columns with `s_k` log-spaced in `[0.05, 50]`, plus
`J = 20` atoms on `[2T, 2T+0.5]`, β free, rows = 4 000 points on `[0, τ₁]` + cutting planes (≤ 6 iterations), fine-grid check; report the
true minimum on `[0, τ₁]` and the analytic tail value; compare with round 5's `−3.18·10⁻³` (M=24 lattice) and round 8's control. If the true
min is `> 0`: STOP and report (the exhaustive verification is a separate authorised step); if the tail is now non-binding, say so — that is
the point of the round even if `c < 0`.
(B1) **Lemma V (mass-vs-value), attempt PROVED:** on atomic relaxed minimisers (Cor. K0), give the exact exchange inequality; determine
whether the deficit `λ_min − c(class)` admits a lower bound linear in the smallest "resolution" of the class (a rate) — or prove the
logarithmic barrier is sharp (an obstruction theorem). Either outcome is a theorem; label accordingly.
(C1) **Riemann's tools, one paragraph each, no fluff:** state which of Poisson summation / theta functions / Mellin inversion / the
functional equation gives an *identity* for `Σ_k b_k ν̂_k + σ_T` that could make a certificate exact rather than approximate (e.g. is there a
choice of smooth `ν` for which `σ_T + ν̂` equals a manifestly nonnegative expression on `R` up to the polar terms — the analogue of the
"magic function"?). Check against Theorem O (exactness is impossible for finite measures — so any identity must involve an infinite or
non-finite object; say exactly which, and whether a finite truncation with a sign-controlled error exists).

## 2. Rules
Labels PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN / REFUTED; FATAL rule; no sign for ζ beyond `log 2`; corpus-check lines; compute limits
as stated (`timeout 600`, single process). Deliverable `R154_025_ROUND9.md` (≤ 5000 words) + `scripts/round9/`. Audit follows.
