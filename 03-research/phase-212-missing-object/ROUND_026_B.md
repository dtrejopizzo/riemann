# Round 026 B — (PBP_T) as an exact extremal problem; Kreĭn and density argument; four-point gate

Object: the form `a^w_T` on `P_T` (Paper 47, `04-papers/47-row-d-dual-certificates/main.tex`). No long
derivations. Opened: R160_M2_R1 complete; G2_B9_R3 §3; P47 `eq:m`, `eq:Aform`, `eq:Kprim`, `prop:finite`, `lem:degen`,
`rem:resweights`; R155_033 §0, §2.1–2.3; index, entry 212-25; ROUND_025_A (grep). Not opened: R155_023/024/027
(thresholds and Theorem N′, only via their summary in the README of phase 155), R155_049, ROUND_025_B, G2_B6_R2.

## 1. Exact formulation (already done in the corpus)

Verbatim from the paper (`eq:m`, `eq:Aform`, `eq:Kprim`): for real `F`, `‖F‖=1`, `c=c_F`,
```
𝔞^{(w)}_T(F) = C_0·c(0) + 𝔈(c) − Σ_{n∈N_T} w_n c(log n),   𝔈(c) = ∫_0^∞ (c(0) − c(u)) K(u) du ≥ 0,
C_0 = ψ(1/4) − log π = −5.3721834…,   K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)),
K(u) = 1/u + O(1) (u↓0),   K(u) = 2e^{−u/2}(1+O(e^{−u})) (u→∞).
```
Pole terms: in the complete form one adds `2A(F)B(F) = 2∫c(u)cosh(u/2)du` (R160_M2_R1 Rem. 2.5). On `P_T`
they disappear and primitivity becomes two linear constraints on `c` (`eq:Kprim`):
`∫ c(u) cosh(u/2) du = 0`, `∫ c(u) u sinh(u/2) du = 0`. Since `c` vanishes for `|u| ≥ 2T`,
`𝔈(c) = ∫_0^{2T} (1 − c)K + ∫_{2T}^∞ K`, and the last summand is `≈ 4e^{−T}`.

Extremal problem (relaxed to mixed states, convex):
```
Z^prim_T = inf { C_0 + 𝔈(Φ) :  Φ even, positive definite, Φ(0)=1, supp Φ ⊂ [−2T,2T],
                 ∫Φ cosh(u/2) = ∫Φ u sinh(u/2) = 0,  Φ(log n) = 0  ∀ 2 ≤ n < e^{2T} } ;
(PBP_T):  Z^prim_T ≥ 0  (equivalently K_T = 𝒱^prim_T ≠ ∅).
```
**Already done (CITED, PROVED there):** it is literally R160_M2_R1 D4–D5, Thm 4.1 (strong duality; the optimal weight is the
Lagrange multiplier of the constraints `Φ(log n)=0`), Thm 4.3(a) (`𝒱^prim_T ≠ ∅ ⟺ Z^prim_T ≥ 0`), Rem. 4.4
(`T→∞` version) and §7.1. Without the contact constraints it is the program `(P_∞)` of R155_033 §2.1–2.2. Nothing new in (1).

## 2. The Kreĭn argument plus density of `log ℕ`: what it gives

Tool (CITED, standard): for positive-definite `Φ` with `Φ(0)=1` there is a Hilbert space with unit
vectors `ξ_u`, `⟨ξ_u, ξ_{u′}⟩ = Φ(u − u′)`. With `ω := 1 − Φ ∈ [0,2]` and `d(h) := ‖ξ_h − ξ_0‖ = √(2ω(h))`:
(K1) `|Φ(u) − Φ(u′)| ≤ d(u − u′)` (Kreĭn); (K2) `d` is subadditive, hence `ω(s) + ω(h−s) ≥ ω(h)/2` for `0 ≤ s ≤ h`.

Consequences (PROVED, one line each; `K` decreasing):
- **Far field.** If `g(u) := dist(u, {log n: n≥2})`, then `|Φ(u)| ≤ D(g(u))`, `D(r) := sup_{|h|≤r} d(h)`, and
  `ω(u) ≥ 1 − D(g(u))`. On `[log N, ∞)` one has `g ≤ ½ log(1+1/N)`, so
  `∫_{log N}^∞ ωK ≥ (1 − D_N) ∫_{log N}^∞ K`, `D_N := D(½log(1+1/N))`.
