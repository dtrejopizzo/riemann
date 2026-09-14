# R140.003 — Builder, round 2, phase 140: repair ledger

*Builder: Claude Opus 5. Date 2026-09-13. Object: the 14 findings of `R140_002_HOSTILE_AUDIT.md`
(1 FATAL, 7 MAJOR, 6 MINOR). All repairs are made **in place** in `R140_001_BUILDER_ROUND1.md` with a
bracketed round-2 note at each site; this file is the ledger, not a second copy of the mathematics.
`README.md` updated. Verdict of the audit — **NOT CONFIRMABLE as round 1** — is accepted in full; two
findings (H3, H8) **reverse the round's headline**, and the reversal is stated as such.*

## 0. Summary

| | count | disposition |
|---|---|---|
| FATAL | 1 | **accepted, repaired** (H1) |
| MAJOR | 7 | **6 accepted and repaired** (H2, H3, H5, H6, H7, H8, H9 — H4 also accepted, so 7/7); **0 contested** |
| MINOR | 6 | **all accepted and repaired** (H10–H15) |
| contested | **0** | — |

**Two findings changed what the round says, not merely how it says it.**
* **H3** — the collapse into the ruling plane is a property of the builder's realization `r`, not of
  the Frobenius family; and the blueprint's instruction to compare with Paper 44's Gram forms
  (Thms 8bis.1, 8bis.4a) was not executed. It is executed now, in a new §D.23.3bis, and **the
  comparison reverses the round's message**: the *pure Frobenius* Gram form is unsigned at every finite
  chart (Paper 44 Theorem 8bis.4a), the opposite of "equality always, empty".
* **H8** — the round's proposed phase-141 target (O-16) is Weil positivity on an orbit. A new Theorem
  D.23.13 proves it (Castelnuovo on the orbit `=` Bochner positive-definiteness of a Toeplitz kernel
  `=` RH for the zeros `E_0` sees), and **O-16 is withdrawn**.

## 1. Per-finding ledger

