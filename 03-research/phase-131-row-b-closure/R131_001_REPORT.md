# R131.001 — Report: closing row B (Paper 44), phase 131

Inputs: `R131_000_BLUEPRINT.md`; Paper 44 as corrected in phase 128;
Paper 43 after phase 130 (`WEIL-STRENGTH-COMPLETE` on its declared carrier);
D128.002, D128.004; P123.018/022/037/038/039/042/060/082; PLAN §6.
Deliverables produced: Paper 44 `main.md` (new §3bis, new §9, new §9bis,
amended §2/§6/§7/§8/§10, banner and §0), Paper 44 `README.md`, PLAN §6 note,
`scripts/verify_131_contacts.py` (all checks pass).

---

## 1. The mathematics, in one page

The class of the idele `a_S(n) = (1;n,…,n)` in the carrier is, by Paper 43
Lemma 3.3, `δ_S(1/n) = (1/n at ∞; 1 at every finite place)` — unit coordinate
`1`, not `n` (Lemma 3bis.1). The arithmetic object is therefore not the
element but the **ideal class**

    Γ_n^rad := ∫_{K^♮} δ_S(1/n)·u du,   K^♮ = {±1} × ∏_{p∈S_f} Z_p^×,

the normalized Haar measure of the level set `{|x|_S = 1/n}` = the unit
average of the classes of **all** generators of `(n)` (Def. 3bis.4).

Proved about it, in Paper 43's declared category: monoidality
(`Γ_m^rad ⋆ Γ_n^rad = Γ_{mn}^rad`, `Γ_1^rad = Δ^rad` the unit-averaging
projector), dagger (`(Γ_n^rad)^† = Γ_{1/n}^rad`), bidegree
`M = (n^{1/2}, n^{−1/2})`, and independence of lift, gauge, uniformizers and
chart (Thm. 3bis.5). Its **finite contact** in row A's own trace is
`Λ(n)n^{−1/2}` with `Λ(p^k) = log p = vol_{d^*x}(p^kZ_p^×)`, the Haar volume
of the valuation shell, and `0` at composite `n` (Thms. 3bis.7, 3bis.8). Its
**archimedean contact** is the density `K(log n) = n^{3/2}/(n²−1)`. The
degrees match: `log[L_S:nL_S] = log n = Σ_{d|n}Λ(d)` and
`deg_det Prim_n = log|Φ_n(1)| = log|det(1−T|V_n)| = Λ(n) = n^{1/2}·contact_fin`
(Thm. 3bis.10). And `Γ_n^rad ∈ N_A^dist`, with canonical primitive component
`(I_A(Γ_n^rad,·),0)` and ruling component `σ(n^{1/2},n^{−1/2})` (Thm. 8.3).

The `n−1` is gone as a contact: `δ_S(1/n)` is in the image of **no** finite
slice map `j_q` (Prop. 3bis.2), so a test concentrated at the class meets no
finite shell and no finite unit packet (Cor. 3bis.3), and for a **radial**
section the unit packet vanishes identically (proof of Thm. 3bis.7).

---

## 2. Clause by clause: proved / corrected / open

**B.1 (source category).** `PROVED`, upgraded from `PARTIAL`.
*Proved:* `W = (N_{≥1},×)` with the divisor poset, objects and morphisms
stated (Def. 4.1); the **symmetry is realized** — `C_S` is abelian and the
ideal classes commute (Thm. 3bis.5(i)) — which is what phase 128 had recorded
as unrealized; the divisor arrows are realized on the `Z`-linear model
`Q_{S,·}` (P123.038 §3) and on the ideal classes as divisibility of moduli.
*Honest sentence carried:* they have **no** morphisms in `G` (P123.082), and
B.1 as written does not ask for any.
*Open:* nothing for B.1. (If a future clause demands a functor `W → G`,
P123.082 refutes it; that is a statement about the source specification, not
about this paper.)

**B.2 (realization).** `PROVED on the label monoid`, now with independence
proved **by construction**: unit averaging is exactly the operation that
removes the lift ambiguity of P123.018 §2 (Thm. 3bis.5(iv)). Chart
compatibility is `(π_{TS})_*Γ_n^rad(T) = Γ_n^rad(S)`, so the family lives on
the colimit `D_A^∞`. The element realization `n ↦ Γ_n = E_{a_S(n)}` (Thm. 4.3)
is kept, with the relation `Γ_n^rad = ∫_{K^♮} E_u ⋆ Γ_n du` (3bis.4).
*Open:* nothing.

