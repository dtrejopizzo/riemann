# CA_R3_001 — SPEC_A, clause (θ): where log ℕ enters the exact Schur step (phase 193, round R3)

Specification round, pen and paper, no numerics, no proof of the step. Row D (λ_A(T) ≥ 0 on P_T ∀T, P46 eq:target).
Inputs: SPEC_A (phase 191) §2–§3, Lemma S; CA_R2_002; EI_001 (2.1) (SPEC_A §2(d) correction: polar partner = opposite-collar Tate
moment p); P46 thm:shape, cor:shape, prob:region, lem:wh-schurabs, cor:margin1; index README PRINCIPIO RECTOR + front M correction.
**No negative value of 𝔞_T for ζ is produced or claimed.**

**Numbering erratum (SPEC_A §4 table).** SPEC_A uses O6 = Beurling, O7 = a_P. P46 (lines 8331–8345): O6 = a_P, O7 = quartets,
O8 = f_t, O9 = rational twist, O10 = Epstein, O11 = Beurling, O12 = field change, O13 = bounded range, O14 = truncation,
O15 = Poisson. This memo uses P46 numbering.

## 1. The exact step quantity in Chebyshev coordinates (PROVED, identity)
Notation of SPEC_A: window T_{j+1}, frozen window I_{T_j}, collars L_j, R_j of width ε_j = ½log(n_{j+1}/n_j); comb n ≤ n_j;
e = (α,β;G), x ∈ P_{T_j} ∩ 𝒟. Key arithmetic fact: e^{T_j + T_{j+1}} = √(n_j n_{j+1}) < n_{j+1}, so every comb lag reachable from
a collar point into I_{T_j} lies in [1, n_{j+1}).

**Proposition Θ (PROVED).** For G supported on L_j ∪ R_j and x ∈ P_{T_j}:
  ⟨G, 𝒯_j x⟩ = ⟨x, 𝒬_G⟩ + ⟨x, 𝒦₁G⟩,
  𝒬_G(s) := ∫_{[1, n_{j+1})} u^{−½}[G(s + log u) + G(s − log u)] d(ψ(u) − u),   𝒦₁G := ½K₁ ⋆ G (exponents 5/2, 9/2, …),
and hence ℓ_e(x) = α𝔞_{T_j}(e⁺_j,x) + β𝔞_{T_j}(e⁻_j,x) − ⟨x, 𝒬_G + 𝒦₁G⟩.
*Proof.* Comb part: Σ_{n≤n_j}Λ(n)n^{−½}G(s+log n) = ∫_{[1,n_{j+1})}u^{−½}G(s+log u)dψ(u) since ψ is constant on [n_j, n_{j+1}).
Density part: ∫u^{−½}G(s+log u)du = e^{−s/2}∫G(r)e^{r/2}dr (u = e^{r−s}; the u-range lies in [1, n_{j+1}) by the key fact),
a multiple of e^{−s/2}, which pairs to 0 with x since B(x) = 0; the G(s − log u) term gives a multiple of e^{s/2}, killed by A(x) = 0.
Polar part 2e^{−u/2} of K: likewise multiples of e^{∓s/2}, killed by A(x) = B(x) = 0. What remains is the K₁ part. ∎
**Consequences.** (a) The density/polar contribution to the coupling is *exactly zero* on P_{T_j}: the step wins only from
ψ − u (R)(7), proved here, not argued. (b) The contact block (SPEC_A §2(d)) is the restriction of d(ψ − u) to the last stretch
[n_j, √(n_j n_{j+1})): **Λ(n_j)δ_{n_j} − du**. Atom v_{n_j} at lag log n_j = 2T_j and its polar partner (density on
[n_j, e^{t+T_j}), = opposite-collar Tate moment p of EI_001) are the two halves of one jump of ψ − u; the ratio is Λ(n_j) against
the gap length, i.e. the successor n_{j+1} enters through the support of the stretch. (c) Schur term:
  ‖ℓ_e‖²_{𝔄_j^{−1}} = ⟨Φ_e, 𝔄_j^{−1}Φ_e⟩,  Φ_e := Π_{P_{T_j}}[α𝔄e⁺ + β𝔄e⁻ − 𝒬_G − 𝒦₁G]  (Riesz representative).
