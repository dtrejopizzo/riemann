# E73.014 - Local action intertwiner

## 1. Purpose

E73.013 defines the local Cauchy ideal.  This note tests whether the coupled finite operator

```text
C_E-mu I
```

maps a primitive local ideal into a source local ideal.

## 2. Primitive and source ideals

The first attempt used only

```text
DD_L(-gamma,d)/(d^2+beta^2)^r,        r=1,2.
```

That did not close the action well enough.  The successful finite class includes endpoint/polynomial
pieces:

```text
Primitive:
DD_L(-gamma,d)/(d^2+beta^2)^r,        r=0,1,2,
d^2 DD_L(-gamma,d).

Source:
DD_L(-gamma,d)/(d^2+beta^2)^r,        r=0,1,2,3,
d^2 DD_L(-gamma,d),
d^4 DD_L(-gamma,d).
```

These added terms are natural: applying the finite operator to a rational divided difference produces
both higher denominator powers and endpoint/polynomial remnants.

## 3. Intertwiner target

Let

```text
P_{O,K}:=Primitive local ideal,
S_{O,K}:=Source local ideal.
```

The finite action target is:

```text
LOCAL-ACT:
(C_E-mu I)P_{O,K} subset S_{O,K} + Phase72Residual.
```

The numerical probe shows the image is captured by `S_{O,K}` to `10^-8`--`10^-7` relative error in the
tested windows.

## 4. Consequence

Together with E73.010, this gives the right proof architecture:

```text
S_b in S_{O,K},
S_b lies in the subspace (C_E-mu I)P_{O,K} modulo residuals,
residuals pair polynomially with xi.
```

Thus the endpoint is now an **intertwining identity between two explicit finite local ideals**, not a
least-squares coefficient problem.

## 5. Status

```text
observed: local action closes after adding r=0 and polynomial endpoint generators;
current proof target: prove LOCAL-ACT symbolically from the coupled W02-WR-Prime action.
```

