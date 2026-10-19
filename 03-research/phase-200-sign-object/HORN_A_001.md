# HORN_A_001 — Binary decision on Horn A (P46 §19.9), phase 200, round 20b

Sources: P46 `main.md` §§11.4–11.5 (Thm 11.13, Thm 11.14), full §19 (Def 19.1,
Thm 19.2, Thm 19.21, Thm 19.23, Thm 19.25, Cor 19.25b, Rem 19.25c, §19.9); R142_004 l.141–147 (finding J1, origin of
`η_F(a−b)`); P47 `main.tex` l.123 (`W_T = 𝔞_T + 2Re(A B̄)`); SPEC_SIGN_OBJECT_010 §H3; SPEC_006 (C-pol, Theorem O3);
LEMMA_E_EPSTEIN_001.

## Summary (≤200 words)

(1) The pair `{E_w, K−E_w}` of Cor 19.25b has degrees `(d, 1−d)` with `d > d_0^{(R)} ≈ 325` (Thm 19.23: `d > 324.96`;
certified instance `d = 400`). Degree `> 1`: **Cor 19.25b does not kill Horn A**. The `Δ` of §19.9 absorbs exactly that
pair (`R(E_w) < Δ(d)`). (2) The term `η_F(a−b)` is the polarization of the polar term `2Re(AB̄)` of P47 and vanishes
when `F ∈ P_T`. But Thm 19.25 does **not** use it: its proof uses identity (19.3), without Cauchy–Schwarz and without primitivity.
Moreover Cor 19.25b already holds in `𝒟_p = P_c^∞ ⊕ ℝK` with `F = F_R^♭` primitive. The term `η_F` appeared elsewhere: in the
sufficiency step of the gated candidate (R142 J1). C-pol repairs that step, but does not touch the frame defect.
(3) Theorem HA (PROVED): for every finite `Δ`, the Horn A hypothesis implies in two lines `I_∞(G,G) ≤ 0` for every
real class `G` of degree 0, without using Thm 12.3. With the admissible `Δ_♮(d) = max(0,(d²−d)/4)`, the hypothesis
**is equivalent** to that positivity, with `h⁰ ≡ 0`. **Horn A is a trivial reformulation of the objective** and contributes no
tool. With P46's minimal `Δ` it is strictly stronger: objective + sufficiency (P33-6, REF-D). The
falsifiers (Epstein, `a_P`, `Ξ_a`) fail Horn A, but only because they fail the objective. Label: **NO-GO as a
route (trivial reformulation, PROVED)**. With this the Hodge-transfer line is closed.

## 0. Index and corpus check

"Horn A" and "(c′)" have no entry in ROUTES-TRIED-INDEX (SPEC_010 l.327). Neighbors: P33-6 (sufficiency in moments) and
R142_004 J1 (`η_F`). This memo does not retry anything indexed. It decides the first substep requested by SPEC_010 §D and, along the way,
the complete logical status of Horn A.

## 1. Exact statement of Horn A (P46 §19.9)

Notation from P46 §11 and §19: `D^W` is the Weil class, `I_∞` the form (11.6) and `M(E) = (a,b) = (Φ_E(1), Φ_E(0))`.
Also `deg E = a+b = I_∞(E,2K)`, `K` is the Pólya class (`Φ_K = ξ`, `deg K = 1`, `I_∞(K,K) = ½`), `𝓝_∞` is the
radical and

  `R(E) = ½ I_∞(E,E) − ¼ deg E + χ`  (Def 19.1),  with  `R(K−E) = R(E)`  (Thm 19.2).

Let `Δ : ℝ → ℝ_{≥0}` with `Δ(0) = Δ(1) = 0` and `Δ(d) = Δ(1−d)`. **Horn A** is the hypothesis of Thm 12.3 with (c)
replaced by (c′). It requires the existence of `h⁰ : D^W → ℝ_{≥0}` such that:

- (a) `h⁰ ≥ 0`;
- (b′) if `h⁰(E) > 0`, then there exists `E' ≥ 0`, `E' ≢ 0`, with `E − E' ∈ 𝓝_∞`;
- (c′) `h⁰(E) + h⁰(K−E) ≥ R(E) − Δ(deg E)` for every `E ∈ D^W`.

