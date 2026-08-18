# E89.005 - Exact crosswalk to LP and IDENT

## 1. The bordered profile is the safe Cauchy profile

Let `D` be the diagonal mesh operator and let the full bordered row have the
form

```text
h_z^T=1^T+q^T(zI-D)^(-1).                             (1.1)
```

For the effective resonant vector `p_t`, define its full-space lift

```text
tilde p_t=(p_t,-C_t^(-1)B_t^*p_t).                   (1.2)
```

The Feshbach bordered profile satisfies exactly

```text
phi_t(z)=h_(t,z)^eff p_t=h_z tilde p_t.               (1.3)
```

It is a finite Cauchy transform plus the mass at infinity:

```text
phi_t(z)
 =1^T tilde p_t
  +sum_j q_j tilde p_(t,j)/(z-d_j).                  (1.4)
```

Consequently, after fixing one safe base point `z_*`,

```text
Phi_t(z;z_*)=phi_t(z)/phi_t(z_*)                     (1.5)
```

is exactly the projective safe Cauchy profile used by the Weyl limit-point
and identification chain.  The Feshbach reduction changes the coordinate
representative of the resonant direction and transports its embedding through
`C_t^(-1)B_t^*`, but does not change the full bordered scalar in (1.3).

## 2. Layer rotation is endpoint identification

Where the profile is nonzero,

```text
partial_t log Phi_t(z;z_*)
 =partial_t log phi_t(z)-partial_t log phi_t(z_*).    (2.1)
```

Integration across the endpoint layer gives

```text
log[Phi_1(z;z_*)/Phi_(1-epsilon)(z;z_*)]
 =integral_(1-epsilon)^1
    partial_t log Phi_t(z;z_*)dt.                    (2.2)
```

Thus `PROFILE-ROTATION-RDI` does not introduce a new limiting object.  It is
the endpoint-layer coordinate form of the arithmetic identification clause:
the unique projective Cauchy profile selected by the finite system must equal
the independently normalized Euler--Gamma profile.

## 3. Bilateral crosswalk

Put `u=s-1/2` and define

```text
B_t(s;s_*)
 = [phi_t(iu)phi_t(-iu)]
   /[phi_t(iu_*)phi_t(-iu_*)].                        (3.1)
```

Then

```text
partial_t log B_t(s;s_*)
 =ROT_t(s)-ROT_t(s_*),                               (3.2)
```

and

```text
B_1(s;s_*)/B_(1-epsilon)(s;s_*)
 =exp integral_(1-epsilon)^1
   [ROT_t(s)-ROT_t(s_*)]dt.                           (3.3)
```

Under `DOM-E` and matched-width existence, the scalar eigenvalue and source
overlap cancel by E89.002.  Hence (3.3) is precisely the nonconstant part of
the endpoint scattering quotient in E88.003.  Combining it with `BASE-BULK`
is equivalent to the relative ratio in E80.003.

## 4. Logical consequence

The endpoint cascade has now been separated into two kinds of information:

```text
normalization data:
  resonant eigenvalue;
  source overlap;
  absolute inverse scale;

projective arithmetic data:
  safe Cauchy profile of the resonant line;
  its base-point-subtracted rotation current.         (4.1)
```

The first group can prove dominance but cannot establish RDI.  The second
group is IDENT in deformation coordinates.  Therefore the endpoint-layer
analysis does not bypass the arithmetic discriminant; it locates it exactly
in the rotation of the projective resonant profile.

This also proves that `GAP-Z` is convergence infrastructure rather than the
arithmetic anchor.  A proof of `GAP-Z` may construct the limit, but only the
profile identity can identify that limit with the Euler--Gamma object.

## 5. Status

```text
proved:
  exact equality of the resonant bordered scalar with a projective safe
  Cauchy profile;
  inclusion of the Schur-row transport in the lifted profile current;
  exact base-point-subtracted layer current;
  equivalence of the surviving layer quotient with the endpoint contribution
  to RDI under DOM-E and matched-width existence;

open:
  DOM-E and matched-width existence;
  the Euler--profile identity for the projective rotation current.
```
