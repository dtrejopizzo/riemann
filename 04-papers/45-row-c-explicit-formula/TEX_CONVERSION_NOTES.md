# Conversion notes: `main.md` → `main.tex`

Source: `04-papers/45-row-c-explicit-formula/main.md` (2401 lines).
Target: `main.tex`, compiled with `pdflatex`, 31 pages, zero errors, zero
LaTeX warnings, zero **pdfTeX** warnings, zero overfull/underfull boxes.
(See "Repairs after review R1" at the end: the first version of this file
claimed zero warnings without mentioning 97 pdfTeX duplicate-destination
warnings; those are now eliminated.)

The whole Markdown was read first, including the withdrawal ledger (§13) and
the closing notes (§14), so that only the **final** state of each statement was
converted.

---

## (a) Included statements, with their LaTeX labels

| LaTeX label | environment | Markdown origin |
|---|---|---|
| `prop:carrier` | Proposition 2.1 | §1.2 (Paper 43 Lem 3.3, Cor 3.4) — cited |
| `prop:trace` | Proposition 2.2 | §1.2 (Paper 43 Def 8.5–8.6, 8A.7d) — cited |
| `prop:offidentity` | Proposition 2.3 | Paper 43 Thm 8.8 — cited |
| `prop:symbol` | Proposition 2.4 | Paper 43 Thm 9.7, (9.11), 9.7(d′) — cited |
| `prop:tate` | Proposition 2.5 | Paper 43 Thm 9.1, 9.12 — cited |
| `prop:rulings` | Proposition 2.6 | Paper 43 Thms 9.13(a), 9.14, 9.14a–c′ — cited (was Prop 8.3) |
| `prop:colimit` | Proposition 2.7 | Paper 43 Thm 8A.7c — cited |
| `rem:C1` | Remark 2.8 | §1.2 convention (C1) |
| `prop:indefinite` | Proposition 2.9 | Paper 43 Thm 14.1 — cited (was Warning 8.5) |
| `def:radial` | Definition 3.1 | Definition 3.1 |
| `prop:radalg` | Proposition 3.2 | Proposition 3.2 |
| `rem:typing` | Remark 3.3 | Remark 3.3 |
| `lem:profile` | Lemma 3.4 | Lemma 1.1 |
| `prop:primepacket` | Proposition 4.1 | Theorem 5.1 (+ Cor 5.2, Thm 4.1 folded into the surrounding prose) |
| `lem:radial-trace` | **Lemma 4.2** (Theorem A) | **Lemma 5.1a** |
| `prop:normalisation` | Proposition 5.1 | Theorem 6.1 |
| `cor:threenumbers` | Corollary 5.2 | Corollary 6.2 |
| `def:NGamma` | Definition 6.1 | Definition 7.1 |
| `prop:heattrace` | Proposition 6.2 | Theorem 7.2 |
| `prop:zetadet` | Proposition 6.3 | Theorem 7.3 |
| `rem:scope` | Remark 6.4 | the scope clause attached to Thm 7.3 |
| `thm:archsymbol` | Theorem 6.5 | Theorem 7.4 |
| `thm:archresidue` | **Theorem 6.6** | **Theorem 7.5** (archimedean Tate residue) |
| `rem:onepole` | Remark 6.7 | Remark 7.6 |
| `thm:polarpacket` | **Theorem 7.1** | **Theorem 8.1** (polar packet = hyperbolic form) |
| `rem:swap` | Remark 7.2 | Remark 8.2 (the swap), restated positively |
| `prop:live` | Proposition 7.3 | Proposition 8.3 + Corollary 8.4 |
| `lem:testfn` | Lemma 8.1 | Lemma 9.1 |
| `lem:contour` | Lemma 8.2 | Lemma 9.2 |
| `lem:reflection` | Lemma 8.3 | Lemma 9.3 |
| `thm:EF` | **Theorem 8.4** (Theorem B) | **Theorem 9.4** (explicit formula) |
| `cor:EFeven` | Corollary 8.5 | Corollary 9.4a |
| `rem:abs` | Remark 8.6 | Remark 9.8 |
| `rem:route` | Remark 8.7 | Remark 9.5 (+ a fourth item recording that no contour crosses a zero) |
| `def:weilform` | Definition 9.1 | §1.4 (S1) and (1.5)–(1.7) |
| `lem:traceweil` | Lemma 9.2 | Lemma 1.3, legs (S1),(S2) |
| `thm:comparison` | **Theorem 9.3** (Theorem C) | **Theorem 9.6** |
| `cor:c-unique` | **Corollary 9.4** (Theorem D) | **Corollary 9.6a** |
| `rem:loadbearing` | Remark 9.5 | Remark 9.6b(1),(2), restricted to what is proved |
| `thm:limitsymbols` | Theorem 9.6 | Theorem 9.6′ |
| `rem:notafunction` | Remark 9.7 | the two "not claimed" clauses of Thm 9.6′ |
| `rem:noposition` | Remark 9.8 | Remark 9.7 |
| (table, §9.4) | — | §9.6, order of limits (nine rows compressed to eight; rows 1–2 merged) |
| `lem:localsymbols` | Lemma 10.1 | Lemma 9bis.1 |
| `def:A` | Definition 10.2 | Definition 9bis.1a |
| `thm:residues` | **Theorem 10.3** (Theorem E) | **Theorem 9bis.2′** |
| `rem:collapses` | Remark 10.4 | Remark 9bis.2a |
| `rem:reflected` | Remark 10.5 | Remark 9bis.2b |
| `cor:noncommute` | Corollary 10.6 | Corollary 9bis.3 |
| `prop:mertens` | Proposition 10.7 | Theorem 9bis.4(iii) |
| `rem:mertens-scope` | Remark 10.8 | Theorem 9bis.4(ii) + the §11 deletion test |
| `rem:nomechanism` | Remark 10.9 | Remark 9bis.5 |
| `lem:Pi` | Lemma 11.1 | Lemma 10.1 |
| `cor:Pi` | Corollary 11.2 | Corollary 10.2 |
| `thm:sufficiency` | **Theorem 11.3** (Theorem F) | **Theorem 10.4** |
| `rem:sufficiency` | Remark 11.4 | Remarks 10.5, 10.6, restated as mathematics |
| `def:radsec` | Definition 12.1 | Definition 12.1 |
| `thm:radical` | **Theorem 12.2** (Theorem G) | **Theorem 12.2** |
| `rem:three` | Remark 12.3 | Remark 12.3 |
| `rem:nocolimit` | Remark 12.4 | Remark 12.4 |
| Appendix A | (E1)–(E8) | §11 import table, with book/section citations added |
| Appendix B | dependency summary | §14.3, reduced to "proved here / quoted" |

