# R163_103 — Random Witt rounding: discrete countermodels up to the 1/3 frontier

**Status:** complete internal proof, pending external review. **Does not close Row D.** It resolves `R163_101`'s `C_{1/3}` conjecture in the sense indicated below. Together with Broucke's discrete construction for `θ≥1/2`, it rules out a class threshold for paper 48 strictly greater than `1/3`. The paper is not modified.

## Theorem

For every `1/3 < θ < 1/2` there exists a **discrete** Beurling system (a multiset of real primes with integer multiplicities) with

```
N_B(x)=ρ_B x+O_ε(x^{θ+ε})   for every ε>0,
```

whose zeta has infinitely many zeros on `Re s=(1+θ)/2>1/2`. The same argument at `θ=1/3` gives `N_B(x)=ρ_B x+O_ε(x^{1/3+ε})` for every `ε>0` and zeros on `Re s=2/3`. The constant `ρ_B>0` depends on the chosen realization. The bound with `+ε` does not imply a strict bound `O(x^{1/3})` at the endpoint.

This is an **existence-by-probability** result, not a statement about ζ. The new part relative to `R163_101 §4` is a moment estimate that controls *all* orders of the convolution product, not just the linear and quadratic terms.

## 1. Positive Witt factorization and rounding

Set `a=θ/(1−θ)`, `Q_p=p^{1/(1−θ)}` and `q_{p,m}=Q_p^m`. Broucke's extended zeta is

```
Z_θ(s)=ζ((s−θ)/(1−θ))=∏_p(1−p^a Q_p^{-s})^{-1}.
```

Its **prime** multiplicities at positions `q_{p,m}` are not the coefficients of `dΠ_θ`. They are the Witt coefficients

```
w_{p,m}=(1/m) Σ_{d|m} μ(d) p^{a m/d} > 0.
```

Positivity for real arguments `p^a>1` is Broucke's Lemma 6.1, [§6.1](https://arxiv.org/abs/2409.10051). The exact identity is checked by `Σ_{m|k}m w_{p,m}=p^{ak}`:

```
∏_{m≥1}(1−q_{p,m}^{-s})^{-w_{p,m}}=(1−p^a Q_p^{-s})^{-1}.
```

For each pair `j=(p,m)` we independently choose `M_j∈{⌊w_j⌋,⌈w_j⌉}` with `E M_j=w_j`. Then `ε_j=M_j−w_j` satisfies `E ε_j=0`, `|ε_j|≤1`, and the `M_j` are non-negative integers. The discrete list that places `M_j` primes at `q_j` defines `B`. Formally, and then by convergence for `Re s>1`,

```
ζ_B(s)=Z_θ(s) exp Z(s),
Z(s)=Σ_j ε_j log(1−q_j^{-s})^{-1}.
```

**Importance of the Witt transform.** Rounding the weights `p^{ma}/m` of `dΠ_θ` directly as if they were prime multiplicities would be wrong: the powers of those primes would contribute extra terms. Witt inversion subtracts exactly those terms before rounding.

## 2. Zeros: the random factor is holomorphic and never zero

Let `σ₀=(1−θ)/2`. We have

```
Σ_j q_j^{-2σ} = Σ_p Σ_{m≥1}p^{-2σ m/(1−θ)} < ∞   if σ>σ₀.
```

The `k=1` part of `Z(s)` is `Σ_j ε_j q_j^{-s}`. On every compact rectangle contained in `Re s>σ₀`, the partial sums form a martingale of analytic functions whose increments have summable squared Bergman norms: by independence and zero mean, the sum of the expectations of the squared norms is dominated by a constant times `Σ q_j^{-2σ_1}`, with `σ_1>σ₀` smaller than the real parts in the rectangle. Martingale convergence in that Hilbert space, followed by the interior-evaluation inequality, gives almost-sure locally uniform convergence. A countable exhaustion by rectangles gives a single probability-one event.

