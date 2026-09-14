# Derived arithmetic theta: the spectral-parameter gate

Status: the proposed connected arithmetic-theta height does not furnish the
row-(d) square.  The obstruction is the location of the spectral parameter,
not the local Euler/Gamma calculation.

## 1. The two parameters are different

An incoherent Eisenstein series has the form

    E(g,s,Phi).                                     (1)

Arithmetic Siegel--Weil differentiates in the induction parameter `s` at a
fixed special point `s_0` and identifies Fourier coefficients in the
automorphic variable `g=g_z`, `z=x+iy`, with arithmetic heights:

    E'(g_z,s_0,Phi)
      =sum_m height(Z(m),Phi) W_m(y,s_0)e^(2 pi i m x). (2)

For fixed arithmetic cycles, `height(Z_1,Z_2)` is a scalar.  It has no
critical-line parameter `tau`.  The `z` in (2) is the modular variable of a
generating series; it is not the spectral parameter in

    A_T(tau)=Re psi(1/4+i tau/2)-log pi-prime terms. (3)

Thus evaluating the arithmetic pairing itself cannot produce (3).

## 2. Where a tau can be manufactured

One may Mellin transform the `y` variable in (2):

    M_E(u)=int_0^infinity E'(iy,s_0,Phi)y^(u-1)dy.  (4)

Putting `u=u_0+i tau` makes (4) nonconstant in `tau`.  But (4) is the
Rankin--Selberg/Mellin transform of the *height generating series*.  Its
Dirichlet coefficients are the arithmetic intersection numbers in (2), not
the von Mangoldt coefficients of one fixed zeta function.  It therefore
produces a new L-function attached to the height series, not the boundary
logarithmic derivative (3).

Moreover the weights `y^(i tau)` are oscillatory.  Negative definiteness of
the arithmetic height pairing gives a sign before (4), on each primitive
cycle class.  It gives no pointwise sign for the Mellin transform (4).
Consequently nonconstant `tau`-dependence exists, but it is in the wrong
slot and the Hodge sign does not pass through it.

## 3. The only possible repair and its no-go

The only way to put `tau` inside the signed pairing is to form a family of
classes such as

    Z_tau(F)=sum_m F(m)m^(-i tau) Z(m)              (5)

and use

    -<Z_tau(F),Z_tau(F)>_Ar>=0.                     (6)

Equation (6) is genuinely `tau`-dependent.  Its kernel, however, is

    sum_(m,n) F(m)conj(F(n))(m/n)^(-i tau)
       <Z(m),Z(n)>_Ar,                              (7)

so matching (7) with `A_T(tau)` requires an additive map from the complete
primitive test space into a space with at most one positive direction whose
pairing realizes or dominates the Weil form.  By the amended Gap G-1
(`114_d3_03`, Theorem 6.5, cited in
`114_d3_01_THE_IMPORTED_INDEX_THEOREMS.md`), existence of any such linear
map is already equivalent to row (d).  Choosing the cycles to force the
match would therefore insert the conclusion.

On a fixed arithmetic surface there is also the finite-rank obstruction of
Gap G-2: the algebraic degree-zero part cannot carry the infinite-rank
prime-contact block.  Allowing arbitrary Green metrics removes literal
finite rank but returns exactly to the unconstructed place-wise compatible
map of G-1/G-3.

## 4. Verdict

- local logarithmic derivatives give `log p` and the quarter-Gamma term:
  **TAUTOLOGICAL TATE IDENTITIES, NOT GATES**;
- the arithmetic height pairing itself: **INDEPENDENT OF tau**;
- Mellin transform of its generating series: **NONCONSTANT IN tau, BUT A
  DIFFERENT L-FUNCTION AND NO INHERITED POINTWISE SIGN**;
- inserting `tau` in a family of cycle classes: **RETURNS TO THE
  RH-EQUIVALENT LINEAR REALISATION OF G-1**;
- connected arithmetic-theta route to the global square: **CLOSED
  NEGATIVELY**.

The useful lesson is precise: a viable global polarization must carry the
critical-line spectral parameter *internally in its zero-carrying
cohomology*.  A generating series of Arakelov heights carries it only as an
external Mellin variable and therefore remains on the special-value side of
the Attempt-6 separation.