| # | sev | finding | disposition | where repaired |
|---|---|---|---|---|
| **H1** | FATAL | `L_S := O_{K,S}` is not Paper 44's lattice (`44/main.md:2668–2672`: `L_S = ∏_{p∈S_f}Z_p`); with it `𝔫O_{K,S} = O_{K,S}`, the cone is acyclic, `H^0 = 0`, `deg_{det} = 0` — D.22.5 proved the opposite of its claim; O-9 not closed | **ACCEPTED, REPAIRED.** Definition D.22.4 replaced by the literal transport `L_S := ∏_{𝔓∈S_f}O_𝔓`, `𝔫L_S := ∏_𝔓 𝔓^{v_𝔓(𝔫)}O_𝔓`. "Projective `O_K`-module" deleted. D.22.5 re-proved **place by place**, where `𝔓^kO_𝔓` is principal: (i) `H^0 = ∏_𝔓O_𝔓/𝔓^{v_𝔓(𝔫)} ≅ O_K/𝔫` of order `N𝔫` **with no hedge**; (ii) the triangle now needs only that `π_𝔪` is a non-zero-divisor in a local ring — **cheaper than round 1's appeal to invertibility**; (iii),(v) unchanged; (iv) `\mathrm{Tor}_1(O_𝔓/π^a,O_𝔓/π^b) ≅ O_𝔓/π^{\min(a,b)} ≠ 0`. **O-9 reopened and closed again**; Corollary D.22.6 says so explicitly. §D.22.1 (measures, law, bidegrees) untouched, as the auditor allows. | D.22.4–D.22.6 |
| **H2** | MAJOR | Theorem D.24.5's general biconditional is false: `ψ ≡ 0` satisfies the hypotheses and (c) fails for it under RH | **ACCEPTED, REPAIRED.** Split into (i) `(⇒)` fully general (`PROVED`); (ii) `(⇐)` for exactly the class of `ψ` satisfying the displayed (D.24.5a) (`PROVED`); (iii) the biconditional for `h⁰_□` with `χ ≤ 1/8`. The counterexample is quoted in the round-2 note. Nothing downstream used `(⇐)`. | Thm D.24.5 |
| **H3** | MAJOR | the collapse is a property of `r`; Papers 44/46 never realize `Frob_n` in `D^W`; `r` deletes `Λ_K(𝔫)N𝔫^{−½}`; the blueprint's comparison with Thms 8bis.1/8bis.4a was not performed | **ACCEPTED, REPAIRED, and the message reversed.** (a) Definition D.23.6 renamed the **Pólya realization**, declared a *choice*, with the deletion of the arithmetic weights stated. (b) New **§D.23.3bis**: Definition D.23.11 (Paper 44's Gram matrix, with §12 correction K1 carried) and **Theorem D.23.12**, the three-Gram-form table — (A) pure Frobenius: `W_fin` only, sparse on the prime-power-ratio graph, weights `Λ(q^k)q^{−k/2}`, **unsigned by Thm 8bis.4a**; (B) unit-averaged: full Weil kernel, sign `⟺` RH, forgets factorization; (C) Pólya: **rank 2** (`u⊗v+v⊗u`), reads neither. (c) Headline rewritten in §0.2, the D.23.3 blockquote, the Weil table (two new rows), D.25 and the README. | D.23.6, **§D.23.3bis (new)**, §0.2, D.23.4 table, D.25 §2 |
| **H4** | MAJOR | D.23.8 is `R138_001` Cor. D.15.4c on a sub-cone; "the phase's central structural finding" overstates | **ACCEPTED, RELABELLED.** D.23.8 is now `RESTATEMENT` of Cor. D.15.4c on `r(Div_□⊗R)`, `PROVED` as a computation; the blockquote is withdrawn and replaced; D.23.9 stays `PROVED` (new) with its novelty narrowed to the rank count and the phase-41 comparison. | Thm D.23.8, blockquote, label table |
| **H5** | MAJOR | `F_1,F_2` are not `e_∓` (`e_± ∉ D^W`, Paper 46 Prop. 14.1(iv)); they are `a_0`-dependent | **ACCEPTED, REPAIRED.** Recorded as the **third correction of the blueprint** (§0.3.3, alongside the coprimality and `χ` corrections). `F_1,F_2` are stated as lifts of the ruling data, canonical **mod `𝓝_∞`** — with a one-line proof that two choices of `a_0` differ by an element of `𝓝_∞`. P46-10 now **extends** Prop. 14.1 and carries its clause (iv); "replacing" deleted. | §0.3.3, Def. D.23.6, P46-10 |
| **H6** | MAJOR | the CC refutation asserts `\deg_{CC} = \deg`, which Finding 13.8 contradicts (`\deg K_{CC} = −2\log2` vs `\deg K = 1`); 13.8(1) cited for a proposition it does not make; `h_c^{CC}(0) = 1` is outside Definition D.24.1 | **ACCEPTED; the refutation is WITHDRAWN.** Lemma D.24.2 replaced by **Observation D.24.2**: (i) `λ_{CC} < 1` `PROVED` **in CC's own units**; (ii) the `λ_{CC}²` deficit `PROVED-CONDITIONAL` on the declared identification; (iii) **two unit problems named and left `OPEN`** — (U1) the degree dictionary (Finding 13.8's unreconciled entry), (U2) `\dim_{\mathbb S}` (integer, over `\mathbb S`) versus a real functional on `D^W`. Definition D.24.1 widened to `h_c(x) = 0` for `x ≤ −c''`, so (β) is in the class with `c'' = \log 2`. **P46-14 withdrawn**, replaced by the conditional. Candidate (β): **`OPEN`, not `REFUTED`**. | Def. D.24.1, Obs. D.24.2, Prop. D.24.3a, P46-14, README |
| **H7** | MAJOR | (AT-1)(ii): D.19.5's witness is effective, not primitive; the primitive⇔RH bridge is a `ξ`-theorem | **ACCEPTED, WEAKENED as the auditor's second option.** (AT-1)(ii) now concludes only: (c) for `h⁰_□^{(Q)}` implies a **`Ξ_Q`-primitive-cone** positivity statement the corpus has not proved and that D.19.5 makes implausible. The missing witness is recorded as **O-17 (new)**, with the auditor's suggested route (Landau on `Π_P`-images, fixed factor at the Davenport–Heilbronn zero) quoted and **not** carried out. (AT-1) now rests on (i), a theorem. **Contrast added:** for `Ξ_a` the bridge **does** exist in the corpus (Paper 46 Lemma 12.4A and §12.3), so (AT-2) is met by a primitive-cone theorem and (AT-1)(ii) is not — the asymmetry is recorded. | (AT-1)(ii), (AT-2)(iii), O-17 |
| **H8** | MAJOR | D.23.10(ii) asserts nothing checkable; "the Euler product enters at `T_n`" is a hope; `\|T_n\| ≤ 2W(E_0)` over the family **is** RH for the zeros `E_0` sees | **ACCEPTED IN FULL; O-16 WITHDRAWN.** (1) Clause (ii) replaced by the clean identity (D.23.5a) with a proof from (11.6) applied twice. (2) The Euler-product sentence is **deleted, not demoted**, with the auditor's reason stated (`τ_{\log m}τ_{\log n} = τ_{\log mn}` is the group law of `R`, which `Ξ_a` shares — this round's own Thm D.23.5(i)); only a `HEURISTIC` residue remains. (3) New **Theorem D.23.13**: the orbit Gram form is the Toeplitz kernel `κ_{E_0}(c) = W(E_0,τ_cE_0)`; Castelnuovo on all finite spans of translates `⟺` **Bochner positive-definiteness** of `κ_{E_0}`; sufficiency unconditional; necessity proved (Bohr almost-periodicity) when finitely many real parts occur, the general case recorded as **O-15′**. D.25 §5 and the README carry H8.3 verbatim. | D.23.10(ii), **Thm D.23.13 (new)**, D.25 §5, O-16→withdrawn, O-15′ |
| **H9** | MAJOR (proof) | D.23.4 uses `Cl(K_0)` and `h(−D_0)` where the form class group is the **ring class group** of `O_{−D}`; `h(−D)>1 \not⟹ h(−D_0)>1` (`−32` over `−4`) | **ACCEPTED, REPAIRED.** The proof is restated for the order `O_{−D}`, proper ideals, `Cl(O_{−D})`, Chebotarev in the **ring class field** (Cox Thms 7.7, 9.12), primes prime to the conductor. **The auditor's explicit witness is adopted**: `Q = x²+5y²`, `r_Q(3) = r_Q(7) = 0 < r_Q(21)` (`21 = 1²+5·2²`), which makes the theorem checkable without Chebotarev. Statement unchanged. | Thm D.23.4 proof |
| **H10** | MINOR | Cor. D.23.3 over-transports the *isomorphism*; injectivity over `K` is the builder's own O-13 | **ACCEPTED.** D.23.3 now asserts a **surjective** monoid homomorphism `I(O_K) → \{Frob_𝔫\}`, iso **iff O-13**, and `Div_□^{(K)}` is defined on the generators `\{Frob_𝔫\}` so that nothing depends on O-13. | Cor. D.23.3 |
| **H11** | MINOR | `Div_□` is not the displayed direct sum | **ACCEPTED.** `Z·Δ` summand dropped; `Δ := Frob_1` is a name. | Def. D.23.1 |
| **H12** | MINOR | internal inconsistency inside D.22.5 (the hedge vs (iii),(v)) | **ACCEPTED.** Disappears with H1's repair of the definition, as the auditor required — the hedge is deleted, not patched, and the deletion is noted as the symptom it was. | D.22.5 |
| **H13** | MINOR | the grid sweep is not a lower-bound certificate; `--fast` is 0.13 s not 1 s; the second "constant" is a `print` | **ACCEPTED.** §0.4 and the README say **"illustrates"**, not "certifies"; the absence of any Lipschitz/interval bound, the fact that the minimizer is not a node, and the timing are all stated. The script's docstring already said the value is proved, not computed; it is unchanged. | §0.4, README, label table |
| **H14** | MINOR | "`NS(P¹×P¹)`, scaled" hides that `K_S = −2(f_1+f_2)` ≠ `+½(F_1+F_2)`, and that `2 = 2−2g` is a curve formula on a surface diagonal, which Finding 13.8 declines to reconcile | **ACCEPTED.** Cor. D.23.9 now says the **lattice with its form** matches, lists the canonical-class mismatch explicitly, and carries Finding 13.8's refusal; P46-11 carries the refusal verbatim. | Cor. D.23.9, P46-11 |
| **H15** | MINOR | (N) is **moot**, not unsatisfiable; the step tacitly needs Thm 12.3 for every member of `𝒵` | **ACCEPTED.** (AT-1)(iii) now reads "**moot, and a fortiori unsatisfiable**", and names Paper 46 §12.5's four substitutions as the step that carries Thm 12.3 across `𝒵`. | (AT-1)(iii) |

