# CA_B_003 — Candidate (c): self-matching — the comb whose symbol is the on-line log-derivative of its own Euler series (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed.**

## 0. Corpus / index check
Index: W3′ (R163_1001 Thm O: "conductor 1 = identification (Hamburger)"), N_009/010 (Λ as fixed point of the Poisson–Euler map,
uniqueness CONDITIONAL on Hamburger), G4F-R162_2801 (quantitative Hamburger rigidity, DEAD as route). So "Hamburger identifies ζ" is
known; what is new here is the **on-line, first-order** form of the matching between test and symbol (Theorem 1) — the exact property
that CA_B_001 §5 shows is the only ζ in the symbol.

## 1. Definitions
For a real comb a: ℕ_{≥2}→ℝ with Σ|a(n)|n^{−σ} < ∞ (σ>1), Z_a(s) := exp Σ a(n)n^{−s}/log n = Σ b_a(n)n^{−s}, Φ_a := γZ_a, γ = π^{−s/2}Γ(s/2).
**Matching defect** (when Φ_a continues meromorphically to ℂ): Δ_a(τ) := ∂_σ log|Φ_a(σ+iτ)|²|_{σ=½} = 2Re Φ_a'/Φ_a(½+iτ).
Meaning: the window symbol of a is ½m − Re P_{a,X} = −½∂_σ log|Z_a/Z_{<X,a}|² + ½Δ_a, so the symbol equals "minus the σ-log-derivative
of the test's own Euler series beyond the window" **iff Δ_a ≡ 0** — test and symbol come from the same series to first order on the line.

## 2. Theorem 1 (self-matching ⟺ FE; PROVED)
Assume Φ_a meromorphic on ℂ. Then Δ_a ≡ 0 on ℝ (off a discrete set) ⟺ Φ_a(s) = εΦ_a(1−s) with ε ∈ {±1}.
Proof. Reality of a gives Φ_a(s̄) = conj Φ_a(s). L(s) := Φ_a'/Φ_a(s) + Φ_a'/Φ_a(1−s) is meromorphic; on s = ½+iτ, 1−s = s̄, so
L = 2Re Φ_a'/Φ_a = Δ_a. Δ_a ≡ 0 ⇒ L ≡ 0 (identity theorem) ⇒ (log Φ_a(s) − log Φ_a(1−s))' = 0 ⇒ Φ_a(s) = εΦ_a(1−s), and applying it
twice ε² = 1. Converse: differentiate the FE and restrict to the line. ∎
## 3. Corollary (uniqueness; CONDITIONAL on Hamburger's hypotheses, Hamburger CITED)
If moreover (s−1)Z_a is entire of finite order and ε = +1, then Z_a = cζ (Hamburger 1921; Titchmarsh §2.13, CITED); comparing
the coefficient of 1 (b_a(1) = 1) gives c = 1, and log ζ = Σ Λ(n)n^{−s}/log n gives a = Λ. The case ε = −1: OPEN (Hamburger's
argument with the sign reversed; not checked). So **Λ is the unique comb in this class for which test and symbol match on the line.**

## 4. Pre-screen
| test | outcome |
|---|---|
| key test a_P / Λ+cδ₂ (test kept) | Δ_a is either undefined (no continuation) or ≢ 0 (Thm 1 + Cor): **property destroyed — passes** |
| O1–O6, O10 (Epstein/DH: FE but no Euler, so not of the form Z_a), O11 (Beurling: Euler, generically no FE), O15 | destroyed (Thm 1, Cor). O7/O8/O13/O14 (kernel/test modifications) do not act on a: property survives them — must be checked against those lemmas' ranges (OPEN) |
| (R)(2) Euler × FE(q=1) | YES — exactly Euler (Z_a) × FE with Γ(s/2) × conductor 1 (Hamburger) |
| (R)(10) names the separating property | YES (identification) |
| (R)(11) **load-bearing at the sign step** | **NO (as of now)**: Δ_Λ ≡ 0 is an identity; substituting it into the window form returns Q_M (CA_B_001 (1.3) + EI_002 pieces) with no inequality. It is the property W3′ already records as identification |
| (R)(4) | the identity is zero-free (FE only) ✓; any sign drawn from it so far goes through CA_B_001 §4 (zeros) ✗ |
| (R)(3) non-linear | YES (exp of the comb) |
Verdict: **passes the modification screen (first candidate of this round to do so), fails (R)(11)**: it is a ζ-specific property with no
sign. By thm:shape(C)/rem:shape-ident it is the kind of property a proof must add; what is missing is an inequality whose proof
uses Δ ≡ 0 and fails when Δ ≢ 0.

## 5. Attempted sign step (ARGUED negative)
Natural attempt: a defect-monotonicity inequality Q_a(s) ≥ Q_Λ(s) − C‖Δ_a‖ or "Q is minimized over combs at Δ=0". False in general:
Q_a is affine in a with no extremality at a = Λ (prop:finite(iv)); a + small positive weight raises or lowers Q_a(s) depending on s.
So Δ cannot enter as a penalty; it must enter through the σ-structure off the line (§6).

## 6. Next construction (proposed, not done): the matched σ-transport
J(σ) := ∫F̂₀²(τ)|Z_{<X}(½+iτ)|²|g_X(σ+iτ)|²dτ, g_X = ζ/Z_{<X} (CA_B_001). Facts: Q-piece I_ζζ = −(1/2π)J'(½) (PROVED, CA_B_001 (1.3));
for σ > 1, J(σ) = Σ_{m,n≥X or =1} b(m)b(n)(mn)^{−σ}ω̂(log m/n) with b ≥ 0 the Euler-tail coefficients; J → ω̂(0) as σ → ∞. The FE (Δ ≡ 0)
fixes J on σ < ½ in terms of σ > ½ with the |χ|² weight. Unlike rem:fe this is **not** a symmetrization (weight |g_X(σ)|² is σ-dependent and
not σ↦1−σ symmetric), so (R)(9) does not exclude it. Target to examine: a log-convexity / Phragmén–Lindelöf argument for J on [½,2] whose
endpoint data are Euler (σ=2) and FE (σ=½) and which fails for Δ_a ≢ 0. Risk: J'(σ) for σ>1 is the non-square bilinear form
−2Σ b(m)log m·b(n)(mn)^{−σ}ω̂(log m/n) — no sign visible; and the polar/family pieces I_pp, I_ζp, I_ρ are outside J.

## 7. Self-review
- Thm 1 proof: L meromorphic, vanishes on a line minus a discrete set ⇒ L ≡ 0 ✓. ε = ±1 ✓. Hamburger's hypotheses (finite order,
  finitely many poles, absolute convergence of both sides' Dirichlet series) — for Z_a they must be assumed: CONDITIONAL ✓ labelled.
- Overlap with W3′/N_009: the uniqueness is Hamburger identification (known); Theorem 1 (first-order on-line matching ⟺ FE) is the new,
  elementary piece. No sign. ✓
- YES→NO: none of the region's clauses; within this candidate (R)(11) stays NO.
