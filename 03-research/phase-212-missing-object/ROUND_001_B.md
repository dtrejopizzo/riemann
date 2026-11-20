# Round 1 B — Candidate K2: Schur pivots along a multiplicative nesting of the integers (selection memo)

Target (★): λ_A(T) ≥ 0 for every T, in the reduced form "𝖡 positive definite on ℝ" (P47 thm:oneprofile) or
"𝔸_M ⪰ 0 for every M" (P47 prop:AM). Notation of `../phase-211-sign-sandbox/STATEMENT_001.md` §2: fixed profile F_0,
c_0 = c_{F_0}, support of c_0 in [−2T_0, 2T_0], 2T_0 < log 2, β := 𝖡(0) = 𝔞(F_0).
For finite S ⊂ ℕ, 𝔸_S := [𝖡(log m − log k)]_{m,k∈S}; e_d := translate of F_0 by d, so that
s^⊤𝔸_S s = 𝔞(Σ_{k∈S} s_k e_{log k}). For n ∉ S,

    π(S; n) := inf_{s ∈ ℝ^S} 𝔞(e_{log n} − Σ_{k∈S} s_k e_{log k}),

which is the pivot (scalar Schur complement) β − b^⊤𝔸_S^{−1}b, b = (𝖡(log n − log k))_{k∈S}, when 𝔸_S ≻ 0.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Cross-check

**(1) Closest antecedent.**
- 211/LEDGER C6 and STATE_001 point 4 (lines 213–214): "transport M → M+1; first lemma: exact formula for
  𝔸_{M+1} ⪰ 0 given 𝔸_M ≻ 0 as a scalar Schur complement in the new row". NOT STARTED. It is candidate K2 in the
  natural order of the integers; K2 only changes the order of adjunction.
- P47 subsec:KEP (thm:KEP1, KEP2, KEPdich) and GRID §6 item 27 "KEP: Nevanlinna parametrization of 𝔖(T)" (cell 7F,
  OPEN-RESIDUE, "never written"; P47 itself notes that the parametrization presupposes a known solution). It is the same
  extension problem with nesting by window length.
- 211/LEDGER C7 (route N of phase 160, R160_X_C1 §0.1; phase 35 doc. 99): rigidity mechanism on approximants whose
  recorded objection is that the content passes to the limit.
- 211/ROUND_025_B (C49): local factorization of (ab)^{−1/2} and Schur product test, NO-GO PROVED; the weight of the comb
  is additive over the primes (a derivation of the local product).
- 211/ROUND_003_B (C9): Schur coupling of the two metrics; weighted diagonal dominance reduces to
  Σ_{n|m}Λ(n) = log m used linearly.
- Phase 188, L2_BUILD_028–031: 𝔸_M = Arch − Div − Near; multiplicativity diagonalizes only Div; Near is the
  finite-resolution remainder of |P_s|²·V; restricted families equivalent to the target (reformulation).
- Phase 200, A_MU_FACTORIZATION_001 §1(b) (IDX README l. 520): "Cholesky of the grouped matrix", NO-GO (fixed basis, depends
  on Λ only through the form; exists equally for a_P and cΛ). §1(f) of the same memo and 211/LEDGER C33b: the comb
  collapsed by Λ∗1 = log as derivative of a norm.
- Phase 204, L2_INTERLACE_001 (IDX README l. 594): interlacing for S_{T,k} NO-GO because k → k+1 does not nest and there is no
  rank-one border.
- W-det (P47 thm:wh-detinherit): every determinant that decides inherits the margin.
- 211/POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION: excludes sums of PSD blocks of bounded support; explicitly leaves out
  Schur complements and blocks of growing size.
- Memory of rejected selections (the project rules), "Transport by shift and congruence": a non-diagonal
  transport without explicit coefficients independent of inverting or factoring the matrix itself does not enable construction.

