# R163_108 — An infinite exchange can land exactly on the prime lattice

**Status:** explicit model and capacity computation proved. **It is not an exchange of ζ's zeros and does not close Row D.** Its purpose is to falsify extrapolating the finite case's continuous-density argument.

## Theorem (cosh exchange)

Fix `0<δ<1/2`, `a=(log 2)/2`, `w=s−1/2` and

```
γ_n=(n+1/2)π/a=(2n+1)π/log 2,       n=0,1,2,... .
```

The canonical product of `R163_001`'s factors at those heights is

```
E_δ(s)=∏_{n≥0} E_{δ,γ_n}(s)
      =cosh(a(w+δ))cosh(a(w−δ))/cosh²(aw)
      =1+sinh²(aδ)/cosh²(aw).                              (1)
```

It converges normally away from its poles. It has zeros at `w=±δ±iγ_n` and double poles at `w=±iγ_n` — exactly the geometry of an infinite quartet exchange. Unlike a finite exchange, `E_δ(s)−1=O(2^{-s})` as `s→+∞` on the real axis: the cancellation of infinitely many factors produces an *exponential* tail, not an algebraic one.

Moreover, `R163_001`'s current `q_E` is **purely atomic on the powers of 2**. For `Re s` large enough,

```
log E_δ(s)^{-1}=Σ_{k≥1} c_k 2^{-ks},
c_k=[2(-1)^k/k] 2^{k/2}[cosh(kδ log 2)−1].              (2)
```

So `q_E=Σ_{k≥1}c_k δ_{k log 2}` in the sense of Laplace transforms and locally finite distributions. In particular, the argument "the exchange leaves a negative continuous density outside the prime atoms" **does not extend** to infinite products without an extra hypothesis on the heights.

## Proof

The Euler product for the hyperbolic cosine is

```
cosh(az)=∏_{n≥0}(1+z²/γ_n²).
```

Applying it to `z=w+δ`, `w−δ` and `w` gives (1), factor by factor; the last equality uses `cosh(x+y)cosh(x−y)=cosh²x+sinh²y`.

Set `t=exp(−2aw)=2^{1/2−s}` and `r=exp(2aδ)=2^δ`. From (1),

```
E_δ(s)=[(1+rt)(1+r^{-1}t)]/(1+t)².
```

Expanding `2log(1+t)−log(1+rt)−log(1+r^{-1}t)` gives (2). The series converges absolutely if `|rt|<1`. The identification with **the factor-by-factor distributional current** defined in `R163_001` is likewise direct: with `L=log 2`, Poisson summation gives, as distributions in `u>0`,

```
Σ_{n≥0} cos((2n+1)πu/L)
  =(L/2) Σ_{k≥1}(-1)^k δ_{kL}(u).
```

Multiplying by `4e^{u/2}(cosh(δu)−1)/u`, `q_j`'s prefactor, gives exactly the `c_k` of (2). So there is no informal exchange of an infinite sum with a non-compact Laplace integral.

## The capacity of the prime 2 still fails

In `log ζ`, the atom at `k log 2` weighs exactly `1/k`. If the formal quotient `ζ/E_δ` is formed, its prime measure at that point has weight

```
(1/k)+c_k
 = [1+2(-1)^k 2^{k/2}(cosh(kδ log 2)−1)]/k.       (3)
```

For every `δ>0`, (3) is negative for all sufficiently large odd `k`. Indeed, the second term is negative and its modulus grows like `2^{k(1/2+δ)}`. So the lattice of powers of 2 **does absorb the support** of the current, but **not its amplitude**: `ζ/E_δ` has no positive Beurling prime measure.

The negativity proof uses Euler's exact values `1/k`, not just the location of its atoms. This is an infinite case in which `R163_002`'s capacity condition can be checked completely and explicitly.

## Logical scope for O2601.1∞

The heights `γ_n` are artificial; in particular, they are not a subset of ζ's zeros. The model does **not** show that an exchange of ζ's real zeros can concentrate on the prime lattice, nor that (3) resolves RH. It shows the following, more limited but useful, fact:

1. The normal convergence of `E` and the quartet geometry allow for a current that is infinitely exchanged and purely atomic. So the finite case's smooth-density no-go does not prove the arithmetic vanishing property in the infinite case.
2. Even when the support lands exactly on prime powers, the weights `1/k` impose an independent restriction: capacity can fail by amplitude.
3. A law closing D must use ζ's **effective** heights and prove that its current does not fit within prime capacity, or else produce some other direct contradiction. Mere integer support, functional symmetry and the limit `E(s)→1` are not enough: (1) satisfies those formal features.

**Remaining gate:** prove a non-formal restriction for the exchange built from ζ's effective zeros. The positivity of `ζ/E` is not inferred here; even if it were ruled out, that alone would not exclude zeros off the line either.
