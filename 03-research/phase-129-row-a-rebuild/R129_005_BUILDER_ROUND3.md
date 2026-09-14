# R129.005 — row A rebuild, round 3: builder report

Date: 2026-09-12.  Target: Paper 43.  Input: `R129.004` (auditor, round 2).

**The auditor's central finding is accepted without reservation: round 2's
claim that clause A.6 is structurally blocked, and that A.6 and A.10 are in
tension, is FALSE.**  It is withdrawn in full.  The A.10-clean route the
auditor pointed to works, and it yields a stronger theorem than the route
itself required: **the numerical radical vanishes.**

---

## 1. The withdrawal (step 1)

Round 2's §9.3 argued from "`T` is carried by Haar-null slices `j_v(Q_v^×)`
while `λ_±` are Haar integrals" that `λ_±` could not be reached from `T`, and
that the only corpus route (P123.035 §5's polar packet = `λ_−+λ_+`, via the
explicit formula) is barred by A.10.

The error is a confusion of supports.  The radical is a condition on **Fourier**
support, not on support in the space variable:
`𝓝 = {F : F̂ = 0 on supp T̂}`.  `c·δ_1` is carried by one point and has full
Fourier support.  So the observation had no implication and was not an
argument.  Withdrawn: display (9.6), the paragraph "Why the only known route
is forbidden here", and the "structural finding" about the specification.
Recorded in `main.md` §13.7 rather than deleted, with the lesson that an
impossibility claim needs a proof exactly as much as a possibility claim does.

The correct formulation is now §9.3.1: `λ_∓(F) = F̂(ε=0, τ=∓i/2; (1))`, the
value of the **analytic continuation** of the entire Mellin transform of a
`C_c^∞` function off the unitary axis — so `λ_±` are not points of `Ĉ_S`, which
is also why round 2's "spectral measure" phrasing was ill posed.

---

## 2. The new mathematics

### Theorem 9.7 — the symbol of `T`.  `PROVED`.

Using Lemma 3.3, `Ĉ_S` is a disjoint union of copies of `{0,1}×R` indexed by
the systems `(κ_q)` of finite-order characters.  From (9.5b),
`χ(j_p(p^k w)) = η_p(χ)^k κ_p(w)` with `η_p = p^{−iτ}∏_{q≠p}κ_q(p)^{−1}`, and
(8.5) gives, with `ζ_p = p^{−1/2}\bar η_p`:

    Ŵ_p(χ) = (log p)·2Re( ζ_p/(1−ζ_p) )   if κ_p = 1,
    Ŵ_p(χ) = − c(κ_p)·log p                if κ_p ≠ 1.

The unramified case is the geometric series over the shells (Lemma 8.2(i),
`vol_{d^*x}(p^kZ_p^×)=\log p`).  The ramified case uses the **exact** identity
`∫_{Z_p^×}(κ(u)−1)/|1−u|_p\,du = −c(κ)`, which is P123.105 §3 (4)–(5) read
with `φ=κ`.  Both are bounded on a component and real-analytic in `τ`.

Archimedean: `Ŵ_∞(ε,τ) = −\log|τ| + O(1)` uniformly in the parity.  Proved
directly: the only singularity of `τ_∞(x)=|x|^{1/2}/|1−x|` is at `x=1`, in the
positive component, where `sgn^ε = 1` for both parities; there
`τ_∞(e^t)d^*x = (1/|t| + O(1))dt`, and
`∫_0^1(\cos τt − 1)/t\,dt = −Cin(|τ|) = −\log|τ| + O(1)`.  Away from `x=1` the
integral converges absolutely (`|x|^{−1/2}dx` at `0`, `|x|^{−3/2}dx` at `∞`)
and is bounded, indeed `o(1)` by Riemann–Lebesgue.  Real-analyticity: the
Mellin transform is holomorphic in `|Re s|<1/2` by the same bounds.  For
`ε=0` this agrees with P123.035 (4.1), `\log π − Re ψ(1/4+iτ/2)`; the **odd**
archimedean symbol is nowhere computed in the corpus, which is why the
asymptotic is proved here directly — it is all that is used.

