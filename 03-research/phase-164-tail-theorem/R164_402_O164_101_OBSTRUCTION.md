# R164_402 — O164.101, obstruction side: what POSITIVITY + FE + POLAR DATA force

Round 2, line L1 (obstruction side). Pure math, no numerics. Sources read: R164_190 §Síntesis,
R164_102 (Thm L, Cor L.1, Prop W, Thm H, Prop I), R164_101 (Thm E1, Prop D), R163_401 §2.4/§3/§4.8/§4.11(c) (Thm F, f_t),
R163_1001 Thm O, R163_101 §5, grid R162_2300 §3.

**Verdict.** No obstruction proved. O164.101 is **reduced exactly** (PROVED) to a positive Poisson-summation problem:
a self-dual positive tempered measure that equals the Poisson comb on (−e^L, e^L). In that form, four new constraints are
PROVED: the perturbation must change sign (no pure addition and no pure deletion, at either the N-level or the μ-level),
its deleted mass must be infinite, and it must be locally balanced. The question "does a member with an off-line zero exist"
stays **OPEN**, and so does the weaker question "does 𝒞 contain anything except ζ". **O164.101 ⇒ RH** (PROVED, trivial).
The converse is OPEN. If 𝒞 = {ζ}, O164.101 ⟺ RH and the result is identification (W3′), with no sign.

## 0. Status table

| # | statement | status |
|---|---|---|
| (a) | ζ_B ∈ 𝒞 ⇒ σ_c(μ_B) = 1, ζ_B ≠ 0 on Re s > 1, and on Re s < 0 only trivial zeros | PROVED (Landau + Euler exp; FE) |
| Prop P | **Poisson form.** ζ_B ∈ 𝒞 (finite order) ⟺ M_B := δ₀ + dN_B(\|x\|) (even, on ℝ) is tempered, M_B ≥ 0, \hat M_B = M_B, and M_B = Π := Σ_{n∈ℤ}δ_n on (−a,a), a = e^L. Here dN_B = exp^*(μ_B) (in x = e^u) | PROVED (Hecke–Mellin; density of x^{2k}e^{−πx²}) |
| Lem G | Δ := M_B − Π is real, even, self-dual, Δ = 0 on (−a,a), so Δ*K ≡ 0 for every K with supp \hat K ⊂ (−a,a). This is Prop W, measure form | PROVED |
| Prop S | **Sign change forced.** Δ ≥ 0 ⇒ Δ = 0, and Δ ≤ 0 ⇒ Δ = 0. Hence ν ≥ 0 ⇒ ν = 0 (recovers Cor L.1 inside 𝒞) and ν ≤ 0 ⇒ ν = 0 (**new**: no pure deletion) | PROVED |
| Prop F | **Infinite deletion.** Write Δ = Δ⁺ − Σ c_n δ_n with 0 ≤ c_n ≤ 1, \|n\| ≥ a (forced by M_B ≥ 0). If Σ c_n < ∞ then Δ = 0 | PROVED |
| Prop B | **Local balance.** Δ⁺*K = C*K ≤ Π*K for every K ≥ 0 with supp \hat K ⊂ (−a,a). So Δ⁺ is translation-bounded, and its mass in every window is paid by integer mass deleted nearby | PROVED |
| Prop C | The N-level class 𝒞′ (dN_B ≥ 0 instead of μ_B ≥ 0) is convex. 𝒞 ⊂ 𝒞′ is not convex | PROVED |
| Rem T | f_t = ζ + tg (Thm F) is a segment Π + tG in the space {self-dual, = Π on (−a,a)} with off-line zeros. It sits outside 𝒞′ exactly because G has negative atoms off ℕ | PROVED given Thm F (PROVED-CITED) |
| (d) | Does the FE force supp ν into a lattice? **No such theorem**: Prop P turns the FE into self-duality of M, a linear condition with an infinite-dimensional signed solution space (Thm F family). Lattice support (Prop I, Hamburger) is identification (Thm O) | ARGUED (negative), signed part PROVED-CITED via Thm F |
| Q1 | ∃ ζ_B ∈ 𝒞 with an off-line zero (O164.101 fails)? | **OPEN** |
| Q0 | 𝒞 = {ζ}? (positive Beurling–Hamburger rigidity) | **OPEN** |
| Eq | O164.101 ⇒ RH; RH ⇒ O164.101 OPEN; if Q0 holds they are equivalent and the proof is identification | PROVED / OPEN |

