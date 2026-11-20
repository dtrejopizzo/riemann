# Round 14, A — linearizing the ratio channel: independence of the primes, polarization and transport from the product channel

Notation of the common brief and of `ROUND_013_C.md`. For a real weight `w = (w_n)` write `A_w(ξ) = Σ w_n n^{−1/2} n^{iξ}`,
`ĝ = |F̂|⁴ ≥ 0`, `Q(w) = ∫ĝ|A_w|²` (ratio channel, coefficient `w_a w_b/√(ab)` at the delay `log(a/b)`),
`P(w) = ∫ĝ Re A_w²` (product channel). Checks `𝒞 = {2Λ, Λ with a prime power deleted, Beurling}`.

**Result.** No candidate passes the gate. Three class lemmas are proved: the linearization always exists and is
polarization, whose remainder is blind to the weight or whose affine part is circular (Lemma P). The independence of the primes,
by unique factorization, prevents a sum of translations with blind coefficients from taking the product channel to the
ratio channel (Lemma U). The ratio channel is not obtained as the product channel of another object with a Dirichlet
identity that remains exact (Lemma Q). (ii) and (iii) reduce to R161_034/035 and to I2/I5. No new operation
with a written object remains.

Primary-source reading: RULES_AVOID §§I (I2, I5), Q (R7-c), R (R1, R2), S–W; ROUND_013_B §§0–1; ROUND_013_C §§0–1;
ROUND_010_A (through RULES_AVOID T2). For phases 106, 161 and 170 the reading is that of the per-file annexes
`ANNEX_161_FILES_1–3.md` and `ANNEX_170_FILES_3.md`, which contain R170_841, 851, 854, 856 and 860–861, plus the index
`ROUTES-TRIED-INDEX/README.md` (INV_E, INV_F, INV_I, INV_J, BB_001). This reading is indirect, and R161_034/035 and 106_109
were not reread in full.

## 0. Four-point filter

1. **Closest antecedent.** ROUND_013 (RULES_AVOID W3): the quadratic term lives in the ratio channel, and
   there `Λ∗1 = log` does not act. R161_034 and RULES_AVOID Q3 (R7-c): the ratio channel does not see arithmetic and the
   product channel has no sign. RULES_AVOID R1: the product→ratio boundary concomitant is closed (R161_035,
   057–065). I2: `γ = Λ log − Λ∗Λ` collides with Selberg (R170_851). I5: `Σ(Λ(n)/√n)‖F − U_nF‖²` gives a divergent
   constant, and completing the square `D*G⁻¹D` is pure congruence (R170_860–861). INV_J_001 (index): the
   additive correlations `Λ(n)Λ(n+h)`, the large sieve and pair correlation are closed by J3 (H_sparse).
2. **New claim.** There is no new object. What is new are three class statements (Lemmas P, U and Q), which say
   why the ratio channel admits no exact linearization with content.
3. **Why it would avoid the difficulty.** It does not avoid it, it localizes it. The observation of the brief (independence of the
   primes) is used, but **against** transport: it is precisely what prevents the cancellation of the spurious
   terms (Lemma U).
4. **Global link.** None. In the only class where the identity exists (Lemma P, (a)), its existence is equivalent to
   `a_T ≥ 0`.

The gate is not passed. The rest of the memo proves the class closures, as point 3 of the brief asks.

## 1. Lemma P (polarization): the linearization always exists and has no content

**Lemma P.** Let `u_w` be affine in `w` and let `Q(w) = ‖L w‖²` be its quadratic part, with `L` linear.
(a) For every fixed weight `B`, `Q(w) = 2⟨Lw, LB⟩ − ‖LB‖² + ‖L(w − B)‖²` holds for **every** `w`. Hence «linear in
    the weight + remainder ≥ 0» always exists: the remainder is `≥ 0` for every weight of `𝒞` (blind) and vanishes only at `w = B`.
(b) If `R(w)` is a manifestly nonnegative remainder, i.e. `R(w) = ‖Vw + v_0‖²` with `V`, `v_0` independent of
    `w`, and `Q − R` is affine, then `V*V = L*L`, hence `V = UL` with `U` a partial isometry on `Ran L`, and `R ≥ 0`
    holds for every weight. The remainder is blind (patterns B3/B9).
