# E72.268 -- Corrected pole-even RFBD package

**Purpose.** Consolidate the corrected RFBD/LM8 route after the parity repair of E72.261--E72.267.

The old helper removed an accidental even line. The corrected pole-relative geometry is:

```text
e_pole  = lambda_0(H_model)                         # odd pole
B_even  = orthonormal even Fourier basis
C_model = B_even^T(H_model-e_pole I)B_even
C_actual= B_even^T(H_actual-e_pole I)B_even
```

## Corrected model input

By E72.267,

```text
lambda_min(C_model)
= lambda_0(H_model|even)-lambda_0(H_model|odd).
```

Therefore the model coercivity theorem is:

```text
MCOER2-pole-even(c_C,L0):
for lambda >= L0,
lambda_0(H_model|even)-lambda_0(H_model|odd) >= c_C L^2.
```

The observed corrected ratios are:

```text
lambda=16: gap/L^2 = 0.3371033429
lambda=20: gap/L^2 = 0.3855732981
lambda=24: gap/L^2 = 0.4308217907
```

A conservative proof target consistent with the corrected stable package is:

```text
c_C = 0.30,        lambda >= 16.
```

For the stable LM8 envelope alone, one may take `lambda>=20`.

## Corrected LM8 package

The BSE/LM8 split becomes:

```text
lambda >= 20:
  stable pole-even homogeneous LM8 envelope, rational/interval-certified in E72.264--E72.265;

lambda = 16:
  sharp finite BSE certificate target from E72.266;

lambda < 16:
  below the selected stable threshold and handled separately if required by the final quantifier.
```

The stable rational envelope is:

```text
P_j(u)=u^2R_j(u),
```

with the E72.264 coefficients and E72.265 exact Bernstein proof of:

```text
R0 >= 1 on [-1,0],     R0 >= 0.09 on [0,1],
R1 >= 1 on [-1,0],     R1 >= 0.16 on [0,1].
```

## Corrected RFBD theorem schema

The corrected finite route should now be stated as:

```text
MCOER2-pole-even(0.30,16)
+ stable LM8-pole-even(lambda>=20)
+ sharp BSE_16
+ HOC3/K1-pole-even low-mode package
+ XNEG-pole-even-D16 mixed package
+ transport gates CGE-K, ROP, MSB
=> RFBD
=> scalar WRL resonance annihilation
=> Omega_7.
```

The terms `HOC3/K1` and `XNEG/mixed` have now been rechecked in the corrected pole-even geometry:

```text
E72.269: HOC3/K1 survives with positive low-tail margins.
E72.270: XNEG survives for D16/D32/adaptive signed approximants.
```

They still need proof-facing cycle/trace or interval certificates; the floating diagnostics are no
longer based on the old accidental complement.

## What is closed now

Closed:

```text
1. The corrected pole-even geometry.
2. The exact identity reducing MCOER2 to an odd/even model gap.
3. The stable homogeneous LM8 majorant algebra for lambda>=20.
4. The lambda=16 sharp BSE numerical target and slack.
5. Corrected pole-even HOC3/K1 diagnostic survival.
6. Corrected pole-even XNEG/mixed diagnostic survival at D16 and above.
7. XNEG-D16 finite mixed trace expansion.
8. HOC3/K1 finite low-tail block identity.
9. Corrected bordered-minor endpoint identity in the pole-even complement.
10. First corrected pole-even HPAC source probe for b_tau=B_even^T A_x(tau)xi_x.
11. Exact finite-root HPAC gauge split
    A_x(tau_j)xi_x=2xi_x+i(1/2+i tau_j)S_tau_jxi_x.
12. Positive compact-height profile for the left-gauged resonant HPAC residual.
13. Exact inverse-collapse identity splitting the residual into a diagonal term and a commutator term.
14. Exact Cauchy-factor identity for the diagonal term:
    <a_s^perp,S_tau_jxi_x>
    = z M_x(z)(-2tau_j/(z^2-tau_j^2)-V_x(tau_j)).
15. Cauchy-mass decay `M_x(z)/mu_x -> 0` on fixed Cauchy compact sets, conditional on the pole-even gap.
16. Variance-bracket gate: it is enough to prove
    sup_{tau_j<=H}||S_tau_jxi_x||=O_H(L^beta), beta<3/2.
17. Squared-Stieltjes identities:
    V_x(tau)=W_x(tau)-W_x(-tau),
    ||S_tau xi_x||^2=-W_x'(tau)-W_x'(-tau)+V_x(tau)/tau.
18. VBG proved with beta=1 by root-energy control and reciprocal-square mesh sums.
19. The diagonal compact-root HPAC term is closed, conditional on the pole-even gap.
20. Compact-root commutator term is closed conditional on the natural upper complement bound
    ||C_E||=O(L^2).
21. Fixed-height compact-root decay for the left-gauged resonant source follows from
    the lower gap plus the upper complement bound.
22. Upper complement split:
    ||C_actual|| <= ||C_model|| + lambda_max(Delta_arith)_+.
23. APCB rewritten as exact finite arithmetic autocorrelation inequality.
24. MUCB reduced to the pure model endpoint identity
    ||C_model||=lambda_max(H_model|even)-lambda_0(H_model|odd).
25. APCB follows from the scalar Dirichlet-symbol floor
    -2 inf_omega Re sum_{n<=e^L} Lambda(n)n^(-1/2+i omega)=O(L^2).
26. DSF strength audit: the scalar floor is likely RH-strength; compressed APCB remains the better
    target.
27. APCB band-exclusion diagnostic: top positive compressed modes live in high mesh frequency, while
    the DSF bad symbol is low-frequency.
28. APCB band split: low/high/cross block inequality with cutoff |d|<4.
29. High-band APCB reduced to explicit Gershgorin row-sum bound H-GERSH.
30. Low/cross APCB budget reduced to LOW-FIN and CROSS-HS.
31. Analytic lemma stack written. Its original global APCB branch is now retired by E72.295.
32. H-GERSH corrected: absolute high-band row sums erase the sign of the PNT main term. The proof
    target is now the signed high-band theorem H-SIGNED.
33. Global APCB obstructed analytically by high Fourier diagonal modes of size e^(L/2)/L.
34. Upper-complement route replaced by the source-local directional commutator bound DCB.
35. DCB rewritten exactly as the spectral energy identity
    [C_E,S_tau]xi=(C_E-mu I)S_tau xi.
36. FORM-DCB rewritten as a double-commutator finite kernel identity with factor (s_m-s_n)^2.
37. Arithmetic FORM-DCB reduced to an Abelized scalar kernel F_tau(y) with endpoint cancellation
    F_tau(0)=F_tau(L)=0.
38. Standalone MAIN-FORM retired: the e^(y/2) arithmetic main cancels exactly with the e^(y/2)
    model term. Correct target is LOWEXP-FORM + WR-FORM + PNTERR-FORM.
39. LOWEXP-FORM and WR-FORM collapsed to one archimedean residual:
    ARCH_tau=1/2 int_0^L e^(-5y/2)/(1-e^(-2y))F_tau(y)dy.
40. PNTERR-FORM converted to the finite Mellin transform
    M_tau(z)=int_0^L e^(zy)F_tau(y)dy, with closed divided-difference formula.
41. Compact-root route packaged as:
    GAP + VBG + ARCH-FORM + MSD-FORM + (EFF-SUP or DCB-square)
    => fixed-height compact-root HPAC decay.
42. ARCH-FORM and MSD-FORM unified: ARCH_tau is the shifted trivial-zero lattice
    1/2 sum_{k>=0}M_tau(-(5/2+2k)).
43. Explicit-formula bookkeeping closed in the compact FORM channel:
    FORM_actual(tau)=-(1/2)sum_rho M_tau(rho-1/2), nontrivial zeros only.
44. Compact-root route sharpened to:
    GAP + VBG + NZ-MSD-FORM + (EFF-SUP or DCB-square)
    => fixed-height compact-root HPAC decay.
45. NZ-MSD normalized:
    M_tau(z)=(1-e^(zL))N_tau(z); apparent mesh poles are removable, so there is no mesh-residue
    shortcut.
46. Normalized transform rewritten as a Loewner double commutator:
    N_tau(z)=(2/L)<xi,[S_tau,[L_z,S_tau]]xi>.
47. Loewner kernel factored to rank two:
    N_tau(z)=-(4/L)(z^2U_0(z)U_2(z)+V_1(z)^2).
48. Weyl root relation collapses normalized MSD to rank one:
    N_tau(z)= -16 z^2 tau^2/(L(tau^2+z^2)) U_0(z)R_tau.
49. Rank-one moment rewritten as finite Cauchy transform:
    U_0(z)=iC_x(iz)/z, so compact NZ-MSD is MC-NZ.
```

