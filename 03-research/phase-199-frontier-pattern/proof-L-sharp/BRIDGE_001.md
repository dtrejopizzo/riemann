# BRIDGE_001 — backward chain from the certified base to L′♯: planks P0–P4

Phase 199, senior mathematician, backward-chaining role (pen and paper). No zero location is used; zeros appear nowhere in this memo except as
already-recorded evaluation data (none is used as input). No numerics were run; every number quoted
is arithmetic on values already recorded in MORI15_EXTREMAL_001, SYNTHESIS_MECHANISM_001 or AUDIT_L_SHARP_7.

**Outcome in one line.** The bridge is written as P0 ⇐ (P1 ∧ P2 ∧ P3a ∧ P3b) on top of the base (I1 + P4). Three corrections to
the brief come out of writing it exactly: (1) A Lemma 4.1 alone localizes only to J(μ) = e^{O(√μ)} prolate rungs, so P1 needs
a separate **polynomial-margin bulk inequality** (stated as (P1-bulk)); (2) the requested "diagonal dominance at scale
√((1−λ_j)(1−λ_k))" is the wrong shape for P2: exterior prolate tails are **exactly orthogonal** (Slepian), the relative
Langer phase of rungs j ≠ k is 4(k−j)·arcsec ω (μ-free, no stationary-phase decoupling), and the weighted (1,1)-dilate
block is **positive without dominance** because 𝔴_μ ≥ log 2μ pointwise; P2 is therefore restated as a **cross-dilate**
(m ≠ n) bound; (3) the chain fails for cΛ at P3a **only for c > 1**; for c < 1 the pointwise weight stays positive and the
falsifier dies at the base identity I1 (PROVED Λ-specific), not in a plank. One new elementary result: **Lemma B.0
(weight lemma, PROVED): 𝔴_μ(ω) ≥ log 2μ for all ω > 1 and μ ≥ 4**, with the phase-space form w(ω,ν) ≥ H(ω)·log(ν/2π).
First theorem to attempt: **Theorem B (non-resonant dilate evaluation)**, §6. L′♯ / (★★) OPEN. Row D OPEN.

## 0. Corpus / index check, and why this is not a retry
- Read in full: MORI15_EXTREMAL_001, SYNTHESIS_MECHANISM_001, PROOF_L_SHARP_W_001, AUDIT_L_SHARP_7; read the cited parts
  of A_001 (Thm 1.1, Rem 1.1(ii),(iv), Thm 3.1, Lemmas 3.5, 4.1, 4.2, §6 table), U_001 (Thm U.2.1, §4), S_001 (S.6, S.7),
  E_001 (Cor E.3, Rem 3.1), PATTERN_001 (Conjecture κ-band). Index: ROUTES-TRIED-INDEX README l.449–470 (phase 199);
  04_PHASES l.35 (W-Sonin), 1003/1006 (Sonin trace) searched for "phase space / additive frequency / Sonin edge": no entry.
- Why new. Nothing here is a new route. This memo is the **assembly** of the S0–S5 chain of SYNTHESIS §4 after AUDIT_L_SHARP_7,
  rewritten as statements with exact hypotheses, kill-tests and Λ-ingredient placement. The two new items are Lemma B.0 (an
  elementary proof of a fact that was NUMÉRICO) and the restatement of P2 (exact exterior orthogonality instead of
  stationary phase between rungs). Neither uses Sonin positivity as a sign source (W-Sonin stays dead): Π is used only as the
  canonical gauge (constraint 17/19a).

## 1. Notation (from the corpus; checked against A_001 and U_001)
μ ≥ 5, λ = √μ, T = a = ½log μ, I = (−T,T), c = 2πμ. Admissible f: even, real, supp f ⊂ [−λ,λ], f(0) = f̂(0) = 0;
g = Ef|_I. Core: f(λ) = 0. ψ_k = prolates of [−λ,λ] at bandwidth c, eigenvalues λ_k, defects d_k := 1−λ_k.
r_f = f̂|_{(λ,∞)}, ρ_f(t) = r_f(λt) (t > 1). Π = orthogonal projection onto 𝒮(1,1)⁺; ℓ(g) = λ‖Πρ_f‖² (U.2.1, PROVED).
𝒲_ext, Z, Z_log as in E_001 Cor E.3. 𝔴_μ(ω) = H(ω)·log(μω²/√(ω²−1)) − 2H₁(ω), H(ω) = Σ_{n≤ω}1/n, H₁(ω) = Σ_{n≤ω}(log n)/n.
Base identity **I1** (A Thm 1.1, PROVED): W_T(Ef) = 𝒲_ext[Zr_f] for f admissible with f(λ) = 0.

