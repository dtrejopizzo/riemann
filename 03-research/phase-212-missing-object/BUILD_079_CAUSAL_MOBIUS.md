# Construction 079 — Causal Möbius corrector with moment repair

Status: formulas (1)–(5), domains and the failure of V1 checked independently. Positivity of V2 pending. No global sign nor novelty of the ingredients is claimed. It is developed under the permission to build incomplete candidates and review them afterwards.

## Data and written operator

We first work with F smooth, compactly supported in I=(-T,T), with both moments zero. Functions are extended by zero. Let U_l F(t)=1_I(t)F(t-l), l>0. Since I is an interval, U_l U_r=U_(l+r). If l≥2T, U_l=0.

Define, with finite sums n<exp(2T),

    E=Σ_{n≥2} Λ(n)/(sqrt(n) log n) U_log n,
    L=Σ_{n≥2} Λ(n)/sqrt(n) U_log n,
    R=exp(-E)=Σ_{n≥1} μ(n)/sqrt(n) U_log n.

The exponential is a finite polynomial: E^k=0 if k log 2≥2T. The equality with Möbius is checked coefficient by coefficient through the formal Euler product; it does not require convergence of an infinite series. It is a formula of its own, not an inversion of the target form. For generic weights w one defines E_w and exp(-E_w), but their coefficients are not μ(n).

Antecedents of the ingredients: 212-58 (arithmetic inverse on cells), R170_856 (causal Möbius extraction), 212-73 (finite-rank terms), 212-77 (continuous non-HS Gram). The purpose here is to compute a concrete realization with exact moment correction, not to attribute a sign to the Möbius inverse.

## Exact repair of the two moments

Let e_σ(t)=exp(σt/2) on I, σ=±1, and ℓ_σ(f)=∫_I e_σ(t)f(t)dt. The moment matrix H is

    H = [[2 sinh T, 2T], [2T, 2 sinh T]].

It is invertible for T>0. Write Qf=f−Σ_σ e_σ (H^(-1)ℓ(f))_σ. Q is the orthogonal projection onto P_T (also for complex functions, with the usual conjugation convention). Let Y=Q(R−I)F; then QRF=F+Y.

The moments of each shift are explicit. With l=log n<2T,

    ℓ_σ(U_l F)=exp(σl/2)∫_{-T}^{T-l}exp(σs/2)F(s)ds
              =−exp(σl/2)∫_{T-l}^T exp(σs/2)F(s)ds.

The second equality uses ℓ_σ(F)=0. Thus every repair is determined by written boundary integrals, not by an eigenvector or a minimization.

## First square and its residue

Put β=1−C0>0, where C0=ψ(1/4)−log π. Define the explicit increment operator

    Jf = ( f, (u,t)↦sqrt(K(u)/2)[f(t)−f(t-u)] )

with values in L²(R)⊕L²((0,∞)×R). Its norm is

    b(f)=||Jf||²=Arch(f)+β||f||².

The integral is kept as a joint square. Its divergent diagonal is not separated. Also denote by b(f,g)=<Jf,Jg> its polarization.

The initial candidate is V^(0)F=JQRF=J(F+Y). Its exact residue is

    a_T(F)−||V^(0)F||²
      =−β||F||²−2 Re<F,LF>−2 Re b(F,Y)−b(Y).             (1)

All terms are finite for the smooth core: R produces a finite sum of piecewise smooth functions with compact support; the repair adds cut exponentials. They are compactly supported BV, hence belong to H^s for s<1/2 and to the logarithmic domain of J.

## First correction motivated by an exact failure

If 2T≤log 2, E=L=0 and R=I. Then Y=0 and the residue (1) is −β||F||²<0 for F≠0. The initial candidate can NOT be a positive piece dominated by a_T, not even in the window without primes. This failure is exact, not numerical.

To remove that overload, the identity channel is removed from the corrector and one defines

    V^(1)F=JQ(R−I)F=JY.

Now the square vanishes exactly when there are no contacts. It is nonlinear in the weights through exp(-E), and uses the two constraints through the boundaries of Q. Its residue is written as

    ρ^(1)(F)=Arch(F)−2 Re<F,LF>−b(Y).                    (2)

ρ^(1)≥0 is not claimed. The modification repairs the failure of the window without contacts, but does not yet provide the arithmetic mechanism that signs (2).

## Explicit equations of the residue, without spectral shorthand

For n≥2 with μ(n)≠0, put d_n=μ(n)/sqrt(n),

    Z_nF=U_log n F−Σ_σ e_σ (H^(-1)ℓ(U_log n F))_σ.

Then Y=Σ_n d_n Z_nF and

    ρ^(1)(F)=Arch(F)−2Σ_n Λ(n)/sqrt(n) Re<F,U_log n F>
             −Σ_{m,n≥2} μ(m)μ(n)/sqrt(mn) b(Z_mF,Z_nF). (3)

