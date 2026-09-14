# Paley--Wiener Julia-short candidate

Status: the source-defined candidate is automatically contractive but fails
the primitive intertwining gate at `T=log 2`.  It is retired.  No square root
of `A_T` and no Douglas contraction was used.

## 1. The two passive systems and their normalized defects

Use the independently constructed positive-real impedances

    Z_X=H_Gamma+theta,
    Z_Y=m_0+theta H_S,                              (1)

and their Cayley transfers

    S_X=(Z_X-1)/(Z_X+1),
    S_Y=(Z_Y-1)/(Z_Y+1).                            (2)

Both are Schur functions in the right half-plane.  If

    X=(W_Gamma,sqrt(theta)I),
    Y=(sqrt(m_0)I,sqrt(theta)O_eff),                 (3)

define the vector defect multipliers

    E_X=2X/(Z_X+1),
    E_Y=2Y/(Z_Y+1).                                 (4)

The positive-real identities give, on the boundary,

    E_X^*E_X=I-S_X^*S_X,
    E_Y^*E_Y=I-S_Y^*S_Y.                            (5)

Every object in (1)--(5) is constructed from the Gamma oscillators and the
effective Frobenius return before row (c) is evaluated.

## 2. Finite-horizon defect landings

Let `P_T` be the orthogonal projection onto the Paley--Wiener/model space
corresponding in time to the interval `(-T,T)`, and put

    T_X=P_T M_(S_X) P_T,
    T_Y=P_T M_(S_Y) P_T.                            (6)

These are contractions.  Their defect operators are

    D_X=(I-T_X^*T_X)^(1/2),
    D_Y=(I-T_Y^*T_Y)^(1/2).                         (7)

The square roots in (7) are admissible: their arguments are positive by the
already proved Schur property of the separate passive systems, not by the
desired sign of `A_T`.

More importantly, their physical landings are explicit.  For `h` in the
window model space set

    delta_X h=(M_(E_X)h,(I-P_T)M_(S_X)h),
    delta_Y h=(M_(E_Y)h,(I-P_T)M_(S_Y)h).           (8)

Then

    ||delta_X h||^2=||h||^2-||T_Xh||^2=||D_Xh||^2,
    ||delta_Y h||^2=||h||^2-||T_Yh||^2=||D_Yh||^2. (9)

Thus (8) canonically identifies each abstract defect range with

    normalized physical energy direct-sum causal escape.                (10)

There is no choice of a unitary on a defect complement.

## 3. The candidate

For a contraction `T`, let

    J(T)=[[T,D_(T^*)],[D_T,-T^*]]                  (11)

be its canonical Halmos--Julia unitary.  Form the relative unitary

    U_XY,T=J(T_Y)^* J(T_X).                         (12)

Let `Pi_2` denote the second Julia port.  The finite global transmission
candidate is the transported defect-to-defect block

    Theta_JR,T
      =V_Y P_(D_Y) [Pi_2 U_XY,T Pi_2^*]
          |_overline(Ran D_X) V_X^*,               (13)

and the middle block is explicitly

    Pi_2 U_XY,T Pi_2^*
      =D_(T_Y^*)D_(T_X^*)+T_YT_X^*.               (13a)

where `V_X D_Xh=delta_Xh` and `V_Y D_Yh=delta_Yh` are the canonical
isometries supplied by (9), and `P_(D_Y)` is the orthogonal projection onto
`overline(Ran D_Y)`.  Since (12) is unitary, compression and restriction of
its block in (13) are contractions.  Hence

    ||Theta_JR,T||<=1                               (14)

is proved before any comparison with `A_T`.

This is the missing kind of candidate: it is nonstationary because of
`P_T`, incorporates the endpoint escape rather than reflecting it, and is
functorial in the two source Schur systems.  It also has no prime-index
defect ambiguity because all finite places have already been replaced by
`C_eff`.

## 4. The exact primitive gate