(c) If `u_0` may contain the arithmetic function `Λ` as a fixed datum (i.e. `B = Λ`), an identity
    `a_T(F) = ‖u_0(F) + u_Λ(F)‖²` exists if and only if `a_T ≥ 0` on `P_T`: it suffices to take `u_0 = a_T^{1/2}F − u_Λ`.
    It is J3 (circular).

*Proof.* (a) is the expansion of the square. (b): equate the quadratic parts and apply the Douglas
factorization (RULES_AVOID W2). (c): one direction is immediate and the other is the square root of a positive operator. ∎
PROVED.

**Consequence.** The distinction «weight / no weight» is formal as long as `u_0` can encode values of `Λ`. Under each
check of `𝒞` what breaks in (a) is the **equality** with the form, not the sign of the remainder: the remainder remains
`‖L(w − Λ)‖² ≥ 0`. By rule R3-i, this is not a reason for the sign. For `c = 2`, moreover, W1 shows that breaking
at `c ≠ 1` has no probative value.

## 2. Lemma U (independence of the primes against product→ratio transport)

Class `𝒯`: operators on measures on the delay axis of the form `𝒮 = Σ_j γ_j τ_{β_j} J^{ε_j}`, with
`ε_j ∈ {0,1}`, real **weight-free** coefficients `γ_j` and shifts `β_j` (they do not depend on `w`), the family
possibly infinite, applied to the product measure `μ_×(w) = Σ_N (w∗w)(N) N^{−1/2} δ_{log N}`. One requires
`𝒮μ_×(Λ) = μ_÷^{off}(Λ) + (linear in Λ)`, with `μ_÷^{off} = Σ_{a≠b, (a,b)=1} Λ(a)Λ(b)(ab)^{−1/2} δ_{log(a/b)}`.

**Lemma U.** No `𝒮 ∈ 𝒯` achieves this. Let `N = pq` with `p ≠ q` primes. If `𝒮` takes the mass of `log(pq)` to
`±log(p/q)`, then there exist `j` with `β_j = −2 log p` or `β_j = −2 log q` (for `ε_j = 0`; with `J` it is symmetric).
Those same `j` take the mass `(Λ∗Λ)(p'q)` to `log(p'q/p²)` for every prime `p' ≠ p, q`. By unique factorization,
`p'q/p²` is a coprime ratio `a/b` with `b = p²` and `a = p'q`, composite with two distinct prime factors, so
that `Λ(a) = 0` and the ratio coefficient at that point vanishes. Moreover no other pair `(N', j')` lands at the
same point with mass that cancels it: the product mass of `Λ` lives only on `N'` with at most two prime factors,
and `N' e^{β_{j'}} = p'q/p²` with `β_{j'}` another shift of the same form `±2 log r`, or with another `β`, fixes `N'`
by unique factorization unless `j' = j`. For the spurious term to be «linear in Λ» one would need
`(Λ∗Λ)(p'q) = 2 log p' log q` to be linear in `Λ` with weight-free coefficients for all `p'`, which is again
the original problem. ∎
PROVED for `𝒯` with shifts of the form `±2 log r` and for arbitrary finite combinations (a finite number
of `β_j` does not reach the infinitely many delays `log(p/q)`). ARGUED for infinite families with arbitrary `β_j`: the
summability control remains to be written.

**Reading.** The observation of the brief is correct (the map `(a,b) ↦ a/b` is injective on coprime
pairs, and `ab ↦ {a,b}` is too for squarefree `ab` with two factors). But the map
`log(pq) ↦ log(p/q)` is not affine in the delay, and translations only realize affine maps. Independence
of the primes then prevents the spurious terms from cancelling. Multiplying by a window does not move the support.
`𝓕` sends point masses to almost periodic functions: to return to the delay axis one must apply `𝓕` again, and
the composition is affine or a convolution. The inclusion of `𝓕` and of multiplication by a window in the class is ARGUED.

