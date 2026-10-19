# INV_C_001 — h⁰ off the multiplicative diagonal: exact object, exact identity, decisive test (phase 194, track C)
 Pen and paper, no numerics. No negative value for ζ.
Definitions checked against P47: def:PD (l.622), def:W + eq:nuw (l.1179–1190), thm:Z (l.1194). 𝒫_T = {F even, supp ⊂ [−2T,2T], F̂(±i/2) = 0}.
Window form (linear in F = g∗g̃): W(F) = F̂(i/2)+F̂(−i/2) − Σ_{n≥2} v_n F(log n) + A_ℝ(F), v_n = 2Λ(n)n^{−1/2}, A_ℝ = C₀δ₀ + p.v. part with
density −K(|u|) (K the Γ_ℝ kernel of eq:nuw, K(u) ~ 1/(2u²)·… singular at 0).

## 0. Corpus / index check (done first)
- Index: P36-4 (two-variable W₂, OPEN, pair-correlation wall); G6C-R166_502 (Dirichlet square × Λ = μ∗log at identity level: REF-D, repeat of E70_11/12);
  G3A-R160_S2 §3.2 (per-window evaluation finer than Montgomery–Vaughan, OPEN-RESIDUE); NG-A3, NG-B8 (MV covariance, pair correlation: NO-GO);
  CA_M_001 Prop 1.1 (Arch − Near), Cor 3.2 (site arithmetic information-free), Prop 4.1 (m + 2Re ζ′/ζ = 0 on the line); INV_B_002 §4; AUDIT_194 D.1.
- "Farey / coprime-ratio fibre" and "Möbius normalisation of the pair count": not in the index, grid or crossword. New reason vs. R166_502: that route
  multiplied Dirichlet polynomials (product coordinate log(de)); here the object is the ratio (Toeplitz) count of INV_B_001, and the question is
  whether its *fibre structure over ℚ_{>0}* yields Λ with exact weights. Different object; the answer turns out to land in the same place (§3).

## 1. The exact object (DEFINITIONS + PROVED fibre lemma)
For a weight K: ℕ×ℕ → ℂ (finitely supported, or with a cutoff), the **pair form** is
  h⁰[K](F) := Σ_{m,n} K(m,n) (mn)^{−1/2} F(log(n/m)).
INV_B_001's h⁰_X is K = 1_{m,n≤X}; smooth version K_w = w(m/X)w(n/X), w ∈ C_c^∞[0,∞), w ≡ 1 near 0.
**Ratio fibration.** Every (m,n) is uniquely (bj, aj) with r = a/b, (a,b) = 1, j ≥ 1. Put
  κ_K(r) := (ab)^{−1/2} Σ_{j≥1} K(bj,aj)/j,   ρ_K := Σ_{r∈ℚ>0} κ_K(r) δ_{log r}.
**Lemma 1 (fibre lemma; PROVED).** h⁰[K](F) = ρ_K(F) = Σ_r κ_K(r) F(log r). (Regroup by r; (mn)^{−1/2} = (ab)^{−1/2}/j.)
So every pair form sees (m,n) only through the ratio r and the fibre mass κ_K(r). The additive structure of ℕ (the j-line, "m ≈ kn" at fixed
ratio) enters only through Σ_j K(bj,aj)/j: for the sharp cutoff it is H(X/max(a,b)) = log X − log max(a,b) + γ + O(max(a,b)/X).
**Multiplicative diagonal** 𝔇 := {1} ∪ {q^{±1}: q prime power}. **Off-diagonal form** h⁰_off[K] := ρ_K restricted to log(ℚ_{>0} ∖ 𝔇);
**diagonal form** h⁰_diag[K] := ρ_K restricted to log 𝔇. h⁰ = h⁰_off + h⁰_diag (PROVED, Lemma 1). Note h⁰_off is *not* a Gram form (AUDIT_194 D.1 warning
confirmed: removing fibres destroys Bochner positivity).

**Lemma 2 (Möbius normalisation = the coprime-ratio measure; PROVED).** For σ > 1 and F bounded with compact support,
  P_σ(F) := Σ_{(a,b)=1} (ab)^{−σ} F(log(a/b)) = ζ(2σ)^{−1} ∫ F̂(t) |ζ(σ+it)|² dt/2π.
*Proof.* Σ_{m,n}(mn)^{−σ}F(log n/m) = Σ_r (ab)^{−σ}F(log r)Σ_j j^{−2σ} = ζ(2σ)P_σ(F) (abs. conv.: a ≍ b in the window, Σ_b b·b^{−2σ} < ∞);
the left side is ∫F̂|ζ(σ+it)|²dt/2π by Parseval for Dirichlet series (F̂ ∈ L¹ for F ∈ C_c^2). ∎
This is the natural Möbius/inclusion–exclusion normalisation: the ℚ^×-invariant fibre weight. **In it every prime power ratio has weight
exactly 1 (times q^{−σ}), never Λ(q).** Same for the cutoff normalisation (weight H(X/q) ~ log X − log q). Since log q = k log p ≠ Λ(q) for k ≥ 2,
and since κ_K(q) for any K built from the lattice by cutoffs/Möbius is a function of the fibre mass, Λ(q) is obtained only by inserting it by hand.
(ARGUED for "any natural K"; PROVED for sharp cutoff, smooth cutoff and the ζ(2σ)-normalisation.)

