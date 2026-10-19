# INV_U_001 — The contact-crossing event: edge law, onset, one-sided derivatives (track U, residual seed of INV_S_001 §5)

 Notation of Paper 47: 𝔞_T(F)=C₀‖F‖²+Lev(c_F)−Σ_{n∈𝒩_T}v_n c_F(log n) (eq:Aform),
P_T={A=B=0}, λ_A(T)=min 𝔞_T on unit P_T∩𝒟_T (lem:compact), T_n=½log n, v_n=2Λ(n)n^{−½}. Labels: PROVED / ARGUED / CONDITIONAL / NUMÉRICO.
No new numerics were run; NUMÉRICO items below are quotations of R186_048 Tabla 4.2.

## 0. Corpus / index check and new reason
- ROUTES-TRIED-INDEX: README «Fase 191» SPEC_A (exact induction in T by contacts; design correction: entry instant empty,
  atom seen only through a 2ε collar; reworked: identity-only version OPEN, gap (θ)); CA_R3_001 Prop Θ, CA_R4_001 (step ½log5→½log7);
  04_PHASES L2_001 (edge-mass lemma, PARTIAL), lem:flowdet / Hellmann–Feynman in T (NO-GO, coefficient dominated by h*-functionals);
  lem:monoT / G8F-157 O1 (REF-D); L2_016 (Frobenius doubling induction, NO-GO); R8-02 (monotonicity, NUMERICAL-ONLY);
  Fase 195 INV_S_001 (Stokes, residual seed = this track). Grid/crossword: R186_048 (entry invisibility L3.1, visibility bound L3.2,
  Prop 4.3, Tabla 4.2 with the NUMÉRICO edge exponent a≈0.15–0.25, p≈1.3–1.5).
- **What is new (written reason).** SPEC_A/R186_048 treat the crossing as a perturbation whose size is a *numerically fitted*
  edge-mass power ε^{2a+1}. They never derive the edge law of the minimizer from the symbol, never give a proved modulus, and never
  compare the *local crossing law* across falsifiers. This memo changes the object: (i) the boundary asymptotics of h*_T derived from
  the Lévy kernel (log-Laplacian type), (ii) a proved, test-uniform modulus at a crossing, (iii) the one-sided derivatives, (iv) a
  classification of crossing-local data under O_4/O_6/Beurling. It is not an induction (no step lemma is proposed), so the SPEC_A
  kills/gaps are not re-entered; the recursion of §3 is tested only for whether a crossing-local monotone exists.

## 1. Correction of the premise «clamped ends, order 2»
P_T is a closed subspace of L²(I_T) cut by two **moment** conditions A(F)=∫F e^{t/2}=0, B(F)=∫F e^{−t/2}=0. They impose no boundary
vanishing: 1_{I_T} − (projection on span(e^{±t/2})) ∈ P_T∩𝒟_T has nonzero edge values (𝟙_{I_T}∈𝒟_T since ∫log(2+|τ|)|τ|^{−2}dτ<∞).
**PROVED.** So there is no Tate clamping; any edge vanishing of h* must come from the operator, not from P_T. Edge behaviour is
decided by the Lévy kernel K(u)~1/(2|u|) as u→0 (symbol m(τ)~log|τ|, lem:K) through the killing term on leaving I_T (INV_N_001 split).

## 2. The crossing at T_n
**Lemma U0 (entry invisibility; = R186_048 L3.1, recalled).** c_F(2T_n)=0 on L²(I_{T_n}); 𝔞_{T_n^+}=𝔞_{T_n^−}. PROVED.

**Lemma U1 (universal edge-mass bound; PROVED).** For F∈𝒟_T with ‖F‖=1 and ‖F‖_Q²:=(1/2π)∫log(2+|τ|)|F̂|²≤Q, and any interval J of
length δ<1/e: ‖F1_J‖² ≤ (Q+2)/log(1/δ) · (1+o(1)).
*Proof.* Split F=F_≤R+F_>R in frequency. ‖F_>R‖²≤Q/log(2+R). ‖F_≤R 1_J‖²≤δ‖F_≤R‖_∞²≤δ(R/π)‖F‖². Take R=1/(δ log(1/δ)). ∎

