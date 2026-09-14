# R131.008 — Hostile audit of Paper 44, round 3 (§3ter, §6bis, §8bis)

Auditor: Claude (Opus 5, 1M), adversarial. Date: 2026-09-12.
Scope: every `[REBUILT, phase 131, round 3]` passage of
`04-papers/44-row-b-arithmetic-family/main.md`, checked against Paper 43
(Lemma 3.3, (8.5), (8.5∞), (8.5b), Rem. 8.6a, Thm. 8.8, Thm. 9.7(b)/9.7b,
Lemma 9.14a0, Thms. 9.14–9.14b, Thm. 14.1), P123.022 §2, P123.038 §2–§4,
P123.042 §1, P123.082, and against `R131.002/.003/.005/.006/.007`.
Method: re-derivation from the declared formulas, not re-reading of the proofs.

**Headline.** §3ter and §6bis survive a hostile re-derivation essentially
intact — they are the strongest mathematics in the paper, and they do dissolve
R1, R3, R6 and (in degree) R2. §8bis does **not**: its central claim, that the
Gram form of the Frobenius family *is* the Weil kernel, is **refuted by the
paper's own Corollary 3ter.10b**, and the one direction of the Weil interface
that is labelled `PROVED` fails with it. Reservation R5 is therefore **not**
dissolved, and the round-3 label is **not** earned.

---

## 1. Findings

### F1 `FATAL` — the Frobenius Gram form is NOT the Weil kernel (Cor. 8bis.1a, Thm. 8bis.4(i),(iii); §0; §10 verdict block)

