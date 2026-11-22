# AUDIT_012 — Falsifier of the domination of map011

2026-10-19. Independent check. Read LINK012, certify.py, check_laplace.py and their outputs. Both programs reproduced with python-flint0.9.0, Arb precision 128 bits; they finished without failures.
**Verdict: PROVED the falsifier for the EXACT normalisation of U of LINK011. No exclusion of all rescalings nor closure of D.**

## 1. Corpus and new class

Consulted: index (including entry011 and P1/Gram), grid and crossword; cross-checked the definitions of P46 and audit011. The equality of the map was already refuted and is not retried. The new question is the TOTAL inequality Q_T≥||UF||² for that same U and scale, which remained open. The test and the certification answer exactly that question; no other auxiliary family is built nor are margins on zeros used.

## 2. Exact test, domain and polar

T=4/5, ω=π/(2T), r=3(ω²+1/4)/(9ω²+1/4) define exact numbers. Ball arithmetic encloses them; r is not replaced by an independent float. For f=cos(3ωx)+r cos(ωx), orthogonality gives ||f||²=T(1+r²) and f(±T)=0.

The cosh moments of the two frequencies have the signs and factors written in LINK012. Substituting r cancels them ALGEBRAICALLY. A ball containing zero would not prove that identity, but no such criterion is used here: the cancellation is exact by the formula. F=f/√N is even, polar-free and belongs to H¹₀, hence to the domain of gamma and of Q_T.

The approximation by even C_c∞ with moment correction is valid in H¹. Q_T is continuous for that convergence and U is L²-bounded. The strict negative margin survives on a smooth core. The falsifier is not limited to a matrix realisation without controlled domain.

## 3. Rank-one term and Gaussian tail

From S=κG_s+κvv*+Π with the other two pieces PSD it follows that ||UF||²≥κ|M(F)|². The sum M=Σa_d(d^(−1/2)−d^(−1)) converges absolutely by the bounds of 011. Interchanging it with the integral on a compact set is legitimate.

Grouping k=dn produces exactly b_k and the subtraction z_cτ, with z_c=ζ(3/2)−ζ(2)>0. The normalisation by √N is applied afterwards to M(f). The factors 2 of τ and of map011 are correct.

The bound 0≤b_k≤k suffices for the tail. For a=πexp(−2T), K=12 one checks aK²>1/2, so xexp(−ax²) decreases for x≥K. The two integral comparisons give the tails exp(−aK²)/a and exp(−aK²)/(aK). Multiplying by length 2T, bound |f|≤1+r and the outer factor 2 of the map, one obtains EXACTLY the written ε_M. No sign is attributed to f to discard terms.

The truncated integral of M is of an ENTIRE function: finite sums of exponentials, cosines and exp(exp(2z)). Ignoring the analytic indicator of the callback does not hide a singularity in that integral. The validated evaluation and the positive tail give the bound on |M| in the correct direction.

## 4. Main certificate of gamma and comb

The entire Fourier transform with sinc is correct for the convention of P46. On the real axis f is even and real, hence fhat²=|fhat|² and the symmetric extension of digamma coincides with m. Its complex extension is meromorphic, not entire; the acb computation must keep the singularities, as the memo warns. The final result additionally has the independent verification of §5 without that quadrature.

For t≥100>6ω, the rational formulas of each cosine give |fhat|≤(8/3)ω(r+3)/t². The bound m(t)≤2logt+10 is proved by splitting the Lévy energy into three intervals. I checked K≤1/u+1/2, the integrals 1/4+1/(12t) and 2logt+1−1/t and the tail ∫₁∞K<28/9. The negative C₀ is omitted only for an UPPER bound. Integrating the frequency majorant gives ε_Γ with its coefficients 2/3, 2/9, 10/3 correct.

At T=4/5 the contacts are 2,3,4. The autocorrelation intervals and their weights Λ(2)=Λ(4)=log2, Λ(3)=log3 are correct. The normalisation by N affects both gamma and comb.

## 5. Closed independent verification

The Laplace formula I(a) of §7 was checked via the differential equation of the kernel exp(−a|x−y|). The particular solution, the Robin conditions and the homogeneous coefficient C produce exactly the positive square term with factor 1+exp(−2aT). I=½〈F,v〉 carries the correct factor 1/2.

The normalised gamma energy is C₀+2Σ_j[1/a_j−I(a_j)], a_j=2j+1/2. The translation inequality

    1−c_F(u)=||F−τ_uF||²/2≤u²||F'||²/2

holds for the extension by zero in H¹. Hence the tail ≤2||F'||²Σ_{j≥J}a_j^(−3) and the majorant a_J^(−3)+1/(4a_J²) by sum-integral comparison. The value ||F'||²=ω²(r²+9)/(1+r²) is correct.

check_laplace.py uses J=200 and the exact comb of lem:combsine with coefficients (r,−1)/√(1+r²); the negative sign comes from e₃=−cos(3ωx). Reproduced:

    partial gamma = −0.2361826974540901495…,
    upper tail <0.000098513228,
    comb = −0.2377321365688090439…,
    Q_T(F)<0.001647953.

The main certificate produced Q_T(F)<0.002351. These are compatible upper bounds; the second check removes all dependence on quadrature for gamma and comb.

## 6. Certified result and scale

The reproduction of certify.py gave balls with

    |M(F)|>0.1812652378,
    κ>7.95393245,
    ||UF||²≥κ|M(F)|²>0.26134304.

Even using the weaker bound Q<0.002351 one obtains

    Q_T(F)−||UF||²<−0.25899<0.

Hence the exact inequality posed for U011 is false. It was not necessary to know the full ||UF||² nor to prove a sign of Q_T separately.

This refutes the fixed scale, not all c_T||UF||². The exploratory quotient is not a certified threshold for all rescalings. From the conservative bounds some large scales could be excluded, but not arbitrarily small or T-dependent ones; the memo does not claim that conclusion.

**Final verdict:** equality011 already refuted and domination012 now refuted for that same candidate. The auxiliaries −R/FE remain valid; no general conclusion about other maps or about D. Full target D OPEN and active.
