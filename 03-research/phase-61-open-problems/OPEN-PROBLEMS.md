# Open Problems — RH program (CCM frame), Phase 61 cut

Complete inventory of what remains to close, walking the 12 steps of `RH-PROOF-PAPER` down to the
minimal loose ends of the "proved" ones. For each problem: **what we have · why it does not close ·
what is needed**. Chain status convention (at the cut): proved/closed 1, 3, 4, 5, 6, 7, 8, 10;
Step 2 proved at finite λ (numerical uniformity, see O5); open 9, 11, 12. Steps 3, 5, 8 are
**working axioms** (community-validated; not re-litigated). The real wall is Step 12 = `ε₀≥0 ∀λ` =
RH. Document meant to work alongside A.: not to solve everything, but to have the exact front of
pending tasks.

---

## Loose ends in the "proved" steps (1–8, 10) — RH-neutral, closable with finite work

### O1 — Step 1.2, normalization of the multiplier
- **We have:** `â(t)=Ω̃(t)−D_λ(t)` via the explicit formula; the coefficient of `δ₀` fixes the normalization.
- **Why it does not close:** the identification `2∫₀^∞ w_arch(u)cos(tu)du = Ω̃(t)` is used via the explicit-formula relation, not verified term by term against the Tate constants.
- **To close:** a direct check of the archimedean constant (factor `Γ_ℝ`) against the local functional equation. A finite computation.

### O2 — Step 4.1, the tail beyond the horizon
- **We have:** `|Ξ_T−Ξ|≤Cλ^{5/2+δ}e^{−πλ²}` for `|t|≤T*`; tail `e^{−πγ²/L}`.
- **Why it does not close:** `C` and the exponent `5/2+δ` are bounded, not optimized; the tail control assumes Gaussian decay without an explicit uniform bound in λ.
- **To close:** a λ-uniform bound on the incomplete-gamma remainder (standard, just needs writing).

### O3 — Step 4.3, edge amplification
- **We have:** `1−ω=O(1/λ²)` (Boas) and `λ^{|y|}≤λ^{1/2}` (Phragmén–Lindelöf).
- **Why it does not close:** "cite+verify" — theorems cited, missing the numerical verification of the harmonic-measure constants in the concrete case.
- **To close:** an explicit, reproducible evaluation of the harmonic measure in the strip.

### O4 — Step 10.3, "argued"
- **We have:** `H_λ=(p²−λ²)(q²−λ²)` has open orbits (scattering) in the Sonin region ⟹ only `N_smooth`.
- **Why it does not close:** a physical argument (no closed archimedean orbits), not a proof of zero contribution from the archimedean trace.
- **To close:** a rigorous trace formula for `W_λ` with zero contribution from archimedean periods.

---

## Step 2 — uniformity of the gap

### O5 — rigorous `liminf_λ (ε₁−ε₀)/|ε₀| > 0` ⟵ **central knot, together with O11**
- **What we proved:** numerically, with primes and a validated engine (dps=40): `ε_k/ε₀→(k+1)²`; `ε₂/ε₀→9.0` very cleanly; gap `ε₁/ε₀∈[3.51,4.19]` (min 3.51), robust over λ∈[3,12] and N∈[8,24]. Uniformity **holds numerically with margin** (gap ≥ 2.5 > 0).
- **What we tried and why it failed (two refuted routes, NO-GO):**
  - **(A) archimedean skeleton + primes as a bounded perturbation — REFUTED.** With primes off, the archimedean `M_θ` is **indefinite** (`Ω̃(0)=−logπ+ψ(1/4)≈−5.37<0`), no ladder, ratios →0. The ladder and the positivity of `ε₀` are **constitutively arithmetic**: there is no archimedean limit to perturb.
  - **(B) free Dirichlet box, eigenvectors = sine modes — REFUTED.** The spectrum is `(k+1)²`-like, but the eigenvectors are not box modes: de-modulating by `(−1)^j` gives overlap<0.35 and nodes 10,13 (should be 0,1,2); with an adjusted carrier `cos(ω(j−c))` overlap≈0.5 and `m` scrambled.
