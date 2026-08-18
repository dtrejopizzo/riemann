# Phase 89 closure - Projective endpoint localization

## 1. Closed mathematics

For a simple dominant resonant line, the bordered numerator admits

```text
G_t(z)
 =-[(h_(t,z)^eff p_t)(p_t^Tb_t^eff)]/lambda_t
  +R_t(z).                                            (1.1)
```

Uniform dominance implies

```text
G_t(z)/G_t(z_*)
 ->[h_(t,z)^eff p_t]/[h_(t,z_*)^eff p_t].             (1.2)
```

The collapsing eigenvalue and source overlap cancel exactly.  The remaining
quantity is the projective safe Cauchy profile.

The exact transported Kato formula gives its rotation current:

```text
partial_t log(h_(t,z)^eff p_t)
 =[(dot h_(t,z)^eff)p_t]/[h_(t,z)^eff p_t]
  +sum_q
   [h_(t,z)^eff q_t]/[h_(t,z)^eff p_t]
   [q_t^T dot F_t p_t]/(lambda_t-lambda_(q,t)).       (1.3)
```

Equivalently, with

```text
tilde p_t=(p_t,-C_t^(-1)B_t^*p_t),                   (1.4)
```

the current is `partial_t log(h_z tilde p_t)`.  Base-point subtraction removes
every scalar normalization.  The resulting bilateral quotient is exactly the
endpoint contribution to RDI and hence to IDENT.

## 2. Correction

Scale separation between the even and odd resonances does not by itself
prove a matching window.  Uniform dominance on a sequence satisfying

```text
rho_E<<epsilon_N<<rho_O                               (2.1)
```

is a separate theorem obligation.

## 3. Exact location of the arithmetic discriminant

The endpoint analysis proves the following localization:

```text
spectral collapse and boundary overlap
  -> projective normalization only;

rotation of the normalized Cauchy profile
  -> arithmetic identification.                      (3.1)
```

Thus the force-bearing step is the Euler identification of the projective
profile, equivalently RDI-ANCHOR.  `GAP-Z` remains sufficient convergence
infrastructure but is not this identification.

## 4. Closure grade

```text
closed:
  scalar-factor cancellation;
  exact lifted profile-rotation formula, including Schur-row transport;
  crosswalk from the endpoint layer to LP and IDENT;
  correction of the matched-width implication;

open and transferred:
  DOM-E;
  matched-width existence;
  Euler identification of the projective Kato current;
  RDI-ANCHOR and Omega7.
```
