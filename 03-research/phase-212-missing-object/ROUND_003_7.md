# Round 3, option 7 — The formulation (S): divisor incidence on 𝔸_M (selection memo)

Goal (★): λ_A(T) ≥ 0 for every T, with the definitions of `../phase-211-sign-sandbox/STATEMENT_001.md`.
Reduction used (PROVED, P47 prop:AM): with a fixed profile F_0 ∈ P_{T_0}, 2T_0 < log 2, (★) is equivalent to
𝔸_M = [𝖡(log m − log k)]_{m,k≤M} = Arch_M − Div_M − Near_M ⪰ 0 for every M. Notation of P47 §subsec:oneprofile:
β(d) := (1/2π)∫ m F̂_0² cos(τd) dτ (archimedean part of 𝖡), v_n = 2Λ(n)n^{−1/2}, c_0 = c_{F_0}, sop c_0 ⊂ [−2T_0, 2T_0].
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

### What was searched and where

Grep in `03-research/` (all phases), `04-papers/47` and `48`, grid, crossword, index (README and 06) and annexes of
phase 212 for: Arch_M, Div_M, Near_M, 𝔸_M, mathbb A_M, prop:AM, «Arch_M − Div_M», GCD/mcd, Smith, meet matrix,
incidencia, Möbius, LDL, Cholesky, Schur, «rango uno», coprimo, «site independence». Opened in primary:
P47 prop:AM with proof, thm:oneprofile, prop:nearfree, rem:boxes, rem:bar-arith, problem (S) of §sec:open;
phase 188 `N_BUILD_022` (complete), `L2_BUILD_031` (complete), `L2_BUILD_028` §§1–4; phase 193
`CA_K_001` §1 (Lemma 1.1, Thm. 1.2, Prop. 1.3), `CA_K_002` §3 (Thm. 3.2) and `CA_K_001_002_REVIEW`; phase 200
`A_MU_FACTORIZATION_001` §§0–1(b); 211 `ROUND_003_B` (headings and §§2–5), 211 LEDGER C7, C9, C43; index 06 §R9;
`RULES_AVOID.md` I1–I3 and §E; this phase `ROUND_001_B` §4 (Prop. 6, condition (4.1)), `REVIEW_001_ABD` E-B4,
`ROUND_003_2`. I did not open in primary phase 205 (Toeplitz−Hankel), 206 nor the hits of phases 120 and 162
for «Smith»/«GCD» (by titles: global polarization and torsion atoms, not 𝔸_M); this remains a limit of the cross-check. A
search without hits does not prove novelty.

### Answer of the corpus to questions (i)–(iv) of the task

(i) **Arch_M − Div_M is not ⪰ 0** for large M: already PROVED in the corpus. `CA_K_001` Prop. 1.3(a): β is not positive
definite (its Bochner density m F̂_0²/2π is negative near 0 because m(0) = C_0 = −5.37… < 0), hence Arch_M is
indefinite for M ≥ M_1. `CA_K_002` Thm. 3.2 (site independence): (★) is equivalent to 𝔸_M restricted to primes ⪰ 0
for every M; there Div ≡ 0, and Cor. 3.3(ii) gives Arch − Div indefinite on prime sites. Moreover Div_M is not a
matrix of type f(gcd): it is the Dirichlet convolution by v (unitriangular on one side), with the exact identity
Δ = Z⁻¹LZ − L (`N_BUILD_022` §1; = R162_903 B2.1). The Smith factorization [log gcd] = E diag(Λ) Eᵀ exists and is
⪰ 0 (`ROUND_001_B` Prop. 6), but it is homogeneous in the weight and does not contain the archimedean factor.

(ii) **Near as −(square) + absorbable / 𝔸_M = WᵀDW with W unitriangular in divisibility.** Antecedents:
`N_BUILD_022` §3 (NO-GO PROVED: no exact matrix identity derived from 1∗Λ = log reaches Near; Near is
the discretization defect); `L2_BUILD_030` §2 in the index (Near as a separate signed operator: NO-GO);
`ROUND_001_B` (4.1): a factor with incidence pattern requires rank one on coprime pairs, with failure only
NUMERICAL; `ROUND_003_2` Lemma 2 (LDL with D ≥ 0 iff 𝔸 ⪰ 0: circular); phase 200 §1(b) (grouped Cholesky, mixed
inertia, C8). What is new in this memo is Lemma 1: the failure of (4.1) passes from NUMERICAL to PROVED, and with greater scope
(any diagonal D, any sign, without going through the row of 1).

