# R134.000 — Blueprint for the opening of row D (the sign)

Status: `BLUEPRINT` for the
first campaign of row D. Decisions acted on: A.8 and B.7 amendments
accepted (phase 133); rows A, B, C carry `WEIL-STRENGTH-COMPLETE` on the
declared carrier; row D opens with the boxed target of the three papers.
Protocol: construction → audit + review audit → repair rounds →
review decision by grep-verified record. **No label for row D is expected from
this campaign.** Its deliverable is Paper 46 (skeleton and first theorems),
with every statement labelled, and a record of what is refuted.

## 0. The target, and what is already known about its shape

    ROW D'S TARGET: I_∂ ≤ 0 on every primitive radial class Γ_g,
    g ∈ C_c^∞(R), on the colimit D_A^∞ with T_∞ and c = 0 (Paper 45 Cor 9.6a);
    this implies RH by Paper 45 Thm 9.6 (9.10) and Thm 10.4.

Standing negatives (theorems, not opinions): Paper 43 Thm 14.1 (`I_A` on `N_A`
is indefinite with infinite index on both sides; the primitive sector has zero
`I_A`-orthogonal complement; the rulings are a quotient of the test sector);
Paper 44 Thm 8bis.4a (positivity fails on the pure Frobenius form at every
finite chart); Paper 44 Thm 8bis.7 (Dirichlet-polynomial profiles suffice only
under `(H_L)`, `OPEN`); P124.014 (Gate R is not a structural theorem of the
functional-equation class: it fails on `Ξ_a = ξ(s+a)ξ(s−a)`). The review panel
(phase 133, PANEL_3 §5) names what is missing: **a functor to something
carrying a nonnegative invariant, plus a vanishing theorem, turning the
biextension equality (Paper 43 (10.10)) into an inequality.**

## 1. What rows A–C give row D that it did not have before

1. The object is named: the Gram form of the unit-averaged Frobenius family
   `Frob ⋆ Δ^{rad} = Γ^{rad}` is the full Weil kernel (Paper 44 Thm 8bis.1e);
   the sign question is a question about the Gram matrix of that family on
   primitive combinations, in the colimit.
2. The comparison is proved, not cited: `I_∞(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) −
   Σ_ρ Φ_F(ρ)Φ_F(1−ρ)` (Paper 45 Thm 9.6), with `c = 0` the unique compatible
   constant (Cor 9.6a) and the primitive class sufficient (Thm 10.4).
3. The Frobenius family is a commutative inverse semigroup with true unit and
   `Frob_n ⋆ Frob_n^† = Δ^{(n)}` (Paper 44 Thms 3ter.4, 3ter.6, 3ter.7): the
   Frobenii are **partial isometries** of the convolution algebra. In any
   *positive* functional their Gram matrix would be positive semidefinite for
   free. The whole content of D is that `T` is not positive (its symbol is
   indefinite at every chart) and yet `−T` must be positive on the primitive
   radial sector in the colimit.
4. The archimedean Frobenius `Frob_∞(t) = E_{j_∞(e^{−t})}` (Paper 44 §3ter) is
   the flow of the modulus group `(R,+)` on the carrier; radial classes are
   exactly the functions of that flow.

## 2. Theorems to prove in the first campaign (all with honest labels)

