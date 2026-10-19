# R163_140 — Exact ledger of rational collisions in the Selberg collar

**Status:** exact decomposition of `R163_139`'s collar into positive Gamma energy, physical interior, and finite rational-ratio collisions. It does not control the sign of the latter and does not close Row D.

## Theorem

Let `X=e^{2T}`, `F` real, primitive, of parity `ε`, supported on `I_T`, and `A=M−C_Λ` the full operator. Define the autocorrelation `c_F(v)=∫F(t)F(t+v)dt`, supported on `[−2T,2T]`, and the weights `v_d=Λ(d)d^(−1/2)` for `2≤d≤X`. For each integer `n>X`,

```
 w_A(n)=−εΣ_{m≥1}K_m(F)² n^(−2m−1)
        −n^(−1/2)Σ_{2≤d≤X}v_d c_F(log(n/d)).       (1)
```

The second sum can be non-zero only if `X<n<dX≤X²`; in particular it vanishes for `n≥X²` (at the endpoint `c_F(±2T)=0`). With `W=Λ·log+Λ*Λ` from `R163_135`, define

```
 I_X(F)=Σ_{2≤n≤X}W(n)w_A(n),
 E_X(F)=Σ_{m≥1}K_m(F)²Σ_{n>X}W(n)n^(−2m−1),
 C_X(F)=Σ_{X<n<X²} W(n)n^(−1/2)
          Σ_{2≤d≤X}Λ(d)d^(−1/2)c_F(log(n/d)).   (2)
```

Then `C_X` is a **finite** sum, `E_X(F)>0` if `F≠0`, and the second jet has the exact balance

```
 B_F''(0)=E_X(F)+ε C_X(F)−ε I_X(F).          (3)
```

*Proof.* For `v=log n>2T`, every point `t+v` with `t∈I_T` lies to the right of `I_T`. The exterior expansion of `MF` in `R162_1201 Thm 1.2`, after removing the Tate mode by primitivity, gives

```
 ∫F(t)(MF)(t+v)dt=−εΣ_mK_m(F)²e^(−a_m v).
```

The full comb acts via `CF=Σ_dv_d(τ_{log d}F+τ_{−log d}F)`. In the correlation at displacement `v>2T`, the term with `v+log d` vanishes by support and the other equals `c_F(v−log d)`, giving (1) after multiplying by `n^(−1/2)`. `c_F`'s support forces `v−log d<2T`, i.e. `n<dX`; since `d≤X`, only `n<X²` contributes. Inserting (1) into `B_F''(0)=−εΣ_nW(n)w_A(n)` (`R163_135`) produces (3). Absolute convergence and `E_X`'s strict positivity follow from `W≥0`, `s_m=2m+1>1`, the Gamma-moment bound and their completeness. □

## Divisibility versus non-divisible ratios

In `C_X`, each pair `(n,d)` reads `c_F(log(n/d))`. We can split exactly

```
 C_X=C_X^{div}+C_X^{nondiv},
 C_X^{div}: sum over d|n,
 C_X^{nondiv}: sum over d∤n.                 (4)
```

For `d|n`, the displacement is `log k` with `k=n/d∈ℕ`; there a divisor reindexing exists compatible with the Dirichlet ring and with `Λ*1=log`. For `d∤n`, the displacement is the logarithm of a **non-integer rational ratio**; a reindexing by divisors alone does not include those terms, and `c_F` generally does not vanish there. These are the physical collisions that a simultaneous application of Poisson/Fourier and Euler must transport with their sign. Discarding them without an additional identity would turn the product of translation operators into an incorrectly purely divisorial convolution.

Neither `C_X^{div}` nor `C_X^{nondiv}` has a determined sign: a contact `F` can change sign, so `c_F(v)` can be negative. Nor does `PAPF=0` imply `C_X` vanishes; `R163_139 (3)` shows it lies within the Tate/exterior pairing. So (3) implies neither `B_F''(0)>0` nor a contradiction. The usefulness of (4) is a precise test for a future `(PC-ren)` identity: it must preserve the non-divisible rational contacts and explain how the Poisson orientation combines them with the Tate counterterms; the isolated Euler-divisor datum cannot do it.
