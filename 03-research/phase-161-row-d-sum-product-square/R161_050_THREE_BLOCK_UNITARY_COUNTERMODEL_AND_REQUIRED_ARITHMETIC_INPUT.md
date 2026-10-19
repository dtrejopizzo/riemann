# R161_050 — Three-block unitary countermodel and the required arithmetic input

## Purpose

R161_049 distinguishes the central cancellation already proved from the right-exterior scattering gate. The following exact model tests whether unitarity, the central gap and the scattering parity can perform that transfer algebraically.

## Model

Let H=C^3 with orthonormal basis e_L,e_0,e_R and projections onto the three coordinate lines P_L,P_0,P_R. Define the selfadjoint unitary

    C e_L=e_R,  C e_R=e_L,  C e_0=e_0,

and take g=e_R. For either epsilon in {+1,-1}, put

    h_epsilon=g+epsilon Cg=e_R+epsilon e_L.

Then

    g=P_Rg,
    C=C*=C^(-1),
    P_0 h_epsilon=0,
    C h_epsilon=epsilon h_epsilon.

Thus h_epsilon has the exact central gap and scattering parity of the three-block residual. Nevertheless

    P_R h_epsilon=e_R !=0,

and

    P_R Cg=0 != -epsilon g.

The leakage and right error have equal nonzero norm. This realizes equations (2.1)-(2.4) of R161_049 exactly.

## Consequence

There is no theorem of the form

    central cancellation + selfadjoint unitarity + scattering parity
       => right compressed scattering.

Therefore the last implication cannot be a missing manipulation of those three facts. A valid proof must use a property excluding this model. In the present corpus the available equivalent arithmetic properties are:

1. physical co-Poisson range membership of the product port (R161_012);
2. removability of the corrected defect at the positive odd Gamma poles (R161_024);
3. vanishing of the faithful Gamma residue energy (R161_025-R161_026);
4. preservation of the finite active Euler ideals (P121_ACTIVE_EULER_IDEAL_OVERDENSITY);
5. an exterior PC Green/reciprocity identity producing the extremal correlation (R161_021-R161_023).

Each property already implies exclusion of first contact by a proved downstream theorem. None is derived by the central cancellation itself.

This countermodel does not reproduce the integer translation semigroup, the explicit zeta product port, or the Gamma/Tate collars. It therefore does not refute a physical theorem using those data. It does refute calling the remaining transfer purely algebraic unless the alleged algebra explicitly contains one of those physical structures.

Status: finite countermodel proved by direct matrix multiplication; purely three-block algebraic closure rejected; arithmetic exterior transfer and D open.
