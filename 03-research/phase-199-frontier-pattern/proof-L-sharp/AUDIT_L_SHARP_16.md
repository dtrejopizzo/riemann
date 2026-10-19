# AUDIT_L_SHARP_16 — audit of FF_001, GG_001, HH_001, TEST_KINKS_001, TEST_MOBIUS_SAWTOOTH_001

Phase 199, "E1" is
not a criterion. Checked against AA_001 (D.1, D.2) +
AUDIT_13, EXTERIOR_DATUM_001 + AUDIT_12, A_001 (Thm 1.1), T_001 Lemma 1.1, PATTERN_001 §2, Mori V Table 1 (text of the paper,
lines 395–426 of the scratchpad copy). One new check script: `AUDIT_L_SHARP_16_comb.py` (mpmath dps 60, g* = MORI15 `p0_eig.json`
vector 0, same Legendre normalisation as TEST_KINKS_001_jets.py; NUMÉRICO).

**Verdict.** FF: identity ACCEPTED; reading "no cancellation / escapes Constraint 25" REJECTED; FF.2 CORRECTED (gauge jet is
of the same order). GG: ACCEPTED WITH CORRECTIONS (Mellin identity and a_P mirror correct; GG.1 is a ~70-digit cancellation
identity). HH: ACCEPTED WITH CORRECTIONS (scale 209 → 54 in data units; "≤3 %" → "≤20 %"; §2(d) only for ω < mλ; its
"Constraint 26" renumbered 28). TEST_KINKS: NUMÉRICO ACCEPTED; "no 33-digit cancellation" in §4 REJECTED, "non-local cell
content" downgraded to ARGUED and gauge-dependent. TEST_SAWTOOTH: data provenance CONFIRMED; verdict relabelled
"NOT SUPPORTED / hypothesis without mechanism" (contradiction rests on one robust step); Λ-reading count 7/9, not 8/9.
No sign of row D. L′♯ OPEN. Row D OPEN.

## 1. FF_001
F1. **FF.0 and the integer table: PROVED, re-checked.** c_N = Σ_{m|N,m<μ}μ(m); for 2 ≤ N < μ all divisors are < μ, so c_N = 0;
for N ≥ μ, c_N = −Σ_{m|N,m≥μ}μ(m). Recomputed for N = 15…39 (script): matches the memo (c_15 = −1, c_17 = c_19 = c_23 = c_29 =
c_31 = c_37 = 1, c_21 = c_22 = c_26 = c_33 = c_35 = c_39 = −1, others 0). "c_μ = −μ(μ)" holds for every integer μ (squarefree
not needed: if μ(μ) = 0 then c_μ = 0).
F2. **Theorem FF.1: PROVED, re-derived.** With F[f](ξ) = ∫f e^{−2πiuξ}, Poisson Σ_{n∈ℤ}f̂(nu) = u^{−1}Σ_kf(k/u) gives, for even f
and u = e^x, Φ_{f̂}(x) = Φ_f(−x) + ½f(0)e^{−x/2} − ½f̂(0)e^{x/2} (T_001 Lemma 1.1 ✓). Inserting (D.1) and regrouping N = nm
(Abel/L² reading, AUDIT_13 C2) gives (FF.1) with the cut |x − log N| ≤ a ✓; N = 1 drops for x > a ✓.
F3. **Does FF.1 escape Constraint 25? NO, confirmed with a precision.** The comb itself does not cancel
internally; it cancels **against the gauge mirror Φ_{φ₀}(−x)**. Ψ̌ = Zr is at the leakage scale (|r| ≲ 10⁻³⁵ on (λ,∞); Ψ̌ ≲
Ce^{−3x/2}·10⁻³⁵), while the comb on g* (|g*| ≤ 1.598, g*(0) = −1.598) is (NUMÉRICO, script):
| x − a | 0.05 | 0.5 | 1 | 2 |
|---|---|---|---|---|
| Σc_N N^{−1/2}g(x−log N) | 3.5·10⁻²⁴ | 5.6·10⁻⁶ | 0.076 | 0.046 |
| max single term | 3.5·10⁻²⁴ | 5.6·10⁻⁶ | 0.109 | 0.296 |
| # active N (c_N ≠ 0) | 1 | 6 | 14 | 46 |
So at depth x − a ≳ 1 the comb is O(10⁻¹) and Φ_{φ₀}(−x) (φ₀ = filler − Σμ(m)h(m·)1_{[1/(mλ),1/λ)}, bulk O(1)) must cancel it to
≈ 33 digits. FF.1 is an exact *rewriting* of the cancellation (lines ↔ translates + gauge), not its removal. The memo's sentence
"the 33-digit cancellation is exactly the step Σ_{m|N}μ(m) = 0 for 2 ≤ N < μ" is REJECTED: that step removes the N < μ
translates only; the remaining 33 digits sit in comb-vs-gauge for N ≥ μ. **Constraint 25 extends verbatim to the translate basis.**
F4. **FF.2 CORRECTED (C-FF2, PROVED for k ≤ 2 since f ∈ C² on (0,λ)).** The gauge jet at a+ is not small. For x ↓ a only n = 1
contributes to Φ_{φ₀}(−x) = e^{−x/2}φ₀(e^{−x}), and continuity of f (and of f′, f″) at u = 1/λ forces φ₀ = h as a germ at 1/λ⁻
(the m = 1 cell is cut at 1/λ, all m ≥ 2 cells are smooth there). Hence e^{−x/2}φ₀(e^{−x}) = g(−x) = g(x) near a+, and
 Ψ̌^{(k)}(a+) = [1 + (−1)^k c_μ μ^{−1/2}] g^{(k)}(a)  (k ≤ 2; polar term 0 by GG.0).
