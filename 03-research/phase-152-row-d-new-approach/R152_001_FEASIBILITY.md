# R152.001 — Feasibility, phase 152 round 0: two never-analyzed non-positivity mechanisms

* FATAL rule in force: nothing
below is a new zero-free region, a new moment bound or a new cancellation estimate. **No sign is claimed; row D
keeps no label.** Every external statement is marked `IMPORTED` (read and known precisely here) or
`CERTIFIED` (believed on memory of the literature, not re-read here); where the exact form of a theorem is
uncertain this is said in the line itself. No reference is invented.*

---

## §0 Verdicts

| mechanism | verdict |
|---|---|
| **A** — resonances of the modular surface (`= ρ/2`), Dolgopyat / fractal-uncertainty gap | **DEAD for the sign.** Kill criterion A fires on all four clauses: (Q1) yes, (Q2) none known, (Q3) circular/empty, (Q4) structural obstruction (Prop. A.4: the branch series of the Gauss transfer operator has abscissa of convergence exactly `σ = ½`, so there is no operator to which Dolgopyat's method could be applied on `Re s ∈ (¼,½)`). Recorded with the four reasons; one dictionary entry retained (§7). |
| **B** — Poineau's `M(Z)`, Frobenius lattice as integer points | **DEAD as a route to the sign.** Kill criterion B fires: (Q5) refuted (Prop. B.3: a tree-potential pairing is a function of the **meet** of the locations, the Weil kernel a function of their **difference**; and the tree energy of the corpus's atomic measure is an `f`-independent constant, Prop. B.2), (Q6) no Frobenius and no published square pairing known. Survives only as a **dictionary** (RESTATEMENT), one remark for Paper 44. |

Neither (P152.A) nor (P152.B) is formulated. Both deaths are documented with the exact obstruction below.

---

## §1 Corpus check

Command template, run from the repository root:

```
grep -rli --include=*.md "<name>" 03-research 04-papers 05-meta-and-planning NO-GO-LIST.md
```

| name | files | reading |
|---|---|---|
| Dyatlov | 3 | only `R152_000`, `ABCD-CLOSURE-PLAN/PLAN.md`, `ROW-D-CLOSURE-PLAN.md` — i.e. **this phase's own planning only**. NEW. |
| Bourgain | 9+ | all hits are Bourgain–Gamburd / Bourgain's sum-product or large-sieve work in phases 136, 149–150, 60–61; **no** Bourgain–Dyatlov. NEW. |
| Dolgopyat | 4 | `R151_005`, `R152_000`, the two plan files. NEW. |
| Naud | many | every hit is the Spanish word *nada* / OCR noise inside audit matrices (phase 107) plus this phase's files; **no** F. Naud. NEW. |
| Baladi | 2 | `R152_000`, `ROW-D-CLOSURE-PLAN`. NEW. |
| Vallée | 4 non-"Vallée Poussin" files | phase-24-lower-bounds-bj setup, phase-29-zeta-spectral-triples doc 39, `phase-151/README`, `R152_000`; none is Baladi–Vallée dynamical analysis. NEW. |
| Mayer | 2 | phase-29-zeta-spectral-triples doc 52 (motivic context, incidental), `R152_000`. NEW as transfer operator. |
| Lewis (–Zagier) | 3 | this phase's planning only. NEW. |
| Maass | 8+ | phase 16 (docs 01–06), phase 102 audit fragments. **Not new**: phase 16 is the corpus's Route A. |
| "scattering determinant" | 6 | phase 16 doc 01; phase 106 `SELFADJOINT_EULER_DETERMINANT_NO_GO`; phase 120 `P3_G125_T2_AHK`; phase 71. **Not new.** |
| Eisenstein | 8+ | phase 16, phase 111, phase 120. **Not new.** |
| resonan* | 8+ | phase 16 docs 02 and **05** (`resonance-pairing-definite-THEOREM`), phases 21, 118, 136. **Not new.** |
| Poineau | 3 | `R151_005` + the two plan files. NEW. |
| Berkovich | 6 | `AUDIT_A_CATEGORY_CHANGES.md` ("No Berkovich space over `Spec Z` … is built anywhere"), `AUDIT_CONSOLIDATED`, phase-136 map, `R151_005`, plans. **Named as unbuilt, never built.** |
| Baker–Rumely / Thuillier / Chambert-Loir | 1 each | `R152_000` only. NEW. |
| Furstenberg | 3 | phase-49 doc 154 (taxonomy of crossings) + plans. Essentially new. |
| Rudolph / Lindenstrauss | 2 each | planning files only. NEW. |
| Bombieri–Stepanov | 8+ | phase-38 doc 116 (`auditoria-stepanov`), phase-33 doc 74, phases 141–142, phase-44 doc 133. **Not new**; see §4.3. |
| "fractal uncertainty" / "incertidumbre fractal" | 2 | planning files only. NEW. |

