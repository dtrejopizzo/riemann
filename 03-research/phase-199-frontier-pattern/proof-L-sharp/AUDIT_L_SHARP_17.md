# AUDIT_L_SHARP_17 — audit of MM_001 (Barkhausen) and NN_001 (passivity)

Phase 199.
Sources checked: MM_001 (+check.py), NN_001, II_001, E_001, A_001, AUDIT_L_SHARP_16 / CONSTRAINTS_001, R186_052/117,
ES-19, TEST_BRIDGE_001 §5 (table l.106), EXTERIOR_DATUM_001 l.119, JJ_001 l.84, index README l.205–207, 06_ l.212,
04_ l.663 / l.782. Script: scratchpad s0.py (primes < 10⁷ + E₁ tail).

## 1. Local PR facts — CONFIRMED (PROVED)
- MM.1 / NN.1: Re 1/(1−z) ≥ 1/(1+r) on |z| = r and > ½ on the disc: correct (image of |z|=r is the circle on diameter
  [1/(1+r), 1/(1−r)]). max|arg| = arcsin r: correct (tangent line from 0 to the circle 1−re^{iθ}).
- NN.3 both directions verified. c ≤ 1: arg(1−z)^{−c} ∈ (−cπ/2, cπ/2) ⊂ (−π/2, π/2) ⇒ Re > 0 (c = 1 included, Re > ½).
  c > 1: explicit violator for c = 2: z = 1 − 0.1e^{1.4i}, |z| = 0.988 < 1, (1−z)^{−2} = −94.2 − 33.5i (Re < 0); in general
  z = 1 − εe^{iφ} with φ ∈ (π/(2c), π/2), ε small. PROVED.
- NN.2 correct.

## 2. NN.4 and van de Lune — CONFIRMED, one wording fix
- Recomputed σ₀ (root of Σ_p arcsin p^{−σ} = π/2; primes < 10⁷, tail ∫x^{−σ}/log x = E₁((σ−1)log N)):
  **σ₀ = 1.1923474** (NUMÉRICO). Literature: van de Lune (1983, Math. Centrum report ZW 201/83): Re ζ(s) > 0 for
  σ ≥ σ₀ = 1.19234…, σ₀ the root of exactly this equation, and sharp (negative values for 1 < σ < σ₀). Agreement to 7 digits;
  the NN memo's "digit-level agreement not re-verified" is now discharged. The statement is CITED correctly.
- "Exact by Kronecker": correct for the sup over t (finitely many phases aligned, tail small); the sup is NOT attained, so at
  σ = σ₀ the inequality is strict — NN's "(also at σ = σ₀)" is right but needs this one-line reason. The 1/ζ half follows by
  arg negation: correct.
- NN.4 note (ζ^c PR region exists for every c) correct and important: global PR is not c-specific.

## 3. MM.2 "lossless closed loop" — DOWNGRADE to CONDITIONAL (formal identity, not a new theorem)
- Pointwise algebra correct: ∂_σ|F|² = 0 on σ = ½ (|F(σ+it)| even in σ−½), giving |ζ|²Θ + ∂_σ|ζ|² = 0 with
  Θ = Re ψ(¼+it/2) − log π, ∂_σ|ζ|² = 2Re(ζ̄ζ′). check.py (5) confirms numerically.
- Gap 1 (convergence): the prime comb acts on Zr with multiplier 2Re(ζ′ζ̄) only formally — Σ Λ(n)n^{−s} and Σ n^{−s} diverge on
  σ = ½; the identification needs the contour/boundary-value argument (the Weil symbol −2Re F′/F on the line is a distributional
  boundary value; at critical-line points where F vanishes it carries δ-masses, killed only because |ζ|²|R|² vanishes to order 2
  there). MM.2 silently passes through this. The claim "no zero data" is fine for the identity, but the rigorous version is
  exactly II_001's Gram identity / Guo 4.4 (complete Weil form vanishes on Z-images), already PROVED there; MM.2 is a Mellin
  **restatement** of it, not an independent proof, and "PROVED" overstates. Label: CONDITIONAL (on II_001's growth/convergence
  handling) / restatement of II_001.
- "Pole cancelled by comb mean" is a sketch (borrowed from II_001), not proved in MM.
- "W_T = truncation-edge energy of a lossless system": fair as language; it is A_001 Thm 1.1 + II_001 relabelled. No new content.
  "Loop gain exactly 1 at phase 0 on the whole line" is metaphor (there is no loop-gain operator defined); delete or mark ARGUED.

