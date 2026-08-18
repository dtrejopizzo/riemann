# E101.048 - Shifted endpoint coboundary

## 1. Rectangular displacement source

Let `M:V_c->V_r` be a full-row-rank rectangular CCM block with diagonal
meshes `D_c,D_r`.  Let `1_c,1_r` be the constant vectors and let `s_c,s_r`
be the two restrictions of the odd Weil symbol.  The displacement identity is

```text
D_rM-MD_c
=-a(s_r 1_c^T-1_r s_c^T),
a=2/L.                                                (1.1)
```

Let the coupled endpoint source be

```text
f=alpha s_r+beta 1_r.                                (1.2)
```

### Proposition 1.1 - Moment representation

If `g in V_c` satisfies

```text
1_c^Tg=-alpha/a,
s_c^Tg= beta/a,                                      (1.3)
```

then

```text
f=(D_rM-MD_c)g.                                      (1.4)
```

If `s_r` and `1_r` are linearly independent, (1.3) is also necessary.

### Proof

Apply (1.1) to `g` and substitute (1.3).  Necessity follows by comparing the
coefficients of `s_r` and `1_r`. `QED`

This is the rectangular form of the endpoint construction in the preceding
coboundary work.

## 2. Shifted range transfer

For any scalar `zeta`, scalar matrices commute with `M`, so

```text
f=(D_r-zeta I)Mg-M(D_c-zeta I)g.                    (2.1)
```

Define

```text
h_zeta=-(D_c-zeta I)g,
r_zeta=(D_r-zeta I)Mg.                               (2.2)
```

Then

```text
f=Mh_zeta+r_zeta.                                    (2.3)
```

Equation (2.3) is an explicit `WEIL-RANGE-TRANSFER`.  It uses only the two
moments (1.3), the mesh multiplier and the finite CCM block.  No right
inverse is used to construct `h_zeta`.

## 3. Exact dual pairing

Let `p_zM=q_z` be the dual Green equation of E101.046.  Applying `p_z` to
(2.3) gives

```text
p_z f
=-q_z(D_c-zeta I)g
 +p_z(D_r-zeta I)Mg.                                 (3.1)
```

The first term is an elementary source observation.  The only reduced
leakage is

```text
LEAK_(N,z,zeta;g)
=p_z(D_r-zeta I)Mg.                                  (3.2)
```

Although its two terms depend on `zeta`, their sum does not.  Indeed,

```text
d/dzeta[-q_z(D_c-zeta I)g
         +p_z(D_r-zeta I)Mg]
=q_zg-p_zMg=0.                                       (3.3)
```

Thus the shift is a genuine gauge for distributing the same signed current
between the direct source and the leakage.

## 4. Safe rows separate row residuals

Let `K` have an accumulation point outside the column mesh.  Assume the
normalized boundary problem has the unique solution `y`, so the restriction
`T=M|_(ker ell)` is injective as in E101.045.

### Theorem 4.1

If `r in V_r` satisfies

```text
p_zr=0 for every z in K,                              (4.1)
```

then `r=0`.

### Proof

Since `M` has full row rank, there is a unique `v in ker ell` with `Mv=r`.
The dual equation gives

```text
p_zr=q_zv=c_zv-B_y(z)ell v=c_zv.                    (4.2)
```

Hence the rational Cauchy transform `c_zv` vanishes on a set with an
accumulation point and therefore vanishes identically.  Its residues recover
all coordinates away from a possible zero mesh point.  The remaining
coordinate is recovered from `ell v=0`.  Thus `v=0` and `r=Mv=0`. `QED`

### Corollary 4.2 - Exact leakage annihilation

Choose `zeta` outside the row mesh.  Then

```text
LEAK_(N,z,zeta;g)=0 for every z in K
iff
Mg=0.                                                 (4.3)
```

### Proof

Theorem 4.1 applied to `r=(D_r-zeta I)Mg` gives `r=0`.  The diagonal factor
is invertible, so `Mg=0`.  The converse is immediate. `QED`

This proves that a continuum of safe observations cannot be annihilated by
tuning a finite corrector unless the corrector is an actual boundary-kernel
vector.  Cancellation at one selected safe point is insufficient.

## 5. Kernel-moment alignment criterion

Let `ker M=span{y}` and write

```text
m_0=1_c^Ty,
m_s=s_c^Ty.                                          (5.1)
```

### Theorem 5.1

There exists a vector `g` satisfying both the source moments (1.3) and
`Mg=0` if and only if

```text
alpha m_s+beta m_0=0,                                (5.2)
```

with the evident nonzero compatibility when one of `m_0,m_s` vanishes.

### Proof

Every kernel vector is `g=cy`.  Its moment pair is

```text
(1_c^Tg,s_c^Tg)=c(m_0,m_s).                          (5.3)
```

It equals the target pair `(-alpha/a,beta/a)` exactly when the two pairs are
collinear and their nonzero component fixes `c`.  Their two-by-two
determinant is

```text
(-alpha/a)m_s-(beta/a)m_0,
```

whose vanishing is (5.2). `QED`

When (5.2) holds, the entire endpoint source belongs to the represented
range:

```text
f=-M(D_c-zeta I)g,                                   (5.4)
```

and (3.1) has no reduced leakage.  When (5.2) fails, exact disappearance on
a safe set is impossible for every corrector satisfying the two source
moments.

## 6. Approximate alignment is the cofinal theorem

Exact finite alignment is not required by IDENT.  The cofinal requirement is
the weaker statement that one can choose moment-correct vectors `g_N` and a
fixed shift outside the row meshes so that

```text
sup_(z in K)
|p_(N,z)(D_(r,N)-zeta I)M_Ng_N|/|B_(k_N)(z)| ->0.   (6.1)
```

The parity-cluster construction of the earlier endpoint work is one method
of choosing `g_N` near `ker M_N`.  E101.048 shows exactly what it must prove:
not smallness of `M_Ng_N` in an ambient norm, but safe annihilation of its
shifted row-mesh image.

The force-bearing arithmetic statement is still (6.1).  The commutator and
moment algebra close the construction of the range transfer but do not prove
its cofinal leakage estimate.

## 7. Revised tail ledger

The radical-tail obligations of E101.047 now read

```text
RT-0  cofinal l1 source convergence for PROLATE-INBAND;
RT-1  shifted endpoint range transfer;                         proved;
RT-2  recombined Fourier collar through RDP-SHELL;
RT-3  shifted safe leakage (6.1).                              (7.1)
```

`RT-3` is the rectangular dual form of the cofinal parity-cluster response.
It is not an additional theorem beside that response.

## 8. Status

```text
proved:
  rectangular two-moment endpoint representation;
  explicit shifted WEIL-RANGE-TRANSFER;
  gauge independence of the complete dual pairing;
  separation of row residuals by the safe dual family;
  exact kernel-moment alignment criterion;

closed:
  construction half of RT-1;

open:
  RT-0, cofinal l1 prolate convergence;
  RT-2, recombined RDP-SHELL;
  RT-3, shifted safe leakage and hence DIRECTIONAL-IDENT.
```
