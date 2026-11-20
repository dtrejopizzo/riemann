# POWER CELL AUDIT 024

Status: CELL_BALANCE024 and the single certificate of first cell129 APPROVED. Papers untouched.

## 1. Integrated criterion — APPROVED

Reviewed `POWER_CELL_BALANCE_024.md`. The definition S_N(n)=H_(n−1)∫J−log(n)J(n) keeps the jumps and slopes of B; the absolute sum is −F_N/2. That identity is not used as a sign assumption.

The differential identity J(x)=xJ(n)/n+x∫_x^nK(t)t^−2dt, integrated over the finite triangle, produces exactly LOCAL with the factor H/2 and weight 1−(n−1)²/t². The nonnegative weight integrates to1/n. Thus BUFFER keeps the whole adverse part, with no sign hypothesis on J or K. The criterion J(n)≥0 and sup K^-≤4aJ(n), a=3/4−log2, implies S≥0 because b_n≥a and H/(2n)≤1/4. These hypotheses are not proved for all cells.

## 2. Exterior and exact interface — APPROVED

OUTER020 implies h≥H/4 on the whole tail x≥exp((N−1)/30), whence J(n)≥w(n)/4 and J is decreasing on each entirely exterior cell. Hence OUT-CELL and its improvement via H−log n are correct. Possible adverse cells are only localized to a finite region for each N; their balance is not automatically controlled.

The recurrence31Q−Q′=P has positive coefficients and generates T(x)=x^−31Q(log x)=∫_x∞w. The change y=mx in ∫_1²w(mx)dx correctly produces the factor m^−32 in the Möbius-sum interface. The formula for J(2) keeps2^−32. No Jacobian is missing.

## 3. Corpus and scope

The distinction relative to023 is an explicit integrated budget tolerating negative K, not a resurrection of universal K≥0. The Möbius and primitive identities are antecedents; the new local inequality quantifies a margin and requires real bounds on its terms. The identity W/C0=ARCH_sharp/C0+2ΣS keeps the archimedean deficit. Neither F≤0 nor a favorable cell implies W≥0 or a new window T.


## 4. First cell129 — APPROVED

Reviewed `POWER_CELL_TEST_024.md` and `tools/power_cell_test_024_verify.py`. Independent run PASS: 31/100<∫_1²K C_B<8/25, 33/100<S129(2)<1/3 and 1/2<∫_1²K/x²<3/5. The computation is rational with complete tail; it uses no quadrature.

Integration by parts gives exactly ∫K C_B=∫J−(3/4)J(2), using the left limit of the weight at2, and ∫K/x²=J(1)−J(2)/2. The jump of the global representation at2 is not eliminated: the pointwise value of the weight does not change this ordinary integral. S(2)=∫J−log2 J(2) is another boundary assignment and must not be added as a benefit independent of the first.

The script checks31Q−Q′=P coefficient by coefficient. Its finite integrals and endpoints use the correct factors m^−32,2^−31 and2^−32. The factorization of μ and the outward interval evaluator are those already audited022/023. For each m, decreasing w(mx)>0 gives ∫_1²w(mx)dx≤w(m) and w(2m)≤w(m). Hence each error of the three combinations is less than2T_P. The positive majorant via the integrals from64 covers ALL m≥65 and is less than10^−10. No sign of the Möbius remainder is assumed.

The negativity K129(1)<0 is compatible with these positive averages and, by continuity, forces K to be positive at some interior point. No number of transitions is deduced. The ERR benefit of this cell does not determine total ERR nor W. The other cells and the ARCH_sharp deficit remain pending in this round; no later construction is incorporated here.