## 4. MM.3 / MM.4 / NN §2 — CONFIRMED
- Re ζ(½) = −1.4604 correct; Θ(0) = −5.372, t₀ = 6.2898 (check.py) consistent with prop:archneg. Cascade non-PR on
  1 < σ < σ₀: CITED van de Lune, now with verified constant.
- MM.4 NO-GO: correct within the declared class 𝒫 (any H-passivity certificate for the full-line loop is 0 ≥ 0; the strict
  part is the truncation term = W_T). It is the ES-19 mechanism made explicit; adequate as a NO-GO of class 𝒫. Small-gain:
  sup|ζ(½+it)| = ∞ CITED correct. Falsifier analysis (cΛ breaks losslessness, a_P keeps MM.1) correct.
- NN §2 NO-GO (standard interconnection with blocks 𝒜/pole/comb/Möbius) correct; ARGUED label for the formal Mellin form right.

## 5. MM.5 numbers — CONFIRMED vs TEST_BRIDGE_001 l.106, two omissions
- γ₂..γ₅ = −0.479, −0.295, +0.062, −0.148; Σ X_nn/S = 0.761; off-diag −0.550; ratio 0.723; X₁₂/√(X₁₁X₂₂) = −0.557: all match v_glob.
  γ₄ > 0 (n = 4 = 2², non-prime, positive) is real and the memo reports it without comment; it is a prime-power channel and
  breaks the "phase π on every dilation channel" reading — the memo's "dominant channels have phase π" must say "n = 2,3,5".
- Omission 1: the comparison bound 1/√3 = 0.577 is the μ → ∞ limit of JJ (l.84) and Y_001's ARGUED bound, not a theorem.
- Omission 2: TEST_BRIDGE l.117: the n = 3 correlation (−0.576) **exceeds** the ARGUED bound 0.426 for n = 3; MM.5 quotes only
  n = 2 ("within 3.5 %"), which is the favourable case. Must be added.
- Also v_1 has ratio 0.519/0.673 = 0.77 and corr −0.714 (> 0.577): the margin 0.28 is vector-dependent. Stays NUMÉRICO,
  irrelevant to any proof (constraint 4).

## 6. NN's three OPEN requirements
(a) storage absorbing the rank-2 pole: well-posed but it is a storage S with ⟨u,y⟩ ≥ S(x_T) − S(x_0) and supply = 𝒲_ext; by
MM.4 the only admissible S makes the inequality W_T itself — not plausibly provable independently. (b) Zames–Falb multiplier
making the Möbius loop passive on the admissible class: falls under constraint 4 (multiplier certificate, SOFT) and must be
c-specific; NN.4 shows global PR is c-agnostic, so a multiplier would have to encode NN.3 locally — no candidate; ill-posed until
the admissible class is fixed. (c) composition rule carrying c ≤ 1 to the closed loop: well-posed as a question but false in the
naive form (products of PR functions are not PR; ζ itself fails for σ < σ₀). Verdict: (a),(c) reduce to the target; (b) is
constraint 4. None plausibly provable as stated. OPEN, no recommended follow-up.

## 7. The "boundary energy / boundary triples" residue — NOT untried
06_ l.212 and 03_ l.201/256 list "boundary triples for W_λ" as never attempted, but this is stale: README l.207 records it as
closed (= polar capacity 𝔊_T, PROVED), 04_ l.663 (G8D-160 C2, DEAD) and l.782 (G1D-R162_2702b: deficiency (2,2), invariants
depend only on (λ,2π), no Λ; DEAD [W3;F3:all], "supersedes phase-60 §4.B"). MM's pointer to it as the live residue is wrong;
any new boundary-energy route must state why it differs from R162_2702b (needs Λ-dependence of the boundary form, which the
prolate triple lacks). Recommend fixing 06_ l.212 status to DEAD (→ R162_2702b).

## 8. Label corrections
MM.1 PROVED; MM.2 PROVED → CONDITIONAL (restatement of II_001 Gram identity; formal on the line); "loop gain = 1" ARGUED/metaphor;
MM.3 CITED (σ₀ = 1.1923474 verified) + NUMÉRICO; MM.4 NO-GO (class 𝒫) kept; MM.5 NUMÉRICO + add n = 3 exceedance and γ₄ > 0.
NN.1–NN.3 PROVED; NN.4 PROVED + CITED, σ₀ NUMÉRICO now digit-verified (1.19235); NN.5 CITED; NN NO-GO kept; (a)–(c) OPEN, not
promising. Residue "boundary triples" → already DEAD (R162_2702b). L′♯ OPEN. **Row D OPEN.**
