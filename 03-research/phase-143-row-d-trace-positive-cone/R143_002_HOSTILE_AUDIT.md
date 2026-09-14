# R143.002 — Hostile audit, round 1, phase 143 (`s_*`, the trace-positive cone B4, 12.3-B4)

*Auditor: Claude Opus 5. Date 2026-09-13. Method: every claim assumed wrong until re-derived from the
cited source; all certified constants recomputed independently with mpmath (`mp.dps = 40`, my own
Newton/derivative code, not the builder's); `scripts/certify_s_star.py --fast` re-run to completion
(exit 0). Sources actually opened and read: `R143_000`, `R143_001`, `README.md`,
`scripts/certify_s_star.py`; `R141_001` §D.26 (Lemma D.26.1, Def. D.26.2, Lemma D.26.3 with (D.26.1),
Lemma D.26.4, Thm D.26.5, Lemma D.26.6) and §D.30 (Def. D.30.4, Thm D.30.5); `R142_001` §§D.31.10,
D.31.13, D.31.14; `R142_004` J3; Paper 46 §§11.5, 12.2 (Thm 11.8, 11.11, 11.13, 11.14, Thm 12.3 and
its printed proof, Lemma 12.4A(v), Prop. 12.4B, Restatement 12.4a); Paper 45 Thm 10.4;
`R138_001` §D.17.2. No builder file was edited.*

**Headline: no FATAL. The two load-bearing theorems of the round — Theorem D.34.4/D.34.5 ((T1′),
unconditional) and Theorem D.34.8 (the transfer theorem) — survive the audit; I re-derived both from
the sources and could not break either. Three MAJOR findings, all outside the main line: a genuine
gap in Theorem D.34.7 ((T2) is false), a well-posedness defect in the definition of the cone of
record (and an undercount of the RH-uses), an unproved existence clause in Theorem D.34.14(ii), plus
one MAJOR framing error ("strictly stronger than Theorem 12.3") that is repeated in the README.
Seven MINOR findings. The round's central honest statement — `(b′)_{B4} ⟺ RH`, so O-24 *is* RH — is
correct and is correctly flagged by the builder himself; my item-5 verdict below sharpens it to
`RESTATEMENT`, not `reduction`.**

---

## 0. What I recomputed

| quantity | builder | my independent recomputation (`mp.dps = 40`) | verdict |
|---|---|---|---|
| `γ_1` | 14.13472514173469379 | 14.134725141734693790457251983562 | ✓ |
| `s_1 = s(γ_1,π/2)` | 0.998460162718809109 | 0.9984601627188091092345474 | ✓ |
| `u^*` | −0.110991563370513694 | −0.1109915633705136940835335 | ✓ |
| `1 − s_1²` | 3.0773034635×10⁻³ | 0.00307730346353 | ✓ |
| `L(γ_2) = 1/cosh(π/4γ_2)` | 0.99930249463368 | 0.999302494633682644 | ✓ |
| `L(γ_2) − s_1` | 8.42331915×10⁻⁴ | 0.000842331914874 | ✓ |
| `(1−s_1²)/4` (D.35(ii)) | 7.693×10⁻⁴ | 7.6932587×10⁻⁴ | ✓ |
| `d_* = (1−s_1²)^{−1}` | 324.9598… | 324.959826631 | ✓ |
| `b_J = ½(cosh 1 − e^{−1})` | 0.58760… | 0.5876006 | ✓ |
| `a_J = ½(cosh 1 − e)` | −0.58760… | −0.5876006, `a_J+b_J = 0` to 10⁻⁴¹ | ✓ |
| `deg τ_2K = cosh 1` | (implicit) | 1.5430806 ≠ `deg K = 1` | ✓ (the coefficient `cosh 1` is exactly what makes `deg J = 0`) |
| script `--fast` | as printed in README | re-run here, exit 0, output identical | ✓ |

`L(γ_1) = 0.998458240354706579`, i.e. the elementary bound is `1.9×10⁻⁶` below `s_1` — relevant to H5.

**Lemma D.33.2's factor `π/(4γ)` is CORRECT, and the auditor's brief was wrong to doubt it.** The
peaks of `|cos(γu+θ)|` form a progression of step `π/γ`, so some peak has `|u_k| ≤ π/(2γ)`; the bound
is `1/cosh(u_k/2) ≥ 1/cosh(π/(4γ))` — the `4` is the halving inside `cosh`, not a second halving of
the spacing. Verified numerically: `m(γ) ≥ L(γ)` with equality to `8×10⁻⁶` on the whole printed grid.

**Sign convention of the polar term, checked against the source and not against the brief.**
`R141_001` (D.26.1) reads `t_n(E) = n^{½}Φ_g(1)Φ_E(0) + n^{−½}Φ_g(0)Φ_E(1) − Σ_ρΦ_E(ρ)Φ_g(1−ρ)n^{½−ρ}`,
i.e. **`b = Φ_E(0)` pairs with `n^{½}` and `a = Φ_E(1)` with `n^{−½}`** (from `Φ_{τ_cg}(s) =
e^{(s−½)c}Φ_g(s)` at `s = 1,0`). `R143_001` (D.34.1) reproduces this correctly, and (D.34.2) is the
correct term-by-term transform. **The builder's "`b ≥ 0` comes first" is therefore right**: the `n^{½}`
coefficient is `b`, so the top real pole `w = 3/2` carries residue `Φ_g(1)b`, and it is `b`, not `a`,
that Landau reaches first.

---

## 1. Findings

### H1 (MAJOR, non-load-bearing) — Theorem D.34.7 ((T2) is false) does not prove `C'_X = +∞`; as written it proves `C'_X ≳ 10^{90}`.
The construction fixes one single-zero direction `F^{(φ)}(u) = e^{−u²/18}\sin(γ_1u+φ)` whose
off-`ρ_1` tail is `Σ_{ρ≠ρ_1}|Φ_{F^{(φ)}}(1−ρ)| < 10^{−90}` — **a constant of that fixed Gaussian
width**. The trace estimate then carries an error `O(r·10^{−90}n^{½})` which must stay below the only
surviving positive term, `p_0(ε/2)(n^{½}+n^{−½})`, *for every `n`*; both grow like `n^{½}`, so the
admissible range is `r ≲ 10^{90}ε/(2p_0)`, i.e. `r/ε` is **bounded**. Since `|I_∞(E,X)|/\deg E ≈
rG|Φ_X(ρ_1)|/ε`, the family yields a large but **finite** lower bound, not `+∞`. The proof as printed
does not establish the claimed supremum.
*Repair (not performed here, per the no-edit rule):* let the Gaussian width `→ ∞` jointly with `t`, so
that the tail constant `10^{−90}` is replaced by a quantity `→ 0`, and take the supremum over the
family; this needs `R142_001` Lemma D.31.7(ii),(iv) restated with the width as a parameter. Until that
is done, Theorem D.34.7 should read `C'_X ≥ c·10^{90}` (`CERTIFIED`-style) or be labelled `SKETCH`.
*Consequences:* Corollary D.34.7a(i)'s conclusion ("(T2) fails, so Theorem D.32.4 does not apply to
B4") survives in weakened form only if `C'_X` is genuinely infinite; with the finite bound, D.32.4's
(T2) is merely *not established* rather than *false*. **Nothing on the main line depends on this**
(Theorem D.34.8 does not use (T2)), which is why this is MAJOR and not FATAL. Two smaller defects in
the same proof are recorded as H8.

### H2 (MAJOR) — the cone of record is defined by a property of `g` that is not known to be satisfiable unconditionally; and the RH-uses of Theorem D.34.10 are undercounted (three, not two).
Definition D.34.1's "**Convention:** `B4 := B4^{g,0}` for one fixed `g` that is admissible and
satisfies `(G^+)`" makes the *definition* of the cone of record depend on Lemma D.34.9, which is
`PROVED` **under RH** and `OPEN` unconditionally (the builder's own O-25). Consequently:
 (i) the right-hand side of Corollary D.34.12 and the statement of O-24 are, read literally, not known
     to be well-posed unconditionally. The repair is one quantifier and costs nothing, because
     Theorem D.34.8 holds *for every admissible `g`*: state the equivalence as
     `RH ⟺ ∃ admissible g ∃h⁰ : (a), (b′)_{B4^{g,0}}, (c)`, and state O-24 with `∃g` inside.
 (ii) Theorem D.34.11 and O-24 say the proof of D.34.10 "uses RH **twice** and irremovably,
     at `|n^{½−ρ}| = 1` and at `W(E) ≥ 0`". It uses RH **three** times: the third is the existence of a
     `g` with `(G^+)` (Lemma D.34.9), whose unconditional status is exactly O-25. The missing-estimate
     description of O-24 must therefore name three items, not two. (Note also that `W(E) ≥ 0` is used
     twice over inside D.34.10 — once to force `a,b > 0`, once in the final inequality.)

### H3 (MAJOR) — Theorem D.34.14(ii) is labelled `PROVED` but its existence clause is not proved.
The second clause ("if `ξ_K` has a real zero `β_0`, then the primitive trace-positive cone contains
classes outside `𝓝_∞^{(K)}`") requires a class `E ∈ D^W_K` with `Φ_E(0) = Φ_E(1) = 0`, `Φ_E(ρ) = 0` at
**every** zero except `β_0` (and, for real `E`, its partner `1−β_0`), and `Φ_E(β_0) ≠ 0`. That is an
interpolation statement over an infinite constraint set; nothing in the corpus supplies it (Lemma
D.26.6 gives surjectivity onto **finite** windows only, and Paper 46 Theorem 11.10 describes the
primitive perp without a realisation theorem). The displayed "proof" verifies only that *if* such a
class exists, its traces have one sign. Label should be `CLAIM`/`SKETCH`. **The first clause of
D.34.14 — that (T1′) for `ξ_K` is conditional on "no real zero" — is correct and is proved**, and it
is the clause the falsifier row needs; the builder's reading of why a Siegel zero breaks the mechanism
(a *real* pole at `3/2−β_0` strictly between `½` and `3/2`, where Landau's singularity is then
permitted to sit) is exactly right.

### H4 (MAJOR, framing; repeated in the README headline and in D.36(3)) — "Theorem D.34.8 is a **strictly stronger** transfer theorem than Theorem 12.3" is false as stated.
Theorem D.34.8's hypothesis is `(b′)_{B4}`; Theorem 12.3's is `(b′)` (effective representative). By the
builder's own Remark D.34.2, `𝓔 ⊄ B4` and `B4 ⊄ 𝓔`: the two clauses are **incomparable**, so neither
implication is weaker than the other and neither theorem implies the other. What is true, and what
should be printed instead, is: *D.34.8 uses strictly fewer inputs about its cone (only (T1′), which is
a theorem here, rather than Theorem 11.13(i),(ii) plus ampleness Theorem 11.14 plus a bounded-density
constant), and its clause is not refuted, whereas 12.3's is unsatisfiable.* That is a real gain; it is
not "strictly stronger". (Dropping `E' ≢ 0` from the clause — Definition D.34.8a — **is** a genuine
weakening of the hypothesis and I verified both Steps 2 and 4 survive `E' = 0`: `E' = 0` forces
`K−nF ∈ 𝓝_∞`, resp. `nF ∈ 𝓝_∞`, and the argument closes either way.)

### H5 (MINOR) — `s_* = s_1` exactly is certified, not proved: the `θ`-argmin is a numerical scan.
Corollary D.33.3 rigorously gives `s_* = m(γ_1)`, and Lemma D.33.2 rigorously brackets
`L(γ_1) = 0.998458240… ≤ s_* ≤ s(γ_1,π/2) = 0.998460162…`. The **equality** `m(γ_1) = s(γ_1,π/2)` —
i.e. that `θ = ±π/2` is the argmin — rests on a `60`-point grid plus two refinement passes with no
interval arithmetic and no monotonicity/convexity lemma in `θ`. (The heuristic is sound: `θ = π/2`
maximises the distance `dist(θ,πZ)/γ` from `u = 0` to the nearest peak; but `s(γ,θ)` is a sup over all
extrema, not over the nearest peak, so this is not a proof.) Theorem D.33.4's label
"`PROVED` (analysis) + `CERTIFIED` (the constant)" should be "`PROVED`: `s_* ∈ [L(γ_1), s_1]` and the
infimum is attained at `ρ_1`; `CERTIFIED`: `s_* = s_1` to 18 decimals". **Immaterial downstream**: the
only use (D.35(ii)) would move `d_*` from 324.96 to at most 325.37, and D.35(ii)'s point is that the
constant needed there is `s_*^{\mathrm{cone}}` anyway.

### H6 (MINOR) — Remark D.34.15 / O-20: "A8 enters through the index set `n ∈ N`" is over-precise, and its supporting sentence is false.
The claim *"had the traces been indexed by a generic sequence `c_k → ∞`, no Dirichlet series would
exist"* is wrong: `Σ_k t_{c_k}e^{−wc_k}` is a **generalised** Dirichlet series and Landau's theorem
applies verbatim to it. What actually fails for a generic `c_k` is the **meromorphic continuation**, not
the existence of the series. Moreover `N` is not necessary: I checked the geometric semigroup
`n ∈ {2^k}`, where the generating function is
`p_1b/(1−2^{½−w}) + p_0a/(1−2^{−½−w}) − Σ_ρ c_ρ/(1−2^{½−ρ−w})`, whose real poles are exactly the two
polar ones (`w = ½` and `w = −½`) while the zero-poles `w = ½−ρ+2πim/\log 2` are non-real for every
`ρ` unless `γ_ρ ∈ (2π/\log 2)Z` — so the entire cascade (i)→(ii)→(iii) runs on the sparse index set
`{2^k}` too. The correct labelled remark is: *A8 enters through the requirement that the set of test
translations be a multiplicative semigroup whose generating function continues, and through the two
polar exponents `{0,1}` of `ξ` (i.e. the pole of `ζ`), which put the real poles at `3/2` and `½`.*
This does not weaken any theorem; it weakens the rhetoric of O-20's "affirmative answer", and it
suggests a sharper cone (`t_{2^k} ≥ 0` only) for phase 144.

### H7 (MINOR) — Lemma D.34.9's Baire step is a sketch.
The perturbation argument must simultaneously keep (i) `g ≥ 0`, (ii) evenness, (iii) admissibility
`Φ_g(1−ρ) ≠ 0`, and (iv) `(G^+)`. (i)–(iii) are Lemma D.26.1's own mechanism verbatim (perturb inside
a strictly smaller support, `‖h‖_{C^0} < κ := \min g_0`) and do work for each of the two bumps of
`g_T`; (iv) survives because `(G^+)` holds with unbounded slack (`Φ_{g_T}(0)Φ_{g_T}(1) =
4\cosh²(T/2)Φ_h(0)Φ_h(1) → ∞` while `W(g_T) ≤ 4Σ_ρ|Φ_h(ρ)|²` is `T`-uniform under RH — I re-derived
both). But the printed proof does not say that the perturbation is confined to the two bumps, and
"continuous in `h'` for the `C^2`-seminorms" is asserted rather than estimated. Label `SKETCH` for the
Baire step; the analytic content is correct.

### H8 (MINOR) — two further slips inside Theorem D.34.7's proof.
(a) "the admissible set of phases is a half-circle, on which the linear functional attains modulus `≥`
its maximum over a quarter-circle" is not an argument. The correct statement (which I verified) is:
every **closed** arc of length `π` contains a point of `πZ`, so `\max|\cosθ| = 1` on it, and the
required modulus bound follows. (b) The `n ≥ 2` estimate cancels `0.70p_0tb_J` against `2rG|Φ_g(ρ_1)|
= 0.70p_0tb_J` exactly; the margin is the `ε`-term plus `(n^{½}−n^{−½}) ≥ 0.7071 > 0.70`. That is
correct but should be printed, since the cancellation is exact to the stated digits.

### H9 (MINOR) — §D.34.5 item 3's "interleave" is imprecise.
For `Ξ_a` the real polar poles are `3/2±a, ½±a` and the zero-poles have real parts `1±a`. For
`a < ¼` the ordering is `3/2+a > 3/2−a > 1+a > 1−a > ½+a > ½−a`, i.e. the zero-poles are **bracketed**
by the polar ones and the cascade stops only after *two* steps, not one; for `a > ¼` they genuinely
interleave. The conclusion the builder needs — that the cascade never closes for `Ξ_a`, so
Theorem D.34.4 does not transport, while **(T1′)_a does** transport (no real pole at all once all four
polar coefficients vanish; `Ξ_a` has no real zero by Lemma 12.4A(v)) — is correct in both regimes. I
re-derived the `Ξ_a` transport of D.34.8 and confirm it is verbatim.

### H10 (MINOR) — §D.34.5 item 5's last sentence asserts more than it proves.
"The `Ξ_a`-witness of Theorem D.30.16 (`rF_+ + K_a`) has `R_a > 0`, `\deg_a > 0` and, by the above,
negative traces for large `n`." Corollary D.34.13 proves only that **some** class violates
`(b′)_{B4_a}`; it does not identify that class, and no trace computation for `rF_+ + K_a` is given.
Either compute it or write "some class in the `R_a > 0`, `\deg_a > 0` region".

### H11 (MINOR, labelling) — Corollary D.34.12 should carry `RESTATEMENT (of RH)` beside `PROVED`.
It is a correct theorem (both directions verified below) whose content is an equivalence with RH; the
corpus convention has been to tag such statements `RESTATEMENT`. The `§Label` table's row for row D
("no label change; nothing with a sign is proved") is correct and honest, and the builder's boxed
warning "Why this is not a proof of RH" is exactly the right disclosure — this is a labelling nicety,
not a dispute.

---

## 2. Per-item verdicts

### D.33 (`s_*`) — **ACCEPTED with H5.**
* Lemma D.33.2: re-derived, three lines, correct, factor `π/(4γ)` right. `PROVED`. ✓
* Corollary D.33.3: correct; uses only `γ_2 ≥ 21` from (V2) and `L` increasing. Margin `8.42×10⁻⁴`
  recomputed. ✓
* Theorem D.33.4: value, `u^*`, `1−s_1²` all reproduced independently to printed precision; the
  truncation window (`|u| ≤ 3/2`, `1/cosh(3/4) = 0.7552`) is a genuine certified truncation and the
  script asserts it at runtime. The one overclaim is the `θ`-argmin (H5).
* **The caveat is right, and is the most valuable paragraph of §D.33.** `R142_001` Definition D.31.13
  defines `s_*` as an infimum over **directions** `F` of degree `0` (`C_F\sqrt{2/W_F}`), and D.31.14(iii)
  records `s_*^{\mathrm{cone}} ≤ s_1`. The blueprint's D.33 asks for a different constant (infimum over
  **zeros** and `θ`). The builder computed the latter, said so, and refused to transport it to Horn A.
  **Horn A's `Δ` is indeed still undetermined, and `s_*^{\mathrm{cone}} = 0` is not excluded.** Confirmed
  against both sources. D.35(ii) states this correctly.

### D.34.5 / D.34.4 ((T1) NO, unconditionally) — **ACCEPTED. This is the round's result.**
I re-derived every step and tried to break each:
* **(D.34.2) and the continuation.** The Dirichlet series is the correct transform of (D.26.1);
  `|t_n| ≤ A(E)n^{½}` follows from `|n^{½−ρ}| = n^{½−β_ρ} ≤ n^{½}` by (E2) and `Σ|c_ρ| < ∞` from
  (11.2) + `M` integrations by parts + (E3d), exactly as in Theorem D.26.5's proof; the interchange
  `Σ_ρ ↔ Σ_n` is licensed by absolute convergence on `\mathrm{Re}\,w > 3/2`; the continuation is Lemma
  D.26.4's argument verbatim (finitely many poles per compact, classical polynomial bound for `ζ` on
  the tail). Poles: `3/2` (residue `Φ_g(1)b`), `½` (residue `Φ_g(0)a`), `3/2−ρ` (non-real by Lemma
  13.5b), with `\mathrm{Re}(3/2−ρ) ∈ (½,3/2)` **strictly** by (E2). All correct.
