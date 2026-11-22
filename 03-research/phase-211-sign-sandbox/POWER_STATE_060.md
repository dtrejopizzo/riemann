# POWER_STATE_060 — Uniform positivity cone for all numerators

Status: PROVED in the declared region; global sign OPEN. Papers untouched.

With u=63/2, Q(s)=s/(s+u), q_n=ceil(log_2(n+1)) and J(n)=10^12(nq_n)^3, for ALL n>=1, ALL nonzero real polynomials P of degree<n and ALL integers j>=J(n),

    W[Q^j P/(s+u)^n] > ||Q^j P/(s+u)^n||².

Moreover the absolute integral of the density shifted to height3 is less than2 times the real integral, with a constant INDEPENDENT of n and P. This controls the autocorrelations by2exp(−3|t|)norm² and keeps the WHOLE infinite comb.

Source POWER_UNIFORM_STRIP_060.md, ten sections. Full independent audit POWER_UNIFORM_STRIP_AUDIT_060.md APPROVED. The full proof and its audit were read and verified. It is analytic mathematics, without a campaign over parameters or computation of isolated cases.

## Mechanism and difference relative to054

The exact rational weight in inverse frequency has orthogonal polynomials with an explicit recurrence. This allows controlling the first derivative of an amplitude without causal phase by200(n+2)^(3/2)/(u sqrt(j)). On differentiating repeatedly the change of class(n,j) to(n+3r,j−r) is accounted for.

The large constantD_n of054 only pays the Taylor tail, by Cauchy in L² at height15. The first20nq_n terms are paid with the derivative bound; a norm in fixed dimension is not exponentiated nor globally compared with a Gaussian. Thus a translation norm less than1.1 at heights±3 is obtained, uniform in n. For complex polynomials the individual evaluation of054 is used; the density product is then recovered via Cauchy between opposite heights.

The full arithmetic sum has modulus<2norm², ARCH>4norm² and the polar has modulus<norm². The balance proves the sign with margin. The cutoff goes from the enormousK(n)054 toO(n³ log³n);10^12n^6 also suffices.

## What remains open

The segment j<J(n) is not proved, its positivity is not deduced by descent nor by mixture, and no uniform quadratic cone is claimed.059 only gives a quadratic necessary condition for this class of estimates. No windowT of Paper46 is added. The result053 for thirteen arbitrary poles remains valid separately. Global closure still requires controlling the signed arithmetic interior.