**Corpus finding that decides the framing of mechanism A.** Phase 16 already contains Route A in full: doc 01
computes `φ(s) = ξ(2s−1)/ξ(2s)` and verifies numerically that `|φ|` blows up at `s = ¼ + iγ/2`; doc 05 proves
that the **resonance pairing on the modular surface is negative definite for every configuration of zeros**,
on-line or off-line, hence structurally sign-blind. Mechanism A is therefore *not* a new object in the corpus;
what is new is only the **dynamical** (Dolgopyat/FUP) way of asking for a gap. §2 treats exactly that.

---

## §2 Mechanism A

### A.0 Facts

**(A.0.1) Scattering determinant.** `IMPORTED`. For `Γ = PSL₂(Z)`, `E(z,s)` has constant term
`y^s + φ(s)y^{1−s}` with `φ(s) = ξ(2s−1)/ξ(2s) = √π Γ(s−½)ζ(2s−1) / (Γ(s)ζ(2s))` (the two displays agree by
`ξ(s) = π^{−s/2}Γ(s/2)ζ(s)` up to the elementary factor; the second is the form in `R152_000` §A). The
resonances in the Eisenstein sector are the poles of `φ`, i.e. `s = ρ/2` for the nontrivial zeros `ρ`, together
with `s = 1` (from the pole of `ζ(2s−1)`) and trivial points on the real axis. Hence

> **RH ⟺ every Eisenstein resonance of the modular surface lies on `Re s = ¼`,**

the symmetry line of `s ↦ ½ − s̄`; `φ(s)φ(1−s) = 1` and `|φ(½+it)| = 1` are the unitarity relations. Corpus:
phase 16 doc 01 (`RESTATEMENT`; this is the automorphic clothing of RH, not a new statement).

**(A.0.2) Maass–Selberg gives exactly the trivial region.** `IMPORTED`, and proved here.

> **Proposition A.1.** The Maass–Selberg relation, by itself, yields exactly: `φ` has no poles in
> `Re s > ½` off the real axis. This is the region `Re w > 1` for `ζ(w)`, i.e. the Euler-product region.

*Proof.* Maass–Selberg for the truncated Eisenstein series gives, for `s` not real and `Re s > ½`,
`‖E^T(·,s)‖² = (T^{2σ−1} − |φ(s)|²T^{1−2σ})/(2σ−1) + (φ(s)T^{2it} − φ(s)‾T^{−2it})/(2it)`, `s = σ+it`. The
left side is `≥ 0` for every `T`. If `φ` had a pole at such an `s₀`, `E^T(·,s₀)` would not be defined; the
standard consequence is rather the converse statement: a pole of `φ` at `s₀` with `Re s₀ > ½` forces a residual
`L²` eigenfunction with eigenvalue `s₀(1−s₀) ∉ [¼,∞)` i.e. non-real, contradicting self-adjointness of the
Laplacian. Hence poles in `Re s > ½` are real. Translating by `s = ρ/2`: `ζ(w) ≠ 0` for `Re w > 1`. ∎

The content used is **self-adjointness** = the unitarity `|φ(½+it)| = 1`, which is the automorphic form of
"`|ζ| ≠ 0` where the Euler product converges". It is the corpus's invariant conclusion 2 (MW-2) verbatim: the
region obtained is exactly the region of absolute convergence, and nothing more. Any statement about
`Re s ∈ (¼,½)` is outside the reach of Maass–Selberg for the same reason the Euler product stops at `Re w = 1`.

**(A.0.3) Bourgain–Dyatlov.** `IMPORTED` in statement, `CERTIFIED` in proof detail. J. Bourgain, S. Dyatlov,
*Spectral gaps without the pressure condition*, Ann. of Math. **187** (2018): for every **convex cocompact**
hyperbolic surface `M = Γ\H` (infinite volume, no cusps, limit set of dimension `δ ∈ (0,1)`) there is `β > 0`,
depending on `δ` and the Ahlfors–David regularity constants, such that the resolvent continues with only
finitely many resonances in `Re s > ½ − β`. Proof via the **fractal uncertainty principle**: a function cannot
be concentrated near an `Ahlfors–David`-regular set of dimension `δ < 1` and have Fourier transform
concentrated near another such set. No positivity is used — this is the property that made the mechanism worth
one round.

**(A.0.4) Dolgopyat / Naud / Baladi–Vallée.** `CERTIFIED`. D. Dolgopyat (1998, *Ann. of Math.*, on decay of
correlations for Anosov flows) introduced oscillatory cancellation in iterates of a twisted transfer operator
under a **uniform non-integrability** (UNI) hypothesis; F. Naud (2005) obtained resonance-free strips
`Re s > δ − ε` for convex cocompact Schottky groups; V. Baladi, B. Vallée (2005) proved a Dolgopyat-type
uniform bound for the Gauss-map transfer operator `L_s` for `Re s` near `1`, the basis of dynamical analysis of
continued-fraction algorithms. Mayer's theorem: `Z_Selberg(s) = det(1 − L_s)det(1 + L_s)` for the
Gauss–Kuzmin–Wirsing operator acting on holomorphic functions on a disc, `L_s` nuclear of order 0 there
(`CERTIFIED`; the exact disc and the exact placement of the Eisenstein zeros `s = ρ/2` as zeros of one of the
two factors I have **not** re-read and do not assert precisely).

