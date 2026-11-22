# R162_1401 — Douglas bound via Λ*1 = log after the string decomposition — **NO-GO (PROVED)**, exact obstruction located

Note. Pure mathematics, no numerics. Inputs: README (F1–F4, rounds 1–13), R162_590, R162_1301
(Thms 1, 3, 4), R162_1201 ((2.1), Thm 2.1 with the R162_1390 sign fix (t−T)), R162_502 (B1, B2), R162_903 (Thm 3.2).

**Labels.**
- Lemma 1 (ray action: every element of 𝒜_T acts on e_m as a step-function multiplier) PROVED. Elementary, new form.
- Thm 2 (secular ledger: A_T e_m = (X − T + μ_m^reg − σ_m(X))e_m + R_m on I) PROVED. Assembles R162_1201 (2.1) + Lemma 1.
- Thm 3 (Tate-only cancellation: Λ*1 = log removes the secular X only at a_0 = ½; for m ≥ 1 the X-coefficient is 1) PROVED. **New.**
- Thm 4 (ray reduction of the conjugation: on the e_m-ray ZXZ⁻¹ = X + M_T(Λ) is the scalar identity (−ζ'/ζ)·ζ = −ζ' at
  s = 2m+1, truncated) PROVED. **New.**
- Thm 5 (inequality ledger: 𝔥 controls exactly one functional ℓ_m(G) = (T−μ_m^reg)x_m − x'_m + … ; Douglas at e_m ⟺
  Douglas at the Jordan partner) PROVED. Restatement (E1).
- Thm 6 (NO-GO: the step using Λ*1 = log is universal (Thm 3.2 of R162_903) and passes verbatim to Λ1_{n≥5} and DH, where
  the Douglas bound is false) PROVED.
Gate 1 OPEN. No label moves.

## 0. Corpus check

grep "Douglas|secular|ZXZ|Mertens|Chebyshev identity|log⌊|Tate ray|ray" in phase 162, R160_S1–S5, Paper 46: Douglas
form only in R162_1301 Thm 3; secular term only R162_1201 (2.1); conjugation R162_502 B2 / R162_903 Thm 3.2; Mertens
appears only as an estimate in collar asymptotics (subsec:collars). Not found: the action of 𝒜_T on e_m (Lemma 1), the
Tate-only cancellation (Thm 3), the ray reduction (Thm 4).

## 1. Ray action (Lemma 1)

Notation: I = (−T,T), ℓ_n = log n, e_m = e^{a_m t}1_I, a_m = 2m+½, M_T(α)F(t) = 1_I(t)Σα(n)n^{−½}1_I(t+ℓ_n)F(t+ℓ_n).

**Lemma 1.** For every finitely supported α,
  M_T(α)e_m = σ^+_{α,m}(X) e_m,  σ^+_{α,m}(t) = Σ_{ℓ_n < T−t} α(n) n^{2m},
  M_T(α)*e_m = σ^−_{α,m}(X) e_m, σ^−_{α,m}(t) = Σ_{ℓ_n < t+T} α(n) n^{−2m−1}.
*Proof.* e^{a_m(t+ℓ_n)} = n^{a_m}e^{a_m t}, n^{a_m−½} = n^{2m}; adjoint shifts by −ℓ_n, n^{−a_m−½} = n^{−2m−1}. ∎

So on the ray {φ(X)e_m} the whole algebra 𝒜_T and X act by multiplication: they commute there. The comb enters the
e_m-direction only through the step multipliers σ^±_{Λ,m} (collar moments ρ^± of R162_1201 are their pairings).

## 2. Secular ledger (Thm 2)

**Thm 2.** On I, with σ_m := σ^+_{Λ,m} + σ^−_{Λ,m} and R_m the Hankel remainder of R162_1201 (2.1)
(R_m = −Σ_{k≠m}e^{(a_m−a_k)T}e_k/(a_m−a_k) + Σ_{k≥0}e^{−(a_m+a_k)T}e^{−a_k t}1_I/(a_m+a_k)),
  A_T e_m = (X − T + μ_m^reg − σ_m(X)) e_m + R_m.
*Proof.* (2.1) at a → a_m: μ(a)e^{at} − e^{(a−a_m)T}e^{a_m t}/(a−a_m) → (μ_m^reg + t − T)e^{a_m t} (sign as fixed in
R162_1390). Comb C_I = M_T(Λ) + M_T(Λ)*; Lemma 1. ∎

The secular piece (X − T)e_m is where the Jordan resonance lives; the conjugation ZXZ⁻¹ = X + M_T(Λ) is the only place
X meets the arithmetic. The task's hope is that σ_m(X) contains a copy of X that cancels or dominates the secular term.

## 3. Tate-only cancellation (Thm 3)

**Thm 3.** (i) m = 0 (Tate ray a_0 = ½): σ^−_{Λ,0}(t) = Σ_{n<e^{t+T}}Λ(n)/n = (t+T) − γ_* + E(e^{t+T}), E = O(1)
(E → 0 iff PNT form), so the X-linear parts of the Euler step and of the secular term cancel exactly to O(1):
  A_T e_0 = (μ_0^reg − 2T + γ_* − E − σ^+_{Λ,0}(X)) e_0 + R_0.
The input is precisely Λ*1 = log in the summed form Σ_{n≤y}Λ(n)⌊y/n⌋ = log⌊y⌋! plus ψ(y) = O(y).
(ii) m ≥ 1: σ^−_{Λ,m}(t) = −ζ'/ζ(2m+1) − Σ_{ℓ_n ≥ t+T}Λ(n)n^{−2m−1}, bounded and increasing, with no linear part;
σ^+_{Λ,m}(t) = ψ_{2m}(e^{T−t}) ≍ e^{(2m+1)(T−t)}/(2m+1), convex, decreasing, no linear part. Hence the coefficient of
the secular X in A_T e_m is exactly 1 and is untouched by the comb.
*Proof.* (i) Partial summation of Chebyshev's identity; the constant γ_* is Mertens'. (ii) Absolute convergence at
s = 2m+1 > 1 and the prime number theorem at weight n^{2m}; no log term can arise since Σ Λ(n)n^{−s} is regular at
s = 2m+1 and Σ_{n≤y}Λ(n)n^{2m} has leading term y^{2m+1}/(2m+1). ∎

**Reading.** "Λ*1 = log" is, on the rays, the statement that the Euler symbol has a simple pole with residue 1 at
s = 1, i.e. at the Tate point a_0 = ½ (weight n^{−1}). That pole is what makes the arithmetic linear in X, and it sits
on the ray already killed by primitivity (x_0^± = 0). On the Gamma lattice m ≥ 1 the arithmetic evaluates Dirichlet
series at regular points; no log survives to meet the secular term.

## 4. Ray reduction of the conjugation (Thm 4)

**Thm 4.** With Z = M_T(1), B2.1 applied to e_m reads (Lemma 1)
  [X, Z]e_m = −M_T(log)e_m = −σ^+_{log,m}(X)e_m and M_T(Λ)Z e_m = σ^+_{Λ*1,m}e_m = σ^+_{log,m}e_m,
i.e. the truncated scalar identity Σ_{n≤y}(Λ*1)(n)n^{2m} = Σ_{n≤y} n^{2m}log n; on the adjoint ray the untruncated limit is
(−ζ'/ζ)(s)·ζ(s) = −ζ'(s) at s = 2m+1. In particular
  x'_m(G) = ⟨XG,e_m⟩ = ⟨(X + M_T(Λ))ZG, Z^{−*}e_m⟩,  Z^{−*}e_m = σ^−_{μ,m}(X)e_m = (1/ζ(2m+1) + collar) e_m,
so the conjugation transports the Jordan moment x'_m(G) to the Jordan moment x'_m(ZG) (plus Λ-step pairings), with
scalar factors ζ(2m+1)^{±1} and no coercive remainder.
*Proof.* Lemma 1 for α = 1, μ, Λ, log and B1(a),(b). ∎

So the hope "⟨G,e_m⟩ through ⟨ZG, X-something⟩ with a coercive remainder" is realised only as a transfer identity
between Jordan moments of G and ZG; the remainder is a pairing with a step multiplier, of either sign, with no 𝔥 in it.

## 5. Inequality ledger (Thm 5)

Π e_m lies in the form domain. Cauchy–Schwarz for H ≥ 0 (this is where λ = 0 as bottom enters, F1):

**Thm 5.** For all G in the form domain of 𝔥 (primitive),
  |ℓ_m(G)| ≤ 𝔥(G)^{1/2} 𝔥(Πe_m)^{1/2} + (Tate correction, linear in A(G),B(G) = 0),
  ℓ_m(G) := (μ_m^reg − T)x_m + x'_m − ⟨G, σ_m(X)e_m⟩ + ⟨G,R_m⟩.
Moreover Douglas at e_m ⟺ Douglas at the Jordan partner j_m := Π(X − σ_m(X) + R_m/e_m-part)e_m: since
Π A_T e_m ∈ ran H up to the Tate span, e_m ∈ ran H^{1/2} ⟺ j_m ∈ ran H^{1/2}.
*Proof.* ⟨G, HΠe_m⟩ = ℓ_m(G) by Thm 2; Cauchy–Schwarz in the form 𝔥. Second claim: ran H ⊂ ran H^{1/2}. ∎

Thus 𝔥 controls exactly one linear functional on the ray, which mixes x_m with its Jordan partner x'_m, the collar
steps and the Hankel couplings — this is (S_m) of R162_1201 with the equality relaxed to ≤ √𝔥. To obtain
|x_m|² ≤ C_m𝔥 one needs an independent 𝔥-bound on x'_m − ⟨G,σ_m e_m⟩ (the Jordan partner), which is again a
Douglas bound (Thm 5, second part). By Thm 3 the arithmetic cannot supply an X-linear term to cancel x'_m for m ≥ 1,
and by Thm 4 the conjugation only moves x'_m to x'_m(ZG). Circular.

## 6. NO-GO and the falsifier test (Thm 6)

**Thm 6.** Let Λ' be any real weight on 2 ≤ n ≤ e^{2T}. Put a' := exp_*(Λ'/log) (unipotent, R162_903 Thm 3.2) and
Z' = M_T(a'). Then Z'XZ'^{−1} = X + M_T(Λ'), Lemma 1 and Thms 2, 4, 5 hold verbatim with Λ → Λ', 1 → a'. For
(a) deletion Λ' = Λ1_{n≥5}: a' = coefficients of ζ(s)exp(−2^{−s} − 3^{−s} − ½·4^{−s}) (bounded, signed); the Tate
cancellation Thm 3(i) also holds (Σ_{5≤n<y}Λ(n)/n = log y + O(1)); for m ≥ 1 Thm 3(ii) holds with
−ζ'/ζ(2m+1) − Σ_{n≤4}Λ(n)n^{−2m−1} > 0;
(b) DH: a' = DH coefficients (lattice 2m+3/2, Λ_DH := log-derivative coefficients); Thms 1–5 hold with the shifted lattice;
the only difference is that a'^{−1} grows (input (iv) of R162_502 B3), which is not used anywhere above.
Both models have first contacts with x_m ≠ 0 (R162_102, R162_702, thm:finmod), so their Douglas bound fails
(R162_1301 Thm 3, q_m(0−) = ∞). Hence every argument built from {string decomposition, conjugation, Λ*1 = log in
operator or summed (Chebyshev/Mertens) form, H ≥ 0 with λ = 0 bottom} proves a falsehood for (a) and (b).
*Proof.* Thm 3.2 of R162_903 is formal in Λ'; Lemma 1 is formal in α; the Chebyshev–Mertens step used only
Λ' ≥ 0, ψ' = O(y) and the pole at s = 1, all shared by deletion. ∎

**Where exactly it fails for the falsifiers (as demanded).** The step "use Λ*1 = log" is Thm 3/Thm 4. For deletion it
succeeds identically (same Tate cancellation, same transfer identity, different positive scalar at s = 2m+1). For DH it
succeeds identically with its own a'. So the step does not fail in the falsifiers; it is inert. The bound fails for
them at the step *after* it — the attempt to bound the Jordan partner x'_m by 𝔥 — which is the same step for ζ. This
is the exact obstruction:

  **Obstruction.** Λ*1 = log couples to X only through the pole at s = 1 (Tate ray, already primitive-killed). On the
  Gamma rays m ≥ 1 all arithmetic operators are commuting step multipliers evaluating regular Dirichlet values at
  s = 2m+1; the secular X of the Jordan resonance has no arithmetic partner, and the Douglas bound at e_m is equivalent to
  the Douglas bound for its own Jordan partner.

## 7. Falsifiers

- F1: used (Cauchy–Schwarz for H ≥ 0 in Thm 5), but only produces the one functional ℓ_m, already in (S_m).
- F2: no orientation added; σ_m, ζ(2m+1)^{±1} are comb-orientation data of fixed sign for ζ and deletion alike.
- F3: failed (Thm 6: deletion and DH pass every step).
- F4: finite T exact (finite sums, truncated steps); Mertens used only as O(1).

## 8. Verdict and residual

**NO-GO (PROVED).** After the string decomposition, applying Λ*1 = log through ZXZ⁻¹ = X + M_T(Λ) on the e_m-rays is a
scalar identity at s = 2m+1 (Thm 4); the only place the log cancels the secular X is the Tate ray (Thm 3), which carries
no Gate-1 information. The Douglas bound reduces to itself for the Jordan partner (Thm 5). Deletion and DH satisfy every
step (Thm 6).

**Residual.** A mechanism must couple the secular X on a Gamma ray m ≥ 1 to arithmetic with a *pole* there — i.e. the
arithmetic must see s = 2m+1 as singular. Nothing in the Euler product does (Dirichlet series are regular for Re s > 1);
the only singular data at the Gamma lattice are archimedean (poles of ψ, R162_1201 Lemma 1.1). So a closing argument
must couple the Tate pole at s = 1 to the Gamma poles at a_m through the functional equation — the pairing that R162_1003
Thm R showed resums to Σ_ρ (E1). Suggested entry for R162_590 §1c: "Douglas via Λ*1=log after strings — R162_1401 —
log meets X only on the Tate ray; Gamma rays see regular Dirichlet values; Douglas ⟺ Douglas for Jordan partner |
E1, F3".

Files edited: this file only.
