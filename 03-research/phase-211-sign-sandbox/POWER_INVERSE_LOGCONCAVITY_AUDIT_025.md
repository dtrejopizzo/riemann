# POWER INVERSE LOGCONCAVITY AUDIT 025

Status: APPROVED. Papers untouched.

Reviewed `POWER_INVERSE_LOGCONCAVITY_025.md` and `tools/power_inverse_logconcavity_025_verify.py`; independent run PASS. The first-cell certificate `POWER_CELL_TEST_024` and its verifier were reviewed and independently reproduced in POWER_CELL_AUDIT_024.

## 1. Log-concavity and infinite cut

The identity c_j=p_j(3d+30j)/(2d−j) follows exactly from D=33P−P′ and the gamma recurrence. The quotient (j+1)c_(j+1)/c_j has the two declared factors: the first decreases or is constant when d1; the second decreases strictly. The final quotient r_d=0 preserves monotonicity. With the weights c_jt^j/D, D′/D is the expectation of r_j and its derivative is Cov(r_j,j)/t≤0. This proves LC for all N≥2, without deducing from it an automatic Möbius sign.

The Fraction comparison D129′(2/3)<30D129(2/3) is certified. LC extends it to all t≥2/3; integrating the logarithmic quotient gives D(t+log m)/D(t)≤m^30. The absolute sum over ALL m≥2 is then dominated by Σm^−2≤3/4. CUT is a statement about the COMPLETE inverse. Since log2>2/3, one obtains K129>0 for all x≥2. It is not claimed that there is a single transition in [1,2].

## 2. Complete integrated balance

The representation J(x)=x∫_x∞K(t)t^−2dt implies J129(x)>0 for x≥2. In each cell n≥3, LOCAL024 and K>0 give S129(n)≥b_nJ129(n)>0. The first cell has the independent certificate S129(2)>33/100 with complete Möbius tail. Absolute convergence of the cell sum was proved earlier. Hence ERR129=−2ΣS129(n)<−33/50 on the WHOLE half-line. The C_B benefit of that same cell is not additionally combined.

## 3. Novelty and scope

The covariance lemma and the coefficient ratios are classical tools. The specific progress relative to020/023 is the improved cut for the real compensated kernel; relative to024, it allows controlling all remaining cells analytically and closing a COMPLETE signed arithmetic inequality at N129. The negativity K129(1) remains intact.

The result is not W≥0: W/C0=ARCH_sharp/C0−ERR keeps a pending quantitative comparison with ARCH_sharp. Nor is ERR<0 extended to all orders, to the whole table or to a new window T. The certificate of the complete form requires that additional balance.