The tail `k≥2` of `log(1−q_j^{-s})^{-1}` converges absolutely and locally uniformly in the same half-plane, because it is dominated by `C Σ_j q_j^{-2σ_1}`. Hence `Z` is almost surely holomorphic on `Re s>σ₀` and `exp Z` does not vanish there. The identity above extends `ζ_B` meromorphically to that region. Each zero `1/2+it` of ζ transports to

```
s=θ+(1−θ)(1/2+it),       Re s=(1+θ)/2>σ₀.
```

There are infinitely many such zeros; they are not cancelled by `exp Z`.

## 3. Moment lemma for the full convolution

Write `K_j` for the signed measure with transform `(1−q_j^{-s})^{-ε_j}` and `K_J=*_{j∈J}K_j` for finite `J`. Its coefficient at `q_j^k` is

```
c_k(ε_j)=(ε_j)_k/k!,     c_0=1,
```

with `|c_k(ε_j)|≤1` for `k≥1` and `|ε_j|≤1`. Denote `U_j=E K_j`, `X_j=K_j−U_j`. `U_j`'s coefficient at `q_j` is zero, because `E ε_j=0`; all of `X_j`'s coefficients have zero mean.

For `x≥2` define the weight, for `u≥1`,

```
W_x(u)=x^θ u^{-θ}     (u≤x),
W_x(u)=x u^{-1}       (u>x).
```

Checking the three cases `u,qu≤x`, `u≤x<qu` and `u>x` gives

```
W_x(qu) ≤ b_x(q) W_x(u),
b_x(q)=q^{-θ}                    (q≤x),
b_x(q)=x^{1−θ}q^{-1}            (q>x).
```

Fix an integer `r≥2` and let `C_{r,J}(x)` be the supremum of `||∫F dK_J||_{L^r}` over deterministic real functions `F` with `|F(u)|≤W_x(u)`. If an index `j∉J` is added, we split the contribution `K_j=U_j+X_j` into a part `A` measurable with respect to the old indices and a part `Y` with `E(Y|old indices)=0`. Minkowski, independence and the weight above give

```
||A||_r ≤ α_j(x) C_{r,J}(x),
||Y||_r ≤ β_{j,r}(x) C_{r,J}(x),
α_j=1+Σ_{k≥2}|E c_k(ε_j)| b_x(q_j^k),
β_{j,r}=Σ_{k≥1}||c_k(ε_j)−E c_k(ε_j)||_r b_x(q_j^k).
```

For real variables and `r≥2`, Taylor's inequality

```
|A+Y|^r ≤ |A|^r+r|A|^{r−2}AY+C_r(|A|^{r−2}Y²+|Y|^r)
```

kills the linear term upon conditioning and, by Hölder, produces

```
C_{r,J∪{j}}(x)^r ≤ [α_j^r+C_r(α_j^{r−2}β_{j,r}²+β_{j,r}^r)] C_{r,J}(x)^r.
```

Since `C_{r,∅}(x)=W_x(1)=x^θ`, `α_j−1≪b_x(q_j²)` and `β_{j,r}≪_r b_x(q_j)`, we obtain, uniformly over finite sets `J`,

```
C_{r,J}(x) ≪_r x^θ exp{C_r[Σ_j b_x(q_j²)+Σ_j b_x(q_j)²]}.
```

The chaos expansion was not truncated: the recursion includes every product of the `K_j`.

### Evaluating the two sums

If `θ>1/3`, `Σ_j q_j^{-2θ}<∞`. Since `b_x(q)≤q^{-θ}` and `b_x(q²)≤q^{-2θ}`, both sums are bounded independently of `x`; hence

```
sup_J ||∫F dK_J||_r ≪_r x^θ.
```

For `θ=1/3`, the `m=1` positions are `q_{p,1}=p^{3/2}` and give

