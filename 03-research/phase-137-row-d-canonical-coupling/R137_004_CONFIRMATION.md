# R137.004 — Confirmation, round 2, phase 137

Object: `R137_003_ROUND2.md` and every artefact it
touches — `R137_001_ROUND1.md` (withdrawal banner), `R137_001b_PART_III_DRAFT.md`, `README.md`,
`scripts/d137_lattice.py`, the header note in `03-research/phase-65-signature-continuity/RH-PROOF.md`, and
the `NO-GO-LIST.md` entry. Everything below was checked against the **current files**, not against the
its summary. Algebra was redone from scratch; the script was run.

**Headline.** Both `FATAL` findings are genuinely repaired — H1 by an analytic certificate I verified line
by line, H2 by withdrawal that I confirmed propagated to all six places it had reached. Eighteen of the
twenty findings are `FIXED` outright, one (`H18`) is `FIXED` and reproducible, and one (`H8`) is
**partially fixed** and leaves the round's single `MAJOR` residue, recorded as `N1`. Six further `MINOR`
issues are new (`N2`–`N7`), none load-bearing.

---

## 1. Priority checks, done independently

### 1.1 H1 — Lemma 2.1, the cubic, redone from scratch (`CONFIRMED`)

I rederived the whole chain without looking at its intermediate lines.

With `f_n = (A−B)e^{φ}`, `A = 2π²n⁴e^{9t/2}`, `B = 3πn²e^{5t/2}`, `φ = −x`, `x = πn²e^{2t}`:
`dx/dt = 2x`, so `φ' = −2x`, `φ'' = −4x`; `A' = \tfrac92A`, `A'' = \tfrac{81}4A`, `B' = \tfrac52B`,
`B'' = \tfrac{25}4B`. Using `(ge^{φ})'' = (g''+2g'φ'+g(φ''+φ'^2))e^{φ}`:

    f_n'' = e^{φ}\big[A(\tfrac{81}4 − 18x − 4x + 4x²) − B(\tfrac{25}4 − 10x − 4x + 4x²)\big]
          = e^{φ}\big[A(4x²−22x+\tfrac{81}4) − B(4x²−14x+\tfrac{25}4)\big] ,

which is its display **exactly**. Subtracting `\tfrac14f_n = \tfrac14(A−B)e^{φ}` turns
`\tfrac{81}4 \mapsto 20` and `\tfrac{25}4 \mapsto 6`, so (2.1) is `A(4x²−22x+20) ≥ B(4x²−14x+6)`.
`A/B = \tfrac{2π}{3}n²e^{2t} = \tfrac23x`; multiplying through by `3/B > 0`:

    2x(4x²−22x+20) ≥ 3(4x²−14x+6)
    ⟺ 8x³−44x²+40x ≥ 12x²−42x+18
    ⟺ p(x) := 8x³−56x²+82x−18 ≥ 0 .

The reduction is **correct**. `p(5.1) = 1061.208 − 1456.56 + 418.2 − 18 = 4.848 > 0`; `p(5.0) = −8 < 0`
(matching the blueprint's own check, and showing `5.1` is close to the true root, so the constant is not
padded). `p'(x) = 24x²−112x+82` has roots `(112±\sqrt{4672})/48 = 0.9093, 3.7573`, so `p' > 0` on
`[5.1,∞)` and `p` is increasing and positive there. For `t ≥ u_0` and every `n ≥ 1`,
`x = πn²e^{2t} ≥ πe^{2u_0} = 5.1`, so the termwise bound holds for **every** term and
`K'' ≥ K/4`, i.e. `ΠK ≤ 0`. `u_0 = \tfrac12\log(5.1/π) = 0.2422553269…` (mpmath, dps 20) — the report's
value is right; see `N3` for the script docstring. `β = πe^{2u_0} = 5.1` exactly, by construction.
The blueprint's independent `u_0^{\text{true}} = 0.238624 < 0.2422553` is consistent, as it must be.

The one step not written out is termwise differentiation of `K = 2Σf_n` — legitimate (the differentiated
series converges locally uniformly by the `e^{−πn²e^{2t}}` factor) and worth one clause.