**B.3 (unit, transposition, half-densities).** `PROVED`. Thm. 4.4 for the
element classes; Thm. 3bis.5(i)–(iii) for the ideal classes, with the unit
`Δ^rad = Γ_1^rad` identified as the unit-averaging projector (the identity on
the radial sector, **not** on `D_A`).
*Open:* nothing.

**B.4 (derived contact).** `REFUTED AS STATED`; `PROVED AS AMENDED`.
*Refuted, unchanged from phase 128:* `LΔ^*Γ_n` is the fixed complex with
differential `n−1` (P123.060), not `[Z→Φ_n(1)→Z]`; and no `C`-linear additive
contact functor carries `Z/p` (P123.022). Phase 131 adds a third reason the
literal clause has no object: `Γ_n` has **no finite contact at all** (Cor.
3bis.3).
*Amended clause, stated and proved in §6.2a′ / Thm. 6.3a:* the derived contact
of `Γ_n^rad` with the diagonal — the value on it of Paper 43's declared trace,
whose integrand is place by place the Haar-regularized rank of the relative
Hochschild shadow times the half-density–Lefschetz weight (Paper 43 Thm. 7.1,
Thm. 8A.9 (8A.24)–(8A.24′)) — has finite-place degree `Λ(n)n^{−1/2}` =
`n^{−1/2}·deg_det[Z→Φ_n(1)→Z]`; the identification is of **degrees**.
*Exact missing statement, still open:* an **integral carrier** on which the
contact is an object-level derived intersection. `OPEN`; and `REFUTED` for
additive `C`-linear contact functors (P123.022).
*Decision required of the repository record:* whether to adopt the amendment, exactly as
with Paper 43's A.6. Recorded in Paper 44 §2, §10 and PLAN §6.4.

**B.5 (`deg_det = log|Φ_n(1)| = Λ(n)`).** `PROVED` twice and the two proved
equal: as a shell volume in the declared category (Thm. 3bis.7, Def–Thm
3bis.8) and on the `Z`-linear models (Thm. 5.3); equality is Thm. 3bis.10(iii).
`n = 1` is identity/excess: `Γ_1^rad = Δ^rad`, treated by the `c·F(1)` term of
Paper 43 (8.4) with `c := 0`, and `t = 0` is excluded from `ω_fin` by
construction — **not** by the degree formula.
*Open:* nothing.

**B.6 (family by structure; classes in the numerical object).** Both halves
`PROVED`, the second newly.
*First half:* Prop. 7.1, plus Thms. 3bis.5, 3bis.7, 3bis.10, all stated and
proved for all `n` with no case analysis beyond "one prime divisor or
several", itself proved.
*Second half (new, Thm. 8.3):* `𝓝 = 0` and `N_A = D_A` are now theorems of
Paper 43 (Thm. 9.8), so the phase-128 caveat is void. `Γ_h ∈ D_A^rad` for
smooth `h`; and `Γ_n^rad ∈ N_A^dist` as the limit of `J(Γ_{h_ε})`, with
convergence proved **in the strong dual** (uniform on bounded sets), by an
`R`-then-`ε` argument on the symbol using the *proof* of Paper 43 Lemma
9.14a0. Canonical primitive component `(I_A(Γ_n^rad,·),0)`; moments
`λ_± = n^{∓1/2}`.
*Recorded honestly:* the ruling component `σ(n^{1/2},n^{−1/2})` is **nonzero**,
so the arithmetic classes are **not primitive**. No positivity is claimed.
*Open:* `I_A` is not claimed to extend to `N_A^dist × N_A^dist` (Paper 43 does
not claim it either), and this paper never uses such an extension.

**B.7 (discriminating test; mechanism located).** `PROVED`, and now located
**on the carrier** (new Thm. 6.5): at `p | n` the fixed-point weight
`1/|1−x|_p` is identically `1` on the shell `p^kZ_p^×` (so the linear-dilation
contact contributes nothing), and the cyclotomic `log p` is
`vol_{d^*x}(p^kZ_p^×)` = the Haar volume of the **unit orbit of the ideal**,
independent of `k` — the carrier-side reason `Φ_p(1) = Φ_{p²}(1) = p`.
Explicitly `contact_fin(Γ_p^rad) = (log p)p^{−1/2}`,
`contact_fin(Γ_{p²}^rad) = (log p)p^{−1}`, while the fixed data
`|1−p|_q^{−1}`, `|1−p²|_q^{−1}` belong to the lift and the class does not see
them. Thm. 6.4 (on `G_m/Z`) is kept unchanged.
*Flagged, not proved:* "`log p` is the deck group `μ_n` in measure form" is a
**dictionary entry**, labelled as such in Rem. 6.5a and used nowhere.

