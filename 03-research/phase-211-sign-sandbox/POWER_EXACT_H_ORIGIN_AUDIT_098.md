# POWER_EXACT_H_ORIGIN_AUDIT_098 — Independent audit

Status: **APPROVED**, run19778 exit0/FULL PASS128panels and POSITIVE sign. Independent reproduction run57072 exit0/FULL PASS128, with positive H3/Th0 and matching hash. Final source `POWER_EXACT_H_ORIGIN_DESIGN_098.md` read in full; design and literal code approved BEFORE the run. Hash checked locally:

    bebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9

Papers untouched; a single predeclared sign test, no campaigns.

## Exact datum and regularization

The formula097 T_h0=12aH3/b⁴ was independently reproduced by formal expansion. a>0 is a variance; b<0 comes from086R'0>0 andR=1/N, not merely fromM''<0 in theinterior. B0=(a−N)/x hasvalue−b>0 and gives h=N/B0 analytic at0. Hence the signH3 is exactly the signT_h0, not a stronger density condition as093.

The six even momentsI0..I10 give the seriesZ/Z0 withcoefficients m2k/(2k)!, since the bilateral normalization2cancels. m0=1exact. The series is declared withprec11 (onlyknowndegrees0..10); logZprec11 andMderivativeprec10 keep exactly thecoefficients1,3,5,7,9 ofN=a+bx+cx²+dx³+ex4. Unknown coefficients are not filled in, moment12 is not required and normalized cumulants are not confused with positive moments.

## Moments, remainders and literal text

093 is kept:128panels[0,2],degree64/cap65/512bits,16modeswithCOMPLETEtailEPS. For even orders up to10, |t^rPhi|<3^10·2^22<1e12 on thecomplex region. The TOTAL integrationremainder2e12·4^-65/(1−1/4)<1e−24 is added symmetrically. The coefficient tailsEPS32^k are incorporated intoPhi0..64 BEFORE multiplying byt^r.

The new temporal tail is adapted to order10: (2+s)^r<=1024exp5s, togetherPhi2+s<2^-140exp−300s, gives(1024/295)2^-140<2^-138. Adding[0,2^-138] toEACH moment is safe; reusing2^-140from093 would have been insufficient, and the code does NOT do so.

The literal code imports no previous runs. It verifies precision/finiteness/positivity of moments and series, a>0,b<0. It evaluatesH3=ace−ad²−b²e+2bcd−c³ and acceptsBOTH strict signs. Th0 divides by non-zerob⁴; there is no assert forcing positive nor later tuning of parameters. The source keeps the previous design and documents the SINGLE run19778 withimmutable hash.

## Result and scope

H3 is enclosed in a strictly positive ball (centre approx1.73824840842e−21) andTh0 in another positive one (approx3.15512974175e−5). The decimals are a reading; the proof is the rigorous interval assert that propagates all errors. The run ended exit0/FULL PASS128. Run57072 independently reproduced exit0/FULL PASS128 with the same positive balls and matching hash.

One obtains **T_h(0)>0 for the real Phi** and, byanalyticity, positivity on an existing neighbourhood withoutradius. The origin is auxiliary, not an admissible Wexponent. Together with097 there is positivity on a neighbourhood of the origin and on the whole tail u>=512, not a complete splice: the intermediate interval remainsOPEN. No globalT_h,triplesGp,five/allgenerators,newW/T or global objective resolved. Consultation073/077/087–097 and records distinguish this EXACT jet from the stronger particular one093.
