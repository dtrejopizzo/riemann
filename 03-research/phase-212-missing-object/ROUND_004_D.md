# Round 4, zone D — Factorization of 𝔸_M with support on the near-coincidences m ≈ kn (selection memo)

Target (★): λ_A(T) ≥ 0 for all T, definitions from `../phase-211-sign-sandbox/STATEMENT_001.md`. Reduction used
(PROVED, P46 prop:AM, thm:oneprofile): fixed profile F_0 ∈ P_{T_0}, 2T_0 < log 2; (★) is equivalent to
𝔸_M = [𝖡(log m − log k)]_{m,k≤M} ⪰ 0 for all M, with 𝔸_M = Arch_M − Div_M − Near_M. Notation: β(d) archimedean part
of 𝖡, c_0 = c_{F_0} (supp ⊂ [−2T_0, 2T_0], c_0(0) = 1), v_n = 2Λ(n)n^{−1/2}, θ_0 := 2T_0.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

### What was searched, what was opened, what was not

Grep (case-insensitive) in `03-research/` (all phases), P46, P48 and `05-meta-and-planning/` (index,
crossword) for: near-divisib, casi-divisib, almost divisor, interval order, orden de intervalo, semiorder, Farey,
continued fraction, fracción continua, Green matri(x), matriz de Green, semisepar, totally positive, totalmente
positiv, Pólya frequency, sign-regular, complemento de Schur, closed under elimination, transitive. Results:
"near-divisib", "casi-divisib", "almost divisor", "semiorder", "closed under elimination", "orden de intervalo": 0
matches; "interval order": 1 (phase 73, E73_115, not pertinent by title, not opened); "Farey": 42 files
(phases 167, 191, 200, 194); "totally positive"/"Pólya frequency": 24/14 (phases 102–104, 114–116, 154, 162, 184, 186,
200, 201) plus the AUDIT_A index (A14a-1: PF₅ of the de Bruijn–Newman kernel, NO-GO CITED; A14a-2: PF₄ OPEN), L23,
L48, L49; "Green": phases 116, 170, 194, 205, 206.

Opened as primary sources: P46 prop:AM with proof, thm:oneprofile with proof, prop:nearfree with proof,
rem:boxes, rem:bar-arith; `ROUND_003_7` (in full), `REVIEW_003`, `RULES_AVOID` §§B, E, F, J; `OBJECT_SPEC`;
`BRIEF_CONSTRUCTOR`; STATEMENT_001; phase 194 `INV_C_001` §§0–1 (fibration by ratios r = a/b, Lemmas 1–3);
phase 205 `SKELETON_001` (lines of §5 "Pole Green identity" and its search table: "semiseparable: 0");
211 LEDGER rows C9 and C43; AUDIT_A index §1 (PF₅). Not opened as primary sources (limit of the cross-check): `N_BUILD_022`,
`L2_BUILD_031`, `CA_K_001`, `CA_K_002` (used only through their reading in `ROUND_003_7` §Cross-check and `REVIEW_003`,
which confirms them); phase 202 (exterior table); phase 206 except the NODE_001 line that names the Green kernel
of the pole; 211 `ROUND_003_B` (only via LEDGER C9); the 42 Farey files except INV_C_001; the
total positivity files of phases 102–116 and 186. A search without matches does not prove novelty.

### (1) Closest antecedent

- `ROUND_003_7` Lemma 1 and "not excluded" (factor on divisibility: format NO-GO), with `ROUND_001_B` §4.
- `INV_C_001` §1 (phase 194): the fibration of pairs (m, n) by the ratio r ∈ ℚ_{>0} with fibre mass κ_K(r);
  the Farey/coprime ordering of the pairs was examined there and lands on an object without sign information
  (the weights of prime ratios are 1, not Λ(q), except by insertion by hand).
- 211 LEDGER C9 (`ROUND_003_B`): size metrics |log m/k| and factorization metrics log(lcm/gcd) coupled on
  𝔸_M: reformulation, explicit negative minors.
- phase 205 `SKELETON_001` §5: Green identity of the pole (kernel e^{|s|/2} = rank 2 + Green of ¼ − ∂²) in the
  window: it is the only Green-type structure recorded; it lives in the pole, not in 𝖡 nor in Near.
- AUDIT_A index A14a-1/2: total positivity of order ≥ 5 of the de Bruijn–Newman kernel, NO-GO CITED; it is not 𝖡.

