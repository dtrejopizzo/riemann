# SKELETON_002 — Reduced skeleton after AUDIT_205_SKELETON_001 (phase 205, round 2)

REF-D / NUMERICAL. no external equivalence is used.
Applies the coordinator's five instructions and the facts fixed in REVIEW_STATE.md.

## Summary (≤250 words)

1. **I adopt (R1)**, which is a REWRITE of P47 lem:polarelim extended to all of L²(I_T):
   M(F) = 𝔢(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²), with 𝔢 = (1/2π)∫|F̂|²/(¼+τ²).
   Corrected typos: β_{½log15} = 1.903696 and t₀′ = 6.12587 (zero of m^♯ = m + 1/(¼+τ²), NUMERICAL).
   The E_G/β_T variant is withdrawn because it is not canonical (R2).
2. **𝔅_T and (6.1) remain as REWRITE/REF-D.** Z_T = 𝔞^♯ − 𝓕_T on L²_ev. Φ_E = −𝓕_T = −R_Λ. The "slack" (β−2)ℓ² is
   an artifact and vanishes on P_T.
3. **L205.★ is withdrawn.** The skeleton has no sign node.
4. **P1.c, decided in its original form: NO-GO for large T** (ARGUED; the inputs are PROVED/CITED and the
   constants are pending). The high-frequency complement contains ≈10% of χ_ev, so −2ℓ² ~ −0.005e^{2T} dominates
   𝔪 + 𝔢 = O(e^T) and Φ_E = o(e^{2T}) (dlVP). The polar direction must be moved into the low block. What remains is
   **P1.c′** (complement of E_N^ev ⊕ ℝχ, within P_T): OPEN, with a death criterion. Every size-based proof requires
   E(x) ≪ x^{½+o(1)} → REF-D.
   **Pointwise question σ_T vs m for τ > t₀: FALSE.** It fails for each fixed τ along a sequence of T, by the main
   term (PROVED with CITED dlVP). Without the main term, |σ^E_T| ≤ m^♯ cannot be proved without zero information
   and is false near the ordinates (ARGUED).
5. **No sign step exists that satisfies (Def O1.2) with two channels in the same step and an identified abstract
   falsifier.**
   Final skeleton: P2a, (R1) as a rewrite, c_k (PROVED); P1.c′ is the only OPEN piece; P5 is its calibrator.

---

## 0. Index and corpus

In addition to SKELETON_001 §0, I ran grep on `ROUTES-TRIED-INDEX/README.md` and on P47 for "polarelim," "Poisson,"
"main term," "R_Λ," "𝓕_T," "prop:sharp" (review blacklist). (R1) and Φ_E appear there: B_001 Lemma 3.1
(index l.451), V_001 Thm V.2.1, E_001 E.4, MORI15_EXTREMAL, N_BUILD_001. **I claim no novelty for (R1).**
The block partition E_N ⊕ E_N^⊥ (P1.c) does not appear as such. Its sign content (block inertia) does appear at
l.536 (SPEC_004 N3). So I use it only as a reduction tool, and the decision in §3 is a new NO-GO for the index.

---

## 1. Corrections (instruction 1)

**(R1) (REWRITE, PROVED; P47 lem:polarelim outside P_T).** For every F ∈ L²(I_T):
  M(F) := −∫∫F(x)F(y)e^{|x−y|/2}dxdy = 𝔢(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²),
with ch = cosh(x/2)1_{I_T}, sh = sinh(x/2)1_{I_T} and 𝔢(F) = (1/2π)∫|F̂|²/(¼+τ²) = ‖G′‖² + ¼‖G‖²
(G = e^{−|·|/2}∗F/1, the potential on the line).
*Proof.* e^{|s|/2} = 2cosh(s/2) − e^{−|s|/2}; the kernel e^{−|s|/2} has transform 1/(¼+τ²) on ℝ, and cosh((x−y)/2)
has rank 2. ∎
In the even sector: M = 𝔢 − 2ℓ², with ℓ = ⟨·,χ_ev⟩ and χ_ev = ch. The coefficient 2 is the same "2" from the pole
in W^ev = 𝔄_ev + 2ℓ².

