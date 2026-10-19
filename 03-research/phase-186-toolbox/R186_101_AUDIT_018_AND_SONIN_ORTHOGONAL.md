# R186.101 — Audit of R186.018 + "Sonin-orthogonal" analysis (sign regime at ½log3)

R186_018 not modified.
Scripts (scratchpad, not versioned): `eg.py` rerun; new `egp.py`/`egp_mk.py` (mesh refined toward x = 1 and toward
the dyadic points), `grid2.py` (ε_S grid on the refined basis → `g1_RS_3_8_6_10.npz`), `w101.py`, `p2.py`, `cc101.py`.

## Label summary

| Item of 018 | Memo | Audit |
|---|---|---|
| A1 convergence of A_S (6 digits in λ₂, 1−λ₁ = 2.617e-6) | NUMERICAL | **FATAL: false.** Stable only in `lev`; drifts in p and with refinement toward x = 1 / dyadic points |
| A2 "L1 closed" | NUM + ARGUED | MAJOR: only partially (singularity at 0 resolved; those at x = 1 and 2^{−m} remain) |
| V validation ε_∞′(1⁺), ε_∞(2) | NUMERICAL | Confirmed; also confirmed against CC's K_I (see 1(d)) |
| §3 ε_S and "peak ≈ 3.6 at ρ = 2" | NUMERICAL | **MAJOR:** the peak is a Galerkin ceiling; ε_S not converged (up to 28% at ρ = 2, 20% at ρ = 3) |
| C0 (½log2: n₋(−C) = 0) | NUMERICAL | MAJOR: not robust (refined basis: n₋ = 1, eigenvalue 0.0028) |
| C1 (½log3: n₋(−C) = 2) | NUMERICAL | **FATAL for the count**: refined basis gives n₋ = 6; the two extremes (0.083, 0.040) are indeed stable |
| C2 (min E_S, values at h*) | NUMERICAL | Confirmed and **robust** (C(h*) = 0.01642 → 0.01641) |
| H (Son_S via Π_S) | OPEN | OPEN — not feasible with unconverged data (see 1(d)) |
| Verdict "no sign contact; cancellation at h*" | — | Holds (depends only on C2) |

---

# Part 1 — Audit

## FATAL

**FATAL-1 (A1: the convergence of A_S is only apparent).** Rerun `eg.py` and a family of bases:

| basis (lev,p) / refinement | n | 1 − λ₁ | λ₂ | λ₃ |
|---|---|---|---|---|
| (3,8), (5,8), (6,8), (8,8) — memo | 32–72 | 2.6175e-6 | −0.9926261 | 0.617499 |
| (3,10), (4,10), (5,10) | 40–60 | 2.6105e-6 | −0.9926568 | 0.618427 |
| (3,12), (4,12) | 48–60 | 2.6031e-6 | −0.9926874 | 0.619115 |
| (3,14) / (3,16) | 56/64 | 2.5966e-6 / 2.5959e-6 | −0.9927062 / −0.9927084 | 0.61958 / 0.61962 |
| (3,8) + 4 / 8 geometric cells toward x = 1 | 64/96 | 2.5952e-6 | −0.9927122 | 0.619689 |
| (3,8) + refinement at x = 1 and both sides of 2^{−m} (6,6) | 320 | 2.5919e-6 | −0.9927257 | 0.620101 |
| (3,10) + (6,6) | 400 | 2.5917e-6 | −0.9927265 | 0.620130 |

The memo's results depend **only on p** (lev changes nothing to 8 digits: `lev` refinement acts near 0, where the
singularity has already been absorbed by E). The "stability to 6 digits across two bases" compares two bases with the same p and the same
mesh on [½,1]: it is not a test. The eigenfunction g = E⁻¹f has singularities at x = 1 and at the points 2^{−m}
(E⁻¹ = 1 − D₂ generates jumps at the dyadic points from the jump of f at 1); the piecewise-Legendre basis resolves them
algebraically slowly. Corrected values (NUMERICAL, refined basis, not yet extrapolated): **1 − λ₁ ≈ 2.592e-6 (−1%),
λ₂ ≈ −0.992727 (memo's error 1.0e-4), λ₃ ≈ 0.6201 (memo 0.6175)**. The row (5,10,2) that the memo discarded ("D not conv.",
λ₂ = −0.992713) was the closest to the refined value.