### (2) Genuinely new object

There are no new ℋ_T, V_T, ρ_T. I do not know how to write a W with support on the near-coincidences and its own formula that carries
a sign. What this memo contributes are three delimitation pieces, proved in §1, which answer (i), (ii) and (iv):

- **Lemma A (coupling graph; PROVED except for one citation).** Exact description of the supports of Div, Near, Arch;
  the support of Div + Near depends on the weight only through the finite set {n ≤ n_* : a(n) ≠ 0}.
- **Lemma B (order structure; PROVED).** The near-divisibility relation is not a partial order (it is not
  transitive); its support is contained in the threshold semiorder {m/k > 2e^{−θ_0}} and coincides with it for
  m/k ≥ R_0. Every "Möbius function" extracted from the pattern is, except on a bounded set of ratios, that of the
  threshold semiorder, which does not depend on the weight.
- **Lemma C (closure under elimination; format NO-GO, PROVED).** If 4T_0 < log 2, 𝖡 takes strictly
  negative values on (θ_0, log 2 − θ_0) and 𝖡(0) > 0; and 𝖡 does not coincide on (0, ∞) with any Laplace transform of a
  measure (in particular with no finite sum of exponentials). Hence 𝔸_M, for large M, belongs to none
  of the families closed under Schur complement that the task asked about: totally
  positive or sign-regular kernels of order 1, Green matrices of a tree or of the line with positive weights
  (semiseparable of bounded rank), f(gcd) matrices.

### (3) Why the change would avoid the antecedent's difficulty

It does not avoid it. The antecedent (`ROUND_003_7` Lemma 1) fails by format: the divisor incidence does not see the
nearly proportional coprime pairs. Passing to the near-coincidence support corrects the format (the support is no longer
sparse: Lemma A shows it is almost complete outside a band around the diagonal), but Lemma B shows
that the combinatorial structure of that support is essentially a threshold semiorder independent of the weight, and
Lemma C that 𝖡 is in no known class closed under elimination. The arithmetic information is in the
**values** of the entries of Near, not in their pattern; an explicit pivot would have to be read from the values, and that
is the LDL of `ROUND_003_2` Lemma 2 (circular, RULES_AVOID J3).

### (4) Identity that would connect with global positivity

None written. The form it would have to take: 𝔸_M = WᵀDW + ρ_M with D ≥ 0, W supported on the graph of Lemma A,
W and D given by their own formula in the values Λ(n), n < M e^{θ_0}, and ρ_M with manifest sign; by Lemma 2 of
`ROUND_003_7` (prime sites already equivalent) the restriction of WᵀDW to primes would have to carry high rank, which
the support of Near allows (Lemma A(c)) but which no antecedent nor this memo realizes. What does get fixed
(Lemmas B, C): the "closure under elimination" that would make the pivots an identity cannot come from the class of the
kernel 𝖡 nor from the support pattern; it would have to be a property of the family {𝔸_M} that uses the exact values.

### (5) cΛ and a_P: why the remainder would stop being ≥ 0

- For any construction using only the pattern of Lemma A (and its Möbius, Lemma B): the pattern is identical for
  all c > 0 (Lemma A(d)), hence W and D would be the same for cΛ and for Λ; the remainder ρ^{(c)} = 𝔸^{(c)} − WᵀDW =
  ρ^{(1)} + (1 − c)(Div + Near) is affine in c, and its positivity set is an interval of c. No line
  breaks it through the pattern; the breaking would have to come from (Div + Near) being neither ⪰ 0 nor ⪯ 0 in the direction of ρ,
  i.e. from values. By R3-i this is not a mechanism: it is the condition itself.
- a_P deletes the powers of primes p < P: the pattern changes only at bounded ratios (Lemma A(d)) and in Div; on
  the rest of the support (ratios ≥ R_0, P-dependent) the pattern coincides. The breaking cannot be in the pattern
  of large ratios.
- In a W with its own values (not written) the breaking must be pointed out in the values; there is no object in which
  to point it out.

### Verdict of the cross-check

No new mechanism. The zone "W with support on m ≈ kn" is delimited: its pattern is a semiorder nearly independent
of the weight, and 𝖡 does not belong to classes closed under elimination. Three delimitation lemmas are proved (§1); none
carries a sign. No candidate ready for construction.

