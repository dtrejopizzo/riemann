# POWER_STATE_062 — Indispensable residue in the same case129

Status: quantitative diagnosis PROVED; no new sign region. Global objective OPEN. Papers untouched.

The renormalised balance042 was evaluated on the SAME atom129 already decided061. With normalisation by norm², beta=log(2pi)−1−gamma,

    AFF=ARCHsharp+2gamma−beta J129(1),
    R=(ERR+2gamma−beta J129(1))/2,
    W/norm²=AFF−2R.

The audited rational intervals are

    AFF ∈[−60446492280,−60446492279]/10^12,
    R ∈[−30223246208,−30223246207]/10^12.

The affine part has approximate deficit.06044649228; the full residue repairs it almost exactly. Hence that affine part is of no use as a positive base from which to simply neglect the rest. R includes the periodic termB1 ANDthe Euler error; the whole repair is not assigned to one of them.

Sources POWER_GAMMA_AFFINE_BALANCE_062.md and POWER_GAMMA_AFFINE_AUDIT_062.md. Verifier tools/power_gamma_affine_balance_062_verify.py reproduced independently, exit0/PASS. It reuses024 and061 without newN, cutoffs or precisions. It does not use ABS-TAIL042, which requiresN>=2^80.

The R computed here usesERR061 already known: it is NOT a new independent estimate capable of propagating the sign. The small marginW keeps the proof061 and is not inferred from independent roundings ofAFF/R. The comparison of differences inN ofJ,K andARCHsharp remains pending; positive exteriorK and concaveq do not order those terms. The regroupings024/026/030/042 are not counted as new tools.

## Query063 — direct integration reviewed and deduplicated

The proposal of boundingR directly by cells was reviewed by cases; the divisor identities were checked. For U=B+gamma floor(x)+gamma/2−kappa, R=integral hU and the boundary isJ(1)(3gamma/2−kappa). Integrating by parts keeps dU=−H_floor(x)dx+sum_(m>=2)(logm+gamma)delta_m. The identity sum_(m<=y)mu(m)H_floor(y/m)/m=1 follows from mu*1=delta; withJ=sum mu(m)w(mx), it returns integralH_floor J=integralw. Likewise sum logm J(m)=sum Lambda(m)w(m). MASS eliminates the remaining sum ofJ.

Thus the direct evaluation reconstructs the same contacts, resolvent andJ1 already used in061/062. No other implementation was run and no independent bound ofR was obtained. The factorial/Stirling route was reviewed via insight048 and also returns to030/042 or to the Erlang components033; no new hypothesis avoiding their losses appeared. These are deduplications of concrete proposals, not proofs of general impossibility nor new sign results.
