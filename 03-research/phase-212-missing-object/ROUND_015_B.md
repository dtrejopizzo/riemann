# Round 15, memo B: coupling distinct primes in the block split, and GCD matrices as coupling

Summary. A source of positivity that couples distinct primes and is not exponential in the weight is put
through the gate. There are two variants: (i) a joint split by pairs or triples of primes, with a cross block
(2,3) built from the near-coincidences `2^a ≈ 3^b`, and the hierarchy of levels it induces; (ii) the positivity
of GCD matrices (Smith, Jordan totients), of Gál-type sums and of the
Nyman–Báez-Duarte Gram used as coupling. Both variants are repetitions. (i) is Observation 4.3
(«blocks») of `phase-159-row-d-two-front-construction/G2_B8_R5.md`; its exact level is the form itself (J3).
Moreover, the obstructing pair of round 6 is not a quantum marginal problem (§2). In (ii), restricted to
prime powers, the Smith factorization splits by primes plus a rank-one term (Lemma 2,
PROVED). Hence it cannot carry the coupling between `log 2` and `log 3`. It uses only divisors, so it is blind to the
controls (S2, Lemma T). An observation not mentioned in round 6 is recorded: the threshold `0.695–0.70` of the
DIR split coincides with the entry of the contact `4 = 2²` (NUMERICAL/ARGUED, §4).

