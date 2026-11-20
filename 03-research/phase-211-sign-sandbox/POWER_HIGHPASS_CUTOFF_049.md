# POWER_HIGHPASS_CUTOFF_049 — Effective cutoff J=32 for E2 on Q^j V12

Status: DRAFT SUPERSEDED by POWER_CENTERED_CUTOFF_049 (cutoff 14) and POWER_R12_TRANSPORT_049 (segment 1..13 and uniform transport). Do not record this cutoff 32 as an additional result. Papers untouched.

## Antecedents and difference

Consulted the ROUTES-TRIED-INDEX index, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D, searching for Jacobi, inverse moments and highpass; reviewed JOINT_SCALE016, GEOMETRIC_TRANSFER015 and R12_ENDPOINT048. The Beta/Jacobi coordinates and eventual positivity were already proved. The difference is an explicit uniform inverse bound, with cutoff J=32 for all numerators of V12, instead of a limit without an effective index.

Fix u=63/2, Q(s)=s/(s+u), q=|Q(iτ)|²=τ²/(u²+τ²). For nonzero F∈V12 and j≥32 we prove

    ∫τ^−2 |Q^jF|² / ∫|Q^jF|² ≤ 2/u²=8/3969<1/400.    (INV)

The spectral integrals carry the same factor 1/(2π), which cancels.

## Weighted polynomial lemma, with proof

Let w(q)=q^α(1−q)^β, α>0, β>−1, and p a real or complex polynomial of degree≤m. Write R=∫[(1−q)/q]|p|²w/∫|p|²w. Then

    αR ≤ β+1+2sqrt(m(m+α+β+1)R).                       (JAC)

First, the energy satisfies ∫q(1−q)|p′|²w≤m(m+α+β+1)∫|p|²w. Elementary proof: the operator

    Lp=−w^−1 (q(1−q)wp′)′

preserves the polynomials of degree≤r and has leading coefficient r(r+α+β+1) on q^r. Integration by parts makes it symmetric (the flux q^(α+1)(1−q)^(β+1) vanishes at both ends). Applying Gram–Schmidt to 1,q,...,q^m, each orthogonal polynomial is an eigenvector: its image minus the leading coefficient times itself has lower degree and is orthogonal to all those degrees. The energy is therefore the sum of squared coordinates times these increasing eigenvalues. This proves the bound without importing an external spectral theorem.

By another integration by parts, now of q^α(1−q)^(β+1)|p|², whose endpoint terms also vanish,

    αR = β+1 − 2 Re∫(1−q)p′ conjugate(p)w / ∫|p|²w.

Cauchy, with factors q(1−q)|p′|² and (1−q)|p|²/q, gives JAC.

## Simultaneous application to all numerators

The Laguerre basis 048 turns F into E_0(iτ)P(z), degP≤11, z=(iτ−u)/(iτ+u) on the circle. The measure |E_0|²dτ/(2π) is uniform on the circle; q=(2+z+z̄)/4. Split P(e^{iθ})=A(cosθ)+sinθ B(cosθ), allowing complex coefficients. When integrating any weight depending only on cosθ, the cross term is odd and vanishes. Thus it suffices to apply JAC to two nonnegative sectors:

- even: α=j−1/2, β=−1/2, m=11;
- odd: α=j+1/2, β=1/2, m=10.

The factor sin²θ=4q(1−q) explains exactly the change of weight in the second sector. Lower degrees are included by padding with zero coefficients.

For the even sector, at R=2 we have

    (2j−3/2)² > 88(j+11),    j≥32.

For the odd one,

    (2j−1/2)² > 80(j+12),    j≥32.

Both left-hand sides are positive. The differences at j=32 are respectively 489/4 and 2049/4; their derivatives are positive from 32 on. The function αR−(β+1)−2sqrt(λR) has a single positive root, being quadratic in sqrt(R). The inequalities above place that root below 2, and JAC implies R<2. Mixtures of the two sectors keep this bound. Finally τ^−2=u^−2(1−q)/q, proving INV.

## Domination of the partial form E2 and remaining finite obligation

Use the elementary bound on the symbol from 017,

    m(τ) ≥ log|τ|−log(2π)−1/|τ|−1/(2τ²).

Jensen applied to log(τ^−2), and Cauchy, give for the normalized spectral probability

    ARCH ≥ −(1/2)log Eτ^−2−log(2π)−sqrt(Eτ^−2)−Eτ^−2/2
         > log(10/π)−41/800 > 11/10.

The last inequality follows from π<22/7 and log(35/11)>921/800, which is checked through a positive atanh sum with argument 12/23. Contact 2 has absolute value less than sqrt(2)log2<1 times the norm.

For the polar term, 048 proves |Polar[Q^jF]|/||Q^jF||²≤(9/62)^j PB12. Here PB12<3: each polar band satisfies

    |p_k| ≤ (63/992)[(32/31)^11+1] < 1/5, 0≤k≤11.

Indeed (1+1/31)^12≤1/(1−12/31)=31/19<2, by comparing binomial coefficients with the geometric series. The row sum is less than 12/5<3. Hence 3(9/62)^j<1/1000 for j≥32. We conclude

    E2[Q^jF] > (99/1000)||Q^jF||²,  j≥32, F∈V12\{0}. (TAIL)

This is a uniform effective cutoff, not only eventuality. GEOMETRIC_TRANSFER015 now reduces the R12 transport to checking E2−c norm² on Q^jV12 for j=1,...,31, with c=1/2500. Index 1 is certified in 048. The sign of the other thirty blocks has not been proved here; TAIL does not imply it. R12 is not declared uniform and no sweep over rates or orders has been carried out.