At μ = 15: factors 1 − 0.258 (k = 0), 1 + 0.258 (k = 1), 1 − 0.258 (k = 2). The jump Ψ̌(a+) − Φ̌(a−) = −μ^{−1/2}g(a) is the
image of f's own jump h(λ) at u = λ. The memo's "the edge value is literally the first exterior sample up to −μ^{−1/2}" is
wrong by the O(1) gauge factor; "explains why g*(T) sits at the leakage scale" is ARGUED at most (it is consistent, not causal).
F5. §2 (premise "single Fourier tail of Ĥ" false): ACCEPTED. §3 overlap (N,2N): structural statement PROVED; note that after F3
every overlap is also coupled to the gauge rows. §4 B_{NN′} bilinear decomposition: PROVED (but each B_{NN′} is O(1) vs a 10⁻⁷⁰
total: Constraint 25). §5 "a_P has no mirror": WRONG, corrected by GG (see G4).

## 2. GG_001
G1. **Lemma GG.0: PROVED.** φ₀(0) = f(0) = 0 (H vanishes on |u| < 1/λ); polar term ≡ 0 given f(0) = f̂(0) = 0. Ĥ(0) = 2∫_{1/λ}^{λ}
v^{−1/2}g(log v)dv = 2∫g e^{x/2} = 2A ✓; φ̂₀(0) = −2A·M_μ(1) ✓.
G2. **(GG.1) full-line and Thm GG.1: PROVED as an X-limit, with remarks.** Supports checked: Φ_{φ₀}(−x) ≠ 0 needs x > a + log n,
so the gauge mirror lives on x > a ✓ and 𝒲(g,Φ_{φ₀′}) = 0 by radicality ✓; sign of the ψ-row ✓. Also 𝒲[Ψ̌] = W_T(g) follows from
𝒲[g + Ψ̌] = 0 and 𝒲(g,Ψ̌) = −W_T(g) ✓ (used in §3). **Remark (new):** by F3 each F_g(log N) is O(1) while W_T(g*) is at the
leakage scale (~10⁻⁷⁰ in W* units ℓ); Thm GG.1 is therefore an identity with ≈ 70-digit cancellation between comb rows and the
ψ-row. It is exact but carries Constraint 25. R_X → 0: OPEN (agreed).
G3. **(GG.2) Σ_{N≥μ}c_N N^{−s} = ζ(s)M_μ(s) − 1 (Re s > 1): PROVED** (c = 1∗(μ·1_{<μ}) − δ, c_1 = 1 subtracted ✓). "W_T(g) "=" ∫|ĝ|²|D_μ|²dν̂" is FORMAL (memo says so; the ψ-row is also dropped there). Sign factor = ν̂: restatement, NO-GO as
mechanism ✓.
G4. **a_P mirror: CORRECT, and FF_001 §5 is wrong.** Σ_n 1_{p∤n}f̂(nu) = Σ_nf̂(nu) − Σ_nf̂(pnu), each term has the co-Poisson
mirror. Dirichlet inverse of a_P is μ_P(m) = μ(m)1_{p∤m}; truncated convolution equals δ on N < μ, so the gap survives ✓. Hence
"the gap 2 ≤ N < μ is the Λ-specific feature" (FF §5) is REJECTED: it is shared by a_P. The cΛ failure stays ARGUED.
G5. §2(b) diagonal divergence (c_p = 1 ∀ prime p ≥ μ, Σ1/p = ∞): PROVED, NO-GO ✓. §2(a) coupling set: PROVED.