- **The limit operator RESOLVED (via the Doob transform — route (iii), validated).** Routes (A),(B) used the wrong object. The correct one is the **Doob transform** (divide by the ground state `u_0`): the form `G_λ(v,v)=[A_λ(u_0 v,u_0 v)−ε₀‖u_0 v‖²]/(|ε₀|‖u_0‖²)` has spectrum `{(ε_k−ε₀)/|ε₀|}→{k(k+2)}`. Its limit is the **Doob transform of the Dirichlet Laplacian** `L_∞ v=−(1/sin²θ)∂_θ(sin²θ ∂_θ v)` on `L²([0,π],sin²θ dθ)`, eigenvalues `k(k+2)=(k+1)²−1` ⟹ `ε_k/ε₀→(k+1)²`. Eigenfunctions = **Chebyshev `U_k`** (second kind): the Doob ratios `r_k=u_k/u_0` are `U_k` — **VERIFIED** (λ=7: corr `r_2↔U_2=0.995`, `r_3↔U_3=0.905`; `r_2` corr 0 with the linear mode → not a carrier artifact). Explains the ladder, the non-sine eigenvectors, and the "carrier" (it cancels in `u_k/u_0`).
- **FORMAL CLOSURE (Doob–Feshbach–Mosco):** 2.3 **PROVED modulo a single CCM lemma**. The raw-moments route does NOT work (counterexample — bulk-homogeneous+Markov+Dirichlet does NOT force `−∂²`). The correct closure is **scale-free via Feshbach/Schur shorting** to the sine sector `𝒮_N=span{sin(mθ)}`: `F̃_{λ,N}=P_N A_λ P_N − P_N A_λ Q_N(Q_N A_λ Q_N)⁻¹ Q_N A_λ P_N`. PROVED: **Lemma 2.3.A** (Doob identity `∫|f'|²−∫|f|²=∫|v'|²sin²θ`), **Lemma 2.3.B** (Parter scale-free: `λ_m/λ_1→m²`, the scale `ρ_λ` cancels — no need to prove `e^{−cL}`), **Theorem 2.3** (`(ε_k−ε_0)/|ε_0|→k(k+2)`, gap→3) and **Cor 2.3.G** (3.2 via Kato–Montel–Hurwitz). **ASSUMED (genuine residue) = Lemma 2.3.F (CCM shorted Dirichlet quotient):** `ρ_λ⁻¹F̃_{λ,N}→diag(1²,..,N²)`, equiv. `dist²(ℰ_λ s_m, ℰ_λ Q_N𝓗)=m²dist²(ℰ_λ s_1,·)+o(ρ_λ)` (the norm of `ℰ_λ` on the slow sector is the Dirichlet one). It is NOT soft (counterexample); it is a theorem about the explicit CCM `ℰ_λ`. Validated numerically (Rayleigh→3,8,15 at λ=7,10,13; overlap 0.99/0.80/0.51; ladder robust). **2.3 and 3.2 = CLOSED conditional on 2.3.F.**
- **(historical) To close — reduced to 4 moments:** write `G_λ` in Beurling–Deny form `½∬(v(θ)−v(φ))²dη_λ`, `dη_λ=α_λ⁻¹u_λ(θ)u_λ(φ)dJ_λ` (`J_λ`=jumps of the carré-du-champ of Step 1.4: Lévy `dν` + primes `Λ(n)/√n` at `ξ=log n`). Mosco `G_λ→G_∞` follows from: **(M0)** `|u_λ|²dθ⇒sin²θdθ` ✓ **VERIFIED** (corr 0.97, θ=πy/L geometric anti-circular; and `u_k/u_0↔U_k(cosθ)` corr 0.96/0.96/0.82 k=1,2,3); **(M1)** mass of long jumps →0; **(M2)** local 2nd moment →∫a·sin²θ; **(M3)** 4th moment →0. limsup=Taylor on the C² core; liminf=nonlocal→local theorem (Bourgain–Brezis–Mironescu/Ponce). These are LOW/smoothed moments → **they avoid Kronecker (O11)**. Gives `(ε₁−ε₀)/|ε₀|→3`. **Missing: verify M1,M2,M3 numerically and then make them rigorous.** The only RH-neutral analytic piece left. **3.2 follows from 2.3** (a uniform gap isolates the fundamental projection → Kato+Montel+Hurwitz preserve real-rootedness).