### A.1 (Q1) Does FUP degenerate at `δ = 1`, and is the degeneration exactly the `~log T` resonance density?

**Answer: yes, and necessarily so; the density is the quantitative form of the degeneration.**

> **Proposition A.2.** For `Γ = PSL₂(Z)` the conclusion of (A.0.3) is false for every `β > ¼`; consequently no
> FUP-type argument can hold with those parameters. Quantitatively, the number of Eisenstein resonances with
> `|Im s| ≤ T` is `N(2T) ∼ (T/π)·log(T/π) − T/π`, i.e. `≍ log T` per unit window on `Re s = ¼`.

*Proof.* The resonances `ρ/2` have `Re = β_ρ/2 ∈ (0,½)`. Riemann–von Mangoldt counts the `ρ` with `0<γ≤2T` as
`(T/π)log(T/π) − T/π + O(log T)`, all with `Re(ρ/2) = ¼` at least for `γ ≤ 3·10¹²` (Platt–Trudgian, `IMPORTED`
via phase 37 doc 111 §3.2 (c)) and in any case infinitely many with `Re(ρ/2) ≥ ¼ − o(1)` since a positive
proportion of zeros lie on the line (Levinson/Conrey; `CERTIFIED`). So `{Re s > ½ − β}` with `β > ¼` contains
infinitely many resonances. ∎

Three independent hypotheses of (A.0.3) fail for the modular surface, and it is worth separating them:

1. **`δ = 1`.** The limit set of a lattice is the whole boundary circle: it is not porous at any scale, and the
   Ahlfors–David constant of a `δ < 1` regular set is not available. Every known quantitative FUP exponent
   `β(δ)` degenerates as `δ ↑ 1` (`CERTIFIED`: Dyatlov–Zahl and subsequent work give explicit but
   `δ`-degenerate exponents; I do not assert the exact shape of `β(δ)`).
2. **Finite volume with a cusp.** (A.0.3) is a theorem about infinite-volume convex cocompact surfaces, where
   the continuous spectrum comes from funnels. The modular surface's continuous spectrum is the **cusp's**, and
   the resonances are poles of a `1×1` scattering matrix which is an explicit ratio of completed zeta values.
   No FUP-type resonance-gap theorem for cusped finite-area surfaces is known to this record.
3. **Pressure threshold.** All pre-FUP gaps (Patterson–Sullivan/Naud, and Nonnenmacher–Zworski's
   `P(½) < 0 ⟹ gap`, `CERTIFIED`) require the topological pressure at `½` to be negative, i.e. `δ < ½`. For a
   lattice `δ = 1` and `P(½) > 0`; the leading resonance is `s = 1`, which under `s = ρ/2` is **the pole of `ζ`
   at `w = 1`**.

That last identification is the honest content of Q1 and is recorded in §7: *the FUP/pressure degeneracy at
`δ = 1` is the same fact as the pole of `ζ` at `1`*, and the sought gap "below the leading resonance" is, term
for term, the corpus's pole-repulsion mechanism (de la Vallée Poussin), whose depth `O(1/log γ)` is fixed by
the archimedean sea (`R151_005` §2.2; phase 37 doc 111 §3.2). A *uniform* gap is strictly stronger than dlVP,
so the mechanism is not a restatement; it is an unreachable target with no known machinery (Q2).

### A.2 (Q2) Any dynamical/microlocal constraint on resonances of finite-area surfaces beyond Maass–Selberg?

**Answer: none known to this record, and the negative is structural rather than accidental.** Survey, all
`CERTIFIED` except where marked:

* **Selberg's `3/16`** bounds the smallest nonzero **`L²` (cuspidal/residual) eigenvalue** for congruence
  covers. It is not a statement about scattering poles, and under `s(1−s)`-parametrization it constrains
  `λ₁ ≥ 3/16`, a discrete-spectrum fact. It says nothing about `φ`'s poles. (Aside: for `Γ₀(q)` the scattering
  determinant involves Dirichlet `L`-functions, so a "`3/16` for resonances" would be a zero-free region for
  Dirichlet `L`-functions — FATAL-rule territory, and known to be open.)
* **Nonnenmacher–Zworski, Anantharaman-type entropy bounds**: give gaps under a pressure/entropy condition
  that fails at `δ = 1` (above).
* **Dyatlov–Zahl, Dyatlov–Jin (FUP for porous sets), Dyatlov–Jin–Nonnenmacher**: FUP has been extended beyond
  Ahlfors–David regularity (porosity) and used for **control/observability** of eigenfunctions on hyperbolic
  surfaces of all `δ`; there is **not** aware of any consequence of these for the location of scattering
  poles of a finite-area surface, and does not assert the exact statements of these papers.
* **Expositions** (Zworski's survey of resonances; Sarnak's writings on the spectrum of `PSL₂(Z)\H`) present
  the `ρ/2` dictionary as a dictionary. `CERTIFIED`.

