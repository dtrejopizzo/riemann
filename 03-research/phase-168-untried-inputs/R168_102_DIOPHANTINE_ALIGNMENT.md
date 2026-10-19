# R168_102 — Diophantine alignment of (γ log p mod 2π): can it give (WS*)?

Phase 168, untried inputs, track "Diophantine". Pure mathematics, no numerics. Labels: PROVED / PROVED-CITED /
ARGUED / OPEN. Citations from memory are flagged [mem]. No other file was edited. No label of record moves.

Inputs read: R167_101 (target (WS*), Thm A, Thm C, Cor D), R167_102 (Thm B, Thm D), R167_291 (Lemma K demoted, R5).
Also used: R166_802 (circularity) and 00-references/beurling-dmv (DMV, Broucke–Debruyne–Vindas).

**Corpus check (rule ).** `grep -ri "Baker\|linear forms in log\|Matveev"` over 03-research finds the following:
- phase-45/135 and phase-46/138 ("dos primos"): Baker is used there for two-prime Diophantine facts about log 2/log 3, in a different context.
- R162_2300 master grid: one "Baker no-go" killer.
- R164_291: Baker–Harman–Pintz. This is a different Baker (primes in short intervals).

None of these treats linear forms in logarithms as an input to a single-height twisted prime sum. So the input is new to phase 167/168. The verdict below agrees with the grid's earlier "Baker no-go", and gives a sharper reason.

---

## 0. Outcome

**Verdict: the single-height wall. No genuine Diophantine obstruction exists at γ ≤ Y^A.** Every Diophantine or equidistribution input
on (γ log p)_{p≤Y} falls into one of three classes. Each class either fails to see the point γ_q, or proves too much.

| # | Statement | Label |
|---|---|---|
| Thm 1 | Bilinear blindness: with arbitrary coefficients, the twisted Type II form has sup = trivial (the ℓ¹·ℓ¹ bound); there is no bilinear gain. This contrasts with the additive twist e(αmn) | PROVED |
| Prop 1′ | Type I (smooth inner sums) does get van der Corput / exponent-pair savings at γ ≤ Y^A, but in Vaughan's identity the Type II part with coefficients μ, Λ remains, and its bound is equivalent to the original problem | PROVED (Type I, PROVED-CITED vdC); circularity ARGUED |
| Thm 2 | Large sieve in γ: meas{γ∈[0,Γ]: Re 𝒮(γ) ≥ B} ≤ (Γ+Y)·Σ_{n≤Y}Λ(n)²|w(log n)|²/n / B² ≍ (Γ+Y)(log Y)²‖w‖²_∞/B². Measure statements never exclude a single height | PROVED (MV mean value PROVED-CITED) |
| Prop 2′ | Normalisation correction: the RMS of 𝒮 over γ is ≍ log Y, **not** Y^{1/2}. (WS*) with B ≍ polylog asks for a bound at most a power of log above the mean. "A tiny correlation polylog/Y^{1/2}" is the wrong picture. The relevant comparison is with the sup over γ ≤ Y^A | PROVED |
| Thm 3 | Baker/Kronecker direction: at height γ, quantitative Kronecker aligns ≍ log γ/log(1/ε) primes. This gives Re 𝒮 ≳ (log γ)^{1/2}/log log γ-type values (the Montgomery Ω scale). Baker lower bounds for linear forms make that alignment **easier** to reach (they rule out near-relations), never harder. Diophantine lower bounds are anti-cancellation inputs, so they point the wrong way for an upper bound | PROVED for the direction of logic; Ω-scale PROVED-CITED [mem: Montgomery 1977; Bohr–Jessen] |
| Thm 4 | γ-uniform inputs prove too much: any bound derived only from facts that hold for every real γ (linear independence of log p, Baker–Wüstholz/Matveev bounds, Type I/II estimates) is a bound sup_{γ≤Y^A} Re 𝒮(γ) < B. For all Y that statement implies a zero-free strip, so it is RH-strength (R167_291 R5). No known Diophantine theorem reaches it | PROVED (the implication); unattainability ARGUED |
| Thm 5 | Beurling falsifier: the hypotheses "{log p} ℚ-independent + Baker-type lower bounds + equidistribution in measure" are compatible with prime systems whose zeta has zeros off the line, where (WS*) fails. So these hypotheses alone cannot imply (WS*); integrality of the integers (the Euler product over ℤ) must enter | ARGUED (DMV PROVED-CITED; genericity step ARGUED) |
| M_m | M_m does not falsify Λ-only bounds: 𝒮 is unchanged, and the β_m term pays the witness balance. A Λ-only (WS*) is consistent with M_m, so M_m does not discriminate. Thm 5 is the falsifier that does | PROVED |
| O168.102.1 | Prove sup_{γ∈[Y^{1/A},Y^A]} Re 𝒮(γ) ≤ (log Y)^C from Λ alone | OPEN (RH-strength; equivalent in shape to Lindelöf/RH for log ζ partial sums) |

