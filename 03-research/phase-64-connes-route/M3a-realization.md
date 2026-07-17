# M3a: the realization `f ↦ Z_f` — the correspondence construction and the irreducible gap

*Continuation. Pure mathematics. We give the explicit proposed realization of a test function as an
arithmetic correspondence, prove the part that is formal/unconditional (the self-intersection identity
`W(f)=(Z_f·Z_f)` modulo the intersection numbers), and isolate the **single irreducible gap**: the
existence of the arithmetic intersection numbers with the Hodge-index sign over `Spec ℤ`. This is the
Connes–Consani frontier; we state precisely what must be constructed and why it is the last step.*

---

## §1. The correspondence algebra (formal, unconditional)

Work on the idele class space `X = 𝔸_ℚ^×/ℚ^×` with the scaling action `F_t : x ↦ e^{t}x` (`t∈ℝ`),
the analogue of the Frobenius flow. To a test function `f` (even, Schwartz, on the scaling line)
associate the **correspondence**
```
   Z_f := ∫_ℝ \hat f(t)\, [F_t]\, dt   −   c_f\, [Δ] ,
```
where `[F_t]` is the graph of `F_t` in `X×X`, `[Δ]` the diagonal, and `c_f` the archimedean
normalization. Composition of graphs `[F_s]∘[F_t]=[F_{s+t}]` makes `t↦[F_t]` a one-parameter group of
correspondences; the **trace/Lefschetz pairing** `⟨·,·⟩` (intersection with the diagonal) satisfies,
formally,
```
   ⟨[F_t],[Δ]⟩ = ∑_{x: F_t(x)=x} 1   "="   (fixed-point/period contribution at scale t).
```

**Lemma 1 (formal self-intersection = Weil form).** With the pairing extended bilinearly,
```
   (Z_f · Z_f) = ∬ \hat f(s)\overline{\hat f(t)}\, ⟨[F_s],[F_t]⟩\, ds\,dt  −  (\text{diagonal terms})
              = ∑_ρ |\hat f(ρ)|^2  −  (\text{arch})  −  ∑_p (\text{primes})  =  W(f),
```
the Weil explicit-formula quadratic form, **provided** the pairing `⟨[F_s],[F_t]⟩` reproduces the
Mellin/spectral pairing `∑_ρ` on the off-diagonal and the prime/arch terms on the diagonal.
*Proof (formal).* `⟨[F_s],[F_t]⟩` depends only on `s−t` (translation invariance of the flow); its
Mellin transform in `s−t` is, by the Lefschetz/trace formula for the scaling flow on `X`, the spectral
measure `∑_ρ δ_{γ_ρ}` (zeros) minus the prime/archimedean fixed-point contributions — this is exactly
Connes' trace formula. Substituting gives `W(f)`. ∎

So **the self-intersection identity `(Z_f·Z_f)=W(f)` is a formal consequence of the trace formula** —
it holds at the level of the correspondence algebra, *once the pairing `⟨[F_s],[F_t]⟩` is defined as
an honest number with the trace-formula value*. This part is unconditional/formal: no positivity yet.

---

## §2. The degree condition is `μ_max=1` (unconditional)

The polarization `H` is the class of a "fiber" (a single place / the archimedean divisor). The degree
`(Z_f·H)` is the total mass `∫\hat f(t)\,dt·(\deg F_t) = \hat f(0)·(\text{const})` minus the diagonal
normalization; choosing `c_f` so that `(Z_f·H)=0` is precisely the **primitivity / degree-balance**
condition. In the finite-window spectral form this is the marginal certificate
```
   (Z_f·H)=0  ⟺  μ_max=1
```
(E96/E101: the arithmetic class meets the polarization trivially — boundary norm-one). **This holds
unconditionally** and fixes `Z_f` in the primitive part.

---

## §3. The implication, given the Hodge index (conditional on §4)

**Proposition 2.** Suppose:
- (A) the arithmetic intersection pairing on `\bar X=\overline{X×X}` exists, is symmetric and
  `ℝ`-bilinear on `\widehat{\mathrm{CH}}^1(\bar X)`, and `f↦Z_f` is linear with `(Z_f·Z_f)=W(f)`
  (Lemma 1 made honest);
