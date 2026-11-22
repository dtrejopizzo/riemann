# Round 15, memo A — Non-affine delay transport: cross-check and closure by repetition

Brief: check whether a delay transport that is not affine in the delay (a reindexing of contacts that depends on the
factorization) takes the product channel (delays `log(pq)`, where `Λ·log + Λ∗Λ = μ∗log²` lives) to the ratio
channel (delays `log(p/q)`, where `‖LF‖²` lives). Three realizations were requested: (i) additive reindexing `(k,h)`,
`m − kn = h`; (ii) Mellin multipliers composed with truncation and with `𝓕`; (iii) Ramanujan sums,
large sieve and Selberg's Λ² sieve.

Primary-source reading: ROUND_014_A §§0–3 (Lemmas P, U, Q); RULES_AVOID §L (L2, L4) and lines 37, 57 and 84–89;
`phase-188-closing-D/L2_BUILD_030_NEAR_AS_SHIFTED_CONVOLUTION.md` §§1–2; `N_BUILD_003_LAG_RESTRICTED_SIEVE_NOGO.md`
(cross-check and Theorem 1); `phase-167-witness-weighted-sieve/README.md` and `R167_103` §0;
ROUTES-TRIED-INDEX/README, entries INV_C_001, INV_H_001 and SPEC_SIGN_OBJECT_008; index of
`POWER_GRAM_SLICES_OBSTRUCTION.md` §§17.1–17.2. I did not reread R162_1102 or phase 200 in full, so that part of the
cross-check is indirect (through the index).

## 0. Four-point filter

1. **Closest antecedent, one per realization.**
   - (i) `L2_BUILD_030` §1(c) already writes the near term exactly as a sum over additive shifts `h`,
     `Σ_{m−kn=h} s_m s_k v_n c₀(log(m/(kn)))`, with `c₀(−log(1−h/m))`. Moreover, §2 identifies its sign structure. The
     reindexing by `(k,h)` instead of `n` is that same formula. The «Farey/coprime» variant of the fibre mass
     on `log ℚ` is closed in INV_C_001 («no information for the sign», residue CLOSED). The selection
     `(m,n) → (m+n, m−n)` is rejected in the project rules and in GRAM §§17.1–17.2.
   - (ii) ROUND_014_A, Lemma U and its relation with R1. Multipliers that are functions of the dilation generator
     commute with the translations in `log n`. Composed with `J`, `𝓕` and truncation they give operators of the class
     `𝒯` (ARGUED for `𝓕` in 014_A) or the boundary concomitant `⟨g,[P,S]w⟩` (R161_035, 057–065: without sign).
   - (iii) Ramanujan/`c_q`: INV_H_001, class `𝒞_H` NO-GO («finite Ramanujan = regrouped Möbius», with the explicit
     indication «do not retry Ramanujan … as an identity»). Large sieve: SPEC_SIGN_OBJECT_008 V3 (= R162_1102, Thm O/O′),
     which only gives an upper bound and holds for every comb. To this one adds ROUND_014_A, Lemma Q(a): `TT*` is diagonal in `n`.
     Selberg/Barban–Vehov/GPY/`Λ_R` weights: RULES_AVOID L2 (phase 200 Q1–Q3, R162_1003 §4). Sieve majorants
     restricted to delays: N_BUILD_003. Witness-weighted sieve: phase 167, Theorem B′ and Theorem S (sieves
     valid in discrete Beurling systems).
2. **New object.** I found none. The three realizations coincide, up to notation, with objects already
   written in the corpus.
3. **Why it would avoid the difficulty.** Does not apply. The only thing not written literally is an observation about
   the Λ² sieve (§1), and that observation is another closure, not a route.
4. **Global link.** None.

**The idea is a repetition and stops here.** I did no derivations, computations or certificates.

## 1. Why the Selberg square does not connect (class observation)

