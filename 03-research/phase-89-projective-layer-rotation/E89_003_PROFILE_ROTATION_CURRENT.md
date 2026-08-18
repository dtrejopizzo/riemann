# E89.003 - Exact profile-rotation current

## 1. Derivative of a normalized eigenprofile

Let `p_t` be a differentiable normalized simple eigenvector of a real
symmetric effective operator `F_t`:

```text
F_t p_t=lambda_t p_t,
p_t^T p_t=1.                                          (1.1)
```

Choose the parallel gauge

```text
p_t^T dot p_t=0.                                      (1.2)
```

Let `(lambda_{q,t},q_t)` be the other orthonormal eigenpairs.  Then

```text
dot p_t
 =sum_q q_t
   [q_t^T dot F_t p_t]/(lambda_t-lambda_{q,t}).        (1.3)
```

### Proof

Differentiate (1.1), take the inner product with `q_t`, and use
`q_t^Tp_t=0`.  The component along `p_t` vanishes by (1.2). `QED`

## 2. Transported Cauchy profile current

For

```text
phi_t(z)=h_(t,z)^eff p_t,                             (2.1)
```

one has

```text
partial_t log phi_t(z)
 =[(dot h_(t,z)^eff)p_t+h_(t,z)^eff dot p_t]
   /[h_(t,z)^eff p_t].                                (2.2)
```

For the fixed Feshbach projection of E88.001,

```text
h_(t,z)^eff=h_(P,z)-h_(Q,z)C_t^(-1)B_t^*,             (2.3)

dot h_(t,z)^eff
 =h_(Q,z)C_t^(-1)dot C_t C_t^(-1)B_t^*
  -h_(Q,z)C_t^(-1)dot B_t^*.                         (2.4)
```

Substitution of (1.3) gives

```text
partial_t log phi_t(z)
 =[(dot h_(t,z)^eff)p_t]/[h_(t,z)^eff p_t]
  +sum_q
   [h_(t,z)^eff q_t]/[h_(t,z)^eff p_t]
   [q_t^T dot F_t p_t]/(lambda_t-lambda_(q,t)).        (2.5)
```

The first term is the Schur-row transport current.  The second is the Kato
rotation current.  Omitting the first term would differentiate the effective
eigenline while freezing its embedding into the full space.

Define the lifted resonant vector

```text
tilde p_t=(p_t,-C_t^(-1)B_t^*p_t).                   (2.6)
```

Then

```text
phi_t(z)=h_z tilde p_t,                               (2.7)

partial_t log phi_t(z)
 =[h_z dot tilde p_t]/[h_z tilde p_t].                (2.8)
```

Thus the corrected current is the rotation of the lifted projective line,
not merely the rotation of its `P` coordinate.

## 3. Bilateral current

Put `u=s-1/2`.  The layer current that survives scalar cancellation is

```text
ROT_t(s)
 =partial_t log[phi_t(iu)phi_t(-iu)].                 (3.1)
```

The endpoint layer contribution is

```text
integral ROT_t(s)dt
 =log[
   phi_1(iu)phi_1(-iu)
   /
   {phi_{1-epsilon}(iu)phi_{1-epsilon}(-iu)}].         (3.2)
```

No zero list enters (2.3)--(3.2).

## 4. Correct layer theorem

```text
PROFILE-ROTATION-RDI:
after the dominance and matching estimates, the bilateral rotation current
in (3.2), combined with BASE-BULK, converges projectively to the independent
Euler--Gamma current on Re s>1.                        (4.1)
```

This is the surviving force-bearing clause.  Proving only convergence of
`p_t` without identifying its profile is insufficient.

## 5. Status

```text
proved:
  exact eigenvector rotation formula;
  exact Schur-row transport formula;
  exact lifted projective Cauchy rotation current;
  exact bilateral endpoint quotient;

open:
  PROFILE-ROTATION-RDI.
```
