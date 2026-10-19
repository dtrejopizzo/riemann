# R161_066 — Selection of the new arithmetic input after the Green no-go

## 1. Requirements

The new input must not follow merely from `(PC-ren)`, radicality, parity, unitarity or physical compression, since
R161_050 supplies a countermodel for that formal package and R161_061--R161_065 exhaust the Green/power rewritings.
It must use arithmetic data absent from the countermodel and must have a proved terminal implication.

The candidates in R161_051 are compared as follows.

1. Compressed scattering is global and requires the entire exterior history.
2. Active Euler-ideal preservation requires every harmonic of enough active primes; P121 proves its terminal
   overdensity but also proves that local Mobius inversion leaves the root transport block unchanged.
3. Coherent PC saturation is a full second-moment statement and R161_035 leaves precisely its equality law open.
4. Gamma-pole removability requires only one oriented Laurent coefficient at each point `s=2m+1` in the absolutely
   convergent half-plane.

The fourth is therefore the smallest target: its consequence `F=0` is R161_024, and its faithful positive
aggregation is R161_025--R161_026.

## 2. Why local Mobius inversion is not the new input

The causal integer synthesis has an identity atom and a finite local Mobius inverse.  This tempting gap-transport
mechanism is already tested in `P121_CMO_SOURCE_MATRIX_NO_GO`: after elimination, the logarithmic connection has
zero root diagonal and the old annular transport block remains.  The endpoint-regularity variant additionally
produces the uncontrolled global Mobius tail.

Thus safe-half-plane absolute convergence may be used to evaluate a residue, but Mobius inversion cannot be cited
as the equality-state law which makes it zero.

## 3. Oriented Laurent observation

For `s_m=2m+1`, define on a separated finite left port the contour observation

    R_(m,r)[G]
      =(1/(2 pi i)) integral_(|s-s_m|=r) G(s) ds,              (3.1)

where the circle lies in `Re s>1`.  At the completed limit R161_025 gives

    R_(m,r)[zeta W_epsilon^0]
       =zeta(s_m)K_F(2m+1/2).                                 (3.2)

This observation has three features absent from the failed linear graph limit:

- it is applied to one orientation before recombination;
- it is insensitive to every holomorphic finite Euler/hyperbola term;
- it sees exactly the Gamma pole coefficient and nothing else.

Choose positive summable weights

    omega_m=2^(-m)(2m+1/2)e^(-2(2m+1/2)T)/|zeta(2m+1)|^2

and define the oriented contour energy

    E_T^Laur(F)=sum_(m>=1) omega_m
       |R_(m,r_m)[zeta W_epsilon^0]|^2.                       (3.3)

By (3.2), this is exactly `D_T^pole(F)` of R161_025 and is faithful.

## 4. The genuinely new source law

The required input is not the definition (3.3), but a finite source theorem producing its zero:

> **OAL — oriented annihilation law.** There are separated finite port germs `G_(M,N)^-` obtained directly from
> the unrecombined proof of `(PC-ren)` and radii `r_m>0` such that, on every primitive first-contact radical,
>
>     sum_m omega_m |R_(m,r_m)[G_(M,N)^-]|^2 -> 0,             (4.1)
>
> while the same observations converge in the weighted `ell2` topology to those in (3.3).

The R161_050 countermodel does not instantiate OAL because it has neither the positive-odd Gamma pole lattice nor
the arithmetic zeta normalization.  This only passes the typing test; exclusion follows only if (4.1) is actually
proved.  OAL also cannot collapse formally to the completed commutator: contour extraction is performed before
the opposite orientation is added.

If OAL is proved, then `E_T^Laur(F)=0`, hence `D_T^pole(F)=0`, hence `F=0`, and D follows.

## 5. Noncircular construction criterion

To count as a construction rather than a renaming of D, the finite germs in OAL must satisfy all of the following:

1. they are written explicitly from `E_N^ren`, `H_(M,N)^ren` and the polar continuum in `(PC-ren)`;
2. their contour norms vanish from a finite first-contact identity, not from an assumed limiting removability;
3. local uniform control on every contour is proved before passing to the limit;
4. the weighted `m`-sum is dominated by the compact-support estimate of R161_025;
5. no division by zeta on the critical line occurs.

The next construction problem is now sharply finite: find the unrecombined left-port germ and compute its contour
coefficient from `(PC-ren)`.  If that coefficient is merely `K_F(2m+1/2)` with no independent zero mechanism, OAL
has not been proved.

## 6. Status

- comparison and selection of the smallest arithmetic target: **completed**;
- exact contour realization of the faithful Gamma energy: **proved from R161_025**;
- distinction from the three-block formal countermodel: **proved only at the level of typing**;
- finite oriented annihilation law OAL: **open / new objective**;
- D: **open**.
