# SPEC_SIGN_OBJECT_001 — specification of the sign object and three candidates (phase 200, stage 2)

Stage-2 synthesizer. Pen and paper; no new numerics were run. Row D (λ_A(T) ≥ 0 on P_T)
and its reformulation L′♯ / (★★) are treated as independent goals. No equivalence of
row D with any other statement is invoked.
NUMERICAL. Everything new in this memo is **specification or proposal (OPEN)**: no sign is proved.

Sources read in full: phase 200 README; LEDGER_L1…L5; AUDIT_CONSTRAINTS_001; AUDIT_L_SHARP_16 §6;
MORI15_EXTREMAL_001; BRIDGE_001 (§§0–3); ROUTES-TRIED-INDEX/README (families, "Specification of the sign carrier",
phases 190–199, l.203–212, l.465–510); Paper 47 `sec:ext` (prob:ext-L, prop:ext-consol, lem:ext-weight, lem:ext-cell).

**Notation** (Paper 47 §22, BRIDGE §1). μ = e^{2T} ≥ 5, λ = √μ, f admissible (even, real, supp ⊂ [−λ,λ],
f(0) = f̂(0) = 0), g = Ef|_I, r = f̂|_{(λ,∞)}, Ψ̌ = (Zr)(e^·)1_{(T,∞)}, 𝒢̄ = gauge (radical), ℓ(g) = 2dist²(r,𝒢̄).
(★★): 𝒜[Ψ̌] + 2A(Ψ̌)B(Ψ̌) − 2⟨Ψ̌, Z_log r⟩ ≥ 2κμ^{−A}dist²(r,𝒢̄), with 𝒜 = (1/2π)∫m|Ψ̌^|².
FF.1 (PROVED): Ψ̌ = Σ_{N≥μ} c_N N^{−½} τ_{log N} g + gauge mirror, c_N = Σ_{m|N, m<μ} μ(m), c_N = 0 for 2 ≤ N < μ,
Σ c_N N^{−s} = ζ(s)M_μ(s) − 1 =: D_μ(s). Elementary observation used below: since Σ_{m|N}μ(m) = 0 for N > 1,
**c_N = −Σ_{m|N, m≥μ} μ(m)**, and in particular **c_N = −μ(N) for μ ≤ N < 2μ** (the only divisor ≥ μ is N). (PROVED,
one line.)

---

## A. Convergence of the ledgers

### A.1 Cross table

| Feature required of the sign object | L1 (RH1–9, 0–99) | L2 (100–162) | L3 (163–193) | L4 (194–199, P47) | L5 (meta) | Verdict |
|---|---|---|---|---|---|---|
| **Second order** (Hessian, not a first-order discriminant) | F4: λ_min ≈ cδ², low rank | P16: only radical equations | F3: every first-order discriminant is a functional of h* | I11: Gram (g,Ψ̌) = W_T·[[1,−1],[−1,1]] | C7 (identity + C–S, wrong direction) | **unanimous** |
| **Not factorized** (not place by place, not a sum of local signs) | F1, F9, F13: G_p indefinite; NG-E1 cross-place never built | P13 (meta-136: polar/Frobenius) | F5 separable only in Euler vectors; F8 irrelevant sites | I12 channel by channel PR, lossless loop | C5 dead by theorem | **unanimous** |
| **Half-space / reflection positivity**, orientation-sensitive | §4: cross OS, half-space | §4: changes sign under A ↦ −A | — | I6 mirror (exterior dual), FF.1 gauge mirror | — | L1+L2+L4 converge; L3/L5 neutral |
| **Reads the exact comb on log ℕ without going through h*** | F6, F8 interference | P7 truncated Pólya radical | F3, F9: positions log n with weights v_n; Kronecker | I9, I10: Möbius lattice, c_N | areas 5, 6, 11 | **unanimous** |
| **Output = square or count**, not a bound | F10 (duality, h⁰ RR) | P17 Hodge-index transfer | F1(B′) "it is not an estimate" | §4: loop defect | §2 pattern: integer/dimension or exact quadratic stability | **unanimous** |
| **Post-cancellation coordinates** (c_N, N ≥ μ; gap 2 ≤ N < μ) | — | — | — | §2(iii), §4: 33–34 digits built into the definition | restriction 25 | L4 + L5 (L1–L3 do not reach that scale) |
| **Transverse coercivity to the Pólya radical / gauge 𝒢̄** | S2: PF cone as gauge | P7, S2 | — | I2 gauge = radical | 17 (fix the gauge) | L1+L2+L4 |
| **Specific to Λ** (a_n ≡ 1, residue 1, conductor 1, aliasing n ≈ λ/u, together) | F5 (DH), F6 | P9 (Ξ_a crossing), P13 T1/T2 | F1(C), F9 (S⁺) | 1d battery | C1 (≈330 routes), restriction 2/5 | **unanimous** |
| **Exponential precision** (e^{−4πμ}, not TV-robust in window) | F3 | P12 | F1(B) | 1b | T1 | unanimous qualitatively; scale in tension (T1) |
| **Natively frustrated** (holonomy m → 2m) | — | — | F7 | — | — | only L3; taken as a test, not as a property |

