# BUILD_R1_001 — Phase 202, round 1: the exterior table as an inequality, its exact decomposition by ratio classes, and the first sub-lemma

Phase 202. Nothing was computed beyond
paper algebra; the numbers cited come from EXTERIOR_DATUM_001, ROUGH_COMPLEMENT_001, AUDIT_L_SHARP_16 and the README.

**Index check (grep ROUTES-TRIED-INDEX/README.md, "dilat", "angle", "Euler–Maclaurin", "Poisson", "Möbius lattice",
"sign-sensitive"):** the pieces I use are already registered as tools (thm:ext-half, prop:ext-grouped, prop:ext-latred,
Theorem C′, R-F1, G1, C-pos). Nothing proposed below repeats a closed attempt: (i) the "cutoff-layer" form (§2.2) is a
new exact rewriting of the same objects (not a route, it is a coordinate); (ii) Lemma X1.0 (§4) is a norm bound and I
mark it as such — the reason it does NOT count as progress against death criterion (b); (iii) Lemma X1 is formulated on
the signed class coefficients (c_q, d_q), which is exactly what DD/EE/AUDIT_15 declared necessary and which no one had
formulated as a lemma with hypotheses. The Poisson reading of the whole class (§3.3) is the inverse of thm:ext-half and
I record it as a restatement, not as progress (risk: PROOF_L_SHARP_S_001 §(i) pattern, "self-dual ℤ").

---

## 1. Exact statement of the table (task 1)

