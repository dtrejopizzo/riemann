# R129.001 — row A rebuild: report

Target: Paper 43 (`04-papers/43-row-a-correspondence-algebra/`),
`main.md` and `appendix.md`.  Input: `D128.001` (findings A1–A12 accepted,
R1 rejected), `D128.004`, `P123_A_ACCEPTANCE_SPECIFICATION`.

**Verdict of this rebuild: `WEIL-STRENGTH-COMPLETE` is not earned.**
Clauses A.6 and A.8 are `OPEN`, A.7 is `PARTIAL`.  The remaining obstacles are
named below as exact missing statements, not as attitudes.  The paper's label
is now `CONSTRUCTED`, with seven clauses proved on the declared category.

---

## 1. Per clause

### A.1 Carrier and coefficients — `PROVED` (weakened restriction clause)

Carrier `X_S=[A_S/Γ_S]`, square `Y_S`, coefficients `E_P` and source `U`
(P123.121, `PROVED-IN-REPOSITORY`).  Proposition 3.2 now has a proof
(§3.3, parts (i)–(v)).

*Change of substance.*  The restriction clause is weakened.  The previous text
claimed chart restriction of objects via P123.014 §4.  P123.018 §2 refutes
that by an explicit counterexample (`S={∞,2}⊂T={∞,2,3}`: `a=(1,1)` and
`a'=(2,2)` are equal in `C_S`, but their extensions-by-one are distinct in
`C_T`).  What is claimed now: chart compatibility of the arithmetic lifts
(`L_{ST}(a_S(n))=a_T(n)` literally, P123.038 §1) and of the coefficients
(P123.121 (11)).  A restriction functor on all objects is not claimed.  What
row A actually uses is chart compatibility of the **trace**, which is proved
outright as Theorem 8A.5.

### A.2 Correspondences — `PROVED` on `G`

Proposition 3.2(i)–(iv): stability (P123.064 §2), closure under `⋆`
(P123.019/P123.014 (2.3)), geometric localization on `Y_S` (P123.016 (2.3)),
and infinitely many pairwise non-isomorphic objects, proved from the
intertwiner classification (3.3) and infiniteness of `C_S` — not, as before,
by forward reference to the separating theorem.

### A.3 Composition, unit, excision — `PROVED` on `G`

Unchanged: Theorems 4.1, 4.3, Corollary 4.4, all with proofs, from
P123.124–125.

### A.4 Transpose — `PROVED` on `G`

Unchanged: Theorem 5.3, from P123.073–074 (5.1).  The obstruction `Hom(U,N)=0`
is read correctly (Proposition 5.1).

### A.5 Trace — `PROVED` on a declared smeared domain (was: never addressed)

This is new; finding `A1` was that A.5 appeared nowhere.  A125.014 Thm. 7.1,
the only note that ever discharged it, argues from A125.014 Thm. 1.1, which
A125.016 and A125.017 both refute; that route is abandoned and **not cited**.

* **Domain** (Def. 8A.1): `Corr_A^tr`, bounded complexes of finite sums of
  *smeared* graph objects `E_F`, `F ∈ D_A = C_c^∞(C_S)`, the compactly
  supported scalar Fell sections of P123.014 (5.1).  Section map
  `s(K)=Σ(−1)^n F_n`.
* **Target** (Def. 8A.2): `T_A = Pic_b(C)`, based determinant lines
  (P123.012 §3).  `Tr_A(K)=Det_S^rel(s(K))`.
* **Additivity, shift, cone** (Thm. 8A.3): proved, from additivity of `s` and
  P123.012 (3.2)–(3.3).
* **Cyclicity** `T(K⋆L)=T(L⋆K)` (Thm. 8A.4): proved twice — from
  commutativity of `C_S`, and independently from P123.012 (3.5).  *Recorded
  honestly in the paper:* on this sector cyclicity is weak, because the
  external class group is abelian.
* **`†`-reality** (Thm. 8A.4): proved from the new Lemma 8.4,
  `τ_v(x^{−1})=τ_v(x)`, which the previous version asserted without proof.
* **Restriction compatibility** (Thm. 8A.5): proved outright,
  `T_T(J_{ST}F)=T_S(F)`.  Old places: P123.042 §4 and P123.046 §4 (same
  relative traces).  New places: the local test is constant on `Z_ℓ^×` and
  zero off it, so both terms of (8.5) vanish.  This is a genuine new
  computation and is the correct form of the clause, since object-level
  restriction is refuted (P123.018 §2).
* **Determinant compatibility** (Thm. 8A.7): `exp T` is literally a limit of
  renormalized Fredholm determinants of trace-class operators
  (P123.012 (2.1)–(2.4)), with the biextension of P123.012 §4.