---

## 1. Bilinear blindness (Thm 1). PROVED.

Let M,N ≥ 1, let a ∈ ℂ^{[M,2M)} and b ∈ ℂ^{[N,2N)} be arbitrary, and put
T_γ(a,b) = Σ_m Σ_n a_m b_n (mn)^{iγ}.

**Thm 1.**
(i) T_γ(a,b) = A(γ)B(γ), with A(γ) = Σ a_m m^{iγ} and B(γ) = Σ b_n n^{iγ}.
(ii) sup_{‖a‖₂=‖b‖₂=1} |T_γ| = (MN)^{1/2}, attained at a_m = M^{−1/2}m^{−iγ} and b_n = N^{−1/2}n^{−iγ}. So Cauchy–Schwarz gives nothing beyond the trivial bound.
(iii) The same holds with a coupling 1_{mn≤Y}: choose a and b as in (ii), restricted to the hyperbolic region. Every term is then nonnegative.

*Proof.* (i) is (mn)^{iγ} = m^{iγ}n^{iγ}. For (ii), the bound |A||B| ≤ ‖a‖₁‖b‖₁ ≤ (MN)^{1/2}‖a‖₂‖b‖₂ is attained at the stated choice. For (iii), each term a_m b_n (mn)^{iγ} = (MN)^{−1/2} > 0. ∎

*Contrast.* With e(αmn) the large sieve gives sup ≪ ((M+N)MN)^{1/2}, a gain of min(M,N)^{1/2} (Vinogradov). The reason is that e(αmn) is not a product in (m,n). This confirms R167_102 Thm D rigorously, in the strong form "sup over coefficients".

**Prop 1′.**
- (a) Type I, PROVED-CITED [mem: van der Corput / exponent pairs, Graham–Kolesnik]. For γ ≤ Y^A and M ≥ γ^{ε}, Σ_{m~M} m^{iγ} ≪ (γ/M)^{κ}M^{λ}, with a power saving whenever M ≫ γ^{κ/(1−λ+κ)}. Short pieces (M ≤ γ^{ε}) get no saving. Type I is not the obstruction.
- (b) Type II, ARGUED. Vaughan's Type II carries coefficients built from μ and Λ. By Thm 1, any saving has to come from the specific coefficients, through a pointwise bound on A(γ) = Σ μ(m)m^{−1/2+iγ}-type polynomials at the single γ. That is the original problem for 1/ζ in place of ζ′/ζ. So the step is circular.

## 2. Large sieve in γ (Thm 2, Prop 2′). PROVED.

Put c_n = Λ(n)n^{−1/2}w(log n) for n ≤ Y. By the Montgomery–Vaughan mean value theorem [PROVED-CITED, mem: MV 1974]:
∫_0^Γ |𝒮(γ)|² dγ = Σ_n |c_n|²(Γ + O(n)).
Also Σ_{n≤Y}|c_n|² ≤ ‖w‖²_∞ Σ Λ(n)²/n = ‖w‖²_∞(½(log Y)² + O(log Y)). Chebyshev's inequality then gives Thm 2.

**Prop 2′.** For Γ ≥ Y, the RMS of 𝒮 is ≍ ‖w‖ log Y. The value Y^{1/2} is the ℓ¹ size and is reached only on resonant γ (Lemma K). This needs log γ ≳ Y/log Y (R167_291), which is outside γ ≤ Y^A. So at the witness scale the issue is not a "tiny correlation fraction". The issue is excluding a deviation of polylog/log Y standard units at one point.

Thm 2 bounds a measure. A single γ_q has measure 0, so Thm 2 says nothing about it. Higher moments (Σ|c|²)^k k!-type for k ≤ log Γ/log Y [mem: MV / Soundararajan-style moments] give at best
meas{Re 𝒮 ≥ B} ≤ Γ·exp(−cB²/(log Y)²).
This is still positive for B = (log Y)^C whenever Γ is large. **No measure statement excludes a single height.** PROVED (trivially: null sets are invisible to integrals).

## 3. What Diophantine theory does at a single height (Thm 3).

- **Baker–Wüstholz / Matveev** [PROVED-CITED, mem: B–W 1993, Matveev 2000]. For b ∈ ℤ^k with Σ b_i log p_i ≠ 0:
  |Σ b_i log p_i| ≥ exp(−C^k ∏ log p_i · log max|b_i|).
  This is a lower bound on how close a *relation* can come to zero. In quantitative Kronecker (Bohr–Jessen; Chen [mem]), such lower bounds control the error terms. They guarantee that every target in 𝕋^k is ε-approximated by (γ log p_i/2π) with γ ≤ exp(O_ε(k log k ...)).
