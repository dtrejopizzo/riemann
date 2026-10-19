# R163_135 — Mellin jets of the lift: `Λ` and Selberg's sum×product square

**Status:** exact hierarchy proved from `R163_134`; the weight `W` already appears in `R162_702`, but here it is obtained as a jet of the **same port** that interpolates the Gamma squares. No Weil sign is proved and Row D is not closed.

## Jet hierarchy

With `w_A(n)=n^(−1/2)c_A(log n)` and `B_F(s)` from `R163_134`, for every integer `r≥1`,

```
 B_F^(r)(0)=(-1)^(r+1) ε
       Σ_{n≥2} [μ*(log)^r](n) w_A(n).           (1)
```

The sum converges absolutely because `w_A(n)=O(n^(−3))` and the convolution coefficient grows at most like `d(n)(log n)^r`. The formula comes from differentiating

```
 B_F(s)=−ε Σ_{n≥1}w_A(n)
                 Σ_{d|n} μ(d)(n/d)^(−s),
```

which is `R163_134 (4a)` expanded. For `n=1`, the positive-order derivatives vanish.

The first jet is the known prime channel:

```
 B_F'(0)=εΣ_n Λ(n)w_A(n),
 because μ*log=Λ.                                  (2)
```

The **second** jet is exactly the sum×product square:

```
 B_F''(0)=−εΣ_n W(n)w_A(n),
 W:=μ*(log)²=Λ·log+Λ*Λ.                        (3)
```

To check the second equality, for `Re s>1` the Dirichlet series give

```
 Σ_n[μ*(log)²](n)n^(−s)=ζ''(s)/ζ(s)
   =[(ζ'/ζ)' +(ζ'/ζ)²](s),
```

and the coefficients of the last expression are `Λ(n)log n+(Λ*Λ)(n)`. In particular,

```
 W(p^a)=(2a−1)(log p)²,
 W(p^a q^b)=2(log p)(log q)       (p≠q),
 W(n)=0                           if n has ≥3 distinct primes. (4)
```

These are exactly the arithmetic values that `R162_702 §3` identifies as distinct from mere positivity and from support on prime powers. The `p^a q^b` terms were not discarded: they are the multi-prime crossing of the same jet.

## Normalization by ζ at contact

At a first contact `B_F(0)=0`, and with `P_F=ζB_F`, `ζ(0)=−1/2`, `ζ'(0)=−(1/2)log(2π)`, the product rule gives

```
 P_F'(0)=−(ε/2)Σ_nΛ(n)w_A(n),
 P_F''(0)= ε[½Σ_nW(n)w_A(n)
                     −log(2π)Σ_nΛ(n)w_A(n)].      (5)
```

Together with `R163_134 (3)`, a single function `P_F` gathers:

```
 contact:       P_F(0)=0;
 first jet:     Λ;
 second jet:    Λ·log+Λ*Λ;
 Gamma poles:   (-1)^mP_F(−2m)
                  =(2m)!K_m(F)²/[2(2π)^(2m)]≥0. (6)
```

## Audit: why this is still not the gate

The weight `W(n)` is non-negative and keeps exactly the cross-prime terms, but (3) pairs it with `w_A(n)=n^(−1/2)⟨F,τ_{log n}AF⟩`, **not** with a positive autocorrelation of `F`. The extra factor `A` from `R161_068 §4` remains. So the sign of `B_F''(0)` cannot be inferred from `W≥0`; doing so would remove the compression/exterior that needs to be controlled.

Likewise, (1)–(6) hold formally for the contacts of a `κ` model if ordinary Möbius and ordinary ζ are used in the lift: `B_F`'s jets read `Λ` even though the physical operator reads `a_κ`. `R163_133`'s Ward defect points exactly to that mismatch. A `(PC-ren)` identity that genuinely uses **the same** weight at both ports must reproduce that defect as `κ` varies, and must keep the polar/Tate corrections before comparing (5) with (6)'s Gamma values. That identity is not proved.
