# State041 — Real integrated benefit in a moving energy band

Status: PROVED and audited. Replaces STATE040 as working summary. Goal active, global sign OPEN, papers untouched.

## Result on a full arithmetic integral

POWER_ENERGY_BAND_041 proves for ALL N>=2^80, u=63/2:

    2 int_(exp(T))^(exp(T+L)) h_N(x) B(x) dx < −C_N/25600,
    T=2(N−1)v/(u²−v²), v=1/2+N^(-2), L=sqrt(N)/100,
    C_N=exp(T/2)[rho_N(T)/2−rho_N′(T)]>0.

h_N is the FULL Möbius inverse and B(x)=log(floor(x)!)−xH_floor(x)+floor(x) is the REAL weight with all its jumps. The band moves and grows with N; no list of orders was evaluated and the arithmetic was not truncated.

In the identity W/norm²=ARCH_sharp−F_N, F_N=2int_1^infinito h_N B, this band contributes a benefit greater than C_N/25600. The sign of the full F_N and that of W remain open: the complement still has to be compared, and benefits from distinct representations are not added without their boundary terms.

## What changes relative to the pointwise signs040

The Fourier expansion040 is uniform in the translation. Its factor delta−D is integrated over a FINITE interval, keeping the boundaries exactly. A proved decay of the gamma profile gives a boundary benefit; then the Fourier remainder and the correction of B are bounded. The error is small relative to C_N, the same scale as the contribution, and that is why it decides the sign of this real integral.

A global integral is not interchanged with the critical sum sum|mu(n)|/n, which diverges. Nor is it claimed that an error small relative to C_N suffices to decide total W, whose residue may be much smaller.

Relative to030/031, the result is a MOVING band in the energy region and uses the signed factor of the infinite inverse before the modulus. It is not another integration by parts without inequality nor a new positive point of a kernel.

## Periodic correction with controlled boundaries

The same memo proves for ALL x>=1:

    B(x)=−gamma x−B1({x})logx+kappa+E(x),
    kappa=(log(2pi)−1)/2, −1/x<E(x)<1/(2x).

Elementary proofs of the Stirling and harmonic-number remainders are included. The periodic part keeps the jumps logm at integers, while E is continuous there. A continuous periodic primitive Q2, of norm1/16, produces an explicit integrated bound with boundaries, variation of h(x)logx and int|h|/x. It is an auxiliary tool without its own sign; BAND is already proved with a coarser sufficient bound.

## Evidence and remaining obligation

POWER_ENERGY_AUDIT_041 approves BAND and the periodic expansion. Both were reviewed; the exact constant verifier of BAND was reproduced twice: PASS. The periodic expansion has an autonomous analytic proof. Papers unmodified.

No new W row, arbitrary combination nor window T of Paper47. The positive coverage of W remains that of035 and earlier results. The progress of this round is an integrated and quantified signed benefit, whose compensation with the complement still has to be resolved.
