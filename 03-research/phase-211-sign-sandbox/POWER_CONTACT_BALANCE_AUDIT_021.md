# POWER CONTACT BALANCE AUDIT 021

Status: APPROVED with explicit separation between exact proofs and numerical diagnostic. Papers untouched.

Read `POWER_CONTACT_BALANCE_021.md` and `tools/power_contact_balance_021_verify.py`. The proof was reviewed independently and the exact verifier was run with result PASS. The quadrature was not repeated, since it adds no error certification.

## 1. Exact FAIL234

The same atom N211,k1,u63/2 and normalization020 are kept. For q=p^a, the expression 2log(p)q^−32 K_Nr_N(u log q) contains the correct von Mangoldt factor; at q4 log2 is used. The Fraction Horner evaluation does not round intermediate coefficients. The beta norm and the exact polar coincide with020. The three inequalities ARCH<−.74, POLAR<−.36 and 0<P2+P3+P4<.89 give strictly ARCH+POLAR+P2+P3+P4<−.21. This result concerns that real partial form, not W.

## 2. Exact complete tail

The substitution Λ(q)≤log q and the use of absolute coefficients of r_N produce a valid majorant over all integers q>300, which includes all real prime powers. For f_l(x)=x^−32(log x)^l, l≥1, unimodality gives sum≤integral+supremum. Moreover (log f_l)′≥−32/300 on the whole half-line. From any maximum point x0≥300, f_l(x0+t)≥f_l(x0)exp(−32t/300), so supremum≤(32/300)integral. The total factor 83/75 is correct even when the maximum is at the endpoint300.

The recurrence by parts I_l=300^−31(log300)^l/31+(l/31)I_(l−1), with I0=1/(31·300^31), has only positive summands. Substituting a rational upper endpoint of log300 and multiplying by 2K_N explains the factor166/75 of the script. 0<Σ_(q>300)P_q<5·10^−13 is approved. Strict positivity comes from019; the upper bound does not use a favorable sign of polynomial coefficients.

## 3. Diagnostic and scope

The beta density used in the quadrature is normalized: (2/B(3/2,N−1/2))t²(1+t²)^−N−1 dt on t>0, with τ=ut. The agreement of the45/65-digit computations is a NUMERICAL diagnostic, not a rigorous interval for ARCH. Hence neither the numerical partial sum near −6.08·10^−14 nor its combination with TAIL proves the sign of W. It is not certified that W is negative, zero or positive.

The local novelty with respect to020 consists of FAIL234 and the analytic bound of the whole tail, for a single atom. It is not a new route by renaming the arithmetic sum, not a general NO-GO for finite combs and does not certify a new row or window T. The complete cancellation remains pending.
