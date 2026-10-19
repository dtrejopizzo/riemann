# CA_A_007 — Triage: homotopy/no-crossing (covered), boundary triples (coordinates), cross-place reflection positivity (NO-GO)

Phase 193. Pen and paper. CA_B_006/007 were read; nothing here duplicates them.

## 1. Homotopy / no-crossing seed (proposed in CA_A_006 §6) — ALREADY COVERED; withdrawn
Killing references:
- **N_012** (04_ line 178): the segment λ_t=(1−t)ρ_κ+tΛ from a positive comb; the target holds exactly when t_∞=1 (REF-D);
  "decomposition cannot give t₀" (06_ line 78). My path a_c is a reparametrised segment or broken line, so it is covered.
- **W5** (P124_004–010, R162_101/403–405): first variations / jets vanish at the contact. The crossing condition
  "λ=0 and ∂_cλ=0" is therefore automatically degenerate, and no barrier comes from first order.
- **lem:flowdet** (R186_045): the flow coefficient is dominated by h*²/λ_A, so the flow degenerates at the contact.
- **W-cont** (R186_048): continuation across prime births inherits λ_A(T_n); its regime shrinks from 25% to 4%.
- CA_B_006 Lemma B: λ is concave and L_T-Lipschitz in v. Concavity makes the segment value
  λ(v_t)≥(1−t)λ(v_0)+tλ(v^Λ), which is no help at t=1.
Verdict: no new content. The property "a no-crossing barrier along a positive-comb homotopy" stays where N_012/W5 put it.

