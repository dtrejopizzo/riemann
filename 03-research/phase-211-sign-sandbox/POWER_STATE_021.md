# State021 — Bounded diagnosis of the balance of one atom

Status: two exact partial bounds PROVED; the cancellation diagnosis NUMERICAL; global sign OPEN. Goal active. Papers untouched. Complements and replaces STATE020 as the current summary; all its results remain valid.

## Coverage of the full form

No extension in this round: full rows N1,2,3, cone k>=10000N², eight arbitrary poles and fixed block12. The scalar bridge017 requires completing ALL N,k. No new window T certified.

## Exact result and numerical scope kept separate

POWER_CONTACT_BALANCE_021 keeps a single atom, N211,k1,u31.5. PROVED: ARCH+POLAR+contacts2,3,4<−.21norm². PROVED: the FULL sum of contacts q>300 lies between0 and5e−13 times the norm². The tail proof uses absolute coefficients, unimodality, a bound on the logarithmic derivative and an exact recurrence of integrals; it does not enumerate additional contacts. The proof was read and the Fraction verifier reproduced PASS. The independent review was approved in POWER_CONTACT_BALANCE_AUDIT_021.

NUMERICAL only: quadrature at45 and65 digits and contacts<=300 give a partial sum around−6.0812e−14norm². Agreement of precisions does NOT certify quadrature error. The rational bound of the tail does NOT turn that diagnosis into a rigorous interval for W. W is not claimed positive, negative or zero.

The diagnosis shows very fine cancellation between terms of order1; the coarse separate bounds used here do not decide the sign. This is not a global NO-GO on certificates, finite combs or signed inequalities. The enumeration was stopped at300 so as not to turn the diagnosis into a precision campaign.

## Arithmetic tool from020 still valid

POWER_INVERSE_KERNEL_020, reviewed in POWER_BALANCE_AUDIT_020, controls the FULL Möbius inverse: H_N/4<=h_N<=7H_N/4 if logx>=(N−1)/30, for all N>=2. For N2, h_N positive on the whole half-line. The possible adverse part lies in an explicit interval; its pairing with B remains open.

## Next work

Look for an inequality that keeps the cancellations between ARCH, polar and the comb, or control the interior pairing of the full inverse. Do not extrapolate a numerical partial sum to the sign of W, nor return to a repair by the first contact alone, already refuted. The objective remains active and is neither completed nor blocked.
