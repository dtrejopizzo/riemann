# R185_002 — Positive probe of box O166.802.1: integrality as a nonlinear input

Phase 185. Pure mathematics, no numerics. Read: R166_802 (Thms 0–4, Prop 2.1, Prop 4.1), R166_501 Thm A, R167_101–103 (W-sieve), R184_014, R163_002, R162_2601, CROSSWORD-TO-D §3.2–3.3. RH is not asserted.

## State

**Verdict: NO-GO for box O166.802.1 in the integrality class.** The strongest candidate statement, B_int (nonlinear, multiscale Eulerian integrality), is true for ζ with no zeros and separates every listed falsifier, but it is **closed under deletion of primes beyond X**. That closure reduces the witness exclusion to a lower bound on a count at a single scale, and hence to E1 by R166_802 Thm 2–3. The surviving class is that of statements **not closed under deletion**. Such statements must couple primes > X with primes < X, and the only one of that kind, true and provable without zeros, that we know of is completeness of factorization, 1*Λ = log, which is linear. By (b), that goes back to E1. **The claim that this class contains nothing else is ARGUED, not PROVED.**

| Item | Statement | Label |
|---|---|---|
| Prop A | Chebyshev + 0/1 gives only a lower bound on the **uncorrected** tail (exponent ½); after the polar correction it says nothing | PROVED |
| Prop B | Λ = μ*log / Chebyshev identity (direction (b)) ⇒ Möbius sums ⇒ E1 | PROVED-CITED (Landau, σ_c of 1/ζ) |
| Thm C | Convexity/solidity barrier: a convex, solid statement (downward closed in the ≥ 0 cone) satisfied by 1_P is satisfied by b_θ ⇒ blind to the W-sieve. A convex statement satisfied by all of {0,1}^N is empty | PROVED |
| Thm D | Counting + 0/1: exclusion requires ψ(Xe^Δ) − ψ(X) with relative error η < c·X^{δ_q−½}, which is equivalent to a zero-free region (E1) | PROVED (reduction) + PROVED-CITED (Landau/Ingham) |
| Def/Prop E | B_int (Eulerian integrality): true for ζ with no zeros; false or undefined for b_θ, Λ̃, f_t, M_m, DH, Beurling DMV and L(u,χ) | PROVED |
| Thm F | B_int is closed under deletion of primes > X ⇒ it excludes the witness only via a single K with U_K < 0 (Thm 1) or via counting (Thm D) | PROVED |
| Conj G | Every zero-free true statement not closed under deletion factors through 1*Λ = log | OPEN (ARGUED) |

## 0. Normalization (from R166_802 §1)

Let X = e^{2T_c}, P = primes in [X, Xe^Δ] and a = 1_P ∈ {0,1}^P. Write w_K(p) = (log p) p^{−½} Ψ̌_K(log p).

Tail_K = Σ_p a_p w_K(p) + E_K, with E_K the contribution of prime powers p^k, k ≥ 2. Squares p² ∈ [X, Xe^Δ] contribute Σ (log p)/p ≈ Δ/2·sup|Ψ̌|, which is O(1); powers k ≥ 3 contribute less. Call 𝒫_K := ∫_{2T_c}^{2T_c+Δ} Ψ̌_K(u) e^{u/2} du ≍ e^{T_c} the polar term. The witness restriction is Tail_K ≤ U_K := 𝔄_K − Q_K^{hyp} + S, with 𝔄_K = 𝒫_K + (archimedean + window) and |Q_K^{hyp}| ≲ e^{2δ_q T_c}‖G‖².

## 1. Direction (a): Chebyshev + discreteness. NO-GO

**Prop A. PROVED.** For Ψ̌_K ≥ 0 on the tail, elementary Chebyshev (ψ(2x) − ψ(x) ≥ c₀x with c₀ < 1, no zeros) gives Tail_K ≥ c₀′𝒫_K − O(1) with c₀′ < 1.

*Proof.* Partial sum over the dyadic bound. ∎

Exclusion requires Tail_K > U_K = 𝒫_K − Q + (O(1) + S). That demands (1 − c₀′)𝒫_K < Q − O(1) − S. But the left side is ≍ e^{T_c}, the right side is ≲ e^{2δ_q T_c}, and δ_q < ½. The inequality fails because of the Chebyshev constant. After the polar correction, the bound contributes nothing, consistent with R166_802 Thm 4. An Ω-result for ψ(x) − x of size x^Θ would work, but that is Landau/Littlewood and uses zeros. **NO-GO.**

## 2. Direction (b): two-scale multiplicativity. E1

