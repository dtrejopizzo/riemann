# Revised state of the power route — round 003

The previous turn produced verifiable progress: finite-order theorems and a bridge. This round certifies the fixed family up to order six and refutes a proposed scalar induction. The goal remains active, without closure of the sign.

## Recorded results

- POWER_BRIDGE_002 and POWER_AUDIT_002: full bridge reviewed. Positivity of all leading matrices K_ij=(L(32+i)+L(32+j))/(63+i+j) suffices. Any translated compact test is represented by finite Möbius inversion and approximated in form norm by the fixed ladder.
- POWER_FIXED_GRID_003: all orders 1–6 certified by rational intervals. The script tools/power_fixed_grid_003.py was re-run twice independently with matching output. It includes an exact Schur transformation; it does not assume that the six-parameter pattern extends.
- POWER_POLYNOMIAL_003: Jacobi coordinates and exact dilations; the dilations are neither self-adjoint nor positive contractions in that metric. Identities, not a uniform sign.
- POWER_SCHUR_003: F(z)=(z²-z+10)/10 has F'>0 and F/z decreasing on [1,3]; all its pairs pass, but its triple 1,2,3 has determinant -13/270000. Counterexample to preservation from those two properties. The piecewise version of §7 adds concavity and also fails. No falsifier is of the arithmetic datum.

## What is missing

P3 for all A>=32,h>0 is not proved: there is a high range and the exact case A32,h1 (included in six powers). There is also no uniform control in the order. The bridge is resolved. The union of high ranges u>=2^{40n} is not dense, with a quantitative concentration proof: do not extrapolate that family.

## Next authorised trial

Attack the confluent case (h→0) with a stable basis of exponentials times polynomials and audit whether moving the rates upward preserves the archimedean minimum. That monotonicity is NOT proved. A counterexample to it would force a pivot, not refute the sign. Avoid the monomial Gram near confluence: it produces false negatives through ill-conditioning.

Status: OPEN. Papers untouched. There is no external blockage; substantive mathematical work remains.