Stated honestly: **for finite-area hyperbolic surfaces there is no known constraint on the Eisenstein
resonances beyond the one of Proposition A.1**, because any such constraint is, by (A.0.1), a zero-free region
for `ζ` (or, on `Γ₀(q)`, for Dirichlet `L`-functions). The geometric side has no more information than the
arithmetic side; this is MW-2 on the automorphic square.

### A.3 (Q3) Hecke recurrence / non-concentration for the resonant states `E*(z,ρ/2)`

The Eisenstein series is a Hecke eigenform, `T_p E(·,s) = (p^{s−½}+p^{½−s})E(·,s)` (`IMPORTED`). The
Bourgain–Lindenstrauss entropy bound and Lindenstrauss's AQUE use Hecke recurrence to forbid semiclassical
measures from charging small sets (`CERTIFIED` in statement, not re-read).

The analogue for resonant states would read: *for a resonance `s₀ = ρ/2`, the truncated normalized measure
`|E^T(z,s₀)|² dμ(z) / ‖E^T(·,s₀)‖²` on a fixed compact `K ⊂ X` cannot concentrate on a set of small
Hecke-recurrent dimension.* Three findings.

1. **(i) Meaningfulness.** `E(·,s₀)` is not in `L²`: it grows like `y^{1−s₀}` in the cusp. Normalization
   requires truncation at height `T`, and the truncated norm is given by the Maass–Selberg relation of
   Prop. A.1, whose leading term is `T^{2σ−1}/(2σ−1)` with `σ = Re s₀`. So the normalization constant itself
   depends on `Re s₀` — the quantity one wants to constrain. The statement is formulable but only after one has
   fixed the very unknown.
2. **(ii) Implication for `Re ρ`.** None. A non-concentration bound is a lower bound on the spread of mass on a
   compact piece; the location of the resonance enters the Maass–Selberg identity through the **cusp**
   contribution `T^{2σ−1}` and through the oscillating term `φ(s)T^{2it}/(2it)`. Compact-part non-concentration
   is orthogonal to the cusp asymptotics. R152_001 finds no route from (i) to `σ = ¼`, and the general
   principle in the corpus applies: a lower bound on a positive quantity (mass) is MW-4, the wrong sign.
3. **(iii) Circularity.** The one proved instance of QUE for Eisenstein series (Luo–Sarnak) is proved **on the
   critical line** `s = ½+it` and its proof uses bounds on `ζ(1+2it)` (and in the rate, subconvexity); using it
   to constrain `Re ρ` is circular. `CERTIFIED` (statement known, paper not re-read here).

**Q3 verdict: formulable, empty for `Re ρ`, and circular in its only proved instance.**

### A.4 (Q4) Gauss map: is the obstruction technical or structural?

**Structural. The abscissa of convergence of the branch series of `L_s` is exactly `Re s = ½`.**

> **Proposition A.4.** Let `L_s h(z) = Σ_{n≥1} (n+z)^{−2s} h(1/(n+z))` be the Gauss-map transfer operator. The
> defining series converges absolutely, uniformly on the standard disc, iff `Re s > ½`, and diverges for
> `Re s ≤ ½`. Consequently, on `Re s ∈ (¼,½)` the object called `L_s` is **only** the meromorphic continuation
> of the family `s ↦ L_s`; it is not the transfer operator of any weighted dynamical system there, it has no
> branch decomposition, no positive cone, no Perron–Frobenius leading eigenvalue, and its "iterates" `L_s^n`
> are not sums over `n`-cylinders of the continued-fraction map.

*Proof.* On the disc, `|(n+z)^{−2s}| ≍ n^{−2Re s}`; `Σ_n n^{−2σ} < ∞ ⟺ σ > ½`. The Gauss map has infinitely
many inverse branches, and their derivatives `|T'|^{−1} ≍ n^{−2}`, so the branch series is `Σ n^{−2σ}`. ∎

> **Corollary A.5 (the obstruction, and its identification).** Dolgopyat's method is, in every version known to
> R152_001, an estimate on the **cancellation among the branch sums of `L_s^n`** under a UNI hypothesis on
> the temporal distance function; it produces `‖L_{σ+it}^n‖ ≤ C|t|^{ε}θ^n` with `θ < ρ(L_σ)`, *perturbatively
> around a `σ` where `L_σ` is a genuine positive Ruelle operator with a spectral gap*. On `Re s ∈ (¼,½)` none of
> these objects exists (Prop. A.4). Hence the failure is not a failure of the UNI hypothesis — **the UNI
> hypothesis cannot even be stated there**, since there are no branches to be non-integrable.

The abscissa `σ = ½` of Prop. A.4 is, under `w = 2s`, the abscissa `Re w = 1` of the Euler product: the
Gauss-map branch series and the Dirichlet series stop at the same place, for the same reason. **This is MW-2 in
dynamical clothing**, and it explains why Baladi–Vallée's Dolgopyat estimate lives near `Re s = 1` (i.e. `w = 2`,
deep inside absolute convergence) and why "push it to the critical strip" is not a research programme but a
category error. Mayer's continuation (poles at `s = (1−k)/2`) is a continuation of a *determinant*, not of a
dynamical system; it carries the zeros because `ζ` was put in, which is the corpus's standing lesson on
Hilbert–Pólya realizations (`ROW-D-CLOSURE-PLAN` §8.4).