---

## Step 9 — semilocal prolate

### O6 — closed form of `I_n(L)` ✅ **CLOSED**
- **Resolved (exact, not asymptotic):** `I_n(L) = [cos(LJ)]_{n,n} − [cos(LJ)]_{n−1,n−1}`, with `J` the archimedean Jacobi matrix (`a_n=√((n−½)n)`, `b_n=0`). From `∫e^{iLs}p_n p_m w_∞ ds = (e^{iLJ})_{nm}`.
- **Verified** to `10^{−16}` against the direct integral (`L=log2, log3`, all `n≤14`).
- **Bonus:** `δlog a_n = Σ_p Σ_k (p^{−k/2}/k)([cos(k log p·J)]_{nn}−[…]_{n−1,n−1})` — `δa_n` = diagonal of the propagator `cos(LJ)` of the scale operator; Gutzwiller as an exact identity. RH-neutral.

### O6-bis / Step 9.5 — fine oscillation law of `I_n(L)` ✅ **CLOSED (with proof, 2026-06-21)**
- **Theorem 9.5** (phase-61 paper, §9.5-ter / Theorem 9.5, compiles): with `ω(L)=2arcsin(tanh L)=2·gd(L)` (gudermannian), `[cos(LJ)]_{nn} = (π n sinh L)^{−1/2} cos((n+¼)ω − π/4) + O(n^{−3/2})`, `I_n(L) = (2 tanh L/√(π sinh L)) n^{−1/2} cos((n−¼)ω + π/4) + O(n^{−3/2})`.
- **Proof:** `J` = symmetric Meixner–Pollaczek Jacobi matrix (λ=¼) = `2K_1` boost of `su(1,1)` `D_{1/4}`. (i) spectral integral; (ii) Plancherel–Rotach; (iii) **stationary phase** → `s_*=2n·sech L`, frequency `ω=2arccos(sech L)=2arcsin(tanh L)` [exact]; (iv) index `ν=n−¼` of `a_k=√(k(k−½))≈k−¼`, amplitude+phase via Laplace–Heine of `P_{n−¼}(cos ω)`.
- **Validated** to relerr ≤`3·10⁻⁴` (decreasing `O(n^{−1})`) at `L=log2,3,4,5,8`, `n≤2500` (N≫n); dispersion to 4 digits over `L∈[0.3,2.2]`; `B_n√(π n sinh L)=1` to 4 digits ∀L.
- **Refutes `C₀J₂(2nL)` with a precise reason:** the true frequency is the gudermannian `2arcsin(tanh L)`, NOT `2L`; the envelope is `(π n sinh L)^{−1/2}`. The earlier refutation ("the envelope grows", at `n≤80`) was looking at the pre-asymptotic regime before `|I_n|√n` settles. The gudermannian dispersion is the `su(1,1)` signature: the circular angle `ω` is conjugate to the hyperbolic orbit rapidity `L`.

---

## Step 11 — Sonin + de Branges

### O7 — Sonin spectrum at λ>1 ✅ **CLOSED**
- **Resolved via Prüfer:** monotone angular flow `θ' = cos²θ/(q²−λ²) + ((2πλq)²−ξ)sin²θ`, `θ(λ)=π/2`. Each eigenvalue = a crossing `θ=mπ`; **zero spurious roots, zero missed**, valid at the LCO endpoint (does not use the asymptotic BC(17) functional that required `x≫μ/12`).
- **Validated:** the **density** `dN/dE` matches the counting law `2σ(E,λ)` to ~0.9 **uniformly** in λ=1,2,3 (increments `ΔN/Δ(2σ)=0.85–0.96`, no λ-bias). The cumulative count correctly gives zero eigenvalues before the first (λ=3: first at E≈16).
- (IC bug fixed along the way: `V(λ)=(2πλ²)²`, not `(2πλ)²`.)

