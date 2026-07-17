# P76.057 - Rectangular displacement propagation

Let `M` be the rectangular CCM block with row mesh `I` and column mesh
`I union {b}`.  Let `D_r,D_c` be the corresponding diagonal mesh matrices,
and let `s_r,s_c` be the sampled sine symbols.  The Loewner identity gives
the exact rectangular displacement law

```text
D_r M-M D_c
=-(2/L)(s_r 1_c^T-1_r s_c^T).                  (RDP-1)
```

If `Mw=f`, define the two generator moments

```text
m_0=1_c^T w,
m_s=s_c^T w.
```

Applying `(RDP-1)` to `w` yields

```text
M D_c w
=D_r f+(2/L)(s_r m_0-1_r m_s).                 (RDP-2)
```

This formula is exact and explains why only the moments measured in P76.055
enter after one commutation.  Repeating it propagates higher mesh powers
without introducing the ambient inverse norm.

For the canonical shell vector of P76.054,

```text
r(z_0)w=0,
r(z)w=(z_0-z) sum_j w_j/[(z-d_j)(z_0-d_j)].     (RDP-3)
```

The theorem target is now the structured stability estimate

```text
RDP-SHELL:
||f||+|m_0|+|m_s| <= C_M(L) N^(-M)||w||
```

for sufficiently many fixed commutations, uniformly on compact safe
intervals.  Combining `(RDP-2)`--`(RDP-3)` twice gives

```text
|r(z)w|/|r(z)g|=O_K(L^2/N^2),
```

which is `SHELL-CAUCHY` and hence the summable cutoff cocycle.

The planted falsifier may satisfy this stability theorem; arithmetic
identification is deliberately not claimed here.