### A.5 Kill criterion A, applied

(Q1) **yes** (Prop. A.2 and the three hypothesis failures); (Q2) **none known** (§A.2, with the structural
reason: any such constraint is a zero-free region); (Q3) **empty and circular** (§A.3); (Q4) **structural
obstruction** (Prop. A.4, Cor. A.5). All four clauses fire.

**Mechanism A is DEAD for the sign**, recorded with these four reasons. No (P152.A) is formulated. For the
record, the gates were checked and are moot but instructive:

* **`Ξ_a` gate.** No hyperbolic surface has `Ξ_a` (the Euler product with non-unimodular local roots
  `α_± = p^{±a}`) as scattering determinant; what plays the role of the local roots is the Hecke eigenvalue
  `p^{s−½}+p^{½−s}` of `E(·,s)`, whose unimodularity on `Re s = ½` is the **Ramanujan bound for the Eisenstein
  spectrum, which is a tautology** (`E` is the non-tempered/tempered boundary case). So the automorphic picture
  reads magnitude, not phase, exactly as open item (36) requires and does not supply.
* **`Ξ_Q` gate.** Epstein zeta functions of binary quadratic forms do occur in the scattering **matrices** of
  groups with several cusps and of Bianchi groups, as entries and in linear combinations; Davenport–Heilbronn
  produces off-line zeros from such combinations for class number `≥ 2`. Whether the *determinant* of such a
  scattering matrix can have off-line poles is exactly the question of whether a Dedekind zeta or a Hecke
  `L`-function can, i.e. GRH. **R152_001 is not certain of the exact form of the Bianchi scattering
  determinant and does not assert it.** What is certain is that any purely geometric/dynamical gap theorem
  valid for all cusped hyperbolic surfaces would have to be compatible with the existence of off-line zeros of
  Epstein-type combinations, and therefore could not be blind to which combination is taken — a gate the
  mechanism has no means of passing. This was going to be the falsifier had (Q4) survived.

---

## §3 Mechanism B

### B.0 Facts

**(B.0.1) `M(Z)`.** `CERTIFIED` in the precise normalization, `IMPORTED` in shape. `M(Z)` = the Berkovich
spectrum of `Z` with the trivial norm: multiplicative seminorms on `Z` bounded by the trivial one. It is a tree
with root the trivial absolute value `|·|₀`, one branch for each prime `p` carrying `|·|_p^ε`, `ε ∈ (0,∞]`, the
end `ε = ∞` being the seminorm with kernel `(p)` (the "residue field `F_p`" point), and one archimedean branch
carrying `|·|_∞^ε`, `ε ∈ (0,1]`. Reference: J. Poineau, *La droite de Berkovich sur `Z`*, Astérisque **334**
(2010); Lemanissier–Poineau, *Espaces de Berkovich globaux*. (R152_001 has not re-read these; the tree
picture is standard and is asserted only in this shape.)

**(B.0.2) The dictionary (RESTATEMENT).** On the `p`-branch use `u = −log|p|_p^ε = ε log p`. Then `ε = k ∈ N`
sits at `u = k log p`, so:

> **Dictionary B.1.** The corpus's Frobenius lattice `{k log p : p prime, k ≥ 1}` (Papers 44–46) is the set of
> **integer points of the non-archimedean branches of `M(Z)`**, in the coordinate `u`. The Weil explicit
> formula's prime atoms `(log p)p^{−k/2}δ_{±k log p}` sit exactly at those points, with the weight attached by
> hand; the archimedean branch carries the continuous `Γ`-term.

This is a relabelling, nothing more, and is labelled `RESTATEMENT`. Its only value is that the two ends of the
`p`-branch are `ε → 0` (trivial valuation, the root) and `ε = ∞` (the residue field), so the branch is a
geometric picture of the "degree" variable `k` of the Frobenius powers.

**(B.0.3) Potential theory on trees.** `IMPORTED` for the tree facts used below (they are elementary and are
proved here); `CERTIFIED` for the attributions: M. Baker, R. Rumely, *Potential theory and dynamics on the
Berkovich projective line*; A. Thuillier's thesis; Chambert-Loir–Ducros for forms and currents on Berkovich
spaces (over a *fixed* complete valued field).

### B.1 (Q5) Is the Weil form a tree energy?

**Answer: no, and for two independent reasons — a computation and a structural one.**

> **Proposition B.2 (the tree energy of the atomic measure is a constant).** Let `μ = Σ_{p,k≥1}(log p)p^{−k/2}
> δ_{(p,k)}` on `M(Z)`, with `(p,k)` the point `u = k log p` on the `p`-branch, and let `x ∧ y` denote the
> distance from the root to the meet of `x` and `y`. Then the tree energy
> `E(μ) = ∬ (x∧y)\,dμ(x)dμ(y)` equals
> `Σ_p (log p)³ · Σ_{k,l≥1} p^{−(k+l)/2}min(k,l)`: a quantity attached to the arithmetic of the lattice alone,
> **independent of every test function** — finite on each branch, and divergent as `Σ_p (log p)³/p` when summed
> over primes.