*Location.* `main.md` Cor. 8bis.1a (8bis.3); Thm. 8bis.4(i) ("`W` the
finite-plus-archimedean kernel"); Thm. 8bis.4(iii); §0 ("computes the Gram
form — it is the Weil kernel"); §10 block line "IS the Weil kernel
W(log m − log n)".

*Error.* Take `m ≠ n` in `A` and compute the off-diagonal entry from the
paper's own theorems. `Frob_m^{sm}⋆(Frob_n^{sm})^†` is, by Thm. 3ter.7(i) and
the coset formula, a smeared `Frob_{r,F}`, `r = m/n`, `F = P(m)∪P(n)`. By the
archimedean computation of Thm. 3ter.10 — display (3ter.9), applied verbatim
with `n` replaced by `r` — its archimedean term carries the factor
`∏_{s∈S_f∖F}\mathbf 1[\,s^N \mid \text{(numerator of }r−1)\,]`, which
**vanishes for all large `N`** whenever `S_f ⊋ F`; and Cor. 3ter.10b says
exactly this in invariant form (`supp Frob_{r,F} ∩ Im j_∞ = ∅`). Hence for
large `N` the off-diagonal Gram entries are `W_{fin}(\log m − \log n)`
**with no archimedean term at all**, and for small `N` they are the
archimedean weight multiplied by an arithmetic indicator in `{0,1}` — in
neither case the Weil kernel, whose archimedean part is the density
`K(|\log m − \log n|)` for every pair. The builder's own report `R131.007` §2
("a fourth correction") states this correction; §8bis was then written as if
it did not apply.

*Consequence.* Thm. 8bis.4(iii) is **false as proved**. Its proof asserts that
`I_∂` is `−1` times the Weil functional "up to the Tate terms killed by
(8bis.8)". The discrepancy is not a Tate term: it is
`Σ_{m≠n}c_mc_n\,ω_∞(\log m−\log n)`, a full off-diagonal archimedean block that
primitivity (`Σc_nn^{±1/2}=0`) does not annihilate (take `A=\{2,3,4\}` and any
primitive `c`; the block is a nondegenerate non-multiple of the Tate rank-two
form). So Weil positivity does **not** imply `I_∂ ≤ 0` on the Frobenius class,
and the only `PROVED` half of the interface is lost. R5 stands.

*Repair.* (a) Restate Cor. 8bis.1a as: the Frobenius Gram form is the **finite
half** `W_{fin}` of the Weil kernel, plus diagonal terms; delete "it is the
Weil kernel" from §0, §8bis and §10. (b) Downgrade Thm. 8bis.4(i) accordingly
and Thm. 8bis.4(iii) from `PROVED` to `OPEN`. (c) The honest positive
statement is available and is better: by Prop. 3ter.5 and Cor. 3ter.10b the
two slices are complementary, so the **full** Weil kernel is the Gram form of
a *mixed* family (Frobenii for the finite half, `Frob_∞(t)` / radial classes
for the archimedean half — §3bis's `ω_fin ⊕ ω_∞` already has both). Build the
interface there, or state it as `OPEN`.

### F2 `MAJOR` — the diagonal of the Gram matrix is never computed (Thm. 8bis.1, Cor. 8bis.1a, Thm. 8bis.4(i))

*Location.* Thm. 8bis.1 proof, last sentence: "the unit packets vanish … as
long as `r ≠ 1`"; (8bis.3) and Def. 8bis.3 sum over all `m,n ∈ A`.

*Error.* For `m = n` the product is `Δ^{(n)}` smeared, supported **at** the
identity class: `D_A^0` fails, the `c·F(1)` term and the unit packets of (8.5)
are live, and by the mechanism of Thm. 8bis.2 the entry diverges like
`log(1/ε)`. Thm. 8bis.1 explicitly excludes `r = 1`, so the diagonal entries of
the very matrix that Thm. 8bis.4(i) calls `PROVED` are undefined in the paper.
Thm. 8bis.2 does not fill the gap: it computes the self-pairing of the
**radial** `F_ε = Γ_h`, not of a Frobenius combination.

*Repair.* Compute `T(Δ^{(n)}⋆ρ_ε⋆ρ_ε^†)` (it is `Δ^{(n)}`-averaged, so the
finite unit packets at `p|n` are genuinely present and must be evaluated, not
waved), state its `ε`-divergence, and either put the divergence into the
statement of 8bis.4(i) or restrict `I_∂` to the off-diagonal-plus-counterterm
form. Note this also means `I_∂` has no `ε→0` limit — which is consistent with
Thm. 14.1 but must be said.

### F3 `MAJOR` — missing hypothesis on `ε` in §8bis (Thm. 8bis.1, Thm. 8bis.4)

Thm. 3ter.10's conclusion needs `supp h` to contain no `q^{−m}` but `1/n`.
Thm. 8bis.1 invokes "smeared Frobenii (Def. 3ter.8)" and then "repeat the
proof of Thm. 3ter.10" for the **convolved** profile `h_m⋆h_n^†`, whose support
has width `2ε` and is centred at `1/r`; nothing in the statement forces it to
avoid the other prime powers, and the required `ε_0` depends on `A` and `S`.
This is press point 1 of `R131.007` §5 and it is not discharged.
*Repair:* add "for `ε < ε_0(A,S)`" to Thm. 8bis.1 and Def. 8bis.3, with the
one-line discreteness argument. Also: the convolution of the coset indicators
produces the constant `∏_{r}vol(1+r^NZ_r)`, silently dropped in (8bis.1);
either normalize (`\flat`) or carry it.

### F4 `MINOR` — (3ter.9) misquotes the archimedean folding of (8.5∞)

Paper 43 Rem. 8.6a folds the **sign** into `K`, so the bracket of (8.5∞) is
`b(t)+b(−t)` in the **logarithmic** variable, i.e. `F(j_∞(e^{t}))+F(j_∞(e^{−t}))`.
Paper 44 writes `b(e^{−t}) + b(−e^{−t})`, i.e. the sign-flipped argument —
which would double-count the folding. *Value unaffected here*: both the
reflected term `h(e^{t})` and the negative-argument term `h(−e^{−t})` vanish
for `h ∈ C_c^∞(R_{>0})` supported near `1/n < 1`. Still a misquotation of a
declared formula, in a display labelled `PROVED`. *Repair:* one-line fix, and
say why the second term drops.

### F5 `MINOR` — Thm. 8bis.2: the asymptotic (8bis.6) is used where it does not hold

`Ŵ_∞(0,τ) = −\log|τ|+\log2π+O(\cdot)` is an `|τ|→∞` statement (Paper 43
(9.7)/Thm. 9.7(b), line 2465 there, with `O(τ^{−2})` — Paper 44 weakens it to
`O(|τ|^{−1})`, harmless). After `σ = ετ` the region `|σ| ≲ ε` corresponds to
bounded `τ`, where (8bis.6) is false. The conclusion survives — `Ŵ_∞(0,·)` is
bounded above by `\logπ−ψ(1/4)` and continuous at `0`, so that region
contributes `ε^{−1}·O(ε) = O(1)` — but the proof as written does not say it.
This is press point 3 of `R131.007` §5. *Repair:* one sentence.
*Citation slip:* "Paper 43 Theorem 9.7b(b)" conflates Thm. 9.7(b) with the
distinct Thm. 9.7b; the formula used is Thm. 9.7(b).

### F6 `MINOR` — Thm. 3ter.14(ii): the rate `Rε·N_B`

The displayed uniform bound `\sup_B|I_A(F_{ε,N},G)−ℓ^F_n(G)| ≤ Rε·N_B+η(R)`
suppresses the symbol growth on `|τ|≤R`: with `|\hat T| ≤ A_S+B_S\log(2+|τ|)`
and `|\hat F_{ε,N}−\widehat{Frob_n}| ≤ |τ|ε`, the honest bound is
`C_Bε R^2\log R + η(R)`. The `R`-then-`ε` order still works, so the theorem
stands; the display is wrong. The exact-agreement step for the finite Fourier
factors (press point 2 of `R131.007`) **checks out**: for `κ_r` trivial on
`1+r^{N_B}Z_r` and `N ≥ N_B` the `r`-factor is `\overline{κ_r(n^{−1})}` on the
nose, and at `p ∈ P(n)` both factors are `[κ_p=1]`.

### F7 `MINOR` — "`Λ` = Haar volume of the object's own support" is normalization-relative

Cor. 3ter.11/(3ter.11) is correct *as an identity in the declared measure*:
`vol_{d^*x}(j_p(p^kZ_p^×)) = \log p` is P123.042 §1's **declared** shell
normalization, not a theorem; under the probability normalization the same
object would give contact `p^{−k/2}`. Note also the mild equivocation:
`Frob_{p^k}` is the *probability* Haar measure (total mass 1), while `Λ` is the
`d^*x`-volume of its support — two different measures on the same set. The
paper says this (Rem. 3ter.11a, "the numerical normalization is still row A's
declared one"), so this is `MINOR`: R4 is **partly** dissolved, as claimed, and
the round-2 concession correctly stands.

### F8 `MINOR` — §6bis: "functorial for the divisor arrows" is asserted, not proved

`Sh_Z` **is** a functor on the divisor poset `(N_{≥1},\mid)` — the maps
`(id, n)` compose correctly, `(id,n/m')∘(id,m'/m) = (id,n/m)` — but the paper
never checks composition; it exhibits one triangle. It is **not** a functor on
`G`, and is a **function** (not a functor) on the monoid `(N,×)`, since the
monoid has one object and `Sh_Z` is not monoidal (Thm. 6bis.3(iv)). Rem. 6bis.5
states the negative half correctly, so there is **no overclaim**; add the
one-line composition check and the words "functor on the divisor poset,
function on the monoid".

### F9 `NOTE` — §9bis does not record the fourth correction

`R131.007` §2's "fourth correction" (the blueprint's `W_∞` for the smeared
Frobenius is wrong; the Frobenius is off the archimedean slice) is a refuted
blueprint claim of the same status as W13–W15 and is recorded only inside
Cor. 3ter.10b. Given F1, it is the *most* consequential of the four. It should
be W16.

### F10 `NOTE` — ledger/lead discrepancy on B.7

`R131.005` §2 **ruled** B.7 `PROVED` (test and mechanism). Paper 44's §10 table
still reads "`PROVED` (the test); `PARTIAL` (the mechanism)". Round 3 changed
neither; the paper is the more conservative of the two and that is fine, but
the two documents disagree and one of them should cite the other.

---

## 2. What survives

Re-derived independently and **correct**:

* **Frob_{p^k} is well defined** as the normalized Haar measure of the coset
  `j_p(p^k)·j_p(Z_p^×)`, and by Paper 43 (9.5b) + Lemma 3.3 its support is
  exactly `j_p(p^kZ_p^×) = \{(p^{−k};u\ \text{at}\ p;p^{−k}\ \text{else})\}`.
  Lemma 3ter.3's two computations of `c_n` agree *on the nose* (I redid both:
  the `p`-coordinates are both `(n/p^{v_p(n)})^{−1}`), not merely up to a unit.
* **`Frob_m⋆Frob_n = Frob_{mn}` for all `m,n`, including non-coprime**:
  `μ_{cK}⋆μ_{c'K'} = μ_{cc'KK'}` (uniqueness of Haar on `KK'`),
  `K_{P(m)}K_{P(n)} = K_{P(mn)}` (idempotence of `Z_p^×`-Haar is exactly the
  case `p|(m,n)`), `c_mc_n = c_{mn}`. **`Frob_1 = δ_1 = Δ`** literally, the
  empty product: a point mass, a true unit. R3's "the unit is a projector"
  is dissolved.
* **Thm. 3ter.6**: `ι(n)ι(n)^{−1}(uv^{−1})` computes to `μ_{K_{P(n)}}`
  correctly; idempotence, `Δ^{(n)}≠Δ` (no atoms in Haar of an infinite compact
  group), bidegree `(n^{1/2},n^{−1/2})` from `λ_∓=∫|x|^{∓1/2}` with `|x|≡1/n`.
  Rem. 3ter.6a is honest: the analogy with `Γ_FΓ_F^t=qΔ` is flagged as an
  analogy, the discrepancy is recorded, and it is used nowhere. Confirmed.
* **Thm. 3ter.7 and the builder's refutation of the `Q_{>0}^×` indexing**:
  verified. `Frob_2⋆Frob_1^† = μ_{j_2(2)K_{\{2\}}}` and
  `Frob_6⋆Frob_3^† = μ_{j_2(2)K_{\{2,3\}}}` have supports of different
  dimension; measures determine supports; the blueprint's assignment is not
  well defined. The idempotent law (`Frob_{r,F}` idempotent iff `r=1`) and the
  semilattice `(𝒫_{fin}(S_f),∪)` check out. The blueprint is **refuted** and
  the corrected statement is stronger.
* **Thm. 3ter.10** re-derived from (8.5): at `q∈S_f`, `m≠0`, `a_q(q^mw) =
  h(q^{−m})·(\text{indicators})`; the support hypothesis kills all but
  `n=q^m`; on the surviving shell the `r`-coordinates (`r≠p`) are `p^{−k}=1/n`,
  the **centre** of `n^{−1}(1+r^NZ_r)`, so every indicator is `1` **for every
  `N`** — this is the real reason the identity is exact at every level, and it
  is correct. `a_p` is constant `= h(1/n)` on the shell, hence the **point
  evaluation** rather than `∫h`: the builder's refutation B2 of the blueprint
  is right and the corrected statement is stronger. `τ_p ≡ p^{−k/2}`
  (Lemma 8.2(i)) and `vol = \log p` give `Λ(n)n^{−1/2}h(1/n)`.
  **Unit packets vanish at every `q`, including `q|n`**: `j_q(Z_q^×)` has
  archimedean coordinate `1`, and `1 ∉ supp h` (the hypothesis "no `q^{−m}`
  other than `1/n`" includes `q^0=1`, so the statement is self-consistent —
  checked). Confirmed, subject to F4.
* **Cor. 3ter.10b** is right, **and its hypothesis `S_f ⊋ P(n)` is necessary**
  and correctly stated: if `S_f = P(n)` the support contains `j_∞(1/n)` and
  (3ter.9)'s empty product is `1`. Consistency with Thm. 3bis.7 (the norm class
  *does* have an archimedean term) is **exact, not a tension**: by
  Prop. 3ter.5 `Γ_n^{rad} = Frob_n⋆Δ^{rad}`, and convolving with the
  unit-averaging projector spreads the support onto the whole modulus level
  set, which meets `Im j_∞`. Answer to attack (8): **coherent**, and the
  complementary-slice statement (Rem. 3ter.13a) is the cleanest thing in §3ter.
