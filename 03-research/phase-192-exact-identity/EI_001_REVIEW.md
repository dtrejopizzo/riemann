# EI_001 — Review

lem:compact, lem:degen, prop:wit-sens, lem:transfer, prop:opcalc, lem:polarelim, prop:wit-cheb, sec:shape, prob:region), SHAPE_THEOREM
(A1–A17, B1–B8), SPEC_A, index README/06_. Pen and paper.

## Verdict
**EXCLUDED (O1, O7, O11, O15 — the identity is invariant under every modification of thm:shape(A)); identities CONFIRMED PROVED; sign content REF-D (Lemma S / R186_029 H(ii)).** Two minor FIXes (§2). No SI-column property moves.

## 1. Line-by-line check of the PROVED claims
| claim | check | label |
|---|---|---|
| Lemma 1 (Euler–Lagrange with Tate multipliers) | h* attained (lem:compact); the functional G ↦ 𝔞_T(h*,G) − λ⟨h*,G⟩ is form-continuous and vanishes on ker A ∩ ker B ∩ 𝒟_T; A, B form-continuous and independent on 𝒟_T ⊃ C_c^∞(I_T) ⇒ it is β₀A + β₁B. 𝔞_T(h*,G) = ⟨σ_T(D)h*,G⟩ for G ∈ C_c^∞ as tempered distributions (σ_T of log growth, ĥ* ∈ log-weighted L²). | CONFIRMED PROVED (routine) |
| (1.1) | for t > T the local terms C₀h*(t), ∫K(u)h*(t)du vanish; h*(t+u) = 0 for u > 0; h*(t+log n) = 0. | CONFIRMED |
| Theorem 1, (2.1) | re-derived: ½∫2e^{−(t−s)/2}h* = e^{−t/2}A(h*) = 0; comb = −∫_{[1,X)}u^{−½}h*(t−log u)dψ; u^{−½}h*(t−log u) = e^{−t/2}H̃(e^t/u) with H̃(x) = x^{½}h*(log x); main term ∫₁^X u^{−½}h*(t−log u)du = e^{t/2}∫_{t−2T}^{T}e^{−s/2}h* = −e^{t/2}∫_{−T}^{t−2T}e^{−s/2}h* by B(h*) = 0; signs collect to E = p − q − r. Ranges: p ≡ 0 for t ≥ 3T (= e^{t/2}B), q ≡ 0 for t ≥ 3T (t − log u > T). Left side by h*(s) ↦ h*(−s) (A ↔ B). | CONFIRMED PROVED. Content: the prop:wit-cheb split (dψ = d(ψ−u) + du, polar part removed by Tate) applied pointwise to the exterior; elementary |
| Theorem 2(i) | Fourier transform of Lemma 1 extended by E. | CONFIRMED |
| Theorem 2(ii) | ζ′/ζ(s) + ζ′/ζ(1−s) = log π − ½ψ(s/2) − ½ψ((1−s)/2) from ξ(s) = ξ(1−s) (the 1/s, 1/(s−1) terms cancel); at s = ½+iτ this gives −ζ′/ζ(½+iτ) − ζ′/ζ(½−iτ) = m(τ) and 2Re P_X = Σv_n cos. So Σ(τ) = σ_T(τ) exactly. | CONFIRMED PROVED — but it is eq:symbol/prop:boundary in meromorphic dress: "the zeros do not appear" is the definition of σ_T (prop:finite(iv)), not a result |
| Theorem 2(iii) | p, q compactly supported ⇒ entire transforms; r(t) = Σ_k e^{−(2k+½)t}μ_k⁺ for t > T ⇒ first poles at τ = ∓5i/2; ĥ*(±i/2) = B, A = 0 removes the ±i/2 poles of Σ. | CONFIRMED (structure PROVED; the residue constant is ARGUED, as the memo says) |
| P2 (correction of SPEC_A §2(d)) | SPEC_A paired v_{n_j} with the polar coupling 2n_j^{−½} = 2e^{−(t−s)/2} at lag 2T_j; for x primitive on I_{T_j} and t on the right collar, t − s > 0 throughout, so ∫2e^{−(t−s)/2}x(s)ds = 2e^{−t/2}A(x) = 0. The archimedean partner at that lag is K₁(2T_j) = O(e^{−5T_j}); the polar partner is p(t), the opposite-collar partial Tate moment. | CONFIRMED PROVED; **endorsed as a correction to SPEC_A §2(d)** |
| Corollary §3 ("no further relation exists", R163_1001 Thm C.3) | relies on an index memo not re-verified here. | CITED (internal), not PROVED here |