```
Σ_{q_j≤x}q_j^{-2/3} ≪ log log(3x),
x^{4/3}Σ_{q_j>x}q_j^{-2} ≪ 1,
Σ_{q_j≤√x}q_j^{-2/3} ≪ log log(3x),
x^{2/3}Σ_{q_j>√x}q_j^{-2} ≪ 1.
```

We use the classical bound `π(y)≪y/log y` and the convergence of the `m≥2` part; hence both sums are `O(log log(3x))` and `C_{r,J}(x)≪_r x^{1/3}(log(3x))^{C_r}`.

## 4. From the lemma to `N_B(x)`

The integer measure of `Z_θ` satisfies `N_θ(y)=(1−θ)y+E_θ(y)`, `|E_θ(y)|≤C y^θ` for `y≥1`. For finite `J`, the integer measure of the partially rounded system is `dN_J=dN_θ*K_J` and its residue is

```
ρ_J=(1−θ)∫u^{-1}dK_J(u).
```

An exact identity separates the leading term:

```
N_J(x)−ρ_J x = ∫F_x(u)dK_J(u),
F_x(u)=E_θ(x/u)   if u≤x;
F_x(u)=−(1−θ)x/u if u>x.
```

So `|F_x(u)|≤C W_x(u)`, and the lemma gives uniform moments `||N_J(x)−ρ_Jx||_r≪_r x^θ` if `θ>1/3`, or `≪_r x^{1/3}(log(3x))^{C_r}` at the endpoint.

Since `Σ_j q_j^{-1}<∞` for `θ>0`, the products defining `ρ_J` converge absolutely to some `ρ_B>0`. For each `x`, `N_J(x)` stabilizes once every position `q_j≤x` has been included; Fatou passes the moment bounds to the limit `N_B(x)−ρ_Bx`.

By Markov on a mesh of step `X^{θ+ε}` inside each dyadic interval `[X,2X]`, and taking `r` large enough that `rε>1−θ`, the probability of a violation on the mesh is summable over dyadic scales. Borel–Cantelli gives the almost-sure bound at mesh points. The monotonicity of `N_B` and the linearity of `ρ_Bx` extend the bound to intermediate points. The polylogarithmic factor at the endpoint case is absorbed by any `x^ε`. A countable intersection allows every `ε>0` at once.

## 5. Scope and adversarial tests

- **It does not prove RH or Row D.** If the class target requires that every system with error exponent `η<θ₀` have no zeros in `Re s>θ₀` off `1/2`, our examples refute it directly for `1/3<θ₀<3/4`: choose `1/3<θ<min(1/2,θ₀)` with `θ+ε<θ₀` and `(1+θ)/2>θ₀`. For `θ₀≥3/4` and `θ₀<1`, Broucke's discrete construction with parameter `θ∈(max(1/2,2θ₀−1),θ₀)` supplies the falsifier (its error is `O(x^θ)` if `θ>1/2`). Hence the **combination** rules out every threshold `1/3<θ₀<1`; `R163_103` alone does not cover the higher thresholds.
- **It does not resolve the strict case `θ<1/3`**, nor the case `θ=0`. The quadratic sum `Σ q_j^{-2θ}` diverges by a power if `θ<1/3`; the moment mechanism no longer gives an `x^ε` margin.
- **It does not contradict R163_102 Thm T.** This system's prime measure is not a convergent modification of ζ's to the right of `1/2`; the extended source and the Witt factorization are global.
- **It does not contradict the Epstein falsifier.** Here there is a genuine discrete Euler product, built from integer multiplicities. Unlike Epstein of class greater than 1, the system has no known functional equation.
- **Hypotheses for the panel to audit:** Witt positivity, locally uniform analytic convergence, the conditioned Taylor inequality, the bound on the two sums at the endpoint, and passing from moments to an almost-sure bound.

**Conclusion:** `C_{1/3}` is proved with `+ε` (and at the endpoint `θ=1/3` in that same sense). The goal of closing D requires another mechanism: one that uses ζ's exact arithmetic and does not extend to these discrete systems.