Per §19.9, the proof of Thm 12.3 continues to hold under (c′), because (c) is only used at `E = nF`, of degree 0, and there
`Δ = 0`. The "maximum defect" of P46 is `Δ_P46(d) = max(0, d²(1−s_*²)/4 − d/4)`, with `s_* = inf_F C_F √(2/W_F)`.

*Minor remark (PROVED).* `Δ_P46` is not symmetric under `d ↦ 1−d`: the difference is `(1−2d)(−s_*²)/4`. This does not matter,
because (c′) at `E` and at `K−E` is the same inequality with defects `Δ(d)` and `Δ(1−d)`. The effective defect is then
`min(Δ(d), Δ(1−d))`, which for `d > 1` equals `Δ_P46(d)`.

**Restriction to primitive classes (gate in P_T).** Tests in `P_T` have `A = B = 0`, i.e.
`Φ(0) = Φ(1) = 0`. Hence they have degree 0 and `η = 0`. The classes of `P_T ⊕ ℝK` are `G + dK`, of degree `d`, with
`I_∞(G,K) = 0`. On them

  `R(G + dK) = d²/4 − d/4 + ½ I_∞(G,G) + χ`.   (1.1)

**What would have to be proved for Horn A to give the sign.** One would have to build `h⁰` satisfying (a), (b′) and (c′) without knowing
the sign of `I_∞` in degree 0 beforehand. Then Thm 12.3 (or Theorem HA(i) below) would give `I_∞(G,G) ≤ 0` in
degree 0, which is Weil positivity `W ≥ 0` on the carrier.

## 2. Is `η_F(a−b)` the polar term of P47? Does Thm 19.25 use it?

**2.1 Identification (PROVED).** Let `F` be real of degree 0. Then `Φ_F(0) = −Φ_F(1) =: η_F`. The polar
package of (11.6) gives

  `Φ_E(0)Φ_F(1) + Φ_E(1)Φ_F(0) = −bη_F + aη_F = η_F(a−b)`.

In P47 (l.123) the complete form is `W_T(F) = 𝔞_T(F) + 2Re(A(F) B̄(F))`, where `A` and `B` are the two polar
moments (the values of `Φ` at `1` and `0`, up to normalization). The diagonal term `2Φ_F(0)Φ_F(1)` of `I_∞(F,F)` corresponds
to `2Re(AB̄)`. `η_F(a−b)` is its **polarization** off the diagonal, i.e. the associated bilinear form evaluated at
`(E,F)`. If `F ∈ P_T`, then `η_F = 0` and the term vanishes for every `E`. **Yes: C-pol zeroes it out on P_T.**

**2.2 Where `η_F(a−b)` lived (PROVED, by reading).** R142_004 J1 (l.141–147) locates it in Prop D.32.3(iv). That is
the Cauchy–Schwarz bound `|I_∞(E,F)| ≤ √(W(E)W(F))` from the **sufficiency** argument for the gated candidate, and
P46 §19.9 repeats it. The same record states: "§D.31 unaffected (it uses the identity (D.31.2), not Cauchy–Schwarz)."

**2.3 The proof of Thm 19.25 does not use the pole (PROVED, by reading).** Step-by-step walkthrough:

- Step 1 uses only (b′), the invariance of `deg` modulo `𝓝_∞` and `deg E' > 0` (Thm 11.13).
- Step 2 uses the linearity of `deg` and Serre symmetry.
- Step 3 uses Thm 19.23. This in turn uses the exact identity (19.3): `deg E_{t,d} = d`,
  `I_∞(E_{t,d},E_{t,d}) = d²/2 − t²W_F` and `I_∞(E_{t,d},F) = −tW_F`. It also uses the bound `|I_∞(E',F)| ≤ C_F deg E'`
  from Thm 11.14(ii), which is the integral of `E' ≥ 0` against `w_F`. P46 states this explicitly after Thm 19.21: "No
  Cauchy–Schwarz, no RH and no primitivity enter: only `deg F = 0`."

Moreover, Cor 19.25b establishes the defect on `𝒟_p = P_c^∞ ⊕ ℝK` with `F = F_R^♭ ∈ P_c^∞`, which is **primitive**:
`η = 0` and `A = B = 0` (Lemma 19.25a(v)). By Rem 19.25c(iii), primitive `s_*` is computed over `P_c^∞`. Hence the
frame defect **holds on P_T**, with a witness in P_T.

