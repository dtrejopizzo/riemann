# R153.005 — Lead closing decision, phase 153 (row D: does the certified endpoint carry sign?)

*Lead of record: Fable 5.1. Date 2026-09-19. Inputs: R153_000 (blueprint), R153_001 (builder r1), R153_002 (hostile audit),
R153_003 (builder r2, certificate), R153_004 (hostile confirmation: PROOF ACCEPTED). Scripts: `scripts/`, `scripts/audit/`,
`scripts/certificate/`.*

## 1. Verdicts of record

| item | statement | label |
|---|---|---|
| **Theorem A** (conjugation identity) | `A_T^{(a)} = E_{-a}A_T E_a + E_a A_T E_{-a}`, `E_a` = multiplication by `e^{at}`; hence `⟨A_T^{(a)}F,F⟩ = 2[⟨A_T u,u⟩ − ⟨A_T w,w⟩]`, `u = cosh(at)F`, `w = sinh(at)F`, and `F ∈ P_T^{(a)} ⟺ u,w ∈ P_T`. The Weil form of the falsifier `Ξ_a` is the **cross term** of two `ξ` forms, never a sum of squares. Verified against all four Prop. 12.6 substitutions; `a→0` gives `2A_T` on the ξ²-primitive space (codim 2 in `P_T`), discontinuously in value. Corpus check: no prior hit. | `PROVED` (new) |
| **Lemma C1** (ladder) | `Σ_± Re ψ(¼ ± a/2 + iτ/2) − 2 log π = Σ_{j≥0,±} 2τ²/(a_j^±((a_j^±)²+τ²)) − m_0^{(a)}`, `a_j^± = 2j+½±a`, `m_0^{(a)} = 2log π − ψ(¼+a/2) − ψ(¼−a/2)` (`= 2m_0` at `a=0`); each term is a nonnegative D.76-type energy, so truncation gives a lower bound and the explicit remainder `A/J + B/(2J²)` (plus an exponential tail `< 10^{-2400}`, to be added formally) gives a rigorous upper bound. | `PROVED` |
| **Lemma C3** (exact primitivity) | `F = P(D)G`, `P(D) = (D²−(½+a)²)(D²−(½−a)²)`, `G = (T²−t²)⁴·(polynomial)`, lies in `P_T^{(a)}` exactly: `∫e^{βt}P(D)G = P(−β)∫e^{βt}G = 0` for `β ∈ {±(½±a)}`, vanishing order 4 at `±T` matching the order-4 operator. The written proof in R153_003 ("innermost factor") is wrong and is replaced by this one of record. | `PROVED` (proof repaired) |
| **Certificate** | At `T = log 2`, for the explicit degree-18 `F` of R153_003 (exact decimal coefficients), mpmath.iv at 400 bits: `a = 0.45`: `⟨A_T^{(a)}F,F⟩/‖F‖² ∈ [−0.0373367294804088, −0.0373367294804087]`; `a = 0.30`: `∈ [−0.0142279881516186, −0.0142279881516185]`. Independent from-scratch evaluation (auditor): `−0.03766967`, `−0.01455470`, below the certified upper bounds by exactly the tail budget. Stable in `J` and precision `≥ 300` bits; fails safe at 200 bits (precision floor to be documented). | `PROVED` |
| **D.12-α** (phase 137 acceptance test) | Answered by `(S,T) = ({∞,2,3}, log 2)`: `W_S ≥ 0` for `ξ` on `P_T` (Paper 42 `thm:certifiedendpoints`, interval-certified, cited not reproved) and `W_S^{(a)} < 0` for `Ξ_a` on `P_T^{(a)}`, `a ∈ {0.30, 0.45}`. Note `P_T^{(a)} ⊄ P_T`: the two forms live on different four- vs two-moment spaces, as D.12-α itself allows (same support class). | `PROVED`, conditional only on Paper 42's certificate |
| Q1 at `T = ½ log 3` | no negativity for any `a ≤ 0.499` (`λ_min ≈ +0.79`) | `DIAGNOSTIC-NUMERIC` |
| `a*(log 2)` | first `a` with `A_{log 2}^{(a)} ≱ 0`: `≈ 0.080` (converged, two discretisations); `λ_min(A^{(a)}) → +1.24·10⁻³` as `a → 0⁺` (a jump, not 0). Round-1 claim `a* → 0` | `DIAGNOSTIC-NUMERIC`; r1 claim `WITHDRAWN` |
| `λ_min(A_{log 2}|P_T)` | `∈ (0, 1.05·10⁻⁷]` (L² Rayleigh normalisation; K = 80…320 still drifting down; Richardson ≈ 1.02·10⁻⁷). Round-1 value `2.08·10⁻⁴` was a basis artefact. The certificate margin `8.63·10⁻⁸` is a Feshbach *capacity* margin, not an L² bound: no sharpness statement is made. | `DIAGNOSTIC-NUMERIC` |
| Mechanism of the `Ξ_a` loss | not near-nullity of `v₁` (r1 (A2)), not archimedean convexity (r1 (A3), false: ψ concave); it is the low-frequency archimedean loss: `m_0^{(a)}` grows (`10.74 → 44.92 → 204.8` at `a = 0, 0.45, 0.49`) | `PROVED` (mechanism); (A2),(A3) `WITHDRAWN` |
| **Q2 — prime-blindness** | `λ_min(G_{Γ,T} − m_0 | P_T) = −0.153` at `log 2` while `2ΣΛ(n)n^{-1/2} = 2.249`: the crude bound `A^{abs}` is far negative; archimedean domination in the crude sense is refuted (consistent with phase 46 GAP-142.A: absolute `O(1)` threshold). Sign flips `Λ(3) → −Λ(3)` (`−0.257`), drop `n=3` (`−0.083`), `Λ(2) → −Λ(2)` (`−0.918`) destroy positivity. | `DIAGNOSTIC-NUMERIC`; kill criterion NOT triggered |
| `b`-scan | replacing the shift `log 3` by `b`: `λ_min(b)` has an isolated positive needle at `b = log 3` of height `≈ 1.1·10⁻⁷` and width `~10⁻⁷` (mesh-free), negative elsewhere in the scanned range. Reading: at `T = log 2` positivity of the two-prime Weil form is *exactly critical* and the critical point sits at the arithmetic contact. Not a theorem. | `DIAGNOSTIC-NUMERIC` |
| **T*(a)** detection threshold | `T*(a) := inf{T : A_T^{(a)} ≱ 0 on P_T^{(a)}}`: strictly decreasing, `T*(0.001)=0.8085 … T*(0.08)=0.6935 ≈ log 2 … T*(0.45)=0.6242`, jump at `a = ½` (moments degenerate); `T*(a) → ∞` only logarithmically, fit `≈ 0.624 + 0.0268·log(1/a)` over three decades; `T*(a) > ½ log 3` for all `a ≤ ½` (explains the null result at `½ log 3` and CC's prime-free window `½ log 2`). Property of the falsifier family, not of `ζ`. Corpus check: no prior notion. | `DIAGNOSTIC-NUMERIC` (new object) |
| Q3(i) monotonicity of `T ↦ λ_min(A_T|P_T)` | zero extension preserves primitivity and new contacts act trivially on it | `RESTATEMENT` (main.tex) |
| Q3(ii) `v₁` identification | not established (r1 minimiser unresolved) | `WITHDRAWN` |
| Q3(iii) D.76 `T`-uniform | multiplier is `2τ²/(b(b²+τ²))`; the certificate's capacity step uses `T`-dependent Robin roots; `½ log 5` wall = two uncomputed cross terms (unchanged) | `DOWNGRADE` → `OPEN` (as before) |

FATAL rule: clean (no zero-free region, no moment bound, no cancellation from known theorems). No sign claimed for `ζ` beyond `T ≤ log 2`.

## 2. What phase 153 established that was not known before

1. **The programme has its first sign-carrying theorem.** Until today every positive statement of row D transferred verbatim to the falsifiers (the phase-136 meta-theorem; `Ξ_a` passes every cone, every growth bound, every transport). The pair `({∞,2,3}, log 2)` is the first finite object on which `ζ` and `Ξ_a` are separated by a sign: `ξ ≥ 0` (Paper 42) and `Ξ_a < 0` (this phase), interval-certified on both sides. D.12-α, the acceptance test phase 137 wrote for exactly this, is met.
2. **Why it is possible at all (Theorem A).** The `Ξ_a` form is `2(⟨A_T u,u⟩ − ⟨A_T w,w⟩)` — a difference of two `ξ` forms on the `cosh/sinh` components. A sum-of-squares statement can never be falsified this way; a cross term can. This is the operator-level form of the summand-vs-numerator axis of phase 151: off-line zeros enter with a numerator sign, and Theorem A displays that sign as `−⟨A_T w,w⟩`.
3. **The detection law is logarithmic.** `T*(a)` grows like `0.027·log(1/a)`: a zero at distance `a` from the line is detected by the Weil form on a window of length `≈ 0.62 + 0.027 log(1/a)`. Windows must grow only logarithmically to see exponentially close zeros — but this is for the two-Gamma product family `Ξ_a`, whose off-line zeros come in full vertical lines. Nothing is claimed for a single off-line zero of `ζ`.
4. **The endpoint `log 2` is critical, not comfortable.** `λ_min(A_{log 2}|P_T) ≲ 10⁻⁷` in L² normalisation, and the `b`-needle says the two-prime form is positive essentially only at `b = log 3`. Whatever mechanism eventually extends positivity past `log 2` must be arithmetic (use the contacts), not analytic domination.

## 3. What it does not do

It does not advance the sign for `ζ` at any `T > log 2`; it does not prove anything about `ζ`'s zeros; `T*(a)` is not certified (no lower bound); the `Ξ_Q` (Epstein) and Beurling falsifiers are untested (Lemma C1 is specific to the two shifted Gamma factors). Compared with Connes–Consani: the corpus now has, beyond CC's prime-free archimedean window, (i) a certified window with primes 2,3 coupled and (ii) a certified separation of `ζ` from a function with off-line zeros inside that window. CC have neither; neither of these is a step toward the global sign by itself.

## 4. Repairs of record (from R153_004; applied by this decision, to be written into R153_003 at the next pass)

1. Add the exponential tail term `2N²Σ e^{−bL}/b` (`< 10⁻²⁴⁰⁰`) to the remainder of Lemma C1. 2. Replace Lemma C3's proof by the `P(−β)` argument above. 3. Document the precision floor (`≥ 300` bits; 200 bits fails safe). 4. State D.12-α as conditional on Paper 42 and note `P_T^{(a)} ⊄ P_T`. 5. Record `λ_min(A^{(a)}) → +1.24·10⁻³` as `a→0⁺`; mark R153_001 §§1.3, 2, 3 superseded by R153_003/004.

## 5. Open items carried

| id | statement | label |
|---|---|---|
| (P153.1) | certified lower bound on `T*(a)`; certified negativity for some `a < 0.30` at `log 2` (target `a ≈ 0.10`) | `OPEN` |
| (P153.2) | the same separation for the Euler-product-free falsifier `Ξ_Q` (Epstein) and for a Beurling system: is there a finite `(S,T)` separating `ζ` from them? Requires a ladder for their archimedean factors | `OPEN` |
| (P153.3) | extend certified `ξ`-positivity to `½ log 5` (the two cross terms of W4 §3) — now with the knowledge that the mechanism must use the contacts | `OPEN` (unchanged) |
| (P153.4) | a theorem behind the `b`-needle: is `b = log 3` the unique `b ∈ (log 2, 2T)` with `G_{Γ,T} − m_0 − w_2(S_{±log 2}) − w_3(S_{±b}) ≥ 0` on `P_{log 2}`? | `OPEN` |
| (P153.5) | does Theorem A have an analogue for a single off-line zero pair (a rank-two perturbation of `A_T`), giving a detection law for `ζ` itself? Corpus check required before building (phase 119 DH gate, phase 138 D.17) | `OPEN` |

## 6. Decision

Phase 153 **closed**. Row D acquires its first sign-carrying theorem (D.12-α `PROVED`, conditional on Paper 42) and one new exact identity (Theorem A). Row D's label is unchanged: no sign for `ζ` beyond `log 2`. Paper 46 must receive Theorem A, Lemmas C1/C3, the certificate, D.12-α's resolution and the open items (P153.1)–(P153.5) in §28.3; the six-clause reopening criterion of §28.4 is not invoked (the theorem is about the endpoint, not about all `T`).
