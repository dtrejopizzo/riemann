# INV_J_001 — The Montgomery–Dyson bridge on the prime side: two-variable lift of 𝔞_T, free positivity, sieve direction, parity (track J)

Track J.

Notation of Paper 47 (04-papers/47-row-d-dual-certificates/main.tex): v_n = 2Λ(n)n^{−1/2}, N_T = {n ≥ 2: log n < 2T},
c_F autocorrelation, 𝔞_T(F) = C_0‖F‖² + Lev(c_F) − Σ_{n∈N_T} v_n Re c_F(log n) =: Arch_T(F) − Π_T(F) (main.tex l.403),
modifications O_1–O_15 (def:shape-ops), thm:shape, lem:shape-scale, lem:shape-tail (O_3), prop:shape-eulerdel (O_6).

## 0. Corpus / index check (before building)
- P36-4 (index 03_PHASES_000-099 l.150; 06_OPEN_RESIDUES "W₂ two-variable form"): phase-36 Doc 107 (W₂ = W⊗W, kernel
  g(x₁x₂)φ(x₁/x₂)) and Doc 108 (sieve→index bridge, PUENTE MUERTO). Their off-diagonal is the **multiplicative** correlation
  Σ_{d|N}Λ(d)Λ(N/d)φ(d²/N) (Doc 108 Obs. 4.2: "no singular series"). Doc 108 §5(a1) mentions the additive analogue only as a
  precision comparison (Selberg factor 8).
- NG-B8 (Montgomery pair correlation as detector: zero side, on-line spacings), NG-A3 (MV cross-covariance ≈ 0), L24/L63
  (pair-correlation heuristics/proportions), L52 (Lamzouri: Hilbert inequality + pair correlation, proportion only).
- P47: lem:shape-tail (O_3) already excludes "exact small values + every upper-bound sieve inequality"; lem:shape-del (O_1)
  excludes C_PNT, C_BT; prop:prog excludes BV/BDH/SW. P149 additive pencil (Vaughan singular series) DEAD (T5).
- INV_H_001 row A7 (running in parallel): ARGUED that HL correlations enter only through a square or an asymptotic. Not duplicated:
  below is the exact lift and a PROVED exclusion of the whole additive-correlation class, including the unproved HL conjecture.
- **New reason vs P36-4.** The indexed attempt used the multiplicative tensor square (Dirichlet convolution Λ⋆Λ, Beurling-generic).
  Here the off-diagonal is the **additive** shift n ↦ n+h, which has no meaning in a Beurling system, and the free positivity
  examined is Gram/large-sieve/Hilbert/Selberg/GPY on the integer line, not the tensor signature. The object, the falsifier
  class and the method class all change.

## 1. The two-variable lift (PROVED, exact on 𝒫_T)
Let ℓ(n) = log p if n = p^k, ℓ(n) = 1 otherwise. Integrality gives Λ(n)² = ℓ(n)Λ(n) for all n (PROVED, trivial).
For F ∈ 𝒫_T∩𝒟_T put κ_F(n) := 2n^{−1/2} Re c_F(log n)/ℓ(n) (n ∈ N_T). For any real symmetric off-diagonal kernel
K = (K(m,n))_{m≠n∈N_T} define on weight vectors a ∈ ℝ^{N_T}

  𝔅_T[F;K](a) := Arch_T(F) − Σ_{m,n∈N_T} a_m a_n 𝕂_F(m,n),  𝕂_F(n,n) = κ_F(n), 𝕂_F(m,n) = K(m,n) (m≠n).

**Lemma J1.** 𝔅_T[F;K](Λ) = 𝔞_T(F) − Σ_{h≠0} Σ_{n, n+h∈N_T} Λ(n)Λ(n+h) K(n,n+h). In particular the diagonal restriction
(K = 0) is exactly 𝔞_T(F), and the off-diagonal is exactly the finite additive prime-pair correlation weighted by K.
Proof: diagonal Σ Λ(n)²κ_F(n) = Σ v_n Re c_F(log n) = Π_T(F) by Λ² = ℓΛ; regroup m = n+h. ∎
Remark: Λ² = ℓΛ fails for cΛ (c ≠ 1), so the lift itself is not O_4-equivariant; but 𝔞_T(F) never depends on K, so any
sign statement must still be a statement about the diagonal (§3).

## 2. Free positivity in the lift and its direction (PROVED)
Available unconditional inequalities on the quadratic Q_K(a) := Σ a_m a_n 𝕂_F(m,n):
(i) Gram/Bochner: if 𝕂_F = (Φ(log m − log n)·w_m w_n) with Φ̂ ≥ 0, then Q ≥ 0 (requires κ_F ≥ 0 on the diagonal).
(ii) Montgomery–Vaughan Hilbert inequality / large sieve (CITED): |Σ_{m≠n} a_m ā_n/(λ_m−λ_n)| ≤ πδ^{−1}Σ|a_n|², and
∫_0^U|Σ a_n n^{−iτ}|² = Σ|a_n|²(U + O(n)): **upper** bounds on Gram forms, valid for every complex vector.
(iii) Selberg sieve (CITED): Σ_{n≤X}Λ(n)Λ(n+h) ≤ (8+o(1))𝔖(h)X (HR74 ch.3; explicit Brun–Titchmarsh forms exist): **upper** bounds.
(iv) GPY/Maynard (CITED): lower bounds for sieve-weighted sums Σ_n w_n(Σ_{h∈H}Λ(n+h) − ρ log X) > 0 for X large: **asymptotic lower**.

