# PROOF_L_SHARP_NN_001 — Passivity (positive-real) structure of the Euler product and of the exterior Weil kernel

Phase 199. Companion to the parallel memo MM_001 (feedback-loop / Barkhausen–Nyquist
model of the exterior form).

## 0. Corpus / index check
- ROUTES-TRIED-INDEX: ES-19 (03_PHASES_000-099 l.89) "GLT symbol / index / **passivity in full limit**" — CIRCULAR (returns to
  global positivity / Herglotz). G2F-102/115,116, G1F-R160_S3 §2.1#2, G7F-R162_803: Herglotz criteria = REF-D. INV_F_001 (phase
  194): −ζ′/ζ not Herglotz on the strip; only ID cones cross ∂log.
- **New reason:** ES-19 and the Herglotz entries put the positive-real condition on a *global* object
  (ξ′/ξ, the full symbol, a boundary measure) — that is a restatement of D. Here the PR condition is placed on the **local factors
  E_p themselves (not on log E_p)** and on its exponent threshold c ≤ 1; this is not a cone condition on log ζ (constraint 2/F2),
  since the set {|Im log E| < π/2} is a strip, not a cone, and is not closed under E ↦ E^c, c > 1. The global transfer (§3) is
  then examined and labelled; it is not claimed.

Conventions. PR (positive-real) on a domain Ω: f holomorphic on Ω and Re f ≥ 0 there; strictly PR: Re f ≥ δ > 0.
z = p^{−s}; for Re s > 0, z ranges over the punctured disc 0 < |z| < 1 (all arguments attained as t varies; |z| = p^{−σ}).

## 1. Local positive-real facts (PROVED, classical)
**NN.1 (E_p strictly passive).** For |z| < 1, Re (1−z)^{−1} > ½. Proof: w = 1/(1−z) ⇔ z = 1 − 1/w; |z| < 1 ⇔ |w − 1| < |w| ⇔
Re w > ½. Hence Re E_p(s) > ½ for Re s > 0, and on |z| = r: Re E_p ≥ 1/(1+r). ∎
Sharp argument bound: max_{|z|=r} |arg (1−z)^{−1}| = arcsin r (the circle 1 − re^{iθ} is seen from 0 under half-angle arcsin r).

**NN.2 (log E_p not PR).** Re log E_p = −log|1−z| < 0 whenever |1−z| > 1 (e.g. z = −r: Re = −log(1+r)). Equivalently
Re Σ_k p^{−kσ}cos(kt log p)/k takes negative values for every σ > 0. ∎

**NN.3 (c-threshold).** For c > 0, (1−z)^{−c} (principal branch) is PR on the unit disc **iff c ≤ 1**; for c < 1 it is strictly
PR with Re ≥ cos(cπ/2)·|·|.
Proof. 1 − z maps the disc onto the disc D(1,1) ⊂ {Re > 0}; arg(1−z) fills (−π/2, π/2) (take z → e^{iθ}, θ → 0±, argument
→ ∓π/2). arg (1−z)^{−c} = −c·arg(1−z) fills (−cπ/2, cπ/2). Re > 0 everywhere ⇔ cπ/2 ≤ π/2 ⇔ c ≤ 1. For c > 1 there are z with
|arg| ∈ (π/2, cπ/2), Re < 0. ∎ Restricted to |z| ≤ r < 1 (i.e. σ ≥ σ₁ > 0 for fixed p): PR iff c·arcsin r ≤ π/2 — so at
fixed σ every c is passive for large p; the threshold c ≤ 1 is the uniform-in-p (σ ↓ 0 locally, or p-uniform) statement.

**NN.4 (ζ and 1/ζ: exact PR half-plane).** Let σ₀ be the unique root of Σ_p arcsin(p^{−σ}) = π/2 (σ > 1). Then Re ζ(s) > 0 and
Re 1/ζ(s) > 0 for σ > σ₀ (also at σ = σ₀), and for every 1 < σ < σ₀ both take negative real part for suitable t.
Proof. arg ζ = Σ_p arg E_p (absolutely convergent), |arg E_p| ≤ arcsin p^{−σ} by NN.1 ⇒ |arg ζ| ≤ Σ arcsin p^{−σ}; the same for
1/ζ (arg negated). Sharpness: the maximum of arg E_p on |z| = p^{−σ} is attained at one phase θ_p; by Kronecker (log p ℚ-linearly
independent) t can make finitely many phases simultaneously close to θ_p, and the tail is small ⇒ sup_t arg ζ = Σ arcsin p^{−σ}. ∎
(PROVED; this is van de Lune's classical result on Re ζ > 0 — CITED, J. van de Lune 1983.) Value σ₀ ≈ 1.193 (NUMÉRICO, primes
< 3·10⁶ + PNT tail; literature 1.1923…, digit-level agreement not re-verified).
Note: the PR region of ζ^c is Σ arcsin p^{−σ} = π/(2c) — it exists for every c, so **global** PR of ζ in a half-plane is not
c-specific; only the **local** statement NN.3 is.

