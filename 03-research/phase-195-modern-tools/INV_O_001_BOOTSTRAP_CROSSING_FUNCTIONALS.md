# INV_O_001 — Modular/conformal bootstrap as a clause-5 object (track O)

Notation: Paper 46 (04-papers/46-row-d-sign-radial-intersection-form/main.tex): s_T, v_n, N_T, 𝔞_T (eq:form), P_T, W_T, def:W, ν_w, f_w,
thm:Z, thm:D1, thm:O, def:shape-ops (O_1–O_15), thm:shape, cor:shape. Spec clauses (1)–(6): ROUTES-TRIED-INDEX/README.md.
Pure math; no numerics.

## 0. Corpus / index check and new reason
- Index hits: SURVEY_MODERN_UNTRIED B3 (this seed, score 3, "high REF-D risk"); README "Certificados duales, de red,
  flat-top, SOS" (Paper 46 §3–6, thm:Z, thm:R) = class (D); thm:O magic functions (frentes L, N; CA_N_VIAZOVSKA); L55 Johns
  LP (AUDIT_B); W3′ integer-frequency blindness (R163_1001); F-ζ_θ "only integer multiplicities separate" (R163_101);
  INV_A_001 Hamburger rigidity; INV_F_001 ∂log wall; INV_J_001 J4, INV_K_001 K1. "bootstrap" in the index = bootstrap in T
  (G3E-159, G8E-159, W2) — a different object.
- New reason (written): frentes L/N used the *primal extremal function* (magic function). HKS uses a different
  input — sparseness of the light sector plus positivity of the heavy channel — and Mazáč functionals are a *basis* of
  crossing-functionals, not a single extremiser. The question asked is whether either input differs from (D). §3–§4 answer:
  no for HKS (it is (D) plus a comb-generic Cardy term), and Mazáč = magic functions (thm:O, CITED identification). So the
  new reason is consumed: the route closes.
- INV_L_001 (clause 5 via Tate/Poisson/theta): not present at writing time; §2(c) touches θ only to locate where Λ enters.

## 1. The crossing equation (task 1) — PROVED (restatement)
For any real comb a on ℕ (weights v_n(a) = 2a(n)n^{−1/2}) with fixed archimedean datum Γ_ℝ (symbol m) define, for even
h ∈ C_c^∞(ℝ),
  Φ_a(h) := 2∫h(u)cosh(u/2)du − Σ_{n≥2} v_n(a) h(log n) + (1/2π)∫ m(t)ĥ(t)dt.        (X)
"Direct channel" = u-side: polar exchange 2cosh(u/2), light sector {log n : n ∈ N_T} (|u| < 2T), heavy sector n ∉ N_T.
"Crossed channel" = τ-side: the distribution ρ_a defined by Φ_a(h) = ⟨ρ_a, ĥ⟩.
(a) For a = Λ, ρ_Λ = Σ_ρ δ_{γ_ρ} (Weil; thm:Z(ii)): (X) is exactly the crossing equation, with FE ρ ↦ 1−ρ as the
crossing symmetry γ ↦ −γ and Γ_ℝ as the identity/"vacuum" block m.
(b) For h = c_F (F ∈ L²(I_T)), only the light sector is seen: Φ_a(c_F) = 2π·𝔞_T^{(a)}(F) + 2Re(A·B̄) term, i.e. W_T^{(a)}(F);
on P_T it is 𝔞_T^{(a)}(F). For h = w·cos(τ·), w ∈ 𝒲 (def:W), Φ_Λ(h) = f_w(τ) (thm:Z(i)).
(c) Where Λ enters. The genuinely modular crossing is θ(1/x) = √x θ(x), θ = Σ e^{−πn²x}: spectrum πn², weights 1, comb-free.
Λ enters only via −ζ′/ζ, whose "crossing" is the additive antisymmetry ξ′/ξ(s) = −ξ′/ξ(1−s); its Mellin side is (X).
So the bootstrap crossing whose direct spectrum is the comb Λ is (X) itself — not a new identity — and the passage from the
positive θ-crossing to the Λ-crossing is the ∂log step (clause 6, INV_F_001). PROVED (elementary).

## 2. HKS-type light-sector bound (task 2)
**Prop O1 (Cardy/HKS universality, PROVED).** For every real comb a with A_a := Σ_{n∈N_T}|v_n(a)| < ∞ and every F ∈ D_T,
  𝔞_T^{(a)}(F) ≥ (1/2π)∫ (m(τ) − A_a)|F̂(τ)|²dτ,
