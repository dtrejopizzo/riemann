# R163_125 — Coercive margin between the two square channels

**Status:** spectral inequality proved for ζ's effective exchange; the opposite arithmetic return remains open. Does not close Row D. Improves `R163_124`: a PC-ren/Poisson–Tate bridge need not exactly annihilate the defect, only stay below an explicit relative margin.

## Theorem

With `b=1/2`, `T_b(u)=(b−|u|)_+`, `K₂=T_b²`, `K₃=T_b³` and `M_k=⟨r,K_k⟩` as in `R163_124`, if at least one effective off-line quartet exists, then `M₂>0` and

```
M₃ ≥ (b+0.24) M₂.                                   (1)
```

Consequently, it would **suffice** to prove from an independent arithmetic input a comparison

```
M₃ ≤ (b+η) M₂   for some η<0.24                  (2)
```

for the effective current: (1) and (2) would force `M₂=0`, and the strict positivity of each summand would imply there are no quartets. Comparison (2) is **not proved**. As in `R163_124`, any valid (2) for the effective current would be a formulation of RH strength, not an already-available intermediate result.

## Proof of the margin

`R163_117 (6)` first gives, uniformly for `0<δ<1/2` and `γ≥14`,

```
−\widehat{H_bB_δ}(γ) ≥ 2c_*/γ²,
c_*:=1/4−1/14−12/14²−7/384 > 0.099.              (3)
```

By `R163_124`, `H_b=bK₂−K₃`, and `g₂(u)=K₂(u)B_δ(u)` is even, decreasing and convex on `[0,b]`. We have `g₂'(0+)=-2b=-1`, `g₂'(b-)=0`, `g₂''≥0` and `∫₀ᵇg₂''=1`. Two integrations by parts give

```
0<\widehat{K₂B_δ}(γ)
  = (2/γ²)[1−∫₀ᵇ g₂''(u)cos(γu)du]
  ≤ 4/γ².                                             (4)
```

Combining (3) and (4), for each quartet,

```
\widehat{K₃B_δ}(γ)−b\widehat{K₂B_δ}(γ)
 =−\widehat{H_bB_δ}(γ)
 ≥(c_*/2)\widehat{K₂B_δ}(γ)
 >0.049\widehat{K₂B_δ}(γ).                          (5)
```

All the pairing series converge absolutely by `Σ_jδ_j²/γ_j²<∞`. Summing (5) gives the preliminary margin `0.049`. To prove the **stronger margin of (1)**, we use the actually verified height: every hypothetical effective quartet has `γ≥3·10¹²`.

On `0≤u≤b=1/2`, `B_δ`'s Taylor series allows the finer uniform bounds

```
0≤B_δ−1≤u²/40,   0≤B_δ'≤u/20,   0≤B_δ''≤1/20.    (6)
```

To audit the constants: `B_δ(u)=Σ_{n≥0}2(δu)^{2n}/(2n+2)!` and `δu≤1/4`. In `B−1`'s series, every term after the first has ratio at most `1/480`, and the first is `δ²u²/12≤u²/48`; so the sum is less than `u²/40`. For `B'`, the later ratios are at most `1/240` and the first term is `δ²u/6≤u/24`; for `B''`, they are at most `1/80` and the first is `δ²/6≤1/24`. The resulting geometric series give the other two bounds in (6).

For `H_b=u(b−u)²` on `u≥0`, two integrations by parts as in `R163_117` and (6) bound the perturbation `H_b(B_δ−1)` by `(2/γ²)(7b⁴/80)`. The unperturbed part satisfies (see `R163_117 (2)`)

```
−\widehat{H_bB_δ}(γ)
 ≥ (2/γ²)[b²−2b/γ−12/γ²−7b⁴/80].                (7)
```

For `K₂=(b−u)²` on `0≤u≤b`, the unperturbed transform is `(2/γ²)[2b−2sin(bγ)/γ]`. The remainder `K₂(B_δ−1)` has second derivative of `L¹(0,b)` norm at most `b³/15` by (6), since its three terms are bounded by `b³/60`, `b³/30` and `b³/60`. Hence

```
\widehat{K₂B_δ}(γ)
 ≤ (2/γ²)[2b+2/γ+b³/15].                          (8)
```

With `b=1/2` and `γ≥3·10¹²`, the ratio between (7)'s lower bracket and (8)'s upper one exceeds

```
[1/4−7/1280−2/γ−12/γ²] / [1+1/120+2/γ] > 0.24. (9)
```

So `−\widehat{H_bB_δ}(γ)>0.24\widehat{K₂B_δ}(γ)` term by term. Summing proves (1). The bound `γ≥3·10¹²` comes from the rigorous verification of ζ cited in `R163_117`; it is not a hypothesis about RH at unverified heights. □

## Reading the gate and falsifiers

- The `0.24` margin allows a **relative error** in the eventual return identity. A candidate formula might have polar/Tate corrections and exterior leakage not exactly zero; it would suffice to control them by `ηM₂` with `η<0.24` and the correct orientation. This is more flexible than requiring `M₃≤bM₂` exactly, though it remains of RH strength for ζ.
- The constant comes from the first gap `b<log2` and the verified absence of low-height quartets. It is not a law of the Beurling class: systems with low-height or differently-distributed exterior zeros do not automatically pass (3). The periodic model `R163_108` has heights starting below 14 and does not contradict it.
- Finite modifications of `Λ` that preserve ζ's zero set would pass the **spectral side** (1) just as ζ does; they must fail in the arithmetic derivation of (2). Epstein/DH lack an ordinary Euler product and Beurling–DMV lacks the exact integer lattice. This is the mandatory test for any future comparison.

**Residual:** build (2) from `(PC-ren)`/Poisson–Tate plus the Euler derivation `Λ*1=log`, without replacing it with a square of `(PC-ren)` or assuming positivity of the quotient `ζ/E`. The quantitative margin bounds the allowed error, but does not supply the signed identity.
