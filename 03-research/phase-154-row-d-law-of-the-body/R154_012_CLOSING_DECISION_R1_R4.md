# R154.012 — Closing decision, phase 154 rounds 1–4 (the law of the body → the dual-certificate theory)


## 1. Theorems of record

| id | statement | label |
|---|---|---|
| **Theorem A** (R154_001/002/004) | On the two-condition primitive class `𝒦^prim_{2T}` = {Φ positive-definite, supp ⊂ [−2T,2T], Φ(0)=1, ∫Φcosh(u/2)=0, ∫Φ·u·sinh(u/2)=0}: `λ_min(A_T(v)|P_T) = C₀ − Λ_T(v)`, `Λ_T(v) = sup_Φ [Σ_n v_nΦ(log n) − 𝔈(Φ)]`, `𝔈(Φ) = ∫₀^∞(1−Φ)K`, `K(u) = ½/sinh(u/2)+½/cosh(u/2)`, `C₀ = ψ(¼) − log π`. Lévy–Khintchine form of the archimedean multiplier (partial RESTATEMENT of phase 64). | `PROVED` |
| **Structure** (R154_004/005) | `Re ψ(¼+iτ/2) − ψ(¼) = φ(τ²)`, `φ(x) = Σ_k x/(a_k(x+4a_k²))`, `a_k = k+¼`, complete Bernstein; `ν(u) = Σ_k e^{−(2k+½)|u|} = K/2` completely monotone ⇒ the archimedean Weil generator is a pure-jump subordinate Brownian motion. Subordination upper bound `λ_min(A_T) ≤ C₀ + 2Σw_n + φ((3π/2T)²)` = 1.29 (½log3), 2.33 (log 2) > 0. Phase 64 §5's diffusion identification untenable in that scaling. Credit: R154_003 §0. | `PROVED` |
| **Theorem W** (R154_004) | Euler–Lagrange of the minimiser = finite-interval Wiener–Hopf equation with symbol `σ_T − λ`, RHS `α cosh(t/2) + β sinh(t/2)`; symbol non-elliptic (3 / 11 sign changes on (0,400)); the primes destroy the factorisation | `PROVED` |
| **Theorem O** (R154_004/005) | For every finite signed measure ν on `|u| ≥ 2T` and finitely many continuous multipliers, `inf_τ[σ_T + ν̂ + Σβ_jĝ_j] < λ_min` strictly: the dual is never attained (holds for `v = 0`) | `PROVED` (forbids attainment only) |
| **Theorem D1** (R154_007/008) | Strong duality: `sup` of dual certificates `= λ_min(A_T(v))`, exhausted by finitely atomic ν (repair RJ: `M ⊆ cl(M_c)`, `int cl C = int C`; Rockafellar Cor. 31.2.1). **Equivalent formulation:** `A_T ≥ 0 on P_T ⟺ ∀ε>0 ∃ atomic ν on |u|≥2T, β₀,β₁: σ_T + ν̂ + β₀ĝ₀ + β₁ĝ₁ ≥ −ε` on R. Hence RH ⟺ this for every T. An equivalence, not a proof. | `PROVED` |
| **Lemma D2.1 / D2.3** (R154_007/010) | Lattice atoms `u_j = j·2T/M` make `ν̂` `P`-periodic (`P = 2πM/2T`): the tail is certified on one period; D2.3 collapses `[τ₁,∞)` onto one period of phases with graded right-hand sides (prime term exact for the first N periods) | `PROVED` |
| **Theorem C(½log3)** (R154_010/011) | Explicit dual certificate: 437 atoms on `u_j = j·(log 3)/24`, `j = 24…460`, `β₀ = 2.0025617`, `β₁ = −0.0096544`, with `σ_T + ν̂ + β₀ĝ₀ + β₁ĝ₁ ≥ c = 4.4279281900·10⁻⁵` on R (exhaustive stack B&B, `2.37·10⁸` evaluations, zero unresolved, no discards; mpmath.iv enclosures; independent replay from the archived decimals `scripts/round4/certificate/CERT_log3_M24.json` bit-identical). Hence `A_{½log3} ≥ c > 0` on `P_T`. Uses only weak duality. **First proof of Weil positivity with a prime coupled by an explicit outside-window dual certificate.** | `PROVED` (confirmation: PROOF ACCEPTED) |
| **The polar term** (R154_007/008) | Optimal duals have `β₀ → 2`, `β₁ → 0`: `β₀ = 2` restores exactly `Φ̂(i/2) + Φ̂(−i/2)`, the two pole terms of the explicit formula, coefficient 1 each (exact identity) | `PROVED` (identity); limit `DIAGNOSTIC-NUMERIC` |
| contact set / ν structure | contact set is a comb (49 components at `10⁻⁴`); ν has no arithmetic structure (70% sign alternation, weights decaying from the window edge) | `DIAGNOSTIC-NUMERIC` |
| `T = log 2` | best certificate `−8.49·10⁻²` vs `λ_min ≈ 1.09·10⁻⁷`; ~~D2.3 blocked by the incommensurability of `log 3` with any lattice of `log 2`-multiples~~ **[amended per R154_016] D2.3 applies unchanged (`R154_015 §2`, `R154_016`); the block is the atom budget `M`, measured at `T = 0.58` as a deficit of `3.20·10⁻³`; the `M`-sweep is still open (`R154_017 §4`)** | `DIAGNOSTIC-NUMERIC`; `OPEN` (P154.1) |

