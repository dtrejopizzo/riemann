# R184_002 — audit of phase 170 ("global inequality on the primes")

Audit. No file of phase 170 is modified.
RH is not claimed. Reading: README (full log R170_8xx), R170_000, R170_808,
R170_841, R170_885–888, R170_892–894, R170_898–899 (+ R170_900 in the README);
grid R162_2300 §§3, 4, 7.

## State

**Verdict: the residue of phase 170 is NOT a genuine open inequality.
It is a vanishing equation (not an inequality) posed on a vector
that exists only if RH fails on a finite window; it is composed of
exact identities with no sign [W12] about the jet at first contact [W5], and its
quantified form "∀T, ∀ first-contact vector" is vacuously true
under RH and, combined with the (also open) chain that would turn it into
a contradiction, would be exactly "there is no first contact" = RH [E1].**
By itself it is OPEN-vacuous; as a route to D: NO-GO [W12 + W5, with E1 form].
There is no cheap case in ζ where it can be decided (there is no contact for T ≤ ½log5,
certified). The only informative test is on falsifiers with contact
(§4).

## 1. The reconstructed chain (≤ 2 pages)

Common notation. I = [−T,T], P = restriction to I, Q = I − P. τ_a f(t) = f(t−a).
𝓜 = m(D), m(τ) = Re ψ(¼+iτ/2) − log π. L_M = Σ_{r≤M} Λ(r) r^{−½} τ_{log r},
A_M = 𝓜 − L_M − L_M^*. S_N = Σ_{n≤N} n^{−½} τ_{log n} (integer comb),
C_N f(t) = e^{−t/2}∫_{−∞}^{t+log N} e^{u/2} f(u) du (continuous polar),
Z_N = S_N − C_N (Euler–Maclaurin discrepancy). Virial derivation
Ḃ = d/ds U_s^{−1}BU_s, with τ̇_{log a} = −(log a) ∂_t τ_{log a}.

| step | content | status |
|---|---|---|
| R170_000 | W_T(F) = archimedean + polar − Σ_{n<e^{2T}} 2Λ(n)n^{−½} Re c_F(log n) ≥ 0 ∀F ∈ L²(I). "∀T" ⟺ RH (R163_401 Thm 1.2) | definition; the ∀T form is **E1** (W1, "∀T of a per-window law") |
| R170_101/808 | domain, finiteness, archimedean transport to b − a_L − H_L; theorem (A): the reserve R_S cannot be ruled out | PROVED (identities); (A) PROVED, is a construction no-go |
| T_c, first contact | T_c = inf{T: λ_T ≤ 0}; if T_c < ∞, ∃F ≠ 0 in ker H_{T_c} (KKT: A F = ρb, (F,b)=0, ‖F‖=1) | definition; F exists **only if RH fails** (λ_T>0 certified on (0,½log5]) |
| R170_841 (VIR–LB) | goal: 𝒱_{Λ,T}(F) ≤ 0 on N_T^ε; antisymmetric channel 𝒜 = L̇_M S_N − L_M Ṡ_N with β_Λ(k) = Σ_{d|k}Λ(d)log(d²/k), no sign | coefficients PROVED; sign of β FALSE; VIR–LB OPEN; it is a jet at λ=0 [**W5**] |
| R170_884–885 (EM port) | 𝔚_ext + (h,P𝒫_{C,A_M}F) = W(QZ_N^*h, ℓ) − W(PC_N^*h, r), h = (PS_N^*P)^{−1}b | exact identity with no sign [**W12**] |
| R170_886 (range) | vanishing ⟺ ω_EM ∈ Ran H_T, i.e. H_T g = A_M^* ė − Ȧ_M^* e | Fredholm reformulation (audited as such by 887); [**W12**] |
| R170_887 | covariant version: + χ_e, A Ḟ, Ṗ, Ṙ_T; pending law (5.1) = covariant vanishing | identity PROVED; vanishing OPEN |
| R170_888 | Hellmann–Feynman in Z_N coordinates: ν = (4 lines) ≤ 0; no line carries a sign; parity refutes identifying the linear EM residue with λ̇ | PROVED; the "≤0" is minimality (trivial at a contact), not information |
| R170_890–892 (Tate quadratization, bordered KKT) | σΔ is exact virtual work; hyperbolic block of signature (1,1); moving counterexample in ℝ²: σΔ of either sign with fixed KKT and minimality | PROVED; "KKT fixes σΔ sign" REFUTED |
| R170_893 | gΔ^Tate − Ω_EM = ρ[(ḃ⁰,b) − g] − (h,P𝒫_{C,A_M}F); identification ⟺ (0.5) | identity PROVED; (0.5) OPEN |
| R170_894 | (0.5) ⟺ 𝔑_pol(F) = 0 with two exterior moments 𝖷_N(QȦF), 𝖣_N(QAF) and the moving face t + log N; **§4: the interior contact data does not determine them** | PROVED; abstract independence PROVED |
| R170_898–899 | 𝒫_{C,A_M}(N) = 𝒢_𝓜 − 𝒢_{L_M} − 𝒢_{L_M^*}, 𝒢_B(N) = 𝒢_B(1) + ∫_1^N [Ḃ dC_x − B dĊ_x]; orientations log(x/r) and log(xr); residue (5.3)/(7.2) | identities PROVED; **valid for any sequence of weights in place of Λ** (pure convolution algebra); vanishing OPEN |
| R170_900 | substituting PC recombines ledgers 853/856; no reduction | PROVED (collision) |

