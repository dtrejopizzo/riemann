# E72.359 - Double-residue CFIR certificate

## 1. Purpose

E72.356--E72.358 reduced the remaining Phase 72 obstruction to:

```text
CFIR-DIV:
Delta(z,w) in (Z(z),Z(w))
```

locally on every finite Xi-zero window.  E72.357 proved that this is equivalent to finite Hermite
Taylor-block vanishing.

This note packages the same condition as a double-residue identity.  This is the most explicit
finite form for auditing because it turns every local ideal condition into a contour coefficient.

## 2. Local residue projectors

Let `a` be a zero of `Z` of multiplicity `m`:

```text
Z(z)=(z-a)^m U_a(z),        U_a(a) != 0.
```

For a holomorphic germ `F`, define the local coefficient projector

```text
Pi_{a,r}[F]
:= Res_{z=a} F(z) dz / ((z-a)^{r+1} U_a(z)),
        0<=r<m.                                      (1)
```

Since `Z(z)=(z-a)^mU_a(z)`, this can also be written as

```text
Pi_{a,r}[F]
= Res_{z=a} (z-a)^{m-r-1} F(z) dz / Z(z).            (2)
```

It extracts the Taylor coefficient of `(z-a)^r` in `F` modulo `(z-a)^m`.

## 3. Double projector

For a two-variable holomorphic germ `Delta(z,w)` and zeros `a,b` of multiplicities `m,n`, define

```text
Pi_{a,r;b,s}[Delta]
:= Res_{z=a} Res_{w=b}
   (z-a)^{m-r-1}(w-b)^{n-s-1}
   Delta(z,w) dz dw / (Z(z)Z(w)).                    (3)
```

for

```text
0<=r<m,      0<=s<n.
```

## 4. The certificate

The local ideal condition

```text
Delta in (Z(z),Z(w))
```

is equivalent to

```text
Pi_{a,r;b,s}[Delta]=0
```

for every `0<=r<m`, `0<=s<n`.

### Proof

Write

```text
Delta(z,w)=sum c_{p,q}(z-a)^p(w-b)^q.
```

Substituting into (3) and using

```text
Z(z)=(z-a)^mU_a(z),        Z(w)=(w-b)^nV_b(w),
```

shows that `Pi_{a,r;b,s}` extracts the coefficient `c_{r,s}` after multiplying by the invertible
unit expansions `1/U_a`, `1/V_b`.  The full rectangular family of projectors is therefore an
invertible triangular transform of the Taylor block

```text
{c_{p,q}: 0<=p<m, 0<=q<n}.
```

Thus all projectors vanish if and only if the forbidden Taylor block vanishes.  By E72.357, this is
equivalent to membership in `(Z(z),Z(w))`.  `QED`

## 5. CFIR application

For the CFIR compatibility minor

```text
Delta_{alpha,beta}(z,w)
= X(z)Y(w)-X(w)Y(z),
```

the exact finite certificate becomes:

```text
DCERT-CFIR:
Pi_{a,r;b,s}[Delta_{c,d}]=O_T(L^B)
```

for every zero pair `(a,b)` in the finite window, every multiplicity slot `r,s`, and every adjugate
column pair `c,d`.

Exact closure is the special case where all these projectors vanish.

## 6. Finite contour form

Let `gamma_a,gamma_b` be small circles around `a,b`, containing no other zeros.  Then (3) is

```text
Pi_{a,r;b,s}[Delta]
= (1/(2pi i)^2)
  int_{gamma_a} int_{gamma_b}
  (z-a)^{m-r-1}(w-b)^{n-s-1}
  Delta(z,w)/(Z(z)Z(w)) dw dz.                       (4)
```

Thus `DCERT-CFIR` is a finite list of local contour integrals.  There is no limiting zero tail and no
absolute prime sum in this statement.

## 7. Relation to SCALAR-CONS

Once all double residues vanish, E72.358 gives a scalar `Lambda_*` compatible with the Xi-window
residual.  The remaining scalar gate is independent:

```text
SCALAR-CONS:
Lambda_* = Lambda_L + O_T(L^B).
```

The double-residue certificate proves collinearity; it does not by itself identify the scalar with
the Feshbach left coefficient.

## 8. Status

```text
proved: local ideal membership is equivalent to vanishing double residue projectors;
specified: DCERT-CFIR as a finite list of local contour integrals;
open: prove the DCERT-CFIR projectors vanish for the exact CFIR Delta;
open: prove SCALAR-CONS.
```
