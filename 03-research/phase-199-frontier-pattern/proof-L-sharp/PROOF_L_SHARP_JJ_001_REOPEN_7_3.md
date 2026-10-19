# PROOF_L_SHARP_JJ_001 — reopening constraints 7 and 3 with an operator-valued (2-branch) symbol in the exterior variable

Phase 199, Pen and paper; one scratch evaluation of an elementary closed formula (not stored) is labelled
NUMÉRICO and only checks Prop JJ.3. : , no zero
datum is used,

**Outcome (one paragraph).** (i) The Mellin symbol of the universal exterior form 𝔔 is scalar only before truncation; the
truncation u_n = u(·+log n)·1_{y>0} breaks dilation invariance, and on Langer chirps ρ = a e^{iφ_c} the correct symbol is a
**2×2 Hermitian matrix in the two branches t_−(τ) ∈ (1,√2), t_+(τ) > √2 of the Langer frequency map τ(t) = ct²/√(t²−1)**.
Pointwise in τ this matrix is *indefinite* (Lemma JJ.2: this is exactly constraint 3 again — the − branch can cancel the
symbol at fixed τ). After the averaging that is forced by c-free profiles (amplitudes slow on the τ-scale 2π/log n), the
symbol is block-diagonal: the diagonal is 𝔴_μ on both branches, and the only off-diagonal entries are the (1,n) resonant
couplings between t_− = s_n = √(1+n⁻²) and t_+ = √(n²+1), coefficient n^{−½}log(μ(1+n⁻²)). (iv) **Prop JJ.3 (PROVED,
elementary):** each 2×2 block satisfies |B_n|² ≤ θ_n²·A_nC_n with **θ_n² ≤ (L_n−ℓ_n)/(nH_nL_n) < 1/(nH_n) ≤ 1/3**, uniformly in
μ ≥ 4; hence the averaged matrix symbol is ≥ (1−1/√3)·diag ≥ 0.42·log 2μ. This is Theorem B′ with the coherent (1,n) couplings
as matrix entries (no van der Corput): **Theorem JJ.4 = leading-order (symbol-level) positivity, CONDITIONAL on a
symbol→operator transfer (OPEN at Fresnel scale, Y.8).** (iii) Test: the chirp-symbol predicts a relative floor 1−θ*(15) =
0.50 at μ = 15; the measured extremal has W/S = 0.29 < 0.50, so the extremal is **outside** the chirp class — its (1,n)
couplings are the Möbius-lattice lines (constraint 24), which coincide exactly (not Fresnel-localised) and are not in this
symbol. cΛ: the off-diagonal bound θ_n ≤ 1/√(nH_n) holds for every κ with L_n > κℓ_n; positivity is lost for κ > 1 only
through the diagonal (Y.9), and for κ < 1 the chirp-class matrix stays positive — **the matrix symbol on this class is not
Λ-specific** (constraints 2/5 are not met by it). (ii) Π: a constraint on the profile space can only restrict a form that is
already positive on the class; it does not change the numerator verdict; the denominator ℓ = λ‖Πρ‖² is untouched. Net:
constraint 3 is **genuinely escaped at symbol level on the chirp class** (positive matrix symbol with gap although the scalar
symbol has none), constraint 7 is **not needed on chirps** (θ < 1: no cross-class cancellation), but neither reopening reaches
the real extremal. L′♯ OPEN. Row D OPEN.

## 0. Corpus / index check, and why this is not a retry
- Read: AUDIT_CONSTRAINTS_001 (§1 rows 3, 7; §3 escape list), SYNTHESIS_MECHANISM_001 (M3, κ_emp ≥ 0.56 = W/ℓ), BRIDGE_001
  (Lemma B.0, F(N) = H_N log N − 2H₁(N) ≥ 0), X_001/Y_001/Z_001 (Thms B, B′, C; Y.2, Y.8, Y.9), AUDIT_L_SHARP_12 (Möbius
  lines, signs μ(n), W/S = 0.2904, constraint 24), TEST_2X2_001, U_001 (U.2.1).
- Index: ROUTES-TRIED-INDEX README l.449–493 (phase 199), grep "matrix symbol / matrix-valued / operator-valued": the only hit
  is AUDIT_CONSTRAINTS_001 §3 (the escape itself). No prior memo builds a branch-indexed symbol.
- New reason: Y_001 bounded the (1,n) pairs by van der Corput (size c^{−½}) and only *argued*
  (Y.8) the Fresnel-scale 2×2; constraint 3 excluded only scalar diagonal Mellin weights. Here the object changes: the symbol
  is a matrix over the two Langer branches, the (1,n) entries are kept exactly, and positivity is proved for the matrix (§3)
  instead of bounding the entries. Constraint 7's "forced cancellation" is ARGUED for gauge-type data; on chirps it is tested
  directly by θ_n.