* **(i) `b ≥ 0`.** Does not need Landau at all: `D_E(σ) ≥ 0` for `σ > 3/2` and `σ_c ≤ 3/2`, so
  `\lim_{σ↓3/2}(σ−3/2)D_E(σ) = Φ_g(1)b ≥ 0` with `Φ_g(1) > 0` (Lemma D.26.1, `g ≥ 0`). ✓
* **(ii) `b = 0 ⟹` all `Φ_E(ρ) = 0`.** The auditor's brief hesitated here; the argument is sound. If
  `c_{ρ_0} ≠ 0`, the pole at `3/2−ρ_0` forces `σ_c ≥ \mathrm{Re}(3/2−ρ_0) > ½`, and `σ_c ≤ 3/2` by the
  coefficient bound, so `σ_c` is **finite** — which is the hypothesis Landau needs. Landau then makes
  the real point `w = σ_c` singular; but `D_E` is meromorphic on `C` with poles only at `½` (absent
  here, and anyway `< σ_c`) and at the non-real `3/2−ρ`, hence **holomorphic at every real point of
  `(½,3/2]`**. Contradiction, so all `c_ρ = 0`, and `Φ_g(1−ρ) ≠ 0` (Baire) gives `Φ_E(ρ) = 0`. Then
  `t_n = Φ_g(0)an^{−½}` and `t_1 ≥ 0` gives `a ≥ 0`. ✓ No circularity, no RH, no zero list.
