# E72.312 -- Contour residue form of rotated numerator suppression

**Purpose.** Turn the scalar target `RNS` of E72.311 into a contour theorem. This is the analytic form
of the remaining compact-root obstruction.

No matrix estimates enter here.

## 1. The finite quotient

Use the notation of E72.311:

```text
z=s-1/2,
Q_x(z):=p_x(-z^2)/Delta_x(z),
```

where `p_x` is the pole-even Cauchy numerator and `Delta_x` is the explicit nonzero mesh denominator
after the harmless parity factors have been removed.

For a finite Weyl root `tau`, define

```text
F_{tau,L}(s)
 := (1-e^((s-1/2)L))
    ((s-1/2)tau^2)/(tau^2+(s-1/2)^2)
    Q_x(s-1/2).                                             (1)
```

Then `RNS` is

```text
|R_tau sum_rho F_{tau,L}(rho)| <= C_H L^5                 (2)
```

uniformly for `tau<=H`.

## 2. Residue identity

Let `R_T` be a rectangle in the `s`-plane with vertical sides away from zeros of `Xi` and away from
the finite poles of `F_{tau,L}`. Since `Xi` is entire, the logarithmic derivative `Xi'/Xi` has simple
poles at the nontrivial zeros, with residues equal to multiplicity.

Therefore:

```text
sum_{rho in R_T} m_rho F_{tau,L}(rho)
= (1/2pi i) int_{partial R_T} F_{tau,L}(s) Xi'(s)/Xi(s) ds
 - sum_{a in R_T, a pole of F_{tau,L}}
     Res_{s=a} [F_{tau,L}(s) Xi'(s)/Xi(s)].                 (3)
```

### Proof

Apply the residue theorem to

```text
F_{tau,L}(s) Xi'(s)/Xi(s).
```

The residues at zeros `rho` of `Xi` are `m_rho F_{tau,L}(rho)`. The only other residues come from
the finite poles of `F_{tau,L}`. Moving them to the right side gives (3). `QED`

This is the exact contour version of `RNS`.

## 3. Apparent mesh poles

The quotient `Q_x(z)` may have apparent poles at the Fourier mesh inherited from `D_x(i z)`.
However the full Mellin factor contains

```text
1-e^(zL).
```

At mesh points

```text
z=2pi i n/L,
```

this factor vanishes. E72.306 showed that the normalized Mellin expression is entire at the mesh.
In the present notation this becomes the condition:

```text
MESH-REM:
F_{tau,L}(s) is removable at every mesh pole of Q_x.          (4)
```

Equivalently, all mesh residues in (3) vanish.

This is a finite algebraic condition, not an asymptotic estimate.

## 4. The only genuine finite poles

After `MESH-REM`, the only possible poles of `F_{tau,L}` in a fixed compact height window are the two
kinematic poles

```text
z= i tau,        z=-i tau,
```

coming from

```text
tau^2+z^2.
```

At the finite Weyl root, the numerator condition `p_x(tau^2)=0` is exactly the cancellation of the
corresponding height-plane pole. In the `z` variable this is:

```text
KIN-REM:
Q_x(i tau)=0 and Q_x(-i tau)=0
```

after the same parity normalization.

Thus the compact-root proof needs the following finite cancellation package:

```text
REM:
all finite poles of F_{tau,L} in the compact window are removable.
```

If `REM` holds, (3) reduces to

```text
sum_{rho in R_T} m_rho F_{tau,L}(rho)
= (1/2pi i) int_{partial R_T} F_{tau,L}(s) Xi'(s)/Xi(s) ds.  (5)
```

## 5. Analytic bound sufficient for RNS

Fix a compact root window `tau<=H`. Suppose:

```text
CB1. REM holds for every active finite root tau<=H.

CB2. There are rectangles R_T exhausting the critical strip such that the horizontal integrals in
     (5) tend to zero.

CB3. The vertical integrals obey
     |int_{vertical sides} F_{tau,L}(s) Xi'(s)/Xi(s) ds|
     <= C_H L^5/|R_tau|
     uniformly for tau<=H.
```

Then `RNS` follows.

### Proof

Let `T->infty` in (5). By `CB2`, only the vertical sides remain. By `CB3`, the remaining integral is
`O_H(L^5/|R_tau|)`. Multiplying by `|R_tau|` gives (2). `QED`

## 6. What has to be proved next

The finite algebraic part is now:

```text
REM = MESH-REM + KIN-REM.
```

The analytic part is:

```text
CB = horizontal decay + vertical bound.
```

The compact branch has therefore been reduced to:

```text
REM + CB  =>  RNS  =>  MC-NZ  =>  NZ-MSD  =>  compact-root HPAC decay.
```

This is a real analytic target. It separates:

```text
finite algebra: cancellation of apparent poles;
complex analysis: contour growth of the finite quotient against Xi'/Xi;
arithmetic: only the standard zero-counting logarithmic derivative enters.
```

## 7. Status

```text
proved: exact residue identity (3);
proved: REM + CB imply RNS;
proved: MESH-REM and KIN-REM in the unreduced Cauchy form (E72.313);
open:   prove CB with constants uniform in the fixed compact root window.
```

The remaining lemma is the analytic contour bound `CB`.