**Relation with R1.** R161_035 and 057–065 close the **boundary concomitant** (`⟨g,[P,S]w⟩`, without sign). Lemma U
covers a disjoint class, that of support transports by involutions and translations. The question of the brief
about `J` and `𝓕` lies within `𝒯` (ARGUED for `𝓕`), and is NO-GO.

## 3. Lemma Q (`TT*` duality and extension to ℚ_{>0}): the ratio channel is not the product channel of another exact object

(a) For a single Dirichlet polynomial, `L*L` and `LL*` are both multiplication by `|A|²`, because the operator is
    normal. The duality `‖T‖ = ‖T*‖` of the large sieve exchanges frequencies with sampling points, but the kernel
    `TT*` is `Σ w_n² n^{i(t−t')}`, diagonal in `n`. Hence no product channel appears. PROVED, and
    elementary. Large sieve bounds only give upper bounds (INV_J J2).
(b) If one extends the weight to ℚ_{>0} by `w(1/n) = w(n)`, with `B = A + Ā`, one gets `B² = A² + 2|A|² + Ā²`, so
    that the ratio channel is `½(∫ĝ B² − 2∫ĝ Re A²)`. The Dirichlet identities (`Λ∗1 = log`, Selberg
    `Λ log + Λ∗Λ = μ∗log²`) act in the Dirichlet ring over ℕ. In the group algebra of ℚ_{>0} there is no
    analogue of `1`, because `1∗1` diverges at every point. In particular, `(Λ_ℚ ∗ Λ_ℚ)(1) = 2Σ Λ(n)²/n` is the divergent
    diagonal of W3. PROVED for the divergence. That no other exact identity exists in the group algebra is ARGUED.
(c) Renormalization of the diagonal. Subtracting `Σ_{n≤X}Λ(n)²/n` is exactly the «squares − constant» of I5
    (R170_201/301, falsifier `a_2 = 100`). Repetition.

## 4. Candidates of the brief, one by one

| Cand. | Verdict | Reason |
|---|---|---|
| (i) injectivity + additive lattice | selection NO-GO | Lemma U. The conditions `a ≡ b`, `a − b = h` introduce `Λ(n)Λ(n+h)`, closed by INV_J J3 (H_sparse) |
| (ii) `|−ζ'/ζ|²` versus `(ζ'/ζ)'`, Selberg transported by `J`/`𝓕` | NO-GO in `𝒯` | `(ζ'/ζ)² − (ζ'/ζ)'` belongs to the product channel (`Λ∗Λ`, `Λ log`); its transport is Lemma U; Selberg without sign, I2 (R170_851) |
| (iii) `TT*`, large sieve, duality | NO-GO | Lemma Q(a); with extension to ℚ_{>0}, Lemma Q(b) |
| (iv) polarization / completed square | tautological | Lemma P; R170_854 §6.3, 860–861 |

## 5. Verdict

- No candidate passes the four-point gate. Class NO-GO: Lemma P (PROVED), Lemma U (PROVED in the finite class
  and in that of shifts `±2 log r`, ARGUED in general and with `𝓕`), Lemma Q (PROVED in (a) and in the
  divergence of (b)).
- Independence of the primes does not linearize the ratio channel; it works against any transport from
  the product channel.
- The only explicit operation not covered: a transport **non-affine in the delay**, for example a
  reindexing `log N ↦ log(a/b)` that depends on the factorization of `N`. As an operator on `F` it is not in the
  class of translations, and no weight-blind realization is known. No written object: OPEN. Before any
  attempt it must be cross-checked with D («change (m,n) → (m+n,m−n)», POWER_GRAM_SLICES §17), which is its additive relative.

## 6. What must be rederived for independent verification

1. Lemma P(b): Douglas, and that `R` be affine-quadratic in `w`.
2. Lemma U: the non-cancellation of `log(p'q/p²)` by unique factorization. Check the case `p' = q`
   (`N = q²`, `(Λ∗Λ)(q²) = log² q`, which falls at `log(q²/p²)`; there too the ratio coefficient is
   `Λ(q²)Λ(p²) ≠ 0`, and one must verify that this single point does not rescue the class: the coefficient is fixed by a
   single `j` and is not repeated for all `p'`).
3. The extension of Lemma U to `𝓕` and to infinite families: it is ARGUED.