## 3. HH_001
H1. **Lemma HH.1: PROVED, trivial, gauge-dependent** ✓ (agreed).
H2. **Scale constant WRONG by λ (C-HH1).** The data variable is ω with k = 2πλω (EXTERIOR/TEST_KINKS convention). The ratio of
consecutive jet terms is m(h′/h)/(2πλω) = 1311m/(2π·3.873ω) = **54m/ω**, not 209m/ω (TEST_KINKS_001 `analysis.log`: 107.8 at m = 2,
ω = 1). The conclusion survives: 54m/ω > 1 on the whole window ω ≤ 48 for every m ≥ 1 (m = 1: 1.12 at ω = 48, marginal). The
canonical regime is ω ≫ 54m.
H3. **§2(b) "≤ 3 %" CORRECTED (C-HH2).** Per-line bound |h(λ)|/(1311m) = 5.5·10⁻³⁸/m; summed over the 10 squarefree m < 15 it is
5.5·10⁻³⁸·Σ1/m = 1.5·10⁻³⁷, i.e. 7–20 % of rms Δr_out (0.075–0.20·10⁻³⁵), not ≤ 3 %. Still too small and incoherent; also
"|h_e| ≲ |h(λ)|" is an assumption on the extension, not forced. Verdict of (b) stands as ARGUED.
H4. **§2(d) restricted (C-HH3).** "dilates m ≥ 2 are read in band" holds only for ω < mλ; on ω ∈ [1,48] the dilate m is in band
only for m > ω/λ. The conclusion (r_s carries the Möbius cancellation) stands by F3 independently.
H5. §3 kink–kink block = C′.2/(D.5) with asymptotic profile; NO-GO inherited from AA D(iii)(c): ACCEPTED.
H6. **Numbering.** "Constraint 26" is already taken (AUDIT_14, crossword: η-bound vacuous for N ≲ 130), and 27 by AUDIT_15. HH's
constraint is renumbered **28** (with 54m in place of 209m).

## 4. TEST_KINKS_001
K1. **Jets and jumps: NUMÉRICO ACCEPTED** (jets.json: J/pred = 1.0 at dps 130; μ = 0 jumps 10⁻⁸⁴/10⁻⁶⁰/10⁻⁶⁴). Remark: the check is
near-tautological (f₁ is built term by term, so its jump at λ/m is the cut of cell m); it confirms the code, not new mathematics.
K2. **Divergent jet series: CONFIRMED** (order ≤ 1 relL2 5.5·10³…30; order ≤ 2 ~10⁸…5·10⁵; ratio 54m/ω, h″/h = 4.3·10⁸ ≫ (h′/h)²).
Exponential resummation rms 0.0045 vs 0.05–0.20 (resum.json ✓), corr ≤ 0.08. NO-GO (NUMÉRICO, class: finite-order jet tails and
the one-pole resummation) ACCEPTED.
K3. **Residual reading: PARTLY REJECTED.** (i) "Δr_out ≈ 0.03|h(λ)|": numerically 0.008–0.034·|h(λ)| (|h(λ)| = 5.92 units) ✓,
but this is a coincidence of scale, not evidence. (ii) "no 33-digit cancellation": REJECTED. By F3 and AUDIT_13, the cell
contents μ(m)h(mu)1_{[1/(mλ),λ/m)} are O(1) in bulk and their out-of-band transforms are 10³²–10³⁴ × ρ_p; Δr_out is the
remainder after that cancellation (plus gauge). (iii) "non-local cell content": ARGUED (only a negative test was run; no
positive cell-transform model was fitted). (iv) **Gauge dependence:** Δr_out := p − pro04 − pro8+ − inner_res is defined in
the M = 28 Tate-constrained min-leak gauge of EXTERIOR_DATUM; another φ₀ changes it by a radical vector. The ω ∈ (2,8)
localization is therefore a property of (p, this gauge); gauge-independent only modulo 𝒢̄ (as a coset), which was not tested.
K4. The directional numbers −0.481/−0.296/−0.197 reproduce EXTERIOR ✓; ΣμK order 0 gives +0.016/+0.015/+0.030 (wrong sign) ✓.