## 2. P0 — the target (exact)
**(P0a) L′♯** (AUDIT_199 / A_001 line 3): ∃κ > 0, A ≥ 0: ∀μ ≥ 5, ∀g ∈ E(core): W_T(g) ≥ κμ^{−A}ℓ(g).
By A Thm 3.1 (PROVED) this is (L_ext): 𝒲_ext[Zr_f] ≥ κμ^{−A}dist²(r_f,𝒢̄) for admissible core f.
**(P0b) κ-band shape** (PATTERN_001 Conj κ-band, lower half): λ^W_T ≥ κ₋·d₄(2πμ), μ ≥ 5.
**Status.** OPEN. (P0a) for all g ∈ Dom W_T follows from the core by Rem 1.1(iii)–(iv) only together with P3b (the edge is
the non-core direction). (P0b) follows from (P0a) with A = 0 plus a lower bound ℓ(g) ≥ c·d₄‖g‖² on the admissible sphere;
that lower bound is OPEN and is not implied by anything in the chain (it is the "f(0) = 0 removes index 0" statement:
the admissible sphere has ℓ ≥ min over f(0) = 0 of leak, which in the self-dual span is attained at ψ₄ up to ψ₀'s O(d₀)).
I record it as **(P0c)**: inf{ℓ(Ef)/‖Ef‖² : f admissible} ≥ c·d₄; status ARGUED (Slepian extremal property + f(0) = 0),
provable with named tools (Slepian–Pollak min-max with one linear constraint; Lemma 4.2's comparison ‖g‖ ↔ ‖f‖, MECH 3.1).

## 3. P1 — localization

### 3.1 What A Lemma 4.1 gives, exactly
A Lemma 4.1 (PROVED, comb-generic): W_T(g) ≥ ‖g‖² − (K+λ+1)‖P_<g̃‖², K = C_∞ + 𝒜_T, Ω_* = e^{K+λ+1} − 2, 𝒜_T =
2Σ_{q<μ}Λ(q)q^{−½}. At μ = 15: Σ_{q<15}Λ(q)q^{−½} = 4.971, 𝒜_T = 9.94 (matches MORI15's A_T), so Ω_* ≥ e^{14.8} ≈ 2.7·10⁶.
In general 𝒜_T ~ 4√μ (PNT, CITED), so **Ω_* = exp(4√μ + √μ·O(1) + C_∞)**. A §4 (ARGUED) converts the Fourier cut to a prolate
cut K_* ≳ (2/π)Ω_*, i.e. rungs 4j with
  **J_{4.1}(μ) ≍ Ω_*/(2π) = e^{O(√μ)}**   (≈ 4·10⁵ at μ = 15).
With the Schur complement this gives only: on H_J := E(span{ψ_k : k > 4J_{4.1}}) the form is ≥ ½‖·‖² (α = 1 after
adjusting constants). **This J is super-polynomial and far beyond the plunge k₀ ≈ 4μ, where the Langer/chirp regime of P2–P3
ceases.** So Lemma 4.1 cannot be the localization step of this chain. (PROVED as arithmetic; the conversion to prolate index
is A's ARGUED remark.)

### 3.2 The plank as it must be stated
Split the admissible space by prolate index: L_J := {Ef : f ∈ span{ψ_{4j}, j ≤ J} admissible} (the self-dual span; the
anti-self-dual ψ_{4j+2} are carried by the odd sector / are at the floor on the extremal, MORI15 §4), H_J := its
W_T-relevant complement in E(admissible) (the rest of the prolate expansion, including plunge and beyond).
Fix **J(μ) := ⌈μ + C₁log μ⌉** (rungs 4j ≤ k₀ = 4μ + 4C₁log μ: below the plunge, d_{4J} ≤ μ^{−10}).

**(P1-bulk) [the extra inequality].** ∃α₀, B: for all v ∈ H_{J(μ)} ∩ core:  W_T(v) ≥ α₀μ^{−B}‖v‖².
**(P1-coupling).** ∃δ₀, D: for u ∈ L_J ∩ core, v ∈ H_J ∩ core:  |W_T(u,v)| ≤ δ₀μ^{D}·ℓ(u)^{½}·‖v‖.

**Proposition P1 (Schur step; PROVED given the two inequalities).** Assume (P1-bulk), (P1-coupling). For g = u + v,
  W_T(g) ≥ W_T(u) − ε(μ)·ℓ(u) + ½α₀μ^{−B}‖v‖²,  **ε(μ) := 2δ₀²μ^{2D+B}/α₀**.
Hence if W_T(u) ≥ κ_L(μ)ℓ(u) on L_J with κ_L ≥ 2ε, then W_T(g) ≥ ½κ_L ℓ(u) + ½α₀μ^{−B}‖v‖² ≥ κ(μ)ℓ(g) with
κ(μ) = min(¼κ_L, α₀μ^{−B}/(4C₀μ²)) (ℓ(g) ≤ 2ℓ(u) + 2ℓ(v), ℓ(v) ≤ C₀μ²‖v‖² by A Lemma 4.2).
*Proof.* 2|W(u,v)| ≤ 2δ₀μ^Dℓ(u)^{½}‖v‖ ≤ ½α₀μ^{−B}‖v‖² + 2δ₀²μ^{2D+B}α₀^{−1}ℓ(u) (AM–GM). The rest is the triangle
inequality for dist² and Lemma 4.2. □
**Relative error of localization.** The minimizer's H_J-component satisfies ‖v*‖² ≤ 4δ₀²μ^{2D+2B}α₀^{−2}ℓ(u*), i.e.
‖v*‖²/‖g*‖² ≤ ε'(μ)·d₄ — exponentially small in norm, but **its W-contribution is of the same order as W(u*) unless
κ_L ≫ ε**. This is the honest content: localization in norm is cheap; localization **in the value** needs κ_L ≥ 2ε, i.e.
the coupling constant δ₀μ^D must be ≲ √(κ_L α₀ μ^{−B}).

**Status.** Prop P1 PROVED (elementary). (P1-bulk) OPEN — this is SYNTHESIS S4; polynomial margin, so TV-robust tools are
admissible (constraint 1 bounds slack by the restricted λ_min, polynomial here). (P1-coupling) OPEN; tool: polarised I1,
W_T(u,v) = 𝒲_ext(Zr_u, Zr_v), plus a bound of 𝒲_ext on Π-projected annulus data; obstacle: Z is not L²-bounded (C 4.2).
The natural route to (P1-coupling) is microlocal: L_J-tails are chirps at local additive frequency ≥ c (cycles ≥ μ), H_J-data
spread over the Sonin annulus 1 ≤ ν/2π ≤ μ; separation in ν gives the coupling bound (S1 of SYNTHESIS; OPEN).

**Comb-genericity.** Lemma 4.1 is comb-generic (A §6). (P1-bulk) and (P1-coupling) are **TV-robust within the margin**: a
comb perturbation of norm < α₀μ^{−B}/2 preserves them. So P1 cannot and need not see Λ at the e^{−4πμ} scale (constraint 1
correctly places the Λ-selection elsewhere). Whether (P1-bulk) holds for F-DH is the decisive DH question (SYNTHESIS S4):
the DH negativity must live in H_J or in the edge, because P3a's leading weight for DH is positive.

**Falsification test (MORI15 data).** (i) Compute R_J := W_T(E f*_J)/W_T(g*) where f*_J is the f(0) = 0 re-imposed
truncation of f* to span{ψ_{4j} : j ≤ J}, J = 1,…,11 (prolates to 44 are shipped). Kill P1 if R_J does not enter
[½, 2] by J = 15 (= μ). Risk flagged by the data: MORI15 §5.2 reads W_T(g*) as carried by a rough floor (Legendre j ≥ 240,
energy 3·10⁻⁷¹); if that floor is physical, R_J stays far from 1 and the bottom is **not** localized in the value — P1 dies.
(ii) Compute λ_min of Mori's form compressed to the orthogonal complement of {Eψ_{4j}, j ≤ 15} (rank-15 deflation of the
shipped 832×832 even matrix). Kill (P1-bulk) at μ = 15 if this λ_min is < 10⁻⁶ (an exponentially small bulk margin).

## 4. P2 — decoupling (restated)

### 4.1 The requested form and why it is the wrong shape
Requested: 𝔐_{jk} = W_T(e_j,e_k), e_j := E(ψ_{4j} − (ψ_{4j}(0)/ψ₀(0))ψ₀) (j = 1,…,J; admissible after f̂(0) is repaired at
O(d)), diagonally dominant in the normalisation 𝔐̃_{jk} = 𝔐_{jk}/√(d_{4j}d_{4k}).
Stationary phase on Langer chirps: for ω > 1 the continuation of ψ_k has wavenumber κ_k(ω) = √((c²ω²−χ_k)/(ω²−1))
(AUDIT_7 §1.1 ✓), χ_k = c(2k+1) + O(1). Then
  κ_{4j}(ω) − κ_{4k}(ω) = (χ_{4k} − χ_{4j})/(2cω√(ω²−1)) + O(c^{−1}) = 4(k−j)/(ω√(ω²−1)) + O(c^{−1}),
so the relative phase is **Δφ_{jk}(ω) = 4(k−j)·arcsec ω + const + O(c^{−1})** — independent of c. (ARGUED, WKB; same
computation as AUDIT_7 §1.1.) **There is no large parameter in the j ≠ k phase**: stationary phase in c does not decouple
different rungs. Decoupling instead comes from two exact facts:
- **(2a) Exact exterior orthogonality (PROVED, CITED Slepian–Pollak).** ∫_ℝψ_jψ_k = δ_{jk}, ∫_{−λ}^{λ}ψ_jψ_k = λ_jδ_{jk} ⇒
  ∫_{|x|>λ}ψ_jψ_k = d_jδ_{jk}; with ψ̂_k = (−i)^k√λ_kψ_k (rescaled) the same holds for the exterior Fourier tails r_k.
- **(2b) The weighted (1,1)-dilate block is positive without dominance.** In θ = arcsec ω, the chirp mass density
  dω/(ω√(ω²−1)) = dθ, and on ω ∈ (1,2) 𝔴_μ(sec θ) = log 2μ − log sin 2θ (direct algebra: ω²/√(ω²−1) = 1/(sin θ cos θ)).
  The matrix ∫𝔴 r_j r̄_k is a θ-Toeplitz-type matrix with symbol 𝔴 ≥ log 2μ (Lemma B.0): it is ≥ log 2μ·diag(‖r_j‖²) **as a
  form**, whatever its off-diagonal entries (they are the Fourier coefficients of −log sin 2θ, of size ≍ 1/|k−j| — so a
  Gershgorin bound would in fact FAIL for J ≍ μ: Σ_{k≠j}1/(|k−j|log 2μ) ≈ 2log J/log 2μ ≈ 2). **Diagonal dominance is
  neither true nor needed for the diagonal-dilate part.**

### 4.2 The plank as it must be stated
**(P2) cross-dilate bound.** Write 𝒲_ext[Zr] = Σ_{m,n≥1}X_{mn}[r] (dilate decomposition: archimedean, comb and pole pieces of
E.3 split by the dilate indices of Ψ̌ = Σ_n n^{−½}S_{−log n}r̃|_{(a,∞)} and of Z_log). Then for r ∈ Π(L_J-tails) ∩ core:
  |Σ_{m≠n}X_{mn}[r]| ≤ η₂(μ)·∫_1^∞𝔴_μ|r(λω)|²λdω,  with η₂(μ) ≤ C c^{−½}log c (target), at least η₂ ≤ 1 − θ₂ < 1.
Stationary-phase content (ARGUED, SYNTHESIS §3.3(1)): dilates m,n sample r at ω_m = mw/λ, ω_n = nw/λ with local Mellin
frequencies τ(ω_m), τ(ω_n), τ(ω) = ω·κ(ω). On ω ≥ √2 τ is increasing, so for m,n with both samples ≥ √2 the phases have no
stationary point and each pair is O(c^{−1}) (one integration by parts, gap ≳ c|m−n|w/λ); the only stationary pairs are the
**resonant pairs (1,n)** with ω₁ ∈ (1,√2), ω_n = nω₁ on the increasing branch, at size c^{−½}n^{−2}log(μn) (Fresnel width).
Total resonant contribution ≍ c^{−½} (≈ 0.10 at μ = 15; PATTERN_001's 8–15 % contact sawtooth).
**Status.** OPEN; provable with named tools (non-stationary phase with explicit remainder for Mellin multipliers; Fresnel
asymptotics for (1,n); uniform Langer asymptotics, CITED Dunster) **on data supported away from ω ∈ ℕ and from ω = 1**;
the truncation jumps at ω = n and the edge ω = 1 are not oscillatory integrals and belong to P3b.
**Comb-generic: YES.** X_{mn} for m ≠ n involve the comb only through the dilate structure; the bound is a phase property and
holds verbatim with weight c′ on Z_log (c′Λ). AUDIT_7 §4.3 / constraint 7: on gauge-like data cross classes are of diagonal
size (E.5); (P2) is claimed only on Π-projected L_J-tails — this is exactly where constraint 7 is open.
**Falsification test (MORI15 data).** With the shipped ρ* (the ψ₄ continuation, amplitude 10⁻³⁵, sampled on ω ∈ [1,4]) compute
the (1,2) and (1,3) resonant terms and the non-resonant pair sum by direct quadrature of E.3 split by dilate index (Λ-free,
one-dimensional). Kill P2 if |Σ_{m≠n}X_{mn}| / ∫𝔴|Πρ*|² ≥ 0.5 at μ = 15 (prediction ≈ 0.10).
Matrix version for the record: from the shipped vectors, 𝔐̃_{jk} for j,k ≤ 3; the eigenvalues 4.08, 1.99, 1.79 (N2) should
equal the diagonal 𝔐̃_{jj} to within η₂ if the cross-dilate terms are small; kill if they differ by more than a factor 2.

## 5. P3 — the diagonal

### 5.0 Lemma B.0 (weight lemma; PROVED here, elementary)
**(i)** For μ ≥ 4 and all ω > 1: 𝔴_μ(ω) ≥ log 2μ, with equality iff ω = √2. **(ii) (phase-space form)** For ν > 0 put
w(ω,ν) := Σ_{n≤ω}n^{−1}[log(νω/2π) − 2log n]; then w(ω,ν) ≥ H(ω)·log(ν/2π).
*Proof.* Key inequality: F(N) := H_N log N − 2H₁(N) ≥ 0 for all integers N ≥ 1. F(1) = 0 and
F(N+1) − F(N) = H_N log(1+1/N) − log(N+1)/(N+1) ≥ log(N+1)·(1/(N+1)) − log(N+1)/(N+1) = 0,
using H_N ≥ log(N+1) and log(1+1/N) ≥ 1/(N+1). For ω ≥ 1 with N = ⌊ω⌋: H(ω)log ω − 2H₁(ω) ≥ F(N) ≥ 0. This gives (ii)
at once. For (i): on (1,2), H = 1, H₁ = 0, 𝔴 = log μ + log(ω²/√(ω²−1)) and ω⁴/(ω²−1) ≥ 4 ⟺ (ω²−2)² ≥ 0, so 𝔴 ≥ log 2μ
with equality iff ω = √2. On ω ≥ 2: ω²/√(ω²−1) ≥ ω, so 𝔴 ≥ H(ω)log μ + [H(ω)log ω − 2H₁(ω)] ≥ (3/2)log μ ≥ log 2μ for
μ ≥ 4. □
(This upgrades SYNTHESIS's "min 𝔴 = log 2μ" from NUMÉRICO to PROVED for μ ≥ 4; AUDIT_7's caveat stands: the minimum *at the
caustic* is built in and is not evidence. What is proved is a statement about the **weight**, not about 𝒲_ext.)
Reading of (ii) (ARGUED): in phase space (position ω, additive frequency ν), the leading exterior weight is ≥ H(ω)log(ν/2π),
nonnegative wherever ν ≥ 2π. The Sonin annulus 𝒱_μ (U.2.1) is, microlocally, 1 ≤ ν/2π ≤ μ plus the one-dimensional
"+"-mode (ρ̂ ≡ const on (−1,1)). So the leading weight is positive on the annulus interior and **degenerates only at the
Sonin edge ν → 2π (μ-free region) and on the "+"-mode (= the polar mode S.6, rank two, indefinite)**. The sign burden of
the whole chain is thereby concentrated in two μ-independent places: the near-edge part of the annulus (inside P1-bulk,
where no semiclassics apply) and the edge/polar channel (P3b).

### 5.1 (P3a) the projected chirp evaluation
**(P3a).** For f ∈ L_J ∩ core and r = r_f:
  𝒲_ext[Zr] = ∫_1^∞𝔴_μ(ω)|Πρ_f(ω)|²λdω + R(f),  |R(f)| ≤ η₃(μ)∫𝔴_μ|Πρ_f|²λdω,  η₃(μ) → 0 (target O(c^{−½}log c)),
where R collects: (a) symbol errors Θ_∞(τ) − log(τ/2π) = O(τ^{−2}); (b) Langer amplitude errors O(c^{−1}); (c) the gauge
error ∫𝔴(|ρ_f|² − |Πρ_f|²) — must vanish to O(c^{−N}) by microlocal separation (gauge at ν ≲ 2π, L_J-tails at ν ≳ c);
(d) the cross-dilate sum, which is P2. Together with Lemma B.0: 𝒲_ext[Zr] ≥ (1 − η₃)log(2μ)·ℓ(g)/λ·λ = (1 − η₃)log 2μ·ℓ(g).
**What it needs.** I1 (PROVED); Π (U.2, PROVED); uniform Langer asymptotics of prolate continuations up to the plunge
(CITED Dunster, uniformity in k ≤ 4J to be checked); Egorov-type calculus for Mellin multipliers applied to dilation sums
(standard, unwritten); Lemma B.0 (PROVED).
**Status.** OPEN; provable with named tools on the class of §6 (support away from ℕ and from ω = 1); the full plank needs P3b.
**Falsification test (MORI15 data; AUDIT_7 §5 pre-check, with Π).** Split f* = v* + f*(λ)p_λ (core part v*); compute
C* := 𝒲_ext[Zr_{v*}] by E.3 directly (Λ-free), and S* := ∫𝔴_15|Πρ_{v*}|²λdω. Prediction C*/S* ∈ [0.8, 1.2]. Kill P3a if
C*/S* ∉ [½, 2]; kill M3's leading order if, on r = Πψ̂₄|_{(λ,∞)} at μ = 10, 15, 20, 30, C/S does not tend to 1.
**Λ-ingredient (enters here).** a_n ≡ 1 through Λ∗1 = log (E.2/E.3): the term −2H₁ that cancels the log² growth of the
archimedean H·log(μω). Conductor 1 through Θ_∞(τ) = log(τ/2π): the archimedean threshold 2π against c = 2πμ fixes the
surviving log μ (and the Sonin-edge threshold ν = 2π in Lemma B.0(ii)). Window lattice through the truncation n ≤ ω (H(ω)).

### 5.2 (P3b) the edge channel
**Exact form (A Rem 1.1(iv), PROVED).** For admissible f with f(λ) ≠ 0, p_λ admissible with p_λ(λ) = 1, v = f − f(λ)p_λ,
h_p = Ep_λ|_I:
  W_T(Ef) = 𝒲_ext[Zr_v] + 2f(λ)·b(v) + f(λ)²·e₂,  b(v) := Re⟨h_p, XΨ_v⟩,  e₂ := W_T(h_p).
Its pieces: g(T) = λ^{½}f(λ) (the window-boundary value) and jumps (λ/n)^{½}f(λ) at x_n = log(λ/n) (Guo Lemma 4.2) — the
lattice of truncation points; in exterior coordinates these are the jumps of the dilate truncations at ω = n, summing to
Ψ̌(a⁺) = g(−T). The polar mode (S.6, PROVED) is the residue-1 piece: Q(G_pol,G_pol) = c₀ρ₀² − 2ρ₀ρ₁, c₀ = ψ(3/2) − log π =
−1.10824, determinant −1 (indefinite), coupling to the harmonics rank one through Θ_∞.
**Canonical choice (needed).** p_λ is a free choice; the split is canonical only if p_λ is chosen 𝒲-orthogonal to the core
block (Schur). Then, minimizing over the scalar f(λ),
  E(f) := 2f(λ)b(v) + f(λ)²e₂ ≥ −b(v)²/e₂  (e₂ > 0).
**(P3b).** e₂ > 0 and, for all v ∈ L_J ∩ core,  b(v)² ≤ (1−θ)·e₂·∫𝔴_μ|Πρ_v|²λdω, with θ = θ(μ) ≥ μ^{−B_e}.
Equivalently **E_j ≥ −(1−θ)∫𝔴_μ|Πr_j|²** for every rung (and every combination), as asked. Then, with P3a,
W_T(Ef) ≥ (1 − η₃ − √(1−θ))·[S(v) + f(λ)²e₂] ≥ ½(θ − 2η₃)[S(v) + f(λ)²e₂].
**Scale check (arithmetic on recorded data; ARGUED).** Slepian's dλ_k/dc = 2λ_kψ_k(1)²/c (CITED) with d_k ≈ e^{−2c}·poly
gives ψ_k(1)² ≈ c·d_k: the edge amplitude is at the leakage scale. At μ = 15: predicted f*(λ)² ≈ a₄²·c·d₄/λ =
3.32·94.2·1.17·10⁻⁷⁰/3.87 ≈ 9·10⁻⁶⁹; recorded f*(λ)² = (7.2·10⁻³⁵)² = 5.2·10⁻⁶⁹. Same order ✓. Consequence: the edge
self-term f(λ)²e₂ is ≈ 10× W_T(g*) if e₂ = O(1); the observed W = 4.76·10⁻⁷⁰ then requires 1 − θ_emp close to 1. **This is
the dangerous plank**: AUDIT_7 §4.4 already shows the edge must carry −51…−78 % of the chirp value.
**Status.** OPEN. Finite (2×2 per direction, rank one in f(λ)); all entries explicit semiclassical quantities except b,
which is an edge–chirp overlap at the truncation lattice (S.4's μ-free regime — no c-decoupling is available here).
**Falsification test (MORI15 data).** Compute with canonical p_λ: e₂, b* = b(v*), S* (above), and
θ_emp := 1 − b*²/(e₂·S*). Consistency: C* + 2f*(λ)b* + f*(λ)²e₂ = 4.763·10⁻⁷⁰. The certificate forces the 2×2 to be ≥ 0 on
span{v*, p_λ}, so θ_emp ≥ −η-errors automatically; the **kill criterion is quantitative**: if θ_emp < 10⁻² at μ = 15 the
chain requires a 1 %-level cancellation in a μ-free channel and P3b is not provable at leading order; if Mori V Galerkin
data at μ = 7, 10, 20 (not shipped; to be restored) give θ_emp decreasing faster than any power, the polynomial-κ claim fails.
**Λ-ingredient (enters here).** Residue 1 (pole 2AB and the polar mode ρ₀ = Ψ̌'s s = 0 residue, I13/P.2); the lattice (jumps at
x_n = log(λ/n), dilate truncations at ω ∈ ℕ); Poisson self-duality of ℤ (S.7(i)). F-DH (no pole, conductor 5, Gauss sums):
its P3a weight is positive (SYNTHESIS S4), so **F-DH must die in P3b or in P1-bulk**; P3b without residue has no polar mode,
so the DH test discriminates the two.

## 6. P4 — the base
**(P4).** λ^W_T > 0 for μ ≤ 15 (Mori VIII, certified, ball arithmetic; even Schur margin 2.40·10⁻⁷⁰, odd 3.95·10⁻⁶⁶). CITED.
**Role.** The chain proves P0 for μ ≥ μ₀ where η₂ + η₃ < θ/2 and κ_L ≥ 2ε hold with explicit constants. P4 closes the
range only if μ₀ ≤ 15. At μ = 15, c^{−½}log c ≈ 0.10·4.5 ≈ 0.46 (naive constants), so η₃ < θ/2 at μ = 15 needs θ ≳ 0.9 or
much better constants. **Gap (15, μ₀) is OPEN** and is the place where the chain will need either explicit constants or
further certification. Falsification: none (cited).

## 7. Where Λ enters, and the cΛ test
| plank | statement uses | cΛ, c > 1 | cΛ, c < 1 | F-DH | Beurling |
|---|---|---|---|---|---|
| base I1 (PROVED) | a_n ≡ 1 summation map, Poisson | fails (defect (1−c)Σc_q(S+S⁻¹)Φ_f, U §4) | **fails here** | holds (conductor-rescaled) | fails (no Poisson) |
| P1 (bulk, coupling) | margin μ^{−B} | holds within margin | holds within margin | **DH must die here or in P3b** | — |
| P2 cross-dilate | phases of dilates | holds (comb-generic) | holds | holds | no object |
| P3a weight | Λ∗1 = log, conductor 1 | **fails**: 𝔴^c = H log(μω²/√) − 2cH₁ ≈ log μ log ω + (1−c)log²ω < 0 for ω > μ^{1/(c−1)} | holds (weight larger) | holds (weight (4/5)log μ′ log ω) | no object |
| P3b edge | residue 1, lattice | — | — | candidate kill (no pole) | no object |

**Answer to the brief's check ("P1, P2 comb-generic; the chain fails for cΛ exactly at P3").** P1 and P2 are comb-generic
(P1 within its polynomial margin) ✓. The chain fails for cΛ **at P3a only for c > 1, and only pointwise**: on the extremal
chirp family itself (mass density dθ, mass beyond ω ≈ 2/(πω)), the negative region ω > μ^{1/(c−1)} carries mass ≲ μ^{−1/(c−1)},
so ∫𝔴^c dm stays positive for c ≤ 2 — P3a must be used as the **pointwise** weight statement over all L_J-tails (including
those with mass at large ω), not as an evaluation on one family. For **c < 1 the chain does not fail in any plank**; it fails
at the base identity I1 (PROVED Λ-specific). So the correct statement is: Λ enters at I1 (proved) and at P3a/P3b (open);
"exactly at P3" is false for c < 1. (ARGUED for the weight algebra; the I1 failure is PROVED in U §4.)

**[ AUDIT_8 correction: the statement "for c < 1 the chain does not fail in any plank; it fails at I1" is
reclassified from ARGUED to OPEN. X_001 §6 (Cor X.7(i)) shows that 𝔔^{c<1} is indefinite on shallow
(non-PW) data: the negative directions of the 0.85Λ falsifier (AA_001, phase 198) are low-frequency,
multi-cell window vectors, within the convention of §7, under the condition that the normalization of AA_001 matches
the cΛ convention of this section (CONDITIONAL on that normalization). Therefore pointwise positivity of the weight 𝔴^c
in P3a does not certify that any plank survives for c < 1 in general; it only does so in the single high-frequency
cell cone built in X_001. Where c < 1 actually fails on PW tails (I1, P1-bulk, or P3b) remains OPEN.]**

## 8. Ranking by leverage, and the first theorem
| plank | leverage (decides viability?) | difficulty | status |
|---|---|---|---|
| P3b edge 2×2 | **highest**: data say leading order (51–78 %), μ-free channel, DH/residue discrimination | medium (finite, but b is μ-free) | OPEN |
| P1-bulk | high: where falsifiers (DH) must die; polynomial margin | high (no tool) | OPEN |
| P3a evaluation | high: tests M3's leading order; Λ-step (log² cancellation) | medium (standard semiclassics) | OPEN; weight part PROVED (B.0) |
| P2 cross-dilate | medium (≈ 10 % effect) | medium | OPEN |
| P1-coupling | medium | medium (Z unbounded) | OPEN |
| P0c, P4-gap | low leverage, needed for closure | low / numeric | ARGUED / OPEN |

**THE first theorem to attempt: Theorem B (non-resonant dilate evaluation of 𝒲_ext).**
Let N ≥ 2, δ ∈ (0,¼), and ρ(t) = a(t)e^{iφ(t)} with a ∈ C_c^∞((N+δ, N+1−δ)), φ real smooth, φ′ ≥ ν₀ > 2π on supp a,
and t ↦ tφ′(t) increasing (monotone Mellin frequency, so no resonant dilate pairs). Then
  𝔔[ρ] = ∫ w(t, φ′(t))·|a(t)|²dt + O_{N,δ,a}(ν₀^{−1})·‖a‖²,
with w the phase-space weight of Lemma B.0(ii); hence 𝔔[ρ] ≥ (log(ν₀/2π) − O(ν₀^{−1}))‖ρ‖² > 0 for ν₀ large.
Why this one: (i) it is the smallest plank-piece that is **not a reformulation** (an asymptotic evaluation with a remainder,
not an identity, not a class bound over a class containing falsifiers — constraints 2, 4); (ii) it involves the dilates
n = 1,…,N and Z_log non-trivially, so it **contains the Λ-step** (the log² cancellation; with weight c on Z_log the
conclusion becomes ∫w^c|a|² and positivity holds for all N iff c ≤ 1); (iii) supports away from ℕ and from t = 1 exclude
the edge, the truncation jumps and the resonances by hypothesis, so it is provable with non-stationary phase and the
Mellin symbol of Θ_∞ alone; (iv) it is exactly the test AUDIT_7 asked for (diagonal truncation on Π-relevant data; for
ν₀ ≫ 2π the gauge is microlocally invisible); (v) it decides constraint 7 on chirps: if the cross-dilate terms are not
O(ν₀^{−1}) here, M3 is dead and the chain stops at P2.
**[ AUDIT_8 note: see constraint 20 (single-cell data) in AUDIT_L_SHARP_8.md §9 — the single-cell
data used in Theorem B do not test cross-interference, resonances, constraint 7, the P3b edge, or the gauge;
positivity on them is a high-frequency cone statement, compatible with the indefiniteness of 𝔔^c (c<1)
elsewhere.]**
Not claimed: Theorem B says nothing about the bottom (the extremal is not of this form: its mass sits at ω ∈ (1,2) and it
is off-core); with supp ⊂ (1,2) it would be pure archimedean high-frequency coercivity (no dilates, no comb), i.e. a Lemma
4.1-type statement — which is why N ≥ 2 is required.

## 9. Does the completed chain give L′♯ with κ polynomial in μ?
If P1 (both inequalities), P2, P3a, P3b and P0c hold with the stated exponents, then for μ ≥ μ₀
  κ(μ) ≥ min{ ¼(θ(μ) − 2η₃ − 2η₂)·log 2μ, α₀μ^{−B}/(4C₀μ²) } − (Schur loss, absorbed if κ_L ≥ 2ε),
which is **polynomial** in μ provided θ(μ) ≥ μ^{−B_e}. Nothing in the chain is intrinsically exponential **once Lemma 4.1 is
replaced by (P1-bulk)**; with Lemma 4.1 alone J = e^{O(√μ)} and the chain does not apply. Honest risks to polynomiality:
(1) θ(μ) — the edge near-cancellation (AUDIT_7: 51–78 % at μ = 15) has unknown μ-trend; (2) (P1-coupling) through the
unbounded Z (C 4.2); (3) (P1-bulk) has no candidate tool; (4) the gap (15, μ₀). On the concentrated rungs the chain predicts
**no** loss (κ ≍ log μ, N2-consistent), so a polynomial loss, if any, comes from the bulk and the edge. Verdict: polynomial
κ is **plausible but conditional on θ(μ)**; the first number that decides it is θ_emp (§5.2 test).

## 10. Labels, residuals, do-not-retry
- **PROVED:** Lemma B.0 (i)–(ii) (elementary; F(N) = H_N log N − 2H₁(N) ≥ 0); Prop P1 (Schur step, given its hypotheses);
  exact exterior orthogonality (2a) (Slepian–Pollak, CITED); μ-independence of the inter-rung Langer phase (2b) at leading
  order is ARGUED (WKB).
- **CITED:** P4 (Mori VIII); Slepian dλ/dc formula; Dunster (Langer uniform asymptotics).
- **ARGUED:** J_{4.1} = e^{O(√μ)} prolate conversion (A §4); edge scale f(λ)² ≈ c·d₄·a₄²/λ (order-of-magnitude match with
  MORI15); phase-space reading of B.0(ii) (sign burden concentrated at the Sonin edge and the polar mode); cΛ table.
- **OPEN:** P0c, P1-bulk, P1-coupling, P2, P3a, P3b, gap (15, μ₀), Theorem B, L′♯, (★★). No sign is claimed. Row D OPEN.
- **Corrections to the brief/synthesis recorded:** P2 is not a diagonal-dominance statement (Gershgorin fails at J ≍ μ;
  positivity of the diagonal-dilate block is pointwise in 𝔴); "fails for cΛ exactly at P3" holds only for c > 1 (pointwise);
  Lemma 4.1 cannot serve as P1.
  **[ AUDIT_8 correction: added — "for c < 1 the chain does not fail in any plank; it fails at I1"
  (§7) is reclassified ARGUED → OPEN (𝔔^{c<1} indefinite on shallow data, CONDITIONAL on the normalization
  of AA_001 matching the convention of §7). Added constraint 20 (single-cell data; AUDIT_L_SHARP_8.md §9) to the
  corpus constraints list.]**
- **Do not retry:** stationary-phase decoupling between prolate rungs j ≠ k (relative phase 4(k−j)arcsec ω is c-free);
  Gershgorin/diagonal dominance for the (1,1)-dilate block at J ≍ μ; Lemma 4.1 as the localization step of a chirp chain;
  P3a checked on one chirp family as evidence of Λ-selection (passes for 1 < c ≤ 2).
