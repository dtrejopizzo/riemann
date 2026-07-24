# E101.058 - Offset-matched shift separation

## 1. Setting

Retain the rectangular block, diagonal meshes and dual row of E101.048:

```text
D_rM-MD_c=-a(s_r ell-1_r s_c^T),
p_zM=q_z=c_z-B_y(z)ell,
B_y(z)=c_zy,
My=0,
ell y=1.                                             (1.1)
```

Let `g` satisfy the two source moments

```text
ell g=m_0,
s_c^Tg=m_s,                                         (1.2)
```

and put

```text
m_d(g)=ell D_cg.                                    (1.3)
```

The exactly matched choice `zeta=z` of E101.052 simplifies the represented
term, but E101.052(6.2)--(6.5) shows that it also creates a blind corrector
subspace.  The purpose here is to test the nearest nondegenerate choice.

Fix a scalar

```text
eta!=0
```

and choose the offset-matched shift

```text
zeta=z+eta.                                         (1.4)
```

No inverse of `D_r-zeta I` is used below.

## 2. Exact offset formula

Define

```text
L_z^eta(g)=p_z(D_r-(z+eta)I)Mg.                     (2.1)
```

### Theorem 2.1

For every safe observation point `z`,

```text
p_zf
=z m_0+eta c_zg
 +B_y(z)[m_d(g)-(z+eta)m_0]
 +L_z^eta(g).                                       (2.2)
```

### Proof

The shifted range identity E101.048(3.1) gives

```text
p_zf=-q_z(D_c-(z+eta)I)g+L_z^eta(g).                (2.3)
```

The Cauchy identity `c_z(D_c-zI)=-z ell` implies

```text
c_z(D_c-(z+eta)I)g=-z m_0-eta c_zg.                (2.4)
```

Also,

```text
ell(D_c-(z+eta)I)g=m_d(g)-(z+eta)m_0.               (2.5)
```

Insert (2.4)--(2.5) into `q_z=c_z-B_y(z)ell` and then into
(2.3). `QED`

The price of restoring separation is the elementary Cauchy term
`eta c_zg`.  It is finite, inverse-free and retains the complete corrector
rather than collapsing it to one moment.

## 3. Exact covariance

Let `g'` be a second vector with the same two source moments and put

```text
h=g'-g.
```

Then

```text
ell h=0,
s_c^Th=0.                                           (3.1)
```

The displacement law gives

```text
(D_r-(z+eta)I)Mh=M(D_c-(z+eta)I)h.                 (3.2)
```

Applying `p_zM=q_z` and using (2.4) with `m_0=0` yields

```text
L_z^eta(g+h)-L_z^eta(g)
=-eta c_zh-B_y(z)ell D_ch.                          (3.3)
```

Define the offset current

```text
J_z^eta(g)
=eta c_zg+B_y(z)m_d(g)+L_z^eta(g).                  (3.4)
```

Equation (3.3) proves

```text
J_z^eta(g+h)=J_z^eta(g).                            (3.5)
```

Formula (2.2) becomes

```text
p_zf
=m_0[z-(z+eta)B_y(z)]+J_z^eta.                     (3.6)
```

Thus the complete current is independent of the corrector for every `eta`,
as it must be.

## 4. Separation restored by a nonzero offset

### Theorem 4.1

Assume the safe set `K` has an accumulation point outside the column mesh.
For two moment-correct vectors `g,g'`,

```text
L_z^eta(g')=L_z^eta(g) for every z in K
```

if and only if

```text
g'=g.                                                (4.1)
```

### Proof

Let `h=g'-g` and `m=ell D_ch`.  Since `B_y(z)=c_zy`, equation
(3.3) says that equality of the leakage families is equivalent to

```text
c_z(eta h+m y)=0                                    (4.2)
```

for every `z in K`.

The finite Cauchy family separates vectors.  Indeed, if

```text
c_zv=z sum_j v_j/(z-d_j)
```

vanishes on a set with an accumulation point, it vanishes as a rational
function.  Its residues recover every coordinate at a nonzero mesh point;
the remaining zero-mesh coordinate is then recovered from the constant
term.  Hence (4.2) gives

```text
eta h+m y=0.                                        (4.3)
```

Apply `ell` and use `ell h=0`, `ell y=1`.  This gives `m=0`.
Since `eta!=0`, equation (4.3) then gives `h=0`.  The converse is immediate.
`QED`

This theorem is stronger than separation of `Mh`: it separates the
moment-correct coefficient vector itself.  It uses neither an ambient inverse
nor a lower bound for a singular value.

## 5. Singular limit at exact matching

At `eta=0`, equation (3.3) collapses to

```text
L_z^0(g+h)-L_z^0(g)=-B_y(z)ell D_ch.                (5.1)
```

Its kernel is precisely the three-moment blind space

```text
ker ell intersect ker s_c^T intersect ker(ell D_c) (5.2)
```

found in E101.052.  Thus the loss of separation is not a numerical accident.
It is a rank collapse at the single parameter value `eta=0`.

For every nonzero `eta`, the missing Cauchy transform reappears and restores
injectivity.  The degeneration is therefore quantified exactly:

```text
full Cauchy information has coefficient eta;
the single mesh moment has coefficient B_y(z).       (5.3)
```

Any uniform passage `eta->0` must control the first term before allowing it
to disappear.

## 6. Consequence for the proof route

The offset current supplies a valid finite coordinate for further estimates:

```text
OFFSET-MATCHED-IDENT:
  identify
  m_0[z-(z+eta)B_(y_N)(z)]+J_(N,z)^eta
  with the independent Gamma-prime current,          (6.1)
```

bilaterally and with one safe derivative, for one fixed `eta!=0`.

Equation (3.6) shows that (6.1) is exactly the original paired current, not a
new limiting assertion.  The gain is algebraic: a proposed estimate can no
longer hide a nonzero corrector in the blind space of exact matching.

The theorem does not prove decay of `L_z^eta`, boundedness of the dual row or
the arithmetic identification.  It is a diagnostic and a nondegenerate
coordinate, not the force-bearing step.

## 7. Status

```text
proved:
  exact offset-matched endpoint formula;
  corrector covariance of the offset current;
  injectivity of the complete offset leakage family;
  exact rank collapse as eta tends to zero;

rejected:
  use of the exactly matched leakage as a separating family;

open:
  a cofinal estimate for the complete offset current;
  DIRECTIONAL-IDENT and Omega7.
```