- **Near 0.** By (K2), `∫_0^h ωK ≥ (ω(h)/2) ∫_{h/2}^h K ≈ (log 2/2) ω(h)`; with `ω(h) = D²/2` at the point where
  `D_N` is attained, the contribution is `≥ (log 2/4) D_N² ≈ 0.173 D_N²` (≤ 0.69).
- **First contact.** `ω(log 2) = 1` and (K2) give `∫_0^{log 2} ωK ≥ ½∫_{½log2}^{log 2} K = 0.4266`.

Resulting bound (PROVED as an inequality, except for the overlap of the two bounds on `[0, log 2]`, which can only
lower it): `𝔈(Φ) ≥ min_{D∈[0,2]} [ (1−D)_+ ∫_{log 2}^∞ K + max(0.4266, 0.173 D²) ]`. Values (NUMERICAL, mpmath):
`∫_{log 2}^∞ K = 2.9937`, `∫_{log 7}^∞ K = 1.5181` (the figure 1.5 of H1), `∫_{log 3}^∞ K = 2.3642`.
**Ceiling of the method: `𝔈 ≥ ~3.0–3.4` (in the best case `D=0`), against `−C_0 = 5.372`. About `≈ 2.0` is missing (at least 1.7 even
adding the two bounds without overlap, ≤ 3.7).** It does NOT reach; it is not forced.

Where the missing part would have to come from (ARGUED). Archimedean positivity on short windows (`T*_{∞,P} ≈ 0.58–0.60`)
comes from the singularity `K ~ 1/u`: a `Φ` that drops from 1 to 0 at scale `h` pays `≈ log(1/h)` for *all* the dyadic
scales between `h` and 1. (K2) only charges one scale (a factor `log 2`), not the dyadic sum. What is missing is a
**multiscale uncertainty principle for positive-definite functions vanishing on `log ℕ`**: a lower
bound on `∫_0^1 ωK` growing like `log(1/g)` when the vanishings force variation at scale `g ≍ e^{−u}`. It is the
"boundary" wall of R155_033 §0 (`thm:O`, already present with `v=0`), now on the primal side. Without it the argument only
charges the tail of `K`, which is `O(1)` and bounded by `∫_{log 2}^∞ K < 3`.

Primitivity. In the argument of (2) it **does not enter**: (K1)–(K2) hold for every positive-definite `Φ`. Its only
possible role is to force `Φ` to have negative mass weighted by `cosh(u/2)` far from 0, which clashes with `|Φ| ≤ D(g)`. But
the weight reaches `e^{T}`, so amplitude `≍ e^{−T}` far away suffices, which (K1) allows with `D ≍ e^{−T}`: asymptotically
null contribution along this route (ARGUED, not quantified with mixtures). Quantifying it: OPEN.

## 3. Antecedents and what of (1)–(2) already exists

- R160_M2_R1: (1) complete (D4–D5, Thm 4.1–4.5, Rem. 4.4, §7.1–7.2); §6 H1 is the heuristic version of (2) with
  `|c′| ≤ Ω` instead of (K1), and already concludes "≈1.5, not enough against 5.37 by crude bounds". (2) is H1 made rigorous and
  barely improved (from 1.5 to ≤ 3.4 by using all of `[log 2, ∞)` and (K2)); the deficit remains.
- R155_033 §2.2: the same count on the dual side ("`τ=0` cap"): a certificate needs `∫_{2T}^∞(1−w)K ≥ 𝔈(c_{F⋆})`,
  and the tail of `K` alone does not suffice (factors 2.3–2.6). It is the dual version of the ceiling of (2).
- R155_033 §0, Thm AL (only `(D_∞)`; corrected by R155_049 to `Θ(1/M)` in the full program): the wall is the boundary
  of the window, not the lattice. Coincides with the diagnosis of §2.
