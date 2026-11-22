# Recorded state — eight poles and signed transport

Status: PROVED eight arbitrary poles and strong confluent bridge; global sign OPEN. Goal active. No paper modified.

## New reviewed result

POWER_SIGNED_TRANSFER_014, reviewed in POWER_SIGNED_AUDIT_014 and reproduced with tools/power_signed_transfer_014_verify.py, proves

    W[f] > ||f||²/1000

for every nonzero real f with Laplace transform P(s)/Π_(j=1)^8(s+v_j), deg P<8, v_j>=63/2. Repetitions and cancellations are allowed; there is no minimal separation or upper bound. It includes every mixture of up to eight exterior powers with exponents>=32.

## Insight that overcomes the limit013

The filter defect keeps the positive gain: (R−R0)|F0|² decomposes EXACTLY into a positive sum of |G_j|². Each G_j has nine poles and a numerator zero at s=0. The archimedean pole movement applies on that same subspace of numerators; a restricted confluent coercivity>1/4 certifies the sign of the whole correction.

Base AP8>7/200, polar norm<3/2, transport margin and full control of the comb by weighted trace produce the result. 013 is not contradicted: the spectral distribution and the gain that that method discarded are kept. No general AP monotonicity is claimed.

## Exact bridge to the full task

POWER_CONFLUENT_BRIDGE_014 was independently reviewed by cases. For any fixed rate u>1/2, ALL blocks span{y^k e^-uy:0<=k<N} are dense in a weighted H1 norm that controls the whole form. The density proof uses the Laplace transform of an orthogonal H1 vector, includes the boundary term and does not presuppose sufficient L² density.

Therefore it suffices to prove W>=0 on each confluent block of ONE rate, for example31.5. A positive constant uniform in N is NOT needed. Nonnegativity of all blocks and strong continuity suffice to pass to the limit and transfer compact tests to any window.

This has not been achieved: the fixed block of dimension twelve has a separate certificate, but all subsequent sizes are not proved. Finite certificates, even universal in their rates, do not replace that requirement.

## Available full identity and remaining obligation

PRIME_TRANSFER_014 contains the one-pole identity, audited in POWER_PRIME_AUDIT_014:

    W[f_v]−R0 W[f_u]=(1−R0)W[G], G(s)=sF_u(s)/(s+v).

It includes the polar and ALL contacts; the generator is not declared positive without proving W[G]. The multipole version is integrated into SIGNED_TRANSFER. Closing all orders will require controlling these corrections with the full form, not only repeating identities.

A geometric expansion and the behaviour of iterations that add zeros at s=0 are under construction in round015. They are not included here as verified theorems, and no sign is deduced for a mixture whose components are not yet controlled.

## Goal audit

Three case: resolved and extended up to eight. Bridge in form norm: resolved, now for a single confluent rate. Extension to ALL orders: open. Closure of the sign of Paper46: open. Goal neither completed nor blocked; authorised mathematical work remains.
