# Round 16 B — Direct tails of the high block: the chirp matrix on the gauge-quotient bottom, the first Poisson cell, and the limit problem

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_015_A (𝒯, F_N, B_{NN′}, X, D-units, m, 𝒜_∞, 𝒲). λ = e^T.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-11A … P211-15A, P211-15C; ledger C24–C33. Phase 199: PROOF_L_SHARP_E_001 Theorem E.2 (collapse of the
comb on Poisson images, Λ ∗ 1 = log) and PROOF_L_SHARP_X_001 Theorem B (single-cell chirp data) are prior; they are cited,
not reclaimed (Theorem 3.1 of 15A is E.2 for 𝒯). DOSSIER_001 §7.1 (exterior form, half-line identity W_T(Ef) = 𝒲[Ψ̌_f],
universal frame "all T-dependence sits in the data class") is prior; §2 below is the dilation form of that frame written
for the tail map 𝒯 and is labelled accordingly.
What differs. Nothing indexed is retried. This round is the measurement that 15A names as next step: the tails are built
directly (no Galerkin in the ξ-variable), the ledger of Corollary 3.2 of 15A is evaluated chirp by chirp on the actual
bottom vectors of the gauge quotient, and the K-drift is attributed. The new objects are (i) the attribution (§1), (ii) the
first-cell / dilation reduction of the limit problem (§2, PROVED bookkeeping), (iii) the constrained cell problems (§3).

## 1. Direct tails and the chirp matrix (NUMERICAL)

### 1.1 Construction
ψ_k (even, k ≤ 96, T = 0.8, c = 2πλ² = 31.12) from the Legendre coefficients D_l^{(k)} of the tridiagonal Slepian matrix
(inverse iteration at 60 digits, sign D_0 > 0, the convention of tools/prolate_tailgram.py). Closed form (PROVED, Legendre
→ spherical Bessel, ∫_{−1}^1 P_l(t)e^{−iyt}dt = 2(−i)^l j_l(y)):
    ℱ(ψ_k1_{[−λ,λ]})(ξ) = Σ_{l even} D_l^{(k)}(−1)^{l/2} 2√λ √(l+½) j_l(2πλξ),   u_k := ε_k ℱ(ψ_k1)|_{|ξ|>λ}.
Grid: t = log ξ ∈ [log λ, log 200], dt = π/(4·2πλ·200) (Nyquist 4× the top instantaneous frequency), 16 018 nodes.
Check: 2∫_λ^∞u_k² = 0.7309/0.9830/0.9948 vs d_k = 0.7334/0.9872/0.9998 (k = 20, 22, 24): the cut at ξ = 200 loses
≤ 0.5% of the 1/ξ tail of a single raw prolate; on f(λ) = 0 data (u = O(ξ^{−2})) the loss is < 10⁻⁴.
Mollification: at this grid ρ̂(εξ) − 1 ≤ 2π²(εξ)²∫u²ρ ≤ 3·10⁻⁵ for ξ ≤ 200 (ε = 1.9·10⁻⁴), so ũ_k = u_k to plotting
accuracy; the computations below use u_k, which by Prop 1.1(iii)–(iv) of 15A is legitimate on S𝒜 (f(λ) = 0).
Chirps: F_N(x) = 1_{x<−T}e^{−x/2}u(Ne^{−x}); F̂_N(τ) = N^{−1/2}e^{−iτ log N}∫_{t ≥ log Nλ}e^{t/2}u(e^t)e^{iτt}dt by one zero-padded
FFT per N (2^19 points, Δτ = 0.04, τ ≤ 8400), plus the analytic jump tail (1/π)J_N²∫_{τ_max}^∞ m/τ² (J_N := F_N(−T)).
B_{NN′} = (1/π)∫_0^∞ m Re(F̂_N F̂̄_{N′}) − (log N + log N′)⟨F_N, F_{N′}⟩, N, N′ ≤ 60. Tools: tools/tail_direct/ (new; coef.py, tail.py, run2.py).

