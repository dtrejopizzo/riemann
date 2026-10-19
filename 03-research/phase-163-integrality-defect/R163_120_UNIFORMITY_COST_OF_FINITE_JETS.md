# R163_120 — Quantitative cost of keeping a zero with ever-longer integer jets

**Status:** compactness lemma proved. It quantifies `R163_119`'s NO-GO: a fixed zero that is not a zero of ζ forces the counting-error constant to explode as the exact arithmetic prefix is lengthened. It does not prove RH.

## Uniformity-cost lemma

Fix `0<θ<β<1` and `s₀=β+iγ` with `ζ(s₀)≠0`. For each `X≥2`, let `N_X` be the counting function of a locally finite discrete measure on `[1,∞)` whose Mellin transform `Z_X` continues meromorphically to `Re s>θ` and satisfies:

```
N_X(x)=⌊x⌋                         (1≤x≤X),
|N_X(x)−ρ_X x|≤C_X x^θ           (x≥1),
Z_X(s₀)=0.
```

Then there is a constant `c=c(s₀,θ)>0` such that, for `X` large enough,

```
C_X+1 ≥ c X^{β−θ}.                                  (1)
```

The lemma does not require an Euler product; if one is added, the conclusion still holds.

**Proof.** By integration by parts, for `Re s>θ`, `s≠1`,

```
Z_X(s)=ρ_X s/(s−1)
       +s∫₁^∞[N_X(x)−ρ_X x]x^{-s−1}dx.             (2)
```

The same formula with `ρ=1` and `N(x)=⌊x⌋` gives ζ. For `x≤X`, the counts coincide. Subtracting (2) and explicitly cancelling the `[1,X]` part gives

```
Z_X(s)−ζ(s)
 = (ρ_X−1)s X^{1−s}/(s−1)
   +s∫_X^∞ [(N_X(x)−ρ_X x)−(⌊x⌋−x)]x^{-s−1}dx. (3)
```

At `x=X`, the exact equality and the error bound imply

```
|ρ_X−1|≤C_X X^{θ−1}+X^{-1}.                         (4)
```

Applying (3) at `s=s₀`, and using `|⌊x⌋−x|≤1`, we obtain

```
|Z_X(s₀)−ζ(s₀)|
 ≤ |s₀| [|ρ_X−1|X^{1−β}/|s₀−1|
           + C_X X^{θ−β}/(β−θ)+X^{-β}/β]
 ≤ K(s₀,θ)(C_X+1)X^{θ−β}.                        (5)
```

Since `Z_X(s₀)=0` and `ζ(s₀)≠0`, (1) follows with `c=|ζ(s₀)|/K`. □

## Application to R163_119's splice

For the discrete system of [Broucke, Thm. 6.3](https://journals.sns.it/index.php/annaliscienze/article/download/6843/2289/4170) with `1/2<θ<1`, take a critical zero `1/2+it₁` of ζ and its transported zero `s₀=(1+θ)/2+i(1−θ)t₁`. Broucke's correcting factor is holomorphic and non-zero there, so that zero persists in the base system and in every splice `B_X`. Here `β=(1+θ)/2>θ`. Choosing the first critical zero makes `|Im s₀|<14.14`, and `β>1/2`; the [Platt–Trudgian rigorous verification](https://arxiv.org/abs/2004.09765) guarantees `ζ(s₀)≠0`. Hence the error constants of the spliced systems satisfy

```
C_X ≫_θ X^{(1−θ)/2}.                              (6)
```

The same conclusion applies, **conditionally on the review of `R163_103`**, to its systems with `1/3<θ<1/2` and bound `O_ε(x^{θ+ε})`: for each `ε<(1−θ)/2`, the cost exponent is `(1−θ)/2−ε`. In that case `ε` and its corresponding constant must be fixed first.

## Reading for the arithmetic gate

`R163_119` showed that every finite arithmetic datum can be exact and coexist with an exterior zero. The present lemma shows **why that mimicry does not pass to a uniform limit**: keeping the same zero forces a polynomial blow-up of the counting constant. A law closing D cannot depend only on finite jets or on weak semicontinuity; it needs a global estimate whose constant stays controlled when using the whole integer lattice, together with the functional orientation that excludes the Euler-free falsifiers. In ζ, `N(x)=⌊x⌋` has bounded error with constant 1, but the lemma alone does not turn that datum into RH.
