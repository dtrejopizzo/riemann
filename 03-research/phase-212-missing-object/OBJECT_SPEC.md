# Phase 212 — Specification of the object to be built

Merges P46 prob:region and prop:spec, P48 req:spec (R1–R12), GRID §7 (S1–S12), CW §3.2 ((α)–(μ)) and
211/OBJECT_SPEC_001 (R1–R5), without repetition. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}.

## 1. Shape of the object

Scope: this specification defines the identity programme (G), not a proven necessity
for every possible proof of global positivity. The asymptotic route of P46 thm:wit-Tc(iv) and
ROUND_022_B, Lemma 1, remains admissible with its full quantifiers; see RULES_AVOID B2.
That already-recorded route is not presented as a new construction.

An object 𝒪 = (ℋ_T, V_T, ρ_T)_{T>0} with:

- ℋ_T an explicit Hilbert space and V_T : P_T ∩ 𝒟_T → ℋ_T linear;
- ρ_T a form on P_T that is **manifestly** non-negative (a written sum of squares, or a written positive
  measure);
- the exact identity **(G)** a_T(F) = ‖V_T F‖² + ρ_T(F) for every F ∈ P_T ∩ 𝒟_T and every T.

The variant by exact reduction is admitted: (G) on the finite carrier of (L2), on the matrix 𝔸_M
of (S), on the function 𝖡 of a profile, or on the power ladder, provided the reduction
used is one of the PROVED ones (README §3).

## 2. Clauses

O1. **Exactness.** (G) is an equality. No term is bounded in absolute value, by a norm, by
    lossy Cauchy–Schwarz, or by an o(·) remainder.
O2. **Exact dependence on Λ, with the nonlinearity in the coupling.** V_T uses the exact values
    Λ(n), n < N. The form is affine in the comb, so the degree in the weights is invisible to
    it, and every polynomial relation on Λ in [2,N) follows from the linear atoms
    Σ_{d|n}Λ(d) = log n (`ROUND_001_D.md` Lemma A; the degree-two relation is the Leibniz rule
    on Λ∗1 = log, `ROUND_001_A.md` Lemma B). The nonlinearity that decides the sign must lie in
    how V_T acts on F (the square ‖V_T F‖²), not in products of weights. A linear use in which F
    enters only through its autocorrelation is a certificate, whose content is λ^prim (P46 cor:shape (a)).
O3. **The three inputs together in one line.** The Euler product over all primes, the
    functional equation with Γ(s/2) at conductor 1, and integrality (coefficients b ≡ 1 of the series
    over ℕ, or Σ_{d|n}Λ(d) = log n) enter the proof of (G) in one and the same step, not chained
    (P48 req:spec R2–R3; P46 prop:shape-inputs).
O4. **Breaking, not loss of margin.** For each falsifier of `RULES_AVOID.md` §E one points to the line
    of the proof of (G) that ceases to be true. In particular (G) is false for cΛ with c ≠ 1 however
    small |c − 1| is, and for a_P with P > N (which agrees with Λ in almost every class property).
    An isolated formal break is not enough to propose a candidate: one must prove the full
    identity and the non-negativity of its right-hand side for Λ. Once that is proved, the step that fails
    on a falsifier may be the representation identity itself; it is not necessary that the auxiliary
    norm or remainder also lose positivity. `REVIEW_003.md` R3-i describes the automatic algebraic
    break, but does not exclude an exact and specific positive representation of Λ.
    Lemma T of `ROUND_013_C.md` only transfers the conclusion to a falsifier if the
    identification with the form and all the hypotheses giving the sign survive.
O5. **Uniformity in T.** The construction is a single one, valid for all T; not a family of
    certificates whose dimension or precision is recomputed per window (W-fam; P46 cor:shape (b)).
O6. **Sees the near-coincidences.** ‖V_T F‖² does not vanish identically on the vectors that see
    m ≈ kn, m ≠ kn; that is where the sign lies (P46 prop:nearfree, rem:bar-arith).
O7. **Uses the fluctuation, not the density** (P46 thm:ceiling, prob:region (7)); **uses the positive part
    of the symbol on all of ℝ together with the negative set** (prob:region (8)).
O8. **Is not** a functional of the minimizer, a bounded functional of the weights, a local criterion, a
    determinant or moment of the pencil, nor a pure arithmetic sum of squares for T ≥ ½log3
    (P48 req:spec R7, R9, R10).
O9. **Couples Λ(n), n < N, with the functional equation by a route other than the common factor
    ζ(½+iτ)** (P46 prop:spec (5), OPEN: no known object). The strip identities satisfy
    the letter of this clause but are generic in the comb: they do not suffice alone.
O10. **Crosses the logarithmic derivative.** The positivities of the Dirichlet series that pass to its
     logarithmic derivative are only the infinitely divisible ones, a homogeneous cone that cΛ preserves
     (P46 prop:spec (6)); the object must work on the Λ side or cross by a non-homogeneous mechanism.
     The first exact non-homogeneous relation in (1, Λ) has degree two:
     Λ·log + Λ∗Λ = μ∗log² (P46 rem:spec-scope).

## 3. Two proved restrictions on (G) (round 1; `REVIEW_001_LC.md`)

