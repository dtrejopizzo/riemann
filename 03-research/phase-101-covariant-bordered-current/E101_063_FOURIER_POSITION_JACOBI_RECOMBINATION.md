# E101.063 - Fourier-position Jacobi recombination

## 1. Purpose

The Euler sensitivity route uses the physical position operator, while the
rectangular displacement route uses the Fourier mesh operator.  Treating them
as the same operator is incorrect.  Their finite commutator supplies an exact
bridge.

Combining that bridge with the finite logarithm of the Euler unit produces a
new identity:

```text
physical boundary commutator + compression shell
=one explicit rank-two endpoint source.              (1.1)
```

The identity is universal finite algebra.  Its contraction with the
projective cofactor current remains to be tested.

## 2. Fourier-position commutator

On `L2(0,L)` let

```text
phi_n(t)=L^(-1/2)exp(i d_nt),
d_n=2pi n/L.                                        (2.1)
```

Let `P_N` project onto a finite consecutive set of these modes and put

```text
D_N=diag(d_n),
X_N=P_N(t multiplication)P_N,
J_N=1_N1_N^*.                                       (2.2)
```

### Theorem 2.1

```text
[D_N,X_N]=i(J_N-I_N).                               (2.3)
```

### Proof

For `m!=n`, direct integration gives

```text
(X_N)_(m,n)
=1/L integral_0^L t exp(i(d_n-d_m)t)dt
=i/(d_m-d_n).                                       (2.4)
```

The diagonal entry is `L/2`.  Therefore

```text
([D_N,X_N])_(m,n)=i
```

off the diagonal and is zero on the diagonal.  This is exactly (2.3).
`QED`

## 3. Logarithmic Euler generator

Let `Z` be the finite Euler unit in the commutative truncated-shift algebra.
Every positive shift is nilpotent, so

```text
L_E=log Z                                             (3.1)
```

is a finite algebraic sum.  Put

```text
K=L_E-L_E^*.                                         (3.2)
```

Let `delta T=[X,T]`.  Since the shift algebra is commutative,

```text
delta L_E=Z^(-1)delta Z=A.                           (3.3)
```

Moreover,

```text
[X,L_E^*]=-A^*.                                      (3.4)
```

Hence the Hermitian prime direction is

```text
H_P=A+A^*=[X,K].                                     (3.5)
```

## 4. Compression shell is part of the commutator

Let `P=P_N`, `Q=I-P` and define

```text
K_N=PKP,
H_(P,N)=PH_PP,

Sigma_N=PXQKP-PKQXP.                                (4.1)
```

### Theorem 4.1

```text
H_(P,N)=[X_N,K_N]+Sigma_N.                          (4.2)
```

### Proof

Insert `P+Q` between `X` and `K` in each term of `P[X,K]P`:

```text
PXKP=X_NK_N+PXQKP,
PKXP=K_NX_N+PKQXP.                                  (4.3)
```

Subtract. `QED`

The shell `Sigma_N` need not be small.  It is the exact correction required
when the physical commutator is compressed.

## 5. Jacobi collapse to a rank-two source

Apply the Jacobi identity to (4.2).  Theorem 2.1 gives

```text
[D_N,H_(P,N)]
=[X_N,[D_N,K_N]]
 -i[K_N,J_N]
 +[D_N,Sigma_N].                                    (5.1)
```

Let `s_(P,N)` be the odd sine-symbol vector of the prime direction.  Its
finite CCM displacement law is

```text
[D_N,H_(P,N)]
=-a(s_(P,N)1_N^*-1_Ns_(P,N)^*),
a=2/L.                                               (5.2)
```

Define

```text
v_N=iK_N1_N,
w_N=v_N-a s_(P,N).                                  (5.3)
```

Since `K_N^*=-K_N`,

```text
i[K_N,J_N]=v_N1_N^*-1_Nv_N^*.                      (5.4)
```

Combining (5.1)--(5.4) proves the exact identity

```text
[X_N,[D_N,K_N]]+[D_N,Sigma_N]
=w_N1_N^*-1_Nw_N^*.                                (5.5)
```

Thus the physical boundary term and the compression shell collapse together
to one rank-two endpoint source.  Isolating either term before (5.5) loses
this cancellation.

## 6. Contraction gives two endpoint generators

