# R162_502 — Round 6: (A) multiplicative equivariance, NO-GO; (B) signed bilinear square at first contact

Round 6, mechanism H. Part (A) was stopped by the the redirect (R162_590 §3(H)). Part (B)
follows R162_590 §2 item 1 (R160_020 Option 3; S4 §5.15).

**Status.**
- (A) Hecke / prime-translation equivariance: **NO-GO** (dead line, recorded with citations).
- (B) Signed bilinear route: **PARTIAL → NO-GO for closure.**
  - PROVED: an exact compressed semigroup law, and an exact *Möbius-conjugation square* decomposition of
    the Weil form, which is new in this form.
  - PROVED: an admissible-input classification showing that every estimate that could orient the square
    is killed by DH, Λχ₂, Beurling (DMV/Zhang) or F2.

Gate 1 is not closed.

Conventions: Paper 47 def:PD, def:W, eq:nuw. v_n = 2Λ(n)/√n. c_F(u) = ∫F(t)F(t+u)dt on I_T = [−T,T]. The
prime side of 𝔞_T is −Σ_{n≤X} v_n c_F(log n), with X = e^{2T}. H_T is the operator of 𝔞_T on P_T, and T_0
is the first window with λ_A(T_0) = 0. The first contact is F ∈ N = ker H_{T_0}, JF = εF.

---

## Part A. Multiplicative equivariance (NO-GO; short record)

**What was built before the redirect (PROVED, weight-blind or dead).**
- A1 (p-local Hecke law). With T_p = τ_L + τ_{−L}, L = log p and σ_p = p^{1/2} + p^{−1/2}, the p-part of the prime
  side satisfies B^{(p)}(F,T_pF) = σ_p Q^{(p)}(F) + 2 log p·(p^{−1/2}c_F(0) − c_F(L)). Proof: the geometric shape
  of Λ on the powers of p. This is the renewal law (R_p) ν_p^+ − p^{−1/2}τ_L^*ν_p^+ = log p·p^{−1/2}δ_L.
- A2 (DH line). (R_p) fails for DH. There b(p²) = log p(2a(p²) − a(p)²) is not geometric, and
  b(pq) = log(pq)(a(pq) − a(p)a(q)) ≠ 0 puts mass at composite points.
- A3 (no globalization). The off-p cross terms fall on log(q^kp^{±1}), where Λ = 0. The Hecke eigen-structure
  belongs to the coefficients 1 of ζ, and the Weil form sees only log ζ. At first contact, A1 becomes the
  collar identity of R162_405/408 with an indefinite remainder.
- A4 (the only sign). The only sign is strip domination: |2cos(γL)| < σ_p for |Im γ| < ½. It holds for every
  zero set in the open strip, DH included, so it fails F1 and F3.
- A5 (hull lemma, weight-blind but non-perturbative). Every 0 ≠ F ∈ N has convex support hull of length exactly
  2T_0. Reason: 𝔞 and the primitive constraints depend only on c_F, and c_F is translation-invariant.

**Corpus verdict (R162_590 §3(H)).** The line was already dead:
- R160_D4 Thm 5.1 / Cor 5.2: every convolution identity on tests in Z[Q_{>0}] is a window shift at T + ½log X,
  and finitely many exact values of Λ never decide ∀T.
- R152_002: Hecke operators are unbounded in p on the relevant states.
- Phase 159 G1_B1_R2 Prop M and exclusion K3: a useful sign must be non-Frobenius-equivariant.
- I-13 / 159 G2: twist-covariant arguments are dead.
- R162_401 / 403 / 406: symbol identities, and Λ*1 = log cancels at composite thresholds.

A1–A4 add one explicit instance of these walls: the Hecke constant σ_p is the Euler-factor pole, and its only
sign is strip domination. **Line closed.**

---

## Part B. Signed bilinear square at the first-contact vector

### B0. Corpus check

- **R160_M7 (Friedlander–Iwaniec profile), Thm 5, Cor 5.1, Prop 5.2–5.3.** Every bilinear piece of W_T is a
  compressed Toeplitz product with kernel (mk)^{−½}c_F(log mk). Bilinear gain = misalignment of A_α, Ā_β in
  L²(μ_F). The *global* signed bound is E1 (Prop 5.2(c)). The FI/HB weights are absent from W_T (Prop 5.3).
  M7 did not use the first-contact kernel, and it did not produce a square with an orientation.
- **R160_D4 §0.3: G2_B3_R1–R5** (Λ = μ*log, Selberg, Vaughan; separation theorem). Their Cor S2(b) leaves
  "coupled squares" open. B2 below is such a coupled square, written as a conjugation.
- **R161_002.** The canonical sum×product square contains the square of the truncated Weil operator, so it
  is sign-blind (F2). **R162_401:** [X,S_N] = −K_N cancels the log channel.
