# PROOF_L_SHARP_V_001 — Strategy V: Fourier-sector reduction of L′♯ and the remainder form of each sector

Phase 199, prover memo (pen and paper; one NUMÉRICO check on existing MORI15 data, script `PROOF_L_SHARP_V_001_check.py`).
Target: Lemma L′♯ = (★★). , no zero location
is used,

**Outcome in one line.** L′♯ NOT proved. (V.1) The requested equivalence L′♯ ⟺ (L′♯_+ ∧ L′♯_−) is **NO-GO as posed** (sector
data are not carrier data, ℓ does not split, and at μ = 15 each sector form is O(1)-cancelled to the double floor); the constraint
check is corrected (on ε = −1 the constraint is NOT automatic). (V.2, PROVED) each sector form is a **pairing of the
autocorrelation with the classical prime remainder**: 𝒲_refl[u] = ∫_0^∞ e^{−t/2}(u∗u)(t) dR_Λ(t), R_Λ(t) = ψ(e^t) − e^t + ½log(1−e^{−2t});
in particular **𝒫 ≠ correction: its PNT main term is exactly A²**. (V.3, PROVED) the sampling route |H(1)|² ≲ Σ_{j≥1}|H(−2j)|² is
NO-GO with any polynomial (indeed any sub-exponential) loss on the free half-line class. (V.4, NUMÉRICO) on g*:
𝒫 − A² = −Σ_{j≥1}L_j² to 12 digits. No sign is claimed. (★★) OPEN; row D OPEN.

## 0. Corpus / index check and why this is not a retry
Index read: README entries T_001, U_001, AUDIT_L_SHARP_5, MORI15_EXTREMAL_001, A_001; 04_PHASES l.755/764 (images, Toeplitz–Hankel);
l.208 (reflection between places). Why new: (a) T/U wrote the sector form as SOS + 𝒫 − A² and left 𝒫 "indefinite"; nobody
recombined 𝒫 − A² + Σ_{j≥1}L_j² into a single Stieltjes pairing against R_Λ, which shows that the sign question per sector is a
weighted prime-remainder question on an autocorrelation (V.2) and kills the sampling reading (V.3). (b) No memo tested the
sector split against the extremal (V.4). Not a retry of "explicit formula as sign source": no sign is extracted from V.2.

## 1. (i) The sector reduction — what is true
Notation of U_001 §1 (window I = (−a,a), a = T, ǧ(s) = g(−a+s), Ψ̌(s) = Ψ_f(−a−s), u_± = ǧ ± Ψ̌).
**V.1.1 (constraints; PROVED, corrects the brief).** If f̂ = εf (any of 𝔉, 𝔉_μ), then f̂(0) = εf(0); so {f(0) = 0, f̂(0) = 0}
collapses to the single constraint f(0) = 0 **in both sectors**. It is NOT automatic for ε = −1: f̂(0) = −f(0) is consistent with
f(0) ≠ 0 (e.g. Hermite h₂: ĥ₂ = −h₂, h₂(0) ≠ 0; prolate ψ₂ likewise). MORI15's remark "anti-self-dual would break
f̂(0) = 0" is the same fact: on ε = −1 one constraint f(0) = 0 must still be imposed.
**V.1.2 (exact split; PROVED = U.1.3 + T Prop 3.3).** W_T(g) = Q_+ + Q_−, Q_ε := ε·¼𝒲_refl[u_ε], 𝔔-orthogonal.
**V.1.3 (NO-GO as posed: λ_A ≠ min(λ_+,λ_−)).** Three independent obstructions, all PROVED:
 (a) the sectors f_± = (f ± 𝔉_μ f)/2 are never carrier data (f_− ≠ 0 by Paley–Wiener, U.1.2; f_+ is not compactly supported for
 the same reason), so "λ_ε = inf over carrier ∩ sector" is an infimum over {0};
 (b) ℓ(g) = λ‖Πρ‖² (U.2.1) is a gauge distance of the whole datum; there is no decomposition ℓ = ℓ_+ + ℓ_− compatible with
 V.1.2 (Π𝒞_μ ⊂ 𝒱_μ is not 𝔉-stable, U.2.1(c)); the natural sector norms ‖u_±‖² are O(‖g‖²) while ℓ = O(10^{−70}) at μ = 15;
 (c) consequently any sector lemma "Q_ε ≥ c·N(u_ε)" with N(u) ≥ c′‖u‖² and c, c′ > 0 fixed is FALSE at the μ = 15
 extremal: ‖u_±‖² ≈ ‖g*‖² = 1, while |Q_ε| < 10^{−12} (V.4; Q_ε = ±½X + ¼𝒲_refl[ǧ] + ¼𝒲_refl[Ψ̌], X := cross term).
