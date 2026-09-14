# R137.002 — Hostile audit, round 1, phase 137

Auditor: hostile (Opus 5). Date: 2026-09-13. Object: `R137_001_BUILDER_ROUND1.md` (648 lines),
`R137_001b_PART_III_DRAFT.md`, `README.md`, `scripts/d137_lattice.py`, and the two cross-file edits of
round 1 (the header note in `03-research/phase-65-signature-continuity/RH-PROOF.md` and the
`NO-GO-LIST.md` entry). Sources re-read from source: Paper 46 `main.md` §§11–14; Paper 44 `main.md`
Thm 8bis.4a and Rem 8bis.4b; `03-research/phase-45-fredholm/135-teorema-dos-primos.md` §7.2;
`03-research/phase-65-signature-continuity/RH-PROOF.md` and `D8.5b-i-SELF-ADJOINT-COMPLETION.md`;
`cc_2006.13771_text.txt`. No builder file was edited.

**Summary.** The report is unusually careful in places — the sign correction of §3.1 is right, the
support decoupling of §3.2 is right, `Q = Π` is an exact identity and every `[cc:NNN]` citation I spot-
checked is accurate — and wrong in exactly the places where it makes its headline. Two findings are
`FATAL`: a numerically **false** constant inside a `PROVED` theorem, with a script check built so that it
cannot detect the falsity (H1); and a comparison of two **lower** bounds sold as "strictly more sections"
(H2), which carries §2.5's sign verdict, refutation B6, draft Remark 17.7, and the advice on D.14.

---

## Findings

### H1 (`FATAL`) — `u_0 ≤ 0.235` is false; Theorem D.11.2's constant and the whole §2.0 constant block

**Location.** §2.0 (D11.2); Theorem D.11.2; §2.3 (`β ≤ 4.94`); §7 check `C2`; `scripts/d137_lattice.py`
C2/C4; `README.md`; draft Thm 17.2; the headline; Remark 13.6a "correction".

**Claim.** "`u_0 := sup{u > 0 : ΠK(u) ≥ 0} ≤ 0.235`, so `{ΠK > 0} ⊂ (−u_0,u_0)`"; and hence
"`h⁰_Z(mK) > 0` for all `m ≥ 1 883 507`", labelled `PROVED`.

**Why it is wrong.** Recomputed independently (mpmath, `dps = 30`, `NMAX = 8`, root of `ΠK` by
`findroot`): `ΠK(0.235) = +0.34634 > 0` and the true last sign change is `u_0 = 0.238623976…`. So
`0.235` is **not** an upper bound for `u_0`, the inclusion `{ΠK > 0} ⊂ (−0.235, 0.235)` is false, and the
first step of Theorem D.11.2's proof ("where `ΠK(t−log q) > 0` we have `|t−log q| < u_0`") does not hold
at the stated value. With the true `u_0`, `κ_2 = 3.8764·10⁻⁶` and `M_+w_2/κ_2 = 2 143 634.5`, so the
"exact threshold" is `2 143 635`, not `1 883 507`. `β = πe^{2u_0} = 5.066`, not `≤ 4.94`.

The script cannot catch this by construction: `C2` sets `u0 := max{t on the grid : ΠK(t) > 0}` and then
checks `ΠK < 0` only at grid points **strictly greater than that `u0`** — i.e. from `0.240` on — so the
interval `(0.235, 0.2386)` where `ΠK > 0` is never tested. The check is vacuous with respect to the claim
it is cited for. Confirming this, `--fast` (grid `0.02`) prints `u0 = 0.22`, `κ_2 = 7.45243·10⁻⁶`,
`m0 = 1 115 015` — a 70 % swing in the "exact threshold" from a change of grid alone.

**Minimal repair.** Define `u_0` as a *certified* upper bound (bisection on a sign change plus an
interval-arithmetic or explicit-tail argument), state it as `u_0 ≤ 0.24`, recompute `κ_q`, `M_+w_q/κ_q`
and `β` from it, and replace the quoted threshold by a value proved for that `u_0` (`m ≥ 2 143 635`
suffices). Change `C2` to test `ΠK < 0` on the whole of `[u_0^{claimed}, 3]`, not on `(u_0^{grid}, 2]`.
Remove the word "exact" from "the exact threshold": nothing here is sharp — the direct grid check `C4`
already passes at `m = 1 115 015`, below every version of the bound.

---

### H2 (`FATAL`) — "`Ξ_a` has **strictly more** sections than `ξ`" compares two lower bounds

**Location.** Headline (lines 18–20); Theorem D.11.6(ii) and the box "D.11 verdict on the sign" (§2.5);
§2.6 table last row; refutation B6; draft Theorem 17.6 and Remark 17.7; the D.14 recommendation (§6).

**Claim.** `h⁰_{Z,a}(mK_a) ≥ c_a(log m)²/log log m`, "i.e. **strictly more sections than `ξ` has**
(Theorem D.11.3 gives only `(log m)^{3/2}/log log m`)", labelled `PROVED`; hence "the growth carries no
sign … and carries it in the direction opposite", "anti-correlated with the sign", "any future `h⁰` whose
growth is driven by the decay rate of the canonical kernel is therefore disqualified in advance."

