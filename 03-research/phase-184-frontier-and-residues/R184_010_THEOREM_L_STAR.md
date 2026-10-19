# R184_010 — Theorem L*: error-diffusion rounding refutes L* in the linear model

Pure mathematics, no numerics.
Inputs: R164_201 (§1–§3.5, Lemma W, Theorem L, Theorem L*), R164_291, R184_001 §1, R184_008 §3 (Prop M),
R184_092 (Prop M survives), R163_803 eq. (2.2)–(2.3) (Φ and T). RH is not claimed, nor the closure of row D.

## State

| # | Statement | Label |
|---|---|---|
| 1 | Theorem D (dithered error diffusion): there exists a rounding in 𝒦_θ(3) (in fact, almost surely the random rounding of §2) with sup_{X≤x}\|T₁(X)\| ≪ x^{(1−2a)/4}(log x)^{1/2} | **PROVED** (§2) |
| 2 | Corollary: Theorem L* in the linear model T₁ (rms T₁ ≫ Y^{(1−2a)/2−ε} for every rounding) is **false** | **NO-GO** for L* in the model (PROVED) |
| 3 | Corollary: the "modulus-range gap" q ∈ (Y^{1/2}, Y^{1−ε}) **cannot be closed** with primes: the diagonal mass of the p > Y^{1/2} can be cancelled by a rounding | PROVED (§3) |
| 4 | In the linear model, the frontier in θ is max(θ, (1+θ)/4) from above; the crossing remains at θ = 1/3; below 1/3 the exponent remains > θ (Prop M / Theorem L) | PROVED (upper bound); the crossing at 1/3 remains intact |
| 5 | Sharp exponent (1−2a)/4 in the linear model (= lower bound via Bessel up to Q = Y^{1/2−ε}) | CONDITIONAL on Bessel/large sieve up to Y^{1/2−ε} (OPEN; §4) |
| 6 | Theorem L* in the full system (with the composite terms γ_m, m = p₁⋯p_k) | **OPEN**; heuristic in §5: composites cannot be diffused and might force Y^{(1−2a)/2−o(1)} — ARGUED, not proved |
| 7 | O184.001a (reopening the frontier below 1/3) | **not reopened**: the rounding of §2 gives exponent (1+θ)/4 > θ for θ < 1/3 |
| 8 | FLAG on equidistribution of p^a mod 1 | remains CITED from memory (Vinogradov; discrepancy: Leitmann 1977, Baker–Kolesnik 1985), no local copy; Theorem D **does not use it** |
| 9 | Row D movement | none |

## 1. Setup (from R164_201 / R163_803)

a = θ/(1−θ) ∈ (0, ½), X = x^{1−θ}. Generalized primes at v_{p,k} = p^{k/(1−θ)}, integer multiplicities b_{p,k} ≥ 0,
|b_{p,k} − c_{p,k}| ≤ C (class 𝒦_θ(C)). By R163_803 (2.3):

  N_𝒫(x) = (1−θ)x Σ_{m≤X} γ_m/m + ζ(−a) Σ_{m≤X} γ_m m^a + x^θ T(X),  T(X) = Σ_{m≤X} γ_m Φ(X/m),

with Φ(Y) = −ψ(Y) − aY^{−a}∫_Y^∞ ψ(t)t^{a−1}dt, |Φ| ≤ 1, Φ = −ψ + r, |r(Y)| ≤ a/(4Y), r′ ≪ 1/Y.
Only integer X matter (R163_803, proof of Lemma 4). The linear term is

  T₁(X) = Σ_{p≤X} ε_p p^{−a} Φ(X/p),  ε_p = b_{p,1} − p^a ∈ ℤ − p^a, hence |ε_p| ≥ ‖p^a‖ (Lemma W(i)).

**L\* (R164_201 §3.5):** for every rounding, rms_{[Y,2Y]} E ≫ Y^{a+(½−a)−ε}, i.e. rms T₁ ≫ Y^{(1−2a)/2−ε}.
The goal was to close the modulus range q ∈ (Y^η, Y^{1−ε}) in the Bessel argument. Result: in the linear model
the statement is false, so the gap is not merely technical.

## 2. Theorem D (dithered error diffusion)

**Construction.** Order the primes p₁ < p₂ < …. Let U_k be i.i.d. uniform on (−½, ½), S₀ = 0, and for k ≥ 1:

  z_k = p_k^a (1 − S_{k−1}),  b_{p_k,1} = ⌊z_k + U_k + ½⌋,  ν_k := b_{p_k,1} − z_k,  S_k := S_{k−1} + ε_{p_k} p_k^{−a}.

The Witt levels k ≥ 2 are rounded in any bounded way (e.g. the same way).

