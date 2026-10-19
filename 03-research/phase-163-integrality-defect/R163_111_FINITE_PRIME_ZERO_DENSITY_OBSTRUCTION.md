# R163_111 — Zero density against Euler quotients of finitely many primes

**Status:** theorem proved under the explicit hypothesis of periodic meromorphic factorization over a finite set of primes; rationality of the factors is not required. Extends `R163_109`: it does not use the verification of low zeros. **Does not close Row D**, because ζ's exchange may involve infinitely many primes and it has not been proved to have such a factorization.

## No-finite-factorization theorem

Let `S` be a finite set of distinct primes and

```
E(s)=∏_{p∈S} F_p(s),                                   (1)
```

where each `F_p` is meromorphic, not identically zero, and periodic with imaginary period `2πi/log p`; in particular it may be `R_p(p^{-s})` with `R_p` meromorphic on `ℂ*`, not necessarily rational. Suppose `E` has a zero at `s₀=β+iγ` with `1/2<β<1`. Then, for that same `β`, except for finitely many cancellations,

```
# {zeros of E on Re s=β, 0<Im s≤T} ≥ (log p)/(2π) T−O(1)   (2)
```

for at least one `p∈S` (zeros counted with multiplicity). In particular, if **all** zeros of `E` in `1/2<Re s<1` belong to ζ's divisor, (1) is impossible: Ingham's density estimate gives, for every `β>1/2`,

```
N_ζ(β,T) ≪_β T^{3(1−β)/(2−β)}(log T)^5 = o(T).       (3)
```

So no non-trivial canonical exchange `E=∏E_{δ_j,γ_j}` built from **effective** off-line quartets of ζ can be a meromorphic Euler product supported on a finite set of primes, if each factor keeps the indicated local period. The arithmetic datum used is the exact multiplicative independence of the primes; the spectral datum is (3).

## Proof

Since `E(s₀)=0`, some factor `F_p` has a zero at `s₀`. By periodicity, that factor has the same zero throughout the progression of imaginary period

```
T_p=2π/log p.
```

That is, `F_p` vanishes at every point `s₀+ikT_p`, `k∈ℤ`. A different factor `F_q` could only cancel that zero where it has a pole. On `Re s=β`, each `F_q` has **finitely many** poles modulo its period `T_q=2π/log q`: a closed fundamental segment is compact and a meromorphic function cannot accumulate poles there. Each generates a progression. Two progressions of periods `T_p` and `T_q` meet **at most once**: two intersections would give `mT_p=nT_q` with non-zero integers, hence `log p/log q∈ℚ`, contrary to unique factorization (`p^m=q^n`). So each `q≠p` cancels only finitely many points of `p`'s progression; the union over `S` remains finite. This gives (2).

If the remaining zeros are zeros of ζ, (2) forces `N_ζ(β,T)≫T`. For `β>1/2`, the exponent in (3) is strictly less than 1, a contradiction. Formula (3) is the classical Ingham bound, recorded with its precise scope in [Chourasiya–Simonič, *An explicit form of Ingham's zero density estimate*](https://arxiv.org/abs/2507.15184). □

## Limit and the infinite gate

This result is stronger than `R163_109`'s first-height obstruction: even if the verified region were completely ignored, a finite product of **periodic meromorphic** local factors cannot have its off-line zeros among those of ζ. It also does not require `ζ/E` to be positive.

But it is not a proof of RH. (1) does **not** follow from `R163_001`'s canonical zero product, and ζ's exact arithmetic does not say that `E` is supported on finitely many primes either. With infinitely many local factors, a single prime's zero progression can suffer infinitely many cancellations coming from other primes; the proof above no longer gives an `O(1)` bound for them.

An `o(T)` bound on cancellations in an infinite factorization would let this contradiction repeat. But `R163_113` spells out the logical cost: if the factorization includes an ordinary Euler series absolutely convergent in **some** right half-plane, **Hamburger already closes D** before using the cancellation bound. So this should not be presented as a weaker intermediate gate; it only describes an alternative route if a meromorphic decomposition is found that does not reach `R163_113`'s hypotheses. Neither that decomposition nor the bound follows from `exp_*(Λ/log)=1`.

**Audit against falsifiers.** `R163_108` has precisely a zero progression of linear density, so it does not satisfy the premise "its off-line zeros are zeros of ζ"; the theorem correctly separates it. The Epstein, Davenport–Heilbronn and Beurling–DMV systems likewise do not inherit the Ingham bound **for ζ's zeros**. Applying (3) to them would be the invalid leap. The result does not assert a universal density bound for every generalized zeta.

**Revised collision with the corpus.** `P121_ACTIVE_EULER_IDEAL_OVERDENSITY` also uses periodic prime lattices, but on a different object: the zeros of a finite-type Cartwright transform, whose premise is tangency to local ideals. Here we count zeros of a **meromorphic exchange factor** and compare them with `N_ζ(β,T)=o(T)`; faithfulness of a first-contact witness is neither assumed nor deduced. The gate of deriving a faithful local structure remains open in both formulations.
