# SPEC_SIGN_OBJECT_007 — Round 17B: the immersion channel (log ℚ^× ⊂ ℝ versus ℤ ⊂ ℝ)

Phase 200 ("sign object"), synthesizer. Pure mathematics; labels PROVED / CITED / CONDITIONAL /
ARGUED / OPEN / NO-GO. Phase-201 rule: each candidate
declares its Λ channel and the falsifier that kills it.

## Summary (≤300 words)

**(A)** The immersion channel of C-MvN is formalized as three properties of ν_Λ = Σ Λ(n)n^{−½}δ_{log n}: (I) the support
generates a free semigroup, (II) the generators {log p} are ℚ-independent, (III) a separation measure. In the
window [−2T, 2T] all diophantine information is **elementary**: positions are log n with n ≤ e^{2T}, separation
is |log m − log n| ≥ 1/max(m,n) ≥ e^{−2T}, and Baker adds nothing at finite height (index l.38, NG-B7). Lemma A.1
(PROVED): every functional of the positions of ν_Λ in the window is a function of the finite set of integers ≤ e^{2T} and of
their factorizations, i.e. of the def:PD data. **Decision: immersion channel ⊂ 𝒦_200** (quotient coordinates
N′/N, R-K1, R-Q2).

**(B)** For a_P, linearity gives 𝔞^{a_P} = 𝔞^ζ + Σ_{p∈P} 𝔠_p on P_T (Lemma B.1, PROVED). Each single-prime comb 𝔠_p
is indefinite on P_T (Lemma B.2, PROVED). At the prop:shape-eulerdel witness with T ≤ ½log 15, Σ_{p∈P}𝔠_p(g) <
−𝔞^ζ(g) ≤ 0 (Cor. B.3, CONDITIONAL on Mori's certificate). Positivity is a collective balance. But (I)+(II)+Poisson
also hold for a_P, and (I)+(II) hold for the Lemma E falsifier. The only property of the immersion that separates the
battery is **completeness** ⟨supp ν⟩ = ℕ, i.e. that the two embeddings coincide. It is an equality between data
(C-data, branch 5). The form with comb log n·n^{−½} is the multiplier −ζ′ (Z_CARRIER_001, l.527), and Λ = μ∗log makes it
Möbius translates within the radical (R-Q2). Nothing new.

**(C)** Three candidates (near-coincidence spectrum, quantitative completeness, second-order Bohr/Kronecker):
all three are NO-GO. Restriction **C-emb** is written.

**(D)** Ranking: no survivor. The useful residue is Lemma B.2 together with Cor. B.3 (collective sign), which
becomes a requirement (F8) for phase 201.

---

## 0. Corpus and index (mandatory)

Grep of `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md`, done in this session:

| key | hits | citation |
|---|---|---|
| "Baker" | l.38 | "Baker / linear forms in logarithms: phases 12, 168 (too weak; NG-B7)" |
| "Diophantine", "linear independence", "ℚ-linear", "equidistribution", "discrepancy", "Erdős–Turán", "almost periodic", "resolution π/T" | 0 literal | concepts covered by Kronecker/solenoid (l.61, 249, 263, 286) and Theorem X (l.536) |
| "Kronecker" | l.61, 249, 263, 286 | "no measure on log ℚ gives 𝔞_T" (INV_C Thm 4); measure concentrated on the Kronecker line ι(ℝ), without Schur factorization (PROVED); "Kronecker minus Haar on the solenoid"; "monoid symmetries do not preserve the Kronecker line; additive/multiplicative frustration" |
| "Weyl" | l.391, 536 | Weil character (INV_D); N2 functionals of g* = Theorem X |
| "Bohr" | l.422 | BARRIER_D1 (Hamburger with sign) |
| "m≈kn", "coincidence" | l.78, 120, 161, 390, 540, 541 | near-coincidence part of [Ξ(log(m/k))] (Paper 47 problem (S)); phase 190, near-coincidence matrix experiment; R11_1_CUTS: "Λ∗1=log, r(p)r(q)=r(pq), support on p^k … are equalities between DATA" |
| "Theorem X", "W-pat" | l.536, l.50 | walls W-lin…W-pat; N2 = Theorem X / restr. 11 |
| "Λ∗1" | l.149, 541 | "the comb only enters via Λ∗1=log linear (W7)" |
| "−ζ′" | l.527 (Z_CARRIER_001) | "Z_log = −ζ′" |
| "sum-product" | l.259 | phase 161, sum-product estimate: closed |
| "Erdős" | l.260 | separator invariant (S⁺) (Erdős 1946), NO-GO 𝒦_δ |
| "Montgomery", "Hardy–Littlewood" | l.64–65, 312, 397 | INV_J (Λ(n)Λ(n+h)), comb-generic; additive correlations of primes closed |
| "R-Q2", "R-K1" | l.511, 517; SPEC_006 l.55–56 | ladders/mollifiers = translates within the radical; Hankel ⇒ quotients N′/N |
| "prop:shape-eulerdel", "origin" | l.542 (R11_2_ORIGIN, Theorem O3) | witnesses of a_P and of Epstein on P_T with A=B=0 |

Phase sources read: XI1_VN_DIM_001 §6 (C-MvN), SPEC_SIGN_OBJECT_006 (table A, Φ200, §C.2 F1–F7), SPEC_005
(battery table: a_P without origin), R11_2_ORIGIN (C-pol), LEDGER_L1/L3 via index (S5, F7, F9).

**New reason stated against the index.** Previous records attack the diophantine structure **as a measure** (Haar
or Kronecker on the solenoid), **as a bound** (Baker), or **as a correlation** (Hardy–Littlewood, Montgomery). This round's question is
different: whether the *compatibility between the two embeddings* (ℤ via Poisson and log ℚ^× via the comb) is a second-order
object. If the answer is no, the restriction must be written. No construction below retries an entry in the index without stating
how it differs.

---

## A. Formalization of the immersion channel

### A.1 Definitions

Let ν = Σ_n a(n) n^{−½} δ_{log n} be a comb measure with a ≥ 0, supported on log 𝒩 for some set 𝒩 ⊂ [1,∞).
We define:

- **(I) Semigroup.** S(ν) := the multiplicative monoid generated by {n : a(n) ≠ 0}. ν is of *Euler type* if
  supp a = {p^k : p ∈ 𝒫_ν, k ≥ 1} for a set 𝒫_ν of "generators" and a(p^k) = log p.
- **(II) Independence.** {log p : p ∈ 𝒫_ν} is ℚ-linearly independent. Equivalent to S(ν) being free over 𝒫_ν.
- **(III) Separation.** δ_X(ν) := min{|log m − log n| : m ≠ n ∈ S(ν), m, n ≤ X}. More generally, the Baker measure is
  β(B) := min{|Σ b_p log p| : 0 ≠ b ∈ ℤ^{𝒫}, |b| ≤ B}.
- **(IV) Additive embedding.** Poisson in the variable u = e^x relates ν to the lattice ℤ ⊂ ℝ via the summation map E
  (Guo, CITED).

### A.2 For ζ, all of this is elementary

**Lemma A.0 (PROVED, elementary).** For ν = ν_Λ:
(i) S(ν_Λ) = ℕ and it is free over 𝒫 (unique factorization).
(ii) For m ≠ n ≤ X one has |log(m/n)| ≥ log(1 + 1/max(m,n)) ≥
1/(2 max(m,n)) ≥ 1/(2X).
(iii) For b ∈ ℤ^𝒫 non-zero, Σ b_p log p = log(m/n) with m = ∏_{b_p>0} p^{b_p} and n = ∏_{b_p<0} p^{−b_p} coprime and
distinct. By (ii), |Σ b_p log p| ≥ 1/(2 max(m,n)).

*Proof.* (ii): if m > n, then m ≥ n + 1, so log(m/n) ≥ log(1 + 1/n) ≥ log(1 + 1/m), and log(1+y) ≥ y/2 for
0 < y ≤ 1. (iii) reduces to (ii). ∎

**Consequence.** Baker gives exp(−C(k) log B) with effective but enormous constants. The trivial bound 1/(2 max(m,n)) is
**better** at every height that matters in the window: there max(m,n) ≤ e^{2T}. This agrees with the index verdict
(l.38: "too weak"). The diophantine structure of log ℕ that the window sees is elementary.

### A.3 Resolution π/T versus separation e^{−2T}

In the window I_T, the tests of P_T resolve scales of order π/T (Theorem X, phase 186). The comb positions within
[0, 2T] are separated by at least ½e^{−2T}, which is much smaller than π/T. Therefore, "near-coincidences"
m ≈ kn at resolution π/T are pairs of integers with |log(m/(kn))| < π/T, with all integers ≤ e^{2T}. It is a finite
list of relations between integers. There is no genuine diophantine approximation: the list is decided by exact arithmetic.

**Lemma A.1 (PROVED).** Let Ψ(T; ν) be a functional that, for each T, depends on ν only through ν|_{[−2T,2T]} and through the
positions and relations (I)–(III) restricted to it. Then Ψ(T; ν_Λ) is a function of the finite set
{(n, factorization of n, Λ(n)) : n ≤ e^{2T}}, which is exactly the family of def:PD data v_n.

*Proof.* The positions are log n with n ≤ e^{2T}. The relations of (I) are m·n = k, those of (II) are the factorizations, and
(III) is a minimum over the same finite list. None of this depends on anything else. ∎

**Decision A.** The immersion channel, restricted to the window, is channel I4 (coordinates) of Φ200. The relations
between positions are multiplicative relations between integer indices. R-K1 already says this ("the sign lives in
quotients N′/N"), and R-Q2 says that quotients, levels, and subcombs are translates within the radical. **Immersion channel ⊂
𝒦_200 (PROVED as a class inclusion, by Lemma A.1 and piece Φ.4).** What remains outside R-Q2/R-K1 is only what
is not a function of positions within the window:
(a) relations with positions outside the window, which is already strategy E of phase 199 (PROOF_L_SHARP_E_001, l.455) and
the exterior datum FF.1;
(b) the *identity* of the generators, i.e. completeness ⟨𝒫_ν⟩ = ℕ, which is dealt with in §B.

### A.4 TV-robustness warning (AUDIT_CONSTRAINTS restr. 1)

Properties (II)–(III) are destroyed by arbitrarily small total-variation perturbations of the positions. That they are not
TV-robust is exactly what BARRIER_EST demands. But Theorem X and W-pat force the first order to be a functional of
h*, so the diophantine property should enter at second order. By Lemma A.1, within the window there is no diophantine
property that is not a list of integer equalities. An integer equality enters the inequality as **data**, not as a variable
(C-data, Theorem C1, l.541). This is why it cannot enter at second order non-trivially. This is the core of restriction
C-emb (§C.4).

---

## B. What ℤ ⊂ ℝ contributes, and what distinguishes a_P from ζ on P_T

### B.1 Poisson does not separate the battery

- Epstein (h > 1): the summation map f ↦ Σ_{λ ∈ Λ_τ∖0} f(Q(λ)u) exists (Poisson over the lattice Λ_τ). By GUO_QUANT
  Prop 1.3, Φ_f ∈ rad for every L with an explicit formula and a summation map. **Poisson ⇒ radical gauge also holds for
  Epstein (PROVED given Guo L4.4).** What Epstein lacks is not Poisson: its positions log Q(λ) do not form a
  semigroup.
- a_P: it has a free semigroup (over 𝒫∖P) and a multiplicative count, but lacks the lattice origin
  (SPEC_005 §4.3). C-pol (Theorem O3, l.542) says the origin does not act on P_T.

So on P_T, neither Poisson nor the origin distinguishes a_P from ζ. The question becomes what distinguishes them *on P_T*.

### B.2 Exact decomposition

a_P(s) := ζ(s)·∏_{p∈P}(1 − p^{−s}). Then −a_P′/a_P = −ζ′/ζ − Σ_{p∈P} Σ_{k≥1} (log p) p^{−ks}, i.e.
Λ_{a_P} = Λ·1[n is not a power of a p ∈ P].

**Lemma B.1 (PROVED, linearity; def:W convention of Paper 47).** Let 𝔞^{L}(g) be the window form with fixed archimedean
term and fixed polar term and the comb subtracted with a minus sign. For g ∈ P_T (A = B = 0), the polar term vanishes
(C-pol), and

  𝔞^{a_P}(g) = 𝔞^ζ(g) + Σ_{p∈P} 𝔠_p(g),  𝔠_p(g) := Σ_{k ≥ 1, k log p ≤ 2T} (log p) p^{−k/2} · 2Re (g ∗ g̃)(k log p).

*Proof.* The comb of a_P is that of ζ minus the combs of the primes in P. Since the comb enters with a minus sign in
the form, removing it adds +𝔠_p. The archimedean term does not change: prop:shape-eulerdel uses the same Γ_ℝ factor, and this
must be verified against the paper's definition (see the risk). ∎

*Normalization risk.* If prop:shape-eulerdel includes, in 𝔞^{a_P}, the "trivial zeros" of (1 − p^{−s}) on Re s = 0
as an additional term, the identity gains an explicit diagonal term per prime. This must be checked against def:W/eq:nuw
before integrating it into Paper 47 (rule).

**Lemma B.2 (PROVED, elementary).** Let p be prime and T > ½ log p + η, η > 0. The Hermitian form g ↦ 𝔠_p(g) is indefinite
on P_T: there exist g_± ∈ P_T with ±𝔠_p(g_±) > 0.

*Proof.* Let φ ≥ 0 be smooth, even, supported on [−ε, ε] with ε < η/4. Take g = aφ(· − x₀) + bφ(· − x₀ − log p) + r, with
r a combination of two bumps at generic, far-apart positions, chosen to impose A = B = 0 (two linear conditions).
For generic positions, no difference between the supports of r and those of the first two bumps equals
k log p, except the intended one. Then (g∗g̃)(log p) = a b̄ ‖φ‖² exactly, and the other k log p with k ≥ 2 do not touch pairs of
supports. So 𝔠_p(g) = 2(log p)p^{−½}Re(a b̄)‖φ‖², whose sign is that of Re(a b̄). The positions fit in the window
because 2T > log p + 4ε + (room for r); if the window is tight, r can be placed on the same line with
generic shifts incommensurable with log p. ∎

**Corollary B.3 (CONDITIONAL on Mori's ½log15 certificate, CITED/verified l. phases 194–198).** Let g* be the negative
witness of prop:shape-eulerdel with T ∈ [0.60, ½ log 15]. Then

  Σ_{p∈P} 𝔠_p(g*) = 𝔞^{a_P}(g*) − 𝔞^ζ(g*) < −𝔞^ζ(g*) ≤ 0.

*Reading.* Restoring the primes in P **lowers** the form below zero. In other words, the primes in P are
necessary for the positivity of ζ at that g*. This is the collective sign: by Lemma B.2, no single prime, alone, contributes
a comb with fixed sign. The positivity of 𝔞^ζ is a balance among indefinite combs, and the full Euler product is
necessary, not just each factor. Beyond ½ log 15, the corollary remains open: it depends on L′♯ (OPEN).

### B.3 Is there a second-order collective property of {log p} that is neither the explicit formula nor the PNT?

Candidates and verdict:

1. **Pair correlations of {log p} at scale 1/X** (Hardy–Littlewood, Montgomery). In the index: INV_J (l.397,
   comb-generic) and the boundary of additive correlations (l.64–65). Within the window, by Lemma A.1, they reduce to the
   finite list of pairs; the asymptotic content is conjectural or on the zero side. **Do not retry.**
2. **Density (PNT).** It is comb-generic: Beurling with PNT satisfies it (Φ.1). **NO-GO.**
3. **The semigroup as a second-order relation: Λ ∗ 1 = log.** Here the *generator* comb ν_Λ, multiplicatively
   convolved with the indicator of the semigroup ℕ, gives the dense comb log n·n^{−½}. For ζ, the position log(pq)
   is occupied in ℕ but has weight Λ(pq) = 0: the comb is the indicator of the generators and their powers.

   **Identity (PROVED, Möbius inversion).** Let ν_log := Σ (log n) n^{−½} δ_{log n}. Then
   ν_Λ = Σ_d μ(d) d^{−½} τ_{log d} ν_log, with τ the translation. Consequently,
   𝔠^Λ(g) = Σ_d μ(d) d^{−½} 𝔠^{log}(g; shifted by log d),
   and within the window the sum has only d ≤ e^{2T}.
   The form with comb ν_log is that of the multiplier −ζ′ (it is not a log-derivative, so it has no explicit formula with
   zeros). It is already recorded: Z_CARRIER_001 (l.527, "Z_log = −ζ′; (★★) = crossed form"). The Möbius identity
   expresses 𝔞^Λ as translates of 𝔞^{log} with weights μ(d), and this is exactly R-Q2 ("translates within the radical").
   No sign appears: the μ(d) change sign and the balance is the same as in B.2.
   **Classification: REF-D / R-Q2. Not new.**
4. **"Interference between negative plateaus of different primes at m ≈ kn"** (LEDGER_L1, S5). By Lemma B.1, this is
   the quadratic-form structure p, q ↦ 𝔠_p + 𝔠_q on P_T. The interference between p and q appears only in the
   cross terms of g∗g̃ at nearby positions log(p^a) and log(q^b), i.e. |a log p − b log q| < π/T. It is a finite
   list (Lemma A.1). It is W-pat / Theorem X (l.50, 536): "new primes must cancel σ on U at resolution π/T".
   **Do not retry.**

**Honest answer to B.** Within the window there is no second-order collective property of {log p} other than (a) the
explicit formula (REF-D), (b) the PNT or another density (comb-generic), (c) a finite list of integer relations (data,
C-data), or (d) correlations (zero side or conjectural). The only global property separating ζ from a_P on P_T is
**which** the generators are, and in particular that there are **all** of them.

---

## C. Three candidates with full filter

Filter: table A from SPEC_006 (C-Guo, C-E′, C-θ, C-τ, C-int, C-hom, C-data, C-pol, R-K1, R-Q2, Φ.1–Φ.8), F1–F7 of §C.2,
C-MvN, and the 201 rule (channel + falsifier).

### C1 — Near-coincidence spectrum at resolution π/T

**Object.** 𝔐_T := the matrix (or graph) of pairs (m, n) in the support of ν with |log m − log n| < π/T and m, n ≤ e^{2T}.
Its spectrum or its number of components is proposed as the sign.
**Λ channel.** Only the positions (support), (I)+(III).
**Index.** l.78 (Paper 47 problem (S)), l.120 (phase 190 R9: near-coincidence matrix experiment).
**Proposed new reason.** Use the *generator support* instead of all of ℕ.
**Filter.**
- C-data: it is a datum without a free variable ⇒ branch 5.
- C-E′: the Lemma E falsifier, ½(Λ_K + Λ_ψ) + Λ_cosh, has support on prime-power norms of rational primes (the ideal
  norms are p or p²). If Λ_cosh > 0 at composites, its support ⊇ ℕ.
- a_P: its support is that of ζ minus the powers of P, a subgraph.

**Falsifier that kills it (PROVED given the certified Lemma E).** For every T, the support of the Lemma E comb contains that of
ζ. Any monotone invariant of the support that certifies ζ certifies the Lemma E form at T ≥ 1.59, where the form is negative
(interval [−0.0599398587, −0.0599398456]). A non-monotone invariant stops being a function of the generator support and
becomes C2.
**Verdict: NO-GO.**

### C2 — Completeness: ⟨𝒫_ν⟩ = ℕ (the two embeddings coincide)

**Object.** The indicator χ(ν) := 1[S(ν) = ℕ and ν is of Euler type with 𝒫_ν = 𝒫]. Equivalent to the multiplicative
semigroup generated by the comb coinciding, as a subset of ℝ via log, with the additive lattice ℕ ⊂ ℤ used by Poisson.
**Λ channel.** (I) + (IV): compatibility between the two embeddings.
**Battery separation (PROVED).** ζ: χ = 1. a_P: S = ℕ with the P parts null ⇒ χ = 0. Generic Beurling: S ≠ ℕ ⇒ 0.
Epstein h > 1: not a semigroup ⇒ 0. DH: not of Euler type ⇒ 0. Lemma E: weights ≠ log p ⇒ 0.
**Filter.**
- C-data (Theorem C1, l.541): "Λ∗1=log, r(p)r(q)=r(pq), support on p^k are equalities between DATA". χ = 1 is
  precisely Λ ∗ 1 = log with 1 = 1_ℕ. It is branch 5 of Φ200: it separates by existence of structure and does not
  enter any inequality with variables.
- C-int (l.71): the same pattern, "PROVED as separation; NO-GO as object".
- SPEC_005: 𝔖 = h(D) − 1 has the same status, "classifier, not engine".
- C-τ / F4: χ is discontinuous in the comb (fine). But it is also discontinuous in T in the worst way, because it does not depend
  on T: it cannot decide *which* T.

**Falsifier.** a_P for T < 0.60: χ(a_P) = 0, and yet 𝔞^{a_P} ≥ 0 in that region (prop:shape-eulerdel only gives a
witness for T ≥ 0.60). A classifier that equals 0 where the form is positive cannot be a necessary condition for
positivity at every T. It can only be a condition "∀T", and that version is D itself (branch 4, identification).
**Verdict: NO-GO as sign object; correct as a classifier** (joins 𝔖 and C-int).

### C3 — Quantitative completeness / second-order Bohr–Kronecker

**Object.** For ν of Euler type, the completeness defect D_T(ν) := Σ_{p ∉ 𝒫_ν, p^k ≤ e^{2T}} 𝔠_p, as a quadratic
form in g. Or, in the Bohr version, the Gram matrix of the frequencies {e^{iξ log p}}_{p ≤ e^{2T}} on the
Bohr compactum / solenoid, at second order.
**Λ channel.** (II) + (IV) quantitative.
**Index.** Kronecker/solenoid l.249, 263 ("Kronecker minus Haar"), l.286 (additive/multiplicative frustration), INV_C
Thm 4 (l.61).
**Proposed new reason.** Measures the *distance to completeness* instead of a measure on the solenoid.
**Filter.**
- By Lemma B.1, 𝔞^{ν} = 𝔞^ζ + D_T(ν) on P_T. Any bound on D_T is linear in the comb (Φ.1: comb-generic), and
  concluding 𝔞^ν ≥ 0 requires 𝔞^ζ ≥ 0 (REF-D). In the other direction, for ν = ν_Λ, D_T = 0 and the object says
  nothing about ζ (branch 4).
- Bohr version: by Kronecker, {ξ log p} is equidistributed on the torus. Bohr averages are Haar averages ⇒ blind
  to the weights (l.263). The "Kronecker minus Haar" variant is already closed.
- C-θ: D_T is affine in the comb ⇒ affine in θ ⇒ branch 1 via C-E′.

**Falsifier.** Lemma E: its defect relative to ζ is a form linear in the comb with negative value at the witness,
same as a_P (Cor. B.3). The object merely rewrites the difference.
**Verdict: NO-GO (Φ.1 + REF-D; Bohr = l.263).**

### C4 — New restriction C-emb

**Restriction C-emb (PROVED by pieces: Lemma A.1 + Lemma B.1 + Theorem C1 + Φ.1 + Lemma E).** Let Ψ be a functional that reads ν
only through the embedding log: S(ν) → ℝ, i.e. through properties (I)–(IV): semigroup, ℚ-independence,
separation or Baker measure, and compatibility with ℤ via Poisson. Then one of these three holds:
(a) Ψ restricted to the window is a function of the finite list {n ≤ e^{2T}} with their factorizations (Lemma A.1) ⇒ a datum of
def:PD ⇒ C-data / branch 5, or else a quotient coordinate ⇒ R-K1/R-Q2;
(b) Ψ is linear in the comb (defect relative to ζ, Lemma B.1) ⇒ Φ.1 comb-generic, or REF-D if it uses 𝔞^ζ ≥ 0;
(c) Ψ depends only on the support ⇒ the Lemma E falsifier kills it (C1).
Moreover, (II) and (III) add nothing that (I) does not already give within the window: Baker is weaker than the trivial
separation 1/(2X) (Lemma A.0).
> **Do not retry:** Baker, irrationality measures of log p, ℚ-linear independence, near-coincidence matrices or
> spectra, completeness ⟨𝒫⟩ = ℕ, nor completeness defects as carriers of the sign. Any proposal for an
> "interaction of the two embeddings" must state which of (a), (b), or (c) it escapes.

**Requirement (F8) for phase 201 (from Lemma B.2 and Cor. B.3).** A sign object must be **non-additive over primes**: it
cannot be written as Σ_p Ψ_p(𝔠_p), with Ψ_p monotone, because each 𝔠_p is indefinite and positivity only appears in the
total. It must act on the total form, not prime by prime. (This is compatible with, and weaker than, the frustration of
l.281: no ±1 gauge makes 𝔸_M ferromagnetic.)

### C5 — Test on Mori, Lemma E, and a_P

| object | Mori (ζ, T ≤ ½log15) | Lemma E (T ≥ 1.59) | a_P (T ∈ [0.60, ½log P]) |
|---|---|---|---|
| C1 near-coinc. | datum of n ≤ 15: gives no bound | support ⊇ ζ ⇒ same verdict ⇒ fails | subgraph; does not explain the witness |
| C2 completeness | χ = 1 | χ = 0 (fine) | χ = 0 also for T < 0.60, where it is positive ⇒ does not decide T |
| C3 defect | D = 0, empty | D = 𝔞^E − 𝔞^ζ: rewriting | D = Σ𝔠_p < −𝔞^ζ (Cor. B.3): rewriting |

### C6 — First exact lemma (to fix and audit)

**Lemma C-emb.1 = Lemma B.1 + Lemma B.2.** First, the identity 𝔞^{a_P} = 𝔞^ζ + Σ_{p∈P}𝔠_p on P_T, checked against
def:W/eq:nuw of Paper 47. Second, the indefiniteness of each 𝔠_p on P_T for T > ½log p. Audit requested: (i) that the
archimedean term of prop:shape-eulerdel is that of ζ; (ii) that the construction of Lemma B.2 respects A = B = 0 in a
tight window (T just above ½ log p). Risk: low on (ii), medium on (i), due to normalization.

---

## D. Ranking

| # | candidate | channel | falsifier | label | residual value |
|---|---|---|---|---|---|
| 1 | Lemma B.1/B.2 + Cor. B.3 (collective sign) | per-prime comb | — (it is a lemma, not an object) | PROVED / CONDITIONAL (Mori) | requirement (F8): non-additivity over primes |
| 2 | C2 completeness | (I)+(IV) | a_P with T < 0.60; C-data | NO-GO object, PROVED classifier | joins 𝔖 and C-int |
| 3 | C3 defect / Bohr | (II)+(IV) | Lemma E; Φ.1; l.263 | NO-GO | none |
| 4 | C1 near-coincidences | (I)+(III) | Lemma E (support ⊇) | NO-GO | none |

**No survivor.** The round closes the immersion channel with restriction C-emb. It leaves a positive requirement
(F8) for phase 201: the object must act on the total balance of indefinite combs, and that balance, within the
window, is a finite list of integer data. Therefore, the object must bring a **free variable** that is not a
positional datum (C-data). The only direction left unrecorded here is the exterior part (positions
> e^{2T}), already attacked in phase 199 (strategy E, l.455). If reopened, it must explain what changes relative to E.1/E.1′.

## Pending notes (for the index / grid; not written here per this round's rule)

- Index: add "SPEC_SIGN_OBJECT_007 (round 17B): immersion channel ⊂ 𝒦_200 (Lemma A.1, PROVED); Baker weaker than
  the trivial separation in the window (Lemma A.0); restriction C-emb (a/b/c); C1/C2/C3 NO-GO; Lemma B.1/B.2 (per-
  prime comb indefinite), Cor. B.3 (CONDITIONAL on Mori); requirement F8 (non-additivity over primes)".
