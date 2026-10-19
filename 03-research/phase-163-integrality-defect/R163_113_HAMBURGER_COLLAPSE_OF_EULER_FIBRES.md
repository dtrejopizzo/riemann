# R163_113 — Collapse of the ordinary Euler factorization to Hamburger

**Status:** conditional reduction proved with Hamburger's original formulation verified in [Bombieri–Ghosh, §1.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=9410&what=fullteng): the two Dirichlet series need only converge for `Re s` large enough. Audits `R163_109`–`R163_112`. **Does not close Row D**, because ordinary Euler support for the effective exchange is still unproved.

## Collapse theorem

Let `E` be the canonical product of `R163_001` formed by **all** of ζ's effective off-line quartets, with multiplicities, and let `F=ζ/E`. Suppose that in some right half-plane

```
log E(s)^{-1}=Σ_{p prime}Σ_{k≥1}c_{p,k}p^{-ks}          (1)
```

with absolute convergence in a half-plane `Re s>σ_a` for some `σ_a<∞` and the logarithm normalized by `log E(s)→0` as `s→+∞`. Then `E≡1`; hence there are no off-line quartets.

The same conclusion holds if `F` is assumed directly to be an ordinary Dirichlet series convergent for `Re s` large enough, with the analytic hypotheses indicated below. An abscissa of convergence `≤1` is not required.

## Proof and hypothesis control

1. On `Re s>max(1,σ_a)`, `log ζ(s)=Σ_{p,k}p^{-ks}/k` converges absolutely. By (1),

   ```
   log F(s)=Σ_{p,k}(1/k+c_{p,k})p^{-ks}.
   ```

   Exponentiating an absolutely convergent series supported on `log ℕ` produces an ordinary Dirichlet series for `F`, absolutely convergent in some right half-plane; the coefficients may be complex and their positivity is not assumed.

2. `E(1−s)=E(s)`, so `F` satisfies the same completed conductor-1 functional equation as ζ. By construction, `E`'s zeros are ζ's off-line zeros with exact multiplicity; they cancel in `F`. `E`'s poles on the line introduce zeros of `F`, not poles. At most ζ's ordinary pole at `s=1` remains.

3. `E`'s factors form quotients of finite-order canonical products, because the classical zero count is `O(T log T)`. After the cancellations, `(s−1)F` is entire of finite order. So the hypotheses of [Hamburger's original formulation as described by Bombieri–Ghosh](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=9410&what=fullteng) are satisfied: two ordinary series convergent for large `Re s`, a finite-order meromorphic function with finitely many poles, and a Riemann functional equation. Here the two series are `F` itself; its first coefficient equals 1 by the normalization. Hence `F=ζ` (or `F=cζ` if that normalization is dropped).

4. The normalization fixes `c=1`: as `w=s−1/2→+∞`, each factor satisfies `|E_j(s)−1|≪(w²+γ_j²)^{-1}`, and the count `N(T)=O(T log T)` gives

   ```
   Σ_j (w²+γ_j²)^{-1}=O((log w)/w)→0.
   ```

   So `E(s)→1` and `F(s)/ζ(s)→1`. Hence `E≡1`. □

## Consequence for phase 163's strategy

The full factorization (1), for **any finite abscissa of absolute convergence**, is not a weakened intermediate step: together with symmetry and zero cancellation it already closes RH via a known rigidity. No bound on cancellations between primes from `R163_111`, nor the weight comparison of `R163_112`, would be needed after proving (1). The restriction `σ_a≤1` that appeared in an earlier version of this note was unnecessary; the Bombieri–Ghosh reference removes it.

Theorems `R163_108`–`R163_112` keep their value as **adversarial tests and subclass obstructions**:

- `R163_108` shows an artificial infinite exchange can have its current on the prime lattice; since its zeros are not zeros of ζ, `F=ζ/E` keeps new poles and does not satisfy Hamburger's hypothesis.
- `R163_111` excludes finite-prime local factorizations of an effective exchange via zero density, without requiring global (1); however, turning it into a closure of D would first require justifying a faithful factorization of the exchange, which (if it implies (1)) already resolves D by this note.
- `R163_112` measures the `1/k` Euler capacity of local factors; that capacity failing only proves the lack of positivity of `ζ/E`, not the non-existence of its zeros.

**Target that does not re-derive Hamburger:** look for a Poisson–Tate/first-contact identity that directly forces a sign or an arithmetic vanishing **before** postulating an ordinary Euler current for `E`. If the derivation ends up postulating (1), all the substantial work lies in proving the ordinary support and a global Laplace/Dirichlet representation with some finite abscissa, not in the later local consequences. Row D's gate remains open.

**Later improvement `R163_114`.** For the specific (factor-by-factor) current of the effective exchange, it is enough that its distributional support be contained in `log ℕ_{≥2}`: the count `N_ζ(T)=O(TlogT)` automatically excludes delta derivatives, bounds its masses by `O(n²)` and justifies the global Laplace representation. Support need not lie only on prime powers, nor is a finite abscissa needed as a separate postulate. The proof of integer support remains open and, by `R163_114`'s equivalence, carries the full strength of RH.