### 1.1 Objects (all from P47 sec:ext)
- T > 0, λ = e^T, N = λ² (at Mori's extremal, N = μ = 15, T = ½log15).
- f admissible at T (def:ext): even, supp ⊂ [−λ,λ], C², f(0) = 𝓕f(0) = f(λ) = 0. g = Ef ∈ core.
- r = r_f := 𝓕f|_{(λ,∞)} (out-of-band data; f of Paley–Wiener type λ ⇒ r is the out-of-band tail, nonzero).
- Zr(w) = w^{½}Σ_{n≥1} r(nw), Z_log r(w) = w^{½}Σ_{n≥2}(log n) r(nw), w > λ; Ψ̌(y) = (Zr)(e^y)·1_{y>T}.
- Archimedean form plus pole: 𝒜[Ψ̌] := (1/2π)∫ m(τ)|Ψ̌^(τ)|² dτ, with m from eq:symbol; written on the half line it
  carries the killing term ∫_{y>T}|Ψ̌|²κ(y)dy, κ(y) = ∫_{y−T}^∞ ½K (rem:ext-killing (i)). Pole: 2A(Ψ̌)B(Ψ̌).
- Gauge: 𝒢_T, 𝒢̄_T (closure of 𝓕φ|_{(λ,∞)}), dist(r, 𝒢̄_T); ℓ(g) = 2 dist²(r, 𝒢̄_T) (prop:ext-gauge, PROVED).
- Π_μ (PI_MU_001): projection onto the quotient by 𝒢̄_T, which is how (★★) must be read ("mod radical").
- Decomposition (thm:ext-lattice, eq:ext-lattice-r, PROVED): r = Σ_{1≤m<N} (μ(m)/m) σ_g(·/m) + 𝓕φ₀, σ_g = 𝓕𝗉,
  𝗉(u) = u^{−½}g(log u) on [1/λ, λ]. "Prolate tail + Δr_out" reading (EXTERIOR_DATUM_001 §1): r = ρ_pro + Δr_out
  (+ Δr_in, negligible), ρ_pro ⊃ line m = 1 (Langer tail, Theorem C), Δr_out ⊃ lines m ≥ 2 (Möbius-cell content at
  escape scale).

### 1.2 The inequality (★★), written once
For every N ≥ 5 and every r = 𝓕f|_{(λ,∞)}, f admissible:

  𝒲_ext[r] := 𝒜[Ψ̌] + 2A(Ψ̌)B(Ψ̌) − 2⟨Ψ̌, (Z_log r)(e^·)⟩_{L²(T,∞)}  ≥  2κ N^{−A₀} dist²(r, 𝒢̄_T).      (★★)

with 𝒲_ext[r] = 𝒲[Ψ̌] = W_T(Ef) (thm:ext-half). Equivalent to eq:ext-L (prop:ext-consol, PROVED). Implication
(★★) ⇒ λ^W_T > 0 ∀T with explicit margin: PROVED (P47 sec:ext). In lattice coordinates (prop:ext-latred, PROVED):
𝒲_ext[r] = vᵀGv, v = (μ(m))_m ⊕ 1.

### 1.3 What is PROVED and what is the single OPEN item
| piece | content | label |
|---|---|---|
| half-line identity (thm:ext-half) | W_T(Ef) = 𝒲[Ψ̌]; the comb appears only via Λ∗1 = log | PROVED (given Guo L4.2–4.5) |
| B.0 / B / B′ | structural bounds of the exterior form (P47 §22) | PROVED |
| Theorem C (+ CC_001) | prolate tail m = 1: phase (1,2)/X₁₁ = +0.033, controlled | PROVED asymptotically; NUMERICAL below N ≈ 130 (restr. 26) |
| lem:ext-envelope | uniform prolate envelope | PROVED |
| Möbius lattice (thm:ext-lattice, prop:ext-grouped, prop:ext-latred) | r as a lattice; coefficients c_q, d_q; 𝒲 = vᵀGv | PROVED |
| FF.1 | exterior datum = Σ_{N′≥μ} c_{N′}N′^{−½}g(x − log N′) + gauge + polar(≡0) | PROVED |
| T.1 | 𝒲 on the line via tail zeros (rem:ext-killing (iii)) | PROVED |
| Π.0–Π.3 | projection onto the quotient, invariance of 𝒲 | PROVED; Π.5 PROVED per N, uniform NO-GO |
| **(★★) itself** | uniform-in-N quadratic coercivity | **OPEN** |

**Exact OPEN inequality** (reduced form, AUDIT_16 §6): with (i) the prolate tail controlled (Theorem C) and (ii)
Δr_out the Möbius-cell content, what is missing is

  2⟨Ψ̌, Z_log r⟩ ≤ (1 − ε_N)·(𝒜[Ψ̌] + 2AB),  ε_N·(𝒜+2AB) ≥ 2κN^{−A₀}dist²(r,𝒢̄_T),               (OPEN-★★)

where the coupling between (i) and (ii) is the resonance (1,n) (−0.479, −0.295, +0.062, −0.148 X₁₁ for n = 2,3,4,5
in g*; README/ROUGH) and the measured margin is 0.61 against the 0.95 needed for any norm-based version.

---

## 2. Exact decomposition, not by norms (task 2)

### 2.1 Pairs of dilations (PROVED, from the proof of thm:ext-half)
With r̃(x) = e^{x/2}r(e^x), Ψ̌(y) = Σ_{n≥1} n^{−½} r̃(y + log n). Changing to w = e^y:

  I(m,n) := ∫_T^∞ r̃(y+log m) r̃(y+log n) dy = (mn)^{½} K(m,n),   K(m,n) := ∫_λ^∞ r(mw) r(nw) dw.

Hence, exactly,

  ‖Ψ̌‖² = Σ_{m,n≥1} K(m,n),    ⟨Ψ̌, Z_log r⟩ = Σ_{m≥1, n≥2} (log n)·K(m,n).                                  (2.1)

The coefficients are the VALUES Λ∗1(n) = Σ_{q|n}Λ(q) = log n; the factor n^{−½} disappears when passing to dw (it
is absorbed into the measure). Symmetrizing: 2⟨Ψ̌, Z_log r⟩ = Σ_{m,n} log(mn) K(m,n).

### 2.2 Grouped by ratio class and "cutoff-layer" form (PROVED, new as a coordinate)
For q = b/a in lowest terms, (m,n) = (ak, bk), and v = mw:

  K(ak,bk) = (ak)^{−1} J_q(akλ),  J_q(Y) := ∫_Y^∞ r(v) r(qv) dv.

Summing by parts in k (J_q(Y) = ∫_Y^∞ j_q, j_q(v) := r(v)r(qv)):

  ‖Ψ̌‖² = Σ_{(a,b)=1} a^{−1} ∫_{aλ}^∞ j_{b/a}(v)·H(v/(aλ)) dv,         H(Y) = Σ_{k≤Y} 1/k,
  2⟨Ψ̌, Z_log r⟩ = Σ_{(a,b)=1} a^{−1} ∫_{aλ}^∞ j_{b/a}(v)·L_{ab}(v/(aλ)) dv,  L_{ab}(Y) = Σ_{k≤Y} log(abk²)/k.     (2.2)

(All sums absolutely convergent because r = O(ξ^{−2}).) The archimedean part groups the same way because m(D) is a
Fourier multiplier in y = log w, i.e. it commutes with dilations; the only break is the cutoff at y > T, and with the
change y ↦ y + log m this becomes

  𝒜-pair(m,n) = (mn)^{−½}·𝔅_q(T + log m),  𝔅_q(Y) := 𝒜(r̃·1_{>Y}, r̃(·+log q)·1_{>Y}),                       (2.3)

exact (the killing term enters 𝔅_q through the cutoff at Y). Thus

  𝒲_ext[r] = 2AB + Σ_{(a,b)=1} (ab)^{−½} Σ_{k≥1} k^{−1}·[ 𝔅_{b/a}(T+log ak) − log(abk²)·I_{b/a}(T+log ak) ],      (2.4)

with I_q(Y) = ∫_Y^∞ r̃ r̃(·+log q). **(2.4) is the exact form of (★★) by classes; no norms at all.** The arithmetic
enters through: (α) the weight log(abk²) = Λ∗1 at the positions mk, nk; (β) the cutoff positions log(ak) (the
multiplicative lattice); (γ) via r, the lattice coefficients μ(m)/m (eq:ext-lattice-r).

**Diagonal class q = 1 (ARGUED, semiclassical):** r̃ in y oscillates at frequency ≍ λe^y (r is the Fourier transform
of f with support [−λ,λ]), so m(τ) ≈ log(|τ|/2π) ≈ T + y on the support; in the layer y > T + log k the symbol is
≥ 2T + log k, which dominates the weight 2 log k for k < λ² = N. For k ≥ N the cutoff T + log k is already in the
tail where I_1 is O((kλ)^{−3}). Conclusion: the diagonal is locally positive with margin ≍ 2T − log k (ARGUED; it is
the old "archimedean beats the comb on the diagonal", no new sign). **All the sign lives in q ≠ 1.**

### 2.3 On the Möbius lattice: where the resonances are
Inserting eq:ext-lattice-r, each K(m,n) opens into pairs of lines (m′,n′); the coinciding ones (line m′ in summand 1,
line nm′ in summand n) are the same σ_g(w/m′) with coefficient μ(m′)μ(nm′)/(nm′²) = μ(m′)²μ(n)/(nm′²) if (m′,n) = 1
(prop:ext-grouped, PROVED). The measured (1,n) resonances are the sum of those terms plus the cross part
pro04 × Δr_out:

  R_n := 2·Σ_{m′<N/n,(m′,n)=1} μ(m′)²μ(n)/(nm′²)·[𝔅-pair − log-pair](σ_g(·/m′)) + (non-coinciding) .

Measured at g*: R₂ = −0.479X₁₁, R₃ = −0.295, R₄ = +0.062, R₅ = −0.148 (sign μ(n) in 6/6 for n ≤ 7,
EXTERIOR_DATUM_001). The term that decides the sign at the extremal is **R₂: the cross pro04@dilation 1 ×
Δr_out@dilation 2 (−0.481), the reverse +0.0001** — directional: the prolate tail (line 1) read at cutoff λ and the
line 2 of Δr_out read at λ·2.

### 2.4 Lemma X1 (the sign-sensitive bound; OPEN, formulated with exact hypotheses)
Write (prop:ext-latred) 𝒲_ext = Σ_{q,q′}[c_q c_{q′} 𝔅_∞(s_q,s_{q′}) − (c_q d_{q′} + d_q c_{q′})⟨s_q, s_{q′}⟩] +
(φ₀ terms), s_q = e^{y/2}σ_g(qe^y)1_{y>T}, c_{b/a} = (μ(a)/a)M̃_a(N/a), d_{b/a} = log b·c_{b/a} + (μ(a)/a)D_a(N/a),
D_a(Y) = Σ_{k<Y,(k,a)=1}μ(k)log k/k.

**Lemma X1 (OPEN).** There exist ε > 0, A₀ such that for every N ≥ 5 and every g in the core (with φ₀ the min-leak
gauge, Π applied):

 (X1.a) [full class, a = 1] |Σ_{b,q′}(c_b d_{q′} + d_b c_{q′})⟨s_b, s_{q′}⟩| ≤ ε₁·Σ c_q c_{q′}𝔅_∞(s_q,s_{q′});
 (X1.b) [classes a ≥ 2, sign] Σ_{a≥2}Σ_{b,q′}(c_{b/a}d_{q′} + d_{b/a}c_{q′})⟨s_{b/a}, s_{q′}⟩ ≤ ε₂·Σ c c 𝔅_∞ + 2AB,
        where the sum on the left-hand side is taken WITH the signs μ(a), and it is required that the contribution
        of the a with μ(a) = −1 (the ones producing R_n < 0 with n prime) be offset by that of a with μ(a) = +1 and
        by the diagonal, not bounded in modulus;
 (X1.c) ε₁ + ε₂ ≤ 1 − ε and the remainder ε(𝒜 + 2AB) ≥ 2κN^{−A₀}dist²(r,𝒢̄_T) (Π.0–Π.3 + Π_μ).

Then (★★) holds (PROVED: sum of (X1.a–c) in (2.4)/prop:ext-latred).

Arithmetic hypotheses that X1 uses (and that must be used; restriction 5): (H-a) a_n ≡ 1 (Z with no weights),
(H-b) μ multiplicative with squarefree support (coinciding coefficient μ(m)²μ(n)), (H-c) Λ∗1 = log (weights d_q),
(H-d) Poisson in the exterior (thm:ext-half). What X1 can NOT use: |c_q| ≲ 1/a, c_b → 0 (rem:ext-latno (c): blind
to a_P).

Remark on scale: at g*, |c₁| = |M̃(15)| = 0.006 while D₁(15) ≈ −1 (PNT, CITED in the limit). In the full class the
dominant term is therefore D₁·Σ_b⟨Σ_{q′}c_{q′}s_{q′}, s_b⟩ — see §3.3.

---

## 3. Where exact Λ enters non-uniformly (task 3)

### 3.1 What changes in the identity (not in the numbers)
I repeat §2's derivation for each comb X with Dirichlet series L_X = Σ a_X(n)n^{−s} and −L′_X/L_X = ΣΛ_X(n)n^{−s}:

- **ζ:** Φ_f = e^{x/2}Σ_n f(ne^x) with a_n ≡ 1; Poisson over self-dual ℤ ⇒ tail = Zr with the SAME Z; comb weight
  in the tail: Λ∗1 = log; inverse of E with μ (multiplicative, squarefree); lattice coincidences with coefficient
  μ(m)²μ(n).
- **Epstein Q (h > 1):** the summation-map sum carries r_Q(n) (a_n ≠ 1); Poisson is that of the lattice ℤ² with
  dual form Q* ⇒ the tail is Z_{Q*}r with weights r_{Q*}(n), not Z; the comb in the tail weighs Λ_Q ∗ r_Q, which is
  NOT log·r_Q (there is no identity Λ_Q∗1 = log because 1 is not the coefficient); the inverse of E is μ_Q = the
  Dirichlet inverse of r_Q, NOT multiplicative (no Euler product), with support on non-squarefree numbers ⇒ the
  coinciding coefficient μ_Q(m)μ_Q(nm) does not factor as μ_Q(m)²·(something in n). **Identity (2.4) changes shape:
  the weights log(abk²) become (Λ_Q∗r_Q)(·) and weights r_{Q*} appear in ‖Ψ̌‖².** Also Λ_Q(2) = Λ_Q(3) = Λ_Q(7) = 0
  and Λ_Q < 0 at 36… (README): this is numerical; what is structural is the non-factorization.
- **DH:** a_n = b_n with signs, no Euler product; it has an FE (Poisson-type) but the inverse μ_DH is not
  multiplicative ⇒ (H-b) fails.
- **Beurling:** multiplicative, Λ_B∗1 = log_B (R-F1: shared), μ_B multiplicative ⇒ (H-b), (H-c) hold; positions
  log n_k are not translates of a self-dual lattice ⇒ there is NO Poisson: thm:ext-half does not exist (the tail is
  not Zr). (H-d) fails.
- **a_P (Euler factor at P deleted):** (H-a) fails (a_n = 1_{P∤n}), but Poisson is recovered as a difference of two
  sums (Σ_n − Σ_{Pn}); μ1_{P∤·} remains multiplicative; rem:ext-latno (c) says size bounds do not separate it. What
  does separate it: the tail is Zr − P^{−½}D_P Zr, i.e. a dilation by P with sign − appears, which is not present
  in ζ.

### 3.2 Precise answer to the question
Which property of Λ(p^k) = log p (all powers, no gaps, no signs) does X1 use? All four together, but the one that
is **non-uniform and not shared** is the conjunction (H-b) ∧ (H-d) within the same identity: **the Möbius lattice
is self-aligned under integer dilation** (line m′ in summand 1 ≡ line nm′ in summand n, because the positions are
log m with m ∈ ℕ and ℕ is a semigroup) **and** that same ℕ is what Poisson returns in the tail (ℤ's self-duality).
Beurling has the alignment but not Poisson; Epstein has Poisson but the tail lives on the dual lattice with weights
r_{Q*} and the inverse is not multiplicative (the alignment exists in positions but the coinciding coefficients do
not factor with sign μ(n)); DH has an FE but no factorization. Λ∗1 = log alone (R-F1) is not enough: it is
Beurling-shared. "No gaps" = a_n ≡ 1 (H-a), which is what makes the tail's Z the same Z as the summation map
(self-duality); "no signs" = μ(n) ∈ {0,±1} on squarefree numbers with μ(m)μ(nm) = μ(m)²μ(n) — this is what fixes
the sign of R_n as μ(n) (6/6 measured). Label: PROVED as a statement about the FORM of the identity (§3.1 is a
direct derivation); whether X1 is false for the falsifiers: CONDITIONAL on X1 being proved and on the computations
of §5.

### 3.3 The full class collapses via Poisson (PROVED as an identity; it is a restatement)
For a = 1, c_b = M̃₁(N) =: c (constant in b) and d_b = c·log b + D₁(N). Then the full-class part of the tail is

  Σ_b c_b s_b(y) = c·e^{y/2}Σ_{b≥1}σ_g(be^y) = c·(Zσ_g)(e^y),
  Σ_b d_b s_b(y) = c·(Z_logσ_g)(e^y) + D₁(N)·(Zσ_g)(e^y).

By Poisson (𝗉 extended evenly, supp [1/λ,λ] ∪ symmetric): 2Σ_{b≥1}σ_g(bw) = w^{−1}Σ_{k∈ℤ}𝗉(k/w) − σ_g(0) = (Riemann
error of ∫𝗉 with step 1/w < 1/λ). So (Zσ_g)(e^y) is an Euler–Maclaurin error of 𝗉, governed by the jumps of 𝗉's
jets at ±1/λ, ±λ (g vanishes to 2nd order at ±T ⇒ 𝗉 ∈ C¹ with a jump in 𝗉″; error O(e^{−2y}) ARGUED with a constant
to be fixed). **Consequence:** the term D₁(N) ≈ −1 of the full class — the only O(1) signed coefficient that the
arithmetic produces at a = 1 — multiplies a Poisson-small object. Same for each a: Σ_{(b,a)=1}σ_g(bw/a) =
Σ_{d|a}μ(d)Σ_{b′}σ_g(b′dw/a) is a combination of Riemann errors (ARGUED). This is the "Poisson" reading of
Theorem C′.2's near-total Möbius cancellation. **Honesty:** it is the inverse Poisson already used in
thm:ext-half; it is not progress toward the sign, but it does locate where (H-d) and (H-a) act in X1: in the full
class, the signed coupling with D₁ reduces to 𝗉's Euler–Maclaurin defect — PROOF_L_SHARP_S_001 §(i) pattern (do not
retry Euler–Maclaurin by harmonic: restriction 14; this is BY CLASS, not by harmonic, written reason).

---

## 4. First candidate sub-lemma (task 4)

### 4.1 Lemma X1.0 (PROVED): angle between r and its dilate via the mass in the first layer
Let D_n r(w) := n^{½}r(nw) (unitary on L²(0,∞)). For r with support in [λ,∞), let θ_n := ‖r‖²_{[λ,nλ)}/‖r‖² ∈ [0,1].
Then

  |⟨r, D_n r⟩_{L²(0,∞)}| ≤ √(1 − θ_n)·‖r‖²,   i.e. |cos∠(r, D_n r)| ≤ √(1−θ_n).

*Proof.* ⟨r, D_n r⟩ = n^{½}∫_λ^∞ r(w)r(nw)dw = ∫_λ^∞ r(w)·(D_n r)(w)dw, and ‖D_n r·1_{[λ,∞)}‖² = ∫_λ^∞ n|r(nw)|²dw =
‖r‖²_{[nλ,∞)} = (1−θ_n)‖r‖². Cauchy–Schwarz. ∎ (Mellin: ⟨r,D_n r⟩ = (2π)^{−1}∫|Mr(½+it)|²n^{−it}dt, so |cos| < 1
always — trivial.)

If |r(ξ)| ≤ Cξ^{−α} in the outer layer and r is concentrated near λ (spectral gap ⇒ mass at the edge),
θ_n ≥ 1 − O(n^{1−2α}) (ARGUED, depends on the tail shape). For |cos₂| < 0.6, θ₂ ≥ 0.64 would suffice.

### 4.2 Why X1.0 is NOT the sub-lemma we need (exact obstacle)
1. **It is a norm bound** (Cauchy–Schwarz over layers): it falls under death criterion (b) and under R-K1/Schur.
   Blind to the sign μ(n) and valid for Epstein/DH/Beurling unchanged (it does not use (H-a)–(H-d)).
2. **The measured 0.644 is not cos∠(r, D₂r).** It is the coupling prolate tail (pro04, line m = 1) × Δr_out@2
   relative to the diagonals (EXTERIOR_DATUM_001 §2). In (2.1)–(2.2), K(1,2) = ∫_λ^∞ r(w)r(2w)dw includes pro×pro
   (+0.065), pro×Δr (−0.481), Δr×pro (+0.0001), Δr×Δr. The object carrying the sign is the cross BLOCK
   ⟨ρ_pro, D₂Δr_out⟩, not the global angle.
3. **For the cross block, X1.0 gives the right structure but no margin:**
   |⟨ρ_pro, D₂Δr⟩| ≤ ‖ρ_pro‖·‖Δr‖_{[2λ,∞)}. Since Δr_out lives in the bulk of σ_g (lines m ≥ 2 read σ_g at
   ω/m < λ: the remark following eq:ext-lattice-r), its mass in [2λ,∞) is NOT small — line m = 2 of Δr is
   σ_g(ω/2)/2, with ω/2 ≥ λ on [2λ,∞), i.e. precisely σ_g's tail, the same one as line 1! This is exactly the exact
   resonance: D₂(line 2) = line 1 up to the factor μ(2)/2·√2. No layer bound separates it.
4. **What IS proved (Lemma X1.1, PROVED, identity):** the resonant part of the cross block is exactly, with
   normalization line_m(ω) = (μ(m)/m)σ_g(ω/m) ⇒ (D₂ line₂)(w) = √2·(−1/2)σ_g(w) = −2^{−½}σ_g(w) = −2^{−½}line₁(w).
   Thus

     ⟨line₁, D₂ line₂⟩_{(λ,∞)} = −2^{−½}‖σ_g‖²_{(λ,∞)},

   and in general ⟨line_{m′}, D_n line_{nm′}⟩ = μ(m′)μ(nm′)·n^{−½}·m′^{−1}‖σ_g‖²_{(λ/m′,∞)} (PROVED, change of
   variable). The sign is μ(n) (for (m′,n)=1) and the size is NOT small: |coef| = n^{−½}. This confirms (and
   proves) Theorem C′.1 in its coinciding part: **the exact resonance cannot be bounded; it must be offset.** The
   obstacle to the first sign-carrying PROVED sub-lemma is therefore sharp: one must show that the sum
   Σ_{n} log n · μ(n) n^{−½}(·) of exact resonances, combined with the diagonals
   Σ_{m′} μ(m′)²/m′ ‖σ_g‖²_{(λ/m′,∞)} and with 𝔅, is ≤ (1−ε)·(archimedean diagonal). With identical weights σ_g on
   every line, this is an inequality over a DIRICHLET SERIES WITH μ AND log COEFFICIENTS:
   Σ_{n≤N}μ(n)log n/n^{s}-type (see §4.3).

### 4.3 Candidate for the next sub-lemma (OPEN, formulated)
With all exact coincidences (X1.1), the resonant part of 2⟨Ψ̌, Z_log r⟩ is

  𝓡 = Σ_{m′ sq-free <N} Σ_{n≥2,(n,m′)=1, nm′<N} 2 log n · μ(n)/(n m′²)·𝒥(m′),  𝒥(m′) = ∫_λ^∞ σ_g(w/m′)² dw = m′‖σ_g‖²_{(λ/m′,∞)},

(prop:ext-grouped, with the weight log n from (2.1)), and the resonant diagonal 𝓓 = Σ_{m′} μ(m′)²m′^{−2}𝒥(m′). The
ratio 𝓡/𝓓 is a weighted average (weights 𝒥(m′)/m′²) of S(m′) := 2Σ_{n<N/m′,(n,m′)=1} μ(n)log n/n. By PNT,
Σ_{n≤Y}μ(n)log n/n → −1 (CITED), so S(m′) → −2∏_{p|m′}(…) < 0 — **the sign of 𝓡 is fixed and negative, of size
O(1)·𝓓**, consistent with −0.479−0.295−0.148… Hence −2⟨Ψ̌,Z_log r⟩ ⊃ −𝓡 > 0: **the comb's resonant part HELPS
(★★)** (the term enters with sign −2⟨·⟩).

Careful with the sign! In (★★) the comb enters as −2⟨Ψ̌,Z_log r⟩. The measured resonances R_n are negative in the
Gram G (README: "resonances with sign μ(n)"; R₂ = −0.479 X₁₁). One must fix in which form they are measured
(entries of 𝒲 or of ⟨·,·⟩?). If R_n are entries of 𝒲 (vᵀGv with v_m = μ(m)), the sign μ(m)μ(nm) = μ(n) appears
TWICE (v and the entry) and the contribution to 𝒲 is v_1 v_n G_{1n}… I ask the calibrator (§5, P1) to report the
contribution to 𝒲 with sign, separating (𝔅, comb). Lemma X1.2 (OPEN, candidate for PROVED in round 2): "the
coinciding resonant part of 𝒲_ext equals Σ_{m′}μ(m′)²m′^{−2}[𝔅-diag(m′) + Σ_{n}μ(n)n^{−½}(𝔅_n − 2 log n)𝒥(m′)…]
and its sign is determined by Σ μ(n)log n/n (PNT) and by Σ μ(n)n^{−½}𝔅_n(…)". If the 𝔅 part (archimedean, with
sign μ(n)) is the one producing R_n < 0 and the log part partially offsets it, X1 reduces to an inequality between
TWO Dirichlet series with μ coefficients: Σμ(n)n^{−½}·m̂(log n)-type vs Σμ(n)log n/n. That would be the first
exact-valued, non-uniform statement (it uses (H-b): μ multiplicative; Epstein has μ_Q and a different series), and
not a functional of the minimizer (the weights 𝒥(m′) are ≥ 0 and the inequality would be over m′). **OPEN; this is
round 2's objective.**