**Why it is wrong.** Both displayed inequalities are **lower** bounds. `A ≥ f` and `B ≥ g` with `g > f`
implies nothing whatever about `A` versus `B`. The report has **no** upper bound for `h⁰_Z(mK)` on the
full lattice — that is item (23), which it leaves `OPEN` (§2.6, §6) — so it cannot compare the two
counts in either direction. What the construction actually shows is the weaker and already-known fact
that the §2.3 mechanism is *model-uniform*: it exists for `Ξ_a` too. That is Remark 13.7's point, not a
strengthening of it. Every consequence drawn from "more" — anti-correlation, the disqualification
criterion of draft Remark 17.7, the second half of B6, and the reason given in §6 for not opening D.14 —
is unsupported.

**Minimal repair.** Replace the comparison by: "the same construction runs for `Ξ_a` and gives a bound of
at least the same order; the growth mechanism is therefore model-uniform and carries no sign." Delete
"strictly more", "anti-correlated", and "disqualified in advance". The D.14 recommendation survives on
the sound half of the argument (`(log m)^{3/2}` versus `¼m²`, and Corollary D.11.5(iv)) — see H4.

---

### H3 (`MAJOR`) — Theorem D.11.4: the majorant for `A(1+iτ)` is false near `τ = 0`

**Location.** §2.4, proof of Theorem D.11.4, the display `|A(1+iτ)| ≤ (m + m/|ξ(1+iτ)|)/|s(1−s)|` and its
consequence `|A(1+iτ)| ≤ Cm e^{π|τ|/4}(1+|τ|)^{C}/(1+τ²)`.

**Why it is wrong.** At `s = 1+iτ`, `|s(1−s)| = |τ|·|1+iτ| → 0` as `τ → 0`; it is **not** `≍ 1+τ²`. The
stated majorant is therefore false on a neighbourhood of `τ = 0`, and the majorant one does get,
`≍ m/|τ|²`, is not integrable on `[0,T]`, so the step "the left side is `≤ Cm²e^{πT/2}T^{C}`" is not
established. (The quantity `A(1+iτ) = Σ_q a_qΛ(q)q^{iτ}` is of course finite at `τ = 0`; the point is
that the *derivation from `Φ_E`* degenerates there, which is exactly where `A(1)` is the unbounded thing
one wants to bound.)

**Minimal repair.** One line: Montgomery–Vaughan is translation-invariant (replace `b_q` by `b_q q^{iT_0}`),
so run the mean value on `[1, 1+T]` instead of `[0,T]`, where `|s(1−s)| ≥ 1`. Every constant is unchanged.

---

### H4 (`MAJOR`) — "item (23) is *exactly* / *equivalently* a bound on `Q(m)`" is two one-sided implications with a gap

**Location.** Corollary D.11.5's title ("item (23) is exactly a bound on the largest index"); the
"Reading" paragraph ("Item (23) is *equivalent* to controlling one integer"); §2.6 row 3; §6 item (23);
draft Corollary 17.5 ("Item (23) is therefore equivalent to a bound on `Q(m)`").

**Why it is unproved as stated.**
1. What is proved is: `Q(m) = o(m) ⟹ h⁰_Z(mK) = o(m²)` (from D.11.4), and `h⁰_Z(mK) ≥ ¼m² ⟹
   Q(m) ≫ m√{log m}` (D.11.5(iv)). Between `o(m)` and `m√{log m}` there is a gap in which neither
   implication speaks. "Equivalent" and "exactly" overstate this.
2. `Q(m) < ∞` is nowhere proved, and neither is `h⁰_Z(mK) < ∞`. D.11.5(ii) is stated "whenever
   `Q(m) < ∞`", and (ii)'s biconditional `h⁰ < ∞ ⟺ Q(m) < ∞` is trivial in both directions and settles
   neither side. The object the corollary reduces item (23) to may not exist as a finite integer.
3. Paper 46 §14.5 item (23) **already** carries an equivalent reformulation — "equivalently whether `ρ_Q`
   of Lemma 13.5a can be controlled uniformly in the rank". The report neither cites it nor relates
   `Q(m)` to `ρ_Q`, so the reader cannot tell whether a second reduction has been obtained or the same
   one restated.

**Minimal repair.** State the two implications separately with their gap, drop "equivalent"/"exactly",
prove or flag `Q(m) < ∞`, and say explicitly how `Q(m)` relates to the paper's `ρ_Q`.

---

### H5 (`MAJOR`) — an undeclared zero-location import inside a `PROVED` theorem, and an unproved kernel bound

**Location.** §2.4, proof of Theorem D.11.4 ("`|ζ(1+iτ)|^{−1} ≪ log⁷(2+|τ|)` (`CLASSICAL`)"); §2.0
(D11.2); draft §17.4 and §4's ledger row.