## 2. Boundary triples for W_λ (index §G, P60-5, never attempted) — reduces to existing coordinates (PROVED reduction)
Set-up: S := the restriction of the window operator to P_T, which has deficiency 2 inside the operator of W_T on L²(I_T),
with defect directions e^{±t/2}|_{I_T} (the Tate moments A, B). A boundary triple for S* has a 2×2 Weyl function
M(λ)=[⟨(W_T−λ)^{−1}u_i,u_j⟩] (Nevanlinna; Derkach–Malamud, CITED), with u_± the Riesz representers of A and B.
**Prop 1 (PROVED, standard Kreĭn resolvent formula + Paper 47 thm:parityschur).** For λ below the bottom of W_T, the Kreĭn
formula gives λ_A>λ ⟺ M(λ) is of a fixed sign on the 2-dim defect. At λ=0 this is the parity Schur/polar-capacity
statement 𝔊_T of Paper 47 (thm:parityschur, prop:polarcap: λ_W>0 ⟺ λ_A>0 and 𝔊_T≻0).
So a boundary triple is a coordinate system for the exact Schur reduction already in the admissible list ("exact Schur
reductions … carry the whole margin"). It adds no ζ-specific property, and the Weyl function exists for every comb
(lem:shape-ident pattern). Status: covered as coordinates (B″). It is not an object of (R) by itself.
Note: a triple adapted to the *primitive* problem (e.g. defect from the window endpoints ±T rather than the Tate
moments) would give a different Weyl function. Its sign content is λ_A itself, i.e. REF-D (KEP Nevanlinna entries 394/640).

## 3. Cross-place reflection positivity (NG-E1 cross-place, never built) — NO-GO (PROVED)
Osterwalder–Schrader form: for a reflection Θf(t)=f(−t) and a translation-invariant kernel K, reflection positivity (RP)
means H_K(f):=∫∫_{(0,T)²}f(t)f(s)K(t+s)dtds ≥ 0 for every f supported on (0,T).
**Lemma 1 (Toeplitz split, PROVED).** For F=f+Θf with f on (0,T), the window form satisfies 𝔞_T(F)=2𝔞_T(f)+2H_K(f), where K is
the window kernel (archimedean part minus the comb Σ_n (v_n/2)(δ_{log n}+δ_{−log n})). So RP is the Hankel half of the
Toeplitz form. RP alone neither implies nor is implied by 𝔞_T≥0 on even tests.
**Theorem 2 (RP fails for every comb with an atom, PROVED).** Let K=K_c−Σ_n (v_n/2)δ_{±log n}, with K_c continuous on
(0,2T) and some v_{n0}>0, log n0<2T. Then H_K is not ≥0 on any (0,T) with T>½log n0.
*Proof.* Take f_ε=ε^{−1/2}1_{[a−ε/2,a+ε/2]}, a=½log n0, ‖f_ε‖₂=1. The continuous part gives |∫∫f_εf_εK_c(t+s)|≤ε·sup|K_c|→0.
The atom gives −(v_{n0}/2)∫f_ε(t)f_ε(log n0−t)dt = −(v_{n0}/2)·(1+O(0))→−v_{n0}/2, since f_ε is symmetric about a. The other
atoms contribute only when log n∈(2a−ε,2a+ε), which for small ε is only n0. ∎
This holds for every place combination: any cross-place sum of per-place kernels with a positive prime atom inherits the
failure, whatever the archimedean kernel. "Cross-place" cannot repair it, because the archimedean contribution is
continuous and is killed by concentration. It is not ζ-specific (it holds for every comb), and it is the RP analogue of
the phase-6-osterwalder-schrader-reflection falsification G_p(π/log p)<0.
**Corollary 3.** Cross-place OS reflection positivity of the window kernel is FALSE for ζ (and for every comb). That is a
false statement, not a sign for D. (Lemma 1 shows it is not equivalent to the target.) No negative value of λ_A is
implied: H_K is not 𝔞_T.
Check: RP with respect to the FE reflection x↦1/x on the multiplicative side is the FE symmetrization (L2_026:
void; NG-D4: commutes, does not anticommute). Covered.

## 4. Other §G items, one-line pre-screen
- **t-concavity of log|ξ(½+it)| (NG-D2):** a pointwise curvature statement on the line. Paper 47 Prop. shape-twist /
  clause (4): such statements are excluded unless holomorphy and order-one growth are used jointly, or the Euler product on
  the line, and O9 (rational twist) preserves the FE. ARGUED excluded as a stand-alone; not developed.
- **Rigged-space eigenvectors x^{b+iγ} (NG-C3):** these live on the zero side (eigenvectors indexed by γ), so clause (4)
  [zeros] applies unless the rigging is built from primes. ARGUED excluded in the zero-indexed form.
- **Condensed math / Quillen K-theory of Spec ℤ:** no form object proposed anywhere; nothing to pre-screen yet.

## 5. Result and moves
- Homotopy seed: covered (N_012, W5, flowdet, W-cont). No move.
- Boundary triples: index §G "never attempted" → covered as coordinates of thm:parityschur (PROVED reduction).
- Cross-place RP: NG-E1 cross-place "never built" → NO-GO (Theorem 2, PROVED): RP fails for every atomic comb, and RP is
  only the Hankel half of 𝔞_T.
- YES→NO: "a reflection-positivity structure (per place or cross-place) carries the window sign" → NO.
- No sign contact. No negative value for ζ.

## 6. Next seed (proposed): a K-theoretic / index object coupled to h*
Every exclusion in CA_A_001–007 is of one of two kinds: positivity that is blind to the comb (norms, RP, Parseval), or an
exact restatement. What is left is an **integer-valued invariant that is stable on the open ball of CA_B_006**. Example:
a spectral-flow or Maslov-type index of the family T↦(𝔞_T on P_T), or of v↦𝔞^{(v)}_T along a loop that uses Euler × FE
(not a segment). Such an index is locally constant, so it holds on the whole open ball (openness satisfied). Its value
could be computed from ζ-specific data at a degenerate endpoint (T→0 or T→½log2, where positivity is PROVED) and
propagated by local constancy. The obstacle to pre-screen first: the inertia NO-GO (n₋=∞ for T>½log2) and the Cayley
signed index (632) / NG-69 (gauge-robust signed index, DEAD, forcer absent).
