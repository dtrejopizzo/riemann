# E72.314 -- Sine-quotient bound gate for the compact contour

**Purpose.** Identify the exact analytic estimate which closes the compact contour bound `CB` from
E72.312 after the finite removability lemma E72.313.

This is the first place where the exponential off-line pressure is visible in pure analysis.

## 1. The dangerous factor

The compact contour kernel is

```text
F_tau(s)
= (1-e^(zL)) z tau^2/(tau^2+z^2) C_x(iz),
z=s-1/2.
```

On a vertical line `Re z=sigma>0`, the factor `1-e^(zL)` is of size `e^(sigma L)`. Therefore a
generic Cauchy transform bound for `C_x(iz)` is useless. The required estimate is not:

```text
|C_x(iz)| <= polynomial.
```

It is the stronger sine-quotient cancellation:

```text
SQB(sigma,H):
sup_{|Re z|<=sigma, dist(z,mesh)>=c/L}
|(1-e^(zL)) C_x(iz)|
<= A_{sigma,H} L^B (1+|Im z|)^B.                            (1)
```

The finite mesh removability of E72.313 is the local version of (1). `SQB` is the global strip version.

## 2. SQB implies CB

Fix `sigma in (0,1/2)` and a compact root window `tau<=H`. Let `R_T` be the rectangle in the shifted
variable `z=s-1/2`:

```text
|Re z|<=sigma,        |Im z|<=T,
```

with vertical sides avoiding zeros of `Xi`.

Assume:

```text
SQB.  (1) holds on the two vertical sides and on the horizontal sides.

LOG.  On the contour,
      Xi'(1/2+z)/Xi(1/2+z)=O_sigma(log(2+|Im z|))
      away from small zero-avoidance detours.

TAIL. The horizontal integrals vanish as T->infty after the standard zero-avoidance selection.
```

Then

```text
CB:
|int_{partial R_T} F_tau(s)Xi'(s)/Xi(s)ds|
<= C_{sigma,H} L^B
```

for the compact window, after letting `T->infty`.

### Proof

The rational kinematic factor satisfies, uniformly for `tau<=H` away from its removable points,

```text
|z tau^2/(tau^2+z^2)| <= C_{sigma,H}(1+|z|)^(-1)
```

on the vertical sides and is locally bounded at `z=+-i tau` by E72.313. Thus `SQB` gives

```text
|F_tau(1/2+z)| <= C_{sigma,H} L^B(1+|Im z|)^{B-1}.
```

Multiplying by `LOG` gives a polynomial integrand on vertical segments. The finite-height compact
version used in E72.303 only needs the contour portion that encloses zeros in a fixed height slab, so
the vertical contribution is `O_{sigma,H}(L^B)`. In the full-height version, `TAIL` and the usual
zero-avoidance rectangles supply the limiting contour. Hence `CB` follows. `QED`

## 3. What SQB really says

Using

```text
C_x(iz)=P_x(iz)/D_x(iz),
```

the dangerous product is

```text
(1-e^(zL))C_x(iz)
= (1-e^(zL)) P_x(iz)/D_x(iz).                              (2)
```

Since the mesh denominator has zeros at `z=-id_m`, the factor `1-e^(zL)` is the exact sine-type
factor with the same zero lattice. Thus (2) is a finite sine quotient.

So the remaining compact theorem is:

```text
Finite Sine-Quotient Bound:
the finite Cauchy numerator P_x does not destroy the cancellation between the exponential endpoint
factor and the Fourier mesh denominator.
```

This is analytic and finite. It is stronger than real-root divisibility and weaker than RH: it speaks
only about the explicit finite CCM ground vector and its Cauchy numerator.

## 4. Why this is not a numerical matrix problem

`SQB` can be attacked by:

```text
1. product comparison:
   compare D_x(iz)/(1-e^(zL)) to the canonical sine product on the Fourier mesh;

2. numerator growth:
   bound P_x(iz) by a Markov/Cartwright estimate from its real finite divisor and normalization;

3. residue control:
   use the explicit Cauchy residues xi_m to rule out hidden exponential growth between mesh points.
```

No Schatten norm or finite matrix eigenvalue enters the statement.

## 5. Current reduced chain

The compact branch is now:

```text
SQB + LOG + TAIL
=> CB
=> RNS
=> MC-NZ
=> NZ-MSD
=> fixed-height compact-root HPAC decay.
```

`LOG` and `TAIL` are standard contour bookkeeping for `Xi'/Xi`. The new mathematics is `SQB`.

## 6. Status

```text
proved: SQB implies CB on compact root windows;
open:   prove SQB for the finite CCM Cauchy numerator.
```

The next analytic target is a product estimate for `(1-e^(zL))/D_x(iz)` and a Cartwright-type
normalization bound for `P_x(iz)`.