**B.8 (adversarial verification).** `PROVED`. §7's nine rows
(`2,4,8,6,12,30,9,10,16`) kept; the `w_ram`/`w_unit` columns relabelled "of
the lift"; a continuation table added with finite contact, archimedean
contact, bidegree and `Σ_{d|n}Λ(d) = log n`, with exact and numerical values.
Numerics in `scripts/verify_131_contacts.py`: all checks pass (shell sum =
`Λ(n)n^{−1/2}`; `K(log n) = n^{3/2}/(n²−1) = ½[τ_∞(1/n)+τ_∞(−1/n)] =
n^{−1/2}Σ_j n^{−2j}`; `Σ_{d|n}Λ(d) = log n`; `log Φ_n(1) = Λ(n)`;
`∏_{d|n}d^{μ(n/d)} = Φ_n(1)`). Numerics verify; they prove nothing.

**B.9 (compatibility with A; independence).** `PROVED`. Compatibility rests on
Paper 43 (8.5), (8.5a), (8.5b), (8.5∞), Lemma 8.2, Thm. 8.8, Def. 8A.7d,
Thm. 8A.7c, Thm. 8A.9, Thm. 7.1(c), Thm. 9.1, (9.5b), (9.13), (9.14),
Thm. 9.7, Thm. 9.8, Thm. 9.14, Lemma 9.14a0, Thms. 9.14a–b — all cited
exactly (Thm. 8.2, phase-131 block). Independence: no zero, no RH, no sign, no
positivity, and `Λ` **derived** as the shell volume under Paper 43
Rem. 9.7a's rule (Rem. 3bis.8b). Paper 43 is cited in its post-phase-130 form
with its qualifications (A.6 amended, A.8 with target `Pic_b(B_T)`, no sign,
`𝓝_∞^W = 0` not claimed).

---

## 3. Blueprint claims I rejected or corrected

1. **"`Γ_n^rad` lies in the Fell completion of `G`; a continuous compactly
   supported section" (blueprint (b)). FALSE as stated.** `Γ_n^rad` is a point
   mass in the archimedean coordinate; `D_A = C_c^∞(C_S)` requires smoothness
   in the `R^×` coordinate (Paper 43 Def. 8.5), and a compactly supported
   *continuous section* is not a measure. *Counterexample in the strict sense:*
   `Γ_1^rad` is the Haar measure of `K^♮`, and if it were an element of `D_A`
   it would be an identity for `D_A` (it is idempotent and acts as the identity
   on radial elements), but `D_A` is a non-unital convolution algebra on the
   non-compact group `C_S`. *Correct statement written instead
   (Rem. 3bis.4b):* `Γ_n^rad ∉ D_A`; it is a **multiplier** of `D_A`, mapping
   `D_A → D_A^rad` continuously, and it is an **element of `N_A^dist`**
   (Thm. 8.3) — the exact analogue of Paper 43 Rem. 8.11 for the diagonal.
   Nothing downstream breaks; the smeared family `Γ_h` carries all the analytic
   work, as the blueprint's own item (e) anticipated.

2. **The averaging group is `K = ∏_{p∈S_f}Z_p^×` (blueprint (b)). TOO SMALL.**
   It must be `K^♮ = {±1} × ∏_{p∈S_f}Z_p^×`, the maximal compact subgroup of
   `C_S`. With `K` only, the support of `Γ_n^rad` is half the level set
   `{|x|_S = 1/n}`, the Haar-coset computation of monoidality
   (Thm. 3bis.5(i)) is unavailable, and — decisively — the archimedean value
   is `τ_∞(1/n) = n^{1/2}/(n−1)`, **not** the half-sum
   `½[τ_∞(1/n)+τ_∞(−1/n)] = n^{3/2}/(n²−1) = K(log n)` that the blueprint's own
   item (d) asserts. With `K^♮` and the declared measure `d^*x_∞ = dx/(2|x|)`
   (Paper 43 (8.5b)), (d) is exactly right. Corrected in Def. 3bis.4 and §9bis.