The only thing specific to Λ in the whole chain is Λ = μ * log over ℤ
(R170_863–869, 880–883) and δ_Λ = 0 (841). R170_868–869 prove that everything
that factors through the divisor defect D_N lives in the ideal Q·D_N and **does
not determine** the boundary class β_phys = W_K + Θ_ext; R170_874 varies β_phys
while preserving Λ*1 = log, PC, the Tate cocycle and diagonal minimality.
That is: the phase itself proved that its only arithmetic input does not fix
the residue.

## 2. The residue as a single statement

Space: ℋ_ε = {F ∈ L²(ℝ) : supp F ⊂ I, F(−t) = εF(t)}, in the energy
domain 𝒟_T of R170_000. Data: T > 0, integers N ≥ e^{2T}, M ≥ N, parity ε.
b = b_ε ∈ ℋ_ε the polar (Tate) column of the parity; g = ‖b‖²;
h = (P S_N^* P)^{−1} b (causal inverse, exists because P S_N^* P = I + nilpotent);
H_T = compression of A_M to {b}^⊥ ∩ ℋ_ε (the form W_T restricted to the
parity, with the polar part absorbed as a restriction).

**(R170-RES).** For every T > 0 and every F ∈ ℋ_ε, ‖F‖ = 1, (F,b) = 0, with
P A_M F = ρ b for some ρ ∈ ℝ and (F, A_M F) = 0 = min (first contact),
one has

  Re (h, P[C_N Ȧ_M − Ċ_N A_M] F) = ρ · Re[(P Ṡ_N^* P h, b) − g].

Expanded (R170_894(3.2)): with α(f) = ∫_I e^{u/2}f, β(f) = ∫_I u e^{u/2} f,
H_0 = ∫_I e^{−t/2}h, H_1 = ∫_I t e^{−t/2}h, u = PȦ_M F, v = QȦ_M F, ℓ = QA_M F,

  H_0 α(u) + 𝖷_N(v) − ρ[(H_0 − H_1/2)α(b) + (H_0/2)β(b)] − 𝖣_N(ℓ)
     − ρ[(PṠ_N^*Ph, b) − g] = 0,

with 𝖷_N(v) = ∫_I h e^{−t/2} ∫_{−∞}^{t+log N} e^{u/2} v, and 𝖣_N(ℓ) the same
with weights (1 − t/2), u/2 and the face −(log N)√N ℓ(t + log N).

Type observations:
1. **It is an equality, not an inequality.** The sign enters only afterward,
   via σΔ in the KKT (892), and there it is refuted in the abstract. The "inequality"
   form of the request (sign of the Wronskian on the contact vector) is VIR–LB:
   𝒱_{Λ,T}(F) ≤ 0 ∀F ∈ ker H_{T_c}, which likewise uses
   nothing outside contact.
2. **Quantification over an empty set under RH.** For T ≤ ½log5 the
   set of admissible F is empty (λ_T ≥ 10⁻¹⁸, P47 thm:log5W). Under RH
   (with λ_T > 0 strict) it is empty for every T. Hence RH ⟹ (R170-RES) trivially;
   the useful direction is (R170-RES) + [identification (887/892) + sign] ⟹
   absence of contact ⟹ RH. That combination is "contact is
   impossible," the E1 statement of R163_401 rewritten on its witness.
3. The tails: with M, N finite, R_M = L − L_M and U_N enter only through the
   exterior blocks Q; 899 §7 makes explicit that the step M → ∞ is not
   justified (series Σ Λ(r)/r diverge in L C_N).

## 3. Battery of falsifiers (grid §4)

Criterion: identities 884–899 are convolution algebra with generic
weights; hence (R170-RES) is **defined** for every model with an atomic
arithmetic side and a first contact. What separates them is whether the model
satisfies the *inputs* of the chain.

