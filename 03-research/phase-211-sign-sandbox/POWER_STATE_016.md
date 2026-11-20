# State016 — exact localisation of the descent gap

Status: structural results and obstructions PROVED; global sign OPEN. Goal active. Papers untouched. Replaces STATE015 as the current summary.

## What remains proved

Eight arbitrary poles >=63/2: W>norm²/1000. Fixed confluent block of dimension12: separate certificate. Strong bridge: it suffices to prove all confluent blocks of one rate, without a uniform margin in dimension. Theorem015: each orbit Q^k V_N is uniformly positive for k large enough with N fixed. Not all initial blocks are proved.

## New exact pattern

POWER_DESCENT_016 proves W[f]=W[Qf]+W[Lf], Q=s/(s+u), L=u/(s+u), with full polar and comb. Consequently each fixed order of finite differences of W[Q^k f] eventually has alternating sign. No global Rayleigh monotonicity is claimed.

The binomial refinement keeps the original energy. Its norm weights are exactly a mixture of Binomial(m,p) distributions, p=tau²/(u²+tau²), under the spectral measure of f. The error for Lipschitz observables is <=Lip/(2sqrt(m)). The edge with a fixed number of factors L has mass AND energy contribution tending to zero. That edge is precisely what015 covers directly. The sign obligation remains in the interior, where both indices grow together.

## Why two extrapolations do not work

POWER_JOINT_SCALE_016: for F=s^k/(s+u)^(N+k), Z=tau²/(u²+tau²) has law Beta(k+1/2,N−1/2). If k/N->c>0, the normalised contacts tend to cos(u sqrt(c)t), not necessarily to0. c can be chosen in any linear cone so that the contact2 tends to1. It is not a counterexample to the full sign.

The temporal mean is (N−1/2)/u for ALL k, and the variance for k>=1 is (N−1/2)[1+1/(4(k−1/2))]/u². Jensen prevents making the exponential weights used in015 uniform in N, whatever the growth of k. Centring does not make the two opposite weights uniform simultaneously either. Estimates exploiting cancellation and the positivity cones themselves remain open.

POWER_DESCENT_AUDIT_016: the high-pass zeros impose vanishing ordinary moments, continuous functionals in the weighted norm used. Not even the primitive data are approximable by that union: (1/4−D²)g, g compact positive, has vanishing Tate moments but positive ordinary integral. If k tends to infinity and there is a common strong limit, that limit can only be0. This limits that topological bridge, not every possible approximation.

## Falsifier of an inference, not of the real form

W_4=W−4norm² keeps mixtures, partitions and eventual positivity015, but its normalised value on e^(-63y/2) is <-1. Rational verifier tools/power_descent_016_verify.py reproduced PASS. Hence structure+tail does not imply initial sign; the descent needs an additional estimate sensitive to the real multiplier. It is not claimed that W_4 keeps the initial certificates of W.

## Review and next obligation

The identities of DESCENT, the full formulas of JOINT_SCALE and the moment lemmas of the audit were reviewed. The final independent review of both memos is APPROVED in POWER_DESCENT_AUDIT_016 §§6–8; the audit's own lemmas were reviewed as well. No numerical campaign was used.

The next construction must treat the interior of the partition with the full signed comb or supply a controlled moment correction. Do not repeat tail density, uniform disappearance of contacts in linear cones, nor exponential weights uniform in N. The quadratic spectral scale and the sign cones remain OPEN: they have not been refuted. The global objective is neither completed nor blocked.
