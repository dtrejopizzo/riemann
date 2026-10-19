# R163_116 — No gap for the effective exchange with variable displacements

**Status:** theorem proved under `R163_115`'s effective density bound; it does not prove the current has a gap and **does not close Row D**. Replaces `R163_115`'s hypothetical no-gap target with a proved lemma. The remaining arithmetic gate is producing the gap from ζ's exact lattice and `(PC-ren)`.

## Theorem

For each effective off-line quartet write `1/2±δ_j±iγ_j`, with `0<δ_j<1/2`, `γ_j>0` and multiplicities. Let `q_E` be the distributional current of `R163_001`'s canonical exchange. Then, for every `a>0`,

```
q_E|(0,a)=0   ==>   there are no off-line quartets.
```

It matters that the `δ_j` are **not** assumed equal. By contraposition, if at least one quartet exists, the current `q_E` has support accumulating at `u=0+`; in particular, it cannot start only at `log 2`.

### 1. Stripping the universal factor without losing the contact

Define the even function

```
B_δ(u)=2[cosh(δu)−1]/(δ²u²),    B_δ(0)=1,
```

and the even distribution

```
r(u)=Σ_j δ_j² B_{δ_j}(u) cos(γ_j u).                    (1)
```

The series converges in `D'(ℝ)`: for a compactly supported test, two integrations by parts give `O_φ(δ_j²/γ_j²)` uniformly in `δ_j≤1/2`, and `Σ_j γ_j^{-2}<∞` by `N_ζ(T)=O(T log T)`. On `u>0` one has exactly

```
q_E(u)=2e^{u/2}u r(u).                                  (2)
```

So, if `q_E=0` on `(0,a)`, then `r=0` on `(-a,0)∪(0,a)`. It remains to rule out a distribution concentrated at `u=0`.

The mass of the positive measure `ν₂=(1/2)Σ_j δ_j²(δ_{γ_j}+δ_{−γ_j})` satisfies `ν₂([-T,T])=o(T)` by `R163_115`. For a real test `ψ_h(u)=ψ(u/h)` and `h→0+`, series (1) gives

```
⟨r,ψ_h⟩ = h Σ_j δ_j² Re ψ̂(hγ_j) + o(1) = o(1).        (3)
```

Here `B_δ(hu)=1+O(h²u²)` with all the relevant derivatives uniform in `δ≤1/2` on `ψ`'s fixed support; after integrating by parts, its contribution is `O_N(h³ Σ_j δ_j²(1+hγ_j)^{-N})=o(1)`. The main sum is `o(1)` by the sublinear mass and the rapid decay of `ψ̂`. If `r` were supported on `{0}` within `(-a,a)`, it would be a finite combination of `δ_0` and its derivatives; (3), for every `ψ`, forces all coefficients to be zero. Thus,

```
r|(-a,a)=0.                                              (4)
```

### 2. A positive test stable against every `B_δ`

Choose `0<b<min(a,1/10)` and the compactly supported even function

```
f_b(u)=[exp(−|u|/b)−exp(−1)]_+,
```

supported on `[-b,b]`. For `0≤δ≤1/2`, set `g_δ(u)=f_b(u)B_δ(u)`. On `0<u<b`, `B_δ`'s Taylor series gives the uniform bounds

```
B_δ(u)≥1,       0≤B_δ'(u)≤u,       0≤B_δ''(u)≤1.          (5)
```

Differentiating `g_δ` on `(0,b)` and using `b≤1/10`, one gets

```
g_δ'(u)<0,      g_δ''(u)>0,      g_δ(b)=0.                (6)
```

For example, `g_δ'≤e^{-u/b}(−1/b+b)<0` and
`g_δ''≥e^{-u/b}(1/b²−2)>0`; the term `f_b B_δ''` is non-negative.

Strict convexity provides a **positive** Fourier formula. For `γ≠0`, with the convention `ĝ(γ)=∫_ℝg(u)e^{-iγu}du`, representing the convex function `g_δ` as a positive mixture of triangles gives

```
ĝ_δ(γ) = (2/γ²) [−g_δ'(b)(1−cos(bγ))
                     + ∫₀ᵇ g_δ''(t)(1−cos(tγ))dt] > 0. (7)
```

The inequality is strict because `g_δ''(t)>0` on an interval. For `γ=0`, also `ĝ_δ(0)>0`, since `g_δ` is non-negative and non-zero. Moreover `ĝ_δ(γ)=O_b((1+γ²)^{-1})`, uniformly in `δ≤1/2`.

### 3. Contradiction by positivity

From (4), `⟨r,f_b⟩=0`. The test `f_b` is continuous and has bounded-variation derivative, though it is not `C∞`; the pairing is justified by approximating it with smooth convolutions still supported inside `(-a,a)`. The transforms of `f_b B_δ` and those approximants are `O_b((1+γ²)^{-1})` uniformly; the series `Σ_j δ_j²/(1+γ_j²)` converges, so one may pass to the limit term by term. By (1) and (7),

```
0=⟨r,f_b⟩=Σ_j δ_j² ĝ_{δ_j}(γ_j).                       (8)
```

Each summand is strictly positive. Hence no quartet exists. □

## Scope and adversarial tests

- The periodic model `R163_108` does **not** contradict the theorem: its weighted mass grows linearly, so `r` can indeed have a contact term at `u=0`; the stripped current is a Dirac comb. Step (3) is exactly where it gets excluded.
- Epstein and Davenport–Heilbronn lack ζ's ordinary Euler product, and Beurling–DMV lacks the exact integer lattice. The spectral lemma, by itself, **does not distinguish** these three falsifiers: the bound `M₂(T)=o(T)` has been proved here for ζ's effective zeros, not for their spectra, and even under that bound one only gets an implication *from* a gap. So a future arithmetic derivation of the gap must fail on these examples precisely when it uses Euler or integrality.
- The argument uses ζ's zero-density bound to remove the contact term and the positivity of the quartets' multiplicities for (8). It does **not** obtain `q_E=0` on `(0,log 2)` from the integrality of `N_ζ(x)=⌊x⌋` or from the Euler product. That implication is this route's one remaining new gate. Nor is it enough to presuppose that `ζ/E` is positive Beurling: for non-trivial exchanges that positivity is not granted.
- The theorem is a conditional spectral restriction improving `R163_115`; it is not a disguised proof of RH. The gap hypothesis has not been established for the effective current.

**Next, falsifiable goal:** derive from `(PC-ren)`, Poisson–Tate and the exact values `Λ(p^k)/log(p^k)=1/k` that the effective current `q_E` has no support on `(0,log2)`. If that gap is obtained, the theorem above does conclude `E=1`, without assuming any Euler decomposition of `E` nor global arithmetic support.