* **(T1′) `B4^g ∩ P^W ⊆ 𝓝_∞`.** Primitive ⟺ `a = b = 0` (Paper 46 Thm 11.13(iii), Def. 11.6): checked
  in the source. Then (iii) applies. ✓ Consistency probes I ran: it does not conflict with Lemma
  D.26.6 (finite trace windows are unobstructed — (T1′) is an asymptotic statement); it transports to
  `Ξ_a` and is **true** there, so it is not the falsifier line; it fails exactly when a real zero
  exists, which is the `ζ_K` row.
* **Sign conventions:** verified against (D.26.1), see §0. "`b ≥ 0` first" is correct.
* **Side results.** *Literal (T1) false on `B4^g`*: the witness `J = \cosh(1)K − τ_2K` checks out —
  `deg τ_2K = \cosh 1 = 1.5431 ≠ deg K = 1` (this is *why* the coefficient is `\cosh 1`), `deg J = 0`,
  `b_J = −a_J = 0.5876`, zero-sum identically `0` since `Φ_{τ_cK}(ρ) = e^{(ρ−½)c}ξ(ρ) = 0`, hence
  `t_n(J) = p_0b_J(n^{½}−n^{−½}) ≥ 0` with equality only at `n = 1`. The `λF_1` perturbation is
  correct (`n^{½}−n^{−½} ≥ n^{½}/2` for `n ≥ 2`; `λ ≤ p_0b_J/(4S)`). `J ∉ B4^{g,0}` because
  `a_J < 0` — so the `t_0 ≥ 0` DECISION is forced, and is right. ✓ *True with `t_0 ≥ 0`*: trivial from
  D.34.4(iii). ✓ *(T2) false*: **NOT established** — see H1.

