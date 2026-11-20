# Paper 46 — Row D: the sign

**David Alejandro Trejo Pizzo.**  2026-09-12.

**Status: `SKELETON AND FIRST THEOREMS`.  No label is claimed for row D, and
none is expected from this campaign.  No sign is claimed, asserted or
suggested anywhere in this paper.**

**Part III (§§17–19bis, 20–23) is appended.**  It adds the intrinsic characterization of
the primitive sector and the detecting cones (§17), two constraints on any
admissible proof (§18), the theorem that Part II's clause list is
unsatisfiable (§19), the bidegree route on the square and the reason it closes
(§19bis), the trace-positive cone and its unconditional transfer
theorem (§20), the function-field model in which the same defect appears where
the Riemann hypothesis is a theorem (§21), the degree form on the Frobenius
module and the computed diagonal (§22), and the consolidated state of the
question (§23).  **The label of §10 is unchanged.**

---

## 0. The target, the standing negatives, and what this paper is

### 0.1 The target, boxed as rows A–C box it

> **ROW D'S TARGET: `I_∂ ≤ 0` on every primitive radial class `Γ_g`,
> `g ∈ C_c^∞(R)`, on the colimit `D_A^∞` with `T_∞` and `c = 0`
> (Paper 45 Corollary 9.6a); this implies RH by Paper 45 Theorem 9.6 (9.10)
> and Theorem 10.4.  Standing negatives: Paper 43 Theorem 14.1, Paper 44
> Theorem 8bis.4a; Paper 44 Theorem 8bis.7 is conditional under `(H_L)`,
> `OPEN`.**

Four hypotheses travel with the target and none may be dropped (Paper 45
§14.4): the **colimit** quantifier (Paper 44 convention `(C1)`); the
normalization **`c = 0`**, which Paper 45 Corollary 9.6a(iii) proves is the
unique constant for which the identity holds; **primitivity**; **radiality**.
Every statement in this paper carries them explicitly or says which it drops.

### 0.2 The standing negatives, by theorem number

1. **Paper 43 Theorem 14.1.**  `I_A(F,F) = (1/2π)∫|F̂|²(T̂+c)`; with `c = 0`,
   `m := sup T̂ ≥ \log π + γ + 3\log 2 + π/2 ≈ 5.372 > 0`, so `I_A` is
   indefinite with **infinite index on both sides**, unconditionally; and
   `(D_A^{prim})^{⊥I_A} = 0`, with no `D_A`-module splitting of the Tate
   boundary.
2. **Paper 44 Theorem 8bis.4a.**  Positivity fails on the **pure Frobenius
   form** `Q_{fin}` at **every** finite chart, unconditionally; the colimit
   version is `OPEN` and is not asserted.
3. **Paper 44 Theorem 8bis.7.**  Dirichlet-polynomial profiles suffice only
   under `(H_L)`; `OPEN`.
4. **P124.014.**  Gate R is **not** a structural theorem of the
   "functional equation plus finite Tate compression" class: it fails on
   `Ξ_a(s) = ξ(s+a)ξ(s−a)`.
5. **Phase 133, `PANEL_3` §5.**  What is missing, in one sentence: *a functor
   from the correspondence theory to something carrying a **nonnegative**
   invariant, together with a vanishing theorem, turning the biextension
   equality (Paper 43 (10.10)) into an inequality.*

### 0.3 What this paper is

The opening campaign of row D.  It does five things, labelled D.1–D.5:

* **D.1 (§3)** puts the target in the form in which the missing nonnegative
  invariant is visible as an object: a **positive-definite distribution on the
  modulus group of the carrier**, equivalently a unitary representation of
  that group in which the averaged archimedean Frobenius flow acts and in
  which the target functional is a **squared norm**.  The equivalence is
  graded **`RESTATEMENT`** — classical (Weil's criterion, Bochner–Schwartz in
  its `D'` form, SNAG, GNS) plus row A–C content, with **no proof using the
  modulus-group identification beyond naming**; its two new ingredients are
  Lemma 3.1 and Theorem 3.6.  The construction of the Hilbert space **is** row
  D and is **not** done here.
* **D.2 (§4)** transports the shielding dichotomy of P124.013 onto the true
  carrier, proves a **swap law** for the Schur complement `Σ(T)` that reduces
  the surviving constraint-free target to two scalar inequalities, and proves
  that the expected monotonicity in `T` is **not available**.
* **D.3 (§5)** proves what is provable about the inertia of the Gram matrix of
  the smeared unit-averaged Frobenius family on the primitive subspace, and
  determines its `ε → 0` asymptotics (Theorem 5.8: unconditionally negative
  definite below an explicit `ε_1(N)`, for every model).  It records numerics
  for `ζ` and for the falsifier `Ξ_a`, which illustrate and falsify and prove
  nothing.  **D.3 is retired as a programme item, §9.1(13); Theorem 5.8 is
  kept as its result.**
* **D.4 (§6)** proves five negatives about what a nonnegative invariant cannot
  be, each with a counterexample, and a **sixth** structural one added in
  round 3: the requirement list is vacuous for any duality preserving
  primitivity, and `†` — the only duality rows A–C construct — does preserve
  it (Definition 6.8(R5)).
* **D.5 (§7)** states, for `Ξ_a` and for Davenport–Heilbronn, exactly which
  **pre-comparison** axiom of rows A–C each violates.

Every blueprint claim was re-proved.  **Six were refuted or repaired**; they
are marked `REFUTED` or `REPAIRED` in place and listed in §9.2.

---

## 1. Conventions, imported by number

Nothing in this section is new.  Each item is cited by the number under which
it is proved in Papers 43–45, and is used only as stated there.

**(1.1) The carrier.**  Paper 43 §14.0a: a fixed finite chart `S` (`∞ ∈ S`,
`S_f ≠ ∅`), the chart system and its colimit as additional structure,
**invertible sector only**; `C_S` the idele class group of the chart;
`D_A = C_c^∞(C_S)`; the declared trace with **`c := 0`** (Paper 43
Definition 8A.7d, derived in Paper 45 Corollary 9.6a(iii)).

**(1.2) The modulus coordinate.**  `t = −\log|x|_S`, and by Paper 43
Lemma 3.3 `|x|_S = |x_∞|`, so the modulus map `C_S → R` is a split surjection
with compact kernel `K^♮` and `d^*w = dt ⊗ μ`, `μ` a probability measure
(Paper 43 Theorem 9.14a's proof).  **Radial** means `K^♮`-invariant; radial
classes are exactly the functions of the modulus flow.

**(1.3) Radial classes.**  Paper 44 Definition 3bis.6 and Lemma 3bis.6a: for
`h ∈ C_c^∞(R)`, `Γ_h ∈ D_A^{rad}`, `Γ_h ⋆ Γ_g = Γ_{h∗g}`,
`Γ_h^† = Γ_{h^∨}`, `λ_∓(Γ_h) = ∫h(s)e^{±s/2}ds`.

**(1.4) The two halves of the Weil kernel.**  Paper 44 (3bis.9):
`W_{fin} = Σ_{q,k}(\log q)q^{−k/2}(δ_{k\log q} + δ_{−k\log q})`,
`ω_∞ = K(|t|)dt` with `K(t) = e^{−t/2}/(1−e^{−2t})`; and Theorem 3bis.7,
`T(Γ_h) = ∫h\,d(W_{fin}+ω_∞)` for `0 ∉ supp h`.

**(1.5) The Frobenius family.**  Paper 44 Theorems 3ter.4, 3ter.6, 3ter.7:
`Frob_1 = Δ` is a true unit, `Frob_n^† = Frob_{n^{−1}}`,
`Frob_n ⋆ Frob_n^† = Δ^{(n)}`, bidegree `(n^{1/2},n^{−1/2})`, and the
`†`-closure is a commutative **inverse semigroup** graded by prime sets.  The
archimedean Frobenius `Frob_∞(t) = E_{j_∞(e^{−t})}` (Paper 44 §3ter) is a
one-parameter **group**: `Frob_∞(s)⋆Frob_∞(t) = Frob_∞(s+t)`,
`Frob_∞(0) = Δ`, `Frob_∞(t)^† = Frob_∞(−t)` — the flow of the modulus group
`(R,+)` on the carrier.

**(1.6) The kernel is the Gram form of the unit-averaged family.**  Paper 44
Theorem 8bis.1e: with `Γ_n^{rad} = Frob_n ⋆ Δ^{rad}` and smeared profiles
`h_m,h_n`,
`I_A(Γ_m^{rad,sm},Γ_n^{rad,sm}) = ∫(h_m⋆h_n^†)\,d(W_{fin}+ω_∞)`, and in the
concentrated limit the entry is `W_{fin}(\{\log m − \log n\}) +
K(|\log m − \log n|)` (8bis.7).  Hypotheses carried: width `ε < ε_0(A,S)`, and
**chart** — `T` is `T_∞` and `W_{fin}` is the colimit kernel by `(C1)`.  The
diagonal is Theorem 8bis.2, which is **exempted** from `(C1)`.

**(1.7) Primitivity.**  Paper 44 (8bis.9): `M(Γ_g) = (λ_−,λ_+) = (0,0)`, the
two Tate conditions; equivalently (Paper 45 Theorem 8.1(ii), P124.013 (1.3))
`Φ_g(0) = Φ_g(1) = 0` where `Φ_g(s) = ∫g(t)e^{(s−1/2)t}dt`.

**(1.8) The rulings and the polar packet.**  Paper 45 Theorem 8.1:
`M(Γ_F) = (Φ_F(1),Φ_F(0))` and `β_T(M(Γ_F),M(Γ_F)) = 2Φ_F(0)Φ_F(1)`, the
polar packet; `β_T` has matrix `[[0,1],[1,0]]` in the basis `e_∓` of
`B_T = C⊕C`, and `†` acts by the swap `♯`.  **Notation, fixed here and used
without exception (round 2, finding (M7) of `R134.002`): `B_T` denotes this
ruling plane and nothing else.  The Tate `2×2` **block** of the Weil form on
the border `span\{φ_+,φ_-\}` — which P124.013 (2.3) unfortunately also writes
`B_T` — is written `𝔅_T` in this paper.  §4.2 exists to separate them.**
**Remark 8.2**: `M(Γ_F) = σ(z(F))`
with `σ` the swap, not `z(F)`; `β_T` is `σ`-invariant.

**(1.9) The comparison theorem.**  Paper 45 Theorem 9.6, hypotheses carried
(`F` real and `C_c^∞`; `c = 0`; the trace is `T_∞` on `D_A^∞`; symmetric zero
sum):
`I_∞(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)` (9.9), and on the
primitive radial sector `I_∞(Γ_F,Γ_F) = −Σ_ρΦ_F(ρ)Φ_F(1−ρ)` (9.10).  At a
fixed finite chart (9.9)–(9.10) hold **only** inside the window
`R(Γ_h) < \log ℓ_{next}(S)` and are **false** outside it.

**(1.10) Sufficiency.**  Paper 45 Theorem 10.4: if RH is false there are
nonzero compactly supported **primitive** real tests, even and odd, with
`Σ_ρΦ(ρ)Φ(1−ρ) < 0`; hence `q_T ≥ 0` on `P_T` for every `T` implies RH.

**(1.11) The primitivization operator.**  Paper 45 Lemma 10.1,
Corollary 10.2, Lemma 10.3a: `Π := −∂_t² + ¼`, `Φ_{ΠG}(s) = s(1−s)Φ_G(s)`,
`Π` maps `C_c^∞(I_T)` into `P_T` preserving support, reality and parity, and
is **injective by analyticity**; and for `F = ΠG`,
`Σ_ρΦ_F(ρ)Φ_F(1−ρ) = Σ_ρ[ρ(1−ρ)]²Φ_G(ρ)Φ_G(1−ρ)`.

**(1.12) Status labels.**  As in Papers 43–45: `PROVED` (here),
`PROVED-IN-REPOSITORY`, `CLASSICAL` (named, with the clause it serves, §8),
`IMPORTED` (hypotheses checked), `OPEN`, `REFUTED`,
`COMPUTATIONAL-ILLUSTRATION` (proves nothing).

**(1.13) The hypothesis-carrying rule.**  Every statement carries every
hypothesis it uses in its own text.  No statement is made about the location
of the zeros of `ζ` anywhere in this paper except inside the comparison
theorem (1.9), cited from Paper 45, and inside D.1's classical equivalence
(**Theorem 3.7**), where the equivalence *is* with RH; together with
Theorem 5.6, which carries RH as its own explicit hypothesis, and the
bracketed note in §7.1 about the falsifier `Ξ_a`, which is used in no proof.
**[AMENDED, phase 135 round 2, finding M11 of `R135_002`.  The sentence above
was a factual claim about this paper and Part II falsifies it as stated.  Part
II uses, inside proofs, the following **classical unconditional** facts about
the location of the zeros, all of them imported data and none of them a
statement this paper proves or needs to prove: `0 < \mathrm{Re}\,ρ < 1` and
`ζ(σ) ≠ 0` for `σ ∈ (0,1)` (import (E2), used in Lemma 11.9, Theorems 11.10,
11.11, Theorem 11.14 and, as the datum it replaces, Lemma 12.4A); `ζ(s) ≠ 0`
for `\mathrm{Re}\,s ≥ 1` (import (E2), Proposition 11.11a); Hardy's theorem
(import (X16), essentially in Theorem 12.4); and the positive proportion of
simple zeros (import (X18), Theorem 11.12).
**[AMENDED AGAIN, phase 135 round 3, finding N7/M11 of `R135_005`.  Round 2
substituted the rule "no statement about the location of the zeros of `ζ` is
proved, asserted or conjectured anywhere in this paper, and no object is
defined by the location of a zero."  Its second clause holds; its first does
not, and round 2's list was inaccurate in two places.  The rule as actually
obeyed in Part II is this.

* **No statement about the location of the zeros of `ζ` beyond the classical
  unconditional facts listed above is proved, asserted or conjectured** — and
  those facts enter only as **data**: `0 < \mathrm{Re}\,ρ < 1` (import (E2))
  in Lemma 11.9, Theorems 11.10, 11.11 and 11.14; Hardy's theorem (import
  (X16)) in Theorem 12.4; the simple-zero proportion (import (X18)) in
  Theorem 11.12.
* Two classical facts are, exceptionally, **proved here rather than imported**,
  both from the positivity of Pólya's kernel `K > 0` (import (X12)) and both
  used only as data: `ξ(σ) = Φ_K(σ) > 0` for every real `σ` (Lemma 13.5b),
  which is (E2)'s last clause, and its `Ξ_a`-analogue "no zero of `Ξ_a` is
  real" (Lemma 12.4A(v)).  Proving them is a virtue and not a defect, but they
  **are** statements about zero locations and are named here as such.
* **No object anywhere in this paper is defined by the location of a zero**
  (see (11.13), (12.4) and Definition 13.4), and **no sign is claimed**.

Round 2's list also attributed `ζ(σ) ≠ 0` on `(0,1)` to "Proposition 12.4A".
The correct reference is **Lemma** 12.4A, and Lemma 12.4A/Proposition 12.4B
are precisely the statements that **avoid** importing that clause, proving the
`Ξ_a`-analogue instead; and the list omitted **Theorem 11.14**, whose repaired
proof uses `0 < \mathrm{Re}\,ρ < 1` twice.]**]**
**[CORRECTED, round 3, minor `(r2)` of `R134_005`: round 2's text cited
Theorem 3.6, which is the distribution identity and contains no statement
about zeros.  In the clause that defines this paper's compliance with the
zeros rule, the theorem number must be the right one.]**

---

## 2. The contract: routes D-H and D-E, and the acceptance test

### 2.1 The two routes (PLAN §8)

`PLAN` §8 fixes the common target `q_T(F) = −I_A([K_F],[K_F]) ≥ 0` on every
primitive `F`, and offers **two sufficient routes; closing one suffices, and
they are not to be accumulated as simultaneous requirements**.

* **D-H (Hodge index from the source theory).**  Construct a polarization `H`
  and prove an index theorem on the appropriate numerical space.  The
  signature of the hyperbolic Tate plane must be **placed in the relevant
  scalar intersection form**: a signature may not be assigned to a vector of
  traces without specifying its geometric scalarization.  Prove
  non-positivity on the primitive sector.  An RR route needs growth of
  sections, duality and a cone effect sufficient to deduce the inequality; an
  energy route needs a global inequality with an exact constant and a proved
  domain.  In infinite rank, finite-dimensional dimension counts must be
  replaced by proved estimates.
* **D-E (excluding first contact by a source law).**  Revalidate the entry
  point; find a law, prior to the supertrace, annihilating the oriented defect
  of a first-contact state.  `R` and `S` are a candidate factorization of that
  obligation.  A purely local identity valid for arbitrary data has **not**
  selected the arithmetic state.

**Closure of D:** an independent proof of D-H or D-E with all hypotheses
verified, and the sign transported to the domain of C.  No hypothesis of the
form "there exists a contraction", "there is a positive metric" or "the
connection is horizontal" may remain unproved.

### 2.2 The specification of a genuine D object (P122)

`P122_D_SPECIFICATION` §§1–3 require: a stable category `D_T` with two ruling
objects, mixed classes, **oriented** local objects before their scalar trace,
an archimedean object carrying the exact Gamma distribution, restriction
functors and a cofinal system; a mixed product, a Rosati involution **not**
identifying the two causal orientations, a degree/supertrace, numerical
equivalence as the radical against **all** objects, a primitive subspace, and
exact local-to-global reciprocity **including** the archimedean object.  The
category **may not** be defined using positivity, the kernel, or the spectral
decomposition of `Δ_T`; and `(M_f,M_g)_D = B_{nuc}(f,g)` may **not** be taken
as a definition.

### 2.3 The acceptance test (P122 §6), quoted

```text
carrier + operations + orientations + restriction
are constructed without B_nuc positivity;
an independent theorem proves Hodge/RR/oriented reciprocity;
the candidate fails a non-Euler explicit-formula model before comparison;
comparison with B_nuc is proved last.
```

### 2.4 Where this paper stands against the test

**Proposition 2.1 (self-assessment, `PROVED` by inspection).**  Against §2.3:

  (i) *carrier + operations + orientations + restriction, without positivity*:
      supplied by rows A and B for the **invertible sector** (Paper 43 §§3–5,
      8A, 9; Paper 44 §3ter), and **not** re-derived here.  The finite-place
      subobject `D^{fin}_{T,sf}` of P122 (7.1) and the archimedean relative
      determinant of P122 §9 remain **separate**; the relative correspondence
      joining them is `NOT CONSTRUCTED`.
  (ii) *an independent theorem proving Hodge/RR/oriented reciprocity*:
      **absent**.  §6 proves five theorems about what it cannot be.
  (iii) *the candidate fails a non-Euler model before comparison*: §7 states
      the failure axiom for `Ξ_a` and for Davenport–Heilbronn, for the
      **reformulation** D.1 — which is the only candidate object this paper
      puts on the table — and proves it.
  (iv) *comparison proved last*: the comparison is Paper 45 Theorem 9.6, cited
      and not re-proved; nothing in this paper defines an intersection number
      by the comparison.

So this paper satisfies (i) only by inheritance, satisfies (iii), does not
satisfy (ii), and (ii) is row D.  ∎  `PROVED` (by inspection of the cited
constructions)

---

## 3. D.1 — the state reformulation

Throughout this section `g` is real and `C_c^∞(R)`, `Π = −∂_t² + ¼`, and the
trace is `T_∞` on `D_A^∞` with `c = 0` (convention `(C1)`).

### 3.1 `Π` is a bijection onto the primitive class — and Corollary 10.2 does not say so

The blueprint cites Paper 45 Corollary 10.2 for "`Π` is a bijection onto the
primitive class".  **Corollary 10.2 proves injectivity and does not prove
surjectivity.**  Surjectivity is true, and here is its proof; it is needed,
because without it "positivity of `Λ` on `C_c^∞`" would be formally weaker
than "positivity of `q_T` on `P_T`", and D.1 would be an implication and not
an equivalence.

**Lemma 3.1 (`Π` is a linear bijection `C_c^∞(I_T) → P_T`; `PROVED`).**  Let
`I_T = (−T,T)`, `P_T = \{F ∈ C_c^∞(I_T) : Φ_F(0) = Φ_F(1) = 0\}`.  Then
`Π : C_c^∞(I_T) → P_T` is a linear bijection, with inverse
`F ↦ G_{1/2} ∗ F`, `G_{1/2}(t) = e^{−|t|/2}`; moreover
`\mathrm{conv}\,supp(Π^{−1}F) = \mathrm{conv}\,supp F`.

*Proof.*  `Π` maps into `P_T` and is injective: Paper 45 Corollary 10.2.
Surjectivity.  `G_{1/2}` is the Green kernel of `Π` on `R`:
`(−∂_t²+¼)e^{−|t|/2} = δ_0` in `D'(R)` (differentiate twice: the jump of the
first derivative at `0` is `−1`).  Let `F ∈ P_T` and put `u := G_{1/2} ∗ F`.
Then `u ∈ C^∞(R)` (convolution of an `L^1` kernel with a `C_c^∞` function),
and `Πu = F`.  For `t` to the right of `supp F`,

    u(t) = ∫ e^{−(t−s)/2}F(s)ds = e^{−t/2}∫e^{s/2}F(s)ds = e^{−t/2}Φ_F(1) = 0 ,

and symmetrically, for `t` to the left of `supp F`,
`u(t) = e^{t/2}Φ_F(0) = 0`.  **The two Tate conditions are exactly the two
conditions that make `u` compactly supported**, and they are available by
hypothesis.  Hence `u ∈ C_c^∞(I_T)` with
`supp\,u ⊆ [\min supp F, \max supp F]`, and `Πu = F`.  The support statement
follows from the two displays together with `supp\,ΠF ⊆ supp F`.  ∎  `PROVED`

**Remark 3.2.**  Lemma 3.1 is the exact converse of Paper 45 Corollary 10.2
and is the reason the primitive class is not merely an image but a *coordinate
chart*: `P_T ≅ C_c^∞(I_T)` as topological vector spaces, by an isomorphism
that intertwines `Π²` with the identity on the level of the quadratic forms
below.  Nothing about zeros is used.

### 3.2 The functional `Λ`, and a correction to the blueprint's formula

**Definition 3.3.**  For real `g ∈ C_c^∞(R)` put
`Λ(g) := −I_∞(Γ_{Πg},Γ_{Πg})`.

**Theorem 3.4 (the zero-side expression; `PROVED-IN-REPOSITORY`).**  With the
hypotheses of (1.9) — `c = 0`, colimit trace, symmetric zero sum —

    Λ(g) = Σ_ρ [ρ(1−ρ)]² Φ_g(ρ) Φ_g(1−ρ) .                           (3.1)

*Proof.*  `Πg` is primitive (1.11), so (9.10) gives
`−I_∞(Γ_{Πg},Γ_{Πg}) = Σ_ρΦ_{Πg}(ρ)Φ_{Πg}(1−ρ)`, and Lemma 10.3a rewrites the
summand as `[ρ(1−ρ)]²Φ_g(ρ)Φ_g(1−ρ)`.  ∎  `PROVED-IN-REPOSITORY`

**`REFUTED` (blueprint D.1(i)).**  The blueprint writes
`Λ(g) = Σ_ρ |ρ(1−ρ)|²Φ_g(ρ)Φ_g(1−ρ)`, with `|ρ(1−ρ)|²` in place of
`[ρ(1−ρ)]²`.  **That is false as an unconditional identity, and writing it
presupposes the very conclusion row D is forbidden to assume.**
Counterexample: for `ρ = β+iγ` one has
`ρ(1−ρ) = (β−β²+γ²) + iγ(1−2β)`, so `[ρ(1−ρ)]²` is real **iff**
`γ(1−2β)\big[(β−β²+γ²)\big] = 0`, i.e. iff `β = ½` (or `γ = 0`, or
`β−β²+γ²=0`).  Concretely, at `ρ = 0.6+14i`:
`ρ(1−ρ) = 196.24 − 2.8i`, so
`[ρ(1−ρ)]² = 38 502.3 − 1 098.9i` while `|ρ(1−ρ)|² = 38 518.0` — different
numbers, the first not even real.  The substitution `[·]² ↦ |·|²` is legitimate
**exactly on the critical line**, hence assuming it is assuming RH.
**Corrected statement: (3.1), with `[ρ(1−ρ)]²`.**  Lemma 10.3a is the correct
source and says exactly this.

**Remark 3.5 (and the same trap one level up).**  For the same reason
`Φ_g(1−ρ) = \overline{Φ_g(ρ)}` for real `g` holds **iff** `1−ρ = \barρ`, i.e.
iff `ρ` is on the critical line.  Off the line the summand of (3.1) is not a
square modulus, and (3.1) is not a sum of nonnegative terms.  This is the
whole difficulty of row D written once: **the sum (3.1) is manifestly
nonnegative precisely when what is to be proved is already true.**

### 3.3 The linear functional, and the reformulation

**Theorem 3.6 (`Λ` is the quadratic form of an explicit distribution;
`PROVED`).**  **[REBUILT, round 2, finding `(M1)` of `R134.002` = `LF1` of
`R134.003`, and minor `(m1)`.  Round 1 called `𝔏` *tempered* and justified it
by the temperedness of its three summands.  **That justification was false**
— see Proposition 3.6a — and the repair, which is `Πϖ = 0`, also **shortens**
the object.]**  Define the distribution on `D(R)`

    𝔏 := Π²\big[\,ϖ − (W_{fin} + ω_∞)\big] = −\,Π²\big(W_{fin} + ω_∞\big) ,
    ϖ(t)\,dt := 2\cosh(t/2)\,dt ,                                     (3.2)

the second equality because **`Πϖ = 0` identically**: `Π e^{±t/2} =
(−∂_t²+¼)e^{±t/2} = 0`, and `ϖ = e^{t/2}+e^{−t/2}`.  Here:

* `𝔏 ∈ D'(R)` and **no temperedness is claimed**.  `W_{fin}+ω_∞` is a Radon
  measure on `R∖\{0\}` with the finite-part regularization of Paper 44 (8.5∞)
  at `t = 0`; it pairs with every `h ∈ C_c^∞(R)` by Paper 45 **Lemma 5.1a**
  (no support hypothesis), and `Π²` maps `D'(R)` to `D'(R)`.
* **The `δ_0` finite part is exactly the constant `c`, and `c = 0` is part of
  the definition** (minor `(m1)`).  `ω_∞ = K(|t|)dt` is not integrable at `0`
  (`K(t) ∼ 1/2t`), so (3.2) is well defined only once the finite part is
  fixed; two admissible regularizations differ by `κδ_0`, and
  `⟨Π²(κδ_0), g⋆g^†⟩ = κ\,((Πg)⋆(Πg)^†)(0) = κ‖Πg‖_{L²}²` — which is precisely
  the correction `c‖F‖_{L²}²` that Paper 45 Corollary 9.6a(i) isolates.  So
  `c = 0` is not merely carried in the preamble of §3: **it *is* the choice of
  finite part in (3.2)**, and by Corollary 9.6a(iii) it is the unique choice
  for which (3.3) holds.

Then, for every real `g ∈ C_c^∞(R)`,

    Λ(g) = 𝔏(g ⋆ g^†) .                                               (3.3)

*Proof.*  Let `h := g⋆g^†`, so `Φ_h(s) = Φ_g(s)Φ_g(1−s)` for real `g`
(Paper 45 Theorem 8.1's computation).  Paper 45 Theorem 9.4, rearranged, says

    Σ_ρ Φ_h(ρ) = \big[Φ_h(0)+Φ_h(1)\big] − ⟨h, W_{fin}+ω_∞⟩ ,

and `Φ_h(0)+Φ_h(1) = ∫h(t)(e^{−t/2}+e^{t/2})dt = ⟨h,ϖ⟩`; this is `⟨h, ϖ −
(W_{fin}+ω_∞)⟩`.  Next, `Π` is formally self-adjoint with symbol
`Φ_{Πu}(s) = s(1−s)Φ_u(s)`, so
`Φ_{(Πg)⋆(Πg)^†}(s) = [s(1−s)]²Φ_h(s) = Φ_{Π²h}(s)`, i.e.
`(Πg)⋆(Πg)^† = Π²h` as compactly supported distributions (equality of entire
Mellin transforms, Paper 45 Lemma 10.1 and analyticity).  Applying the
previous display to `Π²h` and using Theorem 3.4 gives
`Λ(g) = ⟨Π²h, ϖ − (W_{fin}+ω_∞)⟩ = ⟨h, Π²(ϖ − (W_{fin}+ω_∞))⟩`, all pairings
being of compactly supported smooth functions against a `D'`-distribution.
Finally `Π²ϖ = 0`, which removes the exponentially growing summand.  ∎
`PROVED`

**Proposition 3.6a (the repair is necessary, not cosmetic: neither summand of
round 1's justification is tempered; `PROVED`).**  **[CUT BACK, round 3,
finding `(F1)` of `R134_005`.  Round 2 added a part (iii), "`Π²W_{fin} ∉
S'(R)`", at `PROVED`.  **That part was not proved and is false under RH**; it
is deleted, and Remark 3.6b below replaces it with the true statement.  See
§9.2a for the withdrawal.  Parts (i) and (ii) are correct, are proved here in
full, and are all that is needed to refute round 1's justification.]**  Fix
once a function

    ψ(t) := χ(t)\,e^{−|t|^{1/2}} ,                                     (3.2a)

with `χ ∈ C^∞(R)`, `χ = 0` on `[−1,1]`, `χ = 1` off `[−2,2]`, `0 ≤ χ ≤ 1`.
Then `ψ ∈ S(R)`: every derivative of `e^{−|t|^{1/2}}` is a finite combination
of terms `|t|^{−k/2}e^{−|t|^{1/2}}`, `k ≥ 0`, each decaying faster than any
power of `|t|^{−1}`, and `χ` removes the singularity at the origin.  But `ψ`
decays **slower than every exponential**, and `ψ ≥ 0`.  Then:

  (i) `ϖ(t) = 2\cosh(t/2) ∉ S'(R)`;
  (ii) `W_{fin} ∉ S'(R)`.

*Proof.*  Both are instances of one argument, and the argument is about a
**positive** object paired with a **nonnegative** Schwartz function, which is
what makes it legitimate.  Let `μ` be a positive Radon measure on `R` and
suppose `μ ∈ S'(R)`.  Take `θ_j ∈ C_c^∞(R)` with `0 ≤ θ_j ≤ 1`, `θ_j = 1` on
`[−j,j]`, `θ_j = 0` off `[−j−1,j+1]`, and all derivatives bounded uniformly in
`j`.  Then `ψθ_j ∈ D(R)`, the family `(ψθ_j)_j` is **bounded in every
`S`-seminorm** (Leibniz, with `ψ` Schwartz and `θ_j`'s derivatives uniformly
bounded), so `⟨μ,ψθ_j⟩` is bounded by continuity of `μ` on `S(R)`.  But
`ψθ_j ↑ ψ` pointwise with `ψ ≥ 0` and `μ ≥ 0`, so by monotone convergence
`⟨μ,ψθ_j⟩ → ∫ψ\,dμ`.  Hence `∫ψ\,dμ < ∞` is **necessary** for `μ ∈ S'(R)`.
It fails in both cases:

    (i)   ∫ϖψ\,dt ≥ ∫_2^∞ e^{t/2}e^{−t^{1/2}}dt = ∞ ;
    (ii)  ∫ψ\,dW_{fin} = 2Σ_{n≥2}Λ(n)n^{−1/2}ψ(\log n)
            ≥ 2Σ_{p ≥ 8}(\log p)\,p^{−1/2}e^{−(\log p)^{1/2}} = ∞ ,

the second by Chebyshev's bound `Σ_{p ≤ x}(\log p)p^{−1/2} ≫ \sqrt x`
(import **(X11)**) and partial summation, the factor `e^{−(\log p)^{1/2}}`
being smaller than every power of `\log p` and larger than every power of
`p^{−1}`.  ∎  `PROVED`

**Remark 3.6b (why nothing may be concluded about the temperedness of `𝔏`,
and why Theorem 3.7 does not need it).**  **[NEW, round 3, replacing the
deleted Proposition 3.6a(iii).]**  Proposition 3.6a refutes round 1's
*justification*.  It does **not** decide whether `𝔏` is tempered, and no
argument of that shape can, for a reason internal to Theorem 3.6.

1. *`Π²` annihilates exactly the growth that (i) and (ii) exploit.*  Since
   `Π²ϖ = 0` (Theorem 3.6), writing `ν := W_{fin} − ϖ\,dt` gives
   **`Π²W_{fin} = Π²ν` exactly**.  So a growth estimate on `W_{fin}` alone
   says nothing about `Π²W_{fin}`: the divergence in (ii) is carried entirely
   by the summand that `Π²` kills.
2. *Under RH, `Π²W_{fin}` **is** tempered.*  Let
   `M(t) := Σ_{2≤n≤e^t}Λ(n)n^{−1/2}`, and note
   `∫_0^tϖ(s)ds = 4\sinh(t/2) = 2e^{t/2}+O(1)`.  Under RH,
   `ψ_{Ch}(x) = x + O(\sqrt x\log²x)`, and partial summation gives
   `M(t) = 2e^{t/2} + O(t³)`.  Hence the distribution function of `ν` is
   **polynomially bounded**, so `ν ∈ S'(R)` (a locally integrable function of
   polynomial growth, differentiated once), and therefore
   `Π²W_{fin} = Π²ν ∈ S'(R)`.  Consequently **a proof that `Π²W_{fin}` is not
   tempered would be a proof of ¬RH** — which this paper is forbidden to
   attempt, and which is the decisive reason the deleted part (iii) could not
   stand whatever its proof.
3. *Equivalently, the question is a PNT-type growth statement.*  `𝔏` is
   tempered iff `Π²W_{fin}` is (because `ω_∞` with its (8.5∞) finite part is
   tempered: `K(t) ∼ 1/2t` at the origin after the finite part, and
   `K(t) ∼ e^{−t/2}` at infinity), and `Π²W_{fin}` is tempered as soon as
   `M(t) − 2e^{t/2}` is polynomially bounded.  **Whether that holds is not
   decided here, in either direction.**
4. *And Theorem 3.7 does not need it.*  Import **(X3)** is used in its
   `D'(R)` form, in which temperedness is a **conclusion** of
   positive-definiteness and not a hypothesis.  That is the whole point of the
   `(M1)` repair, and part (iii) was an unnecessary extra on top of a repair
   that was already complete.  By Theorem 3.7 (c) ⟹ (d), temperedness of `𝔏`
   is in fact *implied by* row D's target — one more reason it cannot be
   refuted here.

*(A numerical illustration only, proving nothing: `M(t) − 4\sinh(t/2)` computed
over all prime powers `n ≤ 4·10^6` reads `−2.32, −2.48, −2.39, −2.80, −2.58,
−2.27, −2.20` at `t = 4,6,8,10,12,14,15` — bounded, not growing, over four
orders of magnitude in `e^t`.  The cancellation of item 1 is total in
practice.)*

**`REPAIRED` (blueprint D.1(ii), the distribution).**  The blueprint writes
`μ := −\hat T_∞|_{prim} + polar`.  Four repairs: (a) the object is a
distribution on `R`, `𝔏 ∈ D'(R)`, and `μ` is its **Fourier transform**, so the
two may not be written with the same letter or in the same slot; (b) the
factor `Π²` is **not** optional — without it the polar packet does not drop;
and with it the polar packet drops **identically**, because `Π²ϖ = 0`, which
is the structural reason and not a computation on the primitive sector;
(c) "`\hat T_∞|_{prim}`" is not a defined object: restriction to the primitive
sector is a statement about the test class, not about the symbol; (d) no
temperedness may be asserted (Proposition 3.6a).  Corrected: (3.2)–(3.3).

**Theorem 3.7 (the state reformulation).  `RESTATEMENT` (`CLASSICAL` +
`PROVED-IN-REPOSITORY`).**  **[REGRADED, round 2, `LF2` of `R134.003` and the
adversarial audit's §5, both upholding the the construction's own round-1 press point `P1`.
Round 1 graded this `CLASSICAL + PROVED-IN-REPOSITORY`; every link in the
equivalence is either a named classical theorem or a citation of Papers 43–45,
so the grade over-credited the section.  **Lemma 3.1 and Theorem 3.6 are
carved out and remain `PROVED`**: they are small new theorems and Lemma 3.1 is
load-bearing.]**  **Hypotheses carried:** the trace
is `T_∞` on `D_A^∞` with `c = 0`; classes are radial; tests are real
`C_c^∞(R)`; the zero sum is symmetric.  The following are equivalent.

  **(a)** RH.
  **(b)** `Λ(g) ≥ 0` for every real `g ∈ C_c^∞(R)`; equivalently (Lemma 3.1)
      `I_∂ ≤ 0` on every primitive radial class — **row D's target**.
  **(c)** `𝔏` of (3.2) is a **positive-definite distribution on `D(R)`**:
      `𝔏(g⋆g^†) ≥ 0` for all `g ∈ C_c^∞(R)`.  *(No temperedness is assumed;
      by Proposition 3.6a none is available a priori.)*
  **(d)** `𝔏` **extends to a tempered distribution** and there is a positive
      tempered measure `μ` on `R` with `𝔏 = \hatμ` (Bochner–Schwartz in its
      `D'(R)` form, import **(X3)**).  *(Temperedness here is a **conclusion**,
      not a hypothesis.)*
  **(e)** there is a Hilbert space `H`, a strongly continuous **unitary
      representation** `π` of the modulus group `(R,+)` of the carrier, and a
      cyclic vector `Ω ∈ H`, with spectral measure `μ` and

          Λ(g) = ‖π(g)Ω‖²  for every real g ∈ C_c^∞(R),
          π(g) := ∫_R g(t)\,π(t)\,dt ,                                 (3.4)

      with `⋆` and `†` the convolution and dagger of (1.3), so that
      `‖π(g)Ω‖² = ⟨π(g⋆g^†)Ω,Ω⟩ = 𝔏(g⋆g^†)`.

  If these hold, `μ` is the measure `Σ_γ (¼+γ²)²\,δ_γ` (multiplicities
  included) obtained from the zero sum by `ρ = ½+iγ`.

*Proof.*  **(a) ⟺ (b).**  `(a) ⇒ (b)`: under RH, `ρ = ½+iγ` gives
`Φ_g(1−ρ) = \overline{Φ_g(ρ)}` for real `g` and `[ρ(1−ρ)]² = (¼+γ²)² > 0`, so
every summand of (3.1) is `(¼+γ²)²|Φ_g(ρ)|² ≥ 0`; this is Weil's criterion in
the direction that is a computation, using the symmetric summation convention
of (1.9).  `(b) ⇒ (a)`: by Lemma 3.1 every `F ∈ P_T` is `Πg` for some
`g ∈ C_c^∞(I_T)`, so (b) says `q_T ≥ 0` on `P_T` for every `T`, and
Paper 45 Theorem 10.4 gives RH.  **This is the only place in this paper where
(1.10) is used, and it is used in this direction only.**
**(b) ⟺ (c).**  Theorem 3.6, verbatim: `Λ(g) = 𝔏(g⋆g^†)`.  One line is
needed on the quantifier, because (b) quantifies over **real** `g` and
positive-definiteness over **complex** `g` (minor `(m2)` of `R134.002`):
`W_{fin}`, `ω_∞` and `ϖ` are real and **even**, hence so is `𝔏`; writing
`g = u+iv` with `u,v` real,
`g⋆g^† = u⋆u^† + v⋆v^† + (v⋆u^† − u⋆v^†)`, and the bracket is an **odd** real
distribution, which pairs to `0` against the even `𝔏`.  Hence
`𝔏(g⋆g^†) = Λ(u) + Λ(v)`, and the real and complex quantifiers agree.
**(c) ⟺ (d).**  **[REBUILT, round 2, `(M1)`.  Round 1 justified this step by
asserting that `𝔏` is tempered because its summands are.  **That is false**
(Proposition 3.6a) and the step is repaired by using the right form of the
import.]**  The Bochner–Schwartz theorem **in its `D'(R)` form** (L. Schwartz),
import **(X3)** of §8: *a positive-definite distribution on `D(R)` is
automatically tempered and is the Fourier transform of a unique positive
tempered measure.*  So (c) ⟹ (d) requires **no** hypothesis on `𝔏` beyond
`𝔏 ∈ D'(R)`, which (3.2) supplies via Paper 45 Lemma 5.1a; and (d) ⟹ (c) is
the elementary direction, `\hatμ(g⋆g^†) = ∫|\hat g|²dμ ≥ 0`.
**(d) ⟺ (e).**  The extension in (d) is **unique**: `D(R)` is dense in
`S(R)`, so a tempered distribution is determined by its restriction to
`D(R)`, and the representing measure `μ` is then unique by injectivity of the
Fourier transform on `S'(R)`.  With that, SNAG/Stone, import **(X4)**, and the
GNS construction, import **(X5)**: a positive-definite distribution yields a cyclic unitary
representation of `R` with `Λ(g) = ⟨π(g)Ω,π(g)Ω⟩`, and conversely the
spectral measure of a cyclic unitary representation of `R` is a positive
measure whose Fourier transform is the positive-definite distribution.
**The identification of `μ`.**  Under (a), (3.1) reads
`Λ(g) = Σ_γ(¼+γ²)²|Φ_g(½+iγ)|²` and `Φ_g(½+iγ) = \hat g(−γ)` in the
normalization of (1.7), so `μ = Σ_γ(¼+γ²)²δ_γ` by uniqueness of the
representing measure.  ∎  `RESTATEMENT`: assembled from **(X2)–(X5)**,
(1.9), (1.10), Lemma 3.1 and Theorem 3.6.  The two new ingredients, and the
only ones, are Lemma 3.1 and Theorem 3.6, both `PROVED` above.

### 3.4 What is classical, what is row A–C, and what is row D

**Remark 3.8 (the ledger of Theorem 3.7).**

1. `CLASSICAL`, named: Weil's criterion (the direction (a)⇒(b) is the
   computation just given; the converse direction is Paper 45 Theorem 10.4,
   `PROVED-IN-REPOSITORY`); the Bochner–Schwartz theorem; SNAG/Stone; GNS.
   None of them is new and none of them is asserted to be.
2. `PROVED-IN-REPOSITORY`, row A–C content: the group in (e) is not an
   abstract copy of `R` — it is the **modulus group of the carrier** `C_S`
   (1.2), its action is the archimedean Frobenius flow `Frob_∞` (1.5), the
   distribution `𝔏` is built from the Gram form of the **unit-averaged
   Frobenius family** `Frob ⋆ Δ^{rad}` (1.6), and the constant `c = 0` in it
   is forced (Paper 45 Corollary 9.6a(iii)), not chosen — indeed, by minor
   `(m1)` above, `c = 0` *is* the choice of finite part in (3.2).
   **[REBUILT, round 2, `LF2` and the adversarial audit §2.  Round 1 called this
   "what the equivalence gains over the textbook statement".  That claim is
   **withdrawn**, and it is withdrawn on evidence: **no proof in this paper
   uses the identification of the group with the carrier's modulus group, or
   of the flow with `Frob_∞`, for anything but naming.**  Deleting the
   identification from §3 changes no proof in §3 and no proof anywhere else in
   the paper; the auditor searched for such a use independently and found
   none, and so did the construction.  The identification is a **typing of the
   answer**, not an ingredient of any argument, and that is exactly why
   Theorem 3.7 is graded `RESTATEMENT`.]**
3. `PROVED` here, and these are the only two: Lemma 3.1 (`Π` is **onto** `P_T`)
   and Theorem 3.6 (the explicit `D'`-distribution, the `Π²` intertwiner, and
   `Π²ϖ = 0`), with Proposition 3.6a showing that the temperedness route is
   unavailable.
4. **`OPEN`, and it is row D.**  Theorem 3.7 says the missing nonnegative
   invariant of `PANEL_3` §5 has a **name and a type**: it is a squared norm
   in a unitary representation of the modulus group, and the missing functor
   is the one producing `(H,π,Ω)` from the correspondence theory **without**
   using (a).  **Constructing that Hilbert space is row D, and it is not done
   here.**  Nothing in §3 is evidence for or against any sign.

**Remark 3.9 (why this is not circular, and why it is not free).**  The
inverse-semigroup structure (1.5) — `Frob_n ⋆ Frob_n^† = Δ^{(n)}`, the
Frobenii are partial isometries of the convolution algebra — would make the
Gram matrix of the family positive semidefinite **in any positive functional
on the algebra**.  The content of row D is that the declared trace is **not**
a positive functional (its symbol is indefinite with infinite index on both
sides, Theorem 14.1), and that `−T_∞` must nevertheless be positive on the
primitive radial sector in the colimit.  Two observations keep this honest:

* The primitive sector is **not** a `⋆`-subalgebra: `M` is an algebra map
  (Paper 45 Theorem 8.1), so `M(Γ_F ⋆ Γ_G) = M(Γ_F)M(Γ_G)` and the primitive
  classes form an **ideal**, not a unital subalgebra containing `Δ`; no GNS
  construction applies to `−T_∞|_{prim}` directly, and Theorem 3.7(e) obtains
  its representation from Bochner, i.e. from the conclusion, not from the
  algebra.  **[This is the precise reason the reformulation is not a
  proof.]**
* The blueprint's §1 item 3 sentence — "in any positive functional their Gram
  matrix would be positive semidefinite for free" — is true but has **nothing
  to do with the partial isometry property**: it holds for the Gram matrix of
  **any** family in any positive functional.  `REPAIRED`, as a matter of
  attribution: the partial-isometry theorem 3ter.6 is used nowhere in §3.

---

## 4. D.2 — the dichotomy on the true carrier, and the Schur complement

### 4.1 The bordered form

**Theorem 4.1 (the bordered form and the shielding dichotomy;
`PROVED-IN-REPOSITORY`, P124.013 Theorem 3.1, restated with its hypotheses on
the carrier of (1.1)).**  Fix `T > \log 2`.  In `L²(I_T)` let
`φ_σ(t) = e^{σt/2}\mathbf 1_{I_T}`, `σ = ±`, the Riesz representers of the
two Tate moments, and let `Q_T = P_T ⊕ 𝒯_T`, `𝒯_T = span\{φ_+,φ_-\}`.  Then
the **unconstrained** Weil form on `Q_T` is the bordered form
`[[L_T,X_T],[X_T^*,𝔅_T]]` with `L_T = P_T𝒜_TP_T` the primitive (row-D)
operator, `X_T` the **Tate collar**, `(X_T)_σ(F_0) = ⟨ρ_{σ,T},F_0⟩`, and
`𝔅_T` the Tate **block** — **not** `B_T`, see §4.2 and (1.8) — and `𝒲 ≥ 0`
on `Q_T` iff `L_T ≥ 0`, `Π_{\ker L_T}X_T = 0` and
`Σ(T) := 𝔅_T − X_T^*L_T^†X_T ≥ 0`.  If, in
addition, `T_q < ∞` and `K_{T_q} = \ker L_{T_q}∩P_{T_q} ≠ \{0\}`, then exactly
one of: (1) **Gate R** holds at `T_q`; (2) **shielding** — `𝒲` is indefinite
on `Q_{T_q}`.

**Hypothesis carried, and it is decisive.**  The dichotomy is **conditional on
`T_q < ∞`**.  For `ζ`, `T_q < ∞` is equivalent to the failure of the target
(P124.013 Lemma 1.2 and (1.10)); so **Theorem 4.1 has no content for `ζ`
unless row D's target fails**, and it may never be cited as if it had.  It has
content for models where a first contact exists, which is §7's role.

*Proof.*  P124.013 §§1–3 verbatim; the only transport needed is the
identification of `𝒲` with the comparison theorem's right-hand side, which is
(1.9), and of the primitive space with (1.7).  ∎
`PROVED-IN-REPOSITORY`

### 4.2 The Tate block `𝔅_T` is not the hyperbolic Tate plane `B_T`

**`REFUTED` (blueprint D.2).**  The blueprint says "`B_T` [is] Paper 43's
hyperbolic Tate plane (Paper 45 Thm 8.1)".  **False**, for two independent
reasons, and the confusion is a conflation of three different two-dimensional
objects: the ruling plane `B_T = C⊕C` with the form `β_T` (Paper 45
Theorem 8.1); the border `𝒯_T = span\{φ_+,φ_-\} ⊂ L²(I_T)`; and the Tate
**block** of the Weil form on `𝒯_T`, which P124.013 (2.3) **also** calls
`B_T`.  **This paper writes `𝔅_T` for the block and reserves `B_T` for the
ruling plane of (1.8), throughout; the collision of letters is the whole
subject of this subsection and may not be perpetuated by it.**

**Theorem 4.2 (`PROVED`).**  In the border basis `(φ_+,φ_-)`:

  (i) the **polar** part of the Tate block is the pullback of `β_T` along `M`,
      with matrix, by (1.8) and P124.013 (2.3),

          β_T(M Γ_{φ_σ}, M Γ_{φ_τ}) :  \begin{pmatrix} 8T\sinh T &
            4T² + 4\sinh²T \\ 4T²+4\sinh²T & 8T\sinh T\end{pmatrix} ,   (4.1)

      whose determinant is `64T²\sinh²T − 16(T²+\sinh²T)² = −16(T²−\sinh²T)²
      < 0` for `T > 0`.  So the polar part **is** a hyperbolic plane as a
      form, but its matrix is **not** `[[0,1],[1,0]]`: the border vectors
      `φ_±` are not the rulings `e_∓`, and `M(Γ_{φ_+}) = (2\sinh T, 2T)`,
      `M(Γ_{φ_-}) = (2T, 2\sinh T)` are not basis vectors of `B_T`;
  (ii) the Tate **block** is `𝔅_T = (4.1) + [⟨𝒜_Tφ_σ,φ_τ⟩]`, and the second
      summand is not zero;
  (iii) consequently `𝔅_T` need not be hyperbolic, and is not: at
      `T = 0.72` the computed block has `\det 𝔅_T > 0` and positive trace —
      **positive definite**, hence of signature `(2,0)`, not `(1,1)` — and
      the determinant is **stable under refinement**, which the individual
      entries are not:

      | `refine` | `dim P` | `𝔅_T` diagonal | `𝔅_T` off-diagonal | `\det 𝔅_T` |
      |---|---|---|---|---|
      | 2 | 6 | `0.11264` | `0.07670` | `+6.805·10^{−3}` |
      | 3 | 10 | `0.11124` | `0.08402` | `+5.315·10^{−3}` |
      | 4 | 14 | `0.11181` | `0.08414` | `+5.422·10^{−3}` |
      | 5 | 18 | `0.11152` | `0.08522` | `+5.174·10^{−3}` |
      | 6 | 22 | `0.11175` | `0.08538` | `+5.198·10^{−3}` |

      **[REBUILT, round 2, minor `(m8)` of `R134.002`: round 1 printed the
      `refine = 2` matrix without a resolution caveat, and its off-diagonal
      moves by 11% to `refine = 6`.  The conclusion survives — the determinant
      is positive at every resolution and has settled to three digits by
      `refine = 4` — but the *entries* may not be quoted as converged.]**

*Proof.*  (i) `Φ_{φ_+}(1) = ∫_{I_T}e^t dt = 2\sinh T`,
`Φ_{φ_+}(0) = ∫_{I_T}dt = 2T`, and symmetrically for `φ_-`; insert into
`β_T(z,w) = z_-\overline{w_+} + z_+\overline{w_-}` with
`M(Γ_F) = (Φ_F(1),Φ_F(0))` (1.8).  The determinant identity is algebra.  (ii)
is P124.013 (2.3).  (iii) the matrix is the output of
`scripts/d134_sigma.py --model zeta`, at `refine = 2`, `T = 0.72`; its sign is
`COMPUTATIONAL-ILLUSTRATION`, and it is the *falsifying* use of numerics
permitted by the rules: it exhibits a `T` at which the blueprint's identity
would force `\det 𝔅_T < 0`, while the computed determinant is positive at
every resolution tested.  **The variational caveat of §9.3(2) is stated and
does not weaken this use:** a Galerkin computation of `𝔅_T` is not an
eigenvalue infimum at all — `𝔅_T` is assembled from *exact* integrals
(`gamma_form`, `shift_form`, `exp_moments`) of the two **explicitly known**
border functions `φ_±`, which lie in the Galerkin space only up to the
piecewise-constant approximation of `e^{±t/2}`; the sweep above is the test of
that approximation, and it passes.  ∎  `PROVED`
for (i), (ii); `COMPUTATIONAL-ILLUSTRATION` for (iii)

**Corrected statement.**  *The hyperbolic Tate plane of Paper 45 Theorem 8.1
is the **polar summand** of the Tate block, pulled back along `M`; the Tate
block itself is that summand plus `⟨𝒜_Tφ_·,φ_·⟩` and has no predetermined
signature.*

### 4.3 The swap law for `Σ(T)`

This is the one structural gain of §4.

**Theorem 4.3 (the swap law; `PROVED`).**  Let `R : F(t) ↦ F(−t)` on
`L²(I_T)`.  Then `R` is a unitary involution preserving `I_T`, preserving the
unconstrained Weil form `𝒲`, preserving `P_T`, and exchanging `φ_+ ↔ φ_-`.
Consequently, whenever `L_T > 0`:

    Σ(T) = σ\,Σ(T)\,σ ,   σ = \begin{pmatrix}0&1\\1&0\end{pmatrix} ,   (4.2)

i.e. `Σ(T) = [[α(T), β(T)],[β(T), α(T)]]` with equal diagonal entries; its
eigenvectors are the **even** vector `(1,1)` and the **odd** vector `(1,−1)`,
with eigenvalues `α ± β`, and

    Σ(T) ≥ 0  ⟺  α(T) ≥ |β(T)| .                                      (4.3)

*Proof.*  `𝒲` is `R`-invariant term by term: the polar packet is
`2Φ_F(0)Φ_F(1)` and `Φ_{RF}(s) = Φ_F(1−s)`, so the product is exchanged with
itself; `W_{fin}` is symmetric under `t ↦ −t` by (1.4); `ω_∞ = K(|t|)dt` is
even; and the Gamma multiplier `\log π − \mathrm{Re}ψ(¼+iτ/2)` is even in `τ`
(Paper 43 Theorem 9.7), so `𝒜_T` commutes with `R`.  `R` preserves `P_T`
because `Φ_{RF}(0) = Φ_F(1)` and `Φ_{RF}(1) = Φ_F(0)`, and exchanges `φ_±`
because `φ_σ(−t) = φ_{−σ}(t)`.  Write `U := R|_{P_T}`, a unitary involution of
`P_T`; in the border basis `(φ_+,φ_-)`, `R` acts by `σ`.  `R`-invariance of
`𝒲` gives, entry by entry,

    U^{*}L_TU = L_T ,   𝔅_T = σ𝔅_Tσ ,   and   X_T = U^{*}X_Tσ ,

the last because `(U^*X_Tσ)_{·,σ'} = 𝒲(U\,·\,,φ_{−σ'}) = 𝒲(·,φ_{σ'}) =
(X_T)_{·,σ'}`.  Hence `X_Tσ = UX_T`, and

    σ\,X_T^{*}L_T^{−1}X_T\,σ = (X_Tσ)^{*}L_T^{−1}(X_Tσ)
      = X_T^{*}U^{*}L_T^{−1}U X_T = X_T^{*}L_T^{−1}X_T ,

using `U^*L_T^{−1}U = L_T^{−1}`, which follows from `U^*L_TU = L_T` and
`U^{-1} = U^{*}`.  With `σ𝔅_Tσ = 𝔅_T` this gives `σΣ(T)σ = Σ(T)`, which is
(4.2).  (4.3) is the spectral decomposition of a symmetric Toeplitz
`2×2`.  ∎  `PROVED`

**Verification (`COMPUTATIONAL-ILLUSTRATION`).**  *(This is a check on an
identity, not on a sign, so §9.3(2)'s variational caveat does not bear on it:
a congruence-covariance defect is scale-free and is measured relative to
`‖Σ‖_∞`.)*
`scripts/d134_sigma.py` measures `‖σΣσ − Σ‖_∞/‖Σ‖_∞` and finds it
`≤ 4.2·10^{−13}` for `ζ` at every `T ∈ [0.72, 2.2]`, and `≤ 2.2·10^{−13}` for
`Ξ_{0.35}` on the four-dimensional border (where `σ` is the block exchange of
`u ↔ −u`), at every `T ∈ [0.72,1.9]`.  At `T = 0.72` for `ζ`:
`Σ = [[0.07640, 0.05055],[0.05055, 0.07640]]`.

**Corollary 4.4 (`PROVED`).**  The constraint-free target (3.2) of P124.013 —
`Σ(T) ≥ 0` for all `T < T_q` — is equivalent to the **two scalar
inequalities** `α(T) − β(T) ≥ 0` and `α(T) + β(T) ≥ 0`, i.e. to
non-negativity of `𝒲` separately on the **even** and **odd** completions of
the primitive sector by one border direction each.  In particular it splits
along the parity decomposition that Paper 45 Theorem 10.4 also uses.

**Honest remark 4.5.**  Corollary 4.4 is a **reduction of the shape of the
statement, not progress toward it**.  `Σ(T) ≥ 0` for all `T < T_q` is, by
Theorem 4.1, Weil positivity of the **unconstrained** form up to `T_q`; it is
RH-strength and it is not a shortcut.  No sign is claimed for `α ± β`.

**Warning 4.5a (the variational caveat, applied to this paper's own §4
numerics).**  **[NEW, round 2, finding `(M6)` of `R134.002`.  Round 1 stated
the finding of §9.3(2) against phases 118–124 and did not apply it to §4.]**
`d134_sigma.py` uses `p124_lab.assemble` unchanged, i.e. the same
piecewise-constant Galerkin space.  Both `λ_{\min}(L_T)` **and** `Σ(T)` are
therefore variational **upper bounds**: `L_T`'s least eigenvalue is a minimum
of a Rayleigh quotient over a **subspace** of `P_T`, and
`Σ_T(z) = \inf\{𝒲(F+φ_z) : F ∈ P_T\}` is likewise an infimum, computed over a
subspace, hence `≥` the true value.  A resolution sweep at `T = 0.72` confirms
it: `λ_{\min}Σ = 2.585, 1.327, 1.189, 0.925, 0.789` (`×10^{−2}`) and
`λ_{\min}(L_T) = 2.949, 2.786, 1.724, 1.291, 1.023` (`×10^{−1}`) at
`refine = 2,…,6`, decreasing at every step in both columns.  **Consequently
every positive value of `λ_{\min}Σ(T)` or `λ_{\min}(L_T)` reported in §4.3 and
§4.4 certifies nothing, and Corollary 4.4's two scalar inequalities are not
being tested by these numbers.**  What the numbers do carry — an identity
check (the swap defect), a determinant of an exactly assembled `2×2`
(Theorem 4.2(iii)), and a *sign pattern of differences* (Observation 4.7) —
is stated in those places and nowhere else.

### 4.4 Monotonicity in `T` fails

**`REFUTED` (blueprint D.2, "its behaviour under `T ↦ T+ε` (monotonicity or
its failure)"): monotonicity is not available, and the numerics do not show
it.**

**Theorem 4.6 (`PROVED`).**  For `T < T'` with `L_{T'} > 0`, let
`φ_σ^{(T)}`, `φ_σ^{(T')}` be the border vectors of the two windows and
`δφ_σ := φ_σ^{(T')} − φ_σ^{(T)}`, supported in `T < |t| < T'`.  Then, with
`Σ_T(z) := \inf\{𝒲(F + φ^{(T)}_z) : F ∈ P_T\}` (the variational form of the
Schur complement),

    Σ_{T'}(z) ≤ Σ_T(z) + 2\,𝒲(φ^{(T)}_z, δφ_z) + 𝒲(δφ_z, δφ_z) ,      (4.4)

and **no inequality in either direction follows without controlling the two
correction terms**, which are not of one sign.  In particular the standard
Schur monotonicity argument — `P_T ⊆ P_{T'}` implies the infimum decreases —
does **not** apply, because the border vectors move with the window.

*Proof.*  `Σ_T(z) = 𝒲(F_*+φ^{(T)}_z)` for the minimizer `F_*` (`L_T>0`);
`F_* ∈ P_T ⊆ P_{T'}` by P124.013 Lemma 1.2, and
`φ^{(T')}_z = φ^{(T)}_z + δφ_z`, so `F_*` is admissible for the `T'` infimum
with value the right-hand side of (4.4).  The variational identity for the
Schur complement of a positive `(1,1)` block is the closed-form Schur/Douglas
statement, import **(X7)**.  ∎  `PROVED`

**Observation 4.7 (`COMPUTATIONAL-ILLUSTRATION`).**  `λ_{\min}Σ(T)` is **not
monotone** in `T` for `ζ`, in either of two bases of the border.  In the named
basis `(φ_+,φ_-)` at `refine = 2`, over `T = 0.72 … 2.2`:
`2.58, 1.83, 2.75, 3.45, 3.02, 2.30, 2.43, 1.74` (units `10^{−2}`); in the
Gram-orthonormalized basis used by P124.014, over `T = 1.55…1.76`:
`4.23, 3.88, 3.66, 2.96, 2.77, 2.91, 3.08, 3.14` (units `10^{−3}`).  Both
sequences fall and rise.  **[Round 2: the adversarial auditor re-ran the first
sequence at `refine = 5` and obtained `9.25, 8.29, 10.03, 10.25, 7.90, 6.60,
8.98, 5.30` (units `10^{−3}`) — the **same** sign pattern of successive
differences, `−,+,+,−,−,+,−`, across a `3×` shift in absolute values, and not
tracking the jumps in `\dim P`.  So the non-monotonicity is reproducible and
is not a discretization artifact.  By Warning 4.5a the absolute values carry
nothing and are not quoted as such; the *pattern of differences* is what is
reported, and it is stable.]**  P124.014's control table (`λ_{\min}Σ` "decreasing
from `6.8·10^{−2}` to `9.0·10^{−4}`") reports endpoints of a coarser scan and
is not a monotonicity statement; it should not be read as one.

**Finding 4.8 (what is and is not invariant in P124.013 Corollary 3.3;
`PROVED`).**  **[REBUILT, round 2, finding `(M5)` of `R134.002`, which
**partially refutes** round 1's version of this finding.  Round 1 asserted
that Corollary 3.3's criterion is "basis-dependent as stated".  **That is
wrong**, and here is why, followed by what survives.]**

  (i) *What round 1 got wrong.*  P124.013 Corollary 3.3's criterion is
      `\liminf_{T↑T_*}λ_{\min}Σ(T) > −∞` at a **finite** `T_* = T_q`.  A change
      of border basis replaces `Σ(T)` by `C(T)^{\mathsf T}Σ(T)C(T)` with `C`
      continuous and nonsingular; on a neighbourhood of a **finite** `T_*` the
      condition numbers `\|C\|\,\|C^{−1}\|` are **bounded**, so
      `λ_{\min} ≥ −M` on one side iff on the other, and the criterion
      `\liminf > −∞` is **invariant**.  The two bases this paper compares —
      the named `(φ_+,φ_-)` and the Gram-orthonormalized one — differ by
      exactly such a `C(T)` (`‖φ_σ‖_{L²} ∼ e^{T/2}`, bounded near a finite
      `T_*`).  **Round 1's claim is withdrawn.**
  (ii) *What survives, and it is enough for the recommendation.*  The
      **numerical value** `λ_{\min}Σ(T)` is not a congruence invariant and may
      not be quoted, compared across bases, or compared across papers.  The
      two bases give, at the same `T` and the same resolution, values
      differing by an order of magnitude: at `T = 1.67`, `2.77·10^{−3}`
      (orthonormalized) against `2.35·10^{−2}` (named).  Both are correct;
      neither is a property of the form.
  (iii) *What is invariant.*  `Σ(T) ≥ 0`, the boxed target (3.2) of P124.013,
      is a congruence invariant, as is the inertia of `Σ(T)` and the sign of
      `\det Σ(T)`.

*Proof.*  (i) Let `Σ` be symmetric with `λ_{\min}(Σ) ≤ 0` and `C`
nonsingular.  For a unit vector `x`,
`x^{\mathsf T}C^{\mathsf T}ΣCx = (Cx)^{\mathsf T}Σ(Cx) ≥ λ_{\min}(Σ)\,|Cx|^2
≥ λ_{\min}(Σ)\,\|C\|^2` (the last step reversing because `λ_{\min}(Σ) ≤ 0`), so
`λ_{\min}(C^{\mathsf T}ΣC) ≥ \|C\|^2\,λ_{\min}(Σ)`, and symmetrically with
`C^{−1}`.  On a compact neighbourhood of a **finite** `T_*` the continuous
functions `\|C(T)\|` and `\|C(T)^{−1}\|` are bounded, so `λ_{\min}` is bounded
below in one basis iff in the other.  (ii) is the displayed
computation, `scripts/d134_sigma.py` against `p124_lab.blocks`.  (iii) is
Sylvester's law of inertia.  ∎  `PROVED`

*Recommendation to the corpus, on the corrected ground:* **carry
`Σ(T) ≥ 0`** (P124.013 (3.2)); quote `λ_{\min}Σ(T)` only with its border
normalization named, and never across papers.  This is weaker than round 1's
recommendation in its reason and identical in its content.

---

## 5. D.3 — finite inertia theorems

### 5.1 The object

**Definition 5.1.**  Fix `N ≥ 2`, a width `ε > 0` and a real even profile
`φ ∈ C_c(R)` with `∫φ = 1` and `supp φ ⊆ [−ε,ε]`.  For `2 ≤ n ≤ N` put
`h_n(t) := φ_ε(t − \log n)` and `Γ_n^{rad,sm} := Γ_{h_n}` (1.3), and let

    G_N(ε)_{mn} := I_∞\big(Γ_m^{rad,sm}, Γ_n^{rad,sm}\big) ,
    Δ_{mn} = \log m − \log n ,  ψ_ε := φ_ε ⋆ φ_ε^† ,                  (5.1)

the pairing being the one of Paper 43 Definition 9.2 in the colimit, evaluated
by Paper 45 **Lemma 5.1a** as in (a) below.  **[REBUILT, round 2, `(M2)`:
round 1 displayed the entry as `∫ψ_ε(t−Δ_{mn})\,d(W_{fin}+ω_∞)`.  That integral
**diverges** whenever `0 ∈ supp ψ_ε(·−Δ_{mn})`, because `K(t) ∼ 1/2t`, which is
the case for every diagonal entry and, at `ε ≥ 0.5`, for essentially every
off-diagonal entry as well.  The entry is well defined for every `ε`; the
*formula* round 1 used for it was not.]**

**The attribution, corrected.**  **[REBUILT, round 2, finding `(M2)` of
`R134.002`.  Round 1 cited Paper 44 Theorem 8bis.1e for (5.1) "in its integral
form (8bis.6), which carries **no** width hypothesis".  **That was wrong on
two counts**: 8bis.1e carries the width hypothesis `ε < ε_0(A,S)` **in its own
statement**, and its proof runs through Paper 44 Theorem 3bis.7, which assumes
`0 ∉ supp(h_m⋆h_n^†)`.  Both hypotheses **fail over the whole informative
window** `ε ≥ 0.5` of the §5.4 table — at `ε = 2.0, 1.0, 0.5` essentially every
pair has `0 ∈ supp(h_m⋆h_n^†)`, where `ω_∞ = K(|t|)dt` is not integrable
(`K(t) ∼ 1/2t`), so the displayed integral does not converge.  **The numbers
survive verbatim; the citation does not.**  Here is the correct one.]**

  (a) **What defines the entries, for every `ε`, with no support and no width
      hypothesis: Paper 45 Lemma 5.1a** (the radial trace, `c := 0`, colimit
      form by Paper 43 Theorem 8A.7c and `(C1)`).  For **arbitrary**
      `h ∈ C_c^∞(R)`,

          T_∞(Γ_h) = Σ_{n≥2}Λ(n)\,n^{−1/2}\big[h(\log n)+h(−\log n)\big]
                     + \frac1{2π}∫_R \hat h(−τ)\,\hat W_∞(0,τ)\,dτ ,   (5.1a)

      the finite part a **finite** sum, the archimedean part an absolutely
      convergent integral.  Lemma 5.1a was written in Paper 45 for exactly this
      situation — its own preamble records that `h = F⋆F^†` always has
      `h(0) = ‖F‖²_{L²} > 0`, so `0 ∈ supp h` **always**, and that Theorem
      3bis.7 may **not** be cited there.  Equivalently, in `τ`-space, (5.1a) is
      Paper 43 **(14.1)** with `c = 0`.  This is precisely what
      `scripts/d134_gram.py` computes: finite atoms in `t`-space, archimedean
      half by quadrature against `\hat W_∞(0,τ)`.
  (b) **The entries of `G_N(ε)` are then defined by polarization**,
      `G_{mn} := ¼\big[Q(h_m+h_n) − Q(h_m−h_n)\big]`,
      `Q(f) := I_∞(Γ_f,Γ_f) = T_∞(Γ_{f⋆f^†})`, which is legitimate for every
      `ε` because `Q` is a quadratic form on `C_c^∞(R)` by (a).
  (c) **Paper 44 Theorem 8bis.1e is cited for the *interpretation* only**, and
      only where its hypotheses hold: it is what says the entries are the Gram
      form of the **unit-averaged Frobenius family** `Frob ⋆ Δ^{rad}`, in the
      concentrated reading (8bis.7)
      `W_{fin}(\{Δ_{mn}\}) + K(|Δ_{mn}|)`, valid when `ε < ε_0(A,S)` and
      `0 ∉ supp(h_m⋆h_n^†)`; for `A = \{2,…,N\}` this needs
      `2ε < \min_{m≠n}\big|\,|Δ_{mn}| − \log n'\,\big|` and
      `2ε < \min_{m≠n}|Δ_{mn}| = \log\frac{N}{N−1}`, i.e. `ε = O(1/N)`.
      **In the §5.4 table this holds at no tested `(N,ε)`**; see the regime
      column there.  Remark 5.9(2) draws the consequence.
  (d) **`(C1)` and the exemption.**  (5.1a) is read in the colimit, so
      `W_{fin}` is the kernel over **all** primes.  Paper 44 Theorem 8bis.2 —
      used only in Theorem 5.8, and only for the **archimedean** diagonal —
      is `(C1)`-exempt; in Theorem 5.8's own regime `2ε < \log 2` no finite
      atom reaches the diagonal, so the constant that is used is **purely
      archimedean** and no chart quantity enters (minors `(m3)`, `(m4)` of
      `R134.002`).

Write `G_N^{prim}(ε)` for the compression to the primitive subspace.

**Theorem 5.2 (the primitive subspace is `ε`-free and has codimension exactly
`2`; `PROVED`).**  For `c ∈ R^{N−1}` the class `Γ_g`,
`g = Σ_{n=2}^N c_n h_n`, is primitive iff

    Σ_{n=2}^N c_n\,n^{1/2} = 0  \quad\text{and}\quad
    Σ_{n=2}^N c_n\,n^{−1/2} = 0 .                                      (5.2)

These two conditions do not depend on `ε` or on the profile `φ`, and they are
linearly independent for `N ≥ 3`; so the codimension is exactly `2` for
`N ≥ 3`, and for `N = 2` the primitive subspace is `\{0\}`.

*Proof.*  **[REBUILT, round 2, minor `(m5)` of `R134.002`: round 1's proof
contained a clause that was not a sentence.  The argument is unchanged.]**
By (1.3), `λ_∓(Γ_{h_n}) = ∫h_n(s)e^{±s/2}ds =
n^{±1/2}∫φ_ε(u)e^{±u/2}du = n^{±1/2}κ_∓(ε)`, where

    κ_∓(ε) := ∫_R φ_ε(u)\,e^{±u/2}\,du

depends on the profile and on the width but **not** on `n`.  It is nonzero:
for `φ_ε ≥ 0` (the case of the scripts) the integrand is nonnegative and not
a.e. zero, so `κ_∓(ε) > 0`; for a general real profile with `∫φ_ε = 1`,
`κ_∓(ε) → 1` as `ε → 0`, so `κ_∓(ε) ≠ 0` for small `ε`.  Dividing the two
conditions `λ_∓(Γ_g) = 0` by `κ_∓(ε)` gives (5.2).  The two vectors
`(n^{1/2})_n` and `(n^{−1/2})_n` are proportional only if `n ↦ n` is constant
on `\{2,…,N\}`, false for `N ≥ 3`.  ∎  `PROVED`

**Remark 5.3.**  (5.2) is the exact finite shadow of the two Tate conditions
(1.7); it is the statement that the coefficient vector is orthogonal to the
two ruling characters.  The blueprint's "codimension `≤ 2`" is correct;
Theorem 5.2 makes it exact and `ε`-free, which is what the numerics need.

### 5.2 The claim that Theorem 14.1 transports — refuted

**`REFUTED` (blueprint D.3(a)).**  The blueprint asks to prove "at a fixed
finite chart the inertia [of `G_N^{prim}`] is indefinite for large `N`
(Paper 43 Thm 14.1 transported — or refute this and record it)".  **It is
refuted, and the refutation is carried by Theorem 5.5.**  Remark 5.4 records
separately, and more weakly than round 1 did, in what sense 14.1's own
mechanism is unavailable.

**Remark 5.4 (the mechanism of 14.1 is not literally available on this family;
two valid observations, and one `OPEN` question).**  **[DOWNGRADED FROM A
THEOREM, round 2, finding `(M4)` of `R134.002`.  Round 1's Theorem 5.4 argued
that no element of the span can concentrate because "the Dirichlet factor
`Σc_nn^{−iτ}` is almost periodic, hence cannot concentrate".  **That step is an
assertion, not an estimate, and is very likely false in the form that
matters**: a Dirichlet polynomial resonates — `c_n = a_nn^{iτ_0}` produces a
Dirichlet-kernel peak at `τ_0` of height `Σ|a_n|` and width `∼1/\log N` — and
against the *fixed*, only polynomially decaying envelope `|\hatφ_ε|` such a
peak can carry an arbitrarily large share of the weighted mass, since
`Σ|c_n|` is free.  The bound `|\hat F| ≤ |\hatφ_ε|Σ|c_n|` does not exclude it.
The refutation of blueprint D.3(a) is therefore carried by **Theorem 5.5
alone**, which is unaffected.]**  What is true, and is all that is used:

  (i) *At fixed `N` and `ε` the span is `(N−1)`-dimensional*, so
      Theorem 14.1(a),(b) — whose conclusions are about
      **infinite-dimensional** definite subspaces — are vacuous on it, for
      trivial reasons of dimension.
  (ii) *The concentration profiles are not elements of the span.*  14.1's
      construction uses `φ_{a,δ}(t) = δ^{−1/2}e^{iat}φ_0(t/δ)`, `a,δ → ∞`;
      every element of `span\{Γ_n^{rad,sm}\}_{n≤N}` has
      `\hat F(τ) = \hatφ_ε(τ)Σ_{n≤N}c_nn^{−iτ}` (5.3), which is not of that
      form for any `c`.  So 14.1's proof does not apply verbatim.
  (iii) **`OPEN`:** whether the mechanism revives in the colimit `N → ∞` with
      `ε = ε(N) → 0`.  Round 1 asserted it does not; that assertion is
      **withdrawn**.  By Theorem 5.5 the question may not be answered in
      either direction here, since one answer would negate row D's target.

    \hat F(τ) = \hatφ_ε(τ)\,Σ_{n≤N}c_n\,n^{−iτ} .                      (5.3)

**Theorem 5.5 (the conclusion is, moreover, inconsistent with the target;
`PROVED`).**  Under convention `(C1)` — the colimit kernel, which (5.1) uses —
the assertion "`G_N^{prim}(ε)` is indefinite for large `N`" **implies the
negation of row D's target**, by Theorem 5.6 below.  So it may not be proved,
and asserting it would be asserting a statement about the zeros that this
paper is forbidden to make.  At a *fixed finite chart* the assertion is not
inconsistent — but then the kernel of (5.1) is not the Weil kernel, Paper 44
Theorem 8bis.1e holds only inside the window `\{|t| < \log ℓ_{next}(S)\}`, and
the family `\{Γ_n^{rad,sm}\}_{n ≤ N}` leaves that window as soon as
`\log N > \log ℓ_{next}(S)`.  **So the blueprint's D.3(a) is either
inconsistent with the target (colimit reading) or outside the range of
validity of its own kernel formula (chart reading).**  ∎  `PROVED`

### 5.3 What is provable

**Theorem 5.6 (= blueprint D.3(c); `PROVED`).**  Assume RH.  Then for every
`N ≥ 2`, every `ε > 0` and every real profile `φ ∈ C_c^∞`,
`G_N^{prim}(ε) ≤ 0`.

*Proof.*  A primitive coefficient vector gives a primitive radial class
`Γ_g`, `g` real and `C_c^∞`; by (9.10),
`c^{\mathsf T}G_N^{prim}(ε)c = I_∞(Γ_g,Γ_g) = −Σ_ρΦ_g(ρ)Φ_g(1−ρ)`, and under
RH the sum is `Σ_γ|Φ_g(½+iγ)|² ≥ 0` as in Theorem 3.7(a)⇒(b).  ∎  `PROVED`
(conditionally on RH, which is the hypothesis of the statement)

**Remark 5.7.**  The converse is `OPEN`.  It is not merely unproved: by
Theorem 5.2 the family is a **Dirichlet-polynomial profile class** in the
sense of Paper 44 §8bis.4, so the converse is exactly the question
Theorem 8bis.7 leaves open — `(a)` is `PROVED` only under `(H_L)`, `(b)` is
`CLASSICAL`, `(c)` — whether the negative test can be taken in a moving
window with `R(L) → 0` — is `OPEN`.  The withdrawn import `(Wgr)`
(Lemma 8bis.6b) must not be reintroduced here.  And by Theorem 5.8(b) the
class contains, for each `N`, a whole regime `ε < ε_1(N)` in which the
inequality is **automatic**; so the converse is, if anything, harder than
8bis.7(c), not easier.

**Theorem 5.8 (the `ε → 0` asymptotics, and unconditional negative
definiteness at small `ε`; `PROVED`).**  Fix `N` and a profile `φ`, and put
`c_φ := ε\,ψ_ε(0) = ‖φ_1‖_{L²}²` (`c_φ = 2/3` for the triangular profile of
the scripts).  Then, as `ε → 0^+`,

    G_N(ε) = \frac{c_φ}{ε}\Big[\,-\big(\log\tfrac1ε - C_{φ}\big)\,I
             + A'_N \,\Big] + o\!\big(\tfrac1ε\big) ,                   (5.4)
    (A'_N)_{mn} = \begin{cases} Λ(r)\,r^{−1/2} & m ≠ n,\ m/n = r^{±1},
        \ r\ \text{a prime power},\\ 0 & \text{otherwise,}\end{cases}

where `C_φ` is the profile-and-model constant of Paper 44 (8bis.4c).
Consequently:

  (a) the **diagonal diverges like `−c_φ\,ε^{−1}\log(1/ε)`**, one factor of
      `\log(1/ε)` **faster** than every off-diagonal entry, which is
      `c_φ ε^{−1}(A'_N)_{mn} + O(1)`;
  (b) hence, with `r_N := \max_m Σ_{n≠m}(A'_N)_{mn} < ∞`, for every
      `ε < ε_1(N) := \exp\big(−C_φ − r_N − 1\big)` the matrix `G_N(ε)` is
      **negative definite** — by Gershgorin — and a fortiori
      `G_N^{prim}(ε) < 0`.  **This is unconditional: no hypothesis about
      zeros is used**;
  (c) the same argument, with the same proof, applies verbatim to `Ξ_a`
      (`c_φ` doubles, `A'_N` acquires the factor `n^a+n^{−a}`, `r_N` stays
      finite), so `G_N^{prim}(ε)` is negative definite for `Ξ_a` as well once
      `ε < ε_1^{(a)}(N)`.

*Proof.*  The finite half of (5.1) is `Σ_{n'≥2}w_{n'}[ψ_ε(Δ_{mn}−\log n') +
ψ_ε(Δ_{mn}+\log n')]`, `w_{n'} = Λ(n')n'^{−1/2}`, a **finite** sum because
`ψ_ε` is compactly supported; it equals `ε^{−1}c_φ w_{n'} + o(ε^{−1})` when
`Δ_{mn} = ±\log n'` and `O(1)` otherwise, and it vanishes on the diagonal
because `Λ(1) = 0`.  The archimedean half is
`(2π)^{−1}∫\hatω(τ)|\hatφ_ε(τ)|²\cos(τΔ)dτ`; for `Δ ≠ 0` it converges to
`K(|Δ|)`, bounded on the finite set of pairs.  For `Δ = 0`, substitute
`σ = ετ` and use the symbol asymptotics
`\hatω(τ) = −\log|τ| + \log 2π + O(|τ|^{−1})` of Paper 44 (8bis.8):

    \frac1{2π}∫\hatω(τ)|\hatφ_ε(τ)|²dτ
      = \frac1{2πε}∫\hatω(σ/ε)\,|\hatφ_1(σ)|²\,dσ
      = \frac{1}{ε}\Big[-\log\tfrac1ε\,\|φ_1\|_{L²}^2 + O(1)\Big] ,

since `(2π)^{−1}∫|\hatφ_1|² = ‖φ_1‖_{L²}² = ψ_1(0) = c_φ` by Plancherel.
**This is exactly Paper 44 Theorem 8bis.2 in its normalization-free form
(8bis.4c), carried with its `‖φ‖²_{L²}/ε` factor**, which is the point: the
diagonal is `−(c_φ/ε)(\log(1/ε)+O(1))`, not `−\log(1/ε)+O(1)`.  This gives
(5.4) and (a).  (b) is Gershgorin applied to (5.4): every row of
`−(\log(1/ε)−C_φ)I + A'_N` is strictly diagonally dominant with negative
diagonal once `\log(1/ε) − C_φ > r_N`.  (c) is the same computation for the
falsifier's data of §5.4.  ∎  `PROVED`

**Remark 5.9 (what Theorem 5.8 costs the programme: the infinite genus is an
unconditional damper).**  The divergence of the archimedean diagonal is
Paper 44 Theorem 8bis.2 — "`Δ·Δ = −∞`", the infinite genus.  Theorem 5.8 says
that this divergence **dominates the whole finite Gram matrix** at small `ε`,
one logarithm faster than the prime atoms.  Three consequences, all
restrictive:

1. **Finite inertia at small `ε` is unconditionally uninformative.**  Both
   `ζ` and `Ξ_a` give negative definite matrices there, by Theorem 5.8(b),(c),
   with no hypothesis about zeros.  A negative inertia reported at small `ε`
   is therefore evidence of nothing, for any model.
2. **The falsifier cannot fire at small `ε`, and the separation of §5.4 lives
   in a window of `ε`.**  That window is `ε` of order one — precisely where
   the concentrated Frobenius reading (8bis.7) is **invalid** (Definition 5.1)
   and only the integral form (8bis.6) applies.  So the informative regime and
   the regime in which the entries are "the Weil kernel evaluated at
   `\log m − \log n`" are **disjoint**.
3. **The naive Dirichlet-delta limit does not exist.**  One might hope that
   `ε G_N(ε)` converges to the pure-atom matrix `c_φA'_N`, making the finite
   inertia the Dirichlet-polynomial question of Paper 44 Theorem 8bis.7.  It
   does not: the diagonal beats it by `\log(1/ε)`.  **[This is recorded
   because the the construction's first draft asserted that convergence and it is
   false; the numerical diagonal reads `−1.98, −33.94, −175.56` at
   `ε = 0.1, 0.03, 0.01` for `N = 10`, fitting
   `(2/3ε)(−\log(1/ε)+2.00)` to three digits at all three points, and not
   fitting `−\log(1/ε)+γ+\log4π` at any of them.]**

### 5.4 Numerics: `ζ` against the falsifier `Ξ_a`

`COMPUTATIONAL-ILLUSTRATION`.  These tables illustrate and falsify.  **They
prove nothing.**  Script: `scripts/d134_gram.py`; profile: `φ_ε` the unit
triangle of half-width `ε`, so `ψ_ε` is the cubic B-spline and
`\hatψ_ε(τ) = \mathrm{sinc}^4(ετ/2)`; the finite half computed in `t`-space as
a finite sum, the archimedean half by quadrature against the archimedean
symbol `\hatω(τ)`, which is what makes the diagonal finite and equal to the
regularized value of Theorem 8bis.2.  Double precision, one profile, no
convergence study, no interval arithmetic.  **Range of validity of the
quadrature:** the archimedean integrand is `\hatω(τ)\mathrm{sinc}^4(ετ/2)`,
oscillatory on a scale `1/ε`, and the adaptive quadrature reaches its
subdivision limit below `ε ≈ 0.01`; **no value at `ε < 0.01` is reported
anywhere in this paper**, and the asymptotic regime of Theorem 5.8 is
described by that theorem, not by the quadrature.

*A caveat on the profile.*  The triangle is `C_c^0`, not `C_c^∞`, so the
tests of the numerics are not literally those of (1.9).  This is immaterial
and is why: for `g = Σc_nφ_ε(·−\log n)` with `φ_ε` the triangle,
`Φ_g(½+iτ) = \mathrm{sinc}^2(ετ/2)Σc_nn^{−iτ}·(1+o(1))`, so
`|Φ_g(½+iγ)|^2 = O(γ^{−4})` and the zero sum of (3.1) converges **absolutely**;
Theorem 5.6 and Theorem 3.4 therefore extend from `C_c^∞` to this class by
dominated convergence along a smooth approximation, with no change of
constants.  The theorems of §5 are nevertheless stated for `C_c^∞`, which is
the class the target quantifies over.

*Validation of the normalization* (`--check`): this is the **one** computation
in the paper carried out in the regime where Paper 44 Theorem 8bis.1e's
concentrated reading (8bis.7) **does** apply — a single pair `(m,n)` at
`ε ≤ 0.05`, so `2ε` is below the distance from `Δ_{mn}` to the nearest atom —
and it is used precisely to check that the assembly reproduces (8bis.7) there.
The off-diagonal archimedean entry converges to `K(|Δ|)` —
at `Δ = \log(3/2)`, computed `1.476, 1.4707, 1.46994` at `ε = 0.05,0.02,0.01`
against `K(Δ) = 1.469694`; at `Δ = \log 2`, `0.94405, 0.94301, 0.94286`
against `K(Δ) = 0.942809`, with the separate atom `Λ(2)2^{−1/2} = 0.490129`.

*Falsifier model.*  `Ξ_a(s) = ξ(s+a)ξ(s−a)`, `0 < a < ½`: prime weights
`Λ(n)(n^a+n^{−a})n^{−1/2}`, archimedean symbol
`2\logπ − \mathrm{Re}ψ(¼+\tfrac a2+\tfrac{iτ}2) −
\mathrm{Re}ψ(¼−\tfrac a2+\tfrac{iτ}2)`, equivalently kernel
`K_a(t) = e^{−t/2}(e^{at}+e^{−at})/(1−e^{−2t})`, and a **rank-four** Tate
compression `Σ_nc_nn^{u} = 0`, `u ∈ \{±(½+a), ±(½−a)\}`.  At `a = 0` all data
degenerate to twice the `ζ` data, as they must (`Ξ_0 = ξ²`).

Inertia `(n_+,n_0,n_-)` of `G_N^{prim}(ε)`.  The last two columns record, per
row, the two hypotheses of Paper 44 Theorem 8bis.1e's **concentrated** reading
(Definition 5.1(c)): `W` = "width", `2ε < \log\frac{N}{N−1}` (`ε < 0.053` at
`N = 10`, `ε < 0.017` at `N = 30`); `S` = "support", `2ε < \min_{m≠n}|Δ_{mn}|`,
the same bound.  **Both fail in every row**, so no entry of this table may be
read as `W_{fin}(\{Δ\}) + K(|Δ|)`; every entry is Paper 45 Lemma 5.1a's value,
which is defined at every `ε`.  At `ε = 2.0` one has `0 ∈ supp(h_m⋆h_n^†)` for
**every** pair with `m,n ≤ 30` (since `\max|Δ| = \log 15 = 2.71 < 4 = 2ε`), and
at `ε = 0.5` for every pair with `m/n < e`.

| `N` | `ε` | `ζ` | `Ξ_{0.35}` | `Ξ_{0.45}` | `W` | `S` |
|---|---|---|---|---|---|---|
| 10 | 2.0 | `(0,0,7)` | `(1,0,4)` | — | ✗ | ✗ |
| 10 | 1.0 | `(0,0,7)` | `(1,0,4)` | `(1,0,4)` | ✗ | ✗ |
| 10 | 0.5 | `(0,0,7)` | `(0,0,5)` | `(0,0,5)` | ✗ | ✗ |
| 10 | 0.3 | `(0,0,7)` | `(0,0,5)` | — | ✗ | ✗ |
| 10 | 0.2 | — | — | `(2,0,3)` | ✗ | ✗ |
| 10 | 0.1 | `(0,0,7)` | `(0,0,5)` | — | ✗ | ✗ |
| 30 | 2.0 | `(0,0,27)` | `(7,0,18)` | — | ✗ | ✗ |
| 30 | 1.0 | `(0,0,27)` | `(5,0,20)` | `(7,0,18)` | ✗ | ✗ |
| 30 | 0.5 | `(0,0,27)` | `(3,0,22)` | `(5,0,20)` | ✗ | ✗ |
| 30 | 0.3 | `(0,0,27)` | `(4,0,21)` | — | ✗ | ✗ |
| 30 | 0.2 | — | — | `(5,0,20)` | ✗ | ✗ |
| 30 | 0.1 | `(0,0,27)` | `(4,0,21)` | — | ✗ | ✗ |

*Verification of Theorem 5.8(b),(c)* (`COMPUTATIONAL-ILLUSTRATION`).  The
unconstrained `G_N(ε)` becomes negative definite as `ε` falls, for both
models, exactly as (5.4) forces; and the diagonal doubles for `Ξ_a`, as
`c_φ ↦ 2c_φ` forces.  At `N = 10`:

| `ε` | `ζ` diag | `ζ` inertia of `G_N` | `Ξ_{0.35}` diag | `Ξ_{0.35}` inertia of `G_N` |
|---|---|---|---|---|
| 0.20 | `+0.99` | `(1,0,8)` | `+2.89` | `(3,0,6)` |
| 0.10 | `−1.98` | `(1,0,8)` | `−3.96` | `(1,0,8)` |
| 0.05 | `−13.45` | `(1,0,8)` | `−26.90` | `(1,0,8)` |
| 0.02 | `−64.55` | `(0,0,9)` | `−129.10` | `(0,0,9)` |
| 0.01 | `−175.56` | `(0,0,9)` | `−351.11` | `(0,0,9)` |

The ratio of the two diagonals is `2.00` at every `ε ≤ 0.05`, and the `ζ`
column fits `(2/3ε)(−\log(1/ε)+2.00)` to three digits.  **The falsifier's
positive directions are gone below `ε ≈ 0.02`, unconditionally, exactly as
Theorem 5.8(c) requires — which is why the separation in the table above is a
statement about a window of `ε` and not about the models tout court.**

**Reading, stated with its limits.**

1. **The falsifier fires, and the blueprint's fallback is not needed.**  D.3
   required that `Ξ_a` exhibit a positive eigenvalue at finite `N`, "and if it
   does not, say so".  It does: at `N = 30`, at every tested `ε`, for both
   shifts, and already at `N = 10` for `ε ≥ 1`.  This is the separation of
   `ζ` from `Ξ_a` by an object of row B, computed on the declared carrier.
2. **`N = 10` is below the threshold**: at `N = 10` and `ε ≤ 0.5` the
   falsifier shows **no** positive eigenvalue.  So small `N` is uninformative,
   and a finite-inertia test reported at a single small `N` would be
   worthless.  This is recorded against the informativeness of *small* finite
   inertia, as the blueprint asks.
3. **The compression is not doing the work.**  `Ξ_a`'s primitive subspace is
   cut by **four** conditions against `ζ`'s two, i.e. the falsifier is
   compressed harder, and still shows positive directions.
4. **Nothing here is evidence for `ζ`.**  A negative inertia is what
   Theorem 5.8(b) forces **unconditionally** at small `ε`, for every model;
   at the `ε` of this table it is consistent with RH by Theorem 5.6 and is
   not evidence against its failure, since Theorem 5.6's converse is `OPEN`
   (Remark 5.7).  **No sign is claimed.**
5. The unconstrained `G_N(ε)` for `ζ` has inertia `(1,0,N−2)` at every tested
   `(N,ε)`: one positive direction, the Perron direction of an entrywise
   positive kernel, removed by the compression.  This is the shape a Hodge
   index argument would want, and it is **not** evidence that such an argument
   exists: by Remark 5.4 it says nothing about `I_A` on `D_A`, where
   Theorem 14.1 is the governing statement, and by Theorem 5.8(b) the shape
   itself disappears at small `ε`, where the matrix becomes definite.

---

## 6. D.4 — what a nonnegative invariant cannot be

`PANEL_3` §5 asks for a functor to something carrying a nonnegative invariant
plus a vanishing theorem.  This section proves five negatives, each with a
counterexample, and states the requirement list a candidate must satisfy.

### 6.1 Effectivity does not meet the primitive sector

**Theorem 6.1 (`PROVED`; = blueprint D.4(a), confirmed).**
`Eff_A^{tr} ∩ \{F : Γ_F\ \text{primitive}\} = \{0\}`.

*Proof.*  Paper 43 Theorem 10.3c(a): for `F ≥ 0` pointwise,
`λ_∓(F) = ∫F|w|^{∓1/2}d^*w ≥ 0` and `> 0` unless `F` vanishes a.e., hence
everywhere by continuity.  Primitivity is `λ_- = λ_+ = 0`.  ∎  `PROVED`

**Remark 6.2 (why this closes Weil's verbatim route, and what Weil actually
does).**  Weil's inequality is obtained not from effectivity of the class
whose self-intersection is bounded, but from `h⁰ ≥ 0` for a **different**
divisor: one applies Riemann–Roch to `aΔ + bΓ` — a class with **arbitrary
integer coefficients**, in general not effective — and uses `h⁰ ≥ 0` plus a
vanishing theorem for its adjoint.  So Theorem 6.1 does not by itself defeat
the RR route; what it defeats is the shortcut "primitive classes are
effective, effective classes have nonnegative degree".  The requirement list
of §6.3 is written accordingly.

### 6.2 Three candidate `h⁰`s, each refuted

**Theorem 6.3 (the orthogonality candidate; `PROVED` — and it is a strawman,
so labelled: `R134.002` (m-note to §6) is right that the refutation is one
line and that the candidate was named by the blueprint only to be
discarded).**  Define
`h⁰_⊥(F) := \dim\{G ∈ D_A^{rad} : I_∞(F,G) = 0\}`.  Then `h⁰_⊥(F) = ∞` for
every `F`, so `h⁰_⊥` is not a nonnegative-integer invariant and carries no
information.

*Proof.*  `G ↦ I_∞(F,G)` is a single linear functional on the
infinite-dimensional space `D_A^{rad}`, so its kernel has codimension `≤ 1`
and is infinite-dimensional.  Counterexample making it concrete: for
`F = Γ_{h}` with `h` a bump at `t = \log 2`, every `Γ_{h'}` with `supp h'`
disjoint from the countable set `\{\log n ± supp h\}` and with
`∫\hat h'\overline{\hat h}\,\hat T = 0` — a codimension-one condition —
lies in the kernel.  ∎  `PROVED`

**Theorem 6.4 (the spectral-dimension candidate; `PROVED`).**  Define
`h⁰_{spec}(F) := \dim` of the spectral subspace of the multiplication operator
by `\hat T + c` on which `\hat T + c ≥ 0`, intersected with the cyclic
subspace generated by `F`.  Then (i) `h⁰_{spec} ∈ \{0,∞\}`, by Paper 43
Theorem 14.1(a),(b): with `c = 0` both `\{\hat T ≥ 0\}` and `\{\hat T < −K\}`
carry infinite-dimensional subspaces, unconditionally; and (ii) the definition
**names the sign of `\hat T`**, i.e. it presupposes the datum sought, which
`P122_D_SPECIFICATION` §1 forbids ("the category must not be defined using
positivity, the kernel, or the spectral decomposition of `Δ_T`").

*Proof.*  (i) is Theorem 14.1(a),(b) and (c) (`m ≥ 5.372 > 0`, so both
hypotheses hold at `c = 0`); the cyclic subspace of any `F` with
`\hat F ≠ 0` a.e. meets both.  (ii) is the quoted clause.  ∎  `PROVED`

**Theorem 6.5 (the coefficient-positivity candidate; `PROVED`).**  Define
`h⁰_{eff}(F) := 1` if `F ∈ Eff_A^{tr}` and `0` otherwise, or any functional of
the effective cone.  Then `h⁰_{eff}` cannot appear in a Riemann–Roch identity
whose quadratic term is `I_∞(F,F)`, because the effective cone is **not** the
operator-positive cone and no implication holds in either direction.
Counterexamples, both from Paper 43 Theorem 10.2(e): the effective permutation
kernel exchanging two points is self-adjoint with eigenvalues `+1, −1`, hence
effective and **not** operator-positive; and `(e−t)^†(e−t)` is
operator-positive and **not** effective.  Moreover Theorem 10.3c(d) states
that `I_A(F,F)` has **no** sign on `Eff_A^{tr}`.  ∎  `PROVED`

**Theorem 6.6 (the scalar determinant candidate; `PROVED`).**  Define
`h⁰_{det}` from the analytic determinant `L_S`.  Then the linear term of any
RR-type identity built from `L_S` **vanishes on the rulings**, so the identity
cannot be converted into an inequality by a ruling-side vanishing theorem.
Counterexample: Paper 43 Theorem 10.8, `L_S(F_α,G_β) → (C,1)`, the unit of
`\mathrm{Pic}_b(C)`, along every admissible approximation of `(e_+,e_-)`,
while the intrinsic ruling determinant has
`λ_{per}(e_+,e_-) = (C,e)` with `‖1‖² = e^{−1} ≠ 1`.  Paper 43 Remark 10.8a
gives three independent structural reasons; any one of them suffices.
∎  `PROVED`

**Theorem 6.7 (`PROVED`): no candidate above satisfies even the type
requirement.**  A `h⁰` usable in Weil's argument must take values in
`Z_{≥0}` and be finite.  `h⁰_⊥ ≡ ∞` (6.3); `h⁰_{spec} ∈ \{0,∞\}` (6.4);
`h⁰_{eff}` is finite but is not related to `I_∞` by any inequality (6.5);
`h⁰_{det}` is not `Z`-valued and is trivial where it must be nontrivial
(6.6).  ∎  `PROVED`

### 6.3 The requirement list

**Definition 6.8 (what a row-D nonnegative invariant must be).**  **[SUPERSEDED, phase 135, by Theorem 12.3(a),(b′),(c); see Proposition 12.5 for the clause-by-clause correspondence.  (R5) is **satisfied** by the affine involution `σ_K(E) = K−E` of Theorem 12.2 — the missing object was a *class*, not an involution — (R4) is **deleted** (the vanishing is derived, not postulated), (R3)'s identity is **weakened** to an inequality, and the side condition `χ ≥ 0` is **not needed**.  Definition 6.8 is kept verbatim below because §6.2's five negatives are stated against it and remain valid.]**  **[REBUILT,
round 2, finding `(M3)` of `R134.002`.  **Round 1's version ran backwards**: it
put the vanishing on `h(F^∨)` and concluded `I_∞(F,F) ≤ −2ℓ − 2χ`, whereas
substituting `h(F^∨) = 0` into (R3) gives `h(F) = ½I_∞ + ℓ + χ ≥ 0`, i.e.
`I_∞ ≥ −2ℓ − 2χ` — a **lower** bound, the opposite of row D's target.  In the
one paper whose rule is that no direction may be assumed, a directional error
in the requirement list is the worst kind, and it is corrected here.  The
vanishing must be on the **primitive** side, the side carrying the quadratic
term.]**  A candidate is a functor `h` from the correspondence theory of
Papers 43–44 to `Z_{≥0}` (or to a totally ordered monoid with `0` as least
element), together with a duality `F ↦ F^∨`, such that:

  **(R1) Functoriality.**  `h` is defined on the correspondence algebra
      `Corr_A^{tr}` (or on a category mapping to it), compatibly with `⋆`,
      `†` and the restriction functors of the chart system, and is defined
      **without** using positivity of `B_{nuc}`, the kernel, or the spectral
      decomposition (P122 §1).
  **(R2) Nonnegativity, on the dual side.**  `h(G) ≥ 0` for every `G`; in
      particular `h(F^∨) ≥ 0` for every `F`.
  **(R3) An RR-type identity.**  An identity

          h(F) − h(F^∨) = ½\,I_∞(F,F) + ℓ(M(F)) + χ ,                 (6.1)

      with `ℓ` linear in the **ruling** data `M(F)` of (1.8) and `χ` a
      constant independent of `F`; the quadratic term must be `I_∞(F,F)`
      itself, not a comparison with it.
  **(R4) A vanishing theorem on the primitive sector.**  `h(F) = 0` for every
      primitive `F` — i.e. the declared vanishing class is the class carrying
      the quadratic term, **not** its dual.
  **(R5) The duality must carry the primitive sector off itself.**  **[NEW,
      round 3, finding `(R2-1)` of `R134_005`.  Without it the list is not
      merely unfulfilled but **vacuous**, and the proof is two lines: if
      `F ↦ F^∨` preserved primitivity, then (R4) would give `h(F^∨) = 0` as
      well, and (6.1) would read `0 = ½I_∞(F,F) + χ` for **every** primitive
      `F`, i.e. `I_∞` constant on the primitive sector — false by homogeneity,
      since `F ↦ λF` scales `I_∞` by `λ²`, unless `I_∞ ≡ 0` there, which
      Paper 43 Theorem 14.1 forbids.  So **no `h` whatever** satisfies
      (R1)–(R4) for a primitivity-preserving duality.]**  Formally: there must
      exist primitive `F ≠ 0` with `F^∨` **not** primitive.  In Weil's
      argument the duality is `D ↦ K − D`, and it does move the class.  Here:

      * the **only** duality rows A–C construct on `Corr_A^{tr}` is the
        half-density dagger `†` (Paper 43 §§3–5, Lemma 8.4), and `†`
        **preserves** primitivity: `λ_∓(Γ_h^†) = \overline{λ_±(Γ_h)}`
        (Paper 43 Theorem 9.1, (1.3)), so `M(Γ_h) = 0` iff `M(Γ_h^†) = 0`.
        **Hence `∨ = †` is excluded by (R5)**, and with it the only duality
        the corpus supplies;
      * **`NOT CONSTRUCTED`, and hereby named as an open requirement:** no
        duality on the correspondence theory of Papers 43–44 moves the
        primitive sector off itself.  Producing one — a Serre-type duality
        with a `K`-twist, not an involution of the same sector — is a
        **prerequisite** for (R1)–(R4) to be satisfiable at all, and is added
        to §9.1 as its own open item.

Given (R1)–(R5), for primitive `F` one has `M(F) = 0` and `h(F) = 0`, so (6.1)
reads `−h(F^∨) = ½I_∞(F,F) + χ`, whence

    I_∞(F,F) = −2h(F^∨) − 2χ ≤ −2χ  ≤ 0  \quad\text{when } χ ≥ 0 ,     (6.2)

which is row D's target — the step `h(F^∨) ≥ 0` being (R2), and `F^∨` being a
class on which (R4) says nothing, by (R5).  **Nothing in this paper produces
such an `h`; nothing in rows A–C produces the duality (R5) requires; no sign
is claimed; and (6.2) is displayed only to fix the direction the requirement
list must have.**

**Remark 6.8a (each negative of §6.2, re-checked against (R1)–(R5)).**
**[REBUILT, round 3: the list acquired (R5), so the re-check is redone; and
minor `(r1)` of `R134_005` is carried out in the `h⁰_{eff}` row.  All five
refutations survive, and one of them is sharpened again.]**

| candidate | fails | why |
|---|---|---|
| `h⁰_⊥(F) = \dim\{G : I_∞(F,G) = 0\}` (Thm 6.3) | **(R2)**, **(R4)** | it is `+∞` for every `F`, so it is neither `Z_{≥0}`-valued nor zero on the primitive sector.  **A strawman**, so labelled in Theorem 6.3: the refutation is one line, and the blueprint named the candidate only to discard it. |
| `h⁰_{spec}` (Thm 6.4) | **(R1)**, **(R4)** | it is defined *through the sign of the symbol*, which P122 §1 forbids; and by Thm 14.1(a),(b) it is `0` or `∞`, never a finite nonnegative integer, so it cannot vanish on the primitive sector in the sense (R4) requires. |
| `h⁰_{eff}` (Thm 6.5) | **(R3)** | **[`(r1)`: round 2 wrote that it "vanishes on the primitive sector, vacuously".  Two words wrong.  It vanishes on every **nonzero** primitive class — a *value*, forced by Theorem 6.1, not a vacuity — and it fails (R4) at the origin, since `0` is primitive and `0 ∈ Eff_A^{tr}`, so `h⁰_{eff}(0) = 1 ≠ 0`.]**  Modulo the origin it satisfies the vanishing theorem and fails where it must: there is **no** identity (6.1) relating it to `I_∞(F,F)`, because `Eff_A` is not the operator-positive cone (Thm 10.2(e)) and `I_∞` has no sign on `Eff_A^{tr}` (Thm 10.3c(d)).  **Still the sharpest of the five: the one candidate that satisfies the vanishing theorem has no Riemann–Roch identity at all.** |
| `h⁰_{det}` (Thm 6.6) | **(R3)** | it is not `Z`-valued, and the linear term of any identity built from `L_S` is **trivial on the rulings** (Thm 10.8), so `ℓ(M(F))` carries no information and (6.1) cannot be converted into (6.2) by a ruling-side argument. |
| effectivity as the source of the sign (Thm 6.1, Rem 6.2) | **(R4)** is vacuous | `Eff_A^{tr} ∩ \{primitive\} = \{0\}`, so a vanishing theorem *on effectivity* says nothing about primitive classes; Weil's own argument uses `h⁰ ≥ 0` for `aΔ+bΓ`, a class with arbitrary integer coefficients and in general not effective. |
| **every candidate above, and every candidate not yet named** | **(R5)** | the duality clause is failed *before the candidate is chosen*: `†` preserves primitivity, and rows A–C construct no other duality.  **(R5) is therefore not a test that discriminates between candidates — it is a missing piece of the carrier**, and until it exists the whole list is vacuous.  This is a **new** negative of round 3 and the most structural of the six: it says the obstruction to Definition 6.8 is not the choice of `h` but the absence of a `K`-twist.  **[phase 135: correct as a statement about *algebra involutions*, and the diagnosis "a missing `K`-twist" was right.  Weil's `D ↦ K−D` is an **affine** involution, not an algebra map; Theorem 12.2 constructs it, and Theorem 12.2a records that the missing object was the class `K`.  §9.1 item 3a is thereby closed.]** |

**Remark 6.9 (the one honest candidate on the table, and its status).**
Theorem 3.7(e) supplies an `h` of the **right kind and the wrong type**:
`h(g) := ‖π(g)Ω‖²` is nonnegative by construction and satisfies an exact
identity with quadratic term `Λ(g) = −I_∞(Γ_{Πg},Γ_{Πg})`.  It fails (R1)
as it stands, because the only construction of `(H,π,Ω)` this paper has is
Bochner's, which takes the conclusion as input.  **The row-D problem, in the
language of Definition 6.8, is: construct `(H,π,Ω)` — or any `h` satisfying
(R1)–(R4) — from the correspondence theory, not from the answer.**  This
paper does not do it, and records no opinion about whether it can be done.
**[phase 135: Theorem 12.3 replaces "(R1)–(R4)" in this sentence by the three
properties (a),(b′),(c).  **[phase 135 round 2: round 1 added here that
"Corollary 12.4a proves that any such `h⁰` must use the Euler product in the
form of Paper 44 Theorem 3ter.6(ii)".  That is **withdrawn**: Restatement 12.4a
is a schema about admissible *proofs*, not a theorem about functions, and what
it excludes is a model-free derivation, not a definition (finding M1 of
`R135_002`).  The Euler-product reading survives as the heuristic Remark
12.4b.]**  The sentence is otherwise unchanged and still states row D's
problem.]**

---

## 7. D.5 — the falsifier suite as theorems

`P122_D_SPECIFICATION` §5 requires every candidate row-D law to answer, **before
comparison**, for the port swap, Davenport–Heilbronn, the shifted pair,
function fields and Dedekind zeta.  This section proves the two that bear on
D.1 and states the other three.

### 7.1 The shifted pair

**Theorem 7.1 (`Ξ_a` has no Frobenius family in the sense of row B;
`PROVED`).**  Let `Ξ_a(s) = ξ(s+a)ξ(s−a)`, `0 < a < ½`.  Its explicit-formula
data are those of §5.4: prime weights
`w_n^{(a)} = Λ(n)(n^{a}+n^{−a})\,n^{−1/2}`, four poles, rank-four Tate
compression.  Then:

  (i) `w_n^{(a)} ≠ Λ(n)n^{−1/2}` for every prime power `n ≥ 2` and every
      `a ≠ 0`, since `n^a + n^{−a} > 2`;
  (ii) hence there is **no** family `\{F_n\}` of classes on the carrier (1.1)
      whose finite contacts are the `w_n^{(a)}`, of the shape of Paper 44
      Theorem 3ter.10: those contacts are `Λ(p^k) p^{−k/2} =
      \mathrm{vol}_{d^*x}(p^kZ_p^×)\,p^{−k/2}` by (3bis.8), i.e. the
      **half-density volume of the fixed-point stratum**, and that volume is
      `\log p`, not `(\log p)(p^{ka}+p^{−ka})`;
  (iii) equivalently, in the language of Paper 44 Theorem 3ter.6, the
      would-be Frobenius of `Ξ_a` at `n` satisfies
      `F_n ⋆ F_n^† = (n^a+n^{−a})\,Δ^{(n)}` and not `Δ^{(n)}`: **it is not a
      partial isometry**, and the half-density normalization that makes the
      dagger an inverse (Paper 43 §11bis item 5(ii)) does not exist for it.
  The pre-comparison axiom violated is therefore **unimodularity of the local
  roots**: `Ξ_a`'s local roots are `p^{±a}` rather than `1`.

*Proof.*  (i) is `x+x^{−1} > 2` for `x ≠ 1`.  (ii) is (3bis.8) and
Theorem 3ter.10: the contact of the smeared Frobenius at a prime power is the
shell volume, a quantity fixed by the Haar measure of the carrier, with no free
parameter.  (iii) is (ii) divided by the diagonal normalization of
Theorem 3ter.6.  ∎  `PROVED`

**Corollary 7.2 (`PROVED`).**  Theorem 3.7's chain breaks for `Ξ_a` at
(1.6)/(1.5), i.e. **before** the comparison theorem and before any statement
about zeros: `Ξ_a` has no unit-averaged Frobenius family `Frob ⋆ Δ^{rad}`
whose Gram form is its Weil kernel, because it has no Frobenius family.  Its
Weil kernel exists as a kernel and its bordered form exists (§4, and the
numerics of §5.4 and of P124.014 assemble both); what does not exist is the
row-B factorization of that kernel.

*[The classical fact that the zeros of `Ξ_a` are those of `ξ` shifted by
`±a`, hence off the critical line for `0 < a < ½`, is recorded once here as a
statement about the model.  It is **not used** in the proof of Theorem 7.1 or
Corollary 7.2, and no statement about the zeros of `ζ` is made.]*

**Remark 7.3 (and this is exactly the input P124.014 says Gate R needs).**
P124.014 §4 item 1 concludes: "Any proof of Gate R for `ζ` must use
unimodularity of the local roots, i.e. the same arithmetic input Gate S
needs."  Theorem 7.1 identifies that input with a **theorem of row B** —
Theorem 3ter.6 — and thereby names, in the corpus's own vocabulary, the
hypothesis that separates `ζ` from the falsifier before any spectral
comparison.

### 7.2 Davenport–Heilbronn

**Theorem 7.4 (`PROVED`).**  The Davenport–Heilbronn function has a functional
equation, is entire, and has **no Euler product**.  Consequently, on the
carrier (1.1):

  (i) there is **no** multiplicative family at all: the coefficients of
      `−f'/f` are not supported on prime powers with nonnegative
      shell-volume weights (they are the Dirichlet-convolution
      `dh_λ` of `scripts/p124_lab.py`, of both signs), so nothing of the shape
      of Theorem 3ter.4 exists, and Theorem 3ter.7's inverse semigroup is
      vacuous;
  (ii) it is **entire**, so it has no poles, no Tate characters, `𝔅_T = 0`,
      no primitive condition (1.7), and the polar packet of Paper 45
      Theorem 8.1 is `0`.  Theorem 4.1's border is empty and its dichotomy is
      vacuous; `Σ(T)` is not defined;
  (iii) hence D.1's reformulation fails at its **first** step for DH: there is
      no `Frob ⋆ Δ^{rad}` family whose Gram form is the kernel, and there is
      no primitive sector to restrict to.

*Proof.*  (i) and (ii) are the defining properties of the model, as recorded
in `RH2017_RH9_AUDIT` and implemented in `p124_lab.model_dh`; (iii) is (i)+(ii)
against (1.5)–(1.7).  ∎  `PROVED`.  `RH2017_RH9_AUDIT` retires DH as a
**quantitative** control; it is used here qualitatively only, and no DH
computation is reported.

### 7.3 The remaining three questions of P122 §5, answered or declared

**Proposition 7.5.**

  (a) *Port swap.*  The datum that changes sign under the port swap is the
      **odd** eigenvector `(1,−1)` of Theorem 4.3: by (4.2) the swap `σ` acts
      on the Schur complement with eigenvalues `+1` on the even direction and
      `−1` on the odd one, and the orientation is canonical because `σ` is
      induced by the reflection `R : t ↦ −t` of the modulus group, i.e. by
      `Frob_∞(t) ↦ Frob_∞(−t) = Frob_∞(t)^†` (1.5).  `PROVED` (Theorem 4.3
      and (1.5)).
  (b) *Function fields.*  `NOT ANSWERED HERE.`  Which standard surface
      intersection object is recovered is a question about the non-invertible
      sector, which Paper 43 §11bis item 5(v) declares `NOT CONSTRUCTED`.
  (c) *Dedekind zeta.*  `NOT ANSWERED HERE.`  If a candidate law extends, it
      would imply the corresponding GRH and **must say so**; no candidate law
      is proposed in this paper, so the question has no addressee yet.  It is
      restated in §9 as an open obligation on any future candidate.

**Rule 7.6 (the gate, for the record).**  Any row-D candidate law proposed
after this paper must be shown to fail for `Ξ_a` by Theorem 7.1's mechanism
and for DH by Theorem 7.4's, **before** its comparison with `B_{nuc}` is
proved, per the acceptance test §2.3.

---

## 8. External inputs, each with the clause it serves

Every classical import used anywhere above, with the clause it serves and the
statement that uses it.  Nothing else is imported.

| tag | import | clause it serves | used at |
|---|---|---|---|
| **(X1)** | Weil's explicit formula | not imported: `PROVED-IN-REPOSITORY` as Paper 45 Theorem 9.4 | Theorem 3.6 |
| **(X2)** | **Weil's criterion** (A. Weil, 1952), direction "RH ⟹ the functional is `≥ 0`" — here a computation, not a citation | D.1 (a)⇒(b) | Theorem 3.7 |
| **(X3)** | **Bochner–Schwartz theorem, `D'(R)` form** (L. Schwartz): *a positive-definite distribution on `D(R)` is **automatically tempered** and is the Fourier transform of a unique positive tempered measure.*  **[RESTATED, round 2, `(M1)`: round 1 imported the `S'` form, whose hypothesis — temperedness of `𝔏` — is **false as round 1 justified it** and unavailable a priori (Proposition 3.6a).  In the `D'` form temperedness is a conclusion, and the step needs no hypothesis beyond `𝔏 ∈ D'(R)`.]** | D.1 (c)⇔(d) | Theorem 3.7, Proposition 3.6a |
| **(X4)** | **SNAG / Stone's theorem**: bijection between positive tempered measures on `R` and spectral measures of strongly continuous unitary representations of `(R,+)` | D.1 (d)⇔(e) | Theorem 3.7 |
| **(X5)** | **GNS construction** for a positive-definite distribution on a locally compact abelian group | D.1 (e), the vector `Ω` and (3.4) | Theorem 3.7 |
| **(X6)** | **Gershgorin's circle theorem** for real symmetric matrices.  **[CORRECTED, round 2, `R134.002` §7: round 1's table said "Weyl's inequality"; the proof of Theorem 5.8(b) uses strict diagonal dominance, i.e. Gershgorin.  Weyl is not used anywhere in this paper.]** | D.3, the `ε → 0` inertia | Theorem 5.8(b) |
| **(X7)** | **Closed-form Schur complement / Douglas range lemma** (hypotheses `L_T > 0` checked in each use) | D.2, the bordered criterion and the variational form | Theorem 4.1, Theorem 4.6 |
| **(X8)** | `(E2)`'s no-real-zeros clause, `(E3d)`, `(E6)` (Paley–Wiener) | D.1 (b)⇒(a), **only** inside Paper 45 Theorem 10.4, which is cited and not re-proved | Theorem 3.7 |
| **(X9)** | The digamma integral representation `ψ(z) = −γ + ∫_0^∞(e^{−u}−e^{−zu})/(1−e^{−u})du` | the identification of the archimedean kernel of a Gamma parameter `b_0` as `e^{−b_0t}/(1−e^{−2t})`, used to define the falsifier's kernel `K_a` | §5.4, `scripts/d134_gram.py` |
| **(X10)** | Green's function of `−∂_t²+¼` on `R`, and its kernel `e^{−\|t\|/2}` | D.1, the inverse of `Π`; and `Π e^{±t/2} = 0`, which gives `Π²ϖ = 0` | Lemma 3.1, Theorem 3.6 |
| **(X11)** | **Chebyshev's bound** `Σ_{p ≤ x}(\log p)\,p^{−1/2} ≫ \sqrt x`, with partial summation | the non-temperedness of `W_{fin}`.  **[CORRECTED, round 3, `(F1)`: round 2's entry read "and of `Π²W_{fin}`", which served the deleted Proposition 3.6a(iii).]** | Proposition 3.6a(ii) |
| **(X14)** | The prime number theorem under RH, `ψ_{Ch}(x) = x + O(\sqrt x\log²x)`, with partial summation.  **Used only to state what is *not* decided**, never in the proof of any labelled statement | the observation that RH **implies** `Π²W_{fin}` is tempered, hence that a proof of its non-temperedness may not be attempted here | Remark 3.6b(2) |
| **(X12)** | **Sylvester's law of inertia** | D.2, what is and is not a congruence invariant | Finding 4.8(iii) |
| **(X13)** | **Paper 45 Lemma 5.1a** (repository, not classical): the radial trace with **no** support hypothesis, `c := 0` | D.3, the definition of the Gram entries at every `ε` | Definition 5.1(a) |

Repository imports, by number, are listed in §1 and are not repeated here.
The two explicitly **withdrawn** imports of the corpus — `(Wgr)` (Paper 44
Lemma 8bis.6b) and Paper 43's `c_{cut}` (Remark 8A.7e) — are **not** used
anywhere in this paper, and Remark 5.7 records why the first may not return.

---

## 9. What is open

### 9.1 Open items, one sentence each

1. **Row D's target itself** — `I_∂ ≤ 0` on every primitive radial class in
   the colimit with `c = 0` — is `OPEN`, and nothing in this paper bears on
   its truth in either direction.
2. **The construction of `(H,π,Ω)`** of Theorem 3.7(e) from the correspondence
   theory, rather than from Bochner applied to the conclusion, is `OPEN`; it
   is the row-D problem in the form this paper gives it.
3. **[REPLACED, phase 135, by Theorem 12.3.  The open item is now: *a function
   `h⁰ : D^W → R_{≥0}` satisfying (a), (b′), (c) of Theorem 12.3*, for which no
   **model-free** proof can exist (Restatement 12.4a) and for which §13 closes
   two natural lattice-counting constructions on every finite truncation
   (Theorem 13.6).  **[phase 135 round 2: round 1 wrote "which by Corollary
   12.4a must use the unimodularity of the local roots, and which §13 proves is
   not obtained by counting lattice points in the effective cone (Theorems
   13.3, 13.6, 13.7)".  Both halves are weakened here — see findings M1 and M8
   of `R135_002` and §13 as repaired.]**  The original text is kept because
   §6's five negatives are stated against it.]**  **A functor `h` satisfying (R1)–(R5) of Definition 6.8** — whose direction
   was corrected in round 2 (`(M3)`) and whose duality clause was added in
   round 3 (`(R2-1)`) — is `OPEN`, and §6 proves that four named candidates
   are not it, with Remark 6.8a recording which clause each fails.
3a. **[CLOSED, phase 135: `σ_K(E) := K − E` on the Weil class `D^W` is such a
   duality (Theorem 12.2).  It is **affine**, not an algebra involution, which is
   why §6.3 — searching among `†`-like objects — could not find it; and the class
   `K` it translates by is constructed in Theorem 11.7.  The text below is kept
   verbatim as the record of the requirement it named.]**  **A duality on `Corr_A^{tr}` that carries the primitive sector off
   itself** — the analogue of `D ↦ K − D` — is `NOT CONSTRUCTED`, and by
   Definition 6.8(R5) it is a **prerequisite** for the requirement list to be
   satisfiable by anything at all: the only duality rows A–C supply is `†`,
   which preserves primitivity.  This is the newest and most structural of the
   `OPEN` items.
4. **`Σ(T) ≥ 0` for all `T < T_q`** (P124.013 (3.2)) is `OPEN`; Corollary 4.4
   reduces it to two scalar inequalities `α ± β ≥ 0` and nothing more.
5. **The informative window of `ε`** is `OPEN`: Theorem 5.8(b) makes the
   finite inertia unconditionally definite below `ε_1(N)`, the separation of
   §5.4 is observed above it, and no theorem locates the transition or says
   what the inertia means there.
6. **The converse of Theorem 5.6** — whether `G_N^{prim}(ε) ≤ 0` for all
   `N, ε` implies RH — is `OPEN` and is not to be asserted; it inherits
   8bis.7(c)'s moving-window gap.
7. **Whether `T_q < ∞`** for `ζ`, which is the hypothesis of Theorem 4.1, is
   `OPEN`, and is the negation of item 1; Theorem 4.1 is therefore
   **conditional** and is so marked.
8. **The relative correspondence** joining P122 (7.1) to the archimedean
   determinant datum of P122 §9 is `NOT CONSTRUCTED`.
9. **The non-invertible sector** (Paper 43 §11bis item 5(v)) is `NOT
   CONSTRUCTED`, so Proposition 7.5(b) has no answer.
10. **Dedekind zeta**: any future candidate law must declare whether it
    extends, and if it does, must state that it would imply the corresponding
    GRH (P122 §5).
11. **The numerics** of §5 are single-resolution, double-precision, one
    profile, no interval arithmetic and no convergence study; those of §4 now
    carry a resolution sweep (Theorem 4.2(iii), Warning 4.5a) but are
    variational upper bounds and certify nothing when positive; see §9.3(2).
12. **Whether 14.1's concentration mechanism revives in the colimit
    `N → ∞`, `ε = ε(N) → 0`** is `OPEN` (Remark 5.4(iii)); round 1 asserted it
    does not and that assertion is withdrawn.
13. **D.3 is retired as a programme item** — not `OPEN` but **closed as a
    route** — on the earlier and the auditors' concurring recommendation: after
    the round-2 re-attribution the entries are Paper 45 Lemma 5.1a's values,
    the Frobenius reading holds in **no** computed regime (twelve rows, `W`
    and `S` both `✗`), and Theorem 5.8 makes the small-`ε` end unconditionally
    definite for *every* model.  **Theorem 5.8 is kept as D.3's result and
    Remark 5.9(1)–(3) as its reason**; the finite-inertia test is not to be
    resumed, and in particular the `N = 15,20,25` refinement is not to be run,
    since a finer grid would sharpen a statement with no theorem under it.
14. **A low-priority open audit item:** whether any statement in phases
    119–123 rests on a **positive** double-precision Galerkin eigenvalue.  The
    exposure is narrow and is believed nil — the shared assembly
    (`rowd_assembly`, `p124_lab`) is imported only in phases 118 and 124, both
    of which now carry the `[phase 134]` note, and phase 120 reuses the same
    piecewise-constant meshes only in the **safe** direction (residuals
    establishing a failure, and an entrywise agreement check at
    `6.44·10^{−14}`, neither of which is a positive-eigenvalue certificate) —
    so no round should be spent on it; it is recorded so that it is not
    forgotten.
15. **Whether `𝔏` is tempered** is `OPEN` in both directions, and is
    equivalent to a PNT-type growth statement: `𝔏 ∈ S'(R)` iff
    `M(t) − 2e^{t/2}` is polynomially bounded, where
    `M(t) = Σ_{n≤e^t}Λ(n)n^{−1/2}` (Remark 3.6b(3)).  RH **implies** it, so
    its negation may not be attempted here; and Theorem 3.7 does not need it,
    `(X3)` being imported in the `D'` form where temperedness is a conclusion.
    **[REBUILT, round 3, `(F1)`: round 2's Proposition 3.6a(iii) claimed to
    have decided this question in the negative, which would have proved ¬RH;
    it is deleted.]**

### 9.2 Blueprint claims refuted or repaired in this round

| blueprint claim | verdict | where |
|---|---|---|
| D.1(i): `Λ(g) = Σ_ρ|ρ(1−ρ)|²Φ_g(ρ)Φ_g(1−ρ)` | **`REFUTED`** — the correct factor is `[ρ(1−ρ)]²` (Lemma 10.3a); `[·]² = |·|²` holds exactly on the critical line, so the stated form presupposes RH.  Counterexample at `ρ = 0.6+14i`. | §3.2 |
| D.1: "`Π` is a bijection onto the primitive class (Cor 10.2)" | **`REPAIRED`** — Cor 10.2 proves injectivity only; surjectivity is true and is proved here (Lemma 3.1), the two Tate conditions being exactly what makes `G_{1/2}∗F` compactly supported. | §3.1 |
| D.1(ii): "`μ := −\hat T_∞|_{prim} + polar` is a positive tempered measure" | **`REPAIRED`** — four errors of type: the distribution is `𝔏 = −Π²(W_{fin}+ω_∞) ∈ D'(R)`, `μ` is its Fourier transform, the `Π²` factor is not optional **and annihilates the polar summand identically** (`Πϖ = 0`), "`\hat T_∞|_{prim}`" is not a defined object, and **no temperedness may be asserted** (Prop. 3.6a). | §3.3 |
| D.2: "`B_T` [is] Paper 43's hyperbolic Tate plane" | **`REFUTED`** — three distinct `2×2` objects are conflated; the polar summand is hyperbolic in the pulled-back basis (4.1), the Tate **block** `𝔅_T` is that plus `⟨𝒜_Tφ,φ⟩`, and at `T = 0.72` the block is **positive definite** (`\det = +5.2` to `+6.8·10^{−3}` across `refine = 2,…,6`).  **[round 2, (M7): the block is renamed `𝔅_T` throughout; `B_T` now means only the ruling plane of (1.8).]** | §4.2 |
| D.2: monotonicity of `Σ` under `T ↦ T+ε` | **`REFUTED` as available** — the border vectors move with the window, so the standard argument gives only (4.4); and `λ_{\min}Σ(T)` is numerically non-monotone for `ζ` in both bases. | §4.4 |
| D.3(a): "at a fixed finite chart the inertia is indefinite for large `N` (Thm 14.1 transported)" | **`REFUTED`**, by Theorem 5.5 alone: under `(C1)` the conclusion contradicts the target, and under the chart reading the kernel formula is out of its own window.  **[round 2, `(M4)`: round 1 offered a second, independent refutation via the unavailability of 14.1's mechanism.  Its key step was unproved and probably false; it is **downgraded to Remark 5.4**, keeping only the dimension argument and the non-membership of the concentration profiles, and marking the colimit question `OPEN`.]** | §5.2, Rem 5.4 |
| D.3: "the falsifier must show a positive eigenvalue at finite `N`; if it does not, say so" | **satisfied** — it does, at `N = 30` for every tested `ε` and both shifts; but **not** at `N = 10` for `ε ≤ 0.5`, which is recorded against small-`N` inertia. | §5.4 |
| D.4(a): `Eff_A` meets the primitive sector only in `0` | **confirmed**, two lines from Paper 43 Thm 10.3c(a); the gloss about Weil's route is sharpened in Remark 6.2. | §6.1 |
| §1 item 3: partial isometry ⟹ PSD Gram "for free" | **`REPAIRED`** (attribution) — PSD in a positive functional holds for **any** family; Thm 3ter.6 is used nowhere in §3. | Remark 3.9 |

### 9.2a Round-2 repairs, by finding

| finding | what was wrong in round 1 | repair | where |
|---|---|---|---|
| `(M1)` = `LF1` | Theorem 3.7's Bochner step was justified by "`𝔏` is tempered because `ϖ`, `W_{fin}`, `ω_∞` are".  `ϖ` grows exponentially and `W_{fin}` has mass `≍ e^{|t|/2}|t|`; **neither is tempered** | `Πϖ = 0`, so `𝔏 = −Π²(W_{fin}+ω_∞)`; type `𝔏 ∈ D'(R)`; use Bochner–Schwartz in its `D'` form, where temperedness is a **conclusion**.  Proposition 3.6a(i),(ii) proves the old *justification* unavailable.  **[Round 2's repair overshot with a part (iii); withdrawn in round 3, §9.2b.]** | §3.3, (X3) |
| `(M2)` | (5.1) was displayed as `∫ψ_ε(t−Δ)d(W_{fin}+ω_∞)` and cited to Paper 44 Thm 8bis.1e; that integral **diverges** whenever `0 ∈ supp`, and 8bis.1e's width and support hypotheses fail over the whole informative window | entries defined by Paper 45 **Lemma 5.1a** (no support hypothesis) and polarization; 8bis.1e cited only for the *interpretation*, in the regime `ε = O(1/N)`, which no row of the §5.4 table satisfies | Def 5.1(a)–(d) |
| `(M3)` | Definition 6.8's conclusion ran **backwards**: vanishing on `h(F^∨)` yields a lower bound on `I_∞` | vanishing moved to `h(F)` on the primitive sector, nonnegativity used on the dual; (6.2) now gives `I_∞ ≤ −2χ`.  Remark 6.8a re-tests all negatives.  **[Round 3, `(R2-1)`: the repaired list was still **vacuous** — with a primitivity-preserving duality, (R3)+(R4) force `I_∞` constant on the primitive sector, false by homogeneity — so clause **(R5)** was added, and `†`, the only duality rows A–C construct, is shown to fail it.]** | §6.3 |
| `(M4)` | Theorem 5.4's "almost periodic hence cannot concentrate" was an assertion, and resonated Dirichlet polynomials plausibly refute it | downgraded to Remark 5.4: dimension argument + non-membership of the profiles; colimit question `OPEN`; Theorem 5.5 carries the refutation alone | §5.2 |
| `(M5)` | Finding 4.8 claimed P124.013 Cor 3.3's criterion is basis-dependent | **withdrawn**: at finite `T_*` the criterion is invariant.  What survives: the *value* `λ_{\min}Σ` is not invariant | §4.4, §9.3(1) |
| `(M6)` | §9.3(2)'s variational finding was not applied to this paper's own §4 numerics | Warning 4.5a: `λ_{\min}(L_T)` **and** `Σ(T)` are Galerkin upper bounds, with a `refine = 2…6` sweep; every positive value in §4.3–§4.4 certifies nothing | §4.3, §4.4 |
| `(M7)` | `B_T` denoted both the ruling plane and the Tate block — the very conflation §4.2 refutes | the block is `𝔅_T` throughout; `B_T` is the ruling plane only; announced in (1.8) | (1.8), §4 |
| `LF2` | Theorem 3.7 was graded `CLASSICAL + PROVED-IN-REPOSITORY` | regraded **`RESTATEMENT`**, with Lemma 3.1 and Theorem 3.6 carved out at `PROVED`; Remark 3.8(2) records that **no proof uses the modulus-group identification beyond naming** | §3.3, §3.4 |
| minors `(m1)`–`(m9)` | the `δ_0` finite part is the constant `c`; the real/complex quantifier; `C_φ` is purely archimedean in Thm 5.8's regime; the `(C1)` exemption; a garbled clause in Thm 5.2; a stale script docstring; one over-strong sentence in `R134.001`; `𝔅_T`'s entries not converged at `refine = 2`; label hygiene in the report | all carried out in place | §3.3, §5.1(d), §5.2, §5.4, scripts, `R134_004` |

### 9.2b Round-3 erratum: a round-2 repair that overshot

**One statement of round 2 is withdrawn, and it is the most serious error of
the campaign.**  It is recorded here in full because it was introduced by a
*repair*, found by the adversarial auditor of round 2 (`R134_005` (F1)), and would
— if left standing — have put a forbidden statement about the zeros inside
this paper.

| withdrawn | why it is wrong | why it was forbidden regardless |
|---|---|---|
| **Proposition 3.6a(iii)**, round 2: "`Π²W_{fin} ∉ S'(R)`", labelled `PROVED` | **(a) The proof was invalid.**  It ran `⟨Π²W_{fin},φ⟩ = ⟨W_{fin},Π²φ⟩` with `φ = Π^{−2}ψ`.  `φ ∈ S(R)` — that part is right — but `φ` is **not compactly supported**, and transposing a differential operator across the `D'×D` pairing is available only for test functions in `D(R)`; both sides presuppose that `Π²W_{fin}` is already tempered, which is the thing being denied.  **(b) The statement is false under RH.**  `Π²ϖ = 0` (Theorem 3.6), so with `ν := W_{fin} − ϖ\,dt` one has `Π²W_{fin} = Π²ν` **exactly**; under RH `M(t) = 2e^{t/2} + O(t³)`, so `ν` has a polynomially bounded distribution function and `Π²ν ∈ S'(R)`.  **The invalid step is precisely where the cancellation was discarded.** | By (b), a proof of 3.6a(iii) would be a proof of **¬RH**.  Combined with Theorem 3.6 and Theorem 3.7 (c)⇒(d) the paper as printed in round 2 *contained* that proof: `𝔏 ∉ S'` ⟹ `𝔏` not positive-definite ⟹ ¬(b) ⟹ ¬(a).  **A statement about the location of the zeros, in the one paper forbidden to make one** — so it had to go whatever its provability. |

*What replaces it:* **Remark 3.6b**, which says the true thing — `Π²` kills
exactly the growth the argument exploited; RH implies temperedness; the
question is a PNT-type growth statement on `M(t) − 2e^{t/2}`; and Theorem 3.7
does not need it, because `(X3)` is imported in its `D'` form where
temperedness is a **conclusion**.  This is better motivation for `(X3)` than
the false version was.

*What does **not** change:* Theorem 3.6, `Πϖ = 0`, the typing `𝔏 ∈ D'(R)`,
`(m1)`'s `c = 0` paragraph, all five clauses of Theorem 3.7, `(X3)`, the
uniqueness line for (d)⇒(e), and the `RESTATEMENT` grade.  The cost of the
erratum is one proposition and four cross-references, and **Proposition
3.6a(i),(ii) — the part that actually refutes round 1 — stands, now with the
truncation argument written out in full.**

*Running count, for the record:* **four** of the the construction's own statements have
been refuted across the three rounds — round 1's `εG_N(ε) → c_φA'_N`
(by its own numerics), round 2's three (`𝔏` tempered, Definition 6.8's
direction, Finding 4.8's reason), and now round 2's Proposition 3.6a(iii).
None cost a result.

### 9.3 Findings against the corpus, recorded here for audit

1. **P124.013 Corollary 3.3: the criterion is invariant; the number is not.**
   **[REBUILT, round 2, `(M5)` of `R134.002`, which partially refuted round
   1's version of this finding.  Round 1 said the criterion is
   "basis-dependent as stated"; **that is withdrawn** — at a *finite* `T_*`
   the condition numbers of the rebasing are bounded and
   `\liminf λ_{\min}Σ > −∞` is a congruence invariant, Finding 4.8(i).]**
   What survives (Finding 4.8(ii),(iii)): the **value** `λ_{\min}Σ(T)` is not
   a congruence invariant — the named and orthonormalized borders give
   `2.35·10^{−2}` and `2.77·10^{−3}` at the same `T = 1.67` and the same
   resolution — so it may not be quoted or compared across bases or papers;
   `Σ(T) ≥ 0` and the inertia of `Σ(T)` are invariant, and (3.2) is the form
   to carry.
2. **The Galerkin eigenvalues of the phase-118/124 assembly are variational
   upper bounds** and are not converged.  For `ζ`, `λ_{\min}(L_T)` at
   `T = 1.7` reads `2.93, 1.99, 1.23, 0.84, 0.61` (units `10^{−2}`) at
   `refine = 2,…,6`, decreasing at every step.  Since the piecewise-constant
   space is a **subspace** of the test space, the computed `λ_{\min}` is
   `≥` the true infimum: **a negative computed eigenvalue certifies a genuine
   negative direction; a positive one certifies nothing.**  Consequently the
   `ζ` "control" of P124.014 §3 is, by construction, incapable of supporting
   any conclusion about `ζ` — which is as it should be, and should be said.
   **Scope.**  This finding is about the **double-precision Galerkin scans**
   of phases 118 and 124 and about nothing else.  It does **not** touch the
   `T = \log 2` endpoint certificate replayed in P123.036, which is an
   interval-arithmetic computation with its own bounds; if that certificate
   carries a proved discretization bound then it is unaffected, and if it does
   not, that is a separate question this paper does not open.
3. **P124.014's first-contact brackets for `Ξ_a` are not resolution-stable.**
   At `a = 0.35`, `T = 1.68`: `λ_{\min}(L_T) = +1.31·10^{−1}` at
   `refine = 2`, `−1.58·10^{−1}` at `refine = 3`, `−4.33·10^{−1}` at
   `refine = 4`.  By the variational remark above, the refined values
   **certify** `T_q(Ξ_{0.35}) ≤ 1.68`, outside the published bracket
   `[1.7413, 1.7425]`.  P124.014 §3 disclaims convergence explicitly, so this
   is not a contradiction of its stated scope; but its four printed decimals
   must not be cited as a bracket, and the `Σ(T)` sign flips reported at
   `refine = 2` near `T = 1.70` do not survive refinement in the same place.
   The **qualitative** conclusions of P124.014 — a genuine first contact
   exists for `Ξ_a`, Gate R fails there, case 2 of the dichotomy is realized —
   are unaffected.

---

## 10. Label

**None.**

`ROW D: NO LABEL CLAIMED, NONE EXPECTED FROM THIS CAMPAIGN.`

> **Lead closing decision (R135.007).** Phase 135 is closed. Part II
> (§§11–16) is accepted as a **reduction with no sign**: the Weil completion,
> the canonical class `K` (`Φ_K = ξ`), the radical, the affine duality `σ_K`
> and the Hodge-index transfer theorem (Thm 12.3, conditional on `h⁰` with
> (a),(b′),(c)) are `PROVED`; the falsifier theorem (Thm 12.4) shows the same
> axioms are inconsistent for `Ξ_a`; two natural `h⁰` constructions are
> examined and neither yields (c). Nothing about the sign is claimed. Next
> campaign: R135_007 §4.

> **Lead closing decision (R134.007).** The opening campaign is
> closed after three construction rounds and two adversarial audits. No label; no sign.
> Paper 46 stands as row D's opening state with: Lemma 3.1, Thm 3.6, Thm 3.7
> (`RESTATEMENT`), the swap law, Thm 5.8 (D.3 retired), the negatives of §6 with
> requirement (R5) — no duality carrying the primitive sector off itself is
> constructed in rows A–C — and the falsifier suite. Withdrawn: Prop 3.6a(iii)
> (false under RH; its retention would have been a statement about the zeros).
> Full text: [R134.007](../../03-research/phase-134-row-d-opening/R134_007_CLOSING_DECISION.md).

This paper contains no positivity statement, no sign, and no statement about
the location of the zeros of `ζ` outside the comparison theorem (1.9), cited
from Paper 45, and the classical equivalence of Theorem 3.7, in which the
equivalence *is* with RH and every classical ingredient is named in §8.

> **[phase 135.]**  Part II (§§11–14) adds the canonical class `K` (`Φ_K = ξ`,
> Pólya's kernel), the Weil completion `D^W`, the radical `𝓝_∞`, the affine
> duality `σ_K` closing §9.1(3a), and the Hodge-index transfer theorem
> (Theorem 12.3), which reduces row D's target to the existence of one function
> `h⁰` with three properties — together with Theorem 12.4, which proves those
> three properties **inconsistent** for the falsifier `Ξ_a`, so that no
> **model-free** derivation of the three properties can exist (Restatement
> 12.4a, a schema about *derivations*: it excludes no function `h⁰`, and
> whether the Euler product must enter the *definition* of `h⁰` is not proved
> and survives only as the heuristic Remark 12.4b).
> **[CORRECTED, phase 135 round 3, finding N4 of `R135_005`: round 2 wrote
> "so that any `h⁰` must use the Euler product", the claim withdrawn under
> finding M1.  §10 states this paper's label and must match §14.5.]**  **Still no label, and still no sign**: every
> theorem of Part II holds verbatim for `Ξ_a`, and each says so in its own
> remark.  Eight further blueprint claims are refuted or repaired (§14.4).

**What the paper delivers, graded after round 2.**

| item | grade |
|---|---|
| Lemma 3.1 (`Π` is a bijection onto `P_T`), Theorem 3.6 (`𝔏 = −Π²(W_{fin}+ω_∞)`, `Π²ϖ = 0`), Proposition 3.6a(i),(ii) (`ϖ` and `W_{fin}` are individually **not** tempered) | `PROVED` |
| Remark 3.6b (temperedness of `𝔏` is a PNT-type growth statement, implied by RH, **not decided here**) | `OPEN`, stated in both directions |
| Theorem 3.7, the state reformulation | **`RESTATEMENT`** (`CLASSICAL` + `PROVED-IN-REPOSITORY`) |
| Theorem 4.1 (the dichotomy on the true carrier) | `PROVED-IN-REPOSITORY`, **conditional on `T_q < ∞`** |
| Theorem 4.2(i),(ii), Theorem 4.3 (the swap law), Corollary 4.4, Theorem 4.6, Finding 4.8 | `PROVED` |
| Theorem 4.2(iii), Observation 4.7, all tables of §4 and §5.4 | `COMPUTATIONAL-ILLUSTRATION`, under Warning 4.5a |
| Theorems 5.2, 5.5, 5.8 | `PROVED`; Theorem 5.6 `PROVED` from its own hypothesis; Remark 5.4(iii) `OPEN` |
| Theorems 6.1, 6.3–6.7; Definition 6.8's clause (R5) and its two-line vacuity argument | `PROVED` negatives — **six** after round 3 |
| Definition 6.8 as a synthesis, and the duality (R5) demands | `OPEN`; `NOT CONSTRUCTED` |
| Theorems 7.1, 7.4, Proposition 7.5(a) | `PROVED`; 7.5(b),(c) declared unanswered |
| **[phase 135, round 2]** Lemma 11.2, Thms 11.3, 11.5, Lemma 11.4a, Thms 11.7, 11.8, Lemma 11.9, Thms 11.10, 11.11, Prop 11.11a, Thms 11.12, 11.13, 11.14, 12.2, 12.2a, 12.3, Lemma 12.4A, Prop 12.4B, Thm 12.4, Prop 12.6, Thms 13.2, 13.5, Lemmas 13.5a, 13.5b, Thm 13.6, Thm 14.3 | `PROVED` |
| **[phase 135, round 2]** Restatement 12.4a, Restatement 13.3 | `RESTATEMENT (schema)` — recast from round 1's `PROVED`, finding M1 |
| **[phase 135, round 2]** Remark 12.4b (the Euler-product reading), Remark 13.7 (unimodularity as the discriminating datum), Remark 14.5a (sections indexed by pairs) | `HEURISTIC` — no claim |
| **[phase 135, round 2]** the growth bound (13.4) of round 1, and with it the closure of the route on the **full** lattice `Λ_W` | `WITHDRAWN` / `OPEN` — finding M8; Theorem 13.6 closes every finite truncation |
| **[phase 135]** Prop 12.5 (supersession of Definition 6.8), Props 14.1, 14.2 | `RESTATEMENT` / `PROVED-IN-REPOSITORY` |
| **[phase 135, round 2]** Definition 13.4's `h⁰_{\mathbb Z}`, and every functional of `H⁰(E)` alone | `REFUTED` as a route **on every finite truncation** (Thm 13.6(ii)) and off `\{\deg > 0\}` (Rem 13.5c); `PROVED` as structure (Thms 13.2, 13.5, Lemmas 13.5a, 13.5b); **`OPEN` on the full lattice** (item (23)) and **reopened** for functionals of `H⁰` alone (item (22)) |
| **[phase 135]** Finding 13.8 (three genera), §14.5 items 16–19 | `OPEN`; no reconciliation asserted |
| **row D** | **no label** |

Its deliverable is a reformulation with a named missing object, graded
`RESTATEMENT` (§3); two small new theorems inside it (Lemma 3.1,
Theorem 3.6, with Proposition 3.6a(i),(ii)); one new structural law (§4.3); one
deflation theorem for the finite-inertia programme (§5.3); five negatives with
counterexamples and a corrected requirement list (§6); a falsifier suite tied
to a theorem of row B (§7); and a record of **nine** refuted or repaired
blueprint claims (§9.2), **ten** round-2 repairs (§9.2a), **one** round-3
erratum withdrawing a round-2 repair that overshot (§9.2b), and three findings
against the corpus, two of them confirmed by independent re-run and one
partially withdrawn on audit (§9.3).

**Route status recorded with the campaign's close: D.3 is retired as a
programme item (§9.1(13)), with Theorem 5.8 kept as its result.**

**No sign is claimed, asserted or suggested anywhere in this paper.**

---

---

# PART II — the canonical class, the affine duality, and the transfer theorem

**[ROUND 2, phase 135 (`R135_004`).  Part II has been through one adversarial
audit (`R135_002`, findings M1–M17) and one final audit (`R135_003`, findings
LF1–LF7), and every mandatory repair of the earlier §4 ruling is carried out in
place, marked in place, and tabulated in the new **§14.4a** (repair ledger and
withdrawal table).  The round-2 outcome is **weaker than round 1 claimed**:
round 1's Corollary 12.4a was a non-sequitur and is now a schema about
admissible proofs (Restatement 12.4a); Theorems 13.3 and 13.7, which rested on
it, are withdrawn as quantified statements and survive as a schema and a
heuristic; round 1's growth bound (13.4) is withdrawn in full, and §13's route
closure now holds on every **finite truncation** of the lattice and is `OPEN`
on the full one.  Four repairs make the paper stronger: Theorem 11.14 is
re-proved on the spectral side and no longer needs the archimedean kernel or
Chebyshev's bound; Definition 11.4 is by polarization; the `Ξ_a`-analogue of
Paper 45 Theorem 10.4 is written out in full (Lemma 12.4A, Proposition 12.4B);
and both long scripts now run in seconds and exit `0`.  Four new open items,
(20)–(23), are added to §14.5.]**

**[NEW, phase 135 (`R135_000`, `R135_001`).  Part II adds §§11–14 and changes
nothing in §§0–10 except three cross-reference notes, in §6.3, §9.1(3),(3a) and
§10, which point at the supersession proved in §12.4.  The boxed target of
§0.1 is unchanged, the label of §10 is unchanged (**None**), and no sign is
claimed, asserted or suggested anywhere in Part II.  Seven blueprint claims of
`R135_000` are refuted or repaired; they are marked in place and tabulated in
§14.4.]**

**Standing rule for Part II, restated because this is where it bites.**  The
completed zeta function `ξ(s)` is **data**, exactly as `ζ'/ζ` is data inside
Paper 43's symbol `\hat T` and inside Paper 45 Theorem 9.4.  A class defined by
`Φ_K = ξ` uses the *function*; it uses no statement about where its zeros are,
and every theorem below is stated so that its proof survives the replacement of
`ξ` by the falsifier `Ξ_a`, whose zeros are **not** on the critical line.  Where
a theorem survives that replacement it carries **no sign**, and its own remark
says so.

---

## 11. D.6–D.7 — the Weil class, the canonical class, the radical, the degree

### 11.0 Why an extension is needed at all, and what it is not

Rows A–C work on `D_A = C_c^∞(C_S)` and on the filtered colimit
`D_A^∞ = \mathrm{colim}_S D_A(S)` of Paper 43 Theorem 8A.7c.  **Every element of
`D_A^∞` is compactly supported**: the colimit enlarges the chart, not the
support.  The canonical class constructed below is not compactly supported, so
it is not in `D_A^∞`, and the enlargement it lives in is **not** the colimit.

**Finding 11.0 (`PROVED`; and it repairs blueprint §1's expectation and
answers D.10's question).**  `T_∞` does **not** extend to a non-compactly
supported radial test by its own formula.  Paper 43 (8A.21) reads
`T_∞(F) = T_S(F) + Σ_{ℓ ∉ S_f, \log ℓ ≤ R(F)}(\log ℓ)Σ_{k≠0}ℓ^{−|k|/2}F(δ_S(ℓ^{−k}))`
and is a **finite** sum *because* `R(F) < ∞`.  For a test of unbounded support
the outer sum is over all primes `ℓ ∉ S_f` and the stabilization statement
8A.7c(b) — whose whole content is that the sum terminates — is unavailable.
So the completion on which the canonical class lives is obtained from the
**explicit formula**, not from the colimit trace, and `D^W` below is a
`D_A^{rad}`-module (Theorem 14.3) but is **not** the colimit `T_∞`-domain.
∎  `PROVED` (by inspection of (8A.21) and the hypothesis `R(F) < ∞` of
Theorem 8A.7c(a),(b))

### 11.1 The Weil class `D^W`

**Definition 11.1.**  `D^W` is the set of real functions `g` on `R` such that
`g ∈ C²(R)` and there is `ε > 0` with

    g^{(j)}(t) = O\big(e^{−(1+ε)|t|}\big)  \qquad (j = 0,1,2, \ |t| → ∞).  (11.1)

`g^∨(t) := g(−t)`; `⋆` is convolution; `τ_a g := g(\cdot − a)` is the modulus
translation; `Π = −∂_t² + ¼`.

**Lemma 11.2 (`PROVED`).**  (i) `D^W` is a real vector space, closed under
`g ↦ g^∨`, under `τ_a` for every `a ∈ R`, and under convolution; it is a
commutative real `⋆`-algebra with involution `∨`.
(ii) `C_c^∞(R) ⊂ D^W`, and `Π(D^W_4) ⊆ D^W`, where `D^W_4 ⊂ D^W` is the
subclass of `g ∈ C⁴(R)` satisfying (11.1) for `j = 0,1,2,3,4`.
**[REPAIRED, phase 135 round 2, finding M14 of `R135_002`: `(Πg)'' = −g'''' +
¼g''`, so membership of `Πg` in `D^W` needs the **decay** (11.1) for `j = 3,4`
and not merely the differentiability `g ∈ C⁴`.  `K`, `τ_aK` and `C_c^∞(R)` all
lie in `D^W_4` — Theorem 11.7(ii) gives (11.1) for every derivative of `K` —
and `Π` is applied to nothing else in Part II.]**
(iii) For `g ∈ D^W` the Mellin transform `Φ_g(s) = ∫g(t)e^{(s−1/2)t}dt`
converges absolutely and is holomorphic in the open strip
`S_ε := \{−½−ε < \mathrm{Re}\,s < \tfrac32+ε\}`, which contains the **closed**
critical strip in its interior, and

    |Φ_g(s)| ≤ \frac{C_2(g,σ)}{|s−½|²} ,\qquad
    C_2(g,σ) := ∫|g''(t)|e^{(σ−½)t}dt ,                                (11.2)

uniformly for `\mathrm{Re}\,s = σ` in any closed substrip of `S_ε`.
(iv) `Φ_{g^∨}(s) = Φ_g(1−s)`, `Φ_{τ_a g}(s) = e^{(s−½)a}Φ_g(s)`,
`Φ_{g⋆h} = Φ_gΦ_h`, `Φ_{Πg}(s) = s(1−s)Φ_g(s)`.
(v) `\ker Π ∩ D^W = 0`.

*Proof.*  (i) Only convolution needs a word: if `|g|,|h| ≤ Ce^{−(1+ε)|t|}` then
`|g∗h|(t) ≤ C²(1+|t|)e^{−(1+ε)|t|} ≤ C'e^{−(1+ε')|t|}` for any `0 < ε' < ε`,
and the same for the first two derivatives, which fall on one factor.
(ii) `C_c^∞ ⊂ D^W` is immediate.  For `g ∈ D^W_4`, `Πg = −g''+¼g` is `C²` and
`(Πg)^{(j)} = −g^{(j+2)} + ¼g^{(j)}` for `j = 0,1,2` obeys (11.1) because
`g^{(i)}` does for `i ≤ 4`; so `Πg ∈ D^W`.  Every element to which `Π` is
applied below (`K`, `τ_aK`, `C_c^∞` tests) is `C^∞` with all derivatives
obeying (11.1), hence in `D^W_4`.
(iii) Absolute convergence for `|σ−½| < 1+ε` is (11.1) with `j = 0`;
holomorphy by Morera.  Two integrations by parts give
`Φ_g(s) = (s−½)^{−2}∫g''(t)e^{(s−½)t}dt`, the boundary terms vanishing by
(11.1) with `j = 0,1`, which is (11.2).
(iv) are the substitutions `t ↦ −t`, `t ↦ t+a`, Fubini, and two integrations by
parts.  (v) `\ker Π = \mathrm{span}\{e^{t/2},e^{−t/2}\}` (Theorem 3.6), and
neither is `O(e^{−(1+ε)|t|})`.  ∎  `PROVED`

**`REFUTED` (blueprint D.6(i): the decay exponent).**  The blueprint proposes
`g, g'` of decay `O(e^{−(½+ε)|t|})` — "Weil's class" — and asserts that `I_∞`
extends to it "with (9.9) valid, `CLASSICAL`".  **Three things are wrong with
that as an instruction to this paper.**

 (a) With decay `e^{−(½+ε)|t|}`, `Φ_g` is holomorphic only in
     `−ε < \mathrm{Re}\,s < 1+ε`.  The proof of Paper 45 Theorem 9.4 — the
     repository's only proof of the explicit formula — runs on the line
     `L_c`, `c > 1`, where `ζ'/ζ(s) = −Σ_nΛ(n)n^{−s}` converges absolutely
     ((E1)); that line is **outside** the domain of `Φ_g`.  The proof does not
     extend verbatim, and no repair of it is offered here.
 (b) With only `g, g'` controlled, (11.2) holds with exponent `1` instead of
     `2`, and `Σ_ρ|γ_ρ|^{−1} = ∞` by (E3d): **the zero sum is then not known
     to converge absolutely**, and the blueprint's own demand for "an
     absolutely convergent zero sum" fails on its own class.  Two derivatives
     are needed, and are imposed in (11.1).
 (c) The identity *is* classical on a class of that size (Weil 1952; Barner
     1981, in the sharp form "`g` of bounded variation, normalized, with
     `e^{(½+δ)|t|}g(t)` bounded"), with the zero sum in the **symmetric**
     order and not known to be absolutely convergent.  That is an
     `IMPORTED` statement, and it is **not used anywhere below**: every
     theorem of Part II is proved on `D^W` of Definition 11.1, where the
     repository's own proof applies unchanged.

**Theorem 11.3 (the explicit formula on `D^W`; `PROVED-IN-REPOSITORY`,
by verbatim extension of Paper 45 Theorem 9.4 / Corollary 9.4a).**
Hypotheses carried: `c = 0`; the trace is `T_∞`; imports (E1)–(E5) and (E3d).
Let `h ∈ D^W` be **real and even**.  Then `Σ_ρΦ_h(ρ)` converges **absolutely**
and

    Σ_ρ Φ_h(ρ) = Φ_h(0) + Φ_h(1)
       + \frac1{2π}∫_R \hat h(τ)\big[\mathrm{Re}\,ψ(¼+iτ/2) − \log π\big]dτ
       − Σ_{n ≥ 2}Λ(n)n^{−1/2}\big[h(\log n)+h(−\log n)\big] ,          (11.3)

the prime sum being absolutely convergent (no longer finite), and
`\hat h(τ) = Φ_h(½+iτ)`.  Writing `⟨h,W_{fin}+ω_∞⟩` for **the prime sum of the last line minus the
archimedean integral of the previous one** (`\mathrm{PRIME} − \mathrm{ARCH}`;
the sign convention of (1.4) and Theorem 3.6 — **[CORRECTED, phase 135 round 2,
finding M10 of `R135_002`: round 1 wrote "the last line minus the previous
one", which with the displayed signs reads `−\mathrm{PRIME}−\mathrm{ARCH}`.
The intended and used convention is `\mathrm{PRIME}−\mathrm{ARCH}`, which is
what (11.4) requires and what the numerics compute]**),

    ⟨h, W_{fin}+ω_∞⟩ = Φ_h(0)+Φ_h(1) − Σ_ρ Φ_h(ρ) .                    (11.4)

*Proof.*  Every step of the proof of Corollary 9.4a is checked against
Definition 11.1.  *Lemma 9.1's replacement:* `Φ_h` is holomorphic on `S_ε` ⊇
`\{−½ ≤ \mathrm{Re}\,s ≤ \tfrac32\}` (Lemma 11.2(iii)), `Φ_h(1−s) = Φ_h(s)`
because `h` is even (the computation of Corollary 9.4a, unchanged), and
`Φ_h(½+iτ) = \hat h(τ)` is real and even.  *The decay (9.1):* replaced by
(11.2), `|Φ_h(s)| ≤ C_2/|s−½|²` uniformly on `−½ ≤ \mathrm{Re}\,s ≤ \tfrac32`;
this is **two** powers, which is exactly what the three contour steps need and
all that they need.  *Lemma 9.2:* run the rectangle `R_j` with
`c := \tfrac32 > 1` (admissible, since `\tfrac32 ∈ S_ε`) and `1−c = −½`.  The
horizontal sides have bounded length and carry
`|Φ_h·ξ'/ξ| = O(X_j^{−2}\log²X_j) → 0` by (11.2) and (E3c); the vertical sides
converge absolutely by (11.2) and `|ξ'/ξ| = O(\log|s|)` on `L_{3/2}`
((E1),(E4)).  *Step (a):* unchanged — `A_0` has its two simple poles at
`s = 0,1`, both interior to `−½ < \mathrm{Re}\,s < \tfrac32`, with residues
`Φ_h(0)`, `Φ_h(1)`.  *Step (b):* `A_Γ` is holomorphic in `\mathrm{Re}\,s > 0`
and `O(\log|s|)` there, so `L_{3/2} → L_{1/2}` is legitimate with horizontal
contributions `O(X_j^{−2}\log X_j) → 0`.  *Step (c):* `Σ_nΛ(n)n^{−3/2} < ∞`
by (E1), so Fubini applies on `L_{3/2}`; `Φ_h(s)n^{−s}` is holomorphic on
`½ ≤ \mathrm{Re}\,s ≤ \tfrac32` (no longer entire, and it does not need to be),
so the shift to `L_{1/2}` crosses no singularity, with horizontals
`O(X_j^{−2})` uniformly in `n` since `|n^{−s}| ≤ n^{−1/2}` there; Fourier
inversion (E5) gives `n^{−1/2}h(−\log n)`, and evenness of `h` doubles it.
The prime sum is now infinite and converges absolutely:
`Σ_nΛ(n)n^{−1/2}|h(\pm\log n)| ≤ CΣ_nΛ(n)n^{−1/2}n^{−(1+ε)} < ∞`.
*Absolute convergence of the zero sum:* `|Φ_h(ρ)| ≤ C_2|ρ−½|^{−2} = O(|γ_ρ|^{−2})`
by (11.2), and `Σ_ρ|γ_ρ|^{−2} < ∞` by (E3d) and partial summation
(Paper 45 Remark 9.8).  ∎  `PROVED-IN-REPOSITORY`

**Definition 11.4 (the extended form, by polarization).**
**[REPAIRED, phase 135 round 2, findings M2 of `R135_002` and LF3 of
`R135_003`.  Round 1 set `I_∞(F,G) := ⟨F⋆G^∨, W_{fin}+ω_∞⟩` and justified it by
the parenthetical "real and even when `F,G` are real, by `h^∨ = h`".  **That
parenthetical is false**: `(F⋆G^∨)^∨ = F^∨⋆G`, which for `F` even and
`G = τ_1F` is `τ_{−1}(F⋆F) ≠ τ_1(F⋆F)`.  Theorem 11.3 — the only statement
giving `⟨h,W_{fin}+ω_∞⟩` a meaning — is stated and proved for real **even**
`h`, so the round-1 definition was literally undefined off the diagonal.  The
repair below is the standard one and costs no theorem.]**

For `X ∈ D^W` real, `X⋆X^∨` is real **and even** (`(X⋆X^∨)^∨ = X^∨⋆X = X⋆X^∨`
by commutativity of `⋆`), so Theorem 11.3 applies to it; put

    Q(X) := ⟨X⋆X^∨,\; W_{fin}+ω_∞⟩ ,\qquad
    I_∞(F,G) := \tfrac14\big[Q(F+G) − Q(F−G)\big] .                    (11.5)

**This is a definition by the arithmetic side: it names no zero.**  On
`D_A^{rad}` it is Paper 43 Definition 9.2 read through (1.3), i.e.
`I_∞(Γ_F,Γ_G) = T_∞(Γ_F⋆Γ_G^†)`, whose polarization is the same.

**Lemma 11.4a (the three descriptions agree; `PROVED`).**  For real
`F,G ∈ D^W` put `h := F⋆G^∨` and `h_{\mathrm{ev}} := \tfrac12(h + h^∨) =
\tfrac12(F⋆G^∨ + F^∨⋆G) ∈ D^W`, which is real and even.  Then

    I_∞(F,G) = ⟨h_{\mathrm{ev}},\; W_{fin}+ω_∞⟩ ,                       (11.5a)

and when `h` is itself even (in particular when `F = G`) both sides equal
`⟨h, W_{fin}+ω_∞⟩`, so (11.5) extends the round-1 formula wherever the latter
was defined.  `I_∞` is symmetric and bilinear.

*Proof.*  `Φ_{h_{\mathrm{ev}}}(s) = \tfrac12\big(Φ_F(s)Φ_G(1−s) +
Φ_F(1−s)Φ_G(s)\big)` by Lemma 11.2(iv).  Substituting in (11.4) and using that
the zero multiset is invariant under `ρ ↦ 1−ρ` with multiplicities (E2) — the
zero sum being absolutely convergent, so it may be re-indexed — gives exactly
the right-hand side of (11.6) below.  The same substitution applied to
`X⋆X^∨` gives `Q(X) = 2Φ_X(0)Φ_X(1) − Σ_ρΦ_X(ρ)Φ_X(1−ρ)`, a quadratic form in
`X` whose polarization is, term by term (again using `ρ ↦ 1−ρ` inside the
absolutely convergent sum), the same right-hand side.  Hence (11.5a), and
symmetry and bilinearity are read off it.  ∎  `PROVED`

**Theorem 11.5 (the comparison identity on `D^W`; `PROVED`).**
Hypotheses as in Theorem 11.3.  For all real `F,G ∈ D^W` — **no evenness
assumed on `F` or `G`** —

    I_∞(F,G) = Φ_F(0)Φ_G(1) + Φ_F(1)Φ_G(0) − Σ_ρ Φ_F(ρ)Φ_G(1−ρ) ,      (11.6)

the zero sum absolutely convergent; in particular, for `F = G`,
`I_∞(F,F) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)`, which is (9.9) of (1.9), now
on `D^W`.  `I_∞` is symmetric and bilinear.

*Proof.*  This is Lemma 11.4a, whose proof is the substitution
`Φ_{F⋆G^∨}(s) = Φ_F(s)Φ_G(1−s)` (Lemma 11.2(iv)) into (11.4) at `s = 0,1` and
at the zeros, symmetrized by `ρ ↦ 1−ρ`.  The zero sum converges absolutely by
(11.2) and (E3d), which is what licenses the re-indexing and the polarization
term by term.  ∎  `PROVED`

**Definition 11.6.**  `deg F := Φ_F(0) + Φ_F(1) = ∫F(t)\,2\cosh(t/2)\,dt`;
`P^W := \{F ∈ D^W : Φ_F(0) = Φ_F(1) = 0\}` (**primitive**, (1.7));
`F` is **effective**, written `F ≥ 0`, if `F(t) ≥ 0` for every `t`.

### 11.2 The canonical class

**[NAMING CORRECTION OF RECORD, entered with Part III (§21).  The class `K`
constructed below is called *the canonical class* throughout Parts I–II by
analogy with Weil's `K`.  The function-field model of §21 settles the analogy
against that name: under the dictionary of Theorem 21.7 the frame's `K`
corresponds to the **ample class** `½(F_1+F_2)` of `C×C`, not to the canonical
class `K_{C×C} = (2g−2)(F_1+F_2)`.  Every statement about `K` in this paper is
unaffected — `K` is used only through `Φ_K = ξ`, `\deg`, `I_∞(F,2K) = \deg F`
and the Serre symmetry `σ_K` — but the name is to be read as a label, and
the geometric content of `K` is ampleness, not canonicity.]**

**Definition–Theorem 11.7 (the canonical class; `CLASSICAL` + `PROVED`).**
Let

    K(t) := Σ_{n ≥ 1}\big(4π²n⁴e^{9t/2} − 6πn²e^{5t/2}\big)e^{−πn²e^{2t}} .  (11.7)

Then:

 (i) *(`CLASSICAL`)* the series converges locally uniformly together with all
     its derivatives; `K` is real, **even**, `K(t) > 0` for every `t`, and
     `Ξ(τ) := ξ(½+iτ) = ∫_R K(t)e^{iτt}dt = 2∫_0^∞K(t)\cos(τt)\,dt`.
     **[phase 135 round 2, finding LF6 of `R135_003`: given evenness, the
     positivity `K > 0` is elementary and needs no import.  For `u ≥ 0` each
     term of (11.7) is `2πn²e^{5u/2}e^{−πn²e^{2u}}\big(2πn²e^{2u} − 3\big)`,
     and `2πn²e^{2u} ≥ 2π > 3`, so every term is strictly positive and
     `K(u) > 0` for `u ≥ 0`; by evenness `K > 0` on all of `R`.  Only evenness
     and the Fourier identity are now imported.]**
     This is Riemann's integral representation in Pólya's normalization:
     Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev.
     Heath–Brown), §10.1, equation (10.1.4) and the two displays following it
     (evenness and positivity of `Φ = K`); G. Pólya, *Bemerkung über die
     Integraldarstellung der Riemannschen ξ-Funktion*, Acta Math. **48**
     (1926), 305–317.  Import **(X12)** of §15.
 (ii) *(`PROVED`)* with `ω(x) := Σ_{n≥1}e^{−πn²x}` and `x = e^{2t}`,

          K(t) = 4x^{9/4}ω''(x) + 6x^{5/4}ω'(x) ,                       (11.8)

     and `K(t) = 4π²e^{9|t|/2}e^{−πe^{2|t|}}\big(1+O(e^{−3πe^{2|t|}})\big)`
     as `|t| → ∞`; the same bound holds for every derivative with an extra
     polynomial factor in `e^{2|t|}`.  Consequently
     **`K ∈ D^W`, and so is `K^{(j)}` and `τ_aK` for every `j` and every `a`.**
 (iii) *(`PROVED`)* `Φ_K(s) = ξ(s)` for every `s ∈ C` (both sides entire), and
     therefore

          Φ_K(0) = Φ_K(1) = ξ(0) = ξ(1) = ½ ,\quad M(K) = (½,½) ,
          \deg K = 1 ,\quad ∫K = Φ_K(½) = ξ(½) = 0.497120778188\ldots     (11.9)

*Proof.*  (ii) Term by term, `Σ4π²n⁴e^{−πn²x} = 4ω''(x)` and
`Σ(−6πn²)e^{−πn²x} = 6ω'(x)`; substituting `e^{9t/2} = x^{9/4}`,
`e^{5t/2} = x^{5/4}` gives (11.8).  *Decay as `t → +∞`* (`x → ∞`) is the `n=1`
term, the rest being `O(e^{−4πx})`.  *Decay as `t → −∞`* (`x → 0⁺`) is the
point at which the blueprint's worry about `g'` is settled, and it is a
cancellation, not an estimate.  The theta functional equation
`2ω(x)+1 = x^{−1/2}(2ω(1/x)+1)` gives
`ω(x) = ½x^{−1/2} − ½ + x^{−1/2}ω(1/x)`, and `ω(1/x)` together with all its
derivatives is `O(e^{−π/x})`.  Hence
`ω'(x) = −¼x^{−3/2} + O(x^{−5/2}e^{−π/x})` and
`ω''(x) = \tfrac38x^{−5/2} + O(x^{−9/2}e^{−π/x})`, so

    K(t) = 4x^{9/4}·\tfrac38x^{−5/2} + 6x^{5/4}·(−¼x^{−3/2}) + O(x^{−9/4}e^{−π/x})
         = \tfrac32x^{−1/4} − \tfrac32x^{−1/4} + O(x^{−9/4}e^{−π/x}) ,

**the two leading terms cancel exactly**, and `K(t) = O(e^{9|t|/2}e^{−πe^{2|t|}})`
as `t → −∞`.  Evenness, which is (i), then upgrades this to the stated
two-sided asymptotic.  All derivatives: differentiate the two displays; each
`∂_t` produces a factor bounded by `Ce^{2|t|}`, which is absorbed.  (11.1) holds
for every exponent, in particular for `1+ε`, so `K ∈ D^W`; `D^W` is
`τ`-stable (Lemma 11.2(i)).
(iii) `Φ_K(½+iτ) = ∫K(t)e^{iτt}dt = Ξ(τ) = ξ(½+iτ)` by (i); `Φ_K` is entire
(the integral converges for every `s` by (ii)) and `ξ` is entire (E2), and they
agree on a line, hence everywhere.  `ξ(1) = \lim_{s→1}½s(s−1)π^{−s/2}Γ(s/2)ζ(s)
= ½π^{−1/2}Γ(½) = ½`, and `ξ(0) = ξ(1)` by (E2).  ∎  `PROVED`

*Numerical confirmation (`COMPUTATIONAL-ILLUSTRATION`;
`scripts/polya_class.py --check`):*  `K(t) = K(−t)` from the literal series at
`t = 0.3,0.5,1.0` to `10^{−121}`; `K > 0` on the grid
`t = −2.0(0.05)2.0` with `\min K = 1.0204\cdot10^{−69}` at `|t| = 2`;
`Φ_K(s) = ξ(s)` at `s = 0, 1, ½, \tfrac32, ½+10i` to `10^{−15}`;
`∫K = 0.497120778188314`; `\deg K = 1`.

**Theorem 11.8 (how `K` pairs; `PROVED`).**  For every `F ∈ D^W` and every
`a ∈ R`, `n ≥ 1`:

 (i) `Φ_K(1−ρ) = ξ(1−ρ) = 0` at every zero `ρ`, so the zero sum in (11.6)
     against `K` vanishes identically and

          I_∞(F,K) = ½\big(Φ_F(0)+Φ_F(1)\big) = ½\,\deg F ;              (11.10)

 (ii) `I_∞(K,K) = 2ξ(0)ξ(1) = ½`, and `⟨K,W_{fin}+ω_∞⟩ = 1 = \deg K`
     by (11.4) and `Σ_ρξ(ρ) = 0`.  **[CORRECTED, phase 135 round 2, finding
     M12 of `R135_002`: round 1 also wrote this number as "`T_∞(K)`".  Finding
     11.0 proves that `T_∞`'s own formula (8A.21) does not converge on a test
     of unbounded support, so the symbol `T_∞(K)` denotes nothing and is not
     used;  the bracket `⟨·,W_{fin}+ω_∞⟩` of Theorem 11.3 is what is meant
     here and everywhere below.]**;
 (iii) `M(τ_aK) = ½(e^{a/2},e^{−a/2})` and
     `I_∞(F,τ_aK) = ½\big(e^{a/2}Φ_F(0) + e^{−a/2}Φ_F(1)\big)`; at
     `a = \log n` the weights are `n^{\pm1/2}`, which are exactly the bidegrees
     `M(Frob_n) = (n^{1/2},n^{−1/2})` of Paper 44 Theorem 3ter.6(iii);
 (iv) `K ∈ (P^W)^{⊥_{I_∞}}`, and `K ≠ 0`;
 (v) `2K` is a **degree form**: `I_∞(F,2K) = \deg F` for every `F ∈ D^W`.

*Proof.*  (i) is (11.6) with `G = K`, `Φ_K = ξ` and `Φ_K(0)=Φ_K(1)=½`; the
zero sum is absolutely convergent (Theorem 11.3) and every term is `0`.
(ii) the first from (i) with `F = K`, `\deg K = 1`; the second from (11.4) with
`h = K`.  (iii) Lemma 11.2(iv) and (i), since `Φ_{τ_aK}(1−ρ) = 0` too.
(iv) is (11.10) with `\deg F = 0`.  (v) is (11.10) doubled.  ∎  `PROVED`

*Numerical confirmation (`scripts/polya_class.py --check`,
`scripts/canonical_pairings.py --check`):*  for `h = K`,
`\mathrm{ARCH} = −0.9973107840892264`,
`\mathrm{PRIME} = 0.00268921591077361`, so
`Φ_K(0)+Φ_K(1)+\mathrm{ARCH}−\mathrm{PRIME} = 1.0\cdot10^{−26}` and
`⟨K,W_{fin}+ω_∞⟩ = \mathrm{PRIME}−\mathrm{ARCH} = 1` to `1.3\cdot10^{−26}`;
for `h = K⋆K`, `I_∞(K,K) = \mathrm{PRIME}−\mathrm{ARCH} = 0.5` to
`6.5\cdot10^{−27}` (all from `polya_class.py --check`, exit `0`).
**`[phase 135 round 2, R135_004`: `canonical_pairings.py` has been rewritten
(the round-1 version nested tanh–sinh quadratures and could not resolve the
oscillatory factor `n^{−iτ}` of a translate, which is why `P2` failed by `0.6`
at `n = 4`, and it also truncated the prime sum at `n = 12`, whereas a
translate by `\log n` shifts the effective cut-off by a factor `n`).  With
fixed composite Gauss–Legendre panels and the prime sum carried to `n = 160`,
**`canonical_pairings.py --check` now exits `0` in 28 s** and the round-1
failure is gone.  Reproduced: `I_∞(F,K) = ½\deg F` to `2\cdot10^{−15}` (`P1`,
both test classes; the round-1 figure `3\cdot10^{−18}` was an `mpmath`
tolerance and is withdrawn), `I_∞(F,τ_{\log n}K)` against the ruling
prediction of (iii) to `7\cdot10^{−15}` for `n = 2,3,4` (`P2`), and
`I_∞(τ_a ΠK, F) = 0` to `7\cdot10^{−14}` (`P4`); and (`P3`) the comparison
identity (11.6) on the primitive compactly supported test `Π(\text{bump})`,
arithmetic side `I_∞ = −66.166750865` against
`−Σ_ρΦ_F(ρ)Φ_F(1−ρ) = −66.1667475987` over the first `120` zero pairs, a
relative discrepancy `5\cdot10^{−8}` — which is the truncation of the zero sum,
not a discrepancy of the identity.  The arithmetic is `float64`, so
`10^{−14}` is the floor, not a claim of more.  **`P3` is a test of an identity
and is not evidence about any sign.**]**
These are tests of identities.  **They carry no sign.**

**Remark 11.8a (the falsifier, said at once).**  Put `Ξ_a(s) := ξ(s+a)ξ(s−a)`,
`0 < a < ½`, and `K_a := (e^{at}K) ⋆ (e^{−at}K)`.  Then
`Φ_{K_a}(s) = ξ(s+a)ξ(s−a) = Ξ_a(s)`, `K_a > 0`, `K_a^∨ = K_a`, and
`K_a ∈ D^W` (the super-exponential decay of `K` absorbs `e^{\pm a|t|}`).
Everything in Theorem 11.7 and Theorem 11.8 holds verbatim for `Ξ_a` with the
four-element polar set `\{−a,a,1−a,1+a\}` of `Ξ_a` in place of `\{0,1\}`
(§12.5).  **Theorems 11.7 and 11.8 therefore carry no sign whatever**, and the
same is true of every theorem in §11: each is a statement about a completed
function with a functional equation, and `Ξ_a` is one.

### 11.3 The orthogonal complement of the primitive sector

**[ADDITION OF RECORD P46-3, entered with Part III.  The results of this
subsection are completed in §17 by the `I_∞`-orthogonal splitting
`D^W = Λ ⊥ P^W` with `Λ = span(K, K_odd)` a hyperbolic plane of signature
`(1,1)` and `K_odd = (2\sinh(a/2))^{−1}(τ_aK − τ_{−a}K)` an explicit odd class
of `D^W` (Theorem 17.5).  The ingredients are all here — Theorem 11.8, Theorem
11.10 and the ruling plane `B_T` of (1.8) — but the splitting is not stated in
Part II, and it is what converts Proposition 14.1's statement about *ruling
data* into a statement about *classes*.]**

**Lemma 11.9 (the separation lemma; `PROVED`).**  Let `(c_ρ)` be complex
numbers indexed by the zeros of `ξ` **with multiplicity**, depending only on
the zero (equal on the copies of a multiple zero), with `Σ_ρ|c_ρ| < ∞`.  Let
`α,β ∈ C`.  Suppose

    Σ_ρ c_ρ\,e^{(ρ−½)t} = α e^{t/2} + β e^{−t/2}  \qquad\text{for all } t ∈ R.
                                                                        (11.11)

Then `α = β = 0` and `c_ρ = 0` for every `ρ`.

*Proof.*  The left side converges absolutely and locally uniformly, because
`|e^{(ρ−½)t}| ≤ e^{|t|/2}` (the zeros satisfy `0 < \mathrm{Re}\,ρ < 1`, (E2)),
so both sides are continuous functions and the identity is an identity of
functions.  For `\mathrm{Re}\,s > 1` put `z := s − ½`, so `\mathrm{Re}\,z > ½`,
and take the Laplace transform of (11.11) over `[0,∞)`.  Term by term,

    ∫_0^∞ e^{(ρ−½)t}e^{−zt}dt = \frac1{z+½−ρ} = \frac1{s−ρ} ,

and the interchange is legitimate because
`Σ_ρ|c_ρ|∫_0^∞e^{(\mathrm{Re}ρ−½−\mathrm{Re}z)t}dt ≤
 (\mathrm{Re}\,z−½)^{−1}Σ_ρ|c_ρ| < ∞`.  Hence, for `\mathrm{Re}\,s > 1`,

    H(s) := Σ_ρ \frac{c_ρ}{s−ρ} = \frac{α}{s−1} + \frac{β}{s} .          (11.12)

Now `H` is holomorphic on `C ∖ Z(ξ)`: the zeros of `ξ` form a discrete set
(E3a), so around any `s_0` there is a disc meeting at most one zero, and on it
the remaining series is dominated by `Σ|c_ρ|/r < ∞`.  At a zero `ρ_0` of
multiplicity `m_{ρ_0}`, `H` has at worst a **simple pole with residue
`m_{ρ_0}c_{ρ_0}`**.  The right-hand side of (11.12) is holomorphic on
`C∖\{0,1\}`, and `0,1 ∉ Z(ξ)` (E2).  Both sides are holomorphic on the
connected open set `U := C ∖ (Z(ξ) ∪ \{0,1\})` and agree on
`\{\mathrm{Re}\,s > 1\} ⊆ U`, hence on `U` by analytic continuation.  So `H`
extends holomorphically across each `ρ_0`, forcing `m_{ρ_0}c_{ρ_0} = 0`, i.e.
`c_{ρ_0} = 0`; this for every zero.  Then `H ≡ 0`, so
`α/(s−1)+β/s ≡ 0`, so `α = β = 0`.  ∎  `PROVED`

**Remark 11.9a (what the proof does and does not use).**  It uses: `ξ` entire
of order `1` with a discrete zero set (E3a); `0 < \mathrm{Re}\,ρ < 1` (E2),
which gives the absolute convergence and the strict separation of the exponents
`ρ−½` from `\pm½`; `ξ(s) = ξ(1−s)` nowhere; and **no** statement about where
the zeros are inside the strip.  It is valid verbatim for `Ξ_a`, with
`\{0,1\}` replaced by the four poles.  It is the rigorous form of the
blueprint's "independence argument", which the blueprint left as an assertion
about "infinite exponential sums"; the Laplace transform converts the
independence question into the elementary observation that a function with a
pole is not a function without one.

**Theorem 11.10 (D.6(iii): the perp of the primitive sector; `PROVED`).**
Let `G ∈ D^W`.  The following are equivalent.

 (a) `I_∞(F,G) = 0` for every primitive `F ∈ C_c^∞(R)`;
 (b) `I_∞(F,G) = 0` for every `F ∈ P^W`;
 (c) `Φ_G(ρ) = 0` at every zero `ρ` of `ξ`.

*Proof.*  (b)⇒(a) is inclusion (`C_c^∞ ⊂ D^W`, Lemma 11.2(ii)).
(c)⇒(b): by (11.6), `I_∞(F,G) = −Σ_ρΦ_F(ρ)Φ_G(1−ρ)` for primitive `F`, and
`Φ_G(1−ρ) = 0` because `1−ρ` is a zero whenever `ρ` is (E2).
(a)⇒(c): put `c_ρ := Φ_G(1−ρ)`, so `|c_ρ| = O(|γ_ρ|^{−2})` by (11.2) and
`Σ_ρ|c_ρ| < ∞` by (E3d).  For primitive `F ∈ C_c^∞`, (11.6) gives
`0 = I_∞(F,G) = −Σ_ρ c_ρΦ_F(ρ) = −⟨𝒮,F⟩` with
`𝒮(t) := Σ_ρ c_ρ e^{(ρ−½)t}`, a **continuous function** by the absolute local
uniform convergence noted in Lemma 11.9, the interchange
`Σ_ρc_ρ∫F e^{(ρ−½)t}dt = ∫F𝒮` being Fubini.  By Lemma 3.1 every primitive
`F ∈ C_c^∞(I_T)` is `ΠH` with `H ∈ C_c^∞(I_T)`, for every `T`; hence
`⟨𝒮,ΠH⟩ = 0` for all `H ∈ C_c^∞(R)`, i.e. `Π𝒮 = 0` in `D'(R)`, i.e.
`𝒮(t) = αe^{t/2}+βe^{−t/2}` for some constants (Theorem 3.6, `Πe^{\pm t/2} = 0`;
the solution space of `(−∂²+¼)u = 0` in `D'(R)` is two-dimensional by
hypoellipticity of an elliptic constant-coefficient operator).  Lemma 11.9 gives
`c_ρ = 0` for all `ρ`, i.e. `Φ_G(1−ρ) = 0`, i.e. (c) by the symmetry of the
zero set.  ∎  `PROVED`

**`REFUTED` (blueprint D.6(iii), second half).**  The blueprint identifies the
perp with `ξ·(\text{entire}) ∩ \mathrm{Mellin}(D^W)`.  **That identification
is not available unconditionally.**  Theorem 11.10 gives vanishing of `Φ_G` at
each zero **to order one**, whatever the multiplicity; `Φ_G = ξ·e` with `e`
holomorphic requires vanishing to order `≥ m_ρ` at every `ρ`.  The two
conditions coincide **iff every zero of `ξ` is simple**, which is `OPEN`.
Unconditionally:

    \{G ∈ D^W : Φ_G|_{Z(ξ)} = 0\} ⊇ \{G : Φ_G = ξ·e,\ e\ \text{holomorphic on }S_ε\},
                                                                        (11.13)

with equality **iff** all zeros of `ξ` are simple.  Nothing below uses the
identification: every use is of the left-hand side, and `K` belongs to the
right-hand side by `Φ_K = ξ` (`e ≡ 1`).  **Recording an equality here would
have been an unproved statement about the zeros of `ζ` inside the one paper
forbidden to make one — the same class of error as the withdrawn Proposition
3.6a(iii) (§9.2b).**

### 11.4 The radical, and the compactly supported case

**Theorem 11.11 (D.7(i): the radical of the extended form; `PROVED`).**
Let `𝓝_∞ := \{N ∈ D^W : I_∞(N,G) = 0 \ ∀G ∈ D^W\}`.  Then

    𝓝_∞ = \{N ∈ D^W : Φ_N(0) = Φ_N(1) = 0 \ \text{and}\ Φ_N(ρ) = 0
             \ \text{at every zero } ρ\} = P^W ∩ (P^W)^{⊥_{I_∞}} .       (11.14)

In particular `𝓝_∞ ≠ 0`: it contains `ΠK` and `τ_a(ΠK)` for every `a`, and
`\deg N = 0` and `I_∞(N,X) = 0` for every `N ∈ 𝓝_∞`, `X ∈ D^W`.  Moreover
`𝓝_∞` is an ideal of the convolution algebra `D^W`, and the same conclusion
holds with `D^W` replaced by `C_c^∞(R)` on the right of the defining condition:
pairing to zero against every **compactly supported** test already forces
membership.

*Proof.*  ⊇ is (11.6): both the polar packet and every term of the zero sum
vanish.  ⊆: let `I_∞(N,G) = 0` for every `G ∈ C_c^∞(R)`.  By (11.6),

    Φ_N(0)Φ_G(1) + Φ_N(1)Φ_G(0) = Σ_ρ Φ_N(ρ)Φ_G(1−ρ)   \qquad ∀G ∈ C_c^∞ .

Since `Φ_G(1) = ∫Ge^{t/2}`, `Φ_G(0) = ∫Ge^{−t/2}` and
`Φ_G(1−ρ) = ∫Ge^{(½−ρ)t}`, and `Σ_ρ|Φ_N(ρ)| < ∞` by (11.2) and (E3d), this
says exactly, as an identity of continuous functions,

    Σ_ρ Φ_N(ρ)\,e^{(½−ρ)t} = Φ_N(0)e^{t/2} + Φ_N(1)e^{−t/2} .

Re-index by `ρ ↦ 1−ρ` (the zero multiset is invariant with multiplicities,
(E2)) to get `Σ_ρ Φ_N(1−ρ)e^{(ρ−½)t} = Φ_N(0)e^{t/2}+Φ_N(1)e^{−t/2}`, and apply
Lemma 11.9 with `c_ρ := Φ_N(1−ρ)`: all `c_ρ = 0` and `Φ_N(0) = Φ_N(1) = 0`.
The ideal property is `Φ_{N⋆g} = Φ_NΦ_g` and holomorphy of `Φ_g` on `S_ε`.
`ΠK` and `τ_a(ΠK)` have `Φ = e^{(s−½)a}s(1−s)ξ(s)`, which vanishes at `0`, `1`
and every zero, and lie in `D^W` by Theorem 11.7(ii) and Lemma 11.2(i).  ∎
`PROVED`

**`REFUTED` (blueprint D.7(i): `𝓝_∞ = ΠK ⋆ D^W`).**  The inclusion
`ΠK ⋆ D^W ⊆ 𝓝_∞` holds and is part of Theorem 11.11.  **The reverse inclusion
is false**, and a counterexample is one line long.

> **Proposition 11.11a (`PROVED`).**  For every `a ≠ 0`,
> `τ_a(ΠK) ∈ 𝓝_∞ ∖ (ΠK ⋆ D^W)`.
>
> *Proof.*  Membership in `𝓝_∞` is Theorem 11.11.  If `τ_a(ΠK) = ΠK⋆g` with
> `g ∈ D^W`, then on the line `\mathrm{Re}\,s = \tfrac32` — where `ξ(s) ≠ 0`
> (E2: `ζ` has no zeros with `\mathrm{Re}\,s ≥ 1`) and `s(1−s) ≠ 0` — we may
> divide and obtain `Φ_g(\tfrac32+iτ) = e^{(1+iτ)a} = e^{a}e^{iτa}`, of
> constant modulus `e^a ≠ 0`.  But `Φ_g(\tfrac32+iτ) = ∫(g(t)e^{t})e^{iτt}dt`
> with `g(t)e^t ∈ L¹(R)` by (11.1), so `Φ_g(\tfrac32+iτ) → 0` as `|τ| → ∞` by
> Riemann–Lebesgue.  Contradiction.  ∎  `PROVED`

The gap is not an accident of this example.  `Φ_{ΠK⋆g} = s(1−s)ξ(s)Φ_g(s)`
and `|ξ(½+iτ)| = e^{−π|τ|/4+O(\log|τ|)}` decays **exponentially** on the
critical line ((E3a) and Stirling (E4)), whereas `Φ_N(½+iτ) = \hat N(τ)` for
`N ∈ D^W` is only required to be `O(τ^{−2})`.  So a general `N ∈ 𝓝_∞` has
`Φ_N/ξ` growing like `e^{π|τ|/4}` on the critical line, and that is not the
transform of any `L¹` function.  **`ΠK ⋆ D^W` is a proper — indeed very
small — subideal of `𝓝_∞`, and the correct description of the radical is
(11.14).**  The blueprint's statement "`𝓝_∞ = ΠK ⋆ D^W` (to be proved, both
inclusions)" is refuted in the direction it asked for.  Nothing later depends
on it: §12 uses only that `𝓝_∞` is the radical, which (11.14) establishes.

**Theorem 11.12 (D.7(ii): the compactly supported radical vanishes, by zero
counting; `PROVED`).**  `𝓝_∞ ∩ C_c^∞(R) = 0`.  More precisely,
`(P^W)^{⊥_{I_∞}} ∩ C_c^∞(R) = 0`: **no nonzero compactly supported radial
class is orthogonal to the primitive sector.**  Consequently
`\mathrm{rad}\big(I_∞|_{D_A^{rad}}\big) = 0` on the colimit form.

*Proof.*  Let `N ∈ C_c^∞(R)`, `N ≢ 0`, with `Φ_N(ρ) = 0` at every zero of `ξ`
(Theorem 11.10(c)).  By Paley–Wiener (import (E6)), `Φ_N` is **entire of
exponential type** `≤ T := \max\{|t| : t ∈ \mathrm{supp}\,N\}` and `Φ_N ≢ 0`.
Let `n_N(r)` count its zeros in `|s−½| ≤ r`.  By Jensen's formula applied on
`|s−½| ≤ 2r`, for an entire function of exponential type `T` with
`Φ_N(s_0) ≠ 0` at some fixed `s_0`,

    n_N(r) ≤ \frac{1}{\log 2}\log\frac{\max_{|s−s_0|=2r}|Φ_N(s)|}{|Φ_N(s_0)|}
          = O(r)  \qquad (r → ∞)                                        (11.15)

— **`CLASSICAL`**, import **(X13)**.  Note that `n_N(r)` counts the zeros of
`Φ_N` **with multiplicity**, so it is an upper bound for the number of
**distinct** zeros in the disc.

**[REPAIRED, phase 135 round 2, finding M3 of `R135_002`.  Round 1 compared
`n_N(r)` with `2N(r)+O(1) = \frac rπ\log r(1+o(1))`, the Riemann–von Mangoldt
count of the zeros of `ξ` **with multiplicity** (import (X14)).  That
comparison is invalid: Theorem 11.10(c) gives `Φ_N(ρ) = 0` at each **distinct**
zero, to order one only, and the paper insists on exactly that distinction
eleven lines above, at (11.13).  A multiple zero of `ξ` of multiplicity `m_ρ`
forces one zero of `Φ_N`, not `m_ρ` of them, and the classical bound
`m_ρ = O(\log γ)` leaves the distinct count only `≫ r`, the same order as
Jensen's `O(r)`.  The repair is a sharper import, below.]**

On the other hand, let `N_{\mathrm{dist}}(r)` be the number of **distinct**
zeros of `ξ` in `|s−½| ≤ r`.  A **simple** zero is in particular distinct from
every other zero, and by Conrey's theorem — at least `\tfrac25` of the zeros
of `ζ` are simple (J. B. Conrey, *More than two fifths of the zeros of the
Riemann zeta-function are on the critical line*, J. reine angew. Math. **399**
(1989), 1–26; the weaker Levinson (1974) proportion `\tfrac13` would also do);
import **(X18)** — the number of simple zeros with `0 < γ ≤ T` is at least
`(\tfrac25+o(1))N(T)`.  With (X14) and `γ ≤ r` on the disc,

    N_{\mathrm{dist}}(r) ≥ \tfrac25·2N(r)(1+o(1))
                          = \tfrac{2}{5π}\,r\log r\,(1+o(1)) ,

and every distinct zero of `ξ` in the disc is a zero of `Φ_N`, so
`N_{\mathrm{dist}}(r) ≤ n_N(r)`.  Hence
`\tfrac{2}{5π}r\log r(1+o(1)) ≤ n_N(r) = O(r)`, which is false for large `r`.
So `N ≡ 0`.  The constant `\tfrac2{5π}` is immaterial: any positive proportion
of simple zeros, or indeed any lower bound `≫ r\log r` (or merely
`r\log^{δ}r`, `δ > 0`) for the distinct count, closes the argument.  The last sentence is the case
`N ∈ 𝓝_∞ ∩ C_c^∞ ⊆ (P^W)^⊥ ∩ C_c^∞`, together with Theorem 11.11's last
clause (pairing against compactly supported tests suffices).  ∎  `PROVED`

**`REFUTED` (blueprint D.7(ii): "a new proof of Paper 45 Theorem 12.2").**
Theorem 11.12 is **not** a second proof of Paper 45 Theorem 12.2, and saying so
would misdescribe both.

 * Theorem 12.2 is a statement about `I_A` at a **fixed finite chart `S`**,
   proved by Plancherel against the chart symbol `\hat T_S(𝔠_0,·)`, whose
   non-vanishing off a discrete set is Paper 43 Theorem 9.7(c).  Paper 45
   **Remark 12.4** says explicitly: "Nothing is claimed about `𝓝_∩^∞` on
   `D_A^∞`… This paper asserts no colimit vanishing", and gives the reason —
   the colimit symbol is unbounded (Paper 44 Remark 8bis.4b(1)), so the
   Plancherel step does not transfer.
 * Theorem 11.12 is a statement about `I_∞`, the **colimit** form, proved by
   zero counting against `ξ`, and it uses no symbol at all.

So the correct relation is: **Theorem 11.12 supplies, by a different
mechanism, exactly the colimit statement Remark 12.4 declined to assert.**  It
is a new theorem, recorded as such, and a `[phase 135]` remark is added at
Paper 45 Remark 12.4 saying so — not a second proof of Theorem 12.2.

**Remark 11.12a (this is the reconciliation Paper 43 Theorem 14.1(d) needs).**
Theorem 14.1(d) states `(D_A^{prim})^{⊥I_A} = 0` **inside `D_A`**.  Theorem
11.12 is its colimit analogue for `I_∞` on the radial sector, and Theorem
11.8(iv) exhibits `K ≠ 0` in `(P^W)^{⊥}`.  There is no conflict: `K ∉ D_A^∞`
(Finding 11.0 — every element of the colimit is compactly supported), and the
perp becomes nonzero **exactly** in the passage to `D^W`.  *The Hodge-index
shape rows A–C lack at every chart is a phenomenon of the completion, and this
is the precise sense in which that is true.*  A `[phase 135]` remark is added
at Paper 43 Theorem 14.1.

### 11.5 Degree, effectivity, and the bounded-density bound

**Theorem 11.13 (D.7(iii); `PROVED`).**  For `E ∈ D^W`:
 (i) if `E ≥ 0` and `E ≢ 0` then `\deg E = ∫E(t)2\cosh(t/2)dt > 0`;
 (ii) if `E ∈ 𝓝_∞` (**principal**) then `\deg E = 0`;
 (iii) if `E` is primitive then `\deg E = 0`; hence **no nonzero primitive
     class and no nonzero principal class is effective**, and `\deg` is
     constant on `𝓝_∞`-cosets;
 (iv) `\deg` and `I_∞(\cdot,X)` descend to `D^W/𝓝_∞` for every `X ∈ D^W`.

*Proof.*  (i) the integrand is `≥ 0` and continuous, positive somewhere.
(ii),(iii) are (11.14) and Definition 11.6.  (iv) `\deg = I_∞(\cdot,2K)`
(Theorem 11.8(v)) and `𝓝_∞` is the radical.  ∎  `PROVED`

**Remark 11.13a.**  (iii) is the statement Theorem 6.1 proves on `D_A^{tr}`
(Paper 43 Theorem 10.3c(a)), here on `D^W` and in the form Weil's argument
actually needs: not "primitive classes are effective" — they are not — but
"effective classes have positive degree and principal classes have degree
zero".  Remark 6.2 anticipated exactly this distinction.

**Theorem 11.14 (D.7(iv): the bounded-density bound and the openness of the
ample cone; `PROVED`, unconditionally).**  Let `F ∈ D^W` be real.  Put

    w_F(u) := Φ_F(1)e^{−u/2} + Φ_F(0)e^{u/2} − Σ_ρ e^{(ρ−½)u}Φ_F(1−ρ) ,   (11.16)

a continuous real function of `u`, the zero sum converging absolutely and
locally uniformly.  Then:

 (i) for every `E ∈ D^W`, `I_∞(E,F) = ∫_R E(u)\,w_F(u)\,du`, the integral
     absolutely convergent;
 (ii) `C_F := \sup_{u∈R}\dfrac{|w_F(u)|}{2\cosh(u/2)} < ∞`, with the explicit
      bound

          C_F ≤ |Φ_F(0)| + |Φ_F(1)| + Σ_ρ|Φ_F(1−ρ)| \; < \; ∞ ,          (11.17)

      every term of which is finite by (11.2) and (E3d); hence
      `|I_∞(E,F)| ≤ C_F\,\deg E` for every effective `E`;
 (iii) *(openness of the ample cone)*  call `H ∈ D^W` **ample** if
     `I_∞(E,H) > 0` for every effective `E ≢ 0`.  Then `2K` is ample, and for
     every `m > C_F` the class `H' := F + 2mK` is ample.

*Proof.*  (i) By Theorem 11.5,
`I_∞(E,F) = Φ_E(0)Φ_F(1) + Φ_E(1)Φ_F(0) − Σ_ρΦ_E(ρ)Φ_F(1−ρ)`.  Write
`Φ_E(0) = ∫E(u)e^{−u/2}du`, `Φ_E(1) = ∫E(u)e^{u/2}du` and
`Φ_E(ρ) = ∫E(u)e^{(ρ−½)u}du` (Lemma 11.2(iii)), and interchange the sum over
`ρ` with the integral.  The interchange is legitimate by absolute convergence:
`|e^{(ρ−½)u}| ≤ e^{|u|/2}` because `0 < \mathrm{Re}\,ρ < 1` (E2), and

    Σ_ρ|Φ_F(1−ρ)|∫|E(u)|e^{|u|/2}du < ∞ ,

since `∫|E|e^{|u|/2} < ∞` by (11.1) and `Σ_ρ|Φ_F(1−ρ)| ≤ C_2(F)Σ_ρ|γ_ρ|^{−2}
< ∞` by (11.2) and (E3d).  This is exactly `∫E\,w_F`.
(ii) `e^{\pm u/2} ≤ 2\cosh(u/2)` and `|e^{(ρ−½)u}| ≤ e^{|u|/2} ≤ 2\cosh(u/2)`,
again by `0 < \mathrm{Re}\,ρ < 1` and nothing else; divide (11.16) by
`2\cosh(u/2)` and take absolute values to get (11.17).  Each of the three
quotients is bounded by `1` and by nothing smaller:
`\sup_u e^{\pm u/2}/2\cosh(u/2) = 1` and `\sup_u e^{|u|/2}/2\cosh(u/2) = 1`,
the suprema approached as `u → \mp∞` and `|u| → ∞`, so the coefficients in
(11.17) are `1`, not `½`.  **[CORRECTED, phase 135 round 3, finding N1 of
`R135_005`: round 2 displayed `\tfrac12(|Φ_F(0)|+|Φ_F(1)|)+\tfrac12Σ_ρ|Φ_F(1−ρ)|`,
which its own proof does not give and which is false by a factor `2`.  Only
the finiteness of `C_F` is used downstream (Theorem 12.3 Step 1 chooses any
`m > C_F`), so no other statement changes.]**  Then for `E ≥ 0`,

    |I_∞(E,F)| ≤ ∫E(u)|w_F(u)|du ≤ C_F∫E(u)\,2\cosh(u/2)\,du = C_F\deg E .

(iii) `I_∞(E,2K) = \deg E > 0` for effective `E ≢ 0` by Theorems 11.8(v) and
11.13(i); and `I_∞(E,F+2mK) = I_∞(E,F) + m\deg E ≥ (m−C_F)\deg E > 0`.  ∎
`PROVED`

**[REPAIRED, phase 135 round 2, finding M9 of `R135_002` and §0.4 of
`R135_003`.  Round 1 proved (i) and (ii) on the **arithmetic** side: it wrote
`I_∞(E,F) = ∫E(u)R_F(u)du` with
`R_F(u) = Σ_nΛ(n)n^{−1/2}[F(u−\log n)+F(u+\log n)] +
\mathrm{f.p.}∫F(u−t)K_∞(|t|)dt`, bounded the prime part by Rosser–Schoenfeld
((X15)) and the archimedean part by the kernel `K_∞`.  **The archimedean half
was not licensed.**  The only explicit formula proved on `D^W` is (11.3),
which carries the archimedean term as
`\frac1{2π}∫\hat h(τ)[\mathrm{Re}\,ψ(¼+iτ/2)−\log π]dτ`; the identification of
that integral with `−\mathrm{f.p.}∫h(t)K_∞(|t|)dt` is imported from Paper 44
Theorem 3bis.7 and (8.5∞) **for `h ∈ C_c^∞`**, and `h = E⋆F^∨` with `E ∈ D^W`
is neither compactly supported nor supported away from `0`.  Rather than prove
that kernel representation on `D^W`, the theorem is now proved on the
**spectral** side, where (11.3) already lives.  The new proof is strictly
better in four ways: it is valid for every `F ∈ D^W` and not only for
`F ∈ C_c^∞(R)` of compact support; the constant (11.17) is intrinsic and does
not degrade like `e^{5T/2}` in the support radius; it imports neither (X15) nor
any finite-part convention; and it uses about the zeros only
`0 < \mathrm{Re}\,ρ < 1`, which is import (E2) and is Chebyshev-trivial — no
zero-free region, no PNT, no statement this paper proves.]**

**Remark 11.14a′ (the arithmetic-side bound, recorded and not used).**  For
`F ∈ C_c^∞(R)` with `\mathrm{supp}\,F ⊆ [−T,T]` the prime half of the round-1
computation is correct as it stands and is worth recording, because it bounds
the **finite** part of the density with no reference to the zeros at all:
`F(u−\log n) ≠ 0` forces `e^{u−T} ≤ n ≤ e^{u+T}`; for `u ≥ T`,
`n^{−1/2} ≤ e^{(T−u)/2}` there and
`Σ_{n≤x}Λ(n) = ψ_{Ch}(x) < 1.03883\,x` (Rosser–Schoenfeld, Illinois J. Math.
**6** (1962), Theorem 12; import **(X15)**), so the sum is
`≤ 1.03883\|F\|_∞e^{3T/2}e^{u/2}`; for `u < T` the range has `n ≤ e^{2T}` and
`n^{−1/2} ≤ 1`, so it is `≤ 1.03883\|F\|_∞e^{u+T} ≤
1.03883\|F\|_∞e^{5T/2}e^{−u/2}`.  With the mirror sum, the prime part of the
arithmetic density is `≤ 2·1.03883\|F\|_∞e^{5T/2}·2\cosh(u/2)`.  **Only
`ψ_{Ch}(x) = O(x)` is used.**  The archimedean half of that route is exactly
what finding M9 blocks, so **nothing below uses this remark**; it is kept
because it shows that the ample cone is open for a reason visible on the
arithmetic side too, and because it is the form in which the bound will be
needed if the kernel representation of `ω_∞` on `D^W` is ever proved.  That
representation — the equality of `\frac1{2π}∫\hat h[\mathrm{Re}\,ψ(¼+iτ/2)
−\log π]dτ` with `−\mathrm{f.p.}∫hK_∞(|t|)dt` for `h ∈ D^W`, which would
follow from the `C_c^∞` case of Paper 44 (8.5∞) together with an approximation
argument using the decay (11.1) — is recorded as **open item (21)** of §14.5
and is not asserted here.

**`REPAIRED` (blueprint D.7(iv) and §1, the ample class).**  The blueprint
writes `\deg F := I_∞(F,A)` with `A := e_+ + e_-` "the ruling class", and
"`F + mA` is ample".  **`A` is not an element of `D^W`**, or of any function
space here: by Paper 43 Theorem 9.14c and Paper 45 Remark 12.3 the rulings
`e_\mp` live in the *completion* `N_A^{dist}` as limits of spread Tate families
whose `L¹`-mass escapes, and they are exactly the **radical** of the boundary
form there.  The repair is that `2K` does the job intrinsically:
`I_∞(F,2K) = \deg F` for every `F ∈ D^W` (Theorem 11.8(v)), so `2K` **is** a
degree-computing ample class *inside* `D^W`, and the ample family is
`F + 2mK`.  The sentence "`K ≡ ½(e_++e_-)`" is then true as a statement about
the ruling data, `M(K) = ½(1,1)`, and **only** as such (§14.1); it is not an
identity of classes, because one side is not a class.

**Remark 11.14a (falsifier).**  Theorems 11.10–11.14 hold for `Ξ_a`,
with `\{0,1\}` replaced by the four poles `\{−a,a,1−a,1+a\}`, `\deg` replaced
by the positively weighted functional of §12.5, and `2\cosh(t/2)` by
`Σ_{p∈P}Ξ_a(p)e^{(p−½)t} ≍ e^{(½+a)|t|}`; in (11.17) the exponent `|u|/2` of
`|e^{(ρ−½)u}|` becomes `(½+a)|u|`, matching that weight, because the zeros of
`Ξ_a` satisfy `|\mathrm{Re}\,ρ − ½| ≤ ½+a` (Proposition 12.6).  **They carry no
sign.**

**[ADDITION OF RECORD P46-4, entered with Part III.  Theorem 11.14(iii) is
used in Theorem 12.3 only to make `F + 2mK` ample.  It proves more: the ample
cone is **absorbing at `K`**, which is exactly the hypothesis of the Lorentzian
criterion of §17 (Theorem 17.8), and therefore yields
`RH ⟺ I_∞(F,F) ≤ ½(\deg F)²` **on the ample cone** — the honest
Khovanskii–Teissier statement available here, replacing the effective cone,
for which the corresponding statement is refuted.  **Caveat of record:** the
ample cone is defined *through* `I_∞`, hence through the zero sum, so it is
not a zero-free cone, and the equivalence is a restatement of RH, not a route
to it.]**

---

## 12. D.8 — the affine duality `σ_K`, and the Hodge-index transfer theorem

### 12.1 `σ_K` satisfies (R5), and the duality was never the obstruction

**Definition 12.1.**  `σ_K : D^W → D^W`, `σ_K(E) := K − E`.

**Theorem 12.2 (`PROVED`).**  `σ_K` is an affine involution of `D^W`
(`σ_K² = \mathrm{id}`), it commutes with no algebra structure and is not
claimed to, and it **satisfies requirement (R5) of Definition 6.8**: for every
primitive `F`, `M(σ_KF) = M(K) − M(F) = (½,½) ≠ (0,0)`, so `σ_KF` is **not**
primitive.  Moreover `\deg σ_K(E) = 1 − \deg E`, and `σ_K` descends to
`D^W/𝓝_∞`.

*Proof.*  `M` is linear (Paper 43 Theorem 8A.7c(d)) and `M(K) = (½,½)`
(11.9).  `σ_K(σ_K E) = K−(K−E) = E`.  Descent: `𝓝_∞` is a linear subspace and
`σ_K` is affine with linear part `−\mathrm{id}`.  ∎  `PROVED`

**Theorem 12.2a (the diagnosis of (R5) is confirmed, and its cause is
corrected; `PROVED`).**  Definition 6.8(R5) was stated as a demand for a
**duality `F ↦ F^∨` compatible with `⋆` and `†`** carrying the primitive
sector off itself, and §6.3 records that `†` — the only such involution rows
A–C construct — preserves primitivity, so that the list is vacuous.  Both
halves of that are correct.  What was wrong is the **type** of the missing
object.  Weil's duality `D ↦ K − D` is not an algebra involution: it is a
**translation of the divisor group composed with negation**, i.e. an affine
involution of the additive group of classes.  Once the type is corrected, (R5)
is satisfied by `σ_K` for **any** class `K` with `M(K) ≠ 0`, and the content of
the requirement moves entirely into (R3): `K` must pair with every class
through the rulings alone, which by Theorem 11.10 means `Φ_K|_{Z(ξ)} = 0`, of
which `Φ_K = ξ` is the minimal solution.  **So (R5) is not a missing
involution.  It is a missing class, and §11 constructs one.**  ∎  `PROVED`
(Theorems 11.8(iv), 11.10, 12.2)

### 12.2 The transfer theorem

**[RECORD NOTE, entered with Part III.  **The hypothesis of Theorem 12.3 is
unsatisfiable for `ξ`, for every `χ`**, given the verified-zero import (X19)
(the first zero `ρ_1 = ½+iγ_1` is simple and on the critical line).  This is
Theorem 19.25, proved in §19, and the reader is referred there; the mechanism
is that for every nonnegative `E'` and every real `θ`,
`|\mathrm{Re}(e^{iθ}Φ_{E'}(ρ_1))| ≤ ½s_1\deg E'` with
`s_1 = \sup_u|\sin(γ_1u)|/\cosh(u/2) = 0.99846… < 1` (Lemma 19.17), while
(b′) together with Theorem 11.13, (c) and the Serre symmetry `R(K−E) = R(E)`
(Theorem 19.2) force `h⁰(E) ≥ ½I_∞(E,E) − ¼\deg E + χ` for `\deg E > 1`; the
certified class `E = 53.11911·e^{−u²/18}\sin(γ_1u) + 400K` has `R(E) = 10 > 0`,
`\deg E = 400` and `|\mathrm{Im}\,Φ_E(ρ_1)| = 199.7248 > 199.6920 = ½s_1·400`,
so `E` is equivalent modulo `𝓝_∞` to no nonnegative class.  **Theorem 12.3
keeps its label — its proof is correct — and loses its use:** it can no longer
serve as a route to RH in this normalization.  The same holds for every
admissible `Z` with a simple isolated on-line zero, `ξ_K` verbatim
(Theorem 19.28).  For the geometric diagnosis — the frame transports the
intersection theory of `C×C` and discards its linear systems — see
Restatement 19.29, and for the two repair routes (a defect in (c) vanishing at
the degrees Theorem 12.3 actually uses; an enlargement of the effective cone to
the classes with nonnegative Frobenius traces) see §19.9 and §20.]**

**Theorem 12.3 (Hodge-index transfer; `PROVED`, conditional on the existence
of `h⁰`).**  Hypotheses carried: the conventions of §11 (`c = 0`, colimit
trace, real radial tests, `D^W` of Definition 11.1); imports (E1)–(E6),
(E3d), (X12).  **[CORRECTED, phase 135 round 3, finding N8 of `R135_005`:
round 2 wrote "(X12)–(X15)".  (X13) and (X14) serve only Theorem 11.12, which
Theorem 12.3 does not use, and (X15) serves no proof at all (§15).]**  Suppose
there is a function `h⁰ : D^W → R_{≥0}` with

  **(a)** `h⁰(E) ≥ 0` for every `E ∈ D^W`;
  **(b′)** if `h⁰(E) > 0` then there is `E' ∈ D^W` with `E' ≥ 0`,
      **`E' ≢ 0`**, and `E − E' ∈ 𝓝_∞`;
  **(c)** there is a constant `χ ∈ R` with

          h⁰(E) + h⁰(K−E) ≥ ½\,I_∞(E,E) − ½\,I_∞(E,K) + χ
          \qquad\text{for every } E ∈ D^W .                             (12.1)

Then `I_∞(F,F) ≤ 0` for every primitive `F ∈ C_c^∞(R)`, and hence **RH**, by
Paper 45 Theorem 10.4.

*Proof.*  Fix a primitive real `F ∈ C_c^∞(R)`, `F ≢ 0`, and suppose
`q := I_∞(F,F) > 0`.  Since `F` is primitive, `\deg F = 0`, so by
Theorem 11.8, `I_∞(F,K) = ½\deg F = 0` and `I_∞(F,2K) = 0`.

*Step 1 (the ample class).*  Let `C_F` be the bounded-density constant (11.17)
of Theorem 11.14 and fix an integer `m > C_F`.  Put `H' := F + 2mK`.  By Theorem
11.14(iii), `H'` is ample: `I_∞(E,H') > 0` for every effective `E ≢ 0`.  Note

    I_∞(F,H') = q + 2m·I_∞(F,K) = q > 0 ,
    I_∞(K,H') = I_∞(K,F) + 2m·I_∞(K,K) = 0 + 2m·½ = m .                 (12.2)

*Step 2 (`h⁰` vanishes on `K − nF` for large `n`).*  Suppose
`h⁰(K−nF) > 0` for some `n`.  By (b′) there is `E' ≥ 0`, `E' ≢ 0`, with
`K−nF−E' ∈ 𝓝_∞`.  Since `𝓝_∞` is the **radical** (Theorem 11.11),
`I_∞(K−nF,H') = I_∞(E',H') > 0` by ampleness.  But by (12.2),

    I_∞(K−nF, H') = m − n\,q .

So `h⁰(K−nF) = 0` for every `n > m/q`.

*Step 3 (`h⁰` is positive on `nF` for large `n`).*  Apply (12.1) with
`E := nF`.  Using `I_∞(nF,nF) = n²q` and `I_∞(nF,K) = n·½\deg F = 0`,

    h⁰(nF) + h⁰(K−nF) ≥ ½n²q + χ .

For `n > m/q` the second term on the left is `0` by Step 2, so
`h⁰(nF) ≥ ½n²q + χ`, which is `> 0` as soon as `n > \max\{m/q,\
\sqrt{2\max(0,−χ)/q}+1\}`.  **No hypothesis `χ ≥ 0` is needed**, because the
quadratic term dominates; this is one place where (a),(b′),(c) is weaker than
(R1)–(R5), which needed `χ ≥ 0` for (6.2).

*Step 4 (the contradiction, by degree).*  Fix such an `n`.  By (b′) there is
`E' ≥ 0`, `E' ≢ 0`, with `nF − E' ∈ 𝓝_∞`.  By Theorem 11.13(ii),(iv) the
degree is constant on `𝓝_∞`-cosets, so `\deg E' = \deg(nF) = n\deg F = 0`.
By Theorem 11.13(i), `\deg E' > 0`.  Contradiction.

Hence `q ≤ 0`, i.e. `I_∞(F,F) ≤ 0` on every primitive `F ∈ C_c^∞(R)`.  By
(1.10) — Paper 45 Theorem 10.4, whose contrapositive is exactly this — RH
follows.  ∎  `PROVED`

**Remark 12.3a (the shape of the proof, and where each input is used).**  This
is Hartshorne V.1.9 with `H = 2K`, `H' = F + 2mH/2`, `E = nF` and `E = K−nF`,
and every step is a theorem of §11:

| Hartshorne V.1.9 | here | proved at |
|---|---|---|
| `H` ample, `D·H = 0` | `2K` ample; `I_∞(F,2K) = \deg F = 0` | Thm 11.14(iii), Thm 11.8(v) |
| `H' = D+mH` ample for `m ≫ 0` | `F+2mK` ample for `m > C_F` | Thm 11.14(ii),(iii) |
| `h⁰(K−nD) = 0` for `n ≫ 0` | Step 2 | Thm 11.11 (radical), Thm 11.14(iii) |
| RR forces `h⁰(nD) > 0` | Step 3 | (c) |
| effective of degree `0` is `0` | Step 4 | Thm 11.13(i),(ii) |

The two facts Weil's argument needs from "effective" are exactly Theorem
11.13(i),(ii), and Remark 6.2 said in advance that these, not the effectivity
of the primitive class, are what is needed.  **The theorem transfers the whole
sign problem onto the single object `h⁰`.  It asserts no sign, and it produces
no `h⁰`.**

**Remark 12.3b (why (b′) must say `E' ≢ 0`, checked as the blueprint asks).**
Without `E' ≢ 0`, Step 2 fails (`I_∞(0,H') = 0`, not `> 0`) and Step 4 fails
(`\deg 0 = 0` is consistent).  Both uses are essential and neither is
removable.  Conversely, `E ≡ E' \pmod{𝓝_∞}` **does** preserve `\deg` and
`I_∞(\cdot,X)`: that is Theorem 11.13(iv), which rests on `𝓝_∞` being the
radical, Theorem 11.11.  The blueprint asked for this to be proved; it is.

### 12.3 The falsifier theorem: for `Ξ_a`, (a)+(b′)+(c) are inconsistent

**[NEW, phase 135 round 2, findings M5, M6 of `R135_002` and LF2 of
`R135_003`.  Round 1 asserted the `Ξ_a`-analogue of Paper 45 Theorem 10.4 in a
parenthesis inside a `PROVED` theorem, and the parenthesis mis-stated the
inputs: it omitted (E2)'s last clause (which Paper 45 declares to be the only
place that import is used) and it omitted that `Ξ_a`-primitivity is **four**
conditions, so that Paper 45 Corollary 10.2, Lemma 10.3a and this paper's
Lemma 3.1 must all be redone with a fourth-order operator.  That step is the
load-bearing step of the falsifier theorem.  It is written out here, in full,
as two labelled statements.]**

**Lemma 12.4A (the rank-4 `Π_P`, and the analogue of Lemma 3.1 and of Paper 45
Corollary 10.2 / Lemma 10.3a; `PROVED`).**  Fix `0 < a < ½`, put
`P := \{−a,\,a,\,1−a,\,1+a\}`, `c_1 := ½+a`, `c_2 := ½−a` (so `0 < c_2 < c_1`),
and define the constant-coefficient differential operator of order `4`

    Π_P := \prod_{p∈P}\big(−∂_t + ½ − p\big) = (∂_t²−c_1²)(∂_t²−c_2²) ,

whose symbol is `Φ_{Π_Pg}(s) = π_P(s)Φ_g(s)`, `π_P(s) := \prod_{p∈P}(s−p)`.
Write `P_T^{(P)} := \{F ∈ C_c^∞(I_T) : Φ_F(p) = 0 \ ∀p ∈ P\}` for the
`Ξ_a`-primitive compactly supported class.  Then:

 (i) `Π_P` is real, of even order, with even symbol in `∂_t`, so it preserves
     support, reality and the even/odd parity split;
 (ii) `\ker Π_P` in `D'(R)` is `\mathrm{span}\{e^{(p−½)t}\}_{p∈P}`, of
      dimension `4`;
 (iii) `Π_P : C_c^∞(I_T) → P_T^{(P)}` is a **linear bijection**, with inverse
      `F ↦ G_{c_1}∗G_{c_2}∗F`, `G_c(t) := \tfrac1{2c}e^{−c|t|}`, and
      `\mathrm{conv\,supp}(Π_P^{−1}F) = \mathrm{conv\,supp}\,F`;
 (iv) `π_P(1−s) = π_P(s)` (because `P = 1−P` and `\#P` is even), so for
      `F = Π_PG`, `Φ_F(ρ)Φ_F(1−ρ) = π_P(ρ)²\,Φ_G(ρ)Φ_G(1−ρ)`;
 (v) `Ξ_a(σ) > 0` for every real `σ`; consequently **no `p ∈ P` is a zero of
     `Ξ_a`**, `π_P(ρ) ≠ 0` at every zero `ρ` of `Ξ_a`, and no zero of `Ξ_a` is
     real.

*Proof.*  (i) `Φ_{g'}(s) = −(s−½)Φ_g(s)` by parts, so multiplication of the
symbol by `(s−p) = (s−½)+(½−p)` is the operator `−∂_t+½−p`; pairing `p = −a`
with `p = 1+a` gives `(−∂+c_1)(−∂−c_1) = ∂²−c_1²`, and `p = a` with `p = 1−a`
gives `∂²−c_2²`.  Both factors are real, of order `2`, and even in `∂_t`.
(ii) each factor `(−∂_t+½−p)` kills `e^{(p−½)t}`, and the four exponents
`p−½ ∈ \{−c_1,−c_2,c_2,c_1\}` are distinct (`a ≠ 0`), so the four solutions are
independent and span the solution space of an elliptic constant-coefficient
operator of order `4` (hypoellipticity, as in Theorem 11.10).
(iii) `Π_PG ∈ P_T^{(P)}` because `π_P(p) = 0`; injectivity because
`Φ_{Π_PG} ≡ 0` forces `Φ_G ≡ 0` off `P`, hence everywhere (`Φ_G` entire by
Paley–Wiener), hence `G = 0`.  Surjectivity: `G_c` is the Green kernel of
`(−∂²+c²)` on `R` (the jump of the first derivative of `e^{−c|t|}` at `0` is
`−2c`), and `G_c ∈ L¹(R)` because `c > 0`, which is where `a < ½` is used.  Let
`F ∈ P_T^{(P)}` and put `F_2 := G_{c_2}∗F ∈ C^∞`.  For `t` to the right of
`\mathrm{supp}\,F`,
`F_2(t) = \tfrac1{2c_2}e^{−c_2t}∫e^{c_2s}F(s)ds = \tfrac1{2c_2}e^{−c_2t}Φ_F(1−a) = 0`,
and to the left `F_2(t) = \tfrac1{2c_2}e^{c_2t}Φ_F(a) = 0`; so
`F_2 ∈ C_c^∞` with the same support hull.  Its transform is entire and equals
`Φ_{F_2}(s) = Φ_F(s)/\big(c_2²−(s−½)²\big)` — an identity of meromorphic
functions, proved on the strip `|\mathrm{Re}\,s−½| < c_2` where
`Φ_{G_{c_2}}(s) = (c_2²−(s−½)²)^{−1}` converges absolutely, and extended by
analytic continuation.  At `s = 1+a` and `s = −a` the denominator is
`c_2²−c_1² = −2a ≠ 0` while `Φ_F` vanishes, so
`Φ_{F_2}(1+a) = Φ_{F_2}(−a) = 0`; repeating the argument with `c_1` makes
`u := G_{c_1}∗F_2` compactly supported in the same hull, and `Π_Pu = F` by the
symbol identity.
(iv) `π_P(1−s) = \prod_{p∈P}(1−s−p) = \prod_{p'∈P}(p'−s) = (−1)^4π_P(s)`,
substituting `p = 1−p'` and using `P = 1−P`.
(v) `Ξ_a = Φ_{K_a}` with `K_a > 0` (Remark 11.8a), so for real `σ`,
`Ξ_a(σ) = ∫K_a(t)e^{(σ−½)t}dt > 0`; `P ⊂ R`, so no `p ∈ P` is a zero, and no
zero of `Ξ_a` is real.  **This replaces, for `Ξ_a`, the use of (E2)'s last
clause that Paper 45 Theorem 10.4 needs for `ξ`: positivity of the Pólya kernel
is elementary (Theorem 11.7(i), as repaired) and does the same work.**
∎  `PROVED`

**Proposition 12.4B (the `Ξ_a`-analogue of Paper 45 Theorem 10.4; `PROVED`).**
Fix `0 < a < ½` and suppose `Ξ_a` has a zero `ρ_0` with
`\mathrm{Re}\,ρ_0 ≠ ½`.  Then there are nonzero compactly supported real
`Ξ_a`-primitive tests `F_+` (even) and `F_-` (odd) with

    Σ_{ρ ∈ Z(Ξ_a)} Φ_{F_±}(ρ)\,Φ_{F_±}(1−ρ) < 0 ,

the sum over the zeros of `Ξ_a` with multiplicity.  Equivalently, by (11.6)
read for `Ξ_a` (on a primitive test the polar packet vanishes),
`I_∞^{(a)}(F_±,F_±) > 0`.  Consequently: **if** `I_∞^{(a)}(F,F) ≤ 0` for every
compactly supported `Ξ_a`-primitive real `F`, **then** every zero of `Ξ_a` lies
on `\mathrm{Re}\,s = ½`.

*Proof.*  We run the proof of Paper 45 Theorem 10.4 with `Π` replaced by
`Π_P`, checking each of its inputs for `Ξ_a`.

*The quartet.*  `Ξ_a` is entire of order `1`, `Ξ_a(s) = Ξ_a(1−s)`, and
`Ξ_a(\bar s) = \overline{Ξ_a(s)}` because `Ξ_a` is real on `R`; so with
`ρ_0 = β_0+iγ_0`, `β_0 ≠ ½`, the four points `ρ_0, 1−ρ_0, \barρ_0, 1−\barρ_0`
are zeros of `Ξ_a`, and they are four distinct points because `β_0 ≠ ½` and
`γ_0 ≠ 0` (Lemma 12.4A(v)).

*The interpolation, `106_11` (20)–(21).*  In `106_11`'s variable
`z = (ρ−½)/i`, the quartet representative is `s_0 = x_0+iy_0` with `x_0 = γ_0`
and `y_0 = ½−β_0`.  Its (20)–(21) require `x_0y_0 ≠ 0`, i.e. `s_0² ∉ R`, which
makes `(α,β) \mapsto Z_R(s_0)Φ(s_0)^N(α+βs_0²)` an `R`-linear isomorphism
`R² → C` and lets **real** coefficients realize any complex target.  Here
`y_0 ≠ 0` is the hypothesis `\mathrm{Re}\,ρ_0 ≠ ½`, and `x_0 = γ_0 ≠ 0` because
`Ξ_a` has no real zero (Lemma 12.4A(v)) — **the check Paper 45 makes with
(E2)'s last clause is made here with the positivity of `K_a`, and it is the
check round 1 omitted.**  The odd family `z ↦ izZ_R(z)(γ+δz²)Φ(z)^N` is
handled identically.

*Primitivity and the transfer of the target values.*  By Lemma 12.4A(iii),
`F = Π_PG` is `Ξ_a`-primitive, compactly supported in the same interval, of the
same parity, and `F ≠ 0` for `G ≠ 0`; by Lemma 12.4A(v),
`Φ_F(ρ) = π_P(ρ)Φ_G(ρ)` with `π_P(ρ) ≠ 0` at every zero, so prescribing
finitely many values of `Φ_F` at zeros is equivalent to prescribing them for
`Φ_G`, which is `106_11`'s own statement.

*The strip.*  **[ADDED, phase 135 round 3, finding N5 of `R135_005`.]**
`106_11`'s estimates (15), (16), (27) and (29) are all stated on the strip
`|\Im z| ≤ ½`, that being `\max_ρ|\mathrm{Re}\,ρ−½|` for `ξ`.  For `Ξ_a` the
quartet can reach `|y_0| = |½−β_0| = ½+a`, so those four estimates must be
re-read on the wider strip `|\Im z| ≤ ½+a`.  This is legitimate, and nothing
else in `106_11`'s proof is touched, for the following reason.  The only
property of the profile `Φ` that (15) and (16) use is membership in the
Paley–Wiener class: here `Φ = \hatφ` with `φ ∈ C_c^∞(R)`, whose Fourier
transform is entire of exponential type and satisfies
`\sup_{|\Im z| ≤ h}(1+|\Re z|)^M|Φ(z)| < ∞` for **every** `M` and **every**
`h < ∞`, not merely for `h = ½`.  Hence (15) holds on `|\Im z| ≤ ½+a` with a
constant depending on `(M,a)` only; (16)'s choice of `R` is made from that
same uniform decay, now taken on the wider strip; and (27), (29) are integral
and supremum estimates over the strip, so they hold verbatim with `½` replaced
by `½+a` and the constants `C_R` replaced by their wider-strip values.  What
changes is only the size of those constants, which enter no conclusion: the
argument needs, for each fixed `N`, finiteness of the constants and the
geometric factor `4^{−(N−N_0)}`, both of which survive.  The four vanishing
conditions of (20)–(21) are imposed at the quartet, which lies inside the
wider strip by construction.

*Paley–Wiener* (import **(E6)**).  `π_P` is a polynomial, and multiplication by
a polynomial does not change the exponential type, so `F` is supported in the
same interval as `G`.

*Counting* (import **(E3d)**).  The zero-counting function of `Ξ_a` is the sum
of two copies of `N(T)` shifted by `\pm a`, so `N_{Ξ_a}(T) = 2N(T)+O(1) =
O(T\log T)` and `Σ_ρ(1+|γ_ρ|)^{−2} < ∞`.

*Tail domination.*  By Lemma 12.4A(iv) the tail acquires the factor
`|π_P(ρ)|² = O\big((1+|\mathrm{Im}\,ρ|)^{8}\big)` — **degree `8`, not the
degree `4` of `|ρ(1−ρ)|²` in Paper 45**, because `π_P` has degree `4`.
`106_11`'s tail bound (27) reads
`|F_{N,±}(z)| ≤ C_R(1+|z|)^{D}\big(|Φ(z)|/|Φ(s_0)|\big)^{N}` on the strip, with
`D` a fixed integer chosen at least as large as the total degree of the
polynomial factors carried through (20)–(21) and (27), and (28)–(30) then sum
the tail against the global geometric factor `4^{−(N−N_0)}`.
**[RE-DERIVED, phase 135 round 3, finding N5 of `R135_005`: round 2 asserted
the bump `D ↦ D+4`; here is the count.]**  The polynomial factor enters (27)
once per interpolation condition, as the value of the multiplier at the
corresponding node.  In Paper 45 the multiplier is `Π`, of symbol `ρ(1−ρ)`,
degree `2`; the construction imposes **two** conditions (the pair
`ρ_0, 1−ρ_0`, the conjugates being automatic for real coefficients), so the
tail acquires `|ρ(1−ρ)|² = O\big((1+|z|)^{4}\big)` and `D ↦ D+2` suffices —
`+2` being the degree of one factor times the one extra power of `(1+|z|)²`
that the pair of conditions costs, in `106_11`'s bookkeeping, where each
condition contributes half of the total polynomial degree.  Here the
multiplier is `Π_P`, of symbol `π_P(s) = [(s−½)²−c_1²][(s−½)²−c_2²]`, degree
`4` in `s`, and the construction imposes **four** conditions, one at each
point of the quartet `ρ_0, 1−ρ_0, \barρ_0, 1−\barρ_0` (the quartet is four
*distinct* points here, where in Paper 45 the conjugate pair collapses).  The
tail therefore acquires `|π_P(ρ)|² = O\big((1+|z|)^{8}\big)`, twice the
exponent of Paper 45, and four conditions instead of two; in the same
bookkeeping the bump is `D ↦ D+4`.  With that `D`, (29) still converges,
because (15) — now on `|\Im z| ≤ ½+a`, as above — gives decay faster than any
polynomial in `|\Re z|` on the strip, so `(1+|z|)^{D+4}|Φ(z)|^{N}` is
integrable for every `D` and every `N ≥ 1`, and (28) is unchanged.  It is the
degree `D`, not the exponent `N`, that absorbs the factor.

Hence for `N` large the target quartet's contribution
`4\,\mathrm{Re}\big[Φ_F(ρ_0)Φ_F(1−ρ_0)\big]` — made negative by the choice of
target values, and weighted by the positive multiplicities — dominates the rest
of the sum, giving the two tests.  The last sentence is the contrapositive.
∎  `PROVED`, using imports (E3d), (E6), the repository construction `106_11`
Theorem 1, and Lemma 12.4A; **it uses neither (E2)'s last clause, nor Hardy's
theorem, nor any statement about where the zeros of `ζ` are.**

**Theorem 12.4 (`PROVED`).**  Fix `0 < a < ½` and let `Ξ_a(s) = ξ(s+a)ξ(s−a)`.
Let `I_∞^{(a)}`, `D^W`, `K_a`, `𝓝_∞^{(a)}`, `\deg_a` be the objects of §11 built
from `Ξ_a` in place of `ξ` (§12.5 lists the four substitutions).  Then **there
is no** `h⁰_a : D^W → R_{≥0}` satisfying (a), (b′) and (c) for those objects.

*Proof.*  By §12.5, Theorem 12.3 holds verbatim for `Ξ_a`; its conclusion would
be `I_∞^{(a)}(F,F) ≤ 0` for every `Ξ_a`-primitive `F ∈ C_c^∞`, hence, by the
**Proposition 12.4B**, that every zero of `Ξ_a` lies on
`\mathrm{Re}\,s = ½`.  But by Hardy's theorem — `ξ` has infinitely
many zeros on the critical line; G. H. Hardy, *Sur les zéros de la fonction
`ζ(s)` de Riemann*, C. R. Acad. Sci. Paris **158** (1914), 1012–1014; import
**(X16)** — `Ξ_a` has infinitely many zeros with real part `½ \pm a ≠ ½`.
Contradiction.  ∎  `PROVED`

**Restatement 12.4a (the Euler-product locus, `RESTATEMENT (schema)`).**
**[RECAST, phase 135 round 2, finding M1 of `R135_002`, upgraded and ruled on
in §4 of `R135_003`.  Round 1 stated this as a `PROVED` **corollary**: "let
`h⁰` be any candidate whose *definition* is a function of the data `(Z, its
polar set, D^W, ⋆, ∨, τ, {·≥0}, K_Z, 𝓝_∞^{(Z)})`, uniformly in `Z`; then `h⁰`
does not satisfy (a)+(b′)+(c) for `ζ`".  **That was a non-sequitur, twice
over.**  (1) Uniformity of a *definition* transfers a *proof*, not the *truth*
of a conclusion: a uniformly defined rule `Z ↦ h⁰_Z` may perfectly well satisfy
(a)+(b′)+(c) for `ξ` and fail them for `Ξ_a`, and Theorem 12.4 forbids only the
latter.  (2) `Z` was itself listed among the data, so the hypothesis class was
everything (read `Z`, then branch), and the statement read literally asserted
that **no** `h⁰` whatever satisfies (a)+(b′)+(c) for `ζ` — which would make
Theorem 12.3 a reduction with a hypothesis just proved unsatisfiable, in
contradiction with this paper's own deliverable and with §14.5's `OPEN`.  The
statement below is what is actually true; it is a **principle about admissible
proofs**, not a theorem about functions, and it is labelled accordingly.  `Z`
has been removed from the data list.]**

Call a candidate **model-uniform** if it is given by a rule `Z ↦ h⁰_Z` whose
definition reads only the data

    \big(\text{the polar set } P\text{ of }Z,\ D^W_Z,\ ⋆,\ {}^∨,\ τ_\bullet,
    \ \{\cdot ≥ 0\},\ K_Z,\ 𝓝_∞^{(Z)}\big)                             (12.3)

— **`Z` itself is not among them** — over the class of admissible `Z` of
Proposition 12.6.  Then:

> **if** properties (a), (b′) and (c) are **derived** for `h⁰_ξ` from a
> derivation that uses only (12.3) and properties of those data valid for
> every admissible `Z`, **then** the same derivation, read for `Z = Ξ_a`,
> yields (a), (b′) and (c) for `h⁰_{Ξ_a}`, contradicting Theorem 12.4.
> Hence **no such derivation exists.**

*Proof.*  Every datum in (12.3) exists for `Ξ_a` (Proposition 12.6), and a
derivation that mentions only those data and their model-uniform properties is
a derivation for every admissible `Z`; Theorem 12.4 says its conclusion is
false for `Ξ_a`.  ∎  `RESTATEMENT (schema)`

**Remark 12.4a′ (exactly what this does and does not exclude).**  It does
**not** exclude any function `h⁰`.  A model-uniform *definition* whose
(a)+(b′)+(c) are established by a proof that inspects `ξ` — its Euler product,
its unimodular local roots, Hardy's theorem, anything `Ξ_a` lacks — is
untouched by the schema, because the transfer step fails at the first
`ξ`-specific line.  What the schema rules out is a **model-free proof**: one
carried out inside the structure (12.3) alone.  Its force is entirely in
Theorem 12.4 and Proposition 12.6; its content is a constraint on the shape of
any future argument, not on the set of functions.

**Remark 12.4b (a heuristic reading, demoted; `HEURISTIC`).**
**[DEMOTED, phase 135 round 2, finding M1 of `R135_002`, ruling §4 of
`R135_003`.  Round 1 called the paragraph below "the main structural output of
Part II" and drew from it the conclusion "**the definition of `h⁰` must use a
datum that `Ξ_a` lacks**".  With Restatement 12.4a recast as a schema about
proofs, that conclusion is **not proved**: what is excluded is a model-free
*derivation*, not a model-uniform *definition*.  The paragraph is kept, without
its quantifier and without its title, as a heuristic reading of Theorem 12.4 —
and, in that weaker role, as the most useful thing Part II has to say about
where to look next.]**

Everything in §11 and §12 is *model-uniform*: the Weil class, the canonical
class, the radical, the degree, the bounded-density bound, the ample cone, the
affine duality and the transfer theorem all exist for `Ξ_a`.  By Theorem 12.4
the conjunction (a)+(b′)+(c) does **not**.  So a proof that some `h⁰` satisfies
(a)+(b′)+(c) for `ζ` cannot be carried out inside that structure alone: **at
some line it must read a datum of `ζ` that `Ξ_a` does not share**, and Paper 46
§7 names the natural candidate — a Frobenius family in row B's sense (Theorem
7.1: `Ξ_a`'s local roots are `p^{\pm a}`, not unimodular, so
`F_n ⋆ F_n^† = (n^a+n^{−a})Δ^{(n)} ≠ Δ^{(n)}` and there is no partial isometry),
equivalently a Tate block of rank two rather than four.  *Where* the Euler
product must enter is therefore **suggested**, not proved, to be `h⁰`; this is
a direction for construction, it is not a theorem about where the arithmetic
must be used, and it is not a sign.

**Remark 12.3c (an elementary predecessor of the falsifier theorem; entered
with Part III, correction of record P46-2; `PROVED` in §17, Theorem 17.21).**
The inconsistency of (a)+(b′)+(c) for `Ξ_a` is proved above through the rank-4
operator `Π_P` and Proposition 12.4B.  It has a two-line predecessor at a lower
level: **for `Ξ_a` the Hodge-index inequality already fails on the *effective*
class `τ_uK_a + τ_{−u}K_a`, for every `u ≠ 0`**, by strict Cauchy–Schwarz on
the four polar weights — with no `h⁰`, no primitivity, and no zero anywhere in
the argument.  The falsifier is therefore visible in the polar block alone, and
the invariant it turns on — equimodularity of the polar exponents `|p − ½|` —
is the datum that (S2)/(S3) of §12.5 silently use.  See §17 for the statement,
the proof, and the ceiling: `ζ_K` is equimodular too, so equimodularity is
necessary and cannot by itself yield the sign.

**Remark 12.4c (the `Ξ_a` weights as slice evaluations on `M(Z)`; a
dictionary remark; identity `PROVED`, reading `RESTATEMENT`).**
**[ADDED, phase 157: `R157_005` Lemma 6.1, as cleared by `R157_006` §§6.3, 12,
with that audit's repairs (B10).]**  Write `|·|_p^ε` (`0 < ε < ∞`) for the
points of the `p`-branch of the Berkovich spectrum `M(Z)`, so that
`|p^k|_p^ε = p^{−kε}`.  For `0 < a < ½`,
`−Ξ_a′/Ξ_a(s) = −ξ′/ξ(s+a) − ξ′/ξ(s−a)`, whose prime part is
`Σ_nΛ(n)(n^{a}+n^{−a})n^{−s}`; at `s = ½+iτ` the weight of `n = p^k` is

    Λ(p^k)\big(p^{−k(½−a)} + p^{−k(½+a)}\big)
      = \log p\,\big(|p^k|_p^{½−a} + |p^k|_p^{½+a}\big) ,

against `\log p\,|p^k|_p^{½}` for `ξ`; the archimedean factor
`Γ_R(s+a)Γ_R(s−a)` is the local factor at the shifted parameters.  So the
weights of `Ξ_a` are the evaluations at the two points `ε = ½ ∓ a` of the
**same** branches of `M(Z)` at whose point `ε = ½` the weights of `ξ` are
evaluated, and the pair `{½−a, ½+a}` is symmetric about `½`, so the functional
equation does not single out `ε = ½`.  *Proof:* logarithmic derivative of
`ξ(s±a)`; the evaluation reading is the tautological rewriting
`p^{−kε} = |p^k|_p^ε`.  ∎  The identity is `PROVED`; the sentence "the space
`M(Z)` (and `A^{1,an}_Z` over it, §28.3a) cannot distinguish `ξ` from `Ξ_a`"
is a dictionary sentence, `RESTATEMENT`.  "The same branches" does not mean
"the same measure": the `Ξ_a` comb weights are `∼ n^{a−½}Λ(n)` and grow
relative to those of `ξ`.

What the remark does, and does not, license.  It lets Restatement 12.4a be
read for energies built on `A^{1,an}_Z` (§28.3a): a construction whose
weights are produced by the geometry of `M(Z)` (Green-kernel levels for
`\log p`, a slice for the half-power) is defined for `Ξ_a` by moving the slice
from `{½}` to `{½−a,½+a}`.  Two repairs of record apply to that reading.
(1) If positivity of such an energy **and** its identity with the Weil form
were both **derived** model-uniformly, the derivation read for `Ξ_a` would give
`Σ_{ρ∈Z(Ξ_a)}Φ_F(ρ)Φ_F(1−ρ) ≥ 0` on every compactly supported real
`Ξ_a`-primitive test, and the contradiction is with **Proposition 12.4B
together with Hardy's theorem (X16)** — Theorem 12.4's *argument* — not with
Theorem 12.4 itself, which is a statement about `h⁰_a` in the intersection
frame.  (2) `Ξ_a`-primitivity is the **four** conditions `Φ_F(p) = 0`,
`p ∈ \{−a,a,1−a,1+a\}` (the class `P_T^{(P)}` of Lemma 12.4A, cut out by the
rank-4 `Π_P`), not the two conditions of `P_T`; the transferred positivity must
hold on a class containing `P_T^{(P)}`.  As Remark 12.4a′ requires, this
excludes **derivations**, not functions: an unconditional positivity of the
energy built for `Ξ_a` shows only that the identity with the Weil form fails
for `Ξ_a`, and a termwise-positive energy whose identity with the Weil form of
`ξ` is established by an argument that reads `ξ` beyond the space is **not**
excluded by it (it would be case (2) of Theorem 28.3 with the gap closed).
It asserts nothing about the zeros of `ζ`.

### 12.4 Supersession of Definition 6.8

**Proposition 12.5 (`RESTATEMENT`).**  Requirements (R1)–(R5) of Definition 6.8
are **superseded** by (a), (b′), (c) of Theorem 12.3, as follows.

| Definition 6.8 | status after §12 | where |
|---|---|---|
| (R1) functoriality, no positivity/kernel/spectral input | **kept as a rule, not as a clause**: `h⁰` is still forbidden the three inputs of P122 §1; but no compatibility with `⋆`, `†` or the restriction functors is needed — Theorem 12.3 uses `h⁰` only on the classes `nF` and `K−nF` | Thm 12.3, Steps 2–4 |
| (R2) `h(G) ≥ 0` | **(a)**, unchanged | Thm 12.3(a) |
| (R3) the RR **identity** `h(F)−h(F^∨) = ½I_∞+ℓ(M)+χ` | **weakened to the inequality (c)**, with `ℓ(M(E)) = −½I_∞(E,K) = −¼\deg E` now **proved linear in the ruling data** rather than postulated — this was (R3)'s real content, and it is what pins `K` | Thm 11.8(i), (12.1) |
| (R4) vanishing on the primitive sector | **deleted**: no vanishing is postulated.  `h⁰(K−nF) = 0` is **derived** in Step 2 from ampleness and (b′) | Thm 12.3, Step 2 |
| (R5) a duality carrying the primitive sector off itself | **satisfied**, by `σ_K(E) = K−E` | Thm 12.2 |
| the side condition `χ ≥ 0` of (6.2) | **not needed** | Thm 12.3, Step 3 |
| — | **new**: (b′), an *effectivity* clause with `E' ≢ 0`, replacing the exact identity | Rem 12.3b |

Consequently §9.1 item **3a** — "a duality on `Corr_A^{tr}` that carries the
primitive sector off itself is `NOT CONSTRUCTED`, and is a **prerequisite**" —
is **closed**: `σ_K` is such a duality, it is affine and not an algebra
involution (which is why §6.3 could not find it among `†`-like objects), and
the prerequisite it named is met.  §9.1 item **3** is **replaced** by the
single open item "a function `h⁰` with (a),(b′),(c)", for which Restatement
12.4a shows no **model-free** proof can exist.  **[phase 135 round 2: round 1
wrote "which Corollary 12.4a shows must use the Euler product"; withdrawn with
finding M1, and kept as the heuristic Remark 12.4b.]**  ∎  `RESTATEMENT`

**Remark 12.5a (and what is *not* superseded).**  Theorems 6.1 and 6.3–6.7
stand unchanged: they refute four named candidates and they are cited, not
weakened, by §13.  Remark 6.8a's last row — "(R5) is failed *before* the
candidate is chosen" — is now historical: it was a correct statement about
algebra involutions and a wrong statement about the problem.  Remark 6.9's
`h(g) = \|π(g)Ω\|²` remains the one candidate of the right kind and the wrong
type, and Theorem 12.3 does not help it.

### 12.5 The four substitutions that carry §§11–12 to `Ξ_a`

**Proposition 12.6 (`PROVED`, with the substitutions of the proof listed and
the three non-verbatim ones proved).**  Let `Z` be entire of order `1` with
`Z(s) = Z(1−s)`, real and **strictly positive on `R`**, with
`−Z'/Z(s) = A_P(s) + (\text{archimedean}) + Σ_n c_n n^{−s}` where
`A_P(s) = Σ_{p ∈ P}(s−p)^{−1}` for a finite set `P ⊂ R` of simple poles with
`P = 1−P`, and `c_n ≥ 0` with `Σ_{n≤x}c_n = O(x^{½+θ})`, where
`θ := \max_{p∈P}|p−½| ≥ ½`.  Assume further

    every zero ρ of Z satisfies |\mathrm{Re}\,ρ − ½| ≤ θ .               (12.4)

**[REPAIRED, phase 135 round 2, finding M4 of `R135_002` and LF1 of
`R135_003`.  Round 1 wrote "all zeros in `0 < \mathrm{Re}\,s < 1`".  **That
hypothesis excludes `Ξ_a`, the one function the proposition exists to cover**:
the zeros of `Ξ_a` are `ρ \pm a`, with real parts in `(−a,1+a)`.  The clause is
replaced by (12.4), which for `Ξ_a` reads `|\mathrm{Re}\,ρ−½| ≤ ½+a = θ` and
**is** satisfied, by (E2) applied to the two shifted copies of `ξ`.  Note that
(12.4) is a hypothesis on `Z`, verified for `ξ` and for `Ξ_a` from (E2); it is
imported data, not a claim.]**

Let `D^W_Z` be the class (11.1) with the decay exponent `1+ε` replaced by
`½+θ+ε`.  Then §§11–12 hold for `Z` on `D^W_Z` after the four substitutions

  (S1) `\{0,1\} \rightsquigarrow P`; primitivity is `Φ_F(p) = 0` for all
       `p ∈ P`, and `Π` is replaced by `Π_P` with symbol
       `π_P(s) = ∏_{p∈P}(s−p)`, whose kernel in `D'` is spanned by
       `\{e^{(p−½)t}\}_{p∈P}` and is **disjoint from the exponents
       `\{ρ−½\}`** — the latter because `Z(p) > 0` for `p ∈ P ⊂ R`, so no
       pole is a zero;
  (S2) `2\cosh(t/2) \rightsquigarrow \sum_{p∈P}Z(p)\,e^{(p−½)t} > 0`, and
       `\deg_Z F := Σ_{p∈P}Z(p)Φ_F(p) = I_∞^{(Z)}(F,K_Z)`, still **strictly
       positive on nonzero effective classes** because `Z > 0` on `R`.
       **[CORRECTED, finding M13 of `R135_002`: for `Z = ξ` the right-hand side
       of (S2) is `½(e^{t/2}+e^{−t/2}) = \cosh(t/2)`, i.e. **half** of the
       weight `2\cosh(t/2)` of Definition 11.6, and correspondingly
       `\deg_ξ F = ½\deg F`.  §11 is therefore the case `Z = ξ` **up to that
       factor `2`**, which is exactly Theorem 11.8(v)'s statement that it is
       `2K`, not `K`, that computes `\deg`.]**
  (S3) the contour abscissa `c = \tfrac32` `\rightsquigarrow` any `c` with
       `½+θ < c < 1+θ+ε`, a nonempty range for every `θ`; there `Φ_g` is still
       holomorphic **and** `Σ_nc_nn^{−c} < ∞`.
       **[CORRECTED, finding M13 of `R135_002`: round 1 wrote
       `1 < c < 1+θ+ε`, which for `Ξ_a` does not guarantee convergence of the
       Dirichlet series — `Σ_{n≤x}c_n = O(x^{1+a})` needs `c > 1+a = ½+θ`.]**
       In Theorem 11.14 the weight `2\cosh(t/2)` of (11.17) is replaced by the
       weight of (S2), which grows like `e^{θ|t|}`, and `|e^{(ρ−½)u}| ≤
       e^{θ|u|}` by (12.4): the two exponents **agree**, which is the
       structural reason the bound closes for `ξ` as for `Ξ_a`;
  (S4) `K \rightsquigarrow K_Z` with `Φ_{K_Z} = Z`, so that
       `\deg_ZK_Z = Σ_pZ(p)²` and `K_Z/\!\deg_Z\!K_Z` is the degree-computing
       ample class.

For `Z = ξ`: `P = \{0,1\}`, `θ = ½`, decay exponent `1+ε` — Definition 11.1.
For `Z = Ξ_a`: `P = \{−a,a,1−a,1+a\}`, `θ = ½+a`, `c_n = Λ(n)(n^a+n^{−a})` with
`Σ_{n≤x}c_n = O(x^{1+a})`, decay exponent `1+a+ε`, and `K_{Ξ_a} = K_a` of
Remark 11.8a.  **All of §§11–12 is then available for `Ξ_a` on the
correspondingly smaller class `D^W_a`, which still contains `K_a`
(super-exponential decay) and every compactly supported test.**

*Proof.*  **[REWRITTEN, phase 135 round 2, finding M5 of `R135_002`.  Round 1
closed with "`PROVED` (each substitution is a line-by-line re-reading of the
proofs of §§11–12)".  A prose report of a prose re-reading is not evidence.
Below, the statements re-read are **listed**, and the three substitutions that
are **not** verbatim are proved.]**

*Verbatim under (S1)–(S4), with no step that mentions `θ` or `P` other than by
name:* Lemma 11.2 (with the decay exponent `½+θ+ε`, which makes `Φ_g`
holomorphic on `−θ−ε < \mathrm{Re}\,s < 1+θ+ε` and gives (11.2) there);
Definition 11.4, Lemma 11.4a, Theorem 11.5, Definition 11.6; Theorem 11.7(iii)
and Theorem 11.8 (whose proofs use only `Φ_{K_Z} = Z` and `Z(ρ) = 0`);
Theorem 11.10; Theorem 11.11; Theorem 11.13; §12.1 (Theorems 12.2,
12.2a, with `M` the `\#P`-tuple `(Φ_F(p))_{p∈P}`); §12.2 (Theorem 12.3 and
**[CORRECTION OF RECORD P46-1, entered with Part III (§17).  The tuple
printed here is transposed relative to the convention of Proposition 14.1 and
Theorem 11.8(iii), which set `M(F) = (Φ_F(1),Φ_F(0))`; for `P = \{0,1\}` in its
natural order the display above reads `(Φ_F(0),Φ_F(1))`.  `M(K) = (½,½)` hides
the discrepancy and `M(τ_aK)` does not.  **The convention of record is
`M(F) = (Φ_F(1),Φ_F(0))`**, and the display above is to be read in that order;
no statement of §§12.5 or 14 changes.]**
Remarks 12.3a, 12.3b, whose only quantitative inputs are Theorems 11.8, 11.11,
11.13 and 11.14).

**Not claimed for `Ξ_a`: Theorem 11.12.**  **[CORRECTED, phase 135 round 3,
finding N3 of `R135_005`: round 2 listed Theorem 11.12 as verbatim.  Its
repaired proof runs on import **(X18)**, Conrey's positive proportion of simple
zeros **of `ζ`**, and nothing in (12.4) or in the other hypotheses on `Z`
supplies a lower bound on the number of **distinct** zeros of `Z`.  Theorem
11.12 is therefore **not** asserted for a general admissible `Z`, and it is not
asserted here for `Ξ_a` either.  Nothing needs it: Theorem 12.4 goes through
Theorem 12.3, whose quantitative inputs are Theorems 11.8, 11.11, 11.13 and
11.14.]**

*Not verbatim.*  Three steps change, and here they are.

 **(a) The contour in Theorem 11.3.**  The proof runs a rectangle with right
 edge `L_c` and left edge `L_{1−c}`.  Two conditions must hold at once: `Φ_h`
 must be holomorphic on `L_c`, which by Lemma 11.2(iii) needs `c < 1+θ+ε`; and
 the Dirichlet series `Σ_nc_nn^{−s}` must converge absolutely on `L_c`, which
 by `Σ_{n≤x}c_n = O(x^{½+θ})` and partial summation needs `c > ½+θ`.  The
 interval `(½+θ,\,1+θ+ε)` is nonempty for every `θ > 0`; fix any `c` in it.
 The poles of `A_P` are the `\#P` points of `P`, all in
 `|\mathrm{Re}\,s−½| ≤ θ < c`, hence all interior to the rectangle, and each is
 simple with residue `Φ_h(p)` — this is where the polar packet
 `Σ_{p∈P}Φ_h(p)` of (11.4) comes from, in place of `Φ_h(0)+Φ_h(1)`.  The
 horizontal sides carry `O(X_j^{−2}\log^2X_j)` by (11.2) and the order-one
 growth of `Z'/Z`; the shift of the archimedean piece to `L_{1/2}` is unchanged.
 Absolute convergence of the zero sum is `|Φ_h(ρ)| = O(|γ_ρ|^{−2})` by (11.2)
 — which needs `|\mathrm{Re}\,ρ−½| ≤ θ` and the decay exponent `½+θ+ε`,
 i.e. (12.4) — together with `Σ_ρ|γ_ρ|^{−2} < ∞`, which for `Z = Ξ_a` is
 `2Σ_ρ^{(ξ)}|γ_ρ|^{−2} < ∞`.

 **(b) Lemma 11.9, the separation lemma.**  The statement becomes: if
 `Σ_ρc_ρe^{(ρ−½)t} = Σ_{p∈P}α_pe^{(p−½)t}` for all real `t`, with
 `Σ_ρ|c_ρ| < ∞`, then all `c_ρ = 0` and all `α_p = 0`.  Three points change.
 (1) *Convergence:* `|e^{(ρ−½)t}| ≤ e^{θ|t|}` by (12.4), so both sides are
 continuous.  (2) *The Laplace half-plane:* the transform
 `∫_0^∞e^{(ρ−½)t}e^{−zt}dt = (s−ρ)^{−1}` with `z = s−½` converges, uniformly
 in `ρ`, exactly for `\mathrm{Re}\,z > θ`, i.e. on
 `\mathrm{Re}\,s > ½+θ` — **not on `\mathrm{Re}\,s > 1`**, which is the
 abscissa round 1 inherited from `ξ`.  The identity
 `Σ_ρc_ρ/(s−ρ) = Σ_{p∈P}α_p/(s−p)` therefore holds on `\mathrm{Re}\,s > ½+θ`,
 which is a nonempty open set, and both sides continue analytically to
 `C ∖ (Z(Z) ∪ P)`.  (3) *Separation:* the argument needs `P ∩ Z(Z) = ∅`, so
 that the right-hand side is holomorphic at each zero.  This is the clause of
 (S1): `P ⊂ R` and `Z > 0` on `R`, so `Z(p) > 0` for every `p ∈ P`.  For
 `Z = Ξ_a` it says `ξ(2a) ≠ 0` and `ξ(1−2a) ≠ 0`, which round 1 cited nowhere
 and which is here **proved**, not imported, from `Ξ_a = Φ_{K_a}` with
 `K_a > 0`.  The rest — a function with a pole is not a function without one —
 is unchanged, and gives `m_ρc_ρ = 0` at every zero, then `α_p = 0` by the
 linear independence of the `\#P` simple poles at the distinct points of `P`.

 **(c) Theorem 11.14, the bounded-density bound.**  The proof of Theorem 11.14
 as repaired in §11.5 is on the spectral side, and the only inequality it uses
 about the zeros is `|e^{(ρ−½)u}| ≤ e^{θ|u|}`, which is (12.4).  The weight
 `2\cosh(u/2)` becomes `\sum_{p∈P}Z(p)e^{(p−½)u}`, which is `≍ e^{θ|u|}` and
 is **strictly positive** on `R` because every `Z(p) > 0`; so both
 `|e^{(p−½)u}|` and `|e^{(ρ−½)u}| ≤ e^{θ|u|}` are dominated by a fixed multiple
 of that weight, and (11.17) goes through with the constant
 `C_F^{(Z)} ≤ C\big(Σ_p|Φ_F(p)| + Σ_ρ|Φ_F(1−ρ)|\big)`.  *No Chebyshev bound is
 used at all* — which is why the substitution `1.03883x \rightsquigarrow
 O(x^{½+θ})` of round 1's (S3) is no longer needed for anything, and is
 retained above only for Remark 11.14a′, which nothing uses.

**Not covered by this proposition:** Paper 45 §10 and the sufficiency theorem.
Proposition 12.6 carries §§11–12 of *this* paper and nothing else; the
`Ξ_a`-analogue of Paper 45 Theorem 10.4 is Proposition 12.4B above, proved
there in full with its own rank-4 operator (Lemma 12.4A).  ∎  `PROVED`

---

## 13. D.9 — the candidate `h⁰`: what is provable, and what is refuted

### 13.1 The naive candidate

**Definition 13.1.**  For `E ∈ D^W` put
`H⁰(E) := \{g ∈ D^W : E + ΠK⋆g ≥ 0\}`, a **convex** subset of `D^W`
(the map `g ↦ ΠK⋆g` is linear and `\{\cdot ≥ 0\}` is a convex cone).

**Theorem 13.2 (structure of `H⁰`; `PROVED`).**
 (i) `H⁰(0) = \{0\}` — exactly, not merely modulo `\ker Π`.
 (ii) If `H⁰(E) ≠ ∅` then `E ≡ E' \pmod{𝓝_∞}` with `E' ≥ 0`; and `E' ≢ 0`
     unless `E ∈ ΠK⋆D^W`.
 (iii) If `\deg E < 0` then `H⁰(E) = ∅`.
 (iv) `H⁰(E)` is invariant under `E ↦ E + ΠK⋆g_0` up to translation of the
     parameter, so `H⁰` descends to the quotient by the ideal `ΠK⋆D^W`
— but **not** to `D^W/𝓝_∞`, by Proposition 11.11a.

*Proof.*  (i) If `ΠK⋆g ≥ 0`, then
`\deg(ΠK⋆g) = Φ(0)+Φ(1) = 0` because `Φ_{ΠK⋆g}(s) = s(1−s)ξ(s)Φ_g(s)` vanishes
at `s = 0,1`; but `\deg` of a nonnegative continuous function is
`∫(ΠK⋆g)(t)2\cosh(t/2)dt`, which is `0` only if `ΠK⋆g ≡ 0` (Theorem
11.13(i)).  Then `s(1−s)ξ(s)Φ_g(s) ≡ 0` on `S_ε`, so `Φ_g ≡ 0`, so `g = 0`.
(ii) `E' := E + ΠK⋆g ≥ 0` and `ΠK⋆g ∈ 𝓝_∞` (Theorem 11.11).  (iii) `\deg E' =
\deg E < 0` contradicts Theorem 11.13(i).  (iv) by linearity; the failure of
descent is Proposition 11.11a, `τ_a(ΠK) ∈ 𝓝_∞ ∖ ΠK⋆D^W`.  ∎  `PROVED`

**Restatement 13.3 (no *model-free* proof that a functional of `H⁰` alone
satisfies (c); `RESTATEMENT (schema)`).**  Let `Φ` be any rule assigning to a
convex subset of `D^W` a number in `R_{≥0}`, and put `h⁰(E) := Φ(H⁰(E))`.
Definition 13.1 mentions only `D^W`, `⋆`, `Π_PK_Z` and `\{\cdot ≥ 0\}`, all of
which belong to the data (12.3) and exist for every admissible `Z`
(Proposition 12.6).  Hence the rule `Z ↦ Φ(H⁰_Z(\cdot))` is **model-uniform**,
and Restatement 12.4a applies to it: **no derivation of (a)+(b′)+(c) for
`h⁰ = Φ(H⁰)` can be carried out inside (12.3) alone.**

*Proof.*  Restatement 12.4a, with the definition above as the model-uniform
rule.  ∎  `RESTATEMENT (schema)`

**[WITHDRAWN, phase 135 round 2, finding M1 of `R135_002`, ruling §4 of
`R135_003`.  Round 1 stated this as Theorem 13.3, `PROVED`: "Let `Φ` be any
rule … Then `h⁰` does not satisfy (a)+(b′)+(c)", proved by round 1's Corollary
12.4a.  **That quantified statement is withdrawn.**  It inherits the
non-sequitur of M1 verbatim: a model-uniform *definition* may satisfy
(a)+(b′)+(c) for `ξ` and fail them for `Ξ_a`.  Nothing in this paper rules out
the existence of a rule `Φ` with `Φ(H⁰_ξ)` satisfying the three properties, and
the question of whether some functional of `H⁰(E)` alone can satisfy (c) is
therefore reopened and recorded as **`OPEN`, §14.5 item (22)**.  What survives
is the schema above, and it is not nothing: it says that if such a `Φ` exists,
the proof that it works must read `ξ` somewhere.]**

**Remark 13.3a.**  The blueprint's D.9(i) demand was to "show why **no**
dimension function of this convex set alone can satisfy (c)".  Round 1 claimed
to have met it; round 2 does not.  What is met is the weaker and honest form:
*no model-free argument can establish (c) for such a functional.*  The
structure of Theorem 13.2 survives as structure — it is proved outright, and it
is the only part of §13.1 with a label stronger than `SCHEMA`.

### 13.2 The integral candidate, and its growth

Row B supplies two integral structures: the Frobenius family `Frob_n` with
`M(Frob_n) = (n^{1/2},n^{−1/2})` (Theorem 3ter.6(iii)), whose action on radial
classes is the modulus translation `τ_{\log n}` (Theorem 11.8(iii)); and the
integral shadow `Sh_Z(Frob_n) = [L_S \xrightarrow{n} L_S]` on the objects
(Paper 44 §6bis, Definition 6bis.1, Theorem 6bis.3), whose Möbius cofiber is
`[Z \xrightarrow{Φ_n(1)} Z]` and whose degree is `\log n`.  Connes–Consani's
integer dimension over the sphere — `\dim_{\mathbb S}\|H\mathbb Z\|_n =
\lceil \log(2n+1)/\log 3\rceil`, the minimal size of a generating subset of
`[-n,n]∩\mathbb Z` with coefficients in `\{-1,0,1\}` (arXiv:2205.01391v2,
Proposition "dimhzn" and Theorem "mainth"), with
`\dim_{\mathbb S}H⁰(D) = \lceil(\deg D+\log2)/\log3\rceil − \mathbf 1_L` — is a
`\log`-scale count of exactly this kind: `\dim_{\mathbb S}` is
`\log\#/\log 3 + O(1)`.  This fixes the **one** definition to test.

**Definition 13.4 (the integral candidate; one definition, not a menu).**
Let `Λ_W ⊂ 𝓝_∞` be the **arithmetic lattice of principal classes**

    Λ_W := \bigoplus_{q = p^k,\ p\ \text{prime},\ k ≥ 1}\;
           \mathbb Z\cdot w_q\,τ_{\log q}(ΠK) ,\qquad
           w_q := Λ(q)\,q^{−1/2} = (\log p)\,p^{−k/2} > 0 ,             (13.1)

the sum over **prime powers only** (finite `Z`-combinations; every generator
lies in `𝓝_∞` by Theorem 11.11 and Proposition 11.11a, and the weight `w_q` is
the exact finite contact of `Frob_q`, Paper 44 Theorem 3ter.10).  Put

    H⁰_{\mathbb Z}(E) := \{\,λ ∈ Λ_W : E + λ ≥ 0\,\},\qquad
    h⁰_{\mathbb Z}(E) := \log\#\,H⁰_{\mathbb Z}(E) ∈ [0,∞] ,            (13.2)

with the **convention** `\log\#∅ := 0`, i.e. `h⁰_{\mathbb Z}(E) := 0` when
`H⁰_{\mathbb Z}(E) = ∅`.  (`\#∅ = 0` and `\log 0 = −∞`; the value `0` is
stipulated, not computed — see the bracketed note below.)
Write `Λ_1` for the same construction with every weight `w_q` replaced by `1`,
the index set still the prime powers (the **naive** lattice).

**[REPAIRED, phase 135 round 2, finding M7 of `R135_002`.  Round 1 indexed
(13.1) by **all** `n ≥ 2`, with generator `Λ(n)n^{−1/2}τ_{\log n}(ΠK)`.  Since
`Λ(n) = 0` for every `n` that is not a prime power, infinitely many generators
were the **zero element**, and three statements of §13.2 were false as written:
Theorem 13.5(i) (its Dirichlet-uniqueness step recovers only `a_nΛ(n) = 0`,
vacuous off the prime powers), Theorem 13.5(ii) (`#H⁰_{\mathbb Z}(0) = ∞`,
since every tuple supported off the prime powers maps to `λ = 0 ≥ 0`, so
`h⁰_{\mathbb Z}(0) = ∞` and even (a) fails as a real-valued statement), and
Theorem 13.6's proof (which divides by `\min_nΛ(n)n^{−1/2} = 0`).  Indexing by
prime powers, as above, repairs all three with no other change; the naive
lattice `Λ_1` is re-indexed the same way, so that the two lattices differ only
in the weights, which is what §13.2 compares.  `r135_common.py` and
`h0_candidate.py` have been corrected to match.]**

**[CORRECTED, phase 135 round 2, finding M15 of `R135_002`: round 1 wrote that
the value `0` on `\{\deg < 0\}` is "forced".  It is not: `\log\#∅ = −∞`, and
`0` is a choice, made here because (a) requires a value in `R_{≥0}`.  It is
recorded as a convention, and it does not distinguish "no sections" from "only
the zero section".]**

**Theorem 13.5 (`PROVED`).**  (i) The generators of `Λ_W` (and of `Λ_1`) are
linearly independent over `R`, so `λ ↦ E+λ` is injective and
`\#H⁰_{\mathbb Z}` is well defined.
(ii) `H⁰_{\mathbb Z}(0) = \{0\}` and `h⁰_{\mathbb Z}(0) = 0`.
(iii) `h⁰_{\mathbb Z}(E) > 0 ⟹ \deg E > 0`, and then `E ≡ E' \pmod{𝓝_∞}`
with `E' ≥ 0` and `E' ≢ 0`; so **(b′) holds unconditionally** for
`h⁰_{\mathbb Z}` (and for `h⁰_{Λ_1}`).  Moreover
`\deg E < 0 ⟹ H⁰_{\mathbb Z}(E) = ∅`.
(iv) **(a) holds**, with the convention of Definition 13.4.

*Proof.*  (i) `Φ` of the generator at the prime power `q` is
`w_q\,q^{s−1/2}s(1−s)ξ(s)`; a vanishing finite real combination gives
`Σ_q a_qw_qq^{−1/2}·q^{s} ≡ 0` on the line `\mathrm{Re}\,s = \tfrac32`, where
`s(1−s)ξ(s) ≠ 0`, i.e. a vanishing Dirichlet polynomial in `q^{−s}`; **every
coefficient `a_qw_qq^{−1/2}` vanishes by uniqueness of Dirichlet coefficients,
and `w_q > 0` on the index set, so every `a_q = 0`.**  (It is exactly here that
the round-1 index set failed.)
(ii) If `λ ≥ 0` with `λ ∈ Λ_W ⊂ 𝓝_∞` then `\deg λ = 0` (Theorem 11.13(ii)),
so `λ ≡ 0` by Theorem 11.13(i), so the coefficient vector is `0` by (i).
(iii) Suppose `h⁰_{\mathbb Z}(E) > 0`, i.e. `\#H⁰_{\mathbb Z}(E) ≥ 2`: there
are `λ_1 ≠ λ_2 ∈ Λ_W` with `E+λ_i ≥ 0`.  Since `Λ_W ⊂ 𝓝_∞`, every `λ ∈ Λ_W`
has `\deg λ = 0` (Theorem 11.13(ii)), so `\deg(E+λ_i) = \deg E`.  If
`\deg E < 0` then no `E+λ ≥ 0` exists at all (a nonnegative class has
nonnegative degree), so `H⁰_{\mathbb Z}(E) = ∅`.  If `\deg E = 0` then each
`E+λ_i` is nonnegative of degree `0`, hence `E+λ_i ≡ 0` by Theorem 11.13(i),
hence `λ_1 = −E = λ_2`, contradicting `λ_1 ≠ λ_2`; so
`\#H⁰_{\mathbb Z}(E) ≤ 1` and `h⁰_{\mathbb Z}(E) = 0`.  Therefore
`h⁰_{\mathbb Z}(E) > 0` forces `\deg E > 0`, and then `E' := E+λ_1 ≥ 0`
satisfies `E − E' = −λ_1 ∈ 𝓝_∞` and `\deg E' = \deg E > 0`, so `E' ≢ 0`.
This is exactly (b′), with no restriction on `E`.  (iv) by definition.
∎  `PROVED`

**Remark 13.5c (`CORRECTED`, phase 135 round 3, finding N2 of `R135_005`).**
Round 2's text read: "(b′) is verified only on `\{\deg > 0\}`.  So
`h⁰_{\mathbb Z}` is **not** a candidate satisfying (a)+(b′)+(c) even before any
growth estimate … Theorem 13.6 below is therefore a second, independent
obstruction, not the only one."  **That is withdrawn**, on two counts: "not
verified" does not entail "fails", and the conclusion is in fact false.  By
Theorem 13.5(iii) as now proved, `h⁰_{\mathbb Z}(E) > 0` already forces
`\deg E > 0`, because degree `0` leaves at most one section and negative
degree none; so (b′) holds with no restriction.  `h⁰_{\mathbb Z}` is therefore
a genuine candidate satisfying **(a)** and **(b′)**, and the **only**
requirement it is known to fail is **(c)**, and that only on every finite
truncation (Theorem 13.6(ii)).  Theorem 13.6 is the sole obstruction on
record, not a second one.

**Lemma 13.5a (homogeneity, and boundedness on every finite truncation;
`PROVED`).**  Fix a finite set `Q` of prime powers, `d := \#Q`, and let
`Λ_W(Q) ≅ \mathbb Z^Q` be the corresponding sublattice of `Λ_W`.  Put

    C(Q) := \{\,x ∈ R^{Q} : K + Σ_{q∈Q}x_q\,w_q\,τ_{\log q}(ΠK) ≥ 0\,\} .

Then (i) `C(Q)` is closed, convex and contains `0`; (ii) for every `m > 0`,
`\{λ ∈ Λ_W(Q) : mK+λ ≥ 0\} = \mathbb Z^{Q} ∩ m\,C(Q)`; (iii) `C(Q)` is
**bounded**.  Consequently there is `ρ_Q < ∞` with
`C(Q) ⊆ [−ρ_Q,ρ_Q]^{Q}`, and

    \#\{λ ∈ Λ_W(Q) : mK+λ ≥ 0\} ≤ (2mρ_Q+1)^{d} ,\qquad
    \log\# ≤ d\,\log(2mρ_Q+1) = O_Q(\log m) .                           (13.3)

*Proof.*  (i) The defining condition is a family of closed linear inequalities,
one for each `t ∈ R` (`x ↦ K(t)+Σx_qw_q(ΠK)(t−\log q)` is affine and
continuous in `x`), so `C(Q)` is a closed convex set, and `0 ∈ C(Q)` because
`K > 0`.  (ii) `mK + Σx_qw_qτ_{\log q}(ΠK) ≥ 0 ⟺ K + Σ(x_q/m)w_qτ_{\log q}(ΠK)
≥ 0`: the constraint is positively homogeneous, so the feasible set at level
`m` is exactly `m\,C(Q)`.
(iii) Let `x` be a recession direction of `C(Q)`, i.e. `0 + λx ∈ C(Q)` for
every `λ > 0` — equivalently (by (i), for a closed convex set containing `0`)
`K + λN ≥ 0` for all `λ > 0`, where `N := Σ_qx_qw_qτ_{\log q}(ΠK)`.  Dividing
by `λ` and letting `λ → ∞` gives `N ≥ 0` pointwise.  But `N ∈ 𝓝_∞` (a finite
linear combination of elements of the linear subspace `𝓝_∞`, Theorem 11.11),
so `\deg N = 0` by Theorem 11.13(ii); a continuous `N ≥ 0` with `\deg N = 0` is
identically `0` by Theorem 11.13(i); and then `x = 0` by the linear
independence of Theorem 13.5(i).  So the recession cone of `C(Q)` is `\{0\}`,
and a nonempty closed convex subset of `R^d` with trivial recession cone is
bounded.  (13.3) is then the count of integer points in a box.  ∎  `PROVED`

**Lemma 13.5b (a positivity constraint on the coefficients, and the sign of the
top one; `PROVED`).**  Let `λ = Σ_qa_qw_qτ_{\log q}(ΠK) ∈ Λ_W`, `λ ≠ 0`, with
`mK + λ ≥ 0`, and let `Q` be the largest prime power with `a_Q ≠ 0`.  Then

    m + σ(1−σ)\,Σ_q a_q\,w_q\,q^{σ−1/2} ≥ 0 \qquad\text{for every } σ ∈ R ,
                                                                       (13.3b)

and consequently `a_Q ≤ −1`.  Taking `σ = ½`, also
`Σ_q a_q\,Λ(q)\,q^{−1/2} ≥ −4m`.

*Proof.*  Put `E := mK + λ ≥ 0`.  Every summand of `E` has a Mellin transform
that is **entire**, by the super-exponential decay of `K` and of `ΠK`
(Theorem 11.7(ii)): `Φ_K = ξ` and
`Φ_{τ_{\log q}ΠK}(s) = q^{s−1/2}s(1−s)ξ(s)`.  So for every real `σ` the
integral `Φ_E(σ) = ∫E(t)e^{(σ−1/2)t}dt` converges absolutely, and it is
`≥ 0` because the integrand is the product of a nonnegative function and a
positive one.  Now

    Φ_E(σ) = ξ(σ)\Big[m + σ(1−σ)Σ_qa_qw_qq^{σ−1/2}\Big] ,

and `ξ(σ) = Φ_K(σ) = ∫K(t)e^{(σ−1/2)t}dt > 0` for every real `σ`, because
`K > 0` (Theorem 11.7(i), whose positivity is now elementary).  Dividing by
`ξ(σ)` gives (13.3b).  *(This is an honest use of `ξ` as data: the inequality
names no zero and needs no import.)*  As `σ → +∞` the sum is dominated by its
largest exponent, `Σ_qa_qw_qq^{σ−1/2} = a_Qw_QQ^{σ−1/2}\big(1+o(1)\big)`, while
`σ(1−σ) = −σ²(1+o(1))`; so (13.3b) reads
`m − σ²a_Qw_QQ^{σ−1/2}(1+o(1)) ≥ 0`, and since `Q ≥ 2` the factor
`σ²Q^{σ−1/2} → +∞`, which forces `a_Qw_Q ≤ 0`.  As `w_Q > 0` and
`a_Q ∈ \mathbb Z∖\{0\}`, `a_Q ≤ −1`.  The case `σ = ½` is `m + ¼Σ_qa_qw_q ≥ 0`.
∎  `PROVED`

**Theorem 13.6 (the growth obstruction, on every finite truncation;
`PROVED`).**  Take `E = mK`, `m ∈ N`.  Then:

 (i) requirement (c) forces

          h⁰_{\mathbb Z}(mK) ≥ \tfrac14 m² − \tfrac14 m + χ \qquad (m ≥ 2),
                                                                        (13.4)

     because `I_∞(mK,mK) = ½m²`, `I_∞(mK,K) = ½m`, and
     `h⁰_{\mathbb Z}(K−mK) = h⁰_{\mathbb Z}((1−m)K) = 0` by Theorem 13.5(iii)
     and the convention of Definition 13.4, `\deg((1−m)K) = 1−m < 0`;
 (ii) for **every finite truncation** `Λ_W(Q)` of the lattice — and likewise
     for `Λ_1(Q)` — the corresponding count satisfies, by Lemma 13.5a,

          h⁰_{\mathbb Z,Q}(mK) ≤ d_Q\log(2mρ_Q+1) = O_Q(\log m) = o(m²) ,

     so (13.4) fails for all large `m`: **the truncated candidate does not
     satisfy (c)**, whatever the constant `χ`.  It does satisfy (a) and (b′)
     (Theorem 13.5(iii),(iv)); (c) is the only failure.

*Proof.*  (i) is the displayed computation with Theorem 11.8(ii),(iii).
(ii) is Lemma 13.5a(iii) and `\log m = o(m²)`.  ∎  `PROVED`

**[WITHDRAWN, phase 135 round 2, finding M8 of `R135_002` and LF4 of
`R135_003`.  Round 1 stated, as part of a `PROVED` Theorem 13.6, the bound

        \#H⁰_{\mathbb Z}(mK) ≤ (2B(m)+1)^{d(m)},\quad d(m) = O(\sqrt{\log m}),
        \quad B(m) = O(m)                                              (13.4-r1)

for the **full** lattice, "hence `h⁰_{\mathbb Z}(mK) = O((\log m)^{3/2})`".
Its proof is not a proof.  The displayed inequality
`0 ≤ mK(\log n_0+t_0) − |a_{n_0}|Λ(n_0)n_0^{−1/2}c_0 +
c_1Σ_{n<n_0}|a_n|Λ(n)n^{−1/2}` was used to conclude
`Λ(n_0)n_0^{−1/2}c_0 ≤ mK(\log n_0+t_0)+c_1Bn_0\log n_0`, whose right-hand side
grows with `B` and `n_0` while the left tends to `0`: the inequality as derived
is vacuous.  The two load-bearing steps ("the unique index attaining `B`", and
"`K(\log n_0+t_0) ≥ c/m` **is necessary**") were asserted, not derived, and the
competing generators at indices `n ≈ n_0` are of the same order at the
evaluation point, not negligible.  **(13.4-r1) is withdrawn in full.**  It is
replaced by (13.3) on finite truncations, which is proved, and by the structural
Lemma 13.5b.  Whether `h⁰_{\mathbb Z}(mK) = o(m²)` on the **full** lattice is
recorded as `OPEN`, §14.5 item (23).]**

**Remark 13.6b (`HEURISTIC`; why the round-1 mechanism is not merely unproved,
and what the obstruction to it is).**  Single-point evaluation cannot bound the
coefficients on the full lattice, for a structural reason.  Two generators at
**adjacent** prime powers `q < q'` are nearly parallel: `τ_{\log q}(ΠK)` and
`τ_{\log q'}(ΠK)` differ by a translation of
`\log(q'/q) = O\big((q'−q)/q\big) = O(\log q/q) = o(1)`, so
`w_{q'}τ_{\log q'}(ΠK) − w_qτ_{\log q}(ΠK)` is small in every `C^k` norm on
compacta once the change of weight `w_{q'}−w_q` is taken into account.
**[CORRECTED, phase 135 round 3, finding N6 of `R135_005`: round 2 wrote
`\log(q'/q) = O(1/q)`, which consecutive prime powers do not satisfy — gaps are
`≍\log q` on average — and the displayed difference also carries the change of
weight.  Only `\log(q'/q) → 0` is used, so the conclusion is unaffected; and
the remark is now labelled `HEURISTIC`, like Remarks 12.4b, 13.6a, 13.7 and
14.5a.]**  A pair of large opposite coefficients on such a pair therefore
produces a **small** class, and nothing evaluated at one point excludes
`|a_q| ≫ m`.  So `B(m) = O(m)` is not just unproved; **it should not be
expected**, and the remark of round 1 that "`mK` dominates `τ_{\log n}(ΠK)`
only for `n ≲ \sqrt{\log m}`" describes the behaviour of a *single* generator,
not of the lattice.  Lemma 13.5a shows the near-degeneracy is nevertheless
harmless in each fixed rank — `C(Q)` is bounded for every finite `Q`, with a
constant `ρ_Q` that the argument does not control uniformly in `Q`, and the
uniformity is exactly what is open.

**Remark 13.6a (the mechanism, in one sentence, as a heuristic).**  `K` decays
like `e^{−πe^{2|t|}}`, so a class `mK` dominates a *single* translate
`τ_{\log q}(ΠK)` only for `\log q ≲ \tfrac12\log\log m`: **the arithmetic curve
of row D appears to have far too few integral sections**, and the apparent
deficit is not marginal — it is the difference between a logarithm and `m²`.
The numerics below find the count `1` for every `m` tested.  `#` **itself**
(rather than its logarithm) is not excluded by (13.3) for growing rank, and
this is said because it is the one loophole the argument leaves; but `#` is not
a dimension and cannot occupy the `h⁰` slot of a Riemann–Roch identity, whose
additivity under exact sequences is logarithmic in a count.  **Everything in
this remark beyond Theorem 13.6(ii) is heuristic.**

**[CORRECTION OF RECORD, entered with Part III (§18).  The first sentence of
this remark is no longer heuristic: the domination of a single translate
`τ_{\log q}(ΠK)` by `mK` is a **theorem in both directions**, in the sharp
form `e^{πq²} ≤ m ≲ e^{5.1q²}` per generator — a necessary and a sufficient
bound of the same shape, proved in §18.  What remains heuristic is only the
passage from one generator to the lattice; there §18 replaces the heuristic by
the unconditional lower bound `h⁰_{\mathbb Z}(mK) ≫ (\log m)^{3/2}/\log\log m`
and by the certified non-vanishing `H⁰_{\mathbb Z}(mK) ≠ 0` from
`m ≈ 4.5·10^6`.  The deficit against `m²` is unchanged.]**

**Remark 13.7 (`HEURISTIC`: the weights are not the discriminating datum).**
**[DEMOTED from Theorem 13.7, phase 135 round 2, finding M1 of `R135_002`,
ruling §4 of `R135_003`.  Round 1 stated, `PROVED`: "`h⁰_{\mathbb Z}` and
`h⁰_{Λ_1}` both fail (a)+(b′)+(c) by Corollary 12.4a as well".  With
Restatement 12.4a recast as a schema about proofs, **that claim is
withdrawn**.]**  What remains is an observation, and it is the most useful one
in §13.  Both lattices are model-uniform in the sense of (12.3): `Λ_1` because
it mentions no arithmetic at all, and `Λ_W` because — with the substitution
`Λ(n) ↦ Λ(n)(n^a+n^{−a})` — it is defined for `Ξ_a` too.  **The weights `w_q`
are Euler data, but they enter `Λ_W` only as positive numbers, and the
falsifier supplies positive numbers too.**  So merely *mentioning* `Λ(q)` puts
no `ξ`-specific line into any proof, and Restatement 12.4a says such a proof
cannot succeed.  The datum that `Ξ_a` genuinely lacks is the **unimodularity**
of the local roots, `Frob_n ⋆ Frob_n^† = Δ^{(n)}` (Paper 44 Theorem
3ter.6(ii)), which for `Ξ_a` reads `(n^a+n^{−a})Δ^{(n)}` and fails (Theorem
7.1(iii)).  **This is a direction for construction and it is not a theorem.**

*Numerics (`COMPUTATIONAL-ILLUSTRATION`, `scripts/h0_candidate.py --check`;
run of record executed in round 2, `ALL CHECKS PASSED`, exit `0`, 15 s; the
`--fast` run, 0.2 s, over the smaller index set `q ≤ 5`, agrees on every line
it shares).*  `\deg(ΠK) = ∫ΠK·2\cosh(t/2)\,dt = −4.1\cdot10^{−15}` (predicted `0`;
`float64`, so `10^{−15}` is the arithmetic floor); on the grid
`t = −4.0(0.04)4.0`, `ΠK` attains `\max = 16.953849` at `t = 0` and
`\min = −8.669861` at `t = −0.40`, so the constraint is genuinely two-sided;
`\#H⁰_{\mathbb Z}(0) = \#H⁰_{Λ_1}(0) = 1`.

**`[phase 135 round 2, R135_004`: three corrections to the round-1 numerics
paragraph.  (1) The index set is now the **prime powers** `q ≤ 7`, i.e.
`\{2,3,4,5,7\}`, in both lattices (finding M7); round 1 ranged
over `n ≤ 3` and over `n ≥ 2` inconsistently with (13.1) as then written.
(2) `\deg(ΠK)` is printed as reproduced: round 1's `1.5\cdot10^{−18}` came from
an `mpmath` run at 18 digits and is withdrawn in favour of the `float64` value
above; the extrema `16.9538` / `−8.6699` of round 1 **are** reproduced, now
with the abscissae at which they occur, and `ΠK` is differentiated term by term
from (11.7) rather than by finite differences.  (3) The round-1 note that the
default parameters exceed a 1500 s budget no longer applies: the enumeration is
vectorised.]**

For `E = mK`, `m = 1,\dots,8`, with generators at the prime powers `q ≤ 7`
(five of them) and coefficients `|a_q| ≤ 6` — a search over `13^5 = 371\,293`
lattice points per row, tested against the grid `t = −4.0(0.04)4.0`:

| lattice | `m` | `\#H⁰_{\mathbb Z}(mK)` | `\log\#` | `\tfrac14m²−\tfrac14m` |
|---|---|---|---|---|
| naive `Λ_1` | 1,…,8 | 1 | 0 | 0, 0.5, 1.5, 3.0, 5.0, 7.5, 10.5, 14.0 |
| arithmetic `Λ_W` | 1,…,8 | 1 | 0 | 0, 0.5, 1.5, 3.0, 5.0, 7.5, 10.5, 14.0 |

The count is `1` — only the zero correction — for every `m` tested and both
lattices, while the right-hand side of (c) grows quadratically.  **This
illustrates Theorem 13.6(ii) at one particular truncation; it proves nothing,
it says nothing about the full lattice (open item (23)), and it is not evidence
about any sign.**

### 13.3 The three genera, recorded and not reconciled

**Finding 13.8 (`PROVED` as arithmetic, `OPEN` as a reconciliation).**  The
corpus now carries three mutually inconsistent "genus" numbers, and they are
recorded side by side **without reconciliation by fiat**.

| source | canonical datum | genus read off `\deg K = 2g−2` |
|---|---|---|
| Connes–Consani, *Riemann–Roch for `\overline{\mathrm{Spec}\,\mathbb Z}`* (arXiv:2205.01391v2, §5, Theorem "serredual") | `K_{CC} = −2\{2\}`, `\deg K_{CC} = −2\log 2` | `g_{CC} = 1 − \log 2 ≈ 0.3069`, consistent with their RR `h⁰−h¹ = \lceil \deg'D+\log'2\rceil' − \mathbf 1_L` read against `\deg D + 1 − g` |
| row D, here | `Φ_K = ξ`, `\deg K = 1`, `I_∞(K,K) = ½` | `g_D = \tfrac32` |
| row B, Paper 44 Theorem 8bis.2 | `Δ·Δ = −∞` | `g_B = ∞` |

Three remarks, and no more.
 1. *The scale is not free here.*  Paper 44 Theorem 8bis.8 fixes the shell
    normalization only **up to a global scale `λ`**, and `I_∞ ↦ λI_∞` under
    it.  But `\deg F = Φ_F(0)+Φ_F(1)` and `Φ_K = ξ` are **defined without
    reference to the measures**, and the identity `I_∞(F,K) = ½\deg F` of
    Theorem 11.8(i) comes from the explicit formula, whose two sides are
    normalized independently.  So `λ = 1` is forced, and `\deg K = 1`,
    `I_∞(K,K) = ½` are scale-free statements given the declared measures.
    **The blueprint's reading "`\deg K = 1 = 2(2g−2)`" is not derived from
    anything and is not adopted; `\deg K = 2g−2` gives `g_D = \tfrac32`, and
    even that is a convention about which formula to read, not a theorem.**
 2. *They measure different objects.*  `g_{CC}` is a genus of a curve
    `\overline{\mathrm{Spec}\,\mathbb Z}` over `\mathbb S`; `g_D` reads a
    surface-theoretic `K` through a curve formula; `g_B` is the
    self-intersection of the diagonal of a *surface* in the divergent
    normalization of Theorem 8bis.2, which is a **fixed-chart** statement
    explicitly exempted from `(C1)`.
 3. *No identification is asserted*, and none of the three is used in any
    proof above.  This is a finding for the record.

---

## 14. D.10 — connections to rows A and B, and the Part II ledger

### 14.1 `K` in the ruling plane

**Proposition 14.1 (`PROVED-IN-REPOSITORY`).**  In the ruling plane `B_T` of
(1.8), with `M(F) = (Φ_F(1),Φ_F(0))` and `β_T = \begin{pmatrix}0&1\\1&0\end{pmatrix}`
in the basis `e_\mp`:
 (i) `M(K) = (½,½) = ½(e_-+e_+)`, and `β_T(M(F),M(K)) = ½\deg F = I_∞(F,K)`
     for every `F ∈ D^W` — **the polar packet of (11.6) is the whole pairing
     against `K`**, the zero sum contributing nothing (Theorem 11.8(i));
 (ii) `β_T(M(K),M(K)) = 2·½·½ = ½ = I_∞(K,K)`;
 (iii) `†` acts on `B_T` by the swap `♯` (Paper 43 Theorem 9.1), and
     `M(K^∨) = M(K)`, i.e. `K` is `†`-**fixed** in the ruling plane; `σ_K`
     acts on `B_T ⊕ P` by `(b,f) ↦ (M(K)−b, −f)` — an affine reflection whose
     linear part is `−\mathrm{id}` and whose fixed point is `½K`;
 (iv) the statement "`K ≡ ½(e_++e_-)`" is true **as an identity of ruling
     data** and is false as an identity of classes, because `e_\pm ∉ D^W`
     (Paper 43 Theorem 9.14c; the repair of Theorem 11.14).

*Proof.*  (i),(ii) are Theorem 11.8 and (1.8).  (iii) `K^∨ = K` (evenness),
and `σ_K` is affine with linear part `−\mathrm{id}` and `M` linear.  (iv) is
the cited refutation.  ∎  `PROVED-IN-REPOSITORY`

### 14.2 `Frob_n` and the canonical class

**Proposition 14.2 (`PROVED-IN-REPOSITORY`).**  For `n ≥ 1`,
`τ_{\log n}K` is the image of `K` under the modulus translation by which
`Frob_n` acts on radial classes, and

    M(τ_{\log n}K) = ½\,(n^{1/2},\,n^{−1/2}) = M(Frob_n)\cdot M(K) ,
    I_∞(F, τ_{\log n}K) = ½\big(n^{1/2}Φ_F(0) + n^{−1/2}Φ_F(1)\big) ,   (14.1)

so **the Frobenius pairs with the canonical class through the rulings only**,
with the same weights `n^{\pm1/2}` by which it acts on the rulings themselves
(Paper 44 Theorem 3ter.6(iii), Theorem 3ter.10).  `τ_{\log n}(ΠK) ∈ 𝓝_∞`
for every `n`, and these classes are `R`-linearly independent (Theorem 13.5(i));
so the Frobenius family generates an infinite-rank lattice inside the radical
— **the principal classes of row D's surface are indexed by the Frobenius
family**, and that is the exact sense in which "principal" is arithmetic here.

*Proof.*  Theorem 11.8(iii), Theorem 11.11, Theorem 13.5(i), and the
multiplicativity `λ_∓(F⋆G) = λ_∓(F)λ_∓(G)` of Paper 43 Theorem 9.1.  ∎
`PROVED-IN-REPOSITORY`

### 14.3 `D^W` versus the colimit `T_∞`

**Theorem 14.3 (`PROVED`).**
 (i) `D^W ⊄ D_A^∞` and `D_A^∞ ⊄ D^W`: every element of the colimit is
     compactly supported (Finding 11.0) and `K` is not; conversely `D_A^∞`
     contains non-radial tests, which `D^W` does not model.
 (ii) `D^W` **is** a module over the radial subalgebra: `Γ_h ⋆ Γ_g = Γ_{h∗g}`
     for `h ∈ C_c^∞` and `g ∈ D^W` lands in `D^W` (Lemma 11.2(i)); so `D^W` is
     a `D_A^{rad}`-module and a `D_A^{∞,rad}`-module, and `τ_a` is the action
     of the archimedean Frobenius group `Frob_∞` of (1.5).
 (iii) `I_∞` on `D^W` **restricts** to `I_∞` on `D_A^{rad}`: on compactly
     supported radial tests, (11.5) is Paper 43 Definition 9.2 with the
     colimit trace, and (11.6) is (9.9).  So `D^W` is a genuine enlargement of
     the radial sector on which the same form lives, obtained from the
     explicit formula and **not** from (8A.21).
 (iv) Consequently the completion in which row D's Hodge-index shape can even
     be posed is **not** the colimit of Paper 43 (8A.7c), and the blueprint's
     sentence "the Hodge-index shape rows A–C lack at every chart exists in the
     colimit completion" is **`REFUTED` as stated** and **`REPAIRED`** to: it
     exists in the **Weil completion `D^W`**, and Theorem 11.12 shows it does
     *not* exist in the colimit itself, where the perp of the primitive sector
     is still `0`.

*Proof.*  (i) Finding 11.0 and Theorem 11.7(ii).  (ii) Lemma 11.2(i),(ii) and
(1.3).  (iii) Theorem 11.3 specializes to Corollary 9.4a on `C_c^∞`, and
Theorem 11.5 to (9.9).  (iv) Theorem 11.12 and Theorem 11.8(iv).  ∎  `PROVED`

### 14.4 Part II ledger: blueprint claims refuted or repaired

| `R135_000` claim | verdict | where |
|---|---|---|
| D.6(i): the class is `g,g'` of decay `O(e^{−(½+ε)\|t\|})`, and (9.9) extends to it, `CLASSICAL` | **`REFUTED` as an instruction** — on that class `Φ_g` is holomorphic only in `−ε<\mathrm{Re}\,s<1+ε`, so the repository's contour proof (Thm 9.4) cannot reach `L_c`, `c>1`; and with only `g,g'` the zero sum is **not** known to converge absolutely (`Σ\|γ\|^{−1} = ∞`).  **`REPAIRED`:** `D^W` of Definition 11.1 (`C²`, decay `e^{−(1+ε)\|t\|}`), on which the proof extends verbatim and the zero sum converges absolutely | §11.1, Thm 11.3 |
| D.6(iii): `P^⊥ ∩ D^W = ξ·(\text{entire}) ∩ \mathrm{Mellin}(D^W)` | **`REFUTED`** — the perp condition is vanishing of `Φ_G` at each zero **to order one**; the stated equality holds **iff every zero of `ξ` is simple**, which is `OPEN`.  Unconditional form: (11.13).  Writing the equality would have been an unproved statement about the zeros | §11.3, (11.13) |
| D.6(iii): the independence argument, "`Σ_ρ c_ρρ(1−ρ)e^{(ρ−½)t}` vanishes only if all `c_ρ = 0`; convergence stated" | **`REPAIRED`** — as written the series need not converge (`\|c_ρρ(1−ρ)\| = O(1)`, no decay).  The correct statement uses `c_ρ = Φ_G(1−ρ)` **without** the factor `ρ(1−ρ)`, converges absolutely by (11.2)+(E3d), and the independence is proved by a Laplace transform and a residue, not by an appeal to almost periodicity | Lemma 11.9 |
| D.7(i): `𝓝_∞ = ΠK ⋆ D^W` | **`REFUTED`** — `⊇` fails.  `τ_a(ΠK) ∈ 𝓝_∞ ∖ ΠK⋆D^W` for every `a ≠ 0` (Riemann–Lebesgue against a unimodular symbol); structurally, `ξ` decays like `e^{−π\|τ\|/4}` on the critical line while `Φ_N` is only `O(τ^{−2})`, so dividing by `ξ` leaves the class of transforms.  Correct description: (11.14) | Prop 11.11a |
| D.7(ii): "a **new proof** of Paper 45 Theorem 12.2" | **`REFUTED` as a description** — Thm 12.2 is a fixed-chart Plancherel statement about `I_A` and `\hat T_S`; Theorem 11.12 is a colimit statement about `I_∞` proved by zero counting.  It supplies precisely what Paper 45 **Remark 12.4** declined to assert, and is recorded as a new theorem, not a second proof | Thm 11.12 |
| D.7(iv) and §1: `\deg F := I_∞(F,A)`, `A = e_++e_-`, and "`F+mA` is ample" | **`REPAIRED`** — `e_\pm` are not elements of any function class here (Paper 43 Thm 9.14c: they live in the completion and are its radical).  `2K` is an intrinsic degree-computing ample class, and the ample family is `F+2mK`, `m > C_F` | Thm 11.8(v), Thm 11.14(iii) |
| §1: "the Hodge-index shape … exists in the **colimit** completion", reconciling Paper 43 Thm 14.1(d) | **`REFUTED` as stated, `REPAIRED`** — the colimit consists of compactly supported tests and its own perp is still `0` (Thm 11.12).  The shape appears in the **Weil completion `D^W`**, which is not the colimit and on which `T_∞`'s formula (8A.21) does not even converge | Finding 11.0, Thm 14.3 |
| §1: `T_∞(K) = 1`, `I_∞(K,K) = ½`, `M(K) = (½,½)`, `∫K = ξ(½)`, `Φ_K(0)=Φ_K(1)=½` | **confirmed**, proved and checked numerically to `10^{−26}`; **[phase 135 round 2, finding M12: the first is written `⟨K,W_{fin}+ω_∞⟩ = 1`, not `T_∞(K) = 1` — `T_∞` does not extend to `K` (Finding 11.0)]** | Thm 11.7, Thm 11.8 |
| D.8: `(b′)` needs "`E' ≥ 0` nonzero"; `E ≡ E' \bmod 𝓝_∞` preserves `\deg` and `I_∞(\cdot,F)` | **confirmed**, both; the second because `𝓝_∞` is the radical, (11.14) | Rem 12.3b |
| D.8: the transfer theorem needs `χ ≥ 0` (inherited from (6.2)) | **improved** — no sign condition on `χ` is needed; the quadratic term dominates | Thm 12.3, Step 3 |
| D.9(i): `H⁰(0) = \{0\}` "modulo `\ker Π`" | **`REPAIRED`** — exactly `\{0\}`: `\ker Π ∩ D^W = 0` (Lemma 11.2(v)) | Thm 13.2(i) |
| D.9(iii): "row D `\deg K = 1 = ``2(2g−2)``" | **`REFUTED` as a reading** — nothing derives the factor `2`; `\deg K = 2g−2` gives `g_D = \tfrac32`, and that too is a choice of formula, not a theorem | Finding 13.8 |

**Running count.**  Part II refutes or repairs **eight** blueprint claims of
`R135_000` and confirms three, on top of the nine of §9.2.  No result of Part I
is affected.

### 14.4a Round-2 repair ledger (phase 135, `R135_004`)

Every finding of the adversarial audit `R135_002` and of the final audit `R135_003`
that was ruled mandatory, with the edit that answers it.

| finding | severity | repair in this paper |
|---|---|---|
| **M1** / LF5 | `FATAL` | Corollary 12.4a → **Restatement 12.4a**, `RESTATEMENT (schema)`: a principle about admissible *derivations*, with `Z` removed from the data list (12.3).  Remark 12.4b demoted to `HEURISTIC`.  Theorem 13.3 → **Restatement 13.3** (schema); its quantified form **withdrawn**.  Theorem 13.7 → **Remark 13.7**, `HEURISTIC`; its claim **withdrawn**.  §14.5 rewritten below |
| **M2** / LF3 | `MAJOR` | Definition 11.4 is now by **polarization** of `Q(X) = ⟨X⋆X^∨,W_{fin}+ω_∞⟩`; Lemma 11.4a proves the three descriptions agree and proves (11.6) off the diagonal.  The false parenthetical "`h^∨ = h`" is deleted |
| **M3** | `MAJOR` | Theorem 11.12 now counts **distinct** zeros, via the new import **(X18)** (Conrey 1989: `≥ \tfrac25` of the zeros are simple).  Propagated to Paper 45 Remark 12.4a and Paper 43 Remark 14.1a |
| **M4** / LF1 | `MAJOR` | Proposition 12.6's hypothesis is now `\|\mathrm{Re}\,ρ−½\| ≤ θ` (12.4), which `Ξ_a` satisfies; the Laplace abscissa is `\mathrm{Re}\,s > ½+θ`; `Z(p) > 0` for `p ∈ P` is proved, not assumed |
| **M5** | `MAJOR` | Proposition 12.6's proof lists the statements re-read and **proves** the three non-verbatim substitutions (contour abscissa; Lemma 11.9's exponents and half-plane; Theorem 11.14's weight) |
| **M6** / LF2 | `MAJOR` | The `Ξ_a`-analogue of Paper 45 Theorem 10.4 is now **Lemma 12.4A** (rank-4 `Π_P`, its Green kernel, `π_P(1−s) = π_P(s)`, `Ξ_a > 0` on `R`) and **Proposition 12.4B** (quartet, `106_11` (20)–(21), (E6), (E3d), degree bump `D ↦ D+4`) |
| **M7** | `MAJOR` | `Λ_W` and `Λ_1` are indexed by **prime powers**; Theorem 13.5(i),(ii) repaired; `h0_candidate.py` corrected |
| **M8** / LF4 | `MAJOR` | Round 1's (13.4) **withdrawn in full**.  Replaced by Lemma 13.5a (homogeneity `C_m = mC_1`, trivial recession cone, boundedness) and Lemma 13.5b (`a_Q ≤ −1` from the positivity functionals `Φ_E(σ) ≥ 0`).  Theorem 13.6 now closes the route on **every finite truncation** and says so; the full lattice is `OPEN` (item (23)) |
| **M9** | `MAJOR` | Theorem 11.14 re-proved on the **spectral** side: (11.16) is the zero-side density `w_F`, and (11.17) needs only `0 < \mathrm{Re}\,ρ < 1`.  The archimedean-kernel and Chebyshev route is demoted to Remark 11.14a′ and used nowhere; the kernel representation of `ω_∞` on `D^W` is open item (21) |
| **M10** | `MINOR` | the bracket `⟨h,W_{fin}+ω_∞⟩` is `\mathrm{PRIME}−\mathrm{ARCH}`, said explicitly |
| **M11** | `MINOR` | §1.13 amended: the classical zero-location **data** used in Part II are listed, and the rule in force is restated in its correct, stronger form |
| **M12** | `MINOR` | `T_∞(K)` replaced by `⟨K,W_{fin}+ω_∞⟩` everywhere |
| **M13** | `MINOR` | (S2)'s factor `2` and (S3)'s abscissa `½+θ < c` corrected in Proposition 12.6 |
| **M14** | `MINOR` | Lemma 11.2(ii) restated as `Π(D^W_4) ⊆ D^W` with the decay of `g''',g''''` imposed |
| **M15** | `MINOR` | `h⁰_{\mathbb Z} := 0` on `\{H⁰ = ∅\}` recorded as a **convention**, not as forced, with `\log\#∅ := 0` stated as that convention.  **[Round 2's second clause — that Remark 13.5c shows the candidate fails (b′) — is withdrawn in round 3, finding N2: (b′) holds unconditionally.]** |
| **M16** | `NOTE` | the one-directionality and the unproved satisfiability of (a)+(b′)+(c) are stated as open item (20) |
| **M17** | `NOTE` | (X12)'s normalization confirmed by two independent recomputations; recorded |
| **LF6** | `NOTE` | positivity of `K` proved in one line from (11.7); the import is now only evenness and the Fourier identity |
| **LF7** | `NOTE` | new heuristic Remark 14.5a below, and open item (18) restated in its terms |
| numerics | — | `canonical_pairings.py` rewritten (`--check` exits `0` in 28 s — the figure printed by `R135_004` §3.2 and repeated in §16; round 2's ledger row said 26 s, corrected in round 3, finding N8; `--fast` in 10 s); `h0_candidate.py` rewritten with prime-power indexing and a `--fast` mode; every number printed in Part II is from a run executed in round 2 |

### 14.4b Round-3 repair ledger (phase 135, `R135_006`)

Every finding of the round-2 adversarial confirmation `R135_005` (N1–N8), with the
edit that answers it.  No new numerics; no sign; §10's label is still **None**.

| finding | severity | repair in this paper |
|---|---|---|
| **N1** | `MINOR` | the two factors `½` in (11.17) deleted: `C_F ≤ |Φ_F(0)|+|Φ_F(1)|+Σ_ρ|Φ_F(1−ρ)|`.  The proof line now records `\sup_u e^{\pm u/2}/2\cosh(u/2) = 1` and `\sup_u e^{|u|/2}/2\cosh(u/2) = 1`, so the coefficient is `1` and is sharp.  Nothing downstream quotes the `½`: Theorem 12.3 Step 1 needs only `C_F < ∞` and any `m > C_F` |
| **N2** | `MAJOR` | **(b′) holds unconditionally for `h⁰_{\mathbb Z}`**, and is now proved: `h⁰_{\mathbb Z}(E) > 0` gives `\#H⁰ ≥ 2`; `Λ_W ⊂ 𝓝_∞` gives `\deg(E+λ) = \deg E`; `\deg E < 0` empties `H⁰`, `\deg E = 0` forces `E+λ ≡ 0` (Theorem 11.13(i)) hence `\#H⁰ ≤ 1`; so `\deg E > 0` and `E' ≢ 0`.  Theorem 13.5(iii) restated and reproved; **Remark 13.5c withdrawn and replaced**; the three propagations deleted — Theorem 13.6(ii) ("(c) is the only failure"), §14.5 item (3), and the M15 row of §14.4a |
| **N3** | `MINOR` | Theorem 11.12 removed from Proposition 12.6's verbatim list, with a new paragraph "**Not claimed for `Ξ_a`: Theorem 11.12**" — its repaired proof is `ζ`-specific through import (X18), and nothing uses it for `Ξ_a` |
| **N4** | `MAJOR` | §10's "so that any `h⁰` must use the Euler product" replaced by the schema-honest wording of Restatement 12.4a: no **model-free** derivation can exist; no function `h⁰` is excluded; the Euler-product reading survives only as the heuristic Remark 12.4b |
| **N5** | `MINOR` | Proposition 12.4B gains a *The strip* paragraph widening `106_11` (15),(16),(27),(29) from `|\Im z| ≤ ½` to `|\Im z| ≤ ½+a`, justified by `Φ = \hatφ`, `φ ∈ C_c^∞`, being Paley–Wiener on **every** horizontal strip (only the constants change, and they enter no conclusion); and the bump `D ↦ D+4` is re-derived from (27)–(30) — degree `4` symbol `π_P` and **four** interpolation conditions at the quartet, against degree `2` and **two** in Paper 45 |
| **N6** | `NOTE` | Remark 13.6b: `\log(q'/q) = O(1/q)` → `O(\log q/q) = o(1)`, with the change of weight `w_{q'}−w_q` named; the remark is labelled `HEURISTIC` |
| **N7** / **M11** | `MINOR` | §1.13 amended again: the rule is stated as actually obeyed — nothing about zero locations beyond the listed classical facts, those entering only as data, with `ξ > 0` on `R` (Lemma 13.5b) and "no real zero of `Ξ_a`" (Lemma 12.4A(v)) named as zero-location statements proved here from `K > 0`; **Lemma** 12.4A corrected for "Proposition 12.4A"; Theorem 11.14 added to the list |
| **N8** / **M15** | `NOTE` | (X13)–(X15) removed from Theorem 12.3's import line; §14.4a's `26 s` → `28 s` (the figure `R135_004` §3.2 printed, matching §16); Definition 13.4 states `\log\#∅ := 0` as the convention; the phase `README.md` row for `polya_class.py` now writes `⟨K, W_{fin}+ω_∞⟩ = 1` per Finding 11.0 |

**Withdrawal table (rounds 2 and 3).**  Statements whose label changed, and
what is no longer claimed.  The last row is round 3.

| statement | round-1 label | round-2 label | what is withdrawn |
|---|---|---|---|
| Corollary 12.4a | `PROVED` | **Restatement 12.4a**, `RESTATEMENT (schema)` | that no model-uniformly *defined* `h⁰` satisfies (a)+(b′)+(c) for `ζ`; and the reading under which `Z` is itself a datum |
| Remark 12.4b | "the main structural output of Part II" | `HEURISTIC` | that the definition of `h⁰` **must** use a datum `Ξ_a` lacks |
| Theorem 13.3 | `PROVED` | **Restatement 13.3**, `RESTATEMENT (schema)` | that no functional of `H⁰(E)` alone satisfies (a)+(b′)+(c).  Reopened as item (22) |
| Theorem 13.7 | `PROVED` | **Remark 13.7**, `HEURISTIC` | that `h⁰_{\mathbb Z}` and `h⁰_{Λ_1}` fail by the schema; the unimodularity reading survives as a direction |
| (13.4) of round 1, `d(m) = O(\sqrt{\log m})`, `B(m) = O(m)` | `PROVED` | **withdrawn** | the growth bound on the **full** lattice, and with it `h⁰_{\mathbb Z}(mK) = O((\log m)^{3/2})`.  Replaced by (13.3) on finite truncations and by (13.3b).  Item (23) |
| Theorem 11.12 | `PROVED` (multiplicity count) | `PROVED` (distinct count, (X18)) | nothing — the statement stands, on a sharper import |
| Theorem 11.14(i),(ii), round 1 form | `PROVED` via `R_F` and `K_∞` | `PROVED` via `w_F`; arithmetic form → Remark 11.14a′ | that the archimedean term of (11.3) equals a `K_∞`-kernel integral on `D^W`.  Item (21) |
| Definition 11.4, round 1 form | definition | superseded by polarization | that `F⋆G^∨` is even for `F ≠ G` |
| Definition 13.4, round 1 index set `n ≥ 2` | definition | prime powers | Theorem 13.5(i),(ii) as stated for that index set |
| Theorem 11.8(iii) numerics | "does not reproduce" | reproduced to `7\cdot10^{−15}` | the round-1 figures `3\cdot10^{−18}` (`P1`) and the `P2` failure |
| **Remark 13.5c** *(round 3, finding N2)* | round-2 assertion, unlabelled | **withdrawn and replaced** | that `h⁰_{\mathbb Z}` fails (b′), and with it the reading "the candidate fails before any growth estimate".  (b′) **holds** unconditionally (Theorem 13.5(iii)); the only failure on record is (c), on every finite truncation, and the full lattice stays `OPEN` (item (23)).  The three propagated clauses (Theorem 13.6(ii), §14.4a's M15 row, §14.5 item (3)) are deleted |

### 14.5 What Part II adds to §9.1, and what it closes

**[REWRITTEN, phase 135 round 2, ruling §4 of `R135_003`.  Round 1's version of
this section rested on Corollary 12.4a and on Theorems 13.3, 13.6, 13.7 as
round 1 stated them.  With M1 and M8 answered, the honest statement of what
Part II delivers is below, and it is weaker than round 1's.]**

* **Closed:** §9.1 item **3a** (a duality carrying the primitive sector off
  itself) — `σ_K`, Theorem 12.2, Proposition 12.5.  *This is unaffected by the
  round-2 findings.*
* **Replaced:** §9.1 item **3** (a functor `h` satisfying (R1)–(R5)) by:
  *a function `h⁰ : D^W → R_{≥0}` satisfying (a),(b′),(c) of Theorem 12.3*.
  `OPEN`.  What is known about it: **(1)** it suffices for row D's target
  (Theorem 12.3, a genuine reduction, proved); **(2)** no **model-free**
  derivation of (a)+(b′)+(c) can exist — any proof must at some line read a
  datum of `ξ` that `Ξ_a` does not share (Restatement 12.4a, a schema);
  **(3)** the natural lattice-counting candidates satisfy (a) and (b′)
  unconditionally (Theorem 13.5(iii),(iv)) and fail (c) on every finite
  truncation (Theorem 13.6(ii)); whether they fail (c) on the full lattice is
  `OPEN` (item (23)).  **What is *not* known: whether any `h⁰` with the three
  properties exists at all** — the reduction has never been shown to be
  non-vacuous, not even under RH and not even for a function-field model.
* **New open items.**
  (16) Whether `𝓝_∞ = \{Φ_N = ξ·e\}` — equivalently whether every zero of `ξ`
       is simple — is `OPEN` and **may not be attempted here**, being a
       statement about the zeros; (11.13) is stated in the only unconditional
       form available.
  (17) Whether `#H⁰_{\mathbb Z}` itself (not its logarithm) can occupy the
       `h⁰` slot: excluded on type grounds (a count is not a dimension) and
       not excluded by (13.3); recorded as the one loophole of Theorem 13.6.
  (18) A `h⁰` built from `Frob_n ⋆ Frob_n^† = Δ^{(n)}` — the partial-isometry
       property itself, not merely the weights `w_q` — is `NOT CONSTRUCTED`.
       Remark 13.7 and Remark 14.5a say why this is the place to look; neither
       is a theorem.  **[NARROWED, entered with Part III: see §19bis and the
       bookkeeping note below.]**
  (19) The reconciliation of the three genera of Finding 13.8 is `OPEN`, and
       is not to be effected by rescaling: the explicit formula fixes the
       scale Theorem 8bis.8 leaves free.
  (20) **[NEW, round 2, finding M16 of `R135_002`.]**  **Satisfiability.**
       Theorem 12.3 is one-directional: `(a)∧(b′)∧(c) ⇒ RH`, with no converse
       and no example — under RH, in a function-field model, or anywhere —
       showing the triple is consistent.  Until such an example exists, the
       deliverable of Part II is *a sufficient condition isolated and
       localized*, and nothing stronger.  `OPEN`.
  (21) **[NEW, round 2, finding M9 of `R135_002`.]**  The **kernel
       representation of `ω_∞` on `D^W`**: whether
       `\frac1{2π}∫\hat h(τ)[\mathrm{Re}\,ψ(¼+iτ/2)−\log π]dτ =
       −\mathrm{f.p.}∫h(t)K_∞(\|t\|)dt` for every real even `h ∈ D^W`, with the
       finite part of Paper 44 (8.5∞).  Known for `h ∈ C_c^∞` with
       `0 ∉ \mathrm{supp}\,h` (Paper 44 Theorem 3bis.7) and at `t = 0` by
       (8.5∞); the extension to unbounded support by the decay (11.1) is
       plausible and is **not proved here**.  Nothing in Part II depends on it
       (Remark 11.14a′).  `OPEN`.
  (22) **[NEW, round 2, finding M1 of `R135_002`.]**  Whether some rule `Φ` on
       convex subsets of `D^W` makes `h⁰ = Φ(H⁰)` satisfy (a)+(b′)+(c).  Round
       1 claimed a negative answer; the claim is withdrawn (Restatement 13.3).
       `OPEN`.
  (23) **[NEW, round 2, finding M8 of `R135_002`.]**  Whether
       `h⁰_{\mathbb Z}(mK) = o(m²)` on the **full** lattice `Λ_W` — equivalently
       whether `ρ_Q` of Lemma 13.5a can be controlled uniformly in the rank.
       Remark 13.6b explains why the round-1 mechanism cannot give it.  `OPEN`.
       **[CORRECTED, entered with Part III (§18).  The word *equivalently* in
       this item is wrong.  Uniform control of `ρ_Q` in the rank does **not**
       suffice for `h⁰_{\mathbb Z}(mK) = o(m²)`, nor is it implied by it.  What
       §18 proves is a **one-sided** reduction to the largest index `Q(m)`
       occurring in a feasible combination: `Q(m) = o(m\sqrt{\log m})` alone
       gives `h⁰_{\mathbb Z}(mK) = o(m²)`, while requirement (c) forces
       `Q(m) ≫ m\sqrt{\log m}`.  The item is restated in that form in §23, and
       the upper bound of §18 is conditional on a zero-free region, import
       (X23).]**
* **Unchanged:** items 1, 2, 4–15 of §9.1, and the label of §10.
* **[ADDED WITH PART III.]**  Items **(24)–(36)** continue this list and are
  stated in §23.4.  Three items above are settled by Part III: item **(20)**
  (satisfiability) is answered **negatively** for `ξ` — Theorem 19.25 shows the
  triple (a),(b′),(c) is unsatisfiable, so Theorem 12.3 keeps its label and
  loses its use; item **(22)** is closed with it, since no rule `Φ` on convex
  subsets can produce what does not exist; and item **(23)** survives only in
  the corrected one-sided form of the bracketed note above, restated as item
  (27).  Item **(18)** is **narrowed, not closed**, by §19bis: the pair-indexed
  candidate it points to cannot be a function of the Frobenius bidegree alone
  (Theorem 19bis.19), and what such a candidate must read instead is named in
  Corollary 19bis.23; the item stays `OPEN`.  Items (16), (17), (19) and (21)
  are unchanged.

**Remark 14.5a (`HEURISTIC`; where phase 136 should start — finding LF7 of
`R135_003`).**  Remark 13.6a's mechanism says that the integral sections of
§13.2 were sought in a **one-parameter** family: the translates
`τ_{\log q}(ΠK)`, indexed by a single Frobenius.  On a surface `C×C` the growth
`h⁰(nD) ∼ n²(D\cdot D)/2` comes from a **two-dimensional** lattice of sections,
and the deficit §13 finds — a logarithm where `m²` is wanted — is exactly the
deficit of one parameter against two.  The suggestion is therefore to index the
sections by **pairs**, in the Frobenius bi-grading `M(Frob_n) = (n^{1/2},
n^{−1/2})` of Paper 44 Theorem 3ter.6(iii): by the correspondences
`Frob_m ⋆ Frob_n^†` rather than by `Frob_n` alone.  The datum that such a count
would then see, and that no weighting by positive numbers can see (Remark
13.7), is the diagonal relation

    Frob_n ⋆ Frob_n^† = Δ^{(n)}                                    (14.2)

of Paper 44 Theorem 3ter.6(ii) — which fails for `Ξ_a`, where it reads
`(n^a+n^{−a})Δ^{(n)}` (Theorem 7.1(iii)).  **This is a direction, not a claim,
and it is not evidence for any sign.**  It is open item (18), and it is where
phase 136 should begin.

**Part II claims no sign, asserts no sign, and suggests no sign.**  Its
deliverable is a **reduction of unknown satisfiability**: *row D's target
follows from the existence of one function `h⁰` with three properties, on a
completion that is constructed here, with a duality that is constructed here;
no such function is constructed, none is known to exist, two natural
constructions are closed on every finite truncation, and no model-free proof
that one works can exist.*

---

## 15. External inputs added by Parts II and III

| tag | import | clause it serves | used at |
|---|---|---|---|
| **(X12)** | **Riemann's integral representation in Pólya's normalization**: `Ξ(τ) = 2∫_0^∞K(t)\cos(τt)dt` with `K` of (11.7); `K` real, **even**, and `K(t) > 0` for all real `t`.  Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath–Brown), §10.1, eq. (10.1.4) and the following two displays; G. Pólya, Acta Math. **48** (1926), 305–317 | `Φ_K = ξ`; evenness and positivity of the canonical class | Thm 11.7(i) |
| **(X13)** | **Jensen's formula / the zero-counting bound for entire functions of exponential type**: `n_f(r) = O(r)` for `f ≢ 0` of exponential type | the zero-counting half of Theorem 11.12 | Thm 11.12 |
| **(X14)** | **Riemann–von Mangoldt asymptotic** `N(T) = \frac{T}{2π}\log\frac{T}{2π} − \frac{T}{2π} + O(\log T)` (the asymptotic form of (E3d)) | the other half of Theorem 11.12: `ξ` has `\sim(r/π)\log r` zeros in `\|s−½\|≤r` | Thm 11.12 |
| **(X15)** | **Chebyshev's bound in Rosser–Schoenfeld's explicit form** `ψ_{Ch}(x) < 1.03883\,x` for all `x > 0`: Illinois J. Math. **6** (1962), 64–94, Theorem 12 | **[phase 135 round 2: no longer used by any proof.]**  Round 1 used it for the constant `C_F`; Theorem 11.14 is now proved on the spectral side and needs no Chebyshev bound.  Retained only in Remark 11.14a′, which nothing uses | Rem 11.14a′ |
| **(X18)** | **A positive proportion of the zeros of `ζ` are simple**: `N_s(T) ≥ (\tfrac25+o(1))N(T)`.  J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta-function are on the critical line*, J. reine angew. Math. **399** (1989), 1–26; N. Levinson, *More than one third of the zeros of Riemann's zeta-function are on `σ = ½`*, Advances in Math. **13** (1974), 383–436, would also serve | **[NEW, phase 135 round 2, finding M3 of `R135_002`.]**  The count of **distinct** zeros of `ξ` in `\|s−½\| ≤ r`, which is what Theorem 11.10(c) supplies zeros of `Φ_N` at.  (X14) counts with multiplicity and does **not** give this | Thm 11.12 |
| **(X16)** | **Hardy's theorem** (1914): `ζ` has infinitely many zeros on `\mathrm{Re}\,s = ½` | that `Ξ_a` has zeros off the critical line, **unconditionally** | Thm 12.4 |
| **(X17)** | **Connes–Consani**, *Riemann–Roch for `\overline{\mathrm{Spec}\,\mathbb Z}`*, arXiv:2205.01391v2: `\dim_{\mathbb S}\|H\mathbb Z\|_n = \lceil\log(2n+1)/\log3\rceil` (minimal generating set with coefficients in `\{-1,0,1\}`); `\dim_{\mathbb S}H⁰(D) = \lceil(\deg D+\log2)/\log3\rceil − \mathbf 1_L`; Serre duality `H⁰(K−D) ≅ \underline{\mathrm{Hom}}(H¹(D),U(1)_{1/4})` with `K = −2\{2\}`, `\deg K = −2\log2` | the `\log`-scale type of an integral dimension (Definition 13.4) and the first row of Finding 13.8 | §13.2, Finding 13.8 |


**Added by Part III (§§17–23).**  The tags below continue the list above;
`(X19)` is entered here for the first time although it is used from §12 on, by
the record note at Theorem 12.3.

| tag | import | clause it serves | used at |
|---|---|---|---|
| **(X19)** | **The first zero, verified**: `ρ_1 = ½ + iγ_1` with `γ_1 = 14.134725141734693790…` is a zero of `ξ` **on the critical line** and is **simple**, and `ξ` has no zero `ρ ≠ ρ_1,\barρ_1` with `|\mathrm{Im}\,ρ| ≤ 21`.  J. B. Rosser, J. M. Yohe, L. Schoenfeld, *Rigorous computation and the zeros of the Riemann zeta-function*, IFIP Congress 1968, 70–76; D. J. Platt and T. S. Trudgian, *The Riemann hypothesis is true up to `3·10^{12}`*, Bull. LMS **53** (2021), 792–797 (Turing's method; the verification establishes that the zeros in the checked range are simple and on the line).  **New to this paper as an import of record; Platt–Trudgian is already cited elsewhere in the corpus.**  Of the same evidential type as (X15), (X16), (X18); a cheaper substitute would be `ξ'(ρ_1) ≠ 0` plus an argument-principle count on `|\mathrm{Im}\,s| ≤ 21`, both certifiable by rigorous interval arithmetic | the simplicity and isolation of `ρ_1`, on which the exact constant `C_{F_0} ≤ Gs_1` and the value `W_{F_0} = 2G²` depend | Lemma 19.20(iv),(v), Thm 19.22, Thm 19.23, Thm 19.25, Lemma 19.25a, Cor 19.25b, Thm 19.30; load-bearing per Remark 19.27.  **[phase 156: Lemma 19.20(iv)'s per-interval count for `21 ≤ T ≲ 2×10^4` needs the verified zero list on that range or an explicit Trudgian count — flagged gap, see the note at Lemma 19.20(iv)]** |
| **(X20)** | **Landau's theorem for Laplace transforms and Dirichlet series**: a Laplace integral `∫_0^∞f(T)e^{−zT}dT` with `f ≥ 0`, or a Dirichlet series with nonnegative coefficients, whose abscissa of convergence `σ_c` is finite, has a **singularity at the real point `z = σ_c`** of its analytic continuation.  D. V. Widder, *The Laplace Transform*, Princeton Univ. Press (1941), Theorem II.5b; E. Landau, *Handbuch der Lehre von der Verteilung der Primzahlen*, §8 (the Dirichlet-series form) | the passage from `W(h_T) ≥ 0` for all `T > 0` to the absence of a real singularity other than `z = 0`, hence `σ_c = 0`, hence analyticity of `G` on `\mathrm{Re}\,z > 0` | Thm 17.14 (and Rem. 17.14a, the same argument for `Ξ_a`) |
| **(X20a)** | **The prime-number theorem with the Vinogradov–Korobov remainder**: `ψ_{Ch}(u) = u + O\big(u\exp(−c(\log u)^{3/5}(\log\log u)^{−1/5})\big)` for an absolute `c > 0`.  I. M. Vinogradov (1958); N. M. Korobov (1958); see A. Ivić, *The Riemann Zeta-Function*, Ch. 12, or H. L. Montgomery–R. C. Vaughan, *Multiplicative Number Theory I*, §6.3 | the best unconditional size of `\mathcal E(u)` against which `R(T)` is estimated, and the admissibility profile of the one-signed perturbation `η` | Thm 17.19, Rem. 17.20 |
| **(X21)** | **Davenport–Heilbronn**: if `h(−D) > 1` then the Epstein zeta function `Z_Q` of a form of discriminant `−D` has **infinitely many zeros in the half-plane `Re s > 1`**.  H. Davenport and H. Heilbronn, *On the zeros of certain Dirichlet series* I, II, J. London Math. Soc. **11** (1936), 181–185 and 307–312.  (Voronin's zeros in `½ < Re s < 1`, 1976, would **not** serve: see Remark 18.10a) | the existence of a real singularity of `G_Q` strictly right of `θ_R`, and the failure of A7 | Lem 18.4, Thm 18.10, Thm 18.12 |
| **(X22)** | **Montgomery–Vaughan mean value theorem** for Dirichlet polynomials: `∫_0^{T}|Σ_qb_qq^{−iτ}|²dτ = Σ_q|b_q|²(T + O(q))`.  H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974), 73–82 | the diagonal lower bound converting a pointwise majorant for `A(1+iτ)` into a bound on `Σ_q|a_qΛ(q)|²` | Thm 18.29, Rem 18.29a |
| **(X23)** | **The quantitative zero-free region for `ζ` on `Re s = 1`**, in the form `|ζ(1+iτ)|^{−1} ≪ \log^{7}(2+|τ|)` (any polynomial-in-`\log` bound serves).  Landau; Vinogradov; Titchmarsh, *The Theory of the Riemann Zeta-Function*, §3.11 and §6.19.  A quantitative strengthening of the qualitative (E2), already listed in §1.13 | the majorant `|ξ(1+iτ)|^{−1} ≤ Ce^{π\|τ\|/4}(1+\|τ\|)^{C}` on the one line where the degree ceiling is available | Thm 18.29 |
| **(X24)** | **The real-zero input for Epstein and Dedekind zeta functions**: a real **primitive odd** character has no real zero of `L(σ,χ)` in `(0,1)` (Landau; Davenport, *Multiplicative Number Theory*, §14); and for a real **even** character — equivalently for `ζ_K` with `K` real quadratic — no unconditional exclusion of a real zero in `(0,1)` is known (the Landau–Siegel zero) | A9 for `ξ_K`, `K` imaginary quadratic (proved) and `K` real quadratic (`OPEN`); the real-zero clause of the packet form of the Landau step | Thm 18.14, Cor 18.17, Thm 18.18(v), Rem 18.20a |
| **(X25)** | **Artin's holomorphy conjecture**: for `L/K` Galois and `χ ≠ 1` irreducible, `Λ(s,χ,L/K)` is entire.  E. Artin, Abh. Math. Sem. Hamburg **8** (1930), 292–306; Aramata–Brauer gives only that `ζ_L/ζ_K` is entire, which is a statement about the product, not the factors | the conditional half of base change: the zero multiset of `ξ_L` is the disjoint union of the factors' multisets | Thm 18.20 (general case only) |
| **(X25a)** | **Classical analytic data for Dedekind zeta and Artin `L`-functions**: Hecke's continuation and functional equation `Λ_K(s) = Λ_K(1−s)` with simple poles exactly at `s = 0,1`; the class-number formula `Res_{s=1}Λ_K = 2^{r_1}h_KR_K/w_K`; the Artin factorization `ζ_L = ζ_K∏_{χ≠1}L(\cdot,χ)^{χ(1)}` with the conductor–discriminant formula, so that the completed functions factor exactly; the Artin functional equation `Λ(s,χ) = W(χ)Λ(1−s,\barχ)` with `\|W(χ)\| = 1`, `W(χ)W(\barχ) = 1`; and the Phragmén–Lindelöf/Stirling growth bound (18.8) on vertical strips.  Hecke; Artin; Brauer; Neukirch, *Algebraic Number Theory*, VII §§10–12; Landau, *Einführung …*, §§28–29 | the field-uniform frame: poles, residue, the contour-shift construction of `K_K`, and the exact factorization used by base change | Thm 18.18, Lem 18.19, Thm 18.20 |
| **(X25b)** | **Heilbronn**: `h(−D) → ∞` as `D → ∞`; in particular `h(−4k) > 1` for all large `k`.  H. Heilbronn, Quart. J. Math. **5** (1934), 150–160 | that the family `Q_k = x²+ky²` of Theorem 18.5, which carries real zeros in `(0,1)`, meets the hypothesis `h(−D) > 1` of (X21) infinitely often | Thm 18.5 |
| **(X26)** | **Classical surface theory**: Riemann–Roch with Serre duality, `h⁰(D) + h⁰(K_S−D) ≥ χ(𝒪_S) + ½D·(D−K_S)` (Hartshorne, *Algebraic Geometry*, GTM **52**, Ch. V, Thm 1.6); *`D² > 0`, `D·H > 0` ⟹ `nD` effective for `n ≫ 0`, i.e. `D` big* (Hartshorne Ch. V, 1.8; Lazarsfeld, *Positivity in Algebraic Geometry I*, Ergebnisse **48**, Springer 2004, §2.2); Hodge index (Hartshorne Ch. V, Thm 1.9, already pinned by Remark 12.3a) | the geometric side of the diagnosis: which half of surface theory the arithmetic frame transports and which half it fails, with the deficit `s(γ,θ) < 1` | Restatement 19.29(i),(ii),(iii) |
| **(X27)** | **Weil's Riemann hypothesis for curves over finite fields, with the structure of `NS(E×E)` and the degree form on endomorphisms.**  For a smooth projective geometrically irreducible `C/F_q`: rationality and the functional equation of `Z_C(T)`, `N_m = q^m+1−Σ_iα_i^m`, `∏α_i = q^g`, conjugation- and `α ↦ q/α`-stability, and `|α_i| = √q`; the Lefschetz count `Γ_{q^m}·Δ = \#\mathrm{Fix}(F^m) = N_m` with transverse fixed points, `Γ_{q^m}·Γ_{q^n} = q^nN_{m−n}` and `Γ_{q^m}^{\,t}·Γ_{q^n} = N_{m+n}` for `m ≥ n ≥ 0`; Tate's theorem `\mathrm{rk}\,NS(A×B) = \mathrm{rk}\,NS(A)+\mathrm{rk}\,NS(B)+\mathrm{rk}\,\mathrm{Hom}(A,B)` with `\mathrm{End}(E)` an order in an imaginary quadratic field for ordinary `E`, so that `NS(E×E)_R` is spanned by `F_1,F_2` and the graphs `Γ_α`, `α ∈ Z[π]`, with `Γ_α·F_1 = 1`, `Γ_α·F_2 = \deg α`, `Γ_α·Γ_β = \deg(α−β)`; and, on an abelian variety, algebraic equivalence of translates (theorem of the square), hence *effective `⟹` nef*.  A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*, Hermann 1948; J.-P. Serre, *Zeta and L-functions*, in *Arithmetical Algebraic Geometry*, Harper & Row 1965, §§1–2; J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. **2** (1966), 134–144, Thm 2; D. Mumford, *Abelian Varieties*, Ch. II §6; Hindry–Silverman, *Diophantine Geometry*, App. A.4; Stichtenoth, *Algebraic Function Fields and Codes*, 2nd ed., §§V.1–V.2 | `\mathrm{Re}\,ρ_i = ½` in the model; the Toeplitz Gram `κ(a−b)`; `V_C = NS(E×E)_R` for the curve of record; the nef upper bound of Theorem 21.17(iii); the norm form (21.14) | Lem. 21.2, Thm 21.5, Thm 21.7, Thm 21.8, Thm 21.17(iii), Prop. 21.22, Rem. 21.23 |
| **(X28)** | **Intersection theory, Riemann–Roch, Serre duality, the Hodge index theorem and the bigness criterion on a smooth projective surface.**  On `S = C×C`: the numbers (21.1), including `Δ² = 2−2g`, `Γ_f² = d(2−2g)`, `K_{C×C} = (2g−2)(F_1+F_2)` and `χ(𝒪_S) = χ(𝒪_C)^2 = (1−g)^2` (Künneth); Riemann–Roch `χ(𝒪(D)) = ½D·(D−K_S)+χ(𝒪_S)`; Serre duality `h^2(D) = h^0(K_S−D)`; the Hodge index theorem (`H` ample, `D·H = 0`, `D ≢ 0 ⟹ D^2 < 0`); and bigness: `D^2 > 0`, `D·H > 0 ⟹ nD` effective for `n ≫ 0`.  R. Hartshorne, *Algebraic Geometry*, GTM 52, §V.1 (V.1.1, V.1.5, V.1.6, V.1.8, V.1.9) with Exercises V.1.9, V.1.10, and III.7.6 for duality; R. Lazarsfeld, *Positivity in Algebraic Geometry I*, Ergebnisse **48**, §§1.5, 2.2 | the intersection numbers (21.1) underlying the dictionary; that `h⁰_C` satisfies (a),(b′),(c); `\overline{\mathrm{Pos}} ⊆ \overline{\mathrm{Eff}}`; the model column of the (P145′) supply table | (21.1), Thm 21.7, Thm 21.16, Thm 21.17(iii), §21.6, §21.8 |
| **(X29)** | **Toeplitz operators with continuous symbol**: for real `f ∈ C(T)` with Fourier coefficients `\hat f(k)`, the Toeplitz operator `T(f)` on `ℓ^2(N)` (and the Laurent operator on `ℓ^2(Z)`) is bounded self-adjoint with `\inf\mathrm{spec}\,T(f) = \min f` and `\sup\mathrm{spec}\,T(f) = \max f`; in particular `T(f) ⪰ 0 ⟺ f ≥ 0`.  U. Grenander and G. Szegő, *Toeplitz Forms and Their Applications*, 2nd ed., Chelsea 1984, Ch. 5; A. Böttcher and B. Silbermann, *Analysis of Toeplitz Operators*, 2nd ed., Springer 2006, §1.2 and Prop. 2.14.  Applied to the Kac–Murdock–Szegő symbol `f_ρ(θ) = (1−ρ^2)/(1−2ρ\cosθ+ρ^2)`, and to the sum of two such Poisson kernels for the falsifier | the trichotomy (22.15) and its thresholds `τ_±(p)`, and the `Ξ_a` thresholds of Remark 22.16a | Thm 22.15, Rem 22.16a |
| **(X29a)** | **The affine anti-equivalence**: `\mathrm{Spec}` is an anti-equivalence from commutative rings to affine schemes, so `\mathrm{Hom}_{\mathrm{Sch}}(\mathrm{Spec}\,A,\mathrm{Spec}\,B) = \mathrm{Hom}_{\mathrm{Ring}}(B,A)`, and more generally `\mathrm{Hom}_{\mathrm{Sch}}(X,\mathrm{Spec}\,B) = \mathrm{Hom}_{\mathrm{Ring}}(B,Γ(X,𝒪_X))`.  R. Hartshorne, *Algebraic Geometry*, Springer 1977, Prop. II.2.3 and Exercise II.2.4; A. Grothendieck and J. Dieudonné, *EGA I*, §1.6 | passing from "the only ring endomorphism of `Z` is the identity" to the scheme statement and to terminality of `\mathrm{Spec}\,Z` | Thm 22.17(ii) |
| **(X30)** | **Hadamard's constant for `ξ` (Davenport's identity)**: `Σ_ρ\mathrm{Re}(1/ρ) = 1 + ½γ_E − ½\log 4π = 0.0230957089…`, the sum over the nontrivial zeros with multiplicity, a series of positive terms `β/\|ρ\|²`; unconditional (it is `−B` in the Hadamard product of `ξ`).  H. Davenport, *Multiplicative Number Theory*, 3rd ed. (rev. H. L. Montgomery), GTM **74**, Springer 2000, Ch. 12, eqs. (10)–(11).  `CLASSICAL`.  **[NEW, phase 156 (`R156_002` Lemma 3.2, cleared by `R156_003` D4).]**  Serves only the explicit constants; the existence statements need only (E3d) | the explicit bound `S_2 = Σ_ρ\|ρ−½\|^{−2} ≤ 0.0465`, hence the explicit `R_0(ϑ)`, `s_{F_R} < 0.998464`, `d_0^{(R)} < 325.78` and `s_{F_R^♭} ≤ 0.998469` | Lemma 19.25a(ii),(iv),(v) |
| **(X31)** | **A Beurling system with a power-saving integer law and zeros tending to `\mathrm{Re}\,s = 1`** — the reduced statement (H-DMV′) of §27.4: there are `θ < 1` and a discrete Beurling system `𝒫` with `N_𝒫(x) = ρx + O(x^θ)`, `ρ > 0`, whose zeta function has zeros `β_n + iγ_n` with `β_n → 1`.  For the system of H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, *Beurling primes with large oscillation*, Math. Ann. **334** (2006), 1–36, as stated in: F. Broucke, G. Debruyne, J. Vindas, Adv. Math. **370** (2020), §1 (arXiv 2004.11501); F. Broucke, arXiv 2409.10051, §6.2; F. Broucke, G. Debruyne, arXiv 2211.08716, §1.  Independently, for the second system of W.-B. Zhang, Math. Ann. **337** (2007), 671–704 (author's abstract, zbMATH Open Zbl 1121.11061), combined with Sz. Gy. Révész, arXiv 2207.00665, Theorem 5.  Local copies: `00-references/beurling-dmv/` (`2004.11501.txt`, `2409.10051.txt`, `2211.08716.txt`, `2207.00665.txt`, `zbMATH-records.txt`).  `CITED (secondary source)`: **the primary texts (DMV 2006, Zhang 2007) have not been read**; the check against them is open item (41), residual `OPEN`.  **[NEW, phase 157 (`R157_001` as amended, cleared by `R157_003` §5).]**  Everything else (H-DMV) needs is proved in §27.4 from (H-DMV′) or is `CLASSICAL` (Landau's prime number theorem for BE5, Landau's theorem (X20) for BE8) | (H-DMV), hence the one bad model in the soundness argument of T3 | Hyp. (H-DMV), Rem 27.16, Prop 27.17(3) |
| **(X32)** | **Berkovich spaces over `Z` and adelic potential theory on the line.**  (i) The Berkovich line `A^{1,an}_Z` (multiplicative seminorms on `Z[T]` bounded on `Z` by `\|·\|_∞`), `π : A^{1,an}_Z → M(Z)`, with archimedean fibres `C^n/\mathrm{conj}` for `A^{n,an}_Z`, `p`-adic fibres Berkovich spaces over `Q_p` (rescaled), branches meeting at the trivial norm, and the topology of `M(Z)` at the root strictly coarser than the tree topology: J. Poineau, *La droite de Berkovich sur Z*, Astérisque **334** (2010), arXiv 0809.2880, introduction.  (ii) Fibre products in the category of `A`-analytic spaces: T. Lemanissier, J. Poineau, *Espaces de Berkovich globaux*, arXiv 2010.08858, Thm 4.3.8.  (iii) Local Arakelov–Green energies and their positivity on mass-zero measures: C. Favre, J. Rivera-Letelier, Math. Ann. **335** (2006), 311–361, arXiv math/0407471, eq. (7) and Prop 2.6, eq. (9) (archimedean), Lemma 4.4, eq. (22) (the Hsia kernel) and Prop 4.5, eq. (23) (non-archimedean), eq. (3) and Def 1.2, eq. (4) (the height, with the product formula).  (iv) For the survey claim only: J. Poineau, *Dynamique analytique sur Z. I*, arXiv 2201.08480 (Thm A, Prop C, Cor D, Defs 3.16–3.17: fibrewise pairings only); J. S. Morrow, arXiv 2507.10410 (Defs 3.1.2, 3.1.3, 3.3.1, §7.1, Def 8.2.1: fibrewise Monge–Ampère measures, a hand-chosen base measure, no energy); A. Chambert-Loir, arXiv 1001.2517, §3 and §3.4.1 (the one non-local term, `−2ĥ_{NT}`, vanishes in genus 0).  Read as text in phase 157 (`R157_006` §§0, 2.1, 3), not stored in the repository.  Baker–Rumely, Thuillier, Rumely LNM 1378 are cited from standard knowledge; Chinburg–Rumely, *The capacity pairing*, J. reine angew. Math. **434** (1993), is **unread**.  `CITED`.  **[NEW, phase 157 (`R157_005` as amended, cleared by `R157_006` §12).]** | the fibre description and the categorical fibre product in Lemma 28.1; the local positivity in case (2) of Theorem 28.3; the exhaustion of the literature by `𝔄⁺` (survey, `CITED`, one title unread) | §28.3a |
| **(X33)** | **The adèle class space, its nuclear `H¹`, and the Serre argument.**  (i) A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) **5** (1999), 29–106, arXiv math/9811068: the introduction (the global trace formula "is equivalent to the Riemann Hypothesis for all L-functions with Grössencharakter"); Thm 1 (on `L²_δ`, `δ > 1`, the spectrum of `D_χ` is the set of imaginary parts of the **critical** zeros, multiplicity capped by `n < (1+δ)/2`) and the remark after it (at a multiple zero `D` "has a non trivial Jordan form … compatible with the almost unitary condition … but not with skew symmetry"); Thm 4 (the S-local trace formula, proved); §VIII Thm 5 (the global trace formula ⟺ RH, proved in positive characteristic; for number fields stated by analogy, no proof); §VIII Remark d.  (ii) R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv math/0412277 (local copy `00-references/papers-nuevos/C/arXiv-math0412277v3`): Thm "Lap_range" (the Laplace-side description `𝓗_- ≅ 𝒪`, `Z𝓗_∩ ≅ I`, `D_-` = multiplication by `s`), Cor "Dminus_eigenvalues" (eigenvalues of `ᵗD_-` = zeros, algebraic multiplicity = order), the character identity (the explicit formula, unconditional, on nuclear spaces).  Meyer's *On a representation of the idele class group related to primes and zeros of `L`-functions*, Duke Math. J. **127** (2005), 519–595, is cited by CCM and **not read**.  (iii) A. Connes, C. Consani, M. Marcolli, *The Weil proof and the geometry of the adeles class space*, arXiv math/0703392: Thm 4.16 (all zeros contribute to `Tr(ϑ_m(f)\|H¹)` with their natural multiplicity), Rem 4.18 and (4.47) (the trace pairing), (6.9) (the Rosati involution `f^♯`), Thm 6.1, Prop 6.2, Cor 6.3 (RH for all Grössencharaktere ⟺ `⟨f,f^♯⟩ ≥ 0`), Prop 6.4, §7.1, Def 7.1, Prop 7.2 and (7.6)–(7.8) (Hodge index on the square).  (iv) E. Leichtnam, *On the analogy between `L`-functions and Atiyah–Bott–Lefschetz trace formulas for foliated spaces*, arXiv 1307.3851 (local copy `00-references/papers-nuevos/C/arXiv-1307.3851v1`): §2 eq. (6) (Serre's argument: a flow-conformal positive form forces `Re ρ = ½`, "an idea of Serre", formalized for foliations by Deninger–Singhof), axioms 5]–6], Comment 6 ("the first six Assumptions imply the Riemann hypothesis").  Read as text in phase 158 (the source lists heading `R158_003` and `R158_004`).  `CITED`.  **[NEW, phase 158 (`R158_002` as amended, cleared by `R158_004` §4; `R158_001` as amended, accepted by `R158_003`).]** | the object and the four statements of Remark 28.6; the OT-2 verdict on the Hilbert-space realisation | §28.3b |

---

## 16. Reproduction

```text
cd 03-research/phase-134-row-d-opening/scripts
python3 d134_gram.py  --model zeta --N 10 30 --eps 2.0 1.0 0.5 0.3 0.1 --check
python3 d134_gram.py  --model xi_a --a 0.35 --N 10 30 --eps 2.0 1.0 0.5 0.3 0.1
python3 d134_gram.py  --model xi_a --a 0.45 --N 10 30 --eps 1.0 0.5 0.2
python3 d134_sigma.py --model zeta --tmin 0.72 --tmax 2.2 --steps 8
python3 d134_sigma.py --model xi_a --a 0.35 --tmin 0.72 --tmax 1.9 --steps 8
```

`d134_sigma.py` imports `p124_lab.py` from
`03-research/phase-124-direct-first-contact/scripts` unchanged.  Numerics
illustrate and falsify; they prove nothing.

**Part II (phase 135).**

```text
cd 03-research/phase-135-row-d-canonical-class/scripts
python3 polya_class.py        --check          # mpmath, 25 digits
python3 canonical_pairings.py --check          # P1, P2, P3, P4
python3 canonical_pairings.py --check --fast   # same checks, coarser panels
python3 h0_candidate.py       --check          # H1, H2, H3
python3 h0_candidate.py       --check --fast   # same checks, smaller search box
```

Each exits `0` only if every printed check passes.  **`[phase 135 round 2,
R135_004`: all four runs above were executed and **all exit `0`**.  Timings on
the audit machine: `polya_class.py --check` 60 s; `canonical_pairings.py
--check` 28 s and `--fast` 10 s; `h0_candidate.py --check` 15 s and `--fast` 0.2 s.  Round
1's two failures — `canonical_pairings.py` failing at `P2` and exceeding 2400 s,
`h0_candidate.py` exceeding 1500 s at its defaults — are both repaired: see the
bracketed notes under Theorem 11.8 and Definition 13.4.  The two long scripts
were rewritten with fixed Gauss–Legendre panels and `float64` linear algebra
(`mpmath` is kept for `ξ`, `ψ` and the zeros), and both gained a `--fast`
mode.]**  `r135_common.py` carries the shared definitions (`K`, `ΠK`, `ξ`, the
archimedean and prime terms of (11.3)) in both an `mpmath` and a `float64`
layer.
Numerics illustrate and falsify; they prove nothing, and no number in Part II
is evidence for any sign.

---

# PART III — detecting cones, the method constraints, the frame defect, and the state of the sign

**Part III records §§17–23.  It proves no sign and claims none.  Its
statements carry their own hypotheses; the labels are those of (1.12),
together with `METHOD-CONSTRAINT` for the two theorems of §18, which are
statements about admissible *derivations* and not about `ζ`.  Cross-references
to Parts I–II are by theorem number, and the corrections of record entered in
Parts I–II with this Part are collected in §23 and in the bracketed notes at
the places they correct.**

## 17. Detecting cones and the intrinsic characterization of the primitive sector

*Provenance.  The statements and proofs of this section are taken from
`03-research/phase-138-row-d-detecting-cones/R138_001_ROUND1.md`
(items D.15.1–D.15.5, D.16.1–D.16.3, D.17.1–D.17.4), with the final labels and
the list of withdrawals fixed by `R138_005_CLOSING_DECISION.md`,
`R138_002_AUDIT.md` and `R138_004_CONFIRMATION.md` in that
file's own record.  The repository results cited without proof are
`03-research/phase-114-closing-the-four-rows/114_d_185_PNT_TATE_LOW_BLOCK_NOGO.md`,
`03-research/phase-72-feshbach-leakage-calculus/E72_49_BANDLIMITED_PNT_ENDPOINT_THEOREM.md`,
`03-research/phase-113-the-trace-on-schwartz-data/113_08_THE_TWO_RULINGS_AND_THE_INDEX_ENGINE.md`
and `03-research/phase-118-the-exact-threshold-inequality/W4_CERTIFIED_RANGE.md`.*

Throughout, `D^W` is Definition 11.1, `Φ_F(s) = ∫F(t)e^{(s−½)t}dt`, and

    I_∞(F,G) = Φ_F(0)Φ_G(1) + Φ_F(1)Φ_G(0) − Σ_ρ Φ_F(ρ)Φ_G(1−ρ)

is Theorem 11.5, the zero sum being absolutely convergent by (11.2) and (E3d).

### 17.1 The two data of a Weil class

**Definition 17.1 (ruling datum, zero datum, polar block).**  For `F ∈ D^W`,

    M(F) := (\deg⁺F, \deg⁻F) := (Φ_F(1), Φ_F(0)) ∈ R² ,
    \deg F := \deg⁺F + \deg⁻F = ∫F·2\cosh(t/2)\,dt ,
    μ(F)   := \deg⁺F − \deg⁻F = ∫F·2\sinh(t/2)\,dt ,

`Z(F) := (Φ_F(ρ))_{ρ ∈ Z(ξ)} ∈ ℓ¹(Z(ξ))`, and

    B_pol(F,G) := Φ_F(0)Φ_G(1) + Φ_F(1)Φ_G(0) = β_T(M(F),M(G)) ,
    β_T = \begin{pmatrix}0&1\\1&0\end{pmatrix} ,

so that `I_∞(F,G) = B_pol(F,G) − Σ_ρ Φ_F(ρ)Φ_G(1−ρ)`.  Write
`P^W := \ker M = \{\deg⁺F = \deg⁻F = 0\}` for the primitive sector,
`E := \{F ∈ D^W : F ≥ 0\}` for the effective cone (Theorem 11.13) and
`A := \{H : I_∞(E,H) > 0 \text{ for every effective } E ≢ 0\}` for the ample
cone (Theorem 11.14(iii)).  `M(F)` is the convention of Proposition 14.1 and of
Theorem 11.8(iii).

**Definition 17.2 (detecting cone).**  A convex cone `C ⊆ D^W` is **detecting**
if for every zero `ρ_0` of `ξ` with `\mathrm{Re}\,ρ_0 ≠ ½` there is `F ∈ C` with
`I_∞(F,F) > ½(\deg F)²`.

**Remark 17.2a.**  `I_∞(−F,−F) = I_∞(F,F)` and `(\deg(−F))² = (\deg F)²`, so
failure of the Hodge-index inequality at `F` and at `−F` are the same
statement; a set and the symmetric set it generates detect together.

### 17.2 The splitting `D^W = Λ ⊥ P^W`

**Lemma 17.3 (`M` is surjective; `PROVED`).**  For `a ≠ 0`, `M(K) = (½,½)` and
`M(τ_aK) = ½(e^{a/2}, e^{−a/2})` are linearly independent; hence
`M : D^W → R²` is onto and `P^W = \ker M` has codimension `2`.

*Proof.*  `M(τ_aK) = ½(e^{a/2},e^{−a/2})` is Theorem 11.8(iii), and

    \det\begin{pmatrix}½&½\\½e^{a/2}&½e^{−a/2}\end{pmatrix}
      = ¼(e^{−a/2} − e^{a/2}) ≠ 0 .   ∎

**Definition 17.4 (the odd canonical class).**  Fix `a > 0` and put

    K_odd := (2\sinh(a/2))^{−1}\,(τ_aK − τ_{−a}K) .

By Lemma 11.2(i) and Theorem 11.7(ii), `K_odd ∈ D^W`; it is an **odd** function
(`K` being even), and by `Φ_{τ_{\pm a}K}(s) = e^{\pm(s−½)a}ξ(s)`
(Lemma 11.2(iv)),

    Φ_{K_odd}(s) = \frac{\sinh((s−½)a)}{\sinh(a/2)}\,ξ(s) ,

so `Φ_{K_odd}` vanishes at every zero of `ξ`, and
`M(K_odd) = (½,−½)`, `\deg K_odd = 0`, `μ(K_odd) = 1`.

**Theorem 17.5 (the intrinsic description of the primitive sector; `PROVED`).**
Put `Λ := \mathrm{span}_R(K, K_odd) ⊂ D^W`.  Then:

 (i) `P^W = \ker(\deg⁺) ∩ \ker(\deg⁻)` is the **radical of `B_pol`**, and in the
     basis `(\deg⁻,\deg⁺)` of `D^W/P^W ≅ R²` the form `B_pol` is the hyperbolic
     plane `\begin{pmatrix}0&1\\1&0\end{pmatrix}`, `B_pol(F,F) = 2\deg⁺F·\deg⁻F`;
 (ii) `P^W = K^{⊥_{I_∞}} ∩ K_odd^{⊥_{I_∞}}`; more generally
     `P^W = X^⊥ ∩ Y^⊥` for any `X,Y ∈ D^W` whose `Φ` vanish at every zero of `ξ`
     and whose ruling data are linearly independent;
 (iii) `Λ ∩ P^W = 0`, `D^W = Λ ⊕ P^W`, and the sum is `I_∞`-**orthogonal**;
 (iv) `I_∞|_Λ = B_pol|_Λ` has Gram matrix `\mathrm{diag}(½,−½)` in the basis
     `(K,K_odd)`: a **hyperbolic plane of signature `(1,1)`**, with `K` a
     positive vector and `K_odd` spanning `K^⊥ ∩ Λ`;
 (v) `I_∞|_{P^W}(F,F) = −Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`, the pure zero form;
 (vi) `K^{⊥_{I_∞}} = \{\deg F = 0\} = P^W ⊥ R·K_odd`, and `I_∞ ≤ 0` on `K^⊥`
     **iff** `I_∞ ≤ 0` on `P^W`.

*Proof.*  (i) If `B_pol(F,G) = 0` for every `G`, then letting `M(G)` run over a
basis of `R²` (Lemma 17.3) forces `Φ_F(0) = Φ_F(1) = 0`; the converse is
immediate.  The matrix statement is Definition 17.1.

(ii) `I_∞(F,K) = ½\deg F` by Theorem 11.8(i).  Since `Φ_{K_odd}` vanishes on
`Z(ξ)`, the zero sum drops out and

    I_∞(F,K_odd) = B_pol(F,K_odd)
      = Φ_F(0)Φ_{K_odd}(1) + Φ_F(1)Φ_{K_odd}(0)
      = ½Φ_F(0) − ½Φ_F(1) = −½μ(F) .

So `F ⊥ K` and `F ⊥ K_odd` iff `\deg F = μ(F) = 0` iff `F ∈ P^W`.  The general
form is the same computation with `M(X),M(Y)` a basis of `R²`.

(iii) `M|_Λ` is an isomorphism onto `R²` by `M(K) = (½,½)`, `M(K_odd) = (½,−½)`,
and `P^W = \ker M`; orthogonality is (ii).

(iv) `Φ_K` and `Φ_{K_odd}` vanish on `Z(ξ)`, so `I_∞ = B_pol` on `Λ`:
`I_∞(K,K) = 2·½·½ = ½`, `I_∞(K_odd,K_odd) = 2·½·(−½) = −½`,
`I_∞(K,K_odd) = ½·½ + ½·(−½) = 0`.

(v) is Definition 17.1 with `M(F) = 0`.  (vi) `I_∞(F,K) = ½\deg F`, and on
`P^W ⊥ R K_odd` the form is the orthogonal direct sum of `I_∞|_{P^W}` with the
negative form `⟨−½⟩`.  ∎  `PROVED`

**Remark 17.6 (separation of data).**  `I_∞` on `D^W` is the orthogonal direct
sum of a hyperbolic plane and the zero form, and the two summands read disjoint
data: `Λ` reads only `M(F) ∈ R²`, `P^W` reads only `Z(F) ∈ ℓ¹(Z(ξ))`.  The
radical `𝓝_∞` of Theorem 11.11 is exactly the common kernel
`\ker M ∩ \ker Z`, and `D^W/𝓝_∞ ↪ R² ⊕ ℓ¹(Z(ξ))` with `I_∞ = β_T ⊕ (−\,·)`.
The ingredients — the two rulings, their isotropy, the hyperbolic form
`\begin{pmatrix}0&1\\1&0\end{pmatrix}` — are those of `113_08` and of §14.1; what
Theorem 17.5 adds is the odd direction: on even tests the polar form is the
rank-one positive form `2λ⊗λ`, while on all of `D^W` it has signature `(1,1)`,
with the explicit odd companion `K_odd` **inside `D^W`**, so that the splitting
is a splitting of classes and not only of ruling data.

**Remark 17.6a (the falsifier).**  Everything in Theorem 17.5 holds verbatim for
any admissible `Z` in the sense of Proposition 12.6, with `\dim Λ = \#P` and
`B_pol^{(Z)}(F,G) = Σ_{p∈P}Φ_F(p)Φ_G(1−p)`.  For `Ξ_a`, `\#P = 4` and the polar
block is **two** hyperbolic planes, of signature `(2,2)`; see §17.6.
Theorem 17.5 carries no sign.

### 17.3 The polar block satisfies the Hodge-index inequality identically

**Theorem 17.7 (the polar slack; `PROVED`).**  For every `F ∈ D^W`:

 (i) `½(\deg F)² − B_pol(F,F) = ½(\deg⁺F − \deg⁻F)² = ½μ(F)²
     = ½(∫F·2\sinh(t/2)dt)² ≥ 0`;
 (ii) the **polar block alone satisfies the Hodge-index inequality**, with slack
     exactly `½μ(F)²`, with equality precisely on the classes with
     `\deg⁺F = \deg⁻F`;
 (iii) the Hodge-index inequality holds at `F` if and only if
     `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) ≥ −½μ(F)²`;
 (iv) on even `F`, and on `F ∈ P^W`, (iii) is Weil positivity verbatim; on odd
     `F` (where `\deg F = 0`, `μ(F) = 2\deg⁺F`) it is the strictly weaker
     `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) ≥ −2(\deg⁺F)²`;
 (v) with `h := F⋆F^∨` and the explicit formula (11.3),

      Hodge index at `F`  ⟺  PRIME(h) ≤ ARCH(h) + ½(\deg F)² ,            (17.1)

     where `PRIME(h) = Σ_{n≥2}Λ(n)n^{−1/2}[h(\log n)+h(−\log n)]` and
     `ARCH(h) = (1/2π)∫ĥ(τ)[\mathrm{Re}\,ψ(¼+iτ/2) − \log π]\,dτ`.  **No zero
     appears in (17.1).**

*Proof.*  (i) `½(x+y)² − 2xy = ½(x−y)²` with `x = \deg⁺F`, `y = \deg⁻F`; the
integral forms are Lemma 11.2(iii).  (ii) is (i).  (iii) is Definition 17.1
combined with (i).  (iv) is substitution.  (v) By Lemma 11.4a and (11.4),
`I_∞(F,F) = ⟨h, W_{fin}+ω_∞⟩ = PRIME(h) − ARCH(h)`, and the Hodge-index
inequality is `I_∞(F,F) ≤ ½(\deg F)²`.  ∎  `PROVED`

**Corollary 17.7a (`PROVED`).**  No inequality on `D^W` that is a function of the
ruling datum `M(F)` alone can separate `ξ` from a function with off-line zeros:
every such inequality is implied by, or is independent of, an identity already
satisfied by `B_pol`.  Precisely, by Theorem 17.7(ii) the Hodge-index inequality
restricted to the polar block holds for every `F ∈ D^W` whatever the location of
the zeros, so its validity carries no information about `Z(ξ)`; by
Theorem 17.7(iii) the entire content sits in the zero sum.  ∎  `PROVED`

### 17.4 The Lorentzian criterion and the cone it can be run on

**Theorem 17.8 (Lorentzian criterion; `PROVED`).**  Let `V` be a real vector
space, `Q` a symmetric bilinear form on `V`, and `K ∈ V` with `Q(K,K) > 0`;
write `Q(F) := Q(F,F)`.  The following are equivalent.

 (a) `Q(F₀) ≤ 0` for every `F₀ ∈ K^⊥ := \{F : Q(F,K) = 0\}`;
 (b) `Q(F,K)² ≥ Q(F)Q(K)` for every `F ∈ V`;
 (c) there is a subset `C ⊆ V` with `K ∈ C` which is **absorbing at `K`** (for
     every `F ∈ V` there is `ε > 0` with `K + εF ∈ C`) such that
     `Q(F,K)² ≥ Q(F)Q(K)` for every `F ∈ C`.

Moreover, under (a):

 (d) `Q(F,G)² ≥ Q(F)Q(G)` for every pair with `Q(F) ≥ 0` **or** `Q(G) ≥ 0`;
 (e) (d) is sharp: if `\dim V ≥ 3`, (a) does **not** imply
     `Q(F,G)² ≥ Q(F)Q(G)` for all `F,G` in a convex cone with `K` in its
     interior.

*Proof.*  (a)⇔(b).  For `F ∈ V` put `λ := Q(F,K)/Q(K)` and
`F₀ := F − λK ∈ K^⊥`.  Then `Q(F) = λ²Q(K) + Q(F₀)`, so

    Q(F,K)² − Q(F)Q(K) = λ²Q(K)² − λ²Q(K)² − Q(F₀)Q(K) = −Q(K)Q(F₀) .

Since `Q(K) > 0`, (b) at `F` is exactly `Q(F₀) ≤ 0`; and every `F₀ ∈ K^⊥`
arises, by taking `F = F₀`.

(b)⇒(c) is trivial, with `C = V`.  (c)⇒(b): fix `F ∈ V` and `ε > 0` with
`K + εF ∈ C`, and apply (c) to `K + εF`:

    (Q(K) + εQ(F,K))² ≥ (Q(K) + 2εQ(F,K) + ε²Q(F))·Q(K) .

The terms of order `ε⁰` and `ε¹` cancel on both sides, leaving
`ε²Q(F,K)² ≥ ε²Q(F)Q(K)`, i.e. (b) at `F`.

(d)  Let `W := \mathrm{span}(F,G)`.  If `F,G` are dependent both sides agree.
Otherwise `Q|_W` cannot be positive definite: `W ∩ K^⊥` has dimension `≥ 1` and
`Q ≤ 0` there by (a).  If `Q(F) > 0` then `Q|_W` has a positive vector, hence
exactly one positive eigenvalue, hence `\det \mathrm{Gram}(F,G) ≤ 0`, i.e.
`Q(F)Q(G) − Q(F,G)² ≤ 0`.  If `Q(F) = 0` then
`\det\mathrm{Gram}(F,G) = −Q(F,G)² ≤ 0` directly.  The roles of `F` and `G` are
symmetric.

(e)  Take `V = R³`, `Q = \mathrm{diag}(1,−1,−1)`, `K = e₀`, so that (a) holds,
and `C = V`, a convex cone with `K` in its interior; then `F = e₁`, `G = e₂`
give `Q(F,G)² = 0 < 1 = Q(F)Q(G)`.  ∎  `PROVED`

**Theorem 17.9 (the effective cone is not the cone for Theorem 17.8; `PROVED`).**
Let `‖E‖₁ := ∫|E(t)|·2\cosh(t/2)\,dt`, a norm on `D^W` in which `I_∞(·,F)` is
continuous for each fixed `F` (Theorem 11.14(i),(ii)).  Then:

 (i) `E` is absorbing at **no** point of `D^W`; in particular it is not
     absorbing at `K`, and it has empty interior in every vector topology on
     `D^W`;
 (ii) `E` has empty `‖·‖₁`-interior;
 (iii) consequently clause (c) of Theorem 17.8 cannot be run on `E`.

*Proof.*  (i) Let `F₀ ∈ E`.  By (11.1) there are `C, ε > 0` with
`F₀(t) ≤ Ce^{−(1+ε)|t|}`.  Since `D^W` only demands decay `e^{−(1+ε')|t|}` for
some `ε' > 0`, choose `G ∈ D^W` decaying strictly more slowly than `F₀`, say
`G ≥ 0` with `G(t) ≥ c\,e^{−(1+ε/2)t}` for large `t > 0`.  Then for every
`t > 0` fixed and every `s > 0`, `(F₀ − sG)(t) ≤ Ce^{−(1+ε)t} − sc\,e^{−(1+ε/2)t}`,
which is `< 0` for `t` large depending on `s`.  Hence `F₀ − sG ∉ E` for every
`s > 0`, so `E` is absorbing at no point; a set with nonempty interior in a
vector topology is absorbing at each of its interior points, so `E` has empty
interior in every vector topology.  Taking `F₀ = K` gives the second clause, and
directly: by Theorem 11.7(ii), `K(t) = O(e^{9t/2}e^{−πe^{2t}})`, so for every
`ε > 0` there is `t` with `K(t) < ½ε e^{−(1+ε)t}`, whence `(K + εF)(t) < 0` for
any `F ∈ D^W` with `F(t) ≤ −½e^{−(1+ε)t}` for large `t`.

(ii) is a special case of (i); it can also be seen directly.  Let `F ∈ E`,
`δ > 0`, and `F(t) ≤ Ce^{−(1+ε)|t|}`.  Fix a real even `φ ∈ C_c^∞([−1,1])`,
`φ ≥ 0`, `φ(0) = 1`.  For `t₁ > 0` put `G := c·φ(· − t₁)` with
`c := 2Ce^{−(1+ε)(t₁−1)}`.  Then `G ∈ D^W`, `G ≥ 0`, and

    ‖G‖₁ ≤ c·2\cosh((t₁+1)/2)·2‖φ‖_∞ ≤ C'e^{−(1+ε)t₁}e^{t₁/2} → 0

as `t₁ → ∞`; choose `t₁` with `‖G‖₁ < δ`.  But
`(F−G)(t₁) ≤ Ce^{−(1+ε)(t₁−1)} − c < 0`, so `F − G ∉ E`.

(iii) is (i) together with Theorem 17.8(c).  ∎  `PROVED`

**Corollary 17.10 (the criterion on the ample cone; `PROVED`).**  `A` is a convex
cone, `K ∈ A`, and `A` is absorbing at `K`: for `F ∈ D^W` and
`0 < ε < 1/(2C_F)`, `K + εF = ε(F + 2mK)` with `m := 1/(2ε) > C_F` lies in `A` by
Theorem 11.14(iii), `C_F` being the bounded-density constant (11.17).
Consequently

    **RH  ⟺  I_∞(F,F) ≤ ½(\deg F)²  for every F ∈ A.**                    (17.2)

*Proof.*  That `A` is a convex cone is immediate from its definition; `K ∈ A` by
Theorem 11.8(v) and Theorem 11.13(i); absorption is the display.  Apply
Theorem 17.8 with `V = D^W`, `Q = I_∞`, the vector `K` and the set `C = A`,
using `I_∞(F,K) = ½\deg F` and `I_∞(K,K) = ½`, so that clause (b) reads
`¼(\deg F)² ≥ ½I_∞(F,F)`.  By Theorem 17.5(vi), clause (a) says `I_∞ ≤ 0` on
`P^W`, which is RH: for the implication from RH, `Φ_F(ρ)Φ_F(1−ρ) = |Φ_F(½+iγ)|² ≥ 0`
for real `F`, so `I_∞|_{P^W} ≤ 0` by Theorem 17.5(v); the converse is Paper 45
Theorem 10.4.  ∎  `PROVED`

**Remark 17.10a (the caveat on (17.2)).**  `A` is defined by quantifying
`I_∞(E,H) > 0` over all effective `E`, hence through the zero sum.  It is
therefore **not** a cone defined without reference to the zeros, and (17.2) is
not by itself a usable criterion.  A description of `A` that does not quantify
over `I_∞` is not available here and is recorded as `OPEN` in §17.7.

**Corollary 17.11 (`RESTATEMENT`).**  RH holds if and only if the Hodge-index
inequality `I_∞(F,F) ≤ ½(\deg F)²` holds on `D^W`, if and only if it holds on any
one detecting cone.  This restates Theorem 17.8(a)⇔(b), Theorem 17.5(vi) and
Paper 45 Theorem 10.4 in the terms of Definition 17.2; the second equivalence is
Definition 17.2 read in both directions.  `RESTATEMENT`

### 17.5 The Landau criterion: the triangle family detects

**Definition 17.12 (the triangle family).**  For `T > 0` let
`h_T(t) := (1 − |t|/T)_+`, so that
`h_T = F_T ⋆ F_T^∨` with `F_T := T^{−1/2}\mathbf 1_{[−T/2,T/2]}`, and

    Φ_{h_T}(s) = Φ_{F_T}(s)Φ_{F_T}(1−s)
      = \frac{4\sinh²((s−½)T/2)}{T(s−½)²} .                              (17.3)

Write `w_ρ := ρ − ½` and `W(h_T) := Σ_ρ Φ_{h_T}(ρ)`, absolutely convergent since
`|Φ_{h_T}(ρ)| ≤ 4e^{|\mathrm{Re}\,w_ρ|T}/(T|w_ρ|²)` and `Σ_ρ|w_ρ|^{−2} < ∞`
by (E3d).  `F_T` is even, so `μ(F_T) = 0` and, by Theorem 17.7(iii),

    Hodge index at `F_T`  ⟺  W(h_T) ≥ 0 .                                 (17.4)

**Lemma 17.13 (the Laplace transform of the family; `PROVED`).**  Put
`θ₀ := \sup_ρ|\mathrm{Re}\,w_ρ| ≤ ½` (by (E2)).  For `\mathrm{Re}\,z > θ₀` the
integral `G(z) := ∫_0^∞ T·W(h_T)\,e^{−zT}\,dT` converges absolutely and

    G(z) = \frac{2}{z²}\,\frac{ξ'}{ξ}\Big(½ + z\Big) .

*Proof.*  Absolute convergence: `T|W(h_T)| ≤ 4e^{θ₀T}Σ_ρ|w_ρ|^{−2}`, so the
integral converges absolutely for `\mathrm{Re}\,z > θ₀`, and Fubini licenses
termwise integration.  For a single zero, with `w := w_ρ`, one has
`4\sinh²(wT/2) = 2\cosh(wT) − 2`, and for `\mathrm{Re}\,z > |\mathrm{Re}\,w|`

    ∫_0^∞ 4\sinh²(wT/2)\,e^{−zT}\,dT
      = ∫_0^∞ (2\cosh(wT) − 2)\,e^{−zT}\,dT
      = \frac{2z}{z²−w²} − \frac{2}{z}
      = \frac{2w²}{z(z²−w²)} ,                                            (17.5)

so the `ρ`-term of `G` is `w^{−2}·2w²/(z(z²−w²)) = 2/(z(z²−w²))` and

    G(z) = \frac{2}{z}\,Σ_ρ \frac{1}{z² − w_ρ²} .

It remains to identify `Σ_ρ(z²−w_ρ²)^{−1} = z^{−1}(ξ'/ξ)(½+z)`.  By Hadamard's
factorization ((E2),(E3a)), `(ξ'/ξ)(s) = B + Σ_ρ(1/(s−ρ) + 1/ρ)` in the
symmetric order; subtracting the expansions at `s = ½+z` and `s = ½−z` cancels
`B` and every `1/ρ`, and the resulting series converges **absolutely**, each
bracket being `O(|ρ|^{−2})`:

    \frac{ξ'}{ξ}(½+z) − \frac{ξ'}{ξ}(½−z)
      = Σ_ρ\Big[\frac{1}{z−w_ρ} + \frac{1}{z+w_ρ}\Big]
      = 2z\,Σ_ρ\frac{1}{z²−w_ρ²} .

Since `ξ(s) = ξ(1−s)` gives `(ξ'/ξ)(½−z) = −(ξ'/ξ)(½+z)`, the left-hand side is
`2(ξ'/ξ)(½+z)`.  ∎  `PROVED`

**Theorem 17.14 (the triangle family detects; `PROVED`).**  If `W(h_T) ≥ 0` for
every `T > 0`, then every zero of `ξ` lies on `\mathrm{Re}\,s = ½`.
Equivalently,

    **RH  ⟺  Σ_ρ \frac{4\sinh²(w_ρT/2)}{T\,w_ρ²} ≥ 0 \text{ for every } T > 0 ,**

the sum taking, under RH, the form `Σ_γ 4\sin²(γT/2)/(Tγ²)`.

*Proof.*  Suppose `f(T) := T·W(h_T) ≥ 0` for all `T > 0`.  By Lemma 17.13 the
Laplace integral `G(z) = ∫_0^∞ f(T)e^{−zT}dT` converges for
`\mathrm{Re}\,z > θ₀`, so its abscissa of convergence `σ_c` is finite,
`σ_c ≤ θ₀`.  By Landau's theorem for Laplace transforms **(X20)** — a Laplace
integral with nonnegative integrand is singular at its real abscissa of
convergence — the point `z = σ_c` is a singular point of the analytic
continuation of `G`.

Now `G(z) = 2z^{−2}(ξ'/ξ)(½+z)` is meromorphic on `C`, with poles exactly at:

 * `z = w_ρ = ρ − ½` for each zero `ρ` of `ξ`, simple, with residue the
   multiplicity of `ρ`; and
 * `z = 0`.  Indeed `(ξ'/ξ)(½+z)` is **odd** in `z`, so
   `(ξ'/ξ)(½+z) = cz + O(z³)` with `c = −Σ_ρ w_ρ^{−2}`, and `c > 0`: group the
   zeros into the quartets `\{ρ,\barρ,1−ρ,1−\barρ\}`; in the on-line case
   `w = iγ` and `w^{−2} = −γ^{−2} < 0`, and in the off-line case the quartet
   `\{±(δ+iγ), ±(δ−iγ)\}` contributes
   `4\,\mathrm{Re}((δ+iγ)^{−2}) = 4(δ²−γ²)/(δ²+γ²)²`, which is `< 0` because
   `|δ| ≤ ½ < γ` for every zero, `γ` being at least `14.13` by (E3a)/(E3c).
   Hence `G` has a **simple pole at `z = 0`**.  (Only `c ≠ 0` is needed: were
   `c = 0`, `G` would be regular at `0` and the conclusion below would follow a
   fortiori from `σ_c ≤ 0`.)

No zero of `ξ` is real, since `ζ` has no real zero in `(0,1)` by (E2); so every
`w_ρ` is non-real and the **only real singularity of `G` is `z = 0`**.  As
`σ_c ∈ R` is a singularity, `σ_c = 0`.  Therefore the Laplace integral converges
on `\mathrm{Re}\,z > 0` and `G` is analytic there; but a zero `ρ` with
`\mathrm{Re}\,ρ > ½` would give a pole at `z = w_ρ` with `\mathrm{Re}\,w_ρ > 0`.
Hence no such zero exists, and by the functional equation none with
`\mathrm{Re}\,ρ < ½` either.  ∎  `PROVED`

**Remark 17.14a (the falsifier).**  The same proof applied to `Ξ_a` uses

    G_a(z) = \frac{2}{z²}\frac{Ξ_a'}{Ξ_a}(½+z)
      = \frac{2}{z²}\Big[\frac{ξ'}{ξ}(½+z+a) + \frac{ξ'}{ξ}(½+z−a)\Big] ,

whose poles are at `z = w_ρ ∓ a = iγ ∓ a`, all non-real, together with `z = 0`.
The argument gives: if `W_a(h_T) ≥ 0` for every `T`, then `Ξ_a` has no zero off
`\mathrm{Re}\,s = ½`.  But `Ξ_a` does have such zeros, at `ρ ± a`.  Hence
`W_a(h_T) < 0` for some `T`: **the triangle family detects the falsifier.**

**Remark 17.15 (attribution; `OPEN`).**  The mechanism of Theorem 17.14 is
Landau's theorem, and the identity `G(z) = 2z^{−2}(ξ'/ξ)(½+z)` is the
Laplace-transform avatar of the classical fact that `ξ'/ξ` is the generating
function of the zeros.  The criterion in the displayed one-parameter form is
**not** claimed as new; its status in the literature is `OPEN` and the label
`PROVED` on Theorem 17.14 rests on the proof given, not on novelty.  The precise
question to settle: is "RH ⟺ `Σ_ρ 4\sinh²(w_ρT/2)/(Tw_ρ²) ≥ 0` for every
`T > 0`" — Weil positivity tested on the Fejér/triangle family, equivalently the
Landau reading of `2z^{−2}(ξ'/ξ)(½+z)` — already known?  Sources to check:
Fejér-kernel forms of Weil positivity, in particular Bombieri, *Remarks on
Weil's quadratic functional in the theory of prime numbers*; Yoshida (1992);
Riesz-mean and Báez-Duarte-type one-parameter criteria.  `OPEN`

**Lemma 17.16 (transport to `D^W`; `PROVED`).**  Let `ψ_δ ∈ C_c^∞(R)` be real,
even, `ψ_δ ≥ 0`, `∫ψ_δ = 1`, `\mathrm{supp}\,ψ_δ ⊆ [−δ,δ]`.  Put
`F_T^{(δ)} := F_T ⋆ ψ_δ ∈ C_c^∞(R) ⊂ D^W`.  Then `F_T^{(δ)} ≥ 0` (effective),
even, and `W(F_T^{(δ)}⋆(F_T^{(δ)})^∨) → W(h_T)` as `δ → 0`.  Consequently, if
`W(h_T) < 0` for some `T`, then for small `δ` the class `F_T^{(δ)}` is an
effective, even, compactly supported, smooth class at which the Hodge-index
inequality fails.

*Proof.*  `Φ_{F_T^{(δ)}}(s) = Φ_{F_T}(s)Φ_{ψ_δ}(s)`, so the `ρ`-term of the zero
sum is `Φ_{h_T}(ρ)·Φ_{ψ_δ}(ρ)Φ_{ψ_δ}(1−ρ)`.  Since
`|Φ_{ψ_δ}(s)| ≤ ∫ψ_δ(t)e^{(σ−½)t}dt ≤ e^{δ/2}` for `0 ≤ σ ≤ 1`, the terms are
dominated by `e^{δ}|Φ_{h_T}(ρ)| ∈ ℓ¹`, and `Φ_{ψ_δ}(s) → 1` pointwise as
`δ → 0`.  Dominated convergence gives the limit.  Effectivity and evenness are
clear; `μ(F_T^{(δ)}) = 0` by evenness, so Theorem 17.7(iii) applies.  ∎  `PROVED`

**Corollary 17.17 (`E` and `C_c^∞` are detecting cones; `PROVED`).**  The
effective cone `E` and `C_c^∞(R)` are detecting cones in the sense of
Definition 17.2: both are convex cones of classes, and both contain the
witnesses `F_T^{(δ)}` of Lemma 17.16, which by Theorem 17.14 exist whenever `ξ`
has an off-line zero.  ∎  `PROVED`

**Remark 17.17a.**  Together with Theorem 17.9 this is the exact shape of the
difficulty: `E` is detecting, and is defined with no reference to a zero, but it
is not absorbing at `K`, so the Lorentzian criterion cannot be run on the one
cone where detection is cheapest.

### 17.6 On the detecting cones the sign is the prime-number-theorem remainder

**Proposition 17.18 (the exact main-term cancellation; `PROVED`).**  Write
`ψ_{Ch}(u) := Σ_{n≤u}Λ(n) = u + \mathcal E(u)`.  Then

 (i) `Φ_{h_T}(0) + Φ_{h_T}(1) = (16/T)(\cosh(T/2) − 1)
     = (8e^{T/2} + 8e^{−T/2} − 16)/T`;
 (ii) `PRIME(h_T) = (2/T)∫_1^{e^T}ψ_{Ch}(u)\,u^{−3/2}\,[1 + (T − \log u)/2]\,du`;
 (iii) the main term of (ii), obtained by `ψ_{Ch}(u) ↦ u`, equals
     `(8e^{T/2} − 8 − 2T)/T` **exactly**; hence

      [Φ_{h_T}(0)+Φ_{h_T}(1)] − PRIME_{main}(h_T) = 2 − 8(1 − e^{−T/2})/T → 2 ;

 (iv) with `R(T) := (2/T)∫_1^{e^T}\mathcal E(u)\,u^{−3/2}[1 + (T − \log u)/2]\,du`,

      W(h_T) = 2 − 8(1 − e^{−T/2})/T + ARCH(h_T) − R(T) ,                (17.6)

     an identity between an elementary function of `T`, an explicit convergent
     integral of the digamma function against the Fejér kernel
     `\hat h_T(τ) = 4\sin²(τT/2)/(Tτ²) ≥ 0`, and a functional of the Chebyshev
     remainder.  **No zero of `ξ` appears in (17.6).**

*Proof.*  (i) Put `s = 0` and `s = 1` in (17.3), where `(s−½)² = ¼`, and use
`\sinh²(T/4) = (\cosh(T/2)−1)/2`.

(ii) Abel summation against `g(u) := (T − \log u)u^{−1/2}`, so that
`PRIME(h_T) = (2/T)∫_1^{e^T}g\,dψ_{Ch}`, using `g(e^T) = 0`, `ψ_{Ch}(1) = 0` and
`g'(u) = −u^{−3/2}[1 + (T−\log u)/2]`.

(iii) Substituting `u = e^v` turns the main term into
`(2/T)∫_0^T e^{v/2}[1 + (T−v)/2]\,dv`, and
`∫_0^Te^{v/2}dv = 2(e^{T/2}−1)`, `∫_0^Te^{v/2}(T−v)dv = 4e^{T/2} − 4 − 2T`, so
the main term is `(2/T)[2e^{T/2}−2 + 2e^{T/2}−2−T] = (8e^{T/2}−8−2T)/T`;
subtract it from (i).

(iv) is the explicit formula (11.3) applied to `h_T`, i.e.

    W(h_T) = [Φ_{h_T}(0) + Φ_{h_T}(1)] + ARCH(h_T) − PRIME(h_T) ,

combined with (i)–(iii).  ∎  `PROVED`

**Theorem 17.19 (on the detecting cones the sign is the PNT remainder;
`PROVED-IN-REPOSITORY`).**  In the identity (17.6) everything except `R(T)` is
unconditional: (i)–(iii) of Proposition 17.18 are elementary identities, and
`ARCH(h_T)` is an explicit convergent integral of
`\mathrm{Re}\,ψ(¼+iτ/2) − \log π` against the nonnegative Fejér kernel of total
mass `2πh_T(0) = 2π`, requiring no zero information; it is `O(1)` in `T` and
converges as `T → ∞` to `\mathrm{Re}\,ψ(¼) − \log π
= −(γ + π/2 + 3\log 2) − \log π`, the Fejér kernel being an approximate identity
at `τ = 0`.  Hence proving `W(h_T) ≥ 0` for large `T` is exactly proving
`R(T) = O(1)`.  The Abel weight

    w_T(u) := (2/T)\,u^{−3/2}[1 + (T − \log u)/2]

is **positive with no sign change** on `(1,e^T)`, so the only unconditional
route is the absolute bound: with `|\mathcal E(u)| ≤ 0.04\,u` (Rosser–Schoenfeld,
import (X15)),

    |R(T)| ≤ 0.04·(8e^{T/2} − 8 − 2T)/T ≍ 0.32\,e^{T/2}/T ,

which **diverges** against the `O(1)` target; and with the best unconditional
prime-number-theorem remainder **(X20a)**,
`\mathcal E(u) ≪ u\exp(−c(\log u)^{3/5}(\log\log u)^{−1/5})`, one gets
`|R(T)| ≪ e^{T/2}e^{−cT^{3/5}}/T`, still divergent.  Making `R(T) = O(1)`
requires `\mathcal E(u) = O(u^{1/2+ε})`, which **is** RH, by von Koch.  This is
the specialization to the triangle family of the repository's recorded route
no-go `114_d_185_PNT_TATE_LOW_BLOCK_NOGO` — *no theorem whose arithmetic
hypotheses are only a prime-number-theorem remainder and two linear moments can
prove the needed low-block bound* — and of
`E72_49_BANDLIMITED_PNT_ENDPOINT_THEOREM`.  Accordingly no unconditional
positivity proof through Chebyshev, Mertens or the prime-number theorem is
attempted here, and no bound on `R(T)` is claimed.
`PROVED-IN-REPOSITORY`

**Remark 17.20 (convexity of the kernel does not help).**  One might hope that
the convexity and monotonicity of `h_T` protect the inequality by defeating the
perturbation mechanism of `114_d_185`.  It does the opposite: it removes the one
feature that made that construction delicate.  There, a signed perturbation of
the continuous Chebyshev measure is built which satisfies a
prime-number-theorem remainder, has two prescribed Tate-type moments exactly
zero, and carries a Fourier spike, the spike being needed because the pairing
weight `e^{−iτ\log n}` oscillates.  Here the pairing weight is `w_T ≥ 0` — which
is exactly what the convexity and monotonicity of `h_T` produce, by
Proposition 17.18(ii) — so no oscillation is needed and no spike has to be
constructed: take any positive measure `d\tildeψ = (1 + η(u))du` with
`0 ≤ η(u) ≤ \exp(−c(\log u)^{3/5}(\log\log u)^{−1/5})`, bounded below by half
that on `[e^{T/2},e^T]`.  Then `\tildeψ` satisfies the remainder of **(X20a)**,
it is subject to no moment constraint at all (the polar term
`Φ_h(0)+Φ_h(1)` depends on `h` only, never on `\mathcal E`), and its remainder
functional

    \tilde R(T) = ∫_1^{e^T}\tilde{\mathcal E}(u)\,w_T(u)\,du ,
    \tilde{\mathcal E}(u) = ∫_1^uη ≥ 0 ,

pairs a **one-signed** function against a **positive** weight, hence
`\tilde R(T) ≫ e^{T/2}e^{−cT^{3/5}}/T → ∞` by the computation of Theorem 17.19.
So the crudest admissible perturbation already destroys the target, with no
spike, no frequency and no moment budget; no cancellation may be assumed.  A
cancellation could come only from a sign change of the weight, of which there is
none, or from a structural property of `\mathcal E` itself, and admissibility
alone permits `\mathcal E ≥ 0`; second-moment estimates of Mertens type bound
`∫\mathcal E(u)²`, not `∫\mathcal E\,w_T` against a positive `w_T` of total mass
`∫_1^{e^T}u^{−3/2}[1+(T−\log u)/2]du = T`, and no Cauchy–Schwarz on that pairing
beats `e^{T/2}`.

### 17.7 Equimodularity of `|p − ½|` as the separating zero-free invariant

Fix `0 < a < ½`, `Z = Ξ_a`, `P = \{−a, a, 1−a, 1+a\}`,
`K_a = (e^{at}K)⋆(e^{−at}K) > 0`, `Φ_{K_a} = Ξ_a` (Remark 11.8a,
Proposition 12.6).  Put `α := ½ξ(2a) > 0`, `β := ½ξ(1+2a) > 0`, so that
`Ξ_a(a) = Ξ_a(1−a) = α` and `Ξ_a(−a) = Ξ_a(1+a) = β` (using `ξ(0) = ξ(1) = ½`,
`ξ(1−2a) = ξ(2a)`, `ξ(−2a) = ξ(1+2a)`, and `ξ > 0` on `R`, which is
Proposition 12.6(b)(3)).  Set `S := Σ_{p∈P}Ξ_a(p)² = 2α² + 2β² > 0`, so that
`I_∞^{(a)}(F,K_a) = \deg_aF = Σ_pΞ_a(p)Φ_F(p)` and `I_∞^{(a)}(K_a,K_a) = S`.

**Theorem 17.21 (the falsifier fails the Hodge-index inequality on an effective
class; `PROVED`).**  For `u ≠ 0` put `F_u := τ_uK_a + τ_{−u}K_a`.  Then
`F_u ∈ D^W_a`, `F_u > 0` (effective), `F_u` is even, `\deg_aF_u > 0`, and

    I_∞^{(a)}(F_u,F_u)·I_∞^{(a)}(K_a,K_a) > I_∞^{(a)}(F_u,K_a)² ,

i.e. the Hodge-index inequality **fails**, strictly, for every `u ≠ 0`.  The same
computation for `ξ` gives **equality**, for every `u`.

*Proof.*  `Φ_{F_u}(s) = 2\cosh((s−½)u)Ξ_a(s)`, so with `c_p := \cosh((p−½)u)`
and `w_p := Ξ_a(p)²`, using `Ξ_a(1−p) = Ξ_a(p)`, `c_{1−p} = c_p`, and
`Φ_{F_u}(ρ) = 0` at every zero `ρ` of `Ξ_a`:

    I_∞^{(a)}(F_u,F_u) = Σ_p Φ_{F_u}(p)Φ_{F_u}(1−p) = 4Σ_p w_p c_p² ,
    I_∞^{(a)}(F_u,K_a) = Σ_p Φ_{F_u}(p)Ξ_a(1−p) = 2Σ_p w_p c_p ,
    I_∞^{(a)}(K_a,K_a) = Σ_p w_p = S .

The Hodge-index inequality is therefore
`4S·Σ_pw_pc_p² ≤ 4(Σ_pw_pc_p)²`, i.e.
`(Σ_pw_p)(Σ_pw_pc_p²) ≤ (Σ_pw_pc_p)²`.  Cauchy–Schwarz for the measure `(w_p)`
gives the **reverse** inequality, with equality if and only if `c_p` is constant
on `P`.  Here `p − ½ ∈ \{−½−a, −½+a, ½−a, ½+a\}`, so
`c_p ∈ \{\cosh((½+a)u), \cosh((½−a)u)\}`, and these differ for `u ≠ 0`,
`0 < a < ½`.  Hence Cauchy–Schwarz is strict and the Hodge-index inequality
fails strictly.  For `ξ`, `P = \{0,1\}` and `p − ½ ∈ \{−½,½\}`, so
`c_0 = c_1 = \cosh(u/2)` is constant, Cauchy–Schwarz is an equality, and the
Hodge-index inequality holds with equality.  Effectivity: `K_a > 0`, so
`F_u > 0`.  ∎  `PROVED`

**Remark 17.21a.**  No zero, no prime and no `h⁰` enters Theorem 17.21.  It is a
two-line predecessor of the falsifier of §12.3, which proceeds through the rank-4
operator `Π_P` and Proposition 12.4B; it shows that the falsifier is already
visible in the polar block alone, and it exhibits the invariant that the
substitutions (S2)/(S3) of §12.5 were using.

**Theorem 17.22 (the equimodularity criterion; `PROVED`).**  Let `Z` be
admissible in the sense of Proposition 12.6, with polar set `P`, canonical class
`K_Z` and `Φ_{K_Z} = Z`.  The following are equivalent.

 (a) The Hodge-index inequality
     `I_∞^{(Z)}(F,F)\,I_∞^{(Z)}(K_Z,K_Z) ≤ I_∞^{(Z)}(F,K_Z)²` holds on the
     **translation cone** `Λ_Z^+ := \{Σ_j c_jτ_{u_j}K_Z : c_j ≥ 0\}`;
 (b) it holds on the translation span `Λ_Z := \mathrm{span}\{τ_uK_Z\}`;
 (c) `|p − ½|` is the **same** for every `p ∈ P` (equimodularity of the polar
     exponents).

*Proof.*  (c)⇒(b).  If `|p−½| = θ` for every `p ∈ P`, then `P = \{½−θ, ½+θ\}`;
here the reality of `P` is load-bearing — Proposition 12.6 hypothesizes a finite
set `P ⊂ R` of simple poles with `P = 1−P`, whereas for a complex `P` the
condition `|p−½| = θ` cuts out a circle and the normal form fails.  For
`X = Σ_jc_jτ_{u_j}K_Z` one has `Φ_X(p) = Z(p)Σ_jc_je^{(p−½)u_j}`.  Put
`A := Σ_jc_je^{θu_j}`, `B := Σ_jc_je^{−θu_j}`, and
`z := Z(½+θ) = Z(½−θ) > 0`, the two polar values agreeing because
`Z(s) = Z(1−s)`.  Then

    I_∞^{(Z)}(X,X) = Φ_X(½+θ)Φ_X(½−θ) + Φ_X(½−θ)Φ_X(½+θ) = 2z²AB ,
    I_∞^{(Z)}(X,K_Z) = z²(A+B) ,   I_∞^{(Z)}(K_Z,K_Z) = 2z² ,

and the inequality reads `4z⁴AB ≤ z⁴(A+B)²`, i.e. `(A−B)² ≥ 0`, with slack
`z⁴(A−B)²` — which for `Z = ξ`, `θ = ½`, `z = ½` is the slack `½μ(X)²` of
Theorem 17.7(i) up to normalization.

(b)⇒(a) is inclusion.  (a)⇒(c): take `X = τ_uK_Z + τ_{−u}K_Z ∈ Λ_Z^+` and run
the computation of Theorem 17.21 verbatim with `w_p := Z(p)²`,
`c_p := \cosh((p−½)u)`; the Hodge-index inequality forces equality in
Cauchy–Schwarz, hence `\cosh((p−½)u)` is constant in `p` for every `u ≠ 0`,
hence `|p−½|` is constant.  ∎  `PROVED`

**Corollary 17.23 (the translation cone of `ξ`; `PROVED`).**
`Λ_ξ^+ = \{Σ_jc_jτ_{u_j}K : c_j ≥ 0\}` is a convex cone of **effective** classes
of `D^W` (each `τ_uK > 0`), defined with no reference to the zeros, on which the
Hodge-index inequality holds unconditionally with the explicit slack
`⅛(A−B)²`, `A = Σ_jc_je^{u_j/2}`, `B = Σ_jc_je^{−u_j/2}`; equivalently
`I_∞(X,X) = ½AB ≤ ⅛(A+B)² = ½(\deg X)²`.  This is Theorem 17.22 with `Z = ξ`,
`θ = ½`, `z = ½`.  ∎  `PROVED`

**Remark 17.24 (the ceiling; the sign cannot come from equimodularity).**
Theorem 17.22 is a **necessary** condition separating `ξ` from `Ξ_a` with no
zero mentioned.  It does **not** separate `ξ` from `ζ_K` for a number field `K`:
the completed `Λ_K` has `P = \{0,1\}` and is equimodular.  Consequently any
argument deriving the **sign** from equimodularity alone would prove GRH for
every number field.  Equimodularity is therefore necessary and cannot be
sufficient, and no claim to the contrary is made here.

### 17.8 The structurally signed cone is maximally non-detecting

**Corollary 17.25 (`PROVED`).**  `Λ_ξ^+ ⊂ 𝓝_∞`: for every `X ∈ Λ_ξ^+` and every
zero `ρ` of `ξ`, `Φ_X(ρ) = 0`.  Hence `Λ_ξ^+` is **not detecting** — indeed it
is maximally non-detecting, its zero datum being identically `0`.

*Proof.*  `Φ_{τ_uK}(s) = e^{(s−½)u}ξ(s)` by Lemma 11.2(iv), which vanishes at
every zero of `ξ`; the vanishing passes to nonnegative combinations.  So
`Z(X) ≡ 0` and `Λ_ξ ⊂ (P^W)^{⊥_{I_∞}}` by Theorem 11.10; by
Theorem 17.7(iii) the Hodge-index inequality then holds at every `X ∈ Λ_ξ^+`
whatever the location of the zeros, so no `X ∈ Λ_ξ^+` can witness failure in the
sense of Definition 17.2.  ∎  `PROVED`

**Theorem 17.26 (detection and structural signature live on complementary
summands; `PROVED`).**  With the splitting of Theorem 17.5 and the separation of
data of Remark 17.6:

 (1) any inequality on `D^W` that is a function of the ruling datum
     `M(F) ∈ R²` alone is satisfied identically by the polar block
     (Theorem 17.7(ii)) and is therefore blind to detection;
 (2) detection is a statement about the zero datum `Z(F) ∈ ℓ¹(Z(ξ))` alone: by
     Theorem 17.7(iii), the Hodge-index inequality fails at `F` if and only if
     `Σ_ρΦ_F(ρ)Φ_F(1−ρ) < −½μ(F)²`;
 (3) the translation cone `Λ_ξ^+` — the one cone whose sign follows from the
     structure of the carrier (Corollary 17.23) — has `Z ≡ 0` and is maximally
     non-detecting (Corollary 17.25);
 (4) the two data are independent: `M` is onto `R²` (Lemma 17.3),
     `\ker Z = (P^W)^{⊥_{I_∞}}` exactly (Theorem 11.10), and `𝓝_∞` is exactly
     `\ker M ∩ \ker Z` (Theorem 11.11).

Hence "the sign follows from a structure of the carrier — polar block or
translation lattice" and "the cone is detecting" are statements about
`I_∞`-orthogonal complementary summands of `D^W`.

*Proof.*  (1) is Theorem 17.7(ii); (2) is Theorem 17.7(iii); (3) is
Corollaries 17.23 and 17.25; (4) is Lemma 17.3 together with Theorems 11.10 and
11.11.  The final sentence is the conjunction of (1)–(4) read through the
orthogonal splitting `D^W = Λ ⊥ P^W` of Theorem 17.5(iii).  ∎  `PROVED`

**Corollary 17.27 (`PROVED`).**  On a detecting cone the sign is a statement
about prime powers of **unbounded** modulus.  Precisely, let `C` be detecting and
let `F ∈ C` witness failure at an off-line zero.  By Theorem 17.7(v) the witness
satisfies `PRIME(F⋆F^∨) > ARCH(F⋆F^∨) + ½(\deg F)²`, so `PRIME(F⋆F^∨) ≠ 0` and
therefore `\mathrm{supp}(F⋆F^∨)` contains `±\log n` for some prime power
`n ≥ 2`.  ∎  `PROVED`

### 17.9 The one remaining quadrant

**Remark 17.28 (`OPEN`).**  Clauses (i) and (ii) of the question this section
answers — a cone that is detecting, and defined without reference to the zeros —
are cheap: `E = \{F ≥ 0\}` and `C_c^∞(R)` satisfy both (Corollary 17.17,
Definition 17.1).  What is open is clause (iii) **on `E`**: a proof of

    I_∞(F,F) ≤ ½(\deg F)²  for every F ∈ E

that uses the structure of the carrier — the polar block, the translation
lattice, positivity, unimodularity of the local roots — and not the zero sum or
the Chebyshev remainder.  Two sharp constraints stand on any such proof.  First,
by Remark 17.24 it must **fail** for `ζ_K`-shaped data or else prove GRH for
every number field.  Second, by Theorem 17.19 it cannot pass through a bound on
`R(T)`, since that is von Koch's form of RH.  Two subsidiary items are recorded
as open with it: a description of the ample cone `A` that does not quantify over
`I_∞`, without which (17.2) is not usable (Remark 17.10a); and the attribution
question of Remark 17.15.  No such proof is produced here, and no cone
satisfying all three clauses is exhibited.  `OPEN`

**Withdrawn in this section**

| claim | reason |
|---|---|
| Translation is *the* operation that creates detection — the separating operation | `REFUTED`.  The witnesses of Paper 45 Theorem F are `q_±(∂)(φ^{⋆N})` with `φ` a single even window bump chosen after the off-line zero: convolution powers and one real differential operator, with **no** translation anywhere.  The exponential factor `e^{(s−½)u}` attributed to `τ_u` is produced instead by `\hatφ(z)^N`.  Translation is sufficient but not necessary; what all sufficient operation sets share is escape from every fixed window |
| The Pólya cone `C_{Pó}` of even, nonnegative, convex, non-increasing kernels is a detecting cone | `REFUTED` twice over.  It is a cone of **kernels** `h = F⋆F^∨`, not of classes, so Definition 17.2 does not apply to it; and `C_{Pó} ∩ C¹(R) = \{0\}` — convexity plus monotonicity plus `h'(0) = 0` force `h' ≡ 0` — so `C_{Pó} ∩ D^W = \{0\}` and `\{F ∈ D^W : F⋆F^∨ ∈ C_{Pó}\} = \{0\}`.  The detecting objects of record are `E` and `C_c^∞(R)` (Corollary 17.17) |
| `E` has nonempty interior around `K`, because `K > 0` with known decay, so the reverse Cauchy–Schwarz may be run on `E` | `REFUTED`.  The super-exponential decay of `K` (Theorem 11.7(ii)) is exactly what prevents it: `E` is absorbing at no point of `D^W`, `K` included (Theorem 17.9(i)) |
| `K` is the unique `I_∞`-positive direction, up to scale, in `\mathrm{span}(K,K_odd)` | `REFUTED`.  That span is a Lorentzian plane, whose positive vectors form the open cone `\{xK + yK_odd : x² > y²\}` (Theorem 17.5(iv)) |
| Reverse Cauchy–Schwarz `Q(F,G)² ≥ Q(F)Q(G)` holds for all `F,G` in any convex cone with nonempty interior containing `K` | `REFUTED` by Theorem 17.8(e): `R^{1,2}`, `F = e₁`, `G = e₂`.  The correct third clause tests **against `K`**, on a set absorbing at `K` |
| `E` has empty interior in every topology making the functionals `I_∞(·,F)` continuous | `WITHDRAWN` as a non-sequitur: continuity of those functionals is a lower bound on the topology and does not force it to be coarser than `‖·‖₁`.  The conclusion is nevertheless true in the stronger, topology-free form of Theorem 17.9(i) |
| The polar main term matches the prime-sum main term only under unimodularity of the local roots | `REFUTED`.  For `Ξ_a` both are `2e^{(½+a)T}/(T(½+a)²)(1+o(1))`, by (17.3) at `s = p` and the Abel computation of Proposition 17.18(ii),(iii) applied to `Σ_{n≤x}Λ(n)(n^{a−½}+n^{−a−½})`.  The match is the residue matching of Proposition 12.6(S2)/(S3) and holds for **every** admissible `Z`; the invariant that separates is equimodularity (Theorem 17.22), not the growth match |
| On-line zeros contribute `Σ_γ 4\sin²(γT/2)/(γ²T)` of size `O(\log T)` | `REFUTED`: that sum is `O(1/T)`, being bounded by `(8/T)Σ_{γ>0}γ^{−2}`.  The scale `≍ e^{T/2}/T` belongs to the polar and prime main terms, which cancel (Proposition 17.18(iii)) |

---

## 18. What a proof of the sign must use: two method constraints

*Provenance note.  The material of this section is proved in
`03-research/phase-137-row-d-canonical-coupling/R137_001_ROUND1.md`,
`R137_003_ROUND2.md`, `R137_005_ROUND3.md` (items D.0 and D.11),
and in `03-research/phase-139-row-d-two-falsifiers/R139_001_ROUND1.md`
(items D.19–D.21); the labels and withdrawals recorded here are those of
`R137_007_CLOSING_DECISION.md` and `R139_005_CLOSING_DECISION.md`,
checked against `R137_002/004/006` and `R139_002/004`.  Nothing in this section
asserts, claims or suggests a sign.*

This section proves two constraints on any future proof of row D's target.  The
first, **T1**, says that such a proof may not use any property that
distinguishes `ζ` from the Dedekind zeta function of an arbitrary number field.
The second, **T2**, says that the axioms which the frame of §§11–12 makes
available — the analytic frame, the canonical class, the polar block, the
splitting and the explicit formula — are **jointly insufficient**, because a
completed Epstein zeta function satisfies all of them and violates the
conclusion.  Together they force any proof of the sign to invoke the Euler
product (or a real-positivity statement equivalent to the absence of Siegel
zeros) **and** to do so uniformly over all number fields.

Throughout, for an entire `Z` of order `1`, real on `R`, with `Z(s) = Z(1−s)`
and finite polar set `P ⊂ R` of `Z'/Z`, we write, on the Weil class `D^W(α)` of
Definition 11.1 with decay exponent `α > ½`,

    I_∞^{(Z)}(F,G) = Σ_{p∈P}Φ_F(p)Φ_G(1−p) − Σ_{ρ∈Z(Z)}Φ_F(ρ)Φ_G(1−ρ) ,      (18.1)

which for `Z = ξ`, `P = {0,1}` is Theorem 11.5 verbatim; the polar block carries
**weight one**, the value `Z(p)` appearing only when one pairs against the
canonical class, since `Φ_{K_Z}(1−p) = Z(p)` (§12.5 (S2)).  We abbreviate

    B_pol^{(Z)}(F,G) := Σ_{p∈P}Φ_F(p)Φ_G(1−p) ,
    Ŵ^{(Z)}(F,G) := −Σ_{ρ∈Z(Z)}Φ_F(ρ)Φ_G(1−ρ) ,

so `I_∞^{(Z)} = B_pol^{(Z)} + Ŵ^{(Z)}`; `Ŵ^{(Z)}` is the **primitive zero
form**, and on the primitive sector `P^W_Z = {F : Φ_F(p) = 0` for all `p ∈ P}`
it is all of `I_∞^{(Z)}` (Theorem 11.10).  *Hodge index at `F`* means

    I_∞^{(Z)}(F,F)·I_∞^{(Z)}(K_Z,K_Z) ≤ I_∞^{(Z)}(F,K_Z)² ,                   (18.2)

which for `Z = ξ` is `I_∞(F,F) ≤ ½(\deg F)²` and, for **even** `F`, reduces to
`Ŵ^{(Z)}(F,F) ≤ 0`.

---

### 18.1 T1: the proof must be uniform in the number field

**Theorem 18.1 (T1, field uniformity; `METHOD-CONSTRAINT`).**  Let `𝔓` be any
list of properties of a completed zeta function that holds for `ξ` and holds for
`ξ_K` for every number field `K`.  Then no derivation of the Hodge-index
inequality (18.2) from `𝔓` alone can be sound unless GRH holds for `ζ_K` for
every number field `K`.  In particular:

 (i) equimodularity of the polar block (`P = {0,1}`, `|p−½| = ½`) is **not**
     a distinguishing property: every `Λ_K` has it (Theorem 18.18(ii)), so no
     argument deriving the sign from equimodularity alone can be sound short of
     GRH;
 (ii) any property invoked at a load-bearing line of a proof of the sign for
      `ξ` must be named, and must be a property that `ξ` does **not** share
      with every `ξ_K` — or else the proof proves GRH for all number fields,
      and must be held to that standard.

*Proof.*  By Theorem 18.18(vi) the transfer theorem (Theorem 12.3) holds
verbatim for every number field `K`: the data `(P, D^W(α), ⋆, {}^∨, τ_•,
\{\cdot ≥ 0\}, K_K, 𝓝_∞^{(K)}, I_∞^{(K)}, \deg_K)` exist for `ξ_K`, and
(18.2) for `ξ_K` gives `I_∞^{(K)}(F,F) ≤ 0` on the primitive sector, hence — by
the argument of Paper 45 Theorem 10.4 transcribed to `ξ_K` — GRH for `ζ_K`.  A
derivation from `𝔓` is a finite chain of steps each of which invokes only
members of `𝔓` and the listed data; such a chain is a derivation for every
structure satisfying `𝔓`, hence for every `ξ_K`.  So its conclusion, if sound,
holds for every `ζ_K`.  (i) is Theorem 18.18(ii); (ii) is the contrapositive.  ∎
`METHOD-CONSTRAINT`

**Remark 18.1a.**  T1 is a statement about admissible derivations, not about
functions, and it is labelled as Restatement 12.4a rules: uniformity of a
*definition* transfers a *proof*, never the *truth* of a conclusion.  It does
not say that the sign is false, and it does not say that GRH is out of reach.
It says that a proof of the sign which does not name a property separating `ξ`
from some `ξ_K` is, whatever else it is, a proof of GRH for all number fields —
and the second method constraint, Theorem 18.16, says which properties are
available to be named.

---

### 18.2 T2: the Epstein constraint

Let `Q(x,y) = ax²+bxy+cy²` be integral and positive definite with
`\mathrm{disc}\,Q = b²−4ac = −D < 0`, and let
`Z_Q(s) := ½Σ'_{(m,n)∈Z²}Q(m,n)^{−s} = Σ_{n≥1}r_Q(n)n^{−s}` for `Re s > 1`,
where `r_Q(n) = ½\#\{v ∈ Z² : Q(v) = n\} ≥ 0`, and
`Λ_Q(s) := (√D/2π)^sΓ(s)Z_Q(s)`.  Let `h = h(−D)` be the class number of the
underlying imaginary quadratic field.  Two classical facts are imported:
**(X21)** (Davenport–Heilbronn) if `h > 1` then `Z_Q` has infinitely many zeros
in `Re s > 1`; and **(X25b)** (Heilbronn) `h(−D) → ∞`, so the family below is
nonempty.  Nothing about the zeros of `Z_Q` on or near `Re s = ½` is used, and
no unproved hypothesis is used anywhere.

#### 18.2.1 The Epstein canonical class

**Definition 18.2.**  `Ξ_Q(s) := ½·s(s−1)·Λ_Q(s)`.

**Theorem 18.3 (the Epstein canonical class; `PROVED`).**  Let `c := 2π/√D`
and, for `v ∈ Z²∖\{0\}` and `t ∈ R`, `y_v(t) := c\,e^{t}Q(v) > 0`.  Define

    K_Q(t) := ¼\,e^{t/2}\,Σ'_{v ∈ Z²}\big(y_v(t)² − 2y_v(t)\big)e^{−y_v(t)} .  (18.3)

Then:

 (i) the series and all its `t`-derivatives converge locally uniformly, and
     `K_Q ∈ C^∞(R)`;
 (ii) `K_Q` is **even**;
 (iii) `K_Q(t) = O\big(e^{5|t|/2}e^{−c\,e^{|t|}m_Q}\big)` with
       `m_Q := \min_{v≠0}Q(v) ≥ 1`, and the same for every derivative up to a
       factor polynomial in `e^{|t|}`; hence `K_Q ∈ D^W(α)` for **every**
       `α > 0`, and so are `K_Q^{(j)}` and `τ_uK_Q`;
 (iv) `Ξ_Q` is entire of order `1`, `Ξ_Q(s) = Ξ_Q(1−s)`, real on `R`, and
      `Φ_{K_Q}(s) = Ξ_Q(s)` for every `s ∈ C`;
 (v) `Ξ_Q(0) = Ξ_Q(1) = ¼`; the polar set of `Λ_Q` is `P = \{0,1\}`,
     `P = 1−P ⊂ R`, and `|p−½| = ½` for both `p ∈ P` — **equimodular**, with
     `θ_P = ½`, exactly as for `ξ`;
 (vi) `\deg K_Q := Φ_{K_Q}(0)+Φ_{K_Q}(1) = ½`, `I_∞^{(Q)}(F,K_Q) = ¼\deg F`,
      and `I_∞^{(Q)}(K_Q,K_Q) = 2(¼)² = ⅛`.

*Proof.*  Write `Θ(u) := Σ_{v∈Z²}e^{−cuQ(v)}` for `u > 0` and `A := Θ − 1`.

*The theta transformation.*  Put `M := (2/√D)A_Q` with
`A_Q = \begin{pmatrix}a & b/2\\ b/2 & c\end{pmatrix}`, so `\det M = 1` and
`π u\,v^{\top}Mv = c\,u\,Q(v)`; thus `Θ(u) = Σ_v e^{−πuv^{\top}Mv}`.
Two-dimensional Poisson summation gives
`Σ_ve^{−πuv^{\top}Mv} = u^{−1}(\det M)^{−1/2}Σ_ve^{−πu^{−1}v^{\top}M^{−1}v}`,
and `\tfrac{√D}2v^{\top}A_Q^{−1}v = \tfrac2{√D}\widetilde Q(v)` with
`\widetilde Q(x,y) = cx²−bxy+ay²`, which is properly equivalent to `Q` (apply
`(x,y) ↦ (−y,x)`), so `r_{\widetilde Q} = r_Q` and

    Θ(u) = u^{−1}Θ(1/u) .                                                     (18.4)

*Mellin.*  For `Re s > 1`, `∫_0^∞e^{−cuQ}u^{s−1}du = Γ(s)(cQ)^{−s}`, so
`∫_0^∞A(u)u^{s−1}du = Γ(s)c^{−s}Σ'Q(v)^{−s} = 2Λ_Q(s)`.  Splitting at `u = 1`
and using (18.4) in the form `A(u) = u^{−1}−1+u^{−1}A(1/u)`,

    2Λ_Q(s) = \frac1{s−1} − \frac1s + ∫_1^∞A(u)\big(u^{s−1}+u^{−s}\big)du ,    (18.5)

the integral entire in `s` (since `A(u) = O(e^{−cm_Qu})` for `u ≥ 1`) and
invariant under `s ↦ 1−s`.  This proves, without importing it, that `Λ_Q` is
meromorphic with simple poles exactly at `s = 0,1`, residues `∓½`, and
`Λ_Q(s) = Λ_Q(1−s)`.

*The kernel.*  Put `F(t) := Θ(e^t)` and `H(t) := e^{t/2}F(t)`.  By (18.4),
`F(t) = e^{−t}F(−t)`, hence `H(−t) = e^{−t/2}e^{t}F(t) = H(t)`: `H` is even.
From `2Λ_Q(s) = ∫_RA(e^t)e^{st}dt` we get `Λ_Q = Φ_G` with
`G(t) := ½e^{t/2}A(e^t) = ½(H(t)−e^{t/2})`.  Since
`Φ_{Πg}(s) = s(1−s)Φ_g(s)` (Lemma 11.2(iv)) with `Π = −∂_t²+¼`, and
`Πe^{t/2} = 0`,

    Φ_{−½ΠG}(s) = ½s(s−1)Λ_Q(s) = Ξ_Q(s),\qquad −½ΠG = ¼\big(H''−¼H\big) .     (18.6)

Now `∂_t = u∂_u` on functions of `u = e^t`, so with `y_v = ce^tQ(v)` we have
`∂_te^{−y_v} = −y_ve^{−y_v}` and `∂_t²e^{−y_v} = (y_v²−y_v)e^{−y_v}`; therefore
`(∂_t²+∂_t)A(e^t) = Σ'(y_v²−2y_v)e^{−y_v}`.  Writing `F = e^{−t/2}H` one computes
`(∂_t²+∂_t)F = e^{−t/2}(H''−¼H)`, and `(∂_t²+∂_t)F = (∂_t²+∂_t)A(e^t)` because
`(∂_t²+∂_t)1 = 0`.  Hence `¼(H''−¼H) = K_Q`, which with (18.6) gives the
identity `Φ_{K_Q} = Ξ_Q` on the strip where `Φ_{K_Q}` converges; both sides are
entire by (iii) and (18.5), so they agree on `C`.

(i),(iii): for `t ≥ t_0` the sum is dominated by `Σ'(y_v²+2y_v)e^{−y_v}` with
`y_v ≥ ce^tm_Q`, and `\#\{v : Q(v) ≤ X\} = O(X)`, so the sum is
`O(e^{−ce^tm_Q/2})`; derivatives add powers of `y_v`, which are absorbed; the
dominant term carries `y_v² ≍ e^{2t}`, whence the polynomial factor `e^{5t/2}`.
As `t → −∞` use (ii).  Local uniform convergence on compacta is the same
estimate.  (ii): `K_Q = ¼(H''−¼H)` with `H` even.
(iv): `Ξ_Q = Φ_{K_Q}` with `K_Q` of double-exponential decay, so
`|Φ_{K_Q}(s)| ≤ ∫|K_Q(t)|e^{(σ−½)t}dt = O(e^{C|σ|\log|σ|})` and the order is
`≤ 1`; it equals `1` because `Ξ_Q` has infinitely many zeros and `Ξ_Q(0) ≠ 0`.
Reality on `R` is clear from (18.3); the symmetry holds because `½s(s−1)` and
`Λ_Q` are both invariant under `s ↦ 1−s`.
(v): from (18.5), `(s−1)·2Λ_Q(s) → 1` at `s = 1`, so `Ξ_Q(1) = ½·1·½ = ¼`, and
`Ξ_Q(0) = Ξ_Q(1)`.
(vi): (18.1) with `G = K_Q`, using `Φ_{K_Q}(1−ρ) = Ξ_Q(1−ρ) = 0` at every zero
and `Ξ_Q(0) = Ξ_Q(1) = ¼`.  ∎  `PROVED`

**Remark 18.3a (why the `ξ`-proof of positivity does not transfer).**  For `ξ`,
Theorem 11.7(i) proves `K > 0` term by term: each term of (11.7) is
`2πn²e^{5u/2}e^{−πn²e^{2u}}(2πn²e^{2u}−3)` and `2πn²e^{2u} ≥ 2π > 3` for
`u ≥ 0`.  Here each term of (18.3) carries the factor `y_v²−2y_v`, positive iff
`y_v > 2`, i.e. iff `(2π/√D)e^tQ(v) > 2`; at `t = 0` this demands
`πQ(v) > √D` for **every** `v ≠ 0`, i.e. `πm_Q > √D`.  For a reduced form
`m_Q = a` and `D = 4ac−b²`, so the condition fails as soon as `c ≫ a` — the
generic situation once `h(−D) > 1`.  The term-by-term argument is unavailable,
and Corollary 18.6 shows the conclusion itself is false.  `PROVED`

#### 18.2.2 The frame transfers to `Ξ_Q`

From here to the end of §18.2, `Q` is the **principal** form of its
discriminant, so that `m_Q = 1` and `r_Q(1) = 1`; hence
`Z_Q(s) = 1 + Σ_{n≥2}r_Q(n)n^{−s}` and `−Z_Q'/Z_Q` is an ordinary Dirichlet
series supported on the integers `n ≥ 2`.  The restriction is needed: for
`m_Q ≥ 2` one has `−Z_Q'/Z_Q(σ) → \log m_Q ≠ 0` as `σ → +∞`, and the expansion
produces a *generalized* Dirichlet series over the semigroup generated by the
ratios `n/m_Q`, which the frame of §§11–12 does not carry.  It costs nothing:
the family `Q_k = x²+ky²` of Theorem 18.5 is principal, and (X21) applies to the
principal form of any discriminant with `h(−D) > 1`.  The non-principal case is
`OPEN`.

Put `σ_1 := \sup\{Re ρ : ρ ∈ Z(Ξ_Q)\}` and `θ_Z := σ_1 − ½`, and let `σ_a` be
the abscissa of absolute convergence of `−Z_Q'/Z_Q`.

**Lemma 18.4 (`PROVED`).**  `1 < σ_1 < ∞`, `Z(Ξ_Q) ⊂ \{|Re s−½| ≤ θ_Z\}`, the
zero multiset is symmetric under `ρ ↦ 1−ρ` and `ρ ↦ \barρ`,
`Σ_ρ(1+|Im ρ|)^{−2} < ∞`, and `N_{Ξ_Q}(T) = O(T\log T)`.

*Proof.*  `σ_1 > 1` is (X21).  Finiteness: `Z_Q(s)m_Q^{s} → r_Q(m_Q) > 0` as
`Re s → +∞`, so `Z_Q` has no zero in `Re s ≥ σ_0` for some `σ_0 < ∞`, and
neither `Γ` nor `½s(s−1)` has one; by `Ξ_Q(s) = Ξ_Q(1−s)`,
`Z(Ξ_Q) ⊂ \{1−σ_0 ≤ Re s ≤ σ_0\}`.  Symmetry under conjugation is reality on
`R`.  The counting bound and the summability are Jensen's formula for an entire
function of order `1`.  ∎  `PROVED`

**Theorem 18.5 (real zeros of `Λ_Q` in `(0,1)`; `PROVED`).**  For an integer
`k ≥ 1` let `Q_k(x,y) := x²+ky²`, of discriminant `−4k`.  Then for every
`σ_0 ∈ (0,1)` there is `k_0(σ_0)` such that for all `k ≥ k_0(σ_0)`,

    Λ_{Q_k}(σ_0) > 0 ,

and consequently `Λ_{Q_k}` — hence `Z_{Q_k}` and `Ξ_{Q_k}` — has a **real zero
in `(σ_0,1)`**.  By (X25b), `h(−4k) > 1` for all large `k`, so the family of
such `Q_k` with class number `> 1` is infinite.

*Proof.*  Here `D = 4k`, so `c_k := 2π/√D = π/√k`.  Apply (18.5) at `s = σ_0`:

    2Λ_{Q_k}(σ_0) = \frac1{σ_0−1} − \frac1{σ_0} + J_k(σ_0),\qquad
    J_k(σ_0) := ∫_1^∞A_k(u)\big(u^{σ_0−1}+u^{−σ_0}\big)du ,

with `A_k(u) = Σ'_{v≠0}e^{−c_kuQ_k(v)} > 0`.  The two vectors `v = (\pm1,0)`
have `Q_k(v) = 1`, so `A_k(u) ≥ 2e^{−πu/√k}` for `u ≥ 1`, whence
`J_k(σ_0) ≥ 2∫_1^∞e^{−πu/√k}u^{σ_0−1}du`.  As `k → ∞` the integrand increases
pointwise to `u^{σ_0−1}`, and `∫_1^∞u^{σ_0−1}du = ∞` because `σ_0−1 > −1`; by
monotone convergence `J_k(σ_0) → ∞`.  The remaining term
`\frac1{σ_0−1}−\frac1{σ_0}` depends only on `σ_0`.  Hence `Λ_{Q_k}(σ_0) > 0`
for `k ≥ k_0(σ_0)`.

On the other hand `Res_{s=1}Λ_{Q_k} = ½ > 0` (Theorem 18.3), the pole is simple
and `Λ_{Q_k}` is real-analytic on `(0,1)`, so `Λ_{Q_k}(σ) ∼ ½/(σ−1) → −∞` as
`σ ↑ 1`.  By the intermediate value theorem `Λ_{Q_k}(σ') = 0` for some
`σ' ∈ (σ_0,1)`.  Since `Γ(σ') > 0` and `(√D/2π)^{σ'} > 0`, also
`Z_{Q_k}(σ') = 0`, and `Ξ_{Q_k}(σ') = ½σ'(σ'−1)Λ_{Q_k}(σ') = 0`.  ∎  `PROVED`

**Corollary 18.6 (`K_Q > 0` is false; `PROVED`).**  For those `Q`, `K_Q` is not
everywhere positive, since `Ξ_Q(σ') = ∫K_Q(t)e^{(σ'−½)t}dt = 0` with
`K_Q ≢ 0`; and `Ξ_Q` does not satisfy the hypothesis "real and strictly positive
on `R`" of Proposition 12.6.  The expectation that `K_Q > 0` would follow from
the theta series, as `K > 0` does for `ξ`, is **`REFUTED`**.  ∎  `PROVED`

**Lemma 18.7 (real zeros are confined; `PROVED`).**  Every real zero of `Ξ_Q`
lies in the open interval `(0,1)`.  Writing
`θ_R := \sup\{|σ−½| : σ ∈ R,\ Ξ_Q(σ) = 0\}` (`θ_R := 0` if there is none), we
have `θ_R < ½`.

*Proof.*  For `σ > 1` the series `Z_Q(σ) = Σr_Q(n)n^{−σ}` converges absolutely
with non-negative terms, at least one positive, so `Z_Q(σ) > 0` and
`Ξ_Q(σ) = ½σ(σ−1)Λ_Q(σ) > 0`.  By `Ξ_Q(σ) = Ξ_Q(1−σ)` there is no real zero in
`σ < 0`.  At `σ ∈ \{0,1\}`, `Ξ_Q = ¼ ≠ 0`.  So the real zeros form a closed
subset of the compact set `[0,1]` missing its endpoints; being the zero set of a
nonzero entire function it is discrete, hence finite in `[0,1]`, hence
`θ_R = \max|σ−½| < ½`.  ∎  `PROVED`

Real zeros of `Λ_Q` therefore **exist** and lie strictly inside the polar strip
`|Re s−½| < ½`, while the zeros supplied by (X21) lie strictly outside it.  That
gap is exactly the room the following argument needs.

**Theorem 18.8 (the frame transfers to `Ξ_Q`; `PROVED`).**  Let
`α > \max\{θ_Z,\ σ_a−½\}` and `D^W_Q := D^W(α)`.  Then:

 (i) `K_Q ∈ D^W_Q`, `C_c^∞(R) ⊂ D^W_Q`, and `D^W_Q` is a `⋆`-algebra stable
     under `{}^∨` and `τ_u`;
 (ii) the **explicit formula** holds on `D^W_Q`: for real even `h ∈ D^W_Q`,

          Σ_{ρ∈Z(Ξ_Q)}Φ_h(ρ) = Φ_h(0)+Φ_h(1) − ⟨h,W^{(Q)}⟩ ,

      where `⟨h,W^{(Q)}⟩` is the Epstein arithmetic side, read off

          −\frac{Ξ_Q'}{Ξ_Q}(s) = −\frac1s − \frac1{s−1} − \log\frac{√D}{2π}
              − ψ(s) + Σ_{n≥2}c_Q(n)n^{−s},\qquad
          Σ_{n≥2}c_Q(n)n^{−s} := −\frac{Z_Q'}{Z_Q}(s)\ \ (Re\,s > σ_a),        (18.7)

      the zero sum absolutely convergent;
 (iii) `I_∞^{(Q)}` of (18.1) is a symmetric bilinear form on `D^W_Q`, equal to
       `⟨F⋆G^∨,W^{(Q)}⟩` symmetrized, and **named by no zero**;
 (iv) `D^W_Q = Λ_Q^{lin} ⊥ P^W_Q` with
      `Λ_Q^{lin} = \mathrm{span}(K_Q,K_{Q,odd})`,
      `K_{Q,odd} := (2\sinh(u/2))^{−1}(τ_uK_Q − τ_{−u}K_Q)` (independent of
      `u ≠ 0`), a hyperbolic plane of signature `(1,1)` reading only
      `(Φ_F(0),Φ_F(1))`, and `P^W_Q = \ker Φ_\bullet(0) ∩ \ker Φ_\bullet(1)`
      carrying `Ŵ^{(Ξ_Q)}` alone;
 (v) `K_Q` is the **Lorentzian normalization**: `I_∞^{(Q)}(K_Q,K_Q) = ⅛ > 0`,
     `Λ_Q^{lin} ⊂ (P^W_Q)^⊥`, and on the translation cone
     `Λ_Q^+ := \{Σ_jc_jτ_{u_j}K_Q : c_j ≥ 0\}` the Hodge-index inequality
     (18.2) holds **unconditionally**, with slack `z⁴(A−B)² = (A−B)²/256`,
     where `z := Ξ_Q(0) = ¼`, `A := Σ_jc_je^{u_j/2}`, `B := Σ_jc_je^{−u_j/2}`.

*Proof.*  (i) is Theorem 18.3(iii) with Lemma 11.2(i),(ii).

(ii)  `Ξ_Q` lies **outside** the class of Proposition 12.6 (it violates four of
its hypotheses: `Z > 0` on `R`, by Corollary 18.6; `c_n ≥ 0` and the density
bound, by Theorem 18.12; and (12.4), by Theorem 18.12(iii)).  So (ii) is a
separate statement, with hypotheses: `Ξ_Q` entire of order `1`, real on `R`,
symmetric (Theorem 18.3(iv)); `P = \{0,1\}` simple poles of `Ξ_Q'/Ξ_Q` with
`Ξ_Q(p) ≠ 0` (Theorem 18.3(v)); `Σ_{n≥2}c_Q(n)n^{−s}` absolutely convergent for
`Re s > σ_a < ∞`; `θ_Z < ∞` and `Σ_ρ(1+|Im ρ|)^{−2} < ∞` (Lemma 18.4);
`α > \max\{θ_Z,σ_a−½\}`.  **No sign hypothesis on `c_Q(n)` and no bound relating
`θ_Z` to `θ_P` is used.**  What the contour proof of Theorem 11.3 uses is a
single parameter, an abscissa `c` with `Φ_h` holomorphic on `L_c` and
`Σ_nc_Q(n)n^{−c}` absolutely convergent, together with `|Re ρ−½| ≤ α−ε`; both
are supplied by `α > \max\{θ_Z,σ_a−½\}` and any `c ∈ (σ_a,½+α)`, an interval
that is then nonempty, and `D^W(α)` still contains `K_Q` (double-exponential
decay, Theorem 18.3(iii)) and `C_c^∞(R)`.  The rectangle step then runs verbatim
with `P = \{0,1\}` interior; the separation step needs only `Ξ_Q(p) ≠ 0`, which
is `Ξ_Q(0) = Ξ_Q(1) = ¼` — **not** the stronger `Z > 0` on `R`, which is false
here by Theorem 18.5; absolute convergence of the zero sum is
`|Φ_h(ρ)| = O(|Im ρ|^{−2})` by (11.2) (legitimate since `|Re ρ−½| ≤ θ_Z < α`)
together with Lemma 18.4.

(iii),(iv) are Theorems 11.5, 11.10 and 11.11 read for `P = \{0,1\}` with
`Ξ_Q(p) = ¼`; every step there mentions `P` only by name.

(v) is the two-point equimodular computation with `θ = ½` and
`z := Ξ_Q(½±½) = ¼`: `I^{(Q)}(X,X) = 2z²AB`, `I^{(Q)}(X,K_Q) = z²(A+B)`,
`I^{(Q)}(K_Q,K_Q) = 2z²`, so (18.2) reads `4z⁴AB ≤ z⁴(A+B)²`, i.e.
`(A−B)² ≥ 0`, with slack `z⁴(A−B)² = (A−B)²/256`.  ∎  `PROVED`

**Remark 18.8a (the one step that does not transfer).**  Theorem 11.14
(bounded density, hence ampleness) is proved by dominating both `|e^{(p−½)u}|`
and `|e^{(ρ−½)u}|` by the weight `Σ_pZ(p)e^{(p−½)u} ≍ e^{θ_P|u|}`; substitution
(S3) of §12.5 records that the two exponents agree, which is the structural
reason the bound closes for `ξ` and for `Ξ_a`.  For `Ξ_Q` they do not agree
(`θ_Z > ½ = θ_P`).  Hence Theorem 11.14, the ample cone, and Theorem 12.3 are
**not** available for `Ξ_Q`; nothing below uses them for `Ξ_Q`.  The argument of
Theorem 18.10 needs neither.

#### 18.2.3 Hodge index fails for `Ξ_Q`

For `T > 0` put `h_T(t) := (1−|t|/T)_+ = F_T⋆F_T^∨` with
`F_T := T^{−1/2}1_{[−T/2,T/2]}`, so
`Φ_{h_T}(s) = 4\sinh²((s−½)T/2)/(T(s−½)²)`; write `w_ρ := ρ−½` and
`W_Q(h_T) := Σ_{ρ∈Z(Ξ_Q)}Φ_{h_T}(ρ) = −Ŵ^{(Ξ_Q)}(F_T,F_T)`.

**Lemma 18.9 (`PROVED`).**  For `Re z > θ_Z` the integral
`G_Q(z) := ∫_0^∞T\,W_Q(h_T)e^{−zT}dT` converges absolutely and

    G_Q(z) = \frac{2}{z²}\cdot\frac{Ξ_Q'}{Ξ_Q}\Big(\tfrac12+z\Big) .

*Proof.*  Three inputs.  (a) `|Φ_{h_T}(ρ)| ≤ 4e^{|Re w_ρ|T}/(T|w_ρ|²)` and
`Σ_ρ|w_ρ|^{−2} < ∞` (Lemma 18.4), which give absolute convergence for
`Re z > θ_Z` and justify interchanging sum and integral.  (b) The elementary
Laplace identity `∫_0^∞(2\cosh(wT)−2)e^{−zT}dT = 2w²/(z(z²−w²))` for
`Re z > |Re w|`, applied termwise after writing
`TΦ_{h_T}(ρ) = (2\cosh(w_ρT)−2)/w_ρ²`.  (c) Hadamard's factorization for an
entire function of order `1` with `Ξ_Q(s) = Ξ_Q(1−s)`, which gives
`(Ξ_Q'/Ξ_Q)(½+z) − (Ξ_Q'/Ξ_Q)(½−z) = 2zΣ_ρ(z²−w_ρ²)^{−1}` and
`(Ξ_Q'/Ξ_Q)(½−z) = −(Ξ_Q'/Ξ_Q)(½+z)`.  Each is available for `Ξ_Q` by Theorem
18.3(iv) and Lemma 18.4; summing (b) over `ρ` and inserting (c) gives the
displayed identity.  ∎  `PROVED`

**Theorem 18.10 (Hodge index fails for `Ξ_Q`; `PROVED`).**  Let `Q` be principal
with `h(−D) > 1`.  Then there exists `T > 0` with `W_Q(h_T) < 0`; and for every
small `δ > 0` the class `F_T^{(δ)} := F_T⋆ψ_δ ∈ C_c^∞(R) ⊂ D^W_Q` (`ψ_δ` a
standard even non-negative mollifier) is **effective, even, smooth and compactly
supported** and satisfies

    Ŵ^{(Ξ_Q)}\big(F_T^{(δ)},F_T^{(δ)}\big) > 0 ,\quad\text{i.e.}\quad
    I_∞^{(Q)}(F,F)\,I_∞^{(Q)}(K_Q,K_Q) > I_∞^{(Q)}(F,K_Q)^2\ \text{ at }F = F_T^{(δ)} ,

so the Hodge-index inequality (18.2) **fails** on the effective cone
`E_Q = \{F ∈ D^W_Q : F ≥ 0\}` and on `C_c^∞(R)`.

*Proof.*  Suppose `f(T) := T\,W_Q(h_T) ≥ 0` for every `T > 0`.  By Lemma 18.9
the Laplace integral `G_Q(z) = ∫_0^∞f(T)e^{−zT}dT` converges for `Re z > θ_Z`,
so its abscissa of convergence `σ_c` is finite.  By Landau's theorem **(X20)**,
`z = σ_c` is a singular point of the analytic continuation of `G_Q`.

Now `G_Q(z) = 2z^{−2}(Ξ_Q'/Ξ_Q)(½+z)` is meromorphic on `C`, with poles exactly
at `z = w_ρ` (`ρ ∈ Z(Ξ_Q)`) and possibly at `z = 0`.  Its **real** singularities
are therefore contained in `\{0\} ∪ \{σ−½ : σ ∈ R,\ Ξ_Q(σ) = 0\}`, a set
contained in `[−θ_R,θ_R]` with `θ_R < ½` by Lemma 18.7.  Hence
`σ_c ≤ θ_R < ½`, and `G_Q` is analytic in `Re z > θ_R`.

But by **(X21)** there is `ρ_0 ∈ Z(Ξ_Q)` with `Re ρ_0 > 1`, so `G_Q` has a pole
at `z = w_{ρ_0}` with `Re w_{ρ_0} > ½ > θ_R`.  Contradiction.  Hence
`W_Q(h_T) < 0` for some `T > 0`.

Transport to `D^W_Q`: `Φ_{F_T^{(δ)}}(s) = Φ_{F_T}(s)Φ_{ψ_δ}(s)`, with
`Φ_{ψ_δ}` entire, bounded on the strip `|Re s−½| ≤ θ_Z` uniformly in small
`δ`, and `Φ_{ψ_δ} → 1` pointwise; by dominated convergence (legitimate by Lemma
18.4) `Σ_ρΦ_{F_T^{(δ)}}(ρ)Φ_{F_T^{(δ)}}(1−ρ) → W_Q(h_T) < 0` as `δ → 0`, i.e.
`Ŵ^{(Ξ_Q)}(F_T^{(δ)},F_T^{(δ)}) > 0` for small `δ`.  Since `F_T^{(δ)}` is even,
the Hodge-index inequality at `F_T^{(δ)}` **is** the statement `Ŵ ≤ 0`
((18.2) of §18).  It fails.  ∎  `PROVED`

**Remark 18.10a (which zero fact is used, and why Voronin's zeros would not
suffice).**  The proof uses **only** (X21) in its strong form: the existence of
a zero with `Re ρ > 1`.  It would **not** go through with zeros in
`½ < Re ρ < 1` alone (Voronin): those give a pole of `G_Q` at
`Re z ∈ (0,½)`, and the conclusion `σ_c ≤ θ_R` excludes such a pole only if
`θ_R < Re w_{ρ_0}` — which is not known, since Theorem 18.5 shows `θ_R` can be
positive and no lower bound on `Re w_{ρ_0} − θ_R` is available.  Whether a
different argument could run on zeros in the strip is `OPEN`.

**Theorem 18.11 (the witness cannot lie in the translation cone; `PROVED`).**
By Theorem 18.8(v) the Hodge-index inequality holds unconditionally on
`Λ_Q^+`, with slack `z⁴(A−B)²`.  Hence the witness of Theorem 18.10 must, and
does, come from the effective cone `E_Q` and not from the Frobenius translation
cone.  The content of Theorem 18.10 is therefore: **equimodularity of the polar
block, the canonical class, the functional equation and non-negative Dirichlet
coefficients of the datum are jointly insufficient for Hodge index.**  ∎
`PROVED`

**Theorem 18.12 (what the Euler product adds; `PROVED`).**  Let `Q` be principal
with `h(−D) > 1` and let `c_Q(n)` be defined by (18.7).  Then:

 (i) it is **false** that `c_Q(n) ≥ 0` for all `n`;
 (ii) for every `β < σ_1` it is false that `Σ_{n≤x}|c_Q(n)| = O(x^{β})`;
 (iii) `θ_Z > θ_P`, i.e. hypothesis (12.4) of Proposition 12.6 fails for `Ξ_Q`
       with `θ = θ_P = ½`.

*Proof.*  (iii) is (X21): `θ_Z = σ_1−½ > ½ = θ_P`.

(i)  Suppose `c_Q(n) ≥ 0` for every `n`.  The Dirichlet series
`Σ_nc_Q(n)n^{−s}` represents `−Z_Q'/Z_Q`, whose singularities are exactly the
zeros and poles of `Z_Q`; its abscissa of convergence `σ_c` satisfies
`σ_c ≥ σ_1 > 1`, since the function is not holomorphic in any half-plane
`Re s > β` with `β < σ_1` (it has poles at the zeros supplied by (X21), whose
real parts have supremum `σ_1`).  By Landau's theorem for Dirichlet series with
non-negative coefficients — **(X20)** in its Dirichlet-series form —
`s = σ_c` is a singularity of the function.  But on the real half-line `σ > 1`,
`Z_Q(σ) = Σ_nr_Q(n)n^{−σ}` is a convergent sum of non-negative terms, not all
zero, hence `> 0`, and `Z_Q` is holomorphic there; so `−Z_Q'/Z_Q` is holomorphic
at every real `σ > 1`, in particular at `σ_c > 1`.  Contradiction.  Hence some
`c_Q(n) < 0`.

(ii)  If `Σ_{n≤x}|c_Q(n)| = O(x^{β})` with `β < σ_1`, then by partial summation
the Dirichlet series converges absolutely in `Re s > β`, so `−Z_Q'/Z_Q` would be
holomorphic there, contradicting the existence of zeros of `Z_Q` with real part
arbitrarily close to `σ_1`.  (Nothing is claimed about the **signed** partial
sums `Σ_{n≤x}c_Q(n)`.)  ∎  `PROVED`

**Remark 18.12a (`ζ_K` is a product where `Z_Q` is a sum).**  `r_Q(n)` is not
multiplicative once `h(−D) > 1`: by the Hecke–Dirichlet decomposition
`Z_Q(s) = \frac1hΣ_χ\overlineχ(𝔄)L(s,χ)` is a nontrivial linear combination of
`h ≥ 2` distinct Euler products, and such a combination is not itself an Euler
product (its coefficient function is multiplicative iff the combination
collapses to a single `L(s,χ)`, which forces `h = 1`).  Correspondingly
`c_Q(n)` is not supported on prime powers.  For `ξ` and for every `ξ_K` the
coefficients of `−Z'/Z` are von Mangoldt coefficients of an Euler product,
`c(n) = Λ_K(n) ≥ 0`; and row B's form of that statement is the inverse-semigroup
law `Frob_m ⋆ Frob_n = Frob_{mn}` (Paper 44 Theorem 3ter.4(i)) with
`Frob_n ⋆ Frob_n^† = Δ^{(n)}` (Theorem 3ter.6(ii)) and bidegree
`M(Frob_n) = (n^{1/2},n^{−1/2})`.  `RESTATEMENT`

#### 18.2.4 The axiom list, the transfer lemma, and T2

**Definition 18.13 (the axiom list `𝔄`).**  Let `Z` be a function of a complex
variable and `P ⊂ R` a finite set.

* **A1 (analytic frame).**  `Z` is entire of order `1`, real on `R`, and
  `Z(s) = Z(1−s)`.
* **A2 (canonical class).**  There is `K_Z ∈ D^W(α)` for some `α > ½` with
  `Φ_{K_Z} = Z`; `K_Z` is even; `τ_uK_Z ∈ D^W(α)` for all `u`.
* **A2⁺ (polar positivity).**  `Z(p) > 0` for every `p ∈ P`, so the weight
  `Σ_{p∈P}Z(p)e^{(p−½)t}` is strictly positive on `R` and `\deg_Z` is strictly
  positive on nonzero effective classes.
* **A3 (equimodular polar block).**  `P = 1−P ⊂ R`, all poles of `Z'/Z` on `P`
  simple, and `|p−½| = θ_P` is the same for every `p ∈ P`.
* **A4 (non-negative Dirichlet coefficients of the datum).**
  `Z(s) = E(s)·Σ_{n≥n_0}a_nn^{−s}` with `a_n ≥ 0`, `a_{n_0} > 0`, the series
  convergent in some half-plane, and `E` a fixed elementary factor: a finite
  product of `Γ`-factors, exponentials `q^{s}` (`q > 0`) and the polynomial
  `½s(s−1)`.
* **A5 (explicit formula).**  There is `α > ½` such that on `D^W(α)` the zero
  sum `Σ_ρΦ_h(ρ)` converges absolutely for every real even `h`, and
  `Σ_ρΦ_h(ρ) = Σ_{p∈P}Φ_h(p) − ⟨h,W^{(Z)}⟩`, with `⟨h,W^{(Z)}⟩` the arithmetic
  side read off `−Z'/Z`.
* **A6 (splitting).**  `D^W(α) = Λ_Z ⊥ P^W_Z` with
  `Λ_Z = \mathrm{span}(K_Z,K_{Z,odd})` of signature `(1,1)` and
  `I_∞^{(Z)}(K_Z,K_Z) > 0`.
* **A7 (zero strip = polar strip).**  `\sup_ρ|Re ρ − ½| ≤ θ_P`.
* **A8 (Euler product with non-negative atoms).**
  `−Z'/Z(s) = ∓A_P(s) + (\text{archimedean}) + Σ_nc(n)n^{−s}` with `c(n) ≥ 0`
  supported on prime powers and `Σ_{n≤x}c(n) = O(x^{½+θ_P})`.
* **A9 (positivity on the reals).**  `Z(σ) > 0` for every `σ ∈ R`; equivalently,
  given A2⁺ and the functional equation, `Z` has no real zero.  (`K_Z > 0` is a
  **sufficient** condition, since `Z(σ) = ∫K_Z(t)e^{(σ−½)t}dt`, and is how A9 is
  verified for `ξ` and for `Ξ_a`; the converse does not hold and is not used.)

The unconditional Hodge-index inequality on the translation cone `Λ_Z^+` is a
**consequence** of A1–A3 and A6 (Theorem 18.8(v) is the instance for `Ξ_Q`), not
an axiom.

**Theorem 18.14 (the verification table; `PROVED`).**

| | A1 | A2 | A2⁺ | A3 | A4 | A5 | A6 | A7 | A8 | A9 | Hodge index |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ξ` | ✓ | ✓ | ✓ | ✓ (`θ_P=½`) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **`OPEN`** (= RH) |
| `Ξ_a`, `0<a<½` | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ (`θ_P=½+a`) | ✓ | ✓ | **fails** |
| `Ξ_Q`, principal `Q`, `h(−D)>1` | ✓ | ✓ | ✓ | ✓ (`θ_P=½`) | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | **fails** (Thm 18.10) |
| `ξ_K`, `K` a number field | ✓ | ✓ | ✓ | ✓ (`θ_P=½`) | ✓ | ✓ | ✓ | ✓ | ✓ | **`OPEN`** | **`OPEN`** (= GRH for `ζ_K`) |

*Proof.*  Row `ξ`: §§11–12, with A7 and A8 supplied by the Euler product
(Remark 18.14a) and A9 by `K > 0` (Theorem 11.7(i)).  Row `Ξ_a`: Remark 11.8a
and Proposition 12.6 for A1, A2, A2⁺, A4–A9, and Theorem 12.4 for the failure of
the conclusion; A3 fails because `p−½ ∈ \{\pm(½−a),\pm(½+a)\}`.  Row `Ξ_Q`:
A1, A2, A2⁺, A3 are Theorem 18.3(ii)–(vi); A4 is `r_Q(n) ≥ 0`; A5, A6 are
Theorem 18.8(ii),(iv); A7, A8 fail by Theorem 18.12(iii),(i),(ii); A9 fails by
Corollary 18.6; Hodge index fails by Theorem 18.10.  Row `ξ_K`: Theorem 18.16
below; A9 is `OPEN` because a real zero of `ζ_K` in `(0,1)` — a Landau–Siegel
zero — is not excluded unconditionally for real quadratic `K` **(X24)**.  ∎
`PROVED`

**Remark 18.14a (A7 and A8 for `ξ` *are* the Euler product).**  For `ξ`, A8 is
`c(n) = Λ(n) ≥ 0`, the Euler product read logarithmically, with
`Σ_{n≤x}Λ(n) = ψ(x) = O(x)` by Chebyshev.  A7 for `ξ` is "`ζ` has no zero in
`Re s ≥ 1`": in `Re s > 1` this is immediate from the Euler product (an
absolutely convergent product of nonzero factors), and on `Re s = 1` it is
Hadamard–de la Vallée Poussin, whose only known proofs use the Euler product,
through the `3+4\cos σ+\cos 2σ` inequality applied to the non-negative
coefficients of `−ζ'/ζ`.  No proof of A7 for `ξ` avoiding the Euler product is
known.  `RESTATEMENT` + `CLASSICAL`

**Lemma 18.15 (Transfer Lemma; `PROVED`).**  Let `𝔇` be the data list
`(P,\ D^W(α),\ ⋆,\ {}^∨,\ τ_\bullet,\ \{\cdot ≥ 0\},\ K_Z,\ 𝓝_∞^{(Z)},\
I_∞^{(Z)},\ \deg_Z)` of (12.3) extended by `I_∞^{(Z)}` and `\deg_Z` — **`Z`
itself is not in the list**.  Let `𝔖` be the set of statements `S(𝔇)` about
these data derivable from A1–A6 together with A2⁺ alone, a derivation being a
finite chain of steps each of which invokes only A1–A6, A2⁺ and the definitions
in `𝔇`.  Then every `S ∈ 𝔖` that holds for `Z = ξ` holds for `Z = Ξ_Q`.

*Proof.*  By Theorem 18.14, `Ξ_Q` (for principal `Q` with `h(−D) > 1`) satisfies
A1–A6 and A2⁺, and every datum of `𝔇` is constructed for it (Theorems 18.3,
18.8).  A derivation invoking only those axioms and those data is a derivation
for every structure satisfying them, hence for `Ξ_Q`.  ∎  `PROVED`

**Theorem 18.16 (T2, the Epstein constraint; `METHOD-CONSTRAINT`).**  *There is
no derivation of the Hodge-index inequality (18.2) for `ξ` from the axioms
A1–A6 together with A2⁺ and the data `𝔇` alone.*

*Proof.*  By Lemma 18.15 such a derivation would yield the Hodge-index
inequality for `Ξ_Q`, which fails by Theorem 18.10.  ∎  `METHOD-CONSTRAINT`
(the falsifier half, Theorem 18.10, is `PROVED`)

**Consequently, any proof of the sign must invoke, at some line, one of A7, A8,
A9** — the zero-free half-plane `Re s ≥ 1`, the non-negativity of the von
Mangoldt coefficients, or the positivity of `Z` on the real axis.  Combined with
Theorem 12.4 and Restatement 12.4a, which show that A3 must also be invoked
(`Ξ_a` satisfies everything but A3 and violates the conclusion), and with
Theorem 18.1:

> **a proof of the sign must use A3 (equimodularity), must use at least one of
> A7 / A8 / A9, and must be uniform in the number field.**  A7 and A8 for `ξ`
> are theorems *about the Euler product*; A9 for `ξ_K` is open.  `Ξ_a` pins A3;
> `Ξ_Q` pins A7 / A8 / A9.

**Corollary 18.17 (the A9 escape route and its price; `PROVED`).**  A derivation
that evades `Ξ_Q` by invoking A9 — "`Z > 0` on `R`", equivalently "no real
zeros" — is **not field-uniform** unless it also proves that `ζ_K` has no real
zero in `(0,1)` for every number field `K`, i.e. unless it disposes of
Landau–Siegel zeros for real quadratic fields.

*Proof.*  For `ξ_K`, A9 says exactly that `ξ_K` has no real zero; by the
functional equation and `ξ_K(0) = ξ_K(1) = r/2 > 0` (Theorem 18.18(i)) this is
equivalent to `ζ_K` having no real zero in `(0,1)`, i.e. to the absence of a
Siegel zero for `ζ_K`.  That statement is not known for `K` real quadratic
**(X24)**, and is `OPEN` in the table of Theorem 18.14.  By Theorem 18.1, a
proof of the sign from structure shared by all `ζ_K` proves GRH for all `ζ_K`;
a proof that uses A9 is a proof presupposing a statement not known for all
`ζ_K`.  ∎  `PROVED`

**Remark 18.17a.**  T2 is a negative statement about derivations; with Theorem
3.7 it proves neither RH nor its negation.  Theorem 18.10 asserts the failure of
the Hodge-index inequality for `Ξ_Q`, a function that is **not** `ξ` and that
has proven off-line zeros.  No sign for `ξ` is asserted anywhere in §18.2.  T2
also names its own distinguishing properties (A7, A8, A9) explicitly, and each
is shared by `ξ` with every `ξ_K` except A9, which is open for `ξ_K`: so T2 does
not covertly distinguish `Q` from a number field.

---

### 18.3 The field-uniform frame, and base change

Let `K` be a number field of degree `d = r_1+2r_2`, discriminant `d_K`, class
number `h_K`, regulator `R_K`, with `w_K` roots of unity.  Put

    Λ_K(s) := |d_K|^{s/2}\big(π^{−s/2}Γ(s/2)\big)^{r_1}\big((2π)^{−s}Γ(s)\big)^{r_2}ζ_K(s),
    ξ_K(s) := ½\,s(s−1)\,Λ_K(s) .

**Theorem 18.18 (the frame for every number field; `RESTATEMENT` + `PROVED`).**
`Λ_K` is meromorphic with simple poles exactly at `s = 0,1` and
`Λ_K(s) = Λ_K(1−s)`, and
`r := Res_{s=1}Λ_K = 2^{r_1}h_KR_K/w_K > 0` (**(X25a)**).  Then:

 (i) `ξ_K` is entire of order `1`, real on `R`, `ξ_K(s) = ξ_K(1−s)`, and
     `ξ_K(0) = ξ_K(1) = r/2 > 0`;
 (ii) `P = \{0,1\}`, `θ_P = ½`: **every `ζ_K` is equimodular**;
 (iii) there is a real even `K_K ∈ D^W(α)` **for every `α > 0`** with
       `Φ_{K_K} = ξ_K`, namely

           K_K(t) := \frac1{2π}∫_R ξ_K(½+iτ)\,e^{−iτt}\,dτ ;

 (iv) with `\deg_KF := Φ_F(0)+Φ_F(1)` one has
      `I_∞^{(K)}(F,K_K) = \frac r2\deg_KF` and
      `I_∞^{(K)}(K_K,K_K) = r²/2 > 0`; `D^W = Λ_K^{lin} ⊥ P^W_K` with
      `Λ_K^{lin}` hyperbolic of signature `(1,1)`, and the Hodge-index
      inequality holds unconditionally on the translation cone `(Λ_K^{lin})^+`;
 (v) axioms A1–A6, A2⁺, A7 and A8 hold; **A9 is `OPEN`** for `K` real quadratic
     and `PROVED` for `K` imaginary quadratic;
 (vi) Theorem 12.3 holds verbatim for `K`: a function `h⁰_K` with (a), (b′),
      (c) gives `I_∞^{(K)}(F,F) ≤ 0` on primitive `F ∈ C_c^∞(R)`, hence GRH for
      `ζ_K`.

*Proof.*  (i), (ii), (iv), (vi) are the substitutions (S1)–(S4) of §12.5 with
`P = \{0,1\}`, `Z(p) = r/2`, `θ_P = θ_Z = ½`; every step of §§11–12 listed there
as verbatim is verbatim, and the bounded-density step (Theorem 11.14) closes
because `θ_Z = θ_P` — which for `ζ_K` is A7, i.e. `ζ_K(s) ≠ 0` for `Re s ≥ 1`,
classical from the Euler product of `ζ_K` and Hecke's extension of
Hadamard–de la Vallée Poussin.

(iii)  Two classical inputs, both in **(X25a)**.  First, `ξ_K` is of finite
order in every vertical strip: for each `A > 0` there are `C_A, N_A` with
`|ξ_K(σ+iτ)| ≤ C_A(1+|τ|)^{N_A}e^{πd|τ|/4}` uniformly on `|σ−½| ≤ A`
(Phragmén–Lindelöf applied to the functional equation and the half-plane of
absolute convergence; the bound is stated for the entire `ξ_K`, since for `ζ_K`
itself it fails at the pole).  Second, Stirling:
`|Γ(σ/2+iτ/2)|^{r_1}|Γ(σ+iτ)|^{r_2} = O_A\big((1+|τ|)^{M_A}e^{−πd|τ|/4}\big)`
uniformly on `|σ−½| ≤ A`.  With the polynomial factor `½s(s−1)` and
`|d_K|^{s/2}` these give, for every `A > 0`,

    |ξ_K(σ+iτ)| ≤ C'_A(1+|τ|)^{M'_A}e^{−πd|τ|/4}\quad\text{uniformly on }|σ−½| ≤ A. (18.8)

*The integral converges and is smooth.*  By (18.8) at `σ = ½` the integral
defining `K_K` converges absolutely, as does `∫τ^jξ_K(½+iτ)e^{−iτt}dτ` for every
`j`; so `K_K ∈ C^∞(R)` with
`K_K^{(j)}(t) = \frac1{2π}∫(−iτ)^jξ_K(½+iτ)e^{−iτt}dτ`.

*Reality and evenness.*  `ξ_K` is real on `R` and `ξ_K(s) = ξ_K(1−s)`, so
`ξ_K(½+iτ) = \overline{ξ_K(½−iτ)} = ξ_K(½−iτ)`: the function
`τ ↦ ξ_K(½+iτ)` is real and even, hence `K_K` is real and even.

*Decay.*  Fix `A > 0`.  `ξ_K` is entire, and by (18.8) the integrand
`ξ_K(s)e^{−(s−½)t}` tends to `0` uniformly on the horizontal segments
`Im s = \pm X`, `|Re s−½| ≤ A`, as `X → ∞`.  Cauchy's theorem therefore allows
the shift of the line `Re s = ½` to `Re s = ½+A`:

    K_K(t) = \frac1{2π}∫_Rξ_K(½+A+iτ)e^{−(A+iτ)t}dτ ,\qquad |K_K(t)| ≤ C''_Ae^{−At} ;

shifting instead to `Re s = ½−A` gives `|K_K(t)| ≤ C''_Ae^{At}`, so
`|K_K(t)| ≤ C''_Ae^{−A|t|}` for every `A > 0`, and likewise for each
`K_K^{(j)}` (the extra factor `τ^j` is absorbed into `(1+|τ|)^{M'_A}`).  Hence
`K_K ∈ D^W(α)` for every `α`, and so are its derivatives and translates.

*The transform.*  `K_K` decays faster than any exponential, so `Φ_{K_K}` is
entire; by Fourier inversion `Φ_{K_K}(½+iτ) = ξ_K(½+iτ)` for all real `τ`, and
two entire functions agreeing on a line agree.  **No theta series, no
fundamental domain for the units and no ideal-class decomposition is used**; the
argument applies verbatim to any `Z` satisfying A1 with exponential decay on
vertical strips, and in particular re-proves the existence — though not the
explicit form — of `K_Q`.

(v)  A1–A6 and A2⁺ follow from (i)–(iv); A4 is
`a_n = \#\{\mathfrak a : N\mathfrak a = n\} ≥ 0`; A7 and A8 come from the Euler
product of `ζ_K`.  For `K` imaginary quadratic, `ζ_K = ζ·L(\cdot,χ_{−D})` with
`χ_{−D}` a real **odd** character, and `L(σ,χ_{−D}) > 0` on `(0,1)` because a
real primitive odd character has no real zero there **(X24)**, while
`ζ(σ) < 0` on `(0,1)`; so `Λ_K(σ) < 0` and `ξ_K(σ) = ½σ(σ−1)Λ_K(σ) > 0`, i.e.
A9 holds.  For `K` real quadratic `χ_{d_K}` is even and no unconditional
exclusion of a real zero is known **(X24)**.  ∎  `RESTATEMENT` + `PROVED`

**Remark 18.18a (what changes with `K`).**  (1) The archimedean block is a sum
over the archimedean places: `r_1` copies of `½Re ψ(¼+iτ/2) − ½\log π` and
`r_2` copies of `Re ψ(½+iτ) − \log 2π`.  (2) The factor `|d_K|^{s/2}`
contributes a **conductor term** `½\log|d_K|·h(0)` to the explicit formula, with
no analogue for `Q`; it is the only place `|d_K|` enters.  (3) The units and the
regulator enter only through `r = 2^{r_1}h_KR_K/w_K`, i.e. only through the
normalization constants `I_∞^{(K)}(K_K,K_K) = r²/2` and `\deg_KK_K = r`; they do
**not** enter the primitive zero form `Ŵ^{(ξ_K)}` at all.  (4) Nothing else
changes: the polar block is two-dimensional and equimodular with `θ_P = ½` for
every `K`, and the splitting, the Lorentzian normalization and the transfer
theorem are the same statements with `½ ↦ r/2`.

**Lemma 18.19 (conjugate packets are self-dual; `PROVED`).**  Let `L/K` be
finite Galois with group `G`.  Group the nontrivial irreducible characters of
`G` into packets: `\{χ\}` if `χ = \barχ`, and `\{χ,\barχ\}` otherwise, and put
`Λ_{[χ]} := Λ(\cdot,χ)` in the first case, `Λ(\cdot,χ)Λ(\cdot,\barχ)` in the
second.  Then `Λ_{[χ]}` is real on `R` and satisfies
`Λ_{[χ]}(s) = ε_{[χ]}Λ_{[χ]}(1−s)` with `ε_{[χ]} = \pm1`; in particular its zero
multiset is invariant under `ρ ↦ 1−ρ`, which is all that Lemma 18.9 uses.

*Proof.*  The Artin functional equation is `Λ(s,χ) = W(χ)Λ(1−s,\barχ)` with
`|W(χ)| = 1` and `W(χ)W(\barχ) = 1` **(X25a)**.  For `χ ≠ \barχ`,
`Λ_{[χ]}(1−s) = Λ(1−s,χ)Λ(1−s,\barχ) = W(\barχ)^{−1}Λ(s,\barχ)·W(χ)^{−1}Λ(s,χ)
= Λ_{[χ]}(s)`.  For `χ = \barχ` real, `W(χ) = \pm1` and
`Λ(s,χ) = W(χ)Λ(1−s,χ)`, so `ε_{[χ]} = W(χ) = \pm1` and the zero multiset is
`ρ ↦ 1−ρ`-invariant in either case.  Reality on `R` follows from
`\overline{Λ(\bar s,χ)} = Λ(s,\barχ)`.  ∎  `PROVED`

**Theorem 18.20 (base change: additivity of the primitive zero form).**  Let
`L/K` be finite Galois with group `G`, and let `F, G ∈ D^W(α)` with `α` large
enough for `ξ_L`.  Then, with the sum taken over conjugate packets,

    Ŵ^{(ξ_L)}(F,G) = Ŵ^{(ξ_K)}(F,G) + Σ_{[χ]≠1}χ(1)\,Ŵ^{(Λ_{[χ]})}(F,G) ,      (18.9)

and, the polar blocks of `ξ_L` and `ξ_K` being **equal** (weight one,
`P = \{0,1\}`),

    I_∞^{(L)}(F,G) = I_∞^{(K)}(F,G) + Σ_{[χ]≠1}χ(1)\,Ŵ^{(Λ_{[χ]})}(F,G) .      (18.10)

**All the extra terms are primitive**: each `Ŵ^{(Λ_{[χ]})}` carries no polar
block.  The statement is **`PROVED`** unconditionally when `L/K` is **abelian**,
and **`PROVED-CONDITIONAL` on Artin holomorphy (X25)** for general `L/K`.

*Proof.*  Artin's factorization gives
`ζ_L(s) = ζ_K(s)\prod_{χ≠1}L(s,χ,L/K)^{χ(1)}`, and by the
conductor–discriminant formula the completed functions factor **exactly**, with
no extra constant **(X25a)**:

    Λ_L(s) = Λ_K(s)\prod_{χ≠1}Λ(s,χ)^{χ(1)},\qquad
    ξ_L(s) = ξ_K(s)\prod_{χ≠1}Λ(s,χ)^{χ(1)} .                                  (18.11)

When `L/K` is abelian every `χ` is one-dimensional, `χ(1) = 1`, and
`Λ(\cdot,χ)` is a Hecke L-function of a primitive character, hence entire for
`χ ≠ 1`; in general, entirety of each factor is Artin holomorphy **(X25)**.
Under that hypothesis the zero multiset of `ξ_L` is the disjoint union, with
multiplicity, of that of `ξ_K` and `χ(1)` copies of that of each `Λ(\cdot,χ)`,
equivalently of the packets `Λ_{[χ]}`.  Each factor is entire of order `1` with
zeros in a bounded vertical strip, so each zero sum converges absolutely on
`D^W(α)` by the argument of Lemma 18.4, and the sum may be split, giving (18.9);
(18.10) follows since the polar blocks agree.  The primitivity of the extra
terms is the statement that the `Λ(\cdot,χ)`, `χ ≠ 1`, have no pole.  ∎

**Remark 18.20a (what base change gives, and what it does not).**  (18.9) is an
exact **additivity**, not a monotonicity: `Ŵ^{(ξ_L)}(F,F) ≤ 0` for one `F`
neither implies nor is implied by `Ŵ^{(ξ_K)}(F,F) ≤ 0`, the packet terms having
no sign a priori.  Quantified over all even `F ∈ C_c^∞(R)` it becomes an
equivalence: `Ŵ^{(ξ_L)}(F,F) ≤ 0` for all such `F` iff the same holds for `ξ_K`
and for every packet — `⇐` because a sum of non-positive terms is non-positive,
`⇒` by applying Lemma 18.9 and the argument of Theorem 18.10 to each packet,
which is legitimate by Lemma 18.19 and is exactly why the decomposition is taken
over packets and not over individual `χ` (for complex `χ` the individual
`Λ(\cdot,χ)` has no self-dual functional equation and A1 fails for it).  That
direction carries, for each packet, the real-zero hypothesis A9 that the Landau
step needs, which for a real even `χ` is again Landau–Siegel and `OPEN`
**(X24)**.  Finally, (18.9) is an identity between forms evaluated at the
**same** test class: the carrier `D^W(α)` is the same real function space for
every `K`, since the Weil class lives on the modulus variable `t ∈ R`.  So base
change imposes **no new relation on a single `I_∞^{(K)}`**; it relates different
`Z`'s on one carrier.  `PROVED` for the first sentence; `PROVED-CONDITIONAL`
for the equivalence.

---

### 18.4 The fork: what the earlier purported proof establishes

The repository's earlier document
`03-research/phase-65-signature-continuity/RH-PROOF.md` assembles a chain ending in
a Vitali/Montel step.  The following proposition determines its status; the full
audit is not reproduced here.

**Proposition 18.21 (the fork; `PROVED`).**  In that chain there are exactly two
objects to which the Vitali/Montel step could be applied, and **neither carries
both of the premises the step needs**:

| object | uniform Montel bound | identification of the limit |
|---|---|---|
| the sourced channel matrix `G_P^∘` | **available** | **withdrawn**: the cancellation was asserted |
| the renormalized trace `M_P = −∂_z\log D_P^∘ − E_P'/E_P` | **not available** | **available**, by the trace-log identity |

Consequently the chain is **`REFUTED` as a proof of RH**, and is correct as a
**reduction** of RH to the uniformity in `P` of a renormalized family.

*Proof.*  Row 1, left: for `φ_α ⊥ H` and `A_P` self-adjoint,
`|G_P^∘(z)_{αβ}| = |⟨Q_P(A_P−z)^{−1}Q_Pι_Pφ_β,ι_Pφ_α⟩| ≤
‖ι_Pφ_α‖‖ι_Pφ_β‖/|Im z| ≤ C_F/|Im z|` uniformly in `P`, the source norms being
bounded uniformly and the passage to the pole-relative space preserving the
bound in both of its readings — orthogonal projection, `‖Q_Pu‖ ≤ ‖u‖`; or Schur
complement of a positive form, `S := K_{∘∘} − K_{∘H}K_{HH}^{−1}K_{H∘} ⪯
K_{∘∘}`, so `‖u‖_S ≤ ‖u‖_{K_{∘∘}}`.  Row 1, right: the chain's own correction
withdraws the arbitrary-pairing realization, a resolvent not being additive and
its Neumann expansion producing cross words that the log-derivative of an Euler
product does not contain.  Row 2, right: the trace-log identity, which is where
the corrected chain applies Vitali.  Row 2, left: a Herglotz function `M` obeys
`‖M(z)‖ ≤ C/|Im z|` only if its Nevanlinna measure has total mass `≤ C` (let
`|Im z| → ∞` in the Nevanlinna representation to kill the affine part, then
`|Im z||M(iy)| → Ω(R)`); the measure of `−∂_z\log D_P^∘` is the zero multiset of
`D_P^∘`, i.e. the spectrum of `A_P` with multiplicity, whose total mass is the
**eigenvalue count** `\#\mathrm{spec}(A_P) → ∞`.  The subtraction of `E_P'/E_P`
is a renormalizing counterterm, so boundedness of the difference is precisely
the statement that the renormalization does not leak mass; and no source-frame
bound bounds it, because `M_P` is not `⟨(A_P−z)^{−1}u,u⟩` for any vector `u`.
A matrix-Herglotz reading cannot rescue row 2: a sourced matrix built from `M_P`
requires exactly the pairing that row 1's right-hand entry withdraws.  ∎
`PROVED`

---

### 18.5 Growth of `h⁰_Z` as it stands

Recall Definition 13.4: `Λ_W = ⊕_{q=p^k}Z·w_qτ_{\log q}(ΠK)` with
`w_q = Λ(q)q^{−1/2}`, `H⁰_Z(E) = \{λ ∈ Λ_W : E+λ ≥ 0\}`, `h⁰_Z = \log\#`.  For
`λ = Σ_qa_qw_qτ_{\log q}(ΠK)` (finitely many `a_q ∈ Z` nonzero) and `E = mK+λ`,

    Φ_E(s) = ξ(s)\big[m + s(1−s)A(s)\big],\qquad
    A(s) := Σ_qa_qw_qq^{s−1/2} = Σ_qa_qΛ(q)q^{s−1} ,                          (18.12)

so `A` is an integer-weighted von Mangoldt Dirichlet polynomial.

**Lemma 18.22 (`PROVED`).**  Let `K(t) = 2Σ_{n≥1}f_n(t)` with
`f_n(t) = (2π²n⁴e^{9t/2} − 3πn²e^{5t/2})e^{−πn²e^{2t}}` (the normalization of
(11.7), fixed by `Φ_K = ξ`).  Put `x := πn²e^{2t}`.  Then for every `n ≥ 1` and
every `t` with `x ≥ 5.1`, `f_n''(t) ≥ ¼f_n(t)`.  Consequently
`K''(t) ≥ K(t)/4`, i.e. `ΠK(t) = −K''(t)+K(t)/4 ≤ 0`, for every
`t ≥ u_0 := ½\log(5.1/π) = 0.2422553…`, and `\{ΠK > 0\} ⊂ (−u_0,u_0)` since
`ΠK` is even.

*Proof.*  Write `A := 2π²n⁴e^{9t/2}`, `B := 3πn²e^{5t/2}`, so `f_n = (A−B)e^{φ}`
with `φ = −πn²e^{2t} = −x`, `φ' = −2x`, `φ'' = −4x`.  Then `A' = \tfrac92A`,
`B' = \tfrac52B`, `A'' = \tfrac{81}4A`, `B'' = \tfrac{25}4B`, and

    f_n'' = e^{φ}\big[(A−B)'' + 2(A−B)'φ' + (A−B)(φ''+φ'^2)\big]
          = e^{φ}\big[A(4x²−22x+\tfrac{81}4) − B(4x²−14x+\tfrac{25}4)\big] .

So the claim is `A(4x²−22x+20) ≥ B(4x²−14x+6)`.  Since
`A/B = \tfrac{2π}3n²e^{2t} = \tfrac23x`, this reads
`\tfrac23x(4x²−22x+20) ≥ 4x²−14x+6`, i.e. `p(x) := 8x³−56x²+82x−18 ≥ 0`.  Now
`p(5.1) = 4.848 > 0` and `p'(x) = 24x²−112x+82` has roots
`(112\pm\sqrt{4672})/48 = 0.909,\ 3.757`, so `p' > 0` on `[5.1,∞)` and `p > 0`
there.  Finally `x = πn²e^{2t} ≥ πe^{2t} ≥ 5.1` exactly when `t ≥ u_0`, and
`n ≥ 2` only increases `x`.  Evenness of `ΠK` is Theorem 11.7(i).  ∎  `PROVED`

**Lemma 18.23 (`PROVED`).**  `K(t) ≥ 2π²e^{9t/2}e^{−πe^{2t}}` for every
`t ≥ 0`.

*Proof.*  For `n ≥ 2` and `t ≥ 0`, `f_n(t) ≥ 0`, because
`2π²n⁴e^{9t/2} ≥ 3πn²e^{5t/2}` iff `e^{2t} ≥ 3/(2πn²)`, and
`3/(2πn²) ≤ 3/(8π) < 1`.  For `n = 1`,
`2f_1(t) ≥ 2π²e^{9t/2}e^{−πe^{2t}}` iff
`2(2π²e^{9t/2}−3πe^{5t/2}) ≥ 2π²e^{9t/2}` iff `π²e^{9t/2} ≥ 3πe^{5t/2}` iff
`e^{2t} ≥ 3/π = 0.9549…`, i.e. `t ≥ −0.0231`.  ∎  `PROVED`

**Corollary 18.24 (`PROVED`).**  For every prime power `q ≥ 2`, with
`β := πe^{2u_0} = 5.1`,

    κ_q := \min_{|t−\log q| ≤ u_0}K(t) ≥ 2π²q^{9/2}e^{9u_0/2}e^{−βq²} ≥ e^{−βq²} .

*Proof.*  The majorant `t ↦ 2π²e^{9t/2}e^{−πe^{2t}}` of Lemma 18.23 has
logarithmic derivative `\tfrac92 − 2πe^{2t} < 0` for
`t > ½\log\tfrac9{4π} = −0.167`, hence is decreasing on the window
`[\log q−u_0,\log q+u_0] ⊂ [0.45,∞)`; its value at the right endpoint is the
displayed quantity, and `2π²e^{9u_0/2}q^{9/2} ≥ 2π² > 1`.  ∎  `PROVED`

**Theorem 18.25 (non-vacuity; `PROVED`).**  Let `M_+ := \sup ΠK`.  For every
prime power `q` and every integer `m ≥ M_+w_q/κ_q`, the class
`λ := −w_qτ_{\log q}(ΠK)` lies in `H⁰_Z(mK)`.  With the certified constants
`M_+ ≤ 17`, `w_2 = (\log 2)/\sqrt2 = 0.4901291…` and
`κ_2 ≥ 1.83571·10^{−6}` (Corollary 18.24), the value `m = 4\,538\,961`
suffices; hence `H⁰_Z(mK) ≠ \{0\}` and `h⁰_Z(mK) > 0` for all
`m ≥ 4\,538\,961`.

*Proof.*  `mK+λ ≥ 0` reads `w_qΠK(t−\log q) ≤ mK(t)` for all `t`.  Where
`ΠK(t−\log q) ≤ 0` this is immediate from `K > 0`.  Where `ΠK(t−\log q) > 0`,
Lemma 18.22 gives `|t−\log q| < u_0`, so `ΠK(t−\log q) ≤ M_+` and
`K(t) ≥ κ_q`; the hypothesis `m ≥ M_+w_q/κ_q` closes it.  ∎  `PROVED`

*Certified constant.*  `M_+ = \sup ΠK` is a number attached to one fixed entire
function, and only an upper bound is needed.  By Lemma 18.22, `ΠK ≤ 0` off
`(−u_0,u_0)` and `ΠK` is even, so `\sup ΠK = \max_{[0,u_0]}ΠK`.  The script
`03-research/phase-137-row-d-canonical-coupling/scripts/d137_lattice.py`
computes `ΠK` on `[0,u_0]` with step `h = 2·10^{−4}`, obtaining
`\max_{\text{grid}}ΠK = 16.953849` (reproducing §13.2's `\max ΠK = 16.953849`),
and `\max_{\text{grid}}ΠK + Lh/2 ≤ 17` holds for **any** Lipschitz bound
`L ≤ 460`, against a sampled `L ≈ 101.5` — a factor `4.5` of head-room.
`M_+ ≤ 17` is `PROVED` modulo that one certified numerical bound, and is
labelled as such.  The threshold `4\,538\,961` is not sharp and is not the
content; the content is that it is finite.

**Proposition 18.26 (the single-generator threshold, necessity; `PROVED`).**
Let `λ = a_qw_qτ_{\log q}(ΠK)` be a single generator with `a_q ≠ 0` and
`mK+λ ≥ 0`.  Then `a_q ≤ −1` (Lemma 13.5b), and evaluating the constraint at
`t = \log q` gives `mK(\log q) ≥ |a_q|w_qΠK(0) ≥ w_qM_+^{0}` with
`M_+^{0} := ΠK(0) = 16.9538…`.  Since, for `t ≥ 0`,
`K(t) = 2Σ_n(2π²n⁴e^{9t/2}−3πn²e^{5t/2})e^{−πn²e^{2t}} ≤ Ce^{9t/2}e^{−πe^{2t}}`
(the `n = 1` term dominates, the tail `Σ_{n≥2}n⁴e^{−π(n²−1)e^{2t}}` being
bounded on `t ≥ 0`), one gets `m ≥ c\,w_q\,q^{−9/2}e^{πq²} ≥ c\,q^{−5}e^{πq²}`,
i.e. `q ≤ \sqrt{(\log m)/π}(1+o(1))`, i.e.
`\log q ≤ ½\log\log m − ½\logπ + o(1)`.  ∎  `PROVED`

**Corollary 18.27 (Remark 13.6a's heuristic is a theorem, in both directions;
`PROVED`).**  A single generator at the prime power `q` is feasible in
`H⁰_Z(mK)` precisely in the range

    e^{πq²} ≲ m ≲ e^{5.1\,q²} ,

the left inequality **necessary** (Proposition 18.26) and the right
**sufficient** (Theorem 18.25 with Corollary 18.24, `β = 5.1`).  Equivalently
`\log q ≍ ½\log\log m` up to an additive constant: this is exactly the picture
Remark 13.6a describes heuristically — "`mK` dominates a single translate
`τ_{\log q}(ΠK)` only for `\log q ≲ ½\log\log m`" — and both halves of it are
now proved, the threshold being bracketed between `e^{πq²}` and `e^{5.1q²}`.
Remark 13.6a's numerical count `1` is an artefact of the tested range `m ≤ 8`:
`H⁰_Z(mK) ≠ \{0\}` from `m ≈ 4.5·10⁶` on (Theorem 18.25).  Remark 13.6a
contains no false statement — the count `1` means the zero section, not "no
sections" — and its conclusion (a logarithm where `m²` is wanted) survives; what
is added here is a determination of its threshold.  ∎  `PROVED`

**Theorem 18.28 (lower bound on the full lattice; `PROVED`).**  There are
absolute constants `c > 0`, `m_1 < ∞` with

    h⁰_{\mathbb Z}(mK) ≥ c\,\frac{(\log m)^{3/2}}{\log\log m}\qquad (m ≥ m_1).   (18.13)

*Proof.*  Put `β := πe^{2u_0} = 5.1`, and fix the absolute constants `β`,
`M_+ ≤ 17` and `C` (from `\log(M_+/w_q) ≤ C\log Q`) **first**.  Given `m`, let
`Q := \lfloor\sqrt{(\log m)/(2β)}\rfloor`, let `𝒬` be the set of prime powers
`q` with `4 ≤ q ≤ Q`, and `d := \#𝒬`.  For `q ∈ 𝒬`,
`\log q − u_0 ≥ \log 4 − 0.2423 > 1`, so by Lemma 18.23, the monotonicity used
in Corollary 18.24 and Corollary 18.24 itself, `κ_q ≥ e^{−βq²}`.

Put `N_q := \lfloor κ_q m/(d\,M_+\,w_q)\rfloor`.  *Claim:* for every choice of
integers `a_q ∈ \{−N_q,…,0\}` (`q ∈ 𝒬`; `a_q = 0` off `𝒬`), the class
`λ := Σ_qa_qw_qτ_{\log q}(ΠK)` lies in `H⁰_Z(mK)`.  Indeed, for every `t`,

    −λ(t) = Σ_q|a_q|w_qΠK(t−\log q) ≤ Σ_{q:|t−\log q|<u_0}|a_q|w_qM_+
          ≤ Σ_{q:|t−\log q|<u_0}\frac{κ_qm}{d}
          ≤ Σ_{q:|t−\log q|<u_0}\frac{mK(t)}{d} ≤ mK(t) ,

using `ΠK ≤ 0` off `(−u_0,u_0)` (Lemma 18.22) in the first step, `|a_q| ≤ N_q`
in the second, `K(t) ≥ κ_q` when `|t−\log q| ≤ u_0` in the third, and that at
most `d` indices occur in the sum.  Distinct coefficient vectors give distinct
`λ` (Theorem 13.5(i)), so

    h⁰_{\mathbb Z}(mK) ≥ Σ_{q∈𝒬}\log(N_q+1)
      ≥ Σ_{q∈𝒬}\big[\log m − βq² − \log d − \log(M_+/w_q)\big] .

With the chosen `Q` one has `βq² ≤ ½\log m` for every `q ≤ Q`; `d ≤ Q`; and
`\log(M_+/w_q) ≤ C\log Q` since `w_q = Λ(q)q^{−1/2} ≥ (\log 2)Q^{−1/2}` on `𝒬`.
Hence each bracket is `≥ ½\log m − (C+1)\log Q ≥ ¼\log m` for `m ≥ m_1` with
`m_1` absolute (in particular `N_q ≥ 1`), and `d ≥ π(Q)−3 ≫ Q/\log Q` by
Chebyshev.  Therefore
`h⁰_Z(mK) ≫ (Q/\log Q)\log m ≫ (\log m)^{3/2}/\log\log m`.  ∎  `PROVED`

**What this settles.**  §14.5 item (23) asks whether `h⁰_Z(mK) = o(m²)` on the
**full** lattice.  (18.13) does not settle it, but it settles a different
question that Lemma 13.5a left open: the full lattice is strictly better than
every finite truncation (`O_Q(\log m)`, (13.3)), and the improvement is a genuine
power of `\log m`.  The growth is **super-logarithmic**; it is **not** known to
be sub-quadratic.

**Theorem 18.29 (conditional upper bound at bounded rank; `PROVED`, imports
named).**  *Imports: the Montgomery–Vaughan mean value theorem **(X22)**;
Stirling ((E4)); and the quantitative zero-free region
`|ζ(1+iτ)|^{−1} ≪ \log^{7}(2+|τ|)` **(X23)**.*  There is an absolute constant
`C` such that if `λ ∈ H⁰_Z(mK)` has all its nonzero coefficients at prime powers
`q ≤ Q`, then

    Σ_q|a_qΛ(q)|² ≤ C\,m²e^{CQ},\qquad \max_q|a_q| ≤ C\,m\,e^{CQ} ,

and consequently, writing `π_*(Q)` for the number of prime powers `≤ Q`,

    h⁰_{\mathbb Z,≤Q}(mK) := \log\#\{λ ∈ H⁰_Z(mK) : \text{indices} ≤ Q\}
      ≤ C\,π_*(Q)\big(\log m + Q\big) .                                        (18.14)

*Proof.*  By Lemma 13.5b and the degree identity `\deg E = m`, `E ≥ 0` gives
`0 ≤ Φ_E(σ) ≤ m` for `σ ∈ [0,1]` and `|Φ_E(σ+iτ)| ≤ Φ_E(σ)`; in particular
`|Φ_E(1+iτ)| ≤ Φ_E(1) ≤ m`, so by (18.12) with `s = 1+iτ`,

    |A(1+iτ)| ≤ \frac{m + m/|ξ(1+iτ)|}{|s(1−s)|} .

By Stirling ((E3a), (E4)) and **(X23)**,
`|ξ(1+iτ)|^{−1} ≤ Ce^{π|τ|/4}(1+|τ|)^{C}`; hence
`|A(1+iτ)| ≤ Cm\,e^{π|τ|/4}(1+|τ|)^{C}/|s(1−s)|`.  Run the mean value on the
interval `[1,1+T]` rather than `[0,T]`, where `|s(1−s)| = |τ||1+iτ| ≥ 1` — the
mean value theorem is invariant under `b_q ↦ b_qq^{iT_0}`, so no constant
changes, and the degeneration of `|s(1−s)|` at `τ = 0` is avoided.  Applying
**(X22)** with `b_q := a_qΛ(q)`,

    ∫_1^{1+T}|A(1+iτ)|²dτ = Σ_q|b_q|²\big(T+O(q)\big) ≥ \tfrac T2Σ_q|b_q|²

as soon as `T ≥ C_0Q`.  The left side is `≤ Cm²e^{πT/2}T^{C}`, so with
`T := C_0Q` we get `Σ_q|b_q|² ≤ Cm²e^{CQ}`.  The count bound (18.14) is then the
number of integer points in a box of side `2\max_q|a_q|+1` in `π_*(Q)`
coordinates.  ∎  `PROVED`

**Remark 18.29a (why a zero-free region must be imported).**  The ceiling
`Φ_E(σ) ≤ m` holds **only** for `σ ∈ [0,1]`, that being exactly the range in
which `e^{(σ−½)t} ≤ 2\cosh(t/2)`.  Inside `(0,1)` the function `ξ` may vanish,
so division by `ξ(σ+iτ)` is illegitimate there without RH.  The two endpoints
`σ ∈ \{0,1\}` are the **only** abscissae where the degree ceiling and
non-vanishing coexist, and non-vanishing at the endpoints is precisely (E2)'s
last clause.  So the Mellin-positivity route to a coefficient bound is forced
onto the line `Re s = 1`, and any quantitative version of it must import a
zero-free region; (X23) is the import, a quantitative strengthening of the
qualitative (E2) already listed in §1.13.  This is a property of the method, not
a defect of the proof.  One attempt to avoid it — running at `σ = 1+η`, where the
Euler product gives `|ζ(σ+iτ)| ≥ ζ(2σ)/ζ(σ) > 0` with no zero information —
**does not close**: the only unconditional handle on `Φ_E(1+η)` is the degree
identity, whose weight is `≍ e^{|t|/2}`, and feeding the resulting majorant into
the mean value produces a quadratic inequality in
`X := (Σ_q|a_qΛ(q)|²)^{1/2}` whose `X²` coefficient is
`≍ Q^{2η}π_*(Q)T^{−1}e^{πT/2}T^{C}`, which is `≫ 1` because the mean value needs
`T ≳ Q`.  Another majorant is not excluded.

**Corollary 18.30 (one-sided reduction of §14.5 item (23) to the largest index;
`PROVED` / `OPEN`).**  Let `Q(m) ∈ [2,∞]` be the supremum of the largest index
occurring in a class of `H⁰_Z(mK)`, and `Ψ(Q) := Cπ_*(Q)(\log m+Q)` the bound of
Theorem 18.29.  Then:

 (i) `Q(m) ≥ c\sqrt{\log m}` for large `m` (the construction of Theorem 18.28);
     `PROVED`;
 (ii) if `Q(m) < ∞` then `h⁰_Z(mK) ≤ Ψ(Q(m))`; `PROVED`;
 (iii) there is an absolute `ε_0 > 0` such that
       `Q(m) ≤ ε_0\,m\sqrt{\log m}` **implies** `h⁰_Z(mK) < ¼m²−¼m+χ` for large
       `m`, i.e. implies that requirement (c) fails for `h⁰_Z`; equivalently, by
       contraposition, **(c) `⟹` `Q(m) > ε_0\,m\sqrt{\log m}`**; `PROVED`;
 (iv) there is **no converse**: `Q(m)` large does not imply `h⁰_Z(mK)` large,
      (ii) being an upper bound only.  What is true is that
      `Q(m) = o(m\sqrt{\log m})` is **sufficient** for `h⁰_Z(mK) = o(m²)`;
 (v) `Q(m) < ∞` and `h⁰_Z(mK) < ∞` are **not** proved: Theorem 18.29 gives
     finiteness of the count at each fixed rank only, and full-lattice
     finiteness is `OPEN` — so the quantity in (iii) is not known to be a finite
     integer.  `OPEN`

*Proof.*  (i)–(ii) are Theorems 18.28 and 18.29 with `π_*(Q) ≍ Q/\log Q`.
(iii): requirement (c) of Theorem 12.3 forces `h⁰_Z(mK) ≥ ¼m²−¼m+χ` by Theorem
13.6(i); and `¼m² ≤ CQ²/\log Q + CQ\log m/\log Q` forces `Q ≥ cm\sqrt{\log m}`,
the second term being dominated once `Q ≥ \log m`.  (iv), (v) are the failure of
the converse implication and the absence of any full-lattice finiteness
statement.  ∎  `PROVED` for (i)–(iv); (v) `OPEN`

**Observation 18.31 (correction to §14.5 item (23); `PROVED`).**  Item (23)
reads: "whether `h⁰_Z(mK) = o(m²)` on the full lattice `Λ_W` — **equivalently**
whether `ρ_Q` of Lemma 13.5a can be controlled uniformly in the rank".  The word
"equivalently" is **incorrect**.  A uniform bound `ρ_Q ≤ ρ` gives, by (13.3),
only `h⁰_{Z,≤Q}(mK) ≤ π_*(Q)\log(2mρ+1)`, which still diverges with the rank
`Q`; so uniform `ρ_Q` **alone does not** give `h⁰_Z(mK) = o(m²)`.  It must be
combined with a bound on the rank actually occurring, i.e. on `Q(m)`.
Conversely `Q(m) = o(m\sqrt{\log m})` **alone does** suffice, by Corollary
18.30(iii)–(iv), via the explicit bound

    ρ_Q ≤ C\,e^{CQ}/\min_{q≤Q}Λ(q)                                             (18.15)

that Theorem 18.29 supplies — the first explicit bound on `ρ_Q` on record, and
exponential rather than uniform.  So item (23) has one sufficient condition on
record (`Q(m)`) and one insufficient reformulation (`ρ_Q` alone), and the paper
states the latter as an equivalence.  ∎  `PROVED`

**Remark 18.31a (what the growth does and does not carry).**  The construction
of Theorem 18.28 is model-uniform in the sense of (12.3) — it mentions only
`D^W`, `⋆`, the canonical class, the positive weights and `\{\cdot ≥ 0\}`, all
of which exist for every admissible `Z` by Proposition 12.6 — so by Restatement
12.4a no derivation of (a)+(b′)+(c) can rest on it alone.  Both `ξ` and `Ξ_a`
receive **lower** bounds from it, and **no comparison of the two counts is
available in either direction**, there being no upper bound for `h⁰_Z(mK)` on
the full lattice.  Nothing here is claimed about any sign.  Quantitatively, the
proved lower bound `c(\log m)^{3/2}/\log\log m` is of order `10²` at `m = 10⁶`,
against the `¼m² ≈ 2.5·10^{11}` that requirement (c) demands, and the
obstruction is structural: feasible corrections would have to be supported at
prime powers of size `≳ m\sqrt{\log m}`, i.e. at modulus `t ≈ \log m`, where
`K(t) ≈ e^{−πm²}`, while a single generator at `q` needs `m ≳ e^{πq²}`, i.e.
`q ≲ \sqrt{\log m}` (Corollary 18.27).  What is open is precisely whether
near-cancelling combinations evade that; the factor `e^{CQ}` of Theorem 18.29 is
the exact cost of that possibility, and it comes from the exponential type `π/4`
of `1/ξ` on vertical lines against the length `T ≍ Q` that the mean value
requires.

---

### 18.6 The construction problem, and the falsifier gap

**Problem 18.32 (the construction problem; `OPEN`).**  Let `𝒵` be the class of
functions `Z` satisfying A1, A2, A2⁺, A4, A5, A6 of Definition 18.13.  It
contains `ξ`, every `ξ_K`, every `Ξ_a`, and `Ξ_Q` for principal `Q` with
`h(−D) > 1`.  **Construct a rule `Z ↦ h⁰_Z` defined on `𝒵` such that for every
number field `K` the member `h⁰_{ξ_K}` satisfies**

 **(a)** `h⁰_{ξ_K}(E) ≥ 0` for every `E`;
 **(b′)** if `h⁰_{ξ_K}(E) > 0` then there is `E' ≥ 0`, `E' ≢ 0`, with
      `E − E' ∈ 𝓝_∞^{(K)}`;
 **(c)** `h⁰_{ξ_K}(E) + h⁰_{ξ_K}(K_K−E) ≥ ½I_∞^{(K)}(E,E) − ½I_∞^{(K)}(E,K_K)
      + χ_K` for every `E`,

together with the naming clause **(N)**: the proof must name the line that uses
A3 and the line that uses one of A7, A8, A9.  The growth forced by (c) is
`h⁰_K(mK_K) ≥ (r²/4)m² + O(m)`, and `¼m²` in the normalization of `Ξ_Q`.
Three acceptance tests attach to any candidate: **(AT-1)** the rule at `Ξ_Q`
must fail at a named line — for a construction built on row B's structure, at
the inverse-semigroup law `Frob_m ⋆ Frob_n = Frob_{mn}`; **(AT-2)** at `Ξ_a` it
must fail at a use of A3; **(AT-3)** no line may distinguish `Q` from a number
field `K`.  Clause (N) is a condition on proofs, not on the object, so that the
object itself remains purely mathematical.  `OPEN`

The structure that Epstein lacks and that row B has is exactly the
multiplicativity `Frob_m ⋆ Frob_n = Frob_{mn}`, which fails for `r_Q(n)` because
of the class group (Remark 18.12a); this localizes the Euler-product step of
Problem 18.32 inside row B.

**Observation 18.33 (the falsifier gap; `PROVED`).**  Consider the class of
functions with the shape that a rank-one polar divergence argument requires:
an Euler product with non-negative von Mangoldt atoms, a **simple** pole, and a
functional equation.  This class is large — it contains every Dedekind zeta
`ζ_K` — but it **contains no member with proven off-line zeros**.  Consequently:

 (i) `Ξ_a`, whose polar set `\{−a,a,1−a,1+a\}` has four points, **cannot
     adjudicate** any argument that uses rank-one polar divergence: it fails a
     hypothesis such an argument actually uses, and "the falsifier fails a
     hypothesis" is strictly weaker than "the argument distinguishes `ξ` from
     the falsifier";
 (ii) a sound argument of that shape would **prove GRH for all number fields**.

*Proof.*  (i) For `Ξ_a` the polar set has four points, so the divergent block
has rank `≥ 2` and a rank-one projection does not remove it; an argument whose
load-bearing step asserts that the divergence is rank-one therefore has a
hypothesis that `Ξ_a` violates, and the test is vacuous rather than passed.
Within the family `F = ∏_jζ(s+a_j)^{m_j}` with `m_j > 0` and real `a_j` — the
family from which the standing falsifiers are drawn — one has
`−F'/F(s) = Σ_nΛ(n)\big(Σ_jm_jn^{−a_j}\big)n^{−s}` with non-negative
coefficients, and `F` has one pole per distinct `a_j`; a **simple** pole forces
a single `a_j`, and `F(s) = F(1−s)` then forces `a_j = 0`, i.e. `F = ζ^m`, whose
zeros are those of `ζ`.  So the family contains no object with non-negative
weights, a simple pole and off-line zeros.  (ii) is Theorem 18.1 applied to the
list of properties in the shape, each of which `ξ` shares with every `ξ_K`.  ∎
`PROVED`

Whether some object outside that family qualifies — a degree-one `L`-function
with a simple pole, non-negative von Mangoldt weights and a known off-line zero
— is `OPEN`; none is known.  Observation 18.33 is a permanent constraint on the
faithfulness test of §§12.4–12.5: `Ξ_Q` adjudicates arguments that use A7, A8 or
A9 (Theorem 18.16), and `Ξ_a` adjudicates arguments that use A3 (Theorem 12.4),
but neither adjudicates an argument whose load-bearing step is the rank of the
polar divergence.

---

### Withdrawn in this section

| claim | reason |
|---|---|
| `K_Q > 0`, by the theta series, as `K > 0` for `ξ` | `REFUTED`: `Λ_Q` has real zeros in `(0,1)` for `Q_k = x²+ky²`, `k` large, so `Ξ_Q(σ') = ∫K_Q e^{(σ'−½)t}dt = 0` (Theorem 18.5, Corollary 18.6); the term-by-term argument is unavailable as well (Remark 18.3a) |
| `\deg K_Q = Λ_Q(0)+Λ_Q(1)` | denotes nothing: `Λ_Q` has poles at `0` and `1`.  Correct statement `\deg K_Q = Ξ_Q(0)+Ξ_Q(1) = ½` (Theorem 18.3(vi)) |
| Proposition 12.6 conflates the polar and zero quantities `θ_P`, `θ_Z` | withdrawn: Proposition 12.6 defines `θ = \max_{p∈P}|p−½|` and assumes (12.4) as a separate displayed hypothesis.  `Ξ_Q` violates four of its hypotheses and lies outside its class; producing such a function is not a counterexample to the proposition.  Only an editorial suggestion remains (two named symbols `θ_P`, `θ_Z`) |
| Theorem 18.20 (base change) unconditionally, for general `L/K` | `PROVED` only for `L/K` abelian; in general it needs Artin holomorphy **(X25)**.  Aramata–Brauer (`ζ_L/ζ_K` entire) is a statement about the product, not about the factors, and does not suffice |
| the claim that the additivity holds packet-by-packet for individual complex `χ` | withdrawn: for complex `χ`, `Λ(\cdot,χ)` has no self-dual functional equation, so A1 fails for it and Lemma 18.9 does not apply.  The decomposition is taken over conjugate packets (Lemma 18.19) |
| `Ξ_a` has **strictly more** sections than `ξ`, and the growth of `h⁰_Z` therefore carries a sign | withdrawn: `A ≥ f` and `B ≥ g` with `g > f` says nothing about `A` versus `B`, and no upper bound for `h⁰_Z(mK)` on the full lattice exists — that is item (23) |
| any `h⁰` whose growth is driven by the decay rate of the canonical kernel is disqualified in advance | withdrawn: this is the non-sequitur of Restatement 12.4a and Remark 12.4a′ — a model-uniform *rule* may satisfy (a)+(b′)+(c) for `ξ` and fail them for `Ξ_a`; what is excluded is a model-free *proof*, never a function |
| item (23) is *equivalent* to a bound on the largest index `Q(m)` | withdrawn: there is no converse to Corollary 18.30(ii).  `Q(m) = o(m\sqrt{\log m})` is sufficient, not equivalent (Corollary 18.30(iv)) |
| "Remark 13.6a is corrected: the lattice has sections where the remark says it has none" | withdrawn: Remark 13.6a contains no false statement (count `1` means the zero section) and declares itself heuristic.  What is proved is a determination of its threshold, in both directions (Corollary 18.27) |
| the `σ > 1` route to a coefficient bound **fails** | narrowed: one bootstrap does not close (Remark 18.29a); another majorant for `Φ_E(1+η)` is not excluded.  The structural statement — the ceiling and non-vanishing coexist only at `σ ∈ \{0,1\}` — is what survives |
| `Σ_{n≤x}c_Q(n) = O(x)` is false for Epstein | withdrawn as a non sequitur: Theorem 18.12(ii) bounds the **absolute** partial sums, and the signed sums may be far smaller through cancellation.  A8's failure for `Ξ_Q` follows from Theorem 18.12(i) alone |
| the equivalence "A9 `⟺` `K_Z > 0`" | withdrawn as circular and false as an equivalence: only `K_Z > 0 ⟹` A9 holds, since `Z(σ) = ∫K_Z(t)e^{(σ−½)t}dt` (Definition 18.13, A9) |
| the earlier purported proof `RH-PROOF.md` establishes RH | `REFUTED` (Proposition 18.21); it is correct as a reduction of RH to a uniformity statement |
| "no falsifier exists for the rank-one polar divergence argument, therefore the argument stands" | withdrawn: the falsifier class is **empty** for that shape, so the test is vacuous, not passed (Observation 18.33) |

---

---

## 19. The Riemann–Roch-defined `h⁰` and the frame defect theorem

*Provenance note.  The statements and proofs of this section are taken from
`03-research/phase-141-row-d-frobenius-traces/R141_001_ROUND1.md` §D.30 and
`03-research/phase-142-row-d-the-clause/R142_001_ROUND1.md` §§D.31, with §19.8
from `R142_003_ROUND2.md` §D.32; the labels and the withdrawals are those fixed in
`R141_005_CLOSING_DECISION.md`, `R142_002_AUDIT.md`,
`R142_004_CONFIRMATION.md` and `R142_005_CLOSING_DECISION.md`.  The certified
constants are produced by `03-research/phase-142-row-d-the-clause/scripts/certify_sF.py` and
`certify_leakage.py`.*

Throughout, the conventions of §11 are in force: `D^W` (Definition 11.1), `I_∞` (Definition 11.4),
`Φ_E(s) = ∫E(u)e^{(s−½)u}du`, `M(E) = (a,b) = (Φ_E(1),Φ_E(0))`, `𝓝_∞` the radical of `I_∞`
(Theorem 11.11), `K` the Pólya class of Theorem 11.7 (`Φ_K = ξ`, `K > 0` pointwise, `M(K) = (½,½)`,
`\deg K = 1`, `I_∞(K,K) = ½`), `\deg E = I_∞(E,2K) = ∫E(u)·2\cosh(u/2)du = a+b`
(Theorems 11.8(v), 11.13(i)), `W(E) := Σ_ρΦ_E(ρ)Φ_E(1−ρ)` over the zeros of `ξ` with multiplicity,
and the comparison identity (11.6), `I_∞(E,E) = 2ab − W(E)`.  Clauses (a), (b′), (c) are those of
Theorem 12.3.

**Definition 19.1 (the Riemann–Roch functional).**  For `χ ∈ R`,

    R(E) := ½\,I_∞(E,E) − ½\,I_∞(E,K) + χ = ½\,I_∞(E,E) − ¼\,\deg E + χ ,

i.e. **the right-hand side of clause (c)**; the second form is Theorem 11.8(i)
(`I_∞(E,K) = ½\deg E`).  By (11.6),

    R(E) = ab − ½\,W(E) − ¼\,\deg E + χ ,\qquad (a,b) = M(E).                         (19.1)

Put `S_χ := \{E ∈ D^W : \deg E > 0,\ R(E) > 0\}` and `S_0` for `S_χ` at `χ = 0`.  `R` is defined by
the arithmetic side alone: Definition 11.4 names no zero.

### 19.1 Serre symmetry

**Theorem 19.2 (Serre symmetry of clause (c); `PROVED`).**  `R(K−E) = R(E)` for every `E ∈ D^W`,
identically, unconditionally, and for every `χ`.  The proof uses **only** bilinearity and symmetry of
`I_∞` (Definition 11.4, Lemma 11.4a); no value of `I_∞(K,K)` and no property of `K` beyond its being
a fixed class is used.

*Proof.*

    R(K−E) = ½\big[I_∞(K,K) − 2I_∞(K,E) + I_∞(E,E)\big] − ½\big[I_∞(K,K) − I_∞(E,K)\big] + χ
           = ½\,I_∞(E,E) − I_∞(E,K) + ½\,I_∞(E,K) + χ
           = ½\,I_∞(E,E) − ½\,I_∞(E,K) + χ = R(E) . ∎  `PROVED`

*The same identity in coordinates.*  `M(K−E) = (½−a, ½−b)` and
`W(K−E) = W(K) − 2Σ_ρΦ_K(ρ)Φ_E(1−ρ) + W(E) = W(E)`, because `Φ_K(ρ) = ξ(ρ) = 0`; so by (19.1)

    R(K−E) − R(E) = (½−a)(½−b) − ab − ¼(1−a−b) + ¼(a+b) = 0 .

The invariance is exactly invariance under the affine duality `σ_K(E) = K−E` of Theorem 12.2.

### 19.2 The gated candidate `h⁰_{RR}^{+}`: (a) and (c) are free

**Definition 19.3.**  `h⁰_{RR}(E) := \max(R(E),0)`.

**Proposition 19.4 (the ungated candidate fails (b′); `PROVED`).**  For every `χ ∈ R`: clause (a)
holds; clause **(c) holds unconditionally**, since by Theorem 19.2

    h⁰_{RR}(E) + h⁰_{RR}(K−E) = 2\max(R(E),0) ≥ R(E) ;

and clause **(b′) fails, unconditionally**.

*Proof.*  (a) and (c) are the two displays.  For (b′), take `E = mK` with `m < 0`.  Then
`I_∞(mK,mK) = m²/2` and `I_∞(mK,K) = m/2`, so

    R(mK) = \tfrac{m²}4 − \tfrac m4 + χ \xrightarrow[m→−∞]{} +∞ ,

while `\deg(mK) = m < 0`.  By Theorem 11.13(ii),(iv) the degree is constant on `𝓝_∞`-cosets and by
Theorem 11.13(i) it is strictly positive on nonzero nonnegative classes, so no nonzero nonnegative
class is `𝓝_∞`-equivalent to a class of negative degree.  ∎  `PROVED`

The defect is entirely in the negative-degree half-line, where `R` grows quadratically for the wrong
reason.  That is what the gate below removes, and the gate is not ad hoc: any `h⁰` satisfying (b′)
vanishes in degree `≤ 0` (Step 1 of Theorem 19.25's proof).

**Definition 19.5 (the Riemann–Roch-defined candidate).**

    h⁰_{RR}^{+}(E) := \max\big(R(E),\,0\big)\cdot\mathbf 1_{\{\deg E > 0\}} .

**Theorem 19.6 (`h⁰_{RR}^{+}` satisfies (a) and (c) unconditionally, for every `χ`; `PROVED`).**

 (i) **(a)** `h⁰_{RR}^{+} ≥ 0`.
 (ii) **(c)** `h⁰_{RR}^{+}(E) + h⁰_{RR}^{+}(K−E) ≥ R(E)` for every `E ∈ D^W`; that is, clause (c) of
      Theorem 12.3 holds unconditionally, with **any** `χ`.
 (iii) *Growth:* `h⁰_{RR}^{+}(mK) = ¼m² − ¼m + χ` for `m` large — the required `¼m² + O(m)` on the
      nose.  Over a number field, with `I_∞^{(K)}(K_K,K_K) = r²/2` and `\deg_K K_K = r`, the same
      computation gives `\tfrac{r²}4 m² + O(m)`.
 (iv) *Vanishing in degree `≤ 0`:* `h⁰_{RR}^{+}(E) = 0` whenever `\deg E ≤ 0`, in particular on the
      whole primitive subspace `P^W`.
 (v) It is **not** positively `2`-homogeneous, and it is **not** a function of the bidegree `M(E)`.

*Proof.*  (i) is the definition.  (ii): since `\deg E + \deg(K−E) = \deg K = 1 > 0`, **the two gates
cannot both be off**.  If the `E`-gate is on, the left side is `≥ \max(R(E),0) ≥ R(E)`.  If the
`(K−E)`-gate is on, the left side is `≥ \max(R(K−E),0) = \max(R(E),0) ≥ R(E)` by Theorem 19.2.  In
detail, three cases: `\deg E ≤ 0` (then `\deg(K−E) = 1 − \deg E ≥ 1 > 0`, second gate on);
`\deg E ≥ 1` (first gate on); `0 < \deg E < 1` (both on, and the left side is `2\max(R(E),0)`).  No
case uses `χ` and no case uses a sign.  (iii) `\deg(mK) = m`, `I_∞(mK,mK) = m²/2`,
`I_∞(mK,K) = m/2`; the gate is on for `m > 0` and `R(mK) > 0` for `m` large.  (iv) is the gate,
together with `\deg|_{P^W} = 0` (Theorem 11.13(iii)).  (v) `h⁰_{RR}^{+}(λE) ≠ λ²h⁰_{RR}^{+}(E)`
already at `E = K`, `λ = 2` (`R(2K) = 1 − ½ + χ` while `4R(K) = 1 − 1 + 4χ`); and `R` depends on
`W(E)`, which is not a function of `M(E)`, since there are classes of equal bidegree and different
`W`.  ∎  `PROVED`

**Proposition 19.7 (the bidegree witness of Theorem 19bis.19 does not reach this candidate;
`PROVED` under RH).**  Let
`E_0 ∈ D^W`, let `F ∈ C_c^∞(R)` be primitive with `Φ_F(ρ_1) ≠ 0` at some zero, and let
`E_t := E_0 + tF` (constant bidegree, unbounded zero data).  Then

    R(E_t) = ab − ½\big[W(E_0) + 2t\,W(E_0,F) + t²W(F)\big] − ¼\deg E_0 + χ ,

and under RH `W(F) = Σ_ρ|Φ_F(ρ)|² > 0`, since the sum contains `|Φ_F(ρ_1)|² > 0`; hence
`R(E_t) → −∞` and `h⁰_{RR}^{+}(E_t) = 0` for all large `t`.  Unconditionally, `R(E_t) → −∞` unless
`W(F) ≤ 0`, i.e. unless RH already fails at a zero that `F` sees.  ∎  `PROVED`

### 19.3 `χ ≤ 0` is forced, and `χ = 0` is calibrated exactly

**Theorem 19.8 (`χ > 0` is refuted; `PROVED`, unconditional).**  If `χ > 0` then clause (b′) fails
for `h⁰_{RR}^{+}`.

*Proof.*  Fix `c > 0` and `ε > 0` and set `E := αK + βτ_cK` with

    β := \frac{−6ε}{e^{c/2}−e^{−c/2}} ,\qquad α := −2ε − βe^{c/2} .

By Theorem 11.8(iii), `Φ_{τ_cK}(1) = ½e^{c/2}` and `Φ_{τ_cK}(0) = ½e^{−c/2}`, so
`M(E) = (a,b) = (−ε,\,2ε)`.  Then `E ∈ D^W`; both `K` and `τ_cK` have `Φ(ρ) = 0` at every zero, so
`Z(E) = 0` and `W(E) = 0`; `\deg E = a+b = ε > 0`; and by (19.1)

    R(E) = ab − ¼\deg E + χ = −2ε² − \tfrac ε4 + χ > 0

for `ε` small.  Hence `h⁰_{RR}^{+}(E) > 0`.  But `a = Φ_E(1) = −ε < 0`, while every nonnegative
`E' ≢ 0` has `Φ_{E'}(1) = ∫E'(u)e^{u/2}du > 0`, and `M` is constant on `𝓝_∞`-cosets
(Theorem 11.11).  So no such `E'` exists and (b′) fails.  ∎  `PROVED`

**Corollary 19.9 (`χ = 0` is the canonical gate, and it is exactly calibrated to the `√(ab)` bound;
`PROVED`).**  Admissibility forces `χ ≤ 0`, and `χ = 0` is the **weakest** (largest `\{h⁰ > 0\}`)
admissible gate.  At `χ = 0`,

    h⁰_{RR}^{+}(E) = \max\big(½I_∞(E,E) − ¼\deg E,\,0\big)\cdot\mathbf 1_{\{\deg E>0\}} ,
    \qquad h⁰_{RR}^{+}(mK) = ¼m² − ¼m .

Moreover, with `χ ≤ 0` and under RH, `R(E) > 0` together with `\deg E > 0` imply the two elementary
necessary conditions for the existence of a nonnegative representative:

 (i) `a > 0` and `b > 0`;
 (ii) `|Φ_E(ρ)| < \sqrt{ab}` at every zero.

*Proof.*  The first two sentences are Theorem 19.8 and monotonicity of `\{R > 0\}` in `χ`.  (i) Under
RH `W(E) ≥ 0`, so `R(E) > 0` gives `ab > ½W(E) + ¼\deg E − χ ≥ ¼\deg E > 0`; with
`a + b = \deg E > 0` this forces `a,b > 0`.  (ii) Under RH every zero is `ρ = ½+iγ` and, `E` being
real, `Φ_E(1−ρ) = \overline{Φ_E(ρ)}`; the zero multiset is stable under `ρ ↦ \barρ`, so
`W(E) = 2Σ_{γ>0}|Φ_E(½+iγ)|²`.  With `χ ≤ 0`, `R(E) > 0` gives
`Σ_{γ>0}|Φ_E(½+iγ)|² ≤ ½W(E) < ab − ¼\deg E + χ ≤ ab`, and each term is at most the sum.  ∎  `PROVED`

Condition (ii) is exactly the necessary bound `|Φ_{E'}(ρ)| ≤ b^{1−β}a^{β}` at `β = ½`, made strict.
So the gate `R > 0` at `χ = 0` cuts out precisely the classes passing both elementary tests — no more
and no less **against that constant**.  §19.5 shows that constant is not sharp, and that this
apparently exact calibration is the source of the failure.

### 19.4 The clause (b′)⁺, and that it implies RH

**Definition 19.10 (the clause).**  For `χ ≤ 0`:

> **(b′)⁺** : `\deg E > 0` **and** `R(E) = ½I_∞(E,E) − ¼\deg E + χ > 0`
> `⟹` there is `E' ∈ D^W` with `E' ≥ 0`, `E' ≢ 0`, `E − E' ∈ 𝓝_∞`.

At `χ = 0` this reads: *every class of positive degree and positive self-intersection is
`𝓝_∞`-equivalent to a nonzero nonnegative class.*  Both hypotheses are `I_∞`-pairings, hence
arithmetic (Definition 11.4); no zero is named.

**Theorem 19.11 ((b′)⁺ implies RH; `PROVED`, two independent proofs).**

*Proof 1 (through Theorem 12.3).*  By Theorem 19.6, `h⁰_{RR}^{+}` satisfies (a) and (c); and (b′)⁺ is
exactly clause (b′) for it, since `h⁰_{RR}^{+}(E) > 0` iff `\deg E > 0` and `R(E) > 0`.  Theorem 12.3
applies and gives `I_∞(F,F) ≤ 0` on primitive `F ∈ C_c^∞(R)`, hence RH.  ∎

*Proof 2 (direct; it needs no ampleness).*  Let `F ∈ C_c^∞(R)` be real and primitive with
`q := I_∞(F,F) > 0`; we derive a contradiction, which gives `I_∞(F,F) ≤ 0` on the primitive
`C_c^∞` cone, i.e. RH by Paper 45 Theorem 10.4.  Put `E := rF + K` with `r > 0`.  Since
`I_∞(F,K) = ½\deg F = 0` (Theorem 11.8(i)),

    \deg E = \deg K = 1 > 0 ,\qquad I_∞(E,E) = r²q + I_∞(K,K) = r²q + ½ ,
    R(E) = ½r²q + ¼ − ¼ + χ = ½r²q + χ ,

which is `> 0` as soon as `r² > −2χ/q`.  By (b′)⁺ there is `E' ≥ 0`, `E' ≢ 0`, with `E−E' ∈ 𝓝_∞`.
Since `𝓝_∞` is the radical (Theorem 11.11), `I_∞(E',F) = I_∞(E,F) = rq + I_∞(K,F) = rq`, and
`\deg E' = \deg E = 1` (Theorem 11.13(ii),(iv)).  But `E'` is nonnegative, so the bounded-density
bound Theorem 11.14(ii) gives

    rq = |I_∞(E',F)| ≤ C_F\,\deg E' = C_F < ∞ ,

with `C_F` the constant (11.17), independent of `r`.  Taking
`r > \max(C_F/q,\ \sqrt{−2χ/q})` is a contradiction.  ∎  `PROVED`

Proof 2 uses only bilinearity, `I_∞(F,K) = ½\deg F` (Theorem 11.8(i)), `𝓝_∞` = radical
(Theorem 11.11), the `𝓝_∞`-invariance and positivity of `\deg` (Theorem 11.13), and Theorem 11.14(ii).
It uses neither ampleness, nor Step 2 of Theorem 12.3, nor Hardy's theorem — and it is the proof that
transports to other models (Theorem 19.15).

**Theorem 19.12 (the stable weakening suffices; `PROVED`).**  Theorem 12.3 remains valid with (b′)
replaced by

> **(b′)_{st}** : `h⁰(E) > 0 ⟹ ∃N ∈ N_{≥1}` and `E' ∈ D^W` with `E' ≥ 0`, `E' ≢ 0`,
> `N·E − E' ∈ 𝓝_∞`.

*Proof.*  Re-read the proof of Theorem 12.3.  Step 2: if `h⁰(K−nF) > 0`, (b′)_{st} gives `N ≥ 1` and
`E' ≥ 0`, `E' ≢ 0`, with `N(K−nF) − E' ∈ 𝓝_∞`; then `N·I_∞(K−nF,H') = I_∞(E',H') > 0` by ampleness
of `H'`, and `N > 0`, so `I_∞(K−nF,H') = m − nq > 0`, exactly as before.  Step 3 uses only (c).
Step 4: at the chosen `n`, (b′)_{st} gives `N ≥ 1` and `E' ≥ 0`, `E' ≢ 0`, with `NnF − E' ∈ 𝓝_∞`, so
`\deg E' = Nn\deg F = 0` by Theorem 11.13(ii),(iv), contradicting `\deg E' > 0` by
Theorem 11.13(i).  ∎  `PROVED`  *(An extension of Theorem 12.3's hypothesis; Theorem 12.3 itself is
untouched and unrelabelled.)*

**Corollary 19.13 (the weakest form of the clause).**

> **(b′)⁺_{st}** : `\deg E > 0` and `I_∞(E,E) > ½\deg E − 2χ` `⟹` **some positive multiple of `E`**
> is `𝓝_∞`-equivalent to a nonzero nonnegative class,

and it still implies RH, by Theorems 19.6 and 19.12.  At `χ = 0` this is the arithmetic analogue of
the classical *"`D² > 0` and `D·H > 0` ⟹ `D` is big"*, i.e. of asymptotic Riemann–Roch on a surface,
where the multiple is exactly what the classical statement provides and the unstabilized version does
not.  ∎

**Proposition 19.14 ((a) and (c) are model-uniform; `PROVED`).**  Let `Z ∈ 𝒵` satisfy A1, A2, A2⁺,
A5, A6, with polar set `P`, canonical class `K_Z`, `\deg_Z := I_∞^{(Z)}(\cdot,2K_Z)` and
`R_Z(E) := ½I_∞^{(Z)}(E,E) − ½I_∞^{(Z)}(E,K_Z) + χ`.  Then `R_Z(K_Z−E) = R_Z(E)` identically
(Theorem 19.2's proof is pure bilinearity), and

    h⁰_{RR}^{+,Z}(E) := \max(R_Z(E),0)\cdot\mathbf 1_{\{\deg_Z E > 0\}}

satisfies **(a)** and **(c)** unconditionally, for every `χ`.  The gate argument needs only
`\deg_Z K_Z > 0`, which is A2⁺: `\deg_Z K_Z = 2Σ_{p∈P}Z(p)Φ_{K_Z}(p) = 2Σ_{p∈P}Z(p)² > 0`.  The rank
of the polar block is irrelevant: for `Ξ_a`, `\#P = 4` and `\deg_a K_a = 2Σ_{p∈P}Ξ_a(p)² > 0`, so
`\deg_a E ≤ 0 ⟹ \deg_a(K_a−E) = \deg_a K_a − \deg_a E > 0`, and the two gates still cannot both be
off.  ∎  `PROVED`

Thus the entire model-dependence of the construction sits inside (b′)⁺.

**Theorem 19.15 ((b′)⁺ is false for `Ξ_a`; `PROVED`).**  Fix `0 < a < ½`.  Then (b′)⁺ fails for
`Ξ_a`, for every `χ`, and the witness is explicit: with `F_+` the even `Ξ_a`-primitive compactly
supported test of Proposition 12.4B (`I_∞^{(a)}(F_+,F_+) =: q > 0`) and `r` large,
`E := rF_+ + K_a` has `\deg_a E = \deg_a K_a > 0`,
`R_a(E) = ½r²q + ½I_∞^{(a)}(K_a,K_a) − ¼\deg_a K_a + χ > 0`, and `E` is `𝓝_∞^{(a)}`-equivalent to no
nonzero nonnegative class.

*Proof.*  Proof 2 of Theorem 19.11, transported by §12.5.  The comparison identity (11.6),
`I_∞^{(a)}(F,K_a) = ½\deg_a F = 0` for `Ξ_a`-primitive `F`, the radical property of `𝓝_∞^{(a)}`
(Theorem 11.11) and Theorem 11.13 all transport verbatim.  The one substantive point is
Theorem 11.14, whose transport is §12.5(c): the weight `2\cosh(t/2)` is replaced by
`Σ_{p∈P}Ξ_a(p)e^{(p−½)t}`, which grows like `e^{(½+a)|t|} = e^{θ_a|t|}` and therefore still dominates
`|e^{(ρ−½)u}| ≤ e^{θ_a|u|}`; so `C_{F_+} < ∞`.  Then
`rq = |I_∞^{(a)}(E',F_+)| ≤ C_{F_+}\deg_a E' = C_{F_+}\deg_a K_a` bounds `r`, a contradiction for `r`
large.  Existence of `q > 0` is Proposition 12.4B, whose hypothesis — a zero of `Ξ_a` off the line —
is Hardy's theorem (X16) via Theorem 12.4's argument.  ∎  `PROVED`

*Independent confirmation.*  By Proposition 19.14, `h⁰_{RR}^{+,Ξ_a}` satisfies (a) and (c); if it also
satisfied (b′) it would contradict Theorem 12.4.  The two arguments agree, and the first exhibits the
witness.

For `Ξ_Q` the constant of Theorem 11.14 is infinite — the polar weight
`Σ_{p∈\{0,1\}}Ξ_Q(p)e^{(p−½)u} = ¼·2\cosh(u/2)` grows like `e^{|u|/2}` while the Davenport–Heilbronn
zero terms `e^{(ρ−½)u}` grow like `e^{(β−½)|u|}` with `β > 1` — so axiom A7 fails and neither
Theorem 12.3 nor Proof 2 of Theorem 19.11 transports.  The frame, not the clause, has already failed
there.

### 19.5 The cosh lemma

**Definition 19.16.**  For `γ, θ ∈ R`,

    s(γ,θ) := \sup_{u∈R} \frac{|\cos(γu+θ)|}{\cosh(u/2)} ∈ (0,1] .

**Lemma 19.17 (the cosh lemma; `PROVED`, unconditional).**  Let `E' ∈ D^W`, `E' ≥ 0`.  Then for all
real `γ, θ`,

    \Big|∫E'(u)\cos(γu+θ)\,du\Big| ≤ ½\,s(γ,θ)\,\deg E' .

In particular, if `ρ = ½+iγ` is a zero of `ξ` on the critical line, then for every `θ`

    \big|\mathrm{Re}\big(e^{iθ}Φ_{E'}(ρ)\big)\big| ≤ ½\,s(γ,θ)\,\deg E' ,
    \qquad |Φ_{E'}(ρ)| ≤ ½\big(\max_θ s(γ,θ)\big)\deg E' = ½\deg E' .                  (19.2)

*Proof.*  By Definition 19.16, `|\cos(γu+θ)| ≤ s(γ,θ)\cosh(u/2)` pointwise; integrate against
`E' ≥ 0` and use `\deg E' = ∫E'(u)·2\cosh(u/2)du` (Theorem 11.13(i)).  For the second display,
`Φ_{E'}(½+iγ) = ∫E'(u)e^{iγu}du`, so `\mathrm{Re}(e^{iθ}Φ_{E'}(ρ)) = ∫E'(u)\cos(γu+θ)du`.  ∎  `PROVED`

**Proposition 19.18 (the sharpness gap, certified; `PROVED`).**  `s(γ,θ) < 1` **strictly** for every
`γ ≠ 0` and every `θ ∉ πZ`, and at `θ = π/2`, `γ = γ_1`,

    s_1 := s(γ_1,π/2) = \sup_u \frac{|\sin(γ_1u)|}{\cosh(u/2)} = 0.99846016271880910923… ,
    \qquad u^* = 0.110991563370513694… ,

with `1 − s_1² = 3.0773034635×10^{−3}`.

*Proof.*  `|\cos(γu+θ)| ≤ 1 = \cosh(0)`, with equality in the numerator only on the discrete set
`u ∈ (πZ−θ)/γ`, which contains `0` iff `θ ∈ πZ`; off `u = 0` the denominator is `> 1`; and
`|\cos(γu+θ)|/\cosh(u/2) ≤ 1/\cosh(u/2) → 0` as `|u| → ∞`, so the supremum is attained and is `< 1`.
For the numerical value, the critical equation is
`γ_1\cos(γ_1u)\cosh(u/2) = ½\sin(γ_1u)\sinh(u/2)`; outside `|u| ≤ 0.4` the quotient is at most
`1/\cosh(0.2) = 0.9803… < s_1`, and inside, a `40`-digit scan with one Newton refinement gives `u^*`
and `s_1` as displayed.  Certified by `certify_sF.py` (mpmath, `mp.dps = 40`).  ∎  `PROVED`

Corollary 19.9(ii) calibrated `χ = 0` against the constant `\sqrt{ab} ≤ ½\deg E'`.  Lemma 19.17 shows
that at an on-line zero the sharp constant in a fixed direction `θ` is `½s(γ,θ)\deg E'` with
`s(γ,θ) < 1`, and when `a = b` (so `\sqrt{ab} = ½\deg E'`) the gap is a genuine factor `s_1 < 1`.
**The gate `R > 0` at `χ = 0` is therefore strictly wider than the set of classes with a nonnegative
representative.**

### 19.6 The witness, and the failure of the clause

**Definition 19.19 (the test class).**  `σ := 3`, `G := σ\sqrt{2π}/2 = 3.759942411949…`, and

    F_0(u) := e^{−u²/18}\,\sin(γ_1u) ∈ C^∞(R) .

**Lemma 19.20 (properties of `F_0`; `PROVED`; uses (X19), (E2), (E3d)).**

 (i) `F_0 ∈ D^W`, real, **odd**;
 (ii) `\deg F_0 = 0` exactly, and `Φ_{F_0}(0) = −Φ_{F_0}(1) = η` with `|η| < 10^{−390}`;
 (iii) `Φ_{F_0}(ρ_1) = iG(1 + O(10^{−390}))` and `Φ_{F_0}(1−ρ_1) = \overline{Φ_{F_0}(ρ_1)}`;
 (iv) `L := Σ_{ρ ≠ ρ_1,\barρ_1}|Φ_{F_0}(1−ρ)| ≤ 5.46×10^{−91}` (with multiplicity);
 (v) `|W(F_0) − 2G²| ≤ 6×10^{−91}`; in particular `W_0 := W(F_0) = −I_∞(F_0,F_0) − 2η²` and
     `−I_∞(F_0,F_0) = 2G²(1 ± 10^{−90}) > 0`;
     **[CORRECTED, phase 156 (`R156_003` item E1): the sign of the `2η²` term was printed `+`; the
     proof line of (v) below, `I_∞(F_0,F_0) = −2η² − W`, gives `−`.  The discrepancy `4η² < 10^{−780}`
     is invisible in both two-sided bounds of (v), so nothing downstream changes.]**
 (vi) `w_{F_0}(u) = −2G\sin(γ_1u) + r(u)` with `|r(u)| ≤ (L + 2|η|)·2\cosh(u/2)`, whence the exact
      constant of Theorem 11.14(ii) satisfies `C_{F_0} ≤ G·s_1 + L + 2|η| < G·s_1 + 10^{−90}`.

*Proof.*  (i) Gaussian decay gives (11.1) and (11.2) for all derivatives; `F_0` is real and odd.
(ii) `\deg F_0 = ∫F_0(u)·2\cosh(u/2)du = 0`, the integrand being odd (Theorem 11.13(i) for the
identity); hence `Φ_{F_0}(0) + Φ_{F_0}(1) = 0`.  For their common magnitude, with
`∫e^{−u²/2σ²}e^{αu}du = σ\sqrt{2π}e^{α²σ²/2}`,

    |Φ_{F_0}(1)| = \Big|∫e^{−u²/2σ²}\sin(γ_1u)e^{u/2}du\Big| ≤ σ\sqrt{2π}\,e^{σ²(¼−γ_1²)/2}
                 ≤ 7.52·e^{−898.5} < 10^{−390} .

(iii) `Φ_{F_0}(½+iγ) = ∫F_0(u)e^{iγu}du = \frac{σ\sqrt{2π}}{2i}\big(e^{−σ²(γ+γ_1)²/2} −
e^{−σ²(γ−γ_1)²/2}\big)`; at `γ = γ_1` this is `\frac{σ\sqrt{2π}}{2i}(e^{−2σ²γ_1²} − 1) = iG(1 −
e^{−1598…})`.  Reality of `F_0` gives the conjugate statement.
(iv) For any zero `ρ = β+iγ` write `½−ρ = c − iγ` with `|c| = |½−β| < ½` by (E2).  Then

    |Φ_{F_0}(1−ρ)| ≤ \tfrac{σ\sqrt{2π}}2 e^{σ²c²/2}\big(e^{−σ²(γ−γ_1)²/2} + e^{−σ²(γ+γ_1)²/2}\big) ,

with prefactor at most `Ge^{9/8} = 11.5814…`.  By (X19) every zero other than `ρ_1,\barρ_1` has
`|γ| ≥ 21`, so `|γ ∓ γ_1| ≥ 6.86`; summing the explicit bound over the zeros, using the unconditional
Riemann–von Mangoldt count `\#\{γ ∈ [T,T+1]\} ≤ \log T` (which counts off-line zeros too) started at
`T = 21`, gives, **with no zero list at all**,

    L ≤ Ge^{9/8}·Σ_{T ≥ 21} 2\log T\,e^{−\frac92(T−γ_1)²} ≤ 5.46×10^{−91} ,

which is `88` orders of magnitude below the margin `G(1−s_1) = 5.79×10^{−3}`.  Certified by
`certify_leakage.py`.
**[FLAGGED GAP, phase 156 (`R156_003` item E3); the mathematics above is not changed.]**  The
phrase *"with no zero list at all"* is not supported as written: explicit Trudgian-type bounds for
`S(T)` give about `6.5` ordinates per unit interval at `T = 21`, against `\log 21 = 3.04`, and they
reach `\#\{γ ∈ [T,T+1]\} ≤ \log T` only for `T ≳ 2×10^4`.  For `21 ≤ T ≲ 2×10^4` the count must be
supplied either by the verified zero list on that range (the Platt–Trudgian verification already
cited under (X19), used beyond `|\mathrm{Im}\,ρ| ≤ 21`), or by replacing `\log T` with an explicit Trudgian count.  The margin is untouched: any count
`≤ 10\log T` moves `L` to at most `5.5×10^{−90}`, which weakens the displayed `< 10^{−90}` of (vi)
to `≈ 10^{−89}` and leaves `L ≪ G(1−s_1)`.  The same caveat applies to the header of
`certify_leakage.py`.  `OPEN` as a citation item only.
(v) `W(F_0) = Σ_ρΦ_{F_0}(ρ)Φ_{F_0}(1−ρ)`; by (X19) the zero `ρ_1` is **simple**, so the terms at
`ρ_1` and `\barρ_1` contribute `2(iG)(−iG) = 2G²` up to the error of (iii), and the remaining terms
are bounded by `(\max_ρ|Φ_{F_0}(ρ)|)·L ≤ 11.59·L`.  The identity
`I_∞(F_0,F_0) = 2Φ_{F_0}(0)Φ_{F_0}(1) − W = −2η² − W` is (11.6).
(vi) is (11.16) with (ii),(iii),(iv), using `|e^{(ρ−½)u}| ≤ e^{|u|/2} ≤ 2\cosh(u/2)` (proof of
Theorem 11.14(ii)) for the leakage terms and `|e^{±u/2}| ≤ 2\cosh(u/2)` for the polar terms.  ∎
`PROVED`

**Theorem 19.21 (the exact necessary condition (C4.1); `PROVED`, unconditional).**  Let `F ∈ D^W` be
real with `\deg F = 0` and `W_F := −I_∞(F,F) > 0`, let `d > 0`, `t ∈ R`, and put
`E_{t,d} := tF + dK ∈ D^W`.  Then, identically,

    \deg E_{t,d} = d ,\qquad I_∞(E_{t,d},E_{t,d}) = \tfrac{d²}2 − t²W_F ,\qquad
    I_∞(E_{t,d},F) = −t\,W_F ,                                                         (19.3)

so that

 (i) `E_{t,d} ∈ S_χ` ⟺ `d > 0` and `t²W_F < \tfrac{d²}2 − \tfrac d2 + 2χ`;
 (ii) consequently **(b′)⁺ at level `χ` forces**, for every such `F` and every admissible `d`,

          C_F ≥ \sqrt{W_F\big(\tfrac{d²}2 − \tfrac d2 + 2χ\big)}\big/d ,
          \qquad\text{and, letting } d → ∞,\qquad \boxed{\ C_F ≥ \sqrt{W_F/2}\ }        **(C4.1)**

     with `C_F` the exact constant of Theorem 11.14(ii).

*Proof.*  (19.3): `\deg K = 1` and `\deg F = 0` (Theorem 11.13(i)); `I_∞(F,K) = ½\deg F = 0`
(Theorem 11.8(i)); `I_∞(K,K) = ½`; bilinearity.  (i) is
`R(E_{t,d}) = ½(d²/2 − t²W_F) − d/4 + χ > 0`.  (ii): if (b′)⁺ holds then `E_{t,d}` has a nonnegative
representative `E'` with `\deg E' = d` and `I_∞(E',F) = I_∞(E_{t,d},F) = −tW_F` (Theorem 11.11,
Theorem 11.13(ii),(iv)), so Theorem 11.14(ii) gives `t\,W_F ≤ C_F d`; take `t` to the supremum
allowed by (i) and let `d → ∞`.  ∎  `PROVED`

No Cauchy–Schwarz, no RH and no primitivity enter: only `\deg F = 0`.  The identity (19.3) replaces
the chain `|I_∞(E,F)| ≤ \sqrt{W(E)W_F}`, `W(E) < 2ab`, `ab ≤ (\deg E)²/4`, whose composite is sharp
only in the limit `a = b`, `d → ∞`; the sharpest classes of `S_0` are `E_{t,d}` with `a = b = d/2` and
`d` large, and the free parameter is the **degree**.

**Theorem 19.22 ((C4.1) is FALSE; `PROVED`, unconditional given (X19)).**  For `F_0` of
Definition 19.19,

    C_{F_0} ≤ G·s_1 + 10^{−90} = 0.99846016…·G + 10^{−90} < G(1 − 1.5×10^{−3})
            < \sqrt{W_{F_0}/2} = G(1 ± 10^{−90}) .

Hence (C4.1) fails at `F_0`, with relative margin `1 − s_1 = 1.53983728×10^{−3}`, i.e. absolute
margin `G(1−s_1) = 5.7897×10^{−3}`, against a leakage error `< 10^{−90}`.

*Proof.*  Lemma 19.20(v),(vi) and Proposition 19.18.  ∎  `PROVED`

**Theorem 19.23 ((b′)⁺ is false for every `χ`; `PROVED`, unconditional given (X19)).**  Put
`s_{F_0} := C_{F_0}\sqrt{2/W_{F_0}}` (the ratio whose infimum over `\deg F = 0`, `W_F > 0` is `s_*`
of §19.9); by Lemma 19.20(v),(vi) and Proposition 19.18, `s_{F_0} ≤ s_1^+ := s_1(1+10^{−89})^{1/2}`.
Fix `χ ∈ R` and let `d` satisfy

    d²(1 − s_{F_0}²) > d − 4χ \qquad\big(\text{sufficient: } d²(1 − (s_1^+)²) > d − 4χ;\ \text{at } χ = 0:\ d > d_0^+ := (1−(s_1^+)²)^{−1} = 324.9598266…\big) .

Pick `t > 0` with `s_{F_0}²d²/2 < t²W_{F_0} < d²/2 − d/2 + 2χ` — a nonempty range, by the displayed
inequality; it suffices that `(s_1^+)²d²/2 < t²W_{F_0}` — and put `E := tF_0 + dK`.
Then `E ∈ S_χ`, and **there is no `E' ∈ D^W` with `E' ≥ 0`,
`E' ≢ 0`, `E − E' ∈ 𝓝_∞`.**  In particular clause (b′)⁺ of Definition 19.10 is false for `ξ`, at
every `χ`, and `h⁰_{RR}^{+}` fails clause (b′).
**[CORRECTED, phase 156 (`R156_003` item E2): the window and threshold were stated with `s_1` in
place of `s_{F_0}`.  The proof reaches only `t²W_{F_0} ≤ s_1²d²/2·(1+10^{−89})`, so the sliver
`t²W_{F_0} ∈ (s_1²d²/2,\ s_1²d²/2·(1+10^{−89})]` of the old window was not covered and
`(1−s_1²)^{−1}` was a sliver too low as a threshold.  `d_0^+` agrees with `(1−s_1²)^{−1}` in every
displayed digit.  Downstream, Theorem 19.25 needs one admissible `t` (its Step 3 is restated
accordingly), Corollary 19.24 only cancels `N`, Theorem 19.30 replaces `C` by `C'`, and the certified
instance below lies `≈ 26` units inside the window; no statement uses the exact `s_1` form.]**

*Proof.*  `E ∈ S_χ` by Theorem 19.21(i).  If such an `E'` existed then, by Theorem 11.11 and
Theorem 11.13(ii),(iv), `\deg E' = d` and `I_∞(E',F_0) = I_∞(E,F_0) = −tW_{F_0}`, so
Theorem 11.14(ii) would give `t\,W_{F_0} ≤ C_{F_0}d`, i.e.
`t²W_{F_0}² ≤ C_{F_0}²d²`, i.e. `t²W_{F_0} ≤ s_{F_0}²d²/2`, contradicting the choice of `t`.  For the
bound on `s_{F_0}`: `C_{F_0} ≤ Gs_1 + 10^{−90}` and `W_{F_0} = 2G²(1±10^{−90})` give
`s_{F_0}² ≤ s_1²(1+10^{−89})`.  ∎  `PROVED`

**Certified instance** (`certify_sF.py`, mpmath, `mp.dps = 40`).  At `χ = 0`, `d = 400`: the
admissible window for `t²W_{F_0}` is `(s_{F_0}²·80000,\ 79800) ⊇ (79753.8157…·(1+10^{−89}),\ 79800)`,
nonempty.  Taking
`t²W_{F_0} = 79780`, i.e. `t = 53.11911…` with `W_{F_0} = 2G² = 28.274333882…`, the class
`E = 53.11911…·F_0 + 400·K` has

    \deg E = 400 ,\quad I_∞(E,E) = 80000 − 79780 = 220 > 200 = ½\deg E ,\quad R(E) = 110 − 100 = 10 > 0 ,
    |\mathrm{Im}\,Φ_E(ρ_1)| = tG = 199.72481… \ >\ ½s_1\deg E = 199.69203… ,

while the non-sharp bound `\sqrt{ab} = 200` is **satisfied**.  The witness passes every necessary
condition available before Lemma 19.17 and fails exactly that one.  Its rulings are
`200 ± 10^{−390}` and `W_{F_0} = 9π` exactly in the Gaussian normalization of Definition 19.19.

**Corollary 19.24 ((b′)⁺_{st} is false too; `PROVED`).**  The stable weakening of Corollary 19.13 —
*some positive multiple `N·E` is `𝓝_∞`-equivalent to a nonzero nonnegative class* — fails at the same
witness.

*Proof.*  If `N·E − E' ∈ 𝓝_∞` with `E' ≥ 0`, `E' ≢ 0`, then `\deg E' = N\deg E` and
`I_∞(E',F_0) = N\,I_∞(E,F_0)`, so Theorem 11.14(ii) gives `N t W_{F_0} ≤ C_{F_0}Nd`: the factor `N`
cancels and the contradiction is that of Theorem 19.23.  ∎  `PROVED`

Stabilisation buys nothing, because the constraint is homogeneous of degree `0` in the class.

### 19.7 The frame defect theorem

**Theorem 19.25 (frame defect: no `h⁰` satisfies (a), (b′), (c) for `ξ`; `PROVED`, unconditional
given (X19)).**  There is **no** function `h⁰ : D^W → R_{≥0}` satisfying clauses (a), (b′), (c) of
Theorem 12.3, for any constant `χ ∈ R`.  Equivalently, the hypothesis of Theorem 12.3 is
**unsatisfiable** for `ξ`, and Theorem 12.4's verdict for `Ξ_a` holds verbatim for `ξ`.

*Proof.*  Suppose `h⁰` satisfies (a), (b′), (c) with constant `χ`.

*Step 1 (`h⁰` vanishes in degree `≤ 0`).*  If `h⁰(E) > 0` and `\deg E ≤ 0`, then (b′) gives `E' ≥ 0`,
`E' ≢ 0` with `E − E' ∈ 𝓝_∞`; by Theorem 11.13(ii),(iv) `\deg E' = \deg E ≤ 0`, contradicting
`\deg E' > 0` (Theorem 11.13(i)).

*Step 2 ((c) forces `h⁰ ≥ R` above degree `1`).*  Let `\deg E > 1`.  Then
`\deg(K−E) = 1 − \deg E < 0` by linearity of `\deg` (Theorem 11.13(iv)) and `\deg K = 1`
(Theorem 11.7, Theorem 11.8(v)), so `h⁰(K−E) = 0` by Step 1; and (c) together with the Serre symmetry
`R(K−E) = R(E)` of Theorem 19.2 gives `h⁰(E) ≥ R(E)`.

*Step 3 (the witness).*  Take `E := tF_0 + dK` as in Theorem 19.23, with `d` large enough that both
`d > 1` and `d²(1−s_{F_0}²) > d − 4χ` (for instance `d²(1−(s_1^+)²) > d − 4χ`).  Then `\deg E = d > 1` and `R(E) > 0`, so `h⁰(E) ≥ R(E) > 0` by
Step 2, so (b′) supplies `E' ≥ 0`, `E' ≢ 0` with `E − E' ∈ 𝓝_∞` — which Theorem 19.23 forbids.  ∎
`PROVED`

*Provenance of Lemma 19.25a – Remark 19.25c.  Taken from
`03-research/phase-156-row-d-per-window-converse/R156_002_R1_TRUNCATION.md` (Lemmas 1.2, 3.1,
3.2, 4.1, 5.1, Proposition 2.1, Theorem 6.1, Proposition 7.1, Remarks 8.3, 8.4), as amended in place
per `R156_003_AUDIT_R1.md` (A1–A10); only what §5 of `R156_003` clears is carried.  Theorem
19.25 as stated quantifies over `h⁰` defined on all of `D^W`; what follows removes that, and needs
no new certified constant.*

**The ratio `s_F` and the seminorm `N`.**  For real `F ∈ D^W` with `\deg F = 0` and
`W_F := −I_∞(F,F) > 0` (as in Theorem 19.21) put `s_F := C_F\sqrt{2/W_F}`, with `C_F` the exact
constant of Theorem 11.14(ii); so `s_* = \inf s_F` (§19.9), and Theorems 19.21, 19.23 and 19.25 use
of `F_0` only `F_0 ∈ D^W` real, `\deg F_0 = 0` exactly, `W_{F_0} > 0` and `s_{F_0} < 1`
(`R156_003` D1).  For measurable `g` put `N(g) := ∫|g(u)|\,2\cosh(u/2)\,du`, and
`S_2 := Σ_ρ|ρ−½|^{−2}` over the zeros of `ξ` with multiplicity.  Fix a cutoff `ϑ ∈ C_c^∞(R)`,
**even**, `0 ≤ ϑ ≤ 1`, `ϑ = 1` on `[−1,1]`, `\mathrm{supp}\,ϑ ⊆ [−2,2]`; put
`A := 1 + \|ϑ'\|_∞ + \|ϑ''\|_∞`, `ϑ_R(u) := ϑ(u/R)`, and

    F_R := F_0\,ϑ_R ∈ C_c^∞(R) ,\qquad D_R := F_0 − F_R .

(The cutoff is written `ϑ` because `χ` is the constant of Definition 19.1.)  Fix also a real odd
`B ∈ C_c^∞(R)` with `Φ_B(0) = 1` — e.g. `B := −uψ(u)/c_ψ` with `ψ ≥ 0` an even bump, `ψ ≢ 0`,
`c_ψ := ∫uψ(u)\sinh(u/2)du > 0` — so `Φ_B(1) = −1`.

**Lemma 19.25a (truncation of the witness; `PROVED`, given (X19), (E2), (E3d)).**
 (i) *(seminorm bounds, unconditional given (E3d))*  For real `E, F, F' ∈ D^W`: `C_{F+F'} ≤ C_F + C_{F'}`;
     `|Φ_F(0)| + |Φ_F(1)| ≤ N(F)`; `C_F ≤ N(F) + S_2\,N(F'')`; and `|I_∞(E,F)| ≤ C_F\,N(E)` for
     **every** `E ∈ D^W`, effective or not.
 (ii) *(the constant; `CLASSICAL` import (X30))*  `S_2 ≤ 0.0465`.
 (iii) `F_R` is real and **odd**, `\mathrm{supp}\,F_R ⊆ [−2R,2R]`, and `\deg F_R = 0` **exactly**.
 (iv) `s_{F_R} → s_{F_0}` as `R → ∞`.  Explicitly, for `R ≥ R_0(ϑ) := 6\sqrt{40 + 2\log A}`:
      `N(D_R) ≤ 4e^{−R²/36}`, `C_{D_R} ≤ 80ARe^{−R²/36} ≤ 10^{−6}`,
      `C_{F_R} ≤ Gs_1 + 10^{−6} + 10^{−90}`, `|W_{F_R} − W_{F_0}| ≤ 9.3×10^{−5}`, and

          s_{F_R} ≤ s_1 + 3.6×10^{−6} < \bar s := 0.998464 ,\qquad
          d_0^{(R)} := (1 − s_{F_R}²)^{−1} ≤ (1−\bar s²)^{−1} < 325.78 ,

      with `|Φ_{F_R}(0)| = |Φ_{F_R}(1)| < 2×10^{−17}`.
 (v) *(primitive variant)*  If moreover `(10^{−390} + 4e^{−R²/36})(N(B)+N(B'')) ≤ 10^{−6}`, then
     `F_R^♭ := F_R − Φ_{F_R}(0)B` lies in `P_c^∞ := \{F ∈ C_c^∞(R) \text{ real} : Φ_F(0) = Φ_F(1) = 0\}`,
     is odd, and has `W_{F_R^♭} > 0`, `s_{F_R^♭} ≤ s_1 + 8×10^{−6} ≤ 0.998469`,
     `(1 − s_{F_R^♭}²)^{−1} < 326.9`.

The explicit constants of (iv), (v) use (ii); the existence of an `R` with `s_{F_R} < 1` (resp.
`s_{F_R^♭} < 1`) needs only `S_2 < ∞`, i.e. (E3d) with `|ρ−½| ≥ |γ_ρ|`.

*Proof (condensed).*  (i) (11.16) is linear in `F`, so `w_{F+F'} = w_F + w_{F'}` and the supremum
defining `C` is subadditive.  `e^{±u/2} ≤ 2\cosh(u/2)` gives the polar bound.  For the zero part of
(11.17), the two integrations by parts behind (11.2) hold **pointwise** at `s = 1−ρ`, where
`σ − ½ = ½ − β ∈ (−½,½)` by (E2), so `|Φ_F(1−ρ)| ≤ |ρ−½|^{−2}∫|F''|e^{(½−β)t}dt ≤ |ρ−½|^{−2}N(F'')`;
sum over `ρ`.  Finally Theorem 11.14(i) gives `I_∞(E,F) = ∫E\,w_F`, absolutely convergent, so
`|I_∞(E,F)| ≤ C_F∫|E|\,2\cosh(u/2)`, with no sign hypothesis on `E`.
(ii) By (X30), `Σ_ρ\mathrm{Re}(1/ρ) = 1 + ½γ_E − ½\log 4π = 0.0230957…`, a series of positive terms
`β/|ρ|²`, unconditionally.  The zero multiset is invariant under `ρ ↦ 1−\barρ` ((E2) and reality),
and for `0 < β < 1`, `\mathrm{Re}\tfrac1ρ + \mathrm{Re}\tfrac1{1−\barρ} ≥ (1+γ²)^{−1}`; averaging,
`Σ_ρ(1+γ²)^{−1} ≤ 0.04620`.  Every zero has `|γ| > 14` (X19), so
`|ρ−½|^{−2} ≤ γ^{−2} ≤ (1+14^{−2})(1+γ²)^{−1}` and `S_2 ≤ 1.0052·0.04620 < 0.0465`.  No step
assumes RH.  Only `S_2 ≤ 1` is used below.
(iii) `ϑ_R` is even and `F_0` odd (Lemma 19.20(i)), so `F_R(u)\,2\cosh(u/2)` is odd and integrable:
`\deg F_R = 0` with no error term.
(iv) Write `g := e^{−u²/18}`.  From `F_0'' = g[(u²/81 − 1/9 − γ_1²)\sin γ_1u − (2γ_1u/9)\cos γ_1u]`
and `D_R'' = F_0''(1−ϑ_R) − 2F_0'ϑ_R' − F_0ϑ_R''`, which vanishes on `|u| < R`, one gets
`|D_R''| ≤ A\,u²g\,\mathbf 1_{|u|≥R}` for `R ≥ 18`.  For `u ≥ 18`, `g(u)\,2\cosh(u/2) ≤ 2e^{−u²/36}`,
whence `N(D_R) ≤ 4e^{−R²/36}`, `N(D_R'') ≤ 76ARe^{−R²/36}`, and by (i) with `S_2 ≤ 1`,
`C_{D_R} ≤ 80ARe^{−R²/36}`; with `R = 6\sqrt L` this is `≤ 480Ae^{−L/2} ≤ 10^{−6}` once
`L ≥ 2\log(4.8×10^8A)`, which `R ≥ R_0(ϑ)` ensures.  Then `C_{F_R} ≤ C_{F_0} + C_{D_R}` by (i) and
Lemma 19.20(vi).  Next `W_{F_R} − W_{F_0} = 2I_∞(F_0,D_R) − I_∞(D_R,D_R)`, bounded by (i) by
`C_{D_R}(2N(F_0) + N(D_R))` with `N(F_0) ≤ 4Ge^{9/8} < 46.33`; so `|ΔW| ≤ 9.3×10^{−5}`, and with
`W_{F_0} = 2G²(1±10^{−90})`, `2G² = 9π` (Lemma 19.20(v)), `\sqrt{W_{F_R}/2} ≥ G(1 − 3.3×10^{−6})`.
Hence `s_{F_R} ≤ (s_1 + 2.7×10^{−7})(1 + 3.3×10^{−6}) ≤ s_1 + 3.6×10^{−6} = 0.9984638…`, and
`1 − \bar s² = 3.06964×10^{−3}`.  Oddness gives `Φ_{F_R}(1) = −Φ_{F_R}(0)`, and
`|Φ_{F_R}(0)| ≤ |η| + N(D_R) < 10^{−390} + 4e^{−40}` by Lemma 19.20(ii) and (i).  The same
estimates with `R → ∞` give `C_{D_R} → 0`, `W_{F_R} → W_{F_0}`, hence `s_{F_R} → s_{F_0}`.
(v) `Φ_{F_R^♭}(0) = 0`, and oddness gives `Φ_{F_R^♭}(1) = 0`.  With `D' := D_R + Φ_{F_R}(0)B`,
(i) gives `C_{D'}, N(D') ≤ 2×10^{−6}`; repeating (iv) with `D'` gives `|ΔW| < 1.86×10^{−4}`,
`s ≤ (s_1 + 5.4×10^{−7})(1 + 6.7×10^{−6}) ≤ s_1 + 8×10^{−6}`, and `1 − 0.998469² = 3.0597×10^{−3}`.  ∎
`PROVED`

*Certified instance, carried over (arithmetic only).*  At `χ = 0`, `d = 400`, the window of
Theorem 19.23 with `F_R` in place of `F_0` is `(s_{F_R}²·80000,\ 79800) ⊇ (79754.43,\ 79800)` (for
`F_R^♭`: `⊇ (79755.2,\ 79800)`), and `t²W_{F_R} = 79780` gives `\deg E = 400`, `I_∞(E,E) = 220`,
`R(E) = 10`, exactly as in the certified instance of Theorem 19.23; `t` moves from `53.11911…` only at
the sixth significant digit or later, and is not needed numerically.

**Corollary 19.25b (the frame defect theorem on the small domain; `PROVED`, given (X19), (E2),
(E3d)).**  Let `𝒟_c := C_c^∞(R) ⊕ RK` and `𝒟_p := P_c^∞ ⊕ RK` (direct, since `K > 0` everywhere,
Theorem 11.7(i)); `𝒟_p` is the linear span of `𝒢_min := \{nF,\ K−nF : F ∈ P_c^∞,\ n ∈ Z\}`, the set on
which Theorem 12.3's proof evaluates `h⁰`, and both are `σ_K`-stable.  For `𝒟 ∈ \{𝒟_c, 𝒟_p\}` there
is **no** `h⁰ : 𝒟 → R_{≥0}` satisfying

  (a)_𝒟 `h⁰ ≥ 0` on `𝒟`;  (b′)_𝒟 if `E ∈ 𝒟` and `h⁰(E) > 0`, there is `E' ∈ D^W`, `E' ≥ 0`,
  `E' ≢ 0`, `E − E' ∈ 𝓝_∞`;  (c)_𝒟 `h⁰(E) + h⁰(K−E) ≥ R(E)` whenever `E, K−E ∈ 𝒟`,

for any `χ ∈ R`; and the same holds with (b′)_𝒟 replaced by its stable form (b′)_{st} of
Theorem 19.12 restricted to `𝒟`.  Requiring `E' ∈ 𝒟` in (b′)_𝒟, or reading the equivalence modulo the
finer `𝓝_∞ ∩ 𝒟` or modulo the radical of `I_∞|_𝒟` (both `0`, Remark 19.25c(ii)), only strengthens the hypothesis, so the conclusion
covers those readings too.

**Localised form.**  Fix `χ`, let `F := F_R` (for `𝒟_c`) or `F := F_R^♭` (for `𝒟_p`) as in
Lemma 19.25a, take `d > 1` with `d²(1 − s_F²) > d − 4χ` and `t > 0` with
`s_F²d²/2 < t²W_F < d²/2 − d/2 + 2χ`, and put `E_w := tF + dK`.  On **any** set `𝒟 ⊆ D^W` containing
the pair `\{E_w,\ K−E_w\}`, no `h⁰ ≥ 0` satisfies (b′) at `E_w` and at `K−E_w` together with (c) at
`E_w`.

*Proof.*  Theorem 19.21 and the proof of Theorem 19.23 use of `F_0` only the four properties listed
above, so they hold for `F`, with `s_{F_0}` replaced by `s_F`: `\deg E_w = d`, `R(E_w) > 0`, and no
`E' ≥ 0`, `E' ≢ 0` has `E_w − E' ∈ 𝓝_∞`, nor `NE_w − E' ∈ 𝓝_∞` for any `N ≥ 1` (the `N` cancels as
in Corollary 19.24).  Lemma 19.25a supplies `F` with `s_F < 1`, so `d` and `t` exist.  Now
`E_w ∈ 𝒟_p ⊆ 𝒟_c`, and `K−E_w = −tF + (1−d)K` lies there too.  *Step 1:* `\deg(K−E_w) = 1−d < 0`,
so (b′) (or (b′)_{st}) at `K−E_w` would give `E' ≥ 0`, `E' ≢ 0` of degree `(1−d)` (resp.
`N(1−d)`) `< 0`, against Theorem 11.13(i); hence `h⁰(K−E_w) = 0`.  *Step 2:* (c) at `E_w` gives
`h⁰(E_w) ≥ R(E_w) > 0`; the Serre symmetry is not needed.  *Step 3:* (b′) (or (b′)_{st}) at `E_w`
supplies the forbidden `E'`.  ∎  `PROVED`

**Remark 19.25c (`PROVED`, new).**
 (i) *On the bare set `𝒢_min` the hypothesis is RH itself.*  For `h⁰` defined only on `𝒢_min`, with
     (a), (b′), (c) restricted to it and `χ` existential as in (12.1), the hypothesis of Theorem 12.3
     is **satisfiable if and only if RH holds**.  ⇐: under RH, `Φ_F(1−ρ) = \overline{Φ_F(ρ)}` for real
     `F`, so `I_∞(F,F) = −Σ_ρ|Φ_F(ρ)|² ≤ 0` for `F ∈ P_c^∞` by (11.6); take `χ = 0` and `h⁰ ≡ 0`.
     Then (a) holds, (b′) is vacuous, and `R(K−nF) = R(nF) = ½n²I_∞(F,F) ≤ 0` (Theorem 19.2,
     `\deg F = 0`), with `R(0) = R(K) = 0`.  ⇒: Theorem 12.3's proof evaluates `h⁰` only at `nF` and
     `K−nF` and applies (c) only at `E = nF`; the ample class `F + 2mK` of its Step 1 enters only
     through `I_∞(\cdot,F+2mK)`.  So it runs verbatim on any `𝒟 ⊇ 𝒢_min`.  Hence no unconditional
     non-existence theorem for `h⁰` on `𝒢_min` can be proved unless RH is false, and the kill of
     Corollary 19.25b needs a **linear** domain: it uses the pair `\{E_w, K−E_w\}`, of degrees
     `d > d_0^{(R)}` and `1−d`.  No lower bound on the degree of an arbitrary witness is claimed; that
     is governed by the unknown `s_*` and by witnesses of other shapes.  This sharpens the first
     paragraph of §19.9.
 (ii) *`𝓝_∞ ∩ (C_c^∞ ⊕ RK) = 0`.*  If `N = G + cK ∈ 𝓝_∞` with `G ∈ C_c^∞`, then by (11.14)
     `Φ_G(ρ) = Φ_N(ρ) − cξ(ρ) = 0` at every zero, so `G = 0` by the proof of Theorem 11.12, and then
     `Φ_N(0) = cξ(0) = c/2 = 0`; a fortiori `𝓝_∞ ∩ 𝒟_p = 0`.  Moreover the radical of `I_∞`
     restricted to `𝒟_p` is `0`: if `N = G + cK` pairs to zero with `P_c^∞ ⊕ RK`, then, since
     `I_∞(K,\cdot) = ½\deg = 0` on `P_c^∞`, (11.6) and Lemma 11.9 force `Φ_G(ρ) = 0` at every zero,
     so `G = 0` as before and `c = 0` by pairing with `K`.  So on the
     small domain no two classes are identified modulo the radical: `F_0` cannot be exchanged for an
     `𝓝_∞`-equivalent compactly supported class for free, and the replacement `F_0 ↦ F_R` is
     **analytic** — a different class, admissible because the inequality it must satisfy is strict
     and open.  This is unlike the curve model, where `D^W_C/𝓝^C_∞` is `(2+2g)`-dimensional and the
     evaluation map is onto already from the `δ_m` (proof of Theorem 21.8), so every class, the
     witness of Theorem 21.14 included, has a finitely supported representative modulo `𝓝^C_∞`.
     Whether `F_0` itself is `𝓝_∞`-equivalent to an element of `𝒟_c` is `OPEN` and not needed.
 (iii) *`s_*` is a compactly supported constant.*  For every real `F ∈ D^W` with `\deg F = 0` and
     `W_F > 0` there are real `F_k ∈ C_c^∞`, `\deg F_k = 0`, with `s_{F_k} → s_F`; if `F ∈ P^W`, the
     `F_k` may be taken in `P_c^∞`.  So `s_*` of §19.9 may be computed over `C_c^∞`, and its primitive
     analogue over `P^W` equals that over `P_c^∞`.  *Proof.*  Truncate by `ϑ_R` (by (11.1) for
     `j ≤ 2`, `N` of the error and of its second derivative tend to `0`); mollify with an even `φ_δ`
     on the fixed compact support, where `N ≤ 2\cosh(R+1)\|\cdot\|_{L¹}`; then restore `\deg = 0` by
     subtracting a multiple of a fixed even bump `B_1 ≥ 0` (for which `Φ_{B_1}(0) = Φ_{B_1}(1)`),
     and, in the primitive case, restore `Φ(0) = Φ(1) = 0` with `B_1` and `B` above, the coefficients
     being `≤ N` of the error by Lemma 19.25a(i).  By Lemma 19.25a(i), `C` and `W` converge, and
     `W_F > 0` makes `s = C\sqrt{2/W}` continuous at `F`.  ∎

**Remark 19.26 (what Theorem 19.25 does and does not say).**

* It does **not** contradict Theorem 12.3, which remains `PROVED`: an implication with an
  unsatisfiable hypothesis.  Theorem 12.3 keeps its label and loses its use — the route *"construct
  an `h⁰`, obtain RH"* is closed for `ξ`.
* It does **not** refute RH and proves nothing about the zeros: the witness is a statement about the
  nonnegative cone of `D^W`, and `Ξ_a` satisfies the same obstruction (Theorem 12.4, Theorem 19.15)
  while (a) and (c) hold there too.
* It does say that the `Ξ_a` falsifier was all along detecting a defect of the **frame** — `D^W` with
  `\deg` and its nonnegative cone — and not a separation between `ξ` and `Ξ_a`.
* The operative cause is localisable: **clause (c) with the Serre symmetry demands `h⁰(E) ≥ R(E)` on
  the whole half-space `\deg E > 1`, while the classes admitting a nonnegative representative are
  strictly fewer than `\{R > 0\}` there.**  The `¼m²` growth demanded of `h⁰` is a demand about
  large-degree classes, and large degree is exactly where Lemma 19.17 bites.  `χ` cannot repair it:
  `χ` shifts `R` by a constant while the gap grows like `d²(1−s_1²)`.

**Remark 19.27 (epistemic type, and the load-bearing hypothesis).**  Theorems 19.22, 19.23 and 19.25
are unconditional, but **computer-assisted through (X19) alone**; no other numerical input enters, and
(E2) with (E3d) do all the remaining work, exactly as in the proof of Theorem 11.14.  **Simplicity of
`ρ_1` is load-bearing.**  If `ρ_1` had multiplicity `m ≥ 2` the zero sum would give
`w_{F_0}(u) = −2mG\sin(γ_1u)` and `W_{F_0} = 2mG²`, so `C_{F_0} = mGs_1` while
`\sqrt{W_{F_0}/2} = G\sqrt m`; and `mGs_1 ≥ G\sqrt m` already at `m = 2`, since
`2s_1 = 1.9969 > 1.4142`.  The refutation fails at `m = 2`.

**Theorem 19.28 (the same holds for every admissible `Z` with a simple isolated on-line zero;
`PROVED` modulo the corresponding verified-zero input).**  Every statement of §§19.5–19.7 holds
verbatim for `ξ_K`, with `ξ_K`, `K_K`, `\deg_K`, `I_∞^{(K)}` replacing their `ξ`-counterparts and
`\deg_K K_K = r`, `I_∞^{(K)}(K_K,K_K) = r²/2`; (19.3) becomes `\deg E_{t,d} = rd`,
`I_∞^{(K)}(E,E) = r²d²/2 − t²W_F`, and the threshold is `d_0^{(K)} = (1 − (s_1^{(K)})²)^{−1}` with
`s_1^{(K)} = s(γ_1^{(K)},π/2)` at the lowest simple isolated on-line zero of `ξ_K`.  The only input to
be re-supplied per field is the analogue of (X19); it is available for every field in which a low zero
is known to be simple and isolated.  Smaller lowest ordinate gives smaller `s_1^{(K)}`, hence
refutation at smaller degree.

*Proof.*  Each statement of §§19.5–19.7 uses only: bilinearity of `I_∞^{(K)}`; `\deg_K` linear,
`𝓝_∞`-invariant and positive on nonzero nonnegative classes (Theorem 11.13, transported);
`𝓝_∞^{(K)}` the radical (Theorem 11.11); the comparison identity (11.6); the exact bounded-density
constant of Theorem 11.14(ii); and the Gaussian computation of Lemma 19.20, which depends on the
zero data only through the analogue of (X19).  Substituting the constants above leaves every proof
unchanged.  ∎  `PROVED`

### 19.8 The geometric diagnosis

**Restatement 19.29 (`RESTATEMENT` — the classical half, import **(X26)**; `PROVED` — the arithmetic
half).**  On a smooth projective surface `S` over an algebraically closed field, with `H` ample:

 (i) *(Riemann–Roch with Serre duality)* `h⁰(D) + h⁰(K_S−D) ≥ χ(𝒪_S) + ½D·(D−K_S)` — Hartshorne,
     *Algebraic Geometry*, GTM **52**, Ch. V, Theorem 1.6;
 (ii) *(the positive cone is filled by the effective cone)* if `D² > 0` and `D·H > 0`, then `nD` is
      effective for `n ≫ 0`; equivalently `D` is **big** — Hartshorne Ch. V, 1.8; Lazarsfeld,
      *Positivity in Algebraic Geometry I*, Ergebnisse **48**, §2.2;
 (iii) *(Hodge index)* Hartshorne Ch. V, Theorem 1.9 — the theorem whose proof Remark 12.3a transports
      with `H = 2K`;
 (iv) *(the arithmetic half)* In `D^W` the analogue of (i) is **free**: Theorem 19.6 gives (a) and (c)
      unconditionally, for every `χ`, with the **geometric** constant.  The surface inequality
      `D² ≤ (D·H)²/H²` at `H = 2K` has, in `D^W`, the **shape**
      `I_∞(E,E) ≤ 2ab ≤ (\deg E)²/2 = (\deg E)²/I_∞(2K,2K)`; this is a dictionary of shapes and **no
      bound is asserted**.  Only the second inequality is unconditional (`\deg E = a+b`).  The first
      is `W(E) ≥ 0` by (11.6) — Castelnuovo's inequality (Restatement 19bis.13(ii)), which for every
      real `E` is RH ((1.9)–(1.10); Theorem 20.38 (W1)) — and it is neither proved nor used here.
      **[phase 158: reworded per `R158_003` §6 item 1; the printed text read as if the bound were
      asserted.  Theorem 19.6(ii) proves clause (c) only.]**  But the analogue of (ii) is **false**: by Theorem 19.23 and
      Corollary 19.24, `R(E) > 0` and `\deg E > 0` do not imply that `E`, or any positive multiple of
      `E`, is `𝓝_∞`-equivalent to a nonzero nonnegative class.  The deficit is measured exactly by
      `s(γ,θ) = \sup_u|\cos(γu+θ)|/\cosh(u/2) < 1`, whose geometric analogue is `1`.

*Proof of (iv).*  Clauses (a) and (c) are Theorem 19.6(i),(ii).  The shape: `I_∞(E,E) = 2ab − W(E)`
is (11.6); `2ab ≤ (a+b)²/2 = (\deg E)²/2` is `(a−b)² ≥ 0`; and `I_∞(2K,2K) = 4·½ = 2`.  The failure of the
analogue of (ii) is Theorem 19.23 and
Corollary 19.24; the constant is Lemma 19.17 with Proposition 19.18.  ∎  `RESTATEMENT`

**The diagnosis.**  In geometry the effective cone *fills* the positive cone, so the support function
of the effective cone in any direction equals that of the positive cone.  In `D^W`, effectivity means
*pointwise nonnegativity of a single radial density on the modulus line*, so the image of the
nonnegative cone under `(\deg, (Φ_{E'}(ρ))_ρ)` is a **moment cone**, and a moment cone is strictly
thinner than the positive cone of the form: the degree weight `2\cosh(u/2)` grows while the
zero-datum weight `\cos(γu+θ)` oscillates, and the ratio of their suprema is exactly `s(γ,θ) < 1`.
Lemma 19.17 is the analogue of the nef/Castelnuovo pairing bound, with an extra strict factor that
geometry does not have.  The named cause: **`D^W` retains the intersection theory of `C × C` and
discards its linear systems** — it supplies far too few nonnegative classes relative to how many
classes `I_∞` declares positive, whereas in geometry the missing classes come from the rest of the
Néron–Severi group.  Theorem 19.25 says one cannot keep the first without the second.

### 19.9 The two repair horns, as they stand

Theorem 12.3's proof applies (b′) at `E = K − nF` (`\deg = 1`) and at `E = nF` (`\deg = 0`), and
applies (c) **only** at `E = nF` (`\deg = 0`); Proof 2 of Theorem 19.11 applies the clause at
`rF + K` (`\deg = 1`).  The load-bearing degrees are therefore `0` and `1`, both far below the
threshold `d_*` at which the witnesses of Theorem 19.23 live.  Two repairs are open; §20 takes up the
second.  **[phase 156: on the bare set `𝒢_min` of these load-bearing classes the hypothesis of Theorem 12.3
is equivalent to RH (Remark 19.25c(i)); the frame defect theorem acts on its linear span
`P_c^∞ ⊕ RK` and on `C_c^∞ ⊕ RK` (Corollary 19.25b), through the pair `\{E_w, K−E_w\}`.]**

**Horn A — weaken (c) by a defect vanishing where it is used.**  For `Δ : R → R_{≥0}` with
`Δ(0) = Δ(1) = 0` and `Δ` symmetric under `d ↦ 1−d` (so that the Serre symmetry of Theorem 19.2 is
respected), let

    (c′)\qquad h⁰(E) + h⁰(K−E) ≥ R(E) − Δ(\deg E)\qquad\text{for every } E ∈ D^W .

Theorem 12.3's proof is intact under (c′) for any `Δ` with `Δ(0) = 0`, since (c) is used only at
`E = nF` of degree `0`, and Steps 1, 2, 4 do not use (c) at all; in particular the `¼m²` growth
survives.  Writing `s_* := \inf\{C_F\sqrt{2/W_F}\}` over real `F ∈ D^W` with `\deg F = 0` and
`W_F > 0`, and `d_* := (1−s_*²)^{−1}`, the strongest admissible defect is

    Δ(d) = \max\Big(0,\ \tfrac{d²}4(1−s_*²) − \tfrac d4\Big) ,

because the witnesses of Theorem 19.23 have `R(E_{t,d})` ranging up to that value.  Horn A is
coherent but blocked twice: the degree-gated candidate fails (c′) at `E = dK` (the canonical ray is
nonnegative at every degree, so a degree gate switches `h⁰` off exactly where `R` is largest and
legitimately positive), and the candidate gated by the necessary conditions satisfies (c′) only under
RH — which is useless in a transfer whose conclusion is RH.  The binding obstacle is the **sufficiency
half of the moment problem**: proving (c′) unconditionally for the gated candidate.  A further
technical repair is required in that argument — its Cauchy–Schwarz step drops the polar term
`η_F(a−b)` and is valid only for **primitive** test classes, and `F_0` is not primitive — so the gate
must be taken by primitive test classes.  `OPEN`.

**Horn B — enlarge the class of representatives.**

**Theorem 19.30 (the enlargement test; `PROVED` given (X19)).**  Let `𝓔'` be any cone of classes of
`D^W` playing the role of "nonnegative" in (b′), and suppose it has the two properties Theorem 12.3's
proof actually uses:

    (T1_cone)\quad \deg E' > 0 \text{ for every } E' ∈ 𝓔' ∖ \{0\}    \qquad[\text{Steps 2 and 4}]
    (T2_cone)\quad C'_X := \sup_{E'∈𝓔'} |I_∞(E',X)|/\deg E' < ∞      \qquad[\text{Step 1}]

Then the hypothesis of the corresponding transfer theorem is satisfiable **only if**

    C'_{F_0} ≥ \sqrt{W_{F_0}/2} = G ,\qquad\text{i.e.}\qquad C'_{F_0}/C_{F_0} ≥ 1/s_1 = 1.001542… .

*Proof.*  Theorems 19.21, 19.23 and 19.25 use only (T1_cone), (T2_cone) and bilinearity; replace `C` by `C'`
throughout.  If `C'_{F_0} < G` then the witness `E = tF_0 + dK` with `d` large lies in `S_χ` and
outside `𝓔' + 𝓝_∞`, and Steps 1–3 of Theorem 19.25 close as before.  ∎  `PROVED`

**[phase 156, Horn B on the small domain (`R156_002` Remark 8.1, `PROVED`, same proof).]**  Theorem
19.30's proof uses of `F_0` only the four properties listed before Lemma 19.25a, with `C` replaced by
`C'`.  So for `h⁰` defined only on `𝒟_c = C_c^∞ ⊕ RK` its conclusion holds with `F_R` in place of
`F_0`: a cone `𝓔'` with (T1_cone), (T2_cone) can support the small-domain transfer only if
`C'_{F_R} ≥ \sqrt{W_{F_R}/2} ≥ G(1 − 3.3×10^{−6})`.  Truncation neither closes nor reopens Horn B:
for a general `𝓔'`, `C'_{D_R}` is not controlled by `C_{D_R}` ((T2_cone) gives finiteness, not size),
and the B4 row of the table below was computed at `F_0` (recomputing the traces `t_n(F_R)` is `OPEN`
and not needed, since B4 passes).  **Horn B (the residual R2 of the phase-155 record) stays `OPEN`.**

So Horn B is a single inequality: the enlargement must strictly raise the support function at `F_0`
past `G`, i.e. contain classes more extreme in the `F_0` direction than any nonnegative density —
while (T2_cone) still demands boundedness in every direction.  Of the candidates defined without naming a
zero:

| candidate cone `𝓔'` | verdict |
|---|---|
| **B1.** positive-type classes `E' = G ⋆ G^∨` | `REFUTED` — `Φ_{E'}(s) = Φ_G(s)Φ_G(1−s)`, so `\deg E' = 2Φ_G(0)Φ_G(1) = 0` for primitive `G` while `E' ≢ 0`: **(T1_cone) fails**, and with it Step 4's contradiction and Step 1's ampleness |
| **B2.** classes with `Φ_{E'} ≥ 0` on `\mathrm{Re}\,s = ½` | `REFUTED` — positive-definiteness gives `|E'(u)| ≤ E'(0)`, a bound and not a sign; `\deg E' = Φ_{E'}(0)+Φ_{E'}(1)` is evaluated off the critical line and is uncontrolled, so **(T1_cone) fails**; and `∫|w_F|` diverges, so **(T2_cone) fails** |
| **B3.** closed convex cone on the translates `\{λτ_cK\}` | no gain — it lies *inside* the nonnegative cone (`K > 0`, Theorem 11.7(i)), so `C'_{F_0} ≤ C_{F_0} < G` and Theorem 19.30 refutes it at once |
| **B5.** a completion in which the moment cone is closed | `REFUTED` for the closure — closure cannot raise a support function: `C'_X = C_X` for the closure in any topology making `I_∞(\cdot,X)` and `\deg` continuous |
| **B4.** classes with nonnegative Frobenius traces `t_n(E') ≥ 0` for all `n` | **passes the test of Theorem 19.30** — the whole witness family lies in B4, with `t_n(E) ≥ (d − 2tG)\sqrt{Φ_g(0)Φ_g(1)} > 0` since `2tG = 399.45 < 400`, whence `C'_{F_0}(\mathrm{B4}) ≥ G` with equality, which suffices |

B4 is the only survivor, and the only candidate that reads the Euler product.  Two caveats travel with
it, and §20 carries them: B4 contains `𝓝_∞` (every `N ∈ 𝓝_∞` has `t_n(N) = 0`), so (T1_cone) must be read
modulo `𝓝_∞`; and the inclusion of the nonnegative cone in B4 is unproved and probably false — the
available trace inequality gives only `t_n(E') ≥ −\mathrm{ARCH}(E')` — so B4 is a **different** cone,
not an enlargement, and replacing "nonnegative" by "trace-nonnegative" in (b′) is not a weakening.
The mechanism by which B4 passes is exactly that the trace bound reproduces the non-sharp constant
`\sqrt{ab}` against which the gate `R > 0` was calibrated in Corollary 19.9.

**Withdrawn in this section**

| claim | reason |
|---|---|
| *"(b′)⁺ is not refutable by anything currently known"*, and the fork *"(b′)⁺ is either equivalent to RH or strictly stronger"* | Theorem 19.23: the clause is false outright, unconditionally given (X19); the fork is closed negatively |
| *"the calibration of `χ = 0` is exact"* (the remark accompanying Corollary 19.9) | exact only against the non-sharp constant `\sqrt{ab}`; the sharp constant is `½s(γ,θ)\deg E'` with `s(γ,θ) < 1` (Lemma 19.17, Proposition 19.18) |
| *"(b′)⁺_{st} is the form to target"* (the remark accompanying Corollary 19.13) | Corollary 19.24: the stable form fails at the same witness, the multiple cancelling |
| the sentence *"row D reduces RH to the construction of an `h⁰` satisfying (a), (b′), (c)"* | Theorem 19.25: the hypothesis is unsatisfiable.  Theorem 12.3 keeps its label; only its use as a route is withdrawn |
| *"(★) is exactly the polar description of the closed convex cone generated by the nonnegative classes"* (completeness of the linear necessary conditions) | a polar/bipolar statement needs a locally convex topology on `D^W/𝓝_∞` in which the `I_∞(\cdot,X)` are continuous and exhaust the dual; §11 equips `D^W` with no topology.  Only the `≤` half — Theorem 11.14(ii) itself — is used, in Theorems 19.21, 19.23, 19.25 |
| the universal form *"every class of degree `> d_*` in `S_0` violates a necessary condition"* | false at `E = dK`, which is nonnegative at every degree (`K > 0`, Theorem 11.7(i)).  The correct statement is existential and ray-restricted: for every `d > d_*` there **exist** classes of degree `d` in `S_0` with no nonnegative representative — the witnesses of Theorem 19.23 |
| the optimality clause of Theorem 19.21, *"the supremum over all `E ∈ S_χ` of that degree is attained along `E_{t,d}`"* | its proof is a Cauchy–Schwarz equality case under RH; it is not load-bearing and is omitted.  Theorems 19.23 and 19.25 use only the `E_{t,d}` branch, and are unconditional |

---

## 19bis. The square as a tensor structure: the bidegree route and why it closes

*Provenance note.  The statements and proofs of this section are taken from
`03-research/phase-140-row-d-frobenius-square/R140_001_ROUND1.md` §§D.22, D.23, D.24
(rounds 1–2 applied in place) and `R140_003_ROUND2.md`; the labels of record, the open
item on a general number field carried in §14.5, and the withdrawals tabulated at the end are those
fixed in `R140_002_AUDIT.md`, `R140_004_CONFIRMATION.md` and
`R140_005_CLOSING_DECISION.md`.  The certified constants are produced by
`03-research/phase-140-row-d-frobenius-square/scripts/certify_chi.py`.*

Conventions are those of §11 throughout: `D^W` (Definition 11.1), `Φ_E(s) = ∫E(t)e^{(s−½)t}dt`,
`M(E) = (Φ_E(1),Φ_E(0)) =: (a,b)`, `\deg E = I_∞(E,2K) = a+b` (Theorems 11.8(i),(v), 11.13(i)),
`I_∞` (Definition 11.4, Lemma 11.4a), the canonical class `K` with `Φ_K = ξ` (Theorem 11.7), the
radical `𝓝_∞` (Theorem 11.11), `W(E) := Σ_ρΦ_E(ρ)Φ_E(1−ρ)` and the comparison identity (11.6),

    I_∞(E,E) = 2ab − W(E) ,      I_∞(E,K) = ½\deg E ,      M(K−E) = (½−a,\,½−b) .   (19bis.1)

`τ_c` is the modulus translation of (1.5), and `Z(E) := (Φ_E(ρ))_ρ` is the zero data of a class.
Clauses (a), (b′), (c) are those of Theorem 12.3.

The object of the section is the one route that Remark 14.5a and §14.5 item (18) single out: index
the candidate `h⁰` by the Frobenius **bidegree** rather than by a single Frobenius, and read the
square of the arithmetic surface as a tensor structure.  Three things are proved.  The Frobenius
family itself is constructed, ideal by ideal, over an arbitrary number field, with its
inverse-semigroup law, its bidegree and its integral shadow (§19bis.1); this settles the passage
from `Q` to a general number field for the Frobenius family of Paper 44.  What this section does
**not** do is close §14.5 item (18): it narrows it, by proving that the pair-indexed candidate the
item points to cannot be a function of the bidegree alone, and by naming what such a candidate must
read instead (Corollary 19bis.23); the item itself stays `OPEN`.  The bidegree route then
supplies, exactly and with the right constant, the quadratic growth that clause (c) demands and that
every earlier candidate failed (§19bis.3).  And it fails, for a reason internal to the bidegree:
**no nonzero `h⁰` that factors through `M` satisfies (b′)** (Theorem 19bis.19) — the negative that
makes §20 necessary, and whose witness is the class Proposition 19.7 calls *the bidegree witness*.

### 19bis.1 The Frobenius family over a number field, and its integral shadow

Throughout this subsection `K` is a number field of degree `d = r_1+2r_2`, `O_K` its ring of
integers, `S` a finite chart — a finite set of places containing all archimedean ones — and `S_f` its
finite part, indexed by prime ideals `𝔓 ⊂ O_K`.  Write `A_{K,S}^×` for the `S`-ideles,
`C_{S,K} := A_{K,S}^×/K^×` for the carrier, `|·|_S : C_{S,K} → R_{>0}` for the module (well defined on
classes by the product formula), `j_𝔓 : K_𝔓^× → C_{S,K}` for the slice map, `π_𝔓` for a uniformizer
and `N𝔓 := \#(O_K/𝔓)`.  **`K = Q` is nowhere assumed, and no class number, regulator, unit group or
Hecke character occurs anywhere in this subsection.**

**Definition 19bis.1 (the Frobenius family of `K`; the transport of Paper 44 Definitions 3ter.1–3ter.2).**
For `𝔓 ∈ S_f` and `k ≥ 1` put `O_𝔓^{(S)} := j_𝔓(O_𝔓^×)`, a compact subgroup of `C_{S,K}`, and

    Frob_{𝔓^k} := the normalized Haar probability measure of the coset j_𝔓(π_𝔓^kO_𝔓^×) . (19bis.2)

For finite `F ⊆ S_f` put `K_F := ∏_{𝔓∈F}O_𝔓^{(S)}` and let `Δ^{(F)}` be its normalized Haar measure,
`Δ^{(∅)} = δ_1 = Δ`.  For an integral ideal `𝔫 = ∏_𝔓𝔓^{k_𝔓}` put `P(𝔫) := \{𝔓 : k_𝔓 > 0\}` and

    Frob_𝔫 := ⋆_{𝔓|𝔫}Frob_{𝔓^{k_𝔓}} ,   Frob_{O_K} := Δ ,   Δ^{(𝔫)} := Δ^{(P(𝔫))} .  (19bis.3)

Equivalently, with the **integral idele** `ι(𝔫) := (1` at every archimedean place; `π_𝔓^{v_𝔓(𝔫)}` at
every `𝔓 ∈ S_f`) and `c_𝔫` its class, `Frob_𝔫` is the Haar measure of `c_𝔫K_{P(𝔫)}`.

The definition uses the **ideal** `𝔫`, not a generator.  No principality is asked for, because `ι` is
built from uniformizers place by place and is therefore defined on the whole ideal monoid.  This is
the single point at which a naive transport — "`Frob_α` for `α ∈ O_K`" — would have smuggled in the
class group; the avoidance is by construction, and it is the content of the subsection.

**Lemma 19bis.2 (the support and the module; `PROVED`).**  `\mathrm{supp}\,Frob_𝔫 = c_𝔫K_{P(𝔫)}`, and
`|x|_S = N𝔫^{−1}` for every `x` in that support; `Frob_𝔫` is a probability measure of compact support.

*Proof.*  The support statement is the definition.  For the module,
`|ι(𝔫)|_S = ∏_𝔓|π_𝔓|_𝔓^{v_𝔓(𝔫)} = ∏_𝔓N𝔓^{−v_𝔓(𝔫)} = N𝔫^{−1}`; and `|·|_S` is trivial on `K^×` (the
product formula, `CLASSICAL`) and on `K_{P(𝔫)}` (units have module `1`), so it is constant `= N𝔫^{−1}`
on the class and on the coset.  ∎  `PROVED`

*What replaces Paper 44 Lemma 3ter.3.*  Paper 44 computed a **representative** of `c_n` using the
canonical section of `Q_{>0}^× → Γ_S`.  For a general `K` there is no canonical section of the ideal
monoid into `A_{K,S}^×/K^×` when `h_K > 1`.  The proof above needs none: it uses only the value of
`|·|_S`, which is a class function.  This is the first place a literal transcription fails, and it is
repaired by proving less.

**Theorem 19bis.3 (the inverse-semigroup law over `K`; `PROVED`).**  For all integral ideals `𝔪,𝔫`,
with **no coprimality hypothesis**:

 (i) `Frob_𝔪 ⋆ Frob_𝔫 = Frob_{𝔪𝔫}`, an equality of measures, and `Frob_{O_K} = Δ = δ_1` is a true
     unit; so `𝔫 ↦ Frob_𝔫` is a strong monoidal realization of the ideal monoid `(I(O_K),·)`;
 (ii) `Frob_𝔫^† = μ_{c_𝔫^{−1}K_{P(𝔫)}}`, supported on `\{|x|_S = N𝔫\}`, and
      `Frob_𝔫 ⋆ Frob_𝔫^† = Δ^{(𝔫)}`, an idempotent, with `Δ^{(𝔫)} ≠ Δ` for `𝔫 ≠ O_K`;
 (iii) the bidegree is `M(Frob_𝔫) = (N𝔫^{1/2},\,N𝔫^{−1/2})` and `M(Δ^{(𝔫)}) = (1,1) = M(Δ)`; in
      particular the half-density normalization `λ_−λ_+ = 1` holds, and `M` is **multiplicative**,
      `M(Frob_𝔪⋆Frob_𝔫) = M(Frob_𝔪)M(Frob_𝔫)`;
 (iv) `𝔉_{S,K} := \{Frob_{𝔞,F} := μ_{c_𝔞K_F}\}`, with `𝔞` a fractional ideal and `P(𝔞) ⊆ F ⊂ S_f`
      finite, is a commutative **inverse semigroup** under `⋆`, with idempotent semilattice
      `(𝒫_{\mathrm{fin}}(S_f),∪)`, closed under `†`, containing every `Frob_𝔫` and `Frob_𝔫^†`; and
      `𝔞 ↦ Frob_𝔞⋆Frob_𝔟^†` does **not** descend to the group of fractional ideals.

*Proof.*  The proofs of Paper 44 Theorems 3ter.4, 3ter.6 and 3ter.7 apply verbatim, every step of
them using only the following.  (α) `C_{S,K}` is a locally compact abelian group.  (β) For compact
subgroups `H,H'` and classes `c,c'`, `μ_{cH}⋆μ_{c'H'} = μ_{cc'HH'}`: the image of `μ_H⊗μ_{H'}` under
multiplication is an `HH'`-invariant probability measure on `HH'`, hence its Haar measure by
uniqueness.  (γ) `K_FK_G = K_{F∪G}`.  (δ) `c_𝔪c_𝔫 = c_{𝔪𝔫}`, because `ι` is a monoid homomorphism on
ideals (`v_𝔓(𝔪𝔫) = v_𝔓(𝔪)+v_𝔓(𝔫)`) and the `j_𝔓` commute.  (ε) `P(𝔪𝔫) = P(𝔪)∪P(𝔫)`.  (ζ) For (iii),
`λ_∓(μ) = ∫|x|_S^{∓1/2}dμ` with `|x|_S ≡ N𝔫^{−1}` on the support (Lemma 19bis.2) and `μ` a probability
measure; `N` is multiplicative on ideals (`CLASSICAL`).  For (ii), `†` is push-forward along
inversion and `(c_𝔫K_P)^{−1} = c_𝔫^{−1}K_P`; `Δ^{(𝔫)} ≠ Δ` because `K_{P(𝔫)}` is an infinite compact
group, so its Haar measure has no atoms, while `Δ = δ_1` does.  For (iv), regularity `x⋆x^†⋆x = x` is
the same one-line coset computation, and the last clause is Paper 44's counterexample transported:
`𝔓_1` and `𝔓_1𝔓_2·𝔓_2^{−1}` give measures on cosets of `K_{\{𝔓_1\}}` and of `K_{\{𝔓_1,𝔓_2\}}`, sets
of different dimension.  ∎  `PROVED`

None of (i)–(iv) mentions `h_K`, `R_K`, `w_K`, the units, or a Hecke character; that is visible from
the proof, not asserted.

> **`OPEN` (injectivity).**  Paper 44 Theorem 3ter.4(iv) — `\mathrm{supp}\,Frob_n` determines `n` and
> `P(n)` — transports only in part.  Lemma 19bis.2 gives `N𝔫` and the support gives `P(𝔫)`, but
> `Frob_𝔪 = Frob_𝔫` forces only `P(𝔪) = P(𝔫) =: P` and `c_𝔪c_𝔫^{−1} ∈ K_P`, i.e. `𝔪𝔫^{−1} = (α)` for
> an `α ∈ K^×` that is a unit at every place outside `P`.  For `K = Q` this forces `𝔪 = 𝔫`; for
> general `K` the question is whether the ideal monoid injects into `C_{S,K}/K_P`, and it is not
> settled here.  It is used nowhere below, the realization of §19bis.2 factoring through `N𝔫` anyway.

**Definition 19bis.4 (the integral lattice and the shadow).**  Put

    L_S := ∏_{𝔓∈S_f}O_𝔓 ,     𝔫L_S := ∏_{𝔓∈S_f}𝔓^{v_𝔓(𝔫)}O_𝔓 ⊆ L_S ,

for an integral ideal `𝔫` with `P(𝔫) ⊆ S_f`; equivalently `𝔫L_S` is the image of `L_S` under
coordinatewise multiplication by the finite idele `ι(𝔫)_f = (π_𝔓^{v_𝔓(𝔫)})_{𝔓∈S_f}`.  This is the
literal transport of Paper 44 Definition 6bis.1, *"the integral lattice `L_S = ∏_{p∈S_f}Z_p ⊂ X_S`"*:
`L_S` is a topological ring, **not** a projective `O_K`-module, and it is a module over `O_K` through
the diagonal embedding, every statement below being about `L_S`-modules place by place.  Put

    Sh_{O_K}(Frob_𝔫) := \mathrm{Cone}\big(𝔫L_S \hookrightarrow L_S\big) ,          (19bis.4)

a two-term complex in degrees `−1,0`.  For `K = Q`, `S_f` a set of rational primes and `𝔫 = (n)` with
`P(n) ⊆ S_f`, one has `ι(n)_fL_S = nL_S` and (19bis.4) is exactly `[L_S \xrightarrow{\,n\,} L_S]`,
Paper 44's `Sh_Z(Frob_n)`.

*A ring of `S`-integers is the wrong object here, and the difference is not cosmetic.*  Definition
19bis.1 admits only ideals with `P(𝔫) ⊆ S_f`, and `O_{K,S}` is by definition the ring in which exactly
the primes of `S_f` are inverted; so `𝔫O_{K,S} = O_{K,S}` for every admissible `𝔫`, the inclusion is
the identity, the cone is acyclic and both `H^0` and `deg_{\det}` vanish.  Definition 19bis.4 is the
product of completions, and every clause below is local.

**Theorem 19bis.5 (the integral shadow; `PROVED`).**  For integral ideals `𝔪,𝔫` with
`P(𝔪),P(𝔫) ⊆ S_f`:

 (i) `H^{−1}Sh_{O_K}(Frob_𝔫) = 0` and

         H^0Sh_{O_K}(Frob_𝔫) = L_S/𝔫L_S ≅ ∏_{𝔓∈S_f}O_𝔓/𝔓^{v_𝔓(𝔫)} ≅ O_K/𝔫 ,

     a finite ring of order `N𝔫`, with no hedge: the factors at `𝔓 ∤ 𝔫` are trivial, the product is
     finite, and the last isomorphism is the Chinese Remainder Theorem together with
     `O_K/𝔓^k ≅ O_𝔓/𝔓^kO_𝔓` (`CLASSICAL`);
 (ii) there is an exact triangle
     `Sh(Frob_𝔪) → Sh(Frob_{𝔪𝔫}) → Sh(Frob_𝔫) \xrightarrow{+1}`, from `𝔪𝔫L_S ⊆ 𝔪L_S ⊆ L_S`;
 (iii) `deg_{\det}Sh_{O_K}(Frob_𝔫) = \log N𝔫`, hence additive:
     `deg_{\det}Sh(Frob_{𝔪𝔫}) = deg_{\det}Sh(Frob_𝔪) + deg_{\det}Sh(Frob_𝔫)`;
 (iv) `Sh_{O_K}` is **not** monoidal:
     `Sh(Frob_𝔪)⊗^L_{L_S}Sh(Frob_𝔫) \not≅ Sh(Frob_{𝔪𝔫})` whenever `𝔪 + 𝔫 ≠ O_K`, because the left
     side has `H^{−1} = \mathrm{Tor}_1^{L_S}(L_S/𝔪L_S,\,L_S/𝔫L_S) ≅ (𝔪L_S ∩ 𝔫L_S)/𝔪𝔫L_S ≠ 0` while
     the right side has `H^{−1} = 0` by (i);
 (v) the finite contact is `\mathrm{contact}_{\mathrm{fin}}(Frob_𝔫) = Λ_K(𝔫)N𝔫^{−1/2}`, where
     `Λ_K(𝔫) = \log N𝔓` if `𝔫 = 𝔓^k` and `0` otherwise, and
     `Σ_{𝔡|𝔫}Λ_K(𝔡) = \log N𝔫 = deg_{\det}Sh_{O_K}(Frob_𝔫)`.

*Proof.*  Everything is local, which is the point of Definition 19bis.4.  All four modules in play are
products over `𝔓 ∈ S_f` of their local factors, so it suffices to prove each clause at one place,
where `𝔓^kO_𝔓 = (π_𝔓^k)` is **principal**.

(i) At `𝔓`, multiplication by `π_𝔓^{v_𝔓(𝔫)}` is injective on the domain `O_𝔓`, so the cone is
quasi-isomorphic to the cokernel `O_𝔓/𝔓^{v_𝔓(𝔫)}` placed in degree `0`, and `H^{−1} = 0`.  The order
is `∏_𝔓N𝔓^{v_𝔓(𝔫)} = N𝔫` (`CLASSICAL`).

(ii) At `𝔓`, `π_𝔪π_𝔫O_𝔓 ⊆ π_𝔪O_𝔓` with quotient `π_𝔪O_𝔓/π_𝔪π_𝔫O_𝔓 ≅ O_𝔓/π_𝔫O_𝔓`, the isomorphism
being multiplication by `π_𝔪^{−1}`, legitimate because `π_𝔪` is a non-zero-divisor in the local ring;
no invertibility of a fractional ideal and no appeal to Dedekind theory is needed.  The octahedral
axiom applied to `𝔪𝔫L_S ⊆ 𝔪L_S ⊆ L_S` gives the triangle.

(iii) is (i) together with multiplicativity of `N`, or equivalently (ii) together with additivity of
`deg_{\det}` on triangles.

(iv) At a place `𝔓` dividing both `𝔪` and `𝔫`, the local
`\mathrm{Tor}_1(O_𝔓/π^a,\,O_𝔓/π^b) ≅ O_𝔓/π^{\min(a,b)} ≠ 0` for `a,b ≥ 1`; for `K = Q` and
`𝔪 = 𝔫 = (2)` this is Paper 44's witness.

(v) is Definition 19bis.1 together with the shell computation of Paper 44 Theorem 3ter.10:
`|x|_S ≡ N𝔫^{−1}` on the support, and the shell volume at `𝔓` is `\log N𝔓`.  ∎  `PROVED`

**Corollary 19bis.6 (field-uniformity; `PROVED`).**  The two arithmetic entries of the Weil ledger of
§18 that concern the Frobenius family — *`Frob_𝔪⋆Frob_𝔫 = Frob_{𝔪𝔫}`, the `†`-closure being a
commutative inverse semigroup* and
*`\mathrm{contact}_{\mathrm{fin}}(Frob_𝔫) = Λ_K(𝔫)N𝔫^{−1/2}`, `deg_{\det}Sh(Frob_𝔫) = \log N𝔫`* — hold
for **every number field**, with `n ↦ N𝔫` and `Λ ↦ Λ_K`.  The passage from `Q` to a general number
field for the Frobenius family of Paper 44 is therefore made in full.  ∎  `PROVED`

*Proof.*  Theorems 19bis.3 and 19bis.5.  ∎

### 19bis.2 The Pólya realization, and the three Gram forms

`Frob_𝔫` is **not** an element of `D^W`: the point classes are multipliers, and `I_A(Frob_n,Frob_n)`
does not exist (Paper 44 Remark 3bis.4b, Theorem 3ter.14, Remark 8bis.1c).  What exists is the
**action**: `Frob_n` acts on radial classes by the modulus translation `τ_{\log n}` (Theorem 11.8(iii),
Theorem 14.3(ii), Proposition 14.2).  A correspondence is realized on a surface by applying it to the
diagonal, and that is what the following definition does — as **one choice among many**, made here.

**Definition 19bis.7 (the Pólya realization `r`, and the Pólya representative of the diagonal).**  Fix
`a_0 > 0` and put

    Δ^W := 2K ,   r(Frob_n) := τ_{\log n}Δ^W = 2\,τ_{\log n}K ,
    F_1 := K + K_{\mathrm{odd}} ,   F_2 := K − K_{\mathrm{odd}} ,                   (19bis.5)

with `K` the canonical class of Theorem 11.7 and `K_{\mathrm{odd}}` the odd companion of §17,
`Φ_{K_{\mathrm{odd}}}(s) = \frac{\sinh((s−½)a_0)}{\sinh(a_0/2)}ξ(s)`.  Extend `r` `R`-linearly to the
`R`-span `Div_□ ⊗ R` of the symbols `Frob_n` and their formal combinations.

Three cautions travel with the definition, and each is a statement of record.

* `F_1` and `F_2` are **not** the rulings `e_∓` of Paper 43 §9.  Proposition 14.1(iv) states, and
  Paper 43 Theorem 9.14c proves, that `e_± ∉ D^W`.  What exists in `D^W` are *lifts of the ruling
  data* `M = (1,0)` and `(0,1)`, namely `F_1,F_2` above; they depend on `a_0` and are canonical only
  modulo `𝓝_∞`.  For `a_0 ≠ a_0'` the two `K_{\mathrm{odd}}` have the same `M = (½,−½)` and the same
  (vanishing) zero data, hence differ **exactly** by an element of `𝓝_∞` (Theorem 11.11); so `F_1,F_2`
  are well defined in `D^W/𝓝_∞`, and every statement about them below is made there or is
  `a_0`-independent by inspection.
* The substitution `Δ ↦ 2K` is a **choice of representative**, justified by two matching facts and by
  nothing else: `M(2K) = (1,1) = M(Δ)` (Theorem 11.7(iii) and Paper 44 Theorem 3ter.6(iii)); and
  `I_∞(E,2K) = \deg E` for every `E` (Theorem 11.8(v)), which is Weil's `Δ·D = d_1+d_2` for a class of
  bidegree `(d_1,d_2)`.  Every intersection number in Theorem 19bis.8 is a number attached to `2K` and
  its translates, and **none of them is asserted to be a regularized value of `δ_1⋆δ_1`** — which is
  `−∞` at a fixed finite chart (Paper 44 Theorem 8bis.2).
* `r` **deletes the arithmetic weights** `Λ_K(𝔫)N𝔫^{−½}` that Theorem 19bis.5(v) attaches to
  `Frob_𝔫`, remembering only `N𝔫`.  Everything proved about `r` therefore says something about `r`,
  and nothing about the Frobenius family; §19bis.2's last theorem says what the family's own form
  does instead.

**Theorem 19bis.8 (the realization and its full intersection matrix; `PROVED`).**

 (i) `F_1,F_2,K,K_{\mathrm{odd}},τ_cK ∈ D^W` for every `c ∈ R`, and `M(F_1) = (1,0)`,
     `M(F_2) = (0,1)`, `M(K) = (½,½)`, `M(K_{\mathrm{odd}}) = (½,−½)`, `M(Δ^W) = (1,1)`,
     `M(r(Frob_n)) = (n^{1/2},n^{−1/2})`.  In particular `K = ½(F_1+F_2)` and
     `Λ = \mathrm{span}(K,K_{\mathrm{odd}}) = \mathrm{span}(F_1,F_2)`.
 (ii) `Φ_{r(D)}` vanishes at **every zero of `ξ`**, for every `D ∈ Div_□ ⊗ R`; hence

          W(r(D)) = 0   for every  D ∈ Div_□ ⊗ R ,                                (19bis.6)

     and therefore, writing `\mathrm{bideg}\,r(D) =: (d_1,d_2)`,

          I_∞\big(r(D),r(D)\big) = 2\,d_1d_2   \text{ exactly.}                   (19bis.7)
 (iii) The intersection matrix on `\{F_1,F_2,Δ^W,r(Frob_n),K\}` is, in full:

    | `I_∞` | `F_1` | `F_2` | `Δ^W` | `r(Frob_m)` | `K` |
    |---|---|---|---|---|---|
    | `F_1` | `0` | `1` | `1` | `m^{−1/2}` | `½` |
    | `F_2` | `1` | `0` | `1` | `m^{1/2}` | `½` |
    | `Δ^W` | `1` | `1` | `2` | `m^{1/2}+m^{−1/2}` | `1` |
    | `r(Frob_n)` | `n^{−1/2}` | `n^{1/2}` | `n^{1/2}+n^{−1/2}` | `(n/m)^{1/2}+(m/n)^{1/2}` | `½(n^{1/2}+n^{−1/2})` |
    | `K` | `½` | `½` | `1` | `½(m^{1/2}+m^{−1/2})` | `½` |

     in particular `I_∞(K,K) = ½`, `Δ^W·Δ^W = 2`, and `r(Frob_n)·r(Frob_n) = 2` for every `n`.
 (iv) Modulo the radical,

          r(Frob_n) ≡ n^{1/2}F_1 + n^{−1/2}F_2 \pmod{𝓝_∞} ,                        (19bis.8)

     and `Δ^W ≡ F_1+F_2 \pmod{𝓝_∞}`; consequently `r(Div_□⊗R) ⊆ Λ + 𝓝_∞` and
     `r(Div_□⊗R)/𝓝_∞ = Λ`, a plane.
 (v) `I_∞` on `r(Div_□⊗R)/𝓝_∞ = Λ` is the hyperbolic plane
     `\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}` in the basis `(F_1,F_2)`, of signature `(1,1)`.

*Proof.*  (i) Membership is Theorem 11.7(ii) and Lemma 11.2(i) (`D^W` is a vector space, closed under
`τ_c`).  `M(K) = (ξ(1),ξ(0)) = (½,½)` is Theorem 11.7(iii), and `M(K_{\mathrm{odd}}) = (½,−½)` is the
definition of the odd companion; hence `M(F_1) = M(K)+M(K_{\mathrm{odd}}) = (1,0)`, `M(F_2) = (0,1)`
and `F_1+F_2 = 2K`, so `K = ½(F_1+F_2)`.  By Theorem 11.8(iii),
`M(τ_cK) = (e^{c/2}ξ(1),\,e^{−c/2}ξ(0)) = ½(e^{c/2},e^{−c/2})`, so
`M(r(Frob_n)) = M(2τ_{\log n}K) = (n^{1/2},n^{−1/2})`, matching Paper 44 Theorem 3ter.6(iii) on the
nose — which is the reason for the factor `2` in (19bis.5).  The two spans agree because the change of
basis is invertible.

(ii) Every generator of `r(Div_□⊗R)` is a real multiple of some `τ_cK`, and
`Φ_{τ_cK}(s) = e^{(s−½)c}ξ(s)` (Lemma 11.2(iv)), which vanishes at every zero of `ξ`.  `Φ` is linear
in the class, so `Φ_{r(D)}(ρ) = 0` for every zero `ρ` and every `D`.  Then (11.6) gives
`I_∞(E,E) = 2Φ_E(0)Φ_E(1) − W(E) = 2d_1d_2 − 0`.

(iii) Each entry is (11.6) with vanishing zero sum, i.e.
`I_∞(E,E') = Φ_E(0)Φ_{E'}(1) + Φ_E(1)Φ_{E'}(0)`, evaluated on the `M`-values of (i).  For instance
`I_∞(r(Frob_n),r(Frob_m)) = n^{−1/2}m^{1/2} + n^{1/2}m^{−1/2}`, which is `2` at `m = n`, and
`I_∞(Δ^W,Δ^W) = 1·1+1·1 = 2`.  The `K`-column also follows from `I_∞(E,K) = ½\deg E`
(Theorem 11.8(i)).

(iv) Both sides of (19bis.8) lie in `D^W`, have the same `M` by (i), and have `Φ` vanishing at every
zero by (ii); by Theorem 11.11, `𝓝_∞` is exactly `\{Φ(0) = Φ(1) = 0,\ Φ(ρ) = 0\ ∀ρ\}`, so the
difference lies in `𝓝_∞`.  Explicitly the difference has

    Φ(s) = ξ(s)\Big[2n^{s−½} − (n^{1/2}+n^{−1/2}) − (n^{1/2}−n^{−1/2})\tfrac{\sinh((s−½)a_0)}{\sinh(a_0/2)}\Big] ,

whose bracket vanishes at `s = 0` and `s = 1` by direct substitution, and `ξ(ρ) = 0` at the zeros.

(v) is (iii) restricted to `(F_1,F_2)`, together with Theorem 11.11.  ∎  `PROVED`

**Theorem 19bis.9 (Castelnuovo with equality on the realization, and its emptiness; `PROVED`).**  For
every `D ∈ Div_□ ⊗ R` of bidegree `(d_1,d_2)`, `I_∞(r(D),r(D)) = 2d_1d_2`.  So the Castelnuovo–Severi
inequality `D·D ≤ 2d_1d_2` holds on `r(Div_□⊗R)` **with equality, always**.  Equivalently: the
Hodge-index inequality is true on `r(Div_□⊗R)` unconditionally, and it is **non-detecting**, because
`r(Div_□⊗R)` meets the primitive sector `P^W` only in `𝓝_∞`.

*Proof.*  (19bis.7) is the equality.  For the second sentence, `r(D) ≡ d_1F_1 + d_2F_2 \pmod{𝓝_∞}` by
Theorem 19bis.8(iv) and linearity, so the primitive part of `r(D)` in the splitting `D^W = Λ ⊥ P^W`
of §17 lies in `P^W ∩ (Λ+𝓝_∞) = 𝓝_∞`, on which `I_∞` vanishes identically.  The unconditional Hodge
index on `Λ`, and its non-detection, are the corresponding statements of §17 for the translate cone
`Λ_ξ^+ = \{Σ_jc_jτ_{u_j}K\}`, of which `r(Div_□⊗R)` is a subcone by construction.  ∎  `PROVED`

**Corollary 19bis.10 (the lattice the realization produces; `PROVED`).**  Modulo `𝓝_∞`, `Div_□ ⊗ R`
is carried by `r` onto a lattice of rank `2` with basis `F_1,F_2`, Gram
`\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}`, `Δ^W = F_1+F_2`, `Δ^W·Δ^W = 2` and
`K = ½(F_1+F_2)`.  As a **lattice with its form**, together with the dependence `Δ = F_1+F_2` and the
value `Δ² = 2`, this is that of `NS(P¹×P¹)`, scaled.  Two qualifications are part of the statement.
(1) The **canonical class does not match**: on `P¹×P¹` one has `K_S = −2(f_1+f_2)`, whereas here
`K = +½(F_1+F_2)`.  (2) Reading `Δ^W·Δ^W = 2 = 2−2g` as "`g = 0`" applies the **curve** genus formula
to the diagonal of a **surface**; Finding 13.8 records exactly this as an open reconciliation and
refuses to make it, and the reading is carried here under that refusal.  In particular `Δ^W` is *not*
independent of `F_1,F_2`: the rank-`3` configuration
`\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}` of signature `(1,2)` has no analogue here,
and the determinant of the corresponding Gram matrix
`\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&2\end{psmallmatrix}` is `0`.

*Proof.*  Theorem 19bis.8(iii),(iv),(v); and
`\det\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&2\end{psmallmatrix} = 0(0·2−1) − 1(1·2−1) + 1(1−0) = −1+1 = 0`.
The facts about `P¹×P¹` (`Δ = f_1+f_2`, `Δ² = 2`, `g = 0`) are `CLASSICAL`.  ∎  `PROVED`

> **What this says, and what it does not.**  The collapse is a property of the **realization `r`**, not
> of the Frobenius family.  `r` factors through the bidegree, lands in the translate cone of §17, and
> therefore detects nothing — which is expected, not informative, once one observes that `r` remembers
> only `N𝔫` and deletes the arithmetic weights `Λ_K(𝔫)N𝔫^{−½}`.  The statement *"the Euler-product
> structure of the Frobenius family realizes entirely inside the ruling plane"* is **`REFUTED`** and
> appears only in the withdrawn table below.  The Frobenius family has a different Gram form, and it
> behaves in the opposite way.

**Definition 19bis.11 (Paper 44's Frobenius Gram matrix; `PROVED-IN-REPOSITORY`).**  At a finite chart
`S`, with smeared Frobenii `Frob_n^{\mathrm{sm}}` of unit-height archimedean profiles and level `N`,
and `ε < ε_0(A,S)` (the hypothesis of Paper 44 Theorem 8bis.1), the Gram matrix of the family is, for
`m ≠ n`,

    G^{Frob}_{mn} = c_N(m,n)·W_{\mathrm{fin}}\big(\{\log m − \log n\}\big)·(h_m⋆h_n^†)(n/m) ,
    W_{\mathrm{fin}}\big(\{\log m − \log n\}\big) =
      \begin{cases}(\log q)\,q^{−k/2}, & m/n = q^{\pm k},\ q\ \text{prime},\ k ≥ 1,\\
                   0, & \text{otherwise,}\end{cases}                              (19bis.9)

with `c_N(m,n) = ∏_{s ∈ S_f∖(P(m)∩P(n))}\mathrm{vol}(1+s^NZ_s)` — the complement of the
**intersection**, by Paper 44's correction K1, not of the union.  The **diagonal does not exist**:
`I_A(Frob_n,Frob_n)` is undefined (Paper 44 Remark 8bis.1c), and its regularizations diverge in both
conventions with no convention-free rate.  Writing `q^{−k/2} = (\min(m,n)/\max(m,n))^{1/2}`, (19bis.9)
reads: `G^{Frob}_{mn}` is nonzero **exactly when `m/n` is a power of a single prime**, with value
`Λ(\max/\min)·(\min/\max)^{1/2}·c_N(m,n)`.

**Theorem 19bis.12 (the three Gram forms of the Frobenius family, and what each sees; `PROVED` for
(C), `PROVED-IN-REPOSITORY` for (A) and (B)).**

| | object | Gram form | reads the factorization? | reads the zeros? | sign |
|---|---|---|---|---|---|
| **(A)** | the **pure** Frobenius family `\{Frob_n^{\mathrm{sm}}\}` | `W_{\mathrm{fin}}` only, **no archimedean block** (Paper 44 Cor. 8bis.1d); entries (19bis.9) | **yes** — `G^{Frob}_{mn} = 0` unless `m/n` is a prime power, weights `Λ(q^k)q^{−k/2}` | only the finite half of the kernel | **unsigned, and proved so**: `Q_{\mathrm{fin}} > 0` on an explicit **primitive** class, at every finite chart, unconditionally — Paper 44 **Theorem 8bis.4a** |
| **(B)** | the **unit-averaged** family `Γ_n^{\mathrm{rad}} = Frob_n⋆Δ^{\mathrm{rad}}` | the **full Weil kernel** `W_{\mathrm{fin}}+ω_∞`, exactly and at every level — Paper 44 **Theorem 8bis.1e** | **no** — averaging forgets the factorization | **yes**: its sign on primitive radial classes is equivalent to RH, in the colimit (Paper 44 Thm 8bis.4(iii)) | **equivalent to RH** (a colimit statement; at a fixed chart both forms are indefinite, Paper 43 Thm 14.1) |
| **(C)** | the **Pólya realization** `r(Frob_n) = τ_{\log n}(2K) ∈ D^W` (Definition 19bis.7) | `I_∞(r(Frob_n),r(Frob_m)) = (n/m)^{1/2}+(m/n)^{1/2}` | **no** — depends on `m/n` as a real number only | **no** — `Φ` vanishes at every zero by construction | **identically `= 2d_1d_2`**: Castelnuovo with equality, non-detecting (Theorem 19bis.9) |

Moreover:

 (i) **(C) has rank `2`.**  As a matrix indexed by `n,m ≥ 1`,
     `I_∞(r(Frob_n),r(Frob_m)) = u_nv_m + v_nu_m` with `u_n := n^{1/2}`, `v_n := n^{−1/2}`; it is the
     symmetric outer product `u⊗v + v⊗u`, of rank `≤ 2`, of signature `(1,1)` on every finite index
     set on which `u` and `v` are independent — which they are as soon as two distinct `n` occur.
 (ii) **(A) has infinite rank and is sparse.**  `G^{Frob}` is supported on the prime-power ratio
     relation `m/n ∈ \{q^{\pm k}\}`, a sparse graph on `N_{≥2}`, with weights that are exactly the
     finite contacts `\mathrm{contact}_{\mathrm{fin}}(Frob_{q^k}) = Λ(q^k)q^{−k/2}` of Theorem
     19bis.5(v).  **These weights are the arithmetic, and `r` deletes them.**  One distinction must be
     kept, since the two objects are easily conflated: Paper 44's `Q_{\mathrm{fin}}`, whose
     indefiniteness Theorem 8bis.4a establishes, is a **quadratic form on radial profiles**, whereas
     `G^{Frob}` is the **discrete Gram matrix of the family `\{Frob_n^{\mathrm{sm}}\}`**, which has no
     diagonal at all; the indefiniteness of the first is the sign entry of the (A) row, and it is not
     a statement about the diagonal of the second.
 (iii) **(A) and (B) are complementary slices of one projector.**  They are the two halves of Paper 44
     Theorem 8bis.1′: convolving with `Δ^{\mathrm{rad}}` converts the finite half of the Weil kernel
     into the whole of it, at the cost of forgetting the factorization.  **No object carries both.**
 (iv) **(C) is a third object, and it carries neither.**  It is not a slice of that projector; it is a
     class of `D^W` whose bidegree happens to agree with `M(Frob_n)`.  Its degeneracy is a fact about
     (C) and says nothing about (A) or (B).

*Proof.*  The (A) row is Paper 44 Corollary 8bis.1d, Theorem 8bis.1 with correction K1, Remark
8bis.1c and Theorem 8bis.4a.  The (B) row is Paper 44 Theorem 8bis.1e and Theorem 8bis.4(iii), with
the colimit quantifier (C1) carried.  The (C) row is Theorem 19bis.8(iii) and Theorem 19bis.9.  For
(i), the displayed factorization is immediate from the table of Theorem 19bis.8(iii).  For (ii), the
support and the weights are (19bis.9), and the identification of the weights with the finite contacts
is Theorem 19bis.5(v); the distinction between `Q_{\mathrm{fin}}` and `G^{Frob}` is Definition
19bis.11 together with Paper 44 Remark 8bis.1c.  (iii) and (iv) are as shown.  ∎  `PROVED`

> **The consequence for the route.**  The pure Frobenius Gram form is **not** non-detecting: Paper 44
> Theorem 8bis.4a proves, unconditionally and at every finite chart, that positivity **fails** on it,
> exhibiting a primitive class with `Q_{\mathrm{fin}} > 0`.  What is non-detecting is the Pólya
> realization.  So: the Euler product's own Gram form (A) is arithmetic, sparse and unsigned; the form
> whose sign is RH is (B), which has forgotten the Euler product; and the tensor-square candidate of
> §19bis.3 reads neither, because it reads only bidegrees.  Paper 44 Remark 8bis.4b(3)'s warning is
> carried: Theorem 8bis.4a decides the *left-hand side* of a biconditional at a chart, and decides
> nothing about RH.

### 19bis.2bis Where the Weil shape lives: the translate orbit of one class

The collapse of §19bis.2 is diagnosed exactly by the equality `r(Frob_n) = τ_{\log n}(2K)`, since
`2K` has **zero zero-data**.  Replace the diagonal representative by a class with nonvanishing zero
data and the Weil shape returns — as an equivalent of RH, and as nothing weaker.

**Restatement 19bis.13 (Castelnuovo on a translate orbit, Bochner positivity, and RH;
`RESTATEMENT`).**  For real `E_0 ∈ D^W` put `A_ρ := Φ_{E_0}(ρ)Φ_{E_0}(1−ρ)` and define the
**translate kernel**

    κ_{E_0}(c) := W(E_0,\,τ_cE_0) = Σ_ρ e^{(ρ−½)c}A_ρ ,   c ∈ R ,                  (19bis.10)

absolutely convergent by (11.2) and (E3d), with `κ_{E_0}(0) = W(E_0)`.  Then:

 (i) `W(τ_uE_0,\,τ_vE_0) = κ_{E_0}(u−v)`: the Gram form of the orbit `\{τ_cE_0\}` is a **Toeplitz**
     kernel, and for `D = Σ_ja_jτ_{c_j}E_0` (a finite real combination),
     `W(D) = Σ_{j,l}a_ja_l\,κ_{E_0}(c_j−c_l)`;
 (ii) consequently **Castelnuovo, `I_∞(D,D) ≤ 2\,\mathrm{bideg}_1(D)\mathrm{bideg}_2(D)`, holds on
     every finite span of translates of `E_0` if and only if `κ_{E_0}` is positive-definite in
     Bochner's sense on `R`** — that is, iff `κ_{E_0}` is the Fourier transform of a positive measure;
 (iii) *(sufficiency, unconditional)* if `A_ρ = 0` for every zero `ρ` off the line `\mathrm{Re}\,s = ½`,
     then `κ_{E_0}(c) = Σ_γ e^{iγc}|Φ_{E_0}(½+iγ)|²` is positive-definite, and
     `|κ_{E_0}(c)| ≤ κ_{E_0}(0) = W(E_0)` for every `c`;
 (iv) *(necessity, when finitely many real parts occur)* suppose only finitely many distinct values
     `β` occur as `\mathrm{Re}\,ρ` among the zeros with `A_ρ ≠ 0`.  If `κ_{E_0}` is positive-definite,
     then `A_ρ = 0` for every `ρ` with `\mathrm{Re}\,ρ ≠ ½`.

So the Castelnuovo condition, imposed over the whole orbit, is **RH for the zeros that `E_0` sees**.
It proves no sign, and it is not a weaker intermediate step toward one.

*Proof.*  (i) Termwise,
`W(τ_uE_0,τ_vE_0) = Σ_ρ e^{(ρ−½)u}Φ_{E_0}(ρ)\,e^{(½−ρ)v}Φ_{E_0}(1−ρ) = Σ_ρ e^{(ρ−½)(u−v)}A_ρ
= κ_{E_0}(u−v)`, so no rearrangement question arises; the bilinear expansion follows by linearity of
`Φ`.

(ii) By (11.6), Castelnuovo at `D` is exactly `W(D) ≥ 0`; and `W(D) ≥ 0` for all finite real
combinations of translates is, by (i), the definition of positive-definiteness of `κ_{E_0}`.
Bochner's theorem (`CLASSICAL`) then identifies such kernels with Fourier transforms of positive
measures.

(iii) Under the hypothesis every contributing zero is `ρ = ½+iγ`, so `1−ρ = \barρ`; `E_0` being real,
`Φ_{E_0}(1−ρ) = \overline{Φ_{E_0}(ρ)}`, hence `A_ρ = |Φ_{E_0}(½+iγ)|² ≥ 0` and `κ_{E_0}` is the
Fourier transform of the positive discrete measure `Σ_γ|Φ_{E_0}(½+iγ)|²δ_γ`.  The bound is
`|κ| ≤ κ(0)`.

(iv) A positive-definite function is **bounded**, `|κ_{E_0}(c)| ≤ κ_{E_0}(0)` for all `c`
(`CLASSICAL`).  Write `κ_{E_0}(c) = Σ_j e^{(β_j−½)c}f_j(c)` with `β_1 > β_2 > \dots > β_k` and
`f_j(c) = Σ_{\mathrm{Re}\,ρ = β_j}A_ρe^{iγ_ρc}`, each `f_j` absolutely convergent and hence Bohr
almost periodic.  Suppose `β_1 > ½` and `f_1 ≢ 0`.  Dividing by `e^{(β_1−½)c}` and letting
`c → +∞`, the terms with `j ≥ 2` tend to `0` uniformly, so
`\limsup_{c→+∞}|f_1(c)| ≤ \limsup_{c→+∞}e^{−(β_1−½)c}κ_{E_0}(0) = 0`; but a nonzero Bohr almost
periodic function satisfies `\sup_{c ≥ T}|f_1| = \sup_R|f_1| > 0` for every `T` (`CLASSICAL`, Bohr),
a contradiction.  So `f_1 ≡ 0`, whence `A_ρ = 0` for every `ρ` with `\mathrm{Re}\,ρ = β_1`, by
uniqueness of the coefficients of an absolutely convergent almost periodic series (`CLASSICAL`,
Bohr).  Induct downward on `j` until `β_j ≤ ½`, and argue symmetrically for `β < ½` using `c → −∞`.
∎  `RESTATEMENT`

The general necessity, when infinitely many real parts accumulate, is **not** claimed.  For
`E_0 = 2K` — the class the realization `r` uses — one has `A_ρ ≡ 0`, `κ_{E_0} ≡ 0` and the criterion
degenerates to `0 ≥ 0`; this is the exact sense in which the realization is genus zero and carries no
information.

### 19bis.3 The tensor square: the growth clause is met

**Definition 19bis.14 (a curve Riemann–Roch function, and the tensor square).**  A **curve
Riemann–Roch function** is `h_c : R → R_{≥0}` with `h_c(x) = 0` for `x ≤ −c''` and `h_c(x) ≥ λx − c'`
for constants `λ > 0`, `c',c'' ≥ 0`.  The **trivial** such function is `h_c(x) := \max(x,0) =: x^+`,
with `λ = 1`, `c' = c'' = 0`.  Given `h_c`, the **tensor square** candidate is

    h⁰_□(E) := h_c(a)·h_c(b) ,   (a,b) = M(E) .                                   (19bis.11)

`h⁰_□` **factors through the bidegree map `M`**.  That single fact drives everything that follows.
Clause (a) is immediate, since `h_c ≥ 0`.

**Theorem 19bis.15 (the growth clause is met, with the exact constant, over every number field;
`PROVED`).**  Let `h_c(x) = x^+` and let `K` be any number field, `r := \mathrm{Res}_{s=1}Λ_K =
2^{r_1}h_KR_K/w_K > 0`, so that `M(K_K) = (r/2,r/2)` and hence, for `m ≥ 0`,

    h⁰_□(mK_K) = h_c(mr/2)² = \tfrac{r²}{4}m² ,

which is **exactly** the growth that clause (c) forces, `h⁰(mK_K) ≥ (r²/4)m² + O(m)`; for `K = Q`,
`r = 1`, this is `¼m²`.

*Proof.*  `M(mK_K) = (mr/2,\,mr/2)` by linearity of `M` and the value `M(K_K) = (r/2,r/2)` of §18, and
`h_c(x) = x` for `x ≥ 0`.  The required constant is the growth demand of clause (c) read at `E = mK_K`:
by (19bis.1), `½I_∞(mK_K,mK_K) − ½I_∞(mK_K,K_K) + χ = (r²/4)m² + O(m)`, and by Theorem 19.2 (Serre
symmetry) clause (c) at `mK_K` requires `h⁰(mK_K) + h⁰(K_K−mK_K)` to dominate it, the second term
vanishing for `m > 1` since `M(K_K − mK_K) = ((1−m)r/2,(1−m)r/2)` has negative entries.  ∎  `PROVED`

> **What the tensor structure buys.**  The single number that defeated every earlier candidate —
> `O_Q(\log m)` in Theorem 13.6, and `(\log m)^{3/2}` for the lattice count of §18, against a required
> `m²` — is supplied here on the nose, with the right constant, uniformly in the number field, by the
> product of two linear counts.  The growth obstruction is cleared.  What follows is that the two
> remaining clauses are not.

**Theorem 19bis.16 (the optimal constant in clause (c); `PROVED`).**  Let `h_c = (·)^+` and let
`c > 0` be the common value `Φ_K(0) = Φ_K(1)` (so `c = ½` for `ξ`, `c = r/2` for `ξ_K`, and `c = ¼` for
the falsifier `Ξ_Q`).  Put

    g(a,b) := h_c(a)h_c(b) + h_c(c−a)h_c(c−b) − ab + \tfrac{c}{2}(a+b) ,          (19bis.12)

so that, by (19bis.1), clause (c) for `h⁰_□` reads `W(E) ≥ 2χ − 2g(M(E))` for every `E ∈ D^W`.  Then

    \inf_{(a,b)∈R²} g(a,b) = \frac{c²}{2} ,

attained exactly at `(a,b) = (c,0)` and `(0,c)`, i.e. at `E = ½F_1` and `E = ½F_2` when `c = ½`.  In
particular:

 (i) for `ξ`: `\inf g = 1/8`, so `χ ≤ 1/8`, and `χ = 1/8` is admissible; for `ξ_K` the corresponding
     value is `r²/8`;
 (ii) the multiples of `K` give only the weaker bound `χ ≤ 3/16`, attained at `E = ½K`: on
     `a = b = u`, `g(u,u) = u² − \tfrac u2 + ¼`, so `g(u,u) − ⅛ = (u−¼)² + 1/16 ≥ 1/16 > 0`, and the
     ruling witness `½F_1` is strictly sharper than every multiple of `K`;
 (iii) the obstruction is **a ceiling on `χ`, not a lower bound on `W(E)`**: at every `E` with
     `W(E) = 0` the inequality reads `0 ≥ 2χ − 2g`, which holds for all such `E` **iff**
     `χ ≤ \inf g = c²/2`.

*Proof.*  By homogeneity `g_c(a,b) = c²g_1(a/c,b/c)`, so it suffices to take `c = 1` and show
`\inf g_1 = ½`, attained at `(1,0)` and `(0,1)`.  Write `x^+ := \max(x,0)`, and note `g_1` is
symmetric in `a,b`.  Split `R²` into regions.

*Region `0 ≤ a,b ≤ 1`.*  `g_1 = ab + (1−a)(1−b) − ab + ½(a+b) = 1 − ½(a+b) + ab`.  Its derivative in
`a` is `b − ½`; so for fixed `b < ½` it decreases in `a`, with minimum at `a = 1` of value
`1 − ½ − ½b + b = ½ + ½b ≥ ½`; for `b > ½` it increases in `a`, with minimum at `a = 0` of value
`1 − ½b ≥ ½`; and at `b = ½` it is constant in `a`, equal to `1 − ½(a+½) + ½a = ¾ > ½`.  Hence the
infimum on this square is `½`, attained at `(1,0)` and `(0,1)`; for comparison `g_1(0,0) = 1` and
`g_1(1,1) = 1`.

*Region `a > 1`, `0 ≤ b ≤ 1`.*  `(1−a)^+ = 0`, so `g_1 = ab − ab + ½(a+b) = ½(a+b) > ½`.

*Region `a > 1`, `b < 0`.*  `a^+b^+ = 0` and `(1−a)^+ = 0`, so `g_1 = −ab + ½(a+b)`; writing
`b = −β` with `β > 0`, this is `aβ + ½a − ½β = β(a−½) + ½a > ½` for `a > 1`.

*Region `a > 1`, `b > 1`.*  `g_1 = ab − ab + ½(a+b) > 1`.

*Region `a < 0`, `b ≤ 1`.*  `a^+ = 0` while `1−a > 0` and `(1−b) ≥ 0`, so
`g_1 = (1−a)(1−b) − ab + ½(a+b) = 1 − (a+b) + ab − ab + ½(a+b) = 1 − ½(a+b) ≥ ½`, with equality only
in the limit `a → 0^-`, `b → 1`, i.e. at the closure point `(0,1)` already counted.

*Region `a < 0`, `b > 1`.*  `(1−b)^+ = 0`, so `g_1 = −ab + ½(a+b) = |a|b + ½(a+b)`; as `a → 0^-` this
tends to `b/2 > ½`, and it increases in `|a|` since `∂/∂|a| = b − ½ > 0`.

*Region `a < 0`, `b < 0`.*  `g_1 = (1−a)(1−b) − ab + ½(a+b) = 1 − ½(a+b) > 1`.

The regions cover `R²` up to the symmetry `a ↔ b`.  So `\inf g_1 = ½`, attained at `(1,0)` and
`(0,1)`; undoing the scaling gives `c²/2` at `(c,0)` and `(0,c)`.

For (ii), take `c = ½` and `E = 2uK` with `a = b = u`: substituting into (19bis.12),
`g(u,u) = u² + (½−u)² − u² + ¼(2u) = (½−u)² + \tfrac u2 = u² − \tfrac u2 + ¼`, whose minimum over `R`
is at `u = ¼`, of value `1/16 − 1/8 + 1/4 = 3/16`.  Since `3/16 > 1/8`, the `K`-line is not the
binding constraint; at `u = ¼` and `χ = ¼` clause (c) reads `1/8 ≥ 3/16`, false by `1/16`.  (iii) is
the displayed reformulation of clause (c).  ∎  `PROVED`

*Certified constants.*  `scripts/certify_chi.py` of
`03-research/phase-140-row-d-frobenius-square` evaluates `g` on a `401×401` grid over `[−6,6]²`,
returning the grid minimum `0.1275` — a margin of `+2.5·10^{−3}` above the proved value `0.125` — and
the exact values `g(½,0) = g(0,½) = 0.125`; on a `4001×4001` grid the margin is `+2.5·10^{−4}`.  The
sweep uses no Lipschitz or interval bound and is therefore a consistency check, not a lower-bound
certificate; the value `c²/2` is proved above and nothing depends on the script.

**Theorem 19bis.17 (clause (c) for a bidegree-function; `PROVED`).**

 (i) *(Necessity, fully general.)*  Let `h⁰ : D^W → R_{≥0}` factor through `M`, say
     `h⁰(E) = ψ(M(E))` with `ψ : R² → R_{≥0}`.  If clause (c) holds for some `χ ∈ R`, then
     `I_∞(F,F) ≤ 0` for every primitive `F ∈ C_c^∞(R)` — that is, **RH**.
 (ii) *(Sufficiency, under the stated extra condition.)*  Conversely, assume RH and let
     `ψ : R² → R_{≥0}` satisfy

         ψ(a,b) + ψ(c−a,\,c−b) ≥ ab − \tfrac{c}{2}(a+b) + χ   for all (a,b) ∈ R²,  (19bis.13)

     with `c = Φ_K(0) = Φ_K(1) = ½` and some `χ ∈ R`.  Then clause (c) holds with that `χ`.  By
     Theorem 19bis.16, `ψ(a,b) = a^+b^+` satisfies (19bis.13) for every `χ ≤ 1/8` and for no larger
     `χ`.
 (iii) Consequently, for `h⁰_□` with `h_c = (·)^+` and `χ ≤ 1/8`: **clause (c) holds if and only if
     RH**.

The extra condition (19bis.13) is not removable: `ψ ≡ 0` factors through `M` and is nonnegative, yet
clause (c) then reads `0 ≥ ½I_∞(E,E) − ½I_∞(E,K) + χ`, whose right-hand side at `E = mK` is
`¼m² − ¼m + χ → +∞`, so no `χ` exists, under RH or otherwise.

*Proof.*  (ii) Assume RH.  For real `E ∈ D^W` every zero is `ρ = ½+iγ`, so `1−ρ = \barρ` and
`Φ_E(1−ρ) = Φ_E(\barρ) = \overline{Φ_E(ρ)}` (since `E` is real, `\overline{Φ_E(s)} = Φ_E(\bar s)`),
whence `W(E) = Σ_ρ|Φ_E(ρ)|² ≥ 0`.  By the reformulation in Theorem 19bis.16, clause (c) at `E` is
`W(E) ≥ 2χ − 2g(M(E))`, and (19bis.13) says exactly `g(M(E)) ≥ χ` with `g` built from `ψ` by
(19bis.12); so `W(E) ≥ 0 ≥ 2χ − 2g(M(E))`.

(i) Suppose clause (c) holds with constant `χ` and `h⁰ = ψ∘M`.  Let `F ∈ C_c^∞(R)` be real and
primitive, so `M(F) = (0,0)`, hence `M(nF) = (0,0)` and `M(K−nF) = (½,½)` for every `n ≥ 1`.  Clause
(c) at `E = nF` reads

    ψ(0,0) + ψ(½,½) ≥ \tfrac12 I_∞(nF,nF) − \tfrac12 I_∞(nF,K) + χ = \tfrac{n²}{2}I_∞(F,F) + χ ,

using `I_∞(nF,K) = ½\deg(nF) = 0` (Theorems 11.8(i), 11.13(iii)).  The left-hand side is independent
of `n`, so `I_∞(F,F) ≤ 0`.  By Paper 45 Theorem 10.4, quoted as (1.10), `I_∞(F,F) ≤ 0` on every
primitive `F ∈ C_c^∞` is equivalent to RH.

(iii) combines (i) and (ii) with Theorem 19bis.16.  ∎  `PROVED`

> **Clause (c) is not a reduction of RH here; it is RH.**  The tensor square supplies the growth
> constant and nothing else: the quadratic term `½I_∞(E,E)` of clause (c) contains `−½W(E)`, which a
> bidegree-function cannot see, and the whole gap between `2ab` and `I_∞(E,E)` is `W(E)`.

### 19bis.4 Why the route closes: clause (b′) and the bidegree witness

**Lemma 19bis.18 (the unconditional moment bound; `PROVED`).**  Let `E' ∈ D^W` with `E' ≥ 0`, and put
`(a,b) = M(E')`.  Then `a,b ≥ 0`, and for every `s` with `β := \mathrm{Re}\,s ∈ [0,1]`,

    |Φ_{E'}(s)| ≤ Φ_{E'}(β) ≤ Φ_{E'}(0)^{1−β}Φ_{E'}(1)^{β} = b^{1−β}a^{β} ≤ \max(a,b) .

*Proof.*  `|Φ_{E'}(s)| = |∫E'(t)e^{(s−½)t}dt| ≤ ∫E'(t)e^{(β−½)t}dt = Φ_{E'}(β)` because `E' ≥ 0`.
Log-convexity of `β ↦ Φ_{E'}(β)` on `[0,1]` is Hölder's inequality with exponents `1/(1−β)` and `1/β`
applied to the factorization `E'^{1−β}e^{−(1−β)t/2}·E'^{β}e^{βt/2}`.  Non-negativity of `a` and `b` is
immediate from `E' ≥ 0`.  ∎  `PROVED`

**Theorem 19bis.19 (clause (b′) fails for every bidegree-function; `PROVED`).**  Let
`h⁰ : D^W → R_{≥0}` factor through `M` and not vanish identically.  Then **clause (b′) fails**: there
is `E ∈ D^W` with `h⁰(E) > 0` and **no** `E' ∈ D^W` with `E' ≥ 0`, `E' ≢ 0` and `E − E' ∈ 𝓝_∞`.

*Proof.*  Pick `E_0` with `h⁰(E_0) > 0` and put `(a,b) := M(E_0)`.  If `a < 0` or `b < 0`, take
`E := E_0` and we are done: by Theorem 11.11, `E − E' ∈ 𝓝_∞` forces `M(E') = M(E)`, and by Lemma
19bis.18 no nonnegative `E'` has a negative bidegree entry.  So assume `a,b ≥ 0`.

Fix the first zero `ρ_1` of `ξ`.  Choose a real `g ∈ C_c^∞(R)` with `Φ_g(ρ_1) ≠ 0`; this is possible,
since `Φ_g(ρ_1) = ∫g(t)e^{(ρ_1−½)t}dt` vanishing for every real `g ∈ C_c^∞` would force the continuous
function `t ↦ e^{(ρ_1−½)t}` to be identically `0`.  Put

    F := Πg = −g'' + ¼g ∈ C_c^∞(R) ⊂ D^W ,

real, with `Φ_F(s) = s(1−s)Φ_g(s)` (Lemma 11.2(iv)); then `Φ_F(0) = Φ_F(1) = 0`, so `F` is
**primitive** with `M(F) = (0,0)`, and `Φ_F(ρ_1) = ρ_1(1−ρ_1)Φ_g(ρ_1) ≠ 0`.  Choose `t > 0` with

    |Φ_{E_0}(ρ_1) + t\,Φ_F(ρ_1)| > \max(a,b) ,

possible because `Φ_F(ρ_1) ≠ 0`, and set `E := E_0 + tF`.  Then `M(E) = (a,b)`, so
`h⁰(E) = h⁰(E_0) > 0`.  Suppose `E' ≥ 0`, `E' ≢ 0`, with `E − E' ∈ 𝓝_∞`.  By Theorem 11.11,
`M(E') = M(E) = (a,b)` and `Φ_{E'}(ρ_1) = Φ_E(ρ_1) = Φ_{E_0}(ρ_1) + tΦ_F(ρ_1)`.  By Lemma 19bis.18,
`|Φ_{E'}(ρ_1)| ≤ \max(a,b)`, contradicting the choice of `t`.  ∎  `PROVED`

**The class `E_t = E_0 + tF`, with `F ∈ C_c^∞(R)` primitive and `Φ_F(ρ_1) ≠ 0` — constant bidegree,
unbounded zero data — is the *bidegree witness*.**  It is the witness of the theorem just proved, and
it is the class that Proposition 19.7 tests the Riemann–Roch candidate against.

**Corollary 19bis.20 (`PROVED`).**  `h⁰_□` fails clause (b′), for every curve Riemann–Roch function
`h_c`; and so does every variant obtained by **adding** a nonnegative term, such as
`h⁰_□ + h⁰_{\mathbb Z}` with the lattice count of Definition 13.4, or `h⁰_□` plus any nonnegative
function of the Frobenius data.  By contrast Theorem 13.5(iv) proves that `h⁰_{\mathbb Z}` **alone**
does satisfy (b′); the tensor factor destroys that.

*Proof.*  The sum is `> 0` wherever `h⁰_□` is, so the witness `E = E_0 + tF` of Theorem 19bis.19 is
unchanged and the same contradiction applies.  For the contrast, `Λ_W ⊂ 𝓝_∞` and the defining set of
`h⁰_{\mathbb Z}` is nonempty exactly when `E` is congruent to an effective class, which is Theorem
13.5(iv).  ∎  `PROVED`

**Proposition 19bis.21 (clause (b′) as a moment problem; `PROVED` / `OPEN`).**  For `E ∈ D^W` the
condition *"there is `E' ≥ 0`, `E' ≢ 0`, with `E − E' ∈ 𝓝_∞`"* is, by Theorem 11.11, exactly: there
exists a continuous `E' ≥ 0` on `R` with `E'^{(j)}(t) = O(e^{−(1+ε)|t|})` for `j ≤ 2`, such that

    ∫E'(t)e^{t/2}dt = a ,   ∫E'(t)e^{−t/2}dt = b ,   ∫E'(t)e^{(ρ−½)t}dt = Φ_E(ρ)\ \ ∀ρ ∈ Z(ξ). (19bis.14)

This is a **moment problem on the family of exponentials** `\{e^{(s−½)t}\}_{s ∈ \{0,1\}∪Z(ξ)}` with a
nonnegativity constraint on the density.  Unconditional necessary conditions: `a,b ≥ 0`;
`|Φ_E(ρ)| ≤ b^{1−β_ρ}a^{β_ρ}` at every zero (Lemma 19bis.18); and `\deg E = a+b > 0` unless
`E ∈ 𝓝_∞` (Theorem 11.13(i)).  The moment cone

    𝔐 := \{(M(E'),\,(Φ_{E'}(ρ))_ρ) : E' ∈ D^W,\ E' ≥ 0,\ E' ≢ 0\} ⊂ R² × ℓ^1(Z(ξ))

is the object clause (b′) quantifies over; **its description is `OPEN`**, and by Theorem 19bis.19 it is
the whole remaining content of (b′).  `PROVED` (the reformulation), `OPEN` (the cone).

*Proof.*  The reformulation is Theorem 11.11 read against Definition 11.1; the three necessary
conditions are as cited.  ∎

Clause (b′) is therefore neither Weil positivity in disguise nor a consequence of it: the necessary
condition `|Φ_E(ρ)| ≤ \max(a,b)` constrains the **size** of the zero data, whereas Weil positivity
constrains its **sign**.  The two are logically independent, and the zeros enter (19bis.14) only at the
line `Φ_{E'}(ρ) = Φ_E(ρ)`.

**Theorem 19bis.22 (pairing against the realization adds nothing; `PROVED`).**  Let
`h⁰ : D^W → R_{≥0}` be any function of the pairings of `E` against the Pólya realization, that is
`h⁰(E) = Ψ\big((I_∞(E,r(D)))_{D ∈ Div_□⊗R}\big)` for some functional `Ψ`.  Then `h⁰` **factors
through `M`**, and Theorems 19bis.17(i) and 19bis.19 apply verbatim: clause (c) implies RH, and clause
(b′) fails.

*Proof.*  By Theorem 19bis.8(ii), `Φ_{r(D)}` vanishes at every zero, so (11.6) gives
`I_∞(E,r(D)) = Φ_E(0)Φ_{r(D)}(1) + Φ_E(1)Φ_{r(D)}(0)`, a function of `M(E)` alone, with coefficients
depending on `D` only.  Hence the whole family of pairings is a function of `M(E)`, and so is `h⁰`.
∎  `PROVED`

The same conclusion covers the transport-invariant variants.  The Frobenius action `E ↦ τ_{\log n}E`
sends `M(E) = (a,b)` to `(n^{1/2}a,\,n^{−1/2}b)`, so it preserves the product `ab` — the
unimodularity `λ_−λ_+(Frob_n) = 1` of Theorem 19bis.3(iii) — and also preserves `W`, hence `I_∞`
itself.  A tensor square `h_c(a)h_c(b)` is transport-invariant iff it factors through `ab`: given
`a,b > 0` and `a',b' > 0` with `ab = a'b'`, take `n := (a'/a)²`, so that `n^{1/2}a = a'` and
`n^{−1/2}b = (a/a')b = b'`.  The growth demand then forces `ψ(x) ≥ x` for large `x`, and `ψ(x) = x^+`
gives `h⁰(E) = (ab)^+`, a sub-family of Definition 19bis.14 to which Theorems 19bis.17 and 19bis.19
apply unchanged.

**Corollary 19bis.23 (what an admissible `h⁰` must see; `PROVED` / `GUIDANCE`).**  If `h⁰` satisfies
clause (b′) and is not identically `0`, then `h⁰` is **not** constant on the cosets
`E + (P^W ∩ C_c^∞)`; equivalently, `h⁰` must **separate two classes of equal bidegree with different
zero data**.  `PROVED`.  Since by Theorem 11.11 the pair `(M(E),Z(E))` determines `E` modulo `𝓝_∞`,
and since a definition may not name a zero, an admissible `h⁰` must read `Z(E)` **through the
arithmetic side** — through the pairings `I_∞(E,X)` for classes `X` with `Z(X) ≠ 0`, each of which is
`\mathrm{PRIME} − \mathrm{ARCH}` of `E ⋆ X^∨` by Definition 11.4 and Lemma 11.4a, and therefore names
no zero.  `r(Div_□)` is exactly the **wrong** family of such `X`: every one of its members has
`Z = 0`.  `GUIDANCE`.

*Proof.*  The first sentence is the construction of Theorem 19bis.19: the witness `E_t = E_0 + tF`
with `F` primitive in `C_c^∞` and `M(F) = 0` has the bidegree of `E_0` and unbounded zero data, and
`h⁰` must distinguish it from `E_0`.  The rest is Theorem 11.11 together with Definition 11.4's
declaration that `I_∞` is a definition by the arithmetic side, naming no zero, and Theorem
19bis.8(ii) for the last clause.  ∎

### 19bis.5 The complementary failure, and what it asks for

Two candidate `h⁰` are now on the table, and they fail on **opposite** clauses of Theorem 12.3.  The
Frobenius-lattice count `h⁰_{\mathbb Z}` of §18 satisfies (a) and (b′) and fails (c), its growth being
`(\log m)^{3/2}` where `m²` is required.  The tensor square `h⁰_□` of this section satisfies (a) and
the growth half of (c) — exactly, with the constant `(r²/4)m²`, over every number field — and fails
(b′) for **every** bidegree-function, by Theorem 19bis.19.

By Corollary 19bis.23 the missing ingredient is the same for both.  What is wanted is an `h⁰` that
reads the zero data through the **arithmetic Gram entries of the pure Frobenius family (A)** — the
form whose weights `Λ(q^k)q^{−k/2}` are the Euler product read directly, which the second method
constraint of §18 demands and which the realization `r` deletes.  Theorem 19bis.12 says in the same
breath why that is not a mere matter of writing the candidate down: Paper 44 Theorem 8bis.4a proves
that (A)'s own form is **not positive at any finite chart**, unconditionally, its colimit version
remaining `OPEN`; while the form whose sign is RH, (B), is precisely the one that has forgotten the
factorization.  No object in the corpus carries both.

That is the demand §20 takes up: a pairing family with nonzero zero data, built from the Frobenius
traces themselves rather than from their bidegrees.

> **`OPEN` (the Connes–Consani counting function as `h_c`).**  The candidate obtained by taking
> `h_c^{CC}(x) = \lceil(x+\log2)/\log3\rceil − \mathbf 1_L(x)` for `x ≥ −\log2` and `0` below —
> import **(X17)** — has slope `λ_{CC} = 1/\log 3 = 0.910239226627\ldots < 1` in its own degree, and
> **if** one declares the identification `\deg_{CC} = \deg` in nats it yields
> `h⁰_□(mK_K) = λ_{CC}²(r²/4)m² + O(m)` with `λ_{CC}² = 0.828535449690\ldots`, short of the
> requirement, so that clause (c) fails at `E = mK_K` for large `m`.  That is a **conditional**
> statement and nothing more: the identification `\deg_{CC} = \deg` is not in the corpus, and matching
> the two canonical classes instead (`\deg K_{CC} = −2\log 2` against `\deg K = 1`) is a different
> dictionary that can reverse the verdict — the reconciliation Finding 13.8 records as open and
> refuses to make by fiat (**U1**); and `\dim_{\mathbb S}` is an integer count over the sphere
> spectrum while the `h⁰` slot of Theorem 12.3 is a real-valued functional on `D^W`, with no map
> between the two constructed anywhere (**U2**).  Until U1 and U2 are settled the status of this
> candidate **at clause (c)** is `OPEN`, not `REFUTED`.  It changes nothing overall: the candidate
> fails **(b′)** outright by Theorem 19bis.19, which is a statement about bidegree-functions and is
> independent of every unit convention.  (Both numerical values are arithmetic of `\log 3`, printed by
> `scripts/certify_chi.py`, and are used only inside the conditional.)

**Withdrawn in this section**

| claim | reason |
|---|---|
| *"the Euler-product structure of the Frobenius family realizes, on `D^W`, entirely inside the ruling plane"* — i.e. reading the collapse onto `NS(P¹×P¹)` as a statement about the Frobenius family, or about the square | `REFUTED`.  The collapse is a property of the **Pólya realization** `r` of Definition 19bis.7, one choice among many, which deletes the weights `Λ_K(𝔫)N𝔫^{−½}` and remembers only `N𝔫`.  Paper 44 Theorem 8bis.4a shows the family's own Gram form (A) behaves in the opposite way — sparse, arithmetic, and unsigned at every finite chart (Theorem 19bis.12) |
| the value `χ = ¼` for the constant of clause (c) with `h⁰_□` | `REFUTED` by Theorem 19bis.16: `\inf g = c²/2 = 1/8` for `ξ`, so `χ ≤ 1/8`; at `E = ½K` and `χ = ¼` clause (c) reads `1/8 ≥ 3/16`, false by `1/16`.  The extremal witness is `½F_1`, not a multiple of `K`, and the `K`-line gives only `χ ≤ 3/16` |
| the reading *"clause (c) forces a lower bound on `W(E)` which fails at `E = tK`"* | the obstruction is a **ceiling on `χ`**, not a lower bound on `W`: Theorem 19bis.16(iii) |
| the biconditional *"for **any** `h⁰` factoring through `M`, clause (c) holds for some `χ` iff RH"* | the sufficiency half is false in that generality: `ψ ≡ 0` factors through `M`, and clause (c) at `E = mK` then requires `0 ≥ ¼m² − ¼m + χ` for all `m`, so no `χ` exists, under RH or otherwise.  What is proved is Theorem 19bis.17: necessity in general, sufficiency under (19bis.13) |
| *"`F_1,F_2` are the rulings `e_∓` of Paper 43 §9"* | false as an identity of classes: `e_± ∉ D^W` (Proposition 14.1(iv), Paper 43 Theorem 9.14c).  `F_1,F_2` are `a_0`-dependent **lifts of the ruling data** `M = (1,0),(0,1)`, canonical only modulo `𝓝_∞` (Definition 19bis.7) |
| the composition law stated *"for coprime `m,n`"* | a needless weakening: Paper 44 Theorem 3ter.4(i) holds for all `m,n ≥ 1`, and Theorem 19bis.3(i) for all integral ideals; in particular `Frob_p ⋆ Frob_p = Frob_{p²}` exactly |
| *"`L_S := O_{K,S}`, the ring of `S`-integers"* as the integral lattice | with it, `𝔫O_{K,S} = O_{K,S}` for every admissible `𝔫`, the cone is acyclic and both `H^0` and `deg_{\det}` vanish.  The lattice of record is the product of completions, Definition 19bis.4, the literal transport of Paper 44 Definition 6bis.1 |
| *"the translate datum `T_n` of Restatement 19bis.13 is the line the falsifier `Ξ_Q` lacks, hence the first shape in which a sign clause is formulable"* | a hope, not a result: nothing shows `T_n` multiplicative in `n`, nor that `Frob_𝔪⋆Frob_𝔫 = Frob_{𝔪𝔫}` bears on it.  `T_n` is a **translate** datum, and `τ_{\log m}τ_{\log n} = τ_{\log mn}` is the group law of `R`, which `Ξ_a` has as well; the property invoked does not separate the models |
| the Connes–Consani candidate as a **refutation** at clause (c) | withdrawn; it stands `OPEN` with the two units problems U1 (the degree dictionary) and U2 (`\dim_{\mathbb S}` against a real functional), as recorded in the remark above.  Its failure of (b′) is unaffected |
| the word *"certifying"* applied to the constant sweep | the grid sweep uses no Lipschitz or interval bound and the minimizer `(½,0)` need not be a grid node; it is a consistency check.  The value `c²/2` is proved in Theorem 19bis.16 |

### Imports used

**None.**  This section introduces no new external input.  It cites the existing tag **(X17)**
(Connes–Consani) once, in the `OPEN` remark on the counting function `h_c^{CC}`; the classical facts
used in the proofs — the product formula, the Chinese Remainder Theorem, multiplicativity of the
ideal norm, Hölder's inequality, Bochner's theorem and Bohr's theory of almost periodic functions,
and the intersection numbers of `P¹×P¹` — are labelled `CLASSICAL` at the point of use, in the manner
of §11.

---

## 20. The trace-positive cone

*Provenance note.  The statements and proofs of this section are taken from
`03-research/phase-141-row-d-frobenius-traces/R141_001_ROUND1.md` (§D.26),
`03-research/phase-143-row-d-trace-positive-cone/R143_001_ROUND1.md` (§D.34) and
`03-research/phase-144-row-d-fixed-index/R144_001_ROUND1.md` (§D.37–§D.40);
the labels of record, and the withdrawals tabulated at the end, are those of
`R143_002`, `R143_004`, `R143_005`, `R144_002`, `R144_004` and `R144_005`.*

Conventions are those of §11 throughout: `D^W` (Definition 11.1),
`Φ_E(s) = ∫E(t)e^{(s−½)t}dt`, `M(E) = (Φ_E(1),Φ_E(0)) =: (a,b)`, `\deg E = a+b`,
`I_∞(F,G) = Φ_F(0)Φ_G(1)+Φ_F(1)Φ_G(0) − Σ_ρΦ_F(ρ)Φ_G(1−ρ)` (Definition 11.4,
Lemma 11.4a, Theorem 11.5), the canonical class `K` with `Φ_K = ξ` (Theorem 11.7),
and the radical `𝓝_∞` (Theorem 11.11).  `τ_c` is the modulus translation of (1.5).
Landau's theorem is import **(X20)** of §17 and the zero data (V1),(V2) are import
**(X19)** of §12; neither is restated here.

This section carries out, in full, the analysis of the cone `B4` that §19 isolated as
the one surviving candidate for a Horn-B effective cone.

### 20.1 The Frobenius traces, and the moment cone

The object is the family of pairings of a class against the modulus translates of one
fixed test class, indexed by the **multiplicative** semigroup `N`.

**Lemma 20.1 (the test class exists; `PROVED`).**  There is a real, even
`g ∈ C_c^∞(R)` with `g ≥ 0`, `g ≢ 0`, such that `Φ_g(1−ρ) ≠ 0` for every zero `ρ` of
`ξ`.  Any such `g` also has `Φ_g(ρ) ≠ 0` at every zero, and `Φ_g(0) > 0`, `Φ_g(1) > 0`.

*Proof.*  Fix `T > 0` and let `E_T` be the real Fréchet space of **even**
`φ ∈ C_c^∞([−T,T])` with its usual seminorms `‖·‖_{C^k}`.  Choose `g_0 ∈ E_T` with
`g_0 > 0` on `(−T,T)`, fix `δ ∈ (0,T/2)`, and put `κ := \min_{[−T+δ,T−δ]}g_0 > 0`.  Let

    U := \{h ∈ E_{T−δ} : ‖h‖_{C^0} < κ\} ,

an open neighbourhood of `0` in the Fréchet space `E_{T−δ}`.  For `h ∈ U` one has
`g_0+h ≥ 0`: on `[−T+δ,T−δ]` because `g_0 ≥ κ > ‖h‖_{C^0}`, and off that interval
because `h ≡ 0` there and `g_0 ≥ 0`.

For a zero `ρ` let `ℓ_ρ : E_{T−δ} → C`,
`ℓ_ρ(h) := Φ_{g_0+h}(1−ρ) = Φ_{g_0}(1−ρ) + Φ_h(1−ρ)`, an affine continuous map.  Its
linear part `h ↦ Φ_h(1−ρ) = ∫h(t)\cosh((½−ρ)t)\,dt` (the function `h` being even) is
**not** the zero functional: `t ↦ \cosh((½−ρ)t)` is a nonzero real-analytic function,
so it is non-orthogonal to some even test function supported in `(−T+δ,T−δ)`.  Hence
`A_ρ := ℓ_ρ^{−1}(0)` is a closed affine hyperplane in `E_{T−δ}`, in particular closed
with empty interior.  The zero set `Z(ξ)` is countable, so `⋃_ρ A_ρ` is meagre; by
Baire's theorem the open set `U` is not contained in it, and any
`h ∈ U ∖ ⋃_ρ A_ρ` gives `g := g_0+h`.

`Φ_g(ρ) ≠ 0` follows because `Z(ξ)` is invariant under `ρ ↦ 1−ρ` ((E2)).
`Φ_g(0) = ∫g\,e^{−t/2} > 0` and `Φ_g(1) = ∫g\,e^{t/2} > 0` since `g ≥ 0`, `g ≢ 0`.  ∎
`PROVED`

The choice is non-constructive.  Two consequences must be stated rather than left
implicit: the trace map below **depends on a choice made through the zero set** — a
non-vanishing condition, not a location statement, but a quantification over zeros all
the same; and for each comparison model the class `g` must be re-chosen, so the trace
map is not one object transported across models but the same construction performed
separately in each.  Only `Φ_g(1−ρ) ≠ 0` is ever used, and it is used only in the last
line of the proof of Lemma 20.4.

**Definition 20.2 (the Frobenius traces).**  With `g` as in Lemma 20.1, for `E ∈ D^W`
put

    t_0(E) := \big(Φ_E(1),\,Φ_E(0)\big) = M(E) ,
    t_n(E) := I_∞\big(E,\,τ_{\log n}g\big)  \qquad (n ≥ 1) ,
    x(E)   := \big(t_0(E),\,(t_n(E))_{n≥1}\big) ∈ R^2 × R^{N_{≥1}} ,
    T : D^W → R^2 × R^{N_{≥1}},\qquad T(E) := x(E) .

`T` is real-linear.  By Definition 11.4 each `t_n(E)` is `PRIME − ARCH` of the even part
of `E ⋆ (τ_{\log n}g)^∨`: *it is defined by the arithmetic side and names no zero*.
`t_0(E)` is the polar packet, likewise zero-free.

**Lemma 20.3 (the two readings of `t_n`; `PROVED`).**  For every `E ∈ D^W` and `n ≥ 1`,

    t_n(E) = n^{½}Φ_g(1)Φ_E(0) + n^{−½}Φ_g(0)Φ_E(1) − Σ_ρ Φ_E(ρ)Φ_g(1−ρ)\,n^{½−ρ} ,   (20.1)

the sum absolutely convergent; and

    t_n(E) = ∫_R E(u)\,w_g(u−\log n)\,du ,                                            (20.2)

with `w_g` the bounded-density kernel (11.16) of Theorem 11.14,
`w_g(u) = Φ_g(1)e^{−u/2} + Φ_g(0)e^{u/2} − Σ_ρ e^{(ρ−½)u}Φ_g(1−ρ)`, and
`|w_g(u)| ≤ C_g\,2\cosh(u/2)` with `C_g ≤ Φ_g(0)+Φ_g(1)+Σ_ρ|Φ_g(1−ρ)| < ∞`.

*Proof.*  (20.1) is Theorem 11.5 applied to `(E, τ_{\log n}g)` together with
`Φ_{τ_cg}(s) = e^{(s−½)c}Φ_g(s)` (Lemma 11.2(iv)) at `s = 1, 0, 1−ρ` and `c = \log n`.
For (20.2), Theorem 11.14(i) gives `I_∞(E,F) = ∫E\,w_F`; and `w_{τ_cg}(u) = w_g(u−c)`,
read off (11.16) with the same three substitutions.  The bound is (11.17).  ∎  `PROVED`

**Lemma 20.4 (separation of the exponentials `n^{½−ρ}`; `PROVED`).**  Let
`(c_ρ)_{ρ∈Z(ξ)}` be complex numbers, indexed by the zero **multiset**, with
`Σ_ρ|c_ρ|(1+|γ_ρ|)^A < ∞` for every `A > 0`.  If

    Σ_ρ c_ρ\,n^{½−ρ} = 0 \qquad\text{for every integer } n ≥ 1 ,

then `c_ρ = 0` for every `ρ`.

*Proof.*  Put `s_ρ := ρ−½`, so `|\mathrm{Re}\,s_ρ| ≤ θ = ½` by (E2).  For
`\mathrm{Re}\,w > 3/2`,

    Σ_{n≥1} n^{−w}\Big(Σ_ρ c_ρ n^{−s_ρ}\Big) = Σ_ρ c_ρ\,ζ(w+s_ρ) =: G(w) ,

the interchange legitimate because `Σ_ρ|c_ρ|Σ_n n^{−\mathrm{Re}\,w+½} < ∞` there.  By
hypothesis the left-hand side is `0`, so `G ≡ 0` on `\mathrm{Re}\,w > 3/2`.

`G` is meromorphic on `C`.  Fix a compact `𝒦 ⊂ C`.  Only finitely many `ρ` have
`3/2−ρ` within distance `1` of `𝒦`, since `|γ_ρ| → ∞`; their terms are meromorphic with
a single simple pole each.  For the remaining `ρ`, `w ∈ 𝒦` gives
`|\mathrm{Im}(w+s_ρ)| ≥ |γ_ρ| − C_𝒦 ≥ 1` and `\mathrm{Re}(w+s_ρ) ≥ −C_𝒦`; by the
classical polynomial bound `|ζ(σ+it)| ≪_{σ_0}(1+|t|)^{A_0}`, valid uniformly for
`σ ≥ σ_0` and `|t| ≥ 1` (`CLASSICAL`), those terms are bounded by
`|c_ρ|(1+|γ_ρ|)^{A_0}·C`, and the tail converges uniformly on `𝒦` by hypothesis.  So
`G` is holomorphic on `𝒦` off the finitely many points `3/2−ρ`.

Hence `G` is meromorphic on `C`, holomorphic off `\{3/2−ρ\}`, and vanishes on a
half-plane; by the identity theorem on the connected open set `C ∖ \{3/2−ρ\}` it
vanishes identically there, so every pole is removable.  The residue of `G` at
`w = 3/2−ρ_0` is `m(ρ_0)\,c_{ρ_0}`, with `m(ρ_0) ≥ 1` the multiplicity, since
`\mathrm{Res}_{s=1}ζ = 1` and `3/2−ρ` determines `ρ`.  Therefore `c_{ρ_0} = 0`.  ∎
`PROVED`

For a general admissible comparison model the same proof runs with
`θ := \sup_ρ|\mathrm{Re}\,ρ−½| < ∞` and the half-plane `\mathrm{Re}\,w > 1+θ`.

**Theorem 20.5 (the traces determine the class; `PROVED`).**  With `g` as in
Lemma 20.1,

    \ker T = 𝓝_∞ ,

i.e. `x(E) = x(E')` if and only if `E − E' ∈ 𝓝_∞`.  In particular the traces determine
`(M(E),Z(E))` and hence, by Theorem 11.11, the class of `E` in `D^W/𝓝_∞`; and every
function of the traces is automatically a function on `D^W/𝓝_∞`.

*Proof.*  `⊇`: if `N ∈ 𝓝_∞` then `Φ_N(0) = Φ_N(1) = 0` and `Φ_N(ρ) = 0` for all `ρ`
(Theorem 11.11), so `t_0(N) = 0` and, by (20.1), `t_n(N) = 0`.

`⊆`: let `x(E) = 0`.  Then `Φ_E(0) = Φ_E(1) = 0`, and (20.1) reduces to
`Σ_ρ c_ρ n^{½−ρ} = 0` for all `n ≥ 1`, with `c_ρ := Φ_E(ρ)Φ_g(1−ρ)`.  The decay
hypothesis of Lemma 20.4 holds: `|Φ_E(ρ)| ≤ C_2(E)|γ_ρ|^{−2}` by (11.2), and
`g ∈ C_c^∞([−T,T])` gives, for every `M`,
`|Φ_g(1−ρ)| = |∫g(t)e^{(½−ρ)t}dt| ≤ C_M e^{T/2}(1+|γ_ρ|)^{−M}` by `M` integrations by
parts; together with `Σ_ρ(1+|γ_ρ|)^{−2} < ∞` ((E3d)) this gives
`Σ_ρ|c_ρ|(1+|γ_ρ|)^{A} < ∞` for every `A`.  By Lemma 20.4, `c_ρ = 0`; since
`Φ_g(1−ρ) ≠ 0` (Lemma 20.1), `Φ_E(ρ) = 0` at every zero.  By (11.14), `E ∈ 𝓝_∞`.  ∎
`PROVED`

This licenses writing `h⁰ = Ψ∘T`: no information is lost.  It does **not** say the
traces are a convenient coordinate system — Lemma 20.4 is an inversion in infinitely
many coordinates with no modulus of continuity, and every quantitative statement below
is proved directly, never through the inverse.

**Lemma 20.6 (the finite trace windows are unobstructed; `PROVED`).**  For every
`N ≥ 1` the map `E ↦ (Φ_E(1),Φ_E(0),t_1(E),…,t_N(E)) ∈ R^{N+2}` is **surjective** on
`D^W`, and `F ↦ (t_1(F),…,t_N(F)) ∈ R^{N}` is **surjective** on the primitive subspace
`P^W ∩ C_c^∞(R)`.

*Proof.*  Both maps are linear; if one were not surjective, some nonzero real `λ` would
annihilate its image.  By Theorem 11.8(iii),
`I_∞(E,τ_cK) = ½(e^{c/2}Φ_E(0)+e^{−c/2}Φ_E(1))`, so `Φ_E(0)` and `Φ_E(1)` are fixed
real combinations of `I_∞(E,K)` and `I_∞(E,τ_1K)`; hence in both cases the functional is
`E ↦ I_∞(E,X)` for

    X := α K + α' τ_1K + Σ_{n≤N} λ_n τ_{\log n}g ∈ D^W .

*First map.*  Vanishing for all `E ∈ D^W` means `X ∈ 𝓝_∞` (Theorem 11.11), so
`Φ_X(ρ) = 0` at every zero.  Since `Φ_K(ρ) = ξ(ρ) = 0`, this reads
`Φ_g(ρ)·Σ_{n≤N}λ_n n^{ρ−½} = 0`, and `Φ_g(ρ) ≠ 0`, so the exponential polynomial
`f(z) := Σ_{n≤N}λ_n e^{(z−½)\log n}` vanishes at every zero of `ξ`.  By Langer's theorem
(`CLASSICAL`: the number of zeros of `Σ_j a_je^{μ_jz}` with `|\mathrm{Im}\,z| ≤ T` is
`(μ_{\max}−μ_{\min})T/π + O(1)`), a nonzero `f` has at most `T\log N/π + O(1)` such
zeros, while `N_ξ(T) = (T/π)\log(T/2πe) + O(\log T)` ((E3d), Riemann–von Mangoldt,
`CLASSICAL`) exceeds it for `T > 2πeN`.  So `f ≡ 0`, i.e. every `λ_n = 0`; then
`Φ_X(0) = Φ_X(1) = 0` forces `α = α' = 0`.

*Second map.*  Here `α = α' = 0` from the start, and vanishing for all primitive
`E ∈ C_c^∞` means `X ⊥_{I_∞}(P^W ∩ C_c^∞)`; by Theorem 11.10, `Φ_X(ρ) = 0` at every
zero of `ξ`.  The same Langer / Riemann–von Mangoldt comparison applies.  ∎  `PROVED`

**Definition 20.7 (the moment cone).**

    𝔐 := T\big(\{E ∈ D^W : E ≥ 0,\ E ≢ 0\}\big) = \{x(E') : E' ≥ 0,\ E' ≢ 0\} .

**Theorem 20.8 ((b′) is exactly a containment of cones; `PROVED`).**  Let `h⁰ = Ψ∘T`
for any `Ψ : R^2×R^{N_{≥1}} → R_{≥0}`.  Then clause (b′) of Theorem 12.3 holds for `h⁰`
**if and only if**

    \{x ∈ T(D^W) : Ψ(x) > 0\} ⊆ 𝔐 .                                            (20.3)

*Proof.*  (b′) says: `Ψ(x(E)) > 0 ⟹ ∃E' ≥ 0`, `E' ≢ 0`, with `E−E' ∈ 𝓝_∞`.  By
Theorem 20.5, `E−E' ∈ 𝓝_∞ ⟺ x(E) = x(E')`.  So the conclusion of (b′) at `E` is exactly
`x(E) ∈ 𝔐`.  ∎  `PROVED`

The traces of `𝓝_∞` vanish, so no `𝓝_∞`-correction appears in (20.3) and (b′) is a
statement about `𝔐` alone.

**Theorem 20.9 (structure of the moment cone; `PROVED`).**
 (i) `𝔐 ∪ \{0\}` is a **convex cone**: `𝔐 + 𝔐 ⊆ 𝔐` and `λ𝔐 = 𝔐` for `λ > 0`.
 (ii) `𝔐` is **pointed**: `𝔐 ∩ (−𝔐) = ∅`, and `0 ∉ 𝔐`.
 (iii) *(the degree half-space)* every `x ∈ 𝔐` has `x_{0,1} > 0` and `x_{0,2} > 0`; in
     particular **no trace vector of a primitive class lies in `𝔐`**, and no trace
     vector of a class of degree `≤ 0` lies in `𝔐`.

*Proof.*  (i) `E_1,E_2 ≥ 0`, `≢ 0` gives `E_1+E_2 ≥ 0`, `≢ 0`, and `T` is linear;
likewise for `λ > 0`.  (ii) If `x ∈ 𝔐 ∩ (−𝔐)`, say `x = x(E_1) = −x(E_2)` with
`E_i ≥ 0`, `E_i ≢ 0`, then `x(E_1+E_2) = 0`, so `E_1+E_2 ∈ 𝓝_∞` (Theorem 20.5) and
`\deg(E_1+E_2) = 0` (Theorem 11.13(ii)); but `\deg(E_1+E_2) > 0` (Theorem 11.13(i)).
The same argument with `E_2 := E_1` gives `0 ∉ 𝔐`.  (iii) `Φ_{E'}(1) = ∫E'e^{u/2} > 0`
and `Φ_{E'}(0) = ∫E'e^{−u/2} > 0` for `E' ≥ 0`, `E' ≢ 0`, continuous; a primitive class
has `Φ(0) = Φ(1) = 0`, and a class of degree `≤ 0` cannot have both coordinates
positive.  ∎  `PROVED`

Item (iii) is Theorem 11.13(i),(ii) in trace coordinates, and it is what does the work
below.  A barycentric description of `𝔐` as the moment cone of the curve
`u ↦ (2\cosh(u/2))^{−1}(e^{u/2},e^{−u/2},(w_g(u−\log n))_n)` is available by dividing
and multiplying (20.2) by `2\cosh(u/2)`, but it is a change of variable and not a
structure theorem, and the dual description of `𝔐` is proved in one inclusion only; the
paper uses neither.

### 20.2 The trace-positive cone `B4`

**Definition 20.10 (admissible test classes, and the cone).**  A class `g` is
**admissible** if it is real, even, lies in `C_c^∞(R)` or in `D^W` with `Φ_g(1−ρ)` of
rapid decay in `|γ_ρ|`, satisfies `g ≥ 0`, `g ≢ 0`, and satisfies the Baire condition
`Φ_g(1−ρ) ≠ 0` at every zero of `ξ` (Lemma 20.1 produces one).  For admissible `g`,

    B4^g   := \{E ∈ D^W : t_n(E) ≥ 0 \text{ for all } n ≥ 1\} ,
    B4^{g,0} := B4^g ∩ \{E : Φ_E(0) ≥ 0 \text{ and } Φ_E(1) ≥ 0\}\quad(\text{i.e. } t_0(E) ≥ 0) .

Both are convex cones (each condition is a linear inequality), both are
`𝓝_∞`-saturated, and both contain `𝓝_∞` (Theorem 20.5) — so every statement about them
is a statement mod `𝓝_∞`.  `B4^{g,0}` is the cone of record and is written `B4` where
the distinction is immaterial.  `B4^g` does depend on `g`: the traces do, and by
Lemma 20.6 the finite trace windows are unobstructed, so different admissible `g` give
different cones.  Every statement below is either "for every admissible `g`" or carries
an explicit `∃g`; none fixes `g` silently.

**Proposition 20.11 (the canonical class is inadmissible; `PROVED`).**  `K` is real,
even, positive (Theorem 11.7(i)) and lies in `D^W`, but it is **not admissible**, and it
fails the Baire condition maximally: `Φ_K(1−ρ) = ξ(1−ρ) = 0` at **every** zero.  With
`g = K` the traces would be purely polar,
`t_n(E) = ½(n^{½}Φ_E(0) + n^{−½}Φ_E(1))`, so every primitive class would have
`t_n ≡ 0 ≥ 0` and Theorem 20.15 below would be false: `B4^K ∩ P^W = P^W`.

*Proof.*  `Φ_K = ξ` (Theorem 11.7) and `ξ(1−ρ) = 0` at every zero by (E2); insert
`Φ_K(1−ρ) = 0` and `Φ_K(0) = Φ_K(1) = ½` into (20.1).  A primitive class has
`Φ_E(0) = Φ_E(1) = 0`, whence `t_n ≡ 0`.  ∎  `PROVED`

The Baire condition is exactly what makes the traces see the zero side.  The nearest
admissible class to `K` is `g = K + λh` with `h` admissible and `λ > 0` small, and that
is also the class that makes the condition `(G⁺)` of §20.4 unconditional.

**Remark 20.12 (`B4` is not an enlargement of the effective cone; `PROVED`).**
`𝓔 ⊄ B4`: for `E' ≥ 0`, `t_n(E') = ∫E'(u)w_g(u−\log n)\,du` by (20.2), and `w_g` is not
of one sign — it is the density (11.16), a polar part minus an almost-periodic part — so
nonnegativity of `E'` gives no sign for `t_n(E')`.  **`B4` is a different cone, not a
larger one.**  In particular `(b′)_{B4}` is not a weakening of (b′), and the refutation recorded at
Theorem 12.3, whose entire mechanism is a bound on the effective cone, says nothing
about `(b′)_{B4}`.

**Lemma 20.13 (the trace Dirichlet series; `PROVED`, unconditional).**  Let `E ∈ D^W`
be real and put `c_ρ := Φ_E(ρ)Φ_g(1−ρ)`.  Then `|t_n(E)| ≤ A(E)\,n^{½}` for all
`n ≥ 1`, the Dirichlet series `D_E(w) := Σ_{n≥1}t_n(E)n^{−w}` converges absolutely for
`\mathrm{Re}\,w > 3/2`, and there

    D_E(w) = Φ_g(1)\,b\,ζ(w−½) + Φ_g(0)\,a\,ζ(w+½) − Σ_ρ c_ρ\,ζ(w+ρ−½) .   (20.4)

The right-hand side continues `D_E` meromorphically to all of `C`, holomorphic except
for at most simple poles at

    w = 3/2 \;(\text{residue } Φ_g(1)b),\quad w = ½ \;(\text{residue } Φ_g(0)a),\quad
    w = 3/2−ρ \;(\text{residue } −m(ρ)\,c_ρ) ,

`m(ρ) ≥ 1` the multiplicity.  Every pole `3/2−ρ` has
`\mathrm{Re}(3/2−ρ) ∈ (½,3/2)` and `\mathrm{Im}(3/2−ρ) = −γ_ρ ≠ 0`.

*Proof.*  `|n^{½−ρ}| = n^{½−β_ρ} ≤ n^{½}` by (E2) (`0 < β_ρ < 1`), and
`Σ_ρ|c_ρ| < ∞` (proof of Theorem 20.5: `|Φ_E(ρ)| ≤ C_2(E)|γ_ρ|^{−2}` by (11.2),
`|Φ_g(1−ρ)| ≤ C_M(1+|γ_ρ|)^{−M}` by `M` integrations by parts,
`Σ(1+|γ_ρ|)^{−2} < ∞` by (E3d)); with `|n^{±½}| ≤ n^{½}` this gives the bound on
`|t_n|` and absolute convergence of `Σ t_nn^{−w}` for `\mathrm{Re}\,w > 3/2`.
Term-by-term summation of (20.1) against `n^{−w}` is legitimate there by the same
absolute convergence, and `Σ_n n^{½−ρ−w} = ζ(w+ρ−½)`; this is (20.4).  The continuation
is the argument of Lemma 20.4 verbatim: on a compact `𝒦 ⊂ C` only finitely many `ρ`
have `3/2−ρ` within distance `1` of `𝒦`, and for the rest
`|ζ(w+ρ−½)| ≪ (1+|γ_ρ|)^{A_0}` by the classical polynomial bound, so the tail converges
uniformly on `𝒦` by the rapid decay of `(c_ρ)`.  The residues are
`\mathrm{Res}_{s=1}ζ = 1` times the coefficients, with multiplicity as in Lemma 20.4.
`γ_ρ ≠ 0` because `ξ` has **no real zero** (Lemma 13.5b: `ξ > 0` on `R`).  ∎  `PROVED`

**Theorem 20.14 (the structure of `B4`; `PROVED`, unconditional).**  Let `E ∈ B4^g`,
i.e. `t_n(E) ≥ 0` for all `n ≥ 1`.  Then, with `a = Φ_E(1)`, `b = Φ_E(0)`:

 (i) `b ≥ 0`;
 (ii) if `b = 0` then `Φ_E(ρ) = 0` at **every** zero `ρ`, and `a ≥ 0`;
 (iii) hence `E ∈ B4^g`, `b = 0` and `a = 0` together imply `E ∈ 𝓝_∞`.

*Proof.*  By Lemma 20.13, `D_E` is meromorphic on `C` with the listed poles; the only
**real** points among them are `3/2` and `½`.  All `t_n ≥ 0`, so (X20) applies once the
abscissa of convergence `σ_c` is finite.

(i) If `b ≠ 0` there is a pole at `3/2`, so `σ_c ≥ 3/2`; and `σ_c ≤ 3/2` by
Lemma 20.13's bound `|t_n| ≤ An^{½}`.  So `σ_c = 3/2`, finite.  For real `σ > 3/2`,
`D_E(σ) = Σt_nn^{−σ} ≥ 0`, so
`\mathrm{Res}_{w=3/2}D_E = \lim_{σ↓3/2}(σ−3/2)D_E(σ) ≥ 0`, i.e. `Φ_g(1)b ≥ 0`, i.e.
`b ≥ 0` (indeed `b > 0` in this case).  If `b = 0` there is nothing to prove.

(ii) Let `b = 0`, and suppose `c_{ρ_0} ≠ 0` for some zero `ρ_0`.  Then `D_E` has a pole
at `3/2−ρ_0`, so it is not entire and `σ_c ≥ \mathrm{Re}(3/2−ρ_0) > ½`; also
`σ_c ≤ 3/2`.  By (X20) the **real** number `σ_c` is a singular point of `D_E`.  But
`D_E` is meromorphic with poles only at `½` and at the non-real points `3/2−ρ`, and
`σ_c > ½`; so `D_E` is holomorphic at `σ_c`.  Contradiction.  Hence `c_ρ = 0` for every
`ρ`, and `Φ_g(1−ρ) ≠ 0` gives `Φ_E(ρ) = 0` for every `ρ`.  Then
`t_n = Φ_g(0)\,a\,n^{−½}`, and `t_1 ≥ 0` gives `a ≥ 0`.

(iii) By (ii), `Φ_E(0) = Φ_E(1) = 0` and `Φ_E(ρ) = 0` at every zero; by (11.14) and
Theorem 11.11, `E ∈ 𝓝_∞`.  ∎  `PROVED`

**Theorem 20.15 ((T1′); `PROVED`, unconditional).**  For every admissible `g`,

    B4^g ∩ P^W ⊆ 𝓝_∞ ,

i.e. **there is no primitive `F ∉ 𝓝_∞` with `t_n(F) ≥ 0` for all `n ≥ 1`**.

*Proof.*  Primitive means `a = b = 0` (Theorem 11.13(iii), Definition 11.6); apply
Theorem 20.14(iii).  ∎  `PROVED`

What the proof used, exactly: (a) the index set of the traces is `N` and
`Σ_n n^{−w} = ζ(w)` has a **real** pole; (b) `0 < \mathrm{Re}\,ρ < 1` strictly (E2),
which puts every zero-pole strictly **between** the two polar poles `½` and `3/2`;
(c) `ξ` has no real zero (Lemma 13.5b), which makes every zero-pole non-real;
(d) Landau's theorem (X20).  No RH, no zero list, no equidistribution, no Euler
product.  What is *not* true is the literal (T1_cone) of §19 on `B4^g`: the class
`J := \cosh(1)K − τ_2K` has `Φ_J(ρ) = 0` at every zero,
`b_J = ½(\cosh 1 − e^{−1}) = 0.58760… > 0`, `a_J = ½(\cosh 1 − e) = −b_J < 0`,
`\deg J = 0`, and `t_n(J) = Φ_g(0)b_J(n^{½}−n^{−½}) ≥ 0` for all `n`; so
`J ∈ B4^g ∖ 𝓝_∞` with degree `0`.  On the cone of record the statement is restored:
`E ∈ B4^{g,0} ∖ 𝓝_∞ ⟹ \deg E > 0`, since `\deg E = a+b` with `a,b ≥ 0` and
`\deg E = 0` would force `a = b = 0` and Theorem 20.14(iii).  Neither form is what the
transfer theorem needs; Theorem 20.17 needs only (T1′).

### 20.3 The transfer theorem 12.3-B4

**Definition 20.16 (the clause).**  For a cone `𝓔' ⊆ D^W` containing `𝓝_∞`, let

    (b′)_{𝓔'}:\quad h⁰(E) > 0 \;⟹\; \text{there is } E' ∈ 𝓔' \text{ with } E − E' ∈ 𝓝_∞ .

Write `(b′)_{B4}` for `𝓔' = B4`.  The clause `E' ≢ 0` of (b′) in Theorem 12.3 is **not**
carried: Theorem 20.17 does not use it, so its hypothesis is weaker in that respect.

**Theorem 20.17 (the transfer theorem 12.3-B4; `PROVED`, unconditional).**
*Hypotheses carried:* the conventions of §11 (`D^W`, `I_∞`, `K`, `𝓝_∞`), imports
(E1)–(E6), (E3d), (X12), (X20), Lemma 13.5b, and the choice of an admissible `g`.
Suppose there is `h⁰ : D^W → R_{≥0}` with

  **(a)** `h⁰ ≥ 0`;
  **(b′)_{B4}** if `h⁰(E) > 0` then some `E' ∈ B4` has `E − E' ∈ 𝓝_∞`;
  **(c)** there is `χ ∈ R` with
      `h⁰(E) + h⁰(K−E) ≥ ½I_∞(E,E) − ½I_∞(E,K) + χ` for every `E ∈ D^W`.

Then `I_∞(F,F) ≤ 0` for every primitive `F ∈ C_c^∞(R)`, and hence **RH**, by Paper 45
Theorem 10.4.

*Proof.*  Fix a primitive real `F ∈ C_c^∞(R)`, `F ≢ 0`, and suppose
`q := I_∞(F,F) > 0`.  Since `F` is primitive, `\deg F = 0` and
`I_∞(F,K) = ½\deg F = 0` (Theorem 11.8).

*No ample class is used.*  The step of Theorem 12.3 that produces `H' = F+2mK` and
invokes Theorem 11.14 is deleted; so is any appeal to (T2_cone).  This is the one structural
gain of `B4` over the effective cone: the trace cone carries its own arithmetic and
needs no bounded-density bound.

*Step 1 (`h⁰` vanishes on `K−nF` for all large `n`).*  Suppose, for contradiction, that
`h⁰(K−nF) > 0` for arbitrarily large `n`.  For such `n`, `(b′)_{B4}` gives `E'_n ∈ B4`
with `K−nF−E'_n ∈ 𝓝_∞`; since the traces vanish on `𝓝_∞` (Theorem 20.5) and are
linear,

    0 ≤ t_m(E'_n) = t_m(K) − n\,t_m(F)\qquad\text{for every } m ≥ 1 ,

i.e. `t_m(F) ≤ t_m(K)/n`.  Fixing `m` and letting `n → ∞` along that sequence gives
`t_m(F) ≤ 0` for **every** `m ≥ 1`.  Then `−F` is primitive with `t_m(−F) ≥ 0` for all
`m`, so `−F ∈ 𝓝_∞` by Theorem 20.15, so `F ∈ 𝓝_∞` and `q = I_∞(F,F) = 0` (the radical,
Theorem 11.11) — contradicting `q > 0`.  Hence there is `n_0` with `h⁰(K−nF) = 0` for
all `n ≥ n_0`.

*Step 2 (`h⁰` is positive on `nF` for large `n`).*  Clause (c) at `E = nF`, with
`I_∞(nF,nF) = n²q` and `I_∞(nF,K) = 0`, gives `h⁰(nF) + h⁰(K−nF) ≥ ½n²q + χ`; for
`n ≥ n_0` the second term on the left vanishes, so `h⁰(nF) ≥ ½n²q + χ`, which is `> 0`
once `n > \max\{n_0,\ \sqrt{2\max(0,−χ)/q}+1\}`.  No hypothesis `χ ≥ 0` is needed.

*Step 3 (the contradiction, by primitivity).*  Fix such an `n`.  `(b′)_{B4}` gives
`E' ∈ B4` with `nF − E' ∈ 𝓝_∞`.  Then `Φ_{E'}(0) = Φ_{nF}(0) = 0` and
`Φ_{E'}(1) = 0`, i.e. `E'` is **primitive**, and `E' ∈ B4`; by Theorem 20.15,
`E' ∈ 𝓝_∞`, hence `nF ∈ 𝓝_∞` and `q = 0`.  Contradiction.

Hence `q ≤ 0` for every primitive `F ∈ C_c^∞(R)`, which is RH by Paper 45 Theorem 10.4,
imported as (1.10).  ∎  `PROVED`

**Remark 20.17a (what changed relative to Theorem 12.3).**  The two theorems are
**incomparable**, not nested: the hypothesis here is `(b′)_{B4}` and there it is (b′),
and by Remark 20.12 the two cones are incomparable.  The comparison that is true:
fewer and cheaper inputs about the cone.  Theorem 12.3 needs positive degree and degree
constancy on cosets (Theorem 11.13(i),(ii)) *plus* ampleness (Theorem 11.14);
Theorem 20.17 needs **one** fact about `B4`, namely (T1′), and that fact is proved, not
assumed.  Steps 1–2 of Theorem 12.3 collapse into a limit, and its degree contradiction
becomes a primitivity contradiction.  Consequently the conditions (T1_cone),(T2_cone) of §19 are
not the right axioms for a Horn-B cone — the right axiom is (T1′) — and §19's
bounded-density test is not a necessary condition on a candidate cone.  Dropping
`E' ≢ 0` from the clause is harmless: `E' = 0` forces `K−nF ∈ 𝓝_∞` in Step 1 and
`nF ∈ 𝓝_∞` in Step 3, and the argument closes either way.

The second §19 condition, (T2_cone), is outright false on `B4^g`.

**Lemma 20.18 (Gaussian single-zero directions; `PROVED` given (X19)).**  For `σ > 0`
and `φ ∈ R` put `F_σ^{(φ)}(u) := e^{−u²/2σ²}\sin(γ_1u+φ) ∈ D^W` (real, `C^∞`, Gaussian
decay), and write `G_σ := σ\sqrt{2π}/2`.  Then

 (i) `Φ_{F_σ^{(φ)}}(s) = \dfrac{σ\sqrt{2π}}{2i}\Big(e^{iφ}e^{((s−½)+iγ_1)²σ²/2} − e^{−iφ}e^{((s−½)−iγ_1)²σ²/2}\Big)`;
 (ii) `Φ_{F_σ^{(φ)}}(ρ_1) = iG_σe^{−iφ}\big(1+O(e^{−2γ_1²σ²})\big)` — modulus `G_σ`, argument a free parameter;
 (iii) `|Φ_{F_σ^{(φ)}}(0)|,\ |Φ_{F_σ^{(φ)}}(1)| ≤ 2G_σe^{(¼−γ_1²)σ²/2}`;
 (iv) `L_σ := Σ_{ρ≠ρ_1,\barρ_1}|Φ_{F_σ^{(φ)}}(1−ρ)| ≤ G_σΛ_σ` with
      `Λ_σ := 2Σ_{T≥21}2\log T\,e^{−σ²((T−γ_1)²−¼)/2} ≤ C\,e^{−23σ²}`, uniformly in `φ`.

In particular `L_σ/G_σ → 0` and `G_σ/L_σ ≥ c\,e^{23σ²} → ∞` as `σ → ∞`.

*Proof.*  (i) is `\sin x = (e^{ix}−e^{−ix})/2i` together with
`∫e^{−u²/2σ²}e^{αu}du = σ\sqrt{2π}e^{α²σ²/2}`.  (ii): at `s = ρ_1` the first exponent is
`(2iγ_1)²σ²/2 = −2γ_1²σ²` and the second is `0`.  (iii): at `s ∈ \{0,1\}` both exponents
have real part `(¼−γ_1²)σ²/2`.  (iv): for a zero `ρ = β+iγ`, `s = 1−ρ` gives
`s−½ = c−iγ` with `|c| < ½` by (E2), so both exponents have real part
`(c²−(γ∓γ_1)²)σ²/2 ≤ (¼−(|γ|−γ_1)²)σ²/2`; by (X19)(V2) `|γ| ≥ 21`, so
`|γ|−γ_1 ≥ 6.86` and the exponent is `≤ −23.4σ²`; summing over the zeros with the
unconditional Riemann–von Mangoldt count `\#\{γ ∈ [T,T+1]\} ≤ \log T` gives the stated
`Λ_σ`.  ∎  `PROVED` given (X19)

**Theorem 20.19 ((T2_cone) is false for `B4^g`; `PROVED` given (X19)).**  For every real
`X ∈ D^W` with `Φ_X(ρ_1) ≠ 0`,

    C'_X := \sup\{\,|I_∞(E,X)|/\deg E \;:\; E ∈ B4^g,\ \deg E > 0\,\} = +∞ .

*Proof.*  Let `J = \cosh(1)K − τ_2K` be the degree-`0` class of §20.2
(`b_J = −a_J = 0.58760… > 0`, zero sum identically `0`), fix `ε := 1`, and for `t > 0`
put `E_0 := tJ + εK`.  Then

    \deg E_0 = ε ,\qquad
    t_n(E_0) = Φ_g(0)\big[\,t\,b_J(n^{½}−n^{−½}) + \tfrac ε2(n^{½}+n^{−½})\,\big] ,

so `t_1(E_0) = Φ_g(0)ε > 0` and, for `n ≥ 2`,
`t_n(E_0) ≥ Φ_g(0)tb_Jn^{½}(1−1/n) ≥ ½Φ_g(0)tb_Jn^{½}`.  Put
`κ := \max_ρ|Φ_g(1−ρ)| < ∞` and, for `σ ≥ 1` and `φ ∈ R` to be chosen,
`E := E_0 + rF_σ^{(φ)}`.  By (20.1), Lemma 20.18, and `|n^{½−ρ_1}| = 1` — which is
(X19)(V1), the on-line-ness of `ρ_1` —

    t_n(E) = t_n(E_0) − 2rG_σ|Φ_g(ρ_1)|\cos(γ_1\log n + ψ) + θ_n ,\qquad
    |θ_n| ≤ 2rκ\,Λ_σ\,G_σ\,n^{½} ,

where `ψ = ψ(φ)` runs over all of `R/2πZ` as `φ` does (Lemma 20.18(ii)), the bound on
`θ_n` collecting the other zeros (Lemma 20.18(iv), `|n^{½−ρ}| ≤ n^{½}` by (E2)) and the
two polar leaks (Lemma 20.18(iii), absorbed into `Λ_σ` by enlarging the constant).
Choose, in this order,

    φ \text{ with } \cosψ ≤ 0 ;\qquad r := \frac{Φ_g(0)\,ε}{4κ\,Λ_σ\,G_σ} ;\qquad
    t := \frac{4rG_σ|Φ_g(ρ_1)| + 4rκΛ_σG_σ}{Φ_g(0)\,b_J} .

At `n = 1` the cosine term is `≥ 0`, so
`t_1(E) ≥ Φ_g(0)ε − 2rκΛ_σG_σ = Φ_g(0)ε/2 > 0`.  For `n ≥ 2`, using `n^{½} ≥ 1`,

    t_n(E) ≥ \tfrac12Φ_g(0)tb_J\,n^{½} − 2rG_σ|Φ_g(ρ_1)| − 2rκΛ_σG_σ\,n^{½}
          ≥ n^{½}\Big(\tfrac12Φ_g(0)tb_J − 2rG_σ|Φ_g(ρ_1)| − 2rκΛ_σG_σ\Big) = 0

by the choice of `t`.  So `E ∈ B4^g` with `\deg E = ε = 1` and
`|Φ_E(ρ_1)| = rG_σ(1+o(1))`, where

    r\,G_σ = \frac{Φ_g(0)\,ε}{4κ\,Λ_σ} \;\xrightarrow[\;σ→∞\;]{}\; +∞ ,\qquad
    Λ_σ ≤ Ce^{−23σ²} .

Finally `I_∞(E,X) = −2\mathrm{Re}\big(Φ_E(ρ_1)Φ_X(1−ρ_1)\big) + O(1)`, the `O(1)` being
the polar and leakage terms of `X` against `E_0` and `rF_σ^{(φ)}`, bounded by
`κ'(\deg E_0 + rG_σΛ_σ) = O(1)` by the choice of `r`; in the one case where the `E_0`
term is not `O(1)`, namely `Φ_X(1) ≠ Φ_X(0)`, fix `σ` and let `t → ∞` instead — the
traces `t_n(E)` are increasing in `t` and `\deg E` is unchanged, so the supremum is
already `+∞`.  The admissible set of `ψ` is a closed arc of length `π`, and every closed
arc of length `π` contains a point at which `|\mathrm{Re}(e^{iψ}w)| = |w|` for a
prescribed `w ≠ 0` (the two such points are antipodal, so one lies in any closed
half-circle).  Choosing `ψ` there,

    \frac{|I_∞(E,X)|}{\deg E} ≥ rG_σ|Φ_X(ρ_1)| − O(1)\;\xrightarrow[\;σ→∞\;]{}\;+∞ .  ∎
`PROVED` given (X19)

Consequently §19's (T1_cone)+(T2_cone) test does not apply to `B4^g` — both hypotheses fail — and
no conclusion may be drawn from `B4`'s passing it.  On `B4^{g,0}` the status of (T2_cone) is
`OPEN`, the counterexample needing `a < 0`; nothing below depends on it, because
Theorem 20.17 does not use (T2_cone).

### 20.4 `(G⁺)`, and the clause `(b′)_{B4}` under RH

**Definition 20.20 (the condition `(G⁺)`).**  An admissible `g` satisfies `(G⁺)` if

    W^{\mathrm{abs}}(g) := Σ_ρ|Φ_g(ρ)|\,|Φ_g(1−ρ)| \;≤\; 2\,Φ_g(0)\,Φ_g(1) .

This is unconditional and zero-free in content:
`2Φ_g(0)Φ_g(1) − Σ_ρΦ_g(ρ)Φ_g(1−ρ) = I_∞(g,g)` by (11.6), which by Theorem 11.5 is the
arithmetic bracket `PRIME − ARCH` of the even part of `g⋆g^∨`; and under RH
`W^{\mathrm{abs}}(g) = Σ_ρ|Φ_g(ρ)|² = W(g)`, the form Theorem 20.22 consumes.

**Lemma 20.21 (`(G⁺)` is satisfiable, unconditionally; `PROVED`).**  Let `h` be
admissible in the sense of Definition 20.10 (Lemma 20.1 produces one) and put

    g_λ := K + λ\,h ,\qquad 0 < λ ≤ λ_0 := \big(2\,W^{\mathrm{abs}}(h)\big)^{-1/2} .

Then `g_λ` is admissible and satisfies `(G⁺)`, unconditionally.  Explicitly
`Φ_{g_λ}(ρ) = λΦ_h(ρ)`, `Φ_{g_λ}(0) = Φ_{g_λ}(1) = ½ + λΦ_h(0) > 0`, and

    W^{\mathrm{abs}}(g_λ) = λ²W^{\mathrm{abs}}(h) ≤ \tfrac12 ≤ 2\,Φ_{g_λ}(0)Φ_{g_λ}(1) .

*Proof.*  `K > 0` (Theorem 11.7(i)) and `h ≥ 0`, so `g_λ ≥ 0`, `g_λ ≢ 0`; `K` and `h`
are even, so `g_λ` is even; `K ∈ D^W` (super-exponential decay) and
`h ∈ C_c^∞ ⊂ D^W`, so `g_λ ∈ D^W`.  *Admissibility:* `Φ_K(1−ρ) = ξ(1−ρ) = 0`, so
`Φ_{g_λ}(1−ρ) = λΦ_h(1−ρ) ≠ 0` at every zero, and it inherits `h`'s rapid decay in
`|γ_ρ|` — the only property of the Baire choice used anywhere downstream (the last line
of Theorem 20.5's proof; Lemma 20.13's convergence).  Also
`Φ_{g_λ}(0) = Φ_K(0)+λΦ_h(0) = ½+λΦ_h(0) > 0`, and likewise at `1`.  *`(G⁺)`:* the
displayed identity is immediate from `Φ_{g_λ}(ρ) = λΦ_h(ρ)`, and
`W^{\mathrm{abs}}(h) < ∞` by (11.2), (E3d) and the rapid decay of `Φ_h`; then
`λ²W^{\mathrm{abs}}(h) ≤ ½` by the choice of `λ_0`, while
`2Φ_{g_λ}(0)Φ_{g_λ}(1) ≥ 2·(½)² = ½`.  Nothing in the argument mentions the location of
a zero beyond `Φ_K(ρ) = 0`, which is the definition of `K`.  ∎  `PROVED`

Equivalently `I_∞(g_λ,g_λ) = ½ + λ\deg h + λ²I_∞(h,h) > 0` for small `λ`, by
`I_∞(K,K) = ½`, `I_∞(K,h) = ½\deg h` (Theorem 11.8(i)) and `\deg h > 0`
(Theorem 11.13(i)).  In one sentence: the canonical class is invisible to the zero side
(`Φ_K(ρ) = 0`) and dominant on the polar side (`Φ_K(0) = Φ_K(1) = ½`), so adding a small
multiple of an admissible `h` to `K` buys the Baire condition at a cost of `O(λ)` on the
polar side and `O(λ²)` on the zero side — and `(G⁺)` is precisely the comparison of the
two sides.  `K` alone cannot be used (Proposition 20.11).

**Theorem 20.22 (`(b′)_{B4}` for `h⁰_{RR}^{+}`; `PROVED` under RH, with `(G⁺)`;
`χ = 0`).**  Let `χ = 0`, `R(E) := ½I_∞(E,E) − ¼\deg E`, and
`h⁰_{RR}^{+}(E) := \max(R(E),0)·1_{\{\deg E>0\}}`.  Assume RH and let `g` be any
admissible test class satisfying `(G⁺)` — one exists unconditionally, e.g.
`g = g_λ = K+λh` of Lemma 20.21.  Then for every `E ∈ D^W` with

    R(E) > 0 \quad\text{and}\quad \deg E > 0 ,

one has `a = Φ_E(1) > 0`, `b = Φ_E(0) > 0`, and

    t_n(E) \;≥\; 2\sqrt{ab\,Φ_g(0)Φ_g(1)} \;−\; \sqrt{W(E)\,W(g)} \;≥\; 0
    \qquad\text{for every } n ≥ 1 ,

i.e. `E ∈ B4^{g,0}`.  Hence `h⁰_{RR}^{+}` satisfies (a), `(b′)_{B4}` and (c) — all
three — under RH.

*Proof.*  Under RH, `W(E) = Σ_ρ|Φ_E(ρ)|² ≥ 0` (`E` real, `1−ρ = \barρ`), and
`I_∞(E,E) = 2ab − W(E) ≤ 2ab`.  If `ab ≤ 0` then `R(E) ≤ ½·0 − ¼\deg E < 0`; so
`R(E) > 0` forces `ab > 0`, and with `\deg E = a+b > 0` this gives `a,b > 0`.  Next, in
(20.1) the polar part is, by AM–GM and **uniformly in `n`**,

    n^{½}Φ_g(1)b + n^{−½}Φ_g(0)a \;≥\; 2\sqrt{ab\,Φ_g(0)Φ_g(1)} ,

and the zero part is bounded, using `|n^{½−ρ}| = 1` (RH) and Cauchy–Schwarz, by

    \Big|Σ_ρΦ_E(ρ)Φ_g(1−ρ)n^{½−ρ}\Big| ≤ Σ_ρ|Φ_E(ρ)||Φ_g(ρ)| ≤ \sqrt{W(E)W(g)} .

Now `R(E) > 0` reads `W(E) < 2ab − ½\deg E < 2ab`, so with `(G⁺)`, i.e.
`W(g) ≤ 2Φ_g(0)Φ_g(1)`,

    W(E)W(g) < 2ab·2Φ_g(0)Φ_g(1) = \big(2\sqrt{ab\,Φ_g(0)Φ_g(1)}\big)^2 ,

which is the claim.  Clauses (a) and (c) for `h⁰_{RR}^{+}` are unconditional and are
not re-proved here: (a) is immediate from the definition, and (c) with `χ = 0` is the
Riemann–Roch inequality that defines the candidate `h⁰_{RR}^{+}`.  ∎
`PROVED` under RH

RH is used exactly twice: `W(E) = Σ_ρ|Φ_E(ρ)|² ≥ 0` (once to force `a,b > 0`, once in
the final inequality) and `|n^{½−ρ}| = 1`.  Those two, and only those two, would have to
be replaced by an unconditional argument.  Read against the refutation recorded at
Theorem 12.3: the *effective* version of the same statement for the same
`h⁰_{RR}^{+}` is **false**, unconditionally, with a certified degree-`400` witness,
while the *trace* version is **true under RH**.  The two clauses differ only in the cone
from which the representative `E'` is drawn, and Remark 20.12 says why they are
incomparable.

**Theorem 20.23 (`(b′)_{B4}` is equivalent to RH; `PROVED` + `RESTATEMENT`).**

    \text{RH} \quad⟺\quad \exists\ \text{admissible } g\ \exists\,h⁰ :\
    \text{(a)},\ (b′)_{B4^{g,0}},\ \text{(c)} ,

and more precisely: `⟸` holds for **every** admissible `g`, while `⟹` holds for every
admissible `g` satisfying `(G⁺)`, of which Lemma 20.21 exhibits one unconditionally.
Hence also: **RH ⟺ there exists `h⁰` with (a), `(b′)_{B4}`, (c)**.

*Proof.*  `⟸` is Theorem 20.17, proved for an arbitrary admissible `g` and using only
(T1′).  `⟹` is Theorem 20.22 with `h⁰ = h⁰_{RR}^{+}`, `χ = 0`, `g = g_λ`.  ∎  `PROVED`;
and, the content being an equivalence with RH, also `RESTATEMENT`.

This is an equivalence, not a proof.  It says the sign problem has been transported,
without loss and without gain, onto the single clause `(b′)_{B4}`; proving that clause
unconditionally *is* RH.  What it buys over the state left by §19 is that the target
clause is now true rather than false, is not refutable, and is supported by a transfer
theorem all of whose other inputs are theorems.

**Theorem 20.24 (the falsifier `Ξ_a`; `PROVED`).**  Fix `0 < a < ½`, let `P = \{−a,a,1−a,1+a\}`,
and define `t^{(a)}_n(E) := I_∞^{(a)}(E,τ_{\log n}g_a)` and
`B4_a := \{E : t^{(a)}_n(E) ≥ 0\ ∀n ≥ 1\}` verbatim, with `g_a` the Baire choice for
`Ξ_a`.  Then (T1′) holds for `Ξ_a`, Theorem 20.17 transports verbatim, its conclusion
is **false**, and consequently **there is no `h⁰` satisfying (a), `(b′)_{B4_a}`, (c) for
`Ξ_a`**.  In particular `h⁰_{RR}^{+,Ξ_a}`, which satisfies (a) and (c), fails
`(b′)_{B4_a}`.

*Proof.*  Lemma 20.13 transports with
`D_E(w) = Σ_{p∈P}Φ_E(p)Φ_{g_a}(1−p)ζ(w+p−½) − Σ_ρc_ρζ(w+ρ−½)`: four real poles
`w = 3/2−p`, i.e. `3/2±a` and `½±a`, and non-real poles at `3/2−ρ`, non-real because
`Ξ_a` has no real zero (Lemma 12.4A(v)).  If `E` is `Ξ_a`-primitive, i.e. `Φ_E(p) = 0`
for all four `p ∈ P`, then `D_E` has **no real pole at all**, so by (X20) its abscissa
cannot be a singular point unless there is no pole at all, i.e. `c_ρ = 0` for every `ρ`,
i.e. `E ∈ 𝓝_∞^{(a)}`; this is (T1′) for `Ξ_a`.  Steps 1–3 of Theorem 20.17 use only
(T1′), linearity of the traces, `𝓝_∞^{(a)}` being the radical, and (c), so the transfer
theorem transports verbatim and yields `I_∞^{(a)}(F,F) ≤ 0` for every `Ξ_a`-primitive
`F ∈ C_c^∞`.  That conclusion is false: Proposition 12.4B exhibits a `Ξ_a`-primitive
`F_+` with `I_∞^{(a)}(F_+,F_+) > 0`.  Hence no `h⁰` can satisfy (a), `(b′)_{B4_a}`, (c)
simultaneously.  ∎  `PROVED`

What does **not** transport is Theorem 20.14: for `ξ` the two polar poles `½` and `3/2`
strictly bracket every zero-pole, which is what makes its cascade close, whereas for
`Ξ_a` the four real polar poles leave at least one below the remaining zero-poles and
the cascade never closes.  That difference is genuine, and it is not load-bearing —
Theorem 20.17 uses only (T1′), which `Ξ_a` satisfies.  The falsifier's separating step
is identified in §20.7.

**Theorem 20.25 (Dedekind transport is conditional; `PROVED`).**  Every statement of
this section holds verbatim for `ξ_K` — with `P = \{0,1\}`, `\deg_K`, and the traces
indexed by the rational integers or by the norms of integral ideals, either index set
giving a Dirichlet series with a real pole — **granted one zero-location input, that
`ξ_K` has no real zero in `(0,1)`**; without it the proof of Theorem 20.14(ii) breaks at
precisely one point.

*Proof.*  Read the proofs of Lemma 20.13 and Theorem 20.14 with `ξ_K` in place of `ξ`;
the only step that mentions the location of a zero is "`γ_ρ ≠ 0`", which is used to make
every zero-pole non-real.  A real zero `β_0 ∈ (0,1)` of `ξ_K` puts a **real** pole at
`3/2−β_0 ∈ (½,3/2)`, which is exactly where the singularity supplied by (X20) is then
permitted to sit, and the contradiction of Theorem 20.14(ii) fails.  Granted no real
zero, Theorems 20.14, 20.15 and 20.17 hold verbatim.  ∎  `PROVED`

For `ξ` the hypothesis is classical (Lemma 13.5b); for `Ξ_a` it is Lemma 12.4A(v); for
`ζ_K` it is not known, a Siegel zero not being excluded unconditionally.  The mechanism
of Theorem 20.15 is therefore *exactly* "no real zeros", and nothing else.  This does
not put GRH within reach: Theorem 20.17 for `ζ_K` would need `(b′)_{B4}` for `ζ_K`,
which is no more available there than here.

### 20.5 Index-locality

**Proposition 20.26 (eventual positivity, and the finite head; `PROVED` (i),(ii)
unconditionally, `PROVED` (iii),(iv) under RH).**  Let `E ∈ D^W` be real,
`a := Φ_E(1)`, `b := Φ_E(0)`, `c_ρ := Φ_E(ρ)Φ_g(1−ρ)`, `S(E) := Σ_ρ|c_ρ| < ∞`, and

    β_{\min}(E) := \inf\{\mathrm{Re}\,ρ : Φ_E(ρ) ≠ 0\} ∈ [0,1]\qquad(\inf ∅ := +∞) .

 (i) *(unconditional, non-effective)* if `b > 0` then `t_n(E) → +∞`, so there is a
     finite `N(E)` with `t_n(E) > 0` for every `n ≥ N(E)`;
 (ii) *(unconditional, effective when `β := β_{\min}(E) > 0`)* if `b > 0` and `β > 0`
      one may take

          N(E) = \max\Big\{\Big(\frac{2S(E)}{b\,Φ_g(1)}\Big)^{1/β},\;
                           \frac{2|a|\,Φ_g(0)}{b\,Φ_g(1)}\Big\} ;

 (iii) *(the clause is finite per class)* under RH, for every `E` with `R(E) > 0` and
      `\deg E > 0` the statement `E ∈ B4` is the **finite** statement
      "`t_n(E) ≥ 0` for `1 ≤ n < N(E)`", with

          N(E) \;≤\; \frac{4\,W(E)\,W(g)}{b²\,Φ_g(1)²} ;

 (iv) *(uniform per degree slice, under RH, `g` even and `(G⁺)`)* on
      `\{E : R(E) > 0,\ 0 < \deg E ≤ d\}` one has `a,b > ¼` and `W(E) < 2ab ≤ d²/2`,
      hence `N(E) ≤ 64\,d^2` uniformly on the slice.

*Proof.*  (i),(ii): (20.1) gives
`t_n(E) ≥ bΦ_g(1)n^{½} − |a|Φ_g(0)n^{−½} − Σ_ρ|c_ρ|n^{½−\mathrm{Re}ρ}`, and
`n^{½−\mathrm{Re}ρ} = n^{½}n^{−\mathrm{Re}ρ}`; factor out `n^{½}`.  Each term
`n^{−\mathrm{Re}ρ} → 0` by (E2) and all are dominated by the summable `|c_ρ|`, so
`Σ_ρ|c_ρ|n^{−\mathrm{Re}ρ} → 0` by dominated convergence, which needs only
`\mathrm{Re}\,ρ > 0` and `S(E) < ∞` (Lemma 20.13); hence the bracket is eventually
positive.  With `β > 0`, `Σ|c_ρ|n^{−\mathrm{Re}ρ} ≤ S(E)n^{−β}`, and
`S(E)n^{−β} ≤ ½bΦ_g(1)` is the first displayed condition, while
`|a|Φ_g(0)n^{−½} ≤ ½bΦ_g(1)n^{½}` is implied by the second.
(iii): under RH, `R(E) > 0` and `\deg E > 0` force `a,b > 0` (Theorem 20.22) and every
zero is on the line, so `β_{\min}(E) = ½` whenever `Φ_E` does not vanish identically on
the zeros; then `N(E) ≤ (2S/(bΦ_g(1)))²` and
`S(E) = Σ_ρ|Φ_E(ρ)||Φ_g(ρ)| ≤ \sqrt{W(E)}\sqrt{W(g)}` by Cauchy–Schwarz.
(iv): under RH, `W(E) ≥ 0` and `R(E) > 0` give `2ab > W(E)+½\deg E > ½(a+b) ≥ ½a`, so
`4ab > a` and `b > ¼`; symmetrically `a > ¼`.  Also
`W(E) < 2ab ≤ ½(a+b)² = ½(\deg E)² ≤ d²/2`.  With `g` even, `Φ_g(0) = Φ_g(1) =: p_0`,
and `(G⁺)` gives `W(g) ≤ 2p_0²`; substituting,
`N(E) ≤ 4·(d²/2)·2p_0²/((¼)²p_0²) = 64d²`.  ∎  `PROVED`

Two riders.  First, off RH the clause is *not* known to be finite, for exactly two
reasons: `β_{\min}(E)` may be `0`, and `b > 0` may fail (off RH, `W(E)` may be negative,
so `R(E) > 0` gives no sign for `a` or `b`).  Second — and this is a recorded warning —
**unconditional uniformity of `N` on a degree slice is a quasi-RH zero-free-strip
statement**: it requires `\inf_ρ\mathrm{Re}\,ρ > 0`, which no classical zero-free region
supplies.  It is not a target.

For `Ξ_a` the eventual half of Proposition 20.26 also holds: the leading polar exponent
is `½+a` and the zero exponents `½−\mathrm{Re}\,ρ` with `\mathrm{Re}\,ρ ∈ (−a,1+a)` lie
strictly below it, so `t^{(a)}_n(E) > 0` for all large `n` when `Φ_E(−a) > 0`.  The
violation of `(b′)_{B4_a}` guaranteed by Theorem 20.24 therefore sits at a **fixed
finite index**, not in the tail: with `E_r := rF_+ + K_a` one has `R_a(E_r) → +∞` and
`\deg_a E_r > 0` independently of the sign of `r`, while `F_+ ∉ 𝓝_∞^{(a)}` gives some
`m` with `t^{(a)}_m(F_+) ≠ 0`, and
`t^{(a)}_m(E_r) = t^{(a)}_m(K_a) + r\,t^{(a)}_m(F_+) < 0` for the right sign of `r` and
`|r|` large.

### 20.6 The fixed index, and the final form

Write `S_0 := \{E ∈ D^W \text{ real} : \deg E > 0,\ R(E) = ½I_∞(E,E) − ¼\deg E > 0\}`
and, for `m ≥ 1`, let `(P_m)` be the assertion `t_m(E) ≥ 0` for all `E ∈ S_0`.  The
question of §20.5 is whether the clause decomposes by index — whether some single
`(P_m)` is unconditionally provable.  It is not: every one of them is RH.

**Lemma 20.27 (the one-index witness; `PROVED`, unconditional).**  Let
`F ∈ C_c^∞(R)` be real and primitive with `q := I_∞(F,F) > 0`, and let `g` be
admissible.  For `t ∈ R` put `E_t := tF + K`.  Then, identically in `t`,

    \deg E_t = 1 ,\qquad I_∞(E_t,E_t) = t²q + \tfrac12 ,\qquad
    R(E_t) = \tfrac12t²q > 0 \quad(t ≠ 0) ,

so `E_t ∈ S_0` for every `t ≠ 0`; and for every `m ≥ 1`

    t_m(E_t) = t_m(K) + t\,t_m(F) ,\qquad
    t_m(K) = \tfrac12\big(Φ_g(1)m^{½}+Φ_g(0)m^{−½}\big) = Φ_g(0)\cosh(\tfrac12\log m) > 0 ,

the last equality for even `g`.  Consequently, if `t_m(F) ≠ 0`, then with
`\mathrm{sign}(t) = −\mathrm{sign}(t_m(F))` and

    |t| > t_*(m) := \frac{Φ_g(0)\cosh(\tfrac12\log m)}{|t_m(F)|}

one has `E_t ∈ S_0` and `t_m(E_t) < 0`: **`(P_m)` fails.**  The threshold `t_*(m)` is
minimal at `m = 1`.

*Proof.*  `\deg K = 1`, `\deg F = 0`, `I_∞(F,K) = ½\deg F = 0` (Theorem 11.8(i)),
`I_∞(K,K) = ½` (Theorem 11.8(ii)), so
`I_∞(E_t,E_t) = t²q + 2t·0 + ½` and `R(E_t) = ½(½+t²q) − ¼ = ½t²q`.  For the traces,
`Φ_F(0) = Φ_F(1) = 0` and `Φ_K(ρ) = ξ(ρ) = 0`, so in (20.1) `K` contributes only the
polar part and `F` only the zero part; the displayed value of `t_m(K)` is
`Φ_K(0) = Φ_K(1) = ½` inserted there, and for even `g`,
`Φ_g(0) = Φ_g(1)`.  Minimality of `t_*(m)` at `m = 1` is minimality of
`\cosh(½\log m)`, attained at `m = 1`, which is Lemma 20.34(iv) below.  ∎  `PROVED`

**Lemma 20.28 (index selection; `PROVED`, unconditional).**  If RH is false, then for
**every** fixed `m ≥ 1` and every admissible `g` there is a real primitive
`F ∈ C_c^∞(R)` with `I_∞(F,F) > 0` **and** `t_m(F) ≠ 0`.

*Proof.*  By Paper 45 Theorem 10.4, RH false gives a nonzero real primitive
`F_0 ∈ C_c^∞(R)` with `Σ_ρΦ_{F_0}(ρ)Φ_{F_0}(1−ρ) < 0`, i.e. `q_0 := I_∞(F_0,F_0) > 0`
(Theorem 11.5, the polar packet vanishing on a primitive class).  By Lemma 20.6 (second
map, whose Langer / Riemann–von Mangoldt proof uses only `Φ_g(ρ) ≠ 0`, hence applies to
`g = g_λ`, where `Φ_{g_λ}(ρ) = λΦ_h(ρ) ≠ 0`) there is a real primitive
`F_1 ∈ C_c^∞(R)` with `t_m(F_1) ≠ 0`.  If `t_m(F_0) ≠ 0`, take `F = F_0`.  Otherwise put
`F := F_0 + εF_1`: then `t_m(F) = ε\,t_m(F_1) ≠ 0` for `ε ≠ 0`, and
`I_∞(F,F) = q_0 + 2εI_∞(F_0,F_1) + ε²I_∞(F_1,F_1) > 0` for `|ε|` small, being a real
quadratic in `ε` positive at `ε = 0`.  Both classes are primitive and compactly
supported, hence so is `F`.  (Nothing in Lemma 20.27 or Theorem 20.29 uses evenness of
`F`; only `g` is required even, and `K` is even automatically.)  ∎  `PROVED`

**Theorem 20.29 (`(P_m) ⟺ RH` at every fixed index; `PROVED`).**  Let `g` be
admissible.

 (i) *(unconditional)* if `(P_m)` holds for **one** `m ≥ 1`, then RH;
 (ii) if RH holds and `g` satisfies `(G⁺)` — available unconditionally for
      `g = g_λ = K+λh`, `0 < λ ≤ (2W^{\mathrm{abs}}(h))^{−1/2}` (Lemma 20.21) — then
      `(P_m)` holds for **every** `m`;
 (iii) hence, for every admissible `g` satisfying `(G⁺)` and every fixed `m ≥ 1`,
      `(P_m) ⟺ RH`; in particular `(P_1) ⟺ RH`.  **A single inequality at a single
      index carries the whole of RH: the clause `(b′)_{B4}` does not decompose by
      index.**

*Proof.*  (i) Contrapositive.  Suppose RH is false.  By Lemma 20.28 pick `F` primitive,
compactly supported, real, with `q = I_∞(F,F) > 0` and `t_m(F) ≠ 0`; by Lemma 20.27 pick
`t` with `\mathrm{sign}(t) = −\mathrm{sign}(t_m(F))` and `|t| > t_*(m)`.  Then
`E_t ∈ S_0` and `t_m(E_t) < 0`, so `(P_m)` fails.  (ii) is Theorem 20.22, whose
conclusion is `t_n(E) ≥ 0` for all `n`, in particular for `n = m`.  (iii) combines them.
∎  `PROVED`

**Restatement 20.30 (the final form of the trace-cone route; `PROVED` +
`RESTATEMENT`).**  For `g_λ = K + λh` of Lemma 20.21,

    \mathrm{RH} \quad⟺\quad I_∞(E,\,g_λ) ≥ 0 \quad\text{for every real } E ∈ D^W
    \text{ with } \deg E > 0 \text{ and } \tfrac12I_∞(E,E) > \tfrac14\deg E .

*Proof.*  This is Theorem 20.29(iii) at `m = 1`, since `t_1(E) = I_∞(E,g_λ)` and `S_0`
is exactly the displayed set.  ∎  `PROVED` + `RESTATEMENT`

One bilinear inequality, one test class, no index set, no cone, no `h⁰`, no transfer
theorem.  It is a `RESTATEMENT`: the `⟸` direction is Theorem 20.22 and uses RH twice.
It must not be read as progress towards a proof.  Its value is diagnostic — it shows
that the finiteness results of Proposition 20.26 localise the *positivity* and not the
*difficulty*.  Written out with `I_∞(E,g_λ) = ½\deg E + λI_∞(E,h)`, `(P_1)` reads

    I_∞(E,h) \;≥\; −\frac{\deg E}{2λ}\qquad\text{for all } E ∈ S_0 ,

a bound of the shape of Theorem 11.14 but on `S_0`, with the large constant `1/(2λ)`.
The constant is irrelevant: the witness `E_t` is linear in `t` at frozen degree.

**Theorem 20.31 (bounded density on `S_0` ⟺ RH; `PROVED`).**  For real `F ∈ D^W` put

    C^{S_0}_F := \sup\Big\{\frac{|I_∞(E,F)|}{\deg E} : E ∈ S_0\Big\} ∈ [0,∞] .

 (i) *(unconditional)* if `I_∞(F,F) > 0` then `C^{S_0}_F = +∞`;
 (ii) *(under RH)* for **every** `F ∈ D^W`,
      `C^{S_0}_F ≤ \max(|Φ_F(0)|,|Φ_F(1)|) + \sqrt{W^{\mathrm{abs}}(F)/2} < ∞`;
 (iii) hence **`S_0` has bounded density in every direction if and only if RH**, and the
      failure, when it occurs, is already visible on the degree-`1` slice and along a
      single ray.

*Proof.*  (i) `E_t = tF+K` has `\deg E_t = 1` and `R(E_t) = ½t²I_∞(F,F) > 0`, so
`E_t ∈ S_0`, while `I_∞(E_t,F) = tI_∞(F,F) + I_∞(K,F) = tI_∞(F,F)` by Theorem 11.8(i)
and `\deg F = 0`, which is unbounded in `t`.  (ii) Under RH and `E ∈ S_0`:
`W(E) = Σ_ρ|Φ_E(ρ)|² ≥ 0`, so `R(E) > 0` gives `a,b > 0` and
`W(E) < 2ab ≤ ½(\deg E)²` (Theorem 20.22's first paragraph and AM–GM); then by
Theorem 11.5 and Cauchy–Schwarz

    |I_∞(E,F)| ≤ |Φ_E(0)Φ_F(1)+Φ_E(1)Φ_F(0)| + \sqrt{W(E)W^{\mathrm{abs}}(F)}
      ≤ \max(|Φ_F(0)|,|Φ_F(1)|)(a+b) + \deg E\sqrt{W^{\mathrm{abs}}(F)/2} .

(iii) (i) with Paper 45 Theorem 10.4: RH false produces a primitive `F` with
`I_∞(F,F) > 0`, so some direction is unbounded; RH true gives (ii).  ∎  `PROVED`

So on the effective cone the density is bounded and the size of the constant is the
issue (and, by the refutation recorded at Theorem 12.3, it is too small); on
`S_0` the density is bounded **iff** RH, and no finite constant whatever — however
large — makes `(P_1)` unconditional.

**Corollary 20.32 (no unconditional substitute for `W ≥ 0`; `PROVED`).**  There is
**no** function `Ψ : R³ → R` with

    W(E) \;≥\; −Ψ\big(Φ_E(1),\,Φ_E(0),\,\deg E\big)\qquad\text{for all } E ∈ S_0 ,

unless RH holds; equivalently, the existence of such a `Ψ` is itself equivalent to RH.

*Proof.*  Suppose RH fails and take `F`, `q = I_∞(F,F) > 0`, `E_t = tF+K` as in
Lemma 20.27.  Since `Φ_K(ρ) = ξ(ρ) = 0`, the zero data of `E_t` is
`Φ_{E_t}(ρ) = tΦ_F(ρ)`, so `W(E_t) = t²W_F = −t²q → −∞` as `|t| → ∞`, while
simultaneously `a = Φ_{E_t}(1) = ½`, `b = Φ_{E_t}(0) = ½` and `\deg E_t = 1` are
**constant in `t`** (`F` being primitive), and `E_t ∈ S_0` for every `t ≠ 0`.  The three
arguments of `Ψ` are frozen while `W → −∞`, so no finite `Ψ` exists.  Conversely, under
RH, `W(E) = Σ_ρ|Φ_E(ρ)|² ≥ 0` and `Ψ ≡ 0` works.  ∎  `PROVED`

**Corollary 20.33 (the sparse cone is not a weakening; `PROVED`).**  The cone
`\{E : t_{2^k}(E) ≥ 0 \text{ for all } k ≥ 0\}` satisfies (T1′) by the argument of
Theorem 20.14 run on the generating function
`Φ_g(1)b/(1−2^{½−w}) + Φ_g(0)a/(1−2^{−½−w}) − Σ_ρc_ρ/(1−2^{½−ρ−w})`, whose real poles
are exactly the two polar ones; and it is larger than `B4^g`, hence a formally weaker
clause.  It is nevertheless **not** a weakening of the problem: the single index
`k = 0` of the associated positivity clause is already equivalent to RH.

*Proof.*  The first assertion is Theorem 20.14's cascade applied to the displayed
function, whose zero-poles `w = ½−ρ+2πim/\log 2` are non-real unless
`γ_ρ ∈ (2π/\log 2)Z`; the inclusion is immediate.  For the second, the clause at
`k = 0` is `(P_1)`, and `(P_1) ⟺ RH` by Theorem 20.29(iii).  ∎  `PROVED`

### 20.7 What the separator is not, and what it is

An earlier reading of the `ξ`/`Ξ_a` separation attributed it to the arity of the polar
block — two polar exponents for `ξ` against four for `Ξ_a`, with the claim that a
four-point set has no AM–GM floor.  That reading is false, and the following elementary
lemma refutes it.

**Lemma 20.34 (the polar floor, for every symmetric polar set; `PROVED`).**  Let
`P ⊂ R` be finite with `P = 1−P`, let `C_p > 0` for `p ∈ P`, and put
`A(x) := Σ_{p∈P}C_p x^{½−p}` for `x > 0`.  Then:

 (i) *(weighted AM–GM, any `\#P`)* `A(x) ≥ \#P·\big(∏_{p∈P}C_p\big)^{1/\#P}` for every
     `x > 0` — a strictly positive floor, **uniform in `x`**;
 (ii) *(pairwise)* `A(x) ≥ Σ_{\{p,1−p\},\,p≠½}2\sqrt{C_pC_{1−p}}\ (+\,C_{½}` if
      `½ ∈ P)`, again uniform in `x`, and this bound dominates (i);
 (iii) *(the two-point case)* if `P = \{½−θ,½+θ\}` then
       `\inf_xA = 2\sqrt{C_{½−θ}C_{½+θ}}` **exactly**, attained at
       `x = (C_{½−θ}/C_{½+θ})^{1/2θ}`;
 (iv) *(pair-symmetric coefficients)* if `C_{1−p} = C_p` for all `p` — the case for
      every even admissible `g` and every `E` with `Φ_E(1−p) = Φ_E(p)`, in particular
      `E = K` and `E = K_a` — then
      `A(x) = Σ_{\{p,1−p\}}2C_p\cosh((½−p)\log x)` is a sum of even convex functions of
      `\log x`, so `\inf_{x>0}A = A(1) = Σ_pC_p`, **attained at `x = 1`**.

*Proof.*  (i) Weighted AM–GM with equal weights `1/\#P` on the positive numbers
`C_px^{½−p}`:
`\frac1{\#P}ΣC_px^{½−p} ≥ (∏C_px^{½−p})^{1/\#P} = (∏C_p)^{1/\#P}x^{(Σ(½−p))/\#P}
= (∏C_p)^{1/\#P}`, using `Σ_{p∈P}(½−p) = 0`, which holds because `p ↦ 1−p` is an
involution of `P` pairing `½−p` with `−(½−p)` (its only possible fixed point is `½`,
whose term is `0`).  (ii) `C_px^{½−p} + C_{1−p}x^{−(½−p)} ≥ 2\sqrt{C_pC_{1−p}}`
termwise, and `\inf(f+g) ≥ \inf f + \inf g`; and
`Σ2\sqrt{C_pC_{1−p}} ≥ \#P(∏C_p)^{1/\#P}` by AM–GM on the `\#P/2` pairwise geometric
means.  (iii) is (ii) with one pair, with equality at the stated `x`.  (iv) `\cosh` is
even and convex in its argument and minimal at `0`.  ∎  `PROVED`

So **every** symmetric polar set has a uniform positive floor of exactly the same AM–GM
type, and in the case that actually occurs — `g` even, `Φ_{K_a}(1−p) = Ξ_a(1−p) =
Ξ_a(p)` — the four-point floor is not merely uniform but attained at `n = 1`, i.e. as
good as the two-point floor in every respect.  The polar part of `t^{(a)}_n(K_a)` is
minimal at `n = 1` and grows like `n^{½+a}` thereafter.  The two-versus-four distinction
does one thing only, and it is not this: it is what makes Theorem 20.14's Landau cascade
close, since the two real poles `½` and `3/2` strictly bracket every zero-pole.  That is
a statement about the Dirichlet series over all `n`, not about a fixed index, and it
concerns (T1′), which holds for `Ξ_a` anyway.

**Theorem 20.35 (the true separating step; `PROVED`).**  The proof of Theorem 20.22 has
three ingredients: the polar floor `≥ 2\sqrt{ab\,Φ_g(0)Φ_g(1)}` (Lemma 20.34(iii)); the
zero bound `|Z_n| ≤ \sqrt{W(E)W(g)}`; and the gate `R(E) > 0 ⟹ W(E) < 2ab`.
Transported to `Ξ_a`:

 (i) **the polar floor transports** (Lemma 20.34(i),(ii),(iv)), and for the falsifier
     family it is attained at `n = 1` and independent of `r`;
 (ii) **the zero bound does not**, for two independent reasons: the zeros of `Ξ_a` are
      `ρ ± a`, so `|n^{½−(ρ±a)}| = n^{∓a}` is **unbounded** in `n`; and
      `W_a(E) = Σ_ρΦ_E(ρ)Φ_E(1−ρ)` is **not** `Σ_ρ|Φ_E(ρ)|²`, since `1−ρ ≠ \barρ` for a
      zero off `\mathrm{Re}\,s = ½`, so Cauchy–Schwarz against `W_a(E)` is unavailable;
 (iii) **the gate transports but is vacuous:** `R_a(E_r) > 0` holds for **every** `r`,
      precisely because `W_a` is indefinite, so it imposes no bound whatever on the zero
      data `(Φ_{E_r}(ρ))_ρ = r(Φ_{F_+}(ρ))_ρ`.

Hence the separating step is (ii)+(iii) — *"`R(E) > 0` bounds the zero energy"* — and not
the arity of the polar block.

*Proof.*  (i) is Lemma 20.34 applied to `P = \{−a,a,1−a,1+a\}`, which satisfies
`P = 1−P`, with the pair-symmetry of clause (iv) supplied by evenness of `g_a` and
`Ξ_a(1−p) = Ξ_a(p)`.  (ii) is the computation of `|n^{½−ρ}|` at `ρ ∓ a` together with
the definition of `W_a`.  (iii) is the `r`-independence of the polar data of
`E_r = rF_+ + K_a` (`F_+` being `Ξ_a`-primitive) and `R_a(E_r) = R_a(K_a) + ½r²q_a` with
`q_a > 0`.  ∎  `PROVED`

These three clauses locate the separating step **of Theorem 20.22's proof**.  They are
not a proof that no other separation of `ξ` from `Ξ_a` exists; that would be a
(T2_cone)-type statement about the whole frame.

### 20.8 Closure: one ray refutes every weakening

**Lemma 20.36 (the ray, and its frame invariants; `PROVED`).**  Let `F ∈ C_c^∞(R)` be
real, primitive, with `q := I_∞(F,F) > 0`, and let `E_t := tF + K`, `t ∈ R`.  **Such an
`F` exists if and only if RH is false** (Paper 45 Theorem 10.4 in both directions, the
converse direction being the last step of Theorem 20.17).  If it exists, then along the
ray:

| invariant of the frame | value along the ray | |
|---|---|---|
| `a = Φ_{E_t}(1)` | `½` | frozen (`F` primitive) |
| `b = Φ_{E_t}(0)` | `½` | frozen |
| `\deg E_t = a+b` | `1` | frozen |
| `I_∞(E_t,K) = ½\deg E_t` | `½` | frozen |
| `R(E_t) = ½I_∞(E_t,E_t) − ¼\deg E_t` | `½t²q > 0` | sign frozen (`E_t ∈ S_0`, `t ≠ 0`) |
| `W(E_t) = Σ_ρΦ_{E_t}(ρ)Φ_{E_t}(1−ρ)` | `−t²q → −∞` | unbounded |
| `Σ_ρ|Φ_{E_t}(ρ)|²` | `t²Σ_ρ|Φ_F(ρ)|² → +∞` | unbounded |
| `t_m(E_t)`, any fixed `m` | `Φ_g(0)\cosh(½\log m) + t\,t_m(F) → −∞` | unbounded below |
| `|I_∞(E_t,F)|/\deg E_t` | `|t|q → ∞` | unbounded |

*Proof.*  Existence is Paper 45 Theorem 10.4.  Every row follows from the four
identities `\deg K = 1`, `I_∞(F,K) = 0`, `I_∞(K,K) = ½` (Theorem 11.8(i),(ii)) and
`Φ_K(ρ) = ξ(ρ) = 0`: the polar data of `E_t` is that of `K` because `F` is primitive,
whence rows 1–4; `I_∞(E_t,E_t) = t²q + ½` gives row 5; the zero data is
`Φ_{E_t}(ρ) = tΦ_F(ρ)`, whence rows 6–7 with `W_F = −q` (Theorem 11.5 on a primitive
class); row 8 is Lemma 20.27 with the sign of `t` chosen against `t_m(F)`, which is
nonzero for suitable `F` by Lemma 20.28; row 9 is Theorem 20.31(i).  ∎  `PROVED`

**Theorem 20.37 (the ray refutes every weakening; `PROVED`).**  Each of the following
six weakenings of the clause is refuted by the single object `E_t` of Lemma 20.36, and
hence holds only if RH does:

| weakening | refuted by | at |
|---|---|---|
| `(P_m)` at a fixed index `m` | `t_m(E_t) < 0` with `E_t ∈ S_0` | Theorem 20.29(i) |
| the sparse cone `\{t_{2^k} ≥ 0\}` | the same at `k = 0` | Corollary 20.33 |
| any stratification of the degree-`1` head into unconditional and conditional members | `E_t` has degree exactly `1` | Lemma 20.36, rows 1–3 |
| bounded density of `S_0` in some direction | `|I_∞(E_t,F)| = |t|q → ∞` at `\deg = 1` | Theorem 20.31(i) |
| "the constant `1/(2λ)` is large enough" | the witness is **linear in `t`** at frozen degree | Restatement 20.30 |
| an unconditional lower bound for `W` in the frame's invariants on `S_0` | `W(E_t) → −∞` at frozen `(a,b,\deg)` | Corollary 20.32 |

*Proof.*  Row by row, each entry is the cited statement evaluated on `E_t`, and
`E_t` exists if and only if RH fails (Lemma 20.36).  ∎  `PROVED`

The diagnosis is short.  The frame's unconditional data on a class are
`(a,b,\deg E,R(E))` together with **upper** bounds on `W(E)`.  Along the ray all of
these are frozen, or frozen in sign, while the zero data is unbounded.  A frame whose
invariants are constant along a family on which the clause changes truth value cannot
decide the clause; and that is a property of the invariants, not an accident of the
particular weakenings tried.

**Theorem 20.38 (what the frame cannot see; `PROVED`).**  Exactly two facts are used by
Theorem 20.22 and are unavailable to the frame, and both are **zero-location**
statements:

 (W1) **`W(E) = Σ_ρΦ_E(ρ)Φ_E(1−ρ)` is a norm if and only if RH.**  Unconditionally it
      is a `ρ ↔ 1−ρ` pairing, indefinite; `W(E) = Σ_ρ|Φ_E(ρ)|²` requires
      `1−ρ = \barρ`.  Consequently `R(E) > 0`, which reads `2ab − W(E) > ½(a+b)`, bounds
      `W` from **above** only, and by Corollary 20.32 no lower bound in the frame's
      invariants exists.
 (W2) **`|n^{½−ρ}| = 1` if and only if RH.**  Unconditionally (E2) gives only
      `|n^{½−ρ}| = n^{½−\mathrm{Re}ρ} ∈ (n^{−½},n^{½})`, and
      `\inf_ρ\mathrm{Re}\,ρ > 0` is a quasi-RH zero-free-strip statement, not supplied
      by any classical zero-free region.

Neither is a Riemann–Roch fact, a Hodge-index fact, or a statement about degrees,
effectivity or the canonical class.

*Proof.*  (W1): `Σ_ρΦ_E(ρ)Φ_E(1−ρ) = Σ_ρ|Φ_E(ρ)|²` for all real `E` forces
`1−ρ = \barρ` at every zero, which is RH; conversely RH gives it.  Indefiniteness off
RH is Lemma 20.36's row 6.  The upper-bound remark is the inequality
`2ab − W(E) > ½(a+b)`, i.e. `R(E) > 0` and `\deg E > 0` rewritten by Theorem 11.5, and the non-existence
of a lower bound is Corollary 20.32.  (W2): `|n^{½−ρ}| = n^{½−\mathrm{Re}ρ}` is an
identity; it equals `1` for all `n ≥ 2` exactly when `\mathrm{Re}\,ρ = ½`.  ∎  `PROVED`

**Theorem 20.39 (the parting point with `Ξ_a`; `PROVED`).**  `Ξ_a` satisfies, verbatim
and unconditionally: (T1′) (Theorem 20.24); the transfer theorem (Theorem 20.24); the
eventual half of Proposition 20.26; the polar AM–GM floor in its `\cosh` normal form
(Lemma 20.34); and the degree and `R`-positivity of the ray (Theorem 20.35(iii)).  The
**only** point at which `ξ` and `Ξ_a` part company is the statement

> *there is a primitive compactly supported `F` with `I_∞(F,F) > 0`* —

for `Ξ_a` a **theorem** (Proposition 12.4B, unconditional, its hypothesis "`Ξ_a` has an
off-line zero" being automatic since the zeros are `ρ ∓ a`), and for `ξ` **literally the
negation of RH** (Paper 45 Theorem 10.4).

*Proof.*  Each transported item is the theorem cited.  The displayed statement is
Proposition 12.4B for `Ξ_a` and, for `ξ`, the contrapositive of Paper 45 Theorem 10.4
together with the last step of Theorem 20.17.  ∎  `PROVED` (as a reading of the cited
theorems; cf. the scope caveat after Theorem 20.35)

So the separation *is* the statement itself, not a step towards it: the falsifier is not
a counterexample some finer argument might dodge, but a proof that every statement of
the frame tested here is model-uniform, and that the one non-uniform statement is RH.

**Conclusion of record.**  The Riemann–Roch / Hodge-index frame produces restatements of
RH, not reductions.

### Withdrawn in this section

| claim | reason |
|---|---|
| "a two-point equimodular polar set has a uniform AM–GM floor and a four-point set does not", offered as the line separating `ξ` from `Ξ_a` | **false**: by Lemma 20.34(i),(ii) every symmetric polar set has a uniform positive AM–GM floor, and by (iv) the four-point floor is attained at `n = 1`.  The true separator is Theorem 20.35(ii),(iii): `\|n^{½−(ρ±a)}\| = n^{∓a}` unbounded, and `W_a` indefinite |
| `(G⁺)` proved only for the two-bump family `g_T(u) = h(u−T)+h(u+T)` | that computation is correct but RH-conditional (off the line `\|\cosh((ρ−½)T)\|` grows like the polar term) and its nonnegativity bookkeeping was asserted rather than estimated; Lemma 20.21 replaces it unconditionally |
| the transfer theorem 12.3-B4 is "strictly stronger" than Theorem 12.3 | **false**: the two clauses are incomparable, since `𝓔 ⊄ B4` and `B4 ⊄ 𝓔` (Remark 20.12).  Replaced by the comparison in Remark 20.17a |
| for `ξ_K` with a real zero `β_0`, the primitive trace-positive cone contains classes outside `𝓝_∞^{(K)}` | the existence of such a class is an interpolation statement over an infinite constraint set, and no realisation theorem is available (Lemma 20.6 gives surjectivity onto **finite** windows only); only the sign computation was verified.  `OPEN`; Theorem 20.25 does not use it |
| the dual description of the moment cone `𝔐` as the full dual cone of the nonnegativity cone `𝒫_g` | only the inclusion "`⟨λ,x⟩ ≥ 0` for `λ ∈ 𝒫_g`" is proved; the reverse needs a density statement asserted nowhere.  `OPEN`; nothing here uses it |
| "`R(E) > 0` and `\deg E > 0` say **exactly** the inequality `2ab − W(E) > ½(a+b)`, and nothing more follows" | a maximality claim over all possible consequences, which is not a theorem.  The four consequences actually used are recorded as such |
| the smallest failing index for `Ξ_a` lies in a discrete exceptional set of test classes | withdrawn; what is proved is that `m_*(g_a) < ∞` always, and that `m_* = 1` on a non-empty open set of test classes |
| "A8 enters through the index set `n ∈ N`, since a generic sequence `c_k → ∞` would admit no Dirichlet series" | **false**: `Σ_k t_{c_k}e^{−wc_k}` is a generalised Dirichlet series and (X20) applies verbatim; what fails is meromorphic continuation.  The geometric semigroup `\{2^k\}` runs the whole cascade (Corollary 20.33).  Replaced by: the translations must form a multiplicative semigroup whose generating function continues meromorphically to a neighbourhood of the real axis, and `ξ`'s polar exponents must be the two real numbers `\{0,1\}` |

---

## 21. The function-field model of the frame

*Provenance note.  This section is the paper form of
`03-research/phase-145-row-d-function-field-model/R145_001_ROUND1.md`
(statements and proofs), with final labels, withdrawals and the named
ingredient as decided in `R145_005_CLOSING_DECISION.md` and confirmed in
`R145_002_AUDIT.md` and `R145_004_CONFIRMATION.md`; the corpus
ledger is `CORPUS_CHECK_R145.md`.  Certified constants come from
`03-research/phase-145-row-d-function-field-model/scripts/sC_and_points.py`,
and every one of them is also given here in exact closed form.*

Part II reduced row D's target to the existence of one function `h⁰` on `D^W`
with the clauses (a),(b′),(c) of Theorem 12.3, and §19 proved that no such
`h⁰` exists: the sharp constant `s₁ = 0.99846… < 1` of the frame's effective
cone produces a class of degree `d ≥ 325` that (b′) cannot accommodate.  The
question left by §19 and §20 is what `s₁ < 1` is a statement *about*.  This
section answers it in the only case where every object of the frame exists and
the Riemann hypothesis is a theorem: a curve over a finite field.

The answer is that **the frame defect theorem holds there too**.  Everything of
§19 transcribes, with a *larger* defect (`1 − s_C^* = 0.2023` against
`1 − s₁ = 0.00154`) and a witness at `d = 3` rather than `d = 325`, while
`h⁰_C(D) = \dim H⁰(C×C, 𝒪(D))` exists and is the object Weil's proof uses.  So
`s < 1` is a property of the **cone**, not of the zeros, and not the signature
of a missing sections functor.  What the model then names, exactly, is the
ingredient the arithmetic frame lacks.

Two external inputs are used, **(X27)** and **(X28)**, tabulated at the end of
the section.  Both are classical and neither is reproved.

### 21.1 The discrete frame

`C/F_q` is smooth projective geometrically irreducible of genus `g`, with
function field `F = F_q(C)`; `Z_C(T) = P(T)/((1−T)(1−qT))`,
`P(T) = ∏_{i=1}^{2g}(1−α_iT) ∈ Z[T]`, `N_m = \#C(F_{q^m}) = q^m+1−Σ_iα_i^m`,
`∏_iα_i = q^g`, `|α_i| = √q`, and the multiset `\{α_i\}` is stable under
`α ↦ q/α` and under complex conjugation — all of this is **(X27)**.  The
intersection numbers on the surface `S = C×C`, with `F_1 := \{P\}×C`,
`F_2 := C×\{P\}`, `Δ` the diagonal, and `Γ_f` the graph of a morphism
`f : C → C` of degree `d`,

    F_1² = F_2² = 0,\quad F_1·F_2 = 1,\quad Δ·F_1 = Δ·F_2 = 1,\quad Δ² = 2−2g,
    Γ_f·F_1 = 1,\quad Γ_f·F_2 = d,\quad Γ_f² = d(2−2g),
    K_{C×C} = (2g−2)(F_1+F_2),\quad χ(𝒪_{C×C}) = (1−g)^2 ,                (21.1)

together with the Lefschetz count `Γ_{q^m}·Δ = \#\mathrm{Fix}(F^m) = N_m` and,
for `m ≥ n ≥ 0`, `Γ_{q^m}·Γ_{q^n} = q^nN_{m−n}`,
`Γ_{q^m}^{\,t}·Γ_{q^n} = N_{m+n}`, are **(X28)** and **(X27)**.  Three symbols
are kept distinct throughout and are three different objects: `ω_C`, the
canonical divisor of the curve (`\deg ω_C = 2g−2`); `K_{C×C}`, the canonical
class of the surface; and `K_C`, the **frame's** canonical class of
Theorem 21.20 below.

**The completion.**  `ζ_C(s) := Z_C(q^{−s})` has poles at
`s ∈ \{0,1\} + (2πi/\log q)Z`.  The frame requires `Φ_{K_Z} = Z` with `K_Z` in
the carrier, so `Z` must be entire: the frame's `ξ`-analogue is the
**numerator**, not `ζ_C`.

**Definition 21.1 (the model completion).**  With `z := q^{s−1/2}` (so
`T = q^{−s} = q^{−1/2}z^{−1}`) and `u_i := α_i/\sqrt q` (`|u_i| = 1`),

    Λ_C(z) := z^{−g}∏_{i=1}^{2g}(z−u_i),\qquad ξ_C(s) := Λ_C(q^{s−1/2}) .   (21.2)

**Lemma 21.2 (the model `ξ`; `PROVED`).**  `ξ_C` is a Laurent polynomial in `z`
of degree `g`; `ξ_C(s) = ξ_C(1−s)`; its zeros in the strip are exactly the `2g`
points `ρ_i` with `q^{ρ_i} = α_i`, so `\mathrm{Re}\,ρ_i = ½` by **(X27)**, read
modulo the period `2πi/\log q`; and
`ξ_C(0) = ξ_C(1) = h\,q^{−g/2}` with `h := P(1) = \#\mathrm{Pic}^0(C)(F_q)` the
class number.

*Proof.*  `∏u_i = ∏α_i/q^g = 1`, so

    Λ_C(1/z) = z^{−g}∏(1−u_iz) = z^{−g}∏(−u_i)(z−u_i^{−1}) = z^{−g}∏(z−u_i) = Λ_C(z) ,

using `u_i^{−1} = \bar u_i` and the stability of the multiset under conjugation;
and `z ↦ 1/z` is `s ↦ 1−s`.  For the zeros,
`Λ_C(z) = 0 ⟺ z = u_i ⟺ q^{s−1/2} = α_i/\sqrt q ⟺ q^s = α_i`.  For the values,
`Λ_C(q^{1/2}) = q^{−g/2}∏(q^{1/2}−u_i) = q^{−g/2}q^{−g}∏(q−α_i)`, and
substituting the permutation `α ↦ q/α`,
`∏(q−α_i) = q^{2g}∏(1−α_i^{−1}) = q^{2g}∏(1−α_i)/∏α_i = q^gP(1)`; hence
`Λ_C(q^{1/2}) = q^{−g/2}h`, and `Λ_C(q^{−1/2})` equals it by the functional
equation just proved.  ∎  `PROVED`

**The carrier.**  `C_F` is the idele class group of `F`; `|·| : C_F → q^{Z}` is
onto (F. K. Schmidt: `C` has a divisor of degree `1` over `F_q`), and
`C_F ≅ Z × C_F^0` with `C_F^0` compact.  The modulus line of §11 is therefore
the **lattice** `t ∈ (\log q)Z`, not `R`.

**Definition 21.3 (the model Weil class).**

    D^W_C := \{E : Z → R\ :\ ∃ε>0,\ E(n) = O(q^{−(1+ε)|n|})\} ,
    Φ_E(s) := Σ_{n∈Z}E(n)\,q^{(s−1/2)n} = L_E(z),\quad L_E(z) := Σ_{n∈Z}E(n)z^n .  (21.3)

`E^∨(n) := E(−n)`; `⋆` is convolution on `Z`; `τ_mE := E(\cdot−m)`; and
`\deg E := Φ_E(0)+Φ_E(1) = Σ_nE(n)\,2\cosh(n\log q/2)` — Definition 11.6
verbatim with `∫dt` replaced by `Σ_{n∈Z}`, the weight `2\cosh(t/2)` unchanged.

**Lemma 21.4 (the carrier; `PROVED`).**
 (i) `D^W_C` is a real `⋆`-algebra with involution `∨`, stable under every `τ_m`.
 (ii) `L_E` converges absolutely on the annulus `q^{−(1+ε)} < |z| < q^{1+ε}`;
   equivalently `Φ_E` is holomorphic on `−½−ε < \mathrm{Re}\,s < 3/2+ε`, the
   same strip as Definition 11.1.
 (iii) `Φ_{E^∨}(s) = Φ_E(1−s)`, `Φ_{τ_mE}(s) = q^{(s−1/2)m}Φ_E(s)`,
   `Φ_{E⋆F} = Φ_EΦ_F`.
 (iv) `Φ_E` is periodic in `\mathrm{Im}\,s` with period `2π/\log q`: it is a
   function of `z` alone.
 (v) `δ_m ∈ D^W_C` for every `m ∈ Z`.

*Proof.*  (i),(iii),(iv),(v) are immediate from (21.3) and the definitions.
(ii) is the estimate `|q^{(σ−1/2)n}| = q^{(σ−1/2)n}` against the decay
`q^{−(1+ε)|n|}`, which converges exactly on the stated annulus.  ∎  `PROVED`

Two consequences are worth naming at once, because they are what makes the
model easier than the arithmetic frame rather than harder.  First, no
smoothness hypothesis survives: Definition 11.1 imposes `C²` with decay for
`j = 0,1,2` for one reason only — the bound `|Φ_g(s)| ≤ C_2|s−½|^{−2}` of
(11.2), which with (E3d) makes the zero sum absolutely convergent.  Here the
zero sum has `2g` terms, so the entire apparatus of Lemma 11.2(iii), (11.2) and
(E3d) is vacuous, and the carrier contains the **point masses** `δ_m`, which by
Theorem 21.9(iii) are the extreme rays of its effective cone.  Arithmetically
`δ_a ∉ D^W`, and `𝓔` has no extreme ray inside `D^W` at all.  Second,
periodicity collapses the zero data to the `2g`-tuple `(L_E(u_i))_i` and the
polar data to the pair `(L_E(q^{−1/2}), L_E(q^{1/2}))`, whence the finite rank
of Theorem 21.8.  Both are recorded in the mismatch table of §21.8.

**Theorem 21.5 (the explicit formula in the model; `PROVED` from `CLASSICAL`).**
Put `N_0 := 2−2g` — the value forced by `N_m = q^m+1−Σ_iα_i^m` at `m = 0`,
since `Σ_iα_i^0 = 2g` — and

    κ(n) := q^{−|n|/2}\,N_{|n|}\qquad (n ∈ Z) .                              (21.4)

Then for every `E ∈ D^W_C`,

    Φ_E(0)+Φ_E(1) − Σ_{i=1}^{2g}Φ_E(ρ_i) \;=\; Σ_{n∈Z}E(n)\,κ(n) .           (21.5)

*Proof.*  `Σ_iΦ_E(ρ_i) = Σ_nE(n)Σ_iu_i^n = Σ_nE(n)q^{−|n|/2}S_{|n|}` with
`S_m := Σ_iα_i^m`, where `Σ_iu_i^n = Σ_iu_i^{|n|}` because `u_i^{−1} = \bar u_i`
and the multiset is conjugation-stable, so the sum is real and depends on `|n|`.
On the other side `Φ_E(0)+Φ_E(1) = Σ_nE(n)(q^{|n|/2}+q^{−|n|/2})`.  Subtract and
use `N_m = q^m+1−S_m` from **(X27)**, valid also at `m = 0` with `S_0 = 2g`.  ∎
`PROVED`

This is Weil's explicit formula for `C`, with `N_m = Σ_{d|m}d\,B_d` and `B_d`
the number of closed points of degree `d`.  Its archimedean side is a single
integer: the term at `n = 0` is
`κ(0) = N_0 = 2−2g = χ_{\mathrm{top}}(C) = −\deg ω_C`, and `PRIME − ARCH`
becomes one lattice sum.  The model has **no archimedean place** — `F` is a
function field, all of whose places are finite — so the archimedean integral of
(11.3) is replaced by the Euler characteristic of the curve, and open item (21)
of §14.5 is not a model artefact but exactly a point at which the arithmetic
frame carries structure the model does not.

### 21.2 The intersection identity

**Definition 21.6 (the form and the dictionary).**  For `E,F ∈ D^W_C`,

    I_∞^C(E,F) := Φ_E(0)Φ_F(1) + Φ_E(1)Φ_F(0) − Σ_{i=1}^{2g}Φ_E(ρ_i)Φ_F(1−ρ_i) ,  (21.6)
    γ_n := q^{−|n|/2}\,Γ_n,\quad Γ_n := Γ_{q^n}\ (n ≥ 0),\quad Γ_{−n} := Γ_{q^n}^{\,t}\ (n>0),\ Γ_0 = Δ ,
    D_E := Σ_{n∈Z}E(n)\,γ_n \;∈\; \mathrm{Div}(C×C)⊗R .                       (21.7)

**Theorem 21.7 (the dictionary; the sign is `+`; `PROVED`).**  For all
`E,F ∈ D^W_C`:
 (i) `γ_a·γ_b = κ(a−b) = q^{−|a−b|/2}N_{|a−b|}` for all `a,b ∈ Z` — the Gram is
   the **Toeplitz** matrix of the point counts, with `N_0 = 2−2g` forced;
 (ii) `I_∞^C(E,F) = Σ_m(E⋆F^∨)(m)\,κ(m) = \;\mathbf{+}\,(D_E·D_F)`;
 (iii) `D_E·F_1 = Φ_E(0)`, `D_E·F_2 = Φ_E(1)`, and `\deg E = D_E·(F_1+F_2)`;
 (iv) `E` is **primitive** (`Φ_E(0) = Φ_E(1) = 0`) if and only if
   `D_E ⊥ F_1, F_2`.

*Proof.*  (i) By the Lefschetz relations of **(X27)**: for `a ≥ b ≥ 0`,
`γ_a·γ_b = q^{−(a+b)/2}q^bN_{a−b} = q^{−(a−b)/2}N_{a−b}`; for `a ≥ 0 > b = −n`,
`γ_a·γ_b = q^{−(a+n)/2}N_{a+n} = q^{−|a−b|/2}N_{|a−b|}`; the remaining cases are
the transposes of these.  The value at `a = b` is `κ(0) = Δ² = 2−2g` by (21.1),
which is the same forcing.  (ii) Expand
`D_E·D_F = Σ_{a,b}E(a)F(b)κ(a−b)`, substitute `a = m+b`, and obtain
`Σ_m(E⋆F^∨)(m)κ(m)`; now apply (21.5) to `E⋆F^∨`, using
`Φ_{E⋆F^∨}(0) = Φ_E(0)Φ_F(1)`, `Φ_{E⋆F^∨}(1) = Φ_E(1)Φ_F(0)` and
`Φ_{E⋆F^∨}(ρ_i) = Φ_E(ρ_i)Φ_F(1−ρ_i)`, all three from Lemma 21.4(iii).  That is
(21.6).  (iii) `Γ_n·F_1 = 1` and `Γ_n·F_2 = q^n` for `n ≥ 0` by (21.1) with
`d = \deg F^n = q^n`, transposed for `n < 0`; hence `γ_n·F_1 = q^{−n/2}` and
`γ_n·F_2 = q^{n/2}` **uniformly in `n ∈ Z`**, and these are exactly the
coefficients of `Φ_E(0)` and `Φ_E(1)` in (21.3).  (iv) is (iii).  ∎  `PROVED`

*Certified (`sC_and_points.py` §[5]): for the curve of record,
`\max_{|a|,|b|≤4}|I_∞^C(δ_a,δ_b) − q^{−|a−b|/2}N_{|a−b|}| = 3.6×10^{−15}`, and
the fibre pairings of (iii) reproduce `q^{∓n/2}` exactly.*

The sign in (ii) is `+`, and it is forced: the half-density weight
`q^{−|n|/2}` on the graphs — the same `n^{−1/2}` that Paper 44 §3ter.10 attaches
to `Frob_n`, `Σ_qW_q(Frob_n) = Λ(n)n^{−1/2}h(1/n)` — is what makes the Gram
Toeplitz, and without it no identity holds.  With it, the frame's target
statement is, in the model, literally Weil's proof: row D asks for
`I_∞^C(F,F) ≤ 0` on primitives, which by (ii),(iv) is `D² ≤ 0` on
`\{F_1,F_2\}^⊥`, the Hodge index theorem of **(X28)** with the ample class
`H := F_1+F_2`, `H² = 2 > 0`.

**Cross-reference (the gap left open in the repository).**  Paper 43's
comparison functor, recorded at `A125.009`, is *"not a comparison with all
finite correspondences, and in particular not with the graph of Frobenius on a
curve over `F_q`, which is finite and not invertible."*  Theorem 21.7 **closes
that gap for row D**: the dictionary (21.7) is built on `Γ_{q^n}` and its
transpose, i.e. on exactly the non-invertible correspondences excluded there,
and the non-invertibility is what makes the index set the signed set `Z` rather
than a group.

**Theorem 21.8 (the radical and the isometry; `PROVED`).**  Assume the Weil
numbers `α_1,…,α_{2g}` are pairwise distinct — true for the curve of record,
which is ordinary with `a²−4q = −7 < 0`, so `α ≠ \barα`.  Let

    𝓝^C_∞ := \{N ∈ D^W_C : I_∞^C(N,G) = 0\ ∀G ∈ D^W_C\} .

Then

    𝓝^C_∞ = \{N : Φ_N(0) = Φ_N(1) = 0,\ Φ_N(ρ_i) = 0\ (1 ≤ i ≤ 2g)\} ,
    \dim_R D^W_C/𝓝^C_∞ = 2+2g ,

and `E ↦ D_E` induces an **isometric injection**
`(D^W_C/𝓝^C_∞,\ I_∞^C) \hookrightarrow (V_C,\ ·)`,
`V_C := Σ_nR\,γ_n ⊆ NS(C×C)_R`, of signature `(1,\,1+2g)`.

*Proof.*  The inclusion `⊇` is immediate from (21.6).  For `⊆`: pairing `N`
against `δ_m` for every `m` gives, by (21.6),

    Φ_N(0)q^{−m/2}+Φ_N(1)q^{m/2} = Σ_iΦ_N(ρ_i)\bar u_i^{\,m}\qquad (m ∈ Z) .

The functions `m ↦ q^{\pm m/2}` and `m ↦ \bar u_i^{\,m}` are pairwise distinct
characters of `Z` — `|q^{\pm1/2}| ≠ 1 = |u_i|`, and the `u_i` are distinct by
hypothesis — hence linearly independent, so every coefficient vanishes.  (This
is the discrete analogue of Lemma 11.9, and it is a Vandermonde argument, not a
Laplace-transform one.)  The same independence makes the evaluation map onto
`R^{2+2g}` surjective, giving the dimension.  Isometry is Theorem 21.7(ii).  For
the signature, in the coordinates (21.8) below `I_∞^C = 2ab − 2Σ_i|\cdot|²`,
which is `(1,1)` on the polar plane and negative definite on the zero block.  ∎
`PROVED`

Without the distinctness hypothesis the dimension **drops** below `2+2g`
(supersingular curves, and many curves of genus `≥ 2`); nothing else in this
section uses it, and every certified statement is on the curve of record.

**Coordinates.**  For `g = 1` write `ρ := ρ_1`, `\barρ = 1−ρ`, and

    (a_E,\,b_E,\,x_E,\,y_E) := (Φ_E(1),\,Φ_E(0),\,\mathrm{Re}\,Φ_E(ρ),\,\mathrm{Im}\,Φ_E(ρ)) ,
    I_∞^C(E,F) = a_Eb_F + b_Ea_F − 2(x_Ex_F + y_Ey_F),\qquad \deg E = a_E+b_E .  (21.8)

By Theorem 21.7(iii) the first two are `(D·F_2,\ D·F_1)`, and the signature is
`(1,3)` on the rank-`4` lattice `V_C`.

**Rulings.**  In `V_C`, `e_- := F_1` and `e_+ := F_2` satisfy `e_\pm² = 0`,
`e_+·e_- = 1`: the hyperbolic plane of Paper 43 Theorem 9.1 and of (1.8) is
realised **inside** the model's carrier, and `†` (`= ∨`, `n ↦ −n`) acts on it by
the swap `♯`, since `γ_n^∨ = γ_{−n} = Γ_n^{\,t}` — the involution of Paper 43
§9 is the transpose of correspondences.  `RESTATEMENT`

That the rulings are honest classes here is the single most load-bearing
difference the model exhibits: Theorem 11.14's repair records that
arithmetically `e_∓` live in the completion `N_A^{dist}` as limits of spread
Tate families whose `L¹`-mass escapes, and are exactly the **radical** of the
boundary form there (Paper 43 Theorem 9.14c), so that `K ≡ ½(e_++e_-)` is true
as an identity of ruling data and false as an identity of classes
(Proposition 14.1(iv)).  In the model it is an identity of classes
(Theorem 21.20(iv)), because `F_1,F_2 ∈ V_C` and `F_1·F_2 = 1 ≠ 0`.  That
`F_1 ∈ V_C` needs a rank count and holds for the curve of record: by Tate's
theorem (**(X27)**) `\mathrm{rk}\,NS(E×E) = 2+\mathrm{rk\,End}(E) = 4` for an
ordinary `E/F_q`, while `\dim V_C = 2+2g = 4` by Theorem 21.8, so
`V_C = NS(E×E)_R ∋ F_1`.  For a supersingular `E`, `\mathrm{rk\,End} = 4` and
`\mathrm{rk}\,NS = 6 > 4`: the carrier then sees only a proper sublattice of
`NS`, an additional deficiency not measured by `s_C` and recorded as `OPEN`
in §21.8.

### 21.3 The frame defect theorem holds on the curve

**Theorem 21.9 (Theorems 11.13 and 11.14 in the model; `PROVED`).**  Let
`𝓔_C := \{E ∈ D^W_C : E ≥ 0\ \text{pointwise},\ E ≢ 0\}` be the frame's
effective cone, transcribed.  Then:
 (i) `E ∈ 𝓔_C ⟹ \deg E = Σ_nE(n)2\cosh(n\log q/2) > 0`, and
   `N ∈ 𝓝^C_∞ ⟹ \deg N = 0`; hence no nonzero primitive or principal class is
   effective, and `2κ_C` is **ample**: `I_∞^C(E,2κ_C) = \deg E > 0` on `𝓔_C`,
   with `κ_C` the class of Theorem 21.20, whose proof uses only Lemma 21.2.
 (ii) With
   `w_F(n) := Φ_F(1)q^{−n/2}+Φ_F(0)q^{n/2} − Σ_iq^{(ρ_i−½)n}Φ_F(1−ρ_i)` one has
   `I_∞^C(E,F) = Σ_nE(n)w_F(n)` and

       C_F := \sup_{n∈Z}\frac{|w_F(n)|}{2\cosh(n\log q/2)}
            \;≤\; |Φ_F(0)|+|Φ_F(1)|+Σ_{i=1}^{2g}|Φ_F(1−ρ_i)| \;<\;∞ ,

   so `|I_∞^C(E,F)| ≤ C_F\deg E` for every `E ∈ 𝓔_C`.
 (iii) `𝓔_C` is generated by its extreme rays `\{δ_n\}_{n∈Z}`, and
   `D_{δ_n} = γ_n`; hence **the frame's effective cone is, in the model, exactly**

       𝓔_C = \mathrm{Cone}\{q^{−|n|/2}Γ_{q^n},\ q^{−|n|/2}Γ_{q^n}^{\,t}\ :\ n ≥ 0\} ,

   the cone spanned by the graphs of the Frobenius powers and their transposes,
   and by nothing else.

*Proof.*  (i) `2\cosh(n\log q/2) ≥ 2 > 0` for every `n`, so the sum of a
nonnegative, nonzero `E` against it is positive; a class in the radical has
`Φ_N(0) = Φ_N(1) = 0` by Theorem 21.8, hence degree `0`; and the ampleness
statement is `I_∞^C(E,2κ_C) = \deg E` from Theorem 21.20(iii).  (ii) The
identity `I_∞^C(E,F) = Σ_nE(n)w_F(n)` is (21.6) with `Φ_E` expanded by (21.3).
For the bound, `e^{\pm n\log q/2} ≤ 2\cosh(n\log q/2)` for every `n ∈ Z`, and
`|q^{(ρ_i−½)n}| = 1` because `\mathrm{Re}\,ρ_i = ½`; dividing the three groups of
terms of `w_F(n)` by `2\cosh(n\log q/2)` and bounding each gives the displayed
sum, which is finite because the zero set is finite.  This is (11.17) verbatim.
Only **finiteness** is used downstream — Theorem 12.3 Step 1 picks any
`m > C_F` — and the supremum need not be attained: indeed
`w_F(n)/2\cosh(n\log q/2) → Φ_F(0)` as `n → +∞` and `→ Φ_F(1)` as `n → −∞`, and
for `F = κ_C` it is identically `½`.  (iii) is the definition of `𝓔_C` together
with (21.7): a pointwise nonnegative sequence is a nonnegative combination of
point masses, and no `δ_n` is such a combination of the others.  ∎  `PROVED`

**Definition 21.10 (the model constant).**  For `γ,θ ∈ R`,

    s_C(γ,θ) := \sup_{n∈Z}\frac{|\cos(γ\,n\log q + θ)|}{\cosh(n\log q/2)} .   (21.9)

**Lemma 21.11 (Lemma 19.17 in the model; `PROVED`, unconditional).**  Let
`E' ∈ 𝓔_C`.  Then for all real `γ,θ`,

    \Big|Σ_nE'(n)\cos(γ\,n\log q+θ)\Big| ≤ \tfrac12\,s_C(γ,θ)\,\deg E' ,

and in particular, at a zero `ρ = ½+iγ` of `ξ_C`,
`|\mathrm{Re}(e^{iθ}Φ_{E'}(ρ))| ≤ ½\,s_C(γ,θ)\,\deg E'`.

*Proof.*  By (21.9), `|\cos(γn\log q+θ)| ≤ s_C(γ,θ)\cosh(n\log q/2)` pointwise on
`Z`.  Sum against `E' ≥ 0` and use
`\deg E' = Σ_nE'(n)2\cosh(n\log q/2)`.  The last clause is
`Φ_{E'}(½+iγ) = Σ_nE'(n)e^{iγn\log q}`.  ∎  `PROVED`

Lemma 21.11 holds for **every** `θ`, and the witness of Theorem 21.14 may be
built in whatever direction it likes, the evaluation map of Theorem 21.8 being
onto.  The arithmetic statement of §19 uses `θ = π/2`; in the model that is one
choice among many, and not the best one.

**Proposition 21.12 (the sharpness gap at the arithmetic direction; `PROVED`,
exact).**
 (i) `n = 0` lies in the sample set, so `s_C(γ,θ) ≥ |\cos θ|`; in particular
   `s_C(γ,0) = 1` for every `γ` and `\max_θ s_C(γ,θ) = 1`.
 (ii) `s_C(γ,θ) < 1` **if and only if `θ ∉ πZ`** — and, unlike the arithmetic
   case, **no hypothesis `γ ≠ 0` is needed**, because
   `\cosh(n\log q/2) ≥ \cosh(\log q/2) > 1` for every `n ≠ 0`.
 (iii) For `g = 1`, `θ = π/2`, and `γ_1` the ordinate of `ρ_1` (so
   `γ_1\log q = θ_u = \arg u`), with `a := q+1−N_1`,

     s_C(γ_1,π/2) = \max\Big(\frac{\sqrt{4q−a^2}}{q+1},\ \max_{|n|≥2}\frac{|\sin(nθ_u)|}{\cosh(n\log q/2)}\Big) ,

   and whenever the first entry dominates,

     s_C(γ_1,π/2)^2 = \frac{4q−a^2}{(q+1)^2},\qquad
     d_0 := \frac1{1−s_C^2} = \frac{(q+1)^2}{(q−1)^2+a^2}\quad\textbf{(exact, rational)} .  (21.10)

*Proof.*  (i) and (ii) are immediate from (21.9), the `n = 0` term of which is
`|\cos θ|` and every other term of which has denominator `> 1`.  (iii) At
`n = ±1` the ratio is
`|\sin θ_u|/\cosh(\log q/2) = |\sin θ_u|\cdot 2\sqrt q/(q+1)`, and
`\sin^2θ_u = 1−a^2/(4q)` since `\cos θ_u = a/(2\sqrt q)`; substituting gives
(21.10).  ∎  `PROVED`

**Proposition 21.13 (the model's sharp constant; `PROVED`, exact).**  Let
`g = 1`.  Minimising (21.9) over `θ`, the optimum balances the `n = 0` and
`n = 1` entries, `|\cos θ| = |\cos(θ_u+θ)|/\cosh(\tfrac12\log q)`, giving

    \tan θ^* = \frac{\cosh(\tfrac12\log q)+\cos θ_u}{\sin θ_u} = \frac{q+1+a}{\sqrt{4q−a^2}} ,
    (s_C^*)^2 = \min_θ s_C(γ_1,θ)^2 = \frac{4q−a^2}{(4q−a^2)+(q+1+a)^2} ,
    d_0^* := \frac1{1−(s_C^*)^2} = \frac{(4q−a^2)+(q+1+a)^2}{4q−a^2} ,        (21.11)

**provided no entry with `|n| ≥ 2` exceeds that value at `θ^*`** — a finite
check, which must be run.  For the curve of record `C = E/F_2 : y²+xy = x³+1`
(`g = 1`, `N_1 = 4`, `a = −1`, `h = 4`, ordinary, `α = (−1±i\sqrt7)/2`):
`\tan θ^* = 2/\sqrt7`, `θ^* = 0.647284848016…`, and

    s_C^* = \sqrt{7/11} = 0.797724035217…,\qquad d_0^* = \tfrac{11}4 = 2.75\ \ \textbf{exactly} ,

the side condition holds, and the supremum at `θ^*` is an exact **triple tie**,
attained at `n = −2, 0, +1`.

*Proof.*  The balance condition is the definition of `θ^*`: the map
`θ ↦ |\cos θ|` increases and `θ ↦ |\cos(θ_u+θ)|/\cosh(\tfrac12\log q)` decreases
across the relevant interval, so the minimum of their maximum is where they
agree, and solving `|\cos θ| \cosh(\tfrac12\log q) = |\cos(θ_u+θ)|` by expanding
the right side gives `\tan θ^*` and then `(s_C^*)^2 = \cos^2θ^*` in the form
(21.11), using `\cos θ_u = a/(2\sqrt q)`, `\sin θ_u = \sqrt{4q−a^2}/(2\sqrt q)`
and `\cosh(\tfrac12\log q) = (q+1)/(2\sqrt q)`.

For the curve of record, `\cos θ^* = \sqrt{7/11}`, `\sin θ^* = 2/\sqrt{11}`,
`\cos θ_u = −1/(2\sqrt2)`, `\sin θ_u = \sqrt7/(2\sqrt2)`,
`\cosh(\tfrac12\log 2) = 3/(2\sqrt2)`, `\cosh(\log 2) = 5/4`.  The `n = 0` entry
is `|\cos θ^*| = \sqrt{7/11}`; the `n = 1` entry equals it by the defining
balance; and since `\cos 2θ_u = 2\cos^2θ_u−1 = −\tfrac34` and
`\sin 2θ_u = 2\sin θ_u\cos θ_u = −\tfrac{\sqrt7}4`,

    \frac{|\cos(−2θ_u+θ^*)|}{\cosh(\log 2)}
      = \frac{\big|−\tfrac34\sqrt{7/11} − \tfrac{\sqrt7}4\cdot\tfrac2{\sqrt{11}}\big|}{5/4}
      = \frac{5\sqrt7}{4\sqrt{11}}\cdot\frac45 = \sqrt{\tfrac7{11}} ,

which is the third member of the tie.  Every remaining entry is
`≤ 0.620453 < s_C^*` — the largest is at `n = +3` — and
`|n| ≥ 5 ⟹ \text{entry} ≤ 1/\cosh(\tfrac52\log 2) = 0.1754`, so the side
condition holds.  ∎  `PROVED`

*Certified (`sC_and_points.py` §[1],[8]): `N_1 = 4` by brute force from the
equation, `N_m = 4,8,4,16,44,56` for `m = 1..6`, `θ_u = 1.932163450702…`; the
triple tie is reproduced to `10^{−15}` and the sweep `|n| ≤ 60` confirms the
side condition.  At `θ = π/2` the same script gives, exactly,
`s_C(γ_1,π/2)^2 = (7/8)/(9/8) = 7/9`, `s_C(γ_1,π/2) = \sqrt7/3 = 0.881917103688…`
and `d_0 = 9/2`, the `n = ±1` entry dominating since
`\max_{|n|≥2} ≤ 1/\cosh(\log 2) = 4/5 < \sqrt7/3`.*

The comparison of record is then the following, with the arithmetic column
imported verbatim from §19 (`s_1 = s(γ_1,π/2) = 0.99846016271880910923…`,
`1−s_1^2 = 3.0773…×10^{−3}`, `d_0^{\mathrm{arith}} = 324.9598266…`) and not
re-derived.

|  | arithmetic (`ξ`) | model (`E/F_2`, `a = −1`) |
|---|---|---|
| `s(γ_1,0)` | `1` | `1` |
| `s(γ_1,π/2)` | `0.99846016271880910923` | `\sqrt7/3 = 0.881917103688` (**exact**) |
| `\min_θ s(γ_1,θ)` | `= s_1` — the optimum **is** at `π/2` | `s_C^* = \sqrt{7/11} = 0.797724035217` at `\tan θ^* = 2/\sqrt7` |
| `1 − \min_θ s` | `1.5398×10^{−3}` | `2.0228×10^{−1}` (**131.4×** larger) |
| `d_0 = (1−(\min_θ s)^2)^{−1}` | `324.9598266…` | `11/4` (**exact**) |
| minimal integer witness degree | `d = 325` | **`d = 3`** (`d = 5` at `θ = π/2`) |
| the Riemann hypothesis | `OPEN` | **TRUE** (Weil, **(X27)**) |

The third row is the apples-to-apples comparison, and the two columns differ
there for a reason that is pure discreteness: **arithmetically `θ = π/2` is the
optimum**, because on the line the nearest peak of `|\cos(γ_1u+θ)|` to `u = 0`
sits at `|u| ≤ π/(2γ_1)` and pushing it as far from `u = 0` as possible — where
`\cosh(u/2)` is largest — is exactly `θ = π/2`; **on the lattice it is not**,
because `n = 0` is a sample point contributing `|\cos θ|`, which `θ = π/2` sends
to `0` while pushing the `n = ±1` entries up, so the optimum balances them
instead.

**Theorem 21.14 (the witness in the model; `PROVED`).**  Fix `χ ∈ R` and a
degree `d` with `d^2(1−s_C^2) > d − 4χ`, where `s_C = s_C(γ_1,θ)` is the
constant in the chosen direction `θ`.  Let `F_0 ∈ D^W_C` be the class, unique
modulo `𝓝^C_∞`, with coordinates `(a,b,x,y) = (0,0,0,1)` in (21.8) — primitive,
with `−I_∞^C(F_0,F_0) = 2`.  Pick `t` with
`½s_Cd < t < ½\sqrt{d(d−1)+4χ}`, a nonempty interval by the displayed
inequality, and put `E := tF_0 + dκ_C`.  Then `\deg E = d`,
`R(E) := ½I_∞^C(E,E) − ¼\deg E + χ > 0`, and **there is no `E' ∈ 𝓔_C` with
`E − E' ∈ 𝓝^C_∞`.**  Hence clause `(b′)⁺` is false in the model, at every `χ`.

*Proof.*  By Theorem 21.20(iii),(iv) the class `κ_C` has coordinates
`(½,½,0,0)`, so `E` has coordinates `(d/2,d/2,0,t)`.  Hence `\deg E = d` and, by
(21.8), `I_∞^C(E,E) = d^2/2 − 2t^2`, so
`R(E) = d^2/4 − t^2 − d/4 + χ > 0` by the upper bound on `t`.  Suppose
`E' ∈ 𝓔_C` with `E−E' ∈ 𝓝^C_∞`.  By Theorem 21.8 the radical is the common
kernel of the polar and zero evaluations, so `\deg E' = \deg E = d` and
`Φ_{E'}(ρ_1) = Φ_E(ρ_1)`, whose component in the direction `θ` has modulus `t`.
Then `|\mathrm{Re}(e^{iθ}Φ_{E'}(ρ_1))| = t > ½s_Cd = ½s_C\deg E'`, contradicting
Lemma 21.11.  ∎  `PROVED`

*Certified instance, the witness of record (`χ = 0`, `θ = θ^*`,
`s = s_C^* = \sqrt{7/11}`, `d_0^* = 11/4`; `sC_and_points.py` §[8]).*  At
`d = 3 > 11/4` the admissible window is
`t ∈ (1.196586052963,\ 1.224744871392)`, of width `2.816×10^{−2}`; take
`t = 1.21`.  Then `\deg E = 3`, `I_∞^C(E,E) = 9/2 − 2t^2 = 1.5718`,
`R(E) = 0.0359 > 0`, and `|\mathrm{Re}(e^{iθ^*}Φ_E(ρ_1))| = 1.21 > 1.196586… =
½s_C^*\deg E` — violated — while the non-sharp bound `½\deg E = 1.5` is
satisfied.  *At the arithmetic direction (`χ = 0`, `θ = π/2`, script §[3]),
`d = 5` already suffices (window `(2.204792759,\ 2.236067977)`), and at `d = 6`
the window is `(2.645751311065,\ 2.738612787526)`; taking
`t = 2.692182049295` gives `I_∞^C(E,E) = 3.504311626905 > 3 = ½\deg E`,
`R(E) = 0.252155813453 > 0` and `|\mathrm{Im}\,Φ_E(ρ_1)| = 2.692182… >
2.645751… = ½s_C\deg E`, margin `4.64×10^{−2}` — the arithmetic witness's exact
profile, at degree `6` instead of `400`.*

**Theorem 21.15 (the frame defect theorem holds on the curve; `PROVED`).**
There is **no** function `h⁰ : D^W_C → R_{≥0}` satisfying clauses (a), (b′), (c)
of Theorem 12.3 — with `K := κ_C`, the effective cone `𝓔_C`, and the radical
`𝓝^C_∞` — for any `χ ∈ R`.

*Proof.*  The three steps of §19 transcribe with no change.  *Step 1.*  If
`h⁰(E) > 0` then (b′) supplies `E' ∈ 𝓔_C` with `E−E' ∈ 𝓝^C_∞`, whence
`\deg E = \deg E' > 0` by Theorem 21.9(i) and Theorem 21.8; so `h⁰` vanishes on
every class of degree `≤ 0`.  *Step 2.*  `\deg κ_C = 1` by Theorem 21.20(iii),
so `\deg(κ_C−E) = 1−\deg E < 0` for `\deg E > 1`, hence `h⁰(κ_C−E) = 0` by
Step 1, and (c) together with the Serre symmetry `R(κ_C−E) = R(E)` gives
`h⁰(E) ≥ R(E)`.  *Step 3.*  Take the witness `E` of Theorem 21.14 at any degree
`d > \max(1, \cdot)` with `d^2(1−s_C^2) > d−4χ` — by Proposition 21.13 the
threshold is `d_0^* = 11/4`, so `d = 3` serves.  Then `h⁰(E) ≥ R(E) > 0`, so
(b′) supplies `E' ∈ 𝓔_C` with `E−E' ∈ 𝓝^C_∞`, which Theorem 21.14 forbids.  ∎
`PROVED`

**Theorem 21.16 (the geometric `h⁰` satisfies (a),(b′),(c); `CLASSICAL`).**  For
an integral divisor `D` on `S = C×C` put `h⁰_C(D) := \dim_k H^0(S, 𝒪(D))`.  Then
 (a) `h⁰_C ≥ 0`;
 (b′) `h⁰_C(D) > 0 ⟹ D ∼ D'` with `D' ≥ 0` effective and `D' ≢ 0` if `D ≢ 0` —
   because `h⁰` counts sections and a nonzero section `σ` gives the effective
   divisor `\mathrm{div}(σ)+D`;
 (c) `h⁰_C(D) + h⁰_C(K_S−D) ≥ χ(𝒪(D)) = ½D·(D−K_S) + χ(𝒪_S)`, with
   `K_S = (2g−2)(F_1+F_2)` and `χ(𝒪_S) = (1−g)^2`.
Both are **(X28)** (Riemann–Roch for surfaces and Serre duality
`h^2(D) = h^0(K_S−D)`), and Weil's proof of the Riemann hypothesis for `C` is
Theorem 12.3 run on `(h⁰_C, \mathrm{Eff}(S), K_S, χ = (1−g)^2)`, i.e. the Hodge
index theorem with `H = F_1+F_2`.  `CLASSICAL`

**Remark 21.16a (the three substitutions, and which one bites).**  Exactly three
things separate Theorem 21.16 from the frame's Theorem 12.3, and the model says
which matters.

| | the frame (§12.2), in the model | geometry (Theorem 21.16) | does the difference bite? |
|---|---|---|---|
| the cone in (b′) | `𝓔_C = \mathrm{Cone}\{γ_n\}` | `\mathrm{Eff}(C×C)` | **yes — this is the whole gap** |
| the class `K` | `κ_C`, `\deg κ_C = 1`, `≡ ½(F_1+F_2)`: **half the ample class** | `K_S`, the true canonical class | **no** — Theorem 12.3's proof uses only `\deg K > 0` and the Serre symmetry `R(K−E) = R(E)`, bilinear bookkeeping valid for any `K`; Theorem 21.15 is proved with `κ_C` and would be proved the same way with `K_S` |
| `χ` | any `χ ∈ R` | `(1−g)^2` | **no** — Theorem 21.14 quantifies over every `χ`, which shifts `R` by a constant while the gap grows like `d^2(1−s_C^2)` |

**Consequence of record.**  Theorem 21.15 holds in a case where the Riemann
hypothesis is a theorem, where `h⁰` exists, and where every clause of
Theorem 21.16 is satisfied by it.  Therefore `s < 1` is a property of the
**cone** — of how far `𝓔` falls short of the effective cone of a surface — and
**not** a property of the zeros, and **not** the numerical signature of a
missing sections functor.  What separates the two situations is not the
function but the cone in which `(b′)` is asked to find a representative.

### 21.4 The cones

**Theorem 21.17 (the two cones and the exact gap; `PROVED` for `g = 1`).**
Work in `V_C` with the coordinates (21.8) and `g = 1`, and define the support
function in the direction `θ` by

    σ_θ(𝒞) := \sup\Big\{\frac{|\mathrm{Re}(e^{iθ}Φ_D(ρ_1))|}{\deg D}\ :\ D ∈ 𝒞,\ \deg D > 0\Big\} ,

writing `σ := σ_{π/2}`, so that `σ(𝒞) = \sup\{|y_D|/\deg D\}`.  Then:
 (i) **the pointwise, i.e. Frobenius-graph, cone.**  `σ(𝓔_C) = ½\,s_C(γ_1,π/2)`,
   attained at `D = γ_{\pm1}`; for the curve of record
   `= \sqrt7/6 = 0.440958551844`;
 (ii) **the positive cone** `\mathrm{Pos} := \{D·D ≥ 0,\ D·H > 0\}` has
   `σ(\mathrm{Pos}) = ½`, attained on the boundary classes `D = (c,c,0,\pm c)`
   with `D·D = 0`, `\deg D = 2c`;
 (iii) **the section cone.**  `\overline{\mathrm{Eff}}(C×C) = \overline{\mathrm{Pos}}`,
   hence `σ(\overline{\mathrm{Eff}}) = ½`: **the analogue of `s₁` is `1`**;
 (iv) therefore `𝓔_C ⊊ \mathrm{Eff}(C×C)_R ∩ V_C` **strictly**, with

       \frac{σ_θ(𝓔_C)}{σ_θ(\overline{\mathrm{Eff}})} = s_C(γ_1,θ)\ \text{ in each direction }θ,
       \qquad \min_θ\ \text{ratio} = s_C^* = \sqrt{7/11} = 0.797724… < 1 ,

   the ratio at the arithmetic direction `θ = π/2` being `\sqrt7/3 = 0.881917…`;
 (v) **the gap is witnessed by a single explicit class.**  For `E ∈ 𝓔_C`,
   `E ≢ 0`, both `Φ_E(0) > 0` and `Φ_E(1) > 0`, each being `Σ_nE(n)q^{∓n/2}` with
   `E ≥ 0`, `E ≢ 0`.  But `F_1·F_1 = 0`, i.e. `Φ(0) = 0` for `F_1`.  So
   **`F_1 ∈ \mathrm{Eff} ∖ 𝓔_C`**, and `F_1` is in the image of the dictionary.

*Proof.*  (i) On the extreme rays `δ_n` of Theorem 21.9(iii) the functional is
`|y_{γ_n}|/\deg δ_n = |\sin(nθ_u)|/(2\cosh(n\log q/2))`, and the supremum of a
linear functional over a cone is attained on its extreme rays; by (21.9) with
`θ = π/2` this is `½s_C(γ_1,π/2)`, and the supremum here **is** attained,
because `|\sin(nθ_u)|/2\cosh(n\log q/2) → 0`.  (ii) Maximise `|y|/(a+b)` subject
to `ab ≥ x^2+y^2`: put `x = 0` and `y^2 = ab`; then `\sqrt{ab}/(a+b) ≤ ½` by
AM–GM, with equality iff `a = b`.  (iii) *Lower bound* (`\overline{\mathrm{Pos}}
⊆ \overline{\mathrm{Eff}}`): a class with `D^2 > 0`, `D·H > 0` is big, so `nD`
is effective for `n ≫ 0` — **(X28)**.  *Upper bound*
(`\overline{\mathrm{Eff}} ⊆ \overline{\mathrm{Pos}}`): for `g = 1`,
`C×C = E×E` is an **abelian surface**, and on an abelian variety every effective
divisor is nef — `D` is algebraically equivalent to each translate `t_x^*D`, and
a generic translate meets any given irreducible curve properly, so `D·Γ ≥ 0` for
every curve `Γ`, in particular `D^2 ≥ 0` (**(X27)**, the theorem of the square).
Hence `\overline{\mathrm{Eff}} ⊆ \mathrm{Nef} ⊆ \overline{\mathrm{Pos}}`, and on
`\overline{\mathrm{Pos}}` the inequality `D^2 ≥ 0` reads `x^2+y^2 ≤ ab`, so
`|y_D| ≤ \sqrt{ab} ≤ ½(a+b) = ½\deg D`, the second step again AM–GM and
legitimate since `a,b ≥ 0` for nef `D`.  Combining the two bounds gives the
equality of closures and the value `½`, which is a supremum over big classes and
is **not attained** by an integral effective divisor, the extremal classes having
`D^2 = 0` and lying on the nef boundary.  (iv) is (i)–(iii) with (21.9) read in
the direction `θ`, and Proposition 21.13 for the minimum.  (v) is the displayed
computation; the dictionary image is exhibited in the script.  ∎  `PROVED`

*Certified (`sC_and_points.py` §[7]): a class `E_{F_1} ∈ D^W_C` supported on
`\{−1,0,1,2\}` with coefficients `(−0.353553,\ 0.250000,\ 0,\ 0.500000)` has
coordinates `(1,0,0,0)`, residual `2.2×10^{−16}` — and it has a **negative**
coefficient, which is exactly why `F_1 ∉ 𝓔_C`.  The same script recovers
`κ_C = (0.176777, 0.125, 0.176777, 0)` on that support, which is
`Λ_C/(2hq^{−1/2}) = (1,\ 1/\sqrt2,\ 1)/5.656854`, an independent confirmation of
Theorem 21.20.*

The upper bound in (iii) is `OPEN` for `g ≥ 2`: it needs `|y_D| ≤ ½\deg D` for
every effective `D`, and the Hodge-index estimate
`|y_D| ≤ \sqrt{(\tfrac12(\deg D)^2 − D^2)/2}` delivers `½\deg D` only when
`D^2 ≥ 0`; for `g ≥ 2` the surface has negative curves (`Δ^2 = 2−2g`,
`Γ_{q^n}^2 = q^n(2−2g)`), and **no claim is made there**.  The headline "the
analogue of `s₁` is `1`" is established **for `g = 1`**, which is the certified
case and all the comparison uses.

So the frame's cone is a **moment cone** — the image of the nonnegative measures
on the lattice under finitely many evaluations — while the model's is the
effective cone of a surface, which *fills* the positive cone.  The deficit is
`20.2\%` in the model against `0.15\%` arithmetically, and the two cones agree
nowhere near the boundary.

**Adjoining the rulings does not help.**  `\mathrm{Cone}(𝓔_C ∪ \{F_1,F_2\})` has
the same `σ` as `𝓔_C`, because `σ` of a cone is the maximum over its generators
and `F_1,F_2` have `y = 0`: adjoining the rulings adds degree without adding
`|y|`.  `PROVED`, and it retires the obvious first repair — only a bigness
mechanism closes the gap.

**Definition 21.18 (the model trace cone).**  Put `g_C := δ_0`, which is
admissible in the sense of §20 (real, even, `≥ 0`, `≢ 0`,
`Φ_{g_C}(0) = Φ_{g_C}(1) = 1 > 0`, and `Φ_{g_C}(1−ρ_i) = 1 ≠ 0` at every zero),
and

    t_n^C(E) := I_∞^C(E, τ_n g_C) = I_∞^C(E, δ_n) = D_E·γ_n ,\qquad
    B4_C := \{E : t_n^C(E) ≥ 0\ ∀n ∈ Z\} .

**Theorem 21.19 (the Frobenius-nef cone; `PROVED`).**
 (i) `B4_C = 𝓔_C^{∨}` exactly — the dual cone of the pointwise cone with respect
   to `I_∞^C`; geometrically, the cone of classes pairing nonnegatively with
   every Frobenius graph.  It is `𝓝^C_∞`-saturated and contains `𝓝^C_∞`.
 (ii) `B4_C ⊇ \mathrm{Nef}(C×C) ∩ V_C`, since every `γ_n` is effective; and
   `B4_C ⊉ \mathrm{Eff}(C×C) ∩ V_C` for `g ≥ 2`, since
   `γ_n·γ_n = κ(0) = 2−2g < 0`.  So `B4_C` is **neither** the section cone
   **nor** the pointwise cone: it is a *Frobenius-nef* cone, strictly between
   nef and everything.
 (iii) `𝓔_C ⊆ B4_C ⟺ κ(n) ≥ 0\ ∀n ⟺ N_0 = 2−2g ≥ 0 ⟺ g ≤ 1`.  For `g = 1` the
   containment holds and is exactly the positivity of the point counts
   `N_m ≥ 0`; for `g ≥ 2` it fails at `n = 0`.
 (iv) The Gram of the generators of `𝓔_C` is
   `γ_a·γ_b = q^{−|a−b|/2}N_{|a−b|}`, the point counts, and
   `Z_C(T) = \exp(Σ_mN_mT^m/m) = ∏_v(1−T^{\deg v})^{−1}` is the Euler product.
   So: *the Euler product is precisely the statement that the Gram matrix of the
   frame's effective cone is given by the intersection numbers of the Frobenius
   graphs with each other.*  The section cone's extra generators — the fibres
   over closed points, and the members of `|nD|` for `D` big — are **not**
   Euler-product data.

*Proof.*  (i) `t_n^C(E) = D_E·γ_n` by Theorem 21.7(ii),(iii), and a cone's dual
is cut out by its generators, which are the `δ_n` by Theorem 21.9(iii);
saturation is immediate since the radical pairs to zero.  (ii),(iii) follow from
(21.1) and the Lefschetz relations with `κ(0) = 2−2g`, the sign of which is the
only obstruction to `κ ≥ 0` — every `N_m` with `m ≥ 1` is a point count and
hence `≥ 0`.  (iv) is the definition of `Z_C` together with (i) and
Theorem 21.7(i).  ∎  `PROVED`

The curve of record has `g = 1` and so sits on the side `𝓔_C ⊆ B4_C`, whereas
**arithmetically `𝓔 ⊄ B4`** (§20, the density `w_g` not being of one sign).  The
`g = 1` model is therefore **not faithful** to the arithmetic trace-cone
geometry, and no inference about `B4` may be drawn from it; certifying a `g ≥ 2`
instance is `OPEN`.  Nothing else in this section uses `B4_C`.

### 21.5 The class `K`, and a correction of record

**Theorem 21.20 (the model's canonical class; `PROVED`).**  Let
`K_C ∈ D^W_C` be the finitely supported class with `K_C(n) := k_n`, the
coefficients of `Λ_C(z) = Σ_{n=−g}^{g}k_nz^n` (so `k_{−n} = k_n`,
`k_{\pm g} = 1`).  Then:
 (i) `Φ_{K_C} = ξ_C`, `\mathrm{supp}\,K_C ⊆ \{−g,\dots,g\}`, and
   `Φ_{K_C}(ρ_i) = Φ_{K_C}(1−ρ_i) = 0` for every `i`;
 (ii) `Φ_{K_C}(0) = Φ_{K_C}(1) = h\,q^{−g/2}` and `\deg K_C = 2h\,q^{−g/2}`;
 (iii) with the frame normalization `κ_C := \dfrac{q^{g/2}}{2h}K_C` one has
   `\deg κ_C = 1`, `I_∞^C(F,κ_C) = ½\deg F` for every `F ∈ D^W_C`, and
   `I_∞^C(κ_C,κ_C) = ½` — **Theorem 11.8 verbatim**;
 (iv) `D_{κ_C} ≡ ½(F_1+F_2)` in `V_C`: `κ_C` **is** the class the frame calls
   `½(e_-+e_+)`;
 (v) `I_∞^C(κ_C,κ_C) = ½` while `K_{C×C}^2 = 2(2g−2)^2`: **the frame's `K` is
   not the canonical class of the surface.  It is half the ample ruling class
   `H = F_1+F_2`.**

*Proof.*  (i) and (ii) are Lemma 21.2 and the definition of `k_n`.  (iii) In
(21.6) with `F` arbitrary and `E = κ_C`, the zero sum drops because
`Φ_{κ_C}(1−ρ_i) = 0` by (i) and Lemma 21.2's symmetry, leaving
`Φ_{κ_C}(0)(Φ_F(0)+Φ_F(1))`, which is `½\deg F` by (ii) and the normalization;
taking `F = κ_C` gives `½·1 = ½`.  (iv) A class of `V_C` is determined modulo the
radical by its pairings with `F_1`, `F_2` and the zero block; by (ii),(i) and
Theorem 21.7(iii) those are `(½,½,0)` for `κ_C`, and by (21.1) they are `(½,½,0)`
for `½(F_1+F_2)` as well.  (v) `2(2g−2)^2 = ½` has no solution in integers `g`.  ∎
`PROVED`

**Correction of record (the name of `K`).**  The frame's `K` — arithmetically
the Pólya class of Theorem 11.7, with `Φ_K = ξ`, `\deg K = 1`,
`I_∞(K,K) = ½` — has been called the *canonical class* throughout Part II.  The
model shows that this name is wrong, and says what the object is instead: under
the dictionary it is `½(F_1+F_2)`, **half the ample ruling class**, whereas the
canonical class of the surface is `K_{C×C} = (2g−2)(F_1+F_2)`, with
`K_{C×C}^2 = 2(2g−2)^2 ≠ ½`.  The correction applies to the **arithmetic** frame
as well, by Proposition 14.1(i),(ii): there `M(K) = (½,½)` and
`β_T(M(F),M(K)) = ½\deg F`, which is the pairing profile of `½(e_++e_-)` and of
nothing else.  Everything proved about `K` stands — Theorem 12.3 consumes only
`\deg K > 0`, the Serre symmetry `R(K−E) = R(E)`, and ampleness — but the frame
has an **ample class where geometry has a canonical class**, and correspondingly
its `h^2` is "vanishing in degree `≤ 0`" rather than Serre duality.  Whether
adjoining a genuine `h^2` with `h^2(E) = h^0(K−E)` for a *true* canonical class
changes anything is `OPEN`; by Remark 21.16a it does not bite for the defect
theorem.

**Remark 21.20a (`K_C ≥ 0` is false in general; `PROVED` negative).**
Theorem 11.7(i) proves `K > 0` arithmetically from Pólya's kernel (import
(X12)).  **There is no model analogue.**  `K_C` is the coefficient sequence of
the **numerator** `Λ_C`, not of `Z_C`, so nonnegativity of the point counts is
no argument.  For `g = 1`, `Λ_C(z) = z + k_0 + z^{−1}` with
`k_0 = −(u+\bar u) = −a/\sqrt q` and `a = q+1−N_1`, so

    K_C ≥ 0 \iff a ≤ 0 \iff N_1 ≥ q+1 ,

which fails for a positive proportion of curves.  *Certified
(`sC_and_points.py` §[4]) for all `12` isogeny classes of elliptic curves over
`F_2` and `F_3` (`5` over `F_2`, `a = −2..2`; `7` over `F_3`, `a = −3..3`):
nonnegative exactly for `a ≤ 0`, negative for `a = +1,+2` over `F_2` and
`a = +1,+2,+3` over `F_3`.  Example: `E/F_2` with `N_1 = 1` has
`k_0 = −\sqrt2 < 0`.*  The equivalence displayed is a `g = 1` statement — it is
the sign of the single interior coefficient — and for `g ≥ 2` the `k_n` are, up
to sign, elementary symmetric functions of the `u_i` and no such equivalence is
proved; what survives at every `g` is the negative itself.  Nothing in this
section uses `K_C ≥ 0`: the frame needs only `\deg κ_C = 1` and ampleness, and
ampleness comes from Theorem 21.9(i).  The positivity axiom of §18 still holds
in the model for `g = 1`, since
`Λ_C(x) = x+k_0+x^{−1} ≥ 2 − |a|/\sqrt q > 0` for `x > 0` because
`|a| ≤ 2\sqrt q` with equality only in the supersingular case.

### 21.6 Bigness is equivalent to the Riemann hypothesis

The bigness half of what geometry supplies — `D^2 > 0`, `D·H > 0 ⟹ D` big — is
the operative ingredient of Theorem 21.16, and the obvious move is to demand it
of an enlarged arithmetic cone.  That move is not available.

**Proposition 21.21 (the bigness clause is `RH`; `PROVED` + `RESTATEMENT`, frame-internal).**
Let `𝔈 ⊆ D^W` be a **closed** convex cone, `𝓝_∞`-saturated, with `𝓔 ⊆ 𝔈`,
satisfying the **degree gate**

    (4b)\qquad E ∈ 𝔈,\ E ∉ 𝓝_∞ \ \Longrightarrow\ \deg E > 0                  (21.12)

— the property Theorem 12.3 Step 4 actually consumes (Theorem 11.13(i)).  Then

    \textbf{(4)}\quad I_∞(D,D) > 0 \ \text{and}\ \deg D > 0 \ \Longrightarrow\ D ∈ 𝔈
    \qquad\Longleftrightarrow\qquad \textbf{RH} .

*Proof.*  **(⟹)**  By contraposition.  Suppose RH fails.  By Paper 45
Theorem 10.4 there is a primitive real `P ∈ C_c^∞(R)`, `P ∉ 𝓝_∞`, with
`q := I_∞(P,P) > 0`.  By Theorem 11.8, `I_∞(P,K) = ½\deg P = 0` and
`I_∞(K,K) = ½`, and `\deg K = 1`.  For every `ε > 0`,

    \deg(P+εK) = ε\deg K = ε > 0,\qquad I_∞(P+εK,P+εK) = q + 2ε·0 + ε^2/2 > 0 ,

so clause (4) places `P+εK ∈ 𝔈`.  Letting `ε ↓ 0` and using that `𝔈` is closed
gives `P ∈ 𝔈`, while `\deg P = 0` and `P ∉ 𝓝_∞` — so the gate (21.12) fails.

**(⟸)**  Assume RH, and let `D` lie in the closed positive cone with
`\deg D = 0`.  Then `Φ_D(0)+Φ_D(1) = 0`, and `I_∞(D,D) ≥ 0` together with (11.6)
forces `Φ_D(0)Φ_D(1) ≥ Σ_ρ|Φ_D(ρ)|^2 ≥ 0`; a pair of reals with zero sum and
nonnegative product is a pair of zeros, so `Φ_D(0) = Φ_D(1) = 0` and `D` is
primitive.  Now (11.6) with `1−ρ = \barρ` — which is where RH enters — gives
`I_∞(D,D) = −Σ_ρ|Φ_D(ρ)|^2 ≤ 0`; combined with `I_∞(D,D) ≥ 0` this forces
`Φ_D(ρ) = 0` at every zero, hence `D ∈ 𝓝_∞` by Theorem 11.11.  So the cone
`𝔈 := \overline{\overline{\mathrm{Pos}} + 𝓔}` satisfies both (21.12) — every
class it contains outside `𝓝_∞` has positive degree, by the estimate just made,
which survives the closure — and clause (4), which holds for it by
construction.  ∎  `PROVED`

**Consequences, stated bluntly.**
* **The bigness clause is withdrawn as a target.**  Asking a later construction
  to supply a cone with clause (4) and the gate (21.12) is asking it to prove
  RH; asking for clause (4) without the gate is vacuous, since `𝔈 := D^W`
  satisfies it.  Neither is a construction problem.
* **The model is not thereby circular.**  In geometry bigness is a *theorem* —
  Riemann–Roch on the square, `h^2`-vanishing by Serre duality against an ample
  class, and `χ(mD) → ∞` — and Weil's proof derives it rather than assuming it.
  What may legitimately be asked for is the **mechanism**, never the clause.
* Two further defects of the naive form are worth recording, because the
  corrected statement below repairs both: clause (4) as usually written
  concludes `D ∈ \overline{𝔈}`, a closure, where `(b′)` needs an **actual**
  element — **(X28)** gives `nD` effective, i.e. `D ∈ 𝔈⊗Q`, which is the correct
  form; and it omits the bounded-density constant `C_F < ∞` of
  Theorem 11.14(ii), which Theorem 12.3 Steps 1–2 need for ampleness against the
  enlarged cone and which over `\mathrm{Pos}` is itself a signature statement.

### 21.7 The named ingredient: the frame has `⋆` and no `+`

**Proposition 21.22 (the structure of `NS(E×E)`; `IMPORTED`).**  For an elliptic
curve `E/F_q` with Frobenius `π`, `NS(E×E)_R` is spanned by `F_1`, `F_2` and the
graph classes `Γ_α`, `α ∈ \mathrm{End}(E) = Z[π]`, with

    Γ_α·F_1 = 1,\qquad Γ_α·F_2 = \deg α,\qquad Γ_α·Γ_β = \deg(α−β) .          (21.13)

This is **(X27)** (Tate's theorem, with
`\mathrm{rk}\,NS(A×B) = \mathrm{rk}\,NS(A)+\mathrm{rk}\,NS(B)+\mathrm{rk}\,\mathrm{Hom}(A,B)`,
and the degree form on `\mathrm{End}`).  `IMPORTED`

**Remark 21.23 (what the frame keeps, and what it loses).**  The frame's Gram of
Theorem 21.7(i) is the special case `α = π^a`, `β = π^b` of (21.13), since
`N_m = \deg(1−π^m)`: the cone `𝓔_C` is the cone on the **multiplicative
semigroup** `\{π^n\}` and its transposes `\{\barπ^n\}`, and **nothing else**.
The missing effective classes are exactly the graphs `Γ_{m+nπ}` of the **sums**,
which are not nonnegative combinations of the `Γ_{π^k}`, together with the
fibres.  Equivalently, and this is the sharpest form of the finding: the frame
keeps `\mathrm{Frob}_m ⋆ \mathrm{Frob}_n = \mathrm{Frob}_{mn}` (Paper 44
Theorem 3ter.4(i)) and **has no `+`**.  This is the same gap as
`F_1 ∈ \mathrm{Eff} ∖ 𝓔_C` (Theorem 21.17(v)), stated in the form that can be
acted on.

For `g = 1` the whole of "bigness" is then elementary.  By Theorem 21.17(iii),
`\overline{\mathrm{Eff}} = \overline{\mathrm{Pos}}` — "the analogue of `s₁` is
`1`" — and under (21.13) that statement **is** the positive-semidefiniteness of
the norm form

    \deg(m+nπ) = m^2 + amn + qn^2 \qquad \text{on } Z[π] ,                    (21.14)

whose discriminant condition `a^2−4q ≤ 0` is the Riemann hypothesis for `C`.  Two
things follow that bear on the arithmetic frame.  First, `\deg(m+nπ)` is a
**count** — `\#\ker(m+nπ)` — and not a dimension: a mechanism of that type
supplies the conclusion of Theorem 12.3's clause (b′) without any `h^0`, any
`𝒪(D)` and any cohomology, and so sidesteps the two standing no-gos (no `h⁰`
defined on the carrier can satisfy a Riemann–Roch identity with a nonconstant
degree term; and the imported rank-one dimension theory carries no signature)
rather than fighting them.  Second, the Gram already determines the form:
`a = q+1−N_1` is read off `κ(1) = q^{−1/2}N_1`, so **the Euler product already
contains the form, and only its positivity — the count — is missing**.

**The named obstruction to transport.**  The diagonal entry of the model Gram is
`κ(0) = Δ·Δ = 2−2g`, which tends to `−∞` with the genus.  Arithmetically this is
exactly the divergence already on the record in two independent places:
`I_A(\mathrm{Frob}_n,\mathrm{Frob}_n)` **does not exist** (Paper 44
Remark 8bis.1c), and `τ_{\log n}(ΠK) ∈ 𝓝_∞` for every `n`
(Proposition 14.2) — the Frobenius family sits against the radical, where in the
model `γ_n·γ_n` is a finite number and `γ_n` is an extreme ray of the cone.  The
model supplies the missing interpretation of that divergence: **the arithmetic
curve has infinite genus**, and the value the diagonal is trying to take is
`2−2g`.  Any transport of (21.14) must therefore be a *difference-only* form —
`Γ_α·Γ_β = \deg(α−β)`, whose diagonal has been subtracted — or must carry an
explicit `2−2g` counterterm.

Two warnings belong with this, because both are already proved above.  The
positivity of (21.14) is a theorem on an elliptic curve **because it counts a
kernel**; the corresponding arithmetic statement, "the degree form on
`Z[\mathrm{Frob}]` is positive semidefinite", is Weil positivity, i.e. RH, and
Proposition 21.21 applies to it verbatim — such a construction must deliver the
*count*, never the positivity.  And `g = 1` is degenerate twice over: as
`g → ∞`, not only does `Δ·Δ = 2−2g` diverge, but the rank of the endomorphism
module grows and the elementary norm form is replaced by Rosati positivity
`\mathrm{Tr}(f f^†) > 0` on `\mathrm{End}(\mathrm{Jac})⊗Q`.  The elliptic case
is a control on the *shape* of an argument, not on its difficulty.

### 21.8 What the model does not model, and what remains open

**Eleven mismatches.**  The model was run as a solved case: every statement
transcribed had to come out true about the curve, and every place where the
transcription broke was recorded.  Eleven places broke.  None of them is used in
the proof of Theorem 21.15.

| # | the mismatch |
|---|---|
| 1 | **The completion is not the frame's.**  The polar factor is `(1−q^{−s})(1−q^{1−s})` — periodic, with zeros at `\{0,1\}` *modulo the period* — and the `Γ`-factor is replaced by `q^{(g−1)s}`.  §18's axiom on admissible elementary factors must have `½s(s−1)` widened to `(1−q^{−s})(1−q^{1−s})` to cover the model; with that edit it holds, since `Z_C(T) = Σ_nA_nT^n` with `A_n` the number of effective divisors of degree `n` |
| 2 | **No smoothness.**  No `C²`, no two derivatives, no `(E3d)`: the zero sum has `2g` terms.  Consequence: the carrier contains the point masses `δ_m`, which are the extreme rays of `𝓔_C`; arithmetically `δ_a ∉ D^W` and `𝓔` has no extreme ray inside `D^W` at all |
| 3 | **Periodicity collapses the rank.**  `\dim_R D^W_C/𝓝^C_∞ = 2+2g`, finite, against the infinite-rank radical quotient of Theorem 11.11.  Every construction here is finite linear algebra |
| 4 | **Degree is unchanged.**  `\deg E = Σ_nE(n)2\cosh(n\log q/2)`: the one place where discreteness changes nothing, and the reason `s_C` has a closed form |
| 5 | **No archimedean place.**  The whole archimedean side is the single term `κ(0) = 2−2g = χ_{\mathrm{top}}(C)`.  `F` is a function field: all its places are finite.  So the model gives **no guidance** on open item (21) of §14.5 (the kernel representation of `ω_∞` on `D^W`) — that item is not a model artefact but precisely a point at which the arithmetic frame has structure the model lacks |
| 6 | **The rulings are honest classes.**  `F_1,F_2 ∈ V_C` with `F_1·F_2 = 1`, so `K ≡ ½(e_++e_-)` is an identity of *classes* here, while arithmetically `e_∓` are the radical of the boundary form (Paper 43 Theorem 9.14c; Proposition 14.1(iv)).  The single most load-bearing difference |
| 7 | **`K_C ≥ 0` is false in general** (Remark 21.20a), so Theorem 11.7(i) has no model analogue |
| 8 | **Ample where geometry has canonical.**  The frame's `K` is `½(F_1+F_2)`, and its `h^2` is "vanishing in degree `≤ 0`", not Serre duality (§21.5) |
| 9 | **Admissibility is automatic.**  The genericity condition on test classes that is a Baire statement arithmetically is satisfied outright by the point mass `δ_0`; the warning that `K` is maximally inadmissible transcribes unchanged, `Φ_{κ_C}(1−ρ_i) = 0` at all `2g` zeros |
| 10 | **The trace index set is additive.**  Arithmetically the trace index runs over the multiplicative semigroup `N`, giving a Dirichlet series; here it runs over `Z` additively (`q^n`), giving a Laurent series with `2g+2` poles.  The trace-cone *method* does not transcribe; its *object* does |
| 11 | **The lattice moves the optimal direction off `π/2`.**  On the line `θ = π/2` **is** the optimum; on the lattice it is not, because `n = 0` is a sample point contributing `|\cos θ|` (Proposition 21.13 and the table in §21.3).  A pure discreteness effect, and the reason the honest comparison is `131.4×` rather than `76.7×` |

**The axioms do not separate the model from `ξ`.**  Checked against the list
A1–A9 of §18, with mismatch 1's editorial widening of A4's elementary-factor
list: `ξ_C` satisfies A1, A2, A2⁺, A3 (`θ_P = ½`), A4 (as widened), A5
(Theorem 21.5), A6, A7, A8 (the coefficients are point counts, `≥ 0`) and A9 —
**the same row as `ξ`**, with "Hodge index" **TRUE** instead of `OPEN`.  The
separating feature is therefore not an axiom about the function.  It is
structural, and it is exactly this: *the Frobenius correspondence is a genuine
morphism of a genuine surface*, so that `\mathrm{Div}(C×C)` is a free abelian
group on **prime divisors** — subvarieties — and "effective" means nonnegative
integer coefficients on that basis.  Three consequences follow, each of which the
arithmetic frame lacks: closed points exist, hence the rulings exist as effective
divisors (Theorem 21.17(v)); sections and divisors live in different categories,
so that the divisor map is scaling-invariant by construction, which the frame
cannot arrange inside a single linear space; and bigness is a theorem about sheaf
cohomology, of which the frame has the `χ`-side (`R(E)`, unconditional) and a
surrogate `h^2`-vanishing but no mechanism converting them into membership of the
cone, there being no sheaf, no `𝒪(D)` and no space of sections to be nonzero.

**Open (P145′) — the mechanism.**  `OPEN`.  What may be asked for, in place of
the withdrawn bigness clause, is the mechanism that *proves* bigness for the
arithmetic frame — an arithmetic Riemann–Roch on the square.  Concretely,
construct `(𝔐, 𝔈, H^0, H^2)` with

1. **(carrier and form)** a `𝓝_∞`-saturated closed convex cone `𝔈 ⊆ 𝔐⊗R` and a
   map `ι : D^W → 𝔐⊗R` with `⟨ιE,ιF⟩ = I_∞(E,F)` and `ι(𝓔) ⊆ 𝔈`;
2. **(the named missing generators)** `e_-,e_+ ∈ 𝔈` with `⟨e_\pm,e_\pm⟩ = 0`,
   `⟨e_+,e_-⟩ = 1` and `ι(K) = ½(e_++e_-)`: the rulings leave the radical of the
   boundary form and become effective classes, as they are in the model
   (mismatch 6);
3. **(Frobenius)** `\mathrm{Frob}_n ↦` an element of `𝔈` for every `n`, with the
   Gram given by the weights `Λ(n)n^{−1/2}` of Paper 44 Theorem 3ter.10, so that
   the Frobenius sub-cone lies in `𝔈` and the Euler product is its Gram;
4. **the mechanism, in three separately checkable pieces:**
   * **(4a)** a functor `E ↦ H^0(E)` with `\dim H^0(E) < ∞`, a
     **scaling-invariant** divisor map `H^0(E)∖0 → 𝔈` with
     `E − \mathrm{div}(σ) ∈ 𝓝_∞`, and the conclusion in the form
     `⟨D,D⟩ > 0`, `\deg D > 0 ⟹ D ∈ 𝔈⊗Q` — **not** `\overline{𝔈}`;
   * **(4b)** the degree gate (21.12), Theorem 12.3 Step 4's input;
   * **(4c)** bounded density over the enlarged cone:
     `|I_∞(E,F)| ≤ C_F\deg E` for `E ∈ 𝔈` with `C_F < ∞`, i.e.
     Theorem 11.14(ii) extended from `𝓔` to `𝔈`, which Steps 1–2 need for
     ampleness;
5. **(falsifiers and uniformity)** the construction must **fail** for `Ξ_a`,
   where the Hodge index is false, and for `Ξ_Q`, where A7, A8, A9 all fail, and
   must be uniform in the number field.

**The equivalence of Proposition 21.21 is part of the problem statement**: the
bigness clause is RH, so the deliverable is (4a)+(4b)+(4c) *as constructions
with proofs*, and any attempt that assumes (4a)'s conclusion has proved nothing.
The trivial solution is excluded twice: `𝔈 = D^W` fails (4b) and supplies no
`H^0` for (4a).  By Theorem 21.17, clause 2 alone is provably insufficient.  What
supplies each piece in the model, and its arithmetic status, is the following.

| piece | in the model | arithmetic status |
|---|---|---|
| (4a) sections and bigness | `H^0(C×C,𝒪(D))`, rational functions on the **surface**, `\mathrm{div}` scaling-invariant by construction; bigness from Riemann–Roch (`χ(mD) = ½m^2D^2+O(m) → ∞`) plus Serre duality (`h^2(mD) = h^0(K_S−mD) = 0` once `\deg(mD) > \deg K_S`), giving `D ∈ \mathrm{Eff}⊗Q` — **(X28)** | **missing, and it is the whole problem**: no such `H^0` lives inside the carrier, and the available imported dimension theory is rank-one and signatureless.  The frame has the `χ`-side (`R(E)`, unconditional) and a surrogate `h^2`-vanishing, but no sheaf |
| (4b) degree gate | `D` effective, `D ≢ 0`, `H = F_1+F_2` ample `⟹ D·H > 0` | **present on `𝓔`** (Theorem 11.13(i)), and it is exactly what must be preserved under any enlargement — Proposition 21.21 shows an enlargement that keeps it and adds bigness is RH |
| (4c) bounded density | automatic: `NS(C×C)_R` is finite-dimensional and `H` ample | **present on `𝓔`** (Theorem 11.14(ii)); **unknown over any enlargement containing `\mathrm{Pos}`**, where it is itself a signature statement, and it may bind before (4a) |

Three further residues are `OPEN` and are recorded here: whether
`σ(\overline{\mathrm{Eff}}) = ½` for `g ≥ 2` (Theorem 21.17(iii) is a `g = 1`
theorem); the certification of a `g ≥ 2` instance, the curve of record sitting on
the wrong side of `𝓔_C ⊆ B4_C` (Theorem 21.19(iii)); and whether a model with an
**archimedean place** — a curve over `R`, or an Arakelov `C×C` — exists in which
the named ingredient can also be tested, which is the natural next falsifier and
the only route to any guidance on open item (21).

**Withdrawn in this section**

| claim | reason |
|---|---|
| "`s₁ < 1` is the exact numerical signature of the absence of a sections functor" (recorded in the repository at `R144_004`) | `s_C^* < 1` holds on a curve where the sections functor is **present** and the Riemann hypothesis is a theorem (Theorem 21.15).  `s < 1` is a signature of the **cone**, not of the absence of `h⁰`.  The mathematical content of `s₁ < 1` is untouched; only the diagnosis is withdrawn |
| "on a curve Riemann–Roch is a theorem, so the frame defect theorem will fail there" (the synthesis prediction of record) | It does not fail: Theorem 21.15.  Riemann–Roch on `C×C` is a theorem about a **different cone** (Remark 21.16a) |
| "one cannot run the refutation for a curve over `F_q` and watch it contradict Weil", on the ground that the function-field zeta is not admissible for this frame (the consistency remark accompanying §19's restatement) | One **can** run it; it does **not** contradict Weil; and the reason it does not is §21.3.  The frame is admissible on the lattice — mismatches 1–5 are the only edits, and none of them is used in the refutation.  The corresponding open item, whether a function-field model of `D^W` exists, is closed affirmatively by §21.1–§21.2 |
| the bigness clause `⟨D,D⟩ > 0`, `\deg D > 0 ⟹ D ∈ \overline{𝔈}` as a *target* for a later construction | It is RH restated for a closed `𝓝_∞`-saturated cone with the degree gate, and vacuous without the gate (Proposition 21.21).  Replaced by the mechanism (4a)+(4b)+(4c) |
| `σ(\overline{\mathrm{Eff}}) = ½` for every genus | Proved only for `g = 1`, via the abelian-surface argument of Theorem 21.17(iii); for `g ≥ 2` the surface has negative curves and the bound is `OPEN` |
| that the supremum defining `C_F` in Theorem 21.9(ii) is *attained* | False: `w_F(n)/2\cosh(n\log q/2)` tends to `Φ_F(0)` and `Φ_F(1)` at the two ends, and is identically `½` for `F = κ_C`.  Only finiteness is used, and it follows from (11.17) |

---

## 22. The degree form on `Z⟨Frob_n⟩` and the computed Frobenius diagonal

*Provenance note.  The material of this section is drawn from
`03-research/phase-146-row-d-coupled-pairing/`: `R146_001_ROUND1.md`
§§D.44–D.49 as repaired, `R146_003_ROUND2.md` §§D.47–D.49,
`R146_002_AUDIT.md`, `R146_004_CONFIRMATION.md`,
`CORPUS_CHECK_R146.md`, `CORPUS_CHECK_R146b.md`, and the closing decision
`R146_005_CLOSING_DECISION.md`, which fixes the labels used below.
Certified numerics come from `scripts/cosh_test_cmn.py` and
`scripts/tower_gram.py` in the same directory.*

Section 21 exhibited Weil's proof on a curve in the form in which it uses the
**ring** `Z[π]`: the endomorphism `m + nπ` is an object, its degree is the
cardinality of a kernel, and the resulting quadratic form is a norm form.  The
present section asks the corresponding question over `Spec Z`, where the
Frobenius family `\{Frob_n\}_{n ≥ 1}` of (1.5) is a commutative inverse
semigroup under `⋆` and nothing more.  Four things are proved.  A finite
symmetric form on the free `Z`-module `Z⟨Frob_n⟩` extending Paper 44's
off-diagonal Gram **exists**, for every finite diagonal, and is **not** a
count: it is degenerate against the count axiom and indefinite, with explicit
witnesses (§22.1).  It equals this paper's comparison identity with the zero
sum deleted, so it is **zero-blind** and uniform in the falsifier `Ξ_a`
(§22.2).  The elliptic model's additive identity transports, and the class it
produces passes the test of §19 **structurally**, that test being
non-detecting on this family by construction (§22.3).  The **diagonal**,
however, is not a convention: Paper 44 Theorem 8bis.1b computes it, its
archimedean part is `n`-independent and cancels exactly in differences, and
`P(m) = P(n)` forces `δ_m = δ_n` exactly at every `(ε,N)` and in both
conventions (§22.4).  On a single-prime tower this collapses every convention
into one real parameter and the Gram becomes an explicit Toeplitz form
(§22.5), whose off-diagonal reproduces the function-field model's `q^{\min}`
prefactor of §21 without adjustment, and whose sign carries no information
about `ξ` because it is a pure magnitude.  Finally, the reason none of this
assembles into Weil's argument is structural and is proved in §22.6: the
arithmetic Frobenius is a **translation**, not an endomorphism, and
`Spec Z` admits no ring of correspondences for it to live in.

Throughout, `P(n)` denotes the set of primes dividing `n`, `Λ` von Mangoldt's
function, and `S = \{∞\} ∪ S_f` a fixed finite chart as in (1.1).

### 22.1 Existence, and two obstructions to reading the form as a count

The model of §21 lives on the **un-normalized** side, where
`Γ_{q^a}·F_2 = q^a = \deg π^a`.  Paper 44's Frobenius carries instead the
half-density bidegree `M(Frob_n) = (n^{1/2},n^{−1/2})` (Theorem 3ter.6(iii)),
the degree having been absorbed.  The dictionary between the two is
`Γ_n^{un} = n^{1/2}·(\text{half-density class})`, so that

    \mathrm{bideg}(Γ_n^{un}) = (Φ(1),Φ(0)) = (n,1),\qquad
    \deg Γ_n^{un} = Φ(0)+Φ(1) = n+1 ,                                   (22.1)

matching `\deg Γ_{q^a} = 1+q^a` in the model.  All of §§22.1–22.3 is written
un-normalized.

**Definition 22.1 (the Euler-product data).**  For `m,n ≥ 1` put

    d_n := n ,
    L(m,n) := \min(m,n)·Λ\big(\max(m,n)/\min(m,n)\big)
            = \begin{cases}\min(m,n)\log p, & \max/\min = p^{k},\ k ≥ 1,\\
                           0, & \text{otherwise,}\end{cases}            (22.2)

and let `L(n,n) := δ_n` be a real parameter, the **diagonal counterterm**.

(22.2) is Paper 44 Theorem 8bis.1 with the correction K1, transported to
(22.1): the half-density entry is `Λ(\max/\min)(\min/\max)^{1/2}` times a
positive chart constant `c_N(m,n)`, and
`(mn)^{1/2}·Λ(\max/\min)(\min/\max)^{1/2} = \min·Λ(\max/\min)`.  The chart
constant is `c_N(m,n) = ∏_{s ∈ S_f∖(P(m)∩P(n))}((s−1)s^{N−1})^{−1}`; it is
positive, it depends on `(m,n)` through `P(m) ∩ P(n)`, and it does **not**
cancel out of the form, so no statement below about the numerical size of a
nonzero entry is convention-free.  What is convention-free is the
**vanishing** of an entry, and that is all §22.1's negatives use.

**Lemma 22.2 (the off-diagonal entries are Haar measures of fixed-point sets;
`PROVED-IN-REPOSITORY`).**  Let `p` be prime and `k ≥ 1`.  The fixed-point set
of `Frob_{p^k}` on `C_S` is the shell `\{|x|_S = p^{−k}\}` intersected with
the unit conditions of Paper 44 Definition 3ter.2, and its normalized Haar
measure in the Tate residue normalization is
`\mathrm{vol}(Z_p^×)·p^{−k/2}` times the half-density weight, with
`\mathrm{vol}(Z_p^×) = \log p` uniquely fixed by Paper 44 Theorem 8bis.8.
Hence `⟨Frob_{p^k},Δ⟩ = Λ(p^k)p^{−k/2}` exactly, with no limit and no
regularization at the finite places, and the general off-diagonal entry (22.2)
is `\min(m,n)` times the same measure taken at the ratio.  In particular every
off-diagonal entry is a nonnegative number produced by the measure of a
nonempty fixed set, and it **vanishes exactly when that set is empty**, i.e.
when `\max/\min` is not a prime power.

*Proof.*  Paper 44 Theorem 3ter.4(i) describes the fixed-point set of
`Frob_{p^k}` as the stated coset, Theorem 3ter.10 evaluates the contact term
as `Λ(p^k)p^{−k/2}`, and Theorem 8bis.8 fixes `\mathrm{vol}(Z_p^×) = \log p`
as the unique normalization compatible with the trace.  For `\max/\min` not a
prime power the coset is empty, so the measure is `0`.  Nothing is re-derived
here.  ∎  `PROVED-IN-REPOSITORY`

**Theorem 22.3 (existence and uniqueness of the difference form; `PROVED`).**
Set `⟨⟨Frob_m,Frob_n⟩⟩ := L(m,n)`, the Haar measure of the fixed-point set of
`Frob_m ⋆ Frob_n^†` (Lemma 22.2, with Paper 44's inverse-semigroup law
Theorems 3ter.4 and 3ter.7, the transpose being taken when `n ∤ m`).  Then for
every choice of real `(δ_n)` there is **exactly one** symmetric bilinear form
`B_δ` on `M := Z⟨Frob_n : n ≥ 1⟩` satisfying the model's defining relation
`Γ_α·Γ_β = q(α)+q(β)−2B(α,β)` with `q(Frob_n) = d_n`, namely

    B_δ(x,y) = Σ_{m,n}a_mb_n\,G(m,n),\qquad G(m,n) := ½(m+n−L(m,n)) ,
    Q_δ(x) := B_δ(x,x) = \big(Σ_na_n\big)\big(Σ_na_nn\big)
              − ½Σ_{m,n}a_ma_nL(m,n) .                                  (22.3)

It is finite and symmetric for every finite choice of `(δ_n)`, and on a
difference `Frob_m − Frob_n` it returns `L(m,n) − ½(δ_m+δ_n)`, which at
`δ ≡ 0` is exactly the entry of the smeared-Frobenius Gram of Paper 44
Theorem 8bis.1.

*Proof.*  A symmetric bilinear form on a free module is determined by its
values on pairs of generators, and the relation
`Γ_α·Γ_β = q(α)+q(β)−2B(α,β)` with `q(Frob_n) = d_n = n` and
`Γ_{Frob_m}·Γ_{Frob_n} = L(m,n)` gives `B(Frob_m,Frob_n) = G(m,n)`; bilinear
extension is the unique extension.  For (22.3), expand: the degree part is
`Σ_{m,n}a_ma_n·½(m+n) = (Σ_na_n)(Σ_na_nn)`.  Finiteness holds because every
element of `M` is a finite `Z`-combination, so both sums are finite.  For a
difference, `B_δ(e_m−e_n,e_m−e_n) = G(m,m)+G(n,n)−2G(m,n)` with
`G(n,n) = ½(2n−δ_n) = n−½δ_n`, which equals `L(m,n)−½(δ_m+δ_n)`.  ∎  `PROVED`

So the literal existence question has the answer **yes**: a finite symmetric
form extending the off-diagonal weights exists and is unique once the diagonal
is chosen.  The content is what happens next.

**Theorem 22.4 (the form is not a count: degeneracy and indefiniteness;
`PROVED`, witnesses `CERTIFIED`, `scripts/cosh_test_cmn.py` §[3] and
`scripts/tower_gram.py` §[7]).**  Take the model's convention `δ ≡ 0`.  Then

 (i) **Degeneracy against the count axiom.**  In a genuine degree form
     `\deg(α−β) = 0 ⟺ α = β`, since `\#\ker` of a nonzero isogeny is finite
     and nonzero.  Here `L(m,n) = 0` whenever `\max/\min` is not a prime
     power, while `Frob_m ≠ Frob_n` for `m ≠ n` (Paper 44 Theorem 3ter.4(iv):
     the object determines `n`).  Explicitly `L(6,10) = 0` and `L(15,22) = 0`.

 (ii) **Indefiniteness.**  `Q_0(x) = Φ_x(0)·Φ_x(1) − ½x^{\mathsf T}Lx` is, in
     its leading term, a product of two independent linear functionals, hence
     of signature `(1,1)` on any span on which they are independent.  On a
     pair `\{m,n\}` whose ratio is not a prime power the second term vanishes
     identically and `Q_0(a,b) = (a+b)(ma+nb)`, whose matrix
     `\begin{pmatrix} m & (m+n)/2\\ (m+n)/2 & n\end{pmatrix}` has determinant
     `mn − (m+n)^2/4 = −(m−n)^2/4 < 0`.  In particular, on
     `Z·Frob_6 ⊕ Z·Frob_{10}`,

          Q_0(5\,Frob_6 − 4\,Frob_{10}) = (5−4)(30−40) = −10 < 0 .       (22.4)

 (iii) Consequently `Q_0` is not `\#\ker` of anything, nor the measure of
     anything: a cardinality and a Haar measure are `≥ 0`, and `−10` is not.

 (iv) Indefiniteness is normalization-independent: with `d_n = \log n` in
     place of `d_n = n` the same witness gives `Q_0 = −0.2515 < 0`.

*Proof.*  (i) is Lemma 22.2's vanishing criterion — `10/6 = 5/3` and
`22/15` are not prime powers — set against Theorem 3ter.4(iv).  (ii): by
(22.1), for `x = Σa_nFrob_n` one has `Φ_x(0) = Σ_na_n` and
`Φ_x(1) = Σ_na_nn`, so (22.3) is exactly `Φ_x(0)Φ_x(1) − ½x^{\mathsf T}Lx`;
the product of two linearly independent functionals has signature `(1,1)`.
For the displayed witness, `L(6,10) = 0` by (i), so `Q_0` restricted to the
pair is `(a+b)(6a+10b)`, and `(5−4)(5·6−4·10) = −10`.  The determinant
computation is the general statement.  (iii) is immediate from (ii).  (iv) is
the certified value of `scripts/tower_gram.py` §[7], the substitution changing
only the degree functional and not the vanishing of `L(6,10)`.  ∎  `PROVED`

Two remarks fix the status of this negative.  First, the degeneracy (i) is
**convention-free**: it uses only which entries of `L` vanish, and that does
not depend on the chart constant `c_N(m,n)`, nor on the normalization, nor on
the smearing.  Second, the indefiniteness (ii) needs no witness at all — it is
a one-line consequence of the product structure of the leading term — and the
determinant `mn − (m+n−L)^2/4` appearing there is the **same** discriminant
that governs positivity of the rank-two form `m^2 + a_ℓmn + ℓn^2` with
`a_ℓ = ℓ+1−Λ(ℓ)`, the transported Hasse condition.  The two are one
computation, not two.

**Remark 22.4a (the diagonal is the only entry that is not a count, and the
model says so too).**  `I_A(Frob_n,Frob_n)` does not exist (Paper 44 Remark
8bis.1c: the Frobenius point classes are multipliers, not elements of `D_A`;
Corollary 8bis.1b′: the regularization parameters `(ε,N)` cannot both be
removed), and the self-intersection of the ambient diagonal is `−∞` at a fixed
chart (Theorem 8bis.2).  This is not an arithmetic pathology.  In the model
the count interpretation of `\deg(α−β)` is `\#\ker(α−β)`, and at `α = β` this
is `\#\ker(0) = \#E(\bar F_q) = ∞`: `\deg 0 = 0` is a convention there as
well.  `RESTATEMENT`

### 22.2 Zero-blindness, and uniformity in the falsifier

**Proposition 22.5 (the form is this paper's comparison identity with the zero
sum deleted; `PROVED`).**  For `x = Σ_na_nFrob_n ∈ M` write `Φ_x(s) = Σ_na_nn^{s}`
for the Mellin datum of the un-normalized smeared class attached to `x` by
(22.1).  Then

    Q_0(x) = Φ_x(0)·Φ_x(1) − ½\,x^{\mathsf T}Lx ,                       (22.5)

i.e. `Q_0` is the identity `I_∞ = 2Φ(0)Φ(1) − W` of §11 (11.6), up to the
factor `½`, with the **zero sum `W` deleted and replaced by the finite Gram
`L`**.  Consequently:

 (i) `Q_0` contains **no zero datum whatever**: its value on any `x` is
     determined by `(Φ_x(0),Φ_x(1))` and by the finitely many von Mangoldt
     weights `Λ(\max/\min)`, and is independent of the zero set of `ξ`;
 (ii) every statement of §§22.1–22.3 is **`Ξ_a`-uniform** — it holds verbatim
     with `ξ` replaced by `Ξ_a(s) = ξ(s+a)ξ(s−a)`, for every `0 < a < ½` —
     since §11 holds verbatim for `Ξ_a` and the construction uses only the
     Euler weights and the rulings;
 (iii) indefiniteness is immediate from (22.5), a product of two independent
     linear functionals having signature `(1,1)`.

*Proof.*  By (22.1), `Φ_x(0) = Σ_na_n` and `Φ_x(1) = Σ_na_nn`, so the first
term of (22.3) is `Φ_x(0)Φ_x(1)`, which is (22.5).  (i): the right-hand side
of (22.5) is a function of `Φ_x` at the two ruling points and of the matrix
`L` of (22.2), and `L` is built from `Λ` alone; no evaluation `Φ_x(ρ)` at a
zero occurs.  (ii): the ruling data `(Φ(0),Φ(1))` and the Euler weights are
the same objects for `Ξ_a` as for `ξ`, and §11's pairing identity is recorded
as holding verbatim for `Ξ_a`; since (22.5) never evaluates at a zero, the
substitution changes nothing.  (iii) is Theorem 22.4(ii).  ∎  `PROVED`

This is the strongest structural statement of the section's first half, and it
subsumes the non-detection result of §22.3: an invariant that never reads the
zeros cannot separate `ξ` from a function with zeros off the line.

### 22.3 The elliptic model of the additive structure, and a non-detecting test

**Theorem 22.6 (the class map is additive on an elliptic surface;
`CLASSICAL`).**  Let `E/F_q` be an elliptic curve, `F_1 = \{O\}×E`,
`F_2 = E×\{O\}`, and `Γ_φ` the graph of `φ ∈ \mathrm{End}(E)`.  Then in
`\mathrm{NS}(E×E)`

    [Γ_{φ+ψ}] = [Γ_φ] + [Γ_ψ] − F_2 + 2⟨φ,ψ⟩F_1 ,
    ⟨φ,ψ⟩ := ½\big(\deg(φ+ψ) − \deg φ − \deg ψ\big) ,                    (22.6)

equivalently `c(φ) := [Γ_φ] − (\deg φ)F_1 − F_2` is additive in `φ`.

*Proof (by numerical equivalence; the theorem of the cube is not needed).*
`\mathrm{NS}(E×E)_R` is spanned by `F_1`, `F_2` and the graphs, so it suffices
to pair both sides with `F_1`, `F_2` and `Γ_χ` for arbitrary
`χ ∈ \mathrm{End}(E)`.  Use `F_i^2 = 0`, `F_1F_2 = 1`, `Γ_φ·F_1 = 1`,
`Γ_φ·F_2 = \deg φ`, `Γ_φ·Γ_ψ = \deg(φ−ψ)`, and write `q(·) = \deg` for the
quadratic form with polarization `⟨·,·⟩`.

*Against `F_1`:* `1 = 1+1−1+0` ✓.
*Against `F_2`:* `\deg(φ+ψ) = \deg φ + \deg ψ + 2⟨φ,ψ⟩` ✓, which is the
definition of `⟨·,·⟩`.
*Against `Γ_χ`:* the left side is
`q(φ+ψ−χ) = q(φ)+q(ψ)+q(χ)+2⟨φ,ψ⟩−2⟨φ,χ⟩−2⟨ψ,χ⟩`, and the right side is
`[q(φ)+q(χ)−2⟨φ,χ⟩]+[q(ψ)+q(χ)−2⟨ψ,χ⟩]−q(χ)+2⟨φ,ψ⟩`; the two agree.

Two divisor classes on a surface with equal intersection numbers against a
spanning set are numerically equivalent, hence equal in `\mathrm{NS}`.  The
`c`-form follows by rearranging (22.6).  ∎  `CLASSICAL`

**Corollary 22.7 (`Γ_{1+π}` is effective and has negative coefficients in the
Frobenius basis; `PROVED`).**  With `φ = 1` (so `Γ_1 = Δ`), `ψ = π` and
`2⟨1,π⟩ = \deg(1+π)−1−q = a`,

    [Γ_{1+π}] = Δ + Γ_π − F_2 + a\,F_1 .                                (22.7)

For the curve of record `E/F_2 : y^2+xy = x^3+1` (`q = 2`, `N_1 = 4`,
`a = q+1−N_1 = −1`) this reads `[Γ_{1+π}] = Δ + Γ_π − F_2 − F_1`, with **two**
negative coefficients in the basis `\{F_1,F_2,Γ_{π^n}\}`.  `Γ_{1+π}` is an
irreducible curve, hence effective, yet it does **not** lie in the cone
`\mathrm{Cone}\{Γ_{π^n},Γ_{π^n}^{\mathsf t}\}` generated by the Frobenius
graphs.

*Proof.*  (22.7) is (22.6) at `φ = 1`, `ψ = π`.  The checks:
`·F_1 = 1+1−1+0 = 1` ✓; `·F_2 = 1+q−0+a = 1+a+q = \deg(1+π)` ✓, which at
`q = 2`, `a = −1` is `2`; and the self-intersection is
`2[Δ·Γ_π − Δ·F_2 − Δ·F_1 − Γ_π·F_2 − Γ_π·F_1 + F_1F_2]
 = 2[4−1−1−2−1+1] = 0 = Γ^2` for a graph on a curve of genus `1` ✓.
Effectivity is the irreducibility of the graph of the isogeny `1+π`.  That it
is outside the Frobenius cone is the presence of the negative coefficients
together with the fact that `F_1`, `F_2` and the `Γ_{π^n}` are a basis.  ∎
`PROVED`

**Definition 22.8 (the arithmetic would-be sum classes).**  Transport (22.6)
through the dictionary.  In `D^W`, `F_1 = K + K_{\mathrm{odd}}` and
`F_2 = K − K_{\mathrm{odd}}` have `M(F_1) = (1,0)`, `M(F_2) = (0,1)`, so
`I_∞(E,F_1) = Φ_E(0)` and `I_∞(E,F_2) = Φ_E(1)`: `F_2` is the **degree**
ruling and `F_1` the **unit** ruling, matching `Γ_φ·F_2 = \deg φ`,
`Γ_φ·F_1 = 1`.  Let `E_n ∈ D^W` be the un-normalized smeared Frobenius: for
`ε > 0` and an even `φ ≥ 0` of mass `1`,
`E_n^{(ε)}(u) := n^{1/2}ε^{−1}φ((u−\log n)/ε) ≥ 0`, so that in the limit
`ε ↓ 0`

    Φ_{E_n}(s) = n^{s},\quad M(E_n) = (n,1),\quad \deg E_n = n+1,
    \quad Φ_{E_n}(ρ) = n^{ρ} .                                          (22.8)

`E_n` is effective.  With `G(m,n)` as in (22.3) define

    c_{m,n} := E_m + E_n − F_2 + 2G(m,n)F_1 ,
    \deg c_{m,n} = 2(m+n)+1−L(m,n),\qquad Φ_{c_{m,n}}(ρ) = m^{ρ}+n^{ρ} . (22.9)

**Theorem 22.9 (the test of §19 passes on every `c_{m,n}`, and cannot fail;
`PROVED`; margins `CERTIFIED`, `scripts/cosh_test_cmn.py` §[1]).**  Let
`ρ_1 = ½+iγ_1` be the first zero of `ξ` and let
`s(γ,θ) := \sup_u|\cos(γu+θ)|/\cosh(u/2)` be the quantity of §19.  Then:

 (i) `0.99845 ≤ s(γ_1,θ) ≤ 1` for every real `θ`;
 (ii) for all `m,n ≥ 1`,
     `\max_θ\big[|\mathrm{Re}(e^{iθ}Φ_{c_{m,n}}(ρ_1))| − ½s(γ_1,θ)\deg c_{m,n}\big] < 0`,
     so the test does not refute effectivity of `c_{m,n}` for any pair;
 (iii) the test **cannot** fire on this family, for two independent structural
     reasons: `c_{m,n}` has the same `Φ` as the manifestly effective class
     `E_m + E_n` while carrying strictly more degree, so no criterion reading
     only `(Φ(ρ),\deg)` can distinguish them; and, underneath that, the whole
     correction `−F_2 + 2G(m,n)F_1` lies in the ruling plane, where `Φ`
     vanishes at every zero (Theorem 11.8(i)), while inflating the degree by
     `2G(m,n) ≈ m+n`.

*Proof.*  (i) The upper bound is `|\cos| ≤ 1 ≤ \cosh`.  For the lower bound
choose `u_0` with `γ_1u_0+θ ∈ πZ` and `|u_0| ≤ π/(2γ_1) < 0.1112`; then
`s(γ_1,θ) ≥ 1/\cosh(u_0/2) ≥ 1/\cosh(0.0556) > 0.99845`.

(ii) By (22.9), `|Φ_{c_{m,n}}(ρ_1)| ≤ \sqrt m + \sqrt n`, while by (i) the
subtracted term is at least `0.4992·(2(m+n)+1−L(m,n))`.  Write
`\max = t·\min` with `t ≥ 1`; then `L ≤ \min·\log t` and

    2(m+n) − L ≥ \min·(2+2t−\log t) ≥ 1.5\,\min·(1+t) = 1.5(m+n) ,

because `2+2t−\log t ≥ 1.5(1+t) ⟺ 0.5+0.5t ≥ \log t`, true for every `t > 0`.
Hence the subtracted term is at least `0.4992·1.5(m+n) = 0.7488(m+n)`.  For
`m+n ≥ 4` this exceeds `\sqrt m+\sqrt n`, since
`\sqrt m+\sqrt n ≤ \sqrt{2(m+n)}` and
`0.7488\sqrt{m+n} ≥ \sqrt 2 ⟺ m+n ≥ 3.57`.  The remaining pairs are checked
directly: `(m,n) = (1,1)` has `\deg c = 5`, bound `2.496 > |Φ| = 2`, margin
`−0.4998`; `(1,2)` has `\deg c = 6.307`, bound `3.148 > |Φ| = 0.605`, margin
`−2.5456`.

(iii) The first reason: `Φ_{c_{m,n}} = Φ_{E_m+E_n}` by (22.9), while
`\deg c_{m,n} = \deg(E_m+E_n) − 1 + 2G(m,n) > \deg(E_m+E_n)` for
`2G(m,n) > 1`; a criterion of the form
`|\mathrm{Re}(e^{iθ}Φ(ρ))| ≤ ½s\deg` is monotone in `\deg`, so it passes on
`c_{m,n}` whenever it passes on the effective class `E_m+E_n`, which it does.
The second reason: `Φ_K = ξ` and
`Φ_{K_{\mathrm{odd}}}(s) = \frac{\sinh((s−½)a_0)}{\sinh(a_0/2)}ξ(s)` both
vanish at every zero (Theorem 11.8(i)), so `F_1` and `F_2` are invisible at
the zeros and contribute only to the degree.  ∎  `PROVED`

Certified margins (negative means the test passes):

| `(m,n)` | `\|Φ(ρ_1)\|` | `\deg c` | `2G` | margin |
|---|---|---|---|---|
| `(1,1)` | `2.0000` | `5.000` | `2.000` | `−0.4998` |
| `(1,2)` | `0.6047` | `6.307` | `2.307` | `−2.5456` |
| `(2,3)` | `3.0284` | `11.000` | `5.000` | `−2.4700` |
| `(1,7)` | `2.0492` | `15.054` | `6.054` | `−5.4697` |
| `(3,9)` | `1.3321` | `21.704` | `8.704` | `−9.5138` |
| `(1,101)` | `9.3358` | `200.385` | `97.385` | `−90.7794` |
| `(6,10)` | `5.0172` | `33.000` | `16.000` | `−11.4728` |

**Corollary 22.9a (the shape an informative object would need; `PROVED` given
the cited obstruction).**  Any object realizing a sum `Frob_m + Frob_n` with
content at the zeros must have `Φ(ρ) ≠ m^{ρ}+n^{ρ}`, i.e. must not be
supported on shifted diagonals of the radial line; it would have to live on
`C_S × C_S` in two genuinely independent variables, restricting to `E_m+E_n`
on the radial diagonal and carrying the correction `2⟨φ,ψ⟩` with nonzero zero
data.  Moreover the correction actually available,
`2G(m,n) = m+n−L(m,n)`, is expressible in `\log p`, `p^{−1/2}`, `N` and `Γ`
alone, so by the obstruction cited as `P122.028` in §22.5 below it is barred
as an **independent** input for the sign.  ∎  `PROVED`

### 22.4 The computed Frobenius diagonal

Everything above treats the diagonal as a free parameter, following the
model's convention `δ ≡ 0`.  It is not free.  Paper 44 Theorem 8bis.1b
**computes** it at a fixed chart, and the computation has a structure that the
convention hides.  This subsection extracts it.  It is, so far as the
repository records, the first place in this line of work where the diagonal of
a Frobenius Gram is *computed* rather than chosen.

**Definition 22.10.**  Fix a chart `S` with `S_f ≠ ∅`, a level `N ≥ 1`, and a
unit-height even profile `φ_ε ∈ C_c^∞([−ε,ε])` with `φ_ε(0) = 1` and
`ε < ½\log 2`.  For `n ≥ 2` with `P(n) ⊆ S_f` write, following Paper 44
Theorem 8bis.1b,

    𝔡_{ε,N}(n) := T_∞\big(Δ^{(n),[φ_ε,N]}\big)
      = −Σ_{r ∈ S_f∖P(n)}(\log r)\Big[\tfrac{r−2}{r−1}+(N−1)\Big]
        − \log\tfrac1ε + c_φ ,                                          (22.10)

where `c_φ = γ+\log 4π + O(1)` depends on `φ` **only** and not on `n`, by
Theorem 8bis.1b(iv): the archimedean profile of `Δ^{(n),[φ_ε,N]}` is `φ_ε`
with every finite coordinate equal to `1`, irrespective of `n`.  The Gram
diagonal proper is `δ_n = V_N(n)·𝔡_{ε,N}(n)` in the bare convention and
`V_N(n)^{−1}𝔡_{ε,N}(n)` in the `♭` convention, with
`V_N(n) = ∏_{r ∈ S_f∖P(n)}((r−1)r^{N−1})^{−1} > 0` (Corollary 8bis.1b′).

**Theorem 22.11 (the difference of diagonals; `PROVED`).**  For `m,n ≥ 2` with
`P(m),P(n) ⊆ S_f`:

 (i) the archimedean divergence cancels **identically** — not to `O(1)`, but
     exactly, the term `−\log(1/ε)+c_φ` of (22.10) being the same number for
     every `n` — and

         𝔡_{ε,N}(m) − 𝔡_{ε,N}(n)
           = Σ_{r ∈ P(m)∖P(n)}(\log r)\Big[\tfrac{r−2}{r−1}+N−1\Big]
             − Σ_{r ∈ P(n)∖P(m)}(\log r)\Big[\tfrac{r−2}{r−1}+N−1\Big] , (22.11)

     **supported on the symmetric difference `P(m) △ P(n)`**, with no `ε` and
     no place outside it;
 (ii) each summand is `≥ 0`, and `> 0` except in the single case `r = 2`,
     `N = 1`.  Hence for `N ≥ 2`,
     `𝔡_{ε,N}(m) = 𝔡_{ε,N}(n) ⟺ P(m) = P(n)`, and for `N = 1` the same holds
     modulo the prime `2`;
 (iii) `V_N(n)` depends on `n` through `P(n)` only, so `P(m) = P(n)` gives
     `V_N(m) = V_N(n)` and therefore

          P(m) = P(n) \ \Longrightarrow\ δ_m = δ_n \quad\textbf{exactly, at
          every }(ε,N)\textbf{, in both conventions};                    (22.12)
 (iv) off that regime the difference diverges **linearly in the chart
     parameter `N`**, with slope
     `Σ_{r ∈ P(m)∖P(n)}\log r − Σ_{r ∈ P(n)∖P(m)}\log r`.

*Proof.*  (i) Subtract the two instances of (22.10).  The `n`-independent
tail `−\log(1/ε)+c_φ` cancels term by term.  For the finite sums, put
`A := S_f∖P(m)` and `B := S_f∖P(n)`; then
`−Σ_A + Σ_B = Σ_{B∖A} − Σ_{A∖B}`, and `B∖A = P(m)∖P(n)`,
`A∖B = P(n)∖P(m)`.  This is (22.11).

(ii) For `r ≥ 2` and `N ≥ 1`, `\frac{r−2}{r−1} ≥ 0` and `N−1 ≥ 0`, with both
vanishing only at `r = 2`, `N = 1`; this is the bracket of Theorem
8bis.1b(iii).  The implication `P(m) = P(n) ⟹ 𝔡(m) = 𝔡(n)` is immediate from
(22.11).  For the converse, suppose the difference (22.11) vanishes with
`P(m) ≠ P(n)`.  Positivity of each bracket alone does not exclude a
cancellation *between* the two sums, so argue as follows.  The coefficients
`c_r(N) = \frac{r−2}{r−1}+N−1` are **rational**, and the primes occurring are
distinct, so a vanishing difference is a rational linear relation
`Σ_r q_r\log r = 0` with `q_r ∈ Q` not all zero.  Clearing denominators gives
integers `a_r`, not all zero, with `Σ_ra_r\log r = 0`, i.e. `∏_r r^{a_r} = 1`
with the `r` distinct primes — contradicting unique factorization in `Z`.
Hence `P(m) = P(n)`.  (For `N = 1` the coefficient at `r = 2` is `0`, so the
prime `2` drops out of the relation and the conclusion holds modulo `2`.)

(iii) `V_N(n)` is a product over `S_f∖P(n)`, so it is a function of `P(n)`;
combined with (i)–(ii), `P(m) = P(n)` gives both `𝔡(m) = 𝔡(n)` and
`V_N(m) = V_N(n)`, hence `δ_m = δ_n` in either convention.

(iv) is the `N`-linear part of (22.11).  ∎  `PROVED`

**Remark 22.11a (an honest note on the unique-factorization step).**  The
source record established (22.12) and left the converse of (ii) asserted from
positivity of the bracket alone, which does not by itself exclude an
accidental cancellation between the two sums; the missing step is the
rational-relation-against-unique-factorization half-line, which is supplied in
the proof above.  The statement is unaffected; the gap was one line and it is
closed here.

**Remark 22.11b (what (22.12) replaces, and what it does not claim).**  At a
fixed chart `δ_n` is a **finite negative** number in the regime where Theorem
8bis.1b's contributions are both negative; it is **not** proportional to any
degree of `Frob_n`; and its variation in `n` is entirely supported on
`P(m) △ P(n)`.  The divergence of the *absolute* diagonal as `ε → 0` and
`N → ∞` (Theorem 8bis.2, Corollary 8bis.1b′) is untouched by (22.12); what
(22.12) says is that this divergence **cancels exactly** between two Frobenii
with the same prime support.  No positivity, and no sign, is claimed or
implied.

### 22.5 The single-prime tower: a Toeplitz form, stated as pure magnitude

**Definition 22.12.**  Fix a prime `p ∈ S_f` and put
`M_p := Z⟨Frob_{p^k} : k ≥ 1⟩ ⊂ M`.  Since `P(p^k) = \{p\}` for every `k ≥ 1`:
the chart constant is the **same** for every pair,
`c_N(p^j,p^k) = ∏_{s ∈ S_f∖\{p\}}((s−1)s^{N−1})^{−1} =: c_p > 0`, independent
of `(j,k)`; and by (22.12) the diagonal is the same for every `k`,
`δ_{p^k} = δ_p`, exactly.  Hence with `ρ := p^{−1/2} ∈ (0,1)` and
`T(ρ)_{jk} := ρ^{|j−k|}` the half-density Gram of the tower is

    G^{(p)} = c_p(\log p)\Big[\,T(ρ) + (τ_p−1)I\,\Big],\qquad
    τ_p := \frac{δ_p}{c_p\log p} .                                      (22.13)

**Domain of record.**  (22.13) is an identity **only where the archimedean
part of Paper 44 Theorem 8bis.1's off-diagonal vanishes**: that part carries
the factor `∏_{s ∈ S_f∖\{p\}}\mathbf 1[s^N \mid p^j−p^k]`, which is empty
(hence `1`, hence the archimedean block is present) when `S_f = \{p\}`, and
which equals `1` at `S_f = \{2,p\}`, `p` odd, `N = 1`.  So (22.13) is asserted
**only** for `S_f ⊋ \{p\}` with `N` large enough that this indicator vanishes
on every pair in play; Corollary 8bis.1d's "no archimedean block on the pure
Frobenius family" is conditional in exactly the same way.  Everything below is
stated on that domain and nowhere else.

**Lemma 22.13 (the conventions collapse to one number; `PROVED`).**
`c_p(\log p) > 0`, and `c_p = V_N(p^k)` for every `k`, so
`τ_p = 𝔡_{ε,N}(p)/\log p` — a ratio in which the chart constant cancels
identically.  Therefore the signature of `G^{(p)}` depends on the chart, the
level, the smearing and the convention **through the single real number `τ_p`
and through nothing else**.

*Proof.*  By Paper 44 (8bis.2b) with the correction K1, the index set of
`c_N(p^j,p^k)` is `S_f∖(P(p^j) ∩ P(p^k)) = S_f∖\{p\}`, the same set for every
pair, and this is exactly the index set of `V_N(p^k)` in Definition 22.10;
hence `c_p = V_N`.  In the bare convention `δ_p = V_N·𝔡_{ε,N}(p)`, so
`τ_p = δ_p/(c_p\log p) = 𝔡_{ε,N}(p)/\log p`; in the `♭` convention both
`δ_p` and `c_p` invert and the ratio is unchanged up to the same positive
factor, which does not affect a signature.  Positivity of `c_p` is positivity
of a volume.  ∎  `PROVED`

**Proposition 22.14 (the off-diagonal is a count, and un-normalizes to the
function-field prefactor; `PROVED`).**  For `j ≠ k`,
`G^{(p)}_{jk}/c_p = Λ(p^{|j−k|})p^{−|j−k|/2}` is the Haar measure `\log p` of
the fixed-point shell of `Frob_{p^j} ⋆ Frob_{p^k}^† = Frob_{p^{|j−k|}}`
(Lemma 22.2), times the half-density weight `p^{−|j−k|/2} ≤ 1`.
Un-normalizing by `(p^jp^k)^{1/2}` gives

    (p^jp^k)^{1/2}·(\log p)\,p^{−|j−k|/2} = p^{\min(j,k)}\,\log p ,      (22.14)

which is the function-field model's `q^{\min}N_{|a−b|}` of §21 under the
single substitution `N_k ↔ \log p` — the `q^{\min}` prefactor being reproduced
**without adjustment**.  The diagonal, by contrast, is not a count: on the
domain of record `δ_p < 0`, while a Haar measure and a cardinality are `≥ 0`.

*Proof.*  The off-diagonal identification is Lemma 22.2 together with Paper 44
Theorems 3ter.4 and 3ter.7 for the composition and Theorem 3ter.10 for the
contact; the displayed algebra is one line:
`(p^jp^k)^{1/2}p^{−|j−k|/2} = p^{(j+k−|j−k|)/2} = p^{\min(j,k)}`.  For the
diagonal, on the domain of record (22.10)'s finite sum is a sum of nonpositive
terms and the archimedean part `−\log(1/ε)+c_φ` is dominated by the `N`-linear
finite-place term, so `𝔡_{ε,N}(p) < 0` and hence `δ_p < 0`.  ∎  `PROVED`

**Theorem 22.15 (the Toeplitz trichotomy; `PROVED`, thresholds `CERTIFIED`,
`scripts/tower_gram.py` §§[1]–[2]).**  On the domain of record, with
`ρ = p^{−1/2}` and `τ_p` as in (22.13), for the semi-infinite tower
`\{Frob_{p^k}\}_{k ≥ 1}`:

    G^{(p)} ⪰ 0 \iff τ_p ≥ τ_+(p) := \frac{2ρ}{1+ρ} = \frac{2}{\sqrt p+1} ,
    G^{(p)} ⪯ 0 \iff τ_p ≤ τ_-(p) := −\frac{2ρ}{1−ρ} = −\frac{2}{\sqrt p−1} , (22.15)

and `G^{(p)}` is indefinite strictly between.  For every finite truncation
`\{Frob_{p^k}\}_{k=1}^{K}` with `K ≥ 2`, positive semidefiniteness requires
`τ_p ≥ 1 − λ_{\min}(T_K(ρ)) > 0`.  Certified values:
`τ_+(2) = 0.828427`, `τ_+(3) = 0.732051`, `τ_+(7) = 0.548584`,
`τ_-(2) = −4.828427`; and
`λ_{\min}(T_K(2^{−1/2})) = 0.1974,\,0.1779,\,0.1732` at `K = 4,8,16`.

*Proof.*  `T(ρ)` is the Kac–Murdock–Szegő matrix with symbol

    f_ρ(θ) = Σ_{k∈Z}ρ^{|k|}e^{ikθ} = \frac{1−ρ^2}{1−2ρ\cosθ+ρ^2} ,

a continuous positive function on the circle with
`\min f_ρ = f_ρ(π) = \frac{1−ρ}{1+ρ}` and
`\max f_ρ = f_ρ(0) = \frac{1+ρ}{1−ρ}`.  By (X29), a Toeplitz operator with
continuous real symbol `f` satisfies
`\inf\mathrm{spec}\,T(f) = \min f` and `\sup\mathrm{spec}\,T(f) = \max f`, for
the semi-infinite as for the bi-infinite operator.  Hence (22.13) is positive
semidefinite iff `τ_p−1+\min f_ρ ≥ 0`, i.e.
`τ_p ≥ 1−\frac{1−ρ}{1+ρ} = \frac{2ρ}{1+ρ}`, and negative semidefinite iff
`τ_p−1+\max f_ρ ≤ 0`, i.e. `τ_p ≤ −\frac{2ρ}{1−ρ}`; strictly between, the
spectrum of `T(ρ)+(τ_p−1)I` meets both half-lines.  For a finite section,
`λ_{\min}(T_K) ≤ \mathrm{tr}\,T_K/K = 1` with equality iff `T_K = I`, false
for `K ≥ 2`; so PSD of the section forces `τ_p ≥ 1−λ_{\min}(T_K) > 0`.  At
`K = 2`, `λ_{\min}(T_2) = 1−ρ`, so the threshold is `ρ`, which is `0.7071` at
`p = 2`.  ∎  `PROVED`

**Corollary 22.16 (the computed tower form is not positive semidefinite on the
domain of record; `PROVED`).**  On the domain of record, `δ_p < 0`
(Proposition 22.14), hence `τ_p < 0 < τ_+(p)`, hence `G^{(p)}` is **not**
positive semidefinite — already at `K = 2`.  Moreover, as `N` grows in the
same domain, `𝔡_{ε,N}(p) → −∞` linearly in `N`, so `τ_p` crosses `τ_-(p)` as
well and `G^{(p)}` becomes **negative semidefinite**; with `S_f = \{2,3\}`,
`p = 3`, `ε = 0.34`, this happens for `N ≥ 9`.  ∎  `PROVED`

**Remark 22.16a (what this does and does not decide; the magnitude-only
obstruction).**  Corollary 22.16 is a computed **failure** of positivity and
nothing else.  It must not be read as a sign statement in either direction,
for a reason that is a theorem of the repository and not a caution:

> **Obstruction `P122.028` (`PROVED-IN-REPOSITORY`;
> `03-research/phase-122-row-d-integrity-and-construction/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md`
> §6; the theorem of method it records).**  A relation
> derived solely from the data `\log p`, `p^{−1/2}`, `N` and `Γ` cannot be
> cited as an independent input for the sign: those data already define both
> sides of the scalar explicit formula.

On a single-prime tower every ingredient of `G^{(p)}` is a function of `p`,
`\log p`, `p^{−k/2}` and the chart: the off-diagonal by (22.14), the diagonal
by (22.10), and the threshold by (22.15).  `G^{(p)}` therefore carries **no
phase datum**, and by the obstruction its sign carries no information about
`ξ` whatever it turns out to be.  Consistently with this, the analogous
threshold for the falsifier moves only imperceptibly: replacing `Λ` by
`Λ_a(p^k) = Λ(p^k)·½(p^{ka}+p^{−ka})` gives the kernel
`ĝ_a(k) = ½(ρ_+^k+ρ_-^k)` with `ρ_± = p^{−(½∓a)}`, whose symbol is a sum of
two Poisson kernels attaining their minima at the common point `θ = π`, so the
trichotomy holds verbatim with
`τ_+(a) = \frac{ρ_+}{1+ρ_+}+\frac{ρ_-}{1+ρ_-}`; at `p = 2` this is
`0.828427,\ 0.828477,\ 0.829671,\ 0.833143` at `a = 0,\,0.05,\,0.25,\,0.49`.
That is a statement about **thresholds** only.  No `Ξ_a` diagonal has been
computed, so nothing here separates `ξ` from the falsifier, and the question
is emphatically not one on which the falsifier is silent: see the withdrawal
table below.

### 22.6 The structural theorem: the arithmetic Frobenius is a translation

**Theorem 22.17 (`Spec Z` is terminal, so there is no ring of Frobenius
correspondences; `CLASSICAL` for the `\mathrm{Hom}` statement, `PROVED` for
the consequence).**

 (i) The only ring endomorphism of `Z` is the identity.
 (ii) Equivalently, `\mathrm{Hom}_{\mathrm{Sch}}(\mathrm{Spec}\,Z,
     \mathrm{Spec}\,Z) = \{\mathrm{id}\}`; indeed `\mathrm{Spec}\,Z` is the
     terminal object of the category of schemes.
 (iii) Consequently Weil's ring `Z[π] ⊂ \mathrm{End}(E)` of §21 has **no
     analogue over `\mathrm{Spec}\,Z`**: there is no ring of self-maps of the
     base in which `m + n·Frob_ℓ` is an element.  The additive structure on
     which Weil's degree identity `\deg(m+nπ) = \#\ker(m+nπ)` rests has, in
     the arithmetic setting, **no realization by one-variable objects**: the
     only additive structure available on `\{Frob_n\}` is the formal one,
     `Z⟨Frob_n⟩` with the bilinear extension of Theorem 22.3, whose elements
     are not self-maps of anything and hence have no kernels and no
     fixed-point sets to count.

*Proof.*  (i) Let `f : Z → Z` be a ring homomorphism.  By definition
`f(1) = 1`; by additivity `f(n) = f(1+\cdots+1) = n·f(1) = n` for `n ≥ 0`, and
`f(−n) = −f(n)`, so `f = \mathrm{id}`.

(ii) By the anti-equivalence between commutative rings and affine schemes
(X29a), `\mathrm{Hom}_{\mathrm{Sch}}(\mathrm{Spec}\,Z,\mathrm{Spec}\,Z)
 = \mathrm{Hom}_{\mathrm{Ring}}(Z,Z)`, which is `\{\mathrm{id}\}` by (i).  For
terminality: `Z` is the initial object of the category of commutative rings —
for any ring `R` the map `n ↦ n·1_R` is the unique ring homomorphism `Z → R` —
and for a general scheme `X` one has
`\mathrm{Hom}_{\mathrm{Sch}}(X,\mathrm{Spec}\,Z)
 = \mathrm{Hom}_{\mathrm{Ring}}(Z,Γ(X,𝒪_X))`, a one-element set.

(iii) In the elliptic case, `\mathrm{End}(E)` is a ring because `E` carries a
**group law** in addition to being the object the endomorphisms act on: the
sum `φ+ψ` is defined pointwise by `(φ+ψ)(x) = φ(x) + ψ(x)`, and this second
structure is what makes `m+nπ` an endomorphism and gives it a kernel.  Over
`\mathrm{Spec}\,Z` the analogous position is occupied by the modulus group of
the carrier, and it is already spent: by (1.5) the Frobenii act **by**
translation of that group, `Frob_m ⋆ Frob_n = Frob_{mn}`, and by (ii) the base
admits no endomorphism other than the identity with which to form a second,
independent addition.  A formal sum `Σ_na_nFrob_n` is therefore not a
self-map, has no fixed-point set, and `Q_δ` evaluated on it is not the measure
of anything — which Theorem 22.4(ii) confirms from the other side, `−10` being
a value no count can take.  ∎  `CLASSICAL` (i),(ii); `PROVED` (iii)

**What the theorem does not say.**  It does not say that no additive structure
exists anywhere in reach; it says that none is realized **by one-variable
objects over `\mathrm{Spec}\,Z`**, i.e. by self-maps of the carrier of §1.  It
makes no assertion about two-variable objects on `C_S × C_S`, about
correspondences in the derived sense, or about the sign.

**Remark 22.18 (`OPEN`; no claim).**  The ring that does become available is
`Z[\mathrm{Gal}(K/Q)]`, the group ring of the Galois group of a finite
extension: after the base change of §18 the Frobenius elements of a nonabelian
`\mathrm{Gal}(K/Q)` generate a genuine ring, in which sums of Frobenius
elements are again elements, and in which Weil's `+` is present as an
operation rather than as a formal device.  **Nothing is claimed here about
whether that ring supplies the missing `+` in the sense Theorem 22.17(iii)
shows to be absent over `\mathrm{Spec}\,Z`** — not that it does, not that it
does not, and not that its degree theory would carry a sign.  It is recorded
as the one place the structural obstruction of this section is not in force.
`OPEN`

### 22.7 What the section establishes

The honest summary is short and has two halves.

The **multiplicative** semigroup `\{Frob_n, ⋆, †\}` is complete and fully
counted.  Every quantity it produces — `\log n`, the contacts
`Λ(n)n^{−1/2}`, the off-diagonal Gram entries (22.2), the tower entries
(22.14) — is a cardinality or the Haar measure of a nonempty fixed-point set,
nonnegative by construction (Lemma 22.2, Proposition 22.14).  It contains no
sign, because it contains no negative number.  The additive structure that
would turn these counts into a norm form is not realized by any object over
`\mathrm{Spec}\,Z` (Theorem 22.17), and when imposed formally it yields a form
that is degenerate against the count axiom, indefinite, and — decisively —
**zero-blind and `Ξ_a`-uniform** (Theorem 22.4, Proposition 22.5).  The sign
is not in the multiplicative semigroup and it is not in any count on the
formal additive module built from it.

The **diagonal** is the section's positive result.  It is computable, not
conventional; its archimedean part is `n`-independent and cancels exactly in
differences; its variation is supported precisely on `P(m) △ P(n)`; and
`P(m) = P(n)` forces `δ_m = δ_n` exactly, at every `(ε,N)` and in both
conventions (Theorem 22.11).  That makes the single-prime tower a genuinely
computed object with a single parameter and an explicit Toeplitz threshold
`2/(\sqrt p+1)` whose off-diagonal reproduces the function-field prefactor of
§21 without adjustment.  It is also, so far, **sign-free**: on a single-prime
tower every ingredient is a function of `p`, `\log p`, `p^{−k/2}` and the
chart, and the repository's magnitude-only obstruction forbids reading a sign
out of such data.  A computed diagonal is a new kind of datum in this line of
work; it is not yet a sign.

### Withdrawn in this section

| claim | reason |
|---|---|
| "the single-prime tower form is never positive semidefinite, at any chart, at any level, at any smearing, in either convention" | Withdrawn **as stated**.  The universal quantifier is false: outside the domain where (22.13) is the Gram — at `S_f = \{2,p\}` with `p` odd, `N = 1`, `ε = 0.34` — the finite sum of (22.10) is exactly zero, giving `𝔡 = +2.029 > 0` and `τ_3 = 1.847 > τ_+(3) = 0.732`, a positive semidefinite corner.  That corner is precisely where the archimedean indicator does **not** vanish and (22.13) is missing a term.  Restated as Corollary 22.16 on the domain of record, where in addition the form is eventually negative semidefinite for large `N`; and being magnitude-only its sign carries no information about `ξ` (Remark 22.16a) |
| "the `Ξ_a` falsifier axiom A3 does not enter on the tower" | Withdrawn.  The comparison drawn was between a computed **`ξ`-diagonal** and a **`Ξ_a` threshold**; no `Ξ_a` diagonal was computed anywhere, and non-separation of thresholds is not non-separation of forms.  Moreover the repository's single-prime positivity theorem (Doc 131 Theorem 6.7, `03-research/phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md`) decides positivity for the single-Euler-factor object with the same weights **iff** `|α| = \sqrt p`, i.e. iff `a = ½`: the question is maximally `Ξ_a`-**sensitive**, not insensitive |
| the Hasse-type test transported by `N_1 ↔ Λ(ℓ)`, and the rank-two order `m^2+a_ℓmn+ℓn^2` with `a_ℓ = ℓ+1−Λ(ℓ)` | Kept out of the body, `HEURISTIC`.  The dictionary is over-determined and has no solution at a single prime: matching `q^{−|a−b|/2}N_{|a−b|}` against `Λ(\max/\min)(\min/\max)^{1/2}` forces `N_k ↔ \log p` for every `k ≥ 1`, whereas a genuine rank-two order forces `N_2 = ℓ^2+1−(a_ℓ^2−2ℓ)`; at `ℓ = 2` the order predicts `N_2 = 3.6784` and the dictionary supplies `N_2 = \log 2 = 0.6931` |
| "adjunction forces the arithmetic diagonal `δ_n = d_n(2−2g) = n(2−2g) = −∞`, and the infinite genus is the counterterm that would make the form positive" | Withdrawn in its entirety.  Adjunction is not available over `\mathrm{Spec}\,Z`, and Paper 44 Theorem 8bis.1b computes the diagonal: at a fixed chart it is finite, its `n`-dependence runs through `P(n)` only, and it is not proportional to any degree of `Frob_n`.  Replaced by §22.4 |
| "`Q_δ ⪰ 0` on `Z⟨Frob_n⟩` is equivalent to Weil positivity, hence to RH" | Withdrawn as an equivalence.  The cited cone proposition concerns a closed, `𝓝_∞`-saturated cone carrying the degree gate, and does not say that positive semidefiniteness of `Q_δ` on `Z⟨Frob_n⟩` is RH; no such reduction exists.  Status: `OPEN`, suspected RH-equivalent, not proved so.  The associated prohibition on attempting to choose `(δ_n)` positively is retained |
| "the degree form agrees with `I_∞` on differences" | Withdrawn in the strong reading.  For `x = E_m − E_n` one has `Φ_x(0) = 0` and `Φ_x(1) = m−n`, so by (11.6) `I_∞(x,x) = −W(x)`, of the **opposite** sign to `B_0(x,x) = L(m,n) ≥ 0`.  What agrees is the off-diagonal **entry**, which is the weaker statement made in Theorem 22.3 |
| "the endomorphisms of `C_S` are classified as the affine maps `x ↦ ℓx^{k}`, hence no sum of correspondences is realized as a correspondence" | Withdrawn as stated.  The classification was asserted, not proved, and is false as literally written (`C_Q ≅ R_{>0}×\hat Z^×` has a large continuous endomorphism monoid).  The Riemann–von Mangoldt density argument against `s ↦ ks` for `k ≠ 1` is correct and is retained where used; the structural conclusion is re-proved from `\mathrm{Hom}(\mathrm{Spec}\,Z,\mathrm{Spec}\,Z) = \{\mathrm{id}\}` in Theorem 22.17 |
| "the shadow's degree `\deg_{det}Sh_Z` is a genuine count and is rank one, for arbitrary `Z`-combinations" | Withdrawn.  The additivity used is false in general for `k = m+nℓ`, and the rank-one proof is invalid: `L_S = ∏_{p∈S_f}Z_p` is not a rank-one `Z`-module.  What survives is the monomial statement `\deg_{det}Sh_Z(Frob_m ⋆ Frob_n) = \log(mn) = \log\#(L_S/mnL_S)`, which is all that is used here |
| "the chart constant `c_N(m,n) → 1` and may be suppressed; it affects no sign below" | Withdrawn.  `c_N(m,n) = ∏_{s∈S_f∖(P(m)∩P(n))}((s−1)s^{N−1})^{−1}` decays geometrically to `0` in the bare convention and diverges in the `♭` convention, and depends on `(m,n)` through `P(m) ∩ P(n)`, so it does not cancel out of the form.  What survives is the **vanishing** of an entry, which is convention-free — hence Theorem 22.4(i) and the `−10` witness, which use only zero entries and the degree term.  Every numerical statement about a **nonzero** entry is stated up to an unfixed positive factor; the one regime where this is harmless is the single-prime tower, where `c_N` is a single common positive constant (Lemma 22.13) |
| "the `Ξ_a` tower form becomes unbounded at `a = ½`, so no threshold exists there" | Withdrawn as a statement about the threshold.  The symbol's **supremum** is unbounded (a pole at `θ = 0`), but its **infimum** is finite, `−1` in the Poisson normalization, giving `τ_+(½) = ½+\frac{1}{p+1}` (`= 0.8333` at `p = 2`), the continuous limit of the `a = 0.49` value.  The unboundedness statement is true of the norm and false of the threshold |
| the recommendation to re-run the tower construction on the unit-averaged family `Frob ⋆ Δ^{\mathrm{rad}}` as the route forward | Withdrawn as a route.  Adding the archimedean block adds a `Γ`-datum, which lies **inside** the barred class of the obstruction `P122.028`, not outside it; and the semilocal version of the same object is already recorded elsewhere in this programme with the verdicts "`OPEN`, not provable by the named means", "added prime blocks subtract", and "the finite half alone carries no positivity to donate" |

---

## 23. The state of the sign

*Provenance.  This section consolidates §§17–22 and the closing records of
`03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md`,
`03-research/phase-137-row-d-canonical-coupling/R137_007_CLOSING_DECISION.md`,
`R138_005`, `R139_005`, `R140_005`, `R141_005`, `R142_005`, `R143_005`,
`R144_005`, `R145_005`, `R146_005` of the corresponding directories, and
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-SYNTHESIS-PHASES-135-144.md`.
It states no new mathematics.*

### 23.1 What is proved

Unconditionally, and with no hypothesis on the location of the zeros beyond
the imports listed in §15:

1. **The splitting.**  `D^W = Λ ⊥ P^W` with `Λ = span(K, K_odd)` a hyperbolic
   plane of signature `(1,1)` reading only the rulings, and `K_odd` an explicit
   class of `D^W` (Theorem 17.5).  On `Λ` the Hodge-index inequality holds
   identically with slack `½(\deg⁺F − \deg⁻F)²` (Theorem 17.7); no inequality
   in the ruling datum alone can separate `ξ` from a function with off-line
   zeros (Corollary 17.7a).
2. **Detection is cheap and zero-free.**  `RH ⟺ W(h_T) ≥ 0` for every `T > 0`
   on the triangle family (Theorem 17.14); `E` and `C_c^∞(R)` are detecting
   cones (Corollary 17.17).  On every detecting cone the sign is the
   prime-number-theorem remainder (Theorem 17.19).
3. **The falsifier is visible in the polar block alone.**  For `Ξ_a` the
   Hodge-index inequality fails on the *effective* class `τ_uK_a + τ_{−u}K_a`,
   by strict Cauchy–Schwarz on four polar weights, with no zero, no prime and
   no `h⁰` (Theorem 17.21); the invariant that separates is equimodularity of
   `|p − ½|` (Theorem 17.22), which `ζ_K` also has (Remark 17.24).
4. **Two method constraints.**  T1: any proof must be uniform in the number
   field (Theorem 18.1).  T2: no derivation of the Hodge-index inequality for
   `ξ` from the axioms A1–A6, A2⁺ alone can exist; any proof must use A3
   (equimodularity, pinned by `Ξ_a`) *and* at least one of A7, A8, A9 (pinned
   by the Epstein function `Ξ_Q`) — Theorem 18.16, with the Transfer Lemma
   18.15 and the Siegel-zero price of the A9 escape (Corollary 18.17).
5. **The field-uniform frame.**  The whole frame of §11 exists for every number
   field, with `K_K` built by contour shift (Theorem 18.18), and base change is
   additive over conjugate packets with primitive excess (Theorem 18.20,
   unconditional in the abelian case).
6. **Growth.**  `h⁰_{\mathbb Z}(mK) ≫ (\log m)^{3/2}/\log\log m` on the full
   Frobenius lattice (Theorem 18.28), with the per-generator threshold
   `e^{πq²} ≤ m ≲ e^{5.1q²}` in both directions (Corollary 18.27) and the
   certified non-vacuity from `m ≈ 4.5·10^6` (Theorem 18.25) — against the
   `¼m²` that clause (c) requires.
7. **The Riemann–Roch functional.**  `R(K−E) = R(E)` from bilinearity alone
   (Theorem 19.2); `h⁰_{RR}^{+}` satisfies (a) and (c) unconditionally for
   every `χ`, with growth exactly `¼m² − ¼m + χ` at `mK` (Theorem 19.6);
   `χ > 0` is refuted and `χ = 0` is exactly calibrated (Theorem 19.8,
   Corollary 19.9).
8. **The square as a tensor structure.**  The Frobenius family is
   ideal-indexed over every number field, with the inverse-semigroup law and
   the integral shadow `Sh_{O_K}(Frob_𝔫) = \mathrm{Cone}(𝔫L_S ↪ L_S)`,
   `H⁰ ≅ O_K/𝔫`, `\deg_{det} = \log N𝔫` (Theorems 19bis.3, 19bis.5), which
   makes the passage from `Q` to a general number field for the Frobenius
   family of Paper 44.  The
   tensor square `h⁰_□` clears the growth requirement of clause (c) exactly,
   with `(r²/4)m²` at `mK_K` and the optimal constant `χ = 1/8` for `ξ`
   (Theorems 19bis.15, 19bis.16).  Against that: **no nonzero `h⁰` factoring
   through the bidegree satisfies (b′)** (Theorem 19bis.19), and every `h⁰`
   built from pairings with the realization of the square so factors
   (Theorem 19bis.22); an admissible `h⁰` must therefore read the zero data
   through pairings `I_∞(E,X)` with `Z(X) ≠ 0` (Corollary 19bis.23).  The three
   Gram forms of the Frobenius family are separated, and no object carries the
   arithmetic one and the signed one together (Theorem 19bis.12).

9. **The frame defect theorem.**  Given (X19), **no** `h⁰` on `D^W` satisfies
   (a), (b′), (c) of Theorem 12.3 for `ξ`, for any `χ` (Theorem 19.25); the
   same for every admissible `Z` with a simple isolated on-line zero
   (Theorem 19.28).  The deficit is the constant `s(γ,θ) < 1` of Lemma 19.17,
   with `s_* = 0.99846…` attained at `ρ_1` (Proposition 19.18).
   **[phase 156:]** the same holds for `h⁰` defined only on `C_c^∞ ⊕ RK` or on
   `P_c^∞ ⊕ RK = \mathrm{span}\,𝒢_min`, with the compactly supported witness of
   Lemma 19.25a (Corollary 19.25b); on the bare set `𝒢_min` the hypothesis is
   equivalent to RH (Remark 19.25c(i)).
10. **The trace side.**  `ker T = 𝓝_∞` (Theorem 20.5); (T1′)
   `B4^{g,0} ∩ P^W ⊆ 𝓝_∞` unconditionally (Theorem 20.15); and the
   **unconditional transfer theorem 12.3-B4** (Theorem 20.17), which uses
   (T1′) and nothing else — no ample class, no Theorem 11.14, no (T2_cone).
   `(G⁺)` is unconditional for `g_λ = K + λh` (Lemma 20.21).  Index-locality:
   for every `E` with `Φ_E(0) > 0`, `t_n(E) > 0` for all `n ≥ N(E)`,
   unconditionally (Proposition 20.26(i),(ii)).
11. **The function-field model.**  The frame exists on a curve over a finite
    field with `I_∞^C(E,F) = +(D_E·D_F)` (Theorem 21.7), and **the frame defect
    theorem holds there too**, with `s_C^* = √(7/11)` and a witness at `d = 3`
    (Theorem 21.15) — while the Riemann hypothesis for the curve is a theorem.
    So `s < 1` is a property of the *cone*, not of the zeros.  The frame's `E`
    is exactly the cone of Frobenius graphs, with `σ(𝓔_C) = ½s_C^*` against
    `σ(\overline{\mathrm{Eff}}) = ½` (Theorem 21.17).
12. **The degree form and the diagonal.**  A finite symmetric form on
    `Z⟨Frob_n⟩` extending the off-diagonal Gram exists, is degenerate and
    indefinite, and equals `2ab − W` with the zero sum deleted — hence
    zero-blind and `Ξ_a`-uniform (Theorems 22.3, 22.4, Proposition 22.5).  The
    Frobenius diagonal is *computed*, not chosen, and its differences are
    exact: `P(m) = P(n) ⟹ δ_m = δ_n` (Theorem 22.11).  The arithmetic
    Frobenius is a translation, not an endomorphism: `Spec Z` is terminal, so
    Weil's ring `Z[π]` has no analogue here (Theorem 22.17).

### 23.2 What is a restatement

These are equivalences with RH, not reductions of it.  Each is recorded so
that it is not mistaken for progress.

| statement | where |
|---|---|
| RH ⟺ the Hodge-index inequality on any detecting cone | Corollary 17.11 |
| RH ⟺ `I_∞(F,F) ≤ ½(\deg F)²` on the ample cone (the cone is defined through `I_∞`) | Corollary 17.10, correction of record P46-4 at §11.5 |
| RH ⟺ `∃g` such that `(b′)_{B4^g}` holds for `h⁰_{RR}^{+}`; equivalently `∃h⁰` with (a), (b′)_{B4}, (c) | Theorem 20.23 |
| RH ⟺ `I_∞(E, g_λ) ≥ 0` on `S_0 = \{\deg E > 0,\ ½I_∞(E,E) > ¼\deg E\}` — the shortest form this line of work produced | Restatement 20.30 |
| RH ⟺ `(P_m)` at any one fixed index `m ≥ 1`; RH ⟺ bounded density on `S_0`; RH ⟺ the index-`0` sparse clause | Theorems 20.29, 20.31, Corollary 20.33 |
| RH ⟺ the bigness clause, for closed `𝓝_∞`-saturated cones with the degree gate | Proposition 21.21 |
| Castelnuovo's inequality on every finite span of a translate orbit ⟺ Bochner positivity of the Toeplitz kernel `c ↦ W(E_0,τ_cE_0)` ⟺ RH for the zeros the class sees | Restatement 19bis.13 |
| The geometric diagnosis: the frame keeps the intersection theory of `C×C` and discards its linear systems | Restatement 19.29 |

### 23.3 What is refuted

| claim | verdict | where |
|---|---|---|
| The hypothesis of Theorem 12.3 is satisfiable for `ξ` | `REFUTED` given (X19) | Theorem 19.25 |
| The clause (b′)⁺, in every form, including the stable one | `REFUTED` | Theorems 19.23, Corollary 19.24 |
| `χ > 0` is admissible | `REFUTED` | Theorem 19.8 |
| `(C4.1)`, the cheap necessary condition | `REFUTED` (false) | Theorem 19.22 |
| Clause (b′) for a nonzero `h⁰` factoring through the bidegree | `REFUTED` | Theorem 19bis.19, Corollary 19bis.20 |
| `χ = ¼` as the constant in clause (c) for `ξ` | `REFUTED`; the optimal value is `1/8` | Theorem 19bis.16 |
| Translation is the operation that creates detection | `REFUTED` | §17, withdrawn table |
| The Pólya cone is a detecting cone | `REFUTED` | §17, withdrawn table |
| `K_Q > 0` for the Epstein class | `REFUTED` | Corollary 18.6 |
| The separation of `ξ` from `Ξ_a` is "two polar exponents against four" | `REFUTED`; the true separator is `\|n^{½−(ρ±a)}\| = n^{∓a}` unbounded together with `W_a` indefinite | Lemma 20.34, Theorem 20.35 |
| Six weakenings of the trace clause (defect, primitive gate, fixed index, sparse cone, head/tail, bounded density) | `REFUTED` by one ray `tF + dK` | Theorem 20.37 |
| The earlier chain presented in the repository as a complete proof of RH | `REFUTED` as a proof; correct as a reduction to a uniformity statement | Proposition 18.21 |
| The tower form is never positive semidefinite at any chart | `REFUTED` as stated | §22, withdrawn table |

The corresponding claims that were withdrawn rather than disproved are listed
in the withdrawn table of each section.

### 23.4 What is open

Continuing the numbering of §14.5.

* **(24)** Clause (iii) on `E`: a proof of `I_∞(F,F) ≤ ½(\deg F)²` for every
  `F ≥ 0` from the structure of the carrier alone.  Constrained on both sides:
  it must fail for `ζ_K`-shaped data or else prove GRH (Remark 17.24), and it
  cannot pass through a bound on the Chebyshev remainder (Theorem 17.19).
  `OPEN` (Remark 17.28).
* **(25)** The attribution of the one-parameter criterion of Theorem 17.14 —
  whether it is in the literature (Fejér-kernel Weil positivity, Yoshida,
  Riesz-mean criteria).  `OPEN` (Remark 17.15).
* **(26)** A description of the ample cone that does not quantify over `I_∞`,
  without which the ample-cone equivalence is not usable.  `OPEN`
  (Remark 17.10a).
* **(27)** Item (23) of §14.5 in its corrected, one-sided form: is
  `Q(m) = o(m\sqrt{\log m})`?  That alone gives `h⁰_{\mathbb Z}(mK) = o(m²)`,
  and clause (c) forces `Q(m) ≫ m\sqrt{\log m}`.  `OPEN` (Corollary 18.30).
  The known upper bound at bounded rank imports a zero-free region (X23).
* **(27a)** Injectivity of `𝔫 ↦ Frob_𝔫` over a general number field: the
  inverse-semigroup law is proved for every number field (Theorem 19bis.3), but
  whether distinct ideals give distinct members is not.  `OPEN` (§19bis.1).
* **(27b)** A description of the moment cone `𝔐` — whether the containment of
  Proposition 19bis.21 can be turned into an intrinsic description of the
  classes with nonnegative moments.  `OPEN`.  This is *not* item (32): (32) is
  the sufficiency half of the exponential moment problem for the gate of §19.9,
  while this asks for the cone itself.
* **(27c)** The Connes–Consani counting function as a candidate for the `h⁰`
  slot: withdrawn as a refutation and standing `OPEN`, with its two unresolved
  points — the dictionary between the two notions of degree, and a dimension
  over the sphere spectrum against a real-valued functional (import (X17);
  §19bis.5).  `OPEN`.
* **(28)** The construction problem: a rule `Z ↦ h⁰_Z` on the admissible class
  `𝒵`, field-uniform, satisfying (a), (b′), (c) for every `ξ_K`, with the
  naming clause and the three acceptance tests.  `OPEN` (§18.6).  After
  Theorem 19.25 it is known that the clause list must be *changed*, not merely
  satisfied.
* **(29)** Base change beyond the abelian case, which is conditional on Artin
  holomorphy (X25).  `OPEN` (Theorem 18.20).
* **(30)** The Epstein analysis for non-principal forms; §18 proves it for
  principal `Q` with `h > 1`.  `OPEN`.
* **(31)** The cone constant `s_*^{cone}` — the infimum over the whole
  effective cone rather than over the zeros.  `OPEN` (§19.6).
* **(32)** The sufficiency half of the exponential moment problem, which is
  what blocks the one repair horn that the refutations leave standing.
  `OPEN` (§19.9).
* **(33)** `σ(\overline{\mathrm{Eff}})` in the function-field model for
  `g ≥ 2`; §21 settles `g = 1`.  `OPEN` (Theorem 21.17).
* **(34)** **(P145′)**: build a mechanism `(𝔐, 𝔈, H⁰, H²)` satisfying clauses
  (1)–(5) of §21.8, with `𝔈 = D^W` excluded.  `OPEN`.
* **(35)** Whether `Z[Gal(K/Q)]`, the ring that base change makes available,
  supplies the additive structure `Spec Z` lacks.  Nothing is claimed.  `OPEN`
  (Remark 22.18).
* **(36)** A class on the square carrying an explicit **phase** datum — the
  unimodularity of the local roots, with its falsifier version `α_± = p^{±a}` —
  rather than a magnitude.  Not constructed here, and not found in the
  literature this work has read.  `OPEN`.

### 23.5 The diagnosis, in one paragraph

The intersection theory of the arithmetic square is complete: the explicit
formula *is* it, and §§11, 17 and 21 show it has the shape of the intersection
theory of `C×C`.  What is missing is not the form but the *linear systems*.
The effective cone of the frame is the cone of Frobenius graphs, and it is
provably too thin — the deficit `s < 1` is not an artefact of the arithmetic,
since it appears on a curve over a finite field where the Riemann hypothesis
is a theorem (Theorem 21.15).  The ingredient the model names is the ring
structure on correspondences, the `+` of `Z[π]`: the frame has
`Frob_m ⋆ Frob_n = Frob_{mn}` and no addition, and `Spec Z` admits none
(Theorem 22.17).  The diagonal, the one datum that is computed rather than
chosen, is exact in its differences but is a function of `p`, `\log p`,
`p^{−k/2}` and the chart alone — pure magnitude, which this repository proves
three separate times cannot decide the sign.  Every construction inside the
frame is therefore either a restatement of RH or uniform in the falsifier
`Ξ_a`.  The honest summary is that this line of work converted row D from "find
`h⁰`" into a map with three walls — T1, T2, and the frame defect theorem — and
that the next genuine move must add a non-magnitude, non-archimedean datum with
Euler-product content, namely the phase of the unimodular local roots.  **No
such object exists here, and no sign is claimed, asserted or suggested.**

### 23.6 Reproduction (Part III)

```text
cd 03-research/phase-137-row-d-canonical-coupling/scripts
python3 d137_lattice.py                       # growth constants of §18.5

cd 03-research/phase-140-row-d-frobenius-square/scripts
python3 certify_chi.py                        # the optimal constant χ = 1/8 of §19bis

cd 03-research/phase-142-row-d-the-clause/scripts
python3 certify_sF.py                         # s_1, the degree threshold d_0
python3 certify_leakage.py                    # the zero-list-free leakage bound L

cd 03-research/phase-143-row-d-trace-positive-cone/scripts
python3 certify_s_star.py [--fast]            # s_* = 0.99845824…0.99846016

cd 03-research/phase-144-row-d-fixed-index/scripts
python3 certify_failing_index.py              # the Ξ_a polar block, the failing index

cd 03-research/phase-145-row-d-function-field-model/scripts
python3 sC_and_points.py                      # N_m, s_C* = √(7/11), the witness at d = 3

cd 03-research/phase-146-row-d-coupled-pairing/scripts
python3 cosh_test_cmn.py  [--fast]            # the cosh test on the sum classes
python3 tower_gram.py     [--fast]            # the single-prime tower Gram and its thresholds
```

Numerics illustrate and falsify; they prove nothing, and no number in Part III
is evidence for any sign.

---

**Part III claims no sign, asserts no sign, and suggests no sign.**  Its
deliverable is a **map with walls**: two constraints on any admissible proof
(Theorems 18.1, 18.16), one theorem that the clause list of Part II cannot be
satisfied (Theorem 19.25), one unconditional transfer theorem whose clause is
equivalent to RH rather than weaker than it (Theorems 20.17, 20.23), a model in
which the same defect appears where RH is known (Theorem 21.15), and one
computed datum (Theorem 22.11) that is so far sign-free.

---

# PART IV — the Galois ring, mixed effectivity, the additive pencil, the method theorems, and the closure of row D in the map

**Part IV records §§24–28.  It proves no sign and claims none.  Its statements
carry their own hypotheses; the labels are those of (1.12), together with
`METHOD-CONSTRAINT` for the statements about admissible *derivations* (as in
§18), `RESTATEMENT` for equivalences that reformulate rather than reduce, and
`HYPOTHESIS` for one unverified reading of a source, which is flagged as such at
the only place it is used, and `POINTER` for a statement whose proof is not
reproduced here, which then names its source file, section and label of record.
`METHOD-CONSTRAINT`, `RESTATEMENT`, `HYPOTHESIS` and `POINTER` are the additions
to the list of (1.12), and are used in Part IV only.  Cross-references to Parts I–III are by theorem
number; §§21–22 already record phases 145–146 and nothing here repeats them.
The numbering continues that of Part III, and §28 closes row D in the map.**

## 24. The Galois group ring and its inertness at `ζ`

*Provenance.  The statements and proofs of this section are taken from
`03-research/phase-147-row-d-galois-ring/R147_003b_ROUND3.md`
(§§R3.1–R3.7, items D.55.1′–D.55.10′) and
`R147_001_ROUND1.md` (item D.50.2), with the final labels, the
corrections of record and the list of withdrawals fixed by
`R147_005_CLOSING_DECISION.md`, checked against `R147_002_AUDIT.md`,
`R147_004_AUDIT_R2.md` and `R147_004b_CONFIRMATION.md`, and with the
corpus row from `CORPUS_CHECK_R147b.md`.  Nothing in this section asserts,
claims or suggests a sign.*

Theorem 22.17 says that `Spec Z` is terminal, so that the frame has the
multiplicative law `Frob_m ⋆ Frob_n = Frob_{mn}` and no addition: the ring
`Z[π]` of the model has no analogue.  Open item (35) of §23.4 asks whether
`Z[\mathrm{Gal}(L/F)]`, the ring that base change makes available, supplies the
missing `+`.  This section answers it: **the `+` exists, it is built, and it is
inert at the zeros of `ζ`.**

Throughout, `F` is a number field, `L/F` a **finite abelian** extension,
`G := \mathrm{Gal}(L/F)`, and `\widehat G` its character group — by class field
theory a group of primitive Hecke characters of `F` trivial on the norm group,
with `χ = 1` the trivial one.  Then

    ζ_L = ∏_{χ∈\widehat G}L(s,χ),   ξ_L = ∏_{χ∈\widehat G}Λ(s,χ),   Λ(s,1) = ξ_F ,

the conductor–discriminant factorization being exact in the weight-one
convention, so that the polar blocks of `ξ_L` and `ξ_F` are literally equal,
`P = \{0,1\}` (Theorem 18.20 and its proof).  Four classical inputs are used and
are labelled where they occur: **(H1)** for `χ ≠ 1` primitive, `Λ(\cdot,χ)` is
entire (Hecke); **(H2)** `Λ(s,χ) = W(χ)Λ(1−s,\barχ)` with `|W(χ)| = 1`, so that
`ρ ∈ Z(Λ(\cdot,χ)) ⟺ 1−ρ ∈ Z(Λ(\cdot,\barχ))` with multiplicity (Hecke;
Artin–Brauer); **(H3)** `\overline{Λ(\bar s,χ)} = Λ(s,\barχ)`; **(H4)**
Theorem 11.8(v), `I^{(1)}(E,2K_{ξ_F}) = \deg E`.  All of (H1)–(H3) are
`CLASSICAL`.

### 24.1 The radial collapse

**Lemma 24.1 (the radial realization is the identity; `PROVED`).**  Let
`σ ∈ \mathrm{Gal}(L/F)` and let `Γ_σ` be the graph correspondence of `σ` on the
idele class group.  Let `R : \mathrm{Corr}(C_{F,S}) → \mathrm{End}(D^W)` be the
radial realization, i.e. the action induced on functions of `\log|x|`.  Then
`R(Γ_σ) = \mathrm{id}`.  Consequently `Z[G]` acts on `D^W` through its
augmentation `Σ n_σ σ ↦ Σ n_σ`, and the cone `𝓔`, the form `I_∞`, the degree and
every `h⁰` candidate of §§11–19bis are unchanged by `G`.

*Proof.*  Every `σ` is an automorphism of `L` over `F` and therefore preserves
the idele modulus: `|σx|_{A_L} = |x|_{A_L}` for every idele `x`.  By
Definition 11.1 a class of `D^W` is a function of `t = \log|x|` alone.  Hence
`(Γ_σ)^*E = E` for every `E ∈ D^W`, which is the assertion `R(Γ_σ) =
\mathrm{id}`; the rest follows by `Z`-linearity.  ∎  `PROVED`

Lemma 24.1 says the group ring is invisible on the carrier of Parts I–III.  The
rest of this section builds the carrier on which it *is* visible, and shows that
what it does there is invisible at `ζ`.

### 24.2 The graded carrier, and the `+` it supplies

**Definition 24.2 (the carrier, the action, the form).**  Put

    𝒟_L := ⊕_{χ∈\widehat G}\big(D^W ⊗_R C\big),
    𝒟_L^{\,R} := \{E = (E_χ)_χ : \overline{E_χ} = E_{\barχ}\ \text{for all }χ\},
    Γ_σ·E := (χ(σ)E_χ)_χ\quad(σ∈G),\ \text{extended $Z$-linearly to } Z[G],

    I^{[χ]}(A,B) := Φ_A(0)Φ_B(1)+Φ_A(1)Φ_B(0)-\sum_{ρ∈Z(ξ_F)}Φ_A(ρ)Φ_B(1-ρ)
       \quad (χ = 1),
    I^{[χ]}(A,B) := -\sum_{ρ∈Z(Λ(·,χ))}Φ_A(ρ)Φ_B(1-ρ) \quad (χ ≠ 1),

    I^{(K)}(E,F) := \sum_{χ∈\widehat G} I^{[χ]}\big(E_χ,\ F_{\barχ}\big) ,
    ι : D^W → 𝒟_L^{\,R},\qquad ι(E) := (E)_χ .                              (24.1)

The grading is by **conjugate packets**: the `χ`-slot is paired against the
`\barχ`-slot.  This is forced — for complex `χ` the individual form is neither
real nor symmetric, since the zero multiset of `Λ(\cdot,χ)` is not
`ρ ↦ 1−ρ`-invariant, and only the packet restores A1.

**Theorem 24.3 (the form is well posed, symmetric and real; `ι` is an isometry;
`PROVED`).**
 (i) `Γ_σ` preserves `𝒟_L^{\,R}`;
 (ii) `I^{(K)}` is symmetric;
 (iii) `I^{(K)}` is real on `𝒟_L^{\,R}`;
 (iv) `I^{(K)}(ιE,ιF) = I_∞^{(L)}(E,F)`, the Weil form of `ξ_L` on `D^W` — at
   the level of the **total** form, and only there: no slot-wise identification
   is claimed;
 (v) `𝓝 := \mathrm{rad}\,I^{(K)} = \{E : Φ_{E_χ}(ρ) = 0\ ∀χ,\ ∀ρ∈Z(Λ(\cdot,χ)),
   \ Φ_{E_1}(0) = Φ_{E_1}(1) = 0\}`, and `ι^{-1}(𝓝) = 𝓝_∞^{(L)}`.

*Proof.*  Throughout, the re-indexings `ρ ↦ 1−ρ` and `ρ ↦ \barρ` rearrange the
zero sums; on `D^W(α)` this is licensed by their absolute convergence
(Lemma 18.4).  (i) is `\barχ(σ) = \overline{χ(σ)}`.  (ii) Re-index `χ ↦ \barχ`:
`I^{(K)}(F,E) = Σ_χ I^{[\barχ]}(F_{\barχ},E_χ)`, and by (H2) the substitution
`ρ ↦ 1−ρ` is a multiplicity-preserving bijection
`Z(Λ(\cdot,\barχ)) → Z(Λ(\cdot,χ))`, so
`I^{[\barχ]}(F_{\barχ},E_χ) = I^{[χ]}(E_χ,F_{\barχ})`; the `χ = 1` term is
symmetric by (11.6).  (iii) By (H3) and `\overline{Φ_A(\barρ)} = Φ_{\bar A}(ρ)`,
`\overline{I^{[χ]}(E_χ,F_{\barχ})} = I^{[\barχ]}(E_{\barχ},F_χ)`; sum and
re-index.  (iv) `Φ_{ιE}(ρ) = Φ_E(ρ)` in every slot and
`⊔_χ Z(Λ(\cdot,χ)) = Z(ξ_L)` with multiplicity, by (H1); the polar block is the
`χ = 1` one and equals that of `ξ_L`.  (v) Componentwise.  ∎  `PROVED`

**Theorem 24.4 (canonical class, degree, rulings, isometry; `PROVED`).**  Put
`K_L := (K_χ)_χ` with `Φ_{K_χ} = Ξ_χ := ½s(s−1)Λ(s,χ)`; then `K_{\barχ} =
\overline{K_χ}` by (H3), so `K_L ∈ 𝒟_L^{\,R}`, and `K_1 = K_{ξ_F}`.  Then:

 (i) `\deg E := I^{(K)}(E,2K_L) = \deg E_1`: **the degree sees only the trivial
   slot**;
 (ii) `\deg K_χ = 0` for every `χ ≠ 1`, so every `χ ≠ 1` slot is primitive; the
   normalising constant `\deg K_{ξ_F}` is base-dependent and equals `1` only for
   `F = Q`;
 (iii) the rulings `Φ(0)`, `Φ(1)`, hence the bidegree, live **only** in the
   `χ = 1` slot;
 (iv) `Γ_σ` is an isometry of `I^{(K)}` and preserves the degree, with no
   adjoint invoked;
 (v) `K_χ ∈ D^W ⊗ C` for every `χ`.

*Proof.*  (i) For `χ ≠ 1`,
`I^{[χ]}(E_χ,K_{\barχ}) = −Σ_{ρ∈Z(Λ(·,χ))}Φ_{E_χ}(ρ)\,Ξ_{\barχ}(1−ρ)`, and
`Ξ_{\barχ}(1−ρ) = 0` because `1−ρ ∈ Z(Λ(\cdot,\barχ))` by (H2); the `χ = 1` term
is `½\deg E_1` by (H4).  (ii) is (i) applied to `E = K_L`, together with the
computation of `\deg K_{ξ_F}` in the two instances of record (`\deg K_{ξ_Q} = 1`
by Theorem 11.8(v); `\deg K_{Q_𝔄} = ½` for `F` imaginary quadratic, Theorem
18.20's per-class computation).  (iii) `I^{[χ]}` has no polar block for `χ ≠ 1`
by (H1).  (iv) `I^{(K)}(Γ_σE,Γ_σF) = Σ_χ χ(σ)\barχ(σ)I^{[χ]}(E_χ,F_{\barχ}) =
I^{(K)}(E,F)`, and `\deg(Γ_σE) = 1(σ)\deg E_1 = \deg E`.  (v) For `F` imaginary
quadratic and `χ` a class-group character, `K_χ = Σ_𝔄 χ(𝔄)K_{Q_𝔄}` is a finite
combination of classes lying in `D^W(α)` for every `α > 0`.  For `F = Q` and `χ`
primitive mod `q`, `Λ(s,χ)` is the Mellin transform of
`θ_χ(u) = Σ_n χ(n)n^{δ}e^{−πn²u/q}` (`δ ∈ \{0,1\}` for `χ` even/odd), which is
`O(e^{−πu/q})` at `∞` and, by the theta transformation,
`O(u^{−½−δ}e^{−π/(qu)})` at `0`; applying `Π = −∂_t²+¼` as in (11.7) gives
`K_χ(t) = O(e^{Ct}e^{−c\,e^{2|t|}})`, which is the bound of Definition 11.1.
*(Hecke; Davenport §9; Iwaniec–Kowalski §4.6, `CLASSICAL`.)*  ∎  `PROVED`

**Theorem 24.5 (the character formula; `PROVED`, unconditional for abelian
`L/F`).**  For all `E,F ∈ 𝒟_L` and all `σ,τ ∈ G`,

    I^{(K)}(Γ_σE,\ Γ_τF) \;=\; \sum_{χ∈\widehat G} χ(στ^{-1})\;
      I^{[χ]}\big(E_χ,F_{\barχ}\big) .                                     (24.2)

*Proof.*  `(Γ_σE)_χ = χ(σ)E_χ` and `(Γ_τF)_{\barχ} = \barχ(τ)F_{\barχ}`, and
`I^{[χ]}` is bilinear, so the scalars come out as
`χ(σ)\barχ(τ) = χ(στ^{-1})`.  ∎  `PROVED`

**Remark 24.5a.**  No adjoint is used or needed.  Under the packet pairing the
second argument is drawn from the `\barχ`-slot and bilinearity alone produces
`\barχ(τ)`; the identity `I^{(K)}(Γ_σE,F) = I^{(K)}(E,Γ_{σ^{-1}}F)` is a
corollary of (24.2), not an input.  The character table enters the intersection
numbers exactly as the analogy predicts — on `𝒟_L`, and not on `D^W`, where
Lemma 24.1 applies.

### 24.3 The cone and its support function

**Definition 24.6.**  Write `π_G : C_{F,S} → R×G` for `x ↦ (\log|x|_{A_F},
\mathrm{Art}(x))`, `\mathrm{Art}` the Artin map of `L/F`.  Put

    𝓒 := \big\{(f_χ)_χ \;:\; f ∈ C_c^∞(R×G),\ f ≥ 0,\ f ≢ 0\big\},\qquad
    f_χ(u) := \sum_{g∈G}χ(g)f(u,g) .                                       (24.3)

Each `f_χ ∈ C_c^∞(R) ⊂ D^W ⊗ C`, and `\overline{f_χ} = f_{\barχ}` since `f` is
real, so `𝓒 ⊂ 𝒟_L^{\,R}`.  No point masses occur anywhere.  Write
`𝓔^∞ := 𝓔 ∩ C_c^∞(R)`.

**Standing qualifier.**  `𝓒` is a **model**, not a realization: `π_G` is a
projection, and for finite `S` the `S`-truncated class group surjects onto `G`
only when the primes of `S` generate `G`.  Theorem 24.8 is an equality for this
model and at most a `≤` for any genuinely realizable cone.  This is open item
(37) below, and every statement of §24.3 carries its qualifier.

**Theorem 24.7 (`PROVED`).**
 (a) `𝓒` is a convex cone and is `Z[G]`-stable, `Γ_g` acting by
   `f ↦ f(\cdot,g^{-1}\cdot)`, i.e. `f_χ ↦ χ(g)f_χ`;
 (b) the Galois action on `𝓒` is by translations of `C_{F,S}` by **norm-one**
   ideles: `|a| = 1`, so they fix `u` and move only the coset;
 (c) `ι(𝓔^∞) ⊂ 𝓒`, and the inclusion is strict;
 (d) *(degree gate)* `\deg(f_χ)_χ = \deg f_1 = ∫\big(Σ_g f(u,g)\big)
   2\cosh(u/2)\,du = Σ_g \deg f(\cdot,g) > 0` for `f ≥ 0`, `f ≢ 0`;
 (e) the `G`-invariant **elements** of `𝓒` are exactly those supported on the
   `χ = 1` slot.

*Proof.*  (a), (b) are immediate from (24.3) and from `|a| = 1`.  (c) `ιE` is
the image of `f = E⊗δ_{g=1}`; for strictness take `g ≠ 1`, choose `χ_1` with
`χ_1(g) ≠ 1` (`\widehat G` separates points of `G`) and `f := φ⊗1_{g}` with
`0 ≤ φ ∈ C_c^∞(R)`, `φ ≢ 0`; its image `(χ(g)φ)_χ` has `χ_1`-slot `χ_1(g)φ ≠ φ`,
so it is not constant across slots, while every `ι(E)` is.  (d) is
Theorem 24.4(i) together with Theorem 11.13(i).  (e) is Fourier inversion on the
finite abelian group `G`.  ∎  `PROVED`

**Remark 24.7a.**  With tests in `C_c^∞(R×G)` the cone contains `ι(𝓔^∞)` and not
`ι(𝓔)`; this is harmless for every constant computed here, since
`s(𝓔) = s(𝓔^∞)` by density and support functions are what is computed.

**Theorem 24.8 (the support function; `PROVED`).**  Let
`ρ = ½+iγ ∈ Z(Λ(\cdot,χ_0))` with `γ ≠ 0`, let `m := \mathrm{ord}(χ_0)` in
`\widehat G`, and let `s(γ,θ) := \sup_{u∈R}|\cos(γu+θ)|/\cosh(u/2)` be the
constant of Lemma 19.17.  Then

    S(γ,θ,m) := \sup_{E'∈𝓒}\frac{\big|\mathrm{Re}\big(e^{iθ}Φ_{E'_{χ_0}}(ρ)\big)
      \big|}{\tfrac12\deg E'} = \max_{0≤k<m} s\Big(γ,\ θ+\tfrac{2πk}{m}\Big) .
                                                                           (24.4)

*Proof.*  **(`≤`)**  For `E' = (f_χ)_χ`,

    \mathrm{Re}\big(e^{iθ}Φ_{f_{χ_0}}(ρ)\big)
      = \sum_{g∈G}∫ f(u,g)\cos\big(γu+θ+\arg χ_0(g)\big)\,du ,

each `f(\cdot,g)` being nonnegative, so Lemma 19.17 applies on each coset with
direction `θ_g := θ+\argχ_0(g)`:
`|∫f(\cdot,g)\cos(γu+θ_g)du| ≤ ½s(γ,θ_g)\deg f(\cdot,g)`.  Summing and bounding
`s(γ,θ_g) ≤ \max_k s(γ,θ+2πk/m)` gives `≤ ½(\max_k s)\deg E'` by
Theorem 24.7(d).  **(`≥`)**  Fix `k^*` attaining the maximum and `g^*` with
`\argχ_0(g^*) = 2πk^*/m`; fix `ε > 0` and `u^*` with
`|\cos(γu^*+θ_{g^*})|/\cosh(u^*/2) > s(γ,θ_{g^*})−ε`; take
`f := φ_δ⊗1_{g=g^*}` with `φ_δ ≥ 0` a `C_c^∞` bump of mass `1` supported in
`[u^*−δ,u^*+δ]`.  As `δ ↓ 0` the ratio tends to
`|\cos(γu^*+θ_{g^*})|/\cosh(u^*/2)` by continuity.  The index sets
`\{2πk/m\}` and `\{−2πk/m\}` coincide.  ∎  `PROVED`

**Proposition 24.9 (the `+`, with a bump; `PROVED`).**  Let `g ∈ G` and
`χ ∈ \widehat G` with `χ(g) = −1` (such a pair exists iff `|G|` is even).  For
any `0 ≤ φ ∈ C_c^∞(R)`, `φ ≢ 0`, the class `E' := (χ(g)φ)_χ ∈ 𝓒` is the image of
the **effective** test `φ⊗1_g` and has `χ`-coordinate `−φ`: a negative
coefficient in a basis in which every element of `ι(𝓔^∞)` has only nonnegative
ones.  In general the coordinates are `(χ(g))_χ`, roots of unity.

*Proof.*  Immediate from (24.3) and Theorem 24.7(a).  ∎  `PROVED`

Proposition 24.9 is the arithmetic analogue of the model's class
`[Γ_i] = ½[Γ_π] − ½[Δ] − F_1 + F_2` on a curve over a finite field (§21), by the
same mechanism: a root of unity multiplying the zero datum.  **The `+` exists.**

### 24.4 Inertness at `ζ`

**Theorem 24.10 (the `χ = 1` slot is untouched; `PROVED`).**

 (i) **The `χ = 1` slot of `𝓒` is exactly `𝓔^∞`.**  For `E' = (f_χ)_χ ∈ 𝓒`,
   `f_1 = Σ_{g∈G}f(\cdot,g)`, a finite sum of nonnegative `C_c^∞` functions, so
   `f_1 ∈ 𝓔^∞` (and `f_1 ≢ 0` because `f ≥ 0`, `f ≢ 0`); conversely every
   `0 ≤ φ ∈ C_c^∞(R)`, `φ ≢ 0`, arises as `f_1` for `f := φ⊗1_{g=1}`.  Hence
   `\{E'_1 : E' ∈ 𝓒\} = 𝓔^∞`.
 (ii) **The support function at the `χ = 1` slot is unchanged:** for every
   `ρ = ½+iγ ∈ Z(ξ_F)` with `γ ≠ 0` and every `θ ∈ R`,

       \sup_{E'∈𝓒}\ \frac{\big|\mathrm{Re}\big(e^{iθ}Φ_{E'_1}(ρ)\big)\big|}
         {\tfrac12\deg E'} \;=\; S(γ,θ,1) \;=\; s(γ,θ) ,                   (24.5)

   for **every** abelian `L/F`, every tower, and every order `m` occurring in
   `\widehat G`.

*Proof.*  (i) is the displayed computation.  (ii) `\mathrm{ord}(1) = 1`, so the
index set of Theorem 24.8 is `\{0\}` and every rotation there is trivial; and
`\deg E' = \deg E'_1` by Theorem 24.4(i), so the ratio is exactly the one of
Lemma 19.17 evaluated on `E'_1 ∈ 𝓔^∞`, whose supremum is `s(γ,θ)` by (i)
together with the two halves of Theorem 24.8 at `m = 1`.  ∎  `PROVED`

**Remark 24.10a (why).**  Write `t` for the coset-averaging map; then
`f_1 = |G|\,t(E')`, i.e. the `χ = 1` slot *is* the coset average, and the Galois
action is by norm-one ideles, which fix `u = \log|x|` and move only the coset
(Theorem 24.7(b)).  A coset average cannot see the enlargement.  This is
Lemma 24.1 seen one level up, and the identity `f_1 = |G|\,t(E')` makes it
literal.

**Remark 24.10b (two cautions).**  (a) Theorem 24.7(e) — the `G`-invariant
*elements* of `𝓒` are those supported on the `χ = 1` slot — is true, is
compatible, and is **not** what Theorem 24.10 uses: Theorem 24.10 is about the
`χ = 1` **component of every element** of `𝓒`, invariant or not, and is proved
by `f_1 = Σ_g f ≥ 0`.  The inference "invariant sector, hence support function
unchanged" is a non sequitur and is withdrawn.  (b) There is no "unique `χ_ρ`":
`Z(ξ_L) = ⊔_χ Z(Λ(\cdot,χ))` is a multiset union and nothing known excludes a
zero of `ζ_F` from also lying in `Z(Λ(\cdot,χ))` for some `χ ≠ 1`.  Every
statement above says "at the `χ = 1` slot", never "at a zero of `ζ_F`, `m = 1`".

**Corollary 24.11 (`PROVED`).**  The frame defect theorem for `ξ`
(Theorem 19.25) stands verbatim after the enlargement: at every zero of `ζ_F`
the support-function constant is `s(γ,θ)`, hence the deficit `s_* < 1` of
Proposition 19.18 is unchanged, for every abelian `L/F` and every tower.  ∎

**Remark 24.12 (what the enlargement does move).**  By Theorem 24.8 the
constants at the `χ ≠ 1` slots do move: `σ(γ,m) := \min_θ S(γ,θ,m)` increases
with `m` in the divisibility order, and `S(γ,π/2,m) = 1` exactly when `4 ∣ m`.
The source proves, analytically and not by grid, that `σ(γ,m) < 1` for every
finite `m`; the statement and its proof are at
`R147_003b_ROUND3.md` §R3.4 (Theorem D.55.7′(i),(ii)) and are **not
reproduced here**.  `POINTER`, label of record `PROVED`.  The clause "`S = 1` for
`4 ∣ m` is the first support function in row D to reach `1`" is withdrawn:
`s(γ,0) = 1` always, by (19.2).  These constants bear on a transfer theorem for
`ζ_L`, not on `ζ_F`, and that is open item (38).

**Remark 24.13 (the Epstein class on the graded carrier).**  The principal
Epstein class is the trace `t(Γ_{𝔄^{-1}}K_{H/K})` of a graded class under a
non-isometric projection, with `t(𝓒) ⊆ 𝓔`; and `K_H ∉ \overline{𝓒}` (proved for
`x²+ky²` with `k` large, certified for the listed discriminants).  This is where
the `Ξ_Q` falsifier belongs on the graded carrier: a **sum** of `L`-functions,
not a product.  Statement and proof at `R147_003b` §R3.6, Theorem D.55.10′;
`POINTER`, label of record `PROVED` / `CERTIFIED` by route.

**Remark 24.14 (a by-product).**  `Σ_{σ≠1}\#\mathrm{Fix}(σ) = \log|d_K| =
Σ_χ χ(1)\log 𝔣(χ)` (Hilbert's different formula together with the
conductor–discriminant formula): the character table enters through
**conductors**, not through zero sums.  `CLASSICAL`, `RESTATEMENT`.

**Reading of record.**  The `+` exists, is built, and lives entirely in the
non-trivial isotypic sectors — that is, at the zeros of the `L(s,χ)`, `χ ≠ 1`.
The zeros of `ζ_F` live in the sector where the group ring acts trivially.
Phases 145–147 have now named and tested the missing ingredient three times:
`Spec Z` has no ring of correspondences (Theorem 22.17); where a ring exists, it
is invisible on the radial carrier (Lemma 24.1); where a carrier sees it, it acts
away from the zeros of `ζ` (Theorem 24.10).  **No sign is claimed, asserted or
suggested.**

### Withdrawn in this section

| claim | why | status |
|---|---|---|
| "the character table enters the intersection numbers" on `D^W` | refuted by Lemma 24.1 (the collapse); true on `𝒟_L` by Theorem 24.5 | `WITHDRAWN` on `D^W`, confirmed on `𝒟_L` |
| `K ∈ 𝓔` as a discovery of the phase | already Theorem 11.7(i) | `WITHDRAWN` as a result |
| an effective class with zeros right of `1` via Epstein | replaced by the trivial witness `E = 3e^{−t²}+e^{−(t−\log2)²}`, whose `Φ_E` vanishes on `\mathrm{Re}\,s = ½+\log3/\log2`; the Epstein grid is illustration only | `WITHDRAWN`, replaced |
| "the enlargement kills the horn *enlarge the effective cone*" | non sequitur: the horn is about the support function | `WITHDRAWN` |
| "the first support function in row D to reach `1`" (`S(γ,π/2,m) = 1` for `4∣m`) | `s(γ,0) = 1` always, by (19.2); the statement says only that the `μ_m`-orbit of `π/2` meets `πZ`, a direction Theorem 19.25 never uses | `WITHDRAWN` |
| "the defect theorem may choose `θ`" | no `L(s,χ)`-analogue of Definition 19.19–Theorem 19.23 exists | `WITHDRAWN`; open item (38) |
| `\dim H⁰ ≤ 1` on `𝒟_L`, "multiplicity is the missing object" | `(Z[G]E)^G` is not the sections functor of clause (a) | `WITHDRAWN` as a slogan |
| `\deg K_L = 1` over any base | false: `\deg K_{Q_𝔄} = ½` for `F` imaginary quadratic | `WITHDRAWN`; restricted to `F = Q` (Theorem 24.4(ii)) |
| "invariant sector, hence support function unchanged" | non sequitur; the conclusion stands by Theorem 24.10(i),(ii) | `WITHDRAWN` (Remark 24.10b(a)) |
| "if `ρ` is a zero of `ζ_F` then `m = 1`" | not a lemma; an open problem | `WITHDRAWN` (Remark 24.10b(b)) |

---

## 25. Mixed effectivity on the full square

*Provenance.  The statements and proofs of this section are taken from
`03-research/phase-148-row-d-mixed-effectivity/R148_003_ROUND2.md`
(§§R1–R11, items D.55.5′–D.55.8′, D.56.1′–D.56.4′, D.56.8′) and
`R148_001_ROUND1.md` for the definitions, with the final labels, the
corrections of record and the withdrawals fixed by
`R148_005_CLOSING_DECISION.md`, checked against `R148_002_AUDIT.md`
and `R148_004_CONFIRMATION.md`, and with the corpus row on
`03-research/phase-41-build-G2/125-construction-of-the-intersection-form.md`.  Nothing in
this section asserts, claims or suggests a sign.*

§24 shows that the additive structure Galois theory supplies commutes with the
radial projection.  This section tests the remaining move: keep the square, drop
the radiality, and impose a positivity **constraint** coupling the two sectors.

The carrier is `𝒦 = (T) ⊕ (R)`, where `(T)` is the space of translation kernels
`k_Φ(u,v) := Φ(v−u)` with `Φ ∈ D^W`, and `(R)` is the finite real span of
rank-one kernels `φ⊗ψ`, `(φ⊗ψ)(u,v) := φ(u)ψ(v)`.  The sum is direct.  On `𝒦` a
symmetric bilinear form `B` is defined blockwise: on `(T)×(T)` it is the
regularized trace `I_∞` of Definition 11.4; on `(T)×(R)` and `(R)×(R)` it is the
honest trace of a trace-class operator, with

    B(k_Φ,\ φ⊗ψ) = ∫_R Φ(w)\,χ_{φ,ψ}(w)\,dw ,\qquad
    χ_{φ,ψ}(w) := ∫_R φ(u)ψ(u+w)\,du .                                     (25.1)

**Definition 25.1 (mixed effectivity; the tropical correlation).**  For
`φ_1,…,φ_n,ψ_1,…,ψ_n : R → R` and `P := Σ_{i≤n}φ_i⊗ψ_i ∈ (R)` put
`q_w(u) := Σ_i φ_i(u)ψ_i(u+w)` and

    (⊛P)(w) := \sup_{u∈R} q_w(u) \qquad (\text{max-plus correlation}) ;

for `n = 1` write `φ⊛ψ`.  A kernel `k = k_Φ − P` is **mixed effective** if
`k ≥ 0` pointwise on `R×R`.  The **translation shadow** of the mixed cone `(M)`
is `𝓣(M) := \{Φ ∈ D^W : ∃P ∈ (R),\ k_Φ − P ∈ (M)\}`.

**Theorem 25.2 (the tropical characterisation, at every finite rank;
`PROVED`).**  For `Φ ∈ D^W` and `P ∈ (R)`,

    k_Φ − P ≥ 0 \ \text{ on } R×R \iff Φ(w) ≥ (⊛P)(w) \ \text{ for every } w∈R .

*Proof.*  `k_Φ(u,v) − P(u,v) ≥ 0` reads `Φ(v−u) ≥ Σ_iφ_i(u)ψ_i(v)` for all
`(u,v)`; substitute `v = u+w` and take the supremum in `u` at fixed `w`.  Only
the order of the quantifiers is used, and `n` plays no role.  ∎  `PROVED`

**Lemma 25.3 (nonnegativity of the tropical correlation; `PROVED`,
unconditional).**  Let `φ,ψ : R → R` be measurable, `w ∈ R`, and
`p_w(u) := φ(u)ψ(u+w)`.

 (i) *(nonnegative factors: no hypothesis at all)*  If `φ ≥ 0` and `ψ ≥ 0` then
   `(φ⊛ψ)(w) ≥ 0`.
 (ii) *(signed factors: the escape costs the weaker block)*  `(φ⊛ψ)(w) < 0`
   holds **iff** there is `ε > 0` with `p_w(u) ≤ −ε` for **every** `u ∈ R`; in
   that case `|p_w| ≥ ε` everywhere, so `p_w ∉ L¹(R)` and `χ_{φ,ψ}(w) = −∞`.
 (iii) If `p_w ∈ L¹(R)` then `(φ⊛ψ)(w) ≥ 0`; in particular when `φ,ψ ∈ L²(R)`,
   and when `φ,ψ` are continuous with `p_w(u) → 0` along some sequence
   `|u| → ∞`.

*Proof.*  (i) A supremum of nonnegative numbers is nonnegative.  (ii)
`\sup_u p_w = −ε < 0` is by definition `p_w ≤ −ε` everywhere; then
`∫|p_w| ≥ ∫ε\,du = +∞` and `∫p_w = −∞`.  (iii) If `p_w ≤ −ε < 0` everywhere then
`∫|p_w| = +∞`, so `p_w ∈ L¹` forbids it and (ii) gives the conclusion;
`φ,ψ ∈ L²` gives `‖p_w‖_1 ≤ ‖φ‖_2‖ψ‖_2 < ∞` by Cauchy–Schwarz; and along a
sequence with `p_w → 0`, `\sup_u p_w ≥ \lim_n p_w(u_n) = 0`.  ∎  `PROVED`

**Lemma 25.4 (the continuity plug; `PROVED`).**  Let `Φ ∈ D^W`, so `Φ ∈ C²(R)`
by Definition 11.1, and let `P ∈ (R)` satisfy `Φ ≥ ⊛P` pointwise.  Put
`W^- := \{w : (⊛P)(w) < 0\}`.  If `Φ(w_0) < 0` for some `w_0` then by continuity
`Φ < 0` on a nonempty open interval `I ∋ w_0`, and `I ⊆ W^-`.  Hence an
enlargement of the translation shadow beyond `𝓔 ∪ \{0\}` requires `⊛P < 0` on a
nonempty **open** set: a null set, or any set with empty interior, cannot
enlarge the shadow.  ∎  `PROVED`

**Lemma 25.5 (finite rank; `PROVED`).**  Fix `w`.  (i) If `q_w ∈ L¹(R)` then
`(⊛P)(w) ≥ 0`; in particular if `φ_i(\cdot)ψ_i(\cdot+w) ∈ L¹` for each `i`, and
in particular if every `φ_i,ψ_i ∈ D^W`, by (11.1).  (ii) Conversely, if
`(⊛P)(w) < 0` then `q_w ≤ −ε < 0` everywhere, so `q_w ∉ L¹`, so at least one
generator has `χ_{φ_i,ψ_i}(w) = ±∞`: the `(T)×(R)` block of `B` is then
undefined at `w`.

*Proof.*  Both parts are Lemma 25.3(ii),(iii) applied to `q_w` in place of
`p_w`, together with linearity of the integral: if every
`∫φ_iψ_i(\cdot+w)` were finite, `∫q_w` would be finite, contradicting
`∫q_w = −∞`.  ∎  `PROVED`

**Theorem 25.6 (the kill, at every finite rank; `PROVED`).**  Let
`k = k_Φ − P` with `P ∈ (R)` and `k ≥ 0`, and suppose `q_w ∈ L¹(R)` for almost
every `w` (the minimum required for `B` to be defined on `k`).  Then `Φ ≥ 0`
pointwise, and

    𝓣(M) \;=\; 𝓔 ∪ \{0\} .                                                 (25.2)

*Proof.*  `⊆`: by Theorem 25.2, `Φ ≥ ⊛P`; by Lemma 25.5(i), `(⊛P)(w) ≥ 0` at
almost every `w`, so `Φ ≥ 0` off a null set, and `Φ ∈ C²` gives `Φ ≥ 0`
everywhere (Lemma 25.4).  `⊇`: take `P = 0`.  ∎  `PROVED`

**Remark 25.6a.**  The `⊇` half takes `P = 0` and therefore uses the square not
at all; it is recorded only to make the equality exact.  All the content is in
`⊆`.

**Theorem 25.7 (both signs, both quadrants; `PROVED`).**  Let `P ∈ (R)`,
`Φ ∈ D^W`, and suppose `q_w ∈ L¹` at almost every `w`.  Then

    k_Φ − P ≥ 0 \quad\text{or}\quad k_Φ + P ≥ 0 \qquad\Longrightarrow\qquad Φ ≥ 0 .

*Proof.*  `k_Φ + P = k_Φ − (−P)` with `−P ∈ (R)` and `χ_{−φ_i,ψ_i} =
−χ_{φ_i,ψ_i}` finite exactly where `χ_{φ_i,ψ_i}` is, so both cases are
Theorem 25.6.  Explicitly at rank one: `k_Φ + φ⊗ψ ≥ 0` reads
`Φ(w) ≥ −\inf_u φ(u)ψ(u+w)`, and `\inf_u φ(u)ψ(u+w) > 0` at a given `w` means
`φ(u)ψ(u+w) ≥ ε > 0` for every `u`, whence `χ_{φ,ψ}(w) = +∞`; while if the
infimum is `≤ 0` the constraint reads `Φ(w) ≥ −\inf ≥ 0`.  ∎  `PROVED`

**Corollary 25.8 (`PROVED`).**  Only pairs with `χ_{φ,ψ} ≡ −∞` on a nonempty
open set `W^-` could enlarge the shadow, and for those `B(k_Φ,φ⊗ψ) = −∞` for
every `Φ ∈ D^W` positive on a positive-measure subset of `W^-`.  Hence
(25.2) holds on the **entire domain of definition of `B`**, and there is no
intermediate carrier between "shadow `= 𝓔`" and "`B` undefined against an open
cone of translation tests."

*Proof.*  Lemma 25.4 supplies the open set `W^-`; Lemma 25.3(ii) gives
`χ_{φ,ψ} = −∞` there; (25.1) then gives `B(k_Φ,φ⊗ψ) = −∞`.  ∎  `PROVED`

**Corollary 25.9 (nothing moves; `PROVED`).**  The support-function constant of
the mixed cone equals that of `𝓔`: `s^{(M)}(γ,θ) = s(γ,θ)`, so
`s^{(M)}(γ_1,π/2) = s_1 = 0.99846016…` unchanged (Proposition 19.18); and the
relaxed clause `(b′)^+_X` formed with the mixed cone is equivalent to `(b′)^+`
and fails at the same witness `tF_0 + dK` (Theorem 19.23, Corollary 19.24).

*Proof.*  Both are corollaries of (25.2) and of nothing else: the square
contributes no class to the shadow, so every supremum and every witness is the
one computed on `𝓔` in §19.  ∎  `PROVED`

**Theorem 25.10 (no common radial representation; `PROVED`).**  There is **no**
linear map `R : 𝒦 → D^W` with `B(k,k_Φ) = ∫R(k)(w)\,w_Φ(w)\,dw` for every
`k ∈ 𝒦` and every `Φ ∈ D^W`.  Equivalently, `B(\cdot,k_Φ)` is represented on
`(T)` by the Weil density `w_Φ` and on `(R)` by `Φ` itself, and these differ: at
`Φ = 2K`, `w_{2K}(w) = 2\cosh(w/2)` is unbounded and increasing in `|w|`, while
`2K` is positive and decays faster than every exponential (Theorem 11.7(ii)).
∎  `PROVED`

**Theorem 25.11 (the `(T)×(R)` block is zero-blind; `PROVED`).**  The pairing
`⟨Frob_n, φ⊗ψ⟩ = χ_{φ,ψ}(\log n)` is finite and, for `φ,ψ ≥ 0`, nonnegative: the
first finite nonnegative Frobenius pairing in row D.  Its integrand
`X(w)χ_{φ,ψ}(w)` is built from the measure `du\,dv` and the functions `X,φ,ψ`
alone; **no zero, pole, Euler factor or `L`-function occurs in it.**  It is a
count that sees the radial variable and nothing arithmetic.  No claim is made
about suprema of that term over any cone.

*Proof.*  Both assertions are read off (25.1) and Definition 25.1.  ∎  `PROVED`

**Remark 25.11a.**  Consequently the second term of the mixed pairing is not a
function of any class's coset data: `Φ_N(0) = Φ_N(1) = Φ_N(ρ) = 0` for
`N ∈ 𝓝_∞` says nothing about `∫Nχ_{φ,ψ}`, which by Theorem 19.30's criterion
disqualifies it from refuting `(b′)^+` — the instrument the argument would have
used.

**Remark 25.12 (the three blocks are two prescriptions).**  `B` is a single
well-defined symmetric bilinear form, but the three blocks are computed by
**two inequivalent prescriptions** — regularized on `(T)×(T)`, honest traces
elsewhere — glued along the direct-sum decomposition, and by that alone.  The
gluing is legitimate and empty: the two prescriptions are not two views of one
functional, and Theorem 25.10 measures the gap.  The passage from `(R)` to `(T)`
by diagonal averaging is not a limit of `B`; `B` is `T_a`-invariant and
`T_a k_Φ = k_Φ`, which is all that statement says.

**Problem 25.13 (O-148.2, the principal residue).**  Does there exist a real
vector space `𝒦'` of generalized kernels on `X = R×R` and a finite-valued
symmetric bilinear form `B'` on `𝒦'` such that

 (α) `𝒦' ⊇ (T)` and `B'|_{(T)×(T)} = I_∞`, so that the zero data of `ξ` is
   carried (Theorem 11.5);
 (β) `𝒦'` contains the two degenerate fibre classes `f_1 = "R×\{v_0\}"`,
   `f_2 = "\{u_0\}×R"` as distributions, with `B'(f_1,f_2)` finite and nonzero;
 (γ) `B'` is invariant under the diagonal translations `T_a`, so that the form
   is a property of the square and not of a chart;
 (δ) the analogue of a degree exists?

`OPEN`.  Theorems 25.6 and 25.7 answer `𝒦' = (T) ⊕ (R)` in the negative on (β)
and (δ), and about no other `𝒦'`.  On a compact toy square `C_p × C_p` the answer is
affirmative on (β) and (γ) — a stable tropical intersection gives the integer
`f_1·f_2 = 1`, `T_a`-invariant — and negative on (δ) in the regime that matters:
integral on the thin lattice, real on the continuous flow, with the signature not
persisting to infinite rank and eventual positivity circular.  On `C_Q × C_Q` the
fibre classes have infinite measure and that normalisation is not defined, so the
toy answer does not transfer.  `IMPORTED` for the toy model; `OPEN` for (α)
together with (β)–(γ).

**Reading of record.**  Mixed effectivity is a **tropical** condition, and it
enters row D vacuously.  For nonnegative factors `Φ ≥ φ⊛ψ` *implies* `Φ ≥ 0`
with no decay, growth or integrability hypothesis whatsoever; for signed factors
the escape is coextensive with the destruction of the weaker block of `B`.
Everything the new sector contributes is either nonnegative by construction —
hence a restatement of `Φ ≥ 0` — or infinite, hence outside the form.  This is
the same mechanism as in §§22 and 24, one level up.  **What is proved is that *this*
form is trivial and zero-blind on *its* domain; it is not proved that the square
admits no intersection theory, and this section does not say that it is.**  No
sign is claimed, asserted or suggested.

### Withdrawn in this section

| claim | why | status |
|---|---|---|
| "`(φ⊛ψ)(w) ≥ 0` for every pair for which the `(R)×(R)` block of `B` is finite" | false: `φ ∈ L²` does not imply `φ(u) → 0` (witness: `φ = n` on intervals of width `n^{−3}` about `u = n`) | `WITHDRAWN`; replaced by Lemma 25.3 |
| the collapse is structural because the `(R)×(R)` block is Hilbert–Schmidt | the loophole between the two blocks is real (a growing `ψ` keeps `(T)×(R)` finite while `(R)×(R)` diverges) | `WITHDRAWN`; the collapse holds for a stronger reason (Lemma 25.3(i), Corollary 25.8) |
| "the three blocks are the three restrictions of one composition trace" | refuted by the divergence of Remark 25.12: no single trace functional restricts to both prescriptions | `WITHDRAWN`; replaced by Remark 25.12 |
| "the density anomaly" as a tension inside `B` | `B` is one well-defined form; the two displays pair different arguments through different representations | `RENAMED` Theorem 25.10, content unchanged |
| "no linear map represents `B(\cdot,k_Φ)` blockwise" | false as stated: the blockwise map exists; what fails is a common one, and it is not an averaging limit | `WITHDRAWN`, corrected in Theorem 25.10 |
| the `k_Φ + φ⊗ψ ≥ 0` quadrant as "the one direction the collapse does not close", flagged probably ill-posed | it is the `−` quadrant with signed data, `k_Φ + P = k_Φ − (−P)` | `WITHDRAWN`; `CLOSED` by Theorem 25.7 |
| "the second term is numerically identical for `ξ`, `Ξ_a`, `Ξ_Q` and every `ζ_K`" | true pointwise, false for any optimised quantity, since the admissibility constraint couples the sectors | `DOWNGRADED` to Theorem 25.11 |
| "`B` diverges linearly in `Λ`" as a phenomenon | it is `T_a`-invariance, trivially | `RESTATED` (Remark 25.12) |
| "the square admits no intersection theory" | what is proved is that this form is trivial on its own domain, and nothing wider | `WITHDRAWN` |
| the phase-41 corpus row "not used below" | it is the same object one level up; its `f_1·f_2 = 1` is Problem 25.13 made concrete | `CORRECTED` |

---

## 26. The additive pencil and the Deligne extraction

*Provenance.  The statements and proofs of this section are taken from
`03-research/phase-149-row-d-additive-pencil/R149_001_ROUND1.md`
(items D.59–D.63) as repaired by `R149_003_REPAIRS.md` (repairs (i)–(vi)), with
the labels of record, the reclassifications and the amendments fixed by
`R149_005_CLOSING_DECISION.md`, whose §4 governs wherever it differs from
the repair round, and checked against `R149_002_AUDIT.md`.  Nothing in
this section asserts, claims or suggests a sign; no zero-free region, moment
bound or cancellation estimate is proved anywhere in it.*

The route tested here is Deligne's: bound one fibre of a family by the whole
family, and pay the family's size by a `2k`-th root.  The family is the Farey
family of additive twists `e(na/q)`, `q ≤ Q = N^{c}`; the distinguished fibre is
`α = 0`, where the sum is the Chebyshev remainder.  The section states what the
extraction is, exactly; measures the kill test at `k = 1`; computes the
coinvariant block and proves it zero-blind; and records what the family-moment
hypothesis really is.

Throughout, `w ∈ C_c^∞(0,∞)` with `\mathrm{supp}\,w ⊆ [1,2]`, `w ≥ 0`;
`ψ_w(N) := Σ_n Λ(n)w(n/N)`; `\widehat w(0) := ∫_0^∞ w(u)du > 0`; `Q = N^{c}` with
`0 < c < 1`; and for a model `M : N → C`,

    S̃_M(α;N) := Σ_n (Λ(n) − M(n))\,e(nα)\,w(n/N),\qquad
    M_{2k}(N) := Σ_{q ≤ Q} Σ^{*}_{a \bmod q} |S̃_M(a/q;N)|^{2k} .          (26.1)

### 26.1 The model, and the dichotomy it satisfies

**Definition 26.1 (admissible model).**  `M` is *admissible at level `Q`* if
 **(E)** `Σ_n M(n)w(n/N) = N\widehat w(0) + O_w(N^{1/2})`;
 **(C)** for every `q ≤ Q` and `(a,q) = 1`,
   `Σ_n M(n)e(na/q)w(n/N) = (μ(q)/φ(q))N\widehat w(0) + O_{A,w}(QN^{-A})` for
   every `A > 0`;
 **(B)** `Σ_n|M(n)|²w(n/N) ≪ N(\log N)^{O(1)}`.

**Proposition 26.2 (the model dichotomy; `PROVED`, with the third item
`IMPORTED`).**

 1. The **Selberg-type sieve majorant**
   `Λ_Q^{\mathrm{Sel}}(n) := Σ_{d\mid n,\ d ≤ Q}μ(d)\log(Q/d)` **fails (E)**.
   Indeed, Poisson summation gives
   `Σ_{m≥1}w(dm/N) = (N/d)\widehat w(0) + O_A((d/N)^A)` for `d ≤ N`, whence
   `Σ_nΛ_Q^{\mathrm{Sel}}(n)w(n/N) = N\widehat w(0)Σ_{d≤Q}μ(d)\log(Q/d)/d +
   O_A(Q^{1+A}N^{-A})`, and by Mellin
   `Σ_{d≤Q}μ(d)\log(Q/d)/d = \frac1{2πi}∫Q^{s}\frac{ds}{s²ζ(s+1)} =
   1 + O\big(\exp(−c(\log Q)^{3/5}(\log\log Q)^{-1/5})\big)`, the pole at `s = 0`
   being simple with residue `1` because `1/ζ(1+s) = s+O(s²)`, and the remaining
   error being exactly the Vinogradov–Korobov error, import (X20a).  Since
   `N\exp(−c(\log Q)^{3/5}) ≫ N^{1/2+ε}` for `Q = N^{c}`, (E) fails; worse, the
   error is itself of prime-number-theorem strength, so the chain would be
   circular.
 2. The **trivial model** `M ≡ 1` satisfies (E) and (B) exactly but **fails
   (C)**, fatally: for `q > 1`, `Σ_n e(na/q)w(n/N) = O_A(N^{-A})`, so
   `S̃_1(a/q;N) = S(a/q;N) + O_A(N^{-A})` with
   `S(α;N) := Σ_nΛ(n)e(nα)w(n/N)`; the classical major-arc asymptotic gives
   `S(a/q;N) = (μ(q)/φ(q))N\widehat w(0) + O(N\exp(−c\sqrt{\log N}))` for
   `q ≪ (\log N)^{A}`, so `|S̃_1(a/q;N)| ≍ N/φ(q)` for squarefree such `q`, and
   `M_{2k}(N) ≫_k N^{2k}` for `k ≥ 2`, the series `Σ_qμ²(q)φ(q)^{1−2k}`
   converging.  Against the required `N^{k+2c+o(1)}` and `k ≥ 2 > 2c`, the
   hypothesis is false.
 3. The **truncated singular-series model**
   `M_Q(n) := Σ_{q ≤ Q}(μ(q)/φ(q))\,c_q(n)` is **admissible**.  *(This is
   Vaughan's truncated-singular-series main term; attribution recorded,
   `IMPORTED`, not claimed.)*  *Proof of (C).*  Since
   `c_q(n) = Σ^{*}_{b\bmod q}e(nb/q)`,
   `Σ_n M_Q(n)e(na/q_0)w(n/N) = Σ_{q≤Q}(μ(q)/φ(q))Σ^{*}_{b}Σ_n
   e(n(b/q+a/q_0))w(n/N)`; by Poisson the inner sum is
   `N\widehat w(0)+O_A(N^{-A})` when `b/q+a/q_0 ∈ Z` and `O_A(N^{-A})` otherwise,
   and the congruence has a solution iff `q = q_0`, then `b ≡ −a`.  Taking
   `q_0 = 1` gives (E) with error `O_A(QN^{-A})`.  *(B)* By the orthogonality of
   Ramanujan sums (Lemma 26.11a), `Σ_{n≤N}|M_Q(n)|² = N(\log Q+C)+O(Q²)` for
   `Q ≤ N^{1/2}`; for `Q > N^{1/2}` use `|M_Q(n)| ≪ τ(n)\log Q` and
   `Σ_{n≤N}τ(n)² ≪ N\log^3N`.  ∎  `PROVED`

**Lemma 26.3 (evaluability, for every `c < 1`; `PROVED`).**  For
`M = M_Q` with `Q = N^{c}`, `0 < c < 1` fixed,
`Σ_n M_Q(n)w(n/N) = N\widehat w(0) + O_A(N^{-A})` for every `A > 0`: the spacing
at `q_0 = 1` is `Q^{-1}`, not `Q^{-2}`, so the Poisson step is uniform for every
`c < 1`.

*Proof (a corollary of Proposition 26.2(3)).*  Expand the Ramanujan sum,
`c_q(n) = Σ^*_{b\ \mathrm{mod}\ q}e(nb/q)`, and exchange the finite sums:
`Σ_nM_Q(n)w(n/N) = Σ_{q≤Q}(μ(q)/φ(q))Σ^*_bΣ_ne(nb/q)w(n/N)`.  Poisson summation
with `\widehat w ∈ 𝒮(R)` gives, for every `A ≥ 1` and every real `β`,

    Σ_n e(nβ)w(n/N) = N\widehat w(0)·1[β ∈ Z] + O_A\big(N(1+N‖β‖)^{-A}\big) ,

`‖β‖` the distance to the nearest integer.  At `β = b/q` with `(b,q) = 1`,
`q ≤ Q`, one has `‖b/q‖ = 0` only for `q = 1`, contributing exactly
`(μ(1)/φ(1))N\widehat w(0) = N\widehat w(0)`.  For `q ≥ 2`, `‖b/q‖ ≥ 1/q ≥ Q^{-1}`
— only the single denominator `q` occurs, since `q_0 = 1`, so the spacing is
`Q^{-1}` and not `Q^{-2}` — whence `N‖β‖ ≥ N^{1−c} → ∞`.  Summing over the at
most `Σ_{q≤Q}φ(q) ≤ Q²` pairs `(q,b)` with `|μ(q)/φ(q)| ≤ 1`, the total error is
`≪_A Q²N^{1−A(1−c)} = N^{1+2c−A(1−c)}`, which is `O(N^{-A'})` for any prescribed
`A'` on choosing `A > (1+2c+A')/(1−c)`.  ∎  `PROVED`

(This is the closing step of Proposition 26.2(3) — "taking `q_0 = 1` gives (E)
with error `O_A(QN^{-A})`" — made uniform in `c`; the `Q^{-2}` spacing, and with
it the threshold `c = 1/2`, is a feature of (C) at `q_0 > 1` only.  Cf.
`R149_003_REPAIRS.md` §1.2, Lemma D.59.0c, label of record `PROVED`.)

Theorem 26.4, Corollary 26.5,
Theorem 26.6 and Proposition 26.8 depend on (E) only, hence hold for every
`c < 1`.  The full strength of (C) at `q_0 > 1` is proved for `c < 1/2` and only
there; its averaged form `(C′)` is **`OPEN`**, its large-sieve justification
being false exactly in the range where it was invoked.

### 26.2 The extraction, stated honestly

**Theorem 26.4 (the extraction; `PROVED`).**  Fix `w`, fix `c ∈ (0,1)`, put
`Q = N^{c}`, `M = M_Q`.  Suppose that for every `k ≥ 1` there are constants
`C_k, B_k` with

    (H(k,c))\qquad M_{2k}(N) \;≤\; C_k(\log N)^{B_k}\,Q²\,N^{k}\qquad (N ≥ 2).
                                                                           (26.2)

Then `ψ_w(N) − N\widehat w(0) ≪_{w,ε} N^{1/2+ε}` for every `ε > 0`.

*Proof.*  The pair `(q,a) = (1,1)` lies in the range of summation and
`a/q = 0`, so dropping every other term gives
`|S̃(0;N)|^{2k} ≤ M_{2k}(N) ≤ C_k(\log N)^{B_k}Q²N^{k}`; taking `2k`-th roots,
`|S̃(0;N)| ≤ N^{1/2+c/k+o(1)}`.  By Lemma 26.3,
`S̃(0;N) = ψ_w(N) − N\widehat w(0) + O_A(N^{-A})`.  Given `ε > 0` choose
`k > c/ε`.  ∎  `PROVED`

**Remark 26.4a (what Theorem 26.4 is, exactly).**  It is a **Hölder
inequality**, `‖\cdot‖_∞ ≤ ‖\cdot‖_{2k}` on the finite family, chained with a
Farey dissection and `k → ∞`.  It is *not* a transfer of the extraction lemma of
Weil I, 3.2: what plays the role of "the poles of the family's `L`-function do
not move with `k`" is only the `k`-independence of the family factor `Q²`, which
is an assumption inside (26.2) and not a theorem.  The chain of steps is
folklore; it was found nowhere stated in this form and is recorded as *a folklore
chain, first written down here* — not as a discovery.  `PROVED` /
`RESTATEMENT`.

**Corollary 26.5 (`H(k,c)` for all `k` and the family `w_θ` implies RH;
`PROVED`).**  Assume (26.2) for every `k ≥ 1` and for every member of the family
`w_θ(u) := w(u)u^{θ}`, `θ ∈ R`.  Then RH holds.

*Proof.*  Fix `θ`.  For `\mathrm{Re}\,s > 1`, substituting `N = n/u`,
`∫_0^∞ψ_{w_θ}(N)N^{-s-1}dN = (−ζ'/ζ)(s)\,W(s+θ)` with
`W(s) := ∫_0^∞w(u)u^{s-1}du` entire and `W(1) = \widehat w(0) > 0`.  Splitting
at `N = 1` and subtracting the pole term,

    ∫_1^∞\big(ψ_{w_θ}(N) − W(1+θ)N\big)N^{-s-1}dN
      = (−ζ'/ζ)(s)W(s+θ) − W(1+θ)/(s−1) − E_θ(s),

with `E_θ` entire.  By Theorem 26.4 the integrand is `≪ N^{1/2+ε}`, so the left
side converges absolutely and is analytic on `\mathrm{Re}\,s > 1/2`; hence so is
the right side.  If `ζ` had a zero `ρ` with `\mathrm{Re}\,ρ > 1/2`, then
`−ζ'/ζ` has a pole at `ρ` with positive integer residue and `ρ ≠ 1`, so
analyticity forces `W(ρ+θ) = 0`.  As `θ` ranges over `R`, `ρ+θ` ranges over a
horizontal line, so `W` would vanish on a set with a limit point, hence
`W ≡ 0` — contradicting `W(1) > 0`.  ∎  `PROVED`

**Theorem 26.6 (the continuous form; `PROVED`).**  Suppose that for every
`k ≥ 1` and every `ε > 0`, `∫_0^1|S̃(θ;N)|^{2k}dθ ≪_{k,ε} N^{k+ε}`.  Then
`\sup_θ|S̃(θ;N)| ≪_ε N^{1/2+ε}`.

*Proof (Bernstein).*  `S̃(\cdot;N)` is a trigonometric polynomial of degree
`≤ 2N`.  Let `V := \sup_θ|S̃|`, attained at `θ_0`.  Bernstein's inequality gives
`‖S̃'‖_∞ ≤ 4πNV`, so `|S̃(θ)| ≥ V/2` for `|θ−θ_0| ≤ 1/(8πN)`, a set of measure
`≥ 1/(4πN)`.  Hence `∫_0^1|S̃|^{2k} ≥ (V/2)^{2k}/(4πN)`, i.e.
`V ≪_k N^{1/2+(1+ε)/2k}`; let `k → ∞`.  ∎  `PROVED`

**Theorem 26.7 (what the continuous hypothesis is equivalent to; `PROVED` for
the equivalence).**  The assertion "`∫_0^1|S̃(θ;N)|^{2k}dθ ≪_{k,ε}N^{k+ε}` for
every `k`" is **equivalent** to `\sup_θ|S̃(θ;N)| ≪_ε N^{1/2+ε}` (call this
`ATRH`).  Moreover `ATRH` implies, for every primitive `χ` mod `q ≤ Q = N^{c}`,

    ψ_w(N,χ) = \frac{τ(χ)}{q}Σ^{*}_{a}\barχ(a)\,S̃(a/q;N)
       + Σ_n M_Q(n)χ(n)w(n/N)
       ≪ q^{1/2+ε}N^{1/2+ε} + q^{1/2}N^{c+o(1)} ,

which is of GRH quality uniformly in `q ≤ N^{c}` when `c ≤ 1/2`, and of quality
`q^{1/2+ε}N^{c+ε}` when `c > 1/2`.

*Proof.*  `(⇒)` is Theorem 26.6; `(⇐)` is trivial.  For the twisted bound, the
first term is finite Fourier inversion with `|τ(χ)| = \sqrt q`; the model's own
contribution is bounded by writing `c_r(n) = Σ_{d\mid(r,n)}dμ(r/d)`, so that
`Σ_nM_Q(n)χ(n)w(n/N) = Σ_{r≤Q}(μ(r)/φ(r))Σ_{d\mid r}dμ(r/d)χ(d)Ψ_χ(N/d)` with
`Ψ_χ(Y) := Σ_mχ(m)w(m/Y) ≪_w q^{1/2}\log q` uniformly in `Y`, by partial
summation against `w` and Pólya–Vinogradov (`CLASSICAL`, used only as an upper
bound); assembling and using `Σ_{r≤Q}σ(r)/φ(r) ≍ Q` gives
`≪ q^{1/2}N^{c+o(1)}`.  ∎  `PROVED`

**Remark 26.7a.**  `ATRH` is strictly stronger in content than RH: it asserts
square-root cancellation at Diophantine-generic irrational `θ`, where no
`L`-function conjecture applies at all and the strongest unconditional bound
remains of Vinogradov type, `N^{4/5+ε}`.  A formal non-implication is not
available and is not claimed; `OPEN`.

**Proposition 26.8 (`Ξ_a`-uniformity: the extraction carries no arithmetic;
`PROVED`).**  Theorems 26.4 and 26.6 hold verbatim with `Λ` replaced by **any**
sequence `(b_n)` of complex numbers and `M_Q` by any model satisfying (E).  In
particular, for the falsifier `Ξ_a(s) := ξ(s+a)ξ(s−a)` [typo `+` corrected  to the product of Remark 11.8a, whose log-derivative gives the weights below], `0 < a < ½`, with
`Λ_a(n) := Λ(n)(n^{a}+n^{-a})`, the extraction runs unchanged.

*Proof.*  No step of §26.2 uses any property of `Λ` beyond being a sequence
supported on `[1,2N]`.  ∎  `PROVED`

**Consequence of record.**  The extraction is a statement about trigonometric
polynomials.  All the arithmetic is inside the hypothesis (26.2), and
Proposition 26.21(1) shows that it is: `H(k,c)` is **false** for `Λ_a` once
`k > c/a`.

### 26.3 The kill test at `k = 1`, and the `c = 1/2` boundary

**Theorem 26.9 (`PROVED`).**
 (i) *(exponent identity)*  (26.2) yields exactly
   `ψ_w(N) − N\widehat w(0) ≪ N^{1/2+c/k+o(1)}`, which is `o(N)` **iff**
   `c < k/2`: for `k = 1`, iff `c < 1/2`; for `k ≥ 2`, for every admissible `c`.
 (ii) *(the hypothesis at `k = 1` is the large sieve)*  For `N^{1/2} ≤ Q ≤ N`,
   `M_2(N) ≪ Q²N\log N`, i.e. `H(1,c)` holds with `B_1 = 1` for every
   `c ∈ [1/2,1)`.
 (iii) *(the boundary is exact)*  For `c < 1/2` the large sieve gives only
   `M_2 ≪ N²\log N`, exceeding the required `Q²N = N^{1+2c}` by `N^{1−2c} → ∞`.

*Proof.*  (i) is Theorem 26.4's display.  (ii) The Farey points are
`δ`-spaced with `δ = Q^{-2}`, since `‖a/q − a'/q'‖ ≥ 1/(qq') ≥ Q^{-2}`; the
Montgomery–Vaughan large sieve (`CLASSICAL`) gives
`Σ_{q≤Q}Σ^{*}_a|Σ_n c_ne(na/q)|² ≤ (N+Q²)Σ_n|c_n|²` for coefficients supported
in `[N,2N]`, and here `c_n = (Λ(n)−M_Q(n))w(n/N)` has
`Σ_n|c_n|² ≪ N\log N` by (B); with `Q ≥ N^{1/2}`, `N+Q² ≪ Q²`.  (iii) is the
same inequality with `N+Q² ≍ N`.  ∎  `PROVED` (the deduction), `CLASSICAL`
(the ingredient)

**Corollary 26.10 (`PROVED`).**  The extraction applied to Theorem 26.9(ii)
gives `|ψ_w(N) − N\widehat w(0)| ≪ QN^{1/2}(\log N)^{1/2} = N^{1/2+c+o(1)} ≥ N`
for every `c ≥ 1/2`: **worse than the trivial bound.**  Hence

> `H(1,c)` is **proved exactly for `c ∈ [1/2,1)`**, and there the extraction is
> vacuous; it becomes **useful exactly for `c ∈ (0,1/2)`**, and there it is
> `OPEN` (it follows from GRH by finite Fourier inversion, and is unproved).

The two ranges are complementary and disjoint.  That is the outcome of the kill
test at `k = 1`, and the boundary `c = 1/2` is exact.  ∎

**Remark 26.10a (the `k ≥ 2` interpolation).**  Hölder,
`M_{2k} ≤ ‖S̃‖_∞^{2k−2}M_2`, gives extraction exponent `N^{1−1/2k+c/k}`, which
is `≥ N` for every `k` in the proved range: interpolation from `k = 1` is
vacuous for every `k`.  `PROVED`.  The known counterexamples to Hooley's
conjecture do not refute (26.2): the Fiorilli–Martin and Hayani mechanism is
RH-compatible and its contribution at the relevant level is negligible, with the
`2k`-power leg proved by Siegel–Walfisz alone and only for `k = 1`, `c > 1/2`
(`k < 2c`).  Nothing unconditional is known for `k ≥ 2` in the direction of an
upper bound; the unconditional `Ω`-results of de la Bretèche–Fiorilli and
Harper–Soundararajan are of Gaussian order and, checked against (26.2), yield no
contradiction.  `CERTIFIED` (the shapes of the two `Ω`-results, not read in the
phase); `IMPORTED` (Siegel–Walfisz).

### 26.4 The coinvariant block: what the additive square computes for free

**Lemma 26.11a (Ramanujan orthogonality; `CLASSICAL`).**  For `q,q' ≥ 1` and
`d ∈ Z`, `\lim_{X→∞}X^{-1}Σ_{n≤X}c_q(n)c_{q'}(n+d) = δ_{q,q'}c_q(d)`; in
particular `\{c_q\}` is an orthogonal system with `‖c_q‖² = c_q(0) = φ(q)`.
*(Carmichael 1932; Ramanujan 1918.)*

**Theorem 26.11 (the additive density pairing; `PROVED`).**  For `h ∈ Z`, `q`
with `(h,q) = 1`, let `A_{q,h} := \{p \text{ prime} : p ≡ h\ (\mathrm{mod}\ q)\}`
and let `⟨A,B⟩ := \lim_{X→∞}\#\{p ≤ X : p ∈ A∩B\}/π(X)` be the relative density
inside the primes.  Then `⟨A_{q,h},A_{q',h'}⟩ = 1/φ([q,q'])` if
`h ≡ h'\ (\mathrm{mod}\ (q,q'))` and `0` otherwise.  Setting
`T_h := Σ_{q ≤ Q}μ²(q)φ(q)^{-1}[A_{q,h}]` and retaining the `q = q'` block,

    ⟨T_h, T_{h'}⟩_{\mathrm{diag}} = κ(h−h') := Σ_{q\mid h−h'}\frac{μ²(q)}{φ(q)}
      = \frac{d}{φ(d)}\quad (d := h−h' ≠ 0),
    κ(0) = Σ_{q ≤ Q}\frac{μ²(q)}{φ(q)} = \log Q + C_0 + o(1) ,             (26.3)

with `C_0 = γ + Σ_p\frac{\log p}{p(p−1)}`.

*Proof.*  The Gram entry is the Chinese remainder theorem (the intersection is
empty or a single class mod `[q,q']`, coprime to it) together with Dirichlet's
theorem in the form `π(X;m,b) \sim π(X)/φ(m)` for fixed `m`.  Normalising the
generators to unit length and restricting to `q = q'`, the `q`-th diagonal term
is `μ²(q)/φ(q)` when `q \mid d` and `0` otherwise; summing over `q ≤ Q` and
letting `Q → ∞` (the sum is finite for `d ≠ 0`) gives the first form.  The closed
form `Σ_{q\mid d}μ²(q)/φ(q) = d/φ(d)` holds because both sides are
multiplicative and at `p^a` both equal `1+1/(p−1) = p/(p−1)`.  For `d = 0` every
`q ≤ Q` divides `0`, and Landau's estimate gives the stated asymptotic.  ∎
`PROVED`

**Remark 26.11b (normalisation of record).**  The squarefree weight `μ²(q)` is
not optional: with it the closed form is `d/φ(d)`, and it is the object the model
`M_Q` produces, `M_Q` being supported on squarefree `q` through `μ(q)`.

**Theorem 26.12 (positive-definiteness, and why it is not progress;
`RESTATEMENT`).**  `κ` is a positive-definite function on `Z`; so is the full
(non-diagonal) Gram matrix; and so is the Hardy–Littlewood singular series
`𝔖(d) := Σ_{q≥1}μ²(q)c_q(d)/φ(q)²`.

*Proof.*  `\mathbf 1[q\mid d] = q^{-1}Σ_{a\bmod q}e(ad/q)`, so
`κ(d) = Σ_q\frac{μ²(q)}{qφ(q)}Σ_{a\bmod q}e(ad/q)`, a convergent combination of
unitary characters of `Z` with nonnegative coefficients, hence positive-definite
by Bochner's theorem.  For `𝔖`, `c_q(d) = Σ^{*}_ae(ad/q)` is already a sum of
characters with coefficient `1` and `μ²(q)/φ(q)² ≥ 0`.  The Gram matrix is
positive semidefinite because it is the Gram matrix of a genuine density inner
product.  ∎

**Warning attached to Theorem 26.12.**  *This positivity is free.*  It holds
because `κ` and `𝔖` are, by construction, autocorrelations of a nonnegative
measure.  The corpus has met the pattern three times before — §25's "either
nonnegative by construction or infinite", §24's inertness, and the sterility of
an index computed from the same data on both sides — and this is the fourth
instance.  **Label: `RESTATEMENT`, not progress.**

**Theorem 26.13 (zero-blindness; `PROVED`).**  `κ`, `𝔖` and the whole Gram
matrix are functions of the local densities `1/φ(q)` and `c_q(d)` alone.  They
depend on `ζ` only through its Euler factors, i.e. only through data in
`\mathrm{Re}\,s > 1`.  Replacing `ζ` by `Ξ_a` — same Euler factors up to the
elementary twist `n^{\pm a}`, different zeros — leaves them unchanged.  **No
zero of `ζ` appears in any of them.**  ∎  `PROVED`

**Corollary 26.13a.**  No inequality derived from `κ` alone can bound
`\mathrm{Re}\,ρ`.  ∎

**Theorem 26.14 (the coinvariant block, and the archimedean discrepancy;
`PROVED` for the identity and the subtraction).**  With
`S(α;N) := Σ_nΛ(n)e(nα)w(n/N)`,

    Σ_{q ≤ Q}Σ^{*}_{a\bmod q}|S(a/q;N)|²
      = Σ_{m,n}Λ(m)Λ(n)w(m/N)w(n/N)\,κ_Q(m−n),\qquad
    κ_Q(d) := Σ_{q ≤ Q}c_q(d) ,                                            (26.4)

and, in the Barban–Davenport–Halberstam normalisation
`V(x;Q) := Σ_{q≤Q}Σ^{*}_a(ψ(x;q,a) − x/φ(q))²`, the Montgomery–Hooley theorem
(`CLASSICAL`) gives `V(x;Q) = xQ\log Q − c_0xQ + O_A(\cdots)` with
`c_0 = γ + \log2π + 1 + Σ_p\frac{\log p}{p(p−1)}`, so that, by (26.3),

    V(x;Q) = xQ\big(κ_Q(0) − \log 2π − 1\big) + o(xQ) .                    (26.5)

*Proof.*  (26.4) is `Σ^{*}_{a\bmod q}e((m−n)a/q) = c_q(m−n)` after expanding
`|S|²` and exchanging sums.  (26.5) is the subtraction `c_0 − C_0 = \log2π+1`.
∎  `PROVED` (the identity and the subtraction), `CLASSICAL` (the
Montgomery–Hooley input), `CERTIFIED` (the value of `c_0`)

**Reading.**  The main term of the variance is computed **a priori**, by
Ramanujan orthogonality and Dirichlet densities, without knowing a single zero:
it is exactly the coinvariant block of the scheme, the part an invariant theory
computes for free.  The discrepancy `(\log2π+1)xQ` is archimedean — the
`Γ`-factor and the pole of `ζ` — and the additive pairing, a sum of finite local
densities, cannot and does not see it.  The bad news is Theorem 26.13: the block
is zero-blind, so knowing it perfectly gives nothing, and the error term is the
whole problem.

### 26.5 Exponents add, or subtract: the finding of record

**Theorem 26.15 (Landau is useless on the additive square; `PROVED`).**  Let
`R(n) := Σ_{m+m'=n}Λ(m)Λ(m') ≥ 0` and `𝓡(s) := Σ_{n≥1}R(n)n^{-s}`.  Landau's
theorem (import (X20)) applies, `𝓡` being singular at its abscissa of
convergence `σ_c`; but `σ_c = 2`, unconditionally and a priori, because
`Σ_{n≤x}R(n) ≍ x²`.  Every singularity coming from the zero blocks sits at
`\mathrm{Re}\,s = β+β' ≤ 2`, never above the top pole.  **Hence the unique real
singularity Landau detects is `s = 2`, which is known before any zero is
considered, and Landau returns no information about `β`.**  ∎  `PROVED`

Compare Theorem 17.14, where the same lemma *is* decisive: there
`G(z) = 2z^{-2}(ξ'/ξ)(½+z)` has its only real singularity at `z = 0`, and the
zeros contribute poles at `w_ρ = ρ − ½`, **which can lie to the right of the
abscissa**.  The difference is structural: the multiplicative square pairs `ρ`
with `1−\barρ`, so exponents **subtract** and the top pole sits at the critical
value; the additive square pairs `ρ` with `ρ'`, so exponents **add** and the top
pole sits at the trivial value `2`.

**Theorem 26.16 (twisting kills the additive positivity; `PROVED`).**  For a
non-principal `χ`, `R_χ(n) := Σ_{m+m'=n}Λ(m)χ(m)Λ(m')χ(m')` is not nonnegative
and Landau's lemma does not apply.

*Proof.*  The nonnegativity of `R` comes from `Λ ≥ 0`, not from being a square:
`χ(m)Λ(m)` has modulus `Λ(m)` and argument a root of unity, and `R_χ(n)` is
genuinely complex.  Structurally, `Σ_nR_χ(n)n^{-s}` is, up to elementary
factors, a double Mellin transform of `(−L'/L(\cdot,χ))^{⊗2}`, with no
positivity.  ∎  `PROVED`

**Contrast (`PROVED`, trivial and load-bearing).**  On the multiplicative square
`|ψ(x,χ)|²` is nonnegative for **every** `χ`, being literally a square: Rankin
positivity is twist-stable, and Landau's lemma is available after every twist.

**Theorem 26.17 (what transports, and what does not; `PROVED` for (1)–(3),
`RESTATEMENT` for the framing).**

*Transports that exist.*  **(T1)** For every `q ≥ 2`, with
`V_Λ(x;q) := Σ^{*}_{a\bmod q}(ψ(x;q,a) − φ(q)^{-1}Σ_{n≤x,(n,q)=1}Λ(n))²`,

    V_Λ(x;q) \;=\; φ(q)^{-1}Σ_{χ ≠ χ_0}|ψ(x,χ)|² ,                         (26.6)

by Plancherel on `(Z/q)^{×}` — the left side a second moment on the additive
square (the `q`-block of `M_2`, by (26.4)), the right side a sum of Rankin
squares on the multiplicative square.  `CLASSICAL`.  **(T2)** Under RH, the
additive short-interval variance and Montgomery's pair correlation are
equivalent (Goldston–Montgomery 1987, `IMPORTED`).  Both are transports of
second moments of counting functions at fixed `x`; both are RH-conditional or
`k = 1`; **both are sign-free.**

*What they fail to carry.*
 1. **Positivity and index.**  Neither transports an index or a signature.  On
   the additive square `κ` and `𝔖` are positive-definite (Theorem 26.12), so
   there is no negative eigenvalue to count; on the multiplicative square
   `|ψ(x,χ)|² ≥ 0` is twist-stable and is exactly the positivity Landau consumes
   (Theorem 26.16).  The identity (26.6) equates two **numbers**; it does not
   equate the structures that make one of them Landau-usable.
 2. **`k ≥ 2`.**  (T1) is Parseval, i.e. the `k = 1` invariant theory and nothing
   more.  For `k ≥ 2` the additive `2k`-fold energy and the `2k`-th moments of
   `ψ(x,χ)` are related only by Hölder in the loss-making direction,
   `Σ_χ|ψ_χ|^{2k} ≤ (Σ_χ|ψ_χ|²)^{k}`, which costs exactly the cancellation one
   is trying to prove.  There is no `k ≥ 2` analogue of (26.6).
 3. **Polar structure.**  (T1) is an identity of counting functions at fixed
   `x`, not an identity of Dirichlet series in `s`.  The family object
   `Σ_χ|ψ(x,χ)|²` has no Euler product and no functional equation in `s`, hence
   no a priori polar divisor; the additive side has one, dominated by the trivial
   pole at `s = 2` (Theorem 26.15).

**Statement of the wall.**  *The moment-level transport between the two squares
is classical, `RH`-conditional or `k = 1`, and sign-free.  What does not
transport is the polar/positivity structure: no known construction produces an
object that is simultaneously (a) a square, hence Landau-positive after every
twist, and (b) equipped with an a priori polar divisor determined by local data.
Over a finite field one object is both.  Over `Z`, the singular series `𝔖(d)` and
the pairing `κ(d)` exist only as **densities**, never as **residues**.*  ∎

**Finding of record for §26.5.**  Theorems 26.15–26.16: **exponents add on the
additive square and subtract on the multiplicative square.**  The earlier
wording, "nothing known transports between the two squares", is withdrawn: the
moment-level transports (26.6) and Goldston–Montgomery exist and are classical.

### 26.6 What the family-moment hypothesis really is

**Proposition 26.18 (`PROVED`).**  With `b_n := (Λ(n)−M_Q(n))w(n/N)`,

    M_{2k}(N) = Σ_{d∈Z}κ_Q(d)\,𝒞_{2k}(d),\qquad
    𝒞_{2k}(d) := Σ_{n_1+\cdots+n_k − m_1−\cdots−m_k = d}
      b_{n_1}\cdots b_{n_k}\bar b_{m_1}\cdots\bar b_{m_k} ,                (26.7)

with `κ_Q(0) = Σ_{q≤Q}φ(q) = (3/π²)Q² + O(Q\log Q)` and
`κ_Q(d) ≪ Q^{1+ε}` for `d ≠ 0`.

*Proof.*  Expand `|S̃(a/q)|^{2k}`, sum over `a` using
`Σ^{*}_{a\bmod q}e(da/q) = c_q(d)`, and exchange the order of summation.  ∎
`PROVED`

**Reading.**  By (26.7), `H(k,c)` is equivalent to a `2k`-fold **additive-energy**
bound for the centered prime measure together with control of the off-diagonal.
For `k = 1`, `𝒞_2(0) = Σ_n|b_n|² ≪ N\log N` is trivial, and that is *why* `k = 1`
is a theorem: **the `k = 1` invariant theory is Parseval, and nothing more.**
For `k ≥ 2`, `𝒞_{2k}(0)` is a genuine `2k`-fold correlation of primes.

**Corollary 26.19 (`PROVED`; the off-diagonal clause is a hypothesis, not a
consequence).**  Assume `H(2,c)` **together with** the off-diagonal bound

    Σ_{d ≠ 0}κ_Q(d)\,𝒞_4(d) = o(Q²N²) .                                   (26.9a)

Since `M_4(N) = Σ_dκ_Q(d)𝒞_4(d)` with `κ_Q(0) ≍ Q²` (Proposition 26.18), the two
together isolate the `d = 0` term and give, by Parseval in `d`,

    𝒞_4(0) = Σ_{|d| ≤ 2N}|𝒞_2(d)|² ≪ (\log N)^{B_2}N² ,\qquad
    𝒞_2(d) = Σ_n b_n\,\bar b_{n+d}\ \text{(with the }w\text{-weights)} ,

whence `Σ_{|d|≤2N}|𝒞_2(d)| ≪ N^{3/2+o(1)}` by Cauchy–Schwarz: the
Goldbach/twin-prime correlation with square-root cancellation on average.  Since
`M_Q` is zero-blind (Theorem 26.13), the zero term
`H(x) = −2Σ_ρ x^{1+ρ}/(ρ(1+ρ))` of the average Goldbach formula is not absorbed
by the centering, so a zero with `β > ½` would contribute `≫ x^{1+β}` and violate
the bound.  Hence **`H(2,c)` together with (26.9a) implies RH.**  Without
(26.9a) no isolation of the `d = 0` term is available: `𝒞_4(d)` is complex and
unbounded in sign for `d ≠ 0`, and no bound on it is proved anywhere in §26.

*Citations, in their correct roles.*  The sharp half — the equivalence
`Σ_{n≤x}R(n) = x²/2 + O(x^{3/2+ε}) ⟺ RH` — is **Granville**, Funct. Approx.
Comment. Math. **37** (2007), 159–173, Theorem 1A, together with the
Corrigendum, ibid. **38** (2008), 125–127, the 2007 proof having been incomplete;
the converse direction is Fujii and Languasco–Zaccagnini.  `IMPORTED`.
**Bhowmik–Ruzsa**, Analysis Mathematica **44** (2018), Theorem 2.1, gives only
quasi-RH: from `Σ_{n≤x}R(n) = x²/2 + O(x^{2−δ})` it deduces `β < 1 − δ/6`, i.e.
`β < 11/12` at `δ = ½`; its virtue is that the proof is elementary.  `IMPORTED`.
Bhowmik–Schlage-Puchta's unconditional `Ω(x\log\log x)` calibrates from below:
the *unaveraged* error cannot be pushed past `x\log\log x`.  `IMPORTED`.
**Difficulty verdict:** `H(2,c)` sits at or above RH — above, because it demands
in addition full uniformity in `q ≤ Q`; and the off-diagonal control (26.9a) is
not part of `H(k,c)` and is not implied by RH.  This is a lower bound on the difficulty, not a theorem about
zeros.  ∎  `PROVED`

**Problem 26.20 ((P149), reclassified).**  The problem the route poses — exhibit
a structure `𝒢` acting on the additive pencil, with an invariant theory bounding
`M_{2k}(N)` by `C_k(\log N)^{B_k}Q²N^{k}` for `k ≥ 2`, without using the location
of the zeros of any single `L(s,χ)` and compatibly with the known large
deviations of the fibres — is, by Proposition 26.18 and Corollary 26.19, **the
Hardy–Littlewood `k`-tuple conjecture with square-root error on average, in a
different costume.**  It is not a new object to create.  `OPEN`; label of record
**reclassified**, and not pursued.

**Proposition 26.21 (the falsifiers; `PROVED`).**
 1. **`Ξ_a`.**  The extraction is `Ξ_a`-uniform (Proposition 26.8), but `H(k,c)`
   is **false** for `Λ_a` whenever `k > c/a`: by Proposition 26.8 it would give
   `ψ_{a,w}(N) − (\text{main}) ≪ N^{1/2+c/k+o(1)}`, while the explicit formula
   for `Ξ_a` forces an oscillating term `≫ N^{1/2+a}` from the zeros at
   `½+a+iγ`, by Landau's oscillation theorem applied to the rightmost off-line
   zero.  **Hence all the arithmetic is inside `H(k,c)`**, and a proof of it
   would have to distinguish `Λ` from `Λ_a` in the analytic continuation and
   functional equation of the fibres — not in their Euler factors, which `Ξ_a`
   shares up to `n^{\pm a}`, and not in `κ` or `𝔖`, which `Ξ_a` shares exactly
   (Theorem 26.13).
 2. **`Ξ_Q`.**  The construction does not apply: the model `M_Q` is derived from
   the major-arc behaviour of `Λ`, which rests on the Euler product, and the
   Epstein function has none; with zeros right of `1` (import (X21)) the
   hypothesis is not even formulable at the right normalisation.  **The
   construction presupposes the Euler product.**
 3. **`ζ_K`.**  Everything in §§26.1–26.5 is field-uniform: replace `Z` by
   `O_K`, the Farey family by ideals of norm `≤ Q`, and `c_q` by the
   `O_K`-Ramanujan sums; Theorem 26.9(ii) holds by the number-field large sieve
   (Huxley 1968; Schaal 1970) with the same `N + Q²` shape, hence the same
   boundary `c = 1/2`.  ∎  `PROVED`

### Withdrawn in this section

| claim | why | status |
|---|---|---|
| the extraction is a transfer of the extraction lemma of Weil I, 3.2 | it is a Hölder inequality `‖\cdot‖_∞ ≤ ‖\cdot‖_{2k}` chained with a Farey dissection; the `k`-independence of the family factor is assumed, not proved | `WITHDRAWN` as a transfer; `PROVED` as stated in Theorem 26.4 |
| the Selberg sieve majorant as the model | fails (E), with an error of prime-number-theorem strength; the chain would be circular | `REFUTED` (Proposition 26.2(1)) |
| the trivial model `M ≡ 1` | fails (C); `M_{2k} ≫ N^{2k}` for `k ≥ 2` | `REFUTED` (Proposition 26.2(2)) |
| the truncated singular-series model as a new object | it is Vaughan's truncated singular-series main term | `IMPORTED`, attribution recorded |
| `(C′)`, the averaged form of (C), as proved by the large sieve | the justification is false exactly in the range where it was invoked | `WITHDRAWN`; demoted to a plausibility clause, `OPEN` |
| "nothing known transports between the two squares" (D.61.10 as first worded) | Parseval over `χ` and Goldston–Montgomery transport moments; what fails to cross is the polar/positive structure | `WITHDRAWN`; restated as Theorem 26.17 |
| "the Montgomery–Hooley main term equals `xQ·κ_Q(0)`" | true at leading order only; false at the constant level, by the archimedean `(\log2π+1)xQ` | `CORRECTED` (26.5) |
| `κ(d) = Σ_{q\mid d}1/φ(q)` without the squarefree weight | with `μ²` the closed form is `d/φ(d)`, and it is what `M_Q` produces | `CORRECTED` (Remark 26.11b) |
| "(P149) is the object to create" | it is the Hardy–Littlewood `k`-tuple conjecture with square-root error on average | `RECLASSIFIED` (Problem 26.20) |
| the sharp half of the average-Goldbach equivalence attributed to Bhowmik–Ruzsa | Bhowmik–Ruzsa gives quasi-RH; the equivalence at exponent `3/2` is Granville 2007 + Corrigendum 2008 | `CORRECTED` (Corollary 26.19) |
| "the `2k`-power leg of the Hooley counterexample check is provably negligible" | holds only for `k = 1`, `c > 1/2` (`k < 2c`), by Siegel–Walfisz | `SCOPE REDUCED` (Remark 26.10a) |
| "nothing unconditional is known for `k ≥ 2`" | reworded: no unconditional *upper* bounds; `Ω`-results exist, of Gaussian order, and contradict nothing | `CORRECTED` |

---

## 27. Three method constraints and the classification of coefficient sequences

*Provenance.  The statements and proofs of this section are taken from
`03-research/phase-150-row-d-method-theorems/R150_001_ROUND1.md`
(§§2, 4, 5) as repaired by `R150_003_ROUND2.md` (§§2, 4.1–4.8, 5.1–5.7),
with the labels of record, the downgrades and the withdrawals fixed by
`R150_005_CLOSING_DECISION.md` and by `R150_004_CONFIRMATION.md`
(whose item (b) fixes the label of the classification and whose item D-1 restores
the round-one form of Proposition 27.7), checked against
`R150_002_AUDIT.md`.  Nothing in this section asserts, claims or suggests
a sign; no zero-free region, moment bound or cancellation estimate is proved in
it.*

§18 proves two constraints on any proof of row D's target: T1, field uniformity
(Theorem 18.1), and T2, the insufficiency of the frame's axioms
(Theorem 18.16).  This section adds a third proved constraint, T5, which says
that no `L²`-orthogonality moment bound extracts a single fibre beyond the
trivial bound; it adds the classical **classification of coefficient sequences**
that locates the difficulty exactly; and it records, as a remark and under an
explicitly flagged hypothesis, a fourth constraint T3.  A fifth, T4, survives
only as the two ingredients it was assembled from.

### 27.1 T5: no single-fibre extraction from an `L²`-orthogonality moment

**Definition 27.1 (family moment method).**  The data are a finite index set `ℱ`
(the *family*), unimodular characters `ψ_f : \{1,…,L\} → C`, `|ψ_f(n)| = 1`,
coefficients `b = (b_n)_{n ≤ L}`, the fibre sums `S_f := Σ_{n ≤ L}b_nψ_f(n)`, the
moments `M_{2k} := Σ_{f∈ℱ}|S_f|^{2k}`, and the **extraction**
`|S_{f_0}|^{2k} ≤ M_{2k}` at a distinguished `f_0 ∈ ℱ`.  §26 is the case
`ℱ = 𝓕_Q`, `ψ_{a/q}(n) = e(na/q)`, `f_0 = 0`, `L ≍ N`, `|ℱ| ≍ Q²`; the
archimedean case is `ℱ = [0,T]`, `ψ_t(n) = n^{-it}`; the character case is
`ℱ = \{χ \bmod q\}`.

**Definition 27.2 (Parseval-type bound).**  A moment bound `M_{2k} ≤ 𝔅` is
**Parseval-type** if `𝔅` is a function of `(|ℱ|, L, k, ‖b‖_2, ‖b‖_∞, ‖b‖_1)`
only **and the bound is asserted for every `b` with those norms**.  Equivalently,
it is derived from an `L²`-orthogonality relation on `ℱ` — the large sieve on
Farey points, the Montgomery–Vaughan mean value theorem on `[0,T]`, Heath-Brown's
quadratic large sieve, Ramanujan-sum or character orthogonality — followed by the
trivial evaluation of the resulting convolution norms.  Every bound of the
canonical shape `M_2 ≤ (|ℱ|+L)‖b‖_2²`, and its `2k`-th version obtained by
writing `S_f^{k} = Σ_m(b^{*k})_mψ_f(m)` and applying the same orthogonality to
`b^{*k}`, is Parseval-type.

**Theorem 27.3 (T5, no single-fibre extraction; `METHOD-CONSTRAINT`,
`PROVED`).**  *Let `𝔅` be Parseval-type in the sense of Definition 27.2, valid
for all `b` supported in `\{1,…,L\}` with `‖b‖_∞ ≤ 1`, and suppose the family
contains a point `f_0` with `ψ_{f_0} ≡ 1` — or, more generally, any `f_0`, the
family being closed under the twist `b_n ↦ \overline{ψ_{f_0}(n)}\,b_n`.  Then*

    𝔅^{1/2k} \;≥\; L \qquad\text{for every } k ≥ 1,

*i.e. the extraction yields at best `|S_{f_0}| ≤ L`, the trivial bound, uniformly
in `k`, in `|ℱ|` and in the family type.*

*Proof.*  Take `b_n := \overline{ψ_{f_0}(n)}` for `n ≤ L`.  Then `‖b‖_∞ = 1`,
`‖b‖_2 = \sqrt L`, `‖b‖_1 = L` — the extremal values for the given support and
sup-norm — and `S_{f_0} = Σ_{n≤L}|ψ_{f_0}(n)|² = L`.  Since `𝔅` is valid for this
`b` and `M_{2k} ≥ |S_{f_0}|^{2k} = L^{2k}`, we get `𝔅 ≥ L^{2k}`.  ∎
`METHOD-CONSTRAINT`

**Theorem 27.4 (the quantitative form; `PROVED`).**  For the canonical Parseval
shape, with `‖b‖_∞ ≤ 1` and `\mathrm{supp}\,b ⊆ \{1,…,L\}`,

    M_{2k} = Σ_f\Big|Σ_m(b^{*k})_mψ_f(m)\Big|² ≤ (|ℱ| + kL)\,‖b^{*k}‖_2² ,
    ‖b^{*k}‖_2² ≤ kL·L^{2k−2} = kL^{2k−1} ,

since `|(b^{*k})_m| ≤ L^{k−1}` and `b^{*k}` is supported on at most `kL` points;
hence

    |S_{f_0}| ≤ M_{2k}^{1/2k} ≤ L\big(k(|ℱ|+kL)/L\big)^{1/2k} ,

and, separately,

    L\big(k(|ℱ|+kL)/L\big)^{1/2k} ≥ L\,k^{1/k} ≥ L ,

the first of these two using `|ℱ| + kL ≥ kL`.  So the Parseval bound with the
trivial evaluation of `‖b^{*k}‖_2` never beats the trivial bound, for any `k`,
any `|ℱ|` and any family.  ∎  `PROVED`

**Proposition 27.5 (the one improvable step, and that it cannot be improved for
nonnegative data; `PROVED`).**  Let `b ≥ 0` be supported in `\{1,…,L\}` with
`‖b‖_∞ ≤ 1` and `‖b‖_1 ≍ L`.  Then for every `k ≥ 1` and every `|ℱ|` the
requirement `(|ℱ|+kL)·E_{2k}(b) ≤ L^{k+o(1)}` that a non-trivial extraction
`|S_{f_0}| ≤ L^{1/2+o(1)}` would need, with
`E_{2k}(b) := ‖b^{*k}‖_2²`, is **unsatisfiable**.

*Proof.*  Cauchy–Schwarz on the support of `b^{*k}`, of size `≤ kL`, gives
`E_{2k}(b) ≥ ‖b^{*k}‖_1²/(kL) = ‖b‖_1^{2k}/(kL) ≍ L^{2k−1}/k`; substituting and
using `|ℱ| + kL ≥ kL` gives `(|ℱ|+kL)E_{2k}(b) ≥ L^{2k} > L^{k+o(1)}` for every
`k ≥ 1` and every `|ℱ|`.  ∎  `PROVED`

**Consequence.**  Only **centered** `b` can admit a non-trivial extraction, and
only through square-root cancellation in the `2k`-fold energy `‖b^{*k}‖_2²` — a
statement about the arithmetic of `b`, not about orthogonality.  That statement
is Problem 26.20, and it is `OPEN`.

**Proposition 27.6 (`k = 1`, exactly; `PROVED`).**  With `M_2 ≤ (|ℱ|+L)‖b‖_2²`
and the standing normalisation `‖b‖_∞ ≤ 1`, `\mathrm{supp}\,b ⊆ \{1,…,L\}`, the
extremal `b` is `\overline{ψ_{f_0}}`, for which `‖b‖_2² = L` and `|S_{f_0}| = L`;
the bound reads `L(1+|ℱ|/L)^{1/2} ≥ L` and is never non-trivial.  (The
`δ`-function is extremal for the *different* normalisation `‖b‖_2 = 1`, and the
two cases must not be quoted together.)  The identification with §26 is exact:
`|ℱ| ≍ Q² = N^{2c}`, `L ≍ N`, so `|ℱ| ≥ L ⟺ c ≥ ½` — **the hypothesis has the
required shape exactly where it is useless**, which is Corollary 26.10 stated
without reference to primes.  ∎  `PROVED`

**Proposition 27.7 (`k = 2`, for the additive family; `PROVED` for the identity,
`OPEN` for what it requires).**  For the additive family `ψ_{a/q}(n) = e(na/q)`,
`S_f² = Σ_m(b*b)_mψ_f(m)` with `b*b` the additive convolution
`(b*b)_m = Σ_n b_nb_{m−n}`, so `M_4 ≤ (|ℱ|+2L)‖b*b‖_2²`.  Moreover, for **every
complex** `b`,

    ‖b*b‖_2² \;=\; E(b) := Σ_d\Big|Σ_n b_n\overline{b_{n+d}}\Big|² ,       (27.1)

both sides being `∫_0^1|\widehat b(θ)|^4\,dθ` by Parseval, where
`\widehat b(θ) := Σ_n b_ne(nθ)`: the transform of `b*b` is `\widehat b\,^2` and
that of the correlation sequence `d ↦ Σ_n b_n\overline{b_{n+d}}` is
`|\widehat b|²`.  A non-trivial extraction `|S_{f_0}| ≤ L^{1/2+o(1)}` therefore
requires `E(b) ≤ L^{2+o(1)}/\max(|ℱ|,L)`, i.e. square-root cancellation in the
correlations of `b` — the Hardy–Littlewood statement with power-saving error.
`OPEN`.

*Remark.*  The archimedean family is **not** covered by this proposition: for
`ψ_t(n) = n^{-it}` one has `ψ_t(m)ψ_t(k) = ψ_t(mk)`, so the relevant convolution
is the Dirichlet convolution and the invariant is a multiplicative-energy count.
Theorem 27.3 is uniform over family types; the quantitative corollaries 27.5–27.7
are not, and that is stated rather than assumed.  ∎  `PROVED`

**Falsifier for T5 (`PROVED`).**  `b_n ≡ 1` on `\{1,…,L\}`, `f_0` the trivial
point.  Every hypothesis of every Parseval-type bound holds, every inequality of
Theorem 27.4 is an equality up to constants, and `S_{f_0} = L` exactly.  This is
also why the centering by `M_Q` in §26 is indispensable and yet insufficient: it
removes `b ≡ 1` from the *intended application*, not from the *hypothesis class*
of the large sieve, which is stated for all `b`.

**Remark 27.7a (the exact scope of T5, and what it leaves untouched).**  T5
constrains **one operation**: the extraction of a single fibre from a moment
bound.  It is not a theorem about moment methods.  The standard and productive
use of the same Parseval input is **large-value counting**, which T5 does not
touch: from `M_2 ≤ (|ℱ|+L)‖b‖_2²` one deduces
`\#\{f : |S_f| ≥ V\} ≤ (|ℱ|+L)‖b‖_2²/V²`, and combined with a second moment over
a well-spaced subfamily this gives the classical large-value theorems, which feed
zero-density estimates and their modern successors.  Counting is not extraction.
Similarly untouched: the Montgomery–Vaughan hybrid large sieve, and averaged
statements such as Bombieri–Vinogradov, where the target *is* the average and no
fibre is isolated.  Everything turns on Definition 27.2 — "a function of the
norms only, valid for all `b`": a bound *stated* for all `b` whose *proof* uses
the arithmetic of `b` is not Parseval-type and T5 says nothing about it.  For
Heath-Brown's quadratic large sieve the *statement* is norm-only, so T5 applies
to the statement, and where non-trivial arithmetic is obtained the sieve is
combined with reciprocity, Gauss sums and a restriction of the family — i.e.
Definition 27.2 is left.  The claim that every published moment bound in these
families is Parseval-type is `CERTIFIED`, not proved.

**Corollary 27.8 (`PROVED`).**  No "Deligne extraction over `Z`" that feeds on an
`L²`-orthogonality relation — Farey points, the archimedean line, quadratic
twists, characters mod `q` — reaches a bound better than the trivial one at the
distinguished fibre.  In particular, `H(k,c)` of §26 cannot be obtained by
Parseval-type input, uniformly in `k`.  ∎

### 27.2 Polar at the zeros, or entire at the zeros

This subsection states where the difficulty actually sits.  It is classical, and
it is labelled as such: it sharpens the repository's earlier no-go statements
into a classification; nothing in it is original to this work.

**Definition 27.9.**  Let `a = (a_n)_{n≥1}` be complex with `a_n ≪_ε n^{ε}`, put
`D_a(s) := Σ_n a_nn^{-s}` (absolutely convergent in `\mathrm{Re}\,s > 1`) and
`A(x) := Σ_{n ≤ x}a_n`, and fix `θ ∈ [½,1)`.  Say that `a` is

* **polar-at-zeros** (for `ζ`) if `D_a` continues meromorphically to
  `\mathrm{Re}\,s > 0` and has a pole at `s = ρ` for every non-trivial zero `ρ`
  of `ζ`.  *Examples:* `a_n = Λ(n)`, `D_a = −ζ'/ζ`, with a pole at each `ρ` of
  residue `−m_ρ`; `a_n = μ(n)`, `D_a = 1/ζ`, with a pole at each `ρ` of order
  `m_ρ`;
* **entire-at-zeros** if `D_a` continues to a holomorphic function of finite
  order on `\mathrm{Re}\,s > θ`.  *Example:* `a_n = λ_f(n)` for a holomorphic
  Hecke cusp form, `D_a = L(f, s + \tfrac{k−1}{2})`, entire.

**Theorem 27.10 (the polar class: a partial-sum bound *is* a zero bound;
`CLASSICAL`, `PROVED`).**  Let `a = Λ`, so `D_a = −ζ'/ζ`, `A(x) = ψ(x)`, and let
`θ ∈ [½,1)`.  Then

    ψ(x) − x ≪_ε x^{θ+ε}\ \ \text{for all } x ≥ 2 \text{ and all } ε > 0
      \qquad\Longleftrightarrow\qquad β ≤ θ \text{ for every zero } β+iγ .
                                                                           (27.2)

*Proof.*  (⇐)  Perron with the explicit formula gives
`ψ(x) − x = −Σ_ρ x^{ρ}/ρ − \log2π − ½\log(1−x^{-2})` in the standard truncated
form; if `β ≤ θ` for every `ρ`, the sum is `≪ x^{θ}\log²x`.  (⇒)  Absolute convergence
of the Mellin integral together with uniqueness of analytic continuation: for
`\mathrm{Re}\,s > 1`,

    ∫_1^∞\big(ψ(x) − x\big)x^{-s-1}dx = −\frac1s\frac{ζ'}{ζ}(s) − \frac1{s−1} .

If `ψ(x) − x ≪_ε x^{θ+ε}` the integral converges absolutely and is holomorphic in
`\mathrm{Re}\,s > θ`; by uniqueness of analytic continuation so is the right
member.  But at a zero `ρ` with `\mathrm{Re}\,ρ = β > θ` the right member has a
pole of residue `−m_ρ/ρ ≠ 0`, while `1/(s−1)` is regular there — a
contradiction.  Hence `β ≤ θ`.  ∎  `CLASSICAL` (von Koch–Landau, as attribution
of the **statement**, 1901), `PROVED`.  The step used is *not* Landau's abscissa
theorem, whose one-signedness hypothesis fails for `ψ(x) − x` (Littlewood); in
particular nothing in §27.2 depends on BE8 of §27.4.

**Corollary 27.10a.**  Writing `β_{\max} := \sup\{\mathrm{Re}\,ρ\}`, the
assertion "`ψ(x) − x ≪_ε x^{θ+ε}` for all `x`" is **equivalent** to
`β_{\max} ≤ θ`; the same argument with `D_a = 1/ζ` gives
`M(x) = Σ_{n≤x}μ(n) ≪_ε x^{θ+ε} ⟺ β_{\max} ≤ θ`.  A power-saving bound for the
partial sums of a polar-at-zeros sequence is *exactly* as hard as the
corresponding zero bound: not merely sufficient, but equivalent.  ∎

**Remark 27.10b (the class-level statement).**  Theorem 27.10 and
Corollary 27.10a print the two instances of record, `a = Λ` and `a = μ`.  The
statement at the level of Definition 27.9 — if `a` is polar-at-zeros and
`A(x) ≪_ε x^{θ+ε}`, then `D_a` has no pole in `\mathrm{Re}\,s > θ`, hence
`β ≤ θ` for every zero `ρ` of `ζ` — is the identical argument (absolute
convergence of the Mellin integral, uniqueness of analytic continuation, a pole
at `ρ`), and `θ ∈ [½,1)` is fixed in Definition 27.9 for the (⇐) direction only:
the polar-at-zeros clause itself does not use it.  Only the two instances are
printed; "the classification" in §28.2 and §28.4 means Theorems 27.10–27.11 with
these two instances, together with this class-level observation.  ∎

**Theorem 27.11 (the entire class: a partial-sum bound carries no zero
information; `CLASSICAL`, `PROVED`).**  Let `a` be entire-at-zeros on
`\mathrm{Re}\,s > θ` with `A(x) ≪_ε x^{θ+ε}`, and let
`S ⊂ \{s : \mathrm{Re}\,s > θ\}` be any finite set.  Then there is a sequence `b`
with

    B(x) := Σ_{n ≤ x}b_n ≪_{ε,S} x^{θ+ε},\qquad D_b(s) = D_a(s)·P(s) ,

where `P` is a Dirichlet polynomial whose zero set contains `S`.  Thus for
**any finite** `S ⊂ \{s : \mathrm{Re}\,s > θ\}` there is such a `b` whose
Dirichlet series vanishes on `S`; the hypothesis `A(x) ≪ x^{θ+ε}` therefore
implies no constraint on the zero set.

*Proof.*  For `s_0 ∈ C` put `P_{s_0}(s) := 1 − 2^{s_0}2^{-s}`, a Dirichlet
polynomial with coefficients `c_1 = 1`, `c_2 = −2^{s_0}`, whose zeros are exactly
`s = s_0 + 2πik/\log2`, `k ∈ Z`; in particular `P_{s_0}(s_0) = 0`.  Let
`P := ∏_{s_0∈S}P_{s_0} = Σ_{d ≤ D}c_dd^{-s}`, supported on `d = 2^j`,
`j ≤ |S|`.  Set `b := a * c` (Dirichlet convolution), so `D_b = D_aP` in
`\mathrm{Re}\,s > 1` and by continuation wherever both sides are defined.  Then
`B(x) = Σ_{d≤D}c_dA(x/d) ≪_ε (Σ_{d≤D}|c_d|d^{-θ-ε})x^{θ+ε} ≪_{ε,S}x^{θ+ε}`,
the same power saving with a constant depending only on `S` and `ε`; and the
zeros of `D_b` are those of `D_a` together with those of `P`, which contain `S`.
Since `S` was arbitrary, no constraint on the zero set follows.  ∎  `CLASSICAL`
(the folklore convolution trick), `PROVED`

**Remark 27.11a (why only "add" is available).**  Multiplication by a Dirichlet
polynomial can only **add** zeros to those of `D_a`, never remove one, and each
planted point `s_0` drags in its whole progression `s_0 + 2πik/\log2`, `k ∈ Z`.
Theorem 27.11 is stated and used in exactly that direction: it adds a prescribed
finite set, and asserts nothing about deleting or relocating the zeros of `D_a`.

**Corollary 27.11b.**  `Σ_{n ≤ N}λ_f(n) ≪ N^{1/3}` — Hecke, by the functional
equation and Voronoi summation — is an unconditional power saving at frequency
zero, the smooth regime at its most extreme, and by Theorem 27.11 it implies
nothing about the zeros of `L(f,s)`.  There is no tension with Theorem 27.10:
`λ_f` is entire-at-zeros, `Λ` and `μ` are polar-at-zeros.  ∎

**Reading of record.**  Every unconditional mechanism that gives a power saving
in the smooth regime either acts on an **entire-at-zeros** sequence — Voronoi and
functional-equation summation for cusp forms; spectral and Kuznetsov methods;
the bilinear machinery of Friedlander–Iwaniec and Heath-Brown, whose auxiliary
`L`-functions are entire — or else **consumes zero information it did not
create**: zero-density estimates with zero detection, the short-interval results
they yield, and the recent improvements in the density exponent, all of which
take zero information in and give zero information out, and by Theorem 27.10 could
not do otherwise, a strip-strength partial-sum bound *being* a strip.  The
obstruction in the smooth regime is therefore **not the regime**: it is that the
sequence the sign is about is polar-at-zeros, so that any power-saving bound for
its partial sums is equivalent to the zero bound, and the method must contain the
full strength of the conclusion.  This is a classification of classical facts, and nothing in it is original to this work.

### 27.3 T4, reduced to its two surviving ingredients

**Lemma 27.12 (the untwisted size; `PROVED`).**  For `γ ∈ R` and `N ≥ 1`,

    Σ_{N < n ≤ 2N}n^{-iγ} = \frac{N^{1−iγ}(2^{1−iγ}−1)}{1−iγ} + O(1+|γ|) ,

with an absolute implied constant, and `1 ≤ |2^{1−iγ}−1| ≤ 3`.  Consequently for
every fixed `ε > 0`, every `|γ| ≤ N^{1/2−ε}` and every `N ≥ N_0(ε)`,

    \Big|Σ_{N < n ≤ 2N}n^{-iγ}\Big| ≫_ε \frac{N}{1+|γ|} .                  (27.3)

*Proof.*  Euler–Maclaurin with `g(x) = x^{-iγ}`:
`Σ_{N<n≤2N}g(n) = ∫_N^{2N}g + O(|g(N)|+|g(2N)|+∫_N^{2N}|g'|)`, where `|g| = 1`
and `|g'(x)| = |γ|/x`, so the error is `O(1+|γ|\log2)`; the integral is
`[x^{1−iγ}/(1−iγ)]_N^{2N}`.  Since `|2^{1−iγ}| = 2`, the triangle inequality
gives `1 ≤ |2^{1−iγ}−1| ≤ 3`, so the main term has modulus `≍ N/(1+|γ|)`; the
error is smaller than a fixed multiple of it when `(1+|γ|)² ≪ N`, and
`|γ| ≤ N^{1/2−ε}` makes the ratio `≪ N^{-2ε}`.  ∎  `PROVED`

**Remark 27.12a (what Lemma 27.12 is, and is not).**  The non-cancellation it
exhibits is **the pole of `ζ` at `s = 1`**: `Σ_{n≤N}n^{-iγ} ≈ N^{1−iγ}/(1−iγ)` is
the residue.  It is not a statement about regimes, and by itself it says nothing
about the difficulty of the sign.  What it does say is that any correct upper
bound, produced by any mechanism whose hypothesis class is the one-point class
`a_n ≡ 1` (or a fixed smooth weight) — Kusmin–Landau, van der Corput and exponent
pairs, Vinogradov's mean value theorem and its decoupling descendants — is at
least the modulus (27.3), hence `≥ N^{1−o(1)}` at fixed frequency.  With
`w ∈ C_c^∞`, `\mathrm{supp}\,w ⊂ [1,2]`, `w ≥ 0`, and
`W(s) := ∫_0^∞w(u)u^{s−1}du`, the explicit formula gives
`Σ_nΛ(n)n^{-iγ}w(n/N) = N^{1−iγ}W(1−iγ) − Σ_ρ N^{ρ−iγ}W(ρ−iγ) −
(\text{archimedean})`; at fixed `γ` the main term has modulus `≍ N`, and the sign
is the assertion that the second term is `O(N^{1/2+ε})`.

**Definition 27.13 (coefficient-blind bound scheme).**  A bound scheme is
**coefficient-blind** if its hypotheses on `a` involve only
`\mathrm{supp}\,a, ‖a‖_∞, ‖a‖_2, ‖a‖_1`, so that
`B = B(N,γ,‖a‖_∞,‖a‖_2,‖a‖_1)`, and the bound is asserted for **every** `a` with
those data.

**Theorem 27.14 (the floor for coefficient-blind schemes; `PROVED`).**  For a
coefficient-blind scheme valid for all `a` supported in `(N,2N]` with
`‖a‖_∞ ≤ A`, one has `B(N,γ,A,A\sqrt N,AN) ≥ A·N`.

*Proof.*  `a_n := An^{iγ}\mathbf 1_{(N,2N]}` realises the extremal norms and
`Σ_n a_nn^{-iγ} = A(N+O(1))`.  ∎  `PROVED`

**Remark 27.14a (scope, and the downgrade).**  Theorem 27.14 is a
**normalisation lemma** — a scheme that ignores the arithmetic of `a` cannot beat
the trivial bound — and not an engine.  Its falsifier `a_n = An^{iγ}` lies in the
hypothesis class only of schemes asserted for *all* `a` with given norms; it is
not in the class of any scheme applied to the **centered** object
`Σ_nΛ(n)n^{-iγ}w(n/N) − N^{1−iγ}W(1−iγ)`, and centering is what every real
application does.  Checking the standard mechanisms one by one, **exactly one is
coefficient-blind in the sense of Definition 27.13**: the mean value theorem and
the large sieve, whose hypothesis is norm-only, `(T+O(N))‖a‖_2²` and
`(N+Q²)‖a‖_2²`.  Kusmin–Landau, van der Corput, the Vinogradov mean value
theorem are one-point classes; Vinogradov's minor arcs, the Vaughan,
Heath-Brown and Linnik identities, and the restriction machinery all carry an
arithmetic hypothesis on `a`, and Theorem 27.14 says nothing about them.  For the
one-point classes the stronger and simpler statement is Remark 27.12a.

**Remark 27.15 (T4, and what is left of it).**  The intended fourth constraint
was that no unconditional cancellation mechanism acts at fixed frequency on the
prime-counting sum.  What is **proved** is: (i) Lemma 27.12 with Remark 27.12a,
for the one-point classes and for the mean value theorem in both of its routes;
(ii) Theorem 27.14, for coefficient-blind schemes, i.e. for that one mechanism.
For the arithmetic-hypothesis mechanisms the intended proof is **withdrawn**: the
claim that a completely multiplicative phase factorises every bilinear form is
correct only for uncoupled ranges, and in every Vaughan, Heath-Brown or Linnik
decomposition the ranges are coupled, exploiting the coupling being the entire
method.  It is moreover refuted in the direction that matters, since
Friedlander–Iwaniec (primes represented by `x²+y⁴`) and Heath-Brown
(`x³+2y³`) obtain power-saving bilinear cancellation whose input is the
arithmetic of a quadratic or cubic ring, at no oscillatory frequency at all:
**arithmetic-not-metric bilinear cancellation exists.**  No claim is made here
about what bilinear identities or restriction methods can do at fixed frequency;
both are `OPEN` (O-150.2).  Completeness of any curated list of mechanisms is
**refuted**, not merely unproved.  The content T4 was reaching for is supplied,
correctly and classically, by Theorems 27.10–27.11.

### 27.4 T3, modulo a cited import, and three falsifiers with three conclusions

**Hypothesis (H-DMV).**  *There exists a Beurling system `𝒫` of generalized
primes whose zeta function `ζ_𝒫` satisfies BE1–BE8 below — in particular
meromorphic continuation to a region `\mathrm{Re}\,s > 1 − η(|t|)`, `η > 0`,
with a single simple pole at `s = 1` of positive residue; `ψ_𝒫(x) ≍ x`; and
polynomial growth `ζ_𝒫(σ+it) ≪ |t|^{A}` in that region — and for which, for
every `δ > 0`, `ζ_𝒫` has a zero `β+iγ` with `β > 1 − δ`.*  **Label:
`CITED (secondary source)`** (phase 157). It follows from the reduced statement
**(H-DMV′)**: *there are `θ < 1` and a discrete Beurling system `𝒫` with
`N_𝒫(x) = ρx + O(x^θ)`, `ρ > 0`, whose zeta function has zeros `β_n + iγ_n` with
`β_n → 1`.* Indeed, partial integration gives
`ζ_𝒫(s) = ρs/(s−1) + s∫_1^∞(N_𝒫(x) − ρx)x^{−s−1}dx`, hence meromorphic
continuation to `\mathrm{Re}\,s > θ` with a single simple pole at `s = 1` of
residue `ρ`, and `ζ_𝒫(σ+it) ≪_θ |t|` uniformly on `σ ≥ (1+θ)/2`, `|t| ≥ 2`. So
BE3 and BE7 hold with `η ≡ (1−θ)/2`. BE5 is Landau's prime number theorem for
such systems, BE8 is Landau's theorem on nonnegative Dirichlet integrals, and
BE1, BE2, BE4, BE6 hold for every discrete Beurling system. (H-DMV′) is stated in
the open literature for the system of Diamond–Montgomery–Vorhauer, *Beurling
primes with large oscillation*, Math. Ann. **334** (2006), 1–36. For every
`θ ∈ (½,1)`: `N(x) = ρx + O(x^θ)` (Broucke–Debruyne–Vindas, Adv. Math. **370**
(2020), §1; Broucke, arXiv 2409.10051, §6.2); infinitely many zeros on a curve
`σ = 1 − a/\log(|t|+2)` (ibid. §6.2; Broucke–Debruyne, arXiv 2211.08716, §1);
and, for each fixed `α > θ`, infinitely many zeros with `β ≥ α` (arXiv
2409.10051, §6.2). Independently of these sources, W.-B. Zhang, Math. Ann.
**337** (2007), 671–704 (author's abstract, zbMATH Open Zbl 1121.11061),
constructs a Beurling system with `N(x) = kx + O(x^{1/2}\exp\{c(\log x)^{2/3}\})`
and `\limsup(ψ(x)−x)/(x e^{−2\sqrt{\log x}}) = 2`. By Révész's theorem (arXiv
2207.00665, Theorem 5: under `N(x) = κx + O(x^θ)`, a zero-free half-plane
`σ > 1−δ` with `0 < δ ≤ 1−θ` forces `ψ(x) − x = O(x^{1−(1−ε)δ})`), this system
also satisfies (H-DMV′). **The primary texts have not been read**. The check
against them is open item (41), which no longer blocks at the `CITED` level.

Here BE1–BE8 are: BE1 nonnegative Dirichlet datum; BE2 Euler product with
nonnegative atoms, so that `−Z'/Z = ∫x^{-s}dΛ` with `dΛ ≥ 0`; BE3 meromorphic
continuation to `\mathrm{Re}\,s > 1−η(|t|)` with a single simple pole at `s = 1`
of residue `a > 0`; BE4 reality; BE5 `ψ(x) ≍ x`; BE6 no zeros in
`\mathrm{Re}\,s > 1`; BE7 polynomial growth in the continuation region; BE8
Landau's theorem on the abscissa.

**Remark 27.16 (T3, a meta-theorem modulo a cited import).**  *Assume (H-DMV).  Then
there is no derivation of `(\mathrm{ZFS}_δ)` — "`Z(β+iγ) = 0 ⟹ β ≤ 1−δ`" for a
fixed `δ > 0` — from BE1–BE8 and the objects those axioms name alone; in
particular none for `ξ`, and a fortiori none of RH.*  The proof is one line: a
derivation from BE1–BE8 is valid in every model of BE1–BE8, and (H-DMV) supplies
a model violating `(\mathrm{ZFS}_δ)` for every `δ > 0`.  Hence, modulo that import,
any proof of `(\mathrm{ZFS}_δ)` for `ζ` must invoke a property of `ζ` that is not
a consequence of BE1–BE8: the Euler product with `Λ ≥ 0`, the simple pole at `1`
with its residue, meromorphic continuation with polynomial growth, the Chebyshev
bound and Landau positivity are jointly insufficient.  Unconditionally, only the
soundness half is available — if `(\mathrm{ZFS}_δ)` is derivable from BE1–BE8
then it holds in every model (soundness, immediate) — so everything beyond soundness sits in one place,
now the cited import (H-DMV):
the existence of a bad model.  **Label of the remark: `METHOD-CONSTRAINT`
(meta-theorem), proved modulo the `CITED (secondary source)` import (H-DMV); its
content is a restatement of the Diamond–Montgomery–Vorhauer and Zhang
constructions with the axiom list BE1–BE8 attached. It is recorded as a remark
and not as a theorem of this paper because the primary sources have not been read
(open item (41)).**  It
is also field-uniform, `ζ_K` satisfying BE1–BE8 with the same falsifier, so it is
compatible with T1; and it sharpens T2 on one axis, T2 saying that a proof must
invoke one of A7, A8, A9 and T3 that A8 alone does not suffice.  Nothing here
says or implies that the sign needs more than analytic number theory.

**Remark 27.16a (what is *not* a consequence of BE1–BE8).**  The functional
equation; the integrality of `𝒩 ∩ [N,2N]` on which Vinogradov's mean value
theorem rests; Poisson and Voronoi summation, which need `n ↦ n+h` and a dual
lattice; congruences and `n ↦ n+1`, hence Dirichlet characters and Farey points,
hence the whole additive pencil of §26.  Each is an avatar of the additive
structure of `Z`, and each is **absent from the axiom list** — which is not the
same as impossible in the class: a Beurling system *may* have a functional
equation, the rational primes being the most familiar example and function-field
systems giving Beurling systems that satisfy both the functional equation and
their own Riemann hypothesis.  Each of these non-implications is `PROVED`; the
corresponding statement for the Vinogradov–Korobov region is `CERTIFIED`, no
literature check having been made.

**Proposition 27.17 (three falsifiers, three different conclusions; `PROVED`,
item 3 modulo the `CITED (secondary source)` import (H-DMV)).**

 1. **`Ξ_Q`**, the Epstein zeta function of a principal form with `h(−D) > 1`,
   satisfies the functional equation and equimodularity, and is **not** an Euler
   product — it is a non-trivial complex combination of `h ≥ 2` distinct Euler
   products (Remark 18.12a).  *Conclusion killed:* the Hodge-index conclusion of
   Theorem 18.10, and with it `\mathrm{Re}\,ρ = ½`, since `Ξ_Q` has real zeros in
   `(0,1)` (Theorem 18.5).
 2. **`Ξ_a`**, `0 < a < ½`, is an Euler product and satisfies the functional
   equation, and fails equimodularity, `p − ½ ∈ \{±(½−a),±(½+a)\}`.  *Conclusion
   killed:* `\mathrm{Re}\,ρ = ½`, **infinitely many** of its zeros lying on
   `\mathrm{Re}\,s = ½ ± a` (Theorem 12.4, with Hardy (X16)).  **[phase 158,
   per `R158_003` §6 item 2: printed "its zeros lying on".  The zeros of
   `Ξ_a = ξ(s+a)ξ(s−a)` are the points `ρ ∓ a`; unconditionally only the images
   of the on-line zeros of `ξ` are located.]**
 3. **`ζ_𝒫`**, a system as in (H-DMV), satisfies BE1–BE8; the functional equation
   is not among its axioms and equimodularity is not defined for it.
   *Conclusion killed:* `(\mathrm{ZFS}_δ)` for every `δ > 0`.

**What is not claimed.**  That these assemble into a triangle, that they are the
vertices of one figure, or that they establish the **joint** necessity of the
Euler product, the functional equation and equimodularity for one statement.
They do not: the three items constrain three different conclusions, so no
aggregate necessity follows.  The honest content is three independent negative
results, and they are printed as three.  ∎

### Withdrawn in this section

| claim | why | status |
|---|---|---|
| T3 as an unconditional theorem, with "the DMV system satisfies BE1–BE8" as an import | the inference "`N_𝒫(x) = ax + O(x\exp(−c\sqrt{\log x}))` hence `ζ_𝒫` continues past `\mathrm{Re}\,s = 1`" is false — the Mellin integral diverges for every `σ < 1` — and the source was not read | `WITHDRAWN`; replaced by (H-DMV) and Remark 27.16. The quoted hypothesis misquoted Diamond–Montgomery–Vorhauer: their integer law is `N_𝒫(x) = ρx + O(x^θ)`, `θ ∈ (½,1)`, and with it continuation to `\mathrm{Re}\,s > θ` holds (phase 157). The term `x\exp(−c\sqrt{\log x})` is the size of their **prime** oscillation. The divergence statement in the second column remains correct for the misquoted hypothesis. |
| "no Beurling system has a functional equation, by definition" | false: the rational primes, and function-field systems, are Beurling systems with one | `WITHDRAWN`; restated as non-implication in Remark 27.16a |
| the falsifier triangle: a derivation of the sign must invoke each of the three properties | the three falsifiers kill three *different* conclusions; equimodularity is undefined at the Beurling corner | `WITHDRAWN`; replaced by Proposition 27.17 |
| completeness of the axiom list BE1–BE8 for classical zero-free-region arguments | an inspection claim about a body of proofs, not a theorem; T3 needs only soundness | `DOWNGRADED` to an observation, `CERTIFIED` |
| T4 as a constraint on a complete list of mechanisms | `𝒞`-completeness is **refuted** as a curated list | `WITHDRAWN` |
| "a completely multiplicative phase makes every bilinear form rank one" | true only for uncoupled ranges; the decompositions used in practice are coupled, and Friedlander–Iwaniec and Heath-Brown exhibit power-saving bilinear cancellation with arithmetic input | `WITHDRAWN`, and refuted in that direction |
| "the smooth regime forbids cancellation" | the obstruction is the pole structure at the zeros, not the regime | `WITHDRAWN`; replaced by Theorems 27.10–27.11 |
| Theorem 27.14 as "the engine of T4", applied to six mechanisms | exactly one mechanism is coefficient-blind; for the others the falsifier lies outside the hypothesis class | `WITHDRAWN`; rescoped in Remark 27.14a |
| the range `|γ| ≤ N^{1/2}` in Lemma 27.12 | wrong at the endpoint, where main term and error budget are both `≍ N^{1/2}` | `CORRECTED` to `|γ| ≤ N^{1/2−ε}` |
| "a non-trivial extraction forces `\|ℱ\| ≤ L^{o(1)}`" | exponent error: `(|ℱ|+kL)L^{2k−1}/k ≥ L^{2k} > L^{k+o(1)}` for every `k` and every `|ℱ|` | `WITHDRAWN`; replaced by Proposition 27.5 |
| the identification `‖b*b‖_2² ≠ E(b)` for complex `b`, entered at the second pass | a correction of a non-error: both sides equal `∫_0^1|\widehat b|^4` by Parseval, for every complex `b` | `WITHDRAWN`; the round-one identity (27.1) is restored |
| the archimedean row of the `k = 2` table | the archimedean family has multiplicative convolution; the additive invariant does not apply to it | `WITHDRAWN` from Proposition 27.7 |
| "T5 is the analytic face of the abstract sterility lemma", as a derivation | the common shape is a slogan; an implication would need a functor between the two settings, and none is supplied | `DOWNGRADED` to `ANALOGY` |

---

## 28. The closure of row D in the map

*Provenance.  This section consolidates §§17–27 and the closing records
`R147_005`, `R148_005`, `R149_005`, `R150_005` of the corresponding phase
directories, together with
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-CLOSURE-PLAN.md`
(§§3, 6, 8, 9) for the closing diagnosis, from which only what the phases prove
is carried.  It proves nothing that is not proved above, and it decides nothing about the
truth of any statement about the zeros of `ζ`.*

### 28.1 What is proved across Parts I–IV

To §23.1, which lists items 1–12 for Parts I–III, Part IV adds the following.
Every entry is unconditional except where its own statement says otherwise.

13. **The Galois group ring supplies the `+`, and it is inert at `ζ`.**  On the
    radial carrier every Galois correspondence acts as the identity and `Z[G]`
    acts through its augmentation (Lemma 24.1).  On the packet-graded carrier
    `𝒟_L` the form is well posed, symmetric and real, `ι` is an isometry
    (Theorem 24.3), the degree and the rulings live only in the trivial slot
    (Theorem 24.4), the character table enters the intersection numbers exactly
    (Theorem 24.5), and the cone contains **effective classes with negative
    character coordinates** — the `+` exists (Proposition 24.9).  Its support
    function is `\max_{k<m}s(γ,θ+2πk/m)` (Theorem 24.8).  Against that: **the
    `χ = 1` slot of the cone is exactly `𝓔^∞` and the support function there is
    `s(γ,θ)`, unchanged, for every abelian `L/F`, every tower and every order**
    (Theorem 24.10), so the frame defect theorem stands verbatim
    (Corollary 24.11).  Open item (35) of §23.4 is thereby **answered
    negatively**.
14. **Positivity-type constraints on the full square are vacuous or infinite.**
    Mixed effectivity is the tropical condition `Φ ≥ ⊛P` (Theorem 25.2).  For
    nonnegative factors `⊛P ≥ 0` with no hypothesis at all, so `Φ ≥ ⊛P` implies
    `Φ ≥ 0` (Lemma 25.3(i)); for signed factors an escape at even one point of an
    open set forces the `(T)×(R)` block of the form to be infinite there
    (Lemma 25.3(ii), Lemma 25.4, Corollary 25.8).  Hence the translation shadow
    of the mixed cone is exactly `𝓔 ∪ \{0\}` on the whole domain of definition
    of `B` — Theorems 25.6 and 25.7 carrying `q_w ∈ L¹(R)` at almost every `w`,
    and Corollary 25.8 removing that restriction — at every finite rank and for
    both signs (Theorems 25.6, 25.7, Corollary 25.8), the support constant `s_1` is unchanged and the
    relaxed clause dies at the same witness (Corollary 25.9).  The `(T)×(R)`
    block is the first finite nonnegative Frobenius pairing in row D and is
    **zero-blind** (Theorem 25.11); there is no common radial representation
    (Theorem 25.10).
15. **The additive pencil: the extraction is a Hölder inequality, and the
    arithmetic is entirely in the hypothesis.**  The extraction theorem
    (Theorem 26.4, Corollary 26.5, Theorem 26.6) holds verbatim for an arbitrary
    coefficient sequence (Proposition 26.8), so it carries no arithmetic; the
    continuous hypothesis is *equivalent* to a twisted statement strictly
    stronger in content than RH (Theorem 26.7).  The kill test at `k = 1` is
    exact: the family-moment hypothesis is proved precisely for `c ∈ [1/2,1)`,
    where the extraction is worse than trivial, and is useful precisely for
    `c ∈ (0,1/2)`, where it is open (Theorem 26.9, Corollary 26.10).  The
    coinvariant block is computed a priori, `κ(d) = d/φ(d)` (Theorem 26.11), is
    positive-definite for free (Theorem 26.12, `RESTATEMENT`) and is **zero-blind**
    (Theorem 26.13); it reproduces the variance main term up to an archimedean
    constant (Theorem 26.14).  **Exponents add on the additive square and subtract
    on the multiplicative one** (Theorems 26.15–26.16), which is why Landau is
    decisive in §17 and useless here; moment-level transport between the two
    squares exists, is classical and is sign-free, and what fails to transport is
    the polar/positivity structure (Theorem 26.17).  The family-moment hypothesis
    is, at `k ≥ 2`, a `2k`-fold additive-energy statement (Proposition 26.18),
    implies RH at `k = 2` **together with the off-diagonal bound (26.9a), which
    is a hypothesis of that corollary and not a consequence of `H(2,c)`**
    (Corollary 26.19), and is the Hardy–Littlewood
    `k`-tuple conjecture with square-root error on average (Problem 26.20).
16. **T5 and the classification.**  No Parseval-type moment bound extracts a
    single fibre beyond the trivial bound, uniformly in `k`, in the family size
    and in the family type (Theorem 27.3, Theorem 27.4), and for nonnegative data
    the one improvable step cannot be improved (Proposition 27.5); the same
    statement at `k = 1` and `k = 2` is exact (Propositions 27.6, 27.7, with the
    identity `‖b*b‖_2² = E(b)` for every complex `b`).  Large-value counting is
    untouched (Remark 27.7a).  And the classification: for a **polar-at-zeros**
    sequence a power-saving partial-sum bound is *equivalent* to the corresponding
    zero bound (Theorem 27.10, Corollary 27.10a), while for an
    **entire-at-zeros** sequence it carries no zero information whatever
    (Theorem 27.11, Corollary 27.11b).  Modulo the cited import (H-DMV), the axioms of a
    Beurling system do not yield a zero-free strip (Remark 27.16); three
    falsifiers kill three different conclusions (Proposition 27.17).

Restatements are listed in §23.2 and are extended here by Theorem 26.12
(positivity by construction), Theorem 26.17's framing, and Remark 26.4a (the
extraction as a Hölder inequality).  Refutations are listed in §23.3 and are
extended by the withdrawn tables of §§24–27.

### 28.2 The exact statement of the wall

Everything proved in Parts I–IV converges on one statement.  It uses only T1
(Theorem 18.1), T2 (Theorem 18.16), T5 (Theorem 27.3) and the classification
(Theorems 27.10–27.11), and it is a statement about **admissible derivations**,
not about the location of any zero.

> ┌──────────────────────────────────────────────────────────────────────────┐
>
> **The wall.**  The sign is the assertion
>
>     ψ(x) − x ≪_ε x^{1/2+ε} ,
>
> a **partial-sum bound for a polar-at-zeros sequence**.  As such:
>
> * it is **equivalent** to the corresponding zero bound, not merely sufficient
>   for it, so any method that proves it contains the full strength of the
>   conclusion (Theorem 27.10, Corollary 27.10a);
> * any proof of it is **uniform in the number field**, unless it names a
>   property separating `ξ` from `ξ_K` for some `K`; otherwise it proves GRH for
>   every number field and must be held to that standard (Theorem 18.1);
> * any proof of it **uses the Euler product essentially** — the frame's axioms
>   A1–A6 together with A2⁺ are jointly insufficient, a completed Epstein zeta
>   function satisfying them all and violating the conclusion, so at least one of
>   A7, A8, A9 must be invoked, with the Siegel-zero price attached to the A9
>   escape (Theorem 18.16, Corollary 18.17);
> * it **cannot be obtained by single-fibre extraction from any
>   `L²`-orthogonality moment bound**, uniformly in the moment order, in the
>   family size and in the family type (Theorem 27.3, Theorem 27.4);
> * it **cannot be obtained from partial-sum bounds of entire-at-zeros
>   sequences**, for which any prescribed finite set of points in
>   `\mathrm{Re}\,s > θ` can be added to the zero set at the same power saving
>   (Theorem 27.11).
>
> └──────────────────────────────────────────────────────────────────────────┘

Two readings are worth stating, and neither is a claim about `ζ`.  First, the
wall is *not* a regime phenomenon: unconditional power saving in the smooth
regime is routine, and it is routine exactly on the class of sequences that
carries no zero information (Corollary 27.11b).  Second, the wall is *not* an
artefact of the frame: the frame defect theorem holds on a curve over a finite
field where the Riemann hypothesis is a theorem (Theorem 21.15), and the
enlargements of §§24–26 leave the defect constant unchanged (Corollary 24.11,
Corollary 25.9).

### 28.3 The open items carried

Continuing §23.4, and carrying every item there that is not answered above.

* **(37)** The realizability of the graded cone `𝓒`: an explicit formula on the
  genuinely non-radial sector of `C_{F,S}`, beyond the finite abelian quotients
  (Hecke characters of infinite order); `𝓒` is a model of a projection and the
  equality of Theorem 24.8 is an equality for that model only.  `OPEN`
  (the standing qualifier of §24.3).
* **(38)** The `χ ≠ 1` sectors: a frame theorem for `ζ_F` consumes all zeros of
  `ξ_L = ∏_χΛ(s,χ)`, so the enlarged constants `σ(γ,m)` at `L`-zeros would
  matter to a transfer theorem for `ζ_L`; and there is no `L(s,χ)`-analogue of
  Theorem 19.23, its witness being odd and tied to one direction.  `OPEN`.
* **(39)** The non-abelian case `χ(1) > 1`, where the packet decomposition is
  conditional on Artin holomorphy (import (X25)).  `OPEN`.
* **(40)** A sections functor with `m²`-growth on the graded carrier `𝒟_L` —
  clause (a) of Theorem 12.3 there.  `OPEN`.
* **(41)** *Discharged at the `CITED (secondary source)` level (phase 157); no
  longer blocking.* (H-DMV) follows from (H-DMV′), which the open literature
  states for the Diamond–Montgomery–Vorhauer system, Math. Ann. **334** (2006)
  (Broucke–Debruyne–Vindas, Adv. Math. **370** (2020), §1; Broucke, arXiv
  2409.10051, §6.2; Broucke–Debruyne, arXiv 2211.08716, §1), and, independently,
  for Zhang's system, Math. Ann. **337** (2007) (author's abstract, zbMATH Open
  Zbl 1121.11061, with Révész, arXiv 2207.00665, Theorem 5). *Residual, `OPEN`:*
  confirm against the primary texts.
* **(42)** Whether the sieve-type and spectral mechanisms have a
  coefficient-blind floor at fixed frequency; and, separately, what the bilinear
  identities and the restriction machinery do there.  Both `OPEN`, and the second
  is not to be presumed negative, in view of the arithmetic bilinear cancellation
  of Friedlander–Iwaniec and Heath-Brown (Remark 27.15).
* **(43)** The two gate cells of the classification that are asserted rather than
  derived: the `⇐` half of Theorem 27.10 for a Beurling system and for `Ξ_Q`,
  each of which needs an explicit formula to be more than an assertion.  `OPEN`.
* **(44)** `H(k,c)` for one `k ≥ 2`; presumed beyond present means, and, by
  Corollary 26.19 — taken *together with* its off-diagonal hypothesis (26.9a) —
  at or above RH in difficulty.  `OPEN`, and a claim of it must be presumed
  erroneous until every error term and the `Q`-uniformity are re-derived.
* **O-148.2 = O-149.5, carried as Problem 25.13** — a kernel class on the square
  with a form restricting to `I_∞` on translations, pairing the two fibre classes
  finitely and non-trivially, invariant under the scaling flow, and with an
  unambiguous degree.  This is the single question left by phases 145–149, and it
  is where the "delicate principal values" of the scaling-site programme live
  (`ANALOGY`, not imported).  `OPEN`.
* **(36)** of §23.4, unchanged and still the sharpest open item: a class on the
  square carrying an explicit **phase** datum — the unimodularity of the local
  roots, with its falsifier version `α_± = p^{\pm a}` — rather than a magnitude.
  Not constructed here, and not found in the literature this work has read.
  `OPEN`.
* **(P145′)** of §23.4 item (34): build a mechanism `(𝔐, 𝔈, H⁰, H²)` satisfying
  clauses (1)–(5) of §21.8 with `𝔈 = D^W` excluded.  `OPEN`.
* All remaining items of §23.4 — (24)–(33), together with (34) = (P145′) and
  (36) above — stand as recorded there; (35) is answered negatively by item 13.
* **[phase 156] The phase-155 residuals of the frame defect theorem.**  **R1**
  (whether Theorem 19.25 needs `h⁰` on all of `D^W`) is **closed** by
  Corollary 19.25b: the theorem, its stable form and its localised form hold for
  `h⁰` defined only on `C_c^∞ ⊕ RK` or on `P_c^∞ ⊕ RK = \mathrm{span}\,𝒢_min`,
  given (X19), (E2), (E3d); the bare set `𝒢_min` is excluded for a reason
  (Remark 19.25c(i)).  **R2** (Horn B) is **unchanged and `OPEN`**: Theorem 19.30
  holds on the small domain with `F_R` (the note after its proof), and this
  neither closes nor reopens it.  The citation gap at Lemma 19.20(iv) is recorded
  there.  No label changes.
* **[phase 157] The phase-152 candidate (P152.2)** — a positive energy on the
  Berkovich line `A^{1,an}_Z` reproducing the Weil form, never run before
  phase 157 and not previously recorded in this paper — is **closed as a
  restatement**, with no survivor (§28.3a).  It is not closed as an
  impossibility.  No label changes.
* **[phase 158] MW-5 on the adèle class space `A_Q/Q^×`** is **closed as a
  restatement** (§28.3b, Remark 28.6).  The MW-5 cluster as a whole stays
  `NOT EXCLUDED`, unbuilt.  Its residual (OT-5′, with OT-9 on the Riemann–Roch
  route) is `OPEN` and RH-strength, and passing the object test does not by
  itself meet §28.4 clauses (2) and (3).  No label changes.

### 28.3a [phase 157] The candidate (P152.2): the Berkovich line over `Z`, closed as a restatement

*Provenance.  `03-research/phase-157-row-d-mechanism-search/`:
`R157_005_BERKOVICH_TEST.md` as amended in place, cleared by
`R157_006_AUDIT_BERKOVICH.md` §12, and graded against the one-round
test Lemma P157.S1 **as amended** in `R157_004_AUDIT_SEARCH.md` §3
(A19–A22: criterion (a) is a statement about derivations; (b) is replaced by
(b′); (c) is the schema of Proposition 12.4B with Hardy (X16); (d) is added).
Paper 47's objects are used in its own normalization (its `eq:A`, `eq:W`,
`def:PD`, `thm:Z`); on `P_T` its truncated form `𝔞_T` is the form of this
paper's primitive operator `L_T = P_T𝒜_TP_T` (§4.1), and its `\mathrm{RD}_T`
is `L_T ≥ 0`.  External inputs: (X32).  Nothing here is a statement about the
zeros of `ζ`, nothing is phrased as an impossibility, and no label is raised.
Lemma 3.1(iii) of `R157_005` (`Λ = Σ_pμ∗(−\log|·|_p)`, classical) is **not**
carried: its clearance is conditional on phase 152's Dictionary B.1, which is
not in Paper 44.*

**The candidate.**  Phase 152 (`R152_001` §3, `R152_002` §4.2) proposed a
positive energy on Poineau's line `A^{1,an}_Z`, with a difference kernel along
the archimedean fibre and a meet kernel across the branches of `M(Z)`,
reproducing the Weil form.  Write `π : A^{1,an}_Z → M(Z)` for restriction to
`Z` and `ℓ := −\log|T|`, a continuous function on `A^{1,an}_Z ∖ \{T = 0\}`
whose restriction to the fibre over `|·|_v` is the skeleton coordinate `ℓ_v`
of `G_m^{an}`.

**Lemma 28.1 (the group law is relative to `M(Z)`; `PROVED`, fibre
description `CITED` (X32)(i),(ii)).**  Every point `z` of `A^{2,an}_Z` lies
over a **single** point of `M(Z)`: the two projections `pr_1(z), pr_2(z)`
(restrictions of `|·|_z` to `Z[T_1]`, `Z[T_2]`) have the same restriction to
`Z`.  The addition `m`, induced by `T ↦ T_1+T_2`, is a morphism over `M(Z)`.
The identification `A^{2,an}_Z = A^{1,an}_Z ×_{M(Z)} A^{1,an}_Z` holds **in
the category** of `Z`-analytic spaces (X32)(ii), and **not as sets**: the map
to the set-theoretic fibre product is surjective and not injective (over
`|·|_∞` the fibre is `C²/\mathrm{conj} ≠ (C/\mathrm{conj})²`; over a pair of
Gauss points lie both the bidisc Gauss norm and `P ↦ |P(T,T)|_{Gauss}`).
Consequently `x − y` is a map on `A^{2,an}_Z`, not a function of pairs of
points, and a "difference kernel" on pairs is a symmetrization or a choice —
the sum over the two lifts on `C/\mathrm{conj}`, the Hsia kernel
(X32)(iii) in the non-archimedean fibres, or `k(ℓ(x)−ℓ(y))`.  Every such
choice is supported on `\{π(x) = π(y)\}`, i.e. **compares points over the same
place only**, except the last: the **norm-line kernels** `k(ℓ(x)−ℓ(y))` are
defined on all pairs (because `|T_1T_2|_z = |T|_{pr_1z}|T|_{pr_2z}`), come from
the multiplicative law read through the global function `ℓ` and not from the
additive law, and are Paper 47's dual problem (D) (Lemma 28.2(iii)).
*Proof.*  The restriction of `|·|_z` to `Z ⊂ Z[T_1,T_2]` is one seminorm; `m^*`
is a `Z`-algebra map, so `m` commutes with `π`.  The two counterexamples to
injectivity are the displayed pairs.  ∎  This is why the meet-kernel
conclusion of `R152_001` Prop B.3 on the tree `M(Z)` extends to
`A^{1,an}_Z`: the translation structure is fibrewise, and every cross-place
part of a kernel must come from elsewhere.

**The class `𝔄⁺`.**  Energies `𝓔(f) = ∬ g\,dμ_f\,d\barμ_f`, with
`f ↦ μ_f = (μ_{f,s})_{s∈S}` linear, `S` one point on each branch, `μ_{f,s}` a
signed measure on `π^{−1}(s)`, possibly restricted to a subspace cut out by
global linear constraints (mass or degree zero, the product formula), and a
kernel `g` that is a sum of: a fibrewise kernel on `\{π(x) = π(y)\}`
(difference kernel as in Lemma 28.1, or Arakelov–Green/Hsia); a base kernel
`h(π(x),π(y))`; a kernel `G` on `Σ×Σ`, `Σ` the set of values of global
sections `σ_α`; a **global-function kernel** `H(Φ(x),Φ(y))`,
`Φ = (|P_j|)_{j∈J}` for finitely many `P_j ∈ Z[T]`, the norm-line kernels
included; and a kernel using the scaling flow `x ↦ x^ε` along one branch.  The
last two kinds were missing from the the construction's class and were added on audit
(`R157_006` §2.2).

**Lemma 28.2 (the enlarged branches; `R157_006` Lemmas B.1–B.3).**
 (i) *Flow kernels are branch-local* (`PROVED`): the flow preserves each branch
     of `M(Z)`, so such a kernel is a per-place term (the shared root is one
     base point, covered by `h`).
 (ii) *Finitely many global functions see finitely many primes on the
     skeleton* (`PROVED`, elementary): at the Gauss point `η_{p,ε,r}` of the
     fibre over `|·|_p^ε`, if `p` divides no nonzero coefficient of
     `P_1,…,P_J`, then `Φ(η_{p,ε,r}) = (\max_{i:a_i^{(j)}≠0}r^i)_j` depends
     on neither `p` nor `ε`.  So on skeleton-supported measures such a kernel
     treats all but finitely many primes alike, and any dependence on `p` at
     infinitely many primes enters through the weights of `μ_{f,p}` or through
     atoms at sections.
 (iii) *Norm-line kernels are Paper 47's dual problem (D)* (`RESTATEMENT`; one
     direction `PROVED`): for `G = H(ℓ(x)−ℓ(y))` and `ℓ_*μ_f = f\,du` (the only
     linear choice that does not reintroduce weights by hand), `𝓔 = W_T` on
     `C_c^∞(I_T)` forces `H` to agree with the Weil kernel on `|u| < 2T`,
     arbitrary on `|u| ≥ 2T`; "`𝓔 ⪰ 0` by construction" then means `\hat H ≥ 0`,
     a certificate of value `≥ 0` in the sense of Paper 47 `def:PD` (polar
     term as in `thm:Z`).  `⟸` is weak duality (`prop:weak`), `PROVED`; `⟹` is
     Paper 47's strong duality, `CITED` from Paper 47, with non-attainment
     allowed, hence only in `ε`-form.
 *Proofs:* `R157_006` §2.3.  ∎

**Theorem 28.3 (classification by restatement on `A^{1,an}_Z`; `PROVED` within
`𝔄⁺`; that `𝔄⁺` contains every construction of the literature is `CITED`, five
sources read, one title unread (X32)(iv)).**  Let `𝓔 ∈ 𝔄⁺`, with the
`μ_{f,s}` carrying no atoms on `Σ`, reproduce the Weil form at the window `T`.
Then `𝓔` is one of:
 (1) **the identity** `W = Σ_vQ_v` written on the skeleta (push `f\,du` to the
     `G_m`-skeleton of each fibre by `ℓ_v` and use a multiplicative difference
     kernel) — no sign is inferred, and the positivity question is Paper 47's
     `λ^W_T ≥ 0` itself;
 (2) **a termwise-positive energy minus a scalar load**: local energies
     positive on mass zero ((X32)(iii); tree kernels of negative type),
     `W ≅ 𝓔_P − A_P`, whose positivity on the primitive space is D.195 (3.5),
     which is `\mathrm{RD}_T` (Remark 28.5);
 (3) **a finite-prime form** (Lemma 28.2(ii)), which by Paper 47 `thm:SC` and
     `prop:finsupp` cannot carry the sign for large `T`;
 (4) **a norm-line kernel**, which is Paper 47's (D) (Lemma 28.2(iii)).
If the `μ_{f,s}` are atomic at the sections, the `Σ×Σ` term is FRL's
product-formula kernel `Σ_vn_v\log|α−β|_v = 0` or a kernel on integer pairs
chosen by hand, to which the (a) schema below applies.
*Proof.*  `R157_005` Theorem 4.1 with the amendments of `R157_006` §9 (the
hypothesis "absolutely continuous in the fibres" replaced by "no atoms on
`Σ`"; the two added kinds of kernel handled by Lemma 28.2): Lemma 28.1 puts the
fibrewise term on the fibre diagonal, the base term integrates to a quadratic
form in the fibre masses, and `Σ×Σ` is countable.  ∎

Theorem 28.3 is a **classification by restatement**, not an impossibility
theorem: it says that no realization in `𝔄⁺` supplies a positivity input
independent of the Weil form, and it says nothing about whether `W_T ≥ 0`.
The positivity mechanisms that could be put on top of the four cases are each
excluded as **derivations** by already proved statements:

* **(b′)** the inference "`𝓔_v ⪰ 0` for every `v` (or for `v ∈ S`, `S` finite)
  `⟹ W ⪰ 0`" is excluded by Paper 47 `thm:SC`, `prop:finsupp` (`PROVED`),
  Proposition 28.4 being corroboration and not the exclusion — in case (1) no
  sign is inferred, so (b′) does not fire, and in case (2) it excludes only the
  local inference, the construction itself reducing to `\mathrm{RD}_T`;
* **(a)** with weights attached by hand, `𝓔` factors through the atom list
  `\{(q,k\log q)\}` with its weights (`R157_005` Lemma 5.1), so a derivation of
  "`𝓔 ⪰ 0` by construction" from data common to a class containing `Λ` and
  closed under one-term amplification proves a false `\mathrm{RD}_T` (Paper 47
  `cor:void` and `thm:finmod`(ii), `PROVED`, unconditional); T3 (Remark 27.16)
  is supplementary only, and inapplicable without a bridge
  "`𝓔_𝒫 ⪰ 0 ⟹ (ZFS_δ)`" that does not exist for the DMV system;
* **(c)** a model-uniform structural derivation transfers to `Ξ_a` by the slice
  move of Remark 12.4c and contradicts Proposition 12.4B with Hardy (X16), on
  the four-condition class `P_T^{(P)}`; this excludes derivations and not
  functions (Remark 12.4a′), and a termwise-positive `𝓔` whose identity with
  `W_ζ` is established by a `ζ`-specific argument is case (2), **not
  excluded** — it would prove `\mathrm{RD}_T`, i.e. close D.195 (3.5);
* **(d)** Poineau's and Lemanissier–Poineau's constructions exist over `O_K`,
  and Lemma 28.1, Lemma 28.2 and Theorem 28.3 hold verbatim over `M(O_K)`, one
  branch per place of `K`.  A positivity derivation on `A^{1,an}_{O_K}` would
  therefore be field-uniform, and by T1 read as Remark 18.1a it would prove GRH
  for every `ζ_K`: a standard it must meet, **not** an exclusion.  No
  derivation is proposed, so (d) and the Pass clause (A3 and one of A7, A8, A9
  invoked, T2) are not reached.

**Verdict of record.**  **(P152.2) is `CLOSED`, with no survivor, in the
category `EQUIV` (restatement).**  The coupling the survival clause asked to be
named exists and is canonical: the global function `ℓ` together with the
product formula along integer sections, which puts the prime atoms of every
place on the one norm line.  What it produces there is the Weil form's own
place decomposition, or the Weil form on the norm line — Paper 47's (D).
Neither is a sign.  The bibliographic residual is the one unread title of
(X32)(iv).

**Proposition 28.4 (NG-E1 in proved form: each local form is negative definite
on an infinite-dimensional space of primitive tests; `PROVED`).**
**[phase 157, `R157_005` Lemma 3.3 in the stronger form of `R157_006` §4.]**
In Paper 47's normalization, for real `F ∈ C_c^∞(I_T)`,
`𝔞_T(F) = C_0‖F‖² + ∫_0^∞(‖F‖²−c_F(u))K(u)\,du − Σ_{n∈N_T}v_nc_F(\log n)` with
`c_F(u) = ∫F(t)F(t−u)\,dt`, `v_n = 2Λ(n)/\sqrt n`,
`N_T = \{n ≥ 2 : \log n < 2T\}`.  Grouping the comb by the prime of `n = p^k`,
`𝔞_T = Q_∞ + Σ_{p<e^{2T}}Q_p` with

    Q_p(F) := −Σ_{k≥1,\ k\log p<2T} v_{p^k}\,c_F(k\log p) ,

`Q_∞` collecting the constant and the archimedean term (and, for `W_T` on
`L²(I_T)`, the polar term `2\mathrm{Re}(A(F)\overline{B(F)})`).  Fix a prime
`p` and `T > ½\log p`, put `u_0 := \log p`, choose
`0 < ℓ < \min(u_0,2T−u_0)`, `J := (−T,−T+ℓ)`, and for real `φ ∈ C_c^∞(J)` put
`F_φ := φ + φ(·−u_0)`.  Then

    Q_p(F_φ) = −v_p‖φ‖²   for every φ ∈ C_c^∞(J) ,    v_p = 2\log p/\sqrt p ,

so `Q_p` is **negative definite on the infinite-dimensional subspace
`\{F_φ\}` of `C_c^∞(I_T)`, and on its intersection with `P_T`, which is still
infinite-dimensional** — in both the complete and the primitive form, at every
window `T > ½\log p`, for every prime `p`.
*Proof.*  `ℓ < u_0` makes the translates `J+ku_0`, `k ≥ 0`, pairwise
disjoint, and `J ∪ (J+u_0) ⊂ I_T` because `−T+ℓ+u_0 < T`.  So
`c_{F_φ}(u_0) = ⟨φ+φ(·−u_0),\,φ(·−u_0)+φ(·−2u_0)⟩ = ‖φ‖²` and
`c_{F_φ}(ku_0) = 0` for `k ≥ 2`, the supports being disjoint (the sign
convention is that of Paper 47 `thm:finmod`(ii), where the comb enters as
`−(2c/\sqrt{n_0})c_F(\log n_0)`).  The map `φ ↦ F_φ` is linear and injective,
and `P_T = \{Φ_F(0) = Φ_F(1) = 0\}` has codimension `2`, as in the last
sentence of Paper 47 `lem:cpos`.  ∎  `Q_p` has infinite-dimensional positive
directions too (`φ − φ(·−u_0)`).

This is NG-E1 of the corpus no-go list
(`03-research/phase-136-row-d-map/MAP_1_WALLS_AND_MASTER_DOCS.md`, row NG-E1:
reflection positivity per place, *computed* indefinite at `p = 2,3,5,7`), now
`PROVED` for every `p` in the window setting.  It enters Theorem 28.3 **only as
supporting evidence under (b′), not as an exclusion**: indefinite summands do
not forbid a positive sum (the archimedean form and the comb are both
indefinite, Paper 47 `prop:archneg`, `lem:cpos`).  What it shows is that no
argument can infer the sign from a single `Q_p`; the finite-`S` version is
Paper 47 `thm:SC`, `prop:finsupp`.

**Remark 28.5 (record note: D.195 (3.5) is `\mathrm{RD}_T`; re-audited against
Paper 47's definitions, `RESTATEMENT`, PASS).**  **[phase 157, `R157_006` §7.]**
Phase 114
(`03-research/phase-114-closing-the-four-rows/114_d_195_CONTACT_GNS_POISSON_CP_AND_TATE_JET_DEFECT.md`
§3) writes the Weil form as an adelic energy: `B_P = A_PI − 𝓔_P`, with
`𝓔_P = L_∞ + Σ_{p∈P}\log p\,c_p(I−M_p)` a sum of nonnegative local Dirichlet
forms (the Gamma jump generator at `∞`, a Poisson–Markov defect at each `p`),
`A_P = m_0 + Σ_{p∈P}\log p\,(c_p−1)`, `m_0 = \log π − ψ(¼) = −C_0 > 0`,
`r_p = p^{−1/2}`, `c_p = (1+r_p)/(1−r_p)`, and the boxed inequality
(3.5) `𝓔_P ≥ A_PI` on `\ker M_+ ∩ \ker M_−`, recorded there as equivalent to
row D.  Checked against Paper 47:
 (i) *Sign.*  The operator of `𝔞_T` is `𝓔_P − A_PI`, so D.195's `B_P` is
     **minus** the Weil form and (3.5) says `𝔞_T ≥ 0` on the primitive space;
     `M_±` are the two Tate moments (Paper 47's `A`, `B`; this paper's
     `Φ_F(1)`, `Φ_F(0)`, (1.7)).
 (ii) *Window.*  (3.5) is a window statement only after compression to
     `L²(I_T)`: for `\log p ≥ 2T` the `p`-part `\log p\,(A_p^*A_p − I)
     = \log p\,Σ_{k≠0}p^{−|k|/2}S_{k\log p}` compresses to `0` on `L²(I_T)`
     (D.195 §3: such primes "cancel internally between the two terms of
     (3.1)").  With `P ⊇ \{p < e^{2T}\}`, the compressed (3.5) on `P_T` **is**
     `\mathrm{RD}_T` (`L_T ≥ 0`), and for every `T` it is RH by (1.10).  That the
     compression breaks the Markov/CP structure (D.195 §5) does not affect the
     identity.
 (iii) *Scale, an identity.*  `A_P + C_0 = A_P − m_0 = Σ_{p∈P}\log p\cdot
     2r_p/(1−r_p) = Σ_{p∈P,\,k≥1}v_{p^k}` exactly (`PROVED`): the untruncated
     comb mass over `P`.  With `P = \{p < e^{2T}\}` and
     `V_T := Σ_{n∈N_T}v_n` (the total comb mass, written `\mathsf A_T` in Paper 47
     and `𝒜_T` in `R157_006` §7, not to be confused with this paper's operator
     `𝒜_T`),
     `A_P + C_0 − V_T = Σ_{p<e^{2T},\,p^k≥e^{2T}}v_{p^k} = O(T)` by Chebyshev's
     bounds, so `A_P = V_T + O(T) ∼ 4e^T` (the asymptotic modulo
     Chebyshev/PNT; Paper 47, the text after `cor:SC1`).  The reading of this
     constant as a capacity threshold in the sense of the mass condition of
     `thm:SC` is `HEURISTIC`.
Case (2) of Theorem 28.3 lands exactly here: the sign is not produced by the
energy, it is moved into (3.5), which is the question at the window `T`.

### 28.3b [phase 158] MW-5 and the adèle class space, closed as a restatement

*Provenance.  `03-research/phase-158-row-d-mw5-object/`:
`R158_001_SPEC_SHEET.md` as amended in place, accepted as amended by
`R158_003_AUDIT_SPEC.md`; `R158_002_ADELE_CLASS_FOLIATION.md`
as amended in place, cleared by `R158_004_AUDIT_ADELE.md` §4.  External
inputs: (X33), with (X13), (X14), (X16), (X25a).  Items of `R158_002` that
`R158_004` §4 does not clear are not carried.  The classical content is
attributed where it is used, and no novelty is claimed for it.  Nothing here is
a statement about the zeros of `ζ`, nothing is phrased as an impossibility, and
no label is raised.*

**The MW-5 specification (`R158_001` as amended).**  MW-5 is the corpus name for
a Weil-type object over `Z`: a cohomology `H¹` with a Frobenius flow, a trace
formula, and a positive form compatible with the flow.  `R158_001` derives from
the proved constraints of this paper and of Paper 47 an object test OT-1…OT-12,
organised by one classical fact (Lemma T there; `PROVED`, elementary, content
`CLASSICAL`).  Take as axioms (D1) an `H¹` carrying a flow with generator `Θ`,
and `H⁰, H²` of rank one with `Θ = 0, 1`; (D2) the eigenvalues of `Θ` on `H¹`,
with algebraic multiplicity, are the non-trivial zeros; (D3) a positive-definite
inner product with `⟨φ^tα,φ^tβ⟩ = e^t⟨α,β⟩`.  Then **every** realisation of
(D1)–(D3) forces RH: this is Serre's argument, as formalized in Leichtnam
(X33)(iv) §2 eq. (6) and Comment 6.  Conversely, under RH the spectral
realisation, defined from the zeros, satisfies them (the trivial Hilbert–Pólya
converse).  Hence **OT-5′ is the whole content**: the positive form must be
defined before the spectrum and without it, and its compatibility with the flow
must be **proved**, whatever the position of the zeros.  The residual depends on
the route.  On the conformal route it is OT-5′ on a carrier passing OT-1
(constructed) and OT-2 (a proved Lefschetz formula equal to `ζ`'s explicit
formula, archimedean place included).  On the Riemann–Roch route it is, in
addition, OT-9 (a two-variable carrier, an effective cone strictly larger than
`𝓔`, and (P145′)(4a)–(4c) constructed).  The residual is **`OPEN` and
RH-strength**: an object passing it proves RH, by Lemma T, resp. by
Proposition 21.21.  None of the eighteen published frameworks surveyed in
`R158_001` §4 passes, and the survey is not exhaustive.  **Passing OT-1…OT-12
does not by itself reopen row D.**  The OT list covers clauses (4)–(6) of §28.4,
and clause (1) only in part; clauses (2) (a polar divisor fixed by local data)
and (3) (the zero contribution holomorphic to the left of it) are separate
requirements.

**The object.**  `X = A_Q/Q^×` with the scaling flow (Connes (X33)(i)).  On its
trivial-character sector, Meyer's nuclear `H¹` is, on the Laplace side,
`H¹ = 𝒪/I`.  Here `𝒪` is the space of entire `h` that are Schwartz on every
vertical line, `I` is the image of `Z𝓗_∩`, and `Θ` is multiplication by `s`
((X33)(ii) Thm "Lap_range").  This is CCM's `H¹` ((X33)(iii) Thm 4.16).  Write
`H¹_alg` for the span of the classes `[ξ/(s−ρ)^k]`, `1 ≤ k ≤ m_ρ`.  These
classes are independent, and each generalized eigenspace is **one Jordan block
of length `m_ρ`** (`R158_002` Fact 2.4a, `PROVED` given Meyer's description).
Write `Ξ(t) = ξ(½+it)`, as in Definition–Theorem 11.7.

**Remark 28.6 (MW-5 on the adèle class space; `RESTATEMENT` on `X`, the four
statements `PROVED` or `CITED` as marked, exhaustiveness `ANALYSIS`).**

 (i) *The trace form is Weil's form* (computation `PROVED`; equivalences `CITED`,
     (X33)(iii) and Weil).  Let `g ∈ C_c^∞(R_+^*)` be real and put
     `F(t) := e^{t/2}g(e^t)`, **exactly**, with no further normalisation.  Then
     `ĝ(s) = Φ_F(s)`, and CCM's trace form on the `Ẑ^×`-invariant sector is
     `Tr(ϑ_m(g⋆g^♯)\|H¹) = Σ_ρΦ_F(ρ)Φ_F(1−ρ) = W(F)`: on tests supported in
     `I_T` it is Paper 47's complete form `W_T`.  CCM's degree and codegree are
     `Φ_F(1)` and `Φ_F(0)`, and their transverse self-intersection is
     `2Φ_F(0)Φ_F(1) − W(F) = I_∞(F,F)` by (11.6).  Over `Q` the term `Δ•Δ`
     vanishes (`−\log|a| = \log D = 0`).  So **CCM Prop 7.2, over `Q`, is the
     inequality `W(F) ≥ 0` test by test**: Castelnuovo's form, Hodge index
     against the two fibre classes (Restatement 19bis.13(ii)).  This paper's
     (18.2) is its **weaker** form, Hodge index against the canonical class `K`.
     With `I_∞(F,K) = ½\deg F` and `I_∞(K,K) = ½`, (18.2) reads
     `W(F) ≥ −½(Φ_F(0)−Φ_F(1))²` test by test, which coincides with Prop 7.2 on
     even `F` only.  For all tests, both are RH (Weil; (1.10) with Theorem 20.38 (W1); Corollary 17.11),
     so they are **equivalent only globally**.  The restriction of CCM Cor 6.3
     (all Grössencharaktere) to the trivial sector is Weil's criterion for `ζ`,
     not a statement of CCM.  In adelic dress it is Theorem 20.38 (W1).
 (ii) *Definiteness forces RH and simple zeros* (`PROVED`, elementary; content
     `CLASSICAL`).  Let `H` be a positive-definite hermitian form on `H¹_alg`
     that is `Θ`-compatible, `H(Θx,y) + H(x,Θy) = H(x,y)`, i.e. such that
     `λ^{−½}` times the scaling action is isometric.  Then RH holds and every
     zero is simple.  *Proof.*  On an eigenvector `e_ρ`, compatibility gives
     `(2\mathrm{Re}\,ρ − 1)H(e_ρ,e_ρ) = 0`: this is Serre's argument
     ((X33)(iv) §2 eq. (6)).  At a zero of order `m_ρ ≥ 2`, take `v` with
     `w := (Θ−ρ)v` an eigenvector.  Then `H(w,w) = (1−2\mathrm{Re}\,ρ)H(v,w) = 0`
     with `w ≠ 0`: this is Connes's Jordan-block remark ((X33)(i), after Thm 1),
     made here on Meyer's `H¹`.  ∎  The argument only restricts `H` to the
     invariant subspace `H¹_alg`.  So the conclusion holds on `H¹`, and on
     **any completion into which `H¹_alg` injects `Θ`-equivariantly**, with no
     density hypothesis.  Whether `H¹_alg` is dense in `H¹` is `OPEN`.  CCM's
     hermitian trace form is one such `H`: it is semidefinite ⟺ RH (Cor 6.3), and
     definite on `H¹_alg` ⟺ RH and all zeros simple.
 (iii) *A definite polarization has a multiplier of infinite exponential type*
     (`PROVED`, `R158_002` Proposition H as amended by `R158_004` A21).
     Consider the residue pairings
     `B_Φ(a,b) := Σ_ρ\mathrm{Res}_{s=ρ}Φ(s)a(s)b(1−s)/ξ(s)` on `H¹_alg`, with
     `Φ` entire and real.  If all zeros are simple, every `Θ`-compatible
     bilinear form on `H¹_alg` is a `B_Φ`: alternating for `Φ` even, symmetric
     for `Φ` odd (`R158_002` Fact 4.6a.7 as corrected, `PROVED`).  Suppose the
     hermitian form built from `B_Φ` is definite.  By (ii), RH holds and all
     zeros are simple, and its diagonal values at `ρ = ½+iγ` are `κΦ(ρ)Ξ′(γ)`,
     with a unimodular constant `κ` fixed by the parity of `Φ`.  These values
     have constant sign while `Ξ′` alternates at consecutive zeros.  So
     `t ↦ Φ(½+it)` has a zero of odd order in every gap between consecutive
     positive ordinates, and `n_Φ(T) ≥ N(T) − 1 ≍ (T/2π)\log T` (X14).  By
     Jensen (X13), `Φ(½+i·)` is therefore not of finite exponential type.  In
     particular it is not the Fourier–Laplace transform of a compactly supported
     distribution (Paley–Wiener–Schwartz).  Nor is it any function with `O(T)`
     zeros on the critical line up to height `T`: this excludes finite products
     of Euler polynomials `1 − cp^{−s}`, times `1/Γ(as+b)` with `a, b` real,
     times `e^{\mathrm{polynomial}}`.  Complex shifts of `Γ` are not treated.
     The hypothesis of (iii) is the conclusion of (ii), so (iii) is not a
     statement about `ζ`.  The "multiplier" is not a window test: Paper 47's
     `W_T` is CCM's form, whose multiplier `ξ′` has infinite type, evaluated on
     tests supported in `I_T`.
 (iv) *The canonical residue polarization is indefinite, unconditionally*
     (`PROVED`).  Take `Φ ≡ 1`, so that `B_1` is the Grothendieck–Serre residue
     duality of `𝒪/(ξ)`.  If the associated Hodge–Riemann form were definite,
     then RH and simple zeros would hold, and `Ξ′(γ)` would have one sign at
     every ordinate `γ > 0` (`R158_002` Lemma E, whose necessity half is (ii)).
     But then `Ξ` is real with simple real zeros, of which there are at least
     two positive ones (Hardy (X16)), and `Ξ′` takes opposite signs at
     consecutive ones.  This is a contradiction.  No verified zero is used.  The
     conclusion is unchanged for any `Φ` positive on the critical line.  No
     source proposes `B_1` as a positivity candidate.  The canonical candidate is
     CCM's trace form of (i), whose multiplier `ξ′` is odd.

*Where `X` fails the object test.*  It depends on the realisation.  On Connes'
Hilbert-space realisation, `X` **fails OT-2**.  There the S-local trace formula
is proved ((X33)(i) Thm 4), but the global trace formula is equivalent to RH
(introduction; §VIII Thm 5, proved in positive characteristic and stated by
analogy for number fields).  On the Meyer–CCM nuclear `H¹`, Meyer's character
identity gives the explicit formula unconditionally, and OT-2 passes; this costs
the Hilbert structure.  There `X` **fails OT-5′**, and by (i) OT-5′ on `X` is
exactly Weil's criterion.  The Euler-product line of Meyer's character
computation is the named line at which `Ξ_Q` breaks (OT-4).  The nuclear
quotient built for `Ξ_Q` by lattice Poisson summation carries (ii)–(iv)
verbatim, so none of them can carry a sign (T2, Theorem 18.16).

*The `S₃`-field falsifier (`PROVED` on the zeta side, classical; the transfer
`ANALYSIS`).*  Let `K/Q` be Galois with group `S₃`.  Then
`ζ_K = ζ·L(s,\mathrm{sgn})·L(s,ρ)²` with `ρ` two-dimensional (X25a).  Here
`L(s,ρ)` is a Hecke `L`-function of a cubic character of `Q(\sqrt{−3})`, entire,
with infinitely many zeros, so `ζ_K` has infinitely many zeros of order `≥ 2`.
**Given the `K`-analogue of Meyer's Laplace-range theorem** (cyclicity of the
trivial sector of `X_K`, not verified in a source: `ANALYSIS`), the generalized
eigenspaces there are single Jordan blocks.  Then, by (ii), no definite
`Θ`-compatible form exists on `X_K`, **whatever RH says**.  Read through T1
(Remark 18.1a), a field-uniform route that derives RH for `ζ` from such
unitarity on the adelic `H¹` would prove something false.  This remark is
carried only with its `ANALYSIS` flag.

**Verdict of record.**  The adèle-class instantiation of MW-5 is **closed as a
restatement** (`EQUIV`).  On `X`, every positivity structure on the list of
`R158_002` §4.9, as enlarged by `R158_004` A23, falls into one of four kinds.  It
is a restatement of RH: CCM's trace form, Rosati, Prop 7.2, the log-derivative
pairing `B_{(s−½)ξ′}`, or the relative trace of the type II_∞ factor.  It is a
restatement of RH with simple zeros: any definite compatible form, or Deninger
unitarity.  It is a proved compression, or a zero-blind positivity, that does
not transfer.  Or it is false, like `B_1`.  That the list is exhaustive is
`ANALYSIS`.  The MW-5 cluster as a whole stays **NOT EXCLUDED, unbuilt**.  No
label changes, and no sign is claimed, asserted or suggested.

### 28.4 The decision

**Row D is closed in the map: no label, no sign.**  Rows A, B and C are
`WEIL-STRENGTH-COMPLETE` on the declared carrier (Papers 43–45).  Row D receives
**no** label, and this paper claims, asserts and suggests **no** sign.  What it
delivers is the map with its walls: T1 (Theorem 18.1), T2 (Theorem 18.16), the
frame defect theorem (Theorem 19.25, and Theorem 21.15 on the curve), T5
(Theorem 27.3), and the classification (Theorems 27.10–27.11) as the exact
statement of §28.2.

The decision is made on the following record, and on nothing else.  Five
independent mechanisms close five independent enlargements of the frame: there is
no ring of correspondences on `Spec Z` (Theorem 22.17); where a ring exists it is
invisible on the radial carrier (Lemma 24.1); where a carrier sees it, it acts
away from the zeros of `ζ` (Theorem 24.10); positivity-type constraints on the
full square are vacuous or infinite (Theorems 25.6, 25.7); and on the additive
square the coinvariant block is computable a priori but zero-blind, while
positivity and the polar structure live on two different squares between which
only sign-free moment identities transport (Theorems 26.13, 26.17).  To these,
§27 adds that the one extraction mechanism the Deligne route needs cannot
work over `Z` in any family (Theorem 27.3), and that the difficulty is located
exactly, and classically, by the polar/entire classification.

**What would reopen row D.**  A single object, and nothing less: a construction
`𝒪` on the adelic square satisfying all six of

 (1) it is a **square**, hence positive after every twist, in the Rankin sense;
 (2) its **polar divisor is determined by local data** — the singular series or
   the local root numbers promoted from a density to a residue;
 (3) the contribution of the zeros is **holomorphic to the left of that a priori
   pole**;
 (4) it **reads phase**, hence fails for `Ξ_a`;
 (5) it uses both the additive and the multiplicative structure, hence fails for
   `Ξ_Q` and for every Beurling system;
 (6) it is **uniform in the number field** (T1).

Clauses (1), (2) and (3) are exactly what a single object supplies over a finite
field and what §26 shows is split in two over `Z`; clauses (4), (5), (6) are the
three falsifier gates and T1.  **No such object exists here, and none is
proposed.**  Two further routes are recorded as available and as measuring rather
than moving the wall: the open item (36) phase datum, and the computer-assisted
extension of the certified positivity range of the repository's Weil form beyond
its present endpoint, whose value is to measure the decay of the margin, not to
decide anything.

### 28.5 Reproduction (Part IV)

Phases 147–150 are pen-and-paper phases: their statements are proved in the text
and none of them rests on a computation.  The two numerical constants quoted in
Part IV — `s_1 = 0.99846016…` at `ρ_1` (Corollary 25.9) and the lower bounds for
`σ(γ,m)` (Remark 24.12) — are reproduced by the Part III scripts already listed
in §23.6:

```text
cd 03-research/phase-143-row-d-trace-positive-cone/scripts
python3 certify_s_star.py [--fast]            # s_* = 0.99845824…0.99846016

cd 03-research/phase-142-row-d-the-clause/scripts
python3 certify_sF.py                         # s_1, the degree threshold d_0
```

Numerics illustrate and falsify; they prove nothing, and no number anywhere in
this paper is evidence for any sign.

---

**Part IV claims no sign, asserts no sign, and suggests no sign.**  It adds to
the map three closed enlargements (the Galois ring, the full square with a
positivity constraint, the additive pencil), one further proved method constraint
(Theorem 27.3), one constraint modulo a cited import, held back as a remark until that
import is checked against the primary texts (Remark 27.16), and one classical classification
(Theorems 27.10–27.11) that states the wall exactly.  Phase 157 adds the
closure of the phase-152 candidate (P152.2) on the Berkovich line as a
restatement, not an impossibility (§28.3a).  Phase 158 adds the closure of
the adèle-class instantiation of MW-5 as a restatement, with the MW-5
specification and its residual, which is `OPEN` and RH-strength (§28.3b).
**Row D is closed in the map, with no label and no sign.**