3. **"`δ_S(1/n)` is not in the image of `j_q` for `q ∤ n`" (blueprint (a)).
   TRUE BUT WEAKER THAN THE TRUTH.** For `|S_f| ≥ 2` and `n ≥ 2` the class is
   in the image of **no** `j_q`, `q ∈ S_f` — including `q | n` — because
   `j_q(q^kw)` has coordinate `q^{−k} ≠ 1` at every other finite place of `S`
   (Paper 43 (9.5b)). It **is** in the image of `j_∞`, namely `j_∞(1/n)`.
   Proved as Prop. 3bis.2, which is what Cor. 3bis.3 actually needs (it needs
   *all* finite terms to vanish, not only the `q ∤ n` ones).

4. **"the contact of the ideal class is `Λ(n)n^{−1/2}`" stated as a value of
   `W_p` at a point mass (blueprint (c)). ILL-TYPED AS STATED.** `W_p` is
   defined on `D_A` and `Γ_n^rad ∉ D_A`, so `W_p(Γ_n^rad)` has no meaning as
   written. *Correct statement written instead (Def–Thm 3bis.8):* the
   finite-place part of `T` on the radial sector is a unique Radon measure
   `ω_fin = Σ_{n=p^k} Λ(n)n^{−1/2}(δ_{log n} + δ_{−log n})`, and the finite
   contact of `Γ_n^rad` is **the mass of its atom at `t = log n`**. This is
   rigorous, is what the blueprint meant, and has a consequence the blueprint
   did not state: the archimedean contact is a **density**, not an atom, so the
   two contacts are objects of different type and are **not added**
   (Rem. 3bis.8a). This is also why `contact_∞` is not part of `Λ`, which the
   blueprint asserted without a reason.

5. **"the unit packet vanishes because `F` is constant on units (`c(1)=0`,
   Paper 43 (9.14))" (blueprint (c)). CORRECT, BUT (9.14) IS NOT THE REASON.**
   (9.14) is about the Fourier coefficient of a *character* `κ_p`. The direct
   reason, proved in Thm. 3bis.7, is that `a = Γ_h∘j_p` is constant on `Z_p^×`
   because `|j_p(w)|_S = 1` there, so `a(u) − a(1) ≡ 0` pointwise. The
   character statement is the same fact in Fourier form and is cited as such.

6. **"On the colimit `T_∞` the chart condition `p ∈ S` disappears"
   (blueprint (c)). TRUE, with a proof the blueprint did not give.** It is
   Paper 43 Thm. 8A.7c(a)–(c) applied to `Γ_h`, using
   `Γ_h(δ_S(ℓ^{−k})) = h(k log ℓ)`; the added terms are exactly the missing
   primes with `log ℓ ≤ R(Γ_h)`, and the sum is finite. Written into
   Thm. 3bis.7's last paragraph.

