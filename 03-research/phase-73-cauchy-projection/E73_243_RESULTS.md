# E73.243 results - rational left-coborder audit

Command:

```text
python3 E73_243_rational_left_coborder_audit.py
```

## 1. Summary

The tested module was:

```text
P_rat(r,s)
= span{D^k q_j^*,
       D^k q_j^*/(D^2+beta^2)^m}
```

with fixed geometric betas:

```text
beta in {|w|, 2pi/L, 1}.
```

The audit compared the residual scalar pairing

```text
<rho_a-Y^*E,xi_L>
```

against the original center scale.

## 2. Result

The rational module improves row-norm residuals compared with the polynomial
Cauchy module, but it does not systematically reduce the scalar obstruction.
In several rows it makes the scalar pairing worse.

Typical behavior:

```text
centerB  = L^-15 ... L^-21
resPairB = same scale, sometimes larger
resNormB improves to about L^-9 ... L^-15 in small windows
```

Thus fixed geometric rational denominators are not the `CURV-COB` mechanism.

## 3. Consequence

The next module cannot be chosen by natural scales alone.  It must be derived
from the actual partial-fraction structure of the CCM/Loewner cell:

```text
(F(d_m)-F(d_n))/(d_m-d_n)
```

and the finite Weyl kernel identities.  Otherwise the module sees row geometry
but misses the scalar obstruction.

## 4. Status

```text
rejected: rational Cauchy module with fixed geometric betas;
next: derive primitive denominators from symbolic partial fractions of the
      finite CCM cell action itself.
```