What survives: **sufficiency only** — if Q_ε ≥ κ_ε ℓ_ε with ℓ_+ + ℓ_− ≥ ℓ then L′♯ holds; no admissible (ℓ_+,ℓ_−) is known. The
two sector statements the brief asks for, stated exactly (signs checked against U.1.3):
 (+) Σ_{j≥1}L_j(u_+)² + 𝒫[u_+] − A(u_+)² ≥ 4κμ^{−A}ℓ_+;   (−) A(u_−)² − Σ_{j≥1}L_j(u_−)² − 𝒫[u_−] ≥ 4κμ^{−A}ℓ_−.
**V.1.4 (standard 𝔉 vs window parity; PROVED from T Lemma 1.1).** In A_001 coordinates Φ_{f̂} = Φ_f∘R with R: x ↦ −x the
*window-centre* reflection (given f(0) = f̂(0) = 0). Hence for g in the even window sector, Φ_{(f−f̂)/2}|_I = 0: the standard-𝔉
minus sector carries no window content; it only contributes the exterior identity 𝒲[Ψ] = 𝒲(Ψ, RΨ) (radical applied to
Φ_{f_−} = ½(Ψ − RΨ)). The near self-duality of f* observed in MORI15 (‖f_−‖²/‖f‖² ≈ 5·10^{−72}) is therefore the window-parity
of g* transported by Lemma 1.1, up to the out-of-band tail r* (ARGUED: the band part of f̂* − f* is fixed by Φ_{r*} on I through
the Möbius map; quantitative bound not written). Correction to T §4: for the unscaled 𝔉 in A_001 coordinates the window parity
and 𝔉 ARE the same involution on Φ (T §4 used ρ-units, where R is the edge reflection).

## 2. (ii) The (+) sector: remainder form (PROVED) and the sampling NO-GO
For u on (0,∞) with u(s) = O(e^{−(½+δ)s}) put φ := u∗u, φ(t) = ∫_0^t u(r)u(t−r)dr.
**Theorem V.2.1 (PROVED).** 𝒲_refl[u] = ∫_0^∞ e^{−t/2}φ(t) dR_Λ(t), R_Λ(t) := ψ(e^t) − e^t + ½log(1−e^{−2t}).
*Proof.* (1) A(u)² = ∫∫u(r)u(r′)e^{(r+r′)/2} = ∫_0^∞φ(t)e^{t/2}dt = ∫e^{−t/2}φ d(e^t). (2) Σ_{j≥1}L_j² = ∫φ(t)ν₁(t)dt,
ν₁(t) = Σ_{j≥1}e^{−(2j+½)t} = e^{−t/2}·(d/dt)½log(1−e^{−2t}). (3) 𝒫 = Σ_qΛ(q)q^{−½}φ(log q) = ∫e^{−t/2}φ dψ(e^t). Sum. □
Bilinear form (polarise U.1.3): **W_T(g) = ∫_0^∞ e^{−t/2}(ǧ∗Ψ̌)(t) dR_Λ(t)** (PROVED).
**Consequences.**
- The pole term and the prime term are not independent: the main term of dψ(e^t) is d(e^t), which reproduces A² exactly.
  𝒫 is not a correction to a sampling inequality; it *is* A² + (remainder). Self-duality relation asked for in (ii): on the full
  line, ∫Φ_{f_ε}e^{(s−½)x}dx = ζ(s)M_{f_ε}(s) and the R_a-symmetry gives H(s) + εH(1−s) = 2e^{a(s−½)}ζ(s)M_{f_ε}(s)
  (H(s) := ∫_0^∞u_ε e^{(s−½)t}dt; PROVED, Lemma U.1.1 + Mellin), so A = H(1) = −εH(0) + 2e^{a/2}M′_{f_ε}(1) (pole cancelled by
  f_ε(0) = 0) and H(−2j) = −εH(1+2j) + 2e^{−a(2j+½)}ζ′(−2j)·Res_{s=−2j}M_{f_ε}. These tie A, L_j to the Tate data of f_ε but
  are restatements (REF-D), no inequality follows.
- **(+) in remainder form:** ∫e^{−t/2}(u_+∗u_+)dR_Λ ≥ 4κμ^{−A}ℓ_+; **(−):** ∫e^{−t/2}(u_−∗u_−)dR_Λ ≤ −4κμ^{−A}ℓ_−. Per sector the
  sign is a sign of a smoothed prime remainder against a non-positive-definite weight (φ = u∗u is a half-line autocorrelation,
  not a positive-definite function).
