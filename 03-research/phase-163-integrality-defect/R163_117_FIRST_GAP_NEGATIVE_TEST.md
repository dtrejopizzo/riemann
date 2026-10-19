# R163_117 — Negative test on the first prime gap for infinitely many quartets

**Status:** theorem proved for the exchange built from ζ's effective zeros. It excludes `ζ/E` having a positive Beurling **prime** measure if there are quartets, even infinitely many. **It does not prove RH:** that quotient's positivity does not follow from ζ's arithmetic.

## Theorem

Let `E` be `R163_001`'s effective exchange and `q_E` its current. If at least one off-line zero exists, there is a test function `φ≥0`, `φ∈C_c^∞(0,log 2)`, such that

```
⟨q_E,φ⟩<0.                                             (1)
```

Since the ordinary prime measure `dΠ_ζ=Σ_{p,k≥1}k^{-1}δ_{k log p}` vanishes on `(0,log 2)`, the formal identity `dΠ_{ζ/E}=dΠ_ζ+q_E` cannot be a positive measure. This last statement can be read without presupposing that `q_E` is a measure: a positive distribution would automatically be a positive measure, and (1) rules that out.

## Proof

We use `r` and `B_δ` from `R163_116`, so that `q_E(u)=2e^{u/2}u r(u)` for `u>0` and

```
r(u)=Σ_j δ_j² B_{δ_j}(u) cos(γ_j u).
```

Fix `b=1/2<log2` and the non-negative even function

```
H_b(u)=|u|(b−|u|)_+².
```

For `u∈[0,b]`, `H_b(u)=u(b−u)²`. Its Fourier transform is

```
Ĥ_b(γ)=(2/γ²)[−b²−(2b/γ)sin(bγ)
                         +(6/γ²)(1−cos(bγ))].          (2)
```

Hence, for `γ≥14`,

```
Ĥ_b(γ)≤(2/γ²)[−b²+2b/γ+12/γ²].                 (3)
```

We must keep the variable factor `B_δ`, not discard it. `B_δ`'s positive Taylor series gives, uniformly for `0≤δ≤1/2` and `0≤u≤b`,

```
0≤B_δ(u)−1≤u²/12,
0≤B_δ'(u)≤u/6,
0≤B_δ''(u)≤1/6.                                      (4)
```

Set `R_δ(u)=H_b(u)(B_δ(u)−1)`. On `[0,b]`, both `R_δ` and its first derivative vanish at both endpoints. Also `|H_b''|≤4b`, `|H_b'|≤b²` and `∫₀ᵇH_b(u)du=b⁴/12`. Two integrations by parts and (4) give

```
|R̂_δ(γ)| ≤ (2/γ²) ∫₀ᵇ |R_δ''(u)|du
           ≤ (2/γ²)[b⁴/9+b⁴/6+b⁴/72]
           = (2/γ²)(7b⁴/24).                         (5)
```

Adding (3) and (5), for `b=1/2`, `γ≥14` and every `δ≤1/2`,

```
widehat(H_b B_δ)(γ)
 ≤ (2/γ²)[−1/4+1/14+12/14²+7/384]
 < 0.                                                   (6)
```

The [Platt–Trudgian](https://arxiv.org/abs/2004.09765) rigorous verification of RH up to height `3·10¹²` ensures every height `γ_j` of a hypothetical effective quartet exceeds 14. The series of pairings converges absolutely, since `widehat(H_b B_δ)(γ)=O(γ^{-2})` uniformly and `Σ_j δ_j²/γ_j²<∞`. By (6),

```
⟨r,H_b⟩=Σ_j δ_j² widehat(H_b B_{δ_j})(γ_j)<0       (7)
```

if at least one quartet exists.

### Quantitative comparison with the central detector

The estimate above does more than give a sign. Define `D_-=−⟨r,H_b⟩` and `D_0=log E(1/2)=2Σ_j log(1+δ_j²/γ_j²)` as in `R163_001`. The bracket in (6) is less than `−0.099`, so

```
D_- ≥ 0.198 Σ_j δ_j²/γ_j² ≥ 0.099 D_0.              (8)
```

Likewise, the absolute bounds of (3) and (5), together with `γ_j≥14`, give `D_-≤0.802 Σ_jδ_j²/γ_j²`. Since `δ_j²/γ_j²≤1/784` and `log(1+t)≥t/(1+t)`, we get `D_0≥[2/(1+1/784)]Σ_jδ_j²/γ_j²`, and hence `D_-≤D_0`. In summary,

```
0.099 D_0 ≤ D_- ≤ D_0.                                 (9)
```

This comparison turns the localized negativity into a faithful quantitative detector of the exchange's central excess. It does **not** by itself supply the opposite arithmetic inequality: requiring `D_-≤0` would be equivalent to RH, just as requiring `D_0=0` would.

The function `H_b` is continuous and has bounded-variation derivative, but it is not `C∞` and touches `u=0`. To obtain (1), we cut `H_b` near `0` and `±b`, smooth it while preserving non-negativity, and use even tests `H_{b,n}∈C_c^∞((-b,b)\{0})` converging to `H_b`. Their derivatives have uniformly bounded variation; the transforms of `H_{b,n}B_δ` are dominated by `C_b/(1+γ²)`, uniformly in `n,δ`, and converge pointwise. Passing to the series in (7) is justified by dominated convergence. Since `r` is even, some test `H_{b,n}` has a negative pairing, and so does its restriction to `u>0`. Dividing that restriction by `R163_116`'s positive factor `2e^{u/2}u` produces a smooth `φ≥0`, compactly supported in `(0,b)⊂(0,log2)`, satisfying (1). □

## What it resolves and what it does not

1. It extends the finite-case quotient positivity obstruction (`R162_2901`) to the **effective infinite exchange**, without assuming the current is a density or an atom. The negative sign appears on a test localized before the first prime.
2. It does not prove `E=1`. `ζ/E` may be a meromorphic object with a signed prime measure; there is no theorem making it positive Beurling from `b(n)≡1` for ζ. Postulating that positivity would introduce as a hypothesis exactly what is missing.
3. The periodic model `R163_108` is not a falsifier of (1): its heights are not zeros of ζ, and its current vanishes on the first gap, made possible by a linear spectral mass and a contact term at `u=0`. Epstein and Davenport–Heilbronn lack the ordinary Euler product; Beurling–DMV lacks the exact integer lattice. None supplies the missing bridge that would force `ζ/E` to be positive.

**Remaining arithmetic gate:** find a property of the effective quotient derived from ζ's exact integrality and Euler product that contradicts (1), without postulating generalized positivity of the quotient. Inequality (1) now fixes a concrete falsifier for every candidate.