Requirement 1 is met: the title names the object constructed (an explicit
formula and a comparison theorem for the canonical trace on a correspondence
algebra of the idele class group); the Riemann hypothesis is named nowhere, and
Theorem F is stated purely as a theorem about a zero off the line
`Re s = 1/2`.

Language check: `grep -oiE "row [A-D]|phase|round [0-9]|builder|auditor|honest|
candidly|Riemann hypothesis|\bRH\b|W45\.|106_|P124|P123|D128|ledger"` over
`main.tex` returns nothing (the only hits for `classical` are the ordinary
English adjective).

---

## (b) Excluded, with reasons

1. **All status machinery.** Status labels (`PROVED`, `PROVED-IN-REPOSITORY`,
   `CLASSICAL`, `OPEN`), the status banner, §14.1/§14.1a decisions of record,
   §14.2 clause table, §2 acceptance contract, §14.5 cross-paper edit table,
   §15 numerical verification script. Not mathematics.
2. **The whole withdrawal ledger, §13 (W45.1–W45.16).** Every item is either a
   retraction of an object that no longer exists or a bookkeeping correction.
   The mathematical residue of W45.2, W45.4, W45.7–W45.9, W45.15, W45.16 is
   already carried by the statements that replaced them, which are included.
3. **Withdrawn statements named in the ledger**: old Theorem 4.2 and Lemma 4.1
   (the "two halves of the weight at different places"); old Theorem 5.4 and
   §§5.3–5.6, Cor. 5.5, Cor. 5.7 (corner strata); old Theorem 5.2 (the
   semilocal assembly); old Lemma 6.1's Arakelov reading and Remark 6.3; old
   §11 (the `n−1` obligation); old §12.1, Prop. 12.2, Thms 12.3, 12.5,
   Cor. 12.6; old Corollary 8.2's Hodge-index reading; old Theorem 9bis.2 and
   the name `T̂_∞^{mer}`. All refuted or referring to a withdrawn carrier.