Primary reading: `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§1–10; `RULES_AVOID.md` O–X; `ROUND_014_B.md`;
`G2_B8_R5.md` §§2–5 (Theorem D, Lemma 2.1, Observation 4.3, §5 «cross-prime interference»);
`phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md` §0; `phase-122-*/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md`
§3. Grep in `03-research` and the index for «gcd», «Smith», «Gál», «Nyman», «Báez», «marginal», «compatib»,
«two-prime», «dos primos». Relevant hits: the four files above; `R184_010_THEOREM_L_STAR.md`
l.117 (Franel form `Σ c_q c_{q′} gcd(q,q′)²/(12qq′)`); `MAP_1_WALLS_AND_MASTER_DOCS.md` NG-A5, NG-B4,
CIR-3, CIR-6 (Beurling–Nyman and Báez-Duarte: reformulations, circular distance). The other hits
use the words in passing (line-by-line reading, ARGUED). I did not reread REVIEW_006 or phases 188 in full.

## 0. Four-point filter

1. **Closest antecedent.** `G2_B8_R5.md` Observation 4.3: «primes grouped into blocks with one LK piece per
   block. Theorem D and Lemma 2.1 hold verbatim with `Q_B = Σ_{p∈B}Q_p` … The single block `{2,3}` is `𝔞_T`
   itself». And §5: positivity on `(T_loc, log 2]` is an interference between the values of **one** positive
   definite function `c_F` at `log 2` and at `log 3` («necessarily cross-prime»). For the cross block `X`:
   `ROUND_006` §10.2 (minimal transfer, rank one, no formula) and `RULES_AVOID` O3 (signed parts without a
   rule: empty split). For two primes with explicit coupling: Doc 135 of phase 45 (the Weil data add up
   and the mixed support `p^a q^b` has zero mass) and P122_028 (effective two-prime energy `‖y−x‖²/log(q/p)`).
   For (ii): `R184_010` (Franel form with gcd), NG-B4/CIR-3 (Nyman), NG-A5 (Báez-Duarte), `RULES_AVOID` S2.
2. **What is proposed as new.** A joint block `q_{23}` whose cross term is an operator written from the
   near-coincidences `9/8, 4/3, 3/2, 32/27, 256/243`, and a hierarchy by levels of pairs and triples. For (ii),
   the GCD matrix as cross term.
3. **Does it avoid the difficulty?** No.
   - (i) If the joint block must be `⪰ 0` and the window sees only 2 and 3 (and 4), that block is `a_T` (or
     `a_T` minus an archimedean part). The exact level is the statement itself (J3). With an explicit `X` but
     without an identity making it signed, one falls back into O3.
   - (ii) Between powers of distinct primes, GCD positivity couples nothing except the divisor 1 (Lemma 2), and
     it uses neither `Λ` nor the additive structure.
4. **Global link.** One would need an identity
   `a_T = Σ_B q_B + (squares)`, with `q_B ⪰ 0` written without solving the problem and with blocks of
   bounded size, valid for all `T`. With blocks of bounded size and `T → ∞`, the window contains more and more
   primes per block. Theorem D (max dual) holds with blocks, and the explicit proofs of round 4
   exclude every grouping with at least eight blocks touching `S_0` for `T ≥ 1.50` (Observation 4.3,
   PROVED there). I have no identity connecting to the global sign.

By the filter rule, the memo stops here as far as construction goes. What follows fixes the closure and the
two clarifications.

## 1. Block hierarchy (repetition; the exact level is circular)

**Proposition 1 (PROVED, direct corollary of G2_B8_R5 Theorem D + Observation 4.3).** Let `𝔅` be a partition of
the primes with contacts in `[0,2T]` into blocks `B`. The block split (one LK piece, or DIR with free
potential, per block) exists if and only if `Φ^𝔅_T := inf Φ_T[(σ_B)] ≥ 0`. Here the infimum runs over the families of
states indexed by blocks; in the DIR class the equal-density constraint of `ROUND_006` §5 also applies,
which is ARGUED there and is not rederived. If `𝔅` is finer than `𝔅′`, then `Φ^𝔅_T ≤ Φ^{𝔅′}_T`. For the
trivial partition (a single block) one has `Φ_T = λ_A(T)`, the bottom of `a_T` on `P_T`.

*Proof.* Monotonicity follows because a family indexed by `𝔅′` induces a family indexed by `𝔅`, repeating
the state of each coarse block on its fine blocks, and because `max` over more copies of the same `ε` does not change. The
last case is the equal family (step 5 of Theorem D). ∎

Consequence. «The level-`k` hierarchy is exact for windows with at most `k` primes» is true and says
nothing: at that level the certificate is `a_T ⪰ 0`. The level-`k` certificate is manifestly non-negative only
if each `q_B` is so by its own formula; without one it is J3. Step that breaks under the controls: none. The
split is comb-general (G2_B8_R5 §6, F4) and certifies exactly when the bottom is `≥ 0` (`ROUND_006` §6). With
`2Λ`, deletion or Beurling it simply does not exist, without a signed remainder changing sign. This is the pattern of
`ROUND_013_A` W1.

## 2. Is the failure a problem of compatible marginals? (not in the quantum sense)

**Proposition 2 (structure of the dual; ARGUED, on the DIR duality of `ROUND_006` §5, which is not proved in the
continuum).** The dual of the DIR split is a pair `(Y_2, Y_3)` of states on the **same** space `L²(I)` with
equal diagonal density `ρ_{Y_2} = ρ_{Y_3}`. The joint split (a single block) is the case `Y_2 = Y_3`. The
gap between the two levels is the gap between «same diagonal» and «same state».

There is no tensor product or joint system of which `Y_2` and `Y_3` are partial marginals. The relevant
«compatibility» is equality, not the existence of an extension. The quantum marginal problem
(common extension of reduced states) does not apply as such. The correct reading is that of Theorem D:
the archimedean part charges `max_p ε_{σ_p}`, a sublinear functional. The natural hierarchy goes not by number of
primes but by the class of permitted transfer:

| transfer between pieces | dual constraint | status |
|---|---|---|
| potential `W_p(t)` only | equal diagonal density | DIR, fails at `T ≥ 0.70` (NUMERICAL) |
| potential + jump kernel `θ_p ∈ [0,1]` | the above + pointwise `max` of `D_p` | is DIR (`ROUND_006` §5) |
| arbitrary form `X` | `Y_2 = Y_3` | empty, it is the goal (O3) |
| rank-one `X` with given `ℓ` | intermediate | `ROUND_006` §10.2: `ℓ` without formula |

An intermediate level with `X` restricted to kernels concentrated at the delays `log(3^b/2^a)` is a choice of
`ℓ`. I do not have the formula, and the measured optimal `ℓ` resembles projected `cos(2πt/log 2)` (`ROUND_006` §10.2),
not an object at `log(9/8)` or `log(4/3)`. OPEN, no candidate.

## 3. GCD and related matrices as coupling (repetition and blindness)

**Lemma 2 (PROVED).** Let `σ > 0` and `J_{2σ}(d) = d^{2σ} Π_{p|d}(1 − p^{−2σ})`. For `m, n` in
`𝒫 = {p^a : p prime, a ≥ 1} ∪ {1}`:

`gcd(m,n)^{2σ}/(mn)^σ = (mn)^{−σ} Σ_{d|m, d|n} J_{2σ}(d)`.

Restricted to `𝒫`, this decomposition is the sum of a rank-one term (`d = 1`,
`(mn)^{−σ}`) and of blocks per prime (`d = p^j`, `j ≥ 1`, which touch only the powers of `p`).

*Proof.* The identity is Smith's (`Σ_{d|k} J_{2σ}(d) = k^{2σ}`, CITED/classical, with `k = gcd(m,n)`). If `m`
and `n` are powers of distinct primes, the only common divisor is `1`. ∎

Reading. Between `2^a` and `3^b` the GCD coupling is only the rank-one `(2^a 3^b)^{−σ}`, which does not depend on
`2^a/3^b` being close to 1. It is a multiplicative positivity, «per prime plus a constant», of extended 𝔖
type. It does not see the near-coincidences. Moreover it contains no `Λ`. Under `cΛ` the signed side does not change. Under
deletion of `p^k` a row and column of a `⪰ 0` matrix are removed. Under Beurling the same Smith identity holds
in the free semigroup (ARGUED: requires unique factorization of the system). Then Lemma T of `ROUND_013_C`
excludes the sign coming from there (`RULES_AVOID` S2: «a step that uses only divisors does not fail under Beurling»).

- The GCD sums of Gál, Bondarenko–Seip and Aistleitner–Berkes–Seip type are **upper bounds** for forms
  `Σ c_m c_n gcd(m,n)^{2σ}/(mn)^σ`. They provide no lower sign for a form with negative weight (ARGUED; not
  reread in primary sources). Their role in the corpus is that of Franel in `R184_010`.
- The Nyman–Báez-Duarte Gram of `{θ/n}`: its entries carry gcd/lcm, but the criterion is a distance to a
  subspace, i.e. a reformulation. It is already in the index: NG-B4, CIR-3 (circular), NG-A5, CIR-6. Not
  retried.

## 4. Observation on the round-6 threshold (NUMERICAL/ARGUED, not rederived)

The DIR split reaches the ceiling up to `T ≈ 0.69` and fails between `0.695` and `0.70` (`ROUND_006` §§8.1, 10.2).
On the other hand, the contact `log 4` enters the form exactly when `2T > log 4`, i.e. for `T > log 2 = 0.6931`.
Hence the first failure of the **per-prime** split appears when the piece of the prime 2 starts to carry two
contacts (`log 2` and `log 4`). It does not appear in a new configuration between 2 and 3. `ROUND_006` §10.4 and the
band analysis (§9.3, band `≳ 1.2` with `θ_2 = 0`, contact `log 4`) are compatible with this, but do not
state it. Until proved, the reading «the failure requires coupling 2 with 3» of the assignment is a hypothesis and not a
fact of round 6. The obstructing pair could be an internal 2-adic interaction (`log 2` versus `log 4`)
mediated by the split with 3. There is no proof in either direction.

## 5. Verdict

- (i) Repetition of G2_B8_R5 Observation 4.3 and §5, and of `ROUND_006` §10.2 / O3. The block hierarchy is
  monotone and its exact level is the form (Proposition 1, PROVED given Theorem D). The failure is not a quantum
  marginal problem (Proposition 2, ARGUED). Selection NO-GO.
- (ii) GCD/Smith positivity splits by primes plus a rank one on prime powers (Lemma 2,
  PROVED). It is blind to the three controls (ARGUED for Beurling). Nyman/Báez-Duarte are in the index. Selection
  NO-GO.
- Global sign of `a_T`: OPEN. I have no defensible new idea within this assignment.
- Next explicit operation, the cheapest: decide whether the DIR threshold `0.695–0.70` is the entry of `v_4`.
  For that, redo the `transfer` mode of round 6 at `T = 0.70, 0.72` with the term of `4` removed (deletion
  control) and with the term of `4` assigned to a third piece of its own. If without `v_4` the per-prime split
  2 | 3 reaches the ceiling again, the obstacle is intra-prime (powers), not a 2–3 coupling, and the residue
  «Hadamard coupling distinct primes» loses its numerical support.
