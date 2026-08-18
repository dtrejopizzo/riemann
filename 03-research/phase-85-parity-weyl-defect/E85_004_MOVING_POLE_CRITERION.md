# E85.004 - Moving-pole criterion and quadratic separation

## 1. Positivity of the shifted inner spectrum

Let `H_N` be the full real symmetric section, let `mu_N` be its lowest
eigenvalue, and let `H_N^in` be the principal inner block.  Put

```text
M_N=H_N^in-mu_N I.                                    (1.1)
```

### Proposition 1.1

```text
M_N>=0.                                               (1.2)
```

If the lowest full eigenvalue is strictly below the lowest inner eigenvalue,
then `M_N>0`.

### Proof

Cauchy interlacing gives

```text
lambda_min(H_N^in)>=lambda_min(H_N)=mu_N.              (1.3)
```

Subtracting `mu_N` proves (1.2), with strictness under strict interlacing.
`QED`

Thus the cluster measures in E85.002 are probability measures on the
nonnegative axis.

## 2. Exact bounds at a moving complementary pole

Let `omega` be a probability measure supported in `[0,eta]` and set

```text
Delta(z)=1/z+integral d omega(lambda)/(lambda-z),
m_1=integral lambda d omega(lambda).                   (2.1)
```

### Theorem 2.1

For every real `z>eta`,

```text
Delta(z)<0                                            (2.2)
```

unless `omega=delta_0`, and

```text
m_1/z^2
 <=-Delta(z)
 <=m_1/[z(z-eta)].                                    (2.3)
```

### Proof

The algebraic identity of E85.002 gives

```text
-Delta(z)
 =integral lambda/[z(z-lambda)] d omega(lambda).       (2.4)
```

For `0<=lambda<=eta<z`,

```text
lambda/z^2
 <=lambda/[z(z-lambda)]
 <=lambda/[z(z-eta)].                                 (2.5)
```

Integration proves (2.3), and (2.2) follows unless the first moment is zero,
which on the nonnegative axis is equivalent to `omega=delta_0`. `QED`

## 3. Necessary and sufficient moving-pole scales

For sequences `omega_N`, `eta_N` and `z_N>eta_N`, Theorem 2.1 implies:

```text
Delta_N(z_N)->0
 =>m_{1,N}/z_N^2->0.                                  (3.1)
```

If additionally

```text
eta_N/z_N<=1-kappa                                    (3.2)
```

for a fixed positive `kappa`, then

```text
Delta_N(z_N)->0
 <=>m_{1,N}/z_N^2->0.                                 (3.3)
```

This is a quadratic separation law.  Linear collapse of the cluster relative
to the moving pole is insufficient.

## 4. Weak convergence is insufficient

Take

```text
omega_N=delta_{a_N},
a_N->0,
z_N=2a_N.                                             (4.1)
```

Then `omega_N` converges weakly to `delta_0`, but

```text
Delta_N(z_N)=-1/(2a_N),                               (4.2)
```

which diverges.  Even the choice `z_N=sqrt(a_N)` gives a defect tending to a
nonzero constant.  Therefore ordinary projective convergence of the cluster
does not control the moving complementary poles sampled by the reduced
response.

## 5. Two admissible closure mechanisms

The exact scalar targets `PW-E` and `PW-O` can now close in only two ways:

```text
MP-1  MOVING-POLE COLLAPSE:
      prove a sufficiently uniform version of m_1/z^2->0 across the
      complementary spectral support carrying the safe weights;

MP-2  SIGNED COMPLEMENT CANCELLATION:
      retain the q-sum in PW-E and PW-O and prove cancellation after the
      safe Cauchy weights, without bounding each Delta(lambda_q).       (5.1)
```

`MP-1` is a strong spectral route and must be checked against the collapsing
gap wall.  `MP-2` is the scalar Weyl-reduced leakage route in its irreducible
form.

## 6. Status

```text
proved:
  positivity of the shifted inner spectrum;
  exact two-sided moving-pole bounds;
  quadratic separation criterion under a relative edge gap;

refuted:
  weak cluster convergence as sufficient for PW-E or PW-O;

open:
  MP-1 or MP-2 for the actual CCM sections.
```

