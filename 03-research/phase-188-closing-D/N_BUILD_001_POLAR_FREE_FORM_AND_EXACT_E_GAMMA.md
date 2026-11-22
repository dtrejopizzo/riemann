# N_BUILD_001 — Polar-free form of (N) on P_T, the exact form of (E_γ), mesh Tate constraints, alignment with L2_BUILD_006

Track (N), pen and paper only (no computation). positivity assumed
true; labels PROVED / CITED / CONDITIONAL / OPEN / NO-GO. Notation of Paper 46 (main.tex): ω_k = πk/2T, a_k = |F̂(ω_k)|²,
w = c_F, v_n = 2Λ(n)/√n, K (lem:K), m = Re ψ(¼+iτ/2) − log π, P_T = {A = B = 0}, F = (¼−∂²)G with G ∈ H²_0(I_T)
(thm:nyq-cone), 𝓕_T(F) = 2∫_{[1,e^{2T})} y^{-1/2} w(log y) d(ψ(y) − y) (prop:wit-cheb).

## Corpus check
grep (03-research 1–188, 04-papers, 05-meta, MAP_D.md, master grid): "polar part", "Tate", "5/4", "K₁", "K − 2e^{−u/2}",
"PNT-ventana", "Chebyshev form", "(E_γ)", "Nyquist", "T²+π²k²", "coherence".
- **R186_033 Lemma 1 (PROVED there)**: PNT-window identity 𝔞_T(F) = (C₀+4)Φ(0) + 2∫x^{-1/2}Φ(log x)d(x−ψ) + Lev_{K₁}(Φ),
  K₁ = K − 2e^{−u/2}. **phase-114 114_d_133**: digamma shift ¼ → 5/4. **R160_PD_R1 Thm E(iii)**: Stieltjes form with kernel
  ω = ½c − c′. So items (A), (B) below are **corpus-known**; they are restated only to fix notation for (C)–(F).
- Paper 46 rem:wit-cheb states (E_γ) only up to a slack ±4 (sandwich m(γ)−4 / m(γ)+4). No memo found giving the exact
  form (C). No memo found writing the Tate conditions as explicit alternating mesh identities (D) (R186_052 Cor 3.2 gives
  the weight (τ²+¼)², not the mesh identities). L2_BUILD_006 §2 uses the slack δ₀* = λ_{∞,P} → C₀; the polar-free slack (E)
  is not there.

## (A) Polar elimination (corpus-known: R186_033 L1; proof re-derived)
For F ∈ P_T: 2∫₀^{2T} w(u)e^{u/2}du = −𝔭(F), 𝔭(F) := (1/2π)∫|F̂|²/(¼+τ²) = ‖G′‖² + ¼‖G‖² ≥ 0.
*Proof.* P_T ⇒ ∫_{−2T}^{2T} w cosh(u/2) = Re(AB̄) = 0 (prop:P), w even, so 2∫₀^{2T}we^{u/2} = −2∫₀^{2T}we^{−u/2}
= −∫_{−2T}^{2T} w e^{−|u|/2}, and ∫e^{−|u|/2}e^{iτu}du = 1/(¼+τ²) (Parseval). Second expression: F̂ = (τ²+¼)Ĝ. ∎

## (B) The primitive form is a ψ(5/4) form against the pure fluctuation (corpus-known)
For F ∈ P_T ∩ D_T: 𝔞_T(F) = 𝔞^♯(F) − 𝓕_T(F), 𝔞^♯(F) := (1/2π)∫ m^♯|F̂|², **m^♯(τ) = Re ψ(5/4 + iτ/2) − log π
= m(τ) + 1/(¼+τ²) = (C₀+4) + Σ_{k≥1} τ²/(a_k(τ²+4a_k²))**, a_k = k+¼.
*Proof.* eq:Aform with prop:wit-cheb: Σv_n w(log n) = 2∫₀^{2T}we^{u/2} + 𝓕_T = −𝔭 + 𝓕_T. And ψ(z+1) = ψ(z)+1/z,
Re 1/(¼+iτ/2) = 1/(¼+τ²); the k=0 term of φ (thm:S) is 4τ²/(τ²+¼) = 4 − 1/(¼+τ²). ∎
m^♯ is increasing in |τ| (complete Bernstein φ₁), m^♯(0) = C₀+4 = ψ(5/4) − log π < 0.

## (C) Exact form of (E_γ) — NEW, PROVED
With F_T = F_T^γ the spectral-derivative family (§17):
  **(E_γ) ⟺ limsup_{T→∞} 𝓕_T(F_T)/‖F_T‖² ≤ m^♯(γ).**
*Proof.* F_T ∈ P_T, so 𝔖_T(γ) = (−𝔭(F_T) + 𝓕_T(F_T))/‖F_T‖². By lem:wit-conc with p(τ) = 1/(¼+τ²) (continuous, even,
bounded), 𝔭(F_T)/‖F_T‖² → 1/(¼+γ²). Hence limsup 𝔖_T − m(γ) = limsup 𝓕_T/‖F_T‖² − m(γ) − 1/(¼+γ²). ∎
This replaces the two-sided slack ±4 of rem:wit-cheb by an equality of conditions. The threshold m^♯(γ) is the
archimedean level of the ξ-normalised Gamma factor; it is ≥ C₀+4 for all γ.

## (D) Tate constraints on the mesh — NEW (explicit form), PROVED
For every a ∈ 𝒦_T (thm:nyq-cone):
 (D0) Σ_k (−1)^k a_k = 0;  (D1) Σ_k (−1)^k a_k /(T²+π²k²) = 0;  (D2) Σ_k (−1)^k a_k (π²k²−T²)/(T²+π²k²)² = 0.