## 1. Hypotheses, normalization

𝒞: ζ_B(s) = exp(∫_0^∞ e^{−su}dμ_B(u)), μ_B ≥ 0, σ_c(μ_B) < ∞, ξ_B := π^{−s/2}Γ(s/2)ζ_B continues meromorphically
with ξ_B(s) = ξ_B(1−s), its only poles are simple poles at 0 and 1 with ζ's residues, it has finite order, and μ_B = μ_ζ on
(0,L]. (μ_ζ = Σ_{p,k} k^{−1}δ_{k log p}. The masses log p belong to −ζ′/ζ, Λ = u·μ. The constraint ν ≥ −μ_ζ is the same.)
Q := ζ_B/ζ = exp(∫_L^∞ e^{−su}dν), ν = μ_B − μ_ζ ≥ −μ_ζ.

**(a) PROVED.** μ_B ≥ 0 makes ζ_B = Laplace transform of dN_B = exp^*(μ_B) ≥ 0. By Landau, σ_c(μ_B) is a real singularity
of log ζ_B. The only real singularities of log ζ_B in σ > 0 are the pole at 1 and real zeros. On (σ_c, ∞), log ζ_B is real,
so there is no real zero there, and ζ_B ≠ 0 on Re s > σ_c (exp). If σ_c < 1, ζ_B would be holomorphic at 1: contradiction.
If σ_c > 1, the Laplace transform of μ_B ≥ 0 would have its real singularity at a point where ζ_B is holomorphic and nonzero
(σ_c > 1 is not a zero by monotonicity of log ζ_B(σ) ↑, as in Thm L): contradiction. So σ_c = 1. By the FE and Γ, the zeros
in Re s < 0 are exactly −2,−4,… . Nothing beyond the classical strip.

## 2. Prop P (Poisson form). PROVED