Consequence: `T̂ → −∞` on **every** component, so `T̂` vanishes identically on
none, so its zero set on each component is **discrete**.

Also proved (9.13): `T(H) = ∫ Ĥ T̂ dχ + c·H(1)`, with the interchange
justified — `Ĥ` is supported on finitely many components (unit level) and
Schwartz in `τ`, while `T̂` grows logarithmically.

### Theorem 9.8 — (T5′): `𝓝 = 0`.  `PROVED`.

For `F∈𝓝` and all `G`, `0 = ∫F̂\overline{Ĝ}(T̂+c)dχ` by (9.13) and Plancherel.
`T̂+c` still tends to `−∞` and is still real-analytic, so **the open constant
`c` of (O-A5-3) does not affect the argument**.  Restricting `G` to one
component (`G = χ_𝔠·g`, `g∈C_c^∞(R^×)` of the right parity) makes
`F̂T̂` a tempered distribution annihilated by all `ĝ`, hence `0` a.e.; the
zeros of `T̂` are isolated; `F̂` is continuous; so `F̂ ≡ 0` and `F = 0`.

**This closes (O-A6-1)**: `λ_±` annihilate `𝓝 = {0}`.  And `N_A = D_A`.

*Inputs used:* (8.5) = P123.042 (3.2); P123.105 §3; P123.035 (3.1)/(4.1);
Lemma 3.3.  *Not used:* any zeta zero, `Λ(n)`, Meyer's formula, the explicit
formula, positivity.  **A.10 is untouched.**

### Theorems 9.11, 9.12 — (T1), (T2), (T3).  `PROVED`.

P123.017 §§1–4 transferred to `D_A` with `M=(λ_−,λ_+)`.  I checked its
statements verbatim first.  Its inputs are `M` continuous, multiplicative,
surjective with `M_0(f^†)=\overline{M_1(f)}` (its (1.2)–(1.3)); `I_∂`'s radical
properties; `β_T` nondegenerate.  On `D_A` these are Theorem 9.1
(multiplicativity, `λ_∓(F^†)=\overline{λ_±(F)}`, surjectivity), Theorem 9.4,
and P123.014 (6.4).  P123.017's own (1.4) says the module structure "is
precisely `ρ_T^{ext}` of P123.014", so the transfer is exact, not analogical.

* **(T1)** `𝓝_W = 𝓝 ∩ D_A^0` is a closed two-sided `†`-stable ideal
  (P123.017 Prop. 2.1 + Thm. 3.1, reproved here), and by Theorem 9.8 it is
  `{0}`.
* **(T2)** `0 → D_A^{prim} → N_A → B_T → 0` is exact and canonical, with
  `B_T = C²`, `β_T = [[0,1],[1,0]]`, `†` exchanging `e_∓`, and the idele
  classes acting by `|u|_S^{∓1/2}` on `B_T`.
* **(T3)** The primitive sector is **nonzero**, written out explicitly:
  `Φ := F − F'` of Theorem 9.5 satisfies `λ_∓(Φ)=0` (the two Tate integrals
  factor through the radial profile and the common coset volume
  `vol(1+p^mZ_p)`, by translation invariance of Haar on `Z_p^×`) and
  `T(Φ) = ν(\log p)(p^{j}−p^{j'}) ≠ 0`.  Moreover `I_A` is **nondegenerate**
  on `D_A^{prim}`, proved by a translate/boundedness argument: a functional
  vanishing on the codimension-two `D_A^0` is `a\overline{λ_−}+b\overline{λ_+}`,
  and testing on `G_w` makes the left side bounded in `w` while the right side
  is `a|w|^{1/2}\overline{λ_−(G)}+b|w|^{−1/2}\overline{λ_+(G)}`, unbounded
  unless `a=b=0`.

### Theorem 9.13 — (T4).  `PROVED`, as a negative theorem.

