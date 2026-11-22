# R135.005 — Confirmation of round 2 (phase 135), Paper 47 Part II §§11–16

Object: `04-papers/47-intersection-frame-defect/archive/main.md` lines 1856–3748 (Part II after the
round-2 repairs of `R135_004`), the two `[phase 135]` remarks in
`04-papers/45-row-c-explicit-formula/main.md` (Remark 12.4a, line ~1923) and
`04-papers/43-row-a-torsion-theory/main.md` (Remark 14.1a, line ~5125), against
`R135_002` (M1–M17), `R135_003` §2/§4 (LF1–LF7 and the ruling), `R135_004`
(claimed repairs), Paper 45 Theorem 10.4 (lines 1680–1758) and the repository
construction `106_11` ((14)–(16), (27)–(30)).

All quotations verbatim. No paper was edited. The two `--fast` script modes were
run once each (results in §E); nothing longer was rerun.

---

## (A) Per-finding verdicts

| finding | verdict | evidence |
|---|---|---|
| **M1** `FATAL` (Cor 12.4a a non-sequitur; hypothesis class everything) | **repaired, with one live residue → N4** | Line 2869 ff.: "**Restatement 12.4a … `RESTATEMENT (schema)`**"; the data list is now the display (12.3) at 2890–2891 and line 2893 says "— **`Z` itself is not among them** —"; the statement is a genuine conditional ("**if** properties (a),(b′),(c) are **derived** … from a derivation that uses only (12.3) … **then** the same derivation, read for `Z = Ξ_a`, yields … contradicting Theorem 12.4.  Hence **no such derivation exists.**", 2896–2900). Remark 12.4a′ (2907) states correctly that it "does **not** exclude any function `h⁰`". Downstream: Remark 12.4b → `HEURISTIC` (2917); Theorem 13.3 → **Restatement 13.3** (3135) with the quantified form withdrawn in a boxed note (3147–3157) and reopened as item (22); Theorem 13.7 → **Remark 13.7 (`HEURISTIC`)** (3380); §14.5 rewritten (3605 ff.); the two round-1 sentences at lines 1446 and 1610 are struck in place. **Residue:** §10, line 1813, still asserts the withdrawn claim (N4) |
| **M2**/LF3 (`F⋆G^∨` not even) | **repaired** | Definition 11.4 (2043) is now by polarization, `Q(X) := ⟨X⋆X^∨,W+ω⟩`, `I_∞ := ¼[Q(F+G)−Q(F−G)]` (11.5); the false parenthetical is deleted and quoted as false in the repair note (2046–2048). Lemma 11.4a (2063) proves the three descriptions agree. *Checked independently:* `Q(X) = 2Φ_X(0)Φ_X(1) − Σ_ρΦ_X(ρ)Φ_X(1−ρ)` follows from (11.4) with `Φ_{X⋆X^∨}(s)=Φ_X(s)Φ_X(1−s)`; its polarization is `Φ_F(0)Φ_G(1)+Φ_F(1)Φ_G(0) − Σ_ρ½[Φ_F(ρ)Φ_G(1−ρ)+Φ_F(1−ρ)Φ_G(ρ)]`, which equals (11.6) after the re-indexing `ρ↦1−ρ` in the absolutely convergent sum; and `Φ_{h_{ev}}(s)=½[Φ_F(s)Φ_G(1−s)+Φ_F(1−s)Φ_G(s)]` gives the same at `s=0,1` and at the zeros. All three agree. Theorem 11.5 now says "**no evenness assumed**" (2084). Costs no theorem, as predicted |
| **M3** (multiplicity vs distinct zeros) | **repaired** | 2412–2420 quotes the defect and 2422–2441 replaces the count: `N_dist(r) ≥ (2/5)·2N(r)(1+o(1)) = (2/(5π))r\log r(1+o(1)) ≤ n_N(r) = O(r)`. *Arithmetic checked:* `(4/5)·(r/2π)\log r = (2/(5π))r\log r` ✓. Import (X18) (Conrey 1989, Levinson as fallback) added to §15 at 3702 and correctly described there as what (X14) does **not** give. Propagation verified verbatim in P45 Remark 12.4a and P43 Remark 14.1a; both are accurate and both say the conclusion is unchanged |
| **M4**/LF1 (Prop 12.6 excludes `Ξ_a`) | **repaired** | (12.4) at 2985: "every zero `ρ` of `Z` satisfies `\|\mathrm{Re}\,ρ−½\| ≤ θ`", with the note (2987–2994) stating the defect and that for `Ξ_a` it reads `≤ ½+a = θ`. Laplace abscissa now `\mathrm{Re}\,s > ½+θ` in proof step (b) (3074–3079), explicitly "**not on `\mathrm{Re}\,s > 1`**". Poles-not-zeros: step (b)(3) proves `Z(p) > 0` from `P ⊂ R` and `Z > 0`, and says for `Ξ_a` it is `ξ(2a) ≠ 0`, `ξ(1−2a) ≠ 0`, "here **proved**, not imported" |
| **M5** (`PROVED` on an announced re-reading) | **repaired**, modulo N3 | 3035–3039 quotes the round-1 closing line and replaces it; 3041–3049 **lists** the verbatim statements; 3053–3100 **proves** the three non-verbatim ones (contour abscissa `(½+θ,1+θ+ε)` nonempty; Lemma 11.9's exponents/half-plane/separation; Theorem 11.14's weight). The contour argument is correct: `Σ_{n≤x}c_n = O(x^{½+θ})` forces `c > ½+θ`, holomorphy forces `c < 1+θ+ε`. **But** the verbatim list wrongly includes Theorem 11.12 (N3) |
| **M6**/LF2 (Thm 10.4 analogue in a parenthesis) | **repaired**, with two unverified lines (N5) | Lemma 12.4A (2730) and Proposition 12.4B (2789) are written out; Theorem 12.4's parenthesis is gone and replaced by a citation (2862). *Checked independently:* `Π_P = (∂²−c_1²)(∂²−c_2²)` has symbol `[(z+½)²−a²][(z−½)²−a²] = (z²−c_1²)(z²−c_2²) = π_P(s)`, `z=s−½` ✓; `π_P(1−s)=π_P(s)` ✓; `Φ_{G_c}(s) = (c²−(s−½)²)^{−1}` on `\|\mathrm{Re}\,s−½\|<c` ✓; the two boundary evaluations in (iii) are `Φ_F(1−a)` (right) and `Φ_F(a)` (left), both in `P` ✓; `c_2²−c_1² = −2a ≠ 0` ✓; (v) `Ξ_a(σ)=∫K_ae^{(σ−½)t}dt>0` ✓. In Prop 12.4B the `106_11` variable is checked correctly: `z=(ρ−½)/i = γ + i(½−β)`, so `x_0=γ_0`, `y_0=½−β_0`, and `x_0≠0` is now **proved** from `Ξ_a`'s having no real zero rather than imported from (E2)'s last clause — this is precisely the check round 1 omitted, and it is made. (E6), (E3d) and the `D ↦ D+4` bump are stated. See N5 for what is still not checked |
| **M7** (zero generators) | **repaired** | (13.1) at 3185 is indexed by prime powers `q=p^k`, `w_q := Λ(q)q^{−1/2} = (\log p)p^{−k/2} > 0`; Theorem 13.5(i)'s proof now closes with "`w_q > 0` on the index set, so every `a_q = 0`" (3234); `Λ_1` re-indexed the same way; the repair note (3200–3212) states all three round-1 failures. `h0_candidate.py --fast` prints `index set (prime powers q <= 5)` ✓ |
| **M8**/LF4 (Thm 13.6's proof not a proof) | **repaired**, and honestly | Round 1's (13.4-r1) is **withdrawn in full** in a boxed note (3332–3350) that reproduces the vacuous inequality and names both asserted steps. Replacements checked line by line: **Lemma 13.5a** — recession cone of a closed convex `C(Q) ∋ 0` is `{x : λx ∈ C ∀λ>0}` ✓; `K+λN ≥ 0`, divide by `λ`, `λ→∞` ⟹ `N ≥ 0` ✓; `N ∈ 𝓝_∞` ⟹ `\deg N = 0` ⟹ `N ≡ 0` ⟹ `x = 0` by Theorem 13.5(i) ✓; trivial recession cone ⟹ bounded ✓; box count `#(Z^Q ∩ mC(Q)) ≤ (2mρ_Q+1)^d` ✓ — **the recession-cone argument is correct and the box count is right**. **Lemma 13.5b** — `Φ_E(σ) = ξ(σ)[m+σ(1−σ)Σ_qa_qw_qq^{σ−1/2}]` ✓; `ξ(σ)>0` from `K>0` ✓; as `σ→+∞` the largest prime power dominates and `σ(1−σ) ∼ −σ²`, forcing `a_Qw_Q ≤ 0`, hence `a_Q ≤ −1` ✓; `σ=½` gives `Σa_qw_q ≥ −4m` ✓. **Theorem 13.6** now says "on every finite truncation" in its title and "**the truncated candidate does not satisfy (c)**" in (ii); the full lattice is `OPEN` as item (23), repeated in Remark 13.6b, in the withdrawal table and in §14.5. **The labelling of the full lattice as OPEN is honest.** Remark 13.6b does **not** overclaim as a whole — it argues "should not be expected", not "false" — but see N6 for its one slipped estimate |
| **M9** (archimedean kernel not licensed on `D^W`) | **repaired**, modulo N1 | Theorem 11.14 (2492) is re-proved on the spectral side: (11.16) `w_F(u) = Φ_F(1)e^{−u/2}+Φ_F(0)e^{u/2}−Σ_ρe^{(ρ−½)u}Φ_F(1−ρ)`. *Checked:* this is exactly (11.6) with `Φ_E(0)=∫Ee^{−u/2}`, `Φ_E(1)=∫Ee^{u/2}`, `Φ_E(ρ)=∫Ee^{(ρ−½)u}` ✓. **The interchange is justified**: `\|e^{(ρ−½)u}\| ≤ e^{\|u\|/2}` from `0<\mathrm{Re}\,ρ<1` alone, `∫\|E\|e^{\|u\|/2}<∞` from (11.1), `Σ_ρ\|Φ_F(1−ρ)\| ≤ C_2(F)Σ\|γ_ρ\|^{−2} < ∞` from (11.2)+(E3d) ✓ (the needed uniformity of `C_2(F,σ)` over `σ ∈ [0,1]` is immediate from `∫\|F''\|e^{\|t\|/2}<∞` but is not said). So **`\|I_∞(E,F)\| ≤ C_F\deg E` for `E ≥ 0` does follow using only `0 < \mathrm{Re}\,ρ < 1` and absolute convergence, and `C_F` is finite and explicit** — the constant as displayed is wrong by a factor `2` (N1). The kernel route is demoted to Remark 11.14a′ (2556), explicitly "**nothing below uses this remark**"; open item (21) records the unproved kernel representation; (X15) is marked unused in §15 |
| **M10** (sign of the bracket) | **repaired** | 2005–2011: "the prime sum of the last line minus the archimedean integral of the previous one (`\mathrm{PRIME} − \mathrm{ARCH}`)", with the round-1 reading quoted and corrected |
| **M11** (§1.13 falsified) | **partially repaired → N7** | §1.13 amended at 175–188 with a list of the classical zero-location data used in Part II ((E2), (X16), (X18)). But the "stronger rule" the amendment substitutes is itself false (N7), the list misattributes (E2) to Lemma 12.4A and omits Theorem 11.14, and §10's parallel compliance sentence was not amended |
| **M12** (`T_∞(K)`) | **repaired** in the paper | `grep 'T_∞(K)'` returns only the repair note (2184, 2186) and the blueprint-quotation row (3549). Theorem 11.8(ii) and the numerics line now read `⟨K,W_{fin}+ω_∞⟩`. *Not done:* the phase README still writes `T_∞(K) = 1` in the `polya_class.py` row |
| **M13** (two slips in (S1)–(S3)) | **repaired** | (S2) at 3008–3013 records the factor `2` and ties it to Theorem 11.8(v); (S3) at 3014–3019 is `½+θ < c < 1+θ+ε` with the reason |
| **M14** (`Π(D^W∩C⁴)`) | **repaired** | Lemma 11.2(ii) at 1934: `Π(D^W_4) ⊆ D^W` with `D^W_4` defined by (11.1) for `j ≤ 4`, and the note gives `(Πg)'' = −g''''+¼g''` ✓ |
| **M15** (`\log\#∅`) | **repaired as to the convention; the second half overshoots → N2** | 3196 "with the **convention** `h⁰_{\mathbb Z}(E) := 0`"; 3214–3218 states it is a choice, not forced. Remark 13.5c (3241) records (b′) "only on `{\deg>0}`" — but its conclusion that the candidate therefore already fails (b′) is **false** (N2) |
| **M16** (one-directional, satisfiability) | **repaired** | Open item (20) at 3639–3644; §14.5's closing paragraph (3684) states the deliverable as "a **reduction of unknown satisfiability**"; the auditor's own words from M16 are used |
| **M17** (X12 normalization) | **recorded** | §14.4a row (3582); the Titchmarsh citation is unchanged and still the sole evidence for evenness — acceptable now that positivity is proved in-paper |
| **LF1** | = M4, **repaired** | |
| **LF2** | = M6, **repaired** modulo N5 | |
| **LF3** | = M2, **repaired** | |
| **LF4** | = M8, **repaired** | |
| **LF5** | = M1, **repaired** (label is `RESTATEMENT (schema)`) | |
| **LF6** | **repaired** | 2115–2120: each term is `2πn²e^{5u/2}e^{−πn²e^{2u}}(2πn²e^{2u}−3)` and `2πn²e^{2u} ≥ 2π > 3` for `u ≥ 0`, `n ≥ 1`. *Checked:* `4π²n⁴e^{9u/2} − 6πn²e^{5u/2} = 2πn²e^{5u/2}(2πn²e^{2u} − 3)` ✓. Only evenness and the Fourier identity remain imported |
| **LF7** | **repaired** | Remark 14.5a (3664), `HEURISTIC`, with (14.2) and the explicit disclaimer "This is a direction, not a claim, and it is not evidence for any sign" |

**Count: 22 of 24 fully repaired; M11 partially; M15 partially (its second clause).**

---

## (B) New findings

### N1 — `MINOR` (load-bearing constant) — the two factors `½` in (11.17) do not follow from its own proof, and are wrong

Line 2505–2506:

> `C_F ≤ \tfrac12(|Φ_F(0)|+|Φ_F(1)|) + \tfrac12\,Σ_ρ|Φ_F(1−ρ)| < ∞`

Line 2525–2527 proves it by: "`e^{\pm u/2} ≤ 2\cosh(u/2)` and
`|e^{(ρ−½)u}| ≤ e^{|u|/2} ≤ 2\cosh(u/2)`; divide (11.16) by `2\cosh(u/2)` and
take absolute values". That yields coefficient **`1`**, not `½`. And `1` is
sharp: `e^{−u/2}/(e^{u/2}+e^{−u/2}) → 1` as `u → −∞`, and likewise
`e^{|u|/2}/2\cosh(u/2) → 1`. So the displayed constant is a factor `2` too
small, and it is used in Theorem 12.3 Step 1 to choose `m > C_F` — a too-small
`C_F` breaks ampleness of `H' = F+2mK`, which Step 2 needs.

*Minimal repair:* delete both `½`'s, i.e.
`C_F ≤ |Φ_F(0)|+|Φ_F(1)| + Σ_ρ|Φ_F(1−ρ)|`. Nothing else changes (only
finiteness is used downstream). While there, say that `w_F` is real because
`Φ_F(1−\barρ) = \overline{Φ_F(1−ρ)}` for real `F` and the zero multiset is
conjugation-invariant — asserted at 2496–2497, not shown.

### N2 — `MAJOR` (a false negative claim, propagated three times) — (b′) **does** hold for `h⁰_{\mathbb Z}`; Remark 13.5c is wrong

Line 3241–3245:

> **Remark 13.5c** … (b′) is verified only on `\{\deg > 0\}`.  So
> `h⁰_{\mathbb Z}` is **not** a candidate satisfying (a)+(b′)+(c) even before
> any growth estimate

The inference "not verified ⟹ fails" is invalid, and here the conclusion is
also false. If `h⁰_{\mathbb Z}(E) > 0` then `\#H⁰_{\mathbb Z}(E) ≥ 2`, so there
are `λ_1 ≠ λ_2 ∈ Λ_W` with `E+λ_i ≥ 0`. Since `Λ_W ⊂ 𝓝_∞`,
`\deg(E+λ_i) = \deg E`. If `\deg E < 0` then `H⁰ = ∅` (Theorem 13.5(iii)); if
`\deg E = 0` then each `E+λ_i` is a nonnegative continuous function of degree
`0`, hence `≡ 0` (Theorem 11.13(i)), forcing `λ_1 = λ_2 = −E` and
`\#H⁰ ≤ 1`, i.e. `h⁰_{\mathbb Z}(E) = 0`. Therefore
`h⁰_{\mathbb Z}(E) > 0 ⟹ \deg E > 0 ⟹ E' ≢ 0`, and **(b′) holds
unconditionally** for this candidate.

*Propagated to:* Theorem 13.6(ii)'s clause "and by Remark 13.5c it does not
satisfy (b′) off `\{\deg > 0\}` either" (3326–3327); §14.5 item **(3)**, "and
fail (b′) off `\{\deg > 0\}` (Remark 13.5c)" (3620–3621); §14.4a's M15 row,
"so the candidate fails before any growth estimate" (3580).

*Minimal repair:* replace Remark 13.5c by the proof above — (b′) **holds**, and
the only failure is (c), on every finite truncation — and delete the three
propagated clauses. (This makes §13 *stronger*, not weaker: the candidate is a
genuine (a)+(b′) candidate that fails only the Riemann–Roch inequality.)

### N3 — `MINOR` — Proposition 12.6's "verbatim" list includes Theorem 11.12, whose repaired proof is `ζ`-specific

Line 3046 lists "Theorems 11.12, 11.13" among the statements holding for every
admissible `Z` "with no step that mentions `θ` or `P` other than by name". But
Theorem 11.12 as repaired in round 2 runs on import **(X18)**, Conrey's
positive proportion of simple zeros **of `ζ`**. Nothing in Proposition 12.6's
hypothesis list on `Z` supplies a lower bound `≫ r\log^δ r` for the distinct
zeros of `Z`, so the claim is false for a general admissible `Z`. (For `Ξ_a` it
is true — the distinct zeros of `Ξ_a` contain the shifted distinct zeros of
`ξ` — but that is a one-line argument, not verbatim reading.)

*Mitigating:* nothing uses Theorem 11.12 for `Ξ_a` — Theorem 12.4 goes through
Theorem 12.3, whose quantitative inputs are Theorems 11.8, 11.11, 11.13, 11.14,
as Proposition 12.6 itself says at 3048–3049.

*Minimal repair:* move Theorem 11.12 out of the verbatim list into a fourth
"not verbatim" item, with the shifted-zeros argument for `Ξ_a`, or add the
distinct-zero density to the hypotheses on `Z`.

### N4 — `MAJOR` (label honesty) — §10, the paper's **label** section, still carries the claim withdrawn under M1

Line 1810–1814:

> together with Theorem 12.4, which proves those three properties
> **inconsistent** for the falsifier `Ξ_a`, so that **any `h⁰` must use the
> Euler product**.

That consequent is exactly what Restatement 12.4a no longer says and what
Remark 12.4b is demoted to a `HEURISTIC` about. `R135_004` §1 lists the
corrections made at line 1446, §9.1(3), Proposition 12.5 and §14.5; it did not
reach §10, and the two struck occurrences elsewhere (1446, 1610) are inside
withdrawal brackets while this one is live text in the section that states the
paper's label.

*Minimal repair:* one sentence — "…inconsistent for the falsifier `Ξ_a`, so
that no **model-free proof** that some `h⁰` works can exist (Restatement 12.4a,
a schema about derivations); whether the Euler product must enter the
*definition* is not proved and survives only as the heuristic Remark 12.4b."

### N5 — `MINOR` — Proposition 12.4B does not widen `106_11`'s strip, and the `D ↦ D+4` bump is still argued rather than re-derived

`106_11`'s estimates are all stated on the strip `|\Im z| ≤ 1/2`: (15)
`\sup_{|\Im z|≤1/2}(1+|\Re z|)^M|Φ(z)| < ∞`, (16) the choice of `R` from that
uniform strip decay, and (27) `|F_{N,±}(z)| ≤ C_R(1+|z|)^D(|Φ(z)|/|Φ(s_0)|)^N`
"for `|\Im z| ≤ 1/2`". That half-width is `\max_ρ|\mathrm{Re}\,ρ − ½|` for
`ξ`. For `Ξ_a` it is `½+a`, so (15), (16), (27), (29) must be re-read on
`|\Im z| ≤ ½+a`. Proposition 12.4B (2829–2845) checks Paley–Wiener, the
counting import and the polynomial degree, and does **not** mention the strip.
The substitution is true — `Φ = \hatφ` with `φ ∈ C_c^∞` satisfies (15) on every
horizontal strip — but it is unstated, and it is the one hypothesis of
`106_11`'s proof that the change of model actually touches.

Separately, its own weak point 6 stands: "the degree bump `D ↦ D+4`
… was not re-derived from `106_11` (27)–(30) line by line". The pattern is at
least consistent (`|ρ(1−ρ)|² = O(|ρ|^4)` ↦ `D+2`; `|π_P(ρ)|² = O(|ρ|^8)` ↦
`D+4`), and (27) is indeed organised around a fixed `D`, but it is asserted.

*Minimal repair:* add one clause — "and (15),(16),(27),(29) of `106_11` are
re-read on `|\Im z| ≤ ½+a`, which is legitimate because `Φ = \hatφ`,
`φ ∈ C_c^∞`, obeys (15) on every horizontal strip" — and either re-derive
(29) with `D+4` or label that line `CANDIDATE`.

### N6 — `NOTE` — Remark 13.6b's "`O(1/q)`" is not right, and the remark's status is unlabelled

Line 3354–3357: "Two generators at **adjacent** prime powers `q < q'` … differ
by a translation of `\log(q'/q) = O(1/q)`". Consecutive prime powers differ by
`q'−q ≍ \log q` on average and by more infinitely often, so
`\log(q'/q) = O((q'−q)/q)` is `O(\log q/q)`, not `O(1/q)`; and the difference
`w_{q'}τ_{\log q'}(ΠK) − w_qτ_{\log q}(ΠK)` also carries the change of weight
`w_{q'} − w_q`, which is not small relative to `w_q`. The *conclusion* (that
single-point evaluation cannot bound the coefficients, and that `B(m) = O(m)`
should not be expected) is unaffected — near-degeneracy only needs
`\log(q'/q) → 0` — but the remark reads like an estimate and is not labelled
`HEURISTIC`, unlike Remarks 12.4b, 13.6a, 13.7 and 14.5a.

*Minimal repair:* `O(\log q/q)`, or simply `o(1)`; and label the remark.

### N7 — `MINOR` (label honesty) — §1.13's replacement rule is itself falsified, and its list is inaccurate

Lines 185–188 substitute, for the falsified compliance claim, "the stronger and
more useful one: **no statement about the location of the zeros of `ζ` is
proved, asserted or conjectured anywhere in this paper, and no object is
defined by the location of a zero.**" The second clause holds (see §C). The
first does not: **Lemma 13.5b** proves "`ξ(σ) = Φ_K(σ) > 0` for every real
`σ`" (3298–3299), which *is* a statement about the location of the zeros of
`ζ` — it is (E2)'s last clause — and **Lemma 12.4A(v)** proves "no zero of
`Ξ_a` is real" and leans on it. Both are classical, unconditional, and proved
here from `K > 0`; that is a virtue, not a defect, but the rule as worded is
false. Two further inaccuracies in the same amendment: it attributes `ζ(σ)≠0`
on `(0,1)` to "Proposition 12.4A" (it is **Lemma** 12.4A, and 12.4A/12.4B are
precisely the statements that *avoid* importing it, proving the analogue
instead), and it omits **Theorem 11.14**, whose repaired proof uses
`0 < \mathrm{Re}\,ρ < 1` twice.

*Minimal repair:* "…no statement about the location of the zeros of `ζ` beyond
the classical unconditional facts listed here — all of them either imported or
proved from the positivity of Pólya's kernel — is proved, asserted or
conjectured…", and correct the two list entries.

### N8 — `NOTE` — small ledger inconsistencies

* Theorem 12.3's hypothesis line (2639–2640) still carries "(X12)–(X15)";
  (X13),(X14) serve only Theorem 11.12 and (X15) serves nothing (§15, 3701).
* §14.4a's numerics row says `canonical_pairings.py --check` "exits `0` in
  26 s"; §16 and `R135_004` §3.2 say 28 s.
* §15 lists (X18) between (X15) and (X16).
* M12 was not carried into the phase `README.md`, whose `polya_class.py` row
  still advertises "`T_∞(K) = 1`".
* Restatement 13.3 is a pure specialization of Restatement 12.4a and adds no
  content beyond it; Remark 13.3a says as much, so this is a presentational
  note only.

---

## (C) Sign / RH sweep of the round-2 material

| where | new text | verdict |
|---|---|---|
| Lemma 11.4a, Thm 11.5 (2063–2097) | polarization identity (11.5a), (11.6) off the diagonal | identities; no inequality, no zero location. **Compliant** |
| Thm 11.14 (2492–2533) | `w_F`, `C_F`, `\|I_∞(E,F)\| ≤ C_F\deg E`, `2K` and `F+2mK` ample | positivity of the form on the **effective** cone only, from `0<\mathrm{Re}\,ρ<1` (Chebyshev-trivial) and `\deg E > 0`. Not a statement on the primitive sector. **Compliant**, and it survives `Ξ_a` (Prop 12.6(c)) |
| Lemma 12.4A(v) (2750–2752, 2782–2786) | `Ξ_a(σ) > 0` on `R`; no `p ∈ P` is a zero; no zero of `Ξ_a` is real | a statement about the zeros of **`Ξ_a`**, proved from `K_a > 0`. Classical in content, unconditional, used only as data. **Compliant**, but it is a zero-location statement: §1.13 must say so (N7) |
| Prop 12.4B (2789–2853) | "if `I_∞^{(a)}(F,F) ≤ 0` … then every zero of `Ξ_a` lies on `\mathrm{Re}\,s = ½`" | about `Ξ_a`, a function known to have off-line zeros. The direction is the contrapositive of Paper 45 (1.10) and is correctly oriented. **No sign claimed for `ξ`.** Compliant |
| Thm 12.4 (2855–2867) | non-existence of `h⁰_a` for `Ξ_a` | unchanged from round 1; uses Hardy (X16) about `ζ`, listed in §15 and §1.13. Compliant |
| Restatement 12.4a, Rem 12.4a′, 12.4b (2869–2940) | schema about derivations; "does **not** exclude any function `h⁰`" | **the round-1 danger is gone.** The statement no longer asserts unsatisfiability of Theorem 12.3's hypotheses, and §14.5 records satisfiability as `OPEN` (20). Compliant |
| Prop 12.6 (12.4) (2977–2994) | `\|\mathrm{Re}\,ρ−½\| ≤ θ` | a **hypothesis on `Z`**, verified for `ξ` and `Ξ_a` from (E2); explicitly "imported data, not a claim". Compliant |
| Lemma 13.5a, 13.5b (3247–3307) | `C(Q)` bounded; `Φ_E(σ) ≥ 0`; `a_Q ≤ −1` | inequalities about **lattice coefficients**, from `E ≥ 0` and `ξ > 0` on `R`. No zero of `ζ` enters. Compliant |
| Thm 13.6 (3309–3330) | (c) fails on every finite truncation | a refutation of a candidate, not a sign. Compliant |
| Rem 13.7, Rem 14.5a (3380–3395, 3664–3682) | unimodularity direction; `Frob_m ⋆ Frob_n^†` | both `HEURISTIC`, both say "not a theorem" / "not evidence for any sign". Compliant |
| §10, line 1813 | "so that any `h⁰` must use the Euler product" | **not a sign**, but a withdrawn claim left live. N4 |
| §14.5 closing (3684–3690) | "a **reduction of unknown satisfiability**" | the honest statement M16 asked for. Compliant |

**No unconditional sign appears anywhere in the round-2 material.** Grepped
`RH` over lines 1856–3748: five occurrences, all inside Theorem 12.3's
conditional conclusion, its proof, or open item (20).

**No new statement that with Theorem 3.7 would decide RH.** Theorem 12.3 is
unchanged and remains conditional on `h⁰`; Proposition 12.4B and Theorem 12.4
concern `Ξ_a` only; Lemmas 13.5a/13.5b are about a lattice; Restatement 12.4a
is about derivations. The boxed target of §0.1 and the label of §10 (**None**)
are unchanged.

**No new use of zeros' location as a definition.** `𝓝_∞` is still the radical
(Theorem 11.11) and only *characterized* through the zeros; (11.13) still
refuses the identification; (12.4) is a hypothesis on `Z`, not a definition;
(12.3)'s data list now excludes `Z` itself and mentions no zero; `Λ_W` is
indexed by prime powers and `C(Q)` by pointwise nonnegativity. **No circularity
found.**

---

## (D) Verdict

**Part II is now fit to stand as a reduction theorem with no sign, subject to
two repairs, both of one line.**

The spine is sound and is stronger than after round 1. Specifically, on the
four pieces of new mathematics this round was asked to attack hardest:

1. **Theorem 11.14 on the spectral side — correct.** The bound
   `|I_∞(E,F)| ≤ C_F\deg E` for `E ≥ 0` does follow from
   `0 < \mathrm{Re}\,ρ < 1` and absolute convergence alone; both interchanges
   are justified in the text; `C_F` is finite and explicit. Only the displayed
   constant is wrong, by the factor `2` (N1).
2. **Lemma 11.4a and the polarized Definition 11.4 — correct and complete.**
   The three descriptions genuinely agree; (11.6) is proved off the diagonal;
   the false parenthetical is gone. M2 cost no theorem, as predicted.
3. **Lemma 12.4A + Proposition 12.4B — correct in every step I could check.**
   The rank-4 operator, its Green-kernel inverse, `π_P(1−s) = π_P(s)`, the
   quartet, the `106_11` variable dictionary `x_0 = γ_0`, `y_0 = ½−β_0`, and
   in particular the claim that `Ξ_a > 0` on `R` replaces (E2)'s last clause —
   all verified. Two lines are still argued rather than derived (N5).
4. **Proposition 12.6 — repaired.** (12.4), the abscissa `½+θ`, the
   poles-not-zeros clause and the two `M13` slips are all correct; the
   "verbatim" list overreaches by one entry (N3).
5. **Lemmas 13.5a/13.5b and Theorem 13.6 — correct.** The recession-cone
   argument is right, the box count is right, the labelling of the full
   lattice as `OPEN` is honest, and Remark 13.6b does **not** overclaim (one
   slipped estimate, N6).
6. **The schema statements — now correct as conditionals.** Restatement 12.4a,
   Remark 12.4a′, Restatement 13.3, Remark 13.7 and §14.5 are all correctly
   quantified and mutually consistent. §9.1(3) and Proposition 12.5 are
   corrected. **§10 is not** (N4).
7. **Theorem 11.12 with (X18) — correct**, with the right inequality on
   distinct zeros; the two propagated remarks in Papers 45 and 43 are accurate
   and claim nothing new.

**Blocking:**

* **N2** (`MAJOR`) — a false negative claim about (b′), asserted in Remark
  13.5c and repeated in Theorem 13.6(ii), §14.4a and §14.5. It must be
  withdrawn; the repair makes §13 read better.
* **N4** (`MAJOR`, honesty) — §10 still carries the M1-withdrawn claim. This
  is the paper's label section; it must match §14.5.

**Not blocking, to be fixed in the same pass:** N1 (the factor `2` in (11.17) —
small, but it feeds `m > C_F` in Theorem 12.3 Step 1), N3, N5, N6, N7, N8.

After those, my round-1 verdict is superseded as follows: the reduction
theorem (Theorem 12.3) is earned, its falsifier apparatus (Lemma 12.4A,
Proposition 12.4B, Proposition 12.6, Theorem 12.4) is earned, the schema is
correctly labelled, §13 closes the two lattice candidates on finite truncations
only and says so, and the deliverable is exactly what M16 asked it to be: *a
sufficient condition isolated and localized, of unknown satisfiability, with no
sign anywhere.*

---

## (E) Plausibility of the `--check` claims of `R135_004`

Both `--fast` modes were run once by the auditor; nothing longer was rerun.

* `h0_candidate.py --check --fast` — **exit `0`**, ~0.2 s, `ALL CHECKS
  PASSED`. Index set printed as "prime powers q <= 5" (M7 repair present in the
  code, not only in the prose). Table: `#H⁰ = 1`, `\log\# = 0` for `m = 1..6`
  in both lattices, against `m²/4 − m/4` up to `7.5` — matching `R135_004`
  §3.3's `--fast` line exactly. The `--check` claim (prime powers `q ≤ 7`,
  `\#H⁰ = 1` for `m ≤ 8`, `\deg ΠK = −4.1\cdot10^{−15}`, extrema
  `16.953849 / −8.669861`) is **plausible**: it is the same computation on a
  larger box, and the `float64` floor `10^{−15}` is consistent with what the
  fast run prints.
