# POWER_STATE_053 — Full transport to thirteen poles

Status: PROVED for the declared family; general sign OPEN. Papers untouched.

For every nonzero real polynomial P of degree less than13 and any real rates v_i>=63/2, repetitions included,

    W[P/prod_i(s+v_i)] > ||P/prod_i(s+v_i)||²/4000.

Reference: POWER_FULL_THIRTEEN_053.md. Auxiliary result: fourteen poles with numerator D of degree<14 and D(0)=0 have W>norm²/1000. It is a zero of the transform at s=0, not a temporal value at the origin.

## Evidence and mechanism

CENTERED_MOMENT_053 and its audit prove E23[Q^j F]>norm²/10 for all F in V13 and j>=96 through a single exact moment and monotonicity by covariance. The remaining segment j=1,...,95 satisfies E23>norm²/500: 95 rational LDL certificates, with outer errors and operator error paid against the Gram matrix. The full verifier was reproduced three times independently with exit0 and all PASS. The moment verifier was also reproduced.

MULTI015 transfers the full orbit to fourteen poles with zero numerator. The full arithmetic tail from4 has norm<1/1000 by the trace B_T14=947334302964. FULLTEL014 keeps form, norm, polar and arithmetic and transfers the margin of the confluent block13 of052 to all thirteen poles.

The initial run was slow because of giant denominators in exact logarithms. Its evaluation was replaced by outer rational intervals at each operation, keeping 512 terms, precision260, margins and cutoff; no condition of the certificate was relaxed.

## Pending scope

It does not prove arbitrary dimension nor fourteen poles with general numerator. It does not establish a new window T. The global sign remains open. The next work must look for uniform control of the initial segment as the dimension varies, not confuse eventual positivity with positivity of the whole orbit.
