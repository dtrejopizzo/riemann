# R163_131 — Quartic order of the entropic sign and requirement for `(PC-ren)`

**Status:** exact homogeneity computation and audit against `R162_903 §5`. It delimits the necessary bridge; it is not the bridge and does not close Row D.

## Proposition

Let `0≠F∈ker H_T` under `R163_127`'s hypotheses and `b_F=−εh_A(F)`. For `r∈ℝ`, the cross correlation and the lift are quadratic:

```
 b_{rF}=r²b_F,
 b_F(0)=∫b_F=0,
 b_F≠0.                                             (1)
```

Hence, for any ordinary prime `p`, the exact cocycle satisfies

```
 ⟨Φ_Λ,e^{b_{rF}(p·)}−e^{b_{rF}}⟩
   =(log p)[1−∫e^{r²b_F}]
   =−(log p)r⁴ ||b_F||²₂/2 + O_F(r⁶),         r→0.  (2)
```

The quartic coefficient is strictly negative and, by Parseval and `R163_127 (4a)`, has an explicit bound for any integer `k₀>e^{4T}`:

```
 ||b_F||²₂/2 = Σ_{k≥1}|b̂_F(k)|²
 ≥ [Σ_{m≥1}K_m(F)²/(ζ(2m+1)k₀^(2m+1))]²>0.     (3)
```

*Proof.* The map `F↦AF` is linear; `c_A(F;v)=⟨F,τ_vAF⟩` and Möbius inversion are quadratic. The equality `b_F(0)=∫b_F=0` is `R163_127 (6)` on the radical, and `b_F≠0` follows from the Gamma tail. Uniform Taylor expansion, since `b_F` is continuous and bounded, gives `∫e^{r²b_F}=1+r²∫b_F+r⁴∫b_F²/2+O_F(r⁶)`. The second-order term vanishes. Parseval and the `k₀` coefficient give (3). □

## Compatibility test for a physical bridge

Suppose an identity is proposed, valid for **all** multiples `rF` of the same contact, with entropic side (2) and a physical side homogeneous of degree two in `F`, `r²Q(F)`, with no other terms. Dividing by `r²` and letting `r→0` forces `Q(F)=0`; substituting back gives a contradiction with (2)'s strictly negative `r⁴` coefficient. So a direct quadratic pairing from `(PC-ren)` cannot exactly equal or oppose the entropic defect unless it introduces an additional `F`-dependent operation producing at least degree four (or a non-polynomial family with that leading term).

This does **not** rule out a quartic bridge. However, `R162_903 Thm 5.1` already proves that a degree-four homogeneous polynomial in `F` built only from the operator operations listed there becomes a quadratic form over `F⊗F`; that lift alone carries over the falsifiers and produces no arithmetic orientation. So the new step would have to identify an **oriented** quartic contraction mixing, before taking the limit or the square, the terminal term of `Λ*1=log`, the polar/Tate subtraction, and the exterior of the compression. Neither (2) nor the abstract tensor proves one exists.

**Reading:** the contact selector exactly removes the cocycle's degree-two term; the first new sign is quartic and quantitatively faithful to the Gamma moments. Any supposed closure that compares, without corrections, a quadratic physical form with that sign fails on scale grounds, regardless of the analytic details.