**Lemma D1.** (i) ν_k ∈ (−1, 1) and E[ν_k | 𝓕_{k−1}] = 0, where 𝓕_{k−1} = σ(U₁,…,U_{k−1}).
(ii) S_k = ν_k p_k^{−a}, so that |S_k| < p_k^{−a}.
(iii) ε_{p_k} = ν_k − S_{k−1}p_k^a, so |ε_{p_k}| < 1 + (p_k/p_{k−1})^a ≤ 3, ε_{p_k} ∈ ℤ − p_k^a and b ≥ 0. The system is in 𝒦_θ(3).

*Proof.* (i) For fixed z and V = U + ½ uniform on (0,1): E⌊z+V⌋ = ⌊z⌋ + P(V ≥ 1 − {z}) = ⌊z⌋ + {z} = z, and
|⌊z+V⌋ − z| < 1. Since z_k is 𝓕_{k−1}-measurable and U_k is independent of 𝓕_{k−1}, (i) follows.
(ii) ε_{p_k} = b − p_k^a = ν_k + z_k − p_k^a = ν_k − S_{k−1}p_k^a, so S_k = S_{k−1} + ν_k p_k^{−a} − S_{k−1} = ν_k p_k^{−a}.
(iii) Follows from (ii) by induction. b ≥ 0 because z_k > 0 (|S_{k−1}| < 1) and z_k + U_k + ½ > 0. ∎

> **Theorem D.** Let 0 < a < ½. Almost surely there exists X₀ such that for every integer X ≥ X₀
>   |T₁(X)| ≤ C_a X^{(1−2a)/4} (log X)^{1/2}.
> Moreover Σ_{p≤X} ε_p = O((log X)^{1/2}) and x Σ_{p>X} ε_p p^{−1−a} = O(1) a.s. In particular there exists a
> deterministic rounding in 𝒦_θ(3) with that bound.

*Proof.* Fix integer X, K = π(X), f(p) = Φ(X/p) and Δ_k = f(p_k) − f(p_{k+1}).

*Abel.* With ε_{p_k}p_k^{−a} = S_k − S_{k−1}:

  T₁(X) = S_K f(p_K) + Σ_{k<K} S_k Δ_k = O(1) + M(X),  M(X) := Σ_{k<K} ν_k p_k^{−a} Δ_k.

The coefficients p_k^{−a}Δ_k are deterministic and the ν_k are martingale differences bounded by 1.
Azuma–Hoeffding gives

  P(|M(X)| > t) ≤ 2 exp(−t²/(2V(X))),  V(X) := Σ_{k<K} p_k^{−2a} Δ_k².

*Variance.* We have |Δ_k| ≤ 2, so Δ_k² ≤ 2|Δ_k|. For the block p_k ∈ [P, 2P), Σ|Δ_k| ≤ Var_{[P,2P+o(P)]} Φ(X/·).
Φ(X/·) = −ψ(X/·) + r(X/·). The first term has ≪ X/P + 1 jumps of size 1 plus continuous variation ≪ X/P;
the second has variation ≪ 1. Hence

  Σ_{p_k∈[P,2P)} p_k^{−2a}Δ_k² ≪ P^{−2a} min(X/P + 1, P).

Summing over dyadic P: for P ≤ √X the sum is ≪ P^{1−2a}, increasing up to X^{½−a}; for P ≥ √X it is
≪ X P^{−1−2a}, decreasing from X^{½−a}; the +P^{−2a} term is summable because a > 0. Hence **V(X) ≪ X^{½−a}**.

*Union bound and Borel–Cantelli.* Take t = A (V log X)^{1/2} with A² > 6. For X ∈ [Y, 2Y] the failure probability is
≤ 2Y·Y^{−3} (there are only Y integers), which is summable over Y = 2^j. Borel–Cantelli gives the bound for all large X, a.s.

*Boundary terms.* First, Σ_{p≤X}ε_p = Σ_k (S_k − S_{k−1})p_k^a = S_K p_K^a − Σ_{k<K} S_k(p_{k+1}^a − p_k^a).
The first term is ν_K = O(1). The second is Σ ν_k p_k^{−a}(p_{k+1}^a − p_k^a), with variance ≪ Σ_k g_k²p_k^{−2} < ∞
(g_k is the prime gap), so it is O((log X)^{1/2}) a.s. by the same argument. Second, Σ_{p>X}ε_p p^{−1−a}
has, by Abel, size ≪ X^{−1−a}, and x = X^{1+a}. ∎

**Remark (why it works).** ε_p p^{−a} = Δ(ν p^{−a}) is the **first difference** of a martingale sequence. The
rounding is "blue noise": at scale P the sawtooth p ↦ ψ(X/p) is smooth between jumps (P > √X) and the difference
cancels it except at the ≍ X/P jumps; if P < √X the sawtooth is noise at the prime scale and the variance is the diagonal
P^{1−2a}. The maximum of min(X/P, P)·P^{−2a} is at P = √X.