`S := (D_A^{prim})^{⊥I_A} = \{0\}`, by the same translate argument (which
never used `F ∈ D_A^0`).  The `I_{vec}`-orthogonal coincides with it, since
`I_{Tate}(F,G)=β_T(MF,MG)=0` automatically for `G ∈ D_A^{prim}`.

So the exact sequence (9.16) has **no orthogonal splitting**: `B_T` is a
canonical *boundary quotient*, not a subobject, and the literal reading of
A.6's "contains the ruling plane" is unattainable on this carrier by
orthogonality.  I did not manufacture a splitting; I proved none of this kind
exists.  The residual is therefore a **reading of the clause**, labelled
**(R-A6)**: P123.017 §4's reading ("the rulings and primitive mixed classes
belong to one numerical object as boundary quotient and kernel.  No
noncanonical splitting and no formal direct sum is used") and its §8 ("this
closes A.6 in the appropriate correspondence-module sense") make A.6 `PROVED`;
the subobject reading does not, and would require some other canonical lift.

### Theorem 9.14 — (T6).  `PROVED`; (O-A6-2) closes.

P123.017 §§5–6 transferred: `J(F) = (G↦I_A(F,G), M(F))` into `D_A' ⊕ B_T` is
injective (by `𝓝_W=0`), its closure `N_A^{dist}` is complete and nuclear, the
vector pairing is separating, and `D_A` acts continuously.  P123.017 §5 says
this "removes the unspecified *boundary radical* left in P123.007" — which was
round 2's (O-A6-2).  P123.017 §6's caveat is kept: `N_A^{dist}` is a complete
numerical **module**, not a distribution algebra; A.6 does not ask for
products of distributions.

### Theorem 10.3a — properness of the effective cone in `N_A`.  `PROVED`.

`𝓝 = 0` makes the quotient map the identity, so properness in `D_A`
(pointwise) is properness in `N_A`.  Round 1 proved this circularly, round 2
withdrew it; it now holds for a reason P123.010 could not have used.

### Proposition 8A.7a — the conductor seminorms dominate the trace.  `PROVED`.

`|W_p(F)| ≤ (\log p)[Σ_{k≠0}|a_{k,1}| + Σ_κ c_p(κ)|a_{0,κ}|]`, the second sum
by the exact identity `∫_U(a(u)−a(1))/|1−u|_p du = −Σ_κ c_p(κ)a_{0,κ}` of
P123.105 §3.  So `T` **is** continuous for the conductor-graded seminorms
(2.2), which P123.121 §1 proves submultiplicative.  This converts (O-A8-4)
from "one approach failed" into a precise missing estimate — see §4.

---

## 3. The G-findings

| id | disposition |
|---|---|
| G1 | **Accepted.**  `(c_T − c_S)F(1)` added to (8A.12).  I tried to prove `c_T = c_S` and failed; what the attempt yields (the unit packet vanishes at a new place, which is why the correction is pure-shell) is kept, and `c_T=c_S` is folded into (O-A5-3).  On `D_A^0` the ambiguity drops, which is the only form used. |
| G2 | **Accepted; the central item.**  See §§1–2 above. |
| G3 | **Accepted.**  (9.6) deleted; replaced by the Fourier-support formulation of §9.3.1. |
| G4 | **Accepted.**  The "P123.018 counterexample does not apply" paragraph deleted as a non sequitur.  P123.018 §2 stands unqualified; `π_{TS}` is a different, splitting-defined map, and its arithmetic correctness is supported by P123.042 §4 and P123.046 §4, as the next paragraph of the proof verifies. |
| G5 | **Accepted.**  One-liner installed: `⟨K^†,L⟩ = T((s(K)⋆s(L))^†) = conj(T(s(K)⋆s(L))) = conj(⟨K,L^†⟩) = 0`. |
| G6 | **Accepted.**  §14.1 now writes `T = Σ_v W_v + c·F(1)`. |
| G7 | **Accepted.**  Cross-reference corrected to (8A.13). |
| G8 | **Accepted.**  P123.035 §5 is now "states", and it is cited only for the scalar normalization of the two Tate moments, which is what it proves. |
| G9 | **Accepted.**  `𝓝 ⊆ D_A` and `N_A = D_A/𝓝` defined outright (9.9); the `Corr_A^{tr}` version is its preimage under `s`. |
| G10 | **Accepted.**  The impossibility reading is withdrawn; Prop. 8A.7a supplies the degree-one estimate and reduces the obstacle (see §4). |
| G11 | **Accepted.**  (O-A5-6) added: P123.014 §7 asks for a *faithful* lift; `𝓝=0` gives faithfulness of the represented ray `θ`, but not injectivity of `F ↦ E_F` into `L_S^c` as bimodules. |

