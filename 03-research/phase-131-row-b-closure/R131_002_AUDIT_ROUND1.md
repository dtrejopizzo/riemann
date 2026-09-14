# R131.002 — Hostile audit, round 1: Paper 44 after the phase-131 rebuild

Auditor: Claude (Opus 5, 1M), acting as adversary. Date: 2026-09-12.
Target: `04-papers/44-row-b-arithmetic-family/main.md` (`[REBUILT, phase 131]`
passages), against `R131_000`, `R131_001`, `D128_002_AUDIT_B.md`, Paper 43
(post-phase-130), P123.018/022/037/038/039/042/060/082, PLAN §6.

Method: every new theorem was re-derived from Paper 43's displayed formulas
((8.5), (8.5a), (8.5b), (8.5∞), Lemma 3.3, (9.5b), Thm 8.8, Def 8A.7d,
Thm 9.14a0/9.14b) and from P123.042 §1, not accepted on citation. The numerics
in `scripts/verify_131_contacts.py` were re-run (all pass; they prove nothing).

**Headline.** The *calculations* of §3bis are correct — I could not break
Lemma 3bis.1, Prop 3bis.2, the shell computation of Thm 3bis.7, the
archimedean half-sum of Thm 3bis.8, or the strong-dual argument of Thm 8.3.
What I did break is the *framing*: the object is not an ideal, the amended
B.4 is ill-typed as stated, one phase-128 finding (B2) is re-worded rather
than repaired and is regressed to `PROVED` in the ledger, and the proof of
Thm 8.1(iii) still contains — and now asserts — the very invalid inference
D128.002 B1 accepted as an error. Row B's carrier-side content reduces, after
the relabelling is stripped, to Paper 43 Remark 9.7a restricted to radial
tests, plus two genuinely new items (the `n−1` diagnosis, and membership in
`N_A^dist`).

---

## 1. Findings

### F1. `FATAL (framing)` — `Γ_n^rad` is not "the ideal class". Def 3bis.4, Rem 3bis.4a, banner, §0, §10.

The standing hypothesis of §3bis is `S ⊇ {∞} ∪ P(n)` (Lemma 3bis.1), and the
proof of Lemma 3bis.1 turns on `n ∈ Γ_S`, i.e. **`n` is an `S`-unit**. Then
`nZ_S = Z_S`: the ideal `(n)` of `Z_S` is the unit ideal. The entire
"ideal class / all generators of the ideal `(n)`" reading of (3bis.3) and
Remark 3bis.4a is therefore vacuous on the very chart where Lemma 3bis.1
applies — and the two statements are in direct tension: the class has unit
finite coordinates *because* `n` has been inverted, which is *also* why there
is no ideal left to be the class of.

What (3bis.3) actually is: the normalized Haar measure of the level set
`{x ∈ C_S : |x|_S = e^{−t}}` at `t = log n`, i.e. `Γ^{rad}_{(t)}` — an object
the paper itself defines for **every real `t`** two lines later. Consequences
the paper does not draw:

* the assignment `n ↦ Γ_n^{rad}` factors as
  `(N_{≥1},×) ↪ (R_{>0},×) → {level-set measures}`; the second map is an
  isomorphism of topological monoids. So the realization carries **no**
  arithmetic information: it forgets factorization entirely, and
  `Γ_6^{rad}` differs from `Γ_{6.0001}^{rad}` by nothing structural;
* every clause proved "for the ideal classes" — B.2 (Thm 3bis.5(i),(iv)),
  B.3 (Thm 3bis.5(ii),(iii)), the first half of B.6 — is a statement about
  `R_{>0}` and its Haar-coset measures, provable with `n` replaced by any
  positive real. They are true, and they are empty of arithmetic;
* for composite `n` the object has finite contact `0` and archimedean contact
  equal to the generic density value: `Γ_6^{rad}` is not distinguished from
  `Γ_t^{rad}`, `t` generic, by anything in the paper. So "the general family
  proved by structure" (B.6, Prop 7.1) is proved about a family whose
  composite members carry no content.

