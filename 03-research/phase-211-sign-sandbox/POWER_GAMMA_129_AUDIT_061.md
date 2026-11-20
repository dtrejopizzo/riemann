# POWER_GAMMA_129_AUDIT_061

Status: **APPROVED** POWER_GAMMA_129_DECISION_061 and its complete certificate, after a final reading of the six sections. Papers untouched.

The only object is the historical atom N=129,k=0,u=63/2, not a campaign of orders. The antecedents025/026 left ERR<−.66 without deciding W;032 decides another atom,211,k1, and035 another endpoint,17,k0. The new certificate keeps all pieces of the SAME form and decides the pending sign.

## Reproduction and normalization

Read in full tools/power_gamma_129_decision_061_verify.py. Independent reproduction with python3, exit0: **PASS** and the same printed rational endpoints. The norm of g=y^128 exp(−uy)/128! is comb(256,128)/63^257. The a_r=p_r r! satisfy exactly the recurrence of the normalized autocorrelationrho(0)=1; the Horner divided by r+1 reconstructs sum a_r t^r/r!, with no lost factorial.

ARCH uses the stable A0 of032, with HurwitzEM8/CUT32 and absolute periodic remainder. The exact coefficients multiply the endpoints before creating rounded intervals. Gamma and logpi keep the already audited sources003. The final width ARCH<10^−18 is checked. The polar2/(u²−1/4)^129 divided by the norm is an exact rational. All primes and their powers up to512 are enumerated without duplicating weights; each atom uses2logp·m^−32P(logm), with the root of m cancelled exactly.

## Full adverse tail

Positivity of the coefficients of rho makes all contacts of k=0 adverse. ROOT026 gives q(t)>sqrt((128/t)²+u²)−128/t. At t=6 this lower bound exceeds16 becauseu²>256+4096/6. Since log512>6 and q′>0, the whole tail has q>16 and rho(t)<=rho(log512) exp(−16(t−log512)).

The sum-integral comparison for ALL integers m>=513 starts at512, without omitting the first term of that tail. It gives

    tail <=2rho(log512)sqrt512[2log512/31+4/961]
          =2·512·[P(log512)/512^32]·[2log512/31+4/961].

This is exactly TAIL of the program; the roots cancel before rounding. The adverse sign is subtracted at the lower endpoint of W and not added to the upper one. The prefix is not presumed to be the full sum.

The output of W is formed by EXACT floor/ceiling of the Fraction endpoints, not by floating printing:

    W/||g||² ∈[13456684165,13456684168]/10^20.

Hence the atom is strictly positive. The auxiliary float decimals of the tail are not used as a source of proof.

## Sharp compensation and cells

The exact resolvent is2sum_(r=0)^128 a_r/32^(r+1), corresponding to E[1/(tau²+1/4)]. ARCHsharp=ARCH+resolvent and ERR=ARCHsharp−W. The program preserves the dependencies via the independent formula ERR=PRIME_total−POLAR+resolvent. Certified:

    ARCHsharp/||g||² ∈[−104219397018062543067,−104219397018062543064]/10^20,
    ERR ∈[−104219397031519227232,−104219397031519227231]/10^20.

The normalization of ERR is that of rho(0)=1 used in024/025. The old benefit .66 is not added as if it were another term. Using .33<S129(2)<1/3 already certified024, the joint benefit of ALL cells n>=3 is−ERR−2S129(2), between.3755 and.3822. The signs and the subtraction of the first cell are correct.

The final source states the tail only as<10^−24, exactly the bound checked by Fraction; the tighter decimal is explicitly marked approximate. This separation is correct and requires neither changing nor rerunning the verifier. The narrow printed intervals of W/ARCHsharp/ERR use exact rational floor and ceiling and are indeed certified enclosures. The attribution of the case is documentary: the round takes up a historical obligation; the choice of N is not new.

The result decides that atom and quantifies its real compensation. It does not decide a whole row, general blocks, arbitrary order nor a new time window.