## 1. Setting (definitions as Y_001 §1, E_001 Cor E.3)
ρ on (1,∞); u(x) = e^{x/2}ρ(e^x); dilation group (D_nρ)(t) = ρ(nt), in x a translation by ℓ_n = log n.
Ψ̌ = Σ_n n^{−½}u_n, u_n(y) = u(y+ℓ_n)1_{y>0} (Y.1); 𝔔[ρ] = 𝒜[Ψ̌] − 2Re⟨Ψ̌,Ψ̌_log⟩ + 2Re(A_p B̄_p), Ψ̌_log = Σ n^{−½}ℓ_n u_n.
Hence 𝔔 = ⟨ρ,𝒦ρ⟩ with 𝒦 = Σ_{m,n}(mn)^{−½}T_m^*[Θ_∞(D) − ℓ_m − ℓ_n]T_n + pole, T_n: ρ ↦ u_n.
- **Scalar symbol (why 3 bites).** Without the cut 1_{y>0}, T_n = translation, Fourier multiplier n^{iτ}, and 𝒦 has scalar
  symbol k(τ) = Θ_∞(τ)|Z(τ)|² − 2Re Z(τ)Z̄_log(τ), Z = Σn^{−½+iτ}, Z_log = Σℓ_n n^{−½+iτ} (formal) — a scalar weight on the line;
  constraint 3 (PROVED in its scope) says no such scalar weight is ≥ 0 for the complete distribution. The cut makes 𝒦 not a
  convolution: it is the truncation that carries information (E.1′ harmonic cut, Y.4).
- **Class.** (L_η,X) of Y_001: ρ = a e^{iφ_c}, φ_c = c√(t²−1), c = 2πμ, μ ≥ 4, a ∈ C²_c((1+η,X)), (Z₁), f(λ) = 0.

## 2. The branch-indexed symbol
**Lemma JJ.1 (two branches; PROVED, elementary).** τ(t) = ct²/√(t²−1) decreases on (1,√2), increases on (√2,∞), min 2c. For
τ > 2c there are exactly two preimages t_−(τ) < √2 < t_+(τ), and t_+/t_− takes each value r > 1 once; r = n ∈ ℕ exactly at
τ_n = c(n²+1)/n, t_− = s_n, t_+ = √(n²+1) (Y.2(iii)). At τ_n: log(τ_n/2π) = log(μ(n²+1)/n) =: L_n, the same for both branches.

**Phase-space decomposition (ARGUED, standard stationary phase; the PROVED counterpart is Y.5).** û(τ) = α_+(τ) + α_−(τ) +
O(caustic at τ = 2c), α_± the stationary contributions of t_±(τ), with |α_±|²dτ ↔ 2π|a(t_±)|²dt. Since û_n(τ) = n^{iτ}·(û
restricted to t > n), and t_− < 2, only dilate 1 sees t_−, while dilates 1,…,⌊t_+⌋ all see t_+:
 Ψ̌̂(τ) ≈ α_+(τ)D_{t_+}(τ) + α_−(τ), D_N(τ) := Σ_{n≤N} n^{−½+iτ}, Ψ̌̂_log(τ) ≈ α_+(τ)D^log_{t_+}(τ).
So with L(τ) = log(τ/2π) (log-symbol replacement, Y.3) the integrand of 𝔔 is the Hermitian form of
 **M(τ) = [[L|D|² − 2Re(D̄D^log), L D̄ − D̄^log], [L D − D^log, L]]** in (α_+, α_−) — the operator-valued symbol.

**Lemma JJ.2 (pointwise indefiniteness = constraint 3; PROVED algebra).** det M(τ) = −|D^log(τ)|² ≤ 0, with equality only if
D^log(τ) = 0. *Proof.* With z = α_+D + α_−, the form is L|z|² − 2Re(z ᾱ_+D̄^log); minimising in z at fixed α_+ gives
−|α_+|²|D^log|²/L. □ So the *pointwise* matrix symbol is never positive definite: the − branch reproduces the scalar obstruction.

