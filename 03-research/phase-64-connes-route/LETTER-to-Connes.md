# A letter to Alain Connes — the colligation route, where it lands, and the object we must create

Dear Professor Connes,

This letter accompanies the paper **P50, *The Colligation Route to the Riemann Hypothesis***. Its
purpose is to tell you, plainly and honestly, what we did along the route you proposed, exactly where
we landed, what I believe is now needed to cross the wall, and why I am convinced that crossing it
requires *creating* a piece of mathematics that does not yet exist. I include a map.

Throughout, one rule has governed the work: **a false victory is worse than failure**. Nothing below
claims RH. Every statement is either a theorem (proved) or is flagged as open. Where I corrected my
own earlier proposals — including ones I sent you — I say so.

---

## 1. What we did

Following your three replies, we took the de Branges / Lax–Phillips colligation attached to
`ξ(½+iz)` and carried it from numerics to theorems. The numerical phase (now closed) verified, on the
genuine ζ and against the Davenport–Heilbronn (DH) falsifier, every object you named: the Herglotz
property of `m=−Ξ'/Ξ`; the Pick-matrix passivity of the shifted scattering `Θ_ω` down to ω=0, failing
off-line exactly at `ω=β−½`; the de Branges kernel `K_κ` positivity; the Kreĭn–Langer index; and the
regularized continuation margin surviving `ω↓0`. With those confirmed, we switched, at your encouragement
and the user's, to **pure mathematics** and proved what could be proved.

## 2. What is now unconditional (four results)

1. **`L1 ⟺ RH`** (P50 §3). The finite-window boundedness `L1` of the oscillatory part of the Weil
   form is *equivalent* to RH. The forward direction is your Laplace–pole theorem; its only non-formal
   input is a **Paley–Wiener nonvanishing lemma**, which we prove unconditionally: the window transform
   `ê_n(ρ)=(e^{ρL}−1)/(ρ+2πin/L)` vanishes only at purely imaginary `ρ`, and no nontrivial zero is
   purely imaginary. So the residue at every off-line zero is nonzero, and boundedness forbids off-line
   zeros. This makes precise that `L1` is *not* a lemma below RH — it is RH — so no analytic averaging
   (Cesàro, monotone continuation) can reach it; those are RH-equivalent, as you warned.

2. **The Kreĭn–Langer index is the sharp invariant** (P50 §4): `ind₋(K_{S_κ}) = #{off-line zeros}`, so
   `RH ⟺ ind₋=0`. This is strictly stronger than the boundary certificate `μ_max=1`, which is blind to
   the interior off-line spectrum. ζ has `ind₋=0`; DH has `ind₋=2·#{its off-line zeros}`.

3. **A curvature theorem** (P50 §5, *new*). After Doob conjugation the prime part of the Weil generator
   is a Beurling–Deny pure-jump Dirichlet form, and its **iterated carré-du-champ satisfies `Γ₂≥0`
   unconditionally** — a Bakry–Émery `CD(0,∞)` bound. The mechanism is clean: `Γ₂` is the Gram form of
   the Hadamard square `B^{∘2}` of `B(ξ,η)=½[ψ(ξ)+ψ(η)−ψ(ξ−η)]`, and
   `B = Σ_j c_j[(1−\cos a_jξ)(1−\cos a_jη)+\sin a_jξ\sin a_jη]` is positive-definite **because the von
   Mangoldt weights `c_j=Λ(p^k)/√{p^k}>0`**; Schur's product theorem finishes it. The Euler product
   enters as exactly this positivity (`\log=Λ*1` with nonnegative coefficients), and **DH breaks it**
   (its character-twisted weights make `B` indefinite). This is the first time, in our work, that
   multiplicativity enters as a *local, algebraic* positivity rather than as an analytic miracle.

4. **The wall as a Schrödinger bound state** (P50 §6). In the coordinate `θ=πy/L` the Weil form is a
   Dirichlet Schrödinger operator `H_λ=−d²/dθ²+W_λ`, and `ε₀≥0 ⟺ H_λ` has no negative bound state
   `⟺ ‖K_λ(0)‖≤1` for the Birman–Schwinger operator. The **pole of ζ at s=1 is a repulsive barrier**
   `W^{pole}=+p_λ≥0`; the Perron–Frobenius `u₀` is the threshold resonance, pinned at eigenvalue 1 by
   the pole. **DH is entire — it has no pole, hence no barrier — so its well binds a negative state and
   `ε₀<0`.** This is, I believe, the cleanest possible statement of why the falsifier cannot be
   positive.

(Two honest self-corrections are recorded in P50: the scalar Euler product is a boundary/strip object,
not an analytic product on `ℂ₊`; and a Lieb–Thirring trace bound is too lossy at marginality — the
sharp tool is the Birman–Schwinger principle, not the trace.)

## 3. Where we landed — shape versus sign

Assembling all of this produced one sharp, and to me decisive, structural fact:

> **Every geometric and functional-analytic structure on the route — the curvature, the de Branges
> colligation, the Kreĭn–Langer index, the Hodge-index surface — is built from the Doob-reduced
> generator `G_λ=A−ε₀`, and is therefore *blind to the additive constant `ε₀`*.** It proves the
> *shape* — the `(k+1)²` ladder, `CD(0,∞)`, the internal gap `(π/L)²`, the colligation — **without
> any hypothesis**. RH is the *sign* `ε₀≥0`, the one quantity orthogonal to all Doob/scale-invariant
> structure.

This explains, in a single sentence, why every route in the whole programme terminates at the same
wall: they are all reformulations of the shape, and the shape is unconditionally positive. The
irreducible content is the sign.

