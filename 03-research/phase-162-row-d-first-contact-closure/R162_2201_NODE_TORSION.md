# R162_2201 — Round 22, front A, cell 8B×5C: node tests against the torsion cocycle — **NO-GO (PROVED), one new exact structure**

Mechanism A. Pure mathematics; no numerics. No sign is claimed, no label moves, Gate 1 / OS-1 stay OPEN.
Inputs (read first, rule): grid/R162_2300_MASTER_GRID.md §0, cells 8B and 5C, §3 walls, §7 spec S1–S12;
R160_X_C1 (B, R, FC, G, χ, OS-1/OS-3); R162_1001 (Φ_a, cocycle (3.1), Prop 3.2, Thm 5.1) with the R162_1190 fixes
(Λχ₂ fails (3.1) at every p with χ(p)≠1; factor 2 and k=0 in Prop 3.2; the solenoid sentence is a remark);
R162_1101 (Thm 1.1 duality, Thm 2.2 atom-0 localisation, §3.3 the cocycle is tautological on tests, the correction that
separable tests escape Theorem M); R162_1202 Prop H (atom placement depends on the kernel; the residue value is invariant);
R162_2001/2190/2101 (the two-atom Type I curve, s₂^c = 0.9997678, T_c < ½log 4).

Conventions. Complete form W = W_{T_c}, F a real parity-definite real-rooted witness (R160_X_C1 FC(ii)), nodes
x ∈ 𝒳 := real zeros of F̂ (simple ones used below), node tests Ĥ_x = F̂/(z−x), d_x = W(H_x) ≥ 0,
w_x = d_x/|F̂′(x)|² (Thm G). X := e^{2T_c}. Φ_a = Σ_{d≥2} a(d)(ν_d − Leb), Φ̂_a(k) = (a*1)(|k|).

## 0. Grid position and corpus check (§0 rule)

Cell 8B (node tests are linear in F) × 5C (torsion atoms, a functional beyond linear). Nearest routes: 8B residual
"R160_X_C1 rigid Blaschke witness" and 5C residual "discontinuous functional separating ℤ from Beurling and 1 from χ₂
(residue of R162_903)", whose candidate object is Φ_Λ (R162_1001) and whose NO-GOs are R162_1101 (atom 0) and R162_1202
Prop H. Walls this memo must name: W4 (F2) and W5 (F1) for 8B; W1 (E1) for the Kreĭn reading of Thm G.
Grep over phases 155–162 for "node test", "Gauss-node", "node measure", "θ′", "Z′/Z", "Hardy Z" with "torsion" or "Φ_Λ":
no file pairs the node data of R160_X_C1 with Φ_Λ. The Kreĭn/determinacy reading of the node measure is on record:
P46 def:KEP / thm:KEP3 and phase 155 round 5 ("RH ⟺ Kreĭn indeterminacy"). §3 uses that record and does not redo it.

## 1. Failing lines, stated first (mandatory)

| model | has a Gauss-node witness? | line of this memo that fails / changes | consequence |
|---|---|---|---|
| **Λχ₂** (χ₂ real, contact n=2, T_c ∈ [½log2, 0.38]) | yes (R160_X_C1 χ) | §2 Lemma N0: nothing fails (X = e^{2T_c} < 2.14, so band-limited pairings read only Φ̂(2) = −log 2 instead of log 2; the truncated cocycle fails at p=2, k=1). Thm N1: the cocycle step is replaced by the **twisted** cocycle ℒ_pΦ^χ − χ(p)Φ^χ = χ(p) log p·Σ_kχ(k)e(kx), and the Dirichlet series is −L′/L(s,χ₂). Every later step holds verbatim with θ_χ, Z_χ (Z_χ is real and even because χ₂ is real) | N1 gives Σ w_x\|Ĝ(x)\|²θ_χ′(x) for Λχ₂ exactly as it gives Σ w_x\|Ĝ(x)\|²θ′(x) for ζ. So the combination "quadrature + cocycle" cannot separate them: **S4 fails at the FE step (N1(c))**. |
| **two-atom Type I curve** s₂δ_{log2}+s₃δ_{log3}, s₂^c = 0.9997678 | yes (a Type I first contact, R162_2001/2190) | N0: in the window (T_c < ½log 4) the truncated cocycle holds iff s₂ = s₃ = 1, and then the model *is* ζ on the window. At s₂^c it fails at p=2 by (1−s₂^c)·log 2 ≈ 1.6·10⁻⁴, a continuous defect. N1: the Dirichlet series 2^{-s}s₂log2 + 3^{-s}s₃log3 is entire and has no FE, so step (c) (reflection) fails: the ℝ-part is Σ d_x\|c_x\|²(s₂log2·2^{-½}cos(x log2)+s₃log3·3^{-½}cos(x log3)), with no sign and no contradiction | the window-level data vary continuously in s₂ through the Type I point. Any argument using only the window must also be continuous there, so it cannot exclude ζ's witness while allowing this curve's (S8 / W3). |
| Beurling DMV | yes (record) | Φ_{Λ_B} is undefined on ℝ/ℤ, but N1 has a Beurling version with −ζ_B′/ζ_B, with no circle | same as for Λχ₂ once ζ_B has an FE (DMV systems do not): step (c) fails, and the result has no sign |
| ζ | hypothetical (¬RH) | nothing fails, and nothing follows (N1(d), N3) | — |