**Proposition U2 (proved modulus at a crossing; PROVED).** Let η>0 be smaller than the gap to the next contact and λ^{fr}(T) the bottom
with the comb frozen at 𝒩_{T_n} (n omitted; same window, same P_T). Then for T=T_n+η
  |λ_A(T) − λ^{fr}(T)| ≤ v_n·C_T/log(1/(2η)),
C_T explicit from Q=V+C′ of the proof of lem:contT (near-minimizers have bounded ‖·‖_Q).
*Proof.* The two forms differ by −v_n c_F(log n), and |c_F(log n)|≤‖F1_{[−T,−T+2η]}‖‖F1_{[T−2η,T]}‖ (R186_048 L3.2) and Lemma U1 on near-minimizers of either form (both have bounded ‖·‖_Q); compare
Rayleigh quotients both ways. ∎ This quantifies lem:contA at a crossing: modulus 1/log(1/η), uniform over the class (any
v_n ≥ 0). It carries no sign.

**Proposition U3 (edge law of the minimizer; ARGUED, matched asymptotics).** Near t=T−δ, h*_T(t) = a_+ (log(κ/δ))^{−1/2}(1+o(1)),
and likewise at −T with a_−; the exponent ½ is universal (independent of T, of the comb and of the Tate multipliers).
*Derivation.* Smooth bounded terms (comb, polar part e^{±t/2}, killing from the far side, eigenvalue) are O(g). With g(δ)=L^{−α},
L=log(1/δ), and kernel c/|u| at 0: regional part ∫_δ(g(δ)−g(y))c dy/y = −cαL^{1−α}/(1−α)(1+o(1)); killing part g·c·L = cL^{1−α}.
Leading balance forces α/(1−α)=1, α=½. Agrees with the boundary decay ℓ(δ)^{1/2}, ℓ=1/log, known for the logarithmic Laplacian
(Chen–Weth 2019 and follow-ups; CITED, not re-verified here — hence ARGUED). Consequence: h* has **zero boundary traces** but decays
slower than any power; the power-law reading a≈0.15–0.25 of R186_048 §4 is a finite-resolution artefact of (log 1/δ)^{−1/2}.

**Corollary U4 (onset law; ARGUED from U3).** c_{h*}(2T_n+2η−log n)=c(2T−2η)=∫_0^{2η}h*(−T+s)h*(T−2η+s)ds = a_+a_−·2η/log(κ/2η)·(1+o(1)).
So the first-order cost is D_n(η)=v_n a_+a_− 2η/log(κ/2η): **onset exponent exactly 1 with a logarithmic correction**; effective
local exponent p_eff = 1+1/log(κ/2η), which increases with η.
*Consistency (NUMÉRICO, quoted, not new):* R186_048 Tabla 4.2, column v_n c_{h*}, n=3: local exponents 1.41, 1.47, 1.56 for
2η = .004→.032 — increasing in η, as predicted, and incompatible with a constant power; n=4: 1.47–1.49. n=5 (p≈2.4) is not matched:
there λ_A≈10^{−12} and a_+a_− is nearly cancelled (near-degeneracy of sectors) — open, not fitted.

**Corollary U5 (one-sided derivatives at T_n).** (a) CONDITIONAL on bounded edge traces h*(±T) (hypothesis H_tr) and differentiability of
λ^{fr} at T_n: D^±λ_A(T_n) exist and D^+λ_A(T_n) − D^−λ_A(T_n) = −2v_n h*(T_n)h*(−T_n) (Hellmann–Feynman, lem:flowdet, with c′(2T^−)=F(−T)F(T)).
(b) ARGUED (U3: traces vanish): the jump is **0**; λ_A is C¹ across every crossing, the crossing being visible only at order
η/log(1/η). Sign of the jump in dλ_A/dT: none (zero). (c) PROVED unconditionally: only the C⁰ modulus of U2.

