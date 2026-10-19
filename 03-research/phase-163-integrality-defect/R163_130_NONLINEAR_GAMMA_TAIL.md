# R163_130 — The first Gamma tail survives exponentiation

**Status:** non-linear stability lemma for `R163_127`'s lift. Proved under its hypotheses. It does not supply the missing physical orientation nor close Row D.

## Statement

Let `0≠F∈ker H_T` be real, primitive, of parity `ε`, and define `b=−ε h_A` as in `R163_128`. Let `m₀≥1` be the first index with `K_{m₀}(F)≠0`, which exists by completeness of the Gamma moments, and `s₀=2m₀+1`. Then, as `k→+∞`,

```
 b̂(k) = c₀ k^(−s₀)+O_F,T(k^(−s₀−2)),
 c₀=K_{m₀}(F)²/ζ(s₀)>0,                         (1)

 (e^b)^∧(k) = c₀ k^(−s₀)+o_F,T(k^(−s₀))>0
                                      for k large enough. (2)
```

In particular, the non-linear test `e^b` has a **strictly positive** Fourier tail, and does not become constant or lose the Gamma residues upon exponentiation. Since `b(0)=∫b=0` at contact and Jensen gives `∫e^b>1`,

```
 Σ_{k≥1}(e^b)^∧(k)=[1−∫e^b]/2<0.             (3)
```

By (2) and (3), there is an integer `K₀(F,T)` such that for every `K≥K₀`,

```
 Σ_{1≤k≤K}(e^b)^∧(k)<0;                      (4)
```

some low coefficient is negative. Unlike `R163_128`, the threshold is not explicitly `e^(4T)` because exponentiation mixes low and high frequencies.

## Convolution lemma used

Let `a=(a_k)_{k∈ℤ}` be a real, even, absolutely summable sequence with `a_k=c|k|^(−s)+o(|k|^(−s))`, `c≠0`, `s>1`, and `|a_k|≤C(1+|k|)^(−s)` for all `k`. If `f(θ)=Σ a_k e^{2πikθ}`, then

```
 (e^f)^∧(k)=e^{f(0)}a_k+o(|k|^(−s)).          (5)
```

To see this, split the convolution `(a*d)_k` into `|j|≤R`, `|k−j|≤R` and the remainder. Letting `k→∞` and then `R→∞`, the two extreme parts give `a_kΣd_j` and `d_kΣa_j` respectively; the remainder is `o(k^(−s))` because `s>1`. By induction, `(a^{*n})_k=n f(0)^{n−1}a_k+o(k^(−s))` for each `n≥1`. The weighted-convolution bound `|(a^{*n})_k|≤n C_s^n ||a||_s^n(1+|k|)^(−s)` (with a constant `C_s` depending only on `s`) allows summing the exponential series term by term via dominated convergence, giving (5). The `n=0` term does not contribute when `k≠0`.

## Application and scope

`R163_127 (4a)`'s exact formula gives (1): the next non-zero index contributes at least two extra powers, and the remaining series is uniformly summable for `k>e^(4T)`. At contact, `b(0)=0`, so (5) gives (2) with factor `e^{b(0)}=1`. The absolute sum of `e^b`'s coefficients follows from the Wiener-algebra property, hence (3). Finally, (2)'s tail is positive and its sum tends to zero, so the prefix in (4) converges to the negative number in (3).

**Gate still open:** neither (2) nor (4) is a Poisson–Tate sign. The `Φ_Λ` cocycle applied to `e^b` remains tautological for any test; `R163_129` shows it does not orient Weil. The concrete improvement is that an eventual **non-linear** physical pairing cannot claim exponentiation erased the Gamma tail: its first asymptotic coefficient remains exactly `K_{m₀}(F)²/ζ(2m₀+1)`.
