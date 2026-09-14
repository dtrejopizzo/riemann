# Operator-valued degree--Gamma feedback

Status: active construction. This file is deliberately kept out of paper 42
until the final Green square is proved.

## 1. Scalar feedback is excluded exactly

For `a_p=log p`, the relative prime phase has upper-half-plane poles at

    tau_(p,k)=2 pi k/a_p+i/2,  k in Z.

The pole residues are precisely the Fourier coefficients of the resonant
trace `T_p^+` computed in `P3_EXPLICIT_DIRAC_ATTACK.md`. Distinct primes have
disjoint nonzero pole lattices. The two Tate equations cancel only the
`k=0` polar modes. Therefore no scalar Gamma factor and no rank-two Tate
correction can turn the finite relative Euler product into a causal Schur
function. This recovers D.255 at the actual logarithmic frequencies and
explains geometrically why the contact ports must remain matrix-valued.

## 2. Ports fixed before feedback

Let `H=L^2(R_tau)` and, for a finite active prime set `S`, define

    (A_S F)_p
      =sqrt(log p)sqrt(1-p^(-1))
        (I-p^(-1/2)V_(log p))^(-1)F.

Write `q=A_SF in H tensor C^S`, `m=|S|`,

    e_S=m^(-1/2)(1,...,1),
    q_coh=(e_Se_S^*)q,
    q_0=(I-e_Se_S^*)q,
    d=sqrt(m)e_S^*q.

Then, without using `B_nuc`,

    ||A_SF||^2=||q_0||^2+(1/m)||d||^2.            (1)

The source-defined prime load is the left side. D.247 supplies its
conservative tangent realization, while the Bohr assembly and the Real
maps `J_p` now fix the asymptotic realization of the `q_0` boundary. The
unpaid port is the operator-valued coherent map

    C_(S,T): P_T -> H,   C_(S,T)F=d(F),             (2)

not a scalar degree number. D.258 proves that (2) has infinite rank.

## 3. Exact Green target after the canonical split

The place-Poisson identity becomes

    -B_nuc,T(F,F)
      =||W_Gamma F||^2+theta_T||F||^2-m_0||F||^2
       -||q_0(F)||^2-(1/m)||d(F)||^2.              (3)

Every term in (3) is independently defined. The Real boundary theorem
proves that no additional difference of periodic end-state norms must be
added to (3). Thus the required operator-valued feedback has the fixed
input and output columns

    X_coh F=(W_Gamma F,sqrt(theta_T)F),
    Y_coh F=(sqrt(m_0)F,q_0(F),m^(-1/2)d(F)).       (4)

An acceptable Redheffer construction must produce a contraction `Theta_T`
from the quarter-twisted determinant connection, the D.247 port rotation
and the Real Bohr boundary, satisfying

    Y_coh P_T=Theta_T X_coh P_T.                    (5)

Defining `Theta_T` by (5) is forbidden. Its state equations must be written
from those three source systems first. If that is done, the unitary system
identity gives

    -B_nuc,T|P_T
      =(X_coh P_T)^*(I-Theta_T^*Theta_T)(X_coh P_T). (6)

## 4. What the new boundary calculation actually removes

Before the resonant-trace calculation, a bilateral realization left an
uncontrolled term `||x_-^0||^2-||x_+^0||^2`. For the physical Poisson
resolvents this term is now zero on the Real core because

    x_-^0=J_B x_+^0.

Hence the final state equations need no free unitary on the prime defect
complements. They must retain `q_0` as the positive contact output and wire
only the coherent `H`-valued channel through the Gamma determinant system.

## 5. Next literal calculation

Let `U_Gamma=F^(-1)M_(b_infty)F` be the quarter-twisted determinant
scattering and let `U_DC` be the source-range partial isometry of D.247 after
the coherent/primitive split. The remaining construction is a block system

    U_global = Redheffer(U_Gamma,U_DC; C_(S,T)),     (7)

where the internal port is `H`, not `C`. The calculation is accepted only if
the feedback inverse in (7) is obtained from the strict local contractions
and the compact support core, and its eliminated external columns are
exactly (4). The first unmatched term is the Maslov residual; it may not be
renamed or absorbed.

Equation (7), followed by direct block elimination, is the active proof
task. No scalar Euler cascade, numerical gate, pseudoinverse or separately
estimated Gamma/arithmetic budget is admissible.