---

## 4. A.8: what I attempted, and the exact missing statements

Neither (O-A8-1) nor (O-A8-2) is closed.  I read P123.007 §8, P123.108 §§3–4
and P123.110 §§3–5 in full.

**(O-A8-2).**  The analytic side is complete and strong: the anomaly is an
explicit convergent endpoint Fredholm determinant
`A_{S,q}(F,G) = det_{H_{end}}(1+C_∞ d)` (P123.110 (6)); it is provably
**nonzero** (P123.108 §3's single-shift example gives `1/(1−st)` from the
recurrence `d_n=(1+st)d_{n−1}−st\,d_{n−2}`); it satisfies the cocycle
`A(F,G)A(F⋄G,K)=A(G,K)A(F,G⋄K)`; it is adjoint-compatible; and by
P123.110 §4 (8) it is chart-independent.  Both notes then say the same thing:
P123.108 §4 — "This is not a proof that it equals the correction in a
source-defined determinant line or biextension: that identification still
needs construction"; P123.110 §5 — "its existence alone does not construct a
geometric biextension".

  **Exact missing statement.**  A line bundle `L` on `N_A × N_A` with a
  trivialization of `L_{F⋄G,K}⊗L_{F,G}⊗L_{G,K}^{−1}⊗L_{F,G⋄K}^{−1}` realizing
  that cocycle geometrically, plus a proof that `A_{S,q}` is its determinant
  character.  The cocycle is proved; what is missing is an object whose
  cocycle it is.  I see no route from the present repository: every
  construction in P123.105–110 is a limit of finite-rank determinants of
  cutoff operators, and none carries a base over which a biextension could be
  formed.

**(O-A8-1).**  P123.007 §8's arrow requires a functor transporting the
diagonal multiplier, dagger and trace into the periodic Deligne ruling
category and extending `λ_{per}` to mixed kernels.  Round 3 strictly improves
the *source* of that arrow — `N_A` is now `D_A` with a nondegenerate pairing,
a canonical hyperbolic boundary quotient and a separated nuclear completion —
and constructs nothing on the target.

  **Exact missing statement.**  A monoidal functor
  `Corr_A^{tr} → (periodic Deligne ruling category)` carrying `⋆` to its
  tensor, `†` to its duality, `Δ` to its unit and `Tr_A = Det_S^{rel}` to
  `λ_{per}`, restricting on `e_∓` to the two Tate characters of Theorem 9.1.

**(O-A8-4) = (O-A5-1), reduced.**  P123.107 (6) writes the germ as
`log Δ_φ(z) = −Σ_{r≥1}(−1)^{r+1}z^r[Σ_χ c(χ)a_χ^r]/r`.  Prop. 8A.7a is the
`r=1` estimate in the submultiplicative seminorm `v_{0,1}`.

  **Exact missing statement.**  `|Σ_χ c(χ)a_χ^r| ≤ C ρ^r` with `ρ<1` in terms
  of `v_{0,1}`, uniformly in `r`, so that the germ is holomorphic and
  continuous on a `v_{0,1}`-ball; together with the analogue for the coupled
  induced blocks of P123.109 §2 (stated there via `A = max_χ Σ_k‖T_{k,χ}‖`,
  `B = max_χ Σ_k‖T_{k,χ}‖_1`).  This is an inequality, not a construction.

**A.8 is the binding constraint on row A.  No shortcut found.**

