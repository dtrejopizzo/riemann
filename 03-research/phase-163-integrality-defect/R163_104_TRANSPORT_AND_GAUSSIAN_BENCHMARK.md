# R163_104 — Prime transport and the Gaussian arithmetic benchmark

**Status:** transport theorem proved; `Q(i)` benchmark obtained from cited classical results. Neither closes Row D. They serve to decide what class of mechanism could do so.

## 1. Transfer by transport, even when infinitely many primes are deleted

Let `P={p_j}` and `Q={q_j}` be two discrete multisets of Beurling primes, paired up to finitely many elements. Suppose that for some `σ₀≥0`

```
T_{σ₀}(P,Q):=Σ_j |log(q_j/p_j)| min(p_j,q_j)^{-σ₀}<∞.
```

**Transport theorem.** The quotient of Euler products `ζ_Q/ζ_P` extends as a holomorphic function with no zeros or poles in `Re s>σ₀` (except for the interpretation of the finitely many factors, which are also holomorphic and non-vanishing for `Re s>0`). In particular, if `P` is the ordinary system and `N_Q(x)=ρx+O(x^θ)`, the zeros of `ζ_Q` and of `ζ` coincide, with multiplicity, on `Re s>max(σ₀,θ,0)`.

*Proof.* For `Re s>1`, pair the factors and write

```
log(ζ_Q/ζ_P)=Σ_j [−log(1−q_j^{-s})+log(1−p_j^{-s})]+finitely many.
```

On any compact `K⊂{Re s>σ₀}`, take `σ₁>σ₀` smaller than its real parts. For `t` large enough, the derivative with respect to `log t` of `−log(1−t^{-s})` has modulus at most `2 sup_K|s| t^{-σ₁}`. The mean value theorem along the segment between `log p_j` and `log q_j` bounds the summand by

```
C_K |log(q_j/p_j)| min(p_j,q_j)^{-σ₁}
≤ C_K |log(q_j/p_j)| min(p_j,q_j)^{-σ₀}.
```

The series converges normally, defines a holomorphic function `H`, and the quotient is `exp H` by analytic uniqueness. The finitely many prime factors have no zeros or poles for `Re s>0`. If `ζ_Q` has the meromorphic continuation given by the error `O(x^θ)`, the identity extends to the intersection of the half-planes and transfers the zeros. ∎

This criterion improves on `R163_102` Thm T when the deleted and added parts are both large but **closely paired**. For instance, the pairing `q_p=p+O(1)` satisfies `T_σ<∞` for every `σ>0`, even though literally deleting all ordinary primes would have abscissa `σ_τ=1`. This does not claim that such a concrete system has integer error `O(x^θ)`; if it does, the transfer applies.

**Falsifiable necessary condition.** If a discrete θ-regular system has a zero at `β+iγ`, `β>max(θ,0)`, that ζ does not have, then **no** pairing of its primes with the ordinary ones can have `T_σ<∞` for any `σ<β`. Whatever arithmetic mechanism is eventually found will have to control precisely this failure of transport; merely knowing `N=ρx+O(x^θ)` does not control it with current results.

## 2. The value 1/3 does not isolate ζ: `Q(i)` already enters below it

The non-zero ideals of `Z[i]`, counted by norm, form a discrete Beurling system: its primes are the prime ideals, each with integer multiplicity, and its zeta is

```
ζ_{Q(i)}(s)=ζ(s)L(s,χ_{−4}).
```

Since `Z[i]` is principal and has four units, its generalized integer-counting function is

```
N_{Q(i)}(x)=¼ #{(a,b)∈Z²: 0<a²+b²≤x}.
```

Huxley's result on the circle problem, [*Exponential sums and lattice points III*](https://doi.org/10.1112/S0024611503014485), gives, for some fixed logarithmic exponent `C`,

```
N_{Q(i)}(x)= (π/4)x+O(x^{131/416}(log x)^C).
```

Since `131/416≈0.3149<1/3`, this system satisfies `N=ρx+O(x^θ)` for any `131/416<θ<1/3`. Hence a universal theorem `BF_θ^disc` with threshold `θ₀=1/3` would not only give RH for ζ: it would also prove that `L(s,χ_{−4})` has no zeros to the right of `1/2`, i.e. its GRH via the functional equation. This point does not refute the target, but it shows that it is **stronger** than its formulation as an individual route to D suggests. Paper 48's phrase "quadratic Dedekind zetas have exponent 1/3" is valid as a generic bound, not as the best exponent for `Q(i)`.

## 3. Strategic consequence

`R163_103` builds discrete countermodels with error `x^{θ+ε}` for every `θ>1/3`. The Gaussian family shows that even the region `θ<1/3` contains arithmetic distinct from ζ and additional GRH problems. So, to close **only** Row D, it seems more economical to look for a law of *oriented exact lattice* (`N_ζ=⌊x⌋` together with exact `Λ` and Poisson–Tate) than to first attempt a universal theorem for all θ-regular discrete systems. This is a design priority, not a proof.