**Why it matters.** (a) `|ζ(1+iτ)|^{−1} ≪ log⁷` is a statement about the **location of zeros** of `ζ`
(non-vanishing on `Re s = 1`, quantitatively). Paper 46 §1.13 requires every such fact to be named in the
compliance list, which currently contains only `0 < Re ρ < 1` (E2), Hardy (X16), the simple-zero
proportion (X18), `ξ(σ) > 0` and "no real zero of `Ξ_a`". Appending draft §17.4 as written would break
§1.13. The Part III draft flags the missing **import-table** row but not the **zeros-rule** row.
(b) The bound `K(t) ≥ 2π²e^{9t/2}e^{−πe^{2t}}` (D11.2) is asserted for all `t ≥ 1` but only grid-checked
on `[1,4]` (script `C3`), while §2.3 uses it for `log q ± u_0` with `q` up to `Q ≍ √{log m}`, i.e. far
outside the checked range. This is a numerical stand-in where a proof is available.

**Minimal repair.** (a) Add `ζ(1+iτ) ≠ 0` to the §1.13 list before any Part III appending, or replace the
bound by one that does not name the line `Re s = 1` (the polynomial-in-`log` strength is not needed;
any bound with `|ξ(1+iτ)|^{−1}` of finite order works, but it still uses non-vanishing). (b) Prove (D11.2)
in one line from the `n = 1` term: `K(t) = 2Σ_n(2π²n⁴e^{9t/2} − 3πn²e^{5t/2})e^{−πn²e^{2t}}`, every
`n ≥ 2` term is positive for `t ≥ 1`, and `2(2π²e^{9t/2} − 3πe^{5t/2}) ≥ 2π²e^{9t/2}` iff `e^{2t} ≥ 3/π`.

---

### H6 (`MAJOR`) — the "Correction to Paper 46" corrects nothing; Theorem D.11.2 **confirms** Remark 13.6a

**Location.** §2.2 "Correction to Paper 46 (`PROVED`)"; headline ("correcting the impression left by
Remark 13.6a"); refutation B8; `README.md` row; draft Theorem 17.2 ("**Remark 13.6a's … is an artefact of
the range `m ≤ 8` and is corrected here**").

**Why it is wrong.** Remark 13.6a contains no false statement. It reports "the numerics below find the
count `1` for every `m` tested" — a true report about the tested range — and is explicitly closed by
"**Everything in this remark beyond Theorem 13.6(ii) is heuristic.**" Count `1` means `H⁰_Z = {0}`, the
*zero* section; it is not the claim "no sections at all" that §2.2 attributes to it ("its *picture* (no
sections at all) does not [survive]").

Worse, the substance runs the other way. Remark 13.6a's heuristic is "`mK` dominates a single translate
`τ_{log q}(ΠK)` only for `log q ≲ ½ log log m`". Theorem D.11.2 gives, for a single generator,
`m ≳ e^{βq²}`, i.e. `q ≲ √{log m}`, i.e. `log q ≲ ½ log log m` — **the same statement**. Theorem D.11.2 is
a proof of Remark 13.6a's heuristic, not a correction of it. Labelling a confirmation as a `PROVED`
correction of the paper, and listing it as refutation B8 and as a ledger row "**corrects Remark 13.6a's
picture**", misstates the record.

**Minimal repair.** Restate as: "Theorem D.11.2 proves the single-generator half of Remark 13.6a's
heuristic and shows in addition that the count is `> 1` from `m ≈ 2.1·10⁶`, so the numerical `1` of §13.2
reflects the range `m ≤ 8`." Delete "correction", B8, and the ledger row.

---

### H7 (`MAJOR`) — D.0.3's central sentence is false and is contradicted by the report's own §1.3

**Location.** §1.5, Finding D.0.3: "The document names no such property … Whether rank-one-ness is
load-bearing in §2–§5 is not decided here; **it is not used anywhere in §2–§5 as written**, which is
precisely the complaint." Propagated to the `NO-GO-LIST.md` entry ("and the document names none") and to
the header note added to `RH-PROOF.md`.

**Why it is wrong.** `RH-PROOF.md` §2 reads, in full: "The divergent `½(log P)²` is the excluded `H–H`
element." That sentence *is* the use of G4's rank-one pole mode — the divergence is shorted out precisely
because it is rank one and sits on `H`. The report quotes that very sentence in §1.3, two pages earlier.
So the property that distinguishes `ξ` from `Ξ_a` (rank one versus rank `≥ 2`, the report's own
observation) **is** named by the document and **is** used in §2. The Finding as written is self-refuted.

Separately, the transfer on which the Finding rests is asserted, not shown: "`G1` (a positive canonical
system from nonnegative weights), `G2` (Gram positivity … phase 64), `G3` (`ren-lim D_P^{(a)} = Ξ_a`)"
are declared "verbatim analogues" with no verification, and `G3` in particular presupposes a
determinantal limit theorem for the two-gamma-factor `Ξ_a` that nobody has proved. Under those
conditions the disjunction "either the chain transfers … or some step uses a property `Ξ_a` lacks" is a
tautology, not a finding.

