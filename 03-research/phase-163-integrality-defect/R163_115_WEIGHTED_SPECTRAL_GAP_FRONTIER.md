# R163_115 — Sublinear weighted spectral mass and a gap for fixed displacement

**Status:** two lemmas proved. The extension to variable displacements, open when this note was written, was **later proved in `R163_116`**. Does not close Row D: the effective current still has not been shown to have the required gap.

## 1. Weighted mass of the effective quartets

For each off-line quartet, write its zeros as `1/2±δ_j±iγ_j`, `0<δ_j<1/2`, counting multiplicity. Then

```
M₂(T):=Σ_{0<γ_j≤T}δ_j²
      ≪ T (log log T)²/log T = o(T).                   (1)
```

**Proof.** The [uniform explicit estimate of Chourasiya–Simonič, Corollary 1](https://arxiv.org/abs/2507.15184) gives, for `1/2≤σ≤5/8` and `T` large enough,

```
N_ζ(σ,T) ≪ T^{3(1−σ)/(2−σ)}(log T)^3+(log T)^2.
```

Take `ε_T=10(log log T)/log T`, which eventually lies in `(0,1/8)`. Split `δ_j≤ε_T` and `δ_j>ε_T`. The first part of `M₂` is bounded by `ε_T² N_ζ(T)≪T(log log T)²/log T`. For the second, `δ_j²≤1/4` and

```
N_ζ(1/2+ε_T,T)
 ≪ T^{1−2ε_T/(3/2−ε_T)}(log T)^3+(log T)^2
 ≪ T/(log T)^{31/3}+(log T)^2.
```

This proves (1). The estimate's **uniformity** in `σ` is used because `ε_T→0`; a bound with a constant depending arbitrarily on `σ` would not justify the step. □

## 2. No-gap lemma for sublinear-mass positive measures

Let `ν` be a symmetric positive measure on `ℝ`, of at most polynomial growth, with `ν([-T,T])=o(T)`. If its Fourier transform `ν̂` vanishes as a distribution on `(-a,0)∪(0,a)` for some `a>0`, then `ν=0`.

**Proof.** On `(-a,a)`, `ν̂` would be supported only at `0`, so it would be a finite combination of `δ_0` and its derivatives. But for a scaled test `ψ_h(u)=ψ(u/h)`,

```
|⟨ν̂,ψ_h⟩| ≤ h ∫|ψ̂(hγ)|dν(γ)=o(1)             (h→0+).
```

The last relation is obtained by splitting `|γ|≤C/h` and the tails, using `ν([-T,T])=o(T)` and the rapid decay of `ψ̂`. No non-zero combination of `δ_0` and its derivatives can have all those evaluations `o(1)`. So `ν̂=0` on all of `(-a,a)`.

Take `φ∈C_c^∞(-a/2,a/2)` and `f=φ*\tilde φ`, with `\tilde φ(u)=\overline{φ(-u)}`. Then `supp f⊂(-a,a)` and, by positivity of `ν`,

```
0=⟨ν̂,f⟩=∫|φ̂(γ)|²dν(γ).
```

If `ν≠0`, one can choose a `φ` whose transform does not vanish at a point of its support, giving a positive integral. Contradiction. □

## 3. Application: a single horizontal distance

Suppose, conditionally, that **all** of ζ's off-line quartets have the same distance `δ>0`. Then factor (1) in `R163_114` is common and

```
q_E(u)=A_δ(u) C(u),
C(u)=Σ_j cos(γ_j u),
A_δ(u)=4e^{u/2}[cosh(δu)−1]/u>0  (u>0).
```

The symmetric positive spectral measure `ν=(1/2)Σ_j(δ_{γ_j}+δ_{−γ_j})` has `ν([-T,T])=o(T)` by Ingham's density bound at the fixed point `1/2+δ`. If `q_E` vanished on any interval `(0,a)`, `C` would vanish there too; by parity, `ν̂` would vanish on the punctured gap `(-a,0)∪(0,a)`. The lemma above forces `ν=0`. So, under the fixed-distance hypothesis, **vanishing on the first arithmetic gap `(0,log 2)` alone already excludes every quartet**. There is no need to postulate support on all of `log ℕ`, nor to use Hamburger, in this special case.

## 4. The real frontier: variable distances

For the effective ζ, the `δ_j` can vary and tend to zero. Although (1) says the weighted positive measure

```
ν₂=(1/2)Σ_jδ_j²(δ_{γ_j}+δ_{−γ_j})
```

has mass `o(T)`, the full current is not a fixed multiple of `ν̂₂`: its weights are `[cosh(δ_j u)−1]/u` and depend on both `u` and `j`. Formally splitting off the `δ_j²` term of `cosh`'s expansion does not allow applying the no-gap lemma; the higher moments can cancel the first as distributions. **This expansion alone does not prove** an inequality preventing that cancellation. The later proof `R163_116` avoids the expansion and uses a convex test common to every `δ_j`.

This was the precise mathematical target at the close of `R163_115`. **Update:** `R163_116` proves the no-gap lemma for the full mixture via a compact convex test, and leaves as this route's only gate the arithmetic derivation of `q_E=0` on `(0,log2)` from `(PC-ren)`/Poisson–Tate. The bare bound (1) does not supply that gap.

**Falsifier:** the periodic model `R163_108` has a fixed displacement and the gap `(0,log2)`, but its spectrum has mass `ν([-T,T])≈cT`, **not** `o(T)`; hence it does not contradict the lemma.
