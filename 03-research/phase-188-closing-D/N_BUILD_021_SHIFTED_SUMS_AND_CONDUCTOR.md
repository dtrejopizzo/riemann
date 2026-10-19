# N_BUILD_021 — The arithmetic of the Near part of A_M: shifted sums, primes in progressions, and whether the conductor > 1 family enters

Pen and paper. Setting of L2_BUILD_028/029: profile F₀ (|b| > ½, Theorem S), c₀ = c_{F₀} supported in [−2T₀, 2T₀], A_M = [B_{F₀}(log m − log k)]_{m,k≤M},
D ⟺ A_M ⪰ 0 ∀M; A_M = Arch_M − Div_M − Near_M (028 §2).

## Corpus check
phase 167 (R167_102 Thm B "sieve blindness": Λ ≥ 0 + prime-power support + any family of upper bounds Σ Λφ ≤ U_φ — Brun–Titchmarsh, Selberg,
large sieve, Bombieri–Vinogradov-type upper bounds — gives no square-root saving; Theorem S of R167_103: sieves valid for Beurling systems),
R163_602 (twisted prime sums; Bombieri–Hejhal falsifier F2 for linear combinations of L-functions; sieve majorants only for w ≥ 0), R170_811,
Paper 47 cor:void + thm:finmod, N_BUILD_003 (W-tail), N_BUILD_014/015 (Ξ), L2_BUILD_011 rows 15, 18 (character sums KILLED; Dirichlet L, Euler + FE
at q > 1: UNKNOWN), L2_028 §2(c) (characters do not diagonalize Arch). New: Prop 1 (Near = Ξ-kernel), Theorem 2 (progression classes closed
under finite modification), Prop 3 (χ-twisted vectors give hybrid, not L(s,χ), forms), the verdict on row 18.

## 1. Prop 1 (PROVED): what Near is, arithmetically
Near_M(s) = Σ_{m,k≤M} s_m s_k Σ_{n≥2, m≠kn} v_n c₀(log m − log k − log n) = Σ_{m,k} s_m s_k [Ξ_{F₀}(log(m/k)) − 1_{k|m} v_{m/k}c₀(0)],
with Ξ_{F₀}(d) = Σ_n v_n c₀(log n − d) (N_BUILD_014; main term ∫c₀e^{v/2} = A·B = 0). For fixed (m,k), the inner sum runs over n with
|log(kn/m)| ≤ 2T₀: an interval of RELATIVE length e^{±2T₀} around x = m/k, i.e. Σ_{x e^{−2T₀} < n < x e^{2T₀}} Λ(n)n^{−½}c₀(log(n/x)) — a
smoothed count of primes in a multiplicative interval of fixed relative width (not additively short), minus the exact coincidence n = x.
In additive form, m − kn = h with |h| ≲ 2T₀m: the shifted sums Σ_{m − kn = h}s_m Λ(n)(…) appear only through the test vector s; for smooth s
(e.g. s_m = m^{−½}φ(log m)) the m-summation is smooth and the arithmetic reduces to Σ_n Λ(n) W(n/x) — Ξ at scale x. ∎
So the "shifted-convolution" structure of Near is: (local Chebyshev fluctuation Ξ at every scale m/k) × (correlation of the test vector).

## 2. Which classical results control it, and their classes
(a) PNT in multiplicative intervals of fixed relative width (classical error terms; Vinogradov–Korobov): controls Ξ(d) up to e^{d/2}exp(−c d^{3/5}…)
    (N_BUILD_015 §3(b)). Class C_PNT(ε): closed under finite deletion/amplification (thm:finmod(iii)). KILLED by cor:void.