### 1.2 Calibration against the Galerkin Gram
Bottom vector b of the D-normalised compression to X = S𝒜 ∩ (SDJ)^⊥ (data of 15A, T = 0.8, Nb = 300), u = Σ b_ku_k:
| K | bottom on X (Galerkin, D-units) | 𝒲[𝒯u] direct (‖u‖ = 1) | ratio |
|---|---|---|---|
| 56 | 2.6397 | 1.1860 | 2.2257 |
| 64 | 2.0028 | 0.8994 | 2.2268 |
| 72 | 1.8045 | 0.8111 | 2.2249 |
| 80 | 1.7637 | 0.7941 | 2.2211 |
| 88 | 1.6336 | 0.7354 | 2.2214 |
| 96* | 1.2772 | 0.6427 | 1.9873 |
The ratio is λ = 2.2255 to 0.2% on the resolved range and breaks at K = 96, the row that 15A discarded as past the Galerkin
cap (K ≈ 0.3·Nb): the direct tail computation has no cap, and it confirms independently that the K = 96 collapse is a basis
artifact. NUMERICAL identity: Galerkin D-units = λ·𝒲[𝒯u]/‖u‖² (the factor λ is the scale between W_T(Ef) on the window and
the ξ-normalisation ‖u‖ of the tails; it is a normalisation, not a correction). The archimedean normalisation was checked
separately: (1/2π)∫m|ê|² = −1.1284 against the Lévy-form Galerkin entry −1.1274 for the first sine of a window of length log 2.

Independent check in the window variable (NUMERICAL, tools/tail_direct/efx.py): for the same bottom vectors,
f = Σ_k ε_kb_kψ_k on [0, λ] (Legendre series), Ef(x) = e^{x/2}Σ_{n≤5}f(ne^x) on I_T and a_T(Ef) by the Lévy form in x-space
(autocorrelation by FFT, comb n = 2, 3, 4). Result: a_T(Ef) = 1.1862, 0.8999, 0.8116, 0.7947, 0.7363 (K = 56 … 88) for
‖f‖ = 1, equal to the direct tail values to 4 digits, and A(Ef), B(Ef) ≤ 1.2·10⁻³, f(0), f(λ) ≤ 10⁻¹³. So the three
computations (Galerkin Gram, chirp ledger, x-space Lévy form) agree, and the Galerkin D-unit is λ·a_T(Ef)/‖f‖².
Correction recorded during the round: a coarse interpolation table for m(τ) near τ = 0 (spacing 3.4) biased the ledger
by up to 0.08 on low-frequency data; it is replaced by a table with spacing 0.005 on [0, 20]; all numbers in this memo
are from the corrected tool, and the high-block numbers moved by ≤ 0.001.

