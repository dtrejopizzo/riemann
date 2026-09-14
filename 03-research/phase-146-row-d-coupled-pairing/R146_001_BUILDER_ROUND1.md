# R146.001 — Builder round 1, phase 146: the degree form on `Z[Frob]`, and where the count stops

*Builder: Claude Opus 5. Date 2026-09-14. Blueprint of record: `R146_000_LEAD_BLUEPRINT.md`. Inputs read
in full before writing: `CORPUS_CHECK_R146.md`, `CORPUS_CHECK_R146b.md`, `R145_005` (closing decision),
`R145_001` §D.41.2 (dictionary, Gram, Theorem D.41.6) and §D.42 (Proposition D.42.5), `R145_004` (Q0, Q1,
the two warnings), Paper 44 §§3ter, 5, 6bis, 8bis (Thm 3ter.4, Thm 3ter.10, Thm 8bis.1 with the §12
correction K1, Thm 8bis.2, Rem 8bis.1c, Thm 8bis.4a, `Sh_Z`, `deg_det`), Paper 46 §§11–12 (Thm 11.8,
Thm 11.13) and Prop 14.2, `R140_001` §D.23.3bis (the three Gram forms) and §D.23.1 (`F_1 = K+K_{odd}`,
`F_2 = K−K_{odd}`), `R142_001` Lemma D.31.4 and Prop. D.31.5 (`s_1 = 0.99846016271880910923…`).*

> **[ROUND-2 STATUS, 2026-09-14.** Audited by `R146_002_HOSTILE_AUDIT.md`: **14 MAJOR, no FATAL**; the
> FATAL screen passes and the script is clean. Six `PROVED` stamps are downgraded, four statements are
> **withdrawn**, and the round's terminal diagnosis and phase-147 recommendation are **replaced**. Every
> repair is marked in place below as `[R2: …]`; the substantive round-2 work — the exact computation of
> `δ_m − δ_n` from Paper 44 Thm 8bis.1b and the **single-prime tower**, the first arithmetic diagonal in
> this line that is *computed* rather than assumed — is in `R146_003_BUILDER_ROUND2.md` §D.47. Read this
> document only together with that one.]**

**Warning discipline carried in every section.** (W-a) *deliver the count, never the positivity*: by
Proposition D.42.5 a positivity statement about the degree form **is** RH. This round delivers (i) the
reconstruction of the form from Euler-product data, (ii) two explicit **negative** witnesses, and (iii) the
statement of exactly which entry is not a count and what its sign would have to be. **No positivity of any
degree form is claimed or proved anywhere below**; §D.45.3 is the paragraph that says why the remaining
freedom must not be exercised. (W-b) `g = 1` is degenerate twice, and §D.45.1 shows the degeneracy is not
incidental: it is exactly what hides the counterterm.

**Numerics.** One script, `scripts/cosh_test_cmn.py` (`--fast`, margins printed), for §D.44.1's Hasse test,
§D.45.1's witness scan and §D.45.2's cosh test. Every numerical statement below is additionally proved by
hand, or marked `CERTIFIED` with the script line that produces it.

---

## D.44 — Q0: the form is already in the Euler product

### D.44.0 Normalization (the one thing that must be fixed before anything else)

Paper 44's Frobenius carries the **half-density** bidegree `M(Frob_n) = (n^{1/2}, n^{−1/2})` (Thm 3ter.6(iii)):
the degree has been absorbed (Rem 3ter.6a). The model's additive structure `m + nπ` lives on the
**un-normalized** side, where `Γ_{q^a}·F_2 = q^a = \deg π^a` and `Γ_{q^a}·Γ_{q^b} = q^{\min}N_{|a−b|}`
(`R145_001` D.41.6(i) before the weight `q^{−|n|/2}` is applied). All of §D.44–§D.45 is written
un-normalized; the dictionary is `Γ_n^{un} = n^{1/2}·(\text{half-density class})`, so that

    bideg(Γ_n^{un}) = (Φ(1),Φ(0)) = (n,\,1),\qquad \deg Γ_n^{un} = Φ(0)+Φ(1) = n+1 .        (146.1)

This matches the model exactly: `\deg Γ_{q^a} = 1 + q^a` there (`D_E·(F_1+F_2)`, D.41.6(iii)).

**Definition D.44.1 (the Euler-product data, un-normalized).** For `m,n ≥ 1` put

    d_n := n                       ("\deg Frob_n"; the F_2-pairing, (146.1)),
    L(m,n) := \min(m,n)·Λ\!\big(\max(m,n)/\min(m,n)\big)
            = \begin{cases}\min(m,n)\,\log p, & \max/\min = p^{k},\ p\ \text{prime},\ k ≥ 1,\\
                            0, & \text{otherwise,}\end{cases}                                 (146.2)
    L(n,n) := δ_n   \quad(\textbf{the diagonal counterterm; not fixed by any count — §D.45.1}).

`(146.2)` is Paper 44 Theorem 8bis.1 (`44/main.md:3317–3386`, with the §12 correction K1) transported to
(146.1): the half-density entry is `G^{Frob}_{mn} = Λ(\max/\min)(\min/\max)^{1/2}·c_N(m,n)`
(`R140_001` Definition D.23.11, (D.23.7)), and `(mn)^{1/2}·Λ(\max/\min)(\min/\max)^{1/2} = \min·Λ(\max/\min)`.
**[R2, M8 — WITHDRAWN AND CORRECTED.** Round 1 wrote: *"The chart constant `c_N(m,n) → 1` as `N → ∞` and
is suppressed throughout; it is a volume of a compact group, never negative, and it does not affect a single
sign below."* **False.** By (8bis.2b) and (8bis.0), `c_N(m,n) = ∏_{s∈S_f∖(P(m)∩P(n))}((s−1)s^{N−1})^{−1}`,
which **decays geometrically to `0`** in the bare convention and diverges to `∞` in the `♭` convention;
Paper 44 §8bis headlines *no rate* for exactly this reason. It is also `(m,n)`-dependent through
`P(m)∩P(n)`, so it does not cancel out of the form. **What survives:** the *vanishing* of an entry
(`L(m,n) = 0` off prime-power ratios) is convention-free, hence so are Theorem D.45.2(i) and the `−10`
witness of D.45.2(ii), which uses only zero entries and the degree term. **What does not survive:** every
numerical statement about a *nonzero* `L(m,n)`, `G(m,n)`, `deg c_{m,n}`, the `ℓ ≥ 7` threshold of
Corollary D.44.4, and the printed cosh margins — all are stated up to an unfixed positive factor. O-46.2 is
promoted from presentational to **MAJOR**. The one regime where this is harmless is the **single-prime
tower**, where `P(p^j)∩P(p^k) = {p}` for all `j,k`, so `c_N` is a *single common positive constant* and
every signature statement is unaffected: `R146_003` §D.47.]**

### D.44.1 Every entry but the diagonal is a count, and the form they reconstruct

**Lemma D.44.2 (the off-diagonal entries are Haar measures of fixed-point sets; `PROVED-IN-REPOSITORY`).**
Let `p` be a prime and `k ≥ 1`. The fixed-point set of `Frob_{p^k}` acting on `C_S` is the shell
`\{|x|_S = p^{−k}\}` intersected with the unit conditions of Definition 3ter.2, and its normalized Haar
measure in the Tate residue normalization is `\mathrm{vol}(Z_p^×)·p^{−k/2}·(\text{half-density weight})`, with
`\mathrm{vol}(Z_p^×) = \log p` **uniquely** fixed by Paper 44 Theorem 8bis.8. Hence

    ⟨Frob_{p^k}, Δ⟩ = Λ(p^k)\,p^{−k/2} = \mathrm{contact}_{fin}(Frob_{p^k})         (Thm 3ter.10, (3ter.10))