### O8 — explicit `H_S` (2×2 reformulation) ⟵ **next step, a lever on the wall**
- **What we proved:** the **scalar** route is dead (11.2-bis): `E_S` is not Hermite–Biehler; `Θ_S` is not Schur (poles/zeros in `ℂ₊` at `z=2πm/log p±i/2`).
- **Why it does not close:** the correct object is a **2×2 J-unitary** transfer matrix (Tate) → canonical system `J Ẏ=z H_S Y`. Not constructed.
- **To close:** build `H_S(x)` from the local Tate transfer per place. Relocates the wall to `H_S⪰0` (positivity of a de Branges Hamiltonian). **This is step 11(b).**
- **PROGRESS (Pontryagin):** we built `T_S` explicitly (`T_p=(1−1/p)^{−1/2}[[1,−p^{−1/2+iz}],[−p^{−1/2−iz},1]]`), J-unitary on ℝ (1e-16). It is **generalized-J-inner with FINITE Pontryagin index** `κ=κ₀+|S|` (+1 negative square per prime = Euler poles, RH-neutral; verified, stabilizes on the grid). Via **Potapov–Ginzburg** → a generalized Schur function (unitary on ℝ). The wall `H_S⪰0` is reformulated: **not positivity but control of the index κ.**
- **NO-GO (b) Vladimirov/p-adic:** the p-adic concentration (centered balls) is **rank 1** (one mode); the p-adic Sonin is 1-dim (CCM Prop 4.5). The zeros **cannot come from an operator at a finite place** — spectral richness is only archimedean/global. Route (b) dead.

### O9 — `−γ_n²` = individual zeros (not just the count)
- **What we proved:** `σ(E,λ)=N_smooth` (count) rigorously; primes=`S(E)` (fluctuation) numerically.
- **Why it does not close:** the individual eigenvalue–zero correspondence `−γ_n²` is asymptotic; CM prove only the count (Cor 3.2: "no claim... though there is numerical evidence"). Our Sonin spectrum **scales with λ**, it does not land on fixed `−γ_n²`.
- **To close:** a fine spectral-correspondence theorem (stronger than Weyl) binding individual eigenvalues to zeros. Probably as hard as the wall.

---

## Step 12 — the wall

