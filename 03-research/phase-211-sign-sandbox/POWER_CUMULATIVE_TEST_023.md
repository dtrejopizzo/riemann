# POWER_CUMULATIVE_TEST_023 — Targeted test of the relaxed criterion K=J+xh

Status: PROVED a negative value of the COMPLETE relaxed criterion, executed rational certificate. Independent review approved in POWER_CUMULATIVE_AUDIT_023.md; verifier reproduced PASS. A single N=129,x=1, no campaign. Papers untouched.

## Corpus and new reason before building

Read the project rules, INVERSE_KERNEL020, INVERSE_INTERIOR022 and audit; targeted search in the ROUTES-TRIED-INDEX index, grid part 3 and CROSSWORD-TO-D (cumulative/relaxed kernel/Möbius inverse). Positivity of the full h was already refuted022. The new criterion proposed by `signo` uses K_N=J_N+xh_N, with h_N=−J_N': K>=0 forces J_N/x to be decreasing and allows a cumulative argument weaker than requiring h>=0. Hence the counterexample022 does not decide it.

ONLY the neighbour N=129,x=1 is chosen, suggested by the small positive margin of K_128(1). The certificate will keep the complete infinite tail, not the sign of a prefix. No sign of K will be automatically attributed to the sign of W.

## 1. Result

For u=63/2, N=129, we prove

    −1/250 <K_129(1)<−1/251<0.                           (NEG)

Thus the lemma K_N(x)>=0 for all N>=2,x>=1 is false, even keeping the COMPLETE Möbius inverse. It is not claimed that J_129 is negative, nor that the mean ERR or the form W have negative sign. Only that sufficient criterion has been refuted.

## 2. Normalizations and correct polynomial

With rho_N(t)=e^-ut P_N(t), P_N=Σp_jt^j from020, define

    J_N(x)=Σ(m>=1)mu(m)(mx)^-1/2 rho_N(log(mx))
          =x^-32 Σ(m>=1)mu(m)m^-32 P_N(logx+logm),
    h_N(x)=−J_N'(x)=x^-33 Σ(m>=1)mu(m)m^-32 A_N(logx+logm),
    A_N=32P_N−P_N'.

The differentiation goes through the absolutely convergent series at fixed N. Therefore

    K_N(x)=J_N(x)+xh_N(x)
          =x^-32 Σ(m>=1)mu(m)m^-32 [P_N+A_N](logx+logm).

At x=1 no additional factor of x or m remains. The relevant polynomial is P_N+A_N, not A_N alone. Its129 coefficients are positive rationals and its degree is128.

If one had K_N>=0 on the whole half-line, (J_N/x)'=−K_N/x²<=0 and J_N/x->0 at infinity would force J_N>=0. The proof NEG shows that this global premise does not hold for the complete family; it does not prevent other cumulative inequalities from deciding the pairing.

## 3. Finite certificate and infinite tail

The verifier `tools/power_cumulative_test_023_verify.py` reconstructs P_129 and A_129 by the rational recurrences of020/022, computes mu(m) by integer factorization for1<=m<=64, encloses logm by atanh series with geometric remainder and evaluates P+A with interval Horner and outward rounding. It uses no floating-point special functions.

For each0<=j<=128,

    log64=6log2>4>=j/32,

so that x^-32(logx)^j decreases on x>=64. With L=21/5>log64 and

    I_0=64^-31/31,
    I_j=64^-31 L^j/31+(j/31)I_(j−1),

one obtains a rational bound of the COMPLETE TAIL:

    |Σ(m>=65)mu(m)m^-32[P_129+A_129](logm)|
       <=Σ(j=0..128)(p_j+a_j)I_j<10^-10.

The interval of the segment m<=64 plus that symmetric error satisfies exactly the endpoints of NEG. The executed verifier gives PASS. The approximate value−.003985845090 is given only for orientation, not as input to the proof.

## 4. Scope

There was no search over other N nor a table of points. The result refutes the criterion K>=0, weaker than positivity of h, which was not decided by022. At the same time it keeps the need to control the signed pairing or a different cumulative inequality: K negative at one point does not determine the sign of J, ERR, W, nor of any other sign object.
