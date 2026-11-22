# L2_BUILD_006 — The prime-free inequality (L2-H₀): what δ₀ is, and the signed prime bound

## Corpus check
- Paper 46: thm:coer-A / thm:coer-B (archimedean coercivity on V_k, block-Tate), cor:coer-L1,
  prop:arch, cor:Tarch (0.58 ≤ T*_{∞,P} ≤ 0.60), prop:archneg (T*_∞ ≤ 0.4608), thm:N / Theorem N′
  (lattice certificates, M ≤ 24 impossible at 0.68 and log 2), prop:wit-coh, prop:wit-sens,
  rem:wit-cheb, §open (N).
- phase-155 R155_029 / R155_060: "the role of the primes flips at T*_{∞,P} ≈ 0.596": below it the
  certificate pays for the primes, above it the primes are NECESSARY. MEMORY phase-155 round 3.
Verdict: the sign of δ₀ below is ALREADY KNOWN (phase 155, cor:Tarch). New here: the exact
identification δ₀(T) = λ_{∞,P}(T) inside the (L2-H) frame, the F-uniform impossibility of the
prime bound, and the exact (N)-type statement in the localized frame with its comparison to §open (N).

## 1. Definition and identification (PROVED)
(L2-H₀)(δ₀): 𝒞_arch(F) ≤ Σ_j 𝔞_∞(χ_jF) − δ₀‖F‖² for all F ∈ P_T ∩ D_T (notation of 005).
By 004 (1.1), Σ_j 𝔞_∞(χ_jF) − 𝒞_arch(F) = 𝔞_∞(F). Hence the best δ₀ is exactly
  δ₀*(T) = λ_{∞,P}(T) := inf{𝔞_∞(F): F ∈ P_T ∩ D_T, ‖F‖ = 1},
independently of the partition. ∎

## 2. Sign and scaling of δ₀* (CITED from Paper 46, with the pen-and-paper part marked)
(i) λ_{∞,P} is nonincreasing in T (prop:arch(i), PROVED there: nested feasible sets).
(ii) λ_{∞,P}(T) > 0 for T < 0.58 and < 0 for T ≥ 0.60 (cor:Tarch; CITED, includes interval arithmetic).
(iii) λ_{∞,P}(T) ↓ C_0 = −5.3721… as T → ∞ (prop:arch(ii), PROVED there).
(iv) Pen-and-paper upper bound for (L2)-range windows (PROVED here): for T > ½log5,
  λ_{∞,P}(T) ≤ C_0 + φ((3π/2T)²) (prop:arch(ii), PROVED in Paper 46 without computation), negative for
  T > 0.74921; ½log5 = 0.8047 > 0.74921. So on the whole (L2) range δ₀*(T) < 0, by a computation-free
  argument, and δ₀*(T) ∈ [C_0, C_0 + φ((3π/2T)²)], i.e. δ₀* = C_0 + O(T^{−2}·log-type) → C_0.
(v) thm:coer-B does NOT give (L2-H₀): it gives coercivity of 𝔞_∞ only on V_k (block-Tate, codim 2k),
  not on P_T (codim 2); the 2k−2 extra directions E_k are exactly where 𝔞_∞ is negative.
  Theorem N′ concerns lattice dual certificates and is not a statement about 𝔞_∞|P_T.

**NO-GO (PROVED, given (iv)).** For every T > ½log5 the split "archimedean slack ≥ prime cost" fails:
(L2-H₀)(δ₀) holds only with δ₀ ≤ δ₀*(T) < 0. Any proof of (L2) must have the primes contribute
POSITIVE energy (Π_T(F) > 0) on every F with 𝔞_∞(F) < 0.

## 3. The signed prime bound that closes (L2) (PROVED equivalence)
(L2) at T ⟺ (N_loc): for all F ∈ P_T ∩ D_T,
  Σ_{n∈N_T} v_n Re𝓕(log n) ≤ 𝔞_∞(F).
The right side is negative on the archimedean-negative cone 𝒩_T := {F: 𝔞_∞(F) < 0} ≠ ∅ (by (iv)).
(a) No F-uniform version exists: Σ v_n Re𝓕(log n) ≤ δ‖F‖² on P_T forces δ ≥ A_T > 0 (005 §3(b)),
    while (N_loc) needs δ₀*(T) < 0 on 𝒩_T. So the bound must be correlated with F (PROVED).
(b) On 𝒩_T it is a ONE-SIDED, SIGNED statement: the prime comb must be anti-correlated with the
    autocorrelation of F: Σ v_n Re𝓕(log n) ≤ −|𝔞_∞(F)|.
(c) Comparison with Paper 46 §open (N): there, via prop:wit-coh, a witness is F with
    Σ_k|F̂(ω_k)|²𝒞_T(ω_k) < −𝔟_T(F), ω_k = πk/2T; (N) asks for a signed pointwise bound on the
    coherence 𝒞_T at Nyquist points correlated with the samples |F̂(ω_k)|². (N_loc) is the same
    inequality before sampling: Σ v_n Re𝓕(log n) = (1/2π)∫Σ v_n cos(τ log n)|F̂|²dτ, and sampling at the
    Nyquist mesh of I_T (support of 𝓕 in [−2T, 2T]) converts it to the (N) series. The split of the
    right side differs: 𝔟_T in (N) is the "polar-free" part of the form (eq:Aform), 𝔞_∞ here.
    Equivalence of (N_loc) and (N) at each T: both are ⟺ λ_A(T) ≥ 0 (PROVED: (N_loc) by §3,
    (N) by prop:wit-coh). Content-wise (N_loc) says what (N) says, with the explicit information
    that on 𝒩_T the bound must be strictly negative.
(d) Barriers: by cor:void, (N_loc) cannot follow from PNT/zero-location properties of Λ alone (it
    fails for finite modifications); by prop:wit-sens no bounded functional of the weights decides it;
    by rem:wit-cheb exponent-½ cancellation with sign is needed.

## 4. Review
- §1 exact. §2(iv): uses Paper 46's proof of cor:mono with the comb deleted (pen and paper:
  φ is an explicit Lévy-type bound on λ_3 of 𝔞_∞'s Lévy part); I checked that prop:arch(ii) is
  stated as PROVED without the appendix. OK. Note φ((3π/2T)²) is not evaluated here; the claim
  T₀(0) = 0.74921 is Paper 46's (root of an explicit equation; its evaluation is numerical in the
  paper) — so (iv) is CITED, not pen-and-paper. Corrected label: (iv) CITED.
- §2 NO-GO is real but KNOWN (phase 155 "primes become necessary"). Not new.
- §3 is an exact reformulation; (a) is new in this exact form but elementary; (c) is a correct
  comparison. No sign certified, no negative value of 𝔞_T produced (only of 𝔞_∞, which is known).
- Consequence for the program: there is no prime-free slack to spend; the only possible closing
  input is a correlated, signed arithmetic inequality on 𝒩_T. → 007.
