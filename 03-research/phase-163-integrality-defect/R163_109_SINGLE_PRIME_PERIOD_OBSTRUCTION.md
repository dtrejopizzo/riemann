# R163_109 — The verified strip excludes every single-prime periodic exchange

**Status:** elementary theorem proved; separates `R163_108`'s model from ζ's effective zeros. **Does not close Row D:** it does not exclude multi-prime or non-periodic currents.

## Theorem

Let `p≥2` be a prime and let `E(s)=R(p^{-s})`, with `R` a non-constant rational function. If `E` has a pole on `Re s=1/2`, it also has a pole at

```
Re s=1/2,       |Im s|≤π/log p≤π/log 2<4.54.             (1)
```

Hence **no** canonical exchange product `E=∏ E_{δ_j,γ_j}` built from a non-empty set of ζ's effective off-line quartets can be rational in `p^{-s}` for a single prime `p`. The same result holds for any meromorphic function of `p^{-s}` with a pole on the line, as long as its composition is meromorphically defined there.

**Atomic-current version.** More generally, suppose that for that exchange the current `q_E` is supported only on `k log p` and that its Laplace transform represents `log E(s)^{-1}` by a normally convergent series `Σ_{k≥1}c_k p^{-ks}` in some right half-plane. Then such an exchange is likewise impossible. The representation hypothesis does not follow merely from `R163_001`'s local distributional convergence; it is stated explicitly to avoid that leap.

## Proof

The function `p^{-s}` has imaginary period `2πi/log p`. Consequently, every pole of `R(p^{-s})` repeats exactly at `s+2πik/log p`, `k∈ℤ`. Translating any ordinate into the central interval of length `2π/log p` gives (1).

For the canonical product, each non-trivial quartet `δ_j>0` produces a pole of `E` at `s=1/2±iγ_j`. No numerator factor can cancel it on the line: all its zeros have real part `1/2±δ_j`, different from `1/2`. `R163_001`'s local normal convergence preserves that pole, with the total multiplicity of the quartets at equal height. The [rigorous Platt–Trudgian verification](https://arxiv.org/abs/2004.09765) establishes that there are no zeros **off the line** up to height `3·10^12`; even the most elementary datum of the first zero `γ_1>14.13`, imported in `(X19)` of paper 46, suffices. An exchange of off-line quartets cannot have a pole at height `≤4.54`, contradicting (1). □

For the atomic version, the series `Σ c_k p^{-ks}` has imaginary period `2πi/log p` where it converges. Exponentiating and applying the identity principle to the two meromorphic functions `E(s+2πi/log p)` and `E(s)` extends the periodicity to the whole plane. The same pole argument finishes the proof. □

## Scope for the arithmetic law

`R163_108` concentrates an infinite exchange's current at `k log 2`, but it pays exactly the price of (1): its first pole is at `π/log 2≈4.532`, too low to belong to ζ's divisor. This is not a numerical accident: **every single-prime, exact-period mechanism is excluded** by the known geometry of the low zeros.

The result jointly uses a single-prime multiplicative-support restriction and an effective spectral restriction. It does not prove that the current of ζ's real exchange has support outside the prime lattice, nor that it violates its capacity. In particular, an expression depending on several `p^{-s}` with incommensurable logarithms does not have that single period; the proof does not reach it. Nor does mere distributional support on powers of a single prime automatically give the global Laplace series: the extended version demands that representation, not just local support.

**Next non-circular gate:** treat multi-prime couplings, or prove that the current of an exchange of effective zeros cannot fit within the `1/k` capacity at each prime power, without first inferring the positivity of `ζ/E`.
