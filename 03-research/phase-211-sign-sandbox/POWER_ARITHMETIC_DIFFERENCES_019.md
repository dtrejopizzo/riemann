# POWER_ARITHMETIC_DIFFERENCES_019 — A signed frontier of the full comb

Status: **PROVED** single-transition lemma for the whole column k=1; **PROVED** positive sign of the comb for 1<=N<=211, u>=63/2. Full sign of the table **OPEN**. Papers untouched.

## 1. Antecedents and precise difference

Read: the project rules, STATE018, TABLE_DESCENT018, CONE001§4 (positive theta does not imply the ratio inequalities), TATE_CHAIN009§§2–4 and LOW_TABLE018. Consulted the routes index (Euler/Möbius residues, Λ*1=log and moments), the master grid (Bernstein entries and POWER017/018) and CROSSWORD-TO-D.md (linear use of Λ*1=log, signed arithmetic error). No sign is attributed to an Euler identity, to an abstract moment measure, or to the positivity of the initial row.

The difference is an exact property of the autocorrelation of a WHOLE column of the real atoms F_(N,k)(s)=s^k/(s+u)^(N+k): the kernel weighting Λ at k=1 has a single sign frontier, located analytically at O(sqrt(N)). This allows summing the WHOLE comb with sign on an explicit region of N variables, without separate certificates of W for rows 4,5,... and without dropping the polar term from the final obligation. Reverse Bessel polynomials and Descartes are classical tools; the specific result is the frontier and the signed consequence for these contacts.

## 2. Normalisation and kernel

Let u>0, g_M(y)=y^(M−1)e^(−uy)/(M−1)! for y>0, and C_M(t)=c_(g_M)(t). Its Fourier density is (u²+tau²)^(-M). For t>=0, x=ut and d=M−1,

    C_M(t)=e^(−x) p_d(x)/[2^(d+1)u^(2d+1)d!],
    p_d(x)=sum_(j=0)^d (2d−j)! x^j/[2^(d−j)(d−j)!j!].             (C)

Integrating g_M(y)g_M(y+t) gives (C) directly. For f_(N,1), the density is tau²/(u²+tau²)^(N+1), whence

    c_(f_(N,1))(t)=−C_(N+1)''(t).                              (D)

The differentiation is legitimate even for N=1: the density multiplied by tau² remains integrable. No causal function is differentiated at the boundary here.

## 3. A single sign transition for EVERY N

**Theorem.** For each N>=1 there is exactly one chi_N>0 such that c_(f_(N,1))(t)>0 if 0<=ut<chi_N, it vanishes at chi_N, and it is negative for ut>chi_N. The root is simple. Moreover

    chi_1=1, chi_2=(1+sqrt(5))/2,
    sqrt(2N−3)<chi_N<(1+sqrt(8N−11))/2       (N>=3).             (B)

Proof. Write a_j=[x^j]p_N(x)>0 and r_N=p_N−2p_N'+p_N''. For N>=2 the ratio of coefficients simplifies exactly to

    [x^j]r_N / a_j = [j(j+1)−2N]/[(2N−j)(2N−j−1)] .           (COEF)

The denominator is positive for 0<=j<=N, N>=2. The numerator increases strictly with j, is negative at j=0 and positive at j=N. Ignoring possible zero coefficients, there is exactly one sign change. Descartes gives at most one positive root counting multiplicity; r_N(0)<0 and its leading coefficient is positive, so one exists and it is simple. By (D) the signs are as declared. For N=1, r_1=x−1.

The classical polynomial identities, verifiable coefficient by coefficient, are

    (e^(−x)p_d(x))'=−x e^(−x)p_(d−1)(x),
    p_d=(2d−1)p_(d−1)+x²p_(d−2)              (d>=2).            (R)

Also p_j(x)>x p_(j−1)(x) for j>=1, x>=0. Indeed, for 1<=l<=j the ratio between [x^l]p_j and [x^(l−1)]p_(j−1) is (2j−l)/l>=1; the constant term of p_j is positive. For j>=2 the other coefficients except the leading one are strict.

Differentiating the first identity of (R) gives r_N=x²p_(N−2)−p_(N−1) for N>=2. For N=2 one obtains x²−x−1. For N>=3, at the root,

    chi_N² = p_(N−1)(chi_N)/p_(N−2)(chi_N)
            = 2N−3 + chi_N² p_(N−3)(chi_N)/p_(N−2)(chi_N).

All polynomials are positive; the last summand lies strictly in (0,chi_N), by the inequality above. Solving the two inequalities proves (B). QED.

## 4. Signed consequence for the REAL arithmetic

Define exclusively the contribution of the comb

    P_(N,k)(u)=−2 sum_(q>=2) Λ(q)q^(−1/2)c_(f_(N,k))(log q).

All series converge absolutely for u>1/2: the autocorrelation is e^(−ut) times a finite polynomial and Λ(q)<=log q. There is no need to truncate, replace or modify Λ.

**Corollary.** For ALL 1<=N<=211 and u>=63/2,

    P_(N,1)(u)>0.                                             (ARITH)

Indeed log2>2/3 implies u log q>=u log2>21. For 3<=N<=211, 21²−21−(2N−3)>=1>0, so the upper root of (B) is less than 21. The cases N1,2 are explicit and also less than 21. Therefore C_(N+1)''(log q)>0 at ALL contacts q>=2 and c_(f_(N,1))(log q)<0. Each nonzero summand of the comb is positive; q=2 ensures strictness.

More generally, for ANY N, the stretch q>exp(chi_N/u) of the comb has positive summands; the contacts with log q<chi_N/u have negative summands. The single frontier is exact, not an absolute error bound.

## 5. Which inference about differences is falsified

The isolated comb does NOT always supply the desired positive differences. At k=0, C_N(t)>0 for ALL t>=0 by (C), and therefore

    P_(N,0)(u)<0                 (N>=1,u>1/2).                 (NEG)

The same complementary identity that holds for W holds for P because it only uses the rational densities:

    P_(N,k)=P_(N,k+1)+u²P_(N+1,k).

Thus for all r>=0,

    (−Delta)^r P_(1,0)(u)=u^(2r) P_(r+1,0)(u)<0.              (FD)

This explicitly falsifies the concrete lemma "the positivity Λ>=0 makes the full differences of the arithmetic contribution to row 1 nonnegative". The real Λ and its full sum are used, not an abstract measure nor a shifted archimedean constant. In particular, for N<=211 the comb changes sign between k0 and k1. It is not claimed that (FD) falsifies the differences of the FULL row: its archimedean and polar contributions are essential.

## 6. Scope and remaining obligation

ARITH is a new signed inequality for one column, valid simultaneously for 211 orders and all declared rates; the single frontier holds for ALL orders. It does not prove W_(N,1)>=0 for those orders and does not erase the polar term. Nor does it provide the full differences of EVERY order. For the global obligation one still needs an inequality preserving the cancellation of ARCH, comb and polar at variable orders. Neither the generator of row 1 nor this frontier supplies that step by itself.

Auxiliary exact verification: tools/power_arithmetic_differences_019_verify.py checks the polynomial identities, the endpoints and the threshold 211; the symbolic proofs above cover all N without depending on a sweep.
