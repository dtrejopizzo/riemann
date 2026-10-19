# R163_136 — The Mellin port's reflection defect is exactly the Gamma square

**Status:** meromorphic identity and pointwise evaluation proved from `R163_134`. It formulates an oriented Poisson–Tate target; it does not prove the defect vanishes, and does not close Row D.

## Definition and exact computation

Let `P_F(s)=ζ(s)B_F(s)` be `R163_134`'s port for `F` real, primitive and of parity `ε`. Write ζ's reflection factor as

```
 χ(s)=2^s π^(s−1) sin(πs/2) Γ(1−s),
 ζ(s)=χ(s)ζ(1−s).
```

Define the oriented defect

```
 ℛ_F(s):=P_F(s)−χ(s)P_F(1−s).                (1)
```

As a meromorphic identity,

```
 ℛ_F(s)=ζ(s)[B_F(s)−B_F(1−s)].              (2)
```

For every `m≥1`, `P_F(1+2m)` is finite and `χ(−2m)=0`. `R163_134 (3)`'s interpolation formula then gives, **without taking finite parts**,

```
 ℛ_F(−2m)=P_F(−2m)
          =(-1)^m (2m)!/[2(2π)^(2m)] ·K_m(F)².  (3)
```

In particular, `(-1)^mℛ_F(−2m)≥0`, with equality exactly when `K_m(F)=0`. The full sequence `ℛ_F(−2m)` vanishes if and only if `F=0`, by completeness of the Gamma moments. Vanishing on a subset `S` with `Σ_{m∈S}1/m=∞` also suffices, by `R162_1201 Thm 4.1`.

## What `(PC-ren)` would actually need to contribute

A physical reflection law for the **same** port `P_F`, derived at first contact with every polar/Tate and exterior term, forcing `ℛ_F(−2m)=0` on a sufficient Müntz family, would close Gate 1 via (3). The stronger form `ℛ_F(s)≡0` would also do it. No such law is known. Stating it without proof would be exactly re-postulating the conclusion: (3) shows its value at each Gamma point is a faithful square.

Mere **holomorphy** of `ℛ_F` at `−2m` is not enough: (3) exists and can be non-zero. Nor does ζ's functional equation used in (2) suffice: it just shifts the discrepancy to `B_F(s)−B_F(1−s)`, without annihilating it. The missing orientation has to arise from an identity for the datum `F` and the compressed operator, not from multiplying an arbitrary function by ζ.

## Falsifiers and arithmetic content

For a `κ` model with a kernel, the port built using **ordinary** Möbius and ζ satisfies exactly (1)–(3) with its `F≠0`; so its reflection defect does not vanish. A supposed proof of `ℛ_F=0` valid for that model would be false. To single out ζ, the same weight must be used in `(PC-ren)`'s comb and in the port's arithmetic jets; `R163_133`'s Ward defect measures the mismatch `a_κ−Λ`.

Epstein and Davenport–Heilbronn lack the same ordinary Euler product that makes `R163_134 (4a)` possible; Beurling–DMV lacks torsion indexed by ordinary integers. These differences make the test formulable, but **do not** prove the physical reflection. The goal remains building a formula for `ℛ_F` from `(PC-ren)` that, upon evaluating (3), leaves a sign part incompatible with `F≠0`, without discarding either the collars or the exterior.