### D.34.8 (12.3-B4) — **ACCEPTED as an implication; framing corrected by H4.**
Step by step, against Paper 46's printed Theorem 12.3:
* Hypotheses: (a); `(b′)_{B4}` **without** `E' ≢ 0` (a genuine weakening — verified harmless, see H4);
  (c) in Paper 46's exact form `h⁰(E)+h⁰(K−E) ≥ ½I_∞(E,E) − ½I_∞(E,K) + χ`, which with
  `I_∞(E,K) = ½\deg E` (Thm 11.8(i)) is `R(E)+χ` — matching `R141_001` Theorem D.30.5(ii). ✓
* Step 1 deleted: confirmed that no later step uses `H'`, `C_F`, Theorem 11.14 or (T2). ✓
* Step 2: `t_m` is linear and vanishes on `𝓝_∞` (Thm D.26.5), so `0 ≤ t_m(E'_n) = t_m(K) − n\,t_m(F)`;
  fixing `m` and letting `n → ∞` **along the assumed sequence** gives `t_m(F) ≤ 0` for every `m`; then
  `−F` is primitive and trace-positive, so `−F ∈ 𝓝_∞` by (T1′), so `q = 0` by Theorem 11.11.
  The limit is taken at fixed `m`, so no uniformity is needed. ✓
