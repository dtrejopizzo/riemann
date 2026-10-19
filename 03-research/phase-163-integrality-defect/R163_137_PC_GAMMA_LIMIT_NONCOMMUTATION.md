# R163_137 — `(PC-ren)` and evaluation on the Gamma lattice do not commute

**Status:** exact obstruction proved for `R161_003`'s polar renormalization; it specifies the counterterms a reflection identity must preserve. Does not close Row D.

## Non-commutation theorem

Let

```
 D_N(s)=Σ_{n=1}^N n^(−s),
 Z_N(s)=D_N(s)−N^(1−s)/(1−s),                 (1)
```

be `R161_003`'s polar-renormalized `(PC-ren)` multiplier. For each `m≥1`, the exact Faulhaber formula gives

```
 Z_N(−2m)
   =N^(2m)/2
     +Σ_{r=1}^m [binom(2m,2r−1) B_{2r}/(2r)]
                                      N^(2m−2r+1). (2)
```

In particular, `Z_N(−2m)∼N^(2m)/2→+∞`, even though `ζ(−2m)=0`. For `m=1`, the visible identity is

```
 Z_N(−2)=Σ_{n≤N}n²−N³/3=N²/2+N/6.         (3)
```

*Proof.* `D_N(−2m)=Σ_{n≤N}n^{2m}` is the Faulhaber polynomial; its leading term is `N^{2m+1}/(2m+1)`, exactly what (1) subtracts. The remaining coefficients are (2), whose leading term is `N^{2m}/2`. □

The convergence `Z_N(1/2+iτ)→ζ(1/2+iτ)` proved in `R161_003` is, therefore, **specific to the critical line**. Analytic continuation of the limit and evaluation at `−2m` cannot be permuted. Nor can one first multiply `Z_N(s)` by `R163_134`'s port `B_F(s)` and then naively take the limit at `s=−2m`: `B_F` has a pole there with residue `K_m(F)²/ζ(2m+1)`, while `Z_N(−2m)` diverges.

## Necessary counterterms

To cover a fixed `m`, the polar operator must retain the complete Euler–Maclaurin correction up to order `m`:

```
 C_{N,m}(s)=N^(1−s)/(1−s)+N^(−s)/2
       −Σ_{r=1}^m [B_{2r}/(2r)!](s)_{2r−1}
                                     N^(1−s−2r),       (4)
```

where `(s)_j=s(s+1)…(s+j−1)`. At `s=−2m`, `D_N(s)−C_{N,m}(s)=0=ζ(−2m)` exactly. This equality is checked by substituting `(-2m)_{2r−1}`: the order-`r` term matches the one in (2). Near `−2m`, these counterterms remove the divergent powers, but controlling the product with `B_F`'s pole additionally requires **the first `s`-derivative** of the renormalized subtraction, not just its value at the point. For all `m` a coherent family of increasing orders and uniform estimates are needed; (4) alone does not supply them.

## Consequence for the gate

`R163_136` identifies the desired physical reflection defect at `−2m` with a non-negative Gamma square. This memo shows why `R161_003`'s small Poisson anomaly on the critical line does **not** imply that defect is zero: before reaching `−2m`, the boundary terms `N^{2m}/2, N^{2m−1},…` of (2) survive. A valid `(PC-ren)` identity must include them, cancel them against the polar/Tate collars and the compressed exterior, and justify the limit after multiplying by `B_F`. Declaring them null from ζ's functional equation would remove exactly the residue one is trying to prove null.

This obstruction does not depend on RH or on the weight Λ: it is already present in the sum of ordinary integers. So it serves as an adversarial audit for any candidate construction, but not as a sign law.