**Proposition J2 (direction).** 𝔞_T(F) ≥ 0 is Π_T(F) ≤ Arch_T(F), i.e. Σ_n Λ(n)²κ_F(n) ≤ Arch_T(F). Through the lift,
Σ Λ²κ_F = Q_K(Λ) − Σ_{h≠0}ΛΛ(n+h)K. Hence:
(a) Gram positivity (i) gives Q_K(Λ) ≥ 0, i.e. a **lower** bound on Π_T — an upper bound on 𝔞_T. Wrong direction.
(b) The useful direction needs an upper bound on Q_K(Λ) (MV/large sieve: allowed) **and**, on the pairs with K(n,n+h) > 0, a
**lower** bound on Σ Λ(n)Λ(n+h)K — the twin-prime direction, which the parity barrier forbids for sieve methods (Selberg/Bombieri
parity; CITED). With K ≤ 0 off-diagonal both pieces are upper bounds (sieve-allowed), but then (ii)–(iii) only reproduce
Π_T ≤ (const ≥ 1)·Σ_n Λ(n)²|κ_F(n)|, i.e. the trivial bound Π_T ≤ 𝒜_T‖F‖² (INV_F_001), since every MV/large-sieve constant
is ≥ the diagonal. PROVED (elementary from the identity of J1).
So: **the free positivity of the two-variable object points the wrong way; the sieve-allowed direction is monotone and can only
reach the trivial bound; the sign-carrying half is the parity-forbidden lower bound on positive-kernel pair sums.** (Task 4.)

## 3. Theorem J3 — the additive prime-pair class is excluded (NO-GO, PROVED)
Call a property 𝖯 of weight vectors a: ℕ → [0,∞) **sparse-stable** if a has 𝖯 whenever a = Λ + e with e supported on a set
E with #(E∩[1,X]) = O(log X) and |e| ≤ C. Examples (PROVED by the count below): every asymptotic statement on
Σ_{n≤X} a(n)a(n+h) with main term ≫ X^θ (θ>0), uniform in h ≤ X^{1−ε} — in particular the Hardy–Littlewood pair and k-tuple
**conjectures** themselves, BV, GPY/Maynard lower bounds, Goldston–Montgomery variance of ψ(x+h)−ψ(x).
Count: for a_P = Λ·1{p ≥ P} (O_6), e = −Λ·1{p<P} is supported on prime powers of p < P, #(E∩[1,X]) ≤ π(P)log₂X, |e| ≤ log P;
the change in Σ_{n≤X}a(n)a(n+h) is ≤ 2π(P)log₂X·log P·log X = o(X^θ).
**Theorem J3.** Every sparse-stable 𝖯 is satisfied by a_P for every P, and a_P fails WP_T at every T ∈ [0.60, ½log P]
(prop:shape-eulerdel). Taking P > e^{2T}: no deduction "Λ has 𝖯 ⇒ λ_A(T) ≥ 0" exists at any T ≥ 0.60. Moreover a_P is an Euler
product over ℕ with the zeros of ζ, so the exclusion holds even if 𝖯 also contains every zero-side statement (Montgomery pair
correlation, GUE). PROVED.
Complements: explicit upper-bound inequalities (MV, Selberg, Brun–Titchmarsh) are down-closed ⇒ lem:shape-tail (O_3) /
O_4 small c (PROVED, already in P47). Explicit lower bounds alone are up-closed ⇒ O_4 large c, T > ½log2 (PROVED).
Two-sided explicit bands: O_4^ε (CONDITIONAL on κ_T ≠ 0) and B′ (relative precision needed ≤ 4·10⁹Te^{−15.449T}; sieve
precision is O(1), Doc 108 §5) — ARGUED excluded.

**Corollary J4 (correction to the G1 brief).** "An input that fails for Beurling systems" is necessary but not sufficient:
O_6 stays inside ℕ, keeps additive structure, Euler product and zeros. A ζ-specific input must also distinguish Λ from a_P on
the window N_T, i.e. be an *exact finite statement about Λ on n < e^{2T}* or tie N_T to the exterior through the functional
equation (the only property a_P breaks, prop:shape-eulerdel). For prime-pair data this means: an explicit, two-sided,
small-X₀ statement coupled to the FE — none is known; the coupling with the FE is the polar/Near term ⇒ REF-D.

## 4. Self-check
- thm:shape: J3 is an instance of (A) with O_6; nothing new is claimed about (A)'s windows. (B″): J1 is an identity valid for
  every K ⇒ carries no sign. (B′): §3 complements.
- Problem (R): no clause discharged. REF-D: the residual "FE-coupled pair statement" is the Near/polar term (CA_M_001).
- No partial positivity obtained beyond the trivial bound; no negative value for ζ produced.

## 5. Verdict
P36-4 revived on the additive side: exact lift PROVED (J1); free positivity is wrong-direction or trivial (J2, PROVED); the whole
additive prime-pair class, including HL and pair-correlation conjectures, is NO-GO by O_6 (J3, PROVED). Parity: the sign needs the
parity-forbidden (lower, positive-kernel) direction. P36-4 → CLOSED (NO-GO, both multiplicative (Doc 108) and additive (J3)).
Hypothesis to break: **H_sparse** (sparse-stability). Live residue (OPEN): a pair statement that is *not* sparse-stable, i.e.
sensitive to the small primes p < e^{2T} jointly with the FE; candidate shape: exact finite identities for Σ_{n<e^{2T}}Λ(n)Λ(n+h)
with h small, coupled to the archimedean term — currently no such object.