## 3. Crossing recursion and the search for a monotone quantity
Between crossings (comb fixed) λ_A is nonincreasing (lem:monoT) with drift given by the dilation generator (HF on U_r):
dλ/dT = −(1/T)[(1/2π)∫τm′(τ)|ĥ*|² + Σ_{n∈𝒩_T}v_n log n·(−c′_{h*}(log n)) + Tate-multiplier term] (ARGUED, formal HF; λ simple).
At T_n: no jump in λ (U0), no jump in λ′ (U5b), a non-analytic germ −v_n a_+a_−·2η/log(κ/2η). Recursion:
  λ_A(T_{n⁺}) = λ_A(T_n) − ∫_{T_n}^{T_{n⁺}} [drift] − Σ (germs),
with every term a functional of h* (edge amplitudes a_±, ĥ*) weighted by the data (log n, v_n). A quantity λ_A·w(T) nondecreasing
between crossings is equivalent to w′/w ≥ |λ′|/λ: no explicit w is available without a lower bound on λ_A itself (the condition is a
restatement; REF-D). Crossings contribute nothing to first order, so «controlled jumps» are automatic and carry no information.
**Finding (ARGUED):** the Stokes-type event of INV_S_001 §5 exists (germ η/log η, non-analytic in T, ℤ-indexed in position) but is
weaker than the residual seed hoped: it is invisible at C¹.

## 4. Falsifiers: which crossing property distinguishes Λ?
Local crossing law = (position T_n, weight v_n, exponent ½ of U3, amplitudes a_± of h*).
- O_6 (deleted primes): missing crossings = missing germs v_n a_+a_−η/log η; local law at surviving crossings identical. F-deletion
  is a falsifier (λ fails), so «crossings occur only where they occur» cannot decide.
- O_4 (scaled comb (1+c)Λ): same positions, germs scaled by (1+c); exponent identical.
- Beurling (non-integer x_k): germs at ½log x_k with the same exponent ½ (it comes from the archimedean kernel only) and the same C¹ property.
**Theorem-level statement (ARGUED, class 𝒦_cross = properties determined by crossing-local data):** exponent, C¹-ness, modulus (U2,
PROVED, any v ≥ 0) and germ form are comb-generic; positions and weights are data (clause 1 fails: linear/comb-generic). The only
Λ-dependence is through a_±(T_n) = edge amplitudes of h*, i.e. a functional of h*, not of σ (wall of phases 183–186). NO-GO for 𝒦_cross.

## 5. Six clauses (sign-carrier spec) and REF-D
(1) comb-generic: FAILS (§4). (2) cone on log ζ: not reached. (3) integrality: positions are ½log n, used only as data: FAILS as a
carrier. (4) sparse-stable: deletion leaves surviving crossings unchanged: FAILS. (5) coupling with the FE other than via ζ(½+iτ):
none; the exponent ½ comes from Γ_ℝ (archimedean kernel) alone and is place-additive with the comb (as in INV_S S1). (6) ∂log:
not reached. REF-D: the recursion of §3 summed over all crossings is λ_A itself.

## 6. Labels / outcome
PROVED: §1 (no clamping), U0 (recalled), U1, U2 (modulus 1/log(1/η) at a crossing, class-uniform).
ARGUED: U3 (edge law (log 1/δ)^{−1/2}, CITED analogue Chen–Weth), U4 (onset 2η/log(κ/2η)), U5(b) (C¹ across crossings), §3 drift formula,
§4 NO-GO for 𝒦_cross. CONDITIONAL: U5(a) (H_tr). NUMÉRICO: quoted Tabla 4.2 trend only.
Corrections proposed to the record: R186_048 §4 / SPEC_A §1 «h*~(T−|t|)^a, a≈0.15–0.25» → artefact of (log 1/δ)^{−1/2} (ARGUED).
Row D: OPEN; no sign. Residual: decide U3 rigorously (boundary regularity for the killed Lévy operator with kernel K of lem:K on P_T);
it would turn U4/U5(b) into PROVED, still without sign.

[ nota: §1 correcto en la variable F; equivalencia exacta P_T = (¼−∂²)H²₀(I_T) (extremos sujetos en G) PROVED en VERIFY_CLAMPED_AND_EDGE_LAW.md; U3 sigue ARGUED; cita del exponente ½ óptimo: Hernández-Santamaría–López Ríos–Saldaña 2024 (DCDS-A), Chen–Weth 2019 sólo el marco.]