**(2) New object or claim.** The only thing not recorded textually is the question: is there a chain
S_1 ⊂ S_2 ⊂ … ordered by the multiplicative structure (divisor-closed sets, smooth numbers, one prime
at a time) for which π(S_j; n_{j+1}) has a closed expression, non-linear in Λ, which is a square or a quotient
of manifestly positive quantities? This memo finds no such expression. Instead it finds five structural
statements (§§1–6, PROVED, elementary) that explain why the change of order produces no mechanism.

**(3) Why the change would avoid the difficulty of the antecedent.** It does not avoid it. The multiplicative nesting does give
what was missing in L2_INTERLACE (a rank-one border at each step), but the resulting pivot is the value of the
form at a vector obtained by inverting 𝔸_S itself (§1), it is invariant under every triangular substitution of the
incidence algebra, including the one realized by Λ∗1 = log (§3), and it is bounded above by an
archimedean quantity independent of the comb that tends to zero (§5).

**(4) Identity that would connect with global positivity.** Only the tautological one: for a chain that exhausts a
set 𝒮 with log 𝒮 − log 𝒮 dense, "all pivots > 0" implies (★), and (★) implies "all pivots ≥ 0"
(Prop. 1). There is no additional identity.

**(5) Line that breaks for cΛ and for a_P.** None of the identities that can be written breaks: those of
§§1, 2, 5, 6 hold for every comb and that of §3 holds for every comb with another unit instead of the series of
coefficients 1 (Lemma 4). By OBJECT_SPEC §4, a candidate that cannot write (2) and (5) is not ready.

**Verdict of the cross-check: no new mechanism.** The candidate coincides with C6 (different order) and with the matrix
reading of the extension problem of P47 subsec:KEP; the rest of this memo is not a construction but the record
of the precise structural reasons, so that the question is not relaunched.

## 1. Pivot = value of the form at the innovation; reformulation (PROVED)

**Proposition 1.** Let 𝒮 = ℕ, or 𝒮 = {p^x q^y : x, y ≥ 0} with p ≠ q primes, and S_1 ⊂ S_2 ⊂ … a chain with |S_j| = j and
union 𝒮, S_{j+1} = S_j ∪ {n_{j+1}}.
(a) If π(S_j; n_{j+1}) > 0 for every j, then 𝖡 is positive definite on ℝ, that is (★).
(b) If (★), then π(S; n) ≥ 0 for every finite S and every n ∉ S.
(c) If 𝔸_S ≻ 0, the infimum is attained at s* = 𝔸_S^{−1}b and π(S; n) = 𝔞(u), u := e_{log n} − Σ_k s*_k e_{log k} ∈ P_T
(with T such that the translates fit in I_T). Moreover In(𝔸_{S∪{n}}) = In(𝔸_S) + In(π(S; n)).