## 1. Proofs

### Lemma A (coupling graph)

Let a be a real weight ≥ 0 on {n ≥ 2} (Λ, cΛ, a_P), v_n^a = 2a(n)n^{−1/2}. For m > k ≥ 1, r := m/k.

(a) **Div** (PROVED, P46 prop:AM(iii)): (Div)_{mk} = ½ v^a_{r} if r ∈ ℕ, and 0 otherwise. Potential support: k | m with
a(m/k) ≠ 0 (for Λ: m/k a prime power). Zero diagonal.

(b) **Near** (PROVED, ibid.): (Near)_{mk} = ½ Σ_{n ≥ 2, n ≠ r} v^a_n c_0(log(kn/m)), and the term n contributes only if
|log n − log r| < θ_0. Potential support: there exists n ≥ 2, n ≠ r, a(n) ≠ 0, with n ∈ (r e^{−θ_0}, r e^{θ_0}). Since n ≥ 2,
this requires r > 2e^{−θ_0} > 1. Zero diagonal; moreover Near_{mk} = Near_{km}.

(c) **Arch** (PROVED from STATEMENT_001 §3 and P46 lem:transl(iv)): for d := log r > θ_0,
Arch_{mk} = β(d) = −Σ_{j≥1} γ_j e^{−(2j+½)d}, γ_j = ∫e^{(2j+½)u}c_0(u)du. Since F_0 is even and real (g ∗ g̃ and G_0 are
even), γ_j = (∫F_0(t)e^{(2j+½)t}dt)² ≥ 0, and ∫F_0 e^{st} = F̂_0(−is) = (¼ − s²)ĝ(is)²ĝ(−is)² with
ĝ(±is) = (e^{(b∓s)a} − 1)/(b ∓ s), real and nonzero if b ≠ ±s. Thus, for b ∉ {±(2j+½)}, γ_j > 0 for all j ≥ 1, and
Arch_{mk} < 0 for every ratio r > e^{θ_0}: Arch couples **all** pairs, with negative entries outside the
band |log r| ≤ θ_0 and decay e^{−5d/2}.

(d) **Dependence of the support on the weight.** CITED (prime number theorem): for each η > 0 there exists x_η with
a prime in (x, x(1+η)) for all x ≥ x_η. I take η with 1 + η ≤ e^{θ_0}. For r ≥ R_0 := x_η e^{θ_0}, the two
intervals (r e^{−θ_0}, r) and (r, r e^{θ_0}) each contain a prime, and at least one is ≠ r. Hence, for every weight
with a(p) ≠ 0 at all primes p ≥ x_η (in particular Λ, cΛ with c > 0, and a_P if moreover R_0 ≥ P e^{θ_0}):
**every pair with r ≥ R_0 is in the potential support of Near.** For
r < R_0, the support depends only on {n ≤ n_* := R_0 e^{θ_0} : a(n) ≠ 0}, a finite set. Consequently:

- the potential support of Div + Near is the same for Λ and for cΛ, all c > 0 (PROVED, trivial: a(n) ≠ 0 does not change);
- for a_P it differs from that of Λ only at pairs with r < R_0(P) (PROVED given what is CITED).

Remark: "potential support" because a sum Σ v_n c_0(·) can vanish by cancellation (c_0 changes sign);
the effective support is a subset. ∎

### Lemma B (order structure of near-divisibility)

Let ⊲ be the relation k ⊲ m :⟺ m > k and (m, k) in the potential support of Div + Near (Lemma A) for the weight Λ.

(a) ⊲ is contained in the threshold semiorder S := {(k, m) : log m − log k > log 2 − θ_0}. PROVED: Lemma A(a),(b).
S is a semiorder (unit interval order on the log line): x ≺ y ⟺ y − x > δ, δ := log 2 − θ_0 > 0.

(b) ⊲ is not transitive in general, hence it is not a partial order and has no incidence algebra nor
Möbius function of its own. PROVED by example: 1 ⊲ 2 (Div, Λ(2) > 0); 2 ⊲ 6 (Div, 6/2 = 3, Λ(3) > 0); but (1, 6) is not in
the support if θ_0 < log(7/6): Λ(6) = 0, and the interval (6e^{−θ_0}, 6e^{θ_0}) ⊂ (5, 7) contains no integer
n ≠ 6. Hence 1 ⊲ 2 ⊲ 6 and not 1 ⊲ 6. ∎
The transitive closure of ⊲ is contained in S (S is transitive: δ + δ > δ) and contains all pairs with
r ≥ R_0 (Lemma A(d)).