### 1.3 Attribution of the drift (NUMERICAL; T = 0.8, ‖u‖ = 1, N, N′ ≤ 60)
| K | 𝒲 | B₁₁ = 𝒜_∞[F₁] | B₂₂ | Σ_{N≥3}B_NN | off-diag. arch. | off-diag. comb | ⟨m⟩₁ | ⟨m⟩₂ | J₁² | tail mass in (λ, 2λ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 56 | 1.1860 | 1.0675 | 0.1149 | 0.0063 | −0.0011 | −0.0016 | 2.135 | 2.426 | <10⁻⁴ | 0.556 |
| 64 | 0.8994 | 0.8892 | 0.0080 | 0.0013 | 0.0005 | 0.0004 | 1.778 | 2.513 | 2·10⁻⁴ | 0.971 |
| 72 | 0.8116 | 0.8076 | 0.0065 | 0.0007 | −0.0045 | 0.0013 | 1.615 | 2.131 | 2·10⁻⁴ | 0.965 |
| 80 | 0.7947 | 0.7715 | 0.0232 | 0.0013 | 0.0078 | −0.0090 | 1.543 | 1.890 | 1·10⁻⁴ | 0.816 |
| 88 | 0.7362 | 0.7069 | 0.0058 | 0.0006 | 0.0406 | −0.0178 | 1.414 | 1.853 | 2·10⁻⁴ | 0.950 |
(‖F₁‖² = ½‖u‖² identically. Polar terms of the tail, 2A(𝒯u)B(𝒯u), are ≤ 10⁻⁶ on all these vectors, see §2.3.)
Readings.
(a) **The drift is the first chirp alone.** B₁₁ = ½⟨m⟩₁ carries 96–99% of 𝒲 and 100% of its decrease (1.0675 → 0.7069
against 1.1860 → 0.7362). The comb weight of the first chirp is 2 log 1 = 0: the drifting piece is purely archimedean.
(b) **Not the jump.** J₁ = F₁(−T) = λ^{1/2}u(λ): the bottom vectors live above the plunge of every u_k at ξ = λ, and
J₁² ≤ 2·10⁻⁴; the jump part of 𝒜_∞[F₁] (|F̂₁|² ~ J₁²/τ² beyond the sweep) is ≤ (1/π)J₁²∫_c^∞ m/τ² ≤ 10⁻⁵. Lemma 2.4 below
bounds it in general.
(c) **Not the non-resonant pairs.** The off-diagonal is ≤ 0.04 in modulus (≤ 5% of 𝒲), of both signs, not monotone in K.
The chirp count carrying mass is X_eff ≈ 1 (95–97% of the tail mass in the first cell (λ, 2λ) for K ≥ 64), so the
Montgomery–Vaughan regime of 15A Thm 3.3 (X ≫ 1) is never entered and its sharpness is not the issue here; the measured
off-diagonal is far below any bound of that form (the bound is O(X‖w′‖₁) with X ≥ 1, i.e. O(1) in these units).
(d) **Not the resonant comb.** Σ_{N≥2}B_NN = 2⟨𝒯_log u, 𝒯u⟩-part ≤ 0.12 and decreasing to ≤ 0.024.
(e) The mechanism: as K grows the optimiser moves the tail mass into the first Poisson cell and lowers the x-frequency of
F₁ there (⟨m⟩₁: 2.14 → 1.41; for comparison m(c) = m(31.1) = 1.61). In the window variable the same drift splits evenly
into a Rayleigh factor a_T(Ef)/‖Ef‖² = 1.156, 0.969, 0.901, 0.954, 0.915 and a transfer factor ‖Ef‖²/‖f‖² = 1.026,
0.929, 0.901, 0.833, 0.804 (product × λ = the Galerkin D-unit bottom). The bottom functions f carry no mass in the gauge
region |y| < 1/λ (< 10⁻³).

## 2. Bookkeeping that is exact (PROVED unless labelled)

### Lemma 2.1 (dilation form of the tail; PROVED)
Let u be even on |ξ| > λ, in the domain of 15A Theorem 3.1, and F₁(x) := 1_{x<−T}e^{−x/2}u(e^{−x}). Then for every N ≥ 1 and
x < −T,  F_N(x) = N^{−1/2}F₁(x − log N),  hence  𝒯u = 1_{(−∞,−T)}·Σ_{N≥1}N^{−1/2}τ_{log N}F₁ =: 𝔇F₁,  and ‖F₁‖² = ∫_λ^∞|u|²
= ½‖u‖²_{L²(|ξ|>λ)}.
*Proof.* F₁(x − log N) = e^{−(x−log N)/2}u(Ne^{−x}) = N^{1/2}F_N(x); x − log N < −T whenever x < −T. The norm: substitute
ξ = e^{−x}. ∎
Consequence. The whole tail form is a quadratic form in the single function F₁ ∈ L²(−∞, −T); after the translation x ↦ x + T
it is T-free: 𝔇 and the full comb do not see T. All T-dependence of the high block sits in (i) the constraint functionals,
(ii) the class of F₁ that arise from f supported in [−λ, λ], (iii) the truncation K. (This is the tail-variable form of the
"universal frame" of DOSSIER §7.1, recorded there for the exterior form; it is used, not reclaimed.)

### Lemma 2.2 (first Poisson cell; PROVED)
If u vanishes outside λ < |ξ| < 2λ, then F₁ is supported in [−T − log 2, −T], 𝒯u = F₁, F_N = 0 for N ≥ 2, every comb term
⟨τ_{log m}𝒯u, 𝒯u⟩ (m ≥ 2) vanishes, and 𝒲[𝒯u] = 𝒜_∞[F₁] = (1/2π)∫m|F̂₁|².
*Proof.* For N ≥ 2 and x < −T, Ne^{−x} > 2λ. τ_{log m}F₁ is supported in [−T − log 2 + log m, −T + log m], which meets
[−T − log 2, −T] in at most one point for m ≥ 2. ∎
So the piece that carries the drift (§1.3(a)) is exactly the archimedean form of a function on an interval of length log 2.

### Lemma 2.3 (the complete tail form; CITED + NUMERICAL check)
For admissible f, W_T(Ef) = 𝒲[Ψ_f] + 2A(Ψ_f)B(Ψ_f), Ψ_f = 𝒯(ℱf|_{|ξ|>λ}) (half-line identity with the complete form,
DOSSIER §7.1; 12B Theorem 1.1 is its polarisation). On the bottom vectors of X the polar part is ≤ 10⁻⁶ (|A(𝒯u)|,
|B(𝒯u)| ≤ 1.3·10⁻³), which is why 15A could omit it. It is NOT negligible in general: on an explicit admissible probe
(§3.3, f = smooth truncation of ℱ^{−1} of a three-cell tail, f(0) = ∫f = f(λ) = A(Ef) = B(Ef) = 0 imposed exactly),
x-space Lévy form on Ψ_f (comb m < e^5): 𝒲[Ψ_f] = −0.05775, A = 0.06099, B = 0.47890, 𝒲 + 2AB = 0.00066, against
a_T(Ef) = 0.00066 computed on the window directly. NUMERICAL confirmation of the identity to 5 digits.

### Remark 2.4 (the jump at x = −T; PROVED bound, not needed)
J := (𝒯u)(−T⁻) = Σ_N F_N(−T) = λ^{1/2}Σ_N u(Nλ); in the cell case J = λ^{1/2}u(λ).
For F = J·1_{x<−T}e^{β(x+T)} + (continuous part), the jump part of 𝒜_∞ is J²(1/2π)∫m(τ)(β² + τ²)^{−1}dτ = O(J²log β/β); with
β ≍ c (the turning frequency of the first chirp) it is O(J²·log c/c) (ARGUED for the choice of β; the formula itself is exact). Measured J² ≤ 2·10⁻⁴: the jump contributes < 10⁻⁵.
Since the drift is not the jump, no finite-dimensional boundary trace is needed.

## 3. The limit problem and the normalisation (NUMERICAL + ARGUED)

### 3.1 Idealised cell problems
By Lemma 2.1 the K → ∞ high block is the complete tail form Q[F₁] := 𝒲[𝔇F₁] + 2A(𝔇F₁)B(𝔇F₁) on F₁ arising from admissible
f, against ‖u‖² = 2‖F₁‖² (D-units: ×λ, §1.2). Idealisation (ARGUED): confine u to the first R − 1 cells λ < ξ < Rλ (F₁ on a
window of length log R), neglect the in-band part of ℱf, and transport the admissibility functionals to F₁ through
f ≈ ℱ^{−1}u: f(0) = 2∫u, f(λ) = 2∫u cos 2πλξ, A(Ef) = Σ_n n^{−1}∫_{ne^{−T}}^{min(ne^T, λ)}f, B(Ef) = Σ_n∫f(y)dy/y over the same
ranges (each a continuous functional of F₁). Galerkin: sine basis on the window (Nb = 32 … 96), Lévy-form Arch and comb Π of
tools/galerkin_mp.py composed with the matrix of 𝔇; tools tools/tail_direct/cellR.py, cellRp.py (checked against the x-space
Lévy form and the corrected chirp ledger: −0.0554 by all three at R = 3 without the polar term).
| R (window log R) | no constraint | f(0) = 0 | all four | D-unit value (λ/2)μ |
|---|---|---|---|---|
| without the polar term |  |  |  |  |
| 2 | −1.273 | 0.082 | 0.549 | 0.611 |
| 3 | −3.641 | −0.070 | −0.055 | −0.061 |
| 4 | −6.76 | −0.162 | −0.144 | −0.160 |
| 8 | −23.8 | −0.618 | −0.591 | −0.658 |
| with the polar term 2AB (the correct form, Lemma 2.3) |  |  |  |  |
| 2 | 0.001 | 0.082 | 0.549 | 0.611 |
| 3 | 0.000 | 0.000 | 0.001 | 0.002 |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 |
(T = 0.8; the f(0)-constrained first-cell value converges in Nb as 0.0823/0.0776/0.0759/0.0751 at Nb = 32/64/96/128.)
Readings. (a) Without the polar term the idealised problem goes negative from R = 3 on; that is the omission of 2AB, not a
failure of anything: with 2AB restored every value is ≥ 0 to Galerkin accuracy, as Lemma 2.3 and the proved range of (★)
at T = 0.8 require. (b) With the polar term the idealised problem has near-null directions as soon as R ≥ 3: **in D-units
the limit problem has bottom 0** (ARGUED: the idealisation must be realised by high-block admissible data; §3.2 realises
it by an explicit admissible function, but not inside the high span).

### 3.2 Explicit admissible probes: the near-null directions are near-gauge
Probe: the bottom eigenfunction of the R-cell problem, u ↦ ℱ^{−1}u on [0, λ], times (1 − y²/λ²)³, plus a combination of
(1 − y²/λ²)³(y/λ)^{2j}, j = 0 … 3, solving f(0) = ∫f = A(Ef) = B(Ef) = 0 exactly (f(λ) = 0 by the cutoff). Window side by
the x-space Lévy form on Ef; leakage side: D = 2∫_λ^∞|ℱf|², ℓ_g = 2 dist²(ℱf|_{(λ,∞)}, span of the tails of the gauge
functions (1 − λ²y²)³(λy)^{2j}, j ≤ 30, |y| < 1/λ, with ∫φ = 0) (tools/tail_direct/adm.py, lg.py, ident.py).
| probe | ‖f‖² | mass in |y| < 1/λ | ‖Ef‖² | a_T(Ef) | a_T/‖Ef‖² | λa_T/D | λa_T/ℓ_g |
|---|---|---|---|---|---|---|---|
| R = 2 | 1.351 | 0.416 | 0.3847 | 0.3067 | 0.797 | 0.548 | 1.001 |
| R = 3 | 1.882 | 1.880 | 0.00086 | 0.00066 | 0.773 | 0.0008 | 1.416 |
| R = 8 | 1.943 | 1.934 | 0.00371 | 0.00468 | 1.260 | 0.0054 | 1.433 |
Gauge-rank dependence of the last column (J = 15/30/45 gauge polynomials): R = 2: 0.902/1.001/1.075; R = 3: 1.284/1.416/1.440.
It increases with J (ℓ_g decreases as the gauge span grows) and is converging; the values are lower bounds for J = ∞ in
the direction that matters (a larger gauge only raises λa_T/ℓ_g).
Readings. (a) The near-null directions of the limit problem are realised by admissible f that live almost entirely in
the gauge region |y| < 1/λ: Ef is tiny, the window Rayleigh quotient is healthy (0.77–1.26), and the smallness is entirely
the transfer factor ‖Ef‖²/‖f‖². In D-units these give 0.0008 and 0.0054. (b) In the gauge-quotient metric ℓ_g the same
functions give 1.42–1.43, and the first-cell probe gives 1.00. (c) The gauge G_T is infinite-dimensional; the quotient X of
15A removes only its first 10 (MIN = 12) or 22 (MIN = 24) directions. As K grows, the high span resolves functions
supported in |y| < 1/λ to higher order, so near-gauge directions outside any fixed finite gauge quotient enter X.
Consequence (ARGUED, with the NUMERICAL probes as witnesses): **the D-unit bottom on X tends to 0 as K → ∞** — the high
block genuinely degenerates in D-units, and the degeneration is gauge leakage, not a sign defect.

### 3.3 The gauge-rank control
Rerun of tools/prolate_tailgram.py at T = 0.8, Nb = 300 with MIN = 24 (gauge rank 22) instead of 12 (rank 10):
| K | D on X, rank 10 (dim X) | D on X, rank 22 (dim X) | ℓ_g-bottom, rank 10 | ℓ_g-bottom, rank 22 |
|---|---|---|---|---|
| 80 | 1.764 (16) | 3.335 (4) | 0.838 | 0.877 |
| 88 | 1.634 (20) | 2.894 (8) | 0.799 | 0.834 |
The D-bottom on X depends on the gauge rank at fixed K (1.63 → 2.89): it is not a property of the form. The ℓ_g-bottom moves
by 0.04 between ranks 10 and 22: it is (nearly) converged in the gauge rank, and it is the only one of the 15A quantities
that is intrinsic. On the resolved range it still decreases with K (rank 22: 0.877 → 0.834 from K = 80 to 88; rank 10:
1.067, 0.987, 0.870, 0.838, 0.799 for K = 56 … 88).

## 4. Decision on the floor and the correct normalisation

(i) **D-units: no floor (ARGUED, two independent NUMERICAL witnesses).** The limit problem of Lemma 2.1 with the complete
form has near-null directions (§3.1, R ≥ 3), and they are realised by explicit admissible f concentrated in the gauge
region with D-unit Rayleigh quotient 0.0008 and 0.0054 (§3.2). The X-quotient removes a fixed finite part of an
infinite-dimensional gauge; its D-bottom depends on the gauge rank at fixed K (1.63 vs 2.89 at K = 88, §3.3). Hence a
statement "𝒢 ≥ κD on the high block, κ independent of K" is false in the limit; the drift of 15A §1.2 in D-units is genuine
and its end point is 0, reached through two stages that the data separate: first the first-cell archimedean drift
(⟨m⟩₁ ↓, §1.3; idealised first-cell limit (λ/2)·0.549 = 0.61 with all four constraints), then near-gauge leakage (§3.2),
which at Nb = 300 is not yet resolved inside the high span (the measured bottom functions have < 10⁻³ of their mass in
|y| < 1/λ for K ≤ 88).
(ii) **The correct normalisation is the full gauge-quotient leakage ℓ_g** (gauge closure Ḡ_T, not a finite rank). In it:
ℓ_g-bottom at K = 88 is 0.80 (rank 10) / 0.83 (rank 22); the near-gauge probes give 1.28–1.44; the first-cell probe gives
0.90–1.08. So the statement to prove is
    (HR_g)  𝒢[b] ≥ κ_T·ℓ_g^S[b]  for every b ∈ S𝒜 supported on the high indices, every K,
with κ_T > 0 independent of K. NUMERICAL status at T = 0.8: every value seen is ≥ 0.80; the ℓ_g-bottom still decreases on
the resolved range (1.07, 0.99, 0.87, 0.84, 0.80 for K = 56 … 88; a + b/K through K = 72, 88 gives a ≈ 0.48). A positive
floor in ℓ_g is consistent with all data and is NOT shown; OPEN.
(iii) What the drift in ℓ_g is made of. Lemma 2.2 and §1.3 say it is the archimedean form of the first cell: for a
function on an interval of length log 2 subject to the transported constraints (f(0) = 0 alone already lifts the bottom
from −1.27 to +0.075; all four give 0.549). The first-cell problem is therefore a finite, Λ-free, explicit problem whose
value bounds the first stage of the drift; in D-units it is 0.61, in ℓ_g-units ≈ 1.0 (probe).
(iv) The task alternative "a K-dependent weight": not needed. The degeneration is gauge leakage, which ℓ_g removes; no
weight in K reproduces it (the near-gauge directions have D-unit values ≈ 10⁻³ at every K large enough to resolve them).

## 5. Falsifier test
Lemmas 2.1, 2.2 and Remark 2.4 are Λ-free identities (dilation, support, Fourier). Lemma 2.3 is CITED (complete-form
half-line identity); under (a) cΛ, (b) a_P, (d) finite modifications it acquires the window term of 12B §3 and is not an
identity of the same shape; under (c) there is no tail map. The attribution of §1.3 locates the drift in B₁₁ = 𝒜_∞[F₁],
whose comb weight is 2 log 1 = 0: the drifting piece is literally the same number under (a), (b), (d). The near-gauge
degeneration of §3.2 is a property of the transfer f ↦ Ef (Ef ≈ 0 on functions supported near 0), also weight-blind.
Hence nothing in this round distinguishes Λ from its falsifiers; by rule 4 nothing here is a sign step, and none is
claimed. NUMERICAL: no falsifier runs (no sign claim to test).

## Result
PIVOT with reason, plus PROVED bookkeeping and a settled attribution.
- PROVED: Lemma 2.1 (dilation form: F_N = N^{−1/2}τ_{log N}F₁, the tail form is a T-free form in F₁); Lemma 2.2 (first
  Poisson cell: no comb, 𝒲 = 𝒜_∞[F₁] on a window of length log 2); Remark 2.4 (jump part formula).
- CITED + NUMERICAL: Lemma 2.3 (complete tail form W_T(Ef) = 𝒲[Ψ_f] + 2A(Ψ_f)B(Ψ_f), checked to 5 digits on a probe with
  nonzero polar term; the polar term is ≤ 10⁻⁶ on the X-bottom vectors, so 15A's numbers stand).
- NUMERICAL: direct tails reproduce the Galerkin bottoms (Galerkin D-unit = λ·a_T(Ef)/‖f‖², three methods agree; the
  K = 96 row is confirmed as a Galerkin-cap artifact). The drift is 100% the first chirp B₁₁ = ½⟨m⟩₁ (purely archimedean,
  comb weight 0): not the jump (J² ≤ 2·10⁻⁴), not the non-resonant pairs (≤ 5%, X_eff ≈ 1, MV regime never entered), not
  the resonant comb. Idealised cell problems: first cell 0.549 (all constraints; D-unit 0.61); with ≥ 2 cells the
  complete form has near-null directions. Admissible near-gauge probes: D-unit 0.0008–0.0054, ℓ_g-unit 1.28–1.44.
  Gauge-rank control: D on X depends on the rank (1.63 vs 2.89 at K = 88), ℓ_g does not (0.80 vs 0.83).
- ARGUED: the high block degenerates in D-units as K → ∞ (gauge leakage through an infinite-dimensional gauge); (HR) must
  be stated in ℓ_g (HR_g); its floor is OPEN (all values ≥ 0.80, still decreasing slowly).
Pivot reason: the D-unit question is answered (no floor, by gauge leakage); the live question moves to (HR_g), whose
drift is the archimedean first-cell problem.

### What was proved
Lemma 2.1, Lemma 2.2, Remark 2.4 (complete proofs above). The identity of Lemma 2.3 is cited and numerically confirmed.

### What failed and why
- "The drift is the jump at x = −T": false; J² ≤ 2·10⁻⁴.
- "The drift is the non-resonant off-diagonal (MV sharpness)": false; the bottom vectors carry one chirp (X_eff ≈ 1), the
  off-diagonal is ≤ 5% and of both signs.
- A K-uniform floor in D-units: false in the limit (ARGUED with explicit witnesses); D is the wrong metric.
- The idealised limit problem without the polar term is negative from two cells on: the omission of 2A(Ψ)B(Ψ), recorded
  so that no later round drops it.
- A coarse m(τ) table near τ = 0 in the first version of the ledger (corrected; high-block numbers unaffected to 10⁻³).

### Next concrete step
Prove the first-cell bound: for F supported in an interval of length log 2 and orthogonal to the transported functionals
(f(0), f(λ), A(Ef), B(Ef)), 𝒜_∞[F] ≥ μ‖F‖² with an explicit μ > 0 (numerically 0.549 at T = 0.8; already 0.075 from
f(0) alone, T-independent), by the Lévy form on a short interval (one negative direction of 𝒜_∞ on length log 2, lifted by
the single functional f(0) = ∫F e^{−x/2}·const); then compute the ℓ_g-bottom with the gauge closure resolved (MIN ≥ 30,
Nb ≥ 370, K ≤ 100 at T = 1.0) to decide whether the ℓ_g drift stops at the first-cell value.

## Reproducibility
python3 tools/tail_direct/coef.py; SAVE=t08.npz TOP=96 TOPS=56,64,72,80,88 FASTMUL=1 python3 tools/prolate_tailgram.py
0.8 300 30 120 12 (and MIN = 24 for §3.3); NPZ=t08.npz python3 tools/tail_direct/run2.py; NPZ=t08.npz python3 tools/tail_direct/efx.py;
from tools/: python3 tail_direct/cellRp.py R Nb 0.8 {0,1}; python3 tail_direct/ident.py 3 48 3; JG=15|30|45 python3
tail_direct/lg.py R Nb 3. Every run ≤ 15 min on one core.
