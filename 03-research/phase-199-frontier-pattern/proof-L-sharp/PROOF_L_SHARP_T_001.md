# PROOF_L_SHARP_T_001 — Strategy T: the Poisson mirror as an exact symmetry (Fourier sectors of the exterior form)

Phase 199 memo (pen and paper; no numerics run). Target: Lemma L′♯ = (★★) (AUDIT_L_SHARP_4 §8, constraints 1–15).
, no zero location is used.

**Outcome in one line.** L′♯ NOT proved. New and PROVED (modulo one CITED/CONDITIONAL radical lemma, §1): on the class 𝒮 of
even data f with f = 0 and f̂ = 0 on (−1,1), the Fourier involution 𝔉 splits the exterior form 𝔔 into two 𝔔-orthogonal sectors
𝒮_± (f̂ = ±f), and on each sector the self-dual closure is NOT a tautology: it gives
  **𝔔[Ψ] = ±( Σ_{j≥1} L_j(Ψ)² + 𝒫[Ψ] − A(Ψ)² ),**   L_j(Ψ) = ∫_0^∞Ψ(x)e^{−(2j+½)x}dx,  𝒫[Ψ] = Σ_q Λ(q)q^{−½}(Ψ∗Ψ)(log q),
i.e. the archimedean part becomes a manifest sum of squares (completely monotone Hankel kernel), the B²-pole term is absorbed
exactly by its j = 0 square, and the whole sign burden sits on the prime self-convolution 𝒫 versus the single square A².
No sign is claimed. (★★) OPEN; row D OPEN.

## 0. Corpus / index check and why this is not a retry
- Index read: README l.452 (A_001), l.461–464 (TEST_CG, Q_001, R_001, S_001), l.208 ("positividad por reflexión entre
  lugares: sólo la mitad de Hankel; falla con cualquier átomo", PROVED), 04_PHASES l.755 (G2C-R161_026-028 method of images /
  polar layer = exterior image, PARTIAL), l.764 (G4C-R161 Toeplitz–Hankel, opposite parity kills Tate term), l.299 (G8A-118/W3),
  phase 198 AA_001 (window parity split), AUDIT_L_SHARP_4 §6 (mirror theorem, constraint 15).
- Why new: (a) l.208 reflects *between places*; here the reflection is the Poisson/Fourier involution *inside* ℝ acting on the
  exterior data, and the Hankel kernel that appears is ν(x+x′) (completely monotone), not a Hankel part of the prime lattice
  (Q_001 Q.1 shows the prime part is not Hankel — consistent: here the prime part appears as a self-convolution, not as Hankel).
  (b) AUDIT_4 §6 proved the mirror for general compactly supported ρ, where it carries interface/residue/polar terms and is
  "not a reduction"; this memo restricts to the Fourier-invariant class where all those terms collapse and *uses* the mirror
  as an involution, which AUDIT_4 did not do. (c) G2C-R161 images were for the window polar layer, not for 𝔉-eigen-data.

## 1. Set-up: the exact intertwining (PROVED) and the radical lemma (CITED/CONDITIONAL)
For f even on ℝ with enough decay put Φ_f(x) := e^{x/2}Σ_{n≥1}f(ne^x), x ∈ ℝ (A_001 §1), R: x ↦ −x, f̂ = 𝔉f (𝔉² = id on even f).
**Lemma 1.1 (intertwining; PROVED, Poisson).** Φ_{f̂}(x) = Φ_f(−x) + ½f(0)e^{−x/2} − ½f̂(0)e^{x/2}; in the normalisation of AUDIT_4 (f = ρ_e, f(0) = 0, f̂(0) = c(0) = 2ρ₀):
  Φ_c(y) = Φ_ρ(−y) − ρ₀e^{y/2}.
*Proof.* Σ_{n∈ℤ}f(nu) = u^{−1}Σ_{n∈ℤ}f̂(n/u); multiply by u^{1/2}/2 with u = e^x: Φ_f(x) + ½f(0)e^{x/2} = Φ_{f̂}(−x) + ½f̂(0)e^{−x/2}. □
So E∘𝔉 = R∘E + (rank-two polar correction in f(0), f̂(0)). This is (P) of AUDIT_4 written as an operator identity; **𝔉 is a
genuine involution on f, and R on Φ; the polar correction is the only defect.**