The last sum keeps the cross terms m≠n; they are not discarded. The next design problem is to find a signed cancellation between those cross terms, the contacts and Arch. Replacing that obligation by «ρ^(1) is positive» does not constitute a proof.

## Controls and limits of what was obtained

Identity (1) also exists for rescaled weights and for a Beurling delay system, replacing E and L. The exact identification of R with μ on integers only corresponds to the true weight; this does NOT prove the sign of the residue. There is not yet a sign line distinguishing all falsifiers.

Result: two explicit candidate formulas, complete residue computed, first failure located and a modification that removes that failure. Positivity of the second residue: OPEN. No proof of a_T≥0 has been obtained.

## Second correction: limiting the gain of the corrector

Status of this section: algebra and integrability checked independently; no global sign.

Correction V1 keeps too much energy in high-frequency packets with disjoint translations. Its quadratic gain there is Σ_{2≤n<exp(2T)}μ(n)²/n, which already exceeds 1 when 2,3,5 enter. The moment repair does not affect those packets if each translate keeps its support and its zero moments intact.

The amplitude is modified by a formula independent of a_T:

    S_T=Σ_{2≤n<exp(2T)}|μ(n)|/sqrt(n),
    α_T=1/[2(1+S_T)],
    W_T=α_T Q(R−I)Q,
    V^(2)F=J W_T F.

Here Q is extended to L²(R) as the projection onto P_T of the restrictions to I, followed by extension by zero. Thus ||W_T||≤S_T/[2(1+S_T)]<1/2. No normalization by an eigenvalue of a_T or its inverse is used. If there are no contacts, W_T=0.

Define D_u=I−τ_u on the line and C_u=D_uW_T−W_TD_u. For primitive F in the smooth core,

    D_u W_T F=W_TD_uF+C_uF.

By expanding this square,

    a_T(F)=||V^(2)F||²+P_T^new(F)−B_T^new(F),             (4)

with

    P_T^new(F)=<F,(I−W_T*W_T)F>
       +(1/2)∫_0∞K(u)<D_uF,(I−W_T*W_T)D_uF>du,

    B_T^new(F)=β||F||²+2 Re<F,LF>
       +(1/2)∫_0∞K(u)[2 Re<W_TD_uF,C_uF>+||C_uF||²]du. (5)

One has P_T^new(F)≥(3/4)b(F). This does NOT prove P_T^new≥B_T^new: β and the contacts are still present, and the mixed commutator term has no known sign. It is not replaced by an absolute value.

Identity (4) explicitly keeps the commutation defect with the window and with the constraints. That is the term to modify in the next design. C_u is not a symbol of the original form nor a residue defined by its eigenvalue: it is the commutator of operators already written.

On the core considered all integrals of (5) exist: W_TF is compactly supported BV and lies in the domain of J, W_T is bounded, and C_uF=D_uW_TF−W_TD_uF has square norm integrable with weight K. The mixed term is integrable by Cauchy–Schwarz in (u,t); this is used here only to justify existence, not to estimate the sign.

The factor α_T removes the gain failure of the disjoint packets, since α_T²Σμ(n)²/n≤α_T²S_T²<1/4. It is not claimed to remove other negative witnesses of the residue. The arithmetic part of W_T remains causal and nonlinear in the weights before specializing to Λ.


## Localization of the commutator and change in the order of operations

New computation pending review. Put χ=1_I and Π=χ−Q, the rank-two projection onto the cut exponentials. Since Qχ=χQ=Q,

    W=α Σ_{n≥2} d_n Q τ_log n Q,
    A_u=[D_u,Q]=Qτ_u−τ_uQ,
    C_u=α Σ_n d_n(A_u τ_log n Q+Q τ_log n A_u).           (6)

Here d_n=μ(n)/sqrt(n), with the same finite cutoff. Translations of the line commute; hence all of C_u comes from Q, not from a commutator between arithmetic delays. More explicitly,

    A_u=M_(χ−χ(·−u)) τ_u−Πτ_u+τ_uΠ.                     (7)

The first term is supported on strips at the endpoints; the other two have finite rank. No sign is attributed to any of these pieces.

Instead of JWF, the candidate is now defined with the order reversed in each channel:

    V^(3)F=(WF, (u,t)↦sqrt(K(u)/2)(W D_uF)(t)).          (8)

It is an explicit formula in the same data. It does not require D_uF to belong to P_T: Q inside W performs that correction. One has

    ||V^(3)F||²=||WF||²+(1/2)∫K(u)||W D_uF||²du≤b(F)/4.

Put Z=(I−W*W)^(1/2), the root of a bounded positive operator independent of the target form. If one wishes to avoid the root notation, all following terms are read as <g,(I−W*W)g>.

    a_T(F)=||V^(3)F||²+||ZF||²
       +(1/2)∫K(u)||Z D_uF||²du
       −β||F||²−2 Re<F,LF>.                             (9)

This identity no longer contains C_u. The integrals exist by boundedness of W and Z and by F∈Dom(J). The modification removes the commutator exactly, but leaves the cost β||F||²+2 Re<F,LF> to be controlled against the Z channels. It is not claimed that this cost is dominated.