(iii) **Where the functional equation enters (S).** Only in two places: the symbol m(τ) = Re ψ(¼ + iτ/2) − log π
of Arch_M (factor Γ(s/2)π^{−s/2}, conductor 1) and the Tate conditions F̂_0(±i/2) = 0, which annihilate exactly the
main term of Ξ_{F_0} (P47 thm:band, lem:transl(iii)). The entries of Div_M and Near_M do not contain it; in
(S) the functional equation enters additively, in the archimedean term, and no antecedent read writes an
exact identity linking entries of Near_M with entries of Arch_M (the Poisson identities of P47
thm:PCfinite, already examined in K1, are generic in the comb). ARGUED.

(iv) See §(5) below.

### (1) Closest antecedent

`ROUND_001_B` §4 (Prop. 6 and condition (4.1)), with its review `REVIEW_001_ABD` E-B4; `N_BUILD_022` §§1–3; `CA_K_001`
Prop. 1.3 and `CA_K_002` Thm. 3.2. The candidate of the task («𝔸_M = WᵀDW, W unitriangular in the order of
divisibility, pivots explicit functions of Λ of the type Σ_{d|n}Λ(d) = log n») is that of `ROUND_001_B` §4 on the
formulation (S): **repetition**, except for what Lemma 1 decides.

### (2) Genuinely new object

There are no new ℋ, V, ρ. What is new are three short pieces, proved below:

- **Lemma 1 (format NO-GO, PROVED).** There exists M_0 such that for every M ≥ M_0 the matrix 𝔸_M admits no
  exact factorization 𝔸_M = WᵀDW with D real diagonal (of any sign) and W_{dk} = 0 unless d | k. The exclusion
  holds for every comb supported in [log 2, ∞) (it does not use Λ): it is of format, not of sign.
- **Lemma 2 (PROVED, algebra).** For any W of that pattern, (WᵀDW) restricted to the primes ≤ M is
  D_1 wwᵀ + diag(D_p) (rank one plus diagonal). Since the restriction to primes is already equivalent to (★)
  (`CA_K_002` Thm. 3.2), an identity 𝔸_M = WᵀDW + ρ leaves the whole sign of the equivalent reduction in ρ.
- **Corollary 3 (PROVED, from `ROUND_003_2` Lemma 3 and `CA_K_001` Prop. 1.3(a)).** The matched affine class
  on (S) is also NO-GO: case (iii) that `ROUND_003_2` left open is closed for M ≥ M_1.

What remains to be written to have a candidate: a W **not** supported on divisibility (that sees nearly
proportional coprime pairs m ≈ kn), with its own formula not derived from 𝔸_M, and a ρ with manifest sign. I do not know how to write it.

### (3) Why the change would avoid the difficulty of the antecedent

It does not avoid it: it confirms and proves the difficulty. The structural reason, now PROVED (Lemma 1): in an incidence pattern
the columns of coprime integers share only the coordinate of 1, whereas 𝖡 is continuous in the real delay,
so that primes with nearly equal quotients have nearly parallel columns. No pivot, however explicit
(log n, Λ(n), f∗μ), repairs that.

### (4) Identity that would connect with global positivity

None in the divisibility class (Lemma 1). With remainder, only 𝔸_M[𝒫] = D_1wwᵀ + diag(D_p) + ρ[𝒫] (Lemma 2), where
proving ρ[𝒫] ⪰ 0 is as strong as (★) by site independence: the incidence contributes nothing in the equivalent
reduction except a rank one and a diagonal.

### (5) Line that breaks for cΛ and a_P

- Lemma 1: it does not break for any comb: it is a format impossibility. That is why it is not a mechanism.
- Corollary 3: the line «ρ = Arch_M − V_0ᵀV_0 − V_1ᵀV_1 ⪰ 0» already fails for Λ; for cΛ the remainder is
  ρ^{(c)} = ρ^{(0)} − c²V_1ᵀV_1, even and non-increasing in |c|, without breaking at c < 1.
- Locality remark (PROVED, from P47 prop:AM(ii)): the entries of 𝔸_M depend on the weight only through
  a(n), n < M e^{2T_0}. Hence, for a falsifier that keeps a(n) = Λ(n) for n < X (for example the
  deformation f_t with X = λ₁), every identity on the family {𝔸_M} can only break at M ≥ X e^{−2T_0}: the
  line that breaks has to be used for every large M (O5). For a_P
  (powers of primes p < P erased) Div_M already changes at M = 2: the breaking in (S) would be visible at small M, but
  no identity of this memo uses it.

### Cross-check verdict