**The duality map on the exterior data.** The data class of L′♯ is ρ on (1,∞) (out-of-band data rescaled), f = ρ_e. The map
ρ ↦ c|_{(1,∞)} is NOT an involution (c has an interior part on (0,1), and P²ρ = ρ − 𝔉(c1_{(0,1)})|_{(1,∞)}). It *is* an
involution exactly on
  𝒮 := {f even : f = 0 on (−1,1), f̂ = 0 on (−1,1)}   (then f(0) = f̂(0) = 0, ρ₀ = 0, no polar defect).
𝒮 ∩ L² is infinite-dimensional (the sum L²(−1,1) + 𝔉L²(−1,1) is closed of infinite codimension since ‖P_IQ_I‖ < 1; CITED
Landau–Pollak/Slepian). 𝒮 ∩ C_c = {0} (f̂ entire). **Existence of a rich Schwartz (or O(X^{−2})-decay) subclass: CONDITIONAL**
(not proved here; needed for absolute convergence below).

**Lemma 1.2 (radical; CITED for compact support = Guo Lemma 4.4 / A_001 Thm 1.1(b); CONDITIONAL for 𝒮).** If f(0) = f̂(0) = 0
and f has Schwartz decay then WΦ_f = 0 a.e. on ℝ (W = full Weil distribution, A_001 §1). The proof (Mellin H_Φ = ζ(s)M_f(s),
M_f vanishing at s = 0, 1, explicit formula for the translates) only uses that ζ·M_f is entire with M_f killing the poles; it uses
no information on zeros. The extension from Guo's compact class to Schwartz decay is ARGUED (same proof, cut-off), not checked
line by line.

Throughout, 𝔔[ρ] = 𝒲_{(0,∞)}[Ψ̌_ρ], Ψ̌_ρ := Φ_ρ|_{(0,∞)}, the complete one-sided Weil form (A_001 §3.2 after reflection; F Thm F.1;
convention of AUDIT_4 §6).

## 2. (i) The defect D and its antisymmetry
**Definition/Proposition 2.1 (PROVED for ρ ∈ C_c^∞(1,∞), by P.1 + AUDIT_4 §6).** With D(ρ) := 𝔔[ρ] − 𝔔_line[c]:
  **D(ρ) = 2Q(F,G) + 2AB − 2𝔅[ρ] + R(1)G_h(0) − c₀ρ₀² + 2ρ₀ρ₁.**
*Proof.* Insert Q(G,G) = −𝔔_line[c] + 2𝔅 − R(1)G_h(0) + c₀ρ₀² − 2ρ₀ρ₁ into 𝔔 = −Q(G,G) + 2Q(F,G) + 2AB. □
(Here 𝔔_line[c] is used because c = O(1/ξ) makes A_cB_c delicate, AUDIT_4 §2.)
- **Antisymmetry.** D(Pρ) = −D(ρ) is meaningful only where P is an involution, i.e. on 𝒮; there it is the trivial consequence
  of §3 (𝔔[ρ] = 𝔔[𝔉ρ]). Outside 𝒮 it is FALSE as a structural statement (P not involutive; the interior c1_{(0,1)} enters).
- **Constraint identity on 𝒮 (CONDITIONAL on the PW-tail extension of AUDIT_4 §6, since 𝒮 ∩ C_c = {0}).** On 𝒮, ρ₀ = 0 and
  𝔔[c] = 𝔔[ρ] (Thm 3.1), so D(ρ) = 2A_cB_c, i.e.
  **2Q(F,G) + 2AB − 2𝔅 + R(1)G_h(0) = 2A_cB_c**   (f ∈ 𝒮),
  and on 𝒮_± (c = ±ρ on (1,∞)) A_cB_c = AB, giving **Q(F,G) − 𝔅 + ½R(1)G_h(0) = 0**: the coupling Q(F,G) of P.1 equals the
  interface term minus the residue term. This is a new exact identity among P.1/mirror terms (consequence, not a sign).

