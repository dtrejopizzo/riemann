# R169_101 — Eratosthenes induction: W_T ≥ 0 ⇒ W_{T+Δ} ≥ 0 for Δ ≤ T?

Memo. No numerics. Labels: PROVED / PROVED-CITED / ARGUED / OPEN.
Inputs: R169_000 v2, R169_091, R169_190, R163_702 §3, R163_401 §1–2, R165_202 §1, Paper 47, Paper 48 `thm:M`.
Notation (R163_401 §1): v_n = 2Λ(n)/√n, σ_T = m − Σ_{log n<2T} v_n cos(τ log n), c_F(u)=∫F(t)F̄(t−u)dt,
W_T = 𝔞_T + 2Re(AB̄) on 𝒟_T ⊂ L²(I_T). X = e^{2T}, X' = e^{2T'}, T' = T+Δ, 0 < Δ ≤ T (so X' ≤ X²), z := √X' ≤ X.

## Status (one line)

The induction step is formulated exactly (Box 1) and reduced exactly (Box 2, Box 3). It is **not proved** in any range
beyond what direct certificates give. Obstruction: (i) Theorem M forces the step to be an exact cancellation of size
exp(−½e^{(2−ε)T}), so every Legendre/Type I estimate (remainders polynomial in X at best) is useless (wall W2);
(ii) used as an exact identity, the Eratosthenes link is equivalent to **"the integers are exactly ℕ"** (Prop 5), which
singles out the single object ζ: there is no class on which the step is a law, so the step at fixed (T,Δ) is a finite
certificate and the infinite content is again the quantifier over T. The relaxed class "N(x) = x + O(x^θ)" is the
natural law-carrying class; DMV sits at θ ≈ ½ and falsifies θ ≥ ½; θ < ½ is an OPEN Beurling question (§6). The method
does not reproduce ½log5 from ½log2 except as a restatement of the certificate (§7).

---

## §1 The exact decomposition (task 1)

