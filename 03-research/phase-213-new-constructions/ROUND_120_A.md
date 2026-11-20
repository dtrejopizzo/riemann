# How much data of the even matrix suffices in each window

For the full matrix A in the orthonormal basis of 119 the diagonal and the first row suffice: all remaining entries are recovered exactly, with amplification at most polynomial in N=ceil(T³). The global sign is equivalent to these 2N−1 data, in absolute value and with a common ceiling, being exp(o(T)) or smaller along some sequence T→∞. Under RH they even satisfy a polynomial bound. The converse uses the full matrix and does not need positivity of the entries.

**Identity.** Set a_j=(j+1/2)π/T, d_j=a_j², c_j=2(−1)^j a_j/√T, z=ρ−1/2. The two-sided transform of the normalized cosine evaluated at z is c_j cosh(Tz)/(d_j+z²), with continuous extension at ±ia_j. For i≠j, the polarized Weil formula (even transforms) and partial fractions give

    A_ij=c_i c_j (H_i−H_j)/(d_j−d_i),
    H_i=Σ_z cosh²(Tz)/(d_i+z²).

For fixed T there is absolute convergence by O_T(1/γ²). At a coincidence z=±ia_i the summand of H_i is continued by zero because the numerator has a double zero; in the cross product the other transform vanishes. The diagonal is kept as separate data. Weil's formula is valid for these H¹₀ modes by smoothing, or directly by quadratic decay of their transform in each strip and approximation by compact convolution.

Define U_0=0, U_j=(d_j−d_0)A_0j/(c_0 c_j). Then A_ij=c_i c_j(U_j−U_i)/(d_j−d_i). The coefficient of A_0j has modulus |c_i/c_0|·|(d_j−d_0)/(d_j−d_i)|, and analogously for A_0i. The first is ≤(2N+1)N² because d_j−d_i=(π/T)²(j−i)(j+i+1) and d_j−d_0=(π/T)²j(j+1). Thus the matrix norm is O(N⁴) times the maximum of the 2N−1 data for N≥2.

**Necessity of the absolute bound.** Under RH, W(F)=Σγ|F̂(γ)|² for F unit in this basis. By subharmonicity on discs of radius 1/(2T), the local count O(log(2+|γ|)) and the strip |σ|≤1/(2T), this sum is ≪T²∫_strip∫ log(2+|ξ|)|(exp(σt)F)^∧(ξ)|²dξ dσ. For these modes ∥F'∥≤πN/T, and the extension by zero is in H¹. The exponential product on the support has H¹ norm ≪1+N/T, so the right-hand side is polynomial in T. This gives, by polarization or by the positive norm, the common bound on the data. Conversely, with the assumed subexponential ceiling, the cost O(N⁴) is still subexponential, even for the minimum in absolute value. 119 excludes Δ>0.

**Cross-check.** Divided differences and Loewner objects are already in the corpus (among others R166_103A and the POWER route). Here the Loewner label is not treated as a sign mechanism: the application is the quantitative recovery of this Dirichlet matrix from one row and the diagonal, together with the sequential criterion of 119. The formulas for H_i via zeros may have exponential terms without RH; bounding the data via the arithmetic formula is still missing.

**Confirmed direct antecedent.** In paper 47 itself, lemma `combsine` (main.tex, line 6469), the combination of two quotients for the comb in one parity simplifies to [a_i D_T(a_j)−a_j D_T(a_i)]/[T(a_i²−a_j²)]. It already has the structure that allows recovering the comb from an off-diagonal row. What 120 adds corresponds to the full form, the reconstruction cost and the sequential use of 119.
