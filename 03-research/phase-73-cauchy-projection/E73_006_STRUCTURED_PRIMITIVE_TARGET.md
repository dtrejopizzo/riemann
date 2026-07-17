# E73.006 - Structured primitive target

## 1. Purpose

E73.005 shows that an unrestricted coborder is tautological but numerically compatible with polynomial
control.  The next proof object must replace the pseudoinverse primitive by an explicit primitive in
the rational/divided-difference class.

## 2. Source

For each off-line representative `b`, E73.003 gives

```text
S_b(d_m)=sum_{k=i gamma in K_L} Pi(b,k)DD_L(-gamma,d_m).
```

The remaining source is

```text
SRC_b=<xi,S_b>.
```

## 3. Structured primitive equation

Find an explicit finite kernel `Y_b(d_m)` such that

```text
(C_E-mu I)Y_b = S_b - R_b,                            (1)
```

where:

```text
Y_b belongs to RAT-DD_L(O,K),
R_b is a finite endpoint/high-frequency remainder,
e^(Re b L)|<xi,R_b>| <= L^B.
```

Then:

```text
<xi,S_b>=<xi,R_b>,
```

and `NAT-SRC` follows.

## 4. What the primitive must use

The operator is

```text
C_E = W02 - WR - Prime - e_pole I.
```

The primitive should be built before splitting these terms by absolute values.  The intended identity
has the form:

```text
(W02-WR-Prime-e_pole-mu)Y_b
= S_b + endpoint terms + high-frequency terms.        (2)
```

The endpoint/high-frequency terms are exactly the classes already controlled in Phase 72:

```text
D2BV/SFREQ,
natural-height outside tail,
finite Fourier tail absorption.
```

## 5. First ansatz

Because

```text
DD_L(u,d)=[e^(-idL)-e^(-iuL)]/(u-d),
```

and because the CCM cells are Cauchy/Loewner kernels in the pole mesh, the primitive should be a
one-order-higher divided difference:

```text
Y_b(d)
=sum_{k=i gamma in K_L} Pi(b,k)
  [ DD_L(-gamma,d)/(lambda_b(d)) ],
```

where `lambda_b(d)` is not a fitted scalar but the finite symbol produced by the coupled operator
`W02-WR-Prime-e_pole-mu` acting on the divided-difference family.

The next calculation must derive `lambda_b(d)` from the actual matrix action, not choose it by least
squares.

## 6. Status

```text
target: explicit structured primitive identity (1);
open: derive the action of C_E-mu on RAT-DD_L(O,K) without splitting W02, WR, and Prime incoherently.
```

