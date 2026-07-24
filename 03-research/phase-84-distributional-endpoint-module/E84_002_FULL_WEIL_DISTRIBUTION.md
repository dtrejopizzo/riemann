# E84.002 - Full Weil sine distribution

## 1. The archimedean odd functional

Let

```text
a_L(y)=exp(y/2)+exp(-y/2)-exp(y/2)/(2sinh y).           (1.1)
```

Although `a_L(y)` has a first-order singularity at the origin, the functional

```text
<nu_L^A,psi>=integral_0^L a_L(y)psi(y)dy              (1.2)
```

is well defined for every smooth `psi` satisfying `psi(0)=0`.  Indeed,
`a_L(y)=O(1/y)` and `psi(y)=O(y)` at the origin.

Let the prime current be

```text
nu_L^P=sum_{n<=exp(L)}Lambda(n)n^(-1/2)delta_{log n}. (1.3)
```

Define the full odd Weil distribution by

```text
nu_L^W=nu_L^A-nu_L^P.                                 (1.4)
```

## 2. Exact sine symbol

### Theorem 2.1

For every complex `z`,

```text
S_L(z)=<nu_L^W,sin(z y)>.                             (2.1)
```

### Proof

Apply the finite Weil functional to `psi(y)=sin(z y)`.  Since `psi(0)=0`, all
origin constants vanish.  Its polar integral and Gamma quotient combine to

```text
integral_0^L a_L(y)sin(z y)dy.                        (2.2)
```

The arithmetic term is

```text
-sum_{n<=exp(L)}Lambda(n)n^(-1/2)sin(z log n).         (2.3)
```

Equations (1.2)--(1.4) give exactly (2.1). `QED`

The theorem is valid for complex `z` because the interval is finite and the
renormalized integrand is locally bounded at the origin.

## 3. Exact endpoint representation of the coupled source

Define two finite Fourier boundary maps by

```text
O_N(T)_m=<T,sin(d_m y)>,
E_N(c delta_0)_m=c,                                   (3.1)
```

where `d_m=2pi m/L`.  Then

```text
O_N(nu_L^W)=s_N,
E_N(delta_0)=1.                                       (3.2)
```

Consequently the coupled source has the exact distributional form

```text
f_N=alpha_b O_N(nu_L^W)+beta_b E_N(delta_0).           (3.3)
```

No complement inverse, spectral data or fitted residue is used in (3.3).

## 4. What the Euler ground orbit supplies

The Euler connection of E84.001 produces `nu_L^P`, whereas the source uses

```text
nu_L^W=nu_L^A-nu_L^P.                                 (4.1)
```

Thus the pure Euler orbit does not by itself equal the full sine generator.
The missing term is the continuous archimedean distribution `nu_L^A`, and the
source also contains the independent endpoint mass `beta_b delta_0`.

This closes the ambiguity in `GE-1`: the exact source is a Gamma-minus-Euler
boundary current plus an endpoint mass, not merely an Euler covariant
derivative of a Hilbert vector.

## 5. Status

```text
proved:
  exact archimedean odd distribution;
  exact full Weil sine distribution;
  exact endpoint representation of alpha_b s_N+beta_b 1;

closed:
  source identification as an unspecified Euler-generated vector;

open:
  an inverse-free CCM coboundary for the full distributional source.
```

