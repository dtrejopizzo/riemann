# L2_BUILD_007 — The archimedean-negative cone: necessary signed tests

## Corpus check
- Paper 46 thm:wh-schur / lem:wh-W: Schur reduction onto a prolate block built from the negative set
  of σ_T. A Schur reduction onto the negative eigenspace of 𝔞_∞|P_T is a variant of it; not rebuilt.
- thm:X (averaged inequalities imposed on new contacts).
- phase-146 R146_003 §D.47 (single-prime tower, PSD iff τ_p ≥ 2/(√p+1)): the Euler-tower lower bound
  idea is already explored; not repeated.
- phase-155 (primes necessary past ≈0.596); R183/R185 Theorem X; MEMORY: "every first-order
  discriminant is a functional of h*".
New here: the finite list of necessary signed tests indexed by the negative eigenvectors of
𝔞_∞|P_T, and their relation to (N_loc) of 006.

## 1. Finite negative index (PROVED, from Paper 46)
𝔞_∞ + (|C_0|+1)‖·‖² is a closed form on P_T ∩ D_T whose domain norm dominates N(F) (001 Lemma 2 with
A_T = 0), and D_T ↪ L²(I_T) is compact (lem:compact). So 𝔞_∞|P_T has discrete spectrum
μ_0(T) ≤ μ_1(T) ≤ … → ∞ with eigenvectors φ_j(T), and n_∞(T) := #{j: μ_j < 0} < ∞. By 006 §2
(CITED), n_∞(T) ≥ 1 for every T > ½log5.

## 2. Necessary signed tests (PROVED)
If λ_A(T) ≥ 0, then for every unit F in span{φ_j: μ_j < 0}:
  Σ_{n∈N_T} v_n Re𝓕(log n) ≤ 𝔞_∞(F) < 0.
In particular (test 𝒯_0): Σ v_n Re𝓕_{φ_0}(log n) ≤ μ_0(T) < 0. The prime comb must be strictly
anti-correlated with the autocorrelation of the archimedean ground state of P_T.
Proof: this is (N_loc) of 006 §3. ∎

## 3. Sufficiency gap (PROVED, quantitative)
Let η > A_T and H_η := span{φ_j: μ_j < η}, which is finite-dimensional. On H_η^⊥ ∩ D_T,
𝔞_T ≥ (η − A_T)‖·‖², because |Π_T(F)| ≤ A_T‖F‖² (lem:mbounds(iii)). The proof of thm:coer-schur
(i)–(iii) applies verbatim with (H_η^⊥, H_η) in place of (V_k, E_k). Hence λ_A(T) ≥ 0 ⟺ the Schur
complement of 𝔞_T on H_η is ⪰ 0. The tests of §2 are the diagonal of this Schur complement minus the
correction term: they are necessary, not sufficient. dim H_η ≈ #{j: μ_j < A_T} ~ Te^{A_T}. This is a
Weyl-type count for the log symbol, ARGUED only; it is the same doubly exponential size as k_0(T).
This reduction is a variant of thm:coer-schur / thm:wh-schur and inherits W-det
(thm:wh-detinherit) for determinant criteria.

## 4. What is new and what remains
- 𝒯_0 is a precise, sign-carrying necessary condition in the localized frame. It is one window
  observable, so the W-fam/W-pat barriers forbid it from deciding the window by itself. It is a
  falsifier-detector, not a proof route.
- Closing (L2) needs the full Schur complement on H_η to be ⪰ 0: a correlated signed bound for the
  prime comb on all of H_η jointly with the archimedean coupling — (N_loc) restricted to a
  finite-dimensional space. No mechanism for it is produced here.

## 5. Review
- §1: lem:compact is stated for 𝔞_T; 𝔞_∞ differs by a bounded form, so the domain and compactness
  coincide. PROVED.
- §2: immediate from 006; PROVED. §3: correct; the dimension count is ARGUED only.
- Novelty is low: §3 is of a known type (thm:wh-schur). Evaluating 𝒯_0 needs φ_0, which has no
  closed form (prolate type); evaluation would be numerical, which is excluded here.
- No sign is certified, and no negative value of 𝔞_T is produced.
- Verdict on 003–007: every construction either restates (L2) exactly or falls into a declared
  barrier or a route the corpus already closed (P121 cross term, phase-146 tower, phase-155
  necessity). The common core is now in exact form: (N_loc) on the archimedean-negative space, the
  localized face of (N). The next step must be arithmetic, not archimedean.