Its kernel on R_j × R_j contains Σ_{n,n′≤n_j}w_nw_{n′}·𝔄_j^{−1}(t − log n, t′ − log n′), w_n = Λ(n)n^{−½} minus density; the
(n_j, n′) entries couple the inner left collar [−T_j, −T_j+ε_j] (where t − log n_j lands) to t′ − log n′, displacement
(t′ − t) + log(n_j/n′), |t′ − t| < ε_j. R_j × L_j entries carry log(n n′). This is the + (window edge at log n_j) meeting
· (n_j/n′).

## 2. Arithmetic of the new lags (PROVED; role ARGUED)
**Lemma C (coprimality at prime contacts, PROVED by unique factorization).** If n_j = p is prime, then for all n′, m, m′ < p:
log(p/n′) ≠ log(m/m′) (p·m′ = m·n′ forces p | m n′, impossible). If n_j = p^k (k ≥ 2), the coincidences are exactly
p^k/p^a = p^{k−a}/1 and their multiples along the p-line.
So at prime contacts the new cross-lags are never exact resonances of the frozen comb; their interaction with 𝔄_j^{−1} is
carried only by near-coincidences p ≈ m n′ (residue R9 / problem (S)). Lemma C is a **monoid** fact: it survives O7, O11 (free
Beurling monoids), O15 a.s. — by itself it is excluded (G1 → (R)(10)); it is bookkeeping that sorts the Schur kernel.

## 3. The ℤ-mechanism (+/· through positions and weights, front M reading)
The Chebyshev divisor identity Σ_{d|n}Λ(d) = log n (n < n_{j+1}) gives, by finite Möbius inversion,
  (Ch)  ψ(y) = Σ_{k ≤ y} μ(k)·log⌊y/k⌋!,   log⌊y⌋! = y log y − y + ½log(2πy) − 𝔟(y) + O-free Euler–Maclaurin form with the exact
        periodic sawtooth B̃₁ (𝔟(y) = ∫^y B̃₁(v)dv/v, exact),
so d(ψ − u) on [1, n_{j+1}) is a finite Möbius combination of dilates y ↦ y/k (·) of the lattice sawtooth B̃₁ (+), plus an
explicit smooth main-term mismatch whose coefficients are the finite sums Σ_{k≤y}μ(k)/k, Σ_{k≤y}μ(k)log k/k (exact, finite).
This is the only place in the step where ℤ is used as a mechanism: positions are the consecutive integers (sawtooth period 1,
successor), weights are fixed by divisibility (Möbius dilation). It is not valid for every weight vector (not B″), not valid on
non-lattice positions (not Beurling), not FE-class generic (Epstein has no divisor identity).
Caveat H1 (ARGUED): on a finite range, (Ch) + positions log ℕ determine (Λ(n))_{n<n_{j+1}} uniquely, so as a *hypothesis*
it equals the data (W-identification). The distinction mechanism/data can only be enforced on the *proof class*: the step must be
proved by operations that act on (Ch)'s two factors (sawtooth, Möbius dilation) and not on the resulting numbers. The spec below
states it so.
Caveat H2: Mellin-transforming the Möbius dilations produces 1/ζ (zero side, (R)(4)). The step must stay on the physical
side (finite k < n_{j+1}, u < n_{j+1}).

## 4. The candidate step lemma (OPEN; REF-D content, valid objective)
**L*_j(θ).** Assume H_j (λ_A(T_j) ≥ μ_j > 0). For every e = (α,β;G) ∈ ℰ_j ∩ 𝒟:
  𝔞_{T_{j+1}}(e) − ⟨Φ_e, 𝔄_j^{−1}Φ_e⟩ ≥ ν_j‖e‖²,  ν_j > 0, ν_j ≥ μ_j·exp(−C(n_{j+1} − n_j)),