* **Thm. 3ter.12** (support-level characterization of prime powers) and
  **Rem. 3ter.12a**: correct; R6 is genuinely dissolved — `Frob_4` and `Frob_6`
  differ as objects.
* **Thm. 3ter.14**: membership in `N_A^{dist}` survives (F6 is a display
  error, not a gap); the exact-agreement step checks out.
* **§6bis in full**, modulo F8. Lemma 6bis.2 is right and is better than
  stated: `b_S` is well defined *pointwise on the support* — at `r∤n`,
  `x_f/x_∞ = (1/n)/(1/n) = 1`; at `p|n`, `u_p/(1/n) = nu_p`, valuation
  `v_p(n)` — so `b_S(x)L_S = nL_S` for **every** `x ∈ supp Frob_n`, no lift
  chosen. Thm. 6bis.3: cohomology, the injective chain map `(id,n)` with
  cokernel `(L_S/nL_S)[0] ≃ Sh_Z(Frob_n)` and the resulting exact triangle,
  degree additivity, the `Tor_1(Z/2,Z/2)=Z/2` non-monoidality counterexample,
  and the Möbius cofiber `[Z→Φ_n(1)→Z]` — all verified.
  **Thm. 6bis.4** is a correct identity of degrees on objects; `n` composite
  gives `0 = Λ(n) = \log|Φ_n(1)|` consistently. The P123.022 §2 *Scope*
  paragraph is quoted **verbatim and correctly** (I diffed it), and
  Rem. 6bis.5 concedes exactly the right three things (not a functor on `G`;
  complex realization acyclic; degrees only; P123.038 §5 still `OPEN`).
  **No overclaim in §6bis.**