**Verdict on the decisive question.** Thm 19.25 did not need the pole and continues to hold on `P_T ⊕ ℝK`. The new reason
from SPEC_010 is correct as a fact (on P_T, `η_F = 0`), but it repairs a different step: the sufficiency step, not the frame defect.
This alone is not enough to kill Horn A, because Horn A is not (c) but (c′). That is decided in §3.

## 3. Binary decision: the degree of the pair

**Proposition 3.1 (PROVED, from Cor 19.25b).** One has `deg E_w = d` and `deg(K−E_w) = 1−d`. The conditions are
`d > 1`, `d²(1−s_F²) > d − 4χ` and `s_F²d²/2 < t²W_F < d²/2 − d/2 + 2χ`. With `χ = 0` this forces `d > (1−s_F²)^{−1}`,
and `s_F ≤ s_{F_R^♭} ≤ 0.998469` gives `d > 325`. The certified instance of Thm 19.23 has `d = 400`. **The degree is > 1.**

**Corollary 3.2 (PROVED). Δ absorbs the pair.** By (19.3),
`R(E_w) = d²/4 − t²W_F/2 − d/4 + χ < d²(1−s_F²)/4 − d/4 + χ`. With `χ = 0` and `s_* ≤ s_F` one obtains
`R(E_w) < Δ_P46(d)`. Then (c′) at `E_w` holds with `h⁰(E_w) = 0`, and step 2 of Cor 19.25b does not get started.
No witness of ray form `tF + dK` kills Horn A, because Δ was defined precisely to absorb them. Therefore
Horn A is **not** NO-GO by Cor 19.25b.

It remains to see what Horn A is once it survives.

**Theorem HA (PROVED).** Let `(W⁰)` be the statement: `I_∞(G,G) ≤ 0` for every real class `G ∈ D^W` with `deg G = 0`.

- (i) For **every** finite `Δ` (with the normalizations of §19.9) and every `χ`: if `h⁰` satisfies (a), (b′) and (c′), then
  (W⁰) holds.
- (ii) Let `Δ_♮(d) := max(0, (d²−d)/4)`. It is admissible: `Δ_♮ ≥ 0`, `Δ_♮(0) = Δ_♮(1) = 0` and it is symmetric, because
  `d²−d` is invariant under `d ↦ 1−d`. With `χ = 0` and `Δ = Δ_♮`, (W⁰) implies that `h⁰ ≡ 0` satisfies (a), (b′) and (c′).
  Therefore the Horn A hypothesis with `Δ_♮` **is equivalent** to (W⁰).
- (iii) The same holds restricted to `P_T ⊕ ℝK`, with `G ∈ P_T`.

*Proof of (i).* Suppose `G` is real, of degree 0, with `I_∞(G,G) = c > 0`. Let `E_n := 2K + nG`. Then
`deg E_n = 2` and, since `I_∞(K,G) = ½ deg G = 0`, one gets `R(E_n) = ½(2 + n²c) − ½ + χ`, which tends to `∞` with `n`.
Also `deg(K−E_n) = −1`, so `h⁰(K−E_n) = 0` by step 1 of Thm 19.25 (which only uses (b′)). By (c′),
`h⁰(E_n) ≥ R(E_n) − Δ(2) > 0` for large `n`. By (b′) there exists `E' ≥ 0`, `E' ≢ 0`, with `E_n − E' ∈ 𝓝_∞`. Then
`deg E' = 2` and `I_∞(E',G) = I_∞(E_n,G) = nc`. By Thm 11.14(ii), `nc ≤ 2C_G < ∞`, which is false for large `n`. ∎

*Proof of (ii).* Every class of degree `d` is written `E = dK + G` with `deg G = 0`, and `R(E) = d²/4 − d/4 + ½I_∞(G,G)`.
Under (W⁰) one has `R(E) ≤ (d²−d)/4`. If `d ∉ (0,1)`, this is `≤ Δ_♮(d)`. If `d ∈ (0,1)`, then `(d²−d)/4 < 0`, so
`R(E) < 0 = Δ_♮(d)`. In both cases (c′) holds with `h⁰ ≡ 0`, (b′) is vacuous and (a) is trivial. The converse is (i). ∎

*Proof of (iii).* It is the same, with `G ∈ P_T`. In that case `C_G < ∞` by (11.17). ∎

**Reading.** Horn A does not die from the degree, but it dies from circularity:

- With `Δ_♮`, the canonical `h⁰` is **zero**. Thus (c′) literally says "`R ≤ Δ_♮`", which is (W⁰), and the Hodge
  transfer becomes the identity.
- With a smaller `Δ`, such as `Δ_P46 < Δ_♮`, Horn A is **strictly stronger** than (W⁰). It additionally requires:

  **(Eff_Δ) OPEN.** For `d > 1`, every real class `E` with `deg E = d` and `R(E) > Δ(d)` is `𝓝_∞`-equivalent to a
  nonzero, nonnegative class.

  With `Δ_P46` this says: `I_∞(G,G) > −s_*²d²/2` ⇒ `dK + G` is effective modulo `𝓝_∞`. This is **half the sufficiency**
  of an exponential moment problem: the necessary conditions of Thm 11.14(ii) would imply effectiveness. It is
  P33-6 (REF-D), and as a tool it is harder than the objective, not easier.

No admissible `Δ` gives a hypothesis **weaker** than (W⁰): that is (i). No `Δ` gives a hypothesis different from
"(W⁰) ∧ sufficiency", which is (ii) plus the argument above. That is why Horn A, as a tool, cannot produce the
sign. It can only rewrite it.

## 4. Falsifiers

- **Epstein (Lemma E, T = 8/5, `Z_Q`).** There is an `F ∈ P_T` with `𝔞^Q_T(F) < 0`. In the frame transported to `Z_Q` (ARGUED: the
  transport proof of §19.7 uses only bilinearity, (11.6) and `C_F < ∞`, and here the zeros off the line have
  `β ≈ 0.93 < 1`, so `w_F` and `C_F` remain finite), that is a primitive class `G`
  of degree 0 with `I^Q_∞(G,G) > 0`. By Theorem HA(i), Horn A is **false** for `Z_Q`, for any `Δ` and any
  `χ`.
- **`a_P`** (witnesses of P_T with negative form): the same happens. Horn A is false.
- **`Ξ_a`:** false, consistent with Thm 12.4.

This is fine in the sense that Horn A is **not** comb-generic. But the reason is uninformative: it separates `ζ` from
Epstein only through (W⁰), which is the objective itself. C-E′ holds tautologically. No primitive gate yields Epstein
information beyond the sign of `I_∞` on P_T.

## 5. Labels and index entry

- Proposition 3.1 and Corollary 3.2 (degree of the pair `(d,1−d)`, `d > 325`; Δ absorbs the pair): **PROVED**.
- §2: `η_F(a−b)` is the polarization of P47's polar term and vanishes on P_T: **PROVED**. Thm 19.25 and Cor 19.25b do not
  use the pole and hold on `P_T ⊕ ℝK`: **PROVED** (by reading of the proofs).
- Theorem HA (Horn A ⇒ (W⁰) for every finite `Δ`; Horn A with `Δ_♮` ⟺ (W⁰)): **PROVED**.
- **Horn A: NO-GO as a route (trivial reformulation of the objective, PROVED).** It cannot be weakened: with `Δ_P46` it only
  adds sufficiency (Eff_Δ), **OPEN/REF-D (P33-6)**.
- **Hodge-transfer line complete** (phase 135, Thm 12.3, Horn A): **closed**. (c) is unsatisfiable (Thm 19.25), and
  (c′) is the objective or the objective plus sufficiency. Horn B (enlarging the class of representatives) remains OPEN in P46
  §19.9. Not addressed here.

**Entry for ROUTES-TRIED-INDEX:**

> HORN_A_001 (phase 200, r20b): Horn A from P46 §19.9 ((c′) with defect Δ, gate on P_T). The pair `{E_w, K−E_w}` from
> Cor 19.25b has degrees `(d, 1−d)` with `d > 325`, and Δ absorbs it, so there is no NO-GO by degree. But Theorem HA
> (PROVED) shows that (c′) with any finite Δ implies `I_∞ ≤ 0` in degree 0 in two lines, and that with
> `Δ_♮ = max(0,(d²−d)/4)` it is equivalent to that with `h⁰ ≡ 0`. Horn A is a trivial reformulation of the objective: NO-GO as a
> route. `η_F(a−b)` = polarization of `2Re(AB̄)`. Thm 19.25 does not use the pole and holds on P_T. Do not retry gates or
> defects on (c).
