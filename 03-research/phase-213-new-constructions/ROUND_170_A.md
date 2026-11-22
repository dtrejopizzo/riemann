# Minimal negative mass of a truncated certificate of paper 46

Fix a window T>0 and a finite, symmetric, nonempty list Z of real ordinates, with their multiplicities. In the notation of finDet and finZ of paper 46 let g_Z(u)=Σ_{γ∈Z}cos(γu). For a smooth real even profile, equal to one on [−2T,2T] and supported in [−L,L], let ν be the measure with transform w g_Z, normalized by ν(ℝ)=|Z|. Its negative mass is ν⁻(ℝ). For L sufficiently large,

    c(Z,T)/L² ≤ inf_w ν⁻(ℝ) ≤ C(Z,T)/L².

The lower side holds even for every finite real measure whose transform coincides with g_Z on the window and vanishes for |u|>L. In particular it does not depend on the extension being a product.

**Lower bound.** Use the step a of finDet such that ra<2T and the r distinct nodes z_j=exp(iγ_j a) are separated. Let P(z)=∏(z−z_j). By the moments on the window, ∫|P(exp(iaτ))|²dν(τ)=0: for the discrete measure of Z the integral is zero and only the moments |k|≤r are used. Hence ∫|P|²dν⁺=∫|P|²dν⁻≤||P||∞² ν⁻(ℝ).

Take n=floor(L/a)+1 and Q_n(z)=∏(z^n−z_j^n). On the circle |Q_n(z)|≤C_Z n|P(z)|, with a constant depending on the nodes but not on n. Indeed, choose the nearest node, use |z^n−z_j^n|≤n|z−z_j| in that factor and bound the rest by 2. The quotient |P(z)|/min_j|z−z_j| has positive infimum by separation and compactness, extending by continuity at the roots. All nonconstant terms of |Q_n|² have frequencies that are nonzero multiples of n. Since na>L their integrals vanish. The constant term is the sum of squares of the coefficients of the polynomial in z^n, at least one by monicity. Hence
    |Z| ≤ ∫|Q_n|²dν ≤ ∫|Q_n|²dν⁺ ≤ C_Z² n² ||P||∞² ν⁻(ℝ).
This gives the bound for each admissible extension.

**Constructive upper bound.** Take b the normalized autocorrelation of a smooth real bump supported in [−1/2,1/2], so that b(0)=1, b'(0)=0, supp b⊂[−1,1] and its Fourier density is nonnegative. Choose an even smooth χ of fixed compact support equal to one on the window. Use
    w(u)=b(u/L)+χ(u)(1−b(u/L)).
For L larger than the support radius of χ, w satisfies all the conditions. The first term multiplied by g_Z has nonnegative density. On the fixed support, the correction e_L=χ(1−b(·/L)) and its first two derivatives are O_T(L^(−2)) by Taylor and parity. By the direct L¹ bound at low frequencies and two integrations by parts at high ones, the L¹ norm of its Fourier density is O_T(L^(−2)). Multiplying by g_Z only sums translations, at cost ≤|Z|. This bounds the negative mass of the total measure.

**Cross-check and scope.** The main antecedent is finDet/finZ in paper 46 and its development in R155_040/041/043; the probe G2_B6 already showed that a finite list does not certify the sign. The lower bound uses the same annihilating polynomial and adds a comparison with Q_n at the scale where the transform has vanished. The upper bound builds profiles of matching order. The lower constant depends on the separation of all the nodes and is not uniform when zeros are added. A rate for the finite obstacle is obtained; the sign of the tail of the real spectrum and of the full form remains unjustified.