Neither contributes a sign; they delimit where not to search.

R-comp (PROVED relative to three cited classical theorems; `ROUND_001_L.md`, Theorem 3.1, Cor. 4.1).
On the power ladder, if the target kernel minus ε times a kernel [M₀(u)+M₀(v)]/(u+v), with
M₀ positive-real on Re u > 0 and real on (0,∞), is positive semidefinite at all sizes, then
M₀ has no linear term and its boundary measure is dominated by (1/ε) times that of M, which under that
hypothesis is purely atomic. Atomicity is a conclusion under the hypothesis, not an
unconditional fact. The exclusion is not effective (it gives no block or vector). It does not restrict spaces ℋ_T that do not
come from a comparator of this class: outside it there is no rigidity.

R-cont (PROVED relative to 211 GRAM_SLICES §18.2 and to the holomorphy of z ↦ P_z; `ROUND_001_C.md`,
Lemma 1, Theorem R). In a single identity A_0 = Σ squares + non-negative remainder on the carrier of
integer scales, each square is continuous in the graph norm and its coefficients are integer
values of a holomorphic function of polynomial growth on a half-plane. No nonzero square
vanishes on a set of nodes or modes with divergent reciprocal sum, nor is it the twist of a
continuous functional by a function with a divergent level set of divergent complement
(characters, non-constant Ramanujan sums, μ, μ², Λ, indicators of residues, multiples or fixed
gcd). Hence V_T uses global observables, not finitely supported or arithmetically selected at
the node. Still admitted: continuous squares with arithmetic index or weights in the dilation,
twists without a divergent level set, and per-window objects or objects on 𝔸_M.

## 4. What a candidate delivers before construction

(1) closest antecedent, with file and section; (2) the object: ℋ_T, V_T, ρ_T written, or the part
still to be written identified; (3) why the change avoids the concrete difficulty of the antecedent;
(4) the identity connecting it with (G) on the full carrier; (5) for cΛ and a_P, the line that
breaks. A candidate that cannot write (2) and (5) is not ready for construction.

## 5. Clauses added by rounds 6–17 (master index `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, III.0 §2; the full list of restrictions from the whole corpus is in its Part II)

O11. **The three controls at once.** The exact relation giving the sign fails simultaneously at `cΛ`
     (`c = 2`), at the deletion of a prime power, and at a Beurling-type weight. A sign obtained from
     blind squares plus relations valid in any of the three proves a false statement (Lemma T,
     `ROUND_013_C`; PROVED in the declared class).
O12. **Arch and the weight from the same object.** Against `c = 2`, the archimedean part and the weight come from the
     same object in the same step: an object producing the weight `2Λ` with all exact relations
     (ring `ℤ×ℤ`) also produces doubled Arch (`ROUND_016_B`). Against deletion, integrality is used;
     against Beurling, the equal spacing of the integers. Sharpens O3.
O13. **The vector has its own formula.** In `a_T = ‖V_T F‖² + ρ_T`, `V_T` is written without inverting or
     factoring the form. If `V_T` may contain `Λ` arbitrarily, the identity exists if and only if
     `a_T ≥ 0` (`ROUND_014_A` Lemma P(c)); if `V_T` is affine in the weight, the remainder is blind (polarization).
O14. **A Gram or Schur block needs a construction and an identification independent of the sought sign.**
     It is not enough to manufacture a block whose positivity presupposes a_T≥0, nor to exhibit a positive Gram without
     proving its full identity with a_T. The lemmas of `ROUND_013_B` do not exclude an explicit Gram
     with its own formula and a specific arithmetic identification proved for Λ. The Schur
     equivalence by itself is not a proof of impossibility. The exclusion of a sum of
     per-prime pieces each with a sign is kept (false for `Λ`
     past `T ≈ 0.697` in the two-position class, NUMERICAL; per-prime exponential factors blind,
     `ROUND_014_B`).
O15. **The reason is not "the identity breaks away from `c = 1`".** The set of `c` with positivity
     contains a neighbourhood of 1 of the size of the margin (`ROUND_013_A`); the object has to explain a
     coincidence of that order between Arch and the prime part, not a formal equality.
O16. **Couples distinct primes through the additive structure.** Whatever treats each prime
     separately, is linear in `F` and affine in the lag, is closed or blind (collective reading of
     rounds 13–16; sharpens O6).
O17. **An auxiliary source of positivity does not replace its identification with the full form.**
     Lemma K of `ROUND_013_C` proves positivity of the Hessians of the two classes declared there
     when their measures or weights are positive; it does not exclude a specific arithmetic identity that
     identifies them with a_T for Λ and fails for a falsifier. Hence positive measures and positive weights
     are not universally forbidden as a source of the sign. One is required to build and prove
     the exact link, with the global scope and own formula of the other clauses. The exclusions
     concerning generator rates (`ROUND_016_A`) and archimedean complete monotonicity (`ROUND_016_C`)
     keep the classes and hypotheses of their statements; they are not extended to every positive representation.

## 6. Terrain without an object

The current list is in the master index `05-meta-and-planning/ROUTES-MASTER-INDEX.md` (Part I, sections B and B′) and in sections X–AB of `RULES_AVOID.md`.
