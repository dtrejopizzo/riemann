# State040 — Opposite signs at the centre and positive tail at constant distance

Status: PROVED and audited. Replaces STATE039 as working summary. Goal active, global sign OPEN, papers untouched.

## Uniform pattern of the full arithmetic inverse

POWER_CRITICAL_BALANCE_040 proves for ALL N>=2^80, u=63/2, v=1/2+N^(-2), t_v=2(N−1)v/(u²−v²):

    h_N(exp(t_v))/H_N(exp(t_v)) < −1/N,
    K_N(exp(t_v))/G_N(exp(t_v)) > 1/N.

The denominators H_N and G_N are positive. These are opposite signs of two FULL arithmetic kernels at the SAME centre t_v=(N−1)/992+O(1/N), not prefixes of their sums nor evaluations of W. Negativity of h is not a counterexample to the sign of W.

It is further proved, for the same N, a whole tail:

    h_N(exp(t))>0 and K_N(exp(t))>0
    for ALL t>=(N−1)/992+5.

The certified start is at CONSTANT distance from the centre; it improves the O(sqrtN) shift of039, though with the declared range N>=2^80. It does not identify the exact transition nor prove uniqueness of a transition. The kernel coordinate t=logx is not the window T of Paper46.

## Insight and error control

The elementary factor of the infinite product is separated before estimating it. The identity with the fractional part gives, for Re z>=0 and |z|<=1/8,

    1/zeta(1+z)=z−gamma z²+R3(z), |R3(z)|<=9|z|³.

On inverting Fourier with z=delta−i xi, the full ratio is expressed through delta−f′(0)−gamma[delta²−2delta f′(0)+f″(0)], with explicit remainder less than1/(10000N) in the central regime. delta>0 and absolute convergence of the infinite product are kept. No formal series nor probabilistic interpretation of signed weights is used.

A new elementary bound, −2q′(t)/t<q″(t)<0, is proved from the positive coefficients of P_N and Riccati. It provides effective limits for f′, f″ and a lower bound q′>50/N. Thus the error is genuinely smaller than the sign margin of both inverses. For the tail, delta between2000/N and1000/sqrtN gives positivity by the same remainder and links with039; the shift of the first centre is less than5.

The novelty relative to039 is controlling the scale1/N of the inverse near the centre and extending the tail to constant distance. The local factor replaces the centring with moments that deteriorated when delta dropped to that scale.

## Evidence and remaining obligation

POWER_CRITICAL_AUDIT_040 approves expansion, curvature, central pattern and constant cutoff. All proofs were reviewed; there was an additional independent review of the curvature. The extended exact verifier was reproduced twice: PASS. No sweep over N, primes or numerical W cases was done.

Control of the integrated interior contribution and its balance with ARCH_sharp is missing to decide W. The signs of these kernels, even full ones, are not automatically the sign of the form. No new W row, arbitrary combination nor extension of T. The coverage035 and earlier results are kept: rows1..17, all k>=0 at u31.5, additional regions and atom211,1. The global objective remains open.
