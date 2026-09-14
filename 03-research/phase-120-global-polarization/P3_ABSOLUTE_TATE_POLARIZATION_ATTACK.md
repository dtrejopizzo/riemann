# Absolute Tate polarization attack

Status: the local contact metric and the coherent/primitive prime split are
derived from the absolute Tate curves.  The determinant-Calderon comparison
on the resulting fibre product remains open.

## 1. The new geometric input

For every prime `p`, Connes--Consani construct the complex Tate curve

    E_p=C^x/p^Z

and prove the canonical real decomposition

    E_p=C_p x X_infty_tilde,
    C_p=R_+^x/p^Z,                                  (1)

where the phase circle `X_infty_tilde` is independent of `p`.  Put
`s=log(lambda)`, `a_p=log p` and let `theta` have period `2 pi`.  Their
canonical holomorphic differential is

    omega_p=ds+i dtheta.                             (2)

No row-(c) or row-(d) datum enters (1)--(2).

## 2. Principal polarization gives exactly the contact mass

Orient `E_p` by `ds wedge dtheta`.  Direct calculation gives

    omega_p wedge conjugate(omega_p)
      =-2i ds wedge dtheta,

and hence

    (i/(4 pi)) integral_(E_p)
       omega_p wedge conjugate(omega_p)
      =(1/(2 pi)) integral_0^(a_p)ds integral_0^(2pi)dtheta
      =a_p=log p.                                   (3)

Therefore the principal Hodge metric on a profile-valued harmonic form
`z_p omega_p` is

    ||z_p omega_p||_pol^2=(log p)||z_p||_H^2.       (4)

Summing (4) over the active places gives exactly, without a fitted
normalization,

    sum_p (log p)||z_p||_H^2.                       (5)

This is the contact output of D.247 and the physical Poisson load when
`z_p=O_pF`.  Thus the torsion coefficient `log p` is the normalized area
of the absolute complex Tate curve, not an imposed arithmetic weight.

## 3. The common-phase fibre product

For a finite active set `S`, form the source-defined real fibre product

    E_S^abs=product_(X_infty_tilde,p in S) E_p
           =(product_(p in S) C_p) x X_infty_tilde. (6)

The phase differential `dtheta` occurs only once in (6).  In the
polarization-normalized contact coordinates

    q_p=sqrt(log p) z_p,                             (7)

the covector paired with the common phase is

    delta_S(q)=sum_p q_p
              =sum_p sqrt(log p) z_p.              (8)

Equation (8) is exactly the D.247 arithmetic degree.  It is also the
normalized sum of the arithmetic periods of the forms `z_p omega_p`.
Thus the three objects

    common absolute phase,
    coherent contact covector,
    arithmetic degree

are the same source functional, now for a geometric reason.

Let `m=|S|`, `e_S=m^(-1/2)(1,...,1)` and split

    q=e_Se_S^*q+(I-e_Se_S^*)q.                     (9)

Then the principal metric (5) gives

    sum_p (log p)||z_p||^2
      =||q_0||^2+(1/m)||delta_S(q)||^2.            (10)

The first summand is the vertical primitive polarization of the fibre
product; the second is its sole phase-coherent direction.  Formula (10)
is precisely D.256, but (6) now explains why there is one coherent line
and why its orthogonal complement is canonical.  No unitary extension of
the D.247 source range has been chosen.

## 4. Quarter holonomy and the physical return

On the arithmetic cycle of length `a_p`, the half-density connection has
return holonomy

    r_p=exp(-a_p/2)=p^(-1/2).                      (11)

Its source equation on the covering profile is

    x_p-r_pV_(a_p)x_p=sqrt(1-r_p^2)F,              (12)

so its normalized observation is exactly `x_p=O_pF`.  Combining (3) and
(12), the polarized norm of the returned absolute-Tate state is

    ||x_p omega_p||_pol^2
       =(log p)||O_pF||^2.                         (13)

