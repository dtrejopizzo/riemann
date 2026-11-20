# POWER_AUDIT_006 — Independent review of the test repaired by contact 2

Status: PROVED and rerun. Papers untouched. Audits POWER_ARITHMETIC_WITNESS_006.md and tools/power_arithmetic_witness_006_verify.py.

## 1. Arithmetic and matrix certification

The Fraction verifier was run independently with output PASS. The norm N=99993678, the reduction of Toeplitz bands and the coefficients T_r are correct: the factor 2 of the band pairs cancels the factor 1/2 of b_k, and the substitution psi^(r)(16)=(-1)^(r+1)r!sum m^(-r-1) cancels the remaining factorial. It was checked that each coefficient of negative sign uses the upper tail at the lower endpoint and vice versa. The polar moments produce 126AB with the declared rational sums. The certification gives strictly

    -2/125 < (Arch+Polar)/N < -1/100.

The bounds for d, logarithms and gamma are the same already audited in round 005; the tails of each derivative of psi are bounded by the integrals from 256 and 255, with correct orientation.

## 2. Autocorrelation verified by an independent computation

Besides running the formula of the memo, the polynomial P(x)=sum v_j L_j(x) was expanded directly in monomials and

    Q(t)=integral_0^infinito exp(-x)P(x)P(x+t)dx

was computed. If P(x)=sum p_a x^a, each coefficient is obtained as

    [t^k]Q=sum_{a=0}^{11}sum_{b=k}^{11} p_a p_b binom(b,k)(a+b-k)!.

Exact integration via Fraction/factorials reproduces the twelve coefficients of the memo, without using the shifted Laguerre identity as a premise. This confirms the orientation of the cross terms and the absence of a missing factor two. Scaling x=63y gives exactly c_h(t)=e^(-31.5t)Q(63t).

The shift Q(x+40) has twelve strictly negative coefficients, verified again by the script. Therefore Q<0 and Q'<0 on [40,infinity). Since 63log2>42, each real prime-power contact contributes positive sign:

    -2Lambda(n)n^-32 Q(63log n)>0.

No strict sign is assigned to integers with Lambda(n)=0.

## 3. Lower repair without estimating the tail

The inequalities -Q increasing and log2>2/3 justify with their exact sign

    -2log2*2^-32 Q(63log2)/N >-(4/3)2^-32 Q(42)/N>1/25.

All other terms of the comb are nonnegative. Their series converges absolutely because Q is a polynomial of degree eleven and the weight is n^-32. Consequently

    W[h]/N>1/25-2/125=3/125>1/50.

The tail is not omitted as a small error: it is kept as a sum of terms of favourable sign, which suffices for this lower bound. It is not deduced that removing contact 2 makes the sum of the rest negative; an additional upper bound would be needed.

## 4. Novelty and scope

An explicit exterior case is obtained in which ARCH+POLAR is negative and the isolated contact 2 compensates the deficit. The antecedents on general arithmetic necessity and other uses of Laguerre are detailed in POWER_AUDIT_005§7. The concrete novelty lies in the rational vector, the autocorrelation of checkable sign and the exact repair of the present test; it is not a certificate for the whole block of order twelve nor for the sign of all windows.

## 5. Reviewed extension: removing only contact 2 changes the sign

An upper bound for the tail was added after §§1–4. Reviewed and rerun: APPROVED; it replaces the earlier limitation of not having that bound. For r<=12, log3>1 guarantees that f_r(x)=(log x)^r x^-32 decreases on x>=3. Its sum is controlled by f_r(3)+integral_3^infinito f_r(x)dx. The substitution t=log x and the binomial expansion give exactly the formula of §4 of the main memo; using log3<11/10 has the correct sign because all its coefficients are positive.

The added script certifies 1<log3<11/10 with J/E at r=1/2 and verifies, after summing the twelve absolute values of the coefficients of Q, that the TOTAL contribution of n>=3 is less than N/500. Therefore

    W_sin_contacto2[h]/N < -1/100+1/500=-1/125.

This step now allows asserting the sign change when removing exclusively n=2, keeping all n>=3, including the powers of 2. The earlier claim of §§3–4 was deliberately conditioned on not having an upper bound; this extension supplies exactly the missing piece. The result still refers to the explicit exterior test, not to all directions nor to another class of carriers.
