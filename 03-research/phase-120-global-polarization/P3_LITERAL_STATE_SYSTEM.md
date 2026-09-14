# Literal Frobenius--Gamma state system

Status: exact state equations and exact bulk variational identity. Kept out of
paper 42 until the coupled Green square is closed.

## 1. Frobenius states

Put `a_p=log p`, `r_p=p^(-1/2)` and `s_p=sqrt(1-p^(-1))`. The physical
Poisson state is the unique `L^2` solution of

    x_p-r_p V_(a_p)x_p=s_p F,                       (1)

namely `x_p=O_pF`. The arithmetic load and coherent degree profile are

    E_fin(F)=sum_p (log p)||x_p||^2,
    d(F)=sum_p sqrt(log p)x_p.                       (2)

Equation (1) fixes the state before any occurrence of `B_nuc`. Its two
resonant boundary values are the traces `T_p^+F,T_p^-F` already constructed;
on the Real core they are paired isometrically.

## 2. Gamma oscillator states

For `alpha_n=n+1/4`, let `u_n` be the unique `H^1(R)` solution of

    (-d^2/dt^2+4 alpha_n^2)u_n=4 alpha_n^2 F.       (3)

Thus `u_n=R_nF`, with `R_n` the Markov contraction of the quarter-twisted
Gamma reservoir. Define the local positive action

    I_n(F,u)=1/(4 alpha_n^3)
      [||u'||^2+4 alpha_n^2||u-F||^2].              (4)

Completing the square in Fourier space gives the exact variational identity

    inf_(u in H^1) I_n(F,u)
      =alpha_n^(-1)<F,(I-R_n)F>,                    (5)

and the minimizer is exactly (3). Therefore

    ||W_Gamma F||^2=sum_(n>=0) inf_u I_n(F,u).      (6)

This supplies a literal positive bulk Hilbert space and differential for
the entire Gamma term; no square root of the row-(d) operator is being
taken.

## 3. The complete on-shell action

For a finite support window define the positive reference action

    I_ref(F,(u_n))
      =sum_n I_n(F,u_n)+theta_T||F||^2.             (7)

On the solutions of (1) and (3), the exact row-(c) comparison is

    -B_nuc,T(F,F)
      =I_ref(F,(u_n))-m_0||F||^2
       -sum_p(log p)||x_p||^2.                      (8)

The state variables in (8) are constrained by the source equations (1) and
(3); they are not freely varied. Formula (8) is the literal saddle action
whose missing completion must be produced by the global transmission law.

## 4. Primitive potential and first-order bulk column

On the primitive core write `F=L_0G`, with
`L_0=-d^2/dt^2+1/4`. Introduce the Gamma bulk column

    D_Gamma(G)_n=
      (u_n'/(2 alpha_n^(3/2)),
       (u_n-L_0G)/sqrt(alpha_n)),                  (9)

where `u_n` solves (3) with `F=L_0G`. Then

    ||D_Gamma(G)||^2=||W_Gamma L_0G||^2.           (10)

The full desired differential must adjoin a Frobenius/degree column
`D_mix(G)` constructed from (1), D.247 and the Real boundary transmission,
and satisfy the algebraic identity

    ||D_mix(G)||^2
      =theta_T||L_0G||^2-m_0||L_0G||^2
       -sum_p(log p)||x_p(L_0G)||^2.                (11)

Equation (11) is not a definition: its right side is not known positive.
It states the exact result that the transmission calculation must produce.

## 5. The determinant transmission

D.247 shows that all cross-place dependence of the prime state vector is
carried by

    d(F)=sum_p sqrt(log p)x_p(F).                    (12)

The mean-zero resonant boundaries are already paired by the Real
involution. Hence a local or diagonal coupling in `p` cannot change (11),
and a scalar coupling cannot act on the infinite-rank range of (12). The
missing transmission operator must be an operator on the common profile
space `L^2(R_t)` and can enter the state equations only through `d(F)`.

The quarter-phase boundary transmission is now constructed on the Fourier
profile space by

    K_(1/4)=M_(b_infty),                            (13)

and its signed connection is the exact commutator

    K_(1/4)^*QK_(1/4)-Q=M_(g_Gamma-m_0).           (14)

in the Green formula for (3), use (1) and D.247 for the finite boundaries,
and compute the remainder. The route closes only if the resulting on-shell
identity is

    -B_nuc,T(L_0G,L_0G)=||D_Gamma(G)||^2
                         +||D_Frob(G)||^2,          (15)

with `D_Frob` obtained from the interior state variables and no residual.
The prime relative scatterings combine with (13) to give the exact
zero-residual global Green identity proved in
`P3_GLOBAL_SCATTERING_GREEN_IDENTITY.md`. An ordinary Gram realization of
(14) is impossible because its multiplier changes sign; see
`P3_K14_HILBERT_NO_GO.md`.

## 6. Concrete progress and remaining datum

Equations (1)--(10) construct the bulk state space, its differential and all
local equations explicitly. The determinant transmission and the global
Green commutator are now also explicit. The one object still absent is the
positive primitive factor in (15): it must be produced by the matrix-valued
degree/contact completion, not by taking the square root of the already
identified commutator.
