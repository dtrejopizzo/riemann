# R163_138 — Finite confluence: renormalized integer lattice × Gamma pole

**Status:** for each fixed Gamma index, the joint limit that `R163_137` left as an analytic requirement is proved. It is a value identity, not a vanishing law; Row D remains open.

## Theorem

Let `F` be real, primitive, of parity `ε`, the port `B_F(s)` of `R163_134`, and `m≥1` fixed. Define `C_{N,m}(s)` as in `R163_137 (4)` and

```
 Z_{N,m}(s)=Σ_{n=1}^N n^(−s)−C_{N,m}(s).
```

The product `Z_{N,m}(s)B_F(s)` has a removable singularity at `s=−2m` and

```
 J_{N,m}(F):=[Z_{N,m}B_F]_{s=−2m}
    =[K_m(F)²/ζ(2m+1)] Z'_{N,m}(−2m).         (1)
```

Moreover, for fixed `m`,

```
 Z'_{N,m}(−2m)=ζ'(−2m)+O_m(N^(−1)),          (2)

 lim_{N→∞}J_{N,m}(F)
    =(-1)^m (2m)!/[2(2π)^(2m)]·K_m(F)²
    =ℛ_F(−2m).                                (3)
```

The convergence in (3) is quantitative: the absolute error is `O_{m,F}(N^(−1))`.

## Proof

By the exact Faulhaber formula, `Z_{N,m}(−2m)=0` (`R163_137`). By `R163_134`, near that point

```
 B_F(s)=c_m/(s+2m)+H_m(s),
 c_m=K_m(F)²/ζ(2m+1),
```

with `H_m` holomorphic. Multiplying by the expansion `Z_{N,m}(s)=(s+2m)Z'_{N,m}(−2m)+O((s+2m)²)` proves (1), even if `c_m=0`.

For (2) we use Euler–Maclaurin **on a fixed complex neighborhood** of `−2m`, not only on the critical line. After subtracting `R163_137 (4)`'s terms, the first omitted term is

```
 −[B_{2m+2}/(2m+2)!](s)_{2m+1}N^(−s−2m−1).
```

Its coefficient vanishes at `s=−2m` because of `(s)_{2m+1}`'s factor `(s+2m)`; differentiating it there gives `O_m(N^(−1))`. The Euler–Maclaurin remainder, taken two orders further to control a derivative via Cauchy or by differentiating under the remainder integral, contributes `O_m(N^(−2)log N)` or better. So `Z_{N,m}'(−2m)−ζ'(−2m)=O_m(N^(−1))`.

Finally substitute the exact identity `ζ'(−2m)=(-1)^m(2m)!ζ(2m+1)/[2(2π)^(2m)]` into (1) and use `R163_136 (3)`. □

## What connects and what does not

The finite integer `N` enters the **same limit** as the Gamma pole: the sum was not first replaced by ζ, nor were the Euler–Maclaurin boundary terms discarded. It is thus a rigorous analytic confluence of the integer lattice, its polar continuum, and the lift's exterior tail. The Möbius inversion constant `ζ(2m+1)` cancels only at the end, via the functional equation.

However, (1)–(3) hold for **every** primitive `F`, even positive eigenvectors and `κ` models with a kernel. They still do not use `H_TF=0` nor `(PC-ren)`'s physical comb orientation. At contact, (3) is precisely the square that must be forced to zero, not a contradiction. The remaining work is a physical identity that, with the same Euler weight in the operator and in the port, imposes a sign/vanishing relation on `J_{N,m}` after including the Tate collars and the compression. No such identity was obtained.
