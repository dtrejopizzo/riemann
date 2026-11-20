# Audit108 — correlated polynomial determinant

Status: **DESIGN AND LITERAL APPROVED; fixed run INCONCLUSIVE, independently reproduced.** Source:`POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md`. The difference relative to107 is the algebraic order of evaluation, not increasing parameters after a result.107 remains INCONCLUSIVE without falsifier. Papers untouched.

The modules107 remain intact and must be verified by hash before import. The builder keeps the errors of moments, a and modes in interval coefficients. Forming all24 products as polynomials and not truncating them encloses the polynomial determinant of truncated true coefficients, preserving the common variable lambda. No favourable correlation between coefficient errors is assumed.

The entry bound B=2^62 and per-entry remainder epsilon=2^-400 are those audited in107. For the polynomials of true coefficients, their values differ from the exact functions by epsilon, so they have modulus<B+1. Telescoping the24 products pays96epsilon(B+1)^3<2^-200. It is not necessary to claim that any width of an interval evaluation of the polynomial is less than B+1; only that the true polynomial contained in the enclosure satisfies that bound. Interval arithmetic separately pays rounding and coefficients.

Taylor shift at a dyadic centre: each coefficient is outward and ALL degrees are kept. Lower=b0.lower−sumabs(bj).upper*h^j−2^-200 and the analogous upper give an enclosure for the whole cell. They are not samples. Degree2048 is a safe maximum; the code must not cut uncertain coefficients nor treat balls containing0 as exactly zero coefficients.

The algorithm keeps the limits of107 and complete coverage before PASS; origin not PASS prevents REST. The budget may turn out INCONCLUSIVE or costly; it promises neither sign nor viability. Before running, a literal reading and local verification of the polynomial shift API are required, together with hashes. No theta evaluation was run in this audit.

## Literal108 and API

Read in full `tools/power_mixed_four_polynomial_108_verify.py`. Hashes107 are checked before import, the modules are intact and the import does not evaluate theta. Qpoly=−phi−2lambda phi' and its derivatives are correct.24 permutations are formed with complete products; degree is not truncated and uncertain coefficients are not removed.

Verified the local composition API on a rational toy 1+2x+3x², shifted byx+.5: the coefficient balls contain(2.75,5,3). Structural equality of arb_poly was not used as proof; coefficient-wise containment was. Theta was not evaluated. The literal shifts with exact dyadic centre and sums all degrees; the outward radius includes2^-200 before deciding the sign. Left-first DFS/budgets/exact coverage1/4 kept; REST107 runs only after origin PASS108. Literal review approved before data; a single process is run, with no PASS promise.

## Result and diagnosis without new evaluations

Runs 82660 and 28564 ended exit2/INCONCLUSIVE: degree2042,15 evaluations,4 accepted, coverage141/8192,depth10 at[141/8192,1129/65536],det[+/−2.04e−4]. REST not executed. Driver hash eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a and107 intact, with separate logs.

The replica used sys.setprofile to record ONLY locals existing at the return of evaluate: left,right,coefficients[0],radius and returned value in the15 cells. There were no new evaluations of theta or of polynomials. In the last enclosure coefficient0=[+/−1.79e−4], while the additional radius≈2.4560e−5. The central coefficient itself already contains0; the whole width cannot be attributed to variation within the cell. Nor does this decide whether there is a real zero or which uncertainty source dominates in the construction. In the widest intervals very large balls appear; they only describe enclosures, not certified real magnitude.

The literal stopped correctly without promoting partial coverage. It is neither a falsifier nor a mathematical obstruction; no new W/T/allorders. Parameters were not edited after data.