## 5. TEST_MOBIUS_SAWTOOTH_001
S1. **Provenance: CONFIRMED.** Mori V Table 1 lists ratio 4.21, 4.72, 4.11, 4.94, 4.55, 4.63, 4.49, 4.70, 4.38, 5.34, 4.90 at
μ = 7, 11–20 with N = 240…570; μ = 18, 19 single N; at μ = 20 the N-sequence 7.83 → 4.90 is still decreasing; Mori says the
arithmetic explanation was "not tested". Increments Δlog κ₄ re-derived (e.g. log(4.94/4.11) = 0.184, log(5.34/4.38) = 0.198) ✓.
S2. **Normalization dependence: CONFIRMED and decisive.** Under 1 − λ₂ every step is positive; under 1 − λ₄ or μ^{9/2}e^{−4πμ}
the signs agree. A sign pattern that flips with the smooth normalizer is not an intrinsic observable at integer resolution.
S3. **Label.** The Möbius reading has no mechanism (memo §3, accepted and PROVED in substance: the window form W_T changes at
μ = m only through Λ(m)m^{−1/2}τ_{log m} and the window length; c_N live on the exterior representation). The data side: only
the step 12 → 13 (+18 %, both μ converged, N/(ac) = 3.2 and 3.0) is robustly against "μ(m) = 0 ⇒ no jump"; 17 → 18 → 19 involve
the single-N, possibly over-estimated μ = 18, 19 values. **Relabel: "NOT SUPPORTED (NUMÉRICO, weak) + no mechanism ⇒ NO-GO as a
reading"**; "CONTRADICTED" overstates 3-digit, 9-step, unconverged data. The alternative reading "undecidable" applies to the
quantitative jump sizes, not to the existence of a Möbius term (excluded structurally).
S4. **Λ-contact count: 7/9, not 8/9.** Prime-power entries down 4/5 (16 up), no-contact steps up 3/4 (15 down). 8/9 needs dropping
15 as noise while keeping 16 (+5 %), which is asymmetric. Label: COMPATIBLE (NUMÉRICO), post hoc, normalization-dependent;
Lemma M (λ decreasing) is the only proved fact.

## 6. Consolidated statement after this round
**Single remaining object (OPEN).** On admissible data at window a = ½log μ, with Ψ̌ = Zr written exactly as (FF.1) = translate
comb Σ_{N≥μ}c_N N^{−1/2}τ_{log N}g + gauge mirror Φ_{φ₀}(−·) (polar ≡ 0):
 𝒲_ext[Ψ̌] ≥ κ μ^{−A} dist²(r, 𝒢̄)  (L′♯ ⟺ (★★)),