**Lemma 2.2 (`CONFIRMED`, with a typo — `N2`).** `K ≥ 2f_1` needs `f_n ≥ 0` for `n ≥ 2`, i.e.
`A ≥ B`, i.e. `\tfrac23x ≥ 1`, i.e. `e^{2t} ≥ 3/(2πn²)`. The report prints `3/(2π²n²)` and then
`≤ 3/(8π²)` — **`π` mis-squared, twice**. The correct numbers are `3/(8π) = 0.1194 < 1`; the conclusion
is unaffected. The `n = 1` half is right: `2(2π²e^{9t/2}−3πe^{5t/2}) ≥ 2π²e^{9t/2}` iff `πe^{2t} ≥ 3` iff
`t ≥ \tfrac12\log(3/π) = −0.0231`, so the bound holds on `t ≥ 0`. The script's `C3` reports
`min ratio = 1.0473` at `t = 0`, tight exactly where the proof says it should be.

**Corollary 2.3 (`CONFIRMED`).** The majorant `2π²e^{9t/2}e^{−πe^{2t}}` has log-derivative
`\tfrac92 − 2πe^{2t} < 0` for `t > \tfrac12\log\tfrac9{4π} = −0.167`, so on
`[\log q−u_0, \log q+u_0] ⊂ [0.4509,∞)` it decreases and its minimum is the right endpoint,
`2π²q^{9/2}e^{9u_0/2}e^{−βq²} ≥ e^{−βq²}` (the prefactor exceeds `2π² > 1`). Lemma 2.2 is only proved for
`t ≥ 0` and the window starts at `0.4509` — checked, the hypothesis is respected.

**The threshold (`CONFIRMED`).** `M_+ ≤ 17`, `w_2 = 0.4901291`, `κ_2 ≥ 1.83571·10^{−6}` give
`17·0.4901291/1.83571·10^{−6} = 4\,538\,960.x`, so `4\,538\,961`. The script prints exactly these.
The report's insistence that no threshold here is sharp, and the withdrawal of the word "exact", are
correct and are the right posture: the true `κ_2` on the certified window is `3.40145·10^{−6}` and the
direct check `C5` passes far below every version of the bound.

**`M_+ ≤ 17` (`CONFIRMED` with a caveat — `N7`).** The structure is right: `ΠK` is even and `≤ 0` off
`(−u_0,u_0)` by Lemma 2.1, so `\sup ΠK = \max_{[0,u_0]}ΠK`, and grid-max plus `Lh/2` bounds the sup on
the **whole** interval, not only at grid points. Run: `max on grid = 16.953849` (reproducing Paper 47
§13.2), `L = 101.5`, margin `0.0254` (`--fast`) / `0.01015` (full run, `h = 2·10^{−4}` — the report's
figure). `16.953849 + 0.0254 = 16.979 ≤ 17` ✓.

### 1.2 H2 — withdrawal, traced to every site (`CONFIRMED`)

I checked each of the six places the claim had reached. All are withdrawn:
`R137_001` header banner (explicit); `R137_003` §2.5 (withdrawal, with the auditor's one-line reason
quoted back and "I should have seen it"); `R137_003` §5 row B6 ("second half withdrawn");
`R137_003` §6 (the `(H_a)` row replaces it as `OPEN`); `R137_003` §7 ("the anti-correlation argument that
round 1 gave for closing it is withdrawn"); `README.md`; `R137_001b` (draft Thm 17.6 is now `CANDIDATE`
under `(H_a)`, and Remark 17.7 is gone — I confirmed it is absent from the current draft). H12's
"disqualified in advance" is likewise withdrawn, with the correct citation to Restatement 12.4a /
Remark 12.4a′. Theorem D.11.6′(ii) is `CANDIDATE` under a **stated** hypothesis `(H_a)`, and (iii)
(`M_- < ∞`) is correctly separated out as trivial. The replacement statement — the construction is
model-uniform, hence covered by Restatement 12.4a, with **no** comparison of counts — is exactly the
statement I asked for, and its explicit "nothing is claimed about which count is larger" is the right
guard. The decision **not** to add an illustrative numerical check for `(H_a)` is correct and correctly
reasoned.

### 1.3 H5 / §2.4b — the zero-free-region-free route (`CONFIRMED`)

