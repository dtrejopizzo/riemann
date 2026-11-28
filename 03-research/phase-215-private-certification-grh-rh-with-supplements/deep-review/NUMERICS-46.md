# Fixed windows of paper 46: independent reproduction

Scope clarified by the author: T=(log 5)/2 and T=2.8022 are fixed parameters. No attempt is made to discover or optimise them. What is reviewed are the arguments and certificates that claim to prove bounds on those windows. The programs of this evidence folder do not modify manuscripts.

## Quadrature remainder in the first window

The reconstruction uses 480 panels of length 1/2 and Gauss–Legendre with 46 nodes, with Arb balls of 640 bits. The ellipse of parameter ρ=3.2 over each panel has imaginary semi-axis y=(ρ−ρ⁻¹)/8=0.3609375. For w=1/4±iτ/2, Re w≥1/4−y/2>0. One has |w+8|<130 and Re(w+8)>8.

The digamma recurrence and the Binet bound written in the manuscript give |ψ(w+8)|<7, |w|⁻¹<15 and Σ_{k=1}^7 |w+k|⁻¹<3. Hence |ψ(w)|<25. On continuing the real symbol analytically one uses (ψ(1/4+iτ/2)+ψ(1/4−iτ/2))/2, not the non-holomorphic operation Re ψ on complex τ. With log π<2, s∞<1, A<3 and cosh(y log 4)<2 one obtains |g(τ)|<34.

The printed Bessel bound can be strengthened at no cost using its Legendre representation:

`j_n(z)=(2i^n)⁻¹ ∫_{−1}^1 exp(izt) P_n(t) dt`.

Cauchy–Schwarz and ∫P_n²=2/(2n+1) give √(2n+1)|j_n(z)|≤exp(|Im z|). Therefore, for all the indices used,

`|√((2i+1)(2l+1)) g(τ) j_i(Tτ) j_l(Tτ)| < 34 exp(2Ty) < 68 < 70`.

This avoids multiplying the bound by the indices of the Legendre functions. There is no need to assume the smaller decimal 1.5·10⁻⁴³ announced in the manuscript.

For an analytic function bounded by M=70 on the ellipse, the Chebyshev coefficients of degree k≥1 have modulus ≤2Mρ⁻ᵏ. Gauss with 46 nodes is exact up to degree 91. For each T_k, the absolute value of the integral and that of the rule are ≤2; their difference is ≤4. The odd degrees contribute zero by symmetry. By geometric summation the error on [−1,1] is at most

`8M ρ⁻⁹² / (1−ρ⁻²)`.

On multiplying by 480 changes of variable of factor 1/4 and by 2T/π, one obtains an error per entry smaller than **1.282·10⁻⁴²**, and hence smaller than the ball **2·10⁻⁴²** used in the reconstruction. This is a direct proof of the sufficient remainder; it does not presuppose a convention for numbering the nodes in the theorem cited.

The program `evidence/verify_remainders_46.py` checks with ball predicates the numerical inequalities of this proof. It also checks Λ*₂₈₀<4.5·10⁻²⁰ and Λ*₃₃₀<3.9·10⁻⁷⁰: the first term of the series is multiplied by 1/(1−r), with r=c²/(2k+3)², which dominates all the successive quotients. Result saved in `remainders_46_arb.json`.

## Matrices and inertias

`rebuild_matrix_46.py` generates the 165×140 matrices in each parity, including the preceding ball. The Bessel recurrence is restarted by direct evaluation when its radius grows; all the Bessel balls pass the predicate radius<10⁻⁶⁰. The resumed run finished and wrote `matrices_46_arb.json`.

`verify_inertias_46.py` constructs the matrix of proposition `prop:lowercert`. The products of columns over indices 280≤l<330 are summed explicitly. The tail of each column of G is dominated by (ω₊+ω₋)√Λ*₃₃₀; the products of tails are enclosed by Cauchy–Schwarz. The cosh/sinh coefficients are computed with Bessel I. The tail of their norm is obtained by subtracting from sinh T±T the finite sum of squares, taking the non-negative upper endpoint.

Only the diagonal entry of the border is replaced by a lower bound, obtaining R′≤R. For the odd sector with c=1/2 positivity is proved by interval LDL. In the other cases the principal block formed by the first coordinate and the border is used: if its determinant is negative it has exactly one negative direction; positivity of its Schur complement is verified. In the even case of W_T the border column is first aligned by means of a Householder matrix constructed with its midpoints; its invertibility is certified by means of ‖HᵗH−I‖∞<1.

**Status: the four inertias passed.** The direct LDL elimination of the even Schur complement of W_T loses precision through interval dependency. That failed attempt is kept in the result, followed by a successful verification: a unitriangular L with exact midpoint entries and a positive diagonal D are constructed; P=D⁻¹ᐟ²L⁻¹ is invertible, and P S Pᵗ is computed with balls. Its diagonals minus the sum of moduli off the diagonal are all positive, with minimal margin greater than 0.9999999999999999999999. Gershgorin proves positivity; it is not inferred from the success of a midpoint factorisation.

| Form / parity | μ | Negative inertia of the border | Positive evidence |
|---|---:|---:|---|
| Primitive even | 2.5·10⁻¹² | 1 | LDL, minimal pivot >0.00846 |
| Primitive odd | 3·10⁻¹⁰ | 1 | LDL, minimal pivot >0.02026 |
| W_T even | 10⁻¹⁸ | 1 | Certified congruence and Gershgorin |
| W_T odd | 10⁻¹⁶ | 0 | LDL, minimal pivot >8.14·10⁻¹⁴ |

The minimal pivot of the midpoint factorisation of the third case is approximately 0.00044730756, consistent with the author's table, but the certificate is the congruence with intervals and Gershgorin. Results in `inertias_46_arb.json`; remainders justified above and in `remainders_46_arb.json`.

**Verdict for the bounds requested at T=(log 5)/2: (a), by means of this independent reconstruction and the rounding corrections already indicated.** By inclusion of supports they extend to smaller windows: the new terms of the sum over primes do not contribute when the translates of the supports do not intersect (coincidence at an endpoint has measure zero). This does not certify that the absent original program was exactly the same.

The window 2.8022 is still pending its filter and the 17 announced verifications.