- **H-DMV (R160_001 I-6).** Beurling systems have Λ ≥ 0, an Euler product and Λ_B*1 = log exactly, with zeros
  β_n → 1. They form the mandatory positivity falsifier.

The new element is to use H_{T_0}F = 0 inside a square in which Λ*1 = log is kept exact until the last line.
This is done by the exact semigroup law B1, which is valid because only one-sided shifts are used.

### B1. The compressed one-sided semigroup (PROVED)

For a finitely supported α on ℕ, put M_T(α) = P_T Σ_m α(m)m^{−½}τ_{log m}P_T on L²(I_T), with τ_cF(t) = F(t+c).

**Lemma B1.**
(a) M_T(α)M_T(β) = M_T(α*β) exactly.
(b) [X, M_T(α)] = −M_T(α·log), where X is multiplication by t.
(c) Z := M_T(1) is invertible with Z^{−1} = M_T(μ).
(d) ⟨F, M_T(α)F⟩ = Σ α(m)m^{−½}c_F(log m).

*Proof.*
(a) (P τ_a P τ_b P F)(t) = 1_I(t)1_I(t+a)1_I(t+a+b)F(t+a+b). For a, b ≥ 0, t ∈ I and t+a+b ∈ I imply t+a ∈ I,
because I is convex. Hence P τ_a P τ_b P = P τ_{a+b} P. Terms with mk > X vanish on both sides.
(b) [X,τ_c] = −cτ_c, and X commutes with P_T.
(c) Apply (a) with 1*μ = δ_1, noting M_T(δ_1) = I.
(d) By definition. ∎

(a) is the exact window form of the multiplicative semigroup. It is what part A lacked: two-sided Hecke
translations do not compress exactly, but one-sided ones do. It is weight-blind as algebra: for DH, with
a(1) ≠ 0, M_T(a) is invertible too, because it is unipotent.

### B2. The Möbius-conjugation square (PROVED)

**Theorem B2.** On L²(I_T), with S = (X+T)^{1/2} ≥ 0,

    (B2.1)  M_T(Λ) = Z X Z^{−1} − X,
    (B2.2)  2⟨F,M_T(Λ)F⟩ = ½‖S(Z^* + Z^{−1})F‖² − ½‖S(Z^* − Z^{−1})F‖² − 2‖SF‖².

Hence, on P_T,

    (B2.3)  𝔞_T(F) = 𝔞_T^∞(F) + 2‖SF‖² − ½‖S(Z^*+Z^{−1})F‖² + ½‖S(Z^*−Z^{−1})F‖²,

where 𝔞_T^∞ is everything except the prime side (archimedean, collar and Tate endpoint terms).

*Proof.*
- (B2.1): Λ*1 = log and B1(a),(b) give M_T(Λ)Z = M_T(log) = −[X,Z]. Multiply on the right by Z^{−1}.
- Invariance: (B2.1) is unchanged under X → X + T, which makes the multiplier nonnegative on I_T.
- (B2.2): Then ⟨F, M_T(Λ)F⟩ = ⟨SZ^*F, SZ^{−1}F⟩ − ‖SF‖². Polarize the real pairing.
- (B2.3): The prime side of 𝔞_T is −2⟨F, M_T(Λ)F⟩ by B1(d). ∎

Reading: Z^* is anti-causal (its symbol is ζ̄ truncated) and Z^{−1} is causal (1/ζ truncated). The "aligned"
square ‖S(Z^*+Z^{−1})F‖² carries the sign against positivity. The "misaligned" square ‖S(Z^*−Z^{−1})F‖²
measures the non-unitarity of the compressed Euler object; it would vanish if |ζ| = 1. This is the concrete form
of M7's "misalignment" and a coupled square in the sense left open by G2_B3 Cor S2(b).

**At first contact** (F ∈ N, 𝔞_{T_0}(F) = 0):

    (B2.4)  ½‖S(Z^*+Z^{−1})F‖² = 𝔞^∞_{T_0}(F) + 2‖SF‖² + ½‖S(Z^*−Z^{−1})F‖².

Gate 1 needs (B2.4) to be impossible for F ≠ 0. One route is an upper bound
‖S(Z^*+Z^{−1})F‖² < RHS on N. The other is to use H F ∈ span{g_0, g_1} as the vector identity

    (B2.5)  A^∞F = Z X Z^{−1}F + Z^{−*}XZ^*F − 2XF + (polar),

that is, the Euler-conjugated position operator X̃ := ZXZ^{−1} + (ZXZ^{−1})^* satisfies X̃F = (A^∞ + 2X)F
modulo polar. The self-adjoint operator X̃ − 2X is the prime operator, so (B2.5) is H F = 0 rewritten.