**Repair (required).** Rename throughout: `Γ^{rad}_{(t)}` is the *modulus
class*, or *level class*; `Γ_n^{rad} := Γ^{rad}_{(\log n)}` is its value at an
integer label. Delete Rem 3bis.4a or restrict it to a genuine ideal-theoretic
setting (`n` **not** an `S`-unit, i.e. a chart with `P(n) ⊄ S_f`) and then
re-prove Lemma 3bis.1 there — where it will *fail*, since `φ(a_S(n)) ≠ n`.
Restate B.1/B.2 as: the source monoid embeds in the modulus group, and the
arithmetic is carried by the *atoms of the trace*, not by the objects.

### F2. `MAJOR` — the amended clause B.4 is ill-typed as written; what is proved is not what it says. §2 table, §6.2a′, Thm 6.3a.

The amendment reads: "the derived contact of `Γ_n^{rad}` with the diagonal …
that is, **the value on it of Paper 43's declared trace `T`** …". But
`Γ_n^{rad} ∉ D_A` (Rem 3bis.4b(i)), `T` is defined on `D_A` only (Paper 43
Def. 8.6), and the paper nowhere extends `T` to multipliers. So `T(Γ_n^{rad})`
is undefined, and the amended clause as stated has no content. This is
verbatim the type error the builder charges against the lead's blueprint
(R131.001 §3 item 4); it survives in the two places where it matters most
(the contract table §2 and the boxed amendment the owner is asked to adopt).

