# E73.285 - Gauged frequency weight audit

Date: 2026-07-14.

## 1. Purpose

E73.284 reduced the exact moment freedom to constant gauges:

```text
W'_omega=W_omega-alpha_L,
V'_omega=V_omega-beta_L.
```

E73.285 probes the gauged Gamma-prime frequency weights and their pairing
with exact APR packet coefficients:

```text
sum c_omega W'_omega + sum l_omega V'_omega.
```

## 2. Method

For each frequency in the exact support

```text
omega in {+-d_n},
```

the script evaluates the Gamma-prime functional on basis functions:

```text
W_omega = F_L[e^(iomega y)],
V_omega = F_L[y e^(iomega y)].
```

Then it subtracts constant gauges:

```text
W'=W-mean(W),
V'=V-mean(V),
```

which is legitimate because E73.236 proved

```text
sum c_omega=sum l_omega=0.
```

## 3. Result

The gauged weights are not small:

```text
||W'|| ~ L^(1.3--1.5),
||V'|| ~ L^(2.0--2.2).
```

They are also not smooth in a naive adjacent-frequency sense:

```text
rough(W'), rough(V') ~ 1.
```

Thus `GAUGE-FREQ-DIV` cannot come from small quotient weights.

The important signal is different.  The two block pairings are large but
nearly opposite:

```text
pairW = sum c_omega W'_omega,
pairV = sum l_omega V'_omega,
|pairW+pairV|/(|pairW|+|pairV|) ~ 1e-12--1e-15.
```

So the cancellation lives between the constant and linear frequency blocks
`c` and `l`.

## 4. Numerical caution

The column `directErrB` shows that this reconstruction of individual weights
does not resolve the final APR center:

```text
directErrB is often comparable to centerB.
```

This is not surprising: the basis-weight evaluation uses quadrature-level
functionals on individual modes, and then subtracts two large block pairings.
The subtraction is far below the absolute scale of the reconstructed weights.

Therefore E73.285 should be read as a structural diagnostic, not an interval
certificate for the final center.

## 5. Corrected theorem target

The finite theorem should now be sharpened from generic `GAUGE-FREQ-DIV` to a
block cancellation statement:

```text
BLOCK-FREQ-DIV:
sum c_omega W'_omega
= - sum l_omega V'_omega + O_M(L^(-M)).
```

Equivalently, the coefficient pair `(c,l)` from

```text
B(y)=sum c_omega e^(iomega y)+y sum l_omega e^(iomega y)
```

must satisfy a signed relation between the constant-mode and linear-mode
Gamma-prime weights.

This is stronger and more precise than saying the whole coefficient vector
lies in a rapid kernel.

## 6. Next exact requirement

The next step must derive exact formulas for the weights `W_omega,V_omega`
with enough precision to survive the block cancellation.  Quadrature-defined
basis weights are not adequate.  The candidates are:

```text
1. closed digamma/Bernoulli formulas for W_omega,V_omega;
2. exact prime sums for the finite Euler part;
3. an analytic identity relating W'_omega and V'_omega so that the block
   cancellation follows from a relation between c and l.
```

## 7. Status

```text
tested: gauged frequency weights and c/l block pairings;
rejected: small or smooth quotient-weight explanation;
identified: FREQ-DIV is c/l block cancellation;
open: derive exact W,V formulas and prove BLOCK-FREQ-DIV.
```