Open:

```text
1. Analytic proof of the odd/even gap lower bound.
2. Formal interval/Sturm proof of the lambda=16 finite BSE certificate.
3. Uniform sign proof for the HOC3/K1 finite low-tail inequality.
4. Uniform sign proof for the XNEG-D16 finite mixed trace polynomial.
5. Transport gates CGE-K, ROP, MSB.
6. Proof that the corrected HPAC source is the exact load-bearing scalar WRL source.
7. Model upper endpoint theorem:
   lambda_max(H_model|even)-lambda_0(H_model|odd)=O(L^2).
8. Directional commutator bound DCB:
   sup_{tau_j<=H}||[C_E,S_tau_j]xi||=O_H(L^alpha), alpha<7/2.
9. DCB energy package:
   FORM-DCB in double-commutator form, or the stronger DCB-square finite identity <= C_H L^6.
10. High-root tail estimate beyond fixed compact height.
11. Divisibility for the corrected bordered minor.
12. The final Mellin spectral divisibility / scalar WRL annihilation theorem.
```

## Reading

This does not close RH. It prevents a false closure: the corrected route now has the right pole
geometry and a clean separation between stable asymptotic LM8 and finite transition certification.

E72.293 is the current proof ledger. E72.295 shows that global APCB is false asymptotically, so the
global upper-complement route is retired. E72.296 gives the corrected target: prove the source-local
directional commutator bound DCB and use it directly in the inverse-collapse identity. E72.297 rewrites
DCB as a spectral energy estimate for the single vector S_tau xi. E72.298 gives the double-commutator
finite kernel identity that kills the high diagonal APCB obstruction. E72.299 gives the exact scalar
Abel form for the arithmetic FORM-DCB term. E72.300 combines it with the model term and cancels the
exponential PNT main exactly. E72.301 collapses the remaining archimedean terms to ARCH-FORM, leaving
ARCH-FORM + PNTERR-FORM for FORM-DCB. E72.302 rewrites PNTERR-FORM as the Mellin spectral
divisibility target MSD-FORM. E72.303 packages the resulting compact-root theorem.
E72.304 unifies the archimedean residual and spectral error as one shifted explicit-formula divisor
sum for M_tau.
E72.305 proves the exact cancellation of the trivial lattice, leaving only the nontrivial-zero Mellin
sum as the compact arithmetic target.
E72.306 rewrites that target in normalized form and identifies the off-line zero pressure on
`N_tau(rho-1/2)`. E72.307 rewrites `N_tau` as a finite Loewner double-commutator quadratic form.
E72.308 collapses it further to a rank-two scalar resolvent moment identity.
E72.309 uses the finite root equation to reduce the target to the single scalar moment `U_0(z)`.
E72.310 rewrites that moment as the finite Cauchy transform at rotated spectral points.