**Minimal repair.** Replace the Finding with: "§7's faithfulness check is incomplete — it excludes DH by
signedness, a mechanism `Ξ_a` does not trigger. The visible difference is that G4's divergence is rank
one for `ξ` and rank `≥ 2` for `Ξ_a`, and §2 does use rank-one-ness ('the excluded `H–H` element'); what
is unverified is whether G1–G3, G5 transfer at all. `OPEN`." Correct the `NO-GO-LIST.md` and header-note
wording accordingly.

---

### H8 (`MAJOR`) — D.0 audits a text the file itself declares superseded, and never reads the successor

**Location.** All of §1; the header note inserted at the top of `RH-PROOF.md`.

**Why it matters.** `RH-PROOF.md` lines 16–22 carry a banner: "**R3 update (supersedes the decisive step
below).** The Connes/Consani round R3 replaced the arbitrary-pairing realization with the log-derivative
of the spectral determinant … See `CORRECTIONS-CONNES-R3.md`. **The single load-bearing input is H1 ⇐
G2.**" The audit does not mention this banner, does not open `CORRECTIONS-CONNES-R3.md`, and does not say
whether the R3 replacement of §3 changes where the uniformity in `P` comes from — which is the audit's
entire thesis. The header note the builder added is placed *above* a banner it ignores, so the file now
opens with two competing status paragraphs.

**Minimal repair.** Read `CORRECTIONS-CONNES-R3.md`, state whether the R3 chain still routes uniformity
through L1 (or through H1/G2 instead), and rewrite the header note to reference the R3 version explicitly.
Until then the verdict should be stated as applying to the pre-R3 text.

---

### H9 (`MAJOR`) — Paper 44 Thm 8bis.4a is used far outside the scope its own Remark 8bis.4b fixes

**Location.** §3.3 Theorem D.12.5 ("the prime block is not a reservoir", `PROVED-IN-REPOSITORY`);
§3.5(ii); refutation B3; draft Theorem 18.5 ("*There is no positive prime block to add.*").

**Why it is wrong.** D.12's question is about real `F` with `supp F ⊆ [−T,T]`, `T` slightly above
`½log2`. Thm 8bis.4a's witness is built (Step 1) by choosing `δ > 0` from the continuity of `ω̂_{fin}`
and concentrating `ĝ` on `|τ| ≤ δ`; its `g` therefore has support of size `≳ 1/δ`, uncontrolled and
certainly not `≤ T`. Remark 8bis.4b states the limits explicitly: "It is a **fixed-chart** statement, and
it is **not** claimed in the colimit"; "the two scales in the argument … become comparable"; "The colimit
version is therefore `OPEN`". Nothing in it bears on narrow-support tests. Using it to conclude "the
finite half alone carries no positivity to donate" in the semilocal window is out of scope.

**Minimal repair.** Downgrade Theorem D.12.5 to: "at every finite chart the pure Frobenius form is
positive on *some* primitive class (Thm 8bis.4a), with support uncontrolled; whether this persists under
the support restriction of D.12 is `OPEN`." Draft Theorem 18.5's italic gloss must be deleted.

---

### H10 (`MAJOR`) — CC's vanishing conditions are **not** primitivity; the identification is one of the draft's "two load-bearing" ones

**Location.** §3.2 Corollary D.12.2 ("`ĝ(±i/2) = 0 ⟺ Φ_F(1) = Φ_F(0) = 0` (primitivity)"); §4.1 table row
`[cc:236–239]` ("*the same two linear conditions*"); draft §19 second bullet.

**Why it is wrong.** Two distinct slips, in the same direction.
1. CC's hypothesis is on `g`, and it is **one** condition: Theorem 1 `[cc:109–111]` asks "Fourier
   transform vanishing at `i/2` and `0`"; Theorem 6.11 `[cc:3108]` asks "vanishes at `−i/2`". The corpus
   imposes **two** on `F` (`Φ_F(0) = Φ_F(1) = 0`). One is not the other.
2. CC's (11) `[cc:236–239]` is stated for the test function `f` (`= g⋆g^*`). In the corpus's factorized
   normalization `Φ_{F⋆F^∨}(0) = Φ_F(0)Φ_F(1) = Φ_{F⋆F^∨}(1)`, so both conditions of (11) reduce to the
   **single** equation `Φ_F(0)Φ_F(1) = 0` — strictly weaker than primitivity of `F`.

Corollary D.12.2(a) is therefore *safe* (it hypothesizes more than CC need, so the conclusion still
holds), but it is advertised as "Hence, **exactly**:", and the dictionary entry and draft §19 assert an
identity that does not hold. In a document whose declared value is the dictionary, this is load-bearing.

**Minimal repair.** State: "CC's condition on `g` is the single linear condition `∫g(ρ)ρ^{∓1/2}d^*ρ = 0`;
on `f = F⋆F^∨` the pair (11) collapses to `Φ_F(0)Φ_F(1) = 0`. Primitivity implies it and is strictly
stronger." Correct §4.1 and draft §19.

---

### H11 (`MAJOR`) — most of §4.1's `RESTATEMENT` rows are analogies; one entry is an opinion

**Location.** §4.1 table; §4.4 Statement D.13.3; draft §19 Statement 19.2.