Withdrawn/corrected along the way: orbit fibration at `log 2` (does not exist: dense subgroup); integer 3-smooth breakpoints (dense set); one-condition primitive class; "dual never attained ⇒ route closed" (only attainment forbidden); Kwaśnicki two-term law (1e-2 off at n = 1,2); the round-3 verifier (silent discards) and its `−3.70·10⁻³`. FATAL rule clean throughout; no sign claimed for ζ beyond `T ≤ log 2`.

## 2. What phase 154 created
1. A **complete dual theory of Weil positivity at finite support**: `A_T ≥ 0 ⟺` existence of outside-window atomic certificates (D1 + O), with the archimedean side understood as a subordinate Brownian motion and the arithmetic side as prime evaluations. RH becomes a family of Delsarte-type linear programs, one per `T`. Not in the corpus, not previously found in the literature (corpus-checked; literature check pending, (P154.2)).
2. The **first structural proof** of positivity with a prime coupled, `T = ½log3`: the mechanism is visible — an explicit measure outside the window, the polar term of the explicit formula restored by the optimiser with coefficient 2, and a comb of contact points.
3. The exact obstructions for everything else tried (Theorems O, W; rounds 5–6 of phase 153).

## 3. What it does not do
It does not give the sign for ζ beyond `log 2`. At `log 2` the certificate is six orders short ~~and the periodic method is blocked by incommensurability: the two-prime window needs a genuinely two-frequency certificate.~~ **[amended per R154_016] and the periodic method is *not* blocked: the graded tail lemma holds for any finite contact set (`R154_015 §2`, confirmed `R154_016`), as a sufficient criterion (`⟸`, not `⟺`). What the two-prime window costs is an atom budget: at `T = 0.58` the same class reaches only `−3.1964·10⁻³`, exhaustively verified, against a target `2.16·10⁻⁴`.** The equivalence D1 is Weil's criterion in dual coordinates; the sign for all `T` is exactly the existence of certificates for all `T`, and nothing here produces them uniformly.

## 4. Open items
(P154.1) a certificate at `T = log 2` (two contacts; ~~needs a non-lattice tail lemma~~ **[amended per R154_016] needs an atom budget `M` sufficient for two contacts; the `M`-sweep at `T = 0.58` is the open measurement, attempted and not converged in round 6, `R154_017 §4`**); (P154.2) literature check: Delsarte/Cohn–Elkies-type LP formulations of Weil positivity, Beurling–Selberg with the Weil symbol; (P154.3) a `T`-uniform family of certificates (= RH; record only); (P154.4) repairs W1–W4 and R154_007 §8 text; (P154.5) Paper 47/47 write-up (decision pending).

## 5. Decision
Rounds 1–4 closed. Phase 154 stays open on (P154.1). Row D label: unchanged for the global sign; **row D acquires its first structural positivity theorem with a prime coupled (Theorem C(½log3)) and its dual theory (Theorems A, O, D1).**

## 6. Amendments after the literature and corpus review (R154_013)
1. **§2 item 2 narrowed.** Certified positivity on windows strictly containing ours exists by computer-assisted Galerkin work (Zhu,
   arXiv:2608.24827, supp ⊂ [−0.8, 0.8]; Groskin, arXiv:2607.02828) — to be read in full and cited. Theorem C(½log3) is therefore **the
   first proof of Weil positivity with a prime coupled by an explicit outside-window dual certificate** (no Galerkin, no eigenvalue
   computation), not "the first mesh-free proof" tout court. Wording changed accordingly wherever it appears in this phase.
2. **Structure row: credit corrected.** "Complete Bernstein function of τ²" for the archimedean term is already on record in phase 114
   D.69:140, and the Lévy–Khintchine + killed-on-I_T framing in D.182:140–167 is the closest corpus precursor to Theorem A. The structure
   row is relabelled `RESTATEMENT (D.69, D.182) + PROVED (CM of ν = K/2; subordination bound)`; the earlier "new structural fact" claim is
   withdrawn. Paper 37 `cor:bernstein` concerns a different function and must be distinguished explicitly.
3. **Novelty of D1/O/A (dual equivalence, non-attainment, Legendre form):** NOT FOUND in the literature (closest: Bombieri 2000, primal
   only; Cohn–Elkies machinery never transported to the Weil symbol; Carneiro–Chirre–Milinovich / Chirre–Gonçalves–de Laat LPs assume RH
   and optimise statistics). Suzuki's screw-function programme (2206.03682, 2301.00421) is the closest genus for the negative-definite
   kernel reading and must be read before any novelty claim about (b). Bombieri 2000 and Yoshida 1992 are not in 00-references: obtain.
4. Connes–Consani "log 3" attribution found in a search summary is unverified against 2006.13771 and is dropped.

## 7. Amendment (R154_021): the "polar term" row's limit claim is withdrawn; β₀ = 2 stands as the unique polar multiplier (Prop. P, identity); convergence OPEN; recorded β₀ values are at different T.