Hence both ingredients of every finite contact term--the determinant mass
and the complete Frobenius tower--are recovered from the same polarized
Tate cylinder.

There is also a literal positive cylinder bulk, not merely a resolvent
notation.  On `[0,a_p] x R_t` put

    u_p(s,t)=exp(-s/2)x_p(t-s).                     (14)

It satisfies the flat transport equation

    (partial_s+partial_t+1/2)u_p=0,

and the literal Green formula for `D_p=partial_s+partial_t+1/2` is

    2 Re <D_pu,u>_cyl
      =||u(a_p,.)||^2-||u(0,.)||^2+||u||_cyl^2.    (15)

and its two seam values obey

    u_p(0)=x_p,
    u_p(a_p)=r_pV_(a_p)x_p=x_p-sqrt(1-r_p^2)F.      (16)

Moreover

    integral_0^(a_p)||u_p(s,.)||^2 ds
       =(1-r_p^2)||x_p||^2.                        (17)

Equations (15)--(17) give the boundary identity

    ||x_p||^2-||x_p-sqrt(1-r_p^2)F||^2
       =(1-r_p^2)||x_p||^2.                        (18)

Therefore the complete contact energy is the independently positive bulk

    (log p)||O_pF||^2
      =a_p/(1-r_p^2)
         integral_0^(a_p)||u_p(s,.)||^2 ds.        (19)

The minus sign of the contact term in the global Green form is consequently
an inner-boundary orientation; it is not a negative local metric.

## 5. What this removes from the global-square problem

The boundary complement in D.247 was previously arbitrary outside its
source range.  Equations (6)--(10) supply its geometric carrier:

    H_bd,S=
      [direct-sum_p L2_0(C_p)]
       direct-sum [H_coh x X_infty_tilde].          (20)

The first block has the Real involution already constructed from the
opposite Frobenius traces.  The second block is forced to couple to the
quarter determinant connection because all `E_p` share the same phase
circle.  Thus an admissible transmission can no longer be changed by an
arbitrary unitary on defect complements.

The remaining operator is the Calderon map of the half-density connection
on (6), with the quarter determinant line on the common phase and the two
compact-potential exterior conditions.  Denote this source-defined map by
`Theta_abs,T`.  The exact comparison still required is

    Y_red P_T=Theta_abs,T X_red P_T.                (21)

Unlike a Douglas definition, the proposed domain of `Theta_abs,T` is fixed
by (6), (11), the Real involution and the quarter holonomy.  What is not yet
proved is that the closure of this proposed domain exists with the stated
trace, or that its Green trace is exactly the tangent landing `E_-/E_+` in
(21), with no additional phase mode.  Accordingly (20) is a canonical
candidate carrier, not yet a completed Calderon space.

## 6. Sharp next calculation

Cut each `C_p` at its Frobenius seam and write the first-order
half-density operator `partial_s+1/2` on the resulting cylinder.  Glue all
phase boundaries through the single `X_infty_tilde`, impose Kirchhoff
conservation in the normalized period coordinate (8), and compute Green's
formula.  There are only two possible outcomes:

1. its boundary columns are exactly `X_redP_T,Y_redP_T`; then (21) follows
   from the Calderon contraction and the residual theorem gives the global
   square;
2. an extra phase trace remains; that trace is the literal obstruction and
   this absolute-Tate realization fails without retuning.

## 7. Classification

- canonical absolute Tate carrier (1)--(2): **CONNES--CONSANI**;
- contact coefficient `log p` from principal polarization (3)--(5):
  **PROVED**;
- common phase equals normalized arithmetic degree (6)--(10): **PROVED**;
- half-density holonomy produces the physical Poisson state and the literal
  positive cylinder bulk (11)--(19): **PROVED**;
- canonical candidate carrier for the D.247 complement (20): **FIXED;
  CLOSURE AND TRACE THEOREM OPEN**;
- exact Calderon/tangent comparison (21): **OPEN**;
- global square: **OPEN**.
