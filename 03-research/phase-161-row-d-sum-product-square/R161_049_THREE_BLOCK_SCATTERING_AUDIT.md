# R161_049 — Three-block scattering audit: what the completed incoming theorem actually kills

## 1. The three projections

Let

    P_L=1_(-infinity,-T],  P_0=1_(-T,T),  P_R=1_[T,infinity),

up to immaterial endpoint conventions. Let C be the logarithmic cosine transform and let g=P_Rg be the corrected right product port. With the parity convention of R161_021 put

    h=g+epsilon Cg.                                      (1.1)

Its Mellin boundary is the corrected functional-equation defect zeta W_epsilon^0. The desired compressed gate is

    P_R h=0,                                             (1.2)

equivalently P_R Cg=-epsilon g. By the unitary-compression lemma of R161_020, (1.2) implies h=0.

The completed commutator and incoming-current theorem instead give the physical-window equation

    P_0 h=0.                                             (1.3)

Indeed the full completed current decomposes into its local first-contact term and graph-renormalized incoming term, and P121_GRAPH_RENORMALIZED_INCOMING_CURRENT proves that these cancel. This is the center block of the product-port defect. It is not (1.2).

Thus the tempting one-line argument “the completed incoming current proves the compressed scattering equation” changes P_0 into P_R and is invalid.

## 2. Exact algebra after central cancellation

Write

    a=P_R Cg,  b=P_0 Cg,  c=P_L Cg.

Since g is right-supported, (1.3) is exactly b=0. Unitarity gives

    ||a||^2+||c||^2=||g||^2.                            (2.1)

The right scattering error and left leakage are

    e_R=P_Rh=g+epsilon a,
    e_L=P_Lh=epsilon c.                                  (2.2)

Consequently

    ||e_R||^2-||e_L||^2
      =2||a||^2+2epsilon Re<g,a>,                        (2.3)

and

    ||h||^2=||e_R||^2+||e_L||^2
           =2||g||^2+2epsilon Re<g,Cg>.                  (2.4)

No term in (2.1)-(2.4) forces either exterior block to vanish. The missing scalar condition may be taken as

    Re<g,e_R>=0,                                         (2.5)

because R161_021 identifies it, up to the fixed sign convention, with half the square ||(I+epsilon C)g||^2. Equivalently one may prove e_R=0 directly.

## 3. Why the first collar does not add a second algebraic row

In the first chamber 0.8<T<(log 5)/2, R161_012 identifies the initial right collar of g with the finite delay field Y_3 involving 2,3,4. R161_013 proves that differentiating the co-Poisson identity reproduces that same field; it does not supply a second independent equation. The independent relation is the nonlocal Gamma row

    Y_3(F)-tF+r_epsilon=C Q C F

on the inner collar. Converting that row into (2.5), or into vanishing of Y_3 on a nonempty outer collar, remains the precise local task.

## 4. Consequence

The unitary-compression idea is correct and reduces the full scattering problem to (1.2) or (2.5). The existing completed incoming theorem proves the adjacent central condition (1.3). The algebraic gap is therefore a transfer from central cancellation to right-exterior extremality for this arithmetic product port. Generic Sonin functions show that central cancellation and cosine symmetry alone do not make that transfer.

This note neither assumes nor disproves the extra arithmetic transfer. It rules out only the incorrect identification of the two projections. Status: three-block identities proved; exterior transfer open; D open.
