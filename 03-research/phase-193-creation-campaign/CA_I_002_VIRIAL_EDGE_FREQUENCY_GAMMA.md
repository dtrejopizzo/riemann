# CA_I_002 — Virial/Pohozaev, the collar boundary layer, frequency functions, Γ-convergence and concentration–compactness (seeds I4, I9, I5, I7, I8)

Phase 193. Pen and paper; **no numerics**. **No sign contact. No negative value for ζ.**
Notation as CA_I_001 §0; 𝒱_T = virial of R165_202 1.4; T_n = ½log n.

## 1. Seed I4: exactly which virial statement Davenport–Heilbronn falsifies (retry, sharpened)
**Proposition 1.1 (the identities are B″; PROVED from R165_202 1.4).** For every real comb a (any signs) and every unit F ∈ 𝒫_T ∩ (REG):
d/dT 𝔞_T(U_Tf) = −𝒱^a_T(F)/T with 𝒱^a_T(F) = (1/2π)∫τm′(τ)|F̂|² − Σ v^a_n log n·c_F′(log n) + 𝒯_T(F) (Tate term).
It is linear in a; it holds verbatim for the Davenport–Heilbronn comb (signed coefficients, same Γ-factor and FE) and for every O_i.
*Proof.* R165_202 1.4 differentiates term by term; no sign of a is used. ∎
**Proposition 1.2 (what DH kills; PROVED modulo one ARGUED input).** The three sign statements that have been drawn from the virial are:
(V1) 𝒱_T(h*_T) ≥ 0 — true for every comb (λ_A nonincreasing, nested windows, lem:monoT); content-free.
(V2) Hadamard principle: 𝒱_T(h*) = 0 unless h* has an edge singularity — class-generic (R165_202 1.5, ARGUED there), holds for DH.
(V3) relative bound 𝒱_T(h*_T) ≤ c(T)Tλ_A(T) with c ∈ L¹_loc (Grönwall) — equivalent to λ_A > 0 on the range (R186_111 α, PROVED) and
**falsified by DH**: at a transversal zero crossing T_c of λ_A^{DH} with 𝒱(T_c) > 0 one has c ≥ 𝒱/(Tλ_A) ∉ L¹ (ARGUED: transversality of the DH
crossing is the reading of the index entry F-DH; not reproved here).
So DH does not falsify the identity; it falsifies V3, which is the only sign-bearing virial statement, and V3 is REF-D on finite ranges.
**Pohozaev with the Tate constraint.** The projected commutator ⟨[L_T, iM_x]h*, h*⟩ = 0 reduces to the Tate projection defect (P124_007, exact
cancellation). Nothing new: retry, NO-GO.

## 2. Seed I9: the collar boundary layer (retry made precise)
**Proposition 2.1 (entry is first order in the edge, linear in v_n; PROVED from R165_202 1.2).** For T slightly above T_n, the new term is
q_n(F) = −v_n⟨a, b⟩, a, b the two edge strips of width ε = 2T − log n; in the even sector q_n = −v_n⟨a, Ra⟩ (R reflection of the strip).
Hence the right derivative of λ_A at T_n has the form D⁺λ_A(T_n) = −v_n·Φ(h*_{T_n}) + (archimedean/Tate virial), where Φ is a quadratic
functional of the **edge trace** of h* (for continuous h*: Φ ∝ h*(T)h*(−T), sign = parity, R186_038 α.2).
**Proposition 2.2 (any edge-layer property enters only one-sidedly; PROVED from SPEC_A Lemma S).** Let e be the edge component of h*_{T_{j+1}} in the
Schur splitting. Lemma S(iv) gives λ_𝔰 ≤ λ_A/‖e‖², Lemma S(i) gives λ_A ≥ 0 ⟺ 𝔰_j ⪰ 0. A qualitative lower bound ‖e‖ ≥ c (boundary-layer
non-degeneracy) therefore bounds the Schur margin **from above** by λ_A/c²; a lower bound on λ_A needs 𝔰_j ⪰ 0, the target (REF-D).
**Proposition 2.3 (edge properties are class-generic; PROVED).** Parity, edge non-vanishing at strict decrease, the strip structure of q_n and the
reflection sign hold for every symbol form with even symbol and any comb; the quartet forms of O7 (Markov-breaking but symbol-type) have all of
them. A qualitative edge property is either one of these (dies at O7) or a numerical edge exponent (R186_048, SPEC_A: ‖e_min‖² ≍ ε^{2a+1},
NUMÉRICO quoted), i.e. a window observable (W-pat).
+/· reading: the entry instants T_n = ½log n (·) meet the additive strip translation by log n (+) exactly here — this is the PRINCIPIO RECTOR locus
in the T-flow — but the coupling is linear in v_n (Prop 2.1), so by H-anatomy the non-linearity must again come from h* (REF-D).

