# State032 — Rigorous decision of the candidate211,1

Status: result PROVED and audited. Replaces STATE031 as the current summary. Goal active; global sign OPEN; papers untouched.

## Single pending atom decided

POWER_CONTACT_DECISION_032 proves for F(s)=s/(s+63/2)^212, N211,k1,u31.5:

    3.4·10^-15 < W[f]/||f||² < 4.5·10^-15.

ARCH, polar, all prime powers up to512 and the WHOLE remaining tail are included. The candidate is not a counterexample. Nothing is extrapolated to neighbouring N, to a row, to variable u or to a window T.

CONTACT_BALANCE021 had left a partial sum up to300 of approximately−6.08·10^-14, with a favourable tail even larger than that scale in its upper bound. It never certified W negative. The sign change032 comes from incorporating omitted contacts; it is not attributed to an error of the earlier quadrature. The new formula also removes the analytic uncertainty of that quadrature.

## Exact method and evidence

POWER_ARCH_EXACT_032 proves stable formulas for ARCH_N0 and ARCH_N1, with positive coefficients and positive Hurwitz brackets. For the concrete atom it uses16 summands per series, eight Bernoulli numbers and an absolute integral remainder, not the next-term hypothesis. The final ARCH interval has width<10^-18.

The contacts are evaluated through a polynomial in logq and the EXACT factor q^-32. All prime powers up to a single cutoff512 are enumerated by integer divisions. Horner with divided powers and outer rational arithmetic gives width of the finite comb<10^-40. The polar is an exact fraction. The tail is positive by019 and has a rational majorant<1.1·10^-15 via integrals of logarithmic monomials.

POWER_CONTACT_AUDIT_032 approves all normalisations, formulas and remainders. Both proofs were read and the modules and main certificate reproduced: PASS. A preliminary rounding failure of the reciprocal q^-32 was corrected by dividing the rational endpoints before creating the interval; only the corrected code was accepted and audited.

## Coverage and remaining obligation

To the earlier coverage this positive pointwise atom N211,k1,u31.5 is added. Rows N1..5 for all k, the cone k>=10000N² at that rate, eight arbitrary poles and fixed block12 remain. The regions029 of increasing rates keep their separate scope. The sign of all N,k and a new window T are not proved.

The global budget031 with signed arithmetic primitive remains valid and open on its complement. The decision032 shows that a cancellation of components of order1 can leave a positive margin of order10^-15: coarse bounds must not be confused with the sign of the real balance. Nor does a pointwise decision replace a uniform inequality.

The continuation needs to extract from the exact formulas a structural compensation of all contacts or resolve the signed average031; not launch a campaign of more points.
