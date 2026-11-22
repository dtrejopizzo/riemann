# AUDIT_197_2 — audit of BARRIER_D1_001 and BARRIER_D2_001 (phase 197)

Checked against Paper 46 main.tex (l.3093 v_n(a)=2a(n)/√n; eq:Aform l.402; lem:degen
l.3249; lem:contA l.575; cor:margin1 l.3516; thm:log5A l.4627; prop:wit-sens l.7087; sec:spec l.8942), AUDIT_197_HOSTILE, and the
index (N_010 §3 / 06_ R4, R162_2801, R163_1001c, INV_P/INV_Q, AUDIT_193 #101, ES-18, P34-2/5, L20).

## 0. Global normalisation error (both memos; inherited from BARRIER_001 §1)
Paper 46 uses **v_n(a)=2a(n)/√n** (l.3093; prop:wit-sens). BARRIER_001, D1, D2 use a(n)/√n. Hence the correct objects are
w_T=(2c_{F⋆}(log n)/√n)_n and d_v(a,b)=Σ 2|a(n)−b(n)|/√n (Lipschitz constant 2 in the a(n)/√n metric). Every qualitative statement
survives; every explicit constant changes (Cor 3: W_p doubles, the sup doubles; D2 Thm 2(ii): transferred margin is
λ_A(a_0) − 2Σ|a_0(n)−Λ(n)|/√n). FIX REQUIRED before any integration in Paper 46.

## 1. BARRIER_D1_001
- **Prop 1** — PROVED given Hamburger (CITED), with hypotheses to be stated: absolute convergence in some half-plane, (s−1)D(s)
  entire of finite order, FE with Γ_ℝ on the *same* series. The tangent argument needs the curve to stay in H (finite order
  uniformly along the curve is not needed: only k∈H, and H is linear). Fine. f_a must be a Dirichlet series with an abscissa
  of absolute convergence: requires a growth hypothesis on a (e.g. a(n)=O(n^C)); add it.
- **Thm 2** — PROVED (Kronecker on log p, torus means; M R²=1 since R² is a power series with constant term 1). NUMÉRICO check
  (torus quadrature, 2·10⁵ / 1500² nodes): (p,α)=(2,0.5): 0.0714286 vs formula 0.0714286; (3,−0.7): 0.5756972 both; (2,1.3):
  0.1451613 both; two primes (2,0.4),(3,−0.5): 0.5869565 both. Agreement to ≥10 digits. Minor: a_P asymptotic should read
  ½((6e^γ/π²)log P(1+o(1)) − 1).
- **Cor 3** — PROVED (Cauchy–Schwarz on the ellipsoid Σt_p²/(2(p−1))≤ε), modulo §0 factor 2.
- **Thm 4** — the inequality is PROVED, but the word "symmetric" is wrong and the hypotheses are far too strong. What is used is
  only that {Δ≤ε} contains points Λ+u(st*) with s>0 (w-positive side). A C² (or analytic) Δ with strict minimum is *not* even
  beyond second order (odd cubic terms exist, e.g. Thm 2's t³/(p−1)²); what is true is that an analytic ≥0 function of one
  variable has even leading order, so both sides enter at the same scale. But even that is irrelevant: the half-space test is
  first-order, so **any Δ continuous along one w-positive curve with Δ(Λ)=0** gives π_N S_ε ∩ {⟨·,w_T⟩>0} ≠ ∅ and hence (lem:degen)
  λ_A(T;Λ) ≥ s(ε)⟨Du(0)t*,w_T⟩(1+o(1)) with s(ε)=sup{s: Δ(u(s't*))≤ε, s'≤s}>0. Correct general statement (PROVED): *continuity of
  Δ at Λ along a w-positive curve suffices*; analyticity only fixes s(ε)≍ε^{1/2m}.
- **Label of Thm 4: "NO-GO" overstated.** It is not an impossibility: it shows the premise carries no sign and that a uniform
  method proves the quantitatively stronger λ_A(T;Λ) ≥ s(ε)·κ>0 (REF-D⁺), which tends to WP_T as ε→0. Relabel:
  "PROVED reduction: continuous FE-defect premises are REF-D⁺ (sign-free)"; CONDITIONAL on w_T≠0 (lem:degen degenerate case).
- Separation of cΛ, Beurling, Ξ_Q: ARGUED, as labelled. §7(2) tail-inf on E_N: PROVED (each factor ≥1).

## 2. BARRIER_D2_001
- **Lipschitz lemma** — PROVED (= prop:wit-sens first sentence, which already exists in Paper 46: CITED, not new), constant 2 per §0.
  Concavity of a↦λ_A = lem:degen (CITED).
- **Thm 1** — (a),(b),(c) PROVED; (b) sufficiency correct (CΔ ≥ (d_v−μ)_+ ≥ d_v−μ). Reading "defect contributes no sign" correct.
- **Thm 2** — (i),(iii),(iv) PROVED. (ii) bound PROVED; **sharpness proof wrong as written**: g(x)=min_s[φ(s)+d_v(x,a_s)] has
  g(Λ)=inf(φ+d_v), not the sup bound. Correct witness: g(x)=max_{s≤s₀}[φ(s)−d_v(x,a_s)] (1-Lipschitz, ≥φ on the path, g(Λ)=sup).
  Lipschitz-class sharpness PROVED with this g; concave-class sharpness ARGUED (g is not concave). Fix the text.
- **Thm 3(a)** — injectivity PROVED by the Bohr-coefficient argument (Σc_p h_p real-analytic in t on σ=¾, vanishing on a segment ⇒
  on the line ⇒ the frequency −log p coefficient −c_p·p^{−3/4}=0). Drop the "periods" ARGUED variant. (Rig_C) on 𝓔𝓟_Q PROVED
  (finite-dim injective linear map vs linear d_v).
- **Thm 3(b)** — PROVED for T≤½log5 (thm:log5A gives λ_A≥2.5·10⁻¹² there; μ>0, so (Rig_C) ⇒ (I_T)). Correct but content-free for the
  sign (sign comes from thm:log5A). (c) tails OPEN, sign-free: correct label.
- NO-GO 𝒦_D2 (defect barrier + continuation): ACCEPTED as a PROVED reduction (every bit of sign sits at Λ), with §0 constants.
  Novelty vs N_010 §3 / AUDIT_193 #101: genuine generalisation (all Δ, all paths), as claimed.

## 3. The two residues
- **(R1) "one-sided FE defect at Λ, not a sup of linear forms" — ILL-POSED as specified; COLLAPSES.** D1 §5's own example
  (Δ(Λ+su) ≥ cs for s>0) is continuous, so S_ε still contains Λ+su for 0<s≤ε/c and the corrected Thm 4 applies (REF-D⁺ with
  s(ε)≍ε). Escaping requires S_ε ∩ {⟨·−Λ,w_T⟩>λ_A(T;Λ)} = ∅ for the given ε, i.e. Δ bounded below on the w-positive side near Λ
  — a discontinuity at Λ, i.e. a half-space/cone premise in direction w_T, which is a dual-certificate premise (BARRIER_001 Thm 3(ii))
  or REF-D. No well-posed residue survives: **NO-GO (class: FE-defect premises, continuous or not)**, with the dichotomy
  continuous ⇒ REF-D⁺, discontinuous at Λ in direction w_T ⇒ cone/certificate. Record as closed.
- **(R2) "openness at crossings: no kernel of 𝔞_T^{(a_s)} for s<1" — RESTATEMENT; near-retry.** Along a d_v-continuous path from
  a_0 with λ_A(a_0)>0, "no kernel (bottom eigenvalue ≠0) for s<1" ⟺ λ_A(a_s)>0 ∀s<1 (continuity, Lipschitz) ⟹ μ≥0 (lem:contA-type
  limit). This is exactly AUDIT_193 #101 (no-crossing = positivity) moved to comb space; Pontryagin/Kreĭn index arguments are
  ES-18/P34-2/P34-5 (DEAD/CIRCULAR/OPEN), L20/thm:KEPdich (REF-D). Also unposed: no path with a provably positive a_0 at T≥0.60 is
  named (λ_A(T;0)=laminfP(T) is not known ≥0 there; a_P likewise). Well-posed only if a *structural* kernel obstruction is given
  (an invariant of ker 𝔞_T^{(a_s)} incompatible with s<1 that is not the sign of λ_A); none proposed. Status: OPEN-as-statement,
  REF-D-equivalent, not to be launched without a new written reason.

## 4. Verdict
D1: Prop 1, Thm 2 (NUMÉRICO-confirmed), Cor 3 PROVED; Thm 4 PROVED in a stronger, simpler form (continuity suffices), relabelled
as REF-D⁺ reduction, CONDITIONAL on w_T≠0. D2: PROVED reduction modulo the factor 2 and the Thm 2(ii) witness fix. Residues R1
closed (collapses into REF-D⁺ / certificate), R2 = #101 restatement. No sign. Row D: OPEN. No grid symbol changes.