### A.2 L5 tensions, with decision

**T1 (margin scale).** Decision: **the sign object cannot depend on the scale.** Only what is
PROVED is used as a premise: λ_A ≤ 4·10⁹·T·e^{−15.449T} (simple exponential) and the qualitative barrier r ≤ λ_A (BARRIER_EST Thm 4, PROVED without
a ceiling). Mori's scale exp(−4πμ) (rem:moriceiling, CITED/PLAUSIBLE-UNVERIFIED) is used **only as test data** at μ = 15
(where it is a certified NUMERICAL via the Mori matrix), never as a hypothesis. Consequence: every candidate must deliver an
**exact identity plus a free positivity** (valid under any scale); candidates whose proof spends
slack are excluded (the "with estimates" variant of SPEC_A, which dies under either window scale).

**T2 (Mori ½log15).** Resolved by mandate: CITED, computationally verified (AUDIT_ZENODO_FRONTIER). The
extremal of MORI15_EXTREMAL_001 is used as a NUMERICAL test bench; the basis H.1 (μ ≤ 15) remains PROVED-mod-CITED.

**T3 (governing +/· principle vs. front M).** Reasoned decision: what front M proved (PROVED) is that the arithmetic of
the **sites** carries no information; it proved nothing about the **positions** log N of the post-cancellation coefficients. The
restriction 28 says that the gap 2 ≤ N < μ is shared by a_P; but it does not say it is shared **together with** c_N = −μ(N) in
[μ,2μ) **and** the Poisson mirror of a single term (a_P has a two-term mirror, GG). We adopt: *the (+,·) content of the
object lives in position coincidences of the exterior comb of the type N·N′ ≈ μ·n or N ≈ k·N′ (sums in log N), with
integer coefficients c_N fixed by μ(·)*; never in the arithmetic of individual primes. This is compatible with front M
(positions, not sites), with L3's F9 (S⁺ as a position structure) and with AUDIT_16 §6 (non-local cell content).

---

## B. Formal specification of the sign object

A sign object is a datum 𝔖 = (𝒳_μ, Q_μ, ι_μ) — space, form (or invariant), and an immersion of the exterior datum r ↦
ι_μ(r) ∈ 𝒳_μ — with the following properties. For each one: (i) origin, (ii) falsifier that forces it, (iii) test on
Mori's extremal μ = 15 (all cited data are NUMERICAL from MORI15_EXTREMAL_001).

**P1. Exterior and gauge-invariant.** Q_μ ∘ ι_μ depends on r only modulo 𝒢̄.
(i) restrictions 17 (HARD), 1 (does not tie to the exterior carrier); L2 S2, L4 I2. (ii) gauge falsifier of AUDIT_199 (φ ∈
(−1/λ,1/λ), Eφ = 0, leak > 0). (iii) Evaluate on f* with minimal gauge (M = 28, β = 0.834, 0.677, …) and with φ = 0: the
Q_μ part must coincide; with φ = 0 the jump leak is 0.0645 — Q_μ must not see it.

**P2. Post-cancellation coordinates.** ι_μ(r) is written in the integer coefficients (c_N)_{N≥μ} of FF.1 (or in μ(N), N ≥ μ),
so that the cancellation of 33–34 digits is an identity of the definition rather than a manual operation.
(i) L4 §2(iii), §4; restriction 25 (SOFT, "escapable in an exact basis"), 24(a,b) (HARD: Möbius lattice mandatory, single-line
models invalid). (ii) a_P (shares the gap but not the one-term mirror), deletions q = 3, 7, 8 (break c_N). (iii) Q_μ(ι(r*)) is
evaluated directly on ρ*(ω) (amplitude 7.2·10⁻³⁵ at ω ∈ [1,1.2]): no intermediate piece of Q_μ may
exceed W_T(g*) = 4.763·10⁻⁷⁰ by more than a factor μ^{O(1)}. Quantitative test: the ratio (largest piece of Q_μ)/W_T must be
≤ 10³, not ≈ 10³³ (that of the m ≥ 2 Möbius lines).

**P3. Free second-order positivity.** Q_μ = 𝒫 − ℛ with 𝒫 a square (‖·‖², a Hankel form with a
completely monotone kernel, dimension, count) that exists *before* and *without* the spectrum of W_T, and ℛ controlled by an
exact identity. (i) L1 F4, F10; L2 P16, P18 (N-a: form defined before the spectrum); L5 §2 pattern; restriction 2 (HARD: no
identity + comb-generic C–S). (ii) R161_081 (universal squares refuted by positive eigenvectors). (iii) 𝒫(ι r*) ≥
W_T(g*) and ℛ(ι r*) = 𝒫 − W_T with 𝒫/W_T = O(1)–O(μ^{A}) (not 10³³).

