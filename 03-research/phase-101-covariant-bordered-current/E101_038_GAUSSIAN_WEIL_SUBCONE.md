# E101.038 - Gaussian Weil subcone

## 1. Centered spectral coordinate

For a nontrivial zero `rho`, put

```text
tau_rho=-i(rho-1/2).                                 (1.1)
```

On the critical line, `tau_rho` is real.  The symmetrized partial-fraction
identity and E101.036 give, for `v>0`,

```text
H_Xi(v)=sum_rho exp(-v tau_rho^2).                  (1.2)
```

The sum is absolutely convergent: the imaginary part of `tau_rho` is bounded
in modulus by `1/2`, while its real part is the zero height and the Gaussian
decays quadratically.  Equation (1.2) is used only to identify the Weil test;
the arithmetic definition of `H_Xi` remains E101.036(1.4)--(1.5).

Differentiation gives

```text
(-1)^j H_Xi^(j)(v)
 =sum_rho tau_rho^(2j)exp(-v tau_rho^2).             (1.3)
```

## 2. Gaussian-monomial squares

Define the real entire test function

```text
phi_(j,v)(u)=u^j exp(-vu^2/2).                      (2.1)
```

On the real axis,

```text
|phi_(j,v)(u)|^2
 =u^(2j)exp(-vu^2).                                 (2.2)
```

Let `W` be the centered Weil functional, normalized so that its zero side is

```text
W(h)=sum_rho h(tau_rho).                            (2.3)
```

The Gaussian tests are admissible in the explicit formula.  Equations
(1.3) and (2.2) yield the exact identity

```text
W(|phi_(j,v)|^2)=(-1)^j H_Xi^(j)(v).                (2.4)
```

On the arithmetic side, (2.4) is precisely the archimedean derivative minus
the Laguerre-weighted Gaussian prime sum of E101.037.

## 3. A determining Weil subcone

### Theorem 3.1

The following are equivalent:

```text
(i)  Omega7;

(ii) W(|phi_(j,v)|^2)>=0
     for every j>=0 and every v>0.                  (3.1)
```

### Proof

Under `Omega7`, every `tau_rho` is real, so every summand in (2.4) is
nonnegative.

Conversely, (ii) and (2.4) say exactly that `H_Xi` is completely monotone.
E101.036 gives `Omega7`. `QED`

Thus the Gaussian-monomial squares form a determining subcone of the full
Weil square cone.  Positivity on this subcone is already of full
`Omega7` strength.

## 4. Relation to the earlier Cauchy cone

E70.004 identifies `Omega7` with Weil positivity on Cauchy rational squares.
Theorem 3.1 gives a second determining family:

```text
Cauchy rational squares
       <=> full Weil positivity <=> Omega7
       <=> Gaussian-monomial square positivity.      (4.1)
```

The two families use different coordinates but carry the same force.  The
Gaussian family has the advantage that its arithmetic prime term is the
explicit rapidly convergent sum E101.037(1.4).  It does not turn Weil
positivity into a lower-strength theorem.

## 5. Falsifier behavior

A nonreal `tau_rho` contributes

```text
tau_rho^(2j)exp(-v tau_rho^2),                       (5.1)
```

whose real symmetrization oscillates with `j` and `v`.  E101.037 proves that
arbitrarily many initial inequalities may remain positive before a later
order detects that mode.  Hence truncating the Gaussian subcone at finite
degree destroys its determining property.

## 6. Status

```text
proved:
  exact equality between heat derivatives and Gaussian-square Weil tests;
  Gaussian-monomial squares form an Omega7-determining Weil subcone;
  equivalence with the earlier Cauchy-Weil endpoint;

open:
  arithmetic positivity on the complete Gaussian subcone.
```