4. **Remark 9bis.2b demoted.** Retained, but as a remark (`rem:reflected`) that
   explicitly says no statement rests on it — exactly its final status.
5. **§14.4 "row D's target" box** and the two inheritance discussions. Excluded
   per instructions; the standing negatives it quotes are kept as
   Proposition 2.9 and Remark 11.4.
6. **§5.1's discussion of what place-additivity is not**, §0.1–§0.2, §1.1 status
   labels, §1.2's provenance commentary, §12 Remark 12.4a (a forward reference
   to a later companion paper, phase 135), §12 Remark 12.5. Provenance, not
   mathematics. Remark 12.4a's content is a result of a *different* paper and
   is not claimed here.
7. **Dictionary 2 leg (S3)** (Paper 44's sign convention (8bis.14a),(8bis.14e))
   is not reproduced as a separate statement: it is a notational identification
   with a companion paper, and the mathematics it carries is
   Lemma 9.2 + Theorem 9.3. Legs (S1),(S2) are kept as Definition 9.1 and
   Lemma 9.2.
8. **Theorem 9bis.4(iv)** (the chart/colimit discontinuity of the ruling
   pairing) — a comparison of two quoted companion theorems with no proof of
   its own here; its content is quoted inside Remark 10.8 only to the extent
   needed.

---

## (c) Proofs judged incomplete in the Markdown — flagged, not silently completed

1. **Theorem 10.4 (sufficiency), Markdown §10.3 — repaired, not merely
   transcribed.** The Markdown proof is a *delta* against an external
   repository note (`106_11` Theorem 1): it says "run the construction with one
   change", states the real-linear surjectivity fix, and describes the tail
   absorption as "take `D ↦ D+2`". As written it is not a self-contained proof,
   and the requirement that nothing stated as a theorem be left unproved could
   not be met by transcription. I therefore **wrote the construction out in
   full** in Section 11 (Steps 1–8), reading the cited note for its content.
   Two presentational changes were needed and are recorded here:
   * the annihilating polynomial is taken as `Q(z) = P(z)P(−z)` rather than
     `P(z)` itself, so that it is manifestly real **and even** without having
     to argue about the parity of the multiplicity of a possible zero at
     `z = 0`. The cited note asserts evenness of its `Z_R` directly; that
     assertion is correct only if the multiplicity of `z = 0` in the divisor is
     even, which is not known. The symmetrised product avoids the issue at no
     cost (`Q(z_0) ≠ 0` still holds, since neither `z_0` nor `−z_0` lies in the
     annihilated divisor).
   * the primitivisation is absorbed as the explicit real even polynomial
     factor `(1/4 + z²) = s(1−s)` multiplying the transform, which makes the
     "`D ↦ D+2`" step of the Markdown a one-line degree count rather than a
     claim about somebody else's estimate.
   With those two changes the proof in `main.tex` is complete and uses only
   (E2)'s no-real-zero clause, (E3d) and (E6).

2. **Proposition 10.7 / Remark 10.8 (Mertens).** The Markdown's
   Theorem 9bis.4(ii) is a *citation* of Paper 43 Theorem 10.8b, not a proof;
   it is quoted as such in Remark 10.8 and is explicitly flagged there as
   quoted, with a deletion test showing that no other result depends on it.
   Part (iii) of the same Markdown theorem is a genuine computation and is
   proved in full as Proposition 10.7.

3. **Proposition 2.4(c) place-wise Plancherel.** Lemma 4.2 (Theorem A) needs
   the local form `W_v(H) = ∫ Ĥ Ŵ_v dχ`, place by place, on all of `D_A`. In
   the Markdown this is an amendment recorded mid-proof (the companion paper's
   Theorem 9.7(d′), added after the fact). It is quoted here as part of
   Proposition 2.4(c), and a reader should note that Lemma 4.2 rests on it.
   This is a dependence on a companion paper, not a gap in the present text,
   but it is the single load-bearing import of Theorem A and is flagged.

4. **Proposition 4.1 (the prime packet).** Lemma 4.2's proof re-uses *step (i)*
   of the cited companion proof (vanishing of the unit packet on radial
   classes) outside the hypothesis under which that proof is stated. The
   Markdown makes exactly this argument and it is correct — step (i) uses
   radiality only — but it is an appeal to the internals of a cited proof
   rather than to its statement. Flagged.

5. **Remark 7.2 (the swap).** The Markdown justifies the existence of a real
   compactly supported `F` with prescribed `Φ_F(0), Φ_F(1)` by citing the
   surjectivity of `M`. In the LaTeX the counterexample was dropped and the
   remark restated positively (`M(Γ_F) = σ(Φ_F(0), Φ_F(1))`, with the
   `σ`-invariance of `β_T` proved inline), so no such existence claim is made.

No other statement carried into `main.tex` was judged to have an incomplete
proof.


---

## Repairs after review R1

Applied to `main.tex` in response to `TEX_HOSTILE_REVIEW_R1.md`
(verdict MAJOR REPAIRS NEEDED: 4 MAJOR, 12 MINOR). All 16 findings applied.
Line numbers below are those of the **repaired** file.

### MAJOR

| finding | change | line(s) |
|---|---|---|
| **2.3 / 3.1** — `A` "has exactly two poles" is false and stronger than the proved statement | abstract now reads "exactly two poles in `{0,1}`, both simple and each of residue `1`"; Theorem E in the introduction likewise, with the added clause "its remaining poles are the zeros of `ξ`, contributed by `−ξ'/ξ`"; the §10.2 heading is now "The continued symbol and its poles at `s=0` and `s=1`". The theorem body (Thm 10.3(ii)) already said "in `{0,1}`" and is unchanged, so the paper now agrees with `main.md` Thm 9bis.2′(ii) everywhere. | 77–78, 190–193, 1694 |
| **2.1** — Proposition 7.3 had neither proof nor citation | the environment now carries the bracketed header `[\cite{P43}, Theorems 9.13(a), 9.14a–9.14c′ and Definition 9.14c0]`, the `L¹`-mass clause cites Definition 9.14c0 explicitly, and a one-line proof ("the three assertions are, in order, …; quoted verbatim") was added. Nothing was demoted, so no dependency changed. | 985–1003 |
| **2.2** — the place-wise Plancherel import was cited to the wrong number | Proposition 2.4's header is now `[\cite{P43}, Theorem 9.7, equation (9.11), Theorem 9.7(d′)/(9.13′), and (14.2)]`, and part (c) ends with "The place-wise form is \cite{P43}, Theorem 9.7(d′), equation (9.13′); Lemma 4.2 and Theorem 12.2 rest on it." This is the single load-bearing import flagged as item (c)3 above. | 359–360, 384–386 |
| **2.4** — Step 2 of the sufficiency proof invoked (11.6) with `M=0` | replaced by `M=1`, with the bound written out: "(11.6) with `M=1` gives `|D(z)| ≤ C₁/(1+|Re z|)` in the strip `|Im z| ≤ 1/2`, so that `|D(z)| → 0` as `|Re z| → ∞` there", which is what (11.7) needs. | 2037–2040 |

### MINOR

| finding | change | line(s) |
|---|---|---|
| **1.1** | deleted the unused `problem` and `conjecture` theorem environments from the preamble | 19–20 (deleted) |
| **1.2** | removed the audit-register clauses: "quoted here once and for all, as a standing caution"; "the negative half … recorded as strongly as the positive half"; Remark 9.5's "should be read as saying two things at once"; Remark 10.8's "deletion test" phrasing (the mathematical content — no positivity claimed, (E8) used exactly twice, nothing else depends on it — is kept in every case) | 460–461, 767–768, 1514–1519, 1888, 2386 |
| **2.6** | Corollary 8.5 no longer claims (8.2) for the single transform `Φ_h`; it now cites the bound `|g| ≤ C₄e^{2T|σ−1/2|}|s−1/2|^{−4}`, which is (8.1) with `N=4`, and says that this is all the horizontal estimate of Lemma 8.2 uses | 1316–1321 |
| **2.7** | Remark 8.6's decay bound is now stated for `|γ_ρ| ≥ 1`, with the finitely many zeros of smaller ordinate handled separately (`Φ_h` entire, count finite by (E3d)) | 1327–1334 |
| **2.8** | Step 8: "Fix `N_0` so large that" → "Fix any integer `N_0 ≥ 1`", with the convergence of `Σ_0` deduced from (11.6) for large `M`; and the sentence "`|D(−z)| = |D(z)|` because `φ` is even, so that (11.7) applies to both factors" inserted before the tail display | 2145–2158 |
| **2.9** | Theorem 12.2's last clause is now proved: the two functionals `h ↦ ∫he^{t/2}`, `h ↦ ∫he^{−t/2}` are linearly independent on `C_c^∞(R)`, so `M` restricted to the radial sector is onto `B_T`; the text notes that Proposition 2.5 gives a different statement (surjectivity on all of `D_A`) | 2214–2215, 2257–2267 |
| **2.10** | the proof of Lemma 4.2 no longer imports step (ii) from inside a cited proof: the shell computation is now carried out inline from `τ_p ≡ p^{−|k|/2}` (\cite{P43}, Lemma 8.2(i)), `|j_p(p^k u)|_S = p^{−k}` and `vol(p^kZ_p^×) = log p`, with the display. The reference to "step (i)" was also removed — that step is derived inline as well — so the lemma now imports only *statements* | 683–698 |
| **2.11** | Appendix B: Theorem 6.5 moved from "proved here" to the quoted list, with the note that only the constant reconciliation `γ+log4π+ψ(1/2)=log π` is proved here | 2408, 2420–2422 |
| **3.2** | Proposition 2.4(d)'s numerical lower bound now cites \cite{P43}, equation (14.2) | 389 |
| **4.1** | the 97 `pdfTeX warning (ext4): destination with the same identifier` warnings are gone: `hyperref` is loaded with `hypertexnames=false`, so the hand-written `\tag`s no longer collide with the independently running `equation` counter. Verified: `grep -c 'pdfTeX warning' main.log` = 0 | 8 |
| **5.1** | deleted the reader-instruction framing: "It is worth stating explicitly that"; "For the reader's convenience we tabulate"; "For the reader's orientation we record"; "computations recorded for orientation"; "a consistency check rather than a discovery". The mathematical statements they framed are kept verbatim | 802–803, 845–846, 969–974, 1600–1602, 2403 |
| **5.2** | "Theorem 8.4(b),(c)" → "steps (b) and (c) of the proof of Theorem 8.4", in the order-of-limits table | 1624–1626 |

### Compile after repairs

`pdflatex -interaction=nonstopmode main.tex`, three passes (the table of
contents changed): **0 errors, 0 LaTeX warnings, 0 pdfTeX warnings, 0
overfull/underfull boxes, 31 pages.**

### Findings not requiring a change

Review items 2.5 (independent verification of Theorem B against the classical
Weil formula, of the residue computations, and of Steps 1–8 of Theorem F) and
§§3(b), 5 record verifications, not defects. Review item 5.1's list also
included Remark 10.9's opening "It is tempting to imagine", which is a
statement about a mechanism that does not exist, i.e. mathematics, and was
left.