The negative result is sound and honestly labelled. I checked the two loads:
* `Φ_E(σ) ≤ m` holds **only** on `σ ∈ [0,1]`, because that is exactly where `e^{(σ−1/2)t} ≤ 2\cosh(t/2)`
  pointwise. Correct.
* On `σ ∈ (0,1)` division by `ξ(σ+iτ)` is illegitimate without RH (Lemma 13.5b gives positivity only on
  the **real** axis). Correct. So `σ ∈ \{0,1\}` are the only abscissae where the degree ceiling and
  non-vanishing coexist, and the method is forced onto `\mathrm{Re}\,s = 1`. This is the real content of
  §2.4b and it is right.
* The bootstrap: at `σ = 1+η` the Euler product removes the zero-free region but **Stirling still gives
  `e^{π|τ|/4}`**, so the `e^{πT/2}` factor survives; with `T ≳ Q` forced by the Montgomery–Vaughan
  diagonal, the `X²` coefficient is `≫ 1` and the inequality does not close. Verified.
The declaration of **(X19)** with its two costs (Paper 47 §1.13 row, §15 import tag) is present in
`R137_003` §2.4, in draft §0.2 and in draft §17.4's import line. The observation that §1.13 *already*
carries the qualitative `ζ(s) ≠ 0` for `\mathrm{Re}\,s ≥ 1` is correct and useful. `FIXED`.

### 1.4 H8 — the R3 audit: quotes fair, conclusion not established (`PARTIALLY FIXED`; see `N1`)

Fair-reading checks, all `CONFIRMED`:
* `CORRECTIONS-CONNES-R3.md` §"What this changes in the chain" reads verbatim "`M_P = −∂_z log D_P^∘ −
  E_P'/E_P` matrix-Herglotz, **bounded `≤ C_F/|Im z|`** ⟹ normal family (Montel)". Quoted accurately.
* Its ledger has a **single** entry, "[INPUT, H1 ⇐ G2]", and asserts "Everything else (trace-log identity,
  factor `i`, frame bound `a>1/4`, residue detection, Vitali) is proved with no use of zero locations".
  The boundedness clause is indeed **not** in that list. Its reading is fair.
* The mathematics of the objection is right **for `M_P` as literally defined**: a Herglotz `M` obeys
  `‖M(z)‖ ≤ C/|\Im z|` only if its Nevanlinna measure has total mass `≤ C` (the `A`, `Bz` and
  `−λ/(1+λ²)` terms force `A = B = 0` and `Ω(\mathbb R) ≤ C` as `|\Im z| → ∞`), and for
  `−∂_z\log D_P^∘ = Σ_j m_j/(z_j−z)` that mass is the zero count of `D_P^∘`, divergent.
* Placement: the status note sits **after** the R3 banner, is signposted as auditing both versions, and
  the `NO-GO-LIST.md` entry matches it clause for clause. `FIXED`.

What is **not** established is that this is R3's real gap — see `N1`.

### 1.5 H4, H10, H11, H13, H14 (`CONFIRMED`)

* **H4.** Corollary D.11.5′ is now one-directional, with (iv) stating flatly that round 1's "equivalent"
  was false and (v) recording that `Q(m) < ∞` and `h⁰_Z(mK) < ∞` are unproved (new open item (23c)).
  I re-verified (iii): with `Q = ε_0m\sqrt{\log m}`, `π_*(Q)(\log m+Q) ≍ Q²/\log Q ≍ ε_0²m²`, so
  `Cε_0² < ¼` gives the conclusion, and the second term `Q\log m/\log Q ≍ ε_0m\sqrt{\log m} = o(m²)`.
  Correct. The relation to Paper 47's `ρ_Q` is supplied ((2.2), `ρ_Q ≤ Ce^{CQ}/\minΛ(q)`) — this is the
  part H4(3) asked for and it is delivered. See `N4` for a side-effect.
* **H10.** The three corrections are right and the fourth item is a genuine addition I checked myself:
  for real **even** `F`, `Φ_F(1−s) = ∫F(t)e^{(1/2−s)t}dt = ∫F(−t)e^{(s−1/2)t}dt = Φ_F(s)`, so
  `Φ_F(0) = Φ_F(1)` and `Φ_F(0)Φ_F(1) = 0 ⟺` primitivity. **Correct.** The statement "on the even half
  the two hypotheses coincide, on the odd half CC's is weaker" is the precise relation and is the right
  replacement for round 1's false identification.
