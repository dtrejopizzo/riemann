# POWER SIGNED AUDIT 019

Status: both construction memos APPROVED, with explicit local scope; no new global certificate. Papers untouched.

## Antecedents and novelty restriction

The targeted search of the corpus places the Euler/Möbius identity in the antecedents already cited by `POWER_TATE_CHAIN_009` §0: `PROOF_L_SHARP_E/J` (Λ*1=log and moments), `A_MU_FACTORIZATION/AUDIT200` and `N_018`. The negativity of an accumulated divisor sum does not by itself constitute a new sign route. The distinct step that would require proof is the inequality of the specific and full adjoint kernel, with its Möbius signs.

Descartes already appears in `phase-162-row-d-first-contact-closure/R162_1501_TARGET_AUDIT.md`, Lemma D, and in the inventory of `phase-200-sign-object/SPEC_SIGN_OBJECT_011.md`. Its application to a concrete rational autocorrelation may provide a new and local lemma; it is not presented as a new general nodal route.

## Accumulated identity: initial independent check

If B(x)=log(n!)−xH_n+n, n=floor x, then B(1)=0, B has slope −H_n on each interval [n,n+1) and its integer maxima satisfy B(n+1)−B(n)=log(n+1)−H_n<0, by sum/integral comparison. Thus B(x)<0 for x>1. The identification with the divisor sum of E0 must keep the convention E0(1)=0 and the jumps log n.

This scalar sign does not certify the sign of the adjoint kernel. In particular, a negative truncation of its summands m=1,2,3 does not imply negativity of the remaining infinite sum. The full reviews of the delivered memos are recorded below.

## Full review of SIGNED_MEAN019 — APPROVED

Read `POWER_SIGNED_MEAN_019.md`. The divisor sum, the bound B(x)≤−(1−log2)(x−1), and the positive integration MEAN are correct. The monotonicity of H_n−log(n+1) gives the bound at integers and the slope −H_n extends it between them. The identity ∫H_N(x)(x−1)dx=J_N(1/2) keeps the endpoints. Thus the mean over ALL dilations is strictly negative.

The adjoint h_N(x)=Σμ(m)mH_N(mx) correctly contains the Jacobian. The identity Σd h_N(dy)=H_N(y) follows by grouping divisors; the pairing F_N=2∫h_N B is correct. The permutations are absolutely convergent: H_N(x)=O_N(x^−33 polylog x), while |E0(x)|=O(x log x) suffices. The condition SIGNED is exactly equivalent to −F_N≥−Arch_sharp/c0; it has not been proved.

FAIL3 is correct for N≥2^17: M2=u²/(2N−3)<1/128, rho(log m)≥1−2M2, rho′≤0 and 1/√2+1/√3>7/6 give h_N^[3](1)<−19/256. It refutes positivity of each inverse prefix in the real kernel. It does not determine the sign of the full h_N, nor of F_N, nor of W. New local result: MEAN sign and explicit failure of preservation by prefixes; the Möbius identity by itself belongs to the antecedents.

A second independent review of SIGNED_MEAN019 agrees on the approval of the ERR normalization, jumps/endpoints of B, MEAN constant, absolutely summable adjoint and FAIL3 with its partial scope.


## Review ARITHMETIC_DIFFERENCES019 — APPROVED

Read `POWER_ARITHMETIC_DIFFERENCES_019.md` and its verifier `tools/power_arithmetic_differences_019_verify.py`; independent run PASS. The formula for C_M keeps the norm at t=0 and the identity c_(N,1)=−C_(N+1)″ is legitimate also for N=1: the density of the second derivative is integrable.

For N≥2, the exact coefficient quotient of r_N=p_N−2p_N′+p_N″ has positive denominator and strictly increasing numerator j(j+1)−2N. Ignoring zeros, it has one sign variation. The constant negative sign and the positive leading coefficient give existence; Descartes gives uniqueness and simplicity. The endpoint N=1 is r_1=x−1. The endpoint N=2 gives x²−x−1. The recurrence and p_j>x p_(j−1), proved by coefficient comparison, give the declared bounds of the unique root for N≥3. No small endpoint is missing.

The arithmetic threshold is correct: u log2>21 and 21²−21−(2N−3)≥1 for N≤211. Thus ALL contacts of the column k=1 have negative autocorrelation and the full comb is strictly positive. The sum is absolutely convergent for u>1/2. No contact has been omitted nor has the sign of W been inferred from this summand.

The difference identity of the isolated comb is exact by the same complementary rational identity. C_N>0 gives P_(N,0)<0, so all differences (−Δ)^rP_(1,0) are negative. This refutes only the attribution of positive differences to the comb via Λ≥0; it does not refute the differences of the full form. The novelty relative to the corpus is the specific unique boundary, its bounds and the signed consequence for the 211 orders, not the general use of Descartes.

## Scope closure of the round

Approved: MEAN and FAIL3, and the unique transition of the whole column k=1 with full positive comb for N≤211. The two constructions keep their carriers: mean over dilations versus original residue, and comb versus full W. The full inverse kernel and the global sign of the table remain open. There is no new certified window T nor modification of papers.
