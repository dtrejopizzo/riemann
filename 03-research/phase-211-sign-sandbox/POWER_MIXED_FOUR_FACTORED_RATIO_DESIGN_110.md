# POWER — Factored theta quotient, design110

## Verified update: reproduction finished and WM activated

The run log and the independent reproduction log of110 are byte-for-byte identical, SHA256 `90a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539`. Driver: `c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108`; the four imported modules keep the audited hashes. Exact fractions confirmed the complete origin (16 leaves in lambda[0,1/4]) and 4198 contiguous REST leaves from1/2 to845/32 in BOTH logs. Both programs ended INCONCLUSIVE after8192 evaluations; that label is not changed and no FULLPASS up to64 is claimed.

The analytic tail104, audited independently, proves Wmixed/Phi^4>6t^2/y^2 for all t>=16. Hence the reproduced coverage and that tail overlap and prove WM for ALL t>0. The three prefixes103 complete MIXED4. The real application of the audited implications112 is activated: second density Xi positive for all p,q>0, E/Psi decreasing, strict TP2 and confluence. The literal§8 and the two strengths verified independently by cases were also reviewed: the comparisons of the limiting star pair are activated. It is not claimed that Xi_(p,q)/E_(p,q) is decreasing for finite parameters, five arbitrary powers, all orders, nor a new window.

Later mentions of a pending replica or conditional application describe the status before this update and are superseded exclusively by this evidence. The global sign remains OPEN. See `POWER_REASSESSMENT.md` for the change of strategy.


Status: DESIGN AND LITERAL AUDITED; run52878 ended exit2/INCONCLUSIVE; reproduction12244 in progress, without independent closure yet.109 ended exit2 without FULLPASS, so the precondition is met. PASS is not guaranteed.

## 1. Precise difference

The consultation of the project rules and the three indices for the mixed object104–109 is kept. The remaining branch of107 evaluates the quotient Theta16(y+v)/Theta16(y) with separate numerator and denominator.110 uses an exact identity to preserve the dependence on the common first mode. It does not change the integrated function, the hypotheses, the target or the budget; it is neither a new sign proof nor a modification of109 during its run.

## 2. Exact identity and factors

Define d=2y-3 and, for m=2..16, a_m=m^2-1,

 B_m(y)=m^4+3m^2 a_m/d,
 R16(y)=sum B_m(y)exp(-a_m y).

Then Theta16(y)=d(1+R16(y)). The factor m^4 is essential: (2m^2 y-3)/(2y-3)=m^2+3(m^2-1)/(2y-3), and there is in addition the outer factor m^2. Hence

 Theta16(y+v)/Theta16(y)
 =(1+2v/d)*(1+R16(y+v))/(1+R16(y)).

This identity is used INSIDE the same integrand A16 of106/107. It is not assumed that the errors of the two corrections are correlated: their balls are propagated normally. The preservation is algebraic in the explicit main factor1+2v/d.

The total time derivative, with y'=2y, is

 R_t(y)=-sum exp(-a_m y)[2y a_m B_m(y)+12y m^2 a_m/d^2].

Thus the same local column p16 can be evaluated as

 p16=2y-9/2-6/d-R_t/(1+R16).

Do not confuse R_t with R_y. The jets of p16 are obtained with the same precision/cap and known coefficients of107. The formula does not differentiate an asymptotic equivalent nor discard modes.

## 3. Budget, domain and errors kept

The Cauchy-clip origin109 stays INTACT. In the remainder, precision512,cap4 for integrals/cap5 local,16 modes, Gauss64 on the same10 v segments up to512, initial partition508 time cells of width1/8, depth10 and at most8192 evaluations are kept. The traversal order and the sign/inconclusive criterion are kept. Enclosed nodes and weights, log/power branches and denominator checks are maintained.

The analytic errors of106 apply unchanged because the functions are identical: Gauss2^(-83+5j), total column payment2^-81*32^j and X/Yc error2^-687*32^j for j0..3, besides interval rounding. Tails are not shortened and parameters are not chosen according to the output of109. The factorization does not extend the domain of holomorphy: d and1+R16 are nonzero on the domains already proved in106. exp(-a_m y) and exp(-a_m v) can be reused for the shifted correction.

## 4. Execution condition and scope

Wait for the final output of109 without intervening in its process. If it is FULLPASS,110 is not executed. If not, the new representation first requires audit of the present design and literal; only afterwards may a run be authorized. A later enclosure failure remains INCONCLUSIVE, not a mathematical negative. This design adds no W coverage and does not claim that the factorization suffices to finish within budget.

## 5. Status after review, without anticipating the result

109 ended exit2 because of the REST budget, not FULLPASS. Design and literal110 were approved independently before data; the first coordinated run was authorized. No replica was executed at that point and no PASS is anticipated. Codes107/108/109/110 unmodified during the run. The final result and driver hash will be recorded only after the actual output.

## 6. Terminal result of the run and reproduction in progress

Run52878 ended exit2/INCONCLUSIVE because of the budget of8192 REST evaluations,4198 accepted leaves. Origin PASS16/16. Exact Fraction log audit: the4198 leaves are contiguous REST[1/2,845/32], length829/32. The next pending cell[845/32,3381/128],depth4, was not accepted before the cap. NO FULLPASS of the program with target up to64. Log:`tools/power_mixed_four_factored_110_root.log`, driver hash c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108.

The independent reproduction12244 continues with the SAME program, target64 and budget8192, without stopping at16 nor other adjustment. The run covers16, and104 proves the tail from16, but the global WM application112 remains CONDITIONAL until independent coverage to16 is confirmed. That possible assembly is not confused with FULLPASS of the program, and the final result of the replica is not anticipated.