* **H11.** The §4.1 table is split into exact identities (`Q = Π`, with the symbol computation; the
  vanishing conditions as corrected), analogies relabelled `HEURISTIC` (six rows), and `IMPORTED` with
  no transfer claimed (six rows). §4.4 is rebuilt as Statement D.13.3′ (`HEURISTIC`) with (a) and (b)
  separately sourced, (c) an explicit **non-inference**, the circularity named as such, and the "I think"
  gone. This is a better section than round 1's.
* **H13.** The relabelling table is complete and the one row left at `REFUTED` (B2, the sign of `W_S`) is
  the one row that deserves it — the blueprint's inequality **is** false as an expression of Weil
  positivity, as I verified independently in round 1.
* **H14.** Both limbs. The sign check is now in the text with `[cc:88–90]` ("note the change of sign",
  `W_∞ := −W_R`) and the derivation `W_{\{∞\}}(F) = −⟨F⋆F^∨,ω_∞⟩ = \mathrm{ARCH}(F⋆F^∨)` matching CC's
  `W_∞`. Correct. CC's own semilocal programme `[cc:82–84]` is quoted and identified with D.12-β /
  GAP-135.B — a good addition: it makes clear the open item is the literature's, not the corpus's.

### 1.6 H18 / reproduction (`CONFIRMED`)

`python3 scripts/d137_lattice.py --fast` (31.4 s) prints, and these match the report exactly:

    u0 = (1/2)log(5.1/pi) = 0.2422553269,  beta = 5.1
    p(5.1) = 4.848
    C2 PiK > 0 somewhere in [0.235, u0)  ...  PiK(0.235) = +0.34634
    C3 min ratio = 1.0473445
    C4 max on grid = 16.953849, Lipschitz bound = 101.5, margin = 0.0254
    q = 2 : w_q = 0.490129, kappa_q >= 1.83571e-6 (true min 3.40145e-6), certified m0 = 4538961
    ALL CHECKS PASSED

`--fast` and the full run report the same constants, as claimed, because the constants no longer depend
on the grid. `C2`'s new probe over `[0.235, u_0)` does exhibit the defect H1 found — the script now
falsifies round 1's constant rather than being blind to it, which is the right way to close a finding.

---

## 2. Per-finding status

| # | severity (r1) | status | note |
|---|---|---|---|
| H1 | `FATAL` | **FIXED** | analytic certificate verified line by line (§1.1); `N2`, `N3`, `N7` are cosmetic residues |
| H2 | `FATAL` | **FIXED** | withdrawn at all six sites (§1.2); `(H_a)` stated, Thm D.11.6′(ii) `CANDIDATE` |
| H3 | `MAJOR` | **FIXED** | mean value moved to `[1,1+T]`; constants unchanged, as I said they would be |
| H4 | `MAJOR` | **FIXED** | one-directional; (iv) and (v) added; `ρ_Q` relation supplied ((2.2)); see `N4` |
| H5 | `MAJOR` | **FIXED** | (a) (X19) declared with both costs; (b) Lemma 2.2 proved on the full range used |
| H6 | `MAJOR` | **FIXED** | "correction" withdrawn everywhere; replaced by a confirmation; see `N5` on direction |
| H7 | `MAJOR` | **FIXED** | sentence withdrawn from report, header note and `NO-GO-LIST.md`; replacement is `OPEN` and honest about the tautology |
| H8 | `MAJOR` | **PARTIALLY FIXED** | R3 read, quoted fairly, note relocated correctly; but the strongest reading of R3 is dismissed in a parenthetical — **`N1`** |
| H9 | `MAJOR` | **FIXED** | Thm D.12.5 withdrawn to `OPEN`; Rem. 8bis.4b's limits quoted; new open item D.12-γ |
| H10 | `MAJOR` | **FIXED** | plus a correct and valuable even/odd reconciliation |
| H11 | `MAJOR` | **FIXED** | table split; §4.4 rebuilt as a non-inference |
| H12 | `MAJOR` | **FIXED** | withdrawn with the right citation (Restatement 12.4a, Remark 12.4a′) |
| H13 | `MAJOR` | **FIXED** | relabelling table complete; only B2 stays `REFUTED`, correctly |
| H14 | `MAJOR` | **FIXED** | sign check in the text; `[cc:82–84]` cited |
| H15 | `MAJOR` | **FIXED** | `CANDIDATE` under `(H_a)`; the Laplace-analysis obstruction stated precisely |
| H16 | `MINOR` | **FIXED** | §5 not §4; blueprint not map §3; "contradiction" → "unreconciled gap" — all three in both files |
| H17 | `MINOR` | **FIXED** | conjunction stated, then the narrowing; the `D8.5b-i` §6 operator-norm reading closed explicitly |
| H18 | `MINOR` | **FIXED** | verified by running it (§1.6); docstring errors of round 1 gone, one new one (`N3`) |
| H19 | `MINOR` | **FIXED** | arithmetic corrected to `(φ⋆φ^∨)(0)`; demoted to Remark; monotonicity sentence replaced by the correct converse |
| H20 | `MINOR` | **FIXED** | `2π²q^{9/2}e^{9u_0/2} ≥ 1` is Cor. 2.3; quantifier order written out |

