# R135.002 — Audit of round 1 (phase 135), Paper 47 Part II §§11–16

Object audited: `04-papers/47-intersection-frame-defect/archive/main.md`, lines 1856–3038 (Part II),
against Part I §§1–10, the blueprint `R135_000`, Paper 45 (Thm 9.4 / Cor 9.4a,
Thm 10.4, Thm 12.2 / Rem 12.4), Paper 43 (Thm 9.14c, 14.1), Paper 44
(Thm 3ter.6, 3ter.10, 8bis.2, 8bis.8, §6bis), and the `[phase 135]` insertions
in Papers 43 and 45.

All quotations are verbatim from the file at the line numbers given. No paper
was edited. Independent numerics run by the auditor (mpmath, 40 dps) are noted
where they bear on a finding.

---

## (A) Findings

### M1 — `FATAL` — Corollary 12.4a is a non-sequitur as stated, and read literally it makes Theorem 12.3 vacuous

Line 2564–2572:

> **Corollary 12.4a (the Euler-product locus, `PROVED`).**  Let `h⁰` be any
> candidate whose **definition** is a function of the data
> `(a completed function Z with Z(s)=Z(1−s) of order 1, its polar set, D^W, ⋆,
> {}^∨, τ_•, {· ≥ 0}, K_Z, 𝓝_∞^{(Z)})`, uniformly in `Z`.  Then `h⁰` does
> **not** satisfy (a)+(b′)+(c) for `ζ`.
>
> *Proof.*  If it did, the same definition applied to `Z = Ξ_a` — which is such a
> `Z`, and for which every listed datum exists by §12.5 — would satisfy them for
> `Ξ_a`, contradicting Theorem 12.4.

**Two independent defects.**

1. *The inference is invalid.* Let `Z ↦ h⁰_Z` be a uniform rule. Theorem 12.4
   says: no functional satisfies (a)+(b′)+(c) for `Ξ_a`. Suppose `h⁰_ξ` satisfies
   them for `ξ`. Nothing whatever forces `h⁰_{Ξ_a}` to satisfy them for `Ξ_a` —
   a uniformly *defined* functional may have a property for one `Z` and lack it
   for another. (Trivial model: `h⁰_Z(E) := 0` for all `E` unless a certain
   `Z`-dependent test succeeds.) What transfers under uniformity of definition is
   a **proof** that uses only the listed data, not the **truth** of the
   conclusion. So the corollary is a statement about admissible *proof schemas*,
   not a theorem about functions, and its stated proof is a non-sequitur.
2. *Read literally the hypothesis class is everything, and the corollary
   contradicts the paper's own deliverable.* `Z` itself is listed among the data.
   Therefore **every** function `h⁰ : D^W → R_{≥0}` is "a function of the data,
   uniformly in `Z`" (take the rule that reads `Z` and branches). Under that
   reading Corollary 12.4a asserts: no `h⁰` at all satisfies (a)+(b′)+(c) for
   `ζ`. That contradicts the announced deliverable at line 2946 and §14.5
   ("row D's target follows from the existence of one function `h⁰` …",
   "`OPEN`"): the reduction would be **empty**, since its hypothesis would have
   just been proved unsatisfiable. Part II cannot simultaneously claim
   Theorem 12.3 as a live reduction and Corollary 12.4a as a theorem.

**Downstream.** Remark 12.4b (line 2575 ff.) calls this "the main structural
output of Part II"; Theorem 13.3 (line 2688 ff.) and Theorem 13.7 (line 2965 ff.)
are proved *by* Corollary 12.4a and inherit the defect verbatim; §14.5's
"Replaced" item and new open item (18) rest on it.

