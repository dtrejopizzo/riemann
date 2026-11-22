# Phase 149 — The additive pencil of `Spec Z` and the Deligne extraction

**Row D · · status: round 1 delivered; audit `R149_002` done (D.61.10 and (P149) DOWNGRADE; see its §0); repairs `R149_003` and closing decision `R149_005` done; phase CLOSED**

## The question

Deligne's proof of the Weil conjectures uses five ingredients: (i) even tensor powers give
nonnegative traces (Rankin); (ii) Landau's lemma; (iii) the poles of the tensor-power `L`-function
of a **family** computed a priori by invariant theory, without knowing any fibre; (iv) an extraction
lemma (Weil I, 3.2) bounding one fibre by the family; (v) Künneth amplification.
Over `Z`, do (i)–(v) exist for the **additive pencil** `Z(s;α) = Σ_n Λ(n)e(nα)n^{−s}`, whose fibres
at `a/q` are combinations of `L(s,χ)`, whose fibre at `α = 0` is `ζ`, and whose "field size" is the
length `N`?

## The answer

**Four of the five are present. The missing one is (iii), and phase 149 says exactly why.**

| | over `F_q` | over `Z`, additive pencil |
|---|---|---|
| (i) Rankin positivity | ✔ | ✔ (but on the **multiplicative** square) |
| (ii) Landau | ✔ | ✔ (Paper 47 Thm 17.14) — but **useless on the additive square** (top pole at `s=2`) |
| (iii) a-priori poles by invariant theory | ✔ (Deligne/Katz–Sarnak) | ✖ — **(P149)**; only the large sieve, only `k=1` |
| (iv) extraction | ✔ | ✔ — **D.59, PROVED here** |
| (v) Künneth | ✔ | ✔ (Fujii / Languasco–Zaccagnini / Brüdern–Kaczorowski–Perelli) |

## Documents

| file | content |
|---|---|
| `R149_000_BLUEPRINT.md` | the blueprint's instructions (D.59–D.63), warnings W-H, W-a, the FATAL rule |
| `R149_001_ROUND1.md` | **document of record for round 1**: D.59–D.63, full proofs, labels, corrections C1–C10, open list |

## Results in one page

**D.59 — the extraction theorem. `PROVED`.** With `Q = N^{c}`, `0<c<1`, centering model
`M_Q(n) = Σ_{q≤Q}(μ(q)/φ(q))c_q(n)` and `S̃(a/q;N) = Σ_n(Λ(n)−M_Q(n))e(na/q)w(n/N)`:
if `M_{2k}(N) := Σ_{q≤Q}Σ*_a|S̃(a/q;N)|^{2k} ≤ C_k(log N)^{B_k}Q²N^k` for every `k`, then
`ψ_w(N) − Nŵ(0) ≪ N^{1/2+ε}`, hence RH. The mechanism is exactly Weil I 3.2: the `q=1` term is one
fibre, `Q² ≍ #F_Q` is the family size, and the extraction cost `Q^{1/k} = N^{c/k} → 1`.
A continuous (Bernstein) version and the equivalence "continuous hypothesis for all `k` ⟺
additive-twist RH" are also proved. **Novelty: folklore chain, first stated here — not a discovery.**
Three corrections of record were needed: the model cannot be a Selberg majorant (PNT-strength error
at `q=1`) nor the constant `1` (leaves the `μ(q)/φ(q)` main terms and makes the hypothesis false for
`k≥2`); the "hence RH" step needs a one-parameter family of test functions; and the model that works
is Vaughan's truncated singular series.

**D.60 — the kill test. The route is blocked, sharply, at `c = 1/2`.**

```
   c ≥ 1/2 :  H(1,c) is PROVED (= the Montgomery–Vaughan large sieve)  →  extraction gives N^{1/2+c} ≥ N.  Vacuous.
   c < 1/2 :  extraction gives N^{1/2+c} < N.  Useful  →  but H(1,c) is OPEN (follows from GRH).
```