**Prop B. PROVED-CITED.** The identity Σ_{n≤Y} log n = Σ_{d≤Y} ψ(Y/d) is exact and **linear** in Λ. The nonlinear part, Λ = μ*log, expresses the tail through Σ μ(d)·(…). Any useful bound on these sums is equivalent to the abscissa of convergence of Σ μ(n)n^{−s}, which equals Θ (Landau/Titchmarsh 14.25). Hence it is E1. **E1.**

## 3. Direction (c): convexity and counting

**Thm C (convexity barrier). PROVED.**
(i) Let C ⊂ ℝ^P be convex with {0,1}^P ⊂ C. Then [0,1]^P = conv{0,1}^P ⊂ C, so C carries no information about which integers are prime.
(ii) Let C be convex and *solid* (0 ≤ b ≤ a ∈ C ⇒ b ∈ C) with 1_P ∈ C. Then b_θ/log ∈ C for every θ, because 0 ≤ ½(1 + cos(γ log n + θ)) ≤ 1. Every statement of this type is blind to the W-sieve (R167_102/103).
(iii) Solid statements are exactly intersections of upper bounds Σ c_n a_n ≤ U with c ≥ 0. By R166_802 Thm 1, an upper bound alone never excludes the witness.

*Proof.* (i) is Krein–Milman on the cube. (ii) is immediate by solidity. (iii): a closed, solid, convex set in the orthant is the intersection of half-spaces with normal ≥ 0 (Hahn–Banach separation plus solidity). ∎

**Corollary.** A statement separating ζ from b_θ must be **non-convex** or **non-solid**, i.e. must contain a lower bound.

**Thm D (counting + 0/1 = exponent). PROVED (reduction), PROVED-CITED (equivalence).** Suppose a statement B fixes a ∈ {0,1}^P (any set of partial sums) and adds a lower counting bound ψ(Xe^Δ) − ψ(X) ≥ (1 − η)(e^Δ − 1)X. Let Ψ̌_K ≥ 0 on the tail and 𝒫_K ≍ e^{T_c}. The minimal set of primes compatible with B gives Tail_K ≥ (1 − η′)𝒫_K − O(1), with η′ ≍ η·(relative oscillation of Ψ̌ in the window) + η. Exclusion then reduces to η′𝒫_K < Q_K^{hyp} − O(1) − S, i.e. η ≲ e^{(2δ_q − 1)T_c} = X^{δ_q − ½}.

That condition is a formula for primes in intervals with relative error X^{δ_q − ½} over length ≍ X. By R166_802 Thm 3(b) (Ingham/Landau), it is equivalent to Θ ≤ ½ + δ′ with δ′ < δ_q, which is exactly the absence of the zero. **E1.**

For the family P, the factor G² destroys Ψ̌ ≥ 0 (R164_601 Thm 3.2). In that case the minimal subset sum is taken with the negative-weight p's, and the lower counting bound no longer even gives the lower bound. This reinforces the NO-GO. ∎

**Hand-checked sign.** 2δ_q − 1 < 0, so the right side has a smaller exponent than 𝒫. One needs η → 0 at power speed; the PNT with o(1) (Vinogradov–Korobov, Matomäki–Radziwiłł) is not enough, consistent with CROSSWORD §3.3.

## 4. Direction (d): the candidate statement B_int and why it falls

**Def E.** B_int(Λ) consists of three clauses:
- (I) supp Λ ⊂ {log n : n ∈ ℕ};
- (II) exp(Σ_n Λ(n)(log n)^{−1} n^{−s}) = Σ_n c_n n^{−s} with c_n ∈ ℤ_{≥0};
- (III) c_{mn} = c_m c_n for (m, n) = 1.

The statement is nonlinear (exponential) and multiscale: c_n for n ≈ X·X^{1/2} couples Λ at scales X and X^{1/2}. In R184_014's terms, this is "integrality used nonlinearly".

**Prop E. PROVED.**
- True for ζ: c_n = 1. The proof is the formal Euler product, with no zeros.
- b_θ: c_p = ½(1 + cos(γ log p + θ)) ∉ ℤ for almost every p. **False.**
- Λ̃ (R162_2601): (II)+(III) is precisely the "individual Euler product property" that separates it. **False.**
- f_t, M_m (non-atomic or lacking Λ): **undefined.**
- DH: a linear combination of two L's, no Euler product. (III) fails. **False.**
- Beurling DMV: support outside log ℕ. (I) fails. **False.**
- L(u,χ): c_n = χ(n) ∉ ℤ_{≥0}. **False.**

