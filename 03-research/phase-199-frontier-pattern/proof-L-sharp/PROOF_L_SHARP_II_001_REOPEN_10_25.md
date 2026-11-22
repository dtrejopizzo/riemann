# PROOF_L_SHARP_II_001 — Reopening constraints 10 and 25 in the FF.1 translate basis (pen and paper)

Phase 199, , no zero
datum is used, and
Notation as in FF_001, GG_001, A_001, E_001 and AA_001: μ ≥ 5, a = ½log μ, λ = √μ, g even admissible on [−a,a] with
g(±a) = 0, A = ∫g e^{x/2} = B, c_N = Σ_{m|N,m<μ}μ(m), M := M_μ(1) = Σ_{m<μ}μ(m)/m, D_μ = ζM_μ − 1, W = Guo's full-line
operator, 𝒲(Φ₁,Φ₂) = ∫Φ₁WΦ₂ (convolution kernel ν, primes ±log q, pole 2cosh((x−y)/2)), F_g(s) = 𝒲(g,τ_s g).
**𝒲_ext means the full-line form of the zero-extended exterior function, killing term included (E_001 §1 correction of
A_001's displayed formula; Paper 46 rem:ext-killing).** This is used in every step below.

## 0. Corpus / index check and the new reason (index rule)
Read: AUDIT_CONSTRAINTS_001 §1–§3 (10 and 25 SOFT, written reasons), AUDIT_L_SHARP_16 §6, FF_001, GG_001, P_001
(P.1–P.4), TEST_CG_001, AA_001 (D.1–D.5, D(iv)), A_001 (Thm 1.1, Prop 2.1, Rem (i)), E_001 §1. Index README phase-199 block:
GG entry (diagonal split NO-GO, "mollifier factorization as sign source" closed), AUDIT_16 entry ("FF.1 does NOT escape
constraint 25"), HH entry. **New reason (as required):** AUDIT_CONSTRAINTS §3 items 2–3 authorize (a) the (C_G) block split
in the FF.1 basis, because GG.0 kills the explicit polar term that killed P/(C_G); (b) the D(iv) Gram evaluated directly in
the exterior variable. Neither was computed before. This memo computes both and decides them.

## 1. The (C_G)-type blocks in the FF.1 basis

### 1.1 Two-block split g | Ψ (PROVED, tautological)
Full-line (GG.1): Φ̌ = g + Ψ, Ψ := Ψ_c + Γ on (a,∞), Ψ_c := Σ_{N≥μ}c_N N^{−1/2}τ_{log N}g, Γ(x) := Φ_{φ₀}(−x), and WΦ̌ = 0 a.e.
(Guo L4.4, CITED). Supports: supp τ_{log N}g = [log N − a, log N + a] ⊂ [a,∞) for N ≥ μ; supp Γ ⊂ [a,∞) (φ₀ ⊂ [−1/λ,1/λ]).
So Ψ = Ψ̌ (zero-extended) and the split is a support split at x = a.
**Translation invariance.** ν, the prime terms and the pole kernel 2cosh((x−y)/2) are all convolution kernels, so
𝒲(τ_sΦ₁,τ_sΦ₂) = 𝒲(Φ₁,Φ₂) for every s (in particular 2A(τ_sg)B(τ_sg) = 2e^{s/2}A·e^{−s/2}B = 2AB). Hence
𝒲[g] = W_T(g) (Paper 46 complete form = full-line form of the zero-extended window vector) and 𝒲[τ_{log N}g] = W_T(g).
**Blocks.** Pair WΦ̌ = 0 with g and with Ψ (absolute convergence as in A_001 Thm 1.1(d), with the killing term, E_001 §1):
 0 = 𝒲(g,Φ̌) = W_T(g) + 𝒲(g,Ψ),  0 = 𝒲(Ψ,Φ̌) = 𝒲(g,Ψ) + 𝒲[Ψ].
**Proposition II.1 (PROVED).** The 𝒲-Gram of (g, Ψ̌) is W_T(g)·[[1,−1],[−1,1]]: rank ≤ 1, kernel (1,1).
In particular 𝒲_ext[Ψ̌] = W_T(g) = −𝒲(g,Ψ̌), and the requested formula 𝒲[Ψ] = −2𝒲(g,Ψ) − W_T(g) is the same scalar identity.
**Half-line vs full-line reconciled.** There is nothing to reconcile once 𝒲_ext is the full-line form of the zero-extended
Ψ̌: the only place where "half-line" enters is the killing term κ_a(x) = ∫_{|x−a|}^∞ν, which is the strip {x > a > y}
of the full-line Lévy energy. A_001's displayed half-line double integral without κ_a is NOT the form in II.1 (E_001 §1).
**Consequence (NO-GO, PROVED).** The two-block split carries one number. Every block inequality for it is the inequality
W_T(g) ≥ … itself. This is the FF.1 instance of P.1 (Q(F₀,F₀) = 0 ⇒ 𝔔 = −Q(G,G)+2Q(F,G)+2AB) and of A_001 Rem (i).

### 1.2 Three-block split g | Ψ_c | Γ: the pole is relocated, not removed (PROVED)
**Lemma II.2 (mean of the comb).** For y ≥ 1, C(y) := Σ_{N≤y}c_N = Σ_{m<μ}μ(m)⌊y/m⌋ − 1 = yM − E(y),
E(y) = Σ_{m<μ}μ(m){y/m} + 1, |E(y)| ≤ μ. For x > a, by partial summation against t ↦ t^{−1/2}g(x − log t) (boundary
terms vanish since g(±a) = 0; ∫t^{−1/2}g(x−log t)dt = e^{x/2}∫g(v)e^{−v/2}dv = Ae^{x/2}):
 Ψ_c(x) = A·M·e^{x/2} + R_c(x),  |R_c(x)| ≤ 3μ^{5/4}‖g‖_{C¹}e^{−x/2}.
(Error: ∫|E||∂_t(t^{−1/2}g(x−log t))|dt over t ∈ [e^{x−a},e^{x+a}], ≤ μ·(½‖g‖_∞+‖g′‖_∞)·2e^{−(x−a)/2}.)
**Lemma II.3 (mean of the gauge mirror).** By T_001 Lemma 1.1 applied to φ₀ (φ₀(0) = 0, GG.0):
Γ(x) = Φ_{φ₀}(−x) = Φ_{φ̂₀}(x) + ½φ̂₀(0)e^{x/2} = −A·M·e^{x/2} + Φ_{φ̂₀}(x), using φ̂₀(0) = −2AM (GG.0).
Since Ψ̌ = O(e^{−3x/2}) (Guo L4.3), Ψ_c and Γ each grow like ±AMe^{x/2} and the growth cancels exactly.
**Proposition II.4 (PROVED).** If A·M ≠ 0, neither Ψ_c nor Γ is in L²(a,∞), the pole functional ∫(·)e^{x/2} of each
diverges, and 𝒲[Ψ_c], 𝒲(g,Ψ_c), 𝒲(Ψ_c,Γ) are undefined (𝒲(g,Ψ_c) = ∫Ψ_c·Wg with Wg(x) ∼ Ae^{x/2} from the pole kernel:
integrand ∼ A²Me^{x}). The divergent mode is exactly e^{x/2}, i.e. the s = 1 pole, with coefficient A·Res_{s=1}D_μ = AM.
**Reading.** GG.0 removes the explicit term −½f̂(0)e^{x/2} from FF.1, but the pole re-enters through the **mean density
M of the comb**, which is the residue of the mollifier defect D_μ at s = 1. Any 3-block split must regularise both pieces
by ∓AMe^{x/2} (or a cut-off of it); the regularised pieces R_c, Φ_{φ̂₀} are O(e^{−x/2}) — in L²(a,∞) — but their pole
functionals ∫R_c e^{x/2} = −∫E(e^{x+…})(…) are averages of the sawtooth Σμ(m){y/m}: not absolutely convergent, and they enter
𝒲 through 2Re(A(·)B̄(·)) cross terms between the two blocks. This is the rank-one pole coupling of constraint 10 (P.2:
"the pole's F₀-piece is a residue"), now as the residue of D_μ at s = 1 paired with the window functional A.
**Subclass A = 0 (PROVED, narrow).** Then the mean vanishes, Ψ_c = R_c ∈ L²(a,∞), and II.4's divergence disappears; the pole
functional of R_c remains conditionally convergent only (OPEN whether it converges; it is the Cesàro mean of the sawtooth E).
This subclass is codimension one and is not closed under the gauge (the gauge filler's mirror is radical only modulo the
rank-one ψ-row ∝ AM of GG.0, which is zero there): it removes the coupling by assumption, not by a mechanism.

### 1.3 Verdict on constraint 10
NO-GO for the reopening (PROVED): in the FF.1 basis the (C_G)-type split is either tautological (II.1, two blocks) or
ill-defined until the pole mode AMe^{x/2} is subtracted from both comb and gauge mirror (II.4, three blocks), and the
subtraction reintroduces the rank-one pole coupling. **Relabel constraint 10:** "basis-independent in content; in the FF.1
basis the pole couples through Res_{s=1}D_μ = M_μ(1), paired with A, between the comb and the gauge mirror". It stays
SOFT only in the sense of P.2 (rank one, explicitly computable), not as "vacuous". AUDIT_CONSTRAINTS §1 entry "vacuous in
FF.1 basis" is CORRECTED.

## 2. Constraint 25: evaluating vᵀGv directly in the exterior variable

### 2.1 The direct evaluation is Theorem 1.1 (PROVED, tautological)
D(iv): vᵀGv = Σ_{m,m′}v_mv_{m′}𝒲_ext(Zσ^{(m)},Zσ^{(m′)}) = 𝒲_ext[Σv_mZσ^{(m)}] = 𝒲_ext[Zr] (bilinearity; v = μ(m) ⊕ 1)
= 𝒲_ext[Ψ̌] = W_T(g) (A_001 Thm 1.1). So "evaluate without cancellation" returns the window form itself: no new content.
The cancellation is absent only because nothing is expanded.

### 2.2 Möbius inversion does not compose with Z (PROVED; FF §2 made explicit)
Z multiplies the argument by n (Σ_n r(n·)); the lattice divides it by m (σ(·/m)/m). The composite is indexed by q = n/m
(D(ii)), not by a Dirichlet convolution, so "Σμ(m)D_m = (ΣD_m)^{−1}" cannot be applied inside 𝒲_ext. Möbius inversion acts
only after the co-Poisson mirror, where both act on the same side (dilations of H by N = nm): that is FF.1, with
coefficients c_N = (1∗μ_{<μ})(N) − δ.

### 2.3 The one-line object and the exact lattice defect (PROVED)
Line m = 1: by T_001 Lemma 1.1 with H(0) = 0, Ĥ(0) = 2A, on x > a:
 Zσ^{(1)}(x) = Σ_{N≥2} N^{−1/2}τ_{log N}g(x) − A e^{x/2}  (comb with coefficients ≡ 1 from N = 2; mean Ae^{x/2} cancels).
Hence the **exact lattice defect** (FF.1 minus this), x > a:
 Zr − Zσ^{(1)} = −Σ_{2≤N<μ}N^{−1/2}τ_{log N}g + Σ_{N≥μ}(c_N − 1)N^{−1/2}τ_{log N}g + Φ_{φ₀}(−x) + Ae^{x/2}.      (II.5)
Everything in (II.5) is a translate of g at log N with an integer coefficient, plus the gauge mirror and one pole mode.
Then 𝒲_ext[Zr] − 𝒲_ext[Zσ^{(1)}] = 2𝒲(Zσ^{(1)},Δ) + 𝒲[Δ], Δ := (II.5), and every pairing of translates is
(NN′)^{−1/2}F_g(log(N′/N)), F_g = c_g∗ν (GG).

### 2.4 Where the bulk reappears (PROVED)
Split F_g(s) = F_g^{loc}(s) + F_g^{nl}(s): F_g^{loc} = (b_∞δ₀ + short-range Lévy)∗c_g vanishes for |s| ≥ 2a; F_g^{nl} = Lévy
tail ∗ c_g − Σ_qc_q[c_g(s−log q)+c_g(s+log q)] + 2A²cosh(s/2).
(a) **Far pairs |log(N′/N)| ≥ 2a** (N′/N ∉ (μ^{−1},μ)): the pairing is F_g^{nl}(log N′/N) = Lévy kernel and prime comb at
log of integer ratios, convolved with c_g, plus the pole. This part IS expressible through the comb and the Lévy kernel at
log(N′/N) without a bulk term. (Exact; YES to the question for these pairs.)
(b) **Near pairs N′/N ∈ (μ^{−1},μ), N ≠ N′**: F_g^{loc}(s) = ∫c_g(s−u)dν_{loc}(u) with |s| < 2a reads the autocorrelation of g on
its support — the window bulk. In (II.5) these are: the first sum (copies 2 ≤ N < μ, all mutually near and near the
window boundary), the overlaps (N,2N) of FF §3, and every pair inside one window-length of the comb.
(c) **Diagonal N = N′**: F_g(0) = W_T(g) itself (translation invariance, §1.1). The diagonal sum is Σ(c_N−1)²/N + Σ_{2≤N<μ}1/N
in (II.5) and Σc_N²/N = ∞ in FF.1 (GG §2(b)): circular and divergent.
(d) **Gauge rows**: 𝒲(τ_{log N}g, Φ_{φ₀}(−·)) is not a translate pairing; it reads φ₀, which the min-leak gauge chooses so that
the comb is cancelled to ~33 digits (AUDIT_16): the cancellation of constraint 25 sits here, between (a)–(c) and (d).
**Answer to (ii).** The lattice defect is exactly expressible through the Weil measure at log of integer ratios **only for far
pairs**. The bulk reappears exactly at (b) near pairs (|log N′/N| < 2a: local autocorrelation of g, including all copies
2 ≤ N < μ of the defect), at (c) the diagonal (W_T(g) itself, divergent sum), and the size cancellation reappears in (d)
comb-vs-gauge rows. No exact identity of the form "𝒲_ext[Zr] = 𝒲_ext[Zσ^{(1)}] + (far-pair comb/Lévy terms)" holds.

### 2.5 Verdict on constraint 25
NO-GO for the reopening (PROVED): the only cancellation-free evaluation is tautological (2.1); every exact decomposition
into the one-line object + defect expands into translate pairings whose near and diagonal parts are the window form itself.
Constraint 25 remains SOFT as a statement about floating-point bases (AUDIT_CONSTRAINTS), but its exact-arithmetic escape is
now closed in the two named variables (ρ/Ψ̌ direct; FF.1/line-1 + defect). What would be new: an exact bound on the
near-pair block (b) that does not reduce to W_T on translates — no candidate known.

## 3. Labels
PROVED: II.1 (Gram W_T·[[1,−1],[−1,1]]; translation invariance incl. pole; half/full-line reconciled via killing term),
II.2 (Σ_{N≤y}c_N = yM_μ(1) − E, |E| ≤ μ; comb mean AMe^{x/2}), II.3, II.4 (pole relocated to Res_{s=1}D_μ; blocks undefined
for AM ≠ 0), (II.5) exact lattice defect, §2.4 far/near/diagonal/gauge classification, §2.1–2.2.
OPEN: convergence of the pole functional of R_c (sawtooth mean) on A = 0; any bound on the near-pair block; L′♯.
NO-GO: (C_G) block arguments in the FF.1 basis (constraint 10 reopening); cancellation-free / Möbius-inversion evaluation of
vᵀGv as a reduction (constraint 25 reopening). CORRECTION to AUDIT_CONSTRAINTS_001 row 10: "vacuous in FF.1 basis" → pole
coupling relocated to the comb mean (M_μ(1)·A). NUMÉRICO: none. No sign of row D is claimed. L′♯ OPEN. **Row D OPEN.**
