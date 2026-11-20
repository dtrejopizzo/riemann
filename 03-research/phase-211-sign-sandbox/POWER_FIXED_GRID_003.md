# POWER_FIXED_GRID_003 — Fixed ladder, complete elimination and six certified cases

Status: PROVED (elimination identity, orders 1–6 and algebraic falsifier). OPEN (uniform control of all orders). Papers untouched.

## 1. Antecedents and new reason

Consulted ROUTES-TRIED-INDEX/README.md:393,655 and entries of rounds 001–002; NODE_001:195; grid part3:12, part5:7 and MASTER_GRID, recent entries; CROSSWORD-TO-D, recent entries; POWER_BRIDGE_002, POWER_CONE_001 and POWER_THREE_002. Schur/Pick elimination is known, it is not sold as a new object. The difference with respect to the high range of round 002 is the FIXED ladder a_j=32+j, which has the dense bridge proved in independent review. An exact transformation of the complete datum (not separated into Gamma, prime, polar) is computed and its first six steps are certified by rational arithmetic with explicit remainders.

## 2. Exact elimination keeping all cancellations

Let s_j=63/2+j, L_j=L(32+j), K_ij=(L_i+L_j)/(s_i+s_j). Put

    x_j=j/(63+j), q_j=(L_j-L_0)/(L_j+L_0).

Then K is congruent by a strictly positive diagonal to

    B_ij=(1-q_i q_j)/(1-x_i x_j).

Indeed K_ij=w_i w_j B_ij, where

    w_i=(L_i+L_0)(1-x_i)/(2 sqrt(L_0 s_0)).

No component of the datum is eliminated separately: L includes the three pieces and their exact cancellations. The crossed polar identity of POWER_THREE_002 §1 remains applied.

For r=0,1,..., define alpha_r=q_r^(r), with q_j^(0)=q_j. If |alpha_r|<1 and the denominators 1-alpha_r q_j^(r) are non-zero,

    q_j^(r+1) = [(q_j^(r)-alpha_r)/(1-alpha_r q_j^(r))]
                 /[(x_j-x_r)/(1-x_j x_r)],  j>r.             (E)

Each elimination step, when defined, is an invertible real diagonal congruence of the remaining matrix with (1-q_i^(r+1)q_j^(r+1))/(1-x_i x_j). Proof: apply the fractional transformations Q=(q-alpha)/(1-alpha q), X=(x-x_r)/(1-x_r x); both send the pivot to zero. The new kernel is congruent to the previous one; on subtracting the row/column of the pivot 1, its complement is

    X_i X_j [1-(Q_i/X_i)(Q_j/X_j)]/(1-X_i X_j).

The transformation of the denominator to the original x only introduces positive diagonal factors. The factors coming from 1-alpha_r q_j^(r) may have arbitrary sign outside the positive regime; it suffices that they be non-zero to keep inertia by congruence. If the matrix is positive definite, its diagonals imply |q_j^(r)|<1, so those factors are automatically positive and non-zero. Since x_j>x_r for j>r, dividing by X_i does not alter the inertia. By induction the matrix of order n is positive definite exactly when the first n parameters are defined and |alpha_r|<1. This is a finite algebraic identity, without analytic extension hypotheses.

## 3. Case A=32 and orders up to six, certified exactly

The file `tools/power_fixed_grid_003.py` uses only integers and `fractions.Fraction` for the proof. It calls no numerical special functions nor floating-point arithmetic to certify. The six parameters satisfy the following intervals, with rational endpoints of denominator 10^20:

| r | lower numerator | upper numerator |
|---|---:|---:|
|0|0|0|
|1|51259972990094569363|51259972990094569364|
|2|-25992254732307031752|-25992254732307031751|
|3|31593841033126355467|31593841033126355468|
|4|-25282748230749984903|-25282748230749984902|
|5|29837716612495345653|29837716612495345654|

All are strictly in (-1,1). Independently, interval LDL elimination gives these pivots, with endpoints of denominator 10^30:

| r | lower numerator | upper numerator |
|---|---:|---:|
|0|27353961447421353405359957407|27353961447421353405359957408|
|1|4849334253718313144169652|4849334253718313144169653|
|2|3982421698012363219073|3982421698012363219074|
|3|6513628495257110139|6513628495257110140|
|4|18108703084109592|18108703084109593|
|5|70566563152624|70566563152625|

In particular P3 is proved for A=32,h=1; the third pivot is greater than 3.982421698e-9. The sign is also proved for every real mixture of the six powers X^-32,...,X^-37. It is not a merely numerical statement: each interval is rational and derives from series with remainder.

### Sources of the intervals

* log x: reduce x to [1,2] via powers of two; use 120 terms of 2 atanh((x-1)/(x+1)); remainder <=2t^241/[241(1-t²)].
* pi: Machin's formula 16atan(1/5)-4atan(1/239), 100 alternating terms, error of the next term.
* gamma: H_1000-log1000-1/2000+Σ_{k=1}^{12}B_{2k}/(2k1000^{2k}); error in absolute value <=|B_26|/(26*1000^26), by the Euler–Maclaurin remainder for the digamma function. B_26=8553103/6 is used.
* integer/half-integer psi: psi(m)=H_{m-1}-gamma, psi(m+1/2)=-gamma-2log2+2Σ_{k=1}^m1/(2k-1).
* zeta and zeta': sum n<=50 and bound the tails by the integrals of x^-a and (log x)x^-a; they are decreasing in that range. Thus the certification needs no prime tables nor Λ.
* Each operation rounds the endpoints outward to multiples of 10^-60. The program prints only rational intervals as final certificate.

Reproducible command: `python3 03-research/phase-211-sign-sandbox/tools/power_fixed_grid_003.py`.

## 4. Falsifier: all pairs and monotonicity do NOT suffice for three

POWER_CONE_001 cannot be extrapolated via the lemma «L increasing and L(s)/s decreasing imply sign at every order». Consider the three sites and rational values

    s=(1,5/3,3), L=(1,3/2,121/79).

L increases strictly and L/s decreases strictly; hence each pair passes exactly the criterion of POWER_CONE_001. The complete matrix is

    [1,       15/16,      50/79;
     15/16,   9/10,       1437/2212;
     50/79,   1437/2212,  121/237].

Its three principal minors of order two are 27/1280, 2059/18723 and 916539/24464720, all positive. However

    det K=-332001/391435520<0.

In elimination coordinates, x=(0,1/4,1/2), q=(0,1/5,21/100), alpha_1=4/5 but alpha_2=-665/332, outside the allowed interval. It is an algebraic falsifier of the step from pairs to triples, NOT of the datum L of the paper.

## 5. Exact residue and progress criterion

The new concrete objective is to control (E) for the real values L(32+j), proving |alpha_r|<=1 for all r. The six verifications do not prove an alternation law nor a uniform bound 0.6; they only show the six declared steps. The recurrence keeps all the arithmetic datum, but a sign remainder that is preserved when applying it has not yet been obtained. Every uniform statement requires that new piece. The two-point hypothesis alone is explicitly falsified by §4.
