# E101.052 - Observation-matched shift

## 1. Cauchy cancellation identity

Retain the rectangular notation of E101.048.  Let

```text
c_z=z 1_c^T(zI-D_c)^(-1),
q_z=c_z-B_y(z)ell,
ell=1_c^T.                                           (1.1)
```

The pointwise identity

```text
z/(z-d_j) (d_j-z)=-z                                 (1.2)
```

gives the row formula

```text
c_z(D_c-zI)=-z ell.                                  (1.3)
```

Consequently,

```text
q_z(D_c-zI)
=-z ell-B_y(z)ell(D_c-zI).                           (1.4)
```

This is an exact cancellation between the safe observation and the shifted
column mesh.

## 2. Matched-shift endpoint formula

Let `g` satisfy the two endpoint-source moments

```text
m_0=ell g=-alpha/a,
m_s=s_c^Tg=beta/a,                                   (2.1)
```

and define the additional mesh moment

```text
m_d=ell D_cg.                                        (2.2)
```

Choose the shift `zeta=z` in E101.048(3.1).

### Theorem 2.1

For every safe observation point `z`,

```text
p_zf
=z m_0+B_y(z)(m_d-zm_0)
 +p_z(D_r-zI)Mg.                                     (2.3)
```

### Proof

E101.048 gives

```text
p_zf=-q_z(D_c-zI)g+p_z(D_r-zI)Mg.                   (2.4)
```

Applying (1.4) to `g` yields

```text
-q_z(D_c-zI)g
=z m_0+B_y(z)(m_d-zm_0).                             (2.5)
```

Substitution proves (2.3). `QED`

The full vector `g` has disappeared from the represented part.  Only its
single free mesh moment `m_d` remains.

## 3. Three-moment gauge

Assume the three rows

```text
ell,
s_c^T,
ell D_c                                               (3.1)
```

are linearly independent.  Then for every scalar `tau` there is a vector
`g_tau` satisfying

```text
ell g_tau=m_0,
s_c^Tg_tau=m_s,
ell D_cg_tau=tau.                                    (3.2)
```

It may be chosen without `M^(-1)`, for example as the minimum Euclidean norm
solution of the three scalar equations.  The particularly simple gauge

```text
tau=0                                                (3.3)
```

gives

```text
p_zf
=m_0 z[1-B_y(z)]
 +p_z(D_r-zI)Mg_0.                                   (3.4)
```

The direct term is now completely determined by the normalized finite
boundary transform and the source coefficient `alpha`.  This is a coordinate
choice; it does not imply that the remaining leakage is small.

If the rows in (3.1) are dependent, the admissible values of `tau` form the
corresponding affine compatibility set; no inverse of the CCM block enters
that decision.

## 4. Corrector-gauge covariance

Let `g` and `g'` satisfy the same two source moments and put `h=g'-g`.
Then

```text
ell h=0,
s_c^Th=0.                                            (4.1)
```

The complete value `p_zf` is independent of the corrector.  Formula (2.3)
therefore implies

```text
p_z(D_r-zI)Mh
=-B_y(z)ell D_ch.                                    (4.2)
```

### Direct proof

The zero source moments and the displacement identity give

```text
(D_rM-MD_c)h=0.                                      (4.3)
```

Hence

```text
(D_r-zI)Mh=M(D_c-zI)h.                               (4.4)
```

Apply `p_zM=q_z`, then use (1.4) and `ell h=0`:

```text
p_z(D_r-zI)Mh
=q_z(D_c-zI)h
=-B_y(z)ell D_ch.                                    (4.5)
```

This proves (4.2). `QED`

Thus changing the corrector moves exactly one scalar multiple of `B_y`
between the represented term and the leakage.  No other functional freedom
is present.

Define the matched current

```text
J_z(g)
=B_y(z)ell D_cg+p_z(D_r-zI)Mg.                      (4.6)
```

Equation (4.2) proves

```text
J_z(g')=J_z(g)                                       (4.7)
```

for every two correctors with the same source moments.  Thus `J_z` is the
corrector-invariant quantity.  Formula (2.3) becomes