**Class `𝒮_Λ²`.** These are the expressions `Σ_n x_n Q_n(F, λ)` in which `Q_n ≥ 0` is a square or a sum of squares
whose coefficients do not depend on `Λ` (for example `Q_n = (Σ_{d|n} λ_d)²·|ψ_n(F)|²`) and `x_n` is affine in `Λ` with
`x_n ≥ 0` when `Λ ≥ 0`.

**Observation.** No certificate of the type «`a_T(F) = Λ-free Arch part − Σ_n x_n Q_n + (remainder ≥ 0)`» with terms
from `𝒮_Λ²` uses a relation that fails under the three checks at once. Hence, by Lemma T (ROUND_013_C), it
cannot certify `a_T ≥ 0`.

*Proof.* The nonnegativity of `Σ x_n Q_n` uses only `x_n ≥ 0`, and this holds for `cΛ` with `c = 2`, for `Λ` with a
prime power removed and for a nonnegative Beurling weight. The square `(Σ_{d|n}λ_d)²` does not see `Λ`: its
coefficients are the `λ_d`, fixed in advance. The only thing the Selberg square «knows» about the primes is that
`Σ_{d|p} λ_d = λ_1 = 1` for `p > D`, and that is a property of the support of `λ`, valid for any sequence
`x_n ≥ 0` supported on integers without small factors. The arithmetic information of the sieve comes from evaluating
`Σ_n x_n (Σ_{d|n} λ_d)²` with `x_n ≡ 1`, through the regularity `|r_d| ≤ 1` of the count of multiples in intervals
(R167_103 §0, item 1). That regularity transfers to discrete Beurling systems (phase 167, Theorem S), so
it does not fail under the third check either. ∎

**Label.** PROVED as a direct consequence of Lemma T and Theorem S, in the declared class. It is not a statement
about sieves nonlinear in `Λ`. A sieve whose weights `λ_d` depend on the exact values of `Λ` is not covered,
but that case falls into RULES_AVOID L2/L4 (truncated Möbius, split of the symbol).

**Answer to the question of the brief.** The Selberg square is nonlinear in the sieve weights, not in `Λ`.
The nonlinearity required by OBJECT_SPEC is in the exact values of `Λ`. What the square contributes about primes is a
Λ-free upper bound of the type `Σ_{p≤x} 1 ≤ (2+o(1))x/log x`, and that bound holds for `cΛ` with `c ≤ 2` and for Beurling.
It belongs to the class `C_BT` of Paper 46 (cor:void, thm:finmod), which is closed by deletion (N_BUILD_003, cross-check).
I say nothing about parity: I have no proved statement of that kind within this class, and I do not use one.

## 2. Search for a different nearby idea

I examined two more candidates:
- A kernel on the lattice `(k,h)` whose dependence on `h` is not smooth, for example with weights depending on
  `gcd(h,k)`.
- Cutting the shifted sums `Σ_{m−kn=h} Λ(n)` by classes of `h`.

Both are functions of `h` multiplied onto the formula of `L2_BUILD_030` §1(c). They are linear in `Λ`, and their
arithmetic is deferred by that memo to track (N), which INV_J_001 closes in J2: Gram/Bochner positivity is generic
in the comb. Neither contributes a sign operation. I have no different defensible idea to propose within this
brief.

## 3. For independent verification

- Rederive §1. The delicate point is whether Theorem S (phase 167) covers the positivity used. It suffices that
  only `x_n ≥ 0` be used, and that is immediate.
- Confirm that `L2_BUILD_030` §1(c) coincides with realization (i), with `h = m − kn` and delay `−log(1 − h/m)`.

**Next explicit operation (OPEN, not built).** One would need an identity in which the weights of the square
`λ_d` are defined by the values of `Λ` themselves, for example `λ_d` equal to the solution of an extremal problem whose
datum is `Λ` restricted to the window, so that the square is nonlinear in `Λ`. Before building anything it must be
cross-checked against RULES_AVOID L2/L4 and against ROUND_014_A, Lemma P(b). If `λ` depends on `Λ` only through an affine
quotient, the identity falls again into the polarization of Lemma P.