with Φ_e from Proposition Θ, 𝒬_G written through (Ch), and the proof restricted to the class 𝒞_θ:
 (i) identities only for the exterior field (no remainder; B′/[crit]); (ii) the archimedean kernel K exact (FE, Γ(s/2), conductor 1)
 in 𝔄_j and in the edge energy; (iii) ℤ used only through (Ch): lattice sawtooth B̃₁ and Möbius dilations k < n_{j+1}, plus the gap
 determinism of d(ψ − u) = Λ(n_j)δ − du on [n_j, n_{j+1}); (iv) Lemma C sorts the (n_j, n′) Schur entries into exact resonances
 (p-line only) and near-coincidences; (v) no zero information, no Mellin passage through 1/ζ.
By Lemma S(i) L*_j(θ) for all j is row D with explicit margins (B8: REF-D, a valid objective, not a closure).

## 5. Clause check
| clause | L*_j(θ) | why |
|---|---|---|
| O1 finite deletion, O2 Λ+cδ₂, O3 tail deletion, O4 cΛ, O5 one weight | escaped (PROVED for the hypothesis) | (Ch) fails: Σ_{d|n}a(d) ≠ log n at some n < n_{j+1} once the modification acts inside the window |
| O6 a_P | escaped (PROVED) | Σ_{d|n}a_P(d) = log n − Σ_{p<P, p^k‖n} k log p ≠ log n for n with a small prime factor |
| O7 quartets | **survives in the ℤ-part** (comb identical) | separation only via (ii) exact K/𝔄_j^{−1}; ℤ-mechanism does not escape O7 — cor:shape(a) says it cannot |
| O8 f_t | escaped (ARGUED) | non-Euler coefficients beyond λ₁: (Ch) fails there |
| O9 rational twist | survives the ℤ-part (comb unchanged) | as O7; (ii) |
| O10 Epstein | escaped (ARGUED) | no divisor identity; the sawtooth half alone is FE-class generic (CA_C_007), the Möbius half is not |
| O11 Beurling | escaped (ARGUED, P46 falsifier ARGUED) | non-lattice positions: no sawtooth; Lemma C alone survives |
| O12 field change | escaped / not uniform | ideal norms repeat; (Ch) over ℕ fails; spec is ζ-specific |
| O13 bounded range | escaped | ∀j |
| O14 truncation | escaped | whole form |
| O15 Poisson | escaped | positions random, no sawtooth |
| (B″) | not comb-generic | Prop Θ and Lemma S are B″ bookkeeping; the property is (Ch) |
| (R)(1),(2) | PASS | exact data; Euler (Ch) + FE (exact K) jointly = cor:shape(b) |
| (R)(3) | PASS | Schur term rational in Λ through 𝔄_j^{−1} |
| (R)(4) | PASS-COND | H2: only if Möbius stays physical-side |
| (R)(5),(6),[crit] | PASS-COND | identities only; margin ≤ X^{−7.72} (CA_R2_002) must be resolved by the final inequality itself |
| (R)(7) | PASS, now PROVED in part | density/polar cancel exactly (Prop Θ(a)); integer resolution = sawtooth |
| (R)(8),(9) | PASS | full resolvent, no D_σ |
| (R)(10) | PASS (ARGUED) | lattice positions + divisor identity exceed A1–A6 |
| (R)(11) | PASS-COND | sign step must act on (Ch); H1 |
| (θ) | **MET** | ℤ enters at d(ψ − u) on [1,n_{j+1}) via (Ch); last stretch = contact block |

## 6. Verdict
**ADMISSIBLE as a specification (OPEN)**: (γ), A15 PASS (identity-only), (θ) MET, B8 REF-D (valid objective), O7/O9 escaped
only through the exact archimedean kernel, as cor:shape(a) requires of any argument. Not a proof, no sign, no margin certified.
Weak points: H1 (mechanism enforced on the proof class, not the statement); H2 (1/ζ risk); O8/O10/O11 escapes ARGUED.
First test case: j with n_j = 7 (prime contact, T ∈ (½log7, ½log8]), where Lemma C makes all new cross-lags non-resonant.