**FATAL-2 (C1/C0: the number of negative directions of the remainder is not robust).** ε_S grid recomputed on the refined basis
(3,8,6,6) (`g1_RS_3_8_6_10.npz`, 24 min, 20 cores), M = 24, cp restriction, L²(h) metric:

| T | grid | eigenvalues > 0 of C (= negatives of −C) | min E_S | min Son_S | h*: C / Son |
|---|---|---|---|---|---|
| ½log2 | memo (5,8,1) | — | 0.5487 | 0.2589 | −0.2747 / 0.2740 |
| ½log2 | refined | **0.00284** | 0.5487 | 0.2570 | −0.2773 / 0.2714 |
| ½log3 | memo | 0.08236, 0.03969 | 9.892e-4 | 0.01459 | 0.01642 / 0.01741 |
| ½log3 | refined | 0.08326, 0.03954, **0.01333, 0.01286, 0.00512, 0.00240** | 9.892e-4 | 0.01467 | 0.01641 / 0.01740 |

n₋(−C) goes from 2 to 6 (½log3) and from 0 to 1 (½log2). Mechanism (ARGUED, consistent with R186.012 L2_S): ε_S has a
positive logarithmic singularity at ρ = 2; the form h ↦ ∫c_h(a)·β log(1/|a − log2|)da is a shift form with oscillating symbol
(~cos(s log2)/|s|), indefinite, with infinitely many eigenvalues of both signs as M → ∞ as soon as 2T > log2. Each refinement
resolves more mass of the peak and brings out new small directions. **Conclusion: "n₋ = 2" and "n₋ = 0 at ½log2" are withdrawn;
n₋(−C_{ε_S}) at ½log3 is OPEN (probably unbounded in M).** The two extreme directions (0.083, 0.040) are indeed stable to 1%.
min E_S does not depend on ε (E_S is computed directly: 9.8917e-4 in both).

## MAJOR

**MAJOR-1 (§3: the "≈ 3.6 peak at ρ = 2" is an artifact; ε_S not converged).** On the memo's grid ε_S has an exact
plateau for |a − log2| < 1e-2 (3.6176, slope in log(1/δ) = 0.004 between 1e-4 and 1e-2). On the refined basis the plateau drops to
|δ| < 1e-3 and rises to **4.6185** (+1.00). A singularity β log(1/δ) with β₁(λ=1) = 2^{1/2}(1−½)/(2log2) = **0.510**
(formula from R186.012/R186.097 evaluated at λ = 1; arithmetic verified) predicts an increase ≈ β·ln10 = 1.17 upon lowering the ceiling by a
decade: measured 1.00 (−15%). Slope measured on the memo's grid for δ ∈ [1e-2,1e-1]: 0.46 (left side) — consistent with
0.51 before the ceiling. **Answer to (b): the measured peak is consistent with a log of coefficient ≈ 0.5 truncated by resolution;
"ε_S ≈ 3.6 at ρ = 2" is not a value, it is the height of the ceiling.** Also ε_S differs between bases away from the peak:
ε_S(1.5) 1.463 → 1.401, ε_S(1.9) 3.090 → 2.825, ε_S(3.0) 0.625 → 0.496 (Gibbs-type oscillation). The "1e-5 uncertainty between
the two good bases" again compares two bases with the same p: false as a bound.
What **is** robust: C at h* (1e-5), C at v₁, v₂ (1%), min Son_S (0.5%). Why: c_{h*} is small near a = log2
(integrable against a log), and the extremes of C are dominated by the bounded part of ε_S.

**MAJOR-2 (A2: "L1 closed").** The singularity at 0 is indeed absorbed by E (convergence in `lev` is immediate); but
L1 is only closed to 1% for 1 − λ₁ and 1e-4 for λ₂. The amplification 1/(1−λ₁²) ≈ 1.9e5, which the memo itself notes, means that
a 1% error in 1 − λ₁ becomes a 1% error in the dominant part of ε_S. Label: **L1 PARTIAL** (OPEN for λ₂, λ₃ and for pointwise ε_S).

**MAJOR-3 (C0 "trivial dominance at ½log2").** With the refined ε_S, a direction with C = +0.0028 appears at ½log2. Although
tiny compared with min E_S = 0.549 (the positivity of E_S is not at stake), the statement "the remainder has no negative direction"
is false as a claim: the peak at a = log2 = 2T lies at the edge of the support of c_h.

## MINOR