**Minimal repair.** Demote to a `SCHEMA` / `METATHEOREM` and state it about
proofs, e.g.: *"If (a)+(b′)+(c) for `ζ` is derivable from a definition of `h⁰`
together with only the listed data and properties of them that hold for every
admissible `Z`, then the same derivation yields (a)+(b′)+(c) for `Ξ_a`,
contradicting Theorem 12.4."* Relabel `PROVED` → `RESTATEMENT`/`SCHEMA`, remove
"Then `h⁰` does not satisfy …" as a quantified assertion, and correspondingly
weaken Theorems 13.3 and 13.7 (whose current statements — "Let `Φ` be **any**
rule assigning to a convex subset of `D^W` a number …  Then `h⁰` does not
satisfy (a)+(b′)+(c)" — carry the same invalid quantifier).

---

### M2 — `MAJOR` — `F ⋆ G^∨` is **not** even for `F ≠ G`; Definition 11.4 is undefined and Theorem 11.5, Theorem 11.8, Theorem 11.14(i) rest on it

Line 1988–1993:

> **Definition 11.4 (the extended form).**  For `F, G ∈ D^W` put
> `I_∞(F,G) := ⟨F ⋆ G^∨, W_{fin} + ω_∞⟩`,
> the left-hand side of (11.4) with `h = F⋆G^∨` (**real and even when `F,G` are
> real, by `h^∨ = h`**).

False. `(F⋆G^∨)^∨ = F^∨⋆G ≠ F⋆G^∨` in general. Explicitly, with `F` even and
`G := τ_1 F`, `F⋆G^∨ = τ_{−1}(F⋆F)`, which is centred at `−1` and is not even.
Theorem 11.3 (line ~1930), the *only* statement that gives meaning to
`⟨h, W_{fin}+ω_∞⟩` and to (11.4), is stated for `h ∈ D^W` **"real and even"**,
and its proof uses evenness twice (`Φ_h(1−s) = Φ_h(s)` in the Lemma 9.1
replacement, and the doubling of the prime sum in step (c)). Hence `I_∞(F,G)` is
literally undefined for `F ≠ G`, and (11.6) is not proved for `F ≠ G`. Every
cross pairing used afterwards — `I_∞(F,K)` (11.10), `I_∞(K,K)` via `K⋆K` (that
one is fine), `I_∞(F,τ_aK)`, `I_∞(N,G)` in Theorem 11.11, `I_∞(E,F)` in
Theorem 11.14(i) and the whole of Theorem 12.3 — is affected.

**Minimal repair** (cheap, and it costs no theorem): define `I_∞` by
**polarization** from the diagonal, `I_∞(F,G) := ¼[Q(F+G) − Q(F−G)]` with
`Q(X) := ⟨X⋆X^∨, W_{fin}+ω_∞⟩` (`X⋆X^∨` *is* even, by commutativity), note that
(11.6) for `F = G` plus bilinearity of the right-hand side gives (11.6) in
general, and delete the false parenthetical. Alternatively state and prove
Theorem 11.3 for non-even `h` (the classical Weil formula does hold there, but
the "verbatim extension of Cor 9.4a" claim then fails, since Cor 9.4a is stated
for real **even** tests — Paper 45 line 1089 ff.).

---

### M3 — `MAJOR` — Theorem 11.12's zero count compares multiplicity-counted `ξ`-zeros with order-one vanishing of `Φ_N`

Lines 2286–2295:

> Let `n_N(r)` count its zeros in `|s−½| ≤ r`. … `n_N(r) = O(r)` …
> On the other hand the zeros of `ξ` inside `|s−½| ≤ r` number
> `2N(r) + O(1) = (r/π)\log r (1+o(1))` by Riemann–von Mangoldt …,
> **and all of them are zeros of `Φ_N`**.

`N(T)` counts zeros **with multiplicity** (import (X14)/(E3d)). Theorem 11.10(c),
which is the hypothesis in force, gives only `Φ_N(ρ) = 0`, i.e. vanishing **to
order one** at each *distinct* zero — the paper itself insists on exactly this
distinction eleven lines earlier, at (11.13) and the surrounding `REFUTED` note
("Theorem 11.10 gives vanishing of `Φ_G` at each zero **to order one**, whatever
the multiplicity"). The lower bound therefore requires the count of **distinct**
zeros of `ξ` with `|γ| ≤ r` to exceed `Cr` for every `C`, which does **not**
follow from `N(T) ~ (T/2π)\log T`. The classical multiplicity bound
`m_ρ = O(\log γ)` only yields `≫ r` distinct zeros — the same order as the
Jensen bound `O(r)`, so it does not close the gap.

**Minimal repair.** Add an import: the number of *simple* (hence distinct) zeros
with `0 < γ ≤ T` is `≫ T\log T` (Levinson 1974 + Heath-Brown / Selberg; or
Conrey's proportion), which restores the contradiction. Until then
Theorem 11.12, Remark 11.12a, Paper 45 Remark 12.4a and Paper 43 Remark 14.1a
(all of which reproduce this argument verbatim) are `OPEN`, not `PROVED`.
*Mitigating:* nothing in §12 uses Theorem 11.12, so the transfer theorem is not
blocked by this finding.

---

### M4 — `MAJOR` — Proposition 12.6's hypotheses exclude `Ξ_a`, its intended application

Line 2622–2624:

> **Proposition 12.6 (`PROVED`).**  Let `Z` be entire of order `1` with
> `Z(s) = Z(1−s)`, real and positive on `R`, **all zeros in `0 < Re s < 1`**, …

The zeros of `Ξ_a(s) = ξ(s+a)ξ(s−a)` are `ρ ± a`, hence lie in
`−a < Re s < 1+a`, **not** in `0 < Re s < 1`. Yet line 2648 applies the
proposition to `Z = Ξ_a`. The hypothesis is not decorative: it is exactly what
the `Z`-analogue of Lemma 11.9 uses ("the zeros satisfy `0 < Re ρ < 1`, (E2), …
the strict separation of the exponents `ρ−½` from `±½`", lines 2214–2216 and
Remark 11.9a) and what makes the Laplace half-plane `Re s > 1` admissible.

**Minimal repair.** Replace the clause by `|Re ρ − ½| ≤ θ` with the same `θ` as
the polar set, take the Laplace transform on `Re s > ½+θ`, and *state* the
separation requirement `Z(p) ≠ 0` for `p ∈ P` (which the hypothesis "`Z` real
and positive on `R`" does supply for `Ξ_a`, since `P ⊂ R`, and which for
`Z = Ξ_a` amounts to `ξ(2a) ≠ 0`, `ξ(1−2a) ≠ 0` — classical, but currently not
cited anywhere).

---

### M5 — `MAJOR` — Proposition 12.6 is labelled `PROVED` on the strength of an announced re-reading

Line 2657–2659:

> ∎  `PROVED` (each substitution is a **line-by-line re-reading of the proofs of
> §§11–12**, the only quantitative inputs being holomorphy of `Φ_g` past
> `Re s = 1+θ` and the Chebyshev-type bound)

This is an assertion that a proof exists, covering roughly twenty statements
(Lemma 11.2 through Theorem 12.3) under four substitutions, including a change of
the operator `Π → Π_P` of order `#P` and of Lemma 3.1's Green-function
surjectivity argument (four vanishing conditions instead of two, with a
fourth-order Green kernel). Auditor's rule `R131_017`: prose reports of prose
repairs are not evidence. Every theorem of §13 that invokes Corollary 12.4a
(13.3, 13.7) and Theorem 12.4 itself rest on this label.

**Minimal repair.** Either write out the substitutions that are not verbatim (at
minimum: the `Π_P` analogue of Lemma 3.1, Lemma 11.9 with exponents in
`|Re ρ−½| ≤ θ`, the contour abscissa, the degree weight), or relabel
`PROVED` → `CANDIDATE`/`SKETCH`, and propagate the relabel to Theorem 12.4,
Corollary 12.4a, Theorems 13.3 and 13.7.

---

### M6 — `MAJOR` — the `Ξ_a`-analogue of Paper 45 Theorem 10.4 is asserted in a parenthesis inside a `PROVED` theorem, and the parenthesis mis-states the imports

Lines 2553–2559:

> *(That analogue is available: the proof of Theorem 10.4 uses only an off-line
> zero and its quartet, the interpolation construction of `106_11` (20)–(21),
> the Paley–Wiener import (E6) and the counting import (E3d); `Ξ_a` is entire of
> order one with `Ξ_a(s) = Ξ_a(1−s)`, real on `R`, and satisfies both counting
> statements …)*

Two problems.

1. The list of inputs is **wrong**. Paper 45's own proof (line 1730 ff., and its
   closing line "`PROVED`, using imports **(E2)'s last clause**, (E3d), (E6) and
   the repository construction `106_11` Theorem 1") uses (E2)'s last clause
   `ζ(σ) ≠ 0` for `σ ∈ (0,1)` — to secure `s_0² ∉ R`, i.e. `x_0y_0 ≠ 0` — and it
   is stated there to be "the **only** place in this paper where that import is
   used". The parenthesis omits it. (For `Ξ_a` the corresponding check happens to
   pass — Hardy's zeros give `s_0 = γ − ia`, `γ ≠ 0`, `a ≠ 0` — but the check is
   not performed.)
2. It also omits the *primitivity* change: Paper 45's Theorem 10.4 produces
   primitive tests through `F = ΠG` with `Π`'s symbol `s(1−s)` vanishing at the
   **two** points `{0,1}`. For `Ξ_a` primitivity is **four** conditions and
   `Π_P` is a fourth-order operator (Prop 12.6(S1)); Corollary 10.2, Lemma 10.3a
   and Paper 47 Lemma 3.1 all have to be redone. Proposition 12.6 explicitly
   covers "§§11–12", not Paper 45 §10, so this is not delegated anywhere.

**Minimal repair.** Promote the parenthesis to a numbered lemma with a proof (or
`IMPORTED`-with-hypotheses-checked), and add (E2)'s last clause to it; until
then Theorem 12.4 is `CANDIDATE`, not `PROVED`.

---

### M7 — `MAJOR` — `Λ_W` has zero generators: Theorem 13.5(i),(ii) are false as written, and `h⁰_Z` is not well defined

Line 2724:

>     Λ_W := ⨁_{n ≥ 2} Z·(Λ(n)n^{−1/2} τ_{\log n}(ΠK))

`Λ(n) = 0` for every `n` that is not a prime power. For such `n` the generator is
the **zero element**. Consequences, all fatal to §13.2 as written:

* Theorem 13.5(i) ("The generators of `Λ_W` … are linearly independent over `R`,
  so `λ ↦ E+λ` is injective and `#H⁰_Z` is well defined", line 2737) is false:
  infinitely many generators are `0`. The proof's last step — "hence all
  `a_n = 0` by uniqueness of Dirichlet coefficients" — recovers only
  `a_nΛ(n) = 0`, which is vacuous when `Λ(n) = 0`.
* Theorem 13.5(ii) `H⁰_Z(0) = {0}` and `h⁰_Z(0) = 0` is false: every
  `Z`-tuple supported on non-prime-powers maps to `λ = 0 ≥ 0`, so
  `#H⁰_Z(0) = ∞` and `h⁰_Z(0) = ∞`, violating (a) as a real-valued function and
  contradicting the numeric line "`#H⁰_Z(0) = #H⁰_{Λ_1}(0) = 1`" (line 2981) —
  the script evidently ranges over prime powers or over `n ≤ 5`, not over the
  index set of (13.1).
* Theorem 13.6's proof divides by `\min_n Λ(n)n^{−1/2}` over the active indices
  (line 2947), which is `0`.

**Minimal repair.** Index (13.1) by prime powers, `Λ_W := ⨁_{p,k} Z·(\log p)
p^{−k/2} τ_{k\log p}(ΠK)`. Theorem 13.5(i)'s Dirichlet-uniqueness argument then
works unchanged. Note this is a repair to the *one definition* the section
advertises as "one definition, not a menu".

---

### M8 — `MAJOR` — Theorem 13.6's proof of (13.4) is not a proof

Lines 2765–2786. The displayed inequality

>     0 ≤ mK(\log n_0+t_0) − |a_{n_0}|Λ(n_0)n_0^{−1/2}c_0
>         + c_1 Σ_{n<n_0}|a_n|Λ(n)n^{−1/2}

is then used as "whence … `Λ(n_0)n_0^{−1/2}c_0 ≤ mK(\log n_0+t_0) + c_1 B n_0\log n_0`".
The right-hand side grows with `B` and `n_0` while the left-hand side tends to
`0`: the inequality as derived is **vacuous** and cannot yield an upper bound on
`n_0` or on `B`. The two load-bearing steps are then asserted rather than proved:

> Applying the same inequality with `n_0` replaced by **the unique index
> attaining `B`** … one gets first `B = O(m)` … and then, for the **largest**
> active index, that `K(\log n_0+t_0) ≥ c/m` **is necessary** for `a_{n_0} ≠ 0`
> to be compatible with `B = O(m)` and the super-exponential decay

"the unique index attaining `B`" need not be unique; "is necessary" is not
derived (the other generators are not shown to be negligible at
`t = \log n_0 + t_0` — `ΠK` has support everywhere and the competing terms with
`n ≈ n_0` are of the same order). The conclusion `d(m) = O(\sqrt{\log m})` may
well be true, but it is not established here.

**Minimal repair.** Prove (13.4) properly (a clean route: evaluate the constraint
against the positive functional `deg` and against a family of test evaluations
separating the translates, using the super-exponential decay of `ΠK` to bound
the interaction matrix), or relabel Theorem 13.6 `CANDIDATE` / `PARTIAL`. As it
stands the sentence "**The candidate of Definition 13.4 does not satisfy (c)**"
is not proved — and with M7 the candidate is not even well defined.

---

### M9 — `MAJOR` — Theorem 11.14 silently replaces the archimedean term of (11.3) by a kernel integral on `D^W`

Line 2348 ff. (11.16) defines `A_F(u) := \mathrm{f.p.}∫_R F(u−t)K_∞(|t|)dt` and
line 2376 says "the archimedean part is the same interchange in `⟨h,ω_∞⟩`".
But (11.3) — the only explicit formula proved on `D^W` — carries the archimedean
term in the form `\frac1{2π}∫\hat h(τ)[Re ψ(¼+iτ/2) − \log π]dτ`. The identity

    \frac1{2π}∫\hat h(τ)[Re ψ(¼+iτ/2)−\log π]dτ = −\mathrm{f.p.}∫ h(t)K_∞(|t|)dt

is imported in (1.4) from Paper 44 Theorem 3bis.7 **for `h ∈ C_c^∞` with
`0 ∉ supp h`**, and the `t = 0` finite part from Paper 44 (8.5∞). Neither covers
`h = E⋆F^∨` with `E ∈ D^W` of unbounded support and `0 ∈ supp h`. The whole of
Theorem 11.14(ii) (the `κ_∞(F)` bound, hence `C_F`, hence the ample cone, hence
Theorem 12.3 Step 1) is computed on the kernel side.

**Minimal repair.** State the kernel form of the archimedean term as an explicit
lemma on `D^W` with its finite-part constant `κ_0`, with proof or with a named
`CLASSICAL` import; or carry the bound through the `\hat h`/digamma form.

*(Everything else in Theorem 11.14 checks out. The prime-part bound was verified
line by line: for `u ≥ T`, `1.03883‖F‖_∞e^{3T/2}e^{u/2}`; for `u < T`,
`1.03883‖F‖_∞e^{u+T} ≤ 1.03883‖F‖_∞e^{5T/2}e^{−u/2}` since `u ≤ T`; the mirror
sum and the sum of the two give (11.17). Only `ψ_{Ch}(x) = O(x)` is used, as
claimed — no zero-free region, no PNT. The `e^{5T/2}` constant is correct.)*

---

### M10 — `MINOR` — sign slip in the definition of the bracket `⟨h, W_{fin}+ω_∞⟩`

Line 1955–1956:

> Writing `⟨h,W_{fin}+ω_∞⟩` for **the last line minus the previous one**, as in
> (1.4) and Theorem 3.6,

The last line of (11.3) is `− Σ_{n≥2}Λ(n)n^{−1/2}[h(\log n)+h(−\log n)]`, i.e.
`−PRIME`; the previous line is `+ARCH`. "Last minus previous" is `−PRIME−ARCH`,
whereas (11.4) requires `PRIME − ARCH` — which is what the numerics use
("`T_∞(K) = PRIME − ARCH = 1`", line 2104). Repair: "the prime sum of the last
line minus the archimedean integral of the previous one".

---

### M11 — `MINOR` (honesty of labels) — §1.13's compliance clause is falsified by Part II and was not updated

Line 172–178 states that no statement about the **location** of the zeros of `ζ`
is made anywhere in this paper except inside (1.9), Theorem 3.7, Theorem 5.6 and
a bracket in §7.1. Part II uses, in proofs:

* `0 < Re ρ < 1` (E2) — Lemma 11.9 (line 2214), Theorem 11.10, Theorem 11.11;
* `ζ` has no zeros with `Re s ≥ 1` (E2) — Proposition 11.11a (line 2258);
* **Hardy's theorem**, import (X16): "`ζ` has infinitely many zeros on
  `Re s = ½`" — Theorem 12.4, line 2561, and it is *essential* there;
* `ζ(σ) ≠ 0` on `(0,1)` — required by M6, and by Prop 12.6's separation clause.

These are unconditional classical facts and therefore admissible as data under
the convention at line 1846 ("`ξ` is data"), but §1.13's factual claim about
the paper is now false. Repair: amend §1.13 with a `[phase 135]` clause listing
(E2) and (X16) as the classical zero-location data used in Part II, exactly as
§15 lists (X16).

---

### M12 — `MINOR` — `T_∞(K)` is written although Finding 11.0 proves `T_∞` does not extend to `K`

Line 2088: "`I_∞(K,K) = 2ξ(0)ξ(1) = ½`, and **`T_∞(K)`** `= ⟨K,W_{fin}+ω_∞⟩ = 1`".
Finding 11.0 (lines 1872–1886) proves that `T_∞`'s own formula (8A.21) does not
converge on a test of unbounded support, and §14.3(iii) repeats it. The symbol
`T_∞(K)` therefore denotes nothing. Repair: write `⟨K,W_{fin}+ω_∞⟩` throughout
(also in the numerics line 2104 and in the phase README).

---

### M13 — `MINOR` — two arithmetic slips in Proposition 12.6's substitution list

* (S2), line 2635: "`2\cosh(t/2) ⇝ Σ_{p∈P}Z(p)e^{(p−½)t}`". For `Z = ξ` the
  right side is `½(e^{t/2}+e^{−t/2}) = \cosh(t/2)`, i.e. **half** of `2\cosh(t/2)`.
  Consistently, `deg_Z F = Σ_pZ(p)Φ_F(p) = ½\deg F` for `Z = ξ`, so the claim at
  line 2646 that "§11 **is** the case `Z = ξ`" is off by the factor `2`
  (Definition 11.6's `\deg` is `Φ_F(0)+Φ_F(1)`, and Theorem 11.8(v) already
  records that it is `2K`, not `K`, that computes it).
* (S3), line 2638: "any `c` with `1 < c < 1+θ+ε`, where `Φ_g` is still
  holomorphic **and `Σ_n c_n n^{−c} < ∞`**". For `Ξ_a` the Dirichlet series
  converges only for `c > 1+a = ½+θ`, which `c > 1` does not guarantee. Repair:
  `½+θ < c < 1+θ+ε` (nonempty for all `θ`).

---

### M14 — `MINOR` — Lemma 11.2(ii)'s `Π(D^W ∩ C⁴) ⊆ D^W` needs decay of `g'''`, `g''''`, not merely `C⁴`

`(Πg)'' = −g'''' + ¼g''`, so membership of `Πg` in `D^W` requires (11.1) for
`j = 3,4`. Definition 11.1 imposes it only for `j = 0,1,2`. The proof's remark
("`Π` lowers the differentiability index by two … all elements of `D^W` used
below (`K`, `τ_aK`, `C_c^∞` tests) are `C^∞`") addresses smoothness, not decay.
Repair: state (ii) as `Π(D^W_4) ⊆ D^W` with `D^W_4` the subclass satisfying
(11.1) for `j ≤ 4`; `K` and `C_c^∞` lie in it (Theorem 11.7(ii) gives every
derivative).

---

### M15 — `MINOR` — `h⁰_Z := \log\#` with the convention `\log\#∅ = 0`

Line 2743: "`\deg E < 0 ⟹ H⁰_Z(E) = ∅`, so the convention `h⁰_Z := 0` there is
forced." `\log\#∅ = \log 0 = −∞`; `0` is a *choice*, not forced, and it makes
`h⁰_Z` fail to distinguish "no sections" from "only the zero section". Harmless
for (a) but it should be stated as a convention, not as forced. Also record
plainly that Definition 13.4 satisfies (b′) only on `{\deg > 0\}` (Theorem
13.5(iii)) and therefore is **not** a candidate satisfying (a)+(b′)+(c) even
before Theorem 13.6 — the section currently reads as if (c) were the only
failure.

---

### M16 — `NOTE` — the reduction is one-directional and its hypothesis is never shown satisfiable

Theorem 12.3 proves `(a)∧(b′)∧(c) ⇒ RH`. No converse, and no example (not even
under RH, not even for a function-field model) is offered showing the triple is
satisfiable at all. Combined with Corollary 12.4a's intended content (whatever
survives M1), the honest statement of Part II's deliverable is: *a sufficient
condition has been isolated and localized*, with no evidence that the condition
is non-vacuous. §14.5 and the closing paragraph (line 2946 ff.) should say so.
The blueprint's own §4 standard ("that is a structural theorem, not a sign") is
met; the satisfiability question should be added to §14.5 as open item (20).

---

### M17 — `NOTE` — (X12)'s normalization checked independently, and it is right

The auditor recomputed Pólya's kernel (11.7) at 40 digits:
`∫_R K = 0.4971207781883141099127737396853977198073 = ξ(½)` exactly to all
printed digits; `Φ_K(0) = ∫K\cosh(t/2)\,dt·? = 0.5`; `\deg K = ∫K·2\cosh(t/2) = 1`;
`K(0.3) = K(−0.3)` to 40 digits. The coefficients `4π²n⁴`, `6πn²` of (11.7) are
**twice** those of the `Φ(u)` displayed in several standard presentations of
Titchmarsh §10.1; the paper's normalization is the one consistent with
`Φ_K = ξ` under the convention (1.7), so the numbers are right, but the citation
"eq. (10.1.4) and the two displays following it" should be checked against the
edition, because as quoted it is the only evidence for the classical half of
Theorem 11.7(i) (evenness and `K > 0`).

The cancellation argument for `t → −∞` (lines 2062–2070) was checked and is
correct: `4x^{9/4}·\tfrac38x^{−5/2} + 6x^{5/4}·(−¼x^{−3/2}) = \tfrac32x^{−1/4} −
\tfrac32x^{−1/4} = 0`, error `O(x^{−9/4}e^{−π/x})`, i.e.
`O(e^{9|t|/2}e^{−πe^{2|t|}})`.

---

### Items checked and found **sound** (recorded so the ledger is not one-sided)

* **Lemma 11.2(iii)–(v)**: the two integrations by parts, the strip
  `S_ε = (−½−ε, \tfrac32+ε)`, the two-power bound (11.2), `\ker Π ∩ D^W = 0`.
  The `REFUTED` note on the blueprint's `e^{−(½+ε)|t|}` class (a),(b),(c) is
  correct on all three counts, including `Σ_ρ|γ_ρ|^{−1} = ∞`.
* **Theorem 11.3's contour bookkeeping**: `c = \tfrac32 ∈ S_ε`, `1−c = −½ ∈ S_ε`,
  `Σ_nΛ(n)n^{−3/2} < ∞`, horizontals `O(X_j^{−2}\log²X_j)`, absolute convergence
  of the zero sum from (11.2)+(E3d). Sound **for even `h`** (see M2).
* **Lemma 11.9**: the Laplace/residue argument is correct and genuinely
  multiplicity-honest (residue `m_{ρ_0}c_{ρ_0}`, `c_ρ` constant on the copies of
  a multiple zero); the interchange bound `(\mathrm{Re}\,z−½)^{−1}Σ|c_ρ|` is
  valid because `\mathrm{Re}\,ρ < 1`. No RH, no simplicity, no functional
  equation. The accompanying Remark 11.9a is accurate.
* **Theorem 11.10** and the honest unconditional form **(11.13)**: correct, and
  the refusal to write the equality is exactly right. (Small over-citation:
  the proof invokes Lemma 3.1's surjectivity, but only `Π(C_c^∞) ⊆ P` is
  needed, since `Φ_{ΠH}(s) = s(1−s)Φ_H(s)` always vanishes at `0,1`.)
* **Theorem 11.11** and **Proposition 11.11a**: both correct. The
  Riemann–Lebesgue argument on `Re s = \tfrac32` is clean, and the structural
  remark (`|ξ(½+iτ)| = e^{−π|τ|/4+O(\log|τ|)}` vs `O(τ^{−2})`) is right. The
  blueprint refutation is earned.
* **Theorem 11.13** and **Theorem 12.2 / 12.2a**: correct and trivial in the
  good sense.
* **Theorem 12.3**: the four steps were checked individually and the logic is
  valid given §11. `I_∞(K−nF,H') = m − nq` is right; Step 3's dominance of the
  quadratic term without `χ ≥ 0` is right; Step 4's degree contradiction is
  right; Remark 12.3b's necessity of `E' ≢ 0` is right. The contrapositive use
  of Paper 45 Theorem 10.4 is correctly directed. **Nothing in the proof uses
  the location of any zero.**
* **Theorem 13.2**, **Propositions 14.1, 14.2**, **Theorem 14.3**, **Finding
  11.0**: correct. Finding 13.8 is a clean record with no reconciliation by
  fiat, and remark 1's scale argument is sound.

---

## (B) Label verdicts, every labelled statement in §§11–14

| statement | claimed | verdict |
|---|---|---|
| Finding 11.0 | `PROVED` | **earned** |
| Definition 11.1 | — | earned (def.) |
| Lemma 11.2 | `PROVED` | **earned except (ii)** — relabel (ii) per M14 |
| `REFUTED` note on blueprint D.6(i) | `REFUTED` | **earned** |
| Theorem 11.3 | `PROVED-IN-REPOSITORY` | **earned for real even `h`**; does not cover Definition 11.4's use (M2) |
| Definition 11.4 | — | **not earned** — ill-defined for `F ≠ G` (M2); repair by polarization |
| Theorem 11.5 | `PROVED` | **not earned as stated**; earned after M2's repair |
| Definition 11.6 | — | earned |
| Definition–Theorem 11.7 | `CLASSICAL`+`PROVED` | **earned**; (i)'s citation precision flagged (M17) |
| Theorem 11.8 | `PROVED` | **earned modulo M2**; (ii)'s `T_∞(K)` notation → M12 |
| Remark 11.8a | — | earned as a remark; its "verbatim" depends on Prop 12.6 (M4,M5) |
| Lemma 11.9 | `PROVED` | **earned** |
| Remark 11.9a | — | **earned** |
| Theorem 11.10 | `PROVED` | **earned** |
| `REFUTED` note / (11.13) | `REFUTED` | **earned** — the one place the paper is exemplary |
| Theorem 11.11 | `PROVED` | **earned modulo M2** |
| Proposition 11.11a | `PROVED` | **earned** |
| Theorem 11.12 | `PROVED` | **not earned** → relabel `OPEN` (or `PROVED` after the simple-zero-density import), M3 |
| Remark 11.12a | — | inherits M3 |
| Theorem 11.13 | `PROVED` | **earned** |
| Theorem 11.14 | `PROVED`, unconditional | **(ii) prime part earned**; (i) and the archimedean part **not earned** (M9); (iii) earned given (ii) |
| `REPAIRED` note (ample class `A ∉ D^W`) | `REPAIRED` | **earned** |
| Remark 11.14a | — | inherits M4,M5 |
| Definition 12.1 / Theorem 12.2 | `PROVED` | **earned** |
| Theorem 12.2a | `PROVED` | **earned** |
| Theorem 12.3 | `PROVED` (conditional on `h⁰`) | **earned**, modulo M2 and M9 which are repairs inside §11, not in §12 |
| Remark 12.3a, 12.3b | — | **earned** |
| Theorem 12.4 | `PROVED` | **not earned** → `CANDIDATE` pending M5, M6 |
| Corollary 12.4a | `PROVED` | **not earned** → `SCHEMA`/`RESTATEMENT` about proofs, M1 (`FATAL`) |
| Remark 12.4b | — | **not earned as "the main structural output"**; rewrite per M1 |
| Proposition 12.5 | `RESTATEMENT` | **earned** (the (R1)–(R5) → (a),(b′),(c) table is accurate; `ℓ(M(E)) = −½I_∞(E,K) = −¼\deg E` checks out) |
| Remark 12.5a | — | earned |
| Proposition 12.6 | `PROVED` | **not earned** → `CANDIDATE`, M4 + M5 |
| Definition 13.1 / Theorem 13.2 | `PROVED` | **earned** |
| Theorem 13.3 | `REFUTED` as route / `PROVED` | **not earned** — inherits M1's invalid quantifier |
| Remark 13.3a | — | inherits M1 |
| Definition 13.4 | — | **not earned** — zero generators (M7) |
| Theorem 13.5 | `PROVED` | **(i),(ii) false as stated** (M7); (iii),(iv) earned after the prime-power repair |
| Theorem 13.6 | `PROVED` | **not earned** → `PARTIAL`/`CANDIDATE` (M8), and undefined object (M7) |
| Remark 13.6a | — | inherits M8; the `#`-loophole remark is honest and should be kept |
| Theorem 13.7 | `PROVED` | **not earned** — inherits M1 |
| Finding 13.8 | `PROVED` as arithmetic / `OPEN` as reconciliation | **earned** |
| Proposition 14.1 | `PROVED-IN-REPOSITORY` | **earned** |
| Proposition 14.2 | `PROVED-IN-REPOSITORY` | **earned**, except that its appeal to Theorem 13.5(i) inherits M7 (true for prime-power indices) |
| Theorem 14.3 | `PROVED` | **earned** |
| §14.4 ledger, §14.5, §15 imports | — | **earned**, except: (X13)/(X14) do not suffice for Theorem 11.12 (M3); §1.13 not updated (M11) |

---

## (C) Sign-violation sweep

Every occurrence in Part II (lines 1840–3038) of a claimed sign, an inequality on
the form, or RH/¬RH-implying content, with verdict.

| where | text | verdict |
|---|---|---|
| 1846–1854 | convention: `ξ` is data; every theorem survives `ξ → Ξ_a` | **compliant**; `ξ` is used as a function, never through its zeros' location |
| 1924–1925 (11.1), Def 11.6 line 2013 | `E ≥ 0` means `E(t) ≥ 0` pointwise | **not a sign on the form**; a cone in the test class. Compliant |
| 2025 (Thm 11.7(i)) | `K(t) > 0` for every `t` | **classical** (X12), about the kernel, not the form. Compliant |
| 2077 (11.9) | `\deg K = 1`, `Φ_K(0)=Φ_K(1)=½` | identity; verified numerically by the auditor. Compliant |
| 2088 | `I_∞(K,K) = 2ξ(0)ξ(1) = ½ > 0` | a **positive** value of the form on a *non-primitive* class. Compliant: row D's target is `≤ 0` on the **primitive** sector only, and `\deg K = 1 ≠ 0` |
| 2273–2281 (Rem 11.8a) | "Theorems 11.7 and 11.8 therefore carry no sign whatever" | **correct**, modulo M4/M5 on the `Ξ_a` transfer |
| 2492 (Thm 11.13(i)) | `E ≥ 0`, `E ≢ 0 ⇒ \deg E > 0` | positivity of a **linear functional against an explicit positive weight** `2\cosh(t/2)`. No zero input. Compliant |
| 2368–2372, 2563–2565 (Thm 11.14(iii)) | `2K` ample; `I_∞(E,H') > 0` for effective `E ≢ 0` | positivity of the form on the **effective cone**, not on the primitive sector; proved from Chebyshev + degree. Compliant, and it holds for `Ξ_a` |
| 2628–2636 (Thm 12.3(a),(b′),(c)) | `h⁰ ≥ 0`, `h⁰(E) > 0 ⇒ …`, (12.1) | **hypotheses**, explicitly conditional and `OPEN`. Compliant |
| 2636 | "Then `I_∞(F,F) ≤ 0` … and hence **RH**" | **conditional conclusion**; the boxed target appears only as a consequent. Compliant, and the derivation via Paper 45 Thm 10.4 is correctly directed (contrapositive of (1.10)) |
| 2640, 2647 | "suppose `q := I_∞(F,F) > 0`" | *reductio* hypothesis. Compliant |
| 2675 | "Hence `q ≤ 0`" | inside the reductio, under (a)+(b′)+(c). Compliant |
| 2545–2562 (Thm 12.4) | "every zero of `Ξ_a` lies on `Re s = ½` … Contradiction" | a statement about **`Ξ_a`'s** zeros, resolved by Hardy (X16). This **is** a zero-location input (M11) but is classical and unconditional, and concerns `ζ` only through Hardy's theorem. Compliant as mathematics; §1.13 must be amended |
| 2564–2572 (Cor 12.4a) | "`h⁰` does **not** satisfy (a)+(b′)+(c) for `ζ`" | **the one genuinely dangerous sentence in Part II.** It is not a sign, but read literally (M1) it asserts the unsatisfiability of Theorem 12.3's hypotheses, i.e. it silently converts the paper's reduction into a dead end while the paper advertises it as live. **Verdict: must be rewritten** |
| 2686–2696 (Thm 13.3), 2965–2974 (Thm 13.7) | "does not satisfy (a)+(b′)+(c)" | same defect, same verdict |
| 2756–2762 (13.3) | `h⁰_Z(mK) ≥ ¼m² − ¼m + χ` | a *consequence* of hypothesis (c), not an assertion. Compliant |
| 2932–2940 | `ΠK` "takes a **strictly negative** value" | true, from `\deg ΠK = 0` and `ΠK ≢ 0`. No zero input. Compliant |
| 2994, 3036, 1840–1843, 2946 | "no sign is claimed, asserted or suggested" | **upheld**: no unconditional sign appears anywhere in Part II. Confirmed by grep of every `≤ 0`, `≥ 0`, `> 0`, `< 0`, "positive", "negative", "sign", "RH" in lines 1840–3038 |
| §10 label line, §0.1 box | unchanged, `None` | **verified unchanged** |

**Circularity check (P122 §1).** `K` (`Φ_K = ξ`), `D^W`, `\deg`, `σ_K`, `Λ_W`,
`H⁰`, `h⁰` are all defined without the positivity of the form, its kernel, its
spectral decomposition, or the zeros' location. `𝓝_∞` is **defined** as the
radical of `I_∞` and only *characterized* through the zeros (Theorem 11.11) —
the right way round; no characterization is used as a definition anywhere. The
only forbidden-looking object would be a definition through `\{Φ_G(ρ) = 0\}`,
and (11.13) explicitly declines to make that an identification. **No circularity
found.**

---

## (D) Overall verdict

Part II is, in outline, what it claims to be: a genuine reduction theorem with no
sign in it. The spine — `D^W`, `Φ_K = ξ`, `I_∞(F,K) = ½\deg F`, the radical, the
degree, the Chebyshev ample cone, and the Hartshorne V.1.9 transport of
Theorem 12.3 — is correct, is free of any input about where the zeros are, and
does reduce the target to a single object `h⁰`; Lemma 11.9, Proposition 11.11a
and the unconditional form (11.13) are the strongest work in the campaign, and
the eight blueprint refutations of §14.4 are earned. **But it is not yet fit to
stand as written.** One finding is fatal and three are structural. `M1`
(Corollary 12.4a) is fatal twice over: its inference from uniformity of
*definition* to transfer of *truth* is invalid, and read literally its hypothesis
class is everything, so that the corollary asserts the unsatisfiability of the
very hypotheses Theorem 12.3 is advertised as reducing to — Part II's headline
"structural output" and all of §13's route-closing theorems (13.3, 13.7) rest on
it. `M2` leaves the cross pairing `I_∞(F,G)` literally undefined (one line of
polarization repairs it, costing nothing). `M4`+`M5`+`M6` mean the falsifier
apparatus — the entire justification for the recurring claim "this theorem
carries no sign because it holds verbatim for `Ξ_a`" — is currently an announced
re-reading with a hypothesis list that excludes `Ξ_a`. `M7`+`M8` leave §13's one
definition ill-posed and its refutation unproved. `M3` and `M9` are repairable
gaps in §11 that do not touch the transfer theorem. **Blocking for the reduction
theorem itself: M2 and M9 (both local repairs). Blocking for the paper's
falsifier claims and for §13: M1 (fatal), M4, M5, M6, M7, M8. Blocking for
Theorem 11.12 only: M3.** After those repairs, and with §1.13 amended (M11),
Part II is fit as a reduction theorem with no sign — and its honest deliverable
should be stated as in M16: a sufficient condition isolated and localized, with
no evidence yet that it is satisfiable.