And the sign has a precise operator form. `ε₀≥0` is `‖K_λ(0)‖≤1`: the Birman–Schwinger spectral radius
is exactly 1. **The pole pins it `≥1` from below** (the `u₀` resonance). What must pin it **`≤1` from
above** is RH — and that upper pinning is *missing*.

## 4. The map

```
   UNCONDITIONAL (proved)                         THE WALL                      OPEN (to create)
   ─────────────────────────                   ─────────────                 ──────────────────

   L1 ⟺ RH  ──►  ind₋=0  ──►  Γ₂≥0 (prime)                                
   (Lemma PW)    (Kreĭn-     (Schur/Λ≥0)                                   
                 Langer)         │                                        
                                 │ shape (Doob-invariant)                 
                                 ▼                                        
   SHAPE: (k+1)² ladder,  ───►   ε₀ ≥ 0  ?   ◄─── SIGN = RH  ◄───  Weil-pairing analogue
   curvature, colligation        (μ_max = 1,        (BS spectral         over Spec ℤ:
   [all unconditional]           marginal)           radius ≤ 1           arithmetic Hodge index
                                 ▲                    from above)         on  (Spec ℤ‐hat)²
                                 │                                          [does not yet exist]
                       Pole of ζ at s=1                                  
                       = repulsive barrier                               
                       (BS radius ≥ 1 from below;                        
                        DH entire ⇒ none ⇒ ε₀<0)                         
```

The green spine (left) is rigorous. The two red boxes (pole from below; shape) meet at the wall. The
blue box (right) is the missing object that would pin the spectral radius from above. In the
function-field model that box is the **Weil pairing**: Frobenius on `H¹(C/F_q)` is an isometry of a
positive intersection form, so `|eigenvalues|=√q` — the curve RH. Over `Spec ℤ` there is no such
object.

## 5. What I believe must be done — and why it requires creating new mathematics

The upper pinning is, precisely, an **arithmetic Weil pairing over `Spec ℤ`**: an intersection theory
on the square of your arithmetic site `\widehat{Spec ℤ}`, with

- the scaling/Frobenius correspondences `[F_t]` as classes,
- a diagonal `[Δ]` whose self-intersection is the archimedean term,
- a symmetric pairing for which the realization `f ↦ Z_f` satisfies, *formally by the trace formula*,
  `(Z_f · Z_f) = W(f)` (the Weil quadratic form), and
- a **Hodge-index inequality** `(D·D) ≤ 0` for primitive `D` (your Abboud's arithmetic Hodge index is
  the intended tool), where the degree condition `(D·H)=0` is exactly the marginal `μ_max=1` we observe.

Given this object, RH follows (P50 §7). The point of this letter is that **this object does not exist
in current mathematics**, and I do not think it can be assembled from existing pieces:

- There is no Weil cohomology, and no honest second factor for `Spec ℤ`, in the classical sense — this
  is the wall that the whole programme keeps returning to (we call it MW-5).
- Your arithmetic site `\widehat{Spec ℤ}` is, I believe, the right home, but the **square** of it,
  with intersection theory and the Frobenius correspondences carrying the Hodge-index *sign*, is not
  yet constructed.
- Every purely analytic / Hilbert-geometric reformulation we tried (Pick passivity, Herglotz, de
  Branges, Birman–Schwinger, even the new curvature) is provably **Doob-invariant or RH-equivalent**:
  it cannot supply the sign. The sign is arithmetic.

So I have stopped looking for the proof inside the analysis, and I am convinced the next step is an
**act of construction**: to *create* the arithmetic intersection pairing on `\widehat{Spec ℤ}^2` — the
Weil-pairing analogue — with the property that the pole-pinned Birman–Schwinger radius is bounded
above by 1. This is not a search for a known theorem; it is the invention of the missing geometry,
exactly the kind of thing your arithmetic-site programme exists to build.

A concrete starting point I propose (P50 §7, O1): build the pairing from the **two-variable completed
kernel** `ξ(½+iz)ξ(½+iw)` and its Frobenius/Hecke deformation, taking the arithmetic-site Frobenius as
`[F_t]`; the diagonal restriction must recover the one-variable explicit formula, and the off-diagonal
(Castelnuovo–Severi) part must supply the negative self-intersection that is the upper pinning.

## 6. What I would ask of you

1. Is the **square** `\widehat{Spec ℤ}^2` of the arithmetic site, with intersection theory and the
   scaling correspondences `[F_t]`, within reach of your current framework — and does it carry a
   Hodge-index *sign* (an Abboud-type `(D·D)≤0` for primitive classes)?
2. Does the marginal certificate `μ_max=1` correspond, in your framework, to the **degree-zero /
   Euler-characteristic-balance** condition `(Z_f·H)=0`, as our computations suggest?
3. Is there a structural reason — a Weil-pairing / Rosati-positivity analogue on the arithmetic site —
   that would pin the **Birman–Schwinger spectral radius `≤1` from above**, dual to the way the pole
   pins it `≥1` from below? This is the single missing inequality.
4. If the object must be created from scratch, would you guide which of its axioms (the pairing, the
   correspondences, the Hodge-index sign, the realization `f↦Z_f`) is the load-bearing one to construct
   first?

I am ready to develop, in full detail and with you as evaluator, whichever construction you judge most
promising. The shape is done and unconditional; the sign is one act of arithmetic-geometric creation
away, and I believe it is yours to point toward.

With great respect and gratitude for the route you opened,

— David Alejandro Trejo Pizzo

*Enclosures: P50 (`main.pdf`); the supporting development notes (`CONSTRUCTION-critical-gram`,
`M3-arithmetic-index`, `M3a-realization`, `CONSTRUCTION-spectral-surface`, `CURVATURE-computation`,
`POLE-DEFECT-estimate`); the two earlier reports.*
