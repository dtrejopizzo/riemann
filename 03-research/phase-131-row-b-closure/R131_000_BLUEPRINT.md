# R131.000 — Blueprint for closing row B (Paper 44), phase 131

Status: `BLUEPRINT` —
derived and checked by the review; to be written into Paper 44 with complete
proofs by the construction and attacked by the audit. Nothing below is a
citation; every claim must be re-proved in the paper or refuted.

Inputs: Paper 44 as corrected in phase 128 (label `CONSTRUCTED`; B.1 PARTIAL,
B.4 REFUTED AS STATED, B.6 second half OPEN, realization of the integral
contact as a shadow of `G` OPEN); D128.002; PLAN §6; P123.037/038/039/060;
Paper 43 after phase 130 (`𝓝 = 0`, `N_A = D_A`, `N_A^dist = prim ⊕ B_T`,
Thm 9.7 symbol, (8.5) local terms, Thm 8A.7c colimit trace `T_∞`, Thm 8A.9).

---

## 0. The insight: the arithmetic object is the ideal, not the element

Paper 44 takes `Γ_n := E_{a_S(n)}`, `a_S(n) = (1 at ∞; n at each p ∈ S_f)`.
By Lemma 3.3 of Paper 43 (`C_S ≅ R^× × ∏_{p∈S_f}Z_p^×`, canonical
representative `a/φ(a)` with `φ(a) = ∏p^{v_p(a_p)} = n`), the **class** of
`a_S(n)` is

    δ_S(1/n) = (1/n at ∞ ; 1 at every p ∈ S_f) ,

with unit coordinate **1** at every finite place — not `n`. Two consequences,
both checked against Paper 43's proved formula (8.5) for the local terms.

**(a) The element class is invisible to the finite local traces when
`|S_f| ≥ 2`.** The fixed-point classes of place `p` are
`j_p(p^k u) = (p^{−k} at ∞; u at p; p^{−k} at every q ≠ p)` (Paper 43 (9.5b)).
They coincide with `δ_S(1/n)` only if `n = p^k`, `u = 1` **and** `p^{−k} = 1` in
`Z_q^×` for all `q ∈ S_f∖{p}` — false. So a test concentrated at the point
class `δ_S(1/n)` receives **no** shell contribution from any `W_p`, and the
quantity `w_unit(Γ_n) = ∏_{q∤n}|1−n|_q^{−1} = n−1` of Paper 44 Thm 3.3(v) is the
local factor of the **lift** `a_S(n)` evaluated at `q` — it is not the
contribution of the class to any local trace of row A (the class is not in the
image of `j_q` for `q ∤ n`). D128.002 B7 already said `w` is not a value of `T`;
this says why, and it dissolves the "unit-sector obligation" of Paper 44 §9.2:
there is no `n−1` to absorb.

**(b) The unit-averaged class is the arithmetic correspondence.** Define the
**ideal class**

    Γ_n^{rad} := ∫_{K} E_{(1/n, u)} du ,   K := ∏_{p∈S_f} Z_p^× (probability Haar),