(c) Consequence for "Möbius" pivots. Any pivot construction that depends only on the order
(transitive closure of ⊲, or S) is: at ratios r ≥ R_0, identical to that of the semiorder S, which depends only on δ
(archimedean) and not on the weight; at ratios r < R_0, it depends on the weight only through the finite set
{n ≤ n_* : Λ(n) ≠ 0}. PROVED (Lemmas A(d), B(a)). By B1/B5 of RULES_AVOID (class closed under modifications that
preserve that finite set, e.g. f_t with λ₁ > n_*, or cΛ), such a construction cannot carry the sign
alone. It is a class NO-GO for "pivots determined by the support pattern", not for W with its own values.

The semiorder S, restricted to {log m : m ≤ M}, is indeed an interval order and its Möbius function is explicit
via chains (μ_S(x, y) = Σ_{chains} (−1)^{length}), but it contains no datum of Λ. A "Möbius inversion in
the semigroup of intervals" (the one that turns sums over (r e^{−θ_0}, r e^{θ_0}) into point values) is
deconvolution by c_0, which is exactly passing from Near to the point measure Σ v_n δ_{log n}: it returns the comb, not
a pivot. ARGUED (it is the definition of Near as a convolution, P46 prop:AM(iii)).

### Lemma C (𝖡 is not in the classes closed under elimination)

Hypotheses: 4T_0 < log 2 (i.e. θ_0 < log 2 − θ_0), b ∉ {±(2j+½) : j ≥ 1}.

(a) 𝖡(d) < 0 for d ∈ (θ_0, log 2 − θ_0). PROVED: there |log n ± d| ≥ log 2 − d > θ_0 for all n ≥ 2, hence the comb part
vanishes and 𝖡(d) = β(d) = −Σ_{j≥1}γ_j e^{−(2j+½)d} < 0 by Lemma A(c).

(b) 𝖡(0) = a_{T_0}(F_0) (P46 thm:band, STATEMENT_001 §3). It is > 0 in the certified windows T_0 ≤ ½ log 5
(PROVED in P46; here T_0 < (log 2)/4 is inside). If 𝖡(0) = 0 with 𝖡(d) < 0 at another point, 𝔸_M would no longer be ⪰ 0
for the pair {log 1, log m} with log m ≈ d — this does not happen by what is certified; 𝖡(0) ≥ 0 and (a) suffice.

(c) 𝖡 restricted to (0, ∞) is not the Laplace transform ∫e^{−td}dν(t) of any signed measure ν for which
that integral converges in a neighbourhood of (0, ∞) (in particular it is not a finite sum of exponentials). PROVED: such a
transform is real-analytic on (0, ∞). On (θ_0, log 2 − θ_0) it would coincide with β, and β on (θ_0, ∞) is also a
series of exponentials −Σγ_j e^{−(2j+½)d} analytic on (θ_0, ∞); two analytic functions that coincide on an
interval coincide on (θ_0, ∞); hence the comb part would be ≡ 0 on (θ_0, ∞). But for d ∈ (log 2 − θ_0, log 2 + θ_0)
with θ_0 < (log(3/2))/2 the only n that contributes is n = 2 and the comb part is −½v_2 c_0(log 2 − d), which equals
−½v_2 ≠ 0 at d = log 2. Contradiction. ∎

(d) Consequences (PROVED from (a)–(c) and the definitions of each class):
- Totally positive kernels, or sign-regular of order 1 (all entries of the same sign): excluded by
  (a)–(b): for large M there exists a pair m > k with log(m/k) ∈ (θ_0, log 2 − θ_0) (density of the log(m/k)), so
  𝔸_M has entries > 0 (diagonal) and < 0. Total positivity requires in particular entries ≥ 0.