**I withdraw** the form E_G − β_Tℓ² from SKELETON_001 §5.2 as an object. It is correct, but
E_G = 𝔢 + (½sinh T − 1)ℓ² (R2) splits the rank one non-canonically. The claim "E_G has symbol 1/(¼+τ²)" was
**false**: that symbol belongs to 𝔢.

**Typos.** β_{½log15} = 1 + ½sinh(½log15) = 1.903696 (not 1.90474), and the slack equals −0.09630. The zero of
m^♯ = m + 1/(¼+τ²) is t₀′ = 6.12587 (NUMERICAL), not "2–6." That number is very close to t₀ = 6.28984: the help
from 𝔢 at low frequency barely moves the count. With t₀′ instead of t₀, the number of negative directions of
𝔪 + 𝔢 is N′(T) = ⌈2Tt₀′/π⌉ − 1 ≈ 3.900T. This is a PROVED lower bound by the same proof as A∞, because
m^♯ = C₀ + φ(τ²) + 1/(¼+τ²) is still concave in τ² (sum of concave functions). In practice, in the even sector the
comb has to cover ≈ 1.95T directions instead of ≈ 2.0T.

**c_k (PROVED).** ⟨χ_ev, e_k⟩ = 2ω_k cosh(T/2)/(√T(¼+ω_k²)) for odd k. ‖χ_ev‖² = T + sinh T.

**P2a (PROVED, technical lemma).** Closed formulas for G_kl(u) (SKELETON_001 §3). Before entering P47, pending an
independent quadrature (REVIEW_STATE).

---

## 2. Relabeling and withdrawal (instructions 2 and 3)

- **𝔅_T := 𝔪 + E_G + Φ_E = Z_T + (½sinh T − 1)ℓ²: REWRITE/REF-D.** With (R1), Z_T = 𝔪 + 𝔢 + Φ_E = 𝔞^♯ − 𝓕_T on L²_ev
  (extended prop:sharp(ii)), with Φ_E = −𝓕_T = −R_Λ. Identity (6.1) is PROVED given H1PLUS (1.4), without the
  normalization condition I had placed on it: the two "2"s are the same pole. The slack (β_T − 2)ℓ² comes only
  from E_G's geometry, has no arithmetic content, and vanishes on ker ℓ ∩ L²_ev = P_T^ev.
- **L205.★: WITHDRAWN.** On its domain, E_N^ev ∩ ker ℓ, it is the compression of prop:sharp(ii), 𝓕_T ≤ 𝔞^♯ on
  E_N^ev ∩ P_T. It is REF-D by K2 from the start and is moreover only a necessity. The K1–K6 criteria remain filed
  as filters for future proposals. The correct formulation of K2 is "Z_T ≥ 0 on E_N^ev ∩ P_T," with no slack.
- **The skeleton has no sign node.**
- NO-GO for m − σ_T ≥ 0 at τ = 0: correct, but **it is an immediate corollary of cor:H1minus**. I leave it labeled
  as such.

---

## 3. P1.c: statement, decision, repair (instruction 4)

### 3.1 Original statement
Let 𝒰_N := cl span{e_k : k > N, k odd} ⊂ L²_ev(I_T). **P1.c**: 𝔄_ev|_{𝒰_N} ≻ 0 (closed and coercive). If it holds,
Haynsworth (CITED) gives n₋(𝔄_ev) = n₋(𝔄_N − X𝔄_⊥⁻¹Xᵀ).

### 3.2 Decision: P1.c is FALSE for large T (NO-GO; ARGUED, inputs PROVED/CITED, constants pending)

**Proposition 3.1.** There exists T₂ such that for T ≥ T₂ there is F ∈ 𝒰_{N(T)} with 𝔄_ev(F) < 0.

*Witness.* F := P_{𝒰}χ_ev = Σ_{k>N odd} c_k e_k, the high-frequency part of the polar direction.