---

## 5. Requests to the calibrator (task 5)
All at Mori's extremal μ = 15 (g*, min-leak gauge, EXTERIOR_DATUM_001 quadrature), and repeated with the same r*
replacing the comb with Epstein (T = 8/5, Q with h = 2 as used in CPOS) and DH (T = 9/5), i.e.: same r*, change
(i) the log n weights for the falsifier's weights in (2.1) and (ii) the μ coefficients for the falsifier's
Dirichlet inverse in the lattice.
- **P1.** For n = 2..7: the contribution to 𝒲_ext (not to the Gram, with sign) of class q = n, split into
  (a) the 𝔅 part (archimedean + killing) and (b) the comb part −log(n)·(…), and within each (exact coinciding
  X1.1) vs (non-coinciding).
- **P2.** θ_n = ‖r*‖²_{[λ,nλ)}/‖r*‖² for n = 2,3,5, and also θ_n for ρ_pro and for Δr_out separately (to close or
  kill X1.0).
- **P3.** cos∠(r*, D_n r*) globally and for the cross block ⟨ρ_pro, D_nΔr_out⟩/(‖ρ_pro‖‖Δr_out‖) — to pin down what
  the 0.644 is.
- **P4.** 𝒥(m′) = ∫_λ^∞σ_g(w/m′)²dw for m′ squarefree < 15, and the ratio 𝓡/𝓓 of §4.3 with S(m′) truncated at
  N/m′: compare with the measured sum of R_n.
