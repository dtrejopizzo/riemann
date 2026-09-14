# Paper 46 — Row D: the sign

**David Alejandro Trejo Pizzo, with Claude (Opus 5).**  2026-09-12.

**Status: `SKELETON AND FIRST THEOREMS`.  No label is claimed for row D, and
none is expected from this campaign.  No sign is claimed, asserted or
suggested anywhere in this paper.**

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
hostile audit's §5, both upholding the builder's own round-1 press point `P1`.
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
   **[REBUILT, round 2, `LF2` and the hostile audit §2.  Round 1 called this
   "what the equivalence gains over the textbook statement".  That claim is
   **withdrawn**, and it is withdrawn on evidence: **no proof in this paper
   uses the identification of the group with the carrier's modulus group, or
   of the flow with `Frob_∞`, for anything but naming.**  Deleting the
   identification from §3 changes no proof in §3 and no proof anywhere else in
   the paper; the auditor searched for such a use independently and found
   none, and so did the builder.  The identification is a **typing of the
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
sequences fall and rise.  **[Round 2: the hostile auditor re-ran the first
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
   because the builder's first draft asserted that convergence and it is
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
in `RH1_RH9_AUDIT` and implemented in `p124_lab.model_dh`; (iii) is (i)+(ii)
against (1.5)–(1.7).  ∎  `PROVED`.  `RH1_RH9_AUDIT` retires DH as a
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
    route** — on the lead's and the auditors' concurring recommendation: after
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
*repair*, found by the hostile auditor of round 2 (`R134_005` (F1)), and would
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

*Running count, for the record:* **four** of the builder's own statements have
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

> **Lead closing decision (R135.007, 2026-09-13).** Phase 135 is closed. Part II
> (§§11–16) is accepted as a **reduction with no sign**: the Weil completion,
> the canonical class `K` (`Φ_K = ξ`), the radical, the affine duality `σ_K`
> and the Hodge-index transfer theorem (Thm 12.3, conditional on `h⁰` with
> (a),(b′),(c)) are `PROVED`; the falsifier theorem (Thm 12.4) shows the same
> axioms are inconsistent for `Ξ_a`; two natural `h⁰` constructions are
> examined and neither yields (c). Nothing about the sign is claimed. Next
> campaign: R135_007 §4.

> **Lead closing decision (R134.007, 2026-09-12).** The opening campaign is
> closed after three builder rounds and two hostile audits. No label; no sign.
> Paper 46 stands as row D's opening state with: Lemma 3.1, Thm 3.6, Thm 3.7
> (`RESTATEMENT`), the swap law, Thm 5.8 (D.3 retired), the negatives of §6 with
> requirement (R5) — no duality carrying the primitive sector off itself is
> constructed in rows A–C — and the falsifier suite. Withdrawn: Prop 3.6a(iii)
> (false under RH; its retention would have been a statement about the zeros).
> Full text: [R134.007](../../03-research/phase-134-row-d-opening/R134_007_LEAD_CLOSING_DECISION.md).

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

**[ROUND 2, phase 135 (`R135_004`).  Part II has been through one hostile
audit (`R135_002`, findings M1–M17) and one lead audit (`R135_003`, findings
LF1–LF7), and every mandatory repair of the lead's §4 ruling is carried out in
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

**[Record note, phase 142 (2026-09-13), `R142_001` Theorem D.31.12, hostile-confirmed
`R142_002`, lead-verified numerically. The hypothesis of Theorem 12.3 is UNSATISFIABLE for
`ξ`, for every `χ`, given (X19) (the first zero `ρ₁ = ½+iγ₁` is simple and on the line,
Rosser–Yohe–Schoenfeld / Platt–Trudgian): for every nonnegative `E'` and every real `θ`,
`|Re(e^{iθ}Φ_{E'}(ρ₁))| ≤ ½·s₁·deg E'` with `s₁ = sup_u |sin(γ₁u)|/cosh(u/2) = 0.99846… < 1`
(Lemma D.31.4), while (b′) + Theorem 11.13 + (c) + the Serre symmetry `R(K−E) = R(E)` force
`h⁰(E) ≥ ½I_∞(E,E) − ¼deg E + χ` for `deg E > 1`, and the class
`E = 53.11911·e^{−u²/18}sin(γ₁u) + 400K` has `R(E) = 10 > 0`, `deg E = 400`, and
`|Im Φ_E(ρ₁)| = 199.7248 > 199.6920 = ½s₁·400`, so `E` is not equivalent mod `𝓝_∞` to any
nonnegative class. The theorem keeps its label (its proof is correct); it can no longer be
used as a route to RH in this normalization. The same holds for every admissible `Z` with a
simple isolated on-line zero (`ξ_K` verbatim). Geometric diagnosis (`R142_002`, `R142_001`
§D.32): the frame keeps the intersection theory of `C×C` and discards its linear systems — in
geometry `D² > 0, D·H > 0 ⟹ D` big, whereas here effectivity is pointwise nonnegativity of a
single radial density and its trace cone is a thin moment cone. Repair horns (phase 143): weaken
(c) by a defect vanishing at the degrees Theorem 12.3 actually uses, or enlarge the effective
cone (nonnegative Frobenius traces).]**

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

Every finding of the hostile audit `R135_002` and of the lead audit `R135_003`
that the lead ruled mandatory, with the edit that answers it.

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

Every finding of the round-2 hostile confirmation `R135_005` (N1–N8), with the
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
       is a theorem.
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
* **Unchanged:** items 1, 2, 4–15 of §9.1, and the label of §10.

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

## 15. External inputs added by Part II

| tag | import | clause it serves | used at |
|---|---|---|---|
| **(X12)** | **Riemann's integral representation in Pólya's normalization**: `Ξ(τ) = 2∫_0^∞K(t)\cos(τt)dt` with `K` of (11.7); `K` real, **even**, and `K(t) > 0` for all real `t`.  Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath–Brown), §10.1, eq. (10.1.4) and the following two displays; G. Pólya, Acta Math. **48** (1926), 305–317 | `Φ_K = ξ`; evenness and positivity of the canonical class | Thm 11.7(i) |
| **(X13)** | **Jensen's formula / the zero-counting bound for entire functions of exponential type**: `n_f(r) = O(r)` for `f ≢ 0` of exponential type | the zero-counting half of Theorem 11.12 | Thm 11.12 |
| **(X14)** | **Riemann–von Mangoldt asymptotic** `N(T) = \frac{T}{2π}\log\frac{T}{2π} − \frac{T}{2π} + O(\log T)` (the asymptotic form of (E3d)) | the other half of Theorem 11.12: `ξ` has `\sim(r/π)\log r` zeros in `\|s−½\|≤r` | Thm 11.12 |
| **(X15)** | **Chebyshev's bound in Rosser–Schoenfeld's explicit form** `ψ_{Ch}(x) < 1.03883\,x` for all `x > 0`: Illinois J. Math. **6** (1962), 64–94, Theorem 12 | **[phase 135 round 2: no longer used by any proof.]**  Round 1 used it for the constant `C_F`; Theorem 11.14 is now proved on the spectral side and needs no Chebyshev bound.  Retained only in Remark 11.14a′, which nothing uses | Rem 11.14a′ |
| **(X18)** | **A positive proportion of the zeros of `ζ` are simple**: `N_s(T) ≥ (\tfrac25+o(1))N(T)`.  J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta-function are on the critical line*, J. reine angew. Math. **399** (1989), 1–26; N. Levinson, *More than one third of the zeros of Riemann's zeta-function are on `σ = ½`*, Advances in Math. **13** (1974), 383–436, would also serve | **[NEW, phase 135 round 2, finding M3 of `R135_002`.]**  The count of **distinct** zeros of `ξ` in `\|s−½\| ≤ r`, which is what Theorem 11.10(c) supplies zeros of `Φ_N` at.  (X14) counts with multiplicity and does **not** give this | Thm 11.12 |
| **(X16)** | **Hardy's theorem** (1914): `ζ` has infinitely many zeros on `\mathrm{Re}\,s = ½` | that `Ξ_a` has zeros off the critical line, **unconditionally** | Thm 12.4 |
| **(X17)** | **Connes–Consani**, *Riemann–Roch for `\overline{\mathrm{Spec}\,\mathbb Z}`*, arXiv:2205.01391v2: `\dim_{\mathbb S}\|H\mathbb Z\|_n = \lceil\log(2n+1)/\log3\rceil` (minimal generating set with coefficients in `\{-1,0,1\}`); `\dim_{\mathbb S}H⁰(D) = \lceil(\deg D+\log2)/\log3\rceil − \mathbf 1_L`; Serre duality `H⁰(K−D) ≅ \underline{\mathrm{Hom}}(H¹(D),U(1)_{1/4})` with `K = −2\{2\}`, `\deg K = −2\log2` | the `\log`-scale type of an integral dimension (Definition 13.4) and the first row of Finding 13.8 | §13.2, Finding 13.8 |

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

