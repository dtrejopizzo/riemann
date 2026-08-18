# E101.074 - Horizontal quartet blindness and the fixed-radical no-go

## 1. Result

The horizontal moving-level projection does not add an independent equation
to the four-pole collar of E101.073.  Against the constrained bordered
covector, its scalar level correction disappears identically.  For the
rank-four quartet perturbation `Y=delta M`, the complete horizontal response
is simply

```text
R_z(Y)=sum_(p in P_zeta)K_p R_p^T S_z R_p,          (1.1)
```

where `S_z` is the trace-free cotangent sensitivity of E101.007.

There is an exact blindness criterion.  At a simple characteristic level,
all safe boundary observations are stationary under `Y` if and only if the
normalized characteristic vector is an eigenvector of `Y`.  For the quartet
factorization this leaves two finite alternatives: its Cauchy moments all
vanish, or the characteristic vector lies in the four-Cauchy span.

At the completed Weil level the first alternative becomes decisive.  A
quartet already contained in the zero divisor of the transform of the fixed
radical is invisible to that radical, because every inserted spectral term
is multiplied by zero.  An artificial controlled quartet, chosen away from
the original divisor, can be detected; a hypothetical off-line zero already
belonging to the divisor cannot be excluded by that same fixed-radical
response.

Thus the controlled plant remains a falsifier, but its nonzero response is
not a theorem forbidding actual off-line zeros.  Any further route must
change the source information, not only its finite shift or characteristic
gauge.

## 2. Horizontal and cotangent cancellation

Let

```text
K=H-mu I                                             (2.1)
```

be real symmetric with a simple zero eigenvalue.  Let `v` be its unit kernel
vector and `Pi=vv^T`.  For a symmetric direction `Y`, E101.001 gives

```text
Hor_K(Y)=Y-q_Y I,
q_Y=v^TYv.                                          (2.2)
```

Let `T_z` be the raw bordered covector and

```text
S_z=Cot_K(T_z).                                     (2.3)
```

E101.007 proves

```text
Tr S_z=0,
Tr[T_z Hor_K(Y)]=Tr(S_zY).                          (2.4)
```

### Proposition 2.1 - No new scalar pole equation from level motion

For the quartet perturbation

```text
Y=sum_(p in P_zeta)K_p R_pR_p^T,                   (2.5)
```

one has

```text
Tr[T_z Hor_K(Y)]
=sum_(p in P_zeta)K_p R_p^TS_zR_p.                 (2.6)
```

### Proof

Use (2.4), insert (2.5), and apply cyclicity of the trace. `QED`

The level velocity itself is

```text
q_Y=sum_(p in P_zeta)K_p(v^TR_p)^2.                (2.7)
```

It is already contained in (2.6).  Because `S_z` is trace-free, retaining
`q_Y I` separately cannot impose a fifth relation on the four Cauchy
coordinates.  It only undoes the same scalar gauge in a different notation.

## 3. Determining safe observations

Normalize the characteristic vector by a fixed row `ell`:

```text
y=v/(ell v),
Ky=0,
ell y=1.                                           (3.1)
```

Let

```text
B_y(z)=c_zy,
(c_z)_n=z/(z-d_n).                                  (3.2)
```

The Cauchy rows `c_z` on any set with an accumulation point outside the mesh
determine a finite vector: if `c_z w=0` on such a set, then the rational
function vanishes identically and every residue `w_n` is zero.

Consider the characteristic path

```text
H(t)=H+tY,
mu(0)=mu.                                           (3.3)
```

Let `y(t)` be its normalized simple characteristic vector.  Differentiation
gives

```text
K dot y=-Hor_K(Y)y,
ell dot y=0.                                        (3.4)
```

### Theorem 3.1 - Exact horizontal blindness criterion

The following statements are equivalent:

```text
(i)  d/dt B_(y(t))(z)|_(t=0)=0 on a safe set with an accumulation point;

(ii) dot y=0;

(iii) Hor_K(Y)y=0;

(iv) Yy=q_Y y.                                      (3.5)
```

### Proof

The determining property following (3.2) proves `(i)=>(ii)`, and the reverse
implication is immediate.  Equation (3.4) proves `(ii)=>(iii)`.  Conversely,
if `(iii)` holds, then (3.4), the simplicity of the kernel and
`ell dot y=0` force `dot y=0`.  Finally, (2.2) gives the equivalence of
`(iii)` and `(iv)`. `QED`

The criterion is stronger than first-order stationarity.  If `(iv)` holds,
then

```text
[H+tY]y=[mu+tq_Y]y                                  (3.6)
```

for every `t`.  As long as the branch stays simple, the normalized
characteristic direction and all its boundary transforms remain exactly
constant.  Higher derivatives do not repair this blindness.

## 4. Rank-four alternatives

Let `R` be the matrix whose columns are the four vectors `R_p`, and let
`D_K` be the diagonal matrix of the nonzero coefficients `K_p`.  Then

```text
Y=R D_K R^T.                                       (4.1)
```

For four distinct poles and at least four distinct mesh points, the Cauchy
matrix `R` has full column rank.

### Proposition 4.1

If the quartet direction is horizontally blind, then exactly one of the
following algebraic alternatives occurs:

```text
q_Y=0:
  R^Ty=0, so every quartet Cauchy moment of y vanishes;

q_Y!=0:
  y belongs to ran R and satisfies R D_K R^Ty=q_Yy.  (4.2)
```

### Proof

Blindness gives `Yy=q_Yy`.  If `q_Y=0`, (4.1) and full column rank of `R`,
together with invertibility of `D_K`, give `R^Ty=0`.  If `q_Y!=0`, then
`y=q_Y^(-1)R D_K R^Ty` lies in `ran R`. `QED`

The second alternative is much more restrictive than a generic
rank-four coincidence, but it is not impossible for an arbitrary finite
characteristic vector.  Rank alone cannot exclude it.

## 5. Parity reduction

The controlled quartet kernel is centrosymmetric.  If the simple
characteristic vector is even,

```text
y_(-n)=y_n,                                         (5.1)
```

then

```text
y^TR_(-p)=-y^TR_p.                                 (5.2)
```

The even part of the four-Cauchy span is generated by

```text
E_p(n)=R_p(n)-R_(-p)(n)
      =2p/(d_n^2-p^2),
p=zeta,conj(zeta).                                  (5.3)
```

Hence the blind alternatives reduce to

```text
q_Y=0:
  y^TR_zeta=y^TR_(conj(zeta))=0;

q_Y!=0:
  y belongs to span{E_zeta,E_(conj(zeta))}.         (5.4)
```

This reduction is finite and exact.  It does not establish a lower bound
for either moment.

## 6. Completed fixed-radical blindness

Let `k` be a source with transform `Khat`, and let a controlled divisor
insertion add a finite quartet `Q`.  In the completed spectral
representation,

```text
delta Q(k,phi)
=sum_(rho in Q)Khat(rho)Phi_phi(rho).               (6.1)
```

This is the formula already recorded in E101.056.  It has the immediate
consequence which the controlled-build use must respect.

### Theorem 6.1 - A divisor insertion is invisible to its own radical

If

```text
Khat(rho)=0 for every rho in Q,                     (6.2)
```

then

```text
delta Q(k,phi)=0                                    (6.3)
```

for every admissible test `phi`.

### Proof

Every summand in (6.1) vanishes. `QED`

For the Riemann source,

```text
Khat=Xi.                                            (6.4)
```

An artificial quartet chosen away from the original zero divisor generally
has `Xi(rho)!=0` and is therefore detectable on some tests.  This is the
legitimate controlled falsifier used in E101.056.