The unnormalized bank vectors are recovered from (4) by the fixed wave
operators

    R_X=(Z_X+1)/2,
    R_Y=(Z_Y+1)/2.                                  (15)

For `F=L_0G`, `G in C_c^infinity((-T,T))`, define on the common smooth core

    h_X=P_T R_X F,
    h_Y=P_T R_Y F.                                  (16)

The candidate closes the global square if the direct block elimination of
(12) proves the single vector identity

    delta_Y h_Y
      =Theta_JR,T delta_X h_X                       (17)

after the two exterior Tate traces of `G` are shorted.  The first component
of (17) must, as part of the same calculation, cancel the wave-truncation
terms created by the projections in (16) and reduce to

    YF=Theta_eff,T XF,                              (18)

while equality of the escape components is the boundary term that the
failed bilateral endpoint mismatch omitted.  If this reduction and (18)
hold, then (14) gives

    <A_TF,F>=||XF||^2-||YF||^2
      =||(I-Theta_eff,T^*Theta_eff,T)^(1/2)XF||^2
      >=0.                                         (19)

The displayed inequality is only a consequence once (17) is proved; it is
not used to define the candidate.

## 5. Binary acceptance test

Expand (17) using (8), (12), and `F=L_0G`.  The candidate succeeds only if

1. the wave-truncation residual cancels and the first component is exactly
   the Gamma/effective-Frobenius bank map;
2. the second component is the same causal escape on both sides after the
   two Tate endpoint traces vanish;
3. no multiplier depending on `A_T`, no pseudoinverse and no adjustable
   Julia-complement unitary appears.

If an escape residual remains, (13) is rejected.  If it vanishes
identically, (19) is the finite global square and the already proved exact
stabilization supplies the cofinal passage.

The kill gate was run directly from the complex impedances (1), rather than
from the Douglas Gram contraction.  On three primitive potentials at
`T=log 2`, the relative residuals in the pre-landing form of (17),

    D_Y h_Y
      -(D_(T_Y^*)D_(T_X^*)+T_YT_X^*)D_X h_X,       (20)

converge as follows:

| time step | model dimension | residuals |
|---:|---:|---:|
| 0.01171875 | 119 | 0.184415, 0.174443, 0.166491 |
| 0.00781250 | 177 | 0.183544, 0.173852, 0.166204 |
| 0.00488281 | 283 | 0.183477, 0.173805, 0.166180 |

At the same stages the middle Julia block remains contractive, with norm
`0.999871`, `0.999870`, `0.999868`.  Thus the discrepancy is not a failure
of the free contractive half; it is precisely the missing realizing half.
The calculation is reproducible in
`scripts/p3_julia_short_log2_gate.py`.  No Tate refinement can repair (20)
without changing the already fixed candidate, because the tested inputs are
literal `F=L_0G` with `G` compactly supported strictly inside the window.

The stronger test uses exactly the piecewise-constant W3 meshes and the
whole primitive nullspace `ker(Tate)`, rather than selected potentials:

| W3 refine | primitive dimension | operator residual | Frobenius residual |
|---:|---:|---:|---:|
| 8  | 14 | 0.209201 | 0.147976 |
| 16 | 30 | 0.236000 | 0.173744 |
| 32 | 62 | 0.255268 | 0.200329 |

Doubling the Fourier-box resolution changes the operator residuals by less
than `3.1e-4`.  Hence the failure is an operator-level failure on the same
primitive Galerkin spaces used by phase 118, not a choice-of-test artifact.

## 6. Ledger

- positive-real systems and Cayley transfers (1)--(5): **PROVED**;
- finite-horizon contractions and physical defect landings (6)--(10):
  **PROVED**;
- Julia--Redheffer candidate and contractivity (11)--(14): **CONSTRUCTED
  AND PROVED**;
- primitive short/intertwining (17): **REFUTED AT THE CERTIFIED GATE**;
- Julia-short route: **CLOSED NEGATIVELY**;
- global square: **OPEN**.