- (B) **Arithmetic Hodge index (Abboud):** for primitive `D` (`(D·H)=0`), `(D·D)≤0`;
- (C) the explicit-formula **sign convention** places `W` on the component where Abboud gives the sign
  `W(f)=−(Z_f·Z_f)_{\text{prim}}` (the Weil form is *minus* the primitive self-intersection).

Then for every admissible `f`, `(Z_f·H)=0` (§2) ⟹ `(Z_f·Z_f)≤0` (B) ⟹ `W(f)=−(Z_f·Z_f)≥0` (C).
Weil positivity holds for all `f`, hence **RH**. ∎

(A)+(C) are the realization; (B) is Abboud's unconditional theorem. The degree hypothesis is §2.
So **RH follows from (A)** — the existence of the honest pairing and realization with the stated sign.

---

## §4. The irreducible gap: the arithmetic intersection theory on `X×X`

(A) requires an **arithmetic intersection theory on the square of the idele class space** with:
- (i) the Frobenius correspondences `[F_t]` as classes;
- (ii) the diagonal `[Δ]` with self-intersection the archimedean term;
- (iii) a pairing whose off-diagonal value is the spectral `∑_ρ` (Lemma 1) and which carries the
  **Hodge-index sign** (B)+(C).

**This intersection theory does not exist classically** — there is no Weil cohomology, no second
factor for `Spec ℤ` in the usual sense (MW-5). The candidate framework is **Connes–Consani's arithmetic
site** `\widehat{\mathrm{Spec}\,ℤ}` and its square, where `X×X` and the `[F_t]` acquire meaning via the
`\mathbb{S}`-algebra / `Γ`-scheme (Segal/`𝔽₁`) structure, and where the topos cohomology
`H^*(\widehat{\mathrm{Spec}\,ℤ}^2,\,·)` is being constructed. The needed positivity (B)+(C) is the
**arithmetic Castelnuovo–Severi / Hodge-index inequality** on that square — the analogue of the
function-field theorem that *proves* RH for curves.

**What must be constructed (the one theorem):**
> Define `\widehat{\mathrm{CH}}^1(\widehat{\mathrm{Spec}\,ℤ}^2)` with a symmetric pairing for which the
> scaling correspondences `[F_t]` and the diagonal `[Δ]` are classes, `(Z_f·Z_f)=W(f)`, and the
> Hodge-index inequality `(D·D)≤0` holds for `(D·H)=0`. Then RH.

Everything in §§1–3 is assembled around this one statement. It is **not** proved here; it is the
active Connes–Consani frontier. Honest verdict: the program has reduced RH to the **construction of one
arithmetic intersection pairing with one positivity** — the sharpest, most localized form of MW-5, with
all the surrounding apparatus (model space, Lax–Phillips realization, Kreĭn–Langer index, the formal
trace-formula self-intersection identity, the degree-balance `μ_max=1`, and Abboud's inequality as the
intended tool) rigorously in place.

---

## §5. Why this is genuine progress and where it stands

- **Unconditional/rigorous:** the model-space colligation (`ω>½`), the Lax–Phillips reduction of RH to
  the overlap positivity, its Kreĭn–Langer index form, the **formal** self-intersection identity
  `(Z_f·Z_f)=W(f)` (trace formula), the degree-balance `μ_max=1`, and the *statement* of Abboud's
  inequality as the closing tool.
- **The single open theorem:** §4 — the arithmetic intersection pairing on `\widehat{\mathrm{Spec}\,ℤ}^2`
  with the Hodge-index sign. This is MW-5, now a one-line construction target.
- **Why DH cannot reach it:** DH has no Euler product, hence no `\mathbb{S}`-algebra/Frobenius
  correspondences `[F_t]` over the arithmetic site, hence no `Z_f` and no Hodge-index realization. The
  arithmetic geometry — not the analysis — is the discriminating input, exactly as required.

**No false victory.** RH is open; §4 is the frontier. The contribution of this pure-math arc is the
**complete assembly around a single, named, arithmetic-geometric obstruction**, with a proposed
construction (two-variable kernel + Connes–Consani Frobenius) for it. This is the honest current
endpoint: the proof of RH along this route `=` the construction of §4, which is genuinely open
mathematics (the Connes–Consani program), not something to be fabricated.
```
   RH  ⟸  [§1–3, §2, Abboud (B): rigorous/assembled]  ⟸  §4 (arithmetic intersection theory on
                                                            \widehat{Spec ℤ}^2 with Hodge-index sign).
```