Repetition of `ROUND_001_B` §4 in the formulation (S), with (i) already resolved by `CA_K_001`/`CA_K_002` and (ii) by
`N_BUILD_022` §3 and `ROUND_003_2` Lemma 2. Lemma 1 is added (it closes with class, in PROVED form, the factorization by
divisor incidence) and Corollary 3. No candidate ready for construction.

## 1. Proofs

### Lemma 1 (there is no factorization in the divisibility order; PROVED)

*Statement.* Let F_0 be the profile of P47 §subsec:oneprofile with 2T_0 < log 2 and let a be any real weight with comb
supported in {log n : n ≥ 2} (in particular Λ, cΛ, a_P, erasures, amplifications). Let 𝖡_a be the corresponding one-profile
function and 𝔸_M = [𝖡_a(log m − log k)]. There exists M_0 such that, for M ≥ M_0, there are no real D = diag(D_1, …, D_M)
and real M×M W with W_{dk} = 0 unless d | k, such that 𝔸_M = WᵀDW.

*Proof.* Step 1 (rank one on primes). If 𝔸_M = WᵀDW, then (𝔸_M)_{mk} = Σ_{d | m, d | k} D_d W_{dm}W_{dk}.
For distinct primes p, q ≤ M the only common divisor is d = 1, hence (𝔸_M)_{pq} = D_1 W_{1p}W_{1q}. For four
distinct primes p, p′, q, q′ ≤ M:

    𝖡_a(log p − log q) 𝖡_a(log p′ − log q′) = 𝖡_a(log p − log q′) 𝖡_a(log p′ − log q).        (1.1)

Step 2 (passage to the continuum). The entries of 𝔸_M do not depend on M; if the factorization existed for infinitely many M,
(1.1) would hold for every quadruple of distinct primes. Given pairwise distinct reals x, x′, y, y′ and C > 0, by the
prime number theorem (CITED: p_{n+1}/p_n → 1) there are distinct primes with |log p − C − x| < ε, etc., for large
C; the differences of logarithms tend to x − y, etc. Since 𝖡_a is continuous (P47 thm:oneprofile, statement),
(1.1) holds for all pairwise distinct real quadruples, and by continuity for all. Taking y′ = x, x′ = y:
𝖡_a(x − y)𝖡_a(y − x) = 𝖡_a(0)², and by parity 𝖡_a(d)² = 𝖡_a(0)² for every d. A continuous function of constant
modulus on ℝ is constant (if the modulus is 0 it is identically 0; if not, it does not vanish and does not change sign). Hence
𝖡_a is constant.

Step 3 (𝖡_a is not constant). For |d| < δ := log 2 − 2T_0 > 0 and n ≥ 2, |log n ± d| > 2T_0, so the comb part
of 𝖡_a(d) is zero and 𝖡_a(d) = β(d) = ∫ w(τ) cos(τd) dτ, w := m F̂_0²/2π. Write w = w⁺ − w⁻. The set {m < 0}
is bounded because m(τ) ≥ log(|τ|/2π) − 4 (P47 lem:mbounds(ii)); hence w⁻ has compact support and β_− := ∫w⁻cos(τ·)
is C^∞. If β were constant on (−δ, δ), β_+ = β + β_− would be C^∞ in a neighbourhood of 0, and β_+ is the transform of the
finite positive measure w⁺dτ. By the classical moment lemma (CITED: if the Fourier transform of a finite positive
measure has a derivative of order 2k at 0, the moment of order 2k is finite), ∫ w⁺ τ⁴ dτ < ∞. But
F̂_0(τ) = (τ² + ¼)|ĝ(τ)|⁴ with |ĝ(τ)| = |e^{(b+iτ)a} − 1|/|b + iτ| ≥ |e^{ba} − 1|/(b² + τ²)^{1/2}, and e^{ba} ≠ 1 since
b ≠ 0; thus F̂_0(τ) ≥ c τ^{−2} and F̂_0² ≥ c² τ^{−4} for large |τ|, while m(τ) ≥ 1 for large |τ|. Hence
w⁺τ⁴ ≥ c′ > 0 for large |τ| and ∫w⁺τ⁴ = ∞. Contradiction: β is not constant near 0, hence 𝖡_a is not constant.

Step 4 (uniformity). Steps 2–3 show that (1.1) cannot hold for all quadruples of primes; fix a
quadruple where it fails and M_0 its largest element. For M ≥ M_0 a factorization of 𝔸_M would impose (1.1) on that
quadruple (step 1), hence it does not exist. ∎

*Scope.* It covers the Smith factorization E diag(f∗μ) Eᵀ, every LDLᵀ in a linear order extending
divisibility whose factor inherits the incidence pattern, and every D with pivots of the type Σ_{d|n}Λ(d) = log n. It is not
effective (it does not give M_0). It does not cover: W with support outside divisibility; identities with remainder ρ ≠ 0 (Lemma 2); other
reductions ((L2), ladder, profile). It improves `ROUND_001_B` (4.1) from NUMERICAL to PROVED, without the row of 1 and without
estimating values of 𝖡.