* **Thm. 8bis.2**: the rate is right. `σ=ετ`, `−\log|τ| = −\log|σ|+\logε`,
  Plancherel, and the **uniform** finite bound `|Σ\hat W_p| ≤ A_S` (correct:
  `|ζ_p/(1−ζ_p)| ≤ p^{−1/2}/(1−p^{−1/2})`, `S_f` finite) give
  `−ε^{−1}\|φ\|_2^2(\log(1/ε)+O(1))`, and the `L^2`-normalized form
  `−\log(1/ε)+O(1)`. The builder's refutation B3 of the blueprint's `−2\log(1/ε)`
  is **correct**; the blueprint's coefficient and its `ε`-power are both wrong.
  `Δ·Δ = −∞` is `PROVED`, the divergence is entirely archimedean, and
  Cor. 8bis.2a is correctly labelled an interpretation and used nowhere.
* **The converse density argument**: the builder's claim that the naive
  argument fails is **verified**. `\log(n+1)−\log n → 0` only at `+∞`; in a
  fixed window `[a,b]` the gaps are `≥ \log(1+e^{−b}) > 0`, so bumps of width
  `ε ≪ e^{−b}` at `\{\log n\}∩[a,b]` span nothing dense in `C_c^∞((a,b))`.
  The blueprint's stated route to the equivalence is therefore broken, and
  Thm. 8bis.4(iv)'s `OPEN` is honest. (The paper does **not** get credit for
  8bis.4(iii) in exchange — see F1.)