---

## 5. Theorems (T1)–(T6): status

| | statement | status |
|---|---|---|
| **T1** | `𝓝_W = 𝓝 ∩ D_A^0` closed two-sided `†`-ideal | **PROVED** (Thm. 9.11); and it is `{0}` |
| **T2** | `0 → D_A^{prim} → N_A → B_T → 0` exact, `β_T=[[0,1],[1,0]]`, `†` exchanges `e_±` | **PROVED** (Thm. 9.12) |
| **T3** | primitive sector nonzero; `I_A` nondegenerate on it | **PROVED** (Thm. 9.12, written out) |
| **T4** | "contains" vs quotient | **PROVED as a negative**: no orthogonal splitting (Thm. 9.13).  Residual **(R-A6)**: the reading of the clause |
| **T5′** | `𝓝 = 0`, i.e. `supp T̂ = Ĉ_S` | **PROVED** (Thms. 9.7, 9.8) — the decisive theorem |
| **T6** | separated complete nuclear realization; (O-A6-2) | **PROVED** (Thm. 9.14) |

---

## 6. Per-clause table

| clause | verdict | exact remaining obstacles |
|---|---|---|
| **A.1** | **PARTIAL** | (O-A1-1) geometric descent for `C_X`,`C_Y`; (O-A1-2) a restriction functor on objects (the class-group map `π_{TS}` now exists) |
| **A.2** | **PARTIAL** | the declared completion is not proved to be a localization on `Y_S`; (3.3) is transferred from P123.082's algebra to `U` (Rem. 3.6) |
| **A.3** | **PROVED** on `G` | — |
| **A.4** | **PROVED** on `G` | — |
| **A.5** | **PARTIAL** | (O-A5-1) determinant continuity — now reduced to an explicit estimate; (O-A5-2) chart invariance, proved **false**; (O-A5-3) the constant `c`, including `c_T=c_S`; (O-A5-4) objects vs presentations; (O-A5-5) `Sh` vs `Tr_A`; (O-A5-6) faithfulness of `F↦E_F` |
| **A.6** | **PROVED**, modulo the reading **(R-A6)** | `𝓝=0` (Thm. 9.8); `λ_±` descend; canonical hyperbolic exact sequence (Thm. 9.12); nonzero primitive sector with nondegenerate `I_A`; separated completion (Thm. 9.14).  (O-A6-1) and (O-A6-2) are **CLOSED**.  Residual: whether "contains" means P123.017 §4's exact sequence (then A.6 is proved outright) or a subobject (Thm. 9.13 proves that is unattainable by orthogonality) |
| **A.7** | **PARTIAL** | properness on `N_A` now **PROVED** (Thm. 10.3a); (O-A7-1) properness on `N_A^{dist}` (P123.017 §7 verbatim); (O-A7-2) lifting of positive factorizations |
| **A.8** | **OPEN** — the binding constraint | (O-A8-1) `Φ_det`; (O-A8-2) a geometric object whose cocycle is the proved anomaly cocycle; (O-A8-4)=(O-A5-1).  (O-A8-3) is closed, subsumed into (R-A6) |
| **A.9** | **PASSED for the formalism**, automorphism sector | `Φ` is out of a surrogate `G_Λ`; `†` antilinear vs `D_h` linear; cone comparison refuted (P123.021 §1) and unused |
| **A.10** | **PROVED** | — and it is **not** in tension with A.6; round 2's claim to the contrary is withdrawn |

**Label: `ROW A: CONSTRUCTED`, with A.6 closed in P123.017 §4's sense.**
`WEIL-STRENGTH-COMPLETE` is not claimed: A.8 is open, and A.1, A.2, A.5, A.7
are partial.

Papers 44 and 45 were not modified.  One restriction round 2 placed on
Paper 45 is **lifted** (`main.md` §14.1): it may now cite Theorem 9.8 and the
exact sequence (9.16), with the caveat that `B_T` is a quotient and statements
of the form "the ruling classes lie in `N_A`" must be phrased through `M`.