**Averaging (the profile constraint).** For c-free amplitudes, α_± vary on τ-scale ≍ c, while n^{iτ}m^{−iτ} oscillates with
period 2π/|log(n/m)|. Average over windows of length ≫ 1, ≪ c: ⟨|D_N|²⟩ = H_N, ⟨Re D̄_N D^log_N⟩ = H₁(N), ⟨D_N⟩ = 1,
⟨D^log⟩ = 0, and the cross product α_+ᾱ_− carries the Legendre phase with derivative −(x_+−x_−) = −log(t_+/t_−), which is
stationary against n^{iτ} exactly at τ_n. Hence the averaged symbol is
- diagonal on branch +: H(t_+)L − 2H₁(t_+) = 𝔴_μ(t_+); on branch −: L = 𝔴_μ(t_−) (H = 1, H₁ = 0 on (1,2)) — both = 𝔴_μ
  (Y.4, B.0);
- off-diagonal: only at τ_n (Fresnel width (cn³)^{−½} in t), entry B_n = n^{−½}(L_n − ℓ_n)e^{iθ_n} = n^{−½}log(μ(1+n⁻²))e^{iθ_n};
  the n = 1 term (L·⟨D⟩) pairs t_+ with t_− at ratio ≠ 1 and is non-stationary (no resonance), so it averages out.
- the blocks for different n are disjoint (s_n − s_{n+1} ≈ n^{−3} ≫ Fresnel width for n ≪ c^{1/3}; Y.8).
So in Fresnel-localised coordinates (P_n = mass at s_n, Q_n = mass at √(n²+1)) the symbol is ⊕_n [[A_n, B̄_n],[B_n, C_n]] ⊕
(non-resonant diagonal), A_n = L_n, C_n = H_nL_n − 2H₁(n) (t_+ ∈ (n,n+1)).

## 3. Matrix positivity
**Prop JJ.3 (PROVED, elementary).** For μ ≥ 4, n ≥ 2: |B_n|² ≤ θ_n²A_nC_n with
 **θ_n² = (L_n−ℓ_n)²/(nL_n(H_nL_n − 2H₁(n))) ≤ (L_n−ℓ_n)/(nH_nL_n) < 1/(nH_n) ≤ 1/3.**
*Proof.* C_n − H_n(L_n−ℓ_n) = H_nℓ_n − 2H₁(n) = F(n) ≥ 0 (BRIDGE B.0, F(N) ≥ 0). So C_n ≥ H_n(L_n−ℓ_n) > 0 (L_n − ℓ_n =
log μ(1+n⁻²) > 0), and θ_n² ≤ (L_n−ℓ_n)²/(nL_nH_n(L_n−ℓ_n)). Finally 0 < L_n−ℓ_n < L_n and nH_n ≥ 3. □
NUMÉRICO check of the formula (not of the proof): sup_n θ_n = 0.451 (μ = 4), 0.500 (μ = 15), 0.527 (μ = 100), 0.563
(μ = 10⁸), always at n = 2, → 1/√3 = 0.577 as μ → ∞; θ_n ≈ 0.13 at n = 10, 0.03 at n = 100.
**Corollary.** A 2×2 block with |B|² ≤ θ²AC is ≥ (1−θ)·diag(A,C). Hence the averaged matrix symbol is ≥ (1−1/√3)·diag(𝔴_μ)
≥ 0.42·log 2μ (B.0), uniformly in μ ≥ 4 and n.

**Theorem JJ.4 (matrix-symbol positivity, chirp class).** On (L_η,X) at leading order in c (log-symbol replacement +
stationary phase on each branch, resonant blocks kept exactly):
 **𝔔[ρ] ≥ (1 − 1/√3)∫_1^∞𝔴_μ|a|² dt − (lower order) ≥ 0.42·log(2μ)‖a‖² − (lower order).**
Status: the symbol inequality is PROVED (JJ.3). The operator statement is **CONDITIONAL** on a symbol→operator transfer with
errors o(log μ)‖a‖² uniformly for amplitudes down to the Fresnel scale; for c-free profiles this transfer is Y.5 (PROVED, and
there the off-diagonal is even O(c^{−½})); for Fresnel-scale amplitudes it is OPEN (Y.8: replacement error n^{3/2}c^{−½}).
What is new relative to Y.5/Y.8: the (1,n) entries are no longer bounded in size but placed in a matrix whose positivity is
proved with an explicit μ-uniform gap; the "0.58 ARGUED" of Y.8 becomes the PROVED symbol bound θ_n < 1/√(nH_n).