If, however, `Xi` itself had an off-line quartet, then that quartet would
satisfy (6.2).  Adding another copy of those spectral atoms, or removing
them in the linearized spectral formula, is invisible to the fixed source
`k`.  The radical was constructed to vanish on the entire divisor, without
distinguishing on-line from off-line points.

Therefore

```text
nonzero response of an artificial plant
does not imply
nonzero response at a hypothetical off-line zero of Xi.              (6.5)
```

This is not a numerical caveat.  It is an exact consequence of radicality.

## 7. Consequence for the Loewner discriminant

The separable collar of E101.073 is a finite approximation to (6.1) after
the source is split into interior and exterior coefficients.  The phase-79
discriminant needs a rule which fails for every off-line arithmetic divisor,
not merely for an added quartet which is not a zero of the fixed transform.

The following inference is now rejected:

```text
the controlled inserted quartet has a nonzero rank-four response;
therefore an actual off-line quartet cannot occur in Xi.              (7.1)
```

The premise is true for generic artificial points.  The conclusion does not
follow because actual zeros lie in the blind set (6.2).

Accordingly, `RATIONAL-EXTERIOR-NONCANCELLATION` cannot serve as the full
arithmetic discriminant when it is formulated only with the fixed radical
`kappa_Z`.  Its plant version remains a consistency test.

## 8. The only viable repair class

To detect a point where `Xi` itself vanishes, the source data must contain a
transform which does not vanish there.  A canonical source-first family is

```text
k_r(x)=x^r k(x),
widehat(k_r)(z)=i^r Xi^((r))(z),
r>=1.                                               (8.1)
```

At a zero of multiplicity `m`,

```text
widehat(k_r)(rho)=0 for r<m,
widehat(k_m)(rho)!=0.                               (8.2)
```

The family (8.1) is fixed without knowing any zero location.  It removes the
blindness theorem at the level of point separation.  It also destroys the
original radical identity: the on-line divisor now contributes as well.

Thus a viable jet repair must prove all of the following:

```text
JET-1  construct the source hierarchy and all endpoint corrections before
       selecting a zero or terminal test;

JET-2  derive its Gamma--Euler or differentiated-radical identity without
       assuming a zero location;

JET-3  cancel the complete on-line background by an exact signed relation,
       not by positivity or a zero-by-zero sum;

JET-4  retain enough jet orders to detect arbitrary finite multiplicity;

JET-5  connect the resulting nonzero off-line response to
       DIRECTIONAL-IDENT.                            (8.3)
```

The first and fourth items are algebraic.  The second, third and fifth may
carry the full remaining difficulty.  No claim that they hold is made here.

## 9. Stop rules

The following routes are now frozen:

```text
using characteristic level motion as an extra scalar pole equation;
using higher variation of a direction satisfying Yy=q_Yy;
promoting generic rank-four nonvanishing to actual-divisor detection;
using the artificial plant response as a proof that Xi has no off-line zero;
retaining the same radical while asking it to distinguish parts of its own
zero divisor.                                         (9.1)
```

The last line is the controlling no-go.  It is independent of finite-section
conditioning and survives every exact Abel or Loewner transfer.

## 10. Status

```text
proved:
  exact rank-four horizontal response formula;
  disappearance of the scalar level channel against the cotangent projection;
  equivalence between total safe-observation blindness and Yy=q_Yy;
  exact persistence of that blindness along the full linear path;
  four-Cauchy and parity-reduced blind alternatives;
  completed fixed-radical blindness on its own zero divisor;

rejected:
  the horizontal projection as an independent fifth pole relation;
  actual-zero exclusion from artificial-plant nonvanishing;
  the fixed radical as a discriminator of on-line versus off-line parts of
  its own divisor;

opened conditionally:
  the source-jet repair package JET-1--JET-5;

open:
  a non-circular differentiated-radical identity,
  DIRECTIONAL-IDENT and Omega7.
```