## 3. Consequences for L* and for the modulus-range gap

**Corollary 1 (NO-GO, PROVED).** In the linear model, for θ < 1/3 there exists a rounding with

  x^θ T₁ ≪ x^{θ}·X^{(1−2a)/4+ε} = x^{(1+θ)/4+ε},

because X^{a+(1−2a)/4} = X^{(1+2a)/4} and (1−θ)(1+2a) = 1+θ. Now (1+θ)/4 < (1−θ)/2 ⟺ θ < 1/3. Hence the linear
form of L* (exponent (1−θ)/2) is **false**.

**Corollary 2 (the gap is not technical, PROVED).** The proposed argument (Bessel against {ψ(X/q)}_{q prime ≤ Y^{1−ε}},
using only |ε_q| ≥ ‖q^a‖, with no sign information) would give rms T₁ ≫ Y^{(1−ε)(½−a)} for *every* rounding. Theorem D
contradicts this. So no large sieve over prime moduli q ∈ (Y^{1/2+δ}, Y^{1−ε}) can hold with arbitrary weights
satisfying |ε_q| ≥ ‖q^a‖. The concrete reason: for q > Y^{1/2} the sawtooths ψ(X/q), X ∈ [Y, 2Y], are functions of q of
variation ≍ Y/Q per block, and a sequence with bounded partial sums is nearly orthogonal to all of them
simultaneously. The "dimension count" of R184_008 §3.3 (O184.001a-yes) is realized explicitly in the
range q > Y^{1/2}.

**Corollary 3 (the frontier at 1/3 does not move).** (1+θ)/4 > θ ⟺ θ < 1/3. The best-known rounding still has
exponent > θ below 1/3. This agrees with Theorem L (PROVED) and Prop M, which remain standing: Lemma D1(iii) satisfies
|ε_p| ≥ ‖p^a‖ and κ, η < ½. O184.001a is **not** reopened.

## 4. The sharp exponent in the linear model (CONDITIONAL)

The lower bound that would make Theorem D sharp is Bessel for {ψ(X/q)}_{q ≤ Q} with Q = Y^{1/2−ε}.
- In that range the products qq′ ≤ Y^{1−2ε} fit in the window. The bilinear form ∫_Y^{2Y}|Σ_q c_qψ(X/q)|² is
  compared with Y·(Franel form) Σ c_q c_{q′}gcd(q,q′)²/(12qq′), via Montgomery–Vaughan (frequencies n/q with
  separation ≥ 1/(qQ)).
- One would still need to control the part q > Q of T₁ against those tests: this is step (c) of Prop M, which today forces η < ½.
- If both are closed: inf_{rounding} rms T₁ = Y^{(1−2a)/4 ± o(1)}, and the exponent of the model is exactly
  max(θ, (1+θ)/4).

Status: **CONDITIONAL** on that large sieve (OPEN; not written here). R164_201 §3.5 already anticipated "≈ Y^{1/2}." Theorem D
shows that Y^{1/2} is the ceiling of that method.

## 5. The full system: composites (OPEN, heuristic ARGUED)

T(X) = Σ_m γ_m Φ(X/m) includes m = p₁⋯p_k with γ_m = ∏γ_{p_i} (H is multiplicative), as well as prime powers.
- **Prime powers.** The powers p^j (Witt levels j ≥ 2) admit their own dither (sequence p ↦ p^j, weights
  p^{−ja}). Variance ≪ X^{(1−2ja)/(2j)}: harmless.
- **Composites, the obstacle.** Their rounding is not free: it is the product of the ε_{p_i}. Heuristic (ARGUED) with
  the rounding of §2:
  - For k = 2 and p, q ~ X^{1/3}, the function (p,q) ↦ ψ(X/pq) oscillates at the scale of the prime lattice (moving to
    the next prime, X/pq changes by ≍ log). Double differences gain nothing, and the block variance is
    ≍ Σ (pq)^{−2a} ≈ X^{(2/3)(1−2a)}.
  - For k primes ~ X^{1/(k+1)} one gets ≈ X^{(k/(k+1))(1−2a)}, with factors (log log)^k/k!.
  - Letting k → ∞ slowly, this gives rms X^{(1−2a)/2 − o(1)}, the size of L*.
- Hence L* in the full system is **not** refuted. If true, the mechanism is not that of R164_201 §3.5
  (primes up to Y^{1−ε}). It would be a **multiplicative rigidity**: a rounding of the primes cannot simultaneously
  diffuse all the products γ_{p₁}⋯γ_{p_k}, whose moduli m = p₁⋯p_k range over (Y^{1/2}, Y) with tests ψ(X/m) that, for
  m with factors ≤ Y^{1/(k+1)}, remain "noise."
