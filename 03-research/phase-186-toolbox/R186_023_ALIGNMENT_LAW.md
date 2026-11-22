# R186_023 — Alignment model: fragile archimedean mode + prime phases

**Script:** `r023_alignment.py` (scratchpad copy; uses `r183_030_inertia.build`). Form: E_{S(T)} = A_∞ + Σ_{n<e^{2T}} P_n over 𝒫_T (primitive constraint ∫ξe^{x/2}=0), L²(h) metric, basis ξ_j=(1−u²)²P_j(u), M = 24 and 32. c_h(log n) := −√n·P_n[h]/(2Λ(n)) (normalized autocorrelation). h_a := minimizer of A_∞ alone on 𝒫_T; M(T) := W[h_a] (single-mode model).

## Status
- **VERDICT: the single-mode alignment model is FALSIFIED (NUMERICAL).** M(T) does not track λ_min(T): error of 1 to 12 orders of magnitude. It does not predict a sign change in (0.8, 1.5): M(T) ∈ [0.011, 0.096] > 0 across the whole grid. The "prediction of negativity for T ≳ 1" (item 3b) **does not occur**: the premise that s(T) ≈ 4/T → 0 with all cosine phases → 1 is false (see below).
- What IS confirmed (NUMERICAL): (i) the minimizer h*_T is always **even** (parity +1.00 across the whole grid, with no switch to an odd or paired mode in [0.36, 1.5]); (ii) λ_min decays superexponentially; (iii) the primes switch from costing to paying in the archimedean mode after ≈0.57 (prime 2 helps: c_{h_a}(log 2) < 0).
- Alignment law: reformulated as a **finite-rank conjecture (CONJECTURE/OPEN)**, not a single-mode one; see §3.

## 1. Table (M = 32; M = 24 agrees to <5% up to T = 0.72, afterward only in order of magnitude)

| T | λ_min (E_S over 𝒫_T) | peak s | s·T | width | E_∞(h*) | P₂[h*] (c(log2)) | P₃[h*] | E_∞(h_a) | ⟨h_a,h*⟩ | M(T)=W[h_a] |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.36 | 4.79e-1 | 10.20 | 3.67 | 4.3 | +0.521 | −0.042 (+0.043) | — | +0.509 | 0.995 | 4.87e-1 |
| 0.42 | 1.44e-1 | 8.55 | 3.59 | 5.1 | +0.382 | −0.238 (+0.243) | — | +0.354 | 0.980 | 1.76e-1 |
| 0.48 | 2.64e-2 | 7.95 | 3.82 | 3.4 | +0.232 | −0.205 (+0.210) | — | +0.220 | 0.995 | 4.11e-2 |
| 0.54 | 1.47e-3 | 7.55 | 4.08 | 2.6 | +0.155 | −0.153 (+0.156) | — | +0.101 | 0.963 | 7.63e-2 |
| 0.60 | 6.97e-5 | 7.35 | 4.41 | 2.3 | +0.121 | −0.118 (+0.120) | −0.003 | −0.006 | 0.899 | 7.94e-2 |
| 0.66 | 1.29e-6 | 7.20 | 4.75 | 2.2 | +0.099 | −0.088 (+0.090) | −0.010 | −0.103 | 0.824 | 3.76e-2 |
| 0.72 | 1.06e-8 | 7.05 | 5.08 | 2.2 | +0.081 | −0.063 (+0.064) | −0.018 | −0.192 | 0.750 | 3.02e-2 |
| 0.78 | 5.9e-11 | 6.95 | 5.42 | 2.1 | +0.067 | −0.042 (+0.043) | −0.025 | −0.274 | 0.679 | 3.51e-2 |
| ½log5 | 6.4e-12 | 6.90 | 5.55 | 2.1 | +0.062 | −0.034 (+0.034) | −0.028 | −0.307 | 0.652 | 4.87e-2 |
| 0.90 | 5.4e-14* | 6.70 | 6.03 | 2.1 | +0.033 | +0.013 (−0.013) | −0.045 | −0.423 | 0.567 | 1.66e-2 |
| 1.00 | ~0* | 6.30 | 6.30 | 2.0 | −0.023 | +0.108 | −0.082 | −0.534 | 0.520 | 3.04e-2 |
| 1.2–1.5 | ruido ±5e-14* | 4.6→3.5 | ~5.2 | 1.6–1.8 | −0.33→−0.63 | +0.60→+0.51 | −0.14→+0.53 | −0.73→−0.99 | 0.65–0.71 | 2.0e-2→1.6e-2 |

