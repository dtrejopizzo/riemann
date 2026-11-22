# Phase 190 — Near-coincidence discovery experiment on the integer-lattice matrices A_M

Nothing in this phase uses or mentions any equivalence
between row D and any other statement. Approved numerical DISCOVERY run (double precision, convergence-checked, NUMERICAL; not
certified). No edits to Paper 46, the grid or the routes index; proposed index rows are in memos/EXP_005 §4.

Object: Paper 46 sec:combs — profile F₀ of thm:oneprofile (g = e^{bt}1_{[0,a]}, |b| > ½, T₀ = 2a, F₀ = (¼−∂²)(g*g̃*g*g̃)), lag function
B(d) = Arch(d) − X(d), matrices A_M = [B(log m − log k)]_{m,k≤M} = Arch_M − Div_M − Near_M (prop:AM). Secondary object: (Ω₀), the clamped
ground-mode test (index R2; L2_BUILD_008/009).

## Files
- `memos/EXP_001_SETUP.md` — exact implementation, precision and convergence checks, ranges computed (M ≤ 3000, T₀ ∈ {0.05, 0.15, 0.3}, b ∈ {1, 2, −1}).
- `memos/EXP_002_CONTROLS.md` — 24 controls in the same run: a₃, a₅, amp2(c), pert_n(±10⁻⁵, ±10⁻²), Beurling (two lattices), Poisson (5 seeds), M₁ (δ = 0.1, 0.3); first negative M; amplification threshold c*(M); where the controls fail; 2×2 band to d = 15.
- `memos/EXP_003_NEAR_STRUCTURE.md` — λ_min(A_M(Λ)) = M^{−3+o(1)}; the minimizer ≈ m^{−½}; three-way decomposition; per-atom cancellation and the defect at n = 2, 3, 4; Near matrix statistics; packet family.
- `memos/EXP_004_OMEGA0.md` — (Ω₀) on T ∈ [0.40, 1.10] with controls.
- `memos/EXP_005_CONJECTURES.md` — regularity table with ζ-specificity class, conjectures C1–C3 with status and proof-route assessment, the cutoff result for the minimizer's correction, proposed index rows, exact next step.
- `scripts/` — profile.py (kernels, FFT, convergence check), am.py (matrix builder, combs), run_main.py, run_controls.py, run_band.py, analysis_min.py, near_triples.py, packets.py, identity_check.py, epsilon.py, omega0.py, test1.py (verification).
- `data/` — JSON/NPZ outputs and logs of every run.

## Results in one paragraph
A_M(Λ) ⪰ 0 at every (T₀, b, M) computed; no sign contact. λ_min(A_M(Λ)) decays like M^{−3} (exponent 2.89 → 2.98), so the matrices are
critical: the amplification threshold at n = 2 is c*(M) ≍ λ_min/0.18 ≍ M^{−3}, and a 10⁻⁵ change of v₂ makes A_M indefinite from
M ≈ 200–400. Every control is indefinite at M ≤ 400 (structural controls already at M = 50, with O(1)–O(100) negativity); their negative
eigenvectors are smooth packets of consecutive integers at the top of the window, with Near(v) ≈ Arch(v) + |λ| and Div ≈ 0. The minimizer
of A_M(Λ) is of a different kind: entrywise positive, equal to m^{−½}·w(m/M) with a smooth cutoff w (correction at fixed m → 0 as M grows;
no arithmetic correction), with Div(v) ≈ log M, Near(v) ≈ −Div(v), Arch(v) ≈ 0.3; every atom n ≥ 5 cancels its own divisor part to 3
decimals, and the comb balance against the archimedean energy is carried by the near-coincidence defects at n = 2, 3, 4 alone. On the pure
vector m^{−½} this is an exact identity, s^T(Div+Near)s = 2Σ_N N^{−½}log N·E_M(N), checked to 12 digits (W7 class, no sign). The minimizer's
Dirichlet polynomial vanishes at the zero ordinates (it is a smoothed partial sum of ζ(½+iτ)): the only ζ-specific mechanism found is
zero-side. The 2×2 band kills Poisson/Beurling/a₅ but is passed to d = 15 by a₃, amp2(0.05), pert₂(1.01), which are indefinite at M ≤ 200.
**No prime-side structural fact about Near was found that holds for Λ and fails for every control.** (Ω₀) holds for Λ on T ∈ [0.55, 1.10] with margin 𝔞_T(φ₀) ∈ [0.016, 0.091] (Galerkin, N = 14/20 agree to 2·10⁻⁴); a₃, a₅ fail from T = 0.60, Poisson combs fail at various T, but amp2(0.05) and the 10⁻² perturbations pass at every T — (Ω₀) is necessary only (EXP_004).

## Status labels
NUMERICAL for every numerical statement; PROVED for the lattice identity of EXP_003 §4 / EXP_005 C3 (elementary); no new label on any cell
of the grid; R9 and R2 remain OPEN. Exact next step: EXP_005 §6 (explicit decomposition of Q_M(w) on the family s_w = m^{−½}w(m/M) into a
bulk part — defects at N = 2, 3, 4 against archimedean energy — and an edge part at scale M; check the edge part against [void]).