**NN.5 (no PR on or near the line; CITED).** For ½ < σ ≤ 1 ζ(σ+it) is dense in ℂ (Bohr), and on σ = ½ arg ζ(½+it) has
Gaussian law of variance ~½ log log T (Selberg). Hence ζ, 1/ζ are not PR on any half-plane σ > σ′ with σ′ < σ₀ (NN.4 covers
1 < σ < σ₀). The multiplier of Z on the exterior line is therefore not passive.

## 2. Transfer to the exterior form (formal; labelled)
Convention (E_001, Cor E.3): Ψ̌ = Zr = Σ_n n^{−½} S_{−log n} r̃|_{(a,∞)} on the exterior half-line. For r supported in ω > λ (a
half-line in the logarithmic variable) its Fourier–Mellin transform R(τ) is holomorphic in a half-plane (one-sided support,
Paley–Wiener), not entire; it is entire of exponential type only if r has compact support. Untruncated, the multiplier of Z is
ζ(½+iτ) (formally — the series does not converge on the line; Z is not L²-bounded, C 4.2), so formally
  𝒲_ext[Zr] "=" ∫ |ζ(½+iτ)|² 𝒦̂_W(τ) |R(τ)|² dτ + (truncation/restriction defects),
and 𝒦̂_W vanishes on the line (constraint 3), so the whole content is in the defects (restriction to (a,∞), the comb −Z_log, the
pole rank-2 part 2AB). The formal |ζ|²·symbol term carries no sign. (ARGUED; consistent with AUDIT_16 §6 constraint 3.)

**Passivity decomposition (what would be needed).** Desoer–Vidyasagar / Zames: a negative-feedback interconnection of a passive
plant G and a strictly (input/output-)passive feedback H is passive; dissipation inequality ⟨u, y⟩ ≥ δ‖y‖² + S(x_T) − S(x_0)
with storage S ≥ 0. The candidate split of 𝒲_ext = 𝒜[Zr] + 2AB − 2⟨Zr, Z_log r⟩:
- plant: 𝒜 (Lévy/archimedean kernel, PD part) — passive (PD ⇒ ⟨u, 𝒜u⟩ ≥ 0, PROVED in A/E);
- pole: 2AB rank-2, indefinite (signature (1,1)) — it is a storage-type term, not a passive block;
- comb −2⟨Zr, Z_log r⟩: negative damping; its multiplier is ζ·(−ζ′/ζ)-type = −ζ′, not PR anywhere near the line (NN.5, and
  INV_F_001: −ζ′/ζ not Herglotz on the strip).
- feedback: Möbius/dilation structure Z^{−1} = Σ μ(n) n^{−½}S_{log n}, multiplier 1/ζ — PR only for σ > σ₀ (NN.4), not on the
  line (NN.5).
Hence the required dissipation inequality 𝒲_ext[Zr] ≥ κℓ cannot be obtained from an interconnection theorem with these blocks:
the feedback is not passive on the line, and the damping block is active. The dissipation inequality is exactly the target
(L_ext / L′♯), i.e. supply rate = 𝒲_ext, storage = dist²(r,𝒢̄) — a restatement, not a reduction.

## 3. Decisive check against constraint 2 (F2) and the falsifiers
- NN.1/NN.3 is a condition on E_p, not a cone condition on log ζ: it fails for E_p^c, c > 1 (NN.3). So it **is** not shared by
  ζ^c, c > 1 — consistent with the falsifier direction X.7(ii)/Y.9 (c > 1). It is shared by c < 1 (strictly passive), consistent
  with AA/JJ (c < 1 not detected by these routes; those falsifiers must be killed elsewhere).
- But it is shared by every Euler product with factors (1 − a_p p^{−s})^{−1}, |a_p| ≤ 1 (a_P, Beurling-type generalized primes
  with norms > 1): NN.1 holds verbatim. So local passivity is **c-specific but not Λ-specific** in the sense of constraint 5.
- The global transfer fails twice: products of PR functions are not PR (ζ is PR only for σ > σ₀ ≈ 1.19), and the exterior form
  lives on the line (NN.5). No norm/C–S step is used anywhere (constraints 4/8 respected).

## 4. Labels
PROVED: NN.1, NN.2, NN.3 (c ≤ 1 threshold, local and p-uniform), NN.4 (|arg ζ| ≤ Σ arcsin p^{−σ}, sharp; = van de Lune, CITED).
NUMÉRICO: σ₀ ≈ 1.193. CITED: NN.5 (Bohr density, Selberg CLT), Zames/Desoer–Vidyasagar passivity theorem.
ARGUED: §2 formal Mellin form (multiplier ζ(½+iτ) only formal; Z not L²-bounded).
NO-GO (within the class "passivity interconnection of the blocks 𝒜 / pole / comb / Möbius feedback with standard composition
rules"): the Möbius feedback (1/ζ) is not PR on the line and the comb is active; no block-passivity proof of 𝒲_ext ≥ κℓ.
CONDITIONAL/OPEN: a passivity proof would need (a) a non-standard storage function absorbing the rank-2 pole, (b) a loop
transformation (multiplier/Zames–Falb) making the Möbius loop passive on the admissible class only — such a multiplier is an
instance of constraint 4 (no multiplier certificate, SOFT) and must be c-specific through NN.3; (c) the c ≤ 1 threshold must be
transported from E_p to the closed loop, which no known composition rule does. L′♯ OPEN. **Row D OPEN.**