## 2. FIXes (not load-bearing)
1. §4, size of ⟨G,p⟩: for t ∈ (T, T+ε), s ∈ (−T, −T+ε) the factor is e^{t/2}e^{−s/2} ≈ e^{T}, not e^{T/2}·e^{−T}. Bookkeeping only.
2. Theorem 2(iii) residue matching is stated as "consistent" with an unfinished constant; label the pole-by-pole consistency ARGUED (the memo does, in item 4).

## 3. MUST-NOT clauses, tested by applying the modification
Property set of the object: "(2.1)/(1.1) and Lemma 1 hold for the minimizer of the form". Apply each modification and ask whether the identity survives for the modified form (lem:transfer).
| clause | modification applied | survives? |
|---|---|---|
| O1 / A1 | Λ1_{n≥N} | yes: (2.1) uses dψ only as a positive measure on [1,X); replace ψ by ψ_a. The deleted comb has negative bottom at T ∈ [0.60, ½log N] (thm:finmod(i)) and the identity still holds for its minimizer. **EXCLUDED here already** |
| O2–O5 | amplification, tail deletion, cΛ, ε-weight | yes (same reason) |
| O6/O11 Beurling | positive prime measure on a semigroup | yes verbatim (any positive atomic measure); memo concedes ("ℤ unused") |
| O7 / A7 | a_P | yes (positive comb) |
| O8a quartets | 𝔞_T + kQ_z | yes with the a.c. part −kβ_z added to the kernel (same proof); Lemma 1 holds for any closed semibounded form on P_T |
| O8b f_t, O9 ζ̃, O10 Epstein | signed combs / twisted FE | yes: (2.1) never uses a ≥ 0 or the FE beyond m |
| O12 ζ_K | ψ_K, Γ_K | yes verbatim (memo concedes) |
| O13 bounded J | per-window identity | yes |
| O14 symbol truncation | n/a (not a comb) — Lemma 1 holds for any symbol | yes |
| O15 Poisson positions | {log n} ↦ random u_j | yes (any positive atomic measure) |
| B4 opcalc | the identity is a statement outside (−2T,2T), not a measure identity on the window | not in prop:opcalc's class — correct; but any *use* of it to bound ⟨G,q⟩ is B4/B6 (memo concedes) |
| B8 REF-D | sign content | C*_A = Lemma S (SPEC_A) = D at T_{j+1} given D at T_j (R186_029 H(ii)) — REF-D, as the memo itself states |
Conclusion: the object is invariant under **every** operation of thm:shape(A); by thm:shape(C) no deduction built on it alone is valid. Memo's own table agrees ("invariant as an identity").

## 4. MUST clauses (genuinely met, not asserted)
| clause | verdict |
|---|---|
| exact identity on h*_T | met (Theorems 1–2) |
| non-linear in Λ | **not met**: affine in v at fixed h*; non-linearity only via h*(Λ) (memo concedes) |
| Euler × FE × ℤ jointly as mechanism, ℤ as mechanism | **not met** (memo concedes) |
| margin from the identity | **not met** (relocated into ⟨G,q⟩) |
| fluctuation not density | structure exhibited (p = density-1 field, q = fluctuation), nothing decided — not a mechanism |
| 10⁻⁵-sensitive | vacuous: the identity holds for all weights; nothing decides a sign |
| separates ζ from ζ_K | **not met** (memo concedes) |
| (R)(2),(3),(10) | not met; (R)(4) met; (R)(5)–(9) formally, vacuously |

## 5. Retry check
Not a retry of a dead row: "exterior field" appears only in R163_1001(C) (NO-GO, different question) and SPEC_A (statement). But the identity is prop:wit-cheb's split + L2_008 §4's prime pairing of a clamped mode, applied to h* outside I_T; the only new PROVED fact is P2. The sign content is exactly SPEC_A's C*_A, already REF-D (index: phase 191).

## 6. REF-D scepticism
The object is not D in other coordinates (it decides nothing); its only sign-bearing use, (β) of §4, is Lemma S = D. The memo is honest about this. No new reformulation of D is introduced.