## 2. The honest check: node tests are Paley–Wiener, and the obstruction applies

**Lemma N0 (band-limitation; PROVED).** Take any G built from node data by finitely many of these operations: node
tests H_x; finite linear combinations; finite products Ĥ_{x_1}⋯Ĥ_{x_k}·Ĥ^#_{y_1}⋯ (type ≤ (k+l)T_c); finite quotients
F̂/Π_{i≤k}(z−x_i); products with polynomials, if the result stays in L²(ℝ). Then Ĝ ∈ PW_{T′} with T′ ≤ (number of F̂
factors)·T_c. Hence every pairing of Φ_Λ with a window quantity of G (c_G, w_G, the Weil form W_{T′}(G,·), the
Hilbert-law integrand σ|F̂|²/(τ−x)) reads Φ_Λ only through Φ̂_Λ(k) = log k, k ≤ e^{2T′}. The same holds for infinite
quotients F̂/Π_{x∈S}(z−x) that stay in L²(ℝ).
*Proof.* Entire of exponential type ≤ T′ and L² on ℝ ⇒ PW_{T′} (Paley–Wiener, CITED). For infinite S, the quotient
has the indicator of a Cartwright-class function with zero density T_c/π − dens S (Cartwright–Levinson, CITED). So it
is either of type ≤ T_c and L², hence PW, or not L² on ℝ (S = 𝒳 gives Ce^{bz}z^m by Hadamard). Fourier support in
[−2T′,2T′] then gives R162_1001 Thm 5.1 verbatim. The Hilbert transform preserves Fourier support. ∎

*Honest nuance.* A band-limited pairing does **touch** the atoms r/d with r≠0 when d ≤ e^{2T′}, since
⟨ν_d − Leb, h⟩ = (1/d)Σ_r h(r/d) − ∫h. But its value is a fixed linear combination of Φ̂(k) for k ≤ e^{2T′}, which is
the comb data Λ(n), n ≤ e^{2T′}. So the discontinuity of Φ_Λ in the support positions stays invisible. In
R162_1101 Thm 1.1 terms, u_h is supported in [1, e^{2T′}]. **For the node tests themselves (T′ = T_c) the obstruction
applies in full:** in the window the cocycle for all p is exactly "the comb equals ζ's comb up to X" (R162_1101 §3.3
truncated). Any argument from node tests plus the window cocycle is therefore an argument about W_{T_c}^ζ alone, i.e.
OS-1 (E1). The two-atom row shows this. At s₂ = s₃ = 1 and T < ½log 4 the model is ζ; at s₂^c the defect is
continuous (§1).

## 3. The minimal non-band-limited node object and its atomic pairing

The node data (𝒳, d_x) has no compactly supported Fourier transform: μ_F := Σ_x w_xδ_x is a discrete measure with
infinite support. Lemma N0 says that anything of exponential type falls back into the window. So the smallest
non-band-limited use is **separable** in the sense of R162_1101 §5: an F-free kernel of infinite degree, evaluated on
finitely many node data. The canonical choice is the one that reads Λ on every atom.

**Theorem N1 (the node-diagonal torsion pairing; PROVED).** Let G = Σ_{x∈S} c_xH_x (S ⊂ 𝒳 finite, simple nodes). Set
q_x := d_x|c_x|² = w_x|Ĝ(x)|² ≥ 0, so W(G) = Σ_S q_x (Thm G(d)). For an arithmetic a with a(1)=0 and Re s > 1, define
  𝒜_a(s;G) := Σ_{n≥2} a(n) n^{-s} Σ_{x∈S} q_x n^{-ix} = ⟨Φ_a, g_{s,G}⟩,  ĝ_{s,G}(k) := ½Σ_{j≥1}μ(j)·u(|k|j),
  u(n) := 2n^{-s}Σ_x q_x n^{-ix}.