---

## 3. New findings

### N1 (`MAJOR`) — D.0.4 dismisses R3's own uniform bound in a parenthetical

**Location.** `R137_003` §1.1, the closing parenthetical; propagated to the `RH-PROOF.md` status note
("R3's ledger does not carry it") and to `NO-GO-LIST.md` point 2.

**Claim.** "*(R3 point 4 does prove a uniform-in-`P` bound — `Σ(\log p)p^{−k(1/2+2a)} < ∞` for the source
core `S_a^∘`, `a > 1/4`. That is a bound on the **source frame** … it is not a bound on the Nevanlinna
mass of `M_P`, which is what Montel consumes in the R3 chain.)*"

**Why this is not established.** For a **sourced** (channel) Herglotz matrix of a self-adjoint operator,
the `(α,α)` Nevanlinna mass is exactly `‖ι_Pφ_α‖²` — the total mass of the spectral measure of `A_P` at
the source. R3 point 4 bounds precisely that: with `|\hatφ(k\log p)|² ≤ Cp^{−2ak}`, the diagonal Gram
sum `Σ_{p,k}(\log p)p^{−k/2}|\hatφ(k\log p)|² ≤ CΣ(\log p)p^{−k(1/2+2a)} < ∞`, **uniform in `P`** — which
is L1 verbatim. So on the natural reading of R3 (Montel applied to the channel matrix `G_P`, as R3 point 3
and the word "matrix-Herglotz" both suggest), the uniform bound is *supplied* by point 4 and R3's chain
has no unlisted gap of the kind D.0.4 alleges.

Its objection is correct only for `M_P` read as the **scalar** log-derivative of a determinant,
where the mass is the zero count. R3's text is genuinely ambiguous — it defines `M_P` as a scalar and
calls it "matrix-Herglotz" one line later — and choosing the reading that fails, without saying why the
other is unavailable, is not an audit.

This matters more than a presentational point. If point 4 does deliver L1, then the phase-65 corpus
contains a *complete* chain to RH modulo G1–G5 alone, which is precisely the
situation that must be flagged, and the `Ξ_a` falsifier becomes the only remaining defence. The two
report rounds have now both declined to audit G4 / R3 point 4, which is where the whole question sits.

**Minimal repair.** Decide the reading. Either (i) show that the shorted, pole-relative norm
`‖ι_Pφ‖²_{H_P^∘}` is **not** bounded by point 4's sum (off-diagonal Gram terms, the Feshbach shorting),
in which case D.0.4 stands and should say so in one paragraph rather than one parenthesis; or (ii) concede
that point 4 supplies the uniform bound, in which case the verdict `REFUTED` must be re-grounded — on
G3's unproved `Ξ_a`-transfer, on §4's `thm:rich`, or on the falsifier — and the `RH-PROOF.md` note and
`NO-GO-LIST.md` point 2 rewritten. Until then, the pre-R3 half of the verdict (L1 is the wall) is the
part that is established, and the R3 half is `UNDECIDED`.

### N2 (`MINOR`) — Lemma 2.2's proof mis-squares `π`, twice

