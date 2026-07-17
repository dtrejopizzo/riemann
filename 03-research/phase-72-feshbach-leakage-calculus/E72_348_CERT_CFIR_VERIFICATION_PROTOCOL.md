# E72.348 -- CERT-CFIR verification protocol

**Purpose.** Turn the finite row-ideal endpoint into a concrete verification protocol.  This is not a
numerical heuristic: it is an exact finite construction whose output is a family of determinant or
coefficient identities.

## 1. Input data

For fixed `L`, active mesh cutoff `M`, and zero-pair window `W_T`, the protocol takes:

```text
Mesh:
  d_m=2pi m/L, |m|<=M.

Operator:
  C_E(L), mu(L), E(L)=C_E(L)-mu(L)I.

Window:
  W_T={(a_j,m_j)} and Hermite jet map J_T.

Kernels:
  k_z(m)=(1-e^(zL))/(iz-d_m),
  K_L(z,w) from E72.342,
  TailBasis_{z,n}^M(a) from E72.343.
```

No outside zero data are used.

## 2. Build the interpolation row matrix

For each Hermite slot `alpha=(a_j,p)`, construct the row

```text
R_alpha(L)
```

by differentiating

```text
Lambda_L k_z
- I_T^H k_z
+ Tail_T^M basis
```

at `z=a_j` to order `p`, divided by `p!`.

Concretely, the column `n` is:

```text
R_alpha[n]
= (1/p!) partial_z^p [
   Lambda_L k_z(n)
 - (I_T^H k_.)(z)[n]
 + sum_{b in W_T/+-} m_b TailBasis_{z,n}^M(b)
 ] |_{z=a_j}.                                      (1)
```

This yields the finite matrix

```text
R_T(L)={R_alpha(L)}.
```

## 3. Determinant test

For every Hermite slot `alpha` and every row index `i` of `E(L)`, form

```text
D_{alpha,i}(L)
= det ReplaceRow(E(L); i, R_alpha(L)).              (2)
```

The exact certificate is:

```text
D_{alpha,i}(L)=0
for all alpha,i.                                    (3)
```

Equivalently, compute the reduced adjugate:

```text
R_T(L) adj(E(L))=0.                                  (4)
```

The determinant test is preferable for exact algebra because each `D_{alpha,i}` is a scalar identity.

### Proof

Because the pole-even ground eigenspace is simple, `E(L)` has a one-dimensional right nullspace.  A
row `R_alpha` belongs to `Row(E)` exactly when it annihilates that nullspace.  The reduced adjugate has
range equal to the nullspace and kernel equal to the rowspace annihilator, hence

```text
R_alpha adj(E)=0
```

is equivalent to row membership.  The determinant replacement identities are the maximal minors of
the augmented row system; they vanish exactly when adjoining `R_alpha` does not raise the rank.

## 4. Coefficient extraction

Expand each determinant by multilinearity over the decomposition

```text
E(L)=E_arch(L)+E_prime(L),
R_alpha(L)=R_arch,alpha(L)+R_prime,alpha(L).
```

The result is

```text
D_{alpha,i}(L)
= sum_{omega in Omega_{alpha,i}(L)}
   c_{alpha,i}(omega;L)
   prod_{r in omega} Lambda(r)r^(-1/2).              (5)
```

The coefficient extractor records:

```text
omega:
  ordered list/multiset of prime powers used by the determinant expansion;

Delta(omega):
  total logarithmic displacement invariant;

c_{alpha,i}(omega;L):
  exact archimedean/Fourier coefficient.
```

## 5. Exact pass conditions

There are three nested pass conditions:

```text
PASS-ROW:
  all D_{alpha,i}(L) vanish exactly.

PASS-COEFF:
  all c_{alpha,i}(omega;L) vanish exactly.

PASS-GCOEFF:
  for each alpha,i and each displacement class Delta,
  sum_{omega:Delta(omega)=Delta}
    c_{alpha,i}(omega;L)
    prod_{r in omega} Lambda(r)r^(-1/2)
  vanishes exactly.
```

The implications are:

```text
PASS-COEFF => PASS-GCOEFF => PASS-ROW => CERT-CFIR.
```

`PASS-ROW` is the minimal exact certificate.  `PASS-COEFF` and `PASS-GCOEFF` are proof strategies.

### Proof of the implications

`PASS-COEFF` makes every coefficient in every determinant expansion vanish, hence every grouped sum
vanishes.  `PASS-GCOEFF` makes each displacement-class contribution to each determinant vanish, so
the determinant itself vanishes.  Vanishing of all determinant tests is `PASS-ROW`, which is exactly
`CERT-CFIR` by the determinant proof above.

## 6. Polynomial residual pass

For asymptotic rather than exact closure, compute the least row-ideal residual

```text
S_T(L):=R_T(L)(I-P_Row(E(L))).
```

The polynomial certificate is:

```text
||S_T(L)|| <= C_TL^B.                                (6)
```

In determinant language this means all replacement determinants are smaller than the corresponding
cofactor scale by at most a polynomial factor.

This version should be used only when exact vanishing fails.

## 7. Output

The verifier must output:

```text
1. the finite matrix R_T(L);
2. determinant identities D_{alpha,i};
3. if expanded, the coefficient table c_{alpha,i}(omega;L);
4. PASS-ROW / PASS-COEFF / PASS-GCOEFF / residual status;
5. the maximal residual scale relative to the leading Cauchy block.
```

This is the first endpoint in Phase 72 whose failure would point to a specific finite determinant or
word class rather than to an analytic tail.

## 8. Status

```text
specified: exact finite construction of R_T and determinant tests;
specified: coefficient extraction and grouped displacement tests;
specified: polynomial residual fallback;
open: execute the protocol symbolically or with interval/rational arithmetic on the actual kernels.
```
