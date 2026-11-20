# Fit on prime powers: a scalar replaces the composite equations

Fix g,h from 257, N=⌊2x⌋ and the carries c_{n,k}(m) from 261, 2≤n≤N, 1≤k≤n/2. Let W(x) be the minimum of Σ|a_{n,k}| that reproduces g(m/x) only on prime powers. Let W_c(x) be the same minimum when one additionally imposes

    Σ a_{n,k} e(n,k)=xh,
    e(n,k)=n log n−k log k−(n−k)log(n−k).

This condition equates the continuous masses of the two sides, by 258. For x≥3, W_c is always finite. The global sign is equivalent to W_c(x)≪_ε x^(1/2+ε) for every ε>0. Exactness on integers with several prime divisors is no longer required. For W without the scalar this converse has not been proved.

**Sufficiency.** Put J(x)=Σ_m Λ(m)g(m/x). Every representation in the atoms gives exactly J(x)=Σ a_{n,k}log binom(n,k). By Stirling, uniformly |log binom(n,k)−e(n,k)|≪log(2N). For a calibrated fit it follows that |J(x)−xh|≪W_c(x)log(2N). Its Mellin transform in Re s>1 is H(s)(−ζ'/ζ)(s)−h/(s−1), integrating from 1 (the support of g(m/x) lies in x≥1 for m≥2). A square-root bound with arbitrary loss continues that difference to Re s>1/2, impossible in the presence of a zero to the right because H(ρ)≠0. The use of all prime powers in this identity is essential.

**Necessity and explicit correction.** The combination of the carries of binom(6,1), minus those of binom(3,1) and binom(2,1), is zero on all prime powers, because c_{j,1}(m)=1_(m|j) for m≥2. Its continuous mass, however, is η=6 log 6−5 log 5−3 log 3≠0 (6^6≠5^5 3^3). Any scalar error Δ is corrected exactly at cost ≤3|Δ|/|η|. Under RH take the integer fit of 261, of cost O_ε(x^(1/2+ε)). The mass error costs in absolute value O_ε(x^(1/2+ε)log(2N))+|J(x)−xh|, and the second term is O(√x) by the absolutely convergent series of 257 under RH. Absorb the logarithm by reducing ε. Without RH the same procedure builds a finite fit starting from 261; its square-root cost remains open.

**Dual without calibration.** W is the supremum of Σ z_m g(m/x) over real z on the prime powers up to N, with |H_z(n)−H_z(k)−H_z(n−k)|≤1, H_z(n)=Σ_m z_m⌊n/m⌋. This is finite linear duality, with feasibility via the columns binom(m,1), which allow correcting from the highest to the lowest exponent for each prime. The increments of H_z are an additive function on coprime arguments. By the cyclic averaging of 261, if the additivity defect of H_z is bounded by 1, then |H_z(n)−nH_z(N)/N|≤2. Conversely, approximating H_z by a line through the origin with error E bounds the defect by 3E. This makes it possible to investigate the atomic fit through partial sums of additive functions.

**Certified finite cases.** The following intervals enclose the optima WITHOUT the scalar. Each interval was rounded outward to the thousandth.

| x | Prime powers only | All integers |
|---|---|---|
| 16 | [2.517, 2.518] | [4.477, 4.478] |
| 32 | [2.612, 2.613] | [5.740, 5.741] |
| 64 | [2.745, 2.746] | [7.597, 7.598] |

Run python3 verify_262.py. The solver only proposes witnesses. For the floor, the dual coefficients are rounded and divided by the exact maximum of the constraints and the scale. For the ceiling, the primal is rounded and its residual r is repaired with binom(j,1): on powers of the same prime it suffices to subtract successive residues, at cost ≤2Σ|r_m|. For all integers, inversion over multiples is used, with cost ≤Στ(m)|r_m|. Weights and residual budgets are evaluated with Arb balls. An internal gap <0.0001 is checked before the rounding of the table.

**What remains.** The three examples show that the composite equations genuinely make these fits more expensive. The mass scalar is an additional condition: the example with 6 shows explicitly that the atomic fit alone does not determine it. It does not follow from the table that the calibrated cost grows at square-root scale. To prove this via the proposed correction one must still control the mass error; paying for it with a conditional estimate of J does not give an independent proof.