## 3. Seed I5: Almgren-type frequency (NO-GO for bounded frequency; PROVED given CITED thm:M(b))
Define N(T) := −T·d log λ_A/dT = 𝒱_T(h*)/λ_A (where λ_A > 0, (REG)). An Almgren monotonicity "N nondecreasing and bounded on [T₀,∞)" would give
λ_A(T) ≥ λ_A(T₀)(T₀/T)^{N_∞} — polynomial decay. Paper 48 thm:M(b) (CITED via R186_111: λ_A(T) ≤ exp(−e^{(2−ε)T}) for large T) forces
∫^T N(s)ds/s ≥ e^{(2−ε)T}: **the frequency is unbounded, growing at least like e^{(2−ε)T}**. Any monotonicity formula must therefore carry a
super-exponential weight, and on finite ranges "N ∈ L¹(ds/s)" ⟺ λ_A > 0 (R186_111 α). A frequency law on a bounded range is W-fam (thm:famblind);
on unbounded ranges it is a two-sided asymptotic law (not excluded, rem:bar-fam) but with relative precision e^{−e^{2T}}: (R)(6). DISCARD.

## 4. Seed I7: Γ-convergence (PROVED inadequacy)
Rescale F = T^{−1/2}f(·/T), f ∈ L²(−1,1). The rescaled forms Q_T(f) = 𝔞_T(F) have arch symbol m(s/T) = log T + O(1) + log|s|-type; after
subtracting log T and dividing, the comb part Σ v_n c_f(log n/T) tends (prime number theorem, density only) to a smooth kernel. Any Γ-limit
determines min Q_T up to o(1) **absolute** error, while 0 < λ_A ≤ exp(−e^{(2−ε)T}) (CITED). The Γ-limit can at most identify lim λ_A = 0; it is
blind at the scale (R)(6) requires and uses only the density of Λ ((R)(7)). DISCARD.

## 5. Seed I8: concentration–compactness (PROVED inadequacy)
L := inf_T λ_A(T) = inf over compactly supported F ∈ 𝒫 (all T) of 𝔞(F)/‖F‖² (lem:monoT). For quadratic problems I(α) := inf{𝔞(F) : ‖F‖² = α} = αL
is linear, so the strict subadditivity I(α) < I(β) + I(α − β) never holds; Lions' dichotomy is always admissible and the method gives no
compactness and no sign. Under the target, minimizing sequences for L = 0 vanish (spread over growing windows) since no compactly supported F
attains 0 with all windows positive — a consequence, not a tool. DISCARD.

## 6. Seed I6: unique continuation (one line)
ĥ* is entire of exponential type 2T (Paley–Wiener), so h* cannot vanish on an open subset of the frequency line and Carleman-type unique
continuation is automatic in τ; in t, h* may vanish on subintervals only if λ_A is locally constant in T (R165_202 1.7). Class-generic; no sign.

## 7. Self-review
1. Prop 1.2(V3) DH falsification relies on a transversal DH crossing: ARGUED, flagged.
2. Prop 2.2 is a restatement of Lemma S; its new content is only the one-sidedness of edge information.
3. §3 uses thm:M(b) of Paper 48 (proved in record, not refereed): CITED with that caveat.
4. Nothing here is non-linear in Λ except through h*. **Verdict:** I4, I9 developed: NO-GO / REF-D; I5, I6, I7, I8 DISCARD.
