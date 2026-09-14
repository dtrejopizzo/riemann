# R137.006 — Hostile final confirmation, phase 137

Auditor: hostile (Opus 5). Date: 2026-09-13. Object: `R137_005_BUILDER_ROUND3.md`, the in-place errata in
`R137_003_BUILDER_ROUND2.md`, `R137_001b_PART_III_DRAFT.md`, `README.md`, `scripts/d137_lattice.py`, the
rewritten status note in `03-research/phase-65-signature-continuity/RH-PROOF.md` and points 2 and 4 of the
`NO-GO-LIST.md` entry. Everything checked against the **current files**; the R3 reading was re-derived
from `CORRECTIONS-CONNES-R3.md` and `RH-PROOF.md` line by line; `Proposition 2.2` and `Observation 2.1`
were reproved independently; the vacuity claim was attacked adversarially.

**Headline.** `N1` is **resolved**, and resolved correctly: I verified the fork from source and it holds.
The `UNDECIDED` on the R3 half of D.0 is lifted, and the ground the builder now gives is better than
round 2's. Round 3 also proves two statements that were merely asserted (`Observation 2.1`,
`Proposition 2.2`) — I checked both and both are right. **One new `MAJOR` finding**: `Observation 1.2`,
the vacuity claim, is **false as stated** — the falsifier class is not empty, it contains every Dedekind
zeta function — and it has propagated into two cross-file artefacts (`N9`). It does **not** change any
verdict, because the verdict rests on the fork, which is independent of it. Three `MINOR` housekeeping
items are `NOT FIXED` or only partly fixed despite the erratum table saying otherwise.

---

## 1. `N1` — the fork, verified from source (`RESOLVED`; outcome (A) is correct)

### 1.1 Does R3 point 1 really deny the identification for `G_P^∘`? — **Yes.**

`CORRECTIONS-CONNES-R3.md` point 1 is headed "**Arbitrary-pairing realization is illegitimate (old
Theorem 5.3 / 'Check 4')**" and closes "**The cancellation was asserted.**" "Check 4" is exactly
`RH-PROOF.md` §3, whose content is `⟨R_P^∘(z)ι_Pφ, ι_Pψ⟩ = 𝒲_P^∘(f_{ψ,φ};z)` and
`𝒲_P^∘ → G_Ξ^{G5}(z)_{ψφ}` on `U_-` — i.e. precisely the limit identification for the **sourced** object.
Point 1's "Fix" then leaves the sourced object ("Take the log-derivative of the determinant … There the
cross words reorganize **under the trace**"). The builder's reading is exact.

### 1.2 Does R3 point 3 really run Vitali on `M_P` only? — **Yes, in terms.**

Point 3, verbatim: "`M_Ξ = −Ξ'/Ξ` (and its channel matrix `G_Ξ^{G5}`) is a one-variable function; the Pick
kernel `K_Ξ(z,w)` … is built from it *afterwards*. **Vitali acts on the one-variable `M_P`**; `sq₋` is
read off `K_Ξ` at the end." And the chain paragraph confirms it end to end: Montel on `M_P`,
identification of `M_P → M_Ξ` from G3 plus the trace-log identity, "Vitali ⟹ `M_Ξ` has no off-real pole".

### 1.3 Is there any object in R3 carrying both premises? — **No.**

I looked for a third object and there is none. The two candidates are the ones the builder tabulates, and
each is missing one premise for a reason internal to R3:

* `G_P^∘`: bound **yes** (point 4, §1.4 below), identification **withdrawn by point 1**.
* `M_P`: identification **yes** (trace-log, point 1's Fix, plus G3), bound **not supplied**. A sourced
  matrix built from `M_P` would need the marked pairing that point 1 withdrew, so "matrix-Herglotz" does
  not produce a third object — the builder's closing sentence in Proposition 1.1's proof, and it is right.

The Nevanlinna argument is correct in the proof, where it is stated about `−∂_z\log D_P^∘` alone
(mass `= Σ_jm_jδ_{z_j}`, total mass the eigenvalue count of `A_P`, divergent) and then the subtraction of
`E_P'/E_P` is named as the counterterm whose mass-cancellation is the open question. See `N10` for a
loose phrasing of the same point in the table cell.

### 1.4 The concession — `‖ι_Pφ‖²` and the shorting (`CONFIRMED`)

I re-derived both halves.

* **(1.1) is right.** `H_P` is a sum of positive rank-one atoms at `k\log p` with weights
  `(\log p)p^{−k/2}`, `k ≥ 1`, so the Gram energy of a source is that weighted sum of
  `|\hatφ(k\log p)|²`; with `|\hatφ(t)| ≤ C_Ne^{−at}(1+t)^{−N}` this is
  `≤ CΣ_pΣ_{k≥1}(\log p)p^{−k(1/2+2a)}`, convergent iff `\tfrac12+2a > 1` iff `a > \tfrac14`, and the
  `P`-dependence is a partial sum of a convergent nonnegative series, hence uniform. This **is** L1.
* **The parenthetical note about `k = 0` is a good catch and is correct**: `Σ_p\log p = ∞`, so the absence
  of the diagonal atom is doing real work, independently of the decay.
* **(b) is right, and is the part round 2 got wrong.** For a projection `‖Q_Pu‖ ≤ ‖u‖`; for a Schur
  complement of a PSD block matrix, `S = K_{∘∘} − K_{∘H}K_{HH}^{−1}K_{H∘} ⪯ K_{∘∘}` (standard, and it is
  the right lemma here). So `‖ι_Pφ‖²_{H_P^∘} ≤ ‖ι_Pφ‖²_{H_P}`. The shorting cannot re-introduce the
  divergence into a **source norm**, and `D8.5b-i` §4 — about the assembly of the resolvent — does not
  block it. The builder withdrawing round 2's parenthetical is correct and correctly recorded.

**Status of `N1`: RESOLVED.** Outcome (A), with the reason repaired. `R137_004`'s `UNDECIDED` on the R3
half of D.0 is lifted. This is a better verdict than either previous round's: it is internal mathematics,
it needs no falsifier, and it is a sharper statement of `D8.5b-i` §5's own "each gets one clause, never
both", now at the level of R3's repairs rather than its candidates.

### 1.5 (i) The `Ξ_a` run on point 4 (`CONFIRMED`), and G4 (`conclusion right, reason loose`)

**Point 4 transfers.** `w^{(a)}_{p,k} = (\log p)p^{−k/2}(p^{ka}+p^{−ka}) ≤ 2(\log p)p^{−k(1/2−a)}`, so the
source-core sum converges iff `(\tfrac12−a) + 2a' > 1`, i.e. `a' > \tfrac14 + \tfrac a2`. Verified; the
core is non-empty and the bound is uniform in `P`. The consequence drawn — **point 4 cannot be the
load-bearing step, since it holds for an object with off-line zeros** — is correct and is exactly the kind
of conclusion the falsifier is for. G1 and G2 transfer for the stated reason (positivity of the atoms;
`K = ∫Y^*HY ⪰ 0` is formal in `H ⪰ 0`). All `CONFIRMED`.

**G4: the conclusion is right, the reason as written is not (see `N8`).** The builder argues "`Ξ_a`'s polar
set `\{−a,a,1−a,1+a\}` has four points, so the divergent block has rank `≥ 2`". By that criterion `ξ`
would have rank `2`, since its polar set is `\{0,1\}` — yet phase 65's G4 and `D0-FOUNDATIONS.md`'s
rank-one `Q_P = I − |\hat h_P⟩⟨\hat h_P|` say rank one. The criterion that actually works is the one the
builder himself uses in Observation 1.2: count the poles of the **uncompleted** function. `ζ` has **one**
(`s = 1`); `ζ(s+a)ζ(s−a)` has **two** (`s = 1\pm a`); the completed polar sets `\{0,1\}` and
`\{−a,a,1−a,1+a\}` are these paired with their functional-equation images. So rank `1` versus rank `2`,
the conclusion stands, and the repair is one clause.

---

## 2. `N9` (`MAJOR`, new) — Observation 1.2's vacuity claim is false: `ζ_K`

**Location.** `R137_005` §1.4, Observation 1.2; propagated to the `RH-PROOF.md` status note (*Falsifier*
paragraph) and to `NO-GO-LIST.md` point 4; summarized in `README.md` ("the falsifier family is **empty**
for G4's shape — the test is vacuous, not passed").

**Claim.** "Consider the class in which the phase-65 chain's hypotheses make sense: nonnegative von
Mangoldt weights (G1), a functional equation, and a **simple** pole (G4). Inside the family
`F = ∏_jζ(s+a_j)^{m_j}` … a **simple** pole forces a single `a_j`, and the functional equation then forces
`a_j = 0`, i.e. `F = ζ^m` … **So this family contains no object with nonnegative weights, a simple pole and
off-line zeros: the `Ξ_a` test is *vacuous* against the phase-65 chain.** … Whether some object outside
this family qualifies (**a degree-1 `L`-function** with a simple pole, nonnegative `Λ`-weights and a known
off-line zero) is `OPEN`, and I know of none."

**Why it is wrong.** The computation *inside* the named family is correct (I checked it, modulo `N11`).
The error is the identification of that family with "the class in which the chain's hypotheses make
sense", and the "degree-1" qualifier in the escape clause — G1–G5 say nothing about degree. The class is
far from empty. **Every Dedekind zeta function `ζ_K` is in it:**

* **G1, nonnegative von Mangoldt weights.** `ζ_K = ∏_𝔭(1−N𝔭^{−s})^{−1}`, so
  `−ζ_K'/ζ_K(s) = Σ_𝔭Σ_{k≥1}(\log N𝔭)N𝔭^{−ks}` — atoms at the modulus points `k\log N𝔭` with weights
  `(\log N𝔭)N𝔭^{−k/2}·N𝔭^{−k(s−1/2)}`, all **positive**. So `H_P^{(K)} ⪰ 0` and G2 follows formally,
  exactly as in §1.5.
* **G4, a simple pole, rank one.** `ζ_K` has a **single simple** pole, at `s = 1` (class number formula) —
  the *same* shape as `ζ`, and unlike `Ξ_a`. Its completed `Λ_K` has polar set `\{0,1\}`, identical to
  `ξ`'s. So G4's rank-one, definite divergence on one pole mode transfers on the builder's own criterion.
* **Functional equation.** `Λ_K(s) = Λ_K(1−s)` with
  `Λ_K(s) = |d_K|^{s/2}(π^{−s/2}Γ(s/2))^{r_1}(2(2π)^{−s}Γ(s))^{r_2}ζ_K(s)`. ✓
* **G5** is definitional. **G3** is in exactly the same unproved state for `ζ_K` as for `ζ`.
* **Point 4** transfers: `Σ_𝔭Σ_k(\log N𝔭)N𝔭^{−k(1/2+2a)} ≤ nΣ_pΣ_k(\log p)p^{−k(1/2+2a)} < ∞` for
  `a > ¼`, with `n = [K:\mathbb Q]`, uniform in `P`.

So the class is not empty; it is large. What **is** true is the much weaker statement that no member of
it is *known* to have off-line zeros: GRH for `ζ_K` is open, not false. The correct sentence is therefore
"*the corpus has no falsifier of G4's shape with **proven** off-line zeros*", not "*no falsifier of the
shape G4 requires exists*".

**And the replacement is a stronger test than the one it replaces.** If the chain is sound, it applies to
every `ζ_K` verbatim and therefore proves **GRH for every number field**. That is not a refutation — GRH
may well be true — but it is a far more searching structural test than `Ξ_a`, it *is* available, and it
changes §1.4's conclusion: "the corpus's faithfulness test cannot adjudicate this chain" is too strong.
It cannot adjudicate it *by exhibiting a false consequence*; it can and should record what the chain
would deliver if sound.

I also checked the two nearby candidates and they fail, which is worth recording so nobody re-treads it:
**Epstein zeta functions** `Z_Q(s)` do have a simple pole, a functional equation and, for class number
`> 1`, **proven off-line zeros** (Davenport–Heilbronn) — but they have no Euler product, so `−Z_Q'/Z_Q`
has signed coefficients and they fail G1 exactly as DH does. **`ζ_K/ζ = ∏_{χ≠1}L(s,χ)`** (abelian `K`) is
entire, so it has no pole at all and G4's divergence structure is absent.

**Minimal repair.** Replace Observation 1.2 with: (a) the computation inside `∏ζ(s+a_j)^{m_j}`, which is
correct and worth keeping; (b) the statement that the hypothesis class is **not** that family and contains
every `ζ_K`; (c) "no member of the class is known to have off-line zeros, so the falsifier cannot
currently adjudicate"; (d) the observation that the chain, if sound, proves GRH for every `ζ_K`, recorded
as the sharper standing test. Then correct the *Falsifier* paragraph of the `RH-PROOF.md` status note,
`NO-GO-LIST.md` point 4, and the `README.md` row, all three of which now carry the false claim.

---

## 3. Per-finding status

| # | status | note |
|---|---|---|
| **N1** | **RESOLVED** | outcome (A); fork verified from source (§1); round 2's parenthetical correctly withdrawn; `R137_004`'s `UNDECIDED` lifted. Residues `N10`, `N11` are phrasing |
| **N2** | **NOT FIXED** | `R137_005` §2 and the erratum table say "Fixed in place, with a bracketed round-3 note". It is not: `R137_003` line 165 still reads "`e^{2t} ≥ 3/(2π²n²)`, and `3/(2π²n²) ≤ 3/(8π²) < 1`". The correct threshold is `3/(2πn²)`, `3/(8π) = 0.1194`. Conclusion still unaffected; the erratum claim is wrong |
| **N3** | **PARTLY FIXED** | the docstring's statement of (A) now gives `0.2422553269` ✓, but line 54 of the script still carries the comment `U0 = log(XSTAR/pi)/2  # = 0.2423106...` — the same wrong figure, one line from the code that computes the right one |
| **N4** | **FIXED, and better than asked** | Observation 2.1 is stated, proved and placed in `R137_001b`'s paper-facing table (line 175). I re-verified it: uniform `ρ_Q ≤ ρ` gives only `h⁰_{Z,≤Q} ≤ π_*(Q)\log(2mρ+1)`, divergent in `Q`; `Q(m) = o(m\sqrt{\log m})` alone **does** suffice via `ρ_Q ≤ Ce^{CQ}/\min Λ(q)`. Paper 46 §14.5 item (23)'s "equivalently" is indeed incorrect |
| **N5** | **FIXED by construction** | Proposition 2.2 reproved independently: `a_q ≤ −1` (Lemma 13.5b); at `t = \log q`, `mK(\log q) ≥ w_qΠK(0)`; `K(t) ≤ Ce^{9t/2}e^{−πe^{2t}}` on `t ≥ 0` (the `n = 1` term dominates, `Σ_{n≥2}n⁴e^{−π(n²−1)e^{2t}}` bounded); `w_q ≥ (\log2)q^{−1/2}` gives `m ≥ cq^{−5}e^{πq²}`, hence `q ≤ \sqrt{(\log m)/π}(1+o(1))`. **Correct.** The bracket `e^{πq²} ≤ m ≲ e^{5.1q²}` is consistent (`π < 5.1`) and Remark 13.6a's heuristic is now a theorem in both directions. `R137_003` §2.3b and draft Remark 17.2a are amended ✓ |
| **N6** | **FIXED** | `R137_003` §2.4b retitled "this bootstrap does not close", with a bracketed note, and the structural claim promoted ✓ |
| **N7** | **FIXED in the body, residual in two headers** | `R137_003` §2.3a and §8 and the script docstring now carry the robustness statement (`L ≤ 460` against a sampled `L ≈ 101.5`) ✓. But the word "interval-safe" survives in `R137_003`'s own header line 6 and in `README.md`'s rules line 6 |
| **(i)** `Ξ_a` on point 4 | **CONFIRMED** | `a' > ¼ + a/2` verified; G1, G2 transfer; point 4 shown not load-bearing |
| **(i)** G4 | **conclusion CONFIRMED, reason loose** | see `N8` |
| **(ii)** vacuity | **REFUTED** | see `N9` |

### New findings

* **`N9` (`MAJOR`)** — Observation 1.2's vacuity claim is false; the class contains every `ζ_K`. §2 above.
  Propagated to the `RH-PROOF.md` note, `NO-GO-LIST.md` point 4 and `README.md`.
* **`N8` (`MINOR`)** — G4's failure for `Ξ_a` is argued from "four polar points", a criterion that would
  give `ξ` rank `2` (its polar set is `\{0,1\}`). Count poles of the uncompleted function instead: `ζ`
  has one, `ζ(s+a)ζ(s−a)` has two. Conclusion unchanged; one clause to repair. The same loose criterion
  appears in the `RH-PROOF.md` status note and `NO-GO-LIST.md` point 4.
* **`N10` (`MINOR`)** — Proposition 1.1's table cell for `M_P` says its "Nevanlinna measure is
  `Σ_jm_jδ_{z_j}` with total mass the eigenvalue count, divergent". That is the measure of
  `−∂_z\log D_P^∘`, not of `M_P`; `M_P` is the difference with the counterterm and its mass is precisely
  what is unknown. The proof states this correctly ("the boundedness of the difference is precisely the
  statement that the renormalization does not leak mass"); only the cell is loose. The same compression
  appears in the `RH-PROOF.md` note and `NO-GO-LIST.md` point 2.
* **`N11` (`MINOR`)** — Observation 1.2 restricts to `m_j > 0` by fiat. Nonnegativity of the Dirichlet
  coefficients does **not** force it (`m = (2,−1)`, `a = (0,1)` gives `Λ(n)(2−n^{−1}) > 0`). What does
  exclude negative `m_j` is the *single*-pole hypothesis — a factor `ζ(s+a_j)^{m_j}` with `m_j < 0`
  contributes poles at every zero of `ζ(s+a_j)`. One clause.
* **`N12` (`MINOR`)** — "Neither object carries both premises" (Proposition 1.1, §1.5, and both cross-file
  texts) should be read as *as R3 stands*, not as an impossibility: point 1 says the cancellation "**was
  asserted**", i.e. unproved, not false. The fork is a gap, which is all the `REFUTED` verdict needs; but
  the sentence as written reads as a no-go, and the phase's own label discipline distinguishes the two.

---

## 4. Per-item verdicts

| item | verdict |
|---|---|
| **D.0** | **CONFIRMED.** The verdict `REFUTED` on `RH-PROOF.md` now stands on verified ground in **both** versions: pre-R3, the chain is `(G1–G5) ∧ L1 ∧ L2 ∧ L3 ⟹ RH` with L1 not of the advertised kind; R3, the bound and the identification sit on different objects and R3's single-entry ledger lists neither half. I verified the fork from source (§1.1–§1.3) and the concession on point 4 and the shorting (§1.4). `R137_004`'s `UNDECIDED` is **lifted**. Residue: the *Falsifier* paragraph of the verdict carries `N9` and `N8` and must be corrected — neither touches the verdict, which rests on the fork alone, and the builder says so explicitly. |
| **D.11** | **CONFIRMED**, and strengthened since round 2: Remark 13.6a's heuristic is now a theorem in both directions (Proposition 2.2, verified), and Paper 46 §14.5 item (23)'s "equivalently" is corrected on the record (Observation 2.1, verified, and in the draft's paper-facing table). Minor residues `N2`, `N3`, `N7`. |
| **D.12** | **CONFIRMED** (unchanged from round 2; no round-3 edits). |
| **D.13** | **CONFIRMED** (unchanged from round 2; no round-3 edits). |

**Overall verdict: CONFIRMED.** Phase 137 rounds 1–3 close with four confirmed items, one `MAJOR`
residue (`N9`) that is confined to a paragraph the verdict does not rest on, and five `MINOR` residues
(`N2`, `N3`, `N7`, `N8`, `N10`, `N11`, `N12` — of which `N2` and `N3` are simply not done despite being
recorded as done).

**Required before this is filed as closed** (all small, none mathematical):
1. Correct Observation 1.2 per §2, and with it the `RH-PROOF.md` *Falsifier* paragraph,
   `NO-GO-LIST.md` point 4 and the `README.md` row — the claim "no falsifier of the shape G4 requires
   exists" is false and is currently in three places outside this directory's working notes.
2. Actually apply `N2` and the second half of `N3`; remove "interval-safe" from the two headers (`N7`).
3. One-clause repairs for `N8`, `N10`, `N11`, `N12`.

**Part III.** Unchanged: **not appendable**. Draft §0's four reasons stand, `N4`'s Observation 2.1 is now
correctly in the paper-facing table, and the (X19) §1.13 amendment is still a lead decision.

**D.14.** The builder has adopted the auditor's gate verbatim, including the removal of the
`Q(m) = Ω(m)` disjunct and the precedence of open item (23c). **Agreed, no residue.** Open D.14 only on
`h⁰_Z(mK) = Ω(m^{2−ε})`, and settle (23c) — whether `h⁰_Z(mK)` and `Q(m)` are finite at all — first.