**Why it matters.** The blueprint asked to "distinguish exact identities from analogies dressed as
identities", and the report's §4 preamble promises "`RESTATEMENT` or `IMPORTED`" throughout. Checked
against the source:
* **Exact, verified:** `Q = −(ρ∂_ρ)² + ¼ ↔ Π = −∂_t² + ¼`. CC's footnote `[cc:1445 fn]` gives the symbol
  `z² + ¼`, and `s(1−s)|_{s = ½+iz} = ¼ + z²`, with `ρ∂_ρ = ∂_t` at `t = log ρ`. Correct, and the best
  thing in §4.
* **Analogy, no derivation offered:** "`∆` ↔ the polar/archimedean packet carried by `K` and by
  `2Φ_F(0)Φ_F(1)`"; "`Σ` ↔ the Frobenius lattice `Λ_W ⊂ 𝓝_∞`"; "`δ(ρ)` ↔ the `2×2` Tate block `𝔅_T` and
  the border `Σ(T)`"; "scaling kernel ↔ `Frob_n`". CC's `∆` and `Σ` are two regions of the first quadrant
  (`[cc:588]`, Figure 1); no map from either to a lattice of translates of `ΠK`, or to a `2×2` block, is
  constructed anywhere. These are labelled `RESTATEMENT`. They are `HEURISTIC`.
* **Circular:** §4.4's argument ("CC's `Σ` is a reservoir of positivity; the corpus's structural analogue
  of `Σ` is the radical, a reservoir of zeros; therefore `∆ → Σ` transfers only as a dimension count")
  takes its premise from the table row it is meant to justify. It also carries "This is a new and, **I
  think**, the correct reading" — an opinion inside a labelled statement — under the label
  `RESTATEMENT` + `OPEN`.

**Minimal repair.** Split the table into "exact identity (with the computation)" and "analogy, `HEURISTIC`".
Only the `Q = Π` row and, once H10 is fixed, the vanishing-condition row survive the first column.
Relabel §4.4 and draft §19.2 `HEURISTIC`, and delete "I think".

---

### H12 (`MAJOR`) — the "disqualified in advance" criterion repeats a non-sequitur Paper 46 already withdrew