*Computation.* Exact decomposition, with (R1) and partial summation (PROVED):
  𝔄_ev(F) = 𝔪(F) + 𝔢(F) − 2ℓ(F)² + Φ_E(F).
(a) **Polar term.** ℓ(F) = ⟨F,χ⟩ = ‖F‖² = Σ_{k>N}c_k². With c_k² = 4ω_k²cosh²(T/2)/(T(¼+ω_k²)²) and
  ω_k ≥ ω_{N+2} > t₀, one obtains Σ_{k>N odd}c_k² = (e^T/T)(1 + O(e^{−T}))·Σ_{k>N odd}ω_k^{−2}(1 + O(ω_k^{−2})). Since
  Σ_{k>N odd}(2T/πk)² = (4T²/π²)(1/(2N) + O(N^{−2})) and N = 2Tt₀/π + O(1), this gives
  **ℓ(F) = e^T/(πt₀)·(1 + O(1/T)) ≈ 0.0506·e^T** (PROVED-elementary). Hence −2ℓ(F)² ≈ −0.00512·e^{2T}.
  Check: ‖F‖²/‖χ‖² → 2/(πt₀) ≈ 0.101, consistent with Mori's 91.2%.
(b) **Archimedean + 𝔢.** 𝔪(F) + 𝔢(F) = (1/2π)∫m^♯|F̂|². F has coefficients c_k ~ e^{T/2}/(√T ω_k). By I3 of A∞ and
  an upper bound of m by a logarithm (m(τ) ≤ log(2+|τ|), thm:S), Σ_k m^♯-weight·c_k² = O(e^T). One must pass from
  the sine basis to ∫m^♯|F̂|² with F of bounded variation; the computation is standard
  (|F̂(τ)| ≲ ‖F‖_∞/|τ| + …), but I write it as ARGUED. **Result: O(T·e^T)**, in any case o(e^{2T}).
(c) **Chebyshev remainder.** Integrating by parts, Φ_E(F) = ∫_{(1,X]}E(t) d_t[2t^{−½}Re c_F(log t)]. F has bounded
  variation, with ‖F‖_∞ ≲ e^{T/2} and TV(F) ≲ e^{T/2}·(1+log N). Then c_F is Lipschitz with
  |c_F′| ≲ ‖F‖_∞·TV(F) ≲ T e^T and |c_F| ≤ ‖F‖² ≲ e^T. With dlVP (CITED: E(t) ≪ t·exp(−c√log t)):
  |Φ_E(F)| ≲ ∫_1^{X}|E(t)|·t^{−3/2}(e^T + T e^T)dt ≲ T e^T·∫_1^X t^{−½}e^{−c√log t}dt ≲ T e^{2T−c√(2T)}.
  It is o(e^{2T}).
(d) Hence 𝔄_ev(F) = −(2/(π²t₀²))e^{2T}(1 + o(1)) < 0 for T ≥ T₂. ∎

**Reading.** That P1.c fails has nothing to do with the primes. It is the pole: χ_ev is not band-limited in the
Dirichlet basis, and its high-frequency tail carries a fixed fraction ≈ 2/(πt₀) of its mass, so that the rank-one
term −2ℓ² of size e^{2T} contaminates the high block. Channel usage: only F (Γ_ℝ, t₀) and the residue, plus the
CITED dlVP bound so that E does not compensate. **Steps to upgrade to PROVED:** write out (b) with constants and
fix an explicit T₂. P5 calibrates it at Mori: the prediction is that at T = ½log15 it still does not fail, because
−2ℓ² ≈ −2(0.09·1.5)² is small compared to 𝔪 in the high block. This is NUMERICAL and pending.

### 3.3 Repair: P1.c′ (OPEN), with the pole in the low block
Let 𝓛_N := E_N^ev + ℝχ_ev (dimension ⌈N/2⌉ + 1) and 𝒰′_N := 𝓛_N^⊥ ∩ L²_ev. Since χ_ev ∈ 𝓛_N, 𝒰′_N ⊂ ker ℓ = P_T^ev,
and on 𝒰′_N, 𝔄_ev = 𝔞_T = 𝔞^♯ − 𝓕_T holds (prop:sharp(ii)).