For every vector `g`, equation (5.5) gives

```text
([X_N,[D_N,K_N]]+[D_N,Sigma_N])g
=alpha_g w_N+beta_g1_N,                             (6.1)

alpha_g=1_N^*g,
beta_g=-w_N^*g.                                     (6.2)
```

This is exactly the two-generator source shape used by the shifted endpoint
coboundary of E101.048.  The vector `v_N=iK_N1_N` is the Fourier endpoint of
the finite logarithmic Euler generator; the second part of `w_N` is the
prime sine symbol.

Equation (6.1) is the first direct algebraic bridge between the physical
Euler boundary kernel and the matched two-generator current.

## 7. Shifted transfer of the prime path current

Let `H=H_(P,N)` and let `D_c,D_r` denote its column and row meshes.  For a
safe scalar `zeta`, set

```text
g_zeta=(D_c-zeta I)^(-1)y.                          (7.1)
```

Then

```text
[D,H]g_zeta
=(D_r-zeta I)Hg_zeta-Hy,                            (7.2)
```

and therefore

```text
p_zHy
=p_z(D_r-zeta I)Hg_zeta
 -p_z[D,H]g_zeta.                                   (7.3)
```

When `[D,H]=w1^*-1w^*`, the direct term is

```text
p_z[D,H]g_zeta
=(p_zw)(1^*g_zeta)-(p_z1)(w^*g_zeta).               (7.4)
```

Equations (7.3)--(7.4) split the complete path current into an explicit
two-generator endpoint term and one shifted leakage:

```text
JLEAK_(N,z,zeta)
=p_z(D_r-zeta I)H(D_c-zeta I)^(-1)y.                (7.5)
```

Only diagonal mesh resolvents occur.  No inverse of the CCM block and no
inverse of `ad_D` is used.

The exactly matched choice `zeta=z` has the blind-space defect isolated in
E101.052.  The nondegenerate choice for a falsifier is

```text
zeta=z+eta,
eta!=0,                                              (7.6)
```

as in E101.058.

## 8. Binary projective test

The new identity advances the force-bearing scalar only if the shifted
leakage in (7.5) disappears after the same projective subtraction used in
E101.062.  This gives a finite test before any asymptotic estimate:

```text
DX-LOG-EULER-JACOBI-MATCH:

for one fixed eta!=0, the complete bilateral base-point subtraction of

JLEAK_(N,z,z+eta)/B_y(z)

is either identically zero, or equals the already defined terminal matched
leakage with all mesh factors and signs fixed.                         (8.1)
```

E101.064 evaluates the prime-only clause at several safe points in the
smallest nontrivial sections.  The projective differences are nonzero by many
orders of magnitude, so direct disappearance of the prime leakage is
rejected.  The moving-level scalar direction is invisible to (5.5) and must
be restored through E101.062.  Only an exact equality for the complete
horizontal direction with the already open terminal matched leakage could
survive; without it, (5.5) is infrastructure.

## 9. No-go boundary

Equation (5.5) controls `[D,H_P]`, whereas the path current contains `H_P`
itself.  Recovering `H_P` by dividing each off-diagonal entry by
`d_m-d_n` would apply `ad_D^(-1)` and return to the Hilbert--Loewner leakage
already isolated in the earlier work.

The shifted identity (7.3) is admissible because it keeps the direct source
and leakage coupled.  Estimating `JLEAK` by an ambient inverse norm is not
admissible; that would reproduce the rejected directional inf-sup route.

The entire construction is build-neutral.  Even if (8.1) passes, arithmetic
force must still enter through the identification of `w_N`, the Gamma source
and the independent Euler current.

## 10. Status

```text
proved:
  exact Fourier-position commutator;
  logarithmic Euler representation H_P=[X,K];
  exact compression shell formula;
  Jacobi rank-two collapse (5.5);
  shifted two-generator transfer (7.3)--(7.5);

forbidden:
  recovery of H_P by a termwise inverse of ad_D;
  separate estimates of physical boundary and compression shell;

falsified in E101.064:
  projective constancy and direct disappearance of prime JLEAK;

frozen:
  asymptotic estimates for JLEAK without a new finite evaluation;

open:
  its projective contraction;
  the Gamma--Euler endpoint identification;
  MATCHED-CURRENT-IDENT and Omega7.
```