For Re s > 1, π^{−s/2}Γ(s/2)x^{−s} = ∫_0^∞ e^{−πx²y}y^{s/2}dy/y. So ξ_B(s) = ∫_0^∞ θ_B(y)y^{s/2}dy/y with
θ_B(y) = ∫_{[1,∞)}e^{−πx²y}dN_B(x). Hecke's argument (finite order + Γ decay on σ = 1+ε and, through the FE, on σ = −ε;
Phragmén–Lindelöf inside) moves the Mellin inversion contour through the two poles. It shows that "FE + poles exactly
1/(s−1) − 1/s (ζ's)" ⟺ ϑ_B(1/y) = y^{1/2}ϑ_B(y), with ϑ_B := 1 + 2θ_B = ∫e^{−πx²y}dM_B(x). Both steps can be reversed.
By analyticity this holds for Re y > 0. Write the right side as ∫\hat M_B, using the transform of e^{−πx²y}. This gives
⟨M_B,φ⟩ = ⟨\hat M_B,φ⟩ for φ = e^{−πyx²}, and, after differentiating in y at y = 1 (M_B is tempered because N_B(x) = O(x^{1+ε})),
for φ = x^{2k}e^{−πx²}. These span a dense subspace of even Schwartz space (Hermite). Both sides are even, so
\hat M_B = M_B. The window condition μ_B = μ_ζ on (0,L] ⟺ dN_B = dN_ζ on [1,a] ⟺ M_B = Π on (−a,a)
(exp^* is causal in u). ∎

So the FE is a **Poisson summation formula** for a positive measure. This is the only discreteness-type input in 𝒞.
R163_101 §5 forbids proofs that use only the analytic data. Self-duality is not analytic data of that kind, but by itself
it does not force atoms (§5).

## 3. Consequences of positivity. PROVED

**Lem G.** \hat Δ = Δ, and Δ vanishes on (−a,a), so \hat Δ vanishes there too. Hence ⟨Δ, K(·−y)⟩ = ⟨\hat Δ, \hat K e_y⟩ = 0
whenever supp \hat K ⊂ (−a,a). ∎

Fix b < a/2 and let F_b(x) = (sin πbx/πx)², a Fejér kernel with \hat F_b supported in [−b,b] ⊂ (−a,a). Then
K := F_b + F_{b√2} is > 0 everywhere and integrable.

**Prop S.** If Δ ≥ 0, then Δ*K ≡ 0 with K > 0, so Δ = 0. The same holds for Δ ≤ 0. At the μ-level, exp^* is monotone on
positive measures: 0 ≤ μ ≤ μ′ ⇒ exp^*μ ≤ exp^*μ′. So ν ≥ 0 ⇒ Δ ≥ 0 ⇒ Δ = 0, and ν ≤ 0 (μ_ζ ≥ μ_B ≥ 0) ⇒ Δ ≤ 0 ⇒ Δ = 0.
In 𝒞, ν must therefore have **both** a nonzero positive and a nonzero negative part. This is stronger than Cor L.1, which
only excluded ν ≥ 0. ∎

**Prop F.** M_B ≥ 0 and Π's atoms force Δ⁻ = Σ_{|n|≥a}c_nδ_n with c_n ∈ [0,1]. Δ*K = 0 means Δ⁺*K = C*K. Integrating gives
‖Δ⁺‖·∫K = ‖C‖·∫K. If ‖C‖ = Σc_n < ∞, then Δ⁺ is finite, so Δ is a finite measure and \hat Δ is a bounded continuous function.
Then Δ = \hat Δ has no atoms, so C = 0, Δ ≥ 0, and Δ = 0 by Prop S. ∎ (Infinitely many deletions are needed. This sharpens
Thm H on the measure side.)

**Prop B** is Δ⁺*K = C*K ≤ Π*K ≤ ‖K‖_{ℓ¹(ℤ+y)}, uniformly in y. ∎

**Prop C.** {M ≥ 0, \hat M = M, M = Π on (−a,a), tempered} is a convex cone section. Taking log^* (to recover μ_B ≥ 0)
is not convex. ∎

## 4. Falsifier checks

| model | in 𝒞? | consistent with Props S/F/B? |
|---|---|---|
| Thm A (R164_102) | no: double pole at 1, FE fails | yes. ν ≥ 0, off-line zero. Prop S does not apply because the FE (self-duality) fails. This confirms that Prop S uses the FE, not positivity alone |
| f_t = ζ+tg (Thm F) | no: G has negative atoms at m/√M ∉ ℕ, so M ≱ 0 | yes. Self-dual, equals Π on the window, has off-line zeros. It shows that the signed linear problem has off-line solutions. Exactly the positivity of Δ off ℕ separates it (Rem T) |
| ζ_θ / deletion Λ1_{n≥5} (Prop D) | no: changes the window | Prop S kills pure deletion inside 𝒞. In D's case the FE fails |
| DMV systems | no FE | outside. Off-line zeros come from μ ≥ 0 alone, which is consistent with R163_101 §5 |
| Λχ₂, Epstein, DH | no positivity, or no Euler exp | outside |
| ζ itself | yes | Δ = 0 |
| ζ·S₁^K, S₁=(s−½)²/(s(s−1)) (R162_2901 Thm B) | no: pole of order K+1 at 1 (and at 0) | yes, excluded **for the right reason**. Higher poles add log-y terms to ϑ_B(1/y) − y^{1/2}ϑ_B(y), so \hat M ≠ M (the correction is a non-zero polar distribution). Props S/F/B use \hat Δ = Δ, which is exactly the simple-pole-with-ζ's-residue hypothesis. Positivity holds for it and its strip zeros are on the line, so nothing here is excluded by positivity |

**One-line-RH check.** Nothing here proves RH. Props S/F/B are statements about Δ, and ζ itself has Δ = 0. Positivity enters
non-linearly only through M_B ≥ 0 ⇒ Δ⁻ is supported on ℤ with c_n ≤ 1 (and through monotonicity of exp^* in Prop S). Neither
condition refers to zeros.

## 5. What remains (precise)

**Q1 ⟺ (PQ):** does there exist an even tempered real Δ ≠ 0 with (i) \hat Δ = Δ, (ii) Δ|_{(−a,a)} = 0,
(iii) Δ ≥ −Π, (iv) log^*(Π+Δ) ≥ 0 (μ_B ≥ 0), (v) the Mellin transform of Π+Δ has a zero off Re s = ½?
Props S/F/B: Δ must change sign, have infinite integer deletion and be locally balanced. Rem T suggests a natural route to
a counterexample: find a Thm-F-type self-dual G, Hecke-built, whose negative part lies on ℕ ∩ (a,∞) with t·|G(n)| ≤ 1, and
whose log^* stays ≥ 0. Then along Π + tG the real zeros of ξ collide and leave the line at some t, as for f_t (ARGUED).
**If such a G exists, O164.101 fails and L1 dies.** If positive self-dual measures with a gap are rigid (Q0: M = Π, a
positive-measure Hamburger theorem of Lev–Olevskii type without uniform discreteness; not available, OPEN), then
𝒞 = {ζ} and O164.101 ⟺ RH by identification, which is wall W3′/Thm O and contains no sign.

**The extra property of ζ that would be needed:** a sign mechanism valid for every member of the convex-in-N,
non-convex-in-μ class (PQ). Every such property that is not "M = Π" is a constraint on Δ. The only constraints derived are
linear (Lem G) or support/sign constraints (S/F/B), and none reaches zeros. A property strong enough would have to exclude
the Rem T route, that is, show that a positive self-dual G with deletions only on ℕ cannot produce collisions. No candidate
is known that is not "Δ = 0", which is identification.

**Equivalence.** ζ ∈ 𝒞, so O164.101 ⇒ RH. RH ⇒ O164.101 needs RH for all members, which is OPEN. It is equivalent under Q0,
and strictly stronger if 𝒞 ⊋ {ζ} contains an off-line member (then O164.101 is false and RH is unaffected).

**Corpus answer (R162_2901 §5).** Does POSITIVITY replace finiteness (Thm H) or integrality (Hamburger) when
infinitely many zeros move? **Partially, PROVED:** Prop F is the positive analogue of Thm H on the measure side. A deletion of
finite total N-mass is impossible in 𝒞, and Prop S rules out one-signed moves of any size. **Beyond that, no:** an
infinite, two-signed, locally balanced Δ is not excluded by any argument here, so (PQ) stays OPEN. Status of O164.101: it is
a frontier statement (S11) **iff** 𝒞 ⊋ {ζ}. If Q0 holds it is a restatement of RH. RH does not imply it by any known
argument (OPEN).

## 6. Grid cells (R162_2300)

- **4F** (Euler × global transforms in T): new PROVED rows Prop P, Prop S (no pure deletion), Prop F, Prop B. Residue
  O164.101 sharpened to (PQ). Walls: E1 (Lem G = Prop W, linear), W3′ (Q0 = identification).
- **5G** (integrality × Hamburger/dictionary): the FE is a Poisson formula (Prop P). Lattice support is Prop I = identification.
  The positive gap-rigidity Q0 is the cell's live OPEN item. If true it is identification (W3′).
- **1G** (Hamburger as dictionary): confirmed as dictionary. Rem T places f_t in the signed linear solution space.
  "Mechanism" residue = a sign theorem for (PQ); none found.

## 7. Ledger

| id | item | status |
|---|---|---|
| R164_402.a | classical regions for 𝒞 | PROVED |
| R164_402.P | Poisson form of 𝒞 | PROVED (Hecke; finite order assumed) |
| R164_402.G | Lem G (= Prop W, measure form) | PROVED |
| R164_402.S | no pure addition / no pure deletion in 𝒞 | PROVED |
| R164_402.F | finite deletion impossible | PROVED |
| R164_402.B | local balance | PROVED |
| R164_402.C | convexity of 𝒞′ | PROVED |
| R164_402.T | f_t as signed segment; collision route to an off-line member of 𝒞 | Thm F PROVED-CITED; route ARGUED |
| R164_402.d | no lattice-forcing from FE | ARGUED (negative) |
| O164.101 = (PQ) | existence of an off-line member | OPEN |
| O164.402.0 = Q0 | positive self-dual gap rigidity ⇒ 𝒞 = {ζ} | OPEN (identification if true) |