**P1.c′ (OPEN).** For every T ≥ T₀: 𝔞^♯(F) − 𝓕_T(F) ≥ η_T‖F‖² with η_T > 0, for F ∈ 𝒰′_{N(T)}.
If it holds, Haynsworth reduces even positivity (n₋ = 1) to the inertia of a matrix of size ⌈N/2⌉ + 1 with a Schur
term. q_ev < −½ is also still needed (prop:WT).

**What general theorem would be needed.**
(i) Upper bound of A∞ on P_T: 𝔞^♯ ≥ c‖F‖²_{H^{½}-log} on 𝒰′_N. This is plausible: m^♯ > 0 for |τ| > t₀′, and 𝒰′_N
   is orthogonal to the low-frequency sines. The loss comes from the sines not being band-limited, and that is a
   Landau–Widom-type leakage control (CITED as a technique). **A zero-free tool, OPEN, with content.**
(ii) Control of 𝓕_T at high frequencies: |𝓕_T(F)| ≤ (1−ε)𝔞^♯(F) on 𝒰′_N.

**Death criterion of P1.c′.**
- (M1) If (ii) can only be obtained with a size bound on E(x) → REF-D. For (ii) to hold with 𝔞^♯ = O(log T)‖F‖²,
  |𝓕_T| ≲ log T·‖F‖² is needed on high-frequency P_T. By (c), that magnitude requires ∫t^{−½}|E(t)|t^{−1}dt ≪ T^{O(1)},
  i.e. E(t) ≪ t^{½}(log t)^{O(1)} on average. That is zero-side data (H1PLUS §4.2, index I6). **Every size-based
  proof of P1.c′ dies here.**
- (M2) If the Galerkin version of 𝔞_T on 𝒰′_{N} gives n₋ ≥ 1 in a certified window → P1.c′ is false.
- (M3) If (ii) reduces to prop:sharp(ii) restricted to a subspace → REF-D (the same argument that withdrew L205.★).

**Honest status.** (i) is a genuine tool, zero-free and open. (ii) is REF-D unless a non-size mechanism appears, and
I have none. So **P1.c′ as a whole is OPEN with (ii) probably-REF-D**. The only thing constructible today without
zeros is (i).

### 3.4 Pointwise question: σ_T(τ) versus m(τ) for τ > t₀ (decided)
σ_T(τ) = Σ_{n≤X}2Λ(n)n^{−½}cos(τ log n), X = e^{2T}.

**Proposition 3.2 (PROVED with CITED dlVP).** For every fixed τ there is a sequence T_j → ∞ with σ_{T_j}(τ) > m(τ).
In particular, the pointwise inequality σ_T ≤ m for τ > t₀ is false.
*Proof.* Partial summation with ψ = t + E:
  σ_T(τ) = 2Re[(X^{½−iτ} − 1)/(½ − iτ)] + 2Re∫_1^X t^{−½−iτ}dE(t).
By dlVP and integration by parts, the second term is O((1+|τ|)·e^{T−c√(2T)}). The first is
2e^T·cos(2Tτ − θ_τ)/|½−iτ| + O(1), with θ_τ = arg(½+iτ)… and cos(·) ≥ ½ on a set of T of positive density. Then
σ_T(τ) ≥ e^T/|½−iτ|·(1 − o(1)) → ∞ > m(τ) = O(log τ). ∎

**After removing the main term.** With (R1), the main term is absorbed into 𝔢 − 2ℓ², and what is left to compare
with m^♯ is σ^E_T(τ) := 2Re∫_1^X t^{−½−iτ}dE(t). For |σ^E_T(τ)| ≤ m^♯(τ):
- without zeros, the best bound is dlVP's, O(τ e^{T−c√T}), which is unbounded. **It cannot be proved without zeros
  (PROVED as a method insufficiency).**
