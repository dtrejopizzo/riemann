# POWER — Correlated polynomial determinant, design108

Status: EXECUTED / INCONCLUSIVE, independently reproduced. The previous design is kept; compact sign OPEN.

## 1. Antecedent and precise difference

The project rules and the consultation of ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID and CROSSWORD-TO-D for the mixed object104–107 are kept. Run107 and its independent reproduction ended INCONCLUSIVE:11 evaluations,0 accepted, lambda[0,1/65536], depth10. It was not a negative sign. The odd system093 is not repeated as proof and inheritance from099 is not presumed.

The only change of108 is algebraic: form the determinant in the ring of interval polynomials BEFORE evaluating lambda. Thus the24 permutations keep the same variable; no correlation between coefficient errors is assumed. The107 builder and all its truncation proof are kept intact.

## 2. Unchanged parameters

Origin:1024bits,128 modes, cap t1025, lambda degree512; domain[0,1/4],16 initial cells of width1/64, depth10, at most8192 evaluations. Remainder: module107 INTACT,512bits, Gauss64 on10 segments up to512, cap4/cap5,508 initial time cells of width1/8, depth10, at most8192 evaluations. No change of modes, precision, geometry or acceptance criterion.

power_mixed_four_origin_branch_107.py and power_mixed_four_compact_107_verify.py are not modified. The new controller imports the builder without executing run_origin107. Before import, hashes fixed when saving the literal108 are checked. The import of107 does not evaluate theta. The pointwise evaluation of a and construction of coefficients will occur only in the authorized run108, never during this design.

## 3. Polynomial and errors

The builder delivers the known polynomials for columns K,J,phi,Q and their lambda derivatives0..3. Form, by interval products and sums, the24 terms of the determinant and obtain a single polynomial P(lambda), keeping all its coefficients. Its degree is finite and at most2048. Do not truncate the product to reduce cost and do not identify uncertain coefficients with zero.

The errors of moments103, a and theta modes are ALREADY in the interval coefficients of the builder and propagate through all products. The remaining function error per entry is epsilon=2^-400, according to the audited107. That ball is not introduced as a constant coefficient of P: it is paid afterwards as an independent error of the determinant.

For real lambda[0,1/4], the discs of radius1/8 lie in |lambda|<=3/8. J,K<=2^42 on |lambda|<=1/2; Cauchy up to derivative4 costs less than4!8^4<2^17. The combination Q^(j)=-(2j+1)phi^(j)-2lambda phi^(j+1), j<=3, likewise stays under B=2^62. The polynomial entries are under B+1. Telescoping each product of four entries, without assuming favourable dependence of errors, gives

 |exact det-P| <=24*4*epsilon*(B+1)^3
                 =96*2^-400*(2^62+1)^3 <2^-200.

This bound is uniform on the whole origin. It does not require prior positivity of the determinant.

## 4. Evaluation fixed before data

Exact Taylor shift of the polynomial to each rational centre c is chosen, and NOT direct interval evaluation of its24 terms. If

 P(c+s)=sum b_j s^j,

compute the lower bound b_0.lower - sum_(j>=1) abs(b_j).upper*h^j -2^-200, with h the exact half-width. For an upper bound use b_0.upper + the same loss +2^-200. All shift coefficients are outward balls, the centre and h are exact dyadic rationals. Small coefficients are not discarded. The finite sum incorporates ALL kept degrees.

A cell is accepted only if the lower bound is positive. A negative upper bound gives NEGATIVE for that whole cell; otherwise subdivide left first with the same budgets of107. If they are exhausted, INCONCLUSIVE. An origin output other than PASS prevents executing the remainder. If it passes, certify_rest107 is used without altering its parameters. An inconclusive enclosure is not reinterpreted as a refutation.

## 5. Audit and pending tasks

The entry bounds and the transfer2^-200 were reviewed conceptually before data. Pending: complete audit of this design, literal108 with hashes of the modules107 and verification of the polynomial shift API, literal audit and only afterwards a run. The product/shift of degree up to2048 may be costly; the mathematical budget does not imply a guarantee of viability or PASS.

There is no new theta evaluation, sign result, W coverage nor global transfer in this document. The proposed gain is to preserve the common variable when evaluating; the interval coefficient errors remain independent except for the explicit exact algebraic identities.

## 6. Fixed run and reproduction

Run82660 and independent reproduction28564 ended exit2/INCONCLUSIVE. Polynomial degree2042;15 evaluations,4 accepted leaves, coverage lambda[0,141/8192]. Stop by depth10 at[141/8192,1129/65536], printed determinant[+/−2.04e−4]. REST was NOT executed. Scripts and budgets were not changed.

Driver hash108:`eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a`. Modules107 verified intact: origin15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553; REST2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054. Logs:`tools/power_mixed_four_polynomial_108_root.log` and`tools/power_mixed_four_polynomial_108_audit.log`.

The reproduction added exclusively a profile of the values ALREADY computed at the return of evaluate, with no new theta evaluations, centres, coefficients or parameters. In the final cell, the shifted coefficient0 already has ball[+/−1.79e−4]; additional radius due to cell variation approximately2.4560159427e−5. This distinguishes uncertainty of the central coefficient from the added variation, without identifying a single cause of the width nor claiming that a real zero exists. The decimal readings describe the log; they are not a sign certificate.

Result INCONCLUSIVE: no opposite sign, falsifier, mathematical obstruction, global Chebyshev4, finite U nor new W/T/allorders coverage. A later representation will require design and audit before another run; this one is not readjusted to force PASS.