**Lemma 3 (constant term of the smooth count on 𝒫_T; PROVED, standard contour shift, polar constants not evaluated).** For F ∈ 𝒫_T smooth and log X > 2T,
  h⁰[K_w](F) = X·∫F̂(t)|ŵ(½+it)|² dt/2π + ∫F̂(t)|ζ(½+it)|² dt/2π + c·(F̂′(i/2) − F̂′(−i/2)) + O_A(X^{−A}),
with ŵ the Mellin transform (single pole at 0, residue 1) and c universal (product of the residues of ζ and ŵ; independent of w).
*Proof sketch.* Σ_n n^{−1/2+it}w(n/X) = ζ(½−it) + ŵ(½+it)X^{½+it} + O(X^{−A}) (Mellin, shift left). Expand |·|²; the cross terms are
X^{½}∫F̂ ζ ŵ X^{∓it}: shift t to Im t = ∓A (F̂ entire of type 2T, rapid decay on horizontal lines): size X^{½−A}e^{2TA} → 0 since log X > 2T; the only
pole crossed is the double pole at t = ∓i/2 (ζ and ŵ together), residue F̂(∓i/2)(log X + c′_w) + c F̂′(∓i/2); F̂(∓i/2) = 0 on 𝒫_T. ∎
Corrections to INV_B_001/INV_B_002 (PROVED from the same computation): (i) the X-growth is X·(1/2π)∫F̂(t)dt/(¼+t²) = X∫F(u)e^{−|u|/2}du for the sharp
cutoff, which is **strictly positive** for F = g∗g̃ ≠ 0 and does **not** vanish on 𝒫_T; (ii) there is **no log X term** on 𝒫_T: the "log X·(weight 1 per
prime power)" of the coprime-ratio expansion is cancelled by the off-diagonal fibres (consistent with Lemma 2: ζ(2σ)^{−1} → 0 at σ = ½). So the
diagonal's log X cannot be isolated: h⁰_diag and h⁰_off separately carry divergent log X pieces that cancel.

## 2. Exact identities relating it to 𝔞_T
**Theorem 4 (no atomic realisation; PROVED).** There is no measure ρ supported on log ℚ_{>0} (in particular no h⁰[K], no h⁰_off[K] − h⁰_diag[K′]) with
ρ(F) = W(F) for all F ∈ 𝒫_T.
*Proof.* ρ − W would annihilate the even C_c^∞(−2T,2T) functions orthogonal to cosh(u/2) (𝒫_T contains them; F = g∗g̃ spans a dense set, CITED),
so ρ − W = c·cosh(u/2) as even distributions on (−2T,2T). The a.c. part of ρ − W on (0,2T) is +K(u), singular at 0, not a multiple of cosh. ∎
Hence any exact identity is a **limit** identity: off-diagonal atoms must converge weakly to the a.c. archimedean measure and the diagonal must be
exactly −Σ v_n δ_{±log n}. That is precisely the split W = (a.c. archimedean + polar) − (comb), i.e. CA_M_001 Prop 1.1 Arch − Near (Arch = α-part,
Near = comb Ξ part) on the full test class.
**Identity 5 (the only exact Λ-producing operation; PROVED for σ > 1).** With ϱ_σ(t) := |ζ(σ+it)|² = ζ(2σ)·(density of P_σ), Lemma 2 gives
  Σ_n 2Λ(n) n^{−σ} F(log n) = −∫ F̂(t) ∂_σ log ϱ_σ(t) dt/2π   (σ > 1).
Λ appears exactly, but through ∂_σ log of the h⁰ density: nonlinear in the pair count (INV_B_001 Step 3 wall, now an identity). The left side is entire
in σ (finite sum); continuing the right side to σ = ½ crosses the zeros and the pole — the difference is the explicit formula. At σ = ½ the a.c.
part is −∂_σ log ϱ = m(t) off ordinates (CA_M_001 Prop 4.1): zero slack, content in the singular (zero) part = thm:Z. **REF-D.**

## 3. Decisive test — verdict
- (Q3) Does h⁰ off the diagonal reduce to Arch − Near? **YES (PROVED via Theorem 4 + Lemma 1):** any pair-reweighted object is a measure on log ℚ;
  exactness forces the Arch/Near split; the positivity "lim (h⁰_off-limit) ≥ diagonal" is W ≥ 0 on 𝒫_T itself. **REF-D. Recorded.**
- (ℕ,+,·) content at m ≈ kn: by Lemma 1 the only additive imprint is the fibre mass (harmonic sum along the j-line → log max(a,b), cutoff-dependent)
  and the rate at which the coprime-ratio atoms near log k equidistribute (Farey-type). The target is a limit statement; it needs the limit, not a rate,
  and the limit is the archimedean density (W-independent of the cutoff, Lemma 3). Like CA_M_001 Cor 3.2: information-free for the sign. No new constraint.
- Λ with exact weights: obtainable only (a) by hand (row m = 1: h⁰[δ_{m,1}Λ(n)] = Σ Λ(n)n^{−1/2}F(log n), rank-one cross term, not Gram) or
  (b) via ∂_σ log (Identity 5, nonlinear). Neither is a sign mechanism.
- (Q4) No new positivity conjecture: the only candidate ("h⁰_off ≥ h⁰_diag in the limit") is W ≥ 0 restated. PROVED parts: Lemmas 1–3, Theorem 4, Identity 5,
  and the two corrections in §1. Residue closed.
Screens: (R)(3) linear in Λ only by insertion; (R)(4) Identity 5 lands on the zero side; G0: h⁰ = Gram (Bochner) but W is not its restriction (Thm 4).

