# At the endpoint four mass is still missing

**Status: PROVED, with independent review of the second-order comparison, the factorκ/4 and the logical consequence.**

Let L=log x, z=L², b=log z and p_* as in 393. Under RH one has

    liminf b(p_*/z−4) ≥ 8(1+log 2)log 4.

Hence an eventual ceiling p_*≤(4+κ/b)z with κ strictly less than that constant is ruled out unconditionally: that ceiling would imply RH by 393 and then contradict the new floor. In particular the exact cut 4z does not work either.

**Comparing at the same saddle.** Let α be the exact saddle of 367 for z=L²; c_b=b(α−1/2)→log 2. Under RH, 368 gives

    log |S|=αL+log E_z(α)+O(log L).

The finite sum with any admissible last weight and largest prime ≤Kz, K=4+κ/b, satisfies log |C|≤αL+Σ_{z<p≤Kz}p^(−α)+O(1) by the positive majorant of 393 (the inequality of moduli remains valid in case of zero). Since log E_z(α)≥Σ_{p≤z}p^(−α), it suffices to compare sums of first powers. Using the same α avoids computing the second term of its position.

Set I(T)=∫₂ᵀ t^(−α)dt/log t, keeping α frozen. For T comparable to z, the prime sum up to T and I(T) differ by o(L/b²) by partial summation of the PNT with classical remainder: the range t≤√z costs O(z^(1/4)log z), and higher up the saving exp(−c√b) dominates any power of b. Thus the difference of the two sums is I(Kz)−2I(z)+o(L/b²). One has I(z)∼L/b by integration at the upper end and c_b→log 2.

Changing t=4s in I(4z), the interval s<2 only contributes O(1) (one integrates from 1/2, where log(4s)=log 2). Against the weight s^(−α)/log s of I(z) the multiplier 4^(1−α)log s/(log s+log 4) is introduced. The weighted mean of 1/(log s+log 4) is (1+o(1))/b: on s≤exp(b−√b) the mass fraction is O(poly(b)exp(−c√b)), and on the rest the equivalent is uniform. Hence

    I(4z)−2I(z)=[−2(1+log 2)log 4+o(1)] L/b².

Finally I((4+κ/b)z)−I(4z)=(κ/4+o(1))L/b², by the uniform value of the integrand on that oriented segment, using exp(−c_b)→1/2. Hence the logarithm of the finite majorant minus log|S| is at most

    [κ/4−2(1+log 2)log 4+o(1)] L/b².

If the coefficient is negative, not even the absolute mass allows the exact equality. The O(log L) term of the saddle prefactor is negligible at this scale. The argument identifies an excluded interval above four and does not give a cut that reaches S.

**Review record.** With α=1/2+c_b/b, the factor4^(1−α) is2(1−c_b log4/b+O(b^(−2))); the mean of the quotient log s/(log s+log4) is1−(log4+o(1))/b. Their product gives2−2(1+c_b)log4/b+o(1/b). Since I(z)∼L/b and c_b→log2, the coefficient−2(1+log2)log4 is preserved exactly without requiring a second term for c_b. To shift4z byκz/b, the integrand at4z equals(1/4+o(1))L/(zb): the factor1/2 of4^(−α) and the factor1/2 of exp(−c_b) explainκ/4. The formula also holds for negativeκ with the oriented segment. The PNT errors are o(L/b²), and O(log L)=o(L/b²), so none changes the constant.

For eachκ strictly below8(1+log2)log4, every representation with terminal prime≤(4+κ/b)z is excluded underRH, for all sufficiently large x; lettingκ rise to the threshold gives the stated liminf. The unconditional discard is that of an eventual ceiling: that ceiling, if it existed, would be of scale L^(2+o(1)) and would implyRH by393. Neither a pointwise floor nor the same liminf withoutRH is deduced, nor existence of a representation at the endpoint of the constant.