- **(c) archimedean vs R186.099.** Verified: −0.03246 / −0.03376 / −0.03448 (M = 16/20/24). The "−0.032" of R186.099 is the
 M = 16 value; the eigenvalue is not converged in M (drift ~6% from 16 to 24). n₋ = 1 is indeed stable.
- **Test (c) values verified** (memo's grid, M = 24): v₁: C 0.08236, E 0.12968, Son 0.21203; v₂: C 0.03969,
 E 0.26407, Son 0.30376; h*: E 9.8917e-4, C 0.01642, Son 0.01741, ⟨h*,v₁⟩ = 0.000; min Son 0.01459; two restrictions:
 n₋ 2, min E 0.0360, min Son 0.0720. Everything matches the memo's table (at its ε resolution).
- The check "bases (3,8) vs (5,8): max|dC| ≈ 1e-7" from `win18.py` proves nothing (same p, same mesh on [½,1]).
- §1 "Γ_d ~ c·2^{−d} ⇒ exact first-order geometric closure": confirmed empirically (D = 14…18 identical to 1e-10 with
 lev ≥ 3); the convergence issue is not in D but in p/mesh (FATAL-1).

## 1(d) What was missing

**(d1) Son_S via independent Π_S — NOT DONE, OPEN, with diagnosis.** Halmos's formula is correct in the model u
(F_S self-adjoint with a kernel symmetric in xy and F_S² = 1 ⇒ unitary): with F_S = [[A, X],[X*, B]] on ran P ⊕ ran Q₁,
B² = 1 − X*X, and X*X has the nonzero spectrum of 1 − A²; hence **Π_S = Q₁F_SQ₁F_SQ₁ − Σ_n λ_n²|ζ_n⟩⟨ζ_n|,
ζ_n = Q₁F_Sφ_n/√(1−λ_n²)**, equivalently Π_S = Q₁ − Π_Z, Z = cl(Q₁F_S ran P) (PROVED, two-projection algebra).
But an independent computation of Tr ϑ(f)Π_S needs either (i) Tr ϑ(f)Q₁F_SQ₁F_SQ₁ — the semilocal analogue of CC (43), which
is not available via a route independent of (83)/(84)_S (it would be circular), or (ii) the regularization
Son = lim_L [L‖h‖² − Tr(ϑ(f)Π_Z 1_{t<L})], which requires that span{Q₁F_Sφ_i} cover the logarithmic phase plane up to t = L
(dyadic mesh up to e^{−L}) **and** converged eigendata; moreover A_S ∉ S₂ (only S_p, p > 2), so Σλ_n²⟨ζ_n,ϑζ_n⟩ diverges and
must be compensated against δ_S, for which there is no closed formula in the record. With FATAL-1, the "converged eigendata" the
goal requires do not yet exist. **The exact-constant check pending since R186.017 remains pending.** Minimal plan:
route (ii) first in the archimedean case (it must reproduce W_∞ + C_{ε_∞}, CC (83) CITED) and only then the semilocal case.

**(d2) Comparison with λ_max(K_I) ≈ 1.0516 from CC at ½log2 — DONE (NUMERICAL), agreement.** CC Prop. 5.5 / §6.7 works in
H = L²(I,dx) for the variable ξ (h_CC(ρ) = ξ(log ρ), g = (½ − ρ∂_ρ)h_CC, i.e. our h = ξ/2 − ξ′), with
⟨ξ|N_Iξ⟩ = E(g*g^*) = our C(h), N_I = −c(Id − K_I). Precise metric difference: integrating by parts,
c_h = (¼ − ∂²)c_ξ, and since ε(e^{|a|}) has a corner at a = 0 with slope ε′(1⁺) = 22.9965 on each side, −∂² produces a point
mass −2ε′(1⁺)δ₀: **c = 2ε′(1⁺) = 45.993** is the weight of the identity in the ξ metric. Sylvester: the inertia does not depend on the metric.
Results (`cc101.py`, ε_∞ λ = 1, ½log2):

| M | unrestricted: n₊(C) | max C (ξ) | 1 + max/45.993 | ⟨ξ₀|ζ⟩ | with cp: max C (ξ) → 1 − |·|/45.993 | with cl |
|---|---|---|---|---|---|---|
| 16 | 1 | 2.1959 | 1.0477 | 0.9434 | −15.279 → 0.6678 | n₊ = 0 |
| 24 | 1 | 2.2849 | 1.0497 | 0.9472 | −14.763 → 0.6790 | n₊ = 0 |
| 32 | 1 | 2.3199 | 1.0504 | 0.9488 | −14.553 → 0.6836 | n₊ = 0 |
| CC | 1 | — | **1.05158** (±0.00122) | **0.94865** | λ₂ = 0.6865 | (ĝ(0)=0 kills ζ) |

Thus: (i) our L²(h) picture at ½log2 has **one** unrestricted positive direction of C (max 0.0852 in L²(h), M = 32),
exactly CC's ζ (⟨ξ₀|ζ⟩ → 0.9487 ✓); (ii) the cl restriction (∫ξ = 0 ⇔ ĝ(0) = 0, CC's) kills it, and **cp kills it too**
(∫ξe^{x/2} = 0): that is why the memo saw n₋ = 0 with cp; (iii) λ_max and λ₂ converge toward those of CC (difference at M = 32:
1.2e-3 and 3e-3, within/close to CC's bound ε₁ = 0.00122; linear extrapolation in 1/M ≈ 1.051). **The pipeline validation
becomes quantitative**, not just ε′(1⁺) and ε(2). (Archimedean only; the semilocal case has no analogue in CC.)

---

# PART 2 — Where does window positivity live at ½log3? (NUMERICAL)

## 2.1 Typical sizes of Son_S

𝒫_T, M = 24, cp, L²(h) metric, dim 23 (both ε grids agree to 1e-3):

| T | mean of Son_S over an ONB (= Tr/23) | spectral median | min Son_S | Son_S(h*) | max Son_S |
|---|---|---|---|---|---|
| ½log2 | 2.151 | 2.26 | 0.257 | 0.274 | 3.49 |
| ½log3 | 1.669 | 1.72 | **0.0146** | **0.0174** | 3.12 |

At ½log3, Son_S(h*) is **1.0%** of the typical value, and h* is nearly aligned with the lowest eigenvector s₀ of Son_S
(|⟨h*,s₀⟩|² = 0.996). Interpretation (PROVED as an identity, Son_S(h) = Tr ϑ(g)^*Π_Sϑ(g) = ‖Π_Sϑ(g)‖²_HS, f = g*g^*):
the scale orbit of h* carries almost no Hilbert–Schmidt mass in the semilocal Sonin space.

**On "components in ran P, ran P̂^S and their complement": ill-posed as stated — NOT DONE.** ‖Pϑ(g)‖²_HS = ‖Q₁ϑ(g)‖²_HS = ∞
(ϑ(g) is a convolution on ℝ*₊, not HS); only the Sonin component is finite. "h* lives almost entirely in ran P + ran P̂^S" is therefore
true for **every** h in a relative sense (infinite total mass, finite Sonin mass) and does not single out h*. The only version
with content is the comparative one: Son_S(h*)/‖h*‖² ≪ mean — already measured above.

## 2.2 Test of the two-regimes conjecture — **FALSIFIED at ½log3**

Conjecture proposed in the goal: "in the nearly Sonin-orthogonal subspace V_δ = {Son_S < δ}, C ≤ 0" (equivalently,
the remainder is positive — −C ≥ 0 — where Son_S ≈ 0). Result:

| T | grid | direction | Son_S | C | E_S |
|---|---|---|---|---|---|
| ½log3 | memo | s₀ (lowest eigenvector of Son_S) | 0.01459 | **+0.01031** | 0.00428 |
| ½log3 | memo | s₁ | 0.07197 | −0.01105 | 0.08302 |
| ½log3 | memo | h* | 0.01741 | **+0.01642** | 0.00099 |
| ½log3 | refined | s₀ / h* | 0.01467 / 0.01740 | **+0.01045 / +0.01641** | 0.00422 / 0.00099 |
| ½log2 | both | s₀ | 0.257 | −0.302 | 0.560 |

V_δ at ½log3: δ ≤ 0.05 → dim 1 (s₀), C = +0.0103 > 0; δ = 0.1, 0.2 → dim 2, C|_V with eigenvalues [−0.011, +0.010]: **C is not ≤ 0
in V_δ for any δ.** At ½log2 it is (C < 0 on the first two eigenvectors of Son), but there is no gap to explain there.

**What the numbers show instead (NUMERICAL, robust across the ε grid):** the structure is the opposite — an **absorption
regime**. Let ρ*(T) := sup_{h∈𝒫_T} C(h)/Son_S(h) (largest generalized eigenvalue of the pair (C, Son_S)). Since E_S = Son_S − C
and Son_S ≻ 0,

 E_S ≻ 0 on 𝒫_T ⟺ ρ*(T) < 1, and min E_S/Son_S = 1 − ρ*.

| T | grid | ρ* | 2nd | |⟨maximizer, h*⟩|² |
|---|---|---|---|---|
| ½log2 | memo / refined | −0.0004 / +0.0010 | −0.0005 / −0.0004 | — |
| ½log3 | memo / refined | **0.9437 / 0.9436** | 0.640 / 0.638 | **1.0000** |

At ½log3 the remainder is **positive and absorbs 94.4% of the Sonin mass precisely in the direction where that mass is minimal**;
the maximizer of C/Son_S coincides with h* (the minimizer of E_S in L²(h)). The gap is not at a boundary between two regimes
but at the maximum of a ratio: margin 1 − ρ* = 0.056. The only other relevant direction (v₁, the most negative direction of −C)
has C/Son = 0.39: there Son does dominate.

## 2.3 Precise formulation and status

**Conjecture RB(T) (relative bound of the remainder by the Sonin form).** There exists η(T) > 0 such that for every h ∈ 𝒫_T
(primitive, support in [−T,T]),
 ∫_ℝ c_h(a) ε_S^{(1)}(e^{|a|}) da ≤ (1 − η(T)) · Tr ϑ(g_h)Π_{S}ϑ(g_h)^*, S = {∞,2}, λ = 1.

- **Equivalence:** RB(T) ⟺ E_S ≥ η·Son_S on 𝒫_T, by identity D3 (Son_S = E_S + C, PROVED at λ = 1). It is a
 **restatement**, not a reduction: it only helps if C and Son_S can be bounded separately (C from above via the positive part of
 ε_S, Son_S from below via the geometry of Π_S — e.g. a lower bound on ‖Π_Sϑ(g)‖_HS in terms of ‖h‖ and T).
- **Status:** NUMERICAL at ½log2 (ρ* ≈ 0, trivial) and ½log3 (ρ* = 0.9437, M = 24, stable to 1e-4 across ε grids). OPEN in general.
- **What must be proved, stated precisely:** in the direction s₀ of minimal Sonin mass, ∫c_hε_S ≤ (1−η)‖Π_Sϑ(g_h)‖²_HS.
 Since C(s₀) > 0, no sign argument on ε_S restricted to Sonin-orthogonal autocorrelations suffices (the conjecture
 is a NO-GO as a mechanism: explicit falsifier s₀/h* at ½log3); what is needed is a **quantitative inequality**
 between two positive quantities of the same order (0.0164 vs 0.0174).
- Structural question that is indeed well posed (OPEN): do the maximizer of C/Son_S and the
 lowest eigenvector of Son_S coincide asymptotically (M → ∞)? At M = 24: |⟨h*,s₀⟩|² = 0.996. If so, RB(T) reduces to a scalar
 inequality on a single direction (the one of minimal Sonin mass), which is an object defined without the window.

## Final labels of this note

| Item | Label |
|---|---|
| FATAL-1 (A_S not converged; corrected values 1−λ₁ ≈ 2.592e-6, λ₂ ≈ −0.99273) | NUMERICAL |
| FATAL-2 (n₋(−C) 2 → 6 at ½log3, 0 → 1 at ½log2) | NUMERICAL; n₋ OPEN |
| ε_S peak at ρ = 2 = Galerkin ceiling of a log singularity of coefficient ≈ 0.5 (β₁ = 0.510) | NUMERICAL + ARGUED (L2_S PROVED) |
| Halmos Π_S = Q₁F_SQ₁F_SQ₁ − Σλ_n²|ζ_n⟩⟨ζ_n| | PROVED |
| Son_S via independent Π_S | OPEN (not feasible without converged eigendata or δ_S) |
| Agreement with CC's K_I (λ_max 1.0504→1.0516, ⟨ξ₀|ζ⟩ 0.9488, λ₂ 0.684, c = 2ε′(1⁺)) | NUMERICAL |
| Conjecture "C ≤ 0 on the Sonin-orthogonal part" | **NO-GO (explicit falsifier s₀, h* at ½log3)** |
| Absorption regime ρ*(½log3) = 0.9437 at h* | NUMERICAL |
| RB(T) | CONJECTURE (≡ E_S ≻ 0 via D3; restatement) |