## 3. (ii) The self-dual closure is not a tautology: the reflected form
**Theorem 3.1 (PROVED given Lemma 1.2 on 𝒮).** Let f ∈ 𝒮 (with the decay of Lemma 1.2), ε ∈ {±1} and f̂ = εf. Write
Ψ := Φ_f|_{(0,∞)}. Then Φ_f = Ψ + εRΨ (Lemma 1.1, no polar term), and
  **𝔔[Ψ] = 𝒲_{(0,∞)}[Ψ] = ε·𝒲_refl[Ψ],  𝒲_refl[Ψ] := ∫∫_{x,x′>0}Ψ(x)Ψ(x′)ν(x+x′) + 𝒫[Ψ] − A(Ψ)² − B(Ψ)²,**
with ν(t) = e^{−t/2}/(1−e^{−2t}), 𝒫[Ψ] = Σ_{q≥2}Λ(q)q^{−½}∫_0^{log q}Ψ(x)Ψ(log q − x)dx, A = ∫Ψe^{x/2}, B = ∫Ψe^{−x/2}.
*Proof.* By Lemma 1.2, 0 = ∫Ψ·WΦ_f = 𝒲_{(0,∞)}[Ψ] + ε𝒲(Ψ,RΨ) (disjoint supports; absolute convergence as in A_001 Thm 1.1(d)).
Compute the cross form of A_001 §1 with Φ₁ = Ψ on (0,∞), Φ₂ = RΨ on (−∞,0):
Lévy: −∫∫Ψ(x)Ψ(x′)ν(x+x′); primes: Φ₂(x−log q) = Ψ(log q − x) (nonzero for x < log q), Φ₂(x+log q) = 0 for x > 0, giving
−Σc_q(Ψ∗Ψ)(log q); pole: ∫∫Ψ(x)Ψ(x′)2cosh((x+x′)/2) = A² + B². Hence 𝒲(Ψ,RΨ) = −𝒲_refl[Ψ]. □
**Corollary 3.2 (archimedean part is a manifest SOS; PROVED).** ν(t) = Σ_{j≥0}e^{−(2j+½)t} (geometric series; completely
monotone), so ∫∫Ψ(x)Ψ(x′)ν(x+x′) = Σ_{j≥0}L_j(Ψ)², and L_0 = B. Therefore
  **𝔔[Ψ] = ε( Σ_{j≥1}L_j(Ψ)² + 𝒫[Ψ] − A(Ψ)² ).**
In Mellin terms (H(s) = ∫_0^∞Ψe^{(s−½)x}dx = Σ_n n^{−s}∫_n^∞ρ(t)t^{s−1}dt): L_j = H(−2j) (the Γ_ℝ trivial-zero abscissae),
A = H(1) (the pole), and 𝒫 pairs Ψ with itself along factorisations u·v = q (u = e^x) weighted by Λ(q)q^{−½} — exactly the
(ℕ,+,·) interplay of the semiring principle (ARGUED reading).
- **Answer to (ii).** Not a tautology: W_T/𝔔 on a self-dual sector equals a form that pairs Ψ with its reflection across the
  edge, in which the Lévy diagonal and the b_∞ term have disappeared and the archimedean part is a sum of squares. It is not a
  proof because 𝒫 has no sign: (Ψ∗Ψ)(log q) is indefinite.
- **Predictions (consequences of expected positivity, not proved; usable as falsifiers of positivity on 𝒮_±):**
  𝒮_+: 𝒫[Ψ] ≥ A² − Σ_{j≥1}L_j²;   𝒮_−: 𝒫[Ψ] ≤ A² − Σ_{j≥1}L_j². On 𝒮_− ∩ {A = 0} positivity forces 𝒫[Ψ] ≤ −Σ_{j≥1}L_j² < 0 and
  𝔔 = −(ΣL_j² + 𝒫): the prime self-convolution must be strictly negative there. **Untested (NUMÉRICO: not run).**
**Proposition 3.3 (sector orthogonality; PROVED given Lemma 1.2).** For f_± ∈ 𝒮_±, 𝔔(Ψ_+,Ψ_−) = 0.
*Proof.* Radical: 𝔔(Ψ_+,Ψ_−) = −𝒲(Ψ_+, −RΨ_−) = 𝒲(Ψ_+,RΨ_−); also 𝔔(Ψ_−,Ψ_+) = −𝒲(Ψ_−, RΨ_+). R-invariance and symmetry of
𝒲: 𝒲(Ψ_+,RΨ_−) = 𝒲(RΨ_+,Ψ_−) = 𝒲(Ψ_−,RΨ_+). So the cross term equals X and −X; it is 0. □
Hence on 𝒮, inf 𝔔/‖·‖ = min over the two sectors (the gauge/radical quotient of A_001 Prop 2.1 respects the split only if the
radical 𝒢̄ is 𝔉-stable — OPEN).