(b) Brun–Titchmarsh / Selberg sieve: upper bounds only; class C_BT; KILLED by cor:void and W-tail (N_003), and blind by R167_102 Thm B.
(c) Primes in progressions — Bombieri–Vinogradov, Barban–Davenport–Halberstam, Siegel–Walfisz, Titchmarsh divisor problem Σ_{p≤x}d(p−1)
    (CITED: these follow from the large sieve plus zero-free regions / Siegel's theorem for L(s,χ)). They enter A_M only if the test vector s
    correlates with residue classes (s_m depending on m mod q), via sums Σ_n Λ(n)1_{kn + h ≡ a (q)}W(n/x) (progressions of modulus q/(q,k)).
**Theorem 2 (PROVED).** Let 𝒞_prog be any class of nonnegative arithmetic functions a containing Λ and defined by asymptotic statements on the
progression sums ψ_a(x; q, c) with error terms that are o(x) as x → ∞ (individually or on average over q ≤ Q(x): Siegel–Walfisz, BV, BDH,
Titchmarsh-divisor asymptotics, Brun–Titchmarsh bounds). Then 𝒞_prog is closed under finite deletion (a = Λ1_{n≥N}) and finite amplification
(a = Λ + c1_{n=n₀}), because these change each ψ_a(x; q, c) by O_N(1) or O(c), which is o(x). Hence by thm:finmod / cor:void, 𝒞_prog contains
members failing WP_T at every window T > T₀(0) (deletion) and at every T > ½log2 (amplification); no argument using only membership in 𝒞_prog
proves D. ∎ (W-tail, N_003, kills the class also when all small values are kept.)
So every classical shifted-sum / progression input, used as a class property, is KILLED. Their "sieve" versions are additionally blind (R167_102).

## 3. Does the conductor > 1 family (input map row 18: Euler + FE at q > 1) enter exactly? (PROVED structural answer)
Progression results use L(s,χ) only through zero-free regions / mean values (class statements, §2). An exact, non-linear use of the Euler product
AND FE of L(s,χ) would require the window form of L(s,χ) to appear inside A_M.
**Prop 3 (PROVED).** Let χ be a Dirichlet character mod q and restrict A_M to twisted vectors s_m = χ(m)u_m with u supported on (m,q) = 1. Then:
 Div(s) = Σ_{k|m} χ(m)χ̄(k)u_mu_k v_{m/k} = Σ_{k|m}χ(m/k)v_{m/k}u_mu_k  — the comb of L(s,χ) (twisted Λχ), exactly;
 Arch(s) = Σ_{m,k}χ(m)χ̄(k)u_mu_k a(log(m/k)) — the archimedean convolution of ζ (real lag log(m/k), no χ(m/k) structure; the Γ-factor of
   L(s,χ) for odd χ, Γ((s+1)/2), does NOT appear);
 Near(s) = Σ_{m,k}χ(m)χ̄(k)u_mu_k Σ_{n: m ≠ kn} v_n c₀(log(m/(kn))) — weights χ(m)χ̄(k) with m ≈ kn but m ≠ kn: NOT χ(n) (χ(m) ≠ χ(k)χ(n) when
   m ≠ kn); it is the untwisted Λ comb against a non-multiplicative phase.
Hence on twisted vectors A_M is a HYBRID: (archimedean of ζ) − (Div of L(s,χ)) − (Near of ζ with phases) — not the window form of L(s,χ)
(whose archimedean part has the Γ-factor of conductor q and parity of χ, and whose Near part has χ(n) weights). ∎
Consequence: the conductor > 1 family does not enter A_M exactly; it enters (i) through Div on twisted vectors, where Div passes trivially
(local Euler bounds, L2_029), and (ii) through progression statistics in Near, which are class statements KILLED by Theorem 2. **Row 18 of the
input map remains UNKNOWN as a falsifier source, but it is not an available input for D through A_M** (PROVED for the two exact routes above;
other routes not excluded).

## 4. Where the sign must sit (summary, ARGUED)
Div passes trivially; Arch is explicit; Near = s^T[Ξ_{F₀}(log(m/k)) − exact part]s: the local fluctuation Ξ at every multiplicative scale, correlated
with the test vector. Theorem T (L2_023) bounds each 2×2 section; Theorem L (N_015) shows Ξ oscillates about 0; Theorem 2 shows no classical
equidistribution input decides it. The sign is a statement about the Toeplitz-in-log(m/k) matrix [Ξ(log(m/k))] on ℕ — a ℤ-integral, all-scales
object — and no input from the conductor > 1 family reaches it exactly.

## Self-review
1. Prop 1: the identification of the inner sum with Ξ at scale m/k is exact (Ξ(d) = Σ v_n c₀(log n − d), d = log(m/k), c₀ even); subtracting the
exact-coincidence atom (n = m/k integer) separates Div. Correct.
2. Theorem 2: closure under finite modification — each ψ_a(x; q, c) changes by a bounded amount independent of x; any o(x) (or even
O(x^{1−δ}) or O(x/(log x)^A) on average) statement is preserved. Correct. Applies to BDH (mean square over q ≤ Q of errors: changed by
O(Q·N²)… must be o(x²/ (log x)^A) — for fixed modification and x → ∞ with Q ≤ x, Σ_{q≤Q}O(1)² = O(Q) = o(x²(log x)^{−A}). Correct.
3. Prop 3: for (k,q) = 1 and m = kn exactly, χ(m)χ̄(k) = χ(n) — correct; for m ≠ kn no relation — correct. The Γ-factor claim: A_M's archimedean
kernel is m(τ) = Re ψ(¼ + iτ/2) − log π (even character, q = 1); L(s,χ) needs Re ψ((¼ or ¾) + iτ/2) + log(q/π) — different. Correct.
4. "Not an available input through A_M" is proved only for the two exact routes (Div on twisted vectors; Near via progressions); stated so.
5. No mention of any equivalence involving row D; L(s,χ) zero location is not invoked.
No sign contact; no negative value certified.
