# E72.68 -- Half-power Abel concomitant for scalar WRL

**Date:** 2026-07-08.
**Role:** write the correct finite Abel-WRL concomitant after the `u^(-1/2)` normalization.

## 0. Correction from E72.67

The scalar cell in E72.31 is not:

```text
<v,Q_x(y)k>.
```

It is:

```text
L_x(s;e^y)=e^(-y/2)<v_{x,s},Q_x(y)k_x>,
```

up to the harmless Feshbach centering term, which vanishes in the compressed gauge.

Therefore, for:

```text
rho=1/2+i tau,
```

the Abel resonance becomes:

```text
R_x^{cell}(s;tau)
 = L_x(s;1)+rho int_0^L exp(rho y)L_x(s;e^y)dy
 = <v_{x,s},A_x(tau)k_x>,                                      (HPAC)
```

where:

```text
A_x(tau)
 := Q_x(0)+(1/2+i tau)int_0^L exp(i tau y)Q_x(y)dy.              (A)
```

This is the correct half-power Abel concomitant. The cancellation of the `1/2` in the exponential is
the point:

```text
exp(rho y)e^(-y/2)=exp(i tau y).
```

## 1. Exact entry formula

Let:

```text
d_n=2*pi*n/L,       a=i tau,       E=exp(aL).
```

For `dL in 2*pi Z`, define:

```text
C_d(a)=int_0^L exp(ay)cos(dy)dy = a(E-1)/(a^2+d^2),
S_d(a)=int_0^L exp(ay)sin(dy)dy = d(1-E)/(a^2+d^2),
Y_d(a)=partial_a C_d(a).
```

The removable values at `a=+-id` are taken by continuity.

Then the entries of `A_x(tau)` are:

```text
A_nn(tau)
 = 2+(1/2+i tau) * 2( C_{d_n}(a)-Y_{d_n}(a)/L ),                (DIA)
```

and, for `m != n`,

```text
A_mn(tau)
 = (1/2+i tau) *
   [ S_{d_m}(a)-S_{d_n}(a) ]/[pi(n-m)].                         (OFF)
```

These formulas are finite, explicit, and depend only on the CCM mesh.

## 2. Finite spectral divisibility target

Let:

```text
F_x(s;tau):=<v_{x,s},A_x(tau)k_x>.
```

The correct finite height-plane divisibility statement is:

```text
F_x(s;tau)=P_x(tau)B_x(s;tau)+E_x(s;tau),                       (HPAC-DIV)
```

with:

```text
B_x locally normal on compact height windows,
E_x -> 0 locally uniformly,
```

and the same statement after one `s`-derivative.

Equivalently, on finite windows avoiding the pole mesh, `(HPAC-DIV)` can be checked by the finite
interpolation residuals:

```text
F_x(s;tau_j)=o(1)       for all finite Weyl roots P_x(tau_j)=0,  (HPAC-root)
```

together with a normal quotient bound for `F_x/P_x`.

## 3. Why this is the right object

The unnormalized cell-Abel transform of E72.67 was too large and did not vanish at finite roots. The
half-power transform is different: it is a finite Fourier transform of `Q_x(y)` at the spectral height
`tau`, with the exact Abel prefactor `1/2+i tau`.

This is the first place where all three structures meet in one finite scalar:

```text
half-power from the prime cell,
Abel boundary-minus-bulk resonance,
finite CCM spectral height tau.
```

It still does not include the full arithmetic/model subtraction, so exact finite divisibility is not
asserted. The new target is asymptotic divisibility `(HPAC-DIV)`.

## 4. Numerical signal

Using the same finite CCM harness as E72.66--E72.67, the values at the first finite Weyl roots are
substantially smaller after the half-power correction:

```text
lambda=6, N=18:
  roots tau=1.0162, 3.4414, 5.9779, 8.0360
  |F|=7.3e-2, 8.9e-2, 8.1e-2, 2.15e-1

lambda=8, N=24:
  roots tau=0.7284, 2.7080, 4.0531, 5.9877
  |F|=1.7e-2, 3.8e-2, 3.0e-2, 1.9e-2

lambda=12, N=28:
  roots tau=0.8248, 2.1349, 3.2205, 8.1177
  |F|=3.0e-3, 8.0e-3, 1.0e-3, 6.4e-2

lambda=16, N=34:
  roots tau=0.4847, 2.0770, 3.4936, 4.6914
  |F|=3.0e-3, 3.3e-2, 6.0e-3, 1.5e-2

lambda=20, N=40:
  roots tau=0.2409, 1.8562, 3.8436, 4.3510
  |F|=1.7e-2, 1.0e-3, 2.5e-2, 1.0e-2
```

The signal is not an exact finite identity, but it is no longer the hard falsifier of E72.67.

## 5. Closure theorem

### Theorem 72.68

Assume `(HPAC-DIV)` for `F_x(s;tau)` on the two Cauchy heights, with one `s`-derivative, and assume the
finite spectral convergence:

```text
P_x(tau)/P_x(0) -> Xi(tau)/Xi(0)
```

locally uniformly. Then scalar WRL resonance annihilation holds.

### Proof

Let `rho` be a zero of the completed zeta function and write:

```text
rho=1/2+i tau_rho.
```

Then `Xi(tau_rho)=0`. By finite spectral convergence:

```text
P_x(tau_rho)/P_x(0)->0.
```

Using `(HPAC-DIV)`:

```text
F_x(s;tau_rho)
 = P_x(tau_rho)B_x(s;tau_rho)+E_x(s;tau_rho).
```

The local normal bound on `B_x` and `E_x->0` give:

```text
F_x(s;tau_rho)->0.
```

By `(HPAC)`, this is the half-power Abel-WRL resonance for the scalar cell. With the arithmetic/model
matching of E72.31, the same statement for the full scalar kernel gives scalar WRL resonance
annihilation. `QED`

## 6. Remaining exact identity

The finite identity still to prove is now precise:

```text
Half-Power Abel Divisibility:
F_x(s;tau)=<C_x^(-1)Q_x(sI-D_x)^(-1)1, A_x(tau)k_x>
belongs asymptotically to the determinant ideal (P_x(tau)).
```

Equivalently:

```text
F_x(s;tau_j)=o(1) for finite roots tau_j, with a normal quotient bound.
```

This is finite, explicit, and directly testable from the matrices `D_x`, `C_x`, `Q_x`, `k_x`, and
`xi_x`.

## 7. Status

```text
corrected: the actual Abel-WRL cell has the half-power factor e^(-y/2);
proved:    exact finite formula for A_x(tau);
proved:    HPAC-DIV plus finite spectral convergence implies scalar WRL resonance annihilation;
open:      prove HPAC-DIV from the Feshbach equation and finite CCM algebra.
```