(a) *Atomic.* u has infinite support, so g_{s,G} is not band-limited and ⟨ν_d, g_{s,G}⟩ reads every torsion atom r/d
(R162_1101 Thm 1.1).
(b) *The cocycle for all p gives exactly the log-derivative.* (3.1) for all p ⟺ a = Λ (R162_1001 Thm 3.1b) ⟺
𝒜_a(s;G) = Σ_{x∈S} q_x(−ζ′/ζ)(s+ix), continued meromorphically in s.
(c) *Reflection erases the atoms.* Suppose G is real and no node in S is the ordinate of a zero of ζ on the line. Then at s = ½,
  𝒜_Λ(½;G) = Σ_{x∈S} q_x θ′(x),
where θ is the Riemann–Siegel theta function. The Euler/zero part, i Σ q_x Z′(x)/Z(x), cancels identically.
(d) *Class-level.* (a)–(c) hold for every finite S ⊂ ℝ and every weights q_x ≥ 0 with q_{−x} = q_x. They use neither
λ = 0, nor W, nor the orthogonality of the H_x.
*Proof.* (a) is Thm 1.1 of R162_1101. (b): Σ Λ(n)n^{-s-ix} = −ζ′/ζ(s+ix). The x-sum is finite, so the continuation is
termwise. (c): from ζ(½+it) = e^{−iθ(t)}Z(t) with Z real, i(ζ′/ζ)(½+it) = −iθ′(t) + Z′(t)/Z(t), so
−ζ′/ζ(½+ix) = θ′(x) + iZ′(x)/Z(x). Z is even, so Z′/Z is odd; θ is odd, so θ′ is even. For real F parity-definite, 𝒳 = −𝒳.
The relation (ιH_x)^ = ∓Ĥ_{−x} and the ι-invariance of W give d_{−x} = d_x. |F̂′(−x)| = |F̂′(x)|, and for real G,
Ĝ(−x) = conj Ĝ(x). Hence q_{−x} = q_x. With S closed under x ↦ −x (which we may assume, since q vanishes off supp c),
the odd part sums to 0. (d): only real nodes and even weights were used. ∎

*Reading.* The analogue of R162_1101 Thm 2.2 holds on the critical line. There the trivial-zero inversion
Li_{−2m}(w) + Li_{−2m}(1/w) = 0 (the FE at the Gamma lattice) moves the pole onto atom 0. Here the FE on the line
(ξ real ⟺ Re ξ′/ξ = 0) moves the atomic pairing onto θ′. θ′ is purely archimedean and Λ-free, and its twisted analogue
θ_χ′ serves Λχ₂. The Euler content survives only in iΣq_xZ′/Z(x), and the node symmetry that Thm G requires kills that
term. As in R162_1202 Prop H, *where* the atoms sit is irrelevant. The invariant is the Dirichlet series, and the FE
reduces it to archimedean data at the one point where the node data meets the window form (Plancherel on ℝ, s = ½). At
Re s > ½, s ≠ ½, 𝒜_Λ(s;G) is a finite combination of values of −ζ′/ζ at s+ix. That is a statement about ζ, whose only F
input is the finite list (x, q_x) (Riesz-type collapse, R162_1101 Thm 5.1).

**Proposition N2 (the node measure as the canonical non-band-limited object; PARTIAL = E1).** Assume OS-3 (the node
span is dense in 𝒟_{T_c} in the form norm). Then μ_F is a positive measure whose pairing with |Ĝ|² equals ζ's window
symbol (σ_{T_c}/2π)dτ + polar for all Ĝ ∈ PW_{T_c}. At λ = 0 it is the **unique** positive such extension (the
determinate case of P46 def:KEP, thm:KEP3). Its Fourier transform off [−2T_c, 2T_c] is the non-band-limited part.
Comparing it on the log lattice {log n : n > X} with ζ's zero side Σ_ρ δ_{γ_ρ} (lem:roughEF) means comparing the
unique positive extension with ζ's (non-positive, under ¬RH) zero distribution. That comparison is the Kreĭn-indeterminacy
form of RH (phase 155 round 5). Note that μ̌_F(log n) for n > X is *not* forced to equal −Λ(n)/√n. μ_F is determined by
the window alone, so the cocycle beyond X places no condition on it.
*Status.* The quadrature on the span is PROVED (Thm G); density is OS-3 (OPEN); the reading is **EQUIV (E1)**. The de
Branges function E of the chain at T_c carries the same data: μ_F = Σ δ_x/K(x,x) is the orthogonal sampling measure of
the degenerate chain (R160_X_C1 Prop D). The Hilbert-law kernel is band-limited (Lemma N0). Neither is a smaller or a
different object.

## 4. The combination: quadrature (w_x ≥ 0) + cocycle for all p ⇒ contradiction for ζ?