- **P5.** The Poisson residue of §3.3: ‖Zσ_g‖_{L²(T,∞)}/‖σ_g‖_{L²(λ,∞)} and ‖Z_logσ_g‖/‖σ_g‖ at g*.
- **P6.** The same P1, P4 for Epstein/DH with their μ_X: does the sign of class (1,n) still follow μ_X(n)? Does
  the ratio 𝓡/𝓓 change sign or size? This decides whether X1.2 separates the falsifiers (death criterion (a)).
- **P7.** (control) in a_P (P = 2, valid window) class q = 2: what does the extra term −P^{−½}D_P from §3.1
  contribute?

---

## 6. Round balance
- PROVED: (2.1)–(2.4) exact form by classes and cutoff layers; Lemma X1.0 (norms, no sign value); Lemma X1.1
  (exact coinciding resonances, coefficient μ(m′)μ(nm′)n^{−½}m′^{−1}‖σ_g‖², sign μ(n), size not small); §3.1 FORM
  differences of the identity for Epstein/DH/Beurling/a_P; §3.3 Poisson collapse of the full class (restatement).
- ARGUED: diagonal q = 1 locally positive (margin 2T − log k); E–M error O(e^{−2y}); θ_n via decay.
- OPEN: Lemma X1 (a–c); Lemma X1.2 (reduction of the resonant part to two Dirichlet series with μ coefficients);
  (★★).
- NO-GO (for this phase): X1.0 as a sign sub-lemma (it is a norm statement).
- Death criterion after R1: (a) still no intermediate PROVED with exact Λ that is not an identity for Epstein/DH —
  X1.1 is a valid identity with μ_X in place of μ if μ_X were multiplicative; for Epstein it is not, so X1.1 in its
  "sign μ(n)" form is ζ-specific in its FORM (PROVED), but it is still not an inequality. (b) no: X1.2 is not a
  norm statement. (c) no: 𝒥(m′) is a functional of σ_g, not of the minimizer — but one must verify that σ_g (from
  g in the core) does not become a function of the minimizer once Π is imposed.

No claim of a sign for row D is made. L′♯ OPEN. (★★) OPEN.
</content>