### Lemma 2 (the incidence is invisible in the reduction to primes; PROVED)

For W with the pattern of Lemma 1 and 𝒫 = primes ≤ M: (WᵀDW)[𝒫] = D_1 wwᵀ + diag(D_p W_{pp}²), w = (W_{1p})_{p∈𝒫}.
*Proof.* For distinct primes p ≠ q the only common divisor is 1; for p = q, the divisors are 1 and p. ∎
With `CA_K_002` Thm. 3.2 ((★) ⟺ 𝔸_M[𝒫] ⪰ 0 for every M; PROVED there) and Div_M[𝒫] = 0: in an identity
𝔸_M = WᵀDW + ρ with D ≥ 0, the incidence part contributes in the equivalent reduction only a rank one plus a
diagonal, and the remainder ρ[𝒫] = Arch_M[𝒫] − Near_M[𝒫] − D_1wwᵀ − diag(·) carries the whole sign.

### Corollary 3 (matched affine class on (S); PROVED)

Class: V(a) = V_0 + V_1(a), V_1 linear in the weight, coefficients independent of the weight, with
2 sym(V_0ᵀV_1(Λ)) = −(Div_M + Near_M). Then ρ := 𝔸_M − V(Λ)ᵀV(Λ) = Arch_M − V_0ᵀV_0 − V_1(Λ)ᵀV_1(Λ) ⪯ Arch_M,
and Arch_M is indefinite for M ≥ M_1 (`CA_K_001` Prop. 1.3(a)); hence ρ is not ⪰ 0. It is the computation of `ROUND_003_2`
Lemma 3 with Arch_M in place of Arch on P_T; it closes its case (iii). ∎

## Result

**Repetition in the main part (factorization by divisor incidence on 𝔸_M = `ROUND_001_B` §4 in (S));
(i) already resolved in the corpus (Arch_M and Arch_M − Div_M indefinite: `CA_K_001`/`CA_K_002`). Format NO-GO piece
PROVED (Lemma 1), PROVED delimitation (Lemma 2) and PROVED closure of case (iii) of `ROUND_003_2` (Corollary 3).** No
candidate ready for construction.

## What was proved

- Lemma 1: for M ≥ M_0, 𝔸_M has no exact factorization WᵀDW with W supported on divisibility and D diagonal of
  any sign; it holds for every comb (format). Proof: rank one on primes + density of log 𝒫 + 𝖡 = β near 0
  and β is not C⁴ at 0 (infinite fourth moment).
- Lemma 2: the incidence contributes only rank one plus diagonal on the prime sites, which are already an equivalent
  reduction.
- Corollary 3: the matched affine class also fails on (S).
- Locality: 𝔸_M depends on a(n) only for n < M e^{2T_0}.

## What failed and why

- Divisor incidence does not see the nearly proportional coprime pairs, which is where Near lives; 𝖡 is continuous in
  the real delay and that forces nearly parallel columns that the incidence pattern does not admit.
- The explicit pivots in Λ (log n, Λ(n), f∗μ) cannot save the format: the obstacle is archimedean (β is not
  smooth of order 4 at 0), not arithmetic.
- The functional equation enters (S) only through Arch_M and the Tate conditions, additively; there is in the corpus
  read no identity coupling it to the entries of Near.

## What remains NOT excluded

- W whose support includes nearly proportional coprime pairs (m ≈ kn), with its own formula, for example indexed by
  the Farey fractions or by the rational approximations of log m − log k; no written object.
- Identities with remainder ρ ≠ 0 where ρ[𝒫] has manifest sign for a reason different from the incidence.
- The affine class without matching (case (i) of `ROUND_003_2`) and V non-affine in Λ (case (ii)).
- The other PROVED reductions ((L2), ladder, continuous profile).

## Concrete next step

1. Record in the index (06 §R9), in the grid and in the ledger: «factorization WᵀDW of 𝔸_M with W in the
   divisibility order, any D: format NO-GO PROVED (ROUND_003_7 Lemma 1), generic in the comb»; and Corollary 3
   as closure of case (iii) of ROUND_003_2. Correct in the ledger the label of (4.1) of K2: from NUMERICAL to PROVED
   (not effective).
2. A reopening of (S) by factorization only with a W whose pattern contains the near-coincidences, written before
   deriving, with its ρ and with the breaking line for cΛ and a_P, passing the four-point gate.