**Attack (9), independence.** Re-checked by grep and by reading: the only
mention of zeros or of RH in Paper 44 is Thm. 8bis.4(ii), labelled `CLASSICAL`,
cited and not proved. No positivity, no sign, no `𝓝_∞=0`, no von Mangoldt
input (`Λ` is derived as a shell volume). **Independence holds** — with the
caveat that 8bis.4(iii), the one place the `CLASSICAL` input is *used*, is the
clause F1 refutes; deleting it makes the independence cleaner, not worse.

**Attack (8), consistency of the apparatus.** §0, the banner, §2 contract
table (B.1–B.4, B.6), §9bis W11–W15, §10 block and ledger are mutually
consistent and consistent with §3ter/§6bis. **No leftover "ideal class"
wording**: every occurrence is inside an explicitly historical passage
(banner round-2 note, §3bis.2's own retraction, §9bis W5) — correct.
The **one** inconsistency is F1's: §0, §8bis and the §10 block all repeat
"it is the Weil kernel", which the paper's own Cor. 3ter.10b contradicts.

---

## 3. Renaming test on the round-3 material

* **§3ter**: `PASS`. The content — Haar measures of fixed-point strata, a
  strict monoid with a true unit, an inverse semigroup graded by finite prime
  sets, supports that determine `(n,P(n))`, exactness of the finite contact at
  every level `N` — is not stated, implied or suggested by the explicit
  formula. The *number* `Λ(n)n^{−1/2}` is row A's declared local term and is
  inherited, exactly as round 2 conceded; but the objects are new.
* **§6bis**: `PASS`. `Sh_Z`, the transitivity triangle and the Möbius cofiber
  are lattice statements with no analytic input; `\log n = Σ_{d|n}Λ(d)` is
  labelled `CLASSICAL` where used.
* **§8bis**: `FAIL IN PART`. Cor. 8bis.1a's "this is the geometric side of the
  explicit formula" is, in the only sense in which it would be true, a
  restatement of row A's trace — and in the sense claimed it is false (F1).
  Thm. 8bis.2 passes (it is a statement about `\hat T`'s growth, not about
  zeros). Thm. 8bis.4(ii)+(iii) is the single place where an external
  arithmetic input does work; with (iii) refuted, nothing is left that could
  be a renaming.

---

## 4. Verdict per clause

| clause | round-3 verdict of this audit |
|---|---|
| **B.1** | `PROVED`. The inverse-semigroup completion `𝔉_S` (Thm. 3ter.7) is real and correctly indexed by `(r,F)`; R3's "no dagger in the source" is answered, not relabelled. |
| **B.2** | `PROVED` and, since round 3, **non-vacuous**: the realization is strict, injective, has a true unit, and does not factor through the modulus (Rem. 3ter.4a is a correct obstruction argument). R1 dissolved. |
| **B.3** | `PROVED`, with a true unit. Thm. 3ter.6 verified; the analogy with `Γ_FΓ_F^t=qΔ` is honestly quarantined. |
| **B.4** | `REFUTED AS STATED`; `PROVED AS AMENDED` (owner-accepted), **and now proved on objects in degree** (Thm. 6bis.4). Verified. The Scope quotation is faithful. R2 dissolved *as far as a `C`-linear carrier permits*; `Sh_Z` is a functor on the divisor poset and a function on the monoid (F8). |
| **B.5** | `PROVED` (unchanged, re-checked through (6bis.4)). |
| **B.6** | `PROVED`, both halves non-vacuous (Thm. 3ter.12; Thm. 3ter.14 modulo F6). R6 dissolved. |
| **B.7** | `PROVED` as a test; `PARTIAL` as a mechanism, as the paper says. I do **not** endorse `R131.005`'s upgrade to `PROVED`: Rem. 6.5a′ is still the truth (F10). |
| **B.8** | `PROVED` (unchanged; numerics not re-run by me, and they do not bear on F1–F3). |
| **B.9** | `PROVED`, independence intact (see attack (9)), with `Λ`-as-volume still **inherited in normalization** (F7). |

**New**: §8bis is not a clause of the contract, which is why F1 does not flip a
clause verdict. It is, however, the entirety of round 3's answer to R5.

---

## 5. Does row B now earn `WEIL-STRENGTH-COMPLETE` without R1–R6?

**No.**

* **R1 `DISSOLVED`** (Thm. 3ter.4(iv), Rem. 3ter.4a) — genuinely, with a
  proof that no continuous real-label family interpolates.
* **R3 `DISSOLVED`** (true unit, dagger, inverse semigroup).
* **R6 `DISSOLVED`** (Thm. 3ter.12: a statement about the support).
* **R2 `DISSOLVED IN DEGREE, ON THE MONOID`** — which is the most that
  P123.022 §2 permits, and the paper says so. An auditor who read R2 as asking
  for an object-level identification in `G` should note that this is
  **refuted**, not open, and stop asking.
* **R4 `PARTLY DISSOLVED`** (F7), exactly as the builder claims. The
  attribution moved from a symbol to an object; the normalization did not move.
* **R5 `NOT DISSOLVED`** — F1. The interface delivers the **finite half** of
  the Weil kernel, an uncomputed divergent diagonal (F2), a missing hypothesis
  (F3), and one direction whose proof is invalid. What §8bis *does* establish,
  and it is worth keeping, is Thm. 8bis.2 (`Δ·Δ = −∞` with its rate, correct)
  and Thm. 8bis.4(iv)'s refutation of the naive density argument.

**Grade: the label is NOT EARNED in round 3 beyond the round-2 position.**
Round 3's mathematics is a real advance — §3ter and §6bis are correct and they
retire three of the six reservations outright and a fourth as far as the
declared carrier allows — but §8bis overstates its result in the one place the
lead asked for honesty, and does so against a theorem the same paper proves
three sections earlier. Repair F1–F3 (the repairs are available and make the
paper *more* interesting: the complementary-slice dichotomy is the right
statement, and it says the Weil kernel needs a **mixed** family), record the
fourth blueprint refutation as W16, and row B stands with R1, R2, R3, R6
dissolved, R4 partial, R5 `OPEN` with an exact statement. That is a defensible
`WEIL-STRENGTH-COMPLETE on the declared carrier, with R4 and R5 recorded` —
but not before F1 is fixed, because as written §0, §8bis and §10 assert
something false.