- P47 `lem:degen`, `rem:resweights`: define concave `μ_T` and the degenerate case; `prop:finite`(ii)–(iii): `𝒱_T`
  closed convex, `0 ∉ 𝒱_T` for `T ≥ 0.60`.
- G2_B9_R3 §3 (Thm N, R′): rigidity only for `w − v ∈ 𝒯_meas`; for non-tempered weights, gap recorded in 212-25.
- Grep "Kreĭn inequality / 1 − Re": there is no use of (K1)–(K2) on `Z^prim_T` in the corpus (the matches in 211
  ROUND_012_B/016_A/024_A, 212 ROUND_018_A and R162_1301 are other objects: Kreĭn/Pontryagin spaces, Q function).
  A search without matches does not prove conceptual novelty: (K1) is exactly the control of H1.

## 4. Four-point gate

1. **Closest antecedent:** R160_M2_R1 §6 H1 and §7.1 (plus D5, Thm 4.1/4.3); on the dual side R155_033 §2.2.
2. **What is new:** replacing the band hypothesis `|c′| ≤ Ω` of H1 by (K1)–(K2), valid for every `Φ` of the mixed
   class, and the exact computation of the ceiling (≈ 3.0–3.4 versus 5.372). It is a refinement of a heuristic, not an object.
3. **Does it avoid the antecedent's difficulty?** No. The difficulty of H1 was that the tail of `K` only gives `O(1)`; (K1)–(K2)
   charge the same tail and a single scale near 0. The deficit `≈ 2` lies in the dyadic sum of the singularity,
   which no three-point inequality sees.
4. **Connection with the global target:** (PBP_T) ∀T ⟹ `K_T ≠ ∅` ∀T ⟹ (Tychonoff, 212-25) a `w` with `a^w_T ≥ 0` ∀T;
   passing from that `w` to the true weight requires rigidity for weights with `|w_n| ≲ log n`: **CONDITIONAL** (212-25).
   (PBP_T) ∀T by itself **would be a new theorem relative to the corpus** (OPEN in R160 §7.1 for `T > log 2` pure and
   `T > 0.8` relaxed; no falsifier nor impossibility proof): it would say that *no primitive state whose
   autocorrelation vanishes at every `log n` has negative archimedean energy*, with all the content in the
   positions `log n` and none in weight values. It does not give the sign of the target without rigidity.

Controls. (PBP) has no weight; the control is the lattice. In (2) the lattice enters **only** through two data: the gap
function `g(u) ≤ ½log(1+1/⌊e^u⌋)` and the position of the first contact `log 2`. No step uses that the set is
exactly `log ℕ`: for the integers coprime to `p` the gaps grow at most by a factor `p/(p−1)` and the
first contact moves to `log 3` (`p=2`), with ceiling `∫_{log 3}^∞ K = 2.36`, smaller; a Beurling system with the same
gap profile gives the same bound. The argument varies continuously and does not separate `log ℕ` from its neighbors (if (PBP)
failed for one of them, this method would not see it). The only place where the integer structure could enter and is not used:
in the GNS space, `ξ_{log m} ⊥ ξ_{log n}` when `n | m` (since `Φ(log(m/n)) = 0`); but that divisibility relation
is shared by every multiplicatively closed system (Beurling included), so it does not separate either. Recorded, not
exploited.

## Verdict

**DOES NOT PASS (repetition, and no mechanism).** (1) is done (R160_M2_R1 D4–D5, Thm 4.1/4.3). (2) is H1 of R160 §6 with
(K1)–(K2) instead of band-limitation: ceiling PROVED-as-bound `𝔈 ≳ 3.0–3.4 < 5.372`, deficit `≈ 2`; primitivity does not
enter the argument (contribution ARGUED asymptotically null). What is missing is a multiscale bound on the singularity
`K ~ 1/u` forced by the vanishings (boundary wall of R155_033), not the tail of `K`. (PBP_T) ∀T remains OPEN and would be
new; its connection with the target is CONDITIONAL on rigidity for non-tempered weights (212-25). Reopening: an
uncertainty principle for positive-definite `Φ` vanishing on `log ℕ` that charges `≳ log(1/g)` across scales.