```text
p_zf=m_0z[1-B_y(z)]+J_z.                             (4.8)
```

## 5. Bilateral and derivative form

For `z=plus or minus i sigma`, equation (3.4) gives the two endpoint currents

```text
p_(i sigma)f
=i sigma m_0[1-B_y(i sigma)]
 +LEAK_+(sigma),

p_(-i sigma)f
=-i sigma m_0[1-B_y(-i sigma)]
 +LEAK_-(sigma).                                     (5.1)
```

Their base-point-subtracted logarithmic current requires only `B_y`, `B_y'`
and the two invariant currents `J_(plus or minus i sigma)` with one
derivative.  Differentiating (4.8) gives

```text
partial_z[p_zf]
=m_0[1-B_y(z)-zB_y'(z)]
 +partial_z J_z.                                     (5.2)
```

No derivative of the corrector occurs.

## 6. Blind subspace of the exactly matched gauge

The separation theorem E101.048(4.1) applies to a fixed row residual while
the observation point varies.  It cannot be applied with `zeta=z`, because

```text
r_z=(D_r-zI)Mg                                      (6.1)
```

itself varies with `z`.  Formula (4.5) gives the correct conclusion.

Let

```text
H_3=ker ell intersect ker s_c^T intersect ker(ell D_c).  (6.2)
```

For every `h in H_3`,

```text
p_z(D_r-zI)Mh=0                                     (6.3)
```

for every safe `z`.  If the three rows in (3.1) are independent and the
column space has dimension at least four, then

```text
dim H_3=dim V_c-3>=1.                               (6.4)
```

Under the uniqueness hypothesis of E101.045, `M|_(ker ell)` is injective.
Consequently every nonzero `h in H_3` satisfies

```text
Mh!=0                                               (6.5)
```

while remaining invisible to the entire matched leakage family (6.3).
Thus matched observations do not separate `Mg`.

There is also an exact scalar criterion.  Write

```text
L_z(g)=p_z(D_r-zI)Mg,
J_z=p_zf-m_0z[1-B_y(z)].                            (6.6)
```

Equation (4.8) gives

```text
L_z(g)=J_z-B_y(z)m_d.                               (6.7)
```

Hence a moment-correct `g` has zero matched leakage on a safe set `K` if
and only if

```text
J_z=m_d B_y(z)                                      (6.8)
```

for every `z in K`.  Where `B_y` is nonzero, this says that `J_z/B_y(z)`
is the constant attainable mesh moment `m_d`.  Kernel alignment is a
sufficient realization of (6.8), but it is not necessary.  The previous
claim that zero matched leakage is equivalent to `Mg=0` is therefore false.

## 7. Reduced RT-3 target

The valid theorem must be stated for the invariant combination:

```text
MATCHED-CURRENT-IDENT:
  identify, bilaterally and locally uniformly with one derivative,

  m_0z[1-B_(y_N)(z)]+J_(N,z)

  with the corresponding independent Gamma-prime endpoint current.   (7.1)
```

In the zero-mesh-moment gauge, `J_z` equals the shifted leakage.  In a
spectral-cluster gauge, it is `B_y m_d` plus that leakage.  These are exactly
the same scalar by (4.7).

Requiring the leakage or `J_z` to vanish separately is not justified unless
the independent target has first been shown to equal
`m_0z[1-B_y(z)]`.  Such a separate-vanishing assertion would repeat the
base/anomaly split rejected in the earlier deformation audit.  The coupled
identity (7.1) is the minimal valid target.

## 8. Status

```text
proved:
  exact cancellation c_z(D_c-zI)=-z ell;
  matched-shift endpoint formula;
  inverse-free three-moment gauge;
  complete corrector-gauge covariance;
  bilateral value and derivative decomposition;
  exact blind subspace and scalar vanishing criterion of the matched gauge;

corrected:
  matched leakage does not separate Mg when zeta=z;

reduced:
  RT-3 to the corrector-invariant MATCHED-CURRENT-IDENT;

open:
  MATCHED-CURRENT-IDENT in the cofinal limit.
```
