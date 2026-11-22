# Recorded state — arithmetic compensation of a full block

Status: PROVED indicated cases; global sign OPEN. Goal active. No paper modified.

## Verified progress of the round

POWER_ARITHMETIC_BLOCK_007 and POWER_BLOCK_AUDIT_007 prove W[h]>||h||²/10000 on ALL of V12=exp(-31.5y) times polynomials of degree<=11 (zero extension to y<=0). It includes all cross terms and the whole prime tail; it is not only the vector chosen in006. Exact rational certificate re-run three times independently: AP+contact2>.0008 minus1e−8, tail in norm<.0006. The test006 belongs to this block and has negative AP; the proof crosses a region where the arithmetic contribution is necessary.

Accumulated valid results: all triples a_i>=32 with margin1/20 (004); confluence4 with margin1/5 and local AP transport of all numerators (005); fixed ladder32..37 certified (003); approximation bridge in form norm (002). None of this is extrapolated to all orders.

## Two false patterns discarded with proofs

- POWER_HIGH_ORDER_PM_NOGO_007: at rate31.5 and n=2^17, the AP Rayleigh quotient with numerator1 decreases when any pole is raised. It refutes universal numeratorfixed AP monotonicity, not eigenvalue monotonicity nor the sign.
- POWER_PRIME_PATTERN_FALSIFIER_008, audited in POWER_AUDIT_008: in the same fixed confluent family, the test f=(D²−1/4)[y^(n−1)e^-31.5y], n=2^17, has A=B=0, ARCH<−3.83||f||², and each prime-power contact<=1024 worsens the deficit. The later tail remains open; no full negative sign is claimed. Thus the fact that2 repairs block12 does NOT constitute a universal pattern of repairing primes.

## Pending requirements, with no change of scope

1. Four arbitrary exponents>=32: only an earlier high range and a confluent/local neighbourhood exist; uniformity not proved.
2. All orders on a dense family: open. The bridge is proved, but the margins of finite blocks do not prove uniformity nor passage to the limit without the sign of all of them.
3. Closure of the sign of Paper46: not obtained. Do not edit papers nor declare the goal complete.

## Next useful problem

Look for an identity or inequality for the FULL arithmetic sum that keeps the mixed-sign autocorrelation. Do not repeat AP monotonicity in dimension nor the inference from favourable contacts of a vector. The test008 leaves an explicit obligation (TAIL) but not a solution: it will have to be compared with already recorded residues before proposing a new construction. The earlier record on block12 positivity is real mathematical progress, not closure.