**Proposition V.2.2 (sampling NO-GO; PROVED).** On the free class {u ∈ C_c(0,∞)} there is no inequality
|A(u)|² ≤ C(X)Σ_{j≥1}L_j(u)² with C(X) sub-exponential in the support length X. *Proof.* u = bump of width 1 at X:
A² ≍ e^{X}, Σ_{j≥1}L_j² ≍ e^{−5X}; ratio ≍ e^{6X}. □ (Müntz–Szász gives uniqueness — {e^{−(2j+½)t}}_{j≥1} is complete in
L²(0,∞) since Σ1/j = ∞, CITED — but A is unbounded with respect to (L_j); uniqueness ≠ stability.) The same bump shows the loss
must be compensated by 𝒫, whose main term is A² (V.2.1): the inequality is a cancellation, not a sampling bound. Whether the
carrier/sector constraint (u_± = ǧ ± Ψ̌, ǧ supported in (0,2a)) restores a polynomial constant: OPEN.
**Falsifiers.** cΛ: R_{cΛ} = cψ − e^t + …, so 𝒲_refl,c[u] = c𝒲_refl[u] + (c−1)(A² − Σ_{j≥1}L_j²) and W_{T,c}(g) =
cW_T(g) + (c−1)(A(ǧ)A(Ψ̌) − ΣL_j(ǧ)L_j(Ψ̌)) (PROVED algebra; note U.1.3 itself also needs c = 1). The main-term cancellation is
pinned at c = 1. a_P: R changes by Σ(a_P−1)-weighted prime powers; main term preserved iff the density is preserved — the
mechanism isolates Λ only through PNT-level density plus the exact remainder (ARGUED).

## 3. (iii) The (−) sector
By V.2.1, (−) requires the remainder pairing on u_− to be strictly negative by at least Σ_{j≥1}L_j(u_−)² + 4κμ^{−A}ℓ_−: there
the pole (A²) must beat 𝒫 + SOS, i.e. the smoothed remainder must be negative. No mechanism found; OPEN. By V.1.3 it is in any
case not a standalone lemma for L′♯.

## 4. (iv) MORI15 check (NUMÉRICO, double precision, `PROOF_L_SHARP_V_001_check.py`)
g* from `p0_eig.json` (832 even Legendre modes, a = ½log15), ǧ(s) = g*(−a+s), q ≤ e^{4a} = 225:
A(ǧ)² = 2.941528007, 𝒫[ǧ] = 2.940388871, Σ_{j≥1}L_j(ǧ)² = 1.1391·10^{−3}, B = −0.44283;
**𝒲_refl[ǧ*] = 3.8·10^{−13}** (double floor), i.e. 𝒫 − A² = −Σ_{j≥1}L_j² to 12 digits.
Reading: 𝒲_refl[ǧ] = −𝒲(g, g∘R_a) = −𝒲(g, τ_{2a}g) (g even) — the Weil correlation of g* at shift 2a, which is tiny together
with W_T(g*) (consistency only: Cauchy–Schwarz would bound it by W_T if the form were PSD on span{g,τ_{2a}g}; not used).
Since ‖Ψ̌*‖ ~ 10^{−35}, Q_± = ¼𝒲_refl[ǧ*] ± ½X + O(10^{−70}): **both sector values sit at ±½X below the double floor; which
sector is tight cannot be decided in double precision** (needs arb at ≥ 250 bits on Ψ̌*; not run). What is decided: the O(1)
pieces 𝒫 ≈ A² ≈ 2.94 cancel in each sector; the SOS Σ_{j≥1}L_j² = 1.1·10^{−3} is exactly matched by the prime remainder.

## 5. Residual (exact) and labels
**(★★_V)** ∀μ ≥ 5, on carrier data: ∫_0^∞ e^{−t/2}(ǧ∗Ψ̌)(t) dR_Λ(t) ≥ κμ^{−A}ℓ(g) — the bilinear remainder pairing of the window
datum with its exterior image. Equivalent to (★★) (PROVED identity, REF-D).
**Do not retry:** sector-wise lemmas for L′♯ (V.1.3); sampling at trivial-zero nodes with 𝒫 as perturbation (V.2.2);
treating 𝒫 and A² as independent pieces (V.2.1).
| item | label |
|---|---|
| V.1.1 constraint collapse (both sectors; not automatic on ε = −1) | PROVED |
| V.1.2 exact split W_T = Q_+ + Q_− | PROVED (U.1.3) |
| V.1.3 L′♯ ⟺ L′♯_+ ∧ L′♯_− | NO-GO as posed; sufficiency only |
| V.1.4 standard 𝔉 = window-centre reflection; f* self-duality = parity of g* | PROVED / ARGUED (tail bound) |
| V.2.1 remainder form 𝒲_refl[u] = ∫e^{−t/2}u∗u dR_Λ; W_T = ∫e^{−t/2}ǧ∗Ψ̌ dR_Λ | PROVED (REF-D) |
| H(s)+εH(1−s) relation | PROVED (restatement) |
| V.2.2 sampling route | NO-GO (free class); carrier-restricted OPEN |
| cΛ formula | PROVED algebra |
| V.4 𝒲_refl[ǧ*] ≈ 0, 𝒫 − A² = −ΣL_j² | NUMÉRICO |
| (+), (−), (★★_V), L′♯ | OPEN |
No sign is claimed. Row D OPEN.