- The likely version for the audit (OPEN): let **L\*\_comp** be the statement that for every rounding in 𝒦_θ(C),
  rms T ≫ Y^{(1−2a)/2 − o(1)}. Integrality gives |γ_m| ≥ ∏‖p_i^a‖p_i^{−a}, but a sign-blind Bessel over
  m ≤ Y^{1−ε} is impossible for the same reason as in Corollary 2 *if* the ε_p were free. One would have to use that
  ε_{p₁p₂} = ε_{p₁}ε_{p₂} is determined, and no argument on record does this.

It is also not proved that the rounding of §2 gives, for the full E, anything better than (1−θ)/2: the heuristic says it does not.
As a construction, O184.001a still fails to improve on Theorem C for the full system. **What is at stake:** if the
heuristic failed and the dither also diffused the composites, the full system would have error x^{(1+θ)/4+o(1)}
< x^{1/3}, with zeros of ζ(w) at Re s = (1+θ)/2 > ½. That would resolve O164.201a. The question is thus concentrated at
a single point (O184.010a, OPEN): **do the products γ_{p₁}⋯γ_{p_k} of the dithered rounding have variance
X^{(1−2a)/2−o(1)} or less?**

## 6. Ledger

| Item | Label |
|---|---|
| Lemma D1 (dither: ν martingale, S_k = ν_k p_k^{−a}, system in 𝒦_θ(3)) | PROVED |
| Theorem D: sup\|T₁\| ≪ X^{(1−2a)/4}√log a.s. | PROVED |
| L* in the linear model | NO-GO (false) |
| Gap q ∈ (Y^{1/2+δ}, Y^{1−ε}) closable with primes and without signs | NO-GO |
| Sharp linear exponent (1+θ)/4 | CONDITIONAL (Bessel up to Y^{1/2−ε}, OPEN) |
| Frontier θ = 1/3 (exponent > θ) | intact: Theorem L PROVED, Corollary 3 |
| L* / L\*\_comp in the full system | OPEN; heuristic ARGUED in favor via composites |
| Equidistribution of p^a mod 1 | CITED from memory, FLAG remains open (not used here) |
| Row D | unchanged |

## For the audit

1. Lemma D1(i): the unbiasedness of ⌊z+V⌋ requires V uniform on (0,1) and independent of z. Verify that z_k depends
   only on U₁,…,U_{k−1}.
2. Abel in Theorem D: check the boundary term S_K f(p_K) and that no term for p ≤ X with p = p_K, X not prime, is missing.
3. Var Φ(X/·) on [P,2P]: check that r(Y) = −aY^{−a}∫_Y^∞ψt^{a−1} has variation O(1) on all of [1, ∞)
   (r′ = O(1/Y²)·… bound carefully).
4. Azuma: the coefficients p_k^{−a}Δ_k depend on X but not on the randomness. The union bound over integer X ∈ [Y,2Y] is
   legitimate because N depends only on ⌊X⌋ (R163_803).
5. Does Theorem D contradict Theorem L or Prop M? Check: lower exponents κ(½−a), η(½−a) < (½−a)/2.
6. §5 is heuristic. In particular, the claim that double differences gain nothing for p, q ~ X^{1/3} must be
   verified or refuted. If it failed (i.e. if the dither also diffuses the composites), L* would be false in the
   full system, with exponent (1+θ)/4 + (corrections), and O184.001a would need to be reevaluated.
7. Check the conversion (1−θ)(1+2a)/4 = (1+θ)/4. Note: (1+θ)/4 < 1/3 for θ < 1/3, while the zeros of
   ζ(w) fall at Re s = (1+θ)/2 > ½. If point 6 failed in favor of the dither, the full system would answer
   O164.201a (error O(x^{θ′}), θ′ ≤ 1/3, with zeros off the line). That does not reopen "exponent ≤ θ," but it does
   reopen problem 6 with θ₀ = 1/3. Today it holds only in the linear model.

## Note (R184_093)

* MAJOR: Cor 3 / row 7 "O184.001a is not reopened" does not hold; it should read "reduced to O184.010a" (resolved negatively in R184_013, ARGUED). Cor 2 is only PROVED in a narrow form; the near-orthogonality of the sawtooths is ARGUED.
* Corpus erratum (R164_201 §1, R184_001 §1.1/1.3): the order-2 chaos has variance ≍ X^{1−2a}·loglog/log, of the same order as the linear one; level k diverges for θ<1/(2k+1). Exponent (1−θ)/2 and Theorem L do not change.