* Step 3: verbatim Paper 46 Step 3, with `n_0` in place of `m/q`; no `χ ≥ 0` needed. ✓
* Step 4: `nF − E' ∈ 𝓝_∞` gives `Φ_{E'}(0) = Φ_{E'}(1) = 0`, i.e. `E'` primitive; (T1′) gives
  `E' ∈ 𝓝_∞`, hence `nF ∈ 𝓝_∞`, `q = 0`. This replaces Paper 46's degree contradiction
  (Thm 11.13(i),(ii)), which is unavailable for B4 — correctly identified. ✓
* Conclusion `I_∞(F,F) ≤ 0` on primitive `F ∈ C_c^∞` ⟹ RH by Paper 45 Theorem 10.4: the citation is
  correct (sufficiency of primitive tests for Weil's criterion). ✓
* **"Strictly stronger than Theorem 12.3": REJECTED (H4).** The clauses are incomparable by the
  builder's own Remark D.34.2; the correct claim is "fewer and cheaper inputs about the cone, and a
  clause that is not refuted".

### D.34.10 ((b′)_{B4} under RH) — **ACCEPTED; the RH-use count corrected by H2(ii).**
Every inequality re-derived:
* `a,b > 0`: under RH `W(E) = Σ|Φ_E(ρ)|² ≥ 0`, so `I_∞(E,E) = 2ab − W(E) ≤ 2ab`; if `ab ≤ 0` then
  `R(E) ≤ −¼\deg E < 0`. Hence `ab > 0`, and `a+b = \deg E > 0` forces both positive. ✓ (Cleaner than
  the brief's route, and correct.)
* Polar part `≥ 2\sqrt{ab\,Φ_g(0)Φ_g(1)}`: AM–GM on `n^{½}Φ_g(1)b` and `n^{−½}Φ_g(0)a`, whose product
  is `abΦ_g(0)Φ_g(1)` — **independent of `n`**, so the bound is uniform in `n`. ✓ (`Φ_g(0),Φ_g(1)>0`
  because `g ≥ 0, g ≢ 0`: Lemma D.26.1.)
* Zero part `≤ \sqrt{W(E)W(g)}`: `|n^{½−ρ}| = 1` (RH) and `|Φ_g(1−ρ)| = |Φ_g(ρ)|` (`g` real, RH), then
  Cauchy–Schwarz; `W(E) = Σ|Φ_E(ρ)|²`, `W(g) = Σ|Φ_g(ρ)|²` under RH. ✓
* Closing: `R(E) > 0 ⟺ W(E) < 2ab − ½\deg E < 2ab`; with `(G^+)`, `W(E)W(g) < 4abΦ_g(0)Φ_g(1)`. ✓
  Strict, and uniform in `n`. The `a,b ≥ 0` half of `B4^{g,0}` also holds. ✓
* Consistency with `R142_004` J3: J3's witness `E = 53.119F_0 + 400K` has `a = b = 200`,
  `W(E) = t²W_{F_0} ≈ 79780 < 2ab − ½\deg E = 79800` — the AM–GM margin of D.34.10 is exactly J3's
  `d − 2tG = 0.55 > 0`, specialised. I recomputed the two numbers and they agree. ✓ (Note J3 uses the
  *per-zero* bound `|Φ_g(ρ)| ≤ \sqrt{Φ_g(0)Φ_g(1)}` of Lemma D.24.6, which does **not** suffice for a
  full zero sum — hence the genuinely new demand `(G^+)`, hence O-25, hence H2.)
* `(G^+)` achievable with `g ≥ 0` and the Baire condition: **yes under RH**, with unbounded slack
  (`Φ_{g_T}(0)Φ_{g_T}(1) ≍ \cosh²(T/2) → ∞`, `W(g_T) ≤ 4Σ|Φ_h(ρ)|²` uniformly, since
  `|Φ_{g_T}(ρ)| = 2|\cos(γ_ρT)||Φ_h(ρ)|`). Re-derived. The Baire/nonnegativity bookkeeping is
  sketchy (H7); the unconditional status is correctly `OPEN`.

### The equivalence `RH ⟺ ∃h⁰ (a),(b′)_{B4},(c)` — **ACCEPTED, modulo the `∃g` quantifier (H2(i)); label should add `RESTATEMENT`.**
`⟸` is D.34.8 (unconditional in its own inputs); `⟹` is D.34.10 with `h⁰_{RR}^{+}`, `χ = 0`, whose
(a),(c) are `R141_001` Theorem D.30.5(i),(ii) — unconditional, and I verified (c)'s three-case proof
uses `\deg E + \deg(K−E) = \deg K = 1 > 0` and the Serre symmetry, with no sign input. ✓

### FATAL resolution (Cor. D.34.13, the `Ξ_a` row) — **ACCEPTED. The handling is exemplary.**
The builder triggered his own FATAL rule ((T1′) proved unconditionally **and** a transfer theorem
running on it), stopped, ran `Ξ_a`, and reported. I re-checked the chain: (T1′)_a is **true** for
`Ξ_a` (no real zero, Lemma 12.4A(v); once the four polar coefficients vanish `D_E` has no real pole,
and Landau forbids a non-real abscissa-singularity); D.34.8 therefore transports verbatim; its
conclusion for `Ξ_a` is false (Prop. 12.4B, `PROVED` in Paper 46); hence **no `h⁰` for `Ξ_a` satisfies
(a),(b′)_{B4_a},(c)** — a theorem in the negative, proved *by* the falsifier. The separation is
located precisely where the builder says: inside the clause, at `|n^{½−ρ}| = 1`, which for `Ξ_a` is
`n^{∓a}` (unbounded), and at `W` which is indefinite there. **This is the correct shape demanded by
Restatement 12.4a's schema** (the model-dependent step sits in the clause, not in the transfer), and
it is the strongest structural argument in the round. Verdict: **no FATAL**.
The A8 reading is right in substance and overstated in wording (H6). The `ζ_K` row is right in its
first clause and unproved in its second (H3): a real zero `β_0` would put a **real** pole at
`3/2−β_0 ∈ (½,3/2)`, i.e. strictly between the two polar poles, which is exactly the place Landau's
singularity is allowed to sit — so the mechanism's only zero-location input is "no real zero", as
claimed. `Ξ_Q`: frame broken (A7), traces undefinable — accepted as `RESTATEMENT`.

### D.35 (Horn A) — **ACCEPTED.**
(i) re-verified against Paper 46's printed proof: (c) is used once, at `E = nF` of degree `0`; (b′) at
degrees `0` and `1`. ✓ (ii) is the honest and correct refusal to let `s_1` masquerade as
`s_*^{\mathrm{cone}}`; `d_* = 324.9598…` and `(1−s_1²)/4 = 7.6933×10⁻⁴` recomputed. ✓ (iii),(iv)
carried unchanged, correctly. (v) "Horn B dominates Horn A" — accepted as `ASSESSMENT`, with the
caveat that it partly rests on H4's framing error; even after H4 the judgement stands, because Horn
A's clause is refuted and Horn B's is not.

### Labels, corpus, scripts, README — **ACCEPTED with H3, H5, H11.**
* The Landau precedent is real and correctly cited: `R138_001` §D.17.2 (Widder II.5b, Laplace form) is
  in the corpus and on row D; the builder claims novelty only for the *discrete/arithmetic-index* form
  and for the object it is applied to. Verified — that is the honest claim.
* The corpus table's greps are of the right shape and its verdicts match what I found by spot-check
  (in particular "trace positive" is new terminology and the `s(γ,θ)` material is phase-142's).
* `scripts/certify_s_star.py --fast` runs to completion (exit 0) and its output matches the README and
  the text digit for digit; my independent implementation reproduces `s_1`, `u^*`, `L(γ_2)` and the
  margin. The truncation is genuinely certified (runtime assertion `best > 1/\cosh(U/2)`); the
  `θ`-minimisation is not (H5).
* Paper-facing list P46-34…P46-42: destinations sensible. **P46-37 must carry H4's correction** ("beside
  Theorem 12.3, with incomparable hypotheses", not "strictly stronger"). **P46-40 must carry H3**
  (D.34.14(ii) downgraded). **P46-36 must carry H1** ((T2) not yet false).
* README: accurate to the builder's text, and therefore inherits H1 and H4 in its bullet list.

---

## 3. Item 5 — the explicit answer

**Is `(b′)_{B4}` for `h⁰_{RR}^{+}` "Weil positivity in disguise", and is O-24 a genuine reduction or a
restatement?**

1. **Logically it is a restatement of RH, and the builder says so.** `(b′)_{B4}` for `h⁰_{RR}^{+}` plus
   (a),(c) (both unconditional, Theorem D.30.5) gives RH by Theorem D.34.8; RH gives `(b′)_{B4}` by
   Theorem D.34.10. So `(b′)_{B4} ⟺ RH` (Corollary D.34.12, modulo H2(i)'s `∃g` quantifier), and
   **O-24 is RH**. It buys no logical ground. Anyone reading this round must read the builder's boxed
   paragraph "Why this is not a proof of RH", which states this without hedging; the round does not
   overclaim.
2. **Is it Weil positivity in disguise?** *Partly, and the two halves must be separated.*
   * The `⟹` direction (D.34.10) uses RH three times: `W(E) ≥ 0` (which is precisely Weil positivity
     on the zero side), `|n^{½−ρ}| = 1` (the A3-line), and the existence of a `(G^+)`-test function.
     So the *proof* is Weil positivity plus the on-line modulus, and has no independent content.
   * The `⟸` direction is **not** Weil positivity and is the round's genuine mathematics: it rests on
     (T1′), which is proved **unconditionally** by a Landau/abscissa argument using only
     `0 < \mathrm{Re}\,ρ < 1`, `ξ` has no real zero, and the arithmetic index set. Nothing in that step
     assumes or smuggles RH — I checked this specifically, including against the `Ξ_a` model where the
     same step is true and the conclusion is false.
   * The clause itself has structure that Weil positivity does not obviously have: it is an infinite
     family of **linear** inequalities on classes with `R(E) > 0, \deg E > 0` (a quadratic region),
     indexed by `n`, whereas Weil positivity is one quadratic form on the primitive subspace. It is
     **not** a weakening of the effective clause `(b′)` (Remark D.34.2: `𝓔` and `B4` are incomparable),
     so phase 142's refutation genuinely does not reach it. That is a real structural gain over the
     state after phase 142, where the clause was outright **false**.
3. **What an unconditional proof of `(b′)_{B4}` would have to establish, precisely.** For every real
   `E ∈ D^W` with `2ab − W(E) > ½(a+b) > 0` (where `W(E) = Σ_ρΦ_E(ρ)Φ_E(1−ρ)`, `a = Φ_E(1)`,
   `b = Φ_E(0)`), and every `n ≥ 1`:
   `|Σ_ρ Φ_E(ρ)Φ_g(1−ρ)n^{½−ρ}| ≤ b\,Φ_g(1)n^{½} + a\,Φ_g(0)n^{−½}`, **together with** `a,b ≥ 0`,
   which off RH does *not* follow from `R(E) > 0` because `W(E)` may be negative. Three unconditional
   replacements are needed, not two (H2(ii)): for `W(E) ≥ 0`, for `|n^{½−ρ}| = n^{½−β_ρ}`, and for
   `(G^+)`. **And it is equivalent to RH**, by 12.3-B4 + D.34.10. So O-24 is a restatement.
4. **One structural observation the round does not make, offered for phase 144.** Unconditionally the
   zero part of `t_n(E)` is `O(n^{½−β_{\min}})` with `β_{\min} := \inf_ρ\{\mathrm{Re}\,ρ : Φ_E(ρ) ≠ 0\}
   > 0` by (E2), while the polar part is `bΦ_g(1)n^{½}`: so **whenever `b > 0`, `t_n(E) > 0` for all
   large `n` unconditionally**, and `(b′)_{B4}` is, for each fixed `E`, a statement about the *finite*
   range `n ≤ N(E)` — with `N(E)` non-uniform in `E` precisely because `β_{\min}` and `Σ|c_ρ|` are.
   This localises what an unconditional attack must control and is compatible with the builder's own
   recommendation (run Landau on `t_n(E)` against a positive selector).
5. **Comparison with Restatement 12.4a and T2.** Restatement 12.4a says no model-free proof can
   exist: the model-dependent input must appear somewhere. In phase 135–142 it sat in the transfer
   theorem; here it sits **inside the clause** (A3 at `|n^{½−ρ}| = 1`), and Corollary D.34.13 proves the
   clause **false** for `Ξ_a`. That is the schema's honest shape, and it is the strongest thing this
   round establishes about *where* the problem is. T2 (the demand that a candidate read the prime side)
   is met by B4's definition, but H6 shows the reading is thinner than advertised — a multiplicative
   semigroup with a continuable generating function suffices, so "B4 reads A8" should be read as "B4
   reads the polar structure of `ζ` and the semigroup structure of the translations".

**Verdict on item 5: RESTATEMENT, not reduction — but a well-chosen one.** The clause is
RH-equivalent; its `⟸` half is unconditional new mathematics; its `⟹` half is Weil positivity plus the
A3-line; and unlike its phase-142 predecessor it is not refuted. The correct label for row D is
unchanged, which is what the builder wrote.

---

## 4. Overall

**Round 1 is accepted, with four MAJOR findings (H1–H4) and seven MINOR ones, none of which touches
the main line.** The main line — Lemma D.34.3 → Theorem D.34.4 → Theorem D.34.5 ((T1′)) → Theorem
D.34.8 (12.3-B4) → Theorem D.34.10 → Corollary D.34.12, plus Corollary D.34.13's falsifier separation
— was re-derived here independently and stands. The FATAL rule was triggered correctly, executed
correctly, and resolved correctly: **no FATAL**. No sign is proved and none is claimed.

*Required repairs for round 2:* (H1) re-prove or downgrade Theorem D.34.7; (H2) quantify `∃g` in
Definition D.34.1's convention, Corollary D.34.12 and O-24, and correct the RH-use count from two to
three; (H3) downgrade Theorem D.34.14(ii) to `CLAIM` or supply the interpolation; (H4) delete
"strictly stronger than Theorem 12.3" from D.34.8's remark, D.36(3), the README and P46-37, replacing
it with the incomparability statement. *Recommended:* (H5) restate Theorem D.33.4's label as a
bracketing plus a certified value; (H6) restate Remark D.34.15; (H7)–(H10) the local repairs; (H11)
add `RESTATEMENT` to Corollary D.34.12.