**Lemma 1 (support bookkeeping). PROVED.** For F ∈ L²(I_{T'}) and u ≥ 2T, c_F(u) = ∫_{u−T'}^{T'} F(t)F̄(t−u)dt involves
F only on R_u := (u−T', T') and L_u := (−T', T'−u), each of width ε_u := 2T'−u ≤ 2Δ. Since u−T' ≥ T−Δ, the strips
lie in (T−Δ, T') and (−T', −T+Δ). They are pure annulus strips (contained in I_{T'}∖I_T) iff ε_u ≤ Δ, i.e. u ≥ 2T'−Δ = 2T+Δ;
for u ∈ [2T, 2T+Δ) they reach into the old domain by u−T'−T < 0. ∎

**Proposition 1 (activation identity). PROVED** (from R165_202 1.1–1.2). Split L²(I_{T'}) = H₀ ⊕ H₁, H₀ = L²(I_T),
H₁ = L²(I_{T'}∖I_T), F = F₀ + G. Then, with W_∞ the extended form of R165_202 1.1,
$$
W_{T'}(F)=W_T(F_0)+2\,\mathrm{Re}\,W_\infty^{\rm old}(F_0,G)+W_\infty^{\rm old}(G)\;-\;\sum_{X\le n<X'}v_n\,\mathrm{Re}\,c_F(\log n),
$$
where W_∞^{old} is the sesquilinear form with symbol σ_T (archimedean m, comb log n < 2T, polar term), and the last sum is
the **activated part** 𝒩_{T,T'}(F) := Σ_{X≤n<X'} v_n Re c_F(log n). By Lemma 1, 𝒩 has no F₀–F₀ part
(c_{F₀}(u) = 0 for u ≥ 2T: R165_202 1.1), so
𝒩(F) = 2Re 𝒩(F₀,G) + 𝒩(G) (cross terms only from u < 2T+Δ). ∎

## §2 The induction step (task 2)

Write W_{T'} = [[W_T, C],[C*, D]] on H₀ ⊕ H₁, C = W_∞^{old}(·,·)|_{H₀×H₁} − 𝒩(·,·)|_{H₀×H₁}, D = W_∞^{old}|_{H₁} − 𝒩|_{H₁}.

**Theorem 2 (Schur form of the step). PROVED** (standard; closed semibounded forms, Paper 47 thm:O gives compact resolvent
so λ_T is an eigenvalue with eigenvector F_T). Assume λ_T > 0. Then W_{T'} ≥ 0 ⟺ D − C*W_T^{−1}C ≥ 0 as a form on H₁.
In particular, a **necessary** condition is, for every G ∈ H₁ ∩ 𝒟,
$$
|C(F_T,G)|^2\le\lambda_T\,D(G)\qquad(\|F_T\|=1). \tag{N}
$$
*Proof.* Block LDL*; (N) is positivity of the 2×2 compression to span{F_T, G}. ∎

> **Box 1 (the Eratosthenes induction step, exact).** For T > 0, 0 < Δ ≤ T:
> (Step_{T,Δ})  λ_T > 0 ⇒  D_{T,T'} − C_{T,T'}^* W_T^{−1} C_{T,T'} ≥ 0 on H₁,
> where C, D contain the activated part −𝒩_{T,T'} built from {v_n : X ≤ n < X'}, and Λ on [X, X') is the
> Eratosthenes image of Λ on [1, X) (Prop 3).

**Corollary 2′ (no perturbative step). PROVED** (from Theorem 2 and Paper 48 thm:M(b), PROVED in the record).
For T ≥ T₀(ε), (N) forces |C(F_T,G)| ≤ exp(−½e^{(2−ε)T}) D(G)^{1/2} for all G. The activated cross term
𝒩(F_T,G) has individual summands of size v_n‖F_T 1_{strip}‖‖G‖ ≍ X^{−1/2}log X × (edge mass of F_T). Hence the step
holds only if C(F_T,·) — old symbol plus activated primes — **cancels** to doubly-exponential accuracy on every annulus
direction. No estimate of 𝒩 with error ≥ exp(−e^{(2−ε)T}) — in particular no Legendre, Brun, Selberg, Bombieri–Vinogradov
or Type I/II estimate, all of which lose at least a power of log X — can prove (Step). This is wall W2 / code M. ∎
(The edge mass of F_T is not small enough to help: if it were ≤ exp(−e^{2T}), C(F_T,·) would be negligible and (Step)
would follow from D ≥ 0 on H₁, which is itself the statement on the annulus; edge decay of F_T is OPEN and under RH
the radical vectors of thm:M are not edge-concentrated — ARGUED.)

## §3 The Legendre form of the activated part (task 3)

**Proposition 3 (Eratosthenes determination). PROVED.** For X ≤ n < X' ≤ X², Λ(n) > 0 iff n = p^k; if k ≥ 2 then
p < √X' ≤ X; if k = 1 then n is prime iff (n, P(z)) = 1, P(z) = ∏_{p<z}p, z = √X' ≤ X. So
1_{n prime} = Σ_{d | (n,P(z))} μ(d), and the window primes < z decide everything. ∎

**Proposition 4 (Legendre decomposition of 𝒩). PROVED.** Let g_F(x) := (2 log x/√x) Re c_F(log x). Then
$$
\mathcal N_{T,T'}(F)=\sum_{\substack{p^k\in[X,X')\\k\ge2}}v_{p^k}\mathrm{Re}\,c_F(\log p^k)
+\underbrace{\Big(\prod_{p<z}(1-\tfrac1p)\Big)\int_X^{X'}g_F(x)\,dx}_{\mathcal N^{\rm main}}
+\underbrace{\sum_{d\mid P(z)}\mu(d)\Big(\sum_{X\le dm<X'}g_F(dm)-\tfrac1d\int_X^{X'}g_F\Big)}_{\mathcal N^{\rm Leg}} ,
$$
and by Euler–Maclaurin each bracket equals −∫_X^{X'} g_F(x) dψ₁(x/d) (ψ₁(y) = {y} − ½) up to boundary terms
ψ₁(X/d)g_F(X) − ψ₁(X'/d)g_F(X'). ∎ (Identity; the d-sum has 2^{π(z)} terms.)

**Proposition 4′ (the "main term" is wrong by a constant factor). PROVED-CITED** (Mertens, FROM MEMORY:
∏_{p<z}(1−1/p) ~ e^{−γ}/log z). With z = √X', 𝒩^{main} has density e^{−γ}·(2/log X')·(2 log x/√x) ≈ 2e^{−γ} ≈ 1.123 times
the true prime density 1/log x near x ≈ X' (and up to ≈ 2.25 near x ≈ X when X' ≈ X²). So 𝒩^{main} does **not**
reconstruct the archimedean-like density; 𝒩^{Leg} is of main-term size, not an error. Consequence: the decomposition
"smooth part absorbable into m(τ) + small Legendre remainder" is false. The smooth part of the true density
(2 log x/√x)(1/log x) = 2/√x is, in τ, the Fourier transform of 2e^{u/2}·1_{[log X, log X')}, a low-frequency bump of
height ≍ √X'·(window) which is the truncated pole term; it is not of the form m(τ) ~ log|τ| (which comes from Γ, not
from primes). ARGUED (the pole term is what the polar part 2Re(AB̄) balances, Paper 47; not re-derived here).

**Proposition 4″ (Fourier side). PROVED** (formal identity; ARGUED for the contour bookkeeping).
Σ_{(n,P(z))=1} n^{−s} = ζ(s)E_z(s), E_z(s) := ∏_{p<z}(1−p^{−s}), entire. On [X, X') the rough integers are exactly the
primes, so with smooth Perron weights the new-prime polynomial is
Σ_{X≤p<X'} (log p) p^{−s} w = (1/2πi)∫ −(ζE_z)'(s+w) ŵ(w) dw. The only pole of ζE_z is s+w = 1 with residue E_z(1)
(the Mertens factor of Prop 4′). **Zeros of ζ do not appear** (ζE_z is regular there). Shifting the contour to the left
leaves ∫ (ζE_z)'(½+iτ+w)… on Re(s+w) = ½ (or lower), whose size is governed by |ζ(½+it)E_z(½+it)|; and
|E_z(½+it)| ranges up to exp((2+o(1))√z/log z) = exp(X'^{1/4}(4+o(1))/log X') (take t with p^{−it} ≈ −1 for all p<z,
Kronecker). The 2^{π(z)} blow-up of the identity is this growth. So the activated symbol is
−2Re Σ v_p p^{−iτ} = (Mertens pole term) + (critical-line integral of the window-truncated sieve series ζE_z).

## §4 Key question: (a), (b) or (c)? (task 4)

1. **(c)-attempt — exact identity, no truncation.** With all d | P(z), 𝒩^{Leg} is exactly the prime part minus the
   Mertens term; as an operator on H₀⊕H₁ it is the form with kernel Σ_p v_p δ(t−s−log p) (symmetrized) minus a smooth
   kernel. **Sign structure. PROVED (negative):** the new-prime measure ν = Σ v_p δ_{log p} is positive, so its
   symmetrization ν_s gives the form F ↦ ∫ν_s c_F whose Fourier symbol Σ v_p cos(τ log p) is a positive-definite
   *function*, not a nonnegative one; the form is indefinite with spectrum ±(v_p/2)-type on strips (R165_202 1.2), and
   subtracting the smooth Mertens kernel does not change indefiniteness (the smooth kernel is of lower rank-type in the
   strip coordinates — ARGUED). No positivity/sign property of the exact Legendre remainder operator exists on PW-type
   tests beyond the trivial |Σ v_p cos| ≤ Σ v_p (attained at τ = 0). ARGUED that nothing finer exists, since the only
   structural datum E_z on the critical line has no sign (|E_z| fluctuates between ≈ exp(−c√z/log z) and exp(c√z/log z)).
2. **Is the step equivalent to positivity of a form with symbol σ_T + (window Euler data)?** Yes formally (Prop 4″):
   σ_{T'} = σ_T − Σ_{p^k∈[X,X')}… and the prime part is the critical-line integral of (ζE_z)'. But ζ itself appears
   (the sieve series is ζ·E_z, not E_z alone): the "window data" do not replace the tail; they multiply it. So the step
   in this form is **circular through ζ on the critical line**, i.e. through all zeros at once — **(a)**: a positivity
   statement on |ζE_z| over all τ is uniform in the frequency and is killed by R168_102 Thm 4 (RH-equivalence of uniform
   bounds; ARGUED-transfer, Thm 4 is in the record). PROVED that ζ appears; ARGUED the Thm 4 classification.
3. **Truncated sieve.** Replacing all d | P(z) by d ≤ D (Brun/Selberg/Rosser–Iwaniec) gives one-sided bounds with the
   parity barrier (Selberg): upper bound ≈ 2× truth, lower bound 0 for the linear sieve at level D = X'^{1/2}. The
   needed accuracy (Cor 2′) is doubly exponential; parity loses a constant factor. **(b)**, and dead by W2 before
   parity matters. PROVED-CITED (parity barrier, FROM MEMORY) + Cor 2′.
4. **Verdict on (c).** The exact window identity A8 asks for exists (Prop 3/4), but its only analytic content is
   "integers = ℕ" (Prop 5); as an identity it carries no inequality, and every inequality extracted from it falls into
   (a) or (b). ARGUED (exhaustion of the three outputs of an identity: exact restatement, uniform bound, truncated bound).

## §5 What the Eratosthenes hypothesis really is

**Proposition 5. PROVED.** Let 𝒫 be a Beurling g-prime system with g-integer counting N_𝒫. "For every X, the g-primes in
[X, X²) are the g-integers in [X, X²) with no g-prime factor < X" holds for **every** Beurling system (unique formal
factorization). For ℤ the extra content is that the g-integers are ℕ with multiplicity one, i.e. N(x) = ⌊x⌋; and
N_𝒫(x) = ⌊x⌋ for all x ⟹ ζ_𝒫 = ζ ⟹ Λ_𝒫 = Λ (log of a Dirichlet series with constant term 1 is unique). ∎
**Reading.** "Primes in [X,X²) are determined by primes < X" is not a restriction on primes; the determination is
relative to the integer lattice. The ℤ-specific input is the **additive** fact N(x) = x + O(1). The Eratosthenes
hypothesis therefore selects one object; a step "for all systems satisfying the hypothesis" is a statement about ζ
alone, and at fixed (T, Δ) it is a finite computation (R169_000 v2). The only way to get a *law* is to relax to a class:
(E_θ): N_𝒫(x) = Ax + O(x^θ). (This is the integer-side hypothesis of Beurling theory.)

## §6 Falsifier table (task 5)

| model | Eratosthenes hyp. (integers = ℕ) | relaxed (E_θ) | step for it | verdict |
|---|---|---|---|---|
| ζ | holds | θ = 0 | = row D | target |
| M_m (ζ × rational quartet factors) | **fails**: its prime-side measure = Λ (atomic, Eratosthenes) + β_m(u)du (smooth exponential sum from the quartets); β_m on [X,X') is not the sieve image of the window — the sieve map outputs atoms only. PROVED (β_m ≢ 0 on every interval, exponential polynomial) | not a Beurling system (signed, non-atomic) | step fails at T_c(M_m) (record) | consistent: R163_702 §3 counterexample violates the hypothesis. PROVED |
| f_t (no Euler product) | fails (no prime measure; R163_901) | n/a | — | excluded |
| Davenport–Heilbronn, f_χ combos | fail (no Euler product) | n/a | — | excluded |
| DMV (Diamond–Montgomery–Vorhauer) | holds relative to own g-integers (Prop 5) but integers ≠ ℕ | N = Ax + O(x^{1/2+o(1)})-type (FROM MEMORY, flag) | false (zeros → σ=1) | falsifies any law using (E_θ) with θ ≥ ½. PROVED-CITED (FROM MEMORY) |
| Cramér random primes | integers ≠ ℕ | θ ≈ ½ typically | — | no information (R169_091) |
| ζ_K, [K:ℚ] = d | ideal sieve holds; integers = ideals, N_K(x) = c_K x + O(x^{1−2/(d+1)}) (Landau, FROM MEMORY) | θ = 1−2/(d+1) ≥ ½ for d ≥ 3 | would give GRH(K) | not a falsifier (GRH believed); but shows (E_θ) with θ < ½ would **exclude** ζ_K for d ≥ 3 although GRH(K) is expected — so a θ<½ law is not T1-uniform over number fields. ARGUED |
| L(s,χ) | same primes, weights χ(p) multiplicative | Σ_{n≤x}χ(n) = O(1) | would give GRH(χ) | consistent (W9/T1) |

**OPEN (Beurling question, flagged).** Does (E_θ) with some θ < ½, plus a positivity/atomicity condition, imply
"no zeros of ζ_𝒫 in σ > ½"? I do not know a construction with θ < ½ and an off-line zero, nor a theorem excluding one
(FROM MEMORY: Broucke–Debruyne–Vindas study the optimal pairs (θ, α) for N and ψ; their results concern zero-free
regions, not RH). If such a theorem held, it would be a proof of RH by a different route than row D; if a
counterexample exists, the Eratosthenes link (relaxed) cannot carry the step. Either way the induction adds nothing.

## §7 Test against the certified range (task 6)

T = ½log2 (X = 2). Δ ≤ T allows T' ≤ log 2 (X' = 4); the activated set is {2, 3}, z = 2, P(2) = 1: the sieve is empty
and Eratosthenes says only "2, 3 are prime". Step from ½log2 to ½log5 needs X' = 5 > X² = 4: **not one step**; two steps
½log2 → log2 → ½log5 (second with X = 4, z = √5, P = 2: n = 4 = 2² (k≥2), n = 5 coprime to 2 ⇒ prime). In each step
the required statement is the Schur condition of Theorem 2 on explicit data — exactly the content of the Paper 47
certificate at the target window, with no inequality supplied by the method. So the method **reproduces** λ > 0 up to
½log5 only by re-running the certificate; it gives no proof shortcut. PROVED (bookkeeping) / ARGUED (no shortcut).

## §8 Ledger

| item | label |
|---|---|
| Lemma 1 support bookkeeping (strips reach old domain iff log n < 2T+Δ) | PROVED |
| Prop 1 activation identity W_{T'} = W_T ⊕ … − 𝒩_{T,T'} | PROVED |
| Thm 2 Schur form; necessary condition (N) | PROVED |
| Cor 2′ step must be a doubly-exponential exact cancellation (W2) | PROVED (given thm:M(b), record) |
| Prop 3 Eratosthenes determination on [X, X²) | PROVED |
| Prop 4 Legendre decomposition of 𝒩 | PROVED |
| Prop 4′ Mertens factor 2e^{−γ}: Legendre "remainder" is main-term size | PROVED-CITED (Mertens) |
| Prop 4″ Fourier side = (ζE_z)', zeros absent, |E_z| up to exp(c X'^{1/4}/log X') | PROVED (identity) / ARGUED (contour) |
| §4.1 no sign property of exact Legendre operator | PROVED (indefinite) / ARGUED (nothing finer) |
| §4.2 step circular through ζ on the line → Thm 4 class (a) | PROVED (ζ appears) / ARGUED (class) |
| §4.3 truncated sieve → parity (b), dead by W2 first | PROVED-CITED + PROVED |
| Prop 5 Eratosthenes ⟺ integers = ℕ; selects ζ alone | PROVED |
| §6 M_m fails hypothesis (β_m) — R163_702 §3 consistent | PROVED |
| §6 DMV, ζ_K exponents | PROVED-CITED (FROM MEMORY, flagged) |
| (E_θ), θ<½ ⇒ RH for Beurling systems? | OPEN |
| Step_{T,Δ} for any (T,Δ) beyond certificates | **OPEN** (no proof in any range) |
| Row D | **OPEN** |

**Wall.** W2 (Theorem M) for every estimate; for the exact identity: Prop 5 (no class — single object ⇒ per-window
certificate + master quantifier). The lead "Eratosthenes link" of R169_000 v2 is hereby reduced to the additive datum
N(x) = ⌊x⌋; record it in the master grid as: *Eratosthenes induction — NO-GO (W2 + single-object), residual OPEN
question (E_θ, θ<½).*
