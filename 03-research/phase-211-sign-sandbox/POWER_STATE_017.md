# State017 — sufficient scalar bridge and joint positivity

Status: partial results PROVED with independent review; global sign OPEN. Goal active. Papers untouched. Replaces STATE016 as the current summary.

## What is now needed to close the sign

POWER_SCALAR_BRIDGE_017 shows that it suffices to prove W[h_(N,k)]>=0 for ALL integers N>=1,k>=0, with H_(N,k)=s^k/(s+u)^(N+k) and a fixed rate u=63/2. This scalar table controls all cross terms of the full blocks: the density of any numerator is a base weight times a polynomial R(q)>=0 on[0,1]. R+epsilon has an exact Bernstein expansion of high degree with positive coefficients. The rational identity of densities keeps the polar on evaluating x=-1/4, in addition to each contact and its full sum. Letting epsilon go to0 proves sufficiency. The strong bridge014 then connects to the data of Paper46.

Positivity of a linear envelope is not inferred from a union of tests. The representation is conic in densities and includes all cross terms. The degree elevation is elementary and effective; the degree may grow as epsilon decreases. Proof reviewed independently twice.

## Regions of the table already controlled

POWER_INTERIOR_017: for N=1, ALL k>=0 and ALL u>=63/2, W>4norm²/3. No unknown initial threshold remains in this row. New uniform control by binomial coefficients of the weighted norm, archimedean-only monotonicity, full polar and infinite comb bounded. Rational verifier reproduced PASS. Its §7 gives an effective bound for each row N, uniform in all k, without claiming the sign of all rows.

POWER_QUADRATIC_017: for each c>0, W>0 for P1 at ALL k>=cN² when N>=N0(c), with N0 explicitly boundable. The tool shifts the full rational DENSITY to Imz=1 and proves a uniform L1 bound. It yields |correlation(t)|<=C(c)e^(-|t|) and controls the WHOLE comb. It avoids the separation of temporal weights falsified in016. It also proves an approximation of the full comb by an absolutely convergent modulated Gaussian series; it does not presuppose the sign of that series. Reviewed independently twice; consolidated audit in POWER_INTERIOR_AUDIT_017.

POWER_QUADRATIC_EXPLICIT_017 proves W>49norm²/50 for ALL N>=2,k>=10000N², at rate31.5, by shifting the density by15. The autocorrelation is bounded by5e^(-15|t|), so comb and polar each cost less than1/1000 and ARCH>99/100. The full proof was reviewed and the rational verifier reproduced PASS. Two independent reviews also approved the extension: POWER_INTERIOR_AUDIT_017 §9 and POWER_QUADRATIC_EXPLICIT_AUDIT_017. It is an explicit cone without unknown dimensional threshold.

## Earlier results still valid

Eight arbitrary poles>=31.5: W>norm²/1000. Fixed block of dimension12: separate certificate. All blocks of one rate suffice by strong continuity, without uniform margin. Tail theorem015 for each fixed dimension valid. The obstructions016 to tail density and to making temporal weights uniform remain: the new argument keeps the product of factors of the density before taking the absolute value.

## Limit and remaining obligation

The full table is still NOT proved. Its lower regions and the arithmetic interactions in the regime where both indices grow without entering the controlled positive cone are missing. An infinite row or a cone do not replace the whole table. There is no counterexample to W.

None of these results by itself certifies a new window T>log(5)/2: they are theorems on families of tests. Global sufficiency appears only if the scalar table is completed or another argument covering all data is found. Do not confuse exponents, indices or dimension with the width T.