**P4. Orientation-sensitive.** Q_μ changes sign under the inversion of the source/image role (A ↦ −A in L2 §4's sense);
equivalently it is a half-space (reflection) positivity and not a whole-space one. (i) L1 §4, L2 §4, L4 I6. (ii) Bochner
on zeros (L1 F7: Gram of zeros PSD by construction, blind). (iii) In the odd sector of the extremal the positive carrier is the
comb (prime 2: +0.340, c(log 2) < 0) and not the archimedean part (−0.304): the object must reproduce this **carrier
inversion** between sectors; if its 𝒫 is the same in both sectors, it is blind.

**P5. Λ-exact jointly.** Q_μ uses a_n ≡ 1 (via Λ∗1 = log or c_N), residue 1 (pole ≡ 0 in FF.1 or pole −
Chebyshev cancellation), Γ_ℝ of conductor 1 (Lévy kernel ν(ξ) = 2e^{−ξ/2}/(1 − e^{−2ξ})) and aliasing n ≈ λ/u, in a single
identity. (i) restriction 5 (the "fails for" HARD part), thm:shape(B)(C), spec clause (5). (ii) cΛ (c ≠ 1: residue ≠ 1,
Λ∗1 ≠ log), Beurling (no a_n ≡ 1 on log ℕ), deleted primes (c_N altered), zero comb (no Γ_ℝ/residue), Ξ_a
(shifted conductor/pole), DH (no Euler product). (iii) The exact identity of Q_μ must reproduce the four-piece balance
−5.3722 + 3.9164 + 1.5190 − 0.0632 = 4.8·10⁻⁷⁰ (Γ_ℝ + Lévy + pole − comb) to 50 digits.

**P6. Asymmetry of the falsifiers.** For each certified falsifier F, Q_μ^F(ι r_F) < 0 by −Θ(1)·(scale), with
the 𝒫 part intact and ℛ altered. (i) L4 1d ("Λ at +κ(1−λ₄), every falsifier at −Θ(1)"). (ii) the whole
CERT_FALSIFIERS_001 battery. (iii) At μ = 15 one can only compare against cΛ (Theorem B: c > 1 negative) and against deletions via Lemma M;
prediction: ℛ^{cΛ} − ℛ^{Λ} = (c − 1)·(comb) = (c − 1)·0.0632 in the even extremal.

**P7. Transverse coercivity with quadratic escape.** The output is Q_μ(ι r) ≥ κμ^{−A}dist²(r,𝒢̄) *as a corollary* of 𝒫 ≥
c·dist² and ℛ ≤ (1 − θ)𝒫 by identity. (i) restriction 6 (target form), L′♯. (ii) gauge (P1). (iii) κ_emp ∈ [0.56,1.09]:
the object must predict a κ_pred with κ_pred ≤ 0.56 (bound) and, if fine, in [0.56,1.09].

**P8. Index 4 / self-duality.** The object must explain (not assume) why the extremal repairs itself along ψ₄ and not along
ψ₂: a₄/a₀ = −1.6466, a_{4j+2} ≤ 6·10⁻³⁸, W_T/(1−λ₄) = 4.08. (i) L4 1b, K.1b corrected. (ii) zero comb (does not see the self-
duality). (iii) direct datum.

**Compatibility with the 9 hard restrictions** (AUDIT_CONSTRAINTS_001: 1, 2, 8, 12, 17, 24(a,b) + hard parts of 4, 5,
19(a)): P1 ⇒ 17; P2 ⇒ 24(a,b); P3 + P6 ⇒ 2 (the sign step, 𝒫 − ℛ ≥ c·dist², uses the exact identity of ℛ which is false
for the battery); exterior object ⇒ 1 does not tie down (exterior carrier, AUD_1 §4.3(b) ARGUED); 8: Q_μ cannot be an
antisymmetric Hilbert kernel in an integer index (required: 𝒫 symmetric, Hankel/Gram); 12: ι_μ(r) does not reduce to Eψ₀ +
repair (P8 forbids this: the repair is multi-prolate ψ₄); 4(hard: SOS by class, Bochner-Lévy + C–S, Son ≥ 0 + remainder): 𝒫
cannot be Son nor an SOS by class; 5(hard): P5–P6; 19(a): no stationary-phase evaluation on raw r — only on
Π-projected data or in exact identity.

---

## C. Three candidate constructions

### Candidate K1 — Osterwalder–Schrader reflection at the window edge with a Γ-pole kernel (OS-Γ)

*Seeds:* L1 S1 (cross reflection never built, NG-E1), L2 S1 (Hankel energy of Γ's poles, P15, R161_026),
L4 I6/I10 (Poisson mirror; FF.1). *Negative space:* area 1 (quantitative variational: stability by a Hankel
square) and area 11 ((S⁺) as a position structure: N·N′ ≈ μn coincidences).

**1. Definition.** Variable x ∈ ℝ, edge x = T. Reflection θ_T Φ(x) = Φ(2T − x). For an exterior datum Ψ̌ (support (T,∞))
define the **edge OS form**
 𝔒_μ[Ψ̌] := ⟨θ_TΨ̌, 𝒦 Ψ̌⟩ = ∫_T^∞∫_T^∞ Ψ̌(x)Ψ̌(y) k(x + y − 2T) dx dy,
with k the kernel of the Hankel part of the complete Weil distribution. Its archimedean part is
 k_∞(s) = ν(s) = 2e^{−s/2}/(1 − e^{−2s}) = 2Σ_{j≥0} e^{−(2j+½)s}, s > 0,
**completely monotone**, with spectral atoms exactly at the poles of Γ_ℝ(2·) (s = ½ + 2j). Hence
 𝔒_μ^∞[Ψ̌] = 2Σ_{j≥0} |∫_T^∞ Ψ̌(x)e^{−(2j+½)(x−T)}dx|² ≥ 0  (Widom/Hankel CM: a **square**, classical PROVED).
Its polar part has rank one (e^{±x/2}) and its comb part is the sum of atoms Λ(n)n^{−½} at s = log n, which in
FF.1 coordinates is
 𝔒_μ^Λ = −Σ_n Λ(n)n^{−½} Σ_{N,N′≥μ} c_N c_{N′}(NN′)^{−½} ∫∫ g(x)g(y) 1[x + y + log NN′/μ = log n] …
that is, it only sees pairs (N, N′, n) with **N·N′ ≈ μ·n** at the resolution of g's width. Since N, N′ ≥ μ, NN′/μ ≥ μ, and
therefore **no atom n < μ (no prime from the window) enters 𝔒_μ^Λ except through the tail of g**; the effective
atoms are n ≥ μ (the "future primes" of Theorem X, L3 F2). The object is the pair
 𝔖_K1 = (L²(T,∞), 𝒫 = 𝔒_μ^∞ + rank-one polar term, ℛ = −𝔒_μ^Λ + diagonal Toeplitz term).

**2. Target theorem (OPEN).** *Edge reflection identity:* for an admissible f of the kernel,
 W_T(g) = 𝔒_μ^∞[Ψ̌] + 𝔇_μ[Ψ̌] − 𝔒_μ^{Λ,≥μ}[Ψ̌],
where 𝔇_μ is the "diagonal" Toeplitz form of the exterior datum evaluated with the weight of Lemma B.0 (𝔴_μ ≥ log 2μ, PROVED) and
𝔒_μ^{Λ,≥μ} only contains atoms n ≥ μ. *Target inequality:* 𝔒_μ^{Λ,≥μ}[Ψ̌] ≤ (1 − θ)(𝔒_μ^∞ + 𝔇_μ)[Ψ̌] for θ = μ^{−A}.
Corollary: W_T(g) ≥ θ(𝔒_μ^∞ + 𝔇_μ) ≥ θ·log 2μ·‖Ψ̌‖²_{Π} ≥ κμ^{−A}dist²(r,𝒢̄). The output is **a CM Hankel square plus
a positive point weight**; the inequality only compares the n ≥ μ part (outside the window) against the square.

**3. Why it is not REF-D / dual / comb-generic.** It is not REF-D if the identity of item 2 is proved without going through
λ_A: its content is a *relocation* of the atoms n < μ out of the reflected pairing (a consequence of the gap c_N = 0 in
[2,μ) and of c_N = −μ(N) in [μ,2μ)), which is not a property of the spectrum of W_T. It is not a dual certificate: there is no
optimized test function, 𝒫 is canonical (fixed by Γ_ℝ). Where exact Λ enters: (a) a_n ≡ 1 via Λ∗1 = log in 𝔇_μ (Lemma
B.0 uses H_N log N ≥ 2H₁(N)); (b) residue 1: the pole is exactly rank one and cancels against the comb average (GG,
polar ≡ 0); (c) conductor 1: k_∞ with exponents ½ + 2j (another conductor shifts the exponents and breaks the CM relative to the
reflection at T); (d) aliasing: N ≈ λ/u fixes the c_N. Falsifiers: **cΛ, c > 1**: 𝔇_μ loses Lemma B.0 (Theorem B:
negative for large N, PROVED); **c < 1**: dies at identity I1 (BRIDGE §0); **Beurling**: no integer c_N with a gap
(no Möbius on log ℕ); **deleted primes q**: c_N ≠ 0 inside [2,μ) (a −μ-defect appears at N = q), the atoms n < μ
re-enter 𝔒^Λ; **zero comb / Ξ_a**: k_∞ changes (not CM with exponents ½ + 2j, Ξ_a shifts to ½ ± a + 2j); **odd
sector**: the reflection swaps the source/image roles — P4 requires 𝔒^Λ to be the positive carrier there; test below.

**4. Routes index.** Closest entry: README l.208 (phase-193 front A: "reflection positivity between places
(only half of Hankel; fails with any atom, PROVED)") and NG-E1 (OS by place, FALSIFIED). Second: PROOF_L_SHARP_T_001
(Poisson mirror as an exact symmetry) and Q_001 (Toeplitz + Hankel of 𝔔). **New reason stated:** (1) the center of
reflection is the **window edge x = T in the exterior variable**, not x = 0 nor a pair of places; (2) the
reflected objects are the post-cancellation translates with coefficients c_N, and the gap [2,μ) makes the window atoms
(n < μ), which are exactly the ones that killed l.208 ("fails with any atom"), **not enter** the reflected pairing
except through the tail of g; (3) it does not ask for positivity of the whole Hankel half (what was refuted), but that the
**archimedean** Hankel part (CM, free square) dominate the Hankel part **of atoms n ≥ μ**; (4) Q_001 treated 𝔔 without a
reflection at T or coefficients c_N. Risk of coincidence with R162_2502 Thm K (‖K_T‖ ≥ c/λ(T)): must be checked first (it is the
same risk flagged in L2 S1).

**5. Fire test at μ = 15.** With ρ*(ω) (MORI15 §2) compute: (a) 𝔒^∞[Ψ̌*] = 2Σ_j|∫Ψ̌*e^{−(2j+½)(x−T)}|²; prediction:
𝔒^∞ ≥ W_T(g*) = 4.763·10⁻⁷⁰ and 𝔒^∞/W_T ≤ μ^{A} (≈ 10²–10³), not 10³³ (P2); (b) 𝔒^{Λ,≥μ}: only n = 16, 17, 19, … (≥ 15);
prediction: |𝔒^{Λ,≥μ}| < 𝔒^∞ + 𝔇; (c) the contribution of n = 2 (99% of the comb within the window, 0.0632) to the reflected pairing
must be ≤ 10⁻⁷⁰-relative (direct gap test); (d) odd sector: 𝔒^Λ must come out with the sign that reproduces the
positive carrier +0.340. If (c) fails (n = 2 enters at O(1) scale through the tail of g, which at T−0.05 is 10⁻²³), K1 dies.

**6. First lemma.** *Lemma K1.1 (gap invisibility).* Let g ∈ C_c^∞(−T,T), Ψ̌ = Σ_{N≥μ}c_N N^{−½}τ_{log N}g
(no mirror). For every n with 2 ≤ n < μ, ∫∫_{x,y>T} Ψ̌(x)Ψ̌(y)δ(x + y − 2T − log n)dxdy = 0. *Expected proof:* x + y − 2T ≥
(log N − T + …) — check supports: τ_{log N}g has support (log N − T, log N + T); x + y − 2T > log N + log N′ − 4T =
log(NN′/μ²) ≥ 0, and < log n only if NN′ < μ²n; with N, N′ ≥ μ this requires NN′ ∈ [μ², μ²n) — **not empty**. So the
naive version is false and the correct lemma must use the fine structure of c_N in [μ, μ·n) (c_N = −μ(N) in [μ,2μ)) and the
gauge mirror. *Main risk:* that the correct lemma turns out to be "the contribution of n < μ is the Möbius sum Σ μ(N)μ(N′)
over NN′ ≈ μ²n", which is a Möbius correlation estimate (class C6, dead by restriction 1 if brought into the
window). Honestly: K1 only survives if that sum has an exact identity (via Σ_{m|N}μ(m) = 0) and not a bound.

### Candidate K2 — Defect measure on the solenoid and rigidity of the dilation semigroup (DS-×ℕ)

*Seeds:* L4 seed 1 (matrix symbol of the Möbius channel, R2 of JJ: resonances m@1 ≡ nm@n with sign μ(n)), L1 S2 (PF
cone of the extremal as gauge), L3 F5 (Bochner on the solenoid concentrated on the Kronecker line). *Negative space:* area 6
(×2, ×3 rigidity of Furstenberg–Rudolph / dynamics on the solenoid) and area 5 (geometry of numbers over log ℕ).

**1. Definition.** Let 𝕊 = ℚ̂_{>0}^× be the solenoid (dual of discrete ℚ_{>0}^×), ι: ℝ → 𝕊 the Kronecker line
(t ↦ (q ↦ q^{it})). For an exterior datum in FF.1 coordinates define the **defect measure**
 ν_r := |Σ_{N≥μ} c_N N^{−½} χ_N|² ĝ-weighted, as a measure on 𝕊 (χ_N the character N ∈ ℚ_{>0}^×),
i.e. the spectral measure of the integer sequence (c_N) with respect to the ℚ_{>0}^× dilation action, *before*
restricting to ι(ℝ). Its restriction to ι(ℝ) is the datum seen by 𝔔 (CA_E Thm 2, PROVED: the Bochner measure of the form is on
ι(ℝ)). The semigroup ℕ^× acts on 𝕊 by σ_n(χ) = χ^n; the exact resonance "line m at dilation 1 ≡ line nm at dilation
n" (I9, PROVED) says that σ_n^*ν_r and ν_r couple with weight μ(n). Define the **defect entropy functional**
 𝔈_μ[r] := Σ_{n≥2} μ(n)·(ν_r(σ_n^{−1}·) − ν_r)(ι(ℝ)) ·w_n,
with w_n the lattice weight (μ(a)M̃_a/a of thm:ext-lattice). 𝔖_K2 = (M(𝕊), 𝒫 = Haar-part of ν_r(𝕊 ∖ ι(ℝ)), ℛ = 𝔈_μ).

**2. Target theorem (OPEN).** *Projection identity:* 𝒲_ext[Ψ̌] = ν_r^{Haar}(𝕊)·𝔞_∞ − 𝔈_μ[r] (Near form = Kronecker
line − Haar, CA_H, PROVED as anatomy). *Rigidity theorem:* if a measure on 𝕊 is σ_2- and σ_3-quasi-invariant with
cocycle given by μ(n) and its mass on ι(ℝ) is positive, then its singular part with respect to Haar is bounded by its
relative entropy; applied to ν_r, 𝔈_μ ≤ (1 − θ)ν^{Haar}·𝔞_∞. Output: **an entropy (≥ 0) and a Haar mass (≥ 0)**: the
sign would follow from the fact that a measure on 𝕊 with the ×2, ×3 symmetry cannot concentrate its defect on the
Kronecker line (which has zero entropy).

**3. Not REF-D / not dual / not comb-generic.** The positivity (entropy, Haar mass) exists before the spectrum of W_T
(satisfies N-a of R158). Exact Λ: the action uses ℕ^× **on log ℕ with a_n ≡ 1** (Beurling: the semigroup is a different one, ℕ^× free
on non-integer generators, and the Kronecker line has no additive relations — G1 only says that the multiplicative part
does not distinguish; here what distinguishes is that the Kronecker line be the image of ℝ **with** the lattice log ℕ ⊂ ℝ, which uses +
and · at once); the cocycle μ(n) comes from c_N (aliasing); the residue 1 enters as the atomic mass of ν_r at the trivial
character (pole ≡ 0 in FF.1 requires zero mass there). Falsifiers: cΛ alters the cocycle (μ_c(4) ≠ 0, L4 §4); deletions break
σ_q-quasi-invariance; zero comb has no measure on 𝕊 (lives on ι(ℝ) only); Ξ_a shifts the trivial
character; odd sector: the measure changes by χ ↦ χ̄ and must invert the carrier.
**Honest warning:** the "projection identity" is anatomy CA_H rewritten; if the rigidity inequality is proved
only for ν_r restricted to ι(ℝ), it is REF-D. The candidate is only new if the rigidity uses the mass **outside**
ι(ℝ), which does not exist for the window form (CA_E Thm 2) but does for the exterior datum before the projection. This is the
candidate's survival condition.

**4. Index.** Closest entries: CA_E_001 Thm 1–2 (separability, Bochner on the solenoid), CA_H "Near = Kronecker − Haar"
(README l.90 of 06_), INV_C Thm 4 (no measure on log ℚ_{>0} gives 𝔞_T), G4H-159/G4E-R160 (Witt–Kronecker, covariant
flows: DEAD by setup). **New reason:** no entry uses measure rigidity for ×2, ×3 (empty grep for
"Furstenberg", "×2,×3"); INV_C forbids measures on log ℚ that **give** 𝔞_T, not a measure on 𝕊 whose projection to ι(ℝ) is a
term of an identity; the Witt–Kronecker entries were flows with a zero setup, here there is neither flow nor zeros: it is
a static rigidity statement on the post-cancellation exterior datum.

**5. Fire test μ = 15.** Prediction: the lattice Gram of 10 square-free lines with φ₀ has null vector v = μ
⊕ 1 and vᵀGv = W(p) needs ~70 digits (GRAM_INERTIA_001). K2 predicts that 𝔈_μ is the part of vᵀGv given by the resonances
(1,n) with sign μ(n): the couplings −0.48/−0.30/−0.20 W* (n = 2,3,5 approx., AUDIT_16 §6) must be the terms
n = 2, 3, 5 of 𝔈_μ with sign −μ(n)·(…) > 0 for prime n, and (1,4) of p = +0.108 must be ≈ 0 in 𝔈_μ (μ(4) = 0). Test:
compare the sign and magnitude of 𝔈_μ term by term against those resonances (data already existing, nothing new to compute
beyond the projection). If (1,4) is not negligible against (1,2), the cocycle μ(n) is not the correct one and K2 dies.

**6. First lemma.** *Lemma K2.1 (exact quasi-invariance).* For every square-free n ≥ 2 and every FF.1 datum,
σ_n^*ν_r − ν_r = μ(n)·ν_{r,n} + (boundary term supported on N ∈ [μ, nμ)), with ν_{r,n} ≥ 0 explicit. *Main
risk:* that the boundary term (the cutoff line N ≈ μ) is not small — the mollifier's cutoff at μ breaks the
invariance exactly where the escape lives; if the boundary carries all the mass, the lemma is empty.

### Candidate K3 — Γ-limit at the Hermite scale of windows renormalized by the escape (ultraproduct)

*Seeds:* L1 S2 (PF cone of the extremal), L2 S2 (Pólya radical as gauge), L4 1b (self-duality f* ∈ span{ψ_{4j}},
ladder λ_j/(1−λ_{4j}) = 4.08, 1.99, 1.79), L4 1c (Lemma B.0, Theorem B′, Theorem C). *Negative space:* area 4
(ultraproducts/nonstandard: the limit μ → ∞ as a form in an ultraproduct of windows) crossed with area 1 (quantitative
stability: Γ-convergence with defect, which the index records only as the discard of one line in front I).

**1. Definition.** For each μ, let 𝒳_μ := span{ψ_{4j} : j ≤ J(μ)} admissible (self-dual sector, BRIDGE §3.2, J(μ) =
⌈μ + C₁log μ⌉) with the escape norm ‖f‖_ℓ² := Σ a_{4j}²(1 − λ_{4j}) and the renormalized form
 𝒩_μ(f) := W_T(Ef)/(1 − λ₄(2πμ)) .
Coordinates: b_j := a_{4j}√((1 − λ_{4j})/(1 − λ₄)). Fixing an ultrafilter 𝒰 on μ ∈ ℕ (or μ → ∞ along a sequence), the
**limit object** is the form 𝒩_∞ := st(𝒩_μ)_𝒰 on the limit space ℓ²(b) (Hilbert ultraproduct), with the
restriction f(0) = 0 converted into Σ b_j h_{4j}(0)·(…) = 0 in the Hermite limit (ψ_k → h_k under rescaling, CITED
Slepian; h₄(0)/h₀(0) = 3/(2√6)). The comb part of 𝒩_∞ is the limit of the weight 𝔴_μ − log 2μ (Lemma B.0) and of the
lattice resonances, written with c_N/μ statistics at the scale ω = N/μ.

**2. Target theorem (OPEN).** (a) *Γ-convergence:* 𝒩_μ Γ-converges under 𝒰 to 𝒩_∞, with equi-coercivity with respect to ‖·‖_ℓ.
(b) *Positivity of the limit:* 𝒩_∞(b) ≥ κ_∞Σ|b_j|² with κ_∞ > 0, since 𝒩_∞ is an explicit **square**: the limit of the
caustic layer of Theorem C (diagonal (2/3)log 4N − 0.107689, Bessel J₀) plus the weight B.0, both PROVED in their regime. (c)
*Transfer:* (a) + (b) + compactness ⇒ ∃μ₀ with L′♯ for μ ≥ μ₀ and A = 0, κ = κ_∞/2. With the basis H.1 (μ ≤ 15), 15 < μ < μ₀
remains to be covered: this is the pairwise exclusion 19(b) + 26. The output is **a square in the limit** plus a
compactness (contradiction) argument, not a bound with a remainder.

**3. Not REF-D / not dual / not comb-generic.** It is not REF-D if 𝒩_∞ is computed without W_T (as a limit of the exact pieces of
𝔔: weight B.0, layer C, resonances I9). Exact Λ: the weight 𝔴_μ ≥ log 2μ uses Λ∗1 = log (cΛ, c > 1: 𝔴^c → −∞, PROVED Theorem B);
the limit's resonances have cocycle μ(n); residue 1 is the pole ≡ 0; Γ_ℝ enters the Lévy limit of the layer.
Falsifiers: cΛ c > 1 (the limit is negative, cor:ext-cfals), c < 1 (dies at I1), Beurling (no Möbius lattice
in the limit), deletions (change the resonances), zero comb (no weight B.0), Ξ_a (shifts the pole).
**Honest warning:** the central risk is restriction 2 in the limit: if 𝒩_∞ only sees a_n ≡ 1 and log, it can be
comb-generic for c ∈ (0,1] (B′ is positive for κ < 1, JJ: "not Λ-specific"). K3 is only admissible if the limit
**retains** the lattice resonances with cocycle μ(n) to leading order; otherwise it is Theorem B′ under another name
and must be replaced.

**4. Index.** Closest entries: Theorem B′ (thm:ext-multi), KK_001 (Grönwall/virial, pointwise NO-GO), front I (Γ-convergence
and concentration–compactness: discard of one line), PATTERN κ-band. **New reason:** (i) no entry uses a limit of
**escape-renormalized windows** (front I discarded Γ-convergence of the un-renormalized form, where the limit is
trivial); (ii) the space is the self-dual sector ψ_{4j}, identified only recently by MORI15 (K.1b corrected), so the Hermite
limit with the restriction f(0) = 0 on h₀,h₄ is an object that did not previously exist; (iii) it is neither a flow nor a
continuation in μ (does not clash with restriction 11 or KK): it is compactness by contradiction.

**5. Fire test μ = 15.** Prediction: κ_∞ and the limiting ladder must be consistent with 4.08, 1.99, 1.79 (even) and with
a₄/a₀ = −1.6466 versus −ψ₀(0)/ψ₄(0) in the Hermite limit (ψ₄(0)/ψ₀(0) = 0.6073 at μ = 15 vs 0.6124 in the limit).
Test: compare 𝒩_∞ evaluated at b* = (b_0, b_1, …) of the extremal (b_1 = a₄ with normalization 1) with 𝒩_15(f*) = 4.08; the
measured relative discrepancy (0.6124 vs 0.6073 ≈ 0.8%) gives the order of the Hermite error at μ = 15; K3 predicts
|𝒩_15 − 𝒩_∞| ≲ 1%·𝒩_15 if the limit is correct. If 𝒩_∞(b*) differs from 4.08 by more than a factor of 2, the limit does
not retain the structure and K3 dies.

**6. First lemma.** *Lemma K3.1 (equi-coercivity of the self-dual escape).* ∃c > 0: for every μ ≥ 5 and f ∈ 𝒳_μ admissible,
ℓ(Ef) ≥ c(1 − λ₄)‖Ef‖² (BRIDGE's (P0c), ARGUED: Slepian–Pollak min-max with one linear restriction). *Main
risk:* the pairwise exclusion 19(b) + 26: even with (a)–(b), covering 15 < μ < μ₀ requires new certificates or constants
~10× better in thm:ext-layer(iii).

---

## D. Ranking and recommendation

| | Source of free positivity | Λ-specificity | REF-D risk | Technical risk | Lemma 1 decidable in one round |
|---|---|---|---|---|---|
| **K1 OS-Γ** | CM Hankel of Γ_ℝ's poles (classical square) + weight B.0 | high (gap + c_N = −μ(N) + exponents ½+2j) | medium (R162_2502 Thm K) | naive lemma K1.1 is false; the correct version may turn into a Möbius correlation (C6) | yes (supports + identity Σ_{m|N}μ(m) = 0) |
| **K3 Γ-limit** | limit square (layer C + B.0) + compactness | medium (comb-generic risk for c < 1) | low if 𝒩_∞ is computed piecewise | exclusion 19(b)+26 for 15 < μ < μ₀ | yes ((P0c), named tools) |
| **K2 DS-×ℕ** | entropy / Haar mass on 𝕊 | high in principle (cocycle μ(n), lattice log ℕ ⊂ ℝ) | high (if it only uses ι(ℝ) it is CA_H rewritten) | rigidity with a cocycle does not exist in the literature; boundary N ≈ μ | doubtful |

**Ranking: K1 > K3 > K2.**

Justification. K1 is the only candidate with a **canonical, classical, Λ-specific square in its form** (the CM of
ν(ξ) = 2Σe^{−(2j+½)ξ} is strictly Γ_ℝ of conductor 1) placed on the exterior side and **orientation-sensitive**
(P4) by construction, and its first lemma is a question about supports and the identity Σ_{m|N}μ(m) = 0 decidable in one
round. It was already shown above that the naive version of lemma K1.1 is false (pairs NN′ ∈ [μ², μ²n)), so round 1 has a
precise goal: write exactly the contribution of n < μ to the reflected pairing and decide whether it is an identity (survives)
or a Möbius sum without an identity (dies by C6). K3 is the most technically secure but its typical product is "asymptotic
Theorem B′ + compactness", which inherits the pairwise exclusion 19(b) + 26 and can be comb-generic for c < 1; only its
lemma K3.1 (useful for any candidate: it is (P0c)) is launched in parallel. K2 is the most conceptually new (area 6) but
its survival condition (using mass outside ι(ℝ)) does not yet even have a rigorous definition of ν_r outside
the line with the cutoff at μ; it remains as a reserve.

**Recommendation for stage 3:** launch **K1** (construction and audit) with the order: (1) check R162_2502
Thm K against 𝔒_μ; (2) exact lemma K1.1; (3) evaluation of 𝔒^∞ and of the contribution of n = 2 at ρ* (tests 5(a)–(c), NUMERICAL
on already-existing data). In parallel, a verification of K3.1 = (P0c). Record the result in the index in the same
session. Row D: **OPEN**. L′♯: **OPEN**. No sign is asserted.