## 2. What the audit confirmed and what round 2 did **not** touch

The audit's §0 confirms ten items by independent re-derivation. None was modified: Paper 44
Thm 3ter.4(i) for all `m,n` (§0.3.1); the intersection matrix of Thm D.23.7(iii); the congruence
(D.23.4); `\inf g = c²/2` with witness `½F_1` and the correction of the lead's `χ = ¼`;
Lemma D.24.6 and **Theorem D.24.7** (the round's strongest result — refutation of (b′) for every
bidegree-function, which the auditor could not break); the algebra of Thm D.23.10; `u < v` for `Ξ_a`;
the arithmetic of (AT-1) (only its *proof* moved, H9); the growth `(r²/4)m²`; and the script's output.

## 3. New material added in round 2 (beyond repairs)

| item | statement | label |
|---|---|---|
| **§D.23.3bis, Def. D.23.11, Thm D.23.12** | the three Gram forms (A) pure Frobenius / (B) unit-averaged / (C) Pólya, what each reads and its sign; (C) has **rank 2**; (A) and (B) are complementary slices of one projector and **no object carries both** | `PROVED` (C); `PROVED-IN-REPOSITORY` (A),(B) |
| **Thm D.23.13** | orbit Castelnuovo `=` Bochner positive-definiteness of the Toeplitz kernel `κ_{E_0}` `=` RH for the zeros `E_0` sees | `RESTATEMENT` + `PROVED` (necessity under a finiteness hypothesis) |
| **Thm D.24.11** | any `h⁰` reading the pairings against `r(Div_□)` **factors through `M`**; D.24.5(i) and D.24.7 apply verbatim | `PROVED` |
| **Cor. D.24.12** | an admissible `h⁰` must separate equal-bidegree classes with different zero data, hence must read `Z(E)` **through the arithmetic side** — pairings `I_∞(E,X)` with `Z(X) ≠ 0`; `r(Div_□)` is exactly the wrong family | `PROVED` |
| **O-15′, O-17** | new open items (general necessity in D.23.13(iv); a `Ξ_Q`-primitive witness) | `OPEN` |