`R137_003` §2.2: "`2π²n⁴e^{9t/2} ≥ 3πn²e^{5t/2}` iff `e^{2t} ≥ 3/(2π²n²)` … `3/(2π²n²) ≤ 3/(8π²) < 1`".
The ratio is `A/B = \tfrac{2π}{3}n²e^{2t}`, so the threshold is `3/(2πn²)`, and for `n ≥ 2`,
`3/(8π) = 0.1194 < 1`. Conclusion unaffected; the displayed algebra is wrong.

### N3 (`MINOR`) — the script docstring's `u_0` disagrees with the script and the report

`scripts/d137_lattice.py` docstring: "`u0 := (1/2) log(5.1/pi) = 0.2423106...`". The code computes, and
the run prints, `0.2422553269`; the report says `0.2422553…`. The docstring figure is wrong in the fifth
decimal. Nothing depends on it.

### N4 (`MINOR`) — a correction to Paper 47 §14.5 item (23) is made in passing and not recorded

`R137_003` §2.6 argues that a uniform `ρ_Q` alone does **not** give `h⁰_Z(mK) = o(m²)` (it leaves
`h⁰ ≤ π_*(Q)\log(2mρ+1)`, which still needs the rank bounded), and concludes "**item (23) needs both**".
I checked this and it is right. But Paper 47 §14.5 item (23) states the `ρ_Q` reformulation as an
**equivalence** ("— equivalently whether `ρ_Q` … can be controlled uniformly in the rank"), so this is a
correction to the paper, asserted in one clause of a paragraph about something else, and it appears in no
paper-facing list. Given that H6 was a finding about claiming a correction that was not one, the symmetric
error — making one and not declaring it — should not be left unflagged.

**Minimal repair.** State it as a numbered observation, with the one-line proof, and add it to the
draft's paper-facing table.

### N5 (`MINOR`) — §2.3b claims the necessity half of Remark 13.6a and proves the sufficiency half

`R137_003` §2.3b and draft Remark 17.2a: "Theorem D.11.2′ **proves the single-generator half of exactly
that statement**", where Remark 13.6a's statement is "`mK` dominates a single translate `τ_{\log q}(ΠK)`
**only for** `\log q ≲ \tfrac12\log\log m`". Theorem D.11.2′ proves the **converse**: `m ≳ e^{βq²}`
*suffices*. "Only for" is a necessity claim and needs an *upper* bound on `κ_q`, not a lower one.
The necessity direction is two lines — feasibility at `t = \log q` forces `mK(\log q) ≥ w_qM_+^{(q)}`
where `M_+^{(q)} := ΠK(0)`, and `K(\log q) ≍ e^{−πq²}` — but it is not in the document.

**Minimal repair.** Add the two lines, or reword to "proves the sufficiency direction of the picture
Remark 13.6a describes".

### N6 (`MINOR`) — §2.4b's heading overstates what §2.4b shows