- with the explicit formula (only as a reading, not as an input), σ^E_T(τ) = −2Re Σ_ρ X^{ρ−½−iτ}/(ρ−½−iτ) + O(1).
  For τ near an ordinate γ the resonant term is ≈ min(2T, 1/|τ−γ|), and that exceeds m^♯(τ) ~ log τ for large T.
  **Pointwise false (ARGUED).**
**Verdict: NO-GO as a pointwise criterion for τ > t₀, in both versions.** Control of the high block, if it exists,
is not pointwise in the symbol: it has to use the compression. That is (ii) of P1.c′, with its M1 criterion.

---

## 4. Sign nodes (instruction 5)

**No sign step exists that uses E (Dirichlet series over ℕ) and F (conductor 1) in the same step, that does not
chain according to Def O1.2, and that has an identified abstract falsifier on the intermediate object.** I propose
none.

---

## 5. Final reduced skeleton

| piece | content | label |
|---|---|---|
| A∞ / Cor C (and A∞ with t₀′ for m^♯) | n₋(𝔪) ≥ N(T); n₋(𝔪 + 𝔢) ≥ N′(T) ≈ 3.90T | PROVED (t₀, t₀′ NUMERICAL-certifiable) |
| P1.a, P1.b | necessity on E_N^ev | PROVED |
| P1.c (high block = 𝒰_N) | fails for large T (witness P_𝒰χ) | NO-GO (ARGUED; constants of (b) pending) |
| P1.c′ (high block ⊥ χ) | (i) upper bound of A∞ on P_T, (ii) control of 𝓕_T | OPEN; (i) zero-free tool, (ii) probably-REF-D (M1) |
| P2a | closed G_kl(u) | PROVED (independent quadrature pending) |
| (R1) | M = 𝔢 − 2(ℓ_c² − ℓ_s²) on all of L² | REWRITE of lem:polarelim (PROVED) |
| c_k | coefficients of χ_ev; high fraction → 2/(πt₀) | PROVED |
| 𝔅_T, (6.1), L205.★ | — | REWRITE/REF-D; withdrawn |
| pointwise σ_T ≤ m (τ = 0 and τ > t₀) | — | NO-GO (τ = 0: cor:H1minus; τ > t₀: Prop 3.2 PROVED + ARGUED) |
| P5 | calibrator for P1.c and P1.c′ | pending |

Graph: A∞(t₀′) ──► (i) of P1.c′ ◄── P5. P2a + c_k ──► P5 matrices. (R1) ──► 𝒰′_N ⊂ P_T ──► (ii) [M1 → REF-D].
No sign node.

**Assignment for P5, the calibrator (T = ½log15, N = 5).**
(1) Inertia of 𝔄_ev on 𝒰_5 (Galerkin in sines k = 7, 9, …, 41, for example). Prediction: ≻ 0 at Mori, because P1.c
    only fails asymptotically. Also, the value of 𝔄_ev(P_𝒰χ)/‖P_𝒰χ‖² and its trend for T ∈ {2, 3, 4, 5}, to
    estimate T₂.
(2) Inertia of 𝔞_T on 𝒰′_5 (criterion M2).
(3) The 4×4 matrix 𝓛_5 (k = 1, 3, 5 and χ), its Schur complement and inertia (n₋ = 1 expected).

**Index (editor, same session).**
- SKELETON_002 (phase 205, round 2): (R1) recorded as a REWRITE of lem:polarelim; 𝔅_T, (6.1) and L205.★ as
  REWRITE/REF-D, withdrawn.
- **New NO-GO:** the Dirichlet-frequency Schur split with χ in the high block fails for large T (witness P_𝒰χ,
  −2ℓ² ≈ −0.005e^{2T}).
- **NO-GO:** pointwise σ_T ≤ m for τ > t₀ (main term; remainder not boundable without zeros).
- **OPEN:** P1.c′, with (i) a zero-free upper bound of A∞ on P_T and (ii) probably-REF-D by M1.
- The skeleton has no sign node.