*Proof.* Two points on different branches meet at the root, so `x ∧ y = 0`; on the `p`-branch,
`(p,k)∧(p,l) = min(k,l)·log p`. Hence `E(μ) = Σ_p (log p)²·(log p)Σ_{k,l}p^{−(k+l)/2}min(k,l)`. With
`t = p^{−1/2} < 1`, `Σ_{k,l}t^{k+l}min(k,l) = Σ_{m≥1} (Σ_{k,l ≥ m} t^{k+l}) = Σ_{m≥1} t^{2m}/(1−t)² =
t²/((1−t)²(1−t²))`, finite. Summing over `p`, the terms are `(log p)³·p^{−1}(1+O(p^{−1/2}))`, whose sum over
primes **diverges**; so `E(μ) = +∞` unless the measure is first restricted or renormalized. Either way the
value is a number attached to the arithmetic of the lattice alone, with no dependence on any `f`. ∎

(The divergence is itself informative: the tree energy of the Frobenius lattice diverges exactly as
`Σ_p (log p)³/p`, i.e. at the same place as every other unregularized prime sum; the archimedean branch is not
there to cancel it, because the archimedean branch is a *different branch*, met at the root, hence uncoupled.)

> **Proposition B.3 (structural refutation).** Let `κ : [0,∞) → R` be any function and define the tree pairing
> `⟨μ,ν⟩_κ = ∬ κ(x∧y)dμ dν` on measures on `M(Z)`. No such pairing reproduces the Weil form
> `W(f\*\tilde f) = ∬ f(u)\overline{f(v)}K(u−v)\,du\,dv`, for any assignment `f ↦ μ_f` that is linear and
> supported on the branch points of Dictionary B.1.
>
> *Proof.* A tree pairing is a function of the **meet** `x ∧ y` of the two locations; the Weil form is a
> function of the **difference** `u − v` of the two locations in the group `R`. For `x` on the `p`-branch and
> `y` on the `q`-branch with `q ≠ p`, `x∧y = 0` identically, so `⟨·,·⟩_κ` assigns the same value `κ(0)` to every
> cross-prime pair, whereas `K(k log p − l log q)` is a non-constant function of `(p,k,q,l)` — it is `Ĥ` of the
> archimedean kernel evaluated at a point that varies. Since the cross-prime pairs are dense in the relevant
> range of differences, the two bilinear forms differ. ∎

**Consequences, and the match with the recorded no-gos.** Positivity of a translation-invariant kernel on `R`
is a Bochner statement about the **group** `R`; the tree `M(Z)` has no group structure relating `k log p` and
`l log q`, and its potential theory is *per-branch* by construction (different branches meet only at the root).
But the corpus's finding NG-E1 is exactly that the per-place forms are **indefinite** and that "positivity is a
cross-place phenomenon"; MW-3 is that no Hasse–Minkowski principle assembles local positivity in infinite
dimension. Tree potential theory is therefore structurally blind to the only place where the sign lives. The
blueprint's expectation ("the tree only labels the atoms") is **confirmed and proved**.

One further point, in the mechanism's favour and then against it: tree metrics are of **negative type**
(`d(x,y) = |x|+|y| − 2(x∧y)` and `(x,y) ↦ x∧y = ∫ 1_{[root,x]}1_{[root,y]}dℓ` is a positive-definite kernel),
so every tree energy pairing of the standard form is *unconditionally* positive semidefinite on mass-zero
measures. A mechanism whose output is unconditionally nonnegative cannot distinguish `ζ` from `Ξ_a`, from `Ξ_Q`
or from a Beurling system, all of which have the same lattice-of-atoms shape after relabelling. **All four
gates fail simultaneously**, for the single reason that the tree sees only locations and multiplicities.

### B.2 (Q6) Frobenius and a pairing on the square

* **Frobenius.** Poineau's `Z`-analytic spaces are built from `M(Z)` and its affine lines; R152_001 knows of
  **no** Frobenius endomorphism on them, and none can come from the ring: `Hom(Spec Z, Spec Z) = {id}`, which
  is exactly **Theorem 22.17** of Paper 46 (`Spec Z` is terminal, so there is no ring of Frobenius
  correspondences). The branch parameter `ε` is a **flow**, not an endomorphism of the base; naming it
  "Frobenius" is the same move as the scaling flow of the corpus (rows A–C), with the same content.
* **Comparison with `F₁`/`λ`-rings.** Connes–Consani's arithmetic site and Borger's `Λ`-ring/Witt structure do
  carry `ψ_p`, and phase 16 doc 01 records that the `ψ_p` eigenvalues are **integer Adams weights (local
  data)**, not the global `γ_ρ`. **A published comparison between Poineau's global `Z`-analytic geometry and
  either of these is not known to this record; nothing is asserted.** This is the one literature item that
  would have to be checked before any further work, and it does not change the verdict, because even a
  comparison would deliver `ψ_p` with local eigenvalues (phase 16, Route B/C rejection).