## 4. Π (canonical gauge, U.2)
Π = orthogonal projection onto the Sonin annulus 𝒱_μ (U.2.1, PROVED, Fourier only). Restricting a profile space to Π-range
data restricts the quadratic form; JJ.3/JJ.4 are positive on the whole chirp class, so they remain positive on any subspace.
The gauge enters L′♯ only through the denominator ℓ = λ‖Πρ‖²; JJ.4 compares 𝔔 with ‖a‖², not with ‖Πρ‖². To convert one
needs ‖Πρ‖ ≤ C‖a‖ on the class (trivially true, ‖Π‖ = 1, ‖ρ‖ = ‖a‖), so at symbol level **𝔔 ≥ 0.42 log 2μ·ℓ/λ** on chirps —
but only on chirps; PRECHECK_T1 (Π negligible on real prolate tails) means this says nothing about the real data's gauge
structure. Constraint 7 on Π-data: on the chirp class it is not needed (θ < 1); on general Π-data it stays ARGUED both ways.

## 5. Tests
**(a) Against the measured extremal (μ = 15, NUMÉRICO data of AUDIT_12/13, read not recomputed).** The chirp symbol gives a
relative floor λ_min/diag ≥ 1 − sup_nθ_n(15) = 0.50. Measured: W/S = 0.2904, |offdiag|/S = 0.465, and (1,n) entries O(1) with
sign μ(n) (5/5 on μ(n) ≠ 0), with (1,4) = +0.108 not suppressed. 0.29 < 0.50: **the extremal's cross-dilate coupling is
stronger than any chirp-class matrix can produce**. Reason (AUDIT_12, constraint 24a/b, PROVED identity): the real exterior
datum carries Möbius truncation lines at frequency c/m; line m@1 and line nm@n coincide *exactly* (all τ, no Fresnel
localisation), so their coupling is not a resonant 2×2 block of JJ type but a full-strength rank-one coupling between ratio
classes. JJ.4 does not reproduce κ_emp ≥ 0.56 either (κ_emp = W/ℓ is gauge-normalised; JJ.4's ℓ-version is a chirp-only bound).
Verdict of the test: **the matrix symbol is correct on its class and fails to describe the extremal** (constraint 24b
re-confirmed: single-line/Langer symbols cover only the m = 1 line).
**(b) cΛ (comb × κ).** Entries: C_n^κ = H_nL_n − 2κH₁(n), B_n^κ = n^{−½}(L_n − κℓ_n). Same proof: C_n^κ − H_n(L_n−κℓ_n) =
κF(n) ≥ 0, so **θ_n^κ < 1/√(nH_n) whenever L_n > κℓ_n** — the off-diagonal never breaks positivity. For κ > 1, L_n − κℓ_n < 0
and C_n^κ < 0 for large n: positivity fails through the *diagonal*, uniformly in μ (Y.9, PROVED). For κ < 1, the chirp-class
matrix stays positive (θ^κ_n ≤ 0.54 at μ = 15, κ = 0.5, NUMÉRICO check). **So the matrix symbol on the chirp class is not
Λ-specific**: it separates κ > 1 but not κ < 1 (κ < 1 is killed elsewhere, AUDIT_8 §6, on non-chirp data). It cannot be the
sign mechanism by itself (constraints 2/5 HARD).

## 6. Verdict on the reopening
- **Constraint 3:** escaped at symbol level on the chirp class — PROVED symbol positivity with gap 0.42 log 2μ although the
  scalar (and the pointwise matrix, JJ.2) symbol has none; the escape needs the averaging over c-free profiles, i.e. it is a
  statement about a restricted class. New constraint text: **"3′: on Langer chirps the branch-averaged 2×2 symbol is positive
  (θ_n < 1/√(nH_n)); the pointwise branch symbol is indefinite (det = −|D^log|²)."**
- **Constraint 7:** on chirps, no cross-ratio-class cancellation is needed (diagonal dominance θ ≤ 1/√3). It remains forced
  (ARGUED) on gauge-type data and is visibly active on the extremal (AUDIT_12 offdiag/S = 0.465 with 32-digit Galerkin
  cancellation, TEST_2X2). SOFT status unchanged; scope narrowed: "7 does not bind on chirp-class data".
- **Residual (OPEN), precisely:** (R1) symbol→operator transfer at Fresnel scale (Y.8); (R2) a matrix symbol including the
  Möbius-lattice channels (lines m = 1…⌊μ⌋ with coefficients μ(m)/m, exact coincidences m@1 ↔ nm@n): the needed statement is
  positivity of the lattice Gram G_{m,m′} = Σ_n [coincidence weight]·μ(n)… with the 𝔴 diagonal — not attempted here; it is
  the only place where a Λ-specific (Möbius) sign can enter this symbol; (R3) edge P3b (f(λ) ≠ 0) and the caustic τ = 2c
  (Theorem C) are outside the class; (R4) a κ < 1 separator. L′♯ OPEN. Row D OPEN.