Relation with V2: the difference between the squares of V2 and V3 is exactly the integral of the mixed term and of the square of C_u in (5). It has no predetermined sign; V3 is not declared smaller than V2.

Design warning: (9) is an exact decomposition of the positive energy b by a contraction. The contraction alone remains valid for the falsifiers. The global proof would require an additional cancellation between the cost and the Z channels that exploits the true coefficients; it is not obtained here.

## Numerical diagnosis: the first channel of V2 and V3 exceeds the margin

NUMERICAL, not certified. The lower even vector of T=0.8 from the enriched solver was reused, stored in `build_079_data/vec_T0.8.pkl`. Origin: an earlier temporary working folder. The saved form value is 5.29432592315062e−12; it was not recertified here.

The script `build_079_data/check_extraction.py` reconstructs the vector, corrects its two moments at working precision and evaluates the channel WF by Gauss quadrature split at all boundaries of the original and translated pieces. Orders 32,64,96 produce respectively

    ||WF||² = 0.008298446283822565,
              0.008298446283822581,
              0.008298446283822570.

The reconstructed norm differs from 1 by less than 3e−15; the moments before correction are smaller than 7e−16. Both versions have ||V^(j)F||²≥||WF||². Compared with the saved value of a_T, the first channel already exceeds the margin by approximately 1.57e9. This is strong numerical evidence against domination of the square, not a proof with interval arithmetic.

Design consequence: changing the order of increments is not enough. The defect already exists in the channel WF, common to V2 and V3. α is not adjusted using the observed eigenvalue. A corrector that vanishes structurally on the near-null directions is needed; an analytic diagnosis with the explicit tests of the corpus is investigated before replacing its formula.

## Analytic discard of V2 and V3 for large windows

Status: proof checked, RELATIVE to the following CITED estimate from the corpus. It is not rederived through objects external to the sandbox.

Input: R160_M4_R1 §4 Theorem B(i), paragraph «Primitive bottom», and ANNEX_MARGIN_CONFLICT §3, provide a written test

    X_T=Mχ_T−a_T^corr u_ev∈P_T,
    a_T(X_T)≤C exp(cT) exp(−2π exp(2T)),                 (10)

with χ_T→1 on compacts, 0≤χ_T≤1, and u_ev supported in (-1/2,1/2). The bound of THIS test is used, not a bound on the infimum. M is the explicit profile of BUILD080 (a constant normalization factor does not alter the argument).

For negative t define

    H(t)=Σ_{n≥2} μ(n)/sqrt(n) M(t−log n).

The tail bounds of M and its derivatives give, for each fixed j,

    |M^(j)(t−log n)|/sqrt(n)
      ≤C_j exp(−(17/2+2j)t)n^(8+2j)exp(−π n² exp(−2t)). (11)

On negative compacts the majorant is summable. The term n=2 dominates as t→−∞: putting X=exp(−2t), one obtains

    H(t)=16π⁴·2⁸ X^(17/4)exp(−4πX)(1+O(1/X)),          (12)

in the normalization of M used in BUILD080. The remainder n≥3 is exponentially smaller, also after differentiating a fixed number of times. Hence (1/4−∂²)H(t)<0 for t sufficiently negative.

Choose a fixed interval J⊂(-∞,-2) in that zone and η≥0 smooth, compactly supported, nonzero in J. Then g=(1/4−∂²)η is primitive and

    c_g=<g,H>=<η,(1/4−∂²)H><0.                         (13)

For large T, Q_Tg=g and Q_TX_T=X_T. By the formula for W_T,

    <g,W_TX_T>/α_T=<g,(R_T−I)X_T>→c_g.                (14)

The correction u_ev disappears exactly because, for t∈J and n≥2, t−log n<-1/2. The output projection disappears when pairing against g. The remaining limit follows from (11), 0≤χ_T≤1 and pointwise convergence of the cutoff. The cutoff n<exp(2T) does not obstruct dominated convergence either.

By Cauchy–Schwarz, for large T,

    ||W_TX_T||²≥|c_g|² α_T²/(4||g||²).                 (15)

The normalization of BUILD079 satisfies S_T≤2exp(T), hence α_T≥exp(−T)/6. Thus the first channel is ≥c1 exp(−2T), incompatible with (10). Both candidates V2 and V3 contain that channel, so their residues are negative on X_T for T sufficiently large.

More generally, to keep the domination with THIS same corrector form and a scalar amplitude α_T, (10) and (15) would force

    |α_T|≤C′exp(c′T)exp(−π exp(2T)).                   (16)

An amplitude of that scale is not declared impossible; it is shown that a merely exponential normalization does not repair the mechanism. BUILD080 changes the operator to annihilate the profile, instead of adjusting the scalar using the eigenvalue.

This proof does not refute a_T≥0. It refutes the domination of the concrete squares V2 and V3, under the input (10). The numerical diagnosis T=0.8 plays no part in the proof.
