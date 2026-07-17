# E72.259 -- Rational Bernstein LM8 certificate

**Purpose.** Give an exact rational interval certificate for the strict homogeneous LM8 majorants from
E72.258.

The coefficients are the six-decimal rational coefficients of E72.258, interpreted exactly as
rationals with denominator `10^6`. The certificate proves the four univariate inequalities:

```text
R0(u) >= 1       for -1 <= u <= 0,
R0(u) >= 0.09    for  0 <= u <= 1,
R1(u) >= 1       for -1 <= u <= 0,
R1(u) >= 0.16    for  0 <= u <= 1.
```

Since `P_j(u)=u^2R_j(u)`, this proves the required LM8 majorants while preserving

```text
P_j(0)=P_j'(0)=0.
```

Thus the dimensional drift from E72.247 is absent.

## Method

For each rational polynomial and interval `[a,b]`, the script:

1. changes variables exactly to `[0,1]`;
2. converts the power-basis coefficients to Bernstein coefficients exactly;
3. recursively bisects by exact De Casteljau subdivision;
4. accepts a subinterval only when all Bernstein coefficients are non-negative.

All arithmetic is done with Python `Fraction`. No floating root computation is used in the
certificate.

## Output

```text
E72.259 rational Bernstein LM8 certificate
All coefficients are exact rationals from E72.258 with denominator 10^6.
R0-1 on [-1,0]: PASS boxes=15 depth=5 terminal_min_bern=+1.990000000000e-04 (199/1000000)
R0-0.09 on [0,1]: PASS boxes=15 depth=6 terminal_min_bern=+3.455281238556e-04 (181156249/524288000000)
R1-1 on [-1,0]: PASS boxes=11 depth=3 terminal_min_bern=+1.402327439444e-04 (257328207/1835008000000)
R1-0.16 on [0,1]: PASS boxes=11 depth=5 terminal_min_bern=+6.859011845220e-04 (82485848362667/120259084288000000)
overall PASS
```

The `terminal_min_bern` value is a certified lower bound over the accepted terminal Bernstein boxes.

## Consequence

The LM8 majorant sublemma now has a clean proof-facing version:

```text
P0(u)=u^2R0(u),   P1(u)=u^2R1(u),
```

with rational coefficients, exact interval majorization, and no constant trace term.

This closes the **majorant algebra** part of LM8. It does not yet prove the uniform model moment
bounds for the operators `K0,K1`; those still belong to the Green/coercivity and low-dimensional
dominance package.
