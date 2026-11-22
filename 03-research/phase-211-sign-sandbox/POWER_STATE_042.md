# State042 — Global cancellation and residual tail at absolute scale

Status: PROVED and audited. Replaces STATE041 as working summary. Goal active, global sign OPEN, papers untouched.

## Result relevant to the precision of the full form

POWER_RENORMALIZED_TAIL_042 uses the exact mass sum_(n>=1)J_N(n)=1, h_N=−J_N′ and the periodic expansion041 to cancel GLOBALLY the affine term of B. With kappa=(log(2pi)−1)/2 one obtains exactly:

    F_N/2=−gamma+(kappa−gamma/2)J_N(1)+R_N,
    R_N=−int_1^infinito h_N B1({x})(logx+gamma)dx
                                      +int_1^infinito h_N E(x)dx.

The term J_N(1), the constants, the jumps and the boundaries are kept. The identity alone does not determine a sign.

For ALL N>=2^80, if T=(N−1)/992+5 and X=exp(T), one proves:

    |R_N^tail| <=N(T+2)exp(−3T/2)<exp(−N/1000).

This is an ABSOLUTE bound, not relative to the exponential energy C_N of041. Consequently:

    W[g_N]/norm²=ARCH_sharp+2gamma−(2kappa−gamma)J_N(1)
                           −2R_N^interior+epsilon_N,
    |epsilon_N|<2exp(−N/1000),

with the real interior from1 toX. The sign of the interior expression and a margin dominating epsilon_N have not been proved.

## Mechanism and difference in scope

Euler by cells and MASS022 eliminate the affine term without interchanging an integral with a divergent critical series. After that cancellation, the cutoff040 implies q(T)>1/2+2000/N; the real dilation allows controlling ALL divisors and the derivatives: |h(x)|<=Nx^(-3/2), |h′(x)|<=2Nx^(-5/2) on the tail.

The continuous periodic primitive of norm1/16 keeps the lower boundary X explicitly. Together with |E|<=1/x, it produces the declared absolute decay. Neither monotonicity of h nor a favourable sign of the periodic error is presupposed.

Relative to041, the precision scale of the tail after globally cancelling the principal term is resolved. The energy benefit of another representation is not added nor is the whole complement called favourable: the renormalised interior remains pending.

## Audit and global state

POWER_RENORMALIZED_AUDIT_042 approves the whole proof. Normalisations, boundaries, constants and the passage to absolute scale were reviewed; the exact verifier was reproduced twice: PASS. No new W cases nor prime campaigns were evaluated.

No new positive W coverage, arbitrary combination nor window T of Paper46. Rows1..17, all k>=0 at u31.5, and the earlier regions are kept. The global objective requires deciding the interior balance and then covering the sufficient table/carrier; it remains OPEN.
