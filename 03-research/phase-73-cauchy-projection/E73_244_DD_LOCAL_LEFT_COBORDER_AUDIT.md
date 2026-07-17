# E73.244 - DD-local left-coborder audit

Date: 2026-07-14.

## 1. Purpose

E73.243 shows that rational denominators chosen by geometric scale do not
produce `CURV-COB`.  This note tests the first module actually derived from
the local CCM divided-difference ideal of E73.015--E73.016.

## 2. Module

For the Cauchy plane at height `gamma`, the two row poles are:

```text
d=gamma,       d=-gamma.
```

The local divided-difference atoms are:

```text
DD_+(d)=DD_L(gamma,d),
DD_-(d)=DD_L(-gamma,d).
```

The natural local denominator is the product of the two poles:

```text
d^2-gamma^2 = d^2+(i gamma)^2.
```

The tested primitive module is:

```text
P_DD(r)
= span{
   D^(2k) DD_±,
   DD_±/(D^2-gamma^2)^m :
   0<=k<=2, 1<=m<=r
 }.
```

This is the local ideal shape from E73.015 specialized to the two Cauchy
poles of the transverse residual.

## 3. Audit

Fit:

```text
rho_a approx Y^*E,      Y in P_DD(r).
```

Measure row norm and scalar pairing against `xi_L`.

## 4. Result

The DD-local module improves some row-norm residuals but still does not
systematically reduce the scalar obstruction.  In trusted small windows, the
scalar pairing remains at the center scale.

Thus the local rational ideal alone is not the missing `CURV-COB` theorem.

## 5. Consequence

The remaining primitive must include the coupled coefficient action of the
finite operator itself.  In other words, `CURV-COB` cannot be proved merely by
choosing a better local rational basis; it must use the exact generated image
of the coupled Gamma-prime cell in that basis and isolate its canonical
quotient, as in E73.163--E73.167.

## 6. Status

```text
tested: DD-local primitive module from the two Cauchy poles;
failed: scalar obstruction remains;
next: construct the canonical quotient of rho_a by the generated DD-local
      image, rather than trying larger ad hoc modules.
```