the Haar average over units of the graphs of all generators of the ideal
`(n)` — the exact analogue of "the correspondence of the prime ideal", as
opposed to a chosen generator. It lies in the Fell completion of `G`
(Paper 43 Def 3.1; a continuous compactly supported section), it is a
**radial** section (a function of `|w|_S` alone — Paper 45 §12's `G_rad`), and:

  * `Γ_m^{rad} ⋆ Γ_n^{rad} = Γ_{mn}^{rad}` (Haar), `(Γ_n^{rad})^† = Γ_{1/n}^{rad}`
    (the class of modulus `n`), and `Γ_1^{rad} = Δ^{rad}` is the unit-averaging
    projector, which is the identity on the radial sector;
  * `M(Γ_n^{rad}) = (λ_−,λ_+) = (n^{1/2}, n^{−1/2}) = n^{−1/2}(n, 1)`: the
    Frobenius bidegree `(n,1)` in half-density normalization;
  * smeared: for `h ∈ C_c^∞(R)`, `Γ_h := ∫ h(t) Γ^{rad}_{e^{−t}} dt ∈ D_A^{rad}
    ⊂ Corr_A^tr`.

**(c) The contact of the ideal class is `Λ(n) n^{−1/2}`, in row A's own trace.**
By Paper 43 (8.5), `W_p(F) = (log p)Σ_{k≠0}p^{−|k|/2}∫_{Z_p^×}F(j_p(p^k u))du +
(unit packet)`. For `F = Γ_n^{rad}` (a point mass at modulus `1/n`, constant on
`K`): the shell `k` at `p` contributes iff `p^{−k} = 1/n`, i.e. `n = p^k`; the
unit packet vanishes because `F` is constant on units (`c(1) = 0`, Paper 43
(9.14)); no regularization is needed since `1/n ≠ 1`. Hence

    Σ_{p ∈ S_f} W_p(Γ_n^{rad}) = Λ(n)·n^{−1/2}     (n = p^k with p ∈ S; else 0),

with `Λ(p^k) = log p = vol_{d^*x}(p^k Z_p^×)` — the multiplicative Haar volume of
the valuation shell (P123.042 §1). **`Λ` is the shell volume**, and the
vanishing at composite `n` is the statement that no single place has a shell
of modulus `1/n`. This is the Lefschetz contact `Γ·Δ` of row B, realized in
`G`'s declared trace, not in a `Z`-linear model. On the colimit `T_∞`
(Paper 43 Thm 8A.7c) the chart condition `p ∈ S` disappears.

**(d) The archimedean contact.** With `d^*x_∞ = dx/(2|x|)` and both signs,
`W_∞(Γ_n^{rad}) = ½[τ_∞(1/n) + τ_∞(−1/n)] = ½[n^{1/2}/(n−1) + n^{1/2}/(n+1)]
= n^{3/2}/(n²−1) = K(log n)`, `K(t) = e^{−t/2}/(1−e^{−2t})`, and
`K(log n) = n^{−1/2}Σ_{j≥0} n^{−2j}` — one term for each trivial zero `−2j`.
(The odd component gets the difference.) This is the accounting D128.002 B6
asked for: the arithmetic class has an archimedean contact and it is the
`W_∞` term of the explicit formula sampled at `log n`; it is **not** part of
`Λ(n)`.

**(e) Smeared form = row C's geometric side.**
`T(Γ_h) = Σ_n Λ(n)n^{−1/2}[h(log n) + h(−log n)] + W_∞(h)`, a finite sum for
compactly supported `h` (on the colimit). This is Paper 43 (8.5) read on the
radial sector and is what Paper 45 calls `χ_A`. Row B's job is to attach it to
the family `Γ_n` as objects with composition, dagger, bidegree and contact.

**(f) The `Z`-linear cube is the integral model, and its degrees match.**
`deg_det Q_{S,n} = log[L_S : nL_S] = log n = Σ_{d|n}Λ(d) = Σ_{d|n} d^{1/2}·
Σ_p W_p(Γ_d^{rad})`: the lattice-index degree of P123.038 is the **divisor sum
of the finite contacts of the ideal classes** — this is the arrow P123.038 §5
asked for ("lattice-index operation realized as the diagonal shadow … compared
with the analytic trace"), with Möbius inversion (Paper 44 Lemma 5.1, Thm 5.3)
as the passage back: `deg_det Prim_n = log #(Z/Φ_n(1)) = Λ(n)` = the finite
contact of `Γ_n^{rad}` times `n^{1/2}`. So the cotangent cube, the finite-orbit
determinant `det(1−T|V_n) = Φ_n(1)` (P123.039) and the shell volume all compute
the same number, and the paper must say which is a theorem in `G` (the shell
volume) and which are integral models with matching degree.

---

## 1. Clause-by-clause instructions

**B.1 (source).** `W = (N_{≥1}, ×)` with the divisor poset. State it; the
symmetry **is** realized (`G` is commutative on the radial sector; `C_S`
abelian). The divisor arrows are realized on the integral model `Q_{S,·}`
(P123.038) and on the ideal classes as the **support/divisibility of moduli**;
they have no morphisms in `G` (P123.082) and none are needed by B.1 as written.
Close B.1 `PROVED`, with the honest sentence.

**B.2 (realization).** `n ↦ Γ_n^{rad}`: strong monoidal from `(N,×)` to
`(G_rad, ⋆)`, gauge/chart/lift independent **by construction** (averaging over
units is exactly the operation that kills the lift ambiguity of P123.018 §2).
Prove it. Also keep `n ↦ Γ_n = E_{a_S(n)}` (Paper 44 Thm 4.3) as the element
realization, with the relation `Γ_n^{rad} = ∫_K E_{u}⋆Γ_n du`.

**B.3.** unit `Δ^{rad}` (identity on `G_rad`), dagger, half-density `n^{−1/2}`
canonical; prove `(Γ_n^{rad})^† = Γ^{rad}_{1/n}` and `M(Γ_n^{rad}) =
(n^{1/2},n^{−1/2})`.

**B.4 (contact).** Literal clause stays REFUTED AS STATED (Paper 44 §6.2a is
right: the derived diagonal pullback is the fixed complex, and a `C`-linear
category cannot carry `Z/p`, P123.022). Replace by the **amended B.4**:
"the derived contact of `Γ_n^{rad}` with the diagonal, computed in the declared
category (Paper 43 Thm 7.1/Thm 8A.9: rank-one classes with half-density–
Lefschetz weights, Haar-regularized), has finite-place degree `Λ(n)n^{−1/2}`,
equal to `n^{−1/2}·deg_det[Z→Φ_n(1)→Z]`, the integral cotangent model of
P123.037 on the lattice `L_S ⊂ X_S`; the identification is of **degrees**, and
object-level identification is impossible in a `C`-linear category
(P123.022)." Mark the amendment as the review's proposal mirroring the A.6
decision, for the repository record; record in Paper 44 §2 and in PLAN §6.4 as a note.
Prove the amended B.4 in full (this is theorem (c) above, plus (f)).

**B.5.** `Λ(n)` from the shell volume (theorem in `G`) **and** from the cube
(Paper 44 Thm 5.3) — both, with the equality of the two stated as the theorem.
`n = 1`: `Γ_1^{rad} = Δ^{rad}`, identity/excess, treated by the regularized
identity term (Paper 43 (8.5) at `t=0`), not by the formula.

**B.6.** General family by structure ✓ (no case analysis). Classes into
`N_A`: with `𝓝 = 0`, `N_A = D_A`; `Γ_h ∈ D_A^{rad}` for smooth `h`;
`Γ_n^{rad} ∈ N_A^dist` as the limit of `Γ_{h_ε}`, `h_ε → δ_{−log n}` (prove
convergence in the strong dual: `I_A(Γ_{h_ε}, G) → T(Γ_n^{rad}⋆G^†)`, and
`M(Γ_{h_ε}) → (n^{1/2},n^{−1/2})`); its canonical primitive component in the
splitting `N_A^dist = prim ⊕ B_T` (Paper 43 Thm 9.14b) is
`(I_A(Γ_n^{rad},·), 0)`; its moments are `λ_±`. Close B.6 `PROVED`.

**B.7 (discriminating test).** Keep Paper 44 Thm 6.4 (integral models) and ADD
the mechanism **on the carrier**: at `p | n`, the fixed factor `1/|1−x|_p` is
`1` on the shell `p^kZ_p^×` (linear-dilation contact contributes nothing), and
the cyclotomic `log p` is the **Haar volume of the shell** = the measure of the
unit orbit of the ideal — the deck group `μ_n` in measure form. Compute `p`,
`p²` explicitly: `Γ_p^{rad}`: shell `k=1`, contact `(log p)p^{−1/2}`;
`Γ_{p²}^{rad}`: shell `k=2`, contact `(log p)p^{−1}`; fixed contacts at the
element class: `|1−p|_q^{−1}`, `|1−p²|_q^{−1}` at `q | p−1`, `q | p²−1`, which
the class does not see. So the two differ and the mechanism is located on the
carrier, not only on `G_m/Z`.

**B.8.** Keep the table; add columns: finite contact `Λ(n)n^{−1/2}` of
`Γ_n^{rad}`, archimedean contact `n^{3/2}/(n²−1)`, bidegree
`(n^{1/2},n^{−1/2})`; delete or re-label the `w_unit` column as "local factor
of the lift at `q ∤ n`; not a contact". Rows `2,4,8,6,12,30,9,10,16`.

**B.9.** Compatibility with A now rests on Paper 43 (8.5), Thm 9.7, Thm 8A.7c,
Thm 9.14a–b — cite exactly. Independence: no zero, no `Λ` as input (`Λ` is
**derived** as a shell volume — say so under Paper 43 Remark 9.7a's rule).

**§9 hand-off to C.** Rewrite: (9.1) prime packet is now a theorem of B
(smeared form (e)); (9.2) the `n−1` obligation is **dissolved**, with the
reason (a); correct the cross-reference to Paper 45 §11 (it claimed to
discharge an obligation that does not exist; C's campaign will fix Paper 45,
but Paper 44 must state the truth now). New hand-off: the archimedean contact
(d) and the identification `Λ = shell volume`.

**Corrections to Paper 44's existing text (mark `[REBUILT, phase 131]`):**
Thm 3.3(iv)–(v) and (3.3)–(3.5): keep (i)–(iii) (coprime support of the two
**integral** complexes; the dichotomy of the local factor evaluated on the
lift); re-state (iv)–(v) as properties of the lift `a_S(n)`, not of the class
or of any trace; Remark 3.7 becomes the statement that `T(Γ_n^{rad})` **is**
a value of row A's local terms (exact, no regularization, `1/n ≠ 1`); §6.1 Thm
6.1(iii) becomes theorem (f); §8 Thm 8.1 rewritten with `N_A = D_A`, `𝓝 = 0`
(Paper 43 is no longer `CANDIDATE`); §10 ledger; §0 summary; README.

**What must NOT be claimed:** any statement about zeros or the sum over zeros
for point classes (the explicit formula for `δ_{log n}` diverges); any sign;
`𝓝_∞ = 0`; that the integral torsion `Z/Φ_n(1)` is an object of `G`.

## 2. Checks the review performed

* `a_S(n)/n = (1/n;1,…,1)`: canonical representative (Lemma 3.3).
* `j_p(p^k u)` has `p^{−k}` at `q ≠ p`: Paper 43 (9.5b); so `δ_S(1/n) ∉ Im j_q`
  for `q ∤ n`, and `∈ Im j_p` only after unit averaging.
* Shell sum on the radial point mass: `(log p)p^{−k/2}` iff `n = p^k`.
* `½[n^{1/2}/(n−1) + n^{1/2}/(n+1)] = n^{3/2}/(n²−1) = K(log n)`, and
  `= n^{−1/2}Σ_{j≥0}n^{−2j}`.
* `Σ_{d|n}Λ(d) = log n` (classical), matching `log[L_S:nL_S]`.
* `M(δ_{|w|=1/n}) = (n^{1/2}, n^{−1/2})`.

## 3. Deliverables

1. Paper 44 `main.md` rewritten where needed, complete proofs, every change
   marked `[REBUILT, phase 131]`; new §3bis (ideal classes), new theorems for
   (b)–(f); amended contract table; ledger; README.
2. `R131_001_REPORT.md`: clause by clause; blueprint claims found
   false, if any, with counterexamples; theorem numbers added.
3. PLAN §6.4 note on the B.4 amendment (proposed; pending decision).