**Location.** §2.5 verdict box; refutation B6; draft Remark 17.7 ("Any `h⁰` whose growth is driven by
kernel decay is disqualified in advance", `PROVED`).

**Why it is wrong.** Paper 46 Restatement 12.4a and Remark 12.4a′ (the repair of round-2 finding M1)
state the point explicitly: "a uniformly defined rule `Z ↦ h⁰_Z` may perfectly well satisfy (a)+(b′)+(c)
for `ξ` and fail them for `Ξ_a`, and Theorem 12.4 forbids only the latter"; what is excluded is a
**model-free proof**, never a function. Draft Remark 17.7 disqualifies a *class of functions* from the
behaviour of the `Ξ_a` analogue — the exact form M1 withdrew. It is also empty on its own terms: both
bounds are lower bounds of size `(log m)^{2}` at most, astronomically below the `¼m²` that (c) demands,
so `Ξ_a` fails (c) here as surely as `ξ` does and the comparison carries no information either way.

**Minimal repair.** Reduce to the schema Paper 46 already has: "the §2.3 construction is model-uniform in
the sense of (12.3), so by Restatement 12.4a no proof of (a)+(b′)+(c) can rest on it alone." Label
`RESTATEMENT`, not `PROVED`.

---

### H13 (`MAJOR`) — `REFUTED` is attached to methods and to non-applicability, not to false statements

**Location.** §3.4 heading and its `REFUTED (blueprint D.12(ii) as a method)`; refutation table rows B1,
B3, B4; draft Remark 18.6 (`REFUTED`) and the ledger row "Rem 18.6 | `REFUTED` | closes the Doc-135 route".

**Why it matters.** The report enforces label discipline on everyone else. `REFUTED` should mean: the
statement is false. What §3.4 establishes is that Doc 135's Theorems A/A′ live in the constructive regime
and do not apply to the destructive one — which is what Doc 135 itself says at `[135 §7.2 B3]` and what
it files as its own open problem `[GAP-135.B]`: "el primer caso genuino de H⁺: el objeto semilocal
`(Λ·1_{\{2^m,3^n\}}, [0]+[1], ω_std)` … Decidir H para ese objeto". Non-applicability of a named method is
`NOT-APPLICABLE` or `OPEN`, and the content here is `RESTATEMENT` of Doc 135's B3, not a new refutation.
Likewise B1 refutes a *question's dichotomy* and B4 refutes a *conjecture the blueprint offered for
proof-or-refutation* — neither is a false statement demonstrated false.

**Minimal repair.** Relabel §3.4 / Remark 18.6 `RESTATEMENT` + `NOT-APPLICABLE`, crediting Doc 135 §7.2 B3
and GAP-135.B; relabel B1 "question ill-posed", B4 "conjecture answered: no".

---

### H14 (`MAJOR`) — CC's `W_∞` is imported into Paper 46's normalization without checking the sign

**Location.** §3.2 Corollary D.12.2 and §3.5(i); draft Corollary 18.3.

**Why it matters.** §3.1 is a two-paragraph demonstration that getting this sign wrong inverts the whole
question — and then §3.2 imports `W_∞(g⋆g^*) ≥ Tr(ϑ(g)Sϑ(g)^*)` and rewrites it as `W_S(F) ≥ 0` in
(D12.1)'s normalization with no verification at all. The reader must take on faith that CC's `W_∞` equals
`2Φ_F(0)Φ_F(1) − ⟨F⋆F^∨, ω_∞⟩`. (It does: CC define `W_∞ := −W_R` at `[cc:88–90]`, flagged in their own
text as "note the change of sign", and their statement is "Weil's **negativity**" for the geometric side —
which matches `⟨h, W_{fin}+ω_∞⟩ = PRIME − ARCH ≤ 0` on primitive `h`. But the report does not say so.)

Related omission: CC state their semilocal programme at `[cc:82–84]` — "provide a conceptual reason for
Weil's negativity for functions `f` fulfilling the support condition `Support(f) ⊂ (p^{−1},p)`" — which is
verbatim D.12(ii). §3.5(ii) declares D.12(ii) `OPEN` "not provable by the means named" without citing
that CC name it as their next step.

**Minimal repair.** Insert the normalization check with the `[cc:88–90]` citation; cite `[cc:82–84]` in
§3.5(ii).

---

### H15 (`MAJOR`) — Theorem D.11.6(i)'s `Ξ_a` transfer is asserted, not proved, and has no check

**Location.** §2.5, proof of Theorem D.11.6(i) (`PROVED`): "the only non-verbatim point is that `Π_PK_a`
is *positive* for large `|u|` (its leading term is `K_a^{(4)} ∼ K_a·((log K_a)')^4 > 0`) … with `u_0, M_+`
replaced by `v_0 := sup\{u>0 : Π_PK_a(u) ≤ 0\} < ∞` and `M_- := max(−Π_PK_a) < ∞`, both finite by the same
continuity-plus-asymptotics argument as in §2.0."

**Why it is unproved.** The sign of `Π_PK_a` at large `|u|`, the finiteness of `v_0` (i.e. that
`\{Π_PK_a ≤ 0\}` is bounded, not merely that the function is eventually positive along a subsequence),
and the finiteness of `M_-` are three asymptotic assertions with no derivation and — unlike the `ξ` case —
**no numerical check whatsoever**: `scripts/d137_lattice.py` computes `K`, `ΠK`, nothing about `K_a` or
`Π_PK_a`. The whole of Theorem D.11.6 is nevertheless labelled `PROVED`. The sign of the feasible
coefficients (`a_q ≥ 0` for `Ξ_a` versus `a_q ≤ 0` for `ξ`) is the one point where the transfer is *not*
Proposition 12.6's four substitutions, and it is the point left unargued. (I checked the coefficient sign
independently against the `Ξ_a` analogue of Lemma 13.5b — `π_P(σ) → +∞` as `σ → +∞` forces `a_Q ≥ 0` —
and it is consistent; that is the only part of the paragraph I could confirm.)

**Minimal repair.** Either prove the three asymptotics for `K_a` (the `K_a = (e^{at}K)⋆(e^{−at}K)`
representation makes `K_a^{(4)} ∼ K_a((log K_a)')^4` accessible) and add a `C5` check for `Π_PK_a`, or
relabel Theorem D.11.6 `CANDIDATE`.

---

### H16 (`MINOR`) — mis-citations in D.0 and in the `NO-GO-LIST.md` entry

**Location.** §1.4; `NO-GO-LIST.md` point 2 and header paragraph.

1. "`D8.5b-i` §4: the divergence 'lives in the non-additive cross terms of the Feshbach resolvent'" — that
   phrase is in **§5** (Theorem `thm:robust`, third bullet), not §4. §4's auditbox supplies only the
   second half of the quote ("`G_P^∘` is the genuine Feshbach resolvent `Φ^*F_P^{-1}Φ`"). Repeated in the
   `NO-GO-LIST.md` entry.
2. The `NO-GO-LIST.md` entry attributes the audit order to
   `phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md §3`. It was ordered by
   `R137_000_LEAD_BLUEPRINT.md` item D.0.
3. §1.4 calls the §2-versus-§5 discrepancy "a direct contradiction" and "unreconciled … on the one point
   that decides the audit". The two sentences are about different objects (which mode carries the
   divergence in the Hamiltonian, versus where it lands in the Feshbach inverse); the honest statement is
   the one the report makes in the next sentence — that `RH-PROOF.md` nowhere reconciles them. It is a
   gap, not a contradiction.

**Minimal repair.** Fix the two section numbers and the attribution; downgrade "contradiction" to
"unreconciled gap".

---

### H17 (`MINOR`) — "L1 ⟹ RH" is stated as a bare implication; the true implication is a conjunction

**Location.** §1.3 ("Therefore, by the document's own §5, **L1 `⟹` RH**"); the header note added to
`RH-PROOF.md`; `NO-GO-LIST.md` point 1.

