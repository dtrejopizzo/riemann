# E88.003 - Layer tangent integral as a scattering quotient

## 1. Exact endpoint identity

For every finite section and every positive `epsilon`, the fundamental theorem
of calculus gives

```text
integral_(1-epsilon)^1 partial_t log Q_t(s)dt
 =log[Q_1(s)/Q_{1-epsilon}(s)].                       (1.1)
```

The independent Euler product contributes

```text
integral_(1-epsilon)^1 partial_t log E_{L,t}(s)dt
 =epsilon J_L(s).                                     (1.2)
```

Therefore the exact relative layer is

```text
LAYER_{L,N,epsilon}(s)
 =log[Q_1(s)/Q_{1-epsilon}(s)]-epsilon J_L(s).         (1.3)
```

## 2. Scaled limit

Choose `epsilon_N=rho_N T`.  Under E88.002 and zero-freeness of the limiting
bilateral functions,

```text
Q_{1-rho_N tau}(s)
```

has the same projective limit as

```text
q_tau(s)=g_tau(iu)g_tau(-iu).                         (2.1)
```

Consequently,

```text
LAYER_{L,N,rho_N T}(s)
 ->log[q_0(s)/q_T(s)]                                 (2.2)
```

projectively, provided `rho_N J_L(s)->0` locally uniformly.

### Proof

The common factor `(a_N/rho_N)^2` cancels in the quotient of the two bilateral
functions.  Apply E88.002 at `tau=0,T`.  The Euler term tends to zero under the
stated condition. `QED`

## 3. Interpretation

The singular tangent integral is not estimated pointwise in `t`.  It is
evaluated as the scattering quotient of the effective pencil between
`tau=T` and the exact arithmetic endpoint `tau=0`.

The remaining arithmetic theorem is to identify the outer projective value of
this quotient and show that it cancels the signed `BASE-BULK` defect of
E87.005.

## 4. Status

```text
proved:
  exact finite layer quotient;
  conditional scaled scattering limit;

open:
  CCM verification of the pencil hypotheses;
  outer arithmetic identification of q_0/q_T.
```

