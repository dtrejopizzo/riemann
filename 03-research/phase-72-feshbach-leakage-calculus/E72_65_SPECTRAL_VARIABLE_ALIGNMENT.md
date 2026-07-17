# E72.65 -- Spectral variable alignment for Mellin divisibility

**Date:** 2026-07-08.
**Role:** remove the notational collision between Mellin exponents and finite CCM spectral variables.

## 0. The collision

Two variables have been denoted by `z` in earlier notes:

```text
1. Mellin exponent:     rho, used in u^rho or (u/x)^rho.
2. CCM spectral height: tau, used in P_x(tau)=-det B_x(tau).
```

They are related by:

```text
rho = 1/2 + i tau,                 tau = -i(rho-1/2).              (ALIGN)
```

The completed zeta divisor in height coordinates is:

```text
Xi(tau)=xi(1/2+i tau).
```

RH says that every zero height `tau` is real. The finite CCM polynomial `P_x(tau)` has real zeros at
each finite `x`.

## 1. Correct form of scalar Mellin divisibility

The scalar WRL resonance variable is the Mellin exponent `rho`:

```text
R_x^{WRL}(s;rho)
 = x^rho L_x(s;x)-int_1^x u^rho partial_uL_x(s;u)du.
```

For comparison with the finite CCM divisor, define the height-parametrized transform:

```text
widehat M_x(s;tau)
 := R_x^{WRL}(s;1/2+i tau).                                      (HM)
```

The divisibility target is:

```text
widehat M_x(s;tau)
 = P_x(tau)A_x(s;tau)+E_x(s;tau).                                (HMSD)
```

not divisibility of `M_x(s;rho)` by `P_x(rho)` without the change of variables.

## 2. Correct endpoint reflected variables

In the LFDC endpoint estimates the exponent is usually written as `z` with `Re z>1/2`. In the
resonance application:

```text
z = rho = 1/2+i tau.
```

Thus:

```text
exp(-(z-1/2)r)=exp(-i tau r).                                    (OSC)
```

For an off-critical zero:

```text
rho=beta+i gamma,
tau=gamma-i(beta-1/2).
```

The endpoint factor has modulus:

```text
|exp(-i tau r)|=exp(-(beta-1/2)r).
```

So the dominant member of an off-critical pair, with `beta>1/2`, is exactly the endpoint-damped member
covered by the `Re z>1/2` estimates.

## 3. Correct low-block statement

The low residue identity E72.64 should be read after the substitution:

```text
rho=1/2+i tau.
```

The finite algebraic divisibility to prove is:

```text
widehat M_x(s;tau)
 = P_x(tau)A_x(s;tau)+E_x(s;tau),                                (DIV-tau)
```

with `tau` complex in compact subsets of the height plane.

At a zeta zero `rho`, the corresponding height `tau_rho=-i(rho-1/2)` satisfies:

```text
Xi(tau_rho)=0.
```

If:

```text
P_x(tau)/P_x(0) -> Xi(tau)/Xi(0)
```

and `(DIV-tau)` holds with normal `A_x` and vanishing `E_x`, then:

```text
widehat M_x(s;tau_rho)->0,
```

which is scalar WRL resonance annihilation.

## 4. Consequence for the proof target

The finite spectral divisor is a divisor in `tau`, not in the raw exponent `rho`.

The corrected target is therefore:

```text
construct a finite reflected Loewner/Feshbach concomitant whose height transform
widehat M_x(s;tau) lies in the determinant ideal (P_x(tau)).
```

This correction does not weaken the route. It prevents the false shortcut:

```text
divide an exponent-plane function by a height-plane polynomial without ALIGN.
```

## 5. Status

```text
corrected: Mellin exponent rho and CCM height tau are distinct variables;
corrected: spectral divisibility is widehat M_x(s;tau) divisible by P_x(tau);
open:      construct the height-plane finite concomitant for widehat M_x.
```