The two ranges are complementary and disjoint. For `k ≥ 2` nothing unconditional exists at all
(de la Bretèche–Fiorilli 2023: *"we are not aware of any results on higher moments"*); Hölder from
`k=1` is vacuous. The Green–Tao restriction exponent `N^{r−1}` is **saturated by the major arcs**,
hence is exactly the coinvariant block and is zero-blind. **No chain produced a zero-free region:
the FATAL rule was not triggered.**

**W-H verdict: the hypothesis SURVIVES.** Hooley's conjecture was disproved by **Fiorilli–Martin**
(JEMS 25 (2023), 4791–4812) — *not* Bober–Goldmakher, as the blueprint stated — and the weaker form
by **Hayani** (arXiv:2407.01045). Both counterexample families live at `q ≍ log log x`
(`q`-averaged form: `Q ≤ √(log log x)`), contribute `N^{1+o(1)} = o(Q²N)` to `M_{2k}`, and are driven
by Littlewood's `ψ(x,χ) = Ω_±(x^{1/2}·lll x)` — an **RH-compatible** fluctuation. Hooley's conjecture
is false for a reason orthogonal to RH.

**D.61 — the finding of record: the split of the two squares. `PROVED`.**
On the additive square the pairing is `κ(d) = Σ_{q|d}μ²(q)/φ(q) = d/φ(d)` (and the singular series
`𝔖`); it is **positive-definite** (Bochner — free, a `RESTATEMENT`, not progress) and **zero-blind**;
the BDH main term is exactly `x·Q·κ(0)`; Landau's lemma sees only the a-priori top pole at `s=2`;
and twisting destroys the positivity, because `R(n) ≥ 0` comes from `Λ ≥ 0`, not from a square.
On the multiplicative square `|ψ(x,χ)|² ≥ 0` for every `χ`, so Rankin positivity is twist-stable and
Landau works (Paper 47 Thm 17.14) — but there is no a-priori computation of the poles.

> **Rankin/Landau lives on the multiplicative square; invariant theory lives on the additive square;
> nothing known transports between them. Over `F_q` they are the same square, because
> `H^•_c(X×X) = H^•_c(X)^{⊗2}` carries both the cup product and the weight filtration.**

This is a **fifth** independent wall, joining the four of `R148_005` §5.

**D.62 — Problem (P149)**, with the five things a solution must contain, and the partial mechanism
found (Ramanujan-sum orthogonality computes the diagonal of `M_{2k}` exactly: `M_{2k} = Σ_d κ_Q(d)𝒞_{2k}(d)`,
so `H(k,c)` is a `2k`-fold **additive-energy** bound; `k=1` is a theorem because its invariant theory
is Parseval and nothing more). `H(2,c)` implies the averaged Goldbach formula with square-root error,
hence (Bhowmik–Ruzsa) sits at or above RH in difficulty.

**D.63 — falsifiers.** `Ξ_a`: the *extraction theorem* is `Ξ_a`-uniform (so it carries no arithmetic),
while the *hypothesis* `H(k,c)` is **FALSE** for `Ξ_a` once `k > c/a` — the arithmetic is entirely
inside the hypothesis. `Ξ_Q`: the construction presupposes the Euler product. `ζ_K`: field-uniform,
same boundary `c = 1/2` (Huxley's number-field large sieve).

## Standing rules honoured

* **W-a analogue** — positivity is free here (Theorem D.61.5 is labelled `RESTATEMENT`, not progress).
* **FATAL rule** — checked and recorded at every chain in §3; not triggered.
* **NG-B1, NG-B8** — cited, not reopened. D.60 is a quantitative refinement of NG-B1 at the
  large-sieve entry: it locates the failure at the single exponent `c = 1/2`. No sign is claimed.
* **Corpus check per idea** — §1.1, grep-verified; BDH/Hooley/Farey/`κ`/Ramanujan-orthogonality are
  NEW in the corpus; phase-36 Doc 106 (Deligne amplification axiomatised) is cited, not rebuilt.
* **No scripts.** No counterexample range required numerical checking.

## Row D status

**No label change. No sign.** `PROVED` items are listed in `R149_001` §6.2.

## Next

Audit `R149_002`; then repairs, confirmation, and the closing decision `R149_005`.
Principal open item **O-149.5** should be recorded as the additive face of **O-148.2** — the two are
two faces of one question.