7. **Blueprint B.1 "Close B.1 `PROVED`" — accepted, but the reason given was
   incomplete.** The blueprint says "the symmetry **is** realized (`G` is
   commutative on the radial sector; `C_S` abelian)". That is right and is the
   ground for the upgrade, but phase 128 had downgraded B.1 for **two**
   reasons, the second being that the divisor morphisms have no image in `G`.
   The upgrade is therefore conditional on reading B.1 as written ("a source
   category … stated with objects and morphisms"), which does not demand a
   functor into `G`. The ledger says so explicitly rather than silently.

8. **Blueprint item (e) "`T(Γ_h) = … = χ_A`".** The equality with row C's
   `χ_A` is *not* asserted in Paper 44; Paper 45 §12 defines `χ_A` and the
   comparison belongs to row C. Paper 44 proves only the identity (9.1) and
   hands it over. This is a deliberate narrowing, not a rejection.

No blueprint claim was found to be irreparably false; items 1, 2 and 4 are
type errors with correct repairs, item 3 is a strengthening, and the rest are
missing proofs now supplied.

---

## 4. Theorem numbers added, and passages changed

New (all marked `[REBUILT, phase 131]`):

| number | statement |
|---|---|
| Lemma 3bis.1 | the class of `a_S(n)` is `δ_S(1/n)`, unit coordinate `1` |
| Prop. 3bis.2 | the class is on `Im j_∞` and on no `Im j_q` |
| Cor. 3bis.3 | `W_q ≡ 0` on tests at the class; `w_unit` is of the lift |
| Rem. 3bis.3a | why this dissolves the former §9.2 |
| Def. 3bis.4 (+ Rem. 3bis.4a, 3bis.4b) | the ideal class; why it is "the ideal"; its type (multiplier, not element) |
| Thm. 3bis.5 (+ Rem. 3bis.5a) | monoidality, dagger, bidegree, independence of all choices |
| Def. 3bis.6, Lemma 3bis.6a | the smeared ideal classes and their algebra |
| Thm. 3bis.7 | the trace on the radial sector; `Λ(p^k)= log p =` shell volume |
| Def–Thm 3bis.8 (+ Rem. 3bis.8a, 3bis.8b) | the two contacts; type distinction; `Λ` derived |
| Thm. 3bis.9 | the smeared form = row C's geometric side |
| Thm. 3bis.10 (+ Rem. 3bis.10a, 3bis.10b) | degree matching; what it does not say; the P123.038 §5 arrow |
| §6.2a′, Thm. 6.3a, Rem. 6.3b | the amended clause B.4, stated and proved |
| Thm. 6.5, Rem. 6.5a | the B.7 mechanism located on the carrier |
| Thm. 8.3, Rem. 8.3a | `Γ_n^rad ∈ N_A^dist`; strong-dual convergence; components |
| §9.1–§9.4 | the rewritten hand-off to row C, incl. the Paper 45 §11 correction |
| §9bis W1–W4 | the phase-131 withdrawals |

Changed in place (existing numbers kept stable): the status banner; §0
(phase-131 block); §2 table row B.4; Thm. 3.3 (a `[REBUILT, phase 131]` block
re-reading (iv)–(v) as statements about the lift; (i)–(iii) untouched);
Rem. 3.7 (addition); §6.1 (the arrow, now Thm. 3bis.10(ii)); §7 (column
relabel + continuation table); §8 (`𝓝 = 0`, `N_A = D_A` preamble; Thm. 8.1(iv)
restated; Thm. 8.2 independence block); §10 (verdict, ledger, open-item table,
audit paragraph — the phase-128 audit paragraph kept verbatim below the new
one); §11 (dependencies).

---

## 5. The label the mathematics earns, in the construction's judgement

I do **not** grant `WEIL-STRENGTH-COMPLETE`; the closure rule reserves it to an
adversarial audit, and that is the review's call. What I believe the mathematics
earns, stated so it can be argued with:

```text
ROW B: CLOSED ON PAPER 43'S DECLARED CARRIER, MODULO THE
       ACCEPTANCE OF THE B.4 AMENDMENT.

  B.1, B.2, B.3, B.5, B.6, B.7, B.8, B.9 .... PROVED, in the exact forms
       of the ledger (B.2 on the label monoid; B.1 with the honest
       sentence about divisor arrows; B.7 with the dictionary flagged).
  B.4 ...................................... REFUTED AS STATED;
       PROVED AS AMENDED (Thm 6.3a).  The amendment is a PROPOSAL.
  Object-level realization of the integral contact ... OPEN (integral
       carrier) and REFUTED for additive C-linear contact functors.
  Not claimed: zeros, sign, positivity, primitivity of the classes,
       Z/Phi_n(1) as an object of G, N_infty = 0.
```

Two honest caveats an auditor should weigh before upgrading further.

1. **Row B inherits row A's carrier and its qualifications.** Everything in
   §3bis is proved at a fixed finite chart `S` (with the colimit statement
   where available). Paper 43's own label is qualified (A.6 amended, A.8 with
   target `Pic_b(B_T)`, auditor's dissent recorded); row B cannot be less
   qualified than the carrier it sits on.
2. **The renaming test is where B is most exposed.** `T(Γ_h)` of (9.1) *is*
   the prime-power-plus-Gamma side of the explicit formula. My defence is
   Paper 43 Rem. 9.7a's, applied verbatim: `Λ` is **derived** as the Haar
   volume of a valuation shell, no zero and no explicit-formula identity is
   used, and the family is selected by the monoid `(N_{≥1},×)` and realized by
   an averaging construction, not chosen. An auditor who rejects that defence
   rejects row A with it; but it is the right place to press.

The three places I would press hardest are listed in Paper 44 §10's new audit
paragraph: Lemma 3bis.1 (is the canonical representative right?), the
identical vanishing of the unit packet on radial sections, and the strong-dual
convergence of Thm. 8.3(ii).