**Thm F (closure under deletion). PROVED.** Let P′ ⊂ P be an arbitrary set of primes in [X, Xe^Δ]. Define Λ_{P′} = Λ outside [X, Xe^Δ] and Λ_{P′} = (log p)1_{P′} on the primes of the interval, also adjusting the powers p^k that fall in the interval. Then:
1. Λ_{P′} satisfies B_int, because it is the log-derivative of ∏_{p∉P∖P′}(1 − p^{−s})^{−1}, with coefficients in {0,1} and multiplicative.
2. Λ_{P′} preserves the window and the part below X.

Consequently, {(Tail_K(Λ′))_K : Λ′ ⊨ B_int, same window} contains every subset sum {Σ_{p∈P′} w_K(p) + E_K}_K, including P′ = ∅, which gives Tail ≈ (E_K)_K = O(1). Hence:
- B_int together with the window excludes the witness only if **for every P′** there is a K with Σ_{P′} w_K > U_K;
- with P′ = ∅, this requires U_K < O(1) for some K, a single-scale condition that is R166_802 Thm 1 and, by Thm 2, E1;
- if a lower counting bound is added to B_int to exclude ∅, one lands in Thm D and returns to E1. ∎

**Why the other directions fall.** (a) falls because of the Chebyshev constant. (b) is Möbius, E1. (c) alone is convex or a counting statement (Thm C and Thm D). The value of B_int is that it shows that *not even* the strongest nonlinear integrality escapes: the obstacle is not linearity but **closure under deletion of primes**.

**Conj G (surviving class). OPEN, ARGUED.** Box O166.802.1 can only be filled with a statement meeting the following four conditions:
- not convex-solid (Thm C);
- not a single-scale counting statement (Thm D);
- not closed under deletion of primes > X (Thm F);
- true with no zeros.

Non-closure under deletion forces coupling 1_P beyond X with data that deletion alters, i.e. with the **completeness** of ℕ as a generated semigroup. The only known expression of that completeness is 1*Λ = log, which is linear, and leads to (b), i.e. to E1. A new statement in this class would have to use completeness nonlinearly *and* without passing through Möbius sums. We know of no candidate. That is the precise shape of the blank box.

## For the audit

1. **Thm C(iii).** The characterization solid ⟺ intersection of upper bounds with weights ≥ 0 requires C closed. For non-closed C it holds for the closure, and blindness is preserved.
2. **Thm D.** The step from "η ≲ X^{δ_q−½}" to "Θ ≤ ½ + δ′" uses intervals of length ≍ X (Δ fixed), not short intervals. So the equivalence is the classical Ingham one and does not require zero density. Check that η′ and η are comparable with constants depending only on Ψ̌ and Δ.
3. **Thm F.** Deletion alters the powers p^k in [X, Xe^Δ] with p < X only if primes < X are deleted; this is not done here. Powers of p ∈ P′ fall outside the interval for Δ < log X. Check that E_K does not change.
4. **Conj G** is ARGUED: "completeness ⇒ 1*Λ = log" is a statement about known proofs, not a theorem.
5. Nothing is asserted about RH. Every NO-GO is relative to the R166_802 witness restriction.

## For Paper 46

- **Thm C** (convexity/solidity barrier ⇒ blindness to the W-sieve): PROVED. Can accompany the W-sieve lemma of R167_102/103 as a one-line remark.
- **Thm F** (closure under deletion of primes): PROVED. Proposed as a remark in §7 (alongside Thm finZ): Eulerian integrality conditions do not exclude witnesses because the sub-Euler-products ∏_{p∈𝒫′} inherit the window.
- Thm D and Conj G remain as internal notes (E1 and OPEN respectively).

## Note (R185_091)

* FATAL: Thm D as stated is false (a counting bound on [X,Xe^Δ] does not give Tail_K ≥ (1−η′)𝒫_K because Ψ̌_K vanishes at the endpoint; "one scale ⟺ Θ≤½+δ′" is asymptotic). Moves to ARGUED.
* Prop A/§0: the window term of 𝔄_K is not O(1) (PNT error at scale X); dyadic Chebyshev is empty if Δ<log 2. ARGUED.
* Thm F: core PROVED (window and E_K are preserved; exclusion ⟺ ∃K: E_K>U_K); the step "⇒ E1 via Thm 2" is illegitimate (Λ_∅ does not satisfy (1.1)); the logic is proof transfer (W3). Thm C(i)(ii) PROVED; (iii) cite "0∈C ⇒ Tail=E_K". Prop E: Λ̃ separation legitimate; DH and L(u,χ) ARGUED.
* Ready for Paper 46: Thm C(i)(ii), core of Thm F. Not: Thm D, Prop A, "Thm F ⇒ E1".