*exactly, with no limit and no regularization at the finite places*, and the general off-diagonal entry
`(146.2)` is `\min(m,n)` times the same measure at the ratio. **In particular every off-diagonal entry is a
nonnegative number produced by a measure of a nonempty fixed set, and it vanishes exactly when that set is
empty (`\max/\min` not a prime power, Theorem 3ter.4(i)'s coset description).** ∎ `PROVED-IN-REPOSITORY`
(Paper 44 Thm 3ter.10, Thm 8bis.8, Thm 8bis.1 + K1; nothing new is proved here).

**Remark D.44.2a (the diagonal is the only entry that is not a count, and it is not merely negative).**
`I_A(Frob_n,Frob_n)` **does not exist** (Paper 44 Remark 8bis.1c, `44/main.md:3542`: the Frobenius point
classes are multipliers, not elements of `D_A`; Corollary 8bis.1b′: the regularization parameters `(ε,N)`
cannot both be removed), and the diagonal of the ambient object is `Δ·Δ = −∞` at a fixed chart (Theorem
8bis.2, exempted from (C1)). The reason is visible already in the model and is *not* an arithmetic pathology:
the count interpretation of `\deg(α−β)` is `\#\ker(α−β)`, and at `α = β` this is `\#\ker(0) = \#E(\bar F_q) = ∞`.
**`\deg 0 = 0` is a convention, not a count, in the model too.** `RESTATEMENT` (of Rem 8bis.1c and Thm 8bis.2,
cited, not re-derived — `CORPUS_CHECK_R146b` §3).

**Theorem D.44.3 (Q0, arithmetic side: the Euler product determines the would-be norm form; `PROVED`).**
Fix a prime power `ℓ ≥ 2` and consider the rank-2 module `Z·Frob_1 ⊕ Z·Frob_ℓ` (`Frob_1 = Δ`, Thm 3ter.4).
The unique symmetric bilinear form on it whose off-diagonal is the count `(146.2)` and whose diagonal is
normalized by the model convention `δ ≡ 0` (§D.45.1) has quadratic form

    Q_ℓ(m,n) \;=\; m^2 + a_ℓ\,mn + ℓ\,n^2 ,\qquad
    \boxed{\,a_ℓ := ℓ + 1 − Λ(ℓ)\,} .                                                        (146.3)

This is the exact analogue of the model's `\deg(m+nπ) = m^2 + amn + qn^2` with `a = q+1−N_1`
(`R145_005` §2, `R145_004` Q0), under the dictionary

    q \;\longleftrightarrow\; ℓ ,\qquad N_1 \;\longleftrightarrow\; Λ(ℓ) = \log p \quad(ℓ = p^k) .   (146.4)

*Proof.* A symmetric bilinear form `B` on the module is determined by `B(1,1), B(1,ℓ), B(ℓ,ℓ)`. The model's
defining relation is `Γ_α·Γ_β = \deg(α−β) = q(α)+q(β)−2B(α,β)` with `q(·) = \deg`; imposing
`Γ_{Frob_1}·Γ_{Frob_ℓ} = L(1,ℓ) = Λ(ℓ)` and `\deg Frob_n = d_n = n` gives `2B(1,ℓ) = 1+ℓ−Λ(ℓ) = a_ℓ`, and
`δ ≡ 0` gives `B(n,n) = d_n = n`, i.e. `B(1,1) = 1`, `B(ℓ,ℓ) = ℓ`. Then
`Q_ℓ(m,n) = m^2B(1,1)+2mnB(1,ℓ)+n^2B(ℓ,ℓ)` is (146.3). Substituting `Λ(ℓ) ↦ N_1`, `ℓ ↦ q` returns the model's
form verbatim, which is D.44's claim that *the data is already there and only the interpretation is missing*. ∎
`PROVED` **[R2, M6 — LABEL DOWNGRADED to `DEFINITION`/`RESTATEMENT`.** The proof is the observation that
three numbers determine a symmetric `2×2` form; nothing is *determined* that was not put in. Worse, the
dictionary (146.4) is **over-determined and has no solution at a single prime**: matching
`q^{−|a−b|/2}N_{|a−b|}` against `Λ(max/min)(min/max)^{1/2}` forces `N_k ↔ Λ(ℓ^k) = log p` for *every*
`k ≥ 1`, whereas a genuine rank-2 order forces `N_2 = ℓ^2+1−(a_ℓ^2−2ℓ)`. At `ℓ = 2`: the order predicts
`N_2 = 3.6784`, the dictionary supplies `N_2 = log 2 = 0.6931`. There is no rank-2 order at any single
prime, *before* any Hasse test is run (`scripts/tower_gram.py` §[5]).]**

**Corollary D.44.4 (the reconstructed form is not positive, and the measured genus diverges; `PROVED`,
values `CERTIFIED` `scripts/cosh_test_cmn.py` §[2]).** `Q_ℓ` is positive definite iff `a_ℓ^2 ≤ 4ℓ`, the Hasse
bound in the dictionary (146.4). This holds **only for `ℓ ∈ \{2,3,5\}`** and fails for every prime power
`ℓ ≥ 7` (and for `ℓ = 4`). Quantitatively, since `Λ(ℓ) ≤ \log ℓ`,

    a_ℓ = ℓ+1−Λ(ℓ) ≥ ℓ+1−\log ℓ ,\qquad
    \frac{a_ℓ}{2\sqrt ℓ} \;≥\; \frac{ℓ+1−\log ℓ}{2\sqrt ℓ} \;=\; \tfrac12\sqrt ℓ\,(1+o(1)) \;\longrightarrow\; ∞ . (146.5)

Reading `|a| ≤ 2g\sqrt q` backwards, the **genus measured by the Euler product at `ℓ`** is
`g_ℓ ≥ a_ℓ/(2\sqrt ℓ) ~ ½\sqrt ℓ → ∞`: numerically `g_2 ≥ 0.816`, `g_5 ≥ 0.982`, `g_7 ≥ 1.144`,
`g_{101} ≥ 4.845`, `g_{1009} ≥ 15.79`.

*Proof.* Discriminant: `Q_ℓ ≻ 0 ⟺ a_ℓ^2 < 4ℓ` (and `⪰ 0 ⟺ ≤`). `a_ℓ ≥ ℓ+1−\log ℓ` and `(ℓ+1−\log ℓ)^2 > 4ℓ`
for `ℓ ≥ 7` (at `ℓ = 7`: `6.054^2 = 36.65 > 28`; the left side grows like `ℓ^2`, the right like `4ℓ`, and the
difference `(ℓ+1−\log ℓ)^2 − 4ℓ` is increasing for `ℓ ≥ 7` since its derivative is
`2(ℓ+1−\log ℓ)(1−1/ℓ) − 4 > 0` there). The three passing cases are the printed values
`(ℓ,a_ℓ^2,4ℓ) = (2,\,5.32,\,8),\ (3,\,8.42,\,12),\ (5,\,19.28,\,20)`, and `ℓ = 4` gives `18.55 > 16`. (146.5)
is immediate. ∎ `PROVED` **[R2, M6+M7+M8 — LABEL DOWNGRADED to `HEURISTIC`.** The numbers are certified
correct and reproduce exactly, but the statement is **not a theorem**: (a) it rests entirely on the
un-argued normalization `d_n := n`; with the round's own second arithmetic degree
`d_n = deg_det Sh_Z(Frob_n) = log n` one gets `a_ℓ = 1` for every prime and `a_ℓ^2 ≤ 4ℓ` holds
**everywhere** (`scripts/tower_gram.py` §[6]); (b) by M6 the data does not come from a curve, so
`g_ℓ := a_ℓ/(2√ℓ)` is not a genus (a genus is an integer; `g_2 = 0.816` bounds nothing) — it is the number
obtained by forcing `|a| ≤ 2g√q` backwards on data that has no `q`; (c) by M8 the threshold `ℓ ≥ 7` moves
with the chart constant. What survives is the elementary dimensional observation `Λ(ℓ) = log p ≪ ℓ`: the
arithmetic contact is logarithmic where the normalization `d_n = n` is linear.]**

> **[R2, M7 — the box below OVERCLAIMS; this sentence of it is WITHDRAWN:** *"This is the infinite genus in
> its **count** form … the first time in the corpus that `Δ·Δ = −∞` is exhibited as a *finite* statement
> about *finitely many* Euler factors."* Nothing in D.44.3–D.44.4 is derived from Theorem 8bis.2 and nothing
> implies it; the two are independent. `P46-40` and the README are re-worded accordingly.]**
>
> **What D.44.1 actually says, in one sentence.** *The Euler product does determine the would-be norm form,
> Q0 is answered **yes**, and the form it determines is **not** the norm form of a rank-2 order: the
> arithmetic "point count" `N_1 ↔ Λ(ℓ) = \log p` is **logarithmic** where the degree it must cancel is
> **linear**, so the trace `a_ℓ ≈ ℓ` overshoots the Hasse window `2\sqrt ℓ` by a factor `~½\sqrt ℓ`.* This is
> the infinite genus in its **count** form, measured prime by prime, and it is the first time in the corpus
> that `Δ·Δ = −∞` (Paper 44 Thm 8bis.2 — cited, not re-derived) is exhibited as a *finite* statement about
> *finitely many* Euler factors. `NEW` (`CORPUS_CHECK_R146b` items 2 and 4: the Gram entries exist, this
> reading of them does not).
>
> **This is a negative result and is exactly what W-a permits.** Nothing here asserts that any form *is*
> positive; the content is that the one form the Euler product hands us is *not*.

### D.44.2 The shadow's additive structure is rank 1, and that is rigid

**Definition D.44.5.** `Sh_Z(Frob_n) := [\,L_S \xrightarrow{\ n\ } L_S\,]` (Paper 44 Definition 6bis.1,
Lemma 6bis.2) with `\deg_{det}` of Definition 5.2: `\deg_{det}[Z \xrightarrow{m} Z] = \log\#(Z/m) = \log|m|`
for `m ≠ 0`, extended additively to finite complexes. Extend `n ↦ Sh_Z(Frob_n)` `Z`-linearly to
`Z[Frob] := Z⟨Frob_n⟩` by `Σ a_n Frob_n ↦ Σ a_n·n ∈ \mathrm{End}(L_S)`.

**[R2, M3+M4+M5 — Theorem D.44.6 is WITHDRAWN as stated and replaced by Statement D.44.6′ of `R146_003`
§D.48.** Clause (i) is **false at a finite chart**: `L_S = ∏_{p∈S_f}Z_p` (Paper 44 `main.md:405`), so
`[L_S : kL_S] = ∏_{p∈S_f}|k|_p^{−1}` is the **`S`-part** of `|k|`, equal to `|k|` only when every prime
factor of `k` lies in `S_f` — true for `k = n` in `Frob_n` (Definition 3ter.2 requires `P(n) ⊆ S_f`) but
**false in general for `k = m+nℓ`**. Clause (ii)'s proof is false: `L_S` is not a rank-1 `Z`-module,
`End(L_S) ⊇ ∏_{p∈S_f}Z_p` is enormous and **does** contain rank-2 orders; the only true content is that
`Sh_Z`, *as defined*, sends `Frob_n ↦ n ∈ Z`, which names a definition rather than proving rigidity. Clause
(iii) is a **non-sequitur**: the model's trace is that of a *single* Frobenius, the round's own D.44.3
supplies a finite per-prime candidate `a_ℓ`, and divergence of `Σ_pΛ(p)p^{−1/2}` is a different quantity.
The theorem is left below only as the record of what was withdrawn.]**

**Theorem D.44.6 (the shadow's degree is a genuine count, and it is rank 1) — `WITHDRAWN`, see above.**

 (i) `\deg_{det}Sh_Z(m + n·Frob_ℓ) = \log|m+nℓ| = \log\#\big(L_S/(m+nℓ)L_S\big)` whenever `m+nℓ ≠ 0` — a
     cardinality of a finite abelian group, hence **nonnegative by construction**, and additive under
     composition: `\deg_{det}Sh_Z(Frob_m ⋆ Frob_n) = \log(mn) = \log m + \log n` (Paper 44 (6bis.4),
     Corollary 5.3a's ghost relation `\log n = Σ_{d|n}Λ(d)`).
 (ii) **Rigidity.** `L_S` is a rank-1 `Z`-module inside `X_S`, so `\mathrm{End}_Z(L_S) = Z`; therefore the
     only ring homomorphism `Z[Frob] → \mathrm{End}(L_S)` compatible with `Sh_Z` is `Frob_n ↦ n`, and the
     only additive structure the shadow sees is the rank-1 one. Its associated "norm form" is
     `(m,n) ↦ \log|m+nℓ|`, which is **not quadratic** and whose `Z`-bilinear companion is the rank-1
     degenerate form `(m+nℓ)(m'+n'ℓ)`: it has an isotropic sublattice of corank 1 (`m+nℓ = 0`) and therefore
     carries **no signature information whatever**.
 (iii) **What a rank-2 structure would require, and why it is unavailable.** A rank-2 order `Z[π]` inside
     `\mathrm{End}` requires a single **finite** invariant `a = \mathrm{tr}(π)` satisfying `π^2 − aπ + q = 0`.
     Over `Spec Z` the only candidate trace assembled from the pairing data is the total Frobenius contact
     `Σ_p ⟨Frob_p,Δ⟩ = Σ_p Λ(p)p^{−1/2} = Σ_p \frac{\log p}{\sqrt p}`, which **diverges** (by Mertens /
     Chebyshev, `Σ_{p ≤ x}\log p ~ x`, so `Σ_{p≤x}\log p\,p^{−1/2} ≫ \sqrt x`). There is no finite trace,
     hence no rank-2 order, hence no `Z[π]`. `PROVED`

*Proof.* (i) is Definition 5.2 with `H^0Sh_Z(Frob_n) = L_S/nL_S ≅ Z/n` (Theorem 6bis.3(i)) and
`\deg_{det}Sh_Z(Frob_n) = \log n` ((6bis.4)); the linear extension sends `m+nFrob_ℓ` to multiplication by
`m+nℓ`, whose cokernel is `Z/(m+nℓ)`. (ii) An endomorphism of a rank-1 free `Z`-module is multiplication by
an integer; `Sh_Z(Frob_n) = [n]` fixes the image of each generator, and a ring map out of a free `Z`-module
on the `Frob_n` is determined by its values on generators. Degeneracy: `\log|m+nℓ|` depends on `(m,n)` only
through `m+nℓ`. (iii) as shown; divergence is Chebyshev. ∎ `PROVED`

> **[R2: the reading below survives only in its first half — the shadow's count is real but **partial**
> (the `S`-part), and "rank 1" is a property of `Sh_Z`'s definition, not of `End(L_S)`.]**
>
> **Reading.** The shadow gives what the blueprint asked for — *an object whose degree is a cardinality* —
> and it gives it **unconditionally and with the right sign**. What it does not give is a *form*: rank 1
> means one direction, no `(1,1)` plane, no Hodge index, nothing for RH to be about. This is the exact
> shape of the corpus's recurring finding (`R140_001` D.23.12(iv): "(C) is a third object and it carries
> neither"; phase 136's meta-theorem: *no object does all three*). `NEW` as a rigidity statement
> (`CORPUS_CHECK_R146b` §1).

### D.44.3 The two degrees of `Frob_n`, and the infinite-genus identity

**Restatement D.44.7 (`RESTATEMENT`; every ingredient `PROVED-IN-REPOSITORY`).** The Frobenius carries two
degrees, and they are the `H^0/H^2` datum and the `H^1` datum:

| | value | finite? | what it is |
|---|---|---|---|
| `\deg_{det}Sh_Z(Frob_n)` | `\log n` | yes | the bidegree/`H^0`-`H^2` datum; `M(Frob_n) = (n^{1/2},n^{−1/2})`, Paper 44 Thm 3ter.6(iii) |
| `⟨Frob_n,Frob_n⟩` | `−∞` / does not exist | **no** | the `H^1`-type self-intersection; Paper 44 Thm 8bis.2, Rem 8bis.1c |

In the model the two are related by adjunction: `Γ_{π^a}·Γ_{π^a} = q^a(2−2g) = (\deg π^a)·χ_{top}(C)`
(`R145_001` D.41.4 with `κ(0) = N_0 = 2−2g = χ_{top}(C)`). The arithmetic identity is therefore

    ⟨Frob_n,Frob_n⟩ \;=\; d_n·(2−2g) \;=\; n·(2−2g),\qquad 2−2g = −∞ ,                       (146.6)

**[R2, M1 — (146.6) IS WITHDRAWN as an arithmetic statement and RELABELLED `HEURISTIC` (the model's formula,
transported).** Adjunction is a theorem about a smooth projective surface and is **not available on
`Spec Z`**; and the round's own cited source *computes* the Frobenius diagonal and contradicts the
transported formula. Paper 44 **Theorem 8bis.1b** gives, exactly and for every `N ≥ 1`,
`Σ_q W_q(Δ^{(n),[φ_ε,N]}) = −Σ_{r∈S_f∖P(n)}(log r)[(r−2)/(r−1)+(N−1)]`, and `W_∞ = −log(1/ε)+O(1)`
**independent of `n`**: the `n`-dependence runs through **`P(n)` only**, not through `n`, and nothing is
proportional to `d_n`. The correct treatment of the diagonal, and the exact value of `δ_m − δ_n`, is
`R146_003` §D.47. The table above (the two degrees; `Δ·Δ = −∞` as a cited fact) is **sustained**; only
(146.6)'s arithmetic half falls.]**

and the precise meaning of `g = ∞` is: **the `H^1` of row D's surface is infinite-dimensional, and Paper 46
Proposition 14.2 exhibits the basis** — `τ_{\log n}(ΠK) ∈ 𝓝_∞` for every `n`, and these classes are
`R`-linearly independent (Thm 13.5(i)), so *the principal classes of row D's surface are indexed by the
Frobenius family itself*. The divergence in (146.6) is the divergence of the zero sum, i.e. of
`\#\{ρ\} = ∞`; it is the same fact as Corollary D.44.4's `g_ℓ → ∞`, read in the limit instead of prime by
prime. `RESTATEMENT` (nothing re-derived: Thm 8bis.2, Rem 8bis.1c, Prop 14.2 cited).

---

## D.45 — Q1: does `M := Z⟨Frob_n⟩` admit a finite, symmetric degree form?

### D.45.1 The difference-only form, and the diagonal counterterm

**Theorem D.45.1 (Q1, the existence half; `PROVED`).** Define, for `m ≠ n`,

    ⟨⟨Frob_m, Frob_n⟩⟩ \;:=\; \text{"}\deg(Frob_m − Frob_n)\text{"} \;:=\; L(m,n)                (146.7)

— the Haar measure of the fixed-point set of `Frob_m ⋆ Frob_n^† = Frob_{m/n}` (Lemma D.44.2; Paper 44's
inverse-semigroup law, Thm 3ter.4/3ter.7, with the transposes when `n \nmid m`), a **finite, nonnegative**
number, and let `δ_n := L(n,n)` be a real counterterm. Then there is **exactly one** symmetric bilinear form
`B_δ` on `M` with `B_δ(Frob_m,Frob_n) = ½(d_m + d_n − L(m,n))` for all `m,n`, namely

    B_δ(x,y) = Σ_{m,n} a_m b_n\,G(m,n),\quad G(m,n) := \tfrac12\big(m+n−L(m,n)\big) ,
    Q_δ(x) := B_δ(x,x) = \Big(Σ_n a_n\Big)\Big(Σ_n a_n n\Big) \;-\; \tfrac12\,Σ_{m,n}a_ma_nL(m,n) .   (146.8)

It is **finite and symmetric for every finite choice of `(δ_n)`**, it **extends Paper 44 Theorem 3ter.10's
off-diagonal weights** (by (146.2)/(146.4)) **[R2, M10: misleading — the entries are
`G(m,n) = ½(m+n−L(m,n))`, dominated by the degree term, with `Λ` entering as an `O(log)` correction to an
`O(m+n)` entry]**, and it agrees with `I_∞` on differences in the only sense available **[R2, M9 — blueprint
item (i) is NOT DISCHARGED and the stronger reading is FALSE: by Paper 46 (11.6), for `x = E_m − E_n` one
has `Φ_x(0) = 0`, `Φ_x(1) = m−n`, hence `I_∞(x,x) = −W(x)`, of the **opposite** sign to
`B_0(x,x) = L(m,n) ≥ 0`. What agrees with Gram (A) is the *off-diagonal entry*, a weaker statement]**: on `Frob_m − Frob_n` it returns `L(m,n)`, which is exactly the Gram entry (A) of `R140_001`
Theorem D.23.12 — the *smeared Frobenius* Gram, **not** the Pólya realization (whose `Z` vanishes
identically, `R140_001` D.23.12(C); the blueprint's standing warning is respected: no pairing below uses
`r(Frob_n) = τ_{\log n}(2K)`).

*Proof.* A symmetric form is determined by its values on pairs of generators; the relation
`Γ_α·Γ_β = q(α)+q(β)−2B(α,β)` with `q(Frob_n) = d_n = n` and `Γ_{Frob_m}·Γ_{Frob_n} = L(m,n)` determines
`B(Frob_m,Frob_n) = G(m,n)`, and bilinear extension is the unique extension. (146.8): expand,
`Σ_{m,n}a_ma_n·½(m+n) = (Σ a_n)(Σ a_n n)`. Finiteness: every element of `M` is a finite `Z`-combination.
∎ `PROVED`

> **[R2, M10 — the structural identity that should have been stated, and that governs the whole round.**
> By (146.12), `Φ_x(0) = Σa_n` and `Φ_x(1) = Σa_n n`, so (146.8) reads
>
>     Q_0(x) = Φ_x(0)·Φ_x(1) − ½ x^T L x ,
>
> i.e. **Paper 46's comparison identity `I_∞ = 2Φ(0)Φ(1) − W` with the zero sum `W` deleted and replaced by
> the finite Gram `L`** (up to the factor `½`). Three consequences: (a) the form contains **no zero data by
> construction**, the real and much stronger reason for Theorem D.45.7's non-detection; (b) **every
> statement of §§D.44–D.45 is `Ξ_a`-uniform**, not only Theorem D.45.8 — Paper 46 `main.md:2274` records
> that §11 holds verbatim for `Ξ_a`; (c) indefiniteness is immediate, a product of two independent linear
> functionals having signature `(1,1)`.]**

**So the answer to Q1's literal question is YES** — *a finite, symmetric form exists, and it is unique once
the diagonal is chosen.* The content of the round is what happens next.

**Theorem D.45.2 (Q1, the substantive half: the form is not a count, two independent obstructions;
`PROVED`, witnesses `CERTIFIED` `scripts/cosh_test_cmn.py` §[3]).** With the model's convention `δ ≡ 0`:

 (i) **Degeneracy against the count axiom.** In any genuine degree form, `\deg(α−β) = 0 ⟺ α = β`
     (`#\ker` of a nonzero isogeny is finite and nonzero, and vanishes only for the zero map). Arithmetically
     `L(m,n) = 0` **whenever `\max/\min` is not a prime power** (Lemma D.44.2), while `Frob_m ≠ Frob_n`
     (the object determines `n`: Paper 44 Thm 3ter.4(iv)). E.g. `L(6,10) = 0`, `L(15,22) = 0`. So `(146.7)`
     is **not** the degree of a difference: the "isogeny" `Frob_6 − Frob_{10}` would have degree `0` without
     being zero.
 (ii) **Indefiniteness, with an explicit integral witness.** On the sublattice `Z·Frob_6 ⊕ Z·Frob_{10}`,
     where `L ≡ 0`, (146.8) reads `Q_0(a,b) = (a+b)(6a+10b)`, a form of signature `(1,1)`. Hence

          Q_0\big(5\,Frob_6 − 4\,Frob_{10}\big) = (5−4)(30−40) = -10 \;<\; 0 .                  (146.9)

     More generally `Q_0` is indefinite on **every** pair `\{m,n\}` whose ratio is not a prime power, since
     `(a+b)(ma+nb)` has discriminant `(m+n)^2 − 4mn = (m−n)^2 > 0`. The scan of §[3] returns
     `\min Q_0 = −2088` at `(m,n,a,b) = (1,60,−12,6)`.
 (iii) Consequently **`Q_0` is not `#\ker` of anything**: a cardinality cannot be `−10`.

**[R2, M13 — the content is lower than advertised, and the one-line proof should have been the headline.**
`Q_0(x) = Φ_x(0)Φ_x(1) − ½x^TLx`: the first term is a **product of two independent linear functionals**,
hence of signature `(1,1)` on any span where they are independent — indefiniteness needs no witness, no scan
and no `6/10` degeneracy. On a pair `{m,n}` the determinant is `mn−(m+n−L)^2/4`, which is **exactly**
Corollary D.44.4's Hasse discriminant: D.44.4 and D.45.2(ii) are the *same* computation, not two. The
witnesses `(6,10)`, `(15,22)`, `(1,60)` moreover live in the multi-prime region, where the model (a single
`π`) supplies no counterpart at all. **What survives, and is robust:** indefiniteness is
normalization-independent — with `d_n = log n` the same witness gives `Q_0 = −0.2515 < 0`
(`scripts/tower_gram.py` §[7]) — and the `L(m,n) = 0` degeneracy of (i) is convention-free (M8).]**

*Proof.* (i) is Lemma D.44.2's vanishing criterion against Theorem 3ter.4(iv). (ii) `L(6,10) = 0` because
`10/6 = 5/3` is not a prime power; substitute into (146.8). The general statement: `(a+b)(ma+nb)` has matrix
`\begin{psmallmatrix} m & (m+n)/2\\ (m+n)/2 & n\end{psmallmatrix}` with determinant `mn − (m+n)^2/4 =
−(m−n)^2/4 < 0`. (iii) immediate. ∎ `PROVED`

### D.45.1a The counterterm's sign — the deliverable, and the STOP

The only freedom left in (146.8) is `(δ_n)`, and it enters as `Q_δ(x) = Q_0(x) − ½Σ_n a_n^2 δ_n`. So:

> **Statement D.45.3 (the exact location of the sign; `PROVED` as an equivalence of problems, and
> `DO-NOT-ATTEMPT`).**
> 1. *A finite counterterm can repair any single witness.* On `Z·Frob_6 ⊕ Z·Frob_{10}`, `Q_δ ⪰ 0` iff
>    `(6−δ_6/2)(10−δ_{10}/2) ≥ 64`, which finite negative `δ` satisfy. So no **local** obstruction exists,
>    and the phase-141 verdict ("indefinite at trace level", `CORPUS_CHECK_R146b` §4) is not improved on by
>    exhibiting more witnesses.
> **[R2, M12: the equivalence asserted in item 2 is NOT ESTABLISHED. Proposition D.42.5 is about a closed,
> `𝓝_∞`-saturated cone `𝔈 ⊇ 𝓔` carrying the degree gate (4b); it does not say that `Q_δ ⪰ 0` on
> `Z⟨Frob_n⟩` is RH, and no such reduction is given anywhere. The prohibition (**do not attempt**) is
> endorsed and kept; the *label* becomes `OPEN, suspected RH-equivalent, not proved so`, and `P46-41` must
> not go to a paper carrying "fixing it positively is RH".]**
> 2. *Choosing `(δ_n)` so that `Q_δ ⪰ 0` on all of `M` is suspected to be Weil positivity.* By Proposition D.42.5
>    (`R145_001` §D.42.4) and by `R144`'s family `tF+dK`, positive semidefiniteness of the degree form on
>    the Frobenius lattice is RH. **This round therefore does not attempt it, does not conjecture it, and
>    records that any later round which "proves" it has either proved RH or made an error.** (W-a.)
> 3. **[R2, M1 — WITHDRAWN in its entirety.** Round 1 wrote: *"adjunction (146.6) forces
>    `δ_n = d_n(2−2g) = n(2−2g)`, and `2−2g = −∞`, i.e. `δ_n = −∞` … the infinite genus is precisely the
>    counterterm that would make the form positive."* Adjunction is unavailable arithmetically, and Paper 44
>    Thm 8bis.1b **computes** the diagonal: at a fixed chart it is a **finite negative** number whose
>    `n`-dependence runs through `P(n)` only, with a finite-place divergence **linear in `N`** and an
>    archimedean divergence `−log(1/ε)` that is **independent of `n`**. The replacement — the exact value of
>    `δ_m − δ_n` and the single-prime tower, where the diagonal is constant and the form is therefore well
>    defined up to one constant — is `R146_003` §D.47.]**
> 4. *`g = 1` hides all of this* (W-b): there `2−2g = 0`, so `δ ≡ 0` **is** the arithmetic value, the
>    convention and the truth coincide, and the entire question is invisible. This is a second, independent
>    sense in which the elliptic model cannot be used as a guide here, beyond `\mathrm{rk\,End} = 2g`.

**Answer to Q1, formally.** *Yes*, a finite symmetric form extending the `Λ(n)n^{−1/2}` weights exists, and it
is unique given the diagonal; *no*, it is not a degree form and not a count — it is degenerate against the
count axiom (D.45.2(i)) and indefinite (D.45.2(ii)) at the model's own diagonal convention, and at the
arithmetic diagonal it does not exist at all (D.45.3(3)). **α is therefore not dead in the way the trace cone
was — the object exists — but it is dead as a *count*, which is what the blueprint asked for.**

### D.45.2 The sum classes: the model identity, `Γ_{1+π}`, and the cosh test

**Theorem D.45.4 (the class map is additive; the model; `PROVED`).** Let `E/F_q` be elliptic,
`F_1 = \{O\}×E`, `F_2 = E×\{O\}`, `Γ_φ` the graph of `φ ∈ \mathrm{End}(E)`. Then in `NS(E×E)`

    [Γ_{φ+ψ}] \;=\; [Γ_φ] + [Γ_ψ] − F_2 + 2⟨φ,ψ⟩\,F_1 ,\qquad
    ⟨φ,ψ⟩ := \tfrac12\big(\deg(φ+ψ)−\deg φ−\deg ψ\big) ,                                     (146.10)

equivalently: `c(φ) := [Γ_φ] − (\deg φ)F_1 − F_2` is additive, `c(φ+ψ) = c(φ)+c(ψ)`.

*Proof (by numerical equivalence; no theorem of the cube needed).* `NS(E×E)_R` is spanned by `F_1,F_2` and
the graphs (`R145_005` §2), so it suffices to pair both sides with `F_1, F_2, Γ_χ`. Using `F_i^2 = 0`,
`F_1F_2 = 1`, `Γ_φ·F_1 = 1`, `Γ_φ·F_2 = \deg φ`, `Γ_φ·Γ_ψ = \deg(φ−ψ)`, and writing `q(·) = \deg` for the
quadratic form with polarization `⟨·,·⟩`:
 `·F_1`: `1 = 1+1−1+0` ✓. `·F_2`: `\deg(φ+ψ) = \deg φ+\deg ψ+2⟨φ,ψ⟩` ✓ (definition of `⟨,⟩`).
 `·Γ_χ`: LHS `= q(φ+ψ−χ) = q(φ)+q(ψ)+q(χ)+2⟨φ,ψ⟩−2⟨φ,χ⟩−2⟨ψ,χ⟩`; RHS
 `= [q(φ)+q(χ)−2⟨φ,χ⟩]+[q(ψ)+q(χ)−2⟨ψ,χ⟩]−q(χ)+2⟨φ,ψ⟩` — equal. The two sides are numerically equivalent,
 hence equal in `NS`. The `c`-form follows by rearranging. ∎ `PROVED`

**Corollary D.45.5 (`Γ_{1+π}` has negative coefficients in the frame's basis; `PROVED`).** With `φ = 1`
(so `Γ_1 = Δ`), `ψ = π`, `2⟨1,π⟩ = \deg(1+π)−1−q = a`:

    [Γ_{1+π}] \;=\; Δ + Γ_π − F_2 + a\,F_1 .                                                  (146.11)

For the phase-145 curve of record `E/F_2 : y^2+xy = x^3+1` (`q = 2`, `N_1 = 4`, `a = q+1−N_1 = −1`):

    [Γ_{1+π}] = Δ + Γ_π − F_2 − F_1 ,

**two** negative coefficients in the frame's basis `\{F_1,F_2,Γ_{π^n}\}`. Checks: `·F_1 = 1+1−1−0 = 1` ✓,
`·F_2 = 1+2−0−1 = 2 = \deg(1+π) = 1+a+q` ✓, self-intersection
`2[Δ·Γ_π − Δ·F_2 − Δ·F_1 − Γ_π·F_2 − Γ_π·F_1 + F_1F_2] = 2[4−1−1−2−1+1] = 0 = Γ^2` ✓ (`g = 1`).
`Γ_{1+π}` is an irreducible curve — **effective** — yet it is **not** in `𝓔_C = \mathrm{Cone}\{Γ_{π^n},Γ_{π^n}^t\}`
(`R145_001` D.42.1 `[X]`): it is exactly one of the "missing effective classes" named in `R145_005` §2. ∎
`PROVED`

**Definition D.45.6 (the arithmetic would-be sum classes).** Transport (146.10) through the dictionary. In
`D^W`, `F_1 = K+K_{odd}`, `F_2 = K−K_{odd}` with `M(F_1) = (1,0)`, `M(F_2) = (0,1)` (`R140_001` D.23.7), so
`I_∞(E,F_1) = Φ_E(0)`, `I_∞(E,F_2) = Φ_E(1)`: `F_2` is the *degree* ruling (`Γ_φ·F_2 = \deg φ`) and `F_1` the
*unit* ruling (`Γ_φ·F_1 = 1`), matching `R145_001` D.41.6(iii). Let `E_n ∈ D^W` be the **un-normalized smeared
Frobenius**: for `ε > 0` and even `φ ≥ 0` of mass 1,
`E_n^{(ε)}(u) := n^{1/2}ε^{−1}φ((u−\log n)/ε) ≥ 0`, so that in the limit `ε ↓ 0`

    Φ_{E_n}(s) = n^{s},\quad M(E_n) = (n,1),\quad \deg E_n = n+1,\quad Φ_{E_n}(ρ) = n^{ρ} .   (146.12)

(This is Paper 44 §8bis's smeared Frobenius of unit-height profile, in the un-normalized (146.1); it is
**effective**, `E_n ≥ 0`, and it is not the Pólya class.) Define, with `G(m,n)` from (146.8),

    c_{m,n} \;:=\; E_m + E_n − F_2 + 2G(m,n)\,F_1 ,                                            (146.13)
    \deg c_{m,n} = (m+1)+(n+1)−1+2G(m,n) = 2(m+n)+1−L(m,n) ,\qquad
    Φ_{c_{m,n}}(ρ) = m^{ρ}+n^{ρ} .

Every intersection number of `c_{m,n}` is forced: `I_∞(c,F_1) = Φ_c(0) = 1+1−0+2G·0 = 2−1+…` — concretely
`M(c_{m,n}) = (m+n−1+2G(m,n),\,1)`, `\deg` as printed, and the zero data is carried **by the Frobenius terms
alone**, because `Φ_K = ξ` and `Φ_{K_{odd}}(s) = \frac{\sinh((s−½)a_0)}{\sinh(a_0/2)}ξ(s)` both vanish at
every zero (Paper 46 Thm 11.8(i); `R138_001` Def. D.15.1b). **The rulings are invisible at the zeros.**

**Theorem D.45.7 (the cosh test on `c_{m,n}`: it passes, for every pair, and it is non-detecting; `PROVED`;
margins `CERTIFIED` `scripts/cosh_test_cmn.py` §[1]).** Let `ρ_1 = ½+iγ_1` and `s(γ,θ)` as in `R142_001`
Definition D.31.3. Then:

 (i) `0.99845 ≤ s(γ_1,θ) ≤ 1` for **every** `θ`. *Proof:* the upper bound is `|\cos| ≤ 1 ≤ \cosh`; for the
     lower, choose `u_0` with `γ_1u_0+θ ∈ πZ` and `|u_0| ≤ π/(2γ_1) < 0.1112`, so
     `s(γ_1,θ) ≥ 1/\cosh(u_0/2) ≥ 1/\cosh(0.0556) > 0.99845`. ∎
 (ii) For all `m,n ≥ 1`, `\max_θ\big[|\mathrm{Re}(e^{iθ}Φ_{c_{m,n}}(ρ_1))| − ½s(γ_1,θ)\deg c_{m,n}\big] < 0`:
     the cosh test **passes**, so Lemma D.31.4 does **not** refute effectivity of `c_{m,n}` for any pair.
     *Proof:* `|Φ_{c}(ρ_1)| ≤ \sqrt m+\sqrt n`, and by (i) the right-hand side is
     `≥ ½(0.99845)\deg c = 0.4992\,(2(m+n)+1−L(m,n))`. Write `\max = t·\min`, `t ≥ 1`; then
     `L ≤ \min·\log t` and `2(m+n)−L ≥ \min(2+2t−\log t) ≥ 1.5\,\min(1+t) = 1.5(m+n)` for all `t ≥ 1`
     (since `2+2t−\log t ≥ 1.5(1+t) ⟺ 0.5+0.5t ≥ \log t`, true for every `t > 0`). Hence the bound is
     `≥ 0.4992·1.5(m+n) = 0.7488(m+n) > \sqrt m+\sqrt n` for all `m,n ≥ 1` (at `m = n = 1`:
     `1.4976 > 2`? no — check the two small cases separately: `(1,1)`: `\deg c = 5`, bound `2.496 > |Φ| = 2`;
     `(1,2)`: `\deg c = 6.307`, bound `3.148 > |Φ| = 0.605`; for `m+n ≥ 4` one has
     `0.7488(m+n) ≥ \sqrt m+\sqrt n` since `\sqrt m+\sqrt n ≤ \sqrt{2(m+n)}` and
     `0.7488\sqrt{m+n} ≥ \sqrt 2 ⟺ m+n ≥ 3.57`). ∎ **[R2, m5: the parenthetical above contains a visible false start
     (`"at m=n=1: 1.4976 > 2? no —"`), repaired two clauses later; the clean statement is that `(1,1)` and
     `(1,2)` are checked directly (margins `−0.4998`, `−2.5456`) and `m+n ≥ 4` is covered by
     `√m+√n ≤ √(2(m+n))`.]**
 (iii) Computed margins (negative = passes), `--fast`:

    (m,n)   |Φ(ρ_1)|   deg c    2G      margin
    (1,1)    2.0000     5.000   2.000   −0.4998   (the tightest pair)
    (1,2)    0.6047     6.307   2.307   −2.5456
    (2,3)    3.0284    11.000   5.000   −2.4700
    (1,3)    0.7691     7.901   2.901   −3.1798
    (1,5)    1.6588    11.391   4.391   −4.0299
    (1,7)    2.0492    15.054   6.054   −5.4697
    (2,4)    0.8552    11.614   4.614   −4.9426
    (3,9)    1.3321    21.704   8.704   −9.5138
    (1,101)  9.3358   200.385  97.385  −90.7794
    (6,10)   5.0172    33.000  16.000  −11.4728

> **[R2, M10 — the reason given below is correct but weaker than the true one.** Lemma D.31.4 is a
> **tautology** on this family: `c_{m,n}` is `Φ`-identical to the manifestly effective class `E_m+E_n` while
> carrying strictly *more* degree, so no nonnegativity test reading only `(Φ(ρ), deg)` can ever fire on it.
> Underneath that, the form `Q_0 = Φ(0)Φ(1) − ½x^TLx` contains no zero data at all, and the non-detection —
> like everything else in §§D.44–D.45 — is `Ξ_a`-uniform.]**
>
> **The finding, and it is not the one the blueprint's first branch anticipated.** The cosh test does not
> fail for any pair — **and the reason it cannot fail is structural, not numerical**: by Definition D.45.6
> the entire additive correction `−F_2 + 2G(m,n)F_1` lives in the **ruling plane**, which has `Φ ≡ 0` at
> every zero (Paper 46 Thm 11.8(i)), while it inflates the degree by `2G(m,n) ≈ m+n`. So the test compares
> a zero-datum of size `O(\sqrt m+\sqrt n)` against a degree of size `≈ 2(m+n)`: it is **non-detecting on
> this family by construction**. This is the same collapse `R140_001` §D.23.3bis recorded for the Pólya
> realization, arriving here from the other side: *the additive structure is entirely a ruling-plane
> phenomenon, and the zeros do not see it.* The general case is therefore **not OPEN** — it is proved to
> pass, and proved to be uninformative. `PROVED` / `NEW` (the non-detection statement).
>
> **Corollary (the shape a genuine object would need).** Any object realizing `Γ_{Frob_m+Frob_n}` with
> content at the zeros must have `Φ(ρ) ≠ m^{ρ}+n^{ρ}` — i.e. it must **not** be supported on shifted
> diagonals of the radial line. It would have to be a class on `C_S × C_S` in two genuinely independent
> variables, whose restriction to the radial diagonal is `E_m+E_n` and whose off-diagonal part carries the
> `2⟨φ,ψ⟩` correction with nonzero zero data. Constraint P122.028 applies to it verbatim: nothing
> expressible in `\log p, p^{−½}, N, Γ` alone can carry the sign, and `2G(m,n) = ½(m+n−L(m,n))` is
> expressible in exactly those symbols — **so the correction term as defined is, by P122.028, barred as an
> independent input for the sign, independently of the cosh test.** `PROVED` (given P122.028 as cited).
> **[R2, m2: round 1 wrote "incapable of carrying the sign" and "refutes"; P122.028 is a gate on citing a
> magnitude-only relation as the independent input, not a refutation. Verb weakened.]**

### D.45.3 What `m + n·Frob_ℓ` could mean on `C_S`: only the formal thing

**Theorem D.45.8 (no sum of correspondences is realized as a correspondence; `PROVED`).** Let `C_S` be the
idele class group with its Frobenius action, and let `ψ : C_S → C_S` be a continuous group endomorphism
whose graph carries a Lefschetz/explicit formula for `ξ` (i.e. whose fixed-point count is computed by the
zero sum `Σ_ρ Φ(ρ)` of the same zero set). Then `ψ(x) = ℓ·x` for some `ℓ`, i.e. `ψ` is a **Frobenius
translation** `Frob_ℓ` — and in particular:

 (i) the endomorphisms of `C_S` are the power maps `x ↦ x^k` composed with translations, with graphs
     `\{t' = kt + \log ℓ\}` in the square (slope `k`), acting on characters by `s ↦ ks`;
 (ii) for `k ≠ 1` the zero set is **not** preserved: the pushforward of `\{ρ\}` under `s ↦ ks` has counting
     function `N(T/k) ~ \frac{T}{2πk}\log\frac{T}{k}`, while `N(T) ~ \frac{T}{2π}\log T` (Riemann–von
     Mangoldt, `CLASSICAL`); the two densities differ by the factor `k` in the leading term, so no bijection
     of the two multisets exists and no Lefschetz formula with `ξ` holds for `k ≠ 1`;
 (iii) hence the only available composition law is `Frob_m ⋆ Frob_n = Frob_{mn}` (Paper 44 Thm 3ter.4), and
     **the only additive structure on Frobenius correspondences compatible with the Lefschetz/explicit
     formula is the formal one**: `Z⟨Frob_n⟩` with the bilinear extension (146.8). There is no "sum of
     correspondences realized as a single correspondence" on `C_S`.
 (iv) The model's `m+nπ` is **not** of this form: it is `x ↦ [m]x + π(x)` using the **group law of `E`**,
     which is a second, independent group structure on the curve. On `C_S` the group law is already spent —
     it is the one the Frobenius translations act by — so there is no second addition to form `m+nFrob`
     with.

**[R2, M11 — LABEL DOWNGRADED to `CLAIM` (partially proved).** Clause (ii) (Riemann–von Mangoldt density
against `s ↦ ks`) is correct and is the only proved part. Clause (i) is **asserted**: "the classification of
continuous endomorphisms of the idele class group" is stated as if it were a citation, is not proved here,
and is not true as literally written (`C_Q ≅ R_{>0}×\hat Z^×` has a large continuous endomorphism monoid; on
the modulus line alone the continuous endomorphisms are `x ↦ λx`, `λ ∈ R`). Clause (iii)'s "a sum of
translations is not a translation" is a tautology excluding only realizations *inside* the translation
family. The `Ξ_a`-verbatim check below, and its conclusion "**A3 does not enter here**", are **sustained** —
and by M10 they now apply to the whole of §§D.44–D.45, not only to this theorem.]**

*Proof.* (i) is the classification of continuous endomorphisms of the idele class group modulo the Frobenius
flow (the affine maps `x ↦ ℓx^k`); on characters `s` these act by `s ↦ ks`. (ii) as shown, by Riemann–von
Mangoldt. (iii) `k = 1` leaves translations, whose composition is multiplication of the moduli; the
`Z`-module generated by them has no realization of `Σ a_nFrob_n` as a single self-map because a sum of
translations is not a translation. (iv) as stated. ∎ `PROVED`

> **Falsifier check (`Ξ_a`), and it is decisive for where A3 does *not* enter.** Theorem D.45.8's proof uses
> only the group law of the modulus line and a zero-counting density — both of which `Ξ_a` has (`R140_001`
> Theorem D.23.5(i): `τ_{\log m}τ_{\log n} = τ_{\log mn}` is the group law of `R`, *which `Ξ_a` also has*).
> So Theorem D.45.8 holds **verbatim for `Ξ_a`**: the absence of a realized additive structure is **not** a
> property that separates `ξ` from the falsifier, and **A3 does not enter here**. Recorded, as the blueprint
> requires. `PROVED`. (`Ξ_Q`: the additive structure is unavailable there for a stronger reason — with no
> Euler product there are no `Frob_n` to add, so `M` is not even defined; the falsifier is passed trivially
> and is uninformative. `ζ_K`: every statement of §D.44–§D.45 is uniform in the number field, with `Λ(n)`
> replaced by `Λ_K(\mathfrak n)` and `n` by `N\mathfrak n`; Corollary D.44.4's failure threshold moves but
> the asymptotic `g ≳ ½\sqrt{N\mathfrak p}` is unchanged.)

### D.45.4 The count that does exist

**Theorem D.45.9 (degree is a count on monomials and on differences, never on sums; `PROVED`).** On
`M = Z⟨Frob_n⟩`:

 (i) **Monomials.** `\deg_{det}Sh_Z(Frob_m ⋆ Frob_n) = \log(mn) = \log\#(L_S/mnL_S)` — a cardinality
     (D.44.6(i)); and the fixed-point set of `Frob_{p^k}` on `C_S` is the shell `|x|_p = p^{−k}` with Haar
     measure `\log p` (Lemma D.44.2) — a measure of a nonempty set.
 (ii) **Differences.** `⟨⟨Frob_m,Frob_n⟩⟩ = L(m,n)` is the fixed-point measure of the **composition**
     `Frob_m ⋆ Frob_n^†` (`= Frob_{m/n}` when `n | m`, a transpose otherwise), which is a genuine object of
     the inverse semigroup (Paper 44 Thm 3ter.4, Thm 3ter.7): finite, `≥ 0`, computed by a measure.
 (iii) **Sums.** A formal sum `Σ a_nFrob_n` is **not a self-map of `C_S`** (Theorem D.45.8), so it has no
     fixed-point set, and `Q_δ(Σ a_nFrob_n)` is not the measure of anything. Independently, (146.9) exhibits
     a negative value, which no count can take, and (D.44.6(ii)) shows the one genuine count available on
     sums — `\deg_{det} = \log|Σ a_n n|` — is rank 1 and carries no signature.
 (iv) **This is exactly the difference between the multiplicative semigroup `\{Frob_n\}` and the ring
     `Z[π]`.** `Z[π]` has both operations *realized on the same object* (`End(E)` acts on `E`, and `E` has a
     group law); `\{Frob_n\}` has only `⋆`, and the `+` is formal, i.e. carried by no object and therefore
     by no count. ∎ `PROVED` **[R2: (i)–(ii) sustained; (iii) is conditional on Theorem D.45.8, now a
     `CLAIM` (M11), and on the chosen `δ`; (iv) is rhetorical.]**

> **Corpus placement.** (i)–(ii) are re-readings of Paper 44 Thm 3ter.10, Thm 6bis.4 and Thm 8bis.1
> (`CORPUS_CHECK_R146b` §4, item 3 of "what is NEW": *reading the positive off-diagonal entries as counts*);
> (iii)–(iv) are `NEW` (`CORPUS_CHECK_R146b` §§1, 7: the additive/multiplicative locus of the sign is
> "entirely unexamined in either direction").

---

## D.46 — Synthesis input (one page) — **[R2: SUPERSEDED by `R146_003` §D.49.** Kept as the record of round
1's diagnosis. Its terminal claim ("the sign lives in the diagonal counterterm") and its phase-147
recommendation both rest on (146.6), withdrawn under M1, and on O-46.3 as posed, mis-posed under M2: the
difference-only form consumes `δ_m + δ_n`, **not** `δ_m − δ_n`, since by (146.8)
`B_δ(e_m−e_n, e_m−e_n) = L(m,n) − (δ_m+δ_n)/2`. Read `R146_003` §D.49 instead.]**

**Q1 answered.** *Finite symmetric form:* **YES** — `B_δ` of Theorem D.45.1 exists, is unique given the
diagonal, is finite and symmetric for every finite `(δ_n)`, and extends Paper 44 Thm 3ter.10's weights
`Λ(n)n^{−1/2}` exactly. *Count on sums:* **NO** — Theorem D.45.9(iii), with two independent proofs: no
fixed-point set exists for a formal sum, and the form takes the value `−10` on
`5\,Frob_6 − 4\,Frob_{10}` (Theorem D.45.2(ii)). *And the arithmetic diagonal is not finite at all*: adjunction
forces `δ_n = n(2−2g) = −∞` (D.45.3(3)), so the finite form of Theorem D.45.1 is the model's convention, not
the arithmetic object.

**Where the sign lives.** Not in the multiplicative semigroup, and not in a count on the additive module.
Precisely:

* The multiplicative structure `{Frob_n, ⋆, †}` is **complete and counted**: every entry it produces
  (`\log n`, `Λ(n)n^{−1/2}`, the fixed-point measures) is a cardinality or a Haar measure, nonnegative by
  construction. It contains no sign, because it contains no negative number.
* The additive structure needed for a norm form **is not realized by any object** over `Spec Z` (Theorem
  D.45.8), is rank 1 in the only place it does exist (the shadow, Theorem D.44.6), and when imposed formally
  produces a form whose **entire indeterminacy is the diagonal** — the one entry that is not a count
  (Rem 8bis.1c), whose arithmetic value is `−∞` (Thm 8bis.2), and whose choice, if it could be made finite
  and positivity-producing, **is RH** (Prop. D.42.5).
* **So the sign lives in the additive structure — specifically in the diagonal counterterm — and the
  programme's standing hypothesis (phase 136: the sign is a phase-coherence phenomenon of the
  polar/Frobenius coupling) is not contradicted but *located*: the coupling constant is `δ_n`, and the
  polar block is where it would have to come from, since the rulings `F_1,F_2` are the only classes that
  pair with the Frobenius family at all and they are invisible at the zeros.** That last sentence is the
  round's structural finding and it is what phase 147 has to attack.

**Could an object on `C_S × C_S` carry the missing sums?** It would have to (a) restrict to `E_m + E_n` on
the radial diagonal, (b) carry the `2⟨φ,ψ⟩` correction **off** the shifted diagonals, with nonzero `Φ` at the
zeros — since on the shifted diagonals the correction is ruling-plane and invisible (Theorem D.45.7 and its
corollary) — and (c) obey P122.028: it may not be expressible in `\log p, p^{−1/2}, N, Γ` alone. Constraint
(c) **already refutes the correction term as defined**, since `2G(m,n) = ½(m+n−\min·Λ(\max/\min))` is built
from exactly those symbols. Constraints T1 (uniformity in the number field) and T2 (the identity must read
something `Ξ_Q` lacks) apply unchanged; note that by the falsifier check in §D.45.3, the *absence* of the
additive structure is `Ξ_a`-uniform, so a two-variable object cannot be validated by `Ξ_a` failing on it for
this reason — it must fail for a different one.

**Recommendation for phase 147.** Not a two-variable square: the corollary to Theorem D.45.7 shows the
two-variable object would have to supply new zero-data from nowhere, and P122.028 refutes the only correction
term the Euler product offers. Not `O-32` in isolation. **The recommendation is the archimedean-bearing
model**: the round's one genuinely unexplained asymmetry is that `δ_n` is the coupling between the Frobenius
lattice and the polar block, that `MISMATCH 5` records the model has **no archimedean place at all** (its
whole archimedean side is the single integer `χ(C) = 2−2g`), and that Paper 46 open item (21) — the kernel
representation of `\frac1{2π}∫\hat h(τ)[\mathrm{Re}\,ψ(¼+iτ/2)−\log π]dτ` on `D^W` — is the frame's
replacement for that integer. **`δ_n` and open item (21) are the same slot.** Phase 147 should ask what the
archimedean place contributes to `2−2g`, i.e. whether the divergence of `δ_n` is an archimedean divergence
with a finite regularized *relative* value `δ_n − δ_m`, which is all the difference-only form ever needs. The
relevant standing negative (`CORPUS_CHECK_R146b` §3: regularizations tried, rate computed, still infinite)
applies to the *absolute* diagonal, not to the difference — that gap is recorded below as **O-46.3** and it
is the one place this round found where the corpus's `−∞` verdict is not already dispositive.

---

## Corpus check, per idea

| idea in this round | corpus status (checked) | what is cited, not re-derived |
|---|---|---|
| `Z[Frob]` as an additive module with a bilinear degree form (D.45.1) | `NEW` (`CORPUS_CHECK_R146b` §1: "no prior construction treats `{Frob_n}` as generators of a commutative ring under addition") | the off-diagonal entries, Paper 44 Thm 8bis.1 + §12 K1 |
| reading the off-diagonal Gram entries as counts / Haar measures (D.44.2) | `NEW as a reading`, material `TRIED–PARTIAL` (`R146b` §4, "what is NEW" item 3) | Thm 3ter.10, Thm 8bis.8 (`vol(Z_p^×) = \log p`) |
| the would-be norm form `m^2+a_ℓmn+ℓn^2` and its Hasse failure (D.44.3–4) | `NEW` (`R146b` §2: the elliptic-curve degree form "has never been constructed for `Spec Z` as a labelled object") | `R145_004` Q0; `R145_001` D.41.6 |
| `Δ·Δ = −∞` / infinite genus | `TRIED–PROVED, settled` (`R146b` §3) — **not re-derived anywhere above** | Paper 44 Thm 8bis.2, Rem 8bis.1c; Paper 46 Prop 14.2; `R139_001` W4c |
| indefiniteness of the assembled form (D.45.2) | consistent with, and sharper than, phase 141's `Q_{C^Frob}` "indefinite at trace level" (`R146b` §4) — phase 141 used the colimit/all-primes object, this round uses a **rank-2 integral sublattice** with an explicit integer witness, which is what `R146b` recommended | `R141` outcome, cited |
| positivity of the degree form | **`EQUIVALENT-TO-RH`, not attempted** (Prop. D.42.5) | `R145_001` §D.42.4 |
| power maps / dilations as correspondences (D.45.8) | `NEW` for the idele class group (`R146b` §6); the phase-123 `π_n` machinery is a different object and is **not** conflated | `R140_001` D.23.5(i) for the `Ξ_a` group law |
| "the sign is in the additive structure" (D.46) | `NEW` (`R146b` §7, "entirely unexamined in either direction"); framed against phase 136's phase-coherence principle as a *location*, not a contradiction | `PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53` |
| the cosh test / `s_1` | `TRIED–PROVED` tool, reused unchanged | `R142_001` Lemma D.31.4, Prop. D.31.5 |
| Pólya realization for pairings with zero data | **forbidden by the blueprint and avoided**: `r(Frob_n) = τ_{\log n}(2K)` has `Z = 0` | `R140_001` D.23.12(C) |
| Laguerre–Pólya / finite-genus approximation | `TRIED–EQUIVALENT-TO-RH / NO-GO`, **not reopened** | `CORPUS_CHECK_R138` item 9 |

---

## Paper-facing

| # | statement | destination |
|---|---|---|
| **P46-40** | Theorem D.44.3 + Corollary D.44.4: the Euler product determines the would-be norm form `m^2+(ℓ+1−Λ(ℓ))mn+ℓn^2`; the Hasse bound holds only at `ℓ ∈ \{2,3,5\}` and the measured genus is `g_ℓ ≥ (ℓ+1−Λ(ℓ))/(2\sqrt ℓ) → ∞`. **The first finite, prime-by-prime form of the infinite-genus obstruction.** | Paper 46, new §14.4, next to Prop. 14.2 |
| **P44-12** | Theorem D.44.6: `\deg_{det}Sh_Z` is a genuine count and the shadow's additive structure is rank 1 and rigid; the divergence of `Σ_pΛ(p)p^{−1/2}` is the absence of a finite Frobenius trace | Paper 44 §6bis, after Thm 6bis.4 |
| **P46-41** | Theorem D.45.1 + Theorem D.45.2 + Statement D.45.3: `M`'s degree form exists and is unique given the diagonal; it is degenerate against the count axiom and indefinite (witness `Q = −10`); the diagonal is the only freedom, its arithmetic value is `−∞`, and fixing it positively is RH | Paper 46 §14, as the statement of what the Frobenius lattice can and cannot carry |
| **P46-42** | Theorem D.45.7 and its corollary: the sum classes' additive correction is ruling-plane, invisible at the zeros; the cosh test passes for all pairs and is non-detecting; P122.028 refutes the correction term | Paper 46 §12/§14 |
| **P44-13** | Theorem D.45.9: degree is a count on monomials and differences, never on sums — the exact difference between the inverse semigroup and a ring | Paper 44 §8bis, as a closing remark to Rem 8bis.1c |
| **P46-43** | Theorem D.45.8 with its `Ξ_a` check: the only additive structure compatible with the Lefschetz formula is the formal one, **and this does not separate `ξ` from `Ξ_a`** — A3 does not enter here | Paper 46 §15 (falsifier ledger) |

---

## Open items

* **O-46.1.** Is there a finite `(δ_n)` making `Q_δ ⪰ 0` on `M`? **DO NOT ATTEMPT.** `OPEN, suspected
  RH-equivalent, not proved so` **[R2, M12: round 1 labelled this `EQUIVALENT-TO-RH` citing Prop. D.42.5,
  which does not cover it. The prohibition stands; the label does not.]**
* **O-46.2 [R2: PROMOTED to MAJOR (M8); the parenthetical "a volume `≤ 1`" also contradicted the main
  text's "`→ 1`". Correct statement: `c_N → 0` (bare) / `→ ∞` (`♭`), geometrically, no convention-free
  rate.]** Does the chart constant `c_N(m,n)` (Paper 44 §12 K1) affect Corollary D.44.4's threshold
  `ℓ ≥ 7`? It is a volume `≤ 1` multiplying `Λ`, hence it *lowers* `Λ(ℓ)` and *raises* `a_ℓ`, so the failure
  is only reinforced; an exact statement at finite `N` is not written here. `OPEN` (presentational).
* **O-46.3 [R2: MIS-POSED (M2); RE-POSED and largely ANSWERED in `R146_003` §D.47.]** The absolute diagonal `δ_n` diverges (settled, `R146b` §3).
  Does the **difference** `δ_m − δ_n` admit a convention-free finite value? The difference-only form of
  Theorem D.45.1 needs nothing else, and the corpus's recorded negative is about the absolute value. `OPEN`.
* **O-46.4.** The two-variable object of D.46: does any class on `C_S × C_S` restrict to `E_m+E_n` on the
  radial diagonal and carry nonzero zero-data in the correction? P122.028 refutes the Euler-product
  correction; whether another exists is `OPEN`.
* **O-46.5.** `ζ_K` uniformity of Corollary D.44.4 is asserted (Λ ↦ Λ_K, n ↦ N𝔫) but not written out. `OPEN`
  (presentational).

---

## §Label

**No label is proposed and no label is changed.** Phase 146 round 1 produces:

* **[R2: the list below is SUPERSEDED by `R146_003` §Label.** After the audit: D.44.3 →
  `DEFINITION`/`RESTATEMENT`; D.44.4 → `HEURISTIC` (values `CERTIFIED-CORRECT`); D.44.6 → **withdrawn**;
  D.45.8 → `CLAIM`; D.45.1 clause (i) → **not discharged**; D.45.3 items 2–3 → **withdrawn**; (146.6) →
  `HEURISTIC`; O-46.1 → `OPEN, suspected RH-equivalent`. Sustained as `PROVED`: D.45.1 (existence), D.45.2,
  D.45.4, D.45.5, D.45.7, D.45.9(i)–(ii).]**
* `PROVED` *(round-1 list, superseded)*: D.44.3, D.44.4, D.44.6, D.45.1, D.45.2, D.45.4, D.45.5, D.45.7,
  D.45.8, D.45.9, and Statement D.45.3 as an equivalence-of-problems.
* `PROVED-IN-REPOSITORY`: D.44.2 (Paper 44 Thm 3ter.10, 8bis.1+K1, 8bis.8).
* `RESTATEMENT`: D.44.2a, D.44.7.
* `OPEN`: O-46.2, O-46.3, O-46.4, O-46.5. `EQUIVALENT-TO-RH`, not to be attempted: O-46.1.
* **No positivity of any degree form is claimed.** The `Ξ_a` falsifier was run where the blueprint required
  it (§D.45.3) and returned **"holds verbatim for `Ξ_a`"** for Theorem D.45.8 — recorded as a *negative*
  separation result, not as a defect of the construction, since Theorem D.45.8 is itself a no-go and a no-go
  that also holds for the falsifier is exactly what W-a's protocol expects. No FATAL flag is raised: nothing
  in this round proves positivity of anything, and the two quantitative outputs (Corollary D.44.4's Hasse
  failure, Theorem D.45.2's negative witness) are failures of positivity, which is the safe direction.