**Why.** §5's chain consumes G1–G5 and L1, L2, L3 (both L2 and L3 are used inside §3, which §5 depends
on); §6 itself lists all three as "residual analytic estimates not written in full detail". What follows
is `L1 ∧ L2 ∧ L3 ∧ (G1–G5) ⟹ RH`, hence: **at least one of L1–L3 is not a statement that "cannot encode
zero locations"**, and the report's separate argument that L2, L3 are genuine `Re s > 1` identities is
what narrows it to L1. That argument should be part of the statement, not adjacent to it.

Also noted, and not addressed by the audit: `D8.5b-i` §6 asserts as "Established (unconditional)" that
"`G_P^∘` is a normal family (`≤ 1/|Im z|`)". That is an *operator-norm* bound and does not give the
sourced matrix entries `⟨(A_P−z)^{-1}ι_Pφ_β, ι_Pφ_α⟩` a `P`-uniform bound without L1 — so the report's
identification survives — but it is the one competing reading under which `RH-PROOF.md` might have
escaped, and the audit should close it explicitly rather than leave it standing in the same phase.

**Minimal repair.** State the conjunction, then the narrowing; add one sentence closing the `D8.5b-i` §6
reading.

---

### H18 (`MINOR`) — reproduction section, script, and README do not match the report

**Location.** §7; `scripts/d137_lattice.py` docstring and checks; `README.md` row for the script.

1. `--fast` does **not** reproduce the report's constants: it prints `u0 = 0.22`, `κ_2 = 7.45243·10⁻⁶`,
   `m0 = 1 115 015` against the report's `0.235`, `4.41176·10⁻⁶`, `1 883 507`. §2.0 says these are "all
   checked in `scripts/d137_lattice.py` … `--fast` 5 s". A `--fast` reader sees different numbers and no
   warning. (Both are wrong: see H1.)
2. Docstring: "C4 the single-generator feasibility threshold `m0(q)` of **Theorem D.11.4**" — it is
   Theorem D.11.2.
3. Docstring: "C3 the explicit lower bound `K(t) >= pi^2 e^{9t/2} exp(-pi e^{2t})`" — both the code and
   the report use `2 pi^2`.
4. `README.md` calls the script "passing". It passes; see H1 for what it passes on.

**Minimal repair.** Make `--fast` print a warning that its grid is too coarse for the quoted constants
(or make the reported constants grid-independent per H1); fix the two docstring errors.

---

### H19 (`MINOR`) — Theorem D.12.4: an arithmetic slip and a trivial "theorem"

**Location.** §3.3 Theorem D.12.4 (`PROVED`); draft Theorem 18.4.

1. With `F := φ + τ_{\log2}φ` and `a := \log 2`, `F⋆F^∨ = 2(φ⋆φ^∨) + τ_a(φ⋆φ^∨) + τ_{−a}(φ⋆φ^∨)`, so
   `(F⋆F^∨)(a) = 2(φ⋆φ^∨)(a) + (φ⋆φ^∨)(0) + (φ⋆φ^∨)(2a) = (φ⋆φ^∨)(0) + O(ε\text{-tails})`, **not**
   `2(φ⋆φ^∨)(0)`. The sign conclusion is unaffected.
2. "the functional `F ↦ −⟨F⋆F^∨,W_2⟩` is **not** nonnegative" is immediate: `W_2` is a positive atomic
   measure and `F⋆F^∨` can be made positive at `\pm\log 2`. No two-bump construction is needed, and
   calling it a `PROVED` theorem inflates it.
3. "Hence no monotonicity argument in `S` gives positivity" does not follow. `W_S` is decreasing in `S`;
   the target `W_{\text{all}} ≥ 0` is at the bottom of the chain. What is correct is the converse
   statement — that `W_{\{∞\}} ≥ 0` gives no information about `W_{\text{all}}` — and that is worth
   saying in place of the present sentence.
4. `2(\log2)2^{−1/2} = 0.98026…` — the constant and its sign are correct (checked against the `k = 1`
   term of `⟨h,W_2⟩` with `h` even).

**Minimal repair.** Fix (1), demote (2) to a remark, rewrite (3).

---

### H20 (`MINOR`) — the chosen minimum in §2.3's `κ_q` bound, and `N_q = 0`

**Location.** §2.3, the display `κ_q ≥ 2π²e^{9(\log q+u_0)/2}e^{−πq²e^{2u_0}} ≥ e^{−βq²}`; and
`N_q := \lfloor κ_qm/(dM_+w_q)\rfloor`.

Both are fine but neither is justified in the text: the first needs the stated monotonicity of the whole
majorant on `[1,∞)` (given, one line later) *and* `2π²e^{9(\log q+u_0)/2} ≥ 1` (not stated); the second
needs `N_q ≥ 1`, i.e. the bracket `\log m − βq² − \log d − \log(M_+/w_q)` positive, which the choice of
`Q` supplies only "for `m` large" — the quantifier ordering `c, m_1` versus `Q(m)` should be written out.
No error; the proof is otherwise correct and I reproduced it.

---

## Per-item verdicts

