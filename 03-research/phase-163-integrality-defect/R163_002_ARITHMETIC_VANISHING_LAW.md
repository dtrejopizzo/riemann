# R163_002 — What arithmetic law could make the defect vanish

**Status:** a positive lemma and an obstruction are proved; a direct vanishing law is **open**.

## 1. The temptation of a positive factorization

If one had `ν_N=ν₀*κ` with `ν₀,κ` locally finite positive measures on `[0,∞)`, both with a unit-mass atom at `0`, then **both are supported on `log N`**. Indeed, each factor dominates `δ₀`, so `ν₀*κ≥ν₀` and `ν₀*κ≥κ`; outside `log N`, `ν_N` is zero. This is a support-rigidity lemma, not a proof that the factorization is trivial: even on the lattice there exist non-trivial positive factorizations of the integer series.

Applying it to `ζ=(ζ/E)E` would require both the quotient and the factor to be transforms of positive measures. ζ's arithmetic supplies no such hypothesis. For a non-trivial finite exchange, setting `w=σ−1/2`,

```
E(σ) = 1 − 2(Σ_j δ_j²)/w² + O(w^{-4}) < 1    (σ→+∞).
```

A Laplace transform of a positive measure with unit mass at zero is always at least 1 for real `σ`; hence `E` cannot be that second factor. For the strict finite quotient, `R162_2901` Theorem A already proves directly that `dΠ_{ζ/E}` has a negative continuous part. The positive Beurling hypothesis does not reach from there either.

## 2. A countermodel isolating the missing condition

Fix `0<c<1` and define

```
K(s)=1−c/(s+1)=(s+1−c)/(s+1),
Z₀(s)=ζ(s)/K(s)=ζ(s)(s+1)/(s+1−c).
```

By Frullani,

```
log[(s+1)/(s+1−c)]
  = ∫₀^∞ e^{-su}[e^{-(1−c)u}−e^{-u}] du/u.
```

The density is non-negative. So `Z₀` has a positive measure of generalized primes: ζ's ordinary atoms plus this density. `ζ=Z₀K` still has exact integer coefficients equal to 1 and its ordinary Euler product, but `K` is not trivial. The example **does not** have the functional equation and is not a canonical zero exchange; it only invalidates the general inference "exact integer + Euler + positive Beurling quotient ⇒ trivial factor."

## 3. Prime-lattice capacity: correct formulation, still insufficient

If, as an extra hypothesis, `dΠ_{ζ/E}=dΠ_ζ+q_E≥0` were a measure, `q_E`'s negative part would have to be absorbed by ζ's exact atoms. In signed-measure language:

```
q_E^- ≤ Σ_{p,k≥1} (1/k) δ_{k log p}.       (capacity)
```

This formulation assumes `q_E` is a signed measure with a Jordan decomposition; for a general distribution of infinitely many quartets that regularity still needs to be proved. In the finite case `q_E` is a smooth density that changes sign, so it cannot be absorbed by atoms: this recovers the phenomenon of `R162_2901` Theorem A. In the infinite case, proving a law of "no compensation by the prime lattice" would be significant, but it would only exclude **positivity of the quotient**. It would not prove `E=1`, because that positivity is not given and already fails in the hypothetical finite exchange.

The explicit model `R163_108` shows why the infinite caveat is essential: a product of infinitely many quartets can have `q_E` **purely atomic at `k log 2`**. In that model, capacity fails because of the weights, not the support; its heights are artificial and are not zeros of ζ.

## 4. A non-circular mathematical target

The needed law must act **directly** on the coexistence of:

1. the exact ledger `b(n)≡1` of `ζ=exp_*(Λ/log)`;
2. `Λ` supported on prime powers with its exact values;
3. the functional equation/Poisson–Tate orientation;
4. the global structure of the symmetric exchange `E`, without assuming `ζ/E` is positive.

It must deduce `E≡1` or a strictly weaker restriction that, together with an independent theorem, implies that. In particular, it is not enough to postulate `D_test(E)=0`, a bound equivalent to that vanishing, nor to turn the absence of compensation into "the quotient is positive Beurling": that reintroduces the obstacle as a hypothesis.

A concrete, falsifiable subquestion is to classify, in a defined distributional topology, whether `q_E` for an infinite exchange can have its negative part concentrated exclusively at `log(p^k)` with masses no larger than `1/k`. That classification would attack *capacity*; an independent bridge from ζ's arithmetic to a statement forcing its use would then have to be supplied. The mere integer support of `ν_N` is not that bridge.

**Conclusion:** property 2 of the O2601.1∞ proposal is not developed as a theorem. This phase's new result is an honest reduction of its hidden hypotheses and a precise formulation of the remaining work; Row D remains open.