* **A pairing on `M(Z) × M(Z)`.** Arakelov theory on `Spec Z` is one-dimensional: the arithmetic Chow group is
  `R` and there is no square. The product of two trees is a two-dimensional cell complex; R152_001 knows of
  **no** published intersection theory or pairing on it, and the Chambert-Loir–Ducros calculus is for
  analytifications over a *fixed* valued field, hence does not apply to a product over two different places.
  The corpus records the same wall independently (MW-5; Theorems 25.6, 25.7: positivity-type constraints on the
  full square are vacuous or infinite).

### B.3 (Q7) Does the audit's expectation survive?

`03-research/AUDIT_A_CATEGORY_CHANGES.md` lists "non-archimedean/Berkovich analytic geometry over `Spec Z`" as
*named but never built*, with the explicit caveat that this is a negative claim from absence of keyword hits.
The expectation attached to it was that a genuinely global analytic space over `Z` might supply the missing `+`
(the additive structure across places). Q5 and Q6 show what such a space supplies: the correct **labelling** of
the Frobenius lattice as integer points of the branches, and nothing about the sign — because the cross-place
coupling, which is where the corpus has located the whole difficulty (NG-E1, MW-3, MW-5), is precisely what the
tree collapses to its root. **The expectation does not survive**; the audit item should be annotated with this
round's result rather than left open as a promising direction.

### B.4 Kill criterion B, applied

(Q5) refuted (Props. B.2, B.3); (Q6) no Frobenius (with Thm 22.17 as the ring-level reason) and no square
pairing known. **Mechanism B is DEAD as a route to the sign.** It survives as Dictionary B.1, a `RESTATEMENT`,
worth at most one remark in Paper 44. No (P152.B) is formulated.

---

## §4 Reserve (not built; corpus status only)

**4.1 `×p` measure rigidity on `R/Z`.** Furstenberg's `×2,×3` problem; Rudolph's theorem (a `×2,×3`-invariant
ergodic measure of positive entropy is Lebesgue) and Lindenstrauss's higher-rank extensions. `CERTIFIED`.
Corpus status: **new by name** (only planning files), but the *object* is old here: the Bost–Connes system is
the corpus's `×N` semigroup and doc 161 (Thm 161.9) is a NO-GO; doc 160 Prop. 160.5 records that the Kronecker
flow crossed product computes `{log k}`, the integers, not the zeros. Rigidity theorems classify *invariant
measures*; the zeros of `ζ` are not a measure-rigidity invariant of the `×p` action — they are the spectrum of
a *representation*, and the equidistribution outputs of rigidity are of the "lower bound on spread" type
(MW-4, wrong sign). Not a sign mechanism as far as this round can see.

**4.2 Model-theoretic methods.** Corpus: absent. The available transfer principles (Ax–Kochen–Ershov, and the
model theory of valued fields) compare `F_p((t))` with `Q_p` for large `p` and are insensitive to archimedean
data; there is no known first-order transfer from a curve over `F_q` to `Spec Z` (this is MW-5/Theorem 22.17 in
another language: the transfer would have to carry the Frobenius, which does not exist). Nothing to build.

**4.3 Transcendence / auxiliary functions; Bombieri–Stepanov.** **Verified as the blueprint asks.**
Stepanov's method constructs an auxiliary function vanishing to high order at the rational points of a curve,
i.e. it is the `X × X` diagonal argument in function-theoretic form; Bombieri's version proves the RH for
curves over `F_q` without cohomology. Corpus: phase-38 doc 116 is an explicit audit of the method, and Paper 46
**Theorem 22.17** closes its transcription: there is no ring of correspondences on `Spec Z` (`Spec Z` is
terminal), so there is no square on which to place the auxiliary function and no degree/index inequality to
extract. The blueprint's expectation is confirmed: Thm 22.17 closes it. The transcendence toolkit proper
(Baker, Schmidt, Bombieri–Vaaler) bounds heights of *individual algebraic numbers*; the zeros are transcendental
data of an `L`-function with no known height, so there is no entry point.

---

## §5 Gates

Because both mechanisms died, the gates are applied as a *post-mortem*: the table records, for each, which gate
it fails, since a mechanism failing a gate could not have produced the sign even had the analytic obstruction
been removed.