### B3. Admissible inputs and their falsifiers (PROVED as classification)

(B2.1)–(B2.5) are identities valid verbatim for any coefficient set b with b*a = a·log, a(1) ≠ 0 (replace Z by
M_T(a)). **They hold for DH.** So the DH line must lie in an estimate of Z or Z^{−1}. The estimates that can
distinguish Z = M_T(1) are exactly these:

| input | what it bounds in (B2.4) | where it is also valid (kill) |
|---|---|---|
| (i) Poisson summation for the integers (Z = integral operator + dual comb) | ‖S(Z^*±Z^{−1})F‖ via ζ_T = (PC) | turns both squares into squares of (PC)/(PC-ren) terms: F2 (R161_099 §2; R161_002) |
| (ii) \|μ\| ≤ 1 (Mertens-type size for Z^{−1}) | ‖SZ^{−1}F‖ ≤ ‖S‖·Σ_{m≤X}m^{−½}‖F‖ | valid for Λχ₂ (\|μχ₂\| ≤ 1); losses are polynomial in X, against the Theorem M margin exp(−exp((2−ε)T)) |
| (iii) Λ ≥ 0, 1 ≥ 0 (positivity-preserving Z, M_T(Λ)) | sign of ⟨SZ^*F, SZ^{−1}F⟩ on F ≥ 0 only | Beurling DMV/Zhang (Λ_B*1 = log, positivity, off-line zeros); F is not ≥ 0 on N (J-parity ε = −1 kernels are sign-changing) |
| (iv) \|a^{−1}\| bounded, i.e. ζ ≠ 0 on Re s > 1 | Z^{−1} growth | **fails for DH** (zeros in σ > 1 make a^{−1}(n) grow like n^{σ_0−1}) — the DH line |

**Proposition B3.** Any argument deriving a contradiction from (B2.4) or (B2.5) that uses only (ii)–(iv) and the
identities of B1–B2 also applies to Λχ₂ with ζ's archimedean data, or to a Beurling DMV system. Both have
(primitive) first contacts, so such an argument proves a falsehood. An argument that also uses (i) enters the
(PC) square and is subject to F2.

*Proof.* B1–B2 are formal in (a, b). (ii) holds for μχ₂, and (iii) holds for Beurling systems, which satisfy B1
with Z_B = Σ_{n∈𝒩_B} n^{−½}τ_{log n} (for real generalized integers the compressions compose by the same convexity
argument). (iv) is implied by (ii). The input (i) is the only one that uses integrality of the support: Poisson
summation over ℤ. It rewrites Z as (PC), and the two squares of (B2.2) as a difference of squares of (PC)-terms.
By R161_099 §2, a quadratic expression in (PC) is invariant under A_M → −A_M, so it cannot orient. ∎

**The DH line.** In (B2.4), DH fails exactly at input (iv): Z_a^{−1} = M_T(a^{−1}) has coefficients of
exponential size in log n. Every other line of B1–B3 holds for DH verbatim. But (iv) is implied by (ii),
which Λχ₂ satisfies, so this line alone cannot close.

**F1 check.** (B2.3) holds for every F. On λ > 0 eigenvectors it gives
½‖S(Z^*+Z^{−1})F‖² < 𝔞^∞ + 2‖SF‖² + ½‖S(Z^*−Z^{−1})F‖², with strict inequality. The only use of λ = 0 is (B2.4)–(B2.5)
at a single window, and A5 is the only use of minimality. Neither is sign-bearing. F1 is therefore not passed
by any closure built on B2 alone.

### B4. What would be needed (OPEN, stated precisely)

A closing lemma must bound the aligned square **below the misaligned one** on N:

    (B4.1)  ‖S(Z^*+Z^{−1})F‖² − ‖S(Z^*−Z^{−1})F‖² = 4⟨SZ^*F, SZ^{−1}F⟩ < 2𝔞^∞_{T_0}(F) + 4‖SF‖²  for 0 ≠ F ∈ N.

The lemma must use integrality ((i)) *non-quadratically*, for instance through the arithmetic of the floor
remainder {X/m} inside Z^{−1} = M_T(μ) paired against Z^* (a Type I sum with μ-weights and position weight S²).
Such a use must not reassemble into the (PC) square. It must also use J-parity or A5 to exclude the sign-constant
vectors on which (iii) acts. No such lemma is known. By R160_M7 Prop 5.2(c), its ∀T version without the
restriction F ∈ N is E1.

### Summary of labels
A1–A5 PROVED (weight-blind or dead). B1, B2 PROVED (exact; B2 new as a conjugation square). B3 PROVED
(classification). B4 OPEN. Route status: **NO-GO for closure in the present form**; the residual is (B4.1).