* `canonical_pairings.py --check --fast` — **exit `0`**, ~10 s, `ALL CHECKS
  PASSED`. `P1`,`P2` at `~1.3\cdot10^{−13}`, `P4` at `≤ 4.6\cdot10^{−14}`,
  `P3` geometric side `−66.166750865` against `−66.1660047786` over 60 zero
  pairs, relative `1.13\cdot10^{−5}` — **identical to the figures
  `R135_004` §3.2 reports for `--fast`**. The `--check` claims (`2\cdot10^{−15}`
  on `P1`, `7\cdot10^{−15}` on `P2`, relative `4.94\cdot10^{−8}` on `P3` over
  120 pairs) are **plausible**: finer panels and a longer zero sum, with the
  same geometric side to 10 digits. One observation: in `--fast` the
  diagnostic line prints `Pi K : Phi(0) = Phi(1) = 2.611\cdot10^{−5}`, which
  should be `0` exactly — fast-mode quadrature error, not a defect, but it
  shows the fast panels are two orders coarser than the `10^{−13}` the checks
  report, so the `--check` tolerances are doing real work.
* `polya_class.py --check` (60 s, `mpmath`) — not rerun. Its printed figures
  (`ARCH = −0.9973107840892264`, `PRIME = 0.00268921591077361`, so
  `PRIME − ARCH = 1`, and `I_∞(K,K) = 0.5` to `6.5\cdot10^{−27}`) agree with
  the blueprint's independent run recorded in `R135_003` §0.1 and with
  `\deg K = 1`, `I_∞(K,K) = ½` as proved. **Plausible.**
* The banner of `polya_class.py` still prints `T_∞(K)`; `R135_004` §3.1 says
  so, and Theorem 11.8(ii)'s note disclaims the symbol. Acceptable; the phase
  README was not updated (N8).

---

*No paper was edited by this audit. No sign is claimed, asserted or suggested.*