where (i) the m = 1 Langer/prolate tail is controlled (Theorem C, CC_001, asymptotic; NUMÉRICO below N ≈ 130), and (ii) the
remaining content is the **non-local Möbius-cell content at leakage scale** — the comb-vs-gauge remainder, gauge-dependent as a
function and canonical only as a coset mod 𝒢̄ — whose 𝒲_ext-coupling to (i) is the (1,n) resonance (−0.48/−0.30/−0.20 W* at
μ = 15). Equivalent operator form (AUDIT_15): exact-resolvent Schur plank with uniform leakage margin (0.612 at μ = 15, J = 50).
No estimate exists for (ii) beyond μ = 15 numerics.
**Constraints 1–28 (one line each; sources in brackets).**
1 TV-slack ≤ λ^W on window carrier (AUDIT_1). 2 no identity + Bochner/C–S/Schur (comb-generic) (AUDIT_1). 3 not symbolic
(AUDIT_1). 4 no multiplier/classwise SOS/Son ≥ 0 + remainder/uniform certificate (AUDIT_1). 5 must use a_n ≡ 1, residue 1,
Γ_ℝ conductor 1, aliasing at n ≈ λ/u together, and fail for cΛ, a_P, Beurling (AUDIT_1/2). 6 quadratic leakage scale μ^{−A}dist²
(AUDIT_1). 7 cross-ratio-class cancellation required (AUDIT_1; restricted by 19). 8 no antisymmetric Hilbert kernel in the
integer index (AUDIT_2). 9 deep-mode value 0.046·B_φ² test object (AUDIT_2). 10 pole term couples the Q-null vector (AUDIT_2).
11 no continuation/flow argument without the virial bound (AUDIT_2). 12 no E-image of one prolate with small repair (AUDIT_3).
13 pole couples only through rank-one residues (AUDIT_3). 14 harmonics = dilations, no per-harmonic sign (AUDIT_4). 15 (C_G)(b)
self-dual, not a reduction (AUDIT_4). 16 Sonin-sector/PW transfer gap (AUDIT_5). 17 gauge must be fixed before comparing forms
(AUDIT_5). 18 sector reduction = parity only (AUDIT_6). 19 semiclassical evaluation on Π-projected data, edge channel at leading
order (AUDIT_7). 20 single-cell data test nothing of interference (AUDIT_8). 21 (1,n) resonances: uniform stationary phase with
remainder (AUDIT_9). 22 P3b test needs Schur against a block with v, without bottom eigenvector (AUDIT_10). 23 (no record found by grep in
AUDIT_10–13 or the crossword — numbering gap kept). 24 Möbius-lattice structure of exterior data, single-line models invalid (AUDIT_12).
25 any lattice/class form must respect the 33-digit cancellation (AUDIT_13) — **extended here: holds in the FF.1 translate basis
(comb vs gauge) and in GG.1 (~70 digits)**. 26 thm:ext-layer(iii) explicit η only for N ≳ 130 (AUDIT_14). 27 Schur plank needs
the exact resolvent (AUDIT_15). **28 (new, from HH/TEST_KINKS, corrected):** the edge jet of an admissible extremal is not a
usable coordinate for ω ≲ 54m (μ = 15, k = 2πλω): jet/kink expansions diverge on the data window; any kink split is gauge-dependent
and either negligible (short extension, ≤ 20 % and incoherent) or the falsified 1/ω model (long); and the Möbius gap 2 ≤ N < μ
is shared by a_P (not Λ-specific).

## 7. Labels after audit
PROVED: FF.0, FF.1, C-FF2 (Ψ̌^{(k)}(a+) = [1 + (−1)^kc_μμ^{−1/2}]g^{(k)}(a), k ≤ 2), GG.0, GG.1 (X-limit), GG.2, a_P mirror and gap,
diagonal NO-GO, HH.1. NUMÉRICO: comb table (F3), TEST_KINKS §1–§3, sawtooth increments. ARGUED: "non-local cell content",
HH §2(b). REJECTED: "FF.1 removes the 33-digit cancellation"; "gap = Λ-specific"; "edge value = first exterior sample up to
−μ^{−1/2}"; "Δr_out has no cancellation"; "CONTRADICTED" for the sawtooth (→ NOT SUPPORTED + no mechanism); 8/9 (→ 7/9).
NO-GO: kink-tail class (orders 0–2 + resummation), Möbius sawtooth as reading of the window bottom, diagonal split.
OPEN: R_X → 0, (ii) above, L′♯. No sign of row D claimed. **Row D OPEN.**
