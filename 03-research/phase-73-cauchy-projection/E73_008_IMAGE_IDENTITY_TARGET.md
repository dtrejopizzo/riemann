# E73.008 - Image identity target for the structured primitive

## 1. Purpose

E73.007 gives strong numerical evidence that the source `S_b` lies almost in the image of
`C_E-mu I` on a small rational/divided-difference class.  This note states the symbolic identity that
would turn that evidence into a proof.

## 2. The finite class

For off-line projection nodes `beta` and critical heights `gamma`, define

```text
Y_{gamma,beta,r}(d)
= DD_L(-gamma,d)/(d^2+beta^2)^r,       r>=1.
```

Let

```text
RAT-DD_p(O,K)=span{Y_{gamma,beta,r}: gamma in K, beta in O, 1<=r<=p}.
```

E73.007 tests `p=1,2,3`.

## 3. Desired image identity

For each off-line node `b`, prove that there are explicit coefficients

```text
c_{gamma,beta,r}(b)
```

such that, with

```text
Y_b=sum c_{gamma,beta,r}(b)Y_{gamma,beta,r},
```

one has

```text
(C_E-mu I)Y_b
= S_b - R_b,                                         (1)
```

where `R_b` is a finite linear combination of endpoint and high-frequency packet residuals already
controlled by Phase 72:

```text
D2BV/SFREQ residuals,
natural-height outside-zero residuals,
finite Fourier tail residuals.
```

The required bound is:

```text
e^(Re b L)|<xi,R_b>| <= L^B.                          (2)
```

## 4. Why coefficients must be explicit

Least-squares coefficients are not a proof object.  The coefficients must be obtained by applying the
coupled operator identity

```text
C_E = W02 - WR - Prime - e_pole I
```

to `Y_{gamma,beta,r}` and using the same Cauchy/Loewner divided-difference algebra that produced
E72.318--E72.321.

The proof must keep

```text
W02 - WR - Prime
```

coupled until the final residual.  Splitting the three terms by absolute values would return to the
incoherent ceiling.

## 5. Finite verification form

The exact algebra can be checked at finite `L` by verifying the row identity

```text
S_b - (C_E-mu I)Y_b
```

against the explicit residual basis.  This creates a finite certificate:

```text
coefficients c_{gamma,beta,r}(b),
residual coefficients in the Phase 72 residual basis,
interval bounds for <xi,R_b>.
```

## 6. Status

```text
current endpoint: IMAGE-ID, the structured image identity (1);
proved sufficient: IMAGE-ID => SRC-COB => NAT-SRC => NAT-PROJ;
open: derive explicit coefficients from the coupled C_E action on RAT-DD_p.
```