| item | verdict |
|---|---|
| **D.0** (audit of phase-65 `RH-PROOF.md`) | **CONFIRMED WITH REPAIRS.** The verdict `REFUTED` on `RH-PROOF.md` is correct and I find no reading under which that document survives as a proof: it is explicitly conditional on L1–L3, the uniformity in `P` that Montel needs is exactly L1, and §4's `thm:rich` is in any case a sketch. §1.2's assessment of the Vitali step is correct (I checked: uniform boundedness → Montel → identity theorem on a connected domain → a meromorphic function agreeing with a holomorphic one has no pole). Repairs required: **H7** (the central sentence of the FATAL flag is false and self-contradicted), **H8** (the R3 banner and `CORRECTIONS-CONNES-R3.md` were never read), **H17**, **H16**. |
| **D.11** (growth of `h⁰_Z(mK)`) | **CONFIRMED WITH REPAIRS in its analytic core; REFUTED in its headline.** Theorem D.11.1 is correct as stated (I verified (i)–(iv) against Definition 11.6, (11.9) `deg K = 1`, Theorem 11.13(ii) and Lemma 13.5b). Theorem D.11.2 is correct in structure but its constants are false (**H1**, `FATAL`). Theorem D.11.3 is correct modulo the same constant (**H1**) and the ungrounded (D11.2) (**H5b**) — I reproduced the optimization and it gives `(\log m)^{3/2}/\log\log m`. Theorem D.11.4 has a false displayed majorant (**H3**, repairable in one line) and an undeclared zero-location import (**H5a**). Corollary D.11.5's "equivalence" is overstated (**H4**). Theorem D.11.6 is `CANDIDATE`, not `PROVED` (**H15**), and the comparative conclusion built on it is **REFUTED** (**H2**, `FATAL`), as is the derived disqualification criterion (**H12**) and the claimed correction of Remark 13.6a (**H6**). |
| **D.12** (semilocal positivity) | **CONFIRMED WITH REPAIRS.** The sign refutation of the blueprint (§3.1, B2) is **correct** — I verified against Theorem 11.3 (11.4), Lemma 11.4a and Theorem 11.5 that `Σ_{v}⟨F⋆F^∨,W_v⟩ − 2Φ_F(0)Φ_F(1) = −Σ_ρΦ_F(ρ)Φ_F(1−ρ)`, so the blueprint's `W_S ≥ 0` is the anti-Weil inequality; (D12.1) is the right correction. Theorem D.12.1 is correct and trivial. The CC window and the reconciliation of the two support conventions are correct. Repairs required: **H10** (the vanishing conditions are not primitivity), **H9** (Thm 8bis.4a out of scope), **H14** (sign of CC's `W_∞` never checked; CC's own semilocal programme not cited), **H13** (label), **H19**. Open item D.12-α is well-posed as an acceptance test, and I endorse it. |
| **D.13** (dictionary with CC) | **CONFIRMED WITH REPAIRS.** Every `[cc:NNN]` I spot-checked (144, 186, 193, 204, 226, 236, 243, 258, 264, 289, 588, 1445, 1519, 1766, 3108, 3163) resolves to the quoted material; `13 < c < 17` is at `[cc:3163]`; Theorem 6.11 at `[cc:3108]` (which says `−i/2`, the intro `i/2` — harmless). The `Q = Π` identification is **exact and correct**, and is the section's real result. Everything else in the table is analogy under a `RESTATEMENT` label (**H11**), the primitivity row is wrong (**H10**), and the `∆ → Σ` "dimension count" reading is an opinion labelled `RESTATEMENT` (**H11**). |

**Overall verdict: CONFIRMED WITH REPAIRS, with two `FATAL` findings that must be cleared before any part
of this round enters Paper 46.** The round's genuine, surviving results are: the sign correction of the
blueprint's `W_S` (§3.1); the support decoupling (§3.2); the two-sided Mellin bound (Theorem D.11.1);
the super-logarithmic lower bound (Theorem D.11.3, modulo H1/H5b); the exact identity `Q = Π`; and the
correct localization of `RH-PROOF.md`'s wall at L1. Its headline claims — "more sections than `ξ`", "the
growth is anti-correlated with the sign", "Remark 13.6a corrected", "item (23) is equivalent to `Q(m)`",
"CC's conditions are primitivity" — do not survive.

On the builder's advice **against opening D.14**: I agree with the conclusion and reject the stated
reason. The reason given is Theorem D.11.6's anti-correlation, which is H2. The sound reason is the one
in the same paragraph: the gate measures `(\log m)^{3/2}` against a requirement of `¼m²`, and Corollary
D.11.5(iv) — once restated per H4 as a one-sided implication — quantifies the distance. D.14 should stay
closed on that ground alone.

**Ruling on the Part III draft.** Do not append. §17.4 as written would violate Paper 46 §1.13 (H5a);
Theorems 17.2, 17.6 and Remark 17.7 and the ledger rows for them are carried by H1, H2, H6, H12, H15;
§19's second load-bearing identification is H10. The draft's own reason 1 for not appending (the
protocol) is correct and is now vindicated concretely.