The heading and §0 say "the `σ>1` route … **fails**"; Statement 2.4 is labelled "`PROVED` (as a statement
about this route)". What is shown is that **one** bootstrap — the degree-identity bound on `Φ_E(1+η)` fed
into Montgomery–Vaughan — does not close. Another majorant for `Φ_E(1+η)` is not excluded. The genuinely
structural argument is the paragraph that follows ("the degree ceiling and non-vanishing coexist only at
`σ ∈ \{0,1\}`"), which is correct and is the real result; the heading should be its claim, not the
bootstrap's.

### N7 (`MINOR`) — `C4`'s Lipschitz constant is sampled, so "interval-safe" overstates it

`R137_003` §2.3a and `README.md` call `C4` "interval-safe". The grid-plus-margin **structure** is
interval-safe, but `L` is itself `max|ΠK'|` over ~12 (`--fast`) to ~24 sampled points, i.e. a numerical
estimate of a Lipschitz constant, not a bound on it. The report does label the result "`PROVED` modulo
the certified numerical bound on `L`", which is honest, but `L` is not certified either.

The conclusion is nonetheless robust and that is the better thing to say: `16.953849 + Lh/2 ≤ 17` holds
for **any** `L ≤ 460` at `h = 2·10^{−4}`, against a sampled `L ≈ 101.5`. **Minimal repair:** state the
robustness margin instead of the word "interval-safe", or bound `|ΠK'|` analytically the way Lemma 2.1
bounds `ΠK`.

---

## 4. Per-item verdicts

| item | verdict |
|---|---|
| **D.0** | **CONFIRMED WITH REPAIRS.** The verdict `REFUTED` on `RH-PROOF.md` stands and is now correctly grounded for the pre-R3 text: the chain is `(G1–G5) ∧ L1 ∧ L2 ∧ L3 ⟹ RH`, L2 and L3 are `Re s > 1` identities, L1 is not, and §6's blanket claim fails for it. H7, H16, H17 are cleanly fixed and the competing `D8.5b-i` §6 reading is closed correctly. The **R3 half of the verdict is `UNDECIDED`** pending `N1`: the quotes are fair and the note is correctly placed, but the reading of R3 under which its chain has no unlisted gap is dismissed in a parenthetical rather than refuted. |
| **D.11** | **CONFIRMED.** Lemma 2.1 (the cubic certificate), Lemma 2.2 and Corollary 2.3 are correct — I rederived all three. Theorem D.11.2′ has a certified, non-sharp threshold. Theorem D.11.3 stands with `β = 5.1` and explicit quantifiers. Theorem D.11.4′ is repaired and its zero-location import is declared with both costs. Corollary D.11.5′ is one-directional, with the missing finiteness recorded as (23c). Theorem D.11.6′ is `CANDIDATE` under a stated `(H_a)`. §2.4b is a real negative result. Residues `N2`–`N5`, `N7` are cosmetic. |
| **D.12** | **CONFIRMED.** The sign correction (B2) stands — the only `REFUTED` label left, and the right one. Theorem D.12.5 is withdrawn to its correct scope with Remark 8bis.4b quoted. CC's sign convention is checked before importing, with its citation. The vanishing conditions are corrected, and the even-`F` reconciliation is a genuine addition that I verified. Labels are repaired. D.12-β is now correctly identified with CC's own open programme. |
| **D.13** | **CONFIRMED.** Exact identities separated from analogies; six rows relabelled `HEURISTIC`; §4.4's circularity named and the inference withdrawn; the "I think" removed. `Q = Π` remains the section's one genuine result and it is correct. |

**Overall verdict: CONFIRMED, with one `MAJOR` residue (`N1`) confined to the R3 half of D.0.**

Round 2 is a good repair round. Every finding was accepted without contest, the two `FATAL` items were
repaired **by construction** rather than by relabelling, four statements were downgraded honestly, an
alternative route was worked out and reported as failing, and the withdrawals propagated to every file
including the two outside the phase directory. The one place where the report did not do the work is the
one place where doing it might have changed the headline — `N1` — and that is worth saying plainly.

**Part III.** Still **not appendable**, and the report agrees. Beyond the four reasons in draft §0, `N1`
is not a Part III issue but `N4` is (a paper-facing correction to item (23) must be listed before any of
§17 is proposed).

---

## 5. On the D.14 gate

**Keep D.14 closed — agreed, and now for sound reasons.** Round 1's stated reason (anti-correlation) is
withdrawn; what replaces it is arithmetic and it is sufficient: the proved lower bound is
`c(\log m)^{3/2}/\log\log m` against a requirement of `¼m²`, of order `10²` versus `10^{11}` at
`m = 10^6`, and Corollary D.11.5′(iii) turns the gap into a structural demand that Theorem D.11.2′ shows
runs the opposite way for single generators. Nothing in either round makes near-cancellation plausible,
and item (23) is untouched.

**On the proposed re-wording**, one correction. `h⁰_Z(mK) = Ω(m^{2−ε})` is a good gate: it is a *lower*
bound on the object (c) needs, so it is genuine evidence. `Q(m) = Ω(m)` is **not** a good gate on its own:
by Corollary D.11.5′(iv) there is no converse — a large `Q(m)` does not imply a large `h⁰_Z(mK)`, it is
only a *necessary* precondition for one. Gating D.14 on it risks opening the square on a signal that
carries no information about (c).

**Recommendation.** Gate D.14 on `h⁰_Z(mK) = Ω(m^{2−ε})` alone; record `Q(m) = Ω(m)` as a
*necessary precondition* to be established first, not as an alternative trigger. And note that item (23c)
— whether `Q(m)` and `h⁰_Z(mK)` are finite at all — logically precedes both.