hence 𝔞_T^{(a)}(F) ≥ 0 whenever F̂ is (L²-)concentrated on {|τ| ≥ τ_*(A_a)}, m(τ_*) = A_a; and the crossed density smoothed
by any ŵ, w ∈ 𝒲^{reg}, is (1/2π)m(τ)·∫w + O_{a,w}(1) (heavy-sector universality = Γ_ℝ alone). Proof: |cos| ≤ 1 in s_T;
the second statement is (X) with ĥ = ŵ(·−τ). ∎
This is the exact analogue of HKS: light data enter only through a total weight, the heavy (large-τ) sector is universal.
**NO-GO (PROVED, by thm:shape(A)).** The property set {crossing (X), Γ_ℝ, light mass ≤ A} is closed under O_1 and O_6
(mass decreases) and under O_15; the conclusion "WP_T" from it is therefore excluded at the windows of lem:shape-del /
prop:shape-eulerdel. Prop O1 is a sign on a spectral cone (|τ| ≥ τ_*), never on P_T. Holds for every comb ⇒ closed.

**Sharpened HKS (light data exact + heavy unitarity a(n) ≥ 0 for n ∉ N_T).** Prop O2 (PROVED): for windowed tests (b) the
heavy sector is invisible, so heavy unitarity adds nothing to 𝔞_T; it enters only through non-windowed tests h = w cos(τ·),
where the sign condition used is w(log n)·v_n ≥ 0 / ≤ 0 off the window — i.e. a dual feasible point (ν_w, 2, 0) of def:W/def:PD.
Every HKS functional ("linear functional on (X), sign on the heavy direct channel, evaluated against the light sector") is
therefore a dual certificate f_w. By thm:D1 (strong duality) sup_w inf f_w = W_T; by thm:O it is not attained; by thm:Z
f_w = Σ_ρ ŵ(τ−γ_ρ). **Verdict: REF-D exactly** (lem:shape-lin(ii), lem:shape-restate). Needs Λ exactly only through the value.

## 3. Mazáč analytic functionals — NO-GO by identification (CITED + thm:O)
Mazáč's extremal functionals for the 1D crossing equation (double zeros on the GFF spectrum 2Δ+2n) are the
Fourier-interpolation / magic-function objects of Radchenko–Viazovska and Cohn–Elkies (CITED: Hartman–Mazáč–Rastelli,
"Sphere packing and quantum gravity", JHEP 2019; Mazáč–Rastelli–Zhou). Transposed to (X) they are interpolation bases with
double zeros at {±log n}; the extremal one is the primal optimum, excluded by thm:O (support ℝ ⇒ certificate ≡ λ_P).
Indexed route (thm:O, frentes L/N), no surviving new reason.

## 4. Task 3 — O_4, O_6, Beurling; where it differs from (D)
- O_4 (cΛ): (X) for cΛ is a valid definition of ρ_{cΛ} = cΣδ_γ + (1−c)·(Γ_ℝ density) — "crossing" holds tautologically
  for every comb; O1 survives O_4 for c ≤ 1; Prop O2 class is (D) for every c.
- O_6 (a_P): same Γ_ℝ, same (X); crossed side = zeros of ζ plus the zeros of E_P on Re s = 0 (Euler factors), atomic.
- Beurling (O_11): (X) is a *definition* of ρ_a; no FE constrains it. Bootstrap crossing for a general comb has no content.
- **The one place it differs from (D) (ARGUED, not built):** the bootstrap's genuine extra input would be *crossed-channel
  unitarity in discrete form*: ρ_a is a locally finite atomic measure with positive integer multiplicities, symmetric under
  γ ↦ −γ, γ ↦ γ̄ (from an order-1 entire function with FE). This separates Λ from O_2, O_4 (c ≠ 1: non-atomic Γ-part),
  Beurling; it does not separate Λ from O_6 alone without the Re s = 0 location. But every functional exploiting it must
  evaluate ĥ at the crossed atoms, i.e. lies in C_zeros / thm:Z (cor:void), and the integrality of multiplicities is the
  indexed residue F-ζ_θ (R163_101) and Hamburger rigidity (INV_A_001, R162_2601c). So it is indexed: no new route.
- Clause 5: (X) does couple Λ|_{N_T} with Γ_ℝ/FE without the factor ζ(½+iτ) — but the FE content in (X) is m and γ ↦ −γ,
  both comb-generic (clause 1 fails). Clause 5 in its useful (Λ-specific) form remains OPEN.

## 5. Verdict
Track O: NO-GO / REF-D. Proved: (X) crossing restatement; Prop O1 (HKS/Cardy cone positivity, comb-generic, closed under
O_1, O_6 ⇒ NO-GO by thm:shape(A)); Prop O2 (HKS functionals = dual certificates, REF-D via thm:D1/thm:O/thm:Z). Mazáč = magic
functions (CITED identification + thm:O). Crossed-channel integrality = indexed (F-ζ_θ, Hamburger). No new partial positivity
on P_T. Do not reopen without a crossed-channel input that is not evaluated at zero positions.
