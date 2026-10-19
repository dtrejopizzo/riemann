# R163_134 — Mellin–torsional interpolation of the Gamma squares

**Status:** new identity, proved for the crossed lift; it combines in one computation Möbius inversion, ζ's trivial zeros, and the functional equation. It does not deduce vanishing of the moments nor close Row D.

## Theorem

Let `F≠0` be real, primitive, of parity `ε`, supported on `I_T`, and `b_F=−εh_A(F)` as in `R163_128`. `H_TF=0` is not yet required. For `Re s>−2`, define

```
 B_F(s)=Σ_{k≥1} b̂_F(k) k^(−s).                       (1)
```

The series converges absolutely there and continues meromorphically to all `s∈ℂ`, with at most simple poles at `s=−2m`, `m≥1`, and

```
 Res_{s=−2m} B_F(s)=K_m(F)²/ζ(2m+1).             (2)
```

The product `P_F(s)=ζ(s)B_F(s)` is holomorphic at all those points and takes the exact values

```
 P_F(−2m)
   =ζ'(−2m)K_m(F)²/ζ(2m+1)
   =(-1)^m (2m)!/[2(2π)^(2m)] ·K_m(F)².       (3)
```

In particular, (3)'s alternating orientation comes **from ζ's functional equation**, while the non-negative square comes from the exterior Gamma tail, and the factor `1/ζ(2m+1)` comes from ordinary Euler inversion. The arithmetic constant `ζ(2m+1)` cancels exactly at that very step.

If, moreover, `F∈ker H_T`, then

```
 B_F(0)=Σ_{k≥1}b̂_F(k)=0,
 P_F(0)=0.                                          (4)
```

This is the first-contact condition: for an eigenvector of eigenvalue `λ>0`, `B_F(0)=−ελ||F||²`, non-zero.

The derivative **of the same object** recovers the prime-power channel. Near `s=0`,

```
 B_F(s)=−ε Σ_{n≥1}w_A(n)n^(−s)∏_{p|n}(1−p^s),       (4a)
 B_F'(0)= ε Σ_{n≥2}Λ(n)w_A(n)
         =−½⟨Φ_Λ,b_F⟩.                             (4b)
```

At contact, since `ζ(0)=−1/2` and `B_F(0)=0`, this is equivalent to

```
 P_F'(0)=¼⟨Φ_Λ,b_F⟩.                         (4c)
```

So a single function `P_F=ζB_F` carries the contact selector at `s=0`, the prime/Euler pairing in its derivative, and the oriented Gamma squares at `s=−2m`. None of these identities yet imposes a sign relation between those values.

## Continuation proof

Fix an integer `K>e^(4T)`. By `R163_127 (4a)`, for all integers `k>K`,

```
 b̂_F(k)=Σ_{m≥1}c_m k^(−2m−1),
 c_m=K_m(F)²/ζ(2m+1)≥0.                         (5)
```

From this, first in the half-plane of convergence,

```
 B_F(s)=Σ_{k=1}^K b̂_F(k)k^(−s)
       +Σ_{m≥1}c_m[ζ(s+2m+1)−Σ_{k=1}^K k^(−s−2m−1)]. (6)
```

The bound `K_m(F)²≤2T e^{2a_mT}||F||²` and `K>e^{4T}` make the sum over `m` of the bracketed **tails** converge normally on every compact of `ℂ` avoiding `s=−2m`. Indeed, for `s` in a compact and large `m`, the tail is bounded by a constant of the compact times `(K+1)^(−2m)`, while `K_m(F)²=O_{F,T}(e^{4mT})`; the geometric ratio is `e^{4T}/(K+1)²<1`. For small `m`, ζ's continuation is meromorphic. Only the term indexed by `m` has a pole at `s=−2m`, and ζ's residue at 1 equals 1, giving (2).

ζ has a simple zero at every negative even integer; multiplying (2)'s local expansion by ζ gives (3)'s first equality. The functional equation, differentiated at `s=−2m`, gives

```
 ζ'(−2m)=(-1)^m (2m)! ζ(2m+1)/[2(2π)^(2m)],
```

which proves the second equality. Finally, `R163_127 (6)` gives `Σ_{k≥1}b̂_F(k)=−ε⟨F,H_TF⟩`, giving (4). □

For (4a), inserting `b̂_F(k)=−εΣ_{j≥1}μ(j)w_A(kj)` into (1) and regrouping by `n=kj` gives

```
 Σ_{j|n}μ(j)(n/j)^(−s)
   =n^(−s)Σ_{j|n}μ(j)j^s
   =n^(−s)∏_{p|n}(1−p^s).
```

The rearrangement and term-by-term differentiation near `s=0` are justified by `w_A(n)=O(n^(−3))` and `Σ d(n)|w_A(n)|n^δ<∞` for any `δ<2`. For `n>1`, (4a)'s product vanishes at `s=0`; its derivative also vanishes if `n` has at least two distinct primes. For `n=p^r`, the derivative is `−log p`, giving (4b)'s first equality. The second uses `R163_127 (6a)`'s torsional inversion applied to `b_F=−εh_A`. The product rule and `ζ(0)=−1/2` give (4c).

## Scope audit

1. **Not a closure:** (3) holds for any primitive `F`, even for positive-eigenvalue eigenvectors. Only (4) selects contact, and there is no proved identity transporting `P_F(0)=0` to the values `P_F(−2m)`.
2. **It does not automatically move poles to non-trivial torsional atoms:** (2) is a pole of the Dirichlet series of the test's *Fourier frequencies*; it is not the residue of a pairing of distributions `⟨Φ_Λ,g_{F,s}⟩`. Equating the two without a regularization and an orientation proof would repeat the error audited in `R162_1101`.
3. **Falsifiers:** if a `κ` model preserves the Gamma part and ordinary Möbius inversion is used, (2)–(3) also hold for its kernel `F`. So the identity still needs a mixed law coupling the physical comb's weight with `Φ_Λ`, exactly `R163_132`–`133`'s defect.
4. **Precise gate:** a future Poisson–Tate/`(PC-ren)` identity would have to relate, with the polar collars and the compression, `P_F(0)=0` and `P_F'(0)=¼⟨Φ_Λ,b_F⟩` to at least one oriented value `(-1)^mP_F(-2m)≥0`, and fail on the quantity `D_{a,p}` for `a≠Λ`. Stating that relation does not prove it; (3) and (4c) are explicit ports where it could be tested.
