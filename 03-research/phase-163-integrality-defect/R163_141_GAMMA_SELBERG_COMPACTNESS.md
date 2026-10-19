# R163_141 — Gamma–Selberg energy is faithful but compact: no uniform absorption

**Status:** operator property proved for `R163_140`'s positive energy. It rules out a uniform coarse bound on the collar; it does not rule out a ζ-specific-kernel inequality, nor does it close Row D.

## Theorem

With `X=e^{2T}`, let

```
 α_{m,X}=Σ_{n>X}W(n)n^(−2m−1)>0,
 E_X(F)=Σ_{m≥1}α_{m,X}|K_m(F)|²,
 K_m(F)=∫_{−T}^T F(t)e^{−(2m+1/2)t}dt.       (1)
```

The positive operator `G_X` defined by `E_X(F)=⟨F,G_XF⟩` is of **trace class** on `L²(I_T)`. Its restriction to the primitive space is injective, but there is no `c_T>0` such that

```
 E_X(F)≥c_T||F||²
```

for all primitive vectors. In particular, there exist normalized primitive vectors `F_j` with `E_X(F_j)→0`.

*Proof.* Let `n₀` be the smallest integer `>X` with `W(n₀)>0`; it exists because every sufficiently large prime has `W(p)=(log p)²>0`. For `m≥1`,

```
 α_{m,X}≤n₀^(−2m+2)Σ_{n>X}W(n)n^(−3),
```

and the last sum is finite. Also

```
 ||e^{−(2m+1/2)t}||²_{L²(I_T)}
   =sinh((4m+1)T)/(2m+1/2)
   =O_T(e^{4mT}/m).
```

Since `n₀>X=e^{2T}`, the series

```
 tr G_X=Σ_m α_{m,X}||e^{−(2m+1/2)t}||²
        ≪_{T,X} Σ_m (e^{4T}/n₀²)^m/m<∞
```

converges. Completeness of the Gamma moments (`R162_1201`) implies that `E_X(F)=0` forces `F=0` on the primitive space. Since this space is infinite-dimensional, a positive compact operator cannot be bounded below by `c_T I`; a primitive orthonormal sequence has `E_X(F_j)→0` by compactness. □

## Implication for the rational collar

In `R163_140 (3)`, `B_F''(0)=E_X(F)+εC_X(F)−εI_X(F)`. `E_X`'s strict positivity is **algebraically faithful**, but its scale can be arbitrarily small relative to `||F||²` on the primitive space. So a collar control obtained merely as

```
 |C_X(F)|+|I_X(F)|≤C_T||F||²
```

cannot show the collar is smaller than `E_X(F)` for every `F`; even a small coefficient `C_T` does not establish a relative gap. What is needed is an inequality **on ζ's first-contact kernel**, depending on ζ's exact weight and the Tate/exterior ports, or a relative control in the Gamma observation norm. `R161_068 §4` shows why a direct pullback of that norm inserts the extra factor `A`.

The result does not prove such specific inequalities are impossible: a fixed `H_T`'s kernel is finite-dimensional. It does fix the standard for a valid argument and prevents presenting an absolute Cauchy–Schwarz as compensation for the positive term.

## Nodal audit

Parity likewise gives no sign to `c_F(log(n/d))` in `C_X`: `R162_407 Prop 4.3` observes that the sign near the endpoint depends on the product of `F`'s boundary values, not on prime density; `R162_1602 Prop C` proves that kernel positivity plus the two Tate restrictions does not control the number of sign changes. The floating nodal data of `R162_1501` are not a certified contact inequality. So no nodal-sign hypothesis is incorporated into (1)–(3).