**Theorem N3 (NO-GO; PROVED).** Let 𝔖 be the set of consequences drawn from (i) Thm G (w_x ≥ 0, orthogonality,
Hilbert law) and (ii) the cocycle (3.1) for all p, by pairing Φ_Λ with node-built tests. Every element of 𝔖 is one of:
(α) a window identity for W_{T_c}^ζ, involving Λ(n) for n ≤ X only (Lemma N0), so that any contradiction from it is
OS-1 = RH (E1);
(β) the identity 𝒜_Λ(½;G) = Σ q_xθ′(x) together with its off-line-s versions, which is Λ-free at s = ½ and has no F-content
beyond the finite list (x, q_x) elsewhere (Thm N1(c),(d));
(γ) the determinacy reading of μ_F (Prop N2), which is E1.
None of these is contradictory under ¬RH. Each has an exact analogue for Λχ₂, which does have a Gauss-node witness.
*Proof.* R162_1101 §3.3: the cocycle for all p is an identity on every test, equivalent to the F-free list
Φ̂_Λ(k) = log|k|. So F-information enters only through the node data. Band-limited node data give (α) by N0.
Non-band-limited data must be separable (N0: an F-built object of exponential type is PW), and the canonical separable
kernel gives (β) by N1. The remaining non-separable object is μ_F itself, which gives (γ). The Λχ₂ analogue follows by
the twisted cocycle of §1 and N1 with L(s,χ₂): the same three conclusions hold, and Λχ₂ has a witness (R160_X_C1 χ).
So no contradiction can follow for ζ unless an input is used that Λχ₂ violates *after* the FE step. The only such input
is "coefficient 1" (χ = 1), and N1(c) erases it. ∎

## 5. F1, F2, walls, spec

- **F1 (λ = 0 essential).** Fails. N1 holds for any real finite node set with even weights (N1(d)). λ = 0 enters only
  through Thm G, which is used in (α) and (γ) and is E1 there. The one genuinely λ = 0 phenomenon, KEP determinacy,
  is on record as ⟺ RH.
- **F2 (orientation).** Fails. q_x = d_x|c_x|² and μ_F are quadratic in the witness and fixed by the form W_{T_c}. They
  are invariant under F ↦ −F and do not contain the orientation of (PC). W4.
- **Walls.** W5 (N1(d)), W4 (F2), W1 (N2, and (α)), W3 at the use step (Λχ₂ and the Type I curve pass every line).
- **Spec.** S1 fails (λ = 0 is used only by E1-type steps); S3 fails; S4 fails at N1(c); S5 and S12 pass (no margin,
  no window gap, no finite zero set); S7: Euler enters only through −ζ′/ζ, after the resummation. That is the order
  S7 forbids, and it is why the FE erases it.

## 6. Verdict and residual

**NO-GO (PROVED).**
(1) Node tests, and their finite products and quotients, are Paley–Wiener. R162_1001 Thm 5.1 / R162_1101 applies in
full: they touch atoms r/d only for d ≤ e^{2T′}, and only through log k (Lemma N0).
(2) The minimal non-band-limited node object is the separable pairing 𝒜_Λ(s;G) = Σ q_x(−ζ′/ζ)(s+ix). It is genuinely
atomic, and the cocycle for all p is exactly what identifies its Dirichlet series (N1(a),(b)).
(3) At the central point the functional equation and the node symmetry reduce it to Σ w_x|Ĝ(x)|²θ′(x), which is
archimedean and Λ-free. The Euler/zero part iΣq_xZ′/Z vanishes by oddness (N1(c)). This is the critical-line twin of
R162_1101 Thm 2.2.
(4) The node measure μ_F is the determinate positive Kreĭn extension (N2, E1).
(5) Quadrature plus cocycle yields no contradiction for ζ. Λχ₂ runs through every line with the twisted cocycle, and
the Type I curve is continuous at the window level (N3).

**Residual (sharp, for 5C).** A closing torsion argument at a first contact needs a node-built kernel whose central
value is **not** symmetrised by x ↦ −x. That means a non-real or non-even node weighting, which Thm G does not
supply for a real witness. Equivalently, it must read Z′/Z at the nodes with a sign. Z′/Z changes sign between
consecutive zero ordinates, so this is a statement about interlacing of the nodes 𝒳 with ζ's ordinates, i.e. the
zero side (W12 / E1 unless new). Recorded as O2201.1, OPEN, not a route.

Add to R162_590 §1c: "node tests × torsion cocycle — R162_2201 — node tests are PW (N0); separable node pairing
Σq_x(−ζ′/ζ)(s+ix) is atomic but FE+node symmetry reduce it to Σw_x|Ĝ|²θ′ at s=½ (N1); μ_F = determinate Kreĭn
extension (E1) | F1, F2, S4 at FE step".

Files edited: this file and grid/R162_2300_part7.jsonl (append).