| model | contact? | (R170-RES) defined? | which input it uses / verdict |
|---|---|---|---|
| DH | yes (zeros off) | yes with weight Λ_DH; ordinary comb | δ_a ≠ 0 breaks the telescoping 841(0.4) and the null line 866; separates **only** via Λ*1=log. But 868/874: that identity does not fix the residue. Value not computed |
| deletion Λ1_{n≥5} | yes, λ_W ≤ 0.4608 < T* | yes | same: Λ*1 ≠ log. Real cheap test (§4) |
| κ-models / finmod | yes | yes | same; blind if the chain only uses linear identities (W3) |
| Beurling DMV | yes (in its Weil form) | yes if S_N is rewritten with the Beurling comb | all identities in the chain are generic in the comb; with the Beurling comb Λ_B*1 = log_B holds exactly ⟹ the chain cannot distinguish; the only thing left is Z_N (sawtooth of ℤ), which the grid classifies under W4 and integrality. Separation not proved → **W3/Theorem S** |
| Λχ₂ | — | with ordinary comb the null line fails; with the χ comb it holds | same as DMV: separates by "comb with coefficients 1" (Φ_Λ), not proved to enter the value |
| Type I curve with two atoms | yes, by construction (s₂^c) | yes, weights in {2,3} | Λ*1 = log fails; same status as deletion. Cheap test |
| M_m | yes | **not defined**: non-atomic arithmetic side | the chain does not see it; separation by atomicity = O2601.1, not used |
| M_m windowed | yes | partially (Λ in the window; positive tail) | the residue uses the tail only through linear Q blocks; Thm 3.1 of R164_601: the sign of the tail does not exclude quartets |
| f_t = ζ + t g | shares T_c of ζ if T_c < ½log N₀ | yes in the window with ζ's Λ | if T_c(ζ) = ∞ there is no F; if it existed, f_t shares F, ρ, b, h and every P block; it differs only in Q (primes outside the window, which f_t does not have). Requires (N′): the residue separates only through the exterior blocks |
| b_θ (sieve) | — | yes as a weight | b_θ ≥ 0, ≤ Λ: if the chain closed with upper bounds, b_θ would refute it (W-sieve); the chain does not use bounds, it uses the identity → not directly applicable |

Conclusion of §3: the only property of ζ that the chain can use is
Λ = μ * log over ℤ (plus Z_N). That formally separates it from DH, deletion,
κ, Type I and (with the ordinary comb) from DMV and Λχ₂; **but the phase itself
proves (868, 869, 874, 894 §4, 892 §4) that this input does not determine the
residue**. Hence (R170-RES) is not a proved S4 separator: either it is
false for ζ (undecidable: there is no contact), or its truth comes from something
not identified. Against S1/S5: it is a jet at contact (S1 violated:
W5) and its useful version is "∀T, no window makes contact" (S5 violated: E1).

## 4. Verdict and test case

**Verdict: W12 over W5, with E1 closure. It is not a genuine
open inequality.** What phase 170 truly reduced: D ⟸ [contact ⟹ 𝔑_pol(F) = 0
∧ covariant identification ∧ stabilization in N ∧ sign of σΔ], each
piece OPEN and the last one REFUTED in the abstract. Net gain: a finite,
exact ledger (PROVED) of the polar port; no reduction of D.

Cheap case. In ζ there is none: S = {∞,2}, T < ½log3 has λ_T > 0
(Thm C(½log3)), the admissible set is empty and (R170-RES) is vacuous.
The informative test is **negatively directed**: take a falsifier with
contact at small T and atomic weight (Type I curve s₂δ_{log2}+s₃δ_{log3}
on s₂^c, or deletion), compute F, ρ, h and 𝔑_pol(F) with M = N = ⌈e^{2T}⌉.
If 𝔑_pol(F) = 0 there, the equation is blind (W3) and the route dies; if ≠ 0,
one must show that the only term that changes is the one depending on
Λ*1 = log — which 868 already rules out for the linear parts. Auditor's
prediction: 𝔑_pol ≠ 0 generically in every model (also in a hypothetical ζ
with contact), because it is a linear scalar in the free exterior datum (894 §4).

Phase 183 tools. E_S = Son + R (R183_018), relative bound 0 of the
prime term (R183_023) and E′ (R183_029) are statements about the **form**
in the semilocal space (positivity / finite index), not about contact
vectors. They apply to the P (interior) part of the residue and to λ_T, but the
residue lives in the exterior blocks Q and in the face t + log N, which 183 does
not treat. Useful application: if 183 gives finite index in S = {∞,2}, the
contact radical is finite-dimensional and (R170-RES) becomes a finite
system; that does not give it a sign. There is no direct transfer.

## For the audit

1. Is it unfair to call it E1? Strictly, (R170-RES) is *weaker* than RH
   (vacuous under RH); what is E1 is the conjunction with the rest of the
   chain, which amounts to "there is no contact." Precise label: OPEN-vacuous;
   route NO-GO [W12 + W5], E1 closure.
2. I claim 884–899 are generic in the weights; verified by reading
   898 (1.3) and 899 §§1–4 (they only use L_M = Σ a_r τ_{log r} with finite a_r).
   If any of them uses Λ = μ*log in a hidden way, it changes the DH/deletion row.
3. I did not compute 𝔑_pol in any falsifier; the "value not computed"
   rows are logical, not numerical.
4. The identification of b_ε and of H_T was taken from R170_854/856 without rederiving it.
5. R170_808 (A) is correct and useful as a construction no-go, but it is
   independent of the final residue.

## Note (R184_091)

* Vacuity under RH: it does not follow from strict λ_T>0 (RH only gives W_T ≥ 0). Correct argument: if W_T(F)=0, Φ_F vanishes at all the zeros, whose density ~log γ exceeds that of any function of finite exponential type, so F=0.
* (R170-RES) needs quantifiers over N, M; distinguish (5.3) from (7.2) of R170_899; the falsifier table is ARGUED (without computation).