| gate | mechanism A (resonance gap) | mechanism B (tree potential) |
|---|---|---|
| **`Ξ_a`** (Euler product, non-unimodular roots `p^{±a}`) | Reads magnitude only: the relevant Hecke eigenvalue `p^{s−½}+p^{½−s}` is unimodular on `Re s = ½` tautologically; nothing in FUP or in Dolgopyat's method sees a phase. **Fails.** | Sees locations and weights only; `Ξ_a`'s lattice of atoms is the same set `{k log p}`. **Fails.** |
| **`Ξ_Q`** (`+` without Euler; Epstein/Davenport–Heilbronn) | Epstein-type functions occur in scattering matrices of multi-cusp and Bianchi groups; a purely geometric gap would have to be blind to which combination is taken. **Fails** (with the caveat of §A.5 on the exact Bianchi determinant). | Tree energy is unconditionally `≥ 0` on mass-zero measures; it cannot separate `Ξ_Q` from `ζ`. **Fails.** |
| **Beurling** (Euler without `+`) | A Beurling system has no surface; but equally, nothing in the dynamical argument used the integrality of `{k log p}`. **Fails or is inapplicable.** | Dictionary B.1 applies verbatim to a Beurling generalized-prime system (replace `log p` by `log q_j`). **Fails.** |
| **`ζ_K` / T1 uniformity** | A gap for `PSL₂(O_K)` would be GRH for `K`; the mechanism is uniform in `K`, hence must be held to GRH. Consistent with T1, but that only raises the bar. | Uniform in `K` trivially (`M(O_K)` is the same tree with more branches), hence held to the same bar. |

---

## §6 Labels

| item | label |
|---|---|
| A.0.1 scattering determinant and `RH ⟺ resonances on `Re s = ¼`` | `RESTATEMENT` (corpus: phase 16 doc 01) |
| Proposition A.1 (Maass–Selberg gives exactly the trivial region) | `PROVED` here, `RESTATEMENT` in content (MW-2 / invariant conclusion 2) |
| Proposition A.2 (`~log T` density ⟹ no BD-type gap with `β > ¼`) | `PROVED` (elementary, from Riemann–von Mangoldt) |
| The three hypothesis failures (`δ=1`, cusp, pressure) and the identification `δ=1 ↔` pole of `ζ` at `1` | `PROVED`/`OBSERVATION`; useful, new in the corpus |
| Q2 "none known" | `CERTIFIED` survey, with a structural reason `PROVED` (any such constraint is a zero-free region) |
| Q3 (formulable, empty, circular) | `ARGUED`; Luo–Sarnak circularity `CERTIFIED` |
| **Proposition A.4** (branch series abscissa `= ½`) and **Corollary A.5** | `PROVED`; the one genuinely new piece of this round for mechanism A |
| Bourgain–Dyatlov, Dolgopyat, Naud, Baladi–Vallée, Mayer statements | `CERTIFIED` (not re-read); exact disc and exact zero placement in Mayer's factorization explicitly **not asserted** |
| Dictionary B.1 | `RESTATEMENT` |
| Proposition B.2 (tree energy is `f`-independent; diverges as `Σ(log p)³/p`) | `PROVED` |
| **Proposition B.3** (meet vs difference) | `PROVED`; the one genuinely new piece for mechanism B |
| "no Frobenius on Poineau's spaces", "no published pairing on `M(Z)×M(Z)`" | `NOT KNOWN TO US`, not asserted as literature facts; the ring-level statement is Thm 22.17, `IMPORTED` from Paper 46 |
| §4 reserve paragraphs | `CERTIFIED` survey + corpus cross-reference |
| FATAL rule | **not triggered**: no zero-free region, moment bound or cancellation is claimed anywhere above |

---

## §7 What goes where

**To Paper 46 §28.4 (the reopening clauses), as two sentences of record — not as new clauses.** The six clauses
are unchanged. Add, in the paragraph that records routes measured rather than moved:

> Two further mechanisms were examined and closed in phase 152. (a) The Eisenstein resonances of the modular
> surface are the points `ρ/2`, and every known resonance-gap mechanism — pressure conditions, Dolgopyat's
> method, the fractal uncertainty principle — requires a limit set of dimension `δ < 1`; for a lattice `δ = 1`,
> and the degeneracy at `δ = 1` is the pole of `ζ` at `s = 1`, so the gap sought is the pole-repulsion of de la
> Vallée Poussin in dynamical clothing, with a uniform strength no method supplies. Moreover the Gauss-map
> transfer operator's branch series `Σ_n n^{−2s}` has abscissa of convergence exactly `Re s = ½`, so on the
> critical strip there is no operator, no branch decomposition and no non-integrability hypothesis to impose:
> the arithmetic-propagation wall in dynamical form. (b) The Frobenius lattice `{k log p}` is the set of integer
> points of the branches of the Berkovich spectrum `M(Z)`; but a tree-potential pairing is a function of the
> meet of two locations and the Weil form is a function of their difference, and distinct branches meet at the
> root, so the tree is blind to the cross-place coupling in which the sign lives.

**To Paper 44, one remark.** Dictionary B.1 only, labelled `RESTATEMENT`: the Frobenius lattice is the set of
integer points of the non-archimedean branches of `M(Z)`, the archimedean branch carrying the `Γ`-term; with
Proposition B.3 appended as the reason the picture is a labelling and not a mechanism.

**To `03-research/AUDIT_A_CATEGORY_CHANGES.md`.** Annotate the Berkovich entry with §3 of this document: the
object is still unbuilt, but its expected payoff is now computed and is nil for the sign.

**No new open item is created. Row D keeps no label and no sign.**
