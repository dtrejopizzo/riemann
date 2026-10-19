# L2_BUILD_005 — The signed lag-coupling object (rewritten and expanded)

## Corpus check
Same search as 004 plus "lag", "Toeplitz form", "positive measure", "truncated Toeplitz",
"cross term". Found: Paper 47 sec:wh (truncated Wiener–Hopf R_T f(D) R_T), thm:X (averaged
inequality on U_{T0}), P121 OPTION_MATRIX (signing the IMS cross term = "primitive gap in localized
form", rejected without a new Euler-specific cut identity), R186_001 (Gram of translates in {log n},
NO-GO for Gram alone). Verdict: the reformulation below IS the P121 cross-term problem; new here
are only the exact form (2.1) of 004 with the prime comb inside a single positive measure, and the
proof that (L2-H) is equivalent to (L2) with no overlap correction. Labelled accordingly.

## 1. Exact rewriting (PROVED; this is 004 (2.1))
For a partition χ_j with Σχ_j² = 1 on I_T and supports of length < log 2, for F ∈ P_T ∩ D_T:
  𝔞_T(F) = Σ_j 𝔞_∞(χ_jF) − 𝒞(F),   𝒞(F) := ¼∬ ω̃(x,y) Re F(x)F̄(y) d𝒦(x−y) dy,
  𝒦 = K(|u|)du + Σ_{n∈N_T} v_n(δ_{log n} + δ_{−log n})  (a positive measure on ℝ),
  ω̃(x,y) = Σ_j(χ_j(x) − χ_j(y))² ∈ [0, 4], ω̃ = 2 whenever x, y have no common χ_j, in particular at all
  lags |x − y| ≥ log 2.
Proof: 004 §1–§2 (complete there). There is no overlap correction: the identity is exact; the
"overlap band" of the first draft is the region ω̃ < 2, already inside 𝒞.

## 2. Equivalence (PROVED)
λ_A(T) ≥ 0 ⟺ 𝒞(F) ≤ Σ_j 𝔞_∞(χ_jF) for all F ∈ P_T ∩ D_T  (L2-H).
Proof: immediate from §1 (and thm:coer-schur(iii) for the S_{T,k} form). ∎

## 3. Splitting of 𝒞 and what each part must do
𝒞 = 𝒞_arch + 𝒞_prime, 𝒞_prime(F) = Σ v_n Re𝓕(log n) = −Π_T(F) (004 §2), 𝒞_arch = ¼∬ω̃K ReFF̄.
(a) 𝒞_arch is the coupling of a critical kernel: by 004 §3 its Schur-test size is log(1/ℓ) + O(1),
    equal to the local gain: no slack at leading order.
(b) 𝒞_prime has no sign: sup over unit F ∈ P_T of 𝒞_prime(F) = A_T (PROVED: lem:mbounds(iii) gives
    sup_τ Σv_n cos(τ log n) = A_T; take F_τ = e^{iτt}φ(t) − (Tate projection), φ a fixed bump with
    ‖φ‖ = 1 supported in I_T: 𝒞_prime(F_τ) = Σv_n Re[e^{iτ log n}𝓕_φ(log n)] + O(1/τ) — choose φ with
    𝓕_φ(log n) > 0 for all n ∈ N_T (e.g. φ = normalized 1_{I_T}, 𝓕_φ(u) = 1 − u/2T > 0 for u < 2T) and τ
    from Kronecker: 𝒞_prime(F_τ) → Σ v_n(1 − log n/2T) > 0; the Tate projection changes F_τ by
    O(1/τ) since A(e^{iτt}φ), B(e^{iτt}φ) = O(1/τ) by one integration by parts on each half... φ = 1_I has
    jumps, so A(e^{iτt}1_I) = O(1/τ) directly by integration.) So the prime coupling is strictly
    positive on some unit vectors of P_T — the sign must be supplied jointly with 𝒞_arch and the local
    energies, never by 𝒞_prime alone.

## 4. Review
- §1–§2 exact; PROVED. §3(b) PROVED (elementary; the wave packet leaves P_T by O(1/τ) and is
  projected back).
- Status: (L2-H) is (L2) rewritten. The corpus (P121) already identified "signing the cross term"
  as the gap and asked for an Euler-specific cut identity. This memo adds nothing that closes it.
  It does fix where any proof has to act: on the cross term 𝒞 at the lags log n, jointly with the
  critical archimedean coupling, using P_T.