## 4. Labels that moved

| item | round 1 | round 2 |
|---|---|---|
| D.22.2 (`Sh_{O_K}`) | `PROVED` | **FALSE as written**; `PROVED` after the H1 repair |
| O-9 | closed | reopened by H1, **closed again** by the repair |
| D.23.8 | `PROVED` ("central structural finding") | **`RESTATEMENT`** of `R138_001` Cor. D.15.4c on a sub-cone |
| D.24.5 (general biconditional) | `PROVED` | `(⇒)` **`PROVED`**; `(⇐)` **withdrawn in general**, `PROVED` for the class (D.24.5a) |
| candidate (β) (Connes–Consani) | `REFUTED` at (c) | **`OPEN`**; refutation `PROVED-CONDITIONAL` on `\deg_{CC} = \deg` |
| (AT-1)(ii) | (c) equivalent to a **false** statement for `Ξ_Q` | (c) implies a `Ξ_Q`-primitive-cone statement that is **unproved and implausible** (O-17) |
| O-16 | "the phase-141 target" | **WITHDRAWN** (Thm D.23.13: RH in disguise) |
| P46-14 | paper-facing | **withdrawn**, replaced by a conditional `OPEN` entry |
| clause (N) for `h⁰_□` | "unsatisfiable" | "**moot**, a fortiori unsatisfiable" |
| script | "certifies" | "**illustrates**" |
| **row D** | no change | **no change** — unchallenged by the audit |

## 5. Statement of the round-2 position, in three sentences

The durable results are **Theorem D.24.7** (no `h⁰` reading only bidegrees — now also: only the
Pólya-Frobenius Gram data — satisfies (b′)), **Theorem D.24.4** (`χ = 1/8`, the lead's `¼` corrected),
and **Proposition D.24.3a** (the tensor square supplies the growth `(r²/4)m²` exactly, for every number
field). The round's round-1 *framing* is withdrawn: the collapse belongs to a realization this round
chose, and the Euler product's own Gram form is arithmetic, sparse and **unsigned at every finite
chart**, which is the opposite of non-detecting. What phase 141 should take is **O-15** (the moment
cone, the whole content of (b′), with no zero named) and **O-14′** (can an `h⁰` reading family (A)'s
arithmetic Gram entries satisfy (b′)?), with **O-17** as the falsifier-side prerequisite — and **not**
O-16, which Theorem D.23.13 shows is Weil positivity on an orbit.