### O10 — `(P): ε₀(λ)≥0 ∀λ` = RH ⟵ **the wall**
- **What we proved:** the **equivalence** `(P)⟺RH` (12.1); the **marginality theorem** `2δ_λ/r_λ=√2/π` (12.2) — the sign of `ε₀` is **phase information**, not magnitude (Davenport–Heilbronn has identical magnitudes `{|Λ(n)|}` and `ε₀<0`).
- **Why it does not close:** no functional of the magnitudes decides the sign. The **phase** is needed. This **is** RH.
- **To close:** a new structural idea that accesses the phase. Candidates: `H_S⪰0` (O8); the Bost dynamical symmetry; closing HB with the functional equation `s↔1−s` (11.4). O8 and O9 are its two accesses. **It cannot be fabricated.**
- **PRECISE CHARACTERIZATION (via the Pontryagin index κ, validated):** equivalent reformulation of the wall — **`κ(completed object) = 0 ⟺ RH`**, where `κ` = #negative squares of the de Branges kernel = #off-line zeros (×2). **The functional equation (theta/`SL₂(ℚ)`) is NECESSARY but NOT SUFFICIENT:** a synthetic test confirmed that FE-symmetric objects with off-line zeros have `κ=2,4,…>0` (FE present, κ>0). The archimedean factor `Γ_R` alone does not collapse κ. The collapse `κ→0` requires the zeros on the line = RH. (Conrey–Li/Sarnak is the limiting case of this.)
- **FIDELITY CONFIRMED (test #4, strong marginality):** we built two functions with **identical modulus on ℝ** (via a unimodular factor) but on-line vs off-line zeros: `κ=0` vs `κ=1`. **`κ` is a PHASE invariant, not a magnitude one** — it passes the marginality theorem (12.2). Confirms that the κ reformulation is legitimate (not a magnitude functional, which could not decide RH).

---

## Transverse obstacle (affects O5 and O9)

### O11 — norm convergence of the prime part: probably FALSE
- **What we proved (hankel.md):** the rank-one edge block diagonalizes exactly; the gap is born from edge-to-edge coupling.
- **Why it does not close:** the **operator-norm** convergence `H_λ→¼|φ⟩⟨φ|` fails by **Kronecker recurrence** — `μ̂_λ(ξ)` is a finite exponential sum (almost-periodic), it does not converge uniformly at high frequency; the PNT error does not help (it controls bounded variation, not `e^{−iξv}`).
- **To close:** change topology — SOT on a dense class, or norm after a low-frequency cutoff/smoothing, or Cesàro/log averaging in λ. Rescues convergence but **changes the statement**; one must decide which is acceptable.
- **Phase 62 / E90 (2026-06-26) — Cesàro-in-λ gate, honest verdict (`E90_RESULTS.md`):** averaging the intrinsic Jacobi of `G_λ` over λ ∈ {7..21} shows: **(i)** for ζ the bulk band-width `b_bulk(λ)` is **bounded** (≈0.12, oscillates, no growth) and Cesàro-converges — i.e. the L1 boundedness `sup_λ max|A_ij|<∞` holds in the average sense; **(ii)** the DH falsador has `b_bulk` **growing monotonically** (1.38→2.18) with `max b` linear in λ (3.5→10.0) → L1 **fails**, correctly rejecting DH. **Key correction:** the `k(k+2)` band-edge ladder is **NOT** a discriminator — DH reproduces it (err 0.49) *better* than ζ (err 1.15) because the ladder is generic period-2 Dirichlet **geometry**, not arithmetic. So the load-bearing claim of 2.3.F moves from "averaged Jacobi → k(k+2)" (vacuous) to "ζ Jacobi coefficients are bounded/Cesàro-convergent" (real, falsador-separated). **C1 target accordingly = prove `b_bulk(λ)` bounded in Cesàro via PNT + unconditional zero-density.**
- **Phase 62 / C1 (2026-06-26) — VERDICT: NO-GO with insight ([phase-62 C1-ANALYSIS.md](../phase-62-cesaro-closure/C1-ANALYSIS.md)).** The Cesàro average of the zero-sum is **not** unconditional: a zero `ρ=β+iγ` contributes `λ^{2β−1}·λ^{2iγ}`; on the line (`β=½`) this is pure oscillation that averages to 0, but **off the line it is secular growth `λ^{2β−1}` that no Cesàro average removes**, and zero-density estimates bound counts/imaginary-parts, not real parts. So Cesàro-in-λ convergence of `b_bulk` is **RH-equivalent**, not RH-neutral — averaging relocates the wall but does not cross it. DH confirms: its off-line zeros make `b_bulk` grow as a positive power (log–log exponent ≈0.43) while ζ stays flat (≈0). **What survives is a detector** (`b_bulk` bounded ⟺ zeros on line), not a proof. C2–C4 (which assumed C1 closed) are **withdrawn**. The live lever remains the geometric-positivity / Hodge route, not λ-averaging.

---

## Map for the working session

- **Already closed (RH-neutral):** O6 (`I_n(L)` exact = matrix of `cos(LJ)`), O7 (Sonin λ>1 via Prüfer).
- **Closable with finite work, RH-neutral:** O1, O2, O3, O4 (technical loose ends).
- **Central knot:** O5 (rigorous gap) ↔ O11 (convergence topology). If O11 is solved in smoothed form, O5 falls.
- **Reformulation with leverage:** O8 (`H_S⪰0`) — relocates the wall to positivity of a de Branges Hamiltonian.
- **The wall = RH:** O10. Only with a new structural idea (phase). O8 and O9 are its two accesses.

---

*Phase 61 cut. Validated engine: `phase-60-discriminant/experiments/` (E4_ccm_faithful,
E11/E13 relspec, E12/E18 eigvec). Sonin construction: BC(16)+BC(17) shooting (λ=1 clean).
Anti-self-deception: reproducible numerical results; the wall (O10) is not crossed by fabrication.*
