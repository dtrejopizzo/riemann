# R163_112 — Local capacity theorem: an interior zero forces huge negative weights

**Status:** algebraic theorem proved for rational local factors. Generalizes `R163_108`'s computation; it assumes neither RH nor the positivity of `ζ/E`. **Does not close Row D**, because it has not been proved that the effective exchange decomposes into such local factors, nor that `ζ/E` must be positive.

## Theorem

Fix a prime `p` and a rational function `R(z)` with real coefficients, `R(0)=1`, written with no cancellations. Suppose its smallest-modulus singularities are at distance `r<1`, are **zeros** (not poles), and none lies at the positive real point `z=r`. Write

```
log R(p^{-s})^{-1}=Σ_{k≥1} c_k p^{-ks}                  (1)
```

in the half-plane of convergence. Then there exist `ε>0` and an infinite sequence `k_j→∞` such that

```
k_j c_{k_j} ≤ −ε r^{-k_j}.                              (2)
```

In particular, `c_{k_j}<−1/k_j` for all large `j`. If `q_E` contains this factor as a current **separated at the prime p**, the coefficient of `log(ζ/E)` at `p^{k_j}` is `1/k_j+c_{k_j}<0`: the factor does not fit within ζ's exact Euler capacity.

The case relevant to a local exchange has an interior zero `r=p^{-β}` with `β>1/2` and poles on the critical circle `|z|=p^{-1/2}`. The hypothesis "no zero at `z=r>0`" avoids a real zero at `s=β`, absent from ζ's non-trivial divisor.

## Proof

Let `α_j=r e^{iθ_j}`, with multiplicity, be the minimal-modulus zeros, and let `r_2>r` be the next modulus of a zero or pole; if there is none, the remainder is omitted. Expanding the logarithms of linear factors gives exactly

```
k c_k = r^{-k} A_k + O(r_2^{-k}),
A_k=Σ_j e^{-ikθ_j}.                                    (3)
```

Since `R` has real coefficients, `A_k` is real. No `θ_j` is `0` mod `2π`; by orthogonality of the exponentials,

```
lim_{K→∞} K^{-1}Σ_{k≤K} A_k=0,
lim_{K→∞} K^{-1}Σ_{k≤K} A_k²>0.                        (4)
```

In the second average, repeated angles are grouped: the limit is the sum of the squares of their multiplicities (equivalently the average of `|A_k|²`), strictly positive. Also `A_k` is uniformly bounded. The two relations in (4) force `A_k≤−2ε` for infinitely many `k`: if for every `ε>0` this happened only finitely often, the average of the negative part would tend to zero; the zero mean would then force the same for the positive part, and the average of `A_k²` would also tend to zero, a contradiction. On that subsequence, the remainder of (3) is `o(r^{-k})`, which gives (2). Since `r<1`, finally `εr^{-k}>1`. □

## What it uses and what it does not

- **Zero geometry** enters through the minimal radius `r` and the absence of a positive real zero.
- **Exact arithmetic** enters in the final comparison with the weight `1/k` of `log ζ`'s atom at `p^k`; merely knowing an atom exists is not enough.
- **Prime independence** does not enter this local computation; it would serve to prevent other primes from compensating the same atom once a faithful decomposition into fibers has been proved.
- The theorem proves the local quotient `ζ/E` lacks positivity, **not** the non-existence of the zeros. That quotient's positivity does not follow from `ζ=exp_*(Λ/log)` and already failed for finite exchanges in `R162_2901`.

## Adversarial audit

`R163_108` satisfies the theorem's hypotheses: its interior zeros are at non-zero angles, and (2) explains, without using `cosh`'s closed formula, why arbitrarily large negative weights appear. The mechanism does not apply to Epstein or Davenport–Heilbronn because they lack the required local Euler quotient. Beurling–DMV does have a generalized Euler product, but its prime weights and lattice need not be the ordinary primes' `1/k`; applying the final comparison to them would be incorrect.

**Logical limit:** deriving a faithful local decomposition from Poisson–Tate would be the substantial step. If it produces an ordinary Euler series for `log E^{-1}` absolutely convergent in **some** right half-plane, `R163_113` shows Hamburger already closes D, without using this capacity theorem. If it does not produce such a series, an independent implication turning the local sign into the non-existence of zeros is still missing. Neither outcome is postulated here.
