# R154.014 — Blueprint, round 5 of phase 154: (P154.1) two incommensurable contacts — the staircase to log 2.

## 0. State
Theorem C(½log3) PROVED (one contact, `n = 2`; certificate `CERT_log3_M24.json`; c = 4.43·10⁻⁵ vs λ_min = 9.8·10⁻⁴). Lemma D2.3's tail
collapse used the periodicity of the whole prime term; with contacts `{2,3}` (`½log3 < T ≤ log 2`) the prime term is quasi-periodic.
Targets (R153_012 table, L² normalisation): λ_min(A_T|P_T) ≈ 2.16e-4 (T=0.58), 1.91e-5 (0.62), 2.40e-6 (0.65), 3.24e-7 (0.68), 1.09e-7 (log 2).
Best certificate at log 2 so far: −8.49e-2.

## 1. Two separate difficulties, two separate constructions
(F1) **Two-frequency tail lemma (PROVE).** With ν on a lattice `u_j = j·2T/M` (period `P = 2πM/2T` for ν̂) and `β·ĝ = O(1/τ)`, prove an
explicit `τ₁(ρ, β, T)` such that for `τ ≥ τ₁`: `Re ψ(¼+iτ/2) − log π − 2(w₂+w₃) − ρ − |β·ĝ(τ)| ≥ c₀ > 0` (use the monotone lower bound
`Re ψ(¼+iτ/2) ≥ log(τ/2) − const` with an explicit constant, proved). Then on `[τ₀, τ₁]` handle the prime term either (i) by direct stack
B&B (the prime term has Lipschitz constant `2(w₂log2 + w₃log3) ≈ 2.07`, cheap), or (ii) by a **two-frequency collapse**: for each period of
ν̂, bound `−2w₂cos(τlog2) − 2w₃cos(τlog3)` below by its exact minimum over the period window via a fine grid + its Lipschitz constant
(graded RHS as in D2.3 but with the prime term's own certified minimum per period). State the lemma, prove it, and give the cost model.
(F2) **Precision.** Below ~1e-6 a double-precision LP (HiGHS, tol 1e-7) cannot certify. Build a **high-precision polish**: take the LP's
active set (contact points and active atoms), and solve the equality system for `(a_j, β₀, β₁, c)` in mpmath at 40+ digits (Newton on the
KKT/active-set equations, or re-solve the reduced LP with exact rationals via fractions/sympy if the active set is small); verify with
mpmath.iv. Demonstrate the polish first at `½log3` on the existing certificate (does the certified c rise from 4.43e-5 toward 9.8e-4?).

## 2. The staircase (each step is a theorem; stop climbing when a step fails and report why)
Step 1: `T = 0.58` (contacts 2,3; target 2.16e-4). Step 2: `T = 0.62` (1.91e-5). Step 3: `T = 0.65` (2.40e-6). Step 4: `T = 0.68` (3.24e-7).
Step 5: `T = log 2` (1.09e-7). For each step: LP shape (grid on `[0, τ_max]` plus tail row from F1), block polish (G ≥ 128 columns on a
1000× finer grid as in round 4), high-precision polish (F2) if needed, exhaustive verification (stack B&B, `L·w/2` subtracted, no discards,
budget → raise), iv enclosures at the minima, archive `CERT_T<value>.json` with exact decimals. Record for each step: `N`, `M`, `β₀, β₁`,
`ρ`, `τ₁`, certified `c`, `c/λ_min`, evaluations, wall time. Also record the fraction `c/λ_min` trend: if it collapses as `T → log 2`, say
which of (F1)/(F2)/LP-grid saturates.

## 3. What to read in the certificates (DIAGNOSTIC)
`β₀ → 2`? (polar term restored with two primes too); do atoms develop structure tied to `log 3 − log 2 = log(3/2)` or to `2T − log 3`
(the distance of the new contact to the window edge — R153's needle location); contact comb vs prime frequencies.

## 4. Rules
Labels; FATAL rule (all `T ≤ log 2` are Paper-42-certified; a new-method proof is the point; nothing beyond `log 2`); corpus-check lines
("two-frequency", "quasi-periodic", "cuasiperi", "high-precision LP", "active set"); scripts in `scripts/round5/`; deliverable
`R154_015_ROUND5.md` (≤ 5000 words) with the staircase table and the archived certificates. Compute budget is real: plan the
exhaustive covers (round 4: 2.4e8 evaluations ≈ 30 min); prefer Taylor/second-derivative bounds over pure Lipschitz if they cut evaluations.