* **Homotopy invariance** (Thm. 8A.8): proved, using idempotent-completeness,
  which is now declared in Definition 3.1.

**What remains open inside A.5, and is stated in the paper:** the categorical
shadow `Tr_A` of §7 (the full Hochschild complex) is **not** identified with
the analytic trace of §8.  P123.039's status line forbids calling its
construction "the full A.5 shadow", and P123.007 §8 lists this comparison as
the live open arrow.  The clause as written ("a trace on a declared
trace-class domain, additive, cyclic, compatible with restriction and
determinant") is discharged; the comparison of the two targets is not, and is
recorded as a limitation rather than a discharge.

### A.6 Numerical equivalence — `OPEN` (algebraic half proved)

*Proved.*

* **Theorem 9.1**, the repair of finding `A3`: the two Tate functionals are
  built **directly on the external class group**, from the product formula
  `|γ|_S=1`, so `ρ_T^ext(u)=(|u|_S^{−1/2},|u|_S^{1/2})` is a character of
  `C_S` and no descent is used.  This is P123.014 §6, whose status line reads
  `PROVED-IN-REPOSITORY` for "the external two-Tate realization and its exact
  hyperbolic ruling form", and the P123.018 override touches only §§1 and 4 of
  that note, neither of which enters.  Multiplicativity, `†`-behaviour
  (P123.014 (6.3)), surjectivity of `ρ_T`, and the matrix `[[0,1],[1,0]]` are
  proved.
* **Theorem 9.3**: biadditivity on sums, shifts and cones, Hermitian symmetry,
  joint continuity.  This was never proved before.
* **Theorem 9.4**: radical closed, two-sided `⋆`-ideal, `†`-stable, stable
  under shifts and cones; `N_A` Hausdorff with continuous descended `⋆`, `†`
  and a nondegenerate pairing.  Proved in full, following P123.007
  (3.3)–(3.4) transported to `D_A` in the half-density normalization.  The
  previous proof used the undefined symbol `T(E_w)`.
* **Theorem 9.5**: a nonzero mixed sector, by an exact computation that uses
  **no regularization at all**, because the two tests are supported away from
  the identity class where Theorem 8.8 makes `T` an absolutely convergent
  integral.  For `u,u'∈1+pZ_p` with `v_p(1−u)=j≠j'=v_p(1−u')` and sections of
  equal mass and equal radial push-forward supported in
  `u(1+p^mZ_p)`, `u'(1+p^mZ_p)`, `m>max(j,j')`:
  `T(F)−T(F') = μ(log p)(p^j−p^{j'}) ≠ 0`, while `λ_±(F)=λ_±(F')`.

*Open, and why.*  That `N_A` **contains** the ruling plane.  `λ_±` are
functionals on `D_A`; for them to define classes in `N_A` they must annihilate
the numerical radical `𝓝`.

  **(O-A6-1)** Missing statement: `λ_±` lie in the closed span of
  `{⟨·,L⟩}`; equivalently the two points `s=±1/2` of the trivial character lie
  in the support of the spectral measure of `T`.  Note the paper proves the
  weaker fact that `T` itself annihilates `𝓝` (approximate identity), so the
  obstruction is specific to `λ_±`.  Row C proves the corresponding statement
  on its radial sector (D128.004, surviving item 3), but row A may not import
  it, and the acceptance spec forbids A.6 resting on the explicit formula.

  **(O-A6-2)** A proved perfect-pairing completion: vanishing of the boundary
  radical `R_∂` of P123.007 §4, which that note leaves `OPEN`.

This is exactly the arrow P123.007 §8 draws and calls open.  Recorded as
`OPEN`.

### A.7 Effectivity — `PARTIAL`

*Proved.*  Theorem 10.2, now with a proof (intrinsicness via the half-density
row measures, closedness, stability under `+`, `≥0` scaling, `⋆`, `†`, gauge
and chart maps, and the distinction from operator positivity), at the level
P123.074's status line permits — graph **elements** and finite complexes at
fixed `S`.  Theorem 10.3: the image in `N_A` is a convex `⋆`/`†`-stable cone;
properness in `D_A`.

*Open.*  **Properness after the numerical quotient.**  The previous proof
paired with `e_+`, i.e. used `λ_+` on `N_A` — the same open point (O-A6-1).
It is withdrawn.  P123.010's own status line lists exactly this as `OPEN`
("properness after numerical quotient/completion, effective descent in the
stronger sense of lifting local positive factorizations, and compatibility
with the still-open completed mixed RR determinant"); the previous version
cited P123.010 as if it were closed.

### A.8 Mixed Riemann–Roch — `OPEN`

*Proved for `λ_RR = Det_S^rel`:* existence, nonvanishing and convergence
(P123.012 Thm. 2.1); additivity (P123.012 (3.2)); the biextension with its
Hermitian, additive/conjugate-additive structure and logarithmic character
`I_A` (P123.012 §4); principal/gauge invariance (P123.012 status line);
restriction (Thm. 8A.5); an equality formula in `T_A`,
`log λ_RR(F)=Σ_v W_v(F)` with `W_v` explicit.

*Open, exactly.*  Clause A.8 requires `λ_RR` to **extend the intrinsic
periodic ruling determinant to the mixed sector**.  The two notes previously
cited disclaim this in their own status lines and are no longer cited for it:

* P123.108: "It is **not** identified with the geometric biextension or
  arithmetic RR correction."
* P123.109: "Its geometric RR identification remains open."

Missing statements:
  **(O-A8-1)** the determinant/cohomology realization `Φ_det` of P123.007 §8,
  transporting diagonal, dagger and trace into the periodic Deligne ruling
  category and extending `λ_per` to mixed kernels;
  **(O-A8-2)** a geometric origin for the endpoint anomaly of P123.108/110
  (the cocycle identity is proved there; its biextension-of-RR reading is not);
  **(O-A8-3)** (O-A6-1), since without a ruling plane in `N_A` there is
  nothing to compare the ruling determinant with.

### A.9 Classical control — `PASSED on the automorphism sector`

Theorem 6.1 now has a proof: an explicit functor `Φ` from the graph sector of
a group of automorphisms of `C/F_q` to perfect kernels on `C×C`, matching
composition (transverse fibre product, P123.011 (2.2), with the half-density
twist cancelling by the projection formula), the unit, the transpose
(`D_h`, with `A_DUALITY_WORK`'s `D_h(O_{Γ_f})=σ_*i_{f*}(h⊗f^*h^{−1})` and
`h²=ω_C`), and the diagonal contact
`χ(LΔ^*O_Δ)=(1−g)−(g−1)=2−2g=Δ·Δ`, plus `χ=0` for a fixed-point-free
automorphism, read off an empty intersection with no fixed-point formula as
input.

*Explicitly not claimed:* the cone comparison of P123.011 §4, which P123.021
§1 refutes by the two-point example (`(e−t)^†(e−t)=2e−2t` is a sum of squares
with a negative coefficient; `t` is effective with eigenvalues `1,−1`;
containment fails both ways and survives passage to the numerical quotient);
and any comparison with non-invertible correspondences, P123.021 §2 showing
that for `deg f = d > 1` the cycle-level inverse of `Γ_F` is `Q^{−1}Γ_F^t`.

### A.10 Independence — `PROVED`

No `Λ(n)`, no distinguished `Γ_n`, no Meyer formula, no zero of zeta, no RH,
no positivity.  The archimedean term is P123.035 (3.1), proved there without
Meyer's coefficient (which P123.035 §1 shows fails a Gaussian check).
P123.012 §1: "Only the geometric/local side of this theorem is used."

---

## 2. Definition 8.1 (finding `A2`) — resolved by declaring the regularization

The previous definition was ill posed in three ways, all now recorded in
`main.md` §13.6: (i) the P123.109–110 germ is constructed for small external
Bruhat tests at one normal place and `β_w` is not such a test; (ii) the germ
and the lattice expression (8.2) were never proved equal, and the paper
defined `T` by one and computed with the other; (iii) `Σ_v log τ_v` is the
wrong shape — the relative trace is `Σ_v W_v`, a sum of local distributions
whose **densities** are the `τ_v`, and the same error appears in the appendix
sentence withdrawn under finding `A10`.

The replacement (`main.md` §8):

* **Definition 8.6**: `T(F) = lim_Λ [Tr(θ(F)R_Λ) − 2F(1)logΛ]` — a declared
  regularization, on `D_A`.
* **Theorem 8.7** (existence and local decomposition): the limit exists
  (`IMPORTED` `C`: Connes's semilocal cutoff trace theorem, P123.012 §1,
  audited P123.004) and equals `Σ_v W_v(F)` with `W_p` given exactly by
  P123.042 (3.2) and `W_∞` by P123.035 (3.1).
* **Theorem 8.8**: on `D_A^0` (tests vanishing near the identity class) the
  sum is an absolutely convergent integral — **no regularization**.
* **Theorem 8.9**: any two functionals agreeing with (8.6) on `D_A^0` differ
  by a distribution supported at the identity class; at finite places a
  multiple of `δ_1`, at the archimedean place a finite combination of its
  derivatives.  The concrete comparison between P123.012's counterterm
  `2F(1)logΛ` and P123.046's `F(1)Σ(L_p+1)log p` is `c·F(1)`.
* **Remark 8.10**: the previous Lemma 8.2 — "two admissible regularizations
  differ by `c·log|w|`, hence by a ruling term" — is **withdrawn**.  The
  ambiguity is `c·F(1)`, and no proof that `δ_1` is a ruling term is known
  to me.  This is why Theorem 9.5 is proved on `D_A^0`.
* **Remark 8.11**: `T(Δ)` is withdrawn.  `Δ=E_1` is the Dirac section, a
  multiplier of the Fell core, not an element of it (P123.014 §5); it is not
  trace class, which is the expected state of affairs and is what the
  renormalization exists to handle.

Finding **R1** (rejected by the audit) is now a lemma of the paper:
Lemma 8.2(ii) proves that at a **fixed** unit `x≠1` the cutoff trace of
P123.042 (2.1) is *eventually constant* in `L`, equal to `|x|^{1/2}/|1−x|_p`;
the divergence P123.042 (3.1) exhibits (`I_L=L+1`) is in the integral over the
unit group.  Remark 8.3 records this.

---

## 3. Corrections from phase 128 that are kept

All of them, with their `[CORRECTED, phase 128 …]` markers intact:
Thm. 9.3's hypotheses stated inline and its "isomorphic shadows" clause
deleted (now Thm. 9.5); Appendix D.2's negative-valuation correction
(`τ_p(σ)=p^{−|v_p(σ)|/2}` uniformly, per P123.042 §2); D.3/D.4 restricted to
`u ∈ 1+pZ_p` with the `p=7`, `u=−1` counterexample recorded; Appendix A.2's
sentence withdrawn; the stale `IMPORTED (I-1)` label at Thm. 7.1(b) corrected;
Theorem 7.4 withdrawn.  The import count is corrected again: **three**, not
one and not two (§12: `W` Wodzicki/Meyer excision, `C` Connes's semilocal
cutoff trace, `RR` the six-functor formalism for perfect kernels).  `C` is now
the load-bearing one, because `T` is defined by it.

---

## 4. The invertible sector (finding `A12`) — §11bis

Stated plainly: every generator of `G` is the graph of an **invertible**
external class, and row A is constructed on the automorphism-graph sector.
The previous dismissal of P123.082's prescription ("add non-invertible
objects") on the strength of Corollary 7.5 is withdrawn as a non sequitur —
Corollary 7.5 is about additive invariants, not about which objects the sector
contains — and the corresponding sentence in §13.1 is corrected.

What is true and recorded: in the adelic setting the acting group is the idele
class group and it acts by invertible dilations (P123.013 §4's two-level
carrier), the local weights `τ_v` are the fixed-point weights of those
dilations (P123.042), and row B's family sits inside the sector
(`Γ_n=E_{a_S(n)}`, P123.038 §1).  What is **not** established: any
non-invertible object, any bidegree, any index theorem, and — because
P123.021 §2 shows the transpose is not the inverse for `deg > 1` — any
extension of the dagger to non-invertible graphs.  Therefore **equality of
structural burden with Weil's proof is not established**, and the paper says
so.

---

## 5. Summary table

| clause | status after rebuild | obstacle if open |
|---|---|---|
| A.1 | `PROVED` (weakened restriction clause) | — |
| A.2 | `PROVED` on `G` | — |
| A.3 | `PROVED` on `G` | — |
| A.4 | `PROVED` on `G` | — |
| A.5 | `PROVED` on `Corr_A^tr` | comparison of the categorical shadow (§7) with the analytic trace (§8) is open, but is not part of the clause text |
| A.6 | `OPEN` | (O-A6-1) `λ_±` annihilate `𝓝`; (O-A6-2) perfect-pairing completion |
| A.7 | `PARTIAL` | properness after quotient, which needs (O-A6-1) |
| A.8 | `OPEN` | (O-A8-1) `Φ_det`; (O-A8-2) geometric origin of the anomaly; (O-A8-3) = (O-A6-1) |
| A.9 | `PASSED` on the automorphism sector | non-invertible comparison absent |
| A.10 | `PROVED` | — |

**Label: `ROW A: CONSTRUCTED`.  `WEIL-STRENGTH-COMPLETE` is not claimed and,
on the present repository, cannot be claimed: A.6 and A.8 both reduce to
statements no note in the corpus proves.**

Rows B (Paper 44) and C (Paper 45) were not modified.  One consequence for
Paper 45 is recorded in `main.md` §14.1: it may cite Theorem 9.1's external
Tate characters on `C_S`, which are proved, but not "the ruling plane of
Theorem 9.1 in `N_A`", which §9.3 declares `OPEN`.
