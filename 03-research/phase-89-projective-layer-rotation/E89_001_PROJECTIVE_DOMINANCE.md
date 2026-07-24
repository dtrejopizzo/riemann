# E89.001 - Projective dominance of one resonant parity

## 1. Dominant decomposition

Let `p_t` be a normalized simple resonant eigenvector of the effective even
sector and let `lambda_t` be its scalar Feshbach eigenvalue.  Write

```text
G_t(z)
 =-a_t(z)/lambda_t+R_t(z),                             (1.1)

a_t(z)=(h_(t,z)^eff p_t)(p_t^T b_t^eff).              (1.2)
```

The remainder contains the odd resonant sector and the regular complement.

### Theorem 1.1

Let `V` be a safe domain and suppose

```text
inf_{z in V}|a_t(z)|>0,

sup_{z in V}|lambda_t R_t(z)/a_t(z)|->0               (1.3)
```

along a directed endpoint family.  Then, for every base point `z_* in V`,

```text
G_t(z)/G_t(z_*)
 -a_t(z)/a_t(z_*) ->0                                 (1.4)
```

locally uniformly on `V`.  The same holds for logarithmic derivatives.

### Proof

Factor (1.1):

```text
G_t(z)
 =-[a_t(z)/lambda_t]
   [1-lambda_t R_t(z)/a_t(z)].                         (1.5)
```

The scalar `lambda_t` cancels in the normalized ratio.  The second factor
converges uniformly to one by (1.3), proving (1.4).  Cauchy's formula gives
the derivative statement. `QED`

The theorem is projective; it does not require an upper or lower bound on the
collapsing eigenvalue itself.

## 2. Nested-layer consequence

Suppose the even and odd intrinsic scales satisfy

```text
rho_E/rho_O->0,                                       (2.1)
```

and the even resonant term dominates at `t=1`.  The scale separation (2.1)
alone does not propagate endpoint dominance into a moving layer.  If there is
a sequence `epsilon_N` such that

```text
rho_E<<epsilon_N<<rho_O                               (2.2)
```

and (1.3) holds uniformly for `1-epsilon_N<=t<=1`, then the odd layer belongs
to the regular `BASE-BULK` term rather than the projectively singular endpoint
factor.  Thus matched-width existence is an additional estimate, not a
consequence of the endpoint ratio.

## 3. Status

```text
proved:
  projective dominance theorem;
  irrelevance of the scalar eigenvalue under the dominance hypothesis;

open:
  theorem-grade dominance and overlap bounds for the CCM layer.
```
