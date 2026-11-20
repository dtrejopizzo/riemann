# POWER_GAMMA_AFFINE_BALANCE_062 — The affine part042 is not a positive base at the same129

Status: PROVED, rational certificate PASS and independent review approved in POWER_GAMMA_AFFINE_AUDIT_062.md. Diagnosis of a single case already decided061; no new W sign nor uniform criterion. Papers untouched.

## 1. Concrete question and antecedents

After061, the case N129,k0 already has W>0 with normalized margin approximately1.3456684·10^−10. The question now is whether the affine part of RENORMALIZED042 can serve as a positive base from which to estimate its residue, or whether that residue is essential even in THIS case.

Consulted ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D and026/027/030/042/043. Summing LOCAL024 with ARCHsharp returns to Omega026; inverting the scales of027 returns to Hjoint030, as043/046 already recorded. No other regrouping is presented as a new tool.

The authorized quantitative difference is to evaluate separately, at the SAME129 and reusing the complete intervals024/061, the affine comparator and the complete renormalized residue. Neither130 nor another order is computed, precision is not increased and no other general sign criterion is built.

## 2. Global identity and which residue is measured

Keep the normalization of061 and define

    κ=(log(2π)−1)/2,
    β=2κ−γ=log(2π)−1−γ,
    J1=J129(1),
    AFF=ARCHsharp+2γ−βJ1.

The global identity042, valid for each fixed N by absolute convergence, is

    ERR/2=−γ+(κ−γ/2)J1+R,
    R=(ERR+2γ−βJ1)/2,
    W/||g129||²=AFF−2R.                                 (EXACT)

Here R is the COMPLETE RENORMALIZED residue:

    R=−∫_1^∞h129(x)B1({x})(logx+γ)dx +∫_1^∞h129(x)E(x)dx.

It includes both the periodic term B1 and the Euler error E. The benefit obtained is not attributed to B1 separately. Nor is ABS-TAIL042 applied, which requires N≥2^80 and is not available at129. This computation uses R over the WHOLE half-line, not Rinside nor Rtail of that theorem.

## 3. Complete data reused, without new cuts

CELL_TEST024 already computed endpoint1=Σ_(m≤64)μ(m)m^−32P129(logm), although its output did not print that endpoint. With its SAME positive polynomial and its same remainder tailP,

    J1∈[endpoint1.lo−tailP,endpoint1.hi+tailP].

The remainder controls ALL m≥65 by the positive gamma integral of024. The Möbius sum is not replaced by a prefix of assumed sign.

GAMMA_129_DECISION061 provides complete ARCHsharp and ERR: stable ARCH of032, rational polar, all contacts up to512 and rigorous adverse tail. Gamma and log(2π) use the audited intervals003. The verifier062 imports those two modules without changing their constants, their precision or their parameters, and then evaluates AFF and R via EXACT.

The new box of AFF and that of2R are not subtracted as if they were independent errors to recertify the small margin W: they share exactly J1,γ,β. W keeps its independent certificate061; the identity EXACT explains its algebraic cancellation.

## 4. Rational result

The run of tools/power_gamma_affine_balance_062_verify.py finished exit0 and PASS. Rounding outward to denominator10^12:

    J1 ∈[662483401466,662483401467]/10^12,
    AFF∈[−60446492280,−60446492279]/10^12,
    R  ∈[−30223246208,−30223246207]/10^12,
    −2R∈[60446492414,60446492415]/10^12.                 (BOXES)

In particular, without depending on floating decimals,

    AFF<−1/100,
    R<−1/200.

The affine base has a deficit of approximately0.06044649228. The correction of the complete residue contributes approximately0.06044649241, repairing it almost exactly and leaving the positive margin of061. The diagnosis uses only the precision already available024; it does not chase more digits of the residue.

## 5. Consequence and limit

For this concrete comparator, AFF is NOT a positive base of the proof. Ignoring the residue or treating it only as an unquantified perturbation loses the contribution that repairs the deficit. It is not concluded that a renormalized residue cannot be bounded with sign nor that every affine representation fails: the essential term of THIS real balance is identified.

The datum R<0 is not extended to other N. Moreover R was enclosed using the already known ERR061; no new independent estimate was obtained that would allow propagating the sign in N. The uniform comparison of the cells with ARCHsharp remains open. The result does not refute042, does not use universal K≥0 and does not modify the kernel, the archimedean constant or Λ.

Hence only the quantitative diagnosis and its use are recorded: any continuation from the affine part must keep and genuinely estimate the complete residue, even at129, where its magnitude is of order0.03 although W/norm² is of order10^−10. There is no new sign case, T window nor global conclusion.