## 4. (iii) Crossing with the parity split (phase 198)
The phase-198 parity (AA_001) acts on the window function g by x ↦ −x on I = (−a,a); 𝔉 acts on the exterior data. Through
A_001 Thm 1.1 the window parity does not become R on Ψ̌ (R here reflects across the window *edge* after rescaling, not the
window centre). The two involutions do not act on a common space with a common frame, so the "4 sectors" are not a joint
decomposition (ARGUED). Where the numerically known minimiser (even window sector) and Mori's certified bottom sit relative
to 𝒮_±: **OPEN** (not computed; the minimiser is in PW data, and 𝒮 ∩ PW-type compact data = {0}, so the minimiser is
certainly *not* in 𝒮; its 𝒮-projection is not defined without fixing a Hilbert structure).

## 5. (iv) Falsifiers: where c = 1 is pinned
- **cΛ.** W_c = W + (1−c)Σ_q c_q(S_{log q}+S_{−log q}), so W_cΦ_f = (1−c)Σc_q(S+S^{−1})Φ_f ≠ 0. Then
  𝔔_c[Ψ] = ε𝒲_{refl,c}[Ψ] + (1−c)·⟨Ψ, Σc_q(S+S^{−1})Φ_f⟩ (PROVED as algebra, same convergence), and Prop 3.3 acquires a cross
  term (1−c)·(…) ≠ 0 generically: the sectors couple and Cor 3.2 gets an extra full-line prime term. The defect is linear in
  (1−c), consistent with AUDIT_4 §6(iv) (2(1−c)∫Θ_∞|F_c|²/2π, other normalisation; equality of the two expressions ARGUED, not
  checked). So the exact sector decomposition holds **only at c = 1**.
- **a_P (deleted / modified prime weights).** Same mechanism: Lemma 1.2 fails (H_Φ = ζ_a M_f is not radical for W_a unless the
  weights come from the same Euler product), sector coupling ∝ the weight change. ARGUED.
- **Beurling.** No Poisson summation ⇒ no Lemma 1.1 ⇒ no 𝔉-sectors (AUDIT_4 §6(v)).
- None of these falsifies the *structure*; they show the structure is Λ-specific (it uses Poisson for ℤ and the explicit
  formula for ζ jointly) — which is a necessary condition for a Λ-step, not a sufficient one.

## 6. (v) Residual
(★★_T) On 𝒮_±: ±(Σ_{j≥1}L_j² + 𝒫 − A²) ≥ κμ^{−A}dist²(·, radical). Plus the transfer problem: L′♯ lives on PW data, which
meets 𝒮 only in 0; Theorem 3.1 says nothing directly about the minimiser. Both OPEN. **Do not retry:** treating the
𝔉-sector form as a sign source without controlling 𝒫; using Hankel-CM positivity of the archimedean part as coercivity
(it is cancelled against A² and 𝒫, not against the diagonal); claiming the 4-sector decomposition (involutions do not commute
in a common frame).

## 7. Labels
| item | label |
|---|---|
| Lemma 1.1 intertwining | PROVED |
| 𝒮 infinite-dimensional (L²) | CITED (Landau–Pollak) |
| Schwartz-rich 𝒮; Lemma 1.2 on 𝒮 | CONDITIONAL / ARGUED |
| Prop 2.1 (D formula) | PROVED (C_c^∞) |
| constraint identity Q(F,G) − 𝔅 + ½R(1)G_h(0) = 0 on 𝒮_± | CONDITIONAL (PW-tail extension of mirror) |
| Thm 3.1, Cor 3.2, Prop 3.3 | PROVED given Lemma 1.2 |
| 4-sector decomposition | NO-GO as posed (ARGUED) |
| sector of minimiser | OPEN |
| cΛ / a_P / Beurling breaking | PROVED algebra / ARGUED / PROVED |
| (★★), (★★_T), L′♯ | OPEN |
No sign is claimed. Row D OPEN.