- So Baker gives *upper* bounds on the waiting time for alignment. That is resonance existence, the Ω direction.
- Counting gives the reverse. At height Γ, the curve γ ↦ (γ log p) in 𝕋^k has length ≍ Γ log Y. An ε-net of 𝕋^k has ε^{−k} cells. So at most k ≈ log Γ/log(1/ε) phases can be prescribed. Aligning the first k primes yields Re 𝒮 ≥ Σ_{p≤k log k}(log p/√p)|w| ≍ (log Γ)^{1/2}/(log log Γ)^{O(1)}.
- This matches the Montgomery Ω-scale for log ζ [mem]. It is **below** B ≈ polylog, so it does not threaten (WS*). It also gives no upper bound, because the remaining ≈ π(Y) − k phases are not prescribed and are not controlled either. Controlling them at one γ is again a single-point large-values problem.

**Thm 3 (direction of logic). PROVED.** Every statement of the form "linear forms in log p are not too small" is used, in any argument, only to *produce* γ with prescribed phase vectors. An upper bound on Re 𝒮(γ_q) needs the opposite: "no γ ≤ Y^A has its phase vector in the region {Re 𝒮 ≥ B}". That region is open and has positive Haar measure in 𝕋^{π(Y)}. Whether the curve meets it at the specific point γ_q is not decided by Baker-type lower bounds. Those bounds are satisfied by the curve as a whole and say nothing about which points of it are hit.

## 4. γ-uniform inputs prove too much (Thm 4).

Linear independence of log p, Baker/Matveev bounds, and Type I/II estimates are statements about {log p} or {Λ} that do not mention γ_q. Any conclusion drawn from them about Re 𝒮(γ_q) holds for **every** γ in the same range. It is therefore the uniform bound

(U) sup_{γ ≤ Y^A} Re 𝒮_Y(γ) < B(Y).

**Thm 4. PROVED.** (U), for all large Y with B = (log Y)^C, excludes zeros ρ = β+iγ₀ with β > ½ + (C+2)log log γ₀/log γ₀-type margins at heights γ₀ ≤ Y^A. The proof is Thm A of R167_101 applied with ζ's own witness (Cor D: X^δ is ≫ the polylog at an off-line zero once Δ is chosen per Prop E), or classically through Perron at an off-line zero. So (U) is RH-strength up to the double-log margin. This is R167_291 R5 restated.

Known unconditional bounds for the sup are Y^{1/2}exp(−c(log Y)^{3/5−ε}) [PROVED-CITED, Vinogradov–Korobov]. They come from the zero-free region, not from Diophantine input. ARGUED: no Diophantine theorem on {log p} reaches (U).

## 5. The Beurling falsifier (Thm 5). ARGUED.

Diamond–Montgomery–Vorhauer (2006) [PROVED-CITED; zbMATH record in 00-references/beurling-dmv] construct Beurling primes P whose integer counting satisfies N(x) = ax + O(x^θ), while ζ_P has zeros arbitrarily close to Re s = 1. Hence (WS*) fails for P at its zero heights: the twisted sum is ≍ Y^{β−½} there.

The genericity step is ARGUED. Perturb each Beurling prime by a factor 1+ε_p with ε_p tiny and Lebesgue-generic. Then:
- (log p)_P becomes ℚ-independent;
- Khintchine–Groshev-generic (not very well approximable), which gives Baker-type lower bounds of at least the same quality;
- equidistributed in measure (Thm 2 holds verbatim, since MV needs only the spacing of log n).

The zeros move by o(1), by Rouché on the bounded-change Dirichlet series.

Conclusion: Diophantine and equidistribution hypotheses do not imply (WS*). Any proof must use that P = the rational primes, i.e. the integrality/Euler product over ℤ. This agrees with R167_102 Thm B's atomic falsifier and with R166_802.

**M_m consistency. PROVED.** M_m keeps the atomic Λ, so 𝒮 and every Diophantine fact are unchanged. Its witness identity carries the extra β_m term, which supplies the inserted quartet's amplitude. A Λ-only (WS*) therefore does not contradict M_m. M_m is not a falsifier for Λ-only inputs; the Beurling system of Thm 5 is.

## 6. Ledger and wall

- Closed negative: Diophantine alignment (Baker/Matveev, Kronecker), large sieve in γ, Type II bilinear gain for a multiplicative twist.
- Wall (**single-height wall**). Every Diophantine/equidistribution input is one of the following:
  - (a) a measure statement, blind to a null set (Thm 2);
  - (b) an existence/alignment statement, which points the wrong way (Thm 3);
  - (c) a γ-uniform statement, which equals (U) and is RH-strength (Thm 4).

  Classes (a)–(c) are not separated from the rational primes by any property used (Thm 5).
- Open: O168.102.1 (U). Next useful input must use integrality of ℕ beyond Λ-atomicity. This is consistent with R167_102 and R166_802.