- Pólya frequency functions (PF₂ or higher): require 𝖡 ≥ 0 and log-concave; excluded by (a).
- Green matrices of the line or of a tree, semiseparable of rank ≤ r (those closed under Schur
  complement with explicit parameters): for ordered points x_1 < … < x_M they require 𝖡(x_j − x_i) = Σ_{l≤r} u_l(x_i)w_l(x_j)
  for i < j; for a continuous difference kernel and for all M this forces (functional equation of
  d'Alembert/Levi-Civita, CITED) 𝖡|_{(0,∞)} to be a finite sum of exponential-polynomials, excluded by (c).
- f(gcd) matrices: the entries on distinct primes would be constant f(1); 𝖡(log p − log q) is not constant
  (`ROUND_003_7` Lemma 1, steps 2–3). Excluded.
- Conditionally positive definite functions of order 1: they are not closed under elimination in the requested sense and
  their positivity on zero-sum vectors is weaker than the target; they provide no pivots. ARGUED.
- Green-type kernels on the line for the Near part alone: Near_{mk} = ½Σ v_n c_0(log n − log r) is the
  convolution of the comb measure with c_0 of compact support; by the same analyticity argument it is not
  semiseparable of bounded rank. PROVED (c_0 ≠ 0 of compact support is not an exponential-polynomial).

All of Lemma C is archimedean or about format: it holds for any weight with a(2) ≠ 0. Format NO-GO, without sign.

## Result

**No new mechanism.** Three PROVED delimitation pieces (Lemmas A, B, C; part (d) of A uses the prime number
theorem, CITED): the coupling graph of 𝔸_M is described; near-divisibility is not a partial order
and its pattern is, except at bounded ratios, a threshold semiorder independent of the weight; 𝖡 belongs to no
class closed under elimination among those examined. No candidate ready for construction.

## What was proved

- Lemma A: Div on k | m; Near on pairs with some n ≥ 2, a(n) ≠ 0, |log(kn/m)| < θ_0 (requires m/k > 2e^{−θ_0}); Arch on
  all pairs, negative outside the band |log(m/k)| ≤ θ_0. The pattern of Div + Near is the same for all cΛ and
  changes for a_P only at bounded ratios.
- Lemma B: ⊲ is not transitive (1 ⊲ 2 ⊲ 6, not 1 ⊲ 6, for θ_0 < log(7/6)); its closure is in the threshold semiorder and
  fills it at ratios ≥ R_0. Pivots determined by the pattern: class NO-GO (blind to cΛ, to f_t with λ₁ > n_*).
- Lemma C: with 4T_0 < log 2, 𝖡 < 0 on (θ_0, log 2 − θ_0), 𝖡(0) > 0, 𝖡|_{(0,∞)} is not a Laplace transform; excludes TP,
  PF₂, Green/semiseparable of bounded rank, f(gcd).

## What failed and why

- The pattern m ≈ kn is neither sparse (almost complete outside the band) nor arithmetically structured: the arithmetic
  lives in the values of Near, not in its support. A factor supported on the pattern with pivots read from the values
  is the circular LDL (J3).
- 𝖡 changes sign and is not analytic on (0, ∞): none of the classical classes of closure under elimination applies.
  The reasons are archimedean (γ_j > 0) and the compact support of c_0; generic in the comb.
- Deconvolution in the "semigroup of intervals" returns the comb Σ v_n δ_{log n}, not pivots.

## What remains NOT excluded

- W with support on the graph and values given by its own formula not derived from 𝔸_M (none written).
- Closure under elimination of the **family** {𝔸_M} using the exact values of Λ (for example, that the Schur
  complement on eliminating the site M be 𝔸_{M−1} for another explicit weight a′, or for another profile F_0′); not examined.
- Classes closed under elimination other than those of Lemma C (for example, low displacement rank matrices
  with an arithmetic generator); not examined.
- The other PROVED reductions ((L2), ladder, continuous profile).

## Concrete next step

1. Record in the index (06 §R9), in the grid and in the ledger: "𝔸_M with factor supported on m ≈ kn: pattern = threshold
   semiorder except at bounded ratios, blind to cΛ (ROUND_004_D Lemmas A–B); 𝖡 outside TP/PF₂/Green/f(gcd) (Lemma C);
   format NO-GO, without sign".
2. The only concrete question remaining from this zone: is there an explicit weight a′ (function of Λ) such that the
   Schur complement of 𝔸_M^{Λ} with respect to a site is, exactly, a matrix 𝔸^{a′} of the same family?
   Before deriving, cross-check it against R3-b/J2 (if a′ is affine in Λ with weight-independent coefficients, it falls there)
   and against phase 70 (Riccati/Darboux, J8), which is the natural antecedent of "the complement is the same family with
   transformed weight".
