# IV.1 — Identification of `Â_∞`: second-order Sturm–Liouville operator (oscillation) Consolidation of E13/E14/E15 (my mpmath runs) + the analytic front (IV1star-relative-gap).
The naive "Dirichlet Laplacian" identification was refuted; the correct one is **the
Sturm–Liouville / oscillation class**, with boundary carrier. Connects IV.1 with H1 (positivity). Markers: **[N]** robust numerical · **[P]** proved · **[GAP]** named residual. --- ## Solid facts (E13/E14/E15, λ=7,9,11, mpmath dps=30) 1. **[N] The carrier is the discrete band edge, exact:** `ω* = 2πN/(2N+1)` (measured by FFT of the fundamental): `0.966π`(N=14), `0.970π`(N=16), `0.973π`(N=18) = `2N/(2N+1)·π` exact. **Not `π`** (Nyquist) — hence the failure of de-modulating by `(−1)^j` in E12.
2. **[N] Nodeless ground state after de-modulating by `ω*`:** `0` sign changes, ∀λ. **Recovers the Perron–Frobenius of H1** (the raw `v_0` has ~`N` sign changes = the carrier; once removed correctly, it is positive). The similarity that makes `QW` positivity-preserving is `D=diag(e^{iω*j})` (boundary carrier).
3. **[N] Alternating parity `(−1)^k`:** modes `k=0,1,2,3,…` are `EVEN, ODD, EVEN, ODD,…` (E15, clean ∀λ). **Unambiguous signature of a second-order operator** (eigenfunctions of a symmetric Sturm–Liouville operator alternate parity). Matches the analytic reduction `ε_1/ε_0 = μ_O/μ_E` (odd over even lowest) from the IV1★ front.
4. **[N] Sturmian envelopes** (analytic de-mod, E14, λ=7): even modes `k=0,2,4,6` → `0,2,4,6` nodes. (Noisier at larger λ due to even/odd mixing and Hilbert phase; the even pattern is clean.) Consistent with oscillation (`v_n` has `n` nodes).
5. **[N] Solid `n²` spectrum:** `ε_k/ε_0 → (k+1)²` (λ=11: 4.02, 9.0, 16.1, 25.2, 36.5, 49.8). ## What `Â_∞` is NOT (refuted by overlaps) - **NOT** the constant-coefficient Laplacian (Dirichlet): node count correct but **shape not sinusoidal** (overlap with `sin((k+1)π·)` only 0.1–0.6). Variable coefficients.
- **NOT** Hermite/harmonic oscillator (overlap ≤ 0.40).
- **NOT** prolate/DPSS (overlap ≈ 0.00). ## Identification [N→P via H1] > **`Â_∞` is a second-order Sturm–Liouville operator (oscillation matrix,
> Gantmacher–Krein), in the representation de-modulated by the boundary carrier `ω*`:**
> - eigenfunctions of alternating parity `(−1)^k`, nodeless fundamental, `v_n` with `n`
> nodes (Sturmian);
> - spectrum `ε_n ∝ n²` (Weyl law for second-order operators);
> - **variable coefficients** (fixed by the archimedean data `θ'` + arithmetic `Λ(n)`),
> that is why it is NOT the constant-coefficient Laplacian. **Why it is second-order / oscillation — the rigorous route (connects with E1):**
H1 proved that `e^{−tQW}` is **positivity-preserving** (because `Λ(n)≥0`, via
Lévy–Khintchine + Schoenberg + Trotter). In the de-modulated representation `D⁻¹QW D`
(`D=diag(e^{iω*j})`), this is the **total oscillation property** (Gantmacher–Krein):
an oscillation matrix has simple eigenvalues `0<λ_1<λ_2<…` and the eigenfunction of `λ_k`
has exactly `k−1` sign changes (Sturm), with alternating parity. **That is
exactly what is measured** (parity `(−1)^k`, nodeless fundamental, Sturmian functions). **[residual GAP-IV.1]** Prove that `D⁻¹QW D` is **genuinely** an oscillation
matrix (total non-negativity of the minors, Gantmacher–Krein) **from H1** — H1 gives
positivity-preservation (Perron–Frobenius, controls the fundamental); total non-negativity
(which controls the ENTIRE Sturm order) is a stronger step, to be derived from the
Loewner structure of `sin` (§II) + the sign `Λ(n)≥0`. It is the **same positivity of H1
raised from "fundamental" to "all modes"**. ## Cross impact on IV.1★ (relative gap) The identification **gives `γ` directly**: if `Â_∞` is second order with spectrum `n²`, then
``` ε_1/ε_0 → 2²/1² = 4 ⟹ γ = 3 > 0.
```
And `ε_1/ε_0 = μ_O/μ_E` (odd/even) confirmed by parity alternation (E15). Thus
**IV.1 and IV.1★ close together** modulo the single residual: that the oscillation
(Gantmacher–Krein) follows from H1. The `n²` law is no longer mysterious — it is **Weyl for the
oscillation operator**, and `γ=3` is `2²/1²`. ## Status after the identification | Sub-piece | Status |
|---|---|
| carrier = edge `2πN/(2N+1)` | **[N]** solid |
| nodeless fundamental (de-mod) = H1 | **[N]+[P]** (H1 proved) |
| alternating parity `(−1)^k` | **[N]** solid |
| spectrum `n²` (Weyl) | **[N]** solid |
| Sturmian eigenfunctions `n` nodes | **[N]** (even clean; odd noisy) |
| **`Â_∞` = second-order Sturm–Liouville / oscillation** | **[N→P]** modulo Gantmacher–Krein |
| **IV.1★ `γ=3>0`** | **follows** from the identification |
| **single residual** | **prove oscillation (Gantmacher–Krein) from H1 (`Λ≥0`)** | **Verdict:** IV.1 **identified** (Sturm–Liouville/oscillation class, not a named
constant-coefficient operator), `n²`=Weyl, `γ=3` as a bonus for IV.1★. One residual
remains, and it belongs to the H1 family (total positivity): raising "positivity-preservation
of the fundamental" to "total oscillation of the whole spectrum". Much more concrete and
connected than "identify a mysterious operator". --- ## IV.1-res attacked: Gantmacher–Krein route REFUTED (E16) I tested whether `B = D·QW·D` (`D=diag((−1)^j)`, real de-modulation) is an **oscillation
matrix** (total non-negativity ⟹ Sturmian by Gantmacher–Krein). **It is NOT** (E16, λ=7,9):
- entries `≥0` only **50%** of the time (mixed signs);
- immediate off-diagonals `B[i,i+1]` **negative** (min `−0.66`, `−0.90`) — fails the oscillation requirement;
- **15–22% of consecutive 2×2 minors `<0`** — violates TN. **Consequence:** the Sturmian structure **does NOT come from total matrix positivity**
(Gantmacher–Krein). H1 gives positivity-preservation (order 1 = Perron–Frobenius of the
fundamental); total non-negativity (full order) **is strictly stronger and
FALSE here**. The "soft IV.1-res via H1→TN" route is **closed as false**. **Where the Sturmian character (parity `(−1)^k`, nodeless fundamental, envelopes with
`n` nodes) actually comes from:** the **second-order differential (Sturm–Liouville)
structure** of the *boundary operator* governing the low spectrum of the frame at critical
density — the operator of the prolate *plunge* / boundary layer (cf. Note IV.1★: "boundary-layer
edge operator"). Sturm oscillation is a theorem for second-order ODEs, it does **not**
require matrix TN. ## Candid FINAL status of IV.1 **Identified (solid numerical):** `Â_∞` = **second-order Sturm–Liouville-type**
operator (boundary layer of the critical frame), boundary carrier `2πN/(2N+1)`, alternating
parity `(−1)^k`, nodeless fundamental (= H1), spectrum `n²` (Weyl), variable coefficients. NOT a
TN matrix, NOT Dirichlet/Hermite/standard-prolate. **Residual of IV.1 (not closed):**
> **IV.1-res' — Prove that the scaling limit `Â_∞` exists (Conj 2b) and that its low spectrum
> is that of a second-order Sturm–Liouville operator (boundary layer of the critical frame), with
> spectrum `n²` and gap `ε_1/ε_0 → 4` (γ=3).** It is **asymptotic analysis** (Toeplitz/Loewner limit + Landau–Widom boundary operator +
de Branges/Sturm–Liouville) — **hard but NOT RH-hard** (it is not §V; it does not depend on the
global sign of `Λ(n)`, only on the geometry of the frame at critical density). **Verdict:** IV.1 is **not fully closed**. One residual remains, `IV.1-res'`
(rigorous identification of the second-order boundary operator + existence of the scaling
limit), from the **approximation theory / Sturm–Liouville** family, not from the RH-hard
positivity §V. But IV.1 ended up **very well characterized**: we know WHAT `Â_∞` is (second-order
SL, n²=Weyl, γ=3), why the eigenvectors are not Dirichlet (variable coefficients), and why the TN
route fails. `n²` and `γ=3` are consequences of the SL structure, conditioned on `IV.1-res'`. --- ## IV.1b' attacked (collaborator's idea): SL confirmed QUALITATIVELY, constant coefficients REFUTED I attacked IV.1b' by potential reconstruction (E17) and by carrier×box fit (E18). Result: **Refuted — no CONSTANT-COEFFICIENT / uniform-basis identification:**
- E17 (V(x)=μ_k+φ_k''/φ_k common): residuals `0.45–0.87` (large), `V_k≈μ_k` (not common). *Confound:* carrier `32π/33` near Nyquist ⟹ envelope via Hilbert unreliable.
- E18 (v_k = carrier × box-mode_m): overlap `0.3–0.56`, best `m` erratic, `m=k+1` almost never. **NOT** a free Dirichlet box.
- Added to E12/E14 (not Dirichlet, not Hermite, not prolate) and E16 (not a TN matrix). **Confirmed — QUALITATIVE second order (the robust signature):**
- **Alternating parity `(−1)^k`** (E15, clean ∀λ) = decisive signature of a second-order operator.
- Spectrum `n²` (second-order Weyl), nodeless fundamental, Sturmian even modes. **Coherent reading:** `Â_∞` is a second-order Sturm–Liouville operator with **VARIABLE
COEFFICIENTS** `−(pφ')'+qφ=μwφ`. That explains EVERYTHING: the spectrum is `n²` (Weyl, robust
to the coordinate), parity alternates (symmetric SL), the fundamental is nodeless — BUT the
eigenfunctions, in the raw `j` coordinate, are **distorted box modes** (hence overlap ~0.5
spread across several `m`, and `V` in the `j` coordinate comes out non-constant/messy). The
constant-coefficient identifications fail **because the coefficients are variable**. **Refined residual IV.1-res'':**
> Identify the variable coefficients `(p,q,w)` of the limit SL (= the Liouville
> coordinate) via the continuum limit of the Loewner-against-archimedean-measure
> form (Conj 2b + asymptotics). HARD, **analysis** (not RH-hard). **What the chain needs is ALREADY qualitative:** "second order ⟹ `n²` Weyl ⟹ `ε_1/ε_0→4`,
`γ=3>0`". The `γ>0` rests on the second-order nature (alternating parity + Weyl), which
is robust; the EXACT identification of the operator (IV.1-res'') is refinement, it does not
block the qualitative `γ>0`. **Verdict IV.1 (candid, methodical):** IV.1-res' **not closed**. Further attacked, refined to:
(i) second-order SL **confirmed qualitatively** (parity + n² + nodeless); (ii) **variable**
coefficients (all constant-coefficient IDs refuted, with explanation); (iii) residual IV.1-res'' =
pin down `(p,q,w)`, pure analysis. `γ=3` for IV.1★ rests on (i). The limit of numerical
resolution (N≤20, near-Nyquist carrier) prevents pinning down (p,q,w) — would need large N
or an analytic attack on the boundary operator. --- ## Analytic closure of IV.1 (no Python) — final status **Proved [P]:** (A) `QW` commutes with parity `J:j↦−j` ⟹ even/odd sectors; alternation
`(−1)^k` = interlacing `ε_0^E<ε_0^O<ε_1^E<…`. (B) In the continuum, `QW_∞` is an integral
operator with **bounded Loewner kernel** ⟹ **compact** (eigenvalues accumulate at 0). **Not closed [analytic GAP]:** (C) by (B), the FULL operator is smoothing, NOT
differential — the second-order character lives in the **effective boundary-layer operator**
at the band edge `t=±Ω` after renormalizing `/ε_0~λ²` (measured carrier `2πN/(2N+1)`=edge confirms).
(D) deriving that boundary operator and its spectrum `n²` (Landau–Widom/semiclassical) was NOT
achieved: known profiles do not give `n²` (prolate plunge=logistic; oscillator=`2n+1`). The `n²`
remains numerically robust but analytically underived. **FINAL VERDICT IV.1:** proved = PSD + parity symmetry + compact Loewner form.
Phenomenological (not proved) = second order / `n²` / `γ=3`. IV.1 is ACCEPTED at this level
(methodical decision: do not force a theorem) and we move on to IV.2. The real residual of IV.1 is
**boundary-layer analysis of the critical frame** (Landau–Widom), NOT RH-hard, NOT §V.