\* Double-precision floor (~1e-13). Beyond T≈0.85 λ_min is NOT resolved; moreover λ_min on a subspace is an UPPER bound for the infimum (M=32 < M=24 by 1–2 orders at T ≥ 0.78): the values do not certify positivity and the ~−5e-14 negative values are round-off. Nothing here is sign evidence beyond 0.80.

Remarks: s·T **is not constant** (3.6 → 6.3 over [0.36, 1.0]); s(T) decreases slowly (10.2 → 6.3), not as 4/T. Primes 4, 5, 7 contribute < 1e-3 up to T = 1. Mode weights of the archimedean h_a: peak 9.4 (0.40), 6.8 (½log3), 4.65 (½log5), 3.7 (1.0), 2.45 (1.5) ≈ 3.7/T.

## 2. Model vs. truth (NUMERICAL)
- M(T) = W[h_a] agrees only for T ≤ 0.45 (overlap ≥ 0.99). At ½log3: M = 7.6e-2 vs λ_min = 1.5e-3 (×50); at ½log5: 4.9e-2 vs 6.4e-12 (×10¹⁰). The overlap ⟨h_a,h*⟩ drops from 0.995 to 0.65.
- **Required rank.** λ_min of W restricted to the span of the first k archimedean modes (M=32):

| T | k=1 | 2 | 3 | 4 | 6 | 8 | truth |
|---|---|---|---|---|---|---|---|
| ½log3 | 9.0e-2 | 6.6e-2 | 1.9e-2 | 1.9e-2 | 7.1e-3 | 4.4e-3 | 1.5e-3 |
| 0.70 | 3.4e-2 | 3.4e-2 | 1.5e-3 | 1.5e-3 | 3.7e-4 | 8.1e-5 | ~5e-8 |
| ½log5 | 4.9e-2 | 1.9e-2 | 1.3e-3 | 1.1e-3 | 3.4e-5 | 1.9e-5 | 6.4e-12 |
| 1.0 | 3.0e-2 | 1.7e-2 | 1.8e-4 | 1.8e-4 | 1.8e-5 | 1.7e-6 | n.r. |

 The number of archimedean modes needed grows with T: the superexponential near-cancellation is a property of a subspace of growing dimension (consistent with Zhu's Landau–Widom law, λ ~ exp(−2π²N/ln N), N ≍ number of degrees of freedom of the prolate), **not** of a fragile mode plus phases.
- Sign of the prime contribution at h_a: Σ_n P_n[h_a] < 0 (costs) for T ≤ 0.54, > 0 (pays) from 0.57 on: +0.085 (0.60), +0.36 (0.80), +0.56 (1.0), +1.00 (1.5). c_{h_a}(log 2) = −0.006 (½log3), −0.34 (0.65), −0.61 (½log5), −0.09 (1.5); c_{h_a}(log 3) switches from + to − toward T≈1. That is: in the fragile archimedean mode the prime phases are **favorable on balance** throughout [0.57, 1.5], and compensate E_∞(h_a) < 0 (which crosses 0 at T≈0.597, matching R183_026) with a margin ~0.01–0.05. This is an arithmetic statement about {s·log p mod 2π} and holds on the grid, but the margin it gives (≥1e-2) is irrelevant against λ_min.
- On premise 3(b): false in the measured range. The fragile archimedean mode has frequency ≈3.7/T and the weight ĥ_a spreads over width ~2, so c_{h_a}(log p) does NOT tend to 1 for p < e^{2T}: for T ≤ 1.5 the dominant primes (2, 3) have c ≤ 0. The predicted "negativity around T≈1.2" does not appear.

## 3. Alignment law — the version that survives (CONJECTURE)
The single-mode version is false. The honest form:

**Conjecture AL-k.** Let V_k(T) be the span of the first k(T) modes of A_∞|𝒫_T. Then (a) λ_min(E_S|V_k) = λ_min(E_S|𝒫_T)(1+o(1)) with k(T) = O(N(T)) (N = the Landau–Widom number of the prolate of width 2T); (b) on V_k the phase Gram matrix G_{ij} = Σ_{p<e^{2T}} v_p Re c_{φ_i,φ_j}(log p) satisfies A_∞|V_k − G ≻ 0.

Consequence: a proof of row D along this route needs, per window, the finite matrix inequality **A_∞|_{V_k(T)} ≻ Σ_{p^m<e^{2T}} (2 log p/p^{m/2}) · Re C_{V_k}(m log p)** (k × k, finitely many primes), plus control of the tail of E_S on V_k^⊥ ∩ 𝒫_T (where A_∞ is large, ≥ λ_{k+1}(A_∞) — a Schur-type inequality). This is NOT a sieve-type statement: it is a k×k matrix inequality with Fourier entries of prolate modes evaluated at log p. But the margin of that inequality is λ_min ~ exp(−c T e^{…}) (thm:margin), so the inequality is not "robust" in any numerical sense: the model explains the **structure** (even, frequency ~3.7/T on the archimedean side, favorable phases) but not the **magnitude**.

Status: (a) NUMERICAL for T ≤ ½log5 only as a trend; (b) OPEN; for T ≥ 0.85 there is no reliable data (precision floor).

## 4. prop:align / prop:band vs. the 4/T law (resolved)
These are not the same mechanism and they do not contradict each other. prop:band/prop:align describe the **negative set of the symbol σ** = m − Σ v_n cos(τ log n), whose first component contains 0 and whose components above τ_a=23.3 lie in alignment arcs; prop:negtrace already says "the band does not decide". The minimizer h* lives at low frequencies: for {2,3} the zeros of σ are 2.28, 4.82, 7.27, 9.67, 11.97, 16.25, 18.49, … (for {2}: 3.31, 6.94, 10.53). The peak of h* (7.0–7.55 on (½log3, 0.8)) falls in/at the edge of the low negative component (4.82, 7.27) — and for T < ½log3 (peak 7.6–8.6) inside (6.94, 10.53) of {2}. That is: the minimizer is fixed by the Tate constraint + window uncertainty pushing mass toward **low** negative components of σ, not toward the band [2πe^{2T}, 2πe^{A}].

## Audit notes
- Convergence: M=24 vs 32 agree to < 5% up to 0.72; at ≥0.78 they differ by 1–2 orders (a variational upper bound that decreases with M). The claims "M(T) ≫ λ_min" are robust (M(T) stable between M=24/32 to 3 digits); the λ_min values beyond 0.8 are not.
- h_a = minimizer of A_∞ (not Sonin's s₀; s₀ requires the C term from R186_013 and, by R186_021, has overlap ≈0.93 with h* at ½log3, similar to h_a=0.96): this does not change the verdict; a single vector with overlap 0.96 gives a Rayleigh quotient ≥ (1−0.96²)·λ₂ ~ 3e-3, already >λ_min.
- Parity: measured as ⟨h(x),h(−x)⟩/‖h‖²; +1.00 always. The mode switches of R183_030/032 refer to other forms (pairs, ker ℓ), not to E_S on 𝒫_T.
- No equivalence between row D and other statements is used.

## For Paper 46
- Add an observation (NUMERICAL) after prop:negtrace: the minimizer of the window form is even, with its spectral peak in the **low** negative component of σ, not in the prop:align arcs; and the near-cancellation requires a growing number of archimedean modes (table §2). This reinforces "the band does not decide".
- Do not include any "single-mode alignment law" or sign prediction beyond 0.8.