*Proof.* (a) By induction, det 𝔸_{S_{j+1}} = det 𝔸_{S_j}·π(S_j; n_{j+1}) > 0 (𝔸_{S_1} = (β) and β = π(∅; n_1) > 0),
hence all leading principal minors are positive and 𝔸_{S_j} ≻ 0 (Sylvester's criterion). Every finite
subset of 𝒮 lies in some S_j, so 𝔸_S ⪰ 0 for every finite S ⊂ 𝒮. For 𝒮 = ℕ this is (★) by P47 prop:AM(i);
for 𝒮 = {p^x q^y}, by Prop. 2. (b) e_{log n} − Σ s_k e_{log k} ∈ P_T (P47 lem:transl(i)) and
𝔞 ≥ 0 on P_T. (c) s ↦ 𝔞(e_{log n} − Σ s_k e_{log k}) = β − 2b^⊤s + s^⊤𝔸_S s is a strictly convex quadratic
polynomial; its minimum is β − b^⊤𝔸_S^{−1}b at s*. The additivity of inertia is the Haynsworth formula for the block
(𝔸_S, b; b^⊤, β). ∎

Between (a) and (b) lies the case of a zero pivot, which is not decided by the chain alone.

**Proposition 2 (the 3-smooth numbers suffice; PROVED, trivial variant of L2_028 §1 and L2_031 Theorem E).** Let p ≠ q
be primes and 𝒮 = {p^x q^y : x, y ≥ 0}. Then (★) ⟺ 𝔸_S ⪰ 0 for every finite S ⊂ 𝒮.

*Proof.* (⟹) restriction. (⟸) Γ := ℤ log p + ℤ log q is dense in ℝ (log p / log q is irrational by
unique factorization). Given a_1, …, a_K and ε > 0 choose γ_i = x_i log p + y_i log q ∈ Γ with |γ_i − a_i| < ε, and
integers X, Y with x_i + X ≥ 0, y_i + Y ≥ 0. With m_i := p^{x_i+X} q^{y_i+Y} ∈ 𝒮 one has log m_i − log m_l = γ_i − γ_l.
By continuity of 𝖡, Σ s_i s_l 𝖡(a_i − a_l) = lim_{ε→0} Σ s_i s_l 𝖡(log m_i − log m_l) ≥ 0. ∎

Reading. On 𝒮 = ⟨2, 3⟩ the part Div contains only the powers of 2 and of 3; all other primes enter
exclusively through Near. The same argument holds for the points αℕ + βℕ with any irrational α/β, where
Div = 0 and the whole comb is "Near". The decomposition Div/Near, and with it any multiplicative structure of the
index set, is a property of the sampling points and not of 𝖡: the arithmetic of the problem lies in the
positions log n of the atoms inside the function 𝖡, not in the lattice where it is evaluated. This is already
recorded as a reformulation (IDX README l. 55); it is not progress (RULES_AVOID B3).

**Consequence for K2.** The pivot is the value of 𝔞 at the minimizer of a restricted problem (s_n = 1): it is
a functional of the minimizer (RULES_AVOID B9, OBJECT_SPEC O8). Its non-linearity in Λ is that of 𝔸_S^{−1}, that is,
the one obtained by inverting the object itself (memory of selections, "transport by shift and
congruence"). Since det 𝔸_{S_j} = Π_{i≤j} π_i and, if 𝔸_{S∪{n}} ⪰ 0, λ_min(𝔸_{S∪{n}}) ≤ π(S; n)/(1 + |s*|²) ≤ π(S; n),
the pivots inherit the margin: it is W-det in this basis.

## 2. The Gram realization on the carrier 𝖡 is unique; the order only changes the triangulation (PROVED)

**Proposition 3.** Let 𝒟 ⊂ ℝ and r, r′ : 𝒟 → ℋ, ℋ′ with ⟨r(d), r(d′)⟩ = 𝖡(d − d′) = ⟨r′(d), r′(d′)⟩. Then there is a
unique isometry from the closure of span r(𝒟) onto that of span r′(𝒟) with r(d) ↦ r′(d). If moreover 𝔸_S = R^⊤R + ρ with ρ ⪰ 0,
the stacked map (R; ρ^{1/2}) is a realization with zero remainder.

*Proof.* ‖Σ s_i r(d_i)‖² = Σ s_i s_l 𝖡(d_i − d_l) = ‖Σ s_i r′(d_i)‖²; the map Σ s_i r(d_i) ↦ Σ s_i r′(d_i)
is well defined, isometric and extends to the closure. The second claim is R^⊤R + ρ^{1/2}ρ^{1/2}. ∎

Reading. On the carrier of a profile, the identity (G) of OBJECT_SPEC §1 has, if it exists, a single solution
up to isometry: a curve d ↦ r(d) with ‖r(d) − r(d′)‖² = 2[β − 𝖡(d − d′)]. The integers are samples r(log n) of that
curve and the Cholesky factorization along a chain is the Gram–Schmidt orthogonalization of those
samples in the order of the chain: π(S; n) = dist²(r(log n), span{r(log k)}_{k∈S}). The curve only sees log n ∈ ℝ. Choosing
a multiplicative order changes the triangular basis in which the same realization is written, not the realization.
An explicit pivot for a chain is equivalent to an explicit triangular factor, that is, to complete (G) in a particular
normal form: K2 is not a reduction of (G), it is (G) with an added form condition.

## 3. Λ∗1 = log in the incidence algebra: generic identity, neutral for the pivots (PROVED)

Let 𝒩 ⊂ ℕ be finite and divisor-closed. For arithmetic f, (C_f)_{mk} := f(m/k) if k | m, 0 otherwise (m, k ∈ 𝒩).
Since every d with k | d | m lies in 𝒩, C_f C_g = C_{f∗g}. Let D := diag(log m), z(n) := n^{−1/2}; z is completely
multiplicative, hence (fz)∗(gz) = (f∗g)z, and [D, C_f] = C_{f·log} because log m − log k = log(m/k).

**Lemma 4 (the comb as logarithmic derivative; holds for every comb).** Let a be arithmetic with a(1) = 0 and
𝕍_a := 2C_{az} (the exact-coincidence part of the comb a on 𝒩, Div_a = ½(𝕍_a + 𝕍_a^⊤)). Let u be the unique function
with u(1) = 1 and u·log = u∗a (recurrence u(n) log n = Σ_{d|n, d>1} a(d) u(n/d)), and U := C_{uz}. Then

    𝕍_a = 2 U^{−1}[D, U],        U Div_a U^⊤ = D G + G D − 2 U D U^⊤,   G := U U^⊤ ⪰ 0.

For a = Λ, u ≡ 1, U = Z := C_z, G_{mk} = (mk)^{−1/2} σ(gcd(m, k)) and

    (Z Div Z^⊤)_{mk} = (mk)^{−1/2} Σ_{d | gcd(m,k)} d·[log(m/d) + log(k/d)].

For a = cΛ, u = d_c (coefficients of the c-th convolution power of 1); for a_P, u = indicator of the
integers without prime factors < P.

*Proof.* U is triangular with diagonal 1, hence invertible, and U^{−1} = C_{u^{−1}z} with u^{−1} the convolution
inverse. U^{−1}[D, U] = C_{u^{−1}z} C_{(u log) z} = C_{(u^{−1}∗(u log)) z} = C_{az}. Then
U𝕍_aU^⊤ = 2[D, U]U^⊤ = 2(DG − UDU^⊤) and U𝕍_a^⊤U^⊤ = 2U[D, U]^⊤ = 2(GD − UDU^⊤). For u ≡ 1,
G_{mk} = Σ_{d | (m,k)} (m/d)^{−1/2}(k/d)^{−1/2} and (UDU^⊤)_{mk} = Σ_{d | (m,k)} (mk)^{−1/2} d log d; subtract. ∎

The identity Σ_{d|n}Λ(d) = log n is exactly "u ≡ 1". The form of the identity (comb = U^{−1}[D, U]) is
valid for every comb (RULES_AVOID B1). The version with u ≡ 1 is the prime-free form already recorded: 211/LEDGER C33b,
ROUND_025_B Theorem 1.1/2.1 (weights (NN′)^{−1/2} log(NN′)), phase 200 A_MU_FACTORIZATION §1(f). Here it is written in
matrix coordinates, on exact coincidences; it is not a new result.

**Proposition 5 (neutrality).** Let S_1 ⊂ … ⊂ S_J = 𝒩 be a chain of divisor-closed sets, |S_j| = j, and L
any lower triangular matrix with diagonal 1 in the order of the chain (in particular every C_f with f(1) = 1).
Then, for every symmetric matrix 𝔸 indexed by 𝒩, the leading principal minors of L𝔸L^⊤ and of 𝔸 along
the chain coincide; if they are non-zero, the pivots coincide. Conversely, two symmetric matrices with
non-zero leading minors have the same pivots if and only if they are congruent by such an L.

*Proof.* If k | m then k precedes m in the chain, so C_f is lower triangular in that order. For
unit triangular L, (L𝔸L^⊤)[S_j] = L[S_j] 𝔸[S_j] L[S_j]^⊤ and det L[S_j] = 1. The converse is the uniqueness of the
factorization 𝔸 = L_0 diag(π) L_0^⊤. ∎

Reading. Passing from the form with Λ to the prime-free form is the congruence by Z (Lemma 4), which acts on all of
𝔸_𝒩 = Arch − Div − Near. By Prop. 5 it does not change any pivot of any divisor-closed chain. The
pivots are precisely the invariants of the action of the unipotent group of the incidence algebra; the identity
Λ∗1 = log, used as a triangular substitution, lives inside that group. Hence **there is no "pivot formula
obtained by Λ∗1 = log"** in this class: the identity changes the representation of 𝔸 and leaves the pivot the same.
For integrality to affect the sign of a pivot it would have to enter through an operation that is not a
triangular congruence in the order of divisibility. None is identified.

## 4. The only known mechanism of exact pivots via Σ_{d|n} g(d) = f(n), and why 𝔸 does not have it

**Proposition 6 (gcd paradigm; CITED, classical, one-line proof).** On divisor-closed 𝒩,
[f(gcd(m, k))] = E diag(g) E^⊤ with E_{md} = 1_{d|m} and g = f∗μ; the pivots along every divisor-closed
chain are g(n). With f = log: [log gcd(m, k)] = E diag(Λ) E^⊤ ⪰ 0, with pivots Λ(n) ≥ 0.
*Proof.* Σ_{d | m, d | k} g(d) = Σ_{d | gcd} g(d) = f(gcd). ∎

This is the case in which Σ_{d|n}Λ(d) = log n gives exact non-negative pivots. It does not serve as a sign step: it holds
equally for cΛ (c > 0) and for every g ≥ 0, it is homogeneous (OBJECT_SPEC O10) and it does not contain the archimedean factor.

**Necessary condition for 𝔸 to have a triangular factor with the incidence pattern (PROVED).** If
𝔸_𝒩 = L diag(π) L^⊤ with L_{md} ≠ 0 only for d | m, then for coprime m, k
𝔸_{mk} = L_{m1} π_1 L_{k1}, that is

    β·𝖡(log m − log k) = 𝖡(log m)·𝖡(log k)      for every coprime pair m, k ∈ 𝒩.        (4.1)

*Proof.* 𝔸_{mk} = Σ_{d | m, d | k} L_{md} π_d L_{kd}; if gcd = 1 only d = 1 remains, π_1 = β, L_{m1} = 𝖡(log m)/β. ∎

(4.1) fails (NUMERICAL, with the validation values of STATEMENT_001 §3, profile a = 0.15, b = 1: β = 0.01492 and
|𝖡(d)| ≤ 0.0122 for 0 < d ≤ 13): for m = k + 1 with k large within that range, the left-hand side is
β² − O(β κ_0/k²) by Prop. 7 and the right-hand side is ≤ 0.0122² < β². No new computation has been done; κ_0 has not
been evaluated, and this remark supports no other claim of the memo. The structural reason, without numbers: in an
incidence pattern the columns of two coprime integers share only the coordinate of 1, whereas in the realization
of Prop. 3 the columns of k and k + 1 are almost parallel (§5). The same excludes any sparse pattern fixed by
divisibility; it is the phenomenon C_{ij} → 1 of 211/POWER_FIXED_BLOCK_ASSEMBLY §3 in this basis.

## 5. Collapse of the pivots: archimedean upper bound, independent of the comb (PROVED)

**Proposition 7.** Let κ_0 := (1/2π)∫ |m(τ)| τ² F̂_0(τ)² dτ (finite: F̂_0(τ) = O(τ^{−2}), m(τ) = O(log(2 + |τ|))).
For every finite S, n ∉ S and k ∈ S,

    π(S; n) ≤ 2[β − 𝖡(log n − log k)].

If d := |log n − log k| < log 2 − 2T_0, the right-hand side is (1/π)∫ m F̂_0² (1 − cos τd) dτ, it does not contain the comb, and
|2[β − 𝖡(d)]| ≤ κ_0 d². In particular, in the natural order π({1, …, n−1}; n) ≤ κ_0/(n−1)² for n ≥ n_0(T_0), and
if 𝔸_{[1,n]} ⪰ 0 then λ_min(𝔸_{[1,n]}) ≤ κ_0/(n−1)².

*Proof.* Take s = (canonical vector of k) in the infimum: 𝔞(e_{log n} − e_{log k}) = 2β − 2𝖡(log n − log k). For
|d| < log 2 − 2T_0 and n′ ≥ 2, log n′ ± d > 2T_0, hence c_0(log n′ ± d) = 0 and the comb part of 𝖡(d) is zero;
so is that of 𝖡(0). The archimedean part remains and 1 − cos x ≤ x²/2. In the natural order d = log(n/(n−1)) ≤
1/(n−1). The bound on λ_min is the one at the end of §1. ∎

Reading. For every chain whose points accumulate on a logarithmic scale (every chain in ℕ, and every chain in the
P-smooth numbers with at least two primes) the pivots tend to zero, with a bound that is the same for Λ, cΛ,
a_P, finite deletions and amplifications and any comb supported on log ℕ_{≥2}. A pivot written as a "quotient
of manifestly positive quantities" would need a numerator vanishing at least to second order in the
distance to the nearest previous point, for a purely geometric reason (the non-orthogonality of neighbouring
translates of F_0); the comb only intervenes in the sign of a quantity already bounded by κ_0 d². The pivot recursion has no
uniform margin at any late step and its limit object (pivot after infinitely many steps) is zero. This is the
form taken here by the objection recorded in C7: the content of "pivot ≥ 0 at each step" lies in the sign of
vanishing quantities, not in a bound at a fixed step. It is not a NO-GO (an exact identity could sign a
quantity that tends to zero); it is a design restriction that the candidate does not resolve.

## 6. Where Near is invisible: Kronecker sum, not product (PROVED)

In multiplicative boxes without visible near-coincidences the comb part is a Kronecker sum of local Toeplitz
matrices (P47 rem:boxes, L2_029 §2). The Cholesky factorization respects tensor products, not sums:

**Proposition 8.** Let A = A_1 ⊗ I + I ⊗ A_2 with A_2 = (A_2′, b; b^⊤, α) symmetric of order K + 1. The Schur
complement of the last layer (index K + 1 of the second factor) is σ(A_1), with σ(x) := α + x − b^⊤(A_2′ + x)^{−1}b
= det(A_2 + x)/det(A_2′ + x), provided A_2′ + λ is invertible for each eigenvalue λ of A_1.

*Proof.* Diagonalize A_1 = QΛQ^⊤; A is a direct sum over the eigenvalues λ_i of the matrices A_2 + λ_i, and
the Schur complement of each one is σ(λ_i). ∎

Thus, even in the model without Near, the pivot when adjoining a power of a prime is not a product of local
pivots but a rational function of the matrix of the other primes, and its positivity is the additivity of the
spectra, which is the content of rem:boxes and of prop:nearfree (local bounds against archimedean energy, with
slack). It is the version, for triangular factorizations, of the reason of C49: the weight of the comb is additive over
the primes and a product (Schur there, tensor here) has no room for it. With the fixed profile F_0 the
near-coincidences appear in every sufficiently large box, so this model does not describe 𝔸.

## 7. The possible multiplicative nestings and answer to each antecedent

There are three ways of nesting "one prime or one integer at a time".

(I) **Nesting the index set** (principal submatrices of the same 𝖡). This is what was analysed in §§1–6:
reformulation (Prop. 1–2), pivot = functional of the minimizer, neutral with respect to Λ∗1 = log (Prop. 5), no
incidence pattern (§4), no margin (Prop. 7). Near enters the pivot exactly, but trivially: it is in each
entry of b and of 𝔸_S, and the formula containing it is β − b^⊤𝔸_S^{−1}b.

(II) **Nesting the comb** (adjoining the atoms of a prime to the weights, with 𝖡 changing at each step). The intermediate
objects are not positive semidefinite: the end "small primes missing" is the falsifier a_P, and for the
other end 211/ROUND_025_B §4 records (NUMERICAL) that every partial sum by prime support is negative of order 1
and that positivity appears only with the complete set. There is no recursion of positive pivots passing through
indefinite objects; each step subtracts a matrix of symbol v_{p^j} cos(τ j log p) F̂_0², without sign.

(III) **Nesting both at once** (P-smooth indices and comb). It is the semilocal chain over finite sets of
places, recorded as closed without sign (RULES_AVOID §C, "Sonin, prolates, semilocal"; IDX phases 183–186). It is not
reopened.

Answers.
- **C7 / "dies in the limit".** Route N applied rigidity to a state in a finite window. K2 does not use rigidity;
  its analogue of the objection is Prop. 7: the pivots have no uniform margin and the limit pivot is zero for every
  comb. The objection is not answered, it is localized.
- **P47 subsec:KEP and GRID 7F.** The matrix version of the parametrization is: given 𝔸_S ≻ 0, the admissible rows b
  form the ellipsoid b^⊤𝔸_S^{−1}b ≤ β and the Schur parameter is 𝔸_S^{−1/2}b/√β. It presupposes 𝔸_S ≻ 0 and its inverse,
  just as the continuous parametrization presupposes a solution. Replacing window length by multiplicative order
  does not alter that dependence (Prop. 3: it is the same realization triangulated in another order). Residue 7F stays as
  it is: unwritten and without value for the sign.
- **C49.** §6 is its analogue for triangular factorizations; same reason (additivity over primes).
- **C9.** There Σ_{n|m}Λ(n) = log m enters as a row sum (Schur test with weights k^{−1/2}), a linear use with
  slack. In a pivot the row of Div is paired with 𝔸_S^{−1}b, not with k^{−1/2}; the only exact use of the
  identity is the congruence by Z, neutral (Prop. 5).
- **L2_028–031.** Prop. 2 is another restricted family equivalent to the target; same label ("reformulation or
  trivial").
- **POWER_FIXED_BLOCK_ASSEMBLY.** The Cholesky columns have growing support, so K2 does not fall into the class
  excluded there; the obstruction of that memo reappears only as §4 (no fixed sparse pattern).
- **Phase 204, grouped Cholesky and interlacing.** The NO-GO of grouped Cholesky applies as is: the triangular
  basis depends on Λ only through the form and exists equally for cΛ and a_P as long as the minors do not vanish.
  The obstacle of L2_INTERLACE (no rank-one border) does not apply to K2, which does have one; what is obtained with
  it is the inertia formula of Prop. 1(c), without sign content.
- **W-det.** Confirmed in this basis: det 𝔸_{S_j} = Π π_i and π ≥ λ_min (§1, §5).

## 8. Falsifiers

No sign step is taken. For each statement, the behaviour under the battery:
- Prop. 1, 2, 3, 8 and condition (4.1): valid for every comb with the same structure (cΛ, a_P, finite deletion and
  amplification, b_θ, discrete Beurling systems with the lattice of their generalized integers, and the
  models without Euler product). They are reformulations or linear algebra; they distinguish nothing.
- Lemma 4: the form of the identity holds for every comb with another unit u; with u ≡ 1 it holds only for Λ (for cΛ,
  u = d_c; for a_P, u is the indicator of the P-rough integers; for deletions, amplifications and b_θ the
  recurrence gives another u ≢ 1). But Prop. 5 shows that this difference does not reach any pivot. For the models
  whose comb is not supported on log ℕ with this structure (Epstein, Davenport–Heilbronn, Beurling) the lemma
  applies on the corresponding index lattice or does not apply; it has not been examined case by case.
- Prop. 7: the bound is identical for all falsifiers with atoms in log ℕ_{≥2}; for a Beurling system
  with first generalized integer g_1 > 1 it holds with log g_1 instead of log 2.
- Quartets and f_t: they preserve Λ(n) and hence every claim of this memo that depends only on the comb; no
  claim here separates them.
If any of these propositions were presented as a sign step it would survive all the falsifiers and would be
wrong by rule 6 of the brief. None is presented that way.

## Result

**No new mechanism.** Candidate K2 is not ready for construction: it cannot write the object (explicit
triangular factor) nor the line that breaks for cΛ and a_P. A class NO-GO is not declared: it has not been proved that
no explicit triangular factor can exist; it has been proved that the three available sources of explicitness
(substitution via Λ∗1 = log, incidence pattern, product over primes) do not produce it.

## What was proved

- Prop. 1: pivots along an exhausting chain ⟺ target (with the caveat > / ≥); pivot = 𝔞 at the
  innovation; additive inertia. PROVED, reformulation.
- Prop. 2: the indices {p^x q^y} suffice; the partition Div/Near depends on the sampling points. PROVED, reformulation.
- Prop. 3: uniqueness up to isometry of the Gram realization on the carrier 𝖡; a chain only chooses the order of
  orthogonalization. PROVED.
- Lemma 4: Div_a = sym(U^{−1}[D, U]) for every comb; for Λ, Z Div Z^⊤ = DG + GD − 2ZDZ^⊤ with
  G = [(mk)^{−1/2}σ(gcd)]. PROVED; coincides with the prime-free form already recorded.
- Prop. 5: the pivots of divisor-closed chains are invariant under triangular congruences of the incidence
  algebra; Λ∗1 = log used as a substitution is neutral. PROVED.
- Prop. 6 and (4.1): the gcd paradigm gives pivots Λ(n) for [log gcd]; for 𝔸 it would require rank one on coprime
  pairs. The condition PROVED; its failure NUMERICAL.
- Prop. 7: π(S; n) ≤ 2[β − 𝖡(log n/k)] ≤ κ_0 log²(n/k) for nearby points, without comb. PROVED.
- Prop. 8: Schur complement of a Kronecker sum = function of the matrix of the other factor. PROVED.

## What failed and why

- There is no closed formula for the pivot. The non-linear dependence of π(S; n) on Λ is that of 𝔸_S^{−1}; every
  explicit expression is equivalent to an explicit triangular factor, that is, to the whole identity (G) (Prop. 3).
- Σ_{d|n}Λ(d) = log n does not produce a pivot identity: as a triangular substitution it is neutral (Prop. 5) and as a
  row sum it is linear and with slack (C9, prop:nearfree).
- Adjoining n to a divisor-closed set changes the Schur complement by 𝔞(u), with u the innovation in
  P_T: the sign of the new term is the target evaluated at a vector that depends on the form itself (B9).
- The structure over primes is additive (Kronecker sum, derivation), not multiplicative; Near is not a separate
  operator but the orthogonality defect of the translates (L2_030 §2), and it enters every entry.
- The late pivots have no margin and their upper bound is unrelated to the comb (Prop. 7).

## Next concrete step

None within K2. For the record (this memo does not edit other files):
LEDGER line of phase 212 "K2: pivots by multiplicative nesting — no new mechanism; Prop. 5 and 7
as tools"; close 211/C6 with the same reference; note in IDX (family "integer-lattice matrices and
multiplicative sets") and in GRID 7F: "the matrix variant with multiplicative order is the same realization
(Prop. 3); pivots invariant under the unipotent incidence group (Prop. 5)".
Reopening condition: an explicit operation, which is neither a triangular congruence in the order of
divisibility nor requires inverting 𝔸_S, by which u ≡ 1 (Lemma 4) enters the pivot together with the
archimedean kernel, and whose numerator vanishes to the order required by Prop. 7. None is known.