Worse, the naive reading is not merely undefined but *false-adjacent*: for
`|S_f| ≥ 2`, `Im j_p ∩ {|x|_S = 1/n}` is a single point in each `Z_r^×`,
`r ≠ p`, hence a `Γ_n^{rad}`-null set (Prop 3bis.2's own computation). Any
extension of `W_p` to measures by `a = F∘j_p` gives `W_p(Γ_n^{rad}) = 0`, not
`Λ(n)n^{−1/2}`. The number `Λ(n)n^{−1/2}` is obtained only as the **atom mass
of the disintegration** `ω_{fin}` of `T|_{D_A^{rad}}` along the family
(Def–Thm 3bis.8), which is a *definition of the word "contact"*, canonical
(`ω_{fin}` is a unique Radon measure) but not an evaluation of `T` at the
object. Thm 6.3a(i) does state it correctly; the clause and §6.2a′ do not.

**Repair.** Replace "the value on it of Paper 43's declared trace `T`" by
"the mass at `t = log n` of the unique Radon measure `ω_{fin}` disintegrating
the finite-place part of `T` along the radial family `{Γ^{rad}_{(t)}}`", and
add one sentence stating explicitly that `T(Γ_n^{rad})` is undefined and that
any naive place-wise evaluation returns `0` because the slice image is null.
Without that sentence the reader is invited to believe more than is proved.

### F3. `MAJOR` — D128.002 B2 is not repaired; the ledger regresses it to `PROVED` with the same truncated quotation.

D128.002 B2 was `ACCEPTED` and restored **both** open items, because the
quotation of P123.038 §5 had been truncated. The full demand is:

> "the lattice-index operation must be realized as the admissible diagonal
> shadow, **extended cyclically to mixed correspondences** and compared with
> the analytic **nuclear** trace. **An invariant of the arithmetic family does
> not itself provide that trace functor.**"

and P123.039 §5 adds: "**A collection of equal trace values is insufficient
for those functorial claims.**"

Remark 3bis.10b quotes it as: "the lattice-index operation realized as the
admissible diagonal shadow … compared with the analytic trace" — the same
truncation, dropping "extended cyclically to mixed correspondences", dropping
"nuclear", and dropping the sentence that pre-emptively rejects what is then
supplied. What Thm 3bis.10(ii) supplies *is* a collection of equal numerical
values: `log[L_S:nL_S] = log n = Σ_{d|n}Λ(d)`, in which the left equality is
definitional (P123.038 §4, phase-128 B2) and the right is the classical
identity `Λ = μ∗\log`. No cyclic extension, no mixed correspondences, no
functor.

The §10 open-item table then lists **two** rows, both marked `PROVED`:
"lattice-index operation must be realized as the admissible diagonal shadow |
P123.038 §5 | `PROVED`: (6.1)" — which is exactly the entry D128.002 B2
refuted — and "the lattice-index operation compared with the analytic trace |
P123.038 §5 | `PROVED`: Thm 3bis.10(ii)". Splitting one open item into two and
marking both `PROVED` is a ledger regression, not a repair.

**Repair.** Restore both rows to `OPEN`, quote P123.038 §5 and P123.039 §5 in
full (including the two disqualifying sentences), and state that Thm 3bis.10
supplies a numerical comparison only, explicitly acknowledged as insufficient
by P123.039 §5.

### F4. `MAJOR` — the proof of Thm 8.1(iii) still contains D128.002 B1's invalid inference, and now proves a false statement; it contradicts §7 check 5.

Statement (iii) was corrected: "the arithmetic family **is** separated by the
ruling plane". But the *proof* was not: it reads

> "if `Λ(n)` were a function of the ruling data it would be a function of `n`,
> hence determined by `log n`, but `Λ(4)=Λ(8)` with `log 4 ≠ log 8` shows the
> level sets differ, **so `Λ` is not pulled back from the ruling plane**."

This is the exact fallacy D128.002 B1 accepted, and its conclusion is false:
`Λ(n) = f(\log n)` with `f(t) := \log p` if `e^t = p^k` and `0` otherwise, so
`Λ` **is** pulled back from the ruling plane. §7 check 5 of the same paper
says so ("`w_ram(Γ_n)=n^{−1/2}` is injective in `n`, hence determines `Λ(n)`").
The paper therefore asserts `P` in §7 and `¬P` in the proof of Thm 8.1(iii).

**Repair.** Delete the second clause of the proof of (iii) entirely; the
correct content is the first clause plus §7 check 5.

### F5. `MAJOR` — B.7's "mechanism located on the carrier" is a reinterpretation, not a theorem; PLAN §6's stopping rule is not met. Thm 6.5.

Thm 6.5(i) is correct and trivial (`|1−p^ku|_p = 1` for `k ≥ 1`). Thm 6.5(ii)
is correct and trivial (translation invariance of `d^*x`: `vol(p^kZ_p^×) =
vol(Z_p^×) = \log p`). The claim of interest is the *matching*: "this is the
carrier-side statement matching `Φ_p(1) = Φ_{p²}(1) = p`". That is a
coincidence of two independently-constant quantities with **no map between
them**: `Φ_{p^k}(1) = p` holds because `Φ_{p^k}(x) = Φ_p(x^{p^{k−1}})`, which
has nothing to do with Haar translation invariance. PLAN §6 asks to "locate
the mechanism"; producing two constants and observing they are equal is
precisely what P123.039 §5 disqualifies ("a collection of equal trace values").
Rem 6.5a honourably flags the `μ_n`-in-measure-form sentence as a dictionary;
the *same* flag belongs on Thm 6.5(ii)'s "matching" clause, which is currently
inside a `PROVED` theorem.

**Repair.** Demote the matching clause of Thm 6.5(ii) to a remark labelled
"numerical coincidence, no map supplied"; restate B.7's status as
`PROVED (the test: the two contacts differ); PARTIAL (the mechanism)`.

### F6. `MAJOR` — the two "contacts" are not comparable objects, and the archimedean one is not a contact of `Γ_n^{rad}` at all. Def–Thm 3bis.8, Rem 3bis.8a, §9.2.

`contact_{fin}` is the atom mass of a measure — an invariant of the single
level class. `contact_∞ := (ω_∞/dt)(\log n)` is the *value of a continuous
density at a point*: it is an invariant of `ω_∞` and of the label `t = \log n`,
and is defined for every real `t`. Nothing about the object `Γ_n^{rad}` enters
it. Rem 3bis.8a says the two are "of different type" and are "not added",
which is honest, but the paper then calls both "contacts of `Γ_n^{rad}`"
(banner, §0, §7 table, §9.2, Thm 6.3a) and presents (9.2) as discharging
D128.002 B6 ("the archimedean place is dropped without accounting"). It is not
an accounting of the archimedean contribution *of the arithmetic family*; it
is the value of row A's archimedean local density at a point of its argument.

**Repair.** Rename `contact_∞(Γ_n^{rad})` to `ω_∞(\log n)` — "the archimedean
density of row A's trace at the label `\log n`" — and state that no
archimedean quantity is attached to the object. D128.002 B6 is then answered
as: *the archimedean place contributes a density, and the family has no atom
there*; that is a correct and adequate answer, and it does not need the word
"contact".

### F7. `MINOR→MAJOR` — the realized family is not closed under `†`; B.3 is proved about a larger family than B.1 declares. Thm 3bis.5(ii), §10 B.3 row.

`(Γ_n^{rad})^† = Γ^{rad}_{(−\log n)}`, the Haar measure of `{|x|_S = n}`. This
is **not** in `{Γ_m^{rad} : m ∈ N_{≥1}}`. The paper writes it `Γ_{1/n}^{rad}`
and moves on. A dagger structure requires an involution of the realized
family; here the dagger leaves it, so what is actually realized is the monoid
`Q_{>0}` (or `R_{>0}`) with its inversion, of which `(N_{≥1},×)` is a
non-`†`-stable submonoid. Clause B.1's source category, as stated, has no
dagger at all.
Also in Thm 3bis.5(ii): "Each `Γ_n^{rad}` is `†`-real in the sense that it is
a positive measure" is a non sequitur — `†`-real means `Γ^† = Γ`, which is
false for every `n ≥ 2`.

**Repair.** State the realized structure as a `†`-monoid on `Q_{>0}` (labels
`n` and `1/n`), and either extend B.1's source accordingly or record that
B.3's dagger is realized only after that extension. Delete the "`†`-real"
sentence.

### F8. `MINOR` — Prop 3bis.2 / Cor 3bis.3 fail for `|S_f| = 1`, and the "dissolution of `n−1`" is therefore chart-conditional; the paper never says so outside the hypotheses.

For `S_f = {p}` and `n = p^k`, `j_p(p^k·1) = (p^{−k}\text{ at }∞; 1\text{ at }p)
= δ_S(1/p^k)` exactly: the class **is** on the finite slice, Prop 3bis.2(ii)
is false, Cor 3bis.3 is false, and the "class meets no finite shell" argument
of §9.4(b), §9bis W1 and Rem 3.7 does not apply. The hypothesis `|S_f| ≥ 2` is
correctly carried in the two statements, but the *narrative* conclusions
("the `n−1` obligation is dissolved", "the class is on no finite slice",
banner and §0) are stated without it, and §1's standing convention only
requires `S_f ≠ ∅`. Since `S = {∞, p}` is the minimal legitimate chart for
`n = p^k`, this is not a vacuous case.
Note also that `|S_f| ≥ 2` is not a defect of the argument: it is the
statement that the *dissolution is a large-chart phenomenon*. Say it.

**Repair.** Add the hypothesis to every informal restatement, plus one
sentence: on the minimal chart the element class does sit on the slice, and
the `n−1` still does not appear there because `w_unit` is an empty product on
that chart (Thm 3.3, phase-128 B5 correction) — which is the consistent story.

### F9. `MINOR` — `Λ` is "derived" only in the sense already established by row A; row B earns nothing new here. Rem 3bis.8b, Thm 8.2, §10 audit ¶5.

`Λ(p^k) = \log p = vol_{d^*x}(p^kZ_p^×)` is not new: Paper 43 Remark 9.7a
already reads `Ŵ_p(χ) = Σ_k 2Λ(p^k)p^{−k/2}\cos(kτ\log p + kθ_p)` "since
`Λ(p^k) = \log p`", with the same P123.042 §1 shell-volume justification, and
already answers A.10 with the same three sentences. §3bis's derivation is
(8.5) evaluated on the radial pullback `Γ_h = h(−\log|x|_S)`; every step is
Paper 43's. Row B's claim "`Λ` is derived under Rem 9.7a's rule" is therefore
**inherited, not earned**, and Rem 3bis.8b should say so.
Separately: the normalization `vol_{d^*x}(Z_p^×) = \log p` is a *declared*
convention (Paper 43 (8.5), Rem 8.6a; P123.042 §1), chosen so that the local
measure is compatible with `dt` on the modulus line. It is self-consistent and
I do not contest it, but "`Λ` is a volume" is true relative to that choice,
and the choice is the one that makes the explicit formula come out. The
honest sentence is: *no zero, no RH, no positivity and no von Mangoldt input
is used; the normalization is declared and is row A's.*

### F10. `MINOR` — Thm 3bis.5(iv): the chart projection `π_{TS}` does not descend to idele classes; P123.018 §2 says so explicitly.

`π_{TS} : C_T → C_S` is asserted to be "the coordinate projection". On ideles
the projection `A_T^× → A_S^×` does **not** carry `Γ_T` into `Γ_S` (a
`T`-unit `q ∉ S` maps to a non-`S`-unit), and P123.018 §2 states in terms that
"projection `A_{S'}^× → A_S^×` also does not automatically descend modulo the
specified unit groups". The map used is really the projection of the
*coordinate models* `R^× × ∏_{p∈T_f}Z_p^× → R^× × ∏_{p∈S_f}Z_p^×` supplied by
Lemma 3.3's splitting, which is chart-dependent.
The *substance* of (iv) survives, because `Γ_n^{rad}` depends only on the
modulus, which Paper 43 Thm 8A.7c(d) proves chart-invariant, and because the
inflation statement (the one Paper 43's chart system actually uses) is
correct. But the proof as written leans on a map P123.018 refutes.

**Repair.** Drop the push-forward clause; prove (iv) from the modulus alone
(`Γ^{rad}_{(t)}(S)` is *defined* by `|·|_S`, and `|·|` is chart-invariant),
and keep only the inflation direction, which is the one `T_∞` needs.

### F11. `NOTE` — Thm 3bis.10 is, stripped, two classical identities.

(ii) is `\log n = Σ_{d|n}Λ(d)`; (iii) is `Λ(n) = \log|Φ_n(1)|`. Both are
classical, both are already Thm 5.3/Cor 5.3a. The new content is only the
substitution `Λ(d) = d^{1/2}·contact_{fin}(Γ_d^{rad})`, i.e. F2's definition.
The theorem is true; the word "matching" oversells it, and Rem 3bis.10b's
title ("the arrow P123.038 §5 asked for") is false (F3).

### F12. `NOTE` — citation hygiene.
(a) Rem 3.7 cites "Paper 43 Lemma 8.2" for the `c·\log|w|` regularization
ambiguity; the current Paper 43 Lemma 8.2 is the exact-orbital-values lemma
(`τ_p(p^k) = p^{−|k|/2}`), and the ambiguity statement is now Rem 8.6b /
Def 8A.7d. Stale number, retained from phase 128.
(b) Thm 3bis.7's proof cites "(9.14)" for the unit-packet vanishing "in
Fourier terms"; as R131.001 §3 item 5 itself notes, (9.14) is about a
character's coefficient. The direct argument given is correct and sufficient;
the parenthetical should be marked as an aside, which it nearly is.
(c) §11 Dependencies lists Paper 43 "Def. 8.1" as a used input while Rem 3.7
insists "nothing in row B depends on Paper 43's Definition 8.1". Reconcile.

### F13. `NOTE` — what I could **not** break (re-derived independently).
* Lemma 3bis.1: `φ(a_S(n)) = n`, `n ∈ Γ_S`, `a_S(n)/n = (1/n; 1,…,1)`,
  `|·|_S = |·|_∞` on `ker φ`. **Correct.**
* Prop 3bis.2(ii),(iii) for `|S_f| ≥ 2`: correct, including the neighbourhood
  construction (`v_r(q^{−k}−1)` finite).
* Thm 3bis.7, finite part: `a(p^kw) = h(k\log p)` is `w`-independent because
  `j_p(p^kw) ∈ \ker φ` with `|·|_S = p^{−k}`; the unit packet vanishes
  pointwise; shell part `= Σ_{k≠0}(\log p)p^{−|k|/2}h(k\log p)` matches (8.5)
  and Lemma 8.2(i) exactly, for `k < 0` as well (`τ_p = p^{−|k|/2}` both
  signs). **Correct, and the unit-packet vanishing needs no smallness
  hypothesis — the paper's strongest new step.**
* Thm 3bis.7, archimedean part: with (8.5a)/(8.5b),
  `½[1/(2|\sinh(t/2)|)·2 + …]` collapses to `K(t) = e^{−t/2}/(1−e^{−2t})`;
  I re-derived `½[e^{−t/2}/(1−e^{−t}) + e^{−t/2}/(1+e^{−t})] = K(t)` and
  `K(|t|)` symmetry. **Correct**, and the builder's rejection of the
  blueprint's `K = ∏Z_p^×` (R131.001 §3 item 2) is right: with the sign
  omitted the half-sum is unavailable.
* (3bis.11): `τ_∞(1/n) = n^{1/2}/(n−1)`, `τ_∞(−1/n) = n^{1/2}/(n+1)`,
  half-sum `= n^{3/2}/(n²−1) = K(\log n) = n^{−1/2}Σ_j n^{−2j}`. **Correct**,
  and Rem 3bis.8a's refusal to read `Σ_j n^{−2j}` as trivial zeros is right.
* Lemma 3bis.6a: `λ_∓(Γ_h) = ∫h(s)e^{±s/2}ds`, `Γ_h⋆Γ_g = Γ_{h∗g}`. Correct.
* Thm 3bis.5(i): Haar coset convolution. Correct. (iii): `λ_∓ = n^{±1/2}`.
  Correct.
* Thm 8.3: `\widehat{Γ_n^{rad}}` supported on `𝔠_0`, `= n^{iτ}`, modulus `1`;
  the `R`-then-`ε` split with `|Δ_ε| ≤ \min(2,|τ|ε)` against Lemma 9.14a0's
  `|\hat G| ≤ C''_B\min(1,τ^{−2})` and `|\hat T| = O(\log(2+|τ|))` gives
  genuine uniformity on bounded sets. **The strong-dual claim is earned.**
  (v)'s honesty — the ruling component is nonzero, the classes are *not*
  primitive — is a real and creditable concession.
* Table §7 and `verify_131_contacts.py`: re-run, all values reproduce.
* D128.002 B1 (statement), B4, B5, B6 (as far as F6 allows), B7, B8, B9:
  repaired in substance.

---

## 2. What survives

1. **Lemma 3bis.1 and Prop 3bis.2/Cor 3bis.3** (for `|S_f| ≥ 2`): the class of
   `a_S(n)` has unit finite coordinates, sits on the archimedean slice and on
   no finite slice; hence `w_unit = n−1` is a datum of the *lift*. This is a
   real correction, it kills a false obligation Paper 44 had handed to row C,
   and it is the best thing in the rebuild. §9.4's correction of Paper 45 §11
   is stated truthfully and with the right scope (it does not delete Paper
   45's computation, only its status as a discharge).
2. **Thm 3bis.7**: the exact evaluation of row A's declared trace on the
   radial sector, with no regularization and no counterterm, and with the unit
   packet vanishing *identically* on radial sections. Correct and clean —
   but see F9: it is (8.5) restricted, not a new theorem about arithmetic.
3. **Thm 8.3**: membership of the level classes in `N_A^{dist}` with
   strong-dual convergence, canonical components, and the explicit statement
   that they are **not** primitive. This is new, correct, and honest.
4. **The `Z`-linear side** (Thm 5.3, Thm 5.4, Cor 5.5, Thm 6.3): unchanged
   from phase 128 and still the only part of row B with genuinely arithmetic
   content. It is not in `G`, and the paper says so.
5. **The withdrawals §9bis W1–W4**: all four are correct and correctly
   reasoned. Recording them rather than deleting them is the right practice.

## 3. Verdict per clause

| clause | builder | auditor |
|---|---|---|
| B.1 source category | `PROVED` | **`PROVED`, trivially** — stating a category is free; the upgrade from `PARTIAL` is defensible only on the reading "no functor demanded". Add F7: the source has no dagger. |
| B.2 monoidal realization | `PROVED` | **`PROVED, but empty`** (F1): the functor factors through `R_{>0}` and forgets arithmetic. Independence of lift/gauge/chart: `PROVED` in substance, with F10's proof repair. |
| B.3 unit, transpose, half-densities | `PROVED` | **`PARTIAL`** — dagger not closed on the realized family (F7); unit and bidegree correct. |
| B.4 derived contact | `REFUTED AS STATED` + `PROVED AS AMENDED` | **`REFUTED AS STATED`** (agreed, three independent reasons) **+ `NOT YET PROVED AS AMENDED`**: the amendment as worded is ill-typed (F2). With F2's repair applied verbatim, the repaired amendment **is** proved. So: `PROVED AS AMENDED, CONDITIONAL ON RE-WORDING`. |
| B.5 `deg_det = \log|Φ_n(1)| = Λ(n)` | `PROVED` twice | **`PROVED`**, with F11: the second "proof" is the classical `Λ = μ∗\log` plus a definition. `n=1` handling is correct. |
| B.6 family by structure; classes in `N_A` | both halves `PROVED` | first half **`PROVED but vacuous for composite n`** (F1); second half **`PROVED`** (Thm 8.3 is sound). |
| B.7 discriminating test; mechanism | `PROVED` | **`PROVED` (the test); `PARTIAL` (the mechanism)** — F5. PLAN §6's stopping rule is not met on the carrier. |
| B.8 adversarial verification | `PROVED` | **`PROVED`** — table re-checked, numerics re-run. |
| B.9 compatibility; independence | `PROVED` | **`PROVED`** — no zero, no RH, no sign, no positivity, no `Λ` as input. With F9: the independence is row A's, inherited. |

## 4. The renaming test

**For the prosecution.** `Γ_h(x) = h(−\log|x|_S)` is the pullback of an
arbitrary test function along the modulus map. `T(Γ_h)` is then, by Paper 43
(8.5)/(8.5∞), Weil's prime-power packet plus the archimedean term — which
Paper 43 Rem 9.7a had *already* stated in Fourier form, with the *same*
`Λ(p^k) = \log p` and the *same* shell-volume justification. Row B's addition
on the carrier is to name the level sets `Γ_n^{rad}`, index them by `N`, and
call the atoms "contacts". The objects carry no factorization data (F1); the
degree matching is two classical identities (F11); the arrow P123.038 §5 asked
for is not supplied (F3); the B.7 mechanism is a coincidence of constants
(F5). On the carrier, **row B is largely a renaming** — an indexing of the
atoms of a measure row A had already computed.

**For the defence.** Three things are not renamings. (i) Prop 3bis.2 /
Cor 3bis.3 is a genuine geometric *discovery* with a negative consequence:
it deletes a quantity (`n−1`) that two previous phases believed was a contact,
and it deletes a false obligation on row C. You cannot rename your way to a
withdrawal. (ii) Thm 8.3 puts the classes in `N_A^{dist}` with proved
strong-dual convergence and proves they are **not** primitive — a falsifiable,
unwelcome, and therefore credible structural statement. (iii) The `Z`-linear
cube, `Prim`, `Φ_n(1)`, and Thm 5.4's refutation of monoidal primitive
extraction are real mathematics, independent of the explicit formula.

**Verdict.** Row B fails the renaming test *as a construction on row A's
carrier*, and passes it *as a bookkeeping-and-correction paper*. The
distinction matters for the label: what §3bis proves is a theorem **about row
A's trace**, not a theorem about an arithmetic family in `G`.

## 5. Label

**`WEIL-STRENGTH-COMPLETE` (row B): NOT EARNED.**

Not because of a false calculation — the calculations are, as far as I can
break them, right — but because:

* **F3** shows a phase-128 finding re-worded and regressed to `PROVED` in the
  ledger. The closure rule cannot be satisfied by a ledger that marks as
  proved an item the previous audit restored as open.
* **F4** shows an invalid inference, explicitly accepted as an error in
  D128.002 B1, still sitting in a `PROVED` proof and contradicting §7 of the
  same paper.
* **F2** shows the one clause the owner is being asked to *amend* is ill-typed
  as offered.
* **F1** shows the paper's central object is misnamed in a way that inflates
  what B.1/B.2/B.6 mean.

**`EARNED WITH REPAIRS` is reachable in one round.** Apply F1 (rename; restate
B.1/B.2/B.6 honestly), F2 (re-word the amendment; add the "`T(Γ_n^{rad})` is
undefined, naive evaluation gives `0`" sentence), F3 (restore both P123.038 §5
rows to `OPEN`, quote in full), F4 (delete two clauses), F5 (demote), F6
(rename `contact_∞`), F7 (`†`-monoid on `Q_{>0}`), F8 and F10 (hypothesis and
proof repairs), F9 and F12 (attribution and citations). None of these requires
new mathematics. After them, the honest label is:

```text
ROW B: CLOSED ON PAPER 43'S DECLARED CARRIER, AS A THEOREM ABOUT ROW A'S
       TRACE RESTRICTED TO THE RADIAL (MODULUS) SECTOR, MODULO THE OWNER'S
       ACCEPTANCE OF THE RE-WORDED B.4 AMENDMENT.
  B.1,B.2,B.5,B.6,B.8,B.9 PROVED (B.2/B.6 with the emptiness note);
  B.3 PROVED after the dagger extension to Q_{>0};
  B.4 REFUTED AS STATED; PROVED AS AMENDED (re-worded);
  B.7 PROVED as a test, PARTIAL as a mechanism;
  OPEN: P123.038 §5's arrow (cyclic extension to mixed correspondences,
        comparison with the analytic NUCLEAR trace); an integral carrier;
        object-level realization REFUTED for additive C-linear functors.
```

Round 2 should re-audit F1–F5 only.
