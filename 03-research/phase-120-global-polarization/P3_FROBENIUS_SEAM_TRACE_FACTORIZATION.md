# Frobenius seam-trace factorization

Status: exact new factorization of the finite global Green operator by
literal boundary traces of the half-density cylinders.  The final common
phase--Gamma contraction is open.

## 1. Two canonical seam traces

Fix a prime, put

    a=log p,  r=exp(-a/2),  s=sqrt(1-r^2),
    C=rV_a,  x=O_pF=(s(I-C)^(-1))F.                 (1)

The state equation is

    x-Cx=sF.                                        (2)

Define the normalized incoming and outgoing seam traces

    alpha_p(F)=(sqrt(a)/s)x,
    beta_p(F) =(sqrt(a)/s)Cx.                       (3)

Equation (2) gives the exact affine boundary relation

    beta_p=alpha_p-sqrt(a)F=C alpha_p.              (4)

These maps are fixed before the nuclear form: they are the two boundary
values of the half-density transport cylinder, multiplied by the unique
factor which converts its polarized area to `a=log p`.

## 2. Contact is a boundary loss

Since `V_a` is unitary,

    ||alpha_p||^2-||beta_p||^2
      =(a/s^2)(1-r^2)||x||^2
      =a||O_pF||^2.                                (5)

Thus the entire place-Poisson tower, including every `p^j`, is the literal
loss between the two Frobenius seam traces.  Equivalently,

    a(||F||^2-||O_pF||^2)
      =a||F||^2+||beta_p||^2-||alpha_p||^2.         (6)

No tangent feature, pseudoinverse or spectral sign is used in (5)--(6).

The cylinder field

    u_p(sigma,t)=exp(-sigma/2)x(t-sigma),
       0<=sigma<=a,                                 (7)

has boundary values proportional to `alpha_p,beta_p` and solves

    (partial_sigma+partial_t+1/2)u_p=0.             (8)

Formula (5) is therefore Green's formula for an actual first-order piece,
not an algebraic difference invented after row (c).

## 3. New global bank factorization

Summing (6) and adjoining the independently positive Gamma column gives

    A_T=(X_T^seam)^*X_T^seam
          -(Y_T^seam)^*Y_T^seam,                  (9)

where

    X_T^seam F=
      (W_Gamma F,(sqrt(a_p)F)_p,(beta_p(F))_p),

    Y_T^seam F=
      (sqrt(m_0)F,(alpha_p(F))_p).                 (10)

Indeed (9) is exactly

    g_Gamma-m_0+sum_p a_p(I-P_p).                 (11)

Compared with the D.247 reduction, (9) has an important advantage: every
prime entry of both columns is now the trace of the same explicit cylinder
and the landing relation is the literal equation (4).  There is no
unidentified `E_+`/`E_-` tangent boundary.

## 4. Primitive potential compatibility

All operators in (1)--(4) commute with

    L_0=-partial_t^2+1/4.

For `F=L_0G`, put `y_p=O_pG`.  Then

    alpha_p(L_0G)=L_0[(sqrt(a_p)/s_p)y_p],
    beta_p(L_0G) =L_0[(sqrt(a_p)/s_p)C_py_p].       (12)

Consequently the two Tate equations create no additional local seam
condition: they say exactly that the common source `F` has a compact
potential `G`.  The seam equations remain valid on that potential before
support compression.

## 5. Exact remaining transmission

Let `P_T` be the two-Tate primitive projection.  A positive square follows
from a contraction `Theta_T^seam`, constructed as the Calderon map of the
absolute fibre product and the quarter determinant line, satisfying

    Y_T^seam P_T=Theta_T^seam X_T^seam P_T.         (13)

The forbidden move is to define `Theta_T^seam` by (13).  Its prime block is
already fixed by

    beta_p=C_p alpha_p,
    alpha_p-beta_p=sqrt(a_p)F,                      (14)

and its common phase block is fixed by the normalized period map of the
absolute Tate polarization.  Only the attachment of that common phase to
the quarter-Gamma boundary remains to be computed.

For any independently constructed candidate define

    R_T^seam=Y_T^seam P_T
               -Theta_T^seam X_T^seam P_T.         (15)

The residual expansion of
`P3_GLOBAL_SQUARE_BANK_ELIMINATION.md` applies verbatim.  Hence
`R_T^seam=0` gives the global square immediately, while any nonzero seam
profile is the exact obstruction.

The weighted decomposition of all seam variables has now been carried out
in `P3_COHERENT_PARALLEL_SUM_THEOREM.md`.  Because
`alpha-beta=(sqrt(a_p)F)_p`, its primitive component vanishes identically
for the coherent unit vector `w_p=sqrt(a_p/theta)`.  Eliminating that
primitive block produces one explicit strict contraction `C_eff,T` and
collapses the whole prime load to one coherent Poisson observation.

## 6. Classification

- literal seam traces (3)--(4): **CONSTRUCTED**;
- contact boundary-loss identity (5)--(6): **PROVED**;
- positive-minus-positive global seam banks (9)--(11): **PROVED**;
- compatibility with the compact primitive potential (12): **PROVED**;
- common absolute-phase/quarter-Gamma Calderon map: **OPEN**;
- seam transmission identity (13): **OPEN**;
- global square: **OPEN**.