**D.1 (the state reformulation; PROVED, standard, to be written on the true
carrier).** For real `g ∈ C_c^∞(R)` let `Λ(g) := −I_∞(Γ_{Πg}, Γ_{Πg})` with
`Π = −∂_t² + ¼` (Paper 45 Cor 10.2: `Π` is a bijection onto the primitive
class). Then: (i) `Λ(g) = Σ_ρ |ρ(1−ρ)|² Φ_g(ρ)Φ_g(1−ρ)` (Paper 45 Lemma 10.3a,
Thm 9.6); (ii) **RH ⟺ `Λ` is a positive functional on `C_c^∞(R)⋆C_c^∞(R)^†`
⟺ the distribution `μ := −\hat T_∞|_{prim} + polar` is a positive tempered
measure on `R` ⟺ (Bochner) there is a unitary representation of the modulus
group `(R,+)` whose spectral measure is `μ` and in which `Λ(g) = ‖π(g)Ω‖²`.**
State precisely what is classical (Weil's criterion, Bochner) and what is
row A–C content (that the group is the carrier's modulus group and the flow
is `Frob_∞`). This is the analytic face of the panel's "nonnegative
invariant": the Hilbert space in which the averaged Frobenius flow is
unitary. Label the equivalence `CLASSICAL + PROVED-IN-REPOSITORY`; say in
words that constructing that Hilbert space **is** row D and is not done here.

**D.2 (the dichotomy imported and connected; PROVED-IN-REPOSITORY).** Restate
P124.013 Thm 3.1 on the true carrier: the unconstrained Weil form on tests of
window `T` is the bordered form `[[L_T, X_T],[X_T^*, B_T]]` with `B_T` Paper
43's hyperbolic Tate plane (Paper 45 Thm 8.1) and `X_T` the Tate collar; at
the first contact `T_q` of the primitive form, either Gate R holds or the
unconstrained form is already indefinite. Connect: the Schur complement
`Σ(T) = B_T − X_T^*L_T^{−1}X_T` is a Hermitian form on Paper 43's `B_T`; prove
its transformation law under the swap `σ` of Paper 45 Rem 8.2 and its
behaviour under `T ↦ T+ε` (monotonicity or its failure). The surviving OPEN
target `Σ(T) ≥ 0 for T < T_q` must be stated with the honest remark that it is
Weil positivity of the unconstrained form up to `T_q`, i.e. RH-strength, not a
shortcut.

**D.3 (finite inertia theorems; PROVED for each finite statement; the sign
itself OPEN).** For `N ≥ 2` and `ε < ε_0(N)` let `G_N(ε)` be the Gram matrix of
the smeared averaged Frobenii `{Γ_n^{rad,sm}}_{2≤n≤N}` under `I_∞` (entries
`W_fin(\log m − \log n) + K(|\log m − \log n|)` off the diagonal by Paper 44
Thm 8bis.1e; diagonal by Thm 8bis.2), and `G_N^{prim}(ε)` its compression to
the primitive subspace (codimension ≤ 2, Paper 44 (8bis.9)). Prove what is
provable about the inertia of `G_N^{prim}` **without RH**: (a) at a fixed
finite chart the inertia is indefinite for large `N` (Paper 43 Thm 14.1
transported — or refute this and record it); (b) in the colimit (all primes
`≤ N` in the chart) compute the inertia numerically for `N ≤ 200` at several
`ε` (illustration only) for `ζ` **and for the falsifier `Ξ_a`** (P124.014's
model, whose Gram kernel replaces `Λ(n)` by `Λ(n)(n^a+n^{−a})` and the
archimedean kernel accordingly); (c) prove the exact statement "RH ⟹
`G_N^{prim}(ε) ≤ 0` for all `N, ε`" (immediate from D.1) and record the
converse as `OPEN` under `(H_L)`. The falsifier must show a **positive**
eigenvalue at finite `N` for `Ξ_a`; if it does not, say so — that would be a
finding against the informativeness of finite inertia.

**D.4 (what a nonnegative invariant would have to be; PROVED negatives +
one honest candidate).** Prove, on the true carrier: (a) the effective cone
`Eff_A` of Paper 43 Thm 10.2 meets the primitive sector only in `0` (a
primitive `F` changes sign), so Weil's route through effectivity of `D` is
not available verbatim — Weil uses `aΔ + bΓ`, not effective classes, and the
inequality comes from `h⁰ ≥ 0` of a *different* divisor; (b) a candidate for
`h⁰`: for a smeared correspondence `F ∈ D_A^{rad}` define `h⁰(F) := dim` of
the space of `G ∈ D_A^{rad}` with `I_∞(F,G) = 0`?? — no: state instead the
requirement list a candidate must satisfy (functor on the correspondence
algebra; nonnegative; RR-type identity with quadratic term `I_∞(F,F)` and
linear term through the rulings `M(F)`; vanishing on a dual sector), and
PROVE that the three obvious candidates fail: dimension of eigenspaces of the
symbol (uses the sign), coefficient positivity (Eff_A, not operator
positivity, Thm 10.2(e)), and the scalar determinant `L_S` (trivial on the
rulings, Paper 43 Thm 10.8). Each failure a theorem with a counterexample.
This is the "shapes it cannot have" list, extended by three items.

**D.5 (falsifier suite as theorems).** On `Ξ_a` and on Davenport–Heilbronn
(no Euler product): state and prove which hypothesis of D.1's reformulation
each falsifier violates *before* any comparison (P122_D_SPECIFICATION §5):
for `Ξ_a` the local roots are not unimodular (weights `p^{−1/2±a}`); for DH
there is no Frobenius family at all. Any D-candidate law proposed later must
pass this suite first.

## 3. Rules

Labels as in Papers 43–45; the hypothesis-carrying rule; (C1) for all-primes
statements; every classical import named with the clause it serves; no
statement about zeros outside the comparison theorem and D.1's classical
equivalence; **no sign is to be claimed**; no relabelling; every blueprint
claim re-proved and refuted with a counterexample if false. Numerics
illustrate and falsify; they prove nothing.

## 4. Deliverables

`04-papers/46-intersection-frame-defect/archive/main.md` (Paper 46 skeleton: §0 target and
negatives; §1 conventions imported by number from Papers 43–45; §2 contract
D-H / D-E from PLAN §8 and P122_D_SPECIFICATION with acceptance test §6; §3
D.1; §4 D.2; §5 D.3; §6 D.4; §7 D.5; §8 external inputs; §9 what is open, in
one sentence per item; §10 no label), `README.md`,
`03-research/phase-134-row-d-opening/scripts/` (Gram inertia for `ζ` and
`Ξ_a`; the Schur complement `Σ(T)` reusing phase-124's `p124_lab.py`),
`R134_001_ROUND1.md` with every refuted claim and its counterexample.