*Proof.* f = |F̂|² extends to an entire function of type ≤ 2T, in L¹(ℝ) ∩ L^∞; cardinal series at step π/2T (Nyquist for
type 2T) converges locally uniformly: f(z) = Σ_k a_k S_k(z), S_k(z) = sin(2Tz−kπ)/(2Tz−kπ). [Justification: f ∈ PW_{2T}
∩ L², Whittaker–Kotelnikov–Shannon, CITED.] At z = i/2: sin(iT−kπ) = (−1)^k i sinh T, so
S_k(i/2) = (−1)^k sinh T·(T − ikπ)/(T²+k²π²). For real F, f is even (a_k = a_{−k}); the odd-in-k imaginary parts cancel, and
f(i/2) = 0 gives (D1). Differentiating, S_k′(i/2) = 2T[cos x/x − sin x/x²], x = iT−kπ, cos x = (−1)^k cosh T; f′(i/2) = 0 with
(D1) and symmetry leaves (D2). (D0) is lem:nyq-sampling(iii). For complex F apply to Re F, Im F (§17 opening). ∎
Since ¼+ω_k² = (T²+π²k²)/4T², (D1) is the statement that the polar sample p_k = ((−1)^k e^T − 1)/(¼+ω_k²) acts on 𝒦_T as
−1/(¼+ω_k²): **the e^T-size polar oscillation is invisible on primitive samples**, mesh form of (A).

## (E) Alignment with L2_BUILD_006 — NEW, PROVED
L2_BUILD_006 §3: (L2) at T ⟺ (N_loc) Σ v_n Re w(log n) ≤ 𝔞_∞(F) on P_T, with slack δ₀*(T) = λ_{∞,P}(T) ↓ C₀.
By (A), (N_loc) ⟺ **(N^♯): 𝓕_T(F) ≤ 𝔞^♯(F) for all F ∈ P_T ∩ D_T**, and the archimedean slack becomes
λ^♯(T) := inf_{P_T, ‖F‖=1} 𝔞^♯(F), with
 (i) λ^♯ nonincreasing; (ii) λ^♯(T) ≥ C₀+4 for all T; (iii) λ^♯(T) → C₀+4 as T → ∞.
*Proof.* (i) nested P_T. (ii) m^♯ ≥ m^♯(0). (iii) take F = (¼−∂²)G_T with Ĝ_T concentrated at 0 at scale 1/T (dilates
of a fixed G ∈ C_c^∞ with ∫G ≠ 0 normalised in L²): (1/2π)∫m^♯|F̂|²/‖F‖² → m^♯(0) by the argument of lem:wit-conc (the
weight (τ²+¼)² is continuous and nonzero at 0). ∎
So the deficit the fluctuation has to cover on the negative cone is at most |C₀+4| = 1.37…, not |C₀| = 5.37…: the
"−4" is the polar term, paid exactly by P_T. (Corpus R186_033 noted C₀+4 at the level of the form; the identification
as the (L2)-frame slack is new.)

## (F) No F-uniform signed bound for the fluctuation — NO-GO (PROVED)
sup{𝓕_T(F): F ∈ P_T ∩ D_T, ‖F‖=1} ≥ A_T − 4.
*Proof.* 𝓕_T = Σv_n w(log n) + 𝔭(F) ≥ Σ v_n w(log n), and 𝔭 ≤ 4‖F‖²; L2_BUILD_005 §3(b) gives unit F_τ ∈ P_T with
Σ v_n w(log n) → Σ v_n (1 − log n/2T) ... ; more simply the same packet with φ concentrated near t ∈ {±T/…} — we use only
that the sup of Σ v_n Re w(log n) on the unit sphere of P_T is A_T (005 §3(b), lem:mbounds(iii)). Hence sup 𝓕_T ≥ A_T − 0
on that sequence, and ≥ A_T − 4 a fortiori. ∎
Consequence: any proof of (N^♯) must weight by m^♯ (the high-frequency packets are paid by m^♯ ~ log τ); a signed
bound uniform in F is impossible, consistent with prop:wit-sens.

## Barrier position
(A)–(E) are exact identities/reformulations: they carry the whole margin λ_A and decide nothing (as R186_033). They are
not inside W-coh (no Lipschitz functional of the coherence is asserted to imply anything), W-loc (no local criterion),
W-mom (no trace). (F) is itself a W-coh-type statement.

## Self-review
1. (A)/(B): duplicate of R186_033 / 114_d_133 — accepted, labelled corpus-known. 2. (C): check that F_T ∈ P_T (§17
says A = B = 0 by two integrations by parts — yes) and that p = 1/(¼+τ²) satisfies lem:wit-conc's growth hypothesis
(bounded, M = 0) — yes. Holds. 3. (D): the cardinal series needs f ∈ PW_{2T} ∩ L²: f ∈ L¹ ∩ L^∞ ⊂ L², type ≤ 2T —
yes; differentiation termwise is legitimate (locally uniform convergence of entire functions). Sign conventions of F̂
(e^{iτt}) do not affect (D1)–(D2) since f is even. Holds. 4. (E)(iii): the dilation argument needs F_T ∈ P_T: F = (¼−∂²)G,
G ∈ H²_0 — automatic. Holds. 5. (F): first draft wrote "Σv_n(1 − log n/2T)"; that limit is < A_T, so the sup bound
should cite lem:mbounds(iii) directly (sup_τ comb = A_T, Kronecker) — corrected to the A_T statement via 005 §3(b).
Verdict: (C), (D), (E) PROVED and new in the stated sense; no sign contact; no negative value.
